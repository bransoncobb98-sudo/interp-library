# Classification request: batch 4 of 53 (40 records, IC-0521 to IC-0560)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-004-reply.json`.

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

## IC-0521: After You

- Title: After You
- Author (byline): Matt Mills
- Work: After You
- Publisher: Mushroom Cloud Press
- Publication date as stated: August 1, 2023
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1681
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
“After You” by Matt Mills

LISA PAXTON, 41, a suave, sharp, self-aggrandizing lawyer, stands holding something upright in her right hand.

Lisa: Rachel. Thank you so much for agreeing to meet me at this time.

Across from her nods RACHEL TOMPKINS, 37, a spunky, endearing, but acrimonious lawyer standing as tall as she can (Lisa’s taller, but only in the physical sense).

Rachel: Of course. Should we get started?

Lisa: Absolutely. I motion to record these proceedings for discovery. (Pulls out her phone)

Rachel: Motion approved. (Pulls out her phone) Motion to double-record these proceedings for optimal post-production mixing and mastering.

Lisa: Motion firmly approved. Alright. (Clicks her phone, puts it in her pocket) It is Wednesday, June 28th, 2022 at… (Peeks at her phone) Eleven oh seven a.m. I, Lisa Paxton, am willingly engaging in this settlement discussion with intentions to resolve the dispute without trial.

Rachel: I, Rachel Tompkins, am also willingly engaging in this settlement discussion with intentions to resolve the dispute without trial. Alright. How do you plead?

Lisa: After you, your honor. And how do you plead?

Rachel: After you, your eminence!

Lisa: Agh. You’re really dragging us to trial instead of just walking through the door I’m holding open for you? Come on! Just go in!

Rachel: Reminder we’re on the record, counselor.

Lisa: Ugh, correct. Thank you counselor. Mind if I take opening remarks?

Rachel: You clearly do a remarkable job opening things, so yes. Please do.

Lisa: And you’re great at giving compliments. Okay. (to an invisible jury) Let me begin my case–

Rachel: To whom are you presenting your opening argument?

Lisa: Oh. Force of habit. Mind if I keep pretending there’s a jury, though?

Rachel: Motion approved. Motion for me to do the same?

Lisa: Motion approved.

Throughout the proceedings they oscillate from arguing at each other and at imaginary jurors.

Lisa: I will begin by presenting the facts–

Rachel: As you see them.

Lisa: Objection.

Rachel: That’s not how this conversation works and you know it!

Lisa: Sustained. As I see it, the dispute in question arose thusly: On the morning of June 28th, 2022, at approximately… Eleven oh six a.m., I, Lisa Paxton, was approaching this door – the southeastern door of the central conference room on the fourth floor of the Branchwood Hills Office Park in San Contesto, California. As my hand clasped the handle – which, the record should reflect, I am still holding – I observed Rachel Tompkins, a beloved colleague–

Rachel: Objection. You don’t love me.

Lisa: Double-objection! I thought we agreed we weren’t doing objections.

Rachel: Sustained. But get to the point, counselor.

Lisa: As I grabbed the door handle, I observed Rachel Tompkins, a colleague whom I like (Rachel nods approval), approaching, at which time I offered to hold the door open for Miss Tompkins – an offer which she adamantly and illogically refused and continues to do so!

Rachel: Let the record show that prior to Miss Paxton’s hand establishing firm control of the handle and completing the full motion of the clasp, I was more than ten yards away from the play and made a clear, beyond a reasonable doubt gesture encouraging Miss Paxton to go ahead, as holding the door for me was unnecessary and wasted precious seconds of her life.

Lisa: That is patently untrue. There is incredible personal benefit – such an act improves my mental health by providing emotional support to a caring, talented person whom I respect.

Rachel: Regardless, upon my approach I clearly indicated that the right of way was hers with sufficient time for Miss Paxton to change course.

Lisa: Regardless of said communication, my action did not proceed immediately and Miss Tompkins gained proximity to the door in such a rapid fashion that closing of the door would have undoubtedly been deemed a rude gesture.

Rachel: I disagree. The generosity had already been displayed, so there was no need for further sacrifice on the part of Miss Paxton.

Lisa: Let the record show that Miss Tompkins bought me lunch last month and the incident in question was simply one of many small ways in which I am trying to pay her back.

Rachel: Let the record show that Miss Paxton has been an inspiration for a large portion of my career, placing deference on her passage through the door over mine.

Lisa: Motion to not say “Let the record show” anymore because this is being double-recorded and we don’t need to.

Rachel: Motion approved. Also, motion to stop making motions.

Lisa: Final motion approved. The truth is, Rachel Tompkins established ownership of this door’s passage the day she took me to that new tapas place that I cherish so dearly now.

Rachel: The true pleasure was mine, due to Lisa Paxton’s incredible company, making her the rightful first-entrant.

Lisa: Rachel Tompkins donates to more than ten charities, volunteers on the weekends, and has never said an unfair word in my presence, so she should go through the door first.

Rachel: Lisa Paxton deserves to go through the door first because she nursed an ill stray cat back to health and continues to give it a healthy home to this day! Not to mention–

Lisa: Whoa, hey now–

Rachel: May I finish my argument?!

Lisa: (She settles down) Proceed.

Rachel: (She sends some demonstrative looks/reactions) As I was saying… Lisa sealed ownership as the rightful first entrant of the door when she won the AAJ Partnership Award for her sustained commitments to civil justice!

Lisa: How dare you bring that up. Seriously? Ugh. Come on. That is such a low blow.

Rachel: Hey. Don’t dish it if you can’t take it.

Lisa: Oh yeah? Well you… I once saw you give a homeless man forty dollars! And he wasn’t even asking for money, you just really wanted to make sure he could eat well for a day or whatever – you supported whatever he wanted to do with that money!

Rachel: Alright, if that’s how we’re gonna play this – just sling old mud at each other…

Lisa: I guarantee I’m dirtier than you.

Rachel: I know you pulled a lot of strings to get that poor girl a scholarship to Columbia!

Lisa: You mentored me even when our firms opposed each other!

Rachel: You protected me from that creepy guy in the bowling alley!

Lisa: You hold the door for people all the time!

Rachel: YOU BRING ENERGY INTO EVERY ROOM YOU WALK INTO!

Lisa: YOU ARE A VERITABLE LIGHT OF A HUMAN BEING!

Rachel: YOUR EXISTENCE RAISES MY FAITH IN HUMANITY!

Lisa: EARTH DOESN’T DESERVE YOU!

Rachel: YOU’RE OUT OF ORDER!

Lisa: YOU’RE OUT OF ORDER!

Rachel: AHHH!!!

Lisa: AHHH!!!

Rachel: –HHH WAIT! Wait. Someone’s coming.

Both counselors collect themselves, wiping suits and manufacturing professional posture. They each give polite smiles as some GUY approaches. Lisa curtseys a gesture for him to go in.

Lisa: After you!

Rachel: (gesturing him in, still holding the door open) I insist.

Surrounded by their smiles, he walks in without controversy. Their focuses return to each other.

Rachel: Perhaps we’re getting a bit bogged down in the details. Allow me to provide some background to my case.

Lisa: The floor is yours, counselor. As is the door.

Rachel: Nice try. Picture if you will… a little girl born in a small town called Elk Horn. Her working parents are home for maybe an hour a night, maybe, if she’s lucky. With no resources provided to her, she clawed her way up the educational ladder, shattering the glass ceiling while becoming one of the youngest attorneys in her firm’s history. Now tell me – who could possibly deserve to enter a door first more than this little girl turned hero – from a place called Elk Horn!?

Lisa: I’m glad you ask, counselor. I’ll see your little girl and introduce her to one from Anchorage, Alaska. Resilient to freezing temperatures as well as discrimination, she scraped her way into a stunning major lawsuit victory at age 29. When she was only 33, her mother developed a devastating disease that almost took her life – perhaps it would have if not for her daughter, this little girl from Anchorage, dropping everything to do everything for her mother. She has overcome obstacle after obstacle, a lifetime of kicking butt culminating in deserving the ultimate reward: a politely-held door.

Rachel: Your evidence is flimsy and you know it. Exhibit A…CL: You tore your ACL playing rugby in college! I should hold the door for you!

Lisa: Exhibit B: My ACL healed properly. Exhibit C: You work incredibly long hours!

Rachel: Exhibit D: You’re a treasure I could never live without!

Lisa: A world without you is nothing but a shadow!

Rachel: NO ONE COULD POSSIBLY DESERVE WALKING THROUGH THIS DOOR MORE–

Lisa: YOU’RE AN INSPIRATION!

Rachel: YOU ARE!

Lisa: YOU DESERVE IT!

Rachel: YOU DO!

Lisa: AFTER YOU!

Rachel: AFTER YOU!

Lisa: NO, AFTER YOU!

Rachel: NO, AFTER YOU!

Lisa: I INSIST!

Rachel: I INSIST!

Lisa: I INSIST!!

Rachel: I INSIST!!

Lisa: I INSIST!!! Rachel: I INSIST!!!!!!

The GUY from earlier returns; it’s JEREMY STINTON, 53, a mediator.

Jeremy: Would you PLEASE… either come in or shut the door? (Lisa and Rachel wince-smile) We started the deposition five minutes ago and the recorder is picking up your entire argument.

Lisa: We’ll be right in.

Rachel: Sorry. (Jeremy turns to head back in) Wait. Jeremy! (Jeremy turns back) You heard our case, right?

Jeremy: Correct. Unfortunately.

Rachel: So?

Jeremy: What?

Lisa: Who won?

Rachel: You know she deserves to go first–

Lisa: There is nobody that I would rather–

Jeremy: Stop, stop. Wow that’s annoying. Fine. Rachel. (Rachel brightens) You lose.

Rachel: Awww come on! You know I should go first!

Jeremy: But… but that’s what I just decided.

Rachel: Huh?

Lisa: Yeah what?

Jeremy: You were arguing that Lisa should enter the doorway first. I figure that since Lisa, regardless of tardiness of control of the handle, did establish control and, as the holder of the door, bore the burden of entering second, as the right of way defers to the person in the same vicinity who possesses superior freedom of movement at that time. Thus, you win, Rachel.

Rachel: Yes. Right. Sorry, I just forgot what we were arguing about for a minute.

Lisa: Yeah, same. In fact… I think I’m feeling a bit lightheaded…

Rachel: Well, hey – let me get that door for you!
```

---

## IC-0522: Anxiety Versus You

- Title: Anxiety Versus You
- Author (byline): Shawn LaSota
- Work: Anxiety Versus You
- Publisher: Mushroom Cloud Press
- Publication date as stated: September 1, 2022
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: SPEAKER, ANXIETY
- Teaser before the introduction: No
- Spoken words (computed): 1658
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
A duo play

By Shawn LaSota

Shawn LaSota
524 N. Wood St.
Erie, KS 66733
shawnlasota@gmail.com
(620)249-9587

©2022 SHAWN LASOTA ANXIETY VERSUS YOU

Characters:

SPEAKER: The calm, cool, and collected cast member who is narrating the emotions and feelings of those that deal with anxiety.

ANXIETY: The spastic and bombarding presence. Erratic and fidgety, jumping across the stage behind the speaker while shouting. Is a rollercoaster of emotion throughout.

Synopsis:

Presented are 5 easy-to-follow coping mechanisms that are sure to help in the constant battle with the ever-annoying Anxiety.

ANXIETY VERSUS YOU

ANXIETY VERSUS YOU

Scene 1

(SPEAKER stands CS serenely and addresses the audience directly. He/She is pleasant, with a relaxed demeanor.)

SPEAKER: Anxiety. A condition that plagues young people all across America. An ever-growing epidemic that has stunted our social and professional growth.

(ANXIETY enters stage right at a hurried pace.)

ANXIETY: Damn straight.

SPEAKER: Now that we live in an ever-growing environment of social media comparisons, more options than we can imagine, and constant self-doubt, we are inundated with anxiety.

ANXIETY: I’m like glitter after a toddler’s birthday, man. I’m everywhere!

SPEAKER: And of course, we can recognize the symptoms of anxiety. Feeling restless, wound-up, or on edge.

ANXIETY: (moves stage left) You got to move, son! You need to be getting your butt in gear, ya hear?

SPEAKER: Having difficulty concentrating or your mind going blank.

ANXIETY: ANXIETY VERSUS YOU

Two plus two equals...chair! I know I heard words out of her mouth...she said...Oh look, a squirrel! What was I saying?

SPEAKER: Having feelings of worry and difficulty controlling emotions.

ANXIETY: Nobody likes you. Everyone hates you. They think you smell. They think you smell like hot tuna in a baby’s diaper! (Begins to cry) Why can’t I just be like...everyone...else! (Now angry) Who the hell do those mo-fos think they are!

SPEAKER: And of course, difficulty sleeping at night...which can exacerbate all of the symptoms already mentioned.

ANXIETY: (moves stage right) Did I study enough for that test? What if I forget? What if I go blank? What if I fall asleep during the test? What if I wake up naked during the test? What if my crush laughs at me? What if I...Damn! Why can’t I sleep!

SPEAKER: You get the idea. So here’s the bad news...you can’t cure anxiety.

ANXIETY: Damn! I’m like herpes.

SPEAKER: Correct. But just like genital herpes, you can learn to live with and cope with your anxiety, which is what I’m here for today. These are 5 things you can do in order to cope with your annoying anxiety.

ANXIETY: Well, get after it, Dr. Phil!

SPEAKER: The first tip is pretty simple. Breathe.

ANXIETY VERSUS YOU

ANXIETY:
Like this?
(ANXIETY quickly inhales and exhales at a
rapid pace, loud and panicky)

SPEAKER: No, not like that. Breathing like that will actually make your body feel worse, which will in turn worsen your anxiety.

ANXIETY: Ah, hell!

SPEAKER: What you need to do instead is change up your breathing. The most common method is the 4-7-8 method. You inhale for four seconds. Then hold your breath for seven seconds. And finally, you exhale for 8 seconds.

ANXIETY: Do I Mississippi?

SPEAKER: No, because that could kill you. Or at least cause you more stress. There is a reason that when your plane is crashing the oxygen masks fall from the ceiling. Breathing is a natural way for your body to regulate itself. So by changing your breathing to slow and steady breaths, you’re also relaxing in the process. Therefore, reducing anxiety. This can help at the moment that you’re feeling anxiety and also at night when you’re trying to relax to sleep.

(ANXIETY’S face is turning red. SPEAKER notices)

SPEAKER: What are you doing?

ANXIETY: (Gasps for air) I Mississippied.

SPEAKER: ANXIETY VERSUS YOU

Anyways. The next thing you can do is meditate.

ANXIETY: Like saying a bunch of ‘ohms’ and what not?

SPEAKER: I mean, not really. Meditation is simply taking a moment to focus on your breathing and block out the noise from the rest of the world. (closes eyes)

ANXIETY: (right in SPEAKER’s ear) Hey. Hey. Hey. Listen. Listen. I gotta ask you something. Hey. Hey. Look at that dog right there. Look at that guy in the front row. He’s laughing like you’re an idiot. I know you’re listening. Stop ignoring me. I’m talking to you. Oh, I see how it is. I see how it is.

SPEAKER: (opens eyes) Meditation gives you the opportunity to think about your thought process and address what is stressing you out. It’s also important to be able to stop and think about your emotions before you give into them and do something you will regret.

ANXIETY: Like murder?

SPEAKER: Yeah, like that. Meditation is also beneficial against heart disease, depression, and high blood pressure.

ANXIETY: But you look like a damn fool!

SPEAKER: Is that the worst thing that can happen? Which is a perfect segue into my next tip.

ANXIETY: Damn! I hate being helpful.

SPEAKER: ANXIETY VERSUS YOU

This is going to seem counterintuitive, but I promise it’ll help. Take whatever it is that you’re stressed about and imagine the worst possible scenario happening. It’s called Negative Visualization. Imagine everything going wrong. What’s the worst that could happen?

ANXIETY: (pacing behind SPEAKER) The apocalypse! Nuclear war! Genocide! Barack and Michelle Obama splitting up!

SPEAKER: Relax. Unless you’re God, a world leader, or one of the Obamas, chances are none of that is going to happen. So in order to cope with your anxiety of possible failure, you have to imagine failing and be okay with it. I’ll repeat that. It’s okay to fail. Your life will not be over. The world will keep spinning. The sun will come out tomorrow. And the Obamas will outshine every other married couple on the planet.

ANXIETY: But I’ll be a failure!

SPEAKER: You say that like it’s a bad thing. Thomas Edison made a thousand unsuccessful attempts before inventing the lightbulb.

ANXIETY: He doesn’t sound too bright...get it?

SPEAKER: 12 publishers rejected J.K. Rowling’s first Harry Potter manuscript.

ANXIETY: Maybe they didn’t see the magic.

SPEAKER: Even Michael Jordan said, “I've missed more than 9,000 shots in my career. I've lost almost 300 games. Twenty-six times I've been trusted to take the game-winning shot and missed. I've ANXIETY VERSUS YOU

failed over and over and over again in my life. And that is why I succeed.”

ANXIETY: I mean, he’s no Lebron…

SPEAKER: You shut your mouth.

ANXIETY: But what if I’m just worried about what other people are going to think of me?

SPEAKER: Dude, nobody else cares. That’s tip number four by the way. Nobody cares. You’re the one who is responsible for your emotions and you’re the only one having your emotions. No one else is paying attention to you more than you’re paying attention to yourself. So when you’re feeling stressed and anxious, remind yourself that nobody cares. No one is watching you. No one is keeping tabs on if you succeed or fail. You’re the one holding yourself to such a high standard.

ANXIETY: What about my mom?

SPEAKER: Well, unless you’re a doctor, nothing is going to please her.

ANXIETY: What about my grandma?

SPEAKER: Please, you could’ve assassinated Lincoln and your grandma would still bake you cookies and send you five dollars on your birthday. The final and probably the most important tip is...well...talk to someone.

ANXIETY: Like a shrink?

ANXIETY VERSUS YOU

SPEAKER: I mean, not necessarily. Just talk to, you know, a person. A friend. An acquaintance.

ANXIETY: What about a stranger?

SPEAKER: Let’s not cause anyone else anxiety. Look, whenever we’re an island unto ourselves, our thoughts become exaggerated and built up in our heads. Whether it’s the fear of failure or even doing something embarrassing in front of people, we can escalate it in our minds and increase our anxiety, turning little things into huge problems. For instance, let’s say that Janet didn’t smile at you in the hallway or something.

ANXIETY: Janet didn’t smile at me in the hallway? It must mean she doesn’t like me. Why doesn’t she like me? Do other people not like me? Is there a reason they don’t like me? Is there some flaw about me that is causing them not to like me? Oh God, how long has this been going on? Do they know something I don’t? Am I going to get kicked out of school? Get fired? Will no one be my friend? Will no one be my boyfriend/girlfriend? Am I going to be alone forever? Am I going to have thirty-six cats and knit them sweaters because I have nothing else in my life?

SPEAKER: Chill, man. Janet doesn’t smile at anyone.

ANXIETY: Oh...yeah.

SPEAKER: See? By just talking to someone and sharing your thoughts, you’re able to gain a different perspective or understanding. You’ll realize that you’re not alone because Janet is stuck-up and doesn’t smile at anyone. If you embarrass yourself, talk about it with someone else. Chances are they will have experienced the same thing and guess what, they’re just fine.

ANXIETY VERSUS YOU

And you will be too. Suddenly the thing that you were panicking about is now something to laugh at with someone else.

ANXIETY: (laughing) Aw, man, you’re so right. Janet is totally full of herself.

SPEAKER: Says the guy/girl who thought his/her failure was going to cause the Obamas to break up.

ANXIETY: Hey! (begins moving upstage)

SPEAKER: Look, there’s no cure for anxiety, but that doesn’t mean it needs to control your life. In fact, anxiety is a necessary part of life. It’s a natural feeling that our bodies developed in order to warn us of approaching dangers. It’s not a bad thing. No feeling is good or bad. It all depends on how we react to them. By training yourself to cope with your anxiety, it will help you in the future by training your body to deal with stress before it even becomes a problem. Just like our muscles have a thing called muscle memory, our brains kind of have the same thing with our feelings. So no, our anxiety will never be gone, but we can work on reducing its effect and making its voice a little harder to hear.

ANXIETY: (From upstage, voice fainter) Hey, can you hear me? I’m talking here! I’m still back here!

SPEAKER: And it can stay back there. When it comes to a battle between anxiety and you, by learning how to cope, you always win.

END SCENE
```

---

## IC-0523: Assignment: Apple

- Title: Assignment: Apple
- Author (byline): Mike Noland
- Work: Assignment: Apple
- Publisher: Mushroom Cloud Press
- Publication date as stated: December 1, 2024
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1964
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
Scene INT: Alex’s bedroom

This scene takes place in a bedroom. Any bedroom will do. The characters can be male, female or non-binary because…they are just people. Well, not people exactly but high school students. It’s the bedroom of a high school student and their friend arrives to come up with ideas for an assignment they have in their English class. From here, I think you can figure it out. Good luck, oh… and have fun!

Alex (Alex is looking at his/her notebook in the bedroom.) What kind of assignment is this anyway? An apple, really. We have to do something, anything creative with an apple? (Phone goes off, looks to see who it is, then answers.) Where are you? We are supposed to be working on this stupid project together. At the Police station? What did you do?

Taylor
(Taylor walks into the room on the phone.)
(Still on the phone at first) I was picking out flower arrangements. (Puts down phone and
laughs) You really thought I was at the police station? (Laughs some more.)

Alex Well with you, you never know. Plus I’m really stressed about this stupid assignment. I just don’t understand what he’s wanting. (Reading from the notebook again. Uses a fake teacher voice.)” You may do anything creative to describe an apple. Write a poem, a short story, a haiku, whatever creative outlet you want to use. The key is to describe the apple in a way that is not ordinary.” It’s an APPLE!

Taylor Relax, you are letting this get to you. This is a chance to do something fun and exciting.

Alex Yeah, like getting a D or an F.

Taylor (Laughing) You are looking at this all wrong. We can do whatever we want. Don’t you get it? As long as we try and at least describe an apple in a different way, we are golden, Golden Delicious. Get it…golden delicious is a type of apple. The sky’s the limit here. He has just given us a license to ill.

Alex What? License to ill?

Taylor I just mean, there are no limits. We have total freedom. I find that exhilarating.

Alex I find that nauseating. I like guidelines that I can see. Guidelines that I can follow, that make sense. Not this weird, free-association, nonsense. I need structure. Not this loosey-goosey, livin-in-a-commune-with-old hippies stuff. We’ll just write a poem!

Taylor NO. That’s what half the class will end up doing. (Looks around the room for a second. Finds a pencil and walks over to Alex.) Here just take this pencil and stab me in the eye with it because I would rather you do that then write a poem.

Alex Fine, what’s your idea?

Taylor Here me out. I've been thinking about this all day. Let’s make a film.

Alex A film? You mean like a movie?

Taylor You say movie, I say film but it’s the same thing. Just think about it. Everyone else in class is gonna write some crappy poem or ridiculous short story. Then they will have to get up and read it to the class. We will all have to sit and listen to this dribble till our ears are bleeding. But if we make a film…

Alex Movie…

Taylor Whatever, the class will go nuts. We will be like a pizza to a starving man.

Alex Why pizza?

Taylor Cause it’s more fun and that’s what we will be…FUN.

Alex Alright, suppose I agree to this. What sort of movie…

Taylor Film..

Alex …are we talking about? We can’t just say “Here’s an apple. It comes in many colors and flavors.”

Taylor No, we can make it like a spy story or an adventure film and the fruit can talk. Whatever we want. And as the story goes on, we find unique ways to describe the apple. It doesn’t have to be long, just interesting. I’ll bet he has never had any students do anything like this before. He’ll love it.

Alex But what if he doesn’t?

Taylor Even if he doesn’t he will still give us credit for trying as long as we describe the apple, that’s the key. Why not have some fun with this?

Alex (Thinking before speaking.) Hmmm. I have a few questions.

Taylor Shoot.

Alex

Have you ever written a script before?

Taylor Nope, next question.

Alex

Have you ever shot a movie before?

Taylor Film and no. Next.

Alex What makes you think we can do this?

Taylor I don’t know. We may go down in flames. This may be the single biggest mistake of our young lives. But why not give it a try. How hard can it be? I’ve seen some really terrible movies and somebody got paid to write those…so?

Alex That’s true. But how are we gonna shoot this?

Taylor Are you kidding? (Holds up the phone.) We have all we need right here. We can shoot it, edit it, add music and even special effects if we want. Everything we need is right here.

Alex Except one thing.

Taylor The script. So the first thing we need to do is decide what the story will be about. But is there something that has to come first?

Alex Like what?

Taylor Well I don’t know about you, but I’m starving. I haven’t eaten since breakfast.

Alex You didn’t eat lunch.

Taylor Well, typically, in most cultures, lunch follows breakfast. And if you had breakfast and you have not eaten since that time. Most would assume, and correctly I might add, that you skipped lunch. So no, I did not eat lunch.

Alex Wow, that was a long walk off a short pier. You didn’t have to be quite so snarly.

Taylor Perhaps I have the hangries. You know angry cause I’m hungry

Alex I know what the hangries are. I may have a granola bar in my backpack.

Taylor Great or I could just chew on a belt. It would have about as much flavor.

Alex For someone that’s starving you are certainly picky.

Taylor Maybe I’ll just go into your kitchen and see what’s in the fridge or the pantry. (Starts to walk out.)

Alex No, if you go to the kitchen, we won’t get started for like an hour.

Taylor What?!! Your kitchen is across the hall, not the country.

Alex But I know you. You will start out for the kitchen and then you’ll see my mom and start talking to her. Then you guys will start laughing and it won’t stop.

Taylor I love your Mom. She’s the best and so funny.

Alex I know, I agree but right now we need to work.

Taylor Okay, I promise I won’t talk to your Mom. I will run into the kitchen and grab the first thing I see and run back. It will take me 10 seconds. You can time me.

Alex I don’t want to time you. This is not an olympic event.

Taylor Oh, but that would be a cool one if they had it. (Taylor closes his/her eyes and starts pantomiming, opening things and grabbing things.)

Alex What are you doing?

Taylor I’m practicing. That way when I'm there I won’t waste time. (Pantomiming with eyes open this time.) There’s the fridge and I’m opening the door. Give it a quick glance. How old is that spaghetti?

Alex There’s no spaghetti in there.

Taylor Well, there could have been. I was kind of hoping there was. It sounded good. (Pantomimes again.) Checking in the pantry. (Looks up and down.) Are those Oreos still good?

Alex How did you know there were Oreos in there?

Taylor Everyone has Oreos. But that’s not what I’m hungry for. Maybe just some chips. You got any Hawaiian Punch?

Alex Always. Will you just hurry up, we gotta get started.

Taylor Are you gonna time me?

Alex Really?

Taylor Yes and say the numbers out loud. That will motivate me. Are you ready?

Alex Yes…

(Taylor can run to the side of the stage and pantomime all the action or run up stage with back to the audience and stand still. These are just suggestions, they’re good but you can do whatever you want. After all, you’re the ones performing.)

1…2…3…4…5…6…7…8…9

(Taylor runs back in.)

Taylor (Pantomimes carrying chips and a juicebox.You’ll see why in a minute.) Made it with a second to spare. Whew, I’m good. I even waved at your Mom.

Alex (Sarcastically) Oh, that’s nice.

Taylor Is she doing something different with her hair? It looks nice.

Alex I don’t know and I don’t care.

Taylor Well that’s not a very nice attitude for the woman that raised you. Not to mention the nine months she lugged you around in her belly. That couldn’t have been much of a picnic.

Alex Would it be possible to start working soon? Believe it or not, this isn’t the only homework I have to do, ya know.

Taylor Sounds like someone else might have the hangries. Want some chips?

Alex Is that a juicebox?

Taylor Uh huh! (Take a sip.) And it’s good too.

Alex Was that the last one?

Taylor Uhhh… maybe?

Alex And it's a fruit punch, isn’t it?

Taylor

Yes and it’s deee-licious.

Alex That’s just great! Can we get started now??

Taylor I’m ready to go, let’s do this.

Alex So, what’s your idea for the screenplay?

Taylor Let’s see…(thinks) yep, I got nothing.

Alex Nothing, what do you mean nothing? This was your idea.

Taylor My idea was to write a screenplay and make a film. I don’t have a clue what it will be about.

Alex Maybe the first thing we could do is get the names of different types of apples.

Taylor For someone who hasn’t written a screenplay before, you are quite good at this.

Alex Thanks, let’s start naming different types of apples. There’s Honeycrisp, Gala, Granny Smith..

Taylor Oh, I bet we could do some funny stuff with a Granny Smith. Maybe she’s the crotchety old lady that lives next door. She’s always yelling at the little kid apples. “Stop playing in the street. You wanna car to hit you and turn you into apple sauce? Then we would see your pale yellow insides splattered all over the road.”

Alex I see where you are going with this but it might be a little graphic, don’t ya think?

Taylor Trust me, the guys will love it and it gets a little of the description of the inside of the apple. Which unless I’m mistaken, is part of the assignment.

Alex Well, that’s true. We’ll just put a pin in the idea for a minute. Let’s keep coming up with some more names.

Taylor There’s McIntosh, Red Delicious and Fuji, which is one of my favs.

Alex And Ambrosia, Evercrisp and Pink Lady.

Taylor Pink Lady! Hey that’s it. We could do, like a whole musical thing using songs from Grease. You know cause the Pink Lady’s are the cool chicks in Grease.

Alex Musical, are you crazy? Listen, we are stretching it to write a screenplay. I’m not gonna try and add music too.

Taylor We don’t have to write the music. That’s already been done. All we have to do is rewrite the lyrics to the songs that they already have.

Alex Well, I’m not singing, are you singing?

Taylor Actually, I’m more of a writer-director. Ok, so maybe not a musical but what about if we got a whole bunch of fruit and made it look like a party. All the fruit are hanging out and talking like you do at a party. Then a banana comes up to an apple and says, “Hey Red, you sure look sweet. A bunch of us over there were wondering how you keep yourself so shiny.” Get it? Bunch…bananas? We could do fruit puns and jokes.

Alex Well…I don’t hate it but I don’t think we have any fruit. So you know what that means, right?

(They both look at each other and smile and then answer at the same time.)

Alex Taylor Grocery store run Road trip

Alex Wait, What did you say?

Taylor I thought you were gonna say, a road trip. Just cause, ya know, that would be fun.

Alex Well, I guess we could take a road trip to the grocery store. We’re gonna need a lot of fruit.

Taylor Hahaha yeah!!

Alex Let’s get going, we gotta get this done. You got any money?

Taylor Uh, no. You?

Alex

No…(thinking.) But I know where to get some. Come on and follow my lead.
(Starting to leave the room)
Mom, we gotta run to the store. ( As they exit. This could be done to the side or upstage with
backs to the audience.) Hey, what did you do to your hair, it looks amazing!!

,
```

---

## IC-0524: Beauty and the Beast: Human Resources

- Title: Beauty and the Beast: Human Resources
- Author (byline): Kevin Burgun
- Work: Beauty and the Beast: Human Resources
- Publisher: Mushroom Cloud Press
- Publication date as stated: September 1, 2022
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, PRINCE, SERVANT 1, WITCH, PLATE, BROOM, CUP, BUCKET, FOOTSTOOL, KNIFE, COAT RACK, PAN, GIRL
- Teaser before the introduction: No
- Spoken words (computed): 3041
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
(AUTHOR’S NOTE: Knowledge of the movie or fairy tale should not be necessary for the
audience or performer. However, the piece was written in an open way that a performer or
performers who wish to bring characters from the movie to life can do so.)
Written to be performed as a DUO, although an ambitious performer could probably do it as an
HI. Specific gender should not be necessary for most characters. Depending on competition
rules for changing a piece, the “Prince” nomenclature could be changed to “Princess” to make it
a true Female / Female DUO.
Characters (With a suggested split between the two performers):
Witch - Performer 1
Narrator - Performer 1
Prince / Beast - Performer 2
Plate - Performer 2
Broom - Performer 1
Servant 1 / Coat Rack - Performer 1
Cup - Performer 1
Bucket - Performer 2
Footstool - Performer 2
Knife - Performer 1
Pan - Performer 1
Girl - Performer 1

(If performing as a DUO, Performer 2 starts center facing judge. Performer 1 starts back to Performer 2, facing upstate [back wall]).

NARRATOR: There lived a prince.

PRINCE: Hi there!

NARRATOR: The prince was a very selfish and terrible and abusive and vile prince.

PRINCE: Whoah.

NARRATOR: Who cheated through not only high school, but middle school, and even elementary school.

PRINCE: 11 and 12 should be oneteen and twoteen.

NARRATOR: The prince lived in a castle with many servants high above the town. And never went into town, probably because no one likes the prince.

PRINCE: People like me.I was elected to the secret homecoming court.

NARRATOR: What?

PRINCE: All four years of high school, I was elected to the special homecoming court. No one else ever was. It was a special honor, reserved only for the most important and special people in the whole school. I won it. Four years running.

NARRATOR: (Turns a bit to face the audience.) Are you serious right now?

PRINCE: I had my own VIP dance, very special. I had my own room, all to myself. No one else was allowed in.

NARRATOR: (Stares at audience for a beat.) I have to ask, sorry. Where was this room?

PRINCE: Basement, past the custodians closet. The theme was “Storage Closet”.

NARRATOR: Um…

PRINCE: (Cuts off.) Same theme all four years. Can you believe it? Even reused the decorations. My classmates had no creativity at all. But as my parents said, I must spend time amongst the vile, unwashed, terrible hoi polloi to …..

NARRATOR: (Cuts off) …become a great prince?

PRINCE: (Continues) … to realize how lucky I am and to realize their inferiority so I never ever ever help them or care about them.

NARRATOR: Right. And there we go. Cue witch.

PRINCE: Witch? Pff. So long as it isn’t a clown. Am I right?

NARRATOR: It was a dark and stormy night, the wind howled, the trees shook, and there was a knock at the castle door…..(Makes knocking sound.)

PRINCE: Servant! Get the door! It might be my pizza!

SERVANT 1: On it!

PRINCE: Don’t you dare tip!

SERVANT 1: Um, it’s for you!

PRINCE: No one comes to visit me. (Walks over to door.)

WITCH: Please, dear prince, I am but a poor woman caught in this storm. Could I please rest inside your giant castle until it passes? Perhaps use the bathroom. Perhaps get a cup of warm soup? Chicken Tortilla if you have it.

PRINCE: Vile woman. You disgrace my very opening. And then to have the gall to ask for soup?

WITCH: Do not turn me away, to do so would be to invite my wrath.

PRINCE: The wrath of an old, shriveled woman who likes soup? Pff. I care not. (Door Slams).

WITCH: (knocking)

PRINCE: Pizza! (Opens door.) You?!

WITCH: It is indeed I. But I am not a old, shriveled woman who likes soup. I am a (TRANSFORMATION)...

PRINCE: GASP! And other exclamations of amazement because of the lack of special effects to connote stunning transformation!

WITCH: …. A stunningly beautiful age-appropriate witch with perfect posture. (Pause) I do still like soup.

PRINCE: Ghastly!

WITCH: You have failed the test.

PRINCE: Test? But I didn’t have anyone to cheat off of!

WITCH: For your lack of kindness, I will put a curse on you and all who live in your castle.

PRINCE: It’s literally just me.

WITCH: No, it extends to all of your servants.

PRINCE: I don’t count them.

WITCH: This night you will transform into a vile beast, so that you are as ugly in your outward appearance as the hollows of your soul.

PRINCE: No! I am butt ugly in the hollows of my soul!

WITCH: The curse will only be broken when you get an intelligent, independent woman to fall in love with you.

PRINCE: Those are odd qualifiers. That usually isn’t my type…. So, what are the rules to this curse?

WITCH: There are literally hundreds. Which is why you need to get your rest. I will be back in the morning, 9 am sharp. Make sure everyone is here in the morning. I have a 6 hour presentation about the curse. Boilerplate human resources stuff. I have other people to curse, so I want to make good use of our time. Until the morn! (POOF disappear.)

PRINCE: She has disappeared in a cloud of smoke, and a crackle of electricity, leaving a faintly sulfurous smell in the air.

SERVANT 1: That was intense.

PRINCE: WHAT? You heard the whole thing?

SERVANT 1: We are cursed.

PRINCE: Have no fear. It was but an idle threat. You will see, come morning, that we have nothing to fear. (PRINCE turns upstage, NARRATOR now faces the audience).

NARRATOR: And thus began the curse of the prince and castle. For in the morning is the human resources meeting. As for the Prince, well, the prince found a mirror.

PRINCE: (from upstate) NOOOOO, I AM AS BUTT UGLY AS THE HOLLOWS OF MY SOUL! SUGGESTED INTRODUCTION BREAK - But you cut this as you see fit.

NARRATOR: Morning comes. 9:01 am.

WITCH: Settle down, settle down. Where’s the prince?

PLATE: Still sleeping, but can we address why I am now a plate?

BROOM: Why am I a broom? I was a cook. And now I’m a broom.

PLATE: So many questions.

CUP: If someone pours scalding hot coffee into me, does that hurt now?

BUCKET: Please tell me I am not a bucket to be used for what I think I am a bucket for?

WITCH: I would actually go sit by the prince’s bed, you can get caught up later.

BUCKET: That’s what I thought. Sh…

WITCH: (Cuts off). Okay then. Welcome all to the human resources presentation, “So You Woke Up Cursed, What Now?” I’m your host, the witch.

BUCKET: …it better be a good presentation. Someone take notes!

WITCH: Tough morning already, huh?

PLATE: So, let me get this straight…(Is interrupted)

WITCH: (Interrupts) Or, let me get this plate, am I right?

FOOTSTOOL: Wordplay! (Laughs)

BROOM: This is no laughing matter.

FOOTSTOOL: Gotta find the bright side of things.

WITCH: Love the attitude there. So, today, I am going to explain the rules of the curse, go over any questions, and then hopefully get you started on breaking the curse.

PLATE: Ok, so…(is interrupted)

WITCH: (Interrupting) Just, real quick. There will be a break for lunch. It is on your own. Nothing will be provided. I ask that you not go into town, just in case you don’t make it back for the afternoon portion. Also, you know we want to avoid mass panic.

FOOTSTOOL: Makes total sense. I like clear communication. Appreciate you.

WITCH: Appreciate you.

PLATE: WHY AM I A PLATE?

WITCH: Oh, that’s quite simple. You are a plate because your prince didn’t offer me safe haven from the storm. Or soup.

PLATE: And so why am I cursed for that? For something the prince did?

WITCH: Because you work for the prince.

PLATE: I had to work for the prince, do you realize what inflation is? My rent skyrocketed. And the inn in town was cutting back on jobs.

BROOM: I had to close my bookstore, I only had one customer, and since she was attractive I always gave her a discount.

FOOTSTOOL: Foreshadowing!

CUP: I’m just here because it was take your kid to work day yesterday! I don’t even work here!

FOOTSTOOL: Right, I was wondering who you were. I thought you were KNIFE for a moment.

KNIFE: I’m back here!

FOOTSTOOL: Hi Anita! I can’t see you!

KNIFE: I’m a knife!

FOOTSTOOL: Butter?

KNIFE: Butcher’s!

FOOTSTOOL: Nice!

WITCH: Okay then. Cup, I’m sure it will be a good learning experience for you.

CUP: I’m a cup!

WITCH: Now you will see the world through a different perspective.

PLATE: Listen, witch, I understand you are a witch. And so are evil.

WITCH: Whoah, that’s a pretty big stereotype.

PLATE: You turned good, kind, decent people into kitchenware and common household items.

WITCH: Right, I cursed you.

PLATE: Why not animals? Or beasts? Like the prince?

WITCH: Oh, that’s easy, it’s the prince’s curse. The prince’s soul. Or hollows of the soul, more accurately.

PLATE: But that doesn’t explain why kitchenware and common household items. I saw a dressing cabinet back there.

WITCH: Well, what if you have a guest and want to make a big song and dance about making dinner? And then the guest has to get dressed for dinner. You know?

FOOTSTOOL: Ohhh, it all makes sense now.

CUP: Will the guest break the curse?

PLATE: This seems like we are here solely for the prince and we are not really in control of anything.

WITCH: You get it.

PLATE: We did nothing wrong except, maybe, just maybe, work for somebody who was not a good person.

WITCH: A very vile person.

PLATE: That isn’t us.

WITCH: But you supported it.

PLATE: We had no other option. There is an economic reality. We have to work. And get paid.

WITCH: And he probably paid you next to nothing.

FOOTSTOOL: Actually, he was rather competitive.

COAT RACK: He wasn’t very good with money.

PLATE: I will concede he didn’t think he was paying us much, but he was comparing our wages to what his allowance was when a child so, he was …accidentally generous.

KNIFE: He once gave me a raise every week for a month!

FOOTSTOOL: Taylor ruined that one, told the prince every 6 months was typical.

PAN: Sorry! I thought that was common knowledge!

PLATE: So, why should we suffer?

WITCH: That’s the way of the system, my dear. The way things are.

PLATE: So, how do we break the curse? Let’s just break it and get back to normal.

WITCH: Great question. The prince, now a beast, a ghastly beast, and sort of smelly, must get an intelligent, independent woman to fall in love with him.

FOOTSTOOL: How do we know if she’s intelligent and independent?

WITCH: Just make sure she likes books.

PLATE: Right, that’s how he breaks his curse. How do I break my curse? Because I have a loving spouse at home in town, already loves me. So?

WITCH: I’m not finished. The prince has until this rose (shows rose) loses its last petal. After that, the curse is permanent.

BUCKET: Sorry to interrupt, Bucket here, the prince is still sleeping. Quick question though, this is a little awkward, when I have to go to the bathroom, do I use….(pause as trails off, half points to self)

WITCH: Well, you are (pause) what you are.

BUCKET: Right. So….(trails off awkwardly, points back at self)

WITCH: (A little uncomfortable) Yeah. There’s always one. If it makes you feel any better, it’s usually the nicest, most kind, open, loving, trusting person who gets your transformation.

BUCKET: Yup. That tracks. Okay then. Okay then. (Deep breath). I’ll go be me, then. I guess.

COAT RACK: Super awkward.

PLATE: So, wait. I’m a plate.

WITCH: Don’t sell yourself short. You are not “a plate”. You are a carefully crafted piece of fine china, a work of art, really.

PLATE: Right. So, hypothetically, when I was a person, if I, say, tripped and fell down the stairs, I would probably get a bruise. Skin my knee. Maybe sprain a wrist.

WITCH: RIght.

PLATE: Now, again hypothetically…

COAT RACK: (Whispers) I’m not sure you are using “hypothetically” correctly.

PLATE: …(Continues) let’s say, as a plate… COAT RACK; (Whispers) A carefully crafted piece of fine china, a work of art.

PLATE: …(Continues) as a carefully crafted piece of fine china, a work of art, I fall down those same stone stairs. What happens?

WITCH: Are they stone stairs?

PLATE: Does it matter?

WITCH: Not in the least. You would shatter into an incalculable amount of shards.

PLATE: I’d shatter into pieces?

WITCH: Oh no, pieces you could glue back together. Somewhere here there might be a hot glue gun, that’s hit or miss sometimes. But it wouldn’t matter: incalculable amount of fine shards. So fine and sharp I wouldn’t even recommend trying to pick you up.

PLATE: What?

WITCH: Especially if it were in an out-of-the-way spot? I’d just leave you. Hope you slowly disintegrate or something.

PLATE: (Hand out, trying to come up with the next question.) So, when the curse is broken, and we all change back?

WITCH: I wouldn’t recommend anyone you love seeing you when you turn back. Grisly.

PLATE: So, to sum up, I am cursed through no fault or power of my own, I cannot lift the curse through any power of my own, I could literally die with any false step, or even if I’m bumped into, and the only way I can hope to see my spouse again is if I help a spoiled, privileged, selfish prince find love and happiness?

WITCH: Spot on. Oh, and love with an independent, intelligent woman.

PLATE: Right. Can’t forget the qualifiers.

WITCH: Well, to be honest, at the last witch’s meeting, we all realized that most fairytales have the a sort of cookie cutter, shallow woman fall in love with an even more shallow rich prince. Not a lot of depth. And that’s just not a good message to send out. We want our curses to have a better message.

FOOTSTOOL: That’s really thoughtful of you all.

WITCH: Thank you. I’m actually the first one to try it. I’m really hoping for a good outcome.

FOOTSTOOL: Seems simple enough. How do we do that?

PLATE: Hold on. Because I don’t have position or money, I have no control? No power?

WITCH: Spot on. But you do have the power to influence the prince to find love. Be a better person.

PLATE: So, he wouldn’t listen to any of us when we were people, but he’ll listen to a plate?

KNIFE: I’m a butcher’s knife now, remember.

FOOTSTOOL: I bet Anita could make a pretty convincing argument then.

WITCH: It must be real, true love. It cannot be coerced.

PLATE: How are we to do this?

WITCH: It won’t be easy.

FOOTSTOOL: WAIT! Curses have loopholes and stuff. It’s like the genie’s wish or the monkey’s paw.

CUP: (Freaking out) Is there a genie inside me? Get it out, get it out, Someone rub me! PLATE; There’s no genie inside you. Someone poured tea in you.

CUP: Oh. (Seems to taste it.) Earl gray.

FOOTSTOOL: The love cannot be coerced.

WITCH: Correct.

FOOTSTOOL: But this is a curse on the prince. So the prince has to learn the lesson. Can the girl be coerced?

WITCH: What do you mean?

FOOTSTOOL: Can we figure out how to kidnap an independent, intelligent woman, hold her hostage, and then hope she slowly falls in love with the prince?

WITCH: Well, there’s nothing against that, per se.

PLATE: I thought this was supposed to be a good message you wanted this story to send?

KNIFE: I am a butcher’s knife!

FOOTSTOOL: But would it break any rules?

WITCH: Look, it doesn’t technically break any rules. But I would advise against it.

FOOTSTOOL: Why?

WITCH: I’m not going to go into it here, there are countless YouTube videos and Reddit threads you can look at which will explain the problematic messages that plan would send.

PLATE: We don’t get Internet here.

WITCH: What?

FOOTSTOOL: The Prince said it was a needless expense.

WITCH: What expense? The town has been on free Wi-fi for almost a year now.

FOOTSTOOL: WHAAAAAT?

WITCH: It was part of their rejuvenation plan to attract younger workers to the town. Remote work is here to stay, you know.

PLATE: So, we could be watching Netflix right now? Stranger Things could be on the table?

WITCH: The password is G@ST0N1. (That’s a zero not the letter. Let that be a joke for just people who can connect it.)

FOOTSTOOL: (Pulls out the phone) Works! I can Insta!

CUP: I HAVE NO HANDS! How am I going to play Minecraft? (Or insert other phone-based game that is popular.)

PLATE: We need to find an independent, intelligent woman we can trick!

BROOM: I’m looking up Stockholm Syndrome!

FOOTSTOOL: I’m following a tinkerer’s daughter who is intelligent, independent, and sort of seems alone with her head in the clouds.

WITCH: This is getting wildly out of control here. You shouldn’t kidnap someone to make them fall in love with you.

PLATE: You set the rules, witch. If this is the system, we have to do what it takes.

COAT RACK: We do know the prince is persistent. Remember in high school? The crush? Every day standing with a flower and a box of money by her locker. What was her name?

FOOTSTOOL: Oh yeah…..

KNIFE: Her name was Anita!

FOOTSTOOL: That’s it. What ever happened to her?

WITCH: There’s a real fine line with persistence. You are sort of describing someone who stalks.

FOOTSTOOL: She followed me back!

PLATE: Now we are cooking.

FOOTSTOOL: I told her we had a great library and she should come check it out.

WITCH: She’s not going to be lulled with so phony an offer. No one’s that stupid.

PLATE: You said her intelligence was to be measured just by her love of books, not Internet scams.

WITCH: Well…

FOOTSTOOL: Shoot, I just got a text that my Amazon account was hacked and I need to click this link to confirm my account information or they’ll lock me out forever. I need to take care of this.

CUP: Is this when we make dinner? But it’s lunch. Am I hungry? Do we eat still?

BUCKET: (Walks up with sloshing.) Prince is up. In case you didn’t connect that sound, that’s sloshing. I will admit the Prince did at least apologize as we were (Searches for the right word) communing. So, that’s progress.

CUP: I don’t think that’s Earl Gray tea.

WITCH: Is the prince coming down?

PRINCE: What did I miss? (KNOCK KNOCK KNOCK)

GIRL: I’m here for the library tour?

PLATE: Right this way.

WITCH: It’s a trap!

FOOTSTOOL: Solid reference.

COAT RACK: She ran away.

PRINCE: Was that a beautiful woman who had arrived looking to love me?

PLATE: (Same time as witch) Yes.

WITCH: (Same time as Plate) No.

PLATE: That was our best chance…

WITCH: Ok! That’s it! Curse off!

BUCKET: Quick! Someone empty me out!

CUP: I like tea, so I don’t mind it.

PRINCE: I sort of like being a super strong and agile beast person.

KNIFE: I’m still a knife!

PLATE: And I’m still a plate.

WITCH: Look, these things go sunset to sunrise. So, you’ll have to tough it out until next sunrise. Plate, just go somewhere quiet and safe.

PRINCE: I’m going to run around the woods all beast like! Roar!

WITCH: Everyone just leave!

PRINCE: RABBIT!

NARRATOR: And so the witch sat alone in defeat. Hoping to change the messages of fairytales of lore, but failing miserably and almost creating an even more problematic set of messages, including, never try something new. The end. Roll credits.

PLATE: Hey.

WITCH: Plate, you stayed.

PLATE: This is sort of like the end credits stinger. I just wanted to say: Thank you.

WITCH: You ruined everything, you know.

PLATE: I mean, it’s messed up I’m thanking you. You cursed us all for someone else’s actions. Not our fault But you at least realized how you can’t always control the message. People are going to people.

WITCH: And now the message is if you are annoying and vexing enough you’ll get what you want.

PLATE: No position. No money. But anyone can be annoying and vexing.

WITCH: And the prince? He didn’t even change. Not even a little.

PLATE: If anything he’s having fun out there as a beast.

WITCH: I hate it all sometimes.

PLATE: I get it.

WITCH: I just wanted to use my power to make the world a better place.

PLATE: You repaid negativity with negativity. It went wrong. Maybe we need to try just putting love and kindness into the world.

WITCH: And turn into Buckets?

PLATE: Maybe. Maybe not. END PLAY
```

---

## IC-0525: Brooke Marigold, PI

- Title: Brooke Marigold, PI
- Author (byline): Kevin Burgun
- Work: Brooke Marigold, PI
- Publisher: Mushroom Cloud Press
- Publication date as stated: August 15, 2024
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: BROOKE, MRS. GLADSTONE, TRIXIE, TEACHER, BOBBY, DETECTIVE SPARROW, PATROL OFFICER STACY, PATROL OFFICER, BOSS, BUS DRIVER, TEDDY, MOTHER, BOSS / MRS. GLADSTONE, BOSS/ MRS. GLADSTONE
- Teaser before the introduction: No
- Spoken words (computed): 2100
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
A Humorous Piece
By Kevin J. Burgun
Suggested Doubling:
Performer 1:
Brooke Marigold
Teacher / Mrs. Gladstone
Patrol Officer Stacy
Teddy
Boss
Performer 2:
Trixie
Bobby
Detective Sparrow
Bus Driver
Mother

BROOKE: (As a noir detective voiceover) It was nap time. Thursday. The sun had been out earlier, but the clouds had recently come in casting a pall over the hopscotch court. The wind picked up a little. The “caution tape” strung around the monkey bars making a sound like streamers. But I wasn’t fooled. I knew what it meant. A case. Every time. So, I waited to Mrs. Gladstone to start scrolling the Gram. The rest of the kindergarteners were quiet. Too quiet. I took out my juice pouch, that’s right, a pouch, I never went in for the boxes. Boxes were for immature kids. I was a pouch girl. Precocious. Mrs, Gladstone said that once. The tone was’t flattering. I didn’t care. The word was. I’m Brooke Margold. I solve crimes.

MRS. GLADSTONE: Brooke, keep it down.

BROOKE: I didn’t have to wait too long. Two sips. And then she walked in. The dame.

TRIXIE: Brooke?

BROOKE: That’s what it says on my backpack, my lunchbox, my pencils, and my socks.

TRIXIE: I can’t find Teddy.

BROOKE: Boyfriend? Love triangle was my first thought. Trixie wasn’t the type to settle down. She colored outside the lines. I’d seen it. And she once turned a horse for an art project into a unicorn. FLASHBACK

TRIXIE: Unicorn!

TEACHER: Trixie! Those are mythical creatures! The new state guidelines specifically forbid mythical creatures until May.

TRIXIE: Mommy always says: It’s May somewhere. BACK TO PRESENT

BROOKE: She wasn’t constrained by society’s rules.

TRIXIE: Who are you talking to?

BROOKE: The kid was sharp. Maybe there was more to this than I had first thought.

TRIXIE: Can you help?

BROOKE: I charge by the hour.

TRIXIE: My mother just got back from Costco.

BROOKE: Juice pouches?

TRIXIE: And graham crackers shaped like dinosaurs.

BROOKE: Darn it, I only knew “darn it” so far. I once almost got a 3rd grader to teach me some swear words. But I’m pretty sure “flabbergasted” wasn’t going to cut it, dinosaur grahams, the kid knew my weak spot.

TRIXIE: Cinnamon AND Chocolate flavored.

BROOKE: Flabbergasted. I’m in. Tell me about Teddy.

TRIXIE: Well…

MRS. GLADSTONE: Okay girls, are you done with your nap early?

TRIXIE: I’ll nap when I’m dead.

BROOKE: Our teacher. Mrs. Gladstone. The one who took down Bobby. FLASHBACK

BOBBY: You’ll never prove I put the gum under those desks in those kids hair, you hear me? You’ll never prove it.

MRS. GLADSTONE: I know you did it Bobby Drakenson. I know you did it.

BOBBY: If I did it, where are the wrappers then? Where are the wrappers?! BACK TO PRESENT

BROOKE: She found the wrappers. Bobby went to the corner. And no one has questioned her since. Until today. Until Trixie. And I. And me. I? Me?

TRIXIE: And us!

MRS. GLADSTONE: Are you ready for show and tell?

TRIXIE: (Bursts out crying)

MRS. GLADSTONE: Oh dear, what’s wrong?

TRIXIE: (still crying - like this is serious crying)

BROOKE: The kid was nuts.

TRIXIE: TEDDY IS GOOOOOOOOONE. (The longer you draw it out the better. Don’t underestimate the deep breath at the end, then continuation.)

BROOKE: You were going to show and tell your boyfriend?

TRIXIE: No, that wasn’t my show and tell. But my teddy bear, Teddy, is gone.

BROOKE: That makes more sense than boyfriend.

BOBBY: Uh, Mrs. Gladstone, want me to run that errand now?

MRS. GLADSTONE: Do I have to micromanage you?

BOBBY: On it.

BROOKE: Flabbergasted Bobby Drake.

TRIXIE: Teddy was my best friend. I loved staring into his eye.

MRS. GLADSTONE: Oh, Trixie, dear, I am so sorry, where did you see him last?

TRIXIE: I had him this morning.

BROOKE: Where was the last place you saw him?

TRIXIE: On the bus, for sure. He was getting a little motion sick, so I had to pat his back.

BROOKE: The bus driver was a substitute today.

TRIXIE: He smelled like dill pickles and crushed dreams.

MRS. GLADSTONE: Maybe you left him on the bus, Trixie.

TRIXIE: But whyyyyyyyyyyyyyy?

BROOKE: Mrs. Gladstone, may I please go to the office?

MRS. GLADSTONE: Brooke Marigold, you aren’t going to sneak out of school again to go on some crazy detective adventure, are you?

BROOKE: No, ma’am.

TRIXIE: You aren’t?

BROOKE: (Aside) Of course I am, Trixie. I’m taking your case. I just have to dissemble a bit to Mrs. Gladstone.

TRIXIE: What does dissemble mean?

BROOKE: I don’t know. But my mom uses it all the time after my dad comes home from working late. I think it’s like a reason why you do something.

TRIXIE: Ohhhhhh.

BROOKE: Hang tight, kiddo. I’ll have it solved by afternoon pick-up.

TRIXIE: Can I come with you?

BROOKE: I’m about to sneak out of school and track down a dangerous teddy bear napper. Of course you can come along. Every good detective needs a sidekick to watch her back.

TRIXIE: Yay! I’ll dissemble to Mrs. Gladstone as well. I’ll tell her I need to go poop.

BROOKE: That’s good, and it also will explain why you don’t come back right away.

TRIXIE: I’ll tell her I’m consumated. TRANSITION

DETECTIVE SPARROW: This better be good, dragging me out of bed.

PATROL OFFICER STACY: It’s mid-morning, detective.

DETECTIVE SPARROW: Look, I’m a grizzled, cynical, weary detective 14 months from retiring. That’s just what we say. It’s in the manual.

PATROL OFFICER STACY: Sorry, I didn’t read the manual. I’m an eager, fresh-face patrol officer who also thinks they know it all, so can’t be bothered with manuals.

DETECTIVE SPARROW: Look at us, true originals. What do we have?

PATROL OFFICER STACY: Abandoned bus. Cameras inside disconnected. Inside the bus, it’s not pretty, detective.

DETECTIVE SPARROW: Damnit. Kids? What evil is this?

PATROL OFFICER STACY: No, not kids. But there was…

DETECTIVE SPARROW: Out with it.

PATROL OFFICER STACY: Stuffing. Okay, there was stuffing.

TRIXIE: Stuffing?!

DETECTIVE SPARROW: Damnit, who the hell are you two?

BROOKE: One moment. (writes in notebook.)

DETECTIVE SPARROW: What are you writing?

BROOKE: How do you spell “hell”? Never mind, I’ll ask ChatGPT. Brooke Marigold, private investigator.

DETECTIVE SPARROW: Patrol Officer Stacy, I thought I told you to put up crime scene tape.

PATROL OFFICER STACY: I did! Detective I swear.

BROOKE: We walked right under it.

TRIXIE: I didn’t even need to duck.

BROOKE: It looks like our cases have rammed into each other. It’s okay, I’ll take lead.

DETECTIVE SPARROW: Kid, you have 5 seconds to get out of here, or ….

BROOKE: Detective…Sparrow, was it? I made a promise to Trixie here to find Teddy, her teddy bear, I don’t break my promises.

DETECTIVE SPARROW: You are going to break this one.

BROOKE: So, you don’t need me?

DETECTIVE SPARROW: I do not.

BROOKE: So, you know what happened here?

DETECTIVE SPARROW: We’ll figure it out.

BROOKE: Patrol Officer Stacy.

PATROL OFFICER STACY: Yes?

BROOKE: How much stuffing? .

TRIXIE: Teddy!!!!!!

PATROL OFFICER: More than I wanted to see.

BROOKE: But enough to think that Teddy is still viably a teddy a bear?

DETECTIVE SPARROW: What are you suggesting?

BROOKE: Are we looking for a teddy bear, or a pile of fabric?

DETECTIVE SPARROW: Kid!

BROOKE: Answer the question, Patrol Officer! Just stuffing? Did you see an eye?

(Long pause.)

PATROL OFFICER STACY: I’d say there’s hope.

BROOKE: Detective, did you know that bus driver of that bus was a substitute?

DETECTIVE SPARROW: You don’t say?

BROOKE: And I’m sure you already spotted the teddy bear paw prints in the oil slick over there. Indicating a teddy bear was dragged.

TRIXIE: Teddy!!!!!

BROOKE: Against its will, more than likely.

DETECTIVE SPARROW: Ok kid. You’re in, but you mess up even once, and you are in a cell.

BROOKE: Deal. Now, let’s get a look at this stuffing.

TRIXIE: Teddy!!!!! TRANSITION

BOSS: Where is the diamond?

BUS DRIVER: Boss, it wasn’t in the teddy bear. I looked.

BOSS: Our info said that the kid, Trixie Van Der El Van Hatterhornson, was bringing the King’s Diamond to show and tell today.

BUS DRIVER: Right.

BOSS: And that the diamond was in or on the teddy bear.

BUS DRIVER: Right.

BOSS: Our inside rat told us that this Trixie was all upset that the teddy bear was taken.

BUS DRIVER: Right.

BOSS: Ipso facto…..

BUS DRIVER: Gesundheit.

BOSS: No, you idiot, ipso facto we have the diamond.

BUS DRIVER: I looked all through the bear. No diamond.

BOSS: You missed it.

BUS DRIVER: I brought the bear, here it is. Look.

TEDDY: (look all disheveled, be still and quiet)

BUS DRIVER: No matter what I did, it wouldn’t talk. Would you bear?

TEDDY:

BUS DRIVER: Where’s the diamond?

TEDDY:

BUS DRIVER: I’m not afraid to pluck out that radiant, sparkling, precious eye. You’ll never see with proper depth again.

TEDDY:

BUS DRIVER: See, boss? Won't give it up.

BOSS: I’ve seen this before. Oh yes I have.

BUS DRIVER: What do we do?

BOSS: Bring me the girl. Trixie. Let’s see how tough Teddy is then.

TEDDY: (Eyes should widen in shock.) TRANSITION

DETECTIVE SPARROW: The paw prints suddenly stop.

BROOKE: Got into another vehicle.

DETECTIVE SPARROW: So, the bear is gone. Time to write it up. Stacy, that’s on you.

BROOKE: Not so fast. Look.

DETECTIVE SPARROW: Tire tracks? So what?

BROOKE: Those aren’t just any tire tracks, detective.

DETECTIVE SPARROW: You recognize the tire tracks?

BROOKE: I do. But. I never thought I’d see them again. Ever. FLASHBACK

MOTHER: Now Brooke dear, you have too many stuffed animals, you need to give one away to the toy drive.

BROOKE: But I don’t want to, Mother!

MOTHER: Brooke, you have to help others. What about this teddy bear here? You have another one exactly like it.

BROOKE: The twins?? You can’t break up the twins!

MOTHER: It’s settled, Brooke, in time, you’ll see this is for the best. BACK TO PRESENT

BROOKE: And that’s the twenty-third most painful memory of my life.

TRIXIE: But Brooke, that means.

BROOKE: Yeah, Trixie. Yeah.

TRIXIE: We’re related?

BROOKE: By teddy bear.

DETECTIVE SPARROW: But what does this have to do with the tire tracks?

BROOKE: Detective? Really?

TRIXIE: Try and keep up, detective. TRANSITION

DETECTIVE SPARROW: The old warehouse district.

BROOKE: The old warehouse district.

TRIXIE: The old warehouse district.

PATROL OFFICER STACY: The old warehouse district.

DETECTIVE SPARROW: Patrol Officer? What are you doing here? I thought we left you back at the bus?

PATROL OFFICER: I follow my own rules.

TRIXIE: What’s in the bag?

PATROL OFFICER: Teddy’s stuffing. I put it in a cotton bag. 800 thread count. Keeping it on cotton in case we are in time to restuff.

DETECTIVE SPARROW: First we have to find the warehouse.

BROOKE: There’s only one warehouse where you can’t hear a teddy bear scream.

TRIXIE: What? TRANSITION

BOSS: You’re sure they are here?

BOBBY: Yup, I’ve been following them. That Brooke Marigold is a pretty fantastic detective.

BOSS: Arch nemeses usually are.

BUS DRIVER: Hear that, Teddy? Soon you’ll be in a world of emotional pain and torture.

TEDDY:

BOBBY: So, about my payment. The gum?

BROOKE: Bobby Flabbergasted Drakenson.

DETECTIVE SPARROW: Everyone freeze. The gig is up.

BOSS: Detective.

DETECTIVE SPARROW: Do I know you?

BROOKE: She was talking to me. Weren’t you? Miss?

BOBBY: I’m out of here, keep the gum!

BOSS / MRS. GLADSTONE: (Slow Claps) Well done, detective Marigold. Well done. (Mimes taking off mask.)

TRIXIE: (Gasp!) Mrs. Gladstone!

BOSS/ MRS. GLADSTONE: Trixie Van Der El Van Hatterhornson. How’s the poop?

TRIXIE: I’m very very consumated.

BOSS/ MRS. GLADSTONE: Apparently.

DETECTIVE SPARROW: Your kindergarten teacher? But why?

BOSS/ MRS. GLADSTONE: But why? Does a public servant such as yourself really need to ask that?

TRIXIE: Where’s Teddy?

BROOKE: The money. It’s always about the money.

TRIXIE: Teddy is priceless!

BOSS/ MRS. GLADSTONE: For two long years, I dedicated my life to molding young minds. I endured sticky fingers, endless 'why’s, and the symphony of a thousand off-key recorders. Do you know what it’s like to be paid in peanuts while trying to teach children not to eat them?

TRIXIE: Mrs. Gladstone, I’m allergic to peanuts though.

BOSS/ MRS. GLADSTONE: I taught them to count, but had to skip my own lunch to balance my budget. I preached about the importance of sharing, while I couldn't even afford to share in a decent retirement plan. And let’s not forget the mountain of paperwork! They told me it was about ‘accountability.’ Accountability?

DETECTIVE SPARROW: Mrs. Gladstone, you are under arrest for the destruction of a teddy bear and attempted robbery.

BOSS/ MRS. GLADSTONE: And then, the pièce de résistance—standardized testing! I became a drill sergeant of the alphabet, turning innocent playtime into a regimented nightmare. No longer could we turn horses into unicorns, we had to just (pause) color (pause) horses. So, I’m out. And this was my way out.

DETECTIVE SPARROW: Look at it this way, you are still out.

BROOKE: As soon as I saw those treads. Worn out. Almost bald. Only one profession can’t afford new tires. Teachers. And only one teacher knew where Teddy would be today. You. Book her, detective. I need a juice pouch.

TRIXIE: But where is Teddy?

BOSS/ MRS. GLADSTONE: Where, indeed?

BUS DRIVER: He’s just in the other room there. Remember?

BOSS/ MRS. GLADSTONE: That was my last bargaining chip!

DETECTIVE SPARROW: Substitute bus driver, you are under arrest for the mutilation of a teddy bear. TRANSITION

TRIXIE: Teddy!

TEDDY:

TRIXIE: I’m sorry about all of this. But the the nice patrol officer has your stuffing. You’ll be all better in no time!

TEDDY: TRANSITION

DETECTIVE SPARROW: It’s tough for me to say this, but good job, kid.

BROOKE: You didn’t do half bad yourself.

(This next “scene” can be cut if one cannot figure out the choreography of it. If it’s done, then you would keep the same “One thing bothers me” of the subsequent “scene”.)

DETECTIVE SPARROW: There’s one thing that still bothers me, though.

BROOKE: What’s that?

DETECTIVE SPARROW: I’m a grizzled, cynical, weary detective 14 months from retiring.

BROOKE: And?

DETECTIVE SPARROW: Nothing happened to me. I didn’t get shot. Or anything.

BROOKE: You’re right. (Pause) Oh no.

BOBBY: Take that! (Bobby throws a piece of gum at the detective.)

BROOKE: Nooooooo!!!!! (Brooke jumps in front of the gum, taking the full force of it.)

DETECTIVE SPARROW: Kid!!!!!! Kid, kid, Are you okay? You took a piece of gum for me.

BROOKE: (Coughs) Watermelon twist.

DETECTIVE SPARROW: I owe you one.

BROOKE: To the next adventure.

(End the optional scene.)

DETECTIVE SPARROW: Just one thing bothers me though.

BROOKE: What’s that?

DETECTIVE SPARROW: Where’s the diamond?

PATROL OFFICER STACY: Teddy took the restuffing well. He’s back.

TRIXIE: I think Teddy can explain, detective.

TEDDY: You see, detective, our love for each other is the true diamond. Sacrificing for each other. Never giving up. Pushing each other to be the best we can be. That, truly, is priceless.

DETECTIVE SPARROW: So, there was no diamond?

TEDDY: Oh? The King’s Diamond? It’s my left eye.

BUS DRIVER: The eye! END
```

---

## IC-0526: Cassadee and Ketamine Save

- Title: Cassadee and Ketamine Save
- Author (byline): Collier Kuhlman
- Work: Cassadee and Ketamine Save
- Publisher: Mushroom Cloud Press
- Publication date as stated: December 1, 2024
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: KETAMINE, CASSADEE, RYDER, MRS SMITH, BOTH, ANTHONY, CASSADEE & KETAMINE
- Teaser before the introduction: No
- Spoken words (computed): 2090
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
“Cassadee and Ketamine Save a Non-Verbal Child From a Well” A Humorous Interpretation By: Collier Kuhlman

Synopsis: Cassadee, the snobbiest 9 year old alive, is forced to go to a strange country girl named Ketamine’s “party”, but when thirst leads the two down to a well in the middle of a trailer park, trouble unfolds. When they see a person down at the bottom, the girls know they will have to give all they have to save Anthony, you’re average malnourished well boy, and give him what he really needs, a bath.

KETAMINE - Country, Trailer trash, Southern accent, Unaware. CASSADEE SMITH- Acrylic nail/VSCO type girl, has the newest iPhone, Rich. RYDER - Casadee’s boyfriend. Star quarterback of the 8U parks & rec football team MRS. SMITH - Cassadee’s mother. Elementary school principal. ANTHONY - Kind of reserved. Doesn’t speak that much. Probably shy. Must be due to the fact that he has spent the last 9 years of his life at the bottom of a brick-lined wet pit in the middle of a trailer park.

KETAMINE: (Awkward, borderline southern grandma tone even though she and Cassadee are the same age) Hey Cassadee!, it’s me… Ketamine.

CASSADEE: (Looking up from phone) What do you want dweeb?

KETAMINE: (looking at ripped up Hey Dudes) Yeah, I like your outfit too! So um, I’m having this party tonight, annnnd umm, you should totally be there! I think mama’s makin’ mac and cheese, but don’t worry, she won’t put any form of contraceptive tablets crushed up into a fine powder in the cheese this time.

CASSADEE: Why the heck would I want to go to your party? I have a date with Ryder tonight.

RYDER: Hey babe.

CASSADEE: Heyyy Rydy-Wydy!!! So… What time do you think we should start our evening? I say sunset because it will be sooooo romantic…

RYDER: Ohhhh, Cassadee… I’ve been meaning to tell you… I can’t make it to our date tonight…

CASSADEE: WHAT?! WHY?

RYDER: I’m banned from logging on to Roblox… I guess the moderators didn't really dig our hot cybers-

CASSADEE: But it was consensual?!

RYDER: I know babe! I know. But I promise I won’t let this seperate us. Ryd-a-dee is forever! (RYDER exits. CASSADEE seems sad.)

CASSADEE: (Crying) Oh my god! This is worse than 9/11 AND when the BeReal went off while Ryder playing legos with Sarah! What does this mean for our future? I mean, he’s the hottest guy in the 4th grade… and the week I finally make him mine, he gets suspended from Roblox and I can’t make out with his cute little pixelated lip-

MRS SMITH: Cassadee darling, what’s wrong?

CASSADEE: Go away mom!

MRS SMITH: Cassadee, drop the tone. I applied to be a principal at this school to be closer to you, and when I got the job I assumed that you would enjoy it! Now tell your mother what’s wrong or I will go through your Roblox chat log again.

CASSADEE: NO PLEASE FINE I’LL TELL YOU! It’s just, Ryder canceled our hot da- I mean he got banned from Roblox for being too nice and sweet and perfect and SUCH a good kisser… I had been looking forward to this since we started dating on Monday, and now I don't know what I’m going to do tonight! I need a Xanax!

KETAMINE: You could come to my place! Mama made her extra special macaroni n’ cheese! It might be a little stronger than Xanax though…

CASSADEE: No, I'm not going to go to your house Ketamine!

MRS SMITH: CASSADEE LEIGHANNE-MARIE-RAE-QUESO-JOSEPH-BRYLEIGH-FORD-F-150 SMITH! Let's be nice to Miss Ketamine.

CASSADEE: Sure! I’d love to go to your party tonight!

KETAMINE: Awesome! (Scribbles on scrap paper and hands to Cassadee) Here! Meet me here at 5 PM!

CASSADEE: Yeah… sure… (Scene changes and we are at Ketamines trailer in the trailer park.)

KETAMINE: Welcome to my humble abode! (Both eyebrows raise twice and she gives a wink.)

CASSADEE: Sure is humble alright… (rolls eyes) I thought this was a party… Why is it just me? (Ketamine doesn’t respond)

KETAMINE: Come on in! (they enter.) Ope, here's my mama’s world famous macaroni! It’s a little stiff because the special powder she adds to it for flavor has a tendency to chemically combine with the cheese and form a compound that stiffens the mixture, creating a slab of dairy smothered noodles. It’s extra stiff this time… but that’s probably because instead of adding birth control, she added crystal methamphetamine!

(Ketamine takes a large whiff, sucking up the aroma from the macaroni with her gigantic nostrils.)

CASSADEE: Yeah… I’ll pass… Can I get a glass of water or something?

KETAMINE: Um… Sorry… I- erm…

CASSADEE: Spit it out loser!

KETAMINE: We don’t have runnin’ water… but um… we could go to the well at the bottom of the hill!

CASSADEE: Okay... whatever, but if my heels get all muddy, you’re paying. (They traverse down the hill and arrive at the well.)

KETAMINE: Here we are! (The two peer into the well. Cassadee is shocked and gasps in horror)

CASSADEE: OH MY GOD!!! IS THERE A KID DOWN THERE!?!?!?!?

KETAMINE: Oh that’s Anthony. He’s non-verbal. He’s been down there for years. Nine to be exact. Rumor has it, when his mother went into labor, she couldn’t drive to the hospital because her boyfriend had the car because he had to drive to K-Mart to complete a human trafficking scheme. She ended up just waddlin’ down to this here well and poppin’ a squat. Tony was born, and he’s been down there ever since. Nobody ever taught him how to talk.

CASSADEE: Oh my… what happened to his mom?

KETAMINE: FBI got her. Guilty by association.

CASSADEE: Association to what?

KETAMINE: Human trafficking, remember?

CASSADEE: Oh yeah, sorry.

KETAMINE: (sighs happily while shaking head reminiscently) What a time to be alive.

CASSADEE: (snapping back into fear) Well… we have to get him out somehow!

KETAMINE: So what, you wanna do a rescue mission?

CASSADEE: Well I was thinking you do all the climbing down the moldy pit in the ground and I do all the, you know, standing and watching.

KETAMINE: Oh that won’t be necessary. We can just get something to pull him up with.

CASSADEE: Do you have rope or something?

KETAMINE: No.

CASSADEE: Well what the hell did you want us to use?!?!

KETAMINE: I don't know… I never thought that far.

CASSADEE: Jesus… Well do you have any… like… clothes that we could tie together? I mean I'm guessing camo overalls will be pretty sturdy.

KETAMINE: This is my only outfit. Mama tries not to spend too much on things that I’m only ever gonna wear 8 hours of the day anyway.

CASSADEE: You only wear clothes at- you know what… nevermind. Do you have like… towels or something?

KETAMINE: Nah… mama says that after you take a bath, you’re s’pposed to just lay out in the grass, naked as a tater cake, and let the sun work it’s magic.

CASSADEE: Ew…

KETAMINE: It’s the way God intended.

CASSADEE: Whatever… Are you sure you don’t have rope?

KETAMINE: Come to think of it, mama does! She used to tie up my step dad with it! It might have a few stains and… bite marks… here and there but rope is rope.

CASSADEE: (slightly grossed out) That works. But just so you know, I’m not touching it.

KETAMINE: Fine by me! I’ve touched grosser things my stepdad has used! I’ll be right back. (Ketamine leaves and returns with rope and peers over well)

KETAMINE: Anthony! Yell if you can hear me! (awkward pause)

KETAMINE: Well, that's strange. You try!

CASSADEE: Ok whatever. Anthony… can you hear us? (awkward pause. The two look at each other and realize simultaneously)

BOTH: Ohhhh. He’s non-verbal.

KETAMINE: Well fish sticks.

CASSADEE: How are we going to tell him to grab the rope?

KETAMINE: He’s not deaf, you dumb nut.

CASSADEE: Right.

KETAMINE: Here… (Ketamine throws the rope down the well and the rope grazes Cassadee’s face before the rest plummets down into the well.)

CASSADEE: EW! EW! EW! THIS ROPE SMELLS LIKE AN OLD MANS BUTT!

KETAMINE: Most things around here do, you’ll get used to it. (looking back down into well) ANTHONY! TELL ME WHEN YOU HAVE HOLD OF THE ROPE! (awkward pause. The two look at each other and realize simultaneously)

BOTH: (Sounding exactly like the first time) Ohhhh. He’s non-verbal.

KETAMINE: Ok well… I’m trusting you Tony! (The girls grasp the rope in a line and begin to pull, making grunting noises)

CASSADEE: You know, for a kid who hasn’t eaten in nine years, you sure weigh a lot, Anthony!

(They eventually pull him out of the well, breathing heavily. Anthony emerges, looking malnourished. He has a look on his face that would lead someone to believe he has witnessed something despicable.)

KETAMINE: (hugging him) Oh Anthony, oh Anthony! I haven’t talked to you in years! I always felt our conversations were one sided… but oh boy have I still missed you!

ANTHONY: (moans in a Hellen Keller-esque voice)

CASSADEE: Ew. (Ketamine takes a few whiffs, making a nasty face)

CASSADEE: He stinks!

KETAMINE: Welp, I’m definitely not used to that!

ANTHONY: (moans in a Hellen Keller-esque voice)

KETAMINE: Lets get you a bath… (The girls pick Anthony up and return to the trailer, in the bathroom)

KETAMINE: Luckily, you’re so small and malnourished and pitiful and thin, you’ll fit in the sink! (she loads him into the sink) We couldn’t put you in the bath, because, get this, we dont have any running water! (she laughs uncontrollably, throwing in a few knee slaps.)

CASSADEE: You do realize that washing him in the sink would require running water too, right?

KETAMINE: What? Oh. I never thought about that. I’ve never tried to use the sink.

CASSADEE: How do you wash you’re hands then?

KETAMINE: Oh, mama doesn’t believe in warshing our hands. ‘Specially with soap. She says all the little toilet critters are good for the skin. They maintain a nice moisture barrier.

CASSADEE: Okay… gross. So , are we gonna go back to the well to get water, or what?

KETAMINE: On it! (she begins to run out of the bathroom, but it stopped by Cassadee.)

CASSADEE: You can’t just leave me here alone with this… thing!!

KETAMINE: Well I can’t take him with me! Do you think he wants to see that well again? He’s traumatized!

CASSADEE: Okay fine! I’ll stay here with Anthony, you go get some water. (Ketamine nods and then runs off. Cassadee begins venting to Anthony)

CASSADEE: I can’t believe I’m here. Ugh, this is so lame. You know, I was supposed to be on a date with Ryder tonight. (pause) Who’s Ryder? Oh. Ryder is my boyfriend. He is SO TOTALLY SUPER dreamy. He’s basically like Harry Styles, but instead of me liking him because I fetishize muscular gay men, I like him because he plays football. But… I don’t know… recently he’s been acting strange.

ANTHONY: (moans in a Hellen Keller-esque voice)

CASSADEE: I just feel like he likes Sarah more than me, even though (mockingly) “Sarah” wears clothes from Walmart, and she only texts him from her iPod touch… 2nd generation! I just don’t even know how he still likes her, I mean, we’ve been dating for 3 whole days! (crying) She’s so lame and I think he wants to leave me and I- (Ketamine barges in)

KETAMINE: Heres the water! (Ketamine pours the water over Anthony’s frail, anappealing body and they begin to make circular scrubbing motions over him with their hands. They do this silently for a few moments)

CASSADEE: I don’t think this is working.

KETAMINE: You’re right… I’ll go grab some soap.

CASSADEE: I thought your mom didn’t believe in soap.

KETAMINE: Oh right. Sorry. I can see if we have some Draino, or some mayonnaise perhaps.

CASSADEE: (weirded out) Great. Do that…

(Ketamine exits once more. Cassadee begins talking to Anthony again.)

CASSADEE: (flirtatiously) Alone again. Finally. You know, I actually really enjoyed talking to you Anthony. You’re really sweet, and SUCH a good listener. I dont know… (she begins scrubbing in circular motions again) I guess what I’m trying to say is…. (Cut to Ketamine rummaging through the kitchen to find mayonnaise or Drano. She cannot find anything.)

KETAMINE: Aw, fiddle sticks! (She goes to the next room and grabs two things before returning to the bathroom.)

KETAMINE: I’m back! I couldn’t find draino or mayonnaise, but I did find an entire bottle of Crown Royal and some water-based lubricant in mamas room!- (pause) Oh… I’m sorry. Did I walk in on something?

CASSADEE: (playing it cool) No! Nothing happening here! (giggles awkwardly)

KETAMINE: Ohh! I see! You want to get his Roblox username, if you know what I mean… (Ketamine winks twice.)

CASSADEE: I… uh…

KETAMINE: Anthony… do you even have Roblox? (a few second pause)

ANTHONY: (moans in a Hellen Keller-esque voice)

CASSADEE & KETAMINE: Ohhh. He’s non-verbal.

ANTHONY: (In southern trailer park man voice) Can you take me out of this sink and provide undergarments please?

CASSADEE & KETAMINE: (scream violently)

ANTHONY: Why are you scared? You’re acting like you’ve never seen a malnourished man from a well playing the role of the central intelligence of a human trafficking scheme.

KETAMINE: Do what now?

CASSADEE: Anthony, since when can you talk?

ANTHONY: What do you mean? I’ve been talkin’ for all 62 years of my life.

KETAMINE: But… Anthony? I thought you were only nine?

ANTHONY: Lot’s of people seem to think that just because I’ve been down in that well for nine years, im nine years old.

CASSADEE: But that doesn’t add up… you were born over the well, and you’ve been down there for nine years. You’re supposed to be nine.

KETAMINE: Cassadee, I think what he’s trying to say is that he is the boyfriend of the pregnant lady that squatted over the well, and when he found out that the Po-Po were onto him, you know, for human traffickin’, he just crawled up, you know where, and had his girlfriend rebirth him over the well so that he would never be found and ever since then, he’s been controlling the scheme remotely.

CASSADEE: How do yo-

ANTHONY: Correct! You’re one smart cookie. And young girl, by the way, I do have Roblox, but I seem to have forgotten my username.

CASSADEE: Darn.

ANTHONY: But, I can ask my son, Ryder! We share an account.

CASSADEE: Oh my god. Ryder’s your son?

ANTHONY: Yep. I needed extra hands, and sometimes it gets lonely in that well, so I decided to asexually reproduce and create him. His latest mission was to find some girl named Cassadee and lead her down to my well, but I haven’t heard any updates in a while.

CASSADEE: OH EM GEE!! YOU WERE GOING TO TAKE ME?

ANTHONY: Oh… you’re the girl?

CASSADEE: Um…. I guess.

ANTHONY: Oh ho ho ho! You’ve come to me yourself! I didn’t even need Ryder!

CASSADEE: Um yep! So… (scoots closer and takes his hand) Where to?

ANTHONY: Oh… I’m not taking you. You have a horrible sense of style and I find your voice to be incredibly irritating. I was thinking of selling you. I'm a trafficker, not a foster parent.

CASSADEE: WHAT??? OH MY GOD!!

ANTHONY: Your ride is here! (Ryder enters)

RYDER: Let’s go Cassadee. Sarah’s waiting in the car, and if we don’t take you to the buyer now, we’re gonna be late to our date.

CASSADEE: Sarah? Date? I KNEW SOMETHING WAS UP! You cheating, lying, little-! (He covers her mouth, ties her up, and takes her out of the room)

KETAMINE: Are you going to take me too Anthony?

ANTHONY: No. You smell too bad. Nobody will buy you.

KETAMINE: Oh. Thanks! (pause) You want some mac and cheese? It’s getting cold. ANTHONY:That sounds delightful!

THE END
```

---

## IC-0527: Emily's Post-Apocalyptic Book of Zombie Etiquette

- Title: Emily's Post-Apocalyptic Book of Zombie Etiquette
- Author (byline): Lauren Hance
- Work: Emily's Post-Apocalyptic Book of Zombie Etiquette
- Publisher: Mushroom Cloud Press
- Publication date as stated: September 1, 2021
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2282
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
EMILY’S POST-APOCALYPTIC BOOK FOR ZOMBIE ETIQUETTE

Emily's Post-Apocalyptic Book of Zombie Etiquette

__________________________

A play in ten minutes

By Lauren Hance

www.laurenhance.com

EMILY’S POST-APOCALYPTIC BOOK FOR ZOMBIE ETIQUETTE

SYNOPSIS Years after the break out o HN666N7 most humans have become zombies. In efforts to bring back the decorum of a more civilized society Emily has taken on the task of writing a new and revised version of the classic book Etiquette. Will the zombies take her advice or will natural instinct take over?

CAST OF CHARACTERS
EMILY, A Zombie. Her physical body resembles that of a zombie, but her dress and general
demeanor is clean, polished, and civilized.
ZOMBIE WOMAN 1
ZOMBIE WOMAN 2
ZOMBIE GINA
ZOMBIE CHUCK
ZOMBIE BAR MAN
ZOMBIE BAR WOMAN
ZOMBIE MAN
ZOMBIE WOMAN
ZOMBIE HOSTESS
HUMAN
ZOMBIE GUESTS 1-3
ZOMBIE GIRL
ZOMBIE MOM
ZOMBIE DAD
BILL

SETTING A Post-Apocalyptic world after the outbreak of the H666N7 virus that turned most humans into zombies. This world is now run by zombies and they are the norm. They are on their way to becoming a civilized society.

PRODUCTION NOTES The Zombies should move at a zombie like pace and with some kind of limp/lean/ailment(s) as if they have been injured in some capacity. At times they can speed up their pace, but their injuries should still be evident. Most of the time they are fighting their injury in the effort to become more civilized.

Most of the time, the zombies speak with a normal voice, not much grunting, growling or hissing, but it is acceptable to add these sounds in as you see fit, or when the script dictates.

Lines that may be altered per the performer's preference: Zombie Gina raids an H&M, another store may be used. Zombie Bar Man's pick-up line may be swapped for another bad pick up line.

EMILY’S POST-APOCALYPTIC BOOK FOR ZOMBIE ETIQUETTE

EMILY, a zombie, walks center stage. She is holding

a large book, titled Emily’s Post-Apocalyptic Book

for Zombie Etiquette. Her body is zombie like, yet

her dress and general appearance is clean and

civilized. She opens her book and begins to read

aloud, addressing the audience.

EMILY Arrgghh...

EMILY coughs and clears her throat, then when she

finally speaks, she speaks with clarity and decorum.

Dear Zombie Reader. The world we live in has changed so much since the breakout of H666N7. Some may say we are a less civilized society, yet I beg to differ. I believe with the correct guidance and a little effort, we can regain the general concern for others we once had. By the end of this book you will have a new appreciation of the values and manners of previous generations while being able to promote the best practices of today’s Zombie society. Being respectful and honest is more important than knowing which fork to use, or even knowing that you should use a fork. Because above all, manners are a general awareness of others. I hope that this book will become a trusted companion and guide wherever your journey takes you. Sincerely Yours, Emily.

EMILY turns the page and crosses away from

center.

Chapter 1- The Good Zombie Conversationalist. It is well advised to learn, at minimum, a few words. We all have a tendency towards aggression, but by learning some simple phrases your communication with others will soar and you will find yourself more relaxed and easy going.

Scene shifts to two ZOMBIE WOMEN. ZOMBIE

WOMAN 1 speaks with clarity. ZOMBIE WOMAN 2,

grunts through the scene.

ZOMBIE WOMAN 1 Grrreeetta. Good to see you.

ZOMBIE WOMAN 2 (Becoming aggressive) Grraahhhrraahhhggg!!!-

ZOMBIE WOMAN Hard day?

ZOMBIE WOMAN 2

EMILY’S POST-APOCALYPTIC BOOK FOR ZOMBIE ETIQUETTE

(More aggressive) Gggrrrahhhaafffaaa!!!-

ZOMBIE WOMAN 1 I’ve had days like that myself. Just the other week I wanted to rip the face off my mother-in-law, but I had to remind myself, it’s just a phase. So, remember Grrreeetta, it’s just a phase.

ZOMBIE WOMAN 2 (Yelling) My name isn’t Grrreeetta! Arrrgghhhh!!! It’s Maaaarrrr- Maaarrr- Mary!

ZOMBIE WOMAN 1 I am so sorry. Mary! Of course! Here I’ve been calling you Grrreeetta for months, my mistake. I know a really great speech therapist. Only if you’re interested.

Scene shifts to EMILY.

EMILY Chapter 4- Zombie Image and Grooming. While the world we live in, may at times, appear chaotic and run down, it does not mean we must reflect this. Caring how you look is one of the keys to developing good personal relationships. Try your best to not become lax about your appearance or personal hygiene, remnants of stale brains and flesh can become quite a turn off. Taking care of yourself, lets others know you care for and respect them.

Scene shifts to ZOMBIE GINA and ZOMBIE CHUCK.

ZOMBIE GINA Chuck! Is that you?

ZOMBIE CHUCK Gina? Good to see you!

ZOMBIE GINA I almost didn’t recognize you, Chuck. How the heck are ya?

ZOMBIE CHUCK Pretty good, pretty good. Hey, you’re lookin’ pretty good.

ZOMBIE GINA Oh, yea, I raided an H&M. Found a new jacket, this sequin top, some leather pants.

ZOMBIE CHUCK Well it’s done wonders for you, really.

ZOMBIE GINA

EMILY’S POST-APOCALYPTIC BOOK FOR ZOMBIE ETIQUETTE

I was a little sentimental about the sun dress. It was what I was wearing when the pandemic set in. But years of brains, and blood and all that, it just started to have a distinct aroma, and it had to go.

ZOMBIE CHUCK Well good for you.

ZOMBIE GINA I’ve gotta run. It’s been great to see you.

ZOMBIE GINA extends her hand to shake ZOMBIE

CHUCK’S hand, a moment of hesitation- he does

not have an arm.

EMILY Please note, shaking hands used to be a common and expected courtesy, but in today’s world this can become a sensitive subject. A nod of the head is perfectly acceptable.

ZOMBIE CHUCK Oh, I, uh.... I lost my arm just the other week.

ZOMBIE GINA I’m so sorry.

ZOMBIE CHUCK I was chasing a live one. He had an ax. It got a little ugly. Everything’s fine, but... (becoming emotional) well.... I’m glad you’re doing well.

Scene shifts to EMILY.

EMILY Chapter 7- Zombie Dating. Once upon a time, males were chivalrous; females were demure and coy. He would ask her out and she would graciously accept or decline. But in today’s world dating can be a daunting and confusing experience.

Scene shifts to ZOMBIE BAR MAN and ZOMBIE BAR

WOMAN 1, in a bar.

ZOMBIE BAR MAN If I had a nickel for every time I saw someone as beautiful as you, I’d have five cents.

ZOMBIE BAR WOMAN Arrrrgggghhhhh!!!

EMILY’S POST-APOCALYPTIC BOOK FOR ZOMBIE ETIQUETTE

ZOMBIE BAR WOMAN 1 attacks ZOMBIE BAR MAN

1, and basically eats him. Scene shifts to EMILY.

EMILY Bad pick up lines are still uncouth and can result in your demise. Aggression can be tricky, as it does not always mean the other party wants to eat you. It can also be an indication of interest. It is best to politely remove yourself from the situation, and try again later when a clear answer can be determined.

Scene shifts, ZOMBIE WOMAN is holding a human

leg and chewing on it. ZOMBIE MAN approaches.

ZOMBIE MAN I just wanted to say, the way you took down that human back there, it was just- Wow! You really know how to make a man’s heart stop. Literally and figuratively.

ZOMBIE WOMAN Argghhhh!

ZOMBIE MAN What I mean is- I was just wondering, if maybe sometime, you know, if you’re not too busy, if you would like to wander the streets with me?

ZOMBIE WOMAN Arrgh?

ZOMBIE MAN We could take a stroll down Main Street, swing by the park. That kind of thing. Maybe even pass by the human refuge and grab a bite to eat?

ZOMBIE WOMAN Agghhhhaaaa!!!

ZOMBIE MAN Or not. I mean if you prefer to chase food, we can absolutely do that.

ZOMBIE WOMAN Arrrgggghhhhhh!!!!

ZOMBIE MAN Is that a yes or a no?

ZOMBIE WOMAN AARRRGGGHHHHH!!!!-

EMILY’S POST-APOCALYPTIC BOOK FOR ZOMBIE ETIQUETTE

ZOMBIE MAN You know, I think I’ve caught you at a bad time.

ZOMBIE WOMAN ARRRHHHHH!!!-

ZOMBIE MAN I’m gonna let you finish your dinner there-

ZOMBIE WOMAN AGGGGHHHHH!!!!-

ZOMBIE MAN And uh, maybe we can pick up sometime later.

ZOMBIE MAN exits and ZOMBIE WOMAN

continues eating. Scene shifts to EMILY.

EMILY CHAPTER 15- Entertaining Zombies. Polite conversation used to be a dinner party starter. But in these times it is best to being with food, then move into conversation. Serving live food is always a great way to show respect to your guests, but be cautious because humans are cunning and quick, and could leave you in an embarrassing situation.

Scene shifts. ZOMBIE HOSTESS and her 3 ZOMBIE

GUESTS sit around a table that is draped in a cloth,

whimpers can be herd.

ZOMBIE HOSTESS I’ve prepared a male tonight. I hope that’s okay?

ZOMBIE HOSTESS removes the cloth to reveal a

man strapped down to a table. He begins squirming

and crying.

HUMAN No. No, please, please, no.

ZOMBIE GUEST 1 Fantastic!

ZOMBIE HOSTESS Shall we?

EMILY’S POST-APOCALYPTIC BOOK FOR ZOMBIE ETIQUETTE

HUMAN Please, please don’t eat me.

ZOMBIE HOSTESS & GUESTS ARGGHHHHAAAA!!!!

HUMAN Nooooooo.....

ZOMBIE HOSTESS Look at him squirm.

ZOMBIE GUEST 2 I know. It’s so cute.

The ZOMBIES turn their attention away from the

table long enough for the man to get loose and

quietly escape.

ZOMBIE GUEST 3 You know, I find the men have far more developed muscles, and when you take that first bite the blood just sprays right out, dousing you in a sweet and succulent sauce.

ZOMBIE HOSTESS That blood, it might be my favorite part of the whole meal. To be honest, I might prefer it to the brains.

ZOMBIE GUEST 3 Careful there, you’re almost starting to sound like a vampire.

ZOMBIE HOSTESS (laughing) We all know vampires aren’t real. (Looks back at the table) Oh!- Uh....

ZOMBIE GUEST 1 Where did he go?

ZOMBIE HOSTESS I’m not sure. I thought I had him down tight. I’ve got some day-old brains in the fridge I can pull out.

ZOMBIE GUEST 2 I’m on a special diet, only eating fresh food.

EMILY’S POST-APOCALYPTIC BOOK FOR ZOMBIE ETIQUETTE

ZOMBIE HOSTESS I never intended for our little gathering here to turn into a hunt, but he can’t be that far. If we start now, we can probably chase him down.

Scene shifts to EMILY.

EMILY Chapter 20- Zombie Family Life. At the dawn of this new age the definition of family drastically changed. While some still choose to keep a semblance of the traditional family, with a mother, a father and 2.5 children, others choose to live in herds. Family sizes, structure, and complexity are varied. And since adding to the family does not occur by procreation, but rather by transformation, everyone’s family appears different. But with all the diversity today’s families present, we all still share the same basic values of inclusion, acceptance, and the common goal of self-preservation.

Scene shifts, ZOMBIE GIRL is holding the hand of

BILL, he is petrified as they stand before ZOMBIE

MOM and ZOMBIE DAD.

ZOMBIE GIRL Mom, Dad, I want you to meet Bill, my boyfriend.

ZOMBIE MOM & ZOMBIE DAD Aaarrrgghhhh!!!

ZOMBIE GIRL Stop, you’re scaring him.

BILL Please don’t eat me. Please!

ZOMBIE MOM You brought home a human. How could you?

ZOMBIE GIRL I love him!

ZOMBIE MOM Oh, you love him? Is it for his brains or for his body, tell me that!

ZOMBIE GIRL Both mom, both. He’s really great if you just give him a chance.

ZOMBIE DAD

EMILY’S POST-APOCALYPTIC BOOK FOR ZOMBIE ETIQUETTE

Do you remember your brother? Huh? No. That’s right! He brought home a female, and she ended up chopping off his head. We’re lucky we escaped.

ZOMBIE GIRL But Bill isn’t like that. Are you Bill?

ZOMBIE DAD (To Bill) Are you?! (Aggressively) Arrrggghhh!!!

BILL No. No. I’m not like that. I have no inappropriate intensions with your daughter. Sir.

ZOMBIE DAD Then what are your intensions?

BILL Nothing. I just- She just brought me here. Said it was safe.

ZOMBIE GIRL It is safe. Right mom? Right dad?

ZOMBIE MOM Of course, honey. (To ZOMBIE DAD) He looks strong.

ZOMBIE DAD Muscular.

ZOMBIE MOM Fast.

ZOMBIE DAD Smart.

ZOMBIE MOM Agile.

ZOMBIE MAN That could come in handy.

ZOMBIE GIRL Mom? Dad? What are you talking about?

ZOMBIE DAD Honey, you’ve done great.

EMILY’S POST-APOCALYPTIC BOOK FOR ZOMBIE ETIQUETTE

ZOMBIE MOM He’s going to make a nice addition to the family.

ZOMBIE DAD Ever since your brother lost his head, I’ve wanted another boy around.

ZOMBIE MOM & ZOMBIE DAD (They lunge towards BILL) AAARRRGGGHHHH!!!!!

ZOMBIE GIRL No! I like him the way he is!

ZOMBIE MOM and DAD take down BILL. ZOMBIE

GIRL begins crying.

Please stop! Mom! Dad! No! He was so soft and so warm.

ZOMBIE DAD You had to know this was going to happen.

ZOMBIE GIRL But I just thought we could be different, you know. I know, I know, call me a dreamer or possibly even a radical peace maker.

ZOMBIE DAD Not in this family.

ZOMBIE GIRL I guess not. (Beat) Not the face mom!

ZOMBIE MOM Well dear, we can’t all be perfect. Don’t worry, he’s going to fit in just fine.

Scene shifts to EMILY.

EMILY My dear reader, thank you for trusting not just my advice, but considering me as your companion and guide. And remember, while self-preservation is of the utmost importance in these trying times, politeness and manners never go out of style.

THE END
```

---

## IC-0528: In A Jam

- Title: In A Jam
- Author (byline): Matt Mills
- Work: In A Jam
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1554
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
(Alex, an average-looking teen, sits in a bus, talking on the phone.)

Alex: Yeah I’m taking a bus out there now, it should only be… Thirty more minutes? Maybe an hour in bus-time. Don’t worry, I’ll be there, shooting space-zombies with you in no time. ...I don’t know, I think it’s the last stop on the route, everyone else got off already. It’s just me just sitting here alone, talking like a weirdo in the middle of nowhere. Yeah, duh, alone besides the bus driver--

(The bus stops suddenly.)

Alex: Whoa! Um, excuse me miss? Is something wrong?
Driver: Last stop!
Alex: A-ha, good one. (no response) Um, the last stop is supposed to be Alfredville.
Driver: Yeah maybe on the OLD ROUTE. It changed.
Alex: But I literally looked it up this morning--
Driver: Look, you don’t have to go home but you can’t stay on this bus! (opens door) Now move
it or lose it!
Alex: Uh, I think even if I move it I will lose it. This looks like the middle of nowhere--
Driver: NOW!!!

(The driver grabs Alex, tosses them off the bus. They collect themselves, wiping away dust as the bus drives off.)

Alex: Wow, well that was rude. (looking at his phone) Where even am I? ...Not in Uber-territory apparently. (sees something) What… is. Is that a festival? That’s not a mirage, is it? I’ve heard about those. On the internet.

(Alex walks towards a contained but sizeable little festival jutting out of the desert, a collection of booths with a big grand stage in the middle and a huge, elegant sign marking the ‘Harrisontownville 134th Annual Jam-boree’.)

Alex: (reading) The 134th Annual Harrisontownville Jam-boree?

(Alex approaches the nearest booth, worked by a focus-crazed human named Jimble.)
Jimble: (handing out jars) Here’s two blueberry for ya, one strawberry...
Alex: Excuse me, do you know where the nearest--
Jimble: DON’T TALK TO ME UNLESS YOU’RE BUYING SOMETHING, THIS IS PRIME JAM-
TIME!
Alex: Oh, I’m sorry, I didn’t realize that it was jam-time. I was just hoping you could help me find
a way home, I got abandoned--
Jimble: Help you? Why would I help you? In the middle of the 134th Annual Harrisontownville
Jam-boree?!
Alex: The… the what?
Jimble: Are you dense? Or deaf? Or both?! The 134th Annual Harrisontownville Jam-boree!
Alex: Yeah, saying it again isn’t going to make me understand. I’ve just never heard of--
Jimble: You… pfft. You. You have never heard of the Harrisontownville Jam-boree?
Alex: Mm nope. Never.
Jimble: Have you heard of anything?
Alex: Yes, I’ve heard of lots of things.
Jimble: Wow. Where did you just get off the bus from.
Alex. Uh. Sacramento?
Jimble: That wasn’t an actual question. Now leave me alone! I’ve gotta sell twice as fast now if I
want any shot at winning the jam-crown.
Alex: Sorry, I’m just trying not to die in the desert, so I thought you might help.
Jimble: Well I need some help! Beating Sandra in this life and death competition.
Alex: Selling jelly is a life and death competition?
Jimble: DOES IT LOOK LIKE I’M JUST USING FRUIT JUICE?! This is jam, ya dingus. We’re
not afraid of seeds here. We crush that fruit and make the most delicious nectar the gods have
ever had. Now leave me alone. Go bother Sandra if you want help.
Alex: No need to raise your voice, but okay. I’ll try Sandra, thanks.
Jimble: YOU’RE WELCOME!

(Alex walks over to the next booth and approaches the beauty-pageant star that is Sandra,
who’s handing jars to customers with a big smile.)
Alex: Uh, hi. Sandra?
Sandra: (to Alex) I’ll be with you in just a moment.

Alex: Oh, cool. Thanks. (waits) It’s just that I’ve been stranded here and that person named
Jimble said--
Sandra: Jimble said to bother me? He said that he’d help you if you just distracted me for a
while to get my sales down? Jimble wants to use you for sabotage? Jimble said that raspberry
is the easiest jam to make??
Alex: He said those first three things, yeah basically.
Sandra: Let me tell you something, stranger.
Alex: Alex.
Sandra: Sure. I was born with a silver spoon in my mouth. Do you know what that spoon was
filled with?
Alex: Uh, jelly?
Sandra: JAM! ...It was filled with jam. I was a very popular student. Prom queen. I got into
Harvard, Yale, University of Phoenix Online. But none of it was enough. The only thing I had a
taste for?
Alex: Jam?
Sandra: I was gonna say that.
Alex: I’m sorry.
Sandra: Now you’ve ruined my whole train of thought, it was a whole speech...
Alex: Look, could you just help me? I’m supposed to be at my brother’s place in twenty minutes-
-
Sandra: Yeah and my husband wants me to help you so I lose.
Alex: Wait. Jimble is your husband?
Sandra: Duh. I’ve been married to Jimble for twelve great, jam-filled years. He’s the light of my
life. But on this day… he is my mortal enemy.
Alex: That doesn’t sound healthy.
Sandra: Yeah, well. Neither is jam. (to a customer) Oh, no miss--it’s full of antioxidants and it’s
so good for your bones I brush my teeth with it!
Alex: ...So are you going to help me or not?
Sandra: Not today, Satan.
Alex: What?
Sandra: Sorry, too far. I’m just too busy. Maybe Gladiator will help you.
Alex: There’s a person here named Gladiator?
Sandra: Oh my god shut up and leave me alone! Sorry.
Alex: Ouch.

Sandra: Too far again.
Alex: Yeah.
Sandra:But seriously go away. Get out of my sight. NOW!
Alex: Wow, okay. Sorry.

(A bit bewildered, Alex walks over to the hulking Gladiator’s stand.) Alex: Hi, uh. Gladiator? Gladiator: Good day, smaller person! Could I interest you in one of our jams? You seem like a boysenberry human to me… Alex: Uh, no actually. Thanks. I just got stranded here and no one is helping me. They just wanna sell their jams. Gladiator: Ah yes. That is the mindset of inferior jam creators. But you have come to the god of jams. Alex: Oh. Okay, cool-- Gladiator: The jam-god. Alex: Right. Gladiator: I have won twelve Harrisontownville Annual Jam-boree’s in a row. I have not been defeated since my biceps were under twenty inches wide. And that was a very long time ago. (shaking Alex’s hand) The name is Gladiator. Alex: It’s nice to meet you, Gladiator. Hey, can I ask you something? Gladiator: Shoot. Not literally of course, because your bullet will be stopped by my pectoral muscles. Don’t want you wasting bullets now. Alex: Why is everyone here so obsessed with jam? I mean. It almost feels unreal. A random jam festival in the middle of the desert. There are customers, but no cars, or houses, or… I keep wondering if this is like. Reality, or maybe I just died in that bus and this is some sort of afterlife purgatory? Is this hell? Was I a bad person that deserves to spend eternity going from jam booth to jam booth trying to find a ride? Is this what the rest of eternity will be?! (phone rings/vibrates) Oh thank god. Hey Jack. No, I’m still alive, I guess. I’m just still trying to find a way out of here... Gladiator: Fret no more, tiny Alex. I will gladly help you. Alex: Wait, really? That’s awesome. (to phone) Okay, I’m about to get out of here, I’ll see you soon. (hangs up) So, I just either need a ride to the nearest town, or if you know someone who can-- Gladiator: Before we ship you out of here, you appear famished.

Alex: Well, I am a bit hungry, but I’d really rather just--
Gladiator: Here. Try some boysenberry jam. I’ve spread it atop a crostini with brie, as a flavor
and textural counterpoint to my award-winning jam.
Alex: Really, I just want to get out of this place--
Gladiator: This is your way out, Alex.
Alex: What?
Gladiator: I will only help you if you try my jam.
Alex: Ha, good one. (off Gladiator’s stare) You’re joking, right?
Gladiator: I never joke when it comes to jam.
Alex: ...Okay, sure that’s fine. As long as you promise to help me.
Gladiator: I swear on my deltoids that I will help you. And I never lie when it comes to my
deltoids.
Alex: Hm. Okay. (takes a bite) Oh. Oh that is good.
Gladiator: Mmhmm. Yesss.
Alex: This… this is really really good.
Gladiator: Yes it is.
Alex: Wow. Like. I don’t think I’ve ever eaten anything this good.
Gladiator: You haven’t.
Alex: I think I’m starting to see why you guys are all so obsessed with jams!
Gladiator: You are.
Alex: Mmm. Can I have some more?
Gladiator: I’m sorry, I can only offer one free sample.
Alex: What? No, come on, Glad, you’ve got to! That stupid bus took the last of my money and…
I need my jam, man!
Gladiator: I know you do. Now if you want more jam you must create it yourself.
Alex: ...You’re joking, right?
Gladiator: What did I say about joking about jam?
Alex: No… no. No, no no no no no!!! I died, didn’t I? This is my punishment?!
Gladiator: If you died this would be heaven, so no need to freak out…
Alex: This… what do I do with my life now? I can’t go back to the real world now that I’ve tasted
this jam. Food will never be the same. You knew this and yet you still did it to me!
Gladiator: As was done to all of us at one point.
Alex: I have to leave. I have to meet my brother. But. But I can’t…
Gladiator: And now you understand.

Alex: Oh god. Oh no...

(Flash forward to next year--an elegant host speaks into the mic on stage.) Host: And the winner of the Harrisontownville 135th Annual Jam-boree is… Wow, we have a new champion, folks! Congratulations to your new Jam-God, Alex Mckinney! Alex: Yes! Yes! What’s up now, Gladiator?! Woo! Woo! Man, I’m so glad I abandoned my old life for this. Totally worth it.
```

---

## IC-0529: The Mulligan

- Title: The Mulligan
- Author (byline): AJ Nienow & Brian Sams
- Work: The Mulligan
- Publisher: Mushroom Cloud Press
- Publication date as stated: August 15, 2024
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1417
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
Cast of Characters:
Billy Reynolds - A good kid that just can’t seem to stop trying too hard to be liked.
Denny - Billy’s best friend
Mr. Mulligan - A science teacher and amateur inventor who works at Billy’s school
Kyle - A popular bully that verbally abuses Billy whenever possible (frat dude)
Gavin - Kyle’s sidekick
Kelly - Billy’s crush
--

Billy: Okay, Denny, this ends today! If Kyle makes fun of me again, I’m going to show him Billy
Reynolds is nobody’s joke!
Denny: I don’t know Billy, I think it would be smarter to just ignore him.
Billy: And let him get away with it? No way. It's time for the new Billy! I’m going to be the
funniest, most popular guy in the school. Girls love a guy with a sense of humor. All the experts
agree on that.
Denny: The experts?
Billy: Tiktok and Reddit.
Denny: Oh, that’s not… Ugh…Oh, no…There's Kyle.
Kyle: Hey, Reynolds, nice shirt. Did your mommy buy it for you?
Billy: Oh, yeah? Well, I got news for you! It was on sale, so she got one for my dad, too. Oh, no.
Kyle: Oh my God! You and your dad go twinsies! That’s adorable! Did you hear that Gavin?
Gavin: Ooh. The self-burn! Brutal!
Denny: Let’s go!
Billy: Oh yeah? Oh yeah. You know Kyle, you’re like, um, ah…a BUTT!
Mr. Mulligan: Kyle, Billy, that’s enough.
Denny: Oh no, it’s the science teacher, Mr. Mulligan!

Mr. Mulligan: Go to class, Kyle. Billy, in my office.
Billy: Yes, Mr. McGuffin.
Mr. Mulligan: It’s Mulligan!
Billy: Yes, Mr. Mulligan. See you, Denny. Why can’t I do anything right?
Mr. Mulligan: Billy, why are you yelling butt in the hallway? This isn’t a Walmart, son.
Billy: It’s just that Kyle is constantly roasting me and I can never think of a comeback until 30
seconds too late. It’s like, if I just got a second chance, I could do it, you know?
Mr. Mulligan: Billy, I have something that might help, but it has to be a complete and total secret,
do you understand?
Billy: Oh, boy Mr. Mulligan, if this is some kind of Breaking Bad scenario, I say no to drugs.
Mr. Mulligan: It’s not drugs, Billy. (Aside as he gets the Mulligan out of a cabinet or drawer)
Work in a public school they said, make a difference they said, the pay’s not all that bad they
said...Here. (Handing Billy the Mulligan)
Billy: A watch?
Mr. Mulligan: It’s more than a watch, Billy. I call it the Mulligan.
Billy: The Mulligan?
Mr. Mulligan: The Mulligan.
Billy: Okay. Because it looks like a genuine vintage Hannah Montana Kids Pink Heart Gemstone
Watch.
Mr. Mulligan: This is a custom, compact, localized time travel device.
Billy: No way.
Mr. Mulligan: Ohhh…Yes way. You just tap the bezel to travel back 5 seconds in time. But listen
carefully, Billy, don’t ever, ever, exceed 30 seconds!
Billy: Why not?

Mr. Mulligan: Spaghettification. The butterfly effect. Parallel universes…You could be lost in
space and time forever.
Billy: Whoa.
(Billy hits bezel)
(Time travel sound effect)
Mr. Mulligan: You could be lost in space and time forever.
Billy: Jiminy Freakin’ Christmas!!
Mr. Mulligan: You just did it didn’t you? Billy, you need to be careful, there’s more…
(Billy hits the bezel)
Mr. Mulligan: …space and time…
(Billy hits the bezel)
Mr. Mulligan: It’s not drugs, Billy.
(Billy hits the bezel)
Mr. Mulligan: …this isn't a Walmart, son.
(Billy hits the bezel)
Kyle: …Nice shirt, did your mommy buy it for you?
Billy: (Clears his throat) Yeah, well, I used to have a shirt like yours, Kyle, but then my dad got a
job. Boom! Roasted!
Gavin: Oh snap! Kyle, you got burned! Nice one, Billy!
Denny: Yeah, nice one, Billy. Where did that come from?
Billy: I told you it's the new Billy! (Aside) The Mulligan!
Transition
Billy: Hey Kelly! Hold up, um, I've got a timed survey I have to do for… social studies.

Kelly: Okay…
Billy: And go. What’s your favorite restaurant?
Kelly: Guiseppe’s?
Billy: Favorite food?
Kelly: Manicotti?
Billy: Dream date activity?
Kelly: Umm, a walk in the park, maybe?
Billy: (Looks at watch, is in a hurry) Ah, what night this week do you have absolutely no
commitments?
Kelly: Thursday, I guess.
Billy: Cool! (Presses the bezel - Transition) Hey, Kelly! Thursday, Guissepe’s, manicotti, and
then a walk in the park, what do you say?
Kelly: Are you asking me out?
Billy: I uhhhhh.
(Billy hits bezel)
Kelly: Are you asking me out?
Billy: Yes, I am.
Kelly: Well, sure, okay.
Billy: Okay? Okay! The Mulligan!
Basketball announcer: It's the final shot in the game folks, and even though he’s only been
playing basketball for, wait is this right? Only been playing for three weeks, it all lands on Billy
Reynolds.
Billy: Ok, here we go again. (Misses) Dang it.
(Billy hits the bezel)

Basketball announcer: …it all lands on Billy Reynolds.
Billy: (shoots a gain and misses) Oh, come on!
(Billy hits the bezel)
Basketball announcer: …lands on Billy Reynolds.
Billy: (shoots a gain and misses) YOU GOTTA BE KIDDING ME!
(Billy hits the bezel)
Basketball announcer: Billy Reynolds.
Billy: 63rd time's the charm! (Shoots and makes it) There we go! I did it. I won! The Mulligan!
Basketball announcer: Billy Reynolds in his rookie debut with 96 points and 100% accuracy!
Zero assists, but who needs to be a team player when you’re Billy Freakin’ Reynolds!
Transition
Denny: Look out, Billy, it's Kyle.
Billy: So what? Hey Kyle!
Kyle: Sup, Billy, nice game! Coming to my party tonight?
Gavin: Yeah! We told everyone that you would be there.
Billy: Maybe, boys, maybe. I’ll see what I can do.
Denny: Aw jeez, I gotta go, Billy.
Billy: (Very dismissive) Yeah, okay, bye.
Kyle: You can bring your little buddy if you want.
Billy: Him? Nah. We just…have some classes together.
Kyle: Okay, that's cool dude, cause you realize you have a lot more options now.
Transition
Billy: Hey, Denny, listen, you could be popular, like me. I can help you, but it would have to be a
complete and total secret.
Denny: No thanks.
Billy: What?
Denny: Did you dump Kelly?
Billy: Well, I mean…
Denny: You did. You really liked her. And I think she liked you too, even before all this…
Billy: This what? I’ve got more options now. What do you want me to say?
Denny: In the last month… you've completely changed. You’re the star player on the basketball
team, the girls are all over you, and now everyone’s wearing Hannah Montana watches…
because of you!
Billy: I know, right? No more Screw Up Billy, Can’t Make a Comeback Billy, You Just Missed
Your Chance Billy!
Denny: Yeah. I suppose. But…you're not yourself anymore.
Billy: Are you serious? Because I'm not a screw up? You liked me better when I was a loser, a
failure? When I was…like.. LIKE…
Denny: Like me? You weren't a failure. You were my friend, my best friend, and now you don’t
even care…I just wish I had the old Billy back. I guess I’ll see you around.
Billy: Fine! What an idiot. My life is perfect. I don’t need you, Denny! I have everything -
EVERYTHING I ever wanted! If that's true, why does it feel so pointless? But, hey, look at what
I’ve become! By changing who I am, again and again, until I’m perfect? To impress people I
don't even like? Denny’s not an idiot. I am. I could have done anything, but instead I ruined
everything… Wait! I can go back, I have to go back!
(Billy grabs the Mulligan and clamps down on it, hard.)
Sorry, Mr. Mulligan. Whoooooaaaa!
Abraham Lincoln: Four score and seven years ago…
Billy: Ohhh. Too far. Looks like I’m going to have to go back to go forward! That makes total
sense, right! Bzsoo! Gaaaa!

Billy: (Steps on something) Uh oh! Whew, only a butterfly. Where am I? Hello?
TRex: Rrrrowr.
Billy: Aghh, a TRex!
TRex: Rrrowr!
Billy: Ahhhh!
TRex: Raaaar!
Billy: (Grabs Mulligan) Ahhhh!
Huge explosion
Billy: Whoa! The Big Bang! Looks like I'm going around the horn!
There’s Denny, this is where I get off! (Lets go of the Mulligan and whirls into regular time.)
Kyle: Hey Reynolds, nice shirt. Did your mommy buy it for you?
Billy: (Slams locker. Ready to tell off Kyle, but stops himself) Let's go, Denny. We don't want to
be late for class.
Denny: Really? You’re actually taking my advice?
Billy: Absolutely. You’re my best friend, right?
Denny: Yeah... Okay! What’s with the pink watch?
Billy: It’s the… It’s nothing. Well, this is it, farewell, sweet, sweet Hannah. Just like you, I can no
longer live a double life. It’s time to be Miley. Hey, Mr Mulligan! Here. (Hands him the Mulligan.)
Mr. Mulligan: The name’s McGuffin. What’s this?
Billy: It’s the Mulligan!
Mr. Mulligan: The Mulligan?
Billy: The Mulligan!

Mr. Mulligan: Never seen it before. You can be honest with me Billy, is this some kind of drug thing? Billy: No, it’s not drugs…parallel universe...eh, close enough...I wonder what this would go for on eBay? Mr. Mulligan: Right on, now, get to class.
```

---

## IC-0530: The Organ Ordeal

- Title: The Organ Ordeal
- Author (byline): Parsa Ansari
- Work: The Organ Ordeal
- Publisher: Mushroom Cloud Press
- Publication date as stated: August 15, 2024
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: JOSH, BRAIN, HEART, LUNG, STOMACH, FISH & CHIPS, BUTTER CHICKEN, KABAB
- Teaser before the introduction: No
- Spoken words (computed): 1398
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

# Name Characteristics

1 Josh High-pitched teen who hasn’t gone through puberty yet

2 Brain Leader, mature, keeping everyone organized and on track

3 Heart Always pumping, symbolic of hard worker

4 Lung Always breathing, relaxed, “surfer dude”, eyes always half closed

5 Stomach The scapegoat; big, plump, and kind, but sensitive and soft on the inside; can’t get things right and eats A LOT

6 Fish & Chips Innocent, but feels that no one likes him and always blame him since he smells bad

7 Butter Chicken Flirtatious, dreamy guy; thinks highly of himself

8 Kabab Koobideh Typical Persian; thinks everyone knows him and that he’s everyone’s friend; views himself as #1 in everything Voice Role

Squeaky High Setting Voice

My Voice Lead organ

Complaining New Organ York/Jersey voice

Chill, Surfer Organ Dude, Relaxed Voice

Derpy Voice Organ

Weird English Food 1 Accent (Suspect)

Indian Accent Food 2 (Suspect)

Persian Accent Food Poisoning (Villain)

Script:

JOSH: (grabs plate and starts shaking excitedly) Oh! My! Gosh! They have EVERYTHING in this buffet! Fish & chips, butter chicken, steak! I love a good buffet! (prances over to a seat, sits, and sniffs food) Something smells strange. Oh well. What's the worst that can happen to me? (takes two big bites of food, chews loudly, and swallows) Mmm. Soooo good. (freeze for a couple seconds)

BRAIN: (clap three times and grab clipboard) Alright organs, listen up! It's Josh’s brain here and I have some very important announcements for you all today. I am so disappointed to say that our productivity has decreased by seven percent in the past month so I’m gonna need to know what's up. Heart, do you have anything that you would like to say?

HEART: (pumping crazy) I’m tired, man! I’ve been pumping nonstop for fifteen years; can I just take a five minute break!

BRAIN: No, heart. You can’t take a five-minute break.

HEART: But why??

BRAIN: Because Josh will die! Uhhh, lung, what’s up with you?

LUNG: (breathes deeply) Dude, I’m tired too. Fifteen years of (inhales dramatically, exhales) I just want some fresh air to breathe.

BRAIN: Ok guys, I know we’re tired and we want to take breaks, but if you don’t keep it together there will be some serious consequences. Alright stomach, Josh has gained five pounds in the past two weeks. What's up?

STOMACH: (in the middle of eating something and with a full mouth) I can’t help it!!!

BRAIN: You’re the stomach! Control it, ok?!

STOMACH: (about to cry) Why does everyone always get mad at me!!

HEART: Because you ruin everything.

STOMACH: (still “about to cry” voice) No I don’t!

LUNG: Uhhh, yeah you do. Remember that one time when you accidentally ate all the white blood cells because you said they looked like cookies.

STOMACH: But they did!!

HEART: Or that other time when you were too busy eating Taco Bell, so you let the stomach flu get in.

STOMACH: It was Taco Tuesday!!

BRAIN: Hey! Guys, give stomach a break. He’s already got enough on his plate.

LUNG: You can say that again.

BRAIN: Guys! Oh wait, I’m getting a message from nerve. (receives messages from nerve in earpiece then looks shocked) Guys…...JOSH HAS FOOD POISONING!

It has been said that you are what you eat. Well good thing I just ate a state champion right before this round (creepy smile at camera). Anyway, Josh’s organs panic when they find out he has food poisoning. And although teamwork is just what they lack most, they are going to have to work together to defeat it. The Organ Ordeal, an original.

STOMACH: (stupid grunts) Josh has food poisoning!!

HEART: (pumping intensified) Not again!

LUNG: Don’t let stomach handle it again. Remember last time?

HEART: How can we forget? Stomach ruined the entire thing.

BRAIN: Hey! Guys, leave stomach alone. He’s got bigger fish to fry.

HEART: Yeah, I bet.

BRAIN: Guys. Last time it wasn’t stomach’s fault. Last time we were unsuccessful because we didn’t work as a team. If we work together, the food poisoning will stand no chance, alright? Now hurry, get to your places. We don’t have that much time. (on earpiece with nerve) Nerve, I’m gonna need you to gather all the foods that entered the body in the past twenty-four hours and put them in my office. I’m heading there right now. I’ll meet them there in a second. (goes to office and starts working) Why won’t this boy reach puberty already he’s 15 for heaven’s sake. (Three knocks on door) Come in. (pause) Ah, you must be the suspects. Take a seat.

FISH & CHIPS: Suspects?! Suspects of what?!

BRAIN: Well, there’s been a case of food poisoning, and we know it’s one of you guys.

BUTTER CHICKEN: Food poisoning? (evil laugh) It can’t be me. I’m always made with the freshest of ingredients.

BRAIN: Well, we know it’s one of you guys and we’re going to ask some questions to find out. (pulls out clipboard) If you don’t mind, I will also be taking some notes as well. So first, introduce yourselves.

KABAB: (offended) You don’t know me? I’m the kabab koobideh. Number 1 food in the whole world. You really don’t know me?

BUTTER CHICKEN: I’m the butter chicken. 50% butter. 50% chicken. 100% hot.

FISH & CHIPS: And I’m just the poor old fish and chips. Everyone always blames the fish & chips. Is it my look? Is it my smell? What is it?!

BRAIN: (writing on clipboard) Ok. Where were you guys on Sunday at noon?

BUTTER CHICKEN: Ahh Sunday was a great day for me. I just woke up, and I looked across the buffet to see the most beautiful piece of bread I have ever seen staring right back at me. Her name---was Naan. Her crispy, golden, buttery skin; so soft, so warm. Then I winked at her. Then she winked at me. And then I said, “What is a fine piece of bread like you doing on this lovely night?” And she was about to answer, but then this stupid boy had to put me onto his plate and take me away.

BRAIN: (more weirded out) Did you see anything suspicious happening on Sunday at noon?

KABAB: The only suspicious thing I saw was that no one put me on their plate for two hours! I’m the kabab koobideh! I’m the best food in the whole-

BRAIN: Yes, we know--the whole buffet.

KABAB: Are you kidding me? The whole buffet? The whole WORLD! It seems like anyone can be a brain these days.

BRAIN: (more weirded out) Alright, fish and chips--you’re awfully quiet.

FISH & CHIPS: Because nobody cares about the fish & chips, I’m just the old thing stinking up the place. Mummy was always right about us… (starts crying)

BRAIN: (frustrated) No, don’t cry! Ugh! We’re getting nowhere with this interrogation.

KABAB: Bro, I already told you I don’t have food poisoning. I’m the kabab koobideh! What else do you want, man?

BRAIN: Alright. We’re done. Follow me. Attention all organs, gather around. Unfortunately, I have absolutely no idea who the food poisoning is.

HEART: Aw man! Didn’t they give you some kind of clue during the interrogation?

BRAIN: I wish, heart, but no, they are actually so annoying. They managed to get on all 86 billion of my nerves.

KABAB: (deep sigh) Oh my god, you never listen. I don’t have food poisoning. I’m the kabab koobideh! I’m made fresh every day!

LUNG: (mid-inhale) Wait. Dude, did you just say that you’re made fresh every day?

KABAB: Uhh, yeah.

LUNG: Well, that's a lie. No food is made every day at the Ethnic Buffet.

HEART: (pumping but then comes to realization) Oh yeah that’s right. Brain, use your memory to see what days the kabab is there.

BRAIN: Alright I guess I can try. (closes eyes and activates Memory) Ok, Sunday at noon. Oh, the kabab is there on Tuesdays and Thursdays.

LUNG: Tuesdays and Thursdays! Josh went to the buffet on Sunday!

HEART: Oh yeah that’s true. And now that I’m thinking about it, Josh never said “kabab” when he was grabbing his food. He said steak!

BRAIN: (still in Memory) Heart’s right. Kabab must have been misplaced.

STOMACH: So, the worker who took out the kababs never took him away because he was in the steaks section! And then he was left out for three days and became moldy. But then later on Sunday, Josh ate him. Which means that the Kabab, is the food poisoning!!!

BRAIN: (long pause) Wow stomach!! You figured it out!

KABAB: Alright alright you got me. I never expected you guys to find out. (dramatically extends arm for them to take him away) Just take me away already.

BRAIN: Stomach, would you like to do the honors?

STOMACH: You bet! Kabab, it’s time you go home. (walks over to kabab to take him away but then kabab pulls out a knife and holds stomach hostage)

KABAB: Aha! Nobody move! If anyone comes close, I will kill this stomach in less than a second.

BRAIN: Stomach! No!

KABAB: Aha, nobody saw that coming. (SUPER proud of himself) I am so good.

HEART: What are we gonna do??

BRAIN: Uhh, lung, beat this guy up.

KABAB: If anyone moves, I will slice this fatso’s head off in the blink of an eye.

STOMACH: (super angry and offended) Fatso? NOBODY calls ME fatso. (punches kabab in groin area extremely hard)

KABAB: (in extreme pain) Ahhh!!! (grunts in pain) Good job. I should have seen that one coming.

BRAIN: (shocked at first, blinks eyes a couple times) Yeah, stomach!

HEART: Nice job stomach!

LUNG: Dude, you did it!

KABAB: (in pain) Just let me go already, (super dramatically) let me be free so I can DIEEEEEE in the DIEEEEE-gestive system.

BRAIN: Sorry kabab, but you’re going out right where you came from. (snaps fingers) Stomach!

STOMACH: (nods) On it, brain! (grabs kabab) Kabab, it’s time that you go home. (throws him up high)

JOSH: (immediately cuts to throws up) Bleghh. Gross. (turns around) Huh? I don’t remember eating corn.
```

---

## IC-0531: The Perfect Son

- Title: The Perfect Son
- Author (byline): Elijah Sams & Brian Sams
- Work: The Perfect Son
- Publisher: Mushroom Cloud Press
- Publication date as stated: August 15, 2024
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MS, T, C, D, V, H, J, BA, P, CM, M
- Teaser before the introduction: No
- Spoken words (computed): 1473
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

MS: Mad Scientist. A good guy, raised wrong.

T: His project/son.

C: Chad/Igor. A bro.

D: Dmitri, Russian mad scientist. Competes with MS

V: Dmitri’s daughter. Wants to act. Shy?

H: Hans. Bavarian mad scientist. Underdog complex.

J: Jaeger. Hans’s robot son. Likes poetry.

BA: Blake Allenson

P: Principal Brown

CM: Coach Manosfuertes. Spanish soccer coach forced to coach football.

MS: (Moving around the room, frantically adjusting apparatus) Soon I will know if I have succeeded in my quest to create a teenage son! I will finally know once and for all whether I have created a primarily nocturnal, disorganized, remorseless eating machine…or if I have failed. Igor, throw the switch!

C: Bra, I told you, my name is Chad, bro.

MS: Do you want to go back where I found you, Igor? Working the fragrance counter at a Hollister?

C: Fine, dude, I’ll throw your freakin’ switch, bra.

T: (Groans, rolls over, etc)

MS: It’s alive!

T: (Groans again.)

MS: I said “It’s alive!“ Wake up!

T: Seriously? It’s barely daylight.

MS: It’s 3 pm.

T: Wait, how did I get here? Where did I come from?

MS: Ah, the birds and the bees! How I’ve longed to have this conversation… However, it totally doesn’t apply. Due to my limited dating options as a mad scientist, my only chance at an offspring was to create you from the DNA of hundreds of the most accomplished people in the world and upload the entire internet into your brain, thus creating the Perfect Son!

T: I’ve got the entire internet in here?

MS: Well, not really. Like 3/8ths. I left out the porn and anything with (current pop culture topic - i.e the Kardashians, etc.). There wasn’t that much left. Intro: You’ve heard about helicopter parents, and even bulldozer parents; parents that do everything they can to ensure that their kids turn out perfect, yet sometimes those kids rebel and become complete trainwrecks. Meanwhile, other parents do next to nothing and produce model citizens. Raising kids is guesswork, constant adjustments, and damage control. It’s an art, not a science. But what if it didn’t have to be? The Perfect Son.

MS: There’s no time to waste, school starts in a few days and we have to get you signed up for everything! You’ll be the best athlete, scholar and artist in the country!

T: Really? I’m not sure I want to be “The Best”

MS: And waste your life? No, no, no. I won’t fail you the way my father failed me. Locked away in his lab while I slaved away in the brain fields of our organ farm.

T: You did what where?

MS: I said the grain fields of our organic farm. Never reaching my full potential, forced to be a mad scientist when I always dreamed of being a frontrunner for the Republican Party Presidential nomination.

T: Actually, that seems pretty doable right now. Look, Dad, I really don’t see how I’m going to do all these activities, I mean I show up out of nowhere…

MS: You already know how to do everything! Sports? No problem! Music? Easy! Academics? Piece of cake! The level of cheating I’ve done here makes Lance Armstrong look like a boyscout! Besides, I made some considerable donations at the last bake sale! They owe me!

T: OK, great. Dad, here’s the deal. I don’t want to sign up for these activities and…

MS: …and you don’t see how I can make you? Haha! That’s where you’re wrong! I built in a little special something… The Parental Guiltinator 2000! A couple little tweaks of the joysticks, and… (Using Xbox style controls, takes control of T’s body.)

T: What the? Dad!

MS: (Executes some 80s breakdancing type robot moves…) I’m doing this because I love you.

T: Stop doing that and I’ll go!

MS: Excellent! We’ll take my transitionator! My driving license is suspended. TRANSITION

MS: And here we are… What should you sign up for first? A sport? Yearbook? Your college applications are going to be perfect, not like mine, all I had on mine was Future Homemakers of America.

T: Hey, have you ever heard of Pinocchio? Shouldn’t I be learning right from wrong, developing a conscience and learning to love?

MS: Will any of those earn you a full ride scholarship to an Ivy League School?

T: No.

MS: Then, no. Ooh, there’s my archnemesis, Dmitri. He thinks he’s a better mad scientist than I. Wait til he sees you!

D: Hello, Victor. And what have we here?

MS: My son! All the latest biogengineering, he’s been designed to…

D: …then let me introduce my super daughter! Veronica! Her position as Valedictorian is assured! Veronica, explain quantum theory, now!

V: Father, I don’t think… Principal: It’s good to see all your happy, smiling faces here. I’m Principal Brown. Gonna get you all signed up for these great activities. Gonna make me look real good at the principal’s convention. Might even win a Princy this year. I hope you had a chance to meet Mr. Allenson, our drama director…

V: I would like to meet drama director!

BA: Good day! I’m Blake Allenson! I’ve directed four plays and only suffered three nervous breakdowns! Arsenic and Old Lace was a breeze I tell you! A breeze!

T: Wow. Are you British?

BA: No, old chap, I’m Dramatic!

T: Because it sounds like a British…

BA: I’m ACTING!

D: This is waste of time. Real students have no time for to make pretend…

P: Well, perhaps I could introduce you to our head football coach, Coach Manosfuertes…

CM: Hola! I am coach Manosfuertes. En los Estados Unidos, futbol is called soccer. Manosfuertes should have never taken this job…

T: I don’t think I’m interested in football. Maybe sports aren’t my thing.

MS: Nonsense, I’ve made certain… Great googly moogly… Jaeger: (Enters with much robotic nonsense.) I want to sign up for football. I will crush my opponents. I will hear the lamentations of their fans.

MS: Hans! What have you done? Hans: Vhat? Everyone else was bringing zeir superchildren to school. This is my son, Jaeger.

D: Da. Children. This is not children. Is 1000 pound robot.

H: I’m an engineer, not a biologist!!

J: Father? What is this feeling that burns inside? Making Jaeger want to hide? Like a tiny mouse, inside a tiny house!

D: What is this? Poetry? You make rhyme?

J: These are my words…

V: Is nice.

T: Yeah, that’s cool, Jaeger.

H: He’s very sensitive. On ze way here, he accidentally stepped on an old woman’s dog.

J: I almost cried. My heart, it died. I had killed the little doggy and my soul it felt so…so…

V: Foggy?

T: Groggy?

J: Just wait, Jaeger will find word.

T: Dad, I don’t know what I was thinking when I didn’t want to come here, this is awesome.

MS: This is not awesome. How will you become the most accomplished student in the school like this?

D: Veronica will be most accomplished student in school! Veronica! Destroy puny male!

T: What? I don’t even want to be the most accomplished student in the school!

V: Father, I don’t want to be the most…

D: (Taking out controller) You will do as I say!

MS: Oooh, is that a Parental Guiltinator 2000?

D: It is the 2001, with Extended Familial Obligation Overdrive!

H: I vant in on this, too! Jaeger! Crush!

MS: Let’s do this! (Takes out his controller as well.)

T: (Now under MS’s control, at least physically.) Oh, yeah, like this is for my own good!

MS: Of course it’s for your own good! My father never let me do anything! I’m making sure you do everything! (Everyone gears up/powers up for battle)

V: I’m sorry, I only ever wanted to be in a play, but now it seems I must tear you to shreds with my bare hands.

J: And I only want to rhyme words, like birds, in the sky, so high…Now you must die.

P: Manosfuertes, please contact emergency services. *sigh* Well, there goes my Princy.

T: Wait! Wait! Hold on! Is this really what you want to do? We’re just kids, why pit us against each other? Shouldn’t we just pursue our own dreams and goals and not worry what other kids are doing? Are you just trying to live through us or do you really care about our happiness? Why do we have to be superchildren? Why can’t we just be children?

BA: Bravo! Bravo! What a display! Blake Allenson approves!

M: Si! El nino es correcto! His noble declaration has brought a tear to the mighty Manosfuerte’s eye.

T: How about you just leave us kids here, and we’ll just decide on our own if we want to do an activity?

MS: My father would have never let me just…Ah, I see. Dmitri, Hans, let’s leave these kids here and talk outside. For example, how did you both show up with superchildren the same day as me? Were you spying on me?

D: We follow on the Tiktok.

H: You live streamed ze whole thing…

MS: OK, kids, have fun. We’ll go out for ice cream afterwards! We can take the transitionator!

T: Alright, Dad! So, what do you guys really want to do?

V: I vant to act!

J: I want to fill notebooks with angsty teen robot poetry!

T: I don’t really know what I want to do…

BA: Blake Allenson! That was quite a monologue just now. Have you ever considered the noble art of acting?

MS: Yes! Sign him up!

T: Dad!

MS: Sorry! Sorry. It’s hard to stop. Ah, this is an excellent opportunity to try the conclusion setting on the transitionator! You just push this button, and…
```

---

## IC-0532: The Musicians of Bremen

- Title: The Musicians of Bremen
- Author (byline): Wilhelm and Jakob Grimm
- Work: The World’s Best Fairy Tales, ed by Belle Becker Sideman
- Publisher: Reader's Digest Association
- Publication date as stated: 1977
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 1, ACTOR 2, NARRATOR, DONKEY, HOUND, CAT, COCK, CAPTAIN, ROBBER
- Teaser before the introduction: Yes
- Spoken words (computed): 1215
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
ACTOR 1: This story by the Brothers Grimm is about four farm animals who are convinced they can earn a good living as musicians.

ACTOR 2: Indeed they do, but it isn’t really the sweetness of their barking (bark), braying

(bray), mewing (meow), and cockle-doodle-doing (crow), that earns them their supper

ACTOR 1: – it’s more the terror of the sound they make!

TOGETHER: The Musicians of Bremen by Wilhelm and Jakob Grimm
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Note: The humor of this selection comes through the characterization of each animal and robber as well as the reaction of the narrator to what is occurring. The more outrageous the better. Plan pantomimes, sounds and characters carefully.

ACTOR 1: Narrator, Hound, Cat, Cock and Captain

ACTOR 2: Donkey and Robber

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

NARRATOR: The Cock was delighted with the idea, and so all four traveled on together. They could not, however, reach Bremen in one day, and at evening they came into a forest, where they meant to pass the night. The Donkey and the Hound lay down under a large tree. The Cat and the Cock climbed up into the branches, but the latter flew right to the top, where he was most safe. Before he went to sleep he looked around the countryside and thought he saw a little spark in the distance.

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

## IC-0533: My Most Embarrassing Case Scenario

- Title: My Most Embarrassing Case Scenario
- Author (byline): Ellen DeGeneres
- Work: The Funny Thing Is
- Publisher: Simon and Schuster
- Publication date as stated: Oct 2003
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 1, ACTOR 2, TOGETHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1143
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ellen Degeneres
Book: The Funny Thing Is
ISBN: 978-0743247634
Publisher: Simon and Schuster
Date (Month/Year): Oct 2003
```

### Introduction (context only: never use it for content warnings)

```text
TOGETHER: My Most Embarrassing Case Scenario by Ellen DeGeneres
```

### Performance text (classify this)

```text
ACTOR 1: There are all sorts of books offering advice on how to deal with life-threatening situations, but where’s the advice on dealing with embarrassing ones?

ACTOR 2: Things like landing a burning plane, wrestling a crocodile, or jumping from a moving train happen maybe five, six time in your life.

ACTOR 1: But embarrassing things happen hundreds of times each day. Here are a few things [we’ve] learned about how to survive life’s embarrassing moments

ACTOR 2: SITUATION: FORGETTING SOMEONE’S NAME

ACTOR 1: You’re at a party. Don’t ask me how you were invited.

ACTOR 2: Either your host is very forgiving or he has a very short memory. Or else he realizes that it was partially his fault.

ACTOR 1: Why else would he be bragging about his new fireproof mattress if he didn’t expect you to try it out?

ACTOR 2: And yes, in hindsight it is pretty obvious that just because the mattress is fireproof doesn’t mean that the sheets and irreplaceable antique quilt are fireproof as well.

ACTOR 1: Anyway, that’s all water under the bridge . . .

ACTOR 2: The same water, in fact, that you threw the burning quilt into to put it out.

ACTOR 1: Anyhoo, you’re at the party, you notice an old friend walking toward you, and you start to panic.

ACTOR 2: You’ve forgotten your friends name! What do you do? What do you do?

ACTOR 1: SOLUTION

ACTOR 2: There are a few possible solutions to the “forgetting the name” problem. And I’m not talking about ridiculous ones like pretending to faint, then claiming you don’t speak English.

ACTOR 1: That’s not only silly, but it has been proven not to work after the incident when you set fire to your host’s bedroom.

ACTOR 2: One solution is to have the same nickname for everyone. That way you only have to remember one name.

ACTOR 1: “Scooter!”

ACTOR 2: “Itchy!”

ACTOR 1: A second solution is to say “hi” to your old friend, then immediately grab hold of a third person and say all innocentlike . . .

ACTOR 2: “You two know each other, right?”

ACTOR 1: You wait for them to introduce themselves, and then sit back and relax.

ACTOR 2: The problem with this option is if the thir person just answers . . .

ACTOR 1: “No, I don’t know this person,”

ACTOR 2: Now you find yourself in the doubly awkward position of having to introduce two people whose names you’ve forgotten.

ACTOR 1: I mean, you can always just say, “Scooter, this is Itchy. Itchy, Scooter.”

ACTOR 2: But chances are that isn’t going to work.

ACTOR 1: THE BEST SOLUTION

ACTOR 2: Say to her, “I’m sorry, remind me again how you pronounce your name?”

ACTOR 1: “Kathy”

ACTOR 2: That’s right, the emphasis is on the first syllable, Ka-thy. I always think it’s on the second, Ka-thy. I’m glad you corrected me, my old friend.”

ACTOR 1: PROBLEM SOLVED!

ACTOR 2: SITUATION 2: LOSING YOURSELF IN THE MIDDLE OF A CONVERSATION

ACTOR 1: When our minds are deprived of stimulation, they dent to wander. The mind craves interesting conversation.

ACTOR 2: Which brings us back to the party and Ka-thy.

ACTOR 1: Kathy, it turns out, is a bore

ACTOR 2: Which I’m guessing is why you forgot her name in the first place.

ACTOR 1: She’s been talkin gat you for a long time about this and that and you’ve just drifted off.

ACTOR 2: (sings) “ . . . Fat Kids, skinny kids, even kids with chicken pox love hot dogs . . .”

ACTOR 1: You’re kind of aware of her mouth moving, but you have no idea what she’s saying. Then you hear the words . . .

ACTOR 2: “Inhaling Mold Spores”

ACTOR 1: And, like that, you’re back. You have no idea what the subject of the conversation is, and Kathy has just stopped talking.

ACTOR 2: She’s staring at you

ACTOR 1: (or slightly to the right of you because of her lazy eye)

ACTOR 2: expecting you to say something. What do you do? What do you do?

ACTOR 1: SOLUTION:

ACTOR 2: The only proven way to get yourself out of this embarrassing situation is to say something about Gloria Estefan.

ACTOR 1: I’m telling you, as long as you commit to it, she can fit into any conversation.

ACTOR 2: You don’t believe [us]? Here’s proof.

ACTOR 1: Kath is still staring at you waiting for a response . . . . . Finally you say

ACTOR 2: “That sounds a lot like Gloria Estefan”

ACTOR 1: Kathy looks at you funny and says,

ACTOR 2: “What that got to do with copper plumbing?”

ACTOR 1: To which you respond

ACTOR 2: “Well, Gloria Estefan is the copper plumbing of the music industry. She’s beautiful, reliable and indestructible. Look how she came back after that bus accident! Are you going to debate me on this?!”

ACTOR 1: And, presto, you’re back in the conversation and nobody’s the wiser.

ACTOR 2: SITUATION: ACCIDENTLY REVEALING INTIMATE THOUGHTS TO A STRANGER

ACTOR 1: Revealing intimate thoughts to a stranger isn’t always embarrassing. In fact, sometimes it’s downright therapeutic.

ACTOR 2: Many people pay strangers to listen to their darkest fantasies and most perverse secret thoughts.

ACTOR 1: But, like most situations in life, when there is no money changing hands, the changes of being embarrassed multiply significantly.

ACTOR 2: So you’re sill at the party, standing next to Kathy and you feel the need to reveal something deep and significant. So you say . . .

ACTOR 1: “My underwear keeps going up my crack.”

ACTOR 2: “Excuse me?”

ACTOR 1: You turn and see not Kathy but a total stranger. Kathy has ditched you. The stranger looks at you and says loudly . . .

ACTOR 2: (old lady voice) “Did you just say your underwear keeps going into your crack?

ACTOR 1: People start to look at you. What do you do? What do you do?

ACTOR 2: SOLUTION

ACTOR 1: Deny, deny, deny! Calmly look at her and shriek “No, of course not. Are you kidding? What?! No!” or . . . .

ACTOR 2: Attack, attack, attack. Look at her and say, “Listen, I’ve had just about enough with the questions. Who are you, anyway? I don’t know you. I don’t owe you any explanation. You are way too curious for me, old lady. Why don’t you go stand next to someone else and eavesdrop on them, you weirdo?!”

ACTOR 1: And that’s usually when Kathy comes back and says . . .

ACTOR 2: “Oh, great, I see you’ve met our host’s grandmother.”

ACTOR 1: [And the last embarrassing] SITUATION: HUG, KISS, OR SHAKE HANDS

ACTOR 2: Believe it or not, it is as potentially awkward to greet someone whose name you remember as it is to greet Kathy.

ACTOR 1: That’s because you never know what physical action to take upon greeting each other.

ACTOR 2: Do you shake their hand?

ACTOR 1: Do you hug them?

ACTOR 2: Do you kiss them?

ACTOR 1: Or, trickiest yet, do you to the complicated hug-kiss combo? (demonstrate) What do you do? What do you do?

ACTOR 2: SOLUTION

ACTOR 1: The answer to this dilemma is as simple as it is uncomplicated.

ACTOR 2: Let you friend make the first move and respond accordingly.

ACTOR 1: What’s important for this strategy to work is to adopt the right stance so that you’re ready for whatever physical greeting is about to be laid on you.

ACTOR 2: I recommend legs should-width apart, should leg-width apart, and arms outstretched but with a little bend in the elbow so that you don’t look like you’re being crucified.

ACTOR 1: If you friend, undertaking the same strategy, approaches you with the same stance, that’s okay too.

ACTOR 2: I’ve had long conversations with people where both of us stood a foot away from each other, our arms outstretched, talking for hours.

TOGETHER: [And that’s] how to survive life’s embarrassing moments!
```

---

## IC-0534: Naughty or Nice

- Title: Naughty or Nice
- Author (byline): Jonathan Mitchell and Seth Lind
- Work: Not specified
- Publisher: National Public Radio
- Publication date as stated: Dec 2014
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 2, VOICE OVER TOGETHER, NEWSCASTER 1, NEWSCASTER 2, NAUGHTY CHILD, BELL, SPARK, MICHAEL, UNAMED ELF, SANTA’S SECRETARY, SANTA, COAL LOBBYIST, MALL CREW LEADER, LITTLE GIRL, MOM, FACTORY ELF, MICHAEL’S MOM, MICHAEL’S DAD
- Teaser before the introduction: Yes
- Spoken words (computed): 1258
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
TOGETHER: Naughty or Nice by Jonathan Mitchell and Seth Lind
```

### Performance text (classify this)

```text
Suggested Roles: ACTOR 1: Newscaster 1, Naughty Child, Spark, Coal Lobbyist, Little Girl, Michael’s Mom

ACTOR 2: Newscaster 2, Bell, Michael, Unnamed Elf, Santa’s Secretary, Santa, Mall Crew Leader, Factory Elf, Michael’s Dad

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

VOICE OVER TOGETHER: (singing) You better watch out. You better not cry. You better not pout. I'm telling you why.

NEWSCASTER 1: Deep inside the North Pole . . . past the tinsel, beyond the twinkling lights, is Santa’s highly efficient, questionably ethical corporate headquarters. Forget sugarplums; this is surveillance footage, performance reviews, and elves with access cards.

NEWSCASTER 2: In a world where 30 seconds of bad behavior can earn you a lifetime supply of coal, one idealistic elf dares to ask the unthinkable: “Um . . . are we sure?” This is what happens when Christmas meets middle management. Sit back, stay off the naughty list, and enjoy . . .

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

SPARK: (backtracks quickly) No. Definitely not. No. Glad to be here. (steps out of scene to speak to the audience) See, I don't want to complain about this job. But I'm looking at like 30 seconds of video of a kid, and then they're breathing down my neck to make an instant decision, like, this kid's naughty; this kid's nice. I really don't think this is how Santa would want it to run. (as if hearing a call out from the audience) Talk to Santa? (loves this idea) ***** In Santa’s office*****

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

## IC-0535: The Phantom Tollbooth

- Title: The Phantom Tollbooth
- Author (byline): Norton Juster
- Work: Not specified
- Publisher: Bullseye Books
- Publication date as stated: Oct 1988
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: SUGGESTED DIVISION OF PLAYERS, ACTOR 1, ACTOR 2, NARRATOR, MILO, GATEMAN, MERCHANT 1, MERCHANT 2, MERCHANT 3, MERCHANT 4, PAGE, KING AZAZ, GUEST 1, GUEST 2, GUEST 3, KING AZAS, THE MAN, TERRIBLE TRIVIUM
- Teaser before the introduction: Yes
- Spoken words (computed): 2675
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
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

SUGGESTED DIVISION OF PLAYERS:

ACTOR 1: Narrator (shared), Gateman, 5 Gentlemen, Merchant 1 and 3, King Azaz, GUEST 1, The Man

ACTOR 2: Narrator (shared), Milo, Merchant 2 and 4, Page, GUEST 2, GUEST 3, TERRIBLE TRIVIUM

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

## IC-0536: The Plane Truth

- Title: The Plane Truth
- Author (byline): Ellen DeGeneres
- Work: Sand in My Bra and Other Misadventures
- Publisher: Traveler's Tale
- Publication date as stated: March 2003
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 1, ACTOR 2, TOGETHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1177
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ellen DeGeneres
Book: Sand in My Bra and Other Misadventures
ISBN: 978-1885211927
Publisher: Traveler's Tale
Date (Month/Year): March 2003
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Many people have a fear of flying

ACTOR 2: And the Flight Attendant’s spiel before take-off doesn’t inspire a great deal of confidence either!

(Presented in friendly, flight attendant voices with accompanying gestures)

ACTOR 1: Welcome aboard Flight 245. To operate your seat belt, insert the metal tab into the buckle, and pull tight.

ACTOR 2: It works just like every other seat belt, and if you don’t know how to operate one, you probably shouldn’t be out in public unsupervised.

ACTOR 1: In the event of a sudden loss of cabin pressure, masks will descend from the ceiling.

ACTOR 2: Stop screaming, grab the mask, and pull it over your face.

ACTOR 1: If you have a small child traveling with you, secure your mask before assisting with theirs.

ACTOR 2: If you are traveling with more than one small child, pick your favorite.

TOGETHER: The Plane Truth by Ellen DeGeneres
```

### Performance text (classify this)

```text
ACTOR 1: (Pg 28-34) I know that the experts say you’re more likely to get hurt crossing the street than you are flying

ACTOR 2: (these, of course, would be the street-crossing experts),

ACTOR 1: but that doesn’t make me feel any less frightened of flying.

ACTOR 2: If anything, it makes me more afraid of crossing the street. As soon as the light turns green, I run across the street as fast as I can, screaming like a mad *person.* (Actor 1 demonstrates) I arrive on the other side out of breath, wheezing, and clutching my stomach.

ACTOR 1: I felt edgy the moment I stepped into the aircraft. That could be why I snapped at the woman in front of me. In my defense, she did ask the flight attendant a pretty stupid question:

ACTOR 2 as WOMAN IN 27-B (also a nun): Excuse me, where is seat 27-B?

ACTOR 1: I mean, really. But I see now that I overreacted when I screamed at her, “Well, moron you walk in the only direction you can, and it’s the 27th row seat B – next to seat A. All righty?!”

ACTOR 2: That sort of response is probably one of the many reasons why I’m not a flight attendant.

ACTOR 1: It was only when the woman (27-B) turned around to look at me that I saw she was a nun. (Actor 2 makes the sign of the cross or praying gesture) I guess that sort of hat-like thing she wore on her head should have given me a clue.

ACTOR 1: I tried to apologize by smiling and giving her a playful punch on the arm to let her know I was joking.

ACTOR 2: Well, either my playful punch carried more of a wallop than I intended,

ACTOR 1: Or her advanced years made her frailer than she appeared, but the nun shouted out

ACTOR 2 as WOMAN IN 27-B (also a nun): Owww! (rubbing her arm in pain . . . she rolls up her sleeve)

ACTOR 1: . . . you know, that bruise could easily have been there before I hit her.

ACTOR 2: My good friend Jasmine told me that a good way to combat fear is to chant.

ACTOR 1: (making her way down the airplane aisle) I’m going to die, I’m going to die, oh sweet Lord, I’m going to die.

ACTOR 2: It didn’t work. If anything, I was more petrified when I got to my seat (27-A).

ACTOR 1: Even seeing the familiar face of the nun in 27-B (Actor 2 at the nun looks up aghast) didn’t call me down. So here I am, sitting in my seat. (taking calming breaths, then reacts violently to a sound) ARGHHH! What was that? We’re going to crash!!! (Actor 2 as the nun responds) Oh . . . It was just the beverage cart. Pardon me, Sister, I am sorry, I . . . I was frightened. Pray for me. (Actor 2 as the nun give a hateful look and reaches to turn on the air vent) Now she’s going to turn on that little air thing above her. Maybe I’m paranoid, but I think it takes power away from the plane somehow. Sister, don’t use that, that’s . . . . Dang! Shut if off! Shut it off! (Actor 2 as the nun has had enough. She climbs over her seatmate to find another seat, turning to give a rude gesture) Some people are so touchy. I’m sure she didn’t learn that little hand gesture in her convent, either.

ACTOR 2: I’ve got to relax somehow. Why didn’t I think of this sooner? I’ll recline my seat.

(both Actors do so)

ACTOR 1: Oh, that makes all the difference. That ¾ of an inch between upright and reclined is the difference between agony and ecstasy. I never thought ¾ of an inch could mean so much.

ACTOR 2: When I get home, I’m going to put some gizmo in my chairs so that they go back ¾ of an inch, too.

ACTOR 1: But . . . I’d better not get too comfortable in my ¾-of-an-inch recline because toward the end of the flight, the flight attendant is going to say,

ACTOR 2 as FLIGHT ATTENDANT: You’re going to have to put your seat in the upright position for landing.

ACTOR 1: They’re so adamant about that every single time, like that’s gonna make a difference. Because if we crash, the investigators are going to say,

ACTOR 2 as INVESTIGATOR: Oh, that’s a shame, her seat was reclined ¾ of an inch. When will they learn? What was that – 30,000 feet? She could have made that. Sheesh. If only she’d been upright.

ACTOR 1: Being reclined isn’t working. I’m still freaking out. I know what I need. (Calling out) Oh, flight attendant. Oh ma’am. (to audience) You have to talk nice to the flight attendants because they all have this attitude.

ACTOR 2: And they can afford to have the attitude, because they have the power – they have the peanuts.

ACTOR 1: They have these six peanuts that we need. Six peanuts. Somebody could offer that to you on the street, and you’d say,

ACTOR 2: I don’t want that – get that away from me. Six peanuts? No- oh.

ACTOR 1: Somehow they’ve done research. They know that the higher we go, the more we need nuts. And we go crazy if we don’t get them.

ACTOR 2: Miss, I didn’t get my, uh - - my peanuts. And I’d really appreciate it if you gave me some. (stuffing peanuts one at a time in her mouth) They’re good, aren’t they? I’ve never been able to get them on the ground either. At least not ones this good! (licking the salt from her fingers)

ACTOR 1: (panicked) What was that! We’re going to crash! Oops, false alarm. It’s just the food cart coming down the aisle.

ACTOR 2: Oh, here comes the cart, put down the tray! La la la la. Put down your tray! They’re starting on the other side first. Hurry! Hurry! Those people over there – they’re eating. Those people are eating.

ACTOR 1: Any kind of meat that you get – chicken, steak, anything – has grill marks on each side, like somehow, we’ll actually believe there’s an open-flame grill in the front of the plane

ACTOR 2: And salads are always two pieces of dead lettuce and salad dressing that comes in that astronaut package. (package explodes as she tries to open it) As soon as you open it, it’s on your neighbor’s lap.

ACTOR 1: Could I just dip my lettuce, ma’am? Hm, that’s a lovely skirt. What is that, silk?

ACTOR 2: But you know, should that happen, club soda’s gonna get that stain out immediately. That’s the answer to anything you ask up there, I don’t know if you’ve noticed that.

ACTOR 1: Excuse me, I have an upset stomach.

ACTOR 2 as FLIGHT ATTENDANT: Club soda, be right back.

ACTOR 1: Excuse me, I spilled something.

ACTOR 2 as FLIGHT ATTENDANT: Club soda, be right back.

ACTOR 1: Ooh, the wing is on fire!

ACTOR 2 as FLIGHT ATTENDANT: Club soda, be right back.

ACTOR 1: I thought the food would make me feel less frightened. But it didn’t. Maybe if I stretch my legs and go to the restroom it will help.

ACTOR 2: You have no concept of time when you’re in there – it’s like a casino: no windows, no clocks.

ACTOR 1: I could be the only one to get up out of my seat to go to the bathroom – everybody else is sound asleep when I go – but after I’ve been in there for what I think is thirty seconds, I open the door and everyone in the plane is lined up, looking at their watches, make me feel like I’ve been in there forever.

ACTOR 2: And now I’ve got to explain the smell that was in there before I went in there.

ACTOR 1: Oh! Listen, there’s an odor in there and I didn’t do it. It’s bad. You might want to sprinkle some club soda, if you uh . . .

ACTOR 1: I think my only hope of escaping my mind-numbing fear is to sleep;

ACTOR 2: . . . to sleep and perchance to dream. . .

ACTOR 1: The only trouble is when I fall asleep on a plane, (both drift off while finishing this statement) I always have a nightmare . . .

TOGETHER: (only to jolt awake screaming) Oh sweet Lord, I’m going to die!
```

---

## IC-0537: Playwriting 101: The Rooftop Lesson

- Title: Playwriting 101: The Rooftop Lesson
- Author (byline): Rich Orloff
- Work: Take Ten II
- Publisher: Vintage Books
- Publication date as stated: Nov 2003
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: JUMPER, GOOD SAMARITAN, TEACHER
- Teaser before the introduction: Yes
- Spoken words (computed): 901
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
ACTOR 1: Cliché – A saying, image or idea which has been used so much that it should terribly uncreative.

ACTOR 2: Using cliché’s is considered BAD writing because they make it sound like you didn’t put any thought into your words.

ACTOR 1: Satire – The use of humor, exaggeration or ridicule to expose and criticize peoples stupidity.

ACTOR 2: Politicians and, in this case, playwrights are easy targets – especially when they’re acting self-righteous!

ACTOR 1: In Playwriting 101: The Rooftop Lesson, Rich Orloff masterfully combines Cliché and Satire to create something . . . something . . . .

ACTOR 2: That will make you want to jump off a roof!

TOGETHER: Playwriting 101: The Rooftop Lesson by Rich Orloff.
```

### Performance text (classify this)

```text
NOTE: This cutting asks one student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles: Actor 1: The Jumper and The Teacher Actor 2: The Good Samaritan

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

## IC-0538: The Secret Knowledge of Grown-Ups

- Title: The Secret Knowledge of Grown-Ups
- Author (byline): David Wisniewski
- Work: Not specified
- Publisher: Harper Collins
- Publication date as stated: July 2001
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 1, ACTOR 2, TOGETHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1281
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
TOGETHER: The Secret Knowledge of Grown-Ups by David Wisniewski
```

### Performance text (classify this)

```text
ACTOR 1: (Pg 8-9) The truth must be told to kids!

ACTOR 2: For too long, for centuries in fact, it’s been covered over, hidden, impossible to find.

ACTOR 1: A conspiracy, an organized silence by generations of grown-ups, has kept the truth from millions of children.

ACTOR 2: And what is this truth, you ask.

ACTOR 1: Simply this: The reasons grown-ups tell you to do things are not true!

ACTOR 2: Eat your vegetables, they say. They’re good for you.

ACTOR 1: NONSENSE!

ACTOR 2: Comb your hair, they say. It keeps it neat.

ACTOR 2: POPPYCOCK! There are far mor sinister, truly macabre reasons for these seemingly innocent requests.

ACTOR 1: Over the last three years, [we’ve] gathered as much information as [we] could: crisscrossing the country in clever, impenetrable disguises . . .

ACTOR 2: Breaking into the secret files kept by hundreds of grown-ups . . .

ACTOR 1: Assembling the evidence.

ACTOR 2: And now . . . the truth!

TOGETHER: (Pg 11-15) GROWN-UP RULE #31

ACTOR 1: Eat Your Vegetables

ACTOR 2: Official Reason: They’re good for you

ACTOR 1: The Truth: You don’t eat vegetables because they’re good for you. You eat vegetables to keep them under control!

ACTOR 2: Millions of years ago, vegetables ruled the earth.

ACTOR 1: Big bunches of broccoli stomped through the jungles, followed by ferocious carrots and savage packs of peas.

ACTOR 2: And what were these terrible vegetables looking for? You guessed it . . .

ACTOR 1: People! Yes, these were meat-eating vegetables.

ACTOR 2: They terrorized the early humans, attacking without warning.

ACTOR 1: Our ancestors put up with this for centuries, living in drafty caves and getting nasty head colds. But then they discovered sticks and stones.

ACTOR 2: With these new weapons, humans began to defend themselves. At first, lone hunters would take on a single radish or green bean.

ACTOR 1: Eventually, groups of hunters tackled bigger game, like the saber-toothed asparagus and woolly cucumber.

ACTOR 2: By mixing these vanquished vegetables, primitive chefs invented

TOGETHER: SALAD!

ACTOR 1: More important, the discovery of fire allowed humans to cook their leafy foes.

ACTOR 2: This brought the Age of Vegetables to a close.

ACTOR 1: As the human race grew in size and intelligence, vegetables became smaller and dumber, devolving into the pathetic produce of gardens and grocery stores.

ACTOR 2: To prevent vegetables from ever regaining power, grown-ups eat them.

ACTOR 1: They don’t like the flavor any more than you do, but it keeps the little horrors fearful and demoralized. It’s a simple way to protect modern civilization.

ACTOR 2: Besides, which would you rather do: Eat vegetables or be eaten by vegetables?

ACTOR 1: (Pg 17-21) [And what about] GROWN-UP RULE #37

TOGETHER: Drink Plenty of Milk

ACTOR 2: Official Reason: It’s good for you

ACTOR 1: The Truth: Yes, milk is packed with vitamins and protein, but that’s not why parents want you to drink it. The real reason is . . .

TOGETHER: TO STOP OUR ATOMIC COWS FROM EXPLODING!

ACTOR 2: Kids have been told that millions of cows produce our country’s milk. That’s not true.

ACTOR 1: At this moment, only five giant cows do all the work. The other are decoys made of plywood and old box springs.

ACTOR 2: One of these colossal cows is Flossie. (MOO!) Eighty feet tall, she provides the daily milk supply for Utah, Nevada, Wyoming, and Colorado.

ACTOR 1: Flossie is kept under tight security at a secret air-force base, right next to the hangar where they stack all the banged-up flying saucers.

ACTOR 2: Flossie’s size is no accident. In the 1950s, our government was afraid that the Russians would develop the first atomic cow and flood the market with Communist milk.

ACTOR 1: To prevent this, American scientists fed Flossie and her friends radioactive hay.

ACTOR 2: The experiment worked great. But Flossie can’t be turned off. The milk just keeps coming.

ACTOR 1: [Now], government officials are very happy that all this milk is available. However, there is one crisis the government can’t prepare for: kids NOT drinking milk.

ACTOR 2: If that happened, Flossie would have to hold it (both actors cross their legs)

ACTOR 1: Getting bigger and bigger until

TOGETHER: NUCLEAR MILKDOWN!

ACTOR 2: Such a catastrophe forever scars the landscape between the Arizona towns of Flagstaff and Winslow.

ACTOR 1: A huge crater is all that remains of Doris, the only atomic cow that ever exploded.

ACTOR 2: When kids felt the ground shake and saw the curdled cloud of dairy products form over the desert back in 1962, they were told that a meteor had hit the local Tastee Freeze.

ACTOR 1: Now you know better. So drink your milk!

ACTOR 2: (Pg 37-41) [Which brings us to] GROWN-UP RULE #62

TOGETHER: Don’t jump on your bed. (jumping enthusiastically)

ACTOR 2: Official Reasons: You’ll break it. You might get hurt.

ACTOR 1: The Truth: Yes, it’s possible to break your bed if you jump on it. And it’s possible you might bet hurt if you fall off. But you’ll definitely get hurt . . .

TOGETHER: IF YOU WAKE UP THE MATTRESS!

ACTOR 2: You see, mattresses aren’t just big lifeless rectangles crammed with stuffing.

ACTOR 1: They are active wooly creatures raised on farms in Scotland. After growing to adulthood, the mattresses start a long period of hibernation.

ACTOR 2: Undisturbed by noise and handling, they are rounded up, sorted by size, and sold to stores.

ACTOR 1: Then they end up in your bedroom, where they snooze peacefully year after year.

ACTOR 2: Unless you jump on them!

ACTOR 1: Fortunately, today’s mattresses are very difficult to wake up. That wasn’t the case with their hardy ancestors.

ACTOR 2: One night, about 1040 AD, the Scottish King, Malcolm the Upset, wandered the moors, trying to get over eating haggis --

ACTOR 2: A real humdinger of a national dish – a pudding made from the heart, lungs and liver of a sheep! No, I am NOT making this up!

ACTOR 2: Malcolm stumbled upon a wild hibernating mountain mattress, upon which he slept soundly for the first time in many years. He realized that the wild mattress was more comfortable than the boulder he usually slept on.

ACTOR 1: King Malcolm brought the mattress home and began breeding it. Soon he was giving mattresses as gifts to other kinds and queens.

ACTOR 2: Unfortunately, these feral mattresses woke up and started slinging royalty around!

ACTOR 1: This was very bad for King Malcolm, who spent the rest of his life in prison, eating haggis. (EWWWWW!)

ACTOR 2: The modern domestic mattress [has a mild] disposition and long hibernation period.

ACTOR 1: Still, it’s not a good idea to jump on your bed. The mattress might be hard to wake up, but it’s not impossible.

ACTOR 2: And, for goodness sake, don’t play the bagpipes near it!

ACTOR 1: (Pg 49-52) [And finally] GROWN-UP RULE #82 - Don’t pick your nose.

ACTOR 2: Official Reason: It’s gross and disgusting

ACTOR 1: The Truth: Actually, picking your nose is gross and disgusting. However, that’s not the real reason, which is . . .

TOGETHER: TO STOP YOUR BRAIN FROM DEFLATING!

ACTOR 2: The air pipeline that keeps your brain inflated runs past the nostrils to a vast pumping station inside your head.

ACTOR 1: An intruding digit will certainly dent the pipeline. It may even poke a hole in it, causing an outburst of air called

ACTOR 2: (Sneezes) In technical language, a sneeze.

ACTOR 1: If you can’t give up this nasty habit right away, at least be familiar with the warning signs of brain deflation:

ACTOR 2: A faint hissing noise (noise by Actor 1)

ACTOR 1: A sound like a balloon let loose in a bathtub (noise by Actor 2)

ACTOR 2: Silence, and a floppy rolling noise when you tilt your head (noise by Actor 1)

ACTOR 1: Although this baggy brain still works, it won’t absorb much new information, so it pays to fix it before the next spelling test. Here’s the simple way . . .

ACTOR 2: Shine a flashlight up your nose (demonstrates)

ACTOR 1: Just as a plant tuns toward the sun, your brain will be attracted to the light and flop over to it. Your brain will then be centered over the pipeline, ready for inflation.

ACTOR 2: Hold your nose and hum. (demonstrates)

ACTOR 1: Finger pressure stabilizes the pipeline. Humming entertains the mending muscles as they drive bulldozers around to fix things up.

ACTOR 2: There is a more difficult way to reinflate your brain, but it requires four years of college, one pair of pliers, and three feet of lead pipe.

ACTOR 1: Hundreds of grown-up rules remain. The truth must be told about them ALL!

ACTOR 2: (reaction to an unseen noise - whispers) But they’re on [our] trail. I hear them coming!

TOGETHER: THE GROWN-UPS!!!
```

---

## IC-0539: The Seussification of Romeo and Juliet

- Title: The Seussification of Romeo and Juliet
- Author (byline): Peter Bloedel
- Work: Random Acts of Comedy (Pg 189-216)
- Publisher: Playscripts, Inc.
- Publication date as stated: Aug 2011
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR 1, NARRATOR 2, BOTH, PROLOGUE, PARIS, CAPITULATE, SERVANT, BENVOLIO, ROMEO, TYBALT, JULIET, NURSE, MONK LARRY, MERCUTIO, THE PRINCE, LADY CAPITULATE
- Teaser before the introduction: Yes
- Spoken words (computed): 1439
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
TOGETHER: The Seussification of Romeo and Juliet by Peter Bloedel
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles: Actor 1: Narrator 1; Prologue; Romeo baby; Pregnant Lady Capitulate; Paris; Servant; Romeo, The Prince; Monk Larry in scene with Juliet, Monotone

Actor 2: Narrator 2; Pregnant Lady Monotone, Juliet baby; Capitulate; Benvolio; Juliet; Nurse; Tybalt; Monk Larry in scene with Romeo; Mercutio; Lady Capitulate

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

NARRATOR 1: 'Cus we've all enjoyed it ...

BOTH: One-hundred percent!
```

---

## IC-0540: The Sneetches

- Title: The Sneetches
- Author (byline): Theo Geisel (aka Dr. Suess)
- Work: Not specified
- Publisher: Random House, Inc.
- Publication date as stated: Aug 1961
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR 1, NARRATOR 2, STAR BELLIED SNEETCHES, MCBEAN, PLAIN BELLIED SNEETCHES, TOGETHER
- Teaser before the introduction: Yes
- Spoken words (computed): 832
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
ACTOR 2: At first glance, The Sneetches by Theodor Seuss Geisel feels like a simple children’s story –

ACTOR 1: Bright creatures, ridiculous machines, and a problem as silly as stars on bellies.

ACTOR 2: It invites us to laugh, to relax, to believe this is just another harmless rhyme.

ACTOR 1: But listen a little closer, and the humor starts to shift. Today, division doesn’t feel trivial.

ACTOR 2: It feels constant. It feels loud.

ACTOR 1: It feels uncomfortably real, as people sort themselves into political and moral parties and question the worth of others . . .

ACTOR 2: And that’s when the laughter at a silly children’s story gets quiet.

TOGETHER: The Sneetches by Theodore Geisel (aka Dr. Suess)
```

### Performance text (classify this)

```text
Suggested Roles: Actor 1 – Narrator 1, McBean; Plain Bellied Sneetches Actor 2 – Narrator 2; Star Bellied Sneetches

NARRATOR 1: Now the Star-bellied Sneetches had bellies with stars. The Plain-bellied Sneetches had none upon thars.

NARRATOR 2: The stars weren't so big; they were really quite small. You would think such a thing wouldn't matter at all.

NARRATOR 1: But because they had stars, all the Star-bellied Sneetches would brag . . .

STAR BELLIED SNEETCHES: We're the best kind of Sneetch on the beaches.

NARRATOR 1: With their snoots in the air, they would sniff and they'd snort . . .

STAR BELLIED SNEETCHES: We'll have nothing to do with the plain-bellied sort.

NARRATOR 1: And whenever they met some, when they were out walking, they'd hike right on past them without even talking.

NARRATOR 2: When the Star-bellied children went out to play ball, could the Plain-bellies join in their game? Not at all!

NARRATOR 1: You could only play ball if your bellies had stars, and the Plain-bellied children had none upon thars.

NARRATOR 2: When the Star-bellied Sneetches had frankfurter roasts,
or picnics or parties or marshmallow toasts,
they never invited the Plain-bellied Sneetches.
Left them out cold in the dark of the beaches.

NARRATOR 1: Kept them away; never let them come near, and that's how they treated them year after year.

NARRATOR 2: Then one day, it seems, while the Plain-bellied Sneetches
were moping, just moping alone on the beaches,
sitting there, wishing their bellies had stars,
up zipped a stranger in the strangest of cars.

MCBEAN: My friends . . .

NARRATOR 2: He announced in a voice clear and keen

MCBEAN: My name is Sylvester McMonkey McBean.
I've heard of your troubles; I've heard you're unhappy.
But I can fix that; I'm the fix-it-up chappie.
I've come here to help you; I have what you need.
My prices are low, and I work with great speed,
and my work is one hundred percent guaranteed.

NARRATOR 2: Then quickly, Sylvester McMonkey McBean put together a very peculiar machine. Then he said . . .

MCBEAN: You want stars like a Star-bellied Sneetch? My friends, you can have them . . . for three dollars each. Just hand me your money and climb on aboard.

NARRATOR 2: They clambered inside and the big machine roared. It bonked. It clonked. It jerked. It berked.

NARRATOR 1: It bopped them around, but the thing really worked.

NARRATOR 2: When the Plain-bellied Sneetches popped out, they had stars! They actually did, they had stars upon thars! Then they yelled at the ones who had stars from the start,

PLAIN BELLIED SNEETCHES: We're exactly like you; you can't tell us apart. We're all just the same now, you snooty old smarties. Now we can come to your frankfurter parties!

STAR BELLIED SNEETCHES: Good grief! We're still the best Sneetches, and they are the worst. But how in the world will we know if which kind is what or the other way 'round?

NARRATOR 2: Then up stepped McBean with a very sly wink, and he said . . .

MCBEAN: Things are not quite as bad as you think.
You don't know who's who, that is perfectly true.
But come with me, friends, do you know what I'll do?
I'll make you again the best Sneetches on beaches,
and all it will cost you is ten dollars eaches.
Belly stars are no longer in style.
What you need is a trip through my stars-off machine.
This wondrous contraption will take off your stars,
so you won't look like Sneetches who have them on thars.

NARRATOR 2: That handy machine, working very precisely, removed all the stars from their bellies quite nicely.

NARRATOR 1: Then, with snoots in the air, they paraded about. They opened their beaks and proceeded to shout . . .

STAR BELLIED SNEETCHES: We now know who's who, and there isn't a doubt, the best kind of Sneetches are Sneetches without.

NARRATOR 1: Then, of course those with stars all got frightfully mad. To be wearing a star now was frightfully bad.

Then, of course old Sylvester McMonkey McBean invited them into his stars-off machine.

NARRATOR 2: Then, of course from then on, you can probably guess,
things really got into a horrible mess.
All the rest of the day on those wild screaming beaches,
the Fix-it-up-Chappie was fixing up Sneetches.

NARRATOR 1: Off again, on again, in again, out again,
through the machine and back round about again,
still paying money, still running through,
changing their stars every minute or two,
until neither the Plain- nor the Star-bellies knew
whether this one was that one or that one was this one
or which one was what one or what one was who!

NARRATOR 2: Then, when every last cent of their money was spent, the Fix-It-Up-Chappie packed up and he went. And he laughed as he drove in his car up the beach. . .

MCBEAN: They never will learn; no, you can't teach a Sneetch!"

NARRATOR 2: But McBean was quite wrong, I'm quite happy to say,
the Sneetches got quite a bit smarter that day.
That day, they decided that Sneetches are Sneetches,
and no kind of Sneetch is the BEST on the beaches.

TOGETHER: That day, all the Sneetches forgot about stars,

NARRATOR 2: and whether they had one

NARRATOR 1: or not

TOGETHER: upon thars.
```

---

## IC-0541: Squids will be Squids

- Title: Squids will be Squids
- Author (byline): Jon Scieszka
- Work: Not specified
- Publisher: Viking Press
- Publication date as stated: Sept 1998
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 1, ACTOR 2
- Teaser before the introduction: Yes
- Spoken words (computed): 1388
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jon Scieszka
ISBN: 978-0670881352
Publisher: Viking Press
Date (Month/Year): Sept 1998
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: John Scieszka’s book Squids will be Squids. is a collection of fables that Aesop might have told if he were alive today, sitting in the back of the class day dreaming, goofing around instead of paying attention, because his dog ate his homework and he didn’t have time to run out and buy new paper and do it over again before his bus came to pick him up in the morning..

ACTOR 2: Enjoy a few of these contemporary fables today; listen for the Moral of each story and remember . . . Sometimes the names are changed to protect the not so innocent.

TOGETHER: Squids will be Squids by John Scieszka
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

ACTOR 1: Fables have been around for thousands of years. And it’s no wonder, because even thousands of years ago people were bright enough to figure out that you could gossip about anybody as long as you changed their name to something like “Lion” “Mouse” or “Donkey”

ACTOR 2: Aesop is the guy most famous for telling fables. Though he wasn’t the first or the best looking. Most descriptions of Aesop call him, funny shaped or ugly or worse. But you didn’t hear that from me. I think Aesop was one heck of a swell guy.

ACTOR 1: Deer, Mouse, Rabbit and Squid: Deer, Mouse, Rabbit and Squid sat on the steps trying to decide what to do.

ACTOR 2 (DEER): "Let's go see a movie,"

ACTOR 1: (MOUSE): "Great," said Mouse.

ACTOR 2 (RABBIT): "Great"

ACTOR 1 (SQUID): "There's nothing good on,"

ACTOR 1 (MOUSE): "Let's play Frisbee in the park,"

ACTOR 2 (RABBIT): "Great,"

ACTOR 1 (DEER): "Great,"

ACTOR 1 (SQUID): "My tentacles are too tired,"

ACTOR 2 (RABBIT): “Let's go shopping,"

ACTOR 1 (DEER): “Great,".

ACTOR 1 (MOUSE): "Great,"

ACTOR 1 (SQUID): "That's so boring, I'm just going to go home,”

ACTOR 2: and she oozed off down the street.

ACTOR 1 (AS ALL): "Great,"

ACTOR 2: Then they ran off to see a movie, play Frisbee in the park, and go shopping.

ACTOR 1: MORAL: Squids will be Squids. ************************

ACTOR 2: Grasshopper Logic: One bright and sunny day, Grasshopper came home from school, dropped his backpack and was just about to run outside to meet his friends.

ACTOR 1 (MOM): “Where are you going?”

ACTOR 2 (GRASSHOPPER): “Out to meet some friends,”

ACTOR 1 (MOM): “Do you have any homework due tomorrow?”

ACTOR 2 (GRASSHOPPER): “Just one small thing for History. I did the rest in class.”

ACTOR 1 (MOM): “Okay, Be back at six for dinner.”

ACTOR 2: Grasshopper hung out with his friends, came home promptly at six, ate his dinner, then took out his History homework. His Mom read the assignment and freaked out. “Rewrite twelve Greek myths as Broadway musicals. Write music for songs. Design and build all sets. Sew original costumes for each production.”

ACTOR 1 (MOM): “How long have you known about this assignment?” (trying not to scream.)

ACTOR 2 (GRASSHOPPER): “I don’t know,”

ACTOR 1: MORAL: There are plenty of things to say to calm a hopping mad Grasshopper Mom. “I don’t know” is not one of them. *******************

ACTOR 2: Pigeon Pie: Pigeon was a very good artist. But she had one very annoying habit. Every time she finished a painting she would show it and say, “It’s not very good” just to get someone to say,

ACTOR 1: “Oh no Pigeon. That’s very good.”

ACTOR 2: One day after she chased everyone else away with her annoying habit, she showed her painting to Saber-Toothed Tiger: (as Pigeon) “Oh, Look at my painting…. It’s not very good.”

ACTOR 1: Saber-Toothed Tiger licked his long saber teeth. (as Saber-Tooth) “Oh, no, Pigeon. That’s very good. I’m sure it will be perfect roasted, fried, or baked in a pie.”

ACTOR 2: Pigeon was puzzled. She had painted a sad-eyed clown. Then she noticed that Saber-Toothed Tiger wasn’t looking at the painting. But it was too late and the end of this fable is too messy to even tell.

ACTOR 1: MORAL: Whatever looks like a pigeon and acts like a pigeon usually makes good pigeon pie. **********************

ACTOR 2: Little Walrus: Little Walrus’s mom told her to always tell the truth. One day the phone rang. Little Walrus was the only walrus home so she answered it:

ACTOR 2 (LITTLE WALRUS): “Hello?”

ACTOR 1 (WHALE): “Hello, Little Walrus. Is your mom home?”

ACTOR 2: (LITTLE WALRUS): No, She’s out having the hair taken off her lip.

ACTOR 1: MORAL: You should always tell the truth. But if your mom is out having the hair taken off her lip you might want to forget a few of the details. ***************************

ACTOR 2: Straw and Matches: It was the end of summer vacation. Straw had done everything he could think of. He was bored. So he went over to play with someone he had been warned to stay away from.

ACTOR 1 (STRAW): “Let’s play checkers,”

ACTOR 2 (MATCHES): “Okay, I’m the red ones. I get to move first. I get two moves and you get one,”

ACTOR 1 (STRAW): “Forget it. Let’s play ping-pong instead.

ACTOR 2 (MATCHES): “Okay. I get the good paddle. You stand on that side. I get to serve first, and you have to close one eye.”

ACTOR 1 (STRAW): “Never mind. Maybe we should just watch TV.”

ACTOR 2 (MATCHES): “Okay. You sit over there on the floor. I’ll sit on the couch. I get the remote and we have to watch my favorite video,”

ACTOR 1 (STRAW): “I think I hear my mom calling, “I’d better go.”

ACTOR 2: MORAL: Don’t play with Matches **************************

ACTOR 1: Elephant and Flea: As Elephant grew older, he also grew more responsible. One day he and Flea went to see a movie. They liked it so much that they saw it again and completely lost track of time.

ACTOR 2: (ELEPHANT): “Oh no” (checking his watch). “I was supposed to be home ten minutes ago. Rhinoceros is going to be furious. Do you have a quarter so I can call?” ACTOR 1 (FLEA); (Checking his pockets) “Nope. Spent all my money on popcorn.”

ACTOR 2: So Elephant didn’t call. When Elephant finally showed up, at Rhinoceros’s house, he was twenty minutes late, and she was furious.

ACTOR 1 (RHINO): “You could have at least called.”

ACTOR 2: MORAL: Elephants never forget, except sometimes. ********************

ACTOR 1: Piece of Toast and Fruit Loops: Piece of toast and Fruit Loops sat on the breakfast table arguing over who was loved the most.

ACTOR 2 (TOAST): “Of course everyone loves toast the most. I’m half of eggs and toast. I’m all the toast in French toast. I am the toast with the most. Who could not love me?”

ACTOR 1 (FRUIT LOOPS): “I’m a good source of 11 essential vitamins and mineral containing 20% of the minimum daily requirements of vitamin C, Iron, Thiamin, riboflavin, Niacin, Vitamin B6, folate, vitamin B 12 and Zinc, based on a 2,000 calorie a day diet and a 1 cup serving size not including milk. I also have 1 gram of dietary fiber per serving and 12 grams of sugar, yellow dye #6, blue #1 and #2 and red #40. BHT has been added to preserve freshness.”

ACTOR 2: But while Fruit Loops was rattling off his nutrition facts. . . Mom had a cup of tea. . .

ACTOR 1 (TOAST): “Toast. . . Toast. . . toast. . . “ (getting cold) (As narrator) Dad drank coffee . . .

ACTOR 2 (FRUIT LOOPS): “Fruit loops. . . Fruit loops. . . Fruit loops. . .” (getting soggy) (As narrator) Son ate a doughnut

ACTOR 1 (TOAST): “Toast. . . Toast. . . toast. . . “ (getting colder) (As narrator) Daughter said she’d get a bagel on the way to school.

ACTOR 2 (FRUIT LOOPS): “Fruit loops. . . Fruit loops. . . Fruit loops. . .” (getting soggier)

ACTOR 1: MORAL: Breakfast is the most important meal of the day

ACTOR 2: Hand, Foot and Tongue: One evening at dinner, Hand, Foot and Tongue got into a heated argument over who had the toughest job.

ACTOR 1 (HAND): “I have the toughest job. Every day I work from sunup to sundown. I button shirts. I tie shoes. I hold the spoon and fork to feed all of us. I have to be strong enough to punch with a fist, and gentle enough to pat a baby. I definitely have the toughest job.”

ACTOR 2 (FOOT): “No you don’t. I have the toughest job. Every day I have to carry all of you. And I’m not complaining or anything, but I usually have to do it in the dark – stuck in a smelly sock and laced in a shoe. I have the toughest job.”

ACTOR 1 (TONGUE): “I am a fleshy muscular organ attached to the floor of the mouth. I help in both speech and taste. I start the process of digestion by moving food into position to get ripped and mashed and crushed and smashed to little bits by the teeth. Then I cover the little food bits with saliva and shape them into slimy blobs of guck that I push down the throat and . . . . “

ACTOR 2 (FOOT): “Disgusting”

ACTOR 1 (HAND): “That’s sick”

ACTOR 2: MORAL: There are some things we don’t talk about at the dinner table. ************

ACTOR 1: What fun! I should write some of those myself, you are probably thinking . . . But before you get started, it just occurred to me that you might want to know one more little bit about Aesop.

ACTOR 2: Aesop used to tell this one fable about a real bossy jerk “Lion” who ruled a city. When the real bossy jerk guy who ruled Aesop’s city heard his fable, he didn’t like it. So he had Aesop thrown off a cliff.

ACTOR 1: MORAL: If you are planning to write fables, don’t forget to change the people into animals

ACTOR 2: and avoid places with high cliffs.
```

---

## IC-0542: The Stinky Cheese Man & Other Fairly Stupid Tales

- Title: The Stinky Cheese Man & Other Fairly Stupid Tales
- Author (byline): Jon Scieska
- Work: Not specified
- Publisher: Viking Press
- Publication date as stated: May 2002
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 1, ACTOR 2, JACK THE NARRATOR, TOWNSMAN, LITTLE OLD WOMAN, STINKY CHEESE MAN, LITTLE OLD MAN, COW, LITTLE GIRL, LITTLE BOY, FOX, FROG, PRINCESS, LITTLE RED, WOLF, QUEEN, LITTLE MAN, CINDERELLA, GIANT
- Teaser before the introduction: Yes
- Spoken words (computed): 1833
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jon Scieska
ISBN: 978-0670035694
Publisher: Viking Press
Date (Month/Year): May 2002
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: A long time ago, people used to tell magical stories of wonder and enchantment. Those stories were called Fairy Tales.

ACTOR 2: What we’ll be presenting today are NOT fairy tales.

ACTOR 1: They are ALMOST Fairy Tales, but not quite.

TOGETHER: The Stinky Cheese Man and Other Fairly Stupid Tales by Jon Scieska
```

### Performance text (classify this)

```text
Suggested Roles

ACTOR 1: Jack the Narrator; Little Old Man, Cow, Little Girl, Little Boy, Fox, Princess in the Frog Prince story, Little Man.

ACTOR 2: Ducklings, Townsman, Little Old Woman, Stinky Cheese Man, Frog, Little Red, Wolf, Queen, Princess from the Prince and the Bowling Ball story, Cinderella and the Giant

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

JACK THE NARRATOR: Once upon a time there was a mother duck and a father duck who had seven baby ducklings. Six of them were regular-looking ducklings. (Actor 2 portrays six quacks – one for each regular looking duckling) The seventh was a really ugly duckling.

(Actor 2 portrays the ugly QUERK of a very ugly duckling) Everyone used to say,

TOWNSMAN: What a nice-looking bunch of ducklings – all except that one. Boy he’s really ugly.

JACK THE NARRATOR: The really ugly duckling heard these people, but he didn’t care. He knew that one day he would probably grow up to be a swan and be bigger and look better than anything in the pond. . . Well, as it turned out, he was just a really ugly duckling. And he grew up to be just a really ugly duck. [Actor 2 makes the ugliest duck face possible – QWERK!] The End

JACK THE NARRATOR: Once upon a time there was a little old woman and a little old man who lived together in a little old house. They were lonely. So, the little old lady decided to make a man out of stinky cheese. (Actor 2 pantomimes the making of a Stinky Cheese Man) She gave him a piece of bacon for a mouth and two olives for eyes and put him in the oven to cook. When she opened the oven to see if he was done, the smell knocked her back.

LITTLE OLD WOMAN: Phew! What is that terrible smell?”

JACK THE NARRATOR: The Stinky Cheese Man hopped (Actor 2 hops) out of the oven and ran out the door calling . . .

STINKY CHEESE MAN: (while running) Run run run as fast as you can. You can’t catch me, I’m the Stinky Cheese Man!

LITTLE OLD MAN: (sniffing the air and making a face) I’m not really very hungry,

LITTLE OLD WOMAN: (holding her nose) I’m not really all that lonely.

JACK THE NARRATOR: So, they didn’t chase the Stinky Cheese Man. The Stinky Cheese Man ran and ran until he met a cow eating grass in a field.

COW: (chewing cud, abruptly stops and speaks with her mouth full) Wow! What’s that awful smell?

STINKY CHEESE MAN: (hands on hips) I’ve run away from a little old lady and a little old man and I can run away from you too, I can. (while running) Run run run as fast as you can. You can’t catch me, I’m the Stinky Cheese Man!

COW: (sniffing the air again) I’ll bet you could give someone two or three stomachaches, I think I’ll just eat weeds. (returns to eating)

JACK THE NARRATOR: So the cow didn’t chase the Stinky Cheese Man either. The Stinky Cheese Man ran and ran until he met some kids playing outside school.

LITTLE GIRL: (waving her hand in front of her face) Gross. What’s that nasty smell?

STINKY CHEESE MAN: (dancing around the children, maybe even farting in their general direction) I’ve run away from a little old lady, and a little old man, and a cow, and I can run away from you too, I can. (while running) Run run run as fast as you can. You can’t catch me, I’m the Stinky Cheese Man!

LITTLE BOY: (sniffing the air) If we catch him, our teacher will probably make us eat him. Let’s get out of here.

JACK THE NARRATOR: So, the kids didn’t chase the Stinky Cheese Man either. By and by the Stinky Cheese Man came to a river with no bridge.

STINKY CHEESE MAN: How will I ever cross this river? It’s too big to jump, and if I try to swim across I’ll probably fall apart.

JACK THE NARRATOR: Just then the sly fox (who shows up in a lot of stories like these) poked his head out of the bushes.

FOX: Why, just hop on my back and I’ll carry you across, Stinky Cheese Man.

STINKY CHEESE MAN: How do I know you won’t eat me?

FOX: Trust me.

JACK THE NARRATOR: So the Stinky Cheese Man hoped on the fox’s back. The fox swam to the middle of the river

FOX: (coughing, gagging, sneezing) Oh, man! What is that funky smell?

JACK THE NARRATOR: and the Stinky Cheese Man flew off his back and into the river where he fell apart. The End *******

JACK THE NARRATOR: Once upon a time there was a frog. One day when he was sitting on his lily pad, he saw a beautiful princess sitting by the pond. He hopped (Actor 2 hops) in the water, swam (Actor 2 swims) over to her, and poked his head out of the weeds (Actor 2 pokes head up and tongue darts out a couple of times).

FROG: (in a most sad and pathetic voice) Pardon me, O beautiful princess, I wonder if you could help me.

JACK THE NARRATOR: The princess was about to jump up and run, but she felt sorry for the frog with the sad and pathetic voice.

PRINCESS: (hesitantly) What can I do to help you, little frog?

FROG: Well, I’m not really a frog, but a handsome prince who was turned into a frog by a wicked witch’s spell. And the spell can only be broken by the kiss of a beautiful princess.

JACK THE NARRATOR: The princess thought about this for a second (thinking pose), then lifted (lifting) the frog from the pond and kissed him (kisses frog). (Long pause while nothing happens)

FROG: (Laughing and jumping back into the water) I was just kidding!

JACK THE NARRATOR: and the princess wiped (wiping) the frog slime off her lips. The End *******

JACK THE NARRATOR: This next story is even better than the last three. See, it’s about this girl who runs very fast and always wears red running shorts. That’s where her name comes from, get it? So anyway, this girl is running to her granny’s house when she meets a wolf. He tricks her into taking the long way while he takes the shortcut. Now this is the good part because Red runs so fast that she beats the wolf to granny’s house. He knocks on the door (knocks). Red answers it. And guess what she says? (in Little Red Voice) “My, what slow feet you have.” And that’s it. The end. Is that great or what? So sit back, relax and enjoy – “Little Red Running Shorts. . . . (Long pause; he gestures for actors to take the stage) And now, like I already said – Little Red Running Shorts!

LITTLE RED: (in a hateful and sarcastic voice) You just told the whole story. We’re not going to tell it again.

JACK THE NARRATOR: You can’t say that. You have to start with ‘Once upon a time’.

WOLF: (also sarcastic and disgusted) No way. You blew it.

JACK THE NARRATOR: (To Little Red and Wolf) But you guys are next. Look at the title (gestures as if there is a large sign behind him) – ‘Little Red Running Shorts.’ That’s you.

LITTLE RED: Let’s go, Wolf. We’re out of here.

JACK THE NARRATOR: Wait. You can’t do this. WAIT! The End *******

JACK THE NARRATOR: Once upon a time there was a Prince. And this Prince’s dad and mom (the King and Queen) somehow got it into their royal heads that no Princess would be good enough for their boy unless she could feel a pea through one hundred mattresses. So, it should come as no surprise that the Prince had a very hard time finding a Princess. Every time he met a nice girl, his mom and dad would pile one hundred mattresses on top of a pea and then invite her to sleep over. When the Princess came down for breakfast, the Queen would ask

QUEEN: How did you sleep, dear?

PRINCESS: (politely) Fine, thank you.

JACK THE NARRATOR: And the King would show her the door. Now this went on for three years. And of course nobody ever felt the pea under one hundred mattresses. Then one day the Prince met the girl of his dreams. He decided he better do something out about it. That night, before the Princess went to bed, the Prince slipped his bowling ball under the one hundred mattresses (Actor 2 pantomimes this action). When the Princess came down for breakfast the next morning, the Queen asked,

QUEEN: How did you sleep, dear?

PRINCESS: This might sound odd, but I think you need another mattress. I felt like I was sleeping on a lump as big as a bowling ball.

JACK THE NARRATOR: The King and Queen were satisfied. The Prince and Princess were married. And everyone lived happily, though maybe not completely honestly, ever after. The End *******

JACK THE NARRATOR: Once upon a time there was a beautiful girl named Cinderella who lived with her wicked stepmother and two ugly stepsisters. These step-relatives were not only wicked and ugly --- they also made Cinderella clean the house every day (Actor 2 pantomimes cleaning the floors). One day the local prince announced that he was holding a fabulous ball at his castle. Everyone was invited. The stepmother and stepsisters got all dressed up to go. But, as usual, they made Cinderella clean the house, so she didn’t have time to get ready. After the stepmother and stepsisters left for the ball, Cinderella sat down and began to cry (Actor 2 Cries). Just then a little man appeared.

LITTLE MAN: Please don’t cry. I can help you spin straw into gold.

CINDERELLA: I don’t think that will do me much good. I need a fancy dress, glass slippers, and a coach.

LITTLE MAN: Would you like to try to guess my name?

CINDERELLA: No, Not really.

LITTLE MAN: Come on, Do you think it’s Chester? If you don’t have a dress, it doesn’t really matter. . . Oh, just guess a name, any name.

CINDERELLA: I’m not supposed to talk to strangers.

JACK THE NARRATOR: Then she closed the door and left the little man standing outside screaming.

LITTLE MAN: RUMPELSTILTSKIN! RUMPELSTILTSKIN! RUMPELSTILTSKIN!

JACK THE NARRATOR: When the stepmother and stepsisters got home from the ball, Cinderella told them about the strange little man. They still made her clean the house. And meaner still, they changed her name to Cinderumpelstiltskin. The End *******

JACK THE NARRATOR: Now it’s time for the best story – my story. Because once upon a time I traded our last cow for three magic beans and . . . hey, Giant. What are you doing down here? You’re wrecking my whole story.

GIANT: I DON’T LIKE THAT STORY. YOU ALWAYS TRICK ME.

JACK THE NARRATOR: (to Giant) That’s the best part.

GIANT: FEE FI FUM FORY. I HAVE MADE MY OWN STORY.

JACK THE NARRATOR: (to Giant) Great rhyme, Giant. And I’m sure your story is just as good. But there’s no room for it. So why don’t you climb back up the beanstalk. I’ll be up in a few minutes to steal your gold and your singing harp.

GIANT: I’LL GRIND YOUR BONES TO MAKE MY BREAD.

JACK THE NARRATOR: (to Giant) I knew you’d understand.

GIANT: I WILL [TELL] MY STORY NOW . . . The End of the evil Stepmother said, “I’ll HUFF and SNUFF and give you three wishes.” The beast changed into seven dwarves happily ever after, for a spell had been cast by a Wicked Witch once upon a time.

JACK THE NARRATOR: That’s your story? You’ve got to be kidding. That’s not a Fairly Stupid Tale. That’s an Incredibly Stupid Tale. That’s an Unbelievably Stupid Tale. That is the Most Stupid Tale I Ever – awwwwk!” (Giant grabs Jack; holds him tight in one fist . . . Jack hesitantly begins to tell his story) Once upon a time there was a Giant.

GIANT: (squeezing Jack tightly) TELL ME A BETTER STORY OR I WILL GRIND YOUR BONES TO MAKE MY BREAD. AND WHEN YOUR STORY IS FINISHED, I WILL GRIND YOUR BONES TO MAKE MY BREAD ANYWAY! (an ugly laugh)

JACK THE NARRATOR: (thinking aloud to audience) He’ll kill me if I do. He’ll kill me if I don’t. There’s only one way to get out of this. . . (clears his throat and beings the story) Once upon a time there was a Giant.

GIANT: (squeezing Jack tightly) TELL ME A BETTER STORY OR I WILL GRIND YOUR BONES TO MAKE MY BREAD. AND WHEN YOUR STORY IS FINISHED, I WILL GRIND YOUR BONES TO MAKE MY BREAD ANYWAY! (an ugly laugh)

JACK THE NARRATOR: (thinking aloud to audience) He’ll kill me if I do. He’ll kill me if I don’t. There’s only one way to get out of this. . . (clears his throat and beings the story) Once upon a time there was a Giant.

GIANT: (squeezing Jack tightly) TELL ME A BETTER STORY OR I WILL GRIND YOUR BONES TO MAKE MY BREAD. AND WHEN YOUR STORY IS FINISHED, I WILL GRIND YOUR BONES TO MAKE MY BREAD ANYWAY! (an ugly laugh)

JACK THE NARRATOR: (thinking aloud to audience) He’ll kill me if I do. He’ll kill me if I don’t. There’s only one way to get out of this. . . (clears his throat and beings the story) Once upon a time there was a Giant. . .

(sing softly and fade out to silence) This is the story that doesn’t end . . . it just goes on and on my friends . . . Some people started *listening* not knowing what it was and they’ll continue *listening* forever just because . . . ] The End
```

---

## IC-0543: Sweet Tooth

- Title: Sweet Tooth
- Author (byline): Margi Palatini
- Work: Not specified
- Publisher: Simon and Schuster
- Publication date as stated: Aug 2004
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 1, ACTOR 2, NARRATOR, SWEET TOOTH, STEWART, MOTHER, DAD, GRANDMOTHER, STUART, MRS. FINNEGAN, CROWD, MOTHER/DAD, SISTER, UMPIRE, BABY TEETH, CANINE TOOTH, WISDOM TOOTH, TOOTH FAIRY
- Teaser before the introduction: Yes
- Spoken words (computed): 1138
- Already set (do not supply): none

### Source block (context only)

```text
Author: Margi Palatini
ISBN: 978-0689851599
Publisher: Simon and Schuster
Date (Month/Year): Aug 2004
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Sweet Tooth ACTOR 2: by Margi Palatini
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested roles:

ACTOR 1: Narrator, Mother, Dad, Grandmother, Mrs. Finnegan, Crowd, Sister, Canine Tooth, Tooth Fairy

ACTOR 2: Sweet Tooth, Stewart

NARRATOR: This is Stewart. Your typical, average, everyday kid. Except for one thing.

SWEET TOOTH: Iii oo-er ere.

NARRATOR: Ahh, yes. There it is all right. The molar in the back. You're probably saying, "A tooth? What's the big deal about a tooth?" And ordinarily you would be correct. . . . But that is no ordinary tooth. Uh-uh. This is Stewart's sweet tooth. One nagging, annoying, demanding . . .

SWEET TOOTH: (Loudly) BLAH. BLAH. BLAH. ENOUGH WITH THE YAKKIN'. I NEED A CANDY BAR. NOW-OW!

NARRATOR: . . . very loud, sweet tooth.

.

SWEET TOOTH: "DOES IT HAVE THAT GOOEY STUFF IN THE MIDDLE? 'CAUSE IT'S GOT TO HAVE THAT GOOEY STUFF IN THE MID-DLE!"

STEWART: (Cramming a candy bar into his mouth, chewing loudly and gulping) There. Satisfied?

SWEET TOOTH: AHHHHH . . . SWEET!

NARRATOR: Yes, a tooth that wants what it wants, when it wants it . . . and lets everybody know it. Take, for example, two years ago at cousin Charlotte's wedding . . . Stewart was on his best behavior. His shoes were shined. Bowtie straight. Hands were spotless. Grandfather had just lifted his glass to toast the bride and groom when . . .

SWEET TOOTH: I'm fallin' asleep here! Come on. Move it along, Gramps. Cut the cake. Time to cut the cake. I want the end hunk with all that iiiiii-icing.

MOTHER: (through a gritted smile) I don't know him.

DAD: (under his breath) He doesn't belong to me.

GRANDMOTHER: (muttering) Who is that boy?

NARRATOR: Stewart wiped the pink rose from his lips.

STUART: It's The Sweet Tooth.

NARRATOR: It was not a pretty picture . . . The Tooth was no better behaved in school. Stewart had enough detention slips to wallpaper his room. Why, just two weeks ago in geography class . . .

MRS. FINNEGAN: Who can tell me the capital of North Dakota?”

SWEET TOOTH: (muffled) Jelly beans

NARRATOR: said a muffled voice from the back of the room.

MRS. FINNEGAN: Did you say something, Stewart?

SWEET TOOTH: Licorice.

MRS. FINNEGAN: Stewart, I'm afraid I can't hear your answer.

SWEET TOOTH: Lollipops.

MRS. FINNEGAN: You're going to have to speak up, Stewart.

SWEET TOOTH: Hey! I'm dying here for a couple of CHOCOLATE PEANUT BUTIER CUPS, OKAY?!

NARRATOR: Detention slip number 432.

STEWART: (as he is lead away to the principal’s office) But, I'm telling you, it's not me, It's The Tooth! *******************

NARRATOR: The movies? You don't really want to go there, do you? . . . Not with Stewart, anyway.

SWEET TOOTH: Would somebody pass the yummy yummys, already?!

CROWD: SHHHHHHHHHHHHH!

STEWART: (chewing) Don't look at me . . . It's The Tooth.

NARRATOR: And of course there was the unforgettable "Easter Basket Mishap." Now that was really ugly. That Sunday A.M. the family awoke to find jelly beans littering the living room. Marshmallow chicks were missing. The trail of crumpled yellow foil wrappers led to one person, and one person only.

MOTHER/DAD: (disappointed) Ooooh, Stewart.

SISTER: (whimpering and closing her eyes) I can't look.

STEWART: (moaning and rubbing his belly-aching stomach) Those chocolate bunnies never had a chance . . . It was The Tooth.

SWEET TOOTH: HEY! CAN WE STOP GOING DOWN MEMORY LANE HERE AND OPEN UP THAT BAG OF COOKIES?

STEWART: That's it. I've had enough!

SWEET TOOTH: ENOUGH? I HAVEN'T EVEN HAD ONE.

STEWART: (shouting) No more cookies! No more candy. No more cake. No more nothing!

SWEET TOOTH: That's no more anything. And . . . WHO DO YOU THINK YOU'RE KIDDING, KID? Bring on those chocolate chips!"

NARRATOR: Stewart sighed. What choice did he have? He was a boy with one big Sweet Tooth. He tore open the bag. He grabbed one, then two-three-four cookies. He opened his mouth.

SWEET TOOTH: (shouting) COME TO PAPA!

NARRATOR: Stewart stopped.

SWEET TOOTH: What are you waiting for, kid? Come on. Cookie. Cookie. Cookie. Cookie.

NARRATOR: Stewart dropped the cookies. But . . . . not in his mouth.

STEWART: (determined) It's over, Tooth. I’m cutting you off. Starting right now. It's cold turkey.

SWEET TOOTH: Cold turkey? Yee-ech! I hate cold turkey . . . unless you add a little cranberry sauce,

STEWART: Didn't you hear me, Tooth? I said it's over. From now on there's nothing for you but a . . . a . . . a . . . (large gulp) Healthy diet.

SWEET TOOTH: (wailing) Healthy? Kid, say you don't mean it.

NARRATOR: But Stewart meant it, all right. He meant every word. Yes, it was trying. Yes, it was difficult. Okay, it was darn near impossible. But Stewart stayed strong. For The Tooth it was a different story.

SWEET TOOTH: PEAS? YOU'RE GIVING ME PEAS? LITILE DRY GREEN VEGGIE MARBLES? Broccoli? You're feeding me a shrub? THAT'S NOT GOING TO DO IT. DESSERT! WHERE'S DESSERT? I'm begging you. WHEN DO WE GET TO THE GOOD STUFF?"

STEWART: (putting his hands over his ears) I can't hear you.

NARRATOR: Strong. He stayed strong.

SWEET TOOTH: Just one eensy-teensy CHOCOLATE-COVERED PEANUT before hitting the sack. How about it? . . . A nosh. A nibble. A breath mint. Somethin'!

STEWART: (turning out the light) Forget it.

NARRATOR: Strong. Strong.

SWEET TOOTH: (at breakfast the next morning as Stewart eats his cereal) COME ON. WHADDAYA SAY? ONE SPOONFUL OF SUGAR.

NARRATOR: Stewart shook his head.

SWEET TOOTH: (losing his grip) A DROP OF CHOCOLATE MILK. One measly little crumb-bun crumb.

STEWART: No way.

NARRATOR: Very strong.

SWEET TOOTH: (shouting) HEY, WATCH THAT TOOTHBRUSH! AND KEEP THAT TONGUE OF YOURS ON THE OTHER SIDE OF YOUR MOUTH. TRYIN' TO WIGGLE ME OUT OF HERE, HUH? Well, I'm not going, kid. I'm not going anywhere! Do you hear me? . . . Do you hear me?"

NARRATOR: Stewart brushed. Flossed. Gargled.

SWEET TOOTH: (moaning weakly) U-u-ugh He's not hearing me . . . I'll get you for this, kid.

NARRATOR: Stewart smiled. He was winning. Oh yes, he was winning. Three days passed. The Tooth was quiet. Very quiet. Almost too quiet. But Stewart wasn't thinking "tooth." He was thinking baseball. It was the biggest game of the season. Bottom of the ninth. Stewart was at the plate. Runners were on second and third. Two outs. Two strikes. The crowd was on their feet. The game was on the line. Stewart's team was down by one run. The pitcher went into his windup. There was a hush from the stands. A big fat fastball was heading for the plate. It was all up to Stewart. And then . . .

SWEET TOOTH: BOY, COULD I GO FOR A HUNK OF BUBBLE GUM RIGHT NOW!

NARRATOR: Swing! Swish!

SWEET TOOTH: Heh-heh-heh.

UMPIRE: (yelling) Strike three! Y'er out!

SWEET TOOTH: Gotcha! Now go get me some goodies!

STEWART: (mumbling as he drops the bat) I'll get you goodies.

NARRATOR: Home he marched. Into the kitchen. Straight for the refrigerator. He yanked open the door. Rustled through the vegetable bin. He flung lettuce. He tossed tomatoes. He hurled a head of cauliflower. And then he pulled out . . . .a carrot. That's right. A carrot.

STEWART: (defiantly as he lifts the carrot above his head) It's over for you, Tooth.

SISTER: (wide-eyed) What are you going to do with that?

NARRATOR: Stewart grinned. He opened his mouth wide. Very wide.

SWEET TOOTH: KID! NO! NOT THE CARROT! NOT THE CARROT!"

STEWART: (shouting) Yes. The carrot!

SWEET TOOTH: No, kid, no!

SISTER: (covering her eyes) Am I too young to be watching this?

NARRATOR: Closer. Closer. Closer. And then . . . . CR-CR-CRUNCH.

SWEET TOOTH: Ahhh-ahh-ahhhhh . . . So long, sweet world! . . . What a way to go . . . Done in by an orange veggie.

NARRATOR: Stewart rubbed his jaw. He stared at the carrot . . . (the tooth is in his hand) and The Tooth. It was over.

SISTER: What's going to happen to it?

NARRATOR: Stewart placed the molar under his pillow, then looked at his sister.

STEWART: (smiling) Who knows? That's the tooth fairy's problem now.

**************** [In the Tooth Fairy’s Bag of Teeth] ****************

BABY TEETH: WAH, WAH, WAH!

CANINE TOOTH: WOOF!

WISDOM TOOTH: Please be quiet. I’m trying to read.

SWEET TOOTH: Pipe down, wise guy! What does a sweet tooth have to do to get an ice-cream sundae around here? With hot fudge! And throw some sprinkles on it while you’re at it.

TOOTH FAIRY: ROTTEN TEETH!
```

---

## IC-0544: The Tale of Despereaux

- Title: The Tale of Despereaux
- Author (byline): Kate DiCamillo
- Work: Not specified
- Publisher: Candlewick
- Publication date as stated: April 2006
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, MOTHER, BROTHER, FATHER, AUNT, UNCLE, DESPEREAUX, PEA, KING, BROTHER MOUSE, LESTER, ANTOINETTE, HM, MOUSE, ROSCURO, QUEEN, COOK, MIG, RAT
- Teaser before the introduction: Yes
- Spoken words (computed): 1760
- Already set (do not supply): none

### Source block (context only)

```text
Author: Kate DiCamillo
ISBN: 978-0763625290
Publisher: Candlewick
Date (Month/Year): April 2006
```

### Introduction (context only: never use it for content warnings)

```text
The Tale of Dexpereaux by Kate DiCamillo
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

NARRATOR: This story begins within the walls of a castle, with the birth of a mouse. The only one of his litter to be born alive.

MOTHER: Just the one. It is such the disappointment. I will name this mouse Despereaux, for all the sadness, for the many despairs in this place. Now, where is my mirror?

NARRATOR: The other, older mice children gathered around to stare.

BROTHER: Look, his eyes are open. They shouldn’t be open.

NARRATOR: Despereaux’s eyes should not have been open. But they were.

FATHER: He’ll be dead soon. He can’t live with his eyes open like that.

NARRATOR: But he did live. This is his story.

NARRATOR: Despereaux Tilling lived, but his existence was cause for much speculation in the mouse community.

AUNT: He’s the smallest mouse I’ve ever seen. No mouse has ever been this small.

UNCLE: Those are some big ears he’s got.

AUNT: They are obscenely large.

NARRATOR: Despereaux said nothing in defense of himself. Everything they said was true. And he was sickly. He coughed and sneezed so often that he carried a handkerchief in one paw at all times.

TRANSITION: Despereaux discovered a sound. The sound was music. King Phillip playing his guitar to his daughter, the Princess Pea. Hidden in a hole in the wall the mouse listened.

DESPEREAUX: Oh, it sounds like heaven. It smells like honey.

NARRATOR: Now, Despereaux did adhere to one of the most basic of all mice rules: Do not ever reveal yourself to humans. But…The music made him lose his head, and he was spied by the Princess Pea.

PEA: Oh, look, a mouse.

KING: That my dear Pea, is a bug, not a mouse.

PEA: No, no, it’s a mouse. I think he was listening to the music. Play something Papa.

KING: A king play music for a bug?

PEA: I told you, he’s a mouse.

KING: Oh, well, if it will make you happy, I will play music for a bug.

NARRATOR: Despereaux forgot all his fear. He only wanted to hear the music. The princess smiled at Despereaux, and Despereaux smiled back. The mouse fell in love.

TRANSITION: Despereaux’s brother happened to scurry past the princess’s room. He saw the princess touching the top of his brother’s head.

BROTHER MOUSE: He’s nuts! He’s a goner!

PEA: Papa, I am going to keep this mouse.

KING: A mouse? Mice are rodents. They are related to rats. You know of our own dark history with rats.

PEA: “But, he is not a rat. He’s a mouse.

KING: Put him down. Scat!

PEA: “Please, don’t be mean to him.

DESPEREAUX: My name is Despereaux! I honor you!

KING: Get out! Rodents know nothing of honor.

NARRATOR: Despereaux’s brother went off to tell his father the terrible news of what he had just seen.

LESTER: He simply cannot be my son.

ANTOINETTE: What do you mean he is not your son? That is a ridiculous statement. Why must you always make the ridiculous statements?

LESTER: Sitting at the foot of a human king. Unthinkable!

ANTOINETTE: Oh, so dramatic.

LESTER: I will call a special meeting of the Mouse Council. Together, we will decide what must be done.

ANTOINETTE: Oh, you and this council of the mouse. It is a waste of the time in my opinion.

TRANSITION: The mouse council gathered in a secret hole. The mice listened in horror while Despereaux’s father related the story of what Furlough had seen.

HM: Despereaux Tilling.

NARRATOR: Said the head mouse.

DESPEREAUX: Yes, sir.

HM: We, the members of the Mouse Council have discussed you behavior. We will give you a chance to defend yourself against these rumors of your egregious acts. Did you or did you not sit at the foot of the human king?

DESPEREAUX: I did.

HM: Did you allow the girl human to touch you?

DESPEREAUX: I did, sir. Her name is Pea. But..

HM: Very well. We have no choice. You will die.

NARRATOR: Despereaux marveled at his own bravery. He admired his own defiance. And then, he fainted. Two mice came forward.

MOUSE: We will escort you to the dungeon.

ANTOINETTE: What will happen to him? What will happen to my baby?

MOUSE: The rats will eat him. (Antoinette swoons)

TRANSITION: Together the three mice traveled down. Despereaux was suddenly pushed from behind. It sent Despereaux flying down the stairs into the dungeon.

NARRATOR: As our story continues, we must go backward in time to the birth of a rat, a rat called Roscuro, a rat born in the darkness of the dungeon. Roscuro showed an abnormal interest in illumination. He was always on the lookout for light. His rat soul longed for it. The door to the dungeon was flung open and a brilliant shaft of light cut into the dark of the dungeon.

ROSCURO: Beautiful. I must see more light. I must go upstairs.

TRANSITION: Imagine having spent your life in a dungeon. One day, you step out of the dark and into a world of bright windows and polished floors.

ROSCURO: I will never leave. No, It is here that I belong.

NARRATOR: The rat waltzed from room to room until he found himself at the banquet hall. He looked and saw King Phillip, Queen Rosemary, the Princess Pea, and all the king’s men.

ROSCURO: Oh. Suffering is not the answer. Light is the answer.

NARRATOR: Roscuro flung himself onto the lowest branch of the chandelier. The Princess Pea spotted him.

PEA: A rat is hanging from the chandelier!

ROSCURO: Rat….

NARRATOR: It became clear that it was an extremely distasteful syllable. This revelation hit Roscuro with such a force, that it made him lose his grip on the chandelier. The rat fell. Right into the queen’s bowl of soup.

PEA: See? It is a rat. He is in Mama’s soup!

NARRATOR: In the spirit of honesty, I must utter a difficult and unsavory truth: Rats are not beautiful creatures.

QUEEN: Nneiggghhhiiinnnnkkkkk! There is a rat in my soup!

NARRATOR: The queen was a simple soul and always had done nothing but state the overly obvious. She died as she lived. Soup was outlawed in the Kingdom of Dor.

ROSCURO: I will make the princess suffer for how she looked at me. (SCENE BREAKE)

COOK: This is what you do. You take the tray of food down to the dungeon, wait for the man to eat the food, and then you bring the tray back up. Do you think you can manage that?

NARRATOR: Said Cook.

MIG: Aye, I reckon so.

NARRATOR: Said the serving girl, Mig.

COOK: I’m sure you’ll find a way to bungle it.

NARRATOR: Mig went happily down the twisting stairs.

MIG: I ain’t the Princess Pea / But someday I will be, / The Pea, ha-hee Someday, I will be.

ROSCURO: May I detain you for a moment? (Mig looks around) Down here.

MIG: You’re a rat ain’t you?

ROSCURO: There is no need to panic. How do you do.

MIG: A rat with manners.

ROSCURO: Allow me to introduce myself. I am Roscuro. Am I right in ascertaining that you have aspirations?

MIG: What?

ROSCURO: Aspirations, my dear, are those things that would make a serving girl wish to be a princess.

MIG: A princess is exactly what I want to be.

ROSCURO: May I illustrate for you how we can make your dream a reality?

NARRATOR: Neither noticed as a napkin on the tray moved, nor did they hear the small mouse like noises of outrage that issued from that napkin as Roscuro went on unfolding his diabolical plan. Mig, after her conversation with Roscuro, carried the tray into the kitchen. Despereaux tumbled out of the napkin.

COOK: Kill him!

NARRATOR: Shouted Cook.

MIG: (chop) I missed him. I got the little meecy’s tail, though.

COOK: So? What good will that do us when the rest of him has disappeared into the pantry?

NARRATOR: Despereaux cried for what he had lost. But he also cried because he was happy. He was out of the dungeon just in time to save the Princess Pea from the terrible fate that the rat had planned for her.

TRANSITION: Roscuro put his terrible plan into effect. The serving girl Mig climbed the stairs to the princess‘s room. In her pockets were the rat and a knife.

ROSCURO: Do I need to review with you again our plan?

MIG: I got it straight right here in my head.

ROSCURO: How comforting.

MIG: We go into the princess’s room and I will wake her up and say “you must come with me.” We take her to the deep downs and we gives me some lessons in how to be a princess and when we is all done studding up, I gets to be princess!

NARRATOR: The sun rose and Despereaux awoke. But he awoke too late. The princess was gone. Having heard Roscuro’s plan, Despereaux knew that the princess was hidden in the dungeon. So the small mouse slipped out of the pantry. Desperaux: “I will be the knight in shining armor. It has to be me.

COOK: A mouse! For the first time, I am glad to see a mouse. A mouse is not a king’s man here to punish me for making soup. A mouse. A mouse with a needle tied around his waist. Ho-hee. That is soup you are smelling.

NARRATOR: She took a saucer and spooned some soup into it and set it on the floor. Oh, it was lovely. He drank the soup and when he stepped out of the saucer, his whiskers dripping.

COOK: You must want more.

DESPEREAUX: I don’t have time. I’m on my way to the dungeon to save the princess.

COOK: Well don’t let me stand in your way.

TRANSITION: Despereaux stood at the top of the dungeon.

DESPEREAUX: “Oh my.”

NARRATOR: `But his heart was full of love for the princess and Despereaux felt brave and strong.

RAT: Welcome, welcome. You are armed. How charming. I surrender!

DESPEREAUX: I don’t want to hurt you. I’m… I am on a quest to save the princess.

RAT: How inspiring. What if I told you that I that I could take you directly to her?

DESPEREAUX: But why? You are a. . .

RAT: A rat, yes. Come, come. I will lead you to your princess. I promise. (Scene Break)

DESPEREAUX: Princess! Princess, I have come to save you!

PEA: Despereaux.

NARRATOR: But Roscuro, baring his teeth, blocked the mouse’s way.

MIG: Don’t worry, princess, I will save the meecy. (Chop) Whoopsie

NARRATOR: Roscuro turned to look at where his tail had been and Despereaux drew his needle and placed the sharp tip right where the rat’s heart should be.

DESPEREAUX: Don’t move.

ROSCURO: Ha…what is that smell? There’s something…Soup.

PEA: Roscuro, …would you like some soup.

ROSCURO: Don’t torment me.

PEA: I promise you that if you lead us out of here, I will get Cook to make you some soup.

ROSCURO: Soup?

PEA: Yes. Truly I promise. Let’s go upstairs. Let’s eat some soup.

NARRATOR: Imagine a king and princess, serving girl and a rat, all gathered in a banquet hall. Sitting in the place of honor, is a very small mouse with big ears. Peeking out from behind a curtain, are mice.

ANTOINETTE: He lives, he lives!
```

---

## IC-0545: Tape

- Title: Tape
- Author (byline): Jose Rivera
- Work: Humana Festival 1993: The Complete Play (Pg 211-218)
- Publisher: Smith and Kraus Publishers
- Publication date as stated: June 1993
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: PERSON, ATTENDANT, VOICE
- Teaser before the introduction: Yes
- Spoken words (computed): 924
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jose Rivera
Book: Humana Festival 1993: The Complete Play (Pg 211-218)
ISBN: 978-1880399378
Publisher: Smith and Kraus Publishers
Date (Month/Year): June 1993
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Life after death -- Why all the interest?

ACTOR 2: With the Baby Boom generation in their 60’s and 70’s, suddenly the reality of death is upon us in a personal way.

ACTOR 1: Too often the subject of death is addressed with goofy speculation, close-minded stubbornness, or outright fear and avoidance.

ACTOR 2: So, let's bypass the "Death for Dummies" approach and take a deeper intellectual look at death to better understand the important role it plays in our lives...

ACTOR 1: and especially what it can teach us about how to live.

ACTOR 2: Written as if human culture were the subject of fairy tales told by giants, this selection makes a statement about Karma and our human perception of the afterlife.

TOGETHER: Tape by Jose Rivera
```

### Performance text (classify this)

```text
A small dark room. No windows. One door. A PERSON is being led in by an ATTENDANT. On the table is a large reel-to-reel tape recorder, a glass of water, a pitcher of water.

PERSON: (Pg 211-218) It’s dark in here.

ATTENDANT: I’m sorry.

PERSON: No, I know it’s not your fault.

ATTENDANT: I’m afraid those lights . . .

PERSON: I guess, what does it matter now?

ATTENDANT: . . . not very bright

PERSON: Who care, really?

ATTENDANT: We don’t want to cause you any undue suffering. If it’s too dark in here for you, I’ll make sure one of the other attendants replaces the light bulb.

PERSON: (looks at the ATTENDANT) Any “undue suffering”?

ATTENDANT: That’s right.

PERSON: (looks at the room) Is this where I’ll be?

ATTENDANT: That’s right.

PERSON: Will you be outside?

ATTENDANT: Yes.

PERSON: The entire time?

ATTENDANT: the entire time.

PERSON: Is it boring?

ATTENDANT: (As if he/she hadn’t heard) I’m sorry?

PERSON: Is it boring? You know. Waiting outside all the time.

ATTENDANT: (Soft smile) It’s my job. It’s what I do.

PERSON: Of course. (Beat) Will I get anything to eat or drink?

ATTENDANT: Well, we’re not really set up for that. We don’t have what you’d call a kitchen. But we can send out for things. Little things. Cold food.

PERSON: I understand.

ATTENDANT: Soft drinks.

PERSON: (Hopefully) Beer?

ATTENDANT: I’m afraid not.

PERSON: Not even on special occasions like my birthday?

ATTENDANT: (Thinking) I guess maybe on your birthday.

PERSON: (Truly appreciative) Great. Thanks. (Beat)

ATTENDANT: Do you have any more questions before we start? Because if you do, that’s okay. It’s okay to ask as many questions as you want. I’m sure you’re very curious. I’m sure you’d like to know as much as possible, so you can figure out how it all fits together and what it all means. So please ask. That’s why I’m here. Don’t worry about the time. We have a lot of time. (Beat)

PERSON: I don’t have any questions.

ATTENDANT: (Disappointed) Are you sure?

PERSON: There’s not much I really have to know is there? Really?

ATTENDANT: No, I guess not. I just thought . . .

PERSON: It’s okay. I appreciate it. (The ATTENDANT looks sad. The Person looks at the ATTENDANT and feels bad)

PERSON: Hey I’m sorry. I know it’s not your fault.

ATTENDANT: It’s all right.

PERSON: What’s your name anyway? Do you have a name?

ATTENDANT: Not really. It’s not allowed

PERSON: Really? Not allowed? Who says?

ATTENDANT: The rules say.

PERSON: Have you actually seen these rules? Are they in writing?

ATTENDANT: Oh yes. There’s a long and extensive training course.

PERSON: (Surprised) There is?

ATTENDANT: Oh yes. It’s quite rigorous.

PERSON: Imagine that.

ATTENDANT: You have to be a little bit of everything. Confidant, confessor, friend, stern taskmaster. Guide.

PERSON: I guess that would take time.

ATTENDANT: My teachers were all quite strong and capable. They really pushed me. I was grateful. I knew I had been chosen for something unique and exciting. Something significant. I didn’t mind the hard work and sleepless nights.

PERSON: (Surprised) Oh? You sleep?

ATTENDANT: (Smiles) When I can. (Beat)

PERSON: Do you dream? (Beat)

ATTENDANT: No. (Beat) That’s not allowed. (Beat)

PERSON: I’m sorry.

ATTENDANT: No. It’s something you get used to.

PERSON: (Trying to be chummy) I know I went years and years without being able to remember one single dream I had. It really scared the *crap* out of me when I was ten and . . .

ATTENDANT: I know.

PERSON: I’m sorry.

ATTENDANT: I said I know. I know that story. When you were ten.

PERSON: Oh. Yeah. I guess you would know everything. Every story.

ATTENDANT: (Apologetic) It’s part of the training.

PERSON: I figured (A long uncomfortable silence)

ATTENDANT: (Softly) Have you ever operated a reel-to-reel tape recorder before?

PERSON: (Suddenly terrified) No I haven’t. I mean – no.

ATTENDANT: It’s not hard.

PERSON: I, uhm, these things were pretty obsolete by the time I was old enough to afford stereo equipment, you know. I got into cassettes and, later, CDs, but never one of these jobbies.

ATTENDANT: It’s not hard. (Demonstrates) On here. Off here. Play. Pause. Rewind.

PERSON: (Surprised) Rewind?

ATTENDANT: In some cases the quality of the recording is so poor . . . you’ll want to rewind it until you understand.

PERSON: No fast forward?

ATTENDANT: No.

PERSON: (Getting progressively more frightened) It looks like a pretty good one. Sturdy. Very strong.

ATTENDANT: They get a lot of use.

PERSON: I bet. (Beat) Is this the only tape?

ATTENDANT: (Laughs out loud – then quickly stops) No

PERSON: I didn’t think so.

ATTENDANT: There are many more.

PERSON: How many? A lot?

ATTENDANT: There are then thousand boxes.

PERSON: Ten thousand?

ATTENDANT: I’m afraid so.

PERSON: Did I really . . . did I really lie that much?

ATTENDANT: I’m afraid you did.

PERSON: So . . . everyone goes into a room like this?

ATTENDANT: Exactly like this. There’s no differentiation. Everyone’s equal.

PERSON: For once.

ATTENDANT: What isn’t equal, of course, is the . . . amount of time you spend here. Listening.

PERSON: (Horror stricken) Oh, God.

ATTENDANT: (Part of the training) Listening, just to yourself. To your voice.

PERSON: I know.

ATTENDANT: Listening, word by word, to every lie you ever told while you were alive.

PERSON: Oh, God!

ATTENDANT: Every ugly lie to every person, every single time, every betrayal, every lying thought, every time you lied to yourself, deep in your mind, we were listening, we were recording, and it’s all in these tapes, ten thousand boxes of them, in your own words, one lie after the next, over and over, until we’re finished. So the amount of time varies. The amount of time you spend here all depends on how many lies you told. How many boxes of tapes we have to get through together.

PERSON: (Almost in tears) I’m sorry . . .

ATTENDANT: Too late.

PERSON: I said I’m sorry! I said I’m sorry! I said it a million times! What happened to forgiveness?! I don’t want to be here! I don’t want this! I don’t want to listen! I don’t want to hear myself! I didn’t mean to say the things I said! I don’t want to listen!

ATTENDANT: Yes, well. Neither did we. Neither did we.

(The ATTENDANT looks sadly at the PERSON. The ATTENDANT turns on the tape recorder, then leaves the room, leaving the PERSON all alone. From the depths of the machine comes a long-forgotten voice – The ATTENDANT should voice this line from off-stage)

VOICE: “Where have you been? Do you know I’ve been looking all over? Jesus Christ! I went to Manny’s! I went to the pharmacy! The school! I even called the police! Look at me, Jesus Christ, I’m shaking! Now look at me – look at me and tell me where the hell you were! Tell me right now!”
```

---

## IC-0546: The Three Swine of Most Small Stature

- Title: The Three Swine of Most Small Stature
- Author (byline): Lewy Olfson
- Work: Skits and Short Farces for Young Actors
- Publisher: Boston Plays, Inc.
- Publication date as stated: 1973
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: STAGE MANAGER, NUMBER ONE PIG, NUMBER TWO PIG, NUMBER THREE PIG, WOLF
- Teaser before the introduction: Yes
- Spoken words (computed): 1725
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lewy Olfson
Book: Skits and Short Farces for Young Actors
ISBN: 978-0823801503
Publisher: Boston Plays, Inc.
Date (Month/Year): 1973
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 2: By Lewy Olfson
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

NOTE: The acting should be highly stylized, with the actors pantomiming most of the action in
pseudo-Oriental fashion. STAGE MANAGER bows low to audience
One Actor should play the roles of STAGE MANAGER and NUMBER 2 PIG
One Actor should play the roles of NUMBER 1 and NUMBER 3 PIG
THE ROLE OF WOLF should be split between the actors depending on the PIG being addressed

STAGE MANAGER: O most revered audience, welcome to Imperial Theater of the Orient. I, Oriental Stage Manager, beg your humble attention. Wish to have your permission to introduce play. (Wish to introduce play even without your permission, since actors have been rehearsing for a whole week!) Play tells very ancient and honorable legend: legend of the Three Swine of Most Small Stature. Called in translation, “The Three Little Pigs.” Perhaps you have read legend already, in which case. feel free to nap during performance. However, must warn you that legend in English not so beautiful as legend in Chinese. In Chinese is very symbolic… very aesthetic. Also very hard to understand if you don’t speak Chinese! (Gong sounds offstage.) Ah, So! Signal means, “get this show on the road!”(Bows) The Three Swine of Most Small Stature! (He claps his.)

The three Pigs are dancing and skipping about.

STAGE MANAGER: Behold! A woodland glade in ancient China. Notice: only one tree for scenery. One tree suggests entire woodland. Very symbolic. Very aesthetic. (Claps hands. PIGS stop frolicking and stand in line.)Beg to introduce chief characters. (PIGS step forward and bow as their names are called.) Number One Pig. (He bows.) Number Two Pig. (He bows.) Number Three Pig. (He bows.) Play has one other character. We will introduce him later. For one thing, wish to build suspense. For another thing, he takes a long time to get into his costume. (The gong sounds.) Signal! Signal means: “Let play begin!”

NUMBER ONE PIG: Brother pigs, what a happy life we live here in ancient China.

NUMBER TWO PIG: You have spoken wisely, Number One Pig. Ours is a most carefree existence.

NUMBER THREE PIG: Nothing to do but sing and play, all day long.

NUMBER ONE PIG: Yes, fun is good. But when I spoke of pleasure, I meant also the pleasure of work. The pleasure of going to school. The pleasure of meeting challenges and pursuing honest toil.

NUMBER TWO PIG: What a party-pooper you are, Number One Pig! Number Three Pig and I don’t believe in all that work stuff.

NUMBER THREE PIG: Naw, we just want to dance and sing and have a good time all day long.

NUMBER ONE PIG: Foolish, foolish pigs! Listen to me, your elder brother. All play and no work make for great unhappiness!

NUMBER TWO PIG: Says who!

NUMBER ONE PIG: Old saying of Confucius. NUMBER TWO PIG (Disgusted): Ah, you and your high-flown ideas! Just because you went to college, you’re always showing off.

NUMBER THREE PIG: You used to be a regular guy, Number One Pig. But ever since you got your Ph.D. — in Pig Latin — have you been a grouch!

NUMBER ONE PIG: You may scoff at me now, my brothers. But one day you will see I am right. STAGE MANAGER (Rising, addressing audience): Number One Pig wasn’t exaggerating. He knew that summer could not last forever. Behold: Winter! (He hangs a giant snowflake cutout on the tree.) Cold, cold, cold winter — the worst winter in the history of China. Notice: Only one snowflake for scenery. very symbolic. very aesthetic.

NUMBER THREE PIG: Also very cheap.

STAGE MANAGER: Now came the time to work, just as Number One Pig had predicted.

NUMBER ONE PIG: My brothers, it is winter. We can no longer live out of doors. I think it is time to build a pagoda. NUMBER TWO PIG (Sarcastically): It’s really terrific to have a college graduate in the family. It’s been snowing for a month now, and it’s finally dawned on him to build us a house.

NUMBER THREE PIG: I was wondering when you were going to get around to it, Number One Pig. NUMBER ONE PIG (Smugly): But, my brothers, I am not going to build us a house. I am going to build me a house. You must build houses for yourselves.

NUMBER TWO PIG: Big deal. I guess we can build as good a house as you can if we want to.

NUMBER ONE PIG: We shall see. What will you build your house of, Number Three Pig?

NUMBER THREE PIG: I shall build my house of tatami mats. I know where I can get a real buy on some straw tatami mats, imported from Japan.

NUMBER ONE PIG: If I may say so, esteemed, honorable, and revered brother, it’s a stupid idea. I might call it tatami-rot!

NUMBER TWO PIG: Oink!

NUMBER ONE PIG: And what will you build your house of, Number Two Pig?

NUMBER TWO PIG: I shall build my house of chopsticks. I can get second-hand chopsticks free down at the Chinese restaurant.

NUMBER ONE PIG: House of straw! House of sticks! Is terrible architecture. NUMBER TWO PIG (Wagging his finger; brightly): But is symbolic!

NUMBER THREE PIG: (Likewise): Is aesthetic!

NUMBER ONE PIG: (Proudly): I shall build my house of bricks.

NUMBER TWO PIG: Bricks! But bricks cost a fortune!

NUMBER THREE PIG: Where would you get the money?

NUMBER ONE PIG: Have been making regular deposits at the Piggy Bank. You forget: I am college graduate. I really know how to bring home the bacon.

NUMBER TWO PIG: Oink! STAGE MANAGER (Rising): And so, the Three Swine of Most Small Stature set to work to build themselves the best pagodas they could manage. (PIGS pantomime building houses.) Number One Pig built his house of bricks, while Number Two Pig built his of chopsticks and Number Three Pig used tatami. And when the pagodas were finished, how pleased the pigs were. . . Story now becomes complicated. Is late one night. Each pig sits in his own pagoda. No scenery for night. No scenery for pagodas. Audience must use imagination. We blew budget on the snowflake. Suddenly, out of the woods comes dark, mysterious figure. (WON TON WOLFenters and slinks around at back of stage.) Wicked creature. Evil creature. Hush! Plot thickens! (WOLF pretends to knock on door of straw house by stamping his foot on the stage as he raps his hand in the air.)

WOLF: O, most revered Number Three Pig, I beg you to give me admittance to your snug little pagoda.

NUMBER THREE PIG: Who is that knocking on my door?

WOLF: It is I, your humble friend and neighbor Won Ton Wolf. Let me in, let me in!

NUMBER THREE PIG: Not by the hair of my Chinny Chin-Chin.

WOLF (Perplexed): What the heck is a Chinny Chin-Chin?

NUMBER THREE PIG: Oh. Is my girlfriend. Her name is Chin-Chin. “Chinny” is her nickname. WOLF (Still perplexed): Well, what on earth does her hair have to do with it?

NUMBER THREE PIG: Her hair is her most beautiful feature. It is what caused me to fall in love with her. (Sings) “I dream of Chinny with the light brown hair. . . .” WOLF (Disgusted): What is this, Chinese amateur night? Let me in, I say!

NUMBER THREE PIG: Never!

WOLF: Then I’ll huff and I’ll puff and I’ll blow your house in!

NUMBER THREE PIG: And then what will you do? WOLF (Laughing wickedly): I’ll turn you into pork chow mein! STAGE MANAGER (As WOLF huffs and puffs): So Wolf huffed. Wolf puffed. Son of Confucius! Wolf blew house in! (NUMBER THREE PIG falls over.) Fortunately, Pig escaped to pagoda of Number Two Pig. (NUMBER THREE PIG runs over to NUMBER TWO PIG.)

NUMBER THREE PIG: Listen, brother, I’m in big trouble. May I spend the night with you?

NUMBER TWO PIG: Of course. But what happened? (WOLF knocks at door of second house.)

NUMBER THREE PIG: Never mind. I think it’s about to happen again.

WOLF: O, most noble and esteemed Number Two Pig, let me in, let me in.
NUMBER TWO PIG (To NUMBER THREE PIG): Who can that be?
NUMBER THREE PIG (Dryly): Well, it ain’t Madame Butterfly.
NUMBER TWO PIG (Dramatically): You mean — ?

NUMBER THREE PIG: (Nodding): Yep. Won Ton Wolf.
NUMBER TWO PIG (To WOLF): You’ve got to be kidding. O most feared and vicious wolf.
Never will I lot you in, not by the hair of my brother’s Chinny Chin-
Chin. (Pause) Aren’t you going to ask me what a Chinny Chin-Chin is?

WOLF: Forget it. Been there. Done that. Are you going to open up or do I go into my huff-and-puff stuff?

NUMBER TWO PIG: What will you do if I let you in?

WOLF: I’ll turn you into Barbecued Spare Ribs with Sesame Soy Sauce. STAGE MANAGER (As WOLF huffs): Again, Wolf huffed. Wolf puffed. Again, success! (NUMBER TWO PIG and NUMBER THREE PIG fall over.) Sky looked as if it was raining chopsticks. Just in nick of time, Number Two Pig and Number Three Pig made it to pagoda of Number One Pig. (They race over to NUMBER ONE PIG.)

NUMBER ONE PIG: O my most honorable brothers, to what do I owe the esteemed pleasure of this unexpected visit?

NUMBER TWO PIG: It’s Won Ton Wolf!

NUMBER THREE PIG: He’s after us! NUMBER ONE PIG (Smugly): Why did you not seek refuge in your own pagodas?

NUMBER THREE PIG: All right, don’t rub it in. That tatami of mine just shriveled to bits. It never pays to buy cheap foreign merchandise.

NUMBER TWO PIG: And my chopsticks weren’t much use, either. You were very clever, Number One Pig, to build your house of bricks. NUMBER ONE PIG (Modestly): Well, to tell the truth, I didn’t get the idea by myself. Read it in a fortune cookie.

NUMBER THREE PIG: Who cares how you got the idea! Will you let us stay with you?

NUMBER ONE PIG: Do you think I’d throw my esteemed brothers into the cold, and keep all this warmth for myself? What do you take me for — a pig?

STAGE MANAGER: So the Three Swine of Most Small Stature waited in their safe brick pagoda for the arrival of their enemy. He was not long in showing up. WOLF (Pretending to knock): O, most esteemed Number One Pig, let me in, let me in. THREE PIGS (In unison, singing): “I dream of Chinny with the light brown hair…” WOLF (Angrily): Oh, you’re pulling that on me, are you? O.K. wise guys, prepare yourselves for some huffing and puffing that’ll blow you all into won ton soup!

STAGE MANAGER (As WOLF huffs): Wolf huffed. Wolf puffed. But, lo! Brick pagoda did not give way. Number One Pig had built it too strongly. Pigs were safe! Wolf was outfoxed! WOLF (To STAGE MANAGER): Oh, yeah? Well, there’s more than one way to skin a kumquat. I have a sneaky plan that will get me into that pagoda even if it is made of bricks.

STAGE MANAGER: What’s your plan? WOLF (Triumphantly): I’ll climb up on the roof and drop down the chimney! Just wait’ll I get a ladder. (WOLF exits. Gong is heard. Stage Manager turns to audience.) Stage Manager: O most revered audience, it would be a pleasure to show you outcome of devious plat of Won Ton Wolf. However, is impossible in our humble theater. Not enough money to show roof. Not enough money to show chimney. Not even enough money for symbolic, aesthetic ladder. Besides, actor playing wolf afraid of heights. However, I can tell you how story ended. Number One Pig said:

NUMBER ONE PIG: O, my brothers, after your adventure in the cold, wintry night, I’ll bet you’d like a cup of nice hot Formosa Oolong tea. I will just set a giant cauldron of water — which I just happen to have lying about the house — in the fireplace and let it come to a boil.

NUMBER TWO PIG: You really shouldn’t bother, Number One Pig.

NUMBER THREE PIG: Yes, why go to all that trouble?

NUMBER ONE PIG: Well, you never can tell. Someone may be dropping in.

STAGE MANAGER: And so, clever Number One Pig came up with stratagem that cooked wolf’s goose. But in any case, Wolf would have met sad fate, and story would have had happy ending. For as it is written in ancient, honorable Chinese proverb, “He who drops down Oriental chimney comes down with case of Hong Kong flue.” Get it? Flu? (Bows low. Blackout and quick curtain.)
```

---

## IC-0547: UFO Menance

- Title: UFO Menance
- Author (byline): Woody Allen
- Work: Side Effects
- Publisher: Ballantine Books
- Publication date as stated: Nov 1989
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 1, ACTOR 2
- Teaser before the introduction: Yes
- Spoken words (computed): 2060
- Already set (do not supply): none

### Source block (context only)

```text
Author: Woody Allen
Book: Side Effects
ISBN: 978-0345343352
Publisher: Ballantine Books
Date (Month/Year): Nov 1989
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 2: The Men In Black - or MIB's as they are sometimes called are a group that supposedly show up to harass or intimidate witnesses of UFO sightings and related phenomena the government does not want the public to know about.

ACTOR 1: They usually make vague or sometimes specific threats to stop witnesses from talking or sharing information. They confiscate any physical proof of UFO related sightings -- such as photos, artifacts, or audio / video recordings.

ACTOR 2: Needless to say, they have perpetuated the controversy surrounding crop circles, alien abductions, Stonehenge and Area 51.

ACTOR 1: We’re here today to get to the TRUTH behind the

TOGETHER: UFO Menace by Woody Allen.
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

ACTOR 1: UFOs are back in the news, and it is high time we took a serious look at this phenomenon.

ACTOR 2: (Actually, the time is ten past eight, so not only are we a few minutes late but I'm hungry.)

ACTOR 1: Up until now, the entire subject of flying saucers has been mostly associated with kooks or oddballs.

ACTOR 2: Frequently, in fact, observers will admit to being a member of both groups.

ACTOR 1: Still, persistent sightings by responsible individuals have caused the Air Force and the scientific community to reexamine a once skeptical attitude, and the sum of two hundred dollars has now been allocated for a comprehensive study of the phenomenon. The question is: Is anything out there? And if so, do they have ray guns?

ACTOR 2: All UFOs may not prove to be of extraterrestrial origin, but experts do agree that any glowing cigar-shaped aircraft capable of rising straight up at twelve thousand miles per second would require the kind of maintenance and sparkplugs available only on Pluto.

ACTOR 1: If these objects are indeed from another planet, then the civilization that designed them must be millions of years more advanced than our own.

ACTOR 2: Either that or they are very lucky.

ACTOR 1: Professor Leon Speciman postulates a civilization in outer space that is more advanced than ours by approximately fifteen minutes. This, he feels, gives them a great advantage over us, since they needn't rush to get to appointments.

ACTOR 2: Dr. Brackish Menzies, who works at the Mount Wilson Observatory, or else is under observation at the Mount Wilson Mental Hospital (the letter is not clear), claims that travelers moving at close to the speed of light would require many millions of years to get here, even from the nearest solar system, and, judging from the shows on Broadway, the trip would hardly be worth it.

ACTOR 1: (It is impossible to travel faster than light, and certainly not desirable, as one's hat keeps blowing off.)

ACTOR 2: Interestingly, according to modern astronomers, space is finite.

ACTOR 1: This is a very comforting thought-particularly for people who can never remember where they have left things.

ACTOR 2: The key factor in thinking about the universe, however, is that it is expanding and will one day break apart and disappear. That is why if the girl in the office down the hall has some good points but perhaps not all the qualities you require it's best to compromise.

ACTOR 1: The most frequently asked question about the UFOs is: If saucers come from outer space, why have their pilots not attempted to make contact with us, instead of hovering mysteriously over deserted areas?

ACTOR 2: My own theory is that for creatures from another solar system "hovering" may be a socially acceptable mode of relating. It may, indeed, be pleasurable. I myself once hovered over an eighteen-year-old actress for six months and had the best time of my life.

ACTOR 1: It should also be recalled that when we talk of "life" on other planets we are frequently referring to amino acids, which are never very gregarious, even at parties.

ACTOR 2: Most people tend to think of UFOs as a modern problem, but could they be a phenomenon that man has been aware of for centuries?

ACTOR 1: (To us a century seems quite long, particularly if you are holding an IOU, but by astronomical standards it is over in a second. For that reason, it is always best to carry a toothbrush and be ready to leave on a moment's notice.)

ACTOR 2: Scholars now tell us that the sighting of unidentified flying objects dates as far back as Biblical times. For instance, there is a passage in the Book of Leviticus that reads, "And a great and silver ball appeared over the Assyrian Armies, and in all of Babylonia there was wailing and gnashing of teeth, till the Prophets bade the multitudes get a grip on themselves and shape up."

ACTOR 1: Was this phenomenon related to one described years later by Parmenides: "Three orange objects did appear suddenly in the heavens and did circle midtown Athens, hovering over the baths and causing several of our wisest philosophers to grab for towels"?

ACTOR 2: And, again, were those "orange objects" similar to what is described in a recently discovered twelfth century Saxon-church manuscript: “A lauch lauched he; wer richt laith to weet a cork-heild schonne; whilst a red balle lang owre swam aboone. I thank you, ladies and gentlemen"?

ACTOR 1: This last account was taken by medieval clergy to signify that the world was coming to an end, and there was great disappointment when Monday came and everyone had to go back to work. Finally, and most convincingly, in 1822 Goethe himself notes a strange celestial phenomenon.

ACTOR 2: "En route home from the Leipzig Anxiety Festival, I was crossing a meadow, when I chanced to look up and saw several fiery red balls suddenly appear in the southern sky. They descended at a great rate of speed and began chasing me. I screamed that I was a genius and consequently could not run very fast, but my words were wasted. I became enraged and shouted imprecations at them, whereupon they flew away frightened. I related this story to Beethoven, not realizing he had already gone deaf, and he smiled and nodded and said, 'Right.'

ACTOR 1: As a general rule, careful on-the-scene investigations disclose that most "unidentified" flying objects are quite ordinary phenomena, such as weather balloons, meteorites, satellites, and even once a man named Lewis Mandelbaum, who blew off the roof of the World Trade Center. A typical "explained" incident is the one reported by Sir Chester Ramsbottom, on June 5, 1961, in Shropshire:

ACTOR 2: "I was driving along the road at 2:00 A.M. and saw a cigar-shaped object that seemed to be tracking my car. No matter which way I drove, it stayed with me, turning sharply at right angles. It was a fierce, glowing red, and in spite of twisting and turning the car at high speed I could not lose it. I became alarmed and began sweating. I let out a shriek of terror and apparently fainted, but awoke in a hospital, miraculously unharmed."

ACTOR 1: Upon investigation, experts determined that the "cigar-shaped object" was Sir Chester's nose. Naturally, all his evasive actions could not lose it, since it was attached to his face.

ACTOR 2: Another explained incident began in late April of 1972, with a report from Major General Curtis Memling, of Andrews Air Force Base:

ACTOR 1: "I was walking across a field one night and suddenly I saw a large silver disc in the sky. It flew over me, not fifty feet above my head, and repeatedly described aerodynamic patterns impossible for any normal aircraft. Suddenly it accelerated and shot away at terrific speed."

ACTOR 2: Investigators became suspicious when they noticed that General Memling could not describe this incident without giggling. He later admitted he had just come from a showing of the film War of the Worlds, at the post movie theatre, and "got a very big kick out of it."

ACTOR 1: Ironically, General Memling reported another UFO sighting in 1976, but it was soon discovered that he, too, had become fixated on Sir Chester Ramsbottom's nose-an occurrence that caused consternation in the Air Force and eventually led to General Memling's court-martial.

ACTOR 2: If most UFO sightings can be satisfactorily explained, what of those few which cannot?

ACTOR 1: Following are some of the most mystifying examples of "unsolved" encounters, the first reported by a Boston man in May, 1969:

ACTOR 2: "I was walking by the beach with my wife. She's not a very attractive woman. Rather overweight. In fact, I was pulling her on a dolly at the time. Suddenly I looked up and saw a huge white saucer that seemed to be descending at great speed. I guess I panicked, because I dropped the rope on my wife's dolly and began running. The saucer passed directly over my head and I heard an eerie, metallic voice say, 'Call your service.' When I got home, I phoned my answering service and received a message that my brother Ralph had moved and to forward all his mail to Neptune. I never saw him again. My wife suffered a severe breakdown over the incident and now cannot converse without using a hand puppet." From I. M. Axelbank, of Athens, Georgia, February, 1971:

ACTOR 1: "I am an experienced pilot and was flying my private Cessna from New Mexico to Amarillo, Texas, to bomb some people whose religious persuasion I do not wholly agree with, when I noticed an object flying alongside me. At first I thought it was another plane, until it emitted a green beam of light, forcing my plane to drop eleven thousand feet in four seconds and causing my toupee to snap off my head and tear a two-foot hole in the roof. I repeatedly called for help on my radio, but for some reason could only get the old Mr. Anthony program. The UFO came very close to my plane again and then shot away at blinding speed. By this time I had lost my bearings and was forced to make an emergency landing on the turnpike. I continued the trip in the plane on the ground and only got into trouble when I tried to run a toll booth and broke off my wings." One of the eeriest accounts occurred in August, 1975, to a man on Montauk Point, in Long Island:

ACTOR 2: "I was in bed at my beach house, but could not sleep because of some fried chicken in the icebox that I felt entitled to. I waited till my wife dropped off, and tiptoed into the kitchen. I remember looking at the clock. It was precisely four-fifteen. I'm quite certain of this, because our kitchen clock has not worked in twenty-one years and is always at that time. I also noticed that our dog, Judas, was acting funny. He was standing up on his hind legs and singing 'I Enjoy Being a Girl.' Suddenly the room turned bright orange. At first, I thought my wife had caught me eating between meals and set fire to the house. Then I looked out the window, where to my amazement I saw a gigantic cigar-shaped aircraft hovering just over the treetops in the yard and emitting an orange glow. I stood transfixed for what must have been several hours, though our clock still read four-fifteen, so it was difficult to tell. Fi-nally, a large, mechanical claw extended from the aircraft and snatched the two pieces of chicken from my hand and quickly retreated. The machine then rose and, accelerating at great speed, vanished into the sky. When I reported the incident to the Air Force, they told me that what I had seen was a flock of birds. When I protested, Colonel Quincy Bascomb personally promised that the Air Force would return the two pieces of chicken. To this day, I have only received one piece." Finally, an account in January, 1977, by two Louisiana factory workers:

ACTOR 1: "Roy and I was catfishing in the bog. I enjoy the bog, as does Roy. We was not drinking, although we had brought with us a gallon of methyl chloride, which we both favor with either a twist of lemon or a small onion. Anyways, at about midnight we looked up and saw a bright yellow sphere descend into the bog. At first Roy mistook it for a whooping crane and took a shot at it, but I said, 'Roy, that ain't no crane, 'cause it's got no beak.' That's how you can tell a crane. Roy's son Gus has a beak, you know, and thinks he's a crane. Anyways, all of a sudden this door slides open and several creatures emerge. These creatures looked like little portable radios with teeth and short hair. They also had legs, although where the toes usually are they had wheels. The creatures motioned to me to come forward, which I did, and they injected me with a fluid that caused me to smile and act like Bo Peep. They spoke with one another in a strange tongue, which sounded like when you back your car over a fat person. They took me aboard the aircraft and gave me what seemed to be a complete physical examination. I went along with it, as I had not had a checkup in two years. By now they had mastered my own language, but they still made simple mistakes like using 'hermeneutics,' when they meant 'heuristic.' They told me they were from another galaxy and were here to tell the earth that we must learn to live in peace or they will return with special weapons and laminate every first-born male. They said they would get the results of my blood test back in a couple of days and if I didn't hear from them I could go ahead and marry Clair."
```

---

## IC-0548: We Too

- Title: We Too
- Author (byline): Jacob Shapiro and Madeline Aebersold
- Work: We Too
- Publisher: SpeechGeek
- Publication date as stated: 2019
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2096
- Already set (do not supply): none

### Source block (context only)

```text
We Too by Jacob Shapiro and Madeline Aebersold
ISBN. 978-1-61387-118-8
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
Phone. 1-888-742-2028
Email. thegeek@speechgeek.com
Web. www.speechgeek.com
Facebook. www.facebook.com/speechgeek
```

### Introduction (context only: never use it for content warnings)

```text
(no introduction)
```

### Performance text (classify this)

```text
Author’s Notes: The characters in this play have suggested genders. However, for the sake of performance, actors may choose to change any of the genders and gendered references of any of the characters except for Jim Calloway. And in the event that the gender is changed for Aaron or Gabby, the script may be adapted to reflect that (Sister instead of Brother, Black pants and red t-shirt instead of black dress and red cardigan, etc.). Performers may also choose to collapse the defense Lawyers into a single character for the sake of performance.

BAILIFFS. All rise! AARON. Your honor. Ladies and gentlemen of the jury. Thank you for

being here today. It is not an easy day for any of us, but it is

important to acknowledge that the role we all play today is what

makes tomorrow easier. I was going to start by telling you about

the victim. My sister—twin sister—Gabby. She is the kind of

person who wears every emotion right on her face. Which is how

I knew right away that something was terribly wrong.

TRANSITION TO GABBY AND AARON’S APARTMENT - FEB 13

AARON. Gabby? GABBY. (she sits quietly, shell shocked and horrified) AARON. Hey, you’re home! Ugh, what a crazy ass day! First, I asked the

guy at the coffee cart outside the courthouse for a half a cup so I

wouldn’t spill on myself. And as he is handing it to me, the

bottom of the cup is like just gone—totally disintegrates! And so

now I’ve got coffee all over my sleeve, and I’m due in court in

like 10 minutes. Then I get in there, and you’ll never guess who

the defense attorney is. It was ANGELA CONNOR. What are the

odds? My first case as lead prosecutor and I have to deal with a

defense attorney who’s seen me naked. And on our way out, she

says “Do you still live with your sister?” and I’m like “We shared

a womb. We are not good with distance.” And she said “Yeah,

that was always your problem,” and I was like WHAT? Can you

believe that?!
GABBY. (she cannot speak, there is too much to try to say)
AARON. Gabby…? Sis? What’s wrong? What happened?
GABBY. (she starts to cry)

TRANSITION TO COURTROOM - OCT 21

AARON. That silence, ladies and gentlemen of the jury, was the worst

silence of our lives. But unfortunately, when it comes to sexual

assault, it’s the first of many.

For many survivors, sexual assault is just the beginning of the injustice. For twins Gabby and Aaron, the road to recovery means navigating the confusing, humiliating, and often re-victimizing process of the legal system. While the #METOO movement has been monumental in helping victims speak out against injustice, the response to their raised voices must not be silence. Victims cannot heal alone. We Too, by Jacob Shapiro and Madeline Aebersold

TRANSITION TO GABBY AND AARON’S APARTMENT - FEB 20

AARON. You must be exhausted. Are you hungry? Do you want

something to eat?
GABBY. No.
AARON. You want a drink?
GABBY. No.
AARON. You want a hug?
GABBY. No.
AARON. Ok…do you want…?
GABBY. Aaron, stop trying to be helpful. I don’t need food or drinks or

hugs right now. AARON. OK. GABBY. Can we just… be normal? Like, I don’t want to talk about this

anymore, and I don’t want to think about this anymore and I don’t

want to deal with you tiptoeing around like a six-foot ballerina. AARON. Like a six-foot ballerina, huh? (starts to smile) GABBY. (knows where this is going, starts to smile in spite of herself)

…don’t. AARON. (begins to dance) No tip-toeing. I’m just hanging out... and

now...I’m picking up around the house...and now to the kitchen!
GABBY. Wow.
AARON. Pretty good, right?
GABBY. All that’s missing is the tutu.
AARON. I think we can all agree that it is not missed.
GABBY. Thank you. That was what I needed.
AARON. This whole thing is gonna suck for a while.
GABBY. Yeah.
AARON. And I am so proud of you for pressing charges, but there’s going

to be a trial. You know that, right? GABBY. Yeah. (pause) Aaron, I want you to be my lawyer. AARON. Me? No. They’ll put someone more senior on it. Maybe even the

D.A.
GABBY. I don’t want the D.A. I want you to do it.
AARON. Me.
GABBY. You. That’s what big brothers are for.
AARON. OK. I’ll handle it. I’ll handle everything.

TRANSITION TO COURTROOM - APRIL 3

LAWYER A. Do you swear to tell the whole truth, so help you God? GABBY I do. LAWYER A. This is the testimony of Gabriella Garza. Plaintiff in Garza v.

Calloway. Present are the Plaintiff, lead counsel for the

prosecution, Aaron Garza. Lead counsel for the defense,

Associates Steinbeck… LAWYER B. …and Stevens. If all parties are in agreement, let’s begin. Ms.

Garza, please describe the events of the night in question. GABBY. (addresses the jury) It was February 12th. I went to a Valentine’s

Day party, after work. AARON. Point of clarification, she works in a restaurant. GABBY. Gino’s on Grand. It’s...it was a nice place to work. I haven’t been

able to... I get panic attacks, and public bathrooms are triggers

for me now so I… AARON. It’s okay, Gabs. Just tell them what happened. GABBY. Right. So I went to this party. I didn’t know the people throwing

the party, but I was there with my friends. They knew everybody.

I felt like I wasn’t dressed up enough—I was just wearing an old

black dress and a red cardigan. But anyway, I was just sitting

there, and this guy walks over.
AARON. The defendant?
LAWYER B. Objection. Leading the witness.
AARON. Apologies. Gabby, can you please specify who this “guy” was?
GABBY. Yes. It was the defendant, Jim Calloway. I didn’t know his name at

the time, though. I had only seen him around a few times before.

He had come into the restaurant, maybe. Anyway, he seemed

nice, offered me a drink. LAWYER A. And had you been drinking before that? GABBY. No. I had only been at the party for about 15 minutes. I hadn’t had

a chance to find the bar or the kitchen or anything. And it was

very crowded.
LAWYER A. And you didn’t drink before you went there.
GABBY. No. I went right after work.
LAWYER A. And your outfit—
GABBY. A black dress and a red cardigan.
LAWYER A. Those are standard apparel at your work?
GABBY. The black dress is. But the red cardigan isn’t.
LAWYER A. So you didn’t go straight to the party after work. You had to stop

at home for your cardigan. While you were home, did you drink? AARON. Let me stop this right there. She didn’t go home, she brought the

cardigan with her in her car. She did not drink before she left

work, nor on the way to the party. She wasn’t drunk. LAWYER B. So, you weren’t drunk. Did you use any drugs that night? AARON. Objection. That question is irrelevant, and my sister doesn’t do

drugs. LAWYER B. We are trying to determine the plaintiff’s state of mind at the time

of the incident.
AARON. The attack.
LAWYER B. Objection. Prejudicial language, your honor.
AARON. Removed.
GABBY. And I didn’t even drink the one he gave me. I am really careful

about taking drinks from strangers, because, you know, you hear

all these bad things that happened at parties.

LAWYER A. Where did you hear those bad things? And if you heard that it

was dangerous, why did you go to this party and flirt with a

stranger to begin with?
AARON. She wasn’t flirting.
GABBY. I might have been flirting.
LAWYER B. Counselor, you are leading the witness.
AARON. Apologies your honor, it’s just that I happen to know how difficult

it is for her to detail the events of the party. That she went upstairs

to the bathroom and why does that matter? Because he followed.

He was not invited into the bathroom. LAWYER B. Counselor, unless you were there, I suggest you stop testifying

and let her. GABBY. Why? He’s heard the story as many times as I’ve told it, your

honor. At the police station, we must have had to repeat it 50

times. AARON. I understand, and no, I wasn’t there, but she told me the facts and

she told me she wasn’t flirting or…
LAWYER B. She just admitted to flirting. Is she now lying?
AARON. My sister doesn’t lie.
LAWYER B. If she lied about that, could she also lie about alcohol

consumption?
GABBY. Why do you keep asking the same questions?
AARON/GABBY. She/I wasn’t drunk.
LAWYER A. Objection.
AARON. What are you objecting to?
LAWYER B. Your honor, we’d like to request a continuance based on new

evidence. GABBY. What new evidence? What does that mean, Aaron? AARON. It means they want to delay the trial. (to the judge) Your honor,

this is completely inappropriate. A continuance should have

been filed at least--
LAWYER A. WE have a new witness. We request four weeks continuance.
AARON. A new witness? To the attack?
LAWYER B. Objection your honor.
GABBY. Four weeks!? They want us to wait for four more weeks? He gets

to go home. He gets four more weeks to do whatever he wants,

while I can’t even go to the bathroom? That’s not fair! AARON. Gabby, calm down. I’m handling this. Let me handle this. GABBY. Let you handle this? This is complete bullshit.

TRANSITION TO GABBY AND AARON’S APARTMENT - APRIL 3

AARON. Why did you do that? GABBY. Me?! That was completely insane! Four more weeks because

some new witness has suddenly appeared.
AARON. Yes, it’s insane. But your behavior—
GABBY. My behavior?
AARON. You swore in court. You stormed out. You—
GABBY. I was upset.

AARON. Right, but the judge and the jury can’t see you get like that.
GABBY. Why not?
AARON. Because it makes you seem overly emotional.
GABBY. Overly emotional?!
AARON. Makes you seem like you’re like some pissed off girl. Not like a

victim.
GABBY. And how does a “victim” act, Aaron?
AARON. Collected. Calm. Not like you’re out for revenge.
GABBY. I am out for revenge.
AARON. So am I! But we have to be able to keep it together. Because the

evidence isn’t going to do it for us on this one, OK? Sexual assault

cases are difficult to prove, and if he has a witness that swears

they saw you engage with him in any way that didn’t seem hostile

then we have a problem. GABBY. Because they’ll say I woke up the next morning with buyer’s

remorse. AARON. They’ll ask why you didn’t fight him off. GABBY. Because I didn’t go to the hospital with broken bones and ripped

clothes.
AARON. They’ll ask you what could have happened to let him think—
GABBY. Because he’s some college-educated rich asshole.
AARON. They’ll see him as a good looking, normal guy and you as some

hysterical wreck.
GABBY. They’ll say I wanted it.
AARON. …Yes.
GABBY. Aaron, I didn’t want it. I said no. I told him I was on my period. I

told him that I wasn’t on the pill. I told him everything I could

think of that’s supposed to make him not want to… He didn’t care.

He just did it anyway. Maybe because he was drunk, or because

he was sure I wouldn’t say anything, or maybe because he

figured if he got caught, he could have one of his buddies show

up as a surprise witness in his defense. AARON. I’m so sorry, Gabs. I’m sorry I wasn’t there to protect you. GABBY. Protect me? Is that what you think I needed? AARON. I don’t know. GABBY. How’s a six-foot ballerina supposed to protect me from this, huh? AARON. And that’s the worst part, right? There was nothing else you or I

could have done. This shit just happens.
GABBY. Yes.
AARON. I just want to make it better and I can’t.
GABBY. I don’t need you to make it better, Aaron.
AARON. What else are big brothers for?
GABBY. You tell me.

TRANSITION TO COURTROOM - May 5

BAILIFF. All rise. AARON. Your honor. Ladies and gentlemen of the jury. I was going to start

by telling you about the victim. About the things that have been

done to her at the hands of the defendant. But to only define her

as what’s happened to her would be further injustice, and to

speak for her won’t give her what she needs. Instead, I’m going

to do something that should be done for all victims of sexual

assault and I’m going to ask you to do the same. I’m going to

listen. Sis, they’re all yours. GABBY. Thank you.
```

---

## IC-0549: Where Shadows Dwell

- Title: Where Shadows Dwell
- Author (byline): Rhea Markos
- Work: Where Shadows Dwell
- Publisher: SpeechGeek
- Publication date as stated: 2017
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1715
- Already set (do not supply): none

### Source block (context only)

```text
Where Shadows Dwell by Rhea Markos
ISBN: 978-1-61387-305-2
Copyright 2017 by SpeechGeek.
Free performance of this play for high school and college level competitive forensics is
permitted. All other rights reserved.
This PDF version of this selection, e-published in 2017, is identical to the printed published
version of this same publication dated 2017. This statement, along with the entire printed
PDF of this publication, must be presented at any National Speech and Debate Association
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
MUSES. Long ago in Ancient Greece, gods rose and fell according to the

whims of Zeus. Oh, Mighty Zeus, god of the sky who defeated the

monstrous titans and ruled over the earth. Oh, Terrible Mighty

Zeus, who took whatever he wanted, whenever he wanted.

Goddesses and mortal women lived in fear: his love was pain, but

his wrath was ruin. And when she came of age, there was one

whom Zeus wanted above all others...the goddess Persephone. PERSEPHONE. Help! MUSES. She was beautiful, but naive. She was loving, but rebellious. She

was a goddess and a fool. PERSEPHONE. Please! Who does a goddess pray to? I have nothing and no one

to ask for help. Everything alive serves him. Everything on earth.

There’s nowhere to hide...
MUSES. Unless…
PERSEPHONE. Unless...I’ve heard stories about another world…
MUSES. An underworld.
PERSEPHONE. And a lord of the dead…
MUSES. Hades…
PERSEPHONE. It’s my only chance. Please, Hades. Save me.

In the Encyclopedia of Feminism, Lisa Tuttle explains that revisionist mythmaking, or the retelling of stories to feature strong female heroines, is crucial to the reinterpretation of how we see women in society. She suggests that for every narrative where the damsel isn’t distressed, we create a stronger sense of equality and further the idea that choice, not gender, as the ultimate determinant of success. In this retelling of the Greek myth of Persephone, the goddess is not helplessly seduced by a pomegranate or the victim of kidnap by the god Hades. Instead she seeks freedom from an oppressive patriarch by learning that even in the darkness there is light. Where Shadows Dwell by Rhea Markos.

PERSEPHONE. What happened? Where am I? Where is the light?
HADES. Give your eyes a chance to adjust.
PERSEPHONE. Who is that? Who’s there?
HADES. The one you called for.
PERSEPHONE. You’re Hades?
HADES. I am.
PERSEPHONE. But you’re a woman…
HADES. So your eyes are adjusting after all. Here, let me help you up. I’m

not going to hurt you. PERSEPHONE. I’m sorry. I’ve heard stories about the lord of the underworld. HADES. Yes. I’m sure you’ve heard that I am evil, cruel, and a man.

Obviously it’s not all true.
PERSEPHONE. That doesn’t mean none of it is.
HADES. I rescued you, didn’t I? Brought you somewhere safe.
PERSEPHONE. To the land of the dead?
HADES. If it is not suited to your liking, you are free to go!
PERSEPHONE. No, I didn’t mean...I’m sorry. I am still in shock.
HADES. And I am out of practice in the ways of civility. You called for my

help. What do you need? PERSEPHONE. Zeus means to take me with him to Olympus. HADES. And you do not want to live with the gods on Olympus? To be in

Zeus’s favor?
PERSEPHONE. To be a plaything? No.
HADES. So you wish to stay?
PERSEPHONE. I have nowhere else to go.
HADES. I’ll prepare a room for you and you can rest. Tomorrow, I will

show you around the underworld, your new home. PERSEPHONE. My new home…

MUSES. So Persephone gave up a gilded cage on high, for an unknown

world below. And while Zeus hunted for her, Persephone began

her new life in the dark. Days passed, and Persephone began to

see the Underworld as Hades saw it. Not as a place of death, but

as a place for the lost.

HADES. Is your room to your liking? Did you sleep well? PERSEPHONE. Like the dead. It was a joke. HADES. Yes. Forgive me, I... I haven’t heard laughter in long time. It’s

lovely. Now, as long as you are here, you must follow the rules.

The Underworld is not like where you come from. There are

dangers here that you must avoid. PERSEPHONE. Dangers? I’m immortal. HADES. Yes, a god will not die from natural causes. But in the land of the

dead, there are unnatural causes. And if you die here, you’re

trapped forever.
PERSEPHONE. Aren’t I already trapped here?
HADES. What?
PERSEPHONE. I mean, I can’t leave. This is the only place I can hide from Zeus.

So I’m pretty much powerless either way: it’s his prison or yours. HADES. Your life is now—as it has always been—your choice. You are not

my prisoner. And you are not powerless. So many gods think that

others give you power or the fates make your choices. Those are

lies. Believe me—as a god whom no one has ever built an altar

for, and as one who has seen all fates—I promise you, the only

true powers in this world are choice and belief in yourself. And

you have already proven yourself to be very powerful.
PERSEPHONE. You are not what I expected, Hades.
HADES. Yes, I hear that a lot.
PERSEPHONE. Why do they call you a lord? Why do mortals think you are a

man? HADES. A lie spread by Zeus. My brother. He taunts me because I prefer

the company of women. PERSEPHONE. Oh? Oh. HADES. It’s not just me. Zeus spreads lies about most gods to make

himself more powerful. He is believed only because he is the

king of Olympus. PERSEPHONE. Plus, he can change his form to look like anyone or anything to

get what he wants.
HADES. Indeed. I could be Zeus right now.
PERSEPHONE. Or I could be, and you’d never know.
HADES. I would know it wasn’t you. Zeus can transform outer appearance,

but he can never mimic inner beauty.
PERSEPHONE. Thank you. Do you think he will discover where I’ve gone?
HADES. Perhaps, eventually.
PERSEPHONE. So I’ll never be free. I’ll never go home. I’ll never feel the grass

or or see the night sky or taste a pomegranate. I’m sorry, I don’t

mean to be ungrateful. HADES. Not at all. I am more familiar with grief than most. I only wish I

could offer you some comfort. PERSEPHONE. You have.

MUSES. In the world above, whispers of Persephone’s whereabouts had

reached Zeus. The sky shook with his fury. But far below and

unaware, Hades and Persephone grew closer... Because the only

way to see in the dark is with your heart.

PERSEPHONE. What is this place? HADES. A surprise. A new addition to the Underworld. I created it to host

the wisps of ancient souls. Those who have been gone so long,

they forgot their bodies and all that’s left is their inner light. PERSEPHONE. It looks… HADES. Like the night sky. Yes. I got the idea from you. And the wisps

have yet one more surprise. If you dance for them, they sing.

(offers a hand)
PERSEPHONE. But who will lead?
HADES. We will take turns.
PERSEPHONE. This place is incredible.
HADES. The Underworld can be beautiful, if you are willing to see

beneath the darkness.
PERSEPHONE. I’m beginning to understand.
HADES. I have a gift for you. A necklace.
PERSEPHONE. Made from pomegranate seeds?
HADES. You said you missed them.
PERSEPHONE. It’s beautiful. It reminds me of...
HADES. Your home? I’m sorry, I thought it would make you happy.
PERSEPHONE. Yes. No. I don’t know. It’s wonderful. I’ll cherish it.
HADES. Persephone? What’s wrong?
PERSEPHONE. Nothing. It’s just...I came here to escape from Zeus.
HADES. I know.
PERSEPHONE. It’s why I came. It’s not why I stayed. Do you understand? Hades?

What was that noise? HADES. An alarm. Something’s happened. Stay here. PERSEPHONE. I will…

HADES/ZEUS. Persephone. PERSEPHONE. What’s happened?

HADES/ZEUS. It’s Zeus. He’s discovered where you are. He’ll be here any

moment. He’s coming to take you and kill me. You have to come

with me now.
PERSEPHONE. I don’t understand. Why would we leave the Underworld?
HADES/ZEUS. He’s too strong. Too powerful. Come on.
PERSEPHONE. You’re hurting me.
HADES/ZEUS. I’m sorry, I forget how strong I am. I just, I care so much about

you. PERSEPHONE. You do? HADES/ZEUS. Of course I do! You are as precious to me as...as that old necklace

is to you. PERSEPHONE. What? HADES/ZEUS. That necklace, I assume it’s old because it’s hideous. A gift from

that terrible mother of yours, not doubt. PERSEPHONE. “He can transform outer appearance, but he can never mimic

inner beauty.”
HADES/ZEUS. What did you say, child?
PERSEPHONE. Nice try, Zeus.
HADES/ZEUS. (whole face and demeanor changes from concern to pure evil as

Zeus is revealed) Oh, Persephone. Beautiful and clever. You will

make such a fine addition to my Olympus. PERSEPHONE. What have you done with Hades? HADES/ZEUS. Never mind that now. You’ve got more important things to worry

about. PERSEPHONE. I’m not going with you. HADES/ZEUS. As if it were up to you? As if you had the power to stop it? Give

me what I want, or I will take it.
PERSEPHONE. I’d like to see you try.
HADES/ZEUS. What? What is this? Night sky, I command you!
PERSEPHONE. It’s not the sky. It’s an illusion. And without the sky you have no

lightning or thunder to frighten me with. HADES/ZEUS. Then we’ll do this the old fashioned way.

(They fight. She captures him with the necklace around her throat.)

PERSEPHONE. Yield, Zeus! HADES/ZEUS. Or what? You foolish girl, I’m immortal! PERSEPHONE. Yes, a god will not die from natural causes. But in the land of the

dead, there are unnatural causes. And if you die here, you’re

trapped forever. Yield. HADES/ZEUS. Very well. I yield. PERSEPHONE. Now tell me where Hades is.

MUSES. Persephone ran through the Forest of the Immortals. And even

though she once again saw the sky and her beloved

pomegranate trees, her eyes were fixed for one thing only.

PERSEPHONE. Hades! HADES. Persephone. It was Zeus. He’s coming for you.

PERSEPHONE. All is well. He is gone. He’s left us.
HADES. You’re free?
PERSEPHONE. We both are. Free and together.
HADES. Our story—our true story—will never be known, Persephone.

Zeus’s lies will take root, and they will spread. They will believe

that I…took you, kidnapped you… PERSEPHONE. I am free, Hades. As I have been every moment I’ve been with

you. Our story will be here for those who are willing to see

beneath the darkness. That you saved me. HADES. And then you saved me. PERSEPHONE. We took turns.

MUSES. And so Persephone and her dark wife Hades disappeared into

the Underworld. They chose one another and found true

freedom.
```

---

## IC-0550: Wretched: A Wickedly Funny Parody

- Title: Wretched: A Wickedly Funny Parody
- Author (byline): James Cronan
- Work: Wretched: A Wickedly Funny Parody
- Publisher: SpeechGeek
- Publication date as stated: 2014
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MONKEY
- Teaser before the introduction: No
- Spoken words (computed): 1572
- Already set (do not supply): none

### Source block (context only)

```text
Wretched: A Wickedly Funny Parody by James Canon
ISBN: 978-1-61387-065-5
Copyright 2014 by SpeechGeek.
Free performance of this play for high school and college level competitive forensics is
permitted. All other rights reserved.
This PDF version of this selection, e-published in 2013, is identical to the printed published
version of this same publication dated 2013. This statement along with the entire printed PDF of
this publication must be presented at any National Forensic League District or National event for
the script to comply with NFL rules per the request of the Executive Director.
This and other selections of quality performance literature for competitive oral interpretation
are published by SpeechGeek.
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
MUNCHKIN #1. Look, it’s Glennda! (GLENNDA appears humming. Musical

transitions are encouraged in the performance.) GLENNDA. Fellow Ahhzians, the Wretched Witch of the West is dead! MUNCHKIN #2. Is it true? Is the Wretched Witch of the West really dead? GLENNDA. Yes, I just said that. MUNCHKIN #3. Oooh! I have a question! Was she born wretched? GLENNDA. Well, let me think…

FLASH BACK

MIDWIFE. Here she is. Is lovely baby, is it not? ALPHALBAH. (growls) MIDWIFE. Yes, baby is lovely, no?

FLASH FORWARD

GLENNDA. She wasn’t lovely, not at all. MUNCHKIN #1. Weren’t you her friend, Glennda? GLENNDA. Well, to answer that, we’ll have to go back to the

beginning…. It all started at school, where I met the

Wretched Witch of the West--I mean Alphalbah…

TRANSITION

HORRIBLE. Hello, students! I am Madame Horrible, headmistress here

at Haug-wartz, I mean Whiz…(She picks up the magic chalk

that has written her name on the board.)--thank you,

magic—University. (She puts the chalk in her mouth and

transforms it into gum.) Mmm, chalky! School will be hard

but fun and…(sees ALPHALBAH) Sweet Ahhz; you’re a

green child!
ALPHALBAH. Yes, I am.
HORRIBLE. Are you seasick?
ALPHALBAH. No, I’m just green.
HORRIBLE. Are you an artichoke?
ALPHALBAH. No, I’m not a vegetable.
HORRIBLE. Is your skin an outward manifestation of your twisted and

evil nature? ALPHALBAH. No, it’s not my fault! I can’t help that I can magically

teleport…

HORRIBLE. Impressive.
ALPHALBAH. …or that I can make objects move…
HORRIBLE. Astonishing!
ALPHALBAH. …or that I can say the entire alphabet backwards…
HORRIBLE. Witchcraft!
ALPHALBAH. And I can’t help it that I’m green!
HORRIBLE. Well, to be fair you do look like an artichoke. Oh relax,

don't be so sensitive. I'm just kidding! Now I want

everyone to take out their essays “Magic Wands, What’s

the Point?” Ouch! (laughs) Apparently, the point is very

sharp. (bell rings) Oh, that’s the bell! Hand in your essays

and have fun at your next class! ALPHALBAH. Okay, teleport to Doctor Diamond's class!

TRANSITION

GLENNDA. Alphalbah was learning how difficult it was to be herself.

Her teachers were not very understanding or kind to her.

And neither were her peers. MUNCHKIN #1. How do you know? GLENNDA. Because I was not very nice to her.

TRANSITION

ALPHALBAH. Dr. Diamond’s class. DIAMOND. Hello, I am Dr. Diamond, your token goat teacher at Whiz

University. GLENNDA. Umm, excuse me. Have you read our most recent essays? DIAMOND. You must be Glinda. GLENNDA. NO. It’s Glennda, with an ‘e.’ I don’t want to get sued. DIAMOND. That’s a long name. Well, Glennda-with-an-e-I-don’t-

want-to-get-sued, where is your essay?
GLENNDA. Here (hands it to him)
DIAMOND. (eats it) It wasn’t baaad. You get a C.
GLENNDA. A C!? Ewwwww!
DIAMOND. Ewe? Where? Hubba Hubba.
GLENNDA. Goats are so bad at grading papers!
DIAMOND. You’re next, ugly.
ALPHALBAH. It’s Alphalbah, actually.
DIAMOND. (eats it) Mmmmm, A-plus.

GLENNDA. Ugh. I don’t understand what the problem is. None of the

other professors seem to be having difficulty pronouncing

my name. ALPHALBAH. Listen, Glennda, maybe pronouncing your precious name

isn’t the only purpose of Doctor Diamond’s life. Maybe

this is how Doctor Diamond teaches. Maybe he has a

different style. Maybe he's...different. GLENNDA. Okay, Alfalfa, shush. I’m trying to learn good. It’s hard

with you sprouting up all up in my super cute face. ALPHALBAH. It’s Alphalbah! Why are you pronouncing my name wrong

when YOU hate that yourself! DIAMOND. I agree with the girl who doesn’t want legal trouble, be

quiet, ugly! You're really getting my goat. Class

dismissed. Tomorrow, I will collect more delicious essays. ALPHALBAH. All right, to Madam Horrible's again.

TRANSITION

GLENNDA. I felt horribly about what I had done. MUNCHKIN #3. What did you do? GLENNDA. Luckily, Madam Horrible came up with a solution so that I

could make it up to Alphalbah.

TRANSITION

ALPHALBAH. Madame Horrible! HORRIBLE. Sweet greens-us! ALPHALBAH. Madame Horrible, I have a secret. (pause) I have no

friends. HORRIBLE. Oh, that’s not a secret. At least you’re very bright. Why,

you practically glow in the dark. Do something magical. ALPHALBAH. Ok...(She does something magical.) HORRIBLE. That was astonishing! ALPHALBAH. Sorry, sometimes something just comes over me. HORRIBLE. What? No, never apologize for your gifts! I could never do

that. Oh! I have an idea. Never mind to my rules about

favoritism! You're remarkable. I shall teach you myself!

But you’ll need a partner. If you see Glennda, give her

this training wand. ALPHALBAH. Really? Thank you. Off to Glennda's house!

TRANSITION

ALPHALBAH. Glennda! GLENNDA. AH! Don’t do that! ALPHALBAH: Here, Glennda, Madam Horrible wanted me to give you

this wand. She says we should be partners. GLENNDA. Partners? Even after I was so mean to you? Oh my Whiz,

now we can be best friends! Me, the sparkling leader of

tomorrow, and you, the tragedy. I'm going to make you

over and fix you up! ALPHALBAH. You don't have to do that. GLENNDA. Yes, I do. I really do. Oh Alphabet, Your whole life is

going to be different because of me, and makeup…so

much makeup. Okay, let’s fix all of this! (She attempts to

use magic to fix ALPHALBAH’S face, but she fails.) Well, that

didn’t work. How about you wear this hat? It’s black, like

your personality. ALPHALBAH. No one…no one has ever given me anything before. GLENNDA. Oh, and look at you. You…you…well, you’re wearing a

hat, yay! Can I ask you a question?
ALPHALBAH. Sure.
GLENNDA. Your skin is a different color.
ALPHALBAH. That isn't a question.
GLENNDA. Oh, right. Um...why is your skin a different color? Is your

father a Teenage Mutant Ninja Turtle? ALPHALBAH. I'm not quite sure, but I'm treated differently because of

my skin color. It isn't easy being green. GLENNDA. I'm sorry to hear that. I've never thought about it like that

before. (her phone) Madam Horrible! Yes, Alpha-

Centari’s right here. (As she sets it down, Horrible

appears.) HORRIBLE. Oh El-Phelaphant, I’ve told the Whizard about your

condition and your magical abilities and he wants to meet

you! ALPHALBAH. The Whizard, what? I’m so excited I could just melt! GLENNDA. Not on the carpet please, mother just had them cleaned. HORRIBLE. When the Whizard is done with you, people will scream,

in a different way.
ALPHALBAH. Glennda, let’s go to the City of Emeralds! Together.
GLENNDA. I’ve always wanted to go there!
ALPHALBAH. Okay, Let’s go to the Whizard's room!

TRANSITION GLENNDA. (talking to the Munchkins) Alphalbah had forgiven me, but

we had no idea of the frightening and terrifying task that

lay ahead!
MUNCHKIN #1. Was it a spelling test?
MUNCHKIN #2. Oh, no! Spelling is hard.
GLENNDA. No, and quit interrupting.

TRANSITION

WHIZARD. I am the great and mighty Ahhhz, (WHIZARD suddenly

changes.) Just kidding, I’m the “great” Ahhhz. Now let’s

see, which witch is which? I’m so cute. Alphalbah, you

have come to prove yourself with this, the ancient spell

book of spells. Oooh. Try a flying spell on my monkey

servant. MONKEY #1. (grunts) GLENNDA. Awwwww. Oh, look at all its cute hair all over its face. It

looks just like you, Alf.
ALPHALBAH. Thanks. Okay. Flying spell. Avardahkedaverahhhh!
MONKEY: (The monkey dies.)
WHIZARD. Oh my. Um. (He looks at the book.) Oh! That was a dying

spell, not a flying spell. Ha ha ha. Oh, silly poor eyesight.

I NEED ANOTHER MONKEY! Try again, dear.
ALPHALBAH. All right. Boop!
MONKEY #2. (He grows wings.)
WHIZARD. Perfect! A flying monkey, he’ll make a wonderful spy.

They can fly around and report any shady activity to me,

and fight my battles without me leaving this room. I shall

call them drone monkeys. (hesitates) I mean, flying

monkeys. ALPHALBAH. Wait a minute, you lied to me! WHIZARD. Only verbally. But my dear, I think you know too much.

I'm going to tell everyone in Ahhz that this was your plan

and that YOU are wretched! Destroying you will be

a…whiz. (He laughs.) I’m so cute. ALPHALBAH. Let’s get the Alph out of here!

TRANSITION

ALPHALBAH. Phew. GLENNDA. Alpha-dog, you saved my life. ALPHALBAH. Yeah, but the Whizard shouldn't be allowed to do this.

Why would he want to lie to everyone? He can't use his

power this way.

GLENNDA. That's the way it is in Ahhhz. ALPHALBAH. I just don’t understand why the Whizard doing this! Why is

everyone so mean to me? All I have ever done is what

people have told me! I don't hurt anyone, and I'm not

mean to anyone. GLENNDA. Alpha, I'm sorry you’re treated differently. ALPHALBAH. No. This, all of this, is wrong. I have to go; I have to fix this

because the Whizard is the wicked one. So, I guess this is

goodbye. GLENNDA. I’m going to miss this. Standing next to you made me look

even prettier. ALPHALBAH. Glennda, you know, I only have one friend. You. GLENNDA. And I have so so so so so so so so many. But you’re the

only one that ever mattered, Alphalbah. Tear. ALPHALBAH. You too, and don’t worry about me, Glennda. Nobody, in

all of Ahhhz, no Whizard, then or now, nobody, is ever

going to take me down!

TRANSITION

MUNCHKIN #1. And then what happened?
GLENNDA. A little girl threw water on her and she melted. The end.
MUNCHKIN #2. What? That is a terrible story!
GLENNDA. No, she was my friend, I loved her, and I grew because I

knew her. I'm changed. MUNCHKIN #2. No, this story is not really all that fulfilling. Tell us the one

about the girl who lost her slipper. That sounds nice. GLENNDA. Oh, you are so small-minded! (She uses magic to make

MUNCHKIN #2 disappear.) Oh my, that was rather wicked

of me.
MUNCHKIN #3. You know, Glennda, that was a really good story.
MUNCHKIN #1. Yes, that was a magically good story!
GLENNDA. Yes, you might say it was wickedly good.
```

---

## IC-0551: A . . . My Name is Alice

- Title: A . . . My Name is Alice
- Author (byline): Not specified
- Work: Not specified
- Publisher: Concord Theatricals
- Publication date as stated: Nov 2010
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTRESS 2, POETESS, MS. THOMAS, MRS. JOHNSON, WORKMAN, WOMAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1049
- Already set (do not supply): none

### Source block (context only)

```text
Conceived by: Joan Micklin Silver and Julianne Boyd
ISBN: 978-0573681776
Publisher: Concord Theatricals
Date (Month/Year): Nov 2010
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: With a wry sense of humor, these sketches from A . . . My Name is Alice address the challenges of being a woman.

ACTRESS 2: From beatnik poetry (finger snaps),

ACTRESS 1: To being a power-mom in the cut-throat professional world,

ACTRESS 2: To merely taking a stroll down the street alone –

ACTRESS 1: Women must be prepared to handle it all

ACTRESS 2: And smile while we’re doing it!

ACTRESS 1: A . . . My Name is Alice

ACTRESS 2: Conceived by Joan Micklin Silver and Julianne Boyd
```

### Performance text (classify this)

```text
Conceived by Joan Micklin Silver and Julianne Boyd

Suggested Roles: ACTRESS 1: Split lines for POETESS, MS. THOMAS, WORKMAN

ACTRESS 2: Split lines for POETESS, MRS. JOHNSON, WOMAN

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

POETESS: (Pg 19) A poem. From my collection, For Women Only. (she recites, dramatically)
I am a woman Pity Pretty Polly,
A crippled bird. Doesn’t want a cracker.
The ledge is cold, I am a woman.
My wings are clipped. A crippled bird.
He did it. F—flap
He did it. F—flap
I was his pretty Polly. F—flap
Pity Polly.

Welcome to Kindergarten, Mrs. Johnson (Pg 21-24)

MS. THOMAS: Welcome to kindergarten, Mrs. Johnson.

MRS. JOHNSON: How do you do? It’s a pleasure meeting you. Janie has told me so much about you.

MS. THOMAS: It’s a shame you couldn’t make it to last week’s meeting like the other mothers.

MRS. JOHNSON: I’m sorry. I was speaking at a conference in Zurich.

MS. THOMAS: Well, come along. (crosses back to her desk) I’ve been observing Janie very closely. She’s a very bright girl, Mrs. Johnson. She works beyond potential—a model for her peers, exploring at a level that is way beyond her years. And I’m sorry, but it’s getting on my nerves.

MRS. JOHNSON: I’m sorry.

MS. THOMAS: Don’t fidget, Mrs. Johnson. (beat) She’s a difficult girl, Mrs. Johnson. She helps the other children—Lord knows where it will lead. And I’ve learned that when my back is turned, she’s teaching them to read. I’m to say the least dismayed—what does she think this is, third grade? She’s independent, she’s assertive, she’s always self-assured. Now I don’t know where she’s getting that, but it is not to be ignored—and it generally starts at the home. Did you know that Janie is the only child in class with an even reasonable self-image. Now who’s responsible for that?

MRS. JOHNSON: (a bit thrown) I am.

MS. THOMAS: I’m sorry?

MRS. JOHNSON: (louder) I am.

MS. THOMAS: I am what?

MRS. JOHNSON: I am, Ms. Thomas.

MS. THOMAS: Good. Well, how do you expect her to be intimidated by simple authority?

MRS. JOHNSON: Well, I . . .

MS. THOMAS: Now, I’m not saying you’re a bad mother, even though you missed our pageant And the Halloween parade. No, no one’s saying you’re a bad mother, but your cookies at the bake sale, well, they clearly weren’t homemade.

MRS. JOHNSON: (abashed) They were Pepperidge Farm Mint Milanos!

MS. THOMAS: The other mothers baked.

MRS. JOHNSON: I know, but. . . but I hate baking.

MS. THOMAS: Janie was humiliated!

MRS. JOHNSON: She never said a thing to me!

MS. THOMAS: Well, you’re a busy little bee, Mrs. Johnson. Zipping off to Zurich. I hear next week it’s Rome. Is there really any wonder things are suffering at home? (Mrs. Johnson starts to protest) Oh, there’s no need to object. It’s all here in Janie’s artwork—you can see that I’m correct. (She produces a large pig made out of a Clorox bottle and decorated with hearts. She shows it to Mrs. Johnson)

MRS. JOHNSON: It’s a pig! Made out of a Clorox bottle!

MS. THOMAS: Oh, come on, Mrs. Johnson. There are domestic problems written all over this pig. I know what I’m talking about. I’ve taken psychology courses.

MRS. JOHNSON: But . . .

MS. THOMAS: If you have something to say, you raise your hand! Now, no one wants to be a --

(she waits for Mrs. Johnson to respond)

MRS. JOHNSON: Bad mother.

MS. THOMAS: And I think we can do better if we just make up our minds, ‘cause we all know what happens to a— (she again waits for Mrs. Johnson to respond)

MRS. JOHNSON: Bad mother!

MS. THOMAS: And there’s every indication that this suits your situation. Here’s my evaluation—take it home and have it signed!

MRS. JOHNSON: (fighting back tears) Uh-huh.

MS. THOMAS: Did you know we have these parent-teacher conferences every Monday at four o’clock.

MRS. JOHNSON: (shaking head) Uh-uh.

MS. THOMAS: Well, I hope I’ll be seeing you again very soon.

MRS. JOHNSON: Ye-yes, Ms. Thomas.

MS. THOMAS: That’ll be all . . . (Mrs. Johnson flees for the door) No running in the halls! ******

POETESS: (she continues the 2nd stanza of her poem, dramatically)
I am a woman. “Won’t somebody talk
A neglected plant. to me?”
Hanging by the window I am a woman.
Waiting to be watered. A neglected plant.
He did it. D—droop
He did it. D—droop
I was his philodendron D—droop
Calling out,

****** Hot Lunch (Pg 44-45)

(A workman leans on a bit of construction debris, he’s on lunch break and is ogling imaginary girls that walk by)

WORKMAN: Wowee . . . beautiful, baby, beautiful . . . Hey, don’t ignore me, honey; you’re not that pretty . . . (a woman enters and crosses past him) Wowie, look at them gazoombas! I’d like to show you a taste of heaven, honey bunny.

WOMAN: (very polite) Excuse me, would you repeat what you just said to me?

WORKMAN: (startled) Huh? Oh sure. I said I’d like to show you a taste of heaven, honey bunny.

WOMAN: What else? You said something before that I couldn’t quite make out.

WORKMAN: (getting annoyed) I don’t know. I said you got a great pair of legs or something. I forget.

WOMAN: (matter of fact) No, no, I don’t think you said legs . . . It was something more like daroombas?

WORKMAN: Hey, lady, walk on by, will ya? I’m eating my lunch.

WOMAN: Yes, and I’m very sorry to disturb you, but try to remember what you said. It’s very important to me . . . Now, it sounded like . . .

WORKMAN: (very softly) Gazoombas.

WOMAN: Sorry, I didn’t get that.

WORKMAN: Gazoombas! Now will you please leave me alone? I’m on my lunch break.

WOMAN: I know, I know, I’m infringing on your time and I apologize for it, but what are gazoombas?

WORKMAN: Aw, just a word. A made-up word. No big deal. Look, I’m sorry, okay? I said gazoombas, so what? Since when was it a crime to give a compliment?

WOMAN: Yes, yes, I understand the motivation. It’s just the word, gazoombas. I’d never heard it before. What exactly does gazoombas refer to?

WORKMAN: (embarrassed) You know. (indicates up) Up there. (She looks up) Your chest, lady.

WOMAN: (relieved) Oh, thank goodness. I kind of thought that’s what you meant, but I wasn’t quite sure.

WORKMAN: Well, that’s what I meant, okay? No offense. (He begins to pack up)

WOMAN: Of course not . . . so, you like my gazoombas?

WORKMAN: Hey, cool it, will you? I work here!

WOMAN: Sorry, I just wanted to know if you really appreciated my mammaries.

WORKMAN: Lady, would you excuse me? I gotta get back on the job. (he tries to go past her and she stops him)

WOMAN: Of course, how stupid of me. But before you go, I’d like you to see my gazoombas.

(with her back to the audience . . . )

WORKMAN: Lady, lady, cover yourself! What are you doing?

WOMAN: I thought if I showed you my gazoombas, you’d show me your wogabongo.

WORKMAN: My what?

WOMAN: You know . . . wogabongo!!!

WORKMAN: You’re wacko lady!

WOMAN: Why am I a wacko? You like my gazoombas, I like your wogabongo. I just want that taste of heaven you promised me. Why, with my gazoombas and your wogabongo, we could make great shtahpoonko.

WORKMAN: (calling to an unseen coworker) Hey, Joe! Help! Help! Call the cops! I got a nut-case down here! Help!

WOMAN: (She dusts off her hands, thoroughly pleased with herself) *****

POETESS: (Pg 46) (she finishes her poem, dramatically)
I am a woman. That weekend he took her skiing in Aspen—
A dying swan. That’s when he did it.
Dancing, dancing, dancing. A love bullet
My toe shoes torn. Straight through my feathered gazoombas.
My tutu, too. I am a woman.
He did it. A dying swan.
He did it. Ach-ch
(And he knows who he is.) Ach-ch
Ach-ch
```

---

## IC-0552: After

- Title: After
- Author (byline): Carol K. Mack
- Work: 30 Ten-Minute Plays
- Publisher: Smith & Kraus
- Publication date as stated: September 2001
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: CINDY, GLYNDA
- Teaser before the introduction: No
- Spoken words (computed): 1168
- Already set (do not supply): none

### Source block (context only)

```text
Author: Carol K. Mack
Book: 30 Ten-Minute Plays
ISBN: 978-1575252773
Publisher: Smith & Kraus
Date (Month/Year): September 2001
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS PLAYING GLYNDA – BACK TO AUDIENCE – VOICE OF A TOUR BUS DRIVER:

(Voiceover.) Right over here, folks! That's all, folks! Let's go ... time's up. Back on the bus now, boys and girls, we've got lots more to see! Hi! Step right up ... Hi there. How're ya doin' ... everybody here? Aaalll aboard! ... Hello? ExCUSE me, Miss. HEY, you over there? Hello?! We're boarding ... Lady?! Hey, you can't go over there! Ma'am ... Nobody's allowed over there ... HEY! Hey you, get back here! Somebody get that visitor. She's off-limits! GET HER! GET HER! (Turns to Audience for Intro)

ACTRESS PLAYING CINDY: (Out of Breath) – Holy cow! You would not believe this. One minute I’m all goo-goo eyes over my fiancée and the next minute, I’m compelled to investigate the most amazing thing I’ve ever seen! Who said coming to Disney World was for kids? This is where most fairy tales end. The prince and princess marry and ride off into the sunset to begin their new life together as husband and wife, a life full of promise, romance, and above all, love.

ACTRESS PLAYING GLYNDA: Shhhh! Everything will be fine . . . Just stay calm . . . Not everyone knows the truth about the fairy tale endings . . . Happily Ever After . . . is kept a closely guarded secret. At least the “AFTER” part.

TOGETHER: After by Carol K. Mack
```

### Performance text (classify this)

```text
CINDY: (Awestruck, looks out to back of house.) Oh! ... WHOA! (Lowers her sun- glasses, removes cap.) What the ...

GLYNDA: (Sweetly, out of breath.) There you are!

CINDY: Where?!

GLYNDA: (Graciously.) Off-limits, I fear, but ...

CINDY: What is this place?

GLYNDA: Please come with me now, dear.

CINDY: (Grabs Glynda's wrist, points to rear of house.) What's that?!

GLYNDA: What ... ?

CINDY: Who are they?

GLYNDA: Come along, please?

CINDY: They're all over the grass!

GLYNDA: It's not real grass, it's ... (all right)

CINDY: Allover!

GLYNDA: This isn't part of the tour.

CINDY: As far as the eye can see!

GLYNDA: It's not for visitors ...

CINDY: (Confrontational.) Why not? Why is it "not for visitors"?

GLYNDA: (Whispering.) He wouldn't like it.

CINDY: Who?

GLYNDA: Mr. Walt.

CINDY: Walt. .. ? (Peering at Glynda.) But he's ...

GLYNDA: Yes! But he still cares.

CINDY: (Is she crazy?) Oh yeah?

GLYNDA: He doesn't like our visitors to be unhappy. Look how upset you're getting. And for what?

CINDY: For what?! You see them? There must be hundreds of white horses ...

GLYNDA: This is an unscheduled stop and we must disclaim any ...

CINDY: (Finally realizing.) This is where they all wind up, isn't it?

GLYNDA: (Simply, Glynda the Good.) Oh my, oh my, oh my.

CINDY: And all of those couples were princes and ...

GLYNDA: Are princes. Are! We can't have this!

CINDY: (Into her recorder, a reporter.) Hundreds of white horses have fallen here along with their riders and they're all gorgeous!

GLYNDA: Oh no!

CINDY: The women are dressed up in (Squinting.) prom dresses. Many have blond braids.

GLYNDA: (Aghast.) You're a journalist!

CINDY: All the guys are hunks in helmets ...

GLYNDA: Forget you saw this please, for your own sake! For your species!

CINDY: (Into recorder) They all appear to be smiling expectantly, as if. ..

GLYNDA: It had to end! Try to understand, it had to end!

CINDY: (Childlike anger.) WHY?! It says Happily Ever After!

GLYNDA: (Brightly) That's right, dear!

CINDY: That's RIGHT?!

GLYNDA: (With a sweeping gesture accompanied by stardust) Why yes! This is Happily Ever After.

CINDY: This is IT? A dump site!? (To her recorder darkly.) They're all just lying there, thick as penguins, far as the eye can see.

GLYNDA: But happily.

CINDY: You call that happily!?

GLYNDA: Goodness, yes. They're just ... (A rainbow gesture.) Over.

CINDY: That's not fair. (Cindy unexpectedly bursts into tears)

GLYNDA: Go ahead and cry if it makes you feel better! (Glynda hands Cindy a twinkling handkerchief)

CINDY: (Crying.) It's ... I always thought that after was only the Beginning. I thought they'd go a long way after After!

GLYNDA: Oh dear, I know. But you see nothing was written for them.

CINDY: What?

GLYNDA: Just, "The End."

CINDY: (Explosively ranting.) That's not fair! After they worked so hard? With the moats and the dragons and the towers and hacking through bramble with witches flying after them and does the slipper fit or doesn't it and then finally it's all okay and what!? They wind up sprawled all over some stupid theme park in Florida!? That is sick!

GLYNDA: (Beat, then lamely.) It's sunny. (At Cindy's look.) And you can see they're all quite ... content.

CINDY: Forty acres of horses and lovers ... (Thought, turns dismayed to Glynda.) Oh no! I bet they didn't even ... (get a chance.)

GLYNDA: Into the sunset! Hoof beats, anticipation! A brief and shining moment. En route. It does keep them smiling. Forever. (Lamely.) Jellybean?

CINDY: I just lost my appetite.

GLYNDA: This isn't an easy job for me either, being a part-time guide here!

CINDY: ... You’re an actress?

GLYNDA: A fairy.

CINDY: (Flatly) A fairy.

GLYNDA: An unemployed fairy.

CINDY: Oh yeah?

GLYNDA: You couldn't tell?

CINDY: No, actually, I never met one before.

GLYNDA: SO you think!

CINDY: Right. Do I get three wishes or what?

GLYNDA: That's genies! That's what I mean! Fairies are completely misunderstood and it's impossible to find work. A tooth here, a tooth there ... We are the endangered species nobody talks about. Children ignore our random acts of kindness. Cynics abound. Our forests are cut down and we have nowhere left to go. There are horrible waves in the air from your new-fangled inventions! Oh, how we used to dance to the music of the wind-up Victrola as it wafted gently to the bottom of the garden. And now? We get struck down by words flying through the ether like arrows! "You've got mail!" A million times a night! And what does it mean anyhow? (Disdainfully.) And the New Age?

They've got their angels and their channels but what about us? Nobody cares. You think you're disillusioned? I'm disenchanted! I wish I could cry. Fairies can't cry you know. Of course you don't know! Why would you? (Breaking down.) Now all I can get is "After!" And it's not even supposed to exist. It's strictly OffLimits ... after all these millennia, I'm NOWHERE!

CINDY: I'm really sorry...I don't know what to say ... (Looks at her uniform ID tag.) "Glynda." Should I clap? Would that help?

GLYNDA: That doesn't work. Applause and barking and car horns all scare us to death. And by the way, we hate caraway seeds.

CINDY: Oh. Then, well what can I do?

GLYNDA: Just make up your mind! (A puzzled look, pointedly.) Before you get back to the Bus.

CINDY: (Jolted back to reality.) Bus.

GLYNDA: (Coaching.) Your beau on the Bus?

CINDY: Oh ... (Remembering problem.) Him. Right.

GLYNDA: Yes him! That was why you wandered off, wasn't it?

CINDY: Yeah, I guess it was ... It's such a big commitment! I mean I don't know if! can go through with it. I just ...

GLYNDA: You must decide!

CINDY: Well, if this is Happily Ever After, you know what you can do with it!

GLYNDA: Well, if you've decided against a wedding celebration, I'll just fade out now.

CINDY: Wait! I, I didn't say that. All I said was I don't know ...

GLYNDA: Tell me: Does he have a horse?

CINDY: (With grudging belief) No, they don't ride horses anymore, Glynda.

GLYNDA: (Wistfully.) Things change.

CINDY: Yes!

GLYNDA: But fairies don't. Neither do fairy tales. (Tiny ping sound.)

CINDY: (At ping, small smile.) ... He's got a Jeep Wrangler.

GLYNDA: Ah. (Tiny ping sound.)

CINDY: It was really mine and I sold it to him. That's how we met. See I was selling my car to finance a trip to Nepal, and this guy shows up to buy it and then, we wound up going trekking together and, he's really, uh ... (Doesn't say "great," but her recall is positive, romantic) He's ... we've got a lot in common and ... y'know he's a journalist too .. .in fact, he's covering this place ... I mean not this!

(Stops abruptly, staring at field, realizing.) So, you gotta write your own After. That's the deal, huh?

GLYNDA: Exactly!

CINDY: (Gesturing to field.) It's gotta be better than ...

GLYNDA: It could be!

CINDY: (Getting her point.) Yeah ... It could be anything! Right?

GLYNDA: Right! (small ping.)

CINDY: Thank you! You know what? I want to go back now!

GLYNDA: Good! (As Cindy turns) But you can't take anything with you.

CINDY: What do you mean?!

GLYNDA: Memory. We can't let you ...

CINDY: Look, I swear I won't print this story, okay?

GLYNDA: It's too dangerous. It would end your species.

CINDY: Okay, okay, but you can't make me forget!

GLYNDA: Don't force me to do anything unkind.

CINDY: Now what are you, a hit fairy?

GLYNDA: (Touches Cindy with wand, immediate effect. Cindy freezes in place. Casts spell with wand.) Now, forget this field and all tale-spinning, the horse, and all the princes grinning. Forget The End and make a new beginning! Forget the pumpkins, the mice, and all witchcraft, forget it all in love and laughter. Forget, and keep your dream of After. (Ping.)

CINDY: (Opens her eyes, slight disorientation.) Hello? ... I thought I... Excuse me? Where's the bus!?

GLYNDA: It worked! There you are, we were just getting worried about you. I'm your tour guide, Glynda?

CINDY: Don't I know you from ... ?

GLYNDA: The Bus. We must hurry. There's a nice young man on line who's waiting for you ...

CINDY: (Face brightens.) Oh yeah, him! We're getting married this weekend!

GLYNDA: How lovely! I'll be there ... (Correcting her slip.) in spirit.

CINDY: (Disoriented.) I feel like, like I forgot something.

GLYNDA: Like a toothbrush? Here. I carry extras.

CINDY: Thanks ... Did you see a tape recorder anywhere?

GLYNDA: Is this yours? (Handing her recorder with tape dangling.) I think it. .. dropped.

CINDY: (Shaking her head.) I'm feeling kinda weird.

GLYNDA: (Steering her away from site) Probably something you ate in the cafeteria. Did you eat an apple? Don't worry it's just a spell. .. Now what did you say your name was?

CINDY: Cindy? (As they exit)

GLYNDA: Cindy! Ah, I knew a Cindy once upon a time, long, long ago ...
```

---

## IC-0553: Agnes of God

- Title: Agnes of God
- Author (byline): John Pielmeier
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: June 1982
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: AGNES, DOCTOR
- Teaser before the introduction: Yes
- Spoken words (computed): 1609
- Already set (do not supply): none

### Source block (context only)

```text
Author: John Pielmeier
ISBN: 978-0573630224
Publisher: Samuel French, Inc.
Date (Month/Year): June 1982
```

### Introduction (context only: never use it for content warnings)

```text
Agnes of God by John Pielmeier
```

### Performance text (classify this)

```text
AGNES: (singing off stage) *Gratias agimum tibi propter magnam gloriam tuam. Domine Deus. Rex coelestis. Deus pater omnipotens. Domini Fili unigenite. Jesu Christe

DOCTOR: (Pg 3-4) (Speaking over Agnes) The baby was discovered in a wastepaper basket with the umbilical cord knotted around its neck. The mother was found unconscious by the door to her room, suffering from excessive loss of blood. She was indicted for manslaughter and brought to trial. Her case was assigned to me, Doctor Martha Livingstone, as court psychiatrist, to determine whether she was legally sane. I wanted to help this young woman, believe me . . .

DOCTOR: (Pg 17) Hello. I’m Doctor Livingstone. I’ve been asked to talk to you. May I?

AGNES: (Pg 20-22) You want to talk about the baby, don’t you?

DOCTOR: Would you like to talk about it?

AGNES: I never saw any baby . . . I think they made it up.

DOCTOR: Do you remember the night they said it came? Did it hurt?

AGNES: Yes.

DOCTOR: Where did the baby come from?

AGNES: They say it came from the wastepaper basket.

DOCTOR: But where did it come from before that?

AGNES: From God.

DOCTOR: After God, before the wastepaper basket.

AGNES: I don’t know what you’re talking about! Everybody wants to talk about the baby, but I never saw the baby, so I can’t talk about the baby, because I don’t believe in the baby! Nobody listens to me! (Silence) (Pg 24) Where do you think babies come from?

DOCTOR: From their mothers and fathers, of course. Before that, I don’t know.

AGNES: Well, I think they come from when an angel lights on their mother’s chest and whispers into her ear. That makes good babies start to grow. Bad babies come from a fallen angel. (Silence) Bad babies cry a lot and make their fathers go away and their mothers get very ill and die sometimes. Mummy wasn’t very happy when she died and I think she went to hell. (Silence) (Pg 33) But she watches. She listens.

DOCTOR: (Pg 42-46) Agnes, have you ever thought of leaving the convent? For something else?

AGNES: Oh no. There’s nothing else. It makes me happy. Just being here helps me sleep at night.

DOCTOR: You have trouble sleeping?

AGNES: I get headaches. Mummy did too. She’d lie in the dark with a wet cloth over her face and tell me to go away. Oh, but she wasn’t stupid. Oh no, she was very smart. She knew everything. Things nobody else knew. She told me I would enter the convent, and I did. She even knew about this.

DOCTOR: How did she know . . . about this?

AGNES: Somebody told her.

DOCTOR: Who?

AGNES: You’ll laugh.

DOCTOR: I promise I won’t laugh. Who told her?

AGNES: An angel. When she was having one of her headaches.

DOCTOR: Do you believe that your mother really saw them?

AGNES: No. But I could never tell her that. She’d get angry. She’d punish me.

DOCTOR: How would she punish you?

AGNES: She’d . . . punish me.

DOCTOR: Did you love your mother?

AGNES: Oh, yes. Yes.

DOCTOR: Did you ever want to become a mother yourself?

AGNES: I could never be a mother. I don’t think I’m old enough. Besides, I don’t want a baby.

DOCTOR: But if you did want one, how would you go about getting one?

AGNES: From someone who didn’t want a baby.

DOCTOR: Like you?

AGNES: No! Not like me. A mistake.

DOCTOR: How did your mother get you?

AGNES: A mistake! It was a mistake!

DOCTOR: Is that what she said?

AGNES: You’re trying to get me to say that she was a bad woman, and that she hated me, and she didn’t want me, but that is not true, she was a good woman, a saint, and she did want me. You don’t want to hear the nice parts about her—all you’re interested in is sickness!

DOCTOR: Agnes, I cannot imagine that you know nothing about sex. . .

AGNES: I can’t help it if I’m stupid.

DOCTOR: . . . that you have no idea who the father of your child was . . .

AGNES: They made it up! It’s not my fault!

DOCTOR: . . . and that you don’t believe that you carried a child!

AGNES: It was a mistake!

DOCTOR: What, the child?

AGNES: Everything! Nuns don’t have children!

DOCTOR: Agnes. . .

AGNES: Don’t touch me like that! Don’t touch me like that! (Agnes lashes out at the doctor, who moves away) I know what you want from me! You want to take God away. You should be ashamed! They should lock you up. People like you! (Long beat)

DOCTOR: (Pg 55) (to audience) I wanted to free Agnes – I wanted to make her well.

AGNES: I’m not sick!

DOCTOR: (Pg 57-62) But you’re troubled, aren’t you?

AGNES: That’s because you keep reminding me. If you go away, then I’ll forget.

DOCTOR: And you’re unhappy.

AGNES: Everyone’s unhappy! You’re unhappy, aren’t you?

DOCTOR: Sometimes, yes.

AGNES: Only you think you’re lucky because you didn’t have a mother who said things to you and did things that maybe weren’t always nice, but that’s what you think, because you don’t know that my mother was a wonderful person, and even if you did know that you wouldn’t believe it because you think she was bad, don’t you?

DOCTOR: Agnes.

AGNES: Answer me! You never answer me!

DOCTOR: Yes, I do think your mother was wrong, sometimes.

AGNES: But that was because of me! Because I was bad, not her!

DOCTOR: What did you do?

AGNES: I’m always bad.

DOCTOR: What do you do?

AGNES: (in tears) I breathe!

DOCTOR: What did your mother do to you? (No answer) If you can’t tell me, shake your head, yes or no. Did she hit you? (Agnes shakes her head “No”) Did she make you do something you didn’t want to do? (Agnes nods“Yes”) Did it make you uncomfortable to do this? (Agnes nods“Yes”) Did it embarrass you? (Agnes nods“Yes”) Did it hurt you? (Agnes nods“Yes”) What did she make you do?

AGNES: No.

DOCTOR: You can tell me. She’s dead. She can’t hurt you anymore.

AGNES: She can. She watches, she listens.

DOCTOR: Agnes, I don’t believe that. Tell me. I’ll protect you from her.

AGNES: She. . . makes me. . . take off my clothes and then. . . she makes . . . fun of me.

DOCTOR: She tells you you’re ugly? (Agnes nods“Yes”) And that you’re stupid.

AGNES: Yes.

DOCTOR: And you’re a mistake.

AGNES: She says. . . my whole body. . . is a mistake. She says. . . if I don’t watch out. . . I’ll have a baby. And then. . . she touches me down there with her cigarette. (Silence) Please, Mummy. Don’t. I’ll be good, I won’t be your bad baby anymore. (Silence)

DOCTOR: Agnes, dear, I want you to do something. I want you to pretend that I’m your mother. Only this time, I want you to tell me what you’re feeling. All right?

AGNES: I’m afraid.

DOCTOR: (She takes Agnes’ face in her hands) Please. I want to help you. Let me help you. (Silence) Agnes, you’re ugly. What do you say to that?

AGNES: I don’t know.

DOCTOR: Of course you do. Agnes, you’re ugly. What do you say?

AGNES: No, I’m not.

DOCTOR: Are you pretty?

AGNES: Yes.

DOCTOR: Agnes, you’re stupid.

AGNES: No, I’m not.

DOCTOR: Agnes, you’re a mistake.

AGNES: I’m not a mistake! I’m here, aren’t I? How can I be a mistake if I’m really here? God doesn’t make mistakes. You’re a mistake! I wish you were dead! (shocked silence, then Agnes begins to cry. The doctor takes her in her arms)

DOCTOR: Agnes, I’d like to ask a favor of you. You can say no, if you don’t like what I’m asking. I’d like permission to hypnotize you. There are some things that you might be able to tell me under hypnosis that you aren’t able to tell me now. (to audience) The hypnosis took weeks to achieve, not minutes. An hour a day . . .

AGNES: (Pg 77-79) I’m frightened!

DOCTOR: Don’t be. I cannot make you say or do anything you do not wish to say or do. Sit back and relax. Imagine that you are listening to a chorus of angels. Breathe freely and deeply. Close your eyes, Agnes. When I count to three, you will wake up. Can you hear me?

AGNES: Yes.

DOCTOR: Good. Would you like to tell me why you’re here?

AGNES: Because I’m in trouble.

DOCTOR: What kind of trouble?

AGNES: (Agnes struggles, then says) I had a baby. I was afraid.

DOCTOR: Why were you afraid?

AGNES: Because I wasn’t worthy.

DOCTOR: To be a mother?

AGNES: Yes. (she begins to cry softly)

DOCTOR: (Pg 81-83) All right, Agnes, I’m going to ask you to open your eyes. When you do, you will see your room at the convent. It is the night about four months ago when you were very sick. All right, Agnes, let’s go to your room. Ready? What do you see?

AGNES: My bed. A crucifix.

DOCTOR: Anything else? (Silence) Agnes? What do you see? Something different? Something that’s not normally in the room?

AGNES: A wastepaper basket. (Silence)

DOCTOR: Do you know who put it there?

AGNES: No.

DOCTOR: Why do you think it’s there?

AGNES: For me to get sick in.

DOCTOR: Are you ill?

AGNES: Yes. (Pg 84-85) Oh God! (she holds her stomach in a contraction) Oh my God. Water. . . it’s all water!

DOCTOR: Why doesn’t anyone come?

AGNES: They can’t hear me. Get away from me. Go away! I don’t want you here!

DOCTOR: Is someone in the room with you? Agnes?

AGNES: Don’t touch me! Don’t touch me! Please! Please don’t touch me! (Contraction) You want to hurt my baby! You want to take my baby! (Screams and contraction) It’s not my fault, Mummy. It’s a mistake, Mummy. (Pg 105) Your fault! It’s all your fault!

DOCTOR: (Pg 85) Agnes, it’s all right. It’s all right. It’s me. Doctor Livingstone. It’s all right.

(Agnes relaxes)

AGNES: (Pg 105-108) (softly) I hate him. I hate him for what he did to me.

DOCTOR: Tell us who he is so we can find him and stop him from doing this to other women. Who did this to you?

AGNES: God! God did it to me! It was God! And now I’ll burn in hell because I hate Him!

DOCTOR: Agnes, you won’t burn in hell. It’s all right to hate him. (beat) Agnes, what happened to the baby? It was alive, wasn’t it? Wasn’t it?

AGNES: YES!!! (Silence) I don’t want to remember.

DOCTOR: Mother Miriam was with you, wasn’t she? You saw it all, didn’t you? (no response) What did she do? (Silence) Agnes, what did she do?

AGNES: (Simply and quietly) She left me alone with that little. . . thing. I looked at it and thought, this is a mistake. But it’s my mistake, not Mummy’s. God’s mistake. I thought, I can save her. I can give her back to God. (Silence)

DOCTOR: What did you do?

AGNES: I put her to sleep. I tied the cord around her neck, wrapped her in the bloody sheets, and stuffed her in the trash can.
```

---

## IC-0554: Al Takes a Bride

- Title: Al Takes a Bride
- Author (byline): Gary Sunshine
- Work: The Best American Short Plays 2000-2001
- Publisher: Applause Books
- Publication date as stated: Sept 2002
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: CHARACTERS, TIME, SETTING, ALICE, FREDA
- Teaser before the introduction: Yes
- Spoken words (computed): 2544
- Already set (do not supply): none

### Source block (context only)

```text
Author: Gary Sunshine
Book: The Best American Short Plays 2000-2001
ISBN: 978-1557834805
Publisher: Applause Books
Date (Month/Year): Sept 2002
```

### Introduction (context only: never use it for content warnings)

```text
Actress 1: On a moonlit riverbank, over a hundred years before the U.S. Congress passes the Defense of Marriage Act, two young southern women imagine their wedding to each other.

Actress 2: Award-winning writer Gary Sunshine re-tells the story of Freda Ward and Alice Mitchell and their forbidden love which made headlines in every major newspaper in America during the early 1890s Actress 1: With gay marriage still opposed, and in fact, illegal in most states, this play makes an important statement

Actress 2: Al Takes a Bride by Gary Sunshine
```

### Performance text (classify this)

```text
CHARACTERS: ALICE MITCHELL, 19, a formidable and imposing presence, plain but handsomely attractive, quiet with a streak of wild. FREDA WARD, 19, a southern belle, meticulously put together, impeccable manners, pleasant as can be.

TIME: June 1893. Dusk.

SETTING: A riverbank outside of Memphis, Tennessee.

[ALICE MITCHELL stands in full, somber skirts, hands on hips, her back to the audience. A large cloth bag, stuffed, sits downstage of her. FREDA runs up behind ALICE and grabs her around the waist. ALICE instinctively whirls around and knocks FREDA to the ground, screaming:]

ALICE: I'll kill you before you can breathe!

FREDA: It's me, Al. It's only me. It's your Freddy.

ALICE: Fred? Now what were you doing that for? That's a stupid thing to do-

FREDA: -Wasn't stupid. Just having some fun. Been with my mama all day today- [FREDA struggles to get up.]

ALICE: -Lord, your mama's an old pigface-

FREDA: I wouldn't mind if she was just crazy, that'd all be interesting, like your mother, but my mama's just a big bore and my, you look particularly lovely today. [Silence.

ALICE stands, transfixed.] That's sweet, you're having a fit. You know, your fits help me see more of your eyes, all popped open by the awe, the "Mmmmm, Fred's so gorgeous, she jams up my veins and makes me forget how to blink!"

ALICE: I'd blush if I knew how.

FREDA: I'll teach you how to blush. I'll teach you fineness and elegance and all the proper body functions like cooin' and flutterin' and forgetting how to sweat.

ALICE: [Clearly in on it now.] No ma'am. I ain't doin' it. Sweatin's my best thing. I'm the best sweater in these here parts and I ain't givin' up my title! [ALICE and FREDA laugh. FREDA grabs ALICE by shoulders and kisses her hard. ALICE accepts, ALICE suddenly breaks it.]

FREDA: No Al, please, don't stop me.

ALICE: What time is it?

FREDA: [Looking at her pocketwatch.] Seven. Please Al, let me show you how much I-

ALICE: -Didn't feel real-

FREDA: -You embarrassed? Who all's gonna see?

ALICE: Felt like a play kiss.

FREDA: Look, they put us apart 'til the next world takes our souls. So if our being together is an impossibility, we're not really here, right? And if we're not really here, doing naughty things can't be dangerous, right?

ALICE: You just playacting for the squirrels and the trees and the colors. I know the difference.

FREDA: Fine. I'll find a cloud for us and we can kiss there. No, no, then we'd be entertaining the angels, and God might pop in too, so forget it, we'll have to find somewhere else, maybe under the river?

ALICE: Don't you know what tomorrow is?

FREDA: Course I do. Your family's moving to Chattanooga tomorrow. On account of you and me. Our little mess. I know it. But I don't want to think on it right now. Can't we just be here with the river and the air and us and leave the thinking to, I don't know, the goldfish maybe? [ALICE laughs.] You love me, Al? 'Cause I just adore you.

ALICE: No you don't. You just talking sweet 'cause you think you ain't going to see me again. What time is it?

FREDA: The same time. Now how could you say something so terribly awful like that? I love you now and always will. Not just when you're in Memphis but everywhere, no matter where you'll be. [Pause. FREDA strokes ALICE's hair. ALICE crosses to her bag. She pulls out a man's business suit.]

FREDA: Whatcha doing now? Oh Al, you brought

ALICE: -You going to shield me?

FREDA: Well you can't just take off your clothes ... [ALICE removes her dress.]

ALICE: Thought we could play, you know, one last time. For now. [FREDA hustles to shield ALICE.]

FREDA: Men'd find you pretty, if you let them.

FREDA: If you ask me, it's a little uncharitable how you act to all those nice men. I am never rude, not to Willie Watkins or Jimmie Lynn or Ashley Roselle-

ALICE: -Specially not to Ashley.

FREDA: Well, Ashley's the nicest of all. You'd like Ashley too, if you gave him half a chance.

ALICE: I'm sure I would. Here, help me with this.

FREDA:... wait Al. I know this suit.

ALICE: It's my Daddy's.

FREDA: How's that, Al? Or should I say Alvin.

ALICE: Take your pick. [ALICE whips out a shaving brush, cup and a straight razor.]

FREDA: Oh Al, this ole thing scares me to no end!

ALICE: I'll get the lather going.

FREDA: I'm not so good at it.

ALICE: Every good wife grooms her man. That's her privilege. Now, let's go, and watch my nose, I only got one.

ALICE: A man don't like to be shaved in silence. Makes him suspicious. Like the barber's got thoughts.

FREDA: Well Al, what should I say?

ALICE: Sing, Fred. Sing for me. [Beat.] I said sing!!!! [Soft.] Please. It's my comfort. [FREDA stops, approaches the stump and resumes the shave while humming a beautiful Irish lullaby. When she finishes shaving:]

ALICE: What time is it, Fred?

FREDA: A shave and a kiss later. Why you so interested in the time?

ALICE: Not a lot of time left, that's all. Now walk a few paces and tell me if you can see it, under my nose.

FREDA: We can just pretend it's there, Al. That's the beauty of pretending. Things are only as real as you want them to be. You don't need an honest mustache, just one you see in your head.

ALICE: I've shaved it three times this week. Swear it's going to come in fuller than the Senator's.

FREDA:. Can't you make your family stay in Memphis forever? Then at least we could go on like this, indefinitely. We'd have our times, plain and simple. Wouldn't matter what else happened in our lives, what we did or who we did it with, we could always come back to each other, here by the river under the moon, or before the day-

ALICE: -Our times is when it’s dark out? [Short beat.]

FREDA: And even if I was to marry

ALICE: -Marry???-

FREDA: -Or get in some sort of permanent

ALICE: -Who you marrying, Fred?

FREDA: -situation, -You, you could get swept off your feet

ALICE: -Tell me, it's Ashley-

FREDA: -Not what I'm talking about, Alice. All I'm saying is that if you want something bad enough, you got to figure out how to give in a little. Compromise. Now it's too late. Your parents carting you off cause you let them believe the truth about us. You let them just swipe our truth from your hands, you gave it to them, 'stead of protecting it.

ALICE: I brought you something, Fred. [ALICE crosses to her bag and pulls out a wedding dress.]

FREDA: It's gorgeous! It's the most gorgeous old thing I ever seen! [Pause.] Oh, Gawwwd, I'm putting it on! [FREDA changes quickly as ALICE watches for others, occasionally peek-ing at FREDA, who speaks the following while changing:] Now a dress like this cannot be worn by any old one. You, Al, perfect as you may be, could not do this dress justice. Wouldn't work, no ma' am. Cause you don't believe in it. You don't believe in finery, but you appreciate it on me. Oh, if only I had a mirror. Oh, did I get caught there, no. Al, do up the back, do it up! [ALICE crosses and adjusts FREDA's dress.] Now where's the veil?

ALICE: I'm sorry. I couldn't find it.

FREDA: [Very upset.] I would never, ever get married without a veil! It's practically in the Bible, Thy bride shalt wear a veil, oh you don't know it because you're something of a heathen. The wedding's called off. I'm incomplete!

ALICE: You're much too beautiful to hide behind a veil. [Pause.]

FREDA: Oh! In a Memphis wedding, the bride and groom walk down the aisle sweeter than in any other city in the world. And just before they kiss, they're supposed to feel God's Divine right hand pushing the smalls of their backs. If the couple can feel His Divine right hand, they know they're truly blessed. The pressure of God's hand pushes them together, and their lips lock in a holy partnership, protected from all bad, all sadnesses, for a long, long time to come. If I could choose my life . . . I love you, Al.

ALICE: I see things, Fred. A future There's a way to what we both got to have ... I made a way, Fred. For us to be together.

FREDA: Now, Alice, the whole town knows you Mitchells are up and moving tomorrow,

ALICE: I'm not going. I got choices. Plenty. So do you, if you'd stop and think on it.

FREDA: It's cast in stone, Al. Your mama and daddy's made up their minds, they've got to follow it through, told my folks and everything. They feel it's their duty to save you-

ALICE: *Judge Kettlerson’ll* marry us, as long as we go away and never come back. Just like we said before-

FREDA: -When, we never said it-

ALICE: -Course we did, many times- We played it in your room, downstairs in your daddy's store, in the attic over the church, here-

FREDA: -Just playing, not for real! My God, Alice. Leave here? [Beat.] Where would we go?

ALICE: St. Louis first. The packer's setting off at eight. Then to New Orleans. That's why I keep asking you about the time. I got tickets and everything. [She takes them out and shows them to FREDA.]

FREDA: And how're we going to live, Al, betcha didn't think for a second about that.

ALICE: I'll be Alvin Mitchell, that's why I'm aiming for that mustache. If I'm a man, I can get work doing all sorts of things. Start small, maybe a clerk for the railroad, maybe working with my hands.] We'll get a little spot to live in New Orleans. Every Saturday night we'll make dinner for lots of friends, different than the kind we got here. You can sing, maybe we'll get a piano- [Softly] Marry me, Fred. Now, right here. The Memphis ceremony you dream about.

FREDA: And be happy?

ALICE: It could be us.

FREDA: But you don't know for sure.

ALICE: In my heart-

FREDA: -No! Not your damned heart! I need evidence. Proof that things go that way, someplace. New Orleans. Proof. [Pause.]. ALICE and FREDA stand looking at each other. FREDA, scared and ashamed, gazes away and begins to unbutton the back of her dress:]

FREDA: I'm just going to take this beautiful gown off right about now. Save it for another time. [ALICE grabs her by the arm and squeezes in silence.] You're hurting me. [Pause.] I can't feel my fingers, Al. [Pause.) I can't feel my fingers!

ALICE: Keep it on.

FREDA: I can't go back into town like this.

ALICE: You're going to marry me now, Fred. You're scared but that's fine because I told you over and over, I'll protect you, that's why I'm wearing the suit.

FREDA: I want to take this dirty old dress off! Now!!! [ALICE crosses to FREDA and tears the dress off her. FREDA remains standing. Silence.]

ALICE: There. You're free now. [FREDA begins to remove the rest of her dress, then puts on her regular clothes.]

FREDA: I know you're angry. Wedding breaks down right in front of your eyes, you've got good reason to hate me and everybody else in the world. And it's not that I don't appreciate your planning, I do, I swear, it's the sweetest thing I ever heard and I wish, I so do wish I could accommodate you. But I can't.

ALICE: I understand.

FREDA: You do? You truly do? [She hugs ALICE, and sits her down next to her.) My Lord, that's a relief. 'Cause I'd hate to be a bad spot in your thoughts, ‘specially when, for a while, that's the only place you'll see me, in your thoughts.

ALICE: It's hard. For us. People and all. Too hard.

FREDA: I was meant to walk in the lights of Memphis, Al. Loved and cared for. Walking down an aisle carrying wildflowers or roses, proud of who I grew up to be, proud of who I'm marrying because the world is admiring us ... you can't understand because it never crosses your mind Al, it's not part of you, and that's fine, it really is fine for you. But I cannot imagine anything else for me.

ALICE: You marrying anybody Freda?

FREDA: I'd marry you Al, but like you said, it's just too hard.

ALICE: You marrying anybody, Freda?

FREDA: Stop it, Al.

ALICE: Are you marrying anybody Freda? Are. You. Marrying. Anybody. Freda?

FREDA: [Screaming.] Ashley Roselle! [Pause. With great calm:] Ashley Roselle asked me to marry him, and I've accepted his proposal.

ALICE: Hunh. [ALICE begins to clean up, putting things back into her bag, but leaving the razor for last. She pauses, looks up:]

FREDA: My folks are giving me a second chance. I've decided to take it is all. I wanted to tell you right away, but you've always been so edgy when it comes to Ashley, and what with your going away, I thought I'd write it in a letter.

ALICE: A letter. Hunh.

FREDA: He asked me several times, Ashley wore me down. [ALICE picks up the razor.]

ALICE: Funny, if I was a man, I don't think I'd ever shave off my whiskers. I'd let the hair grow. Let it grow til it reached the ground. Nobody'd say nothing to me about it. Not a word. [ALICE opens razor and, at first, gently brushes it across her neck, from the bottom up.]

FREDA: Sweet Jesus, what are you doing Al?

ALICE: Grooming.

FREDA: Oh. But you don't have any ... Alice! You're cut! [ALICE has drawn blood on her neck and up toward her chin.]

ALICE: My blood's cold. Just like they say.

FREDA: [Racing over to stop her.] Don't kill yourself Alice. , Not over me! [FREDA tries to grab razor away from ALICE. ALICE gets her in a headlock and holds the razor to FREDA's throat.]

ALICE: Can you feel God's right hand now, Fred?

FREDA: Yes, Al. I feel it!

ALICE: Can't live in this world if you're with somebody else. Wouldn't be able to think, Fred, think smart things like how the fish are and "Don't kill yourself, Alice!" Can't live here if I know your best thoughts are going to somebody else.

FREDA: You stopped loving me, is that it? If that's so, then kill me, do it now, I'd like that. [ALICE moves to cut FREDA, but stops herself] Or are you too selfish to love me entirely, in the real world and all? I thought more of you, Al. Thought you had strength of character. Thought you gave freely to what you cared most about. If you changed that much, then maybe the world's gone dark. And I shouldn't live in it. If that's so, then kill me, do it now.

ALICE: You, you lied-

FREDA: -But if you got a ounce of feeling in you, a ounce of what I feel for you, then you'll- [ALICE drops FREDA to the ground. FREDA sobs for a second, then recovers, pulls herself up, gathers her belongings, starts to leave, then looks at ALICE, who has crumpled to the ground. FREDA takes out a handkerchief, crosses to ALICE, and starts to wipe her neck. ALICE fights back screams of pain.]

ALICE: [Finally starts to sob.]-You can't leave me. You can't leave me.

FREDA: Got to. Got to have my life. And you got to have yours.

[FREDA exits.] [Pause.] [ALICE slowly pulls out the razor and opens it. She gazes off in the direction FREDA has just exited.]
```

---

## IC-0555: Always . . . Patsy Cline

- Title: Always . . . Patsy Cline
- Author (byline): Ted Swindley
- Work: Not specified
- Publisher: Ted Swindley, Inc.
- Publication date as stated: 1990 (Revised 08/09)
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: LOUISE - VOICE-OVER, PATSY, LOUISE, TOGETHER
- Teaser before the introduction: Yes
- Spoken words (computed): 2031
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ted Swindley
ISBN: N/A
Publisher: Ted Swindley, Inc.
Date (Month/Year): 1990 (Revised 08/09)
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: On September 8, 1932 a very special little girl entered this world. Her given name was Virginia Patterson Hensley.

ACTRESS 2: Many years later, the world would come to know her as County Music sensation- PATSY CLINE.

ACTRESS 1: This selection “Always…Patsy Cline” is more than a tribute to the legendary country singer who died tragically at age 30 in a plane crash in 1963.

ACTRESS 2: It’s based on a true story about Cline’s friendship with a fan from Houston named Louise Seger, who befriended the star in a Texas honky-tonk in l961, and continued a correspondence with Cline until her death.

ACTRESS 1: The show’s title was inspired by Cline’s letters to Seger, which were consistently signed

TOGETHER: “ALWAYS… Patsy Cline” By Ted Swindley
```

### Performance text (classify this)

```text
LOUISE - VOICE-OVER: Well, friends, let's not keep you waiting any longer tonight. Let's have a swell Grand Ole Opry welcome for our special guest star, Miss Patsy Cline [Music cue]

PATSY: Howdy everybody, and welcome to the Grand Ole Opry!

Honky Tonk Merry-Go-Round
I'M ON A HONKY TONK MERRY-GO-ROUND
MAKING EVERY SPOT IN TOWN
STARTING OUT EARLY, COMING HOME LATE
EVERY NIGHT WITH A BRAND NEW DATE

I'M ON A HONKY TONK MERRY-GO-ROUND
ACTIN' LIKE A FOOLISH CLOWN
STILL RACIN' THOSE BLUES THAT YOU LEFT WITH ME
WONDERIN' IF I'LL EVER BE FREE

LOUISE: Now the first time I ever heard Patsy Cline sing it wasn't on the Grand Ole Opry. No, the first time I ever heard Patsy Cline sing she was in my livin' room. That was in January, 19 and 57. Well this particular momin', I was doin' the dishes, as usual, but subconsciously, I was listening to that television. When all of a sudden I heard this voice that absolutely stopped me in my tracks. I said, " My God, that sounds like I've always wanted to sing." So, I threw the spoons and forks in the kitchen sink and went tearing into the living room to see who it was.

I said, "Get outta my way kids." and I looked and there was this chunky little country girl leaning back and leadin' into a wonderful country song called "Walkin' After Midnight" and I'll tell you I have never heard a voice that impressed me so. [Music cue – Louise acts like she’s watching her on the TV]

PATSY: I GO OUT WALKIN' AFTER MIDNIGHT
OUT IN THE MOONLIGHT JUST LIKE WE USED TO DO
I'M ALWAYS WALKIN' AFTER MIDNIGHT
SEARCHIN' FOR YOU

LOUISE: That TV audience went wild. Then [Arthur] Godfrey said, "Well, little lady, I hope that record sells like hotcakes." And then Patsy said,

PATSY: "I just hope it sells like records."

LOUISE: And it did! Well, she must have been on that show every morning for about two weeks, and every morning you would find me right in front of that TV, waiting. [She does the "TV pose" as if she is watching the TV staring up mesmerized] One day, Godfrey said "Now here's a little girl from Virginia that I think you're going to be hearing a lot from." Then she just dropped out of sight. But I never forgot that voice and I never forgot the feeling it gave me.

By 1961, I was divorced, Yahoo!, hallelujah! And I had taken a job as an electronics technician. Well, we can't all be hairdressers! Anyway, the man I worked for loved country music, and he used to keep the radio in the lab tuned to one of our leading country music stations. Anyway, one day, all of a sudden, I heard that voice again and it absolutely stopped me in my tracks. Well they didn't say who it was, so I called the radio station to find out and they said, "That was Patsy Cline singing "I Fall to Pieces." Well, I called Hal Harris, the local disc jockey, right while he was on the air and I said, "HEY [Very Bossy], you play that one again for me.", and he did. [Music cue]

PATSY: I FALL TO PIECES EACH TIME! SEE YOU AGAIN I FALL TO PIECES HOW CAN I BE JUST YOUR FRIEND

LOUISE: Patsy's music made me feel so alive every time I heard it. I nearly worried that poor man at the radio station half to death. I'd call him every afternoon four or five times a day and everyday he'd say, "Louise, I just played your song.", and I'd say, "Well, flip her over and play the other side and in an hour play my song again." Well, this went on for about two months. Well one day I called in my request, as usual, and he said, "Oh, incidentally, she's coming to town. She's going to be over at the Esquire Ballroom next Friday night."

So I told my bunch, I said, "We're gonna wear our western clothes and we're gonna get there at 6:30." My boyfriend said, "For Cryin' in a bucket, Louise, the band don't even start until 8:00." I said, [emphatically] "I DON'T CARE, WE'RE GONNA BE THERE AT 6:30." Sometimes you just have to talk to them that way.

(During the rest of Louise’s speech, Patsy continues to softly hum “I Fall to Pieces” as she does a check of the stage and instruments, check music, mics and lights, etc. Toward the end of the speech, Patsy leaves the stage and goes to a juke box in the corner of the bar)

When we went stompin' in out there, they were still cleaning the place. Except for the people at the bar we were the only ones there. Well I picked us out a table right in front of the bandstand. My boss said, [note: Louise affects a voice for her boss as a high pitched nasal old man.] "Damn, Louise, we won't even be able to hear ourselves talk." I said, "HEY!- we did not come here to hear ourselves talk. We come here to hear Miss Patsy Cline."

We'd been sittin' there about 15 minutes when I saw this girl come in across the way. She walked across the dance floor and sat down by the juke box. [PATSY sits on the barstool] She looked so lonesome sitting there. I was the only one watching her, nobody else was paying her any attention at all.

PATSY: It Wasn’t God Who Made Honky Tonk Angels
AS I SIT HERE TONIGHT THE JUKEBOX PLAYING
THOSE TUNES ABOUT THE WILD SIDE OF LIFE
AS I LISTEN TO THE WORDS THEY ARE SINGING
IT BRINGS MEMORIES WHEN I WAS A TRUSTING WIFE

LOUISE: She took off her rain coat [PATSY does so] and laid it on the back of the chair. She had on a pale pink two-piece cotton suit. Well something in my mind went DING! DING! DING! Why, it was just like our minds were talking to one another, like she was saying, "Hello, I'm, Patsy Cline, who are you?" As I looked at her sitting there in that nearly empty ballroom, I wondered what that honky-tonk merry-go-round life of hers is really like. [Louise watches Patsy intently] [Sings softly] SHE'S ON A HONKY-TONK MERRY-GO-ROUND [from opening song] So I just picked myself up [LOUISE hoists her bosom up and makes a beeline to PATSY, but then approaches her very timidly] and I walked right on over to her, I said, "Excuse me, Miss Cline.”

PATSY: (looking at Louise and smiling) Yes? (Patsy extends her hand for a handshake, which Louise shakes rather exuberantly)

LOUISE: My name’s Louise and I just want you to know how fond I am of your music. And I was wondering, if you don’t mind and if you have the time, Would you just stop by our table and say hello? (to audience) Now y’all listen up, ‘cause you aint gonna believe what she said next.

PATSY: Well, why don’t I just come over there and sit with y’all?

LOUISE: (screaming and almost fainting) OH MY GOD, WE WOULD BE THRILLED! Patsy, come on over and sit down with us.

PATSY: Well, help me out with this song first. Come on In And Make Yourself at Home NOW COME ON IN AND SIT RIGHT DOWN AND MAKE YOURSELF AT HOME

TOGETHER: COME ON IN AND SIT RIGHT DOWN AND MAKE YOURSELVES AT HOME. (Louise is clapping as they both dance a do-si-do -- As the song ends, Patsy exits.)

LOUISE: Lord . . . take me now! Well, my friends nearly fell off of their chairs. Patsy come over and sit down and in now time at all we were talking to one another like we’d known each other all of lives, she was no stranger to us. After a while, Patsy asked me if I would do her a favor. She wanted to know if I would go up there and stand by the drummer and make sure he didn’t rush her. YES MA’AM, I COULD SURELY DO THAT . . .

(Louise takes her place on the stage and instructs the drummer as to the correct rhythm. Louise gets into the music and her physical moves are big and bold. Lots of arm, hip and leg movements for comic effect)

PATSY: Your Cheatin’ Heart
YOUR CHEATING HEART WILL MAKE YOU WEEP
YOU'LL CRY AND CRY AND TRY TO SLEEP
BUT SLEEP WON’T COME THE WHOLE NIGHT THROUGH
YOUR CHEATING HEART WILL TELL ON YOU

(Louise holds the final cut-off for the ban before ending the song with a final big comic move.) (laughing) Good job, Louise!

LOUISE: (nonchalantly in her new role as manager and music director) Thanks, Patsy. You did good too.

PATSY: (to audience and especially Louise) Lord’s a mercy. I ain’t doing too bad for a girl who can’t even read notes and don’t even know what key she sings in. I feel like I’ve come a long way from working in a drug store during the day to help support my momma and then singing in clubs at night in Winchester Virginia. Next month I go up to Las Vegas. I’ll be doing four shows a day seven days a week. And I’ll tell ya, this cat’s ass will be draggin’ the bottom out of that desert (Both Patsy and Louise share a laugh) Oh, it’s a great life. I don’t want to get rich. I just want to live good. Right, Louise?

LOUISE: You betcha! (to audience) Well, Patsy brought the House down. That place was filled with people just screaming and yelling. People were stomping and hollering for more. She signed autographs and a lot of her fans took pictures.

PATSY: Louise, honey, I have got to go, I’ve got to catch a plant to Dallas tomorrow.

LOUISE: You’re never going to get a taxi out here this time of night. We’ll take you, but first we’re going to my house for some bacon and eggs. (to audience) and I want you to know that lady come right in MY kitchen and stood right alongside me frying up the bacon and eggs, just as big as you please. It was just like finding the sister I never had. When we finished eating, me and Patsy just sat around MY kitchen table and poured out hearts out.

We talked about children . . . and husband problems, broken hearts, loves lost, loves found. We sounded like two people writing country songs.

PATSY: Louise, I think the good Lord broke the mold when he made you.

LOUISE: Yeah, you’re right about that! [Then] Patsy told me about her marriage. She said she and Charlie weren’t getting along too well. She told me about the hell raising arguments they would have and I knew only too well how she must be feeling. (Patsy sings the following song as an internal monologue about her troubled marriage)

PATSY: Crazy
CRAZY, I'M CRAZY FOR FEELING SO LONELY
I'M CRAZY, CRAZY FOR FEELING SO BLUE
I KNEW, YOU'D LOVE ME AS LONG AS YOU WANTED
AND THEN SOMEDAY
YOU'D LEAVE ME FOR SOMEBODY NEW

LOUISE: We traded stories until the wee hours of the morning. Then Patsy said . .

PATSY: Louise, honey, I truly have enjoyed it but I’ve really gotta go, I’ve gotta catch a plane to Dallas tomorrow. Thank you for everything Louise – I want your address cause I don’t want us to lose touch.

LOUISE: Goodnight, Patsy (Louise exits)

PATSY: Just a Closer Walk (Patsy prayerfully sings. She is a woman with many struggles and
her life is not as easy as it may seem)
JUST A CLOSER WALK WITH THEE
GRANT IT, JESUS, IS MY PLEA
DAILY WALKING CLOSE TO THEE
LET IT BE, DEAR LORD, LET IT BE
LET IT BE, DEAR LORD, LET IT BE (Patsy exits)

LOUISE: So we exchanged addresses, but you know how it is, you figure, yeah, well,that will be the end of that. I’ll never hear from her again. [But] you know what? In less than two weeks, I received the first in a long series of letter and telephone calls from Miss Patsy Cline. I tell you something, that country gal was a winner. (Louise takes out a letter and reads silently while Patsy does the voice over)

PATSY: . . . I’m going home next Tuesday and while there, they are proclaiming a Patsy Cline Day in my hometown. Ain’t that a kick in the head? The Mayor is gonna be there and recognize me and so one. Anyway, it sure is a good feeling. I can’t really believe it. I still want all of you to come down and see us at the Opry. Hope to see you again soon.

TOGETHER: Love, Always . . . Patsy Cline.

LOUISE: One morning about two years later, I was driving to work and they come on the radio and said that Patsy Cline had been killed in an airplane crash on her way back to Nashville. She was thirty years old. It had only been six years since I first heard Patsy sing on the Arthur Godfrey show.

PATSY: (off-stage) I GO OUT WALKIN' AFTER MIDNIGHT
OUT IN THE MOONLIGHT JUST LIKE WE USED TO DO
I'M ALWAYS WALKIN' AFTER MIDNIGHT
SEARCHIN' FOR YOU

LOUISE: That’s been a long time ago, but I still call that radio station and I still ask them to play Patsy Cline for me. And as I look at the letters that she wrote to me, I remember . . . and I know she meant it when she signed each and every one of them Love . . . Always . . Patsy Cline.
```

---

## IC-0556: Amy’s Answering Machine: Messages from Mom

- Title: Amy’s Answering Machine: Messages from Mom
- Author (byline): Amy Borkowsky
- Work: Not specified
- Publisher: Atria Books
- Publication date as stated: April 2001
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: AMY, AMY’S MOM, NEWS REPORTER, GANG MEMBER, GANG MEMBER 2, ANDREW, HOSPITAL WORKER, DAIRY BOARD, WOMAN, WOMAN 2
- Teaser before the introduction: Yes
- Spoken words (computed): 1376
- Already set (do not supply): none

### Source block (context only)

```text
Author: Amy Borkowsky
ISBN: 978-0743422284
Publisher: Atria Books
Date (Month/Year): April 2001
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Does your mother call you in a panic whenever there's a storm warning for your area?

ACTRESS 2: Does she act as though it's her duty to alert you to every health story on the news?

ACTRESS 1: Have you ever been briefly out of touch with your mother only to find she's phoned everyone short of the National Guard to track you down –

ACTRESS 2: Or, just maybe, are you that mother?

ACTRESS 1: Take comfort in knowing you're not alone!

ACTRESS 2: This is Amy’s Answering Machine:

ACTRESS 1: Messages from Mom

TOGTHER: by Amy Borkowsky
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles

Actress 1: Amy, Gang Member 2, Hospital Worker, Dairy Board

Actress 2: Amy’s Mom (Note: She peppers her words with Jewish phrases – See glossary at the end of this selection), News Reporter, Gang Member, Andrew, Woman, Woman 2

AMY: (Pg 14) I have a radio that gives weather forecasts every few minutes, and a TV with a channel devoted entirely to the weather. So why does my mother always feel compelled to call me up with a weather report?

AMY’S MOM: (BEEP) Amila?

AMY: (Pg 9) You may wonder why my mother calls me “Amila” (pronounced AY-muh-luh) when my name is actually Amy. The answer is that, as a classic Jewish mother, my mom follows the tradition of adding an “ila” to my name as a term of endearment. And here and there, my mother uses some other Yiddish phrases.

AMY’S MOM: (Pg 14-15) Amila? I hope you’re on your way home. I just heard on the weather, there’s a big storm headed for New York and they’re expecting four to six inches in the city, with accumulations of up to a foot in the outlying areas. So if I were you. I wouldn’t go shlepping to any outlying areas. On the weather map, all over New York, they had snowflakes the size of bagels. So if you have to go out, make sure you bundle up. And wrap a scarf around your face to protect it, ‘cause y’know, there was that man who climbed Mount Everest and lost his entire nose. Okay, honey? I love you. Bye.

AMY: Somehow I just don’t see anywhere I would shlep to as being quite parallel to climbing Mt. Everest.

NEWS REPORTER: Our guest today is Amila Borkowsky, the first woman ever to reach the summit of Macy’s department store. So, Amila, what was it like up there?

AMY: Words just can’t describe it. The view of Linens and Housewares was breathtaking.

NEWS REPORTER: Now the question everyone want to know is, what did you buy?

AMY: Nothing. By the time I got there, they didn’t have the one item I really needed.

NEWS REPORTER: What was that?

AMY: A new nose! *******

AMY’S MOM: (Pg 29-30) (BEEP) Amila? I don’t think you went to bed yet, but maybe you’re in the tub. I wanted to know if you happened to catch the story on the new squirting scam. Apparently, the way it works is, you’ll be walking along the street, and some guy or maybe a woman will squirt you from behind with a bottle of ketchup. Then someone else who’s in cahoots with that person will say, “Excuse me, Miss, but there’s some ketchup on your sweater.” And then, just as you go to wipe it, they grab your bag and that’s the end of that. So if somebody tries to point out any ketchup on you, you can just say something like, “I’m well aware of the ketchup – in fact it matches my pants that have a big blob of relish.” Then as they’re looking down at your pants, you can make a quick qetaway. All right, I hope you’re doing good, and I’ll talk to you tomorrow. Bye-bye.

AMY: In a world where innocent people are being randomly attacked with guns, knives, and AIDS-filled syringes, I find it hard to lose even a millisecond of sleep worrying that someone’s going to come after me with a bottle of ketchup. *******

AMY’S MOM: (Pg 57) (BEEP) Hi, Amila. It’s me. Y’know the red terry robe you wore when I came to visit – it’s like a ruby red with a belt? Do you still wear that or did you throw it out? I just wanna tell you that if you take out the garbage or run to the mailbox, you may wanna put on something else, because my friend Eileen’s grandson said that red is a gang color. Okay, Sweetie-pie? Talk to you later.

AMY: Now what are the odds that two violent street gangs are going to decide to have it out on the twelfth floor of a Murry Hill doorman building, at the exact moment that I’m carrying out a bag of trash, totally oblivious to the Crips and the Bloods lining the hallway? They’ll be yelling . . .

GANG MEMBER: Don’t go after Julio – he’s not the leader!

GANG MEMBER 2: It’s . . . it’s the Jewish girl in the bathrobe! *******

AMY: (Pg 72-74) The TV! It only feeds my mother’s already obsessive concern over my safety.

AMY’S MOM: (BEEP) Yeah, hello, Amila. They just said on TV, “It’s ten p.m., do you know where your children are? And I’m thinking, I don’t know, so I figured I’d call you, mamascheinz. You must be in the bathroom or something. Give me a buzz when you’re don, okay? All right, bye-bye. (Amy, sleeping soundly, snores)(BEEP) Amila? It’s five to eleven and I know you have work tomorrow. I’m getting ga little worried. Call me when you get the message.

AMY: This message was followed by FOUR separate messages from my friends, Michael, Sherry, Alison and Leslie, each saying that my mother had called them looking for me!

ANDREW: (BEEP) Hi, Amy. Yeah, it’s Andrew. I just got a call from your mom about ten minutes ago, and she wanted to know if you were spending the night at my house. I told her we broke up four years ago.

HOSPITAL WORKER: (BEEP) Hello, Miss Borkowsky? I’m calling from NYU Hospital. Someone called here claiming to be your mother and wanting to know if you’d been admitted.

AMY: So where was I, you ask? In my own bed. Sound asleep. I’d conked out early and had just turned my ringer off. When I work up the next morning, I was sooooo mad. I could only imagine who she would have called next . . . (Ring Ring)

DAIRY BOARD: Good morning, National Dairy Board.

AMY’S MOM: Uh, yes, I’d like to find out how I can get my child’s picture on a milk carton.

DAIRY BOARD: How long has the child been missing?

AMY’S MOM: A very long time. I’d say well over ninety minutes.

DAIRY BOARD: Okay, Ma’am, is this a boy or a girl?

AMY’S MOM: It’s a girl – my Amila.

DAIRY BOARD: And what was she wearing when she disappeared?

AMY’S MOM: Let’s see . . . she probably had on a silk blouse with maybe a dark blazer, a matching skirt, and a pair of pumps.

DAIRY BOARD: Was she playing dress up?

AMY’S MOM: No. But she mentioned today she had to go see a new client.

DAIRY BOARD: Ma’am, how old is your Amila?

AMY’S MOM: Thirty-four and three quarters

*******

AMY: (Pg 97-98) People are always debating whether it’s harmful for kids to watch too much TV, but I think the bigger problem is what happens when your parents watch too much TV!

AMY’S MOM: (BEEP) Amila? I just talked to you. Where’d you go? Anyway, I was watching the news and they had a story about the Hell’s Angels motorcycle club. They flashed a shot of a big bear of a guy from Greenwich Village who was covered in tattoos, and on the back of his motorcycle was a very pretty girl. Was that you? She had your hair, and she was wearing a green blouse that looked like the one that I gave you for Chanuka. You know how I feel about motorcycles!

AMY: (Sarcastically) I did understand her confusion. There are so few women in Manhattan with brown, wavy hair that, really, who wouldn’t assume it was me? I’m constantly getting comments . . .

WOMAN: Excuse me, but I was just noticing how completely unique your hair is. What color would you call that?

AMY: Brown.

WOMAN: Can you write that down? I want to ask my colorist about it.

*******

AMY: (Pg 8) I love my mother, but . . . I know my mother means well, but . . . (Pg 84) Halloween . . . REALLY? I outgrew Halloween when I was around twelve!

AMY’S MOM: (BEEP) (in her best scary voice) Boooooo, Amila. Booooooo. Okay, don’t get scared. It’s just me, honey. Tomorrow’s Halloween, and I just want to warn you to throw out anything that looks suspicious in your trick-or-treat bag. Like if you should happen to find a hole in a candy bar, it could mean that someone stuck it with a hypodermic needle, all right? Happy Halloween!

AMY: How could she even imagine me trick-or-treating at this age?

AMY’S MOM: (Pg 74) Thirty-four and three quarters (Pg 84-85) (Knock, knock, knock)

WOMAN 2: Who’s there?

AMY: Trick or treat!

WOMAN 2: My goodness! What a wonderful costume! Can you wait just a minute?

AMY: Actually, I’m not wearing a cos . .

WOMAN 2: Staaaaanley! Bring the camera! There’s a little girl dressed as Jerry’s friend Elaine! She has the hair and everything! It’s amazing. She even looks like she’s in her thirties!

AMY: That’s because . . .

WOMAN: Your mommy must’ve spent quite some time making your costume!

*******

AMY: (Pg 11) So . . . If your own mother drives you crazy, I hope you now know . . . You are not alone!

AMY’S MOM: (BEEP) (Pg 26) Amila . . . it’s me again!
```

---

## IC-0557: And I and Silence

- Title: And I and Silence
- Author (byline): Naomi Wallace
- Work: Not specified
- Publisher: Broadway Play Publishers
- Publication date as stated: Dec 2013
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: YOUNG JAMIE, YOUNG DEE, YOUNC DEE, ACTRESS 1, ACTRESS 2, DEE, JAMIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1773
- Already set (do not supply): none

### Source block (context only)

```text
Author: Naomi Wallace
ISBN: 978-0881455700
Publisher: Broadway Play Publishers
Date (Month/Year): Dec 2013
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Jamie and Dee are teenagers when we meet them in Jamie’s cell in some unidentified prison in an undisclosed (but vaguely Southern) American city in 1950.

ACTRESS 2: The 1950s – often looked back on today with nostalgia, especially when the slogan “Make America Great Again” is heard.

ACTRESS 1: But this play focuses on those who were present but invisible…in a society that was still very oppressive, segregated, and rife with inequality

ACTRESS 2: Young Jamie is black and Young Dee is white, so it takes courage as well as ingenuity for the uneducated and dim-witted Dee to keep sneaking over from the “white wing” in her campaign to make friends with smart and feisty Jamie.

ACTRESS 1: Two young lives going nowhere fast

TOGETHER: And I and Silence by Naomi Wallace
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray a character at 2 different time periods of her life. This is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments. The original script calls for 2 actresses to be cast for each role (ie YOUNG JAMIE/DEE and JAMIE/DEE)

(In a bare prison cell. YOUNG JAMIE is standing alone in her cell, looking out at something we can't see. YOUNG DEE enters. YOUNG JAMIE turns slowly and sees her. They say nothing for a long moment, just looking at one another.)

YOUNG JAMIE: I don't know you.

YOUNG DEE: I've seen you. Over and over. (Beat) I'm in cell block four.

YOUNG JAMIE: White block.

YOUNG DEE: Yeah. Trying to get here for weeks. I want . . .

YOUNG JAMIE: (interrupts) Knew you wanted something.

YOUNC DEE: -to be friends.

YOUNG JAMIE: Well I don't.

YOUNG DEE: Few months ago, I saw old Mister Crackle the guard knock a bowl of hot chili right out of your hands. Hit the floor, splash.

YOUNG JAMIE: I picked the bowl up.

YOUNG DEE: Yep. But Mister Crackle, he knocked it out of your hands a second time. Me. I would have let it lay. Eight times he knocked that bowl outta your hands. I counted. And you picked it up eight times 'til Mister Crackle gave in. That's the kind of friend I want.

YOUNG JAMIE: I don't care what you want and I don't need a friend.

YOUNG DEE: I'll be seventeen in two months.

YOUNG JAMIE: I'm already seventeen for five months now.

YOUNG DEE: You got nine for robbery.

YOUNG JAMIE: Accessory.

YOUNG DEE: I got nine years too.

YOUNG JAMIE: Don't care.

YOUNG DEE: We could do time together. We could make something . . . Plans for when we get out. My name's Dee.

YOUNG JAMIE: Blue eyes make me cold.

YOUNG DEE: Didn't have no family other than [your brother]. He's dead. You're alone. Jamie is all alone. That's what they say.

YOUNG JAMIE: Hear me, girl. Get the hell out. (They stare each other down)

YOUNG DEE: I'm sorry about your brother.

YOUNG JAMIE: Marcel. His name was Marcel. He had a piece of wood in his pocket, made it look like a gun. We went into that grocery store together. Man in the store had a real gun. Shot Marcel in the neck. . . . We're not friends yet. Weeks later (Dee shows up again in Jamie’s cell during lunch break)

YOUNG JAMIE: Might never happen, you and me being friends. (Beat) You were in the hole. That's what they say. They say you don't sleep. You sit and scream at night.

YOUNG DEE: Who says I scream? I'll kick their face.

YOUNG JAMIE: I never been in the hole. Yet. But I been hit. Me and some girls once we sat up front at dinner time, at your table. Guards hit us on the back 'til we moved. We got worms in our bowls so fat we name 'em. You and your table get porridge thats clean.

YOUNG DEE: Not my fault.

YOUNG JAMIE: Maybe it is. (Beat) What's it like in the hole?

YOUNG DEE: Dark. Like sleep without the hours.

YOUNG JAMIE: You shouldn't scream at night. (YOUNG DEE and YOUNG JAMIE regard one another.)

YOUNG JAMIE: What will we be when we get out? I can sew. Make a dress. Can you?

YOUNG DEE: A little bit. Shopkeepers? We'll make dresses. Put them in the window.

YOUNG JAMIE: You got to rent a shop. You got money stashed away?

YOUNG DEE: Nope.

YOUNG JAMIE: Stupid. Neither do I.

YOUNG DEE: Bookkeepers?

YOUNG JAMIE: You can read?

YOUNG DEE: Not much. You?

YOUNG JAMIE: (nodding) My Momma was a parlourmaid.

YOUNG DEE: A servant?

YOUNG JAMIE: She called herself a parlourmaid. Raised me and Marcel up on her own.

YOUNG DEE: She dead?

YOUNG JAMIE: Drowned . . . Cleaning floors. (YOUNG DEE laughs briefly. Then realizes YOUNG JAMIE is not playing)

YOUNG DEE: You can't drown cleaning floors.

YOUNG JAMIE: One time I found her on the kitchen floor. One time on the porch. She had blackouts. Ever since she was a girl. She must of had one and fell with her face in the bucket. That's how they found her. Me and Marcel went to get her body where she worked. I asked for her pay. Gave us half a week, said she hadn't worked past Wednesday.

YOUNG DEE: We could be servants.

YOUNG JAMIE: She made enough to feed us. Sometimes she took me with her. I watched her work. You don't need much. . . . Two buckets. With strong handles. One for each of us.

YOUNG DEE: Rags?

YOUNG JAMIE: And soap. Lots of water. And a clean dress. You got to look professional. If you're dirty they think you can't clean. Got to be spiffy.

YOUNG DEE: Bingo. That's settled then. We'll be servants. Work the finest houses. Get paid in cash!

YOUNG JAMIE: Get leftovers!

YOUNG DEE: Get hand-me-downs!

YOUNG JAMIE: Get anything they throw away! But we'll have to practice.

YOUNG DEE: Yeah. Practice. Weeks later (Dee shows up again in Jamie’s cell during lunch break)

YOUNG JAMIE: Heard they gonna move you. You in the hole three times. One more time and they move you to maximum.

YOUNG DEE: Nobody's gonna move me.

YOUNG JAMIE: Once in the hole for coming here. One time for screaming. You can't get in trouble again. We got years left.

YOUNG DEE: Eight.

YOUNG JAMIE: And a half. You got to stop it, Dec. You got to act right. What you do this time?

YOUNG DEE: Nothing, Christ.

YOUNG JAMIE: Dee.

YOUNG DEE: At breakfast there's this guard, Monkfish, we call him, on account of his smell. Well Monkfish he comes to the table and he drinks my juice. Why's he got to drink my juice every morning? Why not spread it around? So one mornin' I pour my juice into the girls next to me, then I put my cup under the table and I piss in it. Then I put the cup right there on my tray, waiting for Monkfish. He leans over me like he always does. Picks up the cup and drinks deep.

YOUNG JAMIE: Oh no, Oh no, Dee! Did he drink it?

YOUNG DEE: All the way down. Then his face turned pucker and his eyes go wide. Best moment of my life.

YOUNG JAMIE: He hit you.

YOUNG DEE: Didn't stop til I passed out. But I was floating I was so damn glad.

YOUNG JAMIE: Weeks in the hole.

YOUNG DEE: Months would have been worth it. Let’s work.

YOUNG JAMIE: Sure then. Start with dusting. You'll need a rag. But you got to use it right. Because whoever's gonna hire you, they gonna watch you. They watch to see if you love your work. Now you hold your cloth (Beat) like a bird. You hold it and let it flitter its wings across the dust.

YOUNG DEE: Flitter.

YOUNG JAMIE: Flitter.

YOUNG DEE: You're makin' this up. . . Sorry. Go on.

YOUNG JAMIE: You want to be a servant you got to have something no other servants got. Grace. Good cheer. Style. And flitter. (YOUNG JAMIE holds the rag out to YOUNG DEE. YOUNG DEE takes the cloth gingerly, awkwardly)

YOUNG JAMIE: Do the book shelves. (YOUNG DEE looks around, "sees" some imaginary bookshelves and dusts them, leaning over.) Don't hunch when you dust. If you got to do the book shelves low down, curtsey as you dust. Like this.

(YOUNG JAMIE shows YOUNG DEE how to do it. YOUNG DEE tries, not very well.)

YOUNG JAMIE: That's a bend not a curtsey. Don't ever bend. Over. (YOUNG DEE is silent some moments, then calmly speaks.)

YOUNG DEE: In the city. Outside our apartment. There were stairs. When I left for school, when I returned, I'd count them. (YOUNG DEE stalls.)

YOUNG JAMIE: (Encouraging her) You'd count them.

YOUNG DEE: Seventeen steps up, seventeen steps down. My mother would hide her wages. Keep something back for her and me. He'd hit her every time she did it and she did it every time. (YOUNG DEE stalls again.)

YOUNG JAMIE: Seventeen steps up . . .

YOUNG DEE: And seventeen steps down. One night he threw her down the stairs and she tried to stop herself falling and both her hands broke at the wrist. Snap. Snap. When she stood up, she held her arms out to me. I ran to her but her hands were just. Hanging off her wrists. She couldn't hold me. I stuck a bread knife in his side. (After a moment) Can we polish the silver?

YOUNG JAMIE: Sure. Vases and mirrors and candelabras.

YOUNG DEE: Can . . . del . . . a . . . bras.

YOUNG JAMIE: You'll have to know how to say it: "Ma'am, I've finished polishing the candelabras".

YOUNG DEE: I did it with a flitter, Ma'am.

YOUNG JAMIE: No, no. Silver you polish with a swick, swick. It's all in the elbow.

(laughing together)

YOUNG DEE: Jamie. I've never been so . . . Even when I was out there.

YOUNG JAMIE: Me either.

YOUNG DEE: In here it’s like hell but all I feel now is –

YOUNG JAMIE: happy.

TRANSITION

ACTRESS 1: Fast forward 8 ½ years. Both girls have been released from prison into a world rife with racial discord.

ACTRESS 2: Eager to put their housekeeping skills to work so they can earn a living, the friends apply for housekeeping jobs in the posh neighborhoods.

ACTRESS 1: But freedom from prison isn’t exactly how they had envisioned it.

ACTRESS 2: Their hopes and dreams quickly crumble to dust.

ACTRESS 1: Finally . . . the friends stop lying to one another and admit to the humiliating cruelties that have broken their spirits and eaten away at their souls.

(The present. In a small room, JAMIE and DEE are facing one another, poised, serious. Their room is made up of a minimum of furniture.)

DEE: You going to congratulate me?

JAMIE: Why? Oh, you got the job?

DEE: Yep. I got it. Seven others waiting outside for hours, soaked to the bone. But she chose me. She asked me what hours. I said

JAMIE: Any.

DEE: Yep. Asked me about silver. I said (Imitates the voice): "l live to polish, Ma' am. Gives me a powerful sense of

JAMIE: achievement." You start tomorrow?

DEE: Seven A M. Your day?

JAMIE: Washed the curtains. Seven rooms. Pile reached the ceiling. She gave me lunch to eat. Leek soup. Delicious. With celery and onions. And a piece of bread.

(JAMIE takes the bread from her pocket.) I brought you the bread.

DEE: You have it.

JAMIE: I saved it for you. You didn't eat today.

DEE: Not hungry . . . (long pause as the “fake” happiness dies out completely) We were happy when we were inside. Sometimes.

JAMIE: When we were together.

DEE: Here, we can't go out together. We can't sit together. We can't walk together anymore. Folks on the street see us together, everyone thinks you're my maid. Me, have a maid? How could I ever afford a maid? So we tell [them] the truth: that we're both servants. That we're friends. What do we get then? An orange crush bottle flying through the air. Then another 'cross my back. Guts from the butcher in your hair. Doors slamming behind us-

JAMIE: (Interrupts) Quit your whinin'. Guts in my hair is nothing. Bottle 'cross my back is nothing. I walk the street alone to work I never know what's flying through the air. Piss pot from the second floor. Dog shit. People cursin' me, white people, your people, stick out a leg and trip me.

DEE: They're not my people.

JAMIE: But when you walk to work you okay, Dee. You okay. It's only when you walk with me you in trouble.

DEE: I wish I could kill people and get away with it. (JAMIE just shakes her head in exasperation.) When we were inside at least our bellies were full. We got to see each other and we weren't hungry.

JAMIE: We got soup for dinner.

DEE: No we don't. Stop lying. We haven't had soup for three days. There's no money. We've got a couple more weeks here then they'll kick us out.

JAMIE: Then what are we going to do?

DEE: Nothing. Let's do nothing. Both of us. (Beat) Ever again.

JAMIE: What do you mean?

DEE: I can't go out there anymore. Not without you. I can't do it. You can't either.

We should. Quit. Just quit. (JAMIE takes this in some moments, in silence.)

JAMIE: I want to live.

DEE: Like this? Like this? You want to live like this?

JAMIE: (Angry) You should be ashamed.

DEE: There's no place for us. The streets don't want us.

JAMIE: That'll change.

DEE: Bullshit.

JAMIE: So is what you're thinkin'.

DEE: A place where there's no cold 'cause winter forgot what cold was. Where there's no being hungry. That world is ours.

JAMIE: (Beat) You think you're the only one? I can't get quiet in my head. Nothin' in my skull but loose change, rattlin', rattlin' and it don't stop.

DEE: (Gets a butcher knife from the kitchen area then whispers) Yeah, but I'm gonna stop, Jamie. I'm gonna stop. Are you with me? (Dee kneels. JAMIE comes to kneel beside DEE. The women are both calm, as though at the center of a storm.)

DEE: (hands knife to Jamie) Do me first, Jamie. 'Cause I'm a coward. I might change my mind.

JAMIE: You're not a coward. (JAMIE abruptly stabs DEE in the stomach. DEE doubles over, holding her stomach) If this is what it is. Here with you. Then I don’t mind. (JAMIE takes DEE's hand and puts the knife in it but holds onto DEE's hand.)

DEE: (Whispers to her) Jamie. (JAMIE, with DEE helping, pushes the knife into her own stomach.)

JAMIE: (Almost surprised) It hurts.

DEE: I'm happy, Jamie. (crying)

JAMIE: So am I. (beat) Hush. I hear it . . . it’s coming for us. Be quiet. It’s all right now.

(Blackout)
```

---

## IC-0558: Annette and Gina from Parallel Lives

- Title: Annette and Gina from Parallel Lives
- Author (byline): Mo Gaffney and Kathy Najimy
- Work: Parallel Lives
- Publisher: Dramatists Play Service
- Publication date as stated: Jan 1998
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ANNETTE, GINA, BOTH
- Teaser before the introduction: Yes
- Spoken words (computed): 1425
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mo Gaffney and Kathy Najimy
Book: Parallel Lives
ISBN: 978-0822213086
Publisher: Dramatists Play Service
Date (Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: Between the raging hormones, eye rolls and unpredictable behavior,

ACTRESS 2: Our perilous journey into adulthood is likely to leave us and our parents exhausted!

ACTRESS 1: And in some cases, wondering . . . what the heck just happened?

ACTRESS 2: We’re here today to give you just a tiny glimpse into the world of teen-age girls --

ACTRESS 1: Italian-American style!

ACTRESS 2: Live from New Jersey . . . Its

TOGETHER: Annette and Gina from Parallel Lives

ACTRESS 1: by Mo Gaffney and Kathy Najimy
```

### Performance text (classify this)

```text
Annette and Gina are watching the movie West Side Story on TV and crying. *Strong Italian accents (Tutorial Video Link at the end of this selection)

ANNETTE: (Pgs 29-36) Oh God.

GINA: What'd you make me watch West Side Story for Annette? It was so sad.

ANNETTE: It is my favorite movie of all time!!

GINA: It was so beautiful.

ANNETTE: I think Natalie Wood sings so good in that movie. And she's got the prettiest hair. I hate my hair, Gina.

GINA: Your hair is fine. You know what I just thought of?

ANNETTE: What did you just thought of?

GINA: That movie is a lot like Romeo and Juliet! No, just think about it! Juliet's family could not stand Romeo and same with Maria, her family hated Tony.

ANNETTE: I can't believe you thought of that. You are so right, Gina. You know who that's exactly like?

GINA: Who? ANNETTE: Who that we know? GINA: Who?

ANNETTE: Me! My mother cannot stand Junior. Why? Because he is not Italian. I mean, he could be the Pope or whatever and she would not care.

GINA: That's so unfair.

ANNETTE: What the movie is trying to tell us Gina is everyone is the same on the inside. It's just like Beanie's poem, "Colors." Colors, blue, pink, purple, yellow - it does not matter.

GINA: Does not matter.

ANNETTE: Does not matter.

BOTH: Period.

GINA: That is so beautiful.

ANNETTE: I've got goose bumps.

GINA: It's like "you can't judge a book by its cover . . . you gotta read it first."

ANNETTE: You can't judge a book by its cover? I mean how would you know what the book is?

GINA: What?

ANNETTE: For instance, say I was gonna buy you a book for your sweet sixteen . . .

GINA: Don't buy me a book. I want a necklace.

ANNETTE: No, just listen. I go into the store and I say I want to buy a book for my play sister Gina but do I say rip off the cover don't show me the cover I don't want to judge? I don't know what the book is. And then I go home, wrap it and give it to you and you say, *why* you give me a book with no cover.

GINA: I don't want a book, Annette

ANNETTE: That's not the point, Gina.

GINA: Just like Maria in that movie. When she fell in love with Tony she had no idea he was a white guy.

ANNETTE: He could dance good so how could she tell.

GINA: I know. There's one thing I didn't get, Annette. You know when she did it with him?

ANNETTE: That's my favorite part.

GINA: Did she know Tony had just stabbed and killed her brother?

ANNETTE: Yes, Gina. Remember? He comes in the bedroom window and he says "I am so sorry I killed your brother," and she still does it with him, like twice.

GINA: That is so beautiful. And they didn't let it affect their relationship.

ANNETTE: Speaking of true love, I forgot to tell you. I talked to Junior in 6th period jewelry and him and Eddie aren't coming over until way later.

GINA: He is so mean to you, Annette.

ANNETTE: Bah, bah, bah, nah, nah, nah.

GINA: Besides the fact he thinks he is God's gift to the borough which he is not.

ANNETTE: Anyway you want to spend the night tonight?

GINA: Okay. You gonna ask your mother?

ANNETTE: Ma! Could Gina spend the night tonight? I know it is a school night. God.

GINA: What does she think you are a moron or something?

ANNETTE: I guess so. What? You want to eat dinner here?

GINA: What are you having?

ANNETTE: Shells and sauce.

GINA: Okay.

ANNETTE: Okay. Thanks, ma! All right! She says yes!

GINA: All right!

ANNETTE: I hope she doesn't make Junior and Eddie leave early like last time.

GINA: Yeah, well you better not sneak out again like last time and leave me here alone. I thought I was supposed to be your best friend.

ANNETTE: Gina, of course you are my best friend. I would do anything for you. Just like Anita and Maria. But I would never do to you what Anita did to Maria, ever.

GINA: What'd she do?

ANNETTE: Don't you remember, Gina? The part where Maria asked Anita to go give a really important message to Tony to meet her. And Anita was *mad*, I forget why, and said, “Just tell Tony Maria is dead." She wasn't dead, she was like down the street doing laundry or something.

GINA: Annette, number one, they called her tramp, number two they killed her boyfriend, that's why she was *mad*.

ANNETTE: I hear what you are telling me but she was Maria's best friend! I mean, what if it was you and me?

GINA: Like we're Maria and Anita? I want to be Anita.

ANNETTE: Okay, okay. Now I come to you as my best friend and I ask you to give a really important message to Junior from me. Like . . . he has to meet me at Tower Records across from the Burger King. But first he has to do something to *make you mad*.

GINA: That should be easy.

ANNETTE: No Gina, play right.

GINA: Okay, like what?

ANNETTE: Like anything. Like, say, he goes into your house, your mother's cookin' dinner . . .

GINA: What's she cookin'?

ANNETTE: Shells and sauce, doesn't matter, it's a Wednesday. And he says your mother's cooking smells. Would you still tell him for me?

GINA: Yeah. My mother's cookin' does smell. You can't fault Junior.

ANNETTE: Okay, well what if he did something worse. He goes into your house and cuts your little sister's legs off. Would you still tell him?

GINA: Well, I would be *mad* he cut my sister's legs off but I would still tell him for you. I mean, nobody has been killed here. You understand what I'm saying to you?

ANNETTE: Gina, just pretend. Okay, say he goes into your house and like *kills* your entire family, blood everywhere. But I beg you, I say Gina, as my best friend, and I'm crying and I have a shawl on my head or something. Please Gina, the cops are after us, I am so sorry, don't go to your house it's a mess. Please tell Junior to meet me at the Burger King, por favor and everything. (After thought) What does por favor mean again?

GINA: It's like "my friend."

ANNETTE: Please Gina you are my best por favor, please tell Junior to meet me at the Burger King. Would you do it?

GINA: Okay . . . granted my entire family is dead and my sister is running around with no legs . . . but my boyfriend is still alive and that was the whole point of that movie, so it's totally different here.

ANNETTE: I would do it for you no matter what.

GINA: You would not. Besides, why do you want to go around with a guy who cuts off little girls' legs and kills whole families for?

ANNETTE: That is not the point, Gina! You love them no matter what they do, it's part of being a womanhood. It's like, sure, Maria would not want Tony to kill her brother and I would not want Junior to cut your little sister's legs off or be mean or *mess* around with other girls, but I know he does.

GINA: I know.

ANNETTE: I know he does - you know he does too?

GINA: What?

ANNETTE: Did Eddie tell you something?

GINA: What?

ANNETTE: About Tina Antonelli.

GINA: What? I just know they were at that party together, I don't know they did it.

ANNETTE: All right, I just have this feeling that they did.

GINA: You do?

ANNETTE: And you know Gina, if I found out for sure he did . . .

GINA: As your best friend, what would you do?

ANNETTE: I would not break up with him because I love him.

GINA: I would. But first I would kill him. Then I would kill Tina Antonelli. Then I would break up with him.

ANNETTE: Gina, I am trying to tell you what is in my heart here, okay? You know, Gina, I mean, I just wish I could make Junior love me as much as I love him, you know? And I know, Gina, that if I had better skin or prettier hair he would love me back.

GINA: It doesn't matter what you look like. You are losing yourself in him, Annette.

ANNETTE: You are right, Gina. I am losing myself. I can't believe you thought of that. You know, sometimes it's like I look in the mirror and think, "Where is Annette? Where is she?" But I just can't get myself back.

GINA: You should just break up with him once and for all.

ANNETTE: Love hurts. On every level, love hurts. I can't believe I thought of that.

GINA: That is so true.

ANNETTE: Love hurts.

GINA: And love is blind.

ANNETTE: Love is a many splendored thing.

GINA: Love is a rose, but you'd better not pick it.

ANNETTE: Love is thicker than water.

GINA: That is so true.
```

---

## IC-0559: Answering 911: Life in the Hot Seat

- Title: Answering 911: Life in the Hot Seat
- Author (byline): Caroline Burau
- Work: Not specified
- Publisher: Borealis Books
- Publication date as stated: Sept 2007
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: OPERATOR 1, OPERATOR 2, STRANGER, TOGETHER, GIRL CALLER, STEPFATHER, CALLER A, CALLER B, DARIUS, CALLER C, CALLER D, CALLER E, AMBER, CALLER F, JAIME, MAN
- Teaser before the introduction: Yes
- Spoken words (computed): 2019
- Already set (do not supply): none

### Source block (context only)

```text
Author: Caroline Burau
ISBN: 978-0873516020
Publisher: Borealis Books
Date (Month/Year): Sept 2007
```

### Introduction (context only: never use it for content warnings)

```text
Actress 1: Answering 911: Life in the Hot Seat Actress 2: by Caroline Burau
```

### Performance text (classify this)

```text
Suggested Roles

Actress 1: Operator 1; Caller A, B, C, D & F; Amber; Jaime; Man

Actress 2: Operator 2; Stranger; Darius; Girl Caller; Stepfather; Caller E

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

OPERATOR 1: (Pg 4) Every day that I sit down at a console in the 911 center, I tell myself that today could be the day.

OPERATOR 2: Today could be the day that I take a call that will change me a little bit forever.

OPERATOR 1: It could be the day that a bell gets rung that I can never un-ring.

OPERATOR 2: Someone could die in my ear today and take a piece of me with him.

OPERATOR 1: Someone could tell me something unimaginable, and I'll have to imagine it.

STRANGER: You're a 911 operator? Wow! I bet you've got some stories.

OPERATOR 1: I get that a lot. The most interesting stories are also the saddest. And you only think you want to hear them until I tell them to you.

OPERATOR 2: They are the stories where mothers and fathers fail their children.

OPERATOR 1: They are the stories where friends and lovers do awful things to hurt each other because of drugs or alcohol, or worse, for no real reason at all.

OPERATOR 2: Or they are the fascinating ways that some people lose their grip on reality.

TOGETHER: Interesting? Yeah, but not amusing.

OPERATOR 1: (Pg 7) 911?

GIRL CALLER: My mom just killed . . . shot herself. Oh my God.

OPERATOR 1: Where's the gun?

GIRL CALLER: It's in her hand.

OPERATOR 1: Is she still alive?

GIRL CALLER: I don't think so. Oh God! No. She's dead.

OPERATOR 1: How old are you?

GIRL CALLER: I'm twelve.

OPERATOR 1: I would never trade places with the cops that had to go out to Dori Swanson's trailer that night.

OPERATOR 2: I would never say that I have a harder job than the medics who had to treat her dead body while her three kids wailed and screamed outside.

OPERATOR 1: I would never want to be the police chaplain who had to try to comfort them.

OPERATOR 2: But I will say this: At least they had a minute or two to get ready.

OPERATOR 1: Then I talk to her stepfather, who is neither upset nor hysterical. (to stepfather) Is she breathing?

STEPFATHER: I'm not in the room with her. I don't want to be blamed for anything.

OPERATOR 1: Then, with me still on the line, Dad's cell phone rings. He sets me down and answers it. To whomever is on the line, he says,

STEPFATHER: Dori shot herself . . . Yeah. Yeah, no s** . . . I gotta go. Bye.

OPERATOR 1: (Pg 8-10) There are many people in the world just like this man. I never knew that until I took this job.

OPERATOR 2: The tough part, the longer you do this job, is remembering that most people aren't like him.

OPERATOR 1: For the next four minutes, I try to convince Dad to keep his three children out of the room where their mother lies dying (or already dead). They can't help her; at this point they can only endanger themselves. Despite my efforts, all I hear are screams overlapping screams; I am no more in control of this scene than I am of the moon in the sky.

OPERATOR 2: At last, the cops and medics arrive, call a Code 4 (meaning okay, for now), and just like that, I'm disconnected from 874 Langer Drive. It's like I've been dan-gling twenty feet in the air, hoping to be let down. Then somebody cuts my cord, and I'm bracing for the fall. That's the moment I first notice that my body is on fire. My hands and face are burning. My head is thick.

OPERATOR 1: I think, Who does that? Who blows their brains out in front of their kids? This is ridiculous.

OPERATOR 2: Later, the shift is over and I think of what it must be like at Dori Swanson's house. I envision a cramped mobile home, maybe one of those single-wide jobs with the rotting wooden siding and the redwood deck, about six by eight. I see the kids' bikes that never got put away for the winter, now partially snow -covered. Outside of the fact that she lived in a trailer, I really don't know any of this. But I took the call; I'm involved. So I put myself there. I imagine it as it must have been, so I can grieve it, then maybe let it go.

OPERATOR 1: Inside, I see the dirt-soaked beige carpet and the second-hand furniture; the TV that's always on. I see the overflowing ashtrays, and the filth, and the empty box of wine the chaplain later told me she drank that day.

OPERATOR 2: I see kids' drawings taped onto the harvest gold refrigerator. I see five lives that will never be the same. Six. I see the bedroom where Dori killed herself, just briefly, but I don't stay there long. I wonder if what the cops saw at the scene is more or less horrifying than the image in my head.

OPERATOR 1: I never met Dori Swanson, but I wish she had found something worth living for in that trailer. **********

OPERATOR 2: (Pg 198) 911?

CALLER A: (female screaming hysterically) He’s hitting me! He’s hitting me and he won’t leave me alone!

OPERATOR 2: (Pg 146) 911?

CALLER B: (male out of breath) Everybody thinks I hit my girlfriend and they called the cops and I ran because I was scared, but I didn’t hit her.

OPERATOR 2: (Pg 202-203) Someday, I’m going to move out of this town. I can’t even take a walk anymore without passing ten house that I’ve sent police to for come medical or domestic or other. Or maybe, someday, I’ll quit. . . [but] vow to hang on a little while longer. I like helping people. **********

OPERATOR 1: Pg 53-55) 911?

DARIUS: I want someone to come arrest my mom. She's doing drugs.

OPERATOR 1: She's doing drugs right now?

DARIUS: Yeah, she locked herself in the bathroom and she's smoking crack. She does it all the time.

OPERATOR 1: What's your name? How old are you?

DARIUS: Darius . . . Fourteen

OPERATOR 1: Okay, we have a couple squads on the way, but I want you to stay on the phone with me so I know you're okay 'til they get there. Does she have any weapons?

DARIUS: No . . . (to Mom in the bathroom) Mom, I told you I's going to call! I don't want you to get high anymore!

OPERATOR 1: Is she mad at you for calling?

DARIUS: Yeah. But I'm tired of this stuff.

OPERATOR 1: Of course you are. You're very brave for calling. Is she going to fight the cops, do you think?

DARIUS: I don't know. She's all different when she's smoking crack. Are they going to hurt her?

OPERATOR 1: (to audience) I've been trained never to make promises on behalf of the officers. If she fights, they might throw her on the floor, kneel on her back, and cuff her. Is it going to hurt? Probably. I hope she doesn't fight. If she gets hurt, will Darius ever call us again, even if he needs us? (to Darius) I don't think so, Darius. (to audience) I wish I could hug the kid. He trusted me with his mom. **********

OPERATOR 2: (Pg 143) 911?

CALLER C: (whispering) There’s someone at the back door trying to get into my house

OPERATOR 2: (Pg 129) 911?

CALLER D: (older lady) I want someone to come out here and look at what my neighbor is doing to me. She waits for me to leave, then she comes in and pees in my laundry basket. She thinks I don’t know it’s her. But I know. **********

OPERATOR 1: (Pg 58-59) 911?

CALLER E: Yeah, we want to make a report for our son. He says he was molested by a guy from our church, and the guy has admitted to it already.

OPERATOR 1: How old is your son?

CALLER E: He's six.

OPERATOR 1: oes the suspect know you're calling police?

CALLER E: Yes, he's here with us.

OPERATOR 1: (to audience) The guy is a drifter, sixty-seven years old. We run his criminal history.

OPERATOR 2: He has seven prior arrests and convictions for molesting children in all different parts of the country.

OPERATOR 1: "Penetration" is the word used to say that he has had sex with boys.

OPERATOR 2: "Contributing to the delinquency of" means that he gave them drugs or alcohol.

OPERATOR 1: “Failure to comply" means he never went to his court-ordered sex-offender treatment. Some of his victims are adults now.

OPERATOR 2: He is almost begging to be thrown back into prison.

OPERATOR 1: Maybe it's the only way he knows how to be saved from hurting children. Maybe he needs the roof over his head. **********

OPERATOR 2: (Pg 56) 911?

AMBER: (calm and blasé) My name is Amber Gillis. My husband was using a table saw and cut two of his fingers off. We’ve got the fingers right here.

OPERATOR 2: (Pg 9) 911?

CALLER F: (elderly man) My neighbor’s clarinet is keeping me up. It’s 8:30 PM, for God’s sake! **********

OPERATOR 2: (Pg 136 -138) Nine . . . (to audience) The phone disconnects before I can say all three numbers. When I call back, a young woman answers. She is out of breath, and there is a baby wailing in the background. (to caller) This is the sheriff's department. Is everything okay?

JAIME: Um, I just wanted him to leave, that's all.

OPERATOR 2: What happened?

JAIME: He hit me in the head and slammed me up against the wall.

OPERATOR 2: Is he still there? Why did you hang up?

JAIME: He's still here, but he took the phone away from me when I tried to call.

OPERATOR 2: (to audience) As I listen, the two lovers argue back and forth about whether he really hit her. Then it turns quiet, except for the baby. (to Jaime) Jamie? Jamie, what's going on?

JAIME: (to man, begging) Don't!

MAN: I'm going to do it. It's time for me to die.

OPERATOR 2: Jamie, what does he have?

OPERATOR 1: (thinking aloud) A gun? A knife? A bomb? What?

OPERATOR 2: The baby wails and begins to sound out of breath. I've never taken care of an infant for any length of time. I wonder what she needs, and wish I could give it to her.

OPERATOR 1: Is she hungry?

OPERATOR 2: Is she scared?

OPERATOR 1: Shouldn't Mom go and hold her now?

OPERATOR 2: After about one minute of this, I begin to realize what Jamie does not: That dips*** isn't going to kill himself. He just wants her to think that he will. To guys like him, women are necessary for survival.

OPERATOR 1: She is a roof over his head and a bed and a body to curl up with at night. He will be as sorry and as suicidal as he needs to be to make sure that he still has her waiting when he pleads guilty to disorderly conduct in front of a disinterested judge, then gets released from jail.

OPERATOR 2: So he keeps it up. Later I learn he was holding a knife to his throat. Must have seen that in a movie or something. Judging by the way she is eating his little act with a spoon, I assume he had no trouble going right back to Jamie's apartment the next day. That's what guys like him live on, women who buy their stupid crap.

OPERATOR 1: I would love to get him on the phone and tell him to go ahead and do it. I know he won't. But I'd love to say, "Go ahead and do it, worm. You don't have the guts."

OPERATOR 2: He's a s***head.

OPERATOR 1: I can't change it.

OPERATOR 2: And she's making her choices.

OPERATOR 1: I can't change her.

OPERATOR 2: I only have her for these few minutes to do anything to help. He's a big boy and she's a big girl. But when I hang up on Jamie and the cops call a Code 4, one in custody, it's not the man's raspy voice or Jamie's pleas that ring in my ears. It's the baby's cries.

OPERATOR 1: (Pg 142) I remind myself frequently: Most people don’t treat each other that way. Sometimes I imagine what their live would be like . . .

OPERATOR 2: Maybe my female caller later moved back to her mom’s house and enrolled in school. Maybe the male got court-ordered into alcohol treatment and it changed his life. It could happen. Growth happens all the time. Good things happen.

OPERATOR 1: It’s just that nobody calls 911 to tell us about it. (long beat) (Pg 181) There is a God, but that He can’t be blamed for all the times that people hurt people.

OPERATOR 2: I believe that God loves his children, but He can only do so much for them and to them without stepping on their free will.

OPERATOR 1: I pray to God very often to work through me. . . . [like I said before]

OPERATOR 2: (Pg 5) The most interesting stories are also the saddest. And you only think you want to hear them until I tell them to you. . .

OPERATOR 1: . . . stories where mothers and fathers fail their children.

OPERATOR 2: Stories where friends and lovers do awful things to hurt each other because of drugs or alcohol, or worse,

TOGETHER: for no real reason at all. (long beat and calls come in; wearily) 911?
```

---

## IC-0560: Anything for You

- Title: Anything for You
- Author (byline): Cathy Celesia
- Work: Take Ten: New 10-Min Plays, edited by Eric Lane and Nina Shingold, Pgs 13-20
- Publisher: Vintage Books
- Publication date as stated: March 1997
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: GAIL, LYNETTE
- Teaser before the introduction: Yes
- Spoken words (computed): 1162
- Already set (do not supply): none

### Source block (context only)

```text
Author: Cathy Celesia
Book: Take Ten: New 10-Min Plays, edited by Eric Lane and Nina Shingold, Pgs 13-20
ISBN: 978-0679772828
Publisher: Vintage Books
Date (Month/Year): March 1997
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS 1: You’ve been best friends forever. You vacation together. . .

ACTRESS 2: You were in each other’s weddings; your husbands are best friends too.

ACTRESS 2: Lynnette and Gail are the best of friends . . . Friends who can share anything!

ACTRESS 1: But times and people change and so do relationships.

ACTRESS 2: So regardless of how awkward the conversation. It’s friends who will do

TOGETHER: Anything for You by Cathy Celesia
```

### Performance text (classify this)

```text
At Rise: LYNETTE sits alone at a table for two, staring into her drink. GAIL approaches the table, a bit harried. She kisses the preoccupied LYNETTE on the cheek, sits.

GAIL: (Pgs 13-20) Sorry I'm late. I was just about to walk out when this rap artist of ours plops himself in the outer office, announces he's not leaving until somebody acknowledges his artistic crisis. This is a kid, nineteen years old mind you, who has a house in the Hamptons and a hot tub for every day of the week, and he's having an artistic crisis. That needs acknowledgment. (She picks up a menu.) Have you ordered yet? (perusing the menu) So I have to sit there for twenty minutes trying to sound sincere when I tell him "It's not so bad, Roger. Money doesn't compromise your art. It just makes it more affordable." When what I really wanted to say was, This is the legal department. We work here. You're feeling screwed up or dysfunctional, go to artistic, bother them. So anyway. . . the squab looks good. What do you think? (GAIL continues to study the menu. LYNETTE leans forward in her chair.)

LYNETTE: I need to have an affair.

GAIL: Hmm? Did you say something?

LYNETTE: I said, Gail, that I need to have an affair.

GAIL: (looking up) You don't mean that.

LYNETTE: Yes I do.

GAIL: An affair?

LYNETTE: Yes.

GAIL: You?

LYNETTE: Uh-huh.

GAIL: But you and Richard

LYNETTE: I know.

GAIL: Then I don't understand.

LYNETTE: Neither do I.

GAIL: So basically you're sitting here telling me for no good reason that you want to

LYNETTE: Not want. Need. Capital N. The big guns.

GAIL: Why?

LYNETTE: I don't know. An overwhelming biological necessity for alternate body types. I don't know.

GAIL: I don't think this is the place we should be discussing this.

LYNETTE: This is exactly the place. You are exactly the person. Gail. If I don't sleep with someone other than my husband very soon, I won't be responsible for myself.

GAIL: Lynette.

LYNETTE: Time bomb. Tick tick tick.

GAIL: Don't you think you're being a little overdramatic?

LYNETTE: No. Tick.

GAIL: Have you met someone?

LYNETTE: No. Although when you get right down to it, everybody's a candidate.

GAIL: You're kidding, right? All right, joke's over, very funny, ha ha, you're kidding.

LYNETTE: Gail, you don't know what it's like. I can't work. I can't sleep. Yesterday I looked at a clock. I forgot how to tell time. I'm losing my mind.

GAIL: You certainly are. Richard

LYNETTE: Is sweet and kind and good, I know. He adapts, no matter how crazy I am. "You're right honey, I'll be more careful, I'll try not to let my heels touch the floor in that irritating manner anymore." I could tell him I want to chuck it all for a sugar cane farm in Borneo and he'd be researching farming techniques and plane fares within the hour.

GAIL: So it seems to me you have nothing to complain about.

LYNETTE: I'm not complaining. But God, if I don't find someone to sear me to the bones I am going to explode. Little pieces of me flying out my office window and over New York, set-tling on some old ladies in the park. Explode.

GAIL: I don't know what to say. You've put me in a difficult position. I love Richard.

LYNETTE: I do too.

GAIL: He and George are best friends.

LYNETTE: Like brothers.

GAIL: And you're my best friend

LYNETTE: (expectantly) Yes?

GAIL: Yes what?

LYNETTE: I'm your best friend. You'd do anything for me.

GAIL: Of course I would, you know that. What are you driving at?

LYNETTE: Sleep with me.

GAIL: What?! You can't be serious.

LYNETTE: I couldn't live with myself if I did it with another man, not to mention what it would do to Richard if he found out. But you

GAIL: Are astonished.

LYNETTE: You're a woman, Gail. It wouldn't be cheating. It would be experimenting.

GAIL: You're out of your mind.

LYNETTE: Will you do it?

GAIL: Of course not.

LYNETTE: Why not?

GAIL: In the first place, no offense, but I'm not physically attracted to you.

LYNETTE: Liar.

GAIL: What did you call me?

LYNETTE: You're lying. You've wanted me from the day we met.

GAIL: Oh, now I agree with you, Lynette, you have gone over the deep end.

LYNETTE: You stare at me. You watch my mouth when I speak. When we kiss hello, you linger a little bit longer than necessary and you breathe in.

GAIL: I can't really have this conversation anymore, okay? Can we order? (pause) I think you should see a doctor.

LYNETTE: You're angry.

GAIL: I'm not, I'm flabbergasted. To think that after all these years of what I thought was a close friendship you would suddenly come up with this insane notion that I -- that we -- I'm married, Lynette.

LYNETTE: I know.

GAIL: And I love George. Not to mention I'm one hundred percent heterosexual.

LYNETTE: I'm going out of my mind.

GAIL: I wish I could help you. I really do.

LYNETTE: You love me.

GAIL: Of course I do. But that doesn't mean I desire you in a sexual manner.

LYNETTE: What about New Year's Eve?

GAIL: (after a pause) What about it?

LYNETTE: New Year's Eve, 1991. The four of us spent it together. I drank too many peach margaritas.

GAIL: I remember. You were so sick. Richard was so angry.

LYNETTE: I thought I'd never stop throwing up. When I finally did, I laid down on the bathroom floor, closed my eyes, and you kissed me. On the mouth.

GAIL: You must have dreamt it, Lynette, I think I would remember.

LYNETTE: I remember thinking, "how soft her mouth is."

GAIL: I did not kiss you, Lynette. I mean, I may have given you a peck on the cheek because I felt sorry for you, but beyond that, you are mistaken.

LYNETTE: Why are you so against this? You have me, I have my fling -- everybody wins.

GAIL: Except Richard, and George.

LYNETTE: We don't tell them. This is a secret between friends. Inviolable.

GAIL: It's not that simple.

LYNETTE: Why not?

GAIL: Lynette, look -- do you want me to fix you up with someone? There are a lot of lesbians in the music business.

LYNETTE: I want you. Youre my friend, I can trust you, there's no danger of falling in love. I was going to say you're honest, but you can't even admit to kissing me when we both know . . .

GAIL: All right, all right, I kissed you, I kissed you! (helplessly) You looked so pretty. Lying. there with your hair spread out over the mat. So vulnerable and so . . . beautiful, actually.

LYNETTE: Sleep with me, Gail.

GAIL: I can't.

LYNETTE: Why not?

GAIL: Because I'm in love with you.

LYNETTE: What?

GAIL: I'm in love with you, Lynette. You think I go around kissing drunken smelly women on the mouth because it's a thing of mine?

LYNETTE: But I thought

GAIL: That my heart couldn't possibly leap every time I see you? That I don't feel profound jealousy when you and Richard reach for each other like any other happily married couple? That my feelings can't be real?

LYNETTE: No, I mean. . .

GAIL: What, Lynette? What did you think?

LYNETTE: I don't know. A harmless crush. Like schoolgirls.

GAIL: Not exactly.

LYNETTE: No. (pause) So where does this leave us?

GAIL: I don't know.

LYNETTE: (after a pause) Maybe I do drink too much.

GAIL: Maybe.

LYNETTE: I have a problem.

GAIL: Yes.

LYNETTE: And you have a problem.

GAIL: Yes.

LYNETTE: What do you think we should do?

GAIL: I think we should order. (They return to looking at their menus)
```
