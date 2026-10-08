# Classification request: batch 26 of 63 (40 records, IC-1001 to IC-1040)

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

## IC-1001: Good Boys

- Title: Good Boys
- Author (byline): Jane Martin
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: Jan 2003
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 1, THOMAS, JAMES, MARCUS, ETHAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1454
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jane Martin
ISBN: 978-0573628580
Publisher: Samuel French, Inc.
Date (Month/Year): Jan 2003
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 2: Two fathers: each struggling to deal with a deeply disturbing chapter in their lives –

ACTOR 1: The school shooting in which both their sons, Marcus and Ethan, died

ACTOR 2: One a victim and the other the shooter.

ACTOR 1: This selection explores the pressures of modern family life and the breaking points of men and boys.

ACTOR 2: And it raises 2 questions:

ACTOR 1: 1) To what extent are parents responsible for their children's behavior?

ACTOR 2: And 2) Is forgiveness an event or a process?

TOGETHER: Good Boys by Jane Martin
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

ACTOR 1: James, Father of Ethan and Ethan

ACTOR 1: Thomas, Father of Marcus and Marcus

(James is in the park, standing and muttering to himself. He swigs from a flask and moves to a park bench, still talking to himself. We can’t discern what he is saying. He sits. Thomas enters quietly, unassumingly. He surveys the park and finds James on the park bench. It is obvious he knows James will be here. He approaches and gestures for James to share the bench. James does, still wrapped up in his flask and internal thoughts)

THOMAS: (Pg 14) (Beat) Sir, I’m Thomas Thurman, Mr. Erskine. (James turns his head to look at him, caught between conflicting impulses. He rises to leave, then sits again, then rises again to leave) Please talk to me, sir.

JAMES: (Pg 15-16) (James turns harshly, obviously distraught) I don’t talk about that, Mr. Thurman. I’m through talking about that. I’m finished with it! (He starts to go)

THOMAS: (Staying calm) You’d just walk off on me?

JAMES: Dammit! I have to get on the other side of this. I would think you would want to get on the other side of it. There has to be an end to it! (Again turns to leave)

THOMAS: I have a picture of your son . . . (James hesitates) . . . in the school. (Thomas holds out a snapshot)

JAMES: What? (Shift of energy from angry to broken . . . pause) When he was alive? (James takes the picture, looks at it and begins to breakdown) (Pg 29) Is that your son lying on the floor? (Thomas nods and turns away in grief)

THOMAS: (Pg 17) When he was alive. (James does not take the picture)

JAMES: (A moment) You didn’t just run across me in the park.

THOMAS: No, sir. I sought you out. (Pg 19) I am a pastor, Mr. Erskine. (Pg 17) I’m just working on it the best I can. (A pause) And, painful as every part of it is, it seems like I feel some better the more I know . . .

JAMES: Well, that would not be my experience. There isn’t any more I need to know.

THOMAS: (Pg 19) Beg your pardon, but I see here you’re drinkin’ in the middle of the day. I know something about that. Oh, yes. I notice you cannot bear to hear about that day. There was a long time there . . . a long time . . . it made me physically sick to hear it. We are brothers on that score. (beat) (Pg 33) I came here to ask you to come and ask forgiveness in my church.

JAMES: (Pg 35) Goddamnit!

THOMAS: I would ask that you not take the Lord’s name in vain.

JAMES: He was a good boy. You understand that? (Ticking them off) Plays well with others. Imaginative, articulate. Liked by teachers. Straight A student until ninth grade. Untrustworthy? On the small stuff. A pain in the ass? Absolutely. I didn’t raise a shooter, do you understand that? I do not need to stand up in front of your church and be forgiven. (Belligerent) I’ll tell you what, Thomas. My son Ethan killed your boy. (Pg 34) He shot nine children. Four young women. Two standing as close as I am to you. FLASHBACK to Ethan and Marcus (altercation at school)

MARCUS: (Pg 23) (enters and sees Ethan) Hey! What are you doin’, yo, yellin’ stuff when I’m talking to my ladies. Yo, tell you what. Yell some more shit, I’m here to hear it.

ETHAN: Don’t be sayin.’ You talking about yelling across the lunchroom? Did I want to come and suck it?

MARCUS: I didn’t yell it, man, I walked over and said it to you. You think I’m blind, man? I don’t see those signs you hold up at the game? “Don’t feed the animals,” that shit. Look at you. You embarrass the school man.

ETHAN: (Furious) What the hell are you talking about, moron? You’re coming over me when you’re got up in your artificial, phony-ass, imitation LA “gangsta-drag?”

MARCUS: (Physically assaulting Ethan – he takes him to the ground) You know what’s on the ground now, sucker?

ETHAN: (Fighting to get loose, which he does and steps back) Hey, you touch me. You lay one finger on me, I’ll see you in the slammer, asshole . . . (Marcus throws one punch into Ethan’s midsection. Ethan drops to one knee. Marcus grabs him by the hair and lifts him up – they fight) Get off me! FLASHBACK to Thomas and James dealing with the boys (lines should overlap)

JAMES: (Pg 6) Ethan!

THOMAS: (Pg 18) [Marcus!]

JAMES: (Pg 6) In the living room!

THOMAS: (Pg 18) Don’t walk off on me!

JAMES: (Pg 7) Are you out of your mind? What the hell is the matter with you?

THOMAS: (Pg 18) You will call the boy, apologize.

JAMES: (Pg 7) No it isn’t okay . . .

THOMAS: (Pg 18) Did your Lord Jesus ever respond to provocation with violence?

JAMES: (Pg 10) What the hell am I going to say to your mother?

THOMAS: (Pg 18) I told you to walk off from fools . . . Did I not?

JAMES: (Pg 9) Shut up, Ethan . . . your car is gone. Your computer is gone. PRESENT DAY

JAMES: (Pg 35-36) I’ll tell you what, Thomas. If there was a last thing in the world I wanted to do today, I guess I would say this is it. It’s the conversation I’ve spent eight years having with everybody, including myself. But I’ve stayed here because I thought the least I owed you was a conversation.

THOMAS: And we haven’t had it. We’re not having it!

JAMES: We’ve been having it. Because we are two different kinds of people, you can’t hear it.

THOMAS: Different kinds, huh? Oh, we’re different, that’s right. You can’t even hear yourself, man. “I don’t want to talk about it,” Uh-huh, yeah . . . you hidin’ behind this, hidin’ behind that, an’ that’s just chicken shit, man.

JAMES: F*** you!

THOMAS: (Enraged) You so angry at everybody, who you really angry at? FLASHBACK to the day of the shooting (Marcus and Ethan) (Pg 31-32)

(We hear 4 gunshots, then Marcus crosses the stage followed by Ethan who has a 45 in his hand)

ETHAN: (completely amped up and out of control and talking to himself) (Pg 5-6) What, you think I’m an idiot? You think you’re awake but, umm, you’re not awake. I clicked in that clip, we were all awake like this (He snaps his fingers several times) Wow! I felt good. I woke us up. When I opened up. (Marcus enters, sees James and tries to leave) (Pg 31-32) Stay right there, man. (Marcus turns and now James has a new mission. To kill Marcus) Real deal. Drop the books (he does) Goes around, comes around, huh?

MARCUS: Thought we got straight? (Ethan moves in forces Marcus to his knees he circles him as he speaks)

ETHAN: You’ll be dead in sixty seconds. How does that feel? Yeah, you made the list. You beat the piss out of me but you don’t get the big picture, man. I am so way beyond that.

MARCUS: My bad, all right? I’ sorry, okay? (Ethan moves forward until the pistol is directly in Marcus’ face.) Don’t shoot me in the face!

ETHAN: Really? Now I’m completely crazy and it’s all too late. I got SWAT teams up the wazoo, so hey, I don’t have time for this. Okay? See you later! (Ethan shoots Marcus in the face. He then turns and fires 3 more times from a double-handed firing position into the audience. (Pg 42) His cell phone rings. Ethan pauses, answers the phone and listens, it is obviously his father on the other end) (Softly) It’s not your fault. Tell Mom I love her. I’m scared, Dad . . . Gotta go . . . (Pg 45) (Ethan turns the gun on himself and commits suicide) PRESENT DAY

JAMES: (Pg 36) You’re locked in the cage, Thomas. Driving yourself crazy chasing yourself in circles. You are chasing something that does not exist. Closure does not exist.

THOMAS: You got to open the door and walk through it, brother.

JAMES: I don’t want to hear your goddamned sermon. Did I invite your Lord down here? If there’s some Lord on the premises then he must have sanctioned Ethan, right?

THOMAS: You better shut up, James. You raised your son, man. He didn’t just get it from the air. You know the apple don’ fall far from the tree. You know that.

JAMES: You think I’m angry? What the hell do you think you are? You didn’t come down here on the peace and love special, “brother.” You came here for payback.

THOMAS: (Pg 38-39) I’m not. . .

JAMES: (distraught) My son killed those children and then . . . and then . . . he put the pistol I bought him in his mouth . . . and killed himself.

THOMAS: James, [we’re] doing the wrong thing carrying this around. Wrong thing for me and the wrong thing for you.

JAMES: . . . I loved my son. See, I don’t think I’m so different from you . . . that anybody, you , anybody could have foreseen what happened. I didn’t. His teachers didn’t and it’s not clear to anybody what the hell was in his head. He didn’t warn his friends, he didn’t leave a note.

THOMAS: You got it all in your own courtroom, huh? You think as long as you’re the prosecutor and defense and judge, you don’t have to let anybody else in there. I went to a lot of trouble to find you, man, and all this time we been talkin’ you still don’t know why?

JAMES: Because it must be harder than anything in this world not to have somebody to blame.

THOMAS: Oh, I have somebody to blame, James. I blame myself. Who do you blame? I want to know was there a way to stop it. Cause if there was, I need forgiveness. You believe in forgiveness, Mr. Erskine?

JAMES: (Pg 27) The truth is . . . I don’t know what to say anymore. (Taps his forehead) [It’s]

always there. Smashes into my life, and anything I’m doing or feeling seems . . . beside the point. No amount of grieving for him and what he did can ever be enough.

THOMAS: (Pg 37) . . . . I used to go over to your house. 3 am, 4 am . . . stand on your walk . . . think about ringing your bell. I been a lot of bad places in my life . . . standing on your lawn in the dark, that was the worst. (Pg 29) (James weeps) Prayer takes us though moment we would not otherwise survive. We could kneel down here, James.

JAMES: No

THOMAS: We would be heard.

JAMES: No. No, thank you. (James takes out his wallet, in it he has pictures of Ethan as a young boy. He takes a shuddering breath) I miss what Ethan was. Ethan as a little kid . . . I miss that. (Pg 35) He was a good boy. . . (switches back to the picture that Thomas brought) [But] my son killed those children and then he killed himself. . . . listen, I did the best I could . . . (Pg 40) I am . . . deeply sorry. (He reaches out to Thomas)

THOMAS: (reaches out to take James hand) (Pg 44) The Lord’s here . . . (They both bow their heads in prayer)
```

---

## IC-1002: GQ

- Title: GQ
- Author (byline): Sharon Whitney
- Work: More One-Act Plays for Acting Students
- Publisher: Meriwether Publishing
- Publication date as stated: July 2003
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: PENN, QUINN
- Teaser before the introduction: No
- Spoken words (computed): 1008
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sharon Whitney
Book: More One-Act Plays for Acting Students
ISBN: 1566080878
Publisher: Meriwether Publishing
Date (Month/Year): July 2003
```

### Introduction (context only: never use it for content warnings)

```text
PENN: Society seems to think that females have a harder time than males preparing for a date.

QUINN: We’re here to counter that widespread belief.

PENN: Men are just as worried about what to wear,

QUINN: what to say

PENN: what to order

QUINN: how to act

PENN: as the ladies are.

QUINN: I mean, we can’t all be Mr.

BOTH: “GQ” by Sharon Whitney
```

### Performance text (classify this)

```text
PENN: (Trying on clothes while QUINN lounges in a chair) So, OK. The red scarf. Do you think she'll like me in red?

QUINN: Red is, well ... red. Maybe it'll get her excited.

PENN: I thought the line, you know... See how it hangs from my neck? The eye kind of travels, huh? Do you think I look taller?

QUINN: I don't know, it's risky.

PENN: Yeah?

QUINN: A little bit much... for you.

PENN: Yeah?

QUINN: Now don't get hurt feelings. It makes your waist look even thicker.

PENN: Thicker.

QUINN: You asked.

PENN: Oh, God. The other day I heard her say, "Look at that guy-what a pear." Oh, God.

QUINN: Listen... open up your neckline. That's what I do. A nice deep V, with something gold. Show some hair.

PENN: That's so Mafia ... isn't it? What do you think? Could I get away with it?

QUINN: Hey, you want her to look at your gut?

PENN: (Pause) She could look at my jacket. (He takes a jacket from a garment bag.) I just bought it. It was in GQ.

QUINN: GQ?

PENN: I spent a week's pay on it.

QUINN: Huh... You saw it in GQ?

PENN: You don't like it. (QUINN is silent.) I thought I'd wear it with black slacks and a cream-colored shirt.

QUINN: Cream?

PENN: I thought the guy in the ad kind of looked like me. (QUINN raises his eyebrows.) Jeeze.

QUINN: You asked.

PENN: Sorry. (Quinn sighs.) I'm just touchy today. For breakfast, I had two chocolate croissants. I inhaled 'em. (QUINN clucks.) Nerves.

QUINN: Oh, forget it. Why deprive yourself because she's got a thing for Greek gods? (PENN mews like a lost cat.) You're a little plump, a little soft around the edges. So what?

PENN: (He whimpers. Long pause) So. I spend three hundred dollars on a jacket and you say I look like a plate of mashed potatoes.

QUINN: You're overreacting.

PENN: It's the chocolate.

QUINN: (Rising) I don't need this.

PENN: I'm sorry, I'm sorry. Stay with me, buddy. Please. Tell me. Please. What's wrong with the jacket?

QUINN: Well. You need me. OK. The cut is English. It's made for someone who can project a kind of "hounds to the foxes" aura. (Penn mews.) And the tweed. On you, it's like an extension of your face. It looks like black and white whiskers.

PENN: Hurrah. The Hairy Ape. Three hundred bucks.

QUINN: Maybe... somehow... you can get around it. Try a blue shirt, or even mauve. If you can kill the effect of the tweed... get it away from your skin ...

PENN: I thought I should show my skin, my hairy chest.

QUINN: I was wrong. (Pause) Have you ever been draped?

PENN: I'm a winter. Black and white.

QUINN: Oh.

PENN: I'm gong to call her. I'll cancel.

QUINN: Oh, no, no, no. Let's work on this. Build you up.

PENN: I don't even know what to talk about.

QUINN: Ask her about her job. Women like that. It's all they think about, anyway. Their identity depends on it.

PENN: I know all about her job. I work in the same office.

QUINN: Some common sense, please. Play dumb. Let her run her trip. You don't have to listen, just keep eye contact and remember to say "oh" and "uh huh."

PENN: Won't she think I'm slow?

QUINN: She'll never notice. Women love to talk about themselves. It makes them think they got the world under control.

PENN: I read somewhere I should lean across the table and let her sit back. It's very flattering.

QUINN: (Nodding) Eat everything on your plate, too. It makes them upset when you order something and tinker with it.

PENN: OK.

QUINN: Offer to share something, though. That's sexy. Put something small on your fork and offer it with a line like, "This is superb. Will you sample?"

PENN: Superb? A fork full of peas?

QUINN: Peas?

PENN: Roast beef? (QUINN looks like he’s been poisoned.) No?

QUINN: No. For you a sensitive dish. (PENN is clearly stymied. Beat) Linguine with white clam sauce.

PENN: Clams give me hives. How about lasagna?

QUINN: Sure. slop it on your tie. (PENN is lost. Beat) A green salad with nasturtiums and radicchio. Scallops. Barely warm.

PENN: How about lamb chops? Itsy bitsy ones.

QUINN: In panties.

PENN: Right. Lamb with pants.

QUINN: What are you doing after dinner?

PENN: I could ask her to see my apartment.

QUINN: Oh, I don't know...

PENN: I could make her an espresso. I got some little cups and one of those knives that cuts lemon peel. Should I ask her? I know, I'll just trust my intuition.

QUINN: That's a myth - about men's intuition.

PENN: Yeah?

QUINN: Some have it, but most don't. (PENN groans.) All right, if you must: get her to take you to her place. If it's a disaster, you can always go home.

PENN: What if she puts some moves on me?

QUINN: What kind of underwear have you got?

PENN: The best. A hundred percent cotton.

QUINN: White, right?

PENN: You can bleach it.

QUINN: Lord... (Sighs.) Calvin Klein has a new silk line. Why don't you go wild and buy a pair of briefs.

PENN: She won't get the wrong idea?

QUINN: They're for heterosexuals. You can tell. They come in royal blue, banker gray and legal pad yellow.

PENN: I'm good in yellow... at least, I used to be.

QUINN: Then you're set. (PENN gathers his things, prepares to leave, then freezes, stricken.) What? What... ? What...

PENN: I don't know how to walk.

QUINN: Let's see. (Head down, arms bowed, fingers curled under, PENN skulks across the stage. QUINN considers him.) Does "miser's hump" run in your family? (PENN mews.) Come on, sport, chest out, chin up ... hup, hup ... not so stiff ... try to look carefree, maybe that would suit you. (PENN is boggled, but he tries walking this way and that.) By the way, no beer. Stick with white wine in case you spill it. Or maybe a blush, that's classy. But now that I think about it, it's not you. Do ale.

PENN: Someone should write a book: "What Every Man Should Know."

QUINN: Hmmm. Not a bad idea.

PENN: I'm reading "My Father, My Self."

QUINN: The son's search for identity?

PENN: It really gets me. I cried for half an hour.

QUINN: My shrink says it's no good.

PENN: Oh. (Beat) I'm going to call her. I'll cancel.

QUINN: You gonna waste my good advice? (PENN mews.) Hang in there.

PENN: Will you meet me for breakfast? I'll have to debrief.

QUINN: Leave a message on my machine.

PENN: I feel so vulnerable.

QUINN: Uh-huh.

PENN: Thanks for everything.

QUINN: Hey buddy. Walk tall. (PENN exits. QUINN sits a moment, then rises, calling Off-stage.) Clerk... ? Sir... ? Excuse me, sir... Yes, ha, ha - ha, ha. Oh, no, I wasn't shouting. Sir, could I possibly... uh, do you suppose... uh, you know that black and white jacket that was in GQ? The tweed? Is there a chance I could try it on? ... Oh, any size - whatever size you got... I know it's not really me ... but it could be ... Don't you think?
```

---

## IC-1003: Hangman

- Title: Hangman
- Author (byline): William Borden
- Work: More One-Act Plays for Acting Students
- Publisher: Meriwether Publishing
- Publication date as stated: July 2003
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: THEODORE, ROGER
- Teaser before the introduction: Yes
- Spoken words (computed): 1230
- Already set (do not supply): none

### Source block (context only)

```text
Author: William Borden
Book: More One-Act Plays for Acting Students
ISBN: 978-1566080873
Publisher: Meriwether Publishing
Date (Month/Year): July 2003
```

### Introduction (context only: never use it for content warnings)

```text
BOTH: “Hangman” THEODORE: By William Borden
```

### Performance text (classify this)

```text
THEODORE: Don't you feel some dishonesty? Killing people you have so much in common with?

ROGER: I don't find it dishonest, no. Poignant, perhaps. Ironic. Tragic, even. It's like playing a part in a great drama. It fulfills me. Whereas you become nameless, faceless, one of many who die futilely.

(THEODORE, watched by ROGER, stands on a stool, tying a rope to a pipe or beam. He finishes and steps off the stool. They both appraise it/or a moment, then ROGER tugs at the rope. The rope comes off ROGER throws the rope to THEODORE.)

ROGER: You think I haven't seen everything? Every trick and ruse you scum could possibly think of? You think I'm not smart?

THEODORE: You're very smart.

ROGER: I am.

THEODORE: I imagine you have a Ph.D.

ROGER: Don't get smart with me. (THEODORE ties the rope again.)

THEODORE: This will be a foolproof knot. Guaranteed to kill instantly.

ROGER: Not instantly. We want you to ponder your ways, reflect on your errors, as you dangle, swaying slowly in the breeze. Then we allow you to expire.

THEODORE: Expire.

ROGER: Yes.

THEODORE: You have an enormous vocabulary.

ROGER: Thank you.

THEODORE: A veritable prodigious lexicon in your cerebrum.

ROGER: I read vociferously. No television, no card games – I have the complete collection of The Great Books.

THEODORE: The Great Books? Who wrote them?

ROGER: You know those guys, from Homer and the Bible to Melville and Prowst.

THEODORE: Prowst?

ROGER: You're not too well read yourself, are you?

THEODORE: No, I'm not.

ROGER: Prowst was a French guy, wrote in a cork-lined room, suffered from asthma. He pursued the nuances of the past. Cherchez the past. And he was a fag. (ROGER tests the beam.) That's better.

THEODORE: Might be too sturdy.

ROGER: Naw.

THEODORE: I might not dangle long enough. I have a lot of sins to reflect upon as I die.

ROGER: They go fast. Whole life in a flash. That's the rumor.

THEODORE: As I dangle.

ROGER: As you dangle.

THEODORE: In the breeze.

ROGER: In the breeze.

THEODORE: What breeze? We're indoors. Miles from daylight. So you've told me.

ROGER: Well, just the momentum, as you plunge through the opening, and the rope, you know, jerks you up, as you're plunging down - gives your body what they call a torque, an angular momentum, so your body, as it's expiring, will swing, from its own potential energy.

THEODORE: Torque.

ROGER: You'll sway in quite graceful circles, or possibly ellipses, around and around.

THEODORE: Like a pendulum.

ROGER: Exactement.

THEODORE: I could become a clock.

ROGER: If I left you there.

THEODORE: Then you were lying about the breeze.

ROGER: It was a bit of poetry.

THEODORE: Do you write?

ROGER: Reports?

THEODORE: Poetry.

ROGER: Me?

THEODORE: Let me hear something.

ROGER: Naw...

THEODORE: Please! (ROGER pulls out a fat sheaf of scraps of paper. Then he looks at THEODORE.)

ROGER: You'll laugh. (THEODORE doesn't answer. ROGER hesitates, then starts to read.) "The rope sings like a nightingale as it snaps across the breeze" Maybe breeze isn't right there. (ROGER takes out a pencil.) "The rope sings like a nightingale as it snaps ... into the ... abyss ... of death."

THEODORE: "Death" 's trite.

ROGER: You're right. "Abyss of ... "

THEODORE: "Like a raven." "Raven" 's better than "nightingale." "Raven" connotes the harshness of the moment.

ROGER: It's a beautiful moment. Lyrical. And for those who disagree, there's the irony, the poignant reversal of expectation. "Abyss of ... "

THEODORE: "Horror."

ROGER: "Abyss of ... "

THEODORE: "Meaninglessness." "Nothingness." "Darkness."

ROGER: "Into the abyss of..."

THEODORE: "... into the sweet memory of roses." (ROGER looks at him a moment, then writes it down, shoves packet into his pocket.)

ROGER: (Reluctantly) Thanks. (ROGER tests the knot. It holds.) Good work.

THEODORE: Thanks.

ROGER: Of course it's not a professional job.

THEODORE: I'm going to hang!

ROGER: I'd think that would be a particular reason for taking pride in your work. Here. (ROGER hands THEODORE the other end of the rope.)

THEODORE: Now what?

ROGER: The noose. Make the noose.

THEODORE: (Throwing down the rope) No. I won't participate any further in my own murder.

ROGER: Execution, my friend. Words are important.

THEODORE: Shoot me then! That will make it murder!

ROGER: However I do it, it's an execution.

THEODORE: No

ROGER: I'm the executioner. It's a matter of definition. The man who writes the dictionary rules the nation. I can execute you now - (He pulls out the pistol.) Or you can have another minute or two to enjoy God's bounty on earth, while you tie the rope, while I test it, while we engage in scintillating dialect. Which do you prefer?

THEODORE: Shoot me. We might as well get it over with.

ROGER: That seems mighty shortsighted, my friend. Who knows what might occur in the next ninety seconds? An earthquake might kill me and free you. The rebels might stage an attack and divert my attention, allowing you to escape. There might be a coup from above. A foreign invasion. The Commander might commit suicide. You might receive a pardon. Don't forget - what's his name? You know, the Russian

THEODORE: Dostoevsky?

ROGER: That's the guy. Life is ruled by chance, old boy. Ninety seconds can seem like an eternity.

THEODORE: Everything is fated.

ROGER: An Augustinian!

THEODORE: There is a destiny

ROGER: God's? Or the inevitability of historical materialism? (THEODORE doesn't answer.)

THEODORE: I think for me ninety seconds will pass quickly.

ROGER: Time is relative.

THEODORE: Time marches forward inexorably.

ROGER: Inexorably.

THEODORE: Inexorably. I relish intellectual debate. Don't you? I haven't had a good discussion for a hell of a long time.

ROGER: (ROGER hands the rope again to THEODORE.) The noose.

THEODORE: I don't know how.

ROGER: I don't believe it.

THEODORE: It's not something you need to know in the normal course of a lifetime.

(Disgusted, ROGER begins to make the noose.)

ROGER: The other executioners, you know, all they want to do is play cards, read girlie magazines. I'm out of my element.

THEODORE: I can see that. (He watches ROGER deftly make the noose.) You're very good.

ROGER: Funny thing is, you guys usually have something to talk about. You seem to think more. It must be thinking that makes you dissatisfied with things.

THEODORE: It's not only thinking.

ROGER: I suppose not.

THEODORE: It's feeling, too. You know, intuitively, things aren't right.

ROGER: Well, it depends which side you're on, doesn't it? Like for me, things are right. (He completes the noose. He admires his work.)

THEODORE: But they're not.

ROGER: Of course they're right. Right as rain.

THEODORE: You're not happy.

ROGER: (Angrily) I'm happy!

THEODORE: You're a fish out of water. No intellectual companionship. No one to share ideas with.

ROGER: (Slipping the noose over THEODORE's head) Now there's where you're wrong, old sport. I have you to converse with. You and your compatriots. All day, every day, one after another, a veritable parade of intellect.

THEODORE: Perhaps you'd like to join us.

ROGER: Get myself executed?

THEODORE: Fight for a cause.

ROGER: Die before my time?

THEODORE: Live a meaningful life.

ROGER: Die like a dog? There's a flaw in your syllogism. (ROGER motions THEODORE onto the stool.)

THEODORE: Don't you feel some dishonesty? Killing people you have so much in common with?

ROGER: I don't find it dishonest, no. Poignant, perhaps. Ironic. Tragic, even. It's like playing a part in a great drama. It fulfills me. Whereas you become nameless, faceless, one of many who die futilely.

THEODORE: Who knows what's futile?

ROGER: It's plain as the noose around your neck.

THEODORE: But don't we have some effect? Make some difference?

ROGER: Oh, yeah. I learn a lot. I sharpen my wits. You make a big difference to me.

THEODORE: Do I?

ROGER: Definitely. (THEODORE climbs onto the stool.)

THEODORE: I mean, do I? Do I, Theodore, make a difference to you?

ROGER: What do you mean?

THEODORE: Or am I just one of many who pass through your life? What's your name?

ROGER: My name? I have no name. So far as you're concerned.

THEODORE: Have you no conscience?

ROGER: Do you? Wouldn't you kill me if you could? Even after our thrilling conversation? You would. Because I'm on the other side. It would be my fate to die.

THEODORE: It would be a chance you would take.

ROGER: So you see, I have no choice.

THEODORE: You always have a choice.

ROGER: Do you? (ROGER gets ready to kick away the stool.)

THEODORE: One question - (ROGER pauses.) Does everyone participate in his own ... death?

ROGER: Oh, yes. We think it makes a point. It teaches a lesson.

THEODORE: But what good will it do now?

ROGER: That's the irony of it, isn't it? Any further last words?(Several beats. ROGER gets ready to kick away the stool.)

THEODORE: Proost.

ROGER: What?

THEODORE: Proost! It's pronounced Proost, not Prowst!

ROGER: You kidding me?

THEODORE: No.

ROGER: You're sure?

THEODORE: I'm positive.

ROGER: You know French?

THEODORE: Tres bien.

ROGER: Proost.

THEODORE: Proost.

ROGER: I could've gone on for years making a fool of myself.

THEODORE: I know. (Several beats)

ROGER: Well. We can't wait forever.

THEODORE: No. (Several beats)

ROGER: Roger.

THEODORE: Pardon?

ROGER: My name's Roger.

THEODORE: Ah. (Beat) Theodore.

ROGER: Right. (ROGER starts to kick away the stool, the stage goes to black,
and there s a strange musical note, as of a string being plucked, the
overtone lasting for several seconds.)
The rope sings
like a nightingale
as it snaps
into the sweet
memory of roses.

It's a beautiful moment. Lyrical.
```

---

## IC-1004: Han’s Crime

- Title: Han’s Crime
- Author (byline): Shiga Naoya
- Work: The Paper Door and Other Stories
- Publisher: Columbia University Press
- Publication date as stated: Jan 2001
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: JUDGE, STAGEHAND, NARRATOR, HAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1951
- Already set (do not supply): none

### Source block (context only)

```text
Author: Shiga Naoya
Book: The Paper Door and Other Stories
ISBN: 978-0231121576
Publisher: Columbia University Press
Date (Month/Year): Jan 2001
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: In an unusual incident, a young Chinese juggler called Han severed his wife’s carotid artery during a performance with a knife the size of a carver. The young wife died on the spot. Han was immediately arrested.

ACTOR 2: The act was witnessed by an audience of over three hundred. But it was not at all known whether this incident, which had occurred before so many eyes, was a deliberate act or an accident.

ACTOR 1: For this performance, Had made his wife stand in front of a thick board. From a distance of twelve feet, he hurled several of the carver-sized knives to form an outline of her body not two inches removed from it.

ACTOR 2: The judge commenced by interrogating the Stagehand of the troupe.

TOGETHER: Hans’ Crime by Shinga Naoya
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

JUDGE: What is Han’s ordinary behavior like?

STAGEHAND: He’s a good person. He doesn’t gamble, fool around with other women, or drink. About a year ago, he converted to Christianity. His English is good, and when he has the time he often reads collections of sermons.

JUDGE: And his wife?

STAGEHAND: She was a good person too. As you know, people o four sort aren’t’ always known for their strict morals. One often hears of somebody running off with somebody else’s wife. Han’s wife was a beautiful woman, although on the small side, and she now and then got solicitations of that sort. But she never took up with such people.

JUDGE: What were their dispositions like?

STAGEHAND: Toward others, they were both extremely kind and gentle. They never thought of themselves and never got angry. And yet . . . I’m afraid this may be to Han’s detriment, but to tell the truth, when it came to their own relationship, they were surprisingly cruel to each other.

JUDGE: Had they always been that way?

STAGEHAND: No. About two years ago, the wife gave birth. The baby was premature, and died in three days or so. But after that, it was clear even to us that their relationship was slowly going to the bad. They would often have arguments over the most trivial things. At such times, Hand would suddenly turn dead pale. But in the end, no matter what, he always fell silent. When you looked at this face, there was a terrible, uncontrollable anger in it. Once I suggested that if things were so bad between them it might be good to get a divorce. He said that there was no way he could love his wife. It was only natural, he said, if a woman he did not love gradually came not to love him. It was why he took to reading the Bible and collections of sermons.

JUDGE: What is your opinion of the incident? Was it deliberate or an accident?

STAGEHAND: He gave a short cry: ‘Aa!’ That was what drew my attention to what had happened. The blood suddenly gushed out of the wife’s neck. Even so, she remained upright for a moment. Her body was held in place by the knife’s sticking in the board behind her. Then, all of a sudden, her knees buckled, the knife came out and collapsing all together she fell forward. There was nothing anyone could do. We all of us just went stiff and watched. But it seems to me that for those few seconds he was just like us. It was only afterward that I thought: He’s murdered her at last. Han wend dead pale and stood there with his eyes closed. We drew the curtain down and tried to revive the woman, but she was already dead. Han blurted out: ‘How could I make such a blunder?’ Then he knelt, in a long silent prayer.

NARRATOR: Dismissing the Chinese stagehand, the judge finally had Han himself brought in.

JUDGE: I’ve been questioning the owner-manager and the stagehand. I will now ask you some questions. . . Have you never loved your wife at all?

HAN: From the day I married her until the day she had the baby, I loved my wife with all my heart.

JUDGE: Why did the birth become a source of discord?

HAN: Because I knew it wasn’t my child.

JUDGE: Do you know who the father was?

HAN: I have an idea it was my wife’s cousin. He was a close friend of mine. It was he who suggested that we get married. He introduced me to her.

JUDGE: Was there a relationship before she married you?

HAN: Of course there was. The baby was born the eighth month after the marriage.

JUDGE: The baby died shortly afterwards? What was the cause of death?

HAN: Yes. It choked at the breast.

JUDGE: Was that a deliberate act of your wife’s?

HAN: She said it was an accident.

JUDGE: Did your wife tell you about the relationship?

HAN: No, she didn’t. Nor did I ask her about it. I felt that the baby’s death was a judgment on her for what he’d done. I thought that I myself should be as forgiving as possible.

JUDGE: But, in the end, you couldn’t forgive her?

HAN: That’s right. My feeling remained that the baby’s death wasn’t enough of a judgment.

JUDGE: You didn’t think of divorcing her?

HAN: I often thought I’d like a divorce. But I never said anything. I was weak. And my wife had said that if I divorced her she would not survive.

JUDGE: Did your wife love you?

HAN: She did not love me.

JUDGE: If that was so, why did she say such a thing?

HAN: I think it was from the necessity of going on living. Her brother had broken up the household back home, and she knew that no respectable man would marry a woman who’d been the wife of a road-player.

JUDGE: Did your wife feel any sympathy for you?

HAN: I can’t think she felt any sympathy. I believe that for my wife, living with me was an extraordinary hardship. My wife simply observed, with cruel eyes, the gradual destruction of my life.

JUDGE: Did you ever think of killing your wife? (SILENCE) Han, did you ever think of killing your wife?

HAN: (PAUSE) I’d often thought, before then, that it would be good if she were dead.

JUDGE: Then, if the law had allowed it, you might have killed her?

HAN: I was afraid of the law, and I had never had such thoughts before. It was merely because I was weak. But even though I was weak, my desire to live my own life was strong.

JUDGE: So, after that, you thought about killing your wife?

HAN: I didn’t make my mind up to it. But I did think about it.

JUDGE: How long before the incident was this?

HAN: The night before. Toward daybreak.

JUDGE: Had you quarreled that evening?

HAN: Yes . . about something so trivial it isn’t worth mentioning.

JUDGE: Tell me anyway.

HAN: It was about food. When I’m hungry, I get irritable. The way she dawdles over the preparations for supper made me angry. I went to bed, but I couldn’t sleep at all. I looked to one side and the other, always hesitating, without the courage to want what I wanted, without the courage to get rid of what was unbearable. It was all due to my relationship with my wife. I could see no light in my future. What with the pain and unhappiness of it all, I was being poisoned. When the poisoning was complete, I would die. Although alive, I would be a dead man. And though this was what I had come to, I was still trying to put up with it. It would be good if she died – one part of me kept having that dirty, hateful thought. If this was how things were, why didn’t I kill her. The consequences of such an act did not trouble me now. I might be put in jail. Who could tell how much better life in jail might be than this life. At last, I grew tired. My thoughts began to blur. As my tensed up feelings relaxed, my dark thoughts of murder faded away. A feeling of loneliness came over me. I even felt pity for my own weak spirit . . . and then, at last, the night was over. It seemed to me that my wife hadn’t slept either.

JUDGE: Why didn’t you think of leaving your wife?

HAN: For me there was a great difference. (Pause – Judge nods) But, between my thinking about such a thing and actually deciding to kill here, there was still a wide gap. That day, from early morning on, I felt insanely keyed up. But I no longer thought of killing her, as I had the night before. And I was not at all worried about that day’s performance. If I had been, I would not have chosen that particular act. We had many other acts. Finally, that evening, our turn came. As usual, I demonstrated to the audience that the knives were sharp by slicing though a piece of paper and sticking a knife into the stage. My wife, wearing a gaudy Chinese costume, came on. She stepped up to the thick board and stood bolt upright with her back to it. For the first time since the night before, we exchanged looks. Only then did I realize the danger of having chosen this act for tonight. I began to feel that I could not trust my own arm. Closing my eyes, I attempted to calm myself. My body started to sway. I drove in the first knife above her head. Each time one hit, I thought: Thank God. Calm down, calm down, I thought. I drove in a knife to the left of her throat. I was about to drive in the next one to the right, when suddenly a strange look came over her face. She must have felt an impulse of violent fear. Dizziness struck me. But even so, with all my strength, almost without a target, as though aiming in the dark, I threw the knife . . . (LONG PAUSE) I’ve killed her at last, I thought.

JUDGE: How do you mean? That you’d done it on purpose?

HAN: Yes. I suddenly felt as if I had

JUDGE: Afterwards, you knelt by the body in silent prayer . . . ?

HAN: That was a trick that occurred to me at the moment. I knew everyone thought I seriously believed in Christianity. While pretending to pray, I was thinking about what attitude I should take.

JUDGE: You felt sure that what you’d done was intentional?

HAN: Yes. And I thought right away I could make out it was an accident.

JUDGE: But why did you think it was deliberate murder?

HAN: Because of my feelings, which were unhinged.

JUDGE: So you thought you’d skillfully deceived the other?

HAN: I acted surprised in a natural manner, was considerably agitated, and also displayed grief. But any perceptive person, I believe, could have seen that I was playacting. That night, I decided that I would have to be found innocent. Everyone knew we’d been on bad terms, of course, so there was bound to be a suspicion of murder. I couldn’t do anything about that. But if I insisted, throughout, that it was an accident, that would be the end of it. There was no proof. In the end, I though, I would be acquitted for lack of evidence. Soon, thought, for some reason, a doubt rose up in me as to whether I myself believed it was murder. The night before, I had thought about killing her . . . but was that alone a reason for deciding it was murder? Gradually, I became unsure. I was so happy. I wanted to shout for joy.

JUDGE: Was it because you yourself could now believe that it was an accident?

HAN: No. I’m still unsure of that. It was because it was completely unclear, even to myself, which it has been. It was because I could now tell the truth and be found innocent. Being found innocent meant everything to me now. For that purpose, it was far better to be able to be honest, even if it meant saying I didn’t know which it was. Come what may it was no longer a question of a confession of guilt.

JUDGE: (Pause) On the whole, it seems to be the truth . . . Do you not feel the slightest sorrow about your wife’s death?

HAN: None whatsoever. And up to now, no matter what my feeling of hatred for her, I never imagined that I’d be able to talk so cheerfully about her death.

JUDGE: That will be all. You may step down.

NARRATOR: Han, after a slight wordless bow, left the room. The judge felt an excitement, he could not put a name to it, surge up in him. Quickly, he took kup his pen. And, then and there, he wrote: “Innocent.”
```

---

## IC-1005: The Harry and Sam Dialogues

- Title: The Harry and Sam Dialogues
- Author (byline): Karen Ellison
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Jan 1994
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: HARRY, SAM
- Teaser before the introduction: Yes
- Spoken words (computed): 876
- Already set (do not supply): none

### Source block (context only)

```text
Author: Karen Ellison
ISBN: 082221380X
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Jan 1994
```

### Introduction (context only: never use it for content warnings)

```text
Sam: Harry and Sam are old friends who like to pass the time posing outlandish

questions to one another. Harry: "If ya’ had the choice would ya’ rather love a woman whose top half was a fish

and whose bottom half was a woman or a woman whose top half was a woman

and whose bottom half was a fish?” Sam: See what I mean? Together: The Harry and Sam Dialogues by Karen Ellison
```

### Performance text (classify this)

```text
Character: Harry and Sam (30-40), a couple of regular guys.

Scene: Here and Now: Harry and Sam have been best friends for 20 years. Here, they engage in idle, yet imaginative, banter while shooting pool.

(Fade in. McDougal's Bar, Harry and Sam's hangout. Harry and Sam play pool. Two stools sit nearby.)

HARRY: Say ya' gotta tree.

SAM: I gotta tree.

HARRY: Ya' gotta whole forest 'a trees.

SAM: I gotta whole forest 'a trees.

HARRY: Now say there's only one person for miles around-a guy with one of those red and black jackets and a ski hat with an axe...

SAM: A lumberjack.

HARRY: Whatever. And he's chopping one 'a your trees. But he only chopped part way.

SAM: Gotcha.

HARRY: Now he's pulling out his lunch pail.

SAM: A red one?

HARRY: Yeah.

SAM: Like yours?

HARRY: Yeah.

SAM: (Fondly.) With the matching thermos?

HARRY: Yeah! Okay! And he's starting to eat.

SAM: Lunch.

HARRY: Yeah. So this guy-this tree chopper-while he's eating his lunch, he gets a call on his beeper.

SAM: He gotta beeper?

HARRY: Yeah.

SAM: This lumberjack, in the middle 'a the woods using an ax to chop a tree, has a beeper.

HARRY: Yeah, he has a beeper! He's part of a large tree chopping corporation.

SAM: Timber mill.

HARRY: Whatever. So this guy gets a call on his beeper. He pulls out his cellular phone- (Harry gives Sam a look.) 'cause there's no phone booth in the woods...

SAM: 'Course.

HARRY: ...And he calls the number that flashed on his beeper, and the guy on the other end says, "Come on over to the plant, quick! Your wife's having a baby!"

SAM: At the plant?

HARRY: No, not at the plant. At the hospital!

SAM: The lumberjack-he know about this?

HARRY: What?

SAM: He know his wife's gonna have a baby?

HARRY: Yeah! 'Course he knows!

SAM: 'Cause the way you said in, "Come on over, Your wife's having a baby," sounds like it's a surprise.

HARRY: 'Course he knows about it. He whaddaya'-call-it-helped!

SAM: He knew she was pregnant?

HARRY: Yeah, Sam. He knew she was pregnant.

SAM: She wasn't keeping it from him?

HARRY: She's as big as a house, for Christ's sake!

SAM: Don't curse. He hasn't maybe been out of town for nine months chopping trees in the... Black Forest, say?

HARRY: No! He works about fifteen miles from home.

SAM: Fifteen miles.

HARRY: Yeah. (Sam writes something down. Harry looks over his shoulder.)

SAM: What's his wife's name?

HARRY: Doesn't matter what his wife's name is!

SAM: Just thought it might be important.

HARRY: It isn't. Trust me. So, anyway, this tree chopper puts down his lunch...

SAM: What's he eating?

HARRY: What?

SAM: What's he eating for lunch?

HARRY: It doesn't matter what he's eating for lunch.

SAM: How do I know? How do I know it doesn't matter? What if you're going to ask me the contents of his stomach when they pump it during the autopsy after his car is pushed off a cliff by an eighteen wheeler driven by Yahn and Eric, the perpetrators of the tax fraud that the young lumberjack, Yom van Yom, was going to expose at Shady Pines, the timber mill where he works? It could be important! Everything's important to me now, Harry, because I don't know, do I? And sure. Sure you'll say, "Trust me." Trust you? Like the time you were telling that joke to the lodge about the porpoise and the prostitute, only you left out that part about. .

HARRY: Salad.

SAM: Salad?

HARRY: He's eating salad for lunch, and then the tree chopper runs to his pickup truck and drives off to his wife whose name doesn't matter who's having a baby at the hospital.

SAM: Natural or cesarean?

HARRY: How should I know what kind salad it was? So, anyway, while the tree chopper is at the hospital, this one tree that he chopped part way, remember?

SAM: I remember.

HARRY: 'Cause it was sometime ago that I mentioned that.

SAM: I remember.

HARRY: This one tree falls down.

SAM: Lawsuit!

HARRY: No lawsuit!

SAM: It lands on someone's car!

HARRY: Who's telling this story? No. There's nothing and no one around for miles. Just trees.

SAM: Trees.

HARRY: Trees. So?

SAM: So?

HARRY: When the tree hits the ground, does it make any kind 'a noise?

SAM: Let me get this straight: if a tree falls in the forest, and no one's there to hear it, does it make a sound?

HARRY: Well... yeah. That's another way to say it.

SAM: No.

HARRY: What?

SAM: No. (Indicating pool table.) It's your shot. (Harry puts his hand to his back.) You okay?

HARRY: Had to sleep on the end of the bed. Ya' don't want time to think about it?

SAM: No. She made ya' do that? Ballbuster.

HARRY: I'11 give ya' a couple minutes.

SAM: Don't need time. The answer is still no.

HARRY: No, huh?

SAM: No.

HARRY: Ya' don't want to ask me some questions?

SAM: No.

HARRY: Like are there any animals in the forest?

SAM: No.

HARRY: Maybe ya' want to ask me what's on the ground in the forest?

SAM: No.

HARRY: Grass?

SAM: No.

HARRY: Dirt?

SAM: No.

HARRY: Moss?

SAM: No.

HARRY: Moose goo?

SAM: No.

HARRY: No sound?

SAM: No sound. (Pause.)

HARRY: Well, this really stinks. I mean this eats it. You're not playing along!

SAM: Ya' asked me a question, I answered. (Smug.) Go ahead. Ask me another. (Pause.)

HARRY: Okay. It's the beginning of time, and there's this big red barn owned by Caveman Farmer Wilson. ..

SAM: Cut to the chase.

HARRY: Okay. Whi...

SAM: The egg. (Pause. The following exchange takes place fast andfurious.)

HARRY: Is there life after death?

SAM: No.

HARRY: Who built the pyramids?

SAM: Martians.

HARRY: What is Stonehenge?

SAM: Primitive wristwatch - made by Martians.

HARRY: Why can't ya' get a good five cent cigar?

SAM: Recession.

HARRY: What do vice presidents do?

SAM: Wait for someone to die.

HARRY: What is Bigfoot?

SAM: Giant gorilla-man from Mars.

HARRY: Where is Jimmy Hoffa?

SAM: Yankee Stadium, left field, seats 3A through D.
```

---

## IC-1006: Hate the Loser Inside

- Title: Hate the Loser Inside
- Author (byline): John Kern
- Work: The Best Ten-Minute Plays 2012, Pgs 79-94
- Publisher: Smith and Kraus Publishers
- Publication date as stated: June 2013
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: COACH BRODHAUS, WENDELL, COACH B
- Teaser before the introduction: Yes
- Spoken words (computed): 1743
- Already set (do not supply): none

### Source block (context only)

```text
Author: John Kern
Book: The Best Ten-Minute Plays 2012, Pgs 79-94
ISBN: 978-1575257938
Publisher: Smith and Kraus Publishers
Date (Month/Year): June 2013
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 2: A coach’s words can often inspire resilience, teamwork, and the pursuit of excellence.

ACTOR 1: Coaches encourage people to push their limits and believe in their potential, regardless of the outcome.

ACTOR 2: But that coaching fame only lasts for so long. What do you do when your coaching days are over?

ACTOR 1: Low-budget commercials for local companies!

ACTOR 2: This Duo sponsored by Winston’s Kitchens and Designs . . .

TOGETHER: Hate the Loser Inside by John Kern
```

### Performance text (classify this)

```text
(Pg 79-94) Coach Brodhaus is at a table with a breakfast plate of eggs, bacon, and pancakes; half a grapefruit, a glass of milk, a box and bowl of cereal, silverware, and a napkin.

COACH BRODHAUS: I'm Coach Donny Brodhaus, Winner of this year's college football national championship. And when I sit down for a championship breakfast, I make sure MY kitchen [gestures behind him] has cabinet fronts and counter tops by Winston's Kitchens and Design. Take it from a winner like me, when it comes to home furnishings, Winston's is the real champion. They've been providing high-quality kitchen interiors since 1970. And with their low, low prices, you won't need to make millions to look like you do. [awkward pause] So score a touchdown with your neighbors with the style and class of a Winston's home. Winston's Kitchens and Design: It's what completes a real, really complete, real breakfast. [blank]

WENDELL: [offstage] Cut!

WENDELL: [enters, script in hand] That was good. That was really good.

COACH B: I keep *messing* up that last line.

WENDELL: It's a tongue twister. It's ... [slight pause] Are you ready?

COACH B: Yeah, yeah, just give it to me.

WENDELL: It's . . . "It's what really makes a breakfast complete."

COACH B: It's what really makes a breakfast complete. . . really makes a breakfast complete.

WENDELL: Good. Good. Coach, we're really proud to have you for this commercial. You're the man who brought the title back to Illinois.

COACH B: It's what really makes a breakfast complete.

WENDELL: Okay. [slight pause] So let's just jump back on. [exits; offstage] Okay; and rolling.

COACH B: So score a touchdown with your neighbors with the style and class of a Winston's home. Winston's Kitchens and Design: It makes a breakfast what is real. Son of a ****!

WENDELL: [offstage] Cut! [enters] Maybe . . .

COACH B: Is there an yway I can just skip that line?

WENDELL: I'm sorry. That's been the slogan for Winston's Kitchens and Design for more than twenty years. Maybe we should start in the middle and work your way to the line.

COACH B: Sure, I'll give that a shot. You know what might also help . . . If we could get a real kitchen.

WENDELL: I already explained, the kitchen will be put in post-production. That way, throughout the commercial, we can change the Winton's design in the background. [Coach reaches into the box of cereal and starts eating a dry handful] What we need from you is to just look at the camera, And . . . And don't shift anything on the table. Everything on the table is placed carefully, so the camera picks it up but it doesn't block your face. [adjusts the cereal box back in place]

COACH B: I get that. I just think it'd be a little easier to focus on talking about a kitchen, if there was an actual kitchen. But I don't want to hold this up, so . . . Can I see the script?

WENDELL: [hands the script to Coach B] So let's take it from, "They've been providing high quality kitchen interiors since 1970."

COACH B: Could we start with something shorter?

WENDELL: I'm confident you can get it. And I want you to add

COACH B: [interrupting] You want me to add something?

WENDELL: After the line, "You won't need to make millions to look like you do." add a wink to the camera. Can you wink?

COACH B: Like this? [can't help but use two eyes]

WENDELL: No, more like . . . [Coach B winks] Just one eye. Like . . . [Coach B winks] Try to keep the other [Coach B winks] the other eye open. [Coach B winks] [Wendell tries to hold Coach Brodhaus 's eye open] Now try. [Coach B winks; both eyes close] Don't fight it. Don't fight ... Open the other eye! [Coach B winks] Just forget the wink. Can you instead . . . Cross your arms and smile? [demonstrates] Cross you arms [crosses arms] then smile. [smiles]

COACH B: Like this? [crosses arms and smiles]

WENDELL: Perfect. After the line . . .

COACH B: "You won't need to make millions to look like you do."

WENDELL: Perfect. And . . . and take it from, "Take it from a winner like me."

COACH B: Uh . . . [looking at the script]

WENDELL: Ooo, can't have that in the shot. [snatches script and exits][offstage] Places. Ready, Coach?

COACH B: I'm ready.

WENDELL: [offstage] And rolling. [Coach B look to camera. Clears his throat.] [offstage] Still rolling.

COACH B: Take it from a winner like me, when it comes to home furnishings, Winston's is the real champion. They've been providing high-quality kitchen interiors since 1970. And with their low, low prices, you won't need to make millions you look like you do. [stiffly crosses arms, no smile; sudden very fake smile] So score a touchdown with your neighbors with the steel and clips of **** [creatively curses]

WENDELL: [offstage] That was good. Take it from, "And with their low, low prices."

COACH B: And with their low, low prices, you won't need to make millions to look like you do. [bright smile; then no smile, stiffly crosses arms] I just did that backwards, right?

WENDELL: [offstage] Not a problem. Take it again. Still rolling.

COACH B: And with their low, low prices, you won't need to make millions to look like you do. [crosses arms; smiles] So score a touchdown with your neighbors with the style and clams of a Winston's fern. *****[creatively curses]

WENDELL: [offstage] Cut! [enters] Coach, you're doing good. Really.

COACH B: I don't get it. My whole brain has been . . . [blows raspberry] I won a national football championship, and now I can't do some cheap, local commercial.

WENDELL: We're still doing good.

COACH B: It's the damn arm crossing. Before I just had problems with the last line. Now I can't do any of it. [grabs a chair and rattles it against the floor]

WENDELL: Do you need a moment?

COACH B: I'm good. I just want to get this done. It's my head that's a sack of farts. [taps fists on table; restrained anger] You know what I told my players before the Tostitos Fiesta Bowl, [dramatic pause] I told them, "Give me 100% and you will forever be the greatest there ever was." [pause] Those kids were gladiators that night, motorized by a passion I inspired. And now I can't *say* the word kitchen without my brain burning.

WENDELL: Yeah, it can be hard . . . Keeping your mind on track, just so you can get through the day. I wanted to go to Hollywood, when I was in my twenties. But then . . . You fall in love with a girl who wants to settle down, and so you settle for whatever. Then that girl divorces you. And you realize yours is an all too common tale. You look around and all you notice is marinara crusting on dishes and a whole lot of *stuff* that needs to be Swiffered. And you start to think of the kid you were . . . the dumbest *kid*. . . who ever walked this earth. As if what you were - - what you still are -- Is unforgivable.

COACH B: What's your name again?

WENDELL: Um ... Wendell. It's Wendell.

COACH B: Well, Wendell, when I hear your story, you know what I hear? I hear the whining whimper of a quitter. I hear a man who didn't fight for what he wanted.

WENDELL: [to the crew] Can we get ready? We're going to roll in a second.

COACH B: You're going to hear no a lot in life, sure. But you can't ever say no to yourself. In every one of us, there lives a loser and winner. If you want the winner to succeed, you've got to hate the loser inside. That's how you become a champion, Wendell.

WENDELL: We have to continue on. We're going to start from the very top, okay? [exits]

COACH B: [to self] C'mon, Donny. You're not a failure! You can whup this commercial!

WENDELL: [offstage] Are you ready, Coach?

COACH B: [to self] Crush it, Donny boy, Crush it. [to Wendell] Yeah, I'm good. [to camera] I'm Coach Donny Brodhaus, Winner of this year's college football national championship. And when I sit down for a chumpionshap brakfust . . . [sigh] [creatively curses]

WENDELL: Let's keep going.

COACH B: [to camera] I'm Coach Donny Brodhaus, ewnner of this year's college football national championship. And when I sit down for a championship breakfast, I make sure MY kitchen [gestures behind him] has cabinet fronts and counter tops by Winston's Kitchens and Design. Take it from a whimper like pluh / We're not going back. [creatively curses]I'm going to keep marching forward.

WENDELL: [offstage] Still rolling!

COACH B: [to self] You're a champion. You're a champion with a poophead, but you're still a champion. [to camera] Take it from a winner like me, when it comes to home furnishings, it would help to remember your line. Take it from a winner like me, when it comes to home furnishings, Winston's is the crapalapa dong ding. [hurls an apple against the wall]

WENDELL: [offstage] We don't need the apple – not important to the shoot. We're rooting for you, Coach. I know you can finish this!

COACH B: Don't cut. [shakes his body clearing himself of negativity vibes]

WENDELL: [offstage] C'mon, Coach, Woo! You can nail this copy.

COACH B: Don't patronize me. [to camera] Take it from a winner like me, when it comes to home furnishings, Winston's is the real champion. They've been providing high-quality kitchen interiors since 1970. And with their low, low prices, you won't need to make millions to look like you do. [crosses arms; smiles] So score a touchdown with your neighbors with the style and class of a Winston's home. Winston's Kitchens and Design: It breakfasts completely. AAGH! [deep cleansing breath; cracks neck] [to camera] So score a touchdown with your neighbors with the style and class of a Winston's home. Winston's Kitchens and Design . . . It's a breakfast. Actually, it's a kitchen. [Coach B starts flipping plates on the table, slamming food against the floor or walls] I AM SICK OF THIS. [goes berserk, flips the table. As extreme as possible] [Wendell enters; Coach B brandishes a chair at Wendel] No. NO! Stay back! [Wendell scurries off][Coach B to camera, calmly and professionally] I'm Coach Donny Brodhaus, winner of this year's college football national championship. And when I sit down for a championship breakfast, I make sure MY kitchen [gestures behind him] has cabinet fronts and counter tops by Winston's Kitchens and Design. Take it from a winner like me, when it comes to home furnishings, Winston's is the real champion. They've been providing high-quality kitchen interiors since 1970. And with their low, low prices, you won't need to make millions to look like you do. [crosses arms; smiles: NAILS IT!] So score a touchdown with your neighbors with the style and class of a Winston's home. Winston's Kitchens and Design: It's what really makes a breakfast complete. [winks with both eyes]

WENDELL: CUT!
```

---

## IC-1007: Hello Herman

- Title: Hello Herman
- Author (byline): John Buffalo Mailer
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: April 2010
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: HERMAN, SENATOR JOHN COX, CHILDREN’S AID SOCIETY REP, LAX, MR. PHELPS, SUSAN, OFF STAGE VOICE OF CRIBB, CLARKSON 1, MARSHA, HARMAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1672
- Already set (do not supply): none

### Source block (context only)

```text
Author: John Buffalo Mailer
ISBN: 978-0822224105
Publisher: Dramatists Play Service
Date (Month/Year): April 2010
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: 1999 - Columbine, Colorado ACTOR 2: 15 people dead

ACTOR 1: 2012 - Sandy Hook Elementary, CT ACTOR 2: 28 people dead

ACTOR 1: 2018 - Parkland, Florida ACTOR 2: 17 people dead

ACTOR 1: And while the COVID-19 pandemic appears to have interrupted the trend line, it does not mean schools are “safer.”

ACTOR 2: It’s hard to empathize with someone who carries out a school shooting. The brutality of their crime is unspeakable. Whether the shootings were at Columbine, Sandy Hook or Parkland, they have traumatized students and communities across the US.

ACTOR 1: But understanding the culture and the mentality of school shooters are the keys to prevention.

ACTOR 2: Unfortunately, our society seems to be focused on punishment rather than prevention. Are consequences and active shooter drills the answer?

ACTOR 1: Or are we asking all the wrong questions?

TOGETHER: Hello Herman by John Buffalo Mailer
```

### Performance text (classify this)

```text
Suggested Roles: Actor 1: Herman, Clarkson (News Reporter) 2, Senator John Cox

Actor 2: Paul, Clarkson (News Reporter) 1, Children’s Aid Society Rep, Lax, Mr. Phelps, Susan, Cribb, Marsha

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

HERMAN: (Pg 40) (meanacing, he struts around with a gun – this is the happiest moment of his life) Paul! Paul Schruber! Today is your lucky day! Because you are so valuable to our school, you get to live! Now, take a bow and get out of my gym, Paul. (Paul moves toward the exit) You forgot to take a bow! (Herman shoots him in the knee – Paul falls down, screaming in pain) Shut up! ****** CLARKSON (1): (Pg 12) Forty-three students were shot before [Herman]Howards was apprehended

CLARKSON (2): “Bloody Broome” as it is now being called, is the worst high-school massacre in the history of America. CLARKSON (1): (Pg 15) While there remains no clear motive for the killings, what has become very clear, is that today’s teenage culture is rampant with violence . . . Senator John Cox issued a statement to the press this morning. ******

SENATOR JOHN COX: (Overlap lines with Children’s Aid Society Rep) Herman Howards is not a common criminal; he is a terrorist, pure and simple. A coward. He must be executed. And his execution ought to be televised nationally, so that America’s children can witness what happens when you disregard the value of life.

CHILDREN’S AID SOCIETY REP: Herman Howards is a troubled child in serious need of psychiatric treatment. What kind of message does it send to the world when America starts executing our own children on television? Killing people does not stop people from killing people.

LAX: (Pg 11) This Week’s Topic: High School Terrorists . . (Pg 18) (a buzzer goes off. We hear the sound of a prison door opening. Herman enters) (Pg 25) (To Herman) Hello, Herman

HERMAN: “Hello, Herman!” Starring Herman Howards and Lax Morales. I get top billing? I mean, it is my story.

LAX: Get it straight, Herman. I’m not here to turn you into a rock star. I’m here because there’s a world outside that thinks you should be electrocuted, at age sixteen, on national television. That’s a story. That’s important.

HERMAN: (Pg 19) (explodes) I’m an individual! Don’t forget that! You think just anyone could do what I did? No sir. There’s only one Herman Howards, and now history will remember me.

LAX: You don’t talk like the average sixteen-year-old kid.

HERMAN: I’m not your average sixteen-year-old. I’m America’s worst nightmare.

CLARKSON (1): (Pg 30) We’ll be right back.
******
CLARKSON (1): (Pg 12) (Overlap lines with Clarkson (2)) While parents of the formerly peaceful
community of Broome, Iowa grieve the tragic loss of their children

CLARKSON (2): Parents all over suburban America are wondering if their town will be next. ******

LAX: (Pg 18-19) May I interview you now? (long beat)

HERMAN: How much money do I get for talking to you?

LAX: You don’t get anything. Any money goes to the families of the victims. Besides. I thought you wanted to tell your story. (beat) Did you get picked on a lot at school, Herman?

HERMAN: (shrugs it off) The jocks call me names cause I’m small. They’d push me around.

LAX: You kids still play Doom . . . Postal?

HERMAN: (Pg 20) I own it (he begins to ramp up) You’re a postal worker. You go into the office one day cause you’ve had enough of people’s crap and you shoot everyone up til they’re all gone. (Herman laughs)

LAX: Your mom supports you in playing games like Postal?

HERMAN: I don’t think she knows anything about it. (Pg 28) We don’t interfere with each other. She’s very good about giving me my privacy.

LAX: What about your father? (long beat)

HERMAN: (Pg 35) He left when I was eight.

LAX: (Pg 28) When you were eleven, your sister was hurt in a hit-and-run, right? She died a few days later.

HERMAN: Yeah.

LAX: It happened right outside your house . . . did you go out and help her.

HERMAN: I was eleven. There wasn’t a whole hell of a lot I could have done, now was there. (Pg 29) You really don’t get it!

LAX: Don’t get what?

HERMAN: (Pg 27) Jesus Christ you’re asking stupid questions. I thought you were supposed to be some kind of hotshot reporter. (Pg 29) I’m done talking to you today. (long beat)

LAX: (Pg 27) Okay, let’s cut to it. (Pg 40) Tell me more about the day you did it. You rounded up all the kids in the gym. . .

HERMAN: (Pg 20-21) Yeah (Herman smiles) You had to be there. At one point this girl started running for the door. (gunshot) I clipped her right in the back of the head and her face exploded and landed all over some kid (breaks into laughter) Thought she was home free . . . when all of a sudden, “OOPS! THERE GOES MY FACE!”

LAX: Do you even know the girl’s name?

HERMAN: She was background. Not a key player.

LAX: It was a game, wasn’t it?

HERMAN: It’s all a game, Lax. (Pg 37) If I could just get one more game in, I’d be happy.

LAX: (Pg 26) You feel no remorse?

HERMAN: (pause) I didn’t want to kill Mr. Phelps. *****flashback******

(Mr. Phelps enters and slowly walks toward Herman)

MR. PHELPS: (Pg 40) There’s still time. Stop this madness, Herman.

HERMAN: Sit down! I don’t want to kill you! (Phelps keeps walking toward Herman, his hand out asking for the gun. Gunshot. Phelps falls) (to Lax) I had to shoot. He would have grabbed me if I didn’t. He looked so stupid. I almost started laughing, but out of respect, I didn’t. (Pause – flashback continues) Are there any other teachers in the room? (to Lax) I knew Ms. Cribb was there. No one came forward, so I called up three kids who were lying on the floor near me. Susan, this bitchy girl no one really liked, James, the editor of the school paper and Marsha, the hottest girl in school. (flashback continues) (Pg 42-43) Hello! If you are a teacher, please come forward and take a bow! (no response – he puts the gun to Susan’s head) Oink!

SUSAN: What?

HERMAN: Oink! Like in Deliverance. Squeal! (She tries, but is crying too much)

SUSAN: Jesus, please protect me. Jesus, please protect me . . . .

HERMAN: (gets a kooky expression on his face, then starts to laugh) Not today. (Gunshot- end flashback) (To Lax) I shot her at an angle, so the bullet would go through her skull and blood would splatter all over Marsha. [She] walked around those halls like she owned the place. Because she was a nice-looking piece of . . . . You think that’s gonna fly? (shakes his head) It’s the ones like me are going to run the show! This is the only way to make you assholes finally pay attention to us. I wasn’t about to settle for some rinky-dink shit. Oh, no. I blew that dumb b****’s head off and made sure a little got on James as well. But I was never going to kill him. I wanted him to live, so he could write about the day in his precious paper.

OFF STAGE VOICE OF CRIBB: Please, Herman, Stop! (Gunshot)

HERMAN: I shot Cribb right in the mouth. Isn’t she at the hospital or something?

LAX: They had to amputate her jaw. What was left of it. She’ll have to be fed intravenously.

HERMAN: Awesome! She deserved it. Gave me a C- in phys-ed. Can you believe that? A C-! Unreal! Lax? Lax, you still with me?

LAX: (Pause) Why don’t we take a break. I need some coffee.

CLARKSON 1: (Pg 44) (Off-stage) The verdict came in today on The People vs Herman Howards. Howards will be the first minor executed in the state of Iowa.

HERMAN: (Pg 43) Whatever . . .

LAX: (re-inters) (Pg 46) Are you ready to die, Herman?

HERMAN: When you die, it’s “game over.” Nothing. Blackness.

LAX: What about “reset”?

HERMAN: When you hit “reset,” the game you played before doesn’t have *anything* to do with the next one. All the characters come back to life.

LAX: That’s not how it works in real life. Once a kid is killed, he doesn’t come back.

HERMAN: (Herman doesn’t speak. His face changes. It is as if he’s beginning to worry - softly) (Pg 47) I dream they come back . . . I keep shooting. It’s like I have unlimited bullets and they have unlimited lives. How can dead people haunt your dreams?

LAX: Why don’t you ask them the next time you go to sleep?

HERMAN: Shut up! I’m fine! (Pause) You want to hear what else happened or not? The police came to the door and I threw a pipe bomb into the middle of the crowd. It got crazy. I was just running around shooting people left and right. It was anarchy. Awesome! (flashback as Herman narrates) I ran up behind Marsha and put the forty-five to her back. (To Marsha) Ready to die, prom queen?

MARSHA: Please don’t. I’ll do anything. I want to see my mom again. Pleeeeaasse!

HARMAN: Isn’t it funny? She was ashamed to be caught taking to me before that. (Pg 48) You know what that kind of power feels like? I shot her down low. Bashed her nose with the butt of my gun and left her there to bleed. I’m glad she survived. To learn what life is like when you’re not the prettiest girl in school.

LAX: (Now) You’re a teacher? – What did they learn, Herman?

HERMAN: Maybe they learned to be a little nicer to each other. [But] I doubt it. The world’s gotta see more kids like me before they finally get it. That’s okay, they will.

LAX: They’ll finally get it?

HERMAN: No. (he grins) The world will see more kids like me.

LAX: (Pause) We have real problems in this world, Herman. Melting glaciers, massive unemployment, crumbling nations with nuclear missiles. You think I have time to worry about some depressed kid from the suburbs going into his school and killing people? Why didn’t you just wait to go to college and find friends there? I mean, really!

HERMAN: It worked, didn’t it? You’re here, aren’t you? It was the only way to get you to pay attention to me.

LAX: You’re going to be killed. You destroyed hundreds of lives. You inflicted pain on innocent people. You gave up everything just to be on my show?

HERMAN: (Pg 49) I wasn’t about to go through life being unnoticed. (Pg 42) Do you know what the largest generation is? Mine! Believe me, we’re going to do a hell of a lot more than “Rock the Vote.” This is the only way to make you assholes finally pay attention to us!

LAX: (Pg 49) This is not about your generation, Herman. This is about you doing unspeakable things.

HERMAN: You have to do the unspeakable if you want to be noticed.

LAX: You think anyone’s going to care about you in two months? You’re gonna be a footnote, listed next to a bunch of other forgotten footnotes.

HERMAN: Google me in twenty years, Lax. Then we’ll see who’s right. (Pause. Herman’s entire façade has melted and now we are left with a little boy) (Pg 50) Between you an me? I’m scared. I don’t want to die. Sometimes I wish I could take it back. You know, hit reset. But I can’t. (He cries) ******break*******

CLARKSON 1: This is Chet Clarkson reporting live at the execution of Herman Howards. The highest viewed event in television history. Senator . . . your thoughts?

SENATOR JOHN COX: America will see today that the government of the United States will not allow our children to be in danger any longer. Killing people may not stop people from killing people, but seeing the execution live sure as heck will.

CHILDREN’S AID SOCIETY REP: (Pg 15) Herman Howards is . . . [was] a troubled child in serious need of psychiatric treatment. What kind of message does it send to the world when America starts executing our own children on television?
```

---

## IC-1008: Her Name is Kathy

- Title: Her Name is Kathy
- Author (byline): Donna de Matteo
- Work: Not specified
- Publisher: Applause Books
- Publication date as stated: August 2007
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: JACK, BILLY
- Teaser before the introduction: No
- Spoken words (computed): 1829
- Already set (do not supply): none

### Source block (context only)

```text
Author: Donna de Matteo
Books: The Best American Short Plays 2001-2002
ISBN: 978-1557837059
Publisher: Applause Books
Date (Month/Year): August 2007
```

### Introduction (context only: never use it for content warnings)

```text
Abortion was criminalized throughout the U.S. between the late 1800s and 1973. But during that time, millions of women sought and obtained abortions anyway.

Of these, tens upon tens of thousands died from illegal abortions or complications arising from them. One study estimated that illegal abortions or complications from them were the cause of death for 15,000 women each year. Some of these deaths were the result of the abortions themselves, but many more were from infection and hemorrhaging afterward. Because of the fear of being punished and socially ostracized, many women--and their doctors--kept their real condition a secret.

Today, the degree to which abortion is available in the U.S. is an open question. 87 percent of all U.S. counties don't have an abortion provider. Which leads to the question . . . How many women still suffer at the hands of “back-alley” abortion providers? Her Name is Kathy by Donna de Matteo

Time: A hot summer night in August. The year is 1957. The time is 10 PM.

[BILLY LOGAN, A good-looking seventeen-year-old young man is seated in the emergency room waiting room of a New York City hospital, Elmhurst General. He is wearing a pair of buckle back chinos; a white 'T-shirt; a pair of high-top white sneakers and white socks. Splotches of blood coven his pants, T-shirt, socks, and sneakers, and parts of his face and arms. He is shaking like a boy who cannot wake up from a nightmare he is having. He almost starts to cry. To distract himself, he picks up a Life magazine. No longer able to hold back the tears, he starts to cry, wiping his eyes and nose on his shirtsleeve.] [JACK LANDAU, a thirty-something hot-shot criminal defense attorney, enters. He is dressed in a gray suit, a button-down shirt, and tie. He is carrying a soft brown leather attaché case.] [Hearing footsteps, BILLY, still sniffing, covers his face with the magazine.]
```

### Performance text (classify this)

```text
JACK: Billy Logan? [Sniffing, BILLY picks up his head, and, again, goes to wipe his nose on his shirtsleeve. JACK whips out a pressed handkerchief and hands it to him.]

JACK: [Continuing.] Here. Use a handkerchief.

BILLY: Thanks. [BILLY blows his nose and tries to hand it back.]

JACK: Keep it. [Cracks a joke.] I'll put it on my bill. I'm Jack Landau, your attorney. Your father told me to meet you here.

BILLY: Is he coming?

JACK: I advised him against it. The father in him wanted to be here, but the Judge in him knows better.

BILLY: He must be so mad at me.

JACK: He's concerned that you're still in one piece.

BILLY: He told me not to talk to anybody.

JACK: You can talk to me. And whatever you say is strictly confidential.

BILLY: I mean, the whole thing was just an accident ...

JACK: Tell me what you told them.

BILLY: Told who?

JACK: The Admitting Office. The Doctor. Anyone that you spoke to.

BILLY: [Lying.] I told them the truth. That I lost control of the car and smashed into the side of a building. I was doing about forty when I jammed on the brakes and that's when Kathy practically flew through the windshield. Her whole body just crashed against the dashboard, and all of a sudden, she was bleeding, all over the place.

JACK: Any cops around? Pedestrians? Other moving cars?

BILLY: No.

JACK: ... Is that when you called your father?

BILLY: [Lies.] Yeah.

JACK: Where did you call him from?

BILLY: Uh, a pay phone ...

JACK: And how far away from the accident site was the phone?

BILLY: I don't remember. .. I was so confused.

JACK: And that's when you told your father you were taking her to Elmhurst General?

BILLY: I guess ...

JACK: And where exactly was the accident site?

BILLY: Around 108th Street ...

JACK: In Corona ... A lot of tenements there. Were there any people hanging around outside to cool off?

BILLY: ... If there were, I didn't see them ...

JACK: What were the two of you doing in Corona? It's a slum ...

BILLY: Uh, just cruising around ... There's a White Castle there ... on Northern Boulevard ...

JACK: There's a White Castle on Northern Boulevard in Douglaston, too, which is where you happen to live ... so why travel.. ..

BILLY: . We just wanted to ride around ...

JACK: And for no apparent reason, you lose control of the car, crash into a building, where not another soul hears you, and you walk out of the car without a scratch on you, while ... what's her name ...

BILLY: ... Kathy ... Her name is Kathy ...

JACK: ... While Kathy was, as you say, bleeding all over the place, you walked to a pay phone, took out a dime, and called your father instead of an ambulance.

BILLY: I was too scared to call an ambulance because I was drunk .... We, uh, drank a bottle of Seagrams.

JACK: So, she was drunk, too?

BILLY: . Yeah.

JACK: Did anyone here ask you why you didn't call an ambulance?

BILLY: ... I think I told them I was only ten minutes away I don't remember what I told them, I was drunk, confused

JACK: Billy ... you don't sound like you were confused to me. Do you mean to tell me that after drinking a half a bottle of Seagrams, you still had the presence of mind to make a phone call, and then manage to get back into the car and drive ten minutes to this hospital while what's her name was still bleeding?

BILLY: Kathy ... Her name is Kathy ...

JACK: ... How did you even manage to get the car started if the crash was as bad as you said it was?

BILLY: It's a very heavy car ... A brand-new 1957 Ford Fairlane 500. My parents gave it to me for graduation. But, if you don't believe me, take a look at the car. It's right outside that door. It's a wreck.

JACK: I saw the car, Billy. That's my problem. You front ended the car into the building. The headlights are gone. The front fender is upended, and the passenger side windshield is shattered. Did her head go through the windshield?

BILLY: ... I don't think so.

JACK: Then where the hell did that bucket of blood that is covering every inch of those white vinyl seats come from?

BILLY: I already told you ... she went flying against the dashboard! Her head hit the windshield ...

JACK: But did any of the glass hit an artery?

BILLY: [More unnerved.] I don't remember. .. !

JACK: Well, you better remember because it looks like that girl was butchered in that car. How did all of that blood get onto the back seats if she was sitting in the passenger seat? The amount of blood in the interior of the car is not commensurate with the exterior damage, which means, something happened in that car before the accident. ..

BILLY: Nothing happened in the car before the accident!

JACK: There was no accident, Billy, so let's stop the bullshit! You purposely took that car and crashed it three times into an abandoned tenement building in Corona. When the impact didn't do what you wanted it to do, you got out of the car, took a tire iron, and smashed the passenger seat windshield. There were two witnesses who saw you. Two guys were coming out of the Parkside Restaurant. They thought you were some lunatic so they called the Precinct and gave the Police your plate number. When the Precinct got the alert, the Captain, who thank God is a personal friend of your father, recognized the plate number, because he also happened to be at your graduation party when you got the god-damn car. He called your father right after you called your father with that bullshit story of the alleged accident. Billy, your Dad has had to pull some very serious strings to stop the usual wheels of the system from rolling. Look around you ... This is a city hospital. Do you see any cops here yet? Do you see anybody else in this room? All other ER traffic has been sent to Queens General. Your father is going to owe a lot of people a lot of favors. Now, you have got about five minutes before all hell breaks loose here. So once and for all, tell me the truth. What did you do to that girl?

BILLY: I got her pregnant.

JACK: [Confused.] Pregnant?

BILLY: The night of the Senior Prom at Holy Cross.

JACK: What does this have to do with ... ?

BILLY: That's how it all started ...

JACK: By getting her pregnant?

BILLY: She didn't even really want to. She was a virgin. And I told her, "If you love me, you'll let me." When it was over, she said I would think she was a slut now. In a million years I never thought she'd let me. We were gonna get married when I finished college. The next day we broke up. We couldn't even look at each other.

JACK: So, when did the girl tell you she was pregnant?

BILLY: Kathy. Her name is Kathy. A week ago.

JACK: How pregnant was she?

BILLY: Two months ...

JACK: And what about after the Prom until a week ago? Did you have any contact with her?

BILLY: No.

JACK: Did she tell anybody else? Her parents?

BILLY: No. She was sure her father would throw her out of the house.

JACK: And did you tell anyone?

BILLY: Who would I tell? My Morn and Dad are so religious, if they were sailors, they'd have the Ten Commandments tattooed on their arms. I was too scared.

JACK: So, what did you do after she told you?

BILLY: I didn't know what to do. I offered to marry her but she still had another year of high school. What were we going to do with a baby? So, we both agreed to, to ...

JACK: Get rid of it ...

BILLY: Yeah ... So, I called a Buddy of mine, Joey Antonucci. His brother got his girlfriend pregnant before he got killed in Korea, so I asked him the name of, of, of ...

JACK: An abortionist.

BILLY: But he wouldn't talk to me on the phone. He made me meet him in the Loge Section of the RKO in Flushing. He sat down, offered me some buttered popcorn. I told him I needed the name for a friend. So, he hands me the napkin he wiped the butter off his mouth with, and tells me to slip it into my back pocket.

JACK: So, he gave you a name and number ... ?

BILLY: No name. Just a number on a napkin that there was so much butter on, I could hardly make it out.

JACK: And so you called the number ...

BILLY: Yeah.

JACK: And then what?

BILLY: I made an appointment to meet this guy. He told me to bring an old sheet, a box of those things ... Kotex; and fifty dollars in cash. And, he said to let her drink a bottle of whiskey before we got there so she wouldn't feel any pain. But, she wasn't used to drinking ... by the time we got there, all she kept doing was throwing up. [He starts to cry.]

JACK: Come on, just tell me the rest, Billy.

BILLY: So, we meet this old guy on the second floor landing. The building was pitch black except for this flashlight he was carrying. His hand was shaking so much that the light from the flashlight was bouncing off the walls. I saw a rat this big running across the hall. I was ready to leave right then and there, but Kathy said no. The old guy takes what's left of the bottle of Seagrams and drinks it himself. Tells me to stay in the hall, ... not to worry ... he's done this a million times, he says ... Then he brought Kathy into this apartment and slammed the door.

JACK: So, you were never in the room while the crime was being committed?

BILLY: No, but I could hear her screaming through the door. Jesus Christ, I didn't know what to do. I was so scared.

JACK: ... And then what happened?

BILLY: She stopped screaming. I waited for five minutes and walked in. And that old drunken bastard was gone. He must've ran out of the fire escape window and Kathy, was on the floor, on the sheet, covered with blood. I never saw so much blood. I wanted to call an ambulance, but she said we'd both get arrested. That's when I got the idea to make it look like a car accident.

JACK: My God ... And then what?

BILLY: She couldn't walk cause she had these really bad cramps, so, I wrapped her in the sheet, carried her down the stairs and put her on the back seat of my car.

JACK: And that's when you crashed your car into the tenement? Was the girl still conscious at that time?

BILLY: Jesus Christ, for the last time, her name is Kathy.

JACK: Wake up, Billy. Her name was Kathy. The girl is dead. She was dead when the attendants got her out of your car. Her parents are on their way here and they are going to want to know, "How did this happen?"

BILLY: [Buries his head in his hands.] I am sorry. I am so sorry ...

JACK: [Puts an arm around Billy's shoulder to console him.] "How the hell did this happen?"
```

---

## IC-1009: Hidden in This Picture

- Title: Hidden in This Picture
- Author (byline): Aaron Sorkin
- Work: Best American Short Plays 1990 (Pg 141-168)
- Publisher: Applause Theatre Books
- Publication date as stated: Feb 2000
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: REUBEN, ROBERT, JEFF, CRAIG
- Teaser before the introduction: Yes
- Spoken words (computed): 1802
- Already set (do not supply): none

### Source block (context only)

```text
Author: Aaron Sorkin
Book: Best American Short Plays 1990 (Pg 141-168)
ISBN: 978-1557830852
Publisher: Applause Theatre Books
Date (Month/Year): Feb 2000
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Do you know what makes a movie a movie?

ACTOR 2: Think about it. A movie is pictures stitched together to make up 24 frames per second that give the illusion of motion.

ACTOR 1: Photography brought to life to tell the story the artist (the director) wants to tell.

ACTOR 2: It’s beautiful, messy, and beyond fascinating.

ACTOR 1: But today, the director has more to worry about that creating art. Production is 3 weeks behind and 6 million over budget.

ACTOR 2: The sun is setting faster than it's ever set before, and the final long-angle sequence has to be filmed NOW, before the light fades.

TOGETHER: Hidden in This Picture by Aaron Sorkin
```

### Performance text (classify this)

```text
NOTE: This cutting asks one student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles: Actor 1: Robert
Actor 2: Reuben, Jeff and Craig
A small, grassy hill overlooking a massive expanse of land. ROBERT (the director) is surveying
the scene before him. After a moment, REUBEN (the producer) enters. He's out of breath.

REUBEN: (Pg 141-168) The final shot, Robert, one shot, and then the crew, the cast, the six-hundred and ninety-four extras, the cameras, the lights, they all go home. There's no re-take. We can't ask the sun to come back and set again because we *messed* it up the first time. (no response) Three and a half minutes, Robert! Don't you think you should be down with the crew?

ROBERT: The crew knows what to do. (He stops gazing out in the distance. He speaks directly to REUBEN) We've been rehearsing for the past six hours. Despite the fact that this is my first film, a fact that you remind me of four times a day, I'm not an idiot. This is the most important shot in the movie, and I have no intention of *messing* it up. I have left absolutely no room for human error, Reuben. Six-hundred and ninety-four extras, already costumed and approved in their uniforms, will, in a slow, trickling theatrical stream, trot from the ridge of those trees, down past the blue flag and out of camera range. Roll credits. Together we're going to watch art being made. Jeff worked very hard on this screenplay.

REUBEN: Yeah? Well, it's lousy. I got news for you, if the audience doesn't understand what is going on, they leave. And they tell their friends. There's no sequel. And if you think I'm some kind of studio-puppet who only sees dollars and cents, you're right. That's my job. (Reuben storms off)

ROBERT: (JEFF – the screenwriter enters) Reuben's in a bad mood, Jeff. He thinks I've spent too much time and money making a movie about disillusioned Marines in Guam and he thinks your screenplay is full of Yale Drama crap.

JEFF: I'm not sure I'd say the Marines are disillusioned.

ROBERT: Jeff, I've created a picture here, I've communicated with an image -- an idea, an emotion, my idea, and I've done it as succinctly as a well written sentence and as powerfully as a symphony. The rest of this film may end up looking like Beaver Goes to War, but this shot is gonna work.

JEFF: Good luck.

ROBERT: Ssh! (Pause, whispering) Action. (Pause) Oh yeah. Oh. Oh my. This is for my children, Jeff. This is for my daughter, Jennifer, who'll watch it with her friends and say "My Daddy did that." This is for my unborn son who'll look at this and say, "I want to be just like my Dad." This isn't for the actors, Jeff; this one's for me. Look at it, Jeff, look at it.

JEFF: I'm looking . . . Bobby? (Pause) Three cows have walked into the shot.

ROBERT: (Long pause. He must have heard wrong) I'm sorry, what did you say?

JEFF: Three cows have walked into the shot.

ROBERT: (ROBERT turns and looks out) There are cows in the shot. Jesus Christ Almighty. (He runs off yelling) YOU'RE IN THE SHOT! GET OUT OF THE SHOT! COWS! GET THE HELL OUT OF THE SHOT! (Long pause. ROBERT returns) Before I even begin to try and solve this problem, I want you to tell me, Jeff, you wrote the screenplay, you did months of research, you read books, tell me, are there cows on Guam?

JEFF: Not on Marine bases.

ROBERT: Never?

JEFF: No, never. There are no cows on Marine bases. Anywhere. Guam, Nicaragua, Berlin, there are no cows.

ROBERT: Don't tell me there are no cows, there are three cows standing in the middle of the shot!

JEFF: That's because we're ten miles outside of Schenectady on a farm. We're only pretending we're on a Marine base. Bobby, it's okay. Just have some guys run out there and kinda shoo away the cows -- sorta herd 'em off to the left.

ROBERT: Jeff, an entire Marine infantry unit is running toward them with machine guns. They're not moving anywhere.

JEFF: It's 'cause they're all running past them. The cows probably can't even see them. Send some people out to run right towards them and herd 'em off. You can edit this stuff out and the scene'll be nine minutes instead of eleven minutes. (Pause) Bobby, it's the only thing to do.

ROBERT: Those cows have gotta be three-quarters of a mile away. We've got eight minutes left. Do you know how long it's gonna take to get a film crew to run three-quarters of a mile, clear the cows from the shot and then clear themselves from the shot? What are they doing there?

(CRAIG – Production assistant enters)

CRAIG: Bobby, three cows have walked into the shot. I think it's pretty noticeable.

ROBERT: Oh? What makes you say that, Craig, what makes you say it's noticeable?

CRAIG: Well . . . everybody noticed.

JEFF: You might be able to salvage enough ending footage and then fudge around with the continuity on the sunset.

ROBERT: What's goin' on? God, why are you doing this to me? Please move the cows, God. Move 'em seventy-five yards to the left, God, what's the big deal? I'm not kidding, I'm really at a complete - I don't know what I'm supposed to do. Are you - Wait, wait, wait, what are they doing? They're bobbing their heads or something. What does that mean? Do you think that means they're ready to leave? Does it seem to you that they're about ready to leave?

CRAIG: I think they're about ready to leave.

JEFF: I don't - I'm not a livestock psychologist, Rob, I don't know if the cows seem ready to leave. Craig, on the other hand, has a very strong sense that the cows will be leaving soon.

ROBERT: Would you look at those guys? Just trotting by these cows like they weren't there. Doing it exactly the way we did it in rehearsal. You'd sorta think that one of 'em would say to himself "Hm, I'm an actor and I'm supposed to be imitating life. Right now I'm playing a Marine on my way back to the barracks. There's a cow. If I were a Marine, I'd probably think it was somewhat out of the ordinary to see a cow on my way back to my barracks." You'd think one of those guys would acknowledge the fact that they're running past three cows. . . (Pause as Roberts surveys the scene)(Relieved) The extras have discovered the cows. They're acting with the cows -- doing bits of business with the cows. I hate those cows! (Beat) You know what I think? It's not nearly as big a problem as we think it is.

JEFF: Truly, Robert, that's the attitude you gotta have.

ROBERT: I don't think anyone in the audience is gonna notice. I mean, sure, they're gonna notice, they're gonna see these three cows in silhouette against a sunset while 694 Marines file back to their barracks after having spent the most difficult day of their lives engaged in a war game, sure the audience is gonna see these cows, but I don't think they're gonna find that strange. Why should they? They're just cows. Everybody's seen cows.

JEFF: On a Marine compound? In Guam?

ROBERT: You think people are gonna pick that out? (Makes up his mind) Craig, call down to the deck. Get one of the policemen to shoot the cows.

JEFF: Craig, stop. Bobby, you can't tell the police to shoot the cows. You can't kill cows to make a movie.

ROBERT: We kill cows to make hamburgers, why can't I kill cows to make a movie, what's the difference?

JEFF: What's the difference between food and a movie? Are you serious?

ROBERT: They don't have to kill the cows, they don't have to shoot to kill, just drop 'em. Wound 'em for crying out loud, I'm running out of time.

JEFF: Bobby, allow me a very quick hypothetical. Let's assume for a moment that Schenectady police officers carry pistols that can fire three-quarters of a mile and that the officers are accurate at that range to be able to wound and not kill a cow. Fast forward a year. Don't you think that even the people who don't find it a little strange that three cows have wandered into Guam are gonna be a little perplexed when the cows, for no apparent reason, fall down to the ground?

ROBERT: You're right. I've been looking at this all wrong. Look at the cows. What do they look like to you?

JEFF: The cows? They look like cows.

ROBERT: Don't you think they look a little like tanks? Sherman tanks. Don't you think they look a little, off in the distance there in silhouette, like tanks? We have footage of tanks. I just keep jump cutting for half a second at a time to these shots of tanks. All the way through, just keep jump cutting to tanks, three, four frames a shot, they will be subliminally convinced that they're looking at tanks. They will be subliminally convinced!

JEFF: Because you showed them tanks every once in a while, they're gonna think those cows are tanks? Who do you think your audience is?

ROBERT: Idiots, Jeff. I think the vast majority are lazy, stupid idiots who, I believe, can be convinced by a clever director with enough footage at his disposal that three cows are in fact Sherman tanks.

JEFF: Well, you're wrong. The only person who thinks those cows are anything but cows is you.

ROBERT: We are film makers and we don't lock ourselves into conventional notions and labels. We give ourselves the freedom to explore and communicate our own surroundings and we don't file the world around us into little shoe-boxes and label them black and white.

JEFF: Those are cows, Bobby. THEY LOOK LIKE COWS! They walk like cows! They eat like cows! They're cows! Accept that fact. I wouldn't lie to you about something like this. And I think they're the best thing in the movie.

ROBERT: (Pause. quietly) You're right. You're right. They're cows. There's really no way of getting around that. They're cows. They'll have to stay cows. So fine. Okay. There are three cows standing in the last shot of the picture. (Pause) What did I mean by that? What was I trying to say? I need to examine this. What are cows? What are cows? What do cows do? Cows give milk. Milk is life. Is milk life? No, not really. Milk is milk. But it's also life in a way. Sure. Milk. Mother's milk. The milk of life. (Pause) Young, disillusioned Marines ... Young disillusioned Marines . . . what? . . . Sucking the milk of life. . . the last drops of the milk of life, right? . . . Sunset? Endings? The Last Drops? (He's got it) Young disillusioned Marines sucking the last drops of life from cows . . . Because their mother's aren't there with them in Guam! (Beat) (REUBEN enters)

REUBEN: Those cows were a pain in the a**, huh? What the hell, we'll just matte 'em out when we cut it. Hell of a sight though. I swear, I almost *peed* my pants.

ROBERT: Matte' em out? . . . . (With bravado) Why would I want to matte out the cows? I rehearsed those cows, I auditioned over four-hundred cows. Those were my first choice. You gotta admit, the camera loves 'em. It's the whole statement of the picture . . . The cows.
```

---

## IC-1010: His Daddy

- Title: His Daddy
- Author (byline): Cori Thomas
- Work: 2010 The Best 10-Minute Plays
- Publisher: Smith and Kraus
- Publication date as stated: Sept 2010
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: CHARACTERS, PLACE, JOHN, DAVID, CHILD'S VOICE, TOGETHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1470
- Already set (do not supply): none

### Source block (context only)

```text
Author: Cori Thomas
Book: 2010 The Best 10-Minute Plays
ISBN: 978-1575257723
Publisher: Smith and Kraus
Date (Month/Year): Sept 2010
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Innocent faces smiling from milk boxes have served as a chilling reminder that childhood is not always safe in America.

ACTOR 2: Not all of those missing children are found, and regrettably, some of the cases end in tragedy.

ACTOR 1: In this selection, John and David, spent years planning for the surrogate birth of their son Billy

ACTOR 2: 5 years later, the most horrific parental nightmare occurs.

TOGETHER: His Daddy by Cori Thomas
```

### Performance text (classify this)

```text
CHARACTERS: JOHN -- thirties to forties. Caucasian. Works in construction. DAVID -- thirties to forties. Must be played by a person of color: African American, Latino, Asian etc. He is an attorney.

PLACE: The hallway of an institutional building - The morgue.

JOHN: Oh God! Shit! Shit! (hallway of an institutional building. It is the morgue. John sits on the floor, his hands covering his face. David, dressed in a suit and perhaps tie, emerges from a door.)

DAVID: You all right?

JOHN: No. Oh God. How could you be so calm in there? It felt like . . . it felt like . . .

DAVID: You got sucker punched.

JOHN: Yeah. Yeah, that's what it feels like.

DAVID: I can't even process . . . I've dreamt about that moment. I practiced

JOHN: You practiced?

DAVID: You know what I mean.

JOHN: No. I don't. I didn't practice anything. I was hoping. I was wishing. I was praying. I was praying.

DAVID: Me too. But, I knew . . . Deep down I knew . . .

JOHN: Don't say that.

DAVID: I can't help what I felt. (Beat.) I was praying too.

JOHN: You just don't know, not until you see . . . and touch . . . (Exhales.) you don't know anything . . .

DAVID: I know.

JOHN: (With deliberate and sudden ferocity.) You. Don't. You cannot in a thousand years know what it feels like to be me at this particular moment. To have gotten that call and have to come here and identify our son's body.

DAVID: I do. I got that call too.

JOHN: No, David, you don't.

DAVID: OK, I don't. (Beat.) Shit! (Beat.) Sorry.

JOHN: Yeah right. Sure. Sure.

DAVID: And now we know. OK. We know and it's over.

JOHN: Yes.

DAVID: (Beat.) I didn't think that you had . . . I mean, yes I blamed you. I blamed you and I thought you were responsible. I know it makes no sense but you can't help what you feel. I look at you and even now . . . knowing . . . even now . . .

(Dialogue overlaps.)

JOHN: God, David. This again? Damn it! Damn!

DAVID: I'm sorry. I can't . . . I can't help it.

JOHN: But still . . . ? Really? Still?

DAVID: Going in there and seeing . . . I know that you couldn't . . .

JOHN: (Making move as if to hit him.) Don't even go there. Don't you even . . . if for one second that ever crossed your mind . . . You heard what Officer whatever his name in there just said; he waited, that f***head waited patiently till the moment when I let go of Billy's hand. I looked at him like this, (Shows him.) So he would know not to move. I took my hand from his to stick in my pocket to get the 3 pennies to make the exact buck fifty-eight for the Snickers bar. It was in that moment. That second, and if you know how many times I have gone over this, it was no more than 63 seconds. One minute and 3 seconds. That's the long count. I turned away from Billy for barely more than a minute to put the money on the counter. It was then that I turned my head to look down for him, and noticed he was not there. He wasn't there so I looked around. It took maybe 3 or 4 seconds to begin to feel worried and to start asking the people standing on the line behind me waiting to pay if they had seen a little boy. Some of them looked around too. They shook their head. Not more than 5 seconds and I realized, Oh my God! They think he looks like me. I yelled. "I am looking for a five-year-old boy, he is bi-racial, he does NOT look like me." I don't have to tell you . . . I've told you so many times. You know.

DAVID: Yes. I know.

JOHN: I live it over and over again. In the past six weeks since he disappeared, maybe eight hundred or nine hundred times. I can't stay in here. I gotta get out of here. I'll call you about picking up the rest of my stuff.

DAVID: When do you want to have the funeral?

JOHN: Never. I don't ever want to finalize this

DAVID: We have to.

JOHN: Why?

DAVID: Dr. Pearlman . . .

JOHN: (Incredulous.) The therapist!!??

DAVID: I think it helps me.

JOHN: Well, good for you.

DAVID: I'm not like you. You have your work to . . .

JOHN: What? What!

DAVID: Relax! I'm just saying you work with your hands. It's physical . . . construction . .

It's like going to the gym. Or I don't know . . . yelling.

JOHN: OK, I see what you mean

DAVID: You didn't have to . . . you can . . . not speak to anyone if you don't want to. I have to speak to people all day. On the phone. "How are you?" "How are you?" If you say "Fine." They're like, "Really?" In the halls. In the elevator.

JOHN: I know.

DAVID: You don't! Jerry Johnson calls me in. He's sitting at his desk. He doesn't even get up. He looks at me and I can see in his eyes, I'm just a (Beat) you know. Maybe I'm reading into it, I've become so paranoid. Anyway, he doesn't even ask me to sit. I mean I'm a partner, he doesn't even say "David, please sit down." No. He says "I feel for you, but people take one look at you and they know something is wrong. We can't have that in our halls you know. Company morale. I say "I'll work on my demeanor, Sir." He says "Good, you should be over this by now anyway." And I want to say "Don't you tell me what to be feeling. You don't know what I feel. You don't know what I go through every morning to get to this stupid office. How I stand and wait for the bus. You know how that was our thing? I'd drop him off at school and then get back on and go . . . Now, every morning, I see all the people, all the mothers all the kids every one we used to see. They look up and their eyes touch me, and they look down expecting to see Billy, and of course he's not there. Six weeks and they still forget every morning. But then I forget every morning that I'm going to see them too. I wouldn't even get on the bus if I remembered. I feel their pity reaching out to try to curl around me like a boa constrictor and squeeze me but I smile back when instead I feel like snarling and baring my teeth and attacking them for still having their children. These are people who mean me no harm. I know they loved Billy and they care about me but I hate them. (Beat.) I can't believe we're here. I can't believe what we saw in there just now (Beat.) His body . . .

cigarette burns . . .

JOHN: That f*****! That f***** asshole!

DAVID: And you were the last person to see him. And I am furious that I let you take him shopping.

JOHN: Wait a minute, you LET me take him shopping?! He was my son. You didn't have to let me take him anywhere.

DAVID: He was my son and you could tell.

JOHN: What are you like two!??? (Beat.) It's terrible what I feel in my heart right now, David. And to know that you feel this . . . still? (Dialogue overlaps.)

DAVID: I can't help . . .

JOHN: 'Cause he didn't just kill Billy. He killed everything. He killed us. (Long beat encompasses the "us") I wanna kill Robert Pierce. I want to hurt him like he hurt Billy. Worse. I want to keep him alive long enough so he'll suffer. Every time he looks like he's going to succumb, I'll back off. Let him come down a little. Let him feel hope that I'll stop, let him catch a breath and that's when I'll come back twice as hard. I'll burn him once the first time, I'll burn him three times the second time. Then I'll start on his knuckles. I'll go at 'em, one at a time with my drywall hammer. I want to hurt him worse than he hurt my little boy. Every single thing he did to Billy, I'm gonna do three or four more times back to him.

DAVID: God, John.

JOHN: This is what I'm thinking David, once the trial begins we figure out when they're moving him, how they're moving him. You got connections with the courthouse . . . so we get him for what he did to our little boy. (Long beat.)

DAVID: You would do that?

JOHN: (Beat.) Yeah. I think so. (Beat.) I think I could.

DAVID: I feel numb. I just feel . . . numb. (Beat.) I don't believe you would. You're not that kind of person. (Long beat.)

JOHN: Not before, but now I know what it feels like . . .

DAVID: I know, but still . . .

JOHN: (Long beat.) Yeah. But I mean you know . . . I don't think . . . I really could . . . No.

DAVID: No.

CHILD'S VOICE: Daddy! (David and John simultaneously turn towards the door.)

TOGETHER: Billy! (They both laugh: shocked, embarrassed, overwhelmed.)

JOHN: I guess . . . some kid . . . Oh my God!

DAVID: Oh my God!

JOHN: Every time I hear that . . . word . . .

DAVID: Yes. (Long beat.)

JOHN: We didn't even know if he'd be mine or yours . . .

DAVID: I know

JOHN: He was perfect though, right? He was perfect. He looked like you spit him out. Every time I saw the two of you walking down the street together. It took my breath away. It took my breath away

DAVID: Whenever he got upset, he wanted you - his Daddy John. (David turns towards John. John turns away from him and looks towards the door.)

JOHN: OK . . . (Long beat; John goes to the doorway.) It's almost like you can feel him.

DAVID: Yes. (Beat.) I don't want to leave him in there.

JOHN: I don't even want him to be in there.

DAVID: I know. (After a long beat, David makes a physical gesture towards John. Something simple and non-sexual but with ramifications of the possibility of something beyond this moment. Lights slowly fade to black.)
```

---

## IC-1011: The Hoboken Chicken Emergency

- Title: The Hoboken Chicken Emergency
- Author (byline): D. Manus Pinkwater
- Work: Not specified
- Publisher: Aladdin
- Publication date as stated: Sept 2007
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 2, NARRATOR 1, NARRATOR 2, MOM, FISH GROCER, INDIAN SPICE GROCER, TOGETHER, PROF MAZZOCCHI, ARTHUR, CHICKEN, ACTOR 1, RADIO NEWSCASTER, DR. HSU, MAYOR, TOWNSPERSON 1, TOWNSPERSON 2, TOWNSPERSON 3, HENRIETTA
- Teaser before the introduction: Yes
- Spoken words (computed): 1634
- Already set (do not supply): none

### Source block (context only)

```text
Author: D. Manus Pinkwater
ISBN: 978-1416928102
Publisher: Aladdin
Date (Month/Year): Sept 2007
```

### Introduction (context only: never use it for content warnings)

```text
TOGETHER: The Hoboken Chicken Emergency by D. Manus Pinkwater
```

### Performance text (classify this)

```text
Suggested Roles: ACTOR 1: Narrator 1, Mom, Fish Grocer, Professor Mazzocchi, CHICKEN/Henrietta, Dr. Hsu

ACTOR 2: Narrator 2, Indian Spice Grocer, Arthur, Radio Newscaster, Mayor, Townspeople 1, 2 and 3

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

NARRATOR 1: (Pg 5) This was the first time [Arthur] had the job of getting the Thanksgiving bird, and he had messed it up.

NARRATOR 2: (Pg 2) Something had gone wrong at Murphy’s Meat Market. Somehow Poppa’s turkey reservation had gotten lost. Every turkey had some family’s name on it – none of them had the name Bobowicz.

MOM: (Pg 4) Maybe you’d better go back and get two chickens and a duck. (smiling) I’ll explain it to your father.

NARRATOR 2: Things had gone even more wrong than Arthur thought. When he got back to Murphy’s Meat Market, there wasn’t a single chicken in the place –

NARRATOR 1: no ducks either.

NARRATOR 2: He went to every store in town that might possibly have a bird. He went to a few stores that probably did not have birds – just in case.

FISH GROCER: This is a fish market! What makes you think we’d have turkeys or chickens, you silly kid!

INDIAN SPICE GROCER: This is an Indian spice store. Curry powder, we’ve got; mango chutney, we’ve got – birds we do not have.

NARRATOR 1: Arthur was getting depressed. He didn’t want to go home and tell his mother the bad news, [when] he noticed a card stuck in the window of an apartment house door:

TOGETHER: (in amazement and awe) PROFESSOR MAZZOCCHI / INVENTOR OF THE CHICKEN SYSTEM / BY APPOINTMENT.

NARRATOR 1: Arthur rang the bell.

NARRATOR 2: What did he have to lose?

PROF MAZZOCCHI: (from off stage - upstairs) You will not get me evicted! My brother owns this building! I am a scientist! If you people don't stop bothering me, I'll let the rooster loose again.

ARTHUR: (shouting) Do you have a chicken for sale? We need one to cook for Thanksgiving.

PROF MAZZOCCHI: What? You want to buy a chicken? Come right up! I have been waiting for years for someone to come to buy a superchicken. The only people who ever come here are neighbors to complain about my chickens. They don't want me to keep them. How much money did you bring?

NARRATOR 1: The old man went inside the apartment with Arthur's sixteen dollars. When he opened the door, Arthur heard a clucking sound, (Clucking sound) but not like any clucking he had ever heard -it was deeper, louder. (Clucking sound again, but deeper and louder)

PROF MAZZOCCHI: (returning with a superchicken on a leash) This is the best poultry bargain on earth - a medium sized superchicken - six cents a pound - here's your two hundred and sixty-six pound chicken, on the hoof. She'll be mighty good eating. Please don't forget to return the leash and collar. (ushering Arthur out the door and closing it behind him before Arthur can change his mind)

ARTHUR: (perplexed and looking from the chicken to the door to the leash and back again – then pounds on the door)

PROF MAZZOCCHI: (shouting through the door) No refunds!

ARTHUR: Don't you have anything smaller?"

PROF MAZZOCCHI: (shouting through the door) No refunds!

NARRATOR 2: The chicken tamely followed Arthur down the stairs as Arthur led it home and tied the leash to the bannister. Then he went in to prepare his mother.

MOM: That took a long time. Did you get a bird?

ARTHUR: I got a chicken. It only cost six cents a pound.

MOM: That’s very cheap. Are you sure there’s nothing wrong with it. Maybe it isn’t fresh.

ARTHUR: It’s fresh. It’s alive.

MOM: You brought home a live chicken?

ARTHUR: (starting to cry) It was the only one I could find. I went to all the stores and nobody had turkeys or chicken or ducks, and finally I bought this chicken from an old man who raises them in his apartment. (Mom heads for the door) Momma, it’s a very big chicken! (She opens the door)

CHICKEN: (Shifting from foot to foot, blinking) CLUCK! (mom closes the door and stands staring at it – long pause)

MOM: (in shock) There’s a two-hundred pound chicken in the hall. It’s wearing a dog collar.

ARTHUR: I’m supposed to return that. (Mom opens the door a crack and peeks out, closed the door, looks at Arthur, opens the door all the way and looks out at the chicken.) I thought we could call her Henrietta.

MOM: Put her in the kitchen and we’ll discuss it when you father comes home.

NARRATOR 2: That night the family had meatloaf for Thanksgiving dinner.

NARRATOR 1: [and even better] Poppa decided to let Arthur keep Henrietta. *****SCENE ******

NARRATOR 1: (Pg 11) Arthur got up early the day after Thanksgiving. The night before, while Henrietta was sleeping next to his bed, Arthur had made plans to teach her a lot of tricks.

ARTHUR: Henrietta! (no response – Arthur claps his hands) – Henrietta! Come here! (Henrietta looks at him and blinks) OK, just stay here by yourself (begins to walk away – Henrietta gallops after him, crashes into him and begins following Arthur around clucking) Heel, Henrietta, heel, girl.

NARRATOR 1: She was doing pretty well for a chicken who had never been trained before. Every now and then he would pat Henrietta on the back, and scratch her neck feathers.

(Arthur pantomimes these actions) She liked that.

NARRATOR 2: [But just then] a door opened to a house across the street and Bozo bounded across the street. Bozo was a big German Shepherd and he ran straight at Arthur and Henrietta! TRANSITION

ACTOR 1: To make a long story short . . . Henrietta runs away in a panic and ultimately has to be rescued from a tree by the fire department.

ACTOR 2: Unwilling to deal with a giant chicken running wild through the streets, Father makes Arthur return the bird to Professor Mazzocchi.

ACTOR 1: Henrietta, feeling unloved and unwanted by anyone, escapes and begins to terrorize the town.

ACTOR 2: Arthur knows it is up to him to do something – after all Henrietta was his chicken even if his dad made him give her back.

NARRATOR 1: (Pg34) Arthur arrived outside Professor Mazzocchi’s apartment house just in time to see the professor locking the doors of a big green truck. AUGIE'S TRUCK RENTAL, it said on the side. From the muffled clucking and screeching, Arthur could tell that all the professor's experiments were inside.

ARTHUR: Professor Mazzocchi! Are you going away?

PROF MAZZOCCHI: Do you know what happens to people when one of my experiments gets loose? They go crazy! One time they burned down my house! Burned it right to the ground!

ARTHUR: Henrietta is wandering around the streets of Hoboken, all alone. She must be frightened, and cold, and hungry. Don't you care what happens to her?

PROF MAZZOCCHI: Of course I care, but when you've been a mad scientist as long as I have, you learn that some things are more important than others. Most important, right now, is for me to get out of town with all my experiments. If the news gets around that I am responsible for a very large chicken loose in the streets, people will start acting crazy.

NARRATOR 2: Professor Mazzocchi started the engine, and the big green truck rumbled away.

****** SCENE ******

RADIO NEWSCASTER: (Pg 46) AND NOW, A BIZARRE NEWS STORY FROM HOBOKEN, NEW JERSEY . . . LAST NIGHT, MORE THAN FIFTY PEOPLE REPORTED GIANT CHICKEN SIGHTINGS TO THE POLICE, THE F.B.I., AND THE WHITE HOUSE . . . THE CHICKENS, WHICH STAND ABOUT FIFTEEN FEET HIGH, ARE ESTIMATED TO WEIGH ABOUT ONE THOUSAND POUNDS. THERE HAVE BEEN NO REPORTS OF INJURIES, OR ATTACKS ON PERSONS . . . THIS RADIO STATION WILL KEEP YOU POSTED ON THE CHICKEN CRISIS IN HOBOKEN.

NARRATOR 1: (Pg 51) The whole town was chicken-panicky. The police department's switchboard received thousands of calls from frightened people.

NARRATOR 2: The mayor's office was full of citizens demanding protection from the giant chickens.

NARRATOR 1: Schools were closed. People were afraid to go shopping, to go to work, to step outside their doors.

NARRATOR 2: Special police chicken squads were sent to cruise the streets in cars. Helicopters buzzed over the rooftops, looking for chickens.

NARRATOR 1: Men stayed home from work to protect their families. Neighboring towns sent fire trucks, and teams of veterinarians to help in the chicken emergency.

RADIO NEWSCASTER: THE GIANT CHICKEN WAS SEEN EMERGING FROM THE CLAM BROTHERS SEAFOOD RESTAURANT AT FOUR-FIFTY-SEVEN THIS MORNING. HOBOKEN POLICE OFFICERS SMITH AND MOONEY GAVE CHASE IN THEIR SQUAD CAR, AND CORNERED THE CHICKEN ON COURT STREET, NEAR THIRD. THE CHICKEN THEN KICKED A HUGE DENT IN THE LEFT FRONT FENDER OF THE SQUAD CAR AND RAN OFF. TRANSITION

ACTOR 1: For 5 days, Henrietta terrorizes the town: She hijacks a potato chip truck, kicks over a fire-hydrant, and bends the flagpole outside the senior high school.

ACTOR 2: Chicken traps are set, but there is no relief from the chicken situation.

ACTOR 1: The mayor spent sixty-thousand dollars of the town's money trying to resolve the Hoboken Chicken Emergency and nothing worked.

ACTOR 2: Finally, PROF Maz, feeling guilty, sends a specialist to help Hoboken:

ACTOR 1: Dr. Hsu, poultry locator, arrives to meet with the Mayor.

DR. HSU: (Pg 72) Chickens are very sensitive birds. It is very easy to hurt their feelings. When their feelings are hurt, they become unpleasant, anti-social. A perfectly sweet chicken can become a bitter destructive bird, if it feels that it is unwanted.

MAYOR: Do you think Henrietta is a chicken like that? Do you think she feels unwanted, and that's why she's kicking over fire hydrants, and frightening the citizens

DR. HSU: I am sure of it. I have found out that Henrietta was, for a short time, the personal pet of a young boy in this town. His name is Arthur Bobowicz. (Arthur smiles at the audience and waves) Young Arthur and Henrietta got to be great friends. Henrietta got into a tiny bit of trouble, and Arthur's parents insisted he take Henrietta back . . . (Arthur is sad, pantomimes putting the collar and leash on Henrietta and walking her back to Prof. Mazz.) Henrietta missed Arthur, and set out to look for him. Every time people saw her, they screamed and ran away. (Actor 2 acts out this out and Dr. HSU responds to the screaming by putting his hands over his ears) They called the police, and the police chased her. She felt unloved. Think if it happened to you. You'd be angry too. We [have to] encourage the citizens of Hoboken to have a friendly attitude toward chickens. We will ask them to wave and smile when they see Henrietta, instead of screaming, or calling the police, or throwing things at her.

NARRATOR 2: The following day posters were printed. They showed a boy, looking very much like Arthur Bobowicz, with his arm around a big chicken.

NARRATOR 1: The Goodyear blimp was sent for, and it cruised back and forth over Hoboken, towing a large banner which read CHICKENS NEED YOUR LOVE. At night, the message was flashed in electric lights.

NARRATOR 2: The television stations cooperated. There were special panel discussions on the late night talk-shows, in which psychologists and guidance experts told about chickens' need for love and approval. So that they wouldn't upset Henrietta, big white chickens were painted on all the police cars. (Actor 1 assumes the persona of Henrietta and responds to these townspeople with apprehension that slowly changes to a relaxed co-existance)

TOWNSPERSON 1: Nice chicken. Nice chicken. (Henrietta starts to come closer – then runs)

TOWNSPERSON 2: Nice Henrietta. Nice chicken. Nobody’s going to hurt you. (Henrietta allows the townsperson to pet her beak)

TOWNSPERSON 3: Good morning, Henrietta How ya’ going? (Henrietta clucks contentedly and nuzzles the townsperson affectionately)

NARRATOR 1: [Soon] people couldn't remember why they had been afraid of Henrietta. She seemed to be a very pleasant, well-behaved chicken. They liked her.

TOGETHER: [The Hoboken Chicken Emergency was over]

HENRIETTA: (Pg 8) (Shifting from foot to foot, blinking) CLUCK!
```

---

## IC-1012: How to Bargain with a Dragon

- Title: How to Bargain with a Dragon
- Author (byline): R. L. Stine
- Work: The Haunting Hour, Pgs 41-47
- Publisher: HarperCollins
- Publication date as stated: Aug 2011
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR 2, NED, MARGOLIN, GREGORY, SIR DARKWIND, NARRATOR 1, ULRICK
- Teaser before the introduction: Yes
- Spoken words (computed): 1283
- Already set (do not supply): none

### Source block (context only)

```text
Author: R.L. Stine
Book: The Haunting Hour, Pgs 41-47
ISBN: 978-0062106919
Publisher: HarperCollins
Date (Month/Year): Aug 2011
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: This story begins with a question: What if dragons were real?

ACTOR 2: In literature and movies, dragons are fierce and majestic; ugly and beautiful; and much more intelligent than dinosaurs.

ACTOR 1: Dragons have been a part of storytelling and mythology for centuries.

ACTOR 2: Remember The Jabberwocky?! Lewis Carroll’s “ferocious dragon with jaws that bite, claws that clutch, and great eyeballs of fire.”

ACTOR 1: And who can forget Daenerys Targaryen? All she has to do is say “Dracarys” and her fire-breathing companions lay waste to entire armies and cities.

ACTOR 2: Now, I know dragons never existed, but the ones I battle in Dungeons and Dragons – seem mighty real to me!

ACTOR 1: But what if they did exist? Ned certainly believes they do. He’s on a terrifying quest to face the fiercest dragon of them all!

ACTOR 2: Roll for initiative, Ned! (rolls dice) 17!

ACTOR 1: How to Bargain with a Dragon

ACTOR 2: from The Haunting Hour by R.L. Stine
```

### Performance text (classify this)

```text
Suggested Roles: Actor 1 – Narrator 1, Ned, Margolin Actor 2 -- Narrator 2, Gregory, Sir Darkwind, Ulrick (the Dragon)

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO

NARRATOR 2: (Pgs 41-47) On a summer day long ago, when birds as big as clouds flew the skies, a boy named Ned journeyed through leafy forests and over green, grassy hills. (Ned whistles while he walks) Soon he would be meeting Sir Darkwind, the greatest Dragon Master in the kingdom. Ned had long dreamed of this day. Through the trees, he heard the dragons in Sir Darkwind’s stable. (dragon noises, Ned stops whistling an appears intimidated) And Ned wondered which would prove more fierce and menacing—the dragons or the Dragon Master?

NED: (murmuring to himself) Courage. Be strong and brave. Or you will never reach your goal. (takes deep breath, then a step and, shielding his eyes he looks up . . . way up)

NARRATOR 2: A tall stone wall at least four times as tall as Ned rose up like a gleaming mountain in the afternoon sun. Ned gazed in amazement at the faces staring back at him from above the top of the wall. Broad creature faces on long, scaly necks. Black eyes as big as plums, staring from deep sockets. Ancient, long-toothed faces, craggy and lined with wisdom—and sadness.

NED: Dragons!

NARRATOR 2: Gazing at the amazing creatures, Ned remembered the Sorcerer’s stories of how the dragons had once moved freely around the kingdom.

MARGOLIN: Do not be fooled into thinking they are like other animals. Their wisdom is as big as their size. Why are their eyes so sad? Because they have seen everything.

NED: (cupping his hands around his mouth and shouting) Sir Darkwind! Sir Darkwind, a humble peasant boy wishes to speak with you. (a door creaks open)

GREGORY: (from the doorway in a high, boyish voice) What do you want?

NED: I have come to see the great Dragon Master. To ask a favor.

GREGORY: I am Gregory, Sir Darkwind’s servant. Sir Darkwind does no favors.

NED: (swallows) I bring the best wishes of the great Sorcerer Margolin. If Sir Darkwind would come outside and give me a moment—

GREGORY: (sneering) We don’t know any sorcerers, and Sir Darkwind only comes out of his house to whip the dragons -- keep them in their place.

NED: He never leaves his house?

GREGORY: No, he has too many enemies. (dragons growl and groan)

SIR DARKWIND: (deep voice bellows offstage) Go away! You are upsetting the dragons! (he steps to the doorway)

NARRATOR 1: Sir Darkwind was the cruelest man in the kingdom. Even the Sorcerer Margolin, with all his powerful magic, had feared him.

NED: (drops to his knees and bows his head) Are you the great Dragon Master? I am a humble peasant boy, grand sir. I come to beg for work. I was apprenticed to the Sorcerer Margolin, but after Margolin had a terrible argument with another sorcerer, they both suddenly vanished.

SIR DARKWIND: Good riddance! The world doesn’t need sorcerers. A good strong whip is the only magic I need! (cracks his whip) These are the last dragons -- The last in the world.

NED: (fearfully rises) I would be honored to help tend to them.

SIR DARKWIND: You would swing the whip to help teach them their manners? (cracks his whip; dragons growl and groan)

NED: No, sir. But—

SIR DARKWIND: What then is your bargain? All of life is a bargain. So what bargain do you wish to make with me?

NED: I have no answer. I offer myself as a humble worker.

SIR DARKWIND: I have a bargain for you. There is one dragon still roaming free. One dragon not in my collection. And I want them all! All! (cackles maniacally) Bring me last free dragon and I will make you my apprentice.

NED: Capture a dragon? But how? I have no weapon to use against a mighty dragon!

SIR DARKWIND: You must use your wits, boy. The last free dragon is called Ulrick. It lives in a cave on top of Stone Hill. (exit, slamming the door)

NARRATOR 1: Stone Hill, a steep-sloped mountain of smooth gray rock, led to a high cliff. Deep caves were cut into the sides of the hill. No one explored those caves. People were afraid of the fierce creatures that lived inside.

NED: (walking through the forest toward Stone Hill) What weapon can I use to battle a dragon? It will have talons a foot long and teeth the size of tree stumps. How can I make a bargain with a dragon like that?

NARRATOR 2: By the time Ned reached the top of the hill, his heart was thudding and his legs felt heavy as lead. (Ned struggles to catch his breath) He gazed at the cave opening. Enormous bones, bleached white by the sun, were strewn at the entrance. (a bellowing roar from deep in the cave)

NED: (to himself) I have no choice. I have to go through with this. (long, deep breath, then he yells) Ulrick—my name is Ned, and I have come to see you!

NARRATOR 2: The ground shook as a giant creature burst out and rose over Ned. A dragon bigger and more fierce than any in Sir Darkwind’s collection. Leathery wings flapped furiously on its back. Hot yellow drool splashed from its open maw and sizzled on the ground.

ULRICK: (bellowing) WHAT DO YOU WANT?

NED: (trying to shield himself with both hands) You—you talk?

ULRICK: Of course! All dragons speak when there is something to say!

NED: (terror fading, cautiously) Ulrick, why do you stay by yourself up here? Are you not lonely? Why don’t you join the other dragons down below?

ULRICK: (bitterly) Do you know anything about the Dragon Master, Ned? All my brothers and sisters used to roam free, in peace. We are no threat to humans. We eat only the Gorsel bushes. The great Dragon Master destroyed all the gorsel bushes except his own! The dragons had a choice—starve or be captured. As soon as the dragons followed him home, Sir Darkwind clipped their wings. (anger growing) He whips them and keeps them penned up. He charges a fee to see them. And he forces the dragons to roar and battle each other for the crowds. (roars)

NARRATOR 1: The mighty dragon roared and raged.

ULRICK: You want to capture ME and add ME to Sir Darkwind’s sad collection? NEVER! NEVER!

NED: NO! WAIT! PLEASE! NOOOOOO!

NARRATOR 2: And then the dragon lifted him easily off the ground. (Ned thrashes and squirms) The dragon tilted its head back to swallow him.

NED: WAIT! I’LL MAKE YOU A BARGAIN! (dragon pauses, turns his head and listens as Ned whispers) ****** The Next Morning – Sir Darkwind’s castle *****

GREGORY: (empties a water bucket into the dragons’ trough, he hears a sound behind him and let’s out a startled cry) D-D-D-Dragon! Sir Darkwind! Sir Darkwind! A dragon approaches!

NARRATOR 1: An enormous dragon was lumbering toward Sir Darkwind’s house, swinging its head from side to side, wings fluttering on its back.

SIR DARKWIND: (rushing to the door) It is Ulrick coming to join the others! (laughs cruelly) Ulrick probably had the boy for breakfast!

GREGORY: But then why has the dragon come here?

SIR DARKWIND: (giving Gregory a hard push) Go see at once—while I wait in the safety of the house.

GREGORY: (legs trembling, approaches Ulrick and shouts up to him, voice cracking with fear) Ulrick—the Dragon Master demands to know: Why have you come?

NARRATOR 1: With a sudden motion the huge dragon swung down its head. (Gregory gasps and leaps back) And then slowly, very slowly, the dragon opened its massive jaws.

GREGORY: (peers inside the dragon’s mouth and moans) Oh, nooooo!

NARRATOR 1: He saw the boy’s head inside the dragon’s mouth. The head, eyes shut, rested on the creature’s fat red tongue.

GREGORY: (shouting) You have eaten him! You have eaten the boy! (he spins around) Sir Darkwind! You must come and see this! You must come at once! (faints)

NARRATOR 1: The Dragon Master cautiously stepped out of the house and strode up to the dragon. He saw the boy’s head, dark hair matted wetly to his forehead. And saw the boy’s peacefully shut eyes.

SIR DARKWIND: (defiantly) Did you think that would shock me? You have wasted your time, Ulrick! (cracks his whip)

NED: (from his death pose, he pops up from the dragon’s mouth, brushing back his hair and wiping dragon drool from his smock) I do not think so. I knew this would get you out of the house!

SIR DARKWIND: (eyes wide with surprise) How—how have you done this, boy?

NED: I made a bargain with the dragon, just as you instructed me.

SIR DARKWIND: And now the dragon is mine?

NED: Not quite. That isn’t the bargain. You see, before the Sorcerer Margolin disappeared, he taught me many of his spells. I’m going to show you one of my favorites. (waves his hands and mumbles strange-sounding words)

NARRATOR 2: And the Dragon Master began to change. His face sank into his body. Leafy limbs sprouted all around him. And bright-red berries popped out around the leaves. The spell had worked! Ned had turned Sir Darkwind into . . . a Gorsel bush.

NED: (to audience) My mission was to destroy the Dragon Master and free the dragons. But first I had to trick him into leaving the house! As you can see, I have succeeded.

SIR DARKWIND: (waves his leafy arms, and makes terrified noises)

ULRICK: You have kept your bargain with me. How long will your spell last?

NED: It doesn’t really matter—does it?

ULRICK: No, not really. (smiling a huge toothy grin) [As I told you before] . . . We eat only the Gorsel bushes. (takes a huge bite of Sir Darkwind)
```

---

## IC-1013: How to be a Supervillain

- Title: How to be a Supervillain
- Author (byline): Michael Fry
- Work: Not specified
- Publisher: Jimmy Patterson
- Publication date as stated: May 2017
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 1, ACTOR 2, VICTOR, DAD, MOM, THE SMEAR, DSV WORKER, DR. DEPLORABLE, NAP BOY, THE WHINER, SMELLY FEET
- Teaser before the introduction: Yes
- Spoken words (computed): 1268
- Already set (do not supply): none

### Source block (context only)

```text
Author: Michael Fry
ISBN: 978-0316318693
Publisher: Jimmy Patterson
Date (Month/Year): May 2017
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: How to be a Supervillain ACTOR 2: by Michael Fry
```

### Performance text (classify this)

```text
Suggested Roles:

ACTOR 1: Victor, Mom, DSV Worker,

ACTOR 2: Dad, The Smear, Dr. Deplorable, Nap Boy, The Whiner, Smelly Feet

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

VICTOR: (Prologue) My parents fight, A LOT. (reacts to audience) Wait. No. Not each other. They fight other people . . . for a living. My parents are supers. Supervillains, to be exact. Meet Rupert . . .

DAD: (poses menacingly; squints as if shooting laser from his eyes) The Red Death Ray!

VICTOR: And Olivia Spoil

MOM: (intense karate moves)

VICTOR: Otherwise known as . . . The Spoil Sports. I know. Pretty lame. But it works for them. Not so much for me. My name is Victor Spoil. I am 12-years-old and I was raised to be bad. (hangs his head) Which is a problem... (looks up and smiles sheepishly) when you’re actually good.

VICTOR: (Chpt 2) I feel bad for Mom and Dad. They want what all supervillain parents want, (sincerely) They want me to grow up evil, with a burning desire to spread chaos and mayhem across the universe. But, instead, they got me – Tidy Boy. (Chpt 4) My parents were seriously disappointed.

MOM: (both are working on gadgets and/or firing ray guns) What are we going to do with him?

DAD: I have a plan!

MOM: Wait. You don’t mean . . .

DAD: Now that Victor’s out of school for the summer, he can take him on as an apprentice.

MOM: Seriously? He’s the only option?

DAD: The Walrus turned us down. Mr. Sour Cheeks said no. Even Infectious said “Are you kidding?” (pause) He’s our last hope. . . and he should be here any second. *Ding Dong* (door opens)

THE SMEAR: (elderly man, cubby and balding) The Smear is here!

VICTOR: (Chpt 5) (to audience) Not the Smear! Anyone but the Smear. There are hundreds of supervillains. Some are cool; some are okay; a few are seriously lame . . . but the Smear is just pathetic. He once brought a jar of grape jelly to a photon saber fight!

THE SMEAR: (uses fingers as photon sabers, the licks the jelly from them)

DAD: (Chpt 6) This is our son, Victor Spoil.

VICTOR: Seriously?! There’s no way I’m going to apprentice for you!

DAD: You want to be a civilian? Like Uncle Benny? He makes socks. For a living. Socks. All day. Every day. Socks.

THE SMEAR: (Chpt 7) Kid, you ever wonder why I am the lamest supervillain? (intensely) I stained Dr. Deplorable the most evil supervillain on the planet. We used to be partners. Until . . . the incident.

MOM: It was YOU?!

THE SMEAR: (Chpt 8) Dr. Deplorable and I worked together on a few battles against Mr. Awesome.

VICTOR: (impressed) The greatest hero on the planet!

MOM: (haughtily) I heard he has calf implants.

THE SMEAR: Dr. Deplorable had him cornered. I went in to blind him with a stain grenade... but it blew up in my hand . . .and on Dr. Deplorable’s face.

THE SMEAR: The DSV (Department of Supervillains) . . .

DSV WORKER: Number 4? Number 4!

THE SMEAR: . . . banished me for twenty years, but now I can make a comeback. I’m set to battle MegaMole in Des Moines in three days.

VICTOR: The Smear laid his hand on my shoulder. Not around my shoulder. Actually on my shoulder. It felt weird. (attitude shift) But warm.

THE SMEAR: (crouches to Victor’s eye level) It won’t be easy, kid. It won’t be glamorous and it will get messy. I can’t guarantee fame and fortune. But I can guarantee adventure. And pie.

VICTOR: Pie? I like pie. . .

THE SMEAR: Where do you think I get the base for all my smear stains?

VICTOR: (looks at shoulder, to audience) The Smear lifted his hand off my shoulder, leaving a hand-print stain. Normally, I’d freak out at something like that, but this time was different. This wasn’t a stain. This was a mark of distinction. The mark of a supervillain’s apprentice. ***** In Smear’s apartment*****

THE SMEAR: (Chpt 10) Pay attention, kid. There’s a lot to learn. (Victor takes out a notebook and pen) What are you doing?

VICTOR: Taking notes.

THE SMEAR: (grabs notebook and throws it away) First lesson: Supervillains NEVER take notes! (looking at a row of jars) First, let’s talk stains. rotten mango and tartar sauce chutney (hands jar to Victor, who is grossed out) Fizzy clamato, yak milk and Walrus Wart Frappuccino.

VICTOR: Can you pick up walrus warts at Costco? (scene shift to the garage)

THE SMEAR: Less talking, more [evil]! (opens garage door and proudly points out his equipment) Stain soakers *Splat! Splat!*

VICTOR: What about your eyes? Can you spray stains with your eyes?

THE SMEAR: (scoffing) No. That would be weird and really unsanitary. (he goes on with his list) . . . The Stain Mixer, The Flying Stain Bomber. (they get into the car)

VICTOR: (Chpt 11) Um, Mr. Smear? I was wondering about the stains. I mean, it’s just a stain. How is it going to stop a superhero?

THE SMEAR: (intense pause, then he shouts) THEY NEVER WASH OUT! My stains . . . are feared . . . across seven continents...

VICTOR: You’ve fought in Antarctica?

THE SMEAR: Don’t interrupt! My stains don’t just stain... they stick... they goo... they get in your ears, your eyes ... THEY GET IN EVERYWHERE!!!

VICTOR: Everywhere?

THE SMEAR: Everywhere! And the worst is yet to come. Batch 487B. A superstain. . .(ominously) that can stain a man’s soul. *Ker-pow!*

VICTOR: (Chpt 13) (to audience) An explosion rocked the Smearmobile like a toy! We were under attack! (to Smear) What was THAT!

THE SMEAR: GET DOWN! (smiling) Someone doesn’t want us in Des Moines.

VICTOR: Then the strangest thing happened. That dumpy, grumpy, middle-aged fake supervillain had suddenly transformed into . . . The Smear . . . (Chpt 14) pretty darn awesome!

THE SMEAR: Victor, stay down. Stain Soaker set to 11. Let’s roll! (action sequence) *BLAM! LEAP! POW!*

VICTOR: (dodging and ducking) I’d seen a lot, but I’d never seen this. . . The Smear didn’t hesitate. He took action. He was surprisingly limber for a large man.

THE SMEAR: (battle rages on) *BLAM-BLAM!* You’ll never take me alive or dead (launches rocket) Eat stain, you miserable bag of endoskeletal goo! (throws grenade)

VICTOR: (Chpt 15) It was touch and go, back and forth, until finally the smear got the upper hand...

THE SMEAR: (turns away from audience) Stain in the hole! *BOOM!* (Slow motion throws stain grenade at audience and turns to run)

DR. DEPLORABLE: (Chpt 29) (on loudspeaker) You’re done Smear! Say goodbye to this earthly coil and prepare to die (coughing and hacking)

THE SMEAR: I know that phlegm-clotted cough anywhere. That’s Dr. Deplorable! (Chpt 30) *Phew! Phew! Phew!* (bullets fly at Victor, who dodges and zigzags; the pair take cover behind a large boulder)

VICTOR: (terrified) Why is he shooting at us?!

THE SMEAR: (scared, but still The Smear) He’s mostly shooting at me! (pause) I’m the only one who knows his secret weakness. (they run to the Smear Mobile) With me out of the way, (Chpt 36) there’ll be nothing to stop [him] from TAKING OVER THE WORLD!

DR. DEPLORABLE: (Chpt 30) This isn’t over, Smear! I’ll be back! (coughing and hacking)

VICTOR: He should really have that cough checked out.

THE SMEAR: (Chpt 31) (as they drive away, he motions to audience) You see those fans over there? Their lives are predictable. No winners. No losers. Just socks. Lots and lots of socks. They need us. They need good and evil. Light and dark. Real winners and real losers. *******Transition – back in the garage preparing stain weapons*******

VICTOR: [So what’s Dr. D’s secret weakness?]

THE SMEAR: (long pause, not sure if he should share) Tickling.

VICTOR: (in disbelief) Dr. Deplorable’s secret weakness is that he’s afraid of being tickled?

THE SMEAR: It incapacitates him. And makes him laugh. He really hates to laugh.

VICTOR: I tried to keep a straight face. I failed. We both laughed. Hard. (Chpt 32) With each passing day, I felt more and more comfortable around the Smear. More comfortable than I ever felt back home.

THE SMEAR: (Chpt 35) Go get your costume on. It’s almost show time.

VICTOR: Tonight was a big night. I was excited. And nervous. Everything was going according to plan as I opened the door and discovered...

DR. DEPLORABLE: (Chpt 36) That’s it, Smear! You’re finished!

VICTOR: Dr. Deplorable was back! (races to hide behind Smear)

THE SMEAR: (circling each other) Finished?

DR. DEPLORABLE: Eliminated, erased, excised, whichever you prefer (ridiculous moves to ramp up his elbow lasers)

VICTOR: Why is he pointing his elbows at us?

THE SMEAR: (cocks gun) ELBOW LASER CATAPULTS!! Very nasty . . . (fires)

VICTOR: (Chpt 45) The battle had begun.

DR. DEPLORABLE: (Chpt 36) (Dr. D dodges then fires elbow laser, which suspends Smear in midair) *ZAP! WOOSH!*

THE SMEAR: (floating in mid-air, slow motion) WHOA!!!!

VICTOR: (to audience) This was a moment. A moment where you just had to go for it. No matter how silly, no matter how dangerous. NOW! (dives at Dr. D. and begins tickling him)

DR. DEPLORABLE: (laughing hysterically)

VICTOR: Gotcha! (more tickling)

DR. DEPLORABLE: (more laughing)

VICTOR: (rips off Dr. D’s book and tickles his foot)

DR. DEPLORABLE: (Chpt 48) (gasping dramatically) No!, Stop! This isn’t the way (breath) it’s supposed to end! (gives up in defeat)

VICTOR: (Chpt 36) Woah! It worked! (Chpt 47) SUPER TICKLING!

THE SMEAR: Who’s awesome now?!

VICTOR: (Chpt 49) His weakness turned out to be my superpower?

THE SMEAR: (sarcastically) Super-tickling! Who knew!

VICTOR: So, I’m THE TICKLER! (strikes a pose with an evil laugh)

THE SMEAR: (shrugs) You can pick your nose, but you can’t pick your superpower.

VICTOR: I still have one question. You’re a supervillain. You could have gone along with Dr. D. and taken over the world. That would have been the ultimate comeback! What stopped you?

THE SMEAR: It was you

VICTOR: Me?

THE SMEAR: You said I was awesome. Awesome people don’t take over the world. Because, they don’t need to. Because, you know, they’re awesome. I’m a supervillain. [You] helped me see it takes a hero to make a villain. (puts his hand over his mouth) Did I say that out loud?

VICTOR: You are a hero!

THE SMEAR: Language! You kiss your mom with that mouth?

VICTOR: (scene shifts alone on stage, he speaks to the audience) (Epilogue) I now battle on the Junior Super Circuit against other beginner supervillains and superheroes like Nap Boy…

NAP BOY: Is it snack time yet?

VICTOR: . . . and The Whiner

THE WHINER: Wah! I broke a nail!

VICTOR: (Chpt 34) . . . Worm Boy and Smelly Feet

SMELLY FEET: (puts his foot out to Victor’s nose and he reacts)

VICTOR: (Epilogue) But with Dr. Deplorable out of the way, the super battles are no longer winner takes all, but winner picks up the root beer!
```

---

## IC-1014: I Didn’t Know You Could Cook

- Title: I Didn’t Know You Could Cook
- Author (byline): Rich Orloff
- Work: Best American Short Plays 1996-1997 (ed Glenn Young)
- Publisher: Applause Theatre Books
- Publication date as stated: October 1997
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: JEROME, MARK, SETTING
- Teaser before the introduction: Yes
- Spoken words (computed): 2058
- Already set (do not supply): none

### Source block (context only)

```text
Author: Rich Orloff
Book: Best American Short Plays 1996-1997 (ed Glenn Young)
ISBN: 978-1557833174
Publisher: Applause Theatre Books
Date (Month/Year): October 1997
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: When conservative older brother Mark visits his paraplegic brother Jerome's house for dinner, he is shocked by two pieces of information –

ACTOR 2: his little brother is a great cook, and he is gay.

ACTOR 1: When Mark demands Jerome choose between being disabled and being gay, the ensuing conversation reveals how much the brothers have kept hidden from each other over the years.

ACTOR 2: Will Jerome be able to convince his brother to accept him for who he is?

TOGETHER: I Didn’t Know You Could Cook by Rich Orloff
```

### Performance text (classify this)

```text
JEROME: mid-20's, paraplegic, uses a wheelchair

MARK: near 30, his older brother

SETTING: The kitchen of a modest urban apartment. As the play begins, JEROME and MARK are at the kitchen table finishing dinner. JEROME has gone to some effort to make the meal setting look classy.

MARK: Anyway, so he pulls up to the stoplight, and he begins revving up his little Corvette engine, and I think, give me a break:

JEROME: Uh-huh.

MARK: I didn't get my Porsche to be macho or anything. I just like how it feels.

JEROME: Uh-huh.

MARK: But he keeps revving his engine, rhhm, rhhm, rhhmmmm, so, so right before the light changes, I roll down my window

JEROME: Yeah.

MARK: And I say, "I think you've done a wonderful job of compensating for a small penis."

JEROME: You didn't.

MARK: Light changed; I took off; left him in the dust.

JEROME: Wow, it's so cool they gave you a Porsche as a bonus.

MARK: Hey, if you ever want to get into sales. . .

JEROME: I think I'll stick with teaching.

MARK: Well, if you ever want me to help. After all, what's a brother for?

JEROME: Thanks. Not that I could drive one, anyway.

MARK: I'm sure they could adjust it.

JEROME: I'll stick with my Ford. We've developed a very intimate and trusting relationship.

MARK: You know, in a just world, they'd give teachers cars as bonuses.

JEROME: That'll be the day.

MARK: [Finishing eating.] This was delicious, Jerome. Absolutely delicious.

JEROME: I'm glad you liked it.

MARK: I'm really impressed. I didn't know you could cook.

JEROME: Millions of people can cook, Mark. Maybe billions. Would you like some dessert? It's chocolate mousse pie. Made it from scratch.

MARK: Sorry. No room.

JEROME: You don't need room for chocolate mousse pie. It just fills the crevices around the food you've already eaten.

MARK: Besides, I, I probably should be heading back to the hotel.

JEROME: It's early.

MARK: I know, but I have another meeting first thing in the

JEROME: You know - you know how long it's been since we've spent any real time together?

MARK: Six months?

JEROME: Five years.

MARK: Well, we've talked the last hour, haven't we? [PAUSE} Hey, Mom sent me that article about you in the paper.

JEROME: About the disabled schoolteacher all the third graders adore?

MARK: It was a good article.

JEROME: It was your generic "Let's admire the handicapped" piece. They just filled in the blanks with my name.

MARK: Nobody writes about me.

JEROME: Look, it was a fine article; I, I just don't like being written up because I can do what people assume I can't do. If they were honest, the piece would have been titled, "Local Crip Transcends Expectations."

MARK: Well, I liked the piece. And even if this isn't... correct, I'm really impressed by how well you've learned to manage on your own.

JEROME: And I'm impressed by how well you've learned to manage on your own, too, Mark.

MARK: All I mean is, well, I never thought you'd move out and live on your own. I mean, I knew you could. I knew you could do anything you put your mind to. I'm sorry if that bugs you, but it's true.

JEROME: I haven't done anything special.

MARK: I'm not sure I could have done what you've done.

JEROME: You just haven't been tested.

MARK: Still, to live alone when you're, well, you know-I think it's quite an accomplishment.

JEROME: Well, it's not like I'm completely alone.

MARK: Why? Is someone hiding in the bedroom or something?

JEROME: No, I mean friends. You know, friends.

MARK: I know, friends. The people you put in your Rolodex who aren't business connections.

JEROME: I also, um, well, I, there's, there's also one special friend.

MARK: No, really?

JEROME: Really.

MARK: Who?

JEROME: Oh, just. . . just someone special.

MARK: What's her name?

JEROME: Louie.

MARK: Well, if there can be an actress named Glenn Close, I guess there can be a woman named Louie.

JEROME: Louie's a man.

MARK: Oh, so he's just a friend.

JEROME: We're more than friends.

MARK: He's a good friend.

JEROME: We're more than good friends. We're lovers. Mark, I'm gay.

MARK: You can't be gay.

JEROME: Why not?

MARK: Because our father isn't henpecked and our mother isn't castrating.

JEROME: I'm still gay.

MARK: Are you sure you're not just doing this to be trendy?

JEROME: Mark, I'm a homosexual.

MARK: Well, I'm stunned. I'm really stunned. I never even knew you were sexual.

JEROME: Of course, I'm sexual.

MARK: Well, I thought, since the accident. . .

JEROME: Only my legs went limp; I'm one of the lucky ones.

MARK: Well. . . what do you know.

JEROME: To be honest, after the accident, I wasn't sure what I'd be able to do. At the rehab center, they didn't deal with our sexuality at all. At all. Then about six months later, I - I was watching this Mel Gibson movie, and he started getting real sweaty, and inside I started getting real excited, and outside I got real excited, too.

MARK: You're just doing this to be different, aren't you?

JEROME: Stop it! Look, I, I. . . I know you have trouble accepting things sometimes.

MARK: Like what?

JEROME: Like after the accident, when you visited from college and you offered me a hundred bucks if I took five steps.

MARK: I thought you needed encouragement.

JEROME: My spinal cord had been severed, Mark.

MARK: I know.

JEROME: It was physically impossible.

MARK: Look, I just thought you needed a little push to get better.

JEROME: I was getting better.

MARK: Everyone always coddled you.

JEROME: Dad never coddled me.

MARK: Dad never knew either of us existed. [This stops the conversation for a moment.]

JEROME: You're right.

MARK: Look, about this, this deciding to be gay thing, I . . . well, I just can't say I approve.

JEROME: Well then, I guess I'll just have to stop. Do you want to pretend I never said it?

MARK: It's not healthy.

JEROME: Mark

MARK: So I'm giving you a choice.

JEROME: What?!

MARK: You can be gay or disabled, but not both.

JEROME: But I am both!

MARK: Why can't you be satisfied just being disabled?

JEROME: I don't know. Maybe I'm just selfish.

MARK: Have you considered seeing a shrink about this?

JEROME: I've seen a shrink.

MARK: And what did he say?

JEROME: He said I should accept myself for who I am and stop worrying about whether or not I can please my older brother.

MARK: That sounds like something a shrink would say. Does the school know about this?

JEROME: I'm sure some people suspect, but no.

MARK: 'Cause I'm sure a lot of parents would get pretty upset.

JEROME: I know. Some of them are already nervous about me. I think they're afraid that with me as a role model, some of their kids will want to grow up to be disabled.

MARK: Maybe you think women won't be attracted to you because. . . you know.

JEROME: Mark, I've been with women. I wasn't attracted to them the way I am with men.

MARK: What do you mean, "been with?"

JEROME: I mean everything you think I could mean.

MARK: Were these women. . . you know?

JEROME: Disabled?

MARK: Yeah.

JEROME: Some were, and some weren't.

MARK: So then women find you attractive.

JEROME: Well, not an uncontrollable number. . .

MARK: And you've had sex with them.

JEROME: Some of them.

MARK: Well, that proves it. You're attracted to women.

JEROME: No! I, uh, the women were, oh, I don't know. I guess, I guess they were an experiment. I mean, I thought I might be gay even before the accident; actually, I was pretty sure of it. Still, I kept thinking, "Maybe if I meet the right woman..."

MARK: Why can't you just be disabled?!

JEROME: Look, damn it, I'm disabled and I'm gay, and that's the way it is, whether you like it or not or I like it or not or anybody in the world likes it or not. I didn't ask to be either. I always figured I'd get married someday and I'd walk down the aisle, and surprise, I'm not going to do either. I know I should be proud that I'm gay, and accepting that I'm disabled, and I suppose I am, but damn it, I've sure had to give up a lot of fantasies, a whole truckload of fantasies.

MARK: Look, if you've decided to be gay, that's your decision.

JEROME: Oh, yes. That's what it was, a decision. One morning I woke up and thought, "I wonder what I'll do today. See a movie? Go shopping? Turn homo? That sounds interesting."

MARK: Look, I'm sorry, I know this must be hard for you, but I just can't approve.

JEROME: I'm not asking you to approve; I'm asking you to, to accept.

MARK: Well, I'm not sure I can.

JEROME: Why, because I can't be who you want me to be?

MARK: What?

JEROME: It's like when you offered me that money to walk again. I think about that a lot. Was that for me or for you?

MARK: What do you mean?

JEROME: If I could walk again, then you wouldn't have to face the fact that I couldn't.

MARK: Look, Jerome, it's, you know, I'm sure you don't approve of everything I do

JEROME: I don't want your approval, Mark.

MARK: Then why did you tell me?!

JEROME: Because you're, you're my brotl1er.

MARK: I know, but

JEROME: Because you let me tag along with you when you went to get ice cream. Because you explained long division to me better than my teacher. Because you taught me how to play catch.

MARK: You threw like a girl.

JEROME: I don't think it was a sign.

MARK: You know, you could've given me a little hint along the way or something.

JEROME: Like what?

MARK: I don't know. You could've had copies of Playgirl lying around. . . It's just, it's a scary time.

JEROME: I'm careful. We're careful.

MARK: Still

JEROME: You sure you wouldn't like one piece of - [One of JEROME’s legs starts to spasm. It’s not significant, but it’s noticeable, and it lasts ten to fifteen seconds.] Uhp, there goes Old Faithful.

MARK: I thought you were taking medication

JEROME: I stopped years ago. I'm used to them; they don't bother me.

MARK: [Overlapping a bit.] Do you ever get spasms at school?

JEROME: Oh, sure. Not often.

MARK: How did the kids react?

JEROME: Oh, the first time, they were freaked out. Then I told them that whoever got the highest mark on the division quiz would get to ride me next time it happened. They got used to it after that.

MARK: You have a lot of guts, Jerome.

JEROME: I just do what I have to do, that's all.

MARK: You don't have any more surprises for me tonight, do you? You haven't joined a religious cult or anything. You're not a gay disabled Moonie, are you?

JEROME: And if I were?!

MARK: I don't know!

JEROME: Look, I, I . . . I know this must be hard on you. . .

MARK: Well, you know, it's like one moment you think the universe is one way; the next moment, it's another way.

JEROME: No, the universe is always the same. The only thing that changes is what you know about it.

MARK: This Louie guy, is he, you know. . .

JEROME: An Episcopalian?

MARK: No, is he, you know. . .

JEROME: Handicapped? Crippled? Physically challenged? Lame? Euphemism of the month?

MARK: I don't know why you're so angry.

JEROME: It's because I'm afraid that if I ever turn into one of those "nice" cripples, I'll end up on a Jerry Lewis telethon.

MARK: Hey. Look, you're going to do whatever you want anyway. You always did.

JEROME: I'm not your little brother anymore, Mark. There's nothing you have to protect me from.

MARK: From what I've read. You know, this is a real burden you're laying on me. A real burden. [JEROME just looks at MARK.] You're asking me for more than I can give. You've always done that. You want me to make everything okay.

JEROME: I don't

MARK: You wanted the bribe to work. You wanted me to be right. When you were laying in that bed, and everyone else was crying and going nuts, you looked at me, and maybe you don't remember, but God, you really wanted someone to believe you could walk. I didn't think you could either, but if you wanted me to think you could, I was willing to play that role.

JEROME: You didn't think .

MARK: Hell, no.

JEROME: I didn't know.

MARK: Does anyone else in the family know you're

JEROME: No, I thought I'd try it out on you first.

MARK: So how'd I do?

JEROME: You were -.. . [Starts to cry.] I. ..

MARK: Jerome. . .

JEROME: I'm sorry, I. . .

MARK: Hey, you don't have to

JEROME: I wanted to look so together tonight.

MARK: Hey

JEROME: I just wanted -

MARK: Calm down.

JEROME: I . . . I lied.

MARK: You're not gay?

JEROME: No, I mean, yes, I'm gay. I lied about... Yes, damn it, I, I want your approval, and I want your acceptance, and your love, and maybe I'm stupid, maybe I'm stupid for wanting so much from you. . . Consider it a disability.
```

---

## IC-1015: I Hate Hamlet

- Title: I Hate Hamlet
- Author (byline): Paul Rudnick
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Jan 1998
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ANDREW, BARRYMORE
- Teaser before the introduction: Yes
- Spoken words (computed): 1266
- Already set (do not supply): none

### Source block (context only)

```text
Author: Paul Rudnick
ISBN: 978-0822205463
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Andrew Rally, a young and successful television actor, relocates to New York when his series is cancelled. There he rents a marvelous, gothic apartment and is offered the opportunity to play Hamlet onstage in Central Park. Sounds like an actor’s dream, right?

ACTOR 2: Well, it would be if Andrew Rally didn’t hate Hamlet. His dilemma deepens with the entrance of John Barrymore's ghost, who arrives intoxicated and in full Shakespearean regalia.

TOGETHER: I Hate Hamlet by Paul Rudnick
```

### Performance text (classify this)

```text
The Characters: Andrew (30's) a popular television actor, and Barrymore (40-50) a ghost.

The Setting: Present. A brownstone apartment in New York

The Scene: When Andrew is offered the role of Hamlet in a New York production, his subsequent anxiety summons the ghost of John Barrymore. Here, these two very different actors discuss method and romance.

ANDREW: You're... him.

BARRYMORE: AM I?

ANDREW: You're... dead.

BARRYMORE: You know, occasionally I'm not truly certain. Am I dead? Or just incredibly drunk?

ANDREW: You're... Barrymore.

BARRYMORE: Yes. Although my father's given name was Blythe; he changed it when he became an actor, to avoid embarrassing his family. Your name?

ANDREW: (Still completely unnerved.) Andrew. Rally. It's really Rallenberg. I changed it, to avoid embarrassing ... the Jews.

BARRYMORE: (Surveying the premises.) Behold. My nest. My roost. (Indicating where things had been, perhaps with musical cues.) A grand piano. A renaissance globe. A throne.

ANDREW: You're dead! You're dead! What are you doing here?

BARRYMORE: Lad - I'm here to help.

ANDREW: Wait - how do I know you're ghost? Maybe you're just ... an intruder.

BARRYMORE: (Toying with him.) Perhaps. Cleverly disguised as Hamlet. (Andrew slowly sneaks up on Barrymore. He touches Barrymore's forearm. Barrymore is very nonchalant.) Boo.

ANDREW: But - I can touch you. My hand doesn't go through.

BARRYMORE: I'm a ghost, Andrew. Not a special effect.

ANDREW: But... ghosts are supposed to have powers! Special powers!

BARRYMORE: I just rose from the dead, Andrew. And how was your morning? Now shall I truly frighten you?

ANDREW: (Not impressed) I'm not afraid of you.

BARRYMORE: Shall I cause your flesh to quake?

ANDREW: (Very cocky) You couldn't possibly.

BARRYMORE: Shall I scare you beyond all human imagination?

ANDREW: Go ahead and try.

BARRYMORE: In just six weeks time, you will play Hamlet.

ANDREW: (Screams, Genuinely terrified.) Oh my God, you really are him, aren't you?

BARRYMORE: John Barrymore. Actor. Legend. Seducer. Corpse.

ANDREW: So- it worked. The séance. Felicia, her mother she brought you back, from over there.

BARRYMORE: Not at all. You summoned me.

ANDREW: I did?

BARRYMORE: As a link in a proud theatrical tradition. Every soul embarking upon Hamlet is permitted to summon an earlier layer. From Burbage to Kean to Irving - the call has been answered.

ANDREW: Wait - you mean you're here to help me play Hamlet? Because you did it?

BARRYMORE: Indeed.

ANDREW: Okay. Fine. Then the problem's solved. Because I'm not going to play Hamlet. No way. So you can just ... go back. To... wherever.

BARRYMORE: I'm afraid that's not possible.

ANDREW: Why not?

BARRYMORE: I cannot return, I will not be accepted, until my task is accomplished. Until you have... ANDREW and

BARRYMORE: Played Hamlet.

BARRYMORE: Precisely.

ANDREW: (Completely floored) Oh no. Oh my God. You mean, if I don't go through with it.

BARRYMORE: Then I'm here to stay. Within these walls. Trapped for all time, with a television actor.

ANDREW: Well, excuse me - I happen to be a very good television actor! And I don't need any dead ham bone to teach me about anything! Even if I were going to play Hamlet, which I'm not, I could do just fine! All by myself!

(Barrymore glares at Andrew. He removes a small, leather-bound copy of Hamlet from a pouch on' his belt, and tosses it to Andrew.)

BARRYMORE: Very well then: Hamlet. "To be or not to be."

ANDREW: That happens to be the speech I did at my auditions. And I got the part.

(Andrew tosses the copy of Hamlet back to Barrymore)

BARRYMORE: Proceed. (Barrymore reclines full length on the couch. Andrew, very full of himself, decides to show Barrymore a thing or two. He strides in, and turns his back. He hunches over.) Yes?

ANDREW: I'm doing my preparation.

BARRYMORE: Your... preparation.

ANDREW: Yes. My acting teacher taught me this. Harold Gaffney.

BARRYMORE: Harold Gaffney?

ANDREW: The creator of the Gaffney technique. Act To Win. I can't just do the speech cold, I have to get into character. I have to become Hamlet. I'm doing a substitution.

BARRYMORE: A substitution?

ANDREW: I'm thinking about something that really happened to me, so I can remember the emotion, and recreate it.

BARRYMORE: And what are you remembering?

ANDREW: It's a secret. Otherwise it won't work. Be quiet, I'm going to act.

BARRYMORE: Why do I feel we should spread newspapers about? I'm sorry, I shall be silent. Out of deep respect. Road closes - man acting. (Andrew turns, and moves D. facing out. He makes a small snuffling noise. He loosens up his shoulders, like a prizefighter shadow-boxing. He makes a few faces; he is being ultra-naturalistic, very Method. He makes an ungodly howling noise, then slaps his own face. He repeats this. Barrymore watches all this, appalled.) You know, Andrew, I am dead, and I shall be for all eternity. But I still don't have all day. (Andrew begins again. After a few lunges, he begins to speak. His forehead is furrowed with intensity; his speech patterns are reminiscent of a Brooklyn tough guy, in the Brando / DeNiro mode.)

ANDREW: To be ... nah. (He paces. A thought occurs.) Or ... not ... to ... be. That, that is the question. Whoa. Whether... (He holds up a hand.) Whether 'tis nobler ... huh ... in the mind, right ...

BARRYMORE: Wrong.

ANDREW: What?

BARRYMORE: No.

ANDREW: What "No?"

BARRYMORE: No.

ANDREW: No, what? No you disagree with my interpretation, no my interpretation wasn't clear, no you think I'm totally horrible?

BARRYMORE: Yes.

ANDREW: I'm horrible?

BARRYMORE: At the moment. What were you doing?

ANDREW: I was internalizing the role. I was finding an emotional through -line.

BARRYMORE: Why?

ANDREW: Why? So the character will come alive! So I'll achieve some sort of truth! (Barrymore rises, aghast.)

BARRYMORE: Truth! Your performance - the pauses, the moans, all that you clearly consider invaluable - it's utterly appalling. We must never confuse truth with asthma.

ANDREW: What?

BARRYMORE: I understand the impulse, God help me, I lived just long enough for the introduction of truth into the modern theater. As I recall, it accompanied synthetic fibers and the GE Kitchen Of Tomorrow.

ANDREW: Oh - so you just want me to ham it up.

BARRYMORE: I beg your pardon?

ANDREW: Hamming. Mugging. Over the top. Too big. Too

BARRYMORE: (With a grand gesture) Barrymore?

ANDREW: Well, you did have the reputation. As someone ... larger than life.

BARRYMORE: What size would you prefer? Gesture, passion these are an actor's tools. Abandon them, and the result? Mirror reality. Employ them, with gusto, and an artist's finesse, and the theater resounds! I do not overact. I simply possess the emotional resources of ten men. I am not a ham; I'm a crowd! Andrew, who is Hamlet?

ANDREW: A prince?

BARRYMORE: A star.

ANDREW: What?

BARRYMORE: A star. The role is a challenge, but far more an opportunity. To shine. To rule. To seduce. To wit - what makes a star?

ANDREW: Talent? (They exchange a look.) Sorry, I wasn't thinking.

BARRYMORE: A thrilling vocal range? Decades of training? The proper vehicle? (He shakes his head, no.) Tights.

ANDREW: Tights?

BARRYMORE: Tights. Where are you looking? Right now?

ANDREW: I am not!

BARRYMORE: Of course you are! The potato, the cucumber, the rolled sock - this is the history of Prince Hamlet.

ANDREW: You mean - you padded yourself?

BARRYMORE: Unnecessary. Even for the balcony. (Pause, as he gazes upward.) The second balcony.

ANDREW: So Hamlet should be ... horny?

BARRYMORE: Hamlet is a young man, a college boy, at his sexual peak. Hamlet is pure hormone. Ophelia enters, that most beguiling of maidens. Chastity is discussed.

ANDREW: Please, don't joke. Not about chastity.

BARRYMORE: Why? What?

ANDREW: I can't talk about it.

BARRYMORE: Oh dear . Your beloved? A problem?

ANDREW: A nightmare. Five months.

BARRYMORE: What?

ANDREW: Nothing.

BARRYMORE: Truly?

ANDREW: Necking at the Cloisters. Picnics on Amish quilts. Sonnets.

BARRYMORE: Not... sonnets.

ANDREW: Yes. And I've been faithful. Totally. It's unnatural. Do you know what happens when you don't have sex?

BARRYMORE: No.

ANDREW: Thanks.

BARRYMORE: But why?

ANDREW: Why her, or why me? Deirdre won't have sex because ... she's not sure. Because she's the victim of a relentlessly happy childhood, which she fully expects to continue.

BARRYMORE: And you?

ANDREW: Me? Why do I put up with all this? Why have I begged Deirdre to marry me, practically since the day we met? Because, in the strangest way, she's the most passionate woman I've ever met. Because when she sees a homeless person, she gives them a fabric-covered date book. Deirdre's just ... she makes me think that love is as amazing as it's supposed to be. She's romantic, which means she's insane. I know I love her, because I want to strangle her. Does that make sense?

BARRYMORE: Of course, A virgin goddess.

ANDREW: Please - don't encourage her.

BARRYMORE: She is to be treasured, and honored. I have known few such women in my sensual history. Perhaps only five hundred. They are the most adorable saints. But... there are ways.

ANDREW: (Eagerly) What?

BARRYMORE: No. It would be unthinkable.

ANDREW: What?

BARRYMORE: I could never condone such Casanova-like tactics. Such Valentino mesmerism.

ANDREW: Such Barrymore deceit.

BARRYMORE: (Mortally offended) Cad.

ANDREW: Yes?

BARRYMORE: Knave.

ANDREW: Please?

BARRYMORE: Hamlet!

ANDREW: No! Stop with that.

BARRYMORE: Hamlet, to cunningly expose his father's murder, feigns madness. To perfect the pose, he must spurn his beloved, the fair Ophelia. She is undone.

ANDREW: But doesn't she kill herself? I don't want to hurt Deirdre.

BARRYMORE: You'll be merciful.

ANDREW: No, that would be dishonest.

BARRYMORE: You would prefer, perhaps, some form of therapy? Continued discussion? What is the present-day epithet "communication?" That absolute assassin of romance?
```

---

## IC-1016: Inherit the Wind

- Title: Inherit the Wind
- Author (byline): Robert E. Lee and Jerome Lawrence
- Work: Not specified
- Publisher: Bantam Books, Inc.
- Publication date as stated: June 1982
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: DRUMMOND, BRADY
- Teaser before the introduction: Yes
- Spoken words (computed): 1764
- Already set (do not supply): none

### Source block (context only)

```text
Author: Robert E. Lee and Jerome Lawrence
ISBN: 978-0553269154
Publisher: Bantam Books, Inc.
Date (Month/Year): June 1982
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 2: Inherit the Wind is based on the furor that erupted in 1925 when Tennessee schoolteacher John Scopes (referenced here as Professor Cates) was prosecuted for introducing the subject of evolution into his public school classroom.

ACTOR 1: The resulting “Monkey Trial” pitted the orator and Biblical scholar William Jennings Bryant (Matthew Harrison Brady in this play- gesture to Actor 2) against the brilliant defense attorney Clarence Darrow (gesture to self - Mr. Drummond) in a courtroom confrontation that attracted worldwide attention.

TOGETHER: Inherit the Wind by Robert E. Lee and Jerome Lawrence
```

### Performance text (classify this)

```text
DRUMMOND: Your Honor, the court has ruled out any evidence as to scientific knowledge or the Darwinian theory. (There’s the glint of an idea in his eye) Would the court admit expert testimony regarding a book known as the Holy Bible?

(Listen for “unspoken” answer) Thank you. (With relish) I call to the stand one of the world’s foremost experts on the Bible and its teachings- Matthew Harrison Brady!

(BRADY sits, confident and assured. His air is that of a benign and learned mathematician about to be quizzed by a schoolboy on matters of short division.)

DRUMMOND: Am I correct, sir, in calling on you as an authority on the Bible?

BRADY: I believe it is not boastful to say that I have studied the Bible as much as any layman. And I have tried to live according to its precepts.

DRUMMOND: Bully for you. Now, I suppose you can quote me chapter and verse right straight through the King James Version, can’t you?

BRADY: There are many portions of the Holy Bible that I have committed to memory. (DRUMMOND crosses to counsel table and picks up a copy of Darwin.)

DRUMMOND: I don’t suppose you’ve memorized many passages from the Origin of Species?

BRADY: I am not in the least interested in the pagan hypotheses of that book.

DRUMMOND: Never read it?

BRADY: And I never will.

DRUMMOND: Then how in perdition do you have the gall to whoop up this holy war against something you don’t know anything about? How can you be so sure that the body of scientific knowledge systematized in the writings of Charles Darwin is, in any way, irreconcilable with the spirit of the Book of Genesis?

BRADY: Would you state that question again, please?

DRUMMOND: (Not angrily) All right. I get the scent in the wind. (He tosses the volume of Darwin on the counsel table) We’ll play in your ball park, Colonel. (He searches for a copy of the Bibl,. Without opening it, DRUMMOND scrutinizes the binding from several angles) Now let’s get this straight. Let’s get it clear. This is the book that you’re an expert on? (BRADY is annoyed at DRUMMOND’S elementary attitude and condescension.)

BRADY: That is correct.

DRUMMOND: Now tell me. Do you feel that every word that’s written in this book should be taken literally?

BRADY: Everything in the Bible should be accepted, exactly as it is given there.

DRUMMOND: I recollect a story about Joshua, making the sun stand still. Now as an expert, you tell me that as true as the Jonah business. Right? (BRADY nods, blandly) That’s a pretty neat trick. You suppose Houdini could do it?

BRADY: I do not question or scoff at the miracles of the Lord- as do ye of little faith.

DRUMMOND: If they say that the sun stood still, they must’ve had a notion that the sun moves around the earth. Think that’s the way of things? Or don’t you believe the earth moves around the sun?

BRADY: I have faith in the Bible! (Doggedly) The sun stopped.

DRUMMOND: Good. (Level and direct.) Now if what you say actually happened- if Joshua halted the sun in the sky- that means the earth stopped spinning on its axis; continents toppled over each other, mountains flew out into space. And the earth, arrested in its orbit, shriveled to a cinder and crashed into the sun. (Turning) How come they missed this tidbit of news?

BRADY: They missed it because it didn’t happen.

DRUMMOND: It must’ve happened! According to natural law. Or don’t you believe in natural law, Colonel? Would you like to ban Copernicus from the classroom, along with Charles Darwin? Pass a law to wipe out all the scientific development since Joshua? Revelations- period!

BRADY: (Calmly, as if instructing a child) Natural law was born in the mind of the Heavenly Father. He can change it, cancel it, use it as He pleases. It constantly amazes me that you apostles of science, for all your supposed wisdom, fail to grasp this simple fact. (DRUMMOND flips a few pages in the Bible.) The Bible satisfies me, it is enough.

DRUMMOND: It frightens me to imagine the state of learning in this world if everyone had your driving curiosity. (DRUMMOND is still probing for a weakness in Goliath’s armor. He thumbs a few pages in the Bible.) The book goes into a lot of “begats.” (He reads) “And Aphraxad begat Salah; and Salah begat Eber” and so on and so on. These pretty important folks?

BRADY: They are the generations of the holy men and women of the Bible.

DRUMMOND: Did people “begat” in those days about the same way they get themselves “begat” today?

BRADY: The process is about the same. I don’t think your scientists have improved it any.

DRUMMOND: In other words, these folks were conceived and brought forth through the normal biological function known as sex. What do you think of sex, Colonel Brady? I’m not asking what you think of sex as a father, or as a husband. You’re up here as an expert on the Bible. What’s the Biblical evaluation of sex?

BRADY: It is considered “Original Sin.”

DRUMMOND: (With mock amazement) And all these holy people got themselves “begat” through “Original Sin”? (BRADY does not answer. He scowls, and shifts his weight in his chair.) All this sinning make ‘em any less holy?

BRADY: (With dignity) Your Honor, I am willing to sit here and endure Mr. Drummond’s sneering and his disrespect. For he is pleading the case of the prosecution by his contempt for all that is holy.

DRUMMOND: I object, I object, I object.

BRADY: On what grounds? Is it possible that something is holy to the celebrated agnostic?

DRUMMOND: Yes! (His voice drops, intensely) The individual human mind. In a child’s power to master the multiplication table there is more sanctity than in all your shouted “Amens!”, “Holy, Holies!” and “Hosannahs!” An idea is a greater monument than a cathedral. And the advance of man’s knowledge is more of a miracle than any sticks turned to snakes, or the parting of waters! But are we now to halt the march of progress because Mr. Brady frightens us with a fable? (Thoughtfully, seeming to look beyond the courtroom) Darwin moved us forward to a hilltop, where we can look back and see the way from which we came. But for this view, this insight, this knowledge, we must abandon our faith in the pleasant poetry of Genesis.

BRADY: We must not abandon faith! Faith is the important thing!

DRUMMOND: Then why did God plague us with the power to think? Mr. Brady, why do you deny the one faculty which lifts man above all other creatures of the earth: the power of his brain to reason. What other merits have we? The elephant is larger, the horse is stronger and swifter, the butterfly is more beautiful, the mosquito more prolific, even the simple sponge is more durable!

(Wheeling on BRADY) Or does a sponge think?

BRADY: If the Lord wishes a sponge to think, it thinks.

DRUMMOND: Does a man have the same privileges that a sponge does?

BRADY: Of course.

DRUMMOND: (Roaring for the first time: stretching his arm towards CATES – his client) This man wishes to be accorded the same privilege as a sponge! He wishes to think!

BRADY: But your client is wrong! He is deluded! He has lost his way!

DRUMMOND: It’s sad that we aren’t all gifted with your positive knowledge of Right and Wrong, Mr. Brady.

(DRUMMOND strides to one of the uncalled witnesses seated behind him and takes from him a rock, about the size of a tennis ball. DRUMMOND weighs the rock in his hand as he saunters back toward BRADY)

DRUMMOND: How old do you think this rock is?

BRADY: (Intoning) I am more interested in the Rock of Ages, than I am in the Age of Rocks.

DRUMMOND: Dr. Page of Oberlin College tells me that this rock is at least ten million years old. (DRUMMOND opens up the rock, which splits into two halves. He shows it to BRADY) Look, Mr. Brady. These are the fossil remains of a pre-historic marine creature, which was found in this very county- and which lived here millions of years ago, when these very mountain ranges were submerged in water.

BRADY: I know. The Bible gives a fine account of the flood. But your professor is a little mixed up on his dates. That rock is not more than six thousand years old.

DRUMMOND: How do you know?

BRADY: A fine Biblical scholar, Bishop Usher, has determined for us the exact date and hour of the Creation. It occurred in the year 4004 B.C.

DRUMMOND: That’s Bishop Usher’s opinion.

BRADY: It is not an opinion. It is a literal fact, which the good Bishop arrived at through careful computation of the ages of the prophets as set down in the Old Testament. In fact, he determined that the Lord began the Creation on the 23rd of October in the Year 4004 B.C. at- uh, at 9 A.M.!

DRUMMOND: That Eastern Standard Time? Or Rocky Mountain Time? It wasn’t daylight-saving time, was it? Because the Lord didn’t make the sun until the fourth day!

BRADY: (Fidgeting) That is correct.

DRUMMOND: (Sharply) The first day. Was it a twenty-four-hour day?

BRADY: The Bible says it was a day.

DRUMMOND: There wasn’t any sun. How do you know how long it was? A normal day, a literal day, a twenty-four-hour day? (Pause. BRADY is unsure.)

BRADY: I do not know.

DRUMMOND: Isn’t it possible that first day was twenty-five hours long? There was no way to measure it, no way to tell! Could it have been twenty-five hours?

BRADY: (Hesitates- then) It is . . . possible . . .

(DRUMMOND’S got him. And he knows it! This is the turning point. From here on, the tempo mounts. DRUMMOND is now fully in the driver’s seat. He pounds his questions faster and faster.)

DRUMMOND: Oh. You interpret that the first day recorded in the Book of Genesis could be of indeterminate length. It could have been thirty hours! Or a month! Or a year! Or a hundred years! (He brandishes the rock underneath BRADY’S nose) Or ten million years!

(Both BRADY and DRUMMOND crane forward, hurling their answers not at the court, but at each other.)

BRADY: [You] want to destroy everybody’s belief in the Bible, and in God!

DRUMMOND: You know that’s not true. I’m trying to stop you bigots and ignoramuses from controlling the education of the United States! And you know it!

BRADY: How dare you attack the Bible?

DRUMMOND: The Bible is a book. A good book. But it’s not the only book.

BRADY: It is the revealed word of the Almighty. God spake to the men who wrote the Bible.

DRUMMOND: And how do you know that God didn’t “spake” to Charles Darwin?

BRADY: I know because God tells me to oppose the evil teachings of that man.

DRUMMOND: Oh. God speaks to you.

BRADY: Yes.

DRUMMOND: He tells you exactly what’s right and what’s wrong? And you act accordingly?

BRADY: Yes.

DRUMMOND: So you, Matthew Harrison Brady, through oratory, legislation, or whatever, pass along God’s orders to the rest of the world! Gentlemen, meet the “Prophet from Nebraska!”

BRADY: (Almost inarticulate) Please-!

DRUMMOND: (With increasing tempo, closing in) Is that the way of things? God tells Brady what is good! To be against Brady is to be against God!

BRADY: (Confused) No, no! Each man is a free agent-

DRUMMOND: Then what is Bertram Cates doing in the Hillsboro jail? Suppose Mr. Cates had enough influence and lung power to railroad through the State Legislature a law that only Darwin should be taught in the schools!

BRADY: Ridiculous, ridiculous! There is only one great Truth in the world-

DRUMMOND: The Gospel according to Brady! God speaks to Brady, and Brady tells the world! Brady, Brady, Brady, Almighty! (DRUMMOND bows grandly).

BRADY: The Lord is my strength-

DRUMMOND: What if a lesser human being- a Cates, or a Darwin- has the audacity to think that God might whisper to him? That an un-Brady thought might still be holy? Must men go to prison because they are at odds with the self-appointed prophet?

(BRADY is now trembling so that it is impossible for him to speak. He rises, towering above his tormentor- rather like a clumsy, lumbering bear that is baited by an agile dog)

DRUMMOND: Extend the Testaments! Let us have a Book of Brady! We shall hex the Pentateuch, and slip you in neatly between Numbers and Deuteronomy!

BRADY: (Reaching for a sympathetic ear, trying to find the loyal audience which has slipped away from him) My friends- Your Honor- My Followers- Ladies and Gentlemen

DRUMMOND: The witness is excused.

BRADY: (Unheeding) All of you know what I stand for! What I believe! I believe, I believe in the truth of the Book of Genesis! (Beginning to chant) Exodus, Leviticus, Numbers, Deuteronomy, Joshua, Judges, Ruth, First Samuel, Second Samuel, First Kings, Second Kings-

DRUMMOND: Your Honor, this completes the testimony. The witness is excused!
```

---

## IC-1017: Inside Al

- Title: Inside Al
- Author (byline): David S. Baker
- Work: High School Plays: A Collection of Three One-Act Plays
- Publisher: Samuel French, Inc.
- Publication date as stated: 1989
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: AL, INSIDE AL, JASON, BETH, AL/INSIDE AL
- Teaser before the introduction: Yes
- Spoken words (computed): 1363
- Already set (do not supply): none

### Source block (context only)

```text
Author: David S. Baker
Book: High School Plays: A Collection of Three One-Act Plays
ISBN: 978-0573622298
Publisher: Samuel French, Inc.
Date (Month/Year): 1989
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: There are about 764,000 people in the United States with cerebral palsy.

ACTOR 2: In many cases, people with cerebral palsy are labeled as mentally retarded because they are not able to effectively communicate with the outside world.

ACTOR 1: Their true being is locked inside a body that simply won’t work they way they want it to.

ACTOR 2: Such is the case of Alvin Theodore Willson – a 39 year old victim of cerebral palsy.

ACTOR 1: Inside Al by David S. Baker gives a voice to those too often silenced by the disease

ACTOR 2: And shows that regardless of our outward appearances . . it is our soul that makes us who we are.

TOGETHER: Inside Al by David S. Baker
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Actor 1: Al and Beth Actor 2: Inside Al and Jason

AL: He is the outside Al, the body. He is a 39-year old victim of cerebral palsy. His speech is slow and sometimes hard to understand, especially when he is upset or excited.

INSIDE AL: He is Al’s mind and feelings. He is perceptive, blunt and sometimes bitter. His speech is extremely articulate and fluid.

JASON: Average 16-year old boy

BETH: Insecure, frightened child of 16 who hides her fear by using and abusing those she comes in contact with. She manipulates all of her relationships and takes advantage of anyone who is weak-willed enough to let her.

(Al walks stiffly onstage. Inside Al is behind and slightly to one side of him moving with him in perfect synchronization. Al and Inside Al speak sometimes together and sometimes alternatively, but the feel is that the words are coming from the same person, even if from different mouths – the feel is still that of a monologue)

NOTE: Inside Al should assume the body position of AL before he speaks each line and then “morph” out of the crippled body into the character of Al’s mind and feelings

AL/INSIDE AL: (Simultaneously) Hi. I’m Al. Alvin Theodore Willson (They chuckle)

INSIDE AL: . . . Always makes me think of the Chipmunks.

AL: People stay away from me, mostly. I have cerebral palsy.

INSIDE AL: Sometimes, though, I feel like I have leprosy or something. They stare at me or say I’m dumb – retarded. I’m not, though.

AL: My mind tells my body to do things, and my body doesn’t cooperate very well . . . but I’m not dumb.

AL/INSIDE AL: They don’t know me.

INSIDE AL: When I walk to the market, people smile and wave at me as they go by. I know that as soon as they pass, they quit smiling. They stop and think.

AL: (Mocking himself) “Oh, look at poor old Al, he’s so slow and dumb and . . .”

INSIDE AL: . . . I could just scream! They pity me. If there’s one thing in this world I hate the most, it’s pity. I hate charity, too, except real charity.

AL: Why can’t someone be nice to me just to be nice to another human being? Why can’t people look past my body (Al points at Inside Al)

INSIDE AL: . . . and see my soul?

JASON: When my teacher first told us about the “be nice to someone” project, I groaned. I hate this type of assignment. (Beat) I decided to help Al Willson for several reasons. He’s a real friendly guy - always waves at us when we pass him on his way to the market. I don’t think Mr. Willson has any family – never seen any anyway. Most people just ignore him, or barely accept him. I heard a bunch of kids at school once, talking about him; they called him the “village idiot.” (Beat) Anyway, on my way home from school, the day the assignment was given, I checked the back yard of Al’s little flat. I was lucky. It hadn’t been mowed for months.

(Jason exits and reenters, bringing a push mower and a rake. He puts on his hat and shade, one at a time, and takes headphones from around his neck and puts them on. He flips his collar up and grabbing the mower, he makes passes to simulate mowing. Then stops mowing and picks up rake – Uses it as an Air Guitar and dances to the music he’s listening to on his headphones).

AL: (To audience) And I thought I moved funny!

JASON: Uh . . . hi. I did your lawn. What do you think?

AL: It looks real good.

JASON: Anything else I should do for you?

AL: No (Al reaches into his pocket and brings out a worn dollar bill and some small change)

JASON: (narrates action to audience) He tried to pay me, but I told him I wasn’t supposed to take payment. (Al reaches into his pocket again hands something to Jason and then steps back) It was a little ceramic frog. Al made it himself – I could tell. (Al waits patiently). It was a nice gesture, anyway. I thanked him, took my rake and my mower, and left. (All exit)

(SCENE)

BETH: I decided [to] be nice to Al Willson. (pauses then continues explaining) That cripple. You know, that guy who wanders around all the time wearing those jumpsuits and that blue baseball hat. He has a problem, that’s for sure.

(She giggles, pulls a face and imitates Al’s speech) Hello, little kiddies! . . . . Heh, heh . . . Want to pay some games? (moves over in front of an imaginary mirror and begins examining herself) Anyway, since everybody likes cookies, I figure [I] can bake some for him, take them to his house and then get my parents to sign that “be nice to someone” form.

(SCENE – Al’s front porch - (Beth enters and begins to leave some home-made cookies on the doorstep when Al comes out and surprises her

BETH: Oh . . . hi, Mr. Willson. [I] came to bring you these cookies. [I] , ah, made them for you. (Al stands looking at them; he appears confused) (Louder) [I] brought you these cookies. They’re almond cookies. [I] thought you might like to have some.

INSIDE AL: (Loudly and slowly) I’m not deaf; I have cerebral palsy.

AL: Is this for your project? (Actor 2 can do this line as AL)

BETH: How did you know about this project?

AL: A boy named Jason mowed my back lawn. (Actor 2 can do this line as AL)

INSIDE AL: (Cynically) He beat you to the cripple.

BETH: (under her breath) Why , that idiotic little son of a . . . (To Al) Well, [I] have to go. See you around, Mr. Willson. ‘Bye (turns and leaves)

INSIDE AL: (follows circling around her, yelling at her. He almost seems to be dancing) Oh, please don’t. I’d really rather you didn’t see me around. Tell you what. Instead of seeing me around, could you go jump out of a window?

(SCENE)

AL: I’ve noticed something about people: most of them don’t look me in the eye. They look past me, or around, or at each other, but they never look at me.

INSIDE AL: I think they are afraid to see my body, to accept the fact that I am handicapped. They would rather think that it is all mental – that’s much easier for them to accept. (Pauses) Once, I was on the porch watching the kids play. Some little boys came up to me and I asked them if they wanted to hear a story. I’m very good with stories.

AL: One of them called out. “Retard, retard!” and the rest walked around with stiff joints, making fun of me, of course. I wanted to wring their grubby, little necks – all of them! But I couldn’t. I just sat there and . . . “

INSIDE AL: Why didn’t you ever get mad at them?! Quit being such a wimp and do something for a change! You let everybody walk all over you. You’re a person too, why don’t you show them that? Why don’t you ever ACT LIKE A HUMAN! (Imitates Al’s movement and speech) Look at me. I’m a poor, helpless cripple. I can’t walk or talk or do anything.

AL: People always feel sorry for me and that make me mad but

AL/INSIDE AL: I never say anything. (Jason enters and startles Al)

JASON: Mr. Willson? Can I talk to you a second? The reason I came by is to apologize to you.

AL: For mowing my lawn?

JASON: No, no. For . . . well . . .for hurting your feelings. I treated you like a project . . .not a person and I’m sorry.

INSIDE AL: Don’t do this. It’s easier for me to hate you. Don’t make me like you. (Al can do this line)

AL: There is no need . . .

JASON: I really feel bad about this. Please. Maybe you’re used to having this happen to you, but I think that you shouldn’t have to be use to it. People can be so cruel!

AL: Yeah, tell me about it. Just your coming here helps a litte.

INSIDE AL: (to Al) It’s forgiven?

AL: (to Inside Al) It’s forgiven.

(Scene)

BETH: I made the cookies. . .. why does it matter that [Jason and I] were nice to the same cripple? (crosses to Al’s porch) (Bluntly) Hello, Mr. Willson. I came to find out why you didn’t accept y kindness.

INSIDE AL: KINDNESS?? If that was kindness, I’d really hate to see cruelty. What I didn’t accept was your pity.

BETH: (as if there was not response) Did my teacher call you? What did you tell her?

AL: That you brought me cookies (Inside AL can do this line)

BETH: Didn’t you enjoy my cookies?

INSIDE AL: Well, no. They were soggy, greasy and had little pockets of baking soda in them (makes a face at the audience). Frankly, they were the worst cookies I have ever tasted.

AL: Yes, but . . .

BETH: (intimidating) If you liked them so much, then why did you tell my teacher that my project wasn’t good enough? You ruined my grade! (Jason enters)

JASON: (to Beth) What are you doing here? (To Al) Is she harassing you?! (To Beth) What’s your major maladjustment anyway?

BETH: Well, this gimp told the teacher not to give me credit for my project.

JASON: Wait a minute. What exactly do you mean, “project.?” You’re telling me that this man is your project?

BETH: Yeah, stupid (laughs) Now who has the brain problem?

JASON: Do you think Al does?

BETH: (Mocking AL’s speech) Oh, there’s nothing wrong with him. Nothing at all. . .

INSIDE AL: (speaking to the audience, as if they are all that will listen) You know, it’s times like these that I’d really like to knock her head off.

JASON: You really think he’s retarded, don’t you? Oh, you poor child. You’re so confused. He’s got cerebral palsy, not ‘stupidity syndrome.” His body is slow, not his brain.

AL: Both of you – please leave. Leave me alone.

INSIDE AL: Well, get out of here! I don’t’ need rescuers, and I don’t need accusations. I don’t need any of you. I wish your stupid teacher had neer given this asinine project in the first place. You’re hypocrites – all of you! One “being kind to me” and the other “protecting the poor, helpless retard.” I wish you would all just

AL: . . . GO AWAY

(Scene)

JASON: I was trying to defend Al – to help him. Beth just kept going at his throat and I thought he needed me. I figured he couldn’t handle her all by himself. Thing is, I guess he didn’t want to be defended. I made him feel helpless. Handicapped (he cringes). I don’t know. Maybe it’s not the charity, but the way it’s given . . . You have to drop the pity.
```

---

## IC-1018: Inside the Corner Office: The Real Story of The Bonker’s Candy Factory

- Title: Inside the Corner Office: The Real Story of The Bonker’s Candy Factory
- Author (byline): Mike Beyer
- Work: Exposed! Eight 10-Minute Scenes About What Really Happened, Pg 34-42
- Publisher: Heuer Publishing
- Publication date as stated: 2013
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 2, CHARLES, GRANDPA, BILLY, TOGETHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1554
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mike Beyer
Book: Exposed! Eight 10-Minute Scenes About What Really Happened, Pg 34-42
ISBN: 978-1600036767
Publisher: Heuer Publishing
Date (Month/Year): 2013
* Music to Candyman from Willy Wonka can be found here:
https://www.youtube.com/watch?v=sizCBeS03YU
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Inside the Corner Office:

ACTOR 2: The Real Story of The Bonker’s Candy Factory

TOGETHER: by Mike Beyer
```

### Performance text (classify this)

```text
Suggested Characters: ACTOR 1: Charles

ACTOR 2: Billy and Grandpa

NOTE: This cutting asks one student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

(Musical intro – hum or vocalize the melody of The Candy Man by Sammy Davis, Junior*)

An empty office. Billy Bonkers strides in briskly, approaches the desk and begins writing furiously. Charles and Grandpa stick their faces through the partially open door cautiously.

CHARLES: There he is Grandpa! There’s Willy Wonk – I mean, Billy!

GRANDPA: Huh?

CHARLES: Nothing. Stupid lawyers. The tour of his candy factory has taken us to his private office at last! All the other naughty children have met a nasty end, and we’re the only ones left. But why isn’t he inviting us in?

GRANDPA: What?

CHARLES: (Much louder) I said, we’re the only ones left on this tour, and I – never mind. I’m going in. (Charles enters the office and Grandpa cautiously follows)

CHARLES: Mr. Bonkers, sir? (No answer) Sir?

BILLY: (Unpleasant, business-like) May I help you?

CHARLES: Well, my Grandpa and I are the only ones left on the tour, so we were wondering what happens now.

BILLY: (Not looking up) Yes. Well. The exit door is down the hall, second door on your left.

CHARLES: Sir, what about the five pounds of candy per day?

BILLY: Excuse me?

CHARLES: (Taking the ticket from his pocket) It says that everyone who completes the tour gets five pounds of candy every day for the rest of their lives.

BILLY: (Snatching the ticket from Charles’ hand and inspecting it) Ah. So, it does. HOWEVER, it does NOT allow for little thieving boys and their elderly thieving grandpas!

CHARLES: We didn’t steal anything!

BILLY: Really? Then you deny going into the Belchy SugarBlast Drinks room and helping yourself to a taste? Even though such tasting is strictly forbidden?

CHARLES: (Head down) No. We drank it.

BILLY: Aha! I knew it. Well then. If there is nothing else you require, please show yourselves OUT.

CHARLES: We almost died in that room! We got such a sugar rush from that drink that I almost had a heart attack! Look what your drink did to Grandpa!

GRANDPA: (To the wall) Hello there!

BILLY: Then I trust you have both learned a valuable lesson. And that lesson is: DON’T TOUCH OTHER PEOPLE’S STUFF! You don’t get the five pounds of candy! You get NOTHING! Now goodbye!

CHARLES: But-

BILLY: I SAID GOODBYE-BYE! (Pause)

CHARLES: Let’s go. (He turns, takes GRANDPA by the hand, and together they prepare to exit)

GRANDPA: Where we going now?

CHARLES: Home, and the bread and water that waits for us. (They stop at the door, and CHARLES looks back at BILLY) Hold on a second. (He reaches into his pocket, goes back and places a piece of candy on BILLY’S desk then proceeds to leave)

BILLY: (touched) The honesty of a child. Returning that which he could have easily kept. . . (He whirls around) Charles! Don’t go. Please.

CHARLES: But you said the tour was over-

BILLY: I know what I said, but don’t you see? This was the test! You were told to get a piece of my Molarcrusher Rock Candy and give it to my main competitor.

CHARLES: Yes. Mr. Vanilla Fudgerton told me to get a piece of this candy and he would pay me a million dollars and all the chocolate bacon Slurpalicious Shakes I wanted.

BILLY: Yes, and all the other children gave the pieces to Fudgerton, who secretly works for me. But not you! Don’t you see what that means? It means you’ve won! All this will one day be yours!

CHARLES: You mean. . . I’ll be president and CEO of Bonker’s Candy Factory? Oh, my goodness! You don’t want to do that!

BILLY: Oh, but I do. A child is the only one who can truly love fantastic items like the Oreo Cookie/Ranch Dressing Cream Puffs. A child is more open to new ideas – (aside to audience) and by open, I mean he’ll run it exactly my way.

CHARLES: This is a dream come true! When do I start?

BILLY: No time like the present! (He produces a contract and signs it) Charles, when you sign this, you will be the unquestioned boss of the world-famous Bonker’s Candy Factory.

(Hands the contract and pen to CHARLES. GRANDPA leans over CHARLES’ shoulder and reads the contract. He gasps.)

GRANDPA: Do it, Charles! (Charles signs it)

BILLY: Excellent! Fantastic! Splendid! Adjectives! Let’s get into my rocket-powered elevator and grab the rest of your family!

CHARLES: (Charles’ demeanor changes) Let’s you have a seat and let the new boss do his thing!

BILLY: Excellent plan – wait a minute, what?

CHARLES: You heard me. (BILLY sits down in his old chair) You’re sitting in my seat, Mr. Bonkers.

BILLY: Haha, you’re already taking to the job! I like that. Want to go back down to my strawberry lake and eat some mango-flavored orchids?

CHARLES: No thanks. I have plans for that room! Grandpa, take a memo. (GRANDPA takes a notebook and pen from the desk)

GRANDPA: Go, Charles!

CHARLES: You know, Billy, I’m not feeling the name “Bonker’s Candy Factory.” I think a new name is needed. I think the name “Bonker’s Organic Healthy Creations Farm” has a nice ring to it, don’t you?

BILLY: Sacrilege! The name of Bonkers is known from Kalamazoo to Timbuktu! Why, children everywhere look forward to consuming my creations!

CHARLES: Yes, and thanks to your creations, obesity is at an all-time high!

BILLY: Well, that’s not MY fault! It’s the parents who are responsible! Children today are so SPOILED!

CHARLES: Yes, but I plan to change everything inside your company. For starters, your Bonker’s Cherry Cake Batter and Double Caramel Ice Cream will now become just Bonker’s Cherry Yogurt.

BILLY: (Spluttering with rage) You. . . you. . . Ridiculous! No one will eat it. This is an outrage!

CHARLES: The Bonker’s Organic Healthy Creations Farm will help children around the world reach their true nutritious potential -- through healthy snack offerings!

BILLY: My candy is nutritious! Look how fit I am! (He attempts to do jumping jacks. He fails. A beat)

CHARLES: (unimpressed) So, as I was saying, we’ll make smoothies that will cause children to do jumping jacks! Our chewing gum will actually remove plaque and whiten teeth! Our glazed donuts will contain more vitamins than *sugar*!

BILLY: You’re mad! (to audience) He’s ruining everything I’ve helped to create! I knew I should have picked the fat kid who got sucked through the tubes.

CHARLES: His Type 2 diabetes is probably irreversible. But I’ll have him work for me. He can help me convert the chocolate eggs into low-calorie egg whites. He’ll also lead the Bonker’s Marathon Training Team!

BILLY: Charles, Charles, Charles. Before you go completely crazy and send us all to ruin, let’s just talk this out first. My whole mission in life has always been to bring smiles to children’s faces! To make the world taste good!

GRANDPA: Do we even need Bonkers anymore?

CHARLES: Nah. Send him down to the old Exploding Room. We’ll make him a test taster of our Quinoa Brownie Delights.

BILLY: OK, OK, I get it! Candy equals bad! I understand now. But let me help you – I know how this factory works, and I can help you achieve your dreams!

CHARLES: I’m listening.

BILLY: OK, I promise to get rid of the High-Fructose Corn Syrup and Artificial Sweetener Room.

CHARLES: Good.

BILLY: But it helped my chocolate bars taste so delicious! Don’t you like flavor?

CHARLES: Not when kids can barely climb the stairs and develop more pimples than there are stars in the sky!

BILLY: But those candy bars keep those kids from developing bad habits in life. Parents actually DEPEND on me to keep their little brats in line.

CHARLES: I’m not sure I follow you.

BILLY: You see, children need rewards to work for. What better reward than candy? No one will clean their room or eat their broccoli if the incentive is just a stupid apple.

CHARLES: Apples are not stupid! Besides, my new orchards will produce apples as big as your head. Not only that, they give you the ability to do long division problems in your head the minute after you eat them!

BILLY: Whatever! It’s still an apple! They don’t comfort anybody! Who’s going to sit down on a lonely Saturday night for a good cry, a couple of movies, and a tub of kiwis and carrots?

CHARLES: Plenty of people, if they know they have to get up the next morning and run eight miles! We’ll have Bonker’s Nutrition Clubs set up worldwide!

BILLY: But can’t we at least give the lazy people some Bonker’s Sticky Stomach Taffy, just to give them a little break from this terrible world?

GRANDPA: Sorry, Bonkers. The jig is up.

BILLY: Grandpa? Could I perhaps interest you in a Bonker’s Nut-tastic Dark Chocolate Toffee and Peanut Butter Avalanche? A parting gift from me. You won’t be seeing these anymore.

GRANDPA: Well, thank you, Mr. Bonkers. (Takes a bite.)

CHARLES: Grandpa! DON’T EAT THAT – (They fight over the candy bar, but Grandpa is crafty and manages to pop the entire bar into his mouth)

GRANDPA: (with his mouth full) Sorry, Charles. But. . . wow! I forgot how GOOD this tastes!

CHARLES: For your information, those three bites just put about 12,000 calories on your frame, and will keep five dentists employed for at least a year scraping all that toffee from your teeth!

GRANDPA: Maybe we can have one room here in the factory for candy, and the other 7,000 for your health food and juice products!

CHARLES: I don’t believe what I’m hearing!

BILLY: Listen to your Grandpa, Charles. Maybe you should let him run the factory for now, until you get a little bit older.

CHARLES: No deals! Now, Grandpa PLEASE! Step away from the candy!

GRANDPA: But Charles, I haven’t had one of these in years! Do you know why?

CHARLES: The last of your teeth fell out?

GRANDPA: I started listening to all the fitness and nutrition do-gooders! Shouldn’t we at least still observe the time-honored tradition of dessert? In moderation?

CHARLES: We’ll have candy bars! We’re going to roll out Bonker’s Chocolate-Flavored Edamame Krispy Krunch! The youth of tomorrow will thank us!

GRANDPA: Charles, I’m stepping in. I’m appointing myself CEO of the Bonker’s Candy Factory until further notice. At first I went along with your plan, but these food creations of yours push the envelope in ways that are bad and wrong. Edamame Krispy Krunch? Gross. (He takes the contract from the desk and rips it up)

CHARLES: NO!!!

GRANDPA: We’ll split up the factory. Billy can continue to make his fantastically magical candy, and you can start on your super- healthy goodies.

CHARLES: I suppose half-ownership of Bonkers is better than a lifetime doomed to eating cabbage soup and noodles.

BILLY: [And] I get to keep this corner office.

CHARLES: (pouting again as a young child) This is so unfair! GRANDPA!

GRANDPA: Now go to your room. (CHARLES stomps out. BILLY goes to the desk and pours two glasses)

BILLY: (Giving a glass to GRANDPA) Belchy Sugar Blast?

GRANDPA: Don’t mind if I do!

TOGETHER: (Raising glass) To health! (They drink and both burp loudly)
```

---

## IC-1019: Joe & Stew’s Theatre of Brotherly Love and Financial Success

- Title: Joe & Stew’s Theatre of Brotherly Love and Financial Success
- Author (byline): Jacquelyn Reingold
- Work: Best American Short Plays 1999-2000
- Publisher: Applause Books
- Publication date as stated: 2001
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: STEW, JOE, JOE AND STEW
- Teaser before the introduction: Yes
- Spoken words (computed): 1853
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jacquelyn Reingold
Book: Best American Short Plays 1999-2000
ISBN: 978-1557834522
Publisher: Applause Books
Date(Month/Year): 2001
```

### Introduction (context only: never use it for content warnings)

```text
Actor 1: We interrupt this crisis for an important commercial announcement!

Actor 2: Want power and respect? Want to influence the course of world events? Want to be on CNN every night? Tired of hum-drum conventional warfare and messy bio-chemical weapons? Want to watch the citizens of your favorite arcology squirm and sweat in constant nagging fear of instant and unexpected anhilation? Lease a nuclear device!

Actor 1: He’s just kidding . . Survival of the detonation of a nuclear device is tenuous at best . . . Unless, of course, you are safely ensconced in

Together: Joe & Stew’s Theater of Brotherly Love and Financial Success by Jacquelyn Reingold
```

### Performance text (classify this)

```text
STEW: A cockroach. Smart and sensitive.

JOE: His brother. Also a cockroach. Not so smart and not so sensitive.

The sound of a loud explosion. Lights up. Debris is everywhere. We hear voices from under a pile.

STEW: Whoa! What was that?

JOE: I don't know.

STEW: You ok? Joe?

JOE: I don't know. You?

STEW: I don't know. Where are you?

JOE: I don't know.

STEW: Can you see?

JOE: Not really.

STEW: Me either. That was pretty bright.

JOE: Yeah.

STEW: And loud.

JOE: No kidding.

STEW: That wasn't in last night. Must be new, huh?

JOE: I guess.

STEW: I don't see how it makes sense.

JOE: Didn't make no sense to me.

STEW: I mean dramatically, you know. [STEW emerges from the pile. He is a cockroach. He looks around at the mess.] Wow. [To himself] Very realistic. Very site specific. Very breaking the fourth wall.

JOE: What?

STEW: Nothing.

JOE: Ow! Damn.

STEW: You ok?

JOE: Yo, I don't know, I'm stuck. I'm under a beam or somethin'.

STEW: Ok, I'm coming, I'm coming. Just keep talking.

JOE: Three of my legs are stuck under a damn two by four and it's cutting off my circulation! [STEW removes a broomstick [toothpick] from JOE's legs. He emerges. He is a cockroach, too.]

JOE: What was that thing?

STEW: Toothpick. You ok?

JOE: Yeah. I think so.

STEW: Antenna?

JOE: [He checks.] Fine.

STEW: Legs?

JOE: All there.

STEW: Carapace?

JOE: In one piece.

STEW: That was close.

JOE: Sure was. Hey, you saved my life, Stew.

STEW: Ah, what are brothers for? [They clap each other on the back.]

JOE: [Notices the surroundings.] Wow. What a mess.

STEW: Impressive, huh?

JOE: Uh oh.

STEW: What?

JOE: Where are those brownie crumbs?! I worked all week to collect them. [He searches.]

STEW: Uh oh.

JOE: What?

STEW: What do you hear?

JOE: Nothing.

STEW: This is the part in Act 2 where they yell and have that big fight. "You son of a BEEP!" "You daughter of a BEEP!" Remember?

JOE: Not really.

STEW: We better go look.

JOE: I'll stay here. [They look at the audience.]

STEW: . The actors - they're - gone.

JOE: Human toast.

STEW: The audience.

JOE: Burnt to a crisp. Except for that one.

STEW: The critic.

JOE: He's in pain, but he's alive. What should we do?

STEW: Let him suffer.

JOE: Something happened, huh?

STEW: Joe, remember the bedtime story Grandpa used to tell us about the humans and the atomic bomb and how we'd be only ones to survive?

JOE: Uh, no.

STEW: We'd have cookies and milk while he told us?

JOE: Oh, yeah.

STEW: I guess it's true.

JOE: You mean - ?

STEW: Kaboom. The end of the human race. The end of all the races. Except for us.

JOE: You mean?

STEW: The world is ours.

JOE: You mean there won't be an intermission?

STEW: I guess not.

JOE: I wonder what happened to all those snacks.

STEW: How can you think of that right now?

JOE: What-we gotta eat, right?

STEW: Yeah. I guess.

JOE: [Singing and dancing.] This Land is My Land. This Land is My Land. This Land is My Land. This Land is My Land.

STEW: What are you so happy about? Except for the suffering and ultimate slow death of the critic, I don't see the cause the for joy.

JOE: No more humans, right?

STEW: Right.

JOE: That means no more Raid, right? And no more Combat trays. No more boric acid mixed with sugar. No more run for your life here comes a big pair of shoes, right?!

STEW: Right.

JOE: Well, shouldn't we celebrate? I mean we've taken over the world, right?! !

STEW: Right.

JOE: Isn't that what we always wanted? Stew, Stew. Bye bye non profit, hello big bucks! Right? Think of the opportunities. Think of the population explosion. It's unbelievable. We could turn this place into - into the world's first real roach motel. "Where roaches check in, and then they check out."

STEW: Joe.

JOE: Stew.

STEW: You're not thinking of

JOE: What?

STEW: Not having a theatre?

JOE: Sure I am.

STEW: I'm speechless.

JOE: That's fine.

STEW: Now wait one second, this is a theatre.

JOE: No, this was a theatre.

STEW: I have something to tell you. I never told this to anyone before. But now seems like a good time. With what's happened.

JOE: Yeah?

STEW: I know we're brothers and all, but I'm well, different.

JOE: You mean - ?

STEW: I'm not like the rest of the family, or even the rest of the species.

JOE: You're not?

STEW: I'm a

JOE: What?

STEW: A

JOE: What?

STEW: A not for profit theatre lover.

JOE: What?

STEW: I love this theatre. That's why we've stayed here for so long.

JOE: I thought it was for the brownies and the chocolate chip cookies, and how they didn't have the money to pay someone to clean up the crumbs.

STEW: No. It's the smell of the green room and the roar of the dressing room, the dust on the pile of scripts in the literary office, the broken air conditioning, the young hopeful faces of the interns, the tears of the playwrights

JOE AND STEW: - Especially the ones who get produced.

STEW: The constant begging and demeaning of oneself to raise money, the tyranny of the artistic director - how everyone hates him and kisses his butt at the same time - and of course the rehearsals, the performances, the production meetings, the cast parties.

JOE: At least those are good. Lots of hummus.

STEW: The opening night fundraiser for the board.

JOE: Cheese cubes.

STEW: The only thing I hate, of course, is the critic.

JOE: I like the critic, he never picks up his candy wrappers.

STEW: I was born in a trunk. Well, metaphorically. Actually, we were born behind the refrigerator in the artistic director's fabulously tiny deliciously filthy studio apartment. And on the same day that he murdered our mother and father, he unwittingly gave us a new home by carrying us here in his knapsack.

JOE: Things were different then.

STEW: Yes. The plays were daring, the audience was packed, the tickets were cheap, and the critics were so confused by the enthusiasm, they were kind.

JOE: And now we gotta change with the times. Right? No point in the living in the past. I always wanted to be an entrepreneur. Go into real estate. We could form a partnership. I got lots of ideas. Health clubs, cruise ships, coffee bars. They'll all be dark, damp, and filled with food.

STEW: Joe.

JOE: Stew. How many people were in the audience tonight?

STEW: Four. The director, the playwright, the artistic director, the playwright's mother.

JOE: That's not an audience. That's a car pool.

STEW: And the critic. Five. But I guess he doesn't count. You said humans.

JOE: Look, how big was their debt?

STEW: Big.

JOE: How often were they the butt of jokes in their community?

STEW: Often.

JOE: How badly did the actors try to quit the shows by looking for jobs in the movies? Well?

STEW: Well, how bout all the work they've done. That production ofMetamorphosis? I cried every night. Think of their dedication to non-commercialism and multicul-turalism. The work they did with the disabled, the untalented, the criminally insane. Their commitment in the face of constant failure.

JOE: Stew, this place was a bomb way before the one that dropped in here tonight. I may not be a genius, but I know what I know, and this is not the time and place for a theatre. All you had to do was look ator crawl over the face of the guy who ran the place. Heart broken and bitter.

STEW: He dedicated his life to this.

JOE: Exactly. And we survived, and he didn't. Whatever they gave us we lived through it: poison, sterilization, DDT, you name it, we beat it; not by jerking each other off in the name of the theatre. This place? On the evolutionary scale, it thrived for maybe a second. Less.

STEW: But that's why we'd do better.

JOE: Stew, we're talking survival of the fittest, not survival of the artistic! The answer is: No Way. [STEW starts to sob.] Oh, geez, don't cry. Look, uh maybe a movie theatre, ok? We could break it into 70 or 80 smaller ones, and call it a a Cockaplex. Or or a porn theatre, all right? With beautiful young roachettes on stage shaking their antennae and showing off their egg sacs. But that's it.

STEW: You don't understand, without this my life has no meaning. This is why I survived. I know it.

JOE: Don't be dramatic.

STEW: I'm gonna go electrocute myself on the smoke machine.

JOE: Stew.

STEW: I am. That would be a fitting end, I'll fry myself with the others. If this theatre doesn't survive than I don't. And don't forget who saved who earlier today. [He runs off. He shrieks and moans. Shrieks and moans again.]

JOE: Ok.

STEW: [He runs back.] Yes?

JOE: Ok ok.

STEW: Yes!!

JOE: God, all these years I thought you were just a regular roach. Who knew?

STEW: Oh, you won't regret it.

JOE: We'll see about that. So, now what, I mean look at this place, how are we gonna run it?

STEW: Well, well... how many kids do you have?

JOE: I don't know, a few hundred, you?

STEW: The same.

JOE: So?

STEW: Interns!

JOE: Right.

STEW: But my first job as artistic director is to name it. What do you think?

JOE: I don't know. How bout Manhattan Roach Club?

STEW: Hmm. Too commercial.

JOE: Cockroach Horizons?

STEW: Too past its prime.

JOE: Ensemble Roach Theatre?

STEW: Too psychotic.

JOE: Naked Roaches?

STEW: You're kidding, right?

JOE: There'd be good parties. [STEW shakes his head no.] Insert name of the theatre where the play is being performed - Roaches?

STEW: How bout Joe's Theatre?

JOE: Hmm. How bout Joe and Stew's Theatre?

STEW: How bout Joe and Stew's Theatre of Brotherly Love.

JOE: And Financial Success. Hey, I like that.

STEW: Me too. [Both respond to a sound off stage]

JOE: What's that?

STEW: Oh God. It's the

JOE: Critic!

STEW: He's mutated. He's huge!

JOE: What's he saying?

STEW: He's thanking God for the bomb, [More critic sound>.] that the director and the writer got what they deserved, [Critic sound>.] that he's gonna run this place himself and do his favorite shows over and over like The Tale of the Allergist's Wife and Mnemonic, [Critic sounds.] and anything directed by someone named Scott.

JOE AND STEW: [Scream in horror.] Ahh!

JOE: He's coming our way. We better run.

STEW: I'm not running, this is our home. He can it have over my dead body.

JOE: This is no time for idealism.

STEW: Some things you just gotta stand up for.

JOE: Oh, brother.

STEW: Joe, he's not just a critic.

JOE: He's not?

STEW: No, he represents all the negative forces trying to beat us down, take away our creative spontaneity, and make us feel hopeless and alone. He's the bug in grade school that made fun of the way you scampered, the politician that got elected on hate and fear, the punk that stole your ice cream. Come on, this is the first day of the new world, a chance that'll never come again. Stand still and be counted. He may be big, but we have right against his might. We are brothers for art.

JOE: That's a little corn ball, isn't it?

STEW: It was from their last Christmas play, terrible writing, but it seemed apropos, and this guy gave it a good review, worst thing they did all year.

JOE: Here he comes.

STEW: Joe, are you with me? We've lived through it all, just like you said . It's our theatre, not his!

JOE: It doesn't look that way.

STEW: If we don't take a stand against the critic, who will?

JOE: .. We're the only ones left.

STEW: So, are you with me, Joe?

JOE: I'm with you, Stew. [STEW Arms himself with the toothpick.]

STEW: Well, then. Places. [They head towards the stage.]
```

---

## IC-1020: Kelso and Case-Tec

- Title: Kelso and Case-Tec
- Author (byline): Jose Cruz Gonzales
- Work: 10 by 10
- Publisher: Dramatic Publishing
- Publication date as stated: 2004
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: KELSO, CASE-TEC
- Teaser before the introduction: No
- Spoken words (computed): 521
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jose Cruz Gonzales
Book: 10 by 10
ISBN: 978- 1583422410
Publisher: Dramatic Publishing
Date (Month/Year): 2004
```

### Introduction (context only: never use it for content warnings)

```text
According to the website Childhelp.org, in 2009, approximately 3.3 million child abuse reports and allegations were made involving an estimated 6 million children. About 80% of 21 year olds who were abused as children met criteria for at least one psychological disorder. The confusion that comes in these broken homes creates unique sibling relationships as seen in Kelso and Case-Tec by Jose Cruz Gonzales.
```

### Performance text (classify this)

```text
(Kelso and CASE-TEC watch a television set. KELSO surfs the channels by remote.)

KELSO: See there he is again.

CASE-TEC: No way.

KELSO: It looks just like him but younger.

CASE-TEC: Go back. KELSO (changes the remote): See!

CASE-TEC: That’s impossible.

KELSO: Dude, I’m telling you it’s him.

CASE-TEC: Give it here! (CASE-TEC takes the remote from KELSO.)

KELSO: Okay, there he is as an old man with a white beard carrying two stone tablets.

CASE-TEC: He’s Mosese, right?

KELSO: Here, the apes put him in prison.

CASE-TEC: It’s Planet of the Apes.

KELSO: I like Marky Mark’s version better.

CASE-TEC: Wow, check her out.

KELSO: Who?

CASE-TEC: The babe wearing the bikini in jail with him stupid.

KELSO: Oh, yeah.

CASE-TEC: And now, he’s really old holding a musket over his head smiling like an idiot.

KELSO: Weird.

CASE-TEC: What’s his name?

KELSO: I don’t know.

CASE-TEC: Who cares? (The phone rings. They both jump to get it. CASE-TEC grabs it.) Hello? Yeah, it’s me. He’s here too. Ah-huh?

KELSO: Let me listen

CASE-TEC: Shhh! Yeah. Okay. Ah-huh. Ah-huh. Okay. (CASE-TEC hangs up the phone.)

KELSO: Well?

CASE-TEC: Nothing’s changed.

KELSO: How long do we gotta wait?

CASE-TEC: ‘Til something changes.

KELSO: Is Mom going to-

CASE-TEC: I don’t know.

KELSO: Did we do the right thing?

CASE-TEC: We had to do it.

KELSO: But what if Pop hadn’t-

CASE-TEC: It wouldn’t have mattered. He always blows up.

KELSO: What’s going to happen to us?

CASE-TEC: Why are you asking so many questions?

KELSO: just want things the way they were.

CASE-TEC: We’re never going back to that house. (KELSO picks up a game controller.)

KELSO: I’m playing a video game.

CASE-TEC: Dude, the thing’s broken.

KELSO: I know that.

CASE-TEC: Nothing works around here.

KELSO: There’s nothing else to do.

CASE-TEC: So you’re going to pretend you’re playing a game?

KELSO: Go away. (KELSO pretends to play a video game.)

CASE-TEC: So what’s the game? “Medal of Honor Frontline”?

KELSO: No.

CASE-TEC: “NBA Live”?

KELSO: Yeah, right.

CASE-TEC: “Lord of the Rings”? (Beat.) I knew it! It’s a dumb game.

KELSO: I always beat you.

CASE-TEC: No you don’t.

KELSO: You cry every time.

CASE-TEC: Wanna Bet?

KELSO: You’re on! (CASE-TEC sits beside KELSO. They pretend to play. They are very animated pretending to play. CASE-TEC tosses the game controller down.)

CASE-TEC: I win!

KELSO: No, you cheated.

CASE-TEC: Prove it.

KELSO: I can’t.

CASE-TEC: Loser.

KELSO: Cheat. (KELSO picks up the remote, changing channels again. Beat.) I’m scared, Case-Tec.

CASE-TEC: I know, Kelso, I am too.

KELSO: Why did Mom do it?

CASE-TEC: She said something made her feel everything was going to be okay.

KELSO: Like what?

CASE-TEC: Like a giant hand protecting us.

KELSO: DO you think she’s going to make it out of the hospital?

CASE-TEC: I don’t think she can feel a thing right now.

KELSO: He shouldn’t have hit her.

CASE-TEC: He was crying like a baby when they took him away.

KELSO: He’s going to be mad later.

CASE-TEC: he’s never going to lay a hand on us again.

KELSO: Mom led us out of there, didn’t she?

CASE-TEC: Yeah, just like that guy in the movie with the stone tablets. (The phone rings. They both rush to it. CASE-TEC answers it.) Hello? Yeah?

(CASE-TEC shares the phone so KELSO can hear.)

KELSO: I’m here.

CASE-TEC: How is she?

KELSO: Is Mom going to be okay?

CASE-TEC: Yes!

KELSO: When can we see her?

CASE-TEC: Soon?

KELSO: I want to go there now.

CASE-TEC: We can’t. Yes? Okay. Thanks.

KELSO: ‘Bye. CASE-TEC (hangs up the phone. He starts to cry): You better not tell anybody.

KELSO: I won’t.

CASE-TEC: ‘Cause if you do-

KELSO: Is Mom going to remember what happened?

CASE-TEC: I hope so.

KELSO: What if she doesn’t?

CASE-TEC: Then we gotta tell the truth.

KELSO: Pop’s not going to like it.

CASE-TEC: Who cares? It’s you, Mom and me. That’s all that matters, right?

KELSO: Right.

CASE-TEC: So you wanna play?

KELSO: Nah. You want the remote?

CASE-TEC: Sure. (CASE-TEC starts surfing the channels.)

KELSO: Wait!

CASE-TEC: What is it?

KELSO: There he is again.

CASE-TEC: No way!

KELSO: This time he’s driving a chariot!

CASE-TEC: That dude’s on every channel! KELSO (turns off the television): Not anymore! (Beat.) Case-Tec, are we going to be okay?

CASE-TEC: Yeah, we’re going to be okay, Kelso.
```

---

## IC-1021: The Last Days of Judas Iscariot

- Title: The Last Days of Judas Iscariot
- Author (byline): Stephen Adly Guirgis
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: July 2006
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: JUDGE, GLORIA, BAILIFF, PROSECUTING ATTORNEY, SATAN, P ATTORNEY, JUDAS, DEFENSE ATTORNEY, D ATTORNEY, JESUS
- Teaser before the introduction: Yes
- Spoken words (computed): 1399
- Already set (do not supply): none

### Source block (context only)

```text
Author: Stephen Adly Guirgis
ISBN: 978-0822220824
Publisher: Dramatists Play Service
Date (Month/Year): July 2006
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 2: From the moment he planted a kiss on Jesus of Nazareth in the Garden of Gethsemane, Judas Iscariot sealed his own fate:

ACTOR 1: To be remembered as history’s most famous traitor.

ACTOR 2: But by identifying Jesus to the Jewish authorities, Judas set into motion the series of events that became the foundations of the Christian faith:

ACTOR 1: Jesus’s arrest, his trial,

ACTOR 2: His crucifixion, and eventually his resurrection.

ACTOR 1: Given how little we actually know about him from the Bible, Judas Iscariot remains one of its most enigmatic figures.

ACTOR 2: In recent years, the discovery of the long-lost Gospel of Juda, has led some scholars to reconsider his role,

ACTOR 1: And even to ask whether he might have been unfairly blamed for betraying Jesus.

TOGETHER: The Last Days of Judas Iscariot by Stephen Adly Guirgis
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles: Actor 1: Judge, Satan, Jesus Actor 2: Gloria, Bailiff, Attorneys, Judas

JUDGE: (Pg 8-9) Next case!

GLORIA: Between heaven and hell – there is another place. This place: Hope. Hope – is located right over here in downtown Purgatory.

JUDGE: Next case, Bailiff!

GLORIA: Now, Purgatory, contrary to popular belief, has plumbing and bodegas, and they even got a movie theater and a little park that people can walk their dogs at. Hope – well, it ain’t got none a that, and it definitely don’t smell good.

JUDGE: Next case!!

GLORIA: Now Hope, it changes with the times, but has stood always as God’s gift to the last of his children. In Biblical times, Hope was an oasis in the desert. In medieval days, a shack free of plague. Today, Hope is no longer a place for contemplation – “litigation” being the preferred new order of the day.

JUDGE: Where’s my damn bailiff?!

BAILIFF: Here, sir

JUDGE: Then call the next damn case!!!

BAILIFF: Yes, sir. God and the Kingdom of Heaven and Earth versus Thorseen the Implacable: motion to appeal!

JUDGE: Denied – Next case!

BAILIFF: God and the Kingdom of Heaven and Earth versus Benedict Arnold –

JUDGE: Aw, hell no!

BAILIFF: God and the Kingdom of Heaven and Earth versus Judas Iscariot –

JUDGE: -- Judas Iscariot?! Who brings this crap before me?!

PROSECUTING ATTORNEY: (Pg 34) Prosecution now conjures Satan, Prince of Darkness, to the stand! (Satan enters, waves amiably to the jury) (Pg 35-37) So . . . Dark One, tell me: Did you ever have any conversations with Judas Iscariot prior to his selling-out of Jesus Christ?

SATAN: No, I did not.

P ATTORNEY: Never “entered into him” as I believe Saint Luke’s Gospel puts it?

SATAN: No. Quite sure.

P ATTORNEY: Well, then, how ‘bout after he did the deadly deed? Did you speak with the Savior Betrayer then?

SATAN: I spoke to him, yeah.

P ATTORNEY: Care to share?

SATAN: Not a problem. I appeared to Mr. Iscariot at a bar and grill shortly after the night in question.

(Scene Break) - (Actor 2 assumes the role of Judas and Satan observes him)

SATAN: When I encountered Mr. Iscariot, he appeared to have already taken full advantage of the Happy Hour . . . . (to Judas) Oh. Hello, friend. How are you this evening?

JUDAS: (obviously intoxicated) “How am I this evening?” What are you, a maître d’, man?

SATAN: I’m Clementine. Clementine of Cappadocia.

JUDAS: Yeah?! Well why don’t you go home Cappa-douche-a, okay?!

SATAN: Doe-sha -- Cappa-doe-sha.

JUDAS: Well lemme ask you something – Cappa-doucha-a – do I look like someone who [cares] where you’re from? Leave me alone!

SATAN: I will. Thanks for the advice. (Starts to leave)

JUDAS: Hey!!!! . . . Where you going?!

SATAN: It seems you prefer to be alone.

JUDAS: Why would I prefer that?! What’re you saying: I look like some kinda Lone Wolf? So, what’s your name?

SATAN: . . . Clementine . . of Cappadocia . . . ?

JUDAS: I’m Judas, Judas Iscariot. You never heard of me?

SATAN: Nope.

JUDAS: You don’t get around much, do ya? (Beat) (Pg 38-39) Hey man, If I told you something corny, would you think that I was, like a [jerk]?

SATAN: Not at all.

JUDAS: Okay . . . I’m kinda mildly afraid of going to hell.

SATAN: Why?

JUDAS: Minor incident last night – a miscalculation on my part – nothing serious.

SATAN: Well, one thing I can tell you about hell: As an eternal destination, it’s apparently vastly underrated. Hell is nothing more than the absence of God, which, if you’re looking for a good time, is not at all a bad thing.

JUDAS: Even if I did something, perhaps, a little controversial?

SATAN: Hey, I wouldn’t worry about going to Hell. God understands.

JUDAS: Yeah, but, don’t choices have, like consequences?

SATAN: C’mon, you really think we have a choice?

JUDAS: Okay, well, say, what if someone were to betray, for example . . . the Messiah –

SATAN: -- You mean the Messiah, Messiah? Well, since you asked, I guess I’d say that this guy . . .

JUDAS: Cuz this is just some typo-theoretical guy here –

SATAN: Right. I’d say that if this clown we’re talking about betrayed the Messiah, that probably, “It would’ve been better for that man if he had never been born.”

JUDAS: Never been born?!

SATAN: Hey . . . you asked.

(Scene Break) – Courtroom where the defense attorney is cross-examining Satan.

DEFENSE ATTORNEY: (Pg 66-67) Mr. Satan, you’ve had a long standing feud with God, correct?

SATAN: No. I love God.

D ATTORNEY: You love God? (Pg 69-70) Mr. Satan! What specifically do you love about God?

SATAN: I don’t know where to begin.

D ATTORNEY: Pick a spot!

SATAN: I love God because He is all-powerful and all-forgiving. I love God because his justice is perfect. I love God because God loves me.

D ATTORNEY: God loves you?!

SATAN: Very much. Gift basket at Christmas – Hallmark greetings on all the major holidays.

D ATTORNEY: Mr. Satan – does God love Judas Iscariot? Yes or no?!

SATAN: Go love everybody.

D ATTORNEY: And yet Judas is in hell – so what use is God’s love to Judas if my client is allowed to languish in damnation?

SATAN: Your client is free to leave whenever he wants to – in fact, I wish he would – I could use the room.

D ATTORNEY: That’s not true and you know it! -- The real truth is that God’s love is conditional – isn’t that right?! You failed to meet God’s conditions, and he threw you in the trash! Judas failed – and he’s in a catatonic stupor!

SATAN: Your client succumbed to despair –

D ATTORNEY: Yes! And if human despair is so powerful as to render God powerless over it, then, what does that say about God?! Either God’s not all-powerful and therefore useless – or – God’s love is conditional which renders that love false and unworthy! Which one is it? Is God powerless or spiteful – I am ordering you to answer!

SATAN: (not unkindly) You’re powerless and spiteful – Not God. I’m truly sorry you feel that way.

D ATTORNEY: . . . Nothing further.

TRANSITION: Court is now dismissed (Scene break)

(Scene opens on Judas in his own hell – he may be humming, singing, murmuring to himself, perhaps echoing the phrase “I am” aloud as Jesus speaks the next lines)

JESUS: (Pg 70-73) (Makes his way toward Judas as he speaks to the audience) Right now, I am in Fallujah. I am in Darfur. Right now, I am on Lafayette and Astor waiting to hit you up for change so I can get high. . . I was in that cave with Osama, and on that plane with Mohammed Atta . . . And what I need you to believe is that if you hate who I love that you do not know me at all. I am every last one. I love every last one. People ask of me: Where are you? I ask you: Where are you? (to Judas) Judas . . .

JUDAS: Who’s that?

JESUS: Is it ever anybody else, Judas? (Pause) I miss you. (Jesus lays a hand on him)

JUDAS: DON’T TOUCH ME! Just, go away . . .

JESUS: I won’t go away.

JUDAS: Well, that’d be a first.

JESUS: I have never gone away, Judas . . . Look at me. (Judas does) I love you, Judas. And all I want – all I want – is to be not just near you – but WITH you. I’m right here, don’t you see that?

JUDAS: You got a lot of nerve – I’ll tell you what I know: I watched you trip over your own dusty feet to heal the sick, the blind, the lame, the unclean – But when I needed you – where were you, huh?!

JESUS: Judas . . .

JUDAS: You forgave Peter and Thomas – you raised Lazarus from the dead – But me? What about me?! You just, you just – I made a mistake! And if that was wrong, then you should have told me! And if a broken heart wasn’t sufficient reason to hang, THEN YOU SHOULD HAVE TOLD ME THAT TOO!

JESUS: Don’t you think . . . that if I knew that I would have changed your mind . . . that I would have? (Beat)

JUDAS: All I know is that you broke me – unfixable – and that I’m here . . .

JESUS: Judas – What if I were to tell you that you are not here? That you are with me in my kingdom even now, and that you have been there since the morning of my ascension and that you have never left? (Judas spits in Jesus’ face)

JUDAS: That’s what I think about you! (Jesus doesn’t wipe it off)

JESUS: (Pg 71) I’m sorry. (Pause) Judas – If a thousand strangers spit on me, I will smile. But if the brother of my heart gives me a passing hard look, then, Judas – I will not sleep that night, nor sleep – at all – ‘til he will let me love him again. (Pg 73-74) If you don’t love me, Judas – then you’re gonna have to look me in my eyes and say it.

JUDAS: I don’t love you.

JESUS: If you don’t love me, then why are you here?

JUDAS: Go!

JESUS: Judas! . . . Judas, don’t you know what would happen the very instant you got down on your knees?

JUDAS: Why on my knees? I’ve been on my knees my whole life! You left me.

JESUS: I never left you.

JUDAS: I would have never believed that you could have left. That you didn’t love me.

JESUS: I do love you . . .

JUDAS: No! Why . . . didn’t you make me good enough so you could have.

JESUS: Take my hands, Judas . . Please.

JUDAS: Where are they? I can’t see them.

JESUS: They’re right here. (Jesus takes Judas’ hand in his)

JUDAS: Where are you going?! . . . . Don’t leave me!

JESUS: I’m here.

JUDAS: I can’t hurt . . .

JESUS: I love you, Judas . . .

JUDAS: I can’t . . .

JESUS: Please love me, Judas.

JUDAS: I can’t.
```

---

## IC-1022: The Last Touchy Feely Drama on the American Stage

- Title: The Last Touchy Feely Drama on the American Stage
- Author (byline): Greg Gamble and Lee Howard
- Work: Not specified
- Publisher: Dramatic Publishing
- Publication date as stated: Feb 1999
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ANDY, PAT, FATHER, SON, ANDY AND PAT, TOGETHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1413
- Already set (do not supply): none

### Source block (context only)

```text
Author: Greg Gamble and Lee Howard
ISBN: 978-0871298966
Publisher: Dramatic Publishing
Date (Month/Year): Feb 1999
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: What if theater had commentators . . . just like sports.

ACTOR 2: You have to be kidding? Commentators? No way!

ACTOR 1: Just imagine it though . . .

ACTOR 2: The Last Touchy Feely Drama on the American Stage.

ACTOR 1: by Greg Gamble and Lee Howard
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles: Actor 1: Andy and Son; Actor 2: Pat and Father

ANDY: Hello, good evening, and welcome to the first and final performance of The Last Touchy-Feely Drama on the American Stage! I'm Andy McCunn, and I'm here with Pat O'Keefe to bring you all the passion, all the pageantry, all the gooey senti-mentalism that's sure to unfold tonight. There's a palpable feeling of anticipation in the air over this crowd as they impatiently crumple their programs and await that inevitable dimming of the houselights. Pat, give us some of your patented prognostications for the evening. What sort of strategies are you envisioning?

PAT: Pow! That's what I predict! [Emerson Tod Fudgee’s] gonna come out with both barrels blazing on the first light cue! Exaggerated walks, exaggerated accents! Lots of spray-on gray in the dad's hair -- be watching for that! And don't be surprised if we get a script loaded with family conflicts culled from actual experiences!

ANDY: Introspective creature of loneliness or just another ass with a typewriter -- you make the call! Emerson Tod Fudgee first came to the public's attention with his play Christopher Columbus: Genocidal Fruitcake. -not that the play was ever performed. But not content with accomplishing nothing, he boldly stepped forward with his next play, Queer God. It was a concept piece performed entirely in cliche. And then, hot on its heels came 1991's musical extravaganza, Victims on Parade!

PAT: A stunner!

ANDY: Certainly, Victims is what Fudgee will be remembered for; from the big, splashy, show-stopping dance number, "Compensatiable," right up to the act one finale, where the Ghost of the Dead Shoplifter descends from the heavens and grants the characters the coveted mantle of victim status.

PAT: And not just the characters, Andy, but I think everyone in that audience felt like a victim. Especially at Broadway prices. Victims is still an unfinished work, isn't it?

ANDY: No one's really sure. Its run off-Broadway was titanically short, closing after only forty-three minutes. So, it's not known if it has a second or a third act. It is, in fact, Fudgee's longest-running play! Who would've suspected an art form that began in the bold, shark-filled waters courageously charted by the nervy aplomb of Tennessee Williams, Eugene O'Neill and Arthur Miller, could have evaporated into a creatively stag-nant, mosquito-infested backwater of emotionally manipulative dreck, celebrating failure as the human experience.

PAT: But the "viva la victim" play has indeed become the "Ol' Yeller" of the art world. And somebody's gotta love it enough to take it out back and ka-pow!

ANDY: It's time for the awesome spectacle to commence! (With overly dramatic. hushed golf-announcer tones.) A hush falls over the crowd . . . a few stray coughs . . . the creaking of seats . . . (Shattering the mood.) Pat! What's the game plan for the opening? Will it be lights up with the first character already on stage, thus thrusting us into the drama? Or are we going to bring the lights up slowly and watch him enter, so we can read his history and his personality in his mannerisms, in his gait?

(PAT rushes to take his place by the huge wipe-board. During the rest of his speeches, PAT rapidly sketches out stats and stick-figures to illustrate his postulations and facts.)

PAT: Well, Fudgee 's opened three of his last five plays with the character already on stage, It's an in-your-face approach that's worked well for him. But, major event that this is, I'd look for a little risk taking tonight; possibly the first character making his entrance in an ambient half-glow of a colored gel . . . pink, purple-some emotional hue.

ANDY: And here comes our first character in the half-light dim of. . . a pink gel! Good call, Pat! (FATHER slowly lowers himself into the chair.) He . . . takes . . . his . . . seat. . . and the fuse is lit on this powder keg of performing art!

(With nothing happening. ANDY fills the void with random commentary whispered dramatically in quick bursts.) Here at 7:08 . . . on a Friday evening in June . . . Emerson Tod Fudgee's bold new work . . .The Last Touchy-Feely Drama on the American Stage . . . The tension's thick in the air . . . Fudgee needs a success here . . . . (Lights up to full.) And it's lights up! We have lights at full on Emerson Tod Fudgee's Last Touchy-Feely Drama on the American Stage! (Pregnant pause. The ANDY wait excitedly, the FATHER does nothing but read his newspaper.) (Sound fix: Knocking on a door.) It looks like the drama's under way! Pat, are we going get some blocking out of this door knock?

PAT: From any other director you might get a cross to go and answer the door . . .

(Diagrams an actor's cross to a door. As all wait breathlessly, FATHER shifts in his chair, but never rises.) But, no! Fudgee's gonna resist the predictable and keep the father stationary . . . (Draws an. X over the chair and makes a "hundred" circles around it.) . . . possibly mixing it into the character devel-opment somehow! (Sound fix: Louder knock at a door.)

ANDY: It looks like we're coming up on the opening line of The Last Touchy-Feely Drama on the American Stage!

FATHER: Come in! (The SON enters. He is dressed in ill-fitting community theatre prop-room clothes and carries a suitcase.)

SON: (stiffly). Hi . . . Dad.

ANDY: Well, there's obviously some painful memories here!

FATHER: (scoffing snort). Hmph! And what's that supposed to mean?

SON: (confrontationally). What?

FATHER: (boiling). Oh, you heard me!

SON: (like a human time bomb). I said, "Hi."

FATHER: (spitting venom). Liar!

SON: (as if he's been hassled for an hour). All right, all right! I said, "Hi, Dad!" Happy?

FATHER: Hmph! (coming apart). What, what, what would you know about happiness, anyway? Huh? Huh? Huh? What would you know about a lifetime of happiness-happy thoughts, happy memories, just one happy marriage? Hmm? Hmm? Hmm? (Takes a long cross and wrings his hands.) Goddammit! Everywhere-suffocating happiness! Tell, me, Mr. High-and-Mighty, Mr. Showboat, tooling around town shoving your precious G.E.D. in everyone's face, tell me . . .

(Right into SON's face) . . . how am I supposed to feel?

SON: . . . Happy?

FATHER: (with anomalous cruelty). What do you think? (SON pauses, showcasing his full compass of frustrated gestures and false-start mumblings.)

SON: You . . . You don't want to know!

FATHER: No! You don't want to know! (Something's eating at him.)

ANDY: Another of those masterful pauses you could drive a truck through! Pat! Are we working towards a revelation?

PAT: Bet the baby on it, Andy! No crossing to speak of, but look for a tum from profile left to profile right to milk some meaning out of it!

FATHER: (gazing off into space). I'm drinking again.

SON: (drops suitcase). Oh, my God!

ANDY: No tum, Pat! No tum, no cross and a very disappointing revelation!

PAT: The feeling of underwhelmment coming over this capacity crowd tonight is very real! They want Fudgee swingin ' for the fences! But right when he should've taken a triple toe-loop he singles out of it and two-foots the landing!

FATHER: (broken and confused). Why did you come back?

SON: I had to be here for Mom's funeral.

FATHER: That was a year ago!

SON: (ashamed of his own rage). Don't you think I know that? (Tears welling up.) You never listened to me . . . ever! Wrapped up in your own little hypocritical world, making us all eat your middle-class Spaghettios and your suburban Wonder Bread! (Lights dim.)

ANDY: The lights are dimming. Are we headed for an early curtain call?

PAT: (can't believe his eyes). No! No! Fudgee, is setting up for the monologue! What's going to happen is they'll take it all down to a single, eerie spotlight, pull an actor forward to the apron of the stage, and have him speak directly to the audience!

ANDY: So, in essence, what we're discussing here is nothing less than the destruction of the fourth wall!

PAT: The total obliteration of it!

ANDY: The father's frozen in tableau and . . . the son is up! Up and headed for the apron of the stage to express for us all the pain we carry with us but can't release without geniuses like Fudgee! (Spotlight on the SON.)

SON: Will he ever know the real me?

ANDY: A question! Perfect for portraying hope as a straw god!

SON: How do you say, "Dad, I just want you to care! I just want you to hold me"?

(Lights up to full. SON returns to his previous place. FATHER unfreezes, while) (wallowing in drama). I'm seeing a psychiatrist.

FATHER: (disgusted beyond belief). In what way?

SON: (courageously). In the only way I know how!

FATHER: I'm ... so sorry.

SON: No, I'm sorry . . . I never told you . . . I'm gay.

ANDY: Oh, my! There's magic in the air tonight! It looks like they're going for the Tony!

SON: Look at me, Dad! I'm gay! I'm gay! I'm gay! I'm gay! Gay, gay, gay, gay, gay, gay, gay! It's not your fault any more than it's not my fault, and it's nobody's fault that it's not anybody's fault!

FATHER: You're not my son!

SON: I'm begging you to accept me and Jeremy!

FATHER: No! I mean you're not my son. You made a confession, now I'm making one! (Dredging up a painful past.) Your mother . . . she had an affair . . . on the very day we were married! (Buries his head. then looks up with his mood swung to a torpid, blank expression.) It's getting dark outside.

ANDY: (golf-announcer-esque), A symbolic line.

SON: (torpid. blank expression). And it's so cold already.

ANDY: (golf-announcer-esque). And again.

FATHER: Is there something you're not telling me?

SON: You know already.

FATHER: But I need to hear you say it.

SON: And I need you to hear me say it. I'm . . . I'm . . . (SON tries and tries to pull some dark secret out of his innards. After stretching out his hands several times with "I'm . . . " he stretches them out and says nothing.)

PAT: The play-action fake!

SON: I'm . . . (SON's dreadful attempts at hauling an admission from his soul reach a fever pitch of overacting.) I'm HIV-positive!

ANDY: And there it is! They're walkin' away with this year's Tony Award!

ANDY AND PAT: Tony! Tony! Tony! Tony! Tony! Tony! Tony! Tony

ANDY: And that'll about wrap it up here for The Last Touchy-Feely Drama on the American Stage! Emerson Too Fudgee, previously known as a spectacularly unsuccessful hack, proves in the pinch to be a spectacularly successful hack, bidding farewell to an endearingly trite and delightfully derivative theatrical genre that I'm sure will be sorely missed!

PAT: [I’m] Pat O'Keefe

ANDY: [And] this is Andy McCunn saying,

TOGETHER: G'night!
```

---

## IC-1023: Leagues Apart

- Title: Leagues Apart
- Author (byline): Jane Nicolaas
- Work: Leagues Apart
- Publisher: SpeechGeek
- Publication date as stated: 2010
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1509
- Already set (do not supply): none

### Source block (context only)

```text
Leagues Apart by Jane Nicolaas
ISBN: 978-1-61387-032-7
Copyright 2010 by SpeechGeek.
Free performance of this play for high school and college level
competitive forensics is permitted. All other rights reserved.
This PDF version of this selection, e-published in 2011, is identical to the
printed published version of this same publication dated 2011. This
statement along with the entire printed PDF of this publication must be
presented at any National Forensic League District or National event for the
script to comply with NFL rules per the request of the Executive Director.
This and other selections of quality performance literature for competitive
oral interpretation are published by SpeechGeek.
For more information and performance rights, contact SpeechGeek.
SpeechGeek
806 Brownstone Way
Bowling Green, KY 42104
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
(A Negro League baseball game in Missouri. Satchel is on the pitching mound and Josh is approaching the plate as the batter.)

RADIO. Ladies and gentlemen, it’s a great spring day in 1945 and that means one thing and one thing only: baseball. Today’s Negro League All-Star game features some of the greatest colored players in the game: Satchel Paige and Josh Gibson.

JOSH. (swings the bat as he approaches the plate) There he is: Satchel Paige. So good he could strike out Jim Crow.

SATCH. (loosens up his pitching arm) And the Black Babe Ruth, Josh Gibson. How many homeruns you got, boy?

JOSH. Ask me again after I get this next one off of you.

SATCH. You can’t hit what you can’t see.

JOSH. Good one, old man! Sure sweet of you to climb out of your rocking chair to come play baseball with us?

SATCH. Yeah, Big Man. You keep talking while I strike you out. (pitch) What was that? Strike one?

JOSH. You gonna need two more ‘fore you can start bragging.

SATCH. Yeah, alright. I’m just waking up.

JOSH. I got something to wake you up.

SATCH. (pitch) That looked like number two. I don’t know. I mean, I am old. My eyes ain’t what they used to be. Was that number two?

JOSH. Quit your showboating and pitch that ball. I get sick of you sometimes. Messing around. Not today.

SATCH. (pitch)

JOSH. (hit) Oooo-ee. That looks pretty, don’t it?

SATCH. Damn man, I think that would have gone out of Yankee Stadium.

JOSH. Someday it will, I think.

SATCH. Yeah.

INTRO

RADIO. Now from the world of sports: On this day, April 3, 1945, Major League Baseball Owner Mr.

Branch Rickey has announced the formation of the Brooklyn Brown Dodgers.

(Transition to a clubhouse where Satch is kneeling by a radio, fascinated by the news. Josh limps in behind him, beat up.)

SATCH. (not looking at Josh) Oooooee! Did you hear that?

JOSH. And what makes you think they interested in you?

SATCH. I say white folks is crazy, not stupid. If Rickey wants to fill that ballpark, he gonna need Satchel Paige.

JOSH. Huh? (winces)

SATCH. (looks at Josh) Man, what the hell done happen to your face?

JOSH. These barnstorming games we’ve playing are all well and good at paying to feed my family, but they also a good way to get my ass kicked.

SATCH. Why don’t you let them win, Big Man? They don’t hit ya if they think they’ve whipped ya, know what I mean?

JOSH. I didn’t mean to. It was a one-handed swing for crying out loud!

SATCH. You hit a homerun with one hand?

JOSH. It was a change-up in the eighth. Total accident, I swear. (They stare at each other and then burst out laughing.)

SATCH. Well alright, Big Man, meditate on this: me and you. We go to Brooklyn together. What do you say? No more barnstorming games, no more angry Southerners chasing us outta Tuscaloosa or Memphis or wherever—

JOSH. No more letting them white boys win. (marvels at the opportunity for a moment then gets sarcastic) I don’t know… I mean I want to go with you, but you look like you slowing down there a little bit. I might have to go by myself.

SATCH. Yeah, I look slow and you look like you getting a little flabby there in the middle.

JOSH. Oh that? That’s just them pork chops your wife been feeding me.

SATCH. Oh yeah, while I was over at your mama’s house? She told me about that. On second thought, Paige and Gibson on the same team? I don’t think the Big Apple is big enough.

JOSH. Yeah, you best keep your old crusty butt here in Missouri then.

RADIO. Rumors coming through that Rickey’s negro baseball team, The Brown Dodgers, is rumored to be a Trojan horse for the notoriously controversial Mr. Rickey to sign colored players to his Major League team: the Brooklyn Dodgers.

(Transition to Josh’s house at 2am. There is a loud knock on the door phone. Josh grabs his bat and cautiously answers the door.)

JOSH. Who is this?

SATCH. Big man, it’s me.

JOSH. Satchel, I thought you was some angry mob.

SATCH. Big man, is some angry mob gonna knock? Hell, no.

JOSH. Ok, fine. But with what’s been happening in Gainsville and—

SATCH. Look man, never mind that. I’ve been thinking about this Brown Dodgers thing. There is no money in negro league baseball, right?

JOSH. You got that right.

SATCH. So what do you think mister moneybags Branch Rickey is doing?

JOSH. Ok, I’ll bite. Why is Branch Rickey sending scouts around?

SATCH. Maybe it ain’t for the Brown Dodgers…maybe it’s for the Brooklyn Dodgers.

JOSH. Come on, Satch, that’s crazy.

SATCH. It’s the only thing that makes sense. And I feel this, Big Man. I feel this.

JOSH. You better not be playing with me. If you are, them mobs are gonna be the last of your worries.

SATCH. I’ve been around this thing time and again, and I am sure that this is it. We going to the Major Leagues, baby. Big man, you still with me?

JOSH. I’m with you brother. All the way to the majors, Satch.

RADIO. Tension is mounting today after Mr. Rickey issued the following statement: “If a black boy can make it on Okinawa, he can make it in Major League Baseball.”

(Transition to Satchel’s house, 2am. Satchel finds Josh drunk and beat up again on his front porch.)

SATCH. Josh? Josh, man? You ok?

JOSH. Hey, Satchel. Satchel Paige. I’m fine. I’m fine.

SATCH. I heard what happened. Did they hurt you real bad?

JOSH. Nah. Nothing some Kentucky bourbon couldn’t make right as rain.

SATCH. Come on, man. (helps him to his feet)

JOSH. Hey, you know what Dizzy Dean said to me? Dizzy Dean said that homerun I hit off of him in Omaha in ’36 was the best one he ever seen. He ain’t never seen another like that. Said not even the white boys could have hit it better.

SATCH. You just keep it together, Big Man. Soon enough we’ll get there and you won’t have to deal with this anymore.

JOSH. My head hurts, Satch.

SATCH. Let’s get you to a doctor.

JOSH. I ain’t going to no doctor, Satch. (suddenly angry) Is the world really changing? You say it is. But I just don’t even know. Does this life feel any different than my daddy’s? Losing when they say lose, getting whooped for no damn reason, waiting for the chance to stop saying I’m sorry for being colored.

SATCH. Look, Truman’s talking about integrating the military. How long you think it gonna be before it’s our turn?

JOSH. You think it’ll be us? I mean, what if it ain’t? What if we’re too old or too black or something? I just think…I don’t know if I could handle that, man.

SATCH. Hey, I’m already old. Ain’t no sense in worrying about getting older. And who else they gonna find who can hit like Josh Gibson?

JOSH. No one.

SATCH. That’s right, no one. Not even the white boys could hit it better.

RADIO. The Brooklyn Dodgers have signed Jackie Robinson as the first colored baseball player in Major League history. The young, articulate, former army officer comes as a surprise to many.

(Transition to clubhouse where Josh and Satch are listening to the radio.)

JOSH. (frustrated, angry scream) No!

SATCH. Jackie Robinson?

JOSH. They know! They know that if I go up there I’d break all those white boys’ records. Babe Ruth… Gehrig…every damn one. They not gonna let that happen. They picked Robinson cause he can’t do it.

SATCH. (Is so shocked, he has no response.)

JOSH. We did it all didn’t we? Day in and day out. We’ve been spit on and cussed at and beat up. These scars, don’t they buy me nothing? Not even one swing? And who the hell is Jackie Robinson?

SATCH. Why you asking me that?

JOSH. Cause you always got the answer.

SATCH. I ain’t got no answer. I got no answer for you and no answer for me. I thought for sure them scouts were there to see—

JOSH. This is all your fault.

SATCH. My fault?

JOSH. You damn showboat. You make it the Satchel Paige Show and the rest of us can’t even—

SATCH. Now wait just a damn minute.

JOSH. They didn’t want some showboating old clown to be the first—

SATCH. …or a fat, sloppy, beat-up drunk. If you was the first, there’s no way any one of us would have a chance!

JOSH. …

SATCH. Big man. Big man, I’m sorry.

JOSH. (breaks down) It’s all I ever wanted. To prove I was as good as the white boys.

SATCH. You’re not. Josh, you’re better. You’re the best player I ever seen. Maybe even including myself.

JOSH. You still think that?

SATCH. I always will, and someday those scars you got on you are gonna fade. They gonna disappear under them big league lights.

JOSH. And what if they don’t?

SATCH. They will. You gonna be the first black man to hit a homerun outta Yankee Stadium, baby.

JOSH. You gonna be the one to throw it.

SATCH. This ain’t nothing, Big Man. We rained out today, we’ll play tomorrow. We are going to the majors. And someday everyone gonna know our names and know what we did.

JOSH. Even if they don’t. I’ll know what we did, and I’ll be proud just the same.

RADIO. And today Jackie Robinson issued the statement, “I know I’m here now because of the great players who kept the dream alive. I may be the first to break the barrier, but it wasn’t my work alone that got me here.”

(Transition to a Negro League baseball game in Missouri.

Satchel is on the pitching mound and Josh is approaching the plate as the batter.)

JOSH. You warmed up, old man?

SATCH. Big man, I ain’t never cooled off.
```

---

## IC-1024: Mandate

- Title: Mandate
- Author (byline): Kelly Younger
- Work: Best Ten-Minute Plays 2014; Pg 100-107
- Publisher: Smith and Kraus
- Publication date as stated: June 2014
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MARC, DREW
- Teaser before the introduction: Yes
- Spoken words (computed): 1497
- Already set (do not supply): none

### Source block (context only)

```text
Author: Kelly Younger
Book: Best Ten-Minute Plays 2014; Pg 100-107
ISBN: 978-1575258867
Publisher: Smith and Kraus
Date (Month/Year): June 2014
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Men befriending men — it sounds like a simple endeavor,

ACTOR 2: But after 200,000 years on the planet, American men appear to be stuck in a “friendship recession”

ACTOR 1: In a 2021 survey, less than half of the men said they were truly satisfied with how many friends they had,

ACTOR 2: While 15 percent said they had no close friends at all — a fivefold increase since 1990.

ACTOR 1: That same survey found that men were less likely than women to rely on their friends for emotional support or to share their personal feelings with them.

ACTOR 2: But not today . . . A humorous (but oh, so true) look into the

TOGETHER: Mandate by Kelly Younger
```

### Performance text (classify this)

```text
A crowded sports bar. Two bar stools. Two drinks. One bowl of peanuts. Sounds of basketball game on TV. In the blackout, DREW shouting "C'mon! Give it to me! You know you want to!" Then as the light comes up, we see Drew violently and awkwardly giving the Heimlich to Marc. Marc launches a peanut from his mouth. A moment of relief

MARC: What the hell dude? DREW: You're welcome.

MARC: I wasn't choking. DREW: Sure you were.

MARC: I was eating a peanut. DREW: That got lodged in your throat.

MARC: Not until you started crushing my lungs.

DREW: Wait, seriously? You weren't choking?

MARC: That's what I was trying to say but you were shouting and thrusting. Where did you learn the Heimlich, prison?

DREW: (hands to throat) You gave the universal sign for choking.

MARC: I was just adjusting my collar. I told you I was coming straight from a haircut.

DREW: Well, it looks great.

MARC: Thanks?

DREW: Guess that was pretty awkward.

MARC: Yeah. Awkward.

DREW: But you're fit, man. (poking him) Could feel a pretty tight little core while I was squeezing you.

MARC: Not any less awkward.

DREW: I put on some sympathy weight when Hillary first got pregnant-with Addison. She used to say we were having twins. One in her belly, one in mine. Then when we had Bridgie I was like, bring on the sweatpants! (MARC lifts his drink, DREW quickly follows and overeagerly cheers him, almost smashing his mug.) Here's to good friends. Tonight is kind of special.

(MARC doesn't really know how to respond.)

MARC: So, Beth told me you're a teacher.

DREW: Earth science and driver's ed. 124 kids. All girl's school.

MARC: All girls. That's a lot.

DREW: Don't have to tell me. But I can text 90 words in 2 minutes 26 seconds, so, you know, I'm kind of a popular teacher. And I know the words to every One Direction song. Go on. Try me.

MARC: With what?

DREW: One Direction challenge.

MARC: I don't know what that is.

DREW: Seriously? They're like the Monkees for the new generation. (singing, throwing out boy-band gestures) You don't know you're beautiful! Oh-oh! That's what

MARC: (cutting him off) Jake's kind of more into Star Wars.

DREW: Ah, man. I'd give anything to have a son. Don't get me wrong, I love my girls. I'm just, you know, kind of out numbered. I brought out all my old action figures and the girls just wanted to have a pool party with Barbie and I was like, Bobo Fet does not swim.

MARC: He's way into it. I do this funny thing with Jake, whenever we go through the security gate at our condo, it opens automatically, but I put my hand up like a Jedi and act like I'm giving it a force push, and when it opens, you should see his face. (Long moment)

DREW: (with deep admiration) You're amazing.

MARC: I'm sure you do loads of stuff like that.

DREW: Addison and Bridgie paint my toe nails. In fact, my toenails are always painted. Wanna see?

MARC: I'm good.

DREW: Cool.

MARC: Cool. (A moment)

DREW: Can I tell you a secret?

MARC: I think you just did.

DREW: I'm a brony.

MARC: A what?

DREW: A bro who likes My Little Pony.

MARC: That's a thing?

DREW: Huge. My girls got me hooked. We threw a party for the coronation episode where Princess Celestia finally gave Twilight Sparkle her wings. Man. That was a great night. (beat) Friendship is magic. (MARC takes a drink and DREW mirrors his every move.) This is nice. I'm really glad our wives set this up.

MARC: (focusing on the game) Yeah.

DREW: They totally knew we'd get along. And it's so hard, you know, with work and kids and everything, I mean, how do people even make friends anymore? Especially guys, you know? Like there's no way guys just become friends like you did in college. Had a class together or in a frat or something. Now it's all about do the spouses get along, and what if they do but their kid is a *jerk* or the kids get along but the parents are *jerks* and do you want to be best friends?

MARC: (beat) What's that?

DREW: Do you want to be my best friend? (MARC laughs, then stops.)

MARC: You're serious.

DREW: I mean, like, unless you've already got one. Do you?

MARC: A best friend?

DREW: And wives don't count. I'm talking guy best friends. You already have one?

MARC: Dude. I haven't really thought about it like that since

DREW: Since what?

MARC: Grade school.

DREW: So do ya?

MARC: I've got plenty of friends.

DREW: Not counting work.

MARC: Ok, yeah.

DREW: And not counting dads from your kid's school.

MARC: Ok. Yeah, still got 'em.

DREW: And not counting guys from college. Or Facebook.

MARC: Well who's left? You basically eliminated all my social circles.

DREW: Hillary's got like ten best girlfriends and they go out and they talk on the phone every day and confide in one another and chat about work and yoga and how their bodies are changing. And this ... this is what guys should talk about, right?

MARC: (thinking) No.

DREW: But our wives do all the time about everything and I mean everything like shopping and gossip and your yeast infection.

MARC: You know about that? And it was not a yeast infection. (subtly adjusting his crotch) It was a fungus.

DREW: Made of yeast. But don't be embarrassed bro, it happens. You just gotta wash better after the gym.

MARC: Dude. I don't need your hygiene advice. Can we please just watch the Lakers?

DREW: Oh. Are we moving too fast? Or you already have a best friend?

MARC: No. I mean, yeah . . . that's right, I do.

DREW: Who?

MARC: The best man at our wedding. JD. He lives in Baltimore now.

DREW: How often do you guys talk?

MARC: Enough. I guess.

DREW: Like, once a week, or what?

MARC: Like . . . I don't know. I guess- (beat) Huh. When was the last time I talked to him?

DREW: See? He was your best man and you don't even talk anymore.

MARC: We don't have to. He's just the kind of guy that just, you know, we don't need to talk a lot.

DREW: I'm not like that.

MARC: Really.

DREW: And I don't think most guys are either, we just think we're supposed to act that way.

MARC: Didn't you have a best man?

DREW: Hillary's brother. He doesn't like me all that much. Thinks I come on too strong.

MARC: (beat) Look, Drake.

DREW: Drew.

MARC: Sorry. Drew. Listen, Beth told me her friend from yoga ... your wife ... had a cool husband and we should meet up and I said, ok, sure, thinking we would just, you know, meet up, but, all this best friends forever kinda thing is just a little ... I'm just not really ... in the market for one, you know?

DREW: (beat) That's cool.

MARC: Let's just watch the game, be guys. In silence. (DREW plays it off. They both watch the game. Then Drew takes out a small pink notebook and pen, scratches something out.) What's that? (eyeing his pad) Did you just cross my name off of some ... list? What is this? (picking up pad, reading) "Possible candidates for my new best friend." (He flips through pages. Clearly, a long list.) How many ... I'm at the bottom? Dave Scales is on here? That guy's a tool. How is he higher up on the list than me?

DREW: What's it matter now? I've run out of names.

MARC: Wait, seriously, you've done this with all these guys?

DREW: And none of them ever called for a second date.

MARC: Maybe because you're calling it a date.

DREW: What would you call it?

MARC: Just ... hanging out. Getting to know each other. Kind of like ... kind of like ... yeah, I guess ... (Stands, begins to pull wallet out.) Look. You seem like a great guy.

DREW: Here we go again.

MARC: But it's not really a great time for me, right now, and I . . . what's happening? (DREW's trying to keep it together, holding back tears. MARC eyes him, then DREW starts to lose it. MARC looks around. Clearly they have everyone's attention.) You ok? Hey. Buddy.

DREW: (through snot) I'm not your buddy. You've made that perfectly clear.

MARC: Woah. Seriously, pal.

DREW: (losing it) I'm not your pal either. Or your amigo. Or your dawg. Or Edgar Allen Bro. I used to be fun. Guys used to beg to hang out with me. But now I'm on list-serves with mommy and me groups. The last sporting event I went to was a Silpada jewelry party. I've become this overweight, pathetic, whiskered . . . You gotta help me! (He collapses into MARC, a blubbering mess. MARC is stunned, embarrassed, trapped. But then he pats DREW on the back.)

MARC: There there. (But DREW is still weeping. This time, MARC actually pats him with sincerity, gently holding the big lug.) Hey. It's ok. It's going to be ok. (DREW eventually pulls himself together, embarrassed. He pats under his eyes with his ring fingers.)

DREW: Ok. I'm ok. I'm all right.

MARC: Look, man. I get it.

DREW: You're just saying that because I snotted on your sweater vest.

MARC: No, seriously. I do. I mean. If you asked me in high school if I would even be the kind of guy who wore sweater vests, I would have laughed right in your face. You think I wanted to grow up and be this sorry cubicle jockey who works sixty hours a week pushing numbers around? You want to hear something sad? The only thing I excel at ... is Excel. I make good spreadsheets. That's it. And my freaking life has become this massive, over-organized spreadsheet with cells that just go on and on and on. It never ends. And it's sucking the life out of me, one spread-sheet at a time. (Bites his lip.) Damnit. You're gonna make me cry now.

DREW: It's ok. Spreadsheets are hard.

MARC: They're really hard!

DREW: But it feels better to talk about, doesn't it. (A moment. MARC nods.)

MARC: Look. I don't have a lot of time right now, with work and the kids and all, and, I don't know if l'm like best friend material here or anything but ... you can keep my name on the list ... if you want. And I'll ... you know ... I'll call you ... for a second, you know, whatever this is. And maybe we can try it again. See where it goes. Cool?

DREW: Cool. (They both stare forward in silence, watching the game. A big, delighted grin grows across DREW's face.) We totally need nicknames

MARC: We totally do not.
```

---

## IC-1025: Minimalistic Men

- Title: Minimalistic Men
- Author (byline): Spencer Davis
- Work: Best Ten-Minute Plays of 2012, Pgs 161-168
- Publisher: Smith and Kraus
- Publication date as stated: June 2013
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: JERRY, BRAD, SETTING, ERRY
- Teaser before the introduction: Yes
- Spoken words (computed): 1625
- Already set (do not supply): none

### Source block (context only)

```text
Author: Spencer Davis
Book: Best Ten-Minute Plays of 2012, Pgs 161-168
ISBN: 978-1575257938
Publisher: Smith and Kraus
Date (Month/Year): June 2013
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: According to Shakespeare: “All the world’s a stage, and all the men and women merely players.”

ACTOR 2: Just lines from another play, right? But what if they were true?

TOGETHER: Minimalistic Men by Spencer Davis
```

### Performance text (classify this)

```text
JERRY: Mid-twenties. Maybe handsome, but at lights up, he's disheveled, having made a horrifying discovery.

BRAD: His roommate. Same age. Maybe frumpy. Clueless to the truth.

SETTING: Their apartment. Somewhere in America. TIME: Present day.

Lights up on JERRY, standing DR, dialing his phone.

JERRY: (Pg 161-168) Come on, Brad, you son-of-a-gun, pick up. (puts phone to ear, waits) Pick up, pick up, pick up.

BRAD: (D.S.) Hey, this is Brad. If you're hearing this, I didn't pick up like you were anxiously hoping I would. So when the thing goes beep, say stuff. Pause. Then "beep. "

JERRY: (into phone) Brad, it's Jerry. Look, I'm coming home. There's something really important I have to tell you, and we don't have much time. Just, um, don't. Do. Anything. I'm coming home. There's something really important I have -- *Damn*, I already said that. Look, I'm coming home. *Damn*. I said-*Damn*. (hangs up) *Damn.* (looks at audience, furious) Do you people mind? JERRY exits R.

Lights up on C, where BRAD sits on the couch, talking on the phone.

BRAD: (into phone) What do you mean I am? No way. You're the best. Okay, fine. But only if you do. JERRY re-enters R, runs up to the side of the couch.

JERRY: Brad, we need to talk.

BRAD: (oblivious to him) No, you hang up first. No, you. No, you first. Gosh, you're ... what a rascal. JERRY anxiously taps BRAD on the shoulder. (Brad still smiling) Oh, hey, Jerr. (into phone) No, you first. Okay, okay, fine. At the same time then.

JERRY: Brad, we need to

BRAD: One, two, three. (pause, then laughs hysterically) Well, you didn't either.

JERRY: (sternly) Brad. Please. Come on. BRAD looks at him, annoyed.

BRAD: (into phone) Hey, I gotta go. Okay. I'll call you back, Mom. (hangs up phone) Have you no respect?

JERRY: Brad, I'm sorry. But this can't wait.

BRAD: Really? 'Cause I get to talk to my mom once a week. Once a week, for one hour. That's all the guards will allow her. And all I've asked is that you allot me that one hour to speak to her in peace.

JERRY: I know, Brad, but this can't wait an hour-

BRAD: (looks down at caller I.D.) Oh, and look. I have one missed call.

JERRY: Yeah. That was me calling.

BRAD: Oh. Well remind me to call you back later. BRAD walks DL, to the stove. JERRY watches him; already he is almost drained.

JERRY: Brad. What are you doing?

BRAD: I'm making ramen noodles. Is that alright, or are you going to interrupt me before I add the flavoring?

JERRY: (desperately) How can you think about food at a time like this?

BRAD: Most people think about food at lunchtime. JERRY approaches BRAD, grabs his arm.

JERRY: Listen, leave the noodles for a second. There's something very important I need-

BRAD: The noodles'll burn.

JERRY: If you don't listen to me, if you don't take me serious for two seconds, there aren't gonna be any noodles. This, above all else, quiets BRAD. This might sound strange, but I need you to listen: What we have here doesn't exist. (pause)

BRAD: Huh?

JERRY: All of this- (motions to the apartment) None of this is real.

BRAD: (“Nice try, bud") Yeah, right. That lampshade over there alone is made of real wool. Trust me, I checked. It's posh.

JERRY: No, that's not what I - (a new approach) Right now, we're on display. (pause)

BRAD: You are high as hell.

JERRY: No.

BRAD: Yeah, yeah, you are. I can see it in your face.

JERRY: Brad-

BRAD: Why do you do that to yourself? You smoke and then you run in spitting conspiracy theories. Like that time you swore, up and down, that Rachel Ray was the one who killed Bobby Kennedy.

JERRY: Read her book! It's all in there!

BRAD: And whenever I tried to convince you otherwise, you wouldn't stand for it. (pause) I can't prove it, but I'm pretty sure you overfed my goldfish in revenge for me debunking your theory

JERRY: Brad, we're in a play! Silence. We're in ... we're in a play. This is not our apartment, this is a stage. And look. Look. (points BRAD towards audience) Do you see them?

BRAD: See ... ? See who?

JERRY: Keep looking. One. Two. Three. "Stop acting.” JERRY snaps his fingers. House lights come up

(and gradually fade down again) as BRAD sees the audience for the first time.

BRAD: Wh-who are they?

JERRY: May I introduce ... the Audience.

BRAD: And, and they came here to what, watch us? Do what?

JERRY: I don't know. This. Talk. Disagree. Fight. Whatever.

BRAD: I, I need to sit down. (sits down on couch; looks at it) Holy *crap*! Where's our couch?

JERRY: That's what I've been trying to tell you. It wasn't ever a couch. Just two chairs pushed together. This whole thing uses a minimalistic set.

BRAD: (nods knowingly) A minimalistic set. Right. (pause)

JERRY: You have no idea what that means, do you?

BRAD: Nope. (pause; a thought comes to him) You know ... maybe a life on display isn't so bad, though. I mean, we can adapt. With people watching us, we'll be like celebrities. BRAD preens in front of the newly discovered spectators.

JERRY: Can you stop being so optimistic about this? You're forgetting the most important part of this whole thing. (pause) Every play ends. The preening ceases. A moment of realization.

BRAD: Oh *crap*.

JERRY: That's right. "Oh *crap*." That's what I really came here to tell you. Because see, when the play ends, so do we. When the lights black out- (snaps his fingers) We're dead.

BRAD: W-When is the play supposed to end?

JERRY: That's the part I don't know. A play can only last for so long. "August: Osage County" ran for three and a half hours. Even "The Norman Conquests" lasted about ten hours.

BRAD: (hopeful) Great! So we might still have some time.

JERRY: Nah. I have a feeling we have ninety minutes, tops. You better just pray that we're not in a one-act.

BRAD: (nods knowingly) A one-act. Right.

JERRY: ... Never mind.

BRAD: But why does the play have to end? Why would it? I mean- (points to audience) They don't have to stay here. We could keep on

JERRY: Because that's what the Playwright wants. We have to do or say whatever He wants us to do or say.

BRAD: So some hipster types something into Microsoft Word and suddenly it’s the Holy Grail.

JERRY: Well ... the Grail is a cup, but yeah, that's the idea. BRAD rubs his forehead, thinking. Then, a curious realization.

BRAD: How did you know?

JERRY: How did I know-what?

BRAD: All this. That we're in a play. That some guy is writing all this.

JERRY: (realizes) I ... don't know. I guess He sort-of imparted the knowledge to me. Before the play began.

BRAD: You think He wanted you to know that you're in a play.

JERRY: I guess so. Heck, everything we're saying right now might seem spontaneous, but it's all been ... preplanned. (pause)

BRAD: YOU'RE A . . . . YOU’RE A . . . *Booger eater*!

JERRY: (taken aback, then) WELL, YOU'RE A *SLIMEWAD*!

BRAD: No, not you. I was just trying to catch Him off-guard.

JERRY: Oh. Well, I don't think you can catch Him off-guard. Or Her. Or whatever the playwright is. There's not a line we've said so far that wasn't thought out ahead of time. For example, if I said, "This playwright blows," it's because He actually wanted me to say that.

BRAD: Wow ... So we're written by a misogynist.

JERRY: Masochist.

BRAD: Bless you. (suddenly kisses JERRY; to the audience) Sarah Palin. [Could insert another current political figure here] (looks at JERRY, confused) Oh! I'm so sorry! I didn't-

JERRY: (unfazed) It's okay. That was just the Playwright trying to be edgy ... and topical.

BRAD: (sad understanding) So ... there's nothing we can do to stop this, then.

JERRY: Nope. I suppose in a lot of ways, we're in the same position as the guy who discovered death.

BRAD: How'd he do that?

J

ERRY: I guess he died. The two men look at each other as it all sinks in. Pause for several beats. Then something in BRAD registers.

BRAD: Then why did you tell me?

JERRY: ... What do you mean?

BRAD: I mean, you knew, before you even told me, that this play was going to end, no matter what we tried. So why couldn't you just let me die ignorant of my fate?

JERRY: You'd rather me keep that to myself? I did you a favor!

BRAD: Before you burst in here, and told me about the Audience, and the Playwright, and the Blackout, and the couch, I was fine. I was ignorant, but at least I was happy. If you making me conscious of my death doesn't prevent anything, then why couldn't you have just let me have my peace?

JERRY: (comprehending) Oh. Oh, Brad. Brad, I'm sorry . . . I didn't ... I never considered the implications of ... BRAD scoffs, shakes his head in disgust. Look, don't take this out on me. I can't help that I just did was I was written to do.

BRAD: No. Don't fall back on that "written this way" *crap*! Don't you try to-

JERRY: But I am! We have to do what we're written to do!

BRAD: Really? Well what if I'm written to kick your ass! They scuffle. Its messy, clumsy, and very brief. By the end, BRAD has his hands around JERRY'S throat.

JERRY: (choking, breathless) Stop, Brad! You're giving the Writer what He wants: Conflict!

BRAD: What's that, Jerry? I can't understand you. If I could stop strangling you, I might be able to, but I'm sorry. I'm just doing what I'm written to do! JERRY knees BRAD in the groin. BRAD topples over. Both are lying on the ground, exhausted.

JERRY: No! I won't let you give in. I won't let you have us reach a climactic confrontation! If we do, the scene will only end quicker. BRAD pushes JERRY, one last weak effort, before sitting on the floor with his back against the chairs. Brad-

BRAD: I can't do this, Jerry! I can't let some self-important douchebag decide how and when I'm going to die! I can't let it happen. I don't want to be minimalistic anymore, Jerry. Nothing will ever look the same again. JERRY crawls over to his friend, sits down against the chairs too. I just want it all to end. If it has to, I hope it's soon ... I don't want to have to think about it. JERRY rests his hand on BRAD'S shoulder.

JERRY: I know, I know.

BRAD: I just want it all to end. They look at each other. They accept it. Right ... now. They snap their fingers simultaneously. Lights out.
```

---

## IC-1026: Mr. Big

- Title: Mr. Big
- Author (byline): Woody Allen
- Work: Getting Even
- Publisher: Vintage
- Publication date as stated: Aug 1978
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: KAISER, HEATHER/CLAIRE/ELLEN, WISEMAN, CHICAGO PHIL, SERGEANT REED, THE POPE
- Teaser before the introduction: Yes
- Spoken words (computed): 2177
- Already set (do not supply): none

### Source block (context only)

```text
Author: Woody Allen
Book: Getting Even
ISBN: 978-0394726403
Publisher: Vintage
Date (Month/Year): Aug 1978
```

### Introduction (context only: never use it for content warnings)

```text
Mr. Big by Woody Allen
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Actor 1: Kaiser Actor 2: Everyone Else

KAISER: I was sitting in my office, cleaning the debris out of my .38 and wondering where my next case was coming from. I like being a private eye, and even though once in a while I've had my gums massaged with an automobile jack, the sweet smell of greenbacks makes it all worth it. Not to mention the dames, which are a minor preoccupation of mine that I rank just ahead of breathing. That's why, when the door to my office swung open and a long-haired blonde named Heather Butkiss came striding in and told me she needed my help, my salivary glands shifted into third.

KAISER: What can I do for you, sugar?

HEATHER/CLAIRE/ELLEN: I want you to find someone for me, Mr. Lupowitz.

KAISER: Call me Kaiser, sugar. All right, so what's the scam?

HEATHER/CLAIRE/ELLEN: God. The Creator, the Underlying Principle, the First Cause of Things, the All Encompassing. I want you to find Him for me.

KAISER: Why?

HEATHER/CLAIRE/ELLEN: That's my business, Kaiser. You just find Him.

KAISER: I'm sorry, sugar. You got the wrong boy . . . Unless I know all the facts.”

HEATHER/CLAIRE/ELLEN: (biting her lower lip) O.K., O.K.

KAISER: (to audience) She straightened the seam of her stocking, which was strictly for my benefit, but I wasn't buying any at the moment. (to Heather) Let's have it on the line, sugar.

HEATHER/CLAIRE/ELLEN: My name is not Heather Butkiss, either. It's Claire Rosensweig and I'm a student at Vassar. Philosophy major. History of Western Thought and all that. I have a paper due January. On Western religion. All the other kids in the course will hand in speculative papers. But I want to know. Professor Grebanier said if anyone finds out for sure, they're a cinch to pass the course. And my dad's promised me a Mercedes if I get straight Xs."

KAISER: (to audience) I opened a deck of Luckies and a pack of gum and had one of each. Her story was beginning to interest me. Spoiled coed. High IQ and a body I wanted to know better. (To Claire) What does God look like?

HEATHER/CLAIRE/ELLEN: I've never seen Him.

KAISER: "Well, how do you know He exists?

HEATHER/CLAIRE/ELLEN: That's for you to find out.

KAISER: Oh, great. Then you don't know what He looks like? Or where to begin looking?

HEATHER/CLAIRE/ELLEN: No. Not really. Although I suspect He's everywhere. In the air, in every flower, in you and I - and in this chair.

KAISER: (to audience) So she was a pantheist. I made a mental note of it and said I'd give her case a try-for a hundred bucks a day, expenses, and a dinner date. She smiled and O.K.'d the deal. We rode down in the elevator together. Outside it was getting dark. Maybe God did exist and maybe He didn't, but somewhere in that city there were sure a lot of guys who were going to try and keep me from finding out. My first lead was Rabbi Itzhak Wiseman, a local cleric who owed me a favor for finding out who was rubbing pork on his hat. I knew something was wrong when I spoke to him because he was scared. Real scared.

WISEMAN: Of course there's a you-know-what, but I'm not even allowed to say His name or He'll strike me dead, which I could never understand why someone is so touchy about having his name said.

KAISER: You ever see Him?

WISEMAN: Me? Are you kidding? I'm lucky I get to see my grandchildren.

KAISER: Then how do you know He exists?

WISEMAN: How do I know? What kind of question is that? Could I get a suit like this for fourteen dollars if there was no one up there? Here, feel a gabardine-how can you doubt?

KAISER: You got nothing more to go on?

WISEMAN: Hey-what's the Old Testament? Chopped liver? How do you think Moses got the Israelites out of Egypt? With a smile and a tap dance? Believe me, you don't part the Red Sea with some gismo from Korvette's. It takes power.

KAISER: So He's tough, eh?

WISEMAN: Yes. Very tough. You'd think with all that success He'd be a lot sweeter.

KAISER: How come you know so much?

WISEMAN: Because we're the chosen people. He takes best care of us of all His children, which I'd also like to someday discuss with Him.

KAISER: What do you pay Him for being chosen?

WISEMAN: Don't ask.

KAISER: (to audience) So that's how it was. The Jews were into God for a lot. It was the old protection racket. Take care of them in return for a price. And from the way Rabbi Wiseman was talking, He soaked them plenty. I got into a cab and made it over to Danny's Billiards on Tenth Avenue. The manager was a slimy little guy I didn't like. Chicago Phil. Forger, bank robber, strong-arm man, and avowed atheist.

CHICAGO PHIL: The guy never existed, Kaiser. This is the straight dope. It's a big hype. There's no Mr. Big. It's a syndicate. Mostly Sicilian. It's international. But there is no actual head. Except maybe the Pope.

KAISER: I want to meet the Pope.

CHICAGO PHIL: (winking) It can be arranged..

KAISER: Does the name Claire Rosensweig mean anything to you?

CHICAGO PHIL: No.

KAISER: Heather Butkiss?

CHICAGO PHIL: Oh, wait a minute. Sure. She's that peroxide job with the bazooms from Radcliffe.

KAISER: Radcliffe? She told me Vassar.

CHICAGO PHIL: Well, she's lying. She's a teacher at Radcliffe. She was mixed up with a philosopher for a while.

KAISER: Pantheist?

CHICAGO PHIL: No. Empiricist, as I remember. Bad guy. Completely rejected Hegel or any dialectical methodology.

KAISER: One of those.

CHICAGO PHIL: Yeah. He used to be a drummer with a jazz trio. Then he got hooked on logical positivism. When that didn't work, he tried pragmatism. Last I heard he stole a lot of money to take a course in Schopenhauer at Columbia. The mob would like to find him-or get their hands on his textbooks so they can resell them.

KAISER: Thanks, Phil.

CHICAGO PHIL: Take it from me, Kaiser. There's no one out there. It's a void. I couldn't pass all those bad checks or screw society the way I do if for one second I was able to recognize any authentic sense of Being. The universe is strictly phenomenological. Nothing's eternal. It's all meaningless.

KAISER: (to audience) I had a beer at O'Rourke's and tried to add it all up, but it made no sense at all. Socrates was a suicide-or so they said. Christ was murdered. Nietzsche went nuts. If there was someone out there, He sure as hell didn't want anybody to know it. And why was Claire Rosensweig lying about Vassar? Could Descartes have been right? Was the universe dualistic? Or did Kant hit it on the head when he postulated the existence of God on moral grounds? Then the phone rang. The voice on the other end was Sergeant Reed of Homi-cide.

SERGEANT REED: You still looking for God?

KAISER: Yeah.

SERGEANT REED: An all-powerful Being? Great Oneness, Creator of the Universe? First Cause of All Things?

KAISER: That's right.

SERGEANT REED: Somebody with that description just showed up at the morgue. You better get down here right away.

KAISER: It was Him all right, and from the looks of Him it was a professional job.

SERGEANT REED: He was dead when they brought Him in.

KAISER: Where'd you find Him?

SERGEANT REED: A warehouse on Delancey Street.

KAISER: Any dues?

SERGEANT REED: It's the work of an existentialist. We're sure of that.

KAISER: How can you tell?

SERGEANT REED: Haphazard way how it was done. Doesn't seem to be any system followed. Impulse.

KAISER: A crime of passion?

SERGEANT REED: You got it. Which means you're a suspect, Kaiser.

KAISER: Why me?

SERGEANT REED: Everybody down at headquarters knows how you feel about Jaspers.

KAISER: That doesn't make me a killer.

SERGEANT REED: Not yet, but you're a suspect.

KAISER: (to audience) Outside on the street I sucked air into my lungs and tried to dear my head. I took a cab over to Newark and got out and walked a block to Giordino's Italian Restaurant. There, at a back table, was His Holiness. It was the Pope, all right. Sitting with two guys I had seen in half a dozen police line-ups. "Sit down," he said, looking up from his fettuccine. He held out a ring. I gave him my toothiest smile but didn't kiss it. It bothered him and I was glad. Point for me.

THE POPE: Would you like some fettuccine?

KAISER: No thanks, Holiness. But you go ahead.

THE POPE: Nothing? Not even a salad?

KAISER: I just ate.

THE POPE: Suit yourself, but they make a great Roquefort dressing here. Not like at the Vatican, where you can't get a decent meal.

KAISER: I'll come right to the point, Pontiff. I'm looking for God.

THE POPE: You came to the right person.

KAISER: Then He does exist? (to audience) They all found this very amusing and laughed. The hood next to me said, "Oh, that's funny. Bright boy wants to know if He exists." I shifted my chair to get comfortable and brought the leg down on his little toe. "Sorry." But he was steaming.

THE POPE: Sure He exists, Lupowitz, but I'm the only one that communicates with Him. He speaks only through me.

KAISER: Why you, pal?

THE POPE: Because I got the red suit.

KAISER: This get-up?

THE POPE: Don't knock it. Every morning I rise, put on this red suit, and suddenly I'm a big cheese. It's all in the suit. I mean, face it, if I went around in slacks and a sports jacket, I couldn't get arrested religion-wise.

KAISER: Then it's a hype. There's no God.

THE POPE: I don't know. But what's the difference? The money's good.

KAISER: You ever worry the laundry won't get your red suit back on time and you'll be like the rest of us?

THE POPE: I use the special one-day service. I figure it's worth the extra few cents to be safe.

KAISER: Name Claire Rosensweig mean anything to you?

THE POPE: Sure. She's in the science department at Bryn Mawr.

KAISER: Science, you say? Thanks.

THE POPE: For what?

KAISER: The answer, Pontiff. (to audience) I grabbed a cab and shot over the George Washington Bridge. On the way I stopped at my office and did some fast checking. Driving to Claire's apartment, I put the pieces together, and for the first time they fit. When I got there something seemed to be troubling her.

HEATHER/CLAIRE/ELLEN: God is dead. The police were here. They're looking for you. They think an existentialist did it.

KAISER: No, sugar. It was you.

HEATHER/CLAIRE/ELLEN: What? Don't make jokes, Kaiser.

KAISER: It was you that did it.

HEATHER/CLAIRE/ELLEN: What are you saying?

KAISER: You, baby. Not Heather Butkiss or Claire Rosensweig, but Dr. Ellen Shepherd.

HEATHER/CLAIRE/ELLEN: How did you know my name?

KAISER: Professor of physics at Bryn Mawr. The youngest one ever to head a department there. At the midwinter Hop you get stuck on a jazz musician who's heavily into philosophy. He's married, but that doesn't stop you. A couple of nights and it feels like love. But it doesn't work out because something comes between you. God. Y'see, sugar, he believed, or wanted to, but you, with your pretty little scientific mind, had to have absolute certainty.

HEATHER/CLAIRE/ELLEN: No, Kaiser, I swear.

KAISER: So you pretend to study philosophy because that gives you a chance to eliminate certain obstacles. You get rid of Socrates easy enough, but Descartes takes over, so you use Spinoza to get rid of Descartes, but when Kant doesn't come through you have to get rid of him too.

HEATHER/CLAIRE/ELLEN: You don't know what you're saying.

KAISER: You made mincemeat out of Leibniz, but that wasn't good enough for you because you knew if anybody believed Pascal you were dead, so he had to be gotten rid of too, but that's where you made your mistake because you trusted Martin Buber. Except, sugar, he was soft. He believed in God, so you had to get rid of God yourself.

HEATHER/CLAIRE/ELLEN: Kaiser, you're mad!

KAISER: No, baby. You posed as a pantheist and that gave you access to Him-if He existed, which he did. He went with you to Shelby's party and when Jason wasn't looking, you killed Him.

HEATHER/CLAIRE/ELLEN: Who the hell are Shelby and Jason?

KAISER: What's the difference? Life's absurd now anyway.

HEATHER/CLAIRE/ELLEN: Kaiser, you wouldn't turn me in?

KAISER: Oh yes, baby. When the Supreme Being gets knocked off, somebody's got to take the rap.

HEATHER/CLAIRE/ELLEN: Oh, Kaiser, we could go away together. Just the two of us. We could forget about philosophy. Settle down and maybe get into semantics.

KAISER: Sorry, sugar. It's no dice. (to audience) She was all tears now. A Venus whose right hand tousled my hair while her left hand had picked up a .45 and was holding it behind my back. I let go with a slug from my .38 before she could pull the trigger, and she dropped her gun and doubled over in disbelief.

HEATHER/CLAIRE/ELLEN: How could you, Kaiser?

KAISER: (to audience) She was fading fast, but I managed to get it in, in time. (to Ellen) The manifestation of the universe as a complex idea unto itself as opposed to being in or outside the true Being of itself is inherently a conceptual nothingness or Nothingness in relation to any abstract form of existing or to exist or having existed in perpetuity and not subject to laws of physicality or motion or ideas relating to non-matter or the lack of objective Being or subjective otherness. (to audience) It was a subtle concept but I think she understood before she died.
```

---

## IC-1027: Dinner Dilemma

- Title: Dinner Dilemma
- Author (byline): Mike Noland
- Work: Dinner Dilemma
- Publisher: Mushroom Cloud Press
- Publication date as stated: September 1, 2022
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: JIM, BUD
- Teaser before the introduction: No
- Spoken words (computed): 2020
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
JIM is sitting on the couch working on his laptop when BUD comes into the living room. BUD sits on a chair by the couch and just looks at JIM. JIM glances up and then right back down at his laptop. BUD continues to stare. Finally, JIM stops and looks up.

JIM: What?

BUD: Okay, let!s start.

JIM: (Looks at his watch.) Seriously, it!s only like ten till six.

BUD: I know, but I got stuff I gotta do.

JIM: Like what?

BUD: (Pauses) Stuff…

JIM: No you don!t. If you did I would know about it. You don!t have anything to do you!re just hungry.

BUD: Yeah I do and yes I am. If we don!t start figuring it out now, I won!t get to eat until Midnight.

JIM: Alright, but first you gotta tell what it is you have to do.

BUD: You!re not my mom. You don!t have to know everything I do.

JIM: Hahaha, believe me, your mom doesn!t know half the stuff you do.

BUD: Whatever, it!s not like I!m a hitman or something. I!m just living the dream, baby. But I gotta eat something and you take forever deciding.

JIM: Well...you still haven't told me what you are doing.

BUD: Oh my Gosh! Why do you always have to be in my business?

JIM: So I can laugh and make fun of you.

BUD: (Looks at JIM and finally decides to tell him.) Ok, ok. I!m going to play disc golf.

JIM: Whatever, liar. You have never played disc golf in your life. We have laughed at those dorks a million times. Those guys wear tiny ponytails, hiking shorts and smell like patchouli oil. They are still carrying around hacky sacks in case the 90!scome back. (changing his voice) "Dude, I haven!t seen you since that awesome Blues Traveler concert in Santa Fe. You still living in that VW bus?”

BUD: Haha, yeah that!s kind of spot on but this is different.

JIM: How can it be different?

BUD: Well, for one thing I!m not playing disc golf with a bunch of guys...there!s this girl.

JIM: (He just stares with mouth open then.) What??

BUD: (Sheepishly) Yeah.

JIM: Where did you meet her? At the Farmers Market selling homemade candles or all natural, organic goat!s milk soap?

BUD: You know that pizza I got last night?

JIM: Yeah, but you didn!t even leave to pick it up. You got it delivered.

BUD: Uh huh…

JIM: No..no...NO… You did not make a date with the girl who delivered your pizza?

BUD: I did.

JIM: So, what? You didn!t have enough money to tip her so you make a date? So this is like, a tip date?

BUD: A tip date is not a thing.

JIM: Well it is now. Let me see if I get this. A girl comes and brings you a pizza, which is actually kinda cool. But she brings you the pizza and instead of giving her a tip, you ask her out on a date?

BUD: No, I tipped her.

JIM: How much?

BUD: What?

JIM: How much did you tip her?

BUD: That doesn!t matter.

JIM: I think it does, how much?

BUD: Tipping is a personal thing. I!m not gonna tell you.

JIM: Well, the tip may be the reason she is going out with you. How much?

BUD: (Beat) $20

JIM: $20!!!!! Who are you, Bill Gates ? $20!!!

BUD: It!s not that much.

JIM: Not that much! Your whole outfit doesn!t cost $20. Of course she!s going out with you. She probably thinks you are one of those computer programmer guys who just sold his Start-up and is suddenly crazy rich. Why in the world did you tip her $20?

BUD: Well, she was really cute and when she told me how much it was, I was a little distracted and I gave her two twenty!s instead of two ten!s. But then I told her to keep the change and right after that I realized what I'd done and I was to scared to ask for the twenty back.

JIM: So instead of getting your change back you double downed and ask her out on a date?

BUD: Yep.

JIM: Does she know those are probably the last twenty!s you will have until the end of themonth?

BUD: That!s why we are playing disc golf, it!s free.

JIM: But not only have you never played disc golf, you don!t even have a disc.

BUD: Hibiscus does.

JIM: Hibiscus, what does that mean?

BUD: Hibiscus, that!s her name, Hibiscus.

JIM: The pizza girl!s name is Hibiscus? Haha, she must be cute. Was she driving a car that ran on vegetable oil? Hibiscus is a flower, right?

BUD: Either that or a type of dinner roll. Not sure

JIM: Now exactly how did you wind up going from tipping like a drunk trust fund baby to going on a disc golf date? Where did that come from?

BUD: She was wearing a t-shirt with a disc golf picture on it. I was looking for a way to chat her up and I said "Cool shirt.” And she was like, "I know, right?” and I was like "I love that.” And she was like, "We should play.” And I said "Uh, yeah we should.” Then she said, "Tomorrow?” And I was like, "For sure.” Then she gave me her number and we are going to play at 7 o!clock.

JIM: Quick question, how are you going to play? One, you don!t have a disc or even a Frisbee. Second, you don!t know how to even throw one if you did.

BUD: I got it all figured out. When I get there, I!m gonna look all through my car and act like I can!t find it. Then she will probably say, "Use one of mine.” I!ll say sure and when I throw the first one, I!m gonna act like hurt my arm or shoulder or something and then we can just walk and talk.

JIM: (Thinks for a second) That!s actually not bad. You!ve put some thought into this.

BUD: And my parents said those 3 years as a college sophomore was a waste. Guess I!m showing them now. What should I wear?

JIM: To play disc golf? The oldest t-shirt you have, those terrible rope sandals you!ve had since you played a Disciple in that dinner theater production of Jesus Christ Superstar and some ugly shorts. In other words, anything in your closet.

BUD: That!s funny. Now that you know what I!m doing can we please decide on what we are eating for dinner?

JIM: Pizza?

BUD: (Stares at him blankly) Wow, you had that ready to go didn!t.

JIM: Always be prepared besides I don!t have enough money for pizza AND a tip.

BUD: Very funny.

JIM: Wait a minute. Do you realize what you!ve done?

BUD: What?

JIM: When you screw up and this girl dumps you, like we both know you will.

BUD: Yeah…

JIM: You can never order pizza from that place again.

BUD: Oh no...I didn!t think about that. No, no, no...that!s my favorite pizza place. They even know that I like that crust almost slightly burned but not so much that you taste the burn, ya know?

JIM: Well, if you weren!t so distracted by Hydrangea…

BUD: Hibiscus.

JIM: You wouldn!t have created this problem. Cause you will either have to get her fired or find a new pizza place.

BUD: Are those my only options?

JIM: How good are you at disguises?

BUD: I did have a semester of Costume Makeup class and I played that Disciple.

JIM: Well, problem solved. You can go in order a pizza, a 2 liter bottle of Coke and 12 straws.

BUD: You could help me, you know, instead of enjoying my misery.

JIM: Are you kidding? This is better than the last 5 shows I!ve streamed.

BUD: I can!t lose my favorite pizza place.

JIM: Ok, gimme a second here. (Thinks) How about this, you can tell her that you don!t like mixing business with pleasure and that dating her would be a problem because you would feel bad having your girlfriend deliver your pizzas.

BUD: But I wouldn!t.

JIM: I know that and you know that but Honeysuckle doesn!t know that.

BUD: Hibiscus, but you know that!s one of my favorite things about having a girlfriend, they can bring me food.

JIM: Which is exactly why you don!t have a girlfriend now. You treat them all like they are your personal assistant or something. Only they work for free.

BUD: They aren!t working for free, they get me.

JIM: Yeah, that!s a real plus.

BUD: Instead of destroying my self-esteem, can we figure out how to save me from the loss of my favorite pizza place?

JIM: This is a radical idea but stay with me for a second. How about if you just be honest?

BUD: Hahaha, you got me on that one. That!s good.

JIM: (Not smiling) I!m not kidding.

BUD: What do ya mean? Tell her the truth? I can!t see you because if you get sick of me, I won!t be able to order pizzas anymore?

JIM: Yep.

BUD: This is the best you got? I need a new best friend. You really let me down with this one.

JIM: Or is it so crazy, it might work?

BUD: (Beat) Ya know… the more I think about it...it just might work. If she buys it, she will love my honesty. If she thinks I!m lying, she will hate my guts and she just won!t deliver my pizzas anymore. Someone else will have to do it.

JIM: But at least you can still get pizzas from there.

BUD: I think that!s it. I!ll be honest. That!s really good advice. Maybe you should start writing a relationship blog.

JIM: I do give good advice.

BUD: Good, now back to more pressing matters. What are we gonna eat?

JIM: Hmmm, let!s see… how about tacos?

BUD: From where?

JIM: I don!t know. Tacos are tacos?

BUD: But some places don!t have cheese dip and others do.

JIM: You should eat all that if you are about to go on your tip date?

BUD: That!s still not a thing but you may be right. How about a burger?

JIM: Nah, I!m not eating anything that has 4 legs.

BUD: What does that mean?

JIM: No pork or beef.

BUD: Since when?

JIM: Since I saw those pictures of people "cow cuddling.”

BUD: What!s cow cuddling?

JIM: It!s a thing that people do to de-stress. They sit down and a cow lays their head in the person!s lap and they cuddle. You know, like petting a dog. I saw pictures and the cow!s big brown eyes reminded me of my Pugsly and I could never eat my dog. He!s so sweet and innocent.

BUD: He!s not that sweet, he keeps peeing on our rug.

JIM: Only when it rains.

BUD: And he snores like a freight train.

JIM: Like that!s his fault. What do you want me to do?

BUD: Maybe close your door at night, so I don!t have to hear it.

JIM: It!s not that loud.

BUD: Are you kidding? First night I heard him, I thought you were choking on something.

JIM: Did you check on me?

BUD: Uh, no...what would I do? I!m not an EMT. And I!m sure not sticking my fingers down your throat to clear it.

JIM: Ok, on that we both agree. I don!t want your fingers anywhere near my mouth.

BUD: So it!s not a health thing or vegan thing, it!s a cute animal thing, right?

JIM: Pretty much.

BUD: So what about chickens? They have eyes.

JIM: Yeah, but they!re ugly.

BUD: Not as ugly as turkeys.

JIM: Which I can also still eat.

BUD: I hear that chickens are really sweet though and smart.

JIM: Don!t ruin this for me, it!s all I can do to give up pigs and cows. I gotta have some meat.

BUD: Fair enough, then what about some chicken tenders?

JIM: I could do that. Where do you want them from?

BUD: I don!t care, who delivers?

JIM: You think that!s such a good idea? You already have one date.

BUD: Fine, I!ll pick em up.

JIM: Cool.

BUD: Hey..

JIM: What?

BUD: You want dipping sauce?

JIM: Yeah

BUD: You want fries?

JIM: Yeah

BUD: You want a drink?

JIM: Yeah BUD Could I borrow some money?

JIM: No, but good try.

BUD: Worth a shot. (He exits)
```

---

## IC-1028: Everything Bagel

- Title: Everything Bagel
- Author (byline): Cam Eickmeyer
- Work: Everything Bagel
- Publisher: Mushroom Cloud Press
- Publication date as stated: August 1, 2023
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: CAST OF CHARACTERS, SCENE, TIME, AT RISE
- Teaser before the introduction: No
- Spoken words (computed): 1257
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
A 10-minute play

Written by

Cam Eickmeyer

CAST OF CHARACTERS:

Young Man: 20s, full of life and energy, ready to conquer the world

Old Man: 80s, tired and grumpy, perfectly happy to spend the day in the recliner watching old movies

Son: Late 50s, bogged down by obligations and not pleased to be stuck managing his aging father

*Note: All roles can be changed to any gender. Nothing in the story is male specific.

SCENE:

Small apartment

TIME:

Present day 2.

AT RISE:

Setting: Small apartment with minimal furniture. A recliner, small breakfast table with two chairs, and a wheelchair.

At Rise: YOUNG MAN fidgets and bounces impatiently. He's eager to start the day and something off stage is slowing him down.

(Something catches his attention off stage, he takes a few steps forward eagerly)

YOUNG MAN Are you awake?

OLD MAN
(Off stage)
Yes, are you happy? You couldn't
let me sleep a little more?

YOUNG MAN All you do is sleep. Sleep when you're dead.

(OLD MAN enters. He limps and shuffles, dragging a wheeled oxygen tank carefully across the room to his easy chair where he plops down.)

OLD MAN You promise to let me sleep when I'm dead?

YOUNG MAN To be determined.

OLD MAN You're on my last nerve, roomie, and it's not even breakfast.

YOUNG MAN Breakfast is a wonderful idea. Where should we go?

OLD MAN Go? I just sat down!

(Young Man bounces around with excitement. He shakes the chair playfully)

YOUNG MAN
Then stand back up. Get in the
wheelchair if you have to, let's go
out for breakfast.

3.

OLD MAN And where would we go? The odd couple's corner cafe?

YOUNG MAN What's the name of that bagel shop you used to love?

(They both tap their temples trying to jog their memories)

OLD MAN Something with a C

YOUNG MAN Colleen's? Cormica's? Cirrillo's?

OLD MAN Are you just saying random names to confuse me?

YOUNG MAN Capricorn, Candy corn, corn on the cob

OLD MAN You are a real pain sometimes.

YOUNG MAN Camille's Deli! That's it

OLD MAN Camille's, yeah, that was it

YOUNG MAN See? There's a method to my madness

OLD MAN Emphasis on the madness

YOUNG MAN Let's go to Camille's for everything bagels with coffee.

OLD MAN Camille's has to be five miles away, we can't walk there

YOUNG MAN So we take a bus

(Old Man chuckles at the youthful exuberance)

4.

OLD MAN
We just hop on a bus with my
wheelchair and oxygen tank and head
off to Camille's, that it?

YOUNG MAN
Why not? Picture the blanket of egg
and cheese on a slice of Taylor
Ham, all tucked perfectly into a
toasted bagel.

OLD MAN Got a cup of coffee in that fantasy?

YOUNG MAN Two creams, two sugars just the way you like it

OLD MAN Ha! That's the way you like it. I like it black.

YOUNG MAN Fine, black and strong. However you want, let's just go.

OLD MAN You're pretty serious about an everything bagel today

YOUNG MAN And the coffee. Can't forget the coffee

OLD MAN What has your pants on fire?

YOUNG MAN Adventure!

OLD MAN
Adventure? You don't think sitting
in a recliner watching old movies
counts?

YOUNG MAN
We have money, you are stronger
than you think. Let's just go. We
can go anywhere. Think big. Fly to
Los Angeles, go to Disneyland, fly
to New Orleans and party in the
French Quarter. Oh, I've got it!
(MORE)

5.

YOUNG MAN (CONT'D) We fly to Paris, eat baguettes under the Eiffel tower.

OLD MAN You and bread seem to have a thing today.

YOUNG MAN
The Grand Canyon! It's been at
least ten years since you've been
there, right? We'll take a mule
ride to the bottom.

OLD MAN
Did you find a bottle of liquor or
something? You think I can ride a
mule and sleep on the ground? Did
they install a fancy hotel in the
Grand Canyon or something?

YOUNG MAN Think bigger than this room.

OLD MAN You forget about my broken down body.

YOUNG MAN Pain is temporary, everything bagels are forever. You can sleep-

OLD MAN When I'm dead, yeah I remember.

YOUNG MAN
Let's go. If not Paris or the
Canyon, let's make it to Camille's.
Something beyond this room.

(Old Man pauses, he's on the verge of giving in when SON enters carrying a food tray. On the tray is a covered plate and two paper cups)

SON Hi Dad. How you feeling?

(Young Man doesn't like Son and crosses opposite stage in a huff)

OLD MAN I was talking about breakfast.

6.

SON Perfect timing then, eh? Looks good today I think.

(Son removes the lid on the plate and shows it to Old Man like it's fine dining. Young Man peers over skeptically)

YOUNG MAN Gross. Is that supposed to be a scrambled egg?

OLD MAN Got any bagels?

SON No, dad. Like I said last time, they don't have bagels here.

YOUNG MAN
Can you imagine how a bagel would
taste in this place? Lets get out
of here while we still can.
Everything bagel, Taylor ham-

OLD MAN Coffee

SON Coffee I can help you with after you take your pills.

(Young Man recoils in fear)

YOUNG MAN
Don't take them, please. I feel
fine for the first time in a while.
DON'T DO IT.

(Old Man stares at the cup of pills and hesitates)

OLD MAN So many pills.

SON
Look Dad, it's the same thing every
day. The nurse told me you are
fighting them about the meds so I
promised you'd take them today.

YOUNG MAN Please! You don't need those.

OLD MAN I hurt so bad sometimes.

7.

SON Yep, so take the meds. It'll help.

YOUNG MAN
You do that and you can kiss Paris
goodbye. Come on! Let's go, jump in
your wheelchair, I'll help.

OLD MAN How are you going to push the chair?

SON You want to go somewhere Dad? Then take the meds.

YOUNG MAN I'm begging you, please! I'm dying.

OLD MAN I know, I know.

(Old Man tips the contents of one cup into his mouth, then the water cup to swallow the pills)

SON That's it. Thanks. I'll be back with that coffee.

(Old Man looks over at Young Man who sulks with his back turned. Old Man raises his hand to his Son.)

OLD MAN Maybe I can have coffee on the patio today?

(Son lets out a heavy sigh, this request is apparently a large burden)

SON I'll see what I can do.

(Son exits. Young Man sits down at the table in despair)

OLD MAN I had to do it. Just a little relief for this pain.

YOUNG MAN I'm not in pain though.

OLD MAN
Maybe tomorrow we can go for
bagels.
(MORE)

8.

OLD MAN (CONT'D) Today we can sit in the sun a bit. That's pretty good still right?

(As the medicine begins to kick in, Old Man gains some mobility, but Young Man shrinks away)

YOUNG MAN You used to want adventure.

OLD MAN Adventure is in the eye of the beholder.

YOUNG MAN What does it matter anyway? Eat your eggs.

OLD MAN He said he would ask about the bagels.

YOUNG MAN Who said?

OLD MAN The guy, you know, the guy who comes-

YOUNG MAN What's his name?

OLD MAN Don't do that to me.

YOUNG MAN What's his name?

OLD MAN I said stop it-

YOUNG MAN
You don't know your own son's name.
You can't dream about Paris and the
Grand Canyon, but I still can. I'm
still in here. Don't let me die.

(The last burst of anger takes the rest of Young Man's energy. He starts to slump, to shut down, to fade away)

OLD MAN
I'm not letting you die. I just
need some rest. Then maybe we can
go get a bagel.

9.

YOUNG MAN We won't.

OLD MAN
Everything bagel and coffee, just
like you want. Just a little nap is
all, maybe some sun. I'll feel
better.

(Old Man falls asleep in his chair. Young Man rests his head in his hands. They're only asleep for a moment, then again it's hard to say how time passes in these sorts of places. Son enters without warning and pulls the wheelchair next to the recliner)

SON
Hey Dad? Dad? Wake up. I only have
about a half hour so if we're gonna
go for a walk we have to leave now.

(Old Man looks at Young Man, who is still motionless in the chair. Son helps Old Man into the wheelchair as they speak.)

OLD MAN I was going to have some coffee.

SON
Yeah dad, I know. Look, it's
raining so we'll just have to go
down to the dining hall instead OK?
Maybe look out the window at the
parking lot?

OLD MAN Everything bagel with egg and cheese and-

SON
You can't have Taylor Ham anymore
dad, bad for your cholesterol.
Every visit it's everything bagels
and coffee. Camille's closed twenty
years ago and that was in Jersey.
You're in Arizona now.

OLD MAN Colleen's? Cormica's? Cirrillo's?

SON
Camille, dad. Camille's Deli. Look
Dad, can we not argue today? Let's
get some coffee and watch the cars
OK? It's better than sitting in
this room right?

10.

(Old Man looks toward Young Man one last time. Young Man still isn't moving. If he's not already gone, he's very close to the end.)

OLD MAN Maybe bagels tomorrow?

SON Sure Dad, maybe bagels tomorrow.

(Son wheels Old Man off stage)

THE END
```

---

## IC-1029: How Tybalt Capulet (Almost) Saved Italy

- Title: How Tybalt Capulet (Almost) Saved Italy
- Author (byline): JD Holzmann
- Work: How Tybalt Capulet (Almost) Saved Italy
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: TYBALT, ROMEO, BENVOLIO, ROSALINE, CAPULET, MERCUTIO, JULIET, NURSE
- Teaser before the introduction: No
- Spoken words (computed): 1425
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
JD Holzmann

TYBALT: I am a tragic hero. Not just because I’m so tragically handsome. Ok, well that’s part of it. But, I’m so much more. I [dramatic pause] Am Tybalt Capulet, famed swordfighter, wealthy noble, slayer of Montagues. So, here is my tragic story of woe and triumph. You know the beginning. In fair Verona we lay our scene et cetera et cetera. My morning started when I woke up, obviously. I really hate Romeo Montague, I thought. To put in perspective, he’s basically the guy we all knew in high school with dyed black hair always in his eyes and black skinny jeans who wrote lyrics like “I am the foil to this bright delusion called day.” He was so dramatic. He called my sister a nun just because she didn’t like him.

ROMEO:
Oh, Benvolio!
Good friend, oh woe
Is me!
How can it be
That she does not love me?

BENVOLIO: Romeo. Relax.

ROMEO:
Look at the facts!
Explanations! There is only one!
My fair Rosaline is a nun!

TYBALT:
What kind of conclusion is that? You’re not the best looking man in Verona, Montague.
[Hair flip]
I mean.

So, everything really started that fateful afternoon. Rosaline was preparing for the party that night. She had also denied Romeo Montague. I’m so proud of her.

ROSALINE: Tybalt, does this necklace go with this dress?

TYBALT: No. It looks cheap. Like something a Montague would wear.

ROSALINE: You have a point. Speaking of the Montagues, that Romeo has found favour in me.

TYBALT: [in disgusted shock] Romeo Montague?

ROSALINE: The only Romeo we know.

TYBALT: That detestable man! Say it’s not so! Say you aren’t loved by that Romeo!

ROSALINE: [done.] He’s rhyming again.

TYBALT: Can I stand his unforgivable sin?

ROSALINE: Your perspective’s a bit...askew

TYBALT: You got that from your precious Montague!

ROSALINE: Tybalt.

TYBALT:
Perfection.
[beat]
As I was saying, that necklace looks cheap. Like the Montagues. New money, no doubt. Those Montagues know
nothing of tradition!

ROSALINE: Their money’s as old as ours.

TYBALT: Those Montagues told you that! It’s a plan! It’s a conspiracy! They’re clever, those Montagues. Not smart, but clever. Those-

ROSALINE: Say ‘Montagues’ one more time and I’ll hurt you.

TYBALT:
Say no more, sister Rosaline, for I
Leave until the festivities of night.
I bid you farewell, leave with a couplet,
Until tonight with cousin Juliet.

Thus, I went out to prove that precious Romeo wasn’t the only man in Verona who could rhyme.

He thinks he has such a talent for it But he doesn’t know, doesn’t know a bit Of what Tybalt Capulet can do now!

So, I went out into town. And who did I see? None other than that villain Romeo. He was being as Montague-esque as usual. Meaning sad. As the Montagues are sad excuses for human beings. Honestly, the world would be so much better off without them. Wait! That can be arranged.

Uncle, I want to stab him.

CAPULET: Tybalt no.

TYBALT: But-

CAPULET: Tybalt no.

TYBALT: So I just confronted Benvolio.

Ay Benvolio!

BENVOLIO: What?

TYBALT: It appears I’ve broken a mirror recently.

BENVOLIO: With a face like yours, I’m not surprised.

TYBALT: You’re one to know about that, aren't you? But the curse of thirteen misfortunate years arrived when you did.

As you can see, I’m what the kids call savage.

As I was saying, Montague, look upon thy death.

BENVOLIO: CAn’t a guy get some peace-

TYBALT: What, drawn and talk of peace! I hate the word as I hate hell, all Montagues, and thee.

BENVOLIO: What?

TYBALT: Have at thee, coward!

And thus we, and much of our families, fought. I valiantly led the fray, leading to yet another Capulet victory. I know, I know. I’m such a hero. But just sitting there was perfect Romeo.

ROMEO:
Woe!
Woe is me!
Woe is that she,
That she, the bright morning star
Doesn’t care for who I are!

BENVOLIO: Am.

ROMEO:
That perfect lamb!
The nun!
Love, her heart has none.
Oh, my life is done!

BENVOLIO: Chill. Please. You’re killing me.

ROMEO: Love is killing me!

BENVOLIO: [sigh]

Ok that servant said there was gonna be a party right? We should go.

ROMEO: I cannot, dear Benvolio!

BENVOLIO: There will be girls.

ROMEO: I’m game.

TYBALT: Thus, Romeo and his company showed up to the party my uncle was throwing for Juliet. And trust me, his company isn’t exactly likeable. The worst is that scum Mercutio. He loves nothing more than what he calls comedy. He’s a child, I’m telling you. I could be holding a sword to his throat and he’d say,

MERCUTIO: Alright mate. I get the point but you can cut it out now. Eh? Eh?

TYBALT: He’s the disgrace of Italy.

But, I was casually enjoying the party. Dancing, talking, the like, and then I hear it. That Montague Romeo was there. Talking about my cousin Juliet. Can I just take a moment to bring up how disturbing this is? So, I decided to take the necessary measures.

Uncle, Romeo Montague’s here.

CAPULET: That’s great, Tybalt.

TYBALT: He’s killing my vibe and I won’t endure him!

CAPULET: Tybalt, chill.

TYBALT: Imma stab him.

CAPULET: Tybalt no.

TYBALT: Tybalt yes.

CAPULET: Tybalt this is literally your 14 year old cousin’s birthday party.

TYBALT: I mean. It’s not like it’s a sin to kill him, Uncle.

CAPULET: Maybe tomorrow.

TYBALT: But-

CAPULET: Don’t stab him.

TYBALT: Old man ruins all the fun. So, I had to tolerate Romeo’s detestable presence all night. And shockingly, he didn’t ruin anything. Until the very end, when I heard that he had deceived Juliet into loving him. How someone could do that, I’ll never know. I knew he’d be the death of her and me both. I swore to end him or die trying. Thus, I spent my time plotting.

Rosaline, I’m plotting!

ROSALINE: That’s great.

TYBALT: Juliet, I’m plotting to kill your boyfriend.

JULIET: Oh, but my dear cousin Tybalt, why? My love does not deserve to die.

TYBALT: Dear Juliet, you ask me why?

JULIET: Ay.

TYBALT: For he has shamed Our family name!

JULIET: He brings no shame!

TYBALT:
They’re all the same!
Those Montagues
You have no clue
He’s using you!

JULIET: You lie!

TYBALT: You deny!

Nurse, keep her here. I’m going back to plotting.

NURSE: That’s great. Actually, that reminds me of the time when you-

TYBALT: Don’t finish that statement.

I spent the rest of the day plotting more. Then, it hit me. Well, Rosaline more or less threw it at me.

ROSALINE: Hey, idiot. You left your hat in the living room again.

TYBALT: That hat! That hat that-

ROSALINE: Stop rhyming.

TYBALT:
Fine. This hat. This hat that I was going to wear to Juliet and Paris’ wedding. The same hat I wore during [slowing
down] that I wore during the party. When I saw Romeo.
That’s it!

ROSALINE: Here we go.

TYBALT: I’ll kill him after Juliet and Paris’ wedding! [louder]

You hear that, Verona? Tybalt Capulet shall slay Romeo and save all Italy!

I went out the next morning to tell everyone the good news. Then I saw Benvolio and Mercutio. The villains were talking about me and that repulsive Montague. I was so enraged, I decided not to wait until after the wedding. I’d act as soon as I saw him. I decided to interrupt them in order to ask for Romeo.

Good day, gentlemen. A word with one of you, if you please.

MERCUTIO: Just one singular word?

TYBALT: More like a question. Where might one be able to obtain information as to where your leader Romeo currently takes up space?

BENVOLIO: What?

TYBALT: I’ll put it in terms even a Montague would understand: Where Romeo?

MERCUTIO: No idea. But you like fighting people, right?

TYBALT: I suppose.

MERCUTIO: Fight me.

TYBALT: What?

MERCUTIO: Fight. Me.

TYBALT: No.

MERCUTIO: Why won’t you fight me?

ROMEO: Mercutio, who are you trying to fight now?

MERCUTIO: The crazy cat lady.

ROMEO: Tybalt?

MERCUTIO: Yeah.

TYBALT: Excuse.

MERCUTIO: Ignore the cat lady Bromeo.

ROMEO: If you insist, MercutiBro.

TYBALT: What am I witnessing?

MERCUTIO: Shut him up, BenvoliBro.

TYBALT: Put me out of my misery.

MERCUTIO: Gladly.

TYBALT: So we fought. I, of course, won. Poor fool didn’t stand a chance. I fled the scene to spread the word. I was proud. The fool needed to die. His puns were killing the crowd. And then I returned.

ROMEO: Not cool bro.

TYBALT: You dating my cousin isn’t cool ‘bro’.

ROMEO: Excuse you, I married her.

TYBALT: When?

ROMEO: Bout an hour ago.

BENVOLIO: Really? And I wasn’t best man?

ROMEO: Sorry, man. We wanted it to be really lowkey.

BENVOLIO: Nah I get it.

TYBALT: Are we gonna fight or nah? I just kinda killed your friend so.

ROMEO: Oh right.

TYBALT:
And that, dear audience, is where this hero turns tragic. I fought flawlessly, as usual. But Romeo was better than I
took him for. After a long struggle, I did fall. Dying to defend my cause.
My blood stained the streets, never to forget
The tragedy of Tybalt Capulet.
```

---

## IC-1030: Imaginary Friend

- Title: Imaginary Friend
- Author (byline): Marisa Grady
- Work: Imaginary Friend
- Publisher: Mushroom Cloud Press
- Publication date as stated: September 1, 2021
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1974
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
(Jimmy starts off the scene by looking frantically around his room for an object – it’s not clear what he’s looking for but he finds some fairly unpleasant things while he’s looking – Henry, Jimmy’s imaginary friend, sneaks up behind him, scaring Jimmy half to death)

Henry: Looking for this? Jimmy: Why do you have my cell phone? Henry: I was playing Candy Smash. I have to entertain myself somehow while you’re gone and your mom turns off the wifi during the day. Jimmy: I need that phone! How am I supposed to be able to send messages to cute girls during the day if you have my phone? Henry: Psssh, you don’t talk to cute girls. You call that Emma girl cute? I have news for you, buddy, she is not cute. Jimmy: She’s cute. Look, I don’t need my imaginary friend giving me advice on the cuteness of the girls I talk to. Henry: Then what do you need an imaginary friend for? Jimmy: We are not having this conversation again. I need you to be here. End of story. Henry: Why not? Why can’t we have this conversation? Jimmy, Jim, can I call you Jim? Of course I can call you Jim, I can call you whatever I want to, I’m imaginary. You need to move on with your life! You’re….you’re….how old are you now? Jimmy: I don’t see why that matters. Henry: But it does matter! It does! You have to be at least…..21? Jimmy: 21?! I can’t even drive and I’m still in high school, but you think I’m old enough to buy beer. Henry: How am I supposed to know these things?! You shave. You like girls. I don’t know when these things are supposed to happen. I’m an imaginary friend. Usually we deal with lost teeth and monsters. Not cute girls and learning to drive. You do remember that I can’t go anywhere until you let me go, right? Jimmy: I remember.

Henry: Ok….so….I have an idea. How about we practice? You know, like we did when you had
to tell your mom that you broke her tablet.
Jimmy: Ok….wait….I broke mom’s tablet….That was you, remember? I had to take the fall for
you that time. You were the one who dropped it into the aquarium because the fish looked bored.
Henry: They really should put a warning label on those things.
Jimmy: I’m not going to practice. No sir, you are not going anywhere. Who else am I supposed
to play video games with? I’m an only child, in case you forgot.
Henry: Here we go again! I’m an only child, feel sorry for me. Poor, poor little Jimmy, here is
the world’s tiniest saxophone, playing a sad, sad song for you.
Jimmy: Isn’t it supposed to be a violin?
Henry: Imaginary friends have saxophones, not violins. Do you hear it? It sounds like Kenny G.
(hums soothing saxophone music) Are you ready to practice letting me go now?
Jimmy: No.
Henry: How about now?
Jimmy: No.
Henry: How about now? Now? How about now?
Jimmy: Stop!
Henry: Can’t help myself. I’m supposed to be having conversations about kid things, not
convincing an oversized manchild that he should be letting his imaginary friend go. I don’t think
you realize the seriousness of this situation that we find ourselves in.
Jimmy: What do you mean?
Henry: Well, for starters, you’re not seven anymore.
Jimmy: I had noticed.
Henry: Yes, and most um, how do I say this politely? Oh I don’t care. Most normal children give
up their imaginary friends when they’re….at most…seven.
Jimmy: So I’m a late bloomer. My mom always says that I shouldn’t be in any rush to grow up
because growing up is a terrible thing that should be avoided at all costs.
Henry: So that’s what this is about.

Jimmy: Well, what would you do in my situation? I don’t want to pay bills, taxes, get married.
Commitment sounds awful and scary and I don’t want to do it. My friend’s brother lives in their
basement and he’s almost 40 and he seems really happy.
Henry: Happy or delusional?
Jimmy: Is there a difference?
Henry: C’mere, let me take a look at you.
Jimmy: Why?
Henry: Humor me. We’ve been friends for most of your life. You kinda owe me.
Jimmy: Fine.
Henry: Stand here. Recite your alphabet backwards.
Jimmy: What? Why?
Henry: Nevermind there are other ways I can tell.
Jimmy: Tell what. Why are you looking at me like that?
Henry: Yessir, I think I can officially diagnose you.
Jimmy: Diagnose me? How are you in any way qualified to diagnose me, Henry?
Henry: Excuse me? That’s doctor Henry, I didn’t go to imaginary medical school to be called
just “Henry.”
Jimmy: Ok, doctor Henry. What is your prognosis? Am I going to die?
Henry: Do you want the good news or the bad news?
Jimmy: Let’s start with the good news. You know I don’t like bad news. Bad news means mom
is making “creative” tacos again.
(They both shudder at the thought of mom’s tacos)
Henry: The good news is that you are old enough that you don’t need me anymore.
Jimmy: How is that good news?
Henry: I didn’t say it was good news for you, silly. Now the bad news is that you won’t let me
go because you are suffering from Peter Pan syndrome.
Jimmy: You made that up. You have to have made that up.

Henry: No, it’s an official imaginary diagnosis. Basically it means that, like Peter Pan, you refuse to grow up. How this affects me is that I am an imaginary friend who is stuck with a person who is no longer a child but still wants to be one. This is a problem because I have absolutely zero experience with the trials and suffering of teenagers. You are a teenager right? Jimmy: Yes, at least we can agree on that. But I don’t have this….whatever it is…syndrome. I just don’t see the need to let go of my childhood. Henry: But….I have a cure for you. Jimmy: You have a cure for something that I don’t actually have. Henry: Yes. No…you do have it, even if you won’t admit it. You know there are support groups for people like you? Jimmy: Really? Support groups for people with obnoxious imaginary friends. Henry: No, silly, support groups for people who refuse to grow up. It’s called Twitter. Jimmy: I should never have let you get online. Henry: Hey, what else am I supposed to do while you go live your glamorous high school life? Jimmy: Glamorous? Ha…no…you have no idea. Henry: Come here, gather around the therapy couch. Jimmy: You want to give me counseling now? Henry: (with a pad of imaginary paper) Now, tell me, how long are you planning to be single and childlike? Jimmy: I don’t see where you’re going with this. I can have an imaginary friend and date girls and be popular in school. Henry: Oh, right, let’s see how well that goes. Let me describe to you how this one plays out. Oh, hi, cute girl #437, I want to take you home to meet my imaginary friend. What’s that? Oh no, I’m not crazy. I just want to remain a tiny infant forever. Jimmy: You’re hilarious. Get comfortable, you’re not going anywhere. Henry: Maybe I’m not. But I do know I can help you want to be an adult someday. Jimmy: I don’t think you can, but I suppose I can’t stop you from trying. Henry: Nope, you can’t. So prepare yourself for “intensive training in adulting”!! Here is your first scenario. It’s dinner time….what do you do?

Jimmy: Wait until Mom calls me to the table and then I eat whatever she made.
Henry: Wrong! What do you want to eat? You want these Oreos?
Jimmy: Yes, but they’ll spoil my dinner.
Henry: You’re an adult. You can eat the Oreos. You can eat a whole package of Oreos. Oreos
can BE dinner.
Jimmy: Really?! They can??
Henry: Yes. And this is only one of the perks of being an adult.
Jimmy: There’s more??
Henry: Yes. So much more.
Jimmy: Like what?
Henry: What time do you have to be home at night?
Jimmy: 11:30 or mom turns the hose on me when I get home and I’m grounded for a week.
Henry: When you’re an adult there is no curfew.
Jimmy: No curfew?
Henry: No curfew.
Jimmy: That. Is. Amazing!
Henry: I know, right??
Jimmy: Being an adult is starting to not sound so bad.
Henry: I haven’t even told you the best part yet.
Jimmy: There’s something better than Oreos for dinner and no curfew??
Henry: Yes.
Jimmy: What could possibly be better than cookies for dinner and staying out as late as I want
to?
Henry: Picture this: No rules. You make the rules.
Jimmy: I make the rules.
Henry: All of them.

Jimmy: Whoa…..so I get to decide what I want to do and when I want to do it. Henry: Yes. Jimmy: Wait…this all sounds too good to be true. What’s the catch? Henry: What’s the what? Jimmy: The catch, there’s always a catch with something good like this. Henry: Sure there’s other things, things you might be afraid of, but the Oreos….think of all the wonderfully bad dinner decisions there are to be made. And money, you make money, lots and lots of money that you can spend on wifi and Netflix. Jimmy: Money? Doesn’t that mean I have to have a job? Henry: Hush, don’t worry about such trivial things as a job. Just focus on the money. Jimmy: Money. Henry: And cookies as far as the eye can see. Are you with me?? Jimmy: But being an adult means that I have to let you go right? Why can’t I have all of those things and have you too? Henry: You don’t need me anymore. Trust me, there’s nothing more embarrassing than being an adult and having an imaginary friend. I’m a third wheel on dates. It’ll look like you’re talking to yourself. I’m a terrible college roommate. I’ve never been a college roommate, but I know I’d be the worst. Jimmy: I suppose you’re right. Henry: It won’t be so bad, pal. Maybe when I’m gone you’ll spend more time talking to real people. Jimmy: You are real people to me. Henry: That’s touching, it really is…but don’t you think there’s a child out there that needs me just a little more than you do? Jimmy: But I’ll miss you. Who will laugh at my jokes? Who will tell me it’s all going to be ok when I’m scared? Henry: You’re a big boy now. You can deal. And I’ll leave the monster spray for you. Jimmy: Promise?

Henry: Promise.
Jimmy: All right, I can do this. I can adult.
Henry: That’s the spirit. I’ll just grab my things. (He grabs nothing). Ok, see you around.
Jimmy: That’s it. That’s goodbye?
Henry: Yeah, see ya.
Jimmy: Won’t I ever be able to see you again?
Henry: Sure, sure you will. Just like when Patches went to that farm in country.
Jimmy: Uh, Henry, Patches died. We buried him in the backyard. I just told you that Patches
went to a farm to make you feel better.
Henry: You did that. For me? Thanks, pal. See, you’re one step closer to being an adult already.
Jimmy: Thanks. See ya.
Henry: Bye.

(Henry leaves and Jimmy sits for a few minutes, trying to sike himself up to be an adult)
Jimmy: Wait, Henry, I’ve changed my mind. Henry?? Henry.
Henry: Sorry, no takesie backsies.
Jimmy: Fine. I’ll be ok. Just go.
Henry: If I were to stay….
Jimmy: Yes….
Henry: Promise me you won’t bury me in the backyard.
Jimmy: Ok, I promise.
Henry: I can’t leave you when you have that sad look on your face. Maybe I’ll stick around for a
while, just, you know….until you get used to the whole adult thing.
Jimmy: That sounds good. Let’s go find some Oreos. We can pretend to be adults and have them
for dinner.
Henry: Sounds like a plan.
```

---

## IC-1031: The Ad Lib

- Title: The Ad Lib
- Author (byline): Kevin Burgun
- Work: The Ad Lib
- Publisher: Mushroom Cloud Press
- Publication date as stated: September 1, 2022
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ALEX, JORDAN, COACH 1, COACH 2
- Teaser before the introduction: No
- Spoken words (computed): 1873
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
(Author’s Note: This was written with the express goal in mind to make everyone viewing this for
the first time have no idea what is really going on. The more the performers can aid this
dissonance, the better. What is real? What is scripted? Spoiler alert: It is ALL scripted. The
guiding principle of this piece is: What is reality?)
CHARACTERS (with suggested doubling breakdown)
Alex - Performer 1
Jordan - Performer 2
Coach 1 - Performer 1
Coach 2 - Performer 2
** NOTE: Coach 1 and 2 are the same coach, just each does their own impression

(Until the “BREAK” - which is noted - the start of the DUO should be performed in a manner that would make the viewer think it’s not as well rehearsed as it could have been. This will make the break seem more realistic. The point is to constantly trick the audience into confusion. The guiding principle of this piece is: What is reality?)

ALEX: Hello! And welcome to our performance of ALL of Christopher Marlowe’s plays in under 10 minutes!

JORDAN: It’s like the more popular compilations of Shakespeare’s plays, but with a less well known playwright.

ALEX: So, if you don’t know who Christopher Marlowe is - no worries!

JORDAN: Neither do we!

ALEX: (BREAK. This now needs to seem like a genuine argument and not the script. The goal is to make people uncomfortable.) Jordan, c’mon. How many times can you screw up the line?

JORDAN: What the what? We’re performing, Alex.

ALEX: It’s “Neither DID we” DID. DID. Not do. I swear to all that is holy, we have gone over this a hundred times. DID!

JORDAN: Who cares? What’s the big deal? No one noticed. No one cares.

ALEX: It IS a big deal. “Do” means we currently don’t know who Christopher Marlowe is, “DID” the CORRECT term, means that in the past we didn’t know who he was but now we do, and are ready to teach THEM (points to audience).

JORDAN: This is why I didn’t want to be paired with you.

ALEX: Oh, because I begged Coach to be paired with you? Right.

COACH 1: Now Alex, I know that Jordan is a terrible performer, but I need someone to step up, and you are clearly the most talented, the best really, performer on the team. Jordan won’t be able to pull you down. Or dim your shine.

JORDAN: You are making everyone uncomfortable.

ALEX: (To an audience member) Are you uncomfortable? (To Jordan) No, I think they ALL understand my frustration.

JORDAN: They are smiling at you because everyone now knows who is getting the “6”. It’s us Alex. US. Because you have to nitpick every little thing.

ALEX: Not a little thing.

JORDAN: Let’s ask the judge. Did you even notice the tense I used?

ALEX: Don’t answer that! Jordan, you can’t address the judge in round, you are going to get us disqualified.

JORDAN: Who cares?! It’s not like we can start over, right?

(So, a judge might respond, or might not. This next bit should still work.)

ALEX: I’m sorry, you don’t need to respond, this is actually the DUO.

JORDAN: We are currently doing the script.

ALEX: It seems like we aren’t right now, because we are explaining we are doing the script.

JORDAN: But trust us, literally what I am saying right now is scripted.

ALEX: Like, I get that it seems as if we stopped doing the script to explain it to you, hence this isn’t scripted, but it is scripted. Every word.

JORDAN: I think this is level 3 right now, sort of like Inception. But I’ve never seen it. It’s just sort of part of the cultural knowledge now.

ALEX: You are too much, just stick to the script. It’s not hard.

JORDAN: I am literally doing the script word for word. You know this.

ALEX: So am I, Jordan, so am I.

JORDAN: So, why are you angry?

ALEX: It’s okay, we don’t really hate each other.

JORDAN: I mean, you smack your lips when you eat. You constantly show up late to rehearsal, and then leave early to “pick up your little brother”.

ALEX: I have a little brother.

JORDAN: Sure.

ALEX: Hold on, time out. Do you really hate me?

JORDAN: You are not my favorite person, no.

ALEX: Why did you agree to be my partner then?

JORDAN: Like I had a choice.

COACH 2: Now Jordan, you and Alex will be the perfect pair, you complement each other’s strengths and weaknesses.

ALEX: Was that supposed to be Coach? I did it better.

COACH 2: Alex is pretty stuck up, between you and me. You will be a good influence. Since you are such a hard worker.

ALEX: I hate that I am standing up here with you.

JORDAN: This is literally page 3 only. (Deep breath). Okay. Let’s see if we can save this thing. A shred of dignity. Can we try that?

ALEX: Yeah, fine.

JORDAN: Let’s just do our introduction. Get back on track. Maybe we can nab the 5.

ALEX: (Pause, looking around the room.) Yeah, I think we can beat that team, even with this start. I am SO sorry, to have said that, I don’t think that at all, it’s just the script, I’m doing the script, I swear.

JORDAN: We really like your DUO.

ALEX: Did you cut out the insult so I look like the jerk?

JORDAN: What?

ALEX: The script had us both insulting a random DUO.

JORDAN: I must have had a different cutting than you did.

ALEX: I truly hate you now.

JORDAN: Introduction time?

ALEX: Fine. INSERT INTRODUCTION

JORDAN: Ok, we are just going to start from the beginning, and we are just going to hope that the rest of this is so good, the judge will forget about how you (ALEX glares) we messed up earlier.

ALEX: That combined with that team totally messing up. I am so sorry, this is literally the script, I don’t want to say this, you look like wonderful people, seriously find me in the cafeteria after this, I will show the script. (To JORDAN) But they’ll probably mess up.

JORDAN: That’s so mean.

ALEX: I know it’s mean, Jordan. But it’s in the script. Let’s just get started. Ok?

JORDAN: Ok. You know what Coach always says:

COACH 2: Failures don’t define you, you define you by how you get up again and move forward towards triumph.

ALEX: That’s a terrible coach impression.

COACH 1: Failures don’t define you, you define you by how you get up again and move forward towards triumph.

JORDAN: We are running out of time, I want to get through as much Marlowe as possible.

ALEX: Hello! And welcome to our performance of ALL of Christopher Marlowe’s plays in under 10 minutes!

JORDAN: It’s like the more popular compilations of Shakespeare’s plays, but with a less well known playwright.

ALEX: So, if you don’t know who Christopher Marlowe is - no worries!

JORDAN: Neither do we!

ALEX: Are you serious right now? Did you do that on purpose?

JORDAN: Do what?

ALEX: You said “do” instead of “did”.

JORDAN: I am doing what the script says, Alex.

ALEX: You aren’t though. I know what the script says, Jordan.

JORDAN: But I am doing the script exactly. As you are. You were supposed to say that.

ALEX: Who believes anything anymore?

JORDAN: The judge will trust me, right judge?

ALEX: Jordan, no one has the script. Look at your hands. Is there a script there? This is a memorized duo. No script.

JORDAN: I thought the judges had a copy of the script?

ALEX: At NATIONALS they do Jordan. Look around. Do you think we are at Nationals?

JORDAN: Well..

ALEX: Based on our performance so far, do you think we made it to Nationals?

JORDAN: I worked hard though.

ALEX: You did?

JORDAN: You don’t take it very seriously, to be honest.

ALEX: How am I not taking it seriously? I’m the one making sure you say the right word!

JORDAN: (To audience) I’m saying it correctly. Just trust me. I practice in front of the mirror like twice a week.

ALEX: All we have done is lie to them this entire time.

JORDAN: The script is full of lies, true. But, the script itself is real.

ALEX: So, we are telling the truth about the lies?

JORDAN: Exactly. They (references audience) get it.

ALEX: You know what? This is like that time in third grade when the teacher gave us that test that said read all the directions thoroughly before starting the test and then the last question was “don’t do the test”.

JORDAN: I aced that.

ALEX: It was supposed to teach us the nuances of language, but all it taught us was not to trust the teacher who was trying to trick us.

JORDAN: I learned about nuance.

ALEX: You think “did” and “do” connote the same thing!

JORDAN: No one cares.

ALEX: I care!

JORDAN: Wait.

ALEX: What?

JORDAN: Is this the multiverse?

ALEX: How is this the multiverse? There is one of you and one of me.

JORDAN: So this is more of a simulation, where you and I are not saying what we want to say, but what the script says we are supposed to say?

ALEX: So, we have no free will? It’s just an illusion.

JORDAN: Let’s try. Say any word that comes to mind.

ALEX: Sparrow.

JORDAN: No, that was what the script told you to say.

ALEX: But they didn’t know that.

JORDAN: But we did. Say something crazy.

ALEX: I like how orange markers taste.

JORDAN: Drat. Dangit. Smelly. Shut the door. Refrigerator. Fork. Smurf.

ALEX: What are you doing?

JORDAN: Trying to curse. But I can just say the script.

ALEX: Wait, are you saying we aren’t choosing to the do the script now? That the script controls us?

JORDAN: I think so.

ALEX: This is scary. Truce?

JORDAN: Truce!

ALEX: How do we get out of this?

JORDAN: What if we have to do something else we don’t want to do?

ALEX: Like be mean to them? (Gestures towards DUO team)

JORDAN: What if it’s worse?!

ALEX: Let’s just stop and take a breath and go get lunch. Maybe we just need food.

JORDAN: Good idea. What’s for lunch?

ALEX: I assume pizza.

JORDAN: It’s not always pizza.

ALEX: It’s almost always pizza.

JORDAN: I went to a tournament once where they had a taco bar.

ALEX: Oh wow. How was that?

JORDAN: It was fine.

ALEX: Oh. Was that a real memory of yours, or was it just from the script?

JORDAN: I honestly don’t know any longer. I feel like it happened to me, but it was also in the script. But then again, I am also an actor playing a character written by someone else.

ALEX: So, we pretty much have three levels going on at all times.

JORDAN: It was someone’s memory.

ALEX: Or made up.

JORDAN: Wow, the writer really hit a wall here, huh?

ALEX: I think this is right before lunch for him, too.

JORDAN: Do you think he eats pizza to stay in the moment?

ALEX: I think this is getting way too meta for me.

JORDAN: Let’s just Ad Lib the rest of this. Remember in the script at that one point it just says “Ad Lib”?

ALEX: So, we just Ad Lib the remaining time?

JORDAN: Sure, is there a rule how long an Ad Lib could be?

ALEX: Great question.

JORDAN: What if there as a published script that just said “Ad Lib”?

ALEX: Jordan.

JORDAN: Alex.

ALEX: THIS script is CALLED Ad Lib.

JORDAN: Damn. Wait. I cursed. Are we ad libbing now?

ALEX: Damn. I cursed, too! We must be ad libbing! (To DUO team) Genuinely I am sorry. I will buy you a bag of chips or something.

JORDAN: Wait. is your character who only exists in this room offering to buy chips, or are you the actor offering to buy chips?

ALEX: I don’t know.

JORDAN: I think we aren’t totally ad libbing here then.

ALEX: I am. I think.

JORDAN: Part of the reason we don’t know is they don’t have a script, so they don’t know either. This could be the script.

ALEX: Or it could be us just doing like duo impromptu hoping to get out of this situation and avoiding further embarrassment.

JORDAN: Good point.

ALEX: But we aren’t. Judge, we get it, you have to go to tab, because you don’t know what to believe.

JORDAN: You can believe us. Look at this face (references self). Not that one (references Alex). This one (references self).

ALEX: (At same time as Jordan.) Aaaaand scene.

JORDAN: (At same time as Alex). Aaaaaand scene.

ALEX: That was pretty good, huh?

JORDAN: So, the playwright, brilliant, brilliant man, basically read all of Christopher Marlowe’s plays, distilled them into their essences, and wrote this as a modern adaptation of all of his plays.

ALEX: If you are a Christopher Marlowe scholar….

JORDAN: Said no one ever….

ALEX: Then you probably recognized the literal hundreds of clever references.

JORDAN: If you are not a Christopher Marlowe scholar…

ALEX: Said everyone….

JORDAN: Then you were probably just super confused.

ALEX: And in your case (references DUO), sorta mad. And upset.

JORDAN: Or even this explanation is all a big lie.

ALEX: What’s the reality?

JORDAN: You choose.

ALEX: Or just do what the script says. END
```

---

## IC-1032: The Leak

- Title: The Leak
- Author (byline): Gavin Barker
- Work: The Leak
- Publisher: Mushroom Cloud Press
- Publication date as stated: September 1, 2022
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: BERT SUMMERS, HANK MORRIS, BERT, HANK
- Teaser before the introduction: No
- Spoken words (computed): 1274
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
Characters:

BERT SUMMERS: A very excited middle aged man who took his friend Hank fishing in a canoe he just bought from a yard sale.

HANK MORRIS: A middle aged man who was dragged on a fishing trip by his annoying
friend.
Setting:
2021 in the Middle of the Great Bottleman Lake in Canntown, USA.

(The play opens on two men sitting on either end of a canoe holding fishing poles. The first man, BERT, should look very happy, while the second man, HANK should look unimpressed)

BERT: You know I'm glad we got to do this. I haven't had a chance to get out on the water in months!

HANK: Yep, Sure has been a little while.

BERT: Right? (beat) I can’t believe I got such a good deal on this canoe, I mean $15!

HANK: I wouldn’t call it a deal; this thing has definitely seen better days. It kind of looks like this thing is rotting.

BERT: You have to admit this is nice though. It’s so peaceful out here! We’re just sitting out on the water, poles on our backs, wet feet..

HANK: I guess it’s- (beat) did you say wet feet?

(Hank looks down and sees that water is filling the canoe)

HANK: BERT! WE’RE LEAKING!!

BERT: Huh?.. Holy Mackerel!

HANK: Well don’t just sit there you oaf!! Grab a paddle!!

BERT: Oh my God! Tthis is so exciting!!

(Bert and Hank grab a paddle each from in the boat and begin to paddle)

HANK: This is not freaking exciting– why would you think this is exciting?!

BERT: Oh come on Hank, It’s not that bad. It’s just a little water!

HANK: BERT!! It is not the time, just help me paddle this frickin’ boat!

BERT: Alright, alright don’t get your swordfish in a knot.

HANK: Paddle, you salmon head!!

BERT: I am, I am!!

HANK: Not that way you idiot! You’re turning us around!

BERT: Ha ha, I haven't had this much fun since band camp!..

HANK: Bert you half wit, you’re making it worse!!

BERT: ..All those blowable instruments!

HANK: BERT!!

BERT: Huh?

HANK: Will you please just pay attention to what you’re doing!

BERT: Oh, right sorry I’m just having a really nice time.

HANK: (Angry)Well, I’m really happy! (beat) I never should came on this dumb fishing trip, but you just wouldn’t leave me alone about it, because you think it’s just so darn exciting!!

BERT: You think this trip is dumb?

HANK: Yes, Bert I do! I didn’t even want to come in the first place, but that's all you’ve been talking about for the last three and a half weeks! I mean give it rest for God's sake man!

BERT: ...Oh I didn’t realize you felt like that.

(Bert stops paddling)

HANK: What the heck are you doing? (beat) Bert don’t stop paddling!

BERT: Why didn’t you just say you didn’t want to come on the trip with me?

HANK: Bert whenever we get back to land we can have a long talk about it, but I need you to paddle!

(Bert still doesn't paddle)

HANK: Bert we’re taking on a lot of water here, and if you don’t start paddling I swear to god I will shove this ore so far up-!

BERT: I thought you were just as excited as I was about the trip.

HANK: Bert, please just help me!

BERT: I mean we never get to hang out anymore. We used to be buddies, we were inseparable!

HANK: We’re gonna have to plug this hole with something!

BERT: But Ha-

HANK: I’ll find something to stick in the hole, you’re gonna have to get some of this water out!

BERT: Oh alright! (beat) Well do you have a bucket?

HANK: No, I don't have a bucket! J- Just use your hat or something!

BERT: My hat?

HANK: Just do it!!

BERT: Fine, fine but you owe me a new hat. OH, WE CAN GO SHOPPING!

HANK: Whatever, just hurry up! I’ll just uhh (looks around nervously) Ah ha!

(Hank pulls off his gloves and quickly begins trying to shove them in the hole, while Bert frantically bails out water using his hat)

HANK: Almooost… HA! GOT IT!!

BERT: I don’t think that's going to hold very long.

HANK: Yeah I know! Are you still bailing?!

BERT: Nope all done! (leans back and plops his soaking hat back on his head) Well done, me!

HANK: Stop lying there you numbskull, we still gotta paddle!!

BERT: Oh come on, are you scared to get wet? (Splashes Hank)

HANK: Quit freaking splashing me!!

BERT: Oh, lighten up a little Hank!!

HANK: Dammit Bert! I can’t swim!!

BERT: (beat) What?!

HANK: I can’t swim! I never learned how, so can you please just drop it and help me with paddling this Gosh dang Boat!!

BERT: Well, why didn't you just tell me you couldn’t swim? I mean it’s a little embarrassing, but it’s not that big a deal, we could’ve done something else like go camping.. or throw eggs at cars!!

HANK: (Swings arm and points) BERT! Do you see that right there?! That thing is called a paddle and you use it to move canoes, so how about you pick the darn thing up, AND USE IT BEFORE I DROWN!!

(Bert pauses for a second, looking a little hurt before picking up the oar and begins rowing)

HANK: (Sighs) Finally. (beat) Do you have any idea how frustrating you are? You’re really going to have to speed up. We don't have that long until we’re at eye level with the fish!

BERT: I may be frustrating but at least I know how to swim.

HANK: Just hurry and shut up, we’re getting close.

BERT: Don’t tell me to shut up, all I wanted to do was hang out with my best friend!

HANK: For the love of- Bert you and I are not, nor will we ever be best friends! We never have been. All you are is that annoying guy from highschool that would never leave me the hell alone!! Why can’t you just leave me ALONE!!

(Bert is silent for a moment, and then gets a really stern look on his face)

BERT: Ok.

(Bert stops paddling)

HANK: What are you doing!? Are you stupid? I’ll drown!!

BERT: Oh well.

HANK: Listen here you oaf, help me or I swear to god I will drag you to the bottom of this lake!!

BERT: Go on then. I want you to, I want you to pull me down kicking and screaming!

HANK: Yo- YOU- gahh! What is wrong with you! You freaking idiot, row the dang boat!!

BERT: No. You’re going to sit here and sink to the bottom of this lake. (beat) and I’m going to sit here and watch.

HANK: The hell I am! When I get this boat to land we’re done, I never want to see or hear from you again!!

(Hank begins to frantically row)

BERT: This boat is not going to make it to land anyway, we’re too far out. (beat) Looks like you’re stuck out here.

HANK: Why did you even want to go fishing in the first place, you freaking psycho?!

BERT: I just wanted to go on a fun trip with my friend.

HANK: I should have never come with you. I should have ignored you in high school. I should have told you to get away from me and go bother someone else!

BERT: You should’ve learned how to swim.

HANK: You’re nothing but a slimy idiot! There's a reason no one spoke to you in high school, and why you’re a lonely man with no one in your life but me!!

BERT: Well, at least I’ll make it back home, and never have to listen to another insult come crawling out of your mouth, you selfish piece of crap!

HANK: Yeah you might make it home, but what then? You're just going to spend the rest of your sad pathetic life alone, with no friends, no family, and no purpose in this world!

BERT: Shut up..

HANK: You’ll have nobody! Hell, you don’t have anybody! I was the only person you had in your miserable life and I didn’t even want to hang out with you!!

BERT: Hank..

HANK: That is the most pathetic thing-

BERT: STOP! Just shut up, shut up, shut up!!

HANK: WHY!! Because I’m right!? (long Beat) ..Yeah that's what it is right?

BERT: Hank..stop.

HANK: Or what Bert? What are you going to do, yell, scream, or maybe you just sit there and complain?

BERT: GAHH!!

(Bert takes his oar and hits it over Hank’s head, Hank falls back in the canoe limp)

BERT:

(long beat) Hank?

(silence)

BERT: Hank?! (Shakes Hank) Hank wake up!

(Hank doesn’t move as a look of fear comes over Bert's face)

BERT: Oh god.. Hank, I'm so sorry! I didn’t mean it I swear, please forgive me!

(Bert sits in silence as the canoe sinks looking at Hank)

BERT: I shouldn’t have made you come with me on this trip, I just wanted us to hang out again. I'm sorry I forced you to be my friend, you were just the only person who ever talked to me. (beat) You’re right I am alone.

(Bert stares at Hank)

BERT: Oh god what have I done!? (Bert straightens up Hank so he's back in a sitting position) It’s alright Hank I- I -I’m not going to leave you. I’ll stay here with you I promise. (Bert sits with Hank. The sound of water gurgling and sloshing into the canoe grows louder as the canoe sinks, enveloping both Hank and Bert. The lights fade to black)

End of Play
```

---

## IC-1033: Winnebago

- Title: Winnebago
- Author (byline): Elijah Sams & Brian Sams
- Work: Winnebago
- Publisher: Mushroom Cloud Press
- Publication date as stated: August 15, 2024
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1522
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
Dad: Oh, jeez, kids, this is gonna be great! Get your bags and books and head out to the
Winnebago! Woohoo!
Tommy: Where are we going this time, Dad?
Dad: It's going to be quite a ride, Tommy. The Washington Monument, the Statue of Liberty and
then....
Jefferson: How many days should I pack for, Dad?
Dad: Two, Jeffy, we'll just be gone for the weekend! Jack?
Jack: What?
Dad: Get your stuff, buddy.
Jack: No. No way, Dad. These road trips are the worst.
Dad: Sorry, Jack old boy! The Winnebago waits for no man!
Jack: The Winnebago waits for every man, Dad. Even when it's running you can catch up to it
without breathing hard.
Dad: Tommy, Jefferson? Ready? (Putting on seat belt.) Jack, just one last trip. Alright
kids...Winnebago! Winnebago! Winnebago! (Turns key, acts like it starts.) Yes! We're off! (Sings
Born to be Wild by Steppenwolf.)
Intro: Road trips. You either love em or hate em, but most often what makes the difference is
the people you who are along with you for the ride. Winnebago.
Dad: Aw, jeez kids, would you look at that! The Washington Monument! What a sight! How tall,
Tommy?
Tommy: Ummm, 555 feet 5 and 1/8 inches, Dad!
Dad: Wowzers! When was it built?...Okay, Jefferson!
Jefferson: Construction began in 1848, but wasn't completed until 1888.

Jack: About like when you remodeled the bathroom, Dad.

Dad: Haha, Jack. (Turns off key, puts it in Park.) Alright, let's get the tour! (Exits the Winnebago) Dad: Huh, that's weird. No tour guides. Looks like we have the place to ourselves again! Jefferson: Dad, you be the tour guide! Dad: Alright, let's see. Welcome to the Washington Monument! Built to commemorate George Washington, this tower... Jack: Obelisk, Dad. It's an obelisk. It has four sides and it tapers to the top. It's an obelisk. Dad: Thank you, Jack. As I was saying... This tower---ing obelisk is 555 feet tall and was completed in 1888. It took so long to complete because the hardware store is a long ways away and you don't always have the right fittings for the shower... Tommy: The book says it took a long time because of a lack of funds. Dad: Well, I can believe in that, Tommy! Jefferson, what else can you tell us about this towering basilisk? Jefferson: Obelisk, Daddy! Well, when it was completed, it was the tallest building in the world, beating out the Cologne Cathedral, until the Eiffel Tower was built in 1889, in Paris, France. Dad: Darn those French! What an insult! I'm pretty sure there's nothing they could do to make up for that! Oh, no wait, French Fries! Jack: Not actually French. Probably Belgian. Dad: See, there you go! French culinary oppression! Come see the violence inherent in the system! Did you kids read everything? Good. Off to the Statue of Liberty! I want you to draw a picture of the monument for Mommy and read up on the Statue! It's a four hour drive, so grab a sandwich, finish your reading, and take a nap! Lotsa room in the Winnebago! Winnebago! Winnebago! Winnebago! (Turns key and it “starts”) Woohoo! (Singing Life is a Highway) Jack: Dad, how long is this going to take? Dad: Grab a sandwich, Jack! This is the whole weekend!

Jack: I can see that you're teaching the boys a lot, Dad, but why am I here?
Dad: Hey, buddy, a couple months and bam, you're off to college. Full ride scholarship, though!
Why's that?
Jack: Because you made me study on our road trips.
Dad: And...?
Jack: And we haven't got a dime thanks to all the medical bills...
Dad: C'mon Jack, none of that! And...
Jack: And instilled a natural curiosity and love of learning... College entrance essay #2.
Dad: So just humor your old dad, and enjoy the trip.
Jack: Oh, it's a trip alright.
Dad: Ah, you'll soon find yourself loving it, Jack! You always do! Winnebago! Winnebago!
Winnebago! Yes!
Transition - Country Roads -
Dad: Tommy, Jefferson! Wake up! There she is! The Statue of Liberty! Gosh, what a beaut! Got
your shoes on? Fantastic! Out we go! Whattya say we find ourselves an authentic New York
tour guide?
Tommy: I don't know, Dad, I don't see any tour guides.
Jefferson: Neither do I!
Jack: Amazing. Eight and half million people and no tour guides.
Dad: Yeah, Jack, you'd think there'd be an unemployed comedian looking for work...
Tommy: Do it, Dad! Be the tour guide!
Dad: (Now in a New York accent, strong, but poorly done.) Awright, 'spose you two utes could
tell me what it is that we're looking at right over here?
Jefferson: The Statue of Liberty!

Dad: Uh huh, uh huh, dat's correct, hows about some particulars? Tommy: She's was a gift from France, and it's pretty neat that she was built by Gustav Eiffel, the man that beat the Washington Monument for tallest building. Dad: Them Frenchies will surprise you, eh? Now, whose can tells me how much green paint it takes to paint milady each and every year? Tommy? Jefferson? Bueller? Bueller? Hey, you lookin' at me? Jack: Not really. Dad: You lookin at me? You lookin at me? I’m tour guidin’ here! I’m tour guidin’ here! So, how much paint, smart guy? Jack: None. Is that supposed to be DeNiro? That's terrible. Originally, it would have been a bright copper color, but over time it developed the green patina... Dad: Yeah, yeah, yeah. Smarty pants, farty pants. Tommy, Jefferson, hows about chu elucidate Alfred Einstein here about what this fantastical sculpture represents? Jefferson: According to the articles you gave us, Dad... Dad: Eh! Oh! Oh! Eh! Jefferson: Oops, sorry random, aggressive, New York tour guide, there are several symbols used. On her book is written, July 4, 1776, and by her feet there are broken chains. Tommy: And her torch is supposed to symbolize freedom. The real name of the Statue is Liberty Enlightening the World. Dad: Jeez, you kids are so smart! Won't your mom be so proud! Back in the ol' RV, bust out your no. 2s and Crayolas and get to work! Give me your tired, your poor, your huddled masses yearning to breathe free, the wretched refuse of your teeming shore! Something, something, something... Jack: Send these, the homeless, tempest tossed, to me, I lift my lamp beside the golden door. Speaking of homeless, how long until we move into this thing full time? Dad: Hey! Not in front of the kids! Alright, everyone set? Juice boxes ready? Hand one to me...no, don't squeeze it.... ah, no that's okay, happens to the best of us. You can read up on hydraulics, Tommy, we've got a long drive, an overnighter! Winnebago, Winnebago, Winnebago! Yes! Grand Canyon, here we come!

Jack: I'm not staying in the Winnebago overnight, Dad. Dad: C'mon. It's a family road trip! Where else are you gonna go? Jack: I'm going to open this door, step out onto the lawn, walk across the yard and back into our house. Dad: Jack, you'll ruin it for the kids! Jack: Dad, I'm seventeen! I can't play kid’s games anymore. Dad: Your mother doesn't want you in there right now. Jack: Are you serious? You're out here playing games with Tommy and Jefferson and who's helping Mom get to the bathroom? Or don't you care? Dad: She's meeting with a hospice nurse. Jack: What? Hospice is for people that are dying. Mom's just sick… Mom’s just sick, right? Dad: She's stopping certain meds and starting some others that will make things... easier.. Mom didn't want you guys there tonight, it might not be... very pleasant. Tomorrow. After the Grand Canyon. Jack: Holy crap, Dad! Mom's dying and you've got us trapped in a broken down Winnebago playing road trip again! Dad: What do you want me to do, Jack? She asked me to. One last road trip, with pictures from the little boys and me to try to break this to you... which I guess I didn't do a very good job. I'm sorry. We never really had the time or the money to take you anyplace for real. Just this. I thought I'd get it fixed someday and... Jack: Dad. Check out the sunset! Dad: It's nice, Jack. It's a nice sunset. Jack: It's more than a nice sunset! It's a Grand Canyon Sunset! Dad: It's a 34 hour drive to Arizona, Jack. The boys expect a certain amount of realism... Jack: It's the Grand Canyon, Dad.

Dad: Okay... Great news, kids! We're already at the Grand Canyon! And just in time for sunset!
Too late for tour guides, I'm afraid. Everyone out!
Dad: Great Scot! You were right Jack, that's one heckuva sunset.
Tommy: Wow. Thanks for taking us to the Grand Canyon, Dad.
Jefferson: Yeah. Wait until I tell Mom about this view.
Jack: Hey, Dad, you're doing a great job, but we should take the kids to Italy sometime. Rome.
Pompeii, Mount Vesuvius and all that.
Dad: Jack, you know we can't afford that, there's not going to be any life insurance, if that's what
you're...
Jack: No, Dad, I meant, we could take the Winnebago.
Dad: Oh. I see. Hey, kids! Can you believe that this here canyon was just made by Paul Bunyan
dragging his axe?
Jack: Just...just enjoy the moment, Dad.
```

---

## IC-1034: DUCK SURGEON A Play, by Dudley Rental

- Title: DUCK SURGEON A Play, by Dudley Rental
- Author (byline): Dudley Rental
- Work: DUCK SURGEON A Play, by Dudley Rental
- Publisher: Mushroom Cloud Press
- Publication date as stated: 2013
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: VOICE, PATIENT 1, PATIENT 2, SIMON, DR. DUCK, GATOR, BUSHY, KATIE
- Teaser before the introduction: No
- Spoken words (computed): 1585
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
Scene: A Commercial

VOICE: Surgery can be a real pain in the butt.

PATIENT 1: Ow, my butt!

VOICE: No, we mean, a REAL pain in the butt.

PATIENT 2: What are you doing to my butt? Couldn’t you at least numb it first??

VOICE: Love Handles General Hospital is gentle with your butt.

PATIENT 1: Yeah, that actually feels kinda nice!

PATIENT 2: I never knew I could enjoy extensive, elective butt surgery this much.

VOICE: And if we’re not gentle enough on your butt, your next margarita is free. Because we have a Chili’s inside our hospital.

PATIENT 1: I was eating fajitas during my surgery!

PATIENT 2: And I think there’s no better place to recover from butt surgery than in the comfy pleather booth of a Chili’s, humming along to the latest hit song by Macklemore while I consume enough sodium to kill a rabbit.

VOICE: So come on down to Love Handles General Hospital, where your butt is in good hands.

PATIENT 1: More codine queso, please!

VOICE: Coming right up! (Suddenly, talking very fast.) We are required by law to disclose that some of the doctors at Love Handles General Hospital and Mexican Grill are in fact ducks. Love Handles General Hospital and Mexican Grill cannot guarantee that your surgery will not be performed by ducks.

PATIENT 1: Wait, what? Did you say... ducks?

VOICE: Here’s your queso!

(End of commercial)

Theme Song
Duck Surgeon! Duck Surgeon!
He’s a duck who does surgery!
Paging Dr. Quack, come quick,
It’s a ducking emergency!
Somebody didn’t duck, on a badminton court,
And now they have a shuttlecock lodged in their head!
Duck Surgeon! Duck Surgeon!
Operate on this person before they are dead!

Scene: Love Handles General Hospital

DR. DUCK (somehow talking on a phone): Quack? Quack quack. QUACK. Quack quack. Quaaaaack. Qua-qua-quak. Quack. Quack Quack –

(The door bursts open and Simon comes flying in. Dr. Duck throws down the phone and holds his wing down, hoping Simon did not see.)

SIMON: DR. DUCK!

DR. DUCK: Quack!

SIMON: OH! AH! DR. DUCK!

DR. DUCK: Quack! Quack!

SIMON: AHHHHHHHHHHH!

DR. DUCK: Quaaaaaaaaaaaacck!!!

SIMON: THEY’RE HAVING BUFFALO WRAPS TODAY IN THE CAFETERIA!

DR. DUCK: Quack?

SIMON: Sorry, I’m still having that problem where I get excited about the wrong things. Also, the entire city has been hit with a plague of idiocy that makes everyone act really stupid. None of the other doctors can figure it out, and some of them worry it’s because they’re already affected. You’re our only hope, Dr. Quack - as a duck you’re immune to the disease.

DR. DUCK: Quack! Quack.

SIMON: Right. Nothing could make you more stupid. Dr. DUCK: Quack.

SIMON: By the way, here’s your new intern, Gator.

GATOR: Howdy, Lil’ Feathered Fella! Sure is a nice house of witchcraft you got here. And a Chili’s on the top floor! Mmmmm, that’s good medicine!

DR. DUCK: Quaaaack!

SIMON: No, he hasn’t caught the stupidity plague. He’s always like this.

GATOR: You guys wanna head out on the river in my airboat this weekend? I just installed a flatscreen on it so we can watch fishin’ shows while we fish!

DR. DUCK: ...Quack.

SIMON: I’ll come to, EVEN THOUGH AIRBOATS TRIGGER MY PHOBIA OF CHANNING TATUM! Sorry, sorry. Dr. Duck, here’s your first patient. A 14-year-old named Bushy, whose phone became fused to his hand.

BUSHY: You can take it off, Doc, as soon as I get to the next level of Candy Crush.

DR. DUCK: Quack.

BUSHY: (looking up for the first time) Wha... I’m scared of ducks.

SIMON: No need to be afraid of Dr. Duck, he’s an internationally known specialist in internal medicine who attended Georgetown Medical School, speaks 5 languages, and can dive up to 20 feet at a time when searching for delicious mollusks. No, my little friend, you have nothing to be afraid of –

DR. DUCK: QUUUAAAAAAACCCKKK!!!! (attacks Bushy)

BUSHY: What are you doing! Help! This duck is assaulting me. He’s perched on my face. How is this medicine? I want a second opinion! The feathers, the feathers are up my nose. He’s biting my hand! He’s drooling on me! Son of a - ow! The duck is down my pants! Got him out - now he’s on my hand again. Come on! Duck! Hey! Duck! Dr. Quack! Hey! Hey! Hey! This is worse than the time I got in a pillow fight with a homeless guy! Please stop! I can’t take any more duck! No more duck in the face, please, please. (He puts his hands to his face) Hey... wait a second - the phone fell off my hands!

GATOR: Duck spit dissolves super glue. (He grabs the phone) I’ll take this - you need a little timeout from Candy Crush.

BUSHY: Aw, rats.

GATOR: Why that’s an old bit of swamp magic! I once glued my hand to an airboat throttle because my momma broke my moonshine still.

SIMON: She didn’t want you making hooch?

GATOR: Naw, she got drunk on it and fell face first into the tank, cracked it right open! My mom had a forehead hard enough crack anything.

BUSHY: How did he know I glued it to my hand?

DR. DUCK: Quack.

SIMON: Because you were so stupid, you thought it would save you time.

BUSHY: I realize it was a dumb idea now.

SIMON: You’re cured. Out you go. And in comes the new patient. Katie Bunches, Age 16. Refuses to eat anything but a nacho cheese taco DIPPED IN A MOUNTAIN DEW CODE RED SLUSHIE! THAT SOUNDS DISGUSTING! WHY AM I SO EXCITED? Anyway the diet is probably going to kill her.

GATOR: Oh yeah. I mean, same thing killed both my uncles. Though of them also snorted a lot of motor oil. No, my mistake, they both did. They both snorted motor oil. Haha, yep. Probably that was what killed them. (Shaking head, suddenly quiet.) That was an awful fireworks show...

SIMON: What should we do?

DR. DUCK: Quack quack. (Pokes at orange on table.)

SIMON: The orange?

KATIE: The what? What’s an orange?

DR. DUCK: Quack.

SIMON: Katie, have you ever eaten an orange?

KATIE: That this is weird. And orange-colored. Ugh.

DR. DUCK: Quack!

GATOR: Think this little fella wants you to eat the orange.

KATIE: But the orange is all the way over there... DR. DUCK (biting her on the ankles) Quack.

KATIE: Ow! Ok, ok, I’ll go get it. Mmmmm... mmm this is good! Why does anyone ever go to a Taco Bell when they could literally just take this off of a tree in their yard for free? I’ll never eat that stuff again. Mmmm! Oranges!

SIMON: Ok, great. Get out of here. (To Dr. Duck) I’ve never seen someone cured right before my eyes.

DR. DUCK: Quack, quack.

SIMON: Yeah, I love Taco Bell too.

DR. DUCK: (Burps.)

GATOR: (lugging something in) Here’s your next patient. She’s in bad shape.

SIMON: Tasha Reynolds. Tasha filled a kiddie pool full of light beer. And then she dove in. At age 23, she was a little big for a pool meant for ages 3 to 4. And now Tasha is stuck in the kiddie pool full of light beer. The foam from the bear will enter her brain, and she will die of lightheadedness.

GATOR: I seen a lot of things in the swamp. Crazy things. Things that’ll make a man go mad. But I ain’t never seen a thing like this.

DR. DUCK: Quack.

SIMON: That’s right. (Looks at his watch) She’s got only a few minutes to live. HOLY FRIJOLES IT’S 5 O’CLOCK! IT’S HAPPY HOUR AT THE CHILI’S UPSTAIRS! Sorry.

DR. DUCK: Quack. Quack.

SIMON: Wait, you think we should go to Happy Hour at Chili’s? And bring the patient too? THAT’S THE BEST IDEA I’VE EVER HEARD! I mean, that’s insane, Dr. Duck, you’ll surely kill her.

DR. DUCK: Quack!

GATOR: We best do as he says. What if you caught the disease and are already gettin’ too stupid to figure it out?

SIMON: That’s madness.

GATOR: I lost my grandma to a furious duck. She had just stuffed it in the oven, then tried to open it up again to throw in a few squirrels too. The duck came fast, and the squirrels... those bastards finished the job. Since then I hated squirrels, but I always respected ducks. They’re fighters.

SIMON: Let’s get this kiddie pool to the freight elevator. It opens straight onto the lobby of Chili’s.

(They struggle, drag the pool to the elevator, then arrive at Chili’s)

GATOR: Table for 4 please.

DR. DUCK: Quack!

GATOR: Booth, please. Oh. They gave us a little buzzer. There’s a wait.

DR. DUCK: Quack! Quack! Quack!

SIMON: We have to wait Dr. Duck. Those are the rules. Oh look, here comes someone’s fajitas. The fajitas that might save this woman’s life... those delicious fajitas... HEY! HEY! WE NEED THOSE FAJITAS! MEDICAL EMERGENCY! DELIVER THOSE FAJITAS TO DR. DUCK, STAT!

GATOR: Ok, we got the Fajitas. Now what do we do?

DR. DUCK: Quack, quack, quack.

SIMON: There’s no time! I know how to make a damn fajita. First, the warm, fresh tortilla. Then the spreading of the savory grilled onions, and the zesty green peppers. Layer... layer the mouth-watering flame-kissed chicken bits. And then, last, the cheese, raining down on top of it all, and decadent guacamole, and oh - oh - oh you’re so bad, Simon - a big dollop of sour cream. (He pauses. He is clearly about to eat the fajita.)

DR. DUCK: Quack!

SIMON: And then.... you give it to the patient...

GATOR: WOW, she ate it in two bites! Simon! Shove some more into her face!

SIMON: (About to eat another fajita) Oh... yes, this one was for her too.

GATOR: The fajitas have stabilized the light beer by allowing her to absorb more frothy suds. Just give her one more...

SIMON: No. I am eating this one. She can wait for more tortillas.

GATOR: I’m sure she’ll be fine. Excuse me, waiter? Make sure to add an order of chicken fajitas to this patient’s hospital bill.

DR. DUCK: Quack!

GATOR: That’s right, Dr. Duck, this here whole hospital is mine, and the Chili’s too. I’m the owner, Dr. Silas Cornbutt, Attorney at Law.

SIMON: Attorney?

GATOR: What? I went to Yale Law after my moonshinin’ years, but before I decided to switch to medicine.

SIMON: Why were you pretending to be an intern?

GATOR: I wanted to see if Dr. Duck was ready for the big promotion.

SIMON: Head of Medicine at Love Handles General Hospital?

GATOR: Nope - General Manager of the Chili’s!

DR. DUCK: Quack quack quack.

GATOR: That’s right, Dr. Duck, from now on all your meals here are 30% off!

SIMON: You only promoted him because he was a duck.

GATOR: Well, as Mama always said to Pop, better to be a duck, than a dick.

DR. DUCK: Quaaaack!
```

---

## IC-1035: Everyone's Still Dead A Tribute Play to Clyde Hendrickson, Written By Dudley Rental

- Title: Everyone's Still Dead A Tribute Play to Clyde Hendrickson, Written By Dudley Rental
- Author (byline): Not specified
- Work: Everyone's Still Dead A Tribute Play to Clyde Hendrickson, Written By Dudley Rental
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1974
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
(Tom and Ben are in a psych ward. They are making lots of drug induced convulsions, weird faces, etc.
Tom and Ben are obviously hallucinating.)
TOM. This is the good part! Hold on, Hold on… can you feel it?
BEN. Oh yeah… ooohhhh yeah
TOM. Oh man, did you see that? did you see that?
BEN. Pink camels everywhere.
TOM. That would explain the two humps in your pants.
BEN. Wait… wait… here comes the best part! Can you see this, Mr. Pink Donkey? Yeah? well screw you
too!
TOM. Oh my. Oh, oh my. Auntie Jemima, I’m comin home to you!

(suddenly interrupted by door slamming/nurse) BEN. Ah! Wha? TOM. Uhhh… one moment….

(they try to compose themselves)
BEN. Why… no nurse, we would never do something like sniff all the helium for the party balloons while
simultaneously drinking all the robutussin we could get our hands on.
TOM. No. Never.
BEN. We’re angels. Now, can someone get this lusty pink lemur off my back? He’s starting to get a bit
uppity.
TOM. Uh, Ben…
BEN. I mean, uh... you’re my lusty lemur… Nurse Carmicheal…. with your… (shudders) tantalizing
waves of flesh.
TOM. Yes nurse, I’ll see to him. Good day!
BEN. Bye bye…. lover. (disappointed sigh) We have got to get a better hobby.
TOM. We live in the psych ward. The only allowed hobbies are ball bouncing and connect the dots.
BEN. Actually, I had my ball bouncing privleges taken away for recklessly beating the elderly.
TOM. A shame.
BEN. Yeah.
TOM. I feel smothered.
BEN. Mmmhmm, it’s like we’ve been buried under a pile of dead babies.
TOM. Uh huh…

BEN. And then the babies come alive and start trying to eat us.
TOM. Ok. moving on…
BEN. And we keep trying to dig our way out but they just keep throwing on MORE BABIES AND MORE
BABIES. (pauses desperately before exploding) LET ME OUT OF THIS TODDLER HELLHOLE, YOU
BASTARDS!
TOM. (ben breathing heavily) …are you finished?
BEN. Yes. Now let’s get to the bottom of our mysterious circumstances.
TOM. Alright. (thinks briefly) I’ve got it. We’ve been on drugs. Hard drugs.
BEN. No, something more sinister is at work here, and I’m not talking about that pink version of Andrew
Jackson.
TOM. The commie bastard.
BEN. We’ve been out cold for days: our pink animals taken, our honor defiled, our wives… ravished.
TOM. Our wives divorced us. We’re psycho, remember?
BEN. Ah yes. But I married the toaster last week. See, here’s the certificate. Oh what a lover Mr. Warm
Slots is.
TOM. (taking certificate) Ben, the nurses gave that to you so you would stop befouling their breakfast.
BEN. Lies! (sniffs) The air is filled with treachery. (sniffs again) And eroticism. Lots of eroticism.
TOM. I can’t argue with that.
BEN. This can mean only one thing.
TOM. What?
BEN. The Brits are trying to retake the colonies!
TOM. Uh, somehow I don’t think that’s what it means. Margaret Thatcher is not very erotic.
BEN. I expected so much from you, you lousy canadian.
TOM. Half-canadian. I was raised in Maine.
BEN. I was raised to bludgeon british subjects every night!
TOM. I’m one bad mountie you don’t want to mess with, yah.
BEN. You’re no match for… (transforms himself into a revolutionary pose) Patrick Henry.
TOM. Can I help you sir, yah?
BEN. Ah, I can take advantage of your canadian submissiveness with my American cowboy diplomacy.
TOM. Yah.

BEN. Good mountie… may I beat you senseless?
TOM. Sure. Here is my nightstick, yah?
BEN. I love being a patriot.
TOM. Would you like some gasoline too, yah?
BEN. A little here, a dab there… the flame of liberty will always burn, my friend.
TOM. Yah I’m just like a fried pig canuck no?
BEN. I don’t eat canadian bacon. (lights)
TOM. Whooooaaah…. a little intense, eh, Ben?
BEN. I’m just trying to make this as historically accurate as possible. After all, I am a historian.
TOM. How do you know so much about this revolution anyhow?
BEN. A little kid told me.
TOM. I thought by law you weren’t allowed to be around children.
BEN. But this was a… special child. (sexual implications)
TOM. Who?
BEN. Very… special.
TOM. Who was he?
BEN. He looked a lot like you, actually.
TOM. Ohh… you mean (pops) this child!
BEN. How ya doin little fella?
TOM. Boy oh boy, mister, I sure do love the american revolution.
BEN. And I love when you talk dirty to me.
TOM. Can I have your autograph, Mr. Washington?
BEN. Not now son, Uncle George is busy busting British beans.
TOM. I’ll do my dance for you!
BEN. That’s really not necessary.
TOM. (singing) We represent the Lexington league (continues while Ben talks)
BEN. Please stop… oh the horror… uh nurse! nurse, can I borrow that tazer? Thank you. Ok, little Timmy
(stops singing), here’s an autograph for you.

TOM. Oh boy! (gets tazered) Golly, that tickles! (zapped again). Oooh! (zapped) Uhm, my face is starting
to burn (zapped into submission).
BEN. Ah, I love the smell of fried children.
TOM. This is taking too long… we haven’t even killed a single brit yet.
BEN. You’re right. I shall be Muhammed Ali: lean, mean, revolutionary machine.
TOM. And I will play the marauding redcoats.
BEN. I float like a federalist, sting like a bee!

(Ben procedes to punch, uppercut, kick in groin Brits, who scream things like “bloody hell” and “crikey”) TOM. (indian) How. White devil shall not defeat us again.

(Ben coughs. Indian catches pneumonia, sneezes, dies.)
TOM. I’m Ben Franklin – you can’t kill a fellow patriot.
BEN. You’re right. Here, have this kite. (Franklin is electrocuted, dies.)
TOM. (in small, joyous, stupid voice) You wouldn’t kill a sweet little differently abled child, would you?
BEN. Ahhh(stops mid punch) no. Awwww… let’s sing the happy song!
Both: This is the happy song, Oh I love the happy song, It makes me so very very happy cause… (song
repeats. As they both sing, Ben stops dancing while continuing to sing. He quickly prepares a large
revolutionary style cannon and fires.)
TOM. You heartless bastard.
BEN. Yep. Had it shot out in the War of 1812.
TOM. Too bad I shall now kill you… with your own tweezers! (steals tweezers)
BEN. OW! (killed with tweezers). Apparently, I wasn’t patriotic enough.
TOM. Let’s keep this war moving!
BEN. You’re the boss.
TOM. Ok, now you’re George Washington. Didn’t he grow lots of hemp?
BEN. Yes…
TOM. Dude, then can I get a hit off that gnarly hemp wig of yours?
BEN. Well, I don’t see… No! Get away.
TOM. Denied.
BEN. Rightfully so. Now, I need a Jefferson.
TOM. (like guy from TV show “The Jeffersons”) Weezie, Get in heah!

BEN. I need a Thomas Jefferson.
TOM. Georgie! Get in heah.
BEN. More colonial.
TOM. Goooooood Evening, George. Care for a revolution?
BEN. No.
TOM. Come on, Ben, play along.
BEN. This is MY revolution. You don’t get to help.
TOM. Sure I do. Victory is all about teamwork!
BEN. Oh, that was SO the trojan war. This is the 18th century – individualism is in.
TOM. Let me do just a little revolting.
BEN. Well, maybe I’ll… (faking, pointing the opposite direction) Look! A young slave mistress!
TOM. Where?
BEN. Made ya look! (kills him with some inventive karate or something)
TOM. That wasn’t fair. I was on your side.
BEN. Says you.
TOM. Says my pal Jesus, too! You will pay for that.
BEN. How?
TOM. I will be your worst enemy… a scourge from within.
BEN. You couldn’t possibly mean…
TOM. Oh yes… (pops) Oh Georgie-poo! Remember me, old wooden-tooth?
BEN. (winces at her voice). Hello, Martha. (winces again at her name).
TOM. Oh George, it’s been so long since I’ve felt your touch… (George shudders) and thank heavens for
it!
BEN. I tried to be a good husband Martha. It’s hard to be spouse and a revolutionary.
TOM. The only revolution you started is the one with male domination!
BEN. Oh, Martha, really.
TOM. I’m smelly and old! listen to me! I’ve been involved in resurrecting you and your friends.
BEN. You have?

TOM. Yes, I have. There was a great disturbance in history, and I had to get you boys back before the
Adamses through another tea party.
BEN. So you brought me back to save the nation?
TOM. Screw the nation. I just wanted to nag you again.
BEN. Martha, why are you so bitter?
TOM. You never gave me the treatment I deserved.
BEN. But I did! I bludgeoned you every night.
TOM. You should have finished the job!

(George gives look of approval, wails on her. He lets up after awhile) TOM. You missed a spot!

(George beats again)
TOM. I’ll see you in hell, and your extra nipples too!
BEN. (shamefully covering chest) Shhhhhh! (Martha dies)I’ll never know how they can solve domestic
disputes these days without a good wailing.
TOM. I believe it involves several lawyers and a well orchestrated pony riding accident.
BEN. That’s for another day. Let’s move on: George has discovered the plot, now he needs more clues.
Who does he run into next?
TOM. Former President Elanor Roosevelt.
BEN. No, he doesn’t like women in power, remember?
TOM. You just shoot down all my ideas. Fine then, I’ll just pretend I’m drunk.
BEN. Come now, you always do this when we’re having a little tiff.
TOM. Hey George, remember me? Remember ol’ Eli?
George: Eli?
TOM. (obviously drunk) Eli Whitney, that’s me!
BEN. Whitney… ah yes, the gin.
TOM. I don’t know nuttin about yer gin!
BEN. I meant the cotton gin.
TOM. (suspisciously) Oh yeah... right.
BEN. I’ve got a proposition for you, Whitney.
TOM. Oh, you always were a dirty one, Mrs. Adams. You can make a patriot out of me anyday.

BEN. I am not your revolutionary hussie! Get your hands off of me!
TOM. You always were a tough cookie, m’lady.
BEN. Now listen, Whitney, get some sense into yourself. We have a problem. Someone in this era has been
changing history, bringing us old folks back to life, defiling lady liberty…
TOM. You keep your hands offa my woman, Washington!
BEN. Eli… this person is an evil person…
TOM. You’re right, George, but you should watch yer mouth - someone is trying to destroy our nation…
and that someone is me!

(Tom rips “mask” off, reveals self to be Benedict Arnold)
BEN. Arnold!
TOM. Comma Benedict.
BEN. I’m gonna be the original Thug Gangsta President, Booker T. Washington.
TOM. Bring it on, “home boy”.
BEN. I’ve had jus’ bout enough of yo First Amendment. Now iz time to feel duh bizurn from my sizecond
amendment. (shoots him)
TOM. Your bullets can’t hurt me.
BEN. (during this sequence, he grabs something huge and wields it infront of his waist as a giant phallis)
Well den, I guess they didn’t gimme dis big “washin’ton monument” fo’ nothin!
TOM. Oww! Watch where you point that thing.
BEN. Prepare for the ultimate bitch-slap. (kills him with phallis) That wasn’t as hard as I expected it to be.
(Tom begins to laugh again) Come on Tom, let’s go…
TOM. Mwuahahahaha
BEN. Wha?
TOM. You’ll have to beat a more royal foe to destroy the twisted hopes of inbred England!
BEN. You mean, crazy King George III?
TOM. What of King George? I shall be a king twice his stature and thrice his weight!
BEN. No!
TOM. Yes! I am King Henry the Eighth, and I shall devour you as I devoured my wives.
BEN. (as he is bitten by the king) Oww!
TOM. Mmmmm…. like a fresh baby sandwhich.

BEN. But, but… you’re no match for… Former President Bob Barker!
TOM. Come on down, tallywhacker.
BEN. Don’t make me beat you with my skinny microphone.
TOM. Nooo… nooo… it burns! it burns! Blaargh… (eats mic, chews).
BEN. Geez… I guess it’s time to go to the bonus round. Today you’ll be bidding on… (pulls out short
person) one midget!
TOM. Unngh?
BEN. Now, the American pasttime: midget bowling. (to midget) Don’t worry little guy, you’re going to a
better place.
TOM. Don’t make me laugh!
BEN. Here we gooo…. (bowls midget, which lands in king’s mouth) Strike! Yes. (King begins to choke)
Where’s your protestant church now? (King dies) Well that’s done with. Now, which one of you lucky
ladies wants to be my next high bid?
TOM. (suddenly recovering) Ben! Oh Ben, how I’ve missed you.
BEN. Tom! Where have you been?
TOM. Dead for 200 years.
BEN. Really? Did you see Jesus?
TOM. Oh yes.
BEN. Did he say anything about giving me back my camels?
TOM. No. But he did condemn you to hell.
BEN. Fair enough.
TOM. (beat)Well… this was a perfect waste of time.
BEN. Eh, I don’t think so, Tom.
TOM. Then you really are crazy.
BEN. They don’t beat me every night with rubber mallets for nothing!
TOM. Heheh. Boy do those sting.
BEN. Seriously, though, if having fun with life isn’t worthwhile, then what is?
TOM. Perhaps something slightly moral?
BEN. Nah, that’s just pishposh. If history was always depressing you, why would it be worth making some
more?
TOM. You’re right. From now on, we’re gonna make history damn entertaining.

BEN. We already have, Tom; we already have.

(They both nod in agreement for a few seconds. Just when it seems like it’s over…) TOM. Got any Robotussin?

Ze End.
```

---

## IC-1036: Everything falls Off

- Title: Everything falls Off
- Author (byline): Clyde Hendrickson.
- Work: Everything falls Off
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2565
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
Everything Falls Off

Setting: A small dorm-like room. Could be comfortable, but it has been neglected by its owners for a while. There are two beds and two chairs.

Characters: NATE. A 30-year old who acts younger than he looks. SYD. A crotchety old man. Missing fingers and/or arms.

Everything Falls Off

Everything

falls

Off

(Syd’s doing something weird when Nate enters, with suitcase and bag.) NATE. Uh… is this my room? SYD. Number? NATE. Well… what? SYD. Number? Room number? NATE. Oh! I’m looking for 23. SYD. Son of a gun. NATE. Wrong one? SYD. No. This is 23. NATE. Are we gonna be roommates then? SYD. God I hope not. NATE. Oh.

Everything Falls Off

SYD. You should hope for the same.
NATE. Why?
SYD. Because my roommates drop like flies.
NATE. I see.
SYD. They come in here fresh as fruitcakes, and the next thing you know it, they’re hauling them off in
wheelbarrows and pickle jars.
NATE. Pickle Jars?!
SYD. Yeah, you’d think we were in a leper colony or something.
NATE. Well, we are in a leper colony. I was diagnosed two weeks ago.
SYD. Mmm… yeah I see your sense of humor was the first to go. Well, welcome to Zombieland. Let me be the
first to say: I’m going to fantasize about bowling with your head.
NATE. Wow. Have you been a leper for a long time?
SYD. Let me count the years. (shows missing fingers as he does)
NATE. I see.
SYD. It’s more what you don’t see, isn’t it? (laughs evilly)
NATE. (struggling with bags) God these are heavy. Can you spare a hand? (Syd reacts. Nate notices his
mistake.) Oh, I guess… I guess not.
SYD. Hey! Don’t put those there. That’s my floor.
NATE. Ok, what’s my floor?
SYD. All this is mine (indicating wide area). All that is yours.
NATE. Ok.
SYD. But only up to 3 feet off the ground. The rest of the airspace is mine.
NATE. Why do you need airspace?
SYD. I don’t. I just like the idea that I can make you crawl around.
NATE. Oh.
SYD. Otherwise, make yourself at home! And try not to speak to me unless I would care.
NATE. Ok. (sits down). I miss my real home.
SYD. Don’t care!
NATE. (sighs) So, what does one do for fun in a leper colony?

Everything Falls Off
SYD. Besides peeling off whatever’s flaking today?
NATE. Yes, besides that.
SYD. I make designer curtains from stolen gauze. But don’t you think you’re getting any.
NATE. I live in your room and we share a window. I can’t help having the same curtains as you.
SYD. Thief! How dare you threaten to steal the aesthetic value of my interior decorating.
NATE. But you stole all the decorations to begin with.
SYD. Stupid. Ugh. You just don’t get it.
NATE. Let’s play a game!
SYD. Ok.
NATE. Wow, you agreed. I didn’t know you were capable of agreeing.
SYD. I’m a man of many talents.
NATE. Alright… what game?
SYD. The Shut-Up game.
NATE. How does that game-
SYD. SHUT UP!
NATE. - oh.
SYD. You lose.
NATE. You’re no fun. (playing the common practical joke) Got your nose!
SYD. What? WHAT? (frantic, searching) How much of it? (pries open Nate’s hand, sees he doesn’t have it)
Where’d you see it last?
NATE. No, no, Syd, it’s a joke. To ease the tension.
SYD. Don’t you EVER play that joke around here, son, understand?
NATE. Don’t be so uptight.
SYD. If things were fallin’ offa you as fast as they’re fallin’ off of me, believe me, you’d hold on tight too.
NATE. We’re all lepers… nobody’s making fun of anybody.
SYD. I dunno, I think the guy in room 6 has been fakin’.
NATE. Why?
SYD. He only loses fingernails and eyelashes… says he has a “mild case.” Yeah right, he’s just here to check out
the nurses.

Everything Falls Off
NATE. All our nurses are 40 year-old males with drinking problems.
SYD. (looking at Nate closely) Yeah well, people got some funny tastes in nurses these days. Back in my day, they
wouldn’t even let you fill out an application to be a nurse if you didn’t have a d-cup and (indicates legs) primo
stems.
NATE. Anyway I was talking to Mr. Nickerson about living here, and he said -
SYD. Who?
NATE. Ned Nickerson, he lives in number-
SYD. Ned the Nugget! Hah.
NATE. You shouldn’t call him that.
SYD. But he has no arms or legs! How can I help myself?
NATE. Maybe with some compassion?
SYD. What is this strange (pronounced like foreign word) “compassion” you speak of, foreign devil?

(awkward silence, which Nate tries to break)
NATE. Wouldn’t bowling with my head be hard? Your fingers would get all gunky from my eyes.
SYD. Nah, I’d take your eyes for ping-pong.
NATE. Oh. Still, I’m all lumpy.
SYD. The alley has a slight downward incline.
NATE. Oh.

(another silence)
SYD. So… have you lost the big one?
NATE. Excuse me?
SYD. Y’know… the big one. (indicates crotch area)
NATE. Oh! Uh, have you?
SYD. Nope, Mr. Happy Pants still rises with the sunshine!
NATE. That’s alright, then.
SYD. If only I had something left to work it with. Now what about you? Still got the old frankfurter? (answering
his own question) Naaah, you’re too young to be worried about that.
NATE. (quietly) Actually… it was one of the first things to go.
SYD. Oh Uh.. oh, sorry to hear that son. I’m sure he’s fondly remembered.
NATE. Hey, y’know, it’s just another appendage. (he thinks for a moment) I’ll trade you an arm for yours.

Everything Falls Off
SYD. (covering crotch) Absolutely not.
NATE. I had to try.
SYD. Understandable. So did you enjoy the show today?
NATE. What show?
SYD. The shock show, of course.
NATE. No, watching people get electrocuted to cure a strange disease is not my idea of a good time.
SYD. Oh come on. The faces they make!
NATE. No.
SYD. Yes. Like this (he makes one) or this (another face).
NATE. That is so wrong.
SYD. What about the crazed puppy look? (He makes a strange face with a big wagging tongue)
NATE. That one’s kinda… no!
SYD. Or the wet dog! (he shakes his head vigorously as he is pretend-shocked)
NATE. Well, there was this one…
SYD. Ooh, How’d it go?

(Author’s note: at this point, the two roommates imitate some of the shocked patients. Actors are free to add their own reactions, with accompanying lines to describe them. The only one which must be included is “The Syd.”) SYD. like a bunny (he hops around)? NATE. Bigger! The kangaroo! (he leaps around) SYD. The flaming snake (he slithers). NATE. The robot!

(Does the robot dance) SYD. That’s one from my day. NATE. Oooh, how bout the marathon runner?

(He runs in place, trying to get away from the shocks, which only make him go faster) SYD. There’s facial freak-out.

(He remains motionless and silent while shocked, but his face is contorted in ridiculous ways.) NATE. The fish face too!

(He glubs like a fish while flapping his arms frantically.) SYD. Oh, oh, nothing’s worse than the smoke alarm.

(He makes a one note, very high pitched, very annoying scream while shocked.)

Everything Falls Off NATE. I hate that one. But it’s not as bad as the hyperventilator.

(The patient breathes very very short, rapid, shallow breaths, like a machine gun) SYD. Or the whale!

(He makes one long deep sound while slowly sloshing his body around) NATE. The bursting betty seems pretty bad

(He tenses, and his face slowly grows red and swells. Syd prepares for explosion that never comes.)
But they’re worst when they’re duds.
SYD. You feel so unfulfilled.
NATE. I know!
SYD. Sometimes you get the masochist.

(A macho guy asks for more shocks while growling, etc.) NATE. Or the occasional strangely aroused patient.

(He makes sexual noises while shocked, again asking for more.) SYD. What about the Charleston?

(He does old fashioned dance to the time of the shocks)
NATE. Or the Syd.
SYD. What’s that!?
NATE. (while being shocked) No! Do it to that guy!
SYD. (thinks for a second, then bursts out laughing) It’s funny because it’s true.
NATE. I knew it.
SYD. And it all leads up to the surprise triple brain-burner!

(While being normally shocked, he’s hit by three ridiculous waves of it, shouting strange and hopefully hilarious
things).
NATE. (recovering from laughter) Oh my god, we are so sick.
SYD. We’re losin’ limbs, might as well lose our minds as well!
NATE. Hold up. Does that ever scare you? Cause it scares me.
SYD. What, losing your mind?
NATE. Yeah, I mean… it must be terrible.
SYD. Personally I’d love to see you lose your mind.
NATE. You know what I mean. It’s a frightening thought, sort of a plunge into the unknown.
SYD. Clearly you’ve never been old.
NATE. Oh, you’re not crazy. Just senile and smelly.
SYD. Thanks.

Everything Falls Off

NATE. I hope I don’t go crazy in here. SYD. Funny thing, that is… when you’re losing everything else, your body seems to just work harder to keep your sanity around. NATE. Wow. Isn’t science wonderful? SYD. (ignoring him, going into his own world) Of course, sometimes I feel like I’d be better off if I was insane. Wouldn’t have to put up with the pain, with the rejection, with the loneliness. And I especially wouldn’t have to put up with the roommates. Sometimes, I think I’m just gonna snap. NATE. Uh…. SYD. Yeah, I’m just gonna snap, and I’m gonna get out that big whaling knife I keep under my bed, and creep up on my little roommate… maybe while he’s sleeping, or eating, or whittling, or going to the bathroom, and just go (he acts everything out in the attack and the aftermath) WAPOW! WABAAM! SLLLIIICE!! KAPISSH!!! And he’d go VOOOSH! KADOOM!!! All over the room. Yeah. Sometimes I feel like that, but then I take a couple Advil and I’m good. (looking at Nate again) Hey, you OK? You look a little shaky. NATE. I don’t think I’ll ever be able to take a whiz around you again. SYD. How does that work, y’know, without…? (indicates crotch) NATE. Well, actually it’s quite… hey! None of your business. SYD. Right, right. (pause) So do you have to sit down? NATE. I hate you.

(both look out to the side, as if someone has come in.)
NATE. My turn, huh? There’s always more tests at this place…
SYD. These male nurses love to get you out of your clothes.
NATE. That’s an ugly stereotype, Syd.
SYD. Most of them are pretty repulsive. Except for Victor… he’s… well-built…
NATE. What?
SYD. Nothing. Nothing at all. Good luck.
NATE. Nah, nah, tell me to break a leg. I’m suspicious.
SYD. Break a leg, that’s not bad around here. Lose a leg! (Nate laughs, exits. Syd remains standing. He looks
normal, then something comes over his complexion. He touches his hand to his stomach, as if he has a slight ache.
Then his neck convulses. Then he reacts, as if something is trying to escape from his mouth, but he holds it back.. It
happens again, something of a vomiting motion, and this time a little sound escapes before he can close it off.) Fuh!

(He looks amazed and confused. It happens once more, with a larger build up, and this time it completely escapes, as he says in a large, booming voice:) Four Hours Later! (He shrinks with embarrassment, but his ailment seems to pass. He shakes it off.) Must have been the burritos. Never can tell what dropped into them from whoever’s on slop duty.

(Nate slowly walks in, seemingly exhausted.)

Everything Falls Off

NATE. Hey.
SYD. What’s up, partner. Those nurses still hairy.
NATE. Yeah.
SYD. And did you steal some gauze?
NATE. Sure.
SYD. Hot damn, I’m gonna make me some new curtains. What color you want, roomie?
NATE. Syd.
SYD. Ok. It’s something you should think about.
NATE. Syd, it’s getting a lot worse.
SYD. You.. what? (making an unsure guess) Oh… oh, you mean, living here. It’s a tough one, bucko, but things’ll
get better.
NATE. No, I wish… I want to keep living here.
SYD. Well… why?
NATE. They’re transferring me to the hospital on the main island tomorrow. Like I said – it’s a lot worse.
SYD. Oh. (pause as he searches for something appropriate to say) But you’re the first roommate I liked!
NATE. But I don’t really belong as your roommate.
SYD. Why not?
NATE. I don’t have leprosy.
SYD. What? Not a single bit?
NATE. Sorry, buddy. I was misdiagnosed.
SYD. You’re a faker!
NATE. No, Syd…
SYD. You are! You cut off your parts! You’re a big faker! You even…
NATE. I didn’t!
SYD. You cut off Mr. Winky! You big fake! Fake Fake Fake!
NATE. Be reasonable.
SYD. You’re a faker, just like my ex-wife. She had me fooled for years! Fakey!
NATE. Won’t you listen, Syd?

Everything Falls Off
SYD. I can’t! I’m too busy doing the fake dance! (he does the dance)
NATE. SYD! I am infected. I do have a disease.
SYD. Well what is it? Stupid ugly liar’s disease?
NATE. No, actually, it’s Ebola.
SYD. (stops dance) Oh. Crap.
NATE. I know.
SYD. I have it to now, don’t I?
NATE. No, we’d have to kiss, or do intravenous drugs together.
SYD. I think I touched you, once.
NATE. That’s ok. You just can’t touch any of my slushy parts.
SYD. Rrrrr.
NATE. It’s ok. You can do the Ebola dance.
SYD. I can’t do the Ebola dance, Nate.
NATE. Why not?
SYD. Because I’d have to dissolve onto the floor and run down the little drain!
NATE. Syd, that’s mean.
SYD. Well they don’t have the drain for nothing now, do they?
NATE. Ugh.
SYD. Don’t give me that look. I’m not going to die for you.
NATE. What?
SYD. Oh that’s what you want, I’m old, I’m supposed to sympathize with you and magically cure you, or die with
you to make you feel less alone, or something stupid like that. Let’s hold hands and plunge into the abyss together!
Oh goody!
NATE. Uh, that’s crazy.
SYD. No. I can’t do anything. Why did you even come back to the room?
NATE. Jesus. I thought you would like to know.
SYD. Could have just sent for your bags. I would have assumed you were dead.
NATE. You would want to find out that way?!
SYD. It wouldn’t surprise me.

Everything Falls Off
NATE. You’re a cold bastard.
SYD. You first.
NATE. Hey!
SYD. Fine. I’m sorry. But what am I supposed to do. Pretend it’s ok?
NATE. Sure!
SYD. Alright, suggest something.
NATE. Let’s pretend we’re madly in love.
SYD. For all that’s good and holy, why?
NATE. So we feel happy and special.
SYD. That’s crazy.
NATE. You always wanted to try crazy.
SYD. Alright.
NATE. Alright. Syd.
SYD. What?
NATE. I love you baby?
SYD. What?!
NATE. C’mon!
SYD. I, uh… (trying hard) I’m gay and I love you! My… lump of sweet man-sugar.
NATE. I love you too… (they touch awkwardly.) But wait. I don’t have a… y’know. Thingamadoozle. A dong.
SYD. That’s ok, we’ll share mine.
NATE. Oh, stumpy!
SYD. Scabface! (they touch again.)
NATE. Well, that was fun, but I’m still depressed. And I smell like old person.
SYD. It’s a fine scent. Like aged wine.
NATE. Let’s not get off the subject.
SYD. Then try again.
NATE. Ok, uh… Good news! I’m not dying of leprosy.
SYD. I knew that. That’s why you suck.

Everything Falls Off
NATE. I mean, not leprosy or Ebola.
SYD. Oh?!
NATE. No, I’m dying of syphilis!
SYD. …Ok. No.
NATE. Crabs?
SYD. You can die of crabs?
NATE. They’re big crabs. … I dunno. This is hard.
SYD. Don’t complain to me. I don’t know what to do.
NATE. I know, Syd, I know.
SYD. Hah.
NATE. Fine.
SYD. Fine what?
NATE. We’ll just sit here.
SYD. Ok.

(they sit)
SYD. And do what?
NATE. And wait for me to die!
SYD. Hmmph.

(more waiting. Slowly, Syd gets up and starts to poke Nate) NATE. Not yet, moron. I’ll let you know. SYD. Oh. Hmmph. (he sits again).

(There is a long pause).
SYD. Now how are you gonna tell me when you’re dead?
NATE. Just lay off me for once, will you?
SYD. I’ve only been laying into you for a day.
NATE. Well it was enough!
SYD. Oh. (a pause) Am I really that bad?
NATE. I don’t know. I guess you are.

Everything Falls Off SYD. Well then. NATE. Now shut up and let me rot in peace. SYD. No! If I’m going to be a bastard, I’m going to be one all the way to the grave! NATE. Yeah? SYD. Yeah! To your grave! NATE. Whoa. SYD. You no good lying sack of putrid llama dung, you come in here with your fancy shoes and imported diseases and you think you can just tango all up and down the place, like you’re the king of the limb pile. Well let me tell you something, we earned those limbs, not by shocks or drugs but through pure hard loss. I lost everything first, then I lost those limbs. Those limbs were like the afterthought. They’re what the demons take to hell. But I left everything here. A wife, a kid, parents that needed my support. That’s all gone. I watched it rot away, my life and what was important to me. And if there’s not a stinking piece of me left to be compassionate after I lost all of that, well it’s not my problem anymore. And you, you come in here, Mr. pimpy poop shoes, NATE. (quietly) What is this obsession with my shoes? SYD. And you try and become my friend, and heal my pour leper soul. Well let me tell you it worked, and now that soul is back just a little, and it is not ready to be lost again. I am not ready to be lost again. So I’m mad, I’m mad at you. And when I’m mad, I’m a rat bastard. So you better be ready for it. NATE. Syd. SYD. Are you ready for it? NATE. Yeah, I am.

(They embrace.)

CURTAIN
```

---

## IC-1037: Florida Mae Tuesday's Second 6th Birthday

- Title: Florida Mae Tuesday's Second 6th Birthday
- Author (byline): Frank Smith
- Work: Florida Mae Tuesday's Second 6th Birthday
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 3906
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
Florida Mae Tuesday’s

th Second 6 Birthday

A One-Act Play

Written by Frank Smith

SCENE I

The Tuesday Mansion – Porch.

(A gorgeous home – or it would be, were the lawn ornaments not so…crazy-eyed.)

CAREY, PHIL, TENNESSEE.

(CAREY FULLER (36), permanent case of “God help me” face, stands just outside the door with
his son, PHIL FULLER (8), thoughtful, sweet. Carey looks at the bull-shaped knocker like he’s
entering the gates of hell.)
CAREY. Phil, if you’re not having fun, we can just go.
PHIL. Dad, if you’re not having fun, we can just go.
CAREY. No, I’m the parent. I have to pretend like I’m enjoying myself even when I’m not.
PHIL. That’s true.
CAREY. And hey, one day, you’ll be doing it for your son.
PHIL. Or maybe I can take him places we both want to go?
CAREY. What a delusional optimist I’m raising. (He steels himself before finally knocking at the
door.) How old is Florida Mae turning again?
PHIL. Seven.
CAREY. Oh. I thought the invitation said six.
PHIL. It’s her second 6th Birthday.
CAREY. Not to be confused with her first 6th Birthday?
PHIL. No. Remember that baseball game last year, when that kid threw his bat, and it hit her in
the face, and she went into a coma, and the kid cried because he felt bad putting her in a coma?
CAREY. Hazily.
PHIL. So she was in a coma on her actual 6th Birthday. And that’s why it didn’t count.
CAREY. Of course. Via The Law of Unconscious Birthdays. I honestly forgot that she got hurt.
PHIL. Well, I guess it was right around the time that Mom was…sorry.
CAREY. Buddy, you don’t have to be sorry.
PHIL. So…wait. We can start talking about her again?

CAREY. We never stopped, it’s just…easier sometimes when you don’t—

(The front door opens wide to reveal TENNESSEE TUESDAY (32), thick Southern accent for a thick Southern gentleman.) TENNESSEE. If it isn’t Carey and Phil Fuller! Florida Mae can’t wait to see the two of you. CAREY. I mean, my son, obviously, he’s outstanding, but…why can’t she wait to see me? TENNESSEE. Why, because she’s sweet on you, of course! Why else would she refer to you as “the Silverest of Foxes.” CAREY. Your daughter knows the word, “Silver Fox?” TENNESSEE. Okay, I might have taught it to her, but only because it’s what her heart implied! So maybe when you go in, you can say she looks pretty in her red dress, really make her day. CAREY. I’d be happy to. TENNESSEE. She may also ask if she can marry you. Just say yes! That’d really make her day. CAREY. I don’t know about that, Tennessee. TENNESSEE. Ah, you’ll come around. We’ll just have to get you a drink first. CAREY. That is a disturbing plan of action. TENNESSEE. All right, enough chatting on the porch, come on in, you two! I assume your present is a gift certificate because I don’t see any big bags or animal cages, which is fine! Because cash is king, and I’ve had to replace too many ferrets this month anyway. (Gravely.) Florida Mae has not been very forgiving of all the stealing.

SCENE II

The Tuesday Mansion – Kitchen.

(Even in this room…there’s taxidermy. Spaghetti cools in several colanders in the sink.)

TENNESSEE, PHIL, CAREY, FLORIDA MAE.
TENNESSEE. You’ll never guess what the theme of the party is. Spaghetti!
PHIL. I love spaghetti!
TENNESSEE. Of course you do. Everyone does! (Wistful.) Even the ferrets. Poor things never
saw that can opener coming.

CAREY. (Pulling a gift card out of his coat.) So here’s Florida Mae’s present. Sorry if it seems small and not thought-out, it’s just, Joy was the one who used to be on top of this kind of thing… TENNESSEE. Now, don’t you worry your pretty little head. You’re only here to have yourself a good time – so I don’t want to hear any more talk about your beautiful dead wife, you got it? CAREY. Umm…no problem? TENNESSEE. Attaboy.

(FLORIDA MAE TUESDAY (7), good-hearted girl whose mania is too young to be diagnosable, races in wearing a Birthday tiara and wielding a Birthday scepter.) FLORIDA MAE. Well golly me, if it isn’t my good pal Phil! (She gives him a big hug before laying eyes on Carey. She bows to him.) Sir: I do declare, if I ever drink tea half as sweet as you, I’ll have had enough sugar to last me a lifetime. And! You’re so…powerful…like a mountain. TENNESSEE. (Sotto, to Carey.) What did I tell you? CAREY. Happy 7th…I mean, not your 6th…Birthday, Florida Mae. FLORIDA MAE. Thank you, darling! (Sidling up to him.) How can I ever repay such kindness? CAREY. You…and my son…can go off and have fun together. FLORIDA. Aww, and leave you all by your lonesome!? TENNESSEE. Now now, it’s for the best. We do need to get this pasta lunch ready, sweetheart. (Leading.) But before you hunker off…I think Carey had something to say about your dress? CAREY. It’s…red.

(Florida Mae SCREAMS with delight. Seriously, she looks happy enough to pass out.) TENNESSEE. All right girl, calm down, he didn’t go back in time and win the war for you. CAREY. Which war are we talking…? TENNESSEE. Go on, skedaddle. Mr. Fuller and I are going to have us some adult talk. FLORIDA MAE. And we’ll have us some sweet little baby talk!

(Florida Mae takes Phil by the hand as they leave the kitchen.) TENNESSEE. Now, Carey, I know I said not to bring down the mood with all that talk about your lovely deceased spouse…

CAREY. Yes. Almost threateningly. TENNESSEE. But that’s because you owe it to yourself to move on. Been over a year now, as I recall? Long time not to be in…the swing of things. Know what I’m saying? Yeah. You do. And that is why…I have rounded up a cadre of genuine, gorgeous females so you can pick a rebound! CAREY. Tennessee, you really don’t have to— TENNESSEE. Too late. Already did! CAREY. (Concerned.) Please tell me one of them’s not your 6-year-old daughter. TENNESSEE. Quit talking nonsense, boy. Florida Mae is 7!

SCENE III

The Tuesday Mansion – Living Room.

(Kids run around and play in this ode to Southern comfort.)

TROY, FLORIDA MAE, PHIL, RAYNA.

(TROY BOZEMAN (7), chubby red cheeks like a squirrel, intercepts Florida Mae as she takes
Phil into the room.)
TROY. Florida Mae, when’s lunch? I’m starving!
FLORIDA MAE. Troy Bozeman, I swear, if your appetite were any bigger, it’d be Texas.
TROY. (Sarcastic.) Oh, you’re from Texas? I had no idea!
FLORIDA MAE. Mercy me. Someone’s hangry.
PHIL. Wait, if you’re from Texas, why is your name Florida?
FLORIDA. Oh my goodness, Phil, you can’t just ask someone why they’re not from Florida!
Geez Louise. Anyway, let’s talk about you. How you been living?
PHIL. Well, I—
FLORIDA MAE. Mmhmm mmhmm. And how’s your Daddy?
PHIL. He’s all right, I guess. Seems to finally be over my Mom.
FLORIDA MAE. Oh reallyyyyyy. Over her, you sayyyyy.
PHIL. I mean, he never really talks about her anymore.

FLORIDA MAE. Well, isn’t that good? It’s been a year now, right? I measure time by the number of days since I got concussed by that old baseball bat. TROY. I said I was sorry! FLORIDA MAE. Sweet pea, you should’ve seen the dent in that bat! Now IT was sorry. (Darkly.) Just like the ferrets after they took my artisanal candles. (Sweetly.) Besides, your Momma was gettin’ old when she died. I think your Daddy would fancy himself a younger gal these days, don’t you? PHIL. Maybe. And I’d be okay with that. Just as long as he stops acting like Mom never existed. All her pictures are gone. He gave away all her clothes. He doesn’t even talk to my Aunt Cora. Well, that was true before Mom died, too. He says being trapped in a room with just her is like being a victim of the “Salem Bitch Trials.” But Mom said he was wrong about her. It was more like being at an “All You Can Bitch Buffet.”

(RAYNA LETTS (8), sincere to the point of being painful, walks over to the group, intrigued by
this line of conversation.)
RAYNA. Hey, Phil. It’s Rayna. From third grade. While I’ve never had a parent die, exactly, one
time, my Mom did say I was an “accident. But a good one. Like when you get rear-ended and
they pay for it. Actually, it was exactly like that.”
PHIL. Thanks, Rayna. That’s…kind of on-topic?
RAYNA. Kind of I think!
TROY. When are we having spaghetti already!? I’m seeing mirages, but with red sauce.
FLORIDA MAE. Troy, do you ever talk about anything but food?
PHIL. Why would he? He loves it. (Realizing.) Do you think that’s why my Dad doesn’t talk
about my Mom anymore? He stopped loving her once she died?
FLORIDA. Yay hooray for me! Aww, but sad for you. But yay hooray for me!
TROY. Now I’m sangry. Sad, and hungry.
PHIL. I hope I’m wrong. And he does still love her.
FLORIDA MAE. (Sarcastic.) Why…because she isn’t dead yet!?
PHIL. (Sincerely.) I don’t know. Maybe.
RAYNA. But if she isn’t dead, then what would she be…undead?

PHIL. (Won over.) Exactly! FLORIDA MAE. Crap. Now if I want to be your Daddy’s sweetheart, I gotta go stab a zombie through the head? Guess I better find that can opener again.

SCENE IV

The Tuesday Mansion – Kitchen.

TENNESSEE, CAREY, RHONDA, BEVERLY.
TENNESSEE. Now let me introduce you to your first eligible bachelorette.
CAREY. Look, you don’t have to do this, single and sad is actually a pretty good look on me—
TENNESSEE. Rhonda, this is the guy I told you about. With the gorgeous six feet under spouse?
You two mingle. I’m gonna put the meatballs in the spaghetti.
CAREY. Is there a vegetarian or vegan option?
TENNESSEE. What are those two hate-words you just said?

(RHONDA SIMMS (36), too calm to not be insane, puts her hand out for Phil to shake.) RHONDA. Tennessee, leave us alone already! Hi there! It’s Rhonda. My husband’s gone too. CAREY. Carey. And I’m sorry to hear that. TENNESSEE. Oh, not gone gone, like your stunning sleeping with the fishes lover. RHONDA. Tennessee! Let the magic happen. (He goes.) He’s right, though. I am divorced. CAREY. Oh, well, I’m still sorry. RHONDA. Honestly? So am I. In divorce, you only get half the assets. But if he dies, you get all of them! CAREY. That is…true, from personal experience. RHONDA. Oh sorry, that’s so insensitive of me. It’s just, you know, lawyers…ugh. He was in great health, though, my ex. He would never have just…died. I would have had to kill him. CAREY. Oh, umm, that sounds, dangerous. For both of you. RHONDA. Not really. He liked to fall asleep with cigarettes in his mouth. I could’ve burned the house to cinders and gotten away with it.

CAREY. You…never would have done that, though. RHONDA. No. I loved that house. CAREY. But…also, because you have children. Right? RHONDA. Well, obviously I would have made sure the kids were out of the house when I did it. Hired a babysitter, given them an alibi. And even on the off-chance I actually did get caught, if I had to do it all over again? I would still choose murder over divorce. The trial is much shorter. CAREY. (Concerned.) Tennessee. Tennessee!? Need me to cook meat or something? Please!? TENNESSEE. (He comes back over.) All right, scoot, Rhonda, clearly, Mr. Fuller ain’t buying what you’re giving away on clearance.

(Rhonda walks away. Another woman walks up to Carey: BEVERLY GORK (32), fighting through her sad to be strong and caring.) BEVERLY. Hello. I’m Beverly. CAREY. Carey. TENNESSEE. Now you and Bev actually have a lot in common. She also has a fit dead as a doornail, deader than disco, deadest possible dead-iddy-dead-dead life partner. (He goes again.) CAREY. I’m so sorry…that you had to hear that. And that your husband is gone. BEVERLY. Thank you. It was so sudden. CAREY. Same here. BEVERLY. It’s been almost a year, but…I don’t know. Some days I’m still surprised that he doesn’t sit down with me for dinner. He hated my cooking, but never left a bite on his plate. That’s love. Or masochism. Maybe both. CAREY. I totally know what you mean. I see Joy, in crowds, sometimes. I thought that was just a thing people said to get onto a reality show for psychics, but it’s true. BEVERLY. You know, for me, what’s hardest is my little girl. I never know what the right amount to talk about her Dad is. CAREY. (Touched.) Wow. Uh, yeah. Me neither.

TENNESSEE. (He returns.) Okay, WOW, is this depressing, or what? What’s worse than two grieving widows in the same room? Literally nothing! Truthfully, I think I’ve had bowel movements that were more exciting than this. Some really exciting ones, actually. Suspenseful, even. Okay, Bev, you move it along now, I’ve got more single ladies to show Mr. Fuller. CAREY. No, Tennessee, I don’t want to meet more women… TENNESSEE. Why, boy? You’d rather meet men? CAREY. No? TENNESSEE. Good. Since I don’t know many queers. But I’m open to meeting some!

(Clarifying.) For you.

SCENE V

The Tuesday Mansion – Living Room.

PHIL, TROY, FLORIDA MAE, RAYNA. PHIL. What do undead Moms eat, anyway? Brains, same as everyone else? TROY. Gross! No, I should be more open-minded. I’ve never tried brains. Just goat liver. FLORIDA MAE. (Viciously.) Ferret’s better. PHIL. If I want to keep my Mom alive…I need to keep feeding her brains. RAYNA. Phil, I may have never had a dead zombie Mom before, but one time, my Dad didn’t get much sleep, and was very grouchy with me. He said he regretted “having me with my Mom, and even more than that, doing the right thing by staying.” PHIL. Although, what is the right thing in this case? Keeping my Mom alive? Or protecting her future victims from her? There’s a lot of moral relativism at play here. FLORIDA MAE. Maybe your Momma’s not undead after all. Maybe she’s just one of them there immortals. Oh phooey. Now I really won’t stand a chance with your Daddy! (Realizing.) Uh-oh. Quick question. Can certain animals be undead too? Like, I don’t knowwwww, for the sake of a completely random example…somewhere between three to five ferrets? PHIL. Probably? I’d sleep with a weapon. (Determined.) But you guys. I think I need to go find my undead Mom some brains to eat. FLORIDA MAE. Not mine. Take Troy’s! He barely uses his. He’s more of a…gut kind of man. TROY. I trust my instincts. And my instincts say… (Scared.) please don’t feed me to your Mom!

PHIL. I won’t! I promise. No pinky, though. Look, the undead aren’t always the smartest, right? So maybe I can just feed her something that looks like brains. RAYNA. Do you know what brains look like? I’ve only ever seen an exposed kneecap, when my Dad shot out my Mom’s, saying, “This is literally what you do to me metaphorically.” FLORIDA MAE. Rayna, your family’s nuttier than a pecan pie made by squirrels! RAYNA. That’s what grandma said! Before she got shot too. By the mailman. Who looked an awful lot like me, now that I’m thinking about it. TROY. Is it weird that all this talk of senseless violence is making me famished? PHIL. Just imagine being my Mom – she hasn’t eaten in a year! FLORIDA MAE. It’s called a diet, boy, all us females have to try it out at some point. Let’s go!

SCENE VI

The Tuesday Mansion – Kitchen. TENNESSEE, CAREY, SADIE ELLEN, PHIL, FLORIDA MAE, TROY, RAYNA,BEVERLY. TENNESSEE. Fine! One more dame, then you can commit to a lifetime of loneliness and pills. CAREY. Thank you.

(SADIE ELLEN (29), sweet but still mischievous, joins the pair.) TENNESSEE. Now, this one, I’m surprised you haven’t met yet, because she’s definitely my favorite. Here’s good ol’ Sadie Ellen. Sadie, Mr. Fuller is the guy I mentioned earlier, you know, the one with the total-knockout worm-food ride-or-die? SADIE ELLEN. Oh, I remember. CAREY. He makes it impossible to forget. SADIE ELLEN. Salutations, gorgeous. CAREY. (Realizing.) Wait, Tennessee…this isn’t…hold on a sec…is Sadie Ellen your wife!? TENNESSEE. Sure is! SADIE ELLEN. We have one of those, what do you call them… “open relationships.” And I don’t want you to think that this is just a pity date because you’re a widower. I genuinely…want you. Grief is just a fine, fine look on some men. And you’re one of them, Mr. Sad-Sexy-Eyes.

CAREY. Yikes. Tennessee, is this really better than being single forever? TENNESSEE. She was for me! CAREY. Okay, enough. I have entertained this…borderline-predatory match game for way too long. I think I’m just going to grab Phil and leave. TENNESSEE. Oh, so because you’re having a bad time, your son has to suffer along with you? CAREY. Uh, what does that mean? TENNESSEE. It means…Carey. I know you a bit better than you might think. You used to be real fun, and spontaneous…maybe even a little “suggestive.” Now, you just come to things, and go from things. You make no effort to mingle, or get to know anyone. But you’re still…here. And you need to act like it. CAREY. Tennessee, what are you implying, exactly? TENNESSEE. I’m stating outright…that the way you are is starting to affect your family. We’ve all seen it. You hold on a little too tight, are a little too careful with the things you say. BEVERLY. (Pokes her head in.) And I know the feeling. Since Harry died, I always feel like I’m walking on eggshells around my… TENNESSEE. Oh my LORD, Beverly, you could bring down the mood at a candlelight vigil! Would you give me and Mr. Fuller a minute already!? CAREY. Go easy on her, Tennessee, we’re both still grieving. TENNESSEE. Carey. You think I haven’t suffered loss, or very nearly close to it? You know what I did, after Florida Mae hit her head last year? Sent her right back onto the baseball field. Not literally right after, I waited till she was out of the wheelchair, but…and you know why I did that!? Because when you fall off the horse…only solution is to get right back on. And unlike most people who use that phrase, I’ve actually ridden horses – even lady-ones! So I surely know what I’m talking about. CAREY. But Florida Mae survived. Plus, you were the one telling me not to talk about Joy! TENNESSEE. At parties, Carey. There’s a time and place for everything. And here, at this party, it’s about letting your son forget about his sad Dad, and his dead Mom, just for a minute…and helping him have fun.

(On cue, Phil, Florida Mae, Troy, and Rayna race into the kitchen, hunting for spaghetti.) PHIL. Out of the way, out of the way! I’ve got to get brain-food for my Mom-bie!!!

CAREY. What?
FLORIDA MAE. (To Carey.) Grab all the pasta you can now, sweet thing! The more red sauce,
the better. Wouldn’t want your old lady to get in the way of your new one!
TROY. Can I have some of the leftovers?

(The kids throw all the spaghetti they find into a pile on the floor.) TENNESSEE. Now what in the perfect paradise is going on around here!? FLORIDA MAE. (Rapid-fire.) Phil’s Mom is one of the walking dead and we need to feed her spaghetti because it looks like brains and oh my goodness me why aren’t you helping out yet!? CAREY. Excuse me. Hold on a second. You think my wife is undead? RAYNA. Mr. Fuller, I’ve never had an undead bride before, but I did marry my Teddy Bear after we both had had too much tea, and he doesn’t talk to me anymore, so it’s like he’s a zombie. Also, I’m pretty sure my Mom put a camera in him. That’s okay. It’s nice to be watched sometimes. It means people care about you! FLORIDA MAE. Rayna, girl, you gotta get a legal emancipation, like, yesterday, but for now: focus on the task at hand! RAYNA. (Grabbing a jar off the counter.) Okay, I found sauce! Oh, boo. It’s Alfredo. TROY. Ooh, let me have some!

(Rayna pours some sauce into Troy’s mouth.) TROY. (Mouth full.) You’re a queen. Keep it going.

(Rayna pours more sauce into Troy’s mouth before dumping the rest on the floor.) TENNESSEE. Can someone just explain to me, slowly, what is happening right here right now? PHIL. We think my Mom’s a zombie. TENNESSEE. Aww, that’s adorable. PHIL. No, it’s deadly! I saw how my Dad wasn’t talking about my Mom. But it’s not because he doesn’t care about her. It’s because she’s still alive, in…some shape or form. Right, Dad? CAREY. Buddy…buddy, no. PHIL. So you wouldn’t rather have a flesh-eating wife than no wife at all?

TENNESSEE. Well, a little nibble never hurt nobody, but— CAREY. Phil. I don’t talk about your Mom because…I don’t want to reopen an old wound. PHIL. Mom isn’t a wound, Dad. Even if her skin is mostly lesions now. CAREY. It’s really not. Your Mom may not be here with us, but trust me, I won’t forget her. I just don’t like to make you, and me, sadder than we already are by bringing her up all the time. PHIL. But I’m sadder when you don’t say anything at all. I like remembering Mom. She was great. (Sadly.) We loved her. CAREY. (Tearing up.) Yeah. We do, buddy. FLORIDA MAE. Well, it’s plain to see there is no hope for me with you anymore. Now I’m sad. Ooh, I know! Rayna, come with me, let’s go hunting in the backyard for ferrets. TROY. I’m almost hungry enough to eat one! FLORIDA MAE. Heyyyyy, now that could be real fun for me to watch! RAYNA. I actually have had a dead pet before. Well, not so much a pet, as a baby sister, but—

(Florida Mae, Troy, and Rayna leave the kitchen, as Beverly slides in.) CAREY. You know what, Phil? I don’t know if this would be interesting to you at all, but I actually did keep a handful of photos of Mom, just in case I regretted getting rid of the rest of them. Would you want to maybe…put those up with me when we get home? PHIL. Yeah. Yeah, Dad. I really would. SADIE ELLEN. I am getting so damn emotional over here! (Seductively.) Tennessee. You want to head upstairs and…do something with that? TENNESSEE. Carey – last call! No? Okay, just us. Have fun reminiscing about your perfect 10

(Pantomimes a graphic death.) soulmate! (Tennessee and Sadie Ellen holding hands / butts.) CAREY. Phil, you want to say goodbye to your friends, so we can take off? PHIL. Sure, Dad. Hey, listen…I’m really glad you’re still alive. But even if you were un-alive, I would totally come and feed you, no matter how many innocent lives it cost. (He runs off.) CAREY. Back at you, buddy.

BEVERLY. Carey. I’m about to head out too, but I just wanted you to know – I’m really glad I
got to meet you today. It’s nice to finally talk to someone who knows what you’re going through.
Not that being a widow 100% defines my whole personality, but I guess today, it kind of did!
CAREY. Same!
BEVERLY. Seriously, though: Joy sounds…great.
CAREY. She was. Maybe sometime we can get a coffee and…I can tell you more about her?
And you can tell me a little bit more about Harry?
BEVERLY. I’d love that.
CAREY. Well then, I guess we proved the old adage true: misery loves company.
TENNESSEE. (From upstairs.) That’s the spirit!
SADIE ELLEN. (From upstairs.) Loss is nature’s aphrodisiac.
CAREY. Wow. Those two are crazy in love. Moreso crazy than in love.
BEVERLY. I’m looking forward to going crazy again someday.
CARL. Me too.
TENNESSE. (From upstairs.) But don’t go moving too fast, Carey!
SADIE ELLEN. (From upstairs.) Yeah, you know, just because her husband died, doesn’t mean
she’s a good person!
CAREY. (Shouting upstairs.) Goodbye, Tennessee! Thanks for everything.
BEVERLY. (Shouting upstairs.) Great party, minus all the weird parts!
CAREY. Yeah. It really was. Weird. (Sincerely, to himself.) Welp. Happy Second 6th Birthday,
Florida Mae.

THE END.
```

---

## IC-1038: Front Porch Chronicles

- Title: Front Porch Chronicles
- Author (byline): Sidney Ryan
- Work: Front Porch Chronicles
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: BOBBY, SAM
- Teaser before the introduction: No
- Spoken words (computed): 1348
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
FRONT PORCH CHRONICLES

BOBBY: Every morning for the last 50 years I have stood here on my stoop with my neighbor Sam Jones and watched as the nighttime became the morning. From this stoop, we'd grab our pails, walk down the street to the factory and be home by six to have dinner with the Mrs. and homework with the kids. Now my boys live in the city, and my wife passed a year ago today, and a new family is moving in house next door. Life is changing…I’m not sure that I’m ready for where it’s going.



SAM: Hi Mister.

BOBBY: Who are you?

SAM: I’m Bobby Lantzy. I’m your neighbor. Who are you?

BOBBY: I’m the mean old grump who doesn’t want to talk to you…don’t you have a box to move or something?

SAM: No. I’m not allowed to help. I keep breaking things.

BOBBY: Well, you’re breaking things here too. My silence. So go play in the street or something….see how many cars you can dodge.

SAM: What's that?

SAM: What's this? Is this a pirate ship?

BOBBY: Don’t' touch that. It is a rare antique…took me five years to put that together.

SAM: Where'd it come from?

BOBBY: Where'd it come from? Why do you…..(thinking)….well, I got it when I was a boy and I lived on a pirate ship….

SAM: Really? I’d like to live on a pirate ship. INTRO

SAM: Mr. Grump, tell me one of your stories.

BOBBY: Arrgghhh there boy. What are ye bloody doin?

SAM: I’m swabbing the deck captain.

BOBBY: Yere doin a bad job, Ill toss ya overboard!

SAM: Look captain, a ship!

BOBBY: Argh…set sail, it's a British ship…she's probly full of treasure…Set sails, man the guns!

SAM: Captain, they’re twice our size.

BOBBY: Aye, but where there be size there be lots of gold.

SAM: Did you get the gold Mr. Grump?

BOBBY: Mr. Grump?

SAM: Yea, you said you were old Mr. Grump?

BOBBY: Haha…so I did. Sure we got the gold, but then another pirate ship came and took it away.

SAM: Wow, that's cool.



BOBBY: I try everything to get rid of this kid…so I started playin these games with him…plays sort of…they make me laugh… But he’ll get bored and stop comin round soon…they all do. I remember we would sit….



SAM: Mr. Grump…well that’s what I called him, was this really cool old guy who lived next door to me when I was growing up. I didn’t really have a lot of friends in my neighborhood. I was really small and not much of a cool kid.

BOBBY: And then he would leave me.

SAM: So I use to sit on his porch and play games. I’m not sure what else I would have done growin’ up without him

BOBBY: And I haven’t had a friend like that since.



SAM: Mr. Grump! Its my first day of school..

BOBBY: I can see that

SAM: Im getting on the school bus today. The school bus!

BOBBY: Well, you better buckle up.

SAM: Im afraid that the big kids are gonna pick on me though.

BOBBY: Here…take this.

SAM: What is it?

BOBBY: It’s a magic laser gun.

SAM: It looks like a pen…see I can

BOBBY: DON’T PUSH THAT BUTTON!

SAM: Why not?

BOBBY: That is the trigger. If you point that at somebody, you’ll vaporize them.

SAM: Wow (holds it away) Where did you get this?

BOBBY: I got it when I was an astronaut on a secret trip to the moon.

SAM: You were an astronaut?

SAM: This is mission control. How ya doin’ out there, Grump?

BOBBY: I’m doing fine. I can see the moon. It looks like a big wheel of cheese. Lots of holes. Ok I've landed. I’m' stepping out of the ship.

SAM: You stepped out of the ship?

BOBBY: SHUT UP, YOU'LL RUIN THE STORY!

SAM: Sorry

BOBBY: This is one small step for man, one giant leap for mankind.

SAM: Wow. You are the one who said that?

BOBBY: Yep, but the first mission was top secret, so Armstrong repeated it the next time.

SAM: Wow. I’m gonna cross out his name in my social studies book and write yours.



BOBBY: Sometimes I just wish the good Lord would take me…at least somebody would want me then.



SAM: Sometimes I would go over and Mr. Grump would seem kind of out-of-it. Maybe he was just
getting old. My mom told me to stop bothering him so much.



SAM: You sure have a big house, Mr. Grump!

BOBBY: It’s no bigger than yours.

SAM: Yea but I have five people living in mine. Do you live here all by yourself?

BOBBY: I do.

SAM: That must be cool!

BOBBY: Yea, sure is…

SAM: Mr. Grump…how come you have all those little bottles on the table?

BOBBY: You sure do ask too many questions…

SAM: That’s what my mom tells me…

BOBBY: Listen…I think you’d best get home. Ain’t it time for dinner or something?

SAM: In a little while. My mom will start screaming out the door…”Bobby! Bobby! Like that…she says, “Bobby, it’s time for…”

BOBBY: I KNOW! I know. I’ve heard her… Now I have something I need to do…

SAM: Don’t you have to drink water with those pills. My mom always takes her medicine with water. My dad though is so cool, he can take his dry. We just got a lot of this really neat bottled water…its kinda’ like soda, but not…can I get you….

BOBBY: NO! (clear throat) No. I’m fine.

SAM: So does your house have an attic? Mine has an attic, but I’m not allowed in it.

BOBBY: Yes, I have an attic.

SAM: I saw a TV show where a little boy made a fort in his attic with his friends, but I don’t really have any friends to make a fort with…maybe you can take me in yours someday and we can build a fort?

BOBBY: (Cough or something)

SAM: Mr. Grump, do you ever get lonely?

BOBBY: Lonely…I don’t have time for lonely.

SAM: You know what I do when I get lonely?

BOBBY: What’s that?

SAM: I come over here!



SAM: Mr. Grump’s gonna love my new girlfriend. I think. I hope. Oh God. He’s gonna hate her.



SAM: Mr. Grump.

BOBBY: Wow. Look at you all snazzed up. Where are you going?

SAM: It’s my first date…how do I look?

BOBBY: You look clean. You look dressed.

SAM: Come on. How do I look?

BOBBY: Like a secret agent.

SAM: My name is Mr. Golden Leg, and you are?

BOBBY: Grump, Forrest Grump.

SAM: Well then Grump, what can I help you with?

BOBBY: I’m here to stop you from poisoning all the trees on Earth, Golden Leg.

SAM: Not today Grump…it's too late. I have already taken over this park…and you can’t stop me from taking over the world.

BOBBY: Bang.

SAM: Bang. Bang !

BOBBY: Bang Bang Bang Bang Bang! ….wow, I haven’t banged like that in a long time.



BOBBY: Seems like there’s all sorts of boxes over there today…getting packed in the car. I knew it was gonna’ happen… goin’ off to school --- they all do.



SAM: I’m leaving. He’s probably not even gonna know I’m gone. He’s probably gonna like the peace and quiet….



SAM: Mr. Grump, I’m leavin’ for college today. Everything is packed.

BOBBY: Cough, Cough, Ok goodbye boy.

SAM: Ok. Bye.

BOBBY: Franks.

SAM: What?

BOBBY: Sam Franks. My name is Sam Franks…

SAM: I brought you something….to give you…to remember me…

BOBBY: What is this? A coin. Boy, I aint needing any money.

SAM: It’s not just any coin Mr. Grump….it’s a window…to me.

BOBBY: A window.

SAM: That way every time you are lonely you can look through that window and see me, and every time I am lonely, I can see you.

BOBBY: Well, Ill be. I can see you right there…right there! (wave at coin).

SAM: I gotta go Mr. Grump.

BOBBY: And I remember we would sit on my porch and play games and they made me laugh.

SAM: Bang! Bang! Bang!

BOBBY: But then his mom would call and he would leave me.

SAM: Bobby! Get in here Bobby!

BOBBY: And then I would get lonely and I realized I really did miss him.

SAM: This is mission control, how ya doin’ out there?

BOBBY: And now I spend my nights talking to a coin. And I just sit all alone on my porch in my rocker and just think that I haven’t had a friend like that since.

End.
```

---

## IC-1039: The Hamilton Sasquatch

- Title: The Hamilton Sasquatch
- Author (byline): Jeffrey Longval and Kagan Hatch
- Work: The Hamilton Sasquatch
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: SCENE 3 - DAY
- Teaser before the introduction: No
- Spoken words (computed): 1748
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
SCENE 1 - EVENING

Thomas and Liana are walking through a

secluded area of Hamilton’s local

forestry.

THOMAS Liana, you need to keep your eyes closed.

LIANA Oh, Thomas, I reserve myself the right to at least know where I am.

THOMAS Don’t you oh Thomas me missy. Hey come back here you! We’re here. One, two, three...

LIANA Look? Thomas, it’s, it’s…

THOMAS Beautiful? I know, this is my favorite area of the forestry because you have a Generic Eucalyptus on the left, African Maple back in this northern region, Indian Aspen Bark right over in this vicinity, which stretches back miles I think, and Jacaranda to top off the...square

Thomas pulls the engagement ring out and slips it on

his finger for a test before he places it in his pocket

LIANA Thank you for taking me here, Thomas. It’s really nice of you.

THOMAS

(He is very nervous.)

Well, it’s really...it’s really...really...appropriate...

LIANA How so?

THOMAS How so? Liana, I think...I mean...I think...oh my goodness, I’m so bad at this...I think...

There is a sudden sound of branches

snapping in the trees nearby.

LIANA Thomas, did you hear that...?

THOMAS

(He is in his own world, as he is about to propose to her.) ...I think, and I know we haven’t been dating for too long, but...

LIANA Seriously, Thomas. I don’t think we’re alone.

A Sasquatch appears behind Liana with a

ravenous look in his/her eyes.

THOMAS ...you mean so much to me, and I’m sick of repressing my wants because... No, no don’t you say a word.

The Sasquatch attacks Liana from

behind. His loud growls are

intermingled with Liana’s gory screams.

It is a truly horrific moment.

THOMAS So...I guess all that to say...I love you, Liana...and I want to spend the rest of my life with...

She is dead. Thomas finally notices.

THOMAS ...you...?

Long dramatic pause as Thomas begins to

process that his loved one was just

killed by a Sasquatch.
SCENE 2 - MORNING
News Reporter is standing in front of a
wintery pond preparing for the next
news take.

JEFFREY BANE

(to cameraman) Are we rolling? Ten seconds? Good. Would you stop that Robert!

(to camera) This is Jeffrey Bane from channel 5 news, and we are on the scene with what appears to be a heinous clash, a catastrophic...

(long pause) ...sasquatch assault took place in the Hamilton forestry last night. Details of the incident are still unclear and being investigated by Hamilton authorities as we speak...as I speak...and as you listen...sorry...but citizens of Hamilton...please, do not lose hope, or pride even, because, as sure as my name is Mr. Poopypants, this sasquatch...will not get far.

SCENE 3 - DAY: TOWN HALL (DOWNTOWN HAMILTON)

Thomas is running with great

desperation in his voice, and even demeanor.

THOMAS Mr. Mayor, Mr. Mayor, Mr. Mayor!!! I said Mr. Mayor, Mr. Mayor, Mr. Mayor!!!

Opens door to Mayor’s office and keeps

it open when he sees the mayor’s

secretary. Thomas is out of breath.

THOMAS

(to mayor’s secretary) Is this the Mayor’s office?

SECRETARY Yes

THOMAS Oh good.

(Thomas catches his breath and closes the doo.r) Where to?

SECRETARY You are going to go up one flight of stairs, go straight down the hall. You will pass three doors: one on the left, and two on the right. The one on the right is maintenance. That is not the mayor's office. The two doors on the right will be labeled, respectively, with a male symbol and a female symbol. These are the building's water closets.

THOMAS Excuse me?

SECRETARY Facilities...Restrooms.

THOMAS Where is the mayor's...?

SECRETARY I'm getting there. After the three aforementioned doors, you will turn right into a vestibule, moderate in size. This is the corridor that will lead you to the Mayor's waiting room, which...

THOMAS I can't wait. My business is high-priority. It concerns last night's sasquatch assault.

SECRETARY All sasquatch-related orders of business, for the time being, are non-recessive in nature. You won't have to wait, sir.

THOMAS Thank you stars! SCENE 4 - MAYOR’S OFFICE

Thomas knocks on the door to the

Mayor’s office. After no audible

response, he opens the door.

THOMAS Sir, are you Mayor Quatchsas, the mayor of Hamilton?

MAYOR QUATCHSAS Yes I am, Thomas Bindernagel. I’m surprised you didn’t recognize me?

THOMAS I know who you are, I was just being polite...by pretending I didn’t know who you are.

MAYOR QUATCHSAS Oh, that’s funny, Thomas. I was friends with your father John. Back when he was alive.

THOMAS He is alive.

MAYOR QUATCHSAS We all are, some of us more than others… I’m the sasquatch

THOMAS What?

MAYOR QUATCHSAS Nothing, now how can I help you, Thomas?

THOMAS Mayor Quatchsas, didn’t you hear about the Sasquatch attacks last night?

MAYOR QUATCHSAS It’s a tragedy, Thomas. It’s a horrible, horrible thing to happen to this town.

THOMAS Well there must be something we can do.

MAYOR QUATCHSAS Must. Must be. Something. Must be something we can do. We can do something.

THOMAS But what? All the local authorities move as slow as pumpkin juice...

MAYOR QUATCHSAS Thomas, your tone is so resentful!

THOMAS It’s true. We need something more than law enforcement on the sasquatch incident, because this creature does not operate by human law. I’m convinced he will stop at nothing, which means we can’t stop at anything, neither as well.

MAYOR QUATCHSAS Thomas Bindernagel, you are speaking with great haste!

THOMAS

(long pause) I’m sorry, Mayor Quatchsas. Last night, I lost the only person I’ve ever loved and with that mind, I’d like to ask for your permission to orchestrate a town meeting. It won’t be militant in nature; I just want to hear others’ opinions on this matter.

MAYOR QUATCHSAS Be my guest, Thomas Bindernagel. SCENE 5 - TOWN MEETING

Thomas is walking up on stage to an

auditorium full of apathetic and mean-

spirited townspeople.

TOWNSPERSON #1 Get off the stage you filthy animal.

Thomas taps the microphone to test the

volume and tonal levels.

THOMAS Citizens of Hamilton, my name is Thomas Bindernagel...

TOWNSPERSON #2 I’m convinced you’re a woman!

THOMAS ...And I’m up here to discuss a very serious matter that involves the well-being of our town...

TOWNSPERSON #3 ...And I’m down here to discuss your lack of eloquence as a speaker...

THOMAS Last night, a sasquatch attacked a prominent young woman from our community...

TOWNSPERSON #2 I’ve seen him, he wears skirts!

THOMAS Some of you may not realize, but a sasquatch is one of the most dangerous and unsightly creatures to roam this area of the globe...

TOWNSPERSON #1 You’re a filthy animal, which is both dangerous and unsightly to the likes of me.

THOMAS Now, Mayor Quatchsas and I both agree that this is a job only to be shouldered by the respectable citizens of Hamilton, which means...this, this means...it means that...

TOWNSPERSON #3 Ta-ta-today, Thomas...

THOMAS MY NAME IS THOMAS! It’s pronounced phonetically, with a soft ‘th’ lilt. Is that so hard to comprehend? Citizens of Hamilton, listen well: our town is in a grave crisis. A sasquatch attack, even one, equates to grave danger. Now I don’t know why you all are so apathetic and antagonistic to my cause, but this absurdity must end.

TOWNSPERSON #1 Amen, brother Bindernagel.

THOMAS Thank you.

TOWNSPERSON #2 Amen, sister Bindernagel!

THOMAS Look, I’m not a girl! I don’t know why you...I was with my girlfriend when the sasquatch attacked her...

TOWNSPERSON #2 But you’re a girl!

THOMAS Citizens of Hamilton, what do you say we gather all the weapons we can conjure up, form a posse, track down that sasquatch who I presume is still in Hamilton’s forestry, and once and for all take down the Hamilton Sasquatch!

SCENE 6 - HAMILTON’S FORESTRY Thomas and Townspeople #1,2 & 3

THOMAS Shhhh! These tracks seem starkly reminiscent a sasquatch trail.

TOWNSPERSON #1 Thomas, speaking candidly and from the heart, we may very well be walking in circles.

THOMAS I’m just following the trail, I have an inkling we’re coming close, though. Weapon check, boys, Baseball bat?

TOWNSPERSON #1 Check.

THOMAS Shot gun?

TOWNSPERSON #2 Check.

THOMAS Machete?

TOWNSPERSON #3 Check.

THOMAS And I’ve got my Sangh Jeol Bahngs.

Thomas swings around his nunchucks.

There is sound of branches snapping in

the near distance.

TOWNSPERSON #3 Did you guys hear that?

TOWNSPERSON #1 Yep, Townsperson number three, it was the sound of four friends hunting some no-good sasquatch. What do you say to an ice-cold brewsky when we get home?

TOWNSPERSON #3 No, I really think I heard something this time, like some branches snapping or something.

TOWNSPERSON #1 Boss, I don’t mean to doubt you, but there are a lot of possum, locust, and other wilder-beasts in Hamilton this time of year.

THOMAS He’s right, there’s no room for false alarms...

Sasquatch attacks Townsperson #3.

TOWNSPERSON #2 Hey, woman, you call this a false alarm. Look at the blood.

THOMAS

(Noticing the graphic sight of his friend’s dead body) What the stars in the world for the love of them!? Hamilton Sasquatch, I know you’re out there, behind some tree! In the name of pride, possum, Hamilton and happiness, come out from wherever you are!

Sasquatch comes out from behind a

nearby bush.

SASQUATCH

(growls loudly and obnoxiously)

TOWNSPERSON #1

(whispers) He’s hideous.

TOWNSPERSON #2 And definitely not a woman. Look at his claws.

THOMAS

(slowly and intensely) Sasquatch, I hate you! Get him boys

Thomas’ words set off a violent chain

of events between Thomas and the

Townspeople against their dangerous

adversary.

TOWNS PERSON # 1 Oh dang I always go crosseyed when I’m aiming. Which one is Thomas?

THOMAS Ouch! You just shot me! What’s wrong with you? Oh this can’t be good, My hand can fit in the whole…

Ultimately, the sasquatch is

killed and falls to the ground. Thomas

comes out of the fight with a fatal

injury.

TOWNSPERSON #1

(sees Thomas struggling) Whoa, Thomas, we need to get you to a doctor.

THOMAS

(obviously in pain) No. Don’t bother. There’s just on thing I need to do...

Thomas uncovers the sasquatch’s face,

which reveals the face of none other

than Mayor Quatchsas.

THOMAS I knew it.

TOWNSPERSON #1 Mayor Quatchsas? Who would’ve known.

THOMAS Well it’s actually quite simple; you see if you switch around the quatch and the sas, the Mayors name really spells Sasquatch!

TOWNSPERSON #1 He’s dead.

TOWNSPERSON #2 Look at the blood, definitely not a false alarm.

TOWNSPERSON #1 I’m just happy that Thomas is now in a better place, with his soul mate, Liana.

TOWNSPERSON #2 I’m astonished his lucky stars were cursed without even a wound to show for it. What a woman!
```

---

## IC-1040: Luigi & Mario A Comedic duo by Ray Nesrym, © 2010

- Title: Luigi & Mario A Comedic duo by Ray Nesrym, © 2010
- Author (byline): Not specified
- Work: Luigi & Mario A Comedic duo by Ray Nesrym, © 2010
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1597
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
TOAD-Hey! You! have you seen Mario?
LUIGI-Why no Toad, I haven’t. Why?
TOAD-Bowser sent him letter.
LUIGI-What about me?
TOAD-Why would Bowser send you a letter Luigi?
LUIGI-Why would he send my brother a letter?
TOAD-Oh, gee well I don’t know, maybe to tell him HE KIDNAPPED THE PRINCESS
AND MARIO NEEDS TO GO SAVE HER!
LUIGI-Well I could go and save her!
TOAD-hahahahaha, ha(laughing so hard he cries)
LUIGI-(while Toad is Laughing) What? What is so funny?
TOAD-(still laughing)Nothing Luigi, just give this to Mario please.
LUIGI-(grumbling) stupid Toad laughing at me, I could beat Bowser, if only I gotta good
chance. What is this a stupid letter anyways? This stupid letter for my stupid brother. Where
is he anyways?
MARIO-it’s me A-Mario! Hey Luigi my little brother whatcha got there?
LUIGI-Oh, this? It’s a letter for you from Bowser.
MARIO-(takes letter and reads it aloud) Dear Mario, how are you? Are you still living with
that loser brother of yours? He is such a dork. Anyhow, I have captured the princess again
and I-
LUIGI-Wait second! Did He just call me a dork?
MARIO-Calm down Luigi!
LUIGI-Oh, no I don’t think so.
MARIO-Luigi it’s fine I’ll just go save the princess and beat him up like always!
LUIGI-You always get to save the princess, how come I never get to do anything cool! Ever
since we signed that contract with Nintendo it’s I’ll do this, and I’ll do that! I never get to see
any of the action!

MARIO-Ok then… you can come and watch me.
LUIGI-You just don’t get it do you! The contract said we were going to be equals!
MARIO-What are you talking about Luigi? We are equals!
LUIGI-Yeah right you get all the big game titles while I never get to do anything!
MARIO-that’s not true you have plenty of great games!
LUIGI-Like what?
MARIO-like…uh…Like Luigi’s Mansion! That was a good game!
LUIGI-Oh yeah Luigi’s Mansion, you get Mario World, and Super Mario World, and Mario
tennis, and Mario Kart, 8 Mario Parties, Mario Strikers, Mario Sunshine, and Mario Galaxy
and all I have is a Mansion, a frikin’ haunted mansion, where I capture ghosts with a sucky
vacuum cleaner like some kind of frikin’ Ghost Buster. Really Mario How the hell is that
fair!
MARIO-What about the games we are in together eh?
LUIGI-like what?
MARIO-like uh Mario and Lui-
LUIGI- That’s something else I don’t get! Why’s it always Mario and Luigi, never Luigi and
Mario!
MARIO-Calm down your name is just second.
LUIGI-That just it my name is always second! Ever since we were little!
MARIO-Just cool it bro!
LUIGI-Don’t even get me started with bro!
MARIO-(confused) What are you talking about!?
LUIGI-If it’s not (with contempt) Mario and Luigi, it’s The Mario Brothers. Mario isn’t even
our last name. They can tell people it is, but it isn’t! Who would believe them anyways, I
mean that would make your name Mario Mario for crying out loud! Come on who would
buy that? Our last name is Dicapprio! But do they call us the Dicapprio Brothers? No! They
call us the Mario Brothers!
MARIO-you still get attention, remember when we went on Oprah?
LUIGI-yeah
MARIO-you got plenty of attention there!
LUIGI-you got me kicked out by the security guard when you told him I was a hobo!
MARIO I was just playing around. Besides he let you back in afterwards.
LUIGI- I had to hide in a garbage can!
MARIO-Oh…Yeah… well I don’t have it that easy either Luigi! I workout all the time but I
am still a little fatter than you but you don’t see me complaining.
LUIGI-Well no duh you’re fat! You hog all the fame and the pasta! I mean do you even fit in
the pipes anymore?
MARIO-yes
LUIGI-Then why don’t we use the short cut to the castle?
MARIO-Because...I don’t want us to get pipe gunk all over our new clothes.
LUIGI-What new clothes?
MARIO-You know the new clothes we got from our parents as a gift.
LUIGI-Um… no I don’t know
MARIO-Oh…yeah… I wasn’t supposed to tell you about those.
LUIGI-Why not?
MARIO-Cause you aren’t getting any…
LUIGI-Are you serious! EVEN OUR OWN PARENTS LIKE YOU BETTER-
MARIO-Luigi quiet!
LUIGI-QUIET! YOU WANT ME TO BE QUIET!
MARIO-Shut up did you hear that?
LUIGI-hear what?
MARIO-It’s…the Koopa Krew!
KOOPAS-Were the Koopa Krew
Were coming for you!
You’re gonna feel our shellshock oh!

Shellshock oh!
ONE TWO THREE word!
MARIO-Yeah no, don’t do that again. That was so bad 50-cent just dropped dead.
KOOPAS-then I guess you’ll see him in hell Mario.
MARIO-yeah…Right…(stomps on Koopas)
LUIGI-Mario, how come you didn’t let me kill one!
MARIO-Oh. I’m sorry, I just thought they looked a little tough for you.
LUIGI-They died when you jumped on them.
MARIO-Well… there’s a goomba over there you can him if you want.
LUIGI-Freddy was a goomba. And you killed him!
MARIO-Freddy? Who the hell is Freddy? In never killed any Freddy!
LUIGI-Frerddy was my friend! He was a goomba that lived on world 2-1 before you
mercilessly stomped on him. Did he ever do anything to you? No! he just walked back and
forth, but then one day you came along and stomped on him just because he was a goomba!
That’s the only reason you’ve ever had for killing gommbas, your such a racist jerk. I mean
the koopas are at least hostile, but not the goombas. And yet you’ve killed so many innocent
goombas just like poor Freddy.
MARIO-Luigi Have you been sniffing the one up mushrooms?
LUIGI-Are you taunting me? I’ve had it! You never listen and you don’t even value the life
of other creatures! Lets see how you like it Mario!(Luigi Stomps on Mario)
MARIO-(falls over as Mario death music plays) Do doot doot do doo doo doot doo doo
doot
------------------------------------------------------------------------------------------------------
B-Hey princess, what the hell is taking Mario so long?
P-I don’t know Bowser
B-well… this is akward…what should we do?
P-Lets bake a cake!
B-Or we could make out…

P-can we bake a cake afterwards?
B-sure…
P-ok ( they make out)
-------------------------------------------------------------------------------------------------------
LUIGI-Oh my god! What have I done! I killed Mario! What am I gonna do? What if I-
(Mario’s cell phone starts ringing, Luigi is startled, he leans over and picks it up)
LUIGI-Hello?
NINTENDO EXECUTIVE-Hello? Mario it’s me, your manager. Something wrong you
sound kinda funny.
LUIGI-oh this isn’t Mario this is Luigi.
NINTENDO EXECUTIVE-Luigi? Who is that? I must have the wrong number. Sorry for
troubling-
LUIGI-Wait! You have the right number! I’m Mario’s brother Luigi!
NINTENDO EXECUTIVE-He has a brother?
LUIGI-Yeah haven’t you heard of me! I’m the green guy Luigi!
NINTENDO EXECUTIVE-Oh you mean the dino thing!
LUIGI-No that’s Yoshi, I’m Luigi. You know the guy with the green overalls. I have an L on
my head and-
NINTENDO EXECUTIVE-Wait, what's the L for?
LUIGI-Luigi, What else would an l on my head stand for?
NINTENDO EXECUTIVE-um…Never mind I remember you now. I’m so sorry I had
forgotten you existed. Well Luigi can I talk Mario please?
LUIGI-Sure…(turns to hand phone over toMario looks down) oh wait…never
mind..um…no…no you can’t
NINTENDO EXECUTIVE-Um, why not?
LUIGI-He’s…um…kinda busy
NINTENDO EXECUTIVE-Ah, I see busy like a bee eh?

LUIGI-Yeah, um kinda like that…wait…is the bee dead?
NINTENDO EXECUTIVE-of course not
LUIGI-Oh…well then never mind not like that. Um…if you want I can take a message for
him.
NINTENDO EXECUTIVE-That’d be great. We had a new game idea for him, Super
Nation! Do you think he’d be willing to work on it?
LUIGI-Um…no
NINTENDO EXECUTIVE-no?
LUIGI-yeah, he was telling me recently he doesn’t want to be in anymore games for a
while...by which he means forever.
NINTENDO EXECUTIVE-I see, well do you think you know anyone who could take his
place in this game and maybe fill his shoes?
LUIGI-(eagerly) Why sir I know just the person!
NINTENDO EXECUTIVE-Great tell me about him.
LUIGI-Well, he is very closely related to Mario, knows him very well since birth even! But
he hasn’t really gotten much of the limelight yet and-
NINTENDO EXECUTIVE- I think I know exactly who you’re talking about! And I think
he’d be perfect
LUIGI-(excited)you do?
NINTENDO EXECUTIVE-Yeah, thanks a lot this guy will be perfect! Man Wario will be
excited when I tell him about this. Thanks a lot Mr... um Louie?
LUIGI-Eh?!...But… I didn’t…
NINTENDO EXECUTIVE-Say Louie can you do a job for me?
LUIGI-(still hopeful) What?
NINTENDO EXECUTIVE-You knew what Mario looked like fairly well right?
LUIGI-Well I guess
NINTENDO EXECUTIVE-Great! I’ll need someone to make a Mario costume for Wario
to wear. With any luck people won’t even know the difference. And since you knew what he
looked like better than anyone else it would be very helpful if you could sew it for me.

LUIGI- Why would I-
NINTENDO EXECUTIVE-Thanks a lot Louie
LUIGI-(overlapping Nintendo Executive) But I…I really can’t…I never said I would…I
don’t even know how to sew.
NINTENDO EXECUTIVE-I’ll have some people drop by and pick it up tomorrow thank
bye.*click*
LUIGI-(sigh) I hate my life.
```
