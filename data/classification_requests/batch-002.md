# Classification request: batch 2 of 53 (40 records, IC-0441 to IC-0480)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-002-reply.json`.

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

## IC-0441: Sling Blade

- Title: Sling Blade
- Author (byline): Billy Bob Thornton
- Work: Not specified
- Publisher: Miramax
- Publication date as stated: December 1996
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: KARL, MARSHA
- Teaser before the introduction: No
- Spoken words (computed): 973
- Already set (do not supply): none

### Source block (context only)

```text
Author: Billy Bob Thornton
ISBN: 978-0786882502
Publisher: Miramax
Date (Month/Year): December 1996
```

### Introduction (context only: never use it for content warnings)

```text
Sling Blade, winner of the 1996 Academy Award for best screenplay, is the powerful story of Karl Childers, a retarded man who is released from a mental institution where he has been incarcerated for twenty-five years for a murder committed when he was a child. In this scene, Karl is interviewed by a high school reporter about his release, and Karl relates the events surrounding the murder of his mother and her lover with a . . . Sling Blade by Billy Bob Thornton.
```

### Performance text (classify this)

```text
Marsha is staring at Karl. Karl, still breathing and rubbing his palms, starts to speak. His voice is low and raspy, but not just low and raspy; strange.

KARL: Well, I reckon what you're a wanting to know is what I'm doing in here. I reckon the reason I'm in here is cause I killed somebody. But I reckon what you was a wanting to know is how come me to kill somebody. Well, I reckon I'll start at the front and tell you. (pause; heavy breathing)

I lived most of my life out behind my mother and father's house in a little old shed that my daddy'd built for me. They didn't too much want me up there in the house with the rest of 'em. I mostly just set around out there in the shed all the time a lookin' at the ground. It didn't have no floor but I had me a hole dug out to lay down in and a quilt or two that I put down there. (pause; more breathing)

My daddy was a hard workin' man most of his life, not that I can say the same fer myself. I most just set around the shed and tinkered around with a lawnmower or two and went to school off and on from time to time but the children there made quite a bit of sport of me, made fun of me quite a bit. Some of 'em roughed me up sometimes so mostly I stayed out back there in the shed. My daddy worked down at the sawmill there, down there at the planer mill for an old man named Dixon. Old man Dixon was a very cruel feller, he didn't treat his employees very well, didn't pay 'em much of a wage, didn't pay my daddy much of a wage, just barely enough to get by on. But I reckon he got by all right, they come out one or the other of 'em, usually my mother, and fed me pretty regular. At least I know he made enough for me to have mustard and biscuits three or four times a week. Old man Dixon had a boy named Jesse Dixon. Jesse was really more cruel than his daddy. He made quite a bit of sport of me and takened advantage of the little girls around the neighborhood quite a bit. (pause)

He used to say my mother was a very pretty woman. He said it quite a bit from time to time, when I was at the school house. Well, I reckon you want me to get on and tell you what happened so I reckon I'll tell you. I was settin' out in the shed one evenin' not doin' too much, just kindly starin' at the wall and a waitin' fer my mother to come out and give me my Bible lesson and I heared a commotion up in the house there so I got up and run up on the screened-in porch there to see what was a goin' on, and I looked in the kitchen window and I seen my mother a layin' there on the floor without any clothes on. (pause; breathing)

And seen Jesse Dixon a layin' on top of her having his way with her. (pause)

Well, I just seen red. I picked up a kaiser blade that was a layin' there by the screen door, some folks calls it a sling blade, I call it a kaiser blade. It's just a long handle like a axe handle with a long blade on it that's shaped kind of like a banana. Sharp on one edge and dull on the other. It's what the highway boys use to cut down weeds and whatnot. I went in the kitchen there and I hit Jesse Dixon up side the head with it and knocked him off my mother. I reckon that didn't quite satisfy me so I hit him again in the neck with the sharp edge and just plumb near cut his head off. Killed him. Well, my mother, she jumped up from there and started yellin', "What did you kill Jesse for? What did you kill Jesse for?" (pause; intense breathing)

Well, come to find out my mother didn't really mind what Jesse was a doin' to her. I reckon that made me madder than what Jesse had made me. I takened the kaiser blade, some folks calls it a sling blade, I call it a kaiser blade and hit my mother up side the head with it an' killed her. (long pause; breathing)

Some folks has asked me if I had it to do over again would I do the same thing. I don't know, I reckon I would. Anyhow, they seen fit to put me in here and here I've been for a great long while. I've learned to read some; took me four years to read the Bible. I reckon I understand a good deal of it. It wasn't what I expected in a lot of places. I've slept in a good bed for a great long while. They've seen fit to put me out now. They tell me they're a settin' me free today. Anyhow, I reckon that's all you need to know. If you want any more details I reckon I can tell 'em to you. I don't know if that's enough for your newspaper or not.

Suddenly Marsha speaks from the darkness.

MARSHA: Will you ever kill anybody again, Karl? This seems to startle the very room itself Woolridge motions for Marsha to shut up and Karl stops still. Very still. He breathes hard for a moment then starts to calm down. He seems almost at ease. He slowly looks up. From Karl's point of view we barely see Marsha's face in the dim light. Karl is looking straight at Marsha.

KARL: (slowly) I don't reckon I got no reason to kill nobody.
```

---

## IC-0442: Slow Dance on the Killing Ground

- Title: Slow Dance on the Killing Ground
- Author (byline): William Hanley
- Work: Not specified
- Publisher: Dramatists Play Service, Inc
- Publication date as stated: Jan 1998
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: RANDALL, MR. GLAS
- Teaser before the introduction: Yes
- Spoken words (computed): 1776
- Already set (do not supply): none

### Source block (context only)

```text
Author: William Hanley
ISBN: 978-0822210436
Publisher: Dramatists Play Service, Inc
Date: Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
Meet Randall, a young black man on the run from the reality of his own creation. And Mr. Glas, struggling to deal with an impossible choice made decades ago. Both dance around reality . . . Always on guard . . . afraid to face their personal truths, let alone share them with others. They hide behind the images they have chosen to show to the world. This night, however, a chance meeting between strangers offers a safe haven for the unburdening of two troubled souls. The music has begun . . . it is time for this

Slow Dance on the Killing Ground by William Handley
```

### Performance text (classify this)

```text
RANDALL: Hey daddy! Didn’t see you up there! Pretty neat, yes indeedy!

MR. GLAS: What can I do for you?

RANDALL: I mean, what can you do for me. The possibilities are endless, know what I mean? Right? But we start with somethin’ easy. Gimme a . . . gimme an egg cream. You of European abstraction. . .

MR. GLAS: I beg your pardon?

RANDALL: Your accent. Originally you speak another tongue, I mean you come from across the sea, right?

MR. GLAS: Oh, Ex-traction

RANDALL: (Turns to Glas) Sir?

MR. GLAS: You said abstraction. The word is extraction. European extraction.

RANDALL: Oh, Yeah. . . well, I stand corrected, daddy.

MR. GLAS: I don’t see you around here before, sonny.

RANDALL: Do me a little favor; don’t call me sonny

MR. GLAS: What’s your name?

RANDALL: Randall. What’s yours?

MR. GLAS: Glas.

RANDALL: What kinda name is that, Glas?

MR. GLAS: German for the Glas with two esses.

RANDALL: Oh, I dig. German. I like that. Glas with one s. And now that my attention been called to it, and you don’t mind me sayin’, but the glass with two esses here could use a little washin’, I do believe. You can’s hardly even see through it. It donwnright dirty, that glass with two esses.

MR. GLAS: There’s nothing out there I particularly want to see.

RANDALL: You don’t like the nature of things out there particularly?

MR. GLAS: Exactly.

RANDALL: Well now, you see? I had a feelin’, I just knew we was brothers under the skin, somehow. I hasten to repeat, under the skin, no offense intended, no indeed, sir. But I know exactly what you mean, exactly! I mean, it is grotesque out there, ain’t it, now? It is . . . bizarre! You know what it is out there, daddy? You know? That is killing ground out there. I mean that’s No Mans Land out there, daddy! That somebody else’s turf, a regular mine field, you gotta step carefully, they kill you out there, know what I mean?

MR. GLAS: Not exactly

RANDALL: Butcher shop. It a regular butcher shop out there. You know what happened out there just last year alone? What happened out the- and I quote – what happened out there was four hundred and eighty three homicides! “Contrary to public impression, most homicides are spontaneous and are committed in the home; they are not the result of gangland reprisals but of family disputes. Oh, man, man… (picks up newspaper and looks at is, reading an article.. meanwhile Glas is just staring at Randal, perplexed.) O see where they really hung his ass, hah? This here Nazi cat, I mean. Them Jews really hung his ass, after all.

MR. GLAS: Yeah, sure.

RANDALL: I do perceive you ain’t got much sympathy for some of the various and sundry dilemmas currently facin’ mankind, then?

MR. GLAS: No. . . What are you running away from? When you came in here: what were you running away from?

RANDALL: Where’d you get an idea like that, baby? Where in the world?

MR. GLAS: You got trouble out there, don’t bring it in here.

RANDALL: What’d you have in mind I was runnin’ away from?

MR. GLAS: How would I know?

RANDALL: True, ‘course there’s a lotta possibilities. Lemme see, now. . . could be I knocked over my friendly neighborhood grocery store to get me an apple and a little loose change?. . . Or perhaps I am a remnant of one of our local altercations commonly known as the gang rumble, in which several children have been slain, slain on the field of battle?. . . That don’t appeal to you neither? Well, lemmee see, now… could be I just recently committed a criminal assault on a white lady of middle age in the dark deserted end of a subway station platform?. . . No? Or perhaps, perhaps – this a good one – perhaps I just up and done away with my momma, stabbin’ her numerous times about the breast and abdomen with an ice pick.

MR. GLAS: What were you running away from?

RANDALL: You the persistent type though, ain’t you daddy. Ain’t always a good idea to be too persistent, though, you know?. . . I mean, … What is Truth, said Jesting Pilate and would not stay for an answer. You know who said that? You know? Francis Bacon was the one who said it.

MR. GLAS: I don’t like that kinda talk!

RANDALL: What kinda talk is that, daddy?

MR. GLAS: And stop calling me Daddy!

RANDALL: No offense intended, sir, I assure you. It is definitely not my intention to impugn the purity of you ancestral heritage, seein’ as how I heard that a lotta you German folks was unusually sensitive to that topic at one time in the not-to-distant past. Course, you bein’ a Jew and all…

MR. GLAS: I’m not a Jew

RANDALL: Here I been goin’ on the false assumption that you was. Is. A Jewish man. That bein’ the case, it been hard for me to reconcile the fact that you ain’t been givin’ a shit one way or the other about old Aldolf here, swayin’ gently to and fro, as they say, with a broken neck, ruptured larynx, deceased. But you not bein’ a Jew, I now comprehend totally. Your indifference.

MR. GLAS: You think only Jews care?

RANDALL: They do seem to be the ones most upset and distraught by the matter, yeah. I mean they ‘as the ones who hung him. Seem to me somewhat bloodthirsty.

MR. GLAS: What do you know about it?

RANDALL: What I read in the newspapers, baby.

MR. GLAS: There’s more to know than you read in the newspapers, believe me.

RANDALL: What do you know about it?

MR. GLAS: I know! I know!

RANDALL: Of course you do, I know that. But what exactly? Your turn to speak, Mister Glas…

MR. GLAS: This man . . . do you know what they say? They say that when they arrested his he appeared to be relieved. Not frightened. Not defiant. They say he appeared to be – relieved!. . . Do you know why? I’ll tell you why. Because all these years he knew, you see. He waited, and he knew that sooner or later it would happed: the discovery that would mean his judgment and his death. And the anticipation pf a blow is always, somehow, more terrible than the blow itself when it finally comes. So one can understand his relief. When the blow finally came. But I had a wife who was a Jew. And a son who was a Jew. Nineteen thirty eight, a man might as well have been a Jew himself: the Nazis made no distinctions. And, of course, to have been a Jew then was to wait for the day they opened your door and took you away. They opened so many doors… so many doors… and came out with Jews in their fists… Most men, you know, most men can live all of their lives with the conviction that they have honor, and they can go to their graves with that conviction without ever having been put to the test of it. I envy them, the ones who escape the test. Not me. In the summer of nineteen thirty eight I had my test, my choice to make: to wait until I was taken to a concentration camp as a Jew with my Jewish wife and my Jewish son… or to live as a Communist and fight for my country, my Germany, against the Nazis. And, to save my life for that fight, I abandoned them, my wife and my child, in the middle of the night without a word. I went to another city, I took another name. For nearly a year I carried freight between Hamburg and Cologne: chemicals, machinery, armaments. And then I was transferred to another run, to a place called Mauthausen, and the freight was people. … Three trips I made in two months and I carried hundreds and hundreds of people, of Jews, to the concentration camp at Mauthausen… Until August, nineteen thirty nine, and Stalin made his pact with Hitler. Communism embraced Nazism, my god kissed Satan and called him friend. In that moment there was a new truth: that I had abandoned my wife and son to the wolves and saved myself for nothing. For nothing! And I went back . . . and in the house the windows were smashed. . . and the door was open. . . and they were gone. I left Germany them. . . I know. . . For this man. . . the waiting is over. He committed a crime for which a punishment has been named, you see. But me. Who will judge me? Who will condemn me, and by what law?

RANDALL: You stand accused, Mister Glas, sir!

MR. GLAS: What, what!?!

RANDALL: Accused, yes, of continuing to live. . . Hear ye! Hear ye! God bless all here! We are gathered together here for certain special and particular purposes, to wit: to determine the guilt or innocence of one, Glas, first name unknown and immaterial, brought forward here and now before this here qualified tri-bunal with the view in mind to settin’ his heretofore troubled conscience at rest concernin’ a certain matter, to wit: his need to be judged. How do you plead? Guilty or not guilty?

MR. GLAS: Guilty

RANDALL: Done, then. (takes a gun from his coat, puts it to Glas’s temple and pulls the trigger)

MR. GLAS: It should have been loaded, hah?

RANDALL: No sword of justice will pierce your heart, Mister Glas (pause) Glas, if I were dying right now, would you save my life?

MR. GLAS: I don’t know. Maybe, if I could. Why?

RANDALL: Would you die for me? Would you go that far?

MR. GLAS: No. There is only one Jesus Christ, sonny. (pause) Randall? What have you done? Tell me Randall. It’s time. You owe it to me Randall.

RANDALL: Do I. Yes I suppose I do, all things considered, mm, hm (long pause)

MR. GLAS: Go on, Randall.

RANDALL: Up the stairs, first. One flight, two flights, three flights, four. Through the door. Into the room. Dark. Sit. Wait. Noises in the bedroom, familiar noises in the bedroom. Creak, moan. Creak, moan. Creak, moan. Momma moaning, giving value for money. Wait. Quiet. Dark. Clock, tickticktick, clock, tickticktick. Fire engine. Clock, tickticktick. He comes out of the bedroom, head down, faceless man, buttoning, shoelaces clicking on the linoleum. Out the door. Slam. Quiet. Wait. Bedspring creaks. Match strikes in the bedroom. Exhalation. Don’t smoke in the bed, momma: everybody says. Randall stands up. Into the bedroom. Mama on the bed, black on white. Screams. Covers up. No words. Screams when the knife comes down. Screams when the knife comes down. Screams when the knife goes down. Many times. Knife breaks. Ice-pick. Small round holes in the white sheet pumping blood. No screams no more . . . no momma no more, no momma no more!

MR. GLAS: They’ll catch you, Randall, they’ll kill you. I can’t save you. A little bit, maybe. But finally – no.

RANDALL: Why don’t you see. . . I must die, in violence, because of what I am and because of what I have done. Just as you must live, without violence, because of what you are and what you have done. . . We choose the dark streets up which we walk. We choose them. And if we are guilty of the denial of life, who is there to save us from that. . . but ourselves?
```

---

## IC-0443: So, I Killed a Few People

- Title: So, I Killed a Few People
- Author (byline): Gary Rudoren and David Summers
- Work: Plays and Playwrights for the New Millennium
- Publisher: The New York Theatre Experience
- Publication date as stated: Feb 2000
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: ARCHIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1650
- Already set (do not supply): none

### Source block (context only)

```text
Author: Gary Rudoren and David Summers
Book: Plays and Playwrights for the New Millennium
ISBN: 978-0967023410
Publisher: The New York Theatre Experience
Date (Month/Year): Feb 2000
```

### Introduction (context only: never use it for content warnings)

```text
"Go for the heart, just don't eat it," says Archie Nunn, recalling a friend's counsel—pretty sage advice for someone with nothing in the world but an orange jumpsuit, a tape recorder, a date with the electric chair, and a solo show on death row. A legendary killer, Nunn has one last wish: to heap abuse on the Disney Corporation, which he blames for his problems, and tell of his twin obsessions with serial television and serial murder. So I Killed a Few People by Gary Rudoren and David Summers
```

### Performance text (classify this)

```text
ARCHIE: I had to take a dump during my mother’s funeral. This is my earliest memory. I think. To be truthful, I remember this mostly because that’s the first question I get asked by all the head shrinkers in here. Friendly fellows those doctors are…apparently before the State fries my ass they want to get to know me as best they can . . .

(As aside in woman’s voice.) “Bob, when’s he going to talk about the killing and the blood and the gore?”

That’s what you came for isn’t it?? Isn’t it? Hey…How often do you get this close to a so-called serial killer? Most people. . . never. Some people-almost never. . . And in my case. . . eight people-once. . . actually it’s a few more. . . but that’s all they caught me on. . . I’m leaving the rest of them out there for kind of an Easter egg hunt. . . Welcome to my freak show! My court-approved freak show!!

I could go into a long involved story about the trials and tribulations of my trials. . . and tribulations. . . but let’s cut to the chase. . . In the majority opinion of the Supreme Court of the United States in Archie Nunn vs. the State of Florida, Justice Souter wrote that I was entitled to perform my life’s story as an expression of my free speech rights and was a valid request that the State had to honor…the only stipulations was that I could not use the real names of any of the victims because, even though they were dead, I’d be violating their right to privacy. . . apparently killing them was one thing, but I’d be in real trouble if I was going to violate their right to privacy. . . So here I am. . . one week to the fryer. . .

(As aside in woman’s voice.) ”Bob, we know he’s gonna fry, but I want to hear about the killing and the blood and the gore.”

Well hold onto your tits. . . because as they said in Munchkinland, “We’ll be there shortly.”

ARCHIE: I was born outside of the Jewish part of Atlanta, but when I was nine we moved to Orlando. . . my Dad worked for the company. . . he’s an electrical engineer for Disney World…currently he’s the head electrician for “Frontierland” . . . he’s a nice guy my Dad is…always gets along with everyone…

I used to watch the movies and the TV shows and buy the image…and there is no greater problem in our society today than the effect that Disney is having on our children.

I’ve boiled down the entire Disney credo to two messages: One . . . all inanimate objects have the ability to sing. . . And Two . . . if you’re ugly, a cripple or a freak, good things will happen to you. If you’re the beast you’ll find a beauty.

If you’re a hunchback, some gypsy woman with big cartoon tits will want to be your friend. And if you’re a dwarf, a beautiful woman will find you and your freakish friends even if you live in the middle of a frickin’ forest. When I was growing up I was an outcast, but I didn’t know it because I was able to walk around with big mouse ears and huge foam hands and think that was okay just because Disney said so . . .

Disney claims to be a friend of the family, but that’s just part of the conspiracy…if Disney really wants to help little kids . . . if they really want to help all little kids . . . they can show them movies and television shows that are more real . . . send them out a real message about life . . . and that is this: If you’re an ugly, crippled freak, here’s what’s going to happen to you: Nothing. People will hate you. Mommies and Daddies don’t like cripples. Gargoyles won’t be your friends. Restaurants don’t serve ugly people. Nobody will take your checks. You better live on an island. You should kill yourself. You should kill those that don’t like you.

One day these little kids are going to grow up and learn the realities of life and figure out all this stuff and then they are going to snap. . . they’re gonna lose it. . . and then BLAM!! DISNEY HAS CREATED MORE SERIAL KILLERS THAN THE ENTIRE STATE OF WISCONSIN!!

I guess if I have any regrets, it’s that I’ve hurt my dad . . .like I said . . .he’s a good man…and he ended up with a serial killer for a son . . . not a ringing endorsement of fatherhood . . . he’s a good dad though. . . I don’t blame him and no one else should. . . but. . . he is in a little bit of denial about my death. . . he’s never asked me about the killings or why or. . . anything. . .

So he came by to say goodbye and we’re sitting there. . . a little awkward. . . so I break the ice. . . I say, “Hey dad. . . they told me the chair is the new 10,000 model from Westinghouse. . . “

This perked him up a little. . . He started chatting about the advanced technology used to make that chair and how it was a quality piece of equipment. . . I told him about how they wet down my head to get better connections and he thought that was a good way to ensure the flow of electricity to my brain. . . by the end of the discussion he had fully explained the technical aspects of how I was going to die by electrocution. . . in his eyes this might have been the birds and bees discussion that we never had. . . He got up to leave. . . we kind of looked at each other…and his last words to me were. . . “I know Archie. . . I’ve always known” . . . then he just walked out. . . and I just stared at him and made a slight wave. . . it was after he couldn’t see me. . . and I. . .

Right before they pull the switch, they ask you for your last words. I think I’ll tell them about the only time I’ve ever killed out of genuine anger. . . the only time I lost something I truly cared about. . . it was my first time. . . my first killing.

I’ve told you my dad was a good man. . . but while I was growing up he didn’t have much time for me. . . as for my mother. . . being happy to mom meant vodka martinis for breakfast lunch and dinner with bourbon snacks throughout the day. . . well, let’s just say that I was raised by television. . .

TV was my mother, father, priest, friend. . . you have to admit how valuable television is. . . it’s got comedy, drama, news, history. . . when I did want to be alone, all I had to do was turn it off and all my little friends would go away . . . and be there waiting for me when I was ready to get together again. . . and the best thing. . . they’re never gonna be too tired to play or too busy. . . or too drunk. . .

I thought things were going okay in life. . . in general, but then there was this one bitch. . . I don’t know if she was jealous or what, but she was always trying to come between me and my friends. . . she’d make fun of me because we were all so close. . . She’d whine about how I was losing touch with “reality: . . . I explained to her that television was as real as anything else. . . and that a lot of my friends were there. . . she had no friends. . . she grew more jealous of me and my friends. . .

There was this one day. . . we had just had a real blow-out of a fight. . . she was drinking. . . and I just went into my room and turned on the TV. . . when I hear this heavy breathing in the doorway behind me. . . and I turn around and she’s standing there. . . panting. . . sweating. . . and holding a claw-hammer in her hand. . .

“What do you plan on doing with that hammer?” I asked.

“Something I should have done a long time ago. . . “ she said . . .

She had lost it. . . I wasn’t really afraid. . . she was puny. . . I knew I could take her. . . but then I realized that I was not the object of her anger. . . I leaped at her, but it was too late. . . she had put the hammer through my friend. . . there was an explosion of glass and sparks and then they were gone. . . all gone.

And she screamed, “Now maybe you’ll talk to me!” . . . and through my rage. . . I was seething. . . in the calmest voice I could muster said, “It’ll be okay, let’s just clean up the mess.” This confused her, she was ready for a knock-down-drag-out fight . . . she handed me the hammer and turned to get the dustpan . .

. and when she turned, I dug the claw of the hammer into the back of her skull. . . and drug her back into the room. . . she started screaming. . . I took the blunt end of the hammer and smashed it in her throat. . . and then she starts really crying. And I can tell she’s trying to manipulate me, you know? Mess with my emotions? Turn my friends against me. . . actually she owed my friends an apology. . . I picked her up and threw her headfirst into the TV and said, “You tell them you’re sorry. . . “

You tell Johnny Carson you’re sorry

Johnny Quest

Tell’m what they’ve won Johnny!

I can’t believe I ate the whole thing!

Lucy, you got some splainin’ to do!

HOGANNN!

This tape will self-destruct in five seconds!

M-I-C…K-E-Y

WHY

WHY

WHY!!!

Then I realized she wasn’t moving anymore . . . I let the body drop. . . it fell out of the TV. . . But the head stayed in. . . I just stared at her . . . It wasn’t as good as television, but I was fascinated by it. . . It was like I was making my own kind of television. . . I liked this show. . . I wanted to see this show again. . .

I stared at her face for a long while . . . a long time. . . I don’t remember much after that. . . except. . . I had to take a dump at her funeral.
```

---

## IC-0444: Soldier with a Secret

- Title: Soldier with a Secret
- Author (byline): George C. Wolfe
- Work: The Colored Museum
- Publisher: Broadway Play Publishers
- Publication date as stated: May 1987
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: JUNIE
- Teaser before the introduction: No
- Spoken words (computed): 710
- Already set (do not supply): none

### Source block (context only)

```text
Author: George Wolfe
Book: The Colored Museum
ISBN: 978-0413179500
Publisher: Broadway Play Publishers
Date (Month/Year): May 1987
```

### Introduction (context only: never use it for content warnings)

```text
The Colored Museum is a series of exhibits in “a museum where the myths and madness of Black Americans are stored. In this exhibit you will meet Junie Robinson, a black combat soldier. You’ll hear him admit that he has killed some of his comrades in arms, but you’ll also hear the reasoning behind his brutality. You see, Junie believes that death in combat is preferable to the pain of oppression.

Soldier with a Secret from The Colored Museum by George C. Wolfe
```

### Performance text (classify this)

```text
Junie Robinson, a black combat soldier is posed on an onyx plinth. He is somewhat dim-witted with an easy-going charm about him.

JUNIE: Pst. Pst. Guess what? I know the secret. The secret to your pain. ‘Course, I didn’t

always know. First I had to die, then come back to life, ‘fore I had the gift.

Ya see the Cappin sent me off up ahead to scout for screamin’ yella bastards. ‘Course, for the life of me I couldn’t understand why they’d be screamin’, seein’ as how we was tryin’ to kill them and they us.

But anyway, I’m off lookin’, when all of a sudden I find myself caught smack dead in the middle of this explosion. This blindin’, burnin’, scaldin’ explosion. Musta been a booby trap or something, ‘cause all around me is fire. Hell, I’m on fire. Like a piece of chicken dropped in a skillet of cracklin’ grease. Why, my flesh was justa peelin’ off my bones.

But then I says to myself, “Junie, if yo’ flesh is on fire, how come you don’t feel no pain!” And I didn’t. I swear as I’m standin’ here, I felt nuthin’. That’s when I sort of put two and tow together and realized I didn’t feel no whole lot of hurtin’ cause I done died.

Well I just picked myself up and walked right on out of that explosion. Hell, once you know you dead, why keep on dyin’, ya know?

So, like I say, I walk right outta that explosion, fully expectin’ to see white clouds. Jesus, and my Mama, only all I saw was more war. Shootin’ goin’ on way off in this direction and that direction. And there, standin’ around, was all the guys. Hubert, J.F., the Cappin. I guess the sound of the explosion must of attracted ‘em, and they all starin’ at me like I’m some kind of ghost.

So I yells to ‘em, “Hey there Hubert! Hey there Cappin!” But they just stare. So I tells ‘em how I’d died and how I guess it wasn’t my time ‘cause here I am, “Fully in the flesh and not a scratch to my bones.” And they still just stare. So I took to starin’ back.

(The expression on Junie’s face slowly turns to horror and disbelief)

Only what I saw . . . well I can’t exactly to this day describe it. But I swear, as sure as they was wearin’ green and holdin’ guns, they was each wearin’ a piece of the future on their faces.

Yeah. All the hurt that was gonna get done to them and they was gonna do to folks was right there clear as day.

I say how J.F., once he got back to Chicago, was gonna get shot dead by this po-lice, and I saw how Hubert was gonna start beatin’ up on his old lady which I didn’t understand, ‘cause all he could do was talk on and on about how much he loved her. Each and every one of ‘em had pain in his future and blood on his path. And God or the Devil one spoke to me and said, “Junie, these colored boys ain’t gonna be the same after this are. They ain’t gonna have no kind of happiness.”

Well right then and there it come to me. The secret to their pain.

Late that night, after the medics done checked me over and found me fit for fightin’, after everybody done settle down for the night, I sneaked over to where Hubert was sleepin’, and with a needle I stole from the medics . . . pst, pst . . . I shot a little air into his veins. The second he died, all the hurtin-to-come just left his face.

Two weeks later I got J.F. and after that Woodrow . . . Jimmy Joe . . . I even spent all night waitin’ by the latrine ‘cause I knew the Cappin always made a late night visit and pst . . . pst . . . I got him.

(Smiling, quite proud of himself) That’s how come I died and come back to life. ‘Cause just like Jesus went around healin’ the sick, I’m supposed to go around healin’ the hurtin’ all these colored boys wearin’ from the war.

Pst, pst. I know the secret. The secret to your pain. The secret to yours, and yours. Pst. Pst. Pst. Pst.
```

---

## IC-0445: A Steady Rain

- Title: A Steady Rain
- Author (byline): Keith Huff
- Work: Not specified
- Publisher: Faber and Faber
- Publication date as stated: Feb 2010
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: DENNY, JOEY
- Teaser before the introduction: Yes
- Spoken words (computed): 1780
- Already set (do not supply): none

### Source block (context only)

```text
Author: Keith Huff
ISBN: 978-0865479364
Publisher: Faber and Faber
Date (Month/Year): Feb 2010
```

### Introduction (context only: never use it for content warnings)

```text
Law enforcement is dangerous work. But these days, the gravest threat to police officers' lives comes not from criminals but from themselves – death by suicide. In a world where toughness is prized, they hesitate to reveal frailties for fear of jeopardizing their careers. Such reluctance becomes especially dangerous with officers who have temporarily lost their shields or been put on modified duty pending investigations that could cost them their careers. Fear of losing reputation and friends is more than enough to drive them over the edge. Denny and Joey, partners and best friends since childhood, are two cops on the edge.

A Steady Rain by Keith Huff.
```

### Performance text (classify this)

```text
Each character speaks only to the audience unless otherwise noted.

DENNY: (Pg 55-56) (To Joey) Think you’d know the eyes of a demon if you saw one? (beat)

JOEY: (To Denny) We didn’t know, Denny. First thing we’ve got to do to face this thing is let ourselves off the hook. We didn’t know.

DENNY: (To Joey) But we should know, Joey. We should know the eyes of a demon when we see one. It’s our job. Otherwise we end up with demons for friends. (beat)

JOEY: (Pg 60) We sat there in that rain for, I don’t know, an hour, longer, not a word, just Denny mumbling under his breath.

DENNY: (To Joey) They want heroes, Joey. Superhuman, that’s what they want us to be. Abel to tell good from evil in a blink. That’s what they want.

JOEY: (Pg 34) [Denny] was my best friend. My partner. Always back to back, me and Den.

DENNY: (Pg 10) I known the guy since kinnygarten.

JOEY: (Pg 64) (remembering) Denny’d make up these games. To pass the time. For nothing, for fun. Denny invented rock tag. He called it Last Man Standing. Plenty of rocks handy for ammo. The object of the game, of course, was to be the last man standing.

DENNY: (Pg 46) Nobody knows this, I virtually brought the guy back from the dead he drank so bad. You know how many times I covered for that guy, signed in for him, covered his beat? He’s like my brother, I love the guy, but [he] can be the biggest pain in the ass sometimes.

JOEY: (Pg 12) Denny, to keep me off the sauce, [had] me over just about every night of the week. I appreciated the gesture. It was a good thing to do. Denny was always doing things like that, always looking out for people. He was a good guy. (Pg 21) It started to rain that night, I remember. I don’t think it let up more than a minute or two till this whole mess was over. (Pg 45) – I blamed it on the rain

JOEY: (Pg 37) [It] was one of those days you dread. Tail end of our shift, around one a.m., a call came in, routine disorderly in an alley behind an apartment complex near Broadway and Sheridan, the part of town Denny called Deviant Corners. I responded, said we’d check it out. Without a word, Denny turned around the squad car and floored it.

DENNY: We pull up this alley off Deviant Corners. Right away in the headlights is this kid, this Vietnamese kid, stoned out of his mind. Not a stitch of clothes. He’s fumbling through the garbage cans, trying to stack ‘em up and make like this stairway to heaven over a tall, wood fence. We keep the headlights on the kid. We draw our service revolvers ‘cause any cop, you see somebody out of control this way, it’s usually PCP . . .

JOEY: So you play it safe.

DENNY: We go to him slow, cautious.

JOEY: He turns, sees us.

DENNY: We can see the kid’s in tears, verge of hysteria just about. And [he] comes running at us like that ‘Nam photo. Yunno, that girl running naked from the napalm blitzkrieg.

JOEY: Tears running down his face, yammering a mile a minute in Vietnamese about something. He slobbers up to us, ignoring any order we toss him.

DENNY: [He] ducks under my gun arm and locks his arms around me. Hugging me. ‘Course I don’t shoot. I mean I can see he’s unarmed. I look over to Joey for a little assistance. So Joey tells me . . .

JOEY: (To Denny) Try to calm the kid down while I go to the car for a blanket.

DENNY: What do you do to calm this kid down, sing him a Vietnamese lullaby? He’s like thirteen or fourteen and he’s naked. I mean, I can’t hug him back. So I’m standing there like a jerk, both arms in the air, all these people watching from the windowsill bleachers overhead, till Joey finally comes back with the blanket and wraps the kid in it. Joey practically had to peel the kid off of me.

JOEY: We pried him loose eventually. Trying to talk him down and getting nowhere. This beefy blond guy, he looked like a surfer, he comes up to us from outta one of the basement apartments off of the alley carrying a yellow umbrella and says he’ll take care of Li-Yao.

DENNY: He tells us the kid’s name is Li-Yao. He’s from Vietnam, sure enough, and he’s his nephew or cousin or both. I forgot what he said exactly. But I do remember he said the kid had some kinda war trauma and flips out.

JOEY: Which made sense at the time. So Denny tells me . . .

DENNY: (To Joey) Release him to his uncle’s custody and let’s amscray, uh? Joey didn’t wanna do it at first.

JOEY: Li-Yao seemed scared to death of his uncle. I told him I thought maybe we should bring the kid and his uncle in, maybe hunt down an interpreter, hceck out what the kid’s saying. Deny told me . . .

DENNY: (To Joey) Fine, J. Play Mother Teresa. Save the world. I got other official police business to conduct.

JOEY: . . . and took off for the squad car. The kid, Li-Yao, he went limp in my arms. I had to actually catch him, hold him up. The guy, the one who said he was the uncle, he told me this is what happens when Li-Yao’s posttraumatic stress disorder medication finally kicks in. So, I’m standing there with this passed-out naked kid in my arms [and] I don’t know what to do. So I handed Li-Yao over to his uncle. The guy seemed nice enough. I looked him square in the eye to get a read. He seemed decent. He really did.

DENNY: (Pg 44) So this Puerto Rican stiff was at the Citgo, I walked up to him very polite, I asked him: “Excuse me, sir, I’d like to ask you a few questions about your whereabouts last evening.” And like that, he drops his groceries, lunges for his car, and drives off. My partner, he’s off dealing with this alleyway incident across the street. So, no time to call him, I go after this Puerto Rican gentleman. I mean, hey, running from a cop is usually a pretty persuasive indicator something ugly’s amuck. Pouring rain, he tries to jump the concrete embankment doing 80, flips his car over two or three times and lands it upside down. Sure, I woulda called in for backup, woulda followed protocol, but Joey, he’s out on another call and I didn’t wanna cause any more accidents or anything. They guy died in the wreck. It was the guy’s own fault. I blamed it on the rain. (gesturing to himself) Sole survivor of the altercation: Last Man Standing.

JOEY: (Pg 47) Waiting. That’s what that summer was about. An excruciating exercise in patience. Waiting for things to blow sky-high between Denny and me. Waiting for an end to the rain. A lighter air. A brighter sky. Then they caught the psycho guy, this cannibal worse than anything anybody’d ever seen in the movies, and it turned out the Vietnamese boy Li- Yao was one of his victims.

DENNY: No sooner [does] the news flash the guy’s pictures than the boards are lit up with a million or more calls, witnesses the night these two dipshit beat cops turned this crying Vietnamese kid over to the cannibal killer. I mean parts of this kid’s body have still not been found.

JOEY: Instead of piecing together a case, they spent most of the early part of their investigation tying Denny and me to Li-Yao. Going to that length to ID a couple of scapegoats sure made it seem like they were out to nail us. First, [the chief] suspended us both with pay. Week later, after the press got ahold of it, we were suspended without pay. If we admitted breaching protocol by not running Li-Yao in, he promised us reinstatement in a month. Denny didn’t want to admit any wrongdoing.

DENNY: At how many paces can you identify a serial killer who eats his victims’ hearts. I mean, how the hell were we supposed to know? We believed he was his uncle. I don’t know Asian! [I have] kids of my own, don’t you think this eats me up? I still see his face, all the time his face, and I walk around, awake, asleep, I still feel his arms around me like I was his last saving grace and I failed him. Ain’t that punishment enough?

JOEY: Denny took it hard. He collapsed inside. His drinking got worse. I called him on the track marks up and down his arm, he told me mosquito bites.

DENNY: All I’m trying to do, like any other man, is take care of my family. Why take away my means to do that? Why?

JOEY: Denny went off the deep end that night. Me and a couple of other cops found him parked out on the flooded ninth hole of the Waveland Golf Course. He said he only had two or three beers, but it takes more than that to tank Denny. I found a couple of spent vials of morphine and a syringe. We carried him into his house, into the light (Pg 55) He wouldn’t look at me.

DENNY: (To Joey) Think you’d know the eyes of a demon if you saw one?

JOEY: (To Denny) We didn’t know Denny. First thing we’ve got to do to face this thing is let ourselves off the hook. We didn’t know

DENNY: (To Joey) But we should know, Joey. We should know the eyes of a demon when we see one (Pg 61) . . . Get out! . . . Get out! (completely broken) I can’t protect ‘em from it anymore, Joey.

JOEY: (To Denny) I know, Denny, I know. You can’t take responsibility for it all, Denny.

DENNY: (To Joey) Family man, you gotta. I brought it home with me. I can’t wash it off. It’s infected everything. It’s in me, Joey. It is me (Pause) Take care of ‘em for me, Joey.

JOEY: (To Denny) We take care of each other, Den. Back-to-back. Haven’t we always? (Denny shoves Joey away roughly)

DENNY: (To Joey) Back-to-back, J. Starsky and Hutch. Like the old days.

JOEY: I looked at Denny. He was loading [a] service revolver. Two steps and I heard the shot. (long beat) The Department didn’t honor Denny’s pension. There was no life insurance, either, because it was a suicide. When I took Connie [his wife] to make arrangements for Denny’s funeral, we decided to have him cremated. I don’t think he would have liked the idea of lying to rot in some cold plot of dirt for all eternity. Cremation at least saved us the cost of having his face reconstructed. He popped the gun just under his chin. (long beat) Denny was a part of me, gone forever. (Pg 34) My best friend. My partner. Always back to back, me and Den. (Pg 64) Denny invented rock tag. He called it Last Man Standing . . . and the rain . . . (Pg 61) The rain finally let up.
```

---

## IC-0446: Still Life

- Title: Still Life
- Author (byline): Emily Mann
- Work: Testimonies: Four Plays
- Publisher: Theatre Communications Group
- Publication date as stated: March 1997
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MARK
- Teaser before the introduction: Yes
- Spoken words (computed): 1597
- Already set (do not supply): none

### Source block (context only)

```text
Author: Emily Mann
Book: Testimonies: Four Plays
ISBN: 978-1559361170
Publisher: Theatre Communications Group
Date (Month/Year): March 1997
```

### Introduction (context only: never use it for content warnings)

```text
New research shows that four decades after the Vietnam War ended, more than 270,000 veterans who served in the war zone suffer from symptoms of PTSD, a mental health condition characterized by painful flashbacks, severe anxiety, and uncontrollable thoughts about the disturbing events they experienced. Nothing about war, particularly the Vietnam War, can be experienced 2nd hand by people who were not present.

And defining “war crimes” in Vietnam is not a simple black and white issue . . . No more than war crimes in Iraq, Afghanistan or Syria today. You see, there simply are no rules that apply to a nine-year-old boy as an enemy combatant. Is Mark in Emily Mann’s Still Life a war criminal or a war hero? I’ll leave that up to you to decide.

Still Life by Emily Mann
```

### Performance text (classify this)

```text
MARK: My biggest question to myself all my life was: How I would act under combat? That would be who I was as a man. I read my Hemingway. You know . . . The point is, you don’t need to go through it. I would break both my son’s legs before I let him go through it. I’ve thought about it. A lot.

The truth of it is, it’s different from what we’ve heard about war before. I don’t want this to come off as a combat story. It’s a tragedy is what it is. It happened to a lot of people. And you don’t need to go through that shit. It’s bullshit. It just chews people up. I did things over there. We all did (quietly to audience.) We all did.

MARK: There was this whole trip that we were really special. And our training was really hard, like this whole Spartan attitude. And there was this whole ethic: you do not leave your man behind on the field. I love that.

I came to a point in there: Okay, you’re here, there’s no escape, you’re going to get taken, it’s all right to commit suicide. And it was as rational as that. We came across a hit at night, we got ambushed, it was a black guy walking point, and you know, bang, bang, bang. You walk into it. It was a surprise. Well, they got this black guy. And they took his body and we found him about a week later . . . And they had him tied to a palm tree. They’d opened up his stomach and it had been pulled out. And I knew . . . Nobody was going to do that to me. Better for me to rationalize suicide because I didn’t want . . . that. I don’t know.

R.J. was my best friend over there. He and I got into a whole weird trip. We found ourselves competing against one another, setting up ambushes, getting people on kills and things, being the best at it we could. R.J. is dead. He got killed in a bank robbery in Chicago. (He was one of the few friends of mine who survived the war.)

I heard from one guy on a regular basis, maybe once a year. He was green to Viet Nam. We were getting into some real heavy contact. It was late at night, the VC went to us while we were sleeping. They just threw grenades in on us. The explosion came, I threw this kid in a bush. All I did was grab him down, and he got a medical out of there. But he feels I saved his life. He was only in the bush maybe five, six weeks, but it did something to him. He spent two years in a mental institution. I don’t know. I knew he knew what I knew . . . .

It’s become a personal thing. The guilt. It’s getting off on having all that power every day. Because it was so nice. I mean, it was power . . . I had the power of life and death. It’s like the best dope you’ve ever had, the best sex you’ve ever had. You never find anything better. And that’s not something you’re supposed to feel good about.

I haven’t told you what a marine is yet. I mean, we were trained to do one thing. That‘s the one thing about the marines. We were trained to kill. I had the power of life and death. I dug it. I enjoyed it. I really enjoyed it. It’s getting hard to talk. I need to tell this, but I don’t want to be seen as . . . a monster.

I look at my face in a mirror, I look at my hands, and I cannot believe . . . I did these things . . . . I’m sorry. I don’t think you can understand. It was this duty thing. It was like: YOU’RE UNDER ORDERS. You have your orders, you have you job, you’ve got to do it. Well, it was like crazy. At night, you could do anything . . . it was free fire zones. It was dark, then all of a sudden, everything would just burn loose. It was beautiful . . . you were given all this power to work outside the law. We all dug it. But I don’t make any excuses for it. I may even be trying to do that now. I could have got out. Everybody could’ve. If EVERYBODY, had said no, it couldn’t have happened.

(pulling photos from his bag) I brought some photos. This is a picture of some people who at one point in time were in my unit. That is, they were there at the time the photo was taken. Some of them are dead, some of them made it home. (Pause) Some of them are dead now. This photo is of some guys in my unit. We were South/South-West of Danang--we were in that whole triangle, not too far from where My Lai was. Near the mountains, near the coast. Everybody knew about My Lai. But it wasn’t different from what was going on. I mean, the grunts did it all the time. This fellow up there, that’s Michele. He ended up in the nut-house, that’s the fellow I pulled out of the bush. This is the machine gunner. The kid was so good he handled the gun like spraying paint. This kid was from down south. Smart kid. He got hit in the head, with grenade shrapnel. He’s alive, but that was the end of the war for him. There were no two ways about it . . . You knew that you were killing something. You actually knew it, you saw it, you had the body. You didn’t take wounded. That was it. You just killed them. And they did the same to you.

(Focuses on picture of him with medal. Full Dress) This is a picture of my first purple heart. We were out in the bush. To me, a Purple Heart meant it was something you got when you were wounded and you bled. You were hurt during a contact. I didn’t feel anything getting it. But I wanted a picture of it. Actually, I was pissed off about getting that medal. What can I say? I am still alive--my friends aren’t. It’s a still life.

Here’s a picture of me . . . and some kids. (snaps on picture of him and some children) God I LOVED those kids. Everybody hated them. You couldn’t trust ‘em. The VC would send the kids in with a flag. I never saw this, I heard about it, the kid would come in asking for C-rations, try to be your friend, and they’d be maybe wired with explosives or something and the kid’d blow up. There was a whole lot of weirdness. I really dug kids. I don’t know why. (more pictures of kids) I did a really bad number . . . it went contrary, I think, to everything I knew, I’m not ready to talk about that yet.

You know, I get panicky if there’s any element of control taken away from me. (I don’t like to be alone in the dark. I’m scared of it.) I don’t like fireworks. I’ve had bad dreams when my wife’s had to bring me back out. I’ve heard about vets killing their wives in their sleep. But this is personal – for me, the gun was always the instrument, or a grenade. I never grabbed somebody and slowly killed them. I’ve never choked them to death of anything. I never killed with my bare hands.

(Pause) I need to tell you what I did. (shows picture of wounded children) This is a picture of some kids who were hurt. I used to take care of them, change their bandages and all. I loved these kids, Oh, God . . . You want to hear what I did? It’s real confusion. I’m guilty and I’m not guilty. I want to tell. I need to tell what I did.

I . . . I killed three children, a mother and a father in cold blood. I killed them with a pistol in front of a lot of people. I demanded something from the parents and then systematically destroyed them. And that’s . . . that’s what I’m carrying around. For the rest of my life . . . This is what I’m carrying around. A friend hit a booby-trap. And these people knew about it. I knew they knew. I knew that they were working with the VC infra-structure. I demanded that they tell me. They wouldn’t say anything. I just wanted them to confess before I killed them. And they wouldn’t. So I killed their children and then I killed them. I was angry. I was angry with all the power I had. I couldn’t beat them. They beat me.

(crying)

I have a child . . . a child. My son . . . my son wouldn’t know the difference between a VC and a Marine. The children were so little. It’s no different than what the Nazis did. It’s the same thing. I know that I’m not alone. I know that other people did it, too. More people went through more hell than I did . . . but they didn’t do this. I guess deep down I’m just everything that’s bad. (long pause) But, I should have done better. I mean, I really strove to be good. I had a whole set of values. I had ‘em and I didn’t. I want to censor myself for you. I didn’t want you to say: what kind of a nut, what kind of a bad person is he? And yet, I’m not gonna lie. See, I don’t want to see people going through another era of being so ignorant of the fact that war kills people. It will happen again. I don’t want more children to die. I want to come to the point where I tell myself that I’ve punished myself enough. In spite of it all, I don’t want to punish myself anymore.
```

---

## IC-0447: Stuck in Neutral

- Title: Stuck in Neutral
- Author (byline): Terry Trueman
- Work: Not specified
- Publisher: Harper Tempest
- Publication date as stated: Oct 2001
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SHAWN’S INNER VOICE, SHAWN’S VOICE IMPACTED BY CP, ALLY, MOM, DAD, GUY
- Teaser before the introduction: Yes
- Spoken words (computed): 1019
- Already set (do not supply): none

### Source block (context only)

```text
Author: Terry Trueman
ISBN: 978-0060285197
Publisher: Harper Tempest
Date (Month/Year): Oct 2001
```

### Introduction (context only: never use it for content warnings)

```text
Shawn McDaniel is an enigma and a miracle--except no one knows it, least of all his father. His life is not what it may seem to anyone looking at him. Not even those who love him best have any idea what he is truly like. Today, I personally challenge you to look beyond the obvious and truly see a person whose spirit is rich beyond imagining and whose story is unforgettable.

Stuck in Neutral by Terry Trueman
```

### Performance text (classify this)

```text
SHAWN’S INNER VOICE: My name is Shawn McDaniel. My life is like one of those "good news—bad news" jokes. Like, "I’ve got some good news and some bad news–which do you wanna hear first?" In the jokes, it’s always the good news first, so here goes: my mom and dad love me!

I could go on about my good news for hours, but you probably want to hear the punch line, my bad news, right? This bad news is complicated, difficult to explain. In a nutshell, it's that I am pretty sure that my dad is planning to kill me. The good news is that he'd be doing this out of his love for me. The bad news is that whatever the wonderfulness of his motives, I'll be dead.

SHAWN’S INNER VOICE: Every year the school district sends out a school psychologist (scientist) to test me -- mainly intelligence tests filled with questions like "Who was George Washington?" and "What’s two plus one?" And every year I sit there and miss every question. Then the shrink goes in and gives my mom a number: I.Q. = 1.2, or mental age 3 to 4 (that’s months, not years).

(Transition into the vocal qualities and mannerisms of someone with CP)

SHAWN’S VOICE IMPACTED BY CP: The deal is, I have cerebral palsy. I can't control any of my muscles: not my fingers, my eyes, [my voice] . . . none of them. Not a one. So when the psychologist says, "Who was George Washington?" I can't tell him what I know. All I can do is sit there and drool if my drool function is running, or go, "ahhhhhh!"

(Transition back to regular mannerisms and speech)

SHAWN’S INNER VOICE: When people first meet me, they usually speak real slowly and real loudly:

ALLY: Hi Shawn, nice to meet you! My name is Ally Williamson! How are you!

(Transition into the vocal qualities and mannerisms of someone with CP)

SHAWN’S VOICE IMPACTED BY CP: Well, I’m not deaf! (Beat) Oh, but it gets worse. You should see my mom!

MOM: Goo-goo-baby boy-go . . . you a big baby boy . . . boogie woogie googie snoogie.

SHAWN’S VOICE IMPACTED BY CP: It’s OK, you can laugh. I do! You know, people mean well. They just don’t always know how to show it. Like my dad.

(Transition back to regular mannerisms and speech)

SHAWN’S INNER VOICE: I guess I should explain about my father, about why I think he's planning to kill me. It's not as though he's stated it directly. It's more an intuition -- intuition and a thing that happened last week when my dad stopped by the house.

DAD: How're you doing, big boy? Everything going okay for you? Any hot news for me?

(Laughs)

SHAWN’S INNER VOICE: He laughed at his joke, not a big or happy or mean laugh, but a quiet, sad one. Then he leaned over in front of me and brought his face down close to mine. With his brown eyes only inches away from my eyes, it felt as though he were trying to stare through me, straight through my eyes and into my brain.

DAD: (softly) You're not getting any of this, are you, Shawn?

(Transition into the vocal qualities and mannerisms of someone with CP)

SHAWN’S VOICE IMPACTED BY CP: In fourteen years I've heard him say my name aloud in my presence a total of sixteen times.

DAD: God . . . look what he did to you! You can’t even protect yourself, Shawn. I can’t protect you, or your mom or anyone else. You know I love you, right? When I think about you, Shawn, my heart breaks. When I think about you hurting, I can barely even breathe, my chest aches so badly. I want to help you, Shawn, I do. But I just don’t know how. Am I supposed to let all your pain and your seizures continue, or should I just end it. Is that what you want, Shawn – you want me to end your pain?

SHAWN’S INNER VOICE: No, I don’t want that! End my pain? It made me mad. What right does he have to decide what's best for me? What right does he have to think about ending my pain? . . . You see, I know he loves me, but when he looks at me all he sees . . .

(Transition into the vocal qualities and mannerisms of someone with CP)

SHAWN’S VOICE IMPACTED BY CP: . . . is this twisted, drooling pile of flesh. (Beat) What do you see? You know, it’s just a shock to me. There’s an actual person inside here who wants to be seen and loved, but of course, I can’t tell him. He can’t hear me. You see, he can only remember what happened.

(Transition back to regular mannerisms and speech)

SHAWN’S INNER VOICE: One day I was out on our front porch sitting in my wheelchair, when this guy showed up . . .

GUY: Hey! You know if the bus has come by or not? Hey! You there, Roller Derby, has the bus come by or not?

(Transition into the vocal qualities and mannerisms of someone with CP)

SHAWN’S VOICE IMPACTED BY CP: Ahhhhhh!

GUY: Are you laughing at me, huh? Did I say something funny. Look at me when I’m talking to you. Did I say something funny? Maybe I should teach you some respect, huh?

SHAWN’S VOICE IMPACTED BY CP: Then he held a lighter under my chin.

GUY: Not’s so funny now, huh?

SHAWN’S VOICE IMPACTED BY CP: Ahhhhhh!

(Transition back to regular mannerisms and speech)

SHAWN’S INNER VOICE: Do you know what it’s like to smell your own flesh burning and not be able to do anything about it? He burned a hole under my chin and I couldn’t even stop him.

When my dad came out, he freaked. Without a word the stranger scurried out our open gate. In ten seconds he was gone. We never saw him again.

(Transition into the vocal qualities and mannerisms of someone with CP)

SHAWN’S VOICE IMPACTED BY CP: So now I have to worry about what my dad is going to do to me. Is my father going to kill me? When? How? What's going to happen?

DAD: When you were born, and we were told that you'd have these kinds of problems, I got down on my knees and prayed harder than I'd ever prayed, begging God or Satan, or anybody in between, to let me trade places with you. I prayed, night after night, that I could be the one trapped inside your body and that you could take my place. I don't know what to do, son. Shawn . . . I love you.

(Transition back to regular mannerisms and speech)

SHAWN’S INNER VOICE: You know, I just wish for one moment that I could have complete control over my body. Just for 2 minutes. So I could tell my dad that I love him and I could cuddle with my mom. So I could tell her that I love her and tell my dad that I AM happy and that his unconditional love . . .

(Transition into the vocal qualities and mannerisms of someone with CP)

SHAWN’S VOICE IMPACTED BY CP: . . . is everything I need. And that I’m just sorta stuck in neutral.

Find out more about Cerebral Palsy here: https://www.cdc.gov/ncbddd/cp/facts.html
```

---

## IC-0448: Suzanne’s Diary for Nicholas

- Title: Suzanne’s Diary for Nicholas
- Author (byline): James Patterson
- Work: Not specified
- Publisher: Warner Books, Inc
- Publication date as stated: (Month/Year): July 2003
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MATTHEW
- Teaser before the introduction: Yes
- Spoken words (computed): 1219
- Already set (do not supply): none

### Source block (context only)

```text
Author: James Patterson
ISBN: 978-0446611084
Publisher: Warner Books, Inc
Date: (Month/Year): July 2003
```

### Introduction (context only: never use it for content warnings)

```text
Many families keep a journal of special events that occur in the lives of their child: A special book of memories . . . a tradition. In this selection we find Nicholas’ father, Matthew logging his own personal entries in Suzanne’s Diary to Nicholas by James Patterson
```

### Performance text (classify this)

```text
MATTHEW: Hello, my sweet Nicholas, it’s Dada. Have I told you how much I love you? Have I told you how precious you are to me? There---now I have. You are the best little boy, the best anyone could ever hope for. I love you so much. Yesterday morning something happened. And that’s why I’m writing to you today instead of Mommy. Fathers and sons need to talk more than they do. A lot of us are so afraid to show our emotions, but I never want us to be like that. This is so hard, Nicky. It’s the hardest thing I have ever had to say to anybody.

MATTHEW: Mommy was going to the store to the store to pick up your birthday present, your beautiful framed pictures. She was incredibly happy. She looked so pretty, deeply tanned and toned from all her walks on the beach. I remember seeing her leave, and I can’t get that image out of my mind.

Suzanne had such a beautiful smile on her face. She was dressed in a yellow jumper and gauzy white blouse. Her blond hair was full of curls and swung with her body as she walked. She was humming your song, “Whistle a Happy Tune.”

I should have gone to her, should have kissed Suzanne good-bye, should have hugged her in my arms. But I just called, “Love you,” and since her hands were full, she blew me a kiss. Oh, Nicky, Nicky, Nicky. How can I say this? How can I write these words? Mommy had a heart attack on the way into town, sweet baby. Her heart, which was so big, so special in so many ways, could no longer hold out.

I was told that Suzanne was unconscious before she crashed into the guardrail on Old Pond Bridge Road. Her Jeep dropped into the water, landing on its side. I haven’t gone to look at the actual scene of the accident. That is an image I don’t need inside my head. What I can see is already is too much.

Dr. Cotter says that Suzanne died instantly after the massive coronary, But who really knows about those final seconds? I hope she didn’t feel any pain. I hate to think that she did. It would be too cruel.

She was unimaginably happy the last time I saw her. She looked so pretty, Nick. Oh God, I just want to see Suzanne one more time. Is that too much to ask? Is it unreasonable? It doesn’t seem so to me. It’s important to me that you know it wasn’t Mommy’s fault. She was such a safe driver; she would never have taken any chances. I always teased her about her driving.

She was the most generous-hearted person I have ever known, the most caring and compassionate. Maybe what I loved best about her was that she was a great, great listener. And she was funny. She would make a joke, right now. In know she would. And maybe she is. Are you smiling now, Suzanne? I’d like to think that you are I believe you must be.

I went today to the cemetery on Abel’s Hill, to choose Mommy’s special place. She was just thirty-seven when she died. How sad, how completely unthinkable to me, and to everyone else who knew her. What a shame; what a waste. Sometimes it makes me so angry. Tonight I sit in your nursery and watch your clown lamp throw happy shadows against the walls in the half-light. The oak rocking horse I made for you reminds me of the Flying Horses Carousel. Remember when we all went there on our vacation and rode the colorful horses? Nicholas, Suzanne, and Matt.

I held you in front of me, and you loved to stroke the real horsehair mane. I can see Mommy riding ahead of us on National Velvet. She turns and there’s that famous wink of hers.

MATTHEW: Dear, sweet Nick, I was startled out of my thoughts and reveries this afternoon by an unexpected phone call. It was for Mommy. Obviously someone had no idea what had happened, and for the first time, those strange and awful words passed through my lips like heavy weights: “Suzanne has passed away.”

There was a long silence on the other end, followed by quiet apologies, and then nervous condolences. I was the man from the frame shop on the other side of the island, in Chilmark Center. Mommy had never made it there, and the pictures she had framed for you were still at the store. I told the shop owner that I would come around for the photos. Somehow, I would manage to do it.

I walk aimlessly from room to room, trying desperately to find a place where I can feel at peace with myself. Somehow, I always end up back in your room, sitting in the same rocker Mommy so often did when she talked to you and read to you and recited her goofy rhymes.

And so I sit here now, looking at the pictures of us I finally picked up this afternoon. We are all sitting in front of the Flying Horses Carousel on a perfect, blue-skied afternoon.

You are wedged between us, Nick. Mommy has her arm around you and her legs crossed on mine. You’re kissing Mommy, and I’m tickling you, and everyone is laughing, and it’s just so beautiful. Nicholas, Suzanne, and Matt----Forever One.

I pull the cord on your music box in your crib, and it begins to play “Whistle a Happy Tune.” I love this song, Nicky. I reach into the crib and I touch your sweet cheek. I tousle your golden blond hair, always so soft and fragrant. I wish I had listened to Mommy and never cut it.

I place an index finger in each of your small hands and let you squeeze. You’re so strong buddy. I listen to your beautiful laugh, and it almost makes me laugh. “Whistle a Happy Tune” continues to play.

Oh my dear, darling little boy. I remember Mommy leaving on her errand that morning. I called out “I love you,” and she blew me a kiss. Then she crinkled up her nose the way she does. You know what I mean. You know that look of hers. Then she gave me her “famous wink.”

Her arms were full, because she was carrying you, sweet baby. She wanted you to be the first to see the beautiful framed photographs. That’s why she took you with her to town on your birthday morning. Suzanne carried you outside and carefully strapped you in your car seat. You were in the Jeep with Mommy when she crashed on the Old Pond Bridge Road. The two of you were together. I still can’t bear to think about it.

I should’ve been there, Nicholas. I should’ve been there with you and Mommy! Maybe I could have helped: maybe I could have saved you somehow. At least I could have tried, and that would have meant everything to me.

But isn’t it lucky that I knew you, held you and loved you, for the twelve months before God took you away? Isn’t it lucky that I got to know you, sweet little boy, my son?
```

---

## IC-0449: The Swan Song

- Title: The Swan Song
- Author (byline): Anton Chekhov (translated by Marian Fell)
- Work: 7 Short Farces by Anton Chekhov
- Publisher: Dramatist’s Play Service
- Publication date as stated: Jan 1998
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SVIETLOVIDOFF, IVANITCH
- Teaser before the introduction: No
- Spoken words (computed): 2495
- Already set (do not supply): none

### Source block (context only)

```text
Author: Anton Chekhov
Book: 7 Short Farces by Anton Chekhov
ISBN: 0822216450
Publisher: Dramatist’s Play Service
Date(Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
Actor 1: Farce: A light dramatic work in which highly improbable plot situations, exaggerated characters, and often slapstick elements are used for humorous effect. Actor 2: Chekhov was a master of this literary genre and in his honor, we present to you today: Together: The Swan Song by Anton Chekhov.

[The scene is laid on the stage of a country theatre, at night, after the play. To the right a row of rouch, unpainted doors leading into the dressing-rooms. To the left and in the background the stage is encumbered with all sorts of rubbish. In the middle of the stage is an overturned stool.]
```

### Performance text (classify this)

```text
SVIETLOVIDOFF: [With a candle in his hand, comes out of a dressing-room and laughs.] Well, well, this is funny! Here's a good joke! I fell asleep in my dressing-room when the play was over, and there I was calmly snoring after everybody else had left the theatre. Ah! I'm a foolish old man, a poor old dodderer! I have been drinking again, and so I fell asleep in there, sitting up. That was clever! Good for you, old boy! [Calls.] Yegorka! Petrushka! Where the devil are you? Petrushka! The scoundrels must be asleep, and an earthquake wouldn't wake them now! Yegorka! [Picks up the stool, sits down, and puts the candle on the floor.] Not a sound! Only echoes answer me. I gave Yegorka and Petrushka each a tip today, and now they have disappeared without leaving a trace behind them. The rascals have gone off and have probably locked up the theatre. [Turns his head about.] I'm drunk! Ugh! The play tonight was for my benefit, and it is disgusting to think how much beer and wine I have poured down my throat in honour of the occasion. Gracious! My body is burning all over, and I feel as if I had twenty tongues in my mouth. It is horrid! Idiotic! This poor old sinner is drunk again, and doesn't even know what he has been celebrating! Ugh! My head is splitting, I am shivering all over, and I feel as dark and cold inside as a cellar! Even if I don't mind ruining my health, I ought at least to remember my age, old idiot that I am! Yes, my old age! It's no use! I can play the fool, and brag, and pretend to be young, but my life is really over now, I kiss my hand to the sixty-eight years that have gone by; I'll never see them again! I have drained the bottle, only a few little drops are left at the bottom, nothing but the dregs. Yes, yes, that's the case, Vasili, old boy. [Stares ahead of him.] It is strange, though, that I have been on the stage now for forty-five years, and this is the first time I have seen a theatre at night, after the lights have been put out. The first time. [Walks up to the footlights.] How dark it is! I can't see a thing. Oh, yes, I can just make out the prompter's box, and his desk; the rest is in pitch darkness, a black, bottomless pit, like a grave, in which death itself might be hiding. . . . Brrr. . . . How cold it is! The wind blows out of the empty theatre as though out of a stone flue. What a place for ghosts! The shivers are running up and down my back. [Calls.] Yegorka! Petrushka! Where are you both? What on earth makes me think of such gruesome things here? I must give up drinking; I'm an old man, I shan't live much longer. At sixty-eight people go to church and prepare for death, but here I am--heavens! A profane old drunkard in this fool's dress--I'm simply not fit to look at. I must go and change at once. . . . This is a dreadful place, I should die of fright sitting here all night. [Goes toward his dressing-room; at the same time NIKITA IVANITCH in a long white coat comes out of the dressing-room at the farthest end of the stage. SVIETLOVIDOFF sees IVANITCH-- shrieks with terror and steps back.] Who are you? What? What do you want? [Stamps his foot.] Who are you?

IVANITCH: It is I, sir.

SVIETLOVIDOFF: Who are you?

IVANITCH: [Comes slowly toward him.] It is I, sir, the prompter, Nikita Ivanitch. It is I, master, it is I!

SVIETLOVIDOFF: [Sinks helplessly onto the stool, breathes heavily and trembles violently.] Heavens! Who are you? It is you . . . . you Nikitushka? What . . . what are you doing here?

IVANITCH: I spend my nights here in the dressing-rooms. Only please be good enough not to tell Alexi Fomitch, sir. I have nowhere else to spend the night; indeed, I haven't.

SVIETLOVIDOFF: Ah! It is you, Nikitushka, is it? Just think, the audience called me out sixteen times; they brought me three wreathes and lots of other things, too; they were all wild with enthusiasm, and yet not a soul came when it was all over to wake the poor, drunken old man and take him home. I am an old man, Nikitushka! I am sixty-eight years old, and I am ill. I haven't the heart left to go on. [Falls on IVANITCH'S neck and weeps.] Don't go away, Nikitushka; I am old and helpless, and I feel it is time for me to die. Oh, it is dreadful, dreadful!

IVANITCH: [Tenderly and respectfully.] Dear master! it is time for you to go home, sir!

SVIETLOVIDOFF: I won't go home; I have no home--none! none! none!

IVANITCH: Oh, dear! Have you forgotten where you live?

SVIETLOVIDOFF: I won't go there. I won't! I am all alone there. I have nobody, Nikitushka! No wife--no children. I am like the wind blowing across the lonely fields. I shall die, and no one will remember me. It is awful to be alone--no one to cheer me, no one to caress me, no one to help me to bed when I am drunk. Whom do I belong to? Who needs me? Who loves me? Not a soul, Nikitushka.

IVANITCH: [Weeping.] Your audience loves you, master.

SVIETLOVIDOFF: My audience has gone home. They are all asleep, and have forgotten their old clown. No, nobody needs me, nobody loves me; I have no wife, no children.

IVANITCH: Oh, dear, Oh, dear! Don't be so unhappy about it.

SVIETLOVIDOFF: But I am a man, I am still alive. Warm, red blood is tingling in my veins, the blood of noble ancestors. I am an aristocrat, Nikitushka; I served in the army, in the artillery, before I fell as low as this, and what a fine young chap I was! Handsome, daring, eager! Where has it all gone? What has become of those old days? There's the pit that has swallowed them all! I remember it all now. Forty-five years of my life buried there, and what a life, Nikitushka! I can see it as clearly as I see your face; the ecstasy of youth, faith, passion, the love of women- -women, Nikitushka!

IVANITCH: It is time you went to sleep, sir.

SVIETLOVIDOFF: When I first went on the stage, in the first glow of passionate youth, I remember a woman loved me for my acting. She was beautiful, graceful as a poplar, young, innocent, pure, and radiant as a summer dawn. Her smile could charm away the darkest night. I remember, I stood before her once, as I am now standing before you. She had never seemed so lovely to me as she did then, and she spoke to me so with her eyes--such a look! I shall never forget it, no, not even in the grave; so tender, so soft, so deep, so bright and young! Enraptured, intoxicated, I fell on my knees before her, I begged for my happiness, and she said: "Give up the stage!" Give up the stage! Do you understand? She could love an actor, but marry him--never! I was acting that day, I remember--I had a foolish, clown's part, and as I acted, I felt my eyes being opened; I saw that the worship of the art I had held so sacred was s delusion and an empty dream; that I was a slave, a fool, the plaything of the idleness of strangers. I understood my audience at last, and since that day I have not believed in their applause, or in their wreathes, or in their enthusiasm. Yes, Nikitushka! The people applaud me, they buy my photograph, but I am a stranger to them. They don't know me, I am as the dirt beneath their feet. They are willing enough to meet me . . . but allow a daughter or a sister to marry me, an outcast, never! I have no faith in them. [Sinks onto the stool.] No faith in them.

IVANITCH: Oh, sir! You look dreadfully pale, you frighten me to death! Come, go home, have mercy on me!

SVIETLOVIDOFF: I saw through it all that day, and the knowledge was dearly bought. Nikitushka! After that . . . when that girl . . . well, I began to wander aimlessly about, living from day to day without looking ahead. I took the parts of buffoons and low comedians, letting my mind go to wreck. Ah! but I was a great artist once, till little by little I threw away my talents, played the motley fool, lost my looks, lost the power of expressing myself, and became in the end a Merry Andrew instead of a man. I have been swallowed up in that great black pit. I never felt it before, but tonight, when I woke up, I looked back, and there behind me lay sixty-eight years. I have just found out what it is to be old! It is all over . . . [Sobs.] . . . all over.

IVANITCH: There, there, dear master! Be quiet . . . gracious! [Calls.] Petrushka! Yegorka!

SVIETLOVIDOFF: But what a genius I was! You cannot imagine what power I had, what eloquence; how graceful I was, how tender; how many strings [Beats his breast.] quivered in this breast! It chokes me to think of it! Listen now, wait, let me catch my breath, there; now listen to this:

"The shade of bloody Ivan now returning
Fans through my lips rebellion to a flame,
I am the dead Dimitri! In the burning
Boris shall perish on the throne I claim.
Enough! The heir of Czars shall not be seen
Kneeling to yonder haughty Polish Queen!"

Is that bad, eh? [Quickly.] Wait, now, here's something from King Lear. The sky is black, see? Rain is pouring down, thunder roars, lightning--zzz zzz zzz--splits the whole sky, and then, listen:

"Blow winds, and crack your cheeks! Rage! Blow!

You cataracts and hurricanes spout
Till you have drench'd our steeples, drown'd the cocks!
You sulphurous thought-executing fires,
Vaunt-couriers of oak-cleaving thunderbolts,
Singe my white head! And thou, all shaking thunder,
Strike flat the thick rotundity o' the world!
Crack nature's moulds, all germens spill at once
That make ungrateful man!"

[Impatiently.] Now take the part of the fool. [Stamps his foot.] Come take the fool's part! Be quick, I can't wait!

IVANITCH: [Takes the part of the fool.] "O, Nuncle, court holy-water in a dry house is better than rain-water out o' door. Good Nuncle, in; ask thy daughter's blessing: here's a night pities neither wise men nor fools."

SVIETLOVIDOFF: "Rumble thy bellyful! Spit, fire! Spout, rain!
Nor rain, wind, thunder, fire, are my daughters;
I tax not you, you elements, with unkindness;
I never gave you kingdom, call'd you children."

Ah! there is strength, there is talent for you! I'm a great artist! Now, then, here's something else of the same kind, to bring back my youth to me. For instance, take this, from Hamlet, I'll begin . . . let me see, how does it go? Oh, yes, this is it. [Takes the part of Hamlet.] "O! the recorders, let me see one.--To withdraw with you. Why do you go about to recover the wind of me, as if you would drive me into a toil?"

IVANITCH: "O, my lord, if my duty be too bold, my love is too unmannerly."

SVIETLOVIDOFF: "I do not well understand that. Will you play upon this pipe?"

IVANITCH: "My lord, I cannot."

SVIETLOVIDOFF: "I pray you."

IVANITCH: "Believe me, I cannot."

SVIETLOVIDOFF: "I do beseech you."

IVANITCH: "I know no touch of it, my lord."

SVIETLOVIDOFF: "Tis as easy as lying: govern these ventages with your finger and thumb, give it breath with your mouth, and it will discourse most eloquent music. Look you, these are the stops."

IVANITCH: "But these I cannot command to any utterance of harmony: I have not the skill."

SVIETLOVIDOFF: Why, look you, how unworthy a thing you make of me. You would play upon me; you would seem to know my stops; you would pluck out the heart of my mystery; you would sound me from my lowest note to the top of my compass; and there is much music, excellent voice, in this little organ, yet cannot you make it speak. S'blood! Do you think I am easier to be played on than a pipe? Call me what instrument you will, though you can fret me, you cannot play upon me!" [Laughs and claps.] Bravo! Encore! Bravo! Where the devil is there any old age in that? I'm not old, that is all nonsense, a torrent of strength rushes over me; this is life, freshness, youth! Old age and genius can't exist together. You seem to be struck dumb, Nikitushka. Wait a second, let me come to my senses again. Oh! Good Lord! Now then, listen! Did you ever hear such tenderness, such music? Sh! Softly;

"The moon had set. There was not any light,
Save of the lonely legion'd watch-stars pale
In outer-air, and what by fits made bright
Hot oleanders in a rosy vale
Searched by the lamping fly, whose little spark
Went in and out, like passion's bashful hope."

[The noise of opening doors is heard.] What's that?

IVANITCH: There are Petrushka and Yegorka coming back. Yes, you have genius, genius, my master.

SVIETLOVIDOFF: [Calls, turning toward the noise.] Come here to me, boys! [To IVANITCH.] Let us go and get dressed. I'm not old! All that is foolishness, nonsense! [Laughs gaily.] What are you crying for? You poor old granny, you, what's the matter now? This won't do! There, there, this won't do at all! Come, come, old man, don't stare so! What makes you stare like that? There, there! [Embraces him in tears.] Don't cry! Where there is art and genius there can never be such things as old age or loneliness or sickness . . . and death itself is half . . [Weeps.] No, no, Nikitushka! It is all over for us now! What sort of genius am I? I'm like a squeezed lemon, a cracked bottle, and you--you are the old rat of the theatre . . . a prompter! Come on! [They go.] I'm no genius, I'm only fit to be in the suite of Fortinbras, and even for that I am too old. . . . Yes. . . . Do you remember those lines from Othello, Nikitushka?

"Farewell the tranquil mind! Farewell content! Farewell the plumed troops and the big wars That make ambition virtue! O farewell!

Farewell the neighing steed and the shrill trump, The spirit-stirring drum, the ear-piercing fife, The royal banner, and all quality, Pride, pomp and circumstance of glorious war!"

IVANITCH: Oh! You're a genius, a genius!

SVIETLOVIDOFF: And again this:

"Away! the moor is dark beneath the moon,
Rapid clouds have drunk the last pale beam of even:
Away! the gathering winds will call the darkness soon,
And profoundest midnight shroud the serene lights of heaven."
```

---

## IC-0450: Sweet Eros

- Title: Sweet Eros
- Author (byline): Terrence McNally
- Work: Sweet Eros and Witness
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Jan 1998
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: YOUNG MAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1667
- Already set (do not supply): none

### Source block (context only)

```text
Author: Terrence McNally
Book: Sweet Eros and Witness
ISBN: 978-0822211051
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
A disturbed young man, soured by two failed romantic relationships, has kidnapped a young woman (a complete stranger). The woman is seated in a chair, bound and gagged as the man explains his reasons for kidnapping her, and what he’s come to realize about life and love. His goal? To force the woman to understand him - and, ultimately, to submit to him. Sweet Eros by Terrence McNally
```

### Performance text (classify this)

```text
YOUNG MAN: So there's really no reason it was you. Once I'd made my mind up, it could have been anyone. You just happened to cross my path before the next person. (He lowers his eyes.) I said there'd be no lies. (He looks up at her.) It couldn't have been just anyone. I wouldn't have taken a child or an older person. Someone in a religious order. A handicapped person, A lot of people I wouldn't have taken. I wanted a girl. (

YOUNG MAN: So I suppose it was inevitable. I mean when you want to do something that bad that long, sooner or later you do it. And I wanted this for a long time. It started off just being an idea . . . one of those cool, safe abstractions that never got anybody into trouble ... the whole plan just seemed so damned risky! Not unreasonable, mind you, but risky. You can imagine: the police, the one chance in a million of hurting you, morning-after remorse on my part. The same things that cross a murderer's mind probably. And then yesterday morning, overnight, just like that, I woke up thinking. "What the hell?" I'm young, reasonable-looking, clean--certainly I wouldn't terrify her and maybe she'll like me by the time it's over. I'm rich enough-so there's money when it's done if she's got hard feelings. I'm in the country-no chance of neighbors hearing if I took the gag off too soon. And I'm a good person. Mmm. I like myself. That's important. So I took the car, drove into the city, saw you walking your dog (I assume it was yours), and here you are. Easy. (He lowers his eyes, then raises them.) I had to kill the dog. (The Girl struggles.) He barked. (The Girl continues to struggle.) HE BARKED! (The Girl stops struggling.) He was a nice dog. I'm sorry he barked. (He smiles. Slow blackout.)

***************************.

YOUNG MAN: If you really look at another person, you'll find they're rather strange. Oh, I recognize the physical resemblance, but after hair, nose, eyes, mouth, teeth, neck, arms, legs and all, it stops. The resemblance, I mean. Know what I mean? (He smiles) I think insects are less strange to one another than people are. Take ants. An ant either really accepts another ant or he doesn't even think about it. The point is, they cooperate. There's no friction with ants. They make do. Then take people: they don't accept each other, which is fact number one about them, and fact number two, that's all they think about. So there's noncooperation, friction. Let's face it: humans are tense together. (He takes off her shoes.)

My first woman . . . notice I don't say wife . . . was so fraught she couldn't cope at all. They carted her off eventually. And yet you'd have thought she had everything going for her: good background, a big fat inheritance after a touching reunion with her daddy on his deathbed; a spiffy career and me. I include myself in this girl's cornucopia because I loved her. I mean she was lucky. Somebody cared and, sister, there aren't words enough to tell how much I loved this person. (He is taking off her stockings now.) Sounds ideal, no? For her, I mean. Well, there was a fly in this girl's ointment, and he had two arms, two legs, and his name was me. She couldn't stand me. No, I'm confusing you. She could stand me; it was my love for her she couldn't stand. This was a girl who could not bear to be loved. I loved her. It should have been enough. At least it should have mattered. (He starts to unbutton her blouse.)

So there we were. Me loving her; her ... liking me, and every day the worse it got. She took to drinking, ridiculing my work (I was teaching the new math at the time), (He has worked her blouse down over her bound arms.) Oh, did we ever scrap! (He takes off her bra.) Real knockdown-drag-outs. Name calling, doors slamming, the works. Only trouble was I'd feel just rotten every time I landed her a good rap on the mouth. I'd help her up, walk her to the bathroom, clean the blood up. It used to ruin my evenings. God, it was frustrating. (He is working her skirt down over her ankles.) Anyway, years passed like this. Three, to be exact. And then there was this one morning. I woke up and thought to myself, "I've had it." So I dressed, left her a note and never saw her again. (He pulls down her half-slip.) They say she woke up about four that afternoon found the note and promptly went berserk. She went into a deep and swift decline and was eventually committed to an asylum somewhere upstate. (Short pause.) But she'd taught me a lesson. People ... and I didn't include myself . . . people don't like to be loved. (He removes her panties.)

My second woman ... well, she taught me something, too. When we met, soon after my famous note, she was young, successful (she modeled; pick up any issue of one of those magazines and there she was), and beautiful. It hurt to look at her. And the cherry on the icing was this: this Venus loved me! (Pause.) So now I had everything going for me. I was adored! I mean this girl was put on earth for no other purpose than to love. She hand-laundered my shirts and then she ironed them and put them on hangers. She shined shoes, this girl! But she was more than a domestic, you understand. I'd given up teaching and started writing by then. She helped me! She wouldn't just read the poems and smile and nod her head. No, she'd take a pencil and make x's, change words, edit, everything! When the work was good she made me feel like a king. When it wasn't she'd tell me why and I'd still feel like the best poet who ever lived. She inspired poetry! (Pause.)

Our nights were nearly perfect, our sleep like two cubs cuddled, our mornings a time for the dearest laughter, Our days productive and meaningful and our evenings so quiet and gentle alone together that she lost all desire to see other people. (Short pause.) A different girl, a different ointment, but the same fly, alas. I couldn't stand her loving me. Here I had everything I wanted ... well, everything I thought I wanted ... and I didn't want it at all. This time I didn't leave a note. I told her to her face. "I don't love you.". . . and the next morning she helped me pack my things. She kissed me when I left . . .

I waited until about six that evening before calling her to see how she was getting on. I was glad when she didn't answer. The next night, again no answer. I didn't even feel guilty any more. About the sixth day I began to get worried. By the tenth day I forgot all about the pros and cons of it and just went over there. I had this terribly strong desire to make sure she was all right. Know what I mean? I suspected the worst but it was more terrible than that. She was lying on the bed, the bottle of pills on the floor beside her. The cat looked up startled when I entered the bedroom and scurried away. He'd eaten away a good deal of her face, you see, naturally there'd been no one to feed him, and I guess he knew he was in for a spanking. I called the police. There was an autopsy, cause of death listed as probably suicide and a rather shabbily attended funeral. But then she hadn't wanted friends after me. (Short pause.)

Since then I've lived alone out here in envy of the ants. I think I understand them. People just ... seem strange to me. People ... and since her too I've had to include myself . . . people don't like to be loved.

**************************** The Girl is in the chair. The Man finds his latest manuscript and reads.

YOUNG MAN: It's good, it's very good. I'm going to be famous. (Reading over what he has written.) "The girl is sitting in the chair. For days now there has been no rope. She accepts the life we share." (He frowns; then crosses out with a pencil) Goddamn it, I don't know if you accept! (Reads again.) "The girl is sitting in the chair. For days now there has been no rope." Period. (He smiles) That's more like it. (He puts the page away.) I guess you'd like your little late-night newscast. Let's see. It was cold out. Oh, there was sun all right, but not enough for shadows. They've made a cancer breakthrough. Someone prominent died. Oh! This is of interest. The newspapers have forgotten all about you. There wasn't even a mention this evening.

Oh God, I am so deliriously happy! After all, this is how I always imagined it. I have everything I want now. It will be years before I'm done with you (maybe a lifetime) but you can't imagine how much less strange your body already is to me. Sometimes I look across the room at you and feel I almost know you.. How much better words unspoken are! You're happy here, I can tell. Why, your eyes are glowing, you're almost purring. You belong to someone and that's a good feeling. There's no strain left, we're coexisting, that's better than love. Besides, people don't like to he loved. Just go on breathing, staying at 98.6 and you'll have everything you want.

(He sees something on the floor.) Come on, sweetheart, up you go!

(He has let an ant crawl onto his hand.) Look. My friend, the ant.

Once you understand them, all ants are beautiful, hut this one's especially fine. Look at him struggling, thrashing about, trying to find his way! You're in a little frenzy, aren't you there? I see the little legs going, the antennae twitching a mile a minute. (Moving his hand all the time to keep the ant from crawling up his arm.) Go ahead, exhaust yourself. It's hopeless, but how long before you realize that and settle down in the palm of my hand? It's not worth struggling. Look, he can't stop! His death throes and he doesn't know it. I know what you're thinking, ant: "I'm lost, hut I'll find my way. I won't give up the fight. It's worth my effort. Keep struggling, keep the legs going, the heart beating, and I'll find my way to something better. Don't give up, that's the main thing, don't give up!" Isn't that what you're thinking, ant? I'M NOT GOING TO DIE. NOT YET. NOT ME." (He lets the ant escape)

It's time I thought of a name for you. Laura. Would you like Laura? You don't have to answer now. We're not ready for talking to each other yet. It will come . . . in time . . . everything does. I have everything I want now. Everything!
```

---

## IC-0451: Telephone Man

- Title: Telephone Man
- Author (byline): Chris Crutcher
- Work: Athletic Shorts: Six Short Stories
- Publisher: Harper Tempest
- Publication date as stated: Nov 2002
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: JACK, HAWK
- Teaser before the introduction: Yes
- Spoken words (computed): 2102
- Already set (do not supply): none

### Source block (context only)

```text
Author: Chris Crutcher
Book: Athletic Shorts: Six Short Stories
ISBN: 978-0060507831
Publisher: Harper Tempest
Date (Month/Year): Nov 2002
```

### Introduction (context only: never use it for content warnings)

```text
Telephone Man by Chris Crutcher
```

### Performance text (classify this)

```text
JACK: "Eccentric" is what the teachers at Oakland High School call kids they think are crazy. They use words like that so people like me won't know what they're really saying. Around this school they call me Telephone Man, which is one of the few things I like, even though I know they think I'm a dork for wearing telephone equipment strapped to my hip. But without it, I feel like how the Duke must feel when they make him check his six-shooter at the saloon door. I feel bare naked.

I can fix any telephone that a regular telephone man can fix. I can fix it if the people on the other end can't hear you or if you can't hear them. And if you have more than one phone in your place, I can set them up like walkie-talkies, if they have the right stuff in 'em. That's what I can do.

JACK: Sometimes I wish Hawk wouldn't of saved me from the China kids because it confuses me, and I hate that most of all. When a nigger goes saving you from Chinamen, it throws you off because everyone knows niggers are the worst. It all happened on one of those days when I just don't think. That's what my mom and dad both say: "Jack, most of the time you get into trouble because you just don't think." I got up late that day, and it looked like I would have to go to school without breakfast again. Well, Mom was still in bed and the bus was coming in about four minutes and I looked through the cupboards and I couldn't find anything except there was the Bisquick. Well, I knew that's what Mom made biscuits out of, and I figured, hey, even if they don't taste as good not cooked, they have to be just as good for you, right? I mean, your stomach doesn't know if they're cooked. Everything turns about the same temperature pretty quick down there anyway. There wasn't any strawberry jam in the fridge, so I just ate the Bisquick right out of the box, which it was pretty dry. But then, when I was in the bathroom trying to blast off a pimple from my nose that looked about like a spaceship or something, I saw this strawberry stuff sitting on the bathtub, and I didn't know why it was there; but I did figure it was no big deal if I ate it after the biscuits because like I said before, it all ends up in the same place anyway and your stomach would never know which order you ate it in. Right?

I think it should be against the law to make soap or shampoo that smells like jam and has pictures of strawberries on the front. I mean, it was red and it was thick, and even though it didn't have clumps of strawberries in it and it tasted funny, it looked like syrup, which is close enough to jam to drink when you're in a hurry and just want to get something close to your regular breakfast in you.

Well, what went on inside me probably would of made a good science lesson, I bet. I didn't know how many biscuits you can make out of one box of Bisquick, but I found out later it's a lot. And I also didn't know what happens when you get soap inside you.

I was in history when it hit. There was this sort of rumbling inside me, and all of a sudden I knew I had to get to the bathroom really quick, so I just ran for it. I was lucky enough to get my telephone stuff off and up high out of the way, but right after I did that, I started feeling like a balloon that you just let go of the end. I wanted to save my clothes, and I got my shirt off, but my pants got stuck down around my knees right when my butt just turned into a cannon and I was shooting biscuit stuff all over the whole room.

So everything would of been okay except on my way to the bus I ran into the China kids. The China kids hang out at the top of the stairs, and if they're going to get you, that's where they do it. I saw them there, and right away I was going to go back; but our school bell rings outside and inside, and I heard it and I knew the kids would be changing classes and some of them would come outside and see me if I tried to go back the other way-and I thought they'd know what I did in the bathroom. I think people just know if you mess up sometimes, even if no one tells them. So anyway, I decided to just go ahead and pretend I didn't see the China kids and maybe they'd just let me go to the bus so I could go change my clothes.

But they didn't. The leader, he's a guy named Kam, was practicing that karate stuff, and the rest of his gang was clapping their hands and saying "way to go." They call theirselves the Jo-Boys. That's a really dumb name, and I don't get it; but I wasn't going to say anything. I just put my head down and walked around the corner to the steps, trying to make it like no one could see me. I can do that sometimes, but not this time. Somebody said, "Hey, kid!" but I just put my head down farther and kept walking. I tried to do it like when you're trying to get past a mean dog. My dad told me not to walk any faster or anything, just to act like I'm not there. But this kid wasn't a dog, and he said, "Hey, kid,” again. I tried to walk faster; but somebody grabbed my shoulder, and I turned around toward him and said, "You better leave me alone," but I kept my head down.

But he said, "Well, yeah, but these are our stairs, and we have to charge you to go down 'em," and I said I don't have any money, which was a little bit of a lie because I had enough for lunch, but my dad told me to always say I don't have any. Then the kid who talked to me first says, "What's that you got around your waist?" and I tell him it's my telephone stuff. He wants to know what it's worth, and I tell him it's not for sale; but he just laughs, and Kam tells me to take it off. Now, I'm scared a lot of the time, and most of the time I'm afraid to talk because people just make fun of me because I have this really deep voice and these stupid zits on my nose plus it's hard to get the words in my head out so they sound right. But they want my telephone stuff, and they're just not going to get it. They're just not. I'm almost nobody anyway, but if I don't have my tele-phone stuff, I'm really nobody. Absolutely, completely, and all the way nobody. So I scream, "Leave me alone!" and they start laughing and kind of pushing me between each other. I grab the buckle to my telephone belt and hold on to it tight, and they push me harder, and they start sort of singing, "Leave me alone, leave me alone, leave me alone," so I scream it at them again, only louder this time, and I keep my eyes closed really tight and hold on to my belt buckle with all my might. Sometimes if I scream and scream and keep my eyes closed tight, things just get over.

Then all of a sudden everything stops, and I think maybe it worked, but I keep my eyes closed a little bit longer because sometimes that makes sure everyone goes away. Then I open them just a little and take a peek to see if it's time to get up and run yet.

But what I see is Hawk, and I know I'm done for. See, Hawk is this big nigger that goes to OMLC, and everybody knows if he's after you, you might as well buy a plot in a cemetery somewhere because he might just be the toughest guy in the world. He's never teased me before. Usually Hawk just walks up to me and says something like "Telephone Man, you a kick," and he smiles and shakes his head and walks away.

But now I get it. He gets the China kids to beat me up a little, and then he comes along to finish me off. I think, so that's his nigger trick, and I roll up into a ball because now I know it won't be very long until it's all over.

But then I hear him say, "What you Jo-Boys think you doin' here?" and there's no answer. Then Hawk says, "This here’s Telephone Man. Friend of mine," and still there's no answer. "How many time I gotta tell you China boys don' go be messin' with my friends?"

Kam starts breathing big and kind of crouching like an animal; but right before you know it, Hawk's got him down on the ground, and he doesn't get to use any of his karate stuff because Hawk's choking him right to death. The China kid's eyes are so big they're about ready to explode, and Hawk's only using one hand, 'cause he's looking at all these other China guys, who must be thinking they should jump on his back and help out their friend. But nobody does it; they just stand there and Hawk says,

HAWK: "Come on. I be closin' off you number one Jo-Boy air-hole for him; then I take anybody else want some,"

JACK: And still nobody moves. Then Hawk turns back to Kam and says,

HAWK: "Gonna let you up, China boy. Nice an' slow. You try any you Bruce Lee stuff, gonna embarrass you, front you friends,"

JACK: And he lets a little bit loose. Kam gets up kind of slow, and when he's about halfway, Hawk grabs him by his cheeks between his fingers and makes him look at me.

HAWK: "You see that boy? . . . Got all kinda telephone stuff on him?"

JACK: Kam doesn't say anything, so Hawk moves his head up and down for him, like he's saying yes, and then Hawk says,

HAWK: "You touch him, you touchin' me. Unnerstan'?"

JACK: Kam doesn't say anything again, so Hawk moves his head up and down again.

HAWK: "Now you Jo-Boys, get on. This over here be my school, an' you got no binnis here."

JACK: Hawk walks me down the stairs to the bus stop then starts walking back up the stairs. When he gets about halfway back up, he turns and says,

HAWK: "Hey, Telephone Man," (grinning) "You a kick. An' you right. Don' be lettin' nobody get that telephone stuff off you. That's you one big thing."

JACK: So then I'm on the bus and no niggers beat me up like they were supposed to. In fact, they helped me, and so now what was I supposed to do? I quit worrying about it for a while, though, because there was this awful smell, like somebody hung a bunch of strawberries down in the sewer, and I figured out I wasn't all done in that rest room and probably getting beat up made me quit paying attention and I had gone and messed up the sweats Willie Weaver got for me out of the Lost and Found. I’m pretty sure the people around me noticed it because of the way they looked at me and then how the ones with perfectly good seats got up to stand near the back of the bus. So I got out at the next stop and walked on home. While I walked, I got to think a little bit, which is something I don’t usually like to do because it makes me feel nervous, and I wondered if my dad would mind if I stopped hating niggers for a while. I really love my dad and I wouldn’t stop if he said not to, and I wasn’t going to ask him right out because I didn’t want to disappoint him – but if my dad made a mistake about them, I wonder if he could of made a mistake about the other colors, too.
```

---

## IC-0452: Tell Tale

- Title: Tell Tale
- Author (byline): Jeffrey Hatcher
- Work: Three Viewings
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Jan 1998
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: EMIL, TESSIE, JIM
- Teaser before the introduction: Yes
- Spoken words (computed): 1618
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jeffrey Hatcher
Book: Three Viewings
ISBN: 978-0822214946
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
Stalkers come from every walk of life and every socio-economic background. Virtually anyone can be a stalker. Take Emil for instance – married, soft-spoken and a bit of an introvert. He works as a funeral director, so his interactions with people tend to be a little, shall we say, scripted. But lately, he’s become obsessed with a local real-estate agent; and his infatuation is becoming something of a problem. A scary, creepy, dangerous type of problem. . . Tell Tale by Jeffrey Hatcher
```

### Performance text (classify this)

```text
A man, Emil, stands downstage in the light. Middle-aged. A conservative charcoal suit and dark tie. His jacket is buttoned. Behind him are three floral arrangements with flowers in deep reds and purples. Emil stares out front, slightly off to the side.

EMIL: (Lightly - a hushed chant.) . . . . I love you. I love you. I love you. I love you. I love yo - (He abruptly snaps his face forward.) She-almost-saw-me! (A moment to steal a glance back at "her." Beat. He breathes a sigh of relief) Wheww! That was a close one. Real heart-stopper. The beat coming out of my shirt like a bomb about to explode. Bum? bum! Bum?bum! Bum?bum! (He looks off to the side again.)

I started with just one. "I love you." Very quiet, very small. But audible. "I love you. " Said to the back of her head as she moved through the room. Holding hands. Smiling. If she turns around in the middle of "I love you," I thought, she'll catch me. She'll catch me, and I'll be happy to be caught. But one "I love you" wasn't really enough. One "I love you" was too ... subtle. So I advanced to two. I went to three. "I love you. I love you. I love you." Nothing. Now I'm up to nine. And this is the first time she's almost seen me say it. What would I have done if she had? (He stares off at her.) Next time I'll have to go up to ten.

EMIL: Nettie James died yesterday. She was 103. Been on the verge of death for twenty-eight years. Very rich. Terrible woman. I got Tessie in. Not that the James family is going to sell the house on Norton Place let alone use Tessie's real estate company, but it's good for Tessie to be seen, and I got her on the list. She's in the visitation room.

I'm up to 12. I love you. I love you. I love you. I love you. I love you. I love you. I love you. I love you. There's nothing more obvious in life than one person looking longingly at another - unless it's a person desperately trying not to look at all. (beat)

I hate her name. Tessie. Not Teresa, not Tess - Tessie. I love you. I love you.

We go into the service. My mind withdraws to other places. It's a depressed real estate market. Tessie, she's talented. The way she can describe a house .... I've almost bought four myself. She's on commission, and it's getting tight. A slow season. She tells me about wanting to travel, to get away. Mexico. The Berkshires. Spain. I tell her how difficult it is for me to get away: "No slow season." She laughs. Her laugh. Her smile.

She has not had an easy life. Father was an alcoholic - mother spent twelve years dying in the state hospital - the divorce. And she wears a pacemaker, Tessie - something congenital - to regulate her heart. I love you. I love you. I love you. I have to help her. I will find a way to help her. (Blackout. Lights come up.)

I have started to give Tessie advance word of imminent deaths.

Sometimes I get a warning. Hospital. Police. "A friend in power." Last week Bill Goodpastor tells me his wife Marge has a brain tumor, Bill thinks she may not last the week. Marge is dying, the house is too big, Bill told me, I told Tessie. Unethical? Maybe. It's a slippery slope, but passion is a bracing lubricant.

I love you I love you I love you. I'm up to seventeen now. I'm starting to think she knows I'm saying it, and that's why she doesn't turn. I have considered driving past her house at night. The light in the window, the nose pressed against the pane. But I have restrained myself. That way leads to madness, the padded cell, the perch in the book depository window. I am not like that. Why don't I just tell her? What's the worst that could happen? Mockery. Humiliation. A howl of derision.

Anyway, Marge Goodpastor died yesterday. Bill called from his Jaguar. Tessie came early to the visitation - I wanted to introduce her to Bill before the rush and the cremation. I am making this vow: If my "I love you" gambit does not prove fruitful, I will take drastic action. I will tell her my true feelings before the year is out. Tomorrow is Thanksgiving. I have 35 days. (Lights fade. Lights come up. Smiles.)

Tessie said "I hate you" today, and I think there's hope! At The Green Mill. We bumped into each other outside the bank, Christmas shopping. I offered lunch. She said she had to meet Bill Goodpastor to show his house. "BUT," she says ... and I quote her .... "OH - WHAT THE HELL - LET'S - HA VE - LUNCH." (Big proud grin and giggle.) What do you think of that! We were talking about these last few "referrals" I've made her. She sold three houses. Good commissions. She's breathing a little easier now, and she wanted to take me to lunch. I told her, "You know, I can't keep slipping you these tips forever, we're gonna run out, I'll have to start killing them myself." (He laughs, mock-sinister.) HEH-HEH-HEH. She laughed. She said, "You're terrible, I hate you!"

And she slapped me! Just my lower arm, across the table, next to the coffee cup. Her fingers brushed my wrist, near my watch, skin to skin. I almost jumped. Red face. Adrenalin. Dizziness. Vertigo. Just a touch on my wrist.

This has happened to me before. This sort of thing. It goes away. I let it run its course. Lasts a few weeks. This one is in its eleventh month. I will tell her by December 31st. New Year's Eve. But I wish she'd guess it first. I wish she'd tell me. Read my mind, read my lips. Suddenly - out of nowhere - she asks me a question.

TESSIE: Do you know when you're in love?

EMIL: What?

TESSIE: I said, Do you know when you're in love?

EMIL: Oh yes.

TESSIE: How?

EMIL: (To Tessie in an obviously emotional voice.) You always know. Knowing isn't the point. The point is action. The point is speaking. That kind of action, that kind of courage ... Why do you ask? (To audience) She doesn't smile. She looks at me. Three seconds, eye to eye. One. I love you. Two. I love you. Three. I love you. I'm shouting the words in my mind, but my lips are sealed, surely she can hear me, PLEASE, GOD, LET HER HEAR ME! She breaks her stare.

TESSIE: Never mind.

EMIL: She'll pay the check, I'll leave the tip. Exiting, I place my hand under her elbow. She allows it. She does not comment. Outside, she kisses me goodbye. Cheek. Another detonation to the skin. My heart is racing. She walks away. Today is December 7. A date that will live in infamy. I have 24 more shopping days. (Blackout. Lights come up. Tense and angry.)

Ed Carpolotti died, and Tessie didn't come to the funeral. It was a three day affair! I'd left a message on her machine telling her about Ed. Just the usual. But there was no reply. A day passes. I call her again, get her machine, leave another message. No reply. Two days more. I tell Jim Zimbro: "We should go another day, not everyone who would want to see Ed has had the chance."

JIM: (looking at him as if he’s nuts) You want to extend it?

EMIL: What about Art Wise. And Johnny Criss and Bill Goodpastor . . .

JIM: Bill's in Florida. He went down Friday. He and Tessie.

EMIL: Bump-bum ... bump-bum ... bump-bum ... bump-bum ... I slam down the coffin lid! My heart is pounding! Had she been seeing him long? Was it him she was talking about at The Green Mill? Did I miss something? Was there a code she was using? Had she been saying "I LOVE YOU" TO ME AND I JUST WASN'T LISTENING? DOES SHE HAVE ANY INKLING AT ALL? AM I A FOOL! BUMP-BUM! BUMP-BUM! BUMP-BUM! Will someone not stop this ridiculous heartbeat! Surely, everyone will hear it! Surely everyone in the room can HEAR IT!!! (He has reached an explosive crescendo. He finally stops, looks out, fearing he's been caught. His voice is a hushed rasp.) But they do not turn, they do not hear, they do not see. I am not caught.

The hospital called me at eleven twenty-two. An accident on the drive from the airport. Icy roads after Christmas, a slippery slope, a Jaguar over the hill. Bill Goodpastor is dead. So is his passenger. (Pause.)

They bring her in the next afternoon. I notice her hair. Gray at the roots. Was she letting it grow out? Or did she just not have the chance to color it? I attach the machine, I prepare the instruments - needles, tubes. Her partial plate out, I smooth the crow’s feet around her eyes. I do ... what we do . . . to her eyes, her lips. What we do is ... we seal them. Little known facts. Some things don't burn in a crematorium. Diamonds. Some metals. Heavier bones. Some things you can't burn. Like pace-makers. The heat makes them explode. You can damage the inside of the chamber. So it's important to remove them before you ... set fire to the body. (He holds up a small transistor-sized object.) I found this in the preparation room. I really should have given it back to ... someone else. (He holds it up to his ear.) It keeps on ticking.

(Pause.) The funeral is crowded. Zimbro asks if there is anything he should add to the service. "Say something about Mexico, the Berkshires and Spain." I've spoken too loudly. Heads have turned. The casket is closed. And by three o'clock that afternoon, Tessie is gone. Across the room I see my wife - (He looks out front.)

Tonight is New Year's Eve. My wife is upstairs in bed early, and there aren't any customers in the viewing rooms. For the first time in memory ... we are entirely empty. (He holds the pacemaker and looks off at her)

Turn around. Turn around. Look at me, sweetie. Please look at me this time. I'll say it again. I'll say it a thousand times until you turn around and catch me. I love you - one I love you - two ... (Lights fade to black.)
```

---

## IC-0453: Tennessee and Me

- Title: Tennessee and Me
- Author (byline): Will Scheffer
- Work: Falling Man and Other Monologues
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: March 1999
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: ME, TENNESSEE
- Teaser before the introduction: Yes
- Spoken words (computed): 1133
- Already set (do not supply): none

### Source block (context only)

```text
Author: Will Scheffer
Book: Falling Man and Other Monologues
ISBN: 978-0822216681
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): March 1999
```

### Introduction (context only: never use it for content warnings)

```text
“For nowadays the world is lit by lightning, so blow out your candles . . . “ This line closes out one of Tennessee Williams most famous plays, The Glass Menagerie . . . . They are uttered by Laura’s brother, Tom. When Tom talks of the world being "lit by lightning," what he means is that he has made the plunge - he has left the quiet sadness of a world lit by his sister's candles and traded it for the unceasing excitement of a lightning storm as a member of the merchant marines. He asks Laura to blow out her candles - in effect, for her memory to stop haunting him - because he no longer sees the world by the dull light of candles. Instead, his world is lit by the excitement of lightning. As much as it pains him to do it, he needs to leave her behind and embrace the decision he has made to live in the heart of lightning.

It is this line that forms the basis of this dramatic interp. In it you will meet a street-wise male prostitute known only as “ME” who is struggling with his sexuality. It is through his interaction with the confident gay spirit of Tennessee Williams that he comes to realize that, rather than being a frightening place of uncertainty . . . the world truly is “lit by lightning.” ME must leave the past behind to embrace and accept his sexual identity and the future that is to come.

Tennessee and Me by Will Scheffer.
```

### Performance text (classify this)

```text
ME speaks with a heavy New York accent. Tennessee speaks with a very broad deep Southern drawl.

ME: On February 25th, 1983, at approximately 2:00 in the morning, while taking a hot bath in his suite at the Hotel Elysee, the great playwright and notoriously alcoholic homosexual, Tennessee Williams, died amidst the bubbles, asphyxiated by the cap of a pill vial, lodged in his throat.

Lighting candles as he speaks

ME: It so happens that on that same unfortunate morning about an hour earlier, I - who at that time was a rather inarticulate male prostitute from Bensonhurst, Brooklyn - was running naked through the lobby of the Holiday Inn on 48th street, having just extinguished a cigarette in the sagging white belly of a Pulitzer Prize-winning poet, who had paid me five hundred dollars to do so, but who now seemed to be suffering from mild cardiac arrest apparently brought on by my action.

Grasping my five hundred dollars, I ran from the hotel and lunged into a waiting taxi and throwing a one hundred dollar bill into the front seat ordered the gaping cabby to take me to the St. Marks Baths, a popular gay bathhouse on the lower east side that flourished in the innocent age before the plague had come to live with us in this city of strangers. Upon checking into the baths that night I procured for myself the honeymoon suite. The only room in the entire place with a double bed, and at precisely 2:00 A.M., exactly as uptown Mr. Williams was choking in his tub, [I] staggered to the mirror and stared in shock and horror at what I saw reflected there, for the eyes that stared back at me were not my own, and I knew somehow quite clearly, that in one shining instant, oblivious as to how and why he had chosen me, the soul of Tennessee Williams had leapt into my body like a candle flame leaping into the dark night; I was possessed.

ME: What are you doing?

TENNESSEE: I'm moving in baby.

ME: You can't move in. Get out of me!

TENNESSEE: But honey - we've had this date with each other from the beginning.

ME: Why do you have to move into me?

TENNESSEE: I've come back for love, baby . . . and you have the body to get it for me.

ME: I don't even know who you are!

TENNESSEE: Jus' hush up then . . . I've always depended on the kindness of strangers.

ME: (to audience) This was indeed a predicament of major proportions for me, as I had practiced a lifetime avoiding such flagrant effeminacy. And so fleeing from the baths, I instinctively searched for the nearest Catholic Church, believing exorcism to be my only hope.

When I entered the Church of the Heavenly Mother on Third Street it was empty, save for a rather young and attractive priest who was wearing a simple black habit and swinging a smoking incense burner over the altar. I ran to him, genuflecting at his feet. I was about to explain my unfortunate situation when Tennessee who was putting up a tremendous fight to inhabit me, lurched into high gear. And again unable to control myself, while looking the priest up and down, I intoned: "DAHUNG, I love your dress but your bag's on fire." Expecting the priest to take grave offense I cringed before him. But I was surprised when I heard him let out a fluttering shriek of a laugh. And soon it was quite clear to me that this Tennessee Williams was planning to move in for good. I began to speak with a southern accent even as I despised his presence inside me. (Southern accent creeps in.)

He dragged me to bar after bar in search of love, to all the bars I had frequented before to earn my living. Sometimes he would have me affect my most unavailable demeanor, and on those nights we were remarkably successful at winning the favors of boys of all different colors shapes and sizes.

TENNESSEE: The only thing that homosexuals hate more than women is themselves!

ME: (To audience) But it really didn't matter. Any way we played it, the elusive love that Tennessee had come back for, continued to elude us. I however became used to having Tennessee in my body. We had a strange sort of marriage, and for the first time in my life I experienced a more delicate sensibility. I became morose, I began to think about the sadness of the world. I bought a typewriter and started to write bad plays which Ten-nessee criticized unmercifully.

Then one night the impossible happened. We both fell in love with the same boy. A bright particular boy. Tennessee made me kiss him . . . right on the mouth. Something I had never done before, not even for money - because I guess I knew that it would make me a real homosexual. And the boy kissed back with sincerity. And I found that I liked it.

The object of our mutual infatuation was Freddy, who was in all ways a delight to behold, both in appearance and personality. I suppose Freddy was a notoriously modern homosexual. You know the kind: full of himself, unashamed, in your face . . . beautiful. He seemed actually to contain a wholeness of qualities that might best be described as a self. And the tragedy was: that Freddy really did love us. And I came to understand that this love was unacceptable to Tennessee and me. It was not long after that, while taking a bath, that Tennessee told me he was departing.

TENNESSEE: It's all loss here honey, and I could never bear it. Never then and never now, but thank you for the ride.

ME: Please don't leave me Tenn. I'm just street trash without you. TENNESSEE. No you're not baby, you just need to take hold of yourself - and gently, gently with love, hand your life back to yourself.

ME: (to audience as he begins to blow out candles around the acting area. One at a time.) And then he was gone - flying up, up in his bathtub, and into the night. Now I live alone. But there is something of Tennessee that remains with me still. A longing, a nostalgia for a time that will never be again. I might even go so far as to say that I miss those old days. Perhaps I am walking on the streets of this city, and I pass the old location of a bar or a nightclub that we used to frequent. Or perhaps I hear a familiar strain of music, a Donna Summers song, and the memories of that time rush back upon me, like the crystalline lights of a mirrored disco ball, like a thousand pieces of broken glass - Oh Tennessee I tried to forget you. But it's been harder than I ever thought it would be. For nowadays the world is lit by lightning, so blow out your candles, Tennessee. And so good-bye. (blows out the last candle)
```

---

## IC-0454: There Has Possibly Been an Incident

- Title: There Has Possibly Been an Incident
- Author (byline): Chris Thorpe
- Work: Not specified
- Publisher: Oberon Books
- Publication date as stated: April 2014
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SPEAKER
- Teaser before the introduction: Yes
- Spoken words (computed): 1511
- Already set (do not supply): none

### Source block (context only)

```text
Author: Chris Thorpe
ISBN: 978-1783190409
Publisher: Oberon Books
Date (Month/Year): April 2014
```

### Introduction (context only: never use it for content warnings)

```text
Everyone tends to think of themselves as the hero of their own story, at the very least they know they're "right." What is your idea of heroism, of compromise, of individual and collective action? You see, its small acts of choosing or not choosing that either pass unnoticed or send ripples around the world.

Revolution . . . it’s not just fading ink in history books. It’s happening today. All over the world. Myanmar . . . Sudan . . . Ethiopia . . . Haiti . . . the 2021 attack on the US capitol. You don’t get to vote on a revolution. That’s kind of the point.

There Has Possibly Been an Incident by Chris Thorpe
```

### Performance text (classify this)

```text
SPEAKER: I'm listening to someone I have known for years, telling me, with restraint, something terrible. I know this Incident, to be terrible even though the man in front of me is not telling me the detail of it. I know this thing to be terrible because I said it was a good idea for it to happen. But still I need to be told in an untraceable way. We are both comfortable with this because we are aware of responsibilities higher than a responsibility to ourselves. And one of his responsibilities is to tell me, in person, news like this.

A long time ago now, I saw this man who is standing here in my office, in a tailored suit, save the life of another man and a woman, who, all things considered, probably deserved to die. I saw him commit one act of mercy and years later, here we are.

SPEAKER: Years ago we stood on a balcony over a square that was no longer square. The edges of the buildings were so eroded, so pulverised by shellfire that there were no straight lines. We hadn't levelled this building because, I think, there was some agreement, that there would be a moment for people like us. People so long denied the chance to do so by the people entrenched in the building, to stand on that balcony just once as the proxies of everyone below.

I stood on the balcony and raised my arms with the others and the air was electric with promise and noise. The noise an, as yet, unformed roar, before the slogans were written that would carry us all into the future. And while we stood on the balcony, another man and a woman knew their time was finished, that the long, cruel game was over. They sat in straight-backed chairs and looked at the guns, and the tired young people -- Young, like we all were back then, younger than them by far. They would follow the tradition of deposed and hated rulers everywhere and in one of several possible ways, die.

That day on the balcony, the man who is now sitting in my office was the one who decided to fetch the two and bring them out onto the balcony for the last time. We were the focus for those “waiting to see what happened next” and also the “arbiters of what happened next.” In that situation, someone has to step forward and answer. What now? This. And we were turned into the people they so desperately wanted to see in front of them.

He installed our former rulers on the balcony as a centerpiece. The crowd shredded their throats. It's something I notice when I watch the footage of that moment. It's a reflex, surely, but I think I see the woman's lips pull up at the corners for a fraction of a second. Her hard-wired response to adulation -- forced adulation. Encased in its false worldview, her brain is unable to distinguish between the sound of forced love and the sound of pure hatred. We allowed them to stand for a long moment, bathed in light and noise. The noise congealed into peaks and troughs. The first new chant of a new era. The crowd, seeing their former rulers, has made its first decision about the new state of things, and that decision is. Kill them.

And, on the balcony that day, this is what happens. The moment that leads us to now, to here, today, this office, and what we have become. On the balcony, unexpectedly, to all of us, he lifts his right hand. The hand says. Silence. That's what the crowd interpret. And the crowd obey.

And he says, “This isn't about what we want right now. This isn't about revenge. (Beat) What do you want?” And the crowd say. Kill them. And he says, “I'm not here to tell you what should be done.” And the crowd say. Kill them. And he says, “Not yet. Let's think about the kind of society we want to build, now we have the chance. And someone in the crowd says, they've been killing us for years. And he says, “Yes. But do we want to go on living by the rules they created?”

And in that moment, we are separated from the crowd. We are holding our former oppressors at gunpoint. And we are also the crowd's hope, personified -- The new leaders deposing the old. In that moment him sitting there and me sitting here and all this (gestures to the office around him) becomes somehow inevitable.

The crowd no longer says kill them. Something in the appetite is gone. There's a shift. A feeling that we, the random collection of tired and ragged people on the balcony, flanking our former oppressors, have somehow taken responsibility. That we're being given a chance. If we're going to set ourselves apart. If we're going to refuse to do what the moment demands, then we had better damn well make ourselves responsible. We'd better, the crowd says. Ridiculous I know to treat a crowd like a thing of single intent, but there it is. We'd better have a plan.

And so we fall into it. Or step into it. On that balcony, on that day. Making promises designed to at least make it appear we know what we're doing. If we'd been asked to articulate our vision back then on the balcony, I don't think it would have included this. This moment, in this office, now. At that moment just after the old man and the old woman had disappeared inside to face a trial, just as soon as there was a system in place to try them. If we'd been asked, what do you want? What is your alternative? We'd have stared. And we'd have said. (Beat) Something else. We knew the answer needed to be better. It has taken us years to realize the answer would include this day -- This news -- This Incident.

We began to learn. We learned, for example, that for something worthwhile to happen it's simply not enough to wish the situation to be otherwise. It's simply not enough to wish the situation to be otherwise.

As the years progressed, I found I had an aptitude for leadership. I have done what had to be done. One day I will step away. But now, I'm still acting to structure the future. And that future is still something I believe in.

When I had to close the first newspaper, I did it because I believed in a future defined by free speech. When I asked for calm and quiet for the sake of stability, I believed in a future defined by the freedom to protest. The jail terms were brought in because people apparently just won't listen when we say that change is not something that happens overnight. Not if you want it to last.

It's not my fault. I told them loudly and honestly. People won't listen because that's how people are. And I said to the ones who objected to the jail terms, what would you rather we did? Remember that day on the balcony. We aren't murderers. We don't even murder our enemies. You wanted that. I'm only here to see my part of the job through and no more.

And I believe that. I'm only here, still, because I haven't finished safeguarding the future. As the man sitting opposite me tells me that the Incident, what had to happen, has happened. On my orders, my deniable orders of course, but still my orders, a small number of officers in one part of the army in a single city on the border full of spies and liars and agitators have shot some young soldiers who refused an order to fire on a demonstration. And then the army fired on the demonstrators anyway. They fired on the demonstrators anyway because I decided that had to happen.

Of course, there'll be no trace of my part in this. The officers will be shown to have been acting alone, and they will be punished. We've become very good, over the years, at erasing the chain of command, up to and including conversations like this one. Because who in their right mind would order officers to execute young soldiers acting according to their conscience? And who in their right mind would order soldiers to fire on demonstrators? It happens. But who in their right mind would order it? Not us.

We started this with an act of mercy. A public act of mercy. One arm movement from one tired man, but we all stepped forward behind it. I stepped forward, as it turns out, further than the others. We started with an act of mercy, a public act of mercy. I don't know if we shouldn't have killed them. Thrown their bodies from the balcony to the crowd.

Today, there's another crowd below. I need to go and explain to them, that despite this Incident. This regrettable Incident. That nothing has changed. We're still heading in the right direction.
```

---

## IC-0455: Thief River

- Title: Thief River
- Author (byline): Lee Blessing
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: May 2002
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: RAY, GIL
- Teaser before the introduction: Yes
- Spoken words (computed): 1989
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lee Blessing
ISBN: 0822218399
Publisher: Dramatists Play Service, Inc.
Date(Month/Year): May 2002
```

### Introduction (context only: never use it for content warnings)

```text
Actor 1: We may not be your neighborhood high school lovers whose romance culminates in an at long last happy ending, Actor 2: Neither do we have any steamy sex scenes or indulge in any questionable on-stage nudity. Actor 1: But whatever your sexual orientation, Lee Blessing's take on love is universal and less about sex than about the courage to live a full life rather than a safe but half life. Actor 2: After all, the way you fall in love is "one confession at a time." TOGETHER: Thief River by Lee Blessing
```

### Performance text (classify this)

```text
Background: Ray's son is getting married; Gil shows up out of the blue, with his new lover, Kit. Gil is Ray's best friend from twenty years before, and his first and only love.

RAY: What's his name again?

GIL: Kit.

RAY: Kit? That what you made him out of?

GIL: He's sharing my life right now. I'm not surprised you forgot his name.

RAY: It was sort of hard to hear while we were dragging him from under the pews.

GIL: I'm so sorry for that. I never meant to—

RAY: Jesus Christ, Gil. What in the hell are you doing? What are you doing? (BEAT) How can you be with that?

GIL: You don't even know him.

RAY: I know he's half your age.

GIL: You think I should be with someone appropriate?

RAY: Yes!

GIL: Like Molly? (As Ray gives him a hard stare) We're really kind of an adorable couple. You should come visit us sometime.

RAY: I don't think so.

GIL: We're very quiet at home. He wants to move, and I don't--that's about the biggest issue.

RAY: You'd be so lucky to be rid of him.

GIL: Of course, I suppose there are a lot of men who'd be delighted to have someone to settle for at all. Not Kit, though. He's too beautiful. So am I. So are you. We shouldn't have to settle.

RAY: I'm a married man.

GIL: Does your son know about me?

RAY: No.

GIL: He really wanted to kill me today.

RAY: I wanted to kill you myself. I haven't seen you in twenty years, and this is how you--?

GIL: I said I'm sorry—

RAY: Sorry? For Christ's sake, what were you thinking?! Why on earth did you come up here?

GIL: Twenty years. It has been that, hasn't it? And every week, for twenty years, you wrote me a letter. What were you thinking?

RAY: Those letters were about how I could not be with you.

GIL: "I cannot be with you." Once a week, every week, twenty years. They came no matter what. Even after you got married and asked me to stop writing back. Made no difference. The letters kept coming. Monday morning. "How about that? A letter from Ray."

RAY: They were a kind of meditation. Like writing in a journal.

GIL: Oh, I was supposed to meditate? Didn't realize. "I love you, Gil"--that was in every letter. Was I supposed to meditate on that? Or how about, "Gil, you should see the hillside behind Logan's Drug. It's covered in wild roses."

RAY: Why are you here?

GIL: First, I apologize for what happened at the wedding rehearsal. I had no idea that was today, and I had no idea that Kit would—

RAY: Why are you here?!

GIL: Isn't it obvious? You stopped writing. (Ray changes the subject; softens his voice)

RAY: Look at Perry with that horrible kid of yours. What on earth you think they're talking about?

GIL: Kit's very well read in certain areas. What's Perry know about lingerie?

RAY: If they're talking flannel, everything. Perry can sit and listen to anybody about anything. Listens to all sides, too. That's pretty rare up here--well, you know.

GIL: Maybe we should've died here. Like a pair of great lovers.

RAY: Most patient man I know.

GIL: Who?

RAY: Perry. Haven't you been listening?

GIL: Haven't you?

RAY: I can see why you want to be with me. It's like we're married already.

GIL: Like we always have been. We'd be such a great couple. We wouldn't have to live in Brooklyn Center. I wouldn't make you do that.

RAY: We sure couldn't live here.

GIL: We'd go to New York; we'd both be lost. We'd be this aging gay couple, holding hands on the sidewalk, no matter how corny it looked--except at night, when the kids from Jersey with the baseball bats show up.

RAY: Where do you get all this?

GIL: I read.

RAY: Believe me, you're making New York sound real attractive.

GIL: It is! You can say, "I'm gay," and—in general--they won't kill you. (Ray gives him a rueful smile)

RAY: Where'll I put all my personal things.

GIL: Personal things?

RAY: You know--wife, son...(Gil goes silent)

GIL: Trunk. Open it up once a year on Christmas.

RAY: Doesn't sound fair.

GIL: I was there first.

RAY: No, you weren't. I was going with Molly—

GIL: (Pointing to Ray's heart) I was there. First. (BEAT) Why'd you stop writing me?

RAY: My son's getting married.

GIL: So?

RAY: Twenty years. What was I doing? Who was I doing it for? I didn't know anymore. I couldn't...Nobody can live on that, Gil. It's a ghost. (BEAT) Besides, I have to be a family man. I have to be for them, or I'm not...for them.

GIL: Hard to be articulate when you don't believe what you're saying.

RAY: I don't expect you to understand—

GIL: Why? 'Cause I didn't make a fake family?

RAY: It's not fake!

GIL: You are. Every week, when you write that letter, you are fake. No. I take it back. That's the one time you're genuine.

RAY: What we had was over a long time ago—

GIL: It's not over. You know, maybe I wish it was over too, but it isn't.

RAY: Gil—

GIL: If it was over, you'd have shoved Kit and me back in our car and told us to get the hell out. But you didn't. Look where we are, Ray. Look where we're standing.

RAY: You know the kind of questions that are going through my family's minds right now?

GIL: I'm sorry.

RAY: You destroyed the rehearsal. I suppose I'm lucky you didn't stumble in here tomorrow and ruin the real thing.

GIL: I don't pretend I know what I'm doing here. Any more than you know--really--why you stopped writing. All I know is that I have questions. About us. I need the answers. You know, it's totally different out there. The way we grew up...here...you're right, we probably couldn't have done it, but now...I can be a person out there. So can you. And it's only going to get better—

RAY: You're with Kit.

GIL: And you're with Molly, but I don't see them here.

RAY: I can't rip up everyone's life around me.

GIL: You're better off lying to them?

RAY: Why not? It was better to lie. She earned that lie. All she's ever done is love me. (BEAT) I won't leave them. I won't leave my son.

GIL: He's a grown man. He's getting married. Besides, he hates people like us.

RAY: Ray Junior's his own person--all right? I mean, you walk in all unannounced with that...that creature—

GIL: He's not a "creature"—

RAY: My son's never seen anybody like that, he's never been around—

GIL: And that gives him the right to throw Kit over a pew? What the hell kind of values did he grow up with,Ray?

RAY: Our values! This town's values! I did what I could, I told him everyone's a human being; that doesn't mean he has to listen to me. He's got his own mind. I can't change that--I wouldn't change it. Why in the hell did you bring Kit in the first place?

GIL: I didn't want to. He insisted. He lives with me,Ray. You think I can hide how I feel? He's jealous and he's just trying to fuck everything up in his own, adorable little way.

RAY: And he doesn't matter to you?

GIL: I don't know. That's what I'm saying. That's why I'm here. I want to find out. I want to know, if you and I can—

RAY: We can't. (BEAT) We won't. You and Kit get in your car. Get out of here.

GIL: God sees us, Ray.

RAY: Will you get out?

GIL: God sees us.

RAY: When did you get religious?

GIL: I didn't. But God sees what He made. I don't need religion to know that. (Holds his hand up, studying it) My body is religion. Each cell. What I know in each cell. It's all we are: billions--trillions?--of cells. Each one with a wall. Each and every one. Trillions of walls. That's what we're mostly made up of. Walls.

RAY: Some of us are mostly made up of horseshit.

GIL: But which ones? (BEAT) Say you don't love me. Say it. I'll go. (SILENCE)

RAY: Some nights, when Molly's asleep--in the same room, in the same bed where you and I first...I'll get up, and...I'll go downstairs. I have to walk way on the far edges of the steps so they don't creak, and...eventually I'll get downstairs. And I'll see the living room. You remember that day in the living room.

GIL: Yes.

RAY: And if it's summer I'll go out on the porch. And I'll just sit there on the rail, where we sat. That night you first held my hand. In the dark. For an hour. (BEAT) And then I'll go back upstairs to bed. Some nights, I can even fall asleep again.

(BEAT) In the morning Molly's always so pretty. Always so rested. She has so much energy.

GIL: Molly's a strong woman.

RAY: She is.

GIL: She'd survive losing you.

RAY: You don't know a thing about it. I married her. We had a son. That's it--that's my life. I take care of them.

GIL: What if it comes out?

RAY: What?

GIL: You and me.

RAY: It's not going to come out—

GIL: I could make it come out.

RAY: If you did, you'd never hear from me again.

GIL: What have I got to lose?

RAY: She'd never believe you.

GIL: I have your letters, Ray. I brought them with me. Boxes and boxes.

RAY: You didn't. You did not bring those letters.

GIL: Actually, I did. Glad I took the hatchback. They just fill it up. Go out and check if you want.

RAY: I want 'em back.

GIL: Sorry, they're my property.

RAY: They're mine! They were private, to you. They're who I am inside. They're not for other-Jesus, Gil.

GIL: Maybe I'll put 'em in the paper. Or hell--my travel editor might know somebody. "Gay Journal From The Heartland." What do you think?

RAY: It'll take away everything. I won't have them; I won't want you. Is that how you want it?

GIL: Is it worse than what I've got?

RAY: My whole life I've lived without you. We've lived different from each other.

GIL: You'll change.

RAY: I can't.

GIL: You change every day! You change in the time it takes to write a letter. You change whenever you dream. Whenever you think about me.

RAY: What do you want? What do you want me to do?

GIL: I want us to take a week. You could come down to the Cities. You can tell Molly something, I'll tell Kit something. We can stay in a hotel and just...see.

RAY: I can't be gone a week.

GIL: Maybe not a whole week. Maybe a couple of days. It might not take that long. We could realize right away that it's not going to work—

RAY: No excuse would sound right to Molly.

GIL: If you don't find out now, when are you going to? Now's the time, Ray. Now's the chance. Don't let it all just...flow away again.

RAY: What do you think's going to happen in a few day's time in a hotel? (BEAT) Is life even real to you, Gil? Do you care how many people you--?

GIL: No. I don't care. Want to know why? 'Cause nobody up here ever once asked themselves, "What does Gil need? What's his deepest wish in life?"

RAY: They're not responsible for—

GIL: They were sitting in this town, all warm and toasty and accepted, while I was in the hospital, or down in the workhouse, or scraping my way through three abusive college relationships--all with guys that looked exactly like you—

RAY: We never—

GIL: A few days. Together. Then you decide. I promise I won't bother you again.

RAY: No one sees the letters?

GIL: I didn't bring the letters.

RAY: What?

GIL: I didn't bring them, I was...I was lying. I need you to come.

RAY: Christ.

GIL: I had to think of a way. That's all. It was stupid.

RAY: That's an understatement. Where are my letters?

GIL: In my dresser, at home. I'll burn them if you want We can burn them together.

RAY: You saved 'em all? Every one?

GIL: Yeah.

RAY: Twenty years?

GIL: I could tell you what it is in shoeboxes. (BEAT) Well, tell Ray Junior I'm sorry. Tell him congratulations for me. (Starts to walk away)

RAY: I'll come down.

GIL: What?

RAY: Can only be a couple days—

GIL: That'd be all right.

RAY: You sure?

GIL: Whatever you can spare. Are you sure?

RAY: (BEAT) Yeah.
```

---

## IC-0456: Things You Should Know about Flying

- Title: Things You Should Know about Flying
- Author (byline): Kennon Dell and Christopher Scarpo
- Work: Fast Horse Plays, Round 6
- Publisher: Create Space Independent Publishing
- Publication date as stated: May 2015
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: ALEX
- Teaser before the introduction: Yes
- Spoken words (computed): 1266
- Already set (do not supply): none

### Source block (context only)

```text
Author: Kennon Dell and Christopher Scarpo
Book: Fast Horse Plays, Round 6
ISBN: 978-1512244120
Publisher: Create Space Independent Publishing
Date (Month/Year): May 2015
```

### Introduction (context only: never use it for content warnings)

```text
Things You Should Know about Flying by Kennon Dell and Christopher Scarpo.
```

### Performance text (classify this)

```text
Alex; is nervous but expressive, generous but guarded. He is somewhere between 20 and manhood. He addresses the attendees at an Alcoholics Anonymous meeting

ALEX: Hi, my name is Alex and I'm an A . . . (struggling to say it, hesitating) . . . Aardvark. My name is Alex and I'm an ... Agnostic . . . Sorry. Hi, I'm Alex and I'm an Alcoholic.

(He considers before speaking again. A small laugh. He's troubled) Why. Well, that's easy. I'm an alcoholic because I thought that drinking would help me forget that sometimes things don't float when they're supposed to. (beat) But, by the grace of my Higher Power, I didn't drink today.

ALEX: The whole thing just happened so fast. Like (snaps his fingers) that. (He speaks quickly here, moving through the sequence) First, Jade, she's coming out of the bathroom at her parent's house and she's holding this little stick and she's saying "we're gonna have a kid" and I'm thinking, no, we're still kids. This is like a TV show or something, and you go to sleep and wake up to realize that nine months have gone by, and you're at the hospital and you're holding . . . (There's a pause. He's holding his son) this itty-bitty little person. Jesus. You're holding your son. (He snaps out of it) He was a handsome kid. Looked just like his dad, right from day one.

So, thing is, everybody else was going to Prom and applying for school and I was . . . changing hundreds of diapers and sharing pureed chicken with Teddy. And working at Taco Bell and Target. Because nobody cares whether or not you're "ready," right? You're never ready, you just have this person who depends on you and then, nothing else matters. Nothing. But being a dad was the first thing I was ever really good at.

So, um, the Program teaches us a lot about "making amends" with people, but I ended up getting a lot of practice before I ever started drinking. I might've been waiting my whole life to be a dad, but Jade, she, uh, she didn't do too well with the whole being a mom thing. For me, it was all about Teddy, you know? I just looked at him and realized my life meant something now. I was somebody's father. So, I tried hard to . . . umm . . . (he falters a bit) to forgive her when I came home to the apartment one afternoon and she was drunk, and there's some guy there. (numb, detached) And I'm thinking, what kind of sick joke is this? I loved her. But people make mistakes. And we were just kids, and I loved her. I loved Teddy. He was ours. And, so, we talked through it.

And I just kept forgiving. For Teddy, I think. More than for myself. I mean, I thought I was protecting him, but (beat) not everything floats the way that it's meant to. You know what insanity really is? It's doing the same thing over and over again and knowing absolutely what the result is going to be. But you keep doing it anyway.

And so did she. It was like being on a raft that's coming undone, but the current' s just getting stronger. I was paddling as hard as I could - but she’d leave for three, four, five, days at a time, and I’d sit all night in our matchbox of a kitchen, afraid she was dead. I was more afraid that I might be relieved if she was. I kept paddling, hard.

[One night] she passed out at the foot of our bed, with the rubber tubing still tight around her arm. And Teddy's just standing in his crib, wailing at the top of lungs. She said it was me, you know? That all of this was my fault. And I thought, how did we get here? I just kept paddling.

And then the raft came apart altogether. And I couldn't forgive again. Because she got in a car, high out of her mind, and she took him, she took Teddy with her. She had promised. Sworn that she wouldn't. That she'd never hurt him. But somebody up there must've been looking out for him, because the car was twisted up bad, her ribs broken, her face all smashed up, and he's just perfect. Not a scratch. And you want to hear feelings? Truth? Oh my God, the guilt. Awful guilt. What kind of father was I? There was no more forgiving.

She called me from the hospital. (He speaks to Jade on the phone. At first, he's just listening, and then he speaks.) "No. I am done listening to you. Our son, Jade. No, stop. You don't. You don't love me, you don't love Teddy. No. NO! You only love yourself. (Very long beat) I don't love you anymore. Yeah, I care more about him, you are absolutely right. He's my son, Jade. I'd do anything for him. We're going away. You need to get help."

(He comes back to the present) When you're free, you can fly. And we did, we flew, Teddy and I. We came to live here on the coast, stayed in a room at my Aunt's place. And, Jade, she got help. That's what's unbelievable. Months of rehab, meetings, just like this one. And she'd send little drawings, funny pictures for him. Notes to me, saying she was getting better, and that she knew things were over for us, but that she wanted to see him. . . How do you do what's right when nothing is? How do you answer when your three-year-old boy asks, 'Why doesn't Mommy love me anymore?"

Um, so, we were going to meet for lunch, and, Teddy, he was so excited - I was afraid she wasn't going to show, but right on time, she gets to our place and he runs up to her screaming, "Mommy, mommy." And at first, we're talking like it's a bad first date, but then I think we both started breathing and she says she likes our place and how pretty the view is, high up like this. She asks me if I'd mind going down to put quarters in the meter, she'd parked her car on the street in front of the building. And, of course, I do, and I turned back and looked up at them . . . They're standing on the balcony, and they're both laughing and smiling, waving at me - and I smile and wave back. She looks good, standing there, holding Teddy, and I'm thinking, just in that moment, maybe there's hope. It feels like such a long time ago, but we were a family once.

And then, everything froze. It did. Like the air had been sucked out, and the sky was as white as bones. Her arms stretch out wide, and she's holding him over the railing, like she's offering him to me or something. (softly) "Mama 's gonna teach you how to fly."

NO! (Alex is very quiet for a moment, he's at his lowest point) In the early dreams, I would almost catch him. I ran like I was on fire, but it wasn't ever fast enough. I never caught him. I've dreamt that dream a thousand times over, and I've never caught him. (beat)

I don't think I know, really, how to live without him. So I drink instead. When I drink, sometimes I think I can float enough for the two of us and I tell him, "hold on to dad, buddy, hold on as tight as you can and we're going to float away from here."

But it turns to black, and the water turns to sky - he's suspended there in air, there, for just a moment, his eyes wide, and blue and open. How was I supposed to catch him? My Teddy fell. And they took him away.

(He's holding Teddy) You and me, little buddy. I'm here. I love you, Teddy Bear. (to audience) Why am I an alcoholic? Because I'm too crazy to be sober. Because when I drink I get to see him sometimes. For just a moment. A second. You'd drink too. Believe me. (He recomposes himself. Takes a long breath. End)
```

---

## IC-0457: Tied up in Chains

- Title: Tied up in Chains
- Author (byline): Laura Henry
- Work: Best Men’s Stage Monologues of 1998
- Publisher: Smith & Kraus
- Publication date as stated: January 2000
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SAUL MANTHONY DEGROUP
- Teaser before the introduction: Yes
- Spoken words (computed): 2050
- Already set (do not supply): none

### Source block (context only)

```text
Author: Laura Henry
Book: Best Men’s Stage Monologues of 1998
ISSN: 157525185X
Publisher: Smith & Kraus
Date (Month/Year): January 2000
```

### Introduction (context only: never use it for content warnings)

```text
Scripture tells us that “it is not for [us] to know the times or dates the Father has set by His own authority.” But, it’d be much more convenient if we could prepare ourselves for when he was coming to visit. Then we wouldn’t be preoccupied or at work or…in the shower… “Tied up in Chains” by Laura Henry.
```

### Performance text (classify this)

```text
SAUL MANTHONY DEGROUP: When God speaks to you, you don't tell him He'll have to wait. You sit back down and you listen.

SAUL MANTHONY DEGROUP: He spoke to me last night. I had my ears open wide for nine years and eleven months and I was plannin on closing them on the anniversary of the decade. But he must have been listening to my thoughts. 'Cause he got right up to the cutoff date and then it happened. He spoke. The first time it happened I was an ordinary guy. I was sitting on this big rock underneath this big blue sky. Feeling the warm air. Everything so lovely, thinking about Armageddon.

You know Armageddon don't you? The battle in the sky? It's that time when God comes down and fights the evil on our black planet. There's a big rain, drops of blood that feels like fire, but it ain't no pain compared to what we got down here, even on the good days. And there's a song in the air and a big white smoke and we all, the babies and the mothers and the folks who spend their days toilin' on the earth for a dime and no respect, all get wrapped up in the arms of God. And we fly through the air up to him in his heavens laughing and shouting and the Great Chant goes up Arma, Arma, Arma Geddon. Just like that. Arma, Arma, Arma Geddon. And all of us peoples are saved. The earthly peoples, swept up into the sky singing. And we are free at last, free and happy and there is no pain.

I was high up there, that first day, high on the beauty of the rapture of my thoughts when it happened. Oh, no. He didn't speak to me yet. Not yet. But I heard the break bell clanging, and it was time to go back to work again. And right there, coming through the noise of the break bell was when it started, a strange sound. A small sound at first, a little hum, so tiny at the start that I didn't even notice. I stood up, and it got a little louder, and as I walked back towards the shop, the noise shaped itself into sounds that began to shape themselves into words and then suddenly I could hear the words. A voice from nowhere talking to me loud and clearlike.

The voice said, "Saul Manthoney Degroup, I am talking to you." I knew the voice. It stopped me in my tracks, But I said, "Who are you?" just to check. And then He spoke. And he said, "It is me. The Great One. And Saul Manthoney, just like the Saul before you, I have come calling." I couldn't believe it. I said, "God?" And he said, "It is me" and I said, "I'm gonna be late to work. Do you realize that? I've been sittin here on a bench thinking about you through my whole lunch hour and now it's over and now you want to talk." And he said, "Yes, Saul Manthoney. I don't always call at the most convenient time."

When God speaks to you, you don't tell him He'll have to wait. You sit back down and you listen. And that's exactly what I did. I put my butt back down and got ready to receive His word. And He said to me, "Saul, you've got things to do. You go to work now that is what you should do but keep your ears open to me. Keep those ears in your heart open. Because I'm coming back. You are my blessed child. I am choosing you to spread my word in Venezuela." And then he left again just like that.

So I went to work, but I'm sayin' right now, I couldn't keep a clear head. I just kept thinking, "Jesus is coming. Jesus is coming to me, Saul Manthoney, just like he came to the other Saul. He's calling to me." I felt more special inside then than I ever felt in my entire life.

When I got home I cleaned the place. I put on a nice shirt and my good shoes. I combed my hair neat and settled down, ready to receive God's word. He was late. I couldn't help but watch the clock. Eight thirty, nine, nine forty-five...1 read my Bible, clock hands still moving. I took a walk. I sang. It got later. No voice. I stayed up through the night, listening and praying. Two-thirty, two forty-five, three and work in the morning still to come. But He didn't come back. Maybe He just got too busy, I thought. Maybe he was too busy for a man like me. And then I remembered, he didn't say when he was coming back, he just said to keep my ears open. Maybe he wasn't coming back for a while. Maybe there was something I had to learn first, a test, to prove myself. And I thought of the other part of what he said. I was sent to spread his word in Venezuela. Venezuela? I knew I had to follow Him, so I left all my earthly possessions, cashed in all the money I had in the world and picked up and went to Venezuela on a plane through the night.

How I got to Venezuela is another story. We don't have time for that one. You're here to receive God's new letter for the Next Millennium. I'm holding it right here in my hands. God gave it to me and now I am here to give it to you. It is my greatest mission in life.

I've been here ten years, to the day. It wasn't easy at first. I didn't have any money, no place to go. I didn't even know how to speak right. Ohee, I was scared when I came here. Boy, was I scared. But God always has us in his hands and he took care of me and slowly, I learnt to say what I needed to say and I ended up in this place along the Rio Orinico and was taken in by some nice folks. I told them my story, that God had sent me, and they let me stay there so I could tell stories for God, just the way I'm telling you today. And soon I was going all over to tell my stories and people were coming from allover to hear them. They wanted to receive joy. And they seemed to get it. But I can tell you now that the whole time I was preaching like a called man, I felt like a fake. A crazy man singing about Armageddon and the word of God. 'Cause God never spoke to me again. These last ten years, I've been waiting with my ears open and my heart wide, singing the praises of God. And He never again let me receive His word. Not like the first time.

Was I a fake? I didn't know. I would plead with him and plead with him. God, I'd pray, give me a sign. Let me know you're here, that I'm not some crazy man in a new land with a grand delusion. Let me know you sent me here. Still, no word. And I kept preachin' and talkin', telling people about the word of God, but all the time, doubting bigger than Thomas. Am I a fake? If I'm not why won't you come back? Please, please come back. Still, no word.

Until last night. There I was, an ordinary man on an ordinary day. I'd finished my preaching for the night and had just stepped into the bathtub, ready to take myself a hot shower and the water was on, streaming down me, and I was singing songs as loud as I could when I heard this still small voice that I recalled from those other days. Soft at first, but this time I knew for sure what it was. I stopped. "God?" I said? "It is me, my son," he said back. "God," I said, "Can't you see I'm in the shower?" He laughed and said, "Saul, my child. I love you. I'll come back at a better time." "Oh, no you don't," I said. "You said that last time and I've been waitin' for ten whole years. I'll be danged if I'm gonna miss you cause I'm taking a bath. Talk to me. Talk to me now." And he said, "But Saul, you're all wet. I'm going to need you to be ready with a piece of paper. You're going to take dictation for me. You're going to write a letter that will beat the great letters of Paul." To miss this chance, what a fool I would have been.

I'm ready, God. I'm ready right now. And I stepped out of the shower, all soaped up and everything and I put a towel around my middle and I found some paper and I sat my butt down on the chair and I waited for him to speak again. And you know what? He waited for me too. For me. Saul Manthoney Degroup. He waited until I was situated and then he began to speak again. It came in spurts. I'd listen, he'd say a little. I'd write. He'd say a little more, I'd write. I didn't question a thing, just wrote it down, wrote down every word he said. It took all night. I'm a little tired now, if I must say so myself. It's a rough job, being secretary for the Lord. But now I got it-my letter-just as inspired as the letters from Paul, and I have come here to read it to you today.

At first I was a little nervous. I read it over just a few minutes ago, you see, and I know that some of what I have to say to you might seem a little crazy. I can't help it. I didn't come up with the idea. It's all God's thoughts. I just held the pen. So don't judge, if you start to feel like the words come out a little bit strange. Hold on till the end of the message. It is God's great message to me and to you, my friends. The answer to all our prayers, everything we've been waiting for since the last letters from Him. It's the New Letter for the Next Millennium. Hold on to your seats. Close your eyes. Open your hearts. Get ready to receive his word. (Saul takes hold of his letter and begins to speak.) Dear friends: Kiss someone you love when you receive this letter. With love all things are possible. (He stops suddenly)

Wait a second. (He listens.) I hear His voice again. (Saul listens intently Then he begins to have a conversation with God.) What? Are you sure? But we worked on it all night... But Lord, it is so beautiful and these people have come today to hear your word...I understand, but...But...Wait...Don't leave me like this...Goodbye. Goodbye. (He folds the paper up and looks sadly at the audience.) I'm very sorry. I thought he wanted me to share his words with you today. That's why I rang the bell and asked you all to come. But it was my mistake. A misunderstanding, really. I just didn't...This letter that we worked so hard on last night, this perfect specimen of God's word... He says it is not time yet. It's a letter for the new millennium, He says and the new millennium just hasn't come yet. (Saul looks out at the people.) I guess you can all go home. I'm very sorry.

Don't despair. Keep your hearts and your ears open, God said to tell you that. His word will be known. Be ready when the time comes. But first there is much work for me to do.

He says I have to translate it into English immediately and send it to the people back home. He says the folks there need his message more than anything. But we in Venezuela will receive it too. Be ready for the day it comes. Be open to it.

You must leave now. I wish I could have read you the letter but I must obey God. I have to. You do understand, don't you? I have work to do. So much translation...and I have to finish my bath. The soap is beginning to itch.
```

---

## IC-0458: Touch

- Title: Touch
- Author (byline): Toni Press-Coffman
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Jan 2005
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: KYLE
- Teaser before the introduction: No
- Spoken words (computed): 1383
- Already set (do not supply): none

### Source block (context only)

```text
Author: Toni Press-Coffman
ISBN: 978-0822220558
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Jan 2005
```

### Introduction (context only: never use it for content warnings)

```text
Kyle Kalke, an astronomer since childhood, a high school “science nerd,” falls in love with flamboyant, outspoken, openhearted Zoe, who—astonishingly—loves him back. But when she is kidnapped and murdered, Kyle searches for answers in an attempt to understand the meaning of Zoe’s life and ultimately the meaning of her death. Touch by Toni Press-Coffman
```

### Performance text (classify this)

```text
KYLE: I was taking physics, and that’s where I saw her for the first time. She looked into the room. Peeked in. The teacher asked her whether he could help her, and then she stepped in, looking all around the room. Zoe had huge eyes. Gigantic. As she looked around the room, her eyes reminded me of the heavens.

She fixed her glance on me for a second or maybe two seconds, only it felt like much longer. Then she said, “I am so in the wrong room,” and turned around and walked out the door. I didn’t think. Which had rarely - maybe never - happened before. I literally jumped to my feet and went after her. Zoe caused me to be late to class for the first time in my life. Then it was every day. It was impossible to stop looking at her once I started. I would come to school early, I would find her, and I would look at her until the bell. I dreamed of her at night and did nothing but look at her at school.

We got married the Christmas after high school graduation. December 22. Winter solstice. Our decision to marry made our parents insane. Mine told me I didn’t have to marry the first young woman I dated and her folks just thought I was - odd. We had our honeymoon in New York City. The honeymoon was beautiful beyond imagining.

We both went to college. Zoe majored in - umm.. She kept changing her mind. (He thinks) I can’t - I can’t remember what she settled on. (Upset) Why can’t I remember that? (Composes himself.) I majored in astronomy.

A month before our sixth anniversary, she and I gave Thanksgiving. [Zoe] was sitting on a big red pillow in our living room, her cheeks were red too because she’d drunk quite a bit of wine. People kissed us as they left. Her mom kissed each of her cheeks and Zoe threw back her head and through this completely radiant smile told her mother, “You make a great me.” Then she said “I’m so happy you realize how I feel about Kyle now.” (Beat; it’s starting to get him, but he wards it off.) By ten or so, it was just us and Bennie and Serena. Zoe decided had to have this coffee drink she liked to make, with Triple Sec and whipping cream, only we had no whipping cream, and Zoe said she’d run down to twenty-four hour market to get some. Serena told Zoe to wait, she’d go with her, but Zoe said no, Serena should stay, she’d be right back. (Beat) She grabbed her purse. (Beat) She put on her black leather hat. (Beat) She kissed me. (Beat; tears come up) Thank God. (He composes himself) She left. (Kyle pauses for a long time)

Forty-five minutes after she left, her sister asked - umm - how far away the market was anyway. Forty-five minutes. Which is impossible. My wife went to the grocery store to buy one item, I let her go, late at night, by herself – and she’s gone forty-five minutes and even then I don’t notice. Her sister notices. Which is unforgivable. Because that is a long goddamn time, and in that time - I could have - [done something to help her]. I should have – [gone to the grocery store myself.]

After that -- after Serena noticed Zoe wasn’t coming home - I was delirious with worry. I already knew. Maybe not that she was dead – but I knew that she was at least badly hurt because I knew Zoe. (Beat) I knew she would not stay away and not call. I knew she was hurt and I knew I could have gone to the grocery store.

The police wouldn’t look for her until she was missing for twenty-four hours. A detective asked me who she might have – he said “split with.” (Registers this, tries to calm down) Who might your wife, the person you care about most in the world, the only woman you’ve EVER loved, have “split with”? (Beat) I tried to explain that Zoe did not mince words, Zoe always said exactly what was on her mind, no exceptions whatsoever, including, “Sorry, Kyle, I love somebody else, I’m leaving.” That’s what she would have done, she would not have just -- “split.” My wife would not have done that.”

I told the detective about Zoe. I talked and talked and talked and talked. (pleading with the cop) Our car is still in the parking lot, doesn’t that tell you something? It told him that whoever she left me for picked her up in the supermarket parking lot. Nothing registered. He was going to wait twenty-four hours.

(After a pause) I didn’t sleep until much later. When she died. Which I didn’t know at the time, but my body would not shut down until hers did. Then I slept.

(the phone rings. Twice. Three times). (On the phone) Yes? (Beat) Yes, this is Zoe Kalke’s home. I’m her husband. (Quickly) Did you find my wife? (Kyle listens for a beat. Then . . . ) Sixteen days after Thanksgiving . . . . a man’s dog found Zoe’s bag buried in his yard. Up at the southeast corner of the Navajo reservation. Um. . .

He searched and found -- just beyond his property -- a pile a rocks. (Beat) The Navajo believe it will harm them to come in contact with a dead body, and – and he sensed she was there but he didn’t want to uncover her for – uh – spiritual reasons. (Beat) He thought of involving the police but – well, the tribal police are Navajo and he didn’t want them to have to - touch her. (Beat) So he thought if he called her number, that might help him decide what was best. I told him I’d be there immediately.

She has no clothes on. Is she smiling? Could it be just – a – an – anomaly? Could it have happened after she died? Zoe, are you smiling? . . . . . Who killed her? Random chaos – entropy – like a black hole – always increases. The supermarket swallowed Zoe. Or maybe her car swallowed her. Maybe her heart. Maybe Zoe got swallowed by her great big, ever-expanding, loaded-with-the-spirit heart. I prefer not to think about the police and their investigation. I prefer to think about black holes. I’m not confident they will find the men who hurt Zoe.

[But] Then, in the summer, early in July, the police arrested two men for rape, and when the police searched their van, they found pictures. (Beat) Of Zoe. (Beat) I suppose I should be grateful that these criminals were so stupid. The police called me at work, and I went down there. (Beat) She was alive in the pictures. (Beat) She didn’t look hurt, but she wasn’t smiling. My wife was raped and murdered. The police caught them. The men who killed Zoe. They confessed.

I talked to each of them separately. Each one could have said no, but each agreed to speak to me. Which I didn’t understand at first, but now I think it was Zoe. Zoe was smiling. Zoe was telling me, I am dying. I’m dying, Kyle. That’s what my life is now. I’m dying. (Kyle stops, and closes his eyes and breathes. He opens his eyes) The first one said no, he didn’t notice she was smiling. (Beat) She said if one of them would stay there with her until she died, she would like that. (Beat, he can hardly say this). She would be grateful. (Beat) Zoe hated to be alone. This kid was spooked by that. He told me he didn’t know why, but he grabbed her purse and ran with it. He had killed before, but he didn’t want to be there when Zoe died. So the other one stayed with her. (Kyle closes his eyes and breathes. His measured breath becomes more shallow, becomes panting. He opens his eyes).

When he came into the visiting room, he sat down, rigid, and fixed his gaze on me. He didn’t speak. (He takes a deep breath, like he did then). I asked him if he noticed she was smiling, and he said yes. (Pause, like he’s waiting for more, like he did then) I asked him was she scared, and he said yes. (Beat) But as she faded, she seemed less and less so. I asked if she spoke my name. He said no. He said he didn’t want to piss me off, but she was “one weird chick.” Because, as she lay dying, she mumbled something about the stars. (Kyle closes his eyes and breathes. He opens his eyes abruptly). She died . . . She died. He said you’re crazy too, buddy. I banged the telephone on the Plexiglas separating me from him. I said did you touch her? Did you touch her while she was dying? DID YOU TOUCH HER? And there it was. He flinched. He looked at me. (Beat) She – uh -- she reached her hand out to me, he said. She reached for me. (Beat) Yeah. I let her touch me.

(Kyle stops, cries, breathes, waits).

I said – I said – we met in my physics class.
```

---

## IC-0459: A Trace of Panic

- Title: A Trace of Panic
- Author (byline): David Cale
- Work: Out of Character
- Publisher: Bantam Books
- Publication date as stated: Dec 1996
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1516
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Cale
Book: Out of Character
ISBN: 978-0553374858
Publisher: Bantam Books
Date (Month/Year): Dec 1996
```

### Introduction (context only: never use it for content warnings)

```text
Every person is special in some way and different from every other person on earth. Even the personalities of identical twins are different because they are affected by influences that impact on their lives in different ways. Personality development has been a major topic of interest for some of the most prominent thinkers in psychology. Our personalities make us unique, but how does personality develop? How exactly do we become who we are today? A Trace of Panic by David Cale is an absurdist piece about a man who co-ops bits and pieces of other people’s personalities in an attempt to develop one of his own. A Trace of Panic by David Cale.
```

### Performance text (classify this)

```text
A MAN WITHOUT A NAME, he speaks in a voice that is a cross between William Burroughs and the narration to a forties film noir. Nothing is his own.

My mother's name was Paranoia. My father's name was Panic. They lived in a place where gray was the color of choice. On a windy day the preacher of the town decreed,

"I name these neuroses man and wife."

When I was born my mother's best friend, Chemical Dependency, looked at me and cried, "Oh, Paranoia, you must be so happy, he looks just like you, but there's definitely a trace of Panic in his eyes. And he's already wailing about something, and I bet he doesn't know what it is he's wailing about. That's a good sign. He'll fit right in 'round here."

My parents forgot to give me a name, so I was always referred to as Paranoia's son, or the child of Panic.

And childhood for me was one long walk down a lonely lane.

As Paranoia got older she grew clouds around her head. Till eventually all she could see were the clouds. So she started growing eyes all over her body. At a certain point the eyes started looking inward. Paranoia watched her every move all the time, and she became like a truck whose alarms would go off every time she got into her own driving seat. As she got older she stopped moving at all, she just stood in one place with all her eyes blinking, her alarms ready to go off, and the clouds drifting slowly around the features on her face. Nothing got better for Paranoia. From the day she was born it was all downhill.

Which was just the way she thought it would be. Panic spent most of his time standing on the fence smoking cigarettes, running away from views and muttering, "I can't deal with this. I don't want to know."

One day they both just disappeared. The theory was, they'd canceled each other out. All I inherited was the prison they lived in.

Well, one day I slipped through my own bars and made my getaway.

I was always drawn to the sky, so I spent most of my youth gazing out of windows.

"You were a bird in a former life," a fortuneteller told me.

"What about this time around?" I cried.

"I don't see anything for you but your past. Your past stretches all the way into where the future should be." ("Some accent, Madame Fong!")

"There must be some mistake," I cried.

"The cards don't lie," she said.

"Can we play another round?" I inquired. "Give me a chance to win back what I lost."

I started drifting. Anyplace I'd hang my hat was home. I moved in with a little woman called Safety Net. Safety was drawn to blank sheets like me. She got pleasure from coloring people in.

Safety had photographs of her parents all over her house. On one alarming day I noticed she had cut up and glued a photo of her face over the top of her mother's face, and a photo of my face was stuck on top of her father's. Instinct told me it was time to be moving along.

But Safety's photo collage had planted an idea in me. You see, Panic and Paranoia had neglected to give me any kind of character, so I decided to use myself as a canvas and snip away the pieces of other people's personalities that I was drawn to and stick them to me.

I soon became a well-balanced mixed platter, suitable for parties or office functions, or just something to nibble on. I wasn't a real meal, but I was happy. And Panic and Paranoia seemed like something I'd made up. Something that had never happened to me.

Though occasionally I'd look up at the sky and wonder if they were my mother's clouds.

Then I made a big mistake. The relationship with Safety was strictly platonic. You see at this point I had no sexuality. Everyone said that I should adopt one from the pound. There were all these unwanted sexualities desperately looking for a home. So that's where I went.

Dima Dozen ran the pound. A recovering dominatrix, Dima was an expert in drawing the line. She gave me the tour.

"If the sexualities are here for more than forty-eight hours, they're put to sleep. All our sexualities are de-flead. They've all had their shots. Oh, and choose carefully, all sexualities are nonreturnable."

Initially I couldn't see anything I was drawn to. Then I noticed a big, dark thing with needy eyes, separated from the rest.

"What's this one, Dima?" I inquired.

"Oh, that sexuality has no name."

I thought of myself, also drifting without a name, and a strange kind of bonding took place. At which point the sexuality jumped up and licked me on the face, and the look in its eyes told me the poor thing had been alone as long as I had.

"This is the one for me, Dima."

"Are you sure you can manage?" she asked. "This sexuality is very strong. Untrained. It'll need a substantial leash. And remember, it has to go everywhere with you."

"Dima, I'm alone in life. I've got nothing better to do than look after a big, uncontrollable sexuality," I naively replied.

I called my sexuality Scruffy. Scruffy and I left the pound with a sense of optimism. At last we'd both found constant companions. But reality was 'round the corner waiting to pounce on me and change all that.

I'd wake up every morning and Scruffy would be in my face. It would get hyper. Walking the streets it wanted to jump up on everyone. People backed away from me 'cause it was clear I wasn't walking the sexuality, but the sexuality was walking me. Dima's words echoed in my ears:

"All sexualities are nonreturnable, returnable, returnable .... "

Then I woke up one morning and looked down and there were little eyes growing all over me, and a subtle-looking cloud was passing my left eye. Mother! I had wondered where Paranoia had gone all those years, she was hiding out inside me. And I knew deep down, something was aggravating Scruffy. It was Panic. There was no choice but to visit Init Forthemoney. Dr. Forthemoney was an ex-mercenary and onetime bounty hunter who now had a thriving Freudian practice. She had the word "Passive" tattooed on one knuckle and the word "Aggressive" tattooed on the other. She'd clench the two and make a strange growling noise. Grrrr!

"What does your mother look like, so I know what to look for?" she inquired. "Grrr!"

"Picture a cumulus cloud with bad shoes, Doc."

"And your father?"

"The Santa Ana winds with a cigarette."

A couple of days later she gave me her initial report.

"Inside you looks like bad weather. Take off your clothes, I need to look at your mother's eyes."

I obliged. There was something strangely calming about standing naked in front of such a total professional.

Scruffy, don't even consider it!

"What's all this?" the Doc asked. "You have all these bits of personality attached to you. This isn't your sense of humor. These aren't your opinions. That laugh isn't you. And they have little labels with dates on them."

"That's when I got them, Doc."

"They're coming off!"

"Ow!"

She yanked at the pieces of personality. "Ow, but I'm used to them now."

"This isn't you!"

"Ow!"

"And this here, is this you?"

"No, Doc. Ow!"

"I can't get to your mother and father without my assistant Seda Tive." Suddenly the door flung open. [Wolf whistle]

"Shut up, Scruffy!"

Seda Tive was a slinky little tablet with the vocal cords of a dove. She was wearing a dress made out of clear water. It was love at first sight. Seda threw her arms around me.

"Take me," she cooed. "I'll get rid of Paranoia. I'll get rid of Panic. Take me."

How could I say no.

"Oh, Seda," I uttered, "I'm feeling better already. What did you do with mother and father?"

"I'm not telling," she cooed, "take me again."

"Oh, you beautiful relaxant, you, I'm starting to find you irresistible" were the last words I remember uttering.

When I came to I was wrapped in bandages, lying in the hospital. Dr. Forthemoney had removed Mother's eyes. They were glaring at me from the inside of a jar. I looked out the window and I noticed the sky had a few extra clouds. And Father was blowing around outside. The operation had been a success. I looked to my left and Seda Tive had gone, and she'd taken Scruffy with her. Such is life, I thought to myself, wiser but no more bitter.

Leaving the sanitarium, as we all must do, eventually, I waved at the elements that once were my parents. The sky that day seemed particularly blue.

Naw I'm a clean slate, I thought to myself, a blank page. A new chapter. Just waiting to be written.
```

---

## IC-0460: Tradition 1A

- Title: Tradition 1A
- Author (byline): Howard M. Rice
- Work: Off Off Broadway Festival Plays, 14th Series
- Publisher: Samuel French, Inc.
- Publication date as stated: 1989
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MICHAEL
- Teaser before the introduction: Yes
- Spoken words (computed): 1255
- Already set (do not supply): none

### Source block (context only)

```text
Author: Howard M. Rice
Book: Off Off Broadway Festival Plays, 14th Series
ISBN: 978-0573623639
Publisher: Samuel French, Inc.
Date (Month/Year): 1989
```

### Introduction (context only: never use it for content warnings)

```text
Melanoma is a potentially aggressive, life-threatening cancer. It is readily detectable and usually curable if treated early, but it progresses faster than other types of skin cancer and can spread beyond the skin to affect numerous parts of the body, including the bones or brain. Once this occurs, melanoma becomes very difficult to treat and is incurable.

Matthew Banner has aggressive melanoma. It has spread and it is incurable. But he has a few things to hold onto . . . his family, his treasure box and Tradition – 1A by Howard M. Rice.
```

### Performance text (classify this)

```text
(TIME: 2 AM. Michael is sitting at his desk, drinking a cup of coffee, nibbling on a cookie and flipping through some papers. He is not reading the papers; he is just touching them gently When he recognizes the audiences, he takes a bit of the cookie; considers it, and begins talking – softly, evenly)

MICHAEL: Chocolate chip coconut peanut butter marshmallow molasses . . . my daughter’s favorite. (He takes another bite, a sip of coffee) She baked a batch before she went back to college. Her favorite used to be macaroon macadamia nut cinnamon banana blueberry, but two years ago chocolate chip coconut peanut butter marshmallow molasses became number one on the cookie hit parade. (Takes another bite) She calls them her “Everything but the sink” cookies. Appropriate name. The backer of the cookies in my daughter, Cindy. Senior in college, majoring in psychology. I know parents can be biased – but I truly think she is one of the most special people God ever created. I feel blessed having her for a daughter.

(Picks up a picture from the box) My son Richard. I can sum up my relationship with Richard this way: for years I believed I was Job and Richard was my toughest test . . . somewhere between locusts and boils there was Richard. We struggled through some rough times, we did . . . and for a while I was convinced that either he wouldn’t make it to be eleven or I wouldn’t make it to be thirty-six. (Beat) But he grew up and I guess I grew up too. (Beat, picks up another picture)

My wife, Ruth . . . the center of it all . . . the holder together of pieces. I love her very much. I tell her as often as I can, which is still probably not often enough. That is my family. (Beat) That is my life. (He puts the picture down, flips through papers in the box again)

And this is my treasure box -- filled with things I treasure greatly, feelings expressed over 22 years. (Beat) A map of our lives in this box. The notes [my family] sent met went into the treasure box in no particular order. (He gets up, starts to pace.)

MICHAEL: I had been putting the cards in the box for a few years when I realized I had sort of started a tradition. (Beat) I never had any traditions growing up . . . unless you call breaking up fights between my mother and father a tradition. My home was like a war zone, and I was always either running away or ducking for cover when my parents fought with each other, sometimes with fists, sometimes with worse. (Beat) So I felt good when I sensed that we were creating a tradition. In our own small way, we were building something that bonded us and made us more and made us special.

(Beat. He looks satisfied, smiles, sits down again) For years that was my only tradition (Beat) Then something happened to make me start another one . . .

building off this one. Tradition 1A I guess you could call it. (Beat – takes a final sip of coffee)

I was taking one of my annual physicals with Dr. Jenner. He was listening to my heart through his stethoscope when he spotted a red mark near my collarbone. He sort of poked at it a little and asked me how long it had been there, and I said “how long has what been where?” - I have a lot of freckles so I don’t normally notice any little red marks. (Beat) He said it looked like a basal cell . . . a form of skin cancer . . . Then he added, “If you’ve got to get cancer, this is the best kind to get.” I thought that was a little like saying, “If you’re gonna get hit by a car, a Volkswagen is the best kind of car to get hit by.” (Beat) He laughed. I didn’t (Beat) Since then I’ve had about 25 sores taken off in all – from all over; legs, arms, chest face . . . (Beat) After each operation, I felt that something more than a few millimeters of skin had been taken away from me . . . I felt that a piece of whoever and whatever I was had been cut out . . . some of the me in me was gone. (Beat) I wanted to replace the part that [had been] subtracted from the outside by adding something to the inside. And so began Tradition 1A (Beat) A short time after every operation, late at night when everyone else was asleep, I’d come down to this room, reach into the Treasure Box and take out one of the notes . . . and then I’d read it. (He reaches into the box, takes out a note)

My daughter wrote this on Father’s Day five years ago. “Dear Dad. What I want to say most to you today is that you are more than a father to me . . . you are my best friend in the whole world. Your loving daughter, Cindy>”

(He looks at the note for a minute, wipes his eyes) That not put a lot back in me . . . . yeah. (He puts the note back in the box)

Over the years . . . as the operations became almost routine . . . I got the feeling that the cancers were part of my signature, as if I was somehow identified by them. (Takes a deep breath)

And I felt as if I was in a war . . . a war I had the chance to endure . . . to fight and win on my own terms . . . no matter how small the victory. Shoulders back, jaw firm – do not flinch from the needle or knife – ear each scab and scar like a badge. “Where’d you see action, mister? “Valley Forge Medical Building, Suite 202.” “Was it bad?” “Yeah, war is hell.” (He stops, looks around. He’s embarrassed.)

The cancer became part of my manhood . . . a part that I hadn’t, until then, discovered. The cancer made me more, as it made me less. (He looks at the picture of his wife)

Ruth never made me feel less. There were the times we’d be lying in bed and she would gently run her fingers over my body, tracing a path from small scar to small scar . . . certainly an act of loving. (He takes another note out of the box, chuckles)

This is one of my all time favorites. My son wrote it to me when he was eleven. He and I had gotten into this thing where we were calling each other Moose. He was Little Moose and I was Big Moose. I think it started when he saw me lifting weights down in the basement. So a week later, I got this note: "Dear Big Moose. I am very impressed with your upper body strength. I think you can kick King Kong's ass. Signed, Little Moose." (laughs) Pretty big deal when your son tells you you could kick King Kong's ass. (Beat – almost to himself) He had a sense of humor. I wished I had sensed that sooner. (He takes a deep breath) Anyway . . . (Gets us, starts pacing) . . . it went on like that for years. Dr. Jenner would take something off . . . I’d come down here and put something back in . . . replenish myself.

It was a Wednesday night and I was Dr. Jenner’s last patient. As I was getting up from the table after he’d taken something off my shoulder. I felt him touch the back of my neck. “How long’s tat been there?” he said in a voice I had never heard before. He looked longer and harder at whatever was on my neck than he had ever looked before. (Beat) Then I learned that I had more than the VW of all cancers . . . this time it was more like a Mack truck . . . melanoma . . . I’d have six months. (Beat)

When I got home, I went right to the Treasure Box. I remember the first note I picked out was the one from Richard about kicking King Kong’s ass. (Beat) Forty-eight-year-old men with melanomas are in no condition to kick anybody’s ass, let along King Kong;s. (Beat)

I never thought about dying much. Just a little maybe, like I guess everyone does. But I never feared death. (Beat) I have asked to be buried in a cemetery near this house . . . it has lots of trees. I love trees. I have willed that they should take from my body whatever parts might help somebody else. (Beat) Cremate the rest. (Beat) Then buy the box under a white birch tree. There will be a place for Ruth next to me.

And I have put in writing that I want my Treasure Box to be buried with me. I want its ashes to be mixed with mine.
```

---

## IC-0461: Truth in Dreams

- Title: Truth in Dreams
- Author (byline): Joshua Sands
- Work: Turning Points
- Publisher: Tichenor Publishing
- Publication date as stated: 2001
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1016
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joshua Sands
Book: Turning Points
Publisher: Tichenor Publishing
ISBN: 978-0742117013
Date: 2001
```

### Introduction (context only: never use it for content warnings)

```text
I look in the mirror and say to myself:

"I look like me but I don't feel like me. Everything in my life seems to be changing. I'm not reacting the way I usually do. What's happening? Am I going crazy?"

No, I’m not. I’m going through one of the most intense, frightening and difficult emotional experiences of life and sometimes I believe that I’ve only just begun to find the Truth in Dreams by Joshua Sands.
```

### Performance text (classify this)

```text
The dream always begins the same way. Darkness becomes light and I'm marching to the cadence of a drum commander: Left, left, left, right, left. Only I can never stay in step, always skipping a beat to get back with the cadence. The cadence gets faster. And faster. And faster. Suddenly, I'm out of control. I'm marching straight into a tree, only the tree doesn't stop me. It shatters like glass and I continue on. Light becomes darkness. The cadence slowly fades away: Left, left, left, right, left.

My wife, Karen, and I are deeply in love. We only fight approximately three times per year. Sort of a tri-annual ritual, you might say. These fights usually involve money, taxes, or in-laws. Of course the third tight of this year falls into the" miscellaneous" category: we're fighting over my potency. See, we want to have a child but can't seem to make it happen. She says I'm not potent enough; I say let's try harder. She may be right, but I can't admit that. I mean, you're told that one of the reasons you enter this world is to reproduce. Pass something on. Leave it behind. Can't imagine not being able to do that. So we fight; I defend myself out of sheer masculinity. And we try again. You can have anything if you try hard enough, my dad always said.

Our lives have begun to resemble a First Response commercial. It's as if our life evolves around the stick. The plus or minus that determines our future. A plus represents the future. A family. A minus means something is subtracted. With each minus, we lose something: control, hope, dreams.

The dream begins to come into focus. Left, right, left. I'm no longer marching but the cadence is clear. I'm riding a bus. Karen is next to me. She wants to get off the bus but I won't let her so I hold her in her seat. The bus accelerates with the beat. Left, right, left. It hits the tree and the wood shatters like glass. Light becomes darkness.

When she exits the bathroom: Honey, you won't believe this but... What - we got a double minus this time? No honey, we've done it.' See for yourself! My life has evolved around the stick and the stick reads: plus. Positive. As if God were reaching down and saying, "OK, you can start your life now." Positive. Addition. A new addition. What are we gonna do first?

First, the mall. Second, Toys R' Us. They've got some really fine products! Nothing is too much for my kid. I got him a plastic ball and bat. What if it's a girl? Then we'll play softball! You know the baby won't be born ready to throw a curveball. I know. I buy everything I can think of. Things for the future. Additions. I always envisioned buying this deluxe swing set so we got one! Four swings, three slides - a teeter-totter. You know, we're only having one child! Yeah, but we're making this one count! Think we have an overzealous father on our hands! Well, maybe.

It was if time stood still and flew by simultaneously. Karen and I were planners -like we were coordinating a big convention when tons of people would soon arrive. There was only one arrival on the way, but we were planning for more. We were moving from couple to family. Philosophers argue that if you can find just a few days of absolute happiness, then you're fortunate. Karen and I found months of absolute happiness. In the midst of going to work, paying bills, and all the other mundane tasks, we had found joy. And the true joy was still on the way...

Then one October night, Karen's putting away the dinner dishes when she says: Honey, Oh my God! He's coming! Oh my God, he's coming! OK, I've prepared for this for months. I can do this. One: Get her bag with her things. Got it. Two: Call the hospital. Check. Three: Help Karen to the car. Check. The contractions are getting closer. It's almost time! I have to get her there! The way I normally would go to the hospital has a train blocking the road. U-turn. Oh my God! My water broke! Are things supposed to happen that quickly? Don't worry, dear, I'll get you there! I'm taking side roads - swerving back and forth passing the other cars quickly and accurately. Wait - shortcut! I turn left, and I see a car coming straight at me. I turn back. A car is bearing down from the other side. Left. No wait, right. No - left. Suddenly, I'm spinning around. Spinning. Spinning. Karen!

Karen? Karen? I'm not actually speaking, but screaming in my head. My brother is there.

Where am I?

Ryan, you're in the hospital. Save your breath.

The hospital? Did I get Karen here on time? Why don't I remember?

Ryan, you were in an accident. Ryan, it was bad. I don't know how to say this.

Ryan, Karen didn't make it. I'm sorry Ryan.

What? My God - what have I done? I bring myself to say “Baby?”

Ryan, I'm really sorry. There was nothing anyone could do, Nothing? You mean it's over? Over? Don't tell me that. Don't tell me they're gone. I thought, you know, maybe I'm hallucinating. Maybe I'm in a coma. Maybe. Bur I knew. I was in the hospital, the sole survivor of a bad accident. The result of a wrong turn - made by me: an overzealous father.

The dream crystallizes. The bus is a car. I'm driving the car. I swerve left. Then right. Then left again. No matter which way I turn, I am swerving the wrong way. Off beat. The tree has become a telephone pole. I reach over to hold Karen, trying to brace her from the crash. Light turns to darkness as the rescue unit breaks the car windows to save us. They say, “We can still save him but she's already gone.” Gone. Addition becomes subtraction. Dream becomes nightmare.
```

---

## IC-0462: Tuesdays with Morrie

- Title: Tuesdays with Morrie
- Author (byline): Mitch Albom
- Work: Not specified
- Publisher: Broadway Books
- Publication date as stated: Oct 1992
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MITCH, MORRIE, DOCTOR
- Teaser before the introduction: Yes
- Spoken words (computed): 2131
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mitch Albom
ISBN: 978-0767905923
Publisher: Broadway Books
Date (Month/Year): Oct 1992
```

### Introduction (context only: never use it for content warnings)

```text
Tuesdays with Morrie by Mitch Albom
```

### Performance text (classify this)

```text
MITCH: The last class of my old professor’s life took place once a week in his house, by a window in the study where he could watch a small hibiscus plant shed its pink leaves. The class met on Tuesdays. The subject was The Meaning of Life. No books were required, yet many topics were covered, including love, work, community, family, aging, forgiveness, and, finally, death. It was taught from experience. The last class of my old professor’s life had only one student. I was the student.

MITCH: His death sentence came in the summer of 1994. Morrie had amyotrophic lateral sclerosis (ALS), Lou Gehrig’s disease - There was no known cure.

MORRIE: How did I get it?

MITCH: Nobody knew.

MORRIE: “Is it terminal?

DOCTOR: Yes.

MORRIE: So I’m going to die?

DOCTOR: Yes, you are. I’m very sorry.

MITCH: ALS is like a lit candle: it melts your nerves and leaves your body a pile of wax. Often, it begins with the legs and works its way up. You lose control of your thigh muscles, so that you cannot support yourself standing. You lose control of your trunk muscles, so that you cannot sit up straight. By the end, you are breathing through a tube in a hole in your throat, while your soul, perfectly awake, is imprisoned inside a limp husk, perhaps able to blink, or cluck a tongue, a man frozen inside his own flesh. This takes no more than five years from the day you contract the disease. Morrie’s doctors guessed he had two years left. Morrie knew it was less.

But my old professor had made a profound decision: He would not wither. He would not be ashamed of dying. Instead, he would make death his final project, the center point of his days. Since everyone was going to die, he could be of great value, right? He could be research. A human textbook.

MORRIE: “Study me in my slow and patient demise. Watch what happens to me. Learn with me.”

MITCH: Morrie would walk that final bridge between life and death, and narrate the trip.

We Talk about Death

MORRIE: “Mitch, you know that I’m dying.”

MITCH: I knew.

MORRIE: All right, then. [Morrie swallowed the pills, put down the paper cup, inhaled deeply, then let it out.] “Shall I tell you what it’s like?”

MITCH: What it’s like? To die?

MORRIE: Yes.

MITCH: Although I was unaware of it, our last class had just begun.

MORRIE: Dying is only one thing to be sad over, Mitch. Living unhappily is something else. So many of the people who come to visit me are unhappy.”

MITCH: Why?

MORRIE: Well, for one thing, the culture we have does not make people feel good about themselves. We’re teaching the wrong things. And you have to be strong enough to say if the culture doesn’t work, don’t buy it. Create your own. Most people can’t do it. They’re more unhappy than me—even in my current condition.

I may be dying, but I am surrounded by loving, caring souls. How many people can say that?”

MITCH: I was astonished by his complete lack of self-pity. Morrie, who could no longer dance, swim, bathe, or walk; Morrie, who could no longer answer his own door, dry himself after a shower, or even roll over in bed. How could he be so accepting?

We Talk About the World

MORRIE: It’s hard to explain, Mitch. Now that I’m suffering, I feel closer to people who suffer than I ever did before. The other night, on TV, I saw people in Bosnia running across the street, getting fired upon, killed, innocent victims . . . and I just started to cry. I feel their anguish as if it were my own. I don’t know any of these people. But—how can I put this?—I’m almost . . . drawn to them.”

MITCH: His eyes got moist, and I tried to change the subject, but he dabbed his face and waved me off.

Amazing , I thought. I worked in the news business. I covered stories where people died. I interviewed grieving family members. I even attended the funerals. I never cried. Morrie, for the suffering of people half a world away, was weeping. Is this what comes at the end, I wondered? Maybe death is the great equalizer, the one big thing that can finally make strangers shed a tear for one another.

I leaned over to give him a hug. And then, although it is not really like me, I kissed him on the cheek. I felt his weakened hands on my arms, the thin stubble of his whiskers brushing my face.

MORRIE: (whispers) So you’ll come back next Tuesday?

We Talk About Feeling Sorry for Yourself

MITCH: I asked Morrie if he felt sorry for himself.

MORRIE: “Sometimes, in the mornings. That’s when I mourn. I feel around my body, I move my fingers and my hands—whatever I can still move—and I mourn what I’ve lost. I mourn the slow, insidious way in which I’m dying. But then I stop mourning. I concentrate on all the good things still in my life. On the people who are coming to see me. On the stories I’m going to hear. On you—if it’s Tuesday. Because we’re Tuesday people.”

MITCH: I grinned. Tuesday people. I thought about all the people I knew who spent many of their waking hours feeling sorry for themselves. How useful it would be to put a daily limit on self-pity. Just a few tearful minutes, then on with the day. And if Morrie could do it, with such a horrible disease . . .

MORRIE: It’s only horrible if you see it that way. It’s horrible to watch my body slowly wilt away to nothing. But it’s also wonderful because of all the time I get to say good-bye. (smiles) Not everyone is so lucky.”

MITCH: I studied him in his chair, unable to stand, to wash, to pull on his pants. Lucky? Did he really say lucky?

We Talk About Regrets

MITCH: I wondered what regrets he had once he knew his death was imminent. Would he have done much differently? Selfishly, I wondered if I were in his shoes, would I be consumed with sad thoughts of all that I had missed? Would I regret the secrets I had kept hidden?

MORRIE: Mitch, the culture doesn’t encourage you to think about such things until you’re about to die. We’re so wrapped up with egotistical things, career, family, having enough money, meeting the mortgage, getting a new car, fixing the radiator when it breaks—we’re involved in trillions of little acts just to keep going. So we don’t get into the habit of standing back and looking at our lives and saying, Is this all? Is this all I want? Is something missing? (pause) You need someone to probe you in that direction. It won’t just happen automatically.

MITCH: I knew what he was saying. We all need teachers in our lives. And mine was sitting in front of me. And I figured if I was to be the student, then I would be as good a student as I could be.

That day, I made a small list on a yellow legal pad, issues and questions that we all grapple with:

Death
Fear
Aging
Greed
Marriage
Family
Society
Forgiveness
A meaningful life

We Talk About Fear

MITCH: The small horrors of [Morrie’s] illness were growing, and when I finally sat down [again] with him, he was coughing more than usual, a dry, dusty cough that shook his chest and made his head jerk forward. After one violent surge, he stopped, closed his eyes, and took a breath.

MORRIE: “What I’m doing now, (eyes still closed) is detaching myself from the experience. And this is important—not just for someone like me, who is dying, but for someone like you, who is perfectly healthy. Learn to detach. Detachment doesn’t mean you don’t let the experience penetrate you. On the contrary, you let it penetrate you fully. That’s how you are able to leave it.”

MITCH: I’m lost.

MORRIE: Take any emotion—love for a woman, or grief for a loved one, or what I’m going through, fear and pain from a deadly illness. If you hold back on the emotions— if you don’t allow yourself to go all the way through them—you can never get to being detached, you’re too busy being afraid. You’re afraid of the pain, you’re afraid of the grief. You’re afraid of the vulnerability that loving entails. But by throwing yourself into these emotions, by allowing yourself to dive in, all the way, over your head even, you experience them fully and completely. You know what pain is. You know what love is. You know what grief is. And only then can you say, ‘All right. I have experienced that emotion. I recognize that emotion. Now I need to detach from that emotion for a moment.’”

MITCH: Morrie stopped and looked me over; perhaps to make sure I was getting this right.

MORRIE: I know you think this is just about dying, but when you learn how to die, you learn how to live.”

MITCH: I thought about how often this was needed in everyday life. How we feel lonely, sometimes to the point of tears, but we don’t let those tears come because we are not supposed to cry. Or how we feel a surge of love for a partner but we don’t say anything because we’re frozen with the fear of what those words might do to the relationship.

Morrie’s approach was exactly the opposite. Turn on the faucet. Wash yourself with the emotion. It won’t hurt you. It will only help. If you let the fear inside, if you pull it on like a familiar shirt, then you can say to yourself, “All right, it’s just fear, I don’t have to let it control me. I see it for what it is. I know that there are other emotions in the world, and I’m going to experience them as well.”

MORRIE: “Detach.

We Talk about Society

MITCH: Morrie believed in the inherent good of people. But he also saw what they could become.

MORRIE: People are only mean when they’re threatened, and that’s what our culture does. That’s what our economy does. Even people who have jobs in our economy are threatened, because they worry about losing them. And when you get threatened, you start looking out only for yourself. You start making money a god. It is all part of this culture. (exhale). Which is why I don’t buy into it.

You must build your own subculture. Here’s what I mean. . . I don’t mean you disregard every rule of your community. I don’t go around naked, for example. I don’t run through red lights. The little things, I can obey. But the big things— how we think, what we value—those you must choose yourself. You can’t let anyone—or any society determine those for you.

The problem, Mitch, is that we don’t believe we are as much alike as we are. Whites and blacks, Catholics and Protestants, men and women. If we saw each other as more alike, we might be very eager to join in one big human family in this world, and to care about that family the way we care about our own. But believe me, when you are dying, you see it is true. We all have the same beginning—birth—and we all have the same end—death. So how different can we be?

MITCH: He squeezed my hand gently. He smiled.

MORRIE: In the beginning of life, when we are infants, we need others to survive, right? And at the end of life, when you get like me, you need others to survive, right? (whispers) But here’s the secret: in between, we need others as well.

Graduation

MITCH: Morrie died on a Saturday morning. He had fallen into a coma two days after our final visit, and the doctor said he could go at any moment. Instead, he hung on, through a tough afternoon, through a dark night. Finally, on the fourth of November, when those he loved had left the room just for a moment—to grab coffee in the kitchen, the first time none of them were with him since the coma began—Morrie stopped breathing. And he was gone.

Have you ever really had a teacher? One who saw you as a raw but precious thing, a jewel that, with wisdom, could be polished to a proud shine? If you are lucky enough to find your way to such teachers, you will always find your way back.

The last class of my old professor’s life took place once a week, in his home, by a window in his study where he could watch a small hibiscus plant shed its pink flowers. The class met on Tuesdays. No books were required. The subject was the meaning of life. It was taught from experience . . . The teaching goes on.
```

---

## IC-0463: Typical Day

- Title: Typical Day
- Author (byline): Jonathan Walton
- Work: Millennium Monologues
- Publisher: Meriwether Publishing
- Publication date as stated: Nov 2002
- Event as filed: Dramatic Interpretation
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

I remember staring into those same eyes, those same frowning faces. The prosecutor shouting insults, back and forth as he paces. I testified in my own defense, “I wasn’t there,” I cried. “I don’t even own a gun, so how in God’s name could I have shot someone?” Upon the truth I swore and all of the words I said were true but all at once the lawyer turned and said, “Why should they believe you?” The foreman began to rise and he handed down a verdict of guilty. All at once I rose to my feet and at the top of my lungs, I began to scream.

“I don’t belong in prison - get your hands off of me!” I fought as they put cuffs on my hands, and chains on my feet; but it didn’t matter what I did- to prison they carried me. My lawyer filed appeal after appeal, but we could make no one believe.

Awaiting my sentence, I sat within this cement block. I spent many nights crying out to God, “Lord I have done nothing wrong, nothing!” “Please God, don’t leave me here to rot. I don’t think I could take it Lord. No, I know that I could not.” Later that month I received my sentence, the words pierce my heart to this day. The foreman again stood to rise and before he sat, I was condemned to die.

I haven’t seen the stars in eight years, if you could count the drops in the oceans - only then could you begin to count my tears. I am all but forgotten, my family no longer visits me. All I have left are thoughts and memories.

My mother used to cook breakfast on Sunday morning as she sang Amazing Grace, the love of God, shown off her face. As she kneaded the biscuits it would go something like this, (sings verse of Amazing Grace). My wife, she had the smile of an angel. I swear you could see wings, if you gazed from just the right angle. The birth of my daughter, so small within my arms. I remember the first time she called me Daddy, it filled a void with in my heart. But my third year here, my momma passed away. I missed her funeral, the month of January, that fourth Monday. My wife remarried and my daughter should be thirteen; I am all but forgotten, no more visits to Daddy.

The last bite settles in my stomach and the warden instructs me to rise. I have resolved in my mind that I am going to die. I walk the last one hundred feet, one foot in front of the other - left then right, left then right. The chains clank across the floor, I squint my eyes in the light. I try to turn my wrists but I meet pain - the shackles so tight. I walk into the room, with my head held high. I enter into the witnesses’ midst wearing not a frown nor a smile. The executioner asked for my last words and I look each victim in the eye.

“The state killed me years ago, gave me a number - I no longer had a name. Inmate number 49536, I was not a person, I was a convict. I used to be a man until I came here, now I’m part of an unwanted clan. A group of rejected individuals, clasped in chains and wearing orange suits. This was not the way it was supposed to be! Just as your loved one’s life was stolen, the state, the judge, the jury, - each and every one of you; stole my life from me. I have been raped and beaten, ridiculed and scorned. I looked up to God and cursed the day I was born. My spirit is broken and my heart forever dismayed. My body stands before you, but my mind has passed away.”

The shackles were secure and the metal cap put into place, as the tears began to flow down my troubled face.

“Please Lord, take me quick! I am not worthy of this punishment. You are the only one who can read my heart and you know that I am innocent.” I looked over to the wall and the executioner began to reach for the lever. So before the electricity flowed through my veins, I look up to heaven. “The Lord is my Shepherd, I shall not want. He maketh to lie down in green pastures, He leadeth me beside still waters. He restoreth my soul. He leadeth me on the path of righteousness for his namesake. Yea, though I walk through the valley of the shadow of death; I will fear no evil, for thou art with me. (stops abruptly, body convulses, and dies)
```

---

## IC-0464: Under the Wolf, Under the Dog

- Title: Under the Wolf, Under the Dog
- Author (byline): Adam Rapp
- Work: Not specified
- Publisher: Candlewick Press
- Publication date as stated: Sept 2004
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: STEVEN, MOM, DAD, NURSE
- Teaser before the introduction: Yes
- Spoken words (computed): 2182
- Already set (do not supply): none

### Source block (context only)

```text
Author: Adam Rapp
ISBN: 978-0763618186
Publisher: Candlewick Press
Date (Month/Year): Sept 2004
```

### Introduction (context only: never use it for content warnings)

```text
Steven Nugent was a gifted student, in the honor program at school, taking accelerated classes and he appeared to have the world by the tail . . . that is until his world and his family began to fall apart. This is his story . . . . Under the Wolf, Under the Dog by Adam Rapp
```

### Performance text (classify this)

```text
STEVEN: (Page 1-3) How to start. Okay. Here it goes. Mrs. Leene said I should begin by describing myself. So, my name is Steve Nugent. I'm just seventeen. It was my birthday last month, in November. Now it's the middle of December, and the trees around here arc caked in ice and sort of silvery in that creepy, wintry way, so right now seventeen seems like a hundred years off. In terms of size, I'm six foot three and about 145 pounds, which is way too skinny, I know. I can't help that right now. The doctors say I'll fill out in a few years. At this point I would describe myself as being a pretty high-percentage dodge-ball target. I’m also blind in my right eye, which I will tell you more about later. So I'm currently in residence at this place in the middle of Michigan called Burnstone Grove. There are about thirty-five kids here. About half of us are drug addicts, and the other half have tried to check out of this world in one way or another. Probably a third of us have dabbled in both pursuits. I don't entirely fit into either category, so I'm what they call a Gray Grouper. The Red Groupers are the junkies, and the Blue Groupers are the suicide kids. There are only seven Gray Groupers, and we're generally kept here for a month or two before we're either shipped back home or sent to another, more affordable, facility. The truth is that I could easily be a Red or Blue Grouper. I’ve done some drugs, and I have to admit that I’ve through about the other scenario more than once. All of that will come later, though. I don’t want to tell you everything just yet.

STEVEN: (Page 6) So . . . a couple of months ago, my brother, Welton, hanged himself with a necktie. I think that’s a good place to begin. My Mom died just a few weeks before that . . . (Page 9) My mom my mom my mom my mom my mom. . . (page 10-14) Maybe Welton killed himself because he lived in the basement. Who knows what all that damp air and cement will do to a person. Maybe he killed himself because for the last year of his life all he did was smoke weed and play Vice City on his Play Station II. And then again, maybe it was some weird noise in my brother’s head, some little digital murmur he never told anyone about. I’ve heard about that – how you wake up one day and there’s like this permanent dial tone droning somewhere in your head, a little Dustbuster trapped where the brain saves you from going crazy. After a while you wind up ending it all just to make things quiet again. I found Welton in his room in the basement. He'd knotted the necktie around a hook at the top of his door. The hook had broken, but that didn't stop the asphyxiation. What's weird is that he was kneeling. It looked like he was praying or pulling up weeds in a garden. For some reason half his face was blue. Right now when I close my eyes and try and see the parts of his body, I keep missing stuff, like his arms and his shoulders. I can see his face as clear as day and I could even go into detail about his Adam's apple or this little blue vein under his right eye or the weird paste that was coming out of his left nostril, but other more obvious things like limbs are lost to me. Limbs and eye color. I can't place that either. It was like someone had stolen that stuff. The EMT guys were as quiet as aliens, and when they pushed the gurney through the living room, I finally reached over and closed Welton’s mouth. "Bye," I said to him as they wheeled him away. Just for a second I had the feeling that he might say something back, but he didn’t. He just looked sort of waxy and stunned. I know my mom would have been making coffee for everyone and trying not to cry – she was strong like that – but she was already dead. [I remember her last few weeks] . . . I was about to get ready for bed [one night] when I heard my mom call for me. Whenever she would call out my name like that – especially during her last few weeks – it was like getting thumped between the shoulder blades with a hammer. (Page 47-50) In the hospice room, my mom was trying to reach the straw from her water cup. She was totally bald at this point, and the whites of her eves had dulled to this weird brownish gray. She only weighted eighty-something pounds and her lips had sort of disappeared. My mouth hurts just imagining her.

MOM: Steven, help me drink, honey.

STEVEN: I took a step toward her and l could see a new growth pressing through her forehead. There were things emerging all over her lately. At first they were calling it breast cancer, but now it was everywhere. A few weeks before, the oncologist had discovered a tumor in her abdomen that was the size of a baseball. She took my hand and asked me to do an Our Father with her. I knelt down at the side of her bed and bowed my head. She took my hands with one of hers, and we began. [Our father who art in heaven, hallowed be thy name] Her fingers were bloated and soft. While we prayed, I sort of went blank. I kept waiting for something to stir inside – like a holy fluttering or whatever – but it never came. When we were through praying, my mom fell asleep. Even though her mouth was all dried and shriveled, she was sort of smiling. The morphine always made her happy. I must confess here that there was a time or two when I was tempted to slip the needle into my own vein just to see what it was like, but that would have been heinous. I slid my hands out from under hers and quietly left her room. (Page 52) All of a sudden, for some reason, my [house] felt like it was shrinking, like the walls were totally losing in on me. So that’s when I left. The keys to the Fairmont were on the kitchen table. I grabbed them – no one else would be using them anytime soon. (Page 55-57) l got bored with the radio after about fifteen minutes and turned it off. The last think I needed was more insanity in my life. Suddenly the steering wheel was vibrating. I looked at my hands and they were trembling so bad I thought the veins in my wrists would burst. I pulled over to a Shell station. I was sort of hyperventilating, so I had to take a moment to catch my breath. That’s when I started doing the Our Father again. [Our father who art in heaven, hallowed be thy name] I sat there for a moment and thought about my mom. It was her groans of pain that would get me the most. Sometimes they didn’t even sound human. (Page 77-79) When I turned onto our block, I switched the lights off and stopped the engine. Then I shifted to neutral and coasted into the driveway. I left the car keys on the kitchen table and limped straight to my mom’s room. She was sleeping really still and her room smelled even worse than ever, I just stood there and watched her curtains blowing for a moment. I remember how blue they were. I think it was the first time I had ever noticed them. A moment later I heard the door creak behind me. I turned around and my dad was standing in the entrance. He was wearing a three-piece suit. It was gray and it looked too small, like he'd stolen it. He made a swallowing sound and adjusted the knot in his tie.. .

DAD: She's dead.

STEVEN: He just stood there staring at my mom, but I wouldn't look at her. You couldn't have paid me a million dollars. I was afraid of what I might see, that some other crazy tumor was popping out of her mouth or something. Then he said it again. “Dead.” One word. All by itself. (Page 90-91) My mom my mom my mom my mom my mom ... The day after she died, they cremated mv mom and stuffed her ashes into a pine box and put an eight-by-ten photo next to it. When the priest announced that there would be a moment of silence for those of us, who were too shy to share a special memory or speak on [her] behalf, Welton started singing "The Star Spangled Banner." (Page 94) Mrs. Leene says that everyone grieves differently, that sorrow and anger manifest themselves in strange ways because of how our minds are actually designed to protect us from those feelings. I will say this: I wish I could have cried then. I think if I could have had a good cry, things might have gotten better somehow. (Page 239-241) [That night, I found that my mom had left Weldon and me a letter]. . . (Steven reads) “Remember me, please. An ordinary woman with a good heart. A woman who loved her children and took great pride in them. Remember that I was a great nurse who treated everyone with the same compassion. Remember that I wanted our family to be close, but I died without that happening and I felt sad about it. Remember that I loved you both with my whole heart and though I was far from a perfect mom, I did the best I knew how. Welton, have faith that your back will heal and that you will one day again play basketball. [aside: (Page 10) As a junior, Welton was the starting forward on the basketball team, but he had to quit three-quarters of the way through the season because of a herniated disk. My brother never quite made it back onto the basketball court] Steven Jacob, remember that I loved you – and would have done anything to stay with you. I think you are the smartest person I know, my sweet boy. The Moon will rise, The Sun will set, Please do not forget . . . . Mary Lee Nugent.”

(Steven puts his hand to his face and pushes hard against his eyes with his thumbs, struggling to control his emotions) (Page 244-250) I woke to a nurse feeding a tube into my right arm. The IV needle was cold, and I couldn’t see out of my right eye. Everything on the right side of my body sort of throbbed, and I was afraid to move. “Where am I?”

NURSE: You’re in the intensive care unit of the ophthalmology ward at Medical Associates.

STEVEN: “What happened?” My voice sounded like it hasd been taken out and put back in.

NURSE: Well, from what I hear, you put ywn thumb through your right eve. You have a shield over it. It was a various serious puncture, Steven. There’s a strong chance that you’ve lost vision in your right eye.

STEVEN: (Page 272-273) . . . “My mom died,” I said. I had no idea that was going to come out of my mouth, but it did. “She had breast cancer . . . And she died.” I could feel this totally thick sort of anguish feeling taking over my body that has never quite left. (Long silence) (Page 6) And then . . . a couple of months ago, my brother, Welton, hanged himself with a necktie. [I found him . . . ] (Page 286-288) Down in the basement, Welton’s door was three-quarters open. The Price Is Right was on full volume. My brother’s room was a cyclone of laundry, CD boxes and warped and ketchup-stained paper plates. His stereo had been turned down, but a CD was spinning quietly. It was that Bottomside song “Forty Holes and Forty Goals.” I turned the TV off and the music played. [Sing a couple of lines of the song here – link to a video of the song is provided at the end of this selection]: “There’s a hole in my head, I’m gonna find it; I’m gonna fill it . . . . There’s a hole.” I pressed stop and turned the stereo off. I turned around and there he was. He’d hanged himself from a coat hook at the top of the door. He’d used one of my dad’s old Marine Corps ties. I just stared at him for a moment. “Hey . . . Everything’s gonna be okay, okay?” Then I closed his door, which was actually really heavy, and headed back upstairs. (Long silence) (Page 2) So [now] I'm currently in residence at this place in the middle of Michigan called Burnstone Grove. (Page 310) [Before you go] I just have to say a few more things. I’ve been thinking about them a lot the past few days. It’s sort of this list I’m starting . . .

1. People are born and people die.
2. Parents get cancer and their ashes get stuffed into earns.
3. The urns get buried in holes
4. Brothers break your heard.
5. You have to deal with stuff on your own and that’s all there is to it.

Song “Forty Holes and Forty Goals” by Bottomside : https://www.youtube.com/watch?v=p- 8yV4JRehA
```

---

## IC-0465: Unusual Normality

- Title: Unusual Normality
- Author (byline): Ishmael Beah
- Work: The Moth Presents All These Wonders
- Publisher: Crown Archetype
- Publication date as stated: March 2017
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: ISHMAEL
- Teaser before the introduction: Yes
- Spoken words (computed): 1573
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ishmael Beah
Book: The Moth Presents All These Wonders
ISBN: 978-1101904404
Publisher: Crown Archetype
Date (Month/Year): March 2017
```

### Introduction (context only: never use it for content warnings)

```text
From 1991 to 2002, Sierra Leone was embroiled in a devastating civil war, which garnered international attention for its blatant use of child soldiers. Children, some as young as 7 years old, made up between 40 and 50 percent of the Revolutionary force and approximately 20 percent of the government’s military. Approximately 10-14 thousand children were exploited and forced to be child soldiers in Sierra Leone.

Ishmael Beah’s parents and two brothers were killed and he was forcibly recruited into the war at age 13. After two years, with UNICEF help, he was removed from the army and placed in a rehabilitation home in Freetown. Mr. Beah later became UNICEF’s first Advocate for Children Affected by War. He has vowed to do everything in his power to . . . “make sure that what happened to me doesn’t continue to happen to other children around the world.” This is his story.

Unusual Normality by Ishmael Beah
```

### Performance text (classify this)

```text
ISHMAEL: I came to New York City in 1998. I was seventeen. I entered the United States with just a passport in my hand, because somehow the baggage that I'd checked when I boarded the flight from the Ivory Coast (which was tattered in ways unimaginable) didn't make it.

I stood there watching all these huge bags go by, and mine didn't come. This bag held all my possessions at this point: two pairs of pants and two shirts-one long-sleeved and one short. So I just started laughing, and I didn't even bother going to the lost-baggage section to claim it. I just walked right out to meet my new adoptive mother, who was standing there with a beaming smile, waiting for me.

ISHMAEL: I had come to the United States. To have a new home, and to live with a mother who was willing to take me into her life when most people at the time were afraid of somebody like me. It was a chance at living again, because all I had come to know, since I was eleven, was how to survive. I didn’t know how to live. All I knew, really, up until this point in my life, was struggle. This was what I had come to expect from life, and I didn’t trust in happiness or any kind of normality at all.

So here I was in New York, with my new mother. We needed to step into that normality. But we had a lot of things to deal with, and one of the most pressing ones was that I needed to get into school. You see, the visa that I had been given was a prospective-student visa. This meant that when I arrived in the United States, I had three months to get into a school. If I didn’t, I would be returned to my war-torn country, Sierra Leone.

When I went to some of the interviews, I was immediately denied because of the following conversation: “Do you have a report card to show that you had been in school?” I would say, “No.” And then my mother would interject to explain the context. I would sit there thinking to myself, What do these school principals think? Do they really think that when there’s a war in your village and people are gunned down in front of you, and you ‘re running for your life, you’re thinking to yourself, “You know, I must take my report card and put it in the back of my pocket.”

I was [finally] accepted to the United Nations International School. Thus began my two years of high school and making other teenagers confused about who I was. You see, I didn’t fit into any box. I didn’t have the same worries about what shoes or clothes I wore. And of course, I couldn’t tell them, because I felt that they were not ready to hear the truth. What was I going to say? “Hey, you know, I was a child soldier at thirteen.” So I was silent, mostly. And this made them more curious.

They would say to me, “You’re such a weird kid.” And I would respond by saying, “No. I’m not weird. Weird has a negative connotation. I prefer the word unusual.” When I was finished saying this, they would look at me and say, “Why don’t you speak like a normal person?” They thought maybe my English was like this because I was from some royal African family.

But I needed to be silent about my background, because I also felt like I was being watched. When I got into the school, some of the other parents were not very happy that somebody with my background was in school with their children. And I realized that the way I conducted myself would determine whether they would ever let another child who had been through war into such a school.

These kids were tough (they told me). Because they lived in a tough city, New York. And therefore, they were tough. They had gotten into fights and won. So they would say things to me like, "If you want to survive the streets of New York City, we need to teach you a few things." And I would say, "Well, thank you very much. I truly appreciate this advice that you're giving me."

Truth was, I'd been to some of these places that they spoke about, these neighborhoods, and I knew that the people who lived there didn't glorify violence the way they did. They didn't have time to pretend, because they lived in it, just like I had. I noticed that these kids had an idea of violence that they'd never really lived. They glorified it in a way, because they'd never actually experienced it at all.

When I walked with them, I observed that I paid more attention to the people who walked past us. I didn't take the same route twice, because I didn't want to develop a predictable path. These were all habits that were formed from my experiences, but I noticed that my new friends didn't do that. So I knew they were just saying these things to seem tough to me. I wished that the only violence I knew was the violence that I imagined.

After about a year of being friends with these boys, one of them decided to invite a group of us to upstate New York. His family had property up there, and we were going to play a game called paintball.

"You use these balls of paint, and you shoot people," and he explained the basics of the game to me. And I thought, if these guys who only pretend about violence can play it, it must not be that difficult a game.

As soon as we arrived, I began to memorize the terrain immediately. I knew how many paces it took to get to the house, how many paces it took to the first tree, to the first bush, to the shed. And this was all out of habit, because where I came from, in my previous life, this kind of skill set could determine whether you lived or died.

They showed me the weapon, how you shoot it. And I allowed them to teach me to shoot things. They were very macho about it. They said to me, "This is how you shoot, you aim like this." I said, "Okay." I tried it a few times. I deliberately missed. Then they showed me the camouflage and the combat gear.

"Yeah, we're gonna go out! We're gonna DO THIS!!" They started painting their faces, getting into this idea of war that they knew. I declined putting the face paint on. (Beat) So we went off into the bush, and when one of them shouted, "Yeah, let the war begin! I'm going to bring pain to all of you! I'm going to show you how it's done!" I thought to myself: First rule of warfare, you never belittle your opponent. But I didn't say this. I went into the bushes.

I would hide. I would wait for them. And they would come rolling around, jumping, doing all kinds of things, things they'd probably seen in movies about how people act in war. And after they were done exhausting themselves, I would come up behind them, and I would shoot them.

This went on all day. And when we came back that night, they talked about it. “How come you're so good? You're sure you've never played paintball before?

“I grew up in a village. And I used to be a hunter when I was a boy, so I know how to blend into the forest, like a chameleon. I know how to adapt to my environment."

They wanted to beat me, and so they started to team up with each other. I would see them doing this, and then I would come up with a kind of watered-down version of another guerrilla tactic. I would walk backwards and then stand where my footsteps "began" and hide. They would follow my footprints, and then I would come up behind them.

When I returned, I told my mother about this game. And my mother, being a mother, was immediately worried. "Oh, did that bring up something for you?"

"No, it didn't, absolutely." Because I know the difference between pretend war and real war.

They never invited me back to play paintball with them. And I didn't ask to be invited back. I had so wanted to talk to them about the war while we were playing the game. I wanted to explain certain things, but I felt that if they knew about my background, they would fear me.

It was only years later that they learned why I had won the game. But I wish I had been able to tell them early on, because I wanted them to understand how lucky they were to have a mother, a father, grandparents, siblings.

People who annoyed them by caring about them so much and calling them all the time to make sure they were okay.

They were so lucky to have this naive innocence about the world. I wanted them to understand that it was extremely lucky for them to only play war and never have to do the real thing.

[Because] their naive innocence about the world was something for which I no longer had the capacity.
```

---

## IC-0466: Visiting Mr. Green

- Title: Visiting Mr. Green
- Author (byline): Jeff Baron
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Jan 1999
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: ROSS, MR. GREEN
- Teaser before the introduction: Yes
- Spoken words (computed): 2172
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jeff Baron
ISBN: 978-0822216810
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Jan 1999
```

### Introduction (context only: never use it for content warnings)

```text
Think about all the divisions in the world. We humans have an inexhaustible capacity to focus on what separates us rather than on what brings us together. Whether it's religion, ethnicity, nationality, race, gender, sexual orientation, or any of the innumerable other ways we classify each other, focusing on the “right and wrong” of differences leads to nothing but fear, separation and conflict. Jeff Baron in his play Visiting Mr. Green addresses many such separations. Ultimately the decisions each person makes are his own. I hope this selection inspires thought, because I have no answers; I won’t identify right or wrong. That decision is up to you.

Visiting Mr. Green by Jeff Baron
```

### Performance text (classify this)

```text
ROSS: (Pg 9) Sorry I’m a few minutes late. I never leave work this early, and today, especially, was the wrong day to be doing this, but anyway, here I am.

MR. GREEN: (totally baffled) Who are you?

ROSS: (realizes they’ve never been introduced) I’m sorry. (Offers his hand to shake) Ross Gardiner. Nice to meet you. You seem to be doing okay. I’m glad . . . (Pg 10) Mr. Green . . . I’m going to start coming here every week.

MR. GREEN: For what?

ROSS: (Pg 11) I can go shopping for you. It looks like it’s not so easy for you to get around. It must be hard for you. Since the accident, I mean.

MR. GREEN: How did you know about that?

ROSS: That’s why I’m here. For the next six months, I’m coming here once a week to help you. I don’t really have a choice. I have to. I got charged with reckless driving in the accident.

MR. GREEN: You had an accident too?

ROSS: (loses it) It was the same accident! I was driving the car you walked in front of. That’s why I’m here. My punishment is community service. You’re lucky you weren’t killed.

ROSS: (Pg 13) Hi, Mr. Green. It’s Ross Gardiner.

MR. GREEN: (Pg 14) What are you doing here?

ROSS: (sighs wearily) The social worker sent me back to the Judge. I told him you don’t want me to come. He said I have to. (Holds up the mail) Here’s your mail. It was all over the floor downstairs. Looks like you have some bills and a few letters in there.

MR. GREEN: This is your mail you’re so concerned about?

ROSS: Come on, Mr. Green. For now, we’re stuck with each other. (Holds out a paper bag) I brought you some food. It’s Kosher. (Pg 15) (losing his patience) Listen, I know you don’t want me here, and I don’t want to be here. If you want to eat it, eat it. If you don’t want to, don’t.

MR. GREEN: (Mr. Green begins eating hungrily) It’s not like Yetta made.

ROSS: (after a moment) That was your wife? How long ago did she pass away? (Pg 16) Tell me about Mrs. Green. I know she was a good cook. What else?

MR. GREEN: Nothing else. She’s gone. She left me.

ROSS: (after a moment) Mrs. Fanelli, the social worker, told me you don’t have any children.

MR. GREEN: No. I don’t. Gone. Everyone’s gone. . . . (Pg 21) Are you Jewish?

ROSS: Who told you I wasn’t? Well, Mr. Green . . . I don’t remember my bris, but apparently, I had one. My father’s an expensive lawyer . . . what else . . . hey, (Pg 23-24) were you born here?

MR. GREEN: In this apartment?

ROSS: No. Here in the United States.

MR. GREEN: Of course. My parents came over right after the trouble in Kishinev.

ROSS: Kishinev?

MR. GREEN: You don’t know Kishinev? You’re supposed to be Jewish. In Kishinev, which is in Russia in case you don’t know, they ran through the street killing Jews. Hundreds of Jews. They threw us in jail for no reason, they took our money for no reason. You want to beat us, you want to rob us, you want to kill us? Go ahead. The police don’t mind. The czar doesn’t mind. So, when you left, you weren’t moving, you were getting the hell out of there. You heard about this from your grandparents, right?

ROSS: Actually, I never knew my grandparents. They died before I was born. (looks around room) [This] pace really, really needs a cleaning.

MR. GREEN: Yetta always cleaned.

ROSS: (Pg 25) How long were you married?

MR. GREEN: Fifty-nine years. She was a wonderful wife. She came and helped me out at the store.

ROSS: What kind of store?

MR. GREEN: A dry cleaner. Downstairs. I had to stop working about ten years ago. I got sick . . . (Pg 27) What do you do for a living? It’s not important. You make a good living, right? So why aren’t you married? (Silence from Ross) (Pg 30) You know, Ross . . . I think the Good Lord sent you to me. And I hope he sends someone to you. Someone just like Yetta. (Off Ross’s shrug) Believe me, find yourself the right girl and you’ll . . .

ROSS: There is no right girl. Not for me, Mr. Green.

MR. GREEN: I’m telling you, Ross. For every boy . . . there’s a girl.

ROSS: (after a pause) Not if you’re gay.

MR. GREEN: What?

ROSS: Gay (off Mr. Green’s uncomprehending look) Homosexual (Still not registering) A faygele. ******

ROSS: (Pg 31-40) So, Mr. Green . . . about last week . . . you know, the thing I told you . . . (Mr. Green remains silent) I was just wondering . . . all week, actually . . . if you feel . . . you know . . . okay about it.

MR. GREEN: Okay. Okay. I feel okay (let’s change the subject already tone) So . . . you brought food? (Ross puts his briefcase down, puts the deli bag on the table and goes into the kitchen to put the food away)

ROSS: I found out where my grandparents are from . . . Pinsk.

MR. GREEN: I know Pinsk. (after a long pause) It’s near Minsk.

ROSS: (after a pause) So . . . I got some good news this week . . . I got promoted.

MR. GREEN: So now you can afford to get married. It would be so terrible?

ROSS: (frustrated) It wouldn’t be terrible . . . if I were interested in women. But as I already told you . . . quite clearly . . .

MR. GREEN: (interrupting) Maybe you didn’t know this. Jewish boys are not faygeles.

ROSS: What are you talking about? Some of them are. (a beat) Listen, I wasn’t planning to tell you I was gay. I just happened. I was almost gonna come here tonight and tell you I met a very nice woman. A very nice Jewish woman.

MR. GREEN: (pleased) You did?

ROSS: No. I was gonna make up that story so we could pretend what I told you last week wasn’t true. But we’re friends, right. I don’t want to lie to you.

MR. GREEN: (thinks for a moment, then) You know, Ross . . . I’ll tell you the truth. I was a little bit scared of the girls, too.

ROSS: I am not scared of women.

MR. GREEN: (gets up, picks up the deli bag) Maybe I’ll clean up a little.

ROSS: Why can’t we talk about this? (Off Mr. Green’s silence) We’re both grownups. Why does this have to be such a big deal? (Then to himself out loud) I’m sick of it being such a big deal (Starts pacing, then with stored-up frustration) I don’t get it. I really don’t get it. One minute I’m the perfect son – they love me, they’re crazy about me, they can’t stop bragging to their friends about me . . . And the next minute . . . literally the next minute . . . they treat me like I murdered someone. This was years ago, and we still haven’t talked about it. It wasn’t as if I lied to them my whole life. I thought I was straight, too. Well, I wondered about it.

MR. GREEN: (interrupting) Ross . . . Maybe I don’t have to know all this.

ROSS: No, you do . . . So, when you tell me to find a nice girl and get married, you’ll know why I can’t sit here with my mouth shut. (a beat) I mean I can. I have. But really, Mr. Green . . . I’m almost 30 years old. (Mr. Green motions for Ross to continue) I go to a party one night, and I meet this guy, Paul. It was like for the first time in my life, I could relax. I was just . . . in love. It was great. Until this one Saturday morning. I’m alone in my room, and my mother comes in and sits next to me on my bed and says, “Ross . . . are you and Paul . . . more than friends?”

MR. GREEN: She asked you that?

ROSS: I know I couldn’t believe it. I was not ready to have that conversation, but there she was . . . So I just said yes.

MR. GREEN: What did she say?

ROSS: Nothing. She started crying. I kept saying, “Mom, It’s okay. I’m really happy. You’ve met him. He’s a great guy. But she stopped listening. And we never talked about it again. My dad, on the other hand, just stopped talking to me. Completely. He wouldn’t even look at me. I didn’t know what to do. I became completely self-conscious. Am I acting gay? Do I walk like I’m gay? Is this a gay tie? My mission in life was to never say or do anything that might make someone think I was gay. So I wouldn’t go anywhere in public with Paul. I still loved him and he still loved me, and when we were alone, things were great . . . but the rest of the time. (remembers painfully) I basically pretended he didn’t exist. (after a moment) I can’t believe I did that to him. So I haven’t touched or kissed another person in four years. I sort of got used to it. I thought I did. But I’m not used to it. I hate it.

MR. GREEN: (after a moment) No. You shouldn’t be alone. . . . But Ross . . . Not a man.

ROSS: (Taken aback) Why not?

MR. GREEN: You know why not . . . It’s not what God wanted.

ROSS: How do you know what God wanted?

MR. GREEN: You only get a baby with a man and a woman.

ROSS: Did you and Mrs. Green have a baby every time you made love? Of course not. You were together for almost sixty years without having a baby. How is that different from me being with a man. Do you really think God wants me to be alone?

MR. GREEN: No. He wants you to be with a woman.

ROSS: Then why did he make me attracted to men?

MR. GREEN: That’s your decision, not God’s.

ROSS: Oh, I see. One day I just decided. Why not make my life fifty times more difficult? What a good idea. What a smart decision.

MR. GREEN: Listen Ross . . . You’re not like them. They act like women . . . they touch each other in the toilet . . . they bother little boys . . .

ROSS: Wait a minute. Do you really believe that? (Off Mr. Green’s silence) You do. You have no idea what you’re talking about. (Thinks for a minute) You’re doing the same thing you said people did to Jews. “They smell funny, they lie, they heat, they’re all pickpockets.”

MR. GREEN: It’s not the same. We’ve always been persecuted. How are you persecuted? You have money, you have a good job. . .

ROSS: Yeah. As long as I pretend I’m straight. As long as I keep laughing at stupid gay jokes. . . Every day. You don’t know how hard that is.

MR. GREEN: You call that persecution. You’re not persecuted. Not like the Jews. What about the Holocaust?

ROSS: What about the Holocaust? The Nazis were killing Jews and homosexuals. This isn’t a contest. All I’m saying is that being Jewish, you know what it’s like to be hated for something you can’t change.

MR. GREEN: You can change.

ROSS: No, I can’t. I can pretend I’m not who I really am. I’ve been doing it most of my life. I’m sick of it. . . . A week ago, you said the Good Lord sent me.

MR. GREEN: A week ago I didn’t know you were a faygele.

ROSS: Well now you know. But that’s all you know. You don’t know a thing about the Good Lord. He’s not some narrow-minded bigot like you.

MR. GREEN: Get out of my house! Get the hell out! (after a moment) You and my daughter. You think you know everything.

ROSS: (stops in his tracks) Your daughter? (Mr. Green looks away) You have a daughter? (Mr. Green doesn’t respond) You told me]you don’t have any children. What’s her name?

MR. GREEN: Rachel. Her name was Rachel. (thinks, then with stored up anger) You wanna know how you’re like Rachel? You think you wrote the Torah. You think you can change all the rules. You can’t do that! If she stayed home where she belonged, she would have met a Jewish boy and given her mother grandchildren. But she’s gotta run off to college with the goyim and break her mother’s heart. Thanks to you two, no more Jews will be born. You’re finishing the job for Hitler.

ROSS: (after a moment) So she married someone who wasn’t Jewish. (Pg 42) Does Rachel know her mother passed away? (no response) She doesn’t, does she?

MR. GREEN: Maybe you never learned this. There are rules. There are laws. The law says if you marry a goy, you’re dead. Rachel is dead. We sat shiva already.

ROSS: (can’t believe it) And that was it? You never talked to her again. . .

MR. GREEN: (angry) (Pg 46) Rachel, Rachel. You don’t know Rachel. Rachel destroyed my family.

ROSS: I don’t think so.

MR. GREEN: What are you saying? (Furious) You’re telling me how to be a father? What the hell do you know?

ROSS: (frustrated) Nothing. I don’t know anything. (after a moment) All I know is you have to tell Rachel her mother is gone.

MR. GREEN: (Pg 48-49) But . . .

ROSS: But what?! (Off Mr. Green’s silence) Mr. Green, I had a terrible day, and I just can’t . . .

MR. GREEN: What was terrible?

ROSS: You really wanna know? I went out for lunch today. It was a 60th birthday party for my father. Twelve people at a big table – his friends, his partner, my mother, my cousins and me. The waiter comes in to take our drink orders. He’s obviously gay. My father, who is standing sort of behind the waiter, starts making fun of him, imitating his mannerisms. I say to him, quietly, “That’s enough, Dad.” The waiter leaves and my father gets up and does an impression of the waiter. (Acts out his father as the effeminate waiter) “We have some delightful specials for you today.” (as himself) Then he turns to my mother (As his father being the waiter) “Those earrings. They’re fabulous!” (as himself) I can’t take it anymore. I say, “Stop it, Dad. He stops. He turns to me and says, “Relax, Ross. We’re in New York City. Our waiter’s a fag. It’s not gonna make the national news.” And everyone laughs. I say, “Oh yeah? Well so is your son.” Then everyone’s quiet. Very quiet. Then my father says, “Well, maybe you can get a job here.” Everyone laughs. I leave. That’s it.

MR. GREEN: What do you expect?

ROSS: I expect to be able to go out with my father and not be humiliated.

MR. GREEN: Think how he must feel. With his friends. With his family.

ROSS: I’m his family. (a beat) Why am I even talking about this with you? . . . . Tell me, Mr. Green. Because I really want to understand this. You found out Rachel wasn’t gonna be what you wanted her to be, so you sat shiva and you never saw her again. Were you really able to go on with your work and your marriage and never even think about your only daughter? (a pause) How could you to do that? Did your religion help you do that? . . . (silence) She isn’t dead. (a beat) I gotta get out of here (Ross heads for the door)

MR. GREEN: Ross . . . (long pause) I never did. (this is hard to say) I never stopped thinking about her. About Rachel. (Ross doesn’t know what to say. He just stands there. After a moment, Mr. Green motions for Ross to come over. He opens his arms. Ross walks over and Mr. Green takes him in his arms. They comfort each other)
```

---

## IC-0467: A Walk to Remember

- Title: A Walk to Remember
- Author (byline): Nicholas Sparks
- Work: Not specified
- Publisher: Grand Central Publishing
- Publication date as stated: Sept 2004
- Event as filed: Dramatic Interpretation
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
In this heart-wrenching story, Landon Carter is shown the depths of the human heart and the joy and pain of living from a most unexpected person . . . Jamie Sullivan. A Walk to Remember by Nicholas Sparks
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

## IC-0468: Walking on Glass

- Title: Walking on Glass
- Author (byline): Alma Fullerton
- Work: Not specified
- Publisher: HarperTeen
- Publication date as stated: Jan 2007
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: TRIGGER WARNING
- Teaser before the introduction: Yes
- Spoken words (computed): 1583
- Already set (do not supply): none

### Source block (context only)

```text
Author: Alma Fullerton
ISBN: 978-0060778514
Publisher: HarperTeen
Date (Month/Year): Jan 2007
```

### Introduction (context only: never use it for content warnings)

```text
Your mother’s suicide attempt has left her in a coma from which she’s never waking up. You know that she wouldn’t want to live like this, but could you really help her die? The hardest decision of your life, and there’s no one to help you . . . It’s all up to you.

Walking on Glass by Alma Fullerton.
```

### Performance text (classify this)

```text
TRIGGER WARNING: MOTHER’S SUICIDE AND DEATH

*NOTE: Cutting follows the columns left to right as they appear on each page.

(Pg 4) Writing a journal it’ll just make me think,
for some shrink and I don’t want to think.
won’t make me Mom thought too much.
feel better. Look where it got her.
It won’t change
what happened.

(Pg 10) I slouch in a chair He nods, waiting for me to say more.
across from Dr. Mac. I don’t, making him ask,
He takes my journal “How are you?”
and flips through it I shrug. “Same.”
without reading,

****
like he promised.
“I’m glad you’re writing.” (Pg 12) I took the photograph
He hands it back. From the mirror in my mother’s room.
“How’s your mother?” Her at the age of eight,
I spin my chair, lean back, perched high in a tree,
and put my feet up on his desk. arms stretched out like
“Same.” an untamed eagle,

prepared to take on
The world.
I keep the picture
in my pocket
so I’ll always
remember
the way she was
before she was caged
by a baby
she never wanted.

****

(Pg 13) Dad says,
“Come and see Mom.”
So I do.
Mom,
tucked tight in the bed,
empty minded.
No longer herself,
or anyone else.
Wires force life into a body
left hanging
like a marionette
With no one to pull
the strings.
Dad leans close to her
and whispers,
“You’ll come home soon, dear.
Everything will be better.”
I know he really
wants that
to be true,
but the thought of her
coming back
into our lives
makes my insides
flip.

(Pg 16) I don’t want her to die.

I just want

it all to

stop.

Does that make me

so terrible?

****

(Pg 35-36) The beeping

from her machines

shrieks.

A reminder

her soul is tethered to the ground,

a captive falcon,

circling in confusion,

longing for someone

to set it

free.

. . . and I think maybe sometimes

nonexistence

is better than being

caged.

I stand watching her.

I want to smack her

for putting us through this.

I want to scream,

“Why didn’t you want to live

You’re supposed to want to stay here

with us!”

If she’s going to die,

she should get it over with

and just

do

it.

(Pg 45) I stand over Mom,
shaking inside,
and wonder why she did it.
Why she didn’t think about anyone
but herself.
Why she didn’t think
about us.
Why she didn’t think
about me.

****
(Pg 48-49) Nurses lurk
around Mom’s bed
like vultures.
But Dad guards her --
a lion
ready to pounce on
the vultures as they swoop
to take away his mate.
He doesn’t seem to know
what the vultures
already know.

She’s gone.

If Mom came home,
things wouldn’t change.
Her mood would always flip
from bad to worse
in a matter of seconds,
and for the rest of our lives
Dad and I would
be walking on
shards of glass
from a broken
chandelier.

**** (Pg 56) My teacher asks everyone,

“If you could change

anything in history,

what would it be?”

Kids say things like,

I’d prevent wars

or Bin Laden and Hitler

wouldn’t have been born.

Other kids not their heads to agree.

When the teacher asks me,

I say,

“Four months ago,

I would have come home

five minutes earlier.”

Everyone looks away from me

like my face is on

sideways.

****

(Pg 58) It’s too quiet

at home,

and it smells different.

There’s no longer

the scent of fresh flowers

Mom always kept

in the living room.

Instead I smell

dust, rot, and

even after cleaning the floor,

blood.

Why can I still smell

the blood?

****

(Pg 64) As I sit on the couch

staring at a cushion,

in silence,
I keep seeing Mom
curled up and gripping
this cushion on this couch,
alone,
crying
in the dark.
Instead of going to her,
I walked by.
Saying nothing,
like she was invisible.
I hug the cushion
and smell it,
hoping to get a hint
of her perfume,
but it’s gone.
. . . I go to my room,
and turn up the music
loud
so I can forget what
I remember.

****
(Pg 70) My father
cries out to Mom
in his sleep.
I slide from the warmth
of my bed
to sleep on the bumpy couch
in the living room,
where I’ll no longer
hear his calls.

****
(Pg 73) What’s left of the
old chandelier
is heaped next to the window.
And once in a while

the sun shines in

and rainbows dance

against the walls.

It’s as if the crystals

stole Mom’s spirit.

I hang the crystals

by the window

in Mom’s room.

I hope they

give her

spirit

back.

****

(Pg 82-83) Today

the doctors tell Dad

there’s still no hope.

Mom’s not getting better.

They ask if he would

consent

to have the machines

shut down

and donate

Mom’s organs.

Dad gets mad.

He refuses to believe

she’s gone.

But I’m feeling

more relieved

than mad.

God, Forgive Me . . .

The thought of my own mother

dying

shouldn’t leave the taste of

freedom

in my mouth.

****
(Pg 87) Nurses flock
to Mom’s room
like she’s having a sale
on white sneakers.
In between their visits
I’m alone with her
and her machines.
I reach for the machine
to do what I need to do.

My hands shake,
and sweat drips
down the back of my legs,
stinging the open blisters
on my heels.
I jerk my hand away,
without even touching
the switch.
I race out of there,
gasping for air,
and throw up on
the shoes I still can’t
fill.

****
(Pg 93) Dad putters around the house
avoiding me.
I want to get right up
in his face
and scream for him
to be the man he should be
so I won’t have to,
but I
can’t.

(Pg 95) “I know you think I’m wrong,”

Dad says.

He looks at me

over the piles of

takeout containers

on the coffee table.

“I can’t let go yet.”

I scarf down my

chow-mein noodles

to avoid looking

directly at him.

“It’s not my fault. . . ,”

he says.

I glance up.

His eyes water

I focus my attention

on my noodles.

“And I didn’t know she was that

unhappy,” he says.

I put my plate

across the table.

It tips.

I get up

and walk away,

leaving my dad’s heart

and the noodles

spilled all over the floor.

****

(Pg 102) As I left the house

that June morning,

Mom said,

“I love you.”

I just closed the door

and left her

alone.

I should have told her

I loved her.

Maybe then
she wouldn’t be
in the hospital
today.

****
(Pg 103) I bring Mom
roses.
I watch her carefully,
looking for any clue
she knows I’m with her.
She lies there
lifeless.
I try to swallow the lump
building in my throat,
but it just expands.
The aroma from the roses
filters through the air.
They smell like she used to
when I was small.
Sweet and fresh.
Their scent
will fade
now that they’re
no longer attached
to the roots
which gave them life.
I stare outside
and wonder
if I’ll ever have the courage
to cut Mom off
from her roots.

(Pg 106-107) I don’t doubt for a second that most people think what I want to do

is wrong.

But I don’t want to

murder

my mother.

I want to set her

free.

Murder

The unlawful killing of a human

being

with malice

aforethought.

I’m thinking about it.

Does that make it

murder?

(Pg 119) Mom doesn’t have

a future.

Mom doesn’t have

a life.

Mom has been dead

for six months.

You can’t call

it murder.

****

(Pg 112-113) Dad sits beside

Mom’s bed.

He strokes her hair

and whispers to her.

He closes his eyes.

Clenching his jaw,

he lets out a sigh.

When he opens his eyes,

a tear drips from each corner.

He shakes his head

and walks out of the room.

I wait for him to come back.

He doesn’t.
I wonder
if Dad is torn up inside
for the same reason
I’m torn.

*****
(Pg 116) Today
Dr. Mac explains how
sick Mom was.
How she needed medicine
to make her feel better,
but she refused to take it
He explains how,
if she did,
she’d still be here.
Today Dr. Mac
explains how
sick Mom was
and how nothing she did
was my
fault.

***** (Pg 122) What happened ???

That day,
I came home and found
a new pair of shoes
by the door.
When I went into the dining room
to tell Mom they were
too big,
mom stepped off of the table.
A noose slung around her neck.
I caught her
and held her up.

Mom struggled.

She kicked me away.

But I wouldn’t

let go.

(Pg 109) Sometimes I wish

I hadn’t held Mom up.

Then it would have

all been over

that rainy June day.

(Pg 122) [But] I wanted to tell her

I loved her.

I wanted to tell her

I needed her.

I wanted to tell her

to stay with us.

The wires holding

the chandelier snapped

and it crashed on top of her head,

and my arm broke

and I dropped her.

Her blood splattered

all over my new shoes.

****

(Pg 125) I remember

her soft voice

floating through the air

like the smell of fresh roses,

as she sings me a lullaby

to take away

the monsters in the night.

I remember

her dimpled smile,

her blue eyes,

her gentle touch.

I remember my mother, the way she was.

**** (Pg 130) [It’s] Mom’s birthday

The doctors take
Dad into another room,
leaving me alone
with the shell
of my mother.
I brush the hair from her face
and rest my hand
on her forehead.
I sit,
listening to the machines
as their parts move,
```

---

## IC-0469: The White Guy

- Title: The White Guy
- Author (byline): Stephen Hunt
- Work: The Best American Short Plays 1997-1998
- Publisher: Applause Books
- Publication date as stated: February 2000
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1922
- Already set (do not supply): none

### Source block (context only)

```text
Author: Stephen Hunt
Book: The Best American Short Plays 1997-1998
ISBN: 978-1557834263
Publisher: Applause Books
Date(Month/Year): February 2000
```

### Introduction (context only: never use it for content warnings)

```text
Mark Twain once said “There are many humorous things in the world, among them the white man's notion that he is less savage than the other savages.” This might be true, a white man may be no different than any other man. However, history shows that though the white man is down, he most certainly is not out. “White Guy” by Stephen Hunt
```

### Performance text (classify this)

```text
I long to go to Detroit, not Flint.
It is 1968 and I live in Manitoba, Canada.
And as I am seven, my world is divided in two: places that are on television, and places that
aren't. Detroit is on television.
Flint isn't.
Flint has shopping, but Detroit has the Tigers.
I see the Tigers on TV all the time.
Ty Cobb played for the Tigers, in the twenties.
I read a book about Ty Cobb once.
Ty Cobb had a .367 lifetime average.
Do you know how high that is?
Dad, we could go to a game! It would be fun!
It's an American city!
Dad says, No.
[Beat.]
Why not, Pop? We go through Flint every summer. Flint sucks.
Why can't we go to Detroit?
Dad goes, We take one wrong turn at Detroit,
the blacks will turn over the trailer and set fire to it.
[Beat.]
That was a surprise answer.
I don't know what to say.
I don't know any blacks.
There are no blacks where I come from.
The only thing I know about blacks are what I've read
in sports biographies - From Ghetto to Glory, The Bob Gibson Story.
Wilt Chamberlain, the only player to score 100 points in a game. Willie Mays, the most
exciting ballplayer of his era.
Willie Mays sounds so cool, he's my favorite player,
even though his era was never my era.
It's best not to argue with Dad, though.
Travelling is all business with him.
We go through Michigan on our way to Ontario
because gas is cheaper than in Canada.
We write down the mileage in a book, so we can figure out miles-per-gallon. We keep track
of what we spend.
We rise at dawn, to maximize daylight driving.
We always tell Customs the truth.
For me though, travelling isn't business at all.
It's total bonus points.
I'm thinking,
if the blacks realize we're from Canada,
they won't turn our trailer over and set fire to it!
Just point to the license plate, Pop!
We never did anything!

It's 1968, and they're burning down inner cities
across America, and just because Willie Mays is
your favorite ballplayer don't mean nothin’.
To nobody.
We skip Detroit.
I'm the Boss, Dad says, And you do what the Boss says.
When you're the Boss, you can go to Detroit.
Detroit's not going anywhere.
We pull up outside a shopping mall in Flint.
Who wants ice cream? Pop asks.
I'm buying - as if he doesn't buy everything.
My Dad gets out, then sticks his head back inside.
You coming in, or you just gonna sit there and sulk?
I don't speak. I'm never speaking again.
Have it your way, he says. We'll be inside if you change your mind.
They all go into the mall. I watch them, thinking, why is the right answer
always 'no' with him?
Sometimes, I think the guy got his degree from the University of 'No.'
That's when I make a promise to myself.
Someday, I'm getting out of there.
I'm gonna get to a place where people say 'yes.'
I'm goin' to Detroit.
[beat]
Mabuti comes from Lesotho, a township by South Africa.
I can't picture this Lesotho place in my mind. They don't have any teams from Lesotho.
They never get on television.
Lesotho is like, the Flint of South Africa. Down there by South Africa, somewhere.

Country full of protestors, from the sounds of it.
Protesting what?
Well - South Africa. Apartheid. White Guys!
Who sound like the very worst white guys ever invented.
White guys even a white guy could hate.
Mabuti is a small man. He has a beard. He seems wise,
someone who puts the big picture before himself.
He has a bullet scar on his forehead.
That's where he got grazed.
That's what they call it when the bullet doesn't stick,
it just skims past you, leaving a permanent scar.
Mabuti has friends who weren't so lucky.
Mabuti came to Winnipeg. He goes to my university.
He is the first black man I know.
I meet him one day at a party at the university President's house. Our university is
sponsoring him.
Every year, we sponsor one person from someplace awful. Generally ends up being a black
guy, from Africa, as a rule.
We have Yohannes Selassi, from Ethiopia.
Yohannes isn't what you think when you hear 'Ethiopia.'
He's not starving at all.
Yohannes claims he's related to the Emperor Halle Selassie,
and since none of us knows nothin’ about Ethiopia, and hey they have the same last name
we accept this as fact.
We got Grace Edward Galabuzzi, from Uganda.
Grace is a soccer player with astonishing posture.
Like Prince Charles.

And to tell you the truth, Grace seems more British than African. But Mabuti is different.
He seems truly African.
Mabuti is a wise jester, a prankster.
If Grace Edward Galabuzzi is an Empire man, Mabuti is his Irish counterpart.
Mabuti will always join ya for a drink.
And sometimes,
Mabuti hints at the horrors he has witnessed in life,
but he never goes into very much detail.
Of course, I do the right thing.
I'm always horrified by his stories - as if I could be anything but. Mabuti makes me feel
like he understands me.
In fact - and this is what's so great about the guy - he makes me feel
as if he understands how hard it is to be me,
listening to all those bad things that happened to him.
In summer, I lose track of the Africans.
They vanish from my life.
Whoosh! Africans, away.
I rediscover my old life, my high school buddies.
We have barbecues in our backyards,
go to the cottage,
play golf, watch baseball on TV;
none of us has any real plans.
We have our own indigenous way of life.
We are at home here.
Hey - we're white guys!
Nothin is a biggie...
As for the Africans - well, I don't know what happens to the Africans in summer.

You see, I don't want to know what happens to the Africans.
In principle, I am anti-apartheid, but in practice - well, it would be weird,
awkward, it's summer - the thing is, my high school pals, they don't want to meet new
people. They want things to be familiar. Until
Late one night, around midnight, the phone rings,
- and it's Mabuti. Of all people.
Hey man, how are you? He asks.
Mabuti, how you doin'?
Thinking, why are you calling me in the summer?
I'm no good man.
Why not? What's wrong?
Thinking, please don't give me more information than I need? I'm just not doing very good
man, he says. I'm alone here.
He asks. You wanna do something? Mabuti. I'm real tired.
Man, he says. Come on.
I need company.
[Beat.]
No, can't do it. I gotta get up early.
You take care, Mabuti. You'll be OK. 'Night!
I'm going to sleep now.
I can't go out with everyone.
I gotta go to work in the morning.
I think these really normal thoughts everyone thinks all the time. But I have another
feeling, underneath those feelings. Something like, that one was a test, a cosmic challenge.
And I failed.
In my own way, I said,
This is my house.

You can't come in.
OK, I'm a white guy. I know it. It's obvious, right? You probably think I'm this
domestic beer drinking,
red meat eating, USA Today reading, ESPN watching,
normal, perfect home-owning
kind a guy!
And you'd be surprised,
how long I went
before noticing that I'm actually this Bass Ale drinking,
sushi eating,
khaki-shorts wearing, Bravo-Channel watching,
New Yorker reading emotionally-arrested
kind of renter!
[Beat.]
But then again,
To everybody else, lookin' back at me, it's so obvious, I'm just one thing:
a white guy!
I'm part of a tribe!
Know what that means, don't you?
Construction workers sittin' on their high beams when I walk by don't shout 'nice ***’.
Women seeing me come towards them on the street don't, clutch their purses tighter.
[Beat.]
Cops don't shoot me by accident.
Never.
Does not happen.
To live the life of a white guy,
in a white guy's world, well, it's, it's
It's nice.
It's tremendous.
But frankly, it's not the greatest time to be me.
For one thing, my media role models suck.
The only thing you ever read about white guys these days
is either how mean we are or how mad we are.
Witness the collected films of Michael Douglas.
And one reason why so many of us are mad
is this certain intellectual perspective
held by universities and certain political parties and non-profit theater across America -
those season tickets theaters,
you know the ones I'm talking about, theaters
dedicated to serving audiences smarter than usual.
It's not something they say out loud - because a lot of us are season ticket holders - but
it's there, in the subtext,
of almost everything.
You just gotta listen for it.
It goes a little like this:
who invented patriarchy?
A white guy, livin' in a cave, tired of chasing down takeout. Who invented Apartheid?
A white guy, who showed up one day in darkest Africa and said, to hell with Holland, I'm
stayin!
And I gotta be in charge!
Who ruined the Ozone Layer?
Well, let's just say - a white guy, with perfect hair,
driving his Ford Explorer 10 MILES AN HOUR down the Santa Monica Freeway!
Who stole rock and roll?

A fat, spangled jumpsuit wearin', 14-year-old marryin', pill devourin',
B-movie makin', Live-in-Hawaii,
Hunka-hunka burnin’ white guy!
Dead, on a stamp!
Look we're the problem with everything!
But
To tell you the truth, when I was in college,
I hated white guys too!
In fact, I hated white guys so much
I forgot I was one.
As much as I could.
I mean, let's face it - it's tough, when you recognize the enemy - and it's you.
I had a limited set of choices to work with.
I couldn't become a non-white guy.
I was still attracted to women.
I was ashamed of my lifelong passion for competitive sports. [Beat ]
[Then, sadly:]
I turned inward.
Started writing. Poetry. Bad, sad, poetry.
Until I was completely disgusted with myself.
Then, I wrote a TV script - spec script - about a group of tough, yet sensitive lesbians.
Single moms by day, Canadian documentary filmmakers by night. Called it... Goddesses.
I even sold it, to Canadian television.
You never know, with those wacky Canadians.
To those of you out there who aren't white guys and I can feel you out there
- and you're welcome here
you might think our little 5000 year winning streak came at your expense.

You have a point there.
To you, I say, sorry about that.
And to those of you like me,
white guys who feel a little down,
a little browbeaten, a little frustrated, remember:
there are still things we can be proud of:
Who was first on the moon?
A white guy, with a five iron!
Who's almost all of the coaches?
White guys, even though they're almost none of the players. Who's on the money?
White guys, white guys, and more white guys-and pyramids.
Who wrote Death of a Salesman?
A red white guy, a well-liked white guy.
Who were the Beatles?
Tell me a white guy is the problem with everything, and I say, OK, we did steal rock and
roll.
Guilty.
And we do make easy targets.
Don't shoot!
```

---

## IC-0470: Witness

- Title: Witness
- Author (byline): Peter Maloney
- Work: Found in The Best American Short Plays 2006-2007
- Publisher: Applause Theatre and Cinema Books
- Publication date as stated: April 2010
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: KASIM
- Teaser before the introduction: Yes
- Spoken words (computed): 2199
- Already set (do not supply): none

### Source block (context only)

```text
Author: Peter Maloney
Book: Found in The Best American Short Plays 2006-2007
ISBN: 978-1557837486
Publisher: Applause Theatre and Cinema Books
Date (Month/Year): April 2010
```

### Introduction (context only: never use it for content warnings)

```text
In the era of Saddam Hussein, Abu Ghraib, twenty miles west of Baghdad, was one of the world’s most notorious prisons, with torture, weekly executions, and vile living conditions. As many as fifty thousand men and women—no accurate count is possible—were jammed into Abu Ghraib at one time, in twelve-by-twelve-foot cells that were little more than human holding pits But then, after 24 years as the brutal ruler of Iraq and nine months as a fugitive, Saddam Hussein was captured in a US Military raid on December 13, 2003. U.S. forces took over the prison, and renamed it the Baghdad Central Detention Center. Beginning in 2004, accounts of physical and psychological torture, and sexual abuse of prisoners held in the Abu Ghraib prison in came to public attention. These acts were committed by military police personnel of the United States Army. Meet Kasim – a detainee ready to bear . . . Witness by Peter Maloney
```

### Performance text (classify this)

```text
Place: Abu Ghraib Prison, Iraq Time: April 2004 [Sound of metal door slamming very loudly. At same time lights bump up. Shouts of prisoners, dogs barking somewhere.] [KASIM sits on the lower bunk of an iron bed. There is no mattress, only a plywood board. KASIM wears an orange jumpsuit. He holds a baseball in one hand and regards it. He opens his mouth wide, as if he wants to take a bite of the baseball. He looks up at us.]

KASIM: It occurs to me ... perhaps they thought we eat these things. That they thought it is some kind of fruit, and that we eat it. I could have told them that this is not indigenous to Iraq, that baseballs do not grow on trees here. And that, in any case, it is not a fruit. But they do not speak my language. And the translator was not there when they tried to feed it to me. [KASIM looks at the baseball. He opens his mouth as wide as possible. He closes his mouth, looks at us.] It barely fit into my mouth. They had to break two teeth to get it in. [He opens his mouth wide again, points with a finger to broken teeth in back.] I tried to spit the baseball out, to push it out with my tongue, but they tied a scarf around my head to hold it in.

With the baseball in my mouth, I could only breathe through my nose. It was fortunate for me that it was not the season of my asthma, or I might have suffocated. I was frightened, and I wanted to tell them about my asthma, but the baseball in my mouth made it impossible for me to speak.

KASIM: I was abducted on the day the Americans captured Saddam. I was with my friend Ameen. The news of Saddam's capture had just come over the TV: I closed up my shop and we ran out into the street. The TV in the window we left on so that people outside could watch the events as they unfolded. I had loaned Ameen my video camera. He was making a film about the situation here. At the time of the invasion, he had filmed the falling statues, and now he wanted to film the people's reaction to the fall of the man himself. The reaction of the man in the street. We were hurrying along the river in the direction of the AI- Salam Palace. There were so many people, all of them shouting, dancing in the streets. American soldiers sitting atop their Humvees, grinning, smoking cigarettes. I was so happy to see Saddam go away. You know he destroyed our country. He humiliated us. I thank you, President Bush. There was one tank on the street. Ameen laughs and says, "Hey, it's Clint Eastwood's tank." I look, and even with my bad English I can make out, stenciled on the barrel of the big gun: "GO AHEAD, MAKE MY DAY." I am standing right by the tank. Ameen was taking pictures of all the action when somebody behind us starts shooting at the Americans. I hear the firing and the bullets hitting the tank and I ducked down. It becomes a kind of instinct. I know *they* are likely to fire grenades next, so I drop to the ground. Now an American soldier has his foot on my back and his rifle pushing hard behind my ear and he is screaming at me in English. The tank is shaking and I hear explosions, and sure enough Clint is firing the big gun in the direction the shots came from,

I am lying on my stomach with this boot on my back and the barrel of the gun pushing my head into the pavement and then my video camera joins me there on the ground, all the pieces of it clattering into the gutter. Before I know it my hands are tied together behind my back with the plastic laces and I am being pulled up onto my feet. Ameen is up against the tank, another soldier's got him covered. His hands are tied, too, and he has a sandbag over his head.

They took us in a Humvee, with other guys they rounded up. To Camp Cropper, out near the airport. They put us in a tent. I didn't see Ameen again. [He is quiet [or a moment, then, suddenly agitated, he stands and, looking up as if to the upper tier of cells, cries out in a loud voice.]

We were in the tent for eight days. Bagged and cuffed. That was in December. It was cold. No one in the tent knew why we were there. Somebody in the tent knew some English and he asked the soldiers why we were there. They told us we knew why. But we didn't know. They said they were the ones who ask the questions and if they didn't like the answers they'd send us all to Guantanamo. They kept saying we were going to Guantanamo, that once we were there we'd be wishing we were back here.

So when they are loading us into the truck to move us out, this soldier pulls me aside, holds me back. Everybody is in the back of the truck but me, they're packed in, cuffed and bagged, and the soldier is ready to put a bag on my head. But before he does he takes out his wallet and flips through some pictures he keeps in there. There's his mother and his wife or his girlfriend and his kid or his little brother, I don't know, and he finds the picture he's looking for. He puts his hand on my shoulder like we are buddies and he holds out the wallet with the picture for me to see. It's a picture of him in a red and black checked cap. He's holding a rifle, (an ordinary rifle, not the big gun he's carrying now), and tied across the front of his truck is a deer. He's holding on to the horn of this big deer and looking proud of himself. [Change of tone, more intimate. It is important to KASIM that we know what he thinks about this.]

The next thing I know I'm in the dark again and being lifted up, and they throw me across the front of the truck and tie me down. The soldiers are laughing and at first I'm not minding being tied down because the truck has been idling for a while and I am suddenly warmer than I have been in over a week. But by the time we are halfway to Abu Ghraib the hood is red hot and the metal is burning me right through my shirt and my pants. [He touches his jumpsuit very gingerly with his fingertips around his middle, his thighs.]

Can you do something for me? Maybe you can get in touch with my family? Tell my wife where I am. That I'm OK. Five months, man. Five months, and I still don't know what they want from me.

In the middle of the trip here, a sandstorm hit, and I was really glad for the sandbag on my head, which protected me somewhat. When we got here, they untied me, took the bag off, and this ... unearthly light was everywhere, because of the dust. Everything was ghamidh. You know this word? Mysterious. Ambiguous. Yeah.

When we got here we finally could take a shower. They took our clothes away. They took everything away. My watch. The thing is, I wonder if it's really five months, or does it just seem that way? They can do crazy things with time, you know. Stop it, practically. What if it's only been five hours? What if they haven't even noticed I'm gone?

I'm not supposed to tell what happened here. They say you wouldn't understand. But it's not right to do these things to people! Without permission, and without explaining anything! It's inhuman. Of course they aren't human, that's the thing. They can disguise themselves. As anything..

I've seen things you wouldn't believe. That's why we aren't supposed to tell you. Because you wouldn't believe it. It's not the time for you to begin believing. I don't know why they picked me. I guess they think it's time for me. Their ships are sometimes disguised as helicopters. You can tell by the light. It is the brightest light you've ever seen. You can't look into it without it hurting. I don't think they want to hurt us. They forced me to lie down. In a cubicle. It was cool and damp and it smelled bad. They put the bright light on me and looked me over. All over. They seemed quite concerned, about my burns from the truck. They checked me all over to see if I was hurt. Because I was hurt. It was like I was paralyzed. There was never just one of them. They were always with another one, or in a group. They looked human, most of them. Humanoid, I guess is what they are. They just touch you with their hand or an instrument and you go numb. At first it hurts a lot, for an instant, but then it doesn't hurt at all. You can't feel anything, and you can't move. You just lie there. You can't believe that you are just lying there, not saying anything, not protesting, but you can't. You just can't. Sometimes there are computers there and the beings are putting data into the computers while they do these things to you. And they are always taking pictures. There are balconies, and sometimes there are other beings watching from above. There isn't much furniture. You can't always tell by looking at them whether they are male or female, but somehow, you just ... know. The shorter ones are the helpers. The taller ones are in charge. That is definite. The small ones especially stare at you. It is dangerous to look at them. Somehow you know that, so you try not to look in their eyes.

They show us pictures, wide-screen, 360 degrees. In 3-D, no special glasses required. Pictures of things we see all the time, but stopped noticing. The gutters running like sewers; the marshlands disappeared; the pipelines burning in Kuwait; the sky black with smoke. We tried to tell them that it isn't all our fault. That Saddam did a lot of this. That the sanctions did a lot of it. Then the Americans, and in reaction to the Americans. But they didn't want to hear any excuses. They know the Garden of Eden, the original Janat Adn was just a few miles from here! From where we are standing, did you know that? Oh, yes, they know what they are doing by coming here. And they want us to realize what we are doing to the earth. If they are going to come here and take over, well, there has to be something left, after all. Something they can use.

I don't have much time left, but I will tell you what I think. I think that these beings may be ... angels. I think they are beings between us and God. It is not always easy to recognize them. Last night the visitant was E.T. Right here in my cell. I knew there was going to be another examination when they brought out the sheets and blankets and hung them over the bars so that no one could see in. I appreciate that. Privacy is good. They made me strip, which I hate to do, but I have gotten somewhat used to it. They needed to take another sample of some kind, I suppose. They never say. Four of them held me down, face down on the bunk here. Then E.T. was there. I recognized him, even though he was wearing fatigues like the others. He is short and ugly and his head is too big for his body and his eyes are huge. He looked at me. I tried not to look at him. He held up his finger and waved it back and forth in front of my face until I looked up. He was smiling, and his finger was glowing because he was E.T. Then he put the glowing finger up my . . . . [He struggles with what he is feeling.] It hurt and I cried out for God's help.

I believe I am leaving here tonight. They have examined me. All tests have been done, and the results are in. I've been inoculated against smallpox and diphtheria. There is no history of liver disease in my family. I have assured them of my complete cooperation. Tonight the impossible light will come down at the proper angle to form a ramp of energy from here to there. A guide will float us up the ramp straight ... through ... the bars.

AMEEN! ... YOUR FRIEND IS NOT MAD!

Straight through the bars to the ship, which is waiting for us. It will be ... as if ... I am a full bucket, pulled up from the well's darkness, then lifted out and up into the light.
```

---

## IC-0471: XOXO

- Title: XOXO
- Author (byline): Craig Shafer
- Work: Fast Horse Plays Round 4; Pgs 33-41
- Publisher: Fast Horse Drama
- Publication date as stated: Aug 2012
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: RANDY
- Teaser before the introduction: Yes
- Spoken words (computed): 1953
- Already set (do not supply): none

### Source block (context only)

```text
Author: Craig Shafer
Book: Fast Horse Plays Round 4; Pgs 33-41
ISBN: 978-0615711379
Publisher: Fast Horse Drama
Date (Month/Year): Aug 2012
```

### Introduction (context only: never use it for content warnings)

```text
XOXO by Craig Shafer
```

### Performance text (classify this)

```text
Randy – mid to late 20s. Laid back and in control of his emotions; charming, but rarely cocky.

RANDY: (Pgs 33-41) (unfolds a newspaper and scans with his finger; finds the item of interest, and begins reading) On December 23rd, Randy Crawford was the victim of a tragic automobile accident. He lost control of his vehicle on the icy roads of Wolf Creek Pass. He was transported to St. Mark's Medical Center where he never regained consciousness. Mr. Crawford is survived by Julia, his loving wife and his daughter Hailey, six. . . (his voice trails off; he clears his throat, sets the paper down and speaks to the audience)

I don't know about you, but I was never a real fan of obituaries. They're downright morbid, if you ask me. It creeps me out to think about those people who read them every morning. (chipper mocking tone as he mimics those people) "Nothing like starting my day with a glass of fresh OJ and today's obituaries! I can't wait to find out if someone I know has gone on to the other side!

But that one, that one I had my own morbid curiosity about. Probably because it was mine.

RANDY: Wait, lemme guess. You have a whole bunch of questions for me. Save your breath, lemme see if I can cover all of them. (beat) I'm here . . . but what I don't know is why. It's like being in a big, clear bubble. I can see everything that's going on around me, but I'm not part of it. The living world is a giant stage play, and I'm the one-person audience that can't boo or cheer. Don't ask me to explain. There wasn't any instruction manual. If they passed out The Dummies Guide to Being Dead and Perpetually in Limbo, I guess I missed it. (looks down for a moment, collecting his thoughts)

Oddly enough, I haven't thought about having a drink for a while now. And that's a big step for me. That was the last thing I had before the accident. I was over at Mickey's, off Highway 80, drinking with the guys after work. I didn't have just one or two, I had a bunch. The weather was bad, the roads were icy, and I shouldn't have driven. I lost control of the car and had a close encounter with a big oak tree. That's it. That's the ugly truth.

One of the weirdest things about being dead is that it makes the truth seem a lot less scary. If I was still alive, I would be all about baffling you with BS, giving you a line, trying to justify everything I ever did. But now, I don't have to do that anymore. I can just tell it.

I was probably an alcoholic from about 17, when I'd go out and party with my boys and then come home, sneak up to my room and party with another four or eight or twelve of my friends . . . they all happened to be named Bud Light. I was always either drunk or hungover in front of my parents. And either they loved me too much or too little to notice.

I met Julia in college when I was 20. Julia was the most beautiful girl I had ever seen in my life. Julia was worth not drinking. And so I didn't. For about a year. We got married a year later and I was the happiest guy in this little universe of ours. She was all I wanted. All I needed. But then Jules got pregnant, and, well, I got scared. Really, freakin’, out-of-this-universe scared. I had these nightmares where I'd forget to feed the baby, or I wouldn't hold it right and I'd accidentally drop it on its head. So, I started drinking again. Not a lot but sometimes, you know. The scariest part was actually being in the delivery room with Jules. And, I know how corny this sounds, but I realized how incredibly amazing life really was. [Hayley] was this tiny little person with bright red curls and these giant blue eyes and . . . I was a Dad. I told her something when she was just two days old. I told her . . . (suddenly holding Haley in his arms, speaking to her very softly)

“Your Dad is going to protect you forever. I'm gonna make sure you have everything you ever want or need. I love you." And I meant it. It's important that you know that. I loved Julia, but my love for Haley was a hurt-your-heart kind of love. I call her Halo, because she's a little angel. (close to tears; clears his throat and looks back at his audience) Alright, now you're thinking I'm some kinda touchy-feely, sappy sorta guy. Well, I'm not. I love pro wrestling and poker and lots of manly-man kind of stuff. Seriously. (long beat)

I tried to quit drinking. I tried even harder after Haley was born. I went to so many AA meetings that I'd show up at a work meeting and when it was my turn to talk, I'd almost blurt out, "My name is Randy and I am an Alcoholic." The meetings would work for a while and then I'd stop going. If I hadn't drank in a week or a month, I’d convince myself I didn't need to go anymore. That the meetings were stealing my time with Julia and Haley. And then I'd drink again. I went to my doctor and got some prescription . . . the pills gave me heartburn. And . . . umm . . . after a few days I still wanted a beer, so I washed one down with a Heineken. I went through hypnosis, I saw a therapist, I went to outpatient treatment. And every time, I'd stop . . . for a little while.

I never, ever hit my wife. I never yelled at my daughter. I wasn't an angry drunk. I was what the substance abuse people call a “Disorganized Alcoholic.” When I was drunk, I was useless. I wouldn't do the things I'd promised to do and that's how I hurt my family. I saw the pain on Julia's face every time I'd start again. I'd drink myself into a stupor and then I'd sleep for 12, 14, 16 hours to recover. Too drunk to pick Haley up from school. Too drunk to have dinner with our friends. I was sleeping so I couldn't go with Haley to the park to feed the ducks. (pauses, stares blankly)

When Haley was 5, I missed her kindergarten play. "The Grinch Who Stole Christmas." Haley was little Cindy-Lou Who. You know, the little who-girl who tells the mean-old grinch not to steal her family's Christmas tree. I slept through it. My boss had bitten my head off at work because I hadn't finished a project on time and so I went through two six-packs as soon as I got home. I was out cold by the time the curtains went up at Haley's school. I woke up in the middle of the night and went to the kitchen for water and Tylenol, and she'd left me a note on the counter. I've saved it in my wallet ever since. (takes the note out of his wallet and reads aloud)

Dear Dad: Mom says I was the best Cindy-Lou ever. I'm really sad that you were not there, because you're my Dad. I want you to always be my Dad and not the Grinch. But I love you even when you're the Grinch. XOXO, Halo. (refolds the note and returns it to his wallet)

What kind of father hurts his little girl like that? What kind of father picks a beer over his daughter? What kind of father was I? It was the same with Julia. I wasn't the father or husband they deserved. I was sober enough to somehow hang on to a job and provide for them but drunk too much to be the man I meant to be. The man I wanted to be. It was this evil, horrible voice inside me, telling me to drink, insisting that I needed it. I could keep it quiet for a little while, but I couldn't make it go away forever. I couldn't kill it. I tried. I really tried. (clears his throat and considers something for a moment)

I've been honest about everything except for one thing. (beat) That night at Mickey's I only had a couple of beers. I went out to my little red Tercel and I said, "Alright, Ernesto, you've served me well, Buddy, but it's last call." I had to keep myself together, you know? And I drove up to that spot on Wolf Creek Pass, the bend right before the oak, the spot I'd picked out weeks before. There weren't any other cars on the road, and I just sat for a minute and thought about how much I loved Jules and Halo and how I knew what I had to do. Then I jammed my foot hard on the accelerator. I hit that big old oak tree head on. Like a fly on a windshield.

And then I died, alone on Wolf Creek Pass in the middle of the night in my old rusty Toyota Tercel that I'd named Ernesto. (beat) I couldn't keep living as someone I didn't mean to be. I couldn't keep hurting the two people I loved more than I loved myself. I'd taken out a life insurance policy a few months before and set everything up to look like an accident. (beat) My death wasn't ruled a suicide. Everything worked out just as I planned. (pauses again, uncertain)

Perhaps you think I'm weak. Or you think I'm a horrible person. Well . . . I wasn't a very good one when I was alive. (beat) Sometimes, in life, you're given a range of options and you pick the best of the bunch. And the best I could do was make sure that they'd never need a penny. And that's what I did. Because I couldn't stop. I told Haley when she was two days old that I'd give her anything she ever needed. I was able to give more in death than I was in life. (long beat)

What I didn't count on was having to watch afterwards. I never even considered that. I thought it would just be black, to be honest with you. I never thought I'd watch Jules go out on her first date since I died. But I wasn't angry. I saw happiness in her eyes -- a happiness I hadn't seen for a long, long time. I didn't think I'd have to watch Haley and not be able to pick her up and hold her. I didn't think that was how it worked.

I don't know how long I have to stick around here and I sure don't know what's next. Maybe there's two options, maybe there's more. I'm almost as scared of that as I was when Halo was born. I do know one thing, though, I can wait forever. If that's the price, I can handle it. Because that's how long love can wait. It's like living as a shadow -- existing as the strange shades of grey between black and white. Not being with the living but not quite dead either. I can handle it. I'm probably not supposed to even try to communicate -- I'm sure it's against the rules or something, but I wrote something and I'm going to leave it on the kitchen counter at the house. And then I'm going to keep waiting. (unfolds another note and reads aloud, very softly)

Dear Halo: Your Dad wants you to know that you did a really super job as the Great Pumpkin in your Halloween Play. You were so spooky! He also wants you to know that life is going to be really, really hard sometimes. You're going to have to be so strong. It will seem impossible. But it's not. Life is beautiful, and you will be loved by so many people. Love them, Halo, and let them love you back. Don't ever be controlled, not by anything.

Tell Mom that Dad loves her and wants her to be happy. He loves you too -- forever, and that's a real long time. Even when you can't see him, he's there watching to keep you safe. He isn't drinking and he won't ever again. XOXO. (refolds the note and shakes his head sadly to end selection)
```

---

## IC-0472: Yellow Bus

- Title: Yellow Bus
- Author (byline): Leslie Epstein
- Work: Boston Theater Marathon 1 (Pg 57-62)
- Publisher: Samuel French, Inc.
- Publication date as stated: 978-0874401349
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: NISEL
- Teaser before the introduction: No
- Spoken words (computed): 1213
- Already set (do not supply): none

### Source block (context only)

```text
Author: Leslie Epstein
Book: Boston Theater Marathon 1 (Pg 57-62)
ISBN: 978-0874401349
Publisher: Samuel French, Inc.
Date (Month/Year): 978-0874401349
```

### Introduction (context only: never use it for content warnings)

```text
(no introduction)
```

### Performance text (classify this)

```text
“Those who cannot remember the past are condemned to repeat it.” With fewer living Holocaust survivors who can serve as eyewitnesses to the genocide and with a new wave of anti-Semitism in the US and Europe . . . will the past be forgotten?

In a 2020 nationwide survey studying Holocaust knowledge among millennials and Generation Z, 63% of adults under 40 did not know that 6 million Jews were murdered in the Holocaust. In fact, 1 in 10 reported never having heard the word Holocaust. What’s more . . . Over 40,000 concentration camps and ghettos were established during World War II, but nearly half of US respondents could not name a single one. (shakes head, takes a deep break and begins)

The year is 1941: Nisel Lipiczany is a boy of, let us say, 14. The Jewish Ghetto in Lodz, Poland is being liquidated by Nazi forces. Jews are being relocated by trainloads to “work the farms.”

Nisel manages to escape and follows the train track for days. But when he arrives at the train’s final destination, he doesn’t see a farm . . . just a Yellow Bus by Leslie Epstein.

NISEL: (Pg 57-62) I arrived late in the night. The tracks curved off side by side into a forest. The rails gleamed like the path left by a pair of giant snails. And there was the moon, sitting in the branches like a bright, fat owl. I plunged in.

But soon the trees stopped. Cut down. A sound, a groaning, a creaking. It came from a building, a big one, made from wood. All around it were the Death’s-Headers. They were sitting and smoking and walking this way, that way, this way. The moonlight moved on their helmets.

Dawn! Now I could see everything in the clearing. The mill had three stories and a water wheel at one end. Turning and turning. I could see how the black buckets rose out of and sank into the roof. This was the noise, the creaking, I heard in the night. I lay pressed to the ground. They sky above was full of dark, low clouds, like sacks of something about to burst. What was this place? Why were the windows of the mill boarded up? What – could someone tell me what – was it grainding? Then a Warrior – he pulled on gloves, white ones, lifted the bar on the door and some of the Jews came out.

There were thirty of them all together. They carried their bundles. They still had their stars on their coats. They stood about in their black coats, their black hats. The Death’s- Headers were standing too, or leaning against the side of an old yellow bus.

I could see the old-fashioned round headlights, one cracked, the other without a lens at all. The wings of the hood were lifted and a Warrior was lying over the fender, at work on the engine inside. The yellow roof – it was battered, dented, as if it had been stoned.

The band of Jews moved closer to the rear of the bus. They were all from our courtyard: Palfinger, a jeweler, two of the Fiebig sons, the Widow Greenkraut. I thought: Here they are, the plowers, the milkmaids, the ones who will pluck up the eggs. This is the bus that will take them all the way to the farm.

Then one of the Lords and Masters said something to them. Right away the Jews put down their sacks and valises and began to take off their clothes. Everything All of it. Even the undergarments. And they tied their shoes together by the laces. The back door of the bus swung open, the thirty Jews climbed inside, and the door slammed shut once more.

The mechanic slid from the fender, clapped – like this! – his hands together, and turned the crank. The engine started. The bus body shook. Drive off! Drive away! Drive to the farm! But the old bus did not move from the spot.

Only then, then, did I notice two things: first, the front wheels were missing, and second, there was no driver on the seat inside. Yet the engine roars, the body shakes, it sways. Minutes went by, one like another. A dark bird, dark like a crow, floated downward from the sky. It perched on top of Madame Dickstein’s white bundle. The motor ran for a quarter of an hour. But it was the bird that scared me.

Then the engine stopped. A Man of Valor – the same one with the gloves, the one from the mill: he walked to the side of the bus and put his ear against it. Just like in a synagogue. That’s what he said. They took the Jews out of the bus. All of them . . . . were sleeping.

Horses now. They were pulling a rubber-wheeled cart. In this cart the Jews were driven away – Up the riverbed. Out of sight. The piles of clothing, the luggage, the shoes – that remained behind.

And now, one after the other came fresh groups of Jews. The bus shuddered as usual, and then the sleepers were brought out again… again… again. Finally, at dusk, the rubber-wheeled cart picked up the mountain of clothing. The Warriors walked beside it to the mill.

Night fell. No stars. No moon. It was as dark as it is when I have my eyes shut. I walked into the riverbed. After a while, not long, a few minutes, I came to where the Jews were lying. Too dark to see their faces. Impossible to tell if my mother or father were there. I said, Wake up! Wake up, Jews! Let’s go back to the ghetto! I know the way! But they didn’t wake up. It was I who fell asleep beside them instead.

In the morning my mind was clear. Sane. Rational. Before I opened my eyes, I knew I would be surrounded by corpses. And there – there they were. With excrement on their legs. And some of the women stained with their own blood. I heard a sound. Soft. Nice almost. Shhhhh. Shhhhhh. Like someone with his finger on his lips. Shhhhh. Two men were walking among the bodies. Bending like farmers with scythes. They cut off the locks of the dead people’s hair.

What else to do but jump up and run? Run! Up the riverbank, through the clearing, into the forest. Then south, always south, not once stopping – until I came to where I thought there would be Jews. (a brief pause: then) Isn’t it true? Aren’t you? Look at me, dear people! All of you people! Are you awake? Are you alive? Are you Jews?

(pause)

CLOSING

According to the International School for Holocaust Studies, the Nazis first experimented with gas vans in 1940 – they locked mentally ill children inside a sealed van and choked them to death with carbon monoxide. When the extermination of the Jewish population began in 1941, victims were shot to death. However, this was not a quick or secret enough method. The Reich shifted to using gas vans for murder on a larger scale. Ultimately the vans could not handle the sheer number of Jews that the Nazis planned to exterminate.

Remember that study I told you about? There was one last question: Do you believe something like the Holocaust could happen again? More than half of Americans say yes. . .
```

---

## IC-0473: Your Loving Son

- Title: Your Loving Son
- Author (byline): Robert C. Reinhart
- Work: Telling Moments – 15 Gay Monologues
- Publisher: Applause Theater Books
- Publication date as stated: 1994
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1227
- Already set (do not supply): none

### Source block (context only)

```text
Author: Robert C. Reinhart
Book: Telling Moments – 15 Gay Monologues
ISBN: 1557831637
Publisher: Applause Theater Books
Date(Month/Year): 1994
```

### Introduction (context only: never use it for content warnings)

```text
FACT: 45% of gay males and 20% of lesbians experience physical or verbal

assault in high school; 28% of these young people feel forced to drop out of

school due to harassment based on sexual orientation.

FACT: In 1989, suicide was the leading cause of death among teen homosexuals.

But perhaps with family support these statistics can be changed. After all . . . regardless of sexual orientation, parents must realize that the child they gave birth to is still “Your Loving Son” by Robert C. Reinhart.
```

### Performance text (classify this)

```text
Dear Mom, This is the tenth time I've tried to write this. I hope I can mail this one. I don't want to cut myself off from you and Dad, and I know that if I don't write, that may happen.

I don't know what to say to your idea that I've "chosen" to be gay just to hurt you. I don't know how to answer your idea that I'm gay out of spite. I'm just gay and I am as naturally that as grass IS green.

You say that I never gave the slightest indication. I can imagine what you mean by that: I seemed normal. As you say, I was such a good boy, got pretty good grades, did fairly well in sports, though never good enough for Dad. I was a good boy, because I didn't want to draw attention to myself. I found out early that if I was quiet and went about my business, I could stay private. Being good was my way of staying secret. And I've always had secrets; especially the secret that I was gay.

I told you the truth, because I felt that I could not go on lying to you about who I really am and to give you the chance to finally know me, with no old lies between us and no new ones that needed telling, like all that stuff I told you about my dating in college or bringing some poor girl like Edith home that Christmas. I think I did her a lot of harm. She was expecting more from me and I've lost her friendship, because I used her.

You hinted in your letter that I waited to tell you I was gay till I'd graduated, so you'd keep on supporting me. The idea makes me angry and ashamed. And, to tell you the truth, I'm not sure it's not true. If that's why I waited, I didn't know it. But does that mean you wouldn't have sent me through school if you had known? I don't need your money anymore, but I do need you and Dad, need to know that I still have a place with you. It hurts like hell to think that your love for me has always been conditional. My shrink says I have a lot of work to do on that. He says that I have a responsibility for letting things get this tangled and messy. I get furious when he tells me that. I told him that if you and Dad were going to cut me out of your lives, I couldn't see any point in working on my problems with you, because you wouldn't be around. He says that whether I ever see you again or not, my relationship with you will always be there. I hear him and it makes me angry, because I can feel he's right.

You say that if I'd written to tell you I was gravely ill you could handle it better than this. Have you any idea how that makes me feel, knowing that you would rather deal with my having cancer or being in some awful disabling accident? Or crippled? But, of course, you would prefer a grave illness that didn't include AIDS?

Dead giveaway, that. As it is, I'm afraid I'm disappointingly well and likely to be happy. My God, Mom, think before you write such things.

You write that you haven't told Dad yet, because if he knew it would kill him. Why is my being gay enough to cause death? He never expected all that much of me anyway. It was you who always told me that no matter how he behaved towards me he really loved me. He never told me that.

Are you saying that my being gay is a test his unspoken love couldn't stand? If you sense some bitterness in what I say, you're right.

Now to the trip you may still be planning. Glen says he'll move out while you're here, but I don't want him to. It would be like Laura's husband moving out when you go there to visit. If Glen moved out, it would be like telling you that I was ashamed of him or that we were doing something that needed hiding. I'm proud of him and who we are. We're nice people.

You also say that you don't know how you could bring yourself to tell Laura and B.J. because they love me so much. Maybe they love me because they know. I was twelve when I told them, and I can still feel my heart hammering away when I remember trying to work up my nerve to do it. Neither of them fainted and Laura said she'd guessed and, to quote her, "So what?" B.J. had some trouble with it, his main concern being my not taking to wearing dresses or messing around with his football team. He's still uncomfortable and he tells me so, but it isn't enough to keep him from caring about his little brother or promising to beat the hell out of anybody who gives me trouble.

So, I haven't lost all of you. Maybe Laura and B.J. are the most family I can have. I know there has to be a price for demanding to be my own man in my own way. But please, Mom, think: I'm your son. I'm just not who you thought I was or who you planned on my being. But you know me in ways that no one ever will, so I pray that you'll find a way through this.

I don't mean to lecture, but I should explain what being gay means to me, because I don't want you to think that it's just a matter of sex. Sex is a part of it, but it's just the part that shows on the outside. Sure, it's all about an affinity for men in every way, but not only in the way most people think. I think God has made a special kind of man and He's given him a way of seeing and using the world that is very different from the way straight men and women see and use it. I think gay people even have special things to do in life. Because of our difference we contribute things that are special, sometimes even beautiful.

Being gay may even make me stronger, because I may have to go through life without a family I can turn to, with a lot of laws stacked against me, with employers who may not judge my work but my sex, even with churches that don't want my kind.

Well, I've said it all and I hope that I'll be able to send this one. A lot of your letter hurt like hell, so my fear is that I won't mail this and I'll just stop writing or calling. I explained to Dr. Szell that staying out of your lives might solve all our problems. He says not, but I'm not sure I believe him. Maybe I should just stay away for a while or wait till you can write me again.

And if you write, please don't close with "yours sincerely" again. Close with "your loving mother" the way you always used to.

I love you and I still need you.

(He stares at letter on his lap, picks it up and crushes it.)
```

---

## IC-0474: The Zoo Story

- Title: The Zoo Story
- Author (byline): Edward Albee
- Work: The American Dream & Zoo Story
- Publisher: Plume
- Publication date as stated: Oct 1997
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: JERRY, PETER
- Teaser before the introduction: No
- Spoken words (computed): 1804
- Already set (do not supply): none

### Source block (context only)

```text
Author: Edward Albee
Book: The American Dream & Zoo Story
ISBN: 978-0452278899
Publisher: Plume
Date (Month/Year): Oct 1997
```

### Introduction (context only: never use it for content warnings)

```text
The Zoo Story by Edward Albee is a confrontation between middle-class America and the outcasts of society. Set in central park, Peter, an average American, is confronted by Jerry, a lonely man from the wrong side of the park. Jerry tries to teach Peter the realities of life that Peter has tried to ignore. He tries to teach Peter the nature of human existence and relationships. Through a serious of failed conversations and misinterpretations of the act of love, Jerry begins his experiment to see if the middle class Americas are animals after all. The Zoo Story by Edward Albee.
```

### Performance text (classify this)

```text
JERRY: [mysteriously] Peter, do you want to know what happened at the zoo?

PETER: Ah, ha, ha. The what? Oh yes: the zoo. Oh, ho, . . . hee, hee, the parakeets getting dinner ready, and the . . .ha, ha, whatever it was, the . .

JERRY: [calmly] Yes, that was very funny, Peter. I wouldn’t have expected it. But do you want to hear about what happened at the zoo, or not?

PETER: Yes. - Yes, by all means; tell me what happened at the zoo. Oh, my. I don’t know what happened to me.

JERRY: Now I’ll let you in on what happened at the zoo; but first, I should tell you why I went to the zoo. I went to the zoo to find out more about the way people exist with animals, and the way animals exist with each other and with people too. It probably wasn’t a fair test, what with everyone separated by bars from everyone else, the animals for the most part from each other, and always the people from the animals. But if it’s a zoo, that’s the way it is. [He pokes Peter on the arm.] Move over.

PETER: [friendly]: I’m sorry, haven’t you enough room? [He shifts a little.]

JERRY: [smiling slightly]: Well, all the animals are there, and all the people are there, and it’s Sunday and all the children are there. [He pokes Peter again.] Move over.

PETER: [patiently, still friendly]: All right. [He moves some more, and Jerry has all the room he might need.]

JERRY: It’s a hot day, so all the stench is there, too, and all the balloon sellers, and all the ice cream sellers, and all the seals are barking, and all the birds are screaming. [Pokes Peter harder.] Move over!

PETER: [beginning to be annoyed]: Look here, you have more than enough room! [But he moves more, and is now fairly cramped at one end of the bench.]

JERRY: And I am there, and it’s feeding time at the lions’ house, and the lion keeper comes into the lion cage, one of the lion cages, to feed one of the lions. [Punches Peter on the arm, hard.] MOVE OVER!

PETER: [very annoyed]: I can’t move over any more, and stop hitting me. What’s the matter with you?

JERRY: Do you want to hear the story? [Punches Peter’s arm again.]

PETER: [flabbergasted]. I’m not so sure! I certainly don’t want to be punched in the arm.

JERRY: Listen to me, Peter I want this bench. You go sit on the bench over there, and if you’re good I’ll tell you the rest of the story.

PETER: [flustered]: But . . . whatever for? What is the matter with you? Besides, I see no reason why I should give up this bench. I sit on this bench almost every Sunday afternoon, in good weather. It’s secluded here; there’s never anyone sitting here, so I have it all to myself.

JERRY: I said I want this bench, and I’m going to have it. Now get over there.

PETER: People can’t have everything they want. You should know that; it’s a rule; people can have some of the things they want, but they can’t have everything.

JERRY: [laughs]: Imbecile! You’re slow-witted! [pushes Peter almost, but not quite, off the bench]: Get out of my sight.

PETER: [regaining his position]: God da . . . mn you. That’s enough! I’ve had enough of you. I will not give up this bench; you can’t have it, and that’s that. Now, go away. [Jerry snorts but does not move.] Go away, I said. [Jerry does not move.] Get away from here. If you don’t move on . . . you’re a bum . . . that’s what you are . . . If you don’t move on, I’ll get a policeman here and make you go. [Jerry laughs, stays.] I warn you, I’ll call a policeman.

JERRY: [softly]: You won’t find a policeman around here; they’re all over on the west side of the park chasing fairies down from trees or out of the bushes. That’s all they do. That’s their function. So scream your head off; it won’t do you any good.

PETER: POLICE! I warn you, I’ll have you arrested. POLICE! [Pause.] I said POLICE! [Pause.] I feel ridiculous.

JERRY: You look ridiculous: a grown man screaming for the police on a bright Sunday afternoon in the park with nobody harming you. If a policeman did fill his quota and come sludging over this way he’s probably take you in as a nut.

JERRY: Do you know how ridiculous you look now?

PETER: [his fury and self-consciousness have possessed him] It doesn’t matter. [He is almost crying.] GET AWAY FROM MY BENCH!

JERRY: Why? You have everything in the world you want; you’ve told me about your home, and your family, and your own little zoo. You have everything, and now you want this bench. Are these the things men fight for? Can you think of anything more absurd?

PETER: Absurd? Look, I’m not going to talk to you about honor, or even try to explain it to you. Besides, it isn’t a question of honor; but even if it were, you wouldn’t understand.

JERRY: [contemptuously]: You don’t even know what you’re saying, do you? This is probably the first time in your life you’ve had anything more trying to face than changing your cats’ toilet box. Stupid! Don’t you have any idea, not even the slightest, what other people need?

PETER: Oh, boy, listen to you; well, you don’t need this bench. That’s for sure.

JERRY: Yes; yes, I do.

PETER: [quivering]. I’ve come here for years; I have hours of great pleasure, great satisfaction, right here. And that’s important to a man. I’m a responsible person, and I’m a GROWNUP. This is my bench, and you have no right to take it away from me.

JERRY: Fight for it, then. Defend yourself; defend your bench.

PETER: You’ve pushed me to it. Get up and fight.

JERRY: [rises lazily]: Very well, Peter, we’ll battle for the bench, but we’re not evenly matched. [He takes out and clicks open an ugly looking knife.]

PETER: [suddenly awakening to the reality of the situation]: You are mad! You’re stark raving mad! YOU’RE GOING TO KILL ME! [But before Peter has time to think what to do, Jerry tosses the knife at Peter’s feet.]

JERRY: There you go. Pick it up. You have the knife and we’ll be more evenly matched.

PETER: [horrified]: No!

JERRY: [rushes over to Peter grabs him by the collar; Peter rises; their faces almost touch]: Now you pick up that knife and you fight with me. You fight for your self-respect; you fight for that goddamned bench.

PETER: [struggling]: No! Let . . . let go of me! He . . . Help!

JERRY: [slaps Peter on each “fight”]: You fight, you miserable bastard; fight for that bench; fight for your parakeets; fight for your cats, fight for your two daughters; fight for your wife; fight for your manhood, you pathetic little vegetable. [Spits in Peter’s face.] You couldn’t even get your wife with a male child.

PETER: [breaks away, enraged]: It’s a matter of genetics, no manhood, you . . . you monster. [He darts down, picks up the knife and backs off a little; he is breathing heavily.] I’ll give you one last chance; get out of here and leave me alone! [He holds the knife with a firm arm, but far in front of him, not to attack, but to defend.]

JERRY: [sighs heavily]. So be it! [With a rush he charges Peter and impales himself on the knife. Tableau: For just a moment, complete silence, Jerry impaled on the knife at the end of Peter’s still firm arm. Then Peter screams, pulls away, leaving the knife in Jerry. Jerry is motionless, on point. Then he, too, screams, and it must be the sound of an infuriated and fatally wounded animal. With the knife in him, he stumbles back to the bench that Peter has vacated. He crumbles there, sitting, facing Peter his eyes wide in agony, his mouth open.]

PETER: [whispering]: Oh my God, oh my God, oh my God . . . [He repeats these words man times, very rapidly.]

JERRY: [Jerry is dying; but now his expression seems to change. His features relax, and while his voice varies, sometimes wrenched with pain, for the most part he seems removed from his dying. He smiles]: Thank you, Peter. I mean that, now; thank you very much. [Peter’s mouth drops open. He cannot move; he is transfixed.] Oh, Peter, I was so afraid I’d drive you away. [He laughs as best he can.] You don’t know how afraid I was you’d go away and leave me. And now I’ll tell you what happened at the zoo. I think . . . I think this is what happened at the zoo. I think. I think that while I was at the zoo I decided that I would walk north . . . northerly, rather . . . until I found you . . . or somebody . . . and I decided that I would talk to you . . . I would tell you things . . . and things that I would tell you would . . . Well, here we are. You see? Here we are. But . . . I don’t . . . could I have planned all this? No . . . no, I couldn’t have. But I think I did. And now I’ve told you what you wanted to know, haven’t I? And now you know all about what happened at the zoo. And now you know what you’ll see in your TV, and the face I told you about . . . you remember . . . the face I told you about . . . my face, the face you see right now. Peter. . . Peter? . . . Peter . . . thank you. I came unto you [He laughs, so faintly.] and you have comforted me. Dear Peter.

PETER: [almost fainting]: Oh my God!

JERRY: You’d better go now. Somebody might come by, and you don’t want to be here when anyone comes.

PETER: [does not move, but begins to weep]: Oh my God, oh my God.

JERRY: [most faintly, now; he is very near death]: You won’t be coming back here any more, Peter; you’ve been dispossessed. You’ve lost your bench, but you’ve defended your honor. And Peter, I’ll tell you something now; you’re not really a vegetable; it’s all right, you’re an animal. You’re an animal, too. But you’d better hurry now, Peter. Hurry, you’d better go . . . see? [Jerry takes a handkerchief and with great effort and pain wipes the knife handle clean of fingerprints.] Hurry away, Peter. [Peter begins to stagger away.] Wait . . . wait Peter. Take your book . . . book. Right here . . . beside me . . . on your bench . . . my bench, rather. Come . . . take your book. [Peter starts for the book, but retreats.] Hurry . . . Peter. [Peter rushes to the bench, grabs the book, retreats.] Very good, Peter. . . very good. Now . . . hurry away. [Peter hesitates for a moment, then flees, stage left.] Hurry away . . . [His eyes are closed now.] Hurry away, your parakeets are making the dinner . . . the cats . . . are setting the table . . .

PETER: [off stage, a pitiful howl]: OH MY GOD!

JERRY: [his eyes still closed, he shakes his head and speaks; a combination of scornful mimicry and supplication]: Oh . . . my . . . God. [He is dead.]
```

---

## IC-0475: 13 Ways to Screw Up Your College Interview

- Title: 13 Ways to Screw Up Your College Interview
- Author (byline): Ian McWethy
- Work: Random Acts of Comedy: 15 Hit One-Act Plays for Student Actors, Pg 75-93
- Publisher: Playscripts, Inc.
- Publication date as stated: Aug 2011
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: INTERVIEWER 2, INTERVIEWER 1, ACTOR 2, TOGETHER, BRETT, LILY, KELLY, EVE, ELIZABETH, JASON, EMILY
- Teaser before the introduction: Yes
- Spoken words (computed): 1674
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ian McWethy
Book: Random Acts of Comedy: 15 Hit One-Act Plays for Student Actors, Pg 75-93
ISBN: 978-0981909974
Publisher: Playscripts, Inc.
Date (Month/Year): Aug 2011
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: 13 . . .
```

### Performance text (classify this)

```text
Suggested Roles:

Actor 1: Interviewer 1, Brett, Kelly, Elizabeth

Actor 2: Interviewer 2, Lily, Eve, Jason, Emily

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

(INTERVIEWER 1 is in his/her office. INTERVIEWER 2 enters, a worried look on his/her face.)

INTERVIEWER 2: (Pg 75-76) We are . . . short . . . by one student. One student!

INTERVIEWER 1: The dean really thinks one student is going to make a difference?

INTERVIEWER 2: He's convinced if we can get one more kid to enroll this year, all our financial problems will be solved.

INTERVIEWER 1: But we don't have any more interviews scheduled. When does he want our recommendation by?

INTERVIEWER 2: Today . . . Or we're fired. I think he still blames us for accepting that pyromaniac that burned down the science center.

INTERVIEWER 1: But he had an amazing essay! How were we to know? (INTERVIEWER 2 shrugs. INTERVIEWER 1 shakes his head in disgust.) Well, what are we going to do? We finished our interviews last week.

INTERVIEWER 2: Look through the wait listed files and start calling. If any of them can see us today, let's give them a shot.

INTERVIEWER 1: The wait list? Oh God.

INTERVIEWER 2: Hey, keep your head up. The wait listed kids aren't as bad as you think.

ACTOR 2: (no, make that 7)

TOGETHER: Ways to Screw Up Your College Interview by Ian McWethy

(Pg 80-81) (INTERVIEWER 2 is making notes in a file when BRETT, dressed in a suit, talking on a cellphone, comes into the room and paces around.)

BRETT: Okay, okay! I'm totally on it, I'm on it, trust me. I'm gonna push my five o'clock to six, my Tuesday to Friday, and flip another thing with a thing I got next month…

INTERVIEWER 2: Excuse me-

BRETT: Yeah, yeah, yeah, hold on. (To INTERVIEWER 2) I'II be done in a few. We're gonna have a great convo, I can feel it. (Back to the phone) Okay chief, I gotta wrap this up. I'm pumped, we're gonna blow this out of the water and blow people's minds. Manana. (He hangs up) (to Interviewer) Appreciate your patience! You're an ace in the hole. Okay! Let's do this thing.

INTERVIEWER 2: You're Brett? You're thirty minutes late.

BRETT: I know, I know, I got caught up in conference call, a nightmare lunch meeting . . . and this girl I'm dating. . . blah blah blah . . . you know.

INTERVIEWER 2: Well, I have another prospective student . . .

BRETT: I know, I know, I've got a meet and greet in a fiver so let's just bulldoze through this thing, shall we? You know what? I'm gonna take the reigns here and skip the whole "you ask questions part." So here's me: I'm a self-motivator, I'm extremely competitive, and I'm the life of the party. I like your school's aggressive economic program and its Greek social scene. Gonna pledge Alpha-Phi-Beta, or Delta-Kai-Delta . . . depending on the pledge class. My stats are well above your average so let's make this happen. If you're in the boat, I'm driving the ship. We good? (BRETT sticks his hand out for a fist bump. INTERVIEWER 2 doesn't respond. Not noticing, BRETT stands up and answers his phone.) Whattup buttercup! Yeah, I just had to do this lame face-to-face, I'm on my way. Kidding me, nailed it! It's the Brettster you're talking about here. *****Scene - INTERVIEWER 1 with LILY *****

INTERVIEWER 1: (Pg 81-83) Thanks again for coming in on such short notice.

LILY: Please, it was no trouble at all.

INTERVIEWER 1: So tell me about yourself. What subjects do you like in school, do you have any hobbies? You know stuff like that.

LILY: Hobbies? I have a few, I suppose. I used to be really into swimming but . . . I haven't . . . not since . . . that day . . . (LILY simmers with emotion.)

INTERVIEWER 1: Are you okay? We don't have to . . .

LILY: No, it's okay. . . I want to, I. . . I need to talk about it. It was a blistering summer day. it was one of the hottest days in recorded history. But swimming was my life. . . I went to the pool early, got on my swimming suit, and began my morning stretches. It was during my warm-ups that I saw him. . . a little boy, fiery red hair, freckles sprinkled across his pale white skin, teetering on the edge on the pool. Before I could even think to warn him, he tumbled into the watery abyss. His body thrashed about violently, his eyes closed shut from the sting of chlorine, his voice silenced from all the water he was swallowing. I jumped into the water and swam over as quickly as I could but . . . I was too late . . . he was . . . (LILY is overcome with emotion.) That was eight years ago and . . . I've never set foot in a pool since.

INTERVIEWER 1: Lily, that was very brave of you to share this with me. Witnessing a death like that. . . especially that of such a young child-

LILY: No, he didn't die. The lifeguard pulled him out of the water.

INTERVIEWER 1: Oh, well even seeing a near death experience-

LILY: He was only in the water a few seconds when the lifeguard pulled him out.

INTERVIEWER 1: I thought you said "it was too late"?

LILY: IT WAS TOO LATE FOR ME! I couldn't save him because . . . l was TOO . . . late . . . (LILY is overcome with emotion)

INTERVIEWER 1: (confused) So, you saw a kid fall into a pool who was almost immediately picked up by a lifeguard. This is the event that shaped your life and caused you so much emotional distress?

LILY: You weren't there! You don't know what it's like to actually . . . be there and . . . see it! *****Scene - INTERVIEWER 2 with KELLY*****

INTERVIEWER 2: (Pg 84-85) Hi, you must be Kelly. (Opening her file) So, let's see here . . . oh! You know what, we never received your college essay.

KELLY: (tightly wound, a Stepford wife-ish smile) Is that right?!?

INTERVIEWER 2: Yeah, I'm not, uh, sure what happened. Do you have a copy of it?

KELLY: Oh absolutely. I've got it right here in my bag! (She reaches into her bag, pulls out a single sheet of paper and hands it to the interviewer)

INTERVIEWER 2: That's great, thank you . . . so, uh . . . I'm sorry, this is your college essay? It's . . . this is a drawing of a girl. . . in a pink dress. (A very awkward beat.) Okay, well, let's look at your transcript shall we . . . (opens Kelly's file and is speechless.) You have no GPA?

KELLY: That's right.

INTERVIEWER 2: And you didn't take the SATs?

KELLY: Well now, how about that!

INTERVIEWER 2: According to this, you have a perfect attendance record, but have refused do any homework or take any tests. Kelly, I'm not even sure how you got to this point. You can't go to college without a GPA.

KELLY: Perhaps you'd like to see my recommendation. (KELLY hands over another paper)

INTERVIEWER 2: No, Kelly, I'm . . . there is no way any University, let alone ours, is going to- (looks at the paper) This is a picture of a cat . . . saying "meow."

KELLY: (Correcting) Me-ow. Yes. (KELLY nods and gives a big "dead behind the eyes" smile.)

INTERVIEWER 2: Well, thank you for coming, we'll be in touch.

KELLY: Alright then, you take care. (KELLY doesn't leave)

INTERVIEWER 2: Please leave, you're freaking me out. (She doesn't – just a creepy smile) *****Scene - INTERVIEWER 1 with EVE*****

EVE: (Pg 86-87) (EVE belts out the end to "Defying Gravity" from "Wicked.") NOTHING'S GONNA BRING. . . .ME. . . . . . DOOOOOWWWWWWN! (Beat)

INTERVIEWER 1: (covering his/her horror and shock) Wow, well you are obviously very talented, but . . . again, and I can't stress this enough, this IS NOT the audition for the theatre program so . . . a monologue and two songs really aren't-

EVE: (In full "Music Man" performance mode) TROUBLE, OH WE GOT TROUBLE, / RIGHT HERE IN RIVER CITY! / WITH A CAPITAL "T" / THAT RHYMES WITH "P" / AND THAT STANDS FOR POOL. . . *****Scene - INTERVIEWER 2 with ELIZABETH*****

INTERVIEWER 2: (Pg 87-88) Well your grades, recommendations all look pretty good. Is there anything else you can tell me about yourself? Something that's maybe not on the page.

ELIZABETH: Yeah, let's see . . . I never played sports in school but I've played in a number of rec leagues. Volleyball, soccer, basketball. I volunteer at a soup kitchen every month, I'm a practicing vampire, and I teach sailing during the summer at a sleep away camp. Is that what you were looking for?

INTERVIEWER 2: Yeah, definitely, um. . . I'm sorry… it sounded like you said you were a "practicing vampire."

ELIZABETH: Oh. Yes. Pretty much my whole life.

INTERVIEWER 2: Okay. So. . . you think you're a vampire?

ELIZABETH: Oh, no, no, no. I'm a practicing vampire. It's completely different. Basically, I live my life in preparation for the day when I will, hopefully, turn into a vampire. So, I sleep in a coffin, avoid garlic, eat lots of bloody meat, chew with my fangs . . . all in the hopes that one day, if I'm diligent enough . . . I will turn into a vampire.

INTERVIEWER 2: I see, uh . . . well then, uh, what are you doing here now? I mean, you shouldn't be out during the day, right?

ELIZABETH: That's a common stereotype. Vampires, just like humans, can walk freely in daylight without receiving even the slightest irritation to the skin.

INTERVIEWER 2: Elizabeth! You're not going to turn into a vampire. There's no such thing as vampires!

ELIZABETH: (extremely insulted) Wow! That may be the most offensive thing I've ever heard. Honestly, I expected more out of this university. (she storms out) *****Scene - INTERVIEWER 1 with JASON*****

JASON: (Pg 91) (in a cape and top hat, he pulls a card out of the deck) So then is THIS your card?

INTERVIEWER 1: No.

JASON: But where there's a diamond, there must be a . . . Jack of all trades. . . in clubs.

INTERVIEWER 1: Still not my card.

JASON: Darn it. I was practicing all week.

INTERVIEWER 1: Look, I'm very glad you have hobbies outside of school, but maybe we can get back to-

JASON: Oh, sure, sure, sure. After . . . you show me the card UNDERNEATH YOUR SEAT.

INTERVIEWER 1: (looks under his/her seat and picks up a playing card) "Rules on how to Play Texas Hold 'em?"

JASON: And who makes the rules, but a KING.

INTERVIEWER 1: Hey, that's actually my card.

JASON: Really?

INTERVIEWER 1: No.

JASON: Okay, okay . . . let's try this. Pick a number between one and five thousand. NO, wait, first tell me your favorite color, then pick a number. *****Scene – INTERVIEWERS CONSULT*****

INTERVIEWER 1: (Pg 92-93) (defeated) Not one?

INTERVIEWER 2: Not a single . . . one.

INTERVIEWER 1: This is bad.

INTERVIEWER 2: This is . . . extremely bad.

INTERVIEWER 1: You must have been too critical. I'm sure you saw at least one kid we could recommend.

INTERVIEWER 2: Hey, if you want to look through my files, be my guest. (INTERVIEWER 1 looks through INTERVIEWER 2's files.)

INTERVIEWER 2: Well, if you're gonna look at mine, then I'm gonna look at yours. (They read in silence for a bit.)

INTERVIEWER 1: What does "practicing vampire" mean? (INTERVIEWER 2 closes the file for him/her and shakes his/her head "no." They continue to look.) (A knock on the door. EMILY comes in.)

EMILY: Hi, my name's Emily Court. . . I have an appointment at 5?

INTERVIEWER 1: Oh my Gosh, right. Sorry, l. . . got a little sidetracked. (finds her file and as he/she looks at it a look of relief appears on his/her face) Emily, so . . . wow, nice record. Valedictorian of your class?

INTERVIEWER 2: I'm also really impressed with the variety of after school programs you've amassed. First chair cellist, president of the student council, member of the thespians, and treasurer for something called the "relief club."

EMILY: It was a club formed by me and three friends as a public outreach . . . we do shelter meals, food drives, build houses . . . there wasn't really anything like that at our school.

(INTERVIEWER 1 and INTERVIEWER 2 look at each other in glee. Finally.)

INTERVIEWER 1: Well, Emily, we should tell you that. . .

EMILY: (EMILY's phone rings. EMILY scrambles to answer it.) I'm so sorry. I never leave my phone on normally it's just . . . (She looks at the number) . . . this is my mom, I told her not to call unless it was really, really, urgent- I'm so sorry. I'll be quick. (Answering her phone) Hello? Yeah, no it's going fine. Any news? OH MY GOD! I GOT IN! I AM OFFICIALLY AN IVY LEAGUER! AAAAAHHHHH!!! (EMILY dances around, ecstatic.) And what about the Scholarship . . . ? . . . Are you kidding me! ARE YOU . . . but they hardly give out any money let alone a free ride! OH MY GOD! MOM! I'm gonna cry! (To the Interviewers) I'm sorry, I just have to . . . thank you, sorry . . . (EMILY leaves the room, screaming, jumping, etc.) (The two INTERVIEWERS sit for a moment, deflated.) (INTERVIEWER 1 looks through a file sadly.)

INTERVIEWER 1: This guy does magic.
```

---

## IC-0476: Aeonian Parallax

- Title: Aeonian Parallax
- Author (byline): Megan Mandana
- Work: Aeonian Parallax
- Publisher: SpeechGeek
- Publication date as stated: 2020
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1325
- Already set (do not supply): none

### Source block (context only)

```text
Aeonian Parallax by Megan Mandana
ISBN: 978-1-61387-120-1
Copyright 2020 by SpeechGeek.
Free performance of this play for high school and college level competitive forensics is
permitted. All other rights reserved.
This PDF version of this selection, e-published in 2020, is identical to the printed published
version of this same publication dated 2020. This statement along with the entire printed
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
Performance notes: The Overseer may be played by one or both actors. The use of music is permitted to create atmosphere, violin, and transition.

OVERSEER. The Cooperative: society perfected. When our primitive

ancestors ruled the world, they made war, famine, crime, and

selfishness. But from the ashes of governments and grief rose the

Cooperative! Members are provided healthcare, education,

employment, purpose, and belonging. At the age of sixteen

initiates earn their membership by performing a single act of

allegiance, sacrifice, and selflessness. The Cooperative: the

future is waiting to welcome you.

NOVA. Excuse me... Astrid?
ASTRID. Nova! (they embrace as old friends)
NOVA. What are you doing here? Is it time for you already?
ASTRID. Yes, six months to the day your junior. My birthday is--
NOVA. Next week! Of course, it is. How could I forget?
ASTRID. That’s alright. It’s wonderful to see you. All of this. It’s wonderful.
NOVA. I suppose.
ASTRID. Wait, why are you still here? You haven’t earned your

membership yet? NOVA. I’m still preparing.

Whether it’s today’s world or an AI-controlled futuristic dystopia, the challenges of balancing community and individuality are immense. Playwright Megan Mandana uses the alien landscape of sci-fi to cross-examine the very real struggle of growing up: what is the cost of belonging? What is the value of selfishness?

NOVA. (Nova picks up her violin again and a small smile appears as she

plays.) ASTRID. (enters) Nova! I have wonderful news. I spoke with the Overseer.

They will allow you to be my mentor. NOVA. Me? There must be a mistake, Mentors are Cooperative

members. They’ve already completed the Sacrifice. ASTRID. Yes, the Overseer agreed that our Sacrifice can happen

simultaneously. They will allow me to complete my choice early

to be with you. NOVA. Ha, “choice.” ASTRID. They... they said your preparations were longer than expected. I

told them that you were waiting for me. For this (a bracelet or

memento they share). Because we always do things together. NOVA. Astrid. What do you know about the Sacrifice? ASTRID. Oh, that’s easy! It’s at the age of sixteen. Initiates earn their

membership by performing an act of selflessness. An elective

surgery to demonstrate allegiance to the Cooperative. NOVA. Correct. The surgery was developed as a rite of passage,

whereby each initiate sacrifices a part of their primitive self. ASTRID. Which part?

NOVA. Each initiate is different. The surgery will remove what you love

most, in order to prove that you love the Cooperative more.
ASTRID. That’s the selflessness part.
NOVA. Yes.
ASTRID. How do they know what I love most?
NOVA. The assessment will test your body and mind to determine your

unique profile. Then they prepare you to make your final choice:

“Do you wish to join the Cooperative?”
ASTRID. Yes!
NOVA. You don’t have to answer yet, Astrid.
ASTRID. Oh, right. Just excited, I guess. ...Mentor.

(Transition: Astrid is put into an assessment chamber. She stands arms spread while the chamber reads her and there are sounds, lights, etc.)

OVERSEER. Assessment commencing. The Cooperative: society perfected.

10% complete. Members are provided healthcare, education,

employment, purpose, and belonging. 30% complete. At the age

of sixteen, initiates earn their membership by performing a

single act of allegiance – 50% complete – sacrifice – 65%

complete – selflessness – 80% complete. The Cooperative: the

future is waiting to welcome you. Assessment complete.

ASTRID. Well? What did the assessment reveal? What is my Sacrifice

supposed to be?
NOVA. Astrid, calm down. Your results aren’t ready yet.
ASTRID. Is it silly that I hope they change my nose?
NOVA. They take what you love, Astrid. It’s not plastic surgery.
ASTRID. But you get it back, right? I mean they replace it.
NOVA. The Sacrifice is replaced with the finest technology, your

communication uplink, your finances, your healthcare records,

and security measures. Your sacrifice will be linked to your

identity. Therefore, if you are offline for too long, the

Cooperative will assist to ensure you stay connected.
ASTRID. That’s convenient. Nova...what were your assessment results?
NOVA. My...my arm.
ASTRID. What you love most? You loved your arm the most?
NOVA. Not exactly. I love playing the violin.
ASTRID. You won’t play anymore?
NOVA. I’ll be able to execute any song I choose with my new arm. But I

won’t feel the strings, or the warm wood against my palm, I won’t

feel the vibration, but I can play any song I want.
ASTRID. So...what are you waiting for?
NOVA. Astrid, it’s complicated.
ASTRID. Nova, it’s not complicated. When we were Littles, we used to talk

about this day. Joining the Cooperative. Going to school to

become teachers or doctors. Having our own Littles. NOVA. I know. ASTRID. So make the choice.

NOVA. Choice? What choice, Astrid? Either they are going to take my

arm or I’m electing to go to live…where? The outlands? Like the

primitives!? That isn’t a choice! ASTRID. Just because you don’t like the options, does not mean there is no

choice.
NOVA. You sound just like the Overseer.
ASTRID. If you choose yourself, then you choose to be alone.
NOVA. Astrid, I’m not selfish, but I am scared.
ASTRID. Don’t think about yourself. Do it for me, Nova. For us. (references

memento again) NOVA. ...Okay.

OVERSEER. Nova A. Equis do you wish to join the Cooperative? NOVA. Yes.

ASTRID. Nova. You did it! You completed the Sacrifice. You’re part of the

Cooperative now. NOVA. Thank you, Astrid. I’m very tired. Could I ask you to… ASTRID. Yes, of course. Good night.

(Transition: Astrid leaves. Nova sits down and lets her arm rest lifeless at her side. She looks at it for a moment and then removes it again. She sets it down and massages her arm. She takes a deep breath and closes her eyes and hums softly as she “plays” the violin again without the arm. She enjoys it for a moment, humming softly as if she hears the music in her head. Astrid enters again with a question but catches Nova dreaming and playing.)

NOVA. Astrid! (quickly grabs and replaces her mechanical arm)
ASTRID. I thought you said you could still play.
NOVA. Why are you here?
ASTRID. Why did you take the arm off if you can still play?
NOVA. You said good night!
ASTRID. Can’t you play anymore?
NOVA. No. I mean, yes. Technically, the music will sound flawless. But

when I play now, it won’t sound like me.
ASTRID. …So you didn’t really get it back at all.
NOVA. It’s not much of a Sacrifice if they gave it right back.
ASTRID. That’s why you took so long to prepare? Because you knew…
NOVA. …I suspected.
ASTRID. Why wouldn’t you tell me that? Why wouldn’t you tell me that you

would regret it?! NOVA. You told me not to think about myself. You told me to do it for you

– for us.
ASTRID. Well none of that even matters now!
NOVA. What?
ASTRID. I got my assessment results. And it’s you.
NOVA. What?
ASTRID. My Sacrifice to join the Cooperative is my love for you.
NOVA. How would they even…?

ASTRID. I won’t remember you. I won’t remember this. (holds up the

memento) NOVA. You lose us so you can be part of the Collective?! What kind of a

choice is that? ASTRID. Just because I don’t like the options does not mean there is no

choice. NOVA. To hell with this! (removes her arm quickly and smashes it on the

ground) ASTRID. The security measures! NOVA. Astrid, every choice has a consequence, and you have to decide

what it is worth to you. ASTRID. What are you doing? NOVA. I am your Mentor, remember? This is me preparing you! You

don’t have to do this. ASTRID. But what about— NOVA. You choose, Astrid! Don’t do this for me. Don’t do this for them.

Do what is right for you. Astrid!? (she is dragged away) ASTRID. Nova! OVERSEER. Astrid J. Davis. Do you wish to belong to the Cooperative? ASTRID. I…don’t know. I’m scared. OVERSEER. Astrid J. Davis. You must make your choice. ASTRID. Healthcare, education, employment... I’ve wanted this since I was

a little. But what good is it without Nova?
OVERSEER. Astrid J. Davis. Do you wish to belong to the Cooperative?
ASTRID. I don’t want to be alone!
OVERSEER. Astrid J. Davis. Your choice is made.

(Transition: Astrid enters. Nova is there, she sees her and approaches cautiously)

NOVA. Astrid? ASTRID. ...Yes?

END
```

---

## IC-0477: All 7 Deadly Sins Committed at a Church Bake Sale

- Title: All 7 Deadly Sins Committed at a Church Bake Sale
- Author (byline): The Onion Staff
- Work: The Norton Sampler: Short Essays for Composition, 6th Ed – Pg 101-05
- Publisher: W.W. Norton
- Publication date as stated: 2003
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 1, ACTOR 2, REPORTER, CONNIE BARRETT, BETTY WICKS, GEORGIA BRANDT, PENNY COX, JILLY BRANDON, BETH ELLEN COYLE
- Teaser before the introduction: Yes
- Spoken words (computed): 830
- Already set (do not supply): none

### Source block (context only)

```text
Author: The Onion Staff
Book: The Norton Sampler: Short Essays for Composition, 6th Ed – Pg 101-05
ISBN: 978-0393978827
Publisher: W.W. Norton
Date (Month/Year): 2003
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: No one is safe . . . Anywhere (Evil laughter) TOGETHER: All Seven Deadly Sins Committed At a Church Bake Sale by The Onion Staff
```

### Performance text (classify this)

```text
NOTE: This cutting asks one student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested roles: Actor 1: Reporter Actor 2: All other roles

ACTOR 1: The Onion is a satirical newspaper that originated in Madison, Wisconsin.

ACTOR 2: In a typical issue, the paper pokes fun at everything from Politics

ACTOR 1: “Poll Finds Most Americans Would Swap Democracy for $100 Best Buy Gift Card” *

(Original text reads “Bush Extremely Proud of New Suit”)

ACTOR 2: to Entertainment . . .

ACTOR 1: “NRA Accuses ‘Rust’ Producers of Endangering Crew by Not Giving Everyone Guns” *

(Original text reads American lifestyles “TV Helps Build Valuable Looking Skills”)

ACTOR 2: from The Environment . . .

ACTOR 1: “Climate Summit sets Ambitious Goal to Phase Out Fossil Fuels by the Time the Earth Runs Out of Them.” *

(Original text reads Medicine “Colonoscopy Offers Non-Fantastic Voyage through Human Body”)

ACTOR 2: to Religion, which is what this selection is about . . .

ACTOR 1: Sort of . . . [See] According to the Catholic Church, there are basically two types of sins

ACTOR 2: “Venial” ones that are easily forgiven and “deadly” ones that well, are not.

ACTOR 1: Pride

ACTOR 2: Envy

ACTOR 1: Wrath

ACTOR 2: Sloth

ACTOR 1: Avarice (or Greed)

ACTOR 2: Gluttony

ACTOR 1: and Lust.

ACTOR 2: The Seven Deadlies . . .

ACTOR 2: And now reporting to you live from Gadsden, Alabama . . .

REPORTER: The seven deadly sins—avarice, sloth, envy, lust, gluttony, pride, and wrath—were all committed Sunday during the twice-annual bake sale at St. Mary's of the Immaculate Conception Church. Patti George (far right) commits the sin of envy as she eyes fellow parishioner Mary Hoechst's superior strawberry rhubarb pie. In total, 347 individual acts of sin were committed at the bake sale, with nearly every attendee committing at least one of the seven deadly sins as outlined by Gregory the Great in the Fifth Century.

CONNIE BARRETT: (full of pride) My cookies, cakes, and brownies are always the highlight of our church bake sales, and everyone says so. Sometimes, even I'm amazed by how well my goodies turn out.

REPORTER: Fellow parishioner Betty Wicks, who commits the sin of gluttony at every St. Mary's bake sale, as well as most Friday nights at Old Country Buffet, agreed.

BETTY WICKS: (245 lbs and committing the sin of gluttony) Every time I go past Connie's table, I just have to buy something. I simply can't help myself—it's all so delicious.

REPORTER: The popularity of Barrett's mouth-watering wares elicited the sin of envy in many of her fellow vendors.

GEORGIA BRANDT: Connie has this fantastic book of recipes her grandmother gave her, and she won't share them with anyone. This year, I made white-chocolate blondies and thought they'd be a big hit. But most people just went straight to Connie's table, got what they wanted, and left. All the while, Connie just stood there with this look of smug satisfaction on her face. It took every ounce of strength in my body to keep from going over there and really telling her off.

REPORTER: While the sins of wrath and avarice were each committed dozens of times at the event, Barrett and longtime bake sale rival Penny Cox brought them together in full force.

CONNIE BARRETT: Penny said she wanted to make a bet over whose table would make the most money. Whoever lost would have to sit in the dunk tank at the St. Mary's Summer Fun Festival. I figured it's for such a good cause, a little wager couldn't hurt. Besides, I always bring the church more money anyway, so I couldn't possibly lose.

REPORTER: Moments after agreeing to the wager, Cox became wrathful when Barrett, the bake sale's co-chair, grabbed the best table location under the pretense of having to keep the coffee machine full. Cox attempted to exact revenge by reporting an alleged Barrett misdeed to the church's priest.

PENNY COX: I mentioned to Father Mark that I've seen candles at Connie's house that I wouldn't be surprised one bit if she stole from the church's storage closet.

REPORTER: Cox also committed the sin of sloth by forcing her daughter to set up and man her booth while she gossiped with friends.

PENNY COX: Perhaps if he investigates this, by this time next year, Connie won't be co-chair of the bake sale; and in her place, we'll have someone who's willing to rotate the choice table spots.

REPORTER: The sin of lust also reared its ugly head at the bake sale, largely due to the presence of Melissa Wyckoff, a shapely 20-year-old redhead whose family recently joined the church. (Actor 2 pantomimes Wyckoff) While male attendees ogled Wyckoff, the primary object of lust for females was the personable, boyish Father Mark. Though attendees' feelings of lust for Wyckoff and O'Connor were never acted on, they did not go unnoticed. After Jilly Brandon’s husband Craig offered Wyckoff on of her Rice Krispie treats . . . to “welcome her to the parish”

JILLY BRANDON: There's something not right about that Melissa Wyckoff. She might have just moved here from California, but that red dress of hers should get her kicked out of the church.

REPORTER: According to St. Mary's treasurer Beth Ellen Coyle, informal church-sponsored events are a notorious breeding ground for the seven deadly sins.

BETH ELLEN COYLE: Bake sales, haunted houses, pancake breakfasts . . . such church events are rife with potential for sin. This year, we had to eliminate the 'Guess Your Weight' booth from the annual church carnival because the envy and pride had gotten so out of hand. Church events are about glorifying God, not violating His word. If you want to do that, you're no better than that cheap strumpet Melissa Wyckoff.
```

---

## IC-0478: All I Really Need to Know I Learned in

- Title: All I Really Need to Know I Learned in
- Author (byline): Not specified
- Work: Not specified
- Publisher: Dramatic Publishing
- Publication date as stated: Jan 1999
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: NOTE FROM THE ADAPTERS, ACTOR 1, ACTOR 2, TOGETHER
- Teaser before the introduction: Yes
- Spoken words (computed): 928
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ernest Zulia and David Caldwell (Based on books by Robert Fulghum
ISBN: 978-0871299130
Publisher: Dramatic Publishing
Date (Month/Year): Jan 1999
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Welcome to Kindergarten!

ACTOR 2: Today is an exciting day – it’s a day devoted to Fairy Tales.

ACTOR 1: And there isn’t a better fairy tale than Cinderella!

ACTOR 2: (stage whisper) Just remember . . . everything you need to know is in there somewhere

ACTOR 1: All I Really Need to Know I Learned in Kindergarten

ACTOR 2: Adapted by Ernest Zulia and David Caldwell based on books by Robert Fulghum
```

### Performance text (classify this)

```text
Kindergarten - Cinderella Adapted by Ernest Zulia and David Caldwell Based on books by Robert Fulghum

NOTE FROM THE ADAPTERS: (Pg ix – x) Originally presented by a 5-person cast. Stories, lines or songs can be reassigned. It is expected that each production will utilize the names of its own cast members in the script. This selection adapts to 2 Character presentation (Designated as Actor 1 and Actor 2) Genders are flexible

ACTOR 1: (Pg 5-6) Share.

ACTOR 2: Play fair.

ACTOR 1: Don’t hit people

ACTOR 2: Don’t take things that don’t belong to you.

ACTOR 1: If you hurt someone, say you’re sorry.

ACTOR 2: Hold hands and stick together when you cross the street.

ACTOR 1: Live a balanced life – learn some, think some, work and play.

ACTOR 2: And sing and dance and draw

ACTOR 1: Take a nap each day.

ACTOR 2: (Pg 7) Everything you need to know is in there somewhere.

ACTOR 1: (Pg 8) If we all stopped to take a nap each day, how much better our world would be?

ACTOR 2: And it’s still true, when we go out into the world in these uncertain times, it doesn’t matter if you’re six years old or sixty – we should all hold hands and stick together.

ACTOR 1: (Pg 9-15) Cinderella was the title on the chalkboard marquee.

ACTOR 2: Given the task of dramatizing a fairy tale for a teacher’s conference, the kindergarten class decided on the classic old rags-to-riches story, “Cinderella.”

ACTOR 1: You know how it goes: “Shy agreeable protagonist, victimized by abusive step-parent, waits for wise matriarchal figure to rescue here, and deliver her transformed from co-dependency to bliss.”

ACTOR 2: In other words; if you’re good-looking, good at heart and have a fairy godmother . . . you got it made.

ACTOR 1: It was a good choice from the teacher’s point of view, because there were so many characters and every child in the class could be in the play.

ACTOR 2: There was the absolutely ravishing Cinderella

ACTOR 1: The evil stepmother.

ACTOR 2: The two wicked but stupid stepsisters

ACTOR 1: The beautiful and wise fairy godmother

ACTOR 2: The pumpkin, mice, coachmen, horses, king

ACTOR 1: All the people at the King’s ball

ACTOR 2: And of course, (strikes a cocky pose) the Prince.

ACTOR 1: The children were allowed to choose roles for themselves. Finally, every child had a part.

ACTOR 2: Except one. One small boy. Who had remained quiet and disengaged from the selection process. Norman. A kid who was somehow different – not weird, just different – in the way he/she looked at things. Norman was always thinking. And like so many misunderstood, but great thinkers, Norman was teased a lot by his classmates, causing him to live on the fringe of kindergarten society. (during these lines the actor transforms into Norman a deeply earnest and serious individual)

ACTOR 1: (as the teacher) Well, Norman what are you going to be?

ACTOR 2: (as Norman) Well, I am going to be the pig.

ACTOR 1: (as the teacher) Pig? There is no pig in the story of Cinderella.

ACTOR 2: (as Norman) (after a long pause, matter-of-factly) Well . . . There is now.

ACTOR 1: Norman did not relate to being a footman or a mouse of a pumpkin.

ACTOR 2: He knew his character. Pig

ACTOR 1: And he intended to participate wherever pigs fit into the scheme of things. Without giving up dignity or identity. He took it for granted that there was a place for pigs, and that the teacher would know that.

ACTOR 2: What do you say to a kid who is already thinking up a costume of pink long underwear, pipe-cleaner tail, and a paper cup for a nose?

ACTOR 1: (knowing this is the real question) And what do you say to all the pigs? All those who are different and who do not accept the available boxes and pigeonholes?

ACTOR 2: What did the teacher say? (teacher is thinking very hard) Well, sometimes teacher talk more like fairy godmothers!

ACTOR 1: (as the teacher, waiving her own invisible magic wand) So be it!

ACTOR 2: And since there was nothing in the script explaining what the pig was supposed to do, the action was left up to Norman.

ACTOR 1: Norman gave himself one of the all-time best walk-on parts in the history of children’s theatre.

ACTOR 2: He decided he was Cinderella’s “personal pig” (pause) Where she went . . . he went.

ACTOR 1: He made no sound. (Actor 2 as Norman acts out the following narration) He simply sat on his back haunches and observed. The expressions on his face reflected the details of the dramatic action. Worried (Norman responds with intense facial expressions for each emotion) Sad . . . Hopeful . . . Puzzled . . . Mad . . . as the moment required.

ACTOR 2: There was no doubt what was going on, and no doubt that it was important.

ACTOR 1: One look at the pig and you know. The pig was so earnest. So sincere. So very . . . “there.”

ACTOR 2: Norman created such dramatic tension that people who knew how this story was supposed to end began to have doubts.

ACTOR 1: When the Prince finally placed the glass slipper on Cinderella’s foot and the ecstatic couple rode off to live happily ever after, Norman finally made his move. (Norman explodes into a spontaneous dance of joy with reckless abandon) He went wild with joy, dancing around the stage on his back feet . . . (Norman barks wildly, ending with a long howl) (when he stops, pause, then) . . . and barking like a dog??

ACTOR 1: (as teacher to Norman) Even if there was a pig in the Cinderella story, there is no such thing as a dancing, barking pig.

ACTOR 2: (as Norman – matter-of-factly) Well, there is now. (He holds his ground as the teacher contemplates this statement)

ACTOR 1: (as teacher) (considers Norman with respect) It’s true, Norman, it’s true . . . Knock ‘em dead, pig!

ACTOR 2: The presentation at the teachers’ conference was a smash hit! (Pops into the Norman character and dances in slow motion)

ACTOR 1: When Norman danced his dance, the crowd of weary teachers laughed . . . and wept . . . and cheered (both actors cheer) And later when the pig stumbled out for his curtain call.

(Norman crosses for his bow) (both actors start to chant NORMAN . . NORMAN . . . NORMAN)

ACTOR 2: The teachers were able to see that the real Cinderella was not the little girl with the button nose and blonde hair . . . but Norman, the dancing, barking pig.

ACTOR 1: And they knew the real fairy godmother was not the child waiving her fairy wand, but the teacher, standing weeping in the wings.

ACTOR 2: Kindergarten teachers know magic when they see it.

ACTOR 1: (as an epilogue) Well, the kindergarten class had many invitations to perform their highly acclaimed production of “Cinderella.”

ACTOR 2: Sometimes the teacher would have to explain what it was about the performance that was so unique.

ACTOR 1: (as the teacher) It has a pig in it, you see . . . the star of the show is a dancing, barking pig.

ACTOR 2: But there is no dancing, barking pig in “Cinderella.”

TOGETHER: Well, there is now! (Both break into Norman’s unique dance and end with a bark and howl)
```

---

## IC-0479: Ant Farm: And Other Desperate Situations

- Title: Ant Farm: And Other Desperate Situations
- Author (byline): Simon Rich
- Work: Not specified
- Publisher: Random House Trade Paperbacks
- Publication date as stated: April 2007
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 1, ACTOR 2, JUDGE, CRIMINAL, VICTIM, ME, JAKE, UNICEF, SERVANT, TEACHER, TEACHER 2, TEACHER 3, CHILD 1, CHILD 2, MR. BENDER, JONATHAN, SEYMOUR, SETH
- Teaser before the introduction: Yes
- Spoken words (computed): 1747
- Already set (do not supply): none

### Source block (context only)

```text
Author: Simon Rich
ISBN: 978-1400065882
Publisher: Random House Trade Paperbacks
Date (Month/Year): April 2007
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Let’s face it . . . no matter how many times teachers or parents tell you that school is preparing you for “real life” . . .

ACTOR 2: School is nothing like real life.

ACTOR 1: But just to prove our point, we’d like to take you for a walk down memory lane,

ACTOR 2: Compliments of Simon Rich in this selection -- Ant Farm and Other Desperate Situations
```

### Performance text (classify this)

```text
Suggested Roles: Actors should take turns announcing the title of each “scene” in a broad announcer’s voice!

ACTOR 1: Judge, Me. UNICEF, Teacher 2, Child 1; Jonathan, Seymour, Seth

ACTOR 2: Criminal, Victim, Jake, Servant, Teacher 1, Teacher 3; Child 2, Mr. Bender

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

IF LIFE WERE LIKE MIDDLE SCHOOL (Pg 25)

JUDGE: In all my years on the bench, I have never seen a more despicable criminal. You robbed, assaulted, and tortured the victim simply for the thrill of it. Do you have anything to say in your defense before I sentence you?

CRIMINAL: Nope.

JUDGE: In that case, I hereby sentence you to forty years in a maximum-security prison. I also sentence the victim to forty years in prison.

VICTIM: Wait-what? That doesn't make any sense! He attacked me!

JUDGE: I don't care who started it.

SECOND GRADE REALIZATION (Pg 7-8)

ME: Jake, come over here for a second. I need to talk to you about something.

JAKE: What's up?

ME: This is going to sound a little crazy. Oh well ... here goes. Do you remember when we were on the school bus last week and Ms. Higgins taught us that new game?

JAKE: You mean the Silent Game? Yeah, I remember. It was pretty cool of her to let us play games on the bus, huh?

ME: Well, yeah, that's what I thought at first. But then I started thinking about it. And now I'm not so sure.

JAKE: What do you mean?

ME: Well, just think about it. The Silent Game isn't actually fun. We don't do anything-we just kind of sit there. And nobody ever wins. It's always a tie.

JAKE: What are you saying?

ME: I don't think it's a real game. I think she just made it up to get us to be quiet.

JAKE: Oh my God. I think you're right.

ME: I can't believe we fell for it. We were silent for almost twenty minutes!

JAKE: We have to tell the class!

ME: What's the point? They'd never believe us.

JAKE: What about all the other games she taught us? The Politeness Game . . . the Respect Game . . . the Clean Up the Tables Game . . .

ME: What about them?

JAKE: Those might be fake too.

ME: Whoa. You just blew my mind.

JAKE: This has got to be the craziest day of my life. A DAY AT UNICEF HEADQUARTERS AS I IMAGINED IT IN THIRD GRADE (Pg 9-10) [UNICEF sits on a throne. He is wearing a cape and holding a scepter. A servant enters on his knees.]

UNICEF: Halloween is fast approaching! Have the third graders been given their little orange boxes?

SERVANT: Yes, your majesty!

UNICEF: Perfect. Did you tell them what the money was for?

SERVANT: No, sir, of course not! We just gave them the boxes and told them to collect for UNICEF. We said it was for "a good cause," but we didn't get any more specific than that.

UNICEF: Ha ha hal Those fools! Soon I will have all the money in the world. For I am UNICEF, evil king of Halloween!

SERVANT: Sir . . . don't you think you've stolen enough from the children? Maybe you should let them keep the money this year?

UNICEF: Never! The children shall toil forever to serve my greed! [UNICEF tears open a little orange box and rubs the coins all over his fat stomach.] Yes! Oh, yes!

SERVANT: Wait-your majesty! Look at this! Our records indicate that there's a kid out there- Simon-who's planning to keep his UNICEF money this year.

UNICEF: What?!? But what about my evil plans? I was going to give that money to the Russians so they could build a bomb!

SERVANT: I guess there's still one hero left in this world.

UNICEF: Noooo! [Runs out of castle, sobbing.]

SERVANT: Thank God Simon is keeping his UNICEF money. I STILL REMEMBER THE DAY I GOT MY FIRST CALCULATOR (Pg 11-12)

TEACHER: All right, children, welcome to fourth grade math. Everybody take a calculator out of the bin.

ME: What are these?

TEACHER: From now on we'll be using calculators.

ME: What do these things do?

TEACHER: Simple operations, like multiplication and division.

ME: You mean this device just . . . does them? By itself?

TEACHER: Yes. You enter in the problem and press equal.

ME: You . . . you knew about this machine all along, didn't you? This whole time, while we were going through this . . . this charade with the pencils and the line paper and the stupid multiplication tables! . . . I'm sorry for shouting . . . It's just . . . I'm a little blown away.

TEACHER: Okay, everyone, today we're going to go over some word problems.

ME: What the hell else do you have back there? A magical pen that writes book reports by itself? Some kind of automatic social studies worksheet that . . . that fills itself out? What the hell is going on?

TEACHER: If a farmer farms five acres of land a day

ME: So that's it, then. The past three years have been a total farce. All this time I've been thinking, "Well, this is pretty hard and frustrating but I guess these are useful skills to have." Meanwhile, there was a whole bin of these things in your desk. We could have jumped straight to graphing. Unless, of course, there's some kind of graphing calculator!

TEACHER: There is. You get one in ninth grade.

ME: Is this . . . Am I on TV? Is this a prank show? OUR THOUGHTS ARE WITH YOU (Pg 15-17) [Teachers writing a note home to a parent]

TEACHER 2: Dear Mrs. Matthews, I am writing to express my deepest sympathies. I shared your last note with Caleb's classmates and they made a card (which I have enclosed). Ten funerals in three weeks is a lot to ask of any child, let alone a child like Caleb, who has already suffered so many family deaths this month. At first, as humiliating as it is to admit, I thought your son had forged the notes. But denial quickly gave way to grief. I understand he has another funeral to attend on Wednesday and that it will last until Friday. Please let him know that he can take as much time off as he needs.

TEACHER 3: I would volunteer to drop off Caleb's homework myself, but I understand that your house recently exploded. Of all the tragedies that have befallen your family, this one saddened me the most. For a house to suddenly explode, without warning, destroying a child's backpack and books, is very upsetting, particularly in the midst of your High Voodoo Holidays.

TEACHER 2: I was also deeply saddened to learn that your son had suffered brain damage and could no longer complete his social studies assignments. To be hit with such a misfortune, on top of Tourette's, is a blow to any child's self-esteem.

TEACHER 3: Incidentally, I understand that Caleb has recently taken on some serious community service projects. I totally understand Caleb's devotion to the blind, particularly in light of his own blindness. But I'm worried that his extracurricular activities might interfere with his schoolwork, especially on top of the pressures of his upcoming Voodoo Bar Mitzvah. Of course, it's your decision.

TEACHER 2: I would also like to take this opportunity to congratulate you on your son's recent achievement! To be named an FBI super-spy at such a young age is an amazing accomplishment, particularly for a child who suffers from so many varied forms of brain damage. He hasn't told me much about his mission, but from what I gather it sounds like an incredible opportunity. I'm going to miss his presence in the classroom next year, but it would be selfish of me to stand in his way. Caleb's country needs him more than I do. He belongs in Russia.

TEACHER 3: Rest assured: I haven't told anyone about Caleb's mission, not even the principal. I am honored that Caleb felt he could trust me with top secret information, and I would never betray that trust. WHAT GOES THROUGH MY MIND WHEN I’M HOME ALONE (Pg 36-27) (From My Mom’s Perspective)

CHILD 1: Hmm, Mom left me home alone. Better go through the medicine cabinet and drink all the medicine for no reason. Wait, what's this? A note telling me not to "drink any medicines"? Thank God! I was about to do that. I was about to drink all the medicines.

CHILD 2: Well, I better use the stove and then not turn it off. That way, I'll burn down the house and kill myself. Wait a minute. There's a note that says I should "turn off the stove after using it." [WOW], that never would have occurred to me! Mom saved my life again, twice in one night.

CHILD 1: Well, better throw things out the window, something I haven't done since I was seven. I'm fifteen years old, but I haven't matured at all. I still need to be reminded constantly about how to get through the day. What? A note? Guess I shouldn't "throw objects out the window" after all. There go my big plans.

CHILD 2: Ah . . . dinnertime. There's a Tupperware container full of pasta in the fridge, but it's cold! How will I ever heat it up? I guess I'll just starve and die because I'm not competent enough to warm pasta. Whoa! A note telling me to put the container in the microwave and press EASY MINUTE! Thanks, note! You saved my life.

CHILD 1: I hope that when my mom comes home she asks me some very specific, humiliating questions about my changing body. SEX ED (Pg 44-45)

MR. BENDER: Okay class, now it's time to read one of your anonymous sex questions out loud. Here's one . . .

JONATHAN: Hey, Seymour, did you write that one? That looks like your handwriting.

SEYMOUR: Mr. Bender! Don't read it!

MR. BENDER: Please, no talking. It's very important that I answer this question. Whoever asked it is obviously incredibly confused about sex. These are not normal concerns. Not even close.

SETH: Hey, I bet that's Seymour's question. It's written in blue ink like all his homework assignments.

SEYMOUR: Oh, no!

MR. BENDER: Okay, let's see ... it's a seven-part question. The first part is about testicles.

SEYMOUR: Oh my God!

MR. BENDER: Quiet, class. We have to be fair to the boy who wrote this, even if we find his sexual desires morally reprehensible.

JONATHAN: Hey, I think that's Seymour's stationery. I can tell because of the watermark.

MR. BENDER: All right. I'm going to read the question now. But I have to warn you: It's pretty hard to take. If you feel like screaming, that's understandable. I'm probably going to do some screaming myself. It's that extreme. (Bell rings.)

SEYMOUR: That's the bell! Class dismissed!

MR. BENDER: Stay in your seats, everyone. If I don't answer this student's question, he could permanently damage his body. Okay. . . here it goes. . . [WOW}, I can't read this out loud, it's too humiliating. Can I have a volunteer?

SEYMOUR: I'll read it! . . . Great! Um . . .okay . . . it says . . . What do you do if you are a . . . normal boy . . . with no really weird things.
```

---

## IC-0480: Around the World in a Bad Mood!

- Title: Around the World in a Bad Mood!
- Author (byline): Rene Foss
- Work: Not specified
- Publisher: Hyperion Press
- Publication date as stated: March 2002
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: FA 1, FA 2, TOGETHER, WIRT, CAPTAIN, PASSENGER
- Teaser before the introduction: Yes
- Spoken words (computed): 1504
- Already set (do not supply): none

### Source block (context only)

```text
Author: Rene Foss
ISBN: 978-0786890118
Publisher: Hyperion Press
Date (Month/Year): March 2002
```

### Introduction (context only: never use it for content warnings)

```text
Actress 1: Around the World in a Bad Mood! Confessions of a Flight Attendant Actress 2: by Rene Foss
```

### Performance text (classify this)

```text
Suggested Roles

Actress 1: Flight Attendant (FA) 1, Captain

Actress 2: Flight Attendant (FA) 2, WIRT, Passenger(s) – create a new character for each line

NOTE: This cutting asks one student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

NOTE: Words appearing in [ ] are added as transitional items.

FA 1: Good morning, ladies and gentlemen! In a few moments we'll begin the breakfast service in the main cabin.

FA 2: We have a wide selection of choices for you today. You may have any or all of the following items: Prozac, Zoloft, Viagra, Ecstasy, Ritalin, Celebrex, or scrambled eggs.

FA 1: Some of these items may cause side effects, such as dry mouth, fatigue, internal bleeding, temporary blindness; and leprosy.

FA 2: Again, your choices include Prozac, Zoloft, Viagra, Ecstasy, Ritalin . . . oh, one moment please. My apologies, ladies and gentlemen, that is the flight attendants' breakfast menu.

TOGETHER: I am a flight attendant

FA 1: And the world is my oyster. And what an oyster it is!

FA 2: Oversold flights, weather delays, air traffic control delays, center seats, crappy food, air rage - it's so glamorous!

FA 1: Kind of like a Greyhound bus in the sky.

TOGETHER: This is just a glimpse into my life . . .

FA 2: A story about air travel and flight attendants!

FA 1: So . . . fasten your seat belts, raise your tray table, and stow your bag . . . The journey is about to begin.

TOGETHER: Welcome to my nightmare!

*WIRT – What I’m Really Thinking

FA 1: Welcome aboard, sir, so glad you could join us today. You have seat 4B. Get you a gin and tonic? My pleasure.

WIRT: Pleasure, my a**. I'd rather watch paint dry.

FA 1: Here you go, sir. Oh, you couldn't find room for your carryon? You're tired of lifting it and you want someone to get it out of your way?

WIRT: And I guess I'm the lucky someone. I cannot believe my good fortune. Jesus, what has he got in here? A dead body? If this six-foot, 200-pound bruiser can't lift it, how does he possibly think I can lift it?

FA 1: You know, sir, I think this bag is a little big for the overhead. Perhaps I could check it to your final destination?

WIRT: Better yet, perhaps I could check you to your final destination and put the bag in your seat. The bag would probably be a lot more interesting.

FA 1: Unacceptable, you say?

WIRT: I'll tell you what's unacceptable: your personality! He probably thinks just because he's sitting in first class that he's entitled to be rude to everyone in the world. Well, I'm checking this bag, whether Mr. Congeniality likes it or not. (begins dragging it up the aisle)

FA 1: Oh, I didn't mean to disturb you . . . Yes, the only available option is to check it. It sort of exceeds the size requirements.

WIRT: A little bit like your ego, pal. Oh boy, he's getting up now. Well, that got him into action! Probably hasn't moved that fast in years. My, my, look at those muscles .... Amazing how he can heave that two-ton bag into the overhead. Just 2 minutes ago he didn't have the strength.

FA 1: Thanks so much for helping with your bag. I'm glad we didn't have to check it . . . My name?

WIRT: My name . . . what does he want my name for? It's not like we're going to be buddies. In fact, if things work out the way I am hoping, we will never see each other again. So why on God's green earth does he need to know my name? He's probably going to write me up. (outraged) I'm just doing my job, risking my chiropractic good health trying to help this brute with his bag. And what do I get? This idiot requesting my name. Maybe I'll just make up a name . . .

FA 1: Oh no, you don't need to apologize. I'm sure you've had a hard day and having to tow that heavy bag of yours around has got to be tiring. . . .

WIRT: I'll give you a hard day ... my day! Five stops between Chicago and Indianapolis, airplanes of people just like this jack***. And I've got to do the same thing tomorrow and the next day, too. What did I ever do to deserve this? God, I hate my life!

FA 1: Tonight? Well, I'm flattered . . . Oh yes, I'm sure there's a lot of great nightlife, but I really have to get to bed early tonight because I have to wake up at 7:00 A.M. Oh, aren't you funny, you won't take no for an answer. . .

WIRT: Oh, he's funny all right. Funny as a crutch.

FA 1: . . . I guess as long as I'm back by a reasonable hour -- why not? I accept, sir. Charlie? OK, Charlie. I'm really looking forward to it.

WIRT: I'm looking forward to it about as much as I'm looking forward to paying my taxes or getting a root canal.

FA 1: I'll be right back! *******

FA 2: And there you are . . . curled up in a little ball, sucking your thumb, on the verge of uncontrollable sobbing, when the captain makes an announcement.

CAPTAIN: Ladies and gentlemen, I have some bad news: It appears we will be here for at least another hour. Please let us know if there’s anything we can do to make you more comfortable. Thank you.” . . . .

TOGETHER: [ARGGHHHH!] *******

FA 1: TESTING, ONE-TWO-THREE . . . hello? Is this thing on? Oh, for Christ's sake OK. Welcome aboard We Apologize for This Inconvenience Airlines, also known as WAFTI.

FA 2: This flight is under the command of Captain Booze, assisted by First Officer Chance, and as we like to say here at WAFTI, if Booze and Chance can't get ya there . . . nothing can!

FA 1: For your comfort we have four lavatories on this aircraft: one in first class and three in coach. However, only one is working, so pace yourself!

FA 2: The airphones are not working, we have only three pillows and two blankets. We do not have any magazines or newspapers, but we do have the pamphlet How to Deal with Anger in a Positive Non-violent Way. Today we will be passing these pamphlets out in lieu of the meals.

FA 1: We here at WAFTI appreciate your business and we want you to know that we're constantly upping our standards . . .

TOGETHER: So up yours!

FA 2: Now it is time for the safety demonstration. This information could save your life so
please pay attention! It's time for the 'Safety Demo Shuffle.' (Attendants rap and move to
the beat, the more awkward the better . . . with enthusiasm! – Should be said in unison or
alternating sections)
SAFETY DEMO SHUFFLE
If you've never traveled by car
this is your seat belt, please know where they are.
To fasten the belt, just pull till it's tight
and don't let go till the end of the flight!
This is for safety, especially yours,
pay close attention as we point out the doors,
please keep in mind this aircraft has eight,
they all have slides and we hope they inflate.
If we have to get out, there won't be much time,
so head for the door and follow in line,
should the cabin lose pressure, place this mask on your nose,
if the plane's going down, just reach for your toes,
if we have a water evacuation,
use your tushy cushion for your flotation,
pull up and remove, then hold to your chest,
dive in the water, and hope for the best!
A few more reminders, then off on our way:
No smoking, no cell phones, no meals today!
Thank you for flying, we're glad to arrive.
If you want to get there faster,
if you want to get there sooner,
if you just want to get there
why don't you drive???
We dooooooo!!!!!
********

FA 1: Hello, can I get you a beverage?

PASSENGER: Yes, I'll have a can of tomato juice, a bottle of water, and two cups of coffee with cream and sugar.

FA 1: Are you ordering for the whole row?

PASSENGER: No, just for me . . . I'm kind of thirsty.

FA 1: Anything else?

PASSENGER: Yeah, now that you mention it, I'll have a can of apple juice for later.

FA 1: Airline food has been the butt of many jokes over the years.

FA 2: People make fun of its quality, color, taste (or lack thereof), but as soon as you take it away people miss it!

FA 1: People used to complain about the food choices we offered

PASSENGER: All you have are three choices?! And all of them terrible! My God, what is the world coming to?

FA 1: Then as we incurred some cutbacks and started giving everyone the same meal, people were downright appalled:

PASSENGER: You mean everyone is getting the chicken? This is horrifying, I can't believe I don't have a choice!

FA 1: But, you do have a choice: eat or don't.

FA 2: Now, as cost-cutting measures continue, we have not only eliminated choice, but on certain flights we've eliminated the meal service altogether.

FA 1: Airlines are in the transportation business, not the restaurant business!

FA 1: As a passenger you are paying for transport from here to there, not for the bologna sandwich that we throw in your face.

FA 2: When the airline tells you they'll be serving a five-course meal, it means an apple, a granola bar, cheese, crackers, and a mint in a paper bag . . . and . . .

FA 1: Flight attendants, just like waiters, are the last ones to touch your food or beverage before you consume it. Keep this in mind at all times and bon appetit!

TOGETHER: [And finally the flight is over]

FA 1: We here at WAFTI appreciate your business and want you to know that we're constantly upping our standards . . .

TOGETHER: So up yours! [Buh bye!]
```
