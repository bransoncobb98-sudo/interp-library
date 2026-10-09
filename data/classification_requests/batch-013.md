# Classification request: batch 13 of 53 (40 records, IC-0881 to IC-0920)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-013-reply.json`.

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

## IC-0881: Oedi

- Title: Oedi
- Author (byline): Rich Orloff
- Work: The Best American Short Plays 1997-1998 (Edited by Glenn Young), Pgs 162-178
- Publisher: Applause Theatre Books
- Publication date as stated: May 2000
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: TOWN CRIER, OEDIPUS, CREON, JOCASTA
- Teaser before the introduction: Yes
- Spoken words (computed): 1853
- Already set (do not supply): none

### Source block (context only)

```text
Author: Rich Orloff
Book: The Best American Short Plays 1997-1998 (Edited by Glenn Young),
Pgs 162-178
ISBN: 978-1557833655
Publisher: Applause Theatre Books
Date (Month/Year): May 2000
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 2: Welcome to Ancient Greece and the city of Thebes – the birthplace of the infamous Oedipus.

ACTOR 1: Before he was even born, the oracle at Delphi (both gesture in some way to the gods) told his parents that the boy would grow up to kill his father and marry his mother. (shocked gasp)

ACTOR 2: So . . . his parents did what many people with unwanted children did in the past.

ACTOR 1: They had the baby's feet spiked and hired a herdsman to abandon the child in the wild. (both shrug)

ACTOR 2: The kind-hearted herdsman just couldn’t do it. Instead, he gave baby Oedipus to a childless king and queen in Corinth and they raised Oedipus as their own.

ACTOR 1: (in an ominous voice) But one cannot circumvent the will of the gods! (thunderclap)

ACTOR 2: Okay, enough with the dramatic. Our story opens with Oedipus as an adult finding out the news of who he truly is.

ACTOR 1: This is Sophocles’ story of Oedipus from the comedic imaginings of Rich Orloff

ACTOR 2: . . . Oedi! Come on down!
```

### Performance text (classify this)

```text
Suggested Roles: ACTOR 1: Town Crier, Creon and Jocasta ACTOR 2: Oedipus

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

TOWN CRIER: (Pg 162-178) (off stage) Hear ye, hear ye! ________o’clock and all is well. For the best in dining delicacies, treat yourself to Hecuba’s House of Hummus! Try their babagonoosh!

OEDIPUS: Creon, my trusted aide, you have returned! Ever since the plague has hit our beloved Thebes, the people insist that we find the killer of their former king. They are convinced that until we punish the murderer, the plague shall continue. As their new king, I owe them the truth. Besides, the latest polls show my popularity's plummeting. I created the Creon Commission to ferret out the facts of this fearsome felony, and I demand to know what you have learned.

CREON: Well, first we visited the oracles of Delphi. They [told] us that King Laios was murdered by his own son!

OEDIPUS: But that's crazy. Laios had no son.

CREON: Actually, he did, many years ago, but the child was banished as an infant. People assumed the child died in the wilderness.

OEDIPUS: Poor child. I feel his pain, as if it were my own.

CREON: Funny you should say that. We learned the child had been rescued by a shepherd a grew up to be about your height, your weight, and according to descriptions, he looked a lot like you.

OEDIPUS: What a coincidence.

CREON: Oedipus, how to put this... You know how much I admire you. When you first came to town, it was I who encouraged the people to make you king. (beat) You never murdered anyone, did you? Say, kill anyone on your journey here?

OEDIPUS: Let me recall. I decided it was time to leave Corinth and seek my fortune in the world. So I decided to journey to Thebes. When I got to the town of Phokis, I met a hostile band of travellers. One of them called me a mama's boy, so I clubbed them all to death. Other than that, I didn't kill anyone.

CREON: For that you clubbed him to death? Well, Oedipus, I don't know how to tell you this, but we learned that King Laios was clubbed to death in the town of Phokis.

OEDIPUS: You're not suggesting I - I'd never kill a king. It's - It's inappropriate.

CREON: He was on a religious pilgrimage. . . He always dressed down for those things.

OEDIPUS: Then it's possible But Tiresias prophesied that Laios would be killed by his own son. I never even met the man before.

CREON: Oedipus, we discovered Polybus and Merope weren't your real parents. You're an orphan. We also know that the son of Laios had a birthmark in the shape of an olive on the bottom of his left foot. [Creon stares at Oedipus' left foot.]

OEDIPUS: But I hate taking off my sandals. It always takes so long to lace them back up.

[Oedipus unlaces his left sandal and lifts his left foot. On the bottom of his foot is a birthmark in the shape of a huge green olive with a red pimento.] As you can see, my foot has no such mark.

CREON: Oedi, admit it. That's an olive.

OEDIPUS: I prefer to think of it as an unripe eggplant with ketchup on it.

CREON: It's an olive.

OEDIPUS: Okay, okay. Technically speaking, it's an olive. Oh, woe to me and those who dwell in my house! I've slain a king, and I promised the people I'd put the killer to death. I even said, "Read my lips." But wait! One thing isn't clear.

CREON: Here comes the messy part.

OEDIPUS: If I'm Laios' son, and if Laios was married to Jocasta, who is now my wife, that means, that means, that means - Laios must've had a previous wife, right?

CREON: I'm afraid not.

OEDIPUS: Ever fool around on the side?

CREON: Never.

OEDIPUS: Sperm donor?

CREON: Nope.

OEDIPUS: Oh my gods! Oh my gods! I've married my mother!! No wonder she always knows what I want for breakfast. Oh my gods! I've murdered my father and married my mother! Oh, wretched day! Oh, cursed life! How can I expunge the evil deed from my soul? There is only one way! I must pluck out my eyes immediately! [Oedipus tries to pluck out his eyes, but Creon holds his arms back.]

CREON: Don't do it! You'll have a moment's satisfaction, and a lifetime of wondering if your toga's on straight.

OEDIPUS: Okay, okay. Let go...Does my beloved wife know about this?

CREON: Not yet.

JOCASTA: [off stage] Yoo-hoo, oh, Oedi!

CREON: The queen approaches. [Creon exits]

OEDIPUS: [Calling out] In here, snookums! [Jocasta enters. She's easily thirty or more years older than Oedipus. If she happens to be short and speaks with a slight old world inflection, so much the better.]

OEDIPUS: Jocasta, I must tell you something most horrible, worse than the most terrible news you could imagine.

JOCASTA: You didn't like my brisket last night?

OEDIPUS: That's not it.

JOCASTA: My toga's too short, isn't it? You think a woman my age . . .

OEDIPUS: Your toga's fine.

JOCASTA: Are we having problems I'm unaware of in the horizontal department?

OEDIPUS: No, everything's fine in the - Jocasta, I just received the report of the Creon Commission.

JOCASTA: Oh, good. As soon as we name the murderer of Laios and make him drink some seltzer with a shpritz of hemlock, I know your approval rating will bounce right back.

OEDIPUS: I don't think so. Jocasta. . . The murderer of your late husband stands before you.

JOCASTA: You killed Laios? Oh, no! Horror of horrors! I suddenly feel like plucking

OEDIPUS: Don't pluck your eyes out!

JOCASTA: No, I feel like plucking a chicken. I'm so stressed. How are we going to put a spin on this so the public doesn't hate you?

OEDIPUS: Don't you hate me?

JOCASTA: How can I hate you for something I thought of doing every single day of our marriage?

OEDIPUS: I thought you loved him.

JOCASTA: What's to love? The man snored, he had bad breath, and when I think of the things he made me do . . . the news is not that bad at all.

OEDIPUS: But I have not told you all of it. Jocasta, you remember the prophecy of Tiresias that your husband would be murdered by your son?

JOCASTA: Yes, also remember he prophesied. . .The Iliad would never make it as a novel.

OEDIPUS: [Well], there's reason to believe that, by some ferocious folly of the fates, you married your own son.

JOCASTA: So? Tell me something I don't know. From the first moment you came into town. I took one look at those eyes, that smile, that - oh, wait a second, you have a little shmutz on your forehead. [Jocasta licks her fingers and begins to wipe Oedi's forehead.]

OEDIPUS: Stop that! How could you know I was your son and not tell me?

JOCASTA: I didn't think it was significant.

OEDIPUS: You married me!

JOCASTA: You asked. I would've been happy just dating; you were the one in a hurry. "Marry me, Jocasta, and I'll be the happiest man on earth." What mother could refuse such an offer?

OEDIPUS: But I killed Dad!

JOCASTA: So? He never liked you anyway. Once he heard Tiresias' prediction that you were destined to murder him, he insisted you be sent away. I said, "Can't we wait and see? Maybe he'll just wound you a little." Look, you're here and all is well, so unless there's some more news, I want to get to my belly dancercize class. I need to be in ship shape.

OEDIPUS: Don't you think we have some issues to discuss?

JOCASTA: Like what?

OEDIPUS: Like the fact that we can no longer live as husband and wife.

JOCASTA: Why not?

OEDIPUS: Because you're my mother!

JOCASTA: You say that like it's a negative.

OEDIPUS: Men cannot marry their mothers!

JOCASTA: From what I've heard, most men marry women who remind them of their mothers. Why settle for second best when you can have the real thing?

OEDIPUS: No! I want to be with a woman to whom I'm not already related. I'm a public official. I'm a role model.

JOCASTA: So? Look at the Gods. Zeus has slept with his half-sister, his quarter-sister, his sixteenth- sister. If our own gods get to boff their relatives, why can't you?

OEDIPUS: Because you're my mother!

JOCASTA: Must you make everything so complex, Oedipus? Look, Oedi, I understand this is traumatic for you. But in a healthy marriage, you work through these things.

OEDIPUS: We don't have a healthy marriage! Mom. . . I want a divorce.

JOCASTA: [breaks into hysterical crying] I never thought I'd hear such a thing from my own son. Call in your advisor. See what he says.

OEDIPUS: Get me Creon! [CREON enters]

CREON: I have been busy, my lord, making some initial inquiries into public response to the crisis: The people are confused. 85% of those polled strongly agreed with the statement, "If two people love each other, nothing else in a marriage is important." But 54% also believe that those who commit incest should be boiled alive in non-virgin olive oil.

OEDIPUS: I didn't know she was my mother, does it still fit the technical legal definition of incest?

CREON: Why don't you start a war? That's always a good distraction.

OEDIPUS: I'm not going to start a war just to boost my approval rating. There's only one answer which will prove to the people I show remorse for my sins. I must pluck out my eyes!

CREON: Wouldn't a sincere "I'm sorry" suffice?

OEDIPUS: No! Give me your golden pins. [Oedi grabs two large pins from Jocasta’s toga or hair.]

CREON: Oedipus, don't!

OEDIPUS: Silence! Stand back! [Raising the pins.] I declare myself guilty of wretchedness and sin! From this hour forth, I go in darkness! [Oedipus is about to plunge the pins into his eyes, but he stops at the last moment.] Or . . . maybe I'll just cut off the offending organ which caused the sinful deed. That's it! I'll save my sight but lose my jewels. I declare myself guilty of wretchedness and sin! From this hour forth, I go in eunuchness! [Oedipus is about to plunge the pins into his pelvic region, but stops at the last moment.] Or . . . maybe I'll just cut off my arm. It's a more visible symbol anyway. My left arm, or maybe just one of my fingers, since we're talking symbolic action!

CREON: You know, Oedipus, the more I think about it, the more I wonder, why are we driving ourselves into such a tizzy? You know how fickle the people are. Today they'll want to burn you at the stake; in a week, they'll be obsessed with the latest gossip about the gods. All we need is one good speech and a heartfelt explanation.

OEDIPUS: But how can we explain such a monstrous deed? Oh, what am I to do? If only the gods would give me a sign.

CREON: Maybe they have. Run with me a little. Tiresias saw your fate when you were born; you tried your best not to live it out, but there are powers beyond those of we poor mortals.

OEDIPUS: I get it! Any efforts to forswear malfeasance were futile; it was the fault of the fates! I'll make a speech where I'll take complete responsibility for my actions, but none of the blame.

CREON: We'll say you wanted to smite out your eyes, but you placed your sense of public duty ahead of your own desires. [Imagining the headline:] "Oedipus Rex, Tragic Hero."
```

---

## IC-0882: Okoboji

- Title: Okoboji
- Author (byline): Suzanne Bradbeer
- Work: The Best Ten-Minute Plays 2012, Pgs 170-176
- Publisher: Smith and Kraus
- Publication date as stated: June 2013
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ALAN, ANNIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1801
- Already set (do not supply): none

### Source block (context only)

```text
Author: Suzanne Bradbeer
Book: The Best Ten-Minute Plays 2012, Pgs 170-176
ISBN: 978-1575257938
Publisher: Smith and Kraus
Date (Month/Year): June 2013
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: Welcome to Okoboji Lake

ACTOR: -- where ordinary conversations ripple with unspoken revelation –

ACTRESS: -- where every glance, every pause, suggests a deeper story..

ACTOR: Here on the shore, Alan (a father) and Annie (his son’s friend) are drawn together by necessity –

ACTRESS: -- or coincidence, to exchange words that reverberate in the stillness.

ACTOR: Often the battles that matter most:

ACTRESS: Depression, despair . . . guilt

TOGETHER: Are the ones we cannot see.

ACTRESS: But somewhere, perhaps, there might exist a glimmer of grace.

TOGETHER: Okoboji by Suzanne Bradbeer
```

### Performance text (classify this)

```text
Alan Harper – mid 40s / 60s – an artist from Boston; Annie Hansgen – early 20s “ / ” indicates an overlapping of lines

*****

(Alan and Annie, looking at West Okoboji Lake. It is early morning in Iowa)

ALAN: (Pg 170-176) So this is it. The famous blue lake . . .

ANNIE: Yeah.

ALAN: Cobalt. Cobalt blue. It's almost a Prussian blue, but not quite. No, it's definitely cobalt. My favorite color.

ALAN: Have you ever been to Boston?

ANNIE: No. I'd like to someday.

ALAN: There's a painting at the Museum of Fine Arts, it's by William Merritt Chase, have you heard of William Merritt Chase?

ANNIE: No.

ALAN: I don't much care for him, I find him a little prissy in his subject matter, but I like this particular painting, and he uses this exact shade of blue.

ANNIE: I'd love to see it.

ALAN: This exact shade of blue . . .. (uncomfortable, he looks behind them) Look at all those trees.

ANNIE: I know, aren't they beautiful? Oak trees are my favorite.

ALAN: I hate nature.

ANNIE: (picking up a feather from the ground) Look, a hawk's feather! Look!

ALAN: Are you Indian? I mean, sorry, Native American?

ANNIE: No.

ALAN: How do you know so much about the fauna and the flora?

ANNIE: You mean, the hawk's feather?

ALAN: Hawk's feather, oak trees, yes, how do you know all that?

ANNIE: Um, the oak is a pretty common tree? And the red-tailed hawk, they've made their homes all over this country -- in meadows, mountains -- the desert. They even have them in cities, like where you're from, Boston; I even heard there were these red-tailed hawks on Fifth Avenue in New York, a hawk couple named Pale Male and Lola.

ALAN: Fascinating. (looks back at the lake, considering) They say this is one of only three true blue water lakes on the planet. 'Course you probably already know that, what with your obsessive cataloguing of the natural world. (no response from Annie) One of three on the planet and yet I had never heard of West Okoboji Lake until a year ago. Do you know where the other two blue water lakes are?

ANNIE: Lake Geneva in Switzerland, and Lake Louise in Alberta, Canada.

ALAN: Correct. I wonder how many people in the world have seen all three? Maybe there's a group, a society you can join, I could probably go online and find the Blue Water Lake Club.

ANNIE: Sounds neat.

ALAN: Sounds hideous. I hate clubs. Turns out though, I could be a founding member.

ANNIE: You've seen all three? Really?

ALAN: Lake Geneva, beautiful of course. Lake Louise, Brian was conceived in the Hotel Banff on the shores of Lake Louise. At least that's what we always liked to say. Brian's mother and I were very . . . at any rate, let's just say it's hard to pinpoint the exact moment. But I like to think it was in the Hotel Banff. (beat) I'm always quite moved by rarity. One of only three blue water lakes. Biggest diamond in the world. Only son.

ANNIE: (beat) Brian's eyes were this color.

ALAN: Yes.

ANNIE: That was one of the first things I noticed about him. I've never met anyone else with eyes that were/ so blue.

ALAN: Brian's great-great-great grandfather was a Colonel in the Revolutionary Army. A Colonel is a very high rank, during the Revolution it was second only to General and, and I, I don't know what made me think of that except that he, the Colonel, he seemed to be quite fond of nature too. We have a few of his letters; he survived the war and wrote constantly, incessantly about his travels up and down the Massachusetts Shore. They're quite valuable these letters – Boring but valuable. Why are you smiling?

ANNIE: We used to call Brian 'the Colonel'. Even in the short time we knew him. It was very important to him that people respect the lake and the woods. He always spoke to everyone in a nice way, but he was very firm about it, if they were littering, or being careless, he was very firm.

ALAN: Were they mean to him?

ANNIE: Who?

ALAN: Anyone, was anyone mean to him?

ANNIE: No. No.

ALAN: He was bullied quite a lot when he was in school.

ANNIE: He told me.

ALAN: So, calling him the Colonel, they weren't being, mocking/ or, or ?

ANNIE: No, not at all --

ALAN: Because a boy less like a Colonel you could hardly hope to find.

ANNIE: We called him the Colonel because he / had very ---

ALAN: Yes, I remember that he advised people not to litter.

ANNIE: It wasn't just that . . . he, he had standards of behavior, very high standards of behavior -- for himself especially. And he was very, responsible and, and -- Oh! He always identified time in that military way, like nine o'clock at night wasn't nine o'clock, it was 2100 hours.

ALAN: 2100 hours, yes. He started doing that when he was about seven, for some reason.

ANNIE: And he valued loyalty. And doing the right thing. And niceness . . . I think he valued niceness most of all.

ALAN: Brian was much more like his mother. I had a good night’s sleep that night.

ANNIE: Sir?

ALAN: I don't usually sleep well, but that night I was sleeping very well. Until the call. I don't understand how I slept through . . . that moment. I don't understand that. They say he died immediately.

ANNIE: Yes.

ALAN: I thought maybe they lied. To spare me, I thought maybe they lied.

ANNIE: No.

ALAN: (This is what he's been waiting to say) See, I would prefer to think that you fired the gun accidentally, accidentally of course -- but I would prefer to think that you fired it, rather than . . . rather than what you want me to think.

ANNIE: I don't want you to think anything.

ALAN: But can you understand that? Can you understand how a father would prefer to think that?

ANNIE: . . . I guess.

ALAN: So this, this inquiry, or inquest, or

ANNIE: Autopsy, it was just / an autopsy-

ALAN: Whatever it was, it doesn't have a workable result for me.

ANNIE: But why -- I mean, that was a month ago – why / are you

ALAN: And I've been giving it a great deal of thought in the last month, a great deal. As you can imagine. And I just think that maybe you should admit what really happened.

ANNIE: I'm sorry, but didn't you read the report? The forensics were very clear.

ALAN: I don't care about God-damn forensics! I care about my boy. You were there; you could have shot him, you'd / both been

ANNIE: No.

ALAN: Yes! A bunch of you had been drinking earlier that night, you admitted as much. And maybe, maybe you'd never held a gun before / and maybe you-

ANNIE: How can you say that to me?

ALAN: Where did he get the gun?

ANNIE: It's not hard to get a gun.

ALAN: Maybe you were curious and wanted to see what it felt like and maybe Brian was trying to show you but neither of you realized that the gun was loaded / and maybe

ANNIE: Is this why you came all the way back here?

ALAN: No one would blame you. I would make sure / of that.

ANNIE: He shot himself in front of me, Mr. Harper.

ALAN: No he didn't. It was an accident.

ANNIE: He shot himself in front of me.

ALAN: If you ever have children you might understand how cruel you're being right now.

ANNIE: (beat) I'm sorry.

ALAN: My son was not cruel.

ANNIE: No, he wasn't.

ALAN: That's a very cruel thing, if it's true. To do what he did in front of you.

ANNIE: I don't think he meant to.

ALAN: See! It was an accident!

ANNIE: I just meant that he didn't mean for me to see; he didn't expect / me to --

ALAN: Why can't you say it was an accident-just tell me it was a God damn accident -- what the hell is wrong with you?!

ANNIE: . . . It was an accident.

ALAN: . . . I could wish you were a better liar.

ANNIE: . . . Me too. (beat) I knew he was depressed. I think he was depressed for a long time. We talked about it sometimes. He said he considered it part of his life. But it wasn't the only part. And it doesn't take away from the things that made him happy. This lake made him happy, especially this time of day, especially right here. Remembering his Mom made him happy. And you, your paintings, your paintings made him happy.

ALAN: I'm not painting anymore.

ANNIE: You don't hate nature.

ALAN: What?!

ANNIE: You said you hated nature. You're a painter, I don't think you hate nature.

ALAN: You don't know me. You don't know me and you barely knew my son -- you knew him, what, ten months? You can't know someone in ten months.

ANNIE: He talked about showing you this lake. He said the first thing you'd do would be to identify the exact color.

ALAN: Anyone would do that.

ANNIE: And say it was your favorite color and then mention some obscure painter who has three names.

ALAN: William Merritt Chase is hardly obscure. (beat) It's true; Brian was often amused by what he called my, predictability. Did he tell you that? (Annie nods) What else did he say about me?

ANNIE: I know that he loved you, Mr. Harper.

ALAN: (beat) I'm not a warm person. I am aware of that, you know. (Annie rolls her eyes) Did you just roll your eyes?

ANNIE: Did I? Sorry. I thought I just rolled them in my mind. Sorry.

ALAN: It's all right. (looking around) This is a nice spot. And it was nice of you to bring me here. You seem like a nice kid. I'm ready to go back now. (walks off, then looks back at Annie who hasn't moved) Are you coming?

ANNIE: . . . I'm not a nice kid.

ALAN: What?

ANNIE: (distraught) I let him down. I'm not a nice kid! He needed me and I let him down.

ALAN: How?

ANNIE: He reached out to me -- that last week. He left me a couple messages, but I was preoccupied. I don't even know with what, with nothing, with my own boring problems, which were nothing, they were nothing! I didn't get back to him until the party. I knew he was depressed and I didn't get back to him until that party. What is wrong with me?!

ALAN: (carefully) I shouldn't have said those things to you. I'm sorry.

ANNIE: I'm not a nice kid!

ALAN: You didn't let him down.

ANNIE: You don't know!

ALAN: I do know. I know a few things. I've lived a long time and in spite of all evidence to the contrary, I know a few things. You didn't let him down. (looking at her) You don't believe me? (Annie shakes her head) I'm your elder. I think that means you have to believe whatever I say.

ANNIE: I'm sorry, but I don't.

ALAN: Well. Then we'll just have to stay in touch till I figure out how to convince you. Can we do that? (Annie shrugs, helpless) (gently) Let's do that, let's stay in touch. Now tell me something. Why are you still carrying around that dirty feather?

ANNIE: (looking at the feather, surprised she still has it) Birds are believed to carry messages of the spirit. Did you know that? A bird feather represents strength and . . . protection. And a hawk feather, a hawk feather is extra special. If you find a feather like this, you're supposed to let it go back into the wind with a prayer, or . . . or a message.

ALAN: I thought you weren't an Indian.

ANNIE: I'm not, I'm just from Iowa.

ALAN: (of the feather) You're supposed to send it back into the wind?

ANNIE: (nods) With a prayer or a message.

ALAN: Then, let's do it.

ANNIE: Do what?

ALAN: Let's send a message. (Annie hesitates. Then she holds the feather aloft. Alan stands next to her, but not touching her. Beat. Annie lets go of the feather and they watch it fly off over the lake)
```

---

## IC-0883: Once Upon a Tim

- Title: Once Upon a Tim
- Author (byline): Stuart Gibbs
- Work: Not specified
- Publisher: Simon and Schuster Books
- Publication date as stated: Mar 2022
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: TIM, BELINDA, PRINCESS, TOWN CRIER, RUPRECHT, NERLIM, PRINCESS GRACE, STINX
- Teaser before the introduction: Yes
- Spoken words (computed): 1311
- Already set (do not supply): none

### Source block (context only)

```text
Author: Stuart Gibbs
ISBN: 978-1534499256
Publisher: Simon and Schuster Books
Date (Month/Year): Mar 2022
```

### Introduction (context only: never use it for content warnings)

```text
Once Upon a Tim by Stuart Gibbs
```

### Performance text (classify this)

```text
Suggested Roles: Actor: Tim, Nerlim, Stinx

Actress: Belinda, Princess Grace, Town Crier, Ruprecht,

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

TIM: (Pg 1-7) Once upon a time there was a prince who was revered throughout the land for being exceptionally brave in the face of grave danger (strike a brave pose)

BELINDA: This is NOT his story.

TIM: (drops façade) Well, there are lots of other people who aren’t princes or princesses and trust me: we have way more problems than the rich folks do.

BELINDA: We’re called peasants. And being a peasant stinks. We’re all really, really poor.

TIM: See [what] I’m wearing? The only clothes I own. I’ve been wearing the same outfit for two years – and it was a hand-me-down from a cousin who wore it for two years before me.

BELINDA: All the princes and princesses live in castles with hundreds of rooms.

TIM: I live in a hut (gestures to imaginary dwelling) You might be thinking to yourself, “Gosh, that’s awfully small, but it looks cozy.” Well, it’s not! Peasants can’t afford fancy stuff. Any animal that wants to get into your house can do it!

BELINDA: Flies (swats at a fly), lice (scratches furiously), raccoons . . .

TIM: . . . wild boars and the occasional dragon (scans the sky). Here are a few other things we don’t have: Air-conditioning, refrigerators, televisions

BELINDA: Internet. Bathrooms!

TIM: We don’t have bathrooms. No toilets! I’ll admit the princes and princesses don’t have flush toilets either, but they at least have professional wipers to clean them afterward.

BELINDA: Like I said, being a peasant stinks! (sniffs Tim and makes a face)

TIM: There is one way a peasant can change his lot in life. It’s ridiculously, terribly, insanely dangerous. But if you’re smart, brave, confident –

BELINDA: And if you don’t die in the process . . .

TIM: This is the story of how I took that shot.

TIM: (Pg 9-13) My story begins with a princess . . . Princess Grace, who lives in the next kingdom. (gazes at her adoringly until she begins to sing)

PRINCESS: (singing – off key and badly and continues during Tim’s next line)

TIM: (making a face in response to her singing, covers ears) People said she had a voice like an angel, and that when she sang woodland creatures would gather around and gaze at her adoringly. (shakes head) You can’t believe everything you hear.

PRINCESS: AIEEEEE!! (she is snatched away by a monster)

TIM: Princess Grace was snatched away by a stinx. Not a sphinx. A stinx!

BELINDA: It has the left side of a lion, the wings of a bat . . .

TIM: . . . and the right side of an entirely different lion who doesn’t get along with the first.

BELINDA: It’s always in an incredibly bad mood and has a smell –

TIM: A malodorous stench – that keeps anyone from coming within 5 miles of it.

BELINDA: (Pg 15-17) Prince Ruprecht had a serious crush on Princess Grace. He decided to defeat the stinx, rescue the princess and win her hand in marriage -- along with all of her money.

TIM: There were just two problems: 1) Ruprecht was a coward

BELINDA: And 2) He didn’t have any knights to join him on his quest. His sinister adviser, Nerlim, came up with a dastardly plan. It required someone they could take advantage of. Basically, it required a sucker.

TIM: That’s where I come in! (both begin chopping wood) (Pg 21) I was chopping wood with Belinda when we heard the news. Belinda was not supposed to be chopping wood at all, because she was a girl. (Pg 23) [And] while I was annoyed by my lack of options in life, Belinda’s options were even worse: making dinner, scrubbing floors, taking care of children and if they were princesses . .

BELINDA: Getting abducted by mythical creatures! (laughs)

TIM: If a girl wasn’t born royal, she had two career choices: housewife or witch. (Belinda cackles) We were in the woods near the castle when the town crier came along.

TOWN CRIER: (Pg 25) (unrolls a scroll and begins reaching; actually sobbing) Princess . . . WAAAHHHH . . . Grace . . . AAAUUGGHH . . . has been . . . BOOHOOHOO . . . taken!

TIM: (Pg 26) (grabs the scroll and reads aloud) Kidnapped by a stinx . . . looking for brave men to become knights and join me to rescue Prince Grace . . . Have a nice day – Prince Ruprecht

BELINDA: (gasps with excitement) Help convince Prince Ruprecht that I’m a boy! I’ll tuck my ponytail under my hat, steal some boy’s clothes and act dumber than usual. (spits and scratches her butt)

TIM: (Pg 34) (considering) Belinda was smarter and braver than anyone I knew. I couldn’t imagine anyone better to have by my side. (to Belinda) I’ll do it!

BELINDA: (Pg 43) (to audience) We were going on a quest! *****

TIM: (Pg 58) The whole town came to see us off and cheered for Ruprecht as he bravely let the way. (Ruprecht smiles regally and waves to the crowd) (Pg 60-61) However, once we were aways from the town . . .

RUPRECHT: (dropping his façade and whining) How much farther is it? This is boooooring. (to Nerlim) Can’t you just do some magic and get us there instantly?

NERLIM: Um . . . no. . . [but] I have a map! (unfurls another scroll)

BELINDA: We had always been told Nerlim was a great and powerful wizard, but the person who told us that was Nerlim himself. He was always proclaiming things like:

NERLIM: Behold! I am Nerlim, the great and powerful wizard! Do not cross me, or I shall turn you into a newt!

BELINDA: (looks to left, the right, then whispers) I had never seen him turn anyone into a newt.

NERLIM: BEHOLD! (makes a grand gesture)

BELINDA: (Pg 73) We’re wasting time. Are we going to rescue the princess or not? (to audience)

TIM: (making small talk as they walk) I was hoping we’d have a break before encountering something doom-y. Like maybe the Fields of Joy or the Path of Pleasantness. . . [but] we headed into the Forest of Doom. (intimidating sound effect)

BELINDA: (Pg 79-80) This river doesn’t look so bad. And look – there’s even a raft!

NERLIM: Wait! This is called the River of Doom. Why would it be called the River of Doom if there wasn’t any doom?

RUPRECHT: Maybe it was a marketing thing? My uncle, King Snodgrass discovered a beautiful place to build a kingdom, but he didn’t want anyone invading him, so he named it Plague City and now everyone avoids it like the plague.

NERLIM: I heard that place was a cesspit!

RUPRECHT: Exactly! It’s all marketing! This river looks fabulous (sing the last word)! ******

TIM: (Pg 121-122) The stinx’s lair wasn’t hard to find. All we had to do was follow the smell, which could only be described as: HOLY COW THIS IS THE MOST HORRIBLE, DISGUSTING, AWFUL STENCH I HAVE EVER ENCOUNTERED ON EARTH!

BELINDA: (looking incredulously at Tim – then speaks to the audience, holding her nose) Luck appeared to be on our side. The stinx wasn’t at home,

TIM: But we could see the distant form of Princess Grace far across the cave.

RUPRECHT: (Pg 124-126) (also holding his nose) Beer not, bear baidin! I’ll save you! (rushes cross-stage)

TIM: He dashed across the cave, swept the princess up in his arms and then . . . her head fell off! (all scream and cover their eyes- Tim peeks then approaches) [We] steeled ourselves for the sight of some disgusting carnage but . . . (picks up the body) It’s a doll!

PRINCESS GRACE: (stepping from the shadows) Hi there! (all scream) I didn’t mean to scare you. The stinx didn’t actually want to steal me. It only wanted a dress for its doll. I just happened to be wearing the one it liked best.

TIM: [We] had plenty of follow-up questions, but before we could ask them, a shadow fell over all of us.

BELINDA: Our luck seemed to have run out.

TIM: The stinx was home! (Pg 127-129) [We] turned around slowly, expecting to find ourselves face-to-face with he most vicious, terrifying, ill-tempered beast . . .

STINX: (poses with large doe eyes, flaps its wings gently and makes a purring sound)

BELINDA: Awwwww! It’s a baby!

NERLIM: And it’s adorable!

STINX: (flaps over to the doll, picks it up notices the head is missing and starts to cry)

PRINCESS GRACE: Don’t worry, Fluffy! It was just an accident.

TIM: (Pg 130-133) So you weren’t being held prisoner her? You could have left at any time? Why didn’t you?

PRINCESS GRACE: (pauses to think) Well, when a princess gets into trouble, she’s not supposed to rescue herself. She’s supposed to wait for a brave and handsome prince to rescue her – and once he does, they look into each other’s eyes and fall madly in love – and possibly sing a delightful song about it.

TIM: You could have rescued yourself at any time . . .

BELINDA: (righteous indignation) Society has taught you that you had to wait for a man to come and save you? You have to be kidding me! This whole idea that you shouldn’t be able to rescue yourself because you’re a woman is garbage.

TIM: Women can do anything that men can.

RUPRECHT: (asserting his dominance) I am the Brave Prince Ruprecht and I have saved you from the vile stinx! You are only a woman, while I am a man! It is only right for you to fall madly in love with me! (laughing mockingly)

PRINCESS GRACE: (angrily) But you didn’t save me . . . (whacks him with Fluffy’s doll; Ruprecht is knocked out cold – to others) (Pg 141) There’s no way I’m marrying that guy. He’s a jerk!

(spits and scratches her butt) *****

TIM: So that’s how I became a knight and how Belinda became one too. But [we] learned some things.

BELINDA: Princes aren’t always brave and honorable

TIM: Some beasts aren’t nearly as vicious and mean as people say they are.

BELINDA: Princesses don’t always need a hero to rescue them. And if they do, they’re under no legal obligation to fall in love! (spits and scratches butt)
```

---

## IC-0884: One Tennis Shoe

- Title: One Tennis Shoe
- Author (byline): Shel Silverstein
- Work: An Adult Evening of Shel Silverstein
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: March 2003
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: HARVEY, SYLVIA
- Teaser before the introduction: Yes
- Spoken words (computed): 1662
- Already set (do not supply): none

### Source block (context only)

```text
Author: Shel Silverstein
Book: An Adult Evening of Shel Silverstein
ISBN: 978-0822218739
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): March 2003
```

### Introduction (context only: never use it for content warnings)

```text
TOGETHER: One Tennis Shoe by Shel Silverstein
```

### Performance text (classify this)

```text
HARVEY: This is not going to be easy to say. It’s not an easy subject to discuss –

SYLVIA: What is it? What? What? Are you sick? Are you --?

HARVEY: I’m fine –

SYLVIA: You’re having an affair – you’re in love with somebody else –

HARVEY: No, I’m fine – I love you –

SYLVIA: Well, then what?

HARVEY: I can’t – say it – I’ve got to say it – I’m going to say it – you – are –becoming – a –

SYLVIA: Yes – yes – what? I’m becoming a what? I’m becoming a nag? I’m becoming a bore? What?

HARVEY: Worse.

SYLVIA: Nothing is worse than a bore. Harvey – what? What am I becoming?

HARVEY: You – are becoming a – you are turning into a – a – bag lady.

SYLVIA: A bag lady –

HARVEY: Yes. That’s the hardest thing I’ll ever have to say.

SYLVIA: I’m turning into a bag lady.

HARVEY: Yes, I’m afraid you are

SYLVIA: I assume you mean one of those crazy old raggy ladies who pick things out of garbage cans and carry all their clothes in shopping bags and have lice in their hair and talk to themselves – I assume we’re talking about the same ladies.

HARVEY: I didn’t say you had lice in your hair.

SYLVIA: But you did say I was a bag lady.

HARVEY: I said turning into – not was –

SYLVIA: Turning into a bag lady – well, that’s pretty much like turning into a werewolf, isn’t it?

HARVEY: Please – I’m just trying to –

SYLVIA: You are trying to tell me I’m a bag lady.

HARVEY: It’s been evident for some time – you’ve been showing signs for quite some time.

SYLVIA: Signs –

HARVEY: Indications – symptoms – manifestations –

SYLVIA: Of becoming a bag lady –

HARVEY: Yes.

SYLVIA: There’s no chance that you could be mistaken – you’re sure. Well, I think I’d like a second opinion.

HARVEY: I’m serious about this.

SYLVIA: Harvey – look at me. Tell me – look at me, Harvey – wouldn’t you say I was a little too young to be a bag lady? Maybe a little too old to be queen of the prom – but just a teensy weensy too young to be an old bag lady –

HARVEY: You think old bag ladies started out as old bag ladies? They started out as young women and then –

SYLVIA: And then they went to a wild party and somebody slipped them a shopping bag and it was all over.

HARVEY: I’m trying to make you understand –

SYLVIA: That I am a bag lady – because I am carrying a singular shopping bag – a Bloomingdale’s shopping bag – that makes me – a bag lady – oh – Harvey – you are such a schmuck.

HARVEY: It’s not because of carrying a shopping bag – it is because of what’s in the bag –

SYLVIA: Well I’m sorry if the contents of my bag don’t meet your standards – from now on I’ll try to carry only Gucci shoes and Pierre Cardin –

HARVEY: I’m not talking about that – I’m telling you what not to carry.

SYLVIA: What not to carry – what should I not carry, Harvey? Tell me and I’ll stop carrying it – tell me – tell me –

HARVEY: A sweater. And a plastic raincoat-

SYLVIA: A sweater and a raincoat make me a bag lady.

HARVEY: And a tennis shoe - shoe singular – one shoe. Why are you carrying one tennis shoe?

SYLVIA: I’m taking it down to the Bowery – to meet my wino lover – my one-legged wino lover – on Avenue B.

HARVEY: May I Inquire about the picture frame?

SYLVIA: It’s a picture frame – beveled wood – probably pine – approximately nine by twelve with a wire –

HARVEY: Why the picture frame?

SYLVIA: Why indeed – how about to hang a picture with? How about that?

HARVEY: Why did you pick it up – out of the garbage can? That’s what I –

SYLVIA: Not out of the garbage can – it was next to the can – leaning against the can – not touching the garbage.

HARVEY: Why did you pick it up from next to the can?

SYLVIA: Well, how can I hang a picture in it if I didn’t pick it up?

HARVEY: Why didn’t you buy a frame?

SYLVIA: Why buy a frame when this is a perfectly good frame?

HARVEY: That somebody threw away. And the couch cushion –

SYLVIA: It’s a perfectly good cushion – I can use it on my desk chair.

HARVEY: So you just took it.

SYLVIA: When this cushion is covered in a blue floral patter it will be so –

HARVEY: And the magazines – all the magazines –

SYLVIA: Why are you attacking me like this? What’s really bothering you?

HARVEY: This – this is what’s really bothering me – what could bother a man more than seeing his wife collecting picture frames and tennis shoes and –

SYLVIA: Well don’t forget the grapes while you’re at it.

HARVEY: You have grapes in there?

SYLVIA: I have everything in here – I’m a bag lady, aren’t I?

HARVEY: You are a bag lady – you say you have grapes and a tennis shoe in there like it’s perfectly normal – it is not normal – you are a bag lady.

SYLVIA: A moment ago I was becoming a bag lady – now I am a bag lady.

HARVEY: A moment ago I didn’t know about the grapes.

SYLVIA: The grapes make me a bag lady.

HARVEY: The grapes and the raincoat and the tennis shoe –

SYLVIA: Stop harping on the tennis shoe – if the tennis shoe offends you I’ll get rid of it – There – all right?

HARVEY: And the rest of the stuff –

SYLVIA: You want me to throw it all away? I will – I can just leave the bag here and walk away. . . Except for the picture frame – We can leave the rest right here –

HARVEY: Sylvia, do you not see what is happening to you?

SYLVIA: What is happening to me is you – you’re attacking me –

HARVEY: I’m trying to reach you – I’m trying to make you see what you’re doing.

SYLVIA: I’m not doing anything. I just found a nice little picture frame and you turn it into a –

HARVEY: We can stop this now – if we’re aware of it we can nip it in the bud –

SYLVIA: I don’t see what needs nipping – what? What am I doing?

HARVEY: Will you do me a favor? One favor.

SYLVIA: What is it?

HARVEY: Open your purse.

SYLVIA: Why?

HARVEY: As a favor to me – as a whim – Will you open your purse?

SYLVIA: You think there’s another tennis shoe in my purse?

HARVEY: Will you - open your purse? Will you open your purse?

SYLVIA: No. A woman’s bag – purse – is a personal thing –

HARVEY: I’m going to open this purse –

SYLVIA: You will not find another tennis shoe.

HARVEY: (Opens purse – looks away – then looks at her – he extends purse toward her) Look –

(She looks away) Look- (She darts a glance) Please look at this purse – (She nervously looks) What do you see? What? What do you see in your purse? (Sylvia mumbles) What? (She mumbles again) Speak out – let me hear you –

SYLVIA: Oatmeal – oatmeal! All right?

HARVEY: Oatmeal!

SYLVIA: Yes – are you happy now? Are you satisfied – oatmeal!

HARVEY: Cooked oatmeal.

SYLVIA: Yes – cooked oatmeal – cold cooked oatmeal – you are vicious – you knew there was oatmeal in that purse!

HARVEY: I want you to know it. I want you to see it.

SYLVIA: I see it – I see it.

HARVEY: Now – Why? – Why – is your purse filled – filled to the brim with old, cold, wet, cooked oatmeal. Why, Sylvia, why?

SYLVIA: I don’t know.

HARVEY: Do you want a purse full of oatmeal?

SYLVIA: No –

HARVEY: Does any woman want a purse full of cooked oatmeal? Does anybody need that?

SYLVIA: No –

HARVEY: Then why is it there, Sylvia?

SYLVIA: I – don’t know.

HARVEY: It’s because you put it there, didn’t you.

SYLVIA: I’m so embarrassed.

HARVEY: And you got it where?

SYLVIA: Please, you’ve made your point – I can’t –

HARVEY: Where did you get the oatmeal? Did you cook it this morning at home? Did you cook it and then pour it in your purse?

SYLVIA: No.

HARVEY: Then you found it – somewhere.

SYLVIA: Stouffers.

HARVEY: Stouffers – You went into Stouffers for breakfast and you – And you saw a bowl of oatmeal on the next table and reached –

SYLVIA: On the same table – on the table where I sat down - They hadn’t cleared the table yet.

HARVEY: You sat down at a dirty table.

SYLVIA: It was crowded – they were busy.

HARVEY: And you emptied out the bowl into your purse.

SYLVIA: I didn’t empty it – I put it in my purse – all of it.

HARVEY: The bowl too – Sylvia – What does this make you?

SYLVIA: The oatmeal?

HARVEY: The oatmeal and the hubcap and the ketchup bottle and the chicken bones – Chicken bones. Sylvia, you’re an intelligent woman – what does this make you?

SYLVIA: A – bag – lady? I don’t want to turn into a bag lady, Harvey – I don’t want to push a supermarket cart down the street talking to myself and screaming at everybody – I don’t want to sleep in a doorway.

HARVEY: You’ll never sleep in a doorway –

SYLVIA: This is how it starts – the oatmeal – and shopping bags – then talking to myself, then screaming at people on the street and rummaging through garbage cans and begging for money and not bathing and weaving things into my hair and growing a moustache and drinking wine and sleeping in doorways and getting arrested – Oh my God, Harvey, don’t let them arrest me – don’t let me sleep in the doorway, please, Harvey – please –

HARVEY: Don’t get hysterical –

SYLVIA: And if I start weaving that crazy stuff into my hair you’ve got to stop me – slap me –

HARVEY: I could never slap –

SYLVIA: You’ve got to be forceful, Harvey. They have no homes – they prowl the streets – they don’t get their hair done – they don’t have to bathe – they don’t have to shave their legs – they don’t worry about it – No cooking to do – no house to clean – no man to – consider.

They scream out “Hey buster, watch your fender – you son-of-a-bitch – Watch out, you rotten creep – pompous self-righteous – Kiss – me.” (Slap) Ow! Thank you, Harvey – I’m leaving that bag right there – we can go home. I’m all right now!

HARVEY: I jut wanted you to be aware of –

SYLVIA: I’m grateful – you saved me, I’m lucky to have you, Harvey. I’m going to take this sandwich home for later –

HARVEY: Sylvia. . .

SYLVIA: That’s all right – I don’t need it. Wait a minute – what if they see we’re leaving the bag – what if the waitress sees – and shouts – “Hey lady, you’re forgetting your bag” – I’d die of embarrassment, Harvey, I’ll tell you what – I’ll take it outside and we can dump it in the nearest trash basket – now, I know there’s a large basket over on Third Avenue and Fifty- Seventh – oh, wait – there’s a better one on Fifty-Ninth Street – we can just -
```

---

## IC-0885: Opening

- Title: Opening
- Author (byline): Matthew Kelty
- Work: Off Off Broadway Festival Plays (32nd Series)
- Publisher: Samuel French, Inc.
- Publication date as stated: October 2010
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: SELZNICK
- Teaser before the introduction: No
- Spoken words (computed): 1452
- Already set (do not supply): none

### Source block (context only)

```text
Author: Matthew Kelty
Book: Off Off Broadway Festival Plays (32nd Series)
ISBN: 978-0573660238
Publisher: Samuel French, Inc.
Date (Month/Year): October 2010
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: The year is 1939 and Loew's Grand Theater in Atlanta, Georgia, has been selected as the site for the premiere of Gone with the Wind.

ACTRESS: As the date of the premiere approaches, all the black actors are notified that they have been barred from attending.

ACTOR: Ads depicting black actors are also forbidden under the Jim Crow laws.

ACTRESS: This selection shows the complex dynamic between one of the supporting actress of the film, Hattie McDaniel . . .

ACTOR: (Who went on to become the first black actress to win an Oscar for her role in the Gone with the Wind)

ACTRESS: . . . and David Selznick. the producer, as he makes Hattie aware of the restrictions that have been placed on the . . .

TOGETHER: Opening by Matthew Kelty
```

### Performance text (classify this)

```text
(Lights fade up. DAVID O. SELZNICK sits behind a large desk in his studio office, rubbing his forehead with his fingertips. After a moment, he presses a button on his intercom.')

SELZNICK: Sally, could you send Miss McDaniel in, please? (A moment passes. HATTIE McDANIEL enters the office, dressed for a business meeting. She waits for SELZNICK to speak.) Good morning, Hattie.

McDANIEL: Good morning, Mr Selnick.

SELZNICK: Hattie. David. Please.

McDANIEL: Morning, David.

SELZNICK: How are you today?

McDANIEL: I'm fine.

SELZNICK: Good. Good. (Small pause.) I... Listen, Hattie, I just want to thank you again for your wonderful work on the film.

McDANIEL: Thank you, Mr. Selzuick.

SELZNICK: David.

McDANIEL: Thank you, David.

SELZNICK: I mean, you're practically a co-star in the film - not really supporting at all.

McDANIEL: I'm glad you're pleased. Did you ask me to come in today so that you could thank me for my work?

SELZNICK: Yes.

McDANIEL: (Turning to leave:) Well, then. ..

SELZNICK: I mean, that wasn't the only reason, but yes, I... (As McDANIEL turns back to him:) I... Yes, I wanted to thank you. (Small pause.) You're wondering why we're here.

McDANIEL: I think I know, to tell the truth.

SELZNICK: You know.

McDANIEL: I think that I do. (Pause.)

SELZNICK: Well then for God's sake don't make me

McDANIEL: I'm just hoping that I'm wrong.

SELZNICK: Hattie ...

McDANIEL: (Continuing:) I mean, I'm praying that I'm wrong.

SELZNICK: This isn't something we can

McDANIEL: Why am I here today, Mr. Selznick? (Pause.)

SELZNICK: I've been talking to one of our boys down in Atlanta. (No response.) There's been a problem with the programs for the premiere. (No response.) Some of the people - at the theatre and at the print house - they were unhappy with your picture. Unhappy that it was there. They didn't think it would be appropriate for you and Butterfly to be on the cover of the program.

McDANIEL: Are we inside the program?

SELZNICK: We're working on that. Certainly, you'll be on the programs in Los Angeles, New York ... It's just in Atlanta. (Small pause.)

McDANIEL: Well, thank you for asking me. (Turning to go:) I don't know what Butterfly will say, but if you need to take my-

SELZNICK: Hattie, stop. (McDANIEL turns back around.) Please. Just let me finish. Let me say what I have to say. (She stares at him and waits.) We've been talking with the theatre, trying to determine where the cast will sit, where they'll enter. (Small pause.) They've told us that the theatre ... It's segregated. The black actors won't be seated with the rest of the cast. You'll have to enter and exit separately, use separate restrooms - it's crazy, I know, it's ridiculous, but... The restaurant, too. The banquet before the premiere. They won't serve you. (Small pause.) You already know all of this.

McDANIEL: It's Hollywood, David. People talk. (Small pause.)

SELZNICK: I don't want to see you treated badly, Hattie.

McDANIEL: Then don't let them treat me badly, David.

SELZNICK: I think it's just best for everyone involved if –

McDANIEL: Everyone?

SELZNICK: Yes, everyone, if you don't attend the premiere.

McDANIEL: How would that be better for me?

SELZNICK: Do you really want to be turned away at the door, Hattie? With all the press there watching? That's embarrassing for us, humiliating for you -

McDANIEL: They wouldn't do it. Not with people taking pictures.

SELZNICK: They're already making us change the program.

McDANIEL: You could tell them, just tell them. They'd let me in.

SELZNICK: And the public would stream out the doors, while the cameras snapped. We've sunk a lot of money into this movie; we can't have people running out of the premiere. It'll be in every paper in the country. (Pause.)

McDANIEL: (With mock sincerity:) Maybe I could go, and then leave once we get to the theatre.

SELZNICK: I don't see that that's going to -

McDANIEL: (Continuing, over SELZNICK, allowing the sarcasm to show:) You know, just so Vivienne can have someone to carry her things. I've got a really nice kerchief I could wrap around my head that's not too worn ...

SELZNICK: Hattie, I don't know what else to do.

McDANIEL: Move the premiere. Why does Atlanta get to have the premiere if they're going to treat your actors so badly?

SELZNICK: Half the movie takes place in Atlanta.

McDANIEL: Half The Wizard of Oz takes place over the rainbow, but they didn't put little Judy Garland in a hot air balloon and send her -

SELZNICK: We can't move the premiere. We've already announced it, gotten so far along in the planning. If we move it, it'll be a scandal.

McDANIEL: And it won't be a scandal if your black actors don't go to the premiere? (Small pause.)

SELZNICK: Not to as many people, no. (Pause.)

McDANIEL: Well, I guess I didn't know why you called me in here after all. I thought you wanted to talk about how to handle Atlanta, but instead you just called me in to give me an order about -

SELZNICK: Well, the publicity boys actually think we've come up with something that ... (Small pause.) You know that I appreciate the ... It's a wonderful performance you gave us in this movie, Hattie.

McDANIEL: You said that earlier, yes.

SELZNICK: It's really very fine.

McDANIEL: Thank you.

SELZNICK: I think it's deserving of recognition. From the Academy. I'd like to recommend you for consideration for Best Supporting Actress after we open. (Small pause.)

McDANIEL: Thank you, Mr. Selnick.

SELZNICK: David, please.

McDANIEL: David.

SELZNICK: Hattie. I'd like for you to write me a letter.

McDANIEL: About the nomination? I didn't know you needed a-

SELZNICK: I'd like for you to write me a letter saying that you have a previous commitment, and won't be able to attend the premiere in Atlanta.

McDANIEL: And the one is dependent on the other?

SELZNICK: I've really tried to work with you on this movie, Hattie.

McDANIEL: Oh?

SELZNICK: You wanted us to take "nigger" out of the script, we took it out.

McDANIEL: And left in "darkies." You wanted to leave in "nigger."

SELZNICK: It's a historical document, Hattie.

McDANIEL: It's a movie.

SELZNICK: Still, you wanted it out, and I took it out.

McDANIEL: And you did that just for me? That's so sweet, David. It didn't have anything to do with Butterfly and Oscar coming to you and -

SELZNICK: You sent them over.

McDANIEL: (Continuing:) - or the Hayes Commission or the editorials in the Negro papers protesting you even turning this book into a -

SELZNICK: I am trying to give you a way out of this. Trying to find a graceful way for us to handle this. The premiere is in Atlanta. The theater is segregated. We want to avoid a scandal. If you would just write me a letter saying that you have prior commitments, then -

McDANIEL: Then they win.

SELZNICK: Yes. Yes, they do win. You're right. And I hate to see it. But maybe you win, Hattie, injust a few months. Maybe they win that night, but you win at the Awards in the Spring. The first Negro to win an Academy Award, Hattie. Wouldn't that be something?

McDANIEL: You keep bringing those things up together.

SELZNICK: You said it yourself, Hattie. This is Hollywood. People talk.

McDANIEL: Talk about what?

SELZNICK: All kinds of things besides someone's performance. Like whether they're a team player, whether people would want to work with them again. A good role, that's only half of it. Maybe less.

McDANIEL: You're saying I won't win if I make a fuss about this.

SELZNICK: I'm saying you won't work again. (Small pause.)

McDANIEL: I think that's a little extreme. (Small pause.)You'd ruin my career because I won't write you a letter.

SELZNICK: There are plenty of colored actors in this town who want to work.

McDANIEL: And not enough roles as slaves and mammies to go around.

SELZNICK: What's that quote you gave in that interview, Hattie? Something ... "I've worked as a maid in real life ... The money's better in Hollywood." Something.

McDANIEL: I said I'd rather play a maid than work as one.

SELZNICK: Words to live by. (Small pause.) It's going to get better, Hattie. It'll just take some time. Make sure you're around for when it gets better. (McDANIEL doesn't answer. SELZNICK turns to a stack of papers on his desk and begins to shuffle through them.) Good, good, terrific. Now, I'm going to call one of the boys in from publicity to work with you on the letter. We'll keep it nice and simple, short, nothing we could get caught -

McDANIEL: But David, what if we -

(SELZNICK throws his papers onto the desk in frustration; they scatter all over the desk and the floor.)

SELZNICK: All right, I've had enough. I'm going to get someone to work with you on this. I'll be back in five minutes. If you're here, you're going to have a signed letter on my desk before you go home. If you're not here, don't bother coming back. Do you understand?

(He gets up and leaves without waiting for an answer. McDANIEL looks around the office for several moments. Some of the paper has fallen at her feet; she picks it up and puts it on the desk She looks around some more, then picks up some of the other paj)ers that have fallen. As she places them on the desk, her voice is heard reading the text of McDANIEL S letter to

SELZNICK: The voice continues as she straightens the papers on the desk, and then possibly begins to straighten the office a little. She cleans as the voice continues and the lights begin to fade.)

McDANIEL'S VOICE: Dear Mr. Selznick: Thank you so much for your invitation to attend the world premiere of the studio's new film, Gone with the Wind, in Atlanta next month. I am thrilled to be a part of the film, and hope that the premiere goes well. Unfortunately, I will be unable to attend the premiere, due to circumstances that I'm unable to change. Best of luck in Atlanta. Please accept my apologies. And my deep, deep regrets.
```

---

## IC-0886: The Original Last Wish Baby

- Title: The Original Last Wish Baby
- Author (byline): William Seebring
- Work: The Best American Short Plays 1996-97
- Publisher: Applause Books
- Publication date as stated: Nov 1996
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: SUGGESTED ROLES, ACTOR 1, ACTRESS 1, NARRATOR, DOCTOR, NURSE, EXECUTIVE, ASSISTANT, MAN, MS. KORNFELD, REPORTER, WELDA, CLARA, CUSTOMER #2, CUSTOMER #1, GE PITCHMAN, WOMAN, KORNFELD, NEWSBOY, JUDGE, SURGEON
- Teaser before the introduction: Yes
- Spoken words (computed): 2533
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
ACTOR 1: The Original Last Wish Baby, as researched, recorded and revised by William Seebring. Cleveland, Ohio.

ACTOR 2: Or, more specifically, the third-floor maternity room of the Holy Name Hospital on Cleveland's impoverished west-side where, at precisely seven-oh-one P.M. A baby was born.

ACTOR 2: Not just any baby, but the infamous, original, Last Wish Baby.

ACTOR 1: The baby born without a heart.

TOGETHER: The Original Last Wish Baby by William Seebring
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

SUGGESTED ROLES:

ACTOR 1: Doctor, Assistant, Man, Reporter, Customer #1, GE Pitchman, Woman, Judge

ACTRESS 1: Nurse, Executive, Ms. Kornfeld, Welda, Clara, Customer #2, Newsboy, Surgeon

NARRATOR: Shared role between actors

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

## IC-0887: Othello

- Title: Othello
- Author (byline): William Shakespeare
- Work: Not specified
- Publisher: Washington Square Press
- Publication date as stated: Jan 2004
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: OTHELLO, DESDEMONA
- Teaser before the introduction: No
- Spoken words (computed): 770
- Already set (do not supply): none

### Source block (context only)

```text
Author: William Shakespeare
ISBN: 978-0743477550
Publisher: Washington Square Press
Date: Jan 2004
FORENSICS AWARDS
IL State Qualifier
KS State Qualifier
```

### Introduction (context only: never use it for content warnings)

```text
Othello can be regarded as Shakespeare’s greatest lover. Whilst other plays have waxed and waned in popularity, Othello has remained universally acclaimed since its first performance back in 1604. From its inter-racial marriage theme, to the fatal flaw that mars the character of many . . . Othello is an epic tale of manipulation, passion and sorrow. It is, therefore, regarded as one of the finest literary works, and Shakespeare’s greatest tragedy.

We find Othello and his bride Desdemona alone in their bedchamber. Othello’s first lieutenant, Iago has masterfully manipulated events and perceptions to achieve this chilling confrontation. We’ve prepared . . . Othello by William Shakespeare.
```

### Performance text (classify this)

```text
OTHELLO: It is the cause, it is the cause, my soul.
Let me not mane it to you, you chaste stars.
Ti is the cause. Yet I’ll not shed her blood,
Nor scar that whiter skin of hers than snow,
And smooth as monumental alabaster.
Yet she must die, else she’ll betray more men.
Put out the light, and then put out the light.
If I quench thee, thou flaming minister,
I can again thy former light restore
Should I repent me. But once put out thy light,
Thou cunning’st pattern of excelling nature,
I know not where is that Promethean heat
That can thy former light relume.
When I have plucked (the) Rose,
I cannot give it vital growth again.
It needs must wither. I’ll smell (it) on the tree.
O balmy breath, that dost almost persuade
Justice to break her sword! {He kisses her}
One more, one more.
Be thus when thou art dead, and I will kill thee
And love thee after.
One more, and (this) the last.

(He kisses her)
So sweet was ne’er so fatal. I must weep,
But they are cruel tears. This sorrow’s heavenly:
It strikes where it doth love. She wakes.

DESDEMONA: Who’s there? Othello?

OTHELLO: Aye, Desdemona.

DESDEMONA: Will you come to bed, my lord?

OTHELLO: Have you prayed tonight, Desdemona?

DESDEMONA: Aye, my lord.

OTHELLO: If you bethink yourself of any crime Unreconciled as yet to heaven and grace, Solicit for it straight.

DESDEMONA: Alack, my lord, What may you mean by that?

OTHELLO: Well, do it, and be brief. I will walk by. I would not kill thy unprepared spirit. No, (heaven) forfend! I would not kill thy soul.

DESDEMONA: Talk you of killing?

OTHELLO: Aye, I do.

DESDEMONA: Then heaven have mercy on me.

OTHELLO: Amen, with all my heart.

DESDEMONA: If you say (so) I hope you will not kill me.
And yet I fear you, for you’re fatal then
When your eyes roll so. Why I should fear I know not,
Since guiltiness I know not, but yet I feel I fear.

OTHELLO: Think on thy sins.

DESDEMONA: They are loves I bear to you.

OTHELLO: Ay, and for that thou shall die.

DESDEMONA: That death’s unnatural that kills for loving.
Alas, why gnaw you so your nether lip?
Some bloody passion shakes your very frame.
These are portents, but yet I hope, I hope
They do not point on me.

OTHELLO: Peace, and be still.

DESDEMONA: I will so. What’s the matter?

OTHELLO: That handkerchief Which I so loved, and gave thee, thou gav’st Cassio.

DESDEMONA: No, by my life and soul! Send for the man, ask him.

OTHELLO: Sweet soul, take heed, take heed of perjury. Thou art on thy deathbed.

DESDEMONA: Ay, but not yet to die.

OTHELLO: Presently.
Therefore confess thee freely of thy sin.
For to deny each article with oath
Cannot remove nor choke the strong conception
That I do groan withal. Thou art to die.

DESDEMONA: Then Lord have mercy on me!

OTHELLO: I say “Amen.”

DESDEMONA: And have you mercy, too. I never did
Offend you in my life, never loved Cassio
But with such general warranty of heaven
As I might love. I never gave him token.

OTHELLO: By heaven, I saw my handkerchief in ‘s hand! O perjured woman, thou dost stone my heart And mak’st me call what I intend to do A murder, which I thought a sacrifice! I saw the handkerchief!

DESDEMONA: He found it, then. I never gave it him. Send for him hither. Let him confess a truth.

OTHELLO: He hath confessed.

DESDEMONA: What, my lord?

OTHELLO: That he hath used thee.

DESDEMONA: How? Unlawfully?

OTHELLO: Aye

DESDEMONA: He will not say so.

OTHELLO: No. His mouth is stopped. Honest Iago hath ta’en order for ‘t.

DESDEMONA: O, my fear interprets. What, is he dead?

OTHELLO: Had all his hairs been lives, my great revenge Had stomach for them all.

DESDEMONA: Alas, he is betrayed and I undone. {she weeps}

OTHELLO: Out, strumpet! Weep'st thou for him to my face?

DESDEMONA: Banish me, my lord, but kill me not!

OTHELLO: Down strumpet!

DESDEMONA: Kill me tomorrow, let me live tonight.

OTHELLO: Nay, if you strive –

DESDEMONA: But half an hour!

OTHELLO: Being done there is no pause.

DESDEMONA: But while I say one prayer!

OTHELLO: It is too late. {He smothers her}
What noise is this?—Not dead? Not yet quite dead?
I that am cruel am yet merciful.
I would not have thee linger in thy pain.
So, so.
Who’s there?
Yes. ‘Tis Emilia.—By and by.—She’s dead.
‘Tis like she comes to speak of Cassio’s death.
The noise was here. Ha, no more moving?
Still as the grave. Shall she come in? Were ‘t good?
I think she stirs again. No. What’s best to do?
If she come in, she’ll sure speak to my wife.
My wife, my wife! What wife? I have no wife.
```

---

## IC-0888: Out of Control

- Title: Out of Control
- Author (byline): Mary Krell-Oishi
- Work: Perspectives: Relevant Scenes for Teens, Pg 113-122
- Publisher: Meriwether Publishing
- Publication date as stated: March 1997
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MARY, BILL
- Teaser before the introduction: Yes
- Spoken words (computed): 1567
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mary Krell-Oishi
Book: Perspectives: Relevant Scenes for Teens, Pg 113-122
ISBN: 978-1566080309
Publisher: Meriwether Publishing
Date (Month/Year): March 1997
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Alarming numbers of teens experience and accept abusive behavior in dating relationships. Many teens also feel physically and sexually threatened.

ACTRESS: 1 in 5 teens who have been in a serious relationship report being hit, slapped or pushed by a partner.

ACTOR: Dating abuse can happen to anyone, at any age, no matter what race or religion they are, and no matter what their level of education or economical background.

ACTRESS: Dating abuse isn't an argument every once in a while, or a bad mood after a bad day. Dating abuse is a pattern of controlling behavior that someone uses against a girlfriend or boyfriend.

ACTOR: Abuse can cause injury and even death, but it doesn't have to be physical. It can include verbal and emotional abuse - constant insults, isolation from family and friends, name calling, controlling what someone wears-and it can also include sexual abuse.

TOGETHER: Out of Control by Mary Krell-Oishi
```

### Performance text (classify this)

```text
(BILL and MARY give their points of view about their breakup. Note: All ". . . " mean the characters pick up the line before the end of the preceding sentence.)

BILL and MARY: (Pg 113-122) There was nothing I could do. You don't understand. You weren't there.

MARY: He was out of control. . .

BILL: She was out of control. . .

MARY: He was like a crazy man. I was truly frightened. . .

BILL: Frightening. That's the only word I can think of. She came at me like a crazy woman. . .

MARY: The guy is crazy.

BILL: I just went to see how she was; I was concerned. Hey, we were together for a long time. It's natural. . .

MARY: It's unnatural. He was checking up on me. He always did. He never trusted me. That's why I broke it off with him. . .

BILL: I broke it off with her. She said she couldn't trust me. I don't know where that came from. But I wanted to make sure she was OK.

MARY: He was OK at first. Then, jeez, all hell broke loose. He came over about ten o'clock that morning. . .

BILL: I went over about ten o'clock that morning. She was alone. . .

MARY: I was alone.

BILL and MARY: That made me a little nervous. . .

MARY: Being alone with him, I mean. . .

BILL: I mean, I never knew what to expect. . .

MARY: The whole thing was completely unexpected. . .

BILL: I just wanted to see how she was. . .

MARY: I was sitting on the chair, reading a book and there was a knock at the door. (Her version of the scene begins.)

BILL: Anybody home?

MARY: (Quietly) Oh, shit. (Out loud) Just a minute. (She lets him in.) Hey, how you doin'?

BILL: Are you alone?

MARY: Uh. Yeah. But my parents will be back soon.

BILL: Oh, yeah? I heard they were on vacation in Mexico.

MARY: Oh. Yeah, well, they might be coming home early.

BILL: Uh-huh. So, can I sit?

MARY: Sure. I guess. Really, though, you can't stay long.

BILL: No?

MARY: No. See, I really shouldn't have anyone here without my parents being home. So. . .

BILL: So? I have to leave soon? Is that what you're saying?

MARY: Well, yes, I guess it is.

BILL: Are you expecting someone else?

MARY: No, I'm not.

BILL: So, you're here. Alone. Not waiting for anyone?

MARY: Please leave.

BILL: Since when do you tell me when to come and when to go?

MARY: Bill, I think you should leave now.

BILL: Do you? Do you really?

MARY: Come on, Bill, Just go.

BILL: I'll go when I'm ready. And I'm not ready. So watch your mouth. Don't tell me what to do. I never liked when you told me what to do. Never. Or don't you remember that?

MARY: I know, Bill,

BILL: I don't think you do. Maybe you need a little reminder, huh? (He crosses to her threateningly, then freezes.)

MARY: (Coming out of the scene) It was always like that. He was always trying to control me, threatening me, grabbing me. (She moves back into the scene.)

BILL: (Coming out of the scene) She had called me a couple days before and sounded down, so I just wanted to say hi. I mean, I'm not a complete ass. I was concerned. So I went over there. She seemed happy to see me at first. (He moves back into the scene.)

MARY: (Hugging him) Bill, Hi.

BILL: (Hugging back, but being the first to pull away) Hey, you OK?

MARY: I am now that you're here.

BILL: I just wanted to say hi, see how you were.

MARY: I'm glad you're here. Stay a while.

BILL: I can't stay long.

MARY: My parents aren't here. I don't expect them back for days. They're out of the country. You can stay as long as you like.

BILL: Oh. Well. So, you doing all right?

MARY: Yeah. Sort of. You want to sit down with me on the couch?

BILL: No. Really, I can only stay a minute.

MARY: Why? No one is here except us. Just us, alone.

BILL: Yeah. Alone.

MARY: Don't you want to be alone with me?

BILL: It's OK. It's fine. Really. Not a problem. So what have you been doing?

MARY: Doing? You mean since you broke up with me? Since you tore my heart out and threw it on the ground?

BILL: I guess. Yeah. Uh. . .

MARY: Nothing. I've been doing nothing. Eating, watching TV, waiting, hoping for the phone to ring. . . (She goes to him; he freezes.)

BILL: (Coming out of the scene) It was so obvious she wasn't over me. . .

MARY: (Coming out of the scene) It was so obvious he wasn't over me. . .

BILL: She looked so pathetic. . .

MARY: He looked so angry. . .

BILL: So out of it. . .

MARY: So lost. . . BILL and MARY: I actually felt sorry about the whole situation. . .

MARY: Then he grabbed me. (She goes back into her version of the scene.) What are you doing?

BILL: I'm not doing anything I haven't done before.

MARY: Listen, Bill, that was before. You have no right to touch me, now or ever.

BILL: I told you before, don't tell me what to do.

MARY: I'm simply asking you to keep your hands off me.

BILL: Since when? Since when do you tell guys to keep their hands off you? You think I didn't hear about you and David? Did you think I'd never hear about it? You can't humiliate me like that and think nothing will happen.

MARY: What I do now is none of your business. We broke up. Get over it.

BILL: You bitch. You really imagine I can get over us? I never will. You belong to me, now and forever. (He goes to grab her and freezes.)

MARY: (Coming out of the scene) I knew I was in big trouble. . .

BILL: (Coming out of the scene) Trouble. The girl is trouble.

MARY: He was grabbing me, touching me; it made my skin crawl.

BILL: She couldn't keep her hands off me. Every ime I moved away from her, she'd follow me, holding me. It was freaking me out. I couldn't get away from her.

MARY: (Back in Bill’s version) The phone never rang. But now you're here and everything will be OK. Won't it?

BILL: Listen, Mary. We broke up. You need to get over it. Move on.

MARY: Oh, like you have? I heard about you and Caroline. Did you think I wouldn't? Did you think I'd do nothing about it? You can't humiliate me like that and think nothing will happen?

BILL: What I do now is none of your business. We broke up. Get over it.

MARY: You bastard. You really imagine I can get over us? I never will. You belong to me, now and forever. (She goes to grab him and freezes.)

BILL: It was always that way with her. . .

MARY: He was always like that. . .

BILL: Accusations. . .

MARY: Insinuations. . .

BILL: Constant little remarks. . .

MARY: Little remarks that always sounded like a threat. . .

BILL: A threat. I never knew what she'd do. . .

MARY: He'd do the most bizarre things. . .

BILL: Things that didn't make sense. . .

MARY: Ever since I broke up with him, he's been weird, scary weird. . .

BILL: Ever since I broke up with her, it's scary, how she is. It's hard to explain. . .

MARY: I can't explain it.

BILL: (Back in MARY's version) I'll never let you go. You know that, don't you? Never.

MARY: Bill, I don't know what you expect from me. We were together a long time and our relationship ended. You knew it would. I couldn't allow myself to be treated the way you were treating me.

BILL: I treated you how you deserved to be treated. You asked for it.

MARY: I asked for it? Are you insane? No one asks to be treated like a possession, a thing. I wanted respect and I got abuse.

BILL: I respect people who deserve it. You were a lying, cheating, little slut.

MARY: I never cheated on you. Ever!

BILL: Lying bitch. (He freezes in mid-slap.)

MARY: (She comes out of the scene.) That's how it was - name calling, accusations - then it started into physical abuse. . .

BILL: (Coming out of the scene) The abuse took me by surprise. I mean, what's a guy supposed to do? I've never hit a girl in my life, but when you start getting hit, after awhile you have to defend yourself, right?

MARY: I never did anything. . .

BILL: Nothing would have made me. . .

MARY: He thought it was fine to take any action. . .

BILL: Actions speak louder than words. . . (He goes back into his version of the scene.)

MARY: Why are you here?! Did you come to make me feel worse than I already do? Do you get some sort of perverted pleasure in torturing me?

BILL: Mary, come on. We were together a long time. I'm concerned. I still have some feelings for you.

MARY: Do you? You still have feelings for me?

BILL: I would for anyone I cared about.

MARY: You still care about me?

BILL: Like any friend.

MARY: Friend! Friend! Don't do me any favors. I have all the friends I need.

BILL: I think I better go.

MARY: Fine, get out. (She shoves him.) Go! You son of a bitch. Bastard. (She slaps at him, connecting.)

BILL: (Fending off MARY's physical attack) Hey! That's enough. (He grabs her arms.) Stop!

MARY: (Grabbing his arms, also) Stop! (They both freeze.)

BILL: I told her to stop, but she wouldn't.

MARY: He wouldn't. He wouldn't stop. I didn't know what to do. . .

BILL: What would you do? Just stand there?

MARY: He's bigger and stronger. . .

BILL: She's stronger than she looks. . .

MARY: He grabbed my hands, I couldn't move. . .

BILL: I had to hold her so she couldn't move. . .

MARY: I was so scared. . .

BILL: I was so scared. . .

MARY: It had never been like this before. . .

BILL: Before it had been just her slapping, but now she was, going crazy.

MARY: He was crazy. He pinned me down. . .

BILL: She fell down. . .

MARY: I grabbed whatever I could find. . .

BILL: I felt something hit me on the head. . .

MARY: I hit him on the head. . .

BILL: Things went black, just for a second. . .

MARY: I couldn't see what I was doing.

BILL: Then there was blood in my eyes. . .

MARY: Then his blood fell on my face. . .

BILL: I had to let her go. . .

MARY: He let me go, just for a second. . .

BILL: She got up. . .

MARY: I got up and tried to get away. . .

BILL: She moved. . .

MARY: He grabbed my leg. . .

BILL: I tried to get up. . .

MARY: I fell back against the table. . .

BILL: I couldn't get up. . .

MARY: It was like a slow-motion movie. . .

BILL: Everything just slowed down. Got blurry. . .

MARY: It's all a blur. I hit the table. . .

BILL: I heard a crack on the table. . .

MARY: My head. . .

BILL: Everything was dark. . .

MARY: I could feel the warm sticky blood. . .

BILL: My blood. . .

MARY: My blood. . .

BILL: There was the loud rushing sound of waves. . .

MARY: Waves of nausea. . .

BILL: Waves of fear. . .

MARY: I looked over at him. . .

BILL: I saw her. . .

MARY: Bleeding. . .

BILL: Bleeding. . .

MARY: How did we get here?

BILL: How did this happen?

MARY: I looked and then stared. . .

BILL: I stared. . .

MARY and BILL: And then there was nothing.
```

---

## IC-0889: Owl and the Pussycat

- Title: Owl and the Pussycat
- Author (byline): Bill Manhoff
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: October 1965
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: DORIS, FELIX
- Teaser before the introduction: Yes
- Spoken words (computed): 1420
- Already set (do not supply): none

### Source block (context only)

```text
Author: Bill Manhoff
ISBN: 0573613540
Publisher: Samuel French, Inc.
Date (Month/Year): October 1965
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: Felix is a "writer". He also considers himself an intellectual. He is snobby, elitist, and finicky.

ACTOR: Doris is a prostitute who lives across the alley.

ACTRESS: Felix has basically been spying on Doris with binoculars -- he tells the landlord of her building about her extra-curricular activities and Doris gets thrown out of her apartment.

ACTOR: She finds out that Felix is the one who turned her in - so she comes knocking on his door, dragging a suitcase and her television set - demanding that he put her up until she can find a new place.

ACTRESS: The relationship progresses and Felix decides that Doris is train-able - he starts giving her little tasks - she is supposed to look up a word a day in the dictionary and then use it in a sentence.

ACTOR: Not exactly a match made in Heaven . . . but for Doris and Felix it seems to work

TOGETHER: The Owl and the Pussycat by Bill Manhoff
```

### Performance text (classify this)

```text
DORIS: Read me your story.

FELIX: (Picks up typewriter script) You won’t like it.

DORIS: I’ll love it.

FELIX: (Reading.) Scream –

DORIS: “Scream.” That’s the title, right – “Scream.”

FELIX: Yes.

DORIS: That’s a wild title.

FELIX: Thank you. (Reads) The sun spit morning into Werner’s face – one eyelid fluttered – dragging the soul back screaming from its stealthy flight to death –

DORIS: The sun spit morning into this guy’s face?

FELIX: Yes.

DORIS: You were right.

FELIX: When?

DORIS: I don’t like it. I hate it. The sun spit morning into his face! What right do you have to put down a terrible thing like that in a story – “The sun spit morning in a man’s face.”

FELIX: All right - - you don’t like it – but calm down.

DORIS: You know what you are? Your inflabious (hic)

FELIX: Inflabious?

DORIS: Yeah

FELIX: What does that mean?

DORIS: (thumbing her nose.) Ah ha! How does it feel? I’m not gonna tell you!

FELIX: You just made up a word?

DORIS: How do I know you’re not making up yours?

FELIX: Mine are in the dictionary.

DORIS: That’s your story!

FELIX: I suppose it never occurred to you that as an alternative to getting angry, you might make some attempt to understand whatever it is that confuses you?

DORIS: Why? Why should I? What about people making some attempt to not confuse me? (hic)

FELIX: Because progress does not lie in the pampering of the brainless.

DORIS: Drop - (Hic) dead! Damn it!

FELIX: Hold your breath

DORIS: Hold yours . . .

FELIX: Maybe you can hiccup yourself to sleep.

DORIS: You better not be so funny – people have been known to – (His) die from the hiccups.

FELIX: Drink a glass of water.

DORIS: That never works with me. Only one thing words with me – you gotta scare me.

FELIX: How the devil am I gonna scare a holy terror like you?

DORIS: (Hic.) I get them very deep – it’s a strain on the heart, so stop fooling around and scare me – (Hic.) or I’ll scream (Felix turns and walks around the sofa – suddenly pounces with clawed hands snarling like a tiger.) O come – (Hic) on! (Felix drops down behind sofa – Doris hiccups twice. Felix suddenly appears on all fours around the end of the sofa rising menacingly and hissing like a asnake.) It’s no use. I was expecting it. You have to do it when I’m not – (Hic.) expecting it.

FELIX: Oh, that’s ridiculous! How can I do that? You’re waiting for me to frighten you.

DORIS: Well, mate me – (hic.) forget about it – stupid. Then when my mind is on – (Hic) something else – then do it.

FELIX: When your mind is on something else!

DORIS: Of course, stupid! Change the subject – put me off my – (hic) guard.

FELIX: Some weather we’re having. It’s a wonderful summer, isn’t it?

DORIS: Beautiful (Hic)

FELIX: I think it’s quite a bit warmer than it was last year at this time Don’t you?

DORIS: Come on, will you – you want me to hiccup to death? (hic)

FELIX: I’m putting you off your guard!

DORIS: I’m off my (hic) guard by now. Stupid!

FELIX: You’re expecting it now.

DORIS: I am not (hic) Com on, will you! (Felix gives a hideous roar. Doris looks at Felix for a second, then) You’re right. I was (hic) expecting it.

FELIX: Listen – I’m through- I’m finished – I’m exhausted. I just don’t care. I’m going to bed! (Felix exits to bedroom. Doris turns facing audience)

DORIS: Dirty (hic) fink! (Behind her Felix creeps on tiptoe from the bedroom) Rotten (hic) pervert. I could die for all he cares (hic). I could die right . . . (Suddenly Felix growls and puts his hands around Doris’ neck. Doris jumps in terror. She turns and clouts Felix in the face)

FELIX: What’s the idea!

DORIS: You wanna give somebody a heart attack? You maniac, you wanna kill me?

(Felix takes a deep breath, calms himself and then changes the subject)

FELIX: How many times did you say you used the dictionary today?

DORIS: I don't know.

FELIX: Please go over to the dictionary and look at it closely.

DORIS: [Doris goes and looks at the dictionary] What am I supposed to see?

FELIX: Look at the edges -- at the top --

DORIS: What's this? [Peeling off a strip of scotch tape]

FELIX: That is a strip of Scotch tape. It's been there for two days. Undisturbed. Where were you this afternoon?

DORIS: That's such a nasty thing to do.

FELIX: Where were you yesterday afternoon?

DORIS: I do not care for the tone of your voice.

FELIX: Where did you get the dirty but brand new radio?

DORIS: I'm warning you -- stop it -- this warning will not be repeated.

FELIX: We're not going to fight anymore. We're going to have an honest unemotional discussion.

DORIS: Yeah? So you start out by calling me a liar.

FELIX: I did not call you a liar. I'm not going to lose my temper.

DORIS: You might as well. I'm gonna lose mine!

FELIX: Would you care to tell me what's wrong?

DORIS: What's wrong? You're a creep that puts scotch tape on the dictionary -- you know that word -- "creep"? Used in a sentence: "Fred Sherman is a big creep".

FELIX: [starting at "Fred"] What did you call me?

DORIS: It's your name. Fred -- Freddie -- I thought that would jar your apricots! I found your yearbook from school -- Fred Sherman. You didn't tell me you changed your name, did you? You creep. I'm sorry -- pardon my language, but you are a creep.

FELIX: It's all right -- it's a step up from "fink". Congratulations -- now -- I'd like to hear why you feel you have to sneak out afternoons and lie to me.

DORIS: I just got bored. I had to get out. Look -- I tried. I tried working on hats. I tried looking for a job, right? I tried.

FELIX: Have you been plying your old trade?

DORIS: Have I been what? No, I haven't. I told you I was through doing that.

FELIX: Where'd you get the radio?

DORIS: I collected some money. Somebody owed me some money and they paid me.

FELIX: I see. Why didn't you tell me that?

DORIS: Because I knew you wouldn't believe it. I knew what you'd think.

FELIX: I see.

DORIS: Dont' say "I see", like you were looking through your lousy spy glasses. Listen -- why don't you stop trying to make out like you're a human being? I mean the strain must be terrible -- why don't you just relax and admit you're God and you know all about everything?

FELIX: Why did you have to lie? I just want to know why you lied to me about going out and about looking up words.

DORIS: Because I'm a liar, okay?

FELIX: Why didn't you tell me?

DORIS: Why didn't you tell me you changed your name from Fred to Felix?

FELIX: [ignoring her question] I'm very sad. You had a chance to do something important for yourself and you're quitting. You're not giving yourself a chance.

DORIS: I gave myself a chance -- you had me going there for a while, but it's silly. I'm a dope and that's all there is to it.

FELIX: You're not a dope. You're a bright girl.

DORIS: Not when it comes to dictionaries and the history of philosophy, I'm not.

FELIX: You have a potential capacity for --

DORIS: No, I don't have any potential anything.

FELIX: [losing the fight against his temper] Don't interrupt me -- who do you think is better qualified to judge mental capacity -- you or I?

DORIS: You --

FELIX: Then why are you arguing with me?

DORIS: Felix, I --

FELIX: Would I be wasting my time with you if you didn't have a brain?

DORIS: Felix --

FELIX: Do you think an intellectual such as myself would waste his time with a dumbbell?

DORIS: Felix, I know myself -- you can't tell me --

FELIX: I tell you you're a very intelligent girl, and you'd know it yourself if you weren't so damned stupid!

DORIS: I am not stupid! I've got good healthy everyday brains. I haven't got your kind of brains and I'm glad, because I'm gonna tell you something -- I think your brains are rotten!

FELIX: Ah -- the cat turns inevitably and bares her atavistic fangs.

DORIS: To use those ugly, lonely words nobody else uses -- that's all your brains are good for. To keep people away because you're scared to death of people!

FELIX: She spits in inarticulate fury!

DORIS: You know what your brains are good for? To make up your own lousy little language that the rest of the world can't even understand.

FELIX: Well, all right -- stay with the rest of the world -- don't let anybody make you a foreigner there by teaching you to speak the English language!

DORIS: [going to closet] What a dope I was to listen to you. [Mimicking him] I'm gonna save you, Doris! [In her own voice] You are such a phony. I can't believe it. You don't write for money but you keep sending your junk to magazines, don't you? And you keep getting it sent back, don't you? Meanwhile all you got is a phony job, a phony girlfriend, a phony apartment and a phony bunch of words. [she has taken the suitcase from the closet and started to throw garments into it as she talks]

FELIX: What are you doing?

DORIS: What does it look like I'm doing?

FELIX: Now don't get washed away. Think, Doris, try to understand one basic thing. Try to hold on to what I see in you.

DORIS: [Yelling] You see nothing! You don't see me at all! You don't see anything. Because even your eyes are phony! You are now and forever, a miserable magazine peddler named Freddie Sherman and a lousy writer and you always will be and you wanna know why --? [Hitting him deliberately with every word] Because, The -- sun -- does -- not -- spit!
```

---

## IC-0890: People, Places and Things

- Title: People, Places and Things
- Author (byline): Duncan Macmillan
- Work: Not specified
- Publisher: Oberon Books
- Publication date as stated: March 2016
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTRESS, DOCTOR, EMMA, THERAPIST, MEREDITH, TOGETHER AS GROUP, LAURA, PAUL, MARK
- Teaser before the introduction: Yes
- Spoken words (computed): 1676
- Already set (do not supply): none

### Source block (context only)

```text
Author: Duncan Macmillan
ISBN: 978-1783199099
Publisher: Oberon Books
Date (Month/Year): March 2016
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Recovery from an addiction is a journey between life and death that can only be walked one day at a time.

ACTRESS: Life has to win every single day.

ACTOR: And death only has to win once.

TOGETHER: People, Places and Things by Duncan Macmillan
```

### Performance text (classify this)

```text
Suggested Roles: ACTOR: Doctor, Therapist, Paul, Mark

ACTRESS: Emma. Meredith, Laura

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

DOCTOR: (Pg 24-27) Nina? Nina? (No response) Excuse me, hello.

EMMA: (jittery, nervous, obviously under the influence) Sorry. Yes, that’s me.

DOCTOR: Great. (reviews the intake form) Your name is ‘Nina” and you’re an alcoholic and drug addict.

EMMA: This was a mistake.

DOCTOR: You’re not an alcoholic and drug addict?

EMMA: I’m not saying I’m anything. I just want to get clean, get my certificate and go back to work.

DOCTOR: Certificate?

EMMA: A piece of paper or a signed whatever, something that says I can work. That I’m not a risk.

DOCTOR: Once you complete the grogram we can . . .

EMMA: (interrupting) How long will that take?

DOCTOR: It varies. First, I’ll need to see your results and take a history and psychological examination. (consulting the form) Benzodiazepine, Lorazepam.

EMMA: Valium, yeah. For anxiety. It’s a prescription.

DOCTOR: Detoxing from benzos takes about ten days. You’ll start tonight and tomorrow morning you can begin with Group.

EMMA: I don’t need that; I just need the first thing.

DOCTOR: Nina, the Group is the program. The truth is that it doesn’t take long to get everything out of your body. It’s the behavior that is the important thing to address. We can’t do that until we’ve dealt with the physical symptoms. Then it’s twenty-eight days of therapy. Ideally, it’ll be closer to ninety.

EMMA: Ninety? No, that’s not possible.

DOCTOR: Blackouts . . . Memory loss . . . It says here ‘suicide attempt.’

EMMA: Not a successful one. That’s me. Never seeing anything through. Violin lessons. Diets. Suicide attempts. I never finish what I start.

DOCTOR: Your addiction will fight any progress. It’s a parasite and it will fight for its own survival until you’re dead. But progress is possible. I just need to hear you say that you are willing and motivated to make changes.

EMMA: I know that the next time I drink or use that’ll be it. I’ll be dead. I’m not sure if I knew that until now, until I just literally just said it. But it’s true. It’s going to kill me. (She rubs her eyes) Yes. I need help. Please help me.

DOCTOR: (Pg 39-40) The program works for a lot of people. (Pg 27) Let’s start with your name shall we? Your real name.

EMMA: Emma. (cynical) (Pg 39) If it’s vital to my recovery that I come to believe in a power greater than me – to turn my will and my life over to God and have Him remove my defects of character – if all this depends on me having a spiritual awakening, then we might all just be wasting our time.

DOCTOR: You’re worried about the steps.

EMMA: I’m worried that a trained medical professional can also wear a crucifix.

DOCTOR: I don’t believe the scientific methods disproves the existence of . . .

EMMA: (bitterly interrupting) Of course it does. I really need you to be cleverer than this. Otherwise, I’m going to leave. I’m not powerless. I’m not helpless. I don’t believe addiction is a disease and I’m scared and angered by the suggestion that from now on it’s either eternal abstinence or binge to death. I can’t surrender to a higher power because there isn’t one. There just isn’t. My brother had a brain hemorrhage while reading Pinocchio to a group of five-year-olds. Mark. Hew was two years younger than me and never touched drugs or alcohol. He ran marathons. For charity. I should have died a thousand times, but it was him.

DOCTOR: When did you start using, Emma? (Pg 37) Before you join the Group I need some historical context for your using.

EMMA: (Pg 40-42) If I tell you I was sexually abused or the child of alcoholics, if I tell you I returned from back-to-back tours of Iraq and started to self-medicate; is that the kind of thing you want to hear?

DOCTOR: Is it the truth?

EMMA: No. I never had a brother. And he didn’t die in front of children. He died in his car. Or he was stillborn maybe. Or he grew up and died of old age.

DOCTOR: Do you lie to protect yourself or your addiction?

EMMA: I can’t base my survival on slogans and abstractions and vagueness. I’m not someone who can do Pilates on a beach and mistake relaxation for spirituality. I spent a year in the Far East, but I didn’t find enlightenment, I found slums and sex tourism. I need something definitive. I need to be fixed.

DOCTOR: It doesn’t work like that. It’s a long-term, daily . . .

EMMA: I don’t do long-term.

DOCTOR: You’re going to learn. The strategies you’ve been using just aren’t working. Intellectually inferior as I may be, I’m trying to save your life. Now, sit down. (Emma sits) The Twelve Steps outline the process of recovery. Have you heard the expression “powerless over nouns’?

EMMA: Nouns? As in

DOCTOR: People, places and things. It’s a rewrite of Step One of Twelve. Instead of declaring ourselves powerless over alcohol or drugs, we admit that we are powerless over people, places and things. People who make us want to relapse, places we associate with using and things that reactivate old behavior. When you’re in recovery

EMMA: Back in the real world.

DOCTOR: You’ll need to find a way to handle being in those places, with those people.

EMMA: And those things. I find reality pretty difficult. I find picking up my phone to be a mammoth struggle. The friends who won’t see me anymore. The bombings and beheadings, the moral ambivalence you have to have to just be able to carry on with your day. Drugs and alcohol have never let me down. There are substances I can put into my bloodstream that make the world perfect.

DOCTOR: I can’t force you to stay. I can’t force you to be truthful. I can tell you that the process only works if you are honest. With yourself, with me and with others. Denial is what kills you. (beat) You’ve already come so far Emma. Don’t let that be for nothing. I’d like you to meet the Group. ****** GROUP THERAPY*****

THERAPIST: (Pg 43) Hi. I’m Lydia, one of the therapists here. Why don’t you introduce yourself?

EMMA: Er, okay. Hello everyone I’m . . . Emma.

MEREDITH: (Pg 54) I’m Meredith and I’m a Heroin addict.

TOGETHER AS GROUP: Hello, Meredith.

LAURA: Hello, I’m Laura. I’m an alcoholic.

TOGETHER AS GROUP: Hello, Laura.

THERAPIST: (Pg 43-44) Emma, why don’t you tell us about yourself?

EMMA: Seriously? I have to just jump straight in? (Pg 45-47) (Suddenly the door opens and Paul enters, urgently)

PAUL: I’d like to say something to the Group please.

THERAPIST: Mr. Waverly, I’m sorry but your treatment has been terminated. You can’t be in here.

PAUL: (takes a piece of paper from his pocket and reads) I want to apologize to you all with my whole heart. I know that my behavior here was stupid and dangerous. I smuggled in some substances. Ketamine. (he lowers the paper – this is hard for him) But I don’t’ like begging. I was making progress here. I was doing well. Please. Please give me a second chance. I wouldn’t have used if what happened hadn’t happened.

EMMA: What happened?

PAUL: Robert. My fiancé. My partner of eighteen years. Dead. Heroin. I can’t go home again. It’s not real. I don’t want to die. I want it all to stop.

EMMA: (Pg 48) I’m sorry your fiancé died. My brother died too. The week before I came here. Pills. I found him in the stairwell of our building curled into a ball. He cried blood. I wish I’d died instead. I wish I’d died without having to see him dead. We’re the same.

THERAPIST: Paul, you understand you can’t simply re-join the Group.

PAUL: (looks around, laughs bitterly) None of this is real. When you’re sitting here tonight being all serious, think of me out there. I’ll be having the night of my life. (Paul leaves, beat)

THERAPIST: (Pg 55) Would you like to speak to the Group Emma?

EMMA: No.

MARK: (steps up to fill the silence) (Pg 54) [Hello, I’m Mark] I’m a drug addict. (Pg 58) Amends. That’s the hardest part of this whole thing. I can’t forgive myself for a lot of things, so I can’t expect other to. My eldest sister, she was pouring a bottle of Smirnoff down the sink. Vodka to me was like spinach to Popeye. I didn’t know my own strength. I broke her jaw then stamped on her leg, broke her ankle. She forgave me. (he is finding his hard; beat) My gran. She raised me. Cancer. She was in pain and I (big breath in an out, trying to keep his composure) I took her pain relief. I’d hear her calling out. Screaming. And I’d be like ‘sorry Nan. There’s nothing left.’ Now she’s dead so how do I amend for that?

EMMA: (Pg 60-61) (softly) Hello. I’m Emma. I’m an alcoholic and drug addict.

MARK: I’ve seen you onstage a few time. I remember thinking, she’s going to be great.

EMMA: I used to think that too. With a play you get instructions. Stage directions. Dialogue. Someone tells you where to be and when. You get to live the most intense moments of a life over and over again. You get to practice. For weeks. And you’re applauded. Then you leave through stage door. Back to real life. Audition comes in. Never hear back. You try not to take it personally. But you keep going because sometimes, if you’re really lucky, you get to be onstage and say things that are absolutely true, even if they’re mad-up. You get to do things which feel more real to you, more authentic, more meaningful than anything in your own life. You get to speak poetry . . . (From Antigone) When he shall die, take him and cut him out in little stars, and he will make the face of heaven so fine that all the world will be in love with night, and pay no worship to the garish sun. I played Antigone and every night my heart broke about her dead brother. Then my own brother died and I didn’t feel anything. I’m not avoiding talking to the Group because I’ve got something to hide. It’s the opposite. If I’m not in character, I’m not sure I’m really there. (Pg 63) I’m brilliant at being other people and totally useless at being myself. (Pg 61) I’m nothing. (long beat) (Pg 64) (with growing anger) I’d like to believe that my problems are meaningful. But they’re not. There are people dying of thirst. People living in war zones and here we are thinking about ourselves. As if we can solve everything by confronting our own defects. We’re not defective. It’s the world that’s f****ed. (She steps out of the scene and speaks to the audience) (Pg 60) (softly) Hello. I’m Emma. I’m an alcoholic and drug addict. (Pg 87) (sadly) In rehab they tell you: avoid people who make you want to relapse. Places you associate with using and objects that might be a trigger. People, places and things. That’s basically, you know. . . everything.
```

---

## IC-0891: Post-Its (Notes on a Marriage)

- Title: Post-Its (Notes on a Marriage)
- Author (byline): Paul Dooley and Winnie Holzman
- Work: Laugh Lines: Short Comic Plays
- Publisher: Knopf Doubleday Publishing Group
- Publication date as stated: 2007
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR, ACTRESS, PS
- Teaser before the introduction: Yes
- Spoken words (computed): 1256
- Already set (do not supply): none

### Source block (context only)

```text
Author: Paul Dooley and Winnie Holzman
Book: Laugh Lines: Short Comic Plays
ISBN: 978-0307277138
Publisher: Knopf Doubleday Publishing Group
Date (Month/Year): 2007
```

### Introduction (context only: never use it for content warnings)

```text
Actress: In today’s society, everyone is so busy, it isn’t any wonder than more and more of our communication happens via text message or written message left for our family members to find as we go about our hectic lives. Actor: In Post-Its (Notes on a Marriage) by Paul Dooley and Winnie Holzman, the primary source of communication utilizes that cultural phenomenon of the Post-It. Actress: Here you will find the ups and downs of a relationship that were unexpectedly captured on scraps of paper.
```

### Performance text (classify this)

```text
(There is a chair with a small table and a glass if water on either side if the stage, ala A. R. Gurney's Love Letters. The ACTOR and ACTRESS enter simultaneously from either wing, dressed simply. Each grasps a handful if Post-its as if it were a script. They sit, modestly acknowledging each other and the audience. Each takes out a pair of reading glasses, puts them on. 'The ACTOR lifts his first Post-it to begin ... and reads. Every line is read from a Post-it.)

ACTOR: Had an early meeting, couldn't bear to wake you. Close front door hard or it won't lock. PS: Last night was incredible.

ACTRESS: Helped myself to breakfast. You need milk. PS: Next time, wake me.

ACTOR: Hey, sleepyhead. Tried to wake you. Not easy. Left you some coffee, hope you like it black.

ACTRESS: Thought I should spend at least one night this week at my place. Picked up some milk; you don't have to pay me back.

ACTOR: Off to work, extra set of keys on hall table.

ACTRESS: Darling: Went jogging with Lila. If you go out, we need milk. Wow. I can't believe we're a "we"!

ACTOR: Hon: If you have time, could you pick up my shirts? Ticket on hall table. Thanks. PS: Milk.

ACTRESS: Shirts are in your closet. Your mother called. She seemed surprised to hear my voice. You obviously never mentioned me. (Icy.) Your shirts came to fourteen-fifty.

ACTOR: Gone to florist. Back soon. Hope you liked the chocolates.

ACTRESS: Darling, don't go in the den.

ACTOR: Sweetheart, I understand how much it means to you, but at this stage of our relationship I'm just not ready ... to have a dog.

ACTRESS: (After a beat.) We need Milk-Bones. (Next Post-it.) Your mother called; call her. (Next Post-it.) Did you call your mother? (Next Post-it.) Went to lunch with your mother. Back soon.

ACTOR: Your new best friend my mother called. Call her.

ACTRESS: We need milk. Also, your mom mentioned how much you hate Eugene. I don't think Eugene's so bad. You should hear my middle name. Thank God my mother's dead!

ACTOR: Please do not mention the name Eugene to me ever again. Thank you.

ACTRESS: Shopping list: Pistachio ice cream. Sardines. Those tiny little cheeses that come in that cute little net bag .... They're so adorable, they make me cry.

ACTOR: Darling: I understand how much it means to you, but at this stage of our relationship I'm just not ready-

ACTRESS: We need Pampers. And baby wipes. And we need to get married.

ACTOR: Meet me City Hall, six sharp. You bring old and borrowed; I'll do new and blue. Mom will stay with Eugenia.

ACTRESS: Note to self: Find breast pump.

ACTOR: Take cold shower.

ACTRESS: Lose forty pounds.

ACTOR: Redirect sex drive into career. (Next Post-it.) Home late. Don't wait up.

ACTRESS: Hey, stranger, if you're not too busy, could you call Eugenia tonight, around bedtime? Just to see if she recognizes your voice?

ACTOR: Hon: Sorry about your birthday. PS: I got the raise!

ACTRESS: To the new vice president in charge of marketing. We need milk. Please advise.

ACTOR: Hon: I think we're out of milk. (Next Post-it.) Still no milk!

ACTRESS: If you want it so bad, get it yourself The milk train doesn't stop here anymore.

ACTOR: If you can't even manage to get to the store-get some household help!

ACTRESS: (Icy.) Have gone to bed. Dinner is in fridge. If there is something in particular you wish for dinner tomorrow night, please leave note to that effect, and I will have Ursula or Carla or Jose, if it's heavy, pick it up. (Beat.) I can't take this anymore! We barely- (Turns Post-it over.) - communicate! There's got to be more to this marriage than a few hastily scribbled words on a small square of pastel paper! (Beat.) By the way, we're out of Post-its.

ACTOR: You think I want to spend every night at the office? You have absolutely no concept of how a business is run.

ACTRESS: To Whom It May Concern: Regarding your Post-it of June the tenth, allow me to clarify my position-up yours. Eugenia and I will be at your mother's.

PS: You need milk. (The ACTOR glances over at the ACTRESS, she sips her water, coolly avoids his gaze. Finally ... )

ACTOR: Call her at my mother's. (Next Post-it.) Must call her. (Next Post-it.) Reminder: Take out garbage. Call her. (Next Post-it.) People to call: Her.

(The ACTOR looks over again at the ACTRESS. She continues to ignore him.)

ACTOR: Shopping list: Small loaf bread. Half pint milk. Soup for one. (Next Post-it.) Scotch for one. (Next Post-it.) Inflatable doll. (Next Post-it.) Scotch for two.

(The ACTRESS looks at him. He catches her eye. Caught, she hastily looks away.)

ACTOR: Things to tell her. That I'm sorry. That I miss her. That all I want-all I ever wanted-is for her to be happy. (The ACTRESS turns to him, touched by this. Then ... takes the next Post-it. Reads.)

ACTRESS: We need milk.

ACTOR: Dearest-have gone down to the end of the driveway to get the paper. Back soon.

ACTRESS: Honey, that therapist called back. He can see you Monday.

ACTOR: Sweetie, your therapist says your Tuesday is now Friday.

ACTRESS: What a session! Dr. K. believes that part of me is locked in unconscious competition with you, and envious of your masculine role. By the way, we need cucumbers, sausages, and a really big zucchini.

ACTOR: At last-+a breakthrough today with Dr. G. It all became crystal clear. My mother. My father. His mother. You. Your mother. (Turns Post-it over, continues.) I see our entire marriage in a new light! I must free myself from the past so we can truly have a future. This changes everything.

ACTRESS: Hon: A Diet Coke exploded allover that note you left. Hope it wasn't important. (He stares at her. Oblivious to his reaction, she reads the next Post-it.) Took Eugenia to Brownies. Back soon.

ACTOR: Took Eugenia to kickboxing. Back soon.

ACTRESS: Took Eugenia to therapy. Could be a while.

ACTOR: Someone named Olaf called. Needs your resume. What resume?

ACTRESS: I landed the job! I start Monday! (Next Post-it.) Lastminute meeting. I'll try to call. (Next Post-it.) I'll be working late, don't wait up. (Next Post-It.) I'm glad you waited. Last night was incredible.

ACTOR: Drove Eugenia to DMV Hope she doesn't drive me home.

ACTRESS: Eugenia called. Loves college. Mentioned someone named Tyrone. Doesn't miss us at all.

ACTOR: Pick up travel brochures.

ACTRESS: Eugenia called. When can we meet Tyrone?

ACTOR: Schedule trip to campus when we get back.

ACTRESS: Sweetheart: Travel agent called. Cruise is confirmed! The honeymoon we never had! A time for us to leave all this behind and enjoy ten glorious days of total togetherness. (A long, silent beat. Very long. Very silent. They both look straight ahead. Finally he lifts the next Post-it.)

ACTOR: (With great relief.) God, it's good to be home! (Next Post- it.) Dinner Wednesday with Eugenia and what's-his-name.

ACTRESS: Tyrone called-it's a boy. Kareem Eugene.

ACTOR: Eugenia called. Loves being a mom.

ACTRESS: Off to throw pots! Back soon! (Next Post-it.) Don't forget-we're bird-watching Thursday! (Next Post-it.) What night is good for square dancing?

ACTOR: Any night you want-we're free! Nothing to tie us down.

ACTOR: Eugenia called. Could we take Kareem for the weekend?

ACTRESS: Tyrone called. Could we take Kareem for spring break?

ACTOR: Kareem called. Could he spend the summer with us? Again. (Next Post-it.) Took Kareem to DMV

ACTRESS: Honey-last night was incredible. I couldn't believe how long it went on. You've got to do something about your snonng.

ACTOR: Shopping list: Bengay. Dentucreme. Viagra.

ACTRESS: Wrinkles Away. I-Can't-Believe-It's-Support-Hose. Estrogen in a Drum.

ACTOR: We need milk of magnesia.

ACTRESS: Call Medicare.

ACTOR: You left your keys in the door again.

ACTRESS: Do you have my keys?

ACTOR: I can't find my glasses.

ACTRESS: Have you seen my cane?

ACTOR: How can I see your cane if I can't find my glasses?

ACTRESS: Gone for walk.

ACTOR: Where are you? Next time you go out, leave me a note!

ACTRESS: Sweetheart-dinner in oven. Taking nap. Love ya. (There's a pause as lights slowly fade on the ACTRESS. Then ... )

ACTOR: Call Emily. Also cousin Ruthie. Send note to Father McKay and everyone who sent flowers. (Beat.) The service was lovely. Everybody said so. (Beat.) I was looking through your things for that locket you said Eugenia should have. I could hardly believe what I found. You'd saved every Post-it I ever wrote you. I wish I'd saved yours. I could be reading them now. (Beat.) Back soon. Going to the store. We need milk.
```

---

## IC-0892: The Problem

- Title: The Problem
- Author (byline): A.R. Gurney, Jr.
- Work: Plays in One Act
- Publisher: Harper Perennial
- Publication date as stated: Nov 1999
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: WIFE, HUSBAND, USBAND
- Teaser before the introduction: No
- Spoken words (computed): 1599
- Already set (do not supply): none

### Source block (context only)

```text
Author: A.R. Gurney, Jr.
Book: Plays in One Act
ISBN: 0880014903
Publisher: Harper Perennial
Date (Month/Year): Nov 1999
```

### Introduction (context only: never use it for content warnings)

```text
(no introduction)
```

### Performance text (classify this)

```text
Actress: A pipe-smoking absent-minded Professor hasn't had marital relations with his beautiful young wife for five years, but doesn't seem to notice she is pregnant. He nobly deigns to accept the child as his own. Actor: And that’s just he beginning of . . . The Problem by A.R. Gurney, Jr.

WIFE: Hey.

HUSBAND: (Not looking at her.) I'm reading, dear.

WIFE: (Sticking out her stomach.) I know. But look at me.

HUSBAND: (Still reading.) I'm preparing for a class, dear.

WIFE: I know, but just look. (She crosses to him, stands by his chair, and sticks out her stomach.) Just take a gander. (HUSBAND turns his head and looks right into her stomach. He starts, takes off his glasses, looks again, and then looks up into her face.) Well, well.

WIFE: Yes.

HUSBAND: Surprise, surprise. Why have I never noticed before?

WIFE: Because I wear loose-fitting clothes.

HUSBAND: That's true.

WIFE: Clothes without waists. Merri-mekkos. Sack dresses. Granny gowns.

HUSBAND: That's true. (Pause. They smile at each other. Then he looks at his watch.) I've got to teach a class in an hour.

WIFE: I just wanted you to know. (Pause.) So you could plan.

HUSBAND: Yes. I will. I'll plan accordingly. (Smiles at her again, puts on his glasses, and returns to his book. She starts off left, and then stops.)

WIFE: Oh, there's one thing, though.

HUSBAND: (Reading.) Mmmmmm?

WIFE: One small problem.

HUSBAND: (Reading.) Mmmmmm. And what's that, dear?

WIFE: I don't know whether you've thought about this, or not.

HUSBAND: (Looking up.) State the problem. And I'll tell you whether I've thought about it.

WIFE: It's a little tricky.

HUSBAND: Well. We're married, after all.

WIFE: All right. (Pause.) You see, I'm not absolutely sure that this. . .(She looks down at her stomach.) is yours. (Pause. He marks his place in his book, puts it down carefully, takes off his glasses, and then looks up.)

HUSBAND: Ah. So that's the problem.

WIFE: Yes. That's the problem.

WIFE: The thing is . . . that you and I . . . haven't made love very much. Recently. Well, I mean. . . five years, more or less. . . give or take a month or two.

HUSBAND: (Lighting his pipe.) My gosh, has it been that long?

WIFE: Oh, yes.

HUSBAND: Yes, yes. I understand now. What you're really saying is . . .now stop me if I'm wrong. . . but what you're really saying is that you think someone else might have impregnated you.

WIFE: More or less. Yes. On these evenings that you have to go teach.

USBAND: So we do have a problem there, don't we?

WIFE: Yes. We really do. (Pause; he looks at her, looks at her stomach, scratches his head, taps his teeth with a pencil, lights his PiPe, twirls his glasses.)

HUSBAND: You know, darling. . . it occurs to me . . . that I should have made love to you more. But why didn't I? Darn it! Darn it all!

WIFE: Darling, you have your work.

HUSBAND: Oh, sure, but. . .

WIFE: You have your intellectual life . . .You had your book to get out. . .

HUSBAND: Yes, yes, but, darling, that doesn't really answer the question. The question is, why haven't I made love to you in the past five years? That's the question. (Pause.)

WIFE: Well. You used to laugh too much, maybe.

HUSBAND: Laugh?

WIFE: Yes. In the old days. Whenever we started to make love, you'd start to chuckle.

HUSBAND: I did, didn't I? I remember now. (He chuckles.)

WIFE: Yes. You'd chuckle.

HUSBAND: (Chuckling.) Because the whole thing struck me as being slightly absurd. (Chuckling.) When you think about it. (Chuckling.) I should learn to control myself. (He chuckles louder; controls himself stoically; then bursts into loud laughter; then forces himself to subside; looks at her.) I'm sorry.

WIFE: Oh, don't be sorry. I was just as bad.

HUSBAND: Did you chuckle?

WIFE: No. Actually I'd cry.

HUSBAND: I don't remember your crying.

WIFE: Well, I'd whimper.

HUSBAND: Yes, yes! You would. You'd whimper. (Chuckles.)

WIFE: Well, I felt so sad! Making love. While all these horrible things are going on in the world.

HUSBAND: Yes. So you'd whimper. I remember now.

WIFE: Vietnam... Urban blight. . . all that. . . . I felt so guilty!

HUSBAND: And I felt so absurd.

WIFE: Yes. You chuckling, me whimpering. . . .

HUSBAND: Yes. Oh, yes.

WIFE: And so it wasn't very conducive.

HUSBAND: Right. So we gave it up. That answers that. (Pause; picks up his book and starts to read.)

WIFE: But now there's this. (Indicates her stomach.)

HUSBAND: Keep it. Bear it. Bring it home. Give it my name. Consider me its father.

WIFE: Oh, sweetheart.

HUSBAND: I've let you down. Now I'll make it up. Keep it. But you're not satisfied.

WIFE: Oh, I am, I am.

HUSBAND: Darling, we've been married ten years. You are not satisfied.

WIFE: You've got a class.

HUSBAND: My wife comes first. Come on. What's the problem now?

WIFE: All right. (Pause.) What if this. . . (She looks at her stomach.) turns out to be black? (Pause.)

HUSBAND: Black?

WIFE: Black. Or at least mulatto. Depending on how the chromosomes line up. I mean, can you still act as its father if it's black?

HUSBAND: (Pause. Settles down.) Black, eh? That’s a problem. (Pause.) So you must let me think it out.

WIFE: But your class. . .

HUSBAND: I'll just be less prepared than I like to be. Which may be good. Which may be very good. Which may make things more lively and spontaneous. So let me think about this other problem. (Puffs on his pipe; she stands watching him.) I could still adopt it.

WIFE: How?

HUSBAND: We could tell the world that you had a blue baby. Which died. And then we could bring home the black one. Which we say we adopted.

WIFE: That sounds awfully complicated. Besides, the real father might object. He might take pride in it himself.

HUSBAND: No, no. Now wait a minute. . . . (He thinks carefully, then suddenly pounds his fist on the arm of his chair.) Sweetheart, I'm going to be honest with you. (Points to the footstool.) Sit down. Now don't look at me. Face forward. Because this is going to be hard for me to tell, and hard for you to hear.

WIFE: All right. I won't look at you.

HUSBAND: And if I'm inarticulate about this, you must try to understand that this is a difficult thing for a man to tell his wife. I'm only doing it-I'm only telling you-because it seems to be the only way to solve this problem. All right. (He takes a deep breath.) Now. To begin with, I've been lying to you this evening. I don't have a class tonight. I've never had a class at night. I don't believe in evening classes. All these years I've been lying. The class that I've told you meets at night actually meets on Mondays, Wednesdays, and Fridays at ten A.M.

WIFE: I see.

HUSBAND: You may well ask, therefore, where I go on these nights when I say I have classes. (Pause.) And that is what is so difficult to tell you. (Pause.) The fact is, I don't leave this house. Not really. Oh, I leave by the front door, all right. But I immediately circle around in back and go down into the cellar by means of the bulkhead. Now. What do I do in the cellar? You are probably asking yourself that. What do I do in the cellar? . . . Don't look at me, darling! (Pause; then grimly:) Here's what I do in the cellar. I make my way to a small space behind the furnace. And in that small space, I have hidden. . . certain things. (Pause.) What have I hidden? I'll tell you. (He counts them off on his fingers.) Some black theatrical makeup. A woolly wig. A complete change of clothes. And a small mirror. That's what I have hidden in the cellar.

WIFE: I see. . . .

HUSBAND: Yes. You see, my darling, or you're beginning to. When I go into the cellar, I set the mirror up on an adjacent water pipe. I strip myself to the buff. I daub myself from head to toe with that dusky makeup. I glue on that curly wig. I don those makeshift clothes. I leave the cellar. Go to the front door. Ring the bell. And reappear to you. So you see, my poor darling, I am your Negro visitor, and have been all along.

WIFE: You.

HUSBAND: Oh, I know it sounds implausible. But remember how you always lower the lights. Remember, too, that I played Othello in high school. Somehow I was able to pass. I have deceived you for these past years. Deceived my own wife! Disguising myself as a Negro and capitalizing on the sympathies you naturally feel for that unhappy race!

WIFE: But... why?

HUSBAND: Because I wanted to make love to you. And somehow this seemed to be the only way I could do it. You'll have to admit it worked.

WIFE: (Looking at her stomach.) Oh, yes. It worked.

HUSBAND: SO out of all this depravity, at least a child will be born. And I was its father, after all.

WIFE: I'm somewhat. . . stunned. . . by all this. (Grimly.) Sit down. I have a tale to tell too. . . I've known all along you were my dark lover!

HUSBAND: (Sits down.) You've known?

WIFE: From the beginning.

HUSBAND: But... how?

WIFE: Five years ago, when you announced to me that you had scheduled some evening classes, I became suspicious. And so when you left for the first class, I . . . followed you. Yes. I followed my own husband. Followed you to that tacky little theater-supply shop downtown where you bought your disguise. Followed you into the cellar, hid behind the hot-water heater, watched you change into your poor, pathetic imitation of a Negro. When I understood that you were doing it for me, my heart went out to you. With a great rush of longing, I dashed back upstairs, eager to receive you, but at the same time terrified that you would see that I recognized you. Frantically, I dimmed the lights, to make things easier for both of us.

HUSBAND: I thought it was because you were romantic.You were acting? The whole time?

WIFE: Yes. Wasn't I good? Pretending that you were someone new and strange? I, I, who am no actress, improvising like a professional during that whole scene!

HUSBAND: (Shaking his head.) It's hard to believe. . . . You seemed so . . . excited!

WIFE: I was! I was terribly excited. I'll admit it. That strange, sly courtship, the banter, the give-and-take, with all those peculiar racial overtones. I threw myself into it with a vengeance. . . . This is hard to say, but looking at you now, slouched in that chair, surrounded by your books and papers, I sud-denly have the strange urge to experience the stale comforts of bourgeois married love. But there's still this! (Indicating her stomach.) This problem!

HUSBAND: (Moving toward her.) That's no problem.

WIFE: No problem?

HUSBAND: (Stalking her.) That's not really a baby you have in there.

WIFE: (Backing away.) Not really a baby?

HUSBAND: No. That's a balloon you have in there.

WIFE: A balloon? It's a baby. I'm practically positive.

HUSBAND: No, no. Look. I'll show you. (Takes the pointed metal prong of his pipe cleaner and gives her a quick, neat jab in the stomach.) Touche! (There is a pop, and then a hissing sound. She slowly deflates. They both watch.) You see? The problem was simply academic. (Pause.)

WIFE: (Looking at him sheePishly.) Aren't we awful?

HUSBAND: (Going to his chair, closing his book, carefully marking the place.) You started it.

WIFE: I know. It was my turn. You started the last one.

HUSBAND: (Neatening his books and papers.) Well, it's fun.

WIFE: Shouldn't we see a psychiatrist?

HUSBAND: (Tapping out his pipe; putting his glasses in his glasses case.) Why? We're happy. (Turns off his light. The stage is now lit only from a light off left.)

WIFE: But we're so depraved! (He looks at her, then throws back his head and gives a long Tarzan-like whoop; then he pounds his chest like a gorilla; she giggles.) Quiet! You'll wake the children! (He picks her up in his arms; she pummels him melodramatically; speaks in an English accent.) No, Tarzan! White men do not take women by force! No, Tarzan! White men court their women!
```

---

## IC-0893: The Proposal

- Title: The Proposal
- Author (byline): Stephen Bittrich
- Work: 2006: THE BEST 10-MINUTE PLAYS FOR TWO ACTORS
- Publisher: Smith & Kraus
- Publication date as stated: September2007
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MR. AINSWORTH, JULIA
- Teaser before the introduction: No
- Spoken words (computed): 1255
- Already set (do not supply): none

### Source block (context only)

```text
Author: Stephen Bittrich
Book: 2006: THE BEST 10-MINUTE PLAYS FOR TWO ACTORS
ISBN: 978-1575255637
Publisher: Smith & Kraus
Date (Month/Year): September2007
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: The traditional marriage proposal goes something like this: (down on one knee to Actress) “Will you do the honor of becoming my wife?”

ACTRESS: “Of course I will, darling!” (they embrace)

ACTOR: And yet, one fiancée-to-be rejects the common proposal and invents his own marriage invitation.

ACTRESS: An invitation that is less than traditional and, sadly, less than cordial.

BOTH: “The Proposal” By Stephen Bittrich
```

### Performance text (classify this)

```text
MR. AINSWORTH: There you are Miss Hightower. I was beginning to think I'd be called upon to fish you from the trout stream.

JULIA: Beg your pardon, I required a bit of air.

MR. AINSWORTH: Ah, yes. Lovely evening for it. (Pause.) And are you sufficiently pleased with the grounds of Willowbrook?

JULIA: Of course.

MR. AINSWORTH: Splendid - then you approve?

JULIA: Who could find fault with ... the grounds, Mr. Ainsworth?

MR. AINSWORTH: No indeed. No indeed. (Beat.) But then I derive from your careful inflection that there is that at Willowbrook which you could find fault with, Miss Hightower.

JULIA: I - I cannot -

MR. AINSWORTH: Ah, tush, tush, not another word of it. (Beat.) Beautiful, clear night. Did you take in the full moon rising above the peat bogs?

JULIA: I marked it.

MR. AINSWORTH: Dramatic indeed. (Pause.) You know, Ms. Hightower, I rather blush to say, but the highlight of my trip to Sussex last summer was not the tedious family business which beckoned me thither, no, no, but rather my brief sojourn in Heathfield and the various social gatherings during which I was privileged to make the acquaintance of you and your family.

JULIA: (With a taste of irony.) It was a thrilling season.

MR. AINSWORTH: And during the picnic at Heathfield Park I must confess I was most smitten with your wonderful charcoal sketches of the countryside. It is thrilling indeed to discover a woman of such varied and studied accomplishment. Upon leaving there, I admit, I could think of not much else for sometime ... but you ... and your beautiful sketches.

JULIA: You flatter, Mr. Ainsworth.

MR. AINSWORTH: No, indeed, I do not. I very greatly wished to be… connected to you and your great talent - to have some ownership in it.

JULIA: Ownership?

MR. AINSWORTH: And when your family took lodgings in Hampshire this spring it seemed a fortuitous event indeed.

JULIA: Quite fortuitous. I must return to the house, Mr. Ainsworth. It grows cold.

MR. AINSWORTH: Then let me warm you, Ms. Hightower ... Julia.

JULIA: No-

MR. AINSWORTH: Please, take my coat.

JULIA: I fear the chill has deeply set in. There is no remedy you can provide.

MR. AINSWORTH: (Relinquishing all false civility) I grow weary of these intrigues and double entendres. I am not a stupid man, Miss Hightower. I know the particulars for your family's visit. Plainly, your parents mean to parade you about polite society as a farmer at the county fair flaunts his choicest pig-

JULIA: Mr. Ainsworth!

MR. AINSWORTH: - but, and please excuse my audacious candor, you won't be winning any ribbons, I'm sorry to say, nor any husbands either for that matter, because, as sordid as it may be, there are scurrilous and unseemly tongues that wag this way and that 'round this tiny little hamlet. And they wag, Miss Hightower, about you. (Julia appears almost dizzy from Mr. Ainsworth's utter lack of decorum.)

JULIA: I'm sure ... I'm sure I haven't the faintest notion -

MR. AINSWORTH: You are a marked woman. There it is. Sorry to be the bearer of ill tidings. But there 'tis. You may as well sew your old maid's weeds forthwith because no suitors of any repute will be knocking at your door.

JULIA: How dare you, sir!

MR. AINSWORTH: I dare, Miss Hightower. I am the first-born son of the wealthiest man in Christendom. In all truthfulness, mere social convention is a paltry constraint for my sizeable wealth and stature. I dare. .. because I can. The fates, however, have been less kind to you. Being without a male sibling, your birthright, such that it is, has been entailed away, and your future, but for the unsecured and certainly meager offerings of an obscure male relative, can promise nothing more than abject poverty.

JULIA: (After a beat, regaining her composure.) And yet ... I do not tremble, Mr. Ainsworth.

MR. AINSWORTH: (After a beat, taking her in.) And yet you do not. There is much to be admired in you, Julia.

JULIA: And much to be abhorred in you.

MR. AINSWORTH: And still ... such an abhorred man as I might yet be your salvation. (Beat.) I like you, Julia.

JULIA: Mr. Ainsworth, you've said quite enough.

MR. AINSWORTH: Are you surprised? Yes, I like you. You are as handsome a specimen as ever I've seen, lively and energetic, talented in music and art, intelligent almost to a fault. These attributes, I daresay, when matched with my own myriad of graces, could well produce exceptionally pleasing offspring.

JULIA: Thank you for your astute observations, Mr. Ainsworth, but despite your previous reference to prized livestock, you'll be surprised to learn, I am no farm animal. Producing "exceptionally pleasing offspring" is not my life's chief objective.

MR. AINSWORTH: (Ignoring and pressing on.) Be assured, I am not looking for love, Julia, and I am quite certain that you do not love me. However, I do require a wife, a partner, in the business of expanding my honorable lineage. It is a grand, unbroken line spanning centuries before me, and I am called upon to bid adieu to the temptations and distractions of my youth and perform my family duty. I see you as a worthy candidate.

JULIA: Mr. Ainsworth, though your described partnership of convenience is no doubt brimming with fruitful promise, you will be shocked to discover your eloquent declaration of affection met with rejection. I hope the dis-appointment will not linger with you for long. Good evening, sir.

(She starts to leave, and He cuts her off)

MR. AINSWORTH: Julia, certainly you are not ignorant of what I can offer a woman such as yourself in a "partnership of convenience" as you describe it. Not that I care a jot for social mores, but you cannot be completely unaware that your very reputation has recently been called into question. Your association with a local artist, a certain Monsieur Legard, whose name alone inspires credulity, is fatty meat for the maw of outrage, namely, the elder matrons of Bishops Waltham.

JULIA: My association with the gifted Mr. Legard is of my concern alone

MR. AINSWORTH: Unjust, I know. Your guilt in this acquaintance, real or imag-ined, pure or impure, has set you alone and adrift at sea. And I alone am your last hope for security, Ms. Hightower.

JULIA: Really, Mr. Ainsworth, I think you missed your calling. Prize pigs, gristle-filled maws, adrift at sea. It seems you have a bent toward the poetic. But perhaps you should have said, "I alone might offer a sturdy mast and sail" ... or "I alone am a fruitful uncharted isle in your course" or better still "I alone am the God Poseidon deigning to grant fair seas for your passage home."

MR. AINSWORTH: Perhaps I might have.

JULIA: Mr. Legard, whom, as you have intimated, is of French heritage is in fact as true an Englishman as you or I. He is my friend, and his skill with either brush or chisel is equal to anything I have seen displayed in the National Gallery. I admire his talent.

MR. AINSWORTH: Yes, I agree he is talented. I've seen his nudes. He's an eye for detail. (She starts again to leave. He grabs her arm.)

JULIA: Mr. Ainsworth, you will let go my arm!

MR. AINSWORTH: (Pulling her close.) The deal is sealed, Ms. Hightower. Your parents have already accepted my offer of matrimony and despite social proprieties dictating the contrary, have accepted a generous gift of real estate in this accord. You have been sold -

JULIA: - I will not bow -

MR. AINSWORTH: Nay, but you will! As I said, Miss Hightower. You have been sold. I possess the painting!

JULIA: Wh-what did you say?

MR. AINSWORTH: I possess the painting. And I think you must know the one I mean.

JULIA: Impossible ...

MR. AINSWORTH: (Quiet and vicious, in her ear.) It did not come cheaply. (Beat) You now sit precariously on the edge of ruin. If you do not accept my magnanimous offer, you will suffer the pangs of social ignominy that only an itinerant leper might endure. And moreover, I am quite certain that Mr. Legard will never in his short career see profit from a single painting in all of Hampshire. You will give me satisfaction. (She crumbles to her knees and begins to cry.)

JULIA: Have you no heart? Have you no soul? I - I love him.

MR. AINSWORTH: I know. (Beat) Will we be married?

JULIA: (After a pause.) Y- Yes. (The lights fade to black.)
```

---

## IC-0894: Puberty: The Game Show

- Title: Puberty: The Game Show
- Author (byline): Greg Atkins
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: Sept 1998
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: BABS, ALAN, ELANA, KAREN, TOMMY, KAREN AND TOMMY, MOTHER, DATE, PIMPLES, RAPPER 1, BEATBOXER, RAPPER 2
- Teaser before the introduction: Yes
- Spoken words (computed): 2019
- Already set (do not supply): none

### Source block (context only)

```text
Author: Greg Atkins
ISBN: 978-0874400649
Publisher: Samuel French, Inc.
Date (Month/Year): Sept 1998
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: Everyone’s been through the change!

ACTOR: The only thing different about this sudden morph into adulthood is that it’s done on a gameshow.

ACTRESS: Join your hosts and the contestants on a wild ride in

TOGETHER: Puberty: The Game Show by Greg Atkins.
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles: Actress -- Babs, Elana, Karen, Tommy’s Date, Pimples, Rapper #1 Actor -- Alan, Tommy, Mother, Pimples, Rapper #2, Beatboxer

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

ELANA: Alright, it’s a multiple choice and here it is: Your voice is beginning to change and the first time it happens you are: A - Singing in the shower. B - Talking to the guys after you lost a baseball game. C - Talking to Becky Casey in Math class. Or, D - in front of the entire English class during your oral report?

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

RAPPER 1: Not so fast. (Pimples gasp)

BEATBOXER: (creates beat for Rappers to follow during next song)

RAPPER 2: What you need is a Zip-Zap Pad, the best friend you ever had.

RAPPER 1: Just wipe it all along your face and pimples leave without a trace.

RAPPER 2: Now that your skin is looking hot, you can go back to eating chocolate.

RAPPER 1: Fries and chips and all things bad.

RAPPER 2: Just thank your handy Zip-Zap Pad.

BEATBOXER: Zip-Zap Pads come in Padettes, Extra Strength pads and full body wraps -

RAPPER 1: - from AmWay TRANSITION BACK TO THE GAME SHOW

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

## IC-0895: Rabbit Hole

- Title: Rabbit Hole
- Author (byline): David Lindsay-Abaire
- Work: Not specified
- Publisher: Theatre Communications
- Publication date as stated: Sept 2006
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTRESS, HOWIE, BECCA, VOICE OF DANNY, NEWS REPORTER
- Teaser before the introduction: Yes
- Spoken words (computed): 1048
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Lindsay-Abaire
ISBN: 978-1559362900
Publisher: Theatre Communications
Date (Month/Year): Sept 2006
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Eight months ago, in a happy suburban home, the family dog darted out of the front yard

ACTRESS: And Danny followed - right into the path of an oncoming car.

ACTOR: It was an "accident,"

ACTRESS: But that just means that no one is to blame but everyone feels guilty.

ACTOR: The journey through grief is different for all of us . . .

ACTRESS: We each take our own path. There is no right or wrong way to grieve.

TOGETHER: Rabbit Hole by David Lindsay-Abaire
```

### Performance text (classify this)

```text
Suggested Roles: ACTOR: Howie

ACTRESS: Becca, Danny’s voice, TV Voice over (Tornadoes)

HOWIE: (Pg 14) You want more wine?

BECCA: No, I’ve had two already.

HOWIE: Half a glass . . . (he empties the rest into her glass and lowers the lights in the room)

BECCA: What are you doing?

HOWIE: My eyes are sore, staring at that computer all day.

BECCA: (Pg 15-18) How was squash?

HOWIE: Good. I lost but it was good

BECCA: How’s Rick? . . . . and Debbie? Did Rick mention her?

HOWIE: You can call her, you know. You can call Debbie.

BECCA: I don’t wanna call her. She should call me.

HOWIE: She’s uncomfortable, Bec. If she hasn’t called you, it’s because she doesn’t know what to say.

BECCA: How about “Hey, Becca, how you doing? Haven’t seen you in a while. I would’ve been there for her if God forbid something had ever happened to Robbie or Em. I wouldn’t have vanished the way she did.

HOWIE: If you’re pissed, you should call her and tell her . . . Okay, let it go.

BECCA: Let what go?

HOWIE: Whatever’s making you tense. You should try to relax a little. (He moves to massage her shoulders and starts to kiss her neck)

BECCA: What are you doing?

HOWIE: I’m trying to relax you – something wrong with that?

BECCA: I see what this is. Dimming the lights . . . plying me with liquor . . . . You’re trying to seduce me.

HOWIE: Am I? (moves in again romantically)

BECCA: Alright, Romeo (pushes him away) Enough.

HOWIE: Jesus, Bec . . . it’s been almost eight months. (Beat)

BECCA: I’m just not ready yet, Howie. I’m sorry if you think that’s abnormal.

HOWIE: I thought it was nice. That’s all. I was trying to make things nice.

BECCA: Well . . . you can’t. I’m sorry, but things aren’t “nice” anymore.

HOWIE: (Pg 19-20) -- then . . . maybe we should try again. (Beat)

BECCA: Oh for godsakes, Howie . . . Is that . . . Is that what this was?

HOWIE: No. No, of course not. It just . . . it might be something to talk about at some point.

BECCA: I . . . I can’t. I’m sorry. I can’t have that talk. (Becca exits, Howie watches her go, then goes to the TV cabinet and pulls out a videotape and pops it in.)

VOICE OF DANNY: Did you see me, Daddy?

HOWIE: (speaks along with the video) I did.

VOICE OF DANNY: No, you didn’t. I’m invisible. I have magic.

HOWIE: (speaks along with the video) Down, Taz . . . Oh, I didn’t realize. (lights fade) ******** A few weeks later***********

(Howie clicks on the TV and hits play on the VCR. We hear a documentary on tornadoes playing. [ ] words in red are not printed in the original script )

NEWS REPORTER: [Last year was the strongest storm season in a decade . . . ] (Howie is confused. Something isn’t right. He ejects the tape, examines it, puts it back in and hits play again [An F5 Tornado is the most damaging wind force]

HOWIE: (Pg 32-34) What is this? Becca? Becca!?!! (Becca enters – Howie is beside himself)

BECCA: What’s the matter?

HOWIE: The television. What is this?

BECCA: (Looks to TV) It’s the Discovery Channel. The tornado program. I recorded it for you. What’s the matter?

HOWIE: It’s Danny’s tape. You recorded over Danny’s tape. Jesus, Becca! It’s the only copy!

BECCA: Well, I didn’t do it on purpose. (Howie looks at her skeptically) You think I recorded over Danny’s tape on purpose?

HOWIE: You took the paintings off the fridge. Danny’s paintings. And shoved them in a box.

BECCA: For safekeeping

HOWIE: You’re trying to get rid of him. I’m sorry, but that’s how it feels to me sometimes. Every day, it’s something else. It feels like you’re trying to get rid of any evidence he was ever here.

BECCA: (It’s as if she’s been slapped) The paintings are downstairs. In a box. You can look at them whenever you want.

HOWIE: The clothes. His shoes.

BECCA: We don’t need all that stuff. Why would we keep –

HOWIE: Taz. Sending Taz to your mother’s!

BECCA: There was a lot going on, Howie. We couldn’t deal with the dog.

HOWIE: If I hadn’t bought the dog –

BECCA: And if I hadn’t run inside to get the phone, or if I had latched the gate –

HOWIE: I left the gate unlatched!

BECCA: Well, I didn’t check it. (Retreats a bit) I’m not playing this game again, Howie. It was no one’s fault

HOWIE: Not even the dog’s . . . Dogs chase squirrels. Boys chase dogs.

BECCA: Are you telling me or yourself?

HOWIE: He loved that dog! . . . And you got rid of him!

BECCA: Right, like I got rid of the tape. I get it.

HOWIE: He was a reminder.

BECCA: Yes, he was a reminder. So what? I wanted one less reminder around here. (Pg 19) I can’t move without – I mean, Jesus, look at this. (grabs a toy from the shelf) Everywhere. (grabs a kid’s book from a stack of magazines) Here: “Runaway Bunny” for godsake. The puzzles. The smudgy fingerprints on the doorjambs.

HOWIE: I like seeing his fingerprints.

BECCA: Because you don’t have to sit and stare at them day in and day out. You get to escape. You get to go to work. . . . I left all that to be a mom.

HOWIE: (Pg 18-19) (after a pause) I think you should see someone. (Beat) I know you’re not one for therapists, but I think you should. We could go together if that’s help. Or maybe you could try the group again.

BECCA: No. (Pg 29) A room full of God-freaks.

HOWIE: They’re not God-freaks.

BECCA: Most of them are, Howie. That’s all they talk about. God’s plan. My favorite is “God needed another angel.” What is that? He’s God! Why can’t he just make another angel? It pisses me off. Trying to find some ridiculous meaning in – “Hey look, I stepped in shit, it must be part of God’s plan.” How nice they all have something that makes them feel a little better. Like I don’t feel bad enough. I’ve gotta go and have that rubbed in my face? [God’s] a sadistic prick.

HOWIE: (Pg 34-35) (long silence) You have to stop erasing him! I’m not [just] talking about the tape, Becca! It’s Tax, and the paintings, and the clothes and it’s everything! You HAVE - TO - STOP!

BECCA: Do you really not know me, Howie? Do you really not know how utterly impossible that would be? To erase him? No matter how many things I give to charity, do you really think I don’t see him every second of every day? That tape was an accident. And believe me, I will beat myself up about it forever. Like everything else that I could’ve prevented but didn’t.

HOWIE: That’s not what I want, Bec. It’s not what I’m talking about.

BECCA: No? Because it feels like it is. It feels like I don’t feel bad enough for you. I’m not mourning in the right way. But let me just say, Howie, that I am mourning as much as you are. And my grief is just as real and awful as yours.

HOWIE: I know that.

BECCA: You’re not in a better place than I am, you’re just in a different place. And that sucks that we can’t be there for each other right now, but that’s just the way it is.

HOWIE: His stuff is all we have left. That’s all I’m saying. And every bit of it you get rid of –

BECCA: I understand that. You don’t wanna let go of it. I understand, Howie.

HOWIE: Do you? Do you? (No response) Something has to change here. Because I can’t do this . . . like this. It’s too hard. (Beat) it’s too hard. (Howie exits, leaving Becca alone.)
```

---

## IC-0896: Radiant Vermin

- Title: Radiant Vermin
- Author (byline): Phillip Ridley
- Work: Not specified
- Publisher: Methuen Drama
- Publication date as stated: 978-1474251501
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR, JILL, OLLIE, MISS DEE, TOGETHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1626
- Already set (do not supply): none

### Source block (context only)

```text
Author: Phillip Ridley
ISBN: Mar 2015
Publisher: Methuen Drama
Date (Month/Year): 978-1474251501
```

### Introduction (context only: never use it for content warnings)

```text
TOGETHER: Radiant Vermin by Phillip Ridley
```

### Performance text (classify this)

```text
Suggested Roles: ACTRESS: Jill and Miss Dee

ACTOR: Ollie

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Enter Ollie and Jill, Jill is holding a baby.

JILL: (Pg 7-8) Hello, I’m Jill OLLIE: And I’m Ollie.

JILL: This is our son Benjy. OLLIE: We’d like to tell you about our home.

JILL: Our dream home [and] how we got it.

OLLIE: Exactly. Because . . . well . . .

JILL: We’re good people. We try to be.

OLLIE: And yet . . . some of the things we’ve done – well . . . they’re not exactly . . . nice. In fact, they’re . . . horrible.

JILL: I’m afraid they are, yes. OLLIE: But I’m sure once we’ve explained

JILL: Why we did -- OLLIE: What we did –

JILL: Then you’ll understand.

****6 months before Benjy is born****

JILL: (Pg 9) We’ve just got a letter. Hand delivered. Looks official. (reading) ‘Dear Mr. and Mrs. Swift . . . My name is Miss Dee and I have been asked to head a new department of the government’s housing program known as the Department of Social Regeneration through the Creation of Dream Homes. You’ve been selected for participation in our new scheme. To put it simply. We will give you a house.’

OLLIE: What?! (Takes letter and continues reading) ‘To hear more, meet me at the house in question tomorrow at midday. The address is below along with directions.’ (Scene shift) (Pg 10) It’s the next day. (The Swifts arrive at the house and exit their car)

JILL: (Pg 11-12) The front of the house looks okay. (peering through the windows; Ollie is more hesitant) Big rooms. (She tries the door) The front door’s open! Miss Dee?! . . . Miss Dee?!

OLLIE: You’re not going inside?!

JILL: Why not? (beat) Ollie! (he joins her) The hallway’s lovely.

OLLIE: If you like the smell of damp.

JILL: Two reception rooms. We can knock that wall down. More open-plan.

OLLIE: Am I the only one who can see loose wires everywhere? (Jill wanders into another room)

JILL: The kitchen’s huge! . . . [and] Three bedrooms. Three! This would make the perfect nursery, wouldn’t it? (Miss Dee has appeared in true fairy godmother style)

MISS DEE: Miss Dee – that’s me! What a joy to meet you at last!

OLLIE: (Pg 13-15) Have we been under surveillance?

MISS DEE: What on earth makes you say that?

JILL: Miss Dee . . . this house –

MISS DEE: The contract’s in my bag! (Gives contract to Ollie)

OLLIE: I have some questions first. (as he looks over the contract) So . . we just get given it. This house. And it’s ours. You can’t take it back? Not ever?

MISS DEE: Clause One, as you see.

OLLIE: And if we sell it?

MISS DEE: Clause Two.

OLLIE: . . . We keep all the money.

JILL: Oh, Ollie, it’s too good to be true.

OLLIE: Dad used to say if something’s too good to be true it usually is. (Thunder crash or other sound effect)

MISS DEE: Children please. Listen to Miss Dee. This house is a wonderful chance for you both. I tell you – as God is my witness- no two people are more deserving.

OLLIE: We’re nothing special.

MISS DEE: Nothing special? Jillian! When your mums arthritis got so bad her hand swelled up like rubber gloves full of golf balls – who was it washed her? Dressed her, fed her and – forgive any inappropriate language – took her to the toilet?

JILL: Any daughter would have done the same.

MISS DEE: And you, Oliver! Living with your dad’s alcoholism wasn’t easy. All hugs and kissed one second then [one] too many and – BAHM!

OLLIE: Dad was never violent.

MISS DEE: Not physically. But verbally? Yet you never retaliated. Not once. You’re both good people.

JILL: (Pg 20) Give me that contract! (Snatches the contract and signs) I want this house! (to Ollie) Red Ocean Estate sucks all the joy out of you. I don’t want to bring our baby into a world like that. What will its future be? Drugs? Gangs? Prison? I want more than that for our child. I want . . . this house. I know there’ll be problems. But at least we’ll have the hope of things getting better. (Ollie signs contract) *****The Next Night – In Their New Home*****

OLLIE: (Pg 21-22) (Stretching) Bedtime? JILL: We haven’t put a curtain up!

OLLIE: There’s no neighbors, Jill. (a look from Jill) Okay, okay. I’ll hang a sheet over it. (he peers outside as he is hanging the sheet) Hang on! What’s that? (Jill goes to see)

JILL: Oh! A bonfire. OLLIE: There’s another one.

JILL: Who’s made them, d’you think?

OLLIE: The homeless. Didn’t you see them under the flyover? Cardboard City.

JILL: If we can see their fire, I’m sure they can see our candles.

OLLIE: (Pg 23-26) . . . . Next night! (rustling sounds)

JILL: . . . What’s that? A noise . . . Downstairs. Shhhh!

OLLIE: It’s coming from the kitchen.

JILL: (Panicked) It’s one of the homeless. They saw our candles. I told you they would! (Ollie creeps to the bedroom door) What’re you doing? You’re not going downstairs!? There might be more than one down there, Ollie.

OLLIE: Then I’ll . . . politely ask them to leave.

JILL: Politely ask them?!

OLLIE: They’re just homeless, Jill. Not psycho killers.

JILL: What’re you looking for? OLLIE: A weapon.

JILL: I thought you just said –

OLLIE: Candlestick! This’ll crack a skull in! (he exits the bedroom and heads to the kitchen) (From off stage) AHHH! Someone’s grabbed me from behind! (Sounds of a struggle)

JILL: (When it is quiet, Jill races downstairs) Ollie! (Ollie keeps her from entering the kitchen)

OLLIE: We . . . we struggled . . . he stumbled and he fell.

JILL: He’s . . . he’s dead?!

OLLIE: Listen to me, Jill. Deep breaths (Jill breathes deep) Sit on the stiars . . . now what’s happened here is just a bit of bad luck.

JILL: Look! Under the kitchen door. OLLIE: Light?

JILL: There’s no electric, Ollie. So what’s causing the -- I want to know what it is, Ollie! I want to know right now. It’s fading . . . it’s gone.

OLLIE: Wait here. . . (pushes open the kitchen door a crack and stares – in shock) The body. . . It’s gone. (Jill joins Ollie and screams . . . in delight)

JILL: It’s the kitchen we saw in Selfridges!

OLLIE: (Ollie’s phone chimes) Text. Unknown sender. (reads text) ‘Enjoy your dream home. Love, Miss Dee.’ ***** 7 hours later*****

JILL: (Pg 30) . . . What’re you saying, Ollie? You killed a vagrant and he’s been reincarnated as a designer kitchen?!

OLLIE: Isn’t that quite clearly what has happened? (he exits)

JILL: (Pg 31-33) I can’t stay here. I won’t! (to audience) A man died here last night. Oh, I know what some of you are thinking. He was just a vagrant. When I see a homeless person I always give some money. I know what you’re thinking: “They’ll just spend it on drugs.” Well, some might, yes. But most just want a sandwich. Another thing, when you walk past one of them on the street and you don’t give any money, they mumble something like ‘Have a nice day.” Like they’re trying to make us feel guilty. Guilty for what? Having self-respect? Aspiring to a better life. Why should I – why should any of us? – feel guilty about that? I’m going to the kitchen! (As she enters a beautiful sound effect) Oh! Notice the way the marble shines? Beautiful hot water! And the cupboards full of food. The fridge is full too! (Ollie enters and goes to the sink to wash his hands) Oh, don’t wash your hands in the kitchen sink, Ollie!

OLLIE: No hot water upstairs.

JILL: (thinking) Perhaps we can get – not just hot water – but a whole new bathroom. A bathroom every bit as good as this new kitchen.

OLLIE: What happened last night was an accident. What you’re asking me to do now – this is pre-meditated, cold-blooded . . .

JILL: I want a bath!

OLLIE: And you’re prepared to murder for it?! What if it doesn’t work?

JILL: I think we should at least . . . try. ***** The Renovations Continue****

OLLIE: (Pg 35-36) Stab!

JILL: The dead Intruder With the Baseball Cap is starting to sparkle with fairy lights. It’s the staircase and hallway I saw in Ideal Home magazine!

OLLIE: Stab! The Intruder With the Limp is starting to sparkle with . . .

JILL: Fairylights! Outside! – It’s the front garden I saw in Perfect Gardens and Porches magazine. Look, Ollie, look!

OLLIE: It’s the new Lamborghini Huracan LP 610-2 Super Trofeo!

JILL: Let’s go for a spin.

OLLIE: Who! Jill. What’re you thinking? I kill two people -- Brutally. And then a new car comes along and Shazam! You think I can just forget all about it?! Just like that?

JILL and OLLIE: YESSSSS! *****The New Plan*****

OLLIE: (Pg 38-39) If we’re going to carry on . . .

JILL: The renovations? Oh, I think we should!

OLLIE: So do i. But, we can’t have any more . . . messiness. Not for my sake, you understand.

JILL: Of course not. For their sake. The renovations have to be humane. And, Ollie? I can’t see any of it. It’ll upset baby. And I don’t want to know . . . anything about them. Don’t ever tell me their names. And we can’t wait for them to break in. You’ll have to get in the car and . . .

OLLIE: Find them.

JILL: The ones you choose . . . they should only be the ones who . . . deserve it.

OLLIE: Deserve it? JILL: The one who will never . . . contribute.

OLLIE: Of course . . . the scum. JILL: The scroungers.

OLLIE: The spongers.

JILL: The vermin – Aw! (she rubs her stomach lovingly)

OLLIE: (Ollie touches Jill’s belly and chuckles) He’s saying ‘Let me out of here!’

JILL: Not yet! We’ve got your dream home to get ready first. (Beat)

OLLIE: (to audience) Next day. I’ve been trying to solve the problem of humane home renovation. After many hours of trial and error, I’ve finally come up with something I think ticks all the boxes. Electrocution! Yessss! Fast. Silent. Clean And so - Ta dah! This is the answer to our prayers. Think cattle prod times a million.

JILL: (Pg 40-42) I have married a genius! BZZZZZ! It’s the bathroom I saw in Best Bathroom magazine!

OLLIE: After that the renovations – oh, they happened quickly. Garage, Our bedroom.

JILL: Back Garden, Utility room

OLLIE: Spare bedroom, Loft, Nursery

JILL: It all looked wonderful. (a sound attracts her attention) Oh! What’s that?

OLLIE: (Pg 80-83) Sounds like the letterbox. . . . (he retrieves a letter from the box by the front door) Hand delivered. . . From Larry (reading) Dear Ollie and Jill, I speak on behalf of all your good neighbors. It has come to our attention that some of your behavior is not beneficial to the tone of the neighborhood.

JILL: Not beneficial to the?! (Snatches letter from Ollie) Namely, your persistence in bringing vagrants back to your house. May I remind you, these vagrants are not only potential robbers, but also carriers of disease.

OLLIE: The heartless bastard!

JILL: To conclude, you are lowering the value of our houses.

OLLIE: What!??

JILL: We are instigating a Neighborhood Watch. We are setting up CCTV cameras and we would be grateful if you would sign the enclosed contract . . .

OLLIE: We can’t do any more renovations, can we?

JILL: They’ll be watching us all the time.

MISS DEE: (Appears) Hello, children. I know – That silly letter. Something like this always happens. Clause Six. (makes a tsking sound and shakes her head)

JILL: Maintain discretion.

MISS DEE: We have reached . . . “the moment” where you have to make a decision. To say or . . . move on. (beat) I have a new contract for you here. Exactly the same.

OLLIE: With the same . . . perks?

MISS DEE: Perks? I’ve no idea what you mean. If you can make the new house look as wonderful as this, you’ll make Miss Dee very proud. [but] a friendly warning . . . with each new house, it sometimes feels the sacrifices we have to make . . . double.

OLLIE: (draws Jill aside) You know what she’s saying?

JILL: Each renovation will need two renovators.

OLLIE: That’s a lot of renovators, Jill.

JILL: We can’t stay here and never renovate again. That’s just not an option you know that! Miss Dee!

TOGETHER: We’ll sign!
```

---

## IC-0897: Rain, Rain, Go Away

- Title: Rain, Rain, Go Away
- Author (byline): Isaac Asimov
- Work: Buy Jupiter and Other Stories
- Publisher: Fawcett
- Publication date as stated: November 1976
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: LILLIAN, GEORGE
- Teaser before the introduction: Yes
- Spoken words (computed): 1755
- Already set (do not supply): none

### Source block (context only)

```text
Author: Isaac Asimov
Book: Buy Jupiter and Other Stories
ISBN: 0449230627
Publisher: Fawcett
Date(Month/Year): November 1976
```

### Introduction (context only: never use it for content warnings)

```text
Rain, Rain, Go Away by Isaac Asimov
```

### Performance text (classify this)

```text
LILLIAN: There she is again, There she is, George.

GEORGE: There who is?

LILLIAN: Mrs. Sakkaro, The new neighbors, for goodness sake. Sunbathing. Always sunbathing. I wonder where her boy is. He’s usually out on a nice day like this, standing in that tremendous yard of theirs and throwing the ball against the house. Did you ever see him, George?”

GEORGE: I’ve heard him. It’s a version of the Chinese water torture. Bang on the wall, biff on the ground, smack in the hand. Bang, biff, smack, bang, biff—

LILLIAN: He’s a nice boy, quiet and well-behaved. I wish Tommie would make friends with him. He’s the right age, too, just about ten. I should say.

GEORGE: I didn’t know Tommie was backward about making friends.

LILLIAN: Well, it’s hard with the Sakkaros. They keep so to themselves. I don’t even know what Mr. Sakkaro does.

GEORGE: Why should you? It’s not really anyone’s business what he does.

LILLIAN: It’s odd that I never see him go to work.

GEORGE: No one ever sees me go to work.

LILLIAN: You stay home and write. What does he do?

GEORGE: I dare say Mrs. Sakkaro knows what Mr. Sakkaro does and is all upset because she doesn’t know what I do.”

LILLIAN: Oh, George. I think we should make an effort; the neighborhood should.

GEORGE: What kind of effort?

LILLIAN: To get to know them.

GEORGE: Well, didn’t you, when she’d just moved in? You said you called.

LILLIAN: I said hello but, well, she’d just moved in and the house was still upset, so that’s all it could be, just hello. It’s been two months now and it’s still nothing more than hello, sometimes. —She’s so odd. She’s always looking at the sky; I’ve seen her do it a hundred times and she’s never been out when it’s the least bit cloudy. Once, when the boy was out playing, she called to him to come in, shouting that it was going to rain. I happened to hear her and I thought, Oh no, wouldn’t you know and me with a wash on the line, so I hurried out and, you know, it was broad sunlight. Oh, there were some clouds, but nothing, really.”

GEORGE: Did it rain, eventually?

LILLIAN: Of course not. I just had to run out in the yard for nothing.

GEORGE: Well, since they’re from Arizona, I dare say they don’t know rainclouds from any other kind.

LILLIAN: From where?

GEORGE: From Arizona, according to Tommie. He talked to their boy, in between ball chucks, I guess, and he told Tommie they came from Arizona and then the boy was called in. At least, Tommie says in might have been Arizona, or maybe Alabama some place like that. You know Tommie and his non-total recall. But if they’re that nervous about the weather, I guess it’s Arizona and they don’t know what to make out of a good rainy climate like ours.

LILLIAN: But why didn’t you ever tell me?

GEORGE: Because Tommie only told me this morning and because I thought he must have told you already and, to tell the absolute truth, because I thought you could just manage to drag out a normal existence even if you never found out. Wow—”

LILLIAN: [looking out the window at the neighbor] I’ll simply just have to make her acquaintance. She looks very nice. —Oh, look at that, George. I know she’s staring at that cloud. And now she’ll be going in. Honestly.

LILLIAN: Now, you’re not doing anything tomorrow.

GEORGE: That sounds like a statement, not a question.

LILLIAN: It is a statement. We’re going out with the Sakkaros to Murphy’s Park. With the next-door neighbors, George. How can you never remember the name?”

GEORGE: I’m gifted. How did it happen?

LILLIAN: I just went up to their house this morning and rang the bell. I stood there, jittering, with my finger on the doorbell, till I thought that ringing the bell would be easier than having the door open and being caught standing there like a fool. She was sweet as she could be. Invited me in, knew who I was, said she was so glad I had come to visit. You know.”

GEORGE: And you suggested we go to Murphy’s Park.

LILLIAN: I thought if I suggested something that would let the children have fun, it would be easier for her to go along with it. She wouldn’t want to spoil a chance for her boy. You should see her home. I have never seen any place so spotless.

GEORGE: If you get to know her, then, she’ll be setting you impossible standards and you’ll have to drop her in self-defense.

LILLIAN: Her kitchen was so spanking clean you just couldn’t believe she ever used it. I asked for a drink of water and she held the glass underneath the tap and poured slowly so that not one drop fell in the sink itself. It wasn’t affectation. She did it so casually that I just knew she always did it that way. And when she gave me the glass she held it with a clean napkin. Just hospital-sanitary.

GEORGE: She must be a lot of trouble to herself. Did she agree to come with us right off?

LILLIAN: Well—not right off. She called to her husband about what the weather forecast was, and he said that the newspapers all said it would be fair tomorrow but that he was waiting for the latest report on the radio. Anyway, she called up the weather bureau and had them tell her the latest and she called it out to her husband and they said they’d go, except they said they’d phone us if there were any unexpected changes in the weather.

GEORGE: [To audience] The Sakkaros were young and pleasant, dark and handsome.

LILLIAN: Is that a handbag he’s carrying?

GEORGE: Pocket-radio. To listen to weather forecasts, I bet.”

LILLIAN: [To audience] It was a beautiful day at Murphy’s Park; hot and dry without being too hot; and with a cheerfully bright sun in a blue, blue sky. Even Mr. Sakkaro, though he inspected every quarter of the heavens with a careful eye and then stared piercingly at the barometer, seemed to have no fault to find.

GEORGE: [gloomily] The Sakkaro’s went to the refreshment stand. I told them we’d wait here for them.

LILLIAN: Anything wrong?

GEORGE: No, not really, except that I think he must be independently wealthy. I don’t know what he does for a living. I hinted— He said he’s just a student of human nature. With a handsome, wealthy man next door, it looks as though I’ll have impossible standards set for me, too.”

LILLIAN: Don’t be silly.

GEORGE: And he doesn’t come from Arizona. I said I heard he was from Arizona. He looked so surprised, it was obvious he didn’t. Then he laughed and asked if he had an Arizona accent.

LILLIAN: He has some kind of accent, you know. There are lots of Spanish-ancestry people in the Southwest, so he could still be from Arizona. Sakkaro could be a Spanish name.”

GEORGE: Sounds Japanese to me. —Come on, they’re waving. Oh, look what they’ve bought -- cotton candy,

LILLIAN: [To audience] Huge swirls of pink foam. The Sakkaros held one out to each of us, and out of politeness we accepted. We went down the midway and tried their hand at darts. We took pictures of ourselves. Eventually we collected the youngsters, and the Sakkaros ushered theirs off instantly to the refreshment stand. Tommie hinted the extent of his pleasure at the possible purchase of a hot-dog and George tossed him a quarter. He ran off, too.

GEORGE: Frankly, I prefer to stay here. If I see them biting away at another cotton candy stick I’ll turn green and sicken on the spot. If they haven’t had a dozen apiece, I’ll eat a dozen myself.”

LILLIAN: I know, and they’re buying a handful for the child now.

GEORGE: I offered Sakkaro a hamburger and he just looked grim and shook his head. Not that a hamburger’s much, but after enough cotton candy, it ought to be a feast.

LILLIAN: I know. I offered her an orange drink and the way she jumped when she said no, you’d think I’d thrown it in her face. —Still, I suppose they’ve never been to a place like this before and they’ll need time to adjust to the novelty. They’ll fill up on cotton candy and then never eat it again for ten years.

GEORGE: Well, maybe. You know, Lil, it’s clouding up. Uh-oh, Sakkaro’s seen it. One gets you fifty, he’ll want to go home.

LILLIAN: [To audience] All three Sakkaros were polite but insistent. They were sorry, they had had a wonderful time, a marvelous time, the we would have to be their guests as soon as it could be managed, but now, really, they had to go home. It looked stormy. Mrs. Sakkaro wailed that all the forecasts had been for fair weather.

GEORGE: It’s hard to predict a local thunderstorm, but even if it were to come, and it mightn’t, it wouldn’t last more than half an hour on the outside

LILLIAN: [To audience] The Sakkaro youngster seemed on the verge of tears, and Mrs. Sakkaro’s hand trembled visibly.

GEORGE: [resigned] Let’s go home, [to audience] The drive back seemed to stretch interminably. There was no conversation to speak of. Mr. Sakkaro’s radio was quite loud now as he switched from station to station, catching a weather report every time. They were mentioning “local thundershowers” now.

LILLIAN: [brightly] It does look rather threatening, doesn’t it? [under her breath] Honestly!

GEORGE: [To audience] A wind had sprung up, driving the dust of the weeks-dry road before it, when we entered our street. The leaves rustled ominously. Lightning flickered. [to Sakkaros] You’ll be indoors in two minutes, friends. We’ll make it.

LILLIAN: [To audience] George pulled up at the gate that opened onto the Sakkaro’s front yard and got out of the car to open the back door. We were just in time.

GEORGE: [To audience] The Sakkaros tumbled out, faces drawn with tension, muttering thanks, and started off toward their long front walk at a dead run.

LILLIAN: Honestly, you would think—”

GEORGE: [to audience] The heavens opened and the rain came down in giant drops as though some celestial dam had suddenly burst. The top of our car was pounded with a hundred drum sticks, and halfway to their front door the Sakkaros stopped and looked despairingly upward. Their faces blurred as the rain hit; blurred and shrank and ran together. All three shriveled, collapsing within their clothes, which sank down into three sticky-wet heaps.

LILLIAN: -- they were made of sugar and afraid they would melt.
```

---

## IC-0898: Ravenswood from Bad Habits

- Title: Ravenswood from Bad Habits
- Author (byline): Terrance McNally
- Work: Terrence McNally 15 Short Plays
- Publisher: Dramatists Play Service
- Publication date as stated: June 1994
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: BENSON, HUGH
- Teaser before the introduction: Yes
- Spoken words (computed): 1480
- Already set (do not supply): none

### Source block (context only)

```text
Author: Terrance McNally
Book: Terrence McNally 15 Short Plays
ISBN: 978-1880399347
Publisher: Dramatists Play Service
Date (Month/Year): June 1994
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Let's face it, all of us have our own bad habits.

ACTRESS: We may bite our nails or crack our knuckles.

ACTOR: (Interruption) Some of us interrupt people often or procrastinate. All these nasty habits are hard to break.

ACTRESS: But have no fear! Ravenswood is a special facility that has the answer! With daily injections . . ., all of your bad habits can be resolved. No pain, no work, no suffering. Call it a quick fix, if you will.

ACTOR: Ruth Benson, former patient and now a nurse at the facility is the poster child to prove the program works. Once she was an overweight slob with a horrible drinking and smoking habit . . . but now she’s committed her life to helping others . . . and today is her lucky day.

ACTRESS: The love of her life, Hugh Gumbs, has checked himself into

TOGETHER: Ravenswood from Bad Habits by Terrance McNally.
```

### Performance text (classify this)

```text
BENSON: (Reading a list of new patients) I've been given another chance. I'm the luckiest woman alive. He's here. He's at Ravenswood. I've got him where I want him at last! Oh God! Do you know how many years I've waited for this moment? Hugh Gumbs wants to be a new person and I'll be the one helping him to mold his new self.

Benson wheels in Hugh Gumbs, still wearing his bedraggled street clothes.)

HUGH: Aaaaaaaaaaaaaaaaa!

BENSON: Mr. Gumbs, please! You must try to control yourself.

HUGH: Aaaaaaaaaaaa!

BENSON: It's obvious you're in great distress, Mr. Gumbs, but surely ...

HUGH: I'm desperate, Nurse. You name it and I've got it, done it or used it.

BENSON: As soon as I've gone over your forms ...

HUGH: Couldn't I just have my injection first?

BENSON: (Keeping her head down, looking at her charts.) Smoking. Three packs a day. That's a lot, Mr. Gumbs.

HUGH: I'm not even being honest with you. It's closer to five.

BENSON: Five packs?

HUGH: Six, seven, I don't know! Some nights I set my alarm and wake up at fifteen-minute intervals and have a cigarette.

BENSON: Why?

HUGH: Why? Because that's how much I like to smoke! What kind of a question is that? Why? Why do people do anything? Because they like it! They like it!

BENSON: Even when it's bad for them?

HUGH: Yes! That's exactly why I'm here! I'm a liar. I'm a kleptomaniac. I chase women. I bite my nails. You've got to help me!

BENSON: Thank God, Hugh, thank God!

HUGH: What?

BENSON: (Back to the forms.) A terrible drinking problem. How much exactly?

HUGH: Bloody Marys at breakfast, martinis before lunch ...

BENSON: How many?

HUGH: Two, and three before dinner. And three or four cherry herrings after dinner and hot saki nightcaps.

BENSON: It sounds like you still have your drinking problem all right.

HUGH: Still?

BENSON: (Aside.) Oh, Hugh, Hugh, you're breaking my heart!

HUGH: Aaaaaaaaaaaaa!

BENSON: I want to help you, Mr. Gumbs!

HUGH: Then do it! Can't we do all this after the injection?

BENSON: I'm afraid not, Hugh. Excuse me, I meant Mr. Gumbs.

HUGH: That's the first thing I'd like to change about me. My name. How could any woman love a Hugh Gumbs? I meet a woman and it's fine about the drinking, fine about the smoking... but when I tell her my name, it's all over. Ask yourself, nurse, would you want to go through life as Mrs. Hugh Gumbs?

BENSON: Surely there was one woman, somewhere in your life, who didn't mind your name?

HUGH: One, just one.

BENSON: You see?

HUGH: My mother, for Christ's sake! Please, can't I have my first injection?

BENSON: We're nearly done. What really brings you to Ravenswood?

HUGH: I've told you.

BENSON: I thought perhaps there might be a somewhat more personal reason. I only meant perhaps someone else is responsible for your coming here.

HUGH: Like who?

BENSON: A woman.

HUGH: You're telling me! Say, and you're going to think I'm crazy, did you ever work for an answering service? Your voice sounds so familiar.

BENSON: I know.

HUGH: There was this real battle-axe on my service about five years ago. For a minute, you sounded just like her. Where was I?

BENSON: A woman.

HUGH: Oh yeah, a woman. Yes, there is one.

BENSON: Tell me about her.

HUGH: (With a sigh.) She was very beautiful, very feminine, very desirable. Everything a man could want. Intelligent, decisive, yet strangely yielding.

BENSON: (Almost a murmur.) Yet strangely yielding!

HUGH: She's probably the finest woman alive on the face of this earth.

BENSON: Her name, Mr. Gumbs?

HUGH: Char-Burger! Did you ever work part-time in Char-Burger on East 63rd Street!

BENSON: I'm afraid not.

HUGH: You sound so familiar and I never forget a voice. Eleven o'clock news weather girl, maybe?

BENSON: No. Her name, Mr. Gumbs?

HUGH: (A tormented memory.) Mildred Canby!

BENSON: What about Ruth Benson?

HUGH: Ruth Benson?

BENSON: I believe that's the name on your biography here.

HUGH: I don't remember telling anyone anything about Ruth Benson.

BENSON: You were delirious when they brought you in. You were raving about a Ruth Benson. That's all you said. Ruth Benson, Ruth Benson. Over and over again. She must have been very important to you.

HUGH: Not particularly.

BENSON: I'll be the judge of that. Tell me about her.

HUGH: The main thing I could tell you about Ruth Benson is that she was fat. About 280, I'd say. I mean she was circus fat.

BENSON: I know the type. Go on, Mr. Gumbs.

HUGH: What else about her? I think Ruth Benson is the only person, man, woman or child, I ever asked to take a bath. She used to smoke six packs a day, minimum. Cigarillos. Nicotine stains right up to her elbow! I don't guess she ever drew a sober breath. My main image of her is passed out on the floor like a big rancid mountain. And talk about being a slob! She had dustballs under her bed the size of watermelons. She didn't just have roaches in her kitchen. She raised them. It was like a goddamn stud farm in there. You'd light the oven and there'd be a flash-fire from all the grease.

BENSON: It sounds like Ruth Benson was a woman with a lot of bad habits.

HUGH: She was an out and out pig.

BENSON: I can't help noticing a special glow that comes into your voice every time you mention her name.

HUGH: We had a lot in common, Ruthie and I. I'll never forget the night we each caught the other precisely the same instant picking their nose. God, she was gross.

BENSON: There's that glow again.

HUGH: Just thinking of her with all those fingers up there and I have to smile. You're bringing back a lot of bad memories, Nurse. I haven't thought of Ruth Benson and her soiled sheets in a long time. Your voice sounds so familiar. (Benson is making a big show of raising her skirt to fix a stocking.) You have beautiful legs, Nurse.

BENSON: Familiar voice, unfamiliar legs.

HUGH: The legs look like some movie star, the voice still sounds like that answering voice.

BENSON: (Straightening up.) Don't you know who I am yet, Hugh? No, don't say anything until I've finished. I'm not going to turn around until you tell me that you want me to turn around. I'm glad you don't recognize me. There's no reason that you should. I did it all for you, Hugh. Hugh Gumbs. Like your name, it wasn't easy. But I didn't mind the suffering, the self-humiliation, the incredible self-discipline. I wanted to torture myself into becoming someone a man like you could love and I have. Let me finish! I'm brutally honest with myself. That's not enough, I know, hut it's a beginning. When I look in a mirror now I can say yes, yes, I like that person. I'm not smug, Hugh, I just know my own worth. For five years I've made myself thoroughly miserable so that today I could make you happy and I did it all for Jove. (A pause.) Now yes or no, Hugh, do you want me to turn around? (A pause.)

HUGH: Who are you?

BENSON: (Turning to him, ecstatic.) It's me. Ruth.

HUGH: Ruth?

BENSON: Ruth Benson.

HUGH: Fat Ruth Benson?

BENSON: Yes, yes!

HUGH: You don't look like Ruth.

BENSON: (She is so happy.) I know, I know!

HUGH: You don't sound like her, either.

BENSON: Voice lessons, darling.

HUGH: You don't even smell like Ruth.

BENSON: Zest, Dial, Dove, Lava!

HUGH: You have such beautiful legs,

BENSON: I worked for them.

HUGH: Your teeth.

BENSON: All caps.

HUGH: And your ... (He indicates her breasts.)

BENSON: Exercises.

HUGH: Your big hairy mole.

BENSON: Cosmetic surgery.

HUGH: It's really you?

BENSON: It's really me. The real me and it's all for you, Hugh, I did it all for you.

HUGH: You did?

BENSON: And now that I've found you again I'm not going to let you go this time.

HUGH: You didn't let me go the last time. I let you go.

BENSON: It doesn't matter. The point is you won't want to let me go this time. Oh Hugh, I'm going to make you very, very happy. You're the luckiest man alive.

HUGH: (Shaking his head.) No, Ruth, no. It would never work, Ruth.

BENSON: Of course it will work. It has to work.

HUGH: I couldn't do it to you. Ruth, I've committed myself to Ravenswood, I've gotten so bad.

BENSON: Do you love me?

HUGH: Love you? You're so far above me now. I didn't love you when you were fat and rotten. I can't love you now that you're beautiful and perfect and have such terrific legs.

BENSON: I'm not perfect. I still have my faults, too, darling

HUGH: Like what? Name one.

BENSON: I can't off the top of my head but I'm sure I do somewhere.

HUGH: You see, it's hopeless. You're the sky above and I'm the mud below. Maybe someday I'll be worthy of you but right now I want to forget all about you and try to improve myself, too, and maybe, just maybe, you'll still be up there in the stratosphere, all shiny like an angel, when I poke my head up through the clouds.

BENSON: That was poetic, Hugh.

HUGH: You're an angel. I can't even ask you for a cigarette.

BENSON: Yes. Yes you can. Take the whole pack. I'll light it for you. You want a drink, darling, I'll get you a drink! Go ahead, bite your nails. Do anything you want. I love you. (She puts her fingers in her nose.) It can be just like old times together!

HUGH: {Horrified expression – then slowly puts one finger up his nose)
```

---

## IC-0899: Removing the Glove

- Title: Removing the Glove
- Author (byline): Clarence Coo
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: 1994
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 2, LOUIE, SUPPORT GROUP MEMBERS, WILL, NEWSCASTER’S VOICE, PROTESTER’S VOICE, DISAGREER’S VOICE, DAD, MOM, CINDY, JESSICA, MARK
- Teaser before the introduction: Yes
- Spoken words (computed): 1231
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
Suggested Roles: ACTOR 1: Louis, Support Group Members, Newscaster’s Voice, Disagreer’s Voice, Dad, Mom, Jessica, Mark

ACTOR 2: Will, Protestor’s Voice, Cindy

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

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

## IC-0900: The Rental

- Title: The Rental
- Author (byline): Mark Harvey Levine
- Work: The Best 10-Minute Plays 2010
- Publisher: Smith and Kraus, Inc.
- Publication date as stated: Sept 2010
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: HAROLD, SONYA
- Teaser before the introduction: Yes
- Spoken words (computed): 1839
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mark Harvey Levine
Book: The Best 10-Minute Plays 2010
ISBN: 978-1575257723
Publisher: Smith and Kraus, Inc.
Date (Month/Year): Sept 2010
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: No, Sonya didn’t just wake up in an episode of the Twilight Zone

ACTRESS: Harold is truly her Birthday present for the day from her best friend Valerie

ACTOR: And although this selection is a work of fiction . . .

ACTRESS: There really is a website available where you can “RENT A FRIEND” for around $10.00 an hour.

ACTOR: Shameless plug for the website: RENTAFRIEND.com! - You can rent a local Friend to hang out with,

ACTRESS: Go to a movie or restaurant with,

ACTOR: Or someone to go with you to a party or event.

ACTRESS: Rent a friend to teach you a new skill or hobby, or to show you around an unfamiliar town.

ACTOR: RENTAFRIEND.com!

ACTRESS: Ok, enough . . . enough . . . on with the show!

TOGETHER: The Rental by Mark Harvey Levine
```

### Performance text (classify this)

```text
Sonya's apartment, early morning. There is a knock at the door. Sonya staggers out, half awake, tying on a robe. At her door is Harold, a thirtyish, normal-looking man in a nice coat. He carries a bouquet of flowers, a clipboard, and a picnic basket.

HAROLD: (Through door.) Hello, Sonya? It's Harold!

SONYA: ... Who?

HAROLD: (Through door.) Harold! Valerie sent me. Valerie Persky?

SONYA: Valerie ... ? (She opens her door a little. She gapes at all the stuff he has.) Oh my God!!! What did she do?

HAROLD: (Handing her the flowers.) Happy Birthday from Valerie Persky. I'm Harold, your boyfriend. (He kisses her in a familiar manner and enters.)

SONYA: I ... I ... What?!

HAROLD: (Quickly.) Let me get this stuff in the fridge ... Honey, did I wake you? I did. I'm so sorry. Sit down, relax, I'll be right back. Is this the kitchen? Great. (He exits to kitchen. Sonya grabs a baseball bat she has by the door.)

SONYA: Excuse me! Excuse me! Hello? Who are you?

HAROLD: (Offstage.) I'm Harold! Harold, your boyfriend.

SONYA: My boyfriend?!

HAROLD: (Off stage.) Yeah ... You know, for your birth - ? (He reenters and sees her with the bat. He ducks behind the couch.) Aaaah! Don't shoot!

SONYA: ... It's a baseball bat.

HAROLD: Alright, don't hit.

SONYA: I'm pretty sure I'd remember having a boyfriend.

HAROLD: From Valerie! I'm from your friend Valerie! Wait, wait ... I come with a card. (He holds out a standard "enclosure card" which she grabs and open.)

SONYA: Well, this IS her hand-writing. (Reading.) "Sonya ... what do you get for the girl who deserves everything? Well, you deserve a really great boyfriend, so I got you one, for today at least. Don't wear him out, ha ha. Happy Thirtieth! Love, Valerie." (Pause.) You gotta be kidding.

HAROLD: You had no idea I was coming. OK, OK ... this happens occasionally. Once they sent me to the wrong house; I thought I was gonna have to date an eighty-year-old guy named "Lou" ...

SONYA: (Waving bat) They?! Who's they? What is this?

HAROLD: Wait! I'm your birthday present! From Rent-a-Boyfriend, Ltd.! ... Apparently, I'm a SURPRISE birthday present.

SONYA: Rent-a-Boyfriend, Ltd.?!

HAROLD: I can explain, if you promise not to shatter my skull. (Still suspicious, she lowers the bat.) Thank you. (The company speech.) "Rent-A-Boyfriend, Ltd., has been providing the finest in temporary romantic relationships to the discriminating woman since 1985." I've been rented to you for our sixteen hour "affaire de coeur" package. I'm sure you'll enjoy it, it's one of our most popular ones.

SONYA: I'm going to kill Valerie for this.

HAROLD: Listen, this is a generous gift. And I can promise you a relationship that, though brief, will create a burning, romantic memory that will shine in your heart to the end of your days. (Pause, she snickers.) They make me say that.

SONYA: So you're a ... a gigolo?

HAROLD: No, no, no. A professional boyfriend. It's a specialized craft. There's six months of training, three months of supervised infatuation ...

SONYA: Valerie rented me a boyfriend.

HAROLD: It's a very thoughtful present. She told me that ... um, that you've had a lot of ... disappointments in this area. Well, Sonya, you're about to have the most fantastically romantic day of your life.

SONYA: This is crazy ...

HAROLD: (Really selling it.) Is it? Sonya, today you have someone who cherishes you the way you should be cherished. Who adores the way you curl your fingers in your hair, the way you move across a room. The way you hold a baseball bat. Someone who lives and breathes and dies upon the merest glance of your cobalt blue eyes ... (Sonya's starting to crack.) ... and all you have to say is yes, I deserve this. Yes, at long last. Yes.

SONYA: ... Yes.

HAROLD: (Whipping out a contract.) Sign here.

SONYA: (Signing.) I don't believe I'm doing this. But you know what, I DO deserve it.

HAROLD: Of course you do. And initial here, and here.

SONYA: (Initialing.) After all the creeps, the bad dates, the blind dates, the personal ads, the -

(Harold kisses her full on the lips the moment she finishes signing.) - mmmph!

HAROLD: Thank God we got that over with. Finally, I can hold you in my arms. Hello, sweetheart. Happy Birthday.

SONYA: Wh - OK. We've started, right?

HAROLD: Right. Your boyfriend has come to whisk you away on a fun-filled birthday celebration! I've got a picnic here I think you'll like. Salami and egg sandwiches! Chinese noodles in sesame oil! Chocolate Raspberry Mousse Cake!

SONYA: How do you know what my favorite foods are?!

HAROLD: Valerie told me. But remember, I'm your boyfriend. I know all about you. You like Louis Prima records and old Dick Van Dyke reruns. Your books are in strict alphabetical order. You never wear beige. You live in constant fear you've left your purse somewhere.

SONYA: My God.

HAROLD: But Valerie never told me you wake up first thing in the morning looking breathtakingly gorgeous. I thought that only happened in the movies.

SONYA: Wh-What? Oh God. I must look like hell.

HAROLD: You're stunning. Look at you. Your eyes are -

SONYA: Wait, wait ... this is a little much for me right now, OK? I don't like to be cherished before my first cup of coffee. (He takes out a "travel-cup" of coffee and hands it to her.)

HAROLD: Ah! I brought you some. Dark roast Kenyan. Your fav –

SONYA: (Overlapping.) - My favorite ... of course. I don't believe this.

HAROLD: Sonya, my dear, this is just the beginning ... (She sits stunned on sofa, sipping coffee. Harold starts to massage her feet. Sonya protests, then with an "I give up" wave, lets him.) First, I make you breakfast. Then it's off to Lavender Springs Spa, where you get a mud bath and a massage while I see how many sonnets I can compose about you. Then our picnic lunch in a secluded grove, -

SONYA: (Stunned, softly overlapping.) Uh-huh ...

HAROLD: - a drive along the coast, sailing in the bay-

SONYA: (Falling into his spell.) Yeah sure ...

HAROLD: - Our reservations at La Coupole are for seven-thirty, and afterwards a horse-drawn carriage takes us to - (He produces two tickets from his pocket.)

SONYA: The Eric Clapton concert?!!! Oh my GOD!!! I love you!!! (She throws her arms around him. Then realizes what she's doing.) I'm sorry! I mean ... Wow. You ARE good. Are you sure you're just here for one day?

HAROLD: It'll be a day to remember.

SONYA: (Makes a little noise of disbelief) I ... gotta get dressed. Would you ... excuse me for a minute? Don't go anywhere.

HAROLD: Of course.

SONYA: I'll be right back. (As she leaves.) Oh my God ... Oh my God! (She exits. He produces a dust buster-type sweeper and begins to casually clean.) (Sonya - Off stage.) So ... um ... Harold. Do you do this often? I mean ... how many ... uh, girlfriends do you - ?

HAROLD: Sonya ... right now there are no other women for me. I've never met anyone like you.

SONYA: (Off stage.) Oh ... my ... GOD. (She hops in, half-dressed, putting on shoes.) Well, I've certainly never met anyone like - What the HELL are you doing?

HAROLD: Dusting.

SONYA: Don't! Don't ... do that. Just ... sit. Sit! Stay! You win. You are officially the best boyfriend I have ever had. Or ever will have. (She exits. He appears a little concerned over this last remark.)

HAROLD: Really?

SONYA: (Off stage.) Are you kidding? Gold medal, Boyfriend Olympics, One Day Sprint.

HAROLD: I was a little worried. We got off to a kinda weird start there, what with you swinging a baseball bat at me. (Sonya reenters, fully dressed.)

SONYA: (Peeved.) You've been my boyfriend ten minutes, already we're reminiscing? Anyway, I didn't SWING it, I brandished it.

HAROLD: ... in a threatening manner.

SONYA: How do you "brandish” in a non-threatening manner?

HAROLD: All I'm saying, is, is, we started off on the wrong -

SONYA: What the hell did you expect, a strange man comes bursting through my door, kisses me ... you kissed me! You're lucky I didn't bash your brains in!

HAROLD:(Beaming.) We're having our first fight! Oh honey! (He hugs her.)

SONYA: I'm not sure I'm ready for this kind of relationship.

HAROLD: I'm sorry, sweetheart. Let's forget about it.

SONYA: Yeah ... yeah ... we let it go too long ... (He laughs. She leans back and relaxes into his arms.) I have to admit, this is nice. Y'know, this is all I wanted. Just to be in someone's embrace. Is this too much to ask?

HAROLD: Absolutely not.

SONYA: You know what? I want to walk down the street swinging our arms like we're fifteen.

HAROLD: OK.

SONYA: I want to sit at a restaurant and stare into each other's eyes and completely annoy everyone else.

HAROLD: You got it!

SONYA: I can't wait to show up at yoga tomorrow. You'll drop me off with a quick kiss, and then watch as I - you're not gonna be here tomorrow.

HAROLD: Forget about tomorrow.

SONYA: It's just ... kinda hard. Here I am, in your arms. And then you just leave? It's not fair. This is all I get? One really romantic day? For the rest of my life? (She starts to cry a little.)

HAROLD: The nice thing about this kind of relationship is you KNOW when - Sonya? Are you - ? No - don't cry! Oh God.

SONYA: I'm OK.

HAROLD: No, crying's bad. There's not supposed to be any crying.

SONYA: Oh, I cry all the time. (He grabs a tissue and starts to dry her tears himself) I'm OK ... (He hands her tissues - and then more tissues, until she has way too many. He places them on her, floats them at her, etc. She laughs.)

HAROLD: Much better. You know, I just discovered something. I can't stand to see you cry.

SONYA: Oh, Harold. You're very sweet, y'know.

HAROLD: Sonya ... there's something else ... I love you.

SONYA: What?!

HAROLD: I love you! Can't you see it in my eyes?

SONYA: (Since she is wiping her eyes.) Not at the moment, no ... (She continues to wipe her eyes. jokingly glances at him for a split second.) Yeah, now I can. Got it. (Finishes wiping her eyes, then looks at him again.) You can't be serious.

HAROLD: You don't believe in love at first sight?

SONYA: Do you mean it, or is this part of the package?

HAROLD: I'm your boyfriend. I really love you.

SONYA: How can you love me?

HAROLD: How could I not? You're warm, funny, smart -

SONYA: Stop, stop. Look, I don't know if you're crazy, or I am, but -

HAROLD: Don't you deserve to be loved?

SONYA: Of COURSE I do. EVERYONE does. But this - you just - I mean, you don't REALLY really love me. You're doing this because Valerie paid you.

HAROLD: We have today, because someone paid for it, sure. But I do "REALLY really" love you. I love you, Sonya. (She stares at him. They move in closer ... they almost kiss, but - )

SONYA: Wait a minute. As presents go, this beats a basket of bath gels. But don't come in here telling me you love me.

HAROLD: But I do.

SONYA: Well, that's just swell! Where were you when I needed you? Like when my car was stolen. Or when my Grandmother died? I could have used a boyfriend! You weren't there! I had to deal with that alone!

HAROLD: Sonya, I--

SONYA: And are you gonna be there tomorrow or the next day when something really good happens and I want to tell you about it? You gonna be there?

HAROLD: No, I'm not gonna be there.

SONYA: You love me. Ha! You're just like all the other men.

HAROLD: No, I'm not! I'm a trained professional!

SONYA: I mean, yes, I like romance. Yes, picnics are fun. But I want someone who ... wants to do laundry with me. Or do absolutely nothing - with me.

HAROLD: We could do that too! I'm here to give you what you want!

SONYA: What I WANT is someone who not only knows my favorite coffee but also my soul. Love me? You haven't even MET me!

HAROLD: Listen, I thought I'd -

SONYA: You thought you'd give the girl a small thrill for once in her life?! I make my own thrills, darling. Hey, we're having our second fight!

HAROLD: I'm offering you love -

SONYA: No, thanks! Already got some! I've got my whole family! They drive me crazy, but they love me! And my friends - I have great friends! THEY love me! My God, look what Valerie did for my birthday. I have plenty of love, pal.

HAROLD: Do you.

SONYA: Yes I do. And I sure as hell don't need a Don Juan wanna-be. Guess what, Harold, we're breaking up! I'll remember the ten minutes we had with great fondness. But y'know what? This isn't half a couple standing over here. OK? I'm a whole couple all by myself with a great family, incredible friends - I even kind of like my job! Y'know? So if I end up meeting someone, fine! If I don't, ALSO fine! Got it? I don't need you!

HAROLD: No, you don't.

SONYA: You better believe I don't! (Still yelling.) Did you just agree with me?!

HAROLD: Yeah, I did. Because you're right. You don't need me. But if you ever find someone ... who deserves to love you ... I will envy him. Goodbye Sonya. (He exits. Pause. He returns, slightly embarrassed.) (Company speech.) 'This has been a date from Rent-ABoyfriend, Ltd. If you've enjoyed our service, please ... tell a friend." (With a curt bow, he exits. Sonya stands stunned for a moment.)

SONYA: (shouting after him.) Hey! I enjoyed your service! Now get back here and MAKE ME BREAKFAST!
```

---

## IC-0901: Ruined

- Title: Ruined
- Author (byline): Lynne Nottage
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: 2010
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTRESS, MAMA, CHRISTIAN, OSEMBENGA, SALIMA, SOLDIER, KISEMBE
- Teaser before the introduction: Yes
- Spoken words (computed): 1685
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lynne Nottage
ISBN: 978-0822223900
Publisher: Dramatists Play Service
Date (Month/Year): 2010
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: The Congo – a country devastated by civil war,

ACTOR: Where an estimated 48 women are raped every hour . . .

ACTRESS: Where the death toll has reached over 5.4 million – the deadliest conflict since World War II

ACTOR: Today, it is still one of the most dangerous places on Earth.

ACTRESS: And in the heart of the conflict, we find Mama Nadi’s brothel – a safe haven for a few women who have escaped the villages.

ACTOR: But how can a war be resolved when all factions are prone to unbridled violence?

ACTRESS: How can a country and its people be anything other than . . .

TOGETHER: Ruined by Lynn Nottage

(Pg 29-31) Commander Osembenga, a pompous peacock of a man in dark sunglasses, a gold chain, and a jogging suit, struts into the bar. He wears a pistol in a harness. Osembenga stands erect waiting to be acknowledged.)
```

### Performance text (classify this)

```text
Suggested Roles: ACTOR: Christian (traveling salesman), Osembenga (head of government forces), Kisembe (head of rebel forces) and Soldier (rebel)

ACTRESS: Mama (owner of the brothel), Salima (a prostitute sold to Mama by Christian)

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

MAMA: (pg 8-10) (Impatiently.) What did you bring me?

CHRISTIAN: Go on. Take a peek in the truck.

MAMA: How many?

CHRISTIAN: Three.

MAMA: I don’t know. They look used. Worn.

CHRISTIAN: C’mon, Mama. Take another look. You’ve said it yourself business is good. (Mama considers, then finally.)

MAMA: Okay, one. That one in front. (Points) How much? How much for the one?

CHRISTIAN: It’s been a good week, and I’ll tell you what, I’ll give you two for the price of one. Why not?

MAMA: Are you deaf? No. Tst! I don’t need two more mouths to feed. (then reconsiders) But, I’ll only pay for one. (Yelling.) Josephine! Josephine! Take them out back. Get them washed and some proper clothing. . . (to Christian) Did you at least tell them this time?

CHRISTIAN: Yes. They know and they came willingly. Salima is from a tiny village. She was captured by rebel soldiers; the poor thing spent nearly five months in the bush as their concubine. She says her husband is a farmer, and from what I understand, her village won’t have her back. Because . . .

MAMA: And the other?

CHRISTIAN: Sophie. Sophie is . . . is . . . Look, militia did ungodly things to the child, took her with . . . a bayonet and then left her for dead. And she was – ruined.

MAMA: (Flirtatiously.) Good evening.

OSEMBENGA: It is now. (He gives the place a once-over.)

MAMA: Can I get you something?

OSEMBENGA: Bring me a cold Primus. A pack of cigarettes, fresh. (Mama produces a chair for Osembenga, then she fishes into the cooler for a beer.)

MAMA: Monsieur, I must ask you to leave your bullets at the bar, otherwise you don’t come in.

OSEMBENGA: And if I choose not to.

MAMA: Then you don’t get served. I don’t want any mischief in here. Is that clear? (Osembenda is charmed by her tenacity. He laughs with the robust authority of a man in charge.)

OSEMBENGA: Do you know who I am?

MAMA: I’m afraid you must edify me. And then forgive me, if it makes absolutely no difference. Once you step through my door, then you’re in my house. And I make the rules here. (Osembenga laughs again.)

OSEMBENGA: All right, Mama. Forgive me. (Osembenga makes a show of removing the bullets from his gun and placing them on the table.) And who said I don’t respect the rule of law?

MAMA: Monsieur, I don’t recall seeing you here before. What brings you to mon hotel?

OSEMBENGA: Jerome Kisembe, the rebel leader. (Osembenga studies her face to gauge the response.) You know him, of course.

MAMA: I know of him. We all know of him. His name is spoken here at least several times a day. We’ve felt the sting of his reputation.

OSEMBENGA: So, you do know him.

MAMA: No, as I said I know of him. His men control the road east and the forest to the north of here.

OSEMBENGA: Is that so?

MAMA: Yes, but you must know that. (Osembenga speaks to Mama, but he is clearly addressing everyone in the audience.)

OSEMBENGA: This Jerome Kisembe is a dangerous man. You hide him and his band of renegades in your villages. Give them food, and say you’re protecting your liberator. What liberator? What will he give the people? That is what I want to know! What has he given you, Mama? Hm? A new roof? Food? Peace?

MAMA: Me, I don’t need a man to give me anything.

OSEMBENGA: Make a joke, but Kisembe has one goal and that is to make himself rich on your back, Mama. (Osembenga grows loud and more forthright as he speaks.) He will burn your crops, steal your women, and make slaves of your men all in the name of peace and reconciliation. Don’t believe him. He, and men like him, these careless militias wage a diabolical campaign. They leave stains everywhere they go. And remember the land he claims as his own, it is a national reserve, it is the people’s land, our land. And yet he will tell you the government has taken everything, though we’re actually paving the way for democracy.

MAMA: I know that, but the government needs to let him know that. But you, I’m only seeing you for the first time. Kisembe I hear his name every day.

OSEMBENGA: Then hear my name, Commander Prestige de Bembe Osembenga. (A moment. Mama absorbs the news, she seems genuinely humbled.) You will hear my name quite a bit from now on.

MAMA: Commander Osembenga, forgive me for not knowing your name. Karibu. [Welcome.] It’s a pleasure to have such an important man in our company.

OSEMBENGA: You are a practical woman, I know that you have the sense to keep your doors closed to rebel dogs. Am I right?

MAMA: (an aside to audience) (Pg 51) My doors are open to everybody. And that way trouble doesn’t settle here. (to Osembenga) Of course. (calling for one of her girls) (Pg 16) Salima! Salima, come!

SALIMA: (Salima, disgusted, bristles at the sound of her name. She reluctantly approaches and does a little shimmy for Osembenga) So, “gangsta,” you wanna dance with me? . . . .

(Osembenga responds and then freezes in place as Salima steps out of the scene he will exit as Salima begins her story) . . . (Pg 22) (to audience) Sometimes their hands are so full of rage that it hurts to be touched. (long pause as Salima remembers the past) (Pg 45-46) Do you know what I was doing on that morning? I was working in our garden picking the last of the sweet tomatoes. I put Beatrice down in the shade of a tree, because my back was giving me some trouble. The sun was about to crest, but I had to put in another hour before it got too hot.

CHRISTIAN: (pg 28) (Christian enters and also addresses the audience in a separate but interlocking monologue) It’s scaring me. I was just by Yaka-Yaka. When I was there six months ago, it was a forest filled with noisy birds, now it looks like God spooned out heaping mouthfuls of earth! It’s been ugly, but never like this. Not here.

SALIMA: (Pg 45-46) It was such a clear and open sky. This splendid bird, a peacock, had come into the garden to taunt me, and was showing off its feathers. I stooped down and called to the bird. “Wssht, Wssht.” And I felt a shadow cut across my back, and when I stood four men were there over me, smiling, wicked schoolboy smiles.

CHRISTIAN: (Pg 50) (with urgency) Listen, listen to me. I saw a boy, take a machete to a man, sever his neck, a clean blow and lift the head in the air like a trophy.

SALIMA: (Pg 45-46) “Yes?” I said. And the tall soldier slammed the butt of his gun into my cheek. Just like that. It was so quick, I didn’t even know I’d fallen to the ground. Where did they come from? How could I not have heard them?

CHRISTIAN: (Pg 50) Men were hollering. “We strong warriors, we taste victory. We will kill!”

SALIMA: (Pg 45-46) One of the soldiers held me down with his foot. He was so heavy, thick like an ox and his boot was cracked and weathered like it had been left out in the rain for weeks. His foot was so heavy and it was all I could see, as the others . . . “took” me. My baby was crying. She never cried, but she was crying, screaming. “Shhh,” I said. “Shhh.” And right then (Salima closes her eyes.) A soldier stomped on her head with his boot. And she was quiet. (A moment. Salima is overcome with grief.)

CHRISTIAN: (Pg 50-51) Oh shit, my hand, my hand is still shaking. This . . . this man Osembenga is evil. He plays at democracy. But we have to pretend that all this ugliness means nothing. We wash the blood off with buckets of frigid water, and whitewash our walls.

SALIMA: (Pg 45-46) I fought them! I did! But they still took me from my home. They took me through the bush, raiding thieves. F**** demons!

SOLDIER: “She is for everyone, soup to be had before dinner,”

SALIMA: They tied me to a tree by my foot, and the men came whenever they wanted soup. I make fires, I cook food, I listen to their stupid songs, I carry bullets, I clean wounds, I wash blood from their clothing, and, and, and … I lay there as they tore me to pieces, until I was raw … five months. Five months. Chained like a goat. These men fighting … fighting for our liberation. Still I close my eyes and I see such terrible things. Things, I cannot stand to have in my head. How can men be this way? (A moment.) How did I get in the middle of their fight? What did I do? I must have done something. (Salima fades offstage as Kisembe, leader of the rebel forces enters, zipping his pants)

MAMA: (Pg 51-52) Kisembe, I hope my girls gave you good company.

KISEMBE: Very. It is good to be back, Mama. Where’s everyone?

MAMA: You tell me. It’s been this way for a week. I haven’t seen but a handful of minders.

KISEMBE: It is Commander Osembenga. He is giving us some trouble. His men set fire to several of our mining villages. They took machetes to anything that moves. This is their justice. Believe me, when we find Osembenga and his collaborators, he will be shown the same mercy he showed our people.

SALIMA: (Mama fades back into Salima to finish her story) (Pg 45) Five months in the bush, passed between the soldiers like a wash rag. Used. (Pg 47) I walked into the family compound expecting wide open arms. An embrace. Five months, suffering. I suffered every single second of it. And he, the man I loved since I was fourteen chased me away with a green switch. (Pg 45) He called me a filthy dog, and said I tempted them. Why else would it happen? I was made poison by their fingers, that is what he said. He had no choice but to turn away from me, because I dishonored him. (Pg 47) He was too proud to bear my shame . . . but not proud enough to protect me from it. (Salima fades)

KISEMBE: (Pg 52-53) They say we are the renegades. They bring soldiers from Uganda, drive us from our land and make us refuges . . . and then turn us into criminals when we protest or try to protect ourselves. I wish [I] could stay all day, but duty calls. (Exits)

MAMA: (Pg 57) You men kill me. You come in here, take your pleasure, and then wanna judge the way I run my “business.” The front door swings both ways. I don’t force anyone’s hand. My girls, ask them . . . ask them, they’d rather be here, any day, than back out there in their villages where they are taken without regard. They’re safer with me, than in their own homes.

OSEMBENGA: (Enters) (Pg 62) This soldier said he saw Jerome Kisembe here.

MAMA: This soldier is liar.

OSEMBENGA: Where is Kisesmbe? (Frightening. Menacing) Tell me where I can find Kisembe.

MAMA: I don’t know where he is . . . (to audience with ferocity) (Pg 57) I didn’t come to here as Mama Nadi, I found her the same way miners find their wealth in the muck. I stumbled off of that road without two twigs to start a fire. I turned a basket of sweets and soggy biscuits into a business. I don’t give a damn what any of you think. This is my place, Mama Nadi’s! (Pg 59) Let all the mother-hating soldiers fight it out. ‘Cuz in the end do you think that will change anything here?

A resource with background information regarding the Congolese conflict and examples of the dialect for this selection can be viewed here and is highly recommended. https://www.youtube.com/watch?v=NXvZdTvQGiI&index=1&list=PLF6F07EC529297AF2
```

---

## IC-0902: The Sasmann Aesthetic

- Title: The Sasmann Aesthetic
- Author (byline): Jules Tasca
- Work: 35 in 10: Thirty-five Ten-minute Plays
- Publisher: Dramatic Publishing
- Publication date as stated: 2005
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: DOCTOR, HOWARD
- Teaser before the introduction: Yes
- Spoken words (computed): 1664
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jules Tasca
Book: 35 in 10: Thirty-five Ten-minute Plays
ISBN: 1583422838
Publisher: Dramatic Publishing
Date (Month/Year): 2005
```

### Introduction (context only: never use it for content warnings)

```text
TOGETHER: The Sassman Aesthetic by Jules Tasca
```

### Performance text (classify this)

```text
DOCTOR: Would you please tell Mr. Sasmann to come in. (After a beat, Howard Sasmann enters. He is a well-built man who wears a pullover shirt and a pair of form-fitting white pants. The Doctor greets him) Howard Sasmann, I’m Dr. Bullock.

HOWARD: Good morning, Dr. Bullock.

DOCTOR: Good morning.

HOWARD: I was supposed to see a Dr. Eric Gutig, I believe.

DOCTOR: I’m his associate. Dr. Gutig’s caught up in an emergency right now.

HOWARD: You mean the guy in the restraints who’s yelling he’s Jesus?

DOCTOR: We don’t discuss other patients, Mr. Sasmann.

HOWARD: I understand a professional ethic, Doctor. But your Jesus is obviously mentally ill. I’m not. Let me clear that up right now. I don’t really belong in a crazy house.

DOCTOR: Mr. Sasmann, this is a hospital, sir.

HOWARD: I stand corrected, Doctor. It is a hospital. All I’m trying to say is that there’s nothing wrong with me.

DOCTOR: All right. But can we just talk for a while?

HOWARD: All talk all you like, but there’s nothing the matter with me.

DOCTOR: Married?

HOWARD: No, I’m not.

DOCTOR: Girlfriend?

HOWARD: I date a couple of girls, yes. And they’re both upset over this, too. It got into the papers.

DOCTOR: So I read.

HOWARD: I need to explain to them that there’s nothing the matter with me. The papers made me into an evil person.

DOCTOR: All right. Then let me hear it from you. What are you doing here at Morrisville State Hospital?

HOWARD: You know what I’m doing here. You have my file.

DOCTOR: You tell me in your own words.

HOWARD: It was a deal. It was a deal my lawyer made with the judge. Coming here kept me out of jail. I agreed to come here as an outpatient to keep from going to prison. And I have to continue coming here until I’m deemed cured, Dr. Bullock. Does that correlate with what you have in that folder?

DOCTOR: It does.

HOWARD: And there’s nothing wrong with me. Prison. That judge threatened me with prison. Oh, I don’t say I don’t possess the same quirks as every man, but psychologically, there’s nothing wrong with me.

DOCTOR: Often . . . Often we perceive that nothing’s wrong, Mr. Sasmann, because a person falls into a pattern of behavior that brings pleasure or security. But, in many cases, certain behaviors are . . . are destructive to a person’s life and he or she doesn’t see that if he . . .

HOWARD: It’s not destructive. It’s harmless. Harmless. And I lost my job over this harmless.

DOCTOR: You taught English at Community College.

HOWARD: Until I was arrested. And now I’m unemployed.

DOCTOR: Why do you think it’s okay for you to go to the beach and . . .

HOWARD: It’s harmless, I tell you. I’ve done it for years.

DOCTOR: And almost always have gotten away with it.

HOWARD: Away with what? Most of the girls smiled.

DOCTOR: But not all. And the judge called it assault, Mr. Sasmann.

HOWARD: It is not – not- assault, Doctor, to kiss someone. Assault. Jesus. There’s nothing – absolutely nothing – violent about Howard Sasmann. I wouldn’t know how to be violent. (He turns away from the Doctor, pause)

DOCTOR: Look, Mr. . . May I call you Howard?

HOWARD: (Turning back to her). Please . . .

DOCTOR: Howard, I don’t know if most people would agree that what you’re doing is acceptable.

HOWARD: Most people live in a narrow band of the spectrum of life, Doctor. I don’t.

DOCTOR: Uh-huh.

HOWARD: Is that uh-huh agreement or disapproval? Most people . . .

DOCTOR: Howard, let’s look at this realistically. You go to the beach and . . . and you . . . kiss women’s buttocks . . .

HOWARD: Yes.

DOCTOR: Then you run off.

HOWARD: Run off. The way you say it. I just go on my way. Run off. You make it sound pathological.

DOCTOR: Then you say it. You tell me in your own words what this is all about. (Pause) Howard . . .

HOWARD: I . . I . . I like women’s buttock s, Doctor. In my sexual map, a woman’s buttocks are the main roads, thoroughfares and railroad lines. Do you understand?

DOCTOR: You’re saying you have a fixation on a woman’s . . .

HOWARD: Why do you make everything sound so clinical? Fixation. Come on, Doctor. In Africa, men are attracted to elongated lips. So much so that women insert pieces of wood under the skin to stretch them even longer. In Japan, men prize a woman’s neck and so dresses are designed to flatter and display a woman’s neck. Here in the U.S., dresses are cut low and bras amply push up the mammary flesh for those men with a propensity for breasts. And on the beach, women wear thongs and bikinis, so that men who admire that anatomical splendor, a woman’s rear, might partake of its beauty. Beauty, Doctor. Oh, God, when did beauty become pathology?

DOCTOR: Howard, you’re correct. There’s nothing wrong with a person, male or female, having a certain fetish, but in the case of . . .

HOWARD: There, you did it again.

DOCTOR: Did what again?

HOWARD: You’re making it all sound like something from a medical case history. Fetish . . . fetish . . .

DOCTOR: A fetish is simply a . . .

HOWARD: I know what a fetish is, Doctor.

DOCTOR: Then go on. Tell me what it is. Why you feel this compulsion . . .

HOWARD: I suppose you can’t think any other way. Compulsion. Now it’s a compulsion. Your job is to make a malady out of every human whimsy that this repressed society looks askance at. Why is it a compulsion? Beauty attracts human beings. And, I might add, the most sophisticated of human beings. It’s supposed to. You call that profound attraction a compulsion?

DOCTOR: You said you’ve been doing it for years and years . . .

HOWARD: Dr. Bullock, I’ve been shaving my face for years, too. And I’ve been eating corned beef on rye for years. I don’t consider those actions to be compulsions. I like a clean shave, and I love the taste of corned beef, and when I go to the beach and I see – excuse me, Doctor, the perfect ass . . . I enjoy going up and kissing it. It brings me pleasure. It makes me excited for my girlfriends. It’s not a matter of compulsion, though it’s compelling. It’s not a fetish, but a defining female attraction. Dr. Bullock, try to understand, that to me the admiration of a tanned, oiled, shimmering derriere is a matter of . . . of . . .

DOCTOR: Of what?

HOWARD: Of aesthetics.

DOCTOR: Aesthetics?

HOWARD: Aesthetics. Yes. You know how a beautiful sunset captures the human eye simply because it’s beautiful. You stop. You watch as the mighty wings of fire spread and float beneath the ocean’s blue. It brings peace and tranquility. A woman’s buttocks well formed is just another object of beauty on this earth: the firm rounded flesh where almost touching halves create the curved path of the split; the straight lines of the legs veering up to meet the delicate arcs; the tantalizing cross where the buttocks sensually crease atop the line of the thigh. Good God. It’s the perfect human confluence of geometric forms in the body, Doctor. And when I kiss the anatomical precision, my kiss is a a salute to the wonderment of nature’s sculptural handiwork. (Pause. Dr. Bullock stares at him a long beat.) Doctor? Dr. Bullock? Is something wrong?

DOCTOR: No. No, I . . . I understand what you’re saying.

HOWARD: I’m sorry for getting myself all worked up.

DOCTOR: That’s perfectly all right, Howard. You’re giving me your perspective. I understand. You have this spontaneous desire to . . .

HOWARD: Desire . . . desire’s okay. Yes, desire. I have a simple desire. . .

DOCTOR: Regardless of the terminology we use, Howard, you can’t go to the public beaches and just . . . just salute women’s buttocks as if they were the stars and stripes.

HOWARD: But you agree there’s nothing wrong with me?

DOCTOR: People can’t just go off and act out all the desires they have.

HOWARD: You didn’t answer my question.

DOCTOR: I’m not a judge and jury. I’m a doctor. Just because you’re more articulate than the average nuisance at the beach . . .

HOWARD: Nuisance?

DOCTOR: . . . doesn’t change the fact that you’re going to have to exhibit self-control.

HOWARD: I told you most of those girls smiled afterward, I swear to you, Doctor. It was just misfortune that this last time, the woman happened to be a lieutenant in the police department. Just my luck; a cop with a hall-of-fame rear end. Doctor, listen to me. For one question, can we be Howard and Grace?

DOCTOR: Go ahead.

HOWARD: Thank you . . . Grace . . . Grace, have you . . . have you ever looked at a man’s body and seen some part of that body that attracts you? (Pause) Doc . . I mean, Grace?\

DOCTOR: How’s this going to address your dilemma? Of course, women look at men’s bodies and find them the object of . . . well . . . in fact, when I go to the tennis club, I see one fellow who must work out. He had an outstanding physique and I always look and . . and . . . and admire.

HOWARD: You see. You see.

DOCTOR: But I have the self-control not to go up to him in the middle of a forehand and kiss him.

HOWARD: Which part of this fellow’s body attracts you the most?

DOCTOR: I’m Dr. Bullock now.

HOWARD: Okay. Okay. I’m sorry. I just wondered.

DOCTOR: So what else would you like to say? I have to write up a summary of this visit.

HOWARD: How many visits must I make before you consider informing the courts that my lips are no longer a threat to society?

DOCTOR: I can’t say right now. But I do want to prescribe a tranquilizer.

HOWARD: A tranquilizer?

DOCTOR: It’ll help calm the compulsion – sorry, but that’s the nomenclature.

HOWARD: Doctor, com on. Tranquilizers?

DOCTOR: Just during the beach season, Howard, show the judge you’re doing something. What am I going to report that we discussed – aesthetics? (She writes the prescription)

HOWARD: You’re right. A prescription. The judge’ll like that. This is a good idea. A prescription. I’ll fill it and I don’t even have to take it, right? I’ll show the courts my pills. Yes. It’s a good idea ( She hands him the prescription). Thank you.

DOCTOR: You’re welcome, Howard.

HOWARD: Two weeks . . . all right . . . two weeks . . . all the killers running loose and she handcuffs me on the beach and reads me Miranda. What a mess, Doctor.

DOCTOR: Now . . Now. . . don’t worry. I think we can work this all out. (She pats his behind gently as she says this. He turns and looks at her.) I’m sorry. I’m sorry. I didn’t mean to be familiar.

HOWARD: That’s . . . that’s all right. I understand (He smiles.)

DOCTOR: I don’t know what came over me.

HOWARD: I’m not embarrassed.

DOCTOR: I apologize.

HOWARD: I said I understand. SO this guy at the tennis court then, you . . .

DOCTOR: (cutting him off) Two weeks, Mr. Sasmann . . . please . . . please . . . I have other patients . . . (Howard raises his hand as if to apologize for lingering and to say goodbye. Then he exits. She crosses downstage as the lights fade.) Holy cow, what came over me? What?
```

---

## IC-0903: Scripted

- Title: Scripted
- Author (byline): Mark Harvey Levine
- Work: Best Ten-Minute Plays for 2 Actors: 2004 (Pg 67+)
- Publisher: Smith and Kraus
- Publication date as stated: Oct 2004
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ELAINE, SIMON, ELAINE AND SIMON
- Teaser before the introduction: Yes
- Spoken words (computed): 1411
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mark Harvey Levine
Book: Best Ten-Minute Plays for 2 Actors: 2004 (Pg 67+)
ISBN: 978-1575253367
Publisher: Smith and Kraus
Date (Month/Year): Oct 2004
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Do you keep experiencing the same situations over and over again?

ACTRESS: Do you keep wishing things would turn out differently; only to have it end up the same way time and again?

ACTOR: Despite your best efforts, does it always seems to be the same old story?

ACTRESS: Even if we recognize it or not, our lives are compelled by a story; it follows a script that we have either written for ourselves or it has been written for us by others.

ACTOR: Are you a hero or a victim, or lesser, just an extra scene – lost in the mass? Whatever you might be, you need to realize you are the central character of your life story.

ACTRESS: And you have the power to change it!

TOGETHER: Scripted by Mark Harvey Levine
```

### Performance text (classify this)

```text
A comfy, lived-in bedroom. SIMON and ELAINE asleep. The alarm goes off.

ELAINE: (Pg 67+) Oh, God, don’t make me get up. . . (Simon reaches over to turn off the alarm. His hand rests on a script. He picks it up.) What time is it? (Simon is engrossed in the script.) Simon? What time is it?

SIMON: (reading from the script) “It’s. . . 7:20. . . ”

ELAINE: You didn’t even look at the clock. . . (Simon looks at the clock.)

SIMON: It IS 7:20. . . (Simon looks back at the script - reading) “It IS 7:20. . . ”

ELAINE: Whatcha got?

SIMON: This isn’t yours?

ELAINE: No. . .

SIMON: I found it. . . on the nightstand. . .

ELAINE: What is it?

SIMON: It’s. . . a. . . script. . .

ELAINE: You mean like for a movie?

SIMON: No. . . For us. It’s us. It’s-- This is what’s happening right now.

ELAINE: What? What are you talking about. . . ?

SIMON: Say something. Say anything.

ELAINE AND SIMON: (simultaneously) The cows are barking at midnight! How did you do that? Stop that! STOP IT!!

ELAINE: Simon, my God how are you doing this?

SIMON: I don’t know! I don’t know! I just found this script. Our script. This is-- I know everything you’re about to say.

ELAINE: What do you mean?! What do you mean?!

SIMON: Look! Read it!

ELAINE: Oh my God. . . it knows what I’m going to say. . . what I’m saying. . . right now. . . Aaugh! (She drops the script. He picks it up.)

SIMON: And we can’t seem to help saying. . . (turns page) . . . what we’re supposed to say.

ELAINE: Well. . . just don’t. Say something different. Look at your next line, and say something else. Anything else. . .

SIMON: (struggling) I. . . can’t. . . (Elaine grabs the script.)

ELAINE: (reading) “I can’t.” (panicking) Okay. Okay. Okay.

SIMON: All right, let’s not panic.

ELAINE: I’m not panicking. . .

SIMON: Yes you are -- it says so, in parentheses. . . “Elaine. . . panicking. . . ”

ELAINE: Don’t look at it! Just don’t look! Put it down! Put it down! (She throws the script to the floor. They cross as far away from it as they can, clutching each other.)

SIMON: All right. . . let’s stay calm. . . let’s try to think here. . .

ELAINE: How can we stay calm?! Simon, we’ve got our lives. . . our own words written down and plonked on our nightstand!

SIMON: It wasn’t there last night. . .

ELAINE: So who put it here? Who wrote this? Someone came in while we were asleep? Into our apartment?

SIMON: How could anyone know what we’re going to say? Elaine, I think. . . someone. . . is trying to tell us something. . .

ELAINE: Someone?

SIMON: Y’know. . . God. . .

ELAINE: No! No No No! Stop that! I don’t want God to tell me things! The God I believe in does NOT drop off scripts in the middle of the night!

SIMON: Maybe it’s a warning! Maybe something horrible happens today. . . and we have a chance to prevent it. . .

ELAINE: You think?

SIMON: We have to see.

ELAINE: Okay, but don’t let go of me. (Together, they shuffle over to the script. Simon gingerly picks it up. Pause. Dramatically, he opens it.) AAAAAUGH! (Simon drops it as if it were alive.) Sorry. Sorry. I’m just scared. Go ahead, I’m not even gonna look. (He picks the script up again. Elaine looks away. He starts to read.)

SIMON: Okay. . . okay. Let’s see. Well, I’m going to be late for work. Probably ‘cause I’m standing here reading this thing. (flips ahead more) You sing show tunes while you grade papers?

ELAINE: Only when I’m upset. You don’t find this horribly frightening?

SIMON: No. . . I mean, yes, but. . . I think it’s kinda neat. . . (reads further) Your mom’s gonna call.

ELAINE: Oh, great. (She looks at the script.) My God. . . our whole conversation is in here. This is so embarrassing. Look —- it takes us three pages to get off the phone. (reading both parts) “All right. . . ” “Okay. . . ” “I’ll talk to you later. . . ” “All right. . . ” “So everything’s okay?” “Everything’s okay.” “All right. . . ” “Okay. . . ” God! We sound so stupid all written down like this.

SIMON: Look at me, I never finish a sentence. All my lines end in “dot, dot, dot”. . .

ELAINE: Simon. . . I’m scared--

SIMON: I know, sweetie. . .

ELAINE: No, I mean, what if. . . what if one of us. . . dies. . . in this? What if that’s why this is here?

SIMON: Well, then,. . . we’ll just avoid whatever it is. I mean, y’know, if it’s a car wreck or something, then we’ll just stay inside. . .

ELAINE: That never works. You’ve watched the Twilight Zone. Y’know, the car crashes through the house anyway.

SIMON: Well, then, lemme look at the end. Let’s see how this thing ends.

ELAINE: Oh God. Okay.

SIMON: I mean, we have to know. . .

ELAINE: Okay. (Terrified, he turns to the last page. They both exhale in relief.)

SIMON: We’re alive.

ELAINE: We just say goodnight and go to bed. That’s nice. . .

SIMON: It looks like our whole day is here. . .

ELAINE: Okay, then. Let’s read it from the beginning. I want to know what happens.

SIMON: Are you sure?

ELAINE: Yeah. . . Yes.

SIMON: Okay. . . here we go. . . (He flips back to the beginning. They begin to read. The lights change a few times to denote passage of time. They finish reading.)

ELAINE: The end.

SIMON: That’s it?

ELAINE: That’s it.

SIMON: Nothing happened.

ELAINE: Thank God.

SIMON: I mean. . . NOTHING happened. . .

ELAINE: I was so terrified something horrible was-- I mean, even if nobody died, we could have-

SIMON: It’s kind of cool. . . to see what it looks like, the way we talk, and. . . but. . . y’know something? That was the most boring thing I’ve ever read.

ELAINE: I know, and I’m thrilled. I’ve had enough excitement for one day.

SIMON: So why is this here? Why did we get this script? What’s the -- y’know, "Why is this day different from all other days?" And. . . it’s not. It’s just another completely interchangeable day.

ELAINE: Simon, what do you want? Car chases? Shootouts? We’re real people. Perfectly wonderfully boringly normal. I have to go to the bathroom. (Elaine exits to the bathroom.)

SIMON: Yeah, that’s it. We go to the bathroom, we watch a little TV, and the next thing you know you’re sixty-five years old.

ELAINE: (Off-stage) Oh, God.

SIMON: I mean. . . I got so excited when we found this, y’know? I was terrified. . . but I thought-- Wow! SOMETHING incredible must happen today! And we’ve been warned because. . . I don’t know, because we’re special or something.

ELAINE: (O.S., brushing her teeth) Well, at least we know what our day’s going to be like.

SIMON: What, that I go to work and make labels for the archive while you stay at home and grade papers?

ELAINE: (O.S., still brushing) Well-- (spits) Yeah. (spits)

SIMON: We don’t need a script for that! I could've told you that yesterday! I could've told you that three days ago! I mean, if you’d like, I can write out all of next week for you. . .

(Elaine reenters. Pause.)

ELAINE: Are we that predictable? (Simon waves the script at her.) Oh, right.

SIMON: I mean, really. Why NOT drop the script off first thing in the morning. We don’t DO anything. This way, we can just read our whole day and go right back to bed.

ELAINE: . . . Wanna rob a bank?

SIMON: You know what I mean. I mean, I just saw my entire day, and I want my money back.

ELAINE: Every day can’t be a wild adventure, Simon. NOBODY lives like that. That’s the movies, that’s TV. There’s nothing wrong with going to work, earning your pay, coming home to your sweetie who, by the way, loves you, going to bed and saying good night. The end. I like that day. That’s a good day.

SIMON: Would you pay to go see it?

ELAINE: Maybe not but I’m thrilled to live it.

SIMON: I’m not. Elaine. . . it’s like. . . Do you know who my Great Grandfather was?

ELAINE: No.

SIMON: . . . Neither do I. I’m only three generations away and he’s completely VANISHED. He didn’t leave a trace. I don’t want to vanish when the curtain closes. I don’t want to just have a nice normal boring life until one day I’m gone and the next day my Great Grandson doesn’t even know what my name was.

ELAINE: Nobody gets remembered forever. Except for, y’know, Lincoln. And Kennedy. Maybe you can get assassinated.

SIMON: I just want to. . . I want them to remember me, and say “He was great”.

ELAINE: Y’know, I think this is a generational thing. Our parents were quite happy to get married and have children and homes and jobs and that was it. It’s only our generation where you have to win a Pulitzer or you’ve failed.

SIMON: Yeah, well, they did this to us.

ELAINE: I don’t feel like I have to be “great”. I just want to have a great life, y’know?

SIMON: Well, you’ve read this thing. Was it great?

ELAINE: Every DAY doesn’t have to be whiz-bang to make a -- Wait, do you remember mentioning your Great Grandfather?

SIMON: Just now?

ELAINE: No, in the script. You didn’t bring him up in the script, did you?

SIMON: No. . . No!

ELAINE: You changed your line.

SIMON: I changed my line. (laughs) I changed my line!

ELAINE: Look in the script. (Simon finds the appropriate section. He screams in horror.) What?

SIMON: (He shows her) A pink replacement page!

ELAINE: My God.

SIMON: But we can change it. We CAN change it.

ELAINE: So. . . let’s change it. What do you want to do?

SIMON: I don’t know. I just want to do something. Y’know? So that if anyone DOES remember us, they’ll say we were. . .

ELAINE: A real couple of characters?

SIMON: Yeah! Right.

ELAINE: So, what, we’re going to totally change our lives? Quit our jobs, move to Peru and become goat farmers?

SIMON: I don’t think that would be terribly fulfilling. No, y’know what I want? I want a pink replacement page, at least one, every day. Every day we have to do at least one completely unexpected. . . crazy. . . memorable . . . thing.

ELAINE: Okay, well, let’s start right now. Gimme a pen. (She grabs one from a nightstand.)

SIMON: What are you doing?

ELAINE: A little rewriting.

SIMON: (peering over her shoulder) Goodness!. . . Well, now we know why I’m going to be late for work. . .

ELAINE: (writes a little more) What do you think?

SIMON: I think. . . I think you write really good stage directions. I think. . . I’m going to remember today.

ELAINE: (As she writes the final sentence) They. . . kiss. Lights. . . out. (They kiss.)
```

---

## IC-0904: Seascape with Shark and Dancer

- Title: Seascape with Shark and Dancer
- Author (byline): Don Nigro
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: Dec 1985
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: BEN, TRACY
- Teaser before the introduction: Yes
- Spoken words (computed): 1842
- Already set (do not supply): none

### Source block (context only)

```text
Author: Don Nigro
ISBN: 978-0573619724
Publisher: Samuel French, Inc.
Date (Month/Year): Dec 1985
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: This play is set in a beach bungalow.

ACTRESS: Ben, the man who lives there has pulled

ACTOR: Tracy, a lost young woman, from the ocean.

ACTRESS: Soon, she finds herself trapped in his life and torn between her need to come to rest somewhere and her certainty that all human relationships turn eventually into nightmares.

ACTOR: The struggle between his tolerant and gently ironic approach to life and her strategy of suspicion and attack becomes a kind of war about love and creation which neither can afford to lose.

ACTRESS: This scene is the climactic scene after Tracy discovers she is pregnant and decides that an abortion is the best solution

ACTOR: Ben does not agree.

TOGETHER: Seascape with Shark and Dancer by Don Nigro
```

### Performance text (classify this)

```text
BEN: Why don’t you tell me what’s wrong? The suspense is killing me.

TRACY: You won’t like it.

BEN: That’s okay. Suffering is good for me. What is it?

TRACY: Ben –

BEN: You’re pregnant.

TRACY: I’m pregnant. I told you you wouldn’t like it.

BEN: It isn’t necessarily a bad thing.

TRACY: Except that we can’t afford it and aren’t married and we didn’t want it.

BEN: Besides that it’s all right.

TRACY: Besides that. Terrific.

BEN: There’s no reason to get upset. The damage is already done.

TRACY: Damage. That’s a nice way to put it.

BEN: I think we ought to go to bed now and talk about it tomorrow.

TRACY: Our lives are ruined an all you want to do is go to bed. Why don’t you hit me or something? Just once I wish you’d wind up and punch me right in the mouth. You’re so insensitive. You and me and baby shit from now on, huh? Sounds wonderful.

(The next morning. Tracy enters from the bedroom, still dressing.)

TRACY: Why did you let me miss my morning classes? Do you know it’s eleven thirty? What are you doing home at eleven thirty?

BEN: (entering behind her) I came home for lunch.

TRACY: You never come home for lunch.

BEN: Today I came home for lunch.

TRACY: Answer the question.

BEN: I forgot the question.

TRACY: Why didn’t you wake me up before you went to work.

BEN: I though you needed the rest.

TRACY: Don’t you think I’m the one that ought to decide that?

BEN: You were asleep. You slept through the alarm. I tried to wake you up. You called me a dirty goat-***** and went back to sleep. I decided you’d made your decision. I’m sorry.

TRACY: Stop saying you’re sorry.

BEN: I lied. I’m not sorry.

TRACY: That’s better.

BEN: Thank you.

TRACY: You’re welcome.

BEN: What have we got to eat?

TRACY: A jar of mayonnaise, some maple syrup, two onions and the great American novel.

BEN: I thought you went to the store yesterday.

TRACY: I did. I got maple syrup.

BEN: Well, do you want onions and mayonnaise, or onions and maple syrup, or mayonnaise and maple syrup?

TRACY: I don’t want anything. I have to go.

BEN: Where do you have to go?

TRACY: Ben . . .

BEN: What? What’s wrong? There’s something wrong. You don’t say Ben like that unless there’s something wrong.

TRACY: Nothing’s wrong. (Pause; Ben waits) I know you don’t really want to have a baby.

BEN: How do you know that?

TRACY: I just know.

BEN: You don’t know.

TRACY: How do you know?

BEN: How do I know what?

TRACY: How do you know I don’t know?

BEN: I know you don’t know because I told you and I meant it when I said it and I mean it now and that’s how I know you don’t know whatever it was we were talking about.

TRACY: That’s easy for YOU to say.

BEN: No it’s not.

TRACY: You’re just saying that.

BEN: If I was just saying that I wouldn’t be here just saying that, I’d be on a Greyhound bus to Venezuela.

TRACY: I was talking to one of the girls at the restaurant.

BEN: I didn’t know they could talk.

TRACY: She was telling me about when she got pregnant.

BEN: Sorry I missed it.

TRACY: She went to somebody.

BEN: A doctor?

TRACY: No. Well, yes, but –

BEN: A part time doctor. A veterinarian?

TRACY: LISTEN, DUMBASS.

BEN: I’m listening, I’m listening.

TRACY: She said she went to this very nice doctor and it wasn’t hardly any trouble at all and then it was all over and –

BEN: Hold it, wait a minute, stop.

TRACY: It’s the easiest thing in the world and –

BEN: Tracy –

TRACY: If she could do it so easy, I don’t see why –

BEN: No.

TRACY: Well, it isn’t like it’s against the law or anything.

BEN: No. End of conversation. No.

TRACY: It isn’t like there’s anything wrong with it, and it hardly takes any time at all, and –

BEN: I said no.

TRACY: What do you mean, NO? Just who the HELL do you think you ARE, anyway?

BEN: It’s my baby, that’s who I am.

TRACY: It’s my baby and don’t call it a baby. It isn’t a baby. It isn’t anything yet and it isn’t going to be because I’m going to do it and you can’t stop me.

BEN: It’s as much mine as yours and you . . . you . . . just can’t.

TRACY: Of course I can. I have an appointment this afternoon. It’s all perfectly safe and legal.

BEN: You made an appointment to do that before you even told me you were pregnant?

TRACY: Don’t yell at me. I wasn’t going to tell you at all, but you made me last night.

BEN: You weren’t even –

TRACY: What difference does it make? I should never have told you at all. Men get so hysterical.

BEN: You’re incredible. All by yourself you decide to murder our child –

TRACY: Stop calling it a child. It isn’t a child. It isn’t anything. You can’t murder somebody that doesn’t exist. God, you’re so stupid. Reactionary. Selfish. People do it all the time. They do it all the time.

BEN: I don’t care what people do all the time. I don’t do it all the time.

TRACY: I don’t believe I’m having this conversation. All this time, unbeknownst to me, I’ve in reality been sleeping with Herbert Hoover. You didn’t even know about it until last night. You’ve never seen it. If I hadn’t told you, you’d never have known it existed. It probably looks like a fish or something now. You’ll forget all about it in a couple of days and be damned happy you didn’t have to spend the rest of your life worried about it.

BEN: You have no right to do that without at least –

TRACY: Some slimey little amphibian I don’t even know is crawling around in my stomach and I don’t have any right?

BEN: I don’t care if it makes sense or not or if it seems fair or not, if you do that you can forget all about me. I won’t sleep with you, I won’t live in the same house with you, I won’t even be able to look at you.

TRACY: What are you getting so upset about?

BEN: I don’t know, but I mean it.

TRACY: Well, all right, you just go right ahead. I’m pretty sick of you anyway. God, what a straight. You’re just like my father.

BEN: I can’t stand your father.

TRACY: You sound like the Pope or something.

BEN: If I was the Pope you wouldn’t be pregnant.

TRACY: Don’t bet on it.

BEN: Why are we talking about the Pope? Do I care about the Pope? WHO GIVES A GOOD GODDAMN ROYL FLYING SHIT ABOUT THE POPE, ANYWAY?

TRACY: DON’T YOU DARE INSULT THE POPE.

BEN: I don’t care what your father thinks and I don’t care what’s legal or how nice the doctor is or what other people think is wrong or right. This isn’t happening to other people, it’s happening to US, and I’m scared that if you kill that thing inside you you’ll be killing us too, and I don’t want that to happen. TRACY; If you can treat me like this when I’m the one that has to be fat and sick and have the pain then maybe we’re already dead. Maybe we always were (pause; much more quietly) Lit a potato, for instance. You don’t think of a sack of old potatoes as being alive, do you? But they sit around in the cupboard and then after a while they start to sprout and there’s things growing out of them and all, but it isn’t like you’d say the potato was alive or anything. I mean, you wouldn’t give it a name or take it to the park in a stroller or anything. It might be growing, sort of, but it isn’t really alive, and it isn’t really even growing, really, it’s just that part of it is turning into something else. And that’s all this thing inside me is doing. It’s growing, sort of, but it isn’t alive, it’s just a part of me that go hooked up with a part of you and started turning into something else. (pause) It’ll be like having a wart removed. That’s what it’s like. (long pause) I have to go. (She seems to be waiting for something) And you’d better not try and stop me.

BEN: I don’t think I’m going to try to stop you.

TRACY: You mean it’s all right?

BEN: I didn’t say it was all right. I said I don’t think I’m going to try and stop you.

TRACY: Well, good. Because I’m going. So goodbye. (Ben is looking at his hands. She hesitates, starts towards the door, then stops) Ben? Are you okay? I wish I could tell what you’re thinking. You never tell me. I can’t get inside you. I can’t get to know you, I don’t know what to do with you, it’s like you’re from another planet or something, you drive me nuts. (pause) You hate me. (pause) IT’s not yours anyway. I was pregnant when I got here. That’s why I stayed. I set you up.

BEN: (looking her in the eye) Bullshit.

TRACY: (looking away) You go to hell. (She stomps out, slamming the door behind her)

(SCENE - Later that night. Door opens and Tracy enters quietly, looking tired. Pause)

BEN: Are you all right?

TRACY: Yes. I’m all right. What are you doing here?

BEN: I live here.

TRACY: I thought you were going. I thought you said you were going.

BEN: It’s my house.

TRACY: Oh. That’s right. I guess I should go. (pause) You hate me.

BEN: No.

TRACY: You HATE me.

BEN: No. Why do you try to make me hate you?

TRACY: Why do you take it?

BEN: I asked you first (pause).

TRACY: When you were little did your parents keep giving you animals and things? The house we lived in was too close to the road, and what happens when you live too close is that all of your animals get splattered always on the road, and your brothers are always having to go out with a shovel and scrape them off and take them someplace to bury. And sometimes if they’re all squashed but not quite dead your brother has to hit them with the shovel until they stop screaming.

BEN: Listen –

TRACY: No, I don’t want to listen to you. After the last one I made my stupid parents promise me they would never get me another thing that was alive because I had figured out what was true and still is true that there is no excuse and no way ever to make up for the millions and millions and millions of innocent betrayed and squashed up dead,

BEN: Tracy –

TRACY: And nobody’s parents and nobody’s God was ever going to be able to explain that to me and make it all right, and the only way not to go crazy was if you never hooked yourself up with splatterable things then it can never be your fault for needing them and having them because if you can’t give you can’t hurt and you don’t get guilty because you can’t betray if you never gave to begin with. Doesn’t that make sense to you? It does make sense, It does.

BEN: So now you kill your own to keep the world from doing it first?

TRACY: I warned you. I tell lies. I don’t keep promises. I make everything I touch dirty. I spoil everything. And you made me get involved when I didn’t want to and now we’re paying for it. Do you think I ever want to make some poor little kid put up with this all her life?

BEN: I think – (hesitates) - I think – (hesitates) – that – (hesitates) – past the words and the lies, the world sits you down with two or three basic things and tells you it’s time to choose. (pause) And I chose you (pause)
```

---

## IC-0905: Secrets

- Title: Secrets
- Author (byline): Walt Vail
- Work: Not specified
- Publisher: Brooklyn Publishing Company
- Publication date as stated: 1998
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: CHARLIE, DIEDRE, FATHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1055
- Already set (do not supply): none

### Source block (context only)

```text
Author: Walt Vail
ISBN: 978-1930961371
Publisher: Brooklyn Publishing Company
Date (Month/Year): 1998
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: In the words of Samuel Johnson: "We cannot tell the precise moment when friendship is formed. As in filling a vessel drop by drop, there is at last a drop which makes it run over; so, in a series of kindnesses there is at last one which makes the heart run over."

ACTOR: Children of domestic violence however have few friends . . . friends share secrets which is the first lesson victims of child abuse learn. Never tell. No matter how hard she tries to deny it, Deidre is in desperate need of a friend.

ACTRESS: If only she could trust someone. But she believes that if anyone really knew her, they’d realize what an awful person she is. That’s what her Dad told her anyway.

ACTOR: Nothing in life is free.

ACTRESS: Everything has a price. To have a true friend, I’d have to sacrifice my

TOGETHER: Secrets by Walt Vail
```

### Performance text (classify this)

```text
Actor: Charlie and Father Actress: Deidre

NOTE: This cutting asks one student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

CHARLIE: Deidre.

DIEDRE: Yes? I have to finish this term paper.

CHARLIE: Can I help?

DIEDRE: I’d rather do it myself.

CHARLIE: I like you, Deidre.

DIEDRE: Charlie, I go steady with David.

CHARLIE: Why David?

DIEDRE: He doesn’t make unreasonable demands on me.

CHARLIE: And I do? How’s your father treating you?

DIEDRE: I’m sorry I told you that, Charlie. It’s not your concern. I shouldn’t have spoken. (beat) My father treats me okay. He’s not drinking.

CHARLIE: He’ll start up again. Like my old man. Drinks, then starts swinging.

DIEDRE: Your father hits you?

CHARLIE: Not since I got bigger that him.

DIEDRE: I can’t hope for that, I guess.

CHARLIE: (looks closely) You’ve got another bruise.

DIEDRE: I turn black and blue if someone breathes on me.

CHARLIE: He’s beating you up all the time. You think I can’t see that?

DIEDRE: Please, Charlie. Don’t tell anyone!

CHARLIE: I couldn’t sleep last night, Deidre. All I could think of was a guy that weighs 180 pounds beating up on a small, defenseless girl. You know what could happen if he hits you too hard?

DIEDRE: I don’t want to talk about it.

CHARLIE: (pause) You want to pretend it isn’t happening?

DIEDRE: It isn’t happening. He’s been calm. Charlie, my father earns a living for our family. If I make trouble for him, he could lose his job.

CHARLIE: Before your mother died…did he beat her too?

DIEDRE: They had their arguments, like any married couple. In the bedroom at night, I’d hear her cry out, as if she was having a nightmare.

CHARLIE: Deidre, your father is sick.

(As she remembers, D has a flashback. She reverts back to a little girl. D sways back and forth in a rhythmic manner, quietly humming or singing a tune. C changes his stance and attitude into one much older than himself, as C plays D’s father)

FATHER: Daddy’s songbird be singin’?

DIEDRE: (voice of a child) For Mama. I’m singin’ for her. Do ya think she can hear me?

FATHER: Dunno. She barely heard me when she was alive.

DIEDRE: How is me and Peggy gonna get raised now, without Mama?

FATHER: You’ll have to look after Peggy. You’re the lady of the house now, Deidre. I’m counting on my little songbird.

DIEDRE: Me? I can’t do it like her. I ain’t Mama.

FATHER: You’re responsible now. There’s rent to pay. You do a good job, You got to do a good job, ya hear? Rent’s not free no more. Rent’s not free. ******Flashback ends*****

DIEDRE: My father’s not sick, exactly. Men have frustrations.

CHARLIE: The heck we do! I’d never hit a woman. And my father may have beat me, but he’d never dare hit my mother. I’d break his head if he ever did.

DIEDRE: I guess that’s why I told you, Charlie. I just sensed you’d understand. I wasn’t trying to get you angry. When I graduate from high school in two more years, I’ll get a job. I’ll get a place of my own, and I’ll take Peggy with me. I’ll be a mother to her.

CHARLIE: How old is Peggy?

DIEDRE: She’s eleven.

CHARLIE: When did he first hit you?

DIEDRE: I was (beat) eleven. Right after mother died. He was alone. . .

CHARLIE: When you wear out, he’ll start on Peggy. A job won’t be enough. You need money to go out on your own.

DIEDRE: I know where to get it, if necessary. [My father] has a lot of cash. He doesn’t trust banks.

CHARLIE: So, steal it and get out now! He can’t say anything. You could turn him in for abuse!

DIEDRE: I can’t steal his money!

CHARLIE: He owes it to you! I’ll go with you.

DIEDRE: You’re not my boyfriend.

CHARLIE: You don’t like David. You go with him for convenience because he’s stupid and harmless, and he doesn’t really care about you. Not like I do! (beat) How much has the old man got? Tell me where it is, and I’ll steal it for you. Give me the key, and I’ll go in while he’s working. I’ll smash a few windows to make it look like a break in.

DIEDRE: Forget it!

CHARLIE: If I had some of that money—do you know what I’d do? I’d solve this problem for you.

DIEDRE: How much money do you need?

CHARLIE: A thousand dollars. I’ll get a place of my own. Then you can join me and bring your sister. Another town, another state. You and Peggy can go to school there, wherever it is. And I’ll get a job.

DIEDRE: I’ll think about it. Now let me do my schoolwork. I have to be home early today.

CHARLIE: Something more is bothering you, I can tell. You act like you don’t want to be noticed, like you have a secret. I know, because I have my own secrets. I’m like you.

DIEDRE: No one’s like me, Charlie. No one.

CHARLIE: Have you ever thought about killing yourself?

DIEDRE: No, I think about surviving. I work hard at staying alive. You mustn’t think about killing yourself. God wouldn’t like it.

CHARLIE: You believe in God? If there is a God, he’s playing a big joke on all of us.

DIEDRE: No, he’s just testing us. He gives us the answers, if we recognize them. (beat) We all grow up.

CHARLIE: No, we don’t. Some of us never make it. Something happens—a car accident, an drug overdose.

DIEDRE: Don’t get morbid.

CHARLIE: I think there’s something you’re not telling me.

DIEDRE: I have plenty of secrets. More than any girl my age should have.

CHARLIE: (pauses, as D. drifts deeply in thought) Deidre? Deidre? ******Flashback *****

DIEDRE: (shielding her sister) I know it’s been a tough day, Daddy. Don’t! Come on. Please! You don’t need to. There’s one more beer left. Maybe if you drink it, you can go to sleep.

FATHER: (in a rage) Out of my way, girl! You can go to your room. Daddy is giving you permission to leave. Now get your butt out of here before I stop feeling so generous!

DIEDRE: Take it out on me. It’s my fault! Whatever happened, I did it!

FATHER: I spawned a crazy girl. Can’t hear nothin’. Now move before you find yourself sleepin’ in the backyard. Rent on this trailer ain’t free, ya’ know.

DIEDRE: (tries to hold him back) I know, Daddy. But you can’t. She’s only ten. Get out of here, Peggy!!!

FATHER: (grabs her by the collar) You can go to your room, or I can EVICT you. Understand!?! ******Flashback Ends *****

CHARLIE: Deidre…Deidre?

DIEDRE: (painfully) I can’t promise anything for sure, but…

CHARLIE: Trust me.

DIEDRE: I do. But, we’re . . . friends, that’s all. I wouldn’t want to hurt or upset you. But, I’ll get you the money. We have one chance. . . and you’re it, Charlie.

CHARLIE: I won’t let you down.

DIEDRE: You don’t really know me. If you did, you wouldn’t like me. I’m not a very nice person. You’ll find that out before long, Charlie. Life swallowed me up long ago. (pause, a distant look in her eye) No matter which way I turn, rent ain’t never gonna be free.
```

---

## IC-0906: A Series of Unfortunate Events (TV)

- Title: A Series of Unfortunate Events (TV)
- Author (byline): Daniel Handler (aka Lemony Snickett) and Joe Tracz
- Work: Not specified
- Publisher: Netflix
- Publication date as stated: 2017
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTRESS, VIOLET, JUSTICE STRAUSS, KLAUS, TOGETHER, COUNT OLAF, BOTH, TROUP MEMBER 1, TROUPE MEMBER 1, TROUPE MEMBER 2, JUSTICE STRAUS
- Teaser before the introduction: Yes
- Spoken words (computed): 1363
- Already set (do not supply): none

### Source block (context only)

```text
Author: Daniel Handler (aka Lemony Snickett) and Joe Tracz
based on The Bad Beginning: Part 1 by Lemony Snickett
TV Transcript: Season 1, Episodes 1 & 2
https://snicket.fandom.com/wiki/A_Bad_Beginning:_Part_One/Transcript
https://snicket.fandom.com/wiki/A_Bad_Beginning:_Part_Two/Transcript
ISBN: On-line Transcripts
Publisher: Netflix
Date (Month/Year): 2017
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: Not to give away the plot or anything, but I would strongly advise all of you to leave immediately and find something far more cheerful to watch.

ACTOR: Perhaps a cooking show. Or a documentary about baby pandas.

ACTRESS: Unfortunately, this story is filled with miserable orphans, suspicious adults, and Count Olaf, a man whose greatest talent is committing felonies in dramatic eyeliner.

ACTOR: But through it all, the unifying theme of this story is:

ACTRESS: If you are smart, capable . . .

ACTOR: . . . and under 18!

ACTRESS: Your job is to compensate for the confidently incorrect life choices of the adults in your life.

TOGETHER: (singing theme song) Look away, look away . . .

ACTOR: A Series of Unfortunate Events (TV- Season 1, Episodes 1&2)

ACTRESS: by Daniel Handler, aka Lemony Snickett and Joe Tracz
```

### Performance text (classify this)

```text
(based on the book The Bad Beginning: Part 1)

Suggested Roles: ACTOR: Klaus, Count Olaf, Troupe Member 2

ACTRESS: Violet, Justice Straus, Troupe Member 1

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

VIOLET: [Hello], I'm Violet Baudelaire, and this is my brother Klaus.

JUSTICE STRAUSS: Oh, well, I am Justice Strauss of the High Court. Forgive my not shaking hands, but as you can see, I am a mountain of parcels.

KLAUS: We'd be more than happy to be of assistance, Justice Straus. My sister is very mechanically minded, and I'm quite adept at library science. Are you Count Olaf's wife?

JUSTICE STRAUSS: What? Oh, oh, no, no, no. Goodness me, no. No, I don't even really know him that well. He's just my neighbor. His house is over there. (points)

TOGETHER: (singing theme song) *Look away, look away . . .

COUNT OLAF: Welcome to my humble home, orphans. I am Count Olaf, the renowned Actor and your new guardian. Please, come in. Wipe your feet on the mat so you don’t track in any mud. And don't forget your enormous fortune.

VIOLET: How do you do?

COUNT OLAF: How do I do? Better and better, Baudelaire's. Better and better. I’m about to be rather wealthy . . .

COUNT OLAF: (unfurling a paper from his pocket) Do you know what this is?

VIOLET: It looks like a list.

COUNT OLAF: Wrong! It's a list. A list of chores. Rich brats like you probably spoiled rotten and have never done a chore in your life.

VIOLET: Actually, we often help around the house.

COUNT OLAF: (ignoring her, he conducts a grand tour) Welcome to your lucky life. Come with me, and I'll show you the delightful features of your home. This is the kitchen where you may help yourselves to meals. The stove is a bit like a servant. You have to whack it sometimes to get it to work. This is the yard which needs weeding, mowing and pruning. Bathroom #7, the only one you are allowed to use, has all the usual amenities, though the management regrets to inform you that the shampoo is not tear-free. If anything, it encourages tears. And this is where you will sleep, orphans.

VIOLET: There's only one bed.

COUNT OLAF: As you can see, I have provided, at no cost to you, this complimentary pile of rocks. Thoughts?

VIOLET: First impressions are often wrong . . .

COUNT OLAF: True. Your first impression of me may be that I am a terrible person. But in time, Baudelaire's, I hope you'll come to realize. . . (ominously) You haven't the faintest idea. *****Scene Change – theme song*****

COUNT OLAF: Why aren't you cleaning? My list was very specific.

VIOLET: We finished it. We even washed your underwear.

COUNT OLAF: You didn't. (consults list and shows Violet) You still have to prepare a meal for myself and my theater troupe. Now, quick, get a move on. The troupe will be here at 7:00, and in the meantime, I will be up in -- can you guess?

VIOLET: Your secret tower room?

COUNT OLAF: Wrong. My secret tower room, which you are forbidden to go into. Understood?

VIOLET: Forbidden.

COUNT OLAF: Forbidden! *****Scene Change to Count Olaf’s Parlor with his Theatre Troupe*****

VIOLET: (as they watch Olaf jiving in his parlor) Klaus, what's that thing James Brown said?

COUNT OLAF: (strikes a pose) I feel good! And a one, and a two, and a . . . (sings) **It’s the Count, it’s the Count, it’s the Count!

TROUPE MEMBERS (BOTH): C!

COUNT OLAF: Is for courageous, just another word for brave!

TROUPE MEMBERS (BOTH): O!

COUNT OLAF: Oh, my God, what a handsome knave!

TROUPE MEMBERS (BOTH): U!

COUNT OLAF: Unbelievable good looks and brains and heart!

TROUPE MEMBERS (BOTH): N!

COUNT OLAF: For the Knowledge, cause I’m very, very smart!

TROUPE MEMBERS (BOTH): T!

COUNT OLAF: For the talent – the world’s greatest actor!

TROUPE MEMBERS (BOTH): (sings) It’s the Count, it’s the Count, it’s the Count!

COUNT OLAF: The Count! (slides into a bow in front of Violet)

VIOLET: (confused) Yes, we've met.

COUNT OLAF: Orphans, this is my theater troupe. And as anyone in the theater knows, after a grand entrance, the audience is supposed to applaud.

BOTH: (applaud awkwardly, sharing a glance) *****Scene Change to Dining Room *****

KLAUS: (Violet and Klaus enter with plates of food) Dinner is served.

COUNT OLAF: (inspects the plates) What? No roast beef?

KLAUS: You didn't tell us you wanted roast beef.

VIOLET: We made ***Puttanesca . . .

COUNT OLAF: Look at my guests. They can hardly touch this revolting foreign food!

TROUP MEMBER 1: You can't go easy on children. They need to be taught to obey their elders.

COUNT OLAF: I demand that you serve roast beef to myself and my guests! (grabs Violet) *****Scene Change – theme song*****

COUNT OLAF: (addressing Violet and Klaus) I want you children to feel more at home here, now that I am your father. As you know, I have been working hard with my theater troupe, and I'm afraid I may have acted a bit standoffish. I want you to participate in my next play: (with flourish) The Marvelous Marriage. It tells the story of a very handsome man, played by me. (thinking) Violet, Violet, Violet . . . you will be playing the young woman I marry. It's a very important role! Although you only have one line. I think you you know what it is.

VIOLET: I don't.

COUNT OLAF: No, no, no. It's, I DO.

VIOLET: Count Olaf . . .

COUNT OLAF: (threateningly) What did you call me?

VIOLET: (wincing) Father . . . I'm not sure I'm talented enough. I'd hate to disgrace your good name.

COUNT OLAF: You will participate! I would prefer it if you participate voluntarily, but I can act loco parentheses.

KLAUS: ****In loco parentis.

COUNT OLAF: Poco De Laurentiis! The point is, I can order you to participate and you must obey. Now, go!I can't stand you anymore. *****Scene Change to Justice Strauss House – theme song*****

JUSTICE STRAUSS: (Violet and Klaus knock at the door; Justice Straus answers) Baudelaires! I'm so happy to see you!

KLAUS: Justice Strauss, can I ask you something?”

JUSTICE STRAUSS: Certainly.

KLAUS: (opening a rather large legal book, he reads) “The only nuptial requirements are a statement of active acquiescence by participants, utilizing in loco parentis if necessary, and the signing of a document in the bride's own hand.” (looks up) Does that mean what I think it means?

JUSTICE STRAUSS: Well, I suppose it depends upon what you think it means.

COUNT OLAF: (abruptly looms behind Klaus; to Strauss) It means you're going to be a star!

JUSTICE STRAUSS: Count Olaf!

COUNT OLAF: Please, call me your guardian actor. Justice Strauss, you are about to find your drab, legal beagle existence transformed into something mind-blowing, and yet extremely classy, when you become the exciting new face of the next Count Olaf production . . . (with great theatrics) The curtain rises. The audience applauds! (demanding look to Violet and Klaus, who both applaud) And you walk onto stage dressed as . . . . a judge!

JUSTICE STRAUSS: (fan-girling) I get to share the stage with Count Olaf?

COUNT OLAF: You will stand in front of a very handsome me while a stunningly-costumed bride, played by Violet (she makes a face) stands beside me. You will perform the wedding ceremony, getting each and every word exactly right . . . while we sign a document which you shall bring from City Hall, for added realism.

VIOLET: (to audience) This is terrible . . . terrible! I’m not old enough to get married!

KLAUS: (to audience) If my sister says "I do" and signs a piece of paper while Justice Strauss is in the room, she's legally married. This play won't be pretend. It'll be real and legally binding. *****Scene Change to SHOWTIME – theme song*****

TROUPE MEMBER 1: Showtime!

COUNT OLAF: (takes the stage) Please, duchess. What is a very handsome man like me to do . . .

(clears throat)

TROUPE MEMBER 1: By the turrets of Gravelstein, this very handsome man shall be mine.

TROUPE MEMBER 2: By the Gardens of Worthington, if I can’t have him, my heart will break.

BOTH: He's so handsome! He's so handsome!”

COUNT OLAF: My wedding day. (wedding march plays as Violet, Klaus and Justice Strauss take the stage)

JUSTICE STRAUS: (to Count Olaf) Do you take this woman to be your lawfully wedded wife?

COUNT OLAF: I do.

JUSTICE STRAUS: (turning to Violet) Do you take this woman?

COUNT OLAF: Man!

JUSTICE STRAUS: (correcting herself) Man. Do you take this man to be your lawfully wedded husband?

VIOLET: (looks apprehensively at Olaf) I do. (they both sign a document)

JUSTICE STRAUS: By the powers vested in me, I now pronounce you Count and Countess. (Olaf tries to Kiss Violet, but she turns her head away)

COUNT OLAF: (proud of himself, he breaks character) Ladies and gentlemen, I'd like to make an announcement. There is no need to continue with tonight's performance. Its purpose has been served. My marriage to Violet Baudelaire is legal, and I am now in control of her entire fortune.

JUSTICE STRAUS: (shocked) That can’t be true!

COUNT OLAF: The law clearly states that the bride must say "I do" and sign the appropriate document (holds up document)

JUSTICE STRAUS: (bewildered, she scans the document) I’m afraid this marriage is legally binding. I am so sorry. I can't believe how easily I was tricked.

COUNT OLAF: (gleefully) You were! It was child’s play, winning this fortune. And now a reception to celebrate my special day! (to Violet) Care to dance, Countess?

VIOLET: I'm not a Countess. At least I don't think I am.

COUNT OLAF: Why not?

VIOLET: I didn't sign the document in my own hand as the law states.

COUNT OLAF: Don’t lie to me, orphan. Everyone saw you!

VIOLET: But I'm right-handed, and I signed the document with my left.

COUNT OLAF: (scoffs) Well, that doesn't count. You're just being a sore loser and trying to ruin my special day.

JUSTICE STRAUS: (looks at the document again, then to Olaf) You are a vile and terrible person. And I am happy to say that because Violet, who is right-handed, signed the document with her left hand, the marriage is invalid!

KLAUS: (cheers)

JUSTICE STRAUS: [Furthermore] the Baudelaires will be sent to a suitable guardian!

TOGETHER: And this series of unfortunate events has come to a close (bows)
```

---

## IC-0907: The Shadow

- Title: The Shadow
- Author (byline): Conrad Bishop and Elizabeth Fuller
- Work: More One-act Plays for Acting Students
- Publisher: Meriwether Publishing
- Publication date as stated: July 2003
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MORT, MARA, BOTH
- Teaser before the introduction: No
- Spoken words (computed): 1208
- Already set (do not supply): none

### Source block (context only)

```text
Author: Conrad Bishop and Elizabeth Fuller
Book: More One-act Plays for Acting Students
ISBN: 1566080878
Publisher: Meriwether Publishing
Date (Month/Year): July 2003
```

### Introduction (context only: never use it for content warnings)

```text
MORT: Sickness is weakness.

MARA: There’s humiliation and vulnerability in being a patient.

MORT: Treatment can be impersonal

MARA: or incompetent.

MORT: or maybe, impossible.

BOTH: “The Shadow”

MARA: By Conrad Bishop and Elizabeth Fuller
```

### Performance text (classify this)

```text
(MORT and MARA in nightclothes, getting into bed, adjusting pillows, bantering but very edgy)

MORT: Beddy-bye.

MARA: When do we have to get up?

MORT: When's your appointment?

MARA: Nine. Then I'll bring the car back and you go for yours.

MORT: Why'd you make our checkups on the same day?

MARA: That way everything's done.

MORT: Suppose we're both sick?

MARA: If you're sick you're sick.

MORT: If I know it I'm sicker.

MARA: You had too much to drink.

MORT: Alcohol sterilizes. My germs are clean.

MARA: They'll look inside you and find pickled gut.

MORT: Put your sick mind to sleep.

MARA: I feel strange.

MORT: (Settling in) Get some sleep, honey.

MARA: (Settling in) Don't act like my doctor. (Pause. Instant shift of worlds: he stands upright, looming over her. She sits, rigid.)

MORT: Hello, I'm your doctor. How do you feel?

MARA: All right.

MORT: Headaches? Hallucinations?

MARA: No.

MORT: How old are your parents? Epilepsy? Seizures? Searches? When did you have a bath?

MARA: Never.

MORT: What did they tell you in school? Do you like the feel of cotton sheets? Can you take criticism? Dizzy spells? Ringworm? Rats?

MARA: Nothing.

MORT: How'd you like to die?

MARA: Wait! (Blurred focus: they are suspended between dream and waking.) I need sleep.

MORT: Go to sleep.

MARA: I feel strange. (Again they mesh into the nightmare.)

MORT: Hello, I'm your doctor. How do you feel?

MARA: My watch stopped.

MORT: That's messy. You need a big lead box.

MARA: I need a nap.

MORT: Nap. OK. Procedures and risks involved. First we freeze you, make a small incision, insert a tube up the aorta, watch its progress by fluoroscope.

Then we inject the dye. You'll feel a burning sensation for fifteen seconds. At this point you sometimes have a reaction, but it can't be proven until you die. Then we x-ray the remains and before you clog we yank out the tubes and try to stop the blood. At this point you often think of tall buildings swaying in the wind. We try to keep you back from the edge, but there is a slight chance, say half of one percent, that you may lose your balance and fall.

MARA: Am I worried?

MORT: Twice a day.

MARA: Risk? Is there any risk?

MORT: There's always some risk. Less on a passbook account, but there you get only five and a half percent. Municipals are still a good buy, but if your inner city deteriorates, you're gonna have problems with flushing.

MARA: What about malignancy?

MORT: It's like inflation. Eats away at what you've got.

MARA: How long am I in for?

MORT: Well, you can put it in five-year certificates, but I'd recommend a shorter confinement unless you want long-term security at the cost of short-term inflammation.

MARA: Wait! We're not talking about money

MORT: (Grasping her hand voraciously) I am! I'm a doctor! How do you feel?

MARA: Confused!

MORT: (Suddenly solicitous) That's natural. And I'd love to help you. I'd be more than willing to help you. But I'm a doctor. Medicine is not an exact science. Medicine is an art. I'm an artist.

MARA: It's cold.

MORT: You don't expect all painters to paint rosy pictures. You don't expect all writers to write happy endings.

MARA: Clammy.

MORT: There's comic medicine and there's serious medicine. My medicine makes a statement: Nobody lives forever!

MARA: Ahhhhhhh! (He strangles her. She screams. They wake into reality. lying side by side in bed.)

MORT: What's the matter?

MARA: I was dreaming. You were the doctor.

MORT: That's a laugh.

MARA: If you're the doctor you're safe. Nothing to lose.

MORT: Relax.

MARA: It's like auto mechanics. You never know.

MORT: Relax and get to sleep.

MARA: Beddy-bye.

MORT: And try not to yell when we start.

MARA: Start what?

MORT: Cutting. (Nightmare: he grabs her from behind. cuts her throat.)

MARA: Stop it! Stop! I'm the nurse!

MORT: (Releasing her) Oh my God. Sorry. Here, let me button you up.

MARA: It's all right, I'm on the pill. I

MORT: Thank God. Read me the appointments, we're behind schedule.

MARA: There's Mr. Pillsbury.

MORT: Mr. Pillsbury's cancer. I'm sick of his damn cancer. Everybody got a cancer. It's his funeral.

MARA: There's Mrs. Pillsbury, for an abortion.

MORT: How advanced is the pregnancy?

MARA: He'll be nineteen this fall.

MORT: Nurse, people have no respect for human life. They don't deserve to live.

MARA: There's Dr. Pillsbury

MORT: Dr. Pillsbury? That's not right. I'm Dr. Pillsbury.

MARA: You're on the list.

MORT: But I'm the doctor.

MARA: It's on the list.

MORT: You'll be sorry. I'm the doctor. I'll stand up and shake your hand! (They clasp hands, shake violently.)

BOTH: Hello, I'm your doctor, how do you feel? (Mort sinks down, Mara dominant.)

MORT: Well... I don't feel any lumps. I really need to get home. My driver's license expires on Friday, I have to study for the test, I have to get my eyes opened. Couldn't I still be the doctor?

MARA: I can't find the vein.

MORT: The grass needs mowing, it's getting too high to cut.

MARA: I can't find the vein.

MORT: It's growing too fast. The doctors are amazed.

MARA: I'm the doctor, I can't find the vein.

MORT: But Friday I'm due to expire!

MARA: Gotcha!

MORT: Ahhhhhhhhh! (They wake.)

MARA: Bad dream?

MORT: Doctors.

MARA: Relax. (Blurred focus)

MORT: I should have had it out. In school my friends had everything taken out. I should have done it then.

MARA: Are you the doctor or the patient?

MORT: I forgot.

MARA: It's safer to be the doctor.

MORT: Can he wear a white hat?

MARA: I'll be the doctor, too. Then we're a team.

MORT: A medical team.

MARA: MDs!

MORT: Men in white!

MARA: Doctor!

MORT: Doc! (They embrace, then recoil.)

MARA: Oh dear, I contaminated you.

MORT: I was sterile. Wait! The operation! (Focusing on an imaginary patient) But there's nobody here.

MARA: That's OK. It's practice. Run scrimmage, get the plays down pat, then we shove the patients under there and let fly. We don't ever check the face.

MORT: Unless there's a beard. We don't want a beard in the muck.

MARA: What do you think? Rapid Shave? Drano? Easy-Off?

MORT: Wait. He's not real. He's imaginary.

MARA: Then we better work fast. You take the steak knife, I've got the juicer.

MORT: Roger! (They begin burlesque surgery: broad, gross pantomime.)

MARA: Take that out, I saw it move.

MORT: Arthritis. Out with his bones.

MARA: How about the kidneys?

MORT: Feel OK. Oh-oh, bed's wet. Can't have that.

MARA: You did a no-no.

MORT: Give 'em the heave.

MARA: Squeeze that.

MORT: Not very fresh.

MARA: Mold.

MORT: Out.

MARA: Let's do a brain test. What are the three justifications for existence? Wrong. Take out the brain.

MORT: What about the liver?

MARA: We had liver last night.

MORT: Well, it's cheap.

MARA: Three dollars a pound?

MORT: For that we could buy sweetbreads.

MARA: He didn't complain of sweetbreads.

MORT: Out.

MARA: Better wash all this off.

MORT: Wait. I got a bite.

MARA: All we can do is pray.

MORT: Pull out the plug.

MARA: Locomotor ataxia.

MORT: Dynamite up the kazoo! Take cover! (Catastrophic explosion)

MARA: Got him.

MORT: Is he OK?

MARA: He's dead.

MORT: But he's imaginary.

MARA: He is now. (Blurred focus)

MORT: Hey, what am I doing? I'm not the doctor, I'm supposed to see the doctor...

MARA: No, come on, you better be the doctor ...

MORT: I can't speak Latin. I missed the test. Is there a Band-Aid in the house?

MARA: We're running out of gas ... (He transforms into a concrete character: a fatigued fifty-year-old physician, speaking to us directly.)

MORT: I have a patient. Forty years old. Female. White. The most radiant, life-loving woman I know.

MARA: She's a patient. She's dying.

MORT: She has leukemia. She's dying. I do bone-marrow biopsies. Which are very painful. She's had remission twice. Then it goes on.

MARA: She's losing her looks.

MORT: She tries to joke.

MARA: Symptoms?

MORT: Symptoms? I feel a cold sweat. Shaking. I try to laugh.

MARA: Prognosis?

MORT: Six months.

MARA: Side effects?

MORT: Side effects?

MARA: Any side effects?

MORT: You die.

MARA: Who dies?

MORT: The patient dies.

MARA: Who's the patient?

MORT: The patient pays the piper.

MARA: Then who pays the doctor?

MORT: Whoever's dying.

MARA: Everyone's dying. (Pause. Incredulous)

MORT: No... (Stark awake, they kneel clumsily side by side on the bed, hands in prayer.) I'm the patient now.

MARA: I'm the patient too. (They mumble in shambling unison.)

BOTH: Yea though I walk through the valley of the shadow of Yea though I walk
through the valley of
Yea though
Valley of
Sha
Va
I fear no evil!
No evil.
Yea though I fear no
Yea though I fear no
Yea though I walk through the valley of
The Shadow of

(Their lips form a word, soundlessly. Fade.)
```

---

## IC-0908: Shadow Box

- Title: Shadow Box
- Author (byline): Michael Cristofer
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: June 1977
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: BEVERLY, MARK
- Teaser before the introduction: Yes
- Spoken words (computed): 1329
- Already set (do not supply): none

### Source block (context only)

```text
Author: Michael Cristofer
ISBN: 978-0573616136
Publisher: Samuel French, Inc.
Date (Month/Year): June 1977
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: In this scene from Michael Cristofer’s The Shadow Box, Beverly, Brian’s ex-wife, and Mark, Brian’s gay lover, meet for the first time.

ACTOR: And although the circumstances of this meeting would never be ideal – this meeting occurs because Brian is dying.

ACTRESS: Now we know what you’re thinking . . . AIDS, right?

ACTOR: Wrong. Now, we don’t blame you for jumping to that conclusion. The media has pushed the horror of AIDS for quite some time.

ACTRESS: But unfortunately, it has been to the detriment of other illnesses that lead to an even greater death toll.

ACTOR: Cancer kills more people every six weeks than AIDS is projected to kill this year.

ACTRESS: And that “less publicized” but equally devastating disease is what has brought Beverly and Mark together today.

TOGETHER: The Shadow Box by Michael Cristofer
```

### Performance text (classify this)

```text
BEVERLY: Surprise! Oh, who are you? I’m sorry. I’m looking for Brian . . . uh . . . Two. They said cottage two. I must have . . .

MARK: No. This is two. This is cottage two.

BEVERLY: Oh ! Thank God. Is . . . uh . . . .

MARK: No. Not at the moment. But he should be back any minute.

BEVERLY: Good. I wanted to surprise him and he’s not here. Well, Surprise! Hmmm. Very nice. Very nice. All the comforts of home. Amazing what you can do with a coffin if you put your mind to it.

MARK: What?!

BEVERLY: Oh, sorry. Sorry. Introductions first. That way you’ll know who you’re throwing out. I’m Beverly. No doubt you’ve . . .

MARK: Yes. Brian’s wife.

BEVERLY: Ex-wife

MARK: Former

BEVERLY: Yes. Former. He prefers former, doesn’t he.

MARK: Yes. I figured it was you.

BEVERLY: And you’re . . . uh . . .

MARK: Mark

BEVERLY: Well, now that we know who we are . . . how about a drink?

MARK: A what? Oh, no. We don’t keep any liquor here. I could get you some coffee or some penicillin, if you’d like

BEVERLY: No. No. I was inviting you. I had an accident with the scotch on the way out here. There’s quite a dent in it. Anyway, we both look like we could use a little. Hmm?

MARK: No. I don’t drink.

BEVERLY: Ah, a dope man.

MARK: Neither. I like to avoid as much poison as possible.

BEVERLY: I see.

MARK: Well, you go ahead if you feel you have to.

BEVERLY: No. No, really. I don’t need it. I mean. I’m not . . . Forget it. So. How is he?

MARK: Dying. How are you?

BEVERLY: Ooooops. Let’s start again. Is he feeling any pain?

MARK: Are you?

BEVERLY: Strike two. Well, think we’ve got it all straight now. He’s dying. I’m drunk. And you’re pissed off. Did I leave anything out?

MARK: No. I think that just about covers it.

BEVERLY: Tell me. How is he?

MARK: Hard to say. One day he’s flat on his ass, the next day he’s running around like a two-year-old. But he is terminal – officially. He has fainting spells. They’re harmless. Well, that’s what they tell me. But it’s embarrassing for him because he falls down a lot and his face gets a little purple for a minute. I just want you to know. If you’re staying around. I mean, I think it would hurt him if people noticed.

BEVERLY: Well, if he turns purple and falls on the floor, it’d be sort of difficult not to notice, wouldn’t it?

MARK: Look. I don’t mean to be rude or stupid about this . . .

BEVERLY: Why not? I like people to be rude and stupid. It’s one of the ways you can be sure they’re still alive.

MARK: You’re very stoned aren’t you? And you’re dressed in funny clothes, and you’re saying a lot of funny things but I’m just not sure, frankly, what you’re doing here.

BEVERLY: Neither am I.

MARK: . . . . when I met Brian, I was hustling outside a bar in San Francisco. Right after the great “Summer of Love.” People were starving to death in the streets.

BEVERLY: Sounds lovely.

MARK: Like everybody else, I was very hungry, very desperate. So there I was one night, selling it down on Market Street. I wasn’t very good at it, and Brian walks up to me . . . and asks me the time. Right? Well, I did my little number about time for what and how much it was worth to him . . . and all of a sudden, he starts explaining exactly what time was worth to him . . . time warps even! Jesus, I though, I’ve got a real freak on my hands. And he’s talking and talking and talking. Finally, I say “Look man, I haven’t eaten in a long time, and I’m getting a headache. Why don’t we talk some business before I starve to death?”

BEVERLY: What did he do?

MARK: He bought me dinner! I couldn’t believe it. I mean, what did he want from me? And he never stopped talking. Never.

BEVERLY: He didn’t want anything from you.

MARK: It doesn’t matter, and that’s how I got to know him. I got interested in what he was doing. He gave me a room. I could use it whenever I wanted. We talked and talked endlessly. What am I talking about?

BEVERLY: Dead people.

MARK: Exactly! I mean, exactly!

BEVERLY: Exactly what?

MARK: I mean it’s not enough! We are dying here lady. That’s what it’s about. Brian looks at me and I can see it in his eyes. You can wipe up the mucous and the blood and the piss. You can burn the sheets and boil his clothes, but it’s still there. You can smell it on him. You can smell it on me. It’s sick and putrid and soft and rotten and it’s killing me.

BEVERLY: It’s killing him too.

MARK: That’s right, lady. And some of us have to watch it. Some of us have to live with it and clean up after it. Some of us are here for the duration. . . . And it’s not easy.

BEVERLY: And some of us wouldn’t mind changing places with you at all.

MARK: And some of us just don’t care anymore.

BEVERLY: What?

MARK: Some of us just don’t care.

BEVERLY: You’re cute, Mark. But next to me, you are the most selfish *person* I’ve ever met.

MARK: Oh, wonderful! That’s exactly what I needed. Yes, sir. That’s just what I needed.

BEVERLY: Let me tell you something– what you do is your business. You can drag *yourself* through every gutter from here to Morocco. You can trade it, sell it, or give it away. I don’t care. I’ll even show you the best way to do it. But Brian is different. Because Brian is different. Because Brian is stupid. Because Brian is blind. Because Brian doesn’t know where you come from or who you come from or why or how or even what you are coming to. Because Brian happens to need you. And if that is not enough for you, then you get yourself out of his life – fast.

MARK: That simple, huh?

BEVERLY: When the money and the time and the people are all running out faster than you can count, and the reasons don’t sound as good as they used to and you don’t remember any more why . . . why you walked out on the one person who said yes, you do what you have to because I love you. And you can’t remember anymore what it was you thought you had to do or who you thought you were that was so important that you couldn’t hang around long enough to say goodbye or find out what it was you were saying goodbye to . . . One human being who cares. My God, why isn’t that ever enough?

MARK: You want an answer to that?

BEVERLY: I want you to get yourself together or get yourself away from him.

MARK: Just leave? I can’t leave him.

BEVERLY: Why not?

MARK: I owe him.

BEVERLY: What? Pity? I mean, what’s in it for you?

MARK: Nothing’s in it for me.

BEVERLY: He’s just a tired, sick old man . . . A tired old trick with some phoney ideas that don’t hold water . . . a broken-down sewer, that’s all he is.

MARK: I didn’t say that . . .

BEVERLY: You don’t need that. You don’t need to dirty your hands with that kind of rotten putrid filth. Unless of course you need the money. What does he do – pay you by the month? Or does it depend on how much you put out?

MARK: . . . I don’t want him to die. I don’t . . . Please . . . I don’t want him to die.

BEVERLY: Hopes, baby. That’s what you got. A bad case of the hopes. They sneaked up on you when you weren’t looking. You think maybe it’s not gonna happen. You think maybe you’ll find some way out. Some word that still alive, some word that will make it all different . . . Please, baby, just one favor you owe him. Don’t hurt him. Don’t hurt him with your hope. He needs somebody. That was my answer, too . . . Bye, baby.

MARK: Wait . . . .

BEVERLY: Tell Brian goodbye for me

MARK: Don’t you want to see him?

BEVERLY: No, I’ve got a plane to catch. It’s funny. He always makes the same mistake. He always cares about the wrong people.
```

---

## IC-0909: The Shape of Things

- Title: The Shape of Things
- Author (byline): Neil LaBute
- Work: Not specified
- Publisher: Faber and Faber, Inc.
- Publication date as stated: Nov 2001
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: EVELYN, ADAM, JENNY
- Teaser before the introduction: Yes
- Spoken words (computed): 1677
- Already set (do not supply): none

### Source block (context only)

```text
Author: Neil Labute
ISBN: 978-0571212460
Publisher: Faber and Faber, Inc.
Date (Month/Year): Nov 2001
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: How far would you go for love? For art?

ACTRESS: What concessions would you make? What price would you be willing to pay?

ACTOR: Such are the painful questions explored by Neil Labute in The Shape of Things

ACTRESS: A modern retelling of the fall of man.

TOGETHER: The Shape of Things by Neil Labute
```

### Performance text (classify this)

```text
NOTE: This cutting asks one student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles: Actor: Adam

Actress: Evelyn and Jenny

EVELYN: (To audience) Good evening. I promise to make this presentation as quick and painless as possible. My task tonight is to unveil my semester’s work. . . Oh, I almost forgot . . . and this is fairly personal, so please indulge me. (beat) I was given an engagement ring two days ago and I haven’t answered the guy yet (Show ring on finger) . . . so I wanted to do it this evening. (To Adam) Here goes. This is a beautiful stone and an amazing gesture on your part. By the time I’m through here, I promise that you’ll have your answer . . .

EVELYN: I present to you this, my newest work. It is a human sculpture on which I’ve worked these past eighteen weeks, and of whom I’m very proud. The piece itself – him – is untitled. I first spotted my chosen base material . . . it’s so funny not to use names! Sorry, but a lawyer actually told me I had to say that, ‘base material’ . . . on January 9, the fifth day of winter semester. I created a scenario that would allow for our seemingly random connection. *****Scene*****

(EVELYN stands near a stretch of velvet rope. She has a can in one hand and stares up at an enormous human sculpture. ADAM steps across the barrier and approaches her) Authors note: The / in lines denotes an attempt at interruption or overlap by a given character.

ADAM: . . . you stepped over the line, miss? / Ummmm, you stepped over . . .

EVELYN: I meant to / step over . . .

ADAM: What? / yeah, I figured you did. I mean, the way you did it an all, kinda deliberate like./ you’re not supposed to do that.

EVELYN: I know / that’s why I tried it . . . to see what would happen.

ADAM: I’m what happens, I guess. I have to walk over, like I’ve done, and ask you to take a step back.

EVELYN: And if someone doesn’t / what then?

ADAM: Hell, I dunno . . . I’m off in, like, ten minutes, I’d probably just stand here, make sure you didn’t touch anything. Hey, you’re not gonna mess up my weekend with this, are you?

EVELYN: I wasn’t planning on it, but . . . I’m not completely against it, either.

ADAM: See, if you get all crazy, then I gotta write up a report and stuff, I’m here till six, six-thirty easy, and I have a second job to get to. . . step back behind the line there . . . I’d appreciate it.

EVELYN: No. sorry, I can’t. I’m building up my nerve, and if I go back over, I’ll probably be a big wuss about it and take off . . .

ADAM: About what? The ‘wuss ’part, I mean . . .

EVELYN: I was going to do something to the nude. Mess it up or . . . paint a big (gestures) on it, but whatever . . .

ADAM: (beat) . . . so, right over the leaves there, or just a free-floating number.

EVELYN: probably anatomically correct. I mean, if you’re gonna do it, why not . . .

ADAM: . . . do it right? Absolutely.

*****Scene*****

EVELYN: The hair, the glasses, the excessive amount of weight offered a number of physical areas that made him unique and perfect for this project. A short list of alterations I’ve induced would include eating better and losing weight – some twenty-five pounds or more *****Scene*****

ADAM: . . . . You amaze me.

EVELYN: I’m glad. (beat) and you amaze me, you do. Look at you!

ADAM: It’s just a little jogging.

EVELYN: No, it’s not. It’s not just that . . . you’re running, you’re eating better. Are you still lifting?

ADAM: Yeah . . . I mean, I didn’t today, but . . . .

EVELYN: Do you like doing it?

ADAM: Honestly . . . No. It totally hate it! (they laugh)

EVELYN: So why would you . . . ?

ADAM: Because you suggested it. Which is kinda pathetic, but true . . .

EVELYN: You shouldn’t do something you don’t wanna do.

ADAM: Yeah, you should. Why not? If it’s for some one . . . I mean, I’m doing it for you.

EVELYN: I gave you a couple ides and you’re changing your entire life. I’m very proud of you.

(Adam freezes in scene and Evelyn steps out to resume her presentation)

EVELYN: . . .the purchase of contact lenses *****Scene***** Adam and his friend Jenny in the park

JENNY: You are getting cuter by the day. What is that girl doing to you?

ADAM: Lots . . . she’s amazing, really.

JENNY: What happened to your . . . are you wearing . . . Adam, are those contacts?

ADAM: Yeah, contacts.

JENNY: My god, this from the former ‘tape around the nose thing-y’ champion.

ADAM: That was only for a week, that one time!

JENNY: Still, you’ve gotta admit . . .

ADAM: I do, it’s amazing. I feel better . . .

JENNY: Better? You’re like, this totally hot guy now . . . (beat) I always thought you were handsome, anyway, but I didn’t think you’d go in for the makeover thing.

ADAM: Me either. Who knew? (Adam freezes in scene and Evelyn steps out to resume her presentation)

EVELYN: A complete change in hairstyles and significant wardrobe alterations as well. He even tattooed his body for me, without asking . . . in a highly questionable place. *****Scene*****

ADAM: I can show you something . . . just a little thing I had done. For you.

EVELYN: Wait, what . . . show me. (he looks around and lowers his pants to show his backside) “EAT” . . . lemme guess . . . you couldn’t afford the “me.”

ADAM: No, you goof! Your initials: Evelyn Ann Thompson. Like it?

EVELYN: I do. I like it. And I love the gesture . . .

ADAM: “Love” is a big word.

EVELYN: I know. That’s why I used it. . . (Adam freezes in scene readjusting his pants and Evelyn steps out to resume her presentation) These are surface items, to be sure, but if I, in fact, tell you that I’m going through with it and marrying the guy, you’d probably all shake my hand and say, “Wow, how can I do that to my boyfriend?” But this, I’m afraid was not done out of love or caring or concern . . . this was a simple matter of can I instill “X” amount of change in this creature, using only manipulations as my palette knife? I coaxed, made suggestions, created the illusion of interest and desire, but never said, ‘please do this.’ Not once. As my subject became handsomer, firmer and more confident, his actions became more and more . . . questionable. He had work done to his face, cosmetic surgery at age 22, and insisted to those around him that he had merely fallen down. *****Scene*****

ADAM: (To audience as if speaking with friends, gesturing to his nose) I hit it and, you know . . . I banged it pretty bad at home and so I had the doctor look at it. But he didn’t . . . operate or anything. The bandage is from that . . . (Adam freezes in scene touching his nose and Evelyn steps out to resume her presentation)

EVELYN: He was willing to give friends up when asked, walk away from them without any further contact . . . and as stated earlier these corrections culminated in an offer of marriage to me, this coming from a confirmed, albeit young, bachelor.

*****Scene*****

(We enter the scene in the middle of an argument between Evelyn and Adam – the reason for the argument is unimportant, just the conclusion)

ADAM: So, tell me what to do and I’ll do it. . . I just, I just don’t wanna lose you.

EVELYN: You’re sure . . . ?

ADAM: I am so sure. I love you . . .

EVELYN: Anything I say?

ADAM: Anything.

EVELYN: (without emotion) Give up [your] friends, both of them. No explanation. Don’t see them or speak to them again, not ever. That’s the proof to me about how you feel . . .

ADAM: Evelyn . . . that’s . . .

EVELYN: Once should always be careful when asking to be put to a test. . . so what’s it gonna be, Adam?

ADAM: . . . and if I don’t . . . ?

EVELYN: These things end. I mean, in life, at least . . . Final answer? (Adam stares at her for a long moment)

ADAM: . . . I choose you. (Adam freezes in scene after dropping to one knee as if to propose and Evelyn steps out to resume her presentation)

EVELYN: He has then been utterly and totally refashioned as a person (beat) He’s gotten more interesting, more desirable, more normal. In a word, better. He is a living, breathing example of our obsession with the surface of things, the shape of them. (to ADAM – taking off the ring) This was a startling and unexpected gesture, but obviously, I can’t accept. (To audience) I have no feelings of remorse for my actions, the manufactured emotions . . .

none of it. I have always stood by the single and simple conceit that I am an artist. Only that. Art must be created, whatever the cost. (beat) @ith that in mind, I present you with my untitled sculpture. Thank you. (she hands Adam the ring, takes a short bow and steps out of the light.) *****Scene***** At the reception after Evelyn’s presentation

ADAM: . . . not a big "modern art" crowd, I guess, huh?

EVELYN: Look . . .

ADAM: Please don't "Look,” me now, okay, or I might not make it through this. . . (beat) Just refer to me as "it" or "untitled," it'll help me keep some perspective here. . . (wanders over and pours some punch. Stuffs a few cookies in pocket. Shoves three in mouth and chews them down.). . . that's gonna shoot some piece of data all to s***, isn't it?

EVELYN: Doesn't matter now, do what you want. . . you're finished.

ADAM: "You're finished." Wow. (considers) Most people just say, "Hey, sorry, can't marry you." And they say it in private. . .

EVELYN: . . . yeah, that might've been a bit too far.

ADAM: Oh shit, you are so beyond "far" that you're in danger of hitting Uranus.

EVELYN: (Smiling) See, you're still funny....

ADAM: Just stop, alright? I was never funny, or good-looking or clever. I was nothing until you started . . . I admit it. No-thing. But you know what? I was absolutely fine with that. . .

EVELYN: . . . listen, I know my work relied on not telling you what was going on, but I. . .

ADAM: Here we just call it lying. . .

EVELYN: I did lie to you, yes . . . Sorry.

ADAM: You're sorry? Well, that's good. . . I figured I was gonna have to really work to get that one out of you.

EVELYN: I'm not sorry. I mean, not for what I've done. I just feel bad that you're so upset. . . I just want to keep it as truthful as possible.

ADAM: (laughing) That'll be different. . .

EVELYN: . . . you're so angry. . . What'd I do wrong? (beat) Seriously, tell me. . .

ADAM: You don't see this as wrong?! You honestly have no concept here. . . Look, I’m not gonna stand here. . .

EVELYN: The exercising? Or was it the new clothes that really bugged you? Everything I did made you a more desirable person. People began to notice you. . . take interest in you.

ADAM: Well, lucky me.

EVELYN: (beat) Look, if you hadn't been here tonight, hadn't heard all this stuff. . . wouldn't you still be happy? Waiting at home for me, hoping this went well. . .

ADAM: That's not the point. . .

EVELYN: Yes, it is! It's the total point. All that stuff we did was real for you, therefore it was real. It wasn't for me, therefore it wasn't. It's all subjective, Everything.

ADAM: Not love. Not cruelty. Seriously? . . . Don't fool yourself and think that this is "art." 'kay? It's a sick joke, but it is not "art."

EVELYN: Is that right?

ADAM: (beat) You know, when Picasso took a s***, he didn't call it a "sculpture." He knew the difference. That's what made him Picasso. You oughta at least realize there's a price to it all...you know? Somebody pays for your two minutes on CNN. Someone always pays for people like you. And if you don't get that, then you're about two inches away from using babies to make lamp shades and calling it "furniture." (beat) Tell me, though. Was any of it true? Not the things we did, or the kind words or whatever. . . but any of it?

EVELYN: . . . No. Not really. Sorry.

ADAM: (Sarcastic) Don't be. Hey, it's. . . Art.
```

---

## IC-0910: Sharpies

- Title: Sharpies
- Author (byline): David Narter
- Work: Best Ten Minute Plays of 2019
- Publisher: Smith and Kraus
- Publication date as stated: March 2019
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: CHRISTINA, BRETT, MR. GLENN
- Teaser before the introduction: Yes
- Spoken words (computed): 1412
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Narter
Book: Best Ten Minute Plays of 2019
ISBN: 978-1575259338
Publisher: Smith and Kraus
Date (Month/Year): March 2019
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: It's that time of the year!

ACTRESS: Application forms, tests, early admission, teacher recommendations, and even a sleepless night or two.

ACTOR: Time to apply for college? Try preschool!

ACTRESS: Twenty years ago, they just had to show up and not eat glue.

ACTOR: These days it seems that if a kid isn’t ‘gifted’, they’re behind.

ACTRESS: In fact, in many of the larger cities (New York, San Francisco, Chicago) spots are limited and it can be super competitive.

ACTOR: What exactly are elite pre-schools looking for?

ACTRESS: According to Patty Washburn of the North Shore Country Day School, "We are not looking for children who can just handle the program; we also want children who can give something back to the class."

ACTOR: So often, applicants

ACTRESS: (ie children)

ACTOR: are observed in a “play-date” setting with numerous others to see how they fit in.

TOGETHER: Sharpies by David Narter.
```

### Performance text (classify this)

```text
Suggested Roles: Actress – Christina Actor – Brett and Mr. Glenn

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

(BRETT and CHRISTINA are in a waiting room in which there is a single chair upon which is a scattering of brochures and forms. CHRISTINA is pacing. Frequently, they look toward the audience - the window of the playroom.)

CHRISTINA: Oh, God. This is so nerve-wracking.

BRETT: No. Tyler's fine. He'll do fine. (Long pause)

CHRISTINA: Did you talk with him last night?

BRETT: Excuse me?

CHRISTINA: When you two were out for ice cream, you were supposed to talk to him about this.

BRETT: About what? What am I supposed to tell him? Be smart?

CHRISTINA: So you didn't talk to him? Brett, you were supposed to let him know the situation and what was expected of him.

BRETT: Oh, Christina. C'mon. Does it really matter what I say to him? He's going to be doing arts and crafts and listening to story time.

CHRISTINA: Yes, it matters! Some of these kids are going to cry as soon as they get here and some kids are going to be comfortable in the situation and doing what they're supposed to do - maybe going beyond what's expected, Brett. Are you familiar with that expression, Brett? Beyond what's expected?

BRETT: Christina, I'll be happy if he doesn't eat the paste.

BRETT: Seriously, how does watching him play tell them anything about him.

CHRISTINA: It doesn't, Brett. It tells them about us.

BRETT: What?

CHRISTINA: How we parent. That's what they want to know.

BRETT: So this is about us. Don't you think that's a little self- centered?

CHRISTINA: Ugh! So did you tell Tyler anything at all, Brett?

BRETT: Well actually, I told him ... (in an announcer voice) "kill the competition!"

CHRISTINA: What are you talking about?

BRETT: It's an ad. It was an ad for Home Depot or something. He was a little freaked out, and I told him it was a figure of speech about competition and doing your best. I told him ... confidence. (reconsiders and then comes back to it) Confidence.

CHRISTINA: Oh. Oh. Well, good.

BRETT: Yeah. You know, I wasn't really talking about this at all though. It was actually - to be honest, I think he was kind of freaked out about the slogan. So, I just kind of generalized.

CHRISTINA: Well, sure. You tell a toddler to "kill the ... "

BRETT: Right. Listen, Christina, I said that there's lots of people and you have to do your best if you want to get noticed. That's all.

CHRISTINA: Right. Well good. That's good. That's good. So why didn't you just tell me that when I asked?

BRETT: Because I wasn't really talking about this. I mean I think he really thought about it, but I don't remember if I really said anything specific about today.

CHRISTINA: Hmm. Well, that's fine. I did.

BRETT: Yeah? When?

CHRISTINA: When we were driving in.

BRETT: What'd you say?

CHRISTINA: Same as you.

BRETT: Yeah?

CHRISTINA: Yeah, I told him that there are a lot of other kids who he'll see in his life and a lot in the room today and there are winners and there are losers. I told him it's best to think of himself as the sun and always make sure the teacher can see him shining bright. And that it is his job to be sure no one got in the way of his sunshine. (Long pause)

BRETT: Oh.

CHRISTINA: I just reminded him that it's a big world. And one little person can get crowded out by a lot of the mediocrity around him if he doesn't make sure he gets himself in the front of the line. Just like you - kill the competition.

BRETT: Just like me? I told him to be confident! I didn't tell him to "kill the competition"!

CHRISTINA: Well, neither did I.

BRETT: Are you kidding????

CHRISTINA: (realizing this is getting out of hand) Brett. Brett. Listen. Listen. You said it before. This isn't about Tyler. It's about us.

BRETT: I didn't say that. You did.

CHRISTINA: Anyway. We don't want to be arguing when they're watching him. Tyler is going to be Tyler and he's a part of us both. And I'm sure they'll see the best of us when they see him. Okay? Okay?

BRETT: Yeah, you're - right. (looks to audience: a glass through which they can see Tyler play) Hey, there he is!

CHRISTINA: Hey, baby. Who's my little handsome man? (MR. GLENN enters)

MR. GLENN: Oh, he can't see you. That's a one-way window -- or mirror. I suppose it all depends on which side you're on.

BRETT: Well, that's a little creepy.

MR. GLENN: Oh, for the most part it's pretty benign. We use it to evaluate staff members usually. But of course, assuming Tyler is accepted into the program, you're always welcome to watch him play without affecting the ... the chemistry of the classroom environment.

CHRISTINA: Oh. That's nice. What a little fella. He's gonna do a little painting.

MR. GLENN: He's an interesting young man.

CHRISTINA: Really?!

MR. GLENN: Absolutely. We had a good conversation before we went in. He told me he got ice cream last night.

BRETT: Yes he did.

MR. GLENN: He also said something about the radio scaring him. It seems he was a little anxious about it.

CHRISTINA: Really?

BRETT: Yeah. There was some ad - really freaked him out. I changed the station.

CHRISTINA: Yeah. Tyler's a very quiet - well - thoughtful boy. He thinks a lot. (long pause)

MR. GLENN: Well, that's good.

BRETT: Oh, look at that. He's got himself a girlfriend.

CHRISTINA: No, no. Tyler's teaching her how to paint.

BRETT: Yeah, how ‘bout that? They're painting together.

CHRISTINA: No. He's teaching her.

MR. GLENN: Really?

CHRISTINA: He's teaching her how to paint. See he's helping her hold the brush. No. No. Take turns, now. Hmm.

BRETT: Whoa, yeah that's not a lesson. That's a fight.

CHRISTINA: Nonsense, he's helping her, but she's not paying attention.

BRETT: Hmm. Nope they're fighting over that brush. Yeah, that's a fight.

CHRISTINA: Well, of course it's not a fight. Tyler is twice her size. He's helping her.

BRETT: I don't know. Okay, that's a shove.

CHRISTINA: Hey, now! That really was a shove. That little girl just pushed Tyler down. Mr. Glenn, shouldn't the teacher be interceding at some point?

MR. GLENN: I'm not sure that she's seen it yet. Oh! (All of them gasp in horror)

BRETT: Oh, my God. That's just right in her eye!

CHRISTINA: No, of course it isn't.

BRETT: Oh, it's in there.

MR. GLENN: Oh dear. (calling to be heard through the window) Mrs. Schiff!

CHRISTINA: That's not his fault.

BRETT: Christina.

CHRISTINA: It's not his fault. That girl was pulling and he just let go. He was letting her have the brush. He was being generous!

MR. GLENN: Finally, she's noticed.

BRETT: Whoa that was quick!

MR. GLENN: We do have a nurse on sight. And if that button is pushed ... well, as you can see, she's there in an instant.

BRETT: Jeez, I am so sorry ... I don't know what happened there.

CHRISTINA: It was an accident.

MR. GLENN: Of course. Of course it was.

CHRISTINA: Tyler no, no. No, honey. There are other brushes, you don't need that one. Not that one! (Horrified gasp from all three)

BRETT: Oh. That just popped right out.

CHRISTINA: What? Why is she yelling at Tyler? Oh, c'mon now. She's just upsetting him more.

BRETT: (rushing to the door of the observation room) Okay, this is over. I'm going ... (the door is locked) Mr. Glenn. Do you have a key?

MR. GLENN: No. I didn't even know there was a lock.

BRETT: Well, there's something keeping this from opening!

MR. GLENN: Dear God. He's locked us in here.

CHRISTINA: That's ridiculous. Tyler could not have done that.

BRETT: There's no way out!l!

CHRISTINA: Tyler, honey. This is mommy. It's okay. It's okay.

MR. GLENN: He's going for the scissors!

BRETT: No, Tyler!

CHRISTINA: Tyler! Tyler! Use the roundies, honey. Not the sharpies, not the sharpies!

(Both men freeze and look at Christina in shock. Then, looking back at the window, they all gasp in terror)

BRETT: There goes the nurse.

MR. GLENN: (patting his pockets) He's taken my cellphone!

BRETT: Christina. Your phone.

CHRISTINA: Don't be rude, Brett. (Brett makes a dash for her purse and rifles through it till he gets the phone)

CHRISTINA: No. No. Tyler. That's not nice. Gentle hands. Gentle hands.

BRETT: (fumbling with the phone) C'mon! C'mon!

CHRISTINA: Don't you run with those scissors.

MR. GLENN: Why is he climbing up there? (Their eyes follow him up a jungle gym)

CHRISTINA: He's playing king of the mountain! He's a little Moufasa! (She does a tiny wave) Look, Brett. They're all his little subjects! (Their eyes follow him jumping from the jungle gym. Again, the men gasp in horror and Brett drops the phone.)

BRETT: Oh, God.

CHRISTINA: Tyler. Mouths are for food. No biting! No!

MR. GLENN: Oh, that's the entire ear!

CHRISTINA: Tyler, no! People are not food! No! (Suddenly they all exhale.)

MR. GLENN: Oh, dear God.

CHRISTINA: Oh, look who's tired. No. No. Find your own space. Let her sleep. No! (As the men become even more shocked) Hands to yourself, Tyler. Hands to yourself!

MR. GLENN: How did he ... ? He knew exactly where the heart was.

BRETT: Well, that's something.

CHRISTINA: We have a few anatomy CD's. He's very advanced.

MR. GLENN: Dear God, he's walking to window.

BRETT: It's like he can see us.

MR. GLENN: He's looking right at us!

CHRISTINA: Hi, baby. (In baby talk) Who's got the messy red hands? Who's my messy boy? No. No. Wipe on a towel sweety. Not the window.

MR. GLENN: (recoiling in terror) He sees us! He sees us!

CHRISTINA: Don't be silly. He's writing letters. C - 0 -

MR. GLENN: They're backwards. Oh God! He can see us!

CHRISTINA: I know. He is very smart. Aren't you Tyler sweetie! Aren't you!

BRETT: N - F - I - D -

MR. GLENN: Confidence. He spelled confidence.

CHRISTINA: Oh, my little Moufasa is tired. Look at the little angel. He's just gonna lie down and have a "widdle nappie." (She watches him lovingly while Mr. Glenn cowers in the corner, panting)

BRETT: Mr. Glenn. I'm so ... well, I just don't know what to say.

MR. GLENN: There's nothing to say.

BRETT: Of course. Of course ... I just ... this is just... unbelievable.

MR. GLENN: Yes. Yes. (He collects himself and organizes his notes. He then pulls two sheets from the stack.) Well. You'll need to fill out these two forms. And I'll need a copy of Tyler's physical and a copy of your insurance card.
```

---

## IC-0911: A Short History of Weather

- Title: A Short History of Weather
- Author (byline): Jonathan Yukich
- Work: The Best 10-Minute Plays for 2 or More Actors 2009, Pg 70-76
- Publisher: Smith and Kraus
- Publication date as stated: Dec 2009
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: EARL GREY, ALOE VERA, BOTH
- Teaser before the introduction: No
- Spoken words (computed): 1297
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jonathan Yukich
Book: The Best 10-Minute Plays for 2 or More Actors 2009, Pg 70-76
ISBN: 978-1575257594
Publisher: Smith and Kraus
Date (Month/Year): Dec 2009
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: (as if they have already been playing this game for a while) Okay, Okay, next one . . . RAIN.

ACTRESS: (singing) It’s raining, It’s pouring. The Old Man is snoring . . .

ACTOR: Life isn’t about waiting for the storm to pass . . . it’s about learning to dance in the rain. (he dances)

ACTRESS: April showers bring May flowers . . .

ACTOR: If a kid asks where rain comes from, tell him "God is crying." And if he asks why, tell him, "Probably because of something you did." (both laugh)

ACTRESS: Join us on a quick romp through the courtship and marriage of a weather-obsessed couple: Earl Grey (motions to Actor)

ACTOR: and (motions to Actress) Aloe Vera in

TOGETHER: A Short History of Weather by Jonathan Yukich
```

### Performance text (classify this)

```text
Earl Grey gazes into the sky, surveying, then speaks to the audience.

EARL GREY: (Pg 70-76) What's today's weather? What's tomorrow's? Next week's? Have you noticed? Checked? I have. I know the weather very well, or try to. I'm not gloating, just saying. The weather's very important. Critical. It never leaves. (A female yelp is heard, followed by a thud) My wife fell from the sky on a cold, misty morning.

ALOE VERA: Oh gosh! Fallin' from the sky stings!

EARL GREY: Fifty-eight degrees, with a slight southwesterly breeze. Curious, and in the market for a mate, I move toward the stranger.

ALOE VERA: Oh, I think my face is broken! What misfortune!

EARL GREY: Miss, are you all right?

ALOE VERA: (Shielding herself.) Don't look! I’m unseemly!

EARL GREY: You took quite a dive.

ALOE VERA: I should be dead!

EARL GREY: Now, don't say that. Let me have a look. (He draws her hands from her face)

EARL GREY: Oh my . . .

ALOE VERA: I know! Ghastly, aren't I! A she-beast! I was cute once, I swear!

EARL GREY: You still are. As cute as a bunny.

ALOE VERA: Don't goad me. I can take it. I'm a mutant!

EARL GREY: On the contrary . . .

ALOE VERA: I am! AIl because of air balloons! Such an impractical way to travel!

EARL GREY: Outdated, yes.

ALOE VERA: Hours ago I boarded one. Mostly cloudy, highs in the mid-eighties. Out for a stroll, enjoying the grandness of life and climate, when, suddenly, the parachute valve locked up! There was no way to land! I was terrified!

EARL GREY: Naturally.

ALOE VERA: Here I am, stranded in midair, helpless, sailing closer and closer to outer space where I'd probably combust or evaporate, right?

EARL GREY: Very likely.

ALOE VERA: So I gambled and hurled myself overboard, without thinking of the pain or what it'd do to my face.

EARL GREY: Your face is lovely.

ALOE VERA: Oh, cease your niceties! I'm a disfigured hag! Give it to me straight, why don't you!

(Earl Grey kisses her with feeling)

ALOE VERA: I didn't get your name.

EARL GREY: Earl Grey. And yours?

ALOE VERA: Call me Aloe. Aloe Vera.

EARL GREY: Aloe Vera, I'd like to spend a lifetime with you.

ALOE VERA: Our wedding day is sunny and clear. (scene change . . . wedding music)

EARL GREY: Dewpoint: 12 percent.

ALOE VERA: Earl Grey rents a gazebo. I decorate with papier-mâché.

EARL GREY: Do you take this man, me, to be your lawfully wedded husband?

ALOE VERA: I do. Do you take this woman, me, to be your lawfully wedded wife?

EARL GREY: I do. (Loud, celebratory music. They dance -- Music and dance cut abruptly.)

ALOE VERA: After honeymooning at the South Pole, life ensues.

EARL GREY: Our future spreads before us like a broken mirror.

ALOE VERA: It's time to get jobs.

EARL GREY: Be adults.

ALOE VERA: I land a position as a phone psychic.

EARL GREY: I become a traveling gutter salesman.

ALOE VERA: Tough rackets.

EARL GREY: You'll find most homeowners are content with their gutters.

ALOE VERA: And few psychic callers want to discuss the weather.

EARL GREY: (As a caller) Ring-a-ding!

ALOE VERA: Phone psychic! How can I help!

EARL GREY: Will I ever know true love?

ALOE VERA: How 'bout this jet stream we've been seeing?

EARL GREY: (Hanging up) Who gives a flip, you fake! Click!

ALOE VERA: Sadness.

EARL GREY: Our lives become mundane.

ALOE VERA: One dimensional.

EARL GREY: Lethargic.

ALOE VERA: So, we buy a cat and name her Karen. (Aloe Vera is suddenly holding a cat)

EARL GREY: Yeow!

ALOE VERA: Hey kitty, kitty.

EARL GREY: So soft, so sweet.

ALOE VERA: A real part of the family.

EARL GREY: Then one icy winter evening . . .

ALOE VERA: Earl Grey backs over Karen with his gutter van.

EARL GREY: Yeow!

ALOE VERA: A deep depression sets in.

EARL GREY: The only cure is twins. (Crying babies sound. Both are suddenly holding babies)

ALOE VERA: They're born during the summer solstice.

EARL GREY: A long day, indeed.

ALOE VERA: One girl, one boy.

EARL GREY: From the start, we could see the girl was intelligent and resourceful.

ALOE VERA: We name her Google.

EARL GREY: The boy, dull and common.

ALOE VERA: We name him New Hampshire.

EARL GREY: For a while, we're the happiest family. (Celebratory music. Dancing. Cuts abruptly)

ALOE VERA: But funds dwindle.

EARL GREY: Aloe Vera loses her psychic job.

ALOE VERA: Didn't see it coming.

EARL GREY: And, despite the reliability of rain, the great gutter boom never unfolds.

ALOE VERA: I decide to speak to Earl Grey. (To Earl) Earl Grey, I feel somethings missing from our lives.

EARL GREY: I feel it too, Aloe Vera.

ALOE VERA: Two kids, three mortgages, a pile of bills. . . where's the money gonna come from?

EARL GREY: Crime.

ALOE VERA: Earl Grey was right. The only reasonable option was crime. (Babies are tossed. Both pick up guns)

EARL GREY: Our first bank robbery comes on a storybook spring day.

ALOE VERA: Barometric pressure: 30.20 and rising.

EARL GREY: Blue skies and golden sunshine.

ALOE VERA: Perfect for a picnic.

EARL GREY: (Gun pointed) THIS IS A HOLDUP! GET YOUR HANDS UP, MAGGOTS!!!

ALOE VERA: (Gun pointed) DO IT NOW! OR I'LL BLOW OFF YOUR UGLY HEADS! (Distant sirens; they take the loot and run)

EARL GREY: What a rush!

ALOE VERA: Our own private fortune!

EARL GREY: Google and New Hampshire won't have to worry again.

ALOE VERA: And I don't feel guilty, not in the least.

EARL GREY: Who knew we could be so bad? (Loud music, jubilant dance. Cuts abruptly.)

ALOE VERA: Google goes to college, becomes an engineer, and invents a mechanized wind chime.

EARL GREY: We're very proud.

ALOE VERA: Meantime, New Hampshire drops outta school and joins a grunge band called The Sweaty Pickles.

EARL GREY: We're very disturbed. (As if to his son) What's wrong with your biscuit, boy! You haven't left the garage in three weeks! It's time you stop playing this hullabaloo and think about your future! Make somethin' of yourself! Go in the market for a mate!

ALOE VERA: Financially, however, things are looking up.

EARL GREY: With the extra loot, I’m able to expand the gutter business into monsoon regions.

ALOE VERA: Cha-ching!

EARL GREY: And for our twentieth anniversary, we splurge on a trip to Egypt.

ALOE VERA: Where a massive sandstorm ensnares our hotel.

EARL GREY: We watch from our penthouse balcony, knowing we might perish bur unafraid still.

(Gusting winds. Both are awed by what they see.)

ALOE VERA: Isn't it remarkable?

EARL GREY: Wondrous. (Down on one knee, pulling out a ring) Aloe Vera, your falling from the sky was the most amazing gift. I'd like you to have this, love, as a token of my renewed vow.

ALOE VERA: Oh, Earl Grey . . .

EARL GREY: We're just two grains of sand.

ALOE VERA: Swirling madly in the desert debris.

EARL GREY: Clinging to each other despite it all. (The wind gusts reach a crescendo, then cut.)

ALOE VERA: On the strength of our newfound fortune, Earl Grey runs for the Senate.

EARL GREY: My top issue: a national weather day.

ALOE VERA: Google, a celebrity inventor, is a huge help to the campaign.

EARL GREY: New Hampshire, (beat) a minor embarrassment.

ALOE VERA: Election night arrives and victory is ours.

EARL GREY: (Stump speech) For too long this nation has shortchanged its weather! Tonight, with one voice, you sent a resounding message, friends! It's time to recognize! Let's hear it!

BOTH: (Chanting) We like weather! We like weather!

ALOE VERA: So, we move to Washington.

EARL GREY: Where our ideas are met with stone-faced pundits.

ALOE VERA: They say the country isn't ready for a Weather Day.

EARL GREY: Buncha blowhards.

ALOE VERA: Even so, it was a happy rime, those years.

EARL GREY: Google makes us grandparents.

ALOE VERA: And, to our astonishment, New Hampshire's band, The Sweaty Pickles, begins to take off. After three terms in the Senate, Earl Grey finally gets his Weather Bill passed.

EARL GREY: How sweet it is!

ALOE VERA: I was working out on the StairMaster when he broke it to me. (Begins stepping as if working out)

EARL GREY: Darling, I've got news.

ALOE VERA: I'll never forget the weather that day, not as long as I live. The sky was sepia. Sorta. I can't really describe the color, but once or twice in our lives, the heavens have a strange, hazy light to them. Kinda dulled, like the sunshine’s weeping. Maybe I’m nuts, but it's comforting, those days, at least for me. I think it's the color of memory.

EARL GREY: It passed.

ALOE VERA: IT PASSED! (Ecstatic, they embrace and dance again to the joyous music. Cuts.)

EARL GREY: (Again, a stump speech.) Humbly, we gather today to pay homage to the world's most persistent icon. And so, without further delay, what we've all been waiting for: I hereby declare this National Weather Day!

BOTH: Hip Hip Hooray! Hip Hip Hooray!

ALOE VERA: I love you, Earl Grey.

EARL GREY: I love you, Aloe Vera. (A zap. Aloe Vera collapses like a brick.)

ALOE VERA: Ouch! What's happened?

EARL GREY: (Rushing to her aid) You've been struck by lightning!

ALOE VERA: I'm all warm and fuzzy!

EARL GREY: It came outta nowhere!

ALOE VERA: I don't feel so good.

EARL GREY: Irony -- my arch nemesis!

ALOE VERA: Live by it, die by it. Good-bye, Earl Grey. My heart's stopping.

EARL GREY: But you can't! Winters around the corner. . . who'll drink cocoa and collect snowflakes with me? No one can marvel over a snowflake like you, Aloe Vera.

ALOE VERA: You kind man. Time marches, but your keen eyes are the same as that boy's who first rescued me. You asked for a lifetime and that's precisely what we've had together. I'm glad my air balloon malfunctioned.

EARL GREY: I'm glad your face wasn't broken. (They chuckle)

ALOE VERA: When you think of all we'll leave behind . . .

EARL GREY: Not too shabby.

ALOE VERA: (Growing weaker) You'll take care of the tombstone and epitaph. . . ?

EARL GREY: I didn't think the moment would come.

ALOE VERA: But you remember?

EARL GREY: "Everything possible is happening somewhere on earth. And above it, perpetually passive and indifferent, hovers the weather."

(Earl Grey hugs his wife to him as lights fade.)
```

---

## IC-0912: Shrek - Screenplay

- Title: Shrek - Screenplay
- Author (byline): Ted Elliott, Terry Rossio, Joe Stillman and Roger S.H. Schulman
- Work: Not specified
- Publisher: Scriptfly.com
- Publication date as stated: March 2011
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTRESS, ACTOR, SHREK, TOGETHER, HEAD GUARD, DONKEY, PINOCCHIO, FARQUAAD, MIRROR, WOODEN PEOPLE, FIONA, WHISPER
- Teaser before the introduction: Yes
- Spoken words (computed): 1509
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
ACTRESS: Join us today for a fractured fairy tale about a smelly ogre with a bad disposition.

ACTOR: He sets out on a quest to rescue a beautiful princess from a fire-breathing dragon.

ACTRESS: The princess packs a punch, however, that softens his heart.

ACTOR: And through the story, we learn 3 very essential lessons

ACTRESS: 1) The importance of being our authentic selves, for true beauty is found within

ACTOR: 2) You don’t have to be what everyone expects you to be

ACTRESS: And 3) True love is often found in unexpected places and people.
```

### Performance text (classify this)

```text
(based loosely on the book by William Steig)

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles:

ACTRESS: Head Guard, Donkey, Pinocchio, Mirror, Wooden Person 1, Whisper echoing

ACTOR: Shrek, Farquaad, Wooden Person 2, Dragon, Mirror echoing offstage

SHREK: (Pg 1) Once upon a time there was a lovely princess. But she had an enchantment upon her which could only be broken by love's first kiss. She was locked away in a castle guarded by a terrible fire-breathing dragon. She waited in the dragon's keep in the highest room of the tallest tower for her true love and true love's first kiss. (laughs) Like that's ever gonna happen!

TOGETHER: Shrek

ACTOR: by Ted Elliott, Terry Rossio, Joe Stillman and Roger S.H. Schulman

ACTRESS: based loosely on the book by William Steig

Shrek is going about his day, perhaps digging up onions for dinner, or cleaning the windows of his cottage.

HEAD GUARD: (Pg 5) (with false bravado --- he’s really scared of ogres) You there. Ogre!

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

SHREK: (sighs) Okay, fine. You’re comin’ with me (Shrek and Donkey exit) *****Scene – Lord Farquaad’s Castle*****

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

DONKEY: (talking to himself) Cool. You handle the dragon. I’ll handle the stairs. I’m the stair master! (Donkey rounds a corner and . . . ) (Pg 28) Aah! DRAGON!!! (Dragon roars and flaps its wings) That’s one dazzling smile you got there. And you know what else? (flaps turn decidedly “show-girl”) You’re a girl Dragon! Just reeking of feminine beauty. (Dragon flutters her eyes) SHREK! *****Scene – Shrek arrives at Fiona’s Room***** Fiona appears to be asleep. Shrek enters, looks at her and she puckers her lips. Shrek is not entranced. He takes her by the shoulders and shakes her.

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

## IC-0913: Sibs

- Title: Sibs
- Author (byline): Diane Flacks and Richard Greenblatt
- Work: Not specified
- Publisher: Playwrights Guild of Canada
- Publication date as stated: Oct 2000
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: SHE, HE, BOTH
- Teaser before the introduction: Yes
- Spoken words (computed): 1574
- Already set (do not supply): none

### Source block (context only)

```text
Author: Diane Flacks and Richard Greenblatt
ISBN: 978-1774051825
Publisher: Playwrights Guild of Canada
Date (Month/Year): Oct 2000
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: To the outside world we all grow old. But not brothers and sisters.

ACTOR: We know each other as we always were. We know each other's hearts.

ACTRESS: We share private family jokes. We remember family feuds and secrets, family griefs and joys.

TOGETHER: We live outside the touch of time.

ACTOR: After the death of their parents these two adult siblings must put their differences aside

ACTRESS: And realize that no matter what the circumstance -- what distance lies between them -- they will always be

TOGETHER: Sibs by Diane Flacks and Richard Greenblatt
```

### Performance text (classify this)

```text
(Packing for trip to parent’s funeral, they complain out loud about the other) – Separate locations

SHE: (Pg 6-7) We always have to do things his way, I mean always!

HE: She always has to be the centre of attention.

SHE: I can tell he's always seeking my approval, because, frankly he lives his life in a way that is less interesting than he could, and then he starts judging me, and I do just fine thanks for asking!

HE: She really is a very interesting person, it's just that sometimes she can't help herself from saying the wrong thing at the wrong time and basically she just doesn't know when to shut up!

SHE: [When we were teenagers] he took up all my space in the car and then he farted and left it there! And then he scratches his *butt* and he puts his fingers in my hair!

HE: . . . she always had to have like these new jeans or she always had to have those new jeans and it didn’t even matter which new jeans she had because her *butt* was still like 8 feet wide!

SHE: I take care of everything and I don't say a word and the minute he lifts a finger, we all have to bow down.

HE: When the going gets tough, she takes off. Maybe I'm a little slow, but I've finally come to realize ... you can't change a person.

SHE: Well, you can't change.

BOTH: (simultaneously) I'm really worried about her/him.

SHE: He is not happy, and he thinks he has to follow this path that just leads to disappointment - I mean, live your life!

HE: If she keeps on going in this way she won't have anything saved for her retirement, I mean, she can't work forever, what's she gonna do?

BOTH: (simultaneously) And s/he has terrible taste in women.

(On Phone)

HE: (Pg 10 - 12) I just thought . . . that because there's a whole bunch of stuff to do, and because some of it is time sensitive, right? Some of it has to be done right now. Well, some of it is legal stuff, right? Lawyer stuff, the death certificate, getting the will probated -- that kind of stuff, right?

SHE: Right, but I don't have to just sit here in the city. Some of these things just happen --

HE: No they have to be dealt with -- somebody has to be in charge. Somebody has to make sure that they're done, right?

SHE: Right. And you don't want to do it. HE: Well -- I --

SHE: Well, let's do it long distance. HE: No uh --

SHE: You know what, I'll do it? Give me the number -- HE: Excuse me-

SHE: I'll get the number from the lawyer and I'll just handle it all long distance. You don't have to do it. I understand, you're busy.

(Scene transition and they are now little kids)

SHE: Do you want to play with *Play-Dough*? (NOTE: script uses the term “plasticine”)

HE: Yeah.

SHE: Do you know where my *Play-Dough* is? HE: Yeah.

SHE: It's in my room. In my closet! GO! Go! Go go go go go! (HE runs up the stairs to her room and gets it. They play for a few seconds) What are you making? A snake? A bone?

HE: Mommy.

SHE: I'm making mommy too. Isn't mine good? HE: Yeah.

SHE: Yours is good . . . too. (They work a bit) Hey! Can you get me a drink?

HE: Yeah.

SHE: Go! go go go go go go go go go go! (HE runs to go get it, but is gone a long while; SHE has “fixed” his Mommy; after a pause she yells) Where are you?

HE: In the kitchen! SHE: Come here with the drink!

HE: (beat) Oh yeah! (HE sees his "mommy." HE is upset)

SHE: I fixed it. Your mommy looked like a bug. (He smashes both of their sculptures)

SHE: What are you doing?!

BOTH: Mommy! Mommy!

(Scene transition – still kids – Scene opens with SHE tickling HE)

HE: (Pg 18-19) Stop it I have to pee! SHE: Don't pee!

HE: Don't do that. SHE: Pssss.

HE: Stop it! SHE: Pss psss pssss.

HE: No no stop stop. (silent beat) Oh no!! I peed! I peed!

SHE: You peed! You peed! I made you pee!! (SHE throws her arms up, victorious Her laugh becomes the laugh of a drunk teen. SHE turns and starts to walk away)

(Scene transition – teenagers)

SHE: You peed. I made you pee, mister. HE: Shh. You'll wake up Mom and Dad.

SHE: You peed. I made you pee.

HE: That's good. Now, come on, let's get you upstairs. (HE tries to help her up)

SHE: You smell like . . . potatoes.

HE: We've got to get you upstairs before Mom and Dad hear. (Pg 20) God. You're disgusting.

SHE: You're disgusting . . . (Pg 21) Spinning. HE: Are you going to barf?

SHE: No. (SHE barfs) HE: Ewwww!!

(Scene transition – still teenagers –his fantasy rehearsal of how he would ask her for advice. HE and SHE face the audience)

HE: (Pg 23-24) Can I ask you a question? SHE: I don't know, can you?

HE: There's this dance tonight, and I wanted to know, if you're slow dancing with a girl is it o.k.

SHE: Yuck! Ick! Gross! Disgusting! (HE waves away that attempt and tries another)

HE: Can I ask you a question? SHE: Sure.

HE: Say, hypothetically, I was slow dancing with a girl-

SHE: Who?! HE: Well, it doesn't matter who.

SHE: Rochelle? HE: No, not Rochelle.

SHE: Oooh, Rochelle. Rochellllle! (HE waves away that attempt and tries another)

HE: I have this friend -- SHE: Who?

HE: Uh. . . Todd. SHE: Yich.

HE: Yeah. Well, he wanted me to ask you, if he's slow dancing with a girl --

SHE: Who?! HE: Oh, I can't say. I promised.

SHE: Rochelle? HE: No! Todd doesn't like Rochelle.

SHE: No, but Rochelle likes Todd ... (HE waves away that attempt and tries another)

HE: Can I ask you a question!? SHE: Yes!

HE: Todd wanted me to ask you if he's slow dancing with a girl, is it o.k. if I kiss him!?

SHE: I think you should kiss him.

(Scene transition – still teenagers)

SHE: (Pg 25-26) Are you going to that dance tonight? HE: Yeah.

SHE: Well, what are you gonna wear? HE: What I always wear.

SHE: Oh no. You're not! HE: Why not?

SHE: Because you look like a jock. HE: I am a jock.

SHE: I know, but you smell like a jock. I mean, literally. A jock. And your shoes stink, and your socks reek, and your pants smell like skid marks and stale farts and you stink like BO, and you have this stink coming off you, it's like a stinky rank stank, skunky funky funk stinky stink stank rank skank skanky stinkudee skunk stank! (beat) I mean you really do smell-

HE: Alright! OK! (Pause. SHE looks at him) SHE: Hey, stinky,

HE: What? SHE: Can I ask you a question?

HE: (Pg 33-34) (suspiciously) Yeah . . .

SHE: Can you come here for a second? OK. Say you don't know me. And say you saw me walking on the street - could you look straight ahead please? Would you think I was cool or a loser? Straight ahead, please. (SHE walks)

HE: ... Cool.

SHE: Yeah? OK, say you don't know me, and you just saw me -- look straight ahead -- walking down the street, would you think I had a walk of self-confidence or not? Straight ahead, thank you. (SHE walks)

HE: Self ... self-confident. SHE: Yeah? I think I'm ready.

(Scene transition -- As adults after their parents’ funeral)

HE: (Pg 27) So, all I would like, if possible, is for you to stay a few more days. We can get started on it, and then you can go back home --

SHE: I need to get home now -- HE: What’s the soonest you can get back?

SHE: I don’t know HE: You don’t know???

SHE: No, I don’t know because this is all new to me. This is all new information to me

HE: Well, this is all new to me too – new information that you’re leaving

SHE: I don’t live in this city.

HE: As far as I knew you were staying until Thursday.

SHE: Where’d you get that information. HE: You.

SHE: I don’t think so. (Pg 30) (reality bubble as teens, she slaps his face) You lie you lie you lie!

(Scene transition -- As teenagers)

HE: (Pg 31-32) Yeah, right SHE: (imitating him exactly) Yeah, right

HE: Fine SHE: Fine

HE: Stop that. SHE: Stop that. (they become little kids)

HE: Stop copying me! SHE: Stop copying me!

HE: Mom, she’s copying me! SHE: Mom, she’s copying . . . (he smacks her)

(Scene transition – They gasp, back as adults after their parents’ funeral

HE: (Pg 62-65) Fine. . .Then you go home -- SHE: I need to go home!

HE: -- and I will do it *all* !!! (beat)

SHE: You've got your family and your kids --- you've got everything here, and do you know I've been here alone? Do you know that? I've been here alone this whole time. You always had your family to go home to and all these people here to talk to who know you. My whole life is in another city. I can't stay here any more. I've been completely alone! Thank you! (long pause)

HE: I think Rochelle and I are splitting up. (beat) I don't have anybody to go home and talk to. And I'm sorry that you're not at home and you don't have all of your "support systems" and that kind of stuff, but I'm under stress as well. (SHE says nothing) I just thought that we could spend some time together. (SHE gives him a sharp look) This is a chance - I mean, I don't know, you've been away, you've had your own life, you haven't kind of cared about what goes on in my life-

SHE: That's not true!

HE: Come on. Be honest. How often do we speak?

SHE: Well, how often do you call me?!

HE: Well, I tried calling you but it always felt like I was bugging you, so I backed off.

SHE: Do you know that when you call me you don't ask me a thing about my life?

HE: I ask you about work all the time

SHE: You don't ask me about my life. You don't want to know about. . . my girlfriend. I always ask you about Rochelle, and about your kids, and about what's going on with you and you never ask me! What is the point in talking with you - it's like two idiot strangers talking. se.

HE: You know every time I try and ask about you, you always, always ... don't go there.

SHE: Try me!

HE: OK. What's going on with your life? Are you and Suzanna still together, I don't even know that! I heard you were having a bit of a problem, are you together or not, what?!

SHE: Oh boy, that's really nice, it really makes me want to talk about it.

HE: There you go.

SHE: "Are you together or what?" (HE laughs) "I heard you were breaking up, are you together or not, what?" And that implies that I just - I mean you are punishing me with everything you say!

HE: But I try and tell YOU!! You never volunteer anything!

SHE: (simply) We're not friends. (pause. They are both taken aback by what SHE's said)

HE: Clearly. (pause)

SHE: (sincerely) And it's half my fault, I know . . . We're not. . . And I don't know what to do about it. (pause)

HE: Can't we be friends?

SHE: . . . I don't know. (pause They're on the verge of dissolving)

HE: They're dead. (pause) They're dead. It's just you and me. (pause. They look at each other. SHE reaches out to him)
```

---

## IC-0914: A Simple Snow

- Title: A Simple Snow
- Author (byline): Elaine Romero
- Work: 2006: THE BEST 10-MINUTE PLAYS FOR TWO ACTORS
- Publisher: Smith & Kraus
- Publication date as stated: September2007
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MAN, WOMAN
- Teaser before the introduction: No
- Spoken words (computed): 1789
- Already set (do not supply): none

### Source block (context only)

```text
Author: Elaine Romero
Book: 2006: THE BEST 10-MINUTE PLAYS FOR TWO ACTORS
ISBN: 978-1575255637
Publisher: Smith & Kraus
Date (Month/Year): September2007
```

### Introduction (context only: never use it for content warnings)

```text
MAN: Christmastime is joy put on display.

WOMAN: Once a year we try to shut out pain and focus on happiness.

MAN: But is a world without pain, really beautiful?

WOMAN: Is a life of pure joy worth losing reality?

MAN: One woman has to choose in

BOTH: “A Simple Snow” by Elaine Romero
```

### Performance text (classify this)

```text
A carriage in the snow. Man whips the horses. They hit a pothole. Woman loses her balance.

MAN: Hold on.

WOMAN: I don't know if it's your driving or not, but there seems to be a pothole every five seconds.

MAN: It's not my driving.

WOMAN: I guess I'm used to walking. Thank you. Thank you for the lift.

MAN: You didn't have any baggage? Where are you coming from? I understand. I've taken a few like you.

WOMAN: What're you saying, sir?

MAN: People coming from nowhere.

WOMAN: Well, I'd just rather not talk about it. My employer, well, he's very important. Well, I've promised to protect his identity. (They hit another pothole. The snow falls all at once.) Would you watch your driving? I swear a child is in charge of this carriage.

MAN: It's just Christmas. It shakes things up. Inside people. The holidays make people weep.

WOMAN: Not me. I'm frozen here. I would have died out there. I'm sorry for the complaints. My employer - well, you see, he died. Rather sudden. Frozen in the snow.

MAN: I'm sorry.

WOMAN: I found him last night. Myself. So, you see, I'm a little bit out of sorts. He didn't leave any provisions ... in his will. My employer. (She starts to cry.)

MAN: Doesn't sound as if he was just an employer.

WOMAN: Are you accusing me of some sort of disgrace?

MAN: No, ma'am. (The snow falls. Another pothole.)

WOMAN: This is just a shaky world we live in. Earthquakes every few minutes. People freezing in the snow. Life has been thrown asunder. See, I walked through a tunnel. It started in London or in New York City. I had said good-bye to the world. I had kissed the city good-bye, turned on my heel and put my back to it. Betrayed it like that. And then, I landed here - in the land of unsettled earth. And I met my employer. He never said much. Nothing really. Not much could move him, but then, most bosses are like that. Quiet and stern. Don't say much. And I adorned him with suits and clothes, with neckties and cigars. It seemed a paycheck might not come, but he was good to me. Never spoke a harsh word ... never spoke a word. And then I touched him and he was hard like he'd frozen in the night. Like the blood had stopped coursing through his veins - he was so important. But I left the city. Did I say? I left the dress shop. I stopped sweeping in the morning, and I was wrong. I was wrong to love whom I loved. I don't think he knew. My minister. And his wife. I loved them both. In a different way. I loved them both so much. This whole thing unnerves me. This tremor in my heart shakes my hands. I had a cranberry cake that I'd made for them and their children. I am contemptible. And I was walking through the snow on my way to them. And I tripped, or actually, fell through one of those holes in the street. (Realizing where.) In New York City. And I landed, in this strange place where men drive carriages or don't speak for days on end, or pay you for services rendered because their minds are preoccupied with other worlds. But I'm not bitter. I landed here.

MAN: Well, I've been looking for someone to love. I mean, driving in the snow every day from town to town, hitting potholes I cannot see with my hollow eyes, has left me disoriented in this shaky world.

WOMAN: Ever since I left New York. Ever since I was Alice, in the rabbit hole, I just haven't been the same. (She sneezes.)

MAN: You could join me. On this carriage. We could hold hands. Sometimes the snow catches the moonlight and the job becomes very pretty. (Woman looks off the side of the carriage.)

WOMAN: Why, that's my employer. (Woman tries to crawl off the moving carriage.)

MAN: Watch it, miss.

WOMAN: Could you stop this thing?

MAN: I'm sorry. It seems to have a mind of its own.

WOMAN: You could slow down for a lady.

MAN: I apologize, ma'am. I believe it is has stopped, ma'am. (Woman crawls down the side of the carriage.)

WOMAN: That's my employer. I'm beginning to believe, sir, that you have been taking me in a circle 'round and 'round. You have duped me into believing that I am making progress when I am making none.

MAN: No, ma'am. This here is the standstill world. That's where you landed when you left yours. (Man hits a pothole, but she shakes though she is not on the carriage. Her arms are outstretched as she strives to balance herself)

WOMAN: Get off that carriage, sir. I demand it.

MAN: It's my job. Hands on reins. Horses in place. Trees standing next to me.

Frozen body at my side.

WOMAN: Remove your hands.

MAN: Sorry, can't oblige. (She crosses to him and pounds on him, realizing he is frozen.)

WOMAN: If you weren't talking, I'd assume you were dead.

MAN: Sorry to disappoint. I've offered you my world. The seat next to me, in this, my fine carriage. (She falls to her knees. She starts trying to get up.)

WOMAN: What is this place? What is it?

MAN: I don't know. You claim to have fallen down the hole. Do you remember?

(Woman runs to the edge of the world, discovering the glass dome of the snow globe. She runs her hands up the curvature of the space.)

WOMAN: Sir, sir. It feels hard. Like glass. (Their world is shaken again. She presses her eyes against the glass.) It's flesh. Very large flesh. Could it be the hand of God is revealed to me in my sorrow? Did he discover my love for the preacher and encase me as punishment? How cruel is God to those with hearts as large as mine? (Woman lands on her bum.) Oh, no. A world that shakes. A world with endless snow. A world run as if in the hands of a child. I'm beginning to suspect I'm captive here. (She puts her eyes against the glass.) Oh, my, it's Christmas. I see the tree and the lights. The angel at the tree's tip hangs at a precarious angle and I want to catch her. I see the fire and the unwrapped gifts. I see the minister and his wife. They're eating cranberry cake and drinking Christmas wine. Why, the last time I saw him, I fell down that hole. In the city. The city of New York. Outside of Macy's, it was. The whole place was lit up for Christmas. And I could hear the carolers in the background. They sang beautifully as I lay there - dying. Sir, I believe I died. Sir, I think I know where I've landed. I've come to understand the mystery of the afterlife. See, on my way, to their apartment, I stopped at Macy's and I looked at those snowy displays. They had snowmen and Santa and my city in the winter, and they had the sweetest one I'd ever seen. A man and a car-riage. And I willed myself there to that simple life. In the snow. I wished myself there. When I died.

MAN: Would you like to join me, miss?

WOMAN: Sir, it seems you've missed my startling revelation. Sir, did you used to be real?

MAN: This is the life I've always known.

WOMAN: My employer?

MAN: He never did move though I saw you adorned him.

WOMAN: What a macabre scene for a snowy display. A dead man.

MAN: You wished yourself here.

WOMAN: I would like it, sir. But first give me a chance to watch the world I once knew as if I could live there without pain. (She does.) It's the minister. He is holding his wife. On Christmas. (She starts to cry.) I believe, sir, that I am capable of the deepest kind of love. Steadfast love. They are beautiful. Together. (She sees the son.) Oh, here he comes. (He shakes their world.) I wonder what will happen when he forgets about us, when Christmas is over and we are no longer the latest toy.

MAN: Sometimes the moonlight hits the snow and the job can be very pretty.

WOMAN: Will you talk to me forever, sir? Maybe, if you whip your horses hard enough, we could burst through the glass someday. Make ourselves known.

MAN: Maybe. (She goes back and sits beside him.)

WOMAN: I am grateful. For the company in this ordinary life.

MAN: I am, too, ma'am.

WOMAN: If you stopped ... your job, we could kiss. (She grabs his hands.)

MAN: Hands on the reins.

WOMAN: I heard about the frog prince once. The princess kissed him and it made him real. (She kisses his cheek. He releases the reins and turns')

MAN: What is this? What is this I feel?

WOMAN: Will you hold me now? (He does.) You are the most handsome man. The handsome man from the Christmas display at Macy's. The man from the snow globe.

(She puts her arms around him.)

MAN: Oh, my, what is this I feel? (He shivers.)

WOMAN: It's cold. You are in the snow. May I kiss you? (She does.)

MAN: I feel as if ...

WOMAN: As if you're alive. Come, I'll show you a whole new world. (He gets off the carriage with her. She leads him to the back of the carriage.) We will make love. Oh, don't blush. It's very nice. I will rub my body against yours.

MAN: Oh, my.

WOMAN: And when we're done. When I've shown you the most marvelous part of life, we will burst our way out of the glass. Out into the world once mine and lost.

(The world shakes. She moves to the edge of the world.) It's the little boy. He's picked us up. (They tumble.) And dropped us. (She kicks the glass.) But it didn't break.

MAN: Come here, my love, and show me the most wonderful part of life. I am eager to experience it. And when we are done, we will burst into your old world with renewed vigor.

WOMAN: Or we could stay inside and make love forever.

MAN: That is too pleasant a thought though I've never experienced it. My body screams out for your flesh. You've carnalized me!

WOMAN: We could spend our lives discovering each other's bodies. The feel of your legs and chest, the passion of your kiss.

MAN: I am most eager to get started, ma'am.

WOMAN: Alice. Like the looking glass.

MAN: Alice.

WOMAN: And what is your name?

MAN: I have none.

WOMAN: You're Clyde. Your name is Clyde. Clyde, are you ready to learn the most marvelous part of life? (She takes his hand and moves him to the back of the carriage. This time it shakes, not from the hand of the child, but because of their lovemaking.)

MAN: (Offstage.) To think I've only known the front of this carriage when the back held such earthly delights.

WOMAN: (Offstage.) I do love you, Clyde, more than that minister and his wife. Clyde. Clyde, the world holds many difficult things. Hunger and starvation when we could just stay frozen here, as if in a pause.

MAN: (Offstage.) We could.

WOMAN: (Offstage.) Or we could brave it. We could brave empty bellies, employment, disappointment, and joy. Will you? Will you bear the burden of time with me?

(They emerge from the carriage disheveled and content. She takes him to the edge of the world.) Here it is. The edge of the world. See, the Christmas lights and the trees. One. Two. Three. Kick. One, two, three ... kick. One, two, three ... kick. It's useless. The glass that encases us is too strong. (He points to the carriage.)

MAN: I would like to make love again.

WOMAN: (With humor.) You are alive.

MAN: I'd like that.

WOMAN: You are my companion.

MAN: Yes.

WOMAN: Will you help me return to the world someday?

MAN: Let's go back to the carriage, and soon they will leave. (They return) The most wonderful part of life is here for the taking.

WOMAN: But I'm hungry. And my cranberry cake looks moist and sweet.

MAN: I've seen a glimpse of your world and I think I prefer ours.

WOMAN: You're on display. You're a trinket easily forgotten or packed away in an attic.

MAN: The most wonderful part of life is here for the taking.

WOMAN: You are lovely. Perfect. What I always dreamed of. Perhaps I've died and gone to a realm beyond Earth.

MAN: Perhaps. (They kiss.)

WOMAN: I could kiss you forever.

MAN: You will.

WOMAN: No, we must burst out of this place with the force of our will. Will you come with me? Do you dare? (The world shakes. The snow falls. They both teeter. They stand looking at each other from far apart. She walks forward through the glass back into the real world. He returns to his carriage and takes his seat.)
```

---

## IC-0915: The Siren Song of Stephen Jay Gould

- Title: The Siren Song of Stephen Jay Gould
- Author (byline): Benjamin Bettenbender
- Work: The Best American Short Plays 2000-2001
- Publisher: Applause Books
- Publication date as stated: Sept 2002
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MAN, WOMAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1857
- Already set (do not supply): none

### Source block (context only)

```text
Author: Benjamin Bettenbender
Book: The Best American Short Plays 2000-2001
ISBN: 978-1557834812
Publisher: Applause Books
Date (Month/Year): Sept 2002
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Here’s a story for you . . . Two friends are watching television when the news comes on. It shows a guy on a bridge about to jump, obviously suicidal.

ACTRESS: (watching television) I'll bet you $10 he'll jump.

ACTOR: (watching television) Bet you $10 he won't.

ACTRESS: Then, the guy closes his eyes and throws himself off the bridge. (to Actor) I can't take your money. I cheated you. The same story was on the six o'clock news.

ACTOR: No. Take it. I saw the six o'clock news too. I just didn't think the guy would be stupid enough to jump again!

ACTRESS: While suicide is never funny . . . Benjamin Bettenbender takes a lighthearted look at an attempted suicide in

TOGETHER: The Siren Song of Stephen Jay Gould

MAN: Here, sit up. [tries to help her, but she shrugs him off. She removes the object she had been

holding in her injured hand and places it back in her pocket. She extends her arm out in
```

### Performance text (classify this)

```text
[The bank of a river, near a bridge. A WOMAN walks slowly along the bank, staring across the water. She stops, lost in a moment. She then reaches into her pocket, removes something, hesitates, then pulls her arm back to throw. An anguished cry is heard from above. She stops and looks up when a MAN falls on her, knocking her over. Neither moves for a moment. Then the man slowly disengages himself and stands, placing his left foot down gingerly, wincing; he then looks back to her]

MAN: Oh my God. [moves to her side, touching her lightly on the arm] Are you all right? Miss? [Shaking her] Miss, are you all right?

WOMAN: Oowwww! What did you do? [Trying to move her right arm] I think my arm is broken.

MAN: Oh God! Um ... Move your fingers. That's how you tell if your arm is broken.

WOMAN: No it's not. That's how you tell if your fingers are broken!

staring at her fingers] Try to move them.

WOMAN: I am. They're shaking and you're bleeding!

MAN: [Dabbing at his forehead] Is it bad?

WOMAN: Just a little cut. . . . Can I ask you something? I'm a little woozy so I apologize if this sounds strange, but did you jump on me?

MAN: Well, I wasn't ... I didn't exactly, no.

WOMAN: Did you fall? Were you thrown?

MAN: I leapt.

WOMAN: I see. Then when you said no, what you really meant was yes, you did jump on me.

MAN: I didn't even see you.

WOMAN: I was standing right here. Didn't you check first?

MAN: I should have. It was irresponsible of me, but I thought I was over the water.

WOMAN: The water's way over there. It's low because of the drought. You jumped on me! How dare you?!

MAN: I'm really, really sorry.

WOMAN: You could have killed me. All because you couldn't bother to look before leaping off a bridge. And what kind of dunderhead goes swimming dressed like that? In jeans. And spats.

MAN: They're not spats. They're ankle weights.

WOMAN: Oh great. Even better. Why not strap a millstone around your neck? That way you can be sure to ... [She stops, stares at him] Tell me this isn't what it looks like. You weren't jumping ...

MAN: To my death, yes. [Long pause. She then bursts out laughing] Hey!

WOMAN: Off that little bridge. [laughs harder] With those things on your feet, without even checking to ... [laughs even more] Even if you hit the water, it would barely come up to your waist. [laughs] You'd be standing stuck in the mud with those ankle thingies on, trying to pull them out. [mimes pulling a leg out of the mud] Ssssclorp! [laughs]

MAN: All right, that's enough. I mean it! This isn't something you make fun of.

WOMAN: You mean trying to drown yourself in a puddle? [Suddenly serious- mimics him] I was leaping into the mud ... to my death. [laughs]

MAN: I was trying to go head first, for your information, but the ankle weights swung me around so my feet . . . [She laughs harder than ever] That's it. I'm not talking to you.

[starts to limp off]

WOMAN: Wait, I'm sorry. You're hurt. I won't laugh anymore. [He stops, limps over to her, holds out his hand to help her up] So why were you jumping?

MAN: I told you.

WOMAN: Yeah, but why? Depressed? You don't seem it. Depression is a medical condition with a recognizable set of symptoms. I don't see any.

MAN: That's because I'm irritated right now.

WOMAN: There you go. People in a suicidal depression don't get irritated. They're apathetic.

MAN: [apathetic] Whatever.

WOMAN: That's why I thought it might be something else: an illness, bad news, a loss, fear.

MAN: No.

WOMAN: Guilt.

MAN: Over what?

WOMAN: How should I know. Maybe you got into an argument and beat someone into a coma and found out later he was a Zen Buddhist who had taken a vow of nonviolence and couldn't defend himself, and he had six kids and was working on a cure for blindness. Or maybe, maybe, it's love. Maybe you're heartbroken over a romance that ended. Or that never was.

MAN: What's so bad about that?

WOMAN: Are you kidding? That's about the best reason to drown yourself. Meeting the person you want to be with forever and then realizing it can never be. Knowing you'll grow old and die without ever again looking into the one set of eyes that brings peace to your heart.

MAN: But you just said I didn't seem depressed.

WOMAN: That's not depression. That's something far more profound. I don't think you quite understand what I'm getting at.

MAN: What's not to understand? You like someone, they don't like you back. Woe-dee-woo-dee-woo. You mope around a few days, play around with the idea of killing yourself just to show them how sorry they'll be when you're gone, then you get bored with it all, get interested in someone else, and fffffft! It's all better. [sees her staring at him] What? What is it? What?

WOMAN: I don't want to discuss this anymore.

MAN: But you brought it up.

WOMAN: That's before I realized you lacked the emotional sophistication to understand what true loss is. I should have guessed it, though, judging by your pathetic, halfhearted attempt to kill yourself.

MAN: Pathetic?! Hell! Listen, you judgmental. . . whatever, if we had gotten even half the rainfall we usually do, I'd be dead right now! Dragged to the bottom of a dark river with my lungs filled with water and you'd have been on the shore watching the whole thing, thinking how depressed and emotionally sophisticated I was to have done it!

WOMAN: But you didn't, did you? And you want to know why you didn't? Because you're too shallow. Because you never experienced pain so strong it would make eternal darkness seem like a bargain by comparison.

MAN: Oh, and you have, I suppose? Then why are you here talking about it? Why aren't you floating around in eternal darkness all happy and carefree?

WOMAN: Listen, I was close. I was this close.

MAN: What, you gave your wrist a little scratch? Took a few too many aspirin?

WOMAN: I drank poison, bucko!

MAN: You're so committed, tell me what kind of poison you drank. Maybe I'll go buy some. [pause] Well?

WOMAN: What I drank -- in the firm belief that I was, in fact, ending my life -- even though it was extremely dangerous in large doses, wasn't technically poison.

MAN: So what was it? Buttermilk? [pause]

WOMAN: Ipecac. . . I drank ipecac!

MAN: But that's the stuff that makes you-

WOMAN: I know what it is now! I know better than anyone. But before that I had been told never to touch it, and my folks kept it on the top shelf of their medicine cabinet hidden in back, so I thought it must be lethal.

MAN: I bet it felt lethal. [laughs]

WOMAN: You have no idea. [pause] Well, I'm not going to make the same mistake again. As soon as I've completed a sweet, symbolic gesture, I'm going to do it right.

MAN: What'll it be this time, death by Ex-lax? [She stares at him] What? You get to make fun of me, but I can't say the least little thing about you? [pause, then he confesses] Stephen Jay Gould -- he's this scientist up at Harvard.

WOMAN: [excitedly jumps to a conclusion] He flunked you and you had to drop out of school and it ruined your life. No wait, wait! He stole your research and published it and got famous and married your girlfriend, and you ended up broke and alone and bitter. [pause while he stares at her] Maybe you should just tell it.

MAN: He's an author. He writes about trilobites and dinosaurs, stuff like that . . . but he's really talking about how people are this big accident. How most life on earth is bacteria, and how everything else is just sort of ... not bacteria.

WOMAN: So?

MAN: Well, the way he explained it made sense. I could see that life was pretty much just a lot of microbes swimming in the dirt, and all the things we see around us and find beautiful and live for are just a fluke. I read his book and it made everything seem... pointless. Look, I'll get you a copy. See for yourself.

WOMAN: Actually, I'm surprised he was even able to write the thing in the first place. Seems like once he figured out how tiny and random he was, he would've nose-dived straight into the Charles.

MAN: Hah! Fat chance. You don't have a great job and a nice house and a wife and some kids and lots of money and a car with leather seats and a great watch and 20 pairs of pants and really cool sunglasses, and then just go and check out. No, I'll tell you when you check out. When your life is so crappy you embarrass yourself just thinking about it, but you keep at it because you figure it must be "For A Reason," and then you read some rich idiot's book telling you how you're really just some tick on the ass of an elephant, and what's left?!

WOMAN: I see. [pause] So what now? What are you going to do?

MAN: Oh. I don't know. Try something else, I guess. Or maybe wait to see if we get some rain. I kind of had my heart set on the bridge thing.

WOMAN: You might want to try a bigger bridge this time.

MAN: I guess. [pause] What about you? What are your plans?

WOMAN: I don't know. I had this thing I wanted to do, and now I'm not sure when I'll be able to do it. [removes a small box from her pocket] I was going to throw this into the river.

MAN: What is it, a ring?

WOMAN: A ring box, yes.

MAN: But not the ring?

WOMAN: I decided that it would be a sin to throw something of real value away. And since the box is technically what he presented me with, it would be fine if I just tossed that. . . But I throw with my right hand.

MAN: Oh. [pause] I could do it for you.

WOMAN: All right then. Chuck away. [He takes the box from her, hops on his good leg a couple of steps and launches it] Thank you.

MAN: Feel better? Maybe you won't have to ... you know ... If you're feeling better. [they begin walking and hobbling down the path as the conversation continues]

WOMAN: You mean killing myself? You think I change my mind that easy? Toss away one little ring box and everything I'm feeling just flies away with it?

MAN: No, I just thought-- I mean, if you wanted to -- if it wasn't too weird, because I know it's this big personal thing -- but if you wanted ...

WOMAN: [stopping; looking at him] Are you asking me to jump with you?

MAN: I mean, I know bridges aren't for everyone.

WOMAN: No, the bridge is fine. I'm just not sure when I'll be doing it. . .

MAN: You could call me and let me know.

WOMAN: [hesitates then broaches a new idea] What about seeing a show instead?

MAN: [a bit shocked, but excited] That's a great idea. And a ball game, a museum, anything you wanted! [they continue walking]

WOMAN: I don't know. I'll have to think about it. [pause] But it might be nice.
```

---

## IC-0916: Smudge

- Title: Smudge
- Author (byline): Rachel Axler
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: June 2010
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: COLBY, NICHOLAS, NICHOIAS, ACTOR, ACTRESS
- Teaser before the introduction: Yes
- Spoken words (computed): 1852
- Already set (do not supply): none

### Source block (context only)

```text
Author: Rachel Axler
ISBN: 978-0573698248
Publisher: Samuel French, Inc.
Date (Month/Year): June 2010
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Most couples look at the sonogram of their impending baby to see whether it’s a boy or a girl.

ACTRESS: But when Colby and her husband, Nick, scrutinize the picture of the life in her womb for an answer to the “what is it?” question, they are appalled to realize that they mean IT.

ACTOR: Literally.

TOGETHER: Smudge by Rachel Axler
```

### Performance text (classify this)

```text
(COLBY and NICHOLAS are in a strange, sterile hospital room. COLBY is pregnant. They stare at a small slide, motionless.) (Long pause)

COLBY: Maybe it's upside-down.

NICHOLAS: Breach? (COLBY looks at him.) I think they float around a lot, so you don't have to worry. I mean, how it's positioned right now probably doesn't matter with regard to -

COLBY: I meant the picture.

NICHOLAS: . . . Right. (NICHOLAS turns the picture around. They stare with renewed interest.) ( Pause.)

COLBY: No. Right?

NICHOLAS: Right. Yeah. No. It's all . . . grainy.

COLBY: Like a blob.

NICHOLAS: Like it's hiding.

COLBY: Awww . . . it's our first time not seeing our baby together. (They smile at each other) Well. It’s okay. I mean . . . frustrating. We could do it again. Come back in a couple of weeks.

NICHOLAS: You know. I think it is okav. We can surprised.

COLBY: Yeah. Mary if she's plain. Cassandra if she's beautiful.

NICHOLAS: Jake if she's a boy,

COLBY: She's a girl. She's definitely a girl. . . . Nick? I had another one last night.

NICHOIAS: Nightmare?

COLBY: She came out inside-out. Two-dimensional. I got papercuts. . . . Cassandra. Cassandra. Unless she's a Mary . . . Or a Jake. (Pause. They take one last look at the slide.) Maybe it's just . . . smudged.

(COLBY in a hospital gown. No longer pregnant. She talks lo the audience.)

COLBY: I think I thought it would be bigger. They hand it to Nick immediately, like they can’t wait to get rid of it. Like they think I'd hurt it. It's sort of purplish-grey. And it's skinny, so skinny, except for its head, which is immeasurably huge. The nurses won't look me in the eye. They whisper. The doctor comes in, three brisk strides. Tells us they need it back now. They wash it, dry it off. It's a quiet thing. It whispers. I count one head. Shading for a torso. A sort of nub. A sort of spike. A point, like a tail, or like a talon, near the bottom. Sort of like a jellyfish. Sort of like something that's been erased. The doctor rushes it away and puts it under a glass. This is how I see it. Under glass, covered in tubes and tape. The eye has opened. Coils of fur grow on it, in odd places. And mv husband loves it. NICHOLAS. Cassandra. Little Cassie. Cassio. One pretty babe. COLBY. The open eye is beautiful. Luminous, almost. Blue-green. It's a disturbing trick of nature, to put that one beautiful eye into that smudge. The eye is intelligent. Nicholas shows it a Barney puppet, and it blinks. NICHOLAS. There's a girl. There's a girl. Who's the prettiest of all?

COLBY: There's a feeding tube and a breathing tube and several other tubes performing mysterious, important functions. They should have handed it to me. That first moment - that instant did it. It bonded with Nick. It doesn't like me. There's jealousy in its eye as it counts my hands, finds itself lacking. It wants my fingers.

It dares me to unleash it - lift the glass and tear off the tubes, so it can fly at me and claim my fingers as its own.

NICHOLAS: Cassandra. Little Cassie. Cassie watches me with one eye closed, one all-seeing. Her Caribbean Sea-colored eye. I want to touch her, my thumb on her cheek, to smooth her skin, stretched so tightly . . .

COLBY: . . . They're letting us take it home soon. No. I didn't say it was a baby. A baby is something you hold in your arms. That you can wrap in a blanket and show your family and take pictures of and . . . And you're supposed to want to take care of it. I mean, biologically, that's why babies are cute. Because they're helpless little spit-up machines, but somehow nature tricks you into recognizing something of yourself in them. And that’s supposed to be your compensation, at least 'til they grow up and become interesting. You know? In the beginning, you don't get much, but you at least get something you can actually touch. Something that . . . responds. TRANSITION

ACTOR: Imagine being in your early 20s – blissfully expecting your first child. No signs throughout the pregnancy of any complications, any abnormalities.

ACTRESS: Now imagine meeting your severely disabled daughter for the first time, knowing that you will be taking her home soon and that your life will be forever changed . . .

ACTOR: not with the joy of a new-born baby girl, but with monitors, tubes, and a living being who isn’t quite human.

ACTRESS: How do parents cope under these circumstances?

ACTOR: Not the politically correct, fairy-tale version, but realistically? . . .

ACTRESS: At home with Nicholas, Colby and Cassandra (aka Smudge)

(NICHOLAS dangles a stuffed toy carrot over the carriage)

NICHOLAS: Okay, Cass! Do we know what time it is? (like a studio audience) "Eye exercise time!” That’s right! Left. And right. And left. And right – switch it up now! - Right. And left. And right. And – okay, wrong, Cass, but you’ll get it eventually. You will get it. Guess that’s enough eye work for today. Which means it’s tiiiiime tooooo . . catch it! Catch it! Catch it! (Colby enters. She watches Nick) Catch it!

Catch . . . . it! Catch the carrot? Catch? Catch?

COLBY: You’re tormenting it. (Nick turns quickly, caught)

NICHOLAS: Cassie likes it. It’s her favorite game.

COLBY: (with “air quotes”) Did “she” tell you that?

NICHOLAS: (“air quotes”) Don’t say “she.”

COLBY: (“air quotes”) You told me to say "she."

NICHOLAS: (NO “air quotes”) No, I told you to say she.

COLBY: That carrot is creepy. Dangling that thing over that . . . other thing. Perverse. Then again, maybe there’s some sort of kinship there. Neither one is anatomically correct.

NICHOLAS: Honestly? I’d be much more inclined to listen to your parenting tips if I ever saw you doing any parenting . . . What do you do here? When I’m at work?

COLBY: Sit. Weep. Count the hours.

NICHOLAS: Seriously

COLBY: What do you want me to tell you?

NICHOLAS: I want you to tell me what you do. Do you play games? Do you do exercises Are you even home? Who's watching our daughter?

COLBY: I’m always watching the monitor, Nick. If something goes wrong, trust me -

NICHOLAS: Not the monitor. Cassie. Are you watching Cassie? Do you interact with her? You don’t look at her. I’ve never seen you look at her. Not once since she’s come home. I don’t even think you know what she looks like.

COLBY: I know what she looks like.

NICHOLAS: No. you don't. You were so worried about my takin on extra work. But I sit at the office and I can’t concentrate, because I’m too busy worrying about whether you’re taking care of her.

COLBY: You know what - I'm not. I’m not. I’m listening to the “beep-beep-beep” that’s so ingrained in my brain right n ow – SO ingrained – I honestly think I’d keep hearing it if it stopped. And I’d just keep sitting here, listening to a phantom monitor while she died. And you know what else? That would be fine with me.

(Pause)

NICHOLAS: Okay, that's it. I am DEAD SERIOUS. Colby, You're going to pick up that carrot. And you're going to come over here and dangle that carrot over the carriage. And you are going to SMILE. And you are going to CARE. And you're going to tell your daughter a happy story about that carrot and while you tell that happy carrot story YOU ARE GOING TO LOOK AT YOUR DAUGHTER.

(Beat. Then, composed) I’ll be in the bedroom. (Nicholas exits. Colby approaches the carriage and peeks in. As she does the monitor begins frantically beeping – it’s furious, angry. Cassie backs away and the beeping returns to normal. Note – The actor playing Nicholas can provide this sound effect from “off stage”) (Colby sits in a corner, as far as possible from the carriage, which is emitting weird, angry beeps)

COLBY: I’m not listening to you. (Angry beeps) La la la la la la la (mimicking beeps) I’m not paying attention to you. (Angry beeps) . . . Okay, I guess I’m talking to you. But t hat’s it. (Particularly angry beeps) Nick’s going to find out, you know. You can’t hid your nature from a parent for long. He’ll figure it out. Oh – I think I hear him coming, right now! You going to ball “normal” for him? (the beeps subside to a gentle rhythm again) Figured. (Nicolas enters)

NICHOLAS: Okay, girls – I’m off. Have fun. Don’t do anything I wouldn’t do.

COLBY: Ha. (Colby smiles wanly) (Nicholas exits) (Angry beeps begin again) Why don’t you put on your show for Nick? Saving it for me? Should I be flattered? (angry beeping) By the way, you’re not getting that carrot back. I made you something better. No no, please – don’t get up. I’ll bring it over there, to you. (Colby takes out a crude, creepy ragdoll It’s been cobbled together from the useless arms and legs of Cassie’s onesies It’s kind of grotesque) Here it is. You like it? (She dangles it over the carriage) I call him Mister Limbs. Mister Limbs has everything you don’t. Plus? (Colby squeezes Mister Limbs) Water absorbent. Maybe I could use you to mop something up. Or maybe you’d just Smudge all over the floor (Angry beeps). The fact is – and brace yourself, Smudge, ‘cause this is reality – Nothing looks like you. Nothing in nature. Nothing is crated like you. Not purposely (Angry beeping) That’s it? That’s your response? Been there, Smudge. What else have you got? (angry beeping) You need new material. Yeah, I know you’re terrifying. But I can be pretty scary, too. Know what I’ve got, Smudge? (Colby holds up a tiny pair of scissors) I’ve got these. (beeps) And I could do it. Just one snip. Tiny triangle in the tubing. Like the first peck through the shell of an egg. SNIP. Freedom (frantic beeping). I want to scare you. I want to see horror in your little half-face. I want you to scream. I want to hear what your voice sounds like. I want to pinch you until I prove there’s blood in there. I want to poke you with a stick. (the beeps quicken until they’re one steady scream) Move. MOVE, dammit. Blink. Blink! SHOW ME YOU’RE ALIVE. (Everything stops, and Colby draws in a sharp breath, staring into the crib.) Nicholas . . . Nicholas . . .

(Colby runs to the phone. Dials) She smiled. TRANSITION

ACTOR: And a connection, however tenuous it may be is made . . . Hope is renewed . . . .

NICHOLAS: Smile! Smile for the carrot, Cass! Smile! It’s smiling at you! Your heart beats. Your brain functions, and I’m talking to you and I’m not crazy. Which means you’re alive. Living is empirical. It’s scientific. Check off a box – alive or dead? Yes or no. Zero or one. Living can’t be qualified. You’re a one. I’m sure you’re a one. (Freezes in place)

COLBY: (to the carriage) I don’t love you. I hope that’s okay. I know you’re not too fond of me either. Nick told me I’m “not open to our bond.” The thing is, you’re kind of hard to bond with. (breathes in time with the monitor)

NICHOLAS: (unfreezing) You were breathing . . . in rhythm. With the (he indicates the monitor)

COLBY: I was? (He nods) . . . . Oh. (Pause) Is that bad? (pause)

NICHOLAS: (looking into the carriage again) Cassandra rests on one swollen check. Her skin sags where it has given up. Her eye continues to watch me, always, saying, “I am yours, and you must love me.” I look back into the gree-blue sea that refuses to change, and I respond: Now reachfor the carrot. Just reach for it. Look at it. Blink at it. Please. Gow, Cassie. Stretch. Why won’t you look at me? Move! Grow! Change! Change, you little monster.

COLBY: Nick. We could try again. Couldn’t we? Try again? I want a child.

NICHOLAS: We have a child.

COLBY: Where? (Nicholas looks toward the crib. He makes a decision. He makes a cradle with his arms)

NICHOLAS: Right here.

COLBY: . . . Tell me about her.

NICHOLAS: She smells like graham crackers.

COLBY: How many arms does she have?

NICHOLAS: Two.

COLBY: How many legs?

NICHOLAS: Two

COLBY: Does she have a body?

NICHOLAS: And two eyes. A face. A perfect, tiny face.

COLBY: What’s she doing now?

NICHOLAS: She’s reaching out . . . grabbing your hand. Wrapping her stubby little fingers around your thumb.

COLBY: Veins spider-webbing through her skin. The tiniest nails you’ve ever seen. She has eyebrows. Eyelashes. Gums, but eventually teeth.

NICHOLAS: She’s saying her first word. It’s “Mamma.”

COLBY: She’s taking her first step.

NICHOLAS: She’s leaving us – waving goodbye from the school bus.

COLBY: It’s just her first day of kindergarten.

NICHOLAS: Her first day of high school.

COLBY: Her first day of college.

NICHOLAS: She rows crew.

COLBY: Varsity soccer.

NICHOLAS: MVP

COLBY: Pre-med!

NICHOLAS: She’s an artist.

COLBY: She gets engaged!

NICHOLAS: She gets married!

COLBY: She’s having a ba – (by) (Everything goes silent, the word hanging unfinished in the air). (NICHOLAS FREEZES) (Colby speaks to audience as she looks into the carriage at her baby) You know what my primary fear was, whenever I used to think about a child? I was scared that there’d be something unappealing about her. To other kids. Something weird or socially awkward, that would get her teased. Or that she’d . . . Jesus, that maybe she’d be walking to school one day and get hurt. Snatched. Something out of my control.

NICHOLAS: (unfreezes and joins Colby at the carriage) You know it’s going to be hard. You know that, right?

COLBY: I know . . . I really know. (Colby reaches into the carriage to touch her baby for the first time. Unsure of herself, like a new mother)
```

---

## IC-0917: Soap Opera

- Title: Soap Opera
- Author (byline): David Ives
- Work: Time Flies and Other Short Plays
- Publisher: Grove Press
- Publication date as stated: April 2001
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 2, LOUDSPEAKER VOICE, MAITRE D’, REPAIRMAN, MOTHER, MABEL, WASHING MACHINE
- Teaser before the introduction: Yes
- Spoken words (computed): 1659
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
TOGETHER: Soap Opera by David Ives
```

### Performance text (classify this)

```text
Suggested Roles: ACTOR 1: Loudspeaker Voice, Repairman

ACTOR 2: Maitre D’, Mother, Mabel, Washing Maching

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

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

REPAIRMAN: The sphinx in our Oedipal basement was my Mother 's Maypole. The old Ocean IT-40 It sat there like a mystical monolith. An ivory soap tower. One block of some Tower of Bay bel. Or is it Babble. Anyway, in our house the Maypole was a god. Week after week generating out of my miserable clay . . . A line of clean washing flies in over his head-white, filmy, angelic forms, including one cutout of an angel . . . the radiant angels who oversaw my childhood. I was a walking magnet for filth-here was the machine to cleanse me. We were a perfect match.

MABEL enters, a teenage girl in bobby sox and ponytail, chewing gum, sucking on a milk shake through a straw.

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

REPAIRMAN: (to audience) I was awash in confused feelings. But I sensed that this machine and I were locked in permanent press. And if it was love-it was unclean. Mom died during a soapflake blizzard and was buried on a day without blemish-a good send-off for someone who believed that man was not only dust, but dusty. I inherited the Maypole. The pure unapproachable goddess was mine. This machine and I are soulmates! Nobody understood. But who understood Romeo and Juliet, or Tristan and Isolde, or Lewis and Clark? I soon was desperate. So was Mabel.

*******

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

## IC-0918: Something Went Wrong

- Title: Something Went Wrong
- Author (byline): Matt Casarino
- Work: Open 24 Hours
- Publisher: Original Works Publishing
- Publication date as stated: 2008
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MELISSA, HARRY
- Teaser before the introduction: Yes
- Spoken words (computed): 1523
- Already set (do not supply): none

### Source block (context only)

```text
Author: Matt Casarino
Book: Open 24 Hours
ISBN: 978-1934962206
Publisher: Original Works Publishing
Date (Month/Year): 2008
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: Every marriage has conflicts.

ACTOR: You are right . . . Problems in a marriage are inevitable. But the question is whether the couple can communicate effectively enough to resolve their problems or do they instead ignore

ACTRESS: “the elephant in the room.”

ACTOR: Many married couples would rather ignore their problems, hoping that if they don’t acknowledge them the will simply disappear.

ACTRESS: . . . . They have the same empty conversations over and over, resolving nothing.

ACTOR: Resentment moves in and humor and affection leave . . .

ACTRESS: Harry and Melissa have ignored their marital problems

ACTOR: (their elephant)

ACTRESS: for far too long.

ACTOR: But Harry has a solution. He replaces their metaphorical elephant with a very real, very dead clown.

ACTRESS: (Gives Actor an incredulous and shocked look, shaking her head)

ACTOR: I didn’t say it was a GOOD solution!

TOGETHER: Something Went Wrong by Matt Casarino
```

### Performance text (classify this)

```text
The front door opens. In comes HARRY, dragging a dead clown behind him. After quite a struggle, Harry maneuvers the clown into the middle of the room and plops down on his chair, exhausted. We see that a kitchen knife is sticking out of the clown’s back.

MELISSA: (offstage) Harry, is that you?

HARRY: Yeah.

MELISSA: (offstage) I’ll bring in the silverware and plates, okay?

HARRY: Okay. Can you get me a beer?

MELISSA: (offstage) Okay. (A few beats pass. Melissa enters) I hope you wanted Budweiser, because that’s all we . . . (She sees the dead clown. She stops and stares for several beats, taking it in. Meanwhile, Harry takes the beer and opens it.) Harry? What is this?

HARRY: Hmm? (Another beat) Oh, the takeout. Sorry. I didn’t get it. Something went wrong.

MELISSA: But you did bring home a dead clown. It is dead, isn’t it?

HARRY: (With a chuckle) Oh, yeah.

MELISSA: Harry? Is there something you’d like to tell me?

HARRY: No, not really (Beat) Hey, how about I order a pizza?

.

MELISSA: Harry – Why is there a dead clown on my living room rug?

HARRY: (Big sigh) It’s been a long day, Melissa. All I want to do is read the paper and eat some pizza and watch Law and Order and go to bed. Okay?

MELISSA: No, Harry, It’s not okay. There is a dead clown with a knife in its back on my . . . hey! (She goes to the corpse and pulls the knife from its back) That’s my good kitchen knife!

HARRY: Oh, yeah. Sorry about that.

MELISSA: Oh, my god, Harry . . . what did you do? What is going on!

HARRY: Honey, nothing’s going on. I love you. You know that.

MELISSA: Harry . . . did you kill this clown? Did you?

HARRY: Honey . . . (another big sigh) . . . Okay, I’ll tell you all about it. I left work and s topped at Freddie’s for some takeout. But when I came home, I didn’t have the takeout. Instead, I had a dead clown. So I dragged him in here and sat down. That’s what happened.

MELISSA: But something happened in between the time you went to Freddie’s and the time you brought the dead clown home.

HARRY: Honey, look. There is nothing I could possibly say that could even come close to justifying why I brought home this dead clown. You’re just setting yourself up for a big letdown. Let’s just say that something went wrong. What’s done is done. You know, someday we’ll look back on this and laugh.

MELISSA: I don’t care about someday. I care about today. Right now. Where it’s just you and me and . . . (she motions to the clown)!

HARRY: All right, Melissa. I get it. I see what’s going on here. You’re still made about last Thursday.

MELISSA: What!?

HARRY: Honey, I told you. The boss handed me that report to finish. I would have called, but the phones were on the fritz, so I . . .

MELISSA: I don’t care about last Thursday night, Harry!

HARRY: Oh, Melissa. I’ve been married to you for eight years. I can read you like a book. You’re still mad.

MELISSA: Of course I’m mad! You . . . you brought . . .

HARRY: I know, honey, and I admit that this (indicates the clown) is a problem. But nothing is stronger than the foundation of our love! One dead clown can’t ruin that. Besides, I thought you didn’t like clowns.

MELISSA: I like clowns!

HARRY: Really? I never did. They always scared me. It’s like, this is supposed to make me laugh? A middle-aged fat guy in white makeup with a distorted red nose? Come on!

MELISSA: Clowns are supposed to be happy. They’re supposed to be silly and carefree and bring joy to the hearts of children. They’re not supposed to be lying dead in my living room, still bleeding from a wound caused by my kitchen knife! Can you even begin to understand how this makes me feel?

HARRY: Of course I understand. But I don’t think you’re making an effort to understand me. Look at yourself! You’re exhibiting very hostile body language, Melissa. I don’t think anything I say is going to get through right now.

MELISSA: Harry!! What is going on!!

HARRY: Honey, look. We could get into a big discussion over this, and hash out who did what, and why, and to whom, and oh my god, what about the cops, et cetera, et cetera. Instead, how about this idea. You tell me what you want on your pizza. We’ll stash the clown body in the closet, then I’ll call Testa’s and order the pizza. We’ll relax, eat dinner, drink some wine, and when we’re done, we’ll cut this poor bastard up and buy him in the woods in a shallow grave and put this whole dead clown business behind us once and for all. What do you say?

MELISSA: (Beat) Who are you?

HARRY: I’m me, Melissa. I’m the same man you’ve been in love with all these years. I’m just going through a tough time right now.

MELISSA: A tough time? My god, Harry, you . . . okay. Whatever happened, you can tell me. Okay? I’m . . . I’m your wife. I’m here to support you. So please, tell me what happened, and we can sit down, and decide what to do. Together. Okay? Now please tell me what happened.

HARRY: Okay. I’ll tell you. Now remember how much I love you. I’d do anything for you. Keep that in mind for me okay? . . . (Big sigh) There was no report to finish. I was with someone.

MELISSA: What?

HARRY: Last Thursday night. I’m so sorry, honey. I was in a bad place. I was feeling very vulnerable. I want you to know I take full responsibility for my actions. I don’t blame you one bit.

MELISSA: What are you . . . blame me for what?

HARRY: Blame you for not . . . well, honey, you haven’t been entirely . . . intimate with me for a while. But in all fairness, I suppose I’ve been distant lately, and . . .

MELISSA: Distant? Is that what you call it? When our entire conversation anymore revolves around dinner and which rerun we’re going to watch?

HARRY: Hey, now that’s not fair. It takes two to have a conversation, you know.

MELISSA: And what does that mean? That this is somehow my fault?

HARRY: No, no. I told you, I take all the blame. Besides, it’s not like I had actual intercourse with her. I couldn’t go through with it. I love you, Melissa. I could never be . . . intimate with another woman.

MELISSA: Harry, that doesn’t . . . (beat) . . . wait a minute! We are not talking about your stupid little affair! We are talking about this dead clown! Now you tell me what happened, or I swear to god, Harry, soon there will be two clowns on my living room rug.

HARRY: I already told you. Something went wrong . . . We’re talking about the clown.

MELISSA: YES!!!

HARRY: Or are we talking about us? What happened to us, Melissa? We used to have so much fun together, you and me. We would spend hours just laughing. What happened, honey? What happened to the laughter? (Harry and Melissa both look at the clown) Well. I’m sorry, honey. I really am. It’s not you. It’s me, it’s all me. I’ve changed. I used to have such ambitions, such ideals. And now look at me. I’m out of shape. I’m a corporate drone. I’m . . .

MELISSA: You’re a guy who brings home dead clowns.

HARRY: One dead clown. . . It’s not over for us, Melissa. Someday you’ll learn to trust me again, and we’ll be all the more stronger for it. I told you I couldn’t go through with it, honey. The flesh was willing but the heart – ah, the heart was . . .

MELISSA: Harry . . . Listen to me. Okay? Listen carefully. I don’t care. I don’t care about your stupid little non-affair.

HARRY: Do you really mean that?

MELISSA: Yes. I really mean it.

HARRY: Then there is hope for us! I knew it, honey. I knew we were strong enough to get past this and move forward! Let this day be the day of our rebirth! Look out, world . . . here comes Harry and Melissa, and nothing can stop them!

MELISSA: I don’t think so, Harry. (She raises the knife and starts to advance on him) See, I can get past last Thursday night. Your pathetic affairs mean nothing to me Harry. I can get past that. Just as I can get past the fact that you need to buy a new case of Bud every four days. I can even get past that collection of porn that you keep under the floorboard. Oh, yeah. I know about that. Just like I know that you steal salt shakes from fast food restaurants. You see, these are things that happen in a marriage. These are the day to day issues that one must face and deal with and rise above. And I can deal with those issues, Harry. I have risen above. In fact, there’s only one thing I’m still struggling with. One issue I just can’t seem to get past. Do you know what it is?

HARRY: My back hair?

MELISSA: The dead clown on my living room rug!! Now I’m going to ask you one more time before I stab you in your bald spot. Tell me, for the love of God, why is there a dead clown on my living room rug? (By now she’s standing over him, knife ready to strike.)

HARRY: (Feeling threatened) Honey, look, sometimes things happen and. . . .

(Melissa raises the knife and Harry cowers further) Darling, now this in not a constructive . . . (Melissa jerks the knife up and is ready to strike; Harry tries one last ditch effort) Don’t you think there are some things that we just shouldn’t talk about?

(Melissa stops. A few beats pass as she takes this in. She jerks the knife up again and is prepared to strike Harry . . . but she stops short. Finally, she lowers the knife, slumps her shoulders, and looks at Harry.)

MELISSA: Maybe you’re right. . . Yeah. Maybe some things just shouldn’t be talked about.

HARRY: That’s my girl. Hey, come here.

MELISSA: (With a sigh that registers a touch of defeat) Okay. (Melissa tosses the knife into the back of the clown corpse. She sits next to Harry, who takes her in his arms.) You’re buying me a new knife.

HARRY: Of course I will. Hey, I’ll order that pizza now. Pepperoni and mushroom okay? . . . we’re going to be all right, honey. You’ll see. (Beat) Oh, and honey? . . . Can you do me one favor?

MELISSA: What?

HARRY: Don’t look in the trunk, okay?

(On her reaction . . . lights down, end of scene)
```

---

## IC-0919: Stay, Carl, Stay

- Title: Stay, Carl, Stay
- Author (byline): Peter Tolan
- Work: Stay Carl Stay, Best Half Foot Forward and Pillow Talk: Three One-Act Plays Pgs 5-41
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Jan 1998
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: CAROLINE, BRIAN, MARY SUE, CARL, DR. WEISS
- Teaser before the introduction: Yes
- Spoken words (computed): 1546
- Already set (do not supply): none

### Source block (context only)

```text
Author: Peter Tolan
Book: Stay Carl Stay, Best Half Foot Forward and Pillow Talk: Three One-Act Plays
Pgs 5-41
ISBN: 978-0822210771
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Ladies . . . Would you rather have A Dog or a Boyfriend?

ACTRESS: Before you decide, let’s consider 5 important factors in any relationship:

ACTOR: Jealousy, Friends, Expectations and Love.

ACTRESS (as Boyfriend): You’re late. Where have you been? Who were you with?

ACTOR (as Dog): I’m so glad you’re home! I have no idea how long you’ve been gone. Let’s play!

ACTRESS (as Boyfriend): No, I don’t want to spend the day with your friends. I don’t like them.

ACTOR (as Dog): Whoohoo! More people to play with!

ACTRESS (as Boyfriend): I don’t know what you want from me.

ACTOR (as Dog): Sit. Shake, Stay. Got it! What’s next?

ACTRESS (as Boyfriend): You are so needy. Just assume I love you unless I tell you otherwise.

ACTOR (as Dog): I love you! I love you! I love you! Rub my tummy!

ACTRESS: Hmmmm . . . That’s some decision!

TOGETHER: Stay, Carl, Stay by Peter Tolan.
```

### Performance text (classify this)

```text
Suggested Roles: Actress – Caroline Actor – Brian, Mary Sue, Dr. Weiss, Carl and Narrator

NOTE: This cutting asks one student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

NOTE FROM THE AUTHOR (summarized): (Pg 9) The character of Carl should not move around on all fours. He should exhibit real dog characteristics not cartoonish – scratching, sniffing and other canine behavior should be used judiciously. Too much of it will tip the balance to cartoon. No bad dogs.

NOTE: Transitions by the Narrator are not found in the original script. The actor should step outside the scene to narrate these transitions.

Living/Dining Room of Caroline’s apartment. She is at the table with a plate in front of her. Across the room, Brian concentrates on a newspaper.

CAROLINE: (Pg 11-12) Honey? Are you sure you don't want some pasta? I put in those little shrimps you like . . .

BRIAN: I'm not eating dinner because I get home late, I eat late, and then I have a wad of food sitting in my stomach like a lead balloon. I don't think that's smart healthwise. Or sleepwise. (Beat)

CAROLINE: Do you want to sit with me? You don't have to eat, but could you sit with me while I do?

BRIAN: (Exasperated) Honey, come on . . . I'm going to watch you eat?

CAROLINE: You used to love eating dinner together, remember? (long beat) Brian?. . . Do you still love me?

BRIAN: Don’t be silly. And now we’ll be quiet. (Brian goes back to his paper)

CAROLINE: (Pg 13-14) I'm not saying Brian hasn't been good for me . . .

MARY SUE: He has been good for you. He's brought you out more. The first time we met, you were so shy. Let's be honest. When you met Brian, you were a spineless mess. But now you're a super terrific person . . .

CAROLINE: With a spine. It's like he filled a need, but the need isn't there anymore. . You know what's funny? I used to think Brian was the perfect man.

MARY SUE: (Pg 15) Look, Caroline, sweetheart, you need a professional -- Dr. Weiss. The woman has done wonders for me. Remember all that stuff I was going through with Jeffrey? She gave me some great advice. I needed love, companionship . . . someone I could relate to and connect with. She told me to get a dog.

TRANSITION by NARRATOR: [So that’s just what Caroline did . . . she went to the local animal shelter and found a big, beautiful, muscular dog . . . she named him Carl]

Caroline sits at the table with her dinner again. Brian is pulling on a pair of sweatpants. He carries socks and sneakers and sits on the couch to put them on. Carl sits on the floor staring at Brian.

CAROLINE: (Pg 19-20) Are you mad at me? . . . About the dog.

BRIAN: I don't care. Just as long as he doesn't get into my stuff. (To Carl) Stop staring at me. (To Caroline) Tell Cujo to stop staring at me.

CAROLINE: Are you going out?

BRIAN: We're playing basketball.

CAROLINE: On a Tuesday night? You usually play Friday nights.

BRIAN: Well . . . now we're playing two nights a week.

CAROLINE: Thanks for telling me. It's not just this one thing. You don't talk to me anymore.

BRIAN: (breezily, insincere) I'm sorry. I guess I don't have anything to say. Caroline, you know me. I'm not the kind of guy who indulges in a lot of small talk.

CAROLINE: I'm not talking about small talk. I'm talking about necessary talk. What's happening in your life. What you're feeling.

BRIAN: (with an edge) I think I liked you better when you were too terrified to open your mouth.

CAROLINE: (Stung) God . . . that's mean. Will you stay home tonight so we can talk?

BRIAN: Honey . . . Look. We're both upset. Let's have some time away from each other . . . and then we'll talk when we've both calmed down. Don't wait up. Keep him out of my stuff. (Brian exits, long sad beat)

CAROLINE: (their relationship is loving and special) Hi, Carl. Who's my baby? Who's my baby? Sit. Sit, Carl. You are sitting. Good boy. Want some little shrimp? Does baby want some little shrimp? (Caroline tosses some shrimp to Carl.) Good boy. That's a good boy. ******** Caroline and Carl are playing on the floor. Brian is draped on the couch again reading the paper.

CAROLINE: (Pg 23-25) Sit, Carl. Sit. (Carl sits down, crossing his legs Indian-style.) Good baby. Lie down. Down. Down, Carl. (Carl reclines, propping his head up with one hand.) Good baby!

BRIAN: Hey. Don't call the dog 'baby.' It's weird.

CAROLINE: Jealous?

BRIAN: (heavy sigh) Okay.This is so obvious. You think I've been ignoring you, so you ignore me and spend all your time with the dog. You’ve made your point. I'll try to talk to you more. Okay?

CAROLINE: Can we discuss some of the problems we're having?

BRIAN: I don't see any problems. You're the one who keeps talking about problems. You know, sometimes I think you make this stuff up so you can have something to bitch about.

CAROLINE: Is that right? I just want to talk.

BRIAN: You want to fight. You want me to say something I'll regret later.

CAROLINE: I want you to say anything you feel like saying. A little communication is all I'm asking for.

BRIAN: You want a little communication? Talk to your dog. Goodnight. (Brian stalks into the other room.)

CAROLINE: (To Carl.) Good boy. (Pointing to the other room.) Bad boy. Good boy, Carl. Speak, Carl. Speak. Woof. Woof. Woof.

CARL: Woof.

CAROLINE: My ... CARL: Moof.

CAROLINE: My ... CARL: My ...

CAROLINE: Name ... CARL: Woof.

CAROLINE: No. Name ... CARL: Name

CAROLINE: Is ... CARL: Is ...

CAROLINE: Carl. CARL: Carl.

CAROLINE: My name is Carl. CARL: My name is Carl.

CAROLINE: Good boy! CARL: Thank you.

*********** Caroline and Carl are snuggling on the couch. Brian enters.

BRIAN: (Pg 27) It smells like dog in here. Our apartment smells like a kennel. (Exits)

CARL: (Pg 26-28) (Caroline and Carl look at each other) I’m crazy about you; [but] I can't live like this. . . The petty tirades. The accusations spoken and unspoken.

CAROLINE: I know.

CARL: I don't want this to turn into a situation of it's him or it's me. I wouldn't ask you to make that decision. I wouldn't be so presumptuous.

CAROLINE: Presumptuous? Where'd you get that?

CARL: Last night on the "The MacNeil Lehrer Report."

CAROLINE: I'm so impressed. You're such a good boy.

CARL: You're my snuggle-bunny. (He rubs his head on her arm, then gets back to his conversation.) Now, as I was saying ...

CAROLINE: You want me to ask him to leave? It's something I've been thinking about, yes ... but to actually confront him. I don't think I can do it.

(Brian enters, spraying disinfectant around the room.)

BRIAN: I'm sick of that stinking animal, I'm sick of his hair all over the place. And I'm sick of my girlfriend spending every minute of her free time with a dumb animal. This is it, Caroline. It's me or it's him.

CAROLINE: You think you can put me in that position? Brian, you are so ...

CARL: (Under his breath.) Presumptuous.

CAROLINE: Presumptuous. You don't want to ask me to make that choice.

BRIAN: You bet your ass I do.

CAROLINE: (Pointing to Carl) I choose him.

BRIAN: Yeah. Right. Read my lips. Get rid of the mutt.

CAROLINE: I'm serious. The dog stays . . . and you . . . go.

BRIAN: (Turning to exit.) You're serious. (Stricken and overly dramatic) After everything I've done for you?! You used to be afraid of your own shadow. You wouldn't give an opinion, you wouldn't make a comment . . . because you were afraid of sounding stupid. I nurtured you. I made you feel good about yourself ...

CARL: (dryly) I’d like to thank the academy . . .

BRIAN: I knew this day would come. (He exits.)

TRANSITION by NARRATOR: [So . . . Caroline finally found the strength to stand up to Brian and throw him out. Life with Carl was perfect in every way. He doted on her every word, he listened, really listened. He was responsive, obedient, loving. He was the perfect companion . . . until one day]

CAROLINE: (Pg 33-34) Well?

CARL: What?

CAROLINE: Don't play dumb with me, Carl. You know what. That scene in the park with Mary Sue? You kissed her!

CARL: I licked her face.

CAROLINE: Big difference! You don't have to make out with her in front of me!

CARL: Boy, are you paranoid.

CAROLINE: Oh, please. Don't start throwing around terms you know nothing about. If you don't have anything constructive to say, keep your mouth shut.

CARL: Oh! It's the ghost of Brian past.

CAROLINE: What? That does it. Let me remind you of something, mister. I'm number one in this house and don't you forget it. I'm number one, you're number two.

CARL: You're number one because that's the way I like it, missy. I'm letting you be number one because you're getting your kicks. If I really wanted to, I could have you under the coffee table in the fetal position like that! (Carl sits on the couch and opens a magazine to read)

CAROLINE: Hey! Get down. Get down off that couch this instant! You're not allowed up on the couch and you know it. Get down!

CARL: Do you mind? I'm trying to read something . . .

CAROLINE: Get off the couch! (grabs the magazine from him and goes to hit him with it. There is a brief struggle that ends when Carl takes a nip at her. Dropping the magazine, she massages her injured hand in pain) Ow! You bit me.

CARL: I didn't bite you. I nipped. You were hitting me. I'm sorry, Caroline. I'm sorry.

TRANSITION by NARRATOR: [Well, Caroline realized that the relationship needed some help. After all, it HAD spiraled quickly into a domestic violence situation, so she called the only therapist she knew . . . Dr. Weiss]

DR. WEISS: (Pg 35-36) All right. Why don't you begin, Caroline?

CAROLINE: I don't feel like we're connecting. There was a time when I was everything to him. I remember you used to sit at the dinner table and watch me eat.

DR. WEISS: So what went wrong?

CAROLINE: He bit me.

CARL: It was a nip. She hit me with a magazine.

CAROLINE: He was up on the couch.

CARL: She makes all the rules. . . I'm not saying that Caroline hasn't been wonderful for me. But what she has to give me, I don't think I need anymore.

CAROLINE: What do you need, Carl?

CARL: Freedom. Room to run. I need to be responsible for my own life. With you I'm always going to be the dog in the relationship.

CAROLINE: That's funny. You are a dog!

CARL: And you never let me forget that. (Beat) I have to leave. I've taken a job at a kennel in Pennsylvania.

CAROLINE: Carl . . . you can't.

CARL: (Pg 37) Yes, I can. And I did. (Breaking) Caroline, I'll never forget you. [But] I think this is for the best ... for both of us. Goodbye. (Carl exits. Caroline runs to the door after him)

CAROLINE: Carll No! Stay, Carll Stay! (He is gone) What now? What do I do now? I've been dumped by my dog.
```

---

## IC-0920: Stye of the Eye

- Title: Stye of the Eye
- Author (byline): Christopher Durang
- Work: Durang, Durang
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: May 1997
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: CHARACTERS, JAKE, MA, DR. MARTINA, AGNES, MTV.
- Teaser before the introduction: Yes
- Spoken words (computed): 2325
- Already set (do not supply): none

### Source block (context only)

```text
Author: Christopher Durang
Book: Durang, Durang
ISBN: 0822214601
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): May 1997
```

### Introduction (context only: never use it for content warnings)

```text
Christopher Durang's "A Stye of the Eye" is theatrical caricature at its best. Those of you familiar with Sam Shepard (all five of you) will appreciate the blatant references to beat-you-over-the-head-with-it symbols, mostly notably from his play A Lie of the Mind. For those of you unfamiliar with Shepard's depictions of the lonesome prairie, untamed masculinity, and incest, the low humor of white trash will keep you entertained for the full twenty-three minutes and nine seconds. With some parody of David Mamet and whoever wrote Agnes of God in there to boot, "A Stye of the Eye" massacres pretentious plays, family values, and a baby lamb. Enjoy.
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

CHARACTERS: Jake / Dr. Martina Dysart, a psychiatrist Ma, Jake's mother / Beth, Jake's wife

JAKE: Answer the phone damn it. Answer the phone. [Bangs the phone receiver on the side of the phone, or any other surface.] Come on, come on! [Into receiver.] Hello! Hello!

[Lights up on a different part of the stage. MA is discovered next to a phone, or enters calmly over to the ringing phone. MA is between forty and fifty, and dressed in a sloppy, comfortable print dress. Her hair is not fussed with, just pulled back out of her face. She is a no-nonsense woman, tough, matter-ot-fact, sounds like a Cracker.]

MA: Hello?

JAKE: Hey, Ma?

MA: Who is this?

JAKE: Ma, it's your son.

MA: Who?

JAKE: Your son, ma.

MA: I got two sons. Which one are you?

JAKE: I'm Jake.

MA: Jake?

JAKE: Jake!

MA: You're not the other one? What's his name?

JAKE: Frankie. No, it's not Frankie, Ma. It'sJake.

MA: Jake?

JAKE: Stop saying Jake, or I'm going to come over to your house and punch you in the mouth.

MA: [Her voice warming, friendly.] Oh, now it sounds like Jake. How ar eyou, baby?

JAKE: She's real bad, Ma.

MA: Who, Jake?

JAKE: She's all red and blue and purple.

MA: Who you talkin' about, Jake?

JAKE: I had to hit her. She was dressin' real sexy like, and goin' off to rehearsal.

MA: Who is this you're talkin' about, Jake?

JAKE: It's Beth, Ma. My wife.

MA: Are you married, Jake?

JAKE: Ma, you know I am. You wuz at the wedding.

MA: Why didn't you marry your sister, Jake, she always liked you.

JAKE: That would be incest, Ma.

MA: No, it wouldn't. Incest would be if you married me. If you married your sister, it would be ... sorority.

JAKE: Shut up, Ma. I'm tryin' to tell you I killed Beth.

MA: Who's Beth?

[Note: MA’s lapses in memory are complete. When she says something like "Who~ Beth," she has no recollection whatsoever that she heard the name Beth a few seconds before. So all her questions are asked innocently, trying her best to get information. There is no "what was that thing you said a moment ago" tone to any of her repeating questions. And thus when JAKE seems irritated with her forgetting, she has no idea what is the cause of his frustration. ]

JAKE: She's my wife.

MA: I didn't know you were married.

JAKE: You have the attention span of a gnat. Ma, we've been through this. Beth is my wife, you wuz at the wedding, and I just killed her.

MA: [Suspicious.] Who is this calling me?

JAKE: It's your son, Ma! I just killed my wife.

MA: Well, I never pay attention to the tramps you start up with. She probably asked for it.

JAKE: She was goin' to rehearsal, Ma. She's into actin', Ma, and she's goes off to fuckin' rehearsal, and every day she dresses more slutty like, and I just know that she's doin' it with some fuckin' actor on her lunch break. And I seen her in a play once. She stank. .

MA: [Upset.] Whatcha goin' to plays for, baby? I didn't bring you up to spend your time goin' to plays. You're gonna end up like that Sam Shepard boy down the road. Why don't you settle down and marry your sister?

JAKE: Stop talkin' about incest, Ma. I just killed my wife.

MA: Well, did anyone see you?

JAKE: No.

MA: Well, there, you see. Go get a good night's sleep, and in the morn-ing we'll get you another one. Why don't you marry your sis ... Oh, that's right, you don't like that idea. You're stubborn like your father.

JAKE: I didn't want to kill her, Ma, but she asked for it.

MA: Who you talkin' about, baby?

JAKE: Beth, Beth! How many times do I have to say it!

MA: Thirty-three. I'm getting bored with this conversation, Jake. Is your good brother Frankie there?

JAKE: What?

MA: Put Frankie on.

MA: Frankie, is that you?

JAKE: Wait a minute, Ma.

MA: Did you hear what Jake told me?

JAKE: Hold your horses a minute, Ma. Hey, Frankie! Ma wants to speak to you! Frankie! [Changes personalities, and witches phone hands; sounds more polite and reasoned though still has a temper.] Hey, Mom, how are you?

MA: Oh, Frankie, I love it the way you call me "Mom" and Jake calls me "Ma." It's so differentiating. Frankie, did you hear that Jake killed his wife?

JAKE: He told me, Mom. He's a crazy, spoiled, mixed up kid. Mom, what are we gonna do about Jake?

MA: Who?

JAKE: Jake.

MA: Jake's dead. His wife just killed him.

JAKE: You got it backwards, Ma. I mean "Mom."

MA: You know you and Jake sound so much alike that sometimes I think you're both two different aspects of the same personality. That means I gave birth to a symbol, and me with no college edjacation.

JAKE: I'm not a symbol, Ma. I'm a westerner looking for the big open expanses, but they're gettin' smaller and smaller. There's no place to hope, Ma.

MA: You sound like a symbol. But not some prissy Ivy League-type symbol. My children are virile, masculine symbols who carry guns and beat up women. You all got so much testosterone in you, that you got a native kinda poetry in you, even when you spit. Why don't you go kill a woman like your brother?

JAKE: But what woman is like my brother?

MA: That's not what I meant, stupid. The verb was implied in that sentence, as in "Why don't you go kill a woman like your brother did, " "did" in imaginary bracket signs. And me with no college edjacation. Put Jake back on the line, honey, I'm bored with this conversation. No, never mind, I got an idea. Why don't you go try to find Beth. Maybe she's not dead. Maybe she's only brain damaged, and you can marry her. That might have symbolic value of some sort.

JAKE: But what symbolic value would that have, Ma?

MA: I don't know, I'm not a writer. But if we put some jazz music under it, or some good country sounds, it's bound to mean somethin' to somebody. I gotta go now, Frankie, the cactus is whistHn' on the stove. But you keep an eye on your brother, and if you wanna marry your sister, just let me know. [Hangs up, exits; lights fade on her part of the stage.]

JAKE: Goodbye, Mom. [Switches to JAKE personality; grabs for phone from himself] Hey, I ain't done talkin' to her yet! [Switches back to Frankie, hangs up the phone.] Well, she's done talkin' to you. Why'd you go and kill her, Jake? [Switches to JAKE.] Ma? [Switches to Frankie, annoyed.] No, not Mom. Beth. [Switches to JAKE.] I don't know. She just kept goin' to all them rehearsals and ... well, it irritated me. [Switches to Frankie.] I can understand that. [Switches to JAKE; vehement.] Especially this one play called "Agnes is Odd" or some such thing, all about this flakey nun who killed her baby.

[Lights change. We see the play JAKE is remembering. JAKE plays the role of Dr. Martina Dysart] The sound of Stravinsky-like music, or Carmina Burana. Startling, mysterious, otherworldly.

Enter DR. MARTINA DYSART, in a crisp business suit, smoking three cigarettes, one in her mouth, two in her hands. She takes the one in her mouth out, and addresses the audience. She is intense and concerned, solving a deep mystery.]

DR. MARTINA: The baby was-discovered in a waste basket with the umbilical cord knotted around its neck. The mother was unconscious, next to the body. The mother was a young nun called Sister Agnes, Sister Agnes Dei. During the night she had given birth and then seemingly killed her baby. Then she went out to the convent stables and blinded eight horses with a metal crucifix. That much is fact. But she is also a musical genius along the lines of Wolfgang Amadeus Mozart. Furthermore, my life as a psychiatrist is drab and depressing, and even though I think it unappealing that she killed her baby and blinded the horses, still I envy her passion. You wouldn't see me getting up in the middle of the night to go down to the stables. And furthermore, I'm a lapsed Catholic who wishes I had her faith, and I wish I had a horse, and I ... wish I was a composer. In short, there are many ideas and subtleties to think about here, so stop rattling your programs and let's move on with it. My first meeting with Agnes, I thought she was brain damaged. [Enter SISTER AGNES, the sensitive nun. Dressed perhaps in the strange white nun ~ outfit Amanda Plummer wore in the Broadway version of ''Agnes of God, "which is the same design Sally Field wore in "The Flying Nun" tv series. Or a more conventional nun outfit is okay too.

JAKE’s wife BETH is playing SISTER AGNES. Actress formerly playing “MA” plays the role of BETH”

AGNES: Look, stigmata. [AGNES holds out her palms, which at first glance have gaping red holes in them. A second later one notices that she seems to be holding red rubber things in her palms, with reddish centers to them.]

DR. MARTINA: Nonsense, those are plastic Dr. Spock ears. Look, I'll show you. [D R. MARTINA removes the ''plastic stigmata" and puts the Dr. Spock ears on her ears. She leaves them there for the rest of the scene.] People sell these at Halloween. Do you like Halloween, Agnes?

AGNES: Pooh. Pooh.

DR. MARTINA: Pooh. Winnie the Pooh? Do you like Winnie the Pooh?

AGNES: Pooh. Pooh. Puer. [Last word is pronounced "Pooh-air. '1

DR. MARTINA: Puer. That's Latin for boy. Do you like boys, Agnes?

AGNES: Pooh-ella.

DR. MARTINA: Yes, puella. Latin for girl. Maybe it's Latin you like. Do you like Latin, Agnes? Hie, haec, hoc, and all that.

AGNES: Puer. Puella. Eck, eck, equus! [Momentarily mimes blinding horses, then pulls herself together again.]

DR. MARTINA: Boy, girl, horse. This isn't a very intelligent conversation, Agnes. Don't they make you speak sentences in the convent, Agnes?

AGNES: Agnes Dei.

DR. MARTINA: Yes, that's Latin for Lamb of God. [With a shock of recognition.] Oh my God, your name is Agnes Dei, isn't it? Good grief, I wonder if that means you're some sort of sacrificial lamb to God, and that maybe your giving birth was an immaculate conception, and that the father is God Himselfl!! Good Lord, what a shocking idea, oh my mind is running, let me try to breath deeply for a moment. [Puffs on several of her cigarettes.] Goodness, what dreadful rubbish I was just speaking. Rather like speaking in tongues. Do you like tongues, Agnes?

AGNES: We had tongue sandwiches at that convent, and it made all the Sisters menstruate.

DR. MARTINA: [Pause.] I think. that's rather an obscene remark you've just made, Agnes. Did you mean to be obscene?

AGNES: Children should be obscene. And not furred.

DR. MARTINA: Furred?

AGNES: Furred like a bird.

DR. MARTINA: What is the matter with you exactly? Are you a saint or are you brain damaged?

AGNES: [Sings, lasciviously.]Erotic, erotic, Put your hands all over my body!

DR. MARTINA: I see. Well, if you're going to sing, I think I'll go now. By the way, which member of the convent is it who won't let you watch MTV? [Shudders to herself] What a sharp remark of mine. I'm definitely in the right profession.

AGNES: No do with MTV.:

DR. MARTINA: Of course, it do. Does. That's the kind of song that's sung on

MTV.:

AGNES: Noooooooo. Who sing, Doctor?

DR. MARTINA: I forget. That slutty woman who changes her look all the time, whats-her-name ... oh my God, her name is Madonna, which means "Mother of God!" [AGNES has a screaming fit at this scary coincidence, and falls to the ground rolling around in circles, going "Whoop! Whoop! Whooop!'1

AGNES: Whoop! Whoop! VVhoop! Whoop! Whoop!

[Lights back up on JAKE.]

JAKE: [As JAKE; explaining to Frankie.] It was after that terrible play that I took Beth out in the parking lot and I beat her to a pulp. "Your play was pretentious!" I said, and then I punched her. "You were unconvincing as a nun, and I didn't know whether you were supposed to be crazy or sane," and then I kicked her in the side. "And I don't like the previous play you wuz in, "The Reluctant Debutante," either, and then I took her head and I put it under the tire of the Chevrolet, and I dropped it on her. And that's how I killed her. [Switches to Frankie.] Oh, Jake. The play couldn't have been that bad. [Switches to JAKE.] It was. It was. I fuckin' hated it, man. It made me wanna puke. [Switches to Frankie.] Yeah, but to kill someone. [Switches to JAKE; big baby, teary.] Oh, Frankie, I miss her already. I wish she was alive so we could go on a second honeymoon together. [Switches to Frankie.] I got some land in Florida I could sell ya. [Switches to JAKE.] Oh yeah? [Switches to Frankie.] It's called Glen Gary Glen Ross. [Switches to JAKE.] Oh I don't want to go there. [Switches to Frankie, who now speaks in a fast, staccato rhythm, with a lot of aggressive salesman energy.] Why the fuck not? The place is good. Not great maybe, but what I'm sayin' is, it's good. Not great maybe, but good. That's what I'm sayin'. It may be swamp, it may have bugs, but fuck, Jake, what's perfect? You tell me. No, don't tell me, I'll tell you. It's not great, good. Am I right? Do you understand what I'm sayin'? Should I say it again? What I'm sayin' is, fuck shit piss damn, it ain't half bad. Half good, half bad. You gotta settle. It ain't perfect. Settle. Gatta. You gotta settle. A negotiation. Give and take. You know what I'm sayin'? What I'm sayin' is ... [Switches to JAKE, frustrated and angered by Frankie’s irritating sales pitch.] Shut up! I know what you're saying, you sound life-like, granted, but you repeat yourself and you're monotonous, and you're ... insensitive to my upset about my wife. She is dead, you know. I deserve sympathy. [Switches to Frankie.] Yeah, but you killed her.
```
