# Classification request: batch 8 of 53 (40 records, IC-0681 to IC-0720)

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

## IC-0681: Steel Magnolias

- Title: Steel Magnolias
- Author (byline): Robert Harling
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTRESS 1, ACTRESS 2, M’LYNN, SHELBY, ANNELLE
- Teaser before the introduction: Yes
- Spoken words (computed): 1827
- Already set (do not supply): none

### Source block (context only)

```text
(none)
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: M'Lynn is excited to welcome home for the holidays her newly married daughter, Shelby.

ACTRESS 1: Shelby, who is diabetic, has come to tell her family that she's expecting a baby and knows her mom is going to be upset because of the danger to her health.

TOGETHER: Steel Magnolias by Robert Harling
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

ACTRESS 1: M’lynn

ACTRESS 2: Annelle and Shelby

M’LYNN: How are you, honey?

SHELBY: I'm so good, Mama. Just great.

M’LYNN: You're looking well. Is Jackson at the house?

SHELBY: No. You know how twitchy he gets. I sent him to look for stocking stuffers.

M’LYNN: Good thinking.

SHELBY: Uh. Jackson and I have something to tell you. We wanted to tell you when you and Daddy were together, but you're never together, so it's every man for himself. I'm pregnant.

M’LYNN: Shelby?!

SHELBY: I'm going to have a baby.

M’LYNN: I realize that.

SHELBY: Well…is that it? Is that all you're going to say?

M’LYNN: I...what do you expect me to say?

SHELBY: Something along the lines of congratulations.

M’LYNN: Congratulations.

SHELBY: Would it be too much to ask for a little excitement? Not too much, I wouldn't want you to break a sweat or anything.

M’LYNN: I'm in a state of shock! I didn't think ...

SHELBY: In June. Oh, Mama. You have to help me plan. We're going to get a new house. Jackson and I are going house hunting next week. Jackson loves to hunt for anything.

M’LYNN: What does Jackson say about this?

SHELBY: Oh. He's very excited. He says he doesn't care whether it's a boy or girl...but I know he really wants a son so bad he can taste it. He's so cute about the whole thing. It's all he can talk about ... Jackson Latcherie Junior.

M’LYNN: But does he ever listen? I mean when doctors and specialists give you advice. I know you never listen, but does he? I guess since he doesn't have to carry the baby, it doesn't really concern him.

SHELBY: Mama. Don't be mad. I couldn't bear it if you were. It's Christmas.

M’LYNN: I'm not mad, Shelby. This is just...hard. I thought that...I don't know.

SHELBY: Mama. I want a child.

M’LYNN: But what about the adoption proceedings? You have filed so many applications.

SHELBY: Mama. It didn't take us long to see the handwriting on the wall. No judge is going to give a baby to someone with my medical track record. Jackson even put out some feelers about buying one.

M’LYNN: People do it all the time.

SHELBY: Listen to me. I want a child of my own. I think it would help things a lot.

M’LYNN: I see.

SHELBY: Mama. I know. I know. Don't think I haven't thought this through. You can't live a life if all you do is worry. And you worry too much. In some ways it's a comfort to me. I never worry because I know you're worrying enough for the both of us. Jackson and I have given this a lot of thought.

M’LYNN: Has he really? There's a first time for everything.

SHELBY: Don't start on Jackson.

M’LYNN: Shelby. Your poor body has been through so much. Why do you deliberately want to ...

SHELBY: Mama. Diabetics have healthy babies all the time.

M’LYNN: You are special. There are limits to what you can do.

SHELBY: Mama. Listen. I have it all planned. I'm going to be very careful. And this time next year, I'm going to be bringing your big healthy grandbaby to the Christmas festival. No one is going to be hurt or disappointed, or even inconvenienced.

M’LYNN: Least of all Jackson, I'm sure.

SHELBY: You are jealous because you no longer have any say-so in what I do. And that drives you up the wall. You're ready to spit nails because you can't call the shots.

M’LYNN: I did not raise my daughter to talk to me this way.

SHELBY: Yes you did. Whenever any of us asked you what you wanted us to be when we grew up, what did you say?

M’LYNN: Shelby, I am not in the mood for games.

SHELBY: What did you say? Just tell me what you said. Answer me.

M’LYNN: I said all I wanted was for you to be happy.

SHELBY: O.K. The thing that would make me happy is to have a baby. If I could adopt one I would, but I can't. I'm going to have a baby. I wish you would be happy, too.

M’LYNN: I wish I...I don' t know what I wish.

SHELBY: Mama. I don't know why you have to make every thing so difficult. I look at having this baby as he opportunity of a lifetime. Sure, there may be some risk involved. That's true for anybody. But you get through it and life goes on. And when it's all said and done there'll be a little piece of immortality with Jackson's looks and my sense of style...I hope. Mama, please. I need your support. I would rather have thirty minutes of wonderful than a lifetime of nothing special. (Pause) Please don’t tell anybody yet. I wanna tell daddy first.

TRANSITION

. ACTRESS 1: Shelby has her baby – a beautiful little boy and only 3 months premature, but with the birth came some additional complications

SHELBY: The doctor’s just been trying to strengthen my veins (shows bruises on her arms) They’re in terrible shape. It’s my dialysis. It’s not any big thing. No big thing. Don’t look at me like that. Having Jack Junior put too much strain on my kidneys and not they’re kaput. That’s all. The doctors said this would probably happen. I’ll just have a kidney transplant and I’ll be fine. There are people at dialysis that have been waiting for years. But I’m lucky. I don’t have to wait anymore. Mama’s going to give me one of her kidneys.

M’LYNN: We haven’t known that long. We were all just tested last week. I’m the closest match. There are four categories for an organ match. I matched the best.

SHELBY: Swimsuit, evening gown, talent and personality interview. . . . I’m sorry . . . that’s Tommy’s joke. I think it’s very funny.

M’LYNN: I was just so relieved it was me. The boys are young. I would never want them to go through it. And who would want one of Drum’s mean old organs? But! The best thing about all this is that with all the tests and tuff, I have discovered I have the constitution of someone ten years younger. How about that!

SHELBY: My operation’s simple. Mama’s is awful. They basically have to saw her in half to get the kidney. It’s major, major surgery for her.

M’LYNN: They do it on “Circus of the Stars” all the time.

SHELBY: (with a sad smile at her mother’s joke) There have been more than enough tears.

M’LYNN: I’m happy. Look at the opportunity I have. Most mothers only get the chance to give their child life once. I get a chance to do it twice. Poor Shelby . . . .

SHELBY: (firmly) Don’t say that. I have my baby. I’m very happy. If this is a part of the price I have to pay, then I have to pay it. I can deal with it . . .

TRANSITION

ACTRESS 2: Nearly a year later . . . .

ACTRESS 1: And the price to be paid turns out to be much higher than expected. . .

ACTRESS 2: Annelle, a friend of the family, tries to provide some comfort

M’LYNN: After the transplant failed, she went back on dialysis -- She’d been doing fine the last few months. But last Monday, everything went wrong. It was like dominoes. They thought they could correct things with a little surgery. As they wheeled her down, she said, “Mama. I’m going to feel so good when this is over.” They gave her the anesthetic.

ANNELLE: In a way she was right. Maybe she knew she was going to be with her king.

M’LYNN: (a little shaken) Yes, Annelle. Maybe so.

ANNELLE: We should be rejoicing.

M’LYNN: You go ahead. I wish I could feel that way. I guess I’m a little selfish. I’d rather have her here.

ANNELLE: Miss M’Lynn. I don’t mean to upset you by saying that. You see, when something like this happens, I pray very hard to make heads or tails of it. I think in Shelby’s case, she wanted to take care of that baby, of you, of everybody she knew . . . and her poor body was just worn out. It wouldn’t let her do everything she wanted to do. So she went on to a place where she could be a guardian angel. She will always be young. She will always be beautiful. And I personally feel much safer knowing she’s up there on my side. I know some people might think that sounds real simple and stupid . . .and maybe I am. But that’s how I get through things like this.

M’LYNN: (gentler) Thank you, Annelle. I appreciate that. Shelby, would not want us to get all mired down and wallow in this. She would look on it as just one of life’s occurrences.

(Annelle fades and is replaced by Shelby)

SHELBY: I'm going to have a baby. (echos)

M’LYNN: We should deal with it the best way we know how . . . and get on with it.

SHELBY: Would it be too much to ask for a little excitement? (echoes)

M’LYNN: That’s what my mind says. I wish somebody would explain that to my heart.

(BEAT – remembering)

SHELBY: Mama. I want a child of my own. I think it would help things a lot. (echoes)

M’LYNN: I couldn't leave my Shelby. I just sat there and kept pushin' the way I always have where Shelby was concerned.... I was hopin' she'd sit up and argue with me. Finally we realized there was no hope.

SHELBY: Mama. You can't live a life if all you do is worry. And you worry too much. In some ways it's a comfort to me. I never worry because I know you're worrying enough for the both of us. (3choes)

M’LYNN: They turned off the machines. (Pause)

SHELBY: Mama. Diabetics have healthy babies all the time. (echoes)

M’LYNN: Drum left.. couldn't take it. Jackson left. (Slight "laugh") I find it amusin'.. men are supposed to be made outta steel or somethin. I just sat there. I just held Shelby's hand.

SHELBY: No one is going to be hurt or disappointed, or even inconvenienced. (echoes)

M’LYNN: Oh God.. I realize as a woman how lucky I am! I was there when that beautiful creature drifted into my life.. and I was there when she drifted out of it. It was the most precious moment of my life... [Sighs]

SHELBY: And when it's all said and done there'll be a little piece of immortality with Jackson's looks and my sense of style...I hope. (echoes)

M’LYNN: I'm fine.. I'm fine.. I'm fine.. I'm FINE! [sobbing/screaming]

SHELBY: Mama, please. I need your support.

M’LYNN: I could jog all the way to Texas and back.. but my daughter can't!! She never could!! Oh.. God . . . I'm so mad I don't know what to do!! I wanna know why! I wanna know WHY Shelby's life is over!! I wanna HOW that baby will EVER know how wonderful his mother was.. Will he EVER know what she went THROUGH for him? Oh God I wanna know WHY? WHY? Lord...I wish I could understand!

SHELBY: I would rather have thirty minutes of wonderful than a lifetime of nothing special. (echoes)

M’LYNN: No...NO...NO!! It's not supposed to happen this way! I'm supposed to go first!! I've always been ready to go first! I don't think I can take this.. I.. I don't think I can take this! I just wanna hit somethin'! I just wanna hit somebody.. till they feel as bad as I do!! I just wanna hit something!

SHELBY: But you get through it and life goes on. (Echoes)
```

---

## IC-0682: Stop, Rain

- Title: Stop, Rain
- Author (byline): Not specified
- Work: The Best Ten-Minute Plays 2007
- Publisher: Smith & Kraus
- Publication date as stated: 2008
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: RAIN, MARLA
- Teaser before the introduction: Yes
- Spoken words (computed): 1394
- Already set (do not supply): none

### Source block (context only)

```text
Author: Patrick Gabridge
Book: The Best Ten-Minute Plays 2007
ISBN: 978-1575255897
Publisher: Smith & Kraus
Date (Month/Year): 2008
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Decades ago, a hidden population of pregnant girls carried a secret so shameful that their families sent them into exile, far from the whispered suspicions at home.

ACTRESS 2: Generations of parents, fearful of the social taboo of illegitimacy, concealed their unwed daughters' pregnancies and sent them to maternity houses across the country to give birth among strangers.

ACTRESS 1: Most of these new mothers would never know anything about what happened to their babies, who raised them, or how.

ACTRESS 2: But times have changed. Today most adoptions within the United States today are what are termed "open adoptions."

ACTRESS 1: In Patrick Gabridge’s “Stop, Rain” Birth mother Rain desperately wants to see the son she placed for adoption,

ACTRESS 1: But adoptive mom Marla feels she needs to protect her son from Rain's screw-ups and chaotic life.

ACTRESS 2: Can the two mothers learn to understand each other?

TOGETHER: Stop, Rain by Patrick Gabridge

Scene: A park bench. At Rise: Marla waits impatiently. She's in her late thirties and wears a business suit. Finally, Rain enters, a little anxious. She's in her late teens or early twenties, shabbily dressed.
```

### Performance text (classify this)

```text
Patrick Gabridge

RAIN: Sorry.

MARLA: I've been waiting more than an hour.

RAIN: The buses are all screwed up. I hate the bus. The people smell, the men press up against you. And you always gotta wait for the damn thing. Waiting's not my thing, you know.

MARLA: Mine neither.

RAIN: Right. Sorry. You look nice. Is that a new suit?

MARLA: No. It's just one I wear to work. I had to take off from work to be here.

RAIN: Right. It looks good. I know you're busy and all that ... I've been looking for a job.

MARLA: I thought you had one. At the grocery store.

RAIN: Didn't work out. My manager, he was crazy. Always making remarks, you know, passes. I like to flirt a little sometimes, bur he ... You know how it is. And the buses suck. I had to take two transfers to get there.

MARLA: What happened to the car?

RAIN: The car.

MARLA: The car, Rain. The money. The car that Rich helped you choose, so it would be reliable. So you could keep a job.

RAIN: Right. About the car. That's sort of why I called you.

MARLA: Did it break down?

RAIN: Not exactly.

MARLA: Julio.

RAIN: He said he was going to the store for some bread and milk, just like a normal person. Then I don't see him for two days, and when he comes dragging his sorry ass home, no car. Not even most of the money left. You should have heard me scream at him. I kicked him out that night.

MARLA: But he's back.

RAIN: Some things you can't explain.

MARLA: No.

RAIN: SO the car was really a good idea, Marla. I learned my lesson. If I had another, I'd hide the keys. You know I hate to ask for anything, but you know what they say about the poor man: Give him a fish and he eats today, teach him to fish and he, you know, eats a lot more.

MARLA: Aren't you even going to ask about him? RAIN: You know I want to ... How's Nathan? MARLA: He's great. I brought some pictures.

(She pulls out an envelope and sets it on the bench next to Rain, who looks at it, but doesn't pick it up.)

RAIN: Thanks. What's he doing these days?

MARLA: The whole pre-school thing. He likes the social part of it, making new friends, the playground. When he comes home, he's full of stories of who did this and who did that. He's even starting to read a few words - dog, cat. Stop, go. It's like a window opened up to his mind, and all of a sudden a.b,c, go dog go. He's amazing.

RAIN: You're a good ... a good mother to him now. And I'm sure Rich is a good father.

MARLA: We're trying. It's not always easy, but we're very happy. And grateful, Rain. We'll always be grateful to you.

RAIN: It was the right choice for me. For him. I'm glad it was you that adopted him.

MARLA: Rain?

RAIN: Hmm.

MARLA: You missed our meeting last week.

RAIN: I didn't forget. Don't let him think I forgot. I ... it was the car and Julio and the buses and I ...

MARLA: You should have called.

RAIN: My phone's out. If I can get a job again - MARLA: You should have found a pay phone, something.

RAIN: I guess I could have left a message, but ... Was Nathan pretty disappointed?

MARLA: Of course he was. This is the third time this year, Rain. It's one thing to let us down, we're grown-ups, we can handle it. He's just a little boy.

RAIN: I won't let it happen again.

MARLA: Neither will we. RAIN: What do you mean?

MARLA: Rich and I have been talking. Debating. Arguing. It doesn't need to be permanent. It would be good for him to know you, to have a connection to his roots. The books all say he'll need it. But for now, he's too young to be so deeply disappointed so often.

RAIN: You're cutting me off?

MARLA: We want to suspend visits, yes. For a while. We'll keep sending pictures and letters, and we still want them from you.

RAIN: He's my son.

MARLA: And he's my son, too.

RAIN: I gave him life.

MARLA: We know that. All three of us want you to be a part of his life. You're the one who acts like you don't.

RAIN: That's a lie. Sometimes I screw up. I'll make it right.

MARLA: He's only four, Rain. He shouldn't have to do this.

RAIN: But he does, because I'm his mother and that's the way I am.

MARLA: Oh, you've proved it to him quite well. It's hard for him to understand any of this, and the way you've behaved will just make him angry with you.

RAIN: It's an angry world, Marla. I'll do better, I promise. I do a lot of stupid things in my life. I know that. But most days, I know I did the right thing by giving him to you and Rich. But at night, sometimes I wake up and think about him, about him being with me, snuggled in bed, curled up in a little ball in my arms, and I stroke his hair to calm him after his nightmare and I wrap my arms around him. Blood of my blood, breath of my breath. I hold him tight, so he knows he's safe and I'll never let him go. Sometimes I'll stay like that all night, with him in my arms and in my mind, more than a dream, more than a dream. Until the sun comes up, and I have to let him go back to you and Rich, let him go all over again. It hurts, deep in my guts, and I know it won't ever go away. All I want to do is lay there in bed, all day long, until the darkness comes again, and I can have him back.

MARLA: You can't have him back.

RAIN: I know you're a good mother to him. I know it. But even a bad mother, like me, wants to see her son.

MARLA: We all want the same thing, right? For Nathan to grow up safe and happy and loved. Don't make him doubt that he's worthy of being loved.

RAIN: I missed a few meetings, that's all ... I can find you. I have your phone number. I figured out your last name. I know people with computers, and they say that's all it takes. I can find where you live.

MARLA: Is that a threat?

RAIN: It's a fact.

MARLA: And what then? You want to take four years of building trust and flush it down the toilet?

RAIN: You're the one who suddenly wants to change things.

MARLA: Because you're hurting him.

RAIN: It was an accident.

MARLA: But you know what, that's fine. If you want to undo all that, go ahead. Make yourself the bad guy.

RAIN: Of course, it has to be me. Look at you, you have everything - a house, a job, an education, a husband. And now you have a son. How am I sup-posed to fit in with all that? I'm stupid and messy. My life is out of con-trol. But I exist. You can't pretend I don't. Nathan knows better.

MARLA: We give you chance after chance, but you keep blowing it. We opened our lives to you.

RAIN: Give me a break. We met a few times, in out-of-the-way places, places I can hardly get to. You saw how completely whacked my world is, and you felt guilty, so you paid me off a little. But I fuck up a few times, and you slam the door in my face. That mess is why you have a son. You've been looking for an excuse, Marla. Opened your lives to me? I gave you my son. You gave me a few hours of your time, gave me a couple breaks. I just want a scrap, a few hours with Nathan, every once in a while. You're a mother now. What does that mean to you?

MARLA: I ... I know what it means.

RAIN: Fine. You're in control. You decide. OK? But you have to let me keep trying. Please? One more chance?

MARLA: I promised Rich that I would not waver. Let me talk to him, OK? RAIN: OK.

MARLA: But try to do something right. Send Nathan a letter.

RAIN: I will. I'll send a whole handful.

MARLA: I'm sorry.

RAIN: Don't be. I'm going to take care of it. You'll see.

MARLA: I have to go back to work.

RAIN: Yeah ... Hug him for me. Please? I mean, really think of me when you're doing it. I'll know.

MARLA: I will.

(There's an awkward moment of parting, a consideration of an embrace, but it doesn't happen. Marla exits')

(Rain picks up the envelope and opens it. She examines each photo slowly, touching the faces, trying to keep her composure. She hunts in her ragged purse for a pen and a scrap of paper and begins to write as: Lights to black.)
```

---

## IC-0683: SUFFS

- Title: SUFFS
- Author (byline): Shaina Taub
- Work: Not specified
- Publisher: Theatre Communications Group
- Publication date as stated: Nov 2024
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: SUFFS, ALICE, TOGETHER, ACTRESS 2, DORIS, INEZ, DUDLEY, WILSON, ALVA, MOLLIE, LUCY, MRS. HERNDON, DR. WHITE
- Teaser before the introduction: Yes
- Spoken words (computed): 1465
- Already set (do not supply): none

### Source block (context only)

```text
Author: Shaina Taub
ISBN: 978-1636702261
Publisher: Theatre Communications Group
Date (Month/Year): Nov 2024
Historical Figures
Alice Paul left the National American Woman Suffrage Association (NAWSA)
because of a fundamental disagreement over strategy and a belief that NAWSA's
methods were too conservative and slow. She advocated for a more aggressive
approach focused on lobbying Congress for a federal constitutional amendment,
while NAWSA prioritized a state-by-state campaign. This led her to form the
National Woman's Party (NWP) to pursue her more radical vision, which
included direct confrontation and protests.
Doris Stevens organized party delegates for each of the 435 Congressional
districts in an effort to achieve nationwide enfranchisement for women. She also
participated in the Silent Sentinels vigils outside the White House from 1917 –
1919, a protest aimed at forcing the passage of a constitutional amendment for
women's voting rights. Stevens was arrested on multiple occasions and wrote a
memoir in 1920, Jailed for Freedom, outlining the struggle. Once voting rights
for women had been achieved, Stevens turned her attention to the legal status of
women and fought for the Equal Rights Amendment.
Ida B. Wells was fighting a bigger battle — against sexism and racism — and
faced obstacles within their own movement. She took part in the first suffragist
parade in Washington, D.C., in 1913, which was organized by the National
American Woman Suffrage Association, as the sole Black woman in the Illinois
delegation. Wells marched with this group despite being asked at the last moment
to move to the back of the procession with the segregated contingent.
Alva Belmont was the Inez Milholland is best known
most important financial for leading the 1913
benefactor among the women's suffrage parade in
leaders of the Washington, D.C., dressed in a
Congressional Union for flowing white cloak and crown
Woman Suffrage (CU) and riding a white horse. She
and its successor was a talented speaker and a
organization, the passionate advocate for
National Woman's Party women’s rights, socialism, and
(NWP). pacifism.
Lucy Burns, tall and red-haired with bright blue eyes, was a fierce fighter in the
cause for woman suffrage. She carried a banner emblazoned with the slogan
shown above when she led a procession of women through a train yard in 1919.
All the women had served time in jail for protesting in support of woman
suffrage. The women of the “Prison Special” railroad tour of the country wore
drab, baggy dresses similar to the uniforms they were forced to wear when they
were imprisoned. It was fitting that Lucy led them, since she had spent more time
in prison than any other American woman suffragist.
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: This is the mostly forgotten tale of a handful of fearless females who fought for the right to vote.

ACTRESS 2: It’s called the 19th Amendment, and even though the battle began with the Seneca Falls convention in 1848, the Constitutional amendment wasn’t ratified until 1920.

ACTRESS 1: And even then, many women of color continued to be disenfranchised by literacy tests and discriminatory Jim Crow laws until The Voting Rights Act was passed in 1965.

ACTRESS 2: Today The Voting Rights Act is under review by the Supreme Court and old battles have become new again.

ACTRESS 1: Born from our nation’s ugliest history — from the brutal struggles of those who fought for their Constitutional right to vote – 1848 to 1920 to 1965, people have fought for democratic representation.

TOGETHER: If voting rights are eroded for minorities, will the rights of women be far behind?

ACTRESS 2: Every character in this play provides an echo of the past.

ACTRESS 1: Just like us, they were living in an uncertain and hostile world. We tell their story because it is
```

### Performance text (classify this)

```text
Suggested Roles Actress 1: SUFFS, Alice, Wilson, Mollie

Actress 2: SUFFS, Doris, Inez, Dudley, Alva, Lucy, Mrs. Herndon

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

SUFFS: (Pg 106-107) (alternate lines between actresses) How long must women wait for liberty? How many more marches in the streets? How many more efforts gone to waste? How many more deafening defeats? How many more histories erased? How many more Joans burned at the stake? How many more of us will it take? How long? How long til it’s too late?

ALICE: Meet me at the White House gates at dawn!

TOGETHER: Our story

ACTRESS 2: And to remind ourselves that people, ordinary people, are capable of impacting our future.

TOGETHER: SUFFS by Shaina Taub

ALICE: (Pg 18-19) (holding a protest sign) I don’t want to beg for crumbs from a country that doesn’t care what I say. I don’t want to be a meek little pawn in the games they play. I want to shout it out loud in the wide-open light ‘til our generation has made things right. (to Doris) (Pg 33-37) Numbers?

DORIS: 26 floats, 9 brigades – a delegation from all 48 states. Representatives from 30 universities! 200,000 people attending . . . and Ida B Wells wrote to say she plans to march.

ALICE: Ida B Wells?!

DORIS: But . . . we’ve received letters from several southern doners threatening to pull out if colored women participate. Others say they must march in back . . ,.

ALICE: (thinking) Let’s make a special colored delegation at the back of the line. No one pulls out. It’ll all be fine. Without the southern women’s support, there might be no march. ****The March*****

INEZ: (Pg 44-45) Mister President, hear our cry. We, the women of the country demand to be heard.

SUFFS: We demand to be heard!

INEZ: We demand to be seen

SUFFS: We demand to be seen!

INEZ: We demand a voice of our own

SUFFS: We demand an amendment!

TOGETHER: We demand an amendment!

DORIS: (Pg 46-47) But then a mob of sneering men storm the street!

SUFFS: Hundred of hooligans spit and jeer . . .

INEZ: (Pg 48) Listen up! If we all band together . . . Follow me! (protest chant) Get back. Make way. You’re not stopping us today.

SUFFS: (echo) Get back. Make way. *****The Oval Office****

DORIS: (Pg 65) June 5, 1913, our first meeting with President Wilson

DUDLEY: (Pg 63-64) (to President) Sir. . . a committee is here from The National American Woman Suffrage Associa –

WILSON: Ah yes. The ladies. No one adores ladies more than I. When you’re with ladies, you can enjoy your sacred duty as a man. (Dudley moves to interject, but Wilson barrels on) It isn’t wise to weigh down women with the worries of the day. A female wants to focus on her family. (to Dudley) Send them in. (Dudley exits)

DUDLEY: (Pg 75) (addressing the SUFFS) I’m Dudley Malone . . . and you’re the suffragettes?

DORIS: It’s actually suffra-gist, not suffra-gette. Suffragette is what the papers all us to ake us seem like Kewpie dolls instead of legitimate reformers. One of their many tactics to diminish and disempower us.

ALICE: (Pg 66) (SUFFS enter assertively) Mister President, governments derive their just powers from the consent of the governed. Your administration has no right to legislate any reform without the consent of women!

DORIS: (outraged) (Pg 53) At the march, this old man called me a b****!

WILSON: (Pg 64-65) (calmly, dismissively) Ladies rely on us to supervise their lives. They require a man to manage their affairs. Why would ladies vote?

INEZ: (Pg 44-45) Mister President, demand to be heard.

WILSON: (Pg 64-65) (continuing through the interruption) We provide all that they need. If politics pollutes our ladies’ lives, we’ll sacrifice virility, and compromise fertility and threaten the stability of the USA. (long tense pause) (Pg 68) My chief of staff will escort you to the door. Dudley . . . *****Later****

ALICE: (Pg 84-85) My fellow suffs, it’s time to show Wilson that [we] are the vanguard of the future. (chanting) VOTE WILSON OUT!

SUFFS: VOTE WILSON OUT!

ALICE: Let’s show Wilson that if he continues his hostility toward us, we’re ready to. . .

DORIS: (Pg 91) How will we do it when it’s never been done?

ALICE: I want us to meet someone . . . A social-ite . . .

ALVA: (Pg 92-93) (enters, she is obviously very wealthy, she introduces herself) Alva Belmont. I divorced my husband for philandering, now I’ve got his millions for philanthropy.

ALICE: (rushing to shake her hand) I’m Alice Paul. We’re starting a women’s political party and we’d love for you to join it.

ALVA: You mean you’d live for me to fund it. (beat) Let me get this straight – you gals just declared political warfare on Wilson and his party and now you shamelessly demand my riches for this risky rebel coup. The nerve (a tense beat) I LOVE it. To whom do I make out the check? *****Months Later before the White House gates***** The SUFFS are standing in silent protest, blocking the gate to the White House.

DORIS: (Pg 109) I won’t forget that frigid January morning when my heart was in my stomach at the president’s front door.

MOLLIE: (Pg 110-111) It looks like people are blocking the entrance to the White House.

DUDLEY: (to someone trying to enter) Unfortunately, the president must postpone your meeting indefinitely. Since early this morning, the National Woman’s Party has been keeping a silent vigil at the gates. They’re refusing to leave until the president endorses suffrage.

SUFFS: (Pg 112) (actresses should alternate lines) And what started as a dozen turned to hundreds within weeks. Though not a word was spoken, our volume only grew.

DORIS: (Pg 113) April 6th, 1917, Wilson declares war on Germany.

ALICE: (reading the paper, she quotes Wilson) “It is a fearful thing to lead our country into war, but we must fight for democracy.” (with an idea) Let’s put Wilson’s words on our banners. Show how hypocritical he is to fight for democracy abroad while denying it to us here at home.

LUCY: (Pg 114-115) But wait – it also says – “Any citizen who makes unpatriotic statements shall be punished.

ALICE: I could feel us start to panic,

SUFFS: (actresses should alternate lines) But then suddenly we felt it – every cost and battle lost of every generation past. So we rose up in defiance. We chose to risk it all for our sisters’ silent voices. Let the patriarchy fall!

(sirens as unseen policemen and onlookers close in on the SUFFS and they are all arrested) *****In the Oval Office*****

DUDLEY: (Pg 116-117) (enters with urgency) Mister President, something terrible has happened. I just witnessed the trial of the National Women’s Party pickets. The judge sentenced them to six months in prison for “obstructing traffic.” Sir, surely you agree this is some kind of grievous mistake.

WILSON: Well, this is the first I’m hearing of the suffragette situation.

DUDLEY: But I was standing right here when you ordered their arrest. And it’s suffra-gist, not suffra-gette. Perhaps a pardon is in order?

WILSON: Those girls’ banners are treasonous.

DUDLEY: Does quoting the president amount to treason? (Pg 118) (beat, then with passion) It is high time that men of this generation stood up in support of the women of this country. If men had been peacefully demanding our right to vote for over half a century, if men had been repeatedly ignored or met with evasion by Congress; you would understand and forgive their righteous indignation.

WILSON: Come on, now Dudley. Be a man! (exits) *****Occoquan Prison *****

MRS. HERNDON: (Pgs 120-121) Inmates! This is my prison mess hall. You will sit down, shut up and eat your food.

ALICE: But, we’re political prisoners and we refuse . . .

MRS. HERNDON: (interrupting) Political prisoners? Ain’t no such thing in America. Guards, if ona-a these girls says another damn word, knock her teeth out. Now eat!

ALICE: Hunger strike! (Pg 124) Wilson will be shamed into a pardon as soon as word gets out he’s letting women die of starvation.

*****Press Conference and Occoquan Prison *****

DR. WHITE: (Pg 133-136) Mister President, I have the report on the conditions in the prison. This ought to debunk all the baseless claims that the women are being mistreated

WILSON: (reads report aloud at a press conference) We are providing the ladies with excellent care.

DORIS: A doctor came and dragged me out of my bed.

WILSON: Their treatment includes artificial feeding.

DORIS: We are forcibly fed three times a day.

WILSON: The ladies receive it without resistance. There is no force necessary.

DORIS: They pry my mouth open with pliers, and I try to clench my teeth shut but they shove the tube down my throat, up my nose.

WILSON: The ladies are offered fresh milk and eggs.

LUCY: They pour raw eggs through the tube to my gut.

WILSON: They experience no discomfort, and all rumors in the press of physical abuse are entirely false.

LUCY: They withdrew the tube and I bled out my nose, out my mouth, so much blood. (beat) They took Alice away. Have not seen her in days . . .

WILSON: (to Dr. White an order disguised as a suggestion) Someone ought to commit her to an asylum.

DR. WHITE: She does exhibit symptoms of hysteria, such as verbal displays of opinions in public. (Pg 137) (to Alice) Sane women do not starve themselves to prove a point. If you refuse to eat, I shall sign the president’s order for you to permanently committed to St. Elizabeth’s Asylum.

ALICE: (non-verbally responds in defiance, Dr. exits; she speaks to audience) (Pg 140) Is it so insane to want my own choice? Wouldn’t you be hysterical if you had no voice? *****Presidential Address to Congress *****

WILSON: (Pg 147) Let it be known that the voices of foolish agitators in the streets did not reach me at all. Rather it was the voices of patriotic ladies whose service lies at the heart of the war. I know that heart will beat stronger if you give them this . . .thing.

DORIS: (to audience) Fun fact! He actually said that.

WILSON: Thank you and God bless America. (off the podium and away from cameras, he drops the façade) Oh, please. Passing the amendment through Congress means nothing. Convince 36 states to ratify it! The south will never let ladies vote, let alone colored ladies, thank God!

SUFFS: (Pg 170) (alternate lines between actresses) The world can be changed. So keep marching, keep marching. Let history sound the alarm of how the future demands that we fight for it now. Progress is possible, not guaranteed.

TOGETHER: Keep marching!
```

---

## IC-0684: Tables and Chairs

- Title: Tables and Chairs
- Author (byline): Stanley Rutherford
- Work: Scenes and Monologs from the Best New Plays
- Publisher: Meriwether Publishing
- Publication date as stated: Sep 1992
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ALICE, NAOMI
- Teaser before the introduction: Yes
- Spoken words (computed): 1468
- Already set (do not supply): none

### Source block (context only)

```text
Author: Stanley Rutherford
Book: Scenes and Monologs from the Best New Plays
ISBN: 0916260933
Publisher: Meriwether Publishing
Date(Month/Year): Sep 1992
```

### Introduction (context only: never use it for content warnings)

```text
Actress 1 (ALICE) : Every marriage starts with a lot of hope and dreams about a life-long

association filled with love and togetherness. . . . . . . Actress 2 (NAOMI): HOWEVER . . . . committing to a long term relationship like marriage

solely on the basis of that feeling of love is a mistake. Actress 1 (ALICE): It is not. Howard and Alice are like . . . . like Peanut Butter and Jelly, like

Ham and Eggs – like . . . . Actress 2 (NAOMI): Like Tables and Chairs Together: by Stanley Rutherford.
```

### Performance text (classify this)

```text
ALICE: Howard says that –

NAOMI: I don't care what Howard says...if Howard wants to say something, Howard can say if for himself...isn't that right Howie? (glares at Howard)

ALICE: Howard is very shy.

NAOMI: (screams) Speak, Howard! Speak!

ALICE: Howard is the man I love.

NAOMI: Alice, Howard has been married about seventeen times, maybe more...

ALICE: Howard is the man of my dreams.

NAOMI: The longest marriage lasted about seven weeks, the shortest exactly 18 hours...remember her Howard? Gloria Garton? The ventriloquist? And then there was Mary Louise Menderman and Mieu-Mieu-Rohrbach and Allison Kildaire...

ALICE: (pause) Naomi...Howard has asked me to be his bride.

NAOMI: (sigh) Oh, Alice...

ALICE: Howard has asked me to join him in eternal wedlock.

NAOMI: Alice, you need professional help.

ALICE: Howard wants to sanctify our love.

NAOMI: Alice, Howard will get what he wants from you and then he'll dismiss you.

ALICE: He wants to marry me.

NAOMI: He wants to marry everyone...it's his plan for world peace. A world with one husband and five billion wives. Five billion wedding ceremonies with five billion wedding presents. Howard plans to return all of the wedding presents and use the cash to eliminate all international debt.

ALICE: (gasps) Isn't that wonderful!

NAOMI: It's sick.

ALICE: Howard will win the Nobel Prize.

NAOMI: Howard will be indicted for polygamy. Howard will spend the rest of his life behind bars: handcuffed, tethered, and gagged. (pause, gently to Alice) Alice, Howard is a psychopath.

ALICE: I love Howard.

NAOMI: Howard is a sociopath. He’s a barbarian who preys on unsuspecting women, especially those with a healthy bank account.

ALICE: I have bags of money.

NAOMI: That’s what Howard wants.

ALICE: Howard can have it all.

NAOMI: He wants it all.

ALICE: Isn’t Howard wonderful?

NAOMI: Alice, Howard is a Casanova who has ruined the lives of countless women…Mieu-Mieu Rohrbach, Mary Louise Menderman…

ALICE: I love Howard.

NAOMI: Claudia Grierson, Melonie Camberwell, Dottie Leachman, Mimi Nash…

ALICE: Naomi…Howard and I are going to be married this evening. And I would like you to be my maid of honor.

NAOMI: (quickly) I’m going to be having major surgery.

ALICE: Naomi…

NAOMI: Major exploratory surgery.

ALICE: It would mean so much to us both.

NAOMI: I am going to be in the depths of anesthesia.

ALICE: We want it to be special…just Howard and I and our very special friends, Naomi and Spencer…just the four of us…our family.

NAOMI: (dryly) I wish I’d known sooner.

ALICE: We wanted it to be a surprise…Howard wants me to wear his mother’s wedding dress…

NAOMI: Alice…

ALICE: The very dress that she wore when she married Howard’s father.

NAOMI: Alice, Howard wants everybody to wear his mother’s wedding dress. I’m surprised he’s not going to wear it himself. Everyone else has: Mieu- Mieu Rohrbach, Melonie Camberwell, Gloria Garton. Have you ever seen Howard’s mother’s wedding dress?

ALICE: Howard wants it to be a surprise.

NAOMI: Alice, Howard’s mother was a saint, God knows…but she had a hump, a very large hump, back here…(points)…and so does the dress…you’ll have to pad yourself to fill it out. (Alice is starting to have doubts) Alice, we have known Howard since infancy…and he’s the same now as he was then. He’s still an infant… Alice, Howard needs help, he’s not self-sufficient…he can’t get up in the morning, and Spencer and I have graciously taken responsibility for his care and protection…

ALICE: Howard says that he takes care of you.

NAOMI: We take care of him. It’s a long story, Alice, awfully long and awfully tragic. Howard needed someone to take care of him after his mother died. He couldn’t take care of himself, and so Spencer and I adopted him. Howard is our son. We’ll be your in-laws if you marry him.

ALICE: (screaming) Howard…Howard…Howard talk to me! (long pause, moves to Naomi for comfort) I don’t know why I love him.

NAOMI: Honey, love is a heartache. You’re better off without it. It’s overrated. It’s an enzyme. You can get the same feeling from eating chocolate.

ALICE: (pause, stunned) I didn’t know.

NAOMI: I didn’t either. I had to learn.

ALICE: And I’ve watched and I’ve listened trying to learn the movements, the attitudes, the right things to say and do, when to say it, when to keep it to myself…

NAOMI: (comforting) Honey, you’re doing just fine.

ALICE: I’m not a real person. I’m a pretend person.

NAOMI: You’re a very nice person, Alice.

ALICE: (hysterical) I am not a person!

NAOMI: Honey, you’ve got to relax.

ALICE: I have no personality!

NAOMI: Alice, honey, you don’t need a personality to be a person.

ALICE: I want a personality.

NAOMI: Personality is a completely overrated commodity.

ALICE: I want to be like you. You’re fun.

NAOMI: I am?

ALICE: Everyone thinks you’re fun.

NAOMI: I didn’t know that.

ALICE: I want to be fun too.

NAOMI: You are fun.

ALICE: No, I’m not…I’m neurotic.

NAOMI: Alice…

ALICE: (loudly) I’m neurotic!

NAOMI: (louder) I don’t like that word!

ALICE: (screams into Naomi’s face) Neurotic!

NAOMI: Alice, there are certain words that I simply cannot tolerate being used in my presence, and that word it one of them. It is a bad word, Alice.

ALICE: I’m manic-depressive.

NAOMI: Alice…

ALICE: I’m schizophrenic.

NAOMI: (loudly) Bad words! Bad words! Bad, bad, “psychology” words.

ALICE: I disappear with other people leave the room. I vanish. I am a planet. I have no light source of my own. I need other people, light-giving people off of whom I can reflect.

NAOMI: You need to eat more chocolate.

ALICE: I need Howard.

NAOMI: (annoyed) Alice…

ALICE: I need you. (she opens her arms to Naomi)

NAOMI: (embracing Alice) Alice…

ALICE: I’d like you to be my sister.

NAOMI: Alice, I don’t like that word.

ALICE: I never had a sister.

NAOMI: It’s not you I don’t like, it’s the institution.

ALICE: We’d be so close.

NAOMI: We are close.

ALICE: Even closer.

NAOMI: Let’s just be friends.

ALICE: (gasps, thrilled) I’ve never had a friend. I want both of you to be in my wedding so very much.

NAOMI: Honey, I’m having major surgery.

ALICE: Couldn’t you have it tomorrow?

NAOMI: It’s urgent…it has to be done as soon as possible.

ALICE: Maybe we could fit it in before the wedding…

NAOMI: We are not going to fit it in before the wedding.

ALICE: …cut you open, move things around, sew you up…So why don’t we have major surgery and then a little supper -- a nice postoperative, prenuptial supper…

NAOMI: I don’t think I’m going to be up for it.

ALICE: And then we’ll have the wedding!

NAOMI: And then we’ll have the consummation, the disenchantment, the lamentations, and then we’ll have the divorce.

ALICE: (oblivious) I’m so happy.

NAOMI: Alice…

ALICE: I want to have babies.

NAOMI: Alice…

ALICE: And I want them to look like Howard.

NAOMI: Alice…

ALICE: I want them to look like Howard.

NAOMI: Alice…

ALICE: Howard’s eyes and Howard’s nose…

NAOMI: Alice…

ALICE: I want them to sound like Howard and smell like Howard…

NAOMI: You need professional help.

ALICE: I had never experienced real life, I mean real, real, life, until that wonderful moment when I opened my door and saw this beautiful mad standing on my doorstep and then he smiled and I was terrified, my heard was pounding, I was confused…and then he asked me if I wanted to buy a vacuum cleaner…

NAOMI: He’s stolen it.

ALICE: …but I didn’t need a vacuum cleaner…

NAOMI: No one does.

ALICE: I already had a vacuum cleaner, and then he said his name was Howard and I said my name was Alice, and I was paralyzed with fear and joy, and then he asked if he could come it and then he said he wanted to marry me and make a million babies, and then he told me about his friends. He said that you had fallen on hard times and had no place to live and needed a place to stay for a few days and maybe, he said, that I might have a place for you to stay and maybe I might be able to spare some food. (pause) I was thrilled. I’d always wanted someone to live with me, someone who needed me, because my life had been nothing but pain and loneliness and everyday was solitude and terror in the face of an enormous and terrifying world…I had nothing to hold on to, no one to tell me that things were going to be all right until I met Howard and got to know his wonderful friends.

NAOMI: Alice, Howard and Spencer and I are not nice people. We are not the kind of people you want to have lying around your home. We don’t have a real home. We’re on the run, we’re fugitives. We’re wanted in all 50 states…shoplifting, petty theft, extortion…There are posters out with pictures of us. It was the Howard-the-Evangelist episode that pushed us over the edge…an awful period, Alice. We’d set up a nine hundred number and Howard was passing himself off as a television evangelist…call Howard and find salvation. And you’d dial the nine hundred number and get a prerecorded message from Howard. And “inspirational” message…it was quite lucrative…They’re after us for fraud. Alice, we’ve had to resort to a life of crime.

ALICE: (confused, then enthusiastic) I want you to know that you can stay here forever. I will hide you and feed you and we’ll create our own beautiful world safe from the outside.
```

---

## IC-0685: That First Fall

- Title: That First Fall
- Author (byline): Daria Polatin
- Work: Not specified
- Publisher: Vintage
- Publication date as stated: March 2014
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: SKYLER, ZOE
- Teaser before the introduction: No
- Spoken words (computed): 1182
- Already set (do not supply): none

### Source block (context only)

```text
Author: Daria Polatin
Books: Plays for Two
ISBN: 978-0345804549
Publisher: Vintage
Date (Month/Year): March 2014
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Every year as graduation time rolls around, high school seniors around the country face waves of mixed emotions.

ACTRESS 2: Relief that high school is over;

ACTRESS 1: Elation to be moving on;

ACTRESS 2: And of course, sadness that friends forged over years are going their separate ways.

ACTRESS 1: Tearful promises to keep in touch are made, but will things ever truly be the same?

ACTRESS 2: For Skyler and Zoe, a Thanksgiving trip home from their 1st year of college forces them to re-examine exactly what they mean to each other.

TOGETHER: That First Fall by Daria Polatin
```

### Performance text (classify this)

```text
SKYLER and ZOE, two girls around eighteen, sit on the stoop of a brownstone in Brooklyn. ZOE is dressed in preppy clothes, and SKYLER is a hippy-hipster blend. It's dusk. SKYLER is rummaging through her bag.

SKYLER: I mean it was just like, so lame, you know? Like, we read Wuthering Heights in high school, right? And no one there had even heard of it . . . Oh, and also? No one there speaks English. So that's super fun. 'm so over college . . .

ZOE: It'll get better.

SKYLER: I hope so. Do you have to take stupid high school-level English classes too?

ZOE: Kind of. We have these-they call them foundational classes, so there's a lot of remedial stuff.

SKYLER: I don't get it: We already learned that s***, you know? That's why we went to high school.

ZOE: I know, but they just want to make sure everyone knows the basics.

SKYLER: I guess. (After a moment.) So is your mom making a turkey or is she doing duck again?

ZOE: We're going to my uncle's in Westchester.

SKYLER: Is your cute cousin gonna be 'there?

ZOE: Dan?

SKYLER: Amanda. (A tense pause.)

ZOE: I don't know. My parents haven't really told me much. They're just so excited that I'm home. They won't stop trying to feed me. I've gained, like, two pounds already and I've only been home for a day.

SKYLER: I thought you just got back.

ZOE: Oh, I got in last night.

SKYLER: Why didn't you tell me?

ZOE: It was late; and I had a ton of stuff to do today . . .

SKYLER: I was up last night. You should have told me. I streamed this really crazy ninja movie from this Japanese website with the most amazing subtitles. It was so funny.

ZOE: Cool . . . How's your mom?

SKYLER: She's good. She's selling at a bunch more stores now, so she's busy, which is good.

ZOE: That's great! . . . Have you talked to your dad?

SKYLER: You know, if he did even call? I'd be like, I don't even. wanna talk to you, okay? So don't bother. Hope you're having fun in Jersey. (Zoe doesn't know what to say.) He and whatever-her-name-is can take their twins and shove 'em back up her hoo-ha. I was over there last month, and he barely even said a word to me. All he did was fawn over those stupid kids, and he kept being like, "Aren't they cute? Aren't they cute?" Of course, they're cute-they're babies.

ZOE: I'm sorry, Sky.

SKYLER: Oh! Okay, so Friday night, 'member JD? You know, "Rasta-Man"?

ZOE: JD "The Black White Guy"?

SKYLER: He finally got dreads.

ZOE: Blond dreads? That must look weird.

SKYLER: They actually look kinda cute on him. (Beat.) So, okay: He's having everyone over on Friday, and we're gonna, like, party and eat leftover turkey and s***. He's inviting our whole class.

ZOE: Everyone came back?

SKYLER: Pretty much. I think everyone's home, except for Devon -- her family went to, like, Haiti to build houses or something. I think they're Pagan . . . So JD's is gonna be awesome.

ZOE: I'm not sure if I'll be back.

SKYLER: You have to! Everyone's gonna be there. Stella and Todd are back from Vassar, and Evangeline's home from Smith. You're not gonna stay at your uncle's the whole weekend, are you?

ZOE: No . . .

SKYLER: So come back Friday afternoon. Take the train or something.

ZOE: (Beat.) On Friday I'm actually going to stay with another friend.

SKYLER: So bring them.

ZOE: In Connecticut.

SKYLER: Who lives in Connecticut?

ZOE: A friend from school.

SKYLER: Oh . . . What's her name?

ZOE: His name is Chandler.

SKYLER: Chandler? Zoe, "Chandler"? Seriously?

ZOE: He's nice.

SKYLER: He must be if your parents are letting you stay with a guy they don't even know.

ZOE: They do know him.

SKYLER: Your parents met him?

ZOE: A couple of times.

SKYLER: When?

ZOE: At parents' weekend. And . . .

SKYLER: And what, Zoe?

ZOE: . . . He came over for dinner.

SKYLER: You came home? Why didn't you tell me?!

ZOE: It was a really short visit. And I didn't want to bother you 'cause I knew you were busy with schoolwork and stuff.

SKYLER: Um, first of all, if you read any of my emails, Facebook updates, or tweets, or looked at my Instagram, you would know that I happen to be very un-busy with schoolwork. Second of all, this "Chandler" must be a very good friend if you brought him home and you were so busy you didn't even have time to call me.

ZOE: Sky-

SKYLER: So you're gonna, like, go hang out in Connecticut for the weekend at some Ivy League guy's house instead of chilling with your real friends? What are you gonna do, play golf? Cricket?

ZOE: Don't be a snob.

SKYLER: I'm not the one going to Connecticut. Where does he live, Greenwich?

ZOE: Westport. His family is having us over for dinner on Friday, then I'm staying for the weekend.

SKYLER: And your parents are letting you do that? I mean, I know my mom wouldn't care -- she might not even notice if l was gone for a whole weekend, and my dad . . . please. But your parents? Letting you stay at a strange boy's house? This guy must be really special.

ZOE: Come on, Skyler.

SKYLER: So you're seriously going to hang out with some book-smart, preppy jock rather than hang out with your best friend?

ZOE: . . . It's not like that.

SKYLER: Zoe, we played in Prospect Park before it was safe. We hung out on Fifth Avenue before there were boutiques.

ZOE: I know, it's just . . .

SKYLER: What, Zoe? Now that you go to an Ivy League school and I go to state college, I'm not good enough for you?

ZOE: No.

SKYLER: But, Chandler's your boyfriend, right? Which you didn't even tell me. And you've known him for what, two months? We've known each other since we were born. I can't believe you didn't tell me!

ZOE: I knew you were going to get mad.

SKYLER: I'm mad 'cause you don't tell me anything anymore.

ZOE: I wanted to wait until the right time.

SKYLER: Like, during the two seconds you have to see me before you go back to Connecticut?

ZOE: I'm sorry, Sky.

SKYLER: You know what? Whatever. It's fine. If that's the way you want to be, that's fine.

ZOE: Sky, look, it's not what you think. I still . . . You're still my best friend.

SKYLER: Why thank you, your Yale-ness. (ZOE gets up.)

ZOE: I have to get home.

SKYLER: I was kidding. God . . . Don't go . . . (ZOE takes a moment, then slowly sits back down.) If you don't want to come to JD's, that's your deal.

ZOE: It's not that I don't want to. I'm just doing something else instead.

SKYLER: Chandler.

ZOE: Skyler!

SKYLER: What! (They stare at each other for a few moments. Then, slowly)

ZOE: . . . What happened in August isn't going to happen again.

SKYLER: What?

ZOE: You know . . . (Long silence.) It's not. Going. To happen. Again . . . Ever.

SKYLER: Whatever, we were drunk.

ZOE: I'm not going to do that again . . . I'm not that kind of person.

SKYLER: And what exactly is "that kind of person"? A person like me? You're saying you're not a person like me?

ZOE: No, Sky, it's . . .

SKYLER: What, Zoe, don't they teach you how to speak full sentences at Yale?

ZOE: Stop it. (SKYLER is quiet. ZOE takes a moment.) We're friends, Skyler.

SKYLER: I know.

ZOE: That's all.

SKYLER: I get it . , . (Beat.) I've been dating a bunch of guys, BTW

ZOE: That's great.

SKYLER: So . . . (Quiet) I have to go. My mom's making vegan chili for tomorrow and I have to chop a million vegetables.

ZOE: That sounds good.

SKYLER: It's vegan chili. (SKYLER gets ready to go. Zoe reaches for her hand.) What?

(ZOE looks pleadingly at Skyler, her eyes begging her to stay) Oh . . . Okay. (SKYLER sits back down) I do really have to go soon, though.

ZOE: Okay.

SKYLER: Okay . . .
```

---

## IC-0686: A Thousand Acres

- Title: A Thousand Acres
- Author (byline): Jane G. Smiley
- Work: Not specified
- Publisher: Anchor
- Publication date as stated: Dec 2003
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ROSE, GINNY
- Teaser before the introduction: No
- Spoken words (computed): 1682
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jane G. Smiley
ISBN: 978-1400033836
Publisher: Anchor
Date (Month/Year): Dec 2003
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Incest is a tragedy of enormous proportions, with repercussions that are often far-reaching.

ACTRESS 2: Children who are sexually abused by a family member rely on creating coping mechanisms in order to survive

ACTRESS 1: As adults, these coping patterns can get in the way of having a full and healthy life.

ACTRESS 2: In A Thousand Acres by Jane G. Smiley, the abuse two sisters lived through as teenagers shadow their adult lives.

ACTRESS 1: Rose, married and now a mother of two girls, has become hard and angry.

ACTRESS 2: Ginny, also married, is stuck in peace-making inertia, perpetually afraid, uncertain and empty.

ACTRESS 1: In this scene, the sisters finally discuss their childhood experiences and come up with a plan to confront their father.

TOGETHER: A Thousand Acres by Jane G. Smiley
```

### Performance text (classify this)

```text
ROSE: Sometimes I hate him. Sometimes waves of hatred just roll through me, and I want him to die, and go to hell and stay there forever, just roasting!

GINNY: Rose!

ROSE: Why are you saying “Rose!” in that shocked way? Because you’re not supposed to wish evil on someone or because you don’t really hate him?

GINNY: I don’t, I really don’t. He’s a bear, but --

ROSE: He’s not a bear. He’s not innocent like that.

GINNY: (raising voice) Last night I told him in no uncertain terms that if he drove drunk again, I’d take the truck keys away from him. He heard me, too. He was looking right at me. I think things’ll improve. He’s hard to live with --

ROSE: Sometimes I hate you too…I hate you because you’re the link between me and him.

GINNY: Who?

ROSE: (throwing up hands in exasperation) Daddy, of course! Don’t be so stupid you’re such a good daughter…so slow to judge, it’s like stupidity. It drives me crazy!

GINNY: (smiling) Just last night, I was thinking the same thing about Ty -- last night.

ROSE: Every time I’ve made up my mind to do something—get off this place, leave Pete, go back to teaching just to earn the money—you stop me. When I was little, I mean really little, three or four, you were like this wall between me and him, but now you’re the path, you don’t keep him out, you show him the way in, every time you’re reasonable, every time you pause to wonder about his point of view. Every time you stop and think! I don’t want to stop and think! (pushes hair back and puts fist on hip, defiant)

GINNY: I’m not like him. I don’t always sympathize with him. But I can’t say I have any faith that he’s going to meet us halfway. I think it’s practical to try and work around him sometimes. Anyway, the point is, yes, you’re right, I’ve let him get away with a lot of stuff. We all have. But we can set rules, and I think the rules can be pretty simple. (Long pause)

ROSE: Ginny? Tell me what you really think about Daddy

GINNY: Well, I don’t know. I love Daddy. But he’s so in the habit of giving orders, no back talk. You know. “I mean, he drinks and everything. I don’t know how that colors things. I’m willing to admit that he’s been drinking a long time, probably as long as we’ve known him. I haven’t really thought about it, but I’m sure if we sat down and worked it out—

ROSE: (stares at her sister)

GINNY: Rose, you’re making me nervous. What do you want me to say? “I mean, Mommy hasn’t been around to tell us what to think of Daddy. I wonder about whether they were happy. Whether she liked him. Or he liked her. Though everybody liked Mommy. I think different things.

ROSE: (clears throat) Shit Ginny, (Ginny laughs; Rose rolls her eyes . . . . long pause) I don’t hate you. I know what I was saying, but I don’t know what it means, exactly. Or how to tell you what it means. Or something. Let’s say the real story here is what you think. He’s a pain in the butt, we divvy up the work. Maybe rules will do the trick. We can try it. United front, right?

GINNY: Right.

ROSE: I used to fantasize that Mommy had escaped and taken an assumed name, and someday she would be back for us. You want to hear the life I had picked out for us?

GINNY: Sure.

ROSE: She was a waitress at the restaurant of a nice hotel, and we lived with her in a Hollywood-style apartment, you know, its own door, two floors, two bedrooms and a bathroom up and living room and kitchen down. Nice shag carpeting, white walls, little sounds from the neighbors on either side, sliding door out to the back deck. There had to be neighbors on both sides. I thought it would be scary to live on the end.

GINNY: I guess I never really thought about not living on the farm. Isn’t that funny? I wanted it to be different, though, in some ways.

ROSE: Ginny you sound so…mild…Aren’t you furious?

GINNY: What good is that? We still have to deal with it. [Daddy’s] always had rages, I admit.

ROSE: Ginny, you don’t remember how he came after us, do you?

GINNY: I remember the shoe incident. I was remembering that when he was yelling at me, the way he made Mommy -

ROSE: I don’t mean when we got strapped or spanked.

GINNY: Came after us?

ROSE: When we were teenagers. How he came into our rooms.

GINNY: (licking lips and fidgeting) We slept together while Mommy was sick.

ROSE: And then, that Christmas, we moved into separate rooms. He said it was time we had separate rooms.

GINNY: Well, of course I remember having separate rooms. I don’t remember why.

ROSE: He went into your room at night.

GINNY: What for? I don’t remember that at all.

ROSE: How can you not remember? You were fifteen years old!

GINNY: I’m sure I was asleep. Grandpa Cook used to prowl around looking at everybody. It was like checking the hogs or something.

ROSE: It wasn’t like checking the hogs with Daddy.

GINNY: What are you saying, Rose?

ROSE: You know.

GINNY: I promise you I don’t know.

ROSE: (Inhales, holds breath, then exhales) He was having sex with you.

GINNY: He was not!

ROSE: I saw him go in! He stayed for a long time!

GINNY: Times always seem longer in the middle of the night. He was probably closing the windows, or something. (concillatory)

ROSE: I checked my clock.

GINNY: Oh, Rose! How am I going to believe that you woke up twenty-one years ago and saw Daddy come into my room and checked your clock and then saw him come out and checked your clock and that constitutes evidence that he was - Anyway Daddy might be a drinker and even a rager, but he goes to church…

ROSE: It’s true. (voice is low, demanding belief) He threatened you. He made sure you wouldn’t tell me. He said if you told me, I’d be really jealous, and wouldn’t like you any more. You were fifteen. You didn’t have much spunk. You believed that.

GINNY: But it didn’t happen.

ROSE: But it did.

GINNY: Well, why don’t I remember? Do you think I’m lying?

ROSE: That’s the way it happened with me. (flat affect)

GINNY: What?

ROSE: Because, after he stopped going in to you, he started coming in to me, and those are the things he said to me, and that’s what we did. We had sex in my bed.

GINNY: You were thirteen!

ROSE: …and fourteen…and fifteen…and sixteen.

GINNY: I don’t believe it!

ROSE: I thought you knew. I thought all these years you and I shared this knowledge, sort of underneath everything else. I thought if after that you could go along and treat him normally the way you do, then it was okay to just put it behind us.

GINNY: What about Caroline?

ROSE: (long pause) I’m not sure. I mean, he told me that if I went along with him, he wouldn’t get interested in her. He presented it as a kind of biological fact. I suspect he never tried anything with her, mostly because she acts like she feels differently toward him than we do. She humors him and sympathizes with him. He doesn’t overwhelm her the way he does us.

GINNY: But he doesn’t overwhelm you! You stand right up to him?

ROSE: He liked that. All those dates and escapes when I was in high school? It made him think he had to subdue me. He liked it.

GINNY: You sound like you were trying to keep him interested!

ROSE: Well, I was afraid he’d try something with Caroline, and she was only eight or ten. But I was flattered, too. I thought that he’d picked me, me, to be his favorite, not you, not her. On the surface, I thought it was okay, that it must be okay if he said it was, since he was the rule maker. He didn’t rape me, Ginny. He seduced me. He said it was okay, that it was good to please him, that he needed it, that I was special. He said he loved me.

GINNY: I can’t listen to this

ROSE: And why I send them to boarding school. Though it gave me a little shiver, having him driving all over, down to Des Moines and everything. I’m not sure the school would prevent them from going out with him.

GINNY: Has he ever . . .

ROSE: Not that I know of. I bought the books, and we went through all the drills and stuff. I prepared them without mentioning Daddy. And I’ve kept my eyes peeled. And we were in our teens.

GINNY: It didn’t happen to me, Rose. I don’t know what to say! This is ridiculous! I mean, the strangest thing is how idiotic I feel, how naïve and foolish. God, I am so sorry he did that.

ROSE: Don’t make me feel sorry for myself. That’s the hardest. The more pissed off I am, the better I feel.

GINNY: Okay. Okay. Okay. I don’t understand Daddy. I just don’t

ROSE: (angry) I understand him perfectly. You’re making it too complicated. It’s as simple as a child’s book. I want, I take, I do.

GINNY: That’s not enough for me. I can’t believe it’s that simple. We’re his children!

ROSE: I’m telling you, if you try to understand, it just holds you back. You start seeing things from his point of view and you’re just paralyzed. That was his goddamed hold over me, Ginny! For all those years! He talked. He made me see things from his point of view! He needed someone! He needed me! He loved me. Ginny, you don’t want to understand it, or imagine it. You don’t . . . you don’t . . . you don’t.

GINNY: We’ve got to talk to him about it . . . .

ROSE: He won’t get away with it, Ginny. I won’t let him get away with it. I just won’t. I know that his face is a black ocean and there’s always, always, always the temptation to drown in that ocean, to just give yourself up and sink. You’ve got to stare back. You’ve got to remind yourself what he is, what he does, what he did. We have to stand up to that. Until there’s true remorse. Nothing will be right until there’s that. He’s got to repent and feel humiliation and regret. I won’t be satisfied until he knows what he is.
```

---

## IC-0687: Train Story

- Title: Train Story
- Author (byline): Adam Rapp
- Work: The Best American Short Plays 2000-2001
- Publisher: Applause Theatre Books
- Publication date as stated: 2002
- Event as filed: Duo Interpretation
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

## IC-0688: The Trojan Women

- Title: The Trojan Women
- Author (byline): Robert Patrick
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Sept 2004
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: HECUBA, COMMON WOMAN, WOMAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1884
- Already set (do not supply): none

### Source block (context only)

```text
Author: Robert Patrick Book: Polyphony Magazine (On-line publication)
ISBN: N/A Publisher: Polyphony Magazine
Date(Month/Year): Sept 2004
NOTE FROM THE AUTHOR: This entire play is available by e-mailing me at
rbrtptrck@aol.com with the words "Trojan Women" in the title line.
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Trojan Women by Euripides is one of the greatest tragedies ever written. Hecuba, The Queen of Troy has lost her country, her husband, her children, and now must watch what is left of her countrywomen be handed out to the victorious Greeks as trophies of war. She herself is to be the slave of the conquering Greek ruler, King Odysseus.

ACTRESS 2: An adaptation of Euripies’ The Trojan Women by Robert Patrick
```

### Performance text (classify this)

```text
HECUBA: What can we take on trust in this uncertain life? Happiness, greatness, pride - nothing is secure, nothing keeps.

Setting: A beach outside of Troy. Early dawn. HECUBA, old and in the rags of royal sleepwear, lies face-down on the ground.

HECUBA: Arise, you wretch, at least upon your knees.
[RISES to kneeling position]
Look, you've left an impression on the earth,
a hollow Hecuba like you've become,
an empty image of lost royalty
the full, foul tide of dawn will wash away.
And what is it that greets your ancient eyes
on this first dawn of peace in ten long years?
One thought the age of miracles was past
but the sun seems to be rising in the West
as if the whorish world has turned in bed
to show her face to her victorious Greeks.
Enough, you've lost your wits, now lose your wit.
That line of fire upon the Western strand
is not sunrise, but torches borne by Greeks
all borne to burn the unmanned towers of Troy.

There, Hecuba, you hear? It can be said.
The towers of Troy stand hollow as old bones.
Now, shall I wail upon this wet salt shore,
or shall I moan against the whipping wind?
Or shall I mourn the corpses in the doors
about to burst and send their sizzling blood
across the stones of undefeated Troy?
Troy! Keeper of the gate from East to West,
whom Asia and whom Europe tribute paid.
Troy with her worldly wit and her wide walls
Which held till last night's onslaught. Here come tears,
to crawl triumphant down my stonelike face,
then steam in that chilled wind that beats the sails
of those Greek ships! Look, women, how they swell,
tugging against their masts, mad to inhale
unhallowed dead men roasting on our stones!
Oh, eager ships! How shall Greeks hold you back
for long enough to load slave women on?
The treasury of Troy is not enough,
not rich enough to hold their bellies down.
They rear up in the harbor, ships in rut!
Hold, hold. Your captains will be coming soon
to winnow out us women, and each claim
his horde of Trojan women, Trojan whores,
old widows, orphans, drudges, Trojan slaves,
no sons nor husbands, but sufficient wives
to weight you in this blood-tinged bay, and hold
you steady as you turn to canter home
on tides of undefended women's tears!
Why do I kneel before this sacrilege?
Why lift my corpse up high enough to kneel
on shattered shells of sea-beasts whose lives end
to cut the knees of women where they wail?
Fall, Hecuba, fall down face down to fit
in that cold hollow mold of Hecuba
you can hide in again. Lie down and die ...
But why? Why not use now to learn to kneel?

COMMON WOMAN: [ENTERS, sees Hecuba]
Your majesty! What are you doing here?
I searched for you in all the women's huts.
We woke to find you, woke to find you gone.
She's here! She's here! Come now, rise from the sand.
Oh, let me help you with my common hands.
Dread rumor had you dead, drowned in the sea,
dashed down the cliffs, drained pale by some Greek blade,
or even fallen to base suicide,
strangled by your own hair, or monstrously
coring your heart out with a smuggled sword.
Come, rise, come back, come in, and let them see
who huddle in their rags alone, afraid,
Queen Hecuba's alive and well today!

HECUBA: I? Stand up like a doddering flagpole
stripped of its banner? I like a scarecrow
to frighten cawing, vulturous Greeks away?
No, you kneel, too, kneel down and tell them all
to grovel, fall, and kneel. No, do not kneel.
How dare you kneel to me? What do I rule?
Those ruins where flames send fat rats scuttling now
from interrupted nightlong greasy feasts?
No, I command you, do not kneel to me.
But let me kneel where there is yielding sand
to beat with these hard hands while I intone:
"I am a widow that was last night a wife!
Childless that was the dam of a royal line!
Captive insane upon this frigid beach
that was at sunset mistress of warm halls.
And I am a pitiful slave without a name,
Queen yesternight of all-unrivalled Troy."
Oh, women, count no man happy till he's dead.

WOMAN: Oh, Hecuba, great queen, great lady, great,
great mother of great men, you should be proud.
You must be proud enough to shame us all.
For this ten years against a plague of Greeks,
wisest of warriors, your husband, Priam,
stern Hector and glad Paris, your tall sons,
led my meek husband and all Trojan men
to stand against a siege more formidable
than any ever seen by war-worn Earth.
Why, legends till Earth's unimaginable end
will swear that Priam's men were the most valiant,
heroic men that ever stood at arms.
We would be worthy of them, but we need
you standing as our guide, as Priam stood
staunch and unyielding when his men would sway.
What will your weak, dependent women say
to see you humbled on your knees this way?

HECUBA: What will the women say if they are wise?
If they are wise, they'll say, "Bear no more sons.
Let Mother Earth bear what she thinks is wise,
but I will bear no soldiering men today!"
This they would say if they were ever wise,
but they are not wise, and cheer waste-laying men.
What will the women say if they are strong?
If they are strong, they'll say, "Give me a blade,
give me a rope, give me a poison's gall
to scald my guts that I might die in pain
before I let a man pump seed in me
to make more women that must bear such woes."
This they would say if they were ever strong,
but they are weak, and soon upon the decks
of those tossed ships they'll tumble under Greeks
and treasonable wombs will gulp Greek seed,
ovens to bake men to make women mourn.

WOMAN: Anguish has maddened you, when most we want
your sovereign wisdom and most royal command.
Oh, God Apollo, her great strength restore.
Olympian healer, in your halcyon sphere,
look to this suffering Earth.

HECUBA: Look to the sky!
Look, Lord Apollo rises in his East,
thrusting his arms through early coils of smoke
and pioneering vultures. Oh, surely now
our Troy will resurrect, like a shamming boy,
playing dead, and all its bones and stones,
billow and tug together to be Troy?
What, no? Not yet? No miracle? Come, God,
vanquish the heathen. Reward this woman's faith.
Blind, burn our foes, blaze back the Greeks, great god!
No, it's the Trojan women you make mad,
Queen Hecuba mad to think Troy is in ruins,
this woman mad to think herself a slave,
her husband gone, her starving queen alone,
screeching among the seaweed on her knees.

WOMAN: Now blasphemy issues from you like the rank
discharge down madmen's chins. Gods, is our goddess
overthrown? Weep, women, in your huts,
weep for yourselves, weep for the waste of Troy!

HECUBA: No, not of Troy, but Greeks, my daughter, Greeks!
There are no Trojan women anymore.
In our men's blood, we were re-christened Greeks!
I have not even subject daughters now
to take the place of those I gave to Priam,
for I, that mothered Troy, cannot say this:
"Daughter, you may not take that man to bed
and be his wife," or, "Yes, my blessing, go;
follow him to his bed and bear him sons."
These Greeks, when Troy is gutted of its gold,
will come for you, pitch dice, draw lots, make riddles,
and whichever one has won you take you off
to ravish on the waves, or even here,
haul you from line and have you in my sight,
and in the sight of all these wailing women,
kiss you with mouths that called your husbands dogs.

WOMAN: That I, a common woman of great Troy
who thought it blessing twice in a good year
to glimpse you in a festival parade,
gorgeous with flowers in bejeweled state,
or watch you waving from your balcony,
authority's icon, Hellespont's gilded queen,
should come so close to hear you curse and scathe
the god that guarded us for war's decade,
the husband king that held the beasts at bay,
your valiant sons as warlike, and denounce
even the living memory of tall Troy,
drawing in smoky swirls such hideous pictures
of our near future to make hope drop from me
like an aborted child. Is there no hope?

HECUBA: None.

WOMAN: Is there no promise?

HECUBA: No.

WOMAN: No dream?

HECUBA: Bad dreams, or good ones that seem horrible
when you wake, reeking sluts on mats of straw,
hobbling with chained feet to make a meal
for the pig that fell on you the night before.

WOMAN: Women of Troy, come and be counted now,
concubine cattle, by right of wanton war.
Stagger, weeping, from corrals of bondage,
trembling, shove aside the ragged skin
that makes your prison's door. Set naked feet
carefully on sharp stones and broken weapons,
hungry and shivering, women of Troy, in line,
stand, gaze, and see the mistress of your minds,
a ravening mad dog whom we have adored:
Hecuba, queen of Priam, star of souls
she whom we aped and studied, longed to be,
whose veriest gown or ornament imitate,
Hecuba who set fashions for each season
and whose full life was model for us all,
again, as she did always, showing us
what we must next become. Come, Trojan women,
shaking like aspens, with blank eyes, and necks
scarcely strong to hold your heads upright,
master yourself to bow to your queen's will.
Her will is that we utterly submit
to fate that seemed impossible last night.
Pay her the homage due the rightful queen,
and fall in hopeless bitterness in these weeds.

HECUBA: Oh, daughters still, the only ones I have,
see that I do what I can do for you.
What can I do but shake you like bad girls,
and say, "Give up those frivolous, foolish dreams
that you were once dear daughters, mothers, wives,
daydreaming girls with suitors for your hands,
obedient girls with fathers you purred to please,
spirited girls whose mothers spanked your hands,
yet smiled remembering their mothers spanking theirs.
You're nothing now. Believe you never were.
Life till last night was dreamed. Wake up to fate.
Life is a punishment. Life was always grim.
Love was a lie, freedom a fable for slaves.
Nothing is yours. Nothing was ever yours.
You stand alone, the helpless slaves of whims
indomitable as weather and old age.
Greeks are not men, will not be men to you,
are sun and rain, volcano, tidal wave,
nothing you can control. Your are not women,
but toads and monkeys fleeing fits of gods.
That's the best good that I can do for you.
Be grateful to be chained with your baby girls
if needed still to nurse them like a sow
or grateful if they separate you from them,
so not to see them bred to bleeding shame.
For everything, be grateful, and for death--
if it comes quickly--gratefullest of all.
You see I set new fashions for our fall.
```

---

## IC-0689: Twisted Sister

- Title: Twisted Sister
- Author (byline): Lora Lee Cliff and Janet Wilson
- Work: Play it Again (ed. Norman Bert)
- Publisher: Meriwether Publishing
- Publication date as stated: March 1993
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: SR. CHERYL, DR. BLANK
- Teaser before the introduction: No
- Spoken words (computed): 1349
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lora Lee Cliff and Janet Wilson
Book: Play it Again (ed. Norman Bert)
ISBN: 978-0916260972
Publisher: Meriwether Publishing
Date (Month/Year): March 1993
```

### Introduction (context only: never use it for content warnings)

```text
DR. BLANK: Therapy is often a place where one’s “true self” can come out.

SR. CHERYL: Or should we say…”true SELVES?”

DR. BLANK: A nun gives her therapist insight into areas of her life even she isn’t aware of.

SR. CHERYL: and a doctor hears every side of the story in…

BOTH: “Twisted Sister”

DR. BLANK: By Lora Lee Cliff and Janet Wilson.
```

### Performance text (classify this)

```text
*NOTE Dr. Blank can be played by either a man or woman

(SR. CHERYL is lying on the couch clutching her purse while DR. BLANK is sitting in an easy chair. He blows the whistle.)

SR. CHERYL: (As her thirteen-year-old self) I'm thirteen and I just got my period. I've been crabby all day and didn't know why and boom my period started, first time. I thought God was punishing me for being crabby...

DR. BLANK: Go on, Sr. Cheryl.

SR. CHERYL: (Sitting up and coming out of "character") Dr. Blank, all I need is a little help sleeping. If you would just write me another prescription ...

DR. BLANK: Go on with your dream.

SR. CHERYL: All right. (Laying back on the sofa. DR. BLANK blows whistle. As her thirteen-year-old self) I'm walking home from school and I just gotta have some candy it's all I can think about. (Jumping up and looking in the "candy store window") Then I'm at the candy store and I see the butterscotch, and the chocolate-covered cherries. And then I see the chocolate mints and the chocolate creams! And I get really upset because then I don't know which I want more. And the lady's getting mad 'cause I'm taking a long time to decide. Anyway, I look up and there's Daddy and he smiles at me. Then, all of a sudden, he gets this weird look on his face and falls down. (Running to the "door '') So I run over to the door and it's locked I don't know how it got locked and I keep trying it and then I (Running back to the "window'') run back over to the window to see Daddy - and, and, and - he's laying on the ground and (Running back to the "door ") I run back to the door to try to get out and I'm screaming and kicking at the door (Coming out of "character ") and that's it.

DR. BLANK: It's great! It's a terrific dream because of all the symbolism - crabby and getting your period. I get this image of crabs. What a marvelous metaphor. I would love to work on this. Now, all you have to do is play out the different characters...

SR. CHERYL: What?

DR. BLANK: See, Sr. Cheryl, each character in your dream is an aspect of your personality - now, through exploring and tying up the fragmented selves ...

SR. CHERYL: (Jumping up and heading for the door) You're not going to tie me up! Why, Mother Superior ...

DR. BLANK: (Intercepting her at the door with his hands up) Oh no, no, no! Metaphorically speaking, metaphorically speaking! Oh hell, Sr. Cheryl, it's fun! Come on - you'll feel better. Why don't we start with your father. Now, you're outside the candy store. What are you doing there? (Blows whistle.)

SR. CHERYL: I don't know about this.

DR. BLANK: Yes you do, Sister. (Blows whistle again.)

SR. CHERYL: (As "Daddy," pacing back and forth) Whew! I gotta have a break. Too much going on - the pressure! I need a drink, but Thelma won't like it. That Thelma - whoa! Guess I'll just have some candy. (Dropping the "character ") Is that what you mean?

DR. BLANK: Yes. Yes. Go on. Who do you see in the candy store?(Blows whistle.)

SR. CHERYL: (As "Daddy") Hi there, Cheryl! Isn't that funny? She looks kind of happy to see me. Come on, I'll buy you a Coke.

DR. BLANK: You seem very fond of her.

SR. CHERYL: (As "Daddy") Yeah. When she was a little girl, I used to hold her, read to her...

DR. BLANK: And now?

SR. CHERYL: (As "Daddy") I'm a very busy man. I don't have time for... Come on, Cheryl - now! (Suddenly stricken with chest pains) God, I don't feel well. Must have been that lousy goose liver I had for lunch. Cheryl, come on out here - you gotta call Mother.

DR. BLANK: Are you having a heart attack?

SR. CHERYL: (As "Daddy') I don't know! Would you just call my office?

DR. BLANK: I think we should call an ambulance.

SR. CHERYL: (As "Daddy") No, I'm fine.

DR. BLANK: You don't look fine.

SR. CHERYL: (As "Daddy') I told you to call my office.

DR. BLANK: Boy, you're stubborn, aren't you?

SR. CHERYL: (As "Daddy') I'm not stubborn. Where the hell is Cheryl?

DR. BLANK: She can't open the door. She's struggling with it.

SR. CHERYL: (As "Daddy') What's so hard about a little door? She had to open it to get in.

DR. BLANK: Can't you see she's trying?

SR. CHERYL: (As "Daddy") Just shut up and don't get into my business.

DR. BLANK: How dare you talk to me like that! What makes you so angry?

SR. CHERYL: (As "Daddy") For Christ's sake, what's a little door? These girls - just like their mother - can't do anything without throwing these little fits. Oh - don't start crying like that. Always crying, that one.

DR. BLANK: Aha! So it's her crying that pisses you off!

SR. CHERYL: (Coming out of "character") C'mon, Dr. Blank. You call this fun?

DR. BLANK: How insightful! The internalized father is incapable of taking in your feminine self thereby causing a polarization between your masculine and feminine selves.

SR. CHERYL: Forget it! Now just give me my prescription ...

DR. BLANK: (Starts whistling "The Candy Man" and starts a "soft shoe" dance.) I want to go back to the candy store - back to the sweetness. Now I want you to play one of the chocolates. (He is about to blow his whistle but SR. CHERYL stops him.)

SR. CHERYL: No. I'll be a peppermint patty 'cause that's the best. (DR. BLANK blows whistle. SR. CHERYL as the "patty" jumping on the arm of the couch, crossing her legs and imitating Mae West; she "strips" off her sweater as she speaks.) On top of my melt-in-your-little-mouth chocolate, I have a flashy, shimmery, silvery paper wrapping. Shows you what a good taste I'll be. And over that one, there's a little cellophane wrap to make me very secure and never stale, you know, reliable every time.

DR. BLANK: Do you think you can do anything for Cheryl?

SR. CHERYL: (As "patty") Of course, honey - mmmm ... she's gonna love me. (As "patty" to SR. CHERYL) Hi there! Oh, you don't feel good, do you? Well, I'll fix that. Listen, I am so good. Now, undo my cellophane - OK, take away my silver lining - see, I'm all chocolate. Take a bite - the first time is great - that's it. See, I'm a little hard on the outside - ooh, surprise - I'm all white inside - that squishy, gooey, marshmallow - real, real moist...

DR. BLANK: Ahhh... fascinating ... the pieces of the subconscious are falling into place. There's a real paradox here. On the one extreme, there's this helpless child unable to accomplish a simple task, and then there's the adolescent's smoldering sexuality about to explode. I want to talk to your mother now. She's not exactly in the dream, but I want to talk to her anyway. Sit over here. Thelma, how do you feel about Cheryl growing up? (Blows whistle.)

SR. CHERYL: (As "Mama" putting her sweater back on and buttoning it) I do not look forward to having another teenage daughter. She's my favorite, but ... I told her when she was six, I said, "You were a lot nicer when you were three." And it's just gone on that way.

DR. BLANK: How does this change her relationship with her father?

SR. CHERYL: (As "Mama ") Her father's uncomfortable about things like this - emotional things. I'll be able to handle her. She'll come to me like she always does.

DR. BLANK: So she'd rather come to you than to Daddy – I mean to her father?

SR. CHERYL: (As "Mama '') Oh heavens, yes. Her father thinks a period is a punctuation mark. They're not close.

DR. BLANK: Does Cheryl miss that?

SR. CHERYL: (As "Mama '') Oh no. I don't think it fazes her.

DR. BLANK: Are you sure about that, Thelma?

SR. CHERYL: (As "Mama '') Yes! Cheryl's father works hard. He's a good provider. And I see to it that his time at home is spent with me.

DR. BLANK: You are a selfish woman.

SR. CHERYL: (As "Mama '') You can't talk to me like that!

DR. BLANK: OK. Change places and be Cheryl. (He attempts to blow the whistle but "Mama" stops him.)

SR. CHERYL: (As "Mama '') Wait just a minute! I'm not finished yet!

DR. BLANK: (Blows his whistle and points to the sofa; "Mama" refuses to budge; DR. BLANK blows several short sharp blows on his whistle and SR. CHERYL complies.) Now Cheryl- is it true what your mother said?

SR. CHERYL: No! Mama won't let me know Daddy 'cause she wants me to be her girl.

DR. BLANK: (Pointing to where "Mama" is sitting) Tell your mother that.

SR. CHERYL: No! I'm not telling her anything. (Standing up and holding out her hand for the prescription) Just give me my prescription and let me go!

DR. BLANK: I'm offering you this creative process in order for you to discover who you really are, and all you want is more pills. I'm so disappointed! Come on, Sr. Cheryl. You can play Mama again. (SR. CHERYL resumes her "Mama" position.) You seem a little upset. (Blows whistle.)

SR. CHERYL: (As "Mama '') What else can a mother do? What can a mother do? The sacrifices I have made for her. Her sisters did not get the dancing lessons. They did not get a lot of the things she did. She can just go off with her father - be his girl and leave me alone.

DR. BLANK: What are you feeling right now?

SR. CHERYL: (As "Mama") Betrayed. The last of my three blessings has betrayed me.

DR. BLANK: The missing link - betrayal. The fact that you're wanting to separate from the symbiotic relationship, but she just won't let you!

SR. CHERYL: (As "Mama") What are you talking about?! (Grabbing her purse and beating DR. BLANK with it) Just who do you think you are?

DR. BLANK: (Blocking her blows with his arms) I think we've done enough for one session, Sr. Cheryl.

SR. CHERYL: (As "Mama," still beating him) You have a lot of nerve sticking your nose in where it doesn't belong!

DR. BLANK: (Still defending himself) The session is over! (He blows his whistle.)

SR. CHERYL: (Ignoring the whistle, "Mama" yanks the whistle out of his mouth and tries to cram it down his throat.) All my daughter wants is a few lousy pills so she can sleep at night. (DR. BLANK searches for his prescription pad.) Is that asking too much? But no! You have to go dragging me into this! Why is it always the mother's fault? And I wasn't even in her damn dream...

DR. BLANK: (Quickly writing her a prescription) Here it is! (Fearfully hands it to "Mama.")

SR. CHERYL: (As "Mama," snaps it out of his hand.) I'll give this to Cheryl and I'll be back for more!

DR. BLANK: Yes, yes, next week. (As "Mama" exits, DR. BLANK throws himself on the couch.)
```

---

## IC-0690: United Front

- Title: United Front
- Author (byline): Barbara Lhota and Ira Brodsky
- Work: Forensics Duo Series Volume 4; Pgs 289-297
- Publisher: Smith and Kraus
- Publication date as stated: Nov 2005
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MIMI, ELIZABETH
- Teaser before the introduction: Yes
- Spoken words (computed): 1874
- Already set (do not supply): none

### Source block (context only)

```text
Author: Barbara Lhota and Ira Brodsky
Book: Forensics Duo Series Volume 4; Pgs 289-297
ISBN: 978-1575254074
Publisher: Smith and Kraus
Date (Month/Year): Nov 2005
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Families like to believe that love is enough. That blood makes loyalty simple. That if you show up for the holidays, smile for the pictures, and agree not to talk about certain things, everything will hold together.

ACTRESS 2: But sometimes love turns into silence.

ACTRESS 1: And silence becomes survival.

ACTRESS 2: In this selection two sisters are desperately trying to come to terms with what family really means when addiction, memory, and denial refuse to stay buried.

ACTRESS 1: One sister believes in boundaries.

ACTRESS 2: The other just wants to hold everyone together.

ACTRESS 1: What begins as small talk quickly unravels into memories of shared trauma and a truth that can no longer be ignored.

TOGETHER: United Front by Barbara Lhota and Ira Brodsky
```

### Performance text (classify this)

```text
(Pgs 289-297) ELIZABETH: (Mimi flips the pages of a photo album for Elizabeth) Very nice. (Pause, flip) Uh huh, cute. (Flip) Nice.

MIMI: Isn't he beautiful? Honestly, isn't he just the cutest, most adorable thing?

ELIZABETH: (Looking at the photo) What's he doing in this one?

MIMI: Ah, licking the wall.

ELIZABETH: Now that's cute!

MIMI: I told him to stop, but something about Manchester white sends his taste buds soaring. You feel I've misrepresented my dog?

ELIZABETH: Well, he's your first. You're allowed to brag. That's what mothers do. Make their little ones out to be what they're not.

MIMI: Is that what mothers do?

ELIZABETH: I don't know. Who knows what mothers do? (Continues to look through photographs, beat) What is this!?

MIMI: Oh God. Sorry. I forgot. Don't be upset. Please.

ELIZABETH: Why shouldn't I be?

MIMI: Look, I know that we made a deal. But I'm not strong like you. It was Halloween, and I wanted to see Mom. (Elizabeth smirks) You know how she loves the holidays. She had those pumpkin lanterns out. Unfortunately, she tripped over one. Spent the rest of the evening on the couch.

ELIZABETH: With Dad bringing her one Tom Collins after another.

MIMI: It was the holiday. Everybody drinks a little on a holiday. It was fun, actually. Remember how you and Harry and Mom tried to haunt my room? (Reaching up. Putting on her brother's spooky voice) "I call upon the spirits of those people who have gone before us. Those voices who we need to hear now, in this room, so desperately. Come into our room, spirit of Chief Crazy Horse, come John F. Kennedy, come William Shakespeare and Jane Austen!”

ELIZABETH: Come Dasher, Dancer, Comet, and Vixen. (They laugh)

MIMI: She was so mad at you. She said you always ruined everybody's fun. She says you were always too grown up.

ELIZABETH: Someone had to be. (Pause) You know, I haven't talked to Harry since he moved back home. How is he?

MIMI: He's fine. He still hasn't found a job.

ELIZABETH: Of course not. He's divorced, living at home with parents, why would he get a job? I don't have any patience left. If he wants to return to the gin-soaked womb, that's fine. And if you want to watch her drink on Halloween, that's fine too. But I'm not enabling anymore.

MIMI: We're not enabling. We're just visiting our folks. And you might as well know Scott was there, too.

ELIZABETH: Great. One big unhappy family! So much for a united front, huh?

MIMI: Come on, Elizabeth. Don't be mad. We just decided it takes more energy to not go.

ELIZABETH: You are cowards!

MIMI: She knows you've got a point about her issues. She does and she's trying. Look, she's dealing with Gram's death right now.

ELIZABETH: And we aren't dealing with our grandmother's death? There's always something, Mimi. That's no excuse. The dog dies, they raised the taxes, Dad's business isn't doing well-all are excuses that I've heard a million times.

MIMI: I know you don't trust it, Elizabeth, but she's working on it this time.

ELIZABETH: How? Is she in therapy? Has she joined AA?

MIMI: No, but-

ELIZABETH: So there's nothing except the usual empty promises and the usual slight reduction of drinking followed by the usual let's-ignore-the-ten-ton-alcoholic-snoozing in the middle of the living room.

MIMI: Look, I know. But Thanksgiving is coming up. Can you just give it a break for one night, please? We're all going to be there.

ELIZABETH: I'm disgusted.

MIMI: I know, but can't you just pretend? Be like Scott. He keeps himself far away physically and emotionally, except for a few measly holidays. Then he sacrifices himself for one day and then he leaves.

ELIZABETH: For him it's the path of least resistance. Another way to keep the status quo. That is the one thing I won't do anymore.

MIMI: What's with you? Just because you've made a decision about visiting Mom, we can't visit her?

ELIZABETH: I never said that! I asked you guys if you wanted to be a united front on all this and you all said yes. I asked you! If you said no, that would have been fine too. I would have told you that my personal decision is to remove myself from the family drama. The rest of you can do as you please. I just wish you all didn't lie and pretend.

MIMI: Well, it felt like if we didn't follow your plan, that you'd drop us too. (Beat) It just feels weird at home without you. You know, no matter what, she's always our mother.

ELIZABETH: Other than the title, our mom was rarely motherly in any way.

MIMI: Well, the whole thing puts Dad in a painful position too.

ELIZABETH: He chose it! It's painful to see Dad suffer, but the fact is, does he do anything to change it?

MIMI: What is he supposed to do, Elizabeth? Leave her? She wouldn't survive!

ELIZABETH: Oh my God! Can't you see? That's exactly what she wants you to think. She wouldn't die. She's a lot tougher than any of you give her credit for. It's the rest of us I don't think would make it. We have a terrible record thus far. Three out of four children have nearly died as a result of her.

MIMI: Three out of four? What do you mean? OK, I know you had that really bad time in high school. But it wasn't just about Mom. [And] you can't exactly blame Harry's situation on Mom. I mean, he has a horrible marriage and a cheating wife --

ELIZABETH: Who bears a striking resemblance to Mom in every way.

MIMI: Well, who's the third? Scott never did anything like that.

ELIZABETH: Forget it. The point is, she's plenty strong. Anybody who drinks as much as her has to be strong.

MIMI: (Beat) Mom's been telling me a lot more about her life.

ELIZABETH: I know her life has been sad. I've heard it all. I've been her shoulder far longer than you have. And I appreciate that she had a difficult life. But look at all of us.

MIMI: It wasn't as bad as hers though.

ELIZABETH: How do you measure that? Did you ever invite friends over after school? Kids do that. How [about] the day Harry had to coax Mom down from Mrs. Flowers' balcony? Or the day Mom broke the bottle and then walked right through the glass.

MIMI: Those are extreme. It wasn't the day-to-day.

ELIZABETH: It was day-to-day for us to cook our own meals and tuck her into bed late afternoon. They do sad movies about kids like us. I'd say we're pretty sad. Unconfident. Slow to make decisions. Did any of us ever have a boyfriend or girlfriend in high school? You don't even date now.

MIMI: I'm too busy.

ELIZABETH: Sure. And Scott? Who's never had a girlfriend in his life? And poor Harry. He leaves one alcoholic to marry another one. And now he's right back where he started-pathetic, poor, unemployed, and watching soaps while Mom drinks.

MIMI: You are so damn negative.

ELIZABETH: I have so damn much to be negative about. And while I can't do anything about the childhood I had or the mother we all had, I sure as hell don't have to pretend that everything's hunky-dory. That's where I'm drawing the line. I mean as kids we couldn't help being used by her: as her therapist, her caretaker, her nurse, her maid. But I'm not going to go on doing it for the rest of her life!

MIMI: I know, I know! But you just get so mad! It's hard to talk to you.

ELIZABETH: Well, why don't you get mad?! All of you! You all know I'm right!

MIMI: I don't know what I feel. To tell you the truth, all I feel is angry at you because I don't think your plan is going to change a damn thing. All it does is make her even more upset and drink more.

ELIZABETH: And that's my fault now?

MIMI: No! I didn't say that. I just think it's selfish to make all of us suffer because Mom drinks too much. So now I don't get to see you either?!

ELIZABETH: Selfish? This is incredible. Now I'm the bad guy?

MIMI: No one's the bad guy! I just want us to all be together! That's all! And I don't think it's such a big deal to just come to Boston for a few hours. Just for the holiday. (Beat) I talked to her last night. She knows you're right.

ELIZABETH: Did she ask you questions? Did you feel protected and safe like a mother should make you feel? Or did she just cry on your shoulder about horrible me?

MIMI: No, she was trying to explain why she's the way she is.

ELIZABETH: So she never asked you one damn thing about you? How you felt?

MIMI: Well ...

ELIZABETH: Of course not. There's never enough time for you, right? Don't you understand? She's playing you! I'm not following the plan! So she enlists all her little soldiers.

MIMI: I think she wants to patch things up with you.

ELIZABETH: She's out of her mind. When she makes the first move to do something about her drinking, that's when I'll come to see her and help her.

MIMI: Come on, Elizabeth! I don't see why it's that big of a deal?!

ELIZABETH: You're the third.

MIMI: What?

ELIZABETH: Three out of the four of us kids. You're the third.

MIMI: What? I never tried to ... hurt myself.

ELIZABETH: I didn't say they were all suicide attempts.

MIMI: I don't know what you're talking about!

ELIZABETH: That's because you were a baby. We never told you. Mom asked us not to. (Beat) She passed out while you were in the tub. The water was still running. You weren't even two yet. We were out playing in the backyard and Scott came in to use the bathroom. When he saw your face under the water, he started screaming. He was only five. Harry and I came running. Harry pulled you out while I woke Mom up. Thank God she got up because you weren't breathing. She pushed the water out of your stomach. She was afraid she broke your ribs, she pushed so hard. She breathed air into your lungs a bunch of times and she kept sayin over and over, "Jesus, God, Jesus, God! Help me God!" It was the most terrifying few minutes of my life. And then suddenly, out of nowhere, you breathed. My legs were shaking. Mom asked us all not to tell anyone. So we didn't. Ever. We all kept our promise, until now, I guess. But I don't think any of us trusted her alone with you again, when you were little. (Beat) And mom has never apologized for that event to any of us. So, yes, I do think it's a big deal to go to her house for Thanksgiving or any day until she quits. I won't fall in line. I won't pretend we were just some big happy family again. I can't.

MIMI: I don't know what to say. I can't believe this.

ELIZABETH: Ask Harry and Scott if you'd like, but you know I'd never make up a story like that. (Mimi looks at her sister) I was so afraid we lost you. (hugs Mimi, long beat) I don't hate Mom. I love her. I know she didn't mean to hurt you, to hurt any of us, but she won't get well if we let things be as they have been. All I can do is to keep screaming at all of you until one day, one of you hears me.

MIMI: (Quietly) I hear you. (Elizabeth doesn't believe Mimi's response) I mean it. I hear you. I do. (Pause. They hug)
```

---

## IC-0691: The Wasp

- Title: The Wasp
- Author (byline): Morgan Lloyd Malcolm
- Work: Not specified
- Publisher: Oberon Books
- Publication date as stated: Sept 2015
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: HEATHER, CARLA
- Teaser before the introduction: Yes
- Spoken words (computed): 1470
- Already set (do not supply): none

### Source block (context only)

```text
Author: Morgan Lloyd Malcolm
ISBN: 978-1783198603
Publisher: Oberon Books
Date (Month/Year): Sept 2015
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Author Lewis B Smedes once said, “The problem with revenge is that it never evens the score. It ties both the injured and the injurer to an escalator of pain.“

ACTRESS 2: There is no doubt that revenge is a powerful emotional urge that triggers some people into action.

ACTRESS 1: People who have been hurt believe that if the wrong-doer suffers, they will feel better.

ACTRESS 2: That their emotional pain will diminish.

ACTRESS 1: But in reality, is this true? We’ll leave that for you to decide.

TOGETHER: The Wasp by Morgan Lloyd Malcolm.
```

### Performance text (classify this)

```text
A café – outside smoking courtyard. Carla, in her early thirties and pregnant is smoking. She fiddles nervously with her phone. Heather, also early thirties, emerges from the café. This meeting is awkward – The last time the women saw each other, Carla and her clique were the school bullies to a very ostracized Heather. But times have changed. Heather is obviously upper-class, while Carla hasn’t changed much since high school.

HEATHER: (Pg 9-12) Carla? I’m so sorry! I didn’t realize there was this bit out here. I’ve been in there all this time.

CARLA: (exhales cigarette smoke) I got here early.

HEATHER: (awkward pause as Heather realizes that Carla is pregnant) Wow. Well. Look at us! You haven’t changed a bit. Well. Other than . . . when are you due?

CARLA: Couple of months. Thanks. What happened to the glasses?

HEATHER: Oh, long gone! As soon as I went to uni I realized I spent years looking like a complete idiot. No wonder you found it so funny.

CARLA: Yeh, well. I’m not like that no more. Cos if it were years ago, then there’s no way I’d be seen dead with you, right? (Carla laughs and Heather joins in uncomfortably)

HEATHER: Well. What have you been doing since we last saw each other? You have kids now don’t you?

CARLA: Yeh. Four. (feigning interest) What about you? (lights another cigarette)

HEATHER: No. But I’d like to. (Pg 14) My husband, [Simon], and I have been trying for about four years now . . .

CARLA: (Pg 15) Do you want this one? (laughing, but with an undertone of seriousness; Heather reacts, aghast. Carla has had enough of the chit-chat and her tone changes harshly) (Pg 14) Look, why did you want to meet?

HEATHER: (Heather is flustered, she stammers nervously) Sorry. . . Perhaps I should start at the beginning.

CARLA: Yeh that would help. (Pg 23-24) Why the hell am I here?!

HEATHER: The pigeon . . . in the fields out back of the school. That pigeon with the broken wing. You didn’t just break its neck. Did you? Nope. You wanted to pluck it first, Snap its feet off. Take its eyes out with a stick.

CARLA: I’m going (She rises to leave and Heather stops her)

HEATHER: I want you to kill Simon.

CARLA: What?!

CARLA: What?!

HEATHER: (Pg 18) He’s been emailing another woman. It started about two years ago. Just flirty chats. Silly stuff. (Pg 20) I was paranoid he was cheating on me, so I made a fake Facebook profile and messaged him. . . He messaged back.

CARLA: Crafty. I love it! (she chuckles, enjoying the story)

HEATHER: (Pg 18) He started telling her things about us. About me. How he wasn’t finding me attractive anymore. Horrible things. (Pg 24) I’ve had enough. I want him gone. Completely. And you’re the only person I know who can do it. Kill him. Kill Simon. I want him dead. (deep breath) You’ve done it before.

CARLA: To a pigeon! A pigeon! What’s wrong with you?! (Stands to leave, Heather rises also)

HEATHER: I’ve got ten thousand in this bag. And there’s another twenty once it’s done. Thirty grand. (Pg 25) It’s a load of money.

CARLA: Well, not really . . . actually.

HEATHER: It is when you have nothing.

CARLA: (Angry) That would be none of your business.

HEATHER: (Pg 26-27) Look at you pretending. As if thirty grand isn’t something you’re desperate for.

CARLA: I don’t know who you think I am . . .

HEATHER: You’re scrabbling. In the dirt. You’re nothing. You’d do anything to get out of here. For your kids. Thirty grand could relocate you all. Move to a different city. Start again. You need this.

CARLA: You’re wrong. **** you. You’re wrong. (Carla leaves, a long beat and she returns) Thirty grand? ****Scene Break*****

Heather’s house. Upper class. On the wall is a collection of Tarantula Hawk Wasps on display under glass. Heather is preparing tea and biscuits when Carla arrives.

HEATHER: (Pg 28) (Doorbell – Heather answers and leads Carla into the living room) Shoes off if you don’t mind. (Carla removes her shoes while Heather pours tea)

CARLA: (Pg 30-31) So I was thinking we make it look like a botched burglary. (she picks up and examines something from a side table) I’ll take some stuff . . . It’ll look more authentic that way. (Heather hands Carla a teacup and they both sip during the following conversation)

HEATHER: I’d rather not lose any belongings. I mean, I’m already paying you an awful lot.

CARLA: You want me to kill your husband and you’re worrying about losing your DVD Player?

HEATHER: (Pg 32) If you do a burglary, you could leave evidence.

CARLA: (Pg 31) Well, you come up with something then. (Carla sips her tea)

HEATHER: Actually, I have. I cook him a lovely meal and slip something in his drink (Heather watches Carla takes another sip of tea and smiles knowingly) that sedates him. Once he’s out, I call you and that’s when you kill him.

CARLA: (Pg 36-37) (pause in the conversation as Carla wanders around the living room drinking her tea. She spots the wasp display on the wall) Weird thing to have on your wall.

HEATHER: Yeh, well, that’s Simon. Ever the enthusiast. It’s a wasp called a Tarantula Hawk. It preys on [tarantulas]. It paralyses them. Plants an egg on it which burrows into it and grows feeding off its insides, but avoiding the major organs so it’s still alive.

CARLA: Bit like being pregnant.

HEATHER: What? Being eaten from the inside out? (Heather laughs inappropriately)

CARLA: May as well be. (Heather pours more tea for Carla – awkward silence) (Pg 39) This all feels very chummy doesn’t it? It’s funny, I didn’t expect that we would be getting on. We’re so different. (beat, then somewhat of an accusation) I spent most of my teen years severely depressed. I just want you to know that.

CARLA: You’re saying it like it’s my fault.

HEATHER: You don’t think it’s your fault?

CARLA: No! It was school. I mean come on. Everyone was horrible to everyone.

HEATHER: Not everyone.

CARLA: (Pg 40) (angry) Yes everyone. You’re nothing special, Heather. I dealt with shit too.

HEATHER: (Pg 41-42) I spent every lunch time in the art room with Ms. Beacher and every break making sure I avoided you and your gang.

CARLA: You thought you were so much better than me. Teacher pleaser. Goody two shoes. You didn’t know what my life had been like, and you judged me every day. You want to know what happened the day I killed the pigeon? I watched my dad smack my mum so hard her eye popped out of its socket. I watched her put it back in while I called an ambulance. I couldn’t be your friend. You pissed me off, you and your sunshine family -- my family? A black hole of shit! (Pg 43) (Carla sways slightly; Heather notices and checks her watch). Are we going to finish talking about the plan? (Pg 44) I don’t know what [he] looks like. Photo?

HEATHER: (takes a deep breath and lets it out calmy; she appears sufficiently chastised by Carla’s outburst) (Pg 45) I made you a pack of photos and information. It’s in the desk (motions to the desk) You grab it and I’ll tidy up.

Carla drains the last of her tea and holds it out to Heather as if she were the maid; Heather takes it, eyes down. Carla sways again as she turns to the desk. Out of Carla’s line of sight, Heather takes latex gloves from her pocket and puts them on. She takes a vial of liquid from her pocket and dampens a handkerchief. She stands watching Carla and waiting.

CARLA: (looking through the envelope, she is shocked. Slurring her words) This is . . . this is James.

HEATHER: (sweetly) No. His name is Simon. You must know that men who visit prostitutes don’t use their real name. He’s been visiting you for a couple of years now – quite heavily around seven months ago. (In one step Heather quickly grabs Carla who is still processing what’s going on, places the handkerchief over her mouth and holds it there until Carla passes out) ****Scene Break*****

(Pg 47) (Carla is sitting on a chair, hands and feet bound with plastic ties. She is gagged. Heather produces some smelling salts and waves it under Carla’s nose. She wakes and reacts aggressively, but is too restrained to do much)

HEATHER: (Pg 49) I’ll remove the gag shortly. I just want some space for my words first. (coldy) (Pg 42) I knew about your dad. I’d seen your bruises. (Pg 43) [But] I’d never even been slapped let alone punched before that day. You did it. I couldn’t see out of my left eye for two weeks it was so swollen. One minute I’m walking, next I’m on the floor. (Pg 49) And you all just stood there looking at me. And that’s when you walked over to me and whispered in my ear. (Heather moves behind Carla and whispers in her ear) Good girl. (Briskly, change of tone) (Pg 50) I’m going to remove the gag. This is your opportunity to speak. (she takes the gag off) Do you have anything to say?

CARLA: (Pg 51) (frantically) Are you going to kill me? I’m really sorry, but I was f*** up myself. I didn’t know what I was doing and I didn’t know right from wrong and I’m sorry, I am I’m really really sorry. I don’t know what else to say, but please don’t hurt me or my baby. Please.

HEATHER: (Pg 52) (laughs bitterly) I can’t believe I’ve actually made Carla Jackson cry. Actually you almost derailed all of this when we first met. When you offered me your child.

CARLA: You can have it. You can. (Pg 53) It’s his kid, Heather. You know it and I know it. So if you want [it] then it’s yours.

HEATHER: (Pg 54-55) (laughs again) Oh, sweetheart! I wish I could find some empathy somewhere. I know I should be looking at your background and excusing your behaviour as a symptom. I was just caught in the crossfire wasn’t I. And yet . . . What if I told you that Simon was dead already? That I’d hacked him to death in a bit of a jealous rage and he is currently in the freezer until I work out what to do with him. (Heather picks up a large kitchen knife from a table behind Carla) And what if I told you that I was planning on using this knife to extract the baby from your stomach while you were still alive. You said yourself you don’t want the child. What’s the problem?

CARLA: You’re insane! Let me go! LET ME GO! Help me! Help!

HEATHER: There is an impact to everything a person does. Even a single word can have an effect. (Heather’s phone rings and it snaps her out of her mania. She looks at the message and makes a decision. She shakily puts the knife down on the floor) (Pg 57) I’m going to undo the hand and foot ties. (She takes a pair of scissors and cuts the plastic ties) I’m trusting you not to run.

CARLA: (Carla lunges for the knife and hold it out in front of her to keep Heather at bay)

(Sarcastically – she believes she has the upper hand now) (Pg 59) You’re more insane than I thought you were.

HEATHER: (Pg 56) (softly) I’ve always found the idea of revenge repulsive. I find the threat of violence worse. (calmly) (Pg 59) By freeing you I have given you two opportunities. Kindness or violence? Which one are you going to choose?

CARLA: (a beat then plunges the knife into heather’s chest – Heather smiles) (Pg 60) Why are you smiling? (She hears a noise off stage, a door opening) Who’s that? Who’s that? [Simon?} You said he was dead. What have you done? They’ll think it was all me. Heather, what have you done?

HEATHER: Good girl . . . . (louder) Good girl. (Heather collapses)
```

---

## IC-0692: Watermelon Boats

- Title: Watermelon Boats
- Author (byline): Wendy MacLaughlin
- Work: 20 One-Act Plays from 20 yrs of the Humana Festival
- Publisher: Smith and Kraus Publishers
- Publication date as stated: 1996
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: KITTY, KATE
- Teaser before the introduction: Yes
- Spoken words (computed): 1573
- Already set (do not supply): none

### Source block (context only)

```text
Author: Wendy MacLaughlin
Book: 20 One-Act Plays from 20 yrs of the Humana Festival
ISBN: 978-1880399989
Publisher: Smith and Kraus Publishers
Date (Month/Year): 1996
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Henri Nouwen once said . . . . When we honestly ask ourselves which person in our lives mean the most to us, we often find that it is those who, instead of giving advice, solutions, or cures, have chosen rather to share our pain and touch our wounds with a warm and tender hand.

ACTRESS 2: The friend who can be silent with us in a moment of despair or confusion, who can stay with us in an hour of grief and bereavement, who can tolerate not knowing, not curing, not healing and face with us the reality of our powerlessness, that is a friend who cares.

TOGETHER: Watermelon Boats by Wendy MacLaughlin.
```

### Performance text (classify this)

```text
Characters: age from eleven to twenty-one in the course of the play KATE tan, thin, and healthy. She wears one long braid, jeans, and a button-down shirt. KITTY rounder, softer, and more feminine. She wears a peasant blouse, a full skirt, and two braids tied with ribbons.

KITTY: (Face front.) How much longer?

KATE: (Checking her watch.) Twelve seconds. Oh help, your candle went out. (Mimes lighting a match on jeans.)

KITTY: (Cupping candle.) Thank heavens you brought more matches.

KATE: Five, four, three, two, one. . . push them off. (They each push a boat into the water and watch them sail.)

KITTY: (Blows a kiss.) Bon Voyage.

KATE: Good luck. (She waves.)

KITTY: Aren't they gorgeous?

KATE: The best watermelon boats we've ever made.

KITTY: Fabulous.

KATE: Fantastic.

KITTY: With the candles they look like stars dancing across the water.

KATE: Sir Galahad sailing out to sea in search of the Holy Grail. Mine'll be first across I bet.

KITTY: Why?

KATE: It's smaller. The wind'll pick it up.

KITTY: They look the same to me.

KATE: The secret's in the cutting.

KITTY: {Preening} Kate, notice something?

KATE: No.

KITTY: I'm wearing a bra.

KATE: I'm never going to wear one.

KITTY: My mother says you'll look like a cow if you don't.

KATE: I like cows.

KITTY: Hanging to your knees.

KATE: She just says that to scare you so when you have breasts you'll smash them all down.

KITTY: Ummm. {Unbraiding her hair.} Who do you think we'll have for sixth grade?

KATE: Mr. Hawkins I hope.

KITTY: Me too. He has neat eyes. Every time he looks at me I have to go to the bathroom. Did you know I was born nine months after my brother died?

KATE: Exactly?

KITTY: He died January ninth. I was born October ninth.

KATE: {Incredulously.} They did it the day he died?

KITTY: I can't believe boys put that. . .

KATE: The whole idea is gross.

KITTY: I wonder what it feels like?

KATE: No boy is ever going to do it to me. .

KITTY: Never?

KATE: Well maybe if I get married but I probably won't because of my career.

KITTY: There're still pictures of him all over the house. My father wanted me to be a boy.

KATE: Mine too.

KITTY: Doesn't that just make you furious. (Frustrated with her hair.) Why does Mother braid my hair so tight.

KATE: Here, let me help. (Unbraids KITTY's hair and mimes brushing.)

KITTY: Thanks. You've been my best friend since first grade. Isn't it amazing we've been coming to this lake for six years? Am I yours?

KATE: My what?

KITTY: Best friend.

KATE: Sure.

KITTY: Do you have a lot of best friends?

KATE: Some.

KITTY: Don't you think it's weird we're best friends and we're both named Katherine?

KATE: Lucky everyone calls you Kitty and everyone calls me Kate.

KITTY: Kitty's a funny name.

KATE: Perfect for you.

KITTY: I like Kate better.

KATE: When I'm a great writer everyone'll call me Katherine.

KITTY: Like Katherine Mansfield.

KATE: Who?

KITTY: "I want by understanding myself to understand others." She wrote that in 1922. In her journal.

KATE: Oh... yes.

KITTY: I have total recall. People with high I.Q.'s usually do.

KATE: (Impressed.) You know your I.Q.?

KITTY: Ah-huh.

KATE: How?

KITTY: Once I looked it up in Miss Porter's office.

KATE: What's mine.

KITTY: That's not my business.

KATE: But you know it.

KITTY: I might.

KATE: Then tell me.

KITTY: I shouldn't.

KATE: I'll tell Miss Porter if you don't.

KITTY: Weeeeelllllll... I don't remember exactly but it's lower than mine. (A foghorn blows. KATE stops brushing and fixes her hair.) If this fog ruins everything I'll die. We can hardly see the boats. Oh there they are. Look, Kate. (No answer.) Kate? Are you still mad?

KATE: (Cold) I'm not, but the rest of the class is furious. We had a chance to win the Drama High School Cup three years in a row.

KITTY: It's just a stupid play. I'm sorry. I know you wrote it and it's very good but. . .

KATE: It would have looked good on my college transcript.

KITTY: I'm sorry. I told you to give me sets. I'm good at art. Why'd you make me be that dumb ol’ maid?

KATE: Come off it, Kitty. You died to be the maid. The maid got to wear the cute costume.

KITTY: Well no one told me she had any lines.

KATE: Only one.

KITTY: You know I freeze in front of people.

KATE: Four words. Four simple words and you screw them up.

KITTY: My parents must have gone through the floor with embarrassment. God, I wish I had a drink.

KATE: I've told you a million times every ounce of liquor you drink destroys ten thousand brain cells.

KITTY: Who cares about my brain anyway. Boys certainly don't.

KATE: You really make me mad, you know it? When are you going to grow up? Really, Kitty. When?

KITTY: (Imitating) Really, Kitty? When? You sound exactly like my parents. Grow up, Kitty, be like Kate. Kate has her feet on the ground. Kate has a head on her shoulders. I don't want to be like you. I want to be me. Anyway I can't be you, can I? Boy am I insecure. Guess it's because I haven't had my period in two months. (A laugh.) You don't think I'm pregnant do you?

KATE: Two months isn't very long.

KITTY: I stopped wearing a diaphragm.

KATE: Damn.

KITTY: It's such a bother. Who knows what's going to happen every date.

KATE: You know what's going to happen if you get pregnant.

KITTY: I'll get an abortion.

KATE: Don't be crazy.

KITTY: I don't have the vaguest idea who the father might be. Can't imagine any of the imbeciles we know being a father. Can you?

KATE: You've got to stop sleeping around.

KITTY: I can't. I mean I don't want to.

KATE: Have some respect for yourself.

KITTY: I like it.

KATE: You like being used? That's what they're doing you know. You might just as well be a urinal.

KITTY: It's not like that. When I'm close to a boy... really close, I feel important. For a time someone needs me. We're connected. Both a part of the same thing. Afterwards though, at home in bed. . . I feel more alone. Kate, do you think there might be a real person growing inside of me. A little body with fingers and toes?

KATE: Why do I feel responsible for you?

KITTY: Promise you'll come with me if I have to have an abortion.

KATE: I'd do anything in the world for you but that.

KITTY: You have to.

KATE: I can't. It's wrong.

KITTY: I would for you.

KATE: Abortion is wrong.

KITTY: What'll I do?

KATE: I'm sorry, Kitty. I have to follow my conscience.

KITTY: You're really hard, Kate. You know it.

KATE: If having principles is hard. . .

KITTY: Even here... in the Spring, at the lake. I'm all relaxed but you're still so strong. Thin, brown. . .

KATE: I wish I could help you. . .

KITTY: Thin... brown and hard. Year round.

KATE: So be it.

KITTY: Very dull.

KATE: What?

KITTY: Thin... brown and hard. Year round. It's very dull . . . .booooorrrrring.

KATE: (Tight lipped.) Sorry.

KITTY: Some day you should let go a little. Maybe... smile at a guy.

KATE: Too disciplined I guess.

KITTY: Well brought up.

KATE: Probably.

KITTY: Or afraid.

KATE: Afraid?

KITTY: You might spoil the image. Perfect woman. Nobly planned.

KATE: Well it's late. I have to go.

KITTY: I bet you'll spend the night thinking of lines you won't cross. Perfect stays on one side looking down her nose at the rest of us screwing it up on the other.

KATE: (Turns to go.) Goodnight, Kitty.

KITTY: (Grabs her arm.) And you think you're going to be a writer? That's a laugh. Who's going to read you? You don't know the first thing about life. (Foghorn blows. They change hair style.)

KITTY: (Shivers.) Ohhh it's getting cold. (They put on sweaters.) Not even a moon. But look, the first star is out. Don't you wonder if there aren't people just like us up there thinking we're a star. Oh God, Kate, promise YOU WON’T write that in your first book. Everyone'll think I'm psycho.

KATE: I doubt I'll write one page, much less a book.

KITTY: You're kidding.

KATE: No.

KITTY: You're going to be a famous writer.

KATE: Who says?

KITTY: You've always said.

KATE: Changed my mind.

KITTY: You can't do that.

KATE: Stop staring at me.

KITTY: I counted on you.

KATE: Swell.

KITTY: You've always known where you were going and how you'd get there.

KATE: That was grade school.

KITTY: High school too.

KATE: Well college is different. Not only harder but there're lots of people out there smarter. And they don't try to please everyone all the time. You were right, Kitty, I do want to be perfect. Remember when you said that?

KITTY: No.

KATE: Five years ago. Here at the lake. At first I was furious. Then I wanted to cry but I couldn't. Know why? I didn't feel enough.

KITTY: That's better than feeling too much like me.

KATE: You're sensitive.

KITTY: I get hurt.

KATE: You know what I do when I start to feel something? I come on with my holier than thou superior look. Inside I'm dying to experience everything but I never will because I act like I already have. Oh Kitty, what if I die without ever feeling anything?

KITTY: Then you won't feel guilty all the time. That's what makes me want to throw myself in the lake.

KATE: Right now you wouldn't believe how guilty I feel. If I don't become the world's greatest writer my parents won't be proud of me and you'll be disappointed.

KITTY: But you'll make it. You've got talent.

KATE: I'm not as smart as you.

KITTY: But you're stronger.

KATE: No, Kitty, you are. You wouldn't let me change you.

KITTY: Did you want to?

KATE: I thought you wanted me to.

KITTY: All I want is to get married, be a good mother and have you as my friend.

KATE: You don't need me.

KITTY: We need each other. You're my perfect friend. I love you.

KATE: The only thing perfect about me is that. (Foghorn.)

KITTY: (Climbs ladder.) Look at our boats. . . way out. Sailing together, neck and neck.

KATE: (Climbs ladder.) We're not across yet.

KITTY: But we're going to make it.

KATE: The trick is the journey.

KITTY: Isn't it hard to believe we're already twenty-one?

KATE: Seems like only minutes ago we were eleven.

KITTY: (Extends hand.) Sometimes I wish we didn't have to get any older.

KATE: (Takes KITTY's hand.) Wouldn't it be nice if now could be always. (They hold hands as the light gets blinding bright before fading to black.)
```

---

## IC-0693: Well

- Title: Well
- Author (byline): Lisa Kron
- Work: Not specified
- Publisher: Theatre Communications Group
- Publication date as stated: March 2006
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: LISA, ANN, OSCAR, LORI
- Teaser before the introduction: Yes
- Spoken words (computed): 2152
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lisa Kron
ISBN: 978-1559362535
Publisher: Theatre Communications Group
Date (Month/Year): March 2006
```

### Introduction (context only: never use it for content warnings)

```text
TOGETHER: Well by Lisa Kron
```

### Performance text (classify this)

```text
NOTE: This cutting asks one student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

NOTE: Actress 1: Lisa Actress 2: Ann, Oscar, Lori

LISA: (To the audience) This play that we’re about to do deals with issues of illness and wellness. It asks the question: Why are some people sick and other people are well? What is the difference between those people? This play is NOT about my mother and me. That is my mother. She doesn’t feel well enough to get up and do things – but this is not about her. It’s not about how she’s been sick for years and years and years and I was sick -- but somehow I got better. It’s not about how she was able to heal a neighborhood but she’s not able to heal herself.

ANN: (Groaning) Oh, dear lord.

LISA: (Reacting in sudden irritation to her mother’s unexpected interruption) Mom!!!

.

LISA: Mom, how’re you doing?

ANN: (NOTE: throughout the play, Ann should play up how bad she feels) Oh, lord. I’m having such a bad allergy day. I just can’t focus on anything. Of course I didn’t get any sleep today because the phone started to ring at about ten o’clock this morning and people kept calling all through my prime sleeping hours so . . . (To audience) Oh, hello. Lisa, why don’t you offer these people something to drink? (painfully limping) Oh, lord, this hip is just . . . . Oh! I don’t know . . . (exits)

LISA: (Watches her exit, then to the audience) My mother’s been sick, like that, for as long as I can remember. For her whole life actually. Well, I come from a family where everyone is ill. It is the norm . . . the family mystery illness – the general inability to move, to physically cope, to stay awake. This is the primary malady suffered by my mother.

ANN: (enters with individual packages of chips and/or cookies and unexpected energy and impishness) I found these at that restaurant supply place. Aren’t they cute? Here. (She throws one at Lisa. It hits her and falls. Ann is delighted) You don’t want one? They’re so cute. (She throws another one and hits Lisa again). Okay. Suit yourself. (She exits again toward the kitchen)

LISA: (To the audience) My mother is a fantastically energetic person trapped in an utterly exhausted body. It’s very confusing. Her energy level has two settings: all or nothing. Most of the time it’s nothing, but when she has a burst of energy it’s awe-inspiring. . For instance, when we were very young she decided she wanted my brother and me to be raised in a racially integrated neighborhood, and then she set about to create one.

ANN: (returning, with a thought just occurring to her) You’re not writing a play about me are you? (To audience) I don’t even like to have my picture taken. I certainly don’t want to be in a play. (Shrugging her shoulders . . . To Lisa) [Well,] it’s not like you’re going to make it seem like I’m a hypochondriac or something. You go ahead and do your thing.

LISA: (To audience) From the time I was seven to the time I was fourteen, my mother was the president of the West Side Neighborhood Association. In 1968, when my mother started the Association, our neighborhood in Lansing, Michigan, was in serious trouble. She started suggesting to people that not only was the West Side not sick, but that an integrated neighborhood was actually healthier than a non-integrated neighborhood. The houses in this neighborhood are beautiful. The streets are curvy. There are flowers on the boulevards. When the first black families moved in, the city sent crews to dig the flowers up. That’s the way it works, my mom says. That is how a slum is made. It’s not that the people who live in the neighborhood aren’t taking care of themselves. The city withdraws all the resources.

ANN: What else do you remember about that time?

LISA: (entering a memory scene -- to the audience) My best [friend was] Oscar. The neighborhood is integrated, but by demographic chance my brother and I are the only white kids in our school. In any case, it’s a good thing to be different, my mother says. But I’m not so different from Oscar.

OSCAR: Hold up. I gotta idea. I gotta idea. Lisa. You stand here, I’m’a stand there. This is a really good game. It goes like this. I call out like this: “Hey, white girl!” And you call me back, “Hey, black boy!” Okay? It’s cool. It’s a cool game.

LISA: Okay, you start.

OSCAR: Hey, white girl!

LISA: Hey, black boy! (They both laugh) (To the audience) We continue in our loud, cool voices until I hear my mother call me. I go into the back hall where I am informed gently . . . but firmly that “black boy” is a phrase I am not to use again. I state the obvious: “But he is a black boy!” “Yes,” she tells me . . .

LISA and ANNE: But that is a term that has been used historically to insult black men and it’s hurtful . . . “

ANN: (To the audience) I don’t have the vaguest recollection of saying that . . .

LISA: (simultaneously with Ann above) “Oscar’s not hurt by it! He made up the game!” (by herself) Mom, please!

ANN: (To Lisa) Oh. Shh. I’m sorry

LISA: Mom . . . I’m doing a thing here. This is where we look more closely at your use of social activities to build the political power of the Association.

ANN: Oh, yeah. Everybody thought I was kooky about that, just like they think I’m kooky about the allergies now. Nobody could figure out why I’d put so much work into a Fourth of July celebration. (makes a horrible noise of pain) Oy, boy, Oy, boy.

LISA: (To Ann) Are you all right?

ANN: Yeah. I’m about to take a pain pill (Reaches for her glass, even more pain) Oh! If I could reach that glass of water. It’s just a little out of my reach unless I get up out of this chair, which I would rather not do right now.

(switches character to LORI)

LORI: Lisa!

LISA: What do you want?!

LORI: What do you have to do with your hair? (Pokes Lisa in the head) (Pulling at Lisa’s hair) Ugly, stringy, nasty. Eew.

LISA: (Doing her best to be firm) Okay. I’m going to have to ask you to leave –

LORI: You’re gonna what? (A threatening pause) You’re gonna what? (Lisa is trapped in Lori’s treacherous gaze for a moment, until suddenly Lori makes a move and chases Lisa across the stage into Ann’s area – LORI morphs back into ANNE)

ANN: What’s going on?

LISA: I don’t know! I’m being tormented by a nine year old from my past, who is creating a totally wrong impression about the neighborhood. (To the audience) What I am trying to convey is that the Association stabilized the neighborhood and, by the way, it’s still a stable racially integrated neighborhood today. Okay, there might have been a little bit of tension between some of the kids. But the big picture is that the Neighborhood Association was working. The adults were getting along.

ANN: What are you talking about? Of course there was tension among the adults. You’re right, the Association was very successful –

LISA: Yes!

ANN: . . . but there were certainly tensions. Howard and Jim for instance, those two were condescending as all get out. You know, they took over.

LISA: (Muttering to herself) Okay, go ahead. Tell the story.

ANN: Oh, yeah. At the end of the second year, when it was suddenly clear that the Association had become a major political power in the city of Lansing, Jim ran against me for president because, as he said: “Now that the Association has gotten some power it’s time for a man to take over.” When Jim took over, they went ahead and cut all the things that they thought were so frivolous – the door-to-door newsletter delivery and the holiday decorations and all of that – and at the end of the year all the power was gone and no one was even showing up for meetings . . . I sure didn’t like how condescending they were, but frankly I was relieved that someone else was finally willing to take over. I hadn’t been well enough to do it in the first place. (ANNE morphs into Lori Jones enters, looks at Lisa and bursts into loud, derisive laughter)

LISA: (To audience) Okay, I would like to make something clear here. I would like you to know that Lori Jones is NOT representative of my experience growing up in this neighborhood. (Lori moves in on Lisa and runs her finger up Lisa’s back.)

LORI: (Overlapping) How come you ain’t got no bra on yet?

LISA: (Overlapping) – it does not make clear that growing up –

LORI: (Overlapping) Hmm? How come you don’t answer me?

LISA: (Overlapping) - growing up in this neighborhood was a positive –

LORI: (Overlapping) Are you deaf?

LISA: (Overlapping) - it was a positive experience, but Lori J –

LORI: (Overlapping) I said: “Are You Deaf?” Huh? Huh? Huh?

LISA: (Overlapping) -- Lori Jones is not helping to establish that. Seeing her is just going to play into any stereotypes you might already be holding.

LORI: (To Lisa) I don’t care if you don’t want me in your stupid play. What’re you going to do about it? ‘Cause I was in your stupid life. (exits)

LISA: (To Ann) Do you see why I don’t want her in my . . .

ANN: Well, yes and no. Bad manners is one thig. Kick Lori out of the play for acting like a crumb if you want, but not because she’s not an appropriate “representation.” Part of the point of growing up in an integrated neighborhood was that you didn’t have to extrapolate from abstract impressions of black people, because you knew actual people. Lori didn’t have that kind of power. She was just one little girl. (BEAT)

LISA: YOU KNOW WHAT? WHY DON’T YOU DO YOUR OWN SHOW? YOU TELL THEM THE “REAL STORY,” SINCE APPARENTLY I’M NOT DOING IT RIGHT. HAVE A REALLY FUN TIME, MOM, BECAUSE IT’S YOUR SHOW! (Exits)

ANN: I don’t want a show. (To the audience) She must be having a reaction. (Pause) (To Lisa) Lisa? Your audience is still here, honey. (Back to the audience) I don’t know where I got my ideas about integration and so forth, because the town where I grew up was all white, so it’s not like I had any personal experiences with it. I had very strong feelings about the evils of segregation and the evils of discrimination and all that. Lisa . . . she is like an amazing star to me – my daughter. We were rooted in the same place, and she kept growing which was the most wonderful thing. To see her branch off and to have a life so different, and to have all that energy that I couldn’t even imagine. But I guess I never questioned that we were starting from the same place. But I think maybe she doesn’t feel that. (Ann waits for a response from Lisa. There is none. She retreats into her private thoughts and then transitions into an emotionally exhausted half-sleeping state)

LISA: (To audience) Sometimes I see her in that almost comatose state – even just to raise her arm a little or turn her head makes her gasp in pain, and I get angry. She can’t walk. She can’t move. The moaning – the moaning drives me CRAZY. What is the difference between that body and mine? I look at her in that state and I feel like I’m going to drown! (Beat, deep cleansing breath) (To Ann) Hey.

ANN: Do you want to just say whatever it is you’re afraid to say to me? Because I’ll tell you, frankly, I’d rather you just said it out loud whatever it is.

LISA: (To audience) What am I supposed to say to her?! . . . I moved to New York and got into therapy. I learned, finally what I never learned at home, that there is a correlation between not sleeping at night and feeling tired during the day. I started to learn how to inhabit my body – that there is an alternative to dragging your body around like a stone and wishing it would disappear. That the label of “allergies” doesn’t work for me. That I resent that the sick people keep trying to pull me down and make me like them. I escaped to the land of the healthy people – and when I come back here I want to scream: “I AM NOT LIKE YOU!” And then I’m seized with dread because how do I know, really, that I’m not.

ANN: Oh! Lisa, did you really bring me out here to make people think that I’m crazy and . . . whiney . . . and a hypochondriac? I’m about ready to come over there and wring your neck if you don’t just say what you have to say to me.

LISA: (Overlapping) I can’t. This thing has gotten all out of proportion.

ANN: (Overlapping) You can –

LISA: (Overlapping) I can’t. .There’s nothing –

ANN: (Overlapping) You’re tying yourself in knots – just say what you want to say.

LISA: How can you let this happen?! WHY CAN’T YOU MAKE YOURSELF WELL?! (Tiny stunned pause)

ANN: That is a horrible question. You have seen me struggle for years.

LISA: I was sick, too. And I got better.

ANN: And I am so grateful for that. But we are not the same person

LISA: But, we were, Mom. We were. I wanted to be just like you. I thought I was going to save a neighborhood because I couldn’t imagine a life more meaningful than that. But in order to get better, I had to grow in a different direction. I left home and I got better.

ANN: So what you’re saying is – what? How do you think you got better?

LISA: I think I was sick because you were sick, Mom. I think I watched you and took for granted that it was how one lives in the world. And then I went away and learned I didn’t have to be that way. Why are some people sick and other people get well? (To audience) She’s overwhelming to me. She doesn’t make any sense. She’s so sick. And she’s so well. I can’t make her make sense . . . . This is something my mother wrote for one of the [Association] meetings:

(She reads as Ann gives voice to the letter; voices can overlap and ANNE’s voice should gain strength, her stature should become stronger – she should become “well” during this closing)

ANN: This organization is about people. It’s about busy people and lonely people. Happy people and frightened people. Young people who want a good life for their children, and old people who want to know that somebody cares. People so busy that they don’t have time to wonder if anything they are doing is worthwhile, and people who face day after day of having nothing to do but wish that someone might need them. This is what integration means. It means weaving into the whole even the parts that are uncomfortable or don’t seem to fit. Even the parts that are complicated and painful. What is more worthy of our time and our love than this.
```

---

## IC-0694: Women in Flames

- Title: Women in Flames
- Author (byline): Mary Garripoli
- Work: The Best Stage Scenes of 1994, Pg 121-127
- Publisher: Smith & Kraus
- Publication date as stated: Jan 1995
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: DORIS, ANNETTE
- Teaser before the introduction: No
- Spoken words (computed): 1473
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mary Garripoli
Book: The Best Stage Scenes of 1994, Pg 121-127
ISBN: 978-1880399668
Publisher: Smith & Kraus
Date (Month/Year): Jan 1995
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Advances in American feminism have rarely happened smoothly.

ACTRESS 2: The gains of one generation have often both shaped and conflicted with the ambitions of the next.

ACTRESS 1: First-wave feminists fought for women’s suffrage.

ACTRESS 2: Led in the 1970s by icons like Gloria Steinem and Betty Friedan, a second wave pushed for economic and legal gains.

ACTRESS 1: Their ideals would eventually clash with the spirited individualism of women in their 20s and 30s who still advocated for women’s rights while embracing a “girlie culture.”

ACTRESS 1: Welcome to 1969, as a mother and daughter try to bridge the generation gap and find common feminist ground.

TOGETHER: Women in Flames by Mary Garripoli
```

### Performance text (classify this)

```text
It is the middle of the night. Annette enters. Unbeknownst to Annette, her mother, Doris is sitting on the other side of the room in the dark. Annette opens the front door. Before she can switch on the lights, the beam of a high voltage flashlight hits her.

DORIS: (Pg 121-127) Stay right where you are! Don't move a muscle.

ANNETTE: Mom?! It's me!

DORIS: I know who it is. Jump! Three inches off the ground, let's go!

ANNETTE: Mother, give me a break! I'm turning on the lights.

DORIS: Aha! I knew it! When you moved just now, I saw it with my own eyes. You're not wearing a bra, are you?!

ANNETTE: Mother?!

DORIS: I knew it! I knew it all along! Okay, let's have it. Spit it out! If you're not wearing them, then what have you done with my brassiers?

ANNETTE: Mom, it's the middle of the night. Can we talk about your brassiers in the morning?

DORIS: They're my brassiers, I'll talk about them when I want to . . . Well . . . I'm waiting.

ANNETTE: I burned them.

DORIS: You what?!

ANNETTE: I burned them! ...At the Feminist rally outside the mayor's office last Saturday! I burned six of your bras and tied together three of your longline girdles to make a banner!

DORIS: You burned my underwear? In public?! Did anyone know it was MY underwear?

ANNETTE: Nobody knew! I didn't write your name on 'em!

DORIS: Why? Why did you do it?

ANNETTE: To liberate women from the oppression of men. We have to burn our bras to free ourselves! Is there a better way to celebrate Fourth of July?

DORIS: Is that a real question?

ANNETTE: Go ahead, make a joke! It's easier than listening to me.

DORIS: Don't start with me, I always listen to you! You think I'm nothing! That I'm not a part of life, that I don't matter. Well, this time you went too far!

ANNETTE: Sometimes you have to go far to get what you want!

DORIS: Look, I don't wanna fight with you. There's really only one thing I need to know---and I need to know so I can get some sleep, which believe me I also need---why my bras? Why burn my underwear to free yourself?

ANNETTE: Because I only own one bra and I need it for dance class. (beat) Can we finish talking about this tomorrow? I have to get to bed. They bombed the chem lab last week. I have three experiments to make up tomorrow.

DORIS: Come back here! You can't go to bed yet! Not with my underwear on your conscience! You owe me an apology.

ANNETTE: For what?

DORIS: For what? For stealing. You took something that was mine. I want remorse!

ANNETTE: Look, I'm sorry, okay? If I knew you were gonna get so bent about this . . .

DORIS: This is your apology?! This is how you feel when you break a commandment?

ANNETTE: I didn't think of it as stealing.

DORIS: Whatta you call it? Borrowing? It's not borrowing because you can't give them back--- except maybe in an urn!

ANNETTE: You really should be thanking me. You're asleep. Somebody had to wake you up.

DORIS: So now you're gonna play God and tell me how to think?

ANNETTE: You don't get what I'm about at all. You think this whole thing is about my stealing your underwear. . . which I did! Okay, alright!

DORIS: You are five minutes from being grounded!

ANNETTE: Fine, ground me! See if I care! Ground me for life!

DORIS: That's it! Pack up your love beads, you're outta here! You think I'm stupid. You think I don't know about Women's Liberation? I'm a wife and a mother. If that isn't the definition of "slavery" I don't know what is!

ANNETTE: Then join in with me, don't yell at me.

DORIS: What would I be joining?

ANNETTE: Mother, you're a woman----this is Feminism!

DORIS: Okay, so tell me about it. Tell me about Women's Liberation.

ANNETTE: First of all, call it what it is. Feminism. That's what we call it. Men call it Women's Liberation because. . . well. . .

DORIS: It's catchier?

ANNETTE: Very funny!

DORIS: Well, it is. It definitely has more of a ring to it.

ANNETTE: You think you're so funny, but you play right into that "Helpless Little Woman" s***!

DORIS: This is what you believe?

ANNETTE: This is what I know. Are you listening to me?

DORIS: I'm listening! I am listening! I listen to you more than you listen to me---more than your father listens to either of us! Whatta you want, Annette?

ANNETTE: I want to be everything I can be.

DORIS: That's all I ever wanted for you. Maybe we're both feminists. Although I still can't see how my frying my underwear in the street is gonna make your father pick his up off the floor.

ANNETTE: See Mom, that's what I mean about you. You reduce everything down to something stupid.

DORIS: Well, I'm sorry Miss College Student---or should I say, "Ms."? It's the little everyday things that life's about, everything can't always be big, important issues.

ANNETTE: There's a lot more going on in the world than your laundry. You get more pissed off about dumb little stuff than you even do about the war. You really oughtta look at that.

DORIS: Don't tell me I don't get pissed about the war! Daddy and I fight about Jane Fonda at least twice a week!

ANNETTE: Daddy's a war monger!

DORIS: No, he isn't. He's a Veteran. When you were born, he bragged for months about how you have the same birthday as Mamie Eisenhower. He's a good guy---if he picked up his fruit of the looms, he'd be almost perfect.

ANNETTE: I can't believe Daddy would just refuse to pick up his underwear.

DORIS: It's not that he refuses, it's more like he can't get it. The same way he can't remember to put the toilet seat down so I don't sit in water when I go to the bathroom at night. Men are a mystery.

ANNETTE: Men are the same as us.

DORIS: That's the Women's Lib talking.

ANNETTE: Mom, you're a fossil. This is 1969, things are different now. I'm going to bed!

DORIS: I think I'll sit up a bit for Dad. He went to the fireworks at the V.F.W.

ANNETTE: You always sit up and wait for him. Just once, I wish you'd go out---make him wait up for you. You can walk out the door. You're a free woman.

DORIS: I've heard. But I can also see the fireworks from our window, and that's good enough for me, thank you. Goodnight, Annette.

ANNETTE: I'm sorry about your bras, Mom. I'll get you some new ones.

DORIS: Apology accepted and you don't have to. Your father's gonna buy me all new clothes for our trip. We're going on vacation, him and me.

ANNETTE: You didn't tell me about it.

DORIS: I just decided. Actually, we're going because you burned my bras. See, when I went to get dressed this morning, I had to put on my blouse without a bra---we know why, let's not go into it again---and Daddy could tell.

ANNETTE: That you didn't have a bra on? So what?

DORIS: Netta, I don't flounce around without underwear like you do. No woman my age does. We weren't raised like that. I used to wear a girdle to bed before a big date! When your father didn't see a brassiere on me, he knew something was up. You know how he gets. All crazy in his head when he thinks there's something outta his royal domain. So I told him, "I lost all my bras, don't bug me!" So then we had a fight.

ANNETTE: About your bras?

DORIS: About my having an affair.

ANNETTE: What are you doing? You're thirty-six years old!

DORIS: Meaning what? No one would find me attractive?

ANNETTE: You know what I mean!

DORIS: No, I do not know what you mean. I'm not really what? Young anymore? I'm not pretty or sexy or ALIVE anymore?! No, Annette, I do not know what you mean! Or maybe more to the point, I don't care . . . The fireworks are almost over. Look! Come see them. I love the ones that streak across the moon. Their tales all full of color---like a comet or something. It takes guts to make a splash like that.

ANNETTE: Are you having an affair, Mommy?

DORIS: That's what your father wanted to know.

ANNETTE: Are you?

DORIS: Well, that's nobody's business but mine. I'm a free woman, remember? But since you asked, I'll tell you what I told him. No, I am not having an affair. Of course, I still couldn't explain how I'd lost my underwear. . .

ANNETTE: I'll tell him what happened!

DORIS: You could do that. I wouldn't argue with you.

ANNETTE: You want him to think you're having an affair. . .

DORIS: I want a vacation. And. . . I wouldn't mind if he stayed home a few nights a week. . . and if once in a while he picked up his underwear. Even if he just did it out of fear. Sometimes you have to go far to get what you want.
```

---

## IC-0695: Words to Say at the End of the World

- Title: Words to Say at the End of the World
- Author (byline): Mark W. Sasse
- Work: Theatrical Duets
- Publisher: CreateSpace Independent Publishing Platform
- Publication date as stated: Feb 2016
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MOM, SALLY
- Teaser before the introduction: Yes
- Spoken words (computed): 1440
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mark W. Sasse
Book: Theatrical Duets
ISBN: 978-1523814749
Publisher: CreateSpace Independent Publishing Platform
Date (Month/Year): Feb 2016
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: According to Victor Gilinsky, program advisor to The Nonproliferation Policy Education Center, in the years since Hiroshima and Nagasaki, nuclear war has become an abstraction, stripped of its horrors.

ACTRESS 2: North Korea and the United States exchanged threats of annihilation. Pakistan and India have issued nuclear threats and counter threats. And do we really know how close Iran is to developing their own nuclear weapons?

ACTRESS 1: Oh, I know, it’s easy to put nuclear weapons out of mind, to let sleeping dogs lie. The weapons play essentially no role in day-to-day life. Even Hollywood has given up making apocalyptic nuclear war movies.

ACTRESS 2: But the nuclear weapons aren’t asleep. They are ready to go.

TOGETHER: Words to Say at the End of the World by Mark W. Sasse
```

### Performance text (classify this)

```text
Mom, an overbearing mother preparing her daughter for college Sally, a sassy teen who's ready to leave for college Setting: Anywhere, modern time

Mother packing a suitcase, looking around frantically. Daughter is busy on her phone.

MOM: (Pg 66-77) Sally, do you have everything?

SALLY: (rolling her eyes) Yes, we went over the list five times.

MOM: Do you have your passport?

SALLY: Yes.

MOM: Toothbrush?

SALLY: Yes, Mom. I know how to pack.

MOM: But you've never packed for college before.

SALLY: But I've been brushing my teeth every day of my life. I'm not a little girl anymore.

MOM: (handing her a piece of paper) Now here's a list of all our numbers. Mine. Dad's. Uncle Sy. Mrs. Cho from across the street. Police. Fireman. Family doctor. Chiropractor.

SALLY: Chiropractor?

MOM: You're not going to be used to those college beds. You might tweak your back.

SALLY: Mom, I have a phone. It has everyone's numbers in it.

MOM: I know, but I just want you to be prepared. Here take this paper in case you lose your phone. (There is a huge explosion that shakes them and knocks them nearly off their feet.)

SALLY: What was that? (Sally looks up above the audience, awestruck)

MOM: (tightening a strap on the suitcase) It's probably a gas explosion at the airport.

SALLY: (staring straight ahead) Mom . . . .

MOM: Maybe you should stay home and go next semester.

SALLY: Mom . . . .

MOM: You are young for college anyways ...

SALLY: (screams) Mom!

MOM: What is it? (She turns around and looks up.) That's a mushroom cloud.

SALLY: (frightened) Uh-huh.

MOM: (matter-of-factly) That's not supposed to happen.

SALLY: (frightened) No. (They reach out to hold each other's hand, and then freeze for a second.)

MOM: Pause. (takes a deep breath and let's go of Sally’s hand) Can we just slow time down for a second? I need a moment to ponder this. (to audience, daughter still looking at the mushroom cloud, melancholic) It doesn't seem fair. I've been preparing my daughter for this day her entire life, and on the day I send her off to college, someone drops a nuclear bomb in our backyard. Now you may wonder how I have so much time to talk with you if a nuclear explosion is just north of us a few hundred meters. That's a fair question. It has to do with the equilibrium of time. I read about this on Facebook. There's always a give or take when the sandman comes calling to steal time. He always gives a little back, just for a moment. Don't believe me? Did you ever slam your finger in a door and then consciously think how painful it will feel as soon as that electric synapse sends the signal to your brain? Why just the other day I slipped on a plastic bag which was on my hard tile floor, and before gravity body-slammed me onto that marble, I had time to plan dinner for a week, think out my Christmas shopping list, and even say a little prayer that I wouldn't bruise too badly. Poor Sally. (She turns to her and touches her hair.) She'll never get to experience college or marriage. I'll never see my grandchildren. (motions quickly like insects are flying around her; she keeps swatting them away.) The memories. Flashing. Thick as a swarm of bees. Stinging. They sting my eyes. They ... (Suddenly she gets a big smile on her face as that of a mother looking at a baby. Sally gets down on her knees and pretends like she's a baby.) Look at how adorable she was. Oh ... but (She catches a memory from the sky, and it sours mother's attitude.) She got colicky real quick and then ... (Sally starts crying. Mom points down at Sally) She did that. A lot. Non-stop crying. (Sally continues crying.) The only thing that made her stop was either to carry her outside or lay her on the floor butt-naked. I have pictures around here somewhere, but I'll spare you the details. (She looks up and sees another memory.) And then she hit her terrible twos. (Sally takes off and runs around like crazy.) From non-stop crying to non-stop movement.

SALLY: (running around the room) Da-da-da-da-da-da-da-da-da.

MOM: And noise. Constant noise. I did everything for her, but would she say ‘Mom'? No! Only ...

SALLY: Da-da-da.

MOM: I think she did it to spite me! And then the first day of school. (turns to Sally) Here's your lunch and hat. Don't eat too quickly, and save the fruit for last.

SALLY: Yes, Mommy.

MOM: And straighten your collar. Remember to be polite, don't take candy from strangers, stay away from the neighbor's dog, and always remember to ... (Sally morphs to an older age, now wearing braces.) The years go by so quickly.

SALLY: Mom, these braces hurt my gums.

MOM: Stop your whining. You know how much those cost?

SALLY: Mom! But you don't know what it's like.

MOM: You're right, you ungrateful child. I don't know what it's like because we were dirt poor. Too poor for dental work. You don't know how good you have it. When I was your age ...

SALLY: (sassy) You walked to school, uphill both ways, in four feet of snow, even though you lived in the tropics. (Sally freezes, looking back at the cloud.)

MOM: (to audience) I don't miss that age. (another memory flashes by) But before I knew it, she was sixteen. (Sally becomes older.)

SALLY: (on her phone) Mom, can I spend the night at Lili's house?

MOM: No, you have that science paper to write, don't you?

SALLY: (on her phone) Just chill. I'll get it done.

MOM: Did you tell me to chill? I won't chill.

SALLY: Yeah, don't I know it.

MOM: What's that supposed to mean?

SALLY: (overly dramatic) You're strangling me. I can't go anywhere or do anything.

MOM: Just because I care about my daughter ...

SALLY: Please care less. (Sally goes back to her suitcase and looks up at the mushroom cloud again.)

MOM: (to audience) Almost makes me miss the days of the braces. She always had a mouth on her. Today. A college freshman. (emotional) Look at her. I don't want to turn away, but I have to think of something. (looking up at the sky) There must be a way to stop this. (Mom freezes, reaches back and takes her hand, looking up at the mushroom cloud.)

SALLY: (Unfreezes, drop's Mom's hand, and addresses the audience.) My Mom has always been a little overbearing and completely in control of everything. Undoubtedly, this mushroom cloud is freaking her out. How do you control that? (pointing) But don't get me wrong, if there is an obscure way to survive a nuclear holocaust, she'll find it, or die trying. From the time I was just a little wee girl, she never let me out of her sight. Okay, maybe that's a bad example. But, here's one. Just last year a ... boy asked me out, and I asked Mom if ... (She turns to her mother and her mother unfreezes.) Mom, can I go out with Tony tonight?

MOM: Is that Tony with an 'i' or with a 'y'?

SALLY: 'Y'

MOM: Because I have to know.

SALLY: I said 'y'. Tony with a 'y'.

MOM: Then the answer is no.

SALLY: It won't even inconvenience you. He has his own car.

MOM: That's supposed to make me feel better? You are not getting in that car with that boy.

SALLY: You are so unfair. Why not?

MOM: Because he can't be trusted.

SALLY: His father is Dad's best friend.

MOM: What better reason not to trust him? I know how your father thinks.

SALLY: That makes no sense.

MOM: You know what makes no sense? Standing here arguing with a fifteen-year-old girl, who thinks she's all that, and hot stuff and sassy enough for a 17-year-old loser with a broken down twenty-year-old car.

SALLY: Mom, I'm 17!

MOM: Well, your brains are only 15. (Mom goes back to looking at the mushroom cloud.)

SALLY: (to audience) Classic Mom. I remember when I was ten. My best friend, Agnes, started taking Taekwondo lessons, and I told my Mom I wanted to do it too.

MOM: (turning back towards Sally) Why do you want to run around on a padded floor like a crazed lunatic and kick your legs in the air?

SALLY: (as a 10-year-old) It's fun! Watch! (She kicks her Mom in the behind and starts laughing and running around doing other martial arts poses.)

MOM: You are an evil child.

SALLY: Why can't I, Mom? Why can't I? All of my friends are doing it.

MOM: They are? That's the best reason not to do it. That's what we call opportunity. What do I always tell you to do when opportunity knocks?

SALLY: You kick its butt! (kick, jump, other moves) That's why I need to do this so I can knock opportunity to the floor. (Mom grabs her ear and takes her to a desk.)

MOM: No, silly girl. Who puts these notions in your head? Don't you understand? If you study your math and go to extra lessons after school while your friends are sweating in baggy clothes, then you will be the one with the best test scores. You will be the one who goes to the best college.

SALLY: (defiant) But I want to do Taekwondo!

MOM: It's Taekwon-DON'T! Not Taekwon-DOO!

SALLY: (spitefully) Well, I DOO not care for math.

MOM: Well, I DOO not care that you DOO not care for. Math! (Mom goes back to looking at the cloud.)

SALLY: I hated sitting at that table, spending all my evenings in additional classes. I used to scream: "No, I don't want to go. I don't care about numbers anymore!" (starts laughing) We certainly did have our rough patches. (looking at her Mom) But I see it now for what it was. If it wasn't for her, I wouldn't be here today with a suitcase packed for college.

(Sally goes back to look at the cloud.)

MOM: (to audience) I wasn't really that controlling, was I? I just wanted to be strong for her. I wanted her to think that she could do anything she put her mind to. She's so smart. So clever. (looking at Sally) I never even finished high school. I wanted a better life for her. But now ... (Back to live action.) Sally, we only have a split second ... let's run for the bedroom and get into the closet.

SALLY: Mom --

MOM: (frantically) Come on, if we run to the kitchen and dump out the contents of the refrigerator, we might both be able to fit inside.

SALLY: Mom --

MOM: Sally, you can never give up. Fight till the end. Promise me that.

SALLY: Mom --

MOM: Run to the basement. Now!

SALLY: (grabbing her arm) Mom, there's no fixing this.

MOM: But we can't just give up.

SALLY: There's nothing we can do. But there is one thing I need to say before it's too late.

MOM: What's that?

SALLY: I love you, Mom.

(Mom starts crying and they hug each other. Then they turn towards the mushroom cloud, still holding hands, put their chins in the air, and are suddenly blown backwards onto the ground.)
```

---

## IC-0696: The Wounded Do Not Cry

- Title: The Wounded Do Not Cry
- Author (byline): Lavonne Mueller
- Work: The Best American Short Plays 2003-2004
- Publisher: Applause Books
- Publication date as stated: Oct 2006
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: VOICE OVER, IRENE, FRANCES, DOCTOR, SHOUTS OF, LT STEIN, FRANCES’ VOICE
- Teaser before the introduction: Yes
- Spoken words (computed): 2123
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lavonne Mueller
Book: The Best American Short Plays 2003-2004
ISBN: 978-1557836960
Publisher: Applause Books
Date (Month/Year): Oct 2006
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Two hours after Lieut. Frances Slanger and other Army nurses waded ashore in Normandy on D-plus-four, they were at work.

ACTRESS 2: They slept on the ground, wore the same clothes four days running. In five weeks of rugged going they helped handle 3,000 casualties.

ACTRESS 1: "We have learned a great deal about our American soldier and the stuff he is made of. The wounded do not cry. Their buddies come first. The patience and determination they show, the courage and fortitude they have is sometimes awesome to behold."

ACTRESS 2: Inspired by the life of Frances Slanger, forgotten heroine of the Normandy invasion:

TOGETHER: The Wounded Do Not Cry by Lavonne Mueller
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

VOICE OVER: Now hear this! Now hear this! The William N. Pendleton U.s. Merchant Marine Ship: All troops to your debarkation areas! All troops to your debarkation areas!

IRENE: Frances ... Frances ... this way. The Forty-Fifth they said is this way.

FRANCES: My legs are itchy from the salt water.

IRENE: Thank heavens my lipstick is wrapped in plastic.

FRANCES: [Pause. Looks back.] Where is everybody?

IRENE: Keep paddling!

FRANCES: Eisenhower said we're embarking on the Great Crusade, Irene.

IRENE: Did he mention that sea water's bad for the hair?

FRANCES: He just said: Send the nurses to Normandy.

IRENE: Be careful, .. the Germans sometimes bulldoze furrows in the water. The depth can drop from chest-high to ten feet.

FRANCES: Ok ... Ok.

IRENE: Don't touch that thing! It's a mine lashed to the top of a pole. My boyfriend told me about these.

FRANCES: Why didn't we learn to dog paddle at Fort Devins?

IRENE: We were too busy learning how to dodge bullets.

FRANCES: I've got Keats under my helmet.

IRENE: It'll take more than any Keats to stop bullets. [They struggle in the water.]

FRANCES: There's ... dead bodies floating by me.

IRENE: Frances, there will be hundreds more to come.

FRANCES: I'm going to help them.

IRENE: Don't touch that boot! Let it go by.

FRANCES: But, Irene ... there's part of a leg still in it.

IRENE: We're only a few yards from the beach. Frances ... Frances ... [Irene grabs Frances and Frances' head comes up out of the water as France spits out water.]

FRANCES: I'm ok. Just gulped a little water.

IRENE: When we hit the beach, we hook up with the men.

FRANCES: Where are the rest of us nurses?

IRENE: Waiting for two slowpokes.

FRANCES: I can't see the beach.

IRENE: It's there. Murky looking from the heat. Now let's go. Double time! [They struggle in the water and then finally fall flat on the beach gasping.] And I dreamed of wearing one of those cute starched white nurse's hats.

FRANCES: My hair's too frizzy to wear under any starched hat.

IRENE: Mine isn't. [Pause.] See anybody?

FRANCES: Not yet. [Pause.] I look good in a helmet. Makes my eyes bigger. [Irene takes off her helmet and we see her hair is in large metal rollers.] You .. .look like ... a Picasso.

IRENE: Is that a good thing?

FRANCES: "Nothing's good or bad but thinking makes it so."

IRENE: Do you have to sound like a poet during this invasion? [Frances screams.]

IRENE: What's wrong?

FRANCES: [Happily.] You called me a poet.

IRENE: It's enough to be a nurse. [We hear artillery shells. Irene puts her helmet on as they both duck down.] Now that's something to scream about. Why did I think this job would be glamorous?

FRANCES: Irene, whoever said war was glamorous?

IRENE: For one, it's that war poet you're always reading. What's his name .... Owen?

FRANCES: I'm not doing this because of him. I'm here to stop the Nazis.

IRENE: Before we do that, I'd like to take down my curlers. [They cautiously look up.]

FRANCES: Where is everybody?

IRENE: Guess we drifted off to the north.

FRANCES: Way down there ... see all that ... driftwood?

IRENE: Don't look, Frances.

FRANCES: Are those ... ?

IRENE: We've got to find the hospital.

FRANCES: Oh, god, what's happening here?

IRENE: We're at the front, Frances.

FRANCES: Are the other nurses dead, too?

IRENE: They're probably hooked up with the men. [Light up on a doctor who is a captain.]

SCENE BREAK (Irene assumes the role of DOCTOR in this scene)

DOCTOR: Girls. Over here! [They walk to the hospital area.]

FRANCES: Where are the other nurses?

DOCTOR: Helping bring in the wounded. Push those two footlockers together. [Irene and Frances push the two footlockers together.]

FRANCES: [To Doctor] For your instruments?

DOCTOR: For my patients. I'll soon be up to my neck in surgery.

FRANCES: This is an operating table?

DOCTOR: Where the hell are you from, little girl?

FRANCES: Boston.

DOCTOR: You want Boston General hospital here? Greenhorns. Why me!

FRANCES: We're both fully qualified graduates of ...

DOCTOR: Yah ... yah. Look for flashlights. Supply dumped them somewhere around here.

FRANCES: Flashlights?

DOCTOR: Need light to operate. Even in Boston, they got to have light. We're expecting 10,000 dead. The dead we don't worry about. Now the hundreds of wounded ...

FRANCES: Hundreds?

DOCTOR: Mangled hundreds. Batteries! Little girls, if there are flashlights, can batteries be far behind? When you get time, hang some lanterns, too. And put up the mosquito netting. I want all the glass syringes boiled. And ladies ..

.if you need the latrine, there's a slit-trench on the left side of our tent. A private will be stationed out there to issue you three squares of toilet paper per visit. [Sound of trucks is heard.]

SCENE BREAK

IRENE: [Fanning herself with a large bandage.] The air's stifling in this tent. [Pause.] Getting any sleep?

FRANCES: I was in surgery all night. [Sound of distant artillery.]

IRENE: [About artillery:] That bother you?

FRANCES: I pretend it's the elevated trains from South Port Station near my house in Boston.

IRENE: The one thing that really gets to me ...

FRANCES: ... when the German planes fly over?

IRENE: Trying to take a bath in a helmet full of rainwater, twigs and worms.

FRANCES: I dream about soap.

IRENE: Oh, I finally got some. From one of the medics who got a package from home. He wanted two bucks for it, but I'm so broke, Frances, did you always want to be a nurse?

FRANCES: Sure. You?

IRENE: In third grade a little boy smashed his finger on the jungle bars. I wrapped my hankie around his pinkie. He looked at me with adoring eyes. I figured ... good way to get a guy's attention. And here I am. What got you going?

FRANCES: A pear. My dad's a fruit peddler in South Boston.

IRENE: No kidding.

FRANCES: I helped him since I was seven. [Pause.] We always took such pride stacking the fruit ... polishing apples to put their cheeks next to steps of golden oranges weaving lace of purple and green grapes along the side. Then a big juicy pear on top. But there were kids who didn't like us, and they'd knock over our cart. Once ... the pear rolled away .. .it's flesh all torn. [She reaches for a stone on the beach as if it were the pear.] I tried pushing all the pulp back together. [She squeezes the stone.] I wanted to make it better ... make it whole again. [She squeezes the stone harder.] I wanted it ... perfect .. .like it was.

IRENE: [Tries to get Frances to release her hold on the stone.] Good lord, Frances, that's a sharp stone. Come on, let go.

FRANCES: Fruit has such a short life .... and crooks had to smash it .... bigots had to kill it.

IRENE: Drop it ... Frances, it's like a knife ... your hand's starting to bleed.

SCENE BREAK

SHOUTS OF: Nurse! Nurse! Nurse! [Irene exits. A pause as Frances drops the stone on the ground and wipes her blood stained hands on the side of her uniform and then goes to the ward of the wounded. She stands in the middle of the stage surrounded by agonizing shouts of Nurse! Nurse! [Frances goes to the cot of one wounded soldier. She takes his temperature.]

FRANCES: Good. You're down to 101 today. [She goes to another cot carrying a towel over her arm.] I'm going to give you a new wonder drug-Pencillin. You'll be up and around in no time. What? Yes. Yes. I've taken care of your friends ... they're fine. No, I didn't let them see the medicine I'm giving you. That's right, we don't want to alarm them. See, I've hidden the syringe under my towel. [She now gives him a shot.] [She goes to another cot with a soldier with a head bandage.] Your bandage needs tightening. Here, I'll just pull this closer. Tonight, I'll come back and read your wife's letter to you. [She goes to another cot.] You must eat. I know C-rations aren't too delicious. But you must eat. Let me put some mash potatoes on your tongue. Take a little ... please ... just a little. Good ... good. That's it. If you taste something sweet you're probably biting into a worm. Not to worry. The worm's cooked long enough to be sterilized. [Chuckles.] [She looks out over all the cots.] I know ... I know ... all of you want banana cream pie. Well I'd give anything to see a fat chicken on a platter for Shabbat dinner, myself. [She turns to the next patient in the next cot as light goes up on Irene.]

IRENE: Frances ... that's a German soldier. They found him on the beach.

FRANCES: Irene, we need more cotton.

IRENE: Frances, I can take care of him for you.

FRANCES: We're winning the war. I can afford a dose of compassion. [To the German soldier:] I'm just pouring sulfanilamide powder on your wounds. It will help fight the infection. [Pause.] What? [She puts her ear down next to his lips.] Yes. Juden. I'm 2nd Lt. Freidel Yachet Schlanger, United States Army Nurse Corps. [She powders his wounds. Frances then turns to another soldier as Irene calls to her:]

IRENE: Frances, where did you get that box of surgical gloves and extra bed pans?

FRANCES: [As she is bandaging a patient:] Doc sent me up the road to the Supply Hut.

IRENE: That's dangerous. The road's plastered with mines.

FRANCES: Doc just said: Look for chickens. If they're clucking and alive, the area is probably safe from mines.

SCENE BREAK

FRANCES: Dear Mama and Papa, I know you are unhappy about me being so far away. But didn't you both leave Poland and travel to America? [Pause.] So you've heard about the Invasion. And they rang the church bells at 3 a.m. in Boston. I'm happy to know my Mama and Papa knelt on our front porch at 3 a.m. in their nightclothes and prayed for us here. [Pause.] I wash soldiers. Give morphine shots. Bandage wounds. Put kidney basins under bleeding chins. [Pause.] They brought in a 20-year-old boy, a bullet in both arms. He wanted me to patch him up in a hurry so he could grab his gun and go back into battle. I tried to calm him ... put cold cloths on his forehead ... rubbed his back ... even as the doctor stood behind him ready to amputate both his arms.

SCENE BREAK (Irene assumes the role of Lt. Stein in this scene)

VOICES OF SOLDIERS Nurse! Nurse! Nurse! [Frances goes to the soldiers.]

FRANCES: [Bending over a soldier on a cot.] A splintered bone has cut an artery, lieutenant.

LT STEIN: Am I.going to live?

FRANCES: I'm pressing my finger on your artery. That stops the bleeding. So, Lt. Stein, where do you come from?

LT STEIN: "Much have I travell'd in the realms of gold."

FRANCES: "And many goodly states and kingdoms seen."

LT STEIN: You like Keats, too.

FRANCES: He helps me dodge bullets ... so I can carry on here ... even write a little poetry.

LT STEIN: [Pause as the lieutenant groans.] Nurse. I know I'm done for. How much longer do I have?

FRANCES: As long as my finger's here, Lt. Stein!

LT STEIN: I know it's bad. I could feel the bullets stitching me down the back.

FRANCES: But you can still speak poetry.

LT STEIN: Why are you here? Somebody like you?

FRANCES: Reading too much Walt Whitman, I guess.

LT STEIN: Sure. Old Walt nursed the wounded in the Civil War. "Every hour of the light and dark is a miracle/every cubic inch of space is a miracle." [A pause as he stares at her.]

LT STEIN: Do you really write poetry?

FRANCES: Yes.

LT STEIN: Recite one. Please.

FRANCES: [Recites:] If Whitman wrapped your head in white flags of bandages he'd soothe that black space in the corner of your soul's face and you could reach peace that Americans sings of each to each.

LT STEIN: [After a pause.] I...like that. You should send it to Stars and Stripes so the troops can read it.

FRANCES: Not too many poetry loving GI's like us, Lt. Stein.

LT STEIN: [Groans in pain.] Nurse ... you can be honest with me ... Whitman to Whitman. I know the score.

FRANCES: "Nothing is good or bad but thinking makes it so." Now we're with Shakespeare, Lieutenant Stein. [The sound of trucks leaving. we see fatigued Frances holding on, her finger pressed stubbornly on the artery. Then we hear heavy artillery fire. Then louder artillery fire. Frances slumps over the soldier, her finger finally letting go as her body goes limp.]

SCENE BREAK

IRENE: [She is holding Frances’ helmet.] After our patients were safely in a new area, we came back for Frances ... and did everything we could for her. But she was hemorrhaging. The doctor and I were unable to stop the bleeding in her stomach. [Pause.] She died at age 31 on October 21, 1944. From enemy fire. A black soldier played taps. And I sent off one of her poems. Stars and Stripes published it. [Voice of Frances as the lights slowly go down.]

FRANCES’ VOICE: A nurse sees wooden bullets
that splinter as they shoot into the skin,
waterproof bullets where the powder's sealed
so even the moisture of blood can't get in.
In the shock ward she sees it all
soldiers writhing in pain and thirst.
But the wounded never cry
their buddies come first.
```

---

## IC-0697: 24: The Ultimate Script

- Title: 24: The Ultimate Script
- Author (byline): Dave Barry
- Work: I’ll Mature When I’m Dead: Dave Barry’s Amazing Tales of Adulthood, Pgs 127-156
- Publisher: Putnam Adult
- Publication date as stated: May 2010
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR, ACTRESS, SHARED, NARRATOR, TOGETHER, THE PRESIDENT, THE VICE PRESIDENT, FBI DIRECTOR, GENERAL, CHIEF OF STAFF, DOCTOR, JACK, CHLOE, FIRST TERRORIST, SECOND TERRORIST, TERRORIST, JACK'S HEAD, JACK BAUER'S VOICE
- Teaser before the introduction: Yes
- Spoken words (computed): 1582
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dave Barry
Book: I’ll Mature When I’m Dead: Dave Barry’s Amazing Tales of Adulthood, Pgs 127-156
ISBN: 978-0399156502
Publisher: Putnam Adult
Date (Month/Year): May 2010
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Personally, I gave up on 24 during the second season, when Jack Bauer's daughter was menaced by a cougar, but the show lasted a blockbuster eight years.

ACTRESS: Or, in show terms, eight days. See each episode only covers 1 clock hour in Bauer’s rather mundane life . . . . Each season shows only 1 24-hour day . . . Eight years=8 days. . . but over those eight days secret agent Jack Bauer had to use a lot of excessive force to save the country.
```

### Performance text (classify this)

```text
Suggested Roles:

ACTOR: Vice President, FBI Director, General, Chief of Staff, Jack, 1st Terrorist,

ACTRESS: President, Doctor, Chloe, 2nd Terrorist

SHARED: Narrator

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

NARRATOR: (Pgs 127-156) 6 A.M. -- THE WHITE HOUSE SITUATION ROOM -- The president, seen only in silhouette, sits at the head of a conference table. Seated around the table are the vice president, the Joint Chiefs of Staff, and various important-looking extras. The lighting is dim.

ACTOR: How much excessive force? He killed TWO HUNDRED SIXTY-SEVEN PEOPLE in eight days.

ACTRESS: In case you haven’t seen the series . . . We’ve prepared a trailer for you. . . 1 hour in less than 10 minutes!

ACTOR: Move over Chuck Norris, the new man of the house is Jack Bauer. This is . . .

TOGETHER: 24: The Ultimate Script by Dave Barry

THE PRESIDENT: I've called you together because we have received intelligence concerning a serious threat that could . . . What is it, Mr. Vice President?

THE VICE PRESIDENT: Why is the lighting so dim?

THE PRESIDENT: For dramatic effect. You'll also notice that many characters in this show whisper for no good reason.

THE VICE PRESIDENT: (peering at the president) Wait a minute. You're a kangaroo.

THE PRESIDENT: Yes. The writers already did an African-American president and a woman president, so this season they were thinking, "Maybe a Jewish president?" And then they thought, "Nah, too unrealistic." So they went kangaroo. . . As I was saying, we have received intelligence concerning a threat that could cause the deaths of millions of Americans.

FBI DIRECTOR: We have reason to believe that a vaguely Middle Eastern terrorist organization has acquired a proton defrackulator.

THE PRESIDENT: What's a proton defrackulator?

FBI DIRECTOR: We have no idea. But it sounds very bad.

THE PRESIDENT: Well, if these terrorists think I'm going to let them kill millions of Americans on my watch just because I have short, thumbless forelimbs, then they have another think coming. General, what do the Joint Chiefs recommend?

GENERAL: We recommend an immediate tactical nuclear missile strike against Boston.

THE PRESIDENT: Is that where the terrorists are?

GENERAL: No, we just hate Boston.

THE PRESIDENT: Fair enough. But we also need to do something about these terrorists.

CHIEF OF STAFF: There is only one man who can stop these terrorists, and that man is Jack Bauer.

THE PRESIDENT: Bauer . . . I know that name.

CHIEF OF STAFF: He's the main character.

THE PRESIDENT: Ah, right. But didn't he end the last season being arrested on trumped-up charges after he was framed by a shadowy cabal of powerful men?

CHIEF OF STAFF: That's how he ends every season.

THE PRESIDENT: So where is Bauer now?

CHIEF OF STAFF: Imprisoned in a secret California prison facility.

THE PRESIDENT: Have him released.

CHIEF OF STAFF: He was also tortured, decapitated and fed to boars.

THE PRESIDENT: Whoa.

CHIEF OF STAFF: Fortunately, he was trained for exactly that.

THE PRESIDENT: Are you saying that he could . . .

NARRATOR: SETTING: THE INFIRMARY OF A SECRET CALIFORNIA PRISON -- Jack Bauer is sitting on an examination table. There are boar bites all over his body and a bandage wrapped around his neck. A doctor has just finished examining him.

DOCTOR: You're going to experience some soreness from having your head reattached to your body. I suggest you take it easy for at least the next hour.

JACK: Give me your phone.

DOCTOR: If you need to make a call, there's a phone in the-

JACK: Dammit, there's NO TIME!

NARRATOR: Jack pulls a gun and shoots the doctor in the thigh. As the doctor falls to the floor, Jack snatches his cell phone and dials a number. The scene shifts to an FBI office in Washington, D.C., where Chloe, sitting at her computer, answers the phone.

CHLOE: Hello?

JACK: Chloe, it's Jack.

CHLOE: Jack? I thought you were decapitated and consumed by boars.

JACK: Not anymore. A terrorist cell is bringing in a proton defrackulator. I need a map showing the port of entry for every international freight shipment in the past thirteen days weighing between fifty-two and sixty-three kilograms, overlaid with another grid showing the locations of all metropolitan areas with populations of twenty-eight thousand or more, overlaid with another grid showing prevailing wind direction and speed, overlaid with another grid showing the location of every odd-numbered Waffle House in North America. CHLOE (tapping keyboard) Sending it now.

JACK: (checks his cell phone) They're bringing the defrackulator into the Washington area.

CHLOE: That makes sense. All the other main characters are here.

JACK: (stepping over the doctor to the exit) I'll need transport.

CHLOE: (tapping) I'll send a helicopter.

JACK: ((runs outside. A helicopter immediately appears overhead) I have a visual. Have the FBI set up a perimeter around Washington, Maryland, and Virginia. Don't let anybody in or out. Shut down the shipping lanes and set up satellite surveillance to detect anybody on the Eastern Seaboard who looks vaguely Middle Eastern.

CHLOE: (tapping) I'm on it.

NARRATOR: Jack runs to the helicopter, shoots the pilot in the thigh, throws him out of the chopper, grabs the controls, and takes off. SETTING: A SEAPORT - Two vaguely Middle Eastern-looking terrorists are watching as a crane lowers a wooden crate from a freighter to the pier.

FIRST TERRORIST: Once the proton defrackulator is loaded into the van, we'll take it to our secret hideout in Washington.

SECOND TERRORIST: Then we will activate it and carry out the plan to kill millions of Americans.

FIRST TERRORIST: You should roll your "r"s, so our accents sound more alike. (pulls out a cell phone and dials a number) I have the floral centerpiece and will deliver it to the wedding reception. (ends the call)

SECOND TERRORIST: Was that a coded message to the terrorist mastermind?

FIRST TERRORIST: No, that was my brother-in-law, the florist. I'm helping him out with a wedding.

SECOND TERRORIST: Let's get going, then. Those millions of Americans aren't going to kill themselves!

NARRATOR: The two men enjoy a vaguely Middle Eastern laugh, shoot the dockworkers, get into the van, and drive away. SETTING: INSIDE THE HELICOPTER - Jack is at the controls. The phone rings. He plugs a Bluetooth headset into his ear.

JACK: Jack Bauer.

CHLOE: Jack, we just got satellite recon video showing unusual activity at the Chevy Chase seaport. Two men took possession of a crate exactly the size of a proton defrackulator, loaded it into a van, and took off. Also they shot all the dockworkers.

JACK: Hmm. Were they swarthy?

CHLOE: (tapping) I'm uploading a photo.

JACK: (looking at phone) Those are terrorists, all right. Do you have a visual on the van?

CHLOE: (taping) Yes. The van stopped at a wedding reception to deliver a floral centerpiece.

JACK: Copy that. Where's the van now?

CHLOE: It's heading toward the Department of Commerce building in downtown Washington on Old Plankton Road.

JACK: Keep me posted. I'm landing at the White House now.

NARRATOR: The chopper lands on the White House lawn. Jack jumps out, shoots a Marine attempting to salute him, and strides into the White House. An instant later he enters the Situation Room.

THE PRESIDENT: Mr. Bauer, thank you for . . . Whoa, are those boar bites?

JACK: There was also an ocelot. I'll be fine.

THE PRESIDENT: Ouch. Anyway, thank you for coming from California in eight minutes. Jack, what do you know about the plot?

JACK: The terrorists brought the proton defrackulator in through the Chevy Chase seaport and are heading into Washington on Old Plankton Road. I'll need a tactical assault team of extras headed by an attractive woman.

THE PRESIDENT: Done.

JACK: Also I may have to blow up the Department of Commerce. Apparently it's a terrorist hideout.

THE PRESIDENT: I wondered what they did in there.

NARRATOR: SETTING: DOWNTOWN WASHINGTON, D.C. - Jack lands the helicopter outside the Department of Commerce Building.

JACK: (into phone) Chloe, I need the building schematics now.

CHLOE: (tapping furiously) Here are the schematics.

JACK: (frowning) According to these, we can enter the building by. . . the door.

CHLOE: Jack, there's something else. I just ran a cross-modulated algorithm series on the HEPCOM database, and for shocking-plot twist reasons that make no logical sense, your son is in that building.

JACK: I have a son?

CHLOE: Apparently this season you do.

JACK: We need to get to the proton defrackulator before the terrorists activate it.

NARRATOR: Jack runs into the building, met in the lobby by a hail of bullets. Many extras go down. Jack pulls a pistol and fires approximately eight hundred shots, each of which kills an enemy gunman. But more gunmen keep appearing. Jack crouches behind a lamp. Tens of thousands of bullets ricochet around him.

JACK: (shouting into a Bluetooth headset) Chloe, we're pinned down by hostiles in the Department of Commerce!

CHLOE: I wondered what they did in there.

JACK: (shouting) I need the location of the defrackulator!

CHLOE: (tapping) It's in the basement, next to the National Aquarium.

JACK: Why is the National Aquarium in the Commerce Department Building?

CHLOE: (tapping) Nobody knows. Jack, there's something else. They've put your son into the octopus tank.

NARRATOR: Through a blizzard of bullets, Jack runs across the lobby, killing people en route. He runs into an elevator, which contains fourteen hostile gunmen. The door closes. As the elevator descends, Jack and the gunmen engage in a fierce gunfight, during which he kills them all. The door opens and Jack stumbles out of the elevator into the basement.

JACK: (shouting into headset) Which way?

CHLOE: (tapping) To the right! Hurry, Jack!

NARRATOR: Jack runs to his right. Ahead is the aquarium tank; inside it, in the grasp of an octopus, is a young man, played by Keanu Reeves. Next to the tank is one of the terrorists, doing something to what looks like a large espresso machine.

JACK: (aiming gun) Step away from the defrackulator NOW!

TERRORIST: You're too late, Bauer!

NARRATOR: As Jack looks toward his son, Chloe's voice shouts in his earpiece.

CHLOE: Jack! Look out behind you!

NARRATOR: Jack starts to turn, but he's too late. The second terrorist leaps from a hallway with a machete and whacks Jack's head off.

CHLOE: Jack! Are you all right?

JACK'S HEAD: (on floor) I'll be fine.

FIRST TERRORIST: (pushing a button) The proton defrackulator has been activated!

JACK'S HEAD: What does it do, anyway?

FIRST TERRORIST: We actually don't know. But we assume it's bad.

NARRATOR: The camera zooms in on the proton defrackulator to reveal a digital timer counting down . . . 15 . . . 14 . . . 13 . . .

JACK BAUER'S VOICE: Following are scenes from next week's 24.

NARRATOR: SETTING: THE WHITE HOUSE SITUATION ROOM

CHIEF OF STAFF: Madam President, Newark is gone.

THE PRESIDENT: Newark, New Jersey, or Newark, Delaware?

CHIEF OF STAFF: What difference does it make?

THE PRESIDENT: Good point! (Everybody enjoys a hearty laugh)
```

---

## IC-0698: The 25th Annual Putnam County Spelling Bee

- Title: The 25th Annual Putnam County Spelling Bee
- Author (byline): Rachel Sheinkin, William Finn and Rebecca Feldman
- Work: Not specified
- Publisher: Music Theatre International (MTI)
- Publication date as stated: May 2005
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTRESS, ACTOR, CONEYBEAR, RONA, PANCH, PANCH AND A SPELLER, OLIVE AND BARFEE, OLIVE, BARFEE, SCHWARZY, AUDIENCE SPELLER 1, CHIP
- Teaser before the introduction: Yes
- Spoken words (computed): 1457
- Already set (do not supply): none

### Source block (context only)

```text
Author: Rachel Sheinkin, William Finn and Rebecca Feldman
ISBN: N/A
Publisher: Music Theatre International (MTI)
Date (Month/Year): May 2005
Perusal Script can be ordered from MTI at https://www.mtishows.com/the-25th-annual-
putnam-county-spelling-bee
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: The 25th Annual Putnam County Spelling Bee ACTOR: by Rachel Sheinkin, William Finn and Rebecca Feldman
```

### Performance text (classify this)

```text
Suggested Roles:

ACTRESS: Rona, A Speller, Olive, Schwarzy, Audience Speller #1, Chip

ACTOR: Coneybear, Panch, Barfee,

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

CONEYBEAR: (Pg 11-12) (Phone rings . . . Leaf Coneybear answers) Hello, Leaf speaking. (with growing excitement) Uh, huh. Uh, huh, Uh, huh! Wow! (puts hand over receiver and yells to his family) Mom! Dad! Marigold, Brook, Pinecone, Raisin, Landscape, Paul – you’re not going to believe this! I made the county finals in the spelling bee! ****Scene****

RONA: [Welcome to the] (Pg 5) 25th Annual Putnam County Spelling Bee (Pg 7) Hello, I’m Rona Lisa Peretti, and I’m pleased to be your host. Unfortunately, our usual word pronouncer, Superintendent Spriggs has [fallen ill]*, so please join me in welcoming back Vice Principal Douglas Panch. *[Ad lib note: “fallen ill” can be replaced with a topical or local reference, ex: “Is quarantined with COVID-19 like symptoms]

PANCH: (Pg 8) (clearly infatuated with Rona) Thank you, Rona, and I would like to say as to the incident 5 years ago, I’m in a much better place now.

RONA: And now for the official spelling bee rules.

PANCH: (Pg 9-10) A speller may ask questions about the word’s pronunciation or definition, and use in a sentence. If you start to spell a word, you may start over,

PANCH AND A SPELLER: but the sequences of letters already spoken may not be changed.

RONA: If you misspell a word, we will ring the bell. (Ding) and the comfort counselor will escort you off stage!

PANCH: So, is that understood spellers?

OLIVE AND BARFEE: Yes

OLIVE: (Pg 7) What school do you go to?

BARFEE: Shut up!

PANCH: (Pg 10) Then, without further ado, let the spelling begin.

PANCH: (Pg 10-11) Miss Schwartzandgrubenierre . . .

RONA: Miss Schwartzandgrubenierre is the head of the Gay-Straight Alliance at her elementary school!

PANCH: STRABISMUS

SCHWARZY: (with a pronounced lisp and other facial and body tics) Strabismus. May I please have the definition of that word?

PANCH: “The inability of one eye to obtain binocular vision with the other because of an imbalance of the muscles of the eyeball.”

SCHWARZY: And use in a sentence please?

PANCH: “In the schoolyard Billy protested that he wasn’t cockeyed. ‘I suffer from strabismus,’ he said, whereupon the bullies beat him harder.

SCHWARZY: Strabismus. S-T-R-A-B-I-S-M-U-S. Strabismus.

PANCH: That is correct . . . Mr. Coneybear.

RONA: Mr. Coneybear (Pg 18) is recovering from headlice.

PANCH: (Pg 12-13) CAPYBARA

CONEYBEAR: What? Is that a word? What does it mean?

PANCH: “A tailless largely aquatic South American rodent often exceeding four feet in length”

CONEYBEAR: Oh . . . can you use it in a sentence?

PANCH: Yes. “Don’t look now, Pedro, but I think that tailless, largely aquatic four-and-a-half foot rodent swimming next to you may be a capybara.”

CONEYBEAR: Wow, that didn’t help at all! C-A-P-Y-B-A-R-A. Capybara.

PANCH: This is correct. . . Miss Ostrovsky.

RONA: Miss Ostrovsky came in second in her school’s Halloween contest.

OLIVE: I was road-kill!

PANCH: (Selected from Audience Volunteer Words – Appendix #2 and instructions on page 16) APOOP

AUDIENCE SPELLER 1: (Pg 11) Can I have a definition

PANCH: (from Appendix #2, Pg 85) “Toward the back; to move astern on a boat”

AUDIENCE SPELLER 1: Could you use it in a sentence?

PANCH: (from Appendix #2, Pg 85) “Guido, the seasick Italian sailor said, ‘Scusa me, boys, but I’m-a-gonna go apoop.”

AUDIENCE SPELLER 1: Apoop. A-P-O-O-P. Apoop.

PANCH: (Pg 19-21) That is correct . . . Mr. Tolentino

RONA: Charlito “Chip” Tolentino is a little league pitcher with a wicked 22-mile an hour screwball!

PANCH: OMPHALOSKEPSIS

CHIP: Wait a second, didn’t the [last girl] just get APOOP?

PANCH: Yes, and you got: Omphaloskepsis.

CHIP: Can that also be pronounced “omPHAloskepsis”?

PANCH: It can . . . . It would be WRONG.

CHIP: Omphaloskepesis. O . . M . . . P . . . H. . . A . . L-O-S-K-E-P-S-I-S. Omphaloskepsis.

PANCH: That is correct.

RONA: He rallies and nails it. That’s what it means to be a champion!

PANCH: Mr. Coneybear . . . (Pg 23) CRAYON . . . That’s correct.

CHIP: Come on!

SCHWARZY: (Off stage) Damn it!

PANCH: (Pg 17) Mr. Barfee

BARFEE: It’s Barfee

RONA: (Pg 33) Mr. Barfee made it to the finals last year, but had to be eliminated for health related reasons.

BARFEE: (momentary flashback, a horrified BARFEE in the midst of an allergic reaction) Were there peanuts in the brownies? Cause they said there wouldn’t be no peanuts in the brownies!

PANCH: (Pg 17-18) LUGUBRIOUS

BARFEE: One moment please.

RONA: Okay watch this technique – He calls it the Magic Foot, and he’s the only one I’ve ever seen use it. (Barfee enacts) He spells it out on the floor so he can get a visual an then speaks it outloud.

BARFEE: Lugubrious. L-U-G-U – Lugu! B-R-I-O-U-S – Lugubrious.

RONA: Incredible!

BARFEE: I know.

PANCH: (Pg 10) Miss Schwartzandgrubenierre . . . (Selected from Audience Volunteer Words – Appendix #2 and instructions on page 16) DENGUE

SCHWARZY: (attempts a couple of pronunciations) DENGUE? DENGUE? May I please have the definition of that word?

PANCH: (from Audience Volunteer Words – Appendix #2, Pg 88) “A disease transmitted by mosquitoes that causes headache and severe diarrhea.

SCHWARZY: And use in a sentence please?

PANCH: (from Audience Volunteer Words – Appendix #2, Pg 88) When the pediatrician asked Billy to describe the symptoms of his dengue, he said, “It’s like there was a race out of my Tushy and everybody won.”

SCHWARZY: D-E-N-G-U-E. Dengue

PANCH: That is correct. . . Mr. Tolentino . . .

RONA: Chip (Pg 53) has a sea anemone circus in his basement!

CHIP: (Pg 32) (distracted by a beautiful girl) Leaf . . . that girl in the second row in the fuzzy sweater? Is that your sister? (Pg 36) Marigold . . . Marigold Coneybear . . .

PANCH: Mr. Tolentino . . .

CHIP: (caught up in his fantasy) Sorry- Um . . . can you maybe skip me and ask me two later?

PANCH: Why would you want to do that?

CHIP: I’d rather not say? (awkwardly covering his zipper region)

PANCH: (Pg 37-38) You can either take your turn now or forfeit.

CHIP: I’ll take my turn now

PANCH: TITTUP. The word is TITTUP.

CHIP: (Chip giggles, then squelches it) Definition please

PANCH: It means “lively movement or behavior. It refers to the sound of horse’s hooves – tittup, tittup, tittup. (he demonstrates a little gallop while he repeats the words)

CHIP: Tittup. T . . I . . T (winks and points at Marigold in the audience) U – Oh wait. Two T’s. Backing up, T-I-T-T-U-P. Tittup. (Ding)

PANCH: I’m sorry. The correct spelling is T-I-T-T-U-P. If you start to spell a word you may start over . . .

RONA and PANCH: but the sequences of letters already spoken may not be changed.

CHIP: That’s not fair. It got it right. I can’t get out on a word I spelled right. I won last year!!!

BARFEE: (Pg 44-45) (Jeering) See you next year! (Chip makes a motion toward him) You could be disqualified for that – if you hadn’t already been eliminated!

CHIP: You know something, Barf: I may have lost, but you are the biggest loser here! (stomps off)

BARFEE: Oh yeah? Well, that is a common misperception

OLIVE: Sorry about that – William, right? I’m Olive.

BARFEE: I know your name. Look, I do not need pity from a person named after a vegetable.

OLIVE: It’s a fruit.

BARFEE: Well, it’s a disgusting fruit! (hurt, she begins to walk away) I guess it’s okay for a name though.

OLIVE: Did you know that if you switch the first two vowels in “Olive” it becomes “I love”?

BARFEE: Did you know that if you switch the first two vowels in “William” it becomes . . . “William”?

OLIVE: Oh . . . Well, you’re a really great speller.

BARFEE: Yeah? Thanks! (Olive exits) “Olive.” “I love.” – That’s so . . . (makes an exasperated sound)

RONA: (Pg 45-46) Ladies and gentlemen . . . Our final spellers! Leaf Coneybear, Mr. William Barfee, Miss Olive Ostrovsky and Miss Logainne Schwartzandgrubenierre.

SCHWARZY: I’d like to take one moment to thank my two fathers who’ve been so supportive of me. Thank you, dads!!

PANCH: (Pg 49) Please spell INDICANT

SCHWARZY: Indicant. I-N-D-I-C-A-N-T

BARFEE: P-A-L-A-V-E-R

OLIVE: H-A-L-L-U-X

PANCH: (Pg 27-28) ACOUCHI

CONEYBEAR: A-what? (beat) At a spelling bee?! What’s it mean?

PANCH: “A South American rodent of the genus Myoprocta, resembling an agouti”

CONEYBEAR: It’s funny how I keep getting South American rodents.

PANCH: (Deadpan) Hilarious.

CONEYBEAR: (Pg 29) A-C-O-U-C-H-I. Acouchi.

PANCH: That is correct.

SCHWARZY: (Pg 51-53) (Rapid pace) Part of speech PANCH: That is correct.

OLIVE: From the tupi? BARFEE: Yes, of course. RONA: That is correct.

PANCH: That is correct. RONA: That is correct. PANCH: I’m sorry, that is incorrect.

CONEYBEAR: (Gasps!) It is? (deflated he exits) Apple juice please!

PANCH: (Pg 67) Miss Schwarzandgrubeniere. Vug

SCHWARZY: Vug? That’s the whole word?

PANCH: Vug.

SCHWARZY: Vug. V-U-G-G-H-E. Vugghe. (Ding)

PANCH: I’m sorry, the correct answer is V-U-G. Vug

SCHWARZY: (near tears) So simple? (she exits)

RONA: (Pg 68) How exciting! Will the final two spellers please step forward. (Olive and Barfee step forward)

PANCH: (Pg 71-72) Miss Ostrovsky – Elanguescence.

OLIVE: Elanguescence . . . (Olive freezes)

BARFEE: Hey Olive, don’t think I’m distracted by your eyes and your smile and your hairdo . . .

OLIVE: (looking at Barfee, she misses on purpose) E-L-A-N-G-U-E-S-S-E-N-C-E (Ding)

PANCH: That’s incorrect.

RONA: No speller can win on another’s speller’s mistake. Mr. Barfee must spell the next word correctly to take the Putnam Bee!

PANCH: William. Spell Weltanschauung.

BARFEE: Of course, Weltanschauung. (doing his foot spelling technique) W-E-L-T-A-N-S-C-H-A-

(He freezes)

OLIVE: (Pg 73-74) Mama, I made a friend. I am fine with second.

BARFEE: S-C-H-A-U (he looks over at Olive)

OLIVE: It’s okay, Barf.

BARFEE: U-N-G Weltanschauung

PANCH: We have a winner! (Pg 75) On behalf of our sponsors, we’d like to present you with this two-hundred-dollar savings bond toward your future education.

BARFEE: All my life I have only been able to breathe through one nostril and today is NOT an exception!

OLIVE: (Pg 76) Congratulations!!!

BARFEE: (said with affection) Shut up! **** Epilogues****

PANCH: (Pg 76-78) Vice Principal Panch found a new passion in life -- Rona Lisa Peretti. After courting her tirelessly for over two years, she took out a restraining order on him.

RONA: Rona Lisa Perretti left Putnam County and traveled the world to bring competitive spelling to the less fortunate. She fell in love with an indigenous cashew farmer . . .

CHIP: Chip Tolentino made it through adolescence!

CONEYBEAR: Leaf Coneybear has cats!

SCHWARZY: Logainne Schwartzandgrubenierre won the 31st annual Putnam County Spelling Bee. She went on to become Secretary of Education under President [ insert president’s name here] (dropping her lisp) Her speech therapy was successful!

BARFEE: William Morris Barfee grew up to be incredibly handsome!

OLIVE: Olive Ostrovsky grew up to be the host of her own radio talk show, where every year she interviewed the runner-up of the Putnam County Spelling Bee.
```

---

## IC-0699: 26 Pebbles

- Title: 26 Pebbles
- Author (byline): Eric Ulloa
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: Oct 2017
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR, ACTRESS, JENN, MIKE, SUPERINTENDENT MESSAGE, ACTOR 6, DARREN, CAROLE, FATHER, MICHAEL, PRESIDENT OBAMA’S SPEECH, RABBI, CARRIE, ACTOR 2, ACTOR 3, ACTOR 4, GEORGIA, ACTOR 5, ACTOR 1, STARR, FATHER WEISS, BILL, SALLY, JOE, CARLA, JULIE, YOLIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1546
- Already set (do not supply): none

### Source block (context only)

```text
Author: Eric Ulloa
ISBN: 978-0573706646
Publisher: Samuel French, Inc.
Date (Month/Year): Oct 2017
Background Reference:
https://www.history.com/this-day-in-history/gunman-kills-students-and-adults-at-newtown-
connecticut-elementary-school
Another selection based on the Sandy Hook Shooting is Choosing Hope by Kaitlin Roig-
DeBellis and Robin Gaby Fisher
CUTTING STORED IN THE VAULT: Kaitlin Roig-Debellis is the first-grade teacher at
Sandy Hook Elementary School who saved her entire class of fifteen six- and-seven-year-olds
from the tragic events that took place on December 14, 2012, by piling them into a single-
occupancy bathroom within her classroom, mere feet from the brutal and indiscriminate
massacre taking place outside the door. Since then, despite the unimaginably painful
experiences she endured, she has chosen to share her experience with others, in the hope that
they too can find light in dark moments.
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: On December 14, 2012, Adam Lanza killed his mother, then walked into Sandy Hook Elementary School and killed twenty-six innocent souls before taking his own life.

ACTRESS: These twenty-six innocent deaths, like pebbles thrown into a pond, created ripples and vibrations that were felt far beyond the initial rings.

ACTOR: This is the story of those vibrations.

ACTRESS: Playwright Eric Ulloa conducted interviews with members of the community in Newtown and crafted them into an exploration of gun violence and a small town shaken by a horrific event.

TOGETHER: 26 Pebbles by Eric Ulloa
```

### Performance text (classify this)

```text
Suggested Roles --

ACTOR: Mike, Actors 2, 3, 4, 5 and 6, Darren, Father, President Obama’s Speech, Rabbi, Father Weiss, Bill, Joe

ACTRESS: Jenn, Superintendent Message, Carole, Carrie, Georgia, Starr, Sally, Carla, Yolie

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

JENN: (Pg 13) Communities like ours don’t just form themselves. A true sense of community comes from strangers wanting to come together and know one another for the greater good of their neighborhood. And we need more of that nowadays, right?

MIKE: You know on [December 13, 2012], you didn’t know where Newtown was or that we had a flagpole, or a creamery, or a parade. Obscure was nice.

JENN: He’s right. Obscurity was nice. (Pg 14) They say the world is connected through six degrees, but out here in Newtown, it’s about one. And if you were born and raised here, everyone is family. (PG 20) There are a lot of people from other areas that moved here. [See] Newtown was written up as one of the top ten places to raise kids.

SUPERINTENDENT MESSAGE: (Pg 22-23) All Newtown public schools are in lockdown due to a shooting.

MIKE: I hear sirens from a distance, like rally far out. We were walking back to the office and at the Subway there were four teachers. I intercepted them and I said, “What’s going on?” And they were in shock and tears. And they said, “Something very very bad. Gunshots. Many gunshots.”

ACTOR 6: All clergy go down to the firehouse immediately. All clergy down to the firehouse immediately!

JENN: I got a call saying, “You can pick up your kids at the school, at the firehouse.

MIKE: It’s as if somebody open the floodgates right in that moment, and every personnel, police, you name it, first responders in the world was coming.

JENN: (Pg 25) I, I just can’t even describe how panicked it started to get for me because [my husband] wasn’t answering his phone and the texts were flying. “Do you have him?” Where’s our son? What’s going on?” An I was just leaving him these messages and starting to get that rising panic inside.

DARREN: They said the shooter inside was dead. They said, they, uh, he was (Sniffles) He was found dead in a classroom, found in a classroom. I knew that was the worst case. Shoot . . . shoot . . . shooter killing himself. I – I knew he didn’t just walk in and shoot himself in front of the kids. (Sniffles) And the numbers, we just watched in horror, as it went from a handful . . .to a dozen . . . twenty. (Beat)

CAROLE: (Pg 29-30) The safety of this little town has been shattered. I think that’s the biggest thing that happened her, the shattering of the illusion of . . . our little world. How did this happen to us? What? What just happened here?

FATHER: Don’t get me wrong, I think the story needs to be out there. But I’d never seen anything like it in my life. I mean there were literally hundreds and hundreds [of reporters] there in just the first few hours.

CAROLE: Horrible. Invasive. There was no escape and there was no time for us to grieve. We would all be watching everybody and when somebody went down . . . I mean at the grocery store people would, would go down to their knees and there was a hive of people l that would be there to just let them cry. You know? And you can’t, you can’t do that with the media because it’s so intrusive. They just want – many they want you sobbing. They want to see you in pain.

DARREN: (Pg 31) There’s no place within Newtown or Sandy Hook that you could go It took us to get from our house to Sandy Hook normally, maybe five minutes. The first couple of weeks you’d have to allow at least an hour to get into town because of the traffic jams. People, news truck(s) – Because the highway sign says “Newtown,” people pull off the highway just to see. Just to see.

JENN: (Pg 32) The next week was just funerals and wakes and – it was – it was pretty indescribable. (Responds to the flashes from numerous cameras)

MICHAEL: (Also responding to camera flashes – he yells at the press) Please! Just, just let us mourn.

PRESIDENT OBAMA’S SPEECH: (Pg 33) . . . And that’s what should drive us forward in everything we do. God has called them all home. For those of us who remain, let us find the strength to carry on, and make our country worthy of their memory.

JENN: How could any God let something like that happen?

RABBI: (Pg 36) This was not an act of God, this was an act of man. You got free will and that means that anything could happen. Adolf Hitler can happen. Senseless deaths and shootouts and hold-up and robberies can happen and do happen every day in this country.

CARRIE: He did this, it wasn’t God’s doing. He chose to do this. But I guess my questions are, well, if he had a mental illness then it isn’t really free will. He can’t help it right? Then my daughter asks me, “Is he in hell?” And we tried to explain: “Well, you know, he was probably sick and he didn’t know what he was doing.” And then she would ask, “Well if he was sick then that means he wasn’t an evil person, so would God forgive him? What if he’s sorry? Does he still have to go to hell?” These are questions that we as adults don’t have the answer for. What does a parent do?

(Actor drops character and delivers the following lines straight to the audience simultaneously with Actress Lines)

ACTOR 2: (Pg 37) In the shooter’s home, JENN: (Pg 37) I’m – I’m angry. Obviously there police found the following was a lot more to this story in terms of his

ACTOR 3: A seven-foot pole, with a blade on upbringing . . . Just the lack of care that he one side and a spear on the other. probably received as a child. Did nobody say

ACTOR 4: A metal bayonet anything?

GEORGIA: (PG 38) Not that I’m blaming any

ACTOR 5: Three samurai swords one persons, but the village raises the child. I

ACTOR 6: .323 caliber bolt-action rifle think one of the biggest problems was his

ACTOR 1: .22 caliber Savage Mark II rifle isolation. We’re meant to be connected. And when someone’s not connected . . . bad things start to happen.

ACTOR 3: New articles on the 2008 shooting STARR: (Pg 39) [He] had counseling just at Northern Illinois University before the divorce. Three months prior to this incident, he was fine, then he was disturbed

ACTOR 6: And inside his gun safe was a that his Dad and brother moved. He had holiday card from his mother, [with] a check nobody else to talk to. And that just . . . for the purchase of his next firearm. snapped the camel’s back.

STARR: (continues) When he was on medication and in therapy, he was the one who would take his shirt off his back to help you. He did tutoring for the younger.

FATHER WEISS: I always have twenty-eight candles out. I believe in forgiveness. And that is one of the big issues. Is it twenty-six or twenty-eight?

CAROLE: (Pg 40)The thing is, and maybe it’s not appropriate, but twenty-eight people died that day. It wasn’t twenty-six, it was twenty-eight people who lost their lives. Twenty-eights families that mourned.

BILL: There is no difference between a man who’s being chased by someone with a machine gun, and a man who THINKS he’s being chased by someone with a machine gun.” And the sad part is that he was over eighteen years old, and legally there’s not a thing we could do. We’re no different from Mrs. Lanza.

SALLY: I think that his mother did everything she possibly could. There is a point where you are scared, you’re afraid, but it’s your son. And you have hope because he’s not a monster, he’s mentally ill. Some people honestly just don’t know the difference between right and wrong.

JOE: (Pg 41) The only thing any asshole does, is that he succeeds in becoming infamous. And . . And he will become a mark in a history book, if we let him. How do you bury people like that so people forget them? Because that’s what you need to do. You need to forget them.

CARLA: (Pg 42) There were these people demonstrating outside the National Shooting building. It’s a resource for people who hunt and it’s a very positive organization, and it’s been here for decades. So people were outside it saying . . .

RABBI: (Pg 43) (Leading this protest) “GET OUT OF NEWTON! GET OUT! GET OUT!” We live in a society of 32,000 deaths by guns alone every year! IF these people died in the battlefields of Afghanistan, we wouldn’t accept it. Yet when it happens right here in the cities of America, we somehow are mysteriously silent.

CARLA: I was just begging, begging for them to stop, stop making – stop perpetuating this hate. There’s so much division now, and it’s very strange, ‘cause it’s like (snaps fingers) overnight.

(Beat)

DARREN: (Pg 45) We don’t know all the things that are broken. We’re still discovering them.

JULIE: (Pg 44) They seem to be okay for a while, then my son started to show signs of Post Traumatic Stress Disorder, PTSD. You just have that fear of not being safe. So kids, children, end up just being scared. They weren’t scared of monsters before? Now they’re scared of monsters.

JOE: (Pg 53) This all leaves you with a lot of questions, and I don’t think that’s a bad thing. The more people are questioning, the more they’re talking about it. “Where do we go from here? What can we learn from this? That’s so cliché, but it’s true. What can we learn from this?

YOLIE: It’s all about how you ripple out, and what these vibrations can be. We are love. We are Newtown. That message says it all.
```

---

## IC-0700: 2B (or Not 2B)

- Title: 2B (or Not 2B)
- Author (byline): Jacquelyn Reingold
- Work: Laugh Lines: Short Comic Plays
- Publisher: Vintage
- Publication date as stated: 2007
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: FRANNY, BEE
- Teaser before the introduction: Yes
- Spoken words (computed): 1351
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jacquelyn Reingold
Book: Laugh Lines: Short Comic Plays
ISBN: 978-0307277138
Publisher: Vintage
Date (Month/Year): 2007
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: (In the manner of . . .The Twilight Zone) A story of a woman living a life that is not-so-great and what happens when she is offered the opportunity of a lifetime: to be Queen Bee. 2B (or Not 2B) by Jacquelyn Reingold
```

### Performance text (classify this)

```text
(FRANNY, upset, disheveled, in her studio apartment, on the phone, She talks fast.)

FRANNY: I know you told me it was over and I respect that. I mean, I understand it and I know you don't want to see me again and I know I was not very nice to you at times, and I just want to say that I've had a-well, a complete not-niceostomy and a total unlike-ectomy, I've had all the not-nice unlikable parts removed, so if you call me, I'm sure we can work it out. (She hangs up. She cries. She dials.) I can't believe you haven't called me back. I heard you asked out my friend Eleanor. Okay, well, thanks for breaking my heart. And I still really love you and if you want to change your mind and give it another try, let me know. (Hangs up. Cries.) (A human-size bee appears.) AHH!! (She hides her head; she looks.) Ohmigodohmigodohmigod!

Actors freeze then The BEE steps out of scene for the following introduction

FRANNY: (She tries to hide. The bee is huge. There's nowhere to go. She runs into a corner.) Ohmigod. Okay. Could you just go? Please. Urn. Shoo. Go. (He doesn't budge.) Look, the park is a few blocks away. If you could just fly over there, I'm sure you'd be happier. (He doesn't move. She crouches to the floor or hides under the bed.) Or in the back, there's a garden. With, uh, plants. Or my neighbor downstairs, she has these window boxes: geraniums, impatiens. I'm sure you're in the wrong place.

BEE: Is this 2B?

FRANNY: What?

BEE: 2B or not 2B?

FRANNY: It's a joke, right?

BEE: I wouldn't make a joke like that.

FRANNY: Okay, this is 2B, but I'm sure it's the wrong building.

BEE: 344 West 188 Street?

FRANNY: (Grabs her bag and tosses it at the bee.) Okay, take whatever you want. I only have ten dollars, but I'll write down my PIN number. My bank's on the corner, you can have it all.

BEE: I don't want your money.

FRANNY: Then take the TiVo. Or the organic honey, okay?

BEE: I don't want that.

FRANNY: Look, I'm possibly allergic. And my EpiPen will not be of much use in this case, , cause you are ohmigod so big. You are the biggest bee I have ever seen. I can't believe this is happening.

BEE: [Frank]'s a jerk. Forget about him.

FRANNY: What?

BEE: You deserve better.

FRANNY: Well, thank you, I will consider that. Now please, go away. Or I'll call the police.

BEE: I don't think they'll come for a bee.

FRANNY: I am really afraid of you. I mean, really afraid. Bees are my ... well, thing. You know, some people it's snakes or heights or whatever, but me, it's bees.

BEE: Why would I hurt you?

FRANNY: I don't know. Because you're a bee.

BEE: Have you been hurt before?

FRANNY: Yes.

BEE: Yellow jackets.

FRANNY: No, bee. Bees. I've been stung. So I am sure you are in the wrong apartment.

BEE: It's the right apartment.

FRANNY: Then it's the wrong species. I'm a human, a female human, and you're not invited.

BEE: How's that going for you?

FRANNY: What?

BEE: Being a female human?

FRANNY: It's fine. It's just fine.

BEE: Work and love, it's all good? How's your job? (FRANNY sneaks toward the window while talking.)

FRANNY: Fine. I'm a receptionist. It's a career change. I used to be a painter. Very cutting edge, I didn't even use paint, I used body fluids. But um, it didn't work out because several others already claimed that niche. You wouldn't believe what some people do with their menstrual blood. So now I, uh, have a job and a boss and uh- (She can't get out the window.)

BEE: And your human female love life? (FRANNY crawls all around the room, heading toward a certain cabinet while talking.)

FRANNY: Well, my first relationships were with typical self-involved commitmentphobes when I was between the ages of, say, five and twelve. Then junior high was alcoholics; high school was drug addicts; college, gay men, a guy who owned a duck, then a physically challenged interpretive ice skater, meaning you know an amputee who'd skate with a kind of stick with a blade at the bottom. Then I married a guy who liked to put garlic in his ears, but I went away a lot with my boyfriend, who was a puppeteer for the blind. (FRANNY has snuck around to her cabinet, pulled out a can of bug spray, and points it at the bee.) Okay, get out. Or I will spray you with this deadly spray.

(She sprays. The can is empty. She shakes, tries again, nothing.) Damn. (She runs for the door. It won't open.)

BEE: You like flowers, don't you, Franny?

FRANNY: How do you know my name?

BEE: Do you know how intoxicatingly beautiful you are?

FRANNY: Now, that's a joke.

BEE: We find you unbearably sexy.

FRANNY: Who's we?

BEE: We know you haven't even begun to tap into your [womanly] capacity.

FRANNY: What's that smell?

BEE: That's my nectar.

FRANNY: Mmm. Not bad.

BEE: Franny Dambrose, you are wonderfully demanding, fascinatingly moody, exquisitely impossible to please.

FRANNY: Well ...

BEE: Complicated, codependent, and controlling. Perfect in all ways.

FRANNY: Well ...

BEE: We want to give you everything you always wanted, but thought you couldn't have: love, fulfillment; we will serve your every need.

FRANNY: Well ...

BEE: We want you to be our Queen.

FRANNY: What?

BEE: We've watched you. We've chosen you. We know you.

FRANNY: What is this?

BEE: You can run, but you can't hive. We even have a sense of humor.

FRANNY: Hardly.

BEE: Just think: You wouldn't have to work. You'd have plenty of time: to read, to lounge, to do your art. Think what you could paint with pollen.

FRANNY: That's very nice of you, but hey, why don't you get, um, a real bee? I know you could find one in, um, the park.

BEE: We had a bad experience. She was a ... killer. So we've opted for this scientifically advanced entomologically evolutionary revolutionary solution. We find a very special human female and offer her a better life. Works well for all involved.

FRANNY: If it works so well, what happened to your last one?

BEE: She fell in love with a wasp. Not recommended. The children will be confused.

FRANNY: Okay.

BEE: Franny, imagine yourself as Queen. You'd never be alone again on a Friday night. You'd be serving the greater good by helping to cross-pollinate. Not to mention, we will please you in every way.

FRANNY: Well, urn, look, it's nothing personal, but I find you, I'm sorry to say, physically, uh, repulsive.

BEE: Oh, I think that could change.

FRANNY: And I'm human.

BEE: That too can change. Amelia Earhart? She didn't disappear. She made a choice. So can you.

FRANNY: But what's wrong with being human?

BEE: Have you read the paper lately? Your species isn't exactly living up to its potential.

FRANNY: Amelia Earhart?

BEE: I don't want to rush you, Franny, except that my brothers and cousins are eagerly waiting and time is quickly running out. Don't you want what I've offered? What is it you're reluctant to give up?

FRANNY: Well, my apartment.

BEE: A studio in Inwood?

FRANNY: It's near the subway.

BEE: You'd have your own hive.

FRANNY: My job.

BEE: That job sucks.

FRANNY: And there's Frank.

BEE: Frank is a fly, a gnat, a roach. Besides, he's an actor. Forget Frank.

FRANNY: Believe me, I've tried.

BEE: Franny, oh, Franny, have you looked at your life lately?

FRANNY: I prefer not to.

BEE: All of your qualities that absolutely don't work as a female human will work like gangbusters as a bee.

FRANNY: Things'll get better.

BEE: How long have you been saying that?

FRANNY: Time heals all wounds.

BEE: Weren't you the queen in your grade school play? Didn't you enjoy it?

FRANNY: I loved it. But I didn't get to keep the crown. I wanted that crown.

BEE: You could have a crown.

FRANNY: But still, I'm terrified of you. I see a bee, I flee. It's a kind of a flight-or-flight kind of thing. I don't go on picnics, I avoid practically the entire outdoors because of you.

BEE: What exactly are you afraid of?

FRANNY: Pain, death, dying alone, that sort of thing.

BEE: Touch my stinger.

FRANNY: What?

BEE: Touch it.

FRANNY: No.

BEE: Don't you think it's time to change?

FRANNY: That's a pretty big change.

BEE: I know you, Franny Dambrose. The reason you're afraid of me is because you are me. In your heart, you're a bee. Touch it. (She touches it, pulls her hand away twice. Touches it.)

FRANNY: Oh. Oh. It's-it's nice.

BEE: Isn't it?

FRANNY: And that smell. Your ... nectar.

BEE: Yes. (A musical humming is heard. Lights change.)

FRANNY: That sound. What is it?

BEE: My cousins and brothers. Here to serve you.

FRANNY: Oh my. (She begins to transform into a be – Wings, antennae.) I feel ... different. What's your name?

BEE: Dave the Bee.

FRANNY: Hi, Dave. (The phone rings.)

BEE: Let it ring. It's time.

FRANNY: But ... What if it's Frank? (She answers the phone.) Hello? Frank? (The lights change. The humming stops.) I'm glad you called. What? You want me to stop calling? You're really happy since we broke up? You're still seeing my friend, Eleanor? You've asked her to marry you? Great. That's just great. (As FRANNY is about to burst into tears and launch an attack, Dave puts a crown on her head. Voila. She is transformed. She nearly drops the phone.) Frank, remember the Don't Bee and the Do Bee? Well, you are most definitely a Don't. And when it comes to you and your kind, I am done. Buzz off! (She hangs up.) Okay, boys, let's fly.
```

---

## IC-0701: Ace Lacewing: Bug Detective

- Title: Ace Lacewing: Bug Detective
- Author (byline): David Biedrzycki
- Work: Not specified
- Publisher: Charlesbridge
- Publication date as stated: July 2005
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR, ACTRESS, ACE, MAYOR, XERCES, SGT ZITO, MAGGOT, TWIG, ROACH, DRONE BEE, MANTIS, UNIDENTIFIED DRONE, PRINCESS POLLEN
- Teaser before the introduction: Yes
- Spoken words (computed): 1690
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Biedrzycki
ISBN: 978-1570915697
Publisher: Charlesbridge
Date (Month/Year): July 2005
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: He’s tall, he’s handsome and he has two antennae. ACTOR: He’s Ace Lacewing, Bug Detective by David Biedrzycki
```

### Performance text (classify this)

```text
Suggested Roles

ACTOR: Ace; Maggot, Mantis

ACTRESS: Mayor, Xerces, Sgt Zito, Twig, Roach, Drone Bee, Unidentified Drone, Princess Pollen

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

ACE: It was a night like any other night in the city. Hot and sticky. Great weather if you’re a bug. Everyone’s a bug in Motham City. Some good, some bad. Bad bugs are my business. I was in my office eating some aphid lo mein when the phone buzzed. I answered it. (On Phone) Ace Lacewing, Bug Detective.

ACE: (To audience) It was Mayor Buzzbee. Behind him it sounded like a beehive of activity. Actually, it was a beehive. (On phone) What’s the buzz?

MAYOR: Ace! I’m at the Hive Rise with Princess Pollen. Queenie Bee’s been kidnapped. Get over here now!

ACE: (to audience) Queenie Bee kidnapped? Who would do a thing like that? Everyone loved Queenie and her sister Princess Pollen. The Hive Rise Honey Company made the best honey in town. Maybe someone thought it was too good . . . I was just about to fly out the door when I saw her standing there, like a moth drawn to a flame. Actually I was her flame. But she was no moth. She was the lovely rare butterfly, Xerces Blue. Doctor Xerces Blue. Not the kind of doctor who takes your tonsils out. The kind of doctor who studies bugs – dead bugs. (To Xerces) No time now. The mayor needs my help. (To audience) But those eyes weren’t taking no for an answer.

XERCES: Oh, Acie. How about dinner at my place tonight? Just you and me. I’m making your favorite – aphids a la mode.

ACE: (To audience) How could I resist? Aphids have been my favorite ever since I was a little larva. But I also liked honey. Which reminded me . . . (To Xerces) The aphids will have to stew, sweetheart. Queenie Bee’s in a honey of a jam.

Downtown the traffic was crawling. That’s what traffic does in Motham. It really crawls.

SGT ZITO: Hey, Ace!

ACE: (To audience) It was Sergeant Zito, a mosquito. And a cop. I’ve known him ever since we were pupae at the same school. (To Zito) Whadda ya know, Zito?

SGT ZITO: We have a couple of witnesses, Ace. But none of them are talking except this little maggot.

MAGGOT: I saw the whole thing! I was crawling around minding my own business when all of a sudden I heard all this screamin’. I thought maybe it was a damselfly in distress. But then I looked up and I saw ‘em right outside the Hive Rise – a couple of hooded bugs running off with Queenie Bee!

SGT ZITO: (leaning into Ace and whispering) Ace? You believe this maggot? How could he have seen anything? He doesn’t have any eyes.

ACE: (To audience) I frowned. (To Maggot) Which way did they go?

MAGGOT: Whadda I look like, a tour guide?

ACE: (To audience) I should have known better than to ask directions from a bug with no arms or legs. I told Zito to start rounding up suspects. I looked around . . . and noticed a suspicious trail of honey leading away from the crime scene. I followed it.

At the corner of Tomato and Vine, I stopped in my tracks. The honey trail led to the Beetle Zoo. Lacewings have lost their heads to beetles. But I was on a case, and there was a plate of hot aphids waiting for me at the end of it. The trail went through the broken gate, and so did I. The honey led past the giraffe weevils. (Stooping to exam the honey trail) It was Hive Rise Honey, all right. Still warm. (In words and actions) I heard a noise, stood up, and froze!

Someone had let the tiger beetle out of his cage, and this guy didn’t want to play! He wanted to eat. I did the only thing a bug detective worth his wings would do. (Scream) I screamed and ran . . . smack into a wall. (Pantomime hitting a wall) I heard a familiar flutter of winds, and then the world went to sleep. (Passes out) . .

TWIG: Wake up, Ace.

ACE: My head spun like a whirligig in a whirlpool. I tried to stand up and found myself face to face with a stick. A walkingstick.

TWIG: You don’t look too good, Ace. But if Xerces hadn’t saved your sorry thorax, you wouldn’t have any looks at all. Nyuk, nyuk.

XERCES: Acie!! That was a nasty hit you took.

ACE: (To Xerces; groaning) Ahhh, it could have been worse. It could have been a windshield on the interstate. (To audience) I was lying in a corner of the police station. Behind Sergeant Zito, Xerces and the maggot, a bunch of handcuffed roaches and other pests were waiting to be questioned. Everyone had an alibi. The roaches said of course they ran from the scene of the crime – it was their nature to scatter when the lights go on.

ROACH: Why do you think we wear sunglasses?

ACE: Before we could question the cicada, he molted and flew out the window. Twig couldn’t have run anywhere. He was a walking stick. We brought in Smooch, the assassin bug. No one wanted to get near his kisser. We decided to call it a night.

The full moon hung in the sky like a large compound eye as we left the police station.

DRONE BEE: (whispering) Psssssst! Hey, Lacewing. I know who’s got Queenie and why.

ACE: (to drone) Who are you?

DRONE BEE: (Still whispering) A drone who knows the truth. But there are too many eyes and too many antennae around here. Let’s go someplace we can talk in private . . .

ACE: (to audience) We never got the chance. It happened quick as a cricket – a drive-by gassing. (To Drone; shouting) Hit the dirt! (to audience) But it was too late for the bee. I couldn’t make out the driver, but the other one was no doubt a bombardier beetle. I could tell by the smell. (wave hand in front of face) I wondered if he had a license to pass gas. (In words and actions) I checked the bee. He wasn’t moving, but he was trying to say something. I lowered my ear to his mouth.

DRONE BEE: (moaning) Drone HoneyWorks. (and he dies)

ACE: (muttering to himself) Al the Drone.

SGT ZITO: Al the Drone? Oh no, not Al the Drone! Please don’t let it be Al the Drone. Anybody but Al the Drone . . . Ace?

ACE: (to Zito) Yeah?

SGT ZITO: Who’s Al the Drone?

ACE: (to Zito) Al the Drone owns Drone HoneyWorks. Some bugs say he has his sticky little mandibles in more than just honey. I think we should pay Mr. Drone a visit. (to audience) Xerces worked on the bee as Zito and I took off across town.

Outside Drone HoneyWorks, the smell of honey hung thicker in the air than ants on a popsicle stick. Savage mantises kept guard. As we crawled around the back of the building, I got a sick feeling in my gut. The back gate of the Beetle Zoo was right across the street. And the trail of honey led from the zoo to the HoneyWorks! We needed a way in. But how?

Two dung beetles were making their way up the street, rolling their dung ball and collecting trash. They rolled up next to us.

ACE: (whispering to Zito) You thinkin’ what I’m thinkin’? (To audience) The dung beetles were too busy to notice us.

SGT ZITO: Oh no, Ace, not the dung.

ACE: (whispering to Zito) Hold your breath. (To audience) We leapt onto the dung ball and rolled right past a mantis into the HoneyWorks. I peered in a window. What I saw made my antennae quiver. In the shadows I saw someone tied up and blindfolded. It looked like Queenie. She sure wasn’t getting the royal treatment here.

SGT ZITO: Uh . . . . Ace? We got company . . .

ACE: (To audience) One of the mantises had followed our dung prints. He didn’t look too happy. Neither were we when he tied us up and carried us inside.

Inside, the aroma of honey and pollen was sickeningly sweet. I’ve been in hives before. You can tell a good hive by the buzz of the bees. The buzz in here was not good. The mantis looked as if he were in a trance as he toted us past rows and rows of honeycomb. Standing in the shadows was Al the Drone . . . [or was it?]

MANTIS: Hey, boss. Look what I found snoopin’ around outside.

UNIDENTIFIED DRONE: Well, well, if it ain’t the little lacewing and his blood-sucking friend.

SGT ZITO: That’s a common misconception! Actually it’s the female who – uhhhhh! (groans as the mantis’s claw tightens around him.)

ACE: (squeaks due to the grip of the mantis) I know you got Queenie here, Drone. (to audience) My eyes ran from all the pollen. (To unidentified drone) You’ll never get away with it!

UNIDENTIFIED DRONE: Funny, that’s the same thing Queenie said to me, and look where she is now. (Points)

ACE: (To audience) I couldn’t believe my eyes. Queenie was stuffed into a honeycomb, alive but not for long. If Queenie was holding her breath in the honeycomb, then who was tied up in the next room? All this and the stench of honey made my head spin. I tried to put the facts together but they wouldn’t fit. Who was the mystery bug in the shadows? And why did the Drone smell of pollen? . . . . Pollen! That was it! The clues clicked together in my head like a skip jack beetle.

UNIDENTIFIED DRONE: (muttering) Any last words, Lacewing?

ACE: (To the unidentified drone) Yeah. Since when do drones gather pollen? (to audience) The whole place went quiet.

PRINCESS POLLEN: (emerging from the shadows and tossing her hat and coat aside) Ha, you’re clever, Lacewing. Clever, clever, clever.

SGT ZITO: (stuttering) P-p-princess P-pollen?!

PRINCESS POLLEN: (triumphantly) In the exoskeleton!

ACE: (To Princess Pollen) But why?

PRINCESS POLLEN: Because I’m sick of just being princess!! I want to be QUEEN! (Stomping around as she rants) It’s always Queenie Bee this and Queenie Bee that. I’ll never have my own hive with her around. So I’m making it look like sleazy Al the Drone got rid of her. You guessed it, Lacewing – that’s him tied up in the back room. With Queenie and Drone HoneyWorks gone, I’ll be queen of the town.

As for the mantises, they won’t remember a thing. I hypnotized them with my pollen dance (demonstrate dance). You’re in a rather sticky situation, Lacewing, so see ya, wouldn’t wanna bee ya!

ACE: Princess Pollen made her way to the door. She signaled the mantises to seal us in the honeycombs. I had to think fast. Something fluttered overhead, so I shouted the only thing that makes a mantis run for cover. BAT!!! The mantis threw us high in the air. We soared helplessly until whatever was flying above grabbed us.

XERCES: Are we still on for those aphids, Acie?

ACE: It wasn’t a bat. It was Xerces. She had rounded up every cop from here to Termite Heights and brought them to the HoneyWorks, saving my wings again.

Dawn was emerging like a monarch from a chrysalis when Xerces and I sat down for a plate of aphids a la mode. (To Xerces) Here’s to blue wings and my favorite things. (To audience) And the city of Motham fluttered awake behind her.
```

---

## IC-0702: Act of Devotion

- Title: Act of Devotion
- Author (byline): Deborah Tannen
- Work: The Best American Short Plays 1993-1994
- Publisher: Applause Books
- Publication date as stated: May 2000
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: FATHER, DAUGHTER
- Teaser before the introduction: Yes
- Spoken words (computed): 2795
- Already set (do not supply): none

### Source block (context only)

```text
Author: Deborah Tannen
Book: The Best American Short Plays 1993-1994
ISBN: 978-1557831996
Publisher: Applause Books
Date (Month/Year): May 2000
```

### Introduction (context only: never use it for content warnings)

```text
When speaking about the Holocaust, author Jane Yolen once said “Fiction cannot recite the numbing numbers, but it can be that witness, that memory. A storyteller can attempt to tell the human tale, can make a galaxy out of the chaos, can point to the fact that some people survived even as most people died. And can remind us that the swallows still sing around the smokestacks.” How the Holocaust impacted the future generations of Jewish families is a topic not often addressed, but in Act of Devotion by Deborah Tannen, we find a daughter traveling back to Warsaw with her Jewish family – a family that survived and love of a father figure shines through the tears. Act of Devotion by Deborah Tannen.
```

### Performance text (classify this)

```text
FATHER: a man of eighty-five

DAUGHTER: a woman in her late forties

A hotel room in Warsaw in August, late afternoon. FATHER speaks in the voice of his memory, a younger version of himself. The tone of both DAUGHTER's and FATHER's dialogue is understatement and subtle irony, not stereotypically or exaggeratedly Jewish cadences}.

DAUGHTER: The first thing we did after checking into our hotel in Warsaw was to take a taxi to where my father had lived as a child. The street was still there, with its street sign, Twarda [Pronounced "tuarda"], but in place of the apartment house he had lived in was a grim gray building with a cement wall covered with obscene spray-painted graffiti - I was overwhelmed with the thought that I was standing on the street I had heard my father talk about all my life.

FATHER: We stood under the sign, Twarda Ulica [pronounced "tuarda ooleetsa"]. How dull and quiet it was, how faceless and bland the buildings that had been put up since the war. When I was a child, the neighborhood was always in commotion and crowded with life. Both sides of the street were lined with stores, and the sidewalks were teeming with people - Hasidim with their long beards, black boots, and the ritual fringes of their prayer shawls peeking out from under their vests. Working men, women shopping, men going to and from the synagogue. There were "tragers" - carriers - men hired by people too poor to hire a wagon, carrying amazing loads on their backs - a desk, a bed. Epileptics would fall down and have convulsions in the street. No one stopped to watch, because it was common. And beggars, everywhere beggars in torn clothes. Some wore garments sewn from sacks, some had rags on their feet instead of shoes. Many of the beggars were cripples. When I came to America, I always wondered: where were the cripples?

DAUGHTER: On the second day, we went to the National History museum where we'd heard there was a film about the destruction of Warsaw during World War II. The narrator told how the inhabitants of the city were deported to another part of the country as the Germans systematically demolished their city. When the war ended, the city's inhabitants returned. There was inspiring documentary footage of the Poles handing stones from man to man as they rebuilt Warsaw - but nothing about the killing of thirty percent of the population of the city - the entire Jewish population. There were a few fleeting shots of Jews being deported, as the narrator's voice said, "The Jews were the first to go." He neglected to mention that they didn't come back.

FATHER: In the street were droshkis [pronounced "DROSHkeez'j - horsedrawn carriages that took passengers, and open wagons for trade. The drivers were beating and yelling at their horses, and yelling at pedestrians to get out of the way. Occasionally a "kareta" drove by - a fancy carriage that rich people rode in. One day an old Hasid stepped off the curb just as an automobile came rushing into the space between the streetcar and the curb, and its wheel ran over the old man's foot. As the man shrieked in pain, the driver stopped his car, got out, rushed over to the old man, and began loudly berating him for getting in his way. Soon after I arrived in America, I saw a cab driver and his passenger standing by the cab, arguing with each other. I couldn't get over the contrast. In Poland, if you were rich enough to drive an automobile, you had the right to yell at anyone. In America, a cab driver, in his worker's cap, was shouting at a rich man in a silk top hat.

DAUGHTER: We went to the Jewish cemetery where my father's grandmother was buried. He told us about attending her funeral when he was eleven, shortly before he left for America. He said his grandmother's funeral was so vivid in his mind, he felt as if he could walk right to her grave, but he couldn't walk to it, because the cemetery he'd visited as a child had been destroyed during the war. Headstones had been smashed by vandals or uprooted by trees that sprouted up; paths had been obliterated by undergrowth.

FATHER: Our apartment building was built around a cobblestone courtyard. You entered through a huge archway with wooden doors that were locked at night. There were storefronts facing the courtyard, at ground level. During the day vendors came in, shouting about what they had to sell. Beggars came in and went from door to door, asking for a kopek or a piece of bread, which they'd put into a sack.

DAUGHTER: We went to the memorial to the Warsaw ghetto uprising. There's a long approach to the monument, leading up to a dynamic statue hurtling out of a stone wall: muscular young men brandishing arms, who chose to die fighting rather than follow orders for deportation. On another day, a Polish woman, took us back to see the other side of the monument: a frieze of a throng of people streaming to their deaths - a rabbi carrying a torah, families with children dwarfed by the legs around them. This, she told us, was the truer representation. There were sixty thousand people left in the ghetto at the time of the uprising. Three hundred thousand of the ghetto's inhabitants had been killed in Treblinka in the months before. We had missed this part of the monument on our first visit. We hadn't thought to walk around and look at the back.

FATHER: Vendors came into the courtyard, shouting about what they had to sell. One man had a grinding wheel; people brought him knives and scissors to sharpen. Another man would push a wheelbarrow into the courtyard and set up shop. He took iron pots blackened from cooking and returned them sparkling and shiny.

DAUGHTER: At the ghetto monument, my father got into a conversation with a young Danish woman holding a guidebook. As he walked away, I told her that he had grown up in Warsaw, that his grandfather had died in the ghetto, and that other family members and people he'd grown up with had died there, or lived there and died in the camps. I brandished this information as a badge of honor, as if it gave me a greater right to be visiting the memorial.

FATHER: Our third-floor apartment was my grandfather's home. I was born there, and so was my mother. I lived there until I was seven. My mother was one of the oldest of sixteen brothers and sisters. The youngest was only six years older than I, so I was like the youngest brother, and my grandfather was the closest I ever came to having a father. For years I thought my grandfather's name was "zahzogit" because that's what my grandmother called him: "Zahzogit, would you pull out that chair?", "Zahzogit, may I have money to shop for food?" Then I found out that "zahzogit" meant "be so good." When she spoke to him, she began that way to be properly deferential to her husband. His children feared him, because he was stern and author-itarian with them, but he was always kind and gentle to me.

DAUGHTER: When I was seven or eight, I wrote my first story. It was about my father when he was a child. The story took place in the stairwell outside his apartment in Warsaw. It was a story he'd told me: when he was very little, his mother dressed him in his older sister's outgrown dresses, rather than spend money buying boy's clothes for him. He was too ashamed to go out and play dressed as a girl, so he sat in the stairwell all day and cried.

FATHER: My mother was married at eighteen to a man she'd never met, and she never liked him. She threw him out when I was two. She never told me directly that I was ugly, but whenever she spoke of my father, she's say how she hated his looks, especially his long hooked nose. And whenever she spoke about me, she'd say I looked exactly like him. When I did something she didn't like, which was just about anything I ever did, she'd say, "Just like your father.” It wasn't until I was an adult and talked to people who knew him that I found out my father had been a wonderful man. They said he was kind, gentle, intelligent, and generous. Everyone loved him, except my mother.

DAUGHTER: My father talked so much about his childhood that I felt it as if it had happened to me. But it hadn't happened to me. I believed that nothing that happened to me could be as significant as what he had suffered. What right did I have to be miserable. In my memory, my childhood is an endless train of days spent with my mother, missing my father. He left the house before I woke up in the morning, and he often worked late, so he came home after I had gone to sleep. My favorite object in the house was an old black typewriter with yellow keys rimmed in silver. I'd spend hours typing letters to my father, telling him what had happened to me during the day and laying out my grievances against my mother. I couldn't have any grievances against him, because he wasn't there.

FATHER: My father had tuberculosis. My mother told people that was why she threw him out - so he wouldn't infect my sister and me. And she said she never remarried because she didn't want her children to grow up with a stepfather. Maybe it was true. But I always believed she preferred to live on her own. She wasn't the kind of woman who wanted to spend her life waiting on a man.

DAUGHTER: Sometimes when he was home at our bedtime, my father told us stories that he made up himself -long elaborate tales of dragons and eagles in which we were the heroes. As we lay in our beds, he'd move around the room, acting out all the parts, suddenly rushing right up to our delighted, mock-scared, laughing faces. And then, when it was time to sleep, he'd lie down with us, and we'd snuggle up to him with our heads on his shoulder. That way I could always fall asleep . . . When I was a teenager, I prided myself on my irreverence. I liked to shock people by saying, "If my father had stayed in Poland, he'd be a lamp shade."

FATHER: When I was six, my father died. He was twenty-seven years old. Since I didn't know him, I wasn't sad; I thought it was an interesting piece of news. When I ran into a neighbor on the staircase, I boasted excitedly that I knew something she didn't. "What is it?" she asked. "That your father died?" Though I never knew my father, I certainly knew my grandfather. There was no question in my mind that he was the most powerful, most dignified man in the world, and I was sure everyone else knew this too. But one day, after World War I finally ended, he took me with him on an expedition to the home of someone who owed him money. I was shocked to see the manner he assumed in this house, as he doffed his cap in deference. I couldn't believe my eyes: my grandfather, taking his hat off to someone!

DAUGHTER: Years ago I had a dream. I'm having a birthday party. My father is there, but he's suspended about two feet off the ground, with his head near the ceiling. I don't know what he's doing up there; he doesn't seem to be doing anything, just floating in his own world. I can't reach him, and he doesn't hear me or see me. I desperately try to make contact with him, but he's stuck up there and I can't get him to come down.

FATHER: When we were about to leave for America, my grandfather called me to him and took me on his lap. Tears streamed from beneath his gold-rimmed glasses, down his cheeks, and into his beard. He knew he would never see me again. With his arm around my shoulders, he said, "Never forget that you are a Jew."

DAUGHTER: I'd always known that my father's grandfather died in the Warsaw ghetto, but somehow I'd assumed he died of old age, and the ghetto happened to be where he lived when his time came. In my mind, "the ghetto" was just a dilapidated section of town where Jews were forced to live. But one day, I realized how much I didn't know - that Jews had been crammed into the ghetto from all over the city and the country; that 1 00,000 people died there from starvation, and from epidemics that broke out, caused by the overcrowding and unsanitary conditions. Naked corpses lay in the streets - corpses in the street because people had to pay a fee to bury their dead and they had no money; naked because every shred of cloth had to be salvaged and used. Women nursed infants in the street, but they had no breasts, no nourishment to give their dying babies. German soldiers strolled through the ghetto on their way to somewhere else and shot people for fun. I thought I knew about the Warsaw ghetto, but I really didn't know anything about it at all.

FATHER: Those were my grandfather's last words to me: "Never forget you are a Jew." He believed that when Jews went to America, they ceased to be Jews, because they stopped being Hasidic. Have I betrayed him? What do my daughters know of their Jewish heritage? What can being Jewish mean to them, having grown up in America? Only one of them married a Jew - and she doesn't have children, so what difference does it make?

DAUGHTER: We went to the Unschlagplatz, where each day thousands ofJews gathered to be shipped to Treblinka, where they'd be gassed. Today it's a green park with a monument, a series of stone walls. One wall is a glittering white stone slab with Jewish names, meant to represent the three hundred thousand people who had been sent to be killed from this square. Mordechai, Moishe, Shmuel, Abraham, Rachel, Rebecca, Naomi, Leah, Sarah, Miriam, Deborah. Another stone slab bore the words of a poem. We all lined up facing this wall, and asked my father to translate the Polish text etched into the stone. [As she speaks these lines, DAUGHTER walks over to FATHER and stands beside him on his left, as they both enact the scene she describes.] He began to read the words, but his voice faltered, and he stopped. I turned to see that his body was shaking. He put his right hand up to his left cheek, palm out, making a barrier between our eyes, so I couldn't see his face as he sobbed. I put my arm around him. He gathered himself up and started to read again. But again, he stopped. Again, he held his hand to the side of his face, like a shield against my gaze. On the third try he read:

FATHER: "Earth, do not cover my blood; wind, do not silence my screams ... "

DAUGHTER: As we walked away, my mother whispered to me that in the sixty years of their marriage, she had never seen him break down before. Days later, he told us what overcame him was a picture in his mind of his grandfather and his uncle Joshua, the only son who had stayed behind with the old man, and Joshua's wife and five children. They had all almost certainly been shipped to their deaths from the spot on which we stood. And he kept thinking, "What had they done to deserve their fate? They had never done anything to hurt anyone."

FATHER: I stood under the street sign, Twarda Ulica. Inside my head, it was all still there: the busy courtyards, the people calling out of the windows, the streetcars clanging, the drivers yelling, my grandfather going to shul, But outside, there was nothing. No trace of the world I grew up in. In place of the three-story apartment house with its courtyard was a gray utilitarian building covered with obscene graffiti. After I'm gone, who will remember? If no one remembers, what will remain?

DAUGHTER: My father wanted to take pictures of the Jewish cemetery, but he hates to waste pictures with no one in them, but I hung back. I couldn't figure out if it was a desecration to pose for pictures, like tourists, in a place like that, or if it was an act of devotion, to try to remember.
```

---

## IC-0703: The Actor’s Nightmare

- Title: The Actor’s Nightmare
- Author (byline): Christopher Durang
- Work: Sister Mary Ignatius Explains It All for You and The Actor's Nightmare
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: June 1999
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR, ACTRESS, GEORGE, MEG, ELLEN, VOICE, SARAH, EXECUTIONER
- Teaser before the introduction: Yes
- Spoken words (computed): 1786
- Already set (do not supply): none

### Source block (context only)

```text
Author: Christopher Durang
Book: Sister Mary Ignatius Explains It All for You and The Actor's Nightmare
ISBN: 978-0822210351
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): June 1999
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: We’ve all had dreams spurred by anxiety . . .

ACTOR: Perhaps the lawyer who gets up to begin his opening statement and can’t find his papers? Or when he does, they’re in German?

ACTRESS: The emergency doctor who goes to make an incision and his instruments have turned to rubber?

ACTOR: Still, it seems the cruelest forms of these nightmares are those that dog the poor actor.

TOGETHER: The Actor’s Nightmare by Christopher Durang
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

ACTOR: Plays the role of George

ACTRESS: Plays all other parts

Basically an empty stage with a few set pieces on it. George Spelvin wanders out. He wanders downstage, looking very confused. Enter Meg, with clipboard and master script. She is looking at the clipboard and doesn’t notice George at first.

GEORGE: Oh, I’m sorry. I don’t know how I got in here.

MEG: (Looking up at the sound of his voice and xing to him) Oh, thank goodness you’re here. I’ve been calling you. An awful thing has happened. Eddie’s been in a car accident, and you’ll have to go on for him.

GEORGE: Good Heavens, how awful (Xing a few step SL) . . . who’s Eddie (Xing back)?

MEG: Eddie. (He looks blank.) Edwin. You have to go on for him . . . He’s been in a car accident.

GEORGE: Yes, I understood that part. But what do you mean “go on for him”?

MEG: You play the part. Now I know you haven’t had a chance to rehearse it exactly, but presumably you know your lines and you’ve certainly seen it enough.

GEORGE: I don’t understand. Do I know you?

MEG: George, we really don’t have time for this kind of kidding. Half-hour. (Exits)

GEORGE: My name isn’t George, it’s . . . well, I don’t know what it is, but it isn’t George.

GEORGE: Am I an actor? I thought I was an accountant. Any why does everyone keep calling me George? (Enter Dame Ellen Terry from SR. She Xs to George.)

ELLEN: Hello, Stanley. I heard about Edwin. Good luck tonight. We’re counting on you.

(Starts off L)

GEORGE: Wait. What play are we doing?

ELLEN: (turning towards him) Very funny, Stanley. “Checkmate” by Samuel Beckett. You know, in the garbage cans. You always play these jokes, Stanley, just don’t do it onstage. Well, good luck tonight. I mean, break a leg. Did you hear? Edwin broke both legs! (Exits SL, laughing)

GEORGE: I’ve never heard of “Checkmate”. (Enter Meg SR, looking at her watch.)

MEG: George, get into costume. We have 15 minutes.

GEORGE: I better just go home. (Takes off his pants.) I didn’t mean to do that.

MEG: George, stop that. (Indicating SL) Go into the dressing room to change. Really, you keep this up and we’ll bring you up on charges.

GEORGE: But where is the dressing room?

MEG: George, you’re not amusing. (Indicating again, more angrily and exasperated) It’s that way. And give me those. (Takes his pants) I’ll go soak them for you. Now go get changed. The call is 5 minutes. (Pushes him off towards dressing room SL, Xs back SR) 5 minutes, everyone. 5 minutes. Places.

VOICE: Ladies and gentlemen, may I have you attention please? The management wishes to remind the audience that the taking of photographs is strictly forbidden by law, and is dangerous as it may disorient the actor. Thank you.

GEORGE: Where are you going? Don’t go! (Smiles out at audience. Enter Sarah SR dressed as Queen Gertrude.) Oh, good to see you.

SARAH: O Hamlet, speak no more. These words like daggers enter in mine ears. No more, sweet Hamlet.

GEORGE: Very well. What do you want to talk about?

SARAH: (melodramatically) No more! (Exits SR)

GEORGE: Oh don’t go! (Pauses, smiles uncomfortably at the audience) Maybe someone else will come out in a minute. (Pause) Of course, sometimes people have soliloquies in Shakespeare. (The lights change suddenly to a dim spot center stage. George is not standing in the spot.) Oh dear. (He moves awkwardly to the spot, decides to do his best.) To be or not to be, that is the question. (Doesn’t know anymore.) Oh maid! Line. Line! Ohhhh . . . Oh, what a rogue and peasant slave am I. Whether tis nobler in the mind’s eye to kill oneself, or not killing oneself, to sleep a great deal. We are such stuff as dreams are made on; and our lives are rounded by a little sleep. (Spot light moves and George moves into it.) I pledge allegiance to the flag of the United States of America and to the republic for which is stands, one nation, under God, indivisible, with liberty and justice for all. Line. Line! Line! (Explaining) When you call for a line, the stage manager normally gives you your next line to refresh your memory. Line! The quality of mercy is not strained. It droppeth like a gentle rain upon the place below when we have shuffled off this mortal coil. Alas, Poor Yorick- I knew him well. Get thee to a nunnery- Line!- Nunnery. (Irritated) Line! (Apologetic) I'm sorry. This is supposed to be Hamlet or Private Lives or something and I keep rattling on like a maniac- I really do apologize. I just don't recall attending a single rehearsal. I don't know what I was doing. And also you came here to see Edwin Booth and you get me. I really am very embarrassed. Sorry. Line! (Singing) A, b, c, d, e, f, g, h, i, j, k, l , m, n, o, p, q, r, s, t . . . It’s a far, far better thing I do then I have ever done before . . . It’s a far far better place I go to than I have ever been before. (Ellen enters SL, dragging 2 large trash cans. She puts them side by side, gets in one.) Oh good- Are you Ophelia? Get thee to a nunnery! (She points to the other garbage can, indicating he should get in.) Get in? Okay. (He does.) This must be one of those modern Hamlets.

ELLEN: Nothing to be done. Pause. Pause. Wrinkle nose. (Wrinkles nose.) Nothing to be done.

GEORGE: I guess you’re not Ophelia.

ELLEN: We’ll just wait. Pause. Either he’ll come, pause pause pause, or he won’t.

GEORGE: That’s a reasonable attitude. Are we, on a guess, waiting for Godot?

ELLEN: No, Willie. He came before and was an awful bore. Yesterday he came. Garlic on his breath, telling a lot of unpleasant jokes. He was just dreadful, pause, rolls her eyes upward (she rolls her eyes).

GEORGE: Well, I’m sorry to hear that. Pause. So who are we waiting for?

ELLEN: We’re waiting for Lefty.

GEORGE: Ah. And he is a political organizer or something, I seem to recall?

ELLEN: Yes, dear, he is a political organizer. He’s always coming around saying to get involved, get off your behinds and organize, fight the system, do this, do that, uh, he’s exhausting, he’s worse than Jane Fonda. And he has garlic breath, just like Godot, I don’t know which of them is worse, and I hope neither of them ever comes here again. Blinks left eye, blinks right eye, closes eyes, opens them (does this).

GEORGE: So we’re not really waiting for anyone, are we?

ELLEN: No, dear, we’re not. It’s just another happy day, pause, smile, pause, picks bug from head (does this).

GEORGE: Do you smell something?

ELLEN: (under her breath) That’s not your line. Willie doesn’t have that many lines. (Louder) Oh, Willie, how talkative you are this morning!

GEORGE: There seems to be some sort of muck in the bottom of this garbage can.

ELLEN: Mustn’t complain, Willie. There’s muck at the bottom of everyone’s garbage can. Count your blessings, Willie. I do. (Counts to herself, eyes closed.) One. Two. Three. Are you counting, Willie? I’m up to three. Three is my eyesight. (Opens her eyes.) Oh my God, I’ve gone blind. I can’t see< Willie. Oh what a terrible day. Oh dear. Oh my. (Suddenly very cheerful again.) Oh well. Not so bad really. I only used my eyes occasionally. When I wanted to see something. But no more!

GEORGE: I really don’t know this play at all.

ELLEN: Count your blessings, Willie. Let me hear you count them.

GEORGE: Alright. One. Two. Three. That’s my eyesight. Four. That’s my hearing. Five, that’s my . . . MasterCard. Six, that’s . . .

ELLEN: Did you say God, Willie?

GEORGE: No.

ELLEN: Why did you leave the monastery, Willie? Was it the same reason I left the opera?

GEORGE: I have no idea.

ELLEN: I left the opera because I couldn’t sing. They were mad to have hired me. Certifiable. And they were certified shortly afterward, the entire staff. They reside now at the Rigoletto Home for the mentally Incapacitated. In Turin. Pause. Tries to touch her nose with her tongue (does this.)

VOICE: Ladies and Gentlemen, may I have your attention please? At this evening’s performance, the role of Sir Thomas More, the man for all seasons, normally played by Edwin Booth, will be played by Georg Spelvin. (Enter Meg with a few costume touches but otherwise in her stage manager garb. She is carrying a script.)

MEG: Oh father, why have they locked you up in this dreadful dungeon, it’s more than I can bear. If you don’t give in to King Henry, they’re going to cut off your head. (Sudden alarming crash of cymbals. The Executioner enters USL and Xs CS and stops.)

GEORGE: I’ve got to get out of here.

MEG: He’s over here. And he’ll never give in to the king.

GEORGE: No, no, I might. Quick, is this all about Anne Boleyn and everything?

MEG: Yes and you won’t give in because you believe in the Catholic Church and the infallibility of the Pope and the everlasting life of the soul.

GEORGE: (to Meg) I don’t necessarily believe in any of that. (To Executioner) Oh sir, there’s been an error. I think it’s fine if the King marries Anne Boleyn. I just want to wake up.

MEG: Oh don’t deny God, father, just to spare our feelings. Mother and I are willing to have you dead if it’s a question of principle.

GEORGE: I don’t think the Pope is infallible at all. I think he’s a normal man with normal capabilities who wears gold slippers. I thought about joining the monastery when I was younger, but I didn’t do it.

ELLEN: (waking up from a brief doze) Oh, I was having such a pleasant dream, Willie. Go ahead, let him cut your head off, it’ll be a nice change of pace. (Executioner wheels out chopping block.)

GEORGE: That blade looks very real to me. I wasn’t to wake up now. Or change plays. A horse, a horse, my kingdom for a horse!

EXECUTIONER: Sir Thomas More, you have been found guilty of the charge of High Treason. The sentence of the court is that you be taken to the Tower of London, thence to the place of execution, and there your head shall be stricken from your body and may God have mercy on your soul. (Meg helps George out of the garbage can.)

GEORGE: Alright, I’m sorry I didn’t go to the monastery, maybe I should have, and I’m sorry I giggled during church in the 3rd grade, but I see no reason to be killed for it.

EXECUTIONER: Do I understand you right? You wish to reverse your previous stand on King Henry’s marriage to Anne and to deny the Bishop of Rome?

GEORGE: Yes, yes, YES! (He rises) I could care less. Let him marry eight wives.

EXECUTIONER: That’s a terrible legacy of cowardice for Sir Thomas More to leave behind.

GEORGE: I don’t care!

EXECUTIONER: I’m going to ignore what you’ve said and cut your head off anyway, and then we’ll all pretend you went to your death nobly. The Church needs its saints and school children have got to have heroes to look up to, don’t you all agree?

GEORGE: Yes, yes, I can feel myself waking up now. The covers have fallen off the bed and I’m cold, and I’m going to wake up so that I can reach down and pull them up again.

EXECUTIONER: Sir Thomas, prepare to meet your death.

GEORGE: Be quiet, I’m about to wake up.

EXECUTIONER: Sir Thomas, prepare to meet your death.

GEORGE: I’m awake! (Looks around him) No, I’m not.

EXECUTIONER: Sir Thomas, prepare to meet your death.

GEORGE: Line! Line!

MEG: You turn to the Executioner and say, “Friend, be not afraid of your office. You send me to God.”

GEORGE: I don’t like that line. Give me another.

MEG: That’s the line in the script, George. Say it.

ELLEN: Say it, Willie. It’ll mean a lot to me and to generations of school children to come.

EXECUTIONER: Say it.

GEORGE: They say you can never dream your own death, so I expect that I’ll wake up just as soon as he starts to bring down the blade. So perhaps I should get it over with.

MEG: Say the proper line, George. (George kneels down.)

GEORGE: Friend, be not afraid of your office. (Executioner raises axe.) You send me to God. (Executioner raises axe higher to bring it down.)

EXECUTIONER: (In darkness) Behold the head of Sir Thomas More.

(Everyone bows except George who is dead on the floor. Everyone else does curtain call and leaves. After the stage is clear, George gets up dazed and looks around. Looks out at the audience and leaves.)
```

---

## IC-0704: Alias Grace

- Title: Alias Grace
- Author (byline): Margaret Atwood
- Work: Not specified
- Publisher: Anchor
- Publication date as stated: October 1997
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: GRACE, DR. JORDAN, ACTOR, MRS. QUENNELL, DR. DUPONT, REV. VERRINGER, ACTRESS
- Teaser before the introduction: Yes
- Spoken words (computed): 1931
- Already set (do not supply): none

### Source block (context only)

```text
Author: Margaret Atwood
ISBN: 978-0385490443
Publisher: Anchor
Date (Month/Year): October 1997
Rock of Ages hymn: https://www.youtube.com/watch?v=gM7gt_cSxjw
The Rose of Tralee (Irish folk song): https://www.youtube.com/watch?v=Xo2Q74VN7IU
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: The bodies were found in a cellar. Thomas Kinnear, the owner of the home, had been shot in the left side of his chest.

ACTRESS: Nancy Montgomery, his housekeeper and mistress, was struck in the head with an axe and then strangled.

ACTOR: It was the summer of 1842 and conspicuously absent in the wake of the murders were two domestic servants: 20-year old James McDermott and 16-year old Grace Marks.

ACTRESS: The pair appeared to have fled Kinnear's home wearing clothing belonging to the deceased. They are quickly caught and charged with the murders.

ACTOR: Dr. Simon Jordan, an up-and-coming expert in the burgeoning field of mental illness, is hired. His mission?

ACTRESS: To find out what really happened on the day of the killings.

ACTOR: Was Grace the evil instigator of the murder plot or was she an unfortunate and vaguely stupid girl who had fallen victim to an overwhelming male villain in James McDermott?

ACTRESS: Based on a true story . . . this is

TOGETHER: Alias Grace by Margaret Atwood
```

### Performance text (classify this)

```text
NOTE: This cutting asks one student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles: Actress: Grace Actor: Dr. Jordan, Dr. DuPont, Mrs. Quennell and Rev. Verringer

GRACE: (Pg 309-310) Nancy said we was both to leave after the next day, and she had the money to pay us. She said that Mr. Kinnear was in agreement with her.

DR. JORDAN: Did you believe that?

GRACE: As regards McDermott, I did. But not as regards myself.

DR. JORDAN: Not yourself?

GRACE: She was afraid that Mr. Kinnear would come to like me better than her. She was in the family way, and it often happens like that with a man; (voice gradually grows more coarse; rate of speaking slows – as if another persona has taken over Grace’s speaking voice) and they’ll change from a woman in that condition to one who is not, and it’s the same with cows and horses; and if that happened, she’d be out on the road, her and her bastard. (voice shifts back to Grace’s gentle cadence) It was plain she wanted me out of the way. I don’t believe Mr. Kinnear knew a thing about it.

DR. JORDAN: What did you do then, Grace?

GRACE: I cried, Sir. In the kitchen. It was at this time that McDermott said he had a secret, and I promised not to tell. Once having promised such a thing, I was bound by it. (whispering and shocked) He said he was going to kill Nancy with the axe, and strangle her as well, and shoot Mr. Kinnear when he came back and take the valuables; (back to normal tone) and I was to help him.

DR. JORDAN: You did not warn anyone?

GRACE: Please don’t make fun of me, [Dr. Jordan], it is very distressing, and doubly so considering what I am being asked to remember. . . . (Pg 312) And I did warn Nancy! While she was brushing out her hair, I said, McDermott wants to kill you. She laughed and said, I expect he does. I would not mind killing him, either. There is no love lost between us . . . Then I knew there was nothing I could do to save her.

GRACE: (Pg 312) That night Mary Whitney appeared to me in a dream.

DR. JORDAN: (pg 102) Who is Mary Whitney?

GRACE: Mary Whitney, Sir?

DR. JORDAN: It is written underneath your portrait. At the front of your confession. Grace Marks, Alias Mary Whitney.

GRACE: Oh, yes. It is not a good likeness of me.

DR. JORDAN: And Mary Whitney?

GRACE: Oh, that was just the name I gave, Sir, at the tavern in Lewiston when James McDermott was running away with me. He said I should not give my own name, in case they came looking for us.

DR. JORDAN: And did you give any name that came into your head?

GRACE: Oh, no, Sir. Mary Whitney was once a particular friend of mine. (Pg 148) [She] helped in the laundry [at the home of my previous employer]. (Pg 149) I liked her at once. Next to me she was the youngest one there. (Pg 150) I was often astonished at the words that came out of her mouth, as many of them were quite coarse; it wasn’t that I’d never heard such language before, but I was surprised to hear it from a girl, and one so young and pretty, and so neatly and cleanly dressed. (Pg 177) I did not know she was going to die . . . . (long silence; Grace is lost in thought)

DR. JORDAN: [You were telling me about your dream . . . ]

GRACE: (Pg 312-313) That night Mary Whitney appeared. It was not the first time; she’d come before, but never to say anything. She was holding a glass tumbler in her hand, and inside it was a firefly, trapped and glowing with a cold and greenish fire. Her face was very pale, but she looked at me and smiled. Then up ahead I saw Nancy, on her knees, with her hair fallen over and blood running down into her eyes. Around her neck was a white cotton kerchief printed with blue flowers, and it was mine.

DR. JORDAN: (Pg 314) You dreamt this before the event? (writing feverishly)

GRACE: Yes, sir. And many time since. That was why they put me away.

DR. JORDAN: Away?

GRACE: (looking down at her hands) Into the Asylum, sir. Because of the bad dreams.

DR. JORDAN: (gently) Only the dreams?

GRACE: They said they were not dreams at all, sir. They said I was awake. But I do not wish to say any more about it. (Dr. Jordan steps out of the scene)

DR. JORDAN: (to audience) (Pg 373) Grace’s amnesia seems genuine enough, or so I have come to believe, in the light of my previous clinical experience. On the other hand, although she can’t seem to remember the murder, she has a minute recollection of the details surrounding it. (Pg 377) I must admit I’ve been baffled. What she says has the ring of truth; her manner is candid and sincere; and yet I can’t shake the suspicion that, in some way I cannot put my finger on, she is lying to me. (exits)

TRANSITION

ACTOR: Months pass as Grace is questioned by Dr. Jordan. She tells the same tale over and over, lacing her tale with dreams she recalls – dreams about the murdered victims. But a person can’t be convicted based on their dreams . . . or can they? It was then Dr. Jordan developed a plan.

GRACE: (Pg 381-382) When Dr. Jordan comes back, I am to be hypnotized. Dr. DuPont is to do the hypnotizing, and other will watch and listen. [They] said I need not be afraid, as I will be among friends who mean well, and all I will have to do is go to sleep when Dr. DuPont tells me to. When I am asleep they will ask me questions. In this way they hope to bring back my memory. (Grace steps into scene, rigidly, her lips pressed together, she is obviously afraid)

DR. JORDAN: (Pg 397) (Grace pantomimes Dr. Jordan’s description) Du Pont turns the lamp down low and begins his procedure. First he suggests heaviness, drowsiness; then he tells Grace that her limbs are floating, drifting, that she is sinking down, down, down, as if through water. His voice has a soothing monotony. Grace’s eyelids droop, she is breathing deeply and evenly. He asks: “Are you asleep, Grace?”

GRACE: Yes.

DR. JORDAN: “Good,” he says. “Let us proceed.” (to Dr. DuPont) (Pg 399-404) Ask her whether she ever had relations with James McDermott.

GRACE: (laughs in a tone that doesn’t sound like her own) Relations, Doctor? What do you mean? Really, Doctor, you are such a hypocrite! You want to know if I kissed him, if I slept with him, if I was his paramour! Is that it?

DR. JORDAN: (shaken) Yes. (to audience) I was expecting a series of mere yes’s and no’s dragged out of her. Not such crude mockery. This voice cannot be Grace’s; yet in that case, whose voice is it?

GRACE: So I’ll tell you. Yes. I would meet him outside, in the yard, in my nightdress, in the moonlight. I’d press up against him, I’d let him kiss me, and touch me as well, all over, Doctor, the same places you’d like to touch me, because I can always tell, I know what you’re thinking when you sit with me. But that was all, Doctor. That was all I’d let him do. I had him on a string, and Mr. Kinnear as well. I had the two of them dancing to my tune!

DR. JORDAN: (a horse creak) Why?

GRACE: I would breathe like this. (uttering a high moan) I would twist and twine. After that, he’d say he’d do anything. (laughing) But why? Or, Doctor, you are such a curious man! Curiosity killed the cat, you know.

DR. JORDAN: Ask her if she was in the cellar of Mr. Kinnear’s house on Saturday, July 23rd, 1843.

GRACE: Yes, I was in the cellar.

DR. JORDAN: Ask her if she saw Nancy there.

GRACE: Oh, yes, I saw her. As I can see you, Doctor, from behind the veil. And I can hear you too.

DR. JORDAN: Was she alive? Was she still alive, when you saw her?

GRACE: (sniggering) She was partly alive. Or partly dead. She needed (a high twittering) to be put out of her misery.

DR. JORDAN: Did you help to strangle her?

GRACE: It was my kerchief that strangled her. (giggling) Such a pretty pattern it had on it! It was a shame to lose that kerchief; I’d had it such a long time. It was my mother’s. I should have taken it off Nancy’s neck. But James wouldn’t let me have it, nor her gold earrings neither. There was blood on it, but that would have washed out. . . . The kerchief killed her. Hands held it. She had to die. The wages of sin is death. And this time the gentleman died as well, for once. Share and share alike! (Gleeful)

MRS. QUENNELL: Oh, Grace. I thought better of you! You have deceived us!

GRACE: Stop talking rubbish. You’ve deceived yourselves! I am not Grace! Grace knew nothing about it! (Grace begins to hum/sing) Rock of ages, cleft for me, Let me hide myself in thee! Let the water, and the blood . . (see link at the end of this selection for song)

DR. JORDAN: You are not Grace . . . If you are not Grace, who are you?

GRACE: (continues singing) Cleft for me . . Let me hide myself, in thee . . .

DR. DUPONT: You must answer. I command it!

GRACE: (whispering) You can’t command. You must guess!

MRS. QUENNELL: I know you are a spirit. They can speak through others, in the trance. This one is speaking through Grace. But sometimes they lie, you know.

GRACE: I am not lying! I am beyond lying!

MRS. QUENNELL: It may be James McDermott, come here to sully Grace’s reputation. To accuse her.

GRACE: Not James, you old fraud!

MRS. QUENNELL: Nancy, then. They are often rude. They call us names. Some are angry – those earthbound spirits who cannot tolerate being dead.

GRACE: Not Nancy, you stupid fool! Nancy can’t say anything, she can’t say a word, not with her neck like that. Come, Doctor . . . You like riddles. You know the answer. I told you it was my kerchief, the one I left to Grace, when I, when I . . . (begins singing again: The Rose of Tralee – See link at the end of this selection for a link to the song) Oh, no, ‘twas the truth in her eye ever dawning, That made me love Mary . . . .

DR. JORDAN: Not Mary. Not Mary Whitey

GRACE: (no longer teasing) I told James to do it. I urged him to. I was there all along! But Grace doesn’t know, she’s never known! They almost hanged her, but that would have been wrong. She knew nothing! I only borrowed her clothing for a time.

DR. JORDAN: Her clothing?

GRACE: Her earthly shell. Her fleshly garment. But I wouldn’t want to hurt her. (pleading) You mustn’t tell her!

DR. JORDAN: Why not?

GRACE: You know why, Dr. Jordan. Do you want to see her back in the Asylum? I liked it there at first, I could talk out loud there. I could laugh. I could tell what happened. But no one listened to me. (a small, thin sob) I was not heard.

DR. JORDAN: Grace, stop playing tricks!

GRACE: (hesitantly) I am not . . . I am not . . . Grace.

DR. JORDAN: Is that really you? Are you telling the truth? Don’t be afraid.

GRACE: You see? (wailing) You’re the same, you won’t listen to me, you don’t believe me, you want it your own way, you won’t hear . . . (trailing off into silence)

DR. DUPONT: Grace . . . Grace Marks, can you hear me?

GRACE: (in her normal voice) Yes.

DR. DUPONT: I am going to bring you up now. You are floating up, up. You will not recall what happened here. When I snap my fingers, you will awake. (Snaps fingers)

GRACE: (stirring and opening her eyes, she smiles like a dutiful child) I must have been asleep.

DR. DUPONT: (gently) You may feel a little dizzy. It is frequently the case. Mrs. Quennell, would you see that she is placed in a bed chamber where she may lie down. (Grace exits)

REV. VERRINGER: (Pg 405) Two hundred years ago, [we] would not have been at a loss. It would have been a clear case of possession. Mary Whitney would have been found to have been inhabiting the body of Grace Marks, and thus to be responsible for inciting the crime, and for helping to strangle Nancy Montgomery. An exorcism would have been in order. TRANSITION

ACTRESS: But medicine had made many advancements by the mid 1800’s and no exorcism was performed. Grace’s death sentence was commuted to life in the Asylum and in the mind of the public, justice was done.

GRACE: (Pg 5) It’s 1851. I’ll be twenty-four years old next birthday. I’ve been shut up in here since the age of sixteen. I am a model prisoner and give no trouble. If I am good enough and quiet enough, perhaps after all they will let me go; but it’s not easy being quiet and good, it’s like hanging on to the edge of a bridge when you’ve already fallen over; you don’t seem to be moving, just dangling there, and yet it is taking all your strength.
```

---

## IC-0705: Alice’s Adventures in Wonderland

- Title: Alice’s Adventures in Wonderland
- Author (byline): Lewis Carroll
- Work: Not specified
- Publisher: Dover Publications
- Publication date as stated: May 1993
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: SUGGESTED ROLES, ALICE, WHITE RABBIT, DOOR #1, DOOR #2, DOOR #3, SMALL DOOR, BOTTLE, NARRATOR, ACTOR, CATERPILLAR, CHAPTER VI, CHESHIRE CAT, CHAPTER VII, HATTER, MARCH HARE, CHAPTER VIII, CARD #5, QUEEN, VOICE IN THE DISTANCE, CHAPTER XI, CHAPTER XII, KING
- Teaser before the introduction: Yes
- Spoken words (computed): 1040
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lewis Carroll
ISBN: 978-0486275437
Publisher: Dover Publications
Date (Month/Year): May 1993
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: In 1865 a novel was written that would change the face of children’s literature.

ACTRESS: In fact, Alice in Wonderland’s themes and characters are so bizarre that in the 1960’s rumors began to surface that Lewis Carroll wrote the book under the influence of drugs.

ACTOR: It’s a tempting theory. After all, the story has Alice eating ‘magic’ mushrooms and meeting hookah-smoking caterpillars.

ACTRESS: References to this seminal work appear in modern day films like The Matrix.

ACTOR: "You take the blue pill . . .”

ACTRESS: The story ends, you wake up in your bed and believe whatever you want to believe.

ACTOR: “You take the red pill . . .”

ACTRESS: You stay in Wonderland, and I show you how deep the rabbit hole goes."

TOGETHER: Alice in Wonderland by Lewis Carroll . . .
```

### Performance text (classify this)

```text
SUGGESTED ROLES: Actress – Alice Actor – Everyone else

NOTE: This cutting asks one student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Chapter I: Down the Rabbit-Hole Alice is reading a book, flipping through the pages rapidly and is bored. (Actor simulates the passing of time by pantomiming the movements of a clock with sound effects)

ALICE: (Sighs heavily as she closes the book) What is the use of a book without pictures or conversations! (Suddenly a white rabbit catches her attention)

WHITE RABBIT: Oh, dear! Oh, dear! I shall be too late!” (he takes a watch out of his pocket, looks at it and hurries on. Alice follows.) Oh my ears and whiskers, how late it’s getting! [Rabbit Hole!] (He jumps down the hole and Alice follows. As she lands, the rabbit is no longer in sight. She finds herself in a hall with a serious of doors. She tries each door)

DOOR #1: Locked

DOOR #2: Locked

DOOR #3: Locked

ALICE: [Oh, look] a tiny golden key. (Picks it up) It might belong to one of the doors!

DOOR #1: Too small

DOOR #2: [Nope]

DOOR #3: (Simply laughs)

ALICE: Either the locks [are] too large, or the key [is] too small.

SMALL DOOR: (representing a small door – makes some type of sound to get Alice’s attention)

ALICE: A little door! (She tries the little key in the lock and it fits!) [Oh, look] the loveliest garden you ever saw. Bright flowers . . . fountains! (She tries to fit her head in the doorway, but she’s much too big) Oh, how I wish I could shut up like a telescope! I think I could, if I only knew how to begin.

BOTTLE: Drink Me!

ALICE: [Well, I’m certainly] not going to do that in a hurry. I’ll look first and see whether it’s marked “Poison” or not. (Alice examines the bottle)

BOTTLE: Drink Me! (Alice shrugs her shoulders and took a sip)

ALICE: What a curious feeling! (Alice shrinks down to 10-inches high, quickly tries the key in the lock. It works and she swings open the door)

NARRATOR: Wonderland! (As Alice steps through the doorway, trumpets blare to herald her arrival)

ALICE: Curiouser and curiouser!

ACTOR: No pills or mushrooms required.

Chapter V: Advice from a Caterpillar

ALICE: [What a] large mushroom . . . Caterpillar!

CATERPILLAR: (taking a hookah from its mouth) Who are you?

ALICE: I – I hardly know, sir, just at the present – at least I know who I was when I got up this morning, but I think I must have changed several times since then.

CATERPILLAR: What do you mean? Explain yourself!

ALICE: I can’t explain myself, I’m afraid, sir, because I’m not myself, you see?

CATERPILLAR: I don’t see!

ALICE: (losing her temper) I’m afraid I can’t put it more clearly – Being so many different sizes in a day is very confusing!

CATERPILLAR: Keep your temper! . . . So you think you’re changed, do you? What size do you want to be?

ALICE: Well, I should like to be a little larger, sir – three inches is such a wretched height to be.

CATERPILLAR: One side of the mushroom will make you grow taller, and the other side will make you grow shorter. (He disappears in a puff of smoke)

ALICE: (Alice stretches her arms round the mushroom as far as they will go and breaks off a bit with each hand) And now . . . which is which . . . (she takes a bite of one of the pieces and begins to grow) [Ahhh. . .] Back to my right size! The next thing is to get into that beautiful garden! (Alice walks for a bit and comes to a small house)

CHAPTER VI: Pig and Pepper

ALICE: Cheshire Cat! Would you tell me please, which way I ought to walk from here?

CHESHIRE CAT: That depends a good deal on where you want to get to. In that direction (waiving its right paw round) lives a Hatter: and in that direction (waving the other paw) lives a March Hare. Visit either you like: they’re both mad.

ALICE: But I don’t want to go among mad people.

CHESHIRE CAT: Oh, you can’t help that. We’re all mad here. I’m mad. You’re mad.

ALICE: How do you know I’m mad?

CHESHIRE CAT: You must be or you wouldn’t have come here. . . Do you play croquet with the Queen today?

ALICE: I should like it very much, but I haven’t been invited y et.

CHESHIRE CAT: You’ll see me there! (and he vanishes)

ALICE: [Well], I’ve seen hatters before. The March Hare will be much the most interesting and perhaps as this is May it won’t be raving mad – at least not so mad as it was in March.

(Hatter enters. He pours himself some tea, and follows Alice for a few seconds, establishing character, and then speaks)

CHAPTER VII: A Mad Tea-Party

HATTER: No room!

MARCH HARE: No room!

ALICE: There’s plenty of room! It’s laid for a great many more than three!

HATTER: Your hair wants cutting.

ALICE: (taken by surprise) You should learn not to make personal remarks. It’s very rude.

HATTER: Why is a raven like a writing-desk?

ALICE: I’m glad [you’ve] begun asking riddles! I believe I can guess that.

MARCH HARE: Do you mean that you think you can find out the answer to it? You should say what you mean.

ALICE: I do – at least – at least I mean what I say – that’s the same thing, you know.

HATTER: Not the same thing a bit! Why, you might just as well say that ‘I see what I eat’ is the same thing as ‘I eat what I see!’ . . . (He looks at his watch uneasily, shaking it every now and then and holding it to his ear.) What day of the month is it?

ALICE: The fourth.

HATTER: (sighs) Two days wrong! (begins trying to reset his watch)

ALICE: (grabbing his wrist to look at the watch) What a funny watch! It tells the day of the month, and doesn’t tell what o’clock it is?

HATTER: (pulling his arm back, offended) Why should it? Does your watch tell you what year it is?

ALICE: Of course not, but that’s because it stays the same year for such a long time together.

HATTER: (Continues with his tea) Which is just the case with mine. . . Have you guessed the riddle yet?

ALICE: No, I give it up. What’s the answer?

HATTER: I haven’t the slightest idea. (he laughs)

ALICE: (wearily) I think you might do something better with the time than wasting it in asking riddles that have no answers.

HATTER: If you knew Time as well as I do, you wouldn’t talk about wasting IT. It’s HIM. I dare say you never even spoke to Time!

ALICE: Perhaps not, but I know I have to beat time when I learn music.

HATTER: Ah! That accounts for it. He won’t stand beating! . . . (Alice stammers for a response)

MARCH HARE: Take some more tea!

ALICE: I’ve had nothing yet, so I can’t take more.

HATTER: You mean, you can’t take less. It’s very easy to take more than nothing.

ALICE: (disgruntled) Nobody asked your opinion.

HATTER: Who’s making personal remarks now? I want a clean cup. Let’s all move one place on!

ALICE: Really, now if you ask me . . . I don’t think –

HATTER: Then you shouldn’t talk!

ALICE: (Extremely offended) [This is] the stupidest tea-party I ever was at in all my life!”

(trumpets blare)

CHAPTER VIII: The Queen’s Croquet-Ground

CARD #5: The Queen! The Queen! (Alice straightens her dress)

QUEEN: Who is this? What’s your name child?

ALICE: My name is Alice, so please your Majesty.

QUEEN: (looks her up and down and then makes a decision) Off with her head! Off . . .

ALICE: Nonsense!

QUEEN: Can you play croquet?

ALICE: Well . . .yes . . .

QUEEN: Well, come on then! Get to your places! (she grabs a croquet mallet and ball and tosses the ball to Alice)

ALICE: [This is] a flamingo and the croquet-balls [are] hedgehogs!

QUEEN: Off with her head! (the Queen stalks away)

ALICE: (to herself) They’re dreadfully fond of beheading people here. (then she notices the arrival of the Cheshire Cat) It’s the Cheshire Cat – now I shall have somebody to talk to.

CHESHIRE CAT: How do you like the Queen?

ALICE: Not at all! She’s so extremely . . . (The Queen comes up behind her, listening – Alice notices) . . . likely to win, that it’s hardly worthwhile finishing the game.

VOICE IN THE DISTANCE: The trial’s beginning! (Scene changes to the Court of Justice)

CHAPTER XI: Who Stole the Tarts?

WHITE RABBIT: (blows three blasts on his trumpet) Silence in the court! (unrolls a parchment scroll and reads) The Queen of Hearts, she made some tarts, All on a summer day: The Knave of Hearts, he stole those tarts, And took them quite away! . . . . Alice!

CHAPTER XII: Alice’s Evidence

ALICE: (Complete surprised) Here!

KING: What do you know about this business?

ALICE: Nothing.

KING: Nothing whatever?

ALICE: Nothing whatever.

KING: That’s very important. . . Unimportant! That proves his guilt!

ALICE: It proves nothing of the sort!

KING: Let the jury consider their verdict.

QUEEN: No, no! Sentence first – verdict afterwards

ALICE: Stuff and nonsense! The idea of having the sentence first!

QUEEN: Hold your tongue!

ALICE: I won’t (stomping her foot)

QUEEN: Off with her head!

ALICE: (Looking around the courtroom) Who cares for you? You’re nothing but a pack of cards!

(transition back to the scene that begins this cutting, with Alice having fallen asleep over her book -- Actor simulates the passing of time by pantomiming the movements of a clock with sound effects as Alice slowly wakes up) Oh . . . Oh . . . I’ve had such a curious dream!

WHITE RABBIT: Alice! (Alice’s face reacts in shock)
```

---

## IC-0706: All My Sons

- Title: All My Sons
- Author (byline): Arthur Miller
- Work: Not specified
- Publisher: Crown Publishers, Inc.
- Publication date as stated: 1947
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: CHRIS, ANN
- Teaser before the introduction: Yes
- Spoken words (computed): 849
- Already set (do not supply): none

### Source block (context only)

```text
Author: Arthur Miller
ISBN: 978-0141185460
Publisher: Crown Publishers, Inc.
Date (Month/Year): 1947
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: While war does occur between countries, it is carried out by people, by fellow human beings who should never have to bear witness to such extreme horrors. Many war films depict the brutalities of war, but it seems that these representations merely skim the surface. World Wars I and II, the Cold War, Vietnam, and the Gulf War and now the War in Iraq - millions of men fought, some survive and live among us today.

ACTRESS: Survivors, however, experience difficulty with feeling any strong emotion, particularly love. They often feel disconnected from reality, and guilty for having survived at all. In this scene Chris has returned home from WWII to make a life for himself and to forge a relationship with Ann, his brother’s girlfriend.

ACTOR: My brother Lee is “missing in action,” and life is too short for waste on “might have beens”

TOGETHER: All My Sons by Arthur Miller
```

### Performance text (classify this)

```text
Time and Place: The backyard of the Keller home in the outskirts of an American town, August, 1947. The Scene: Chris (early twenties) professes his love for Ann (early twenties) and talks about the difficulty of resuming his life after the war.

CHRIS: (Calling after him.) Drink your tea, Casanova. (He turns to Ann.) Isn't he a great guy?

ANN: You're the only one I know who loves his parents!

CHRIS: I know. It went out of style, didn't it?

ANN: (With a sudden touch of sadness.) It's all right. It's a good thing. (She looks about.) You know? It's lovely here. The air is sweet.

CHRIS: (Hopefully.) You're not sorry you came?

ANN: Not sorry, no. But I'm...not going to stay...

CHRIS: Why?

ANN: In the first place, your mother as much as told me to go

CHRIS: Well.

ANN: You saw that...and then you...you've been kind of...

CHRIS: What?

ANN: Well...kind of embarrassed ever since I got here.

CHRIS: The trouble is I planned on kind of sneaking up on you over a period of a week or so. But they take it for granted that we're all set.

ANN: I knew they would. Your mother anyway.

CHRIS: How did you know?

ANN: From her point of view, why else would I come?

CHRIS: Well...would you want to? (Ann studies him.) I guess you know this is why I asked you to come.

ANN: I guess this is why I came.

CHRIS: Ann, I love you. I love you a great deal. (Finally.) I love you. (Pause. She waits.) I have no imagination...that's all know to tell you. (Ann, waiting ready.) I'm embarrassing you. I didn't want to tell it to you here. I wanted some place we'd never been; a place where we'd be brand new to each other...You feel it's wrong here, don't you? This yard, this chair? I want you to be ready for me. I don't want to win you away from anything.

ANN: (Putting her arms around him.) Oh, Chris, I've been ready a long, long time!

CHRIS: Then he's gone forever. You're sure.

ANN: I almost got married two years ago.

CHRIS: ...why didn't you?

ANN: You started to write to me... (Slight pause.)

CHRIS: You felt something that far back?

ANN: Every day since!

CHRIS: Ann, why didn't you let me know?

ANN: I was waiting for you, Chris. Till then you never wrote. And when you did, what did you say? You sure can be ambiguous, you know.

CHRIS: (He looks toward house, then at her, trembling.) Give me a kiss, Ann. Give me a... (They kiss.) God, I kissed you, Annie, I kissed Annie. How long, how long I've been waiting to kiss you!

ANN: I'll never forgive you. Why did you wait all these years? All I've done is sit and wonder if I was crazy for thinking of you.

CHRIS: Annie, we're going to live now! I'm going to make you so happy. (He kisses her, but without their bodies touching.)

ANN: (A little embarrassed.) Not like that you're not.

CHRIS: I kissed you...

ANN: Like Larry's brother. Do it like you, Chris. (He breaks away from her abruptly.)

ANN: What is it, Chris?

CHRIS: Let's drive some place...I want to be alone with you.

ANN: NO...what is it, Chris, your mother?

CHRIS: No... nothing Iike that...

ANN: Then what's wrong?..Even in your letters, there was something ashamed.

CHRIS: Yes. I suppose I have been. But it's going from me.

ANN: You've got to tell me

CHRIS: I don't know how to start. (He takes her hand. He speaks quietly, factually at first.)

It wouldn't work this way. (Slight pause.) It's all mixed up with so many other things...You remember, overseas, I was in command of a company?

ANN: Yeah, sure.

CHRIS: Well, I lost them.

ANN: How many?

CHRIS: Just about all.

ANN: Oh, gee!

CHRIS: It takes a little time to toss that off. Because they weren't just men. For instance, one time it'd been raining several days and this kid came to me, and gave me his last pair of dry socks. Put them in my pocket. That's only a little thing...but...that's the kind of guys I had. They didn't die; they killed themselves for each other. I mean that exactly; a little more selfish and they'd've been here today. And I got an idea-watching them go down. Everything was being destroyed, see, but it seemed to me that one new thing was made. A kind of...responsibility. Man for man. You understand me?-To show that, to bring that on to the earth again like some kind of a monument and everyone would feel it standing there, behind him, and it would make a difference to him. (Pause.) And then I came home and it was incredible. I...there was no meaning in it here; the whole thing to them was a kind of a-bus accident. I went to work with Dad, and that rat race again. I felt...what you said...ashamed somehow. Because nobody was changed at all. It seemed to make suckers out of a lot of guys. I felt wrong to be alive, to open the bankbook, to drive the new car, to see the new refrigerator. I mean you can take those things out of a war, but when you drive that car you've got to know that it came out of the love a man can have for a man, you've got to be a little better because of that. Otherwise what you have is really loot, and there's blood on it. I didn't want to take any of it. And I guess that included you.

ANN: And you still feel that way?

CHRIS: I want you now, Annie.
```

---

## IC-0707: American Son

- Title: American Son
- Author (byline): Christopher Demos-Brown
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: April 2019
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTRESS, ACTOR 2, KENDRA, LARKIN, KENDR, SCOTT, STOKES
- Teaser before the introduction: Yes
- Spoken words (computed): 1541
- Already set (do not supply): none

### Source block (context only)

```text
Author: Christopher Demos-Brown
ISBN: 978-0573708022
Publisher: Samuel French, Inc.
Date (Month/Year): April 2019
```

### Introduction (context only: never use it for content warnings)

```text
A summer storm is raging outside a Miami police station and inside, as well, where an interracial couple, black mother/white father, await news of their missing son. As two policemen, one white, one black, pursue details of the missing youth, all four characters become engulfed in a battle of bias, judgment and racial prejudice. With the fate of a child at risk, tensions mount, and fear grows that the answers will never be as simple as black or white.

American Son by Christopher Demos-Brown
```

### Performance text (classify this)

```text
Suggested Roles:

ACTRESS: Kendra Ellis-Connor: African American, recently separated from Scott and Officer Stokes: African-American; career police officer.

ACTOR 2: Officer Larkin: White, young, with career ambitions who lacks life experience. and Scott Connor: White, FBI agent, recently separated from Kendra.

NOTE: This cutting asks the each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

In a police station waiting room. She is on her phone.

KENDRA: (Pg 9-11) (on the phone) Jamal – dammit where are you. I’ve sent you five texts now. You can’t text me back? Call me.

LARKIN: (enters) OK . . . so I checked and the care does show up in the system. Coulda been ticketed. Coulda been towed.

KENDRA: Jamal – my son- was driving it. He’s been gone since 8 o’clock last night. Going on nine hours. And when I called the police, they said something happened to the car – Hold on – I wrote it down. (checking a scrap of paper in her purse) “Identified in an incident.”

LARKIN: I’m sure he’s gonna turn up.

KENDRA: He has work – a very prestigious internship. This isn’t like him. Can’t you do a missing persons report . . . something?

LARKIN: Not for 48 hours, no. Look . . . he’s sixteen?

KENDRA: Just turned 18.

LARKIN: (Pg 16) (heavy sigh) Lemme see what I can find out, OK? (Pg 13-15) But I’m gonna need some additional information. (takes out a note pad and pencil) First name again?

KENDRA: Jamal. J-A-M-A-L

LARKIN: Last name “Connor.” DOB?

KENDRA: 5/1/1998. (should 17 years before the year of the performance)

LARKIN: Has he ever been arrested before?

KENDRA: He’s never so much as torn a tag off a new mattress, OK?

LARKIN: No AKA’s . . . you know “also known as.” Like street names.

KENDRA: (sarcastically) A “street name”? Like “Peanut” or “Black”?

LARKIN: Just in case he might have been printed for . . . (I don’t know; whatever) I need to make sure we have all the correct information.

KENDRA: Fine. [He’s] 6’2”; 185. Glasses. Cornrows. Light green eyes. (Pg 16) Are there that many 6’2” Black boys involved in “incidents” tonight? (Pg 22) Please. Go. Find Jamal. Find my son. (Larkin exits; beat) Unbelievable.

KENDR: (Pg 26-27) (Scott enters) Jesus Christ, Scott.

SCOTT: It’s OK. It’s gonna be fine.

KENDRA: They haven’t told me anything, Scott. They don’t even know if Jamal’s been arrested / or if he’s in custody . . .

SCOTT: Dammit. I got him the car. (Pg 30) The Lexus is registered to me. (Pg 27) It’s 4 am, I haven’t even had a friggin’ cup of coffee yet.

KENDRA: (Pg 31) (full of reproach) I’ve been here for almost an hour.

SCOTT: (Pg 35-37) (beat) Where was he last night? I assume he went out? With who? (beat) Kendra? Listen. You insisted J live with you. But you took on an obligation to be responsible. The kid is going to West Point in like a month. It’s just not acceptable that he -- Kenny, the last few times he’s stayed at my place, he’s looked like a damn gangster.

KENDRA: Why? ‘Cause he’s not wearing Brooks Brothers?

SCOTT: Baggy pants, cornrows. That stupid, loping, surly walk he’s suddenly developed.

KENDRA: You just don’t get it. He’s just trying to figure out who he is. His world is not your world, Scott.

SCOTT: His world is definitely my world. We spend almost a quarter of a million dollars putting that kid through the best private schools. He’s had every possible advantage. I will not accept him regressing into . . .

KENDRA: Into what?

SCOTT: Obviously something happened. He was driving around with two Black kids.

KENDRA: (Pg 38-40) He’s got a right to be in a car with his friends without getting dragged downtown at 3 am. Even if he’s in a car with his Black friends. You think our bougie son has no right to associate with other Black kids?

SCOTT: I think our half-White, half-Black, who-gives-a-shit-what-race-he-is son – the one who got a 1470 on his SAT and aced AP Physics – know better’n to commit unforced errors in life by taking stupid risks. The way you present yourself I life has consequences.

KENDRA: Scott – not matter how many privileges he’s got, the world still looks at him like it looks at me. . . not you.

SCOTT: Boy, I’ll tell ya . . . I can see exactly what’s been happening. I’m outta the house a few months and you’ve been pumping his mind full of victimhood psychobabble.

KENDRA: I’ve done nothing of the sort. Instead of pointing the finger at me, maybe you oughta be looking in the mirror. You’re the one who walked out on him.

SCOTT: (beat) I did not.

KENDRA: You did. I’m sorry, but that’s exactly what you did. You up and walked out on him.

SCOTT: I didn’t walk out on him. I walked out on you! (long beat) Look – J’s on his way to being a commissioned office at one of the most elite institutions on earth. My job is done. He’s a man now. (Pg 42-43) This is just some frivolous nonsense. He probably had his music cranked up too loud. Just . . . keep cool, half an hour – the 3 of us’ll be at Denny’s having a “teachable moment.”

KENDRA: (Pg 44) Scott, listen to me . .

LARKIN: (Pg 45-46) (enters with coffee) Sorry to interrupt. Coffee. No cream, no sugar. I got some more information. (reading from his note pad) Your son was identified as a vehicle occupant in a traffic stop. There were two other Black males in the vehicle: DeShawn Rolle and Jarvis Bell, a 20-year-old with misdemeanor convictions. He had an open warrant. (scans notes) A bumper sticker on the back of your Lexus: “Shoot Cops with your phone whenever they make a bust.” Shoot Cops in like huge letters. The rest in little-bitty font so’s all anyone could see was a Lexus that said “Shoot Cops.”

KENDRA: (Pg 47) It’s about camera phones not guns, Jesus.

SCOTT: Did you know? Please tell me you didn’t know about this.

KENDRA: There are three Black kids in his school. Out of 400 something and the other two are dating each other.

SCOTT: Right. No. I totally get it. Being one of the only Black kids at the most expensive prep school in the city entitles you to put a bumper sticker on your Lexus that says “shoot the stupid dumbass who got me this car”

KENDRA: He’s depressed. He’s confused. He’s grappling with a lot right now.

SCOTT: Bullshit.

KENDRA: (Pg 48-49) (to Larkin, confrontational) You know what? I sat around here almost an hour, you couldn’t tell me a damned thing. But as soon as my husband walks in – my White husband – all of the sudden you’re helpful as can be. Why is that? (Larkin exits)(to Scott) Put yourself in Jamal’s place. He’s the only Black person most of those White kids at his school know. His White friends think he represent the entire race. (beat) That bumper sticker was . . .

SCOTT: Was what? No, really – I want to understand.

KENDRA: Filming the cops is all these kids have. It’s their last line of defense. God forbid I’m stopped – it’s mine too. That’s the world we live in. Whether you get it or not. You really thing that’s what this is about? A bumper sticker?

SCOTT: (Pg 50-52) Look – if I’m a cop rolling down the street at 2 am and it’s a close call on probable cause . . .

KENDRA: The bumper sticker would push you over the edge?

SCOTT: Especially if I get some uppity asshole lecturing me on his rights.

KENDRA: “Uppity?” Is that what you just said?

SCOTT: Dammit, don’t make this about how I tripped on some coded word fossil. I can’t have J lapsing into a life where he makes excuses for himself all the time. I won’t.

KENDRA: And I won’t have him walk around apologizing for who he is.

SCOTT: No one’s asking him to do that.

KENDRA: Oh yes they are. “Keep your hands on the wheel, boy. Look straight ahead and don’t make any sudden moves. Wouldn’t wanna make the man with the bulletproof vest nervous when he walks up to your window with a Glock pointed at your head.”

SCOTT: I’m as eager to sort this out as you are. He’s my son too. I just don’t think lecturing these people about Black Lives Matter is gonna help. Let’s just try catching flies with honey, OK?

KENDRA: Maybe they need a little lecture. They sure finna get one when I sue they asses.

SCOTT: All I’m sayin’ – let’s not act like we’re in some back-asswards Klan county in South Carolina. This is Miami, for God’s sake.

KENDRA: (with sarcasm) Yassa, Massa Scott. Aunti Kendra don won hoit noboby feelins. Sorry, Massa Scott. (Pg 54-55) OK – know what? I’m not running cover for you anymore. He put the bumper sticker on the car to get back at you.

SCOTT: For what?

KENDRA: What do you think, Scott? For leaving him. Sorry – “leaving me.” That’s what all this is about. The bumper sticker. The cornrows. It’s a rebellion. Against you. For the first time in his life, he hates being half White. So get off my back about this ‘cause you don’t get to claim the high road here! ******* The Report*****

STOKES: (Pg 73-74) (with no emotion, to audience as if giving a report to the media) Jamal Connor was a rear seat passenger in a vehicle with a Jarvis Bell and a DeShawn Rolle. The car was tailed by a Metro cruiser near the Scott Projects in Liberty City where the driver was observed purchasing marijuana. Officer Rodney Banks pulled the car over. The camera shows the officer returns to his vehicle checking identification on his laptop. After 30 seconds, Mr. Bell exits the vehicle and attempts to approach the officer. The officer pulls his gun and gets Mr. Bell to the ground.

As the officer calls for backup, Rolle exits from the rear of the vehicle. Jamal Connor exits the vehicle. Jarvis Bell begins to stand up and take flight. The officer, now confronted with all 3 vehicle occupants

SCOTT: (scared) Oh, no . . .

STOKES: Fires three shots at the fleeing suspect. Either a stray shot or a ricochet . . . CSI is at the scene now . . . strikes Jamal Connor in the head killing him instantly.

SCOTT: I can’t breathe. I . . . I. . . can’t breathe . . .
```

---

## IC-0708: Angels in America: Millennium Approaches

- Title: Angels in America: Millennium Approaches
- Author (byline): Tony Kushner
- Work: Not specified
- Publisher: Theatre Communications Group
- Publication date as stated: April 1993
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: HARPER, JOE
- Teaser before the introduction: Yes
- Spoken words (computed): 1525
- Already set (do not supply): none

### Source block (context only)

```text
Author: Tony Kushner
ISBN: 978-1559360616
Publisher: Theatre Communications Group
Date (Month/Year): April 1993
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Harper is a mess. A quirky, loveable mess, but a mess all the same. Agoraphobic (afraid of public places) and hooked on valium, Harper spends most of her time hallucinating in her Brooklyn apartment while her husband, Joe, is away from home.

ACTRESS: Joe is a straight-laced Mormon from Salt Lake City adrift in big city of New York. Raised to think that homosexuality is a sin, he takes a giant step away from the morality he grew up with.

ACTOR: A society that encourages the repression of homosexuality isn't just harmful to gay people themselves.

ACTRESS: If Joe had felt comfortable with his sexuality, he never would have married Harper, and she wouldn't have suffered years of torture.

ACTOR: Maybe they would have just been good friends – who knows? Instead, societal pressure forced them into a life of denial.

ACTRESS: In this scene the walls of denial finally crumble.

TOGETHER: Angels in America: Millennium Approaches by Tony Kushner.
```

### Performance text (classify this)

```text
HARPER: People who are lonely, people left alone, sit talking nonsense to the air, imagining . . . beautiful systems dying, old fixed orders spiraling apart . . .

When you look at the ozone layer, from outside, from a spaceship it looks like a pale blue halo, a gentle, shimmering aureole encircling the atmosphere encircling the earth. Thirty miles above our heads, a thin layer of three-atom oxygen molecules, product of photosynthesis, which explains the fussy vegetable preference for visible light, its rejection of darker rays and emanations. Danger from without.

It’s a kind of gift, from God, the crowning touch to the creation of the world: guardian angels, hands linked, make a spherical net, a blue-green nesting orb, a shell of safety for life itself. But everywhere, thing are collapsing, lies surfacing, systems of defense giving way . . . This is why, Joe, this is why I shouldn’t be left alone. (Little pause)

I’d like to go travelling . . . Leave you behind to worry. I’ll send postcards with strange stamps and tantalizing messages on the back. ‘Later maybe.’ ‘Nevermore . . .’

HARPER: Where were you?

JOE: Out.

HARPER: Where?

JOE: Just out. Thinking.

HARPER: It’s late.

JOE: I had a lot to think about.

HARPER: I burned dinner.

JOE: Sorry.

HARPER: Not my dinner. My dinner was fine. Your dinner. I put it back in the oven and turned everything up as high as it could go and I watched till it burned black. It’s still hot. Very hot. Want it?

JOE: You didn’t have to do that.

HARPER: I know. It just seemed like the kind of thing a mentally deranged sex-starved pill-popping housewife would do.

JOE: Uh huh

HARPER: So I did it. Who know anymore what I have to do?

JOE: How many pills?

HARPER: A bunch. Don’t change the subject.

JOE: I won’t talk to you when you . . .

HARPER: No. No. Don’t do that! I’m . . . I’m fine pills are not the problem, not our problem. I WANT TO KNOW WHERE YOU’VE BEEN! I WANT TO KNOW WHAT’S GOING ON!

JOE: Going on with what? The job?

HARPER: Not the job.

JOE: I said I need more time.

HARPER: Not the job!

JOE: Mr. Cohn, I talked to him on the phone, he said I had to hurry . . .

HARPER: Not the . . .

JOE: But I can’t get you to talk sensibly about anything so

HARPER: SHUT UP!

JOE: Then what?

HARPER: Stick to the subject.

JOE: I don’t know what that is. You have something you want to ask me? Ask me. Go

HARPER: I . . . . can’t. I’m scared of you.

JOE: I’m tired. I’m going to bed.

HARPER: Tell me without making me ask. Please.

JOE: This is crazy, I’m not . . .

HARPER: When you come through the door at night your face is never exactly the way I remembered it. I get surprised by something . . . mean and hard about the way you look. Even the weight of you in the bed at night, the way you breathe in your sleep seems unfamiliar. (Beat) You terrify me.

JOE: I know who you are.

HARPER: Yes. I’m the enemy. That’s easy. That doesn’t change. You think you’re the only one who hates sex; I do; I hate it with you; I do. I dream that you batter away at me till all my joints come apart, like wax, and I fall into pieces. It’s like a punishment. It was wrong of me to marry you. I knew you . . . (She stops herself) It’s a sin, and it’s killing us both.

JOE: I can always tell when you’ve taken pills because it makes you red-faced and sweaty and frankly that’s very often why I don’t want to . . .

HARPER: Because . . .

JOE: Well, you aren’t pretty. Not like this.

HARPER: I have something to ask you.

JOE: Then ASK! AKS! What in the hell are you . . .

HARPER: Are you a homo? (Beat) Are you? IF you try to walk out right now I’ll put your dinner back in the oven and turn it up so high the whole building will fill with smoke and everyone will asphyxiate. SO help me God I will. Now answer the question.

JOE: What if I . . . (Beat)

HARPER: Then tell me, please. And we’ll see.

JOE: No. I’m not. I don’t see what difference it makes. (Beat) I think we ought to pray. Ask God for help. Ask him together . . .

HARPER: God won’t talk to me. I have to make up people to talk to me.

JOE: You have to keep asking.

HARPER: I forgot the question. Oh year. God, is my husband a . . .

JOE: Stop it. Stop it. I’m warning you. Does that make any difference? That I might be one thing deep within, no matter how wrong or ugly that thing is, so long as I have fought, with everything I have, to kill it. What do you want from me? What do you want from me, Harper? More than that? For God’s sake, there’s nothing left, I’m a shell. There’s nothing left to kill. (Beat) As long as my behavior is what I know it has to be. Decent. Correct. That alone in the eyes of God.

HARPER: No, no not that, that’s Utah talk, Mormon talk. I hate it, Joe, tell me, say it . . .

JOE: All I will say is that I am a very good man who has worked very hard to become good and you want to destroy that. You want to destroy me, but I am not going to let you do that. (Beat).

HARPER: I’m going to have a baby.

JOE: Liar.

HARPER: You liar. A baby born addicted to pills. A baby who does not dream but who hallucinates, who stares up as us with big mirror eyes and who does not know who we are. (Beat)

JOE: Are you really . . ..

HARPER: No. Yes. No. Yes. Get away from me. Now we both have a secret. (Beat) When you pray, what do you pray for?

JOE: I pray for God to crush me, break me up into little pieces and start all over again.

HARPER: Oh. Please. Don’t pray for that.

JOE: I had a book of Bible stories when I was a kid. There was a picture I’d look at twenty times every day: Jacob wrestles with the angel. I don’t really remember the story, or why the wrestling – just the picture. Jacob is young and very strong. The angel is . . . a beautiful man, with golden hair and wings, of course. I still dram about it. Many night. I’m . . . It’s me. In that struggle. Fierce, and unfair. The angel is not human, and it holds nothing back, so how could anyone human win, what kind of a fight is that? It’s no just. Losing means your soul torn down in the dust, your heart torn out from God’s. But you can’t not lose.

HARPER: In the whole entire world, you are the only person, the only person I love or have ever loved. And I love you terribly. Terribly. That’s what’s so awfully, irreducibly real. I can make up anything but I can’t dream that way.

JOE: Are you . . . are you really going to have a baby?

HARPER: It’s my time, and there’s no blood. I don’t really know. I suppose it wouldn’t be a great thing. Maybe I’m just not bleeding because I take too many pills. Maybe I’ll give birth to a pill. That would give a new meaning to pill popping, huh? I think you should go to Washington. Alone.

JOE: I’m not going to leave you, Harper.

HARPER: Well maybe not, But I’m going to leave you.

JOE: Harper. Please listen. I still love you very much. You’re still my best buddy; I’m not going to leave you. Please listen. Stay. This is really hard. We have to talk.

HARPER: We are talking. Aren’t we. Now please shut up. OK?

JOE: Just listen. You want the truth. This is the truth. I knew this when I married you. I’ve know this I guess for as long as I’ve known anything, but . . . I don’t know, I thought maybe that with enough effort and will I could change myself . . . but I can’t . . . I’m losing ground here, I go walking, you want to know where I walk, I . . . go to the park or up and down 53rd Street, or places where . . . And I keep swearing I won’t go walking again, but I just can’t. (Beat) I try to tighten my heart into a knot, a snarl, I try to learn to live dead, just numb, but then I see someone I want, and it’s like a nail, like a hot spike right through my chest, and I know I’m losing. My whole life has conspired to bring me to this place, and I can’t despise my whole life. I think I believed when I met you I could save you, you at least if not myself, but . . . I don’t have any sexual feeling for you, Harper. And I don’t think I ever did. (Little pause)

HARPER: I think you should go.

JOE: Where?

HARPER: Washington. Doesn’t matter.

JOE: What are you talking about?

HARPER: Without me. Without me, Joe. Isn’t that what you want to hear? (little pause)

JOE: Yes.

HARPER: You were going to save me, but the whole time you were spinning a lie. I just don’t understand that. . . This is so scary, I want this to stop, to go back . . .

JOE: Harper . . . As long as I’ve known you Harper you’ve been afraid of . . . of men hiding under the bed, men hiding under the sofa, men with knives. Who are these men? I never understood it. Now I know.

HARPER: What?

JOE: It’s me. . . . I’m the man with the knives.
```

---

## IC-0709: Animate Me

- Title: Animate Me
- Author (byline): Ruth Clampett
- Work: Not specified
- Publisher: Clampett Studio Collections
- Publication date as stated: May 2013
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: NATHAN, BROOKE, ACTRESS, ACTOR
- Teaser before the introduction: Yes
- Spoken words (computed): 1284
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ruth Clampett
ISBN: 978-0989391900
Publisher: Clampett Studio Collections
Date (Month/Year): May 2013
```

### Introduction (context only: never use it for content warnings)

```text
TOGETHER: Animate Me by Ruth Clampett
```

### Performance text (classify this)

```text
NATHAN: (Pg 329) There was once a boy, who longed to meet a special girl, yet he couldn’t find her . . . that boy was me. Every girl I met was too hip, or mean, or not appealing . . . But one day, while I sat at a big company presentation, the most beautiful girl walked across the stage. (As he speaks, Brooke enters, steps up to a podium, adjusts the microphone and begins to speak in silent pantomime) She was smart, and funny, and charming . . . and beautiful.

BROOKE: (Pg 157) This is for the animation artists who put their hearts and souls into their work to create magic for us all. I’m honored to be a part of their world.

NATHAN: (Pg 330) And in that single moment, I fell in love.

(Nathan is behind the counter at his 2nd job – A computer store. He’s doodling when Brooke walks in)

BROOKE: (Pg 10-15) Hey, can you help me?

NATHAN: (to audience) Brooke Tobin, the woman of my dreams! (coming around the counter a little too enthusiastically) Sure, what can I help you with?

BROOKE: I need a cord thingy for my computer, and I’m not sure which one.

NATHAN: (trying to sound like an authority) Do you need a USB? (Brooke looks perplexed. Nathan pushes his glasses up his nose) The USB connection simplifies the process of connecting peripherals to the computer and offers much higher data transfer rates.

BROOKE: (puts her hands on her hips and steps in to read his name tag) Na-than? I don’t speak tech geek. Can you give it to me straight? I just want a cord thingy so I can hook my old computer to my new one.

NATHAN: Uhhh, uhhh . . . this is probably what you need.

BROOKE: (as they head to the register) How much do I owe you?

NATHAN: Twelve forty-nine. (to audience) When she starts to set her money down I realize that my sketchbook’s still open. (Nathan hastily closes the book and holds it to his chest)

BROOKE: Was that your drawing? Are you an artist?

NATHAN: Yeah . . . well, actually, I’m an animator. I work at Sketch Republic too. You’re Brooke in development, right? (To audience) Good, that sounded cool . . . believable – like I don’t dream about her all day.

BROOKE: Sorry I didn’t recognize you. So what are you doing here? Don’t we pay you enough? Show me your work. (Reaching for the sketchbook) Are you good?

NATHAN: I’m really good and I’d love to show you my work, but this is just scribbling. (Putting the book under the counter) I want to show you the good stuff.

BROOKE: Okay, when you’re ready, I’d be happy to look at your work. You know where to find me . . . . (she turns to leave. Nathan watches her every move; she turns) You know, Nathan, don’t let the cool clothes fool you. Deep down I’m a fan-girl geek. (she exits)

NATHAN: (to audience) I am in love. (pg 330) [But] I’d never have a chance with [her]. [So] I took all my passion and dreams and put my energy into creating a character in [her] likeness. (holds up a sketch for the audience to see) And B-Girl was born – with sparkling eyes and flowing hair. Strong, brave and beautiful . . . just like Brooke.

******Scene Change******

(The next day at the office – Brooke is at her desk when Nathan shows up at her door with coffee in hand)

NATHAN: (Pg 20 – 23) I brought you coffee.

BROOKE: Thank you! (She takes the coffee and sips.) Mmmmm. If Arnauld saw you got me this, he would insist that you’re flirting with me, but I think you’re just a really nice guy. Which is it?

NATHAN: (To audience) My stomach flip-flops as I try to think how to respond. She smiles at me and lifts the cup. I’ve sketched her on the cup with a “B” on her chest like Superman’s “S” and a cape flapping behind her.

BROOKE: How did you know I was a superhero? That’s top-secret information.

NATHAN: Well, I’m one too. I sensed it with my super powers. (To audience) Wow, this is like a real conversation.

BROOKE: (Pg 25-26) Thanks so much for the coffee. It’s been a crazy day. At least let me pay for it.

NATHAN: No. I’ve been taking a class on chivalry, so this is coursework. You’re helping me out actually.

BROOKE: Really? What other classes are you taking?

NATHAN: Conversation skills. Can I practice with you?

BROOKE: Sure, I’ve got a minute. I’m all yours. (motions with her hand for Nathan to continue)

NATHAN: (flustered, he completely blows it) So is Arnauld really your boyfriend?

BROOKE: (Brooke makes a face) (pg 39) [He] says I’m getting fat and need to work out more. (She turns and looks over her shoulder) Do you think my *butt* looks too big? That’s what Arnauld said.

NATHAN: (Stammering) Ah . . no . . . I think your bottom looks great . . . really, really, really . . . great.

BROOKE: See this is why I should be dating someone like you . . . You’re so sweet. As for Arnauld, I suppose this is what I get for dating a gym addict. He has such an incredible body, but it makes him expect everyone else to have one too.

NATHAN: (To audience) I don’t want to hear about Arnauld’s incredible body. I wish he were a sloth with a beer belly and . . (To Brooke) Does he have hair on his back at least?

BROOKE: No . . he gets it waxed. (giggling) He’d look like a monkey if he didn’t . . . .

NATHAN: (Pg 148) (To audience) The entire walk back to my [cubicle] I plot my revenge. The caricature I’ve got planned will be a pre-waxed Arnold in the Amazon, swinging from a vine with a very small banana. TRANSITION

ACTRESS: There are ups and downs, lots of coffee break visits.

ACTOR: But despite the annoying Monkey Man lurking in the background, over time their relationship grows . . .

ACTRESS: Until, a month later when Arnauld, the illustrious president of Sketch Republic, makes a very public announcement

ACTOR: He and Brooke are getting married!

NATHAN: (pg 224 – 225) (to Audience) I fire up my computer. My task is very specific. Google Search: How to woo a girl. I find just what I’m looking for on Wiki Answers.

BROOKE: (off stage as the computer voice) Show interest . . . look in her eyes when you speak.

NATHAN: Yeah, yeah, yeah

BROOKE: Whisper in her ear

NATHAN: That’s weird, but easy. Do they mean all the time? That would be ridiculous

BROOKE: Learn to dance.

NATHAN: Seriously? That has disaster written all over it.

BROOKE: Take the first step. If you’re ever going to win the prize you have to tell the prize you want it.

NATHAN: Now that makes sense to me! (To audiene) I read the list three times, jotting down ideas on note cards. (Brooke’s voice off stage keeps softly repeating the instructions under Nathan’s monolog; Nathan in words and pantomime) I tape up everything on my bathroom mirror so I can review the suggestions often.

(Nathan picks up his phone and dials – speaking confidently) Hey Brooke, it’s Nathan. I’d like to take you to dinner tonight so we can talk. (awkward pause, then nervously) So, um, give me a call . . . okay . . . thanks . . .bye. (another long pause) Just to let you know . . . I’m not going to let you marry him. TRANSITION

ACTOR: No response from Brooke except for a cryptic text:

ACTRESS: (texting) Sorry, can’t do dinner, at Arnauld’s now.

ACTOR: And when she doesn’t show up at work the next day, Nathan, of course, gets a little crazy and begins texting Brooke like a drug addict fresh out of rehab . . . .

ACTRESS: All. Day. Long.

NATHAN: (to audience while Brook pounds relentlessly on his front door) (Pg 231-235) The crazed beating on my front door is the first indication that this won’t be a pleasant visit.

BROOKE: What’s wrong with you? Have you lost your mind? Why did you call or text me every fifteen minutes today?

NATHAN: But, I needed to talk to you . . .

BROOKE: Right. Got that. But maybe I needed some space and silent support, not more pressure! (Begins to cry she’s so angry) My boss and quasi-boyfriend announced to the entire company that he was marrying me like I’m some idiot mail order bride. I’ve been trying to find another job, so I could finally get out from under him. And you! (She pushes him) You’re the one who’s stirred everything up. You and your damn pedestal, treating me like I’m sooo perfect . . . I’m a mess, Nathan. The sooner you figure [that] out the better off you’ll be.

NATHAN: (crossing his arms and matching her intensity) [Well,] I’m not going anywhere. . . . Besides, even if you are a mess, you’re my perfect mess.

BROOKE: Quit saying that! I’m not perfect Nathan . . . not even close. (taking a deep breath that shivers from left-over tears they have a moment of eye contact) Whatever am I going to do with you. (she smiles) Thank you . . . I actually feel a little bit better. I’m sorry I yelled at you.

NATHAN: And pushed me . . . I’m not. I think you needed that. We both did.

BROOKE: (wiping the tears from her cheeks) Ugh, I’m a mess. Where’s the bathroom.

NATHAN: First door on the right. (Brooke exits) (to himself) (Pg 234-235) She’s been trying to leave Arnold. She wants a new job, she thinks she’s a mess . . . wait Oh, no! (To audience) Brooke is in my bathroom . . . where the instructions are posted. (The bathroom door opens and Brooke steps out with a notecard in her hand and silently hands it to Nathan)

BROOKE: (Pg 239-241) Read it.

NATHAN: (Embarrassed beyond words) Today is the day I will tell Brooke that I’m in love with her? (He can’t look up)

BROOKE: So are you going to tell me?

NATHAN: (Nathan looks up and says softly) I’m in love with you, Brooke.

BROOKE: (Pushes Nathan playfully) Like you mean it!

NATHAN: (Nathan shakes off his mortification and drops to one knee, proclaiming loudly) I’m in love with you, Brooke. Completely, utterly, overwhelmingly in love with you.

BROOKE: (Pg 371) (pause, helping Nathan to his feet) You know something . . . you animate me, Nathan. It’s as if you’ve brought the real Brooke to life.

NATHAN: The real Brooke just needed someone to believe in her.
```

---

## IC-0710: Anniversary

- Title: Anniversary
- Author (byline): Conrad Bishop
- Work: One Act Plays for Acting Students, Pg 6-12
- Publisher: Meriwether Publishing
- Publication date as stated: Dec 1990
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MAN, WOMAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1548
- Already set (do not supply): none

### Source block (context only)

```text
Author: Conrad Bishop
Book: One Act Plays for Acting Students, Pg 6-12
ISBN: 978-0916260477
Publisher: Meriwether Publishing
Date (Month/Year): Dec 1990
```

### Introduction (context only: never use it for content warnings)

```text
WOMAN: Today, half of all marriages end in divorce, and only half of those that endure are truly happy in the long run.

MAN: Pre-marriage counseling is based on the reality that it's important to strengthen your relationship and prepare constructively for future challenges and conflicts that everyone will inevitably face at some point.

WOMAN: Research shows that there is a window of opportunity during the year before the wedding and the six months or so after when couples get the optimum benefit from marriage counseling.

MAN: Later, under stress, negative habits and relationship patterns may become established and be much harder to resolve.

WOMAN: For instance . . .how many couples would think to resolve the issue of who takes out the garbage before it leads to divorce?

TOGETHER: Anniversary by Conrad Bishop
```

### Performance text (classify this)

```text
Takes place in the present in the home of a sophisticated young couple celebrating their first anniversary.

MAN: (Pg 6-12) Terrific meal

WOMAN: For a terrific couple.

MAN: Happy anniversary, honey.

WOMAN: The first of many.

MAN: Many happy returns.

WOMAN: Speaking of returns, do you want to look at the bills?

MAN: This is our anniversary, honey.

WOMAN: There's a final notice.

MAN: Yeh, but. . .

WOMAN: I'll put them on the desk.

MAN: So many things have happened in one year. So many adjustments.

WOMAN: Adjusting, learning to give and take. . .

MAN: Take charge of our lives, face up to our problems and solve them.

WOMAN: And now that we've solved them, it should really be nice.

MAN: Because it has been kind of rough, you know. . .

WOMAN: Well sure, it's hard to grow. We've grown personally.

MAN: We have. Like our quarrels have grown... I mean they've matured.

WOMAN: Our anger, we've learned how to deal with it. That magazine article. . .

MAN: "Have Fun with Your Anger."

WOMAN: And you know, when we have kids, I am never going to be angry with them. It's just not necessary. If you love them and raise them the right way, they'll never cause you problems.

MAN: Not many couples could say on their first anniversary that they have solved all their significant problems.

WOMAN: But it's true.

MAN: I think we're way ahead of most couples. Maybe five years ahead of most.

WOMAN: Happy anniversary, honey. (They kiss and turn front) Our marriage, well it's hard to talk about because it really has been this incredible experience. . .

MAN: Incredible but believable. We're more than just married. We're good friends.

WOMAN: Friends, of course we're more than just friends. It's so stimulating, so liberating... I’ve been liberated to do so much. New furniture, new colors, new recipes. . .

MAN: Zulu cookery. We have so many tastes in common. Even colors. Now the brighter end of the chartreuse scale is not often. . .

WOMAN: It's not often found so early in a marriage.

MAN: Really incredible. (They turn to one another)

WOMAN: Honey, before it gets too late and we get involved in something else, could you take out the garbage?

MAN: Huh?

WOMAN: Would you take out the garbage? It's kind of piled up.

MAN: Honey. . . you're gonna laugh.

WOMAN: What?

MAN: The garbage. I just can't cope with the garbage.

WOMAN: Oh. Well, as long as it's out before breakfast.

MAN: No. I don't mean garbage now. I mean garbage always. Garbage forever.

WOMAN: But we agreed: garbage is your province. Do you think we're making too much garbage, is that it?

MAN: It's not a recycling question, or a question of less garbage or better garbage. It's the fact of garbage.

WOMAN: Well, it's a human fact. We all generate refuse. If you put two people together. . .

MAN: That's it. That's it. This is our product. Our love, our sensitivity, our relationship results in this. . . horrible accumulation. Oh, I know it's a petty little thing, but. . .

WOMAN: It's not petty. There are three sacks of it. Honey, this is our anniversary. I would like it to be a garbage-free anniversary.

MAN: And how can we really, truly say Happy Anniversary when there is this external manifestation of our relationship bulging across the kitchen at us? The Johnsons? Two doors down? He goes out once a week with a little plastic thing. It doesn't look like garbage, it doesn't smell like garbage. It's an intense but comprehensible concentration of semi-organic substance, like the Johnsons. But ours. . .

WOMAN: I don't understand.

MAN: Take out the garbage. Please. You take out the garbage

WOMAN: I could take out the garbage. But I think there's something more basic here.

MAN: Honey...

WOMAN: Why do you want to give me the garbage when you hate it so much?

MAN: I'm not giving it to you.

WOMAN: I just don't like the idea of having it thrust into my hands.

MAN: I'm not thrusting.

WOMAN: You are thrusting.

MAN: Why do you use these masculine images? I'm not trying to thrust it, I'm trying to . . . share it! . . . You've never had the freedom to take out the garbage, and I want that experience for you

WOMAN: Well. . . thank. . . you. . . (They turn front) It is a dilemma, of course, not that it can't be worked out. I have a great concern for the garbage, just as much as Chris does, because it seems to have this place of importance in our lives. . .

MAN: It's a kind of focal point for a lot of things, and maybe if we can just focus on the focal point, things will come more into focus.

WOMAN: Because very often, in terms of taking responsibility, Chris has a tendency to . . . give it to me. And we thought perhaps we should work this out the way we work things out. He would state what he feels and I would state what I feel. Which we did. I stated that the garbage needs taking out.

MAN: And I agreed. But I stated that I had a very negative reaction to her tone of voice in stating her statement.

WOMAN: So I tried to find a better tone of voice in which to state the needs of the garbage, in order to strike a better balance between Chris's needs and those of the garbage. I tried a plain old "Take out the garbage."

MAN: That's very blunt.

WOMAN: OK. "Honey, I wonder if I might ask you to expel the garbage?"

MAN: It rings false.

WOMAN: OK. "Sweetheart. Dearest. I know you don't like to, because there's a lot on your mind such as solving the nation's balance of payments and also paying our bills, but I really don't know where to put any more garbage. Should I pile it in the bathroom or the closets, or put it in the bed as a helpful hint, or serve it again for dinner? Or maybe we could sleep in the garage and use the house for the garbage but could you please take it out?"

MAN: I hate attempts at humor.

WOMAN: "Oh, look at this! It's the garbage! It would be so much fun to do something with this! But I need a big strong man to do it! And everyone will look out their window and say, "What a big strong man going down those stairs! Doesn't he take good care of her garbage!"

MAN: She really misses the whole point.

WOMAN: "Hey baby, haul my garbage!" . . . Not to take away from our anniversary.

MAN: Because it really is a very happy anniversary, really. . .

WOMAN: Really, really, really incredible. (They turn to one another, and start to laugh)

MAN: I don't know how we got into this.

WOMAN: Neither do I.

MAN: I mean I don't think it's really a problem. It's just a new aspect of our relationship.

WOMAN: Though it is an aspect that's beginning to pile up.

MAN: Look, I'm not trying to shove it under the rug.

WOMAN: No way, no way. Let's put it out in the middle of the rug. Some people have potted plants, we'll have canned fungus. The mold will just match the color scheme. . . Go on. Say something.

MAN: No.

WOMAN: Don't repress it.

MAN: I have to repress it.

WOMAN: You don't have to repress it.

MAN: You make me repress it.

WOMAN: I just said it: Don't repress it. Don't repress it.

MAN: But your attitude is repress it, repress it.

WOMAN: OK then, repress it! Only repress it better!

MAN: Look, we both know that in order to be resolved this has to come out some way, and not destructively, of course, but in a constructive way that will bring us closer together. . .

WOMAN: OK then do it! Do it! Do it!

MAN: OK. OK. OK. I'm sick of it all and it has nothing to do with the garbage. It's you and the job and the marriage. I want to throw up. I want to break every window in this mousetrap house. I want to get in the car and take off ninety miles an hour to California and forget I ever got in this because I can't stand the thought of fifty more years of ~he same damn thing. I want to give all the wedding presents to Goodwill and you come at me with this earnest little mousy sarcastic whine and patch it up with one sincere conversation a week and we make a list that we lose under all the garbage. We spew out day and night and I'm sick of it all! . . . Wow. I feel better.

WOMAN: You do.

MAN: Yes. I feel good. Do you feel good?

WOMAN: No.

MAN: We have a better understanding.

WOMAN: Can I react to that?

MAN: I don't need a reaction.

WOMAN: You. . . insensitive. . . insincere. . . insecure. . . immature. . . (Phone rings)

MAN: Telephone.

WOMAN: (She answers it. Total change of tone) Hello? . . . Linda, hi! Oh nothing, just celebrating our anniversary. Talking things over, making plans.

MAN: Tell her about the house.

WOMAN: We looked at a new house. It's incredible! Big lawn, carpets, all electric... George wants to say Happy Anniversary.

MAN: . . . Yeh, made it through the first. Fifty more to go. Yeh, incredible. Everything is incredible. Appreciate it. Yeh. Bye. (Hangs up. Silence)

WOMAN: Nice of them to call.

MAN: We called them on theirs. (Long silence) When do you want to see the lawyer?

WOMAN: I'll call Monday. . .

MAN: You use ours. I'll find a new one.

WOMAN: Everything should be fifty-fifty.

MAN: Even the garbage.

WOMAN: It's good we can be mature about things.

MAN: Make a rational judgment before we get. . . too involved.

WOMAN: You want me to pack you something?

MAN: No, I'll stop by tomorrow.

WOMAN: You know, I think we still are way, way ahead. A lot of couples, it takes, oh, six or seven years before they split. We've saved all those years.

MAN: I wonder what would happen. . . if one of us . . . sort of. . .

WOMAN: Gave in? Compromised?

MAN: Probably. . . set a bad precedent. . . Well, happy. . .

WOMAN: Yes. . . happy. . . (They shake hands. Silence)

MAN: Incredible.
```

---

## IC-0711: Apocalyptic Butterflies

- Title: Apocalyptic Butterflies
- Author (byline): Wendy MacLeod
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: July 2001
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: HANK, MURIEL, FRANCINE, TRUDI, TOGETHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1408
- Already set (do not supply): none

### Source block (context only)

```text
Author: Wendy MacLeod
ISBN: 978-0822200604
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): July 2001
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Cooped up in their cramped cottage in a remote part of Maine, Hank and Muriel Tater are beginning to get on each others’ nerves

ACTRESS: They have still not agreed on a name for their seven-week-old daughter,

ACTOR: Muriel refuses to accept motherhood and housework as a full-time occupation.

ACTRESS: And Hank is having an affair with a busty checkout girl at the local IGA store.

ACTOR: In this series of scenes, we see Hank desperately trying to understand his position as a husband,

ACTRESS: But despite conversations with his wife, his mother and his mistress . . . Hank just doesn’t seem to“get it”

TOGETHER: Apocalyptic Butterflies by Wendy MacLeod
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

NOTE: Muriel is Hank’s wife, Trudi is his mistress and Francine is his mother.

Hank is agitated, perhaps pacing when Muriel enters from outside with the baby and diaper bag.

HANK: (Pg 26-29) Where you been?

MURIEL: Where you been?

HANK: I asked you first

MURIEL: I stayed over your parents.

HANK: Why'd you stay over there? You got a house. What is this? I’m your husband. You’re acting miserable. I get miserable just looking at you. Last time I seen you smile was [insert date]. You’re like a pod person.

MURIEL: (Looking around) This place is a dump. How long you been sitting here? You never once thought to pick up.

HANK: I thought about it, but I was too aggravated. I was wondering where you were. I thought you were with a man.

MURIEL: What man?

HANK: Any man. A man with a college education.

MURIEL: Let me ask you something. Where would I find a man with a college education in this town?

HANK: The ski resort

MURIEL: You thought I was with a skier with a college education.

HANK: It flashed before my eyes, yeah.

MURIEL: No one wants me, Hank. I'm not beautiful. I wear glasses.

HANK: You are. You are beautiful.

MURIEL: What the hell is this? In the sink, what's in the sink? (Muriel hands the baby to Hank, grabs a sponge and furiously starts cleaning)

HANK: Coffee grounds. I'll take care of it

MURIEL: How long have these grounds been in here? This will never come out

HANK: Just use a little of the green stuff on it, the ...

MURIEL: Comet! It's called Comet! Clean people use it to clean their houses! Men and women all over America use Comet to clean their houses!

HANK: Who's acting crazy now Muriel?

MURIEL: How many times have I told you I need some help running this house, I am not your maid! I am a Magna Cum Laude graduate of the University of Maine Augusta. I change this baby twelve times a day, when she sleeps I stay awake with my ear tuned to a baby intercom. When she's hungry I get up and I feed her, when you're hungry I feed you and in between everybody's hunger I clean and I clean and I clean and this house still looks dark and dirty! (Muriel starts to get the baby's things together)

HANK: Where ya going?

MURIEL: Howard Johnson's motel where somebody else cleans the room! (Muriel exits with the baby and the diaper bag)

****** Hank’s mother’s trailer *****

HANK: (Pg 29-31) She took the baby and went to the Howard Johnson's. I didn't get to the cleaning like I promised so bam she's out the door, screaming about coffee grounds. I don't know what to do, Ma, I don't know what to do.

FRANCINE: Why don't you clean the house like you promised?

HANK: Right Exactly. Take her side. See it through her eyes. She's dropping a bundle at the Hojos, putting it on my plastic and she's the victim. I work 40 hours a week, what the hell does she do?

FRANCINE: She works 80 hours a week, bubba.

HANK: Bubba?

FRANCINE: You used to be more than some bubba. Then you started acting like the rest of this town with the pick-up and the language and the girls.

HANK: What girls?

FRANCINE: The girl at the IGA. What's her name? The girl with the chest (Hank shrugs, indicating no knowledge) You better know her name! If you slept with some girl and you don't even know her name . . .

HANK: Trudi.

FRANCINE: Get rid of the girl, Hank. If Muriel doesn't know for sure she senses. You don't need a girl, you need a wife.

HANK: She hasn't been a wife to me. She hasn't been a wife to me for a long, long time. Muriel she don't love me no more. I try to touch her, she turns away.

FRANCINE: Maybe she's tired from the baby.

HANK: My house has a disgusting smell. There's the crying and the diapers and the smell of milk boiling. Trudi she wears this body lotion, this perfume lotion. Ciara. Like the wind.

FRANCINE: There's nothing wrong with the way your house smells, Hank. Your house smells like life. When are you gonna name that baby? A baby needs a name, Hank. There's something not right about a baby with no name. . . . (Pg 32-34) Do the right thing. Call up the girl, Hank, tell her it's over. (Pause)

HANK: I can't break up with her on the phone.

FRANCINE: Well, you can't go see her.

HANK: I can't go to her house, she can't come to my house, I can't call her, what am I supposed to do?

FRANCINE: Write her a letter.

HANK: Okay but you gotta assist me 'cause I don't know how not to hurt a woman's feelings. (Hank gets a pad and pencil) Dear Trudi, You are a very nice girl. The nicest. The sweetest girl I met in a long time.

FRANCINE: Hank. You're breaking up with her.

HANK: Dear Trudi, My mother says I should make up with Muriel and name my baby. Neither of these things involve you so good-bye. Hank. (Pause) It's no good. I can't break up with her in a letter, I got to see her in person -- prove to myself I can resist her temptations.

FRANCINE: The best way to resist temptation is to avoid temptation.

HANK: Ma, this is what's gonna happen. I'm gonna go home. Muriel' s gonna remain elsewhere. I'm gonna call Trudi, tell her come over I gotta talk with her, then I'm gonna tell her me and her we're a memory. . . I’m gonna kiss her softly and sweetly . . . .

FRANCINE: Watch that softly and sweetly stuff!

HANK: . . . on the forehead! Right Ma. I gotta go!

FRANCINE: (Calling after him) What if Muriel comes home?

HANK: She won’t. I know that woman like I know discount shoes! *******Hank and Muriel’s Home ******

TRUDI: (Pg 35) You sure it's okay? I got beat up one time by a wife. Where's Muriel?

HANK: (Pg 36-37) She's at the Howard Johnson's. She's temporarily left me.

TRUDI: She find out about me?

HANK: It was something else. It pertained to coffee grounds.

HANK: Trudi, I can't come around no more. I'm breaking up with you.

TRUDI: Okay.

HANK: Okay. That's it? You're not rejected and sad and crumpled?

TRUDI: No.

HANK: You didn't love me?

TRUDI: Probably not.

HANK: But you said you did. You said I love you, I love you. Didn't you ever think what if I left Muriel and married you?

TRUDI: No. I mean, who wants to marry a guy cheats on his wife? Muriel's in it for the long haul. I just use married men as a resource. You thought about getting married to me?

HANK: Yeah. I'm one person with you. I'm another person here.

TRUDI: (Pg 38-39) You're the same person. I want to kiss this person good- bye.

(Trudi and Hank kiss. Muriel enters carrying the baby. She sees them, registers it and walks back out. Beat. Trudi and Hank look at each other. Muriel re-enters.

MURIEL: You, tits, get out of my house!

(Trudi exits. Hank furiously begins to scrub the sink. He tapers off and looks at Muriel.)

HANK: I was breaking it off with her.

MURIEL: You obviously weren't being real firm about that!

HANK: She wanted to kiss me good-bye.

MURIEL: Kiss me good-bye baby, 'cause I'm outta here. You insult me. You insult everything I am by choosing my opposite.

HANK: You looked at me like I wasn't here, like in your head you'd already left me. The baby cries when I try to hold her, and when I try to hold you, you move away (Muriel heads for the door) IT'S SNOWING OUT THERE! You'll skid, you'll die, I'll never see you again. I'll never see the baby again. I'll be in a dark suit following two coffins to the grave, ladies in veils will hand me tissues.

MURIEL: Okay. I'll stay. You get out I'm the injured party, you get out.

HANK: Muriel, I am a man with primordial urges. . .

MURIEL: You could do with a few less primordial urges, buddy.

HANK: Yeah right Muriel, stick the knife in and twist it. I bring you my shame. I have deposited my shame at your feet and still you torment me.

MURIEL: Your shame. You've deposited your shame at my feet?

HANK: Yeah.

MURIEL: BIG DEAL! I don't want your shame. I can't use your shame. I can’t frame your shame and put it up on my wall. I can’t cook your shame and eat it for breakfast. I can’t bottle your shame and dab it behind my ears. Your shame means nothing to me!

HANK: (Pg 12) JESUS CHRIST MURIEL!

MURIEL: What?

HANK: Be nice to me. Be sweet to me. I need . . . some sweetness in my life.

MURIEL: (Pg 42) Save your breath, Hank. Things were bad long before I walked in this house tonight. There is nothing there is nada there is zero you could possibly say to me to make me reconcile with you! (the baby gurgles)

HANK: (Pg 45) She’s giggling at me this baby. (Hank takes the baby, focuses on her instead of Muriel) Who’s giggling me? Who’s giggling me? (to Muriel) Muriel. A name flashed before my eyes. Not (pg 13) Lorelei or Jessica or Velvet or Elvira (pause) (Pg 45) A hybrid name like two flowers joined together. Your name and my name. Together.

MURIEL: Murank?

HANK: No, my real name. Henry. Henriel.

MURIEL: Henriel?

TOGETHER: (softly) Henriel.
```

---

## IC-0712: Arms

- Title: Arms
- Author (byline): Bekah Brunstetter
- Work: Best Ten-Minute Plays for Actors, 2007
- Publisher: Smith and Kraus
- Publication date as stated: July 2008
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: CHARACTERS, SAM, SIS, SIS/SAM
- Teaser before the introduction: Yes
- Spoken words (computed): 1454
- Already set (do not supply): none

### Source block (context only)

```text
Author: Bekah Brunstetter
Book: Best Ten-Minute Plays for Actors, 2007
ISBN: 978-1575255897
Publisher: Smith and Kraus
Date (Month/Year): July 2008
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: Twins have a special bond. And if they live their lives physically connected to each other as well, the bond becomes increasingly strong.

ACTRESS: There is a social debate surrounding conjoined twins worldwide. Should the twins be separated as early as possible, even if separation would threaten the lives of one or both of the children?

ACTOR: Or should no surgical action be taken until the twins are old enough to decide for themselves whether they want to live out their lives conjoined or separately?

ACTRESS: After all, Abigail and Brittney Hansel have lived very successfully . . . together . . . conjoined.

ACTOR: This short play, Arms by Bekah Brunstetter explores the psychological effects of conjoined twin separation when 1 twin values the independence

ACTRESS: . . . and the other twin is suffering from a deep dependency disorder.

TOGETHER: Arms by Bekah Brunstetter.
```

### Performance text (classify this)

```text
CHARACTERS: Siamese twins, one month after they have been surgically removed from each other. Sis has no left arm. Sam has no right arm.

Late night, a park. Sis, twenty, sits on a bench, playing with a bracelet. She is dressed as Mrs. Claus, badly. She has one arm. From somewhere in the dark, a voice, her brother, Sam.

SAM: (Offstage.) Sis? Sis, where you at?

SIS: (Leaping to her feet, waving.) Over here! I'm by the jungle gym! (Sam, twenty, enters. He, too, is missing an arm. He is dressed in Marine camos. He is rushed, freaked out, out of breath.)

SAM: Where's the fire?

SIS: What fire?

SAM: You sounded real bad on the phone. What's wrong?

SIS: (Holding out her bracelet) My bracelet fell off and I can't get it back on.

SAM: Seriously?

SIS: What? I can't get it back on. I need you to do it.

SAM: I'm meeting you in the park at two AM cause your bracelet fell off?

SIS: I feel funny without it. Can you just help me get it back on?

SAM: Fine. (He goes to her. Takes her hand. Helps her put it back on. It may involve teeth. They've done it thousands of times before. It takes a minute)

SIS: Happy Halloween. I like your costume. Camos are cool right now, right? Well that's kind of weird. Kind of ironic, don't you think so? People in the grocery or going to parties dressed like they're ready to shoot somebody. But no, I like it. Looks good. You look like a soldier. (Pause) Who drove you here, huh? I don't like you riding around with people. Mom doesn't like it either. She's probably up worrying about us right now. Well not me. Mom thinks I'm in bed. She thinks I went to Mindy's to watch Dr. Zhivago.. (Sam is finally done with the bracelet. He looks at her.) You haven't said you like my costume yet.

SAM: You're Mrs. Claus every year.

SIS: Mom spent a month making it, I have to wear it at least seven times or she'll be sad. Dad says he likes it when I wear it cause it reminds him Christmas is coming. I don't know, it makes me want to bake pies and knit and hug fat people. So, um, what are you doing? Wanna go home and watch Food Network? Secret Life of Potato Chips?

SAM: I don't live there anymore.

SIS: That doesn't mean you can't visit.

SAM: Sis.

SIS: Sam?

SAM: We're not supposed to be doing this.

SIS: Doing what?

SAM: We're supposed to be apart. We're supposed to be starting our own lives and learning to live by ourselves. As two different people, separate people. That means not together. It hasn't even been that long. (Pause) If we keep meeting up like this because you can't find your hair thing or because you want to know what I want for my birthday, we're never going to get anywhere. You're not even trying. OK?

SIS: Your shoe's untied. Come here.

SAM: No.

SIS: Sammy, let me do it. Don't be stupid.

SAM: Don't call me stupid. (She pats the bench next to her. Reluctantly, he sits next to her. They become one. They tie his shoe. They've done it a thousand times. During:)

SIS: Hey remember, I almost forgot, remember when we were eight or something like that, and we would play in the creek down there? And remember Mom said never go near the still water because that's where the bacteria was. And then remember, ha. Remember, there was that one time, right over there, we figured out the monkey bars, how we could do it together. We practiced forever like the Olympics and we did it, and everyone watched. And no one laughed. And then we got popsicles.

SAM: I remember.

SIS: And then remember, the fireworks by the baseball field, and we chased them. Every year.

SAM: Yeah, we did.

SIS: I forget how to run.

SAM: You just have to learn again. To do it by yourself.

SIS: But I don't have anyone to talk to.

SAM: Hey, you said you had a date tonight. With Tommy, from the photo center. He seems really nice.

SIS: I don't know. . . . I love you.

SAM: I love you too. (She grabs him, embraces him. He responds. It's tender.)

SIS: What'd you have for dinner?

SAM: Wendy's.

SIS: ME TOO. (They smile.)

SIS/SAM: Jr. Bacon Cheeseburger No Mayo Please Biggie Fries Biggie Coke Side Barbeque Sauce.

SIS: So exactly. Why are we apart?

SAM: It's not good for us. It was hard enough to get away from each other. It took forever, it was so hard, and now you wanna put it right back.

SIS: But maybe we were wrong for trying. Maybe we could get back together? The thing is. The thing is. I don't know if I like it. I don't like it anymore, being separated from you. I'm not used to it, and it scares me. A lot. I don't like being alone.

SAM: You just gotta try. You're not trying.

SIS: I was eating strawberries the other day. Big fat ones.

SAM: I don't like strawberries.

SIS: Since when?

SAM: I just realized it last week that I only ate them a lot because you did.

SIS: Don't say that. You love them. Say you love them.

SAM: Just what about them?

SIS: I was eating them, and I found two stuck together, like freak fruit. Two stuck together like us, cause that happens, when stuff is growing, in nature. Things just join together because it's meant to be. And I cried. And I cried more because I was crying. And I couldn't wipe it on your shirt.

SAM: Wipe it on yourself. (The car bonks.)

SIS: Come home with me.

SAM: I don't live there anymore. I go to college. I left. You could, too.

SIS: You go to community college, Sam.

SAM: The teachers are really good! They like me! They think I'm smart!

SIS: They feel sorry for you! (Sam starts to go.) Sam? Sam? I give up. I tried really hard to live not next to you. I told myself over and over how stupid it was to need somebody so bad. I took pictures of us and spit on them. I looked at other people, really looked at them, and tried to see how they were still good, even though they weren't you. I accentuated the positive. Like you said. I didn't call you. Sometimes I don't call you. Even when I want to. I make myself not do it. But I don't feel like it anymore. I give up. Maybe I am insane and maybe I just want to control you and be controlled like you said, or whatever you said, did you say that? But I don't care. I just wanna be back. Sam? OK. You're ignoring me. That's never happened before. This is the first time anyone has ever ignored anybody at all. Don't you miss me? Even a little bit?

SAM: Of course I miss you.

SIS: When the most?

SAM: At night.

SIS: Me too. (Pause) Come home?

SAM: I can't. It's just that, um, I'm kind of leaving. (Pause) See I kind of joined the army. I kind of did that yesterday. (Long, Long pause.)

SIS: But you only have one arm.

SAM: I'm going to do computer stuff in the government. They just need my brain. They think I'm smart. They want my intelligence. They say I'm an army of one!

SIS: But we don't believe in war.

SAM: No, Sis, you don't believe in war! And you never gave me one second to figure out whether or not I do! I want to have preferences and I can't do that with you telling what I like all the time! (Pause) So I'm going.

SIS: I hate you. I wish you were never born.

SAM: What?

SIS: Why are you leaving? Do you hate me? It's cause I'm a freak, isn't it? Well guess what. SO ARE YOU.

SAM: No, it's cause I love you! Sis! I don't wanna be dead! Do you wanna die?

SIS: (Quietly) No.

SAM: If I slept one more night next to you or had to watch you pee one more time or listened to you pop every bone in your hand, I woulda killed you, I swear to God. It woulda been violent. And I love you, but if I have to help you one more time reach the peanut butter or listen to you explain to me what the comics mean, I will murder myself. If I have to listen to you one more time tell someone how much we love strawberries, I will disappear. I want to be somebody. A me. A one thing. By myself. I love you but you eat me. It's better this way. I'm leaving.

SIS: . . . War is evil!

SAM: War is essential.

SIS: You got that outta the newspaper!

SAM: Your costume is stupid! (Long pause. Sis cries.) But it is. Christmas-themed Halloween costumes are just stupid.

SIS: Everywhere I go, everywhere I look, I keep thinking everybody has one arm. I stare at them walking to me and I think, look at that. And then it turns out they have two. It was just the way I was looking at them. Or the way they were walking. But it's always just me. And you. I can't sleep anymore. I haven't been sleeping. Do you care?

SAM: You have to learn to.

SIS: If you go you'll miss my birthday.

SAM: I know I'll miss your **** birthday. It's mine, too.

SIS: I'm going to be twenty-one. I'm going to get drunk and die.

SAM: I gotta go. Go home, OK?

SIS: No.

SAM: Go home. (Sis grabs Sam again. He pushes her off) GO HOME. (Sam looks at her, lingering, then exits, runs off into the black.)

SIS: . . . OK. (Her bracelet falls off. She holds it up, and looks out, sniff) SAM! SAM! My bracelet fell off! My bracelet fell off I FORGET HOW TO DO IT! SAM!

(Sound of car speeding off Sis collapses, center, holding her wrist. She's quite a mess. She holds her bare side nostalgically. Slowly, Sam re-enters, she can't see him, but he looks at her, longingly. Almost says something, but turns again, and leaves.)
```

---

## IC-0713: Attack of the Moral Fuzzies

- Title: Attack of the Moral Fuzzies
- Author (byline): Nancy Beverly
- Work: Ten-Minute Plays from Actor's Theatre of Louisville
- Publisher: Samuel French, Inc.
- Publication date as stated: 1989
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 1, ACTOR 2, SOMBER VOICE 1, SOMBER VOICE 2, SOMBOR VOICE 1, ANNOUNCER, RAMON, BETHANN, DAVE, JOLLEEN, BETH, ELAINE, BENNIE, NADA, CLAIRICE
- Teaser before the introduction: Yes
- Spoken words (computed): 1624
- Already set (do not supply): none

### Source block (context only)

```text
Author: Nancy Beverly
Book: Ten-Minute Plays from Actor's Theatre of Louisville
ISBN: 978-0573625589
Publisher: Samuel French, Inc.
Date (Month/Year): 1989
```

### Introduction (context only: never use it for content warnings)

```text
TOGETHER: Attack of the Moral Fuzzies by Nancy Beverly
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested division of characters:

ACTOR 1: Somber Voice 1, Ramon, Elaine. Bennie, Clarice

ACTOR 2: Somber Voice 2, Announcer, BethAnn, Dave, Jolleen, Nada,

SOMBER VOICE 1: Do you feel lost? Indecisive? Queasy? Are you a stumbler in the dark? Flailing your arms hopelessly, hitting your head against unseen walls?

SOMBER VOICE 2: Are you tossing and turning on the stormy sea of life, miles from a harbor of safety and calm? (pause)

SOMBOR VOICE 1: Relax, Beth. Come with us. No more indecision. No more guilt. Life made simple. Join us as we play the dream of your choice, . . .

SOMBER VOICE 2: MORALITY MADE EASY!!!

ANNOUNCER: And now, here’s your host, Ramon!

(Zippy music, bright lights – blinking lights if available – as RAMON, our sleazy host, sweeps in.. Note: RAMON is not necessarily of Spanish descent; accent is optional.)

RAMON: Good evening, good morning, good grief, good God, great gosh almighty, hot diggity dog, come on in, sit right down, we’re here, you’re there, and our contestant, BethAnn Shumway is on the spot! (BethAnn Shumway enters or lights rise to reveal her. She has put on her nice Sunday outfit to come down here. She smiles nervously. She simultaneously wants to be here and wants not to mess up.) Say Hi, BethAnn!

BETHANN: Are we on?

RAMON: We’re always on, dear, that’s one of the problems. Life just won’t let up, will it? But today we’re going to take away all of that trauma. Won’t that be wonderful?

BETHANN: Yes, it will, Ramon.

RAMON: Now about those rules: millions and zillions of ‘em, entirely to complicated to understand. If we understood the Rules of Life, we wouldn’t have to play the game. Ah, the Game, the Game, she is simple. Five fun-filled rounds, each more pleasant than the last, each hinging on you unhinging that conscience. And after each one, we hook you up to the old Anxiety-o-meter to see how you’re doing. Yes, how fast can you get to Nirvana, or as we like to call it, Okey-Dokey Land. Just to see where we are, let’s take that first preliminary reading.. (escorts BETHANN to a contraption. RAMON does a trumpet fanfare.) Doooo doo doo doo doo doo dooooooooo…a nine and a half! (SFX: taped groans) BethAnn, for heaven’s sake, come away from that thing. What in the world is causing all that trauma? (stage whisper) This is the part where you tell us about yourself.

BETHANN: Oh. Well, I work in a hospital in a cancer ward where I counsel families of dying patients.

RAMON: Well, BethAnn, it’s time to get rolling, time for Round One: (SFX: ding) International Follies. Ready? You’re buying a new car. Do you purchase Japanese because it has a better performance record… (Lights up on a poster of a Japanese car) or American, to support the home auto industry?

(Another car poster. Thinking music. SFX: ding).

BETHANN: Japanese?

RAMON: Okay, let’s see who we’ve got here! (pulls a curtain or lights reveal DAVE). Dave Armstrong!

DAVE: (eager, freshly scrubbed face) Thank you, BethAnn for helping support my dad’s Toyota dealership. Because of people like you, both Japanese and American workers can stay employed – like my dad and me and my brother Dwayne – and also you’ve helped keep free enterprise alive. Thank you very much, BethAnn. (He exits or lights go out on him.)

RAMON: How does it feel to have made the right choice?

BETHANN: I, I . . . feel pretty good.

RAMON: Ladies and gentlemen, she feels pretty good; how good is pretty good? Let’s check that out scientifically with Mr. Meter. A seven and a half, very nice, BethAnn. I think she’s on a roll, so let’s go to the Second Round right now. (SFX: ding) Funding Mania. It’s time to divvy up the tax pie. There’s only enough money for keeping either Basic Grants to college students… (ELAINE appears) or providing Day Care to working, lower-income moms.

(JOLLEEN appears.) Which do you choose? (Thinking music. SFX: ding).

BETHANN: I guess I’d provide the Day Care.

RAMON: Okay, who have we got this time? (Lights brighten on JOLLEEN.) Jolleen Budge!

JOLLEEN: (a little stiff and camera-shy) Thank you, BethAnn, for thinking of us. Because of your thoughtfulness, I am able to keep working at the Tastee-Freeze and still keep Wanda Sue at the Day Care Center where she receives excellent looking-after, and then I still have enough money left over to buy new tires this year. Thank you, BethAnn. ( Applause.)

RAMON: And what’s the ol’ Meter telling us now? Five and a half. She’s heading straight for Okey-Dokey Land. Jolleen’s happy, Dave’s happy, I’m happy, BethAnn’s happy, the guys in the booth are happy, the parking lot attendant’s happy, one big happy family! Round Three – (During RAMON’s digression BETH’s eyes have strayed back to where ELAINE exited.)

BETHANN: Uh, Ramon, could I ask one quick question? . . . I was just wondering . . .does that girl get to go to college, now that she doesn’t have a Basic Grant?

RAMON: I believe you’re straying from our guidelines, dear. No worrying allowed.

BETH: I’m not worrying . . . exactly. I was just curious. Could I just, you know, chat for a second? It’ll only take a second. Where is she, back here?

RAMON: (Sings, under his breath) “Every party has a pooper . . .that’s why we invited her, party pooper. . . ” (BETH enters dragging ELAINE, who is quite confused.)

ELAINE: What’s going on?

RAMON: Oh, not much. Welcome to my nightmare! We’re making it up as we go along – BethAnn Shumway, meet Elaine Henselmeier.

BETHANN: Hi, I was just wondering, do you get to go to college now?

ELAINE: I’ve already been – for a couple of years, in business. But I could only go part-time because I had to work. At that rate, it was taking me eight years, so I quit and got a full-time job as a receptionist in a doctor’s office.

BETHANN: Are you going back someday?

ELAINE: I doubt it. This job’s okay –

BETHANN: – But this isn’t fair –

ELAINE: Yeah, but I’m engaged, and my finance’s got a good job selling aluminum siding

BETHANN: I’ll give you the grant, you can have the grant – Ramon, I really don’t think I’m cut out for this.

RAMON: Beth, you’re thinking too much. The name of the game is Morality Made Easy, not Life’s A Bitch.

RAMON: (BETH takes a deep breath and mouths an “okay.”) Round Three. (SFX: ding.) Hospital Hijinx. At a famous hospital, the writing is on the wall. Funding is being cut back. Out of these three hot ticket items, which one would you support: heart transplants for adults, liver transplants for cute kids under the age of six, or medicare supplements to keep pace with the cost of living.

(Music starts, then slows down as if the electricity has been pulled. BETH quavers, knees buckle.)

BETHANN: I can’t do it Ramon, it’s too close to home. I think I’d better just throw in the towel.

RAMON: QUITTER. (BETH shrinks.) You know what happens to people like you, don’t you? Huh? HUH? (BETH, feeling like five-year-old, shakes her head no.) You become a misshapen, spineless idiot incapable of even the most elementary decisions. (Reveals a hunched-over male, a la the Elephant Man, with normal, albeit whiney, speech and indecisive clothing.) This is a man paralyzed by caring too much. He could once decide which countries should have the bomb, whether we should be backing the Nicaraguan Contras, and even who could or could not have an abortion. Now he can’t even pick out the color of his socks in the morning. . . So you see, you have to choose, it’s a given . . .Recapping Round Three: heart transplants, liver transplants, or medicare supplements. (Fast music, SFX: ding.)

BETHANN: (in one breath) I want the largest chunk for the medicare patients, they’ve paid into the system the longest, and I want the second largest chunk for kids’ liver transplants because it’s not their fault they were born with a bad liver, and I also want money to go for heart transplants because they seem to be having a lot of success with that recently.

RAMON: (pause, eyes her) Covered those bases, huh, kid? (BENNIE KINCAID is revealed, He’s sweaty, greasy, nervous, and desperate. He’s also an auto mechanic.) Meet Bennie Kincaid!

BENNIE: BethAnn, how could you do this? The hospital bills are gonna kill us. Dad had insurance, but when they found out he had Hodgkin’s disease, well, they aren’t so friendly anymore. And he’s only sixty-five, so this could drag on for a long time. I’m tryin’ to run the Shell Station by myself, and when Dad comes home from the hospital, who’s gonna take care of him ‘cause Mom’s gotta work? We just aren’t quite keepin’ up with the cost of livin’, BethAnn. The increase wasn’t enough.

RAMON: Meet Nada Ivanhoe! (NADA is the warm, nurturing type. She too, is angry, but cooler about it. She speaks in modulated tones – with a veneer.)

NADA: Hello, BethAnn. How are you? Have you had a nice day today? Have you enjoyed the bountiful spring weather we’ve been having? I don’t mind telling you we’re having a hard time enjoying it at the Ivanhoe home. In fact, we’re not even at home most of the time. We’re at the hospital with little Justin. The closest we get to spring is looking out of his hospital window. As you may know, Justin is awaiting a liver transplant. If he does not receive a new liver in the next two weeks…(she trails off) Well, we too, like Mr. Kincaid, are a little strapped for cash. The hospital was hoping to provide six free transplants this year. As you may know, funding didn’t quite come through. (pause) But we’re still praying. (pause) I think I hear some chickadees outside. How lovely. (pause) Have a nice day, BethAnn.

RAMON: And finally, Clairice White!

CLAIRICE: BethAnn, unlike Bennie and Nada, I am speaking for myself. I am dying. They just found out I have terminal heart disease. I am only twenty-three years old. I used to raise flowers for the 4-H. I used to be a cheerleader. I used to work as a dental hygienist. No more. Research on heart disease like mine needs to be done (A TV ad:) Only you can help. Give to the heart foundation of your choice. A young heart is a terrible thing to waste. Goodbye, BethAnn.

BETHANN: I quit, I quit, I quit, I quit, I quit, I quit… No, I want to make the right decision – But I keep messing up –

RAMON: So. Beth. What’s up?

BETHANN: I messed up Round Three. I didn’t make the right choice, did I?

RAMON: Are you kidding? You waffled, you fudged, you hedged, you wanted to please everyone. You and Congress. , , , Well, BethAnn Shumway, looks like the game is over.

BETHANN: But, but, but… Prizes, what about prizes? You kept promising prizes!

RAMON: You’re too tense for prizes.

BETHANN: (desperate) Well, how about…consolation prizes, like a car, or a stereo, or –

RAMON: Whoa, whoa, no, no, Beth, sweetheart. There is no consolation here. We were offering peace of mind. We were offering the smug satisfaction that you’d made a good decision without second thoughts. And you turned it down. Prizes? If you’re lucky, you’ll get out of the studio in one piece – that’ll be your prize.

BETHANN: (with grim determination) My favorite color is yellow, my favorite cereal is Raisin Bran, I am buying Japanese this time, and the money goes to Medicare. (Pause - She lashes out at them – and herself.) What did we all want, huh? Warm breezes and iced tea? Easy answers? People should not come on this show – I hope it dies in the ratings. (She storms out quickly.)
```

---

## IC-0714: Babyhood

- Title: Babyhood
- Author (byline): Paul Reiser
- Work: Not specified
- Publisher: Avon Books
- Publication date as stated: Aug 1998
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MOM, DAD, TOGETHER
- Teaser before the introduction: Yes
- Spoken words (computed): 946
- Already set (do not supply): none

### Source block (context only)

```text
Author: Paul Reiser
ISBN: 978-0380728725
Publisher: Avon Books
Date (Month/Year): Aug 1998
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: It’s the best thing in the world . . .

ACTRESS: It’s certainly not easy, and it does change your life forever, but it really is true.

TOGETHER: There is nothing more rewarding or wonderful than having children.

ACTRESS: At least that’s what they tell you . . . .

ACTOR: Babyhood by Paul Reiser
```

### Performance text (classify this)

```text
NOTE: Narration from the book (non-conversational) has been assigned to either “Mom” or “Dad” – There is no speaker designation for narration within the text. Check with the DUO rules in your state before performing.

MOM: (Pg 4-5) What if we want to travel?

DAD: You can travel with kids

MOM: Not to Africa

DAD: Who’s going to Africa?

MOM: I’m just saying hypothetically. What if we wanted to pick up and go to Africa?

DAD: Do you want to go to Africa?

MOM: Not particularly

DAD: So?

MOM: But, someday, I might . . .

DAD: The problem with this type of argument is that on closer inspection, when you list all the things you fear you’d have to give up if you had a kid . . .

MOM: You can’t help but notice it’s actually a pretty pitiful list.

DAD: What else? What specifically are you afraid you’re not going to be able to do with a kid that you do now?

MOM: Okay – sleep?

DAD: Fine. Are we really going to forgo being parents so we can nap?

MOM: Maybe. . . And what about going to the movies?

DAD: You can still go to the movies with kids.

MOM: Yeah, but not whenever I want.

DAD: (Pg 32) You know, it may not definitely be true. These things aren’t always a hundred percent accurate.

MOM: The stick is blue

DAD: Yeah, but not by a lot. All I’m saying is, it’s barely blue. It’s a very light blue. Like ‘sky blue.’ Sort of ‘bad rental tuxedo blue’

MOM: This, pal, is what they call ‘baby blue’

DAD: But I think it’s supposed to be dark blue. Like navy blue. *********

DAD: (Pg 48-49) Why are you crying?

MOM: I don’t know.

DAD: Do you want me to get you anything?

MOM: No, I’m nauseous.

DAD: How many bananas did you have?

MOM: Eight.

DAD: (to audience) Well, there you go. That might be part of the problem. (to Mom) Honey, next time maybe don’t eat so many bananas at one time. . . Is there anything I can do for you?

MOM: Yeah – shut up and leave me alone. **********

MOM: (Pg 95-96) I want you to promise you’ll remarry . . . If anything ever happens to me, I want you to marry someone and get on with your life.

DAD: What are you talking about?

MOM: I’m serious

DAD: You’re going to be fine. Nothing’s going to happen

MOM: It might. You don’t know. What was that movie . . . ? The movie where the mother was giving birth and they helped pull out the baby but the mother died?

DAD: City Slickers? (Mom nods, scared to death) Sweetie, that was a cow.

MOM: Even so . . . she thought everything was going to be fine, too, and then look what happened.

DAD: (Pg 99) (to audience) At this point my wife contorted in pain and then everything became a blur. There was a chunk of time – I couldn’t tell you how long it lasted . .

(following lines are spoken simultaneously and with a rising level of franticness)

MOM: Doctors came in DAD: Nurses scurried about
Machines were wheeled around Mirrors were brought in
Everybody was talking and moving
And coaching and touching
And prodding and sponging
And gloving and crying
And pulling and crowding

MOM: (Let’s out a huge yell as the baby arrives . . . . then all is silent . . . stunned silence)

DAD: (Pg 100) The next thing I remember was the doctor gleefully pronouncing: It’s a boy! Would you like to cut the cord? (Facial expression of apprehension and slight disgust)

MOM: (Pg 103) Sometime later, the three of us – now and forever a family – went home.

DAD: (Pg 109) A new child in the house is a huge tourist attraction.

MOM: It’s like Disney land, except there the lines are longer and no one brings casseroles.

DAD: (PG 111 – 112) Everybody wants to talk to babies, but no one knows what to say.

MOM: "Hello" is very popular. You can't not say it. You pick up a baby, you just start saying "Hello". Over and over.

DAD: "Hello...hello...helllll-ooooo..." Like you're on the phone and the baby's just not picking up.

MOM: Usually what comes next is a question.

DAD: The inevitably high-pitched, dopey-voiced, grown-ups-talking-to-babies voice.

MOM: "Who's the cutest baby?"

DAD: "Who's got an itty-bitty nose?"

MOM: "Who's got a poopy diaper? You? Do you have a poopy diaper and an itty-bitty nose?"

DAD: First of all, these questions are way too easy. The reason babies don't answer is because they're insulted. They don't like being patronized.

MOM: (Pg 113) Or they just lean over the baby and make amusing noises

DAD: Ha-cha-cha—cha . . . Ha-cha-cha-cha . . . Boo-ta-boo-ta . . . Coochie coochie coo (realizes he’s being watched and assumes a more dignified stance)

MOM: (Pg 115) [But] We had no idea how one starts the process of actually being parents.

DAD: (Pg 129) What’s the difference between couplehood and babyhood?

TOGETHER: Moisture (the following lines are spoken simultaneously)

MOM: Your spittle DAD: Your diapers
Your spit-up And drool
You got your baby food Your wipes
Your formula Your leaky bottles
Sweaty baby backs And numerous other untraceable sources

MOM: (Pg 130) Before we go any further, allow me to take a moment to clarify the various categories of moisture . . . There’s spit

DAD: which is the wet stuff that’s in your baby’s mouth

MOM: Spittle

DAD: spit that’s left the mouth and is hanging off your baby’s face in long, suspended, pendulous gobs . . . and drool

MOM: Which is secreted during sleep and collects in large, lukewarm pools.

DAD: And, last but certainly not least. Spit-up (gag reflex) which is hot, lumpy, and frankly too repulsive to discuss any further.

**********

MOM: (Pg 225) In the beginning, whatever sleeping schedule your baby makes up, you accept.

DAD: But after a few months, for the sake of your own sanity, you have to take matters into your own hands.

MOM: (pg 224) [But] when he’s in the next room screaming at four in the morning one of you has to stumble out of your warm bed to deal with it.

(During this section both actor and actress provide crying sound effects while the other speaks)

DAD: It turns out there’s a popular school of thoughts that maintains the best thing you can do for your child is to teach them to soothe themselves to sleep.

MOM: In short – let ‘em cry???? That’s the whole trick???? leave them alone????

DAD: (pg 225) There’s a book [that] says you’re supposed to let them cry for five minutes, then you can pat them a little bit.

MOM: I’m going in . . . he’s crying!

DAD: Don’t – the book said . . .

MOM: I don’t care about the book, he’s crying!

DAD: If we don’t do it, we’re going to be his slaves for the rest of our lives. Do you want that? (crying continues)

MOM: Is it five minutes yet? How long has it been?

DAD: Eleven seconds (panic-stricken looks as scene ends)
```

---

## IC-0715: A Bad Week for Therapy

- Title: A Bad Week for Therapy
- Author (byline): Barbara Lhota and Janet B. Milstein
- Work: Forensics Duo Series Volume 1
- Publisher: Smith and Kraus
- Publication date as stated: Aug 2003
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTRESS, HARRY, MARTHA
- Teaser before the introduction: Yes
- Spoken words (computed): 2067
- Already set (do not supply): none

### Source block (context only)

```text
Author: Barbara Lhota and Janet B. Milstein
Book: Forensics Duo Series Volume 1
ISBN: 978-1575253084
Publisher: Smith and Kraus
Date (Month/Year): Aug 2003
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: Some people are shy, timid, unsure of themselves, or introverted to the extent that they don't speak up when it would be in their best interest to do so

ACTOR: Absolutely! Learning to be assertive is essential for success in all aspects of life, from relationships to careers to personal happiness.

ACTRESS: That’s why Martha scheduled an appointment with Dr. Holden

ACTOR: The therapy session wasn’t quite what she expected . . . .

ACTRESS: It appears Dr. Holden had many of his own issues to deal with. All in all it was

TOGETHER: A Bad Week for Therapy by Barbara Lhota and Janet B. Milstein
```

### Performance text (classify this)

```text
Martha, late twenties, has come to see Harry, thirties, a therapist, because she is having trouble in her work and personal life. Martha is incredibly timid and needs help gaining the self-confidence that will make her a more effective human being. Harry, unfortunately, has had a bad week – his girlfriend and secretary left him, construction on his office building has begun, and his overbearing mother has dropped in unexpectedly. As the scene begins, Harry is trying to fill out standard forms with Martha.

ACTRESS: Or was it??

HARRY: Martha. (Smiles.) Good. Good That’s easy (Writes) Last name?

MARTHA: Anderson.

HARRY: Easy too. (Writing) My handwriting is something else here. I used to have a secretary who did this.

MARTHA: What happened to her? Did you fire her?

HARRY: No, no. She quite Monday out of the blue. With no warning

MARTHA: That’s terrible.

HARRY: Yeah, she left me high and ry. My files were a mess, my life was even . . . ! Anyway, not that I should be telling you this, Martha. Who wants an angry therapist, huh? Not that I’m angry. I’m not angry. Actually very calm and collected, usually, but when your . . . secretary up and leaves, well . . . ! What’s your address?

MARTHA: 4567 Elmwood, Apartment 24B, Waltham, MA 02154. I thought you might have fired her for being too quiet or timid. You see, I’m a little –

HARRY: (Furious) Ten years we were together! (Claps his hands.) Five, four, three, two, one. (He inhales deeply and then exhales. To Martha.) So, how are you doing today?

MARTHA: Fine. I had a little trouble getting a parking space, but I’m fine.

HARRY: Oooh, I’m sorry to hear that. It’s a little tough around here right now. Course them deciding to reconstruct the whole building out of nowhere last week . . . No warning! Not a bit of warning. That made things a little challenging. And then, of course, my overbearing mother decides to drop by from Pittsburgh and I just want to slam her face into the . . . (Exhales sharply) Just a bad week. OK, um, welcome, Martha. I’m so glad you’re here. I just want to say that I like to create in my office a warm and pleasant and safe environment for you so that you can explore --- do you hear that banging?

MARTHA: Um, a little.

HARRY: A little? It sounds like the roof is caving in. (Looking up to the noise)

MARTHA: Now that you mention it, but it’s not bad. I could get used to it. I got used to my neighbor’s child who screamed around the clock. Now, I even like it.

HARRY: (Calling to the ceiling) Shut up!! I’m trying to work down here! (To Martha. Smiles) It feels good to get help, doesn’t it? (Noticing her expression) Oh, gosh. Did I scare you, Martha?

MARTHA: (Covering) No.

HARRY: I’m sorry. I apologize. Things aren’t generally so tense. So, um, do you have insurance?

MARTHA: Yes.

HARRY: OK. Good. (Writes) It was just the abruptness of everything that threw me really. It’s not like I ever intended for us to become . . . Well, (Laughs) I seem to be a bit distracted. I’m, I’m not usually distracted like this. OK, so um, so . . . um . . .

MARTHA: Did you break off your relationship with your secretary, Dr. Holden?

HARRY: Harry, please. Yes. Yes, Martha, we did. Actually, she did. (He nods sadly)

MARTHA: I’m sorry to hear that.

HARRY: Thank you. Thank you, Martha. You just want a little kindness – a little sympathy. (Wallowing in the moment, shaking out of it.) OK. (Claps) Ok now, Um, let’s not focus on me here. My focus is you. This is for you. This session is about you. Uh, let’s talk about you. I’ll just finish this form up and –

MARTHA: OK

HARRY: Do you have insurance? (She nods.) Oh, you already told me that, didn’t you? And, uh, the name of the plan?

MARTHA: Prudent

HARRY: Terrific. (Looking at the form) Oh, gosh. Um . . . this form is quite long. I think that I should have my new secretary . . . (Pausing because he’s getting emotional. She pats his shoulder) when I hire her or him, fill the rest out with you next –

MARTHA: I could do it.

HARRY: Could you? No, no, no –

MARTHA: Sure, I’d like to. I could even straighten up those papers in the front office.

HARRY: Oh. (Chuckles) Did, did you notice that? I just had a little accident with the filing cabinet. It’s not usually on the floor like that.

MARTHA: I understand.

HARRY: Thank you for that. For all of this. So what brings you here today, Martha?

MARTHA: I really don’t mind filling it out myself

HARRY: Well, thank you, but that’s not necessary.

MARTHA: It’s no trouble at all.

HARRY: Oh, no, really, that’s OK.

MARTHA: (She reaches out for the form.) I’ll just take a second.

HARRY: (Frustrated in general) I said no!! (Martha pulls her hand back. Harry laughs) Ha. I’m sorry. I’m sorry, Martha. That wasn’t about you. That was not about you. I’m experiencing a little frustration today, about my own personal, ya know, stuff. Are you OK?

MARTHA: Uh-huh.

HARRY: Well . . . good. OK, so what brings you here?

MARTHA: Well, I

HARRY: Yes.

MARTHA: I, I, uh, have a problem.

HARRY: OK. And .. . ?

MARTHA: I tend to be a little .

HARRY: Yes? Yes. Feel free to expound.

MARTHA: Shy and non – well, you know.

HARRY: No, no, no, I think it’s better if you put it right out there on the table, Martha. Just expose it and let it breathe.

MARTHA: I’m just non, non, just a little non . . . I kind of have a thing about being non, non –

HARRY: (Screaming) Spit it out!

MARTHA: Aggressive! (Beat) Oh.

HARRY: OK. OK, we can work with that. It’s OK, Martha. That’s very good. We’re doing great here. Let’s reel it in now. Both of us. Let’s reel it in. Why don’t we talk about your little nonaggressive issue in a positive way? Sometimes it’s the connotation of the word that gets us. Let’s make it . . (Waves hands) positive. What would be a positive way to say it?

MARTHA: (Shrugs) Um. Uh. Well, well, let me think. Um . . . (Harry is in his own world. He stares into space and sighs.) Assertive?

HARRY: (Harry is still somewhere else. To himself) Why?

MARTHA: (Seeking approval) I suppose because it doesn’t sound quite so mean? (Beat) Is that not good? (Beat) Doctor?

HARRY: Huh? Oh, yes, That’s it! Very good, Martha. Assertive. Very positive. Now, um, tell me how you plan to work on that or something?

MARTHA: Well, I would like to work on being more assertive because my boss said I need to be more confident if I want to move up and be a real sales associate. And I would like to –

HARRY: (Somewhere else.) Uh-huh.

MARTHA: Be more confident in my life so I feel better about myself (Pause) Doctor?

HARRY: (Startled) Yep!

MARTHA: Don’t you think I should talk about my family of origin to gain some insight into why I have such a lack of self-confidence?

HARRY: (Casually) Yeah, that sounds good. I mean, yes, I was just going to suggest that. Go ahead there, Martha.

MARTHA: Well, my parents split up when I was six and I think that really, really had a profound and terrible effect on me and the way that I am.

HARRY: Well, it’s better than an overbearing mother who makes you sing in the boy’s choir when you obviously can’t sing. (Beat) Go on.

MARTHA: My mother had to work three jobs once the divorce went through. We went to live with my grandmother who was very strict and cold. I don’t just mean cold-cold. She was often really cold. She always fell asleep over the covered radiator. I used to bank around in the kitchen to wake her up. She would get all startled and say, “Oh, oh, oh.” And then go back to sleep. She hated children, but she was the one raising me.

HARRY: (Quietly) Whine, whine, whine.

MARTHA: I’m sorry I didn’t mean to –

HARRY: Not you, Martha! Everyone! Every one of my patients goes on and on – whine, whine, whine about their bad childhood. Do you think you’re the only one? We all had bad childhoods. They sucked! I bet Cynthia had a bad childhood too. Well, so did I, Missy. So did I!

MARTHA: Who’s Cynthia?

HARRY: Never mind. I’m sorry. Forget that. Please go on, Martha.

MARTHA: Anyway, um, my grandma was old-fashioned. She would say, “Children should be seen and not heard.” At the dinner table every night, my mother and grandmother would talk about things that happened in their day and I was expected to be silent. I was so sad, but there was no point in speaking or I would be reprimanded by my grandma. Later, my mother would take a special moment to sit down on the couch and talk to me, but she always fell asleep because she was exhausted from all the jobs.

HARRY: (Sniffing to himself) Yes, yes, she left you. Left you. You must accept that.

MARTHA: Well . . . she lives in Dedham. It’s not that far. But I guess you could say figuratively she left me when she fell asleep when I was a child. I guess you’re right, doctor. She left me. She did leave me. Anyway, I started to think that I had a dull voice because sometimes I was answering questions at school and it was like I could hear the other students dropping off to sleep. I’m not kidding. And my teachers seemed like they weren’t listening most of the time because their eyes glazed over when I spoke. Soon, I started to feel there was no point in me talking at all because no one was listening. That’s why I’m here. I’m so glad to finally come to therapy because finally I know that someone is truly listening to me. This is the main reason I think I’m not very assertive maybe, doctor. What do you think? (Harry is out of it) Doctor?

HARRY: Huh? Oh, yes, yes that’s great.

MARTHA: Great? I just told you I had a very sad childhood because no one listened to me.

HARRY: Oh. Yes. Right. Well, the reason that’s, that’s, that’s great . . . is because, we seem to have narrowed down the problem.

MARTHA: We? I don’t think we have done anything. In fact, I don’t think you were listening to me at all! (Gasps) I didn’t mean to yell!

HARRY: Yes, I was. Yes. I. Was.

MARTHA: What did I say then, Dr. Holden?

HARRY: Um, well, (Clears throat) among lots of things, some things about people not listening and . . . in your childhood and . . . that kind of –

MARTHA: Well, aren’t you supposed to be asking me questions as I go along? Making suggestions?

HARRY: (Getting defensive) Well, yes. Of course. That’s my job. I didn’t realize you were so aware of all the steadfast rules and regulations of conducting therapy.

MARTHA: Well, I’m aware enough to know you are supposed to be focusing on me instead of your pathetic, adolescent relationship with your mother-replacing secretary Cynthia!! (Realizing) Oh. I’m sorry. Good God. I’m so sorry.

HARRY: Adolescent? Mother-replacing? (He starts to tear up)

MARTHA: I’m sorry. I’m sorry.

HARRY: (Trying not to cry) I didn’t realize you had so much background in psychology to know so much about my personal dysfunctionality with m y mother and girlfriend. Shall we continue?

MARTHA: Oh, no, no, I don’t think you have dysfunctionality. I don’t think that at all. You’re doing a great job with me.

HARRY: Just because I’ve had a lot of personal pain and agony in the last twenty-four hours, not to mention major reconstruction and the witch dropping in, doesn’t mean I can’t focus on your little problems, on your little . . . thingies. (Starting to cry) It’s just really, really, really, really, hard, ya know?

MARTHA: I know. I know. And I’m so, so sorry. I didn’t mean to – wait a minute. What am I talking about. I’m not sorry. I’m paying you! Not the other way around.

HARRY: Well, maybe I’m doing something experimental? Something different? Something you didn’t learn about in Psych 101? Ever think of that? (Calling up to the upstairs.) Stop banging!! I’m creating an atmosphere that’s calming!

MARTHA: Calming, my tushy! Now you listen to me, Whiney. She left! OK? Cynthia has left. Why? Probably because you never married her and treated her like she was a secretary.

HARRY: Well . . .

MARTHA: I am your patient. I paid for this session while you were out to lunch thinking about every other thing under the sun. You mother, your girlfriend, the building’s construction, your cat, your dog –

HARRY: We never had a dog –

MARTHA: (Closing her hands together) Shhh! (He’s quiet) I will forget all this mess and won’t go to the licensing board on the strict condition that you give me a free, completely-dedicated-to-me session next week! Do you understand?

HARRY: Yes. I understand. No problem. I will. No problem.

MARTHA: (Realizing) Oh my God! (Getting happy) Oh, my God! I was . . . I was . . assertive! Ha ha! You are good! You are so good, doctor!

HARRY: Oh. Yes. Well . . you know, I like to . . . try new things . . . and this is a good day to toss away the old and make room for the (Sniffs) new.

MARTHA: I can’t believe this. I feel so empowered! I’m going to recommend you to everyone I know. (Shaking his hand) Thank you! Thank you so much, Dr. Holden! How can I ever repay you?

HARRY: Well, you did offer to maybe help me clean up the filing cabinet out there a little.

MARTHA: Did I? I’m sure I did (Realizing) Ha! But I’m cured now! (Firmly) Pick it up yourself (Pats his back) Ooh, I just love this (Exiting) Happy cleaning!
```

---

## IC-0716: Bar Mitzvah Boy

- Title: Bar Mitzvah Boy
- Author (byline): Samara Siskind
- Work: Shorter, Faster, Funnier: Comic Plays and Monologues
- Publisher: Knopf Doubleday Publishing
- Publication date as stated: 2011
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: STACIE, SAMUEL
- Teaser before the introduction: Yes
- Spoken words (computed): 1129
- Already set (do not supply): none

### Source block (context only)

```text
Author: Samara Siskind
Book: Shorter, Faster, Funnier: Comic
Plays and Monologues
ISBN: 978-0307743350
Publisher: Knopf Doubleday Publishing
Date (Month/Year): 2011
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: (In a very geeky manner) MY BAR MITZVAH – The huge party when my family announced to the world that I am a Man.

ACTRESS: (A Look, hair flip an eye roll)

ACTOR: I am too a man

ACTRESS: You’re 13!

ACTOR: And a man . . . who girls LOVE! This is how it happened: I make eye contact with the hottest girl in the 7th grade and give my straw a little tongue action so she knows I mean business.

ACTRESS: You drink about four Shirley Temples while creepily staring at the hottest girl in the 7th grade. She is visibly uncomfortable. What’s with that tongue action anyway??

ACTOR: A slow song comes on and I strut over to her, not even asking if she wants to dance. I give her the look, and suddenly the two of us engage in a passionate make out session in the middle of the dance floor.

ACTRESS: She makes certain that someone else asks her to dance before you do. So you get stuck with that one girl who is a foot and a half taller than you. Your sweaty hands hold her awkwardly at an arm's length away. Then, when you lean in for the kiss, she pushes you on the ground . . .

ACTOR: She does not!

ACTRESS: . . . so you start crying. . .

ACTOR: I do not!

ACTRESS: . . . and run out of the building to your waiting mom.

ACTOR: My mom doesn’t wait for me all the time!

ACTRESS: You slam your finger in the car door as you get in and start crying even more.

ACTOR: (rubbing the fingers on his right hand) Well . . . that’s not the way I remember my Bar Mitzvah

TOGETHER: Bar Mitzvah Boy by Samara Siskind
```

### Performance text (classify this)

```text
Darkness. A sappy slow-dance song plays faintly in the background. We hear an angry voice in the darkness followed by a slap.

STACIE: (Pg 15-25) Hey! (Lights rise on SAMUEL and STACIE facing each other on a dance floor. They are both dressed in fancy evening attire. SAMUEL clutches his sore face.)

SAMUEL: Oww! You hit me!

STACIE: Your hand was on my butt.

SAMUEL: My hand was nowhere near your butt!

STACIE: C’mon, Samuel, your hand was totally touching my butt!

SAMUEL: One – I wouldn’t touch your butt with a ten-foot pole. Two – Even if I did touch your butt, it’s no reason to resort to physical violence.

STACIE: Well, if your hand goes anywhere near my butt again, I’m cutting it off.

SAMUEL: Oh, that’s nice. I’m sure they’ll let you off on the popular “he touched my butt” defense. Now can we just finish this dance already, please? Everyone’s watching.

(Beat. STACIE puts SAMUEL’S right arm high up on her waist, and takes his left hand in hers. They dance rather awkwardly)

SAMUEL: My face is stinging. I can’t believe you hit me. It better not leave a mark.

STACIE: I didn’t hit you that hard. Don’t be a wuss.

SAMUEL: Don’t be a ruffian.

STACIE: Uh, ruffian?

SAMUEL: Savage, bully . . . barbarian.

STACIE: Oh, you’re so smart. This is a party, not honors English. (Beat.) God, how long is this song?

SAMUEL: It just started.

STACIE: I’m only dancing with you because my mom made me.

SAMUEL: I’m only dancing with you for the photo op. (SAMUEL smiles, posing for a photographer. Sound of a flash going off)

STACIE: Just because it’s your birthday, doesn’t mean you’re better than everyone else.

SAMUEL: It’s not just my birthday, it’s my Bar Mitzvah.

STACIE: So?

SAMUEL: So?! (Proud) I am a man today.

STACIE: I see no man before me. I see a dork in a beanie.

SAMUEL: It’s not a beanie. It’s a yarmulke. A religious head covering.

STACIE: Yeah, that makes it cooler.

SAMUEL: I’ll have you know, Bar Mitzvah literally translates to “son of commandment” and implies “responsible male.”

STACIE: Big whoop.

SAMUEL: Did you hear me read from the Torah?

STACIE: Yeah, and I’ve got news for you . . . the Torah is a snore-ah.

SAMUEL: You weren’t impressed?

STACIE: I was ready to hit the door-ah.

SAMUEL: Gee, thanks.

STACIE: On a scale of one to ten, I give it a four-ah.

SAMUEL: Okay, you didn’t like it. I get it. (Beat. They continue dancing. STACIE scopes out the dance floor SAMUEL is annoyed.) Why did you even come? If you hate me so much.

STACIE: Hello? We’ve lived next door to each other since we were four, Samuel. My whole family’s here. We’ve had it marked on our calendar since August.

SAMUEL: You could’ve gotten out of it. You get out of everything else your parents want you to do.

STACIE: Well, maybe I didn’t want to get out of it.

SAMUEL: (Perking up) Really? Why?

STACIE: No reason.

SAMUEL: There’s gotta be a reason. Tell me.

STACIE: Ow!! That’s my foot!

SAMUEL: Why’d you want to come, huh? Say it.

STACIE: God, Samuel, what’s the big deal?

SAMUEL: C’mom, Stacie, just give it up. Tell me.

STACIE: Okay, fine! You invited Kyle Fischer and Justin Flint. (Beat. SAMUEL’S spirits plummet once again.)

SAMUEL: I didn’t’ invite them. Mom did. She’s in the PTA with Mrs. Fischer and did Habitat for Humanity or something with Justin’s mom.

STACIE: Do I look like I care? The point is they’re here.

SAMUEL: So, what? You’re dating them both?

STACIE: Samuel! Hello, I’m twelve.

SAMUEL: But you like them both.

STACIE: One of them likes me.

SAMUEL: Which one?

STACIE: I don’t know.

SAMUEL: (Confused) If you don’t know which one likes you, how do you know if either of them like you?

STACIE: Jeez, Samuel, you’re like clueless. (Beat) One of them is my secret admirer.

SAMUEL: Your secret admirer.

STACIE: Valentine’s Day was last week, and I got a dozen pink carnations in my locker.

SAMUEL: And you think one of those dorkwads did it?!

STACIE: When I found the flowers in my locker they were at the lockers across the hall . . . looking at me, smiling.

SAMUEL: Oh, and that’s like, proof.

STACIE: Shut up.

SAMUEL: You shut up.

STACIE: At least I got something. What did you get for Valentine’s Day? Let me guess, a big heart-shaped cookie your mom made you.

SAMUEL: You’re so dumb (Beat) It was a Cupid.

STACIE: They’re looking over here. Oh my God, I’m gonna die. I am so gonna die.

SAMUEL: One – You’re not gonna die. And two – They’re not looking at you, they’re looking at my cousin Sharon. She’s seventeen, and a thirty-four double D.

STACIE: Go ask them which one did it.

SAMUEL: Which one did what?

STACIE: Put the flowers in my locker.

SAMUEL: What?! No! No way!

STACIE: C’mon, Samuel, please?!

SAMUEL: I’m not talking to those Neanderthals. Uh-uh.

STACIE: Why not?

SAMUEL: Because one – I’m not your messenger boy, and two – I am enjoying my dance.

STACIE: One – What is with the one and two everything? God. And two – You’re just jealous.

SAMUEL: Of who? Those guys? Please.

STACIE: YOUR HAND’S ON MY BUTT!!!!

SAMUEL: Sorry, it slipped!

STACIE: (Breaking free) That’s it, Bar Mitzvah boy. Sone of commandment or not, my dad is gonna kick your ass!

SAMUEL: (Holding on to her) Wait! Wait. Stacie, I’m sorry. Look, if you leave me up here by myself, Mom is gonna make me dance with my little sister. It’ll be more embarrassing than that life-size photo of me in the lobby. Please. (A popular, upbeat song begins to play)

STACIE: Fine, but only ‘cause I like this song. (Beat) Don’t touch me. (They dance without touching, more awkwardly than the slow dance). You’re a really bad dancer.

SAMUEL: I’ve taken dance lessons at Arthur Murray since October.

STACIE: You should get your money back.

SAMUEL: They never got to fast tempo.

STACIE: Seriously, you look like Milton Smidel when he had that epileptic seizure during bio.

SAMUEL: Yeh, well, you’re no Fergie either.

STACIE: I’m sure Kyle and Justin would disagree.

SAMUEL: Kyle and Justin are a few brain cells shy of being mentally retarded.

STACIE: Samuel!

SAMUEL: Haven’t you heard the rumors? They like, still eat their boogers.

STACIE: Take it back!

SAMUEL: And they’re in love with each other.

STACIE: They are not!

SAMUEL: Look, they’re dancing together! See? (Waving) Hi, guys! You look super!

STACIE: (Trying to cover his mouth) Samuel, sshhh!

SAMUEL: Like they could even figure out your locker combination, yeah, as if. How would they even know pink carnations are your favorite flower?! (Beat. Stacie stops dancing)

STACIE: How did you know pink carnations were my favorite flower? (A few beats. The song changes to another slow one. Stacie puts Samuel’s hand on her waist. They start to slow dance again.) It was you, wasn’t it? My secret admirer.

SAMUEL: No.

STACIE: Samuel.

SAMUEL: I mean, well . . . yeah. Kind of. (Beat) Kyle and Justin saw me put them in there, hence the staring.

STACIE: Why?

SAMUEL: They thought they were trick flowers that were gonna squirt you in the face.

STACIE: No, I mean . . . why’d you do it?

SAMUEL: I dunno. It’s kind of obvious, don’t you think?

STACIE: But we haven’t . . . I’ve been so . . . (Beat) I haven’t been very nice to you.

SAMUEL: Yeah, true dat.

STACIE: Well then, why? (Beat)

SAMUEL: When we were in third grade, Bobby Proctor wanted to fight me after school because I wouldn’t let him cheat off me. After he threw the first punch you stepped in and kicked him in the balls. He never touched me again after that.

STACIE: I don’t remember that.

SAMUEL: I never forgot it. (A few beats)

STACIE: Well, thank you. I mean, for the flowers.

SAMUEL: You’re welcome. (Beat) Y’know . . . I know I’m not cool, or popular enough for you or anything. But I just wanted to do something nice to pay you back for that day and . . . well, ‘cause you deserve it.

STACIE: (Smiling) Who knew Samuel Rosenbaum could be so sweet?

SAMUEL: (Shrugging) I am a man today. I’ve matured.

(Stacie wraps her arms around Samuel’s neck. They continue to dance even closer together, but both still a bit shy. They sway back and forth to the music. After a few beats)

STACIE: (Soft) Samuel.

SAMUEL: (Dreamlike) Yeah?

STACIE: Your hand’s on my butt again.

SAMUEL: Sorry.
```

---

## IC-0717: Barbara’s Wedding

- Title: Barbara’s Wedding
- Author (byline): Daniel Stern
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: 2004
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MOLLY, JERRY, ACTOR, ACTRESS, TOGETHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1315
- Already set (do not supply): none

### Source block (context only)

```text
Author: Daniel Stern
ISBN: 978-0573630453
Publisher: Samuel French, Inc.
Date (Month/Year): 2004
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: Celebrity-obsessed unemployed actor and former television star Jerry Schiff lives

next door to the most famous woman in the world, Barbra Streisand
```

### Performance text (classify this)

```text
We see Jerry looking out the window with binoculars.

MOLLY: (Pg 10) Oh, Jerry, don’t. Put those away. Tou can’t do that!

JERRY: I’m not bothering anybody.

MOLLY: That’s ridiculous. Just ignore them.

JERRY: They can’t see me . . . Oh my god. . . Henry Kissinger!

MOLLY: What about Henry Kissinger?

JERRY: Henry Kissinger just popped out of a limousine about four feet in front of me. What is he doing at Barbra Streisand’s wedding? I thought she was a Democrat.

(mini-scene in character)

ACTOR: She is getting married, and I was not invited!

ACTRESS: Pathetic! Self-Absorbed! Narcissist! I’ll bet you don’t even remember our wedding!

ACTOR: I was SOMEBODY! Everybody knew who I was!

ACTRESS: On the day of the media-circus wedding, Jerry finds that the beginning of Barbra's marriage may mark the end of his own

TOGETHER: Barbra’s Wedding by Daniel Stern

JERRY: (Pg 13+) Oh, my God! [Molly], come here! Come here come here come here!!

MOLLY: What is it?

JERRY: You have got to look at this!

MOLLY: Jerry, please!

JERRY: Come on! This is important!

MOLLY: Okay! (She comes to the window) What?

JERRY: Is that . . . Gwyneth Paltrow?

MOLLY: Gwyneth Paltrow? Jesus Christ, Jerry! Gwyneth Paltrow!

JERRY: Is that her?!

MOLLY: Okay . . . what about her?

JERRY: Nothing, it’s just. . . why does she get to go to?

MOLLY: Because Jerry, she was invited.

JERRY: I’m just curious that’s all . . . I want to know just how famous do you have to be to be invited? I mean I saw Ed Begley going in.

MOLLY: So?

JERRY: So I mean, come on. Ed Begley? . . . I was Mr. Marvin on “Everything’s Peachy.”

MOLLY: That show ended eight years ago.

JERRY: They show is on every night --

MOLLY: -- at midnight on The Nostalgia Network--

JERRY: --and I’m the fourth one billed. That’s go to be at least as good as Ed Bedley . . . Where is the line of fame that one needs to cross, in order to be invited? That’s all I’m asking.

MOLLY: I seriously doubt Barbra Streisand is a huge fan of the “Everything’s Peachy” re-runs. I mean, come on!

JERRY: Well, what ‘bout what’s-his-name, James Brolin?

MOLLY: He’s the groom.

JERRY: Well, even so . . . (Continues to look out window)

MOLLY: I think working at your fathers plant is going to be good for you . . . you really need to get out of the house more.

JERRY: I’m just doing it for a week while my brother takes his vacation. Five days, that’s it.

MOLLY: Your dad said you can have a job there any time you want.

JERRY: Are you kidding me?

MOLLY: It’s good to have something to do.

JERRY: That would be real good for my mental health. Spend all day, every day with my father and brother, selling and breathing concrete, while they rub it in my face how “I got too big for my britches.” And how they always knew I would end up back there.

MOLLY: All I’m saying is that it might be better than sitting here, waiting for the phone to ring. Jerry completely oblivious of what molly just said continues to look out the window

JERRY: I don’t believe this. How are we supposed to live like this?

MOLLY: It’s just for a day—

JERRY: The one day they stop construction next door and we could have a little piece and quiet is the day we get the helicopters and traffic.

MOLLY: Well, I feel bad for them. I mean they are practically going to have to shout “I promise to have and to hold” at the top of their lungs just to be heard.

JERRY: Well, why don’t they just get married somewhere else like Las Vegas or something . . . like normal people.

MOLLY: She’s not going to get married in Las Vegas. That’s not her style.

JERRY: Her style?

MOLLY: Everybody gets married in a style.

JERRY: We didn’t. We got married in the woods behind my parents’ house.

MOLLY: Exactly. We got married in the “we can’t afford a wedding so we’re just surrounding ourselves with nature and with our loved ones” style.

JERRY: We had no choice it was that or a synagogue.

MOLLY: So, we chose the woods behind your parents’ house and it was absolutely beautiful and perfect. That was our style.

JERRY: That was our style because we had no money and you weren’t Jewish.

MOLLY: Don’t say that.

JERRY: Well, you weren’t.

MOLLY: We were married by a rabbi.

JERRY: He was barely a rabbi anyway.

MOLLY: Barely a rabbi?

JERRY: He didn’t even do it in Hebrew. The whole thing was in English.

MOLLY: I liked that.

JERRY: Why?

MOLLY: Because we don’t speak Hebrew.

JERRY: So?

MOLLY: So he did the ceremony in English so we could understand it.

JERRY: We’re not supposed to understand it. It’s supposed to be in Hebrew just like it has been for thousands of years.

MOLLY: Well, we speak English.

JERRY: That’s not the point.

MOLLY: What’s the point then?

JERRY: The point is the tradition of doing the same for all those years and not making it convenient.

MOLLY: Don’t you think if you’re taking a vow you should understand what you’re vowing?

JERRY: It’s not about taking a vow.

MOLLY: It’s not?

JERRY: No.

MOLLY: How can you say that?

JERRY: Because it’s not. It’s about the ceremony. It’s about doing it in front of other people, not about what we specifically vowed to do. We just repeated whatever he said.

MOLLY: Did you mean the vows you made to me at our wedding?

JERRY: I think I did, but I don’t know. There was a lot going on.

MOLLY: You weren’t paying attention at our wedding?

JERRY: There was a lot going on! I mean, I had just come from an audition.

MOLLY: . . . You came from an audition?

JERRY: Yeah… you knew about it.

MOLLY: You went to an audition, on our wedding day?

JERRY: Yes. I told you about that. It was like three hours before the wedding.

MOLLY: Oh my god.

JERRY: It was a real good scene too, where I’m yelling at the older brother, “I’m real! I’m as real as a two-dollar bill!” which is really great line for the character, because a two dollar bill is real but it’s rare—

MOLLY: You can remember the lines from a movie that you weren’t even in . . . but you can’t remember your wedding vows? The promises for a life together that we made to each other at our wedding!

JERRY: It was a crazy and confusing day and all I’m saying is that if the rabbi would’ve said, “Do you promise to drink your milk and eat your vegetables” you would have said, “I do” to that also.

MOLLY: No, I wouldn’t have.

JERRY: Of course, you would.

MOLLY: I’m lactose intolerant, Jerry! I’m not going to vow to drink milk!

JERRY: You can’t remember what you vowed.

MOLLY: I vowed to love you until I die! I vowed to stay with you until I die . . . I vowed to make you happy . . . to make a home together! And I promised that even though we are not bound by blood, that you are my family. Forever. No matter what!

JERRY: Okay . . . but you didn’t mean it.

MOLLY: What?!

JERRY: You didn’t mean it.

MOLLY: Yes, I did, Jerry! And to refresh your memory you promised the exact same things. We said the exact same words that day. I meant what I said, Jerry. Did you? (Long pause) You know...I’m not even sure we are legally married.

JERRY: That’s ridiculous.

MOLLY: I mean we made a verbal contract at the wedding but if you were in an altered state of mind, I don’t know if in the eyes of the courts, not to mention the eyes of God, that our contract is valid.

JERRY: Of course, we’re married.

MOLLY: You know what? Fine. Maybe I’ll go over to my sisters for awhile.

JERRY: Don’t you dare.

MOLLY: Why not? It might be good. A little break.

JERRY: Don’t you dare leave with all those reporters out there.

MOLLY: OH MY GOD!

JERRY: You will not embarrass me in front of the national press.

MOLLY: Is that what you care about? Not that your wife IS LEAVING YOU, but that people might see?

JERRY: So what?!

MOLLY: Oh my god! That’s it! It’s official. You are pathetic!

JERRY: I’m pathetic? I’m pathetic! What does that make you?!

MOLLY: It makes me sick! I can’t stand being around you anymore! The world does not focus on you!

JERRY: No the world is focused on BARBRA FRICKING STREISAND!
```

---

## IC-0718: Barefoot in the Park

- Title: Barefoot in the Park
- Author (byline): Neil Simon
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: Nov 1986
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 1, ACTOR 2, PAUL, CORIE
- Teaser before the introduction: No
- Spoken words (computed): 1433
- Already set (do not supply): none

### Source block (context only)

```text
Author: Neil Simon
ISBN: 978-0452258709
Publisher: Samuel French, Inc.
Date (Month/Year): Nov 1986
```

### Introduction (context only: never use it for content warnings)

```text
(no introduction)
```

### Performance text (classify this)

```text
ACTOR 1: Newlyweds Paul and Corie Bratter, back from a blissful honeymoon, are having their first fight.

ACTOR 2: The couple lives in a six-floor walk-up in New York City. Corie thinks the place is wonderful and happily looks forward to decorating her first apartment, despite its bad plumbing, leaky skylight and bad paint job.

ACTOR 1: Serious-minded Paul is involved with preparing for his first court case.

ACTOR 2: In this scene Corie’s mother Ethel and the couple’s neighbor Victor have been out to dinner with Cori and Paul.

ACTOR 1: The two hit it off and Ethel leaves with Victor.

ACTOR 2: Now Corie and Paul are worried that because Ethel and Victor were drinking, they may do something they’ll regret!

ACTOR 1: Like walking . . . . Barefoot in the Park by Neil Simon

{Both getting ready for bed after a night out. Corie, getting in her PJs, in the bedroom; and Paul, in his dress shirt and pants, brushing his teeth/gargling}

PAUL: I just can’t understand how you can be so unconcerned about all this. I really can’t.

CORIE: Unconcerned?

PAUL: I really…

CORIE: Do you think I’ll get one wink of sleep until that phone rings tomorrow? I’m scared to death for my mother. And I’m grateful there’s finally something to be scared about. What I’m really concerned about is you.

PAUL: (Walking out of the bathroom, speaking with Corie face to face) Me? Me?

CORIE: Yeah. I’m beginning to wonder if you’re capable of having a good time!

PAUL: Why? Because I like to wear my gloves in winter?

CORIE: No. Because there isn’t the least bit of adventure in you. You know what you are, Paul? You’re a watcher. You’re a watcher. There watchers in this world, and there are doers. And the watchers sit around watching the doers do. Well, tonight you watched and I did.

PAUL: It was a little bit harder to watch what you did than it was for you to do what I was watching.

CORIE: You can’t even relax for one evening. I don’t know, Paul, sometimes you act like a--

PAUL: What? Hmm? A stuffed shirt? Is that it?

CORIE: I didn’t say that.

PAUL: That’s what you were implying.

CORIE: That’s what you’re anticipating. I didn’t say stuffed shirt.

PAUL: Mm-hmm.

CORIE: But you’re extremely proper and dignified.

PAUL: Proper and dignified? When was I proper and dignified?

CORIE: The other night at Delfino’s, you were drunk, right?

PAUL: Right. I was stoned.

CORIE: Exactly. I didn’t even know it until you told me in the morning. Uhh… I mean, you’re a funny kind of drunk, Paul. You just sat around looking unhappy, watching your coat.

PAUL: I was watching my coat because I saw someone else watching my coat. If you want, I’ll get drunk for you some time, make your hair stand on end.

CORIE: [brushing her teeth in the bathroom] It isn’t necessary.

PAUL: You know in Harry’s Bar last New Year’s Eve, I punched an old woman. Don’t tell me about drunk. When else? When else was I proper and dignified?

CORIE: All the time. You’re always dressed right. You always look right. You always say the right thing. You’re very nearly perfect.

PAUL: That’s a rotten thing to say.

CORIE: Before we were married, I thought you slept with a tie.

PAUL: No. Just for very formal sleeps.

CORIE: You have absolutely no sense of ridiculous. Like last Thursday night, you wouldn’t walk barefoot with me in Washington Square Park. Why not?

PAUL: Simple answer. It was 17 degrees. [undoing the cuffs of his shirt]

CORIE: [walking into the living room] Exactly. It’s very logical, very sensible, and it’s no fun.

PAUL: [following Corie, continuing to unbutton his shirt] Maybe you’re right. Maybe I am a little too proper and dignified for you. Maybe you would have been happier with somebody a little more colorful and flamboyant… like the geek [Victor].

CORIE: It’d be a lot more laughs than a stuffed shirt.

PAUL: I thought you said I wasn’t.

CORIE: Well, you are now.

PAUL: I’m not gonna listen to this. I’m not gonna listen to this. I have a case in court in the morning. [heading for the bedroom]

CORIE: Where are you going?

PAUL: To sleep.

CORIE: Now? How can you go to sleep now?

PAUL: I’m going to close my eyes and count knichis (a Japanese eel dish). Good night dear.

CORIE: You cannot go to sleep now, Paul. We’re having a fight.

PAUL: You have the fight. When you’re through, would you turn off these lights. Please.

CORIE: That gets me absolutely insane! You can even control your emotions!

PAUL: [coming back] No, no. I’m just as upset as you are. But when I get hungry, I eat. When I get tired, I sleep. You eat and sleep too, don’t deny it, I’ve seen you.

CORIE: Not in the middle of a crisis.

PAUL: What crisis? We’re just yelling.

CORIE: You don’t consider this a crisis! Our whole marriage is hanging in the balance.

PAUL: It is? When did this happen?

CORIE: Just now. It has suddenly become very clear to me that you and I have absolutely nothing in common.

PAUL: Because I won’t go walking barefoot in the park? You don’t have a case, Corie. Adultery, yes, but cold feet, no.

CORIE: Don’t you over simplify this. I am angry, Paul. Can’t you see that?

PAUL: It’s 2:15. If I can get to sleep in a half an hour, I can get about 5 hours sleep. I’ll call you from court tomorrow, and we’ll fight over the phone. [trying once again to go to bed]

CORIE: You will not go to sleep, Paul! You will stay here and fight to save our marriage!

PAUL: If our marriage hinges on those fishbowls and pelmechk (A Russian dish), it is not worth saving. Now dear, I’m crawling into our tiny little single bed, if you care to join me. We are sleeping from left to right tonight.

CORIE: You won’t discuss it! You’re afraid to discuss it! I married a—a coward!

PAUL: [popping his head out of the bedroom] Would you bring in a pail? The closet’s dripping.

CORIE: Oh, I hate you! I really, really hate you!

PAUL: Listen! [coming out again] Now wait a minute, Corie. There’s one thing I’ve learned in court. Be careful when you’re tired and angry. You may say something you will soon regret. I am now tired and angry.

CORIE: And a coward!

PAUL: [following Corie around the living room] Maybe you’re right. Maybe we don’t have anything in common. Two people should have more than just a blood test first. Maybe they should be checked first for a little common sense, understanding, and emotional maturity!

CORIE: All right! Why don’t you get it passed by the Supreme Court? Only those couples bearing a certificate from their psychiatrist proving that they’re emotionally mature can be married.

PAUL: Oh, listen—[trying to hold her]

CORIE: Don’t touch me! Don’t lay a finger on me! I can’t stand to have you near me! I don’t want to be in the same room with you!

PAUL: What’s going on here? You’re hysterical.

CORIE: I am not hysterical! I know exactly what I’m saying, Paul. It’s all over between us. And it’s never going to be any good anymore.

PAUL: Oh God…--

CORIE: I’m sorry. I don’t want to cry.

PAUL: Cry, please. Go ahead.

CORIE: Don’t you tell me when to cry! [roaming around cleaning up the apartment] I’ll cry when I feel like crying. And I’m not going to have my cry until you’re out of this apartment.

PAUL: What do you mean “out of this apartment”?

CORIE: Well, you certainly don’t think we’re going to live here anymore, do you? After this?

PAUL: Are you serious?

CORIE: Of course I’m serious, Paul! I want a divorce!

PAUL: Divorce!

CORIE: I’m sorry. I can’t discuss it anymore.

PAUL: Where are you going?

CORIE: To bed. [walking into the bedroom and getting under the covers]

PAUL: You can’t, not now.

CORIE: You did before.

PAUL: In the middle of a fight. This is in the middle of a divorce.

CORIE: I’m sorry, Paul. I can’t talk you when you’re hysterical.

PAUL: I want to know why you want a divorce. [Corie, jumping out of bed, going back into the living room, Paul following her] Huh? Why?

CORIE: Because you and I have absolutely nothing in common.

PAUL: Nothing in common? What about the six days at the Plaza, Corie?

CORIE: Six days does not a week make.

PAUL: What does that mean?

CORIE: I don’t know! I don’t know what it means. All I know is that I want a divorce. (They’re both now seated on the sofa.)

PAUL: You know, I think you mean it. You mean this?

CORIE: I do. I really do.

PAUL: Let’s just… think.

CORIE: [hiding her face sobbing]

PAUL: I thought you weren’t going to cry.

CORIE: Well, I am! I’m gonna cry, I’m going to have the biggest cry I’ve ever had in my whole life, and I’m going to enjoy it! And I’m gonna cry so hard, I’ll keep you awake all night. Good night, Paul. I mean goodbye. [storming off into the bedroom]
```

---

## IC-0719: Beauty and the Beast

- Title: Beauty and the Beast
- Author (byline): AJ Jacobs
- Work: Fractured Fairy Tales, Pgs 103-110
- Publisher: Bantam Books
- Publication date as stated: Jan 1999
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 1, ACTOR 2, NARRATOR 1, TOGETHER, NARRATOR 2, OLD MAN, DAUGHTER, PRINCE
- Teaser before the introduction: Yes
- Spoken words (computed): 1287
- Already set (do not supply): none

### Source block (context only)

```text
Author: AJ Jacobs
Book: Fractured Fairy Tales, Pgs 103-110
ISBN: 978-0553373738
Publisher: Bantam Books
Date (Month/Year): Jan 1999
```

### Introduction (context only: never use it for content warnings)

```text
(no introduction)
```

### Performance text (classify this)

```text
Suggested Roles:

ACTOR 1: Narrator 1, Daughter

ACTOR 2: Narrator 2, Old Man, Prince

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

NARRATOR 1: (Pg 103-110) Once upon a time there was a magnificent golden castle on a silver cloud high up in the sky, which has nothing to do with anything because our story is about an old woodchopper who lived in a shack, but that's a good way to start a fairy tale.

ACTOR 1: Long before Politically Correct Bedtime Stories arrived in bookstores, Americans were getting their giggles from Fractured Fairy Tales,

ACTOR 2: Those delightfully twisted parables brought to us between the cliffhanger adventures of our favorite cartoon heroes, Rocky & Bullwinkle. ACTOR 1 as ROCKY: *And now...

ACTOR 2 as BULLWINKLE: Hey Rocky! Watch me pull a rabbit out of my hat!

ACTOR 1 as ROCKY: But that trick never works!

ACTOR 2 as BULLWINKLE: This time for sure! Presto! (something goes terribly wrong—be creative) Well, I'm getting close.

ACTOR 1 as ROCKY: And now it's time for another special feature!

ACTOR 2: A nostalgic retro adventure re-imagined by AJ Jacobs in his collection of Fractured Fairy Tales.

TOGETHER: Beauty and the Beast

NARRATOR 2: The old man was very happy, but he had a daughter who was very unhappy because . . . well, she was rather plain.

NARRATOR 1: Actually, she was really plain. In fact, she had a face like five miles of bad road. Anyway, it was time for her to marry, but because she was so fat and ugly, none of the young men of the kingdom ever came to ask for her hand, or any other part of her body, for that matter. Then one day, the old man decided to cheer her up.

OLD MAN: Child, it is your birthday and I've brought you something to keep you from being so lonely.

DAUGHTER: (wide-eyed) A man?

OLD MAN: Nope. A mule.

NARRATOR 2: He pointed to a brown, furry, four-legged, grunting beast. Well, a mule wasn't exactly the kind of companion she had in mind, but at least it was somebody to talk to.

DAUGHTER: Hi there, silly beast, I wonder if you were once a handsome prince changed into a mule by a wicked witch. If so, I could break the spell with a kiss. (kisses mule)

NARRATOR 2: She smacked the mule right on its lips. It was no use. The mule was a mule and had always been a mule. The next day the old man instructed his daughter to take a bundle of sticks to the village.

DAUGHTER: A bundle of sticks? What for?

OLD MAN: How should I know. But somebody is always carrying a bundle of sticks around in fairy tales. You know that.

NARRATOR 1: So, the young girl took the bundle of sticks and decided to ride her trusty mule into the village. But something very strange happened. Unknown to her, the moment she climbed onto the mule's back *POOF* she turned into a beautiful maiden.

NARRATOR 2: You know the type: blond hair, blue eyes, a figure like she spends her days doing Jazzercise.

NARRATOR 1: Anyway, when she reached the village, (NARRATOR 2: whistles and catcalls) she could hardly believe her eyes, for all the young men, instead of laughing and throwing mud at her, bowed, tipped their hats, and made catcalls. She was still trying to figure it out when a handsome young prince rode up to her on a snow-white horse.

PRINCE: Ah, fair ladyl You are truly the most lovely beauty in the land.

DAUGHTER: (batting her eyes) Why, my young prince, are you nuts or sumpthin'?

PRINCE: With your permission, I should like to call upon you tonight. How about when the clock strikes the hour of eightish?

NARRATOR 1: Flushed with excitement, the girl raced home; but when she arrived and stepped off her mule, *POOF* she immediately returned to her fat little ugly self. That night, promptly at eightish o'clock, the prince, sitting astride his white charger, knocked on the door.

PRINCE: (prepares himself and knocks regally)

DAUGHTER: (opens door and smiles)

NARRATOR 2: A crooked-toothed smile -- one that made chopped yak liver seem appealing –

DAUGHTER: Hellooooo!

PRINCE: (with a hard to conceal facial reaction) Um . . .

NARRATOR 1: Said the prince, who at that moment was desiring a bit of Pepto-Bismol, or the medieval equivalent.

PRINCE: Is your sister at home?

DAUGHTER: I don't have a sister.

PRINCE: Your aunt then.

DAUGHTER: I don't have an aunt.

PRINCE: (growing more frantic) Your cousin? Your best friend? Your babysitter?

DAUGHTER: What are you talking about? I live here alone with my father.

PRINCE: (makes a break for it)

NARRATOR 1: Figuring he had found the wrong house, the prince galloped quickly off on his white steed.

NARRATOR 2: The poor girl was left standing at the door, brokenhearted and trying to understand what had gone wrong.

NARRATOR 1: The following day, her father again asked her to go into the village. This time to pick up a bundle of sticks.

OLD MAN: (patting her kindly on her head) It'll take your mind off your ugliness.

NARRATOR 1: No sooner had the girl climbed on the mule's back than *POOF* once again she changed into a beautiful maiden.

NARRATOR 2: On the way to the village, she chanced to pass a clear, still pool of water. Looking into it, she saw her reflection and was shocked to see she was now very beautiful.

NARRATOR 1: She jumped off her mule for a close look and *POOF* instantly she changed back into her former ugly self.

NARRATOR 2: And then, she suddenly realized what had happened.

DAUGHTER: I get it now!

NARRATOR 2: She said out loud to no one in particular, as people in fairy tales sometimes do.

DAUGHTER: This is a magic mule. As long as I sit on this beast, I'm a beauty!

NARRATOR 2: The girl jumped back onto the mule, and *POOF* beautiful again.

NARRATOR 1: And the beauty and the beast dashed to find the prince. When he saw her coming, he rode up to her on his gallant steed.

PRINCE: Ah, lovely beauty, I have found you again. Please say you will be mine so that we may be married.

DAUGHTER: Yes, but on one condition: That I remain on my mule at all times.

NARRATOR 2: Of course, this seemed like a strange request, but the prince agreed.

PRINCE: So be it, my love. And so that we start off on the right foot -- or on the right hoof -- I shall stay on my horse as long as you stay on your mule.

NARRATOR 1: And thus they were married by a priest, who delivered the sermon on a donkey.

NARRATOR 2: As the years went by, the young girl was very happy, although the poor mule did get a bit of a backache.

NARRATOR 1: And true to his word, the prince also stayed on his horse. And as any good husband would, he took her dancing every Saturday night at the palace, where they were the most striking couple on the dance floor.

NARRATOR 2: Or actually, the most striking quadruple on the dance floor.

NARRATOR 1: One day, as the girl rode in the garden *WOOSH* the wind blew off her bonnet.

NARRATOR 2: Not stopping to think, she hopped off her mule to get the hat and *POOF* she immediately turned into an ugly, disgusting hag again.

DAUGHTER: (adjusting her hat, she transfroms from beauty to hag)

NARRATOR 2: Realizing her mistake, she scrambled to get back in the saddle again. But it was too late, for just then the prince rode up.

PRINCE: Pardon me, old hag. Have you seen my wife? Wait a minute, this is her mule!

DAUGHTER: (blushing and gulping) Yes. And I am your wife.

NARRATOR 1: She began to sadly confess the whole story to her husband, but instead of being angry . . .

PRINCE: (laughing and clapping for joy) Ha, ha, ha, ha. Yahoo! Yippee!

DAUGHTER: I don't get it. Are you happy to find out that I'm really ugly?

PRINCE: No! I'm happy to know that I can finally get off this blasted horse. You see, I'm only a handsome prince when I stay on him.

NARRATOR 1: And with that, the prince hopped off his horse and *POOF* he changed into one of the ugliest men ever to walk the earth.

NARRATOR 2: He was fat and short and bald and full of warts. His face looked like ten miles of bad road.

DAUGHTER: (gleefully) Ugh! You're uglier than me!

PRINCE: (they hug) We were meant for each other! Just think-no more saddle sores!

NARRATOR 1: And so, the ugly man and the ugly girl were able to live

TOGETHER: Happily ever after.
```

---

## IC-0720: Because I Wanted to Say

- Title: Because I Wanted to Say
- Author (byline): Sean O’Donnell
- Work: Off-Off-Broadway Festival Plays: 22nd Series
- Publisher: Samuel French, Inc.
- Publication date as stated: July 2017
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ANN, STEVEN, TOGETHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1074
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sean O’Donnell
Book: Off-Off-Broadway Festival Plays: 22nd Series
ISBN: 978-0573602498
Publisher: Samuel French, Inc.
Date (Month/Year): July 2017
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR: We hear people talking about "closure" as if there is a door that can be shut after experiencing the death of a loved one

ACTRESS: But really . . . . Why would anyone seek closure? Why would anyone want to close the door on thoughts of that special person?

ACTOR: It’s true that grief will soften in the years after a loss, but the door to memories should always be open

ACTRESS: And the opportunity to say the things that need to be said

ACTOR: Should never be locked in a casket, or an urn.

TOGETHER: Because I Wanted to Say by Sean O’Donnell
```

### Performance text (classify this)

```text
ANN: We were dancing at my wedding (pantomime dancing outrageously) and he said:

STEVEN: (Off-stage) “We’ll always have Poughkeepsie.”

ANN: (She peruses a photo album and stops at a particular photo.)The photographer caught us laughing in a cloud of white wedding dress and Grey Flannel, I told my husband, that picture, for me, totally summed up my relationship with Steven.

STEVEN: (Entering stage left. Stands behind ANN’s chair) I loved it, because it showed you laughing – really laughing. Not that other thing you do when you’re being flirtatious or insecure.

ANN: When I’m playing my “Home movies in my mind,” it’s that image of Steven that always draws me in. There are other more colorful clips, but that’s the one I love. Steven, so handsome in blue linen and a red polka dot tie. Dancing me from one part of my life to another, as he’d done so many times before. (She slowly opens the urn.)

STEVEN: (Crosses center, and holds his hand out to ANN) I always said “When you know where you’re going . . . “

ANN: (Seeing STEVEN, she rises and takes his hand. He twirls her into a dance pose with ANN facing the audience) “You know what to wear.” (She laughs) It was strange how it hit me. The things I missed first about Steven were not what I would have thought.

STEVEN: For instance?

ANN: For instance, that funny laugh we used to do. Our secret calling card. (She demonstrates. STEVEN joins in) Without Steven providing the harmony, it was . . . I don’t know . . .

(They break the pose)

STEVEN: One hand clapping. And . . .

ANN: The million funny things he said to make me laugh. And I can’t recall one of them right now. His strange way of looking at things. These things are already fading, and that’s what scares me. Scare me more . . .

STEVEN: Than all the scary stuff that came before.

ANN: Because if I can’t remember, what is left is an old Godiva box filled with some letters. No stories, no secrets, nothing to tell.

STEVEN: I wanted to tell you. I started to tell you so many times. But . . .

ANN: I think I finally knew before he told me. The shock, the rage I felt was incredible. I wanted to kill him. And I wanted to kill however did this to him.

STEVEN: (Dryly. Out) It was too late for that.

ANN: It was no longer about causes and contributions Ribbons and ranting. The enemy had made a successful attack into my life.

STEVEN: Of course, I wasn’t the first.

ANN: Not the first, but to me, the most important.

STEVEN: Telling you was one of the most terrifying and important moments of my life.

ANN: Steven, how could you let this happen? How could you do something so stupid?

STEVEN: (Out) It was the wrong thing to say.

ANN: Of course, that’s not what I meant. But when faced with that particular piece of news, your first reaction is not likely to be “How inconvenient.”

STEVEN: The funny part is, and I don’t mean to trivialize, but it was inconvenient.

ANN: I’ll never forget his face when he told me. One part “Dark Victory,” two parts Blance DuBois (She smiles) I wanted to smack him.

STEVEN: Perhaps I was a trifle melodramatic. I mean it was a difficult moment. And a difficult moment is always easier when you’re Bette Davis.

ANN: I never thought I couldn’t go on without him. But I couldn’t imagine certain parts of my life without Steven. It hurt my heart to think Steven wouldn’t be there to help my daughter grow. That she’d be denied his humor, his whimsicality, his love.

STEVEN: I’m telling you I was afraid that we would try to stuff every moment after full of caring and sharing. Try to make every meeting so special, so precious, we’d never forget it.

ANN: We started to have strange conversations. What about her prom dress?

STEVEN: For God’s sake, she’s two years old.

ANN: I know, but . . .

STEVEN: Tell her to remember the shoes have to match the bag.

ANN: Catholic school?

STEVEN: (Stares at her for a beat) Don’t be ridiculous.

ANN: Boys?

STEVEN: (Interested) Boys? (He takes her hand.)

ANN: You know, the good from the bad. The naughty from the nice.

STEVEN: Usually, the naughty are the nice.

ANN: Steven!

STEVEN: Just make sure none of them have “Judy: The Decca Years” in their lunch box. You’ll be fine.

ANN: That’s not what I meant.

STEVEN: I know what you meant. You’ll be fine.

ANN: I don’t want to be fine.

STEVEN: You’ll be . . .

ANN: Without you. Without your . . .

STEVEN: (Sings two lines from an up tempo old standard) You’ll be fine. (perhaps Harpy Parson’s “You’ll Be Fine”: see https://www.youtube.com/watch?v=jMuycuDgeDQ for song) (They sit for a moment) Do you remember how you always used to plan your funeral?

ANN: Steven! (Gets up and crosses to the chair stage left)

STEVEN: Tell me about it again.

ANN: Don’t be macabre.

STEVEN: Come on now. . . there were five little blond girls.

ANN: Brunette . . . and there were six . . . all in white. . . dresses, shoes, they carried nosegays of violets with long, trailing, pink ribbons.

STEVEN: And the coffin?

ANN: Glass. Made entirely of glass.

STEVEN: I loved that part. It’s sooo Snow White.

ANN: And they played Italian opera throughout the service. And at the end, my mother heaves herself onto my casket and says “Take me too, God, take me too!”

STEVEN: No wonder I love you. You’re such a drama queen.

ANN: (Beat) I have something to tell you.

STEVEN: Another shocking confession?

ANN: I was thinking about us, you and me.

STEVEN: Uh huh?

ANN: And I realized even though I married someone else, it’s like all these years I’ve had a secret, second marriage to you.

STEVEN: (Beat) Does your husband know about this?

ANN: No.

STEVEN: Good. Go on.

ANN: It’s just that even though we never . . . I don’t think we could be closer.

STEVEN: (Dramatically posing) “And should I die this instant, I had lived Her time to a minute.“

ANN: The Duchess of Malfi, Act 4 (STEVEN drops dramatic pose) You see, a light . . . a light turned off in the middle and you can’t help but wonder where was it going, what was ahead? All those choices that never had a chance.

STEVEN: Sort of like a mini-series with no end.

ANN: An unfinished melody, a broken blossom, a . . .

STEVEN: Honey, get ahold of yourself.

ANN: Some things were said; and some were left unsaid. But no matter how you try and prepare yourself, you’re never fully prepared.

STEVEN: Maybe not saying it was our way of saying it. Or perhaps, we felt in some greater cosmic scheme of things we just didn’t have to.

ANN: I supposed we thought we’d be ready to say it when . . .

STEVEN: Or if we never said it, the moment would never come.

ANN: Good-bye.

STEVEN: Good-bye.

ANN: Unfinished business, no, I don’t think that’s it. I think I tried to conjure Steven because I wanted to say . . .

STEVEN: Thank you. . . because I wanted to say . .

ANN: (Breaking down) I’m not fine without you!

STEVEN: Because I wanted to say. . .

ANN: There were moments . . .

STEVEN: There were moments . . .

ANN: When I felt like we were two halves

TOGETHER: of the same person . . .

ANN: Because I wanted to say . . .

STEVEN: There wasn’t a secret I never tell you . . .

ANN: There wasn’t anything I wouldn’t have done . . .

STEVEN: Well

ANN: Well . . . . I still talk to you when I’m lonely

STEVEN: Because I wanted to say . . .

ANN: Even when I think I’m forgetting.

STEVEN: I remember it all.

ANN: Because I wanted to say . . . .

TOGETHER: I miss you.

(The words hang between them. STEVEN stands behind her for a long moment. He leans over and presses his cheek to hers. ANN closes her yes. STEVEN slowly exits.)
```
