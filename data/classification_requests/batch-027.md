# Classification request: batch 27 of 63 (40 records, IC-1041 to IC-1080)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-027-reply.json`.

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

## IC-1041: Overcooked

- Title: Overcooked
- Author (byline): Paul Owen
- Work: Overcooked
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1447
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
Two elderly neighbors are, once again, having a discussion which will lead inevitably to another argument. On one side is Fred Gunter, a

very cynical, pessimistic, grouch. He is married to Gail, a quiet and sweet lady. She is an eternal optimist. She treads as lightly as possible when it comes to Fred's mood. On the other side is Henry

Meadows, a polite and decent fellow. He is married to Iris, a loud, abrasive temperamental woman. He treads lightly when it comes to

Iris' unpredictable mood swings. The dynamic of the two marriages has always stirred up very colorful conversation. This happens on a daily basis, but today, the results are a bit more tragic than usual.

(Fred and Henry are both picking up the morning paper at 7:08, as usual. Fred approaches Henry to criticize and aggravate him; Henry sees Fred approaching and takes a deep breath to prepare for the incoming attack... as usual.)

FRED Morning, Henry.

HENRY It is a good morning indeed. Beautiful day.

FRED

I didn't say anything about the morning being good at all. I woke up choking on my own mucus again. Thick, brown spongy mucus. My back popped like a 21 gun salute when I got out of bed. And Gail hasn't

even started cooking the eggs yet. I'm gonna be inside with my paper and have nothing to eat like some kind of a hobo. Can you believe that? A hobo in my own house.

HENRY

Well, I am sorry to hear that, Fred. I already had breakfast. I had a piece of leftover lemon pie and finished it with a cup of coffee. Heard the birds singing and thought I might as well come on outside and get the paper.

FRED

You heard the birds singing? You know why they're singing don't you?

HENRY Well, no, not really. I just know it sounded nice to me.

FRED They're singing because they are getting ready to mate. And they aren't really even singing anyway. They are calling out like some kind of desperate boys at a frat party. It's all they do. So, in essence, you were eating pie while birds are doing the hokey pokey right in your backyard. And that's your idea of a nice morning?

HENRY

Well, since you put it that way, I figure if I was them birds I'd be singing, too. (He laughs to himself. Fred isn't amused in the least.)

Oh come on, Fred, they're just birds. You take things too seriously.

FRED Oh, you wanna have that discussion again, huh? I take myself too seriously? Me? Remember that you are the one that has to eat pie in

the corner because you know your wife isn't in there making eggs for you.

HENRY Don't bring my wife into this, Fred.

FRED You said that I take myself too seriously. You would know. You are married to the most serious person in the neighborhood.

HENRY My wife is a decisive person, yes.

FRED (He laughs.) Decisive? That's one way to put it.

HENRY

Well, if you want to spend your time fussing at me, I think I'll pass today. After all, you need to go get your overcooked eggs. At least if my wife does make eggs, they won't be as dry as an old sandbag.

FRED How dare you mock my wife's cooking!

HENRY I am just repeated what I hear you say every other day, Fred. I've never even had your wife's eggs.

FRED And you never will! You'll just keep eating your pie in the corner like a little child hiding from his old grandmother!

HENRY Old grandmoth... Now, you listen here...

FRED Oh, what are you going to do, get your birds after me?

At this point the wives will both make their first appearance. It is preferred that we never actually see them. Each of the men could step behind the other one and play the part of his neighbor's wife. We would then only watch each man's reactions. But, this is only a suggestion.

(Gail enters.)

Gail Fred, what are you shouting about?

FRED Nothing, Gail, we were just discussing the paper... (He quickly

fumbles through it) yes... about the recent, uh, bird migration. It's a darn shame. Darn shame!

GAIL But you hate birds, Fred.

FRED Yes, well, hopefully they'll take their bird flu with them. Are the eggs ready?

GAIL Yes. They are a bit overcooked, though. But, you can use some hot sauce on them.

(Gail exits. Henry chuckles in a mocking way.)

FRED

Okay, I'll be there in a minute. Don't look at me like that. At least I have eggs. You couldn't beg your way into a plate of overcooked eggs if you wanted to.

HENRY

Oh you think so, do you? Iris? Iris, dear? Sweetheart, are you there?

(Iris steps outside.)

IRIS

What can you possibly need, Henry? I am in the middle of my show and you know I don't trust this "DRV" (we know it's actually "DVR") recording thing to work. Is it about the fact that you left your plate out on the table for me to wash or the fact that you ate both

pieces of pie and left me nothing? Because if it is, I don't forgive you.

(Iris exits. Now, it is Fred who's laughing.)

HENRY It's nothing, darling. It can wait. I'll buy you another pie later, okay? Honey?

FRED

I believe that is called "storming off", if I am correct. (He laughs again.) "Bad little Henry" left his plate out again. She's probably going to send you to your room.

(Henry is starting to lose his nerve.)

HENRY Listen, what goes on in my house is my business, okay?

FRED So, you still think she's gonna cook you some eggs? (He laughs again.)

HENRY Well, we know your wife certainly isn't able to cook some that you can eat, unless you dump a a bottle of hot sauce on them!

FrED

Well, my wife might overcook eggs but at least she is not in line to be the wicked witch for Halloween either!

HENRY You take that back, now!

FRED I certainly will not!

(Gail re-enters.)

GAIL Fred, why are you still shouting?

FRED I AM NOT SHOUTING! Now go back in the house and make me some decent eggs!

(Gail exits. Fred freezes and realizes that he has really hurt her feelings.) Gail, wait, I was just kidding. Gail?

HENRY I think you call that "storming off" if I am correct?

(Fred is fuming now.)

FRED

Henry, I have had it with your smart aleck little comments! Why don't you just go back in your house and wait for the next bird show in the backyard! That's probably the only place that you're wanted anyway!

(Henry just stands there for a minute.)

HENRY

Maybe you're right. But at least I know how to treat my wife... With decency and respect! At least I know to act like a gentlemen, not an old bitter nincompoop like you!

FrED Nincompoop? That's the best you've got? You are a small, dainty little man, aren't you?

HENRY Fred, that's enough.

FRED That's why your wife treats you like a little child. Because you aren't a man. You're a gentle little Nancy!

HENRY Fred, I am warning you, that's enough.

FRED Your wife is tougher than you every could be, NANCY!

HENRY That's it!

(Henry punches Fred as hard as can. Fred writhes in pain as Iris walks outside.)

FRED Ow! Oh!

HENRY Fred? Are you okay? Fred?!

IRIS

Henry, what on earth happened? Did Fred finally have a heart attack?

HENRY No, I think I killed him, Iris. He isn't moving at all.

IRIS

What? You killed him? Honey, I never thought you could do it! I am so proud of you!

HENRY Proud? But, he's dead!

IRIS I'll go and make some eggs... With cheese all over them!

(Iris exits.)

HENRY Wait, Iris? (He notices that Fred moves.) Fred? Fred! You're alive!

(Henry helps Fred up to his feet.)

FRED Ow... Henry you...

HENRY I thought you were dead.

FRED Dead? You couldn't kill me if you wanted to.

HENRY You're bleeding.

FRED Of course I'm bleeding. You punched me in the face, you idiot.

(Gail enters.)

GAIL Fred? Fred what happened? Why are you bleeding?

FRED Well... (he looks at Henry.) I think a bird swooped down and pecked

me in the face. I'll be fine. I think your eggs are just what I need right now. Did you throw them out?

GAIL Of course I did. You hurt my feelings.

FRED I'm sorry, Gail. I love your eggs just the way they are. Will you forgive me? Gail?

GAIL I'll start some fresh eggs. (She exits.)

FRED Look, Henry. I, uh, I owe you an apology, too. I never thought you

would actually hit me. I respect that, I do. But you could never kill me.

HENRY Kill you? (He realizes.) Oh, Henry, you have to go inside now!

FRED Why?

HENRY Iris thinks I killed you and if she sees you I may not get those eggs.

FRED She's making you eggs because she thinks you killed me?

HENRY Yes! And this offer isn't gonna hold if you're standing out here.

FRED Okay, Henry. Go enjoy your eggs, okay. Maybe I'll come back to life tomorrow and we can start over.

HENRY Yeah, That sounds good, Fred. See you tomorrow, then.

FRED Okay.

HENRY Iris? Have I ever told you about why the birds are always singing?

IRIS I know why they are singin'. We're stickin' with eggs today!

BlACKOUT.
```

---

## IC-1042: Post Inferno

- Title: Post Inferno
- Author (byline): Spill Major
- Work: Post Inferno
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2119
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
(Lights up. The stage is washed in a mix of warm reds and yellows. Virgil sits alone at a bar table in one of two chairs. Dante is at the bar, picking up two drinks he has just ordered. Both are in tall, stone goblets. He walks hurriedly back to the table and sets the drinks down too quickly, almost spilling both.) Dante: Ha ha! Sorry, my leader, my guide! I’m feeling a bit like a Venetian on dry land today. I don’t know where my feet are. Look at this, look at my hands. (His hands are shaking.) Only one cure for that. (Takes a long drink.) Won’t you drink with me?

(Virgil makes no move, but only stares at Dante.) Then, to the Lord! (He toasts the air and drinks again.) Vengeance is his. (There is a long silence, as Dante sits fidgeting. Virgil still stares.) Virgil? (No response.) On what does your mind dwell, my liege? Virgil: Fools need no guide, for they are all heading to the same place. Dante: In other words, if the cow is falling of a cliff, don’t give him a map on the way down. (drinks) You’re a real wit, my friend. Virgil: Cows. (He drinks.) Wine is never as heartening as when it’s served in the bag… but the beggar at the befouled puddle should not cry out for a cool spring. Dante: (His head falls on the table and stays there. Virgil stares off into space. Eventually Dante speaks.) Aren’t you even going to ask what’s wrong? Virgil: Even the most blundering ignoramus need not ask what he already knows, for by stooping to give the question voice, he wastes both time and thought. Let reason speak to you instead of me, and tell you that I am not one for idle chatter. Dante: Poetry. Virgil: I despise it. Dante: We were just in Hell! Master, may I not have the benefit of your patience? Virgil: If your heart’s sky held its stars properly aligned, you would have no need to fear what you have seen. It would be water sliding off a heron’s back. Dante: Herons’ have no pity. None for the fish, for their brethren, for the world. Virgil: Curse not that you are asked to be steady, for your clockwork was set in motion by a higher power.

Dante: Look at these steady folk here. (indicating audience) These filthy, ugly, greedy, scheming sinners. They’re in the gullet of the bird. All that remains for them is to be digested. Virgil: (He looks at the audience, says nothing) Dante: (finding a different audience member for each damnation) This one, to the boiling pitch! He’s sure to feel the blood of Phlegethon in between his digits. She’s to be whipped by the lover’s winds, and she will be stuffed into a boiling hot kettle, there to roast like a turnip, a screaming, scorched turnip. But at least you’re part of his plan, turnip. Aren’t you happy about that? Aren’t you thankful? That one’s probably already in hell. Demon, do you hear me? Don’t you have enough? Virgil: We were not given this time to tarry and banter. The gulf of souls calls to us, and we must not miss this opportunity to cross. Dante: Why. Virgil: This path was shown to us by the only one who could make it. He has cut the brambles, now we must trace his mighty steps. Dante: Why. Virgil: What would you do with your constant questions? We have been commanded and have no choice but to follow. Dante: Why. Virgil: Because that is how things work, dung-puddle! God is our master and we obey. We are his creations, his toys. We serve in and for his purpose. Dante: (long silence) Why. Virgil: Go flagellate yourself. Dante: It seems God’s wisdom in you has run out. We don’t have to do anything. (he pounds the table.) God Dammit. (He drinks, and immediately spews sand all over the table.) Owwww… oh that stings. Owww. Virgil: (Drawing his finger in a line through the sand) Your wine turned to burning sand. For your blasphemy. Dante: Forgive me, Lord. (he kneels.) I wonder… (he touches the bottom of his foot) I thought it would be burning hot. Virgil: This is not hell, Dante.

Dante: We have been stuck in hundreds of years of political strife, my family cut down
for blood oaths sworn over false pretenses and worthless omens, and you say this is better
than hell? Men still hate each other on assumption. The place where every man thinks
his friends are sinners, that is Hell.
Virgil: With one important exception. Each man believes himself a saint.
Dante: So mankind is saved by his own arrogance.
Virgil: (rising) Those who still walk in the grace of God deserve to be arrogant.
Dante: Those who are burning alive deserve to be pitied.
Virgil: That is where you know you were wrong.
Dante: (sighing) Hell was too much… what I was expecting, that’s all.
Virgil: What else did you expect to see besides an exact and perfect order, working to
distribute God’s will and justice with a perpetual balanced momentum?
Dante: When we go to the bottom.
Virgil: Where the morning star fell.
Dante: I hoped it would be empty.
Virgil: You hoped?
Dante: I had hoped.
Virgil: You hoped. How pathetic.
Dante: No, it’s not.
Virgil: It is! You are supposed to be a man of faith, and yet this shows you to deny God’s
spoken will even as it is laid out before you.
Dante: That is not what hope is. When God speaks I listen and take note. Now I know
the true nature of Hell. But when God is silent, and his mind works in quiet symphony, I
may pray, and I may hope with all the love and faith I can conjure that he shall show the
infinite bounds of his mercy and grace. Otherwise, there is nothing to have faith in.
Virgil: The tricks of a mad magician are what you described to me. You are a blind fool
dreaming that everything beyond your sight is gold. I’m through with you. (He takes a
long drink. Then he stops and lowers the cup slowly. He chews and swallows the sand
which it contained.)
Dante: What?
Virgil: I have blasphemed the Lord’s name.
Dante: I missed it.
Virgil: No, you didn’t. When I mocked the hope of the faithful. There is no greater
affront.
Dante: Oh. So I’m right?
Virgil: How embarrassing.
Dante: Your reason fell short. It happens.
Virgil: (says nothing, draws away from Dante)
Dante: Virgil?
Virgil: Meh.
Dante: Can we go now?
Virgil: Let’s stay here.
Dante: What?
Virgil: There’s no reason to go back. Come, let us sit and be merry. Let us live here, for
a while.
Dante: Virgil, no. I have to finish. I see where my faculties are lacking. You have to
help me understand.
Virgil: You have a profound grasp on the Lord already, more than I could ever hope…
ever want for. You’re done.
Dante: Who are you?
Virgil: Like you, just a poet.
Dante: Just the embodiment of human reason! Although you’re giving me zilch of that
right now. Why are we even here? We have to get through two whole eternal realms
before the end of Easter. It’s already Saturday and you have me drinking French wine in
a bar in wherever this is.
Virgil: Five minutes ago you were not as willing. A mind that wanders in whatever
direction it fancies cannot easily find its way back home. You need to consider your
destination before hitching the horses.
Dante: …Virgil?
Virgil: Yes?
Dante: Are you saying that we should forget God and just get wasted?
Virgil: Yes.
Dante: Whoa.
Virgil: I’m sick of it being smeared in my face, that because I was born before His Son,
I’m somehow lesser.
Dante: Virgil, my liege, my teacher, my companion, you are so much more than me.
You are the master of reason, the weaver of verse, on the level of the spinning muses and
their magic words.
Virgil: The muses burn in hell with the rest of the Olympic swine.
Dante: When you put it that way…
Virgil: Go, and make a milk maid of that sweat-stained minotaur who guards the horde of
men’s courage and vice.
Dante: Are you saying you want another drink?
Virgil: Questions which are rightfully posed are not answered; rather, they are turned into
a concordant silence, which, when wrong, is never known to be right.
Dante: I’m just going to get you a drink anyway.
Virgil: (staring at a chip in his glass) It’s easy to find what’s wrong with a world in
disorder. Cracks leak and grow. Those who find the flaws in an ordered, working
society are those who have the true ability to change the world. Theirs is not just a work
of passion, but a pursuit of intellect.
Dante: (returning) I cannot believe that this foul grape-smelling sludge is what passes for
whine in Gaul. I feel as though I’m drinking from the feet of the mill-turners.

Virgil: So tell me, is this quest of yours really about your love of God, or are you just looking for Beatrice, your dear departed love. Dante: Don't bring her into this. Virgil: You already did! You talked about her the entire time we were in hell. Oh, Beatrice died before we could be together. Oh, Beatrice and I will be reunited again in the holy kingdom. Oh, Beatrice's hair smells like unicorns and cinnamon.. Dante: Meeting her might help you. She is God’s model of Love. She will bring you forth from your funk. Virgil: She's not turning water into wine. Dante: Better than this French swill we're drinking. Virgil: Tell me one reason she deserves such attention. Dante: I hold her and I feel useless, alive with one last breath in me, this is my chance: to peel everything away, thick strands of skin which have died with my lies and my hatred, my unutterably unlovable sin, to let that heavy sick flesh grow light and ephemeral to flake away in the wind. To float away by and through that hair – it floats in the air like God’s one hundred arms. With her wrapped around me I feel all the possibilities of hope in the single moment; not fulfillment, but together we balance on the joyous, feverish point of all faith. Wrapped around me I feel not forgiveness – but better, the chance of forgiveness. I know: she cannot show me there is a God. She simply gives God a chance in my dark and pathetic soul. Virgil: She’s still a wench. Dante: Question. Why didn't we meet any women in hell? Virgil: That’s unfair. We have to relate to our audience. Dante: Men? Virgil: Men. The educated. Same thing. Dante: There are few women in hell, for most are victimized far more by the idiocy of men than they are dragged down by their own feminine infidelities. Virgil: You are a fool. I am tired of leading a fool on a fool’s errand. Dante: Master, I have treated you with respect… how can you be so unreasonable?

Virgil: It is not unreasonable to refuse a foolish request; far more ignorant are those who
burden themselves with the work of dunces and dolts.
Dante: That’s the way it’ll be.
Virgil: Yes.
Dante: So, I didn’t see Aeneis while we were down there.
Virgil: Don’t you dare drag him into this.
Dante: He’s already conspicuous by his absence
Virgil: Not all of us have the liberty of composing epic elocutions about our own
adventures.
Dante: My blatant self-aggrandizement is not the issue here. Let us find your spirit first.
Was he buried too far beneath the coffins of flames? Perhaps your champion was
creeping slowly under his coat of steel for his betrayal of the Carthaginian Queen!
Virgil: Aeneis would be in neither place.
Dante: Maybe we passed him. Maybe you just didn’t draw my attention to him, or
pointed out some fat Florentine who could tickle my pride while the Trojan hero slouched
away.
Virgil: No. I did nothing of the sort.
Dante: Where is he? What circle?
Virgil: I don’t know.
Dante: You don’t?
Virgil: I’ve never looked.
Dante: (leaning back, as though he has heard what he wanted) Because you hope he
isn’t there.
Virgil: I hope he isn’t.
Dante: He probably is.
Virgil: There’s a chance.
Dante: A slim one.

Virgil: It’s a chance. It’s slim as a vestal virgin but it’s there.
Dante: I hope he isn’t there, either.
Virgil: I’ll never know.
Dante: Let’s look for him on the mountain.
Virgil: Well…
Dante: Perhaps I’ll spot him in the fringes of heaven, and shout it down to you.
Virgil: I suppose it’s worth looking.
Dante: In a minute. I feel the urge of the lord in my less than holy places.
Virgil: What does that mean?
Dante: I need to tinkle. I’ve been holding it since Malebolgia.
Virgil: (shouting after him) But thou has had but two drinks! Can you be so weak and
weary after denying yourself for the nine circles of hell?
Dante: You know what they say. The Lord giveth and the Lord pisseth away.

(He leaves. Virgil is left to look out into the audience, and he recalls lines of the Aeneid.) Virgil:

I will sing of battles, and blood, and rage,

Which princes and their people uncovered;

These haughty souls, struck with mutual hate,

In fighting fields they fought and found their fortunes

That echoed across the Tyrrhene realm,

And peaceful Italy was brought to arms.

A great number of things are born by me,

For I set in motion a greater work.

(Virgil smiles.) Dante: (Entering again.) Ahhhhhhh…. I feel like a newly baptized schoolboy. Virgil: Shall we be off? Let's go meet your Beatrice. Dante: Yes, by God’s Grace, I am like newly crushed olives in the till. I see your mind has moved to view my lady more fortuitously.

Virgil: Spirits move in mysterious ways. Dante: Indeed.
```

---

## IC-1043: S H R I NKAGE Text copyright 2008 Andrew Messer.

- Title: S H R I NKAGE Text copyright 2008 Andrew Messer.
- Author (byline): Not specified
- Work: S H R I NKAGE Text copyright 2008 Andrew Messer.
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1367
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
Boss: (smoking, reviewing resume) John, I’m gonna be honest… your resume looks great. You’ve got the job. John: Really? Wow. I heard quite a few people applied for this position. I thought I might… Boss: Shut up, you’re perfect. (picks up phone) Sheila, will you please give the rest of the applicants a call and tell them we’ll be in touch. Then go ahead and throw out their files. Thanks. (hangs up) Anyway, John, before we can officially put you on the payroll, there is one small formality. We need you to take a short psychiatric assessment. John: Oh, you mean like a written questionaire or something? Boss: No, it’s only a quick evaluation with the company psychiatrist. Sheila will give you all the information. Oh, and ah, good luck. Shrink: Oh, hello, John. Come on in. I’m Doctor - John: Nice to meet you, Doctor. Shrink: Likewise, let’s get started. Tell me about yourself, John. John: Well, since you already have my resume, what else would you like to know? Shrink: John, are you hesitant to tell me about yourself? John: Oh, no, not at all…I didn’t want to bore you with repetition. Shrink: John, I don’t find the details of your life boring… quite the contrary, in fact. Even if I did find them boring, I am paid to listen. John: You probably get paid pretty handsomely just to hear me talk, don’t you? Shrink: Well, now, John. Are you suggesting that people only work for the money? Do you not like working, John? Are you only driven by money? John: Of course not, I was just trying to make a little joke. Shrink: Well, John, it wasn’t a very funny witticism. If I were only concerned about money, I would have stayed with Chippendales. John: You were a Chippendale dancer? Shrink: No, John, that was a joke. But it seemed to have piqued your curiosity a bit… John: Well, I was just wondering what…

Shrink: Let’s start with a few hypothetical questions, shall we? Alright, first…you find a
wallet on the ground with one hundred dollars in it. What would you do with it?
John: Ah, well…um…I would try and return the money to its owner.
Shrink: Say the owner was deceased.
John: In that case, I would return it to a relative of the owner.
Shrink: (quickly) Say you had just killed the owner in a botched mugging and picked the
wallet up out of a pool of blood.
John: (shocked) I’m sorry, what?! I would never kill someone over their wallet!
Shrink: Oh? So what would you kill someone over?
John: Nothing!
Shrink: You would kill someone over nothing?
John: No, that’s not what I…
Shrink: Next question. You and an elderly lady are standing on the deck on a sinking
ship, and there is only room for one more person on the lifeboat. Do you allow her to take
the last remaining space on the boat, or do you take it by force?
John: Take it by force?
Shrink: Yes. For example, would you bludgeon the lady with an oar to procure safe
passage?
John: No! I would give the seat to her. I mean, I’m in pretty good shape, I could swim.
Shrink: The waters are shark-infested, John. There will be no swimming.
John: Alright, then I’ll hang onto the side of the lifeboat and take my chances.
Shrink: John, she’s quite old.
John: I’m not going to leave an elderly woman on a sinking ship to die!
Shrink: She’s going to die soon, anyway, John.
John: Just because she’s old? She could live several more years!
Shrink: Not with the ebola virus.

John: She has the ebola virus?! Does she know this?
Shrink: Does it matter? What would you do, John?
John: Okay, fine, I’d take the spot on the lifeboat!
Shrink: Well, John. You are ruthless, aren’t you?
John: You forced me…
Shrink: John, one last hypothetical. A friend has two tickets to see Cher live in concert.
They offer them to you. Do you take them as a gift, or do you insist on giving them
something in return?
John: Um, well…I’m not a big Cher fan, so could I just skip the concert?
Shrink: Correct answer, John! Alright, moving on. This next set of questions is a series
of either/or propositions designed to gauge how confident you are in your decisions.
Are you ready to begin?
John: Sure. Why not?
Shrink: Question one…milk or cookies?
John: You mean milk and cookies?
Shrink: No, John. This is not a perfect world. You cannot have both.
John: Oh. Well then in that case, um…milk. Yeah, milk.
Shrink: Alright…question two. Romance or fantasy novels?
John: Of just those two? Well…I find romance novels very hard to swallow, so I’d have
to say fantasy.
Shrink: Fantasy. Interesting… so you believe in unicorns, centaurs, and the like.
John: No, I…
Shrink: Why don’t we try something a little different, eh? I’m going to say a series of
words and phrases. As soon as the words have evoked some clear mental image, I’d like
you to tell me what that is. Understand?
John: (slightly annoyed) Yes, fine.
Shrink: Alright. Ice skates, toboggan, fireplace, hot cocoa…

John: A winter day? Shrink: Good, John! Next… Ashlee Simpson, Keanu Reeves, Kevin Federline… John: No talent? Shrink: Well, I was expecting ‘pop culture icons’, but your answer is…quite appropriate, actually... Alright, ah...bikini, thong, g-string, French maid outfit your mother… John: My mother?! Shrink: Your mother?! John: You just said my mother. Shrink: No, you said your mother during the list of sexually appealing outfits. It was merely a series of words, John, there was no insinuation at all. John: No, but you… Shrink: John, you’re getting rather worked up about this! Let’s do some relaxation exercises, shall we? Just close your eyes. John: (peeved) Ugh, fine. Shrink: Good, John. Now, just try to calm down. Take a few deep breaths. John: (sighs) Okay. Shrink: Good. Now, I want you to try and create a mental environment, if you will. Your feet are beginning to feel quite heavy. This is because they are slowly settling into the warm sand of a tropical beach. You are surrounded by palm trees. You can hear the waves gently rolling, and the sea birds flying around you. Are you feeling it, John? John: (calmer, into the vision) Yes, yes I see it. Shrink: Alright. You on holiday on this tropical isle with your family. Your father is busily snapping away photos with which to remember this warm, pleasant occasion, and your mother and you while away the time throwing a frisbee disc to one another. As your mother throws the disc to you, you feel the wind gently flow past you and rustle in the palms, and the waves quietly nudge against the shoreline. Just before you are poised to throw the frisbee back, you realize that you are having the most wonderful time of your life on this nude beach…

John: (startled) What?! (ranting) Look, this is ridiculous! I don’t hang out on nude beaches with my parents! I’m not attracted to my mother, I don’t read fantasy novels, and I wouldn’t EVER kill anyone! And “milk or cookies?” It’s MILK AND COOKIES! I want BOTH! I’m done with this! Boss: (enters clapping, still smoking) Excellent, John! John: Excuse me? What are you talking about? Where did you come from? Boss: I was watching behind the two-way mirror. It comes standard in every shrink’s office. You passed with flying colors, though! Most new hires quit after clobbering the old lady! Very few make it all the way to the…motherly love! John: You mean this was all a test? Boss: Yep! We needed to see how you held up, this is a high-pressure job! John: Well, I don’t want it. I don’t want a job where one of the prerequisites is this kind of tormented evaluation! I quit! Boss: You can’t quit, you haven’t even started yet! John: Fine! Then tell Sheila to throw away my file, too! Goodbye! Boss: Well…that was a bit harsh. Hmm…hey, Sheila! You want a promotion? I just need you to come in here for a minute and take a short evaluation!
```

---

## IC-1044: The Altos Copyright 2003 by Clyde Hendrickson.

- Title: The Altos Copyright 2003 by Clyde Hendrickson.
- Author (byline): Not specified
- Work: The Altos Copyright 2003 by Clyde Hendrickson.
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 3053
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
The Time: Present The Place: Nutley, NJ

Characters:
TONY ALTO. A 5’2” Mafia boss with a very suburban family. Talks like he’s on helium.
CHOCOLETTA. Tony’s wife. Has a New Jersey accent.
TA. Tony’s 15 year old son. Very aristocratic and british.
VALLEY. Tony’s 18 year old daughter.
MAMA. Tony’s self-depriciating, hatred-filled mother.
JIMMY-CHRISTOPHER-JOHN. A mob crony that works for Tony. Hey, that rhymed.
UNCLE SENIOR. Tony’s elderly uncle, who is a bit batty.
BIG BONE. A rival mob boss. Smart but slow.
BOY SCOUT. Hit by Tony’s car.
THE KITTY. A persecuted family cat.
HORSE’S HEAD. The disembodied head of Mr. Ed.
JEFF PROBST, HOST OF TV’S SURVIVOR. Jeff Probst, host of TV’s Survivor.
AL CAPONE. The somewhat strange ghost of Al Capone.
FBI GUY. Agent Gaygent, the long arm of the law.
LAWYER. Works for CBS, very blunt and buff. More like a thug.
PIZZA GUY. Young and nerdy.
BIRD. Loud and screechy.
AMERICAN PUBLIC. Guy or girl dressed very generically. Speaks like a TV announcer.
Set:
The play is designed to be carried out on a relatively empty stage. Different parts of the stage should
represent different places. Anything which adds to the correlation between the play and a certain HBO
mob drama is encouraged. A simple set of chairs, a kitchen area with a fridge, and a table are all that’s
necessary. Guns and knives can be mimed or real, although the gattling gun is probably more effective if
real.

Note: This play is conceived as a sequel to Clyde Hendrickson’s The Merchandise King. Back-to-back performance is encouraged.

THE ALTOS

(Tony is standing in front of a mirror. JCJ enters, frantic) JCJ. Tony! Tony! Big Bone killed Little Rod and he says you’re next!

(Tony stares)
JCJ. What should we do? Tony?
TONY. (Looking into mirror) Does this suit make me look short?
JCJ. Yeah… but youz is Five foot two.
TONY. Don’t hate the playa, Jimmy-Christopher-John. Hate the game.
JCJ. Tony! I have some bad news.
TONY. Well make it quick, I have a stripper waiting in the back room.
JCJ. Ohhh.... She gonna, y’know, polish the cannoli?
TONY. No. She’s a very talented seamstress and she’s gonna teach me how to sew buttons. It’s an
important skill to have, Jimmy-Christopher-John. Now what’s your bad news.
JCJ. Big Bone wants to kill you. He says he wants your territory.
TONY. Well ring up the Lord tell him the Virgin Mother Mary’s pregnant, cause that is news. (quietly)
But - did he say anything about my nuts?
JCJ. What?
TONY. My nuts are very precious to me.
JCJ. It’s good to know that.
TONY. Yeah, you know, I had my whole swimming pool filled full of brazil nuts. I did it to give back to
nature, you know, sort of a giant bird feeder, but I think it might have made Big B. jealous.
JCJ. He didn’t mention it. Anyway, we need to be prepared for war.
TONY. Oh, we will be.

JCJ. I know, when it comes to preparedness, you’re a foot below the rest, Tony. (there is a very
uncomfortable silence, then JCJ realizes his mistake) Above! I mean, uh, above the rest. (another silence)
Crap.
TONY. So, Jimmy-Christopher-John, how’d you get such a long name?
JCJ. Well, Ma didn’t know who the father was, but she wanted me to be named after him, so she just
covered all the possibilities. Hey, now that we’re bein’ all philosophical and such, can I ask you...
TONY. Yeah?
JCJ. How’d you get... y’know, like you are?
Tony Alto: Ah, on the way here, a lawnmower chopped up my nuts.
JCJ. What!!?
TONY. Yeah I had this nice bag of peanuts and they just went... (he acts out nuts getting sucked up by
lawnmower) Vuh-boom, y’know. That’s why I’m so angry.
JCJ. Oh. Yeah.
TONY. Then it went straight up and got my balls.
JCJ. (Even bigger reaction) Whattt???!!!
TONY. Yeah I had this sack of baseballs for TA’s little league game, and they got chewed the fudge up.
JCJ. Oh. So... that’s why you’re so tense.
TONY. No, I’m tense because I’m short and talk like a pygmy midget dwarf’s newborn daughter. But I
would’ve liked to have some nuts, as well.
JCJ. We all need our nuts.
TONY. Indeed we do, Jimmy-Christopher-John. Indeed we do.

(They leave. Uncle Senior enters, as we are now in his house.)
UNCLE SENIOR. I’m singing in the rain, just singing in the rain, what a glorious feeling, I’m happy again.
Wow, who could have thought that an old man could be made so happy just by one of the simple pleasures
in life.
TONY. (entering) And what might that be, Uncle Senior?
UNCLE SENIOR. Why, prostitutes, of course. Prostitutes and Raisin Bran.
TONY. Uh...
UNCLE SENIOR. There is nothing more wonderful than sharing a bowl of nutritious breakfast cereal with
a fine young woman of the night. Now, what can I do for you, my daughter?
TONY. Nephew.
UNCLE SENIOR. Same thing. You both get screwed in the will.

TONY. Uncle Senior, I need some advice. As you know, I’m kind of uh, a small man.
UNCLE SENIOR. That’s not what your wife tells me!
TONY. Nah, nah, I don’t mean the cannoli. My cannoli is delicious, creamy and huge. I’m saying I have
uh, a small stature.
UNCLE SENIOR. A small statue? Oh that’s practically useless. You need a big, marble statue. I always
wanted a big statue for the lawn, maybe uh, a horse, or uh, uh, a whaddayacallit?
TONY. I have no idea what you’re talking about.
UNCLE SENIOR. Uh... a prostitute! Yeah. A big horse, or a big prostitute. Those are the only statues
worth having.
TONY. Yeah... look, Senior, Big Bone is movin’ in, and I ain’t got the image to stand up to him.
UNCLE SENIOR. You can’t stand up? Back problems. Probably from all the prostitutes!
TONY. Teach me how to be tough, uncle. I can talk it, but I gotta walk it, y’know? Can you do that?
UNCLE SENIOR. My Son. Nephew. Whatever. I will make you the next Marcus Digrullio.
TONY. Who’s Marcus Digrullio?
UNCLE SENIOR. See, you’re tougher already! (Doorbell rings) Sweet Mary and Joseph. Are you
expecting someone?
TONY. No. I don’t live here.
UNCLE SENIOR. Who could that be? (Doorbell rings again)
PIZZA GUY. (offstage) Pizza Delivery!
UNCLE SENIOR. (pauses for a moment) Oh, it’s just the pizza.

(He walks to the door, opens it) PIZZA GUY. Hey, special delivery for Mr. Alto? UNCLE SENIOR. Wha? A trap! I got your special delivery right here.

(Uncle Senior pulls gun, unloads 3 rounds straight at Pizza guy) PIZZA GUY. (high, screeching) Ahhh.!!! Ahhh!!! UNCLE SENIOR. He brought birds! I hear their vicious calls! (Shoots wildly at the air. Chandelier falls, he catches it.) Tony! I got a big turkey! Look at this! TONY. Great, Senior. You plugged the chandelier. Now we gotta bury it in the back, so it’s relatives the lamp and the nightlight don’t get suspicious. Why don’t we go see if you killed the pizza schmuck as well?

(They look to Pizza Guy. He staggers to his feet.)

PIZZA GUY. They always made fun of me for wearing kevlar on the job. But I showed them. I showed them. TONY. I’ll leave you two to finish this battle of the minds. I’m going home.

(Tony gets in his car, and mimes moving the seat all the way up and forward so that his head is over the steering wheel and he’s practically coming out the windshield. At the same time, he’s humming “Macho Man” by the Village People. As this takes place, the house is set up, Mama and Chocoletta enter. Tony gets out of the car and steps into the house.) TONY. Hello? I’m home! MAMA. Just a little closer... (She stands with butcher knife above her head) TONY. Ma? You tryin’ to kill me again? MAMA. No... no... I was just.... stabbing ants with this butcher knife. Don’t accuse me all the time. You’re such a terrible son. TONY. Super, ma, super. (He turns. She raises knife again and slowly walks after him). What’s for dinner, sweet cheeks? CHOCOLETTA. Tony, do you know how many times people tried to kill your mobster son at school today? TONY. Ah geez. CHOCOLETTA. 47! And he did not even shoot one of them. There is something wrong with that child. TONY. My little ricotta rabbit... CHOCOLETTA. Don’t pastacize me, buster. You need to fix your son. Or give me money, that works too. TONY. Sometimes I feel like he’s not related to me at all.

(TA enters, dressed in all white. He speaks with an aristocratic british accent.)
TA. Oh hello daddy! Dropped in for a spot of tea before the afternoon riff-raff arrives?
TONY. Yeah, something like that.
TA. Daddy, will you come to my polo match this afternoon? It will be ever so fun!
TONY. Hey, TA, look, I’m sorry, but I have business to tend to.
TA. Awww...
CHOCOLETTA. Tony! You need to do some nice things for your son.
TONY. Yeah, alright. Hey, TA, to make up for it... take this .44 magnum. (he produces a gun)
TA. Oh, sweet! Thanks, daddy!(he takes the gun, removes safety and cocks it) Here, kitty kitty kitty....
CHOCOLETTA. That was adorable. You can be such an angel sometimes, Tony.

(Tony smiles. Mama approaches him with a bowl of soup.) MAMA. Here, eat this, I made it myself. TONY. Ma, this soup is black, and it has a dead rat floating in it.

(pause) MAMA. Your father was never a good husband to me. No one cares if I’m alive or dead. CHOCOLETTA. (changing the subject) Sounds like your granddaughter’s home, Ma! Hi, Valley. TONY. How are you, Valley. How was your day at school and/or college and/or work? VALLEY. Yeah, Dad, I’m pretty inconsistent as a character, so I’m gonna go get beaten and mugged while dating a bisexual african-american, than come home to start selling drugs to neighborhood kids from your own garage while I sleep with every old guy that you hang out with. Then I’m going to start a career as a teen pop star, watch it fail horribly, and come back to you, begging to be “written in” to more of your life.

(Tony thinks for a moment, then kills her)
CHOCOLETTA. Tony!
TONY. (whipping out diamonds just in time) Here, I got you a diamond necklace, baby.
CHOCOLETTA. You… are such a good father.
TONY. Phew, parenting is hard work... let’s see if there’s any ice cream. (he opens the freezer) Ahhh!
There’s a horse’s head in the freezer!
CHOCOLETTA. Oh my god!
HORSE’S HEAD. Hello, I’m Mr. Ed!
TONY. That is not funny.
HORSE’S HEAD. I’m sorry, would you like me to go back to scaring the living crap out of you?
TONY. Chocoletta, I’m getting out of here. This means that Big Bone is ready to strike.
CHOCOLETTA. I had no idea! I thought a mob boss like you was totally safe from death threats and
hitmen. What’s gonna happen?
TONY. He could hit anywhere... our house, my office, my mistress’s house if I had a mistress which of
course I do not... he could even hit my nuts.
CHOCOLETTA. Oh Tony, no one’s going after your precious swimming pool filled with brazil nuts.
Honestly, I don’t even know why you keep them there.
TONY. It’s a hobby, alright? I’m giving back to nature. Anyway, I’m gonna figure this out. If you need
me, give my mistress’s cellphone a call.
CHOCOLETTA. Ok, I will, but you better not be with her.
TONY. Right, of course not, I love you honey and I only ever even look at you. See ya later.

(he exits, stuffing the horse’s head into an icebox. TA enters, and Mama is again in the conversation) MAMA. That son of mine. If he loved me, he would do more nice things for me. Like die a horrible, painful death. CHOCOLETTA. Ma! That’s a terrible thing to say in front of your grandson. MAMA. Why do you have to be so mean about every little thing I do? “Mama, why do you have so many guns?” “Grandma, don’t throw the blender at people while it’s on.” “Grandma, you shouldn’t have covered the front lawn in Napalm.” Well, I had had enough with those squirrels, god rest their souls, and I like the lawn all black and charred, for your information. Just like my son’s mother’s heart, he’s so cruel to me.

(TA looks in the freezer)
TA. Mother, did you take my horse’s head out of the freezer?
CHOCOLETTA. What?
TA. It was for my biology project.
CHOCOLETTA. Oh honey, dearest, sweetie... I’m sorry, your Dad thought it was put there as a threat on
his life from a rival mob boss. Not that we’re in the mob.
TA. What? Now I shall surely fail! How I do detest being in a mafia family.
CHOCOLETTA. Can I do anything to make it up to you? Not that there’s anything to make up for
because we’re not in the mob.
TA. Well... you could help me find a new head for my project.
CHOCOLETTA. Of course! You know, the kitty is getting pretty old.
THE KITTY. Meow?

(Tony is driving again. He’s clearly panicked.)
TONY. My family is falling apart... Big Bone is coming after me... My nuts are in constant danger...
BIRD. Sqwauk!
TONY. That bird on my hood... it’s like he’s trying to say something to me.
BIRD. Sqwauk! Your doom is near! Sqwauk!
TONY. Probably just my imagination...
BIRD. Sqwauk! I’m going to eat your nuts and sully your daughter! Sqwauk!
TONY. My nuts! No... no....

(He passes out. Dream sequence begins. Al Capone enters, carrying a limp figure.) TONY. Who are you?

AL CAPONE. Al Capone.
TONY. Whatcha doing?
AL CAPONE. Brushin’ my teeth. What does it look like I’m doin?
TONY. It looks like you’re making out with Daffy Duck.
AL CAPONE. Yeah, well, you say potato, I say... there can be true love between man and duck. (To
Daffy) Isn’t that right, sweetcakes?

(Daffy does not respond) TONY. Your duck looks dead. AL CAPONE. Look, I don’t talk about your ducks, you don’t talk about mine, capiche? (Throws duck away) Anyway, you need help. I brought someone along to, y’know, teach ya a thing or two. JEFF PROBST, HOST OF TV’S SURVIVOR. Hi, I’m Jeff Probst, Host of TV’s Survivor. TONY. Ok... JEFF PROBST, HOST OF TV’S SURVIVOR. Now, with just three weeks left, things are tense on the island. Who will win? Is it the dead gangster come back to life, the pygmy midget dwarf in a poorly-tailored suit, or the disembodied horse head of Mr. Ed? Only time will tell. Time... and the strength of these three competitors to survive. AL CAPONE. Now, whaddaya want do to him? TONY. Bite him in his freakin nuts. AL CAPONE. Try it out, shortie.

(Tony bites Jeff Probst in the nuts.)
JEFF PROBST, HOST OF TV’S SURVIVOR. That’s two more voted off the island!
AL CAPONE. My friend, now you know the key to success.
TONY. That’s it?
AL CAPONE. That and the ducks.
TONY. Why is it always the ducks and the nuts?
AL CAPONE. Life is strange. Now wake up, you just ran over a boy scout.

(Dream ends. Boy Scout runs out and flings himself on the floor)
BOY SCOUT. My spleen hurts.
TONY. Hey, that’s great kid. Do you know where Big Bone’s hideout is.
BOY SCOUT. Yeah, it’s in the back of that erotic cake store over there. Can you call me an ambulance?

TONY. Sorry, I’m, uh.. don’t speak english. Good luck!

(Boy Scout crawls off. Big Bone enters, sits, waits for Tony)
TONY. Big Bone.
BIG BONE. Geraldo.
TONY. No, I’m Tony Alto.
BIG BONE. Yes?
TONY. You want to kill me.
BIG BONE. Right, right. Would you like a peanut?
TONY. No... I only eat... brazil nuts.
BIG BONE. ... Oh.
TONY. I have in this icebox something which I hope will solve our little disagreement.
BIG BONE. Brazil nuts?
TONY. No! You’ll never see my nuts.
BIG BONE. Disappointing.
TONY. (takes out can from icebox) See, we’re a lot like this beer can here. It’s a very dangerous
situation. If you don’t relieve the pressure... (Tony grabs can) you’re lookin’ to get crushed (can, full and
unopened, does not crush).... You’re looking to get crushed (can is not crushed again. He pauses, then
quickly opens it and empties it to the side. Big Bone smiles understandingly, than realizes how strange the
situation is) ... Yeah, you’re looking to get crushed, y’ hear? (can crushes)
BIG BONE. Did Al Capone come to you in a dream and tell you how to do that?
TONY. No... he taught me to do this! (he leaps forward and bites Big Bone in the groin)
BIG BONE. Arrrggg.... get off! (he shakes him off) Now you’ll see why they call me Big Bone (reaches
into his pants)... Well, actually, no you won’t. It has to do with a trombone and a girl and a fire truck... it’s
really quite a long story. Hey, is that a horse’s head in your icebox?
HORSE’S HEAD. Hello, I’m Mr. Ed!
BIG BONE. Yeah?
HORSE’S HEAD. Don’t you want to sing with me? (The Head proceeds to sing the theme song to his
television show, the lyrics to which are not reprinted here due to possible copyright violations. But, in the
middle of the song, the horse yells...) Now, Tony!
TONY. Eat lead, Big Bone! (he shoots him) Wow, that was really cool. Thanks, Ed. Anything I can do
for you?
HORSE’S HEAD. Yeah, think you could maybe reattach me to my body?

TONY. No, but I do know a Boy Scout who could use a new spleen. Maybe you two will hit it off. Anyway, I’m gonna make like a banana and split.

(FBI Guy enters and cuts him off)
FBI GUY. Tony Soprano, I’m Agent Gaygent from the FBI, you’re under arrest for violation of FDA rules
and regulations regarding the collection and storage of nuts.
TONY. What?
FBI GUY. Your pool full of brazil nuts, under federal law, is considered to be a house of ill-repute, as well
as a disruption of the natural order.
TONY. That’s ridiculous.
FBI GUY. The law is the law.
TONY. No, I mean, your name... it’s Agent Gaygent.
FBI GUY. Hah! This isn’t about me, it’s about you.
TONY. My acorns are my business.
FBI GUY. You should have thought about that more carefully before your nuts got so big. I saw the pool
with my own eyes... frankly, you disgust me sir. Who needs so many brazil nuts?
TONY. The ducks! I was giving back to nature!
FBI GUY. Well now you can give back to it from the electric chair!
TONY. What? The FDA can give people the chair?
FBI GUY. Did I say electric chair? I always do that. I meant probation.
LAWYER. Hold up there. I represent CBS, leader of the free world, champion of the press.
FBI GUY. (snickering) Do you really think that CBS is the leader of the free world?
LAWYER. That’s libel. Your behind now belongs to CBS.
FBI GUY. Uh, I work for the federal government.
LAWYER. Shut up! (shoots FBI Guy)
TONY. Oh! You can do that? Maybe I’m in the wrong profession.
LAWYER. Tony Soprano, CBS hearby charges you with a debilitating assault on Jeff Probst, host of TV’s
survivor and champion of the world. You’re coming with me.
TONY. Wait... what are you saying?
LAWYER. No more of this HBO, commercial free, “I can swear whenever I want to” B.S. From now on,
you’re going to be wearing Nike products, with clips of you shooting a machine gun sandwiched between
ads for Starbucks and The Gap for Kids.
TONY. (determined, steeled) I’d rather be dead.

LAWYER. (cocking gun) That can be arranged...

(Mama enters with gattling cannon) MAMA. Take this you son of a...

(Gunshots miss Tony, hit lawyer)
TONY. Good shot Ma!
MAMA. Ah I missed... I mean, uh, I got him!
TONY. See, Ma, everything turned out OK with me in the end.
TA. Daddy, I am so proud of you!
THE KITTY. (holding gun) Meow! (kills TA)
TONY. Oh no, TA! The kitty has taken vengeance upon you! What have my reckless gun safety
standards done? Ma, help me! (he puts his hand on her shoulder,she loses her balance, falls over, and
dies.)
MAMA. Maybe you should try not killing someone for a change? (dies again)
TONY. I killed everyone I love. Surely I must need some come-up-ins.
AMERICAN PUBLIC. Hi, we’re the American Public.
TONY. Yeah, and don’t you think I should get what I deserve?
AMERICAN PUBLIC. No, we love you! You’re our secret role model, because we need validation for
screwing over the rest of the world.
TONY. Yes sir, I believe in America.

(Lights out)
```

---

## IC-1045: The Bright Side of Death

- Title: The Bright Side of Death
- Author (byline): Carlos Zayas
- Work: The Bright Side of Death
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1644
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
Guard: Felix, here is your cell and cellmate, Tristan. Both of you are set to be executed on the morrow. Spend your final hours thinking on your sins and may the gods have mercy on your souls. Felix: Good eventide to you! (cheerfully) Tristan: What are you so excited about? (slightly irritated) Felix: Tomorrow I will be returning to my family whom I have lost. Isn’t that wonderful? Tristan: Tomorrow you will die, descend into Tartarus, and suffer for all eternity. Isn’t that wonderful? Felix: Nonono, why would I end up in Tartarus? I have done nothing wrong! Tristan: In that case, you must be in the wrong place because, last time I checked, murder is wrong. Felix: That’s rich coming from a murderer. (contently) Tristan: Isn’t it? (sarcastically) (a beat) So did you murder anyone or not? Felix: Well, I didn’t “murder” anyone… Tristan: Then what are you here for? Treason? Rape? High-stakes confidence tricks? Felix: Confidence tricks? Tristan: (sigh) Have you ever heard of a con? Felix: As in a negative side effect or a sort of monetary scam? Tristan: Which would you think could result in death? Felix: I feel like most people, excluding myself, would consider death a negative side effect. Tristan: (fuming silence) Felix: I’m going to assume the latter.

Tristan: I can’t believe that someone such as yourself managed to muddle through the thought process of such an elaborate crime… Felix: So you believe that I’m not capable of such a heinous crime? Tristan: (a beat) Yes. (sternly) Felix: Fantastic! We have established my innocence! Tristan: (sputtering) ...Sure. (a beat) So now will you tell me WHY you are here? Felix: I asked to be. (matter-of-factly) Tristan: (a beat) You asked to be executed? Felix: Yes! Tristan: At this point, that sounds completely reasonable. Felix: Now do you understand why I am so elated? Tristan: If only I could share your enthusiasm... (a beat) Then why didn’t you just commit suicide? Wouldn’t that be faster than waiting for a public execution? Felix: Suicide is a coward’s way out. (devotedly) Tristan: And asking to be killed isn’t? Felix: Eh, semantics. Tristan: I beg to differ. Felix: No need to beg, you can be wrong if you want to be. Tristan: I didn’t murder my boss, spend months on the run from the law, get arrested by my own friends, and get put to death so that I could argue semantics with a maniac!!! (Growing in anger as the sentence goes on) Felix: How rude! You call me a maniac AND you are unprepared to quarrel over semantics? Have you never been in an educated discussion before?

Tristan: (still fuming) Alright, I’m fed up with this stupidity! Guard! GUARD! YES, YOU! What is HE dying for?! (pointing at Felix) Felix: I’ve shared this with you already! I asked to be here! (hurriedly and worriedly) Guard: In a manner of speaking I suppose. He turned himself in… after confessing to the murder of his wife and child. Felix: I didn’t “murder” them… Tristan: (interrupting) You are a filthy liar! Felix: As if lying is of high import on your moral scale. Tristan: SHUT UP! We are the same, don’t you see? Felix: Don’t put me on your level, killer! (shrill) Tristan: You are just as much a killer as I am! Maybe even more so considering you murdered your own family! Felix: I did not “murder” them! Tristan: Then give me a GOOD reason for being here! One that isn’t, “I asked to be here bluhbluhbluh.” Felix: They were in pain. I had to stop it. (matter-of-factly) Tristan: (a beat) Oh goodness, you’re a psycho. (frightened) Felix: You already called me a maniac, do you have to persist in these accusations? Tristan: No, I was insulting you with calling you maniac. You are legitimately a psychopath. Felix: Congratulations! You’re the first person I’ve talked to in months that has used legitimately in a correct setting! Tristan: So you’re admitting to being a psychopath? Felix: No, I’m simply stating that you used the word correctly given your belief that I am, in fact, clinically insane. Tristan: (nervously laughing) I’m glad I could make your day, Felix. (in a hushed voice) Hey, Guard, can I get moved to another cell. With this guy around, one of us may not make it to our execution party. Guard: Against protocol, my apologies. Tristan: Darn you, you responsible employee! (angrily sarcastic) (a beat) So, Felix… Felix: Yes, Tristan? Tristan: What exactly qualifies as “in pain”? Am I in pain? Felix: Are you? I could fix that!(excitedly) Tristan: NOPE, I’M GOOD. Just… curious about your family… hehe… Felix: My wife was the most wonderful woman I had ever met: gorgeous, intelligent, gentle, loving… Oh how I miss her! And my daughter, she was duplicate of her mother! I could tell, even as a newborn, that she was going to be just like her mother within a few years. She had greatness to look forward to! Tristan: Then why is she… dead? Felix: Childbirth is a painfully long process, especially when there are no trained professionals around to help. Tristan: You killed them in the middle of the birth of your first child? Felix: Killed is such a strong word… I helped them! Tristan: By ending their lives? Felix: Must we go over this again? Tristan: Right right, sorry sorry. Felix: Now, as I have narrated my tale to you, I feel it only fair for you to tell me why you are here! Previously, you mentioned (clears throat) quote: “I didn’t murder my boss, spend months on the run from the law, get arrested by my own friends, and get put to death so that I could argue semantics with a maniac!!!” End quote. By the way, the section calling me a maniac still hurts. Tristan: Right, sorry about that. (more nervous laughter) It would probably be more appropriate to call him my ex-boss…

Felix: (interrupting) Because you murdered him! Tristan: Huh, I guess that you’re right in that line of thinking but before that, he fired me. I was working my way to the top in the mercenary business when our contractor cut us out of a job. We did our work fully and justly… Felix: (interrupting) As justly as a mercenary can! (laughing) Tristan: Hehe… yeah… Anyways, we were cut out of our pay so we confronted him. He told us that if we didn’t hush up about it, he would let our whole company go! At that point, the fuel of fury and the imminent injustice… Felix: (interrupting) Nice alliteration! Tristan: (a beat) I would really appreciate it if you stopped interrupting me. (silent anger) Felix: Oh right, my apologies! Tristan: So at that point, I just couldn’t control myself any longer and in a fit of blind emotion, I slit his throat in front of all my men. That was my downfall. Suddenly, all of my men turned against me calling me “murderer” and “barbarian”. My closest friends were now against me. It took me about a minute to realize what I had done. Felix: You killed a man? Tristan: No, I’ve killed men in the past. Mercenary, remember? Felix: Ahh… continue! Tristan: I’ve killed men before, but never out of rage. It was always for money, justice, or necessity but not this time. Blind rage drove me to kill a man I had known for years without legitimate purpose. It scared me to know what the powers of emotion can do to a person. They can break us. So I ran and ran for months and months, figuratively of course. All the while, it was my old mercenary buddies that were hunting me, not the imperial guard or anything like that. My closest friends, the men I had work with for years, were the ones who wanted me brought to justice. And now I’m here before you, trying to come to terms with my fate. But by watching you and your understanding of death, I can positively see death as comfort. So thank you for that.

Felix: It seems that you have embraced your fate, hmm? Tristan: It seems that you are in love with yours. Felix: No, I’m in love with my wife which is why I’m excited about tomorrow! Tristan: You know what Felix, I’m beginning to feel better about tomorrow as well. Thank you. Felix: (a beat) So does that mean that you were in pain earlier? Are you still in any pain because I can help! Tristan: (chuckles) No, I think I’ll be fine for now. Guard: Alright, you two better get some sleep now. Tomorrow’s events are scheduled early and you should be fully awake to give your last words. Goodnight and I pray that you both have seen your actions in a new light. Tristan: Thank you Felix. Felix: What are you thanking me for this time? Tristan: For keeping my mind off of the fact that this is my last day on Earth. Tomorrow I will descend into Tartarus but I haven’t spent all this time thinking on my fate but rather on you and your story and your… uniqueness. Felix: That’s so kind of you! I suppose I should thank you too! Tristan: For what? Felix: For reigniting my enthusiasm for being able to meet my family once more on the morrow! I hope they won’t be bother by the fact that I helped them with their pain without asking them… But physicians help unconscious patients all the time right? Same principle. Tristan: Hehehe… Whatever you say Felix. (a beat) Goodnight Felix, sleep well. Felix: Aren’t you going to sleep too? Tristan: Nooooooo I’m going to stay up and uhh… look at the stars!

Felix: But we don’t have a window in our cell. Tristan: Don’t worry about it Felix, I’m just not tired yet. Felix: Whatever you say! (falls asleep and begins to snore excitedly) Tristan: (sigh of relief) I’m not falling asleep in the same room as he is. Guard: I thought that you were comfortable with the idea of death now. Tristan: Were you eavesdropping? Guard: I have been standing outside your cell this entire time, I literally could not help but to overhear all of this. Tristan: Fine. I may be comfortable with death but not with death by Felix.
```

---

## IC-1046: The Commander

- Title: The Commander
- Author (byline): Steve DuBois
- Work: The Commander
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2530
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
[Actor 1 plays two characters: MUTEBA, a monstrous commander of child soldiers, and THE COMMANDER, a benevolent invisible guardian whom only Fabrice can hear, and who may or may not be real.]

[Actor 2 plays FABRICE, a 12-year-old child soldier struggling for survival. At times, his demeanor changes from that of a frightened boy to that of a confident adult as the spirit of the Commander occupies him.]

[At various points in the performance, THE COMMANDER addresses the audience directly, serving as a narrator. Fabrice is confined by the fourth wall, though his thoughts become audible at times.]

1 COMMANDER: [Narrating, from behind Fabrice] The pieces of Fabrice’s weapon were arrayed before him, cleaned and oiled and ready for assembly, glinting under the tropical sun. But he had had nothing but a handful of cassava for supper last night, snd he could not for the life of him remember how to put them back together again.

2 FABRICE: I…I know this. I have done this a dozen times. A hundred times! I must remember!

1 COMMANDER: The years, under Sergeant Muteba’s leadership had taught Fabrice and the other boys many things. How to assemble and disassemble a weapon. How to make a meal of grubs and grass. How to raise their rifles on another boy, and see the lights go out in his eyes. And above all, how to forget. And now, sure enough, Fabrice had forgotten.

2 FABRICE: Muteba will beat me, and I am in no shape to take another beating. He will kill me, and there will be no one left to shield the other boys from him. They will put me in the ground, and move on, but there will be no one to protect them from Muteba. Here he comes now, up the line…

1 MUTEBA: [Hitting a boy] No, you fool! You must learn to care for your weapon! Your weapon is your life! Do you hear me? Your weapon is your life!

2 FABRICE: My life…here in pieces before me. So hungry. I cannot remember. Maybe…maybe if I…

1 COMMANDER: [To Fabrice, insistent but not unkind] No, boy! That is not how it is done!

2 FABRICE: What? Who…who is speaking? I…I hear you, but I cannot see you…

1 COMMANDER: Look at the pieces before you. It is a monumental task, for one so young. Like eating an elephant! Tell me, Fabrice, how does one eat an elephant?

2 FABRICE: Who are you? Where are you? How do you know my name?

1 COMMANDER: One bite at a time. One eats an elephant one bite at a time. Here. Allow me to assist you…

[The two of them move in perfect unision. Fabrice stares down at his hands, amazed, as they do the work for him, of their own accord.]

1 COMMANDER: Short end of the bolt into the bolt carrier…so! Rotate counter-clockwise until the click…so!

2 FABRICE: My hands…how…

1 COMMANDER: Carrier group to the gas piston chamber, notches aligned, into the opening… so! Spring in the rear opening, aligning with the opening…

2 FABRICE: [Remembering, eyes wide] Muteba…that night in the tent…drunk on lotoko, calling out to me, smiling, his belt…his belt undone…

1 COMMANDER: Not now, Fabrice! One bite at a time. Spring into receiver…so! Rear sight folded forwards…so! Dust cover into place, shut with a snap…so! Yes. Just so.

2 FABRICE: And he is coming. Muteba…

1 MUTEBA: [To the other boys] Do not look at me! I will not countenance eye contact! [To Fabrice] Yes. Good, Fabrice. You are a good soldier, my boy. [He caresses Fabrice’s cheek. Fabrice shudders as he moves on]

1 COMMANDER: And what would you know of being a good soldier, Muteba?

2 FABRICE [Terrified] Quiet! He will hear you!

1 COMMANDER: He cannot hear me, Fabrice. No one but you can hear me. For it is you I have chosen.

2 FABRICE: Who…who are you? For what have I been chosen?

1 COMMANDER: Who am I? I once had a name, though I scarce remember it. But you and the other boys are soldiers, or so Muteba says. A soldier has no name, but only a rank. Therefore, let us call me The Commander.

[Intro here]

[Fabrice huddles in a foxhole, rifle raised, as the Commander narrates.]

1 COMMANDER: Another battle. The enemy were boys no older than themselves. The men of the nation were used up long ago.

2 FABRICE: Muteba, behind us, far to the rear, screaming for us to advance. But we who have lasted, we know. The boy who rises to advance will be scythed down instantly. To obey is to die. To flee is to die. Ignore the order, and pretend not to hear, and I may live. For today.

1 COMMANDER: Squeeze the trigger, Fabrice…yes, just so. It will be over soon. Soon, one side will grow tired of the fiasco, and retreat.

2 FABRICE: And then, the night. Muteba, cooking up the lotoko mash, inviting whatever boy fights best to his tent. Best not to fight too well.

1 COMMANDER: Best not to fight at all. [To Fabrice] Look, Fabrice! Across the clearing! They are trying to outflank you!

2 FABRICE: What? Where are you…

[Their heads move in perfect unison. As the Commander raises his arm, Fabrice raises his.]

1 COMMANDER: There! In the trees! They seek to move towards the bluff on your right!

2 FABRICE: Yes! Yes, I see…

1 COMMANDER: From the bluff, they will be able to enfilade you from above. Your cover will be useless. You will be slaughtered.

2 FABRICE: What can I do? I cannot advance, I cannot retreat, and I cannot stay where I am…

1 COMMANDER: Think, boy! A good soldier relies on his comrades.

[The Commander and Fabrice speak as one. Fabrice’s demeanor and voice are no longer that of a boy—he is calm, powerful, commanding.]

1 AND 2: Sony! You must cover me, and hold off the enemy! Pierre! You must turn your rifle around, and hold off Muteba! Do you understand! [Pause] My brave friends! Good luck to you!

[Moving as one, The Commander and Fabrice hop up out of the foxhole and burst into a sprint. Fabrice stares down at his legs in shock as they move without his control.]

1 COMMANDER: Around them, Fabrice. Around the outside. The enemy are intent on your original position. We will out-flank the flankers!

2 FABRICE: How is this possible? Are you a demon, to possess my body so?

1 COMMANDER: No, Fabrice. Though some would say I once was one.

2 FABRICE: Is my soul in danger?

1 COMMANDER: In war, Fabrice, every soldier’s soul is in danger! But look, there, ahead, atop the bluff. They are preparing to fire on your comrades!

2 FABRICE: But their backs are to us!

[They no longer move in unison. Fabrice raises the rifle, his voice full of vengeance]

2 FABRICE: The first one, the one in camoflauge. Squeeze the trigger…so! The second one, the dark skinned one. Squeeze the trigger…so! The third one, the boy, my own age, his rifle lowered, his eyes wide—Ha! yes, I have got you! Squeeze the trigger…squeeze the…

[The Commander raises his own hands into firing position, mirroring Fabrice’s. Fabrice struggles, but he cannot make his finger move. Slowly, in unison, they lower the rifle.]

2 FABRICE: He’s getting away! Why? They were the enemy! They wanted to kill us! They deserved to die!

1 COMMANDER: Fabrice…the first two deaths were necessary, to save your friends. But they were not deserved. No one in this war, save those who perpetuate it and profit by it, deserves to die. And the third boy…his death was neither deserved nor necessary.

[Fabrice scowls, a petulant boy, and kicks a rock away.]

1 COMMANDER: I fear, Fabrice, that you have seen too much death, that you have grown a callus on your soul. Yet I also know that there is mercy in you. Look behind you, Fabrice. Look what has happened.

[They turn in unison. Fabrice’s expression slowly changes from petulance to sorrow.]

2 FABRICE: Sony! Pierre! My friends! No…no!

1 COMMANDER: They died to save you, Fabrice, and the whole platoon. From your true enemy. Behold, Fabrice. Your true enemy advances.

2 FABRICE: Muteba!

1 MUTEBA: COWARD! TRAITOR! YOU HAVE DENIED ME VICTORY, FABRICE! YOU HAVE DENIED…

[Fabrice says nothing. Eyes downcast, he gestures at the men he has just killed.]

1 MUTEBA: You have denied…you have…oh. Oh! [A slow, stupid smile spreads over his face.] Oh! A cunning stratagem! An advance against the enemy, just as I ordered! [He wags a finger at the other boys.] Did I not order you to advance? And here, finally, is a soldier who takes orders! I am a commander who will always countenance cunning and bravery!

[He sweeps Fabrice into a one-armed embrace. Fabrice cringes in terror.]

1 MUTEBA: A cheer for Fabrice, boys! A CHEER, I SAID! [To Fabrice] This calls for a celebration, don’t you think? Let’s have a drink, back at my tent, you and I, my brave boy…

[Scene break]

[Fabrice sits, eyes downcast. Muteba stands tall, leering, cooking something over a fire.]

1 MUTEBA: Command is a lonely burden, my boy, and a heavy one. Ah, our drink is ready. [He lifts a cup from above the fire, and offers it to Fabrice, who shakes his head, his eyes downcast.] Are you sure? It will make things easier, I promise. [Fabrice shakes his head again. Muteba shrugs, and takes a long swallow.] No man who has not picked up the burden of command can know its weight. No man can know the pain I feel at the loss of each soldier under my protection. You may look at me, you know. You have earned the privilege. I will countenance eye contact, under these unique circumstances. [He places a finger under Fabrice’s chin, forces his head up. As soon as he removes his finger, Fabrice’s eyes return to the ground.] As you will. [Muteba takes another long draw from the cup.] But it is not the luxury of the commander to allow himself to feel these deaths as keenly as he might. For if the commander succumbs to grief, who will lead his soldiers? To be a commander is to learn to put one’s own deepest feelings aside. One must advance.

[As Muteba speaks, Fabrice’s eyes begin to slowly lift from the ground, and to fill with a strange light. His posture moves slowly from stooped to erect. Muteba, lost in his rant, does not notice.]

1 MUTEBA: Now, you, Fabrice, it seems to me that you have the stuff of command in you.

[Fabrice speaks under his breath. His voice is not at all that of a boy.]

2 FABRICE: Yes. Just so.

1 MUTEBA: But you care too deeply, Fabrice. The boys will follow you. You proved that today, with Sony and Pierre. But to allow yourself to care as you do? It is a mistake. To care too much can drive a commander mad.

2 FABRICE: [Under his breath] And the commander is mad indeed.

[Muteba, half-drunk, wraps his arm around Fabrice’s shoulders as he speaks. Fabrice’s hand moves steadily around Muteba’s waist, unfastening the gun holster on his opposite hip.]

1 MUTEBA: Let me help you, Fabrice. Let me help you go away to a place inside, where you cannot be hurt, where one can do that which needs doing without shame. Let us give you some practice. [He loosens his belt.] That is an order, and I will not countenance dissent.

2 FABRICE: [Fabrice breaks free, and steps back, turning to face Muteba. He raises his eyes. In his hands he holds Muteba’s pistol.] No more than we shall countenance you any longer, Muteba.

1 MUTEBA: What…my…

2 FABRICE: Your weapon. Your weapon is your life.

1 MUTEBA [Not intimidated.] Ah, but are you sure, boy? Have you truly learned the lessons I have tried to teach you? Are you ready to be a leader? No. No, I think not. You have always been soft, boy. You have not the hard heart of a true killer!

2 FABRICE [A frightened boy again] No. I do not.

[Muteba disappears behind Fabrice, who stands alone, with the pistol raised.]

2 FABRICE But I know one who does. [In voice not his own] Allow me to assist you. [He squeezes the trigger twice, then slowly lowers the pistol.]

[The Commander reappears.]

1 COMMANDER: A death that was both deserved and necessary.

2 FABRICE: Just so. And now, at last…who are you?

[A long pause.]

1 COMMANDER: I was a soldier, Fabrice. I led men into battle, and later, to my shame, I led boys. Death came for me, eventually, as is the way of war. And yet I did not die, but live on. It is my fate, Fabrice, to be one with the children of battle. My soul bonds with that of a boy. I share his experiences and his pain. And I must live on in this fashion forever—or until twenty-four hours pass without a single child of this nation firing a weapon in anger. Until then, I can never rest.

2 FABRICE: But…that is impossible. You have been set an impossible task.

1 COMMANDER: How does one eat an elephant, Fabrice?

2 FABRICE: One bite at a time.

1 COMMANDER: Yes. Just so.

2 FABRICE: How can I help?

1 COMMANDER: You may help by becoming a soldier in my army, Fabrice. By guiding your platoon back to safety and then refusing to take up arms again. By telling the story of your life to all who will listen, for in this new war, your life is your weapon. And you may help by telling them about me, Fabrice. Spread the word to every village and camp. Let the boy soldiers know that the Commander is on the prowl, and that I am coming quickly to their aid, to be their partner and their shield. It is your mission, and mine, to teach them their true strength. To show them what it is to be a man and a soldier. To tell them who the true enemies are, and at whom the guns should be pointed. And tell the Mutebas as well! Tell them the Commander is coming for them. I leave you now, my soldier, to your mission. Tell them all, Fabrice, that the Commander is coming.

[He disappears]

2 FABRICE: And with that, he was gone. And yet I felt no dimunition of my strength. There was only my purpose. The boys waiting for me, back in camp. And the rest of the boys, everywhere, waiting for my story. What had I to fear? I was a man with a mission, ready to advance, and fully in command.

[For a moment, the Commander reappears, and places a hand on Fabrice’s shoulder.]

1 COMMANDER: Yes. Just so.
```

---

## IC-1047: The Lore of the D-Rings

- Title: The Lore of the D-Rings
- Author (byline): Elijah Sams
- Work: The Lore of the D-Rings
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: F, M, S, G, C, O, O2, K
- Teaser before the introduction: No
- Spoken words (computed): 1065
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
Scene: An American High School.

Fred: (Finding binder and picking it up, or taking it off of shelf.) Hey, check it out, Sam, what is this? Sam: It's a D-Ring binder, Fred! It's ancient!

F: (Opens binder and flips through a few pages, then several more, very quickly.) Whoa! There's a copy of every test I've ever seen at the school! –. Better bring it to Mr. Grey–. (Michael Kellum, a Gollum-like charcter, suddenly appears and grabs the binder.) Michael Kellum: Ah ha! Give it to me! It's mine!

F: Who are you? Let go!

M: (Hisses, runs away.)

S: That was Michael Kellum! He's a legend, he's like 25 years old and still at this high school.

F: Well, he's not getting this D-Ring binder. I've got to turn it in.

S: A Quest! Sweet! I call sidekick! One Sophomore, One D-Ring Binder, One Quest to Destroy it. The Lore of the D-Rings.

S: Are you sure you want to turn it in? You could ace every test in every class!

F: Nah, not really my style. You?

S: Nah, I've already got a 4.2 GPA and that's technically impossible already.

F: Hey, Mr. Grey, I found something– Grey: (Aggressively grabs the binder.) Ah! Fred O'Gabbins! I know this binder! Many years ago, the principal of this school, Sir Ron, created the D-Ring Binders, three for the English teachers, seven for those who dare to instruct science and math, and nine just sort of, you know, social studies, music and whatever. But whenever a student has discovered a binder, they become obsessed with it, unable to think beyond the tests, lingering on the outskirts of academic achievement forevermore– This One D-Ring Binder contains them all! Bear it at once to the office and there cast it into the Great Shredder of Gethromel!

S: Seriously? That's awesome!

G: Actually, it's just what I call the regular shredder.

F: Can't you do it? It's a Saturday, we're only here because–

G: Because you're always talking about movies and books in my class and if you don't destroy the D-Ring Binder, YOU!

F: Oh, please, really?

G: –SHALL NOT–

S: –We all know where this is headed–

G: –PASS!

F: Feel better now?

G: Yes, it's very satisfying, PASS! See? You will take with you a company of heroes to aid you in your quest.

S: I already called sidekick.

F: There's basically no one else here except Chad. (He gestures off stage.)

S: Oooh, Bro-mir!

F: Why do you call him that? Chad/Bro-mir: (Swaggering.) Dude, Bro! I heard my name, bra!

F: Oh, dear God, that's why.

G: You will also take Kim Li.

S: Ooh, good call, his knowledge of the World of Warcraft is unparalleled!

F: We're fine with just Chad–

C: Solid, bro!

S: Call him Bro-mir!

G: Beware Michael Kellum–He's been watching us for three minutes now–He wants the binder–

F: Why don't you just expel him?

G: He still has a role to play–

S: Ah, a prophecy!

G: No, I cast him in A Streetcar Named Desire, we're doing it at the middle school–

F: Okay, we'll do it. Let's go. We'll just take the senior hallway–

C: Dude, bra! One does not simply walk down the senior hallway!

F: It doesn't matter today, Chad, it's a Saturday.

C: Then, dude bra, why am I here?

F: I assume it it's because you skip class all the time.

C: Bro, harsh.

S: Perhaps we should stop by my locker and get my fire staff.

F: You have a fire staff?

S: I got it from Kim Li! It's an exact replica of a seventh level mage staff as featured in episode 9 of–

F: Okay, don't flood the room, Okay, if it makes you guys feel better, no senior hallway. We'll just cut through the cafeteria– (Opens door.) Whoa, what's going on here?

S: SHHH–..Easy, easy– Speech kids are easily disturbed, they can snap at almost any moment– Orc: Hey! What are you non speech kids doing 'ere?

Orc 2: Yeah, where's your suits?

O: We're starving! We woke up at 4 am. We ain't had nothing to eat but cold pizza for three stinkin' meets!

O2: What's in the binder? (Moves aggressively towards the binder.) You got some sweet cuttings in there, eh? Some sweet Nat Qual cuttings, I bet!

F: Sam, can't you get us out of this? You seem to understand these kids.

S: Understand them, yes, I understand them, I was one of them! And once I have this cursed dental appliance removed I shall be one of them again! Okay, I got this. (He takes a second to get in character or some kind of pre-speaking ritual.) HEY LOOK, THEY'RE POSTING SOMETHING OVER THERE!

O: (Displaying extreme excitement.) Is it Poetry Finals? OMG! OMG! OMG! Move maggots! (He shoves them aside with a sweeping motion, spins, and switches into Chad/Bro-Mir.)

C: (Stumbling, and shell shocked.) Dude, I have no idea what just happened. Why do we have to destroy the D-Ring Binder anyway?

S: It's a compendium of solutions to this academic establishment's assessments! This appliance is killing me.

F: It's all test answers.

C: Dude. Bra. Give it to me. (He reaches for binder.) I totally need it. Bro, I want it. I can skip class and still pass tests, dude bra.

F: I can't, Chad, I'm supposed to destroy it. Besides, you need to actually learn things, having the answers isn't–. (Kellum suddenly appears again, grabbing the binder. He struggles with Freddo.)

M: Ah ha! Give it to me! You stole it!

C: Dude! Not cool! I need that bro! Bro! Bro! Dude! Dude, bro! Bro! bro. bro. dude bro. (Collapses.)

S: The mighty Bro-mir has fallen!

F: (Continuing to struggle with Kellum.) He'll be fine, he just hasn't had a Monster energy drink in the last 30 minutes.

M: Give it to ME!!!

F: You're like 25 years old and still in high-school–I don't think it's helping.

M: It's not my fault I can't do the daily assignments!

F: Why can't you?

M: They're not in here! Idiot!

F: Well yeah, you have to do the work sometimes. (He puts out supreme effort and rips the binder from Kellum's hands. Holds it over head.) So, let's just destroy it, and then you can move on with your life.

S: (Aside.) –And so, faced with a dilemma of epic proportions, the twisted creature Kellum–

M: That's really distracting, that thing that you're doing.

F: Look, we'll destroy it, but we'll help you with your classes.

S: Speak for yourself! I have a reputation to uphold!

F: You have replica firestaff in your locker.

S: Touche.

M: Well, that's better than my plan.

F: What was your plan?

M: I bites you and runs away with the D-Ring binder.

S: And so the final page of our quest is turned– (Spins and turns into Mr. Grey.)

G: (Holding a staff.) With the one D-ring destroyed, Michael Kellum totally nailed the role of Stanley Kowalski in A Streetcar Named Desire.

K: (Screaming Marlon Brando style.) Stella, hey Stella!

G: Kid's a natural, anyway, he graduated or something. Bro-mir eventually found employment at a Hollister, while Sam and Freddo finished high school. And I, I got this rockin' firestaff. Got the hook up from Kim Li, bought it with money from a deal I made to turn the introduction of this speech into three more speeches. That’s right, I'm gonna prequel this sucker, and then I'm gonna sequel it– (Takes a deep nasal inhalation.) –Ah, I smell a franchise!
```

---

## IC-1048: The Princiapls of Drugs

- Title: The Princiapls of Drugs
- Author (byline): Lawson Powers
- Work: The Princiapls of Drugs
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2321
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
THE PRINCIPALS OF DRUGS

By Lawson Powers

CAST LIST
Mrs. Chapman is a math teacher
Bill Clinton
Obi Two KeToni
Dr. Scott is an explorer
Mike is a student who is high the entire time
Mr. Sully is the Principal of Mike's school

WE BEGIN IN A MATH CLASS ROOM.

Mrs. Chapman is at the front of the class, teaching math.

MRS. CHAPMAN

And that's how you find the derivative of the- Mike! Mike! What are you doing??

Mike has been staring at his hand, very intently. As he brings it closer to his face, it scares him, and he whimpers and thrusts his hand away.

MRS. CHAPMAN (CONT'D)

Mike, I asked you what you were doing, are you just going to sit there like an idiot or answer me?

Mike leans over, takes a slice of pizza out of his bookbag and begins eating it, constantly glancing around as if he is scared and paranoid.

MRS. CHAPMAN (CONT'D)

Mike, that is it! I'm not sure why you're eating a slice of pizza right now or why it was in your bookbag, but I have told you time and time again not to eat in this class! Go to Mr.

Sully's office! He's going to be very upset when he finds out what you have done.

IN MR. SULLY'S OFFICE

MR. SULLY

Mike, I don't know what kind of crap you're trying to pull, but I've dealt with punk kids like you more times than I've crapped in Mrs. Chapman's classroom..and that's a lot! Now I'm asking you for the last time. You better tell me what you're up to or so help me I'll crap ON YOUR HEAD!

MIKE (HIGH)

Mr. Sully, man..you gotta like..chill man.

MR. SULLY

Well, it is a little warm in here..let me go into the other room and turn on the air conditioner.

Mr. Sully walks out of the room. Mike takes out a joint he has in his pocket, lights up, then lays belly-first on the floor, acting as if he is trying to swim.

As he is doing this, Mr. Sully walks back into the room, looks startled, and then...

MR. SULLY (CONT'D)

Mike, what are you doing?

MIKE (GETTING UP) (MUMBLING IN A BILL COSBY VOICE)

Jello..puddin pop....jello puddin pop

MR. SULLY

Yes, that does sound tasty, doesn't it, Mike?

Mike takes another hit of the joint, and this time Mr. Sully sees it.

MR. SULLY (CONT'D)

Mike! WHAT ARE YOU DOING??? You have weed..and you didn't offer me any??

MIKE

Oh.. Sorry, Mr. Sully..I just..well, this stuff is much stronger than the stuff you had back in your day, and-

MR. SULLY

What. You think I can't "hang" with the youngsters nowadays? Give me that!

Mr. Sully snatches the joint from Mike's hand and takes a very long drag. Immediately he is high as a kite.

MIKE

Alright Mr. Sully!!

He begins to chuckle

MR. SULLY

Hey, what are you (chuckling) laughing at? (Chuckling)

They keep chuckling to themselves, sometimes with each other, pointing at each other and laughing.

Immediately they stop as if nothing happened.

MIKE

Alright, well what do we do now?

MR. SULLY (TAKING ANOTHER HIT)

I don't know...but suddenly, I'm extremely hungry.

MIKE

Me too! Want to hit up some Taco Barn? That place is the culmination of a day of bad decisions..

MR. SULLY

That does sound tasty..but I have a pantry full of food right there!

MIKE

AW YEEEEEAH! (Running to pantry) Let's see, you got some Little Donnie's, some Geez-its...SWEET! You have Swiss Trolls! (To audience) Yeah, copyrights suck, don't they.

MR. SULLY (GIDDY)

Ooo hehehe the Swiss Trolls are amaze-balls hehehe

They take the swiss trolls, lay down and begin to eat. After a little...

MR. SULLY (CONT'D)

Well, this is fun and all, but I need a little kick. (Walks to desk, pulls out a syringe) I have some Heroin here..want some?

MIKE

Ah, no thanks, I have some meth here, I'll have some of that.

Mr. Sully shoots up with the Heroin, Mike begins smoking meth.

Mike begins taking his shirt off, it gets stuck on his head. Mr. Sully sits down, curls up in a ball (but still upright), and opens his eyes wide while rocking back and forth. Suddenly Mr. Sully says

MR. SULLY

Psh (walkie talkie sound) prepare for take off. 3...2...1...blast off.

He springs up, making sounds like a rocketship. Mike has managed to get his shirt of and stands watching Mr. Sully. Suddenly they both pretend to be seated, strapped into the rocket.

MIKE

Alright, commander. (Flipping switches on an invisible board in front of him) We're making our way out of the unicorn belt as we speak. OH NO! The unicorns are not happy! I repeat, the unicorns are not happy! They're trying to attack us! Evasive maneuvers!

They imitate evasive maneuvers, then

MR. SULLY

It's not working! They're horns are breaking our defenses!

MIKE

Emergency landing! Land on that moon over there!

OBI TWO KETONI

That's no moon...that's a satellite.

MR. SULLY

Oh no! Obi Two is right! It's the...killer star! (To audience) Again. Copyrights are the worst.

MIKE

Turn around!

MR. SULLY

I can't! They're pulling us in with their magnetic field!

They land

MR. SULLY (CONT'D)

We're about to be boarded by the storm troopers! What do we do??

MIKE

It's okay! I just learned the force and I have a lightsaber!

A school janitor is walking by. As he does, Mike shouts,

MIKE (CONT'D)

It's a stormtrooper! Get him!

And jumps on the janitor. The janitor stands no chance against this meth hyped kid, and soon is knocked out.

MIKE (CONT'D)

Alright, now I have his stormtrooper costume. I'll go check things out.

As he steps out of the space craft, Mr. Sully launches again, Mike stops and stare in shock. Mr. Sully is pulled back in by the magnetic field. Mike begins to walk again and Mr. Sully again launches, only to be pulled back in. Mike walks again, and Mr. Sully again launches and the same happens.

MIKE (FORGETTING WHAT JUST HAPPENED OR THAT THEY THINK THEY ARE ON THE DEATH STAR)

Uh...Mr. Sully! My arm just turned into a snake! And he's angry!!

Mike runs around, fighting his arm snake.

MR. SULLY

Ohhh no. (Groaning in pain) It's happening! It can't be happening now! (Starts breathing like a pregnant woman in labor.) The cow is a-comin!

MIKE (STOPPING MID FIGHT)

Wait..what?

MR. SULLY

THE COW! IS COMING! What about that don't you get?? I'm bout to give birth to a cow!!

Mike breaks character and begins talking

MIKE

Uhh, could we not give traumatize the audience by having you give birth to a cow?

MR. SULLY

But this part is my favorite!

MIKE

I know..but it's pretty clear that watching you give birth to a cow would scar the audience. I mean, pieces that show people giving birth are just gross. Ya know?

MR. SULLY

Alright, fine.

MIKE

Okay good. So I'll go back to fighting my snake arm and you go back to doing..something not traumatizing.

Mike goes back to fighting his snake arm, Mr. Sully again curls up in a ball, but upright, and then launches up, making rocket sounds.

Mike stops fighting, turns to him and says,

MIKE (CONT'D)

We already did that bit, remember?

MR. SULLY

Oh. Right, sorry.

Mike goes back to fighting his snake arm, Mr. Sully stands there, confused, then begins to fight *his* snake arm.

MIKE

No! I'm already doing that! Find your own thing!

MR. SULLY

Oh. Yeah, sorry.

Again, Mike goes back to fighting his snake arm.

Mr. Sully stands there for a second, then looks hard into the distance.

MR. SULLY

Mike...Mike, do you see that?

Mike is gone. We hear the sounds of dinosaurs off in the distance. A pterodactyl swoops over Mr. Sully's head and he has to duck down to miss it. All of a sudden, an off-road vehicle roars over the horizon, screeching to a stop in front of Mr. Sully.

DR. SCOTT

G'day mate! What brings you to the prehistoric age of dinosaurs on such a beaut of a day?

MR. SULLY

Just a little heroin.

DR. SCOTT

Ah, I see. What good is exploring without a little heroin, am I right?

MR. SULLY

Uh, sure. Who are you?

DR. SCOTT

Where are my manners? Dr. Scott here, ready to guide you through these parts during the time when they were most dangerous!

MR. SULLY

So we're in prehistoric times, eh?

DR. SCOTT

That's right! Just built a time machine to take me back, but if I had known that shooting up to ride the magical rainbow would've taken me back in time, I would have just done that!

Well, what are we waiting for? Hop in and let's explore!

They hop in and start driving.

MR. SULLY

Wow! What's that over there??

DR. SCOTT

Ah, that's the extremely interesting Jockus Highschoolius, or in layman's terms, a High School Jock.

MR. SULLY

Fascinating!

DR. SCOTT

Extremely! Here, take this tranquilizer gun. We need to sedate it so that I can collect a DNA sample! But it's going to take a lot of tranquilizer darts in order to knock out such a large dinosaur.

MR. SULLY

Got it! Looks like my years of poning racist 3rd graders on gaming systems are finally going to pay off!

A jock is at his locker, talking to a girl. In the middle of their conversation...

JOCK

Yeah so I totally have this nerd in a headlock and I'm about to take him into the bathroom to give him a swirlie when-

Mr. Sully creeps up, rolls and comes up on one knee, his fingers making a gun shape which he points at the jock

MR. SULLY

Pew! Pew! Pew!

JOCK

Uhh, Mr. Sully...are you okay?

MR. SULLY

Pew! Pew! Got him!

Mr. Sully runs back to the imaginary vehicle and jumps in. They spin out, leaving the jock extremely confused.

MR. SULLY

Boy! That sure was fun! What's next?

DR. SCOTT

Well, I only came back for that DNA sample, so I'm headed back to the present.

MR. SULLY

Aw, man! Well, this sure was fun, Dr. Scott! I guess I'll head back to my office too!

Mr. Sully spins around a couple of times, making whirring noises.

MR. SULLY

It's good to be back in my office!

Mr. Sully stands there for a second, then gets a phone call.

MR. SULLY (CONT'D)

Hello?

BILL CLINTON

Hello! Is this Mr. Sully?

MR. SULLY

..yes...who is this?

BILL CLINTON

This is the 42nd President of the United States of America!

MR. SULLY

Wait.. Is this Bill Clinton??

Bill walks in

BILL CLINTON

Well, define "is." (Laughs to himself)

MR. SULLY

Cool! I'm hanging out with a former President!

BILL CLINTON

That's Mr. President to you!

MR. SULLY

Oh, right, sorry. So what do you want to do?

BILL CLINTON

You got a secretary around here? I like talkin' to those secretaries.

MR. SULLY

Oh, you don't want to..um.."talk" with my secretary, she's very unattractive.

BILL CLINTON

Oh well that's too bad. Why don't we just smoke some doobies and relax, man?

They light up and begin smoking.

MR. SULLY

So what do you do nowadays Mr. President?

BILL CLINTON

Well, I used to be a spokesperson for President Obama, you know, talkin' him up and stuff.

But ever since I made that comment to him, he doesn't seem to like me very much. Even after I apologized! He was all, (Bill Clinton does an Obama impression) "Now, Mr. Clinton, I'm saying this for the last time. Let me be clear. You are not allowed to call us that. Only we are allowed to call ourselves that!" And all because I called him a soup Nazi!

MR. SULLY

Wait, what is the context for this comment?

BILL CLINTON

Well, he was eating a hamburger and I said, "Oh, you soup Nazis love your hamburgers!"

And then he said, "Let me be clear. I do love soups, but I'm not sure that applies here."

MR. SULLY

Oh, I see.

BILL CLINTON

Yep. So now that I'm not a spokesperson for him, I just spend my time visiting people who are crazy high.

MR. SULLY

Wait, so you're really Bill Clinton? I'm not hallucinating?

BILL CLINTON

That's right! But you're starting to come down from your high, so I think I better be going soon. (He shudders and then, eyes wide, stares blankly into the distance.)

MR. SULLY

Is something wrong, Mr. President?

BILL CLINTON

My drug-sense is goin' off. Whenever someone's gettin' crazy high, I feel a disturbance in my drug-sense.

MR. SULLY

Oh. Right. Does it tell you who's doing it?

BILL CLINTON

Only if I concentrate real hard. (Closes eyes and thinks hard) Yep, it's the Toronto Mayor doin' some crack again. I think I'll go join him.

MR. SULLY

Alright, bye Mr. President!

Mr. Sully suddenly becomes drowsy and falls down. He wakes up, and we are back where we were before Clinton showed up. Mike is still fighting with his snake arm.

MIKE

Oh, you finally woke up, Mr. Sully!

MR. SULLY

I guess so. Why didn't you pass out?

MIKE

Oh, I did, but I woke up before you.

MR. SULLY

So you aren't high anymore?

MIKE

Nope

MR. SULLY

Then why are you still fighting your arm?

MIKE

It's a freaky looking arm!

MR. SULLY

Right.

Mr. Sully slaps his face a little to wake himself up, then stands up.

MIKE

Mr. Sully, can I ask you something?

MR. SULLY

Sure, Mike!

MIKE

Well, I feel like we're pretty close after we got high together, and I'd even call you my friend.

So do you think that tomorrow, when you see me in school, that you'll say, "Hi" to me? Or will you just ignore me and walk by like you always do?

MR. SULLY

Well, Mike, I think we're pretty close too. But to be honest, I'm just cooler than you. I can't have my teacher friends thinking that I actually like you!

MIKE (HURT)

Oh. I see. Well, with no satisfying resolution to this story, I think I'll just leave now. Don't you...forget about me, Mr. Sully

Mike walks away and then fist pumps into the air, freezing when his fist is above his head.
```

---

## IC-1049: Nicholas Nickleby

- Title: Nicholas Nickleby
- Author (byline): Charles Dickens
- Work: Not specified
- Publisher: Penguin Group
- Publication date as stated: Dec 2002
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: NICHOLAS, SMIKE, NARRATOR
- Teaser before the introduction: Yes
- Spoken words (computed): 1043
- Already set (do not supply): none

### Source block (context only)

```text
Author: Charles Dickens
ISBN: 0142002755
Publisher: Penguin Group
Date (Month/Year): Dec 2002
```

### Introduction (context only: never use it for content warnings)

```text
NARRATOR: There once lived, in a sequestered part of the county of Devonshire, a mother, and a daughter and a son. Who, recently bereaved were forced to journey up to London. And to throw themselves upon the mercy of their only living relative, Ralph Nickleby. Ralph took Young Nicholas and found him a position in a school in Yorkshire run by Mr. Wackford Squeers, and arriving at the school, he met with the poor drudge Smike.

Nicholas Nickleby by Charles Dickens.
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

NICHOLAS: Hallo. Please, don't be frightened. Are you cold? (Smike shakes his head) You're shivering.

SMIKE: Oh, dear. Oh, dear, oh, dear. My heart. Will break. It will. It will. I know it will.

NICHOLAS: Shh. Shh.

SMIKE: Remember Dorker, do you?

NICHOLAS: Dorker?

SMIKE: I was with him at the end, he asked for me. Who will I ask for? Who?

NICHOLAS: Who will you ask for when?

SMIKE: No One. No Hope. Hope Less.

NICHOLAS: There's always hope.

SMIKE: Is there? O-U-T-C-A-S-T. A noun. Substantive. Person cast out or rejected. Abject. And forsaken. Homeless. Me.

NARRATOR: As the days wore on, Nicholas and Smike became friends.

SMIKE: Can't do it. With the book. Can't do it, with the book, at all.

NICHOLAS: Oh, please. Don't try. Don't For God's sake. I cannot bear it. They are more hard on you, I know. But, please...

SMIKE: Except for you, I die.

NICHOLAS: No, no. You'll be better off, I tell you, when I'm gone.

SMIKE: You gone?

NICHOLAS: Shh. Yes.

SMIKE: You going?

NICHOLAS: I was speaking to my thoughts.

SMIKE: Tell me. Will you? Will you go?

NICHOLAS: I shall be driven to it. yes. To go away.

SMIKE: Please tell me. Is away as bad as here?

NICHOLAS: Oh, no. Oh, no, there's nothing --

SMIKE: Can I meet you there? Away?

NICHOLAS: Well, yes... you can, of course...

SMIKE: Can meet you there? Away? And I would find you in away?

NICHOLAS: You would. And, it you did, I'd try to help you.

SMIKE: To go. Go anywhere. Go everywhere. The world's end. To the churchyard grave. I can. You'll let me. Come away with you. You are my home.

NARRATOR: It was a cold, foggy morning in early Spring, and a few meager shadows flitted to and fro in the misty streets. At intervals were heard the tread of slipshod feet, and the chilly cry of the sweep as he crept shivering to his early toil; the sluggish darkness thickened as the day came on, and those who had the courage to rise and peep at the gloomy street from their curtained windows, crept back to bed again, and coiled themselves up to sleep.

NICHOLAS: Now, listen to me, Smike. We're bound for Portsmouth, because it's a seaport town, and I am thinking we might board some ship. I'm young and active, so are you. Smike, do you have a good memory?

SMIKE: I don't know. I had once, I think. But now all gone.

NICHOLAS: Why do you think you had one once?

SMIKE: Because I could remember, when I was a child.

NICHOLAS: Do you remember, when you went to Yorkshire? What the day was like. The weather, hot or cold?

SMIKE: Wet. Very wet. And afterwards. When it was raining. I could see myself. The day I came.

NICHOLAS: Did you come there alone?

SMIKE: No. No. A man - a dark and withered man, they used to say. And I think I remember, too. Remember - being frightened of him. Glad he went away. But frightened at the place he left me, too.

NICHOLAS: Do you remember anything or anyone or anywhere, before that house in Yorkshire? Think, Smike, think.

SMIKE: A room. I slept once in a room a large and lonesome room, beneath the attic, there was a hook in the ceiling above me. I was frightened of it, covered up my head. Used to dream. Dream terribly about the room. And people in it. Things, that changed. But that room - never changes. Till now, I have not known two days together, when I haven't been afraid.

NARRATOR: At Portsmouth, Nicholas and Smike joined the theatrical troupe of Vincent Crummles and family. The time spent in this company was the happiest they had known. Eventually, however, the two wanderers were re-united with Nicholas' mother and sister. And Smike grew daily weaker. There is a dread disease which so prepares its victim, as it were for death; in which the struggle between soul and body is so gradual, quiet and solemn, that day by day, and grain by grain, the mortal part wastes and withers, and the spirit part grows light and sanguine with its lightening load; a disease which medicine never cured, wealth warded off, or poverty could boast exemption from - which sometimes moves in giant's strides, and sometimes at a tardy, sluggish pace, but slow or quick is ever sure and certain. Nicholas resolved to take Smike to the country for some healthy country air. Dividing the distance into two days' journey, Nicholas and Smike found themselves in the village where Nicholas had grown up.

NICHOLAS: Look, there's our garden, Smike. That's where we used to play, and run, and hide.

SMIKE: You used to hide?

NICHOLAS: Yes, Smike, you know, the game.

SMIKE: Is it the same. As when. Is it the same.

NICHOLAS: Things look a little different, Smike. The tree looks smaller. A the garden has become a little overgrown. But still - it is the same.

NARRATOR: And in a fortnight, Smike became too ill to move about. And he would lie upon an old couch, near the open doors that led into a little orchard. And Nicholas would sit with him and talk for hours and hours together. Till the sun went down, and Smike would fall asleep.

SMIKE: Who calls? So calls so loud? Who calls so loud?

NICHOLAS: Come hither, man. I see that thou art poor. Hold, there is forty ducats. Let me have -

SMIKE: Such mortal drugs I have, but Mantua's law Is - is-

NICHOLAS: Oh, Smike.

SMIKE: Is death to any he that utters them. (Prompting) Art thou so bare?

NICHOLAS: Art thou so bare and full or wretchedness, and fears to die? Famine is in thy cheeks, need and oppression starveth in thy eyes. Contempt and -

SMIKE: No. No, I don't fear to die. My will consents. You know I think, that if I could rise up again, completely well, I wouldn't want to, now. For nothing - can be ill if she be well.

NICHOLAS: Then she is well, and nothing can be ill. Her body sleeps in Capel's monument. But her immortal part with angels lives.

SMIKE: Is it. E'en so? I see a garden. Trees and happy children's faces. And her body sleeps. Light on the faces. Living with the angles. Dreamt my lady came and found me dead. Such happy dreams. I'm going home. Who calls. Who calls so loud?

NICHOLAS: He said - I think you know. And then he said he was in Eden.
```

---

## IC-1050: The Obsolete Man

- Title: The Obsolete Man
- Author (byline): Rod Serling
- Work: The Best of Rod Serling's Twilight Zone Scripts
- Publisher: Gauntlet Press
- Publication date as stated: Nov 2014
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: SECRETARY, NARRATOR, CHANCELLOR, WORDSWORTH
- Teaser before the introduction: Yes
- Spoken words (computed): 2172
- Already set (do not supply): none

### Source block (context only)

```text
Author: Rod Serling
Book: The Best of Rod Serling's Twilight Zone Scripts
ISBN: 978-1934267455
Publisher: Gauntlet Press
Date (Month/Year): Nov 2014
```

### Introduction (context only: never use it for content warnings)

```text
Actor 1: The Obsolete Man by Rod Sterling
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Roles: Actor 1: Secretary, Romney Wordsworth

Actor 2: Narrator, Chancellor

SECRETARY: Wordsworth, Romney, Obsolescence. (A feeble man walks through two large doors. As the two doors close, he is led by a guard to his microphone. His eyes have a look of confusion, awe, and fear as he looks around the word. The Narrator's voice comes over the scene.)

NARRATOR: You walk into this room at your own risk, because it leads to the future; not a future that will be, but one that might be. This is not a new world: It is simply an extension of what began in the old one. It has patterned itself after every dictator who has ever planted the ripping imprint of a boot on the pages of history since the beginning of time. It has refinements, technological advancements, and a more sophisticated approach to the destruction of human freedom. But like every one of the super states that preceded it, it has one iron rule: Logic is an enemy, and truth is a menace. This is Mr. Romney Wordsworth, in his last forty-eight hours on Earth. He's a citizen of the State, but will soon have to be eliminated, because he's built out of flesh and because he has a mind. Mr. Romney Wordsworth, who will draw his last breaths in the Twilight Zone.

CHANCELLOR: Wordsworth, Romney. You've been under investigation, Mr.Wordsworth, for the mandatory period of 1 year and 11 months. You are found to be obsolete. Your occupation, Mr.Wordsworth?

WORDSWORTH: A librarian, sir. . .

CHANCELLOR: (Puzzled and angrily) The field investigators in your sector have classified you as obsolete, this finding carries with it serious implications. Do you understand that, Mr.Wordsworth? (Wordsworth nods) I'd ask you again, your occupation Mr.Wordsworth?

WORDSWORTH: I AM a librarian, that IS my occupation, that is my PROFESSION. If you people choose to call that obsolete . . .

CHANCELLOR: A librarian. Having to do...with books.

WORDSWORTH: (Proudly) Yes sir . . . books!

CHANCELLOR: Since there are no more books, Mr.Wordsworth, there are no more libraries, and, of course, as it follows , there is very little call for the services of a librarian. Case in point: A minister. A minister would tell us that his function is that of preaching the word of God. And since it follows that since The State has proven that there is no God. That would make the function of a minister quite academic as well . . .

WORDSWORTH: There IS a God!! (The Chancellor looks angry)

CHANCELLOR: You are in error, Wordsworth. There is NO GOD! (To the audience) The STATE HAS PROVEN THAT THERE IS NO GOD!!

WORDSWORTH: You cannot erase God, with an edict!

CHANCELLOR: You are obsolete, Mr.Wordsworth!

WORDSWORTH: A lie, no man is obsolete! I am nothing more than a reminder to you that you cannot destroy truth by burning pages!

CHANCELLOR: You're a bug, Mr.Wordsworth. A crawling insect. An ugly, misformed, little creature, that has no purpose here, no meaning!

WORDSWORTH: I am a human being...

CHANCELLOR: You're a librarian, Mr.Wordsworth. You're a dealer in books and two cent finds and pamphlets in closed stacks in the musty finds of a language factory that spews meaningless words on an assembly line. WORDS, Mr.WORDSworth. That have no substance, no dimension, like air, like the wind. Like a vacuum, that you make believe have an existence, by scribbling index numbers on little cards.

WORDSWORTH: I don't care. I tell you: I don't care. I'm a human being, I exist....and if I speak one thought aloud, that thought lives, even after I'm shoveled into my grave.

CHANCELLOR: Delusions, Mr.Wordsworth, DELUSIONS!! That you inject into your veins with printer's ink, the narcotics you call literature: The Bible, poetry, essays, all kinds, all of it are opiate to make you think you have a strength, when you have no strength at all!!! You are nothing, but spindly limbs and a dream, and The State has no use for your kind!!!! (Calming down) You waste our time, Mr.Wordsworth, and you're not worth the waste. Ladies and Gentlemen, how do you find?

SECRETARY: Romney Wordsworth, Step forward. (Wordsworth steps forward) The board finds you obsolete.

CHANCELLOR: Your rights are as followed, Mr.Wordsworth, you are to be liquidated within a period of 48 hours, but you have an option as to method and precise time. There are several prescribed methods, Mr.Wordsworth: pills, gas, electrocution...and it can be done immediately, or an hour from now, or any specific time you request.

WORDSWORTH: I choose the following: to be given an assassin to whom I shall tell the method of my execution . . .

CHANCELLOR: That would be acceptable Mr. Wordsworth, provided that you are eliminated within the 48 hour period.

WORDSWORTH: Oh, yes...and one final request . . . I should like to die . . . with an audience.

CHANCELLOR: Ahhh, Mr.Wordsworth (looking gleeful) that can be arranged indeed. It is not unusual that we televise executions, it has an educative effect on the population.

WORDSWORTH: I have no doubt . . .

CHANCELLOR: Now as to the time of the liquidation, Mr.Wordsworth?

WORDSWORTH: Midnight. . . In my room . . .

CHANCELLOR: Agreed, Mr.Wordsworth. We will choose your liquidator and send him over to you. He will be duty bound not to divulge the method you have decided upon. That will be all Mr.Wordsworth. You may leave and return to your room. (The Doors open back up as Wordsworth walks out.) We will show the people how this . . . obsolete man . . . this librarian . . . dies . . . **************************** Setting: Wordsworth's apartment. A knock is heard on his door and Wordsworth proceeds to open it. Revealing the Chancellor standing in the doorway, smiling . . .

WORDSWORTH: Come in Chancellor. (Chancellor steps in and Wordsworth locks the door as The Chancellor stares into the room of books and pamphlets that he so hates) Thank you for coming . . .

CHANCELLOR: Very irregular, Mr.Wordsworth. You know why I've come, do you?

WORDSWORTH: Well, I invited you.

CHANCELLOR: Well, of course you invited me, but why would I honor such an invitation, a cryptic note sent by a condemned man asking me to visit him in the last hours of his life. Hardly the norm, Mr.Wordsworth. Hardly what I'm accustomed to .

. . and somewhat suspect too . . . how do I know I wasn't invited for that pitiful gesture of vengeance on the part of the condemned . . .

WORDSWORTH: Vengeance . . . ?

CHANCELLOR: Yes . . . I'm somewhat responsible for the finding in your case. Your . . . demise in less than an hour can attributed to my decision.(Pause) I'll tell you why I came here. To prove to you that The State has no fears, none whatsoever . . .

WORDSWORTH: (laughing) Forgive me Chancellor, that has the elements of a joke . . . I mean you come to MY room to prove that The State . . . isn't afraid of me!? Why what an incredible burden I must be! For The State to have to prove that isn't afraid of an obsolete librarian like myself. No, I'll tell you the reason you came...I tell you the reason even though you won't admit it to yourself. . . I don't fit your formuli. Your state has everything categorized . . . indexed, TAGGED. People like you are the strength, people like me are the weakness. You control order and dictate and my kind . . . merely follow and obey. But something has gone wrong hasn't it? I don't fit, do I?

CHANCELLOR: Yes, you fit, Mr.Wordsworth! Indeed, you fit! In a few minutes, you'll be cringing and pleading just like they all do! You have a worthless meaningless little life, but you also have an instinct for survival. And in a few minutes when you feel life slipping away. When you feel that your survival is just a question of minutes, we'll see then which is stronger, Mr.Wordsworth, The State or the librarian! (pause) I take it you've had a talk with whoever has assigned your liquidation.

WORDSWORTH: Yes, you see they brought this equipment here earlier this afternoon . . .

(A TV Camera is shown built into the wall with two large lights built next to it) It's remote control, very efficient. (The Camera and lights click on) Why, we're being televised now.

CHANCELLOR: It's not unusual that we televise executions, Mr.Wordsworth . . . last year in the mass executions, we televised around the clock. (Proudly to the cameras) Thirteen hundred people were put to death in less than six hours.

WORDSWORTH: You never learn do you? History teaches you nothing!

CHANCELLOR: On the contrary. History teaches us a great deal. We had predecessors, Mr.Wordsworth, that had the beginnings of the right idea . . .

WORDSWORTH: Ah, yes, Hitler!

CHANCELLOR: Yes, Hitler. Stalin, too. But their error was not one of excess it was simply not going far enough! Too many undesirables left around and undesirables eventually create a corp of resistance. Old people for example, clutch at the past and won't accept the new. The sick, the maimed, the deformed, they fasten onto the healthy body and damage it. So WE eliminate them! And people like yourself, they can perform no useful function for The State, so . . . we put an end to them. (walks around, sarcastically admiring the decor around him) You aren't facing the camera, Mr.Wordsworth. You're cheating your audience. They'll want to see how you die. Please, face the camera, Mr.Wordsworth. (Wordsworth looks at the cameras with a sly grin on his face, The Chancellor kneels next to him, rubbing his hands together hoping to break Wordsworth but he keeps his sly look) That's right, and don't stifle your emotions, if you feel like crying, go ahead and cry, and if you feel like pleading, by all means plead. Some high State official might take pity on you.

WORDSWORTH: Yes, that would please you wouldn't it? A little abject hand wringing, chest pounded, falling down on my hands and knees . . .

CHANCELLOR: Suit yourself, Mr.Wordsworth. Unfortunately, I won't be able to be entertained by them when they do come. I have another appointment this evening. (Chancellor heads toward the door)

WORDSWORTH: Chancellor . . . You have plenty of time. You're not going anywhere! (Stops and turns around) I'm afraid I haven't been very fair with you. I invited you here for a very special reason. Would you like to know the method I have chosen for my liquidation? Well, in a few moments, here in this room a bomb is going off. (Chancellor tries to open the door and finds that it is locked)

CHANCELLOR: What kind of idiocy is this, Mr.Wordsworth? You've locked the door.

(Chancellor is now scared)

WORDSWORTH: Oh yes, yes, I've locked the door . . . now question (turns to cameras to address the question at the nation-wide audience): How does a man react to the knowledge that he's going to be blown to bits in a half an hour? Answer: (turning back to Chancellor) that depends on the individual. As for me, I'm going to sit down (heads towards safe in his room and pulls a grubby, old, Bible,) and read my Bible. (Wordsworth clutches his Bible like a lost treasure. The Chancellor is slowly moving towards him as if unsure how it would look in front of the cameras to force him to open the door and then stops) It's been hidden here for over twenty years, it's a crime punishable by death, so it's only thing I have that has any value at all to me . . . So I'm just going to read it . . . until the moment of my death. How will you spend your last moments, Chancellor.

CHANCELLOR: (Trying to hide his fear) This is insane Wordsworth let me out of here! (Heads to door and tries to open it) Let me out of here, guards, someone!

WORDSWORTH: You're cheating the audience. You aren't facing the camera . . . and there's no sense in raising your voice. There's nobody there, that's one of the rules you made up yourself. Isolate the person to be liquidated. That's what you said! . . . so why don't you face the camera. It's important, you said so yourself. (Chancellor begins to break, hands rubbing together, but hides it from the camera's broadcast. But then turns around)

CHANCELLOR: I'm beginning to understand, Wordsworth, shoe on the other foot, that's the idea. It's one thing for somebody like yourself, to do a little cringing and pleading, but what a choice opportunity to show a member of The State doing likewise. But you're insane, Wordsworth, if you think they'll let me stay here!

WORDSWORTH: They? Ah, you mean The State! Oh, I think they'll sit on their hands for a while. They wouldn't want to miss this scene. Besides the act of rescue would be very demeaning to them, to have to break in here and rescue a high ranking member of The State, to snatch him out of the soup, so to speak. Oh, I think "They" won't help you. . . You underestimated me. You wanted to the whole world, to see the way a librarian dies. Well, let them see, how an official of The State dies too. Face the camera, step into the light! (The Chancellor, obeys knowing he must not prove himself to be a coward, but the fear is still evident in his glare at Wordsworth) (to the camera) So here you have this strong, handsome, uniformed, bemedaled symbol of giant authority and this little, insignificant, librarian . . . and suddenly in the eyes of God . . . there is precious little to distinguish us . . . (The Chancellor looks toward the door as if expecting to be rescued.)

CHANCELLOR: We shall see, Wordsworth, we shall see . . . (He faces the cameras)

(Wordsworth calmly reads passages from various books of the Bible with no fear on his face, the camera's broadcasting every word and image.)

WORDSWORTH: The lord is my shepherd I shall not want. He maketh me to lie down in green pastures. He leadeth me beside the still waters. He restoreth my soul . . . By rod and by staff they come for me. Thou preparest a table before me in front of mine enemies. Thou annointest my head with oil. My cup runneth over. Surely, goodness and mercy shall follow me all the days of my life . . . (Tears are swelling up in the Chancellor’s eyes and he weeps out of fear. Wordsworth is still calmly reading to him as he breaks) Out of the depths, have I called unto thee, O Lord. Lord hear my voice. Let thine ears be attended to the voice of my suffocations

CHANCELLOR: Please, PLEASE,let me out . . . in the name of God . . . LET ME OUT!!! (Runs to the door, pulling it) LET ME OUT, LET ME OUT!!! LET ME OUT!!!

WORDSWORTH: Yes, Chancellor, in the name of God, I will let you out!

(Wordsworth gives him the key) (The Chancellor unlocks the door and runs and hides on the edge of the stairs, in cowardly fear. Wordsworth, in his room, sighs and closes his eyes and accepts his fate as the camera broadcasts the explosion across the country as it sets off, killing Wordsworth instantly. The Chancellor walks away in tears of fear.)

**************** Setting: The Board Room - (The Chancellor, now all clean walks into the board room only to stop in shock at seeing his secretary dressed as he is in his podium, in the chancellor's garments. Below him at the foot of the podium is another secretary.)

SECRETARY: Stand right where you are! No further! You have been removed from office, the field investigators have declared you obsolete.

CHANCELLOR: Obsolete!?

SECRETARY: You have disgraced The State. You have proven yourself a coward. You have therefore, no function . . . you are OBSOLETE!

CHANCELLOR: But I'm not . . . I'm NOT obsolete.

SECRETARY: You are obsolete!

CHANCELLOR: You're making a terrible mistake. A tragic mistake. I'm not obsolete!! I glory The State, I carry the State, I give The State strength! How can you call me obsolete! HOW CAN YOU!!! Please . . . I'm not obsolete . . . (whimpering) Please .. I have a function, I have a purpose (begins to gently weep) NOOOOO!!! PLEASE, I'M NOT OBSOLETE!!!!! NOOO!!!!!

NARRATOR: The chancellor, the late chancellor, was only partly correct. He was obsolete, but so is the State, the entity he worshiped. Any state, any entity, any ideology that fails to recognize the worth, the dignity, the rights of man, that state is obsolete. A case to be filed under "M" for mankind—in the Twilight Zone.
```

---

## IC-1051: Only Kidding!

- Title: Only Kidding!
- Author (byline): Jim Geoghan
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: 1990
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: TOM, JERRY
- Teaser before the introduction: No
- Spoken words (computed): 1295
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jim Geoghan
ISBN: 978-0573691942
Publisher: Samuel French, Inc.
Date (Month/Year): 1990
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: The old-school world of stand-up saw its fair share of successful comedy duos.

ACTOR 2: The formula sounds simple: one comic plays the straight man, setting up big laughs for the other.

ACTOR 1: But a winning comedy duo requires great chemistry, exceptional writing, and even the ability to adlib.

ACTOR 2: Meet Tom and Jerry

ACTOR 1: (No pun intended)

ACTOR 2: an aspiring young comedy team – eager to “make it big” in the world - but also struggling to find themselves.

ACTOR 1: The pressure to always be “on” can get to the best of us –

ACTOR 2: And when comedy becomes bitter, it’s more than . . . .

TOGETHER: Only Kidding! By Jim Goeghan.
```

### Performance text (classify this)

```text
TOM: Good show.

JERRY: Good? It was terrific!

TOM: You see the guy in the front row? How hard he laughed?

JERRY: The Fat guy?

TOM: Yeah, him.

JERRY: The bartender loved the show, too. Watched every bit we did.

TOM: He had such a good time he forgot to steal from the cash register. You messed up though.

JERRY: What do you mean I messed up

TOM: You dropped some lines. A whole section.

JERRY: Hey, we’re a team, remember? We don’t mess up individually. If something goes wrong, it’s because of us. Together.

TOM: Okay, so “we” messed up tonight.

JERRY: That’s it.

TOM: Because you dropped some lines.

JERRY: Cute. (In a very effeminate voice) Yes, this is Jerry Goldstein.

TOM: What are you doing?

JERRY: Calling my answering service. You talk like [this], they don’t put you on hold. Hmmm? She did? When did that come in? (PAUSE) Oh, Fabulous! Ciao.

TOM: Jerry, do you realize we haven’t done a new bit in over eight months?

JERRY: Bull. We do new stuff all the time.

TOM: Bits and pieces. A line here, a line there. Hunks. Hunks. I want to do new hunks.

JERRY: Why’s it so important?

TOM: Because I am bored to death with our old stuff. I’m daydreaming on stage. . . Did you say you got another commercial?

JERRY: Yeah. Yippie Dog Food. It’s a national, too. I film it next week. Guess who the director is?

TOM: No idea.

JERRY: Sam Peckinpaw. Get it? Paw . . . Peckin-paw.

TOM: I got it.

JERRY: This dog won’t eat the dog food. . . . So I shoot ‘im.

TOM: Kids oughta love it.

JERRY: It’s great. It’s in slow motion and everything. C’mon, man. Lighten up. We did a good show tonight. Now it’s time to cruise the bar for chicks. Bring them down here into our deluxe dressing room.

TOM: Yeah, sure. Don’t start that again.

JERRY: Hey, you never know, man, you never know.

TOM: Jerry, how long have you been a comedian?

JERRY: As long as we’ve been together. Five years.

TOM: And in those five years, how many times have you gotten a girl as a direct result of your being a comedian?

JERRY: As a direct result?

TOM: Direct, indirect, whatever.

JERRY: (Thinks) Approximately . . . . none.

TOM: I keep telling you that we’re comedians . . . rock stars get all the girls! (They look at each other for a beat, then break into an improvisational jazz riff – Tom playing bass, Jerry guitar. When they are done they laugh)

JERRY: Still there’s hope that out there in this world there’s a young and beautiful girl with a very low IQ and equally low self-esteem . . . looking to get back at her parents in her own peculiar way . . .

TOM: That’s a beautiful dream, Jer.

JERRY: I know. I’m a hopeless romantic

TOM: You’re crazy, man! You know that?!

JERRY: Think I’ll stay up all night tonight

TOM: Like you’ve got a choice.

JERRY: Couldn’t sleep if I wanted to. I’ve got a nine a.m. audition tomorrow. I’m gonna nail that one too. You just watch.

TOM: Why do you bother with that Jerry?

JERRY: Why? For the money, that’s why. It’s going to help overcome the three things I’ve go going against me. I’m poor, ugly and Jewish.

TOM: You make it sound like it’s some sort of disease or something. Like . . . (as a solemn doctor). I’m sorry, sir. Your test results are I and I’m afraid you are suffering from Poor, ugly, Jewish.

JERRY: (As an old Jewish man) Ach! Doctor, is there any cure?

TOM: Money . . . big piles of money.

JERRY: Ach! Never say big piles to an old Jew!

TOM: Sir, about my bill. If you’re poor, how are you going to pay me?

JERRY: Oh, great! Now my hearing’s shot, too!

TOM: My bill, sir.

JERRY: Can’t hear a thing.

TOM: You owe me . . .

JERRY: Deaf like a stone. Hello?

TOM: Hello.

JERRY: Hello

(Tom segues his Hello into an impression Jerry Lewis emceeing a telethon)

TOM: Hello! And welcome to the seventeenth hour of our telethon coming to you from our studio of love in Los Angeles.

JERRY: It’s lovely here. We come every year.

TOM: With us now is this year’s poster child for poor, ugly, Jewish . . . Mister Jerry Goldstein.

JERRY: Hello!

TOM: Jerry is ugly.

JERRY: It hasn’t been a good year.

TOM: Boy, is he ugly. . . Real ugly.

JERRY: All right, already.

TOM: He’s so ugly the mice walk hunchback.

JERRY: Enough with the ugly!

TOM: But someday with the help . . .

JERRY: Thank you, McDonalds Corporation!

TOM: Jerry will be rich, handsome and Gentile.

JERRY: Think so?

TOM: It could happen.

JERRY: It would take a miracle.

TOM: (Singing) Walk on, walk on with hope in your heart and you’ll never walk alone! You’ll never walk alone!

(A strange force seems to take Jerry over. His Yiddish accent disappears, he rises to his feet and feels his body tingle as Tom sings)

JERRY: What’s going on? I feel the power . . . Oh, my God! I’m breaking out in argyle!! Quick! Someone get me a pipe! (As Ward Cleaver) June! Wally! Beaver! I’m home. Come on. Let’s hop in the Volvo and drive back to Connecticut. These kids! Where do they get the energy? Meanwhile, we’ll try and figure out what I do for a living. Oh, what the heck. Let’s buy retail! (Tom and Jerry laugh from the fun they’ve had and Tom jots down some notes as Jerry watches) Volvo . . . Hop in the Volvo . . .

TOM: I got it . . I got it. Remember when you were a kid . . . the way you would insult each other’s mother? Like your mother’s so low she could play handball against a curb.

JERRY: Right, right, or your mother wears combat boots.

TOM: Or, uh . . Your mother eats . . . Dirt!

JERRY: Oh, oh! I got it, two kids in England and insulting each other’s mother. O.K.? Two kids in England, I say!

TOM: Yes?

JERRY:: Your mother is . . . . . inappropriate.

TOM: How dare you. You take that back.

JERRY: I shan’t.

TOM: You shan’t?? You shan’t because your mother . . .

JERRY: Yes?

TOM: Your mother is . . . Ostentatious.

JERRY: You despicable lout!

TOM: Watch your mouth, dear boy.

JERRY: You’re dashing for a thrashing.

TOM: I shall be forced to give you the finger.

JERRY: You leave no choice but to respond in the like kind.

TOM: Very well . . . the finger.

JERRY: The finger.

(Back to original characters).

JERRY: You know what? We’re too damn good for toilets like this. Look at this dump, and we’re working for chump change. . . . I’ve been thinking. We ought to sign that contract. With Sal as our agent. He says he can get us on Letterman.

TOM: Signing a management contract with Sal could be the worst mistake of our entire lives.

JERRY: Tom, Sal’s got us our shot. All we have to so is sign.

TOM: All we have to do is NOT sign . . . keep doing good shows, get better and better as an act. We’ll get on the Letterman show without getting involved with Sal. It’s not worth it, Jerry. This contract’s for seven years. Seven years, Jerry.

JERRY: Seven’s my luck number!

TOM: Sal wants thirty percent before an agent takes his ten. He wants to put in lounges . . . Lounges! Opening for guys who sing “feelings” and play the accordion.

JERRY: You don’t know the way my gut aches to get on Letterman. Another young comedian, and another young comedian . . . but never us! Me! Twenty million people! The ones who tormented and teased and humiliated me . . . the ones who stole my lunch money . . . the creeps who called me Jewboy! I want to do it . . Now!

TOM: The price is too high.

JERRY: I want you to sign this and I want you to sign this right now.

TOM: Who are you? Have we met? You look a lot like my partner . . . No way!

JERRY: Your last chance. Sign it or else.

TOM: Is being pathetic an Olympic sport yet? If it is, you should try out for the team.

JERRY: Get out.

TOM: What?

JERRY: I said get out of here! Get out of my dressing room!

TOM: You’re crazy.

JERRY: We’re through. I’m sick and tired of you holding me back. We’re through! Get out of here.

TOM: What are you doing? Stop!

JERRY: Do this to me? Do a thing like this to me?!! Who do you think you are? You are no one! I hate your fricking guts!!! (Tom slaps Jerry hard across the face and it stops Jerry cold)

TOM: What are you, crazy? Who sat up with you in Atlanta when you thought you were going to die? Who? Remember a hundred and five fever? Who stayed up with you for two days and nights? Was it David Letterman? Was it Sal? Who was it?! Are you in there? Are you in there somewhere? (Tom waits for a reply. There is none. After several beats, he let’s go of Jerry. Jerry gathers himself.)

JERRY: I’m going to send you a color TV, Kelly. A great big one. You can watch me kill on Letterman. Alone. Without you.

TOM: Yeah, sure . . . You do that. Looks like you’ve got everything you need. (Tom surveys Jerry for a few beats, then sadly exits.)
```

---

## IC-1052: The Philadelphia

- Title: The Philadelphia
- Author (byline): David Ives
- Work: Take Ten: New 10-Min Plays (ed Lane & Shengold)
- Publisher: Vintage Books
- Publication date as stated: March 1997
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MARK, AL
- Teaser before the introduction: Yes
- Spoken words (computed): 1329
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Ives
Book: Take Ten: New 10-Min Plays (ed Lane & Shengold)
ISBN: 978-0679772828
Publisher: Vintage Books
Date (Month/Year): March 1997
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1 (Al): Two guys meet in a diner in New York

ACTOR 2 (Mark): (Groucho Marx impersonation – cigar, eyebrows, the works) “And the first guy says . . . “

ACTOR 1: Very funny . . . Now be serious. Two guys meet in a diner in New York, but they're both in very different states of mind.

ACTOR 2: See, Al is in a Los Angeles state of mind. Nothing can faze him . . . even if it did he would just make it a Hollywood movie. (Background music provided by Actor 1)

ACTOR 1: Then there's Mark who finds the whole world is against him. He can't get a newspaper at the newsstand, aspirin at the drugstore, and the diner gives him a Cheesesteak when he wants a burger. That's right. Mark's trapped in a Philadelphia state of mind. (Background music provided by Actor 2 - perhaps the Twilight Zone theme)

ACTOR 2: (Groucho Marx impersonation) It could be worse. You could be stuck in a Cleveland. It's like death without the advantages.

ACTOR 1: The Philadelphia by David Ives
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

A diner in New York . . . (AL is at the restaurant table MARK enters, looking shaken and bedraggled.)

MARK: Al!

AL: Hey there, Marcus. What's up?

MARK: Jesus! Oh man. . . !

AL: What's the matter? Sit down.

MARK: I don't get it, Al. I don't understand it.

AL: You want something? Want a drink? I'll call the waitress

MARK: (Desperate.) No! No! Don't even try. (Gets a breath.) I don't know what's going on today, Al. It's really weird. Right from the time I got up.

AL: What is it? What's the story?

MARK: Well-just for an example. This morning I stopped off at a drugstore to buy some aspirin. This is at a big drugstore, right? I go up to the counter, the guy says what can I do for you, I say, Give me a bottle of aspirin. The guy gives me this funny look and he says, "Oh we don't have that, sir." I said to him, You're a drugstore and you don't have any aspirin?

AL: Did they have Bufferin?

MARK: Yeah!

AL: Advil?

MARK: Yeah!

AL: Extra-strength Tylenol?

MARK: Yeah!

AL: But no aspirin.

MARK: No! And that's the kind of weird thing that's been happening all day. It's like, I go to a newsstand to buy the Daily News, the guy never even heard of it.

AL: Could've been a misunderstanding.

MARK: I asked everyplace-nobody had the News! I had to read the Toronto Hairdresser. Or this. I go into a deli at lunch time to buy a sandwich, the guy tells me they don't have any pastrami. How can they be a deli if they don't have pastrami?

AL: Was this a Korean deli?

MARK: This was a kosher from Jerusalem deli. "Oh we don't carry that, sir," he says to me. "Have some tongue." . . . . I just got into a cab, the guy says he doesn't go to 56th Street! He offers to take me to Newark instead! Looking at me like I'm an alien or something!

AL: Mark. Settle down.

MARK: "Oh I don't go there, sir."

AL: Settle down. Take a breath.

MARK: Do you know what this is?

AL: Sure.

MARK: What is it? What's happening to me?

AL: Don't panic. You're in a Philadelphia.

MARK: I'm in a what?

AL: You're in a Philadelphia. That's all.

MARK: But I'm in . . .

AL: Yes, physically you are in New York. But metaphysically you are in a Philadelphia. You see, inside of what we know as reality there are these pockets, these black holes called Philadelphias. If you fall into one, you run up against exactly the kinda *stuff* that's been happening to you all day.

MARK: Why?

AL: Because in a Philadelphia, no matter what you ask for, you can't get it. You ask for something, they're not gonna have it. You want to do something, it ain't gonna get done. You want to go somewhere, you can't get there from here.

MARK: Good God. So this is very serious.

AL: Just remember, Marcus. This is a condition named for the town that invented the cheese steak. Something that nobody in his right mind would willingly ask for.

MARK: And I thought I was just having a very bad day . . .

AL: Sure. Millions of people have spent entire lifetimes inside a Philadelphia and never even knew it. Look at the city of Philadelphia itself. Hopelessly trapped forever inside a Philadelphia. And do they know it?

MARK: Well what can I do? Should I just kill myself now and get it over with?

AL: You try to kill yourself in a Philadelphia, you're only gonna get hurt, babe.

MARK: SO what do I do?

AL: Best thing you can do is wait it out. Someday the great cosmic train will whisk you outa the City of Brotherly Love and off to someplace happier.

MARK: You're pretty mellow today.

AL: Yeah well. Everybody has to be someplace. (WAITRESS enters.)

WAITRESS (Played by Actor 2): Is your name Allen Chase?

AL: It is indeed.

WAITRESS (Played by Actor 2):There was a phone call for you. Your boss? He says you're fired.

AL: Cool! Thanks. (WAITRESS exits.) So anyway, you have this problem. . .

MARK: Did she just say you got fired?

AL: Yeah. I wonder what happened to my pigs' feet. . .

MARK: Al!? You loved your job! How can you be so calm?

AL: Easy. You're in a Philadelphia? I woke up in a Los Angeles. And life is beautiful! You know Susie packed up and left me this morning.

MARK: Susie left you?

AL: And frankly, Scarlett, I don't give a ****. I say, go and God bless and may your dating pool be Olympic-sized.

MARK: But your job? The garment district is your life!

AL: So I'll turn it into a movie script and sell it to Paramount. Toss in some sex, add a little emotional blah-blah-blah, pitch it to Jack and Dusty, you got a buddy movie with a garment background. Not relevant enough? We'll throw in the hole in the ozone, make it E.C.

MARK: E.C.?

AL: Environmentally correct. Have you heard about this hole in the ozone?

MARK: Sure.

AL: Marcus, I love this concept. I embrace this ozone. Sure, some people are gonna get hurt in the process, meantime everybody else'll tan a little faster.

MARK: (Quiet horror.) So this is a Los Angeles. . .

AL: Well. Everybody has to be someplace.

MARK: Wow . . .

AL: You want my advice? Enjoy your Philadelphia. Sit back and order yourself a beer and a burger and chill out for a while.

MARK: But I can't order anything. Life is great for you out there on your cosmic beach, but whatever I ask for, I'll get a cheese steak or something . . .

AL: No. There's a very simple rule of thumb in a Philadelphia. Ask for the opposite.

MARK: What?

AL: If you can't get what you ask for, ask for the opposite and you'll get what you want. You want the Daily News, ask for the Times. You want pastrami, ask for tongue. So. Would you like a Bud?

MARK: I sure could use a . . .

AL: No. Stop. (very deliberately.) Do you want. . . a Bud?

MARK: (Also deliberately.) No. I don't want a Bud. (WAITRESS enters and goes to the specials board.)

AL: Good. Now there's the waitress. Order yourself a Bud and a burger. But do not ask for a Bud and a burger.

MARK: Waitress!

AL: Don't call her. She won't come. You're in a Philadelphia, so just figure, who needs her.

MARK: Who needs her.

AL: You don't need that waitress.

MARK: Hey, waitress! DROP DEAD! (WAITRESS turns to him.)

WAITRESS (Played by Actor 1): Can I help you, sir?

MARK: Uh-no thanks.

WAITRESS (Played by Actor 1): Okay, what'll you have? (Takes out her pad.)

MARK: Well-how about some O.J.

WAITRESS (Played by Actor 1): Sorry. Squeezer's broken.

MARK: A glass of milk?

WAITRESS (Played by Actor 1): Cow's dry.

MARK: Cuppa coffee?

WAITRESS (Played by Actor 1): Oh we don't have that, sir. (The WAITRESS has spoken the magic words.)

MARK: That's too bad. (exchanges a look and nod with the audience) How about a Heineken?

WAITRESS (Played by Actor 1): Heineken? Try again.

MARK: Bud Lite?

WAITRESS (Played by Actor 1): Just plain Bud is all we got.

MARK: No thanks.

WAITRESS (Played by Actor 1): (Calls.) Gimme a Bud! (to MARK) Anything to eat?

MARK: Pork chops.

WAITRESS (Played by Actor 1): (Writes down.) Hamburger. . .

MARK: Medium.

WAITRESS (Played by Actor 1): Well done. . .

MARK: Baked potato.

WAITRESS (Played by Actor 1): Fries . . . (Exits, calling.) Burn one!

AL: Excellent. You sure you've never done this before?

MARK: I've spent so much of my life asking for the wrong thing without knowing it, doing it on purpose comes easy. I could've saved myself a lot of trouble if I'd screwed up on purpose all those years. Maybe I was in a Philadelphia all along and never knew it!

AL: You might've been in a Baltimore. They're practically the same. (WAITRESS enters, with a glass of beer and a plate.)

WAITRESS (Played by Actor 2): Okay. Here's your Bud. (Sets that in front of MARK.) And one cheese steak. (She sets that in front of AL, and starts to go.)

AL: Excuse me. Hey. Wait a minute. What is that?

WAITRESS (Played by Actor 2): It's a cheese steak.

AL: No. I ordered cream of kidney.

WAITRESS (Played by Actor 2): Oh we don't have that, sir.

AL: I beg your pardon? (to MARK.) You son of a bitch! I'm in your Philadelphia!

MARK: I'm sorry, Al. I didn't know it was contagious.

AL: Oh God, please don't let me be in a Philadelphia! Don't let me be in a Philadelphia!

MARK: But maybe you're not really in a Philadelphia!

AL: Do you see the cheese on that steak? What do I need for proof? The Liberty Bell? Waitress, bring me a glass of water.

WAITRESS (Played by Actor 2): Water? Don't have that, sir.

AL: (to MARK) "We don't have water"-? What, you think we're in a sudden drought or something? (Suddenly realizes) Holy ****, I just lost my job. . . ! Susie left me! I gotta make some phone calls! (to WAITRESS) 'Scuse me, where's the pay phone?

WAITRESS (Played by Actor 2): Sorry, we don't have a pay phone

AL: Of course you don't have a pay phone, of course you don't! Oh *****, let me outa here! (Exits.)

MARK: I don't know. It's not that bad in a Philadelphia.
```

---

## IC-1053: The Physician

- Title: The Physician
- Author (byline): John Patrick
- Work: The Doctor Will See You Now
- Publisher: Dramatists Play Service
- Publication date as stated: Jan 1998
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: NURSE, DOCTOR, PATIENT
- Teaser before the introduction: Yes
- Spoken words (computed): 1296
- Already set (do not supply): none

### Source block (context only)

```text
Author: John Patrick
Book: The Doctor Will See You Now
ISBN: 978-0822203179
Publisher: Dramatists Play Service
Date (Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Do you have complete confidence in your doctor?

ACTOR 2: Me? I don’t believe in doctors and more than I believe in Santa Claus!

ACTOR 1: Really? Doctors are the backbone of our medical system. What if you got really, really sick?

ACTOR 2: Nope . . . when it’s my time to go, it’s my time to go. Ever since I went to Doctor Craven that one time for a simple sore throat . . . I’ve vowed that I would never go back to a doctor again! Let me tell you about it . . . no, wait – I’ll show you exactly what happened!

TOGETHER: The Physician by John Patrick.

AT RISE: Doctor Craven, an attractive, but very jittery physician in his thirties, is discovered meditating on the floor in front of his desk squatting in the traditional "lotus” position. His affable nurse enters.

DOCTOR: (Without opening his eyes.) Ssshl (His nurse sighs and stands waiting patiently.

After a moment she speaks.)
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

NOTE: Actor 2 plays the roles of the NURSE and the PATIENT; Actor 1 Plays the role of the DOCTOR.

NURSE: Doctor -

DOCTOR: Sssshl (His Nurse leans back against the door to wait. The Doctor begins to hum a chant, sounding somewhat like a Hindu Cantor. Then with a satisfied smile, he opens his eyes, and takes a deep breath.) Wait! Damn! (He struggles to get his legs unfolded.)

NURSE: What's the matter? Can't you get out of your lotus position?

DOCTOR: (Alarmed.) Nol It's my cranial nerves. I think I'm paralyzed.

NURSE: Oh, come on now, Doctor. You’re just stuck. (Crosses to him.)

DOCTOR: Don’t argue with me. Can’t you see I’ve just suffered a motor impairment. I knew something was wrong with me this morning when I threw up my yogurt.

NURSE: You haven’t had a stroke. You’ve just got a cramp. Here, let me help unwind you. (She kneels and pulls his legs apart) There. (Rises and offers her hand to get him to his feet).

DOCTOR: No. Don’t get close to me. You’ve got a cold.

NURSE: I have not got a cold!

DOCTOR: I heard you sneezing out there, twice. Doctors are exposed to every disease known to man and beast . . . And some pigeons. If I were an insurance company, I wouldn’t insure a doctor for ten cents. (Stops.) Incidentally, is my policy paid up?

NURSE: Would you like to increase it? There was a pigeon on the window sill yesterday.

DOCTOR: Wait’ll I have a few more symptoms. I’m a doctor and I know I’m a very sick doctor.

NURSE: What do you think is the matter with you?

DOCTOR: I don’t know. People are dying every day from diseases we haven’t discovered yet.

NURSE: Maybe you should see a doctor, Doctor.

DOCTOR: I might have caught something they’ve never heard of.

NURSE: Doctor, this is becoming an obsession. I don’t know what is happening to you. I think you ought to see a psychiatrist. They cure people of all sorts of things.

DOCTOR: Well, I never heard of analysis curing a hemorrhoid.

NURSE: I think your trouble is a little higher up, Doctor. Frankly, in my opinion, you’re becoming a paranoid hypochondriac.

DOCTOR: Me? A hypochondriac? You’re fired!

NURSE: After fifteen years?

DOCTOR: I can’t afford the tension you cause me in my present physical condition. Write yourself two weeks severance pay.

NURSE: Oh, this is preposterous! Shall I send in your first patient now. He's been waiting an hour.

DOCTOR: Let him wait. That'll teach him to get sick. Taking up my time. I'll buzz you after I've taken my temperature. And a few pills. (She goes out.)

DOCTOR: (To self.) Hypochondriac, indeed! (He goes to a wall mirror and sticks out his tongue to examine. Next he pulls his eyelid down. He then goes to a basin and washes his hands. Having done this, he gargles three times, each on a progressively higher musical note. He concludes his self-examination by spraying his throat. To self.) Hypochondriac! Women - what do they know. (He then takes an aerosol can and sprays the room, even spraying under a book. He sits down at his and puts a thermometer in his mouth.)

NURSE: (sticking her head in the doorway) Are you ready for your first patient now?

DOCTOR: (With the thermometer in his mouth, his words are almost indistinguishable.) No, but I might as well start. (Removes thermometer.) Send him in. (Returns thermometer to his mouth as she exits, then takes it out to read. To self.) Normal? Damned unreliable thermometer. Probably made in Mexico. (He opens a bottle of pills and begins popping them into his mouth, one after the other - a dozen at least. His nurse returns and stands aside.)

NURSE: The doctor will see you now. (A pleasant-looking man enters expectantly and takes off his hat.)

DOCTOR: Come in. Sit down, sir. (His patient starts to shift the chair closer to the desk.) Don't move it closer!

PATIENT: Why not?

DOCTOR: Germs. Germs are air-borne and we're air-conditioned. Now, what seems to be wrong with you?

PATIENT: That's what I want you to tell me. Actually, Doctor, all I really have is a slightly inflamed throat. I just dropped in to get a prescription.

DOCTOR: How do you know it's just a sore throat? Optimism has caused more deaths than the tsetse fly.

PATIENT: Well, I haven't exactly been bothered this winter by flies.

DOCTOR: We'd better have a look. God knows what we'll find. (He first sprays the area around the Patient with his aerosol.)

PATIENT: What's that - a tsetse fly spray?

DOCTOR: This whole world is divided into two hostile armies - people and germs.

PATIENT: Who's winning?

DOCTOR: You and I - so far. Now, it's safe to open your mouth and stick out your tongue.

PATIENT: How far?

DOCTOR: Whole hog. (The Patient sticks out his tongue.) My God - your tongue is bluel Sit down quickly. You're riddled with Blue Fungus.

PATIENT: Not to worry, Doctor. I had blueberry muffins for breakfast.

DOCTOR: Don't do that to me! I'm not well. Now, I have to take a tranquilizer because of you. (He gets a pill and swallows it.)

DOCTOR: Well, let's look at your tongue again. (Patient slides out tongue.) Hmmmm. Remarkable. . . . The only time I've ever seen a tongue as long as yours was on an iguana.

PATIENT: But am I going to live?

DOCTOR: Your tongue does seem a little swollen.

PATIENT: What could cause that?

DOCTOR: I thought you'd never ask. It could be a fungus of the mucus membrane or infectious mononeucleosis. On the other hand, I don't rule out congenital hypothyroidism.

PATIENT: Is that good or bad?

DOCTOR: Not bad. Of course, that can cause dwarfism, sparse hair, yellow skin, distended abdomen, puffy face, thick lips, depressed nose, tooth eruption, swollen tongue and constipation. Otherwise, it doesn't impair your normal activities.

PATIENT: As what? A dwarf?

DOCTOR: Well, let's take the bull by the horns and look at your throat.

PATIENT: Doctor, it's only a little soreness.

DOCTOR: Little? Just a little naked germ you can't see with the naked eye. And what can a little, little germ do? Nothing! Except cause plague, decimate a democracy, pollute a people, terminate a tribe, eradicate a race and cause a global fungus where no potatoes or peanuts could germinate for generations. Now, stick your tongue out and say "ah."

PATIENT: Ahh - (It sounds more like a sob of anguish.)

DOCTOR: So my diagnosis is simply this –

PATIENT: I'm going to die?

DOCTOR: No. You have nothing more than a mild sore throat. Are you relieved?

PATIENT: Yes - but I wish you hadn't used a cannon to shoot a rabbit.

DOCTOR: Just gargle a little salt in hot water. (Picks up pencil) Now. My brilliant nurse failed to give me your name. I assume you have one?

PATIENT: Charles Abbott. Doctor Charles Abbott.

DOCTOR: Doctor?

PATIENT: That's right.

DOCTOR: (Leaps to his feet) A doctor! Oh, my God - God loves me. (He races to the Patient) Heaven has sent you to me! I need a doctor to confirm the fact that I'm a very sick. Sit down. Draw your chair up closer. Look at my tongue. (He sticks it out.)

PATIENT: But I'm not qualified to make a diagnosis for you. I'm a veterinarian. I could only treat you if you were a dog.

DOCTOR: Where's your humanity. Am I less than a Doberman? All I want is an opinion. You know when a dog is sick by its tongue. Why not me? Look. (Sticks out his tongue again.)

PATIENT: (Studies his tongue.) Well, if you were a dog, I'd say you had rabies.

DOCTOR: I knew I'd caught something. Feel my pulse. I promise you - it'll be a new experience for you. (Extends wrist)

PATIENT: (Holds wrist.) Seems normal to me.

DOCTOR: Normal for what? Me or a Doberman?

PATIENT: Doctor, surely you must realize there is a great difference in the bodily functions between you and a Doberman.

DOCTOR: Name one. We all have similar organs.

PATIENT: Do you lift your leg to micturate?

DOCTOR: It's the same function.

PATIENT: Try it in public.

DOCTOR: Well, I'm sick. as a dog. All I want is corroboration. Treat me like a dog.

PATIENT: Have you swallowed any foreign objects lately?

DOCTOR: Just seaweed.

PATIENT: No coins? Or keys?

DOCTOR: No. But I'm about to swallow my pride. Doctor, I'm on my knees. I know I've caught something from a patient. You wouldn't understand that because you're a veterinarian and they don't catch things from their patients.

PATIENT: Oh, but they do.

DOCTOR: What possible diseases can a veterinarian catch from a sick cat?

PATIENT: Not diseases. Fleas.

DOCTOR: Fleas are not fatal. Fertile but not fatal. (Hands him a stethoscope.) Here - listen to my heart and tell me how bad it is.

PATIENT: (Uses stethoscope.) I'd say you're strong as a horse. Or at least an ox.

DOCTOR: Then the trouble must be someplace else. The human body is a jigsaw puzzle. We have to find the right part. (He drops his pants.)

PATIENT: Doctor - I've just met you!

DOCTOR: Maybe I've got a hernia. Or terminal hemorroids. Feel my hiatus.

PATIENT: Doctor, I really don't think I know you well enough.

DOCTOR: Maybe you'd better look into my prostrate.

PATIENT: Doctor Craven, I wouldn't look at your prostate unless I could see it through your throat. (Starts to get his hat. The Doctor hobbles after him, impeded by the trousers around his ankles.) (He goes out.)

DOCTOR: Some doctor! I wouldn't send him a constipated canary. (Goes to mirror and looks at tongue. His nurse enters.)

NURSE: What was that patient laughing about as he left?

DOCTOR: He has a perverted sense of humor. I guess he thought my prostate was funny.

NURSE: He was a doctor?

DOCTOR: Not in my books.

NURSE: What are you doing with your shirt off?

DOCTOR: I was going to wash it - what else. Here. (He hands her his stethoscope.) See if my heartbeat is normal.

NURSE: What side is your heart on?

DOCTOR: The right side.

NURSE: (Listens to his chest.) It's there alright. I can hear a thump. (Stares at Doctor’s chest.) Oh, good Lord! I can't believe itl

DOCTOR: What is it? Am I hemorrhaging?

NURSE: No. But you've caught something from that doctor who just left.

(Races to get aerosol can.)

DOCTOR: What is it? A sore throat? (Sticks out his tongue like a lizard after a fly·)

NURSE: (Grabs a can.) I think I'm just in time. (Races back.) Don't move. Stand perfectly still.

DOCTOR: For God's sake - what is it? What have I caught?

NURSE: Fleas! (As she sprays his chest the curtain descends.)
```

---

## IC-1054: Pillow Talk

- Title: Pillow Talk
- Author (byline): Peter Tolan
- Work: Stay Carl Stay
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Jan 1998
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: AARON, DOUG
- Teaser before the introduction: Yes
- Spoken words (computed): 1723
- Already set (do not supply): none

### Source block (context only)

```text
Author: Peter Tolan
Book: Stay Carl Stay
ISBN: 978-0822210771
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Aaron and Doug have been friends since childhood.

ACTOR 2: But when they are put in a situation where sharing a bed is the only option . . .

ACTOR 1: Well, anyone who know anything about awkward slumber parties or toxic masculinity will understand how this plays out.

TOGETHER: Pillow Talk by Peter Tolan
```

### Performance text (classify this)

```text
Doug and Aaron are discovered in the tiny bedroom of a mobile home. The room is dominated by a smallish double bed, and bags and luggage crowd the floor making passage around the bed difficult. Doug sits on the edge of the bed dressing a wound on his ankle while Aaron calls through the open door to his (unseen and unheard by us) grandmother.

AARON: (calling off) No, Grandma . . . we're all set. No, we're fine. No, I don't think we need any more blankets. Thank you. Goodnight.

DOUG: (calling off) Goodnight, Mrs. Markell. (listening) No, it's fine. The bleeding's stopped . . . (listening) No, I'm sure Pookie didn't mean it. It was my fault. I shouldn't have been doing what I was doing.

AARON: What were you doing?

DOUG: (quietly) Standing next to the little bastard. (calling off) Uh-huh . . . no, I'm sure he's a very sweet ferret. It's no problem.

AARON: (calling off) Grandma? Grandma, we're going to sleep now so stop talking, okay? Well, I love you too. Yeah, I'll see you in the morning. Goodnight. (quietly to Doug) She doesn't get too many visitors.

AARON: (Doug starts to exit the room) Where are you going?

DOUG: Now you be brave, young fella. I'm just down the hall.

AARON: Doug, where are you going?

DOUG: To my room.

AARON: Yeah. Right here. We're sleeping in here.

DOUG: We? We who?

AARON: We we. You and me we. Here. In the bed. Where did you think you were going to sleep?

DOUG: Down at the end of the hall. I thought there was another bedroom.

AARON: Doug, this is a mobile home. There isn't another of anything. They give you one kitchen, one living room, one bathroom, one bedroom.

DOUG: (brightly) Okay . . . fine, fine. Yeah.

AARON: Goodnight. (covers his face with a pillow. Doug considers for a moment, then begins to moan and stretch)

DOUG: You know, all this driving . . . this is one hell of a long trip. Sitting in that Honda fifteen hours every day . . . and this is only the first day! The old back's already begging for mercy. I'd better sleep on the floor.

AARON: (removes the pillow from his face) You want to sleep on the floor?

DOUG: Don't want to. Have to. My back needs the support . . . a hard surface. Maybe I can sleep on the floor in the living room.

AARON: You want to go out there and sleep on the floor? Go ahead. Tomorrow morning we'll find your shoes and a 155 pound ferret. (flops back down on his pillow)

DOUG: I forgot about Pookie. Damn. I knew I should have killed him when I had the chance. You know, you kill anything named Pookie, you're doing the community at large a great service. People would be stopping you in the street . . . "You killed Pookie? God bless you . . .

AARON: (sits up again) Doug . . . please. I'm tired. I need sleep. The sandman's here and he's backing up the truck. Lie down. Go to sleep. Now. (puts the pillow back over his face. Doug thinks, then gingerly sits on the edge of the bed. Pause. Aaron lifts up one edge of his pillow and looks at Doug) Strange. The light is still on. What could this mean?

DOUG: Can I tell you something? (quietly) I have never. . . I've never slept with a man before.

AARON: (considers this) Really. That's odd. I had you pegged as the kind of guy who's slept with hundreds of men.

DOUG: You know what I mean. I've never slept with a man . . . in the same bed.

AARON: What . . . not even when you were a kid? Like when you were in Scouts or something?

DOUG: I wasn't in Scouts. I was in Chess Club. Sleeping together wasn't allowed. I think they figured it would take our minds off the game.

AARON: Uh-huh. (pause) So . . . what do you think's going to happen? You get into bed, close your little eyes, tomorrow morning you wake up rested, relaxed, with a huge hickey.

DOUG: (concerned) Funny. That's very funny. I'm trying to tell you about a serious thing, and all you do is . . .

AARON: (laughing) I'm sorry, I'm sorry.

DOUG: I hope you're having a good time mocking my discomfort.

AARON: Goodnight.

DOUG: Goodnight. (Aaron clicks off the light as Doug reclines slowly. After a pause, Aaron rolls over so that his body is turned toward Doug, who clicks the light on) Hello. You're facing in my direction.

AARON: Yes. I usually sleep facing this way. Is this a problem?

DOUG: I feel like you're looking at me. Could you turn the other way? (Aaron grumbles loudly through his teeth, grabs the covers and violently turns himself to face away from Doug) Thank you. Goodnight. (clicks the light off and starts to settle in for the night. A pause, then Aaron shifts around trying to get comfortable. After a few moves, Doug clicks the light on)

DOUG: I'm trying to sleep here; you're flailing around like it's a Dance Marathon!

AARON: You made me turn around, this is not the direction I usually sleep in, I'm trying to get comfortable!

DOUG: Why don't you just maul me and get it over with?

AARON: I never even came close to touching you! I'm sorry, Doug . . . (turning to face Doug) but I sleep facing this way, this is the way I'm going to sleep. Final warning. Sleep or be killed. (Doug takes one of Aaron’s pillows and one of his own and puts them in a line down the middle of the bed) I don't believe this. You're making a wall? You know, I don't think I've ever said this to you before, but you're a seething, twisted mass of neuroses. You really are.

DOUG: We all have our little quirks.

AARON: I agree. Why you've decided to lump them all together into one evening, I don't know.

But now it's time for you and me (motioning to the wall of pillows) and the Great Wall of China to go to sleep. (clicks off the light. A pause, then Doug clicks it back on)

DOUG: I won't be able to sleep if you're mad at me. I can't sleep if I think someone's mad at me.

AARON: (trying to control himself) All right. Look. I'm not mad at you. I was only trying to point out that you might have a problem.

DOUG: Oh, that's great.

AARON: Look, it's nothing. You're physically uptight, that's all. You don't like to be touched so you close yourself off. You're a closed person. Come on, it's not like I'm telling you something you don't know. Goodnight.

DOUG: Well, that's a little strong . . .

AARON: Anybody who puts pillows down the middle of the bed is scared of something. Admit it.

DOUG: It's a homo thing, isn't it? I'm serious. You know why I'm having so much trouble with this? Because I never had a homosexual thing as a kid. (pause) Did you?

AARON: (interrupting) Don't even ask!

DOUG: I thought we were such great old friends. You won't tell me about your homosexual experiences? . . . Timmy Loomis and I used to write our names in the snow. We'd *pee* in the snow and write our names. Is that a homosexual thing?

AARON: Well, I think we'd need a handwriting analysis before we could make that determination . . .

DOUG: (a pause as Doug thinks) Okay. When Timmy Loomis and I were in the fourth grade, we did this thing . . .

AARON: (sits up abruptly) You and Timmy Loomis again! What was it with you guys? Didn't you have any toys? Trucks or something like that to keep your hands occupied?

DOUG: We used to touch tongues.

AARON: What?

DOUG: We'd stick out our tongues and touch them together. Does that count?

AARON: (thinks for a second and then nods assuredly) Yes.

DOUG: You think so?

AARON: Oh, yeah. Touching tongues? Definite homosexual experience. Very high on the list. *Ding* And there's the bell, end of discussion! Go to sleep and stop worrying because you don't want to touch me and I sure as hell don't want to touch you! Okay?

DOUG: Okay. Goodnight. (Aaron clicks the light off. A pause, then Doug clicks the light back on) This is going to sound strange. I'm a little offended by that last remark you made. You think I'm ugly, is that it? . . . An ugly, short, balding guy.

AARON: (trying to hold it together) Doug! No! I do not think you're an ugly guy! That's not what I meant when I said I didn't want to touch you. It was just my attempt to assure you that such an action is not and probably never will be on my personal agenda of things to do. Goodnight. (clicks the light off)

DOUG: I don't know what your problem is . . .

AARON: (jumps up and turns on Doug) I'll tell you my problem! I'm trying to get a little sleep and all I hear is a lunatic talking about *peeing* in the snow and sleeping on the floor and putting the pillows down the middle of the bed! And now . . . now you have the nerve to tell me you're offended because I don't want to touch you? I'm going insane! You want to sleep in a closet? Go sleep in a closet! You want to be touched? I'll touch you!

(Aaron lunges at Doug and starts grabbing at him. Doug tries to fight him off, but he's ticklish and all he can do is laugh hysterically. The door swings open and light from the hall spills into the room. Grandma has heard all the noise and comes to investigate. Both men freeze, Aaron nearly on top of Doug, as they realize what's happened.)

AARON: Grandma! (leaps off the bed and turns on the light) I'm sorry. . . did we wake you? (listening) Well, I don't want to go into too much detail . . . Doug and I were sort of . . . wrestling, I guess. (listening, then running across the bed to get to the door) No, it's nothing like Cousin Duane . . . please believe that. No there's no need to talk to Mom and Dad. I'm sorry we got you up. Just go back to bed and we'll be quiet. I love you. Goodnight. (closes the door and stands, stunned -- to Doug) We're not going to talk about this . . . ever.

DOUG: Maybe we should.

AARON: No. We are guys. Guys do not worry about sleeping in the same bed. They do not talk about it. They shut up, they get it over with, and then it's done. Goodnight. (reaches up and clicks the light off) I'm going to tell her that you were having a seizure, and I was trying to keep you from swallowing your tongue when she walked in.

DOUG: You're pathetic.

AARON: No, Doug . . . I'm screwed. As soon as my grandmother wakes up . . . the second her eyes open . . . she's going to think, "Now, what was it I had to do first thing? Oh, that's right. I have to call Dick and Sheila and tell them their son's a homo!"

DOUG: You're blowing this way out of proportion . . . What are you trying to hide? Tell her the truth. Just say you were helping me get over my physical intimacy problem.

AARON: It was the middle of the night. She woke up, she only saw us for three seconds. She went back to sleep. It's highly possible that she's forgotten the whole thing.

DOUG: It's highly possible. But what if she hasn't?

AARON: No problem. We sit down to breakfast. We test the water. "How did you sleep last night, Grandma? I hope we didn't wake you." If she says no, she's forgotten, I'm safe. If she says yes - and she remembers everything - then we go into Operation Confuse Grandma. We deny. Totally. We shrug. And then, we push her over the edge. You look down at Pookie and you say, totally straight, "Pookie seems so nice. Has he ever bitten anyone?" And that does it! She's completely lost!

DOUG: You're trading your grandmother's mental health for your own!

AARON: Only if she remembers.

DOUG: You're really threatened, aren't you? . . . You're my best friend.

AARON: Great. Me and Timmy Loomis.

DOUG: Fine. Be a shit. You're still my best friend. I'm not sure I ever told you before, and I thought it might help.

AARON: Oh, yeah. It helps a lot. I'll tell my grandmother we're best friends and that'll settle the whole thing. (muttering) If only I was driving a pick-up with a gun rack. What can I do? I'll fix something. If nothing needs fixing, I'll break something, then I'll fix it . . . (sees Doug getting undressed) What are you doing?

DOUG: I'm getting undressed. I don't like sleeping in my clothes. (jumps into bed and starts taking the pillow wall apart) Tonight is a small piece of a much larger puzzle. It's new territory. I'm crossing the country. New places. A whole new outlook every day. If I've made this much progress on the first night, imagine what the rest of the trip will be like! (lies back. and closes his eyes as Aaron sits up, his eyes wide)
```

---

## IC-1055: The Pillowman

- Title: The Pillowman
- Author (byline): Martin McDonagh
- Work: Not specified
- Publisher: Faber and Faber
- Publication date as stated: Sept 2004
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: TUPOLSKI, KATURIAN, MICHAL, MICHAEL
- Teaser before the introduction: Yes
- Spoken words (computed): 2668
- Already set (do not supply): none

### Source block (context only)

```text
Author: Martin McDonagh
ISBN: 978-0571220328
Publisher: Faber and Faber
Date (Month/Year): Sept 2004
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 2: In The Pillowman by Martin McDonagh, a writer is interrogated about the gruesome content of his short stories and their similarities to a number of child-murders that are happening in his town.

ACTOR 1: He learns that his older brother, Michal, is also being held and questioned in another cell.

ACTOR 2: Michal, who has the mind of a child.

ACTOR 1: Michal, who our author, Katurian, has raised ever since the death of their parents.

TOGETHER: The Pillowman by Martin McDonagh
```

### Performance text (classify this)

```text
NOTE: This cutting asks one student to portray 2 different characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

PAGE 25 - 30

TUPOLSKI: What happened to the third child? Andrea Jovacovic. You know who she was?

KATURIAN: (pause) Only from the papers. She was the girl they found on the heath.

TUPOLSKI: She was the girl they found on the heath, yes. You know how she died?

KATURIAN: No. The papers didn’t say.

TUPOLSKI: You know who Aaron Goldberg was? He was the boy they found in the dump behind the Jewish quarter. You know how he died?

KATURIAN: No. The papers didn’t say.

TUPOLSKI: (mocking) No, the papers didn’t say. They papers didn’t say a lot of things. The papers didn’t say anything about the third child, a little mute girl, went missing three days ago, the same area, the same age.

KATURIAN: What did my brother say to you? Whatever he said, you made him say. He doesn’t speak to strangers. I want to see him. I’ve got a right to see my brother! (crying) I just write stories! I don’t understand a thing of what’s going on!

TUPOLSKI: No? Well, here’s where we stand. Along with the evidence we found in your house, your brother has, under duress or not, admitted enough about the killings for us to execute him before the evening’s out. But, he’s hardly the brains behind the operation, so we want you to confess too. We like executing writers. Dimwits we can execute any day. And we do. But, you execute a writer, it sends out a signal, y’know? (Pause) It sends out the signal ‘DON’T . . . GO . . AROUND . . . KILLING . . . LITTLE . . . KIDS.’ (Pause) Where’s the mute girl?

KATURIAN: (pause) I’ve listened to your bullshit for a long time now, and I want to tell you a couple of things. . . I don’t believe my brother said a word to you. I believe that you are trying to frame us for two reasons. One, because you don’t like the kind of stories I write, and two, because you don’t like retarded people cluttering up your streets.

PAGE 36 – 67

A cell. Michal is listening to the intermittent screams of his brother, Katurian, being tortured a room away. Michal mimics them till they fade way. Michal’s cell is unbolted and the bloody, breathless Katurian is thrown in. Michal looks over Katurian, who is shivering on the floor, goes to caress his head, can’t quite do it.

MICHAL: Hiya. You were making some racket. What were they doing, torturing ya?

KATURIAN: Did yours hurt? When they tortured you?

MICHAL: They didn’t torture me. (Katurian looks him over for the first time, seeing there are no cuts or bruises) Oh, no, the man said he was going to torture me, but I thought, ‘No way, boy, that’d hurt,’ so I just told him whatever he wanted to hear, and he was fine then.

KATURIAN: (pause) Swear to me on your life that you didn’t kill those three kids.

MICHAL: I swear to you on my life that I didn’t kill those three kids. (Katurian breathes a sign of relief)

KATURIAN: The only thing they’ve got against us is what you’ve said, and the stuff they said they found in the house. Oh my God. Whatever they do, Michal, no matter what, you don’t sign anything. You got it?

MICHAL: Whatever they do to me, I don’t sign anything. (Pause) Can I sign your name?

KATURIAN: Especially don’t sign my name.

MICHAL: ‘I killed a loda kids,’ signed Katurian Katurian. Hah! ‘And it was nothing to do with his brother, Michal, not even a bit,’ Hah!

KATURIAN: (Pause) We’ll be alright, Michal. We’ll be alright. We’ll get out of here. If we just stick together.

MICHAL: Tell us a story, Katurian. It’ll take my mind off . . .

KATURIAN: What story do you want?

MICHAL: Do ‘The Pillowman’.

KATURIAN: (Pause) Once upon a time . . . there was a man, who did not look like normal men. He was about nine feet tall . . . (Michal looks up, silently whistles) And he was all made up of these fluffy pink pillows: Even his head was a pillow, a big round pillow.

MICHAL: A circular pillow – I prefer ‘ a circular pillow’.

KATURIAN: His head was a circular pillow. And on his head he had two button eyes and a big smiley mouth.

MICHAL: Do your mouth smiley like the Pillowman’s mouth is. (Katurian gives a big dopey smile)

KATURIAN: Well, the Pillowman had to look like this, he had to look soft and safe, because of his job, because his job was a very sad and a very difficult one . .

MICHAL: Uh-oh, here it comes . . .

KATURIAN: Whenever a man or a lady was very very sad because they’d had a dreadful and hard life and they just wanted to take their own lives by razor, or by bullet, or by gas, or . . .

MICHAL: Or by jumping off of something big.

KATURIAN: Yes. Just as that person was about to do it, the Pillowman would go to them, and sit with them, and gently hold them, and he’d say, ‘Hold on a minute,’ and time would slow strangely. The Pillowman would go back in time to when that man or that lady was just a little boy or a little girl, to when the life of horror they were to lead hadn’t quite yet begun, and the Pillowman’s job was very, very sad, because the Pillowman’s job was to get that child to kill themselves.

MICHAL: Um, could you skip on to the end, please? This bit’s a bit boring.

KATURIAN: Well, that’s a bit rude, Michal, actually. MICHAL; Oh, Sorry, Katurian. (Pause) But could you skip on to the end, please?

KATURIAN: (Pause) Well . . . the end of the Pillowman . . . See, when the Pillowman was successful in his work, a little child would die. And when the Pillowman was unsuccessful, a little child would have a horrific life, grow into an adult who’d also have a horrific life, and then die horrifically. He decided to do just one final job and that’d be it. So he went to this place beside this pretty stream that he remembered from a time before . . .

MICHAL: I like this bit . . .

KATURIAN: And he brought a little can of petrol with him, and he sat and he waited there a while. There was a little caravan nearby, and the Pillowman heard the door open and little footsteps come out. It was a little Pillowboy. And the Pillowman told him all about his sad job and the dead kids and all that type of stuff. And the little Pillowboy understood instantly, and he poured the can of petrol all over himself. And the Pillowboy struck a match, and the Pillowman sat there watching him burn. And as the Pillowman gently started to fade away, the last thing he saw was the Pillowboy’s happy smiley mouth as it slowly melted away. The last thing he heard was the screams of the hundred thousand children he’d helped to commit suicide coming back to life and going on to lead the cold, wretched lives that were destined to them because he hadn’t been around to prevent them.

MICHAL: (Pause) So the Pillowman just faded away? Ah.

KATURIAN: Into the air. Into Heaven.

MICHAL: I like the Pillomwman. He’s my favourite. (Thinking) Hmmm. I still can’t figure it out.

KATURIAN: Figure what out? Figure out ‘The Pillowman’?

MICHAL: No, I thought I’d hidden it really well.

KATURIAN: Hidden what really well?

MICHAEL: The box with the little boy’s toes in it. They must’ve used sniffer dogs or something. Because, no, way, I hid them brilliant. Christmas tree pot. You only see it once a year.

KATURIAN: You just told me you didn’t touch those kids. You just lied to me.

MICHAL: No I didn’t. I just told you the man came in and said he’d torture me unless I said I killed those kids, so I said I killed those kids. That don’t mean I didn’t kill those kids. I did kill those kids.

KATURIAN: You swore to me, on your life, that you didn’t kill those three kids.

MICHAL: Ohhh. See with that one, yeah, I was kind of playing a trick on ya. Sorry, Katurian. I know it was wrong. Really, But it was very interesting. The little boy was just like you said it’d be [in your story, The Tale of the Town on the River] I chopped his toes off and he didn’t scream at all. His name was Aaron. God, he bled a lot. You wouldn’t’ve thought there’d be that much blood in such a little boy. Then he stopped bleeding and went blue. I feel quite bad now, he seemed quite nice. But the girl was a pain in the *ass*. Kept bawling her eyes out. And she wouldn’t eat them. She wouldn’t eat the applemen, and I’d spent ages making them. It’s really hard to get the razor blades inside. You don’t say how to make them in [that] story, do ya? I checked. So, anyway, I had to force ‘em down her. It only took two. Not being mean, but at least that shut her up.

KATURIAN: (Realization has finally dawned –quietly) What did you do it for?

MICHAL: Don’t cry, Katurian. Don’t cry. You know. Because you told me to.

KATURIAN: (pause) I remember telling to your do your homework on time. I remember telling you to brush your teeth every night . . . I don’t remember telling you to take a bunch of little kids and go butcher them!

MICHAL: I didn’t butcher them. .”Butcher them’ it’d be more like . . . (Michal imitates viciously hacking at someone.) Mine was more like . . . (Michael imitates a gentle, single hack onto imaginary toes, then delicately throwing the tows away.) And . . . (Michal imitates placing two applemen inside a little mouth, then swallowing) And I wouldn’t have done anything if you hadn’t told me, so don’t you act all the innocent. Every story you tell me, something horrible happens to somebody. I was just testing out how far-fetched they were. (Pause) D’you know what? They ain’t all that far-fetched.

KATURIAN: You’re a sadistic, retarded pervert who enjoys killing little kids!

MICHAL: (Pause) I didn’t enjoy killing those kids. It was irritating. It took ages. And I didn’t set out to kill those kids. I just set out to chop the toes off one of them and to put razors down the throat of one of them.

KATURIAN: Are you telling me you don’t know that if you chop the toes off a little boy and put razors down the throat of a little girl, you don’t know that they’re gonna die?

MICHAL: Well, I know now! (Katurian puts his head in his hands, trying to think of a way out of this). Well, the torture man certainly seemed to be on my side. He seemed to agree it was all your fault. [That] all the things I did to all the kids I got from stories you wrote and read out to me.

KATURIAN: That isn’t the truth, Michal.

MICHAL: Yes it is. Did you write some stories with children getting murdered in them?

KATURIAN: Yes, but . . .

MICHAL: Well, did you read them out to me?

KATURIAN: Yes . . .

MICHAL: Well, did I go out and murder a bunch of children? (Pause) ‘Yes, I did,’ is the answer to that one. So I don’t see how the ‘That isn’t the truth’ comes into it. I mean, you’re my brother and I love you, but y’know, you’ve just [been] telling me a story about a bloke, his main thing in life’s to get a bunch of little kids to set themselves on fire, so y’know? And he’s the hero! I’m not criticizing. He’s a very good character. He reminds me a lot of me – You know, getting little children to die. All that.

KATURIAN: The Pillowman never killed anybody, Michal. And all the children that died were going to lead horrible lives anyway.

MICHAL: You’re right, all children are going to lead horrible lives. You may as well save them the hassle.

KATURIAN: Not all children are going to lead horrible lives.

MICHAL: Erm, hmmm. Did you lead a horrible life since you was a child? Yes. Erm, did I lead a horrible life since I was a child. Yes. That’s two out of two for a start.

KATURIAN: They’re going to execute us in an hour and a half. They’re going to destroy us, they’re going to destroy my stories.

MICHAL: Well, I think it’s us we should be worrying about, Katurian, not your stories. They’re just paper.

KATURIAN: (barely containing he anger) If they came to me right now and said, “We’re going to burn two out of the three of you, you, your brother, or your stories,’ I’d have them burn you first, I’d have them burn me second, and I’d have it be the stories they saved.

MICHAL: You’re just like Mum and Dad!

KATURIAN: (Laughing) I’m just like Mum and Dad? Let me work this out . . . Mum and Dad kept their first-born son in a room where they tortured him for seven straight years, and you made a little boy bleed to death, made a little girl choke to death, did God knows what to another little girl and you’re not like Mum and Dad?

MICHAL: I’m not like them. I didn’t want to hurt anybody. I was just doing your stories.

KATURIAN: What did you do to the third girl?

MICHAL: (long pause) When I was in here listening to you screaming next door, I thought his musta been kinda like how it was for you all those years. Well, let me tell ya, it’s easier from this side.

KATURIAN: I know it is.

MICHAL: You only had it for an hour and you came in *whining* your snotty head off. Try it for a lifetime.

KATURIAN: That doesn’t excuse anything.

MICHAL: It excused the two you murdered. Why should it excuse the two I murdered?

KATURIAN: I murdered two people who tortured a child for seven years. You murdered three children who hadn’t tortured anybody for any years. There’s a difference. . . How did you kill the third girl, Michal? I just need to know. Was she like in a story too? . . . Which story was she like?

MICHAL: You’re gonna be mad. Like, um . . . she was like in um . . . ‘The Little Jesus’. ‘The Little Jesus’. (Katurian looks at Michael, hands to his face and, as he pictures the horrific details of the story, he slowly starts to cry.) Will they execute us together or separate? I hope it’s together. I wouldn’t wanna be on my own.

KATURIAN: I haven’t done anything!

MICHAEL: At least we’ll be together in Heaven, whatever happens. And hang out with God.

KATURIAN: Which particular Heaven is this you’re going to Michal? Child-killer Heaven? Do you want to know where you’re going when you die? You’re going to go to a little room in a little house in a little forest, and for the rest of all time you’re going to be looked after not by me, but by a person called Mum and a person called Dad, and they’re gonna look after you in the same way they always looked after you, except this time I’m not gonna be around to rescue you, ‘cos I ain’t going to the same place you’re going, ‘cos I never butchered any little kids . . .

MICHAL: That is just the most meanest thing that any person has ever said to any other person.

KATURIAN: I used to love you so much.

MICHAL: (pause) What do you mean, ‘used to’? (Long silence)

KATURIAN: Right at this moment, I don’t care if they kill me. I don’t care. But they’re not going to kill my stories. They’re all I’ve got. The three stories you chose to act out just happened to be the three most repulsive stories you could’ve chosen to act out. They weren’t the first three you happened to come across, they were the three that most suited your repulsive little mind.

MICHAL: So, what, I could’ve done ones that wouldn’t’ve been so horrible? Like what? Like ‘The Face Basement’? Slice off their face, keep it in a jar on top of a dummy, downstairs? They’re all sick. You couldn’t’ve picked one that wouldn’t’ve been just as sick.

KATURIAN: Why did it have to be ‘The Little Jesus’, though?

MICHAL: Tell me a story. Tell me the one about the little green pig.

KATURIAN: (pause) I can’t remember how it goes, ‘The Little Green Pig’ . . .

(remembering) Okay. Settle down (Michael does so with a pillow beside his head) Once upon a time, on a farm in a strange land far way. . .

MICHAL: Far away . . .

KATURIAN: There lived a little pig who was different from all the other pigs around.

MICHAL: He was green.

KATURIAN: Are you telling this story or am I? Are we interrupting or are we listening and sleeping?

MICHAL: You. Sorry. Fingers on lips. Shhh. Listening and sleeping.

KATURIAN: Good. (pantomimes telling the rest of the story as Michael falls asleep. Katurian looks at Michael and realizes he is asleep – and finishes the story in a whisper) . . . he knew that he was still, and he always would be, just a little bit peculiar . . . (Pause) You like that one, don’t you Michal? You used to like that one. No little toes in it . . . no razor blades in it. (Pause) It’s not your fault, Michal. (Crying) I’ll be coming along soon. (Katurian takes the pillow and holds it down forcefully over Michal’s face. Michal starts to jerk. After a minute Michal’s jerks lessen. He’s dead. Katurian takes the pillow off, kisses Michal, crying, he closes Michal’s eyes. He goes to the door, clangs it loudly) Detective?! (Pause) Detective?! I would like to make a confession to my part in the murders of six people. (Pause) I have one condition. (Pause) It involves my stories . . .
```

---

## IC-1056: Red

- Title: Red
- Author (byline): John Logan
- Work: Not specified
- Publisher: Oberon Books
- Publication date as stated: May 2010
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ROTHKO, KEN
- Teaser before the introduction: Yes
- Spoken words (computed): 2352
- Already set (do not supply): none

### Source block (context only)

```text
Author: John Logan
ISBN: 978-1840029444
Publisher: Oberon Books
Date (Month/Year): May 2010
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Red is the color you feel when anger strikes your bones, and shudders through your being

ACTOR 2: Red is the color of the last rays of the sun touching you and filling you with warmth

ACTOR 1: Red is fire, red is lust

ACTOR 2: Red is passion, red is trust.

ACTOR 1: Red reminds us that we are all simply phoenixes destined to burn.

TOGETHER: Red by John Logan
```

### Performance text (classify this)

```text
Rothko stands, staring forward. Ken, a man in his early twenties, enters nervously. He wears a suit and tie. This is the first time he has been in the studio. Rothko gestures for him not to speak. Then he beckons for Ken to join him. Ken goes to Rothko, stands next to him. Rothko indicates the central painting (ie the audience)

ROTHKO: What do you see? (Ken is about to respond—) Wait. Stand closer. You’ve got to get close. Let it pulsate. Let it wrap its arms around you; let it embrace you. — Meet it halfway for God’s sake! Lean forward, lean into it. Engage with it! . . . Now, what do you see? — Be exact — but sensitive. You understand? Be kind. Be a human being. These pictures deserve compassion, and they live or die in the eye of the sensitive viewer, they quicken only if the empathetic viewer will let them. That is what they deserve . . . Now . . . What do you see?

(Beat.)

KEN: Red.

ROTHKO: Hang up your jacket outside. I appreciate you put on your Sunday clothes to impress me, it’s poignant really, touches me, but it’s ridiculous. We work hard here. Go hang up your jacket outside. (Ken exits and returns without his jacket. Takes off his tie and rolls up his sleeves.) We start every morning at nine and work until five. You’ll help me stretch the canvases and mix the paints and clean the brushes and build the stretchers and move the paintings. You’ll pick up food and cigarettes and anything else I want, any whim, no matter how demanding or demeaning. If you don’t like that, leave right now. Answer me. Yes or no.

KEN: Yes.

ROTHKO: I am not your rabbi, I am not your father, I am not your shrink, I am not your friend, I am not your teacher —I am your employer. You understand?

KEN: Yes.

ROTHKO: I’m painting a series of murals now — (He gestures all around.) You’ll help me put on the undercoat and then I’ll paint them and then I’ll look at them and then paint some more.

(Rothko moves away. Beat.) How do they make you feel?

KEN: Give me a second. (Ken moves to the middle of the room and takes in all the paintings.) Disquieted.

ROTHKO: And?

KEN: Thoughtful . . . Um . . . Sad.

ROTHKO: Tragic.

KEN: Yeah.

ROTHKO: They’re for a restaurant. (Rothko smiles. He enjoys this.) So I’m minding my own business when Mister Philip Johnson calls me. He’s designing the new Seagram Building on Park Avenue. In this building there is to be a restaurant called the Four Seasons, like the Vivaldi, and on the walls of this restaurant . . . (He gestures expansively to his paintings. Beat. Proud.) Thirty-five thousand dollars they are paying me. (Ken is impressed. Thirty-five thousand dollars is a fortune.)

KEN: (Beat . . . trying to impress his new employer) I went to the Modern last night, saw the Picasso show.

ROTHKO: That man — though now a charlatan, of course, signing menus for money like Dali, when he’s not making ugly little pots, also for money — that man at his best understood the workings of time . . . Tragic, really, to grow superfluous in your own lifetime. We destroyed Cubism, de Kooning and me and Pollock and Barnett Newman and all the others. We stomped it to death.

KEN: You take pride in that. “Stomping” Cubism to death.

ROTHKO: The child must banish the father. Respect him, but kill him.

KEN: And enjoy it?

ROTHKO: Picasso I thank for teaching me that movement is everything! Movement is life. The second we’re born we squall, we writhe, we squirm; to live is to move. Without movement paintings are what?

KEN: Dead?

ROTHKO: Precisely (He gestures to his paintings.) . . . Look at the tension between the blocks of color: the dark and the light, the red and the black and the brown. The more you look at them the more they move . . . they breathe . . . They’re not dead because they’re not static.

KEN: (Excited.) They need the viewer. Representational pictures are unchanging; they don’t require the active participation of the viewer. In the Louvre in the middle of the night the “Mona Lisa” is still smiling. But do these paintings still pulse when they’re alone? (Ken is lost in thought. Rothko watches him, pleased.) That’s why you keep the lights so low. . . To help the illusion. Like a magician. Like a play. To keep it mysterious, to let the pictures pulsate. Turn on bright lights and the stage effect is ruined — (Ken goes to the light switches. He snaps on all the lights. Ugly fluorescent lights sizzle on. The room immediately loses its magic.)

ROTHKO: What do you see?

KEN: My eyes are adjusting . . . Just . . . White.

ROTHKO: What does white make you think of?

KEN: Bones, skeletons . . . Charnel house . . . Anemia . . . Cruelty. (Rothko is surprised by this response.)

ROTHKO: How does white make you feel?

KEN: Frightened? . . . It’s like the snow . . . outside the room where my parents died. It was winter. I remember the snow outside the window: white (Turns his attention to the paintings.) . . . And the pictures in this light . . . They’re flat. Vulgar . . . This light hurts them. (Rothko turns off the fluorescent lights. The normal light returns.)

ROTHKO: You see how vulnerable they are? . . . People think I’m controlling . . . It’s not controlling, it’s protecting. A picture lives by companionship. It dies by the same token. It’s a risky act to send it out into the world. (He abruptly stops to stare at his painting. He tilts his head. Like he’s listening. Bring me the second bucket. (Ken, excited, brings him a brush and a bucket of dark maroon paint. Rothko is unsure. He looks at the painting. The moment is passing. He is getting desperate. To himself, frustrated.) Come on . . . come on . . . come on . . . What does it need?

KEN: Red.

ROTHKO: I wasn’t talking to you! (Beat. Tragically, the moment has passed for Rothko. He flings the paintbrush away. It splatters. He spins on Ken.) DON’T YOU EVER DO THAT AGAIN! (He rages, stomping restlessly around the room:) By what right do you express an opinion on my work? Who are you? “RED”?! — I don’t even know what that means! You mean scarlet? You mean crimson? You mean plum-mulberry-magenta-burgundy-salmon-carmine-carnelian-coral? What is “RED”?! (Rothko stands, getting his breath, collecting himself. Beat.)

KEN: I meant sunrise. I meant the red at sunrise . . . The feeling of it. Sunrise is red and red is sunrise. (Ken begins cleaning up.) Red is heartbeat. Red is passion. Red wine. Red roses. Red lipstick.

ROTHKO: Arterial blood.

KEN: That too. (Rothko thinks about it.)

ROTHKO: Rust on the bike on the lawn.

KEN: And apples . . . And tomatoes.

ROTHKO: Lava. Lobsters. Scorpions.

KEN: Stop sign. Sports car. A blush.

ROTHKO: Slash your wrists. Blood in the sink. (Beat.) So . . . red. (Rothko gazes thoughtfully at his painting then turns away) I can’t look at it now. It’s too depressing.

KEN: How can all that red be depressing?

ROTHKO: I don’t see the red anymore . . . .

KEN: What?

ROTHKO: Black. (Beat.) There is only one thing I fear in life, my friend . . . One day the black will swallow the red. (He puts on his glasses again and stares at his painting.) (Beat) I was walking up to my house last week and this couple was passing. Lady looks in the window, says: “I wonder who owns all the Rothkos.” . . . Just like that I’m a noun. A Rothko . . . An overmantel.

KEN: A what?

ROTHKO: (as Rothko speaks, they finish priming the next canvas) The overmantels. Those paintings doomed to become decoration. You know, over the fireplace in the penthouse. They say to you, “I need something to work with the sofa, you understand. Here’s a paint chip from the Sherwin-Williams” . . . . It’s an investment . . . It goes with the lamp . . . It’s interior decoration . . . It’s anything but what it is. (Beat.) (The priming is finished on the canvas and Rothko steps back and studies it. Musing.) So . . . so . . . so . . . it’ll do . . . What do you think?

KEN: It’s a . . . a good ground, a good base layer. Nice and even. (Ken smiles, Then he stops abruptly. Surprisingly, tears come to his eyes. The emotion is unexpected.)

ROTHKO: What is it?

KEN: It’s strange . . . I’m remembering something . . . The, um, color . . . is . . . Dried blood . . . When the blood dried it got darker. On the carpet where my parents died. (Ken tries to shake off the thought. He moves away. But then he stops again. He can’t shake the emotion. The canvas draws him back.) It’s exactly the color.

ROTHKO: What happened to your parents?

KEN: They were murdered.

ROTHKO: What happened? (Ken stares forward, lost in thought. Beat.) What do you see? (Ken shakes his head. Beat.)

KEN: (Reliving it) I woke up . . . and the first thing I saw was the snow outside my window. But . . . but . . . It was really quiet. . . . And it’s cold. There’s a window open somewhere . . . Then I see my sister, just standing in the hallway, staring into my parent’s room. My sister . . . she’s standing in a puddle of pee. Her eyes . . . I go to the door and look in and see the snow first. And then the blood. The bed’s stained with it. And the wall. They’re on the bed . . . Apparently it was a knife. (Beat.) Burglars, I found out. At least two of them . . . I don’t want my sister to see anymore. My little sister [I was seven] . . . I turn around and push her out and shut the door. The door handle . . . With blood . . . Is red. (Beat.) That’s all.

ROTHKO: What happened to you two?

KEN: State took us. Foster homes. People were nice, actually. They kept us together. But they shuffled us around a lot. We were rootless… Never belonged . . . Never had a place. (Ken continues to clean up. Pause.) Can I ask you something? . . . Are you really scared of black?

ROTHKO: No, I’m really scared of the absence of light.

KEN: Like going blind?

ROTHKO: Like going dead.

KEN: And you equate the color black with death. . . Because black is the lack of red, if you will. The bright colors are your passion, your will to survive — your “life force.” But if black swallows those bright colors then you lose that excess and extravagance, and what do you have left?

ROTHKO: [T]rust me, as you get older those colors are harder to sustain. The palate fades and we race to catch it before it’s gone.

KEN: In reality we both know black’s a tool, just like ochre or magenta. It has no effect. Seeing it as malevolent weird.

ROTHKO: You think so? What about equating white with death; like snow?

KEN: That’s different. That’s just a personal reaction. I’m not building a whole artistic sensibility around it.

ROTHKO: Maybe you should.

KEN: Come on, a painter gets older and the color black starts to infuse his work, therefore, the cliché goes, he’s depressed, he’s fearing death. He’s losing touch, he’s losing relevance, he’s saying goodbye.

ROTHKO: That’s a cliché except for when it’s not.

KEN: But it’s not true. . . Look at Van Gogh; his last pictures are all color. He paints the most ecstatic yellows and blues know to man — then shoots himself . . . Or Matisse, his last works were nothing but great shocks of primary colors . . . . he was dying, he knew he was dying, but he was still Matisse. When he got too ill to hold a paintbrush he used scissors, cutting up paper and making collages. He never gave up. On his deathbed he was still organizing the color patterns on the ceiling. He had to be who he was.

ROTHKO: (Rothko looks at him.) In the National gallery in London there’s a picture by Rembrandt called Belshazzar’s Feast . . . Belshazzar, King of Babylon blasphemes, so a divine hand appears and writes some Hebrew words on the wall as a warning . . . In the painting these words pulsate from the dark canvas like something miraculous. Rembrandt’s wrote “Mene, Mene, Tekel, Upharsin.” “You have been weighed in the balance and have been found wanting.” (Beat.) That’s what black is to me . . . ****Scene***** Ken is alone, building a wooden canvas stretcher/frame. Then the sound of a slamming door from outside surprises him. Rothko rages in, flinging off his overcoat and hat.

ROTHKO: THEY’RE TRYING TO KILL ME! I swear to God they’re trying to kill me!

KEN: So . . . how did you like the exhibit? (Rothko is not amused. He lights a cigarette.)

ROTHKO: (Seriously.) These young artists are out to murder me.

KEN: Andy Warhol? (Rothko doesn’t even answer.) You sound like an old man.

ROTHKO: My point is . . . People like me . . . My contemporaries, my colleagues . . . We all had one thing in common . . . We understood the importance of seriousness. (Beat.) You know the problem with those painters? They are painting for this moment right now. And that’s all. Completely temporal, completely disposable, like Kleenex, like —

KEN: Like Campbell’s soup, like comic books —

ROTHKO: You really think Andy Warhol will be hanging in museums in a hundred years?

KEN: He’s hanging alongside Rothko now.

ROTHKO: Because those goddamn galleries will do anything for money — cater to any wicked taste. That’s business, young man, not art! (Ken approaches. Not backing down.)

KEN: You ever get tired of telling people what art is?

ROTHKO: No, not ever. Until they listen.

KEN: You’re just mad because the barbarians are at the gate. And, whattaya know, people seem to like the barbarians.

ROTHKO: Of course they like them. That’s the goddamn point! You know what people like? Happy, bright colors. they want things to be pretty. (Explodes.) “Pretty.” “Beautiful.” “Nice.” “Fine.” How are you? Fine. How was your day? Fine. How are you feeling? Fine. Well, let me tell you, everything is not fine! (He spins to his paintings.) Conflicted. Nuanced. Troubled. Diseased. Doomed. I am not fine. Look at these pictures. Look at them! You see the dark rectangle, like a doorway, , yes but it’s also a gaping mouth letting out a silent howl of something feral and foul and primal and REAL. Not nice. Not fine . . . I AM HERE TO MAKE YOU THINK! . . . I AM NOT HERE TO MAKE PRETTY PICTURES! (A long beat. Rothko roams, disturbed, trying to recover his equilibrium. Ken hasn’t moved.)

KEN: So said the Cubist, the second before you stomped him to death. (Rothko stops, looks at him.) “Tragic, really, to grow superfluous in your own lifetime” . . . Right? “The child must banish the father. Respect him, but kill him.” . . . Isn’t that what you said? . . . You guys went after Cubists and Surrealists and, boy, did you love it. And now your time has come and you don’t want to go. Well, exit stage left, Rothko. Because Pop Art has banished Abstract Expressionism . . . (Beat.) Don’t worry; you can always sign menus for money.

ROTHKO: How dare you?

KEN: (Beat.) Do you know where I live? Uptown? Downtown? Brooklyn? [Do] you know if I’m married? Dating? Queer?

ROTHKO: No. Why should I —? You’re an employee. This is about me. Everything here is about me. You don’t like that; leave . . . your neediness bores me —

KEN: (Explodes) Bores you?! Bores you?! — (Ken roams angrily.) You know, not everything has to be so goddamn IMPORTANT all the time! Not every painting has to rip your guts out and expose your soul! Not everyone wants art that actually HURTS! Sometimes you just want a still life or landscape or soup can or comic book! Nothing is ever good enough for you! Not even the people who buy your pictures! Museums are nothing about mausoleums, galleries are run by pimps and swindlers, and art collectors are nothing but shallow social-climbers. (He stops, slows, realizing.) Who’s good enough to even see your art? . . . Is it just possible no one is worthy to look at your paintings? . . . That’s it, isn’t it? . . . We have all been “weighed in the balance and have been found wanting.” (He approaches Rothko.) You say you spend your life in search of real “human beings,” people who can look at your pictures with compassion. But in your heart you no longer believe those people exist . . . So you lose faith . . . you lose hope . . . black swallows red. (Beat. Ken is standing right before Rothko.) My friend, I don’t think you’d recognize a real human being if he were standing right in front of you.

ROTHKO: (defeated) You’re fired. (Beat. Ken stares at him. He can’t believe it.) Write down your address, I’ll send you your final check.

KEN: You owe me an explanation.

ROTHKO: I don’t owe you anything — (Ken pursues. Rothko tries to avoid him. The conflict builds. Rothko spins on him, points to the outside with the realization dawning that his artistic time is past.) Because your life is out there! (Beat.) Listen, kid, you need to find your contemporaries and make your own world, your own life . . . You need to . . . make them look. (Ken is moved. Rothko continues with quiet emotion.) When I was your age, art was a lonely thing: no galleries, no collecting, no critics, no money. We didn’t have mentors. We didn’t have parents. We were alone. But it was a great time, because we had nothing to lose and a vision to gain. (Beat.) Okay? . . . Make something new. (Rothko steps away. Ken gathers his things and starts to go. He stops at the door. He turns back.) What do you see? (Ken looks at the paintings. But then he looks at Rothko. Beat.)

KEN: Red. (Beat. Ken exits. Rothko stands alone.)
```

---

## IC-1057: Scooter Thomas makes it to the Top of the World

- Title: Scooter Thomas makes it to the Top of the World
- Author (byline): Peter Parnell
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Jan 1998
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: DENNIS, DAD, SCOOTER, WALLY, EDDIE, MR. GREENBAUM, SCOOTER’S FATHER
- Teaser before the introduction: Yes
- Spoken words (computed): 2031
- Already set (do not supply): none

### Source block (context only)

```text
Author: Peter Parnell
ISBN: 978-0822210009
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: We all knew somebody like Scooter Thomas: the kid who was always getting called to the principal’s office,

ACTOR 2: Who sassed the PE coach in junior high,

ACTOR 1: The rebel,

ACTOR 2: The outsider.

ACTOR 1: The risk-taker who we all secretly wanted to be a little more like.

ACTOR 2: But teen-age rebels can have trouble adapting to the realities of adulthood.

ACTOR 1: You see, our childhood is something we carry with us for the rest of our lives

ACTOR 2: – the lessons learned, the relationships built or discarded.

ACTOR 1: Its these experiences that shape us into the adults we become.

TOGETHER: Scooter Thomas Makes it to the Top of the World by Peter Parnell
```

### Performance text (classify this)

```text
Suggested Roles: Actor 1: Dennis, Eddie, Mr. Greenbaum, Scooter’s Father

Actor 2: Dad, Scooter, Wally

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

DENNIS: The call came in only a few hours ago

DAD: (Both on phone) Hello, son.

DENNIS: What’s the matter?

DAD: Don’t worry, Dennis. It’s not any of us – It’s your friend, Scooter.

DENNIS: Scooter Thomas, Scoots? But he’s in California (Pause) Oh, God, no . . . . (Put down phone) (Begins packing a suitcase – talks to audience) How many of you out there would like to receive a phone call from your dad telling you that your best friend in high school, whom you grew up with (Close suitcase) has just killed himself. And you’re expected to drive all night to be a pallbearer at a service taking place in, oh, less than twenty-four hours time? It’s funny, like – no matter how hard you try to just get on with it, other things keep coming back. It isn’t just stories, or names, or . . . or faces . . . it’s . . . it’s . . . this incredible sense of emptiness – you know? I guess it’s just knowing I’ll never see him again that’s really the most upsetting thing of it all. I guess what I’m really trying to tell you about is what happened between us – Scooter and me. That is . . . because (Start pacing to the side) well . . . it’s something that’s been on my mind since this afternoon . . .

SCOOTER: Psst! Tell them how I made it.

DENNIS: Scoots?

SCOOTER: Tell them how I . . .

DENNIS: Scooter, for God’s sake, what are you doing here?

SCOOTER: . . . made it to the top of the world.

DENNIS: What do you mean?

SCOOTER: I made it, Dennis. Don’t you understand? When it happened. You’re not going to leave out the most important part! Wally would have been proud of me.

DENNIS: (to audience) Scooter’s older brother. Now a corporate lawyer in Washington.

WALLY: Let’s not take the children, dear. It’s not an important affair. Just my kid brother, Scooter, who never could manage to . . .

DENNIS: Look, I realize you and he were never the closest of friends, but that’s no reason at this late date for you to start in. And what kind of stupid thing was that to do anyway? Go mountain-climbing all alone and then jump.

SCOOTER: I couldn’t find anyone else to go with. (Dennis pulls something out of his pocket and hands it to Scooter). The picture I sent you from Yosemite! I forgot about that. (slowly) Cathedral Peak! Dennis, that’s the mountain I . . .

DENNIS: Yeah. That’s what I figured. You and your mountains.

SCOOTER: Hatch’s Cliff.

DENNIS: What?

(SCENE – FLASH BACK TO WHEN THEY ARE 10-YEARS-OLD)

SCOOTER: On your mark, get set . . .

DENNIS: Last one to the top is a rotten . . . (Flash to the edge of the cliff) Lookit how high we are!

SCOOTER: Wanna jump into the water?

DENNIS: We can’t, Scoots – we’re too high up. Think anybody’ll find us?

SCOOTER: Nobody even knows we’re up here. You didn’t tell anyone didja?

DENNIS: Uh-uh.

SCOOTER: Me either.

DENNIS: Look, nobody’s got know about this place, okay? It’ll be our secret hiding place, okay.

SCOOTER: Promise? (Start to shake hands) Wait! (Scooter produces a knife from his pocket and cuts his hand open, then hands the knife to Dennis).

SCOOTER: Got it?

DENNIS: What do we say?

SCOOTER: I dunno, blood brothers? (Holds out hand)

DENNIS: Blood brothers (Holds out hand)

(SCENE – FLASH TO WHEN THEY ARE 13-YEARS-OLD (at school desks))

DENNIS: (Whispers) Oh geezo, geez. What’s the capital of Peru?

SCOOTER: (Whispers) It’s Lima

DENNIS: (Whispers) When did Columbus discover America?

SCOOTER: (Whispers) 1492

DENNIS: (Pause – still whispering) How come you know all this stuff, anyway? (Scooter holds out his hand where he has written all the answers) You can’t do that, that’s cheating!

SCOOTER: Relax. I’m going to wash it off.

DENNIS: You better. If Miss Palmer ever found out . . .

SCOOTER: She won’t. (Pounds fist and grinds it in, wiping off the answers) Will she?

(SCENE – POP TO DENNIS AS EDDIE MARCUS – SCOOTER’S BROTHER’S BEST FRIEND)

EDDIE: Psst! Hey, Scooter!

SCOOTER: Eddie, whadda you doin’ here? You cutting’ class in high school? Is Wally goin’ with ya?

EDDIE: He’s waiting outside –

SCOOTER: Oh, boy. I’m coming too!

EDDIE: N-O!

SCOOTER: I’ll tell my dad that you an’ he . . .

EDDIE: (Slaps Scooter) Just shut up, ya little moron, Okay!?! Nobody’d want to go drivin’ with you! You’re just Wally’s kid brother, ya little creep!’

SCOOTER: (to audience) He really got me angry when he said that. About me being Wally’s kid brother. I mean, who did he think he was?

(SCENE – POP TO SCENE WITH MR. GREENBAUM – 8th GRADE)

MR. GREENBAUM: . . . . Well, the nurse seems to think you might have even broken one of his ribs.

SCOOTER: Sorry, Mr. Greenbaum, sir.

MR. GREENBAUM: Let me tell you something, Scooter. You are a very bright, young boy. You could go far. But when will you learn to follow instructions? Eighth grade isn’t the end of the line.

SCOOTER: I didn’t start that fight, Mr. Greenbaum.

MR. GREENBAUM: But you certainly finished it, didn’t you?

SCOOTER: I’m just my brother Wally’s kid brother.

MR. GREENBAUM: Then why don’t you start acting like him, young man? Wallace was always one of my favorite students. He’ll be a tough man to follow – even beat.

SCOOTER: Then I won’t plan on trying, sir.

MR. GREENBAUM: I bet you must think you’re pretty funny, don’t you?

SCOOTER: Not especially, sir.

MR. GREENBAUM: Oh, yes. I think you think you’re very funny. Well, let me tell you something, Scooter Thomas: You may find yourself dead before you’re thirty, with the way you’re going. And that would be just about the un-funniest thing of all.

(SCENE – POP TO BOTH BOYS ON HATCH’S CLIFF – SCOOTER is sitting down, throwing rocks over the edge)

DENNIS: Hey there! Didn’t you hear me? I kept calling and calling down there. Nobody knew where you were . . . figured I’d try Hatch’s Cliff. Why weren’t you at practice.

SCOOTER: I didn’t even know there was one.

DENNIS: Whaddya talkin’ about. I told ya yesterday.

SCOOTER: So maybe I forgot.

DENNIS: Did Razorhead send you to Brownstein again?

SCOOTER: Yeah.

DENNIS: Look, I’m sorry I didn’t raise my hand or anything when he asked who else . . . I mean, I wanted to go up to him after . . . I really did.

SCOOTER: He likes you. He wouldn’t have gotten mad.

DENNIS: No, he’d have remembered from the last time . . . when we put chalk in his erasers.

SCOOTER: Yeah, what did he say?

DENNIS: (mocking Mr. Greenbaum) I’m very disappointed in you, Dennis. Associating yourself with the likes of Scooter Thomas. I should think you’d be embarrassed . . . (Realizes he should not have said that. Scooter stands and throws a rock hard) Yeah

(SCENE – POP TO AGE 16 – and throwing a football)

DENNIS: Margery Matthews?

SCOOTER: About a 6 (Throws ball)

DENNIS: Betsy Hamilton? (Throws ball)

SCOOTER: 4 . . . on Fridays a 5. (Throws ball)

DENNIS: Amy Lewis? (Throws ball) . . . Amy Lewis . . . . Scooter, Amy Lewis. Scooter are you in love with . . .

SCOOTER: What the hell kind of a lousy, stupid, moron thing is that to ask me, Dennis? (Throws ball).

DENNIS: I just wanted to know, that’s all.

SCOOTER: Why? So you can go around and tell every idiot you see that it’s true? Well, you can tell all those idiots anything you like.

DENNIS: (Throws ball down) What’s that supposed to mean?

SCOOTER: It means . . . I just don’t think it’s that big a deal, that’s all.

DENNIS: I suppose you think you could go all the way the first time out or something, huh? Huh?

SCOOTER: Yeah, well. Maybe I could. (DENNIS exits – Scooter paces back and forth and talks to unseen girl off stage front) What have I gotten myself into . . . Are you still out there? I understand if you don’t want to come out. Look, I just want you to hear what I have to say. I never woulda tried to do what I did with you if it hadn’t been for a stupid, crazy, insane bet I made six weeks ago with my idiot friend Dennis Wright. Anyway, I’m sorry I tried to put my tongue down your throat. I’m even sorrier it missed and got stuck in your braces. It wasn’t too pleasant for me either. I hope we can still be friends . . . Okay?

(SCENE – POP TO AGE 17 – Scooter is in a car)

DENNIS: Scoots, where have you been?

SCOOTER: (Hands on the wheel) C’mon, Dennis, get in the car.

DENNIS: (Gets in the car and they are moving) Scoots, are you drunk again?

SCOOTER: Smashed, buddy, ol’ pal of mine.

DENNIS: The guys and I waited all night for you to show.

SCOOTER: To the stars. Tonight I have been to the . . . you can put me right up there with the Big Dipper . . .

DENNIS: Listen, maybe I better drive. Remember what your parents . . . You’ve already nearly wrecked the car once . . . (Watches stop sign go by) Scoots – you just missed that stop sign!

SCOOTER: Was I supposed to hit it?

DENNIS: No, you were supposed to stop!

SCOOTER: Wanna honk the horn?

DENNIS: Jesus Scoots, you’ll wake up the whole . . . WATCH OUT!

SCOOTER: Ooooooh, we almost went over the cliff.

(SCENE – POP TO AGE 18 – playing poker)

DENNIS: Harvard.

SCOOTER: What about Yale?

DENNIS: Too tough.

SCOOTER: Dartmouth?

DENNIS: Too cold. Nobody’s applying to . . . Listen Scoots, your Dad’ll let you drive your car again soon. And anyway, after a year at home, once you pick up your grades, you’ll be able to transfer.

SCOOTER: To where?

DENNIS: Umm . . . well . . . You can visit me on weekends.

SCOOTER: It won’t be the same.

DENNIS: It’ll be cool . . . You still seeing . . .

SCOOTER: Carol? Yeah. I go over a lot. She says “hi.”

DENNIS: Say “hi” to her back. She like you.

SCOOTER: I like her.(Scooter exits)

DENNIS: (to audience) So, I didn’t see much of him the rest of that summer. Not because . . . I don’t know, I was busy working or something. I suppose it was about a year later that Scooter dropped out of college. I never did find out. It wasn’t until I went home one vacation that I ran into him working behind the post office counter that I found out. And then . . . it was sometime the following fall . . . he wrote me about this fight he’d had with his father - see . . .

(SCENE)

SCOOTER’S FATHER: What the hell you doing sleeping all morning? Come on, get up and get out of it . . .

SCOOTER: Dad, it’s Saturday for Christ sakes.

SCOOTER’S FATHER: What’s this all about? A letter from the mental clinic of Boston Hospital. It arrived this morning. A bill for psychiatric services, it says, fifty dollars. Fifty bucks!

SCOOTER: Dad, that letter was addressed to me, you had no right . . .

SCOOTER’S FATHER: No right? A letter to my son from a looney bin and I’m not supposed to know about it? Well, I’m not gonna pay for it if you think . . .

SCOOTER: I had to go in for a check-up . . .

SCOOTER’S FATHER: What kind of a . . . . in your head?

SCOOTER: Yes!

SCOOTER’S FATHER: What was it . . . stuck up your ass?

SCOOTER: I got into a fight with somebody last month. When I went to Boston with Carol, remember? She was going out with this other buy from B.U. and . . .

SCOOTER’S FATHER: Oh, I get it. And you just tagged along. You told us you were both going to visit Dennis. But instead you followed her to Boston and . . .

SCOOTER: I couldn’t help it, Dad. Carol, she lets this guy treat her so bad . . . and I . . . I love her . . . I really do!

SCOOTER’S FATHER: Love her? You love her? You don’t know the first thing about love. Love means responsibility. It means being an adult, which you don’t know the first thing…

SCOOTER: Look . . . just leave me alone, okay!?! Just go screw yourself!

(SCENE – POP TO AGE 26)

DENNIS: Hey, it’s really nice up here, you know? I’m glad you suggested we . . . I haven’t been on top of Hatch’s Cliff since . . . Jesus, must have been over a year ago. Yeah . . . you still seeing . . .

SCOOTER: On and off, yeah.

DENNIS: What’s she been doing?

SCOOTER: Getting married.

DENNIS: Oh, really? To that . . .

SCOOTER: Yeah . . . it’s just the way it is.

DENNIS: Yeah.

SCOOTER: I’ve been thinking about going out to the west coast.

DENNIS: You mean to visit?

SCOOTER: Maybe to live. To get out there and . . . I don’t know. Start sort of a new life for myself. I know you don’t think it’s a good idea.

DENNIS: What? No. I think it’s fine. Great. But, have you thought about maybe going back to school . . .

SCOOTER: I know you think I’m being irresponsible. You think I can’t do it.

DENNIS: No . . No . . . I didn’t say . . . I just thought if maybe you went back to school . . .

(SCENE – PRESENT DAY – DENNIS IS BACK TO PACKING HIS SUITCASE)

SCOOTER: Every time you asked me a question, you didn’t have to judge me . . .

DENNIS: Scooter. . . For Christ . . . I did not . . .

SCOOTER: Face it, man, you did!

DENNIS: Look. If you want to know what really made me judge you, it was all the silly little games you were playing, okay? The whole smug routine. Never telling me at all what was really going on inside your head . . . For Christ’s sake, Scooter. I was your friend!

SCOOTER: Friend, yeah! Just like Mom and Dad and Wally and Eddie and Greenbaum and Carol and all those other . . . all the rest . . . who spent so much time telling me how to live my life they wouldn’t even let me breathe . . .

DENNIS: Look, you’re not even here – You’re dead – so just GO AWAY! I won’t be made to feel responsible! Just because you . . . Oh, God . . .

SCOOTER: (Now he gets it . . . your work here is done) I think it’s time for me to get going.

DENNIS: I’m sorry, Scooter. If I did judge you, I . . . people grow older. Change. Maybe it was meant to be . . . maybe it was my fault, I . . . I had to move on . . . Say, Scoots? Listen, I . . . I hope you found what you were looking for. Up there.

SCOOTER: Found what I . . . Oh, yeah, Dennis. I did. I mean, I made it up, didn’t I? And then, somehow it all suddenly . . . well, finally began to make sense. I got to go now.

DENNIS: I know, Scoots. I know.

SCOOTER: See ya, pardner. (Exits)

DENNIS: See ya, Scooter (Dennis returns to packing then hears Scooter’s voice echo in his memory once more)

SCOOTER at 10: Nobody even knows we’re up here. You didn’t tell anyone, didja?

DENNIS as ADULT: (Hesitates at first) Uh-uh. Look, nobody’s gotta know about this place, okay? It’ll be our secret hiding place.

SCOOTER at 10: Promise . . . Wait! (Hold up hand and traces the scar from the blood brother pact) Got it?

DENNIS: Yeah. What do we say?

SCOOTER: I dunno. Blood brothers?

DENNIS: (Slowly brings his hand up in the air) Blood brothers.
```

---

## IC-1058: Slow Dance on the Killing Ground

- Title: Slow Dance on the Killing Ground
- Author (byline): William Hanley
- Work: Not specified
- Publisher: Dramatists Play Service, Inc
- Publication date as stated: Jan 1998
- Event as filed: Duo Interpretation
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
ACTOR 2: Meet Randall, a young black man on the run from the reality of his own creation.

ACTOR 1: And Mr. Glas, struggling to deal with an impossible choice made decades ago.

ACTOR 2: Both dance around reality . . . Always on guard . . . afraid to face their personal truths, let alone share them with others.

ACTOR 1: They hide behind the images they have chosen to show to the world. This night, however, a chance meeting between strangers offers a safe haven for the unburdening of two troubled souls.

ACTOR 2: The music has begun . . . it is time for this

TOGETHER: Slow Dance on the Killing Ground by William Handley
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

## IC-1059: The Society

- Title: The Society
- Author (byline): J. Omar Hansen
- Work: Play it Again!
- Publisher: Meriwether Publishing
- Publication date as stated: 1993
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: BYRON, KEATS
- Teaser before the introduction: Yes
- Spoken words (computed): 1045
- Already set (do not supply): none

### Source block (context only)

```text
Author: J. Omar Hansen
Book: Play it Again!
ISBN: 978-0916260972
Publisher: Meriwether Publishing
Date (Month/Year): 1993
```

### Introduction (context only: never use it for content warnings)

```text
BYRON: Art is a tool used to convey meaning.

KEATS: or at least, that’s what the majority of people believe.

BYRON: In fact, art is the absence of meaning.

KEATS: That’s what gives it resonance.

BYRON: The one true way to ruin art is to force a meaning on it.

KEATS: And this atrocity would never occur in:

BOTH: “The Society”

KEATS: By J. Omar Hansen
```

### Performance text (classify this)

```text
BYRON: Well.

KEATS: Yes, well. I agree.

BYRON: It has been a long time.

KEATS: It has. A year to be exact.

BYRON: I am overwhelmed.

KEATS: We must begin.

BYRON: Of course, you are right. (The two men take their seats at the ends of the table.)

BYRON: (BYRON stands.) Let it be known that the society of Poets of the World and the Universe comes now to a poetic order.

KEATS: Nice touch.

BYRON: Thank you. We shall be favored to hear the minutes read. (B YRON sits down and KEA TS rises with a sheet of line paper.)

KEATS: I will now read the minutes of the last meeting. Minutes read. Opening remarks. Poetry read. Lively discussion. No. bloodshed. Dues collected. Closing remarks. (KEATS sits.)

BYRON: Thank you. We will now have the opening remarks. Gentlemen, the state of the arts is at an all-time low. The theatre is dead. Has been for years. The painterly arts are in flux. Music remains melodic and therefore dubious and inconsequential. Film never really was an art form. The novel is fare for the masses, and the short story gets longer every year. It is poetry, and poetry alone, that remains a viable art. And why, you will ask? Simply put: we have escaped the foul dredge of meaning. The putrid cesspool of reason. We are art and art is us. We are poetry and therein a light in and of ourselves.

(KEATS starts to applaud. BYRON stares at KEATS with irritation. KEATS stops.) We bind ourselves to no outside order. Order is chaos. Chaos is order. Here, in this place, and this place alone, may the muses reside and flourish. (BYRON sits down. KEATS applauds loudly.)

KEATS: Dear me.

BYRON: Thank you.

KEATS: That was beautiful.

BYRON: You are too kind.

KEATS: I think I must weep.

BYRON: Don't.

KEATS: Poetic.

BYRON: Yes.

KEATS: The report from the secretary?

BYRON: Funding has stopped. The government refuses aid.

KEATS: Death to all tyrants, the presidency to all morons!

BYRON: Calm yourself.

KEATS: You are right ... I move we proceed with the reading of new works commissioned after last year's conference.

BYRON: I second. Who shall begin?

KEATS: May I?

BYRON: By all means.

KEATS: (KEATS stands. A pause) "Trample" ... Horse's hoof... on my... flat face.

(He sits. BYRON sits staring in awe.)

BYRON: What brevity ... I could see it... The horse... the hoof...the face. It is a masterpiece. It is utterly meaningless.

KEATS: You are too kind.

BYRON: May I?

KEATS: Oh yes, please. We are off to such a good start.

BYRON: (He stands and puts on reading glasses.) "Going to the park, and being very cold on a winter's night in Manhattan, when I thought I loved, but it was nothing."

KEATS: That's the title?

BYRON: (Taken aback) Yes.

KEATS: Oh, but I like it. I do. Very poetic.

BYRON: Oh. Do you think so?

KEATS: Oh, yes. Absolutely.

BYRON: ... Ashen black frostbite... toes ... purple pain... (A small envelope is pushed under the door. KEATS sees it.) ... you, black-brown lipped...

KEATS: Did you see that?

BYRON: What?

KEATS: There by the door.

BYRON: I'm not done.

KEATS: Someone pushed an envelope under the door.

BYRON: But I'm not done.

KEATS: Someone has pushed ...

BYRON: It's not fair.

KEATS: I...

BYRON: You got to read yours.

KEATS: But someone has pushed an envelope under the door. (This registers to BYRON for the first time. He gasps.) Should we see what it is?

BYRON: You mean it came from the other side of the door?

KEATS: Yes. I don't know what it could mean.

BYRON: (Frightened) Well, perhaps one of us should see what it is.

KEATS: Yes, I agree.

BYRON: (He doesn't want to.) Do you want me to?

KEATS: Well, I'll do it.

BYRON: All right. (KEATS walks over to the door and picks up the envelope. He looks at the door with a worried glance and then back at BYRON.)

KEATS: Perhaps we should call out to see who put it under the ...

BYRON: No! No, don't! It could be the ruin of the society! (KEATS jumps away from the door.) What is it?

KEATS: (He opens the envelope.) Why... it's a poem. It's a poem. Do you want me to read it?

BYRON: No, no, it's from the outside. I think we ought to put it back where it ...

KEATS: It's rather interesting.

BYRON: You didn't read it did you?

KEATS: I did. I want to read it to the society.

BYRON: I am against it.

KEATS: We must be bold.

BYRON: Very well. It's on your head. (BYRON goes to his seat and sits. KEATS walks to his seat and stands and then reads.)

KEATS: So much depends ... on what I write ... and what they think ... But never the twain shall meet. (A long pause)

BYRON: It smacks of meaning!

KEATS: What?

BYRON: I'll say it again! It smacks of meaning.

KEATS: I think you're right. What do we do?

BYRON: Put it back.

KEATS: Under the door?

BYRON: Yes, yes!

KEATS: Now?

BYRON: The sooner the better. (KEATS walks over to the door and kneels down and almost pushes it under. He stops.)

KEATS: Why do you think they pushed it to us?

BYRON: To corrupt us. They want to corrupt us! Push it back!

KEATS: But... the door... this has never happened before. There's someone out there.

BYRON: Corruption.

KEATS: Really?

BYRON: If you won't push it back at least leave it on the floor and read some more poetry. Come ... read.

KEATS: Perhaps you're right.

BYRON: Read another of your poems.

KEATS: But yours wasn't finished.

BYRON: That's all right. Read. (KEATS looks at the table for a minute and then stands with another poem. He looks at the envelope by the door) Don't look at it! (KEATS looks away. He looks again at his poem.)

KEATS: "The Night" ... Cool blackness ... More or less ... It is a...

BYRON: That rhymed!

KEATS: No it didn't.

BYRON: Yes it did. You read a rhyme.

KEATS: No I didn't!

BYRON: I know a read rhyme when it rends my ear. That was a rhyme.

KEATS: Well... perhaps. Sometimes I like rhyme.

BYRON: What?

KEATS: I like rhymes!

BYRON: I don't believe it. The corruption has started. That envelope! It will be the ruin of us all. I must destroy it! (BYRON lunges towards the envelope but KEATS overtakes him and physically keeps him from the envelope.) Let me destroy it, I tell you!

KEATS: Stop it! Stop it! You're being absurd!

BYRON: Thank you.

KEATS: I didn't mean it as a compliment.

BYRON: How else should I take it?

KEATS: I'm going out the door.

BYRON: (BYRON gasps in horror) No!

KEATS: I think I must.

BYRON: You don't understand. You are young. There is corruption out there. There is meaning out there!

KEATS: How do you know?

BYRON: I can't tell you!

KEATS: (He goes to BYRON and confronts him.) I want to know!

BYRON: (Sobbing, he falls to his knees.) I can't! Don't make me. Please don't make me!

KEATS: (He grabs BYRON by the lapel.) Tell me!

BYRON: (Slowly)... I know... because I went through the door! But I was lucky. I saw the corruption. I saw meaning and knew it would destroy me. How I found the room again, I don't know. But you mustn't try it. You won't return. Others have gone. The society remains here. But they don't return. Please, listen to me.

KEATS: But what did it mean? Never the twain shall meet?

BYRON: Don't you see what's happening to you? You asked what it meant. Do you hear what you said?

KEATS: Did I say that?

BYRON: You did. (KEATS walks over to the door and picks up the envelope.) Don't do it! Don't do it! ... Push it back under. Come away from the door. (For a long pause KEATS stands with the envelope in his hand. Finally he pushes it back under the door. He walks slowly back to BYRON who embraces him.) Dear boy, you have won. The battle is won... I think we should continue ... But no more poems. After this they might be perceived as purposeful.

Come, let's return and finish the conference. There still is left the collection of dues. (They both go back to the table. BYRON takes a plate that was sitting on the table, blows off the dust and pushes it over to KEATS' side of the table. KEATS looks at it with a worried look. He feels in his pocket. He pushes the plate over to BYRON's side of the table. BYRON turns and sees it. He looks a little embarrassed.) ... Now for the final remarks ... Once again we are reaffirmed. We are the last bastion of artistry. We live to be as art.

KEATS: That's very beautiful.

BYRON: Thank you. We are adjourned. Come embrace me. It has been a marvelous experience.

KEATS: Yes.

BYRON: Till next year?

KEATS: Next year. (BYRON smiles and then goes to a corner of the room farthest from the door. He lays down and sleeps. KEATS watches him and then looks at the door. He walks over to BYRON and sees that he is asleep. He looks at the door and then at BYRON. He walks to the door. He tries the knob and it opens. He looks back at BYRON. He exits out the door. BYRON begins to snore quietly as the lights fade to black.)
```

---

## IC-1060: Some Things You Need to Know Before the World Ends

- Title: Some Things You Need to Know Before the World Ends
- Author (byline): Larry Larson and Levi Lee
- Work: A Decade of New Comedy
- Publisher: Heinemann Drama
- Publication date as stated: March 1996
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: INTERVIEWER, APPLICANT, BOTH
- Teaser before the introduction: Yes
- Spoken words (computed): 1035
- Already set (do not supply): none

### Source block (context only)

```text
Author: Larry Larson and Levi Lee
Book: A Decade of New Comedy
ISBN: 978-0435070137
Publisher: Heinemann Drama
Date (Month/Year): March 1996
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: God's busy, right? He doesn't have time to sift through every prayer asking for help.

ACTOR 2: To help out, over the centuries the Catholic Church has recruited patron saints to act as sort of receptionists to sort through your requests.

ACTOR 1: There are tons of patron saints. You name it, the Church probably has a saint for it.

ACTOR 2: You’ve heard of Saint Nicholas,

ACTOR 1: St. Patrick and St. Valentine

ACTOR 2: But did you know that there is also a Patron Saint of Fireworks?

TOGETHER: St. Barbara! *BOOM*

ACTOR 1: Today we witness the application process of a new saint.

ACTOR 2: All hail, Saint Wally.

TOGETHER: Some Things you Should Know Before the World Ends by Larry Larson and Levi Lee
```

### Performance text (classify this)

```text
(Pg 98-103) Lights come up on the desk area where an official-looking man is rubber-stamping documents. Another man enters, looking sheepish. He is carrying an application.

INTERVIEWER: (Ringing bell on desk.) Next! (Goes back to stamping)

APPLICANT: Excuse me.

INTERVIEWER: I'll be right with you.

APPLICANT: They, ah, told me ... (The Interviewer continues to stamp more papers while applicant waits)

INTERVIEWER: All right, what can I do for you?

APPLICANT: Well, they told me I should give this to you personally. (Hands him the form.)

INTERVIEWER: Oh, right. (Reading.) "Application for Sainthood."

APPLICANT: (Beaming saintly.) That's right!

INTERVIEWER: (Reads it over:) All right. Um. Hmm. You just have to answer these questions at the bottom of the form.

APPLICANT: It said not to fill in below the line ...

INTERVIEWER: Well, that's right. But ...

APPLICANT: So I didn't.

INTERVIEWER: I see that.

APPLICANT: I try to follow all instructions exactly. I believe that a saint ...

INTERVIEWER: Well, you're not a saint yet are you?

APPLICANT: I guess not.

INTERVIEWER: Right. Now, I'll just ask you a few questions and we'll get this thing wrapped up.

APPLICANT: The sooner the better!

INTERVIEWER: Right. Okay. First question here is, "Why do you want to be a saint?"

APPLICANT: Well, it all started when I was a very young child. I saw a small bird with a broken wing lying on the ground ...

INTERVIEWER: Poor thing.

APPLICANT: It was a tiny fragile thing, but one of God's creatures all the same. I saw in that bird all of mankind ...

INTERVIEWER: It's there.

APPLICANT: I was only four years old at the time ...

INTERVIEWER: Very young ...

APPLICANT: ... but as I held that broken little body in my hands a soft, wonderful voice spoke in my ear, and she said "You can heal that bird." And I did. After that time, I knew somehow I was special. I tried to do everything by the book. I followed all the teachings of the church. I never cursed, not even in my heart. And I've heard my friends say, "Eh, that Wally, he's really a saint, eh?" And I started thinkin' humbly, in my heart that it might be true. And then I heard that same soft, wonderful voice, this time say, "Wally, why don't you go ahead and fill out an application?" So here I am!

INTERVIEWER: (Writing.) "Wants to sit on the right hand of God." Now there's the question of martyrdom.

APPLICANT: Martyrdom?

INTERVIEWER: Of course, you know, dying a violent death before your time ... ?

APPLICANT: Against your will?

INTERVIEWER: Not necessarily. Now if you'll just tell me what kind of martyr's death you'd like to die ...

APPLICANT: Gee, I never thought about it.

INTERVIEWER: Most people haven't. We have several popular methods. (He opens a large sample book like the ones banks use to feature personalized checks.) Now, this is a real hot number ... (Points with his pencil.)

BOTH: Fire.

INTERVIEWER: Right. A lot of early saints went this way. Joan of Arc, to name a few

APPLICANT: I like that.

INTERVIEWER: Well, we have others. Here's a traditional martyrdom, if you're the old-fashion type, being torn apart by wild beasts.

APPLICANT: Well, it's very colorful ... but I'm kind of allergic to animal fur. I'd hate to sneeze myself to death!

INTERVIEWER: Of course. Well, here's one that's not used too often. Having your throat cut from ear to ear.

APPLICANT: That sounds festive. Let's keep that one in mind.

INTERVIEWER: Of course there's stoning.

APPLICANT: Too heavy.

INTERVIEWER: Crucifixion?

APPLICANT: Don't want to be a copycat.

INTERVIEWER: Beheading? Fast, simple . . (Demonstrates with chopping motion.)

APPLICANT: No, wanna keep my head.

INTERVIEWER: Oh, here's my personal favorite. Hot lead in the ears.

APPLICANT: Oh, I like that! No, no, wait, my mum said never to put anything in your ear smaller than your elbow.

INTERVIEWER: Wise woman.

APPLICANT: No, I was really thinking of something a little more ... modern, eh? Like a couple of cases of beer and some Quaaludes.

INTERVIEWER: No, if that would work, Marilyn Monroe would be a saint.

APPLICANT: Janis Joplin.

INTERVIEWER: Jimi Hendrix.

APPLICANT: Elvis Presley.

INTERVIEWER: Oh, he is a saint.

APPLICANT: He is? I didn't know that.

INTERVIEWER: Check your calendar. Well?

APPLICANT: I don't know. I can't make up my mind.

INTERVIEWER: Here's one. How about the Big M package?

APPLICANT: Big M?

INTERVIEWER: A combo. Look, you can be crucified and torn apart by wild beasts, you can be torn apart by wild beasts and have hot lead poured in your ears, or you can be crucified, have hot lead poured in your ears, and be torn apart by wild beasts with hot lead poured in their ears! Drives 'em crazy.

APPLICANT: No, I think I'm gonna go with something simple ... I'm gonna go with having my throat cut ear to ear.

INTERVIEWER: Well, it's your funeral.

APPLICANT: Well, thanks a lot. I'll be seeing ya ...

INTERVIEWER: Wait a minute. Where are you going?

APPLICANT: Goin' back to Bemidji. You know, make a few arrangements, send out announcements, call the caterer ...

INTERVIEWER: In addition to martyrdom, we require three miracles.

APPLICANT: Three miracles.

INTERVIEWER: Three miracles.

APPLICANT: Let's see. Does the bird count as one?

INTERVIEWER: Was he a lost cause?

APPLICANT: He was in pretty bad shape.

INTERVIEWER: Okay, I'm in a good mood today. (Writes.) Healed bird. Two more.

APPLICANT: Well, once I saw some kids knock down a spider's web, and the spider was left there homeless, so I repaired the web just by lookin' at it.

INTERVIEWER: That's it?

APPLICANT: Well, it's close work.

INTERVIEWER: (Hesitates, looks at Applicant. He is wide-eyed, hopeful.) (Writes.) Fixed web. One more.

APPLICANT: (Thinks hard. Nothing comes.) Gosh, let me think. One more. Jeez, I can't ...

INTERVIEWER: (Correcting him.) Uh, hmm ...

APPLICANT: Sorry, Christ, I ...

INTERVIEWER: Hmm .

APPLICANT: God! I . .

INTERVIEWER: Uh!

APPLICANT: (Getting more upset, confused.) Jesus Chris!

INTERVIEWER: (Interviewer points with his pencil as if issuing a final warning.) That's all right.

APPLICANT: I'm sorry. I just can't think of anything .... Oh, wait, there is one thing. Last summer, while I was on my vacation, I caused the sun to fall to the earth, infusin' all of mankind with its radiant light causin' them to be reborn in the Holy Spirit and thus live forever without fear, hunger or disease!

INTERVIEWER: Fear and hunger, eh?

APPLICANT: That's right.

INTERVIEWER: I'm sorry that's been taken.

APPLICANT: Oh no!!!

INTERVIEWER: I'm sorry.

APPLICANT: But I want to be a saint.

INTERVIEWER: Sorry ...

APPLICANT: I've worked so hard. Couldn't you check your book ....

INTERVIEWER: You'll have to move on.

APPLICANT: But I want to be a saint!

INTERVIEWER: (Angrily.) You want to be a saint! Everybody wants to be a saint! It's not easy! They're laying saints offl Now get out of my office!

APPLICANT: (Dejected, yet resigned.) Well, I guess that's it. (He pulls out a road map from his jacket.) Might as well just get back in the al' Winnebago and head back to Bemidji ...

INTERVIEWER: Wait a minute. Is that your road map?

APPLICANT: Yup.

INTERVIEWER: Where did you get it?

APPLICANT: Picked it up at the Sunoco right near the house.

INTERVIEWER: Did you refold that yourself?

APPLICANT: Sure. (Demonstrates.) Hundreds of times.

INTERVIEWER: (Holds up three fingers.) That's three!

APPLICANT: That's it! I'm a saint! I'm a saint! Oh, boy, I'll have my own day! I hope it's a Thursday ... Saint Wally . . .
```

---

## IC-1061: A Steady Rain

- Title: A Steady Rain
- Author (byline): Keith Huff
- Work: Not specified
- Publisher: Faber and Faber
- Publication date as stated: Feb 2010
- Event as filed: Duo Interpretation
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
ACTOR 1: Law enforcement is dangerous work.

ACTOR 2: But these days, the gravest threat to police officers’ lives comes not from criminals but from themselves – death by suicide.

ACTOR 1: In a world where toughness is prized, they hesitate to reveal frailties for fear of jeopardizing their careers.

ACTOR 2: Such reluctance becomes especially dangerous with officers who have temporarily lost their shields or been put on modified duty pending investigations that could cost them their careers.

ACTOR 1: Fear of losing reputation and friends is more than enough to drive them over the edge.

ACTOR 2: Denny and Joey, partners and best friends since childhood, are two cops on the edge.

TOGETHER: A Steady Rain by Keith Huff
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

## IC-1062: Strange Fruit

- Title: Strange Fruit
- Author (byline): Neil LaBute
- Work: Plays for Two
- Publisher: Vintage
- Publication date as stated: March 2014
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: TOM, JERRY
- Teaser before the introduction: No
- Spoken words (computed): 1775
- Already set (do not supply): none

### Source block (context only)

```text
Author: Neil LaBute
Book: Plays for Two
ISBN: 978-0345804549
Publisher: Vintage
Date (Month/Year): March 2014
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: June is big month for weddings, and for legislation about same-sex marriage. On June 16, 2008, clerks in several California counties began issuing marriage licenses to thousands of same-sex couples.

ACTOR 2: Over the next few months, 18,000 same-sex couples were married in California. The ruling, however, was short-lived. On November 4, 2008, opponents of the freedom to marry pushed through a constitutional amendment that stripped same-sex couples of marital rights.

ACTOR 1: The issue of gay marriage was fought in the courts for years. It wasn’t until June 26, 2015 that the United States Supreme Court ruled in favor of the freedom to marry, ending marriage discrimination not only in California, but across the country.

ACTOR 2: In the words of Supreme Court Justice Anthony Kennedy . . . “No union is more profound than marriage, for it embodies the highest ideals of love, fidelity, devotion, sacrifice, and family. . .

ACTOR 1: . . . marriage embodies a love that may endure even past death. . . these men and women . . . ask for equal dignity in the eyes of the law. The Constitution grants them that right.”

TOGETHER: Strange Fruit by Neil LaBute
```

### Performance text (classify this)

```text
SILENCE. DARKNESS. A man, TOM, standing in a bright light, wearing a tux. He talks to us. Another man, JERRY, in a tux, stands next to him. Smiling. They resemble the figures on the top of a wedding cake

TOM: . . . I love [guys]. I do. I'm really sort of just into [them], you know? [Guys]. And that's what got all this started, I mean, how I ended up here in the first place. Because of that. The ["guy"] situation. (Beat.) And I had, like, no idea when I was younger, I really didn't! None. I wasn't secretly putting on my mom's dresses or makeup at night or . . . or . . . reading the Hardy Boys and getting a . . . (embarrassed gesture) nothing like that.

JERRY: I loved the Hardy Boys, are you kidding me?! They were so cute, with all their . . . or maybe I'm thinking of the show. With Parker Stevenson. Yeah, that's it! That's the Hardy Boys I know. The TV ones. God, he was good-looking . . . Parker . . .

TOM: Funny thing is, I was totally into girls when I was younger. Seriously, I was!

JERRY: I grew up in Oregon. Beautiful part of the country

TOM: So I did the whole "marriage and kids" thing when I was nineteen . . . I did. Yeah! Why I don't know, because I was supposed to? Maybe. It was expected of me and so that's what I did. I did that . . . made it through sixteen years. Sixteen. (Beat.) No, "made it through" sounds so -- accurate. I don't wanna be like that, dump on her or be all . . . Well that's what I did. I just made it through. Barely.

JERRY: I met him when he was living in Chicago, divorced and just starting to dip his toe into the scene a little bit -- totally not sure about what he wanted, how he saw his life going in the next however long ... but he did like [guys]. That part was a given. Oh yeah!

TOM: I already said that, didn't I? And it's true . . . the second I did, that, it was like a light went off in my head and all these, like, fireworks and stuff ... big letters up in the sky saying "YES! WE'RE HOME!!" (Beat.) It was pretty awesome . . .

JERRY: He couldn't get enough and I was, you know what? It's like -- hey, I've always been a very giving person! Who am I to stop a guy who wants to learn? And this dude just couldn't get enough ...

TOM: And somehow we sorta just stayed together and became, I dunno, a couple, I guess . . . I mean, pretty soon he was moved into my place and there we were. Him and me. This . . . couple. In a relationship.

JERRY: I had always been looking for someone. I mean, a guy . . . Someone special, who gets me.

TOM: Anyway! Enough about us . . . trust me, it was working and if it does, when it does -- in life, I'm saying -- you shouldn't question happiness. Not ever.

JERRY: He was just a funny guy, really. That's what I liked about him. (Beat.) And great with his kids -- on the phone, anyway. He's not allowed to have them out to see him; they're in Orlando so he has to fly there if he wants to be around 'em at all, and that's . . . (Beat.) And that's how it went and suddenly, you know how it is . . . like, five years go by! We're looking in the mirror one morning -- we love to shave at the same time, share the water and, and the, you know, use the same little brush thingie with the soap --and, my god, I'm looking at myself and I say to him, "Jesus Christ, look at me. I'm thirty-nine years old." (Beat.) He leans over -- doesn't say a word -- just sort of lowers his head toward me, this little peck on my cheek. Then he whispers to me, "Wait'll next year. Forty's a bitch . . . "

TOM: He had a drop of foam on his nose, like a little puppy. Really cute, if you wanna know the truth . . .

JERRY: And we just stood there, bare-chested and with these towels on and started kissing. It was so good. Just . . . anyway, that's when he asked me. Said "Let's get married."

TOM: Which was a big deal, right? I mean, like I said, I'd already done it before and it was, well, whatever . . . it was what it was. My kids are terrific. (Beat.) Anyway, we'd even talked about marriage before but living in Chicago it was always about civil unions and domestic partnerships. all this s*** that wants to be the same, to give us a little hope that people are about to stop being so goddamn idiotic about something so basic, so simple if they'd just let it be but it's . . . anyway, he told me that he had this dream. About it . . . Like, a wish.

JERRY: I just wanted it to be the same as anyone else, you know? Except two guys on top of the cake, in tuxes -- really cute and both of us looking . . . it's stupid, I know, but I had actual dreams about it! Since I was a kid.

TOM: We kinda just watched and waited, without saying too much about it and yet nothing ·at all was changing so we thought maybe we could move to another state or, . . . or . . . you know -- but years go by and finally I say it as we stand there in the bathroom shaving. I'm the one to say it but we're both thinking it. Let's make this thing real! Marriage.

JERRY: Boom! Next day we've got tickets, we're off to California -- there's a window out there for us, I mean, we're two active, informed, vibrant people, right? We see what's going on in the world and it turns out there's, like, this five-month period in 2008 where that golden state near the ocean comes to its senses and says, "Yes, it's okay to be who you are" and we run out there like everyone else. Do this thing before anybody can say "no" to us again. And they do, they close that thing down like a book snapping shut, a few months later. Darn! But we do it. We get married.

TOM: We looked amazing -- I mean, yes, it was just the courthouse and all, but we did the whole deal he'd been wanting. Tuxes and, and just the entire . . . we were pretty much awesome. Standing there in the hall and . . . well, people were staring. That's all I'm gonna say. They were. Staring.

JERRY: Just like I'd dreamed about. Seriously.

TOM: And we were just giddy the rest of the day. We snuck off to San Diego to be at that hotel that was in the movie with Marilyn Monroe and the guys dressing up like two women . . . you know the one! It's ummmmm . . .

JERRY: I'd never been to the Hotel del Coronado just gorgeous, this big ol' place propped up on the beach there . . . just very . . .

TOM: I took my tux off but I could not get my husband -- or wife or whatever the hell I was gonna call him now -- he wouldn't take his off! Said he was gonna go downstairs and get some cigarettes . . .

JERRY: My one vice.

TOM: He'd been a smoker for years -- works out religiously but wouldn't think of giving up his nicotine! (Smiles.) He was standing there, at the door to the room, smiling at me, this big grin on his face. Asking me if I wanted anything. Some Twinkies or whatever.

JERRY: Somebody loves "Hostess."

TOM: I said "No thank you, I'm a married man now . . . " and we laughed and I blew him a kiss. Out he went.

JERRY: They didn't have any Marlboros there in the little gift shop so I went out into the streets. Looking for a 7-Eleven.

TOM: And . . . apparently . . . he ran into three guys who were coming up from a swim. Just some college kids from what the news said . . . and the police report.

JERRY: I was walking along in my tux, carrying a bag of mangoes and one of those stupid roses that you buy -- the single ones with a bit of plastic around the petals -- they keep 'em right up there by the checkstand so I got one for my fella . . .

TOM: And they must've said something because I know that . . . he could never let it go . . . you know? Ever. Some guy two feet taller than him and ten years younger and he'd go after 'em like a little rooster if it was about us or being gay or, like, any of the stuff he believed in. Those kids in Africa or . . . or Amnesty International -- he'd be up in your face and telling you that you're full of s***! (Laughs.) That was just him. You know?

JERRY: I remember these surfer boys passing . . .

TOM: He wasn't found until the next morning. Down by the rocks, where the water's . . .

JERRY: It's just funny . . . one day I'm standing in Chicago, the next thing you know I'm walking down a street with palm trees on it! I mean, palm trees!! With a rose in my hand and a paper bag full of strange fruit and, I dunno, this . . . love, I guess. Yeah, love in my heart for him and everybody else. Right? Even these three guys who are moving toward me now . . .

TOM: The story made the papers and was kind of a big deal, especially after all the . . . anyway. Yeah.

JERRY: Three boys who are getting louder as they come . . .

TOM: One day, few months later, somebody sent me a picture of us, before all that, standing on the courthouse steps as we waited in line to go in -- and I keep it out where I can see it now; I'll give it a glance when I head off to work or out for a run, that kinda thing -- it's of the two of us, both in our suits and smiling and from a distance or, if you stand back from it just a bit, you know what?

JERRY: I couldn't see their faces but they were laughing-and yelling and the sun was just behind them as they came closer . . .

TOM: We're like that couple you see on top of a cake. That little plastic couple, only it's two guys. Us. Vibrant and young and frozen for a moment. I mean . . . well, you get what I mean, right?

JERRY: They were laughing . . .

TOM: Us standing there and smiling, as if all was right with our lives and not anything could possibly go wrong. You know?

JERRY: And they were getting louder and rowdier but to me, on this day and how I was feeling . . . it sounded like little birds singing.

TOM: As if nothing in the whole wide world was able to scare us or hurt us . . .

JERRY: These beautiful little birds . . . singing just to me from up in Heaven above . . .

TOM: . . . or frighten us. No. Not us. Not ever again . . .

(Suddenly a light over JERRY blinks eff and out. He is now lost in the darkness. Hands unlock. TOM stands alone in the Jading light. TOM tries to smile but this too Jades away. SILENCE. DARKNESS.)
```

---

## IC-1063: Summer Reading is Killing Me

- Title: Summer Reading is Killing Me
- Author (byline): Jon Scieszka
- Work: Not specified
- Publisher: June 2000
- Publication date as stated: Puffin Books
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: JOE, NARRATOR, FRED, SAM, TOGETHER, RED QUEEN, DEVIL, FRANKENSTEIN, THE DEVIL, TEDDY, ANNA
- Teaser before the introduction: Yes
- Spoken words (computed): 1254
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jon Scieszka
ISBN: 978-0141308203
Publisher: June 2000
Date (Month/Year): Puffin Books
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 2: Summer Reading is Killing Me by Jon Scieszka
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles: Actor 1: Joe, Fred, Frankenstein Actor 2: Uncle Joe, Narrator, Giant, Sam, Red Queen, Character from Lord of the Flies, Devil, Teddy, Anna

JOE: (Pg 6-7) This is going to be impossible to explain. But I think I know what happened. My life has not been the same since my uncle Joe gave me THE BOOK (An elderly Uncle Joe hands Joe a very precious book) – a book like no book I’ve ever read before or since. It’s a time-warping book. I know. I know. You’re saying to yourself . . . .

NARRATOR: “What’s with this guy? He probably still believes in the Easter Bunny and the Tooth Fairy.”

JOE: I didn’t really believe it myself. Then Sam and Fred and I opened THE BOOK. We have been chased by a woolly mammoth, turned into mummies and nearly suffocated by one very nasty-smelling giant. (Giant burps a disgustingly foul burp and Joe responds) (Beat) And once we go to another time, the only way to get back to our time is to find THE BOOK in that time . . . So anyway, there we were – sitting in my room the very first day of summer vacation . . . We were trying to be careful. We really were!

FRED: (Pg 8-9) No more classes, no more books. No more teachers’ dirty looks!

SAM: (pointing to a book on the bookshelf) Can we please promise not to open THE BOOK and get sucked into some time-travel trouble like we always do?

FRED: I’m with you. We don’t have to open any books!

SAM: Well, now that you mention books . . . I was thinking we might get an early start on this list.

FRED: Summer reading list? Are you crazy. This is vacation.

SAM: (Reading aloud from the list) Each student must read four books during the summer and fill out the attached study guide for two of them. The list has Hatchet, The Phantom Tollbooth, The Hoboken Chicken Emergency . . .

FRED: (Pg 10-12) (grabs the list from Sam and sticks it in a book from the shelf)

JOE: (stares, aghast at the bookshelf) Forget it you guys! You don’t have to decide!

SAM: What do you mean we don’t have to decide?

JOE: (pointing to the bookshelf) We have about three seconds before this green mist leaking off my bookshelf decides for us! (The boys are engulfed in a green mist)

FRED: How did that happen? I didn’t do nothing.

SAM: Anything. You didn’t do anything except put our summer reading list inside THE BOOK! *****

FRED: (Pg 16) (looking around cautiously) We can’t be in a book. That only happens in movies. There is no way I am going to spend my summer vacation in a book.

SAM: This is very weird, but quite possibly true. What if story characters are real? What if they have a life we just don’t know about.

JOE: (Pg 20-21) Oh no . . We are in huge trouble. If this means what I think it means, all of the characters from every book on the summer reading list are mixed up here. And none of them are in their books where they’re supposed to be. The librarian is going to kill us.

SAM: What if the Red Queen says, “Off with Ramona’s head!?”

JOE: What if the Twits mess up Wayside School?

SAM: What if the Tripods take over the Little House on the Prairie? We have to get everyone back in the right book!

JOE: (Pg 22-23) We have to get back THE BOOK and take the summer reading list out of it before anything happens!

TOGETHER: THE LIBRARY!

JOE: (Pg 25-27) We took off. We passed old houses, an alley, a street lined with shops and in just a few minutes we were at the corner of the park. Just then we heard a wild yelling and the sound of stomping footsteps behind us. (Actor 2 provides sound effects) Dracula was dragging Winnie-the Pooh in a headlock. Mr. Twit was breaking Harold’s purple crayon. Twenty different bad guys from twenty different books were chasing, hauling and pushing all kinds of characters up the steps of a big old brick building.

FRED: (Pg 28) (Reading the sign on the building) Hoboken Public Library!

SAM: The one building in Hoboken that we need to get into is packed with every bad guy from every book ever written! (The boys sneak into the library) (Pg 33) (in a whisper) I see it, but I don’t believe it. That’s Mrs. Twit tying up Marry Poppins and Encyclopedia Brown.

JOE: That’s Frankenstein holding Pippi Longstocking

FRED: They even got Mother Goose.

RED QUEEN: (Pg 34-35) Off with their heads!

CHARACTER FROM LORD OF THE FLIES: Kill the pig! Cut his throat! Bash him in!

JOE: I don’t know what’s going on here, but it doesn’t look good. Let’s sneak up those stairs and start looking for THE BOOK – quick! (they begin up the stairs but are stopped by a commanding voice)

DEVIL: You three boys. What book are you from? Come here now!

FRED: Is that who I think it is?

JOE: Do you know any other red guy with two horns and a pointed tail? (to the Devil) (Pg 38) We’re the Time Warp Trio!

DEVIL: (Looking at his list) I have no Time Warp Trio!

RED QUEEN: (Pg 38) Off with their heads!

SAM: We’re probably not under Time Warp Trio because we’re actually a series . . .

FRANKENSTEIN: (Groaning and making a move toward them) Series . . . bad!

THE DEVIL: (Pg 39-40) (Stroking his beard) Maybe you can make this easier on all of us. What we are doing here is separating the good characters from the bad characters. The bad characters stay here and take over any story they like . . . And the good characters go there . . . to be crushed by those huge stacks of books and wiped out of stories forever! So . . . are you good characters . . . or bad characters?

JOE: (Pg 42-43) Then the door with LIBRARIAN written on the glass slammed open with a bang.

TEDDY: What is going on out here?!

FRED: A . . . . a . . . teddy bear?

TEDDY: (Pg 44) That’s Mr. Bear to you, kid! (The boys try to hold in their laughter) This is exactly what I’m talking about. Just because I’m a teddy bear, I get no respect. Everyone thinks I’m soft and huggable and stupid! What exactly is the holdup here? Why isn’t everyone being crushed?

DEVIL: (Pg 45-50) We were . . .uh . . I was just . . . checking in these three characters.

TEDDY: Characters? Hah! They aren’t characters from a book. These are three kids. In fact, they are just the kind of readers I get no respect from – wise-guy boys! Throw them in the crusher now! (Frankenstein lumbers to do his bidding)

JOE: (Screaming) Now just one minute! Look, Mr. Teddy – I mean Mr. Bear. It is true that we are not the biggest fan of teddy bear books . . . but crushing all of the good characters from every other book is not going to solve anything. (trying to sound very adult and reasonable) Just look how dumb these books sound without their main characters.

SAM: There are giant holes in every story. (he picks up a book and reads) “Run run run as fast as you can. You can’t catch me, I’m the blankety blank?

JOE: (grabbing another book) The Hoboken Chicken Emergency is just The Emergency

FRED: (picking up a third book) Sylvester and the Magic Pebble is And the Magic Pebble.

TEDDY: Aww, that is so sweet. You are worried about all the poor little books. Well, don’t worry. The new titles of those books will be The Teddy Bear Emergency, Teddy Bear and the Magic Pebble and The Teddy Bear Man! (Raises his arms and laughing a crazy villain laugh at the ceiling) Frankenstein in Wonderland . . . Green Eggs and Dracula.

FRANKENSTEIN AND THE RED QUEEN: (Cheering) Ted-dy! Ted-dy! Ted-dy!

TEDDY: (Pg 58-59) Crush those boys now!

FRED: We’ll never make it to the door. Quick. Up these stairs!

JOE: We charged up the steps two at a time. Captain Ahab, the Devil and a red-golden dragon climbed after us. We reached the top landing, blocked by the stack of books that had been meant to crush us. (To the boys) Get back here and push! (They give a massive shove. Frankenstein and Dracula are buried in the avalanche)

SAM: (Pg 60-61) Nice shot!

TEDDY: You are making me angry!

JOE: We couldn’t hold out for much longer. I looked around for a way to escape. Stairs blocked. Window too high to reach. That’s when I saw our salvation! A thin blue book covered with silver stars and moons. A folded list stuck out of the middle. THE BOOK!

TEDDY: (Pg 62) I will squash you! I will flatten you like the bugs you are! No one ruins my plans. I will be the most famous character in every story!

FRED: Give me some cover . . .

(He does an amazing maneuver, in slow motion. to leap over the bad characters and grab the book; Sam and Joe continue to pelt the characters with books as a distraction) (Fred dramatically opens the book and removes the reading list – holding it aloft as if were Excalibur)

******

(the boys are engulfed in a green mist and land back in Joe’s bedroom, surrounded by books. Fred has THE BOOK in one hand the reading list in the other. They shake themselves and immediately begin thumbing through the books)

JOE: (Pg 67-69) Mary Poppins, Charlotte, Frog and Toad – everybody’s back! (the boys laugh in relief)

ANNA: Ahem! (the boys freeze) Ahem! I don’t really want to know what you are doing. I just wanted to ask you if you have any ribbon I can use for my (She holds her teddy bear aloft) teddy bear . . .

TOGETHER: (Cowering in fear) NOoooooooo!
```

---

## IC-1064: Tarzan

- Title: Tarzan
- Author (byline): Wayne Rice and Mike Yaconelli
- Work: Greatest Skits on Earth – Volume 1 (Pg 49)
- Publisher: Zondervan
- Publication date as stated: March 1986
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, COLONEL, TARZAN, CHIEF, JIVE, TENDERBELLY
- Teaser before the introduction: Yes
- Spoken words (computed): 1116
- Already set (do not supply): none

### Source block (context only)

```text
Author: Wayne Rice and Mike Yaconelli
Book: Greatest Skits on Earth – Volume 1 (Pg 49)
ISBN: 978-0310351412
Publisher: Zondervan
Date (Month/Year): March 1986
```

### Introduction (context only: never use it for content warnings)

```text
TOGETHER: Tarzan by Wayne Rice and Mike Yaconelli
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

This skit takes place "in the jungle," of course. As it opens, Tarzan's boy companion, Jive, is tied to a pole, ready to be burned at the stake.

Characters:
• Tarzan - Actor 1
• Colonel Grub, the villain - Actor 2
• Chief – Actor 2
• Jive, Tarzan's boy companion – Actor 2
• Tenderbelly, the chief's daughter – Actor 2
• Narrator – Actor 1

NARRATOR: Darkest Africa! Wild and foreboding! Man-killing beasts stalk their prey in these dark jungles, ready at any moment to spring, tear, and mangle. Wild savages lurk in dense underbrush waiting to ambush unwary travelers. So sit right back and relax, as we present "Tarzan."

COLONEL: (to audience) Hi, there! I'm the villain in tonight's episode! So far, I've burned down the village of the Lumbago Tribe, I've captured Tarzan's little friend Jive, and, worst of all, I've said nasty things to the animals! But, so far, Tarzan hasn't shown up!

TARZAN: (Tarzan enters, swinging on a rope if possible, and yelling.) AHHH ... EEEEE ...

AHHH ... EEEEE ... AHHH ... WAAYA!

COLONEL: Oh-Oh! That's Tarzan now! (to Tarzan) Me Colonel Grub! You Tarzan! Tarzan want boy to live? Tarzan listen to me! Me Boss! You Slave! Savvy?

TARZAN: Tell me, Colonel, have you had this speech problem all your life?

COLONEL: Why-Why, you speak as good as me!

TARZAN: Wrong again, Colonel! That's "as well as I." And I happen to speak better than you.

COLONEL: But when did all this happen? What happened to your English?

TARZAN: Well, Jane isn't with me any longer, so I spend my evenings brushing up on my English!

COLONEL: Well, good English or bad English, the situation remains the same! Either you take orders from me or the boy dies!

TARZAN: Big deal! I hardly know the kid! (Chief enters.)

CHIEF: Ungowah! Tarzan in big trouble! Tarzan burn down village of Lumbagos!

TARZAN: I didn't burn down your village!

CHIEF: We put Tarzan in cobra pit. If Tarzan speak truth, cobra will not kill!

TARZAN: Cobra pit? Isn't it enough if I say, "Cross my heart and hope to die?"

COLONEL: What are you afraid of, Tarzan? I've heard that you're the friend of a million jungle animals!

TARZAN: I am! Unfortunately, there are a million and a half in this jungle! Besides, it was probably you who burned this village.

COLONEL: Maybe! But how are you going to prove it?

TARZAN: With my knowledge of the jungle, it would be easy to follow footprints, search for matches and gasoline in your tent, investigate ashes ...

COLONEL: Resorting to evidence, eh? The 'oldest trick in the book! But it won't work among these savages! They believe in the judgment of the cobra! So into the pit!

TARZAN: What are you going to do with the boy?

CHIEF: He stay tied up! Any friend of Tarzan's no friend of ours!

TARZAN: That's unfair! Why not put the kid in with the cobra and tie me up to the tree?

JIVE: Tarzan! How can you talk like that! I've been at your side every waking moment for the past nine years!

TARZAN: Which is precisely why I'm talking like this!

CHIEF: Enough! Into the pit! (Tarzan exits.)

NARRATOR: Once in the pit, our fearless hero gains the friendship of the cobra, once more proving that all jungle animals love Tarzan. (Tarzan enters with snake over shoulder.)

CHIEF: Ancient tribal code say, since Tarzan make friend with cobra, Tarzan must be telling truth!

COLONEL: Hold on, Chief! I wanted Tarzan to help me trap elephants for ivory! But I don't need him! Your tribe can help me instead! Follow my orders and I'll make you rich!

CHIEF: However, modern tribal code say, since you offer us good deal, ancient tribal code don't stand a chance! We follow!

TARZAN: Don't do it, Chief! Don't you see this man's intentions are dubious, insidious, and furtive?!

COLONEL: And my first order as your leader is to kill the loinclothed Noah Webster!

TARZAN: Stop! After years of companionship and understanding, you can't kill me like that! You aren't that savage!

CHIEF: Right! We must repay him for his kindness! Count to five ... then kill!

NARRATOR: Tarzan, realizing that he is doomed, proceeds to bellow out one of his famous earsplitting jungle cries . . . this momentarily deafens those around him, enabling him to flee to freedom among the familiar jungle surroundings. (Tarzan flees.)

COLONEL: Well, Jive! It looks like your friend Tarzan isn't coming back to help you! Any last requests?

JIVE: Yes! Would you please remove my draft card from my pocket before you light the fire? I don't want to get into trouble for burning my draft card.

TARZAN: (Spying on the Colonel) Now to see what Colonel Grub is up to! Holy ant hills! They're going to burn Jive at the stake! If I didn't have laundry to do I'd rescue him! Wait a minute! Jive does my laundry! Darn! Now I've got to save him! (Tarzan unsheathes his knife and enters to confront the Colonel) O.K., Colonel! Drop the gun!

CHIEF: O.K., Tarzan! Drop the knife!

COLONEL: You'll be sorry you came back, Tarzan! O.K., Chief! Run him through!

TARZAN: Wait, Chief! I appeal to you!

CHIEF: Sorry! Tarzan do not appeal to me! Not even in that miniskirt!

TENDERBELLY: (Tenderbelly enters) Wait! Stop! Spare Tarzan's life! Kill me instead!

TARZAN: Tenderbelly! You're the Chief's daughter! Why do you want to save my life!

TENDERBELLY: Because Tarzan teach me how to love, kiss, and make out!

TARZAN: Tenderbelly! Please! Don't say another word!

TENDERBELLY: Tenderbelly's big heart say Tarzan must live!

TARZAN: Yeah ... but Tenderbelly's big mouth say Tarzan must die.

CHIEF: Enough fooling around! We settle this mess with big fight to finish! If Tarzan loses and is killed, then he must be put to death!

TARZAN: Your sentence structure is a trifle redundant, Chief! Grammatically speaking the proper phrasing should be ...

CHIEF: Hold your filthy tongue in front of the maiden! Have you no respect for an innocent girl? The iron tooth will show the truth!

TARZAN: You mean that knife will decide my life?!

COLONEL: Enough dumb rhyme! You're wasting time! (Tenderbelly shoots the Colonel.)

TENDERBELLY: The job is done! I used the gun!

CHIEF: One more poem and I go home!

TARZAN: Tenderbelly! How could you kill him like that?

TENDERBELLY: I knew you couldn't! You too chicken! Besides, after you spare him, he turn around and stab you in back!

CHIEF: Tenderbelly speak the truth! I was blinded by promises of wealth! But now, Colonel Grub is dead, and Tarzan lives! Tarzan do another show next week! And week after that! And summer reruns! Chief no fool! He know which side of bread to butter up! (Chief exits.)

JIVE: (Jive enters, running) Tarzan, I'm free! They set me free!

TARZAN: Well, I can console myself with the knowledge that there will always be other villains willing to kill a kid!

JIVE: What can I do to repay you for saving my life?

TARZAN: Just a simple token of appreciation will be enough! Like a whalebone slingshot!

JIVE: But the nearest whales are millions of miles from here ... in the Arctic!

TARZAN: Dress warmly, kid! As for you, Tenderbelly ... I think we should continue your lessons! (Tarzan and Tenderbelly exit.)

NARRATOR: So as Tarzan and Tenderbelly frolic through the underbrush together, we come to the end of tonight's [today’s] episode of ... TARZAN!
```

---

## IC-1065: Trigger Mortis, Frontier Mortician

- Title: Trigger Mortis, Frontier Mortician
- Author (byline): Wayne Rice and Mike Yaconelli (eds)
- Work: The Greatest Skits on Earth, Pgs 146-151
- Publisher: Zondervan
- Publication date as stated: March 1986
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR 2, NARRATOR 1, ACTOR 1, SAM, PIE, JOE, ARNIE, TRIG
- Teaser before the introduction: Yes
- Spoken words (computed): 1889
- Already set (do not supply): none

### Source block (context only)

```text
Author: Wayne Rice and Mike Yaconelli (eds)
Book: The Greatest Skits on Earth, Pgs 146-151
ISBN: 978-0310351412
Publisher: Zondervan
Date (Month/Year): March 1986
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Trigger Mortis, Frontier Mortician ACTOR 2: by Wayne Rice and Mike Yaconelli (eds)
```

### Performance text (classify this)

```text
Originally attributed to Warren W. Wiersbe

Suggested Roles: Actor 1: Narrator 1, Sam, Arnie

Actor 2: Narrator 2, Pie, Joe, Trig

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

NARRATOR 2: (Pgs 146-151) The makers of Fatrical present Frontier Mortician!

NARRATOR 2: Are you skinny and run down?

NARRATOR 1: Are you so thin you have to wear skis in the bathroom to keep from going down the drain?

NARRATOR 2: When you turn sideways and stick out your tongue do you look like a zipper?

NARRATOR 1: When you drink strawberry pop, do you look like a thermometer?

NARRATOR 2: Then you need Fatrical—the drink that adds weight to you.

NARRATOR 1: Fatrical is not a capsule. It is not a solid. It is not a liquid. It’s a gas that you inhale. Fatrical comes in one delicious gas flavor – mustard.

NARRATOR 2: It costs only $4.95 a case and the equipment for inhaling it costs only $5,678. This includes a 5,000-cubic foot tank, 400 feet of hose, three pumps, two filter tips, and a partridge in a pear tree.

ACTOR 1: Originally attributed to Warren W Wiersbe

NARRATOR 1: Now for our story. The Adventures of Trigger Mortis, Frontier Mortician.

NARRATOR 2: The scene opens in the residence of Sam Alamode, a wealthy rancher and owner of the Bar-B-Q Ranch in Sparerib, Texas. Sam is dying and is talking to his lovely daughter, Piney Alamode, whom he lovingly calls pie.

SAM: Pie, honey, I’m dying again. Go tell Trigger Mortis, the frontier mortician. Have hearse will travel.

PIE: What’s wrong with you, Daddy? What is your ailment?

SAM: I swallowed the thermometer and I’m dying by degrees.

PIE: I’ll go call Trigger Mortis right away.

NARRATOR 1: Unknown to Sam Alamode, his head foreman, Joe Silver, is hiding outside listening to the conversation. He’s a full-blooded native American-Indian and Sam always calls him his faithful Indian companion Silver. Sam doesn’t hear Joe speak.

JOE: Let old Sam die. I wish he would. Then I can get the ranch and be set for life. He’s always got some fool disease. Last week he swallowed a dynamite cap and his hair came out in bangs. Before that he swallowed a hydrogen bomb and had atomic ache. He’s suffering from flower disease—he’s a blooming idiot. Hey, here comes Pie Alamode’s stupid boyfriend, Arnie. Poor kid. He’s an orphan. Little orphan Arnie. I’ll just sneak away.

ARNIE: I haven’t seen my girlfriend, Pie Alamode, for two weeks. Boy, she has lovely eyes. One is brown and the other two are blue. Last time I was here she rolled her eyes at me and I picked them up and rolled them back. I remember the first time she kissed me. It made chills go up and down my spine. Then I found out her Popsicle was leaking. I’ll knock at the door. (Knocks)

PIE: Who is it?

ARNIE: It’s me, honey. And I call you honey because you have hives.

PIE: Oh, my cookie. I call you cookie because you’re so crummy.

NARRATOR 1: We interrupt this love scene to bring you a message from Peter Pan Makeup.

NARRATOR 2: Use Peter Pan before your pan peters out. This is the makeup used by the stars:

NARRATOR 1: Lassie, Gentle Ben, Phyllis Diller.

NARRATOR 2: Listen to this letter from Mrs. Mergatroid Fluglehorn from Liverlip, Mississippi:

NARRATOR 1: “My face was so wrinkled I had to screw my hat on. Then I used Peter Pan Makeup and I don’t look like an old woman anymore. I look like an old man. I had my wrinkles tightened up and now every time I raise my eyebrows I pull up my socks. I give all the credit to Peter Pan.” Use Peter Pan and you can be beautiful too.

NARRATOR 1: Now back to Frontier Mortician—Trigger Mortis, the frontier mortician, is answering his telephone.

TRIG: Oh, it’s you, Miss Pie Alamode. You want me to come to see your father? Well, my hearse has been giving me trouble—I think I blew a casket. I’ve got to quit using embalming fluid in the gas tank—the motor keeps dying. Yes…yes…well, I have to finish my breakfast. I’m eating Shrouded Wheat and Ghost Toasties…Well, I’ll hurry right out. Goodbye. I must be shoveling off.

NARRATOR 1: Pie Alamode hangs up and goes to meet her lover, little orphan Arnie, in their favorite meeting place, the family graveyard.

PIE: It’s so romantic here in the graveyard. There’s the grave of my Uncle Earnest. Look…there are some maggots making love in dead earnest.

ARNIE: Darling, may I have your hand in marriage?

PIE: My hand? Oh, yes. In fact, you can have my arm too.

ARNIE: Here, I’ll put this ring on your finger.

PIE: Awwww, your face it turning red.

ARNIE: Yeah, and your finger’s turning green. After all, we’ve been going together for twelve years now.

PIE: So what do you want—a pension? Let’s go tell my father.

NARRATOR 2: This program is brought to you by the Double Insanity Insurance Company.

NARRATOR 1: Mothers, do you have children? Then protect them with a double deal policy.

NARRATOR 2: We pay $100,00 if your son is killed by a herd of white elephants going east on Thursday.

NARRATOR 1: If you lose an arm, we help you look for it.

NARRATOR 2: If you get hit in the head, we pay you in one lump sum.

NARRATOR 1: We have double indemnity clause too—if you die in an accident, we bury you twice.

NARRATOR 2: Now a report from the National Safety Council.

NARRATOR 1: It is predicted that 356 people will die in accidents this weekend. So far only 135 have been reported.

NARRATOR 2: Some of you aren’t trying. Now back to our story.

NARRATOR 1: Joe Silver is plotting to kidnap Pie Alamode and hold her for ransom. He thinks Sam Alamode is dying, but he really isn’t. Trigger Mortis, frontier mortician, is on his way to the ranch.

TRIG: Well, here I am. When you’re at death’s door, I’ll pull you through.

SAM: Good to see you, Trigger. Can you give me a good funeral?

TRIG: I’ll give you a good funeral or your mummy back. Could I interest you in our new layaway plan?

SAM: I’m a sick man, a sick man. The doctor told me to drink some medicine after a hot back, and I could hardly finish drinking the bath.

TRIG: You need some of my Whistler’s Mother medicine. One dose and you’re off your rocker.

SAM: Trigger, I can trust you, can’t I?

TRIG: Of corpse, of corpse. Have I ever let you down?

SAM: I don’t trust my faithful Indian companion, Silver. He has a sneaky look.

TRIG: I happen to know, Sam, that Joe Silver wants to kidnap your daughter and keep her from marrying little orphan Arnie.

SAM: Trigger, we gotta do something. Think of a plan.

NARRATOR 2: Will Trigger Mortis think of a plan? While he thinks, a word from Honest John Pendergast, the used car dealer. Honest John has bargains in used cars that you can’t afford to miss.

NARRATOR 1: Here’s an 1887 Essex—this is a revolutionary car. Washington drove it at Valley Forge. The tires are so beat that you not only knock the pedestrians down, you whip them to death. The car has low lines—in fact, it’s so low it doesn’t have doors. It has manhole covers.

NARRATOR 2: This program is also brought to you by Glum, the toothpaste that gives your bad breath the Good Housekeeping seal of approval.

NARRATOR 1: Are your teeth like the Ten Commandments—all broken?

NARRATOR 2: Do you have a Pullman car mouth? One upper and one lower? Then use Glum.

NARRATOR 1: Glum contains eucalyptus oil, flown in from Australia. This eucalyptus oil is the secret of Glum. Millions of users say, “Man, you clipt us.” Be true to your teeth and they will never be false to you.

NARRATOR 2: Now back to Frontier Mortician. Sam, Pie, Arnie and Trigger Mortis are trying to figure out how to get rid of Joe Silver.

SAM: I have a splitting headache.

TRIG: Have your eyes ever been checked?

SAM: No, they’ve always been blue. Trigger, why don’t we put Joe in one of your coffins and ship him out of the state?

TRIG: A tisket, a tasket, I’ll put him in a casket. Listen, Sam, I was in love once, so I know what Arnie and Pie are going through.

PIE: You were in love?

TRIG: I was stuck on a girl who worked in the glue factory. She had a schoolgirl complexion— with diplomas under her eyes. Her lips were like petals—bicycle pedals. Those lips, those teeth, that hair, that eye.

ARNIE: Hey, here comes Joe Silver. Get your coffin ready, Trigger.

PIE: Daddy, lie on the bed and act like you’re dead.

NARRATOR 1: Sam lies on the bed and holds his breath. Trigger takes off his shoes and they all hold their breath. At this breathless moment, we bring you the daily police calls.

NARRATOR 2: Calling car 15, calling car 15—happy birthday, car 15, you are now car 16.

NARRATOR 1: Car 56, car 56, rush to the Bungling Brother’s Circus. The fat woman has hay fever and is crying so much three midgets are about to drown.

NARRATOR 2: Car 23, car 23—return the 10-gallon hat bought for the mayor—he has an 11- gallon head.

NARRATOR 1: Car 19, go to the corner of 6th and Main—the Chinese cook has just committed chop sueycide.

NARRATOR 2: Now back to the story. Joe Silver enters Sam’s bedroom as the others hide.

JOE: So I finally caught you, you scoundrel. You’ve cut my check so many times I have to endorse it with Mercurochrome. I want to marry your daughter, Sam, and nobody’s gonna stop me. Sure I’m tough—I’ve been sent up the river so many times I get fan mail from the salmon. The last time they caught me I got ten years in jail and two in the electric chair. Even when I was a baby people were pinning things on me. Now I’m gonna get you.

SAM: Get him, Arnie!

JOE: Help! Help! You’re mushing me… (muffled sounds)

TRIG: That takes care of him. Now I have to run for a body. A fellow in town swallowed a quart of shellac and died. He had a lovely finish.

ARNIE: How can we thank you? You’ll come to the wedding, won’t you?

TRIG: Yes, I plan to give you a tombstone for a present, but don’t take it for granite.

SAM: Thanks, Trig. By the way, stop over and we’ll play golf someday.

TRIG: Don’t ever play golf with an undertaker—he’s always on top with the last hole. (Sam and Trig exit.)

ARNIE: Now we’re alone, Pie, my love. Someday you’ll have my name.

PIE: I never did find out, what is your last name, Arnie?

ARNIE: My name is Arnie R. Square.

PIE: What a lovely name I’ll have—Mrs. Pie R. Square.

NARRATOR 1: And as the sun sinks slowly in the west, we leave the lovers as they plan their future.

NARRATOR 2: Tune in tomorrow for a new adventure, brought to you by Bleeties, the cereal for old goats.

NARRATOR 2: Bleeties contains 56% iron, 22% copper, 78% steel, 14% bronze and 11% zinc. It doesn’t snap, crack or pop. It lies there and rusts.

NARRATOR 1: Bleeties isn’t the breakfast of champions. It’s for people who just want to get into the semifinals.

NARRATOR 2: In closing, be sure to visit your local dime store where they’re having a monster sale.

NARRATOR 1: Haven’t you always wanted to own your own monster? We have vampires at special prices. They’re excellent for curing tired blood! These are experienced vampires who all work as tellers in blood banks.

NARRATOR 2: Now, tune in tomorrow for the first episode of the new story, “I was a Teenage Spinster,” brought to you by the gardener’s magazine, Weeder’s Digest.
```

---

## IC-1066: Tuesdays with Morrie

- Title: Tuesdays with Morrie
- Author (byline): Mitch Albom
- Work: Not specified
- Publisher: Broadway Books
- Publication date as stated: Oct 1992
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: MITCH, MORRIE
- Teaser before the introduction: Yes
- Spoken words (computed): 2109
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

MITCH: His death sentence came in the summer of 1994. Morrie had amyotrophic lateral sclerosis (ALS), Lou Gehrig’s disease - There was no known cure. ALS is like a lit candle: it melts your nerves and leaves your body a pile of wax. Often, it begins with the legs and works its way up. You lose control of your thigh muscles, so that you cannot support yourself standing. You lose control of your trunk muscles, so that you cannot sit up straight. By the end, you are breathing through a tube in a hole in your throat, while your soul, perfectly awake, is imprisoned inside a limp husk, perhaps able to blink, or cluck a tongue, a man frozen inside his own flesh. This takes no more than five years from the day you contract the disease. Morrie’s doctors guessed he had two years left. Morrie knew it was less.

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

## IC-1067: Visiting Mr. Green

- Title: Visiting Mr. Green
- Author (byline): Jeff Baron
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Jan 1999
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ROSS, MR. GREEN
- Teaser before the introduction: Yes
- Spoken words (computed): 2172
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jeff Baron
2002 National Qualifier
ISBN: 978-0822216810
2010 National Qualifier
Publisher: Dramatists Play Service, Inc.
2015 National Qualifier
Date (Month/Year): Jan 1999
2019 National Qualifier
2021 National Qualifier
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Think about all the divisions in the world.

ACTOR 2: We humans have an inexhaustible capacity to focus on what separates us rather than on what brings us together.

ACTOR 1: Whether it's religion, ethnicity, nationality, race, gender, sexual orientation, or any of the innumerable other ways we classify each other, focusing on the “right and wrong” of differences leads to nothing but fear, separation and conflict.

ACTOR 2: Jeff Baron in his play Visiting Mr. Green addresses many such separations.

ACTOR 1: Ultimately the decisions each person makes are his own.

ACTOR 2: We hope this selection inspires thought, because we have no answers; we won’t identify right or wrong. That decision is up to you.

TOGETHER: Visiting Mr. Green by Jeff Baron
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

## IC-1068: Vivien

- Title: Vivien
- Author (byline): Percy Granger
- Work: Telling Tales: New One-Act Plays (ed Lane, E)
- Publisher: Penguin Books
- Publication date as stated: 0140482377
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: PAUL, VIVIEN
- Teaser before the introduction: Yes
- Spoken words (computed): 1703
- Already set (do not supply): none

### Source block (context only)

```text
Author: Percy Granger
Book: Telling Tales: New One-Act Plays (ed Lane, E)
ISBN: 0140482377
Publisher: Penguin Books
Date (Month/Year): 0140482377
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Paul’s father, Vivien, has been kept medicated and in a maximum security mental institution for the past 30 years.

ACTOR 2: Having only a vague memory of his visiting his father when he was 10 years old and without any assistance from his mother, Paul has finally tracked Vivien down and plans to take him to the opening night of a play he is directing.

ACTOR 1: This scene opens as Paul leaves the hospital’s main office to reunite with his father.

ACTOR 2: The distance between the two and Vivien’s struggle with mental illness makes bridging the father/son gap a formidable task in . . .

TOGETHER: Vivien by Percy Granger
```

### Performance text (classify this)

```text
(A man sits on a bench, his mouth is slack and his eyes are glazed. He stops. No movement. A younger man enters. He stops and peers at the seated figure.)

PAUL: Dad? (No response; the man does not look at him.) Dad? It's Paul. (No response.) Dad. . . Mr. Howard. . . Vivien? (Vivien looks at him.) Hi. (No response.) You been waiting long? (No response.) I'm sorry about the rain.

VIVIEN: (looking away): Weather doesn't bother me.

PAUL: Are you all set to go? (No response. Paul takes a step forward.) Can I give you a hand?

VIVIEN: Keep your distance.

PAUL: What's the matter?

VIVIEN: I'm not going with you. You're not Paul.

PAUL: Yes I am. It's Paul. {Vivien begins to tremble slightly.} Are you cold? Should we get in the car?

VIVIEN: I'm not getting in your car. You're not Paul.

PAUL: Sure I'm Paul. Of course, I'm Paul. It's me. Who else would I be?

VIVIEN: That's your problem.

PAUL: Are you Vivien Howard?

VIVIEN: Yes.

PAUL: I'm Paul Howard, I'm your son. (No response.) I know it's been a long time; I'm just grown up now. It's still me. (No response.) Norristown, you remember? It was just like today, it was raining. We sat in the parking lot. Mom went in and got you. You sat in the back seat. You stared at me, do you remember that? It was 1955, I was ten. I was just ten.

VIVIEN: Everyone I know is dead.

PAUL: I spoke to-Mrs. Tedesco. She said you were very excited.

VIVIEN: I'm all right.

PAUL: I mean we made all the arrangements. She said you wanted to go out. (No response.) Look, it's starting to rain again, let's get in the car, okay? It's right over there

VIVIEN: No.

PAUL: Dad, it's after twelve, we've got to go.

VIVIEN: You go on. I'm sorry you drove all this way for nothing.

PAUL: (taking out his wallet): I can prove I'm Paul. There's my driver's license, there's my picture and my name. (Vivien won't look.) Look-I've got credit cards, union cards-I've got identification coming out of my ears!

VIVIEN: Don't show me your private property. Don't show me your private property!

(Pause.)

PAUL: Can I sit down?

VIVIEN: It's a free country.

PAUL: (sits next to him): Paulie? Po? Pooh? I don't remember; what did you call me? (No response.) How are you?

VIVIEN: I can't complain.

PAUL: You look terrific.

VIVIEN: You're not Paul.

PAUL: I am Paul! Why else would I be here?

VIVIEN: I'm supposed to meet Paul here.

PAUL: Okay-here, right? At the bus stop?

VIVIEN: Yes.

PAUL: In front of the buildings?

VIVIEN: Yes.

PAUL: On the bench?

VIVIEN: Yes.

PAUL: Okay, so here we are.

VIVIEN: Here we are.

PAUL: I'm your son.

VIVIEN: Go away. He's late.

PAUL: It's only twelve-fifteen.

VIVIEN: Late! There's going to be hell to pay. You stick around if you want to see some fireworks, mister. When he sees this son of his there's going to be hell to pay! He won't stand for it-he doesn't have to. He's got other recourses. He knows the score. There's a worm of truth there, you don't think so by your expres-sion? You think he's just free?

PAUL: I didn't know where you were, all right? I had to fight with Mom to get her to tell me. I told her I had a right to know.

VIVIEN: I'm sure you're very busy.

PAUL: (in a frenzy): I rented a car, you want to see the papers? Here-see?-that's my signature! That's my handwriting! And look here, I got a letter from my wife, see? It's addressed to me! What else do you want? I know I'm Paul Howard, I paid a lot of money to an analyst to establish that fact! (Vivien looks at him.) So what I hear you saying is you don't want to come with me.

VIVIEN: I'm going to wait for Paul.

PAUL: Well, he won't come because that's me!

VIVIEN: Go away.

PAUL: We were supposed to spend the day together!

VIVIEN: (rising, advancing on Paul): Go away! Scat!

PAUL: Dad

VIVIEN: Shoo!

PAUL: (backing up, frightened): Hey Dad, come on, okay?

VIVIEN: Sssss!

PAUL: Take it easy

VIVIEN: (makes a large gesture with his arms; roars): Aaaaaaaah! (He turns and walks off with a jerky, stiff-legged stride.)

PAUL: (angry): Why'd you say yes then if you didn't want to come? Why'd you make me rent a car and drive all the way down here? Why'd you make me come?! (sullenly) I'm going. I'm sorry it didn't work out.

VIVIEN: You were right about the rain. I'm soaked to the marrow. You look dank too.

PAUL: (grudgingly): Do you want a lift back to your building? (Beat.)

VIVIEN: I've changed my mind.

PAUL: (looks at him; freezes): What?

VIVIEN: I've decided it will be all right to go with you.

PAUL: You have? Do you think you should?

VIVIEN: I think I can trust you. (taking a pass from his pocket): Here's my pass. We need to show it to the guard at the gate.

PAUL: This rain's going to make it tough.

VIVIEN: So much the better. (Paul, not knowing what else to do, takes the pass and puts the car in motion. After a few awkward moments of silence he nods out the window.)

PAUL: Are you sure you feel up to this?

VIVIEN: (excitedly): There's the gate! (In a conspiratorial tone.) Act normal. Don't worry about me, I'll sit still so they can't see me. I'm still pretty good at that.

(Paul, more nervous than ever, brings the car to a halt by the gate, rolls down the window and shows the pass. Vivien sits rigidly but his face is fairly bursting with excitement; out of the side of his mouth to Paul) Go! go! (Startled, Paul accelerates. Vivien clenches his fists and rocks slightly.)

PAUL: It's just that I'm a little nervous. The critics are coming tonight. They don't count for much out here but still-(He breaks off because Vivien has taken the pass and is slowly, triumphantly, tearing it up.)

VIVIEN: Paul will sure be surprised when he shows up and I'm not there. (Paul stops the car abruptly.) What's the matter?

PAUL: Who am I?

VIVIEN: We met at the bus stop.

PAUL: What's my name?

VIVIEN: We had a long talk.

PAUL: We're not going anywhere until you admit who I am.

VIVIEN: You want me to get out?

PAUL: No! Who am I?

VIVIEN: The little lost sheep.

PAUL: Dad

VIVIEN: We're going to a play, is that right? I've been to a play before. They did a lopped-off Shakespeare for our benefit once.

PAUL: You want me to tell you about it?

VIVIEN: I remember it pretty well.

PAUL: I mean the one we're going to now.

VIVIEN: Oh. Just a little bit. But not the ending.

PAUL: It's called The Seagull. It's about a group of people living in a summer house in Russia about 1890.

VIVIEN: I have to go to the bathroom.

PAUL: What? (No response; Vivien's face contorts.) You do? (No response.) Badly?

VIVIEN: I don't know yet.

PAUL: Can you hold it? If we stop we'll be late.

VIVIEN: I think I can do something with it. (He lifts off the seat slightly and grunts ambiguously. Then he sits back. Pause.)

PAUL: Wha-ah, what'd you do?

VIVIEN: I got it, don't worry. (to himself): I'm not going to drop my trousers on an Interstate.

PAUL: Jesus! Look, why don't I just turn on the radio, okay? You can listen to some music, would you like that?

VIVIEN: If you think it would help. (Paul, chagrined, does not turn it on. They drive in silence several moments.) There's another motel. Are we going to check into a motel tonight?

PAUL: No.

VIVIEN: I'm not going back.

PAUL: What? Of course you are.

VIVIEN: Who told you I was going back?

PAUL: You have to be back by

VIVIEN: I don't have to do anything, you got that, mister?

PAUL: But I promised I'd bring you back, that was the deal.

VIVIEN: You can't. There'd be reprisals.

PAUL: Reprisals?

VIVIEN: Yes.

PAUL: What do you mean?

VIVIEN: There would.

PAUL: Against whom?

VIVIEN: Me.

PAUL: Why?

VIVIEN: I was trying to change doctors; they don't like that. My current doctor is old and cynical; he doesn't have anything to lose anymore. I'd written three letters to a new Jamaican doctor named Sohkey. He acts like he hasn't received them. If he's been forced to show them to the authorities he's curtains.

PAUL: Can't you talk to Miss Tendesco? She seems reasonable.

VIVIEN: She puts on a good show for the outsiders because we're her bread and butter, but in her heart of hearts she's a leopard.

PAUL: How would you live?

VIVIEN: I'll forage.

PAUL: What about your medication?

VIVIEN: I don't need it. I'm always okay once I get away from that place.

PAUL: Where would you go?

VIVIEN: Back to veterinary school. I'll get some clothing to improve my appearance. Professor Milton Dornhoffer said there'd always be a place for me.

PAUL: Have you written to him? (Beat.)

VIVIEN: I don't want to talk about it with you. (He begins to rock back and forth violently; Paul clutches the steering wheel with both hands.) I'm tired of being in this car with you. I don't have enough room. Stop.

PAUL: I can't.

VIVIEN: I want to get out.

PAUL: It's raining.

VIVIEN: I'll be all right.

PAUL: We're going too fast.

VIVIEN: I want to get out.

PAUL: No. This is our day together.

VIVIEN: I don't make deals, mister.

PAUL: I'm not letting you out of this car.

VIVIEN: If you love me you won't take me back. (Pause.)

PAUL: I have to take you back. I'm sorry. . . (Pause.)

VIVIEN: It's stopped raining. (Paul nods. Vivien leans forward and gazes up at the sky) This is a good place to be for rainbows too. (Brief pause; Vivien indicates the pad and the windshield.) I used to sit like this with my father. He let me sit beside him in the front seat and keep the windshield clean.

PAUL: Were you close to him?

VIVIEN: (grins): "Cheek by jowl." He used to take me on long trips. We went to the Chicago World's Fair-"The Century of Progress" they were still calling it then-and Florida, and Michigan. Ocean Boulevard. . . Once we drove all the way to New Mexico. My mother had to sit in the back seat.

PAUL: What did he do for a living?

VIVIEN: He operated a steam shovel, dredged the Mississippi. Oh yeah. We were river rats. Played poker, ate ice cream, drank whiskey, rented rooms. . . . He took us everywhere.

PAUL: What was his name?

VIVIEN: Edgar.

PAUL: What was your mother's name? (Pause. Vivien's brow furrows. He does not want to talk about her.)

VIVIEN: Dougal. (Beat.)

PAUL: It's just that Mom never told me anything about you. The only thing I ever remember her saying was once that you liked the out-of-doors.

VIVIEN: That's right. I could disappear for days into the mountains and no one would know where I was. Bang! I'm gone. I was alone on a mountain one day when I made a discovery. If I stared long enough at the landscape and sat very still, I could blend in with it. I could disappear. The forest animals would go on about their business as if I wasn't there. And the birds would sing different songs, not the ones they sang when people were around. I was no one and that made me special.

PAUL: Sounds wonderful.

VIVIEN: The trouble was when I started doing it around the house. (Pause.) I don't do it anymore now. You get more conservative with age.

PAUL: Were you really studying to be a veterinarian? (No response.) How-how did you and Mom meet?

VIVIEN: I was in charge of the pets at the college. There weren't supposed to be any. She had a cat. (Pause. A look of pain crosses his face.) The confiscated animals were sent to the labs. (Pause.) She never told you even that?

PAUL: (shakes his head; inaudibly): No.

VIVIEN: She's very strong-minded, isn't she? (Paul, unable to speak, just nods.) Well I let her keep that cat I'll tell, you. The next thing you know she invited me home to meet her father. He was pretty imposing too, ate good food. She hoped he wouldn't approve but he took a shine to me because of my prospects which weren't bad. So I went along with it. (Pause.) Recently I've been interested in suspended animation, freezing people until you can find a cure for them. I think that's a good idea. (Pause.)

PAUL: Was it Mom- Was she the one who took you to Norristown?

VIVIEN: (with great difficulty): ... No. I went of my own free will.

PAUL: Why? (Vivien tries to respond; cannot.) I wish you'd tried, you know? I wish you'd tried harder. (Long silence. Finally Vivien looks out the window.)
```

---

## IC-1069: Wigfield

- Title: Wigfield
- Author (byline): Amy Sedaris, Paul Direlio and Stephen Colbert
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: SUGGESTED ROLES, ACTOR 1, ACTOR 2, RUSSELL HOKES, HOYT GEIN, CHARLES HALSTEAD, BURCHAL SAWYER, FLEET HOLLINGER, FARBER, JUDGE, FLEET, JUDGE COLEMAN
- Teaser before the introduction: Yes
- Spoken words (computed): 2130
- Already set (do not supply): none

### Source block (context only)

```text
(none)
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 2: Today you’ll hear personal accounts from the chief of police, 3 self-declared mayors; and an elected government official who will provide a snapshot of “small town”America – which I’m sure you will come to realize is more than “just a little ditty ‘bout Jack and Diane.”

TOGETHER: Wigfield by Amy Sedaris, Paul Direlio and Stephen Colbert.
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

SUGGESTED ROLES:

ACTOR 1: Russell Hokes, Charles Halstead, Judge, Bill Farber

ACTOR 2: Hoyt Gein, Burchal Sawyer, Fleet Hollinger and Bill Farber

RUSSELL HOKES: Welcome to Wigfield. Population: vague. Driven by the government’s recent threat to destroy the local dam, and with it the self-described “town” of Wigfield, residents must race against the clock. The real question: Is Wigfield merely posing as a town in order to collect federal disaster relief?

RUSSELL HOKES: Wigfield is a quarter-mile stretch of highway known as Wigfield. As is the case with many small towns, Wigfield is totally isolated, with the exception of the four-lane interstate that runs parallel to its Main (and only) Street.

I walked down the road staring into the shops, searching for something in this town to tell me its story. I read the signs hanging in the storefront windows: DAM BEING TORN DOWN SALE! EVERYTHING MUST GO BEFORE THE DAM IS TORN DOWN AND TOWN IS DESTROYED!

Wigfield is endangered! I decide to let the town residents tell their story in their own words . . . . I set forth to meet the People of Wigfield.

************

HOYT GEIN: I’m Hoyt Gein, the police chief under Charles Halstead, who is the legitimately self-declared may or Wigfield. I know some townspeople have criticized Mayor Halstead for appointing me chief of police, given my arson arrest record, but come on now, that’s just ludicrous. I can stop lighting fires anytime I want. Yes, I occasionally start fires when I’m out at a social event, but so what? Who doesn’t? It’s a free country.

Fleet Hollinger thought he could force me out . . . he’ll hold an election, and just because he’s the most powerful man in town, he’ll get elected. Well, that not the way things work. A curious electrical fire at the polling station saw to that. It turns out it’s pretty hard to exercise your right to vote when you’re on fire. Case closed. In the confusion, the town ended up with three mayors.

Maybe saving a little town like Wigfield isn’t important to most people, but it’s important to me. I know most people don’t cotton to small towns,. Like lemmings, they follow everyone else to the cities, where they can find jobs, housing, and culture. But in Wigfield we march to is the beat of our hearts. You scrape away the unemployment, the unsolved murders, or even the contaminated topsoil, and what you’ll find is the giant swollen heart of America.

RUSSELL HOKES: And then Hoyt demanded that I follow him out to his camper van. Any doubt I had as to his official capacity was dispelled by the words “Wigfield’s Police Chief” stenciled on the side. Throwing open the rear cargo door with a flourish, he proudly displayed a man win his early forties who was elaborately seat-belted into a lawn chair. According to Hoyt, this cheerfully disheveled man was Mayor Charles Halstead, who had insisted on meeting me.

CHARLES HALSTEAD: I like fudge. I have a briefcase. I keep my fudge in there. I’m not from here, but I live here now. I came to this town to represent the lead dispersal plant. The government wanted to close it because they said it was retarding the employees. I got a court order that allowed me to stay at the plant so I could disprove firsthand the effects of the plant. After I lost the case, I decided to stay in Wigfield. I don’t know why. I like fudge. Guess what I have in my briefcase. I’m one of the mayors. I hope they don’t tear down the dam. My fudge would get wet.

RUSSELL HOKES: I knew now that a vital part of this story was the mayor. All three of him. I had met one, but I knew that some more of them were out there. My search quickly led me to the business establishment of Mayor Burchal Sawyer. We met in his vast junkyard.

BURCHAL SAWYER: I’m the great American success story. One day you’re livin’ out of your car, the next you’re livin’ out of your car, and you’re the mayor of a town. That’s because I make things happen.

Listen to this. Fleet Hollinger tried to tell me that I couldn’t run for mayor of this town because I didn’t have a residence. I was livin’ in my car at the time. Then he gets his [shorts] all in a bunch just ‘cause I didn’t have any identification.

I know who I am. I don’t need fingerprints to prove it. Plus, he says that I’m not educated, and that’s a crock. Look, last time I checked this was a free country.

Speaking of which, as one of the mayors, I feel I should chime in about this dam business. On the record, my official reaction is this: Why would the state want to tear our dam down? It just doesn’t make any sense: flooding a river bed? What kind of logic is that? You think just because I’m used to livin’ in my car it will be easy for me to pull up stakes and drive to another place? But again, if it’s got to come down, well then, I say, as a community we prepare ourselves for the horrifying loss we must endure, and on behalf of the town I accept my relocation money graciously.

RUSSELL HOKES: This only left Fleet Hollinger to complete the trifecta of local leadership. Logic said his home. A series of double and singlewide trailers had been hauled into an impressive maze of aluminum and connected in a haphazard fashion with sheet metal and button rivets. Clearly this was the home of an important man.

FLEET HOLLINGER: I’m a simple man in a simple town. Small towns are built on old-time values. Friendliness, openness, trust. That’s what I’m all about. Besides the used car lot, I also own Fleet’s Used Auto Parts – the oldest business in Wigfield. Another business I run is Mack (M-A-C-K) Donalds. The only and the best fast-food chain in Wigfield. As we speak, a large hamburger chain is trying to shut me down. All I know is my middle name is Donald and my nickname is Mack because this guy I know dries a truck. It seemed natural to me that a clown would be the mascot. How can they have a lock on that? When you think of hamburgers, you think of cows, cows make you think of bullfights, and who distracts the bulls?

Clowns! I named the clown after my nephew Ronald. I wouldn’t be surprised if that unnamed hamburger chain is involved in this whole dam thing.

Along with being a respected businessman, I’m also the mayor. Now, I’m sure the government sees us as a bunch of squatters who gradually accumulated at the bottom of a newly dry riverbed. But we will battle tirelessly to keep our town, and nothing will deter us!

RUSSELL HOKES: Through my many interviews with the mayors of Wigfield a story was starting to shape up. But my journalistic sense of fair play told me that Representative Bill Farber deserved the chance to give his side of the story. I decided to track him down.

FARBER: First of all, Wigfield isn’t a town. These people are living here illegally. Half of those people don’t have social security numbers. They don’t even have a zip code. They don’t pay any taxes. They’re outside of any health care system or school district. But even though they have built illegally on land that belongs to the state, we are willing to discuss a nominal relocation fee. The state will not recognize this place as a town.

RUSSELL HOKES: Well, I guess that will all be settled today in court.

******

JUDGE: Be seated. We have a motion filed by the town of Wigfield. At this time the plaintiffs can make their opening statement.

FLEET: You Honor, or scenic little town is nestled quaintly in the shadow of the Bulkwaller Dam. Our tiny little hamlet will soon be washed away by the cold, unforgiving waters of the so-called Fresh Springs River. I call Eminent Domain! If residents are relocated by the state, they must be financially compensated for both home and property. The pain is immeasurable, as should be our compensation.

FARBER: Your Honor, eminent domain only applies to legally occupied incorporated towns. There is no precedent for payment to what really amounts t o illegal squatters, no matter how many mayors they claim to have.

FLEET: How dare you?! Are you suggesting that we are merely posing as a town in order to get money when the dam is torn down?

RUSSELL HOKES: Your Honor, my name is Russell Hokes. I am a writer. Now perhaps these people don’t possess the necessary legal documents stating they are a town. But I’ll tell you this much, Judge. I have lived with these people for nearly two weeks now. I’ve seen their children play on the mercury mound. I think I can say with great confidence that if Wigfield is not a town, then I am not a writer.

JUDGE COLEMAN: I’m going to take this matter under consideration. The demolition of Bulkwaller Dam is stayed for one month. You will have that one month to prove you are a town. If you can’t prove your township, the dam may come down and the state will have no financial obligation to you whatsoever.

RUSSELL HOKES: At first the town struggled for a solution: 1) Add the words “Town of” to the Wigfield sign. 2) Get a Wigfield sign and 3) Parade!

What better way to prove you are something you are not than to celebrate the very thing that someone says you aren’t! And what better way to celebrate than with a parade?

What happened next is almost impossible to believe. A reporter at one of the big-city papers wrote a human-interest story about the travails of Wigfield. “Small Town Parades to Save Self.” Anyway, somehow that story piqued the interest of other newspapers. Soon, they began showing up in Wigfield. Stories began to spread, and before long crowds began to show up along the parade route.

Representative Farber has informed the town that he would like to address them.

FARBER: Well, ladies and gentlemen, what I have to say is very simple. You win. The state is bowing to public pressure and has decided not to tear down the Bulkwaller Dam.

RUSSELL HOKES: A chant of “where’s our money” rings out from the floor and begins to build

FARBER: I don’t have any money for you, but I do have your new town charter. You should know that among the responsibilities that come with townhood are providing proper sewage, streetlights, a school system . . . well, the list goes on. A tax will have to be levied on the citizens and businesses to pay for all that, of course. You have until the first of the year to initiate these actions.

FLEET: What if we don’t?

FARBER: The town will be dissolved, your property confiscated without compensation, you will be forcibly removed from the area and all town officials, which I might remind you are legally listed as Hollinger, Sawyer, Gein and Halstead will be subject o criminal prosecution. Good day, gentlemen.

*****************

RUSSELL HOKES: Hello, Mr. and Mrs. America, this is Russell Hokes coming to you live from the first annual Wigfield Town Charter Celebration. It’s just about dusk, and I suspect people will begin gearing up for the fireworks display. Hoyt Gein is moving toward the base of the dam carrying fuses, a torch, and other explosive delights. I can only imagine what flaming wonders will emerge from the deep shafts bored directly into the face of the dam.

It’s exploding! It’s exploding! The whole dam is exploding! Oh, the humanity! I can’t talk! I can’t breathe! The dam is a mass of smoking rubble. Water is crashing through the smoking wreckage! The entire town is being submerged!

(5 days later)

Who lived? They all did. In the time that it takes most people to change into their grieving black, the people of Wigfield have bounced back as if their souls were made out of Superballs. The mind reels at the fact that given a disaster of this proportion, almost every member of the town survived, and not only that, they were able to miraculously salvage nearly every possession. God has smiled on these people. Amid all this mournful merriment, one agonizing question remains. What now?

FLEET: Well, here’s the deal. I’ve talked to the boys down at the Federal Emergency Management Agency, and apparently we qualify for disaster relief. The only thing we need in order to get what is justifiably coming to us is this little written account of the tragedy by an impartial third-party witness . .

RUSSELL HOKES: Then is struck me. Third-party account? Why I could be that account! . . . . . [So I leave you with this question]: Was Wigfield merely posing as a town in order to collect federal disaster relief? [The world may never know].
```

---

## IC-1070: Wish Fulfillment

- Title: Wish Fulfillment
- Author (byline): David Simpatico
- Work: Showtime's Act One Festival of One-Act Plays 1994
- Publisher: Smith and Kraus Publishers
- Publication date as stated: Feb 1996
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: FATHER, SON
- Teaser before the introduction: Yes
- Spoken words (computed): 1795
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Simpatico
Book: Showtime's Act One Festival of One-Act Plays 1994
ISBN: 978-1880399965
Publisher: Smith and Kraus Publishers
Date (Month/Year): Feb 1996
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Now more than ever, gays and lesbians are coming out to their parents-and they're doing it when they're quite young.

ACTOR 2: But sometimes it is best to stay in the closet—and here's why.

ACTOR 1: Despite the evidence that Americans are getting more tolerant of gay and lesbian people, some parents still reject their children when they come out— ejecting them from their homes . . .

ACTOR 2: Some even react with violence.

ACTOR 1: Other parents may feel as if their children have died

ACTOR 2: Wish Fulfillment by David Simpatico provides audiences with a wide range of reactions when a son tells his father that he is gay.

ACTOR 1: Where would you fall in this spectrum?

ACTOR 2: How would you react if your son shared this most intimate part of himself with you?

TOGETHER: Wish Fulfillment by David Simpatico.
```

### Performance text (classify this)

```text
ONE The Son rocks. The Father enters holding his drink.

FATHER: Your mother said you wanted to talk to me.

SON: Dad. I got something I need to tell you.

FATHER: What is it.

SON: Mom already knows.

FATHER: What is it.

SON: This is not easy for me.

FATHER: What is it.

SON: Uhm . . . DAD I'M GAY. (They don't move. They stare at each other in tense silence. Slowly, the Father cracks into a mask of tears, sobbing pitifully.) Daddy-

(The Father rises, walks around the chair and starts the scene again.)

TWO The Son rocks. The Father enters holding his drink.

FATHER: Your mother said you wanted to talk to me.

SON: Dad. I got something I need to tell you.

FATHER: What is it.

SON: Mom already knows.

FATHER: What is it.

SON: This is not easy for me.

FATHER: Yes-

SON: Uhml . . . DAD I'M GAY.

FATHER: Is that all? I always thought you might be, ever since you were little. I'm glad you finally feel comfortable enough about your sexuality that you can admit it to yourself Your mother and I just want you to be happy.

SON: Wow.

FATHER: And healthy. Do you practice safe sex?

SON: Absolutely.

FATHER: Well then. As long as you're happy, that's all that matters.

SON: I don't know what to say.

FATHER: You've already said it.

SON: But you're being so cool.

FATHER: Hey now, don't sell your father short. Just because I personally don't ascribe to your sexual orientation, I would never have the pomposity to morally condemn something simply because it is out of the realm of my own personal experience.

SON: Wow. When I grow up, I want to be just like you.

FATHER: I just want you to be happy. Your father loves you. (They are about to embrace, but they start the scene again.)

THREE The Son rocks. The Father enters, holding his drink.

FATHER: Your mother said you wanted to talk to me.

SON: Dad. I got something I need to tell you.

FATHER: What is it.

SON: Mom already knows.

FATHER: What is it.

SON: Uhm ... Dad, I'm gay. (The Father spits out his drink in a violent spume of disbelief, sopping his son with his double scotch. They start the scene again.) FOUR The Son rocks. The Father enters with a new drink.

FATHER: Your mother said you wanted to talk to me.

SON: Dad. I got something I need to tell you.

FATHER: What is it.

SON: Mom already knows.

FATHER: What is it.

SON: This is not easy for me. I mean I - Dad, I'm gay. (The Father's drink dribbles out of his mouth.) Dad- (The Father clutches his heart, suffers a massive coronary, collapses to the floor shaking in agony. The Son races to his father's side, alternately pounding on his chest and giving him mouth-to-mouth) No-Daddy please don't die, it's all my fault, I didn't mean it, I'll change, I was kidding--don't die Daddy please don't die-Daddy please- (With a final horrific shudder, the Father dies.) I'VE KILLED MY FATHER! (He throws himself weeping across his father's corpse. They start the scene again.) FIVE The Son rocks in his chair. The Father enters, holding his drink.

FATHER: Your mother said you wanted to talk to me.

SON: Dad. I got something I need to tell you.

FATHER: What is it.

SON: Mom already knows.

FATHER: What is it.

SON: This is not easy for me. Uhm I. . . . DAD, I'M GAY.

(A tense beat of stillness. Suddenly, the Father takes out a gun. Shoots his son in the head. The Son does a backward tumble out of the chair and shakes in postmortem frenzy. The Father methodically empties the gun into his son's body. They start the scene again.)

SIX The Son rocks. The Father enters, holding his drink.

FATHER: Your mother said you wanted to talk to me.

SON: Dad. I got something I need to tell you.

FATHER: What is it.

SON: Mom already knows.

FATHER: What is it.

SON: It's hard, Dad. . . . What I have to tell you.

FATHER: WHAT IS IT!

SON: Can you please stop yelling at me-

FATHER: I AM NOT YELLING--

SON: YES YOU ARE TOO YOU'RE ALWAYS YELLING I CAN'T STAND IT ANYMORE JUST STOP YELLING FOR CHRIST'S SAKE--

FATHER: What the hell did you want to tell me already--

SON: NONE OF YOUR STUPID BUSINESS OK, GET OFF MY BACK AND LEAVE ME ALONE ALL YOU EVER DO IS YELL AT ME MY WHOLE LIFE WHY CAN'T WE JUST TALK --

FATHER: DON'T YOU EVER TALK TO YOUR FATHER LIKE THAT, I DON'T CARE HOW BIG YOU ARE I AM STILL YOUR FATHER DO YOU UNDERSTAND ME (Slaps him.) DO YOU UNDERSTAND ME (Slaps him.) DO YOU UNDERSTAND ME

(Slaps him.) (The Son shakes his head "Yes”) (Gently.) Now what did you want to tell me? (They start the scene again.)

SEVEN The Son rocks. The Father enters, holding his drink.

FATHER: Your mother said you wanted to talk to me.

SON: Dad. I got something I need to tell you.

FATHER: What is it?

SON: I love you Dad.

FATHER: What did you want to talk about?

SON: Do you love me?

FATHER: Is this what you wanted to talk about?

SON: Do you love me, Dad?

FATHER: I'm your father. Yes, I love you.

SON: No matter what.

FATHER: What is it?

SON: Well, Dad, I'm gay. (Silence.)

FATHER: I don't want to hear this. (They start the scene again.) EIGHT The Son rocks. The Father enters, holding his drink.

FATHER: Your mother said you wanted to talk to me.

SON: Dad, I'm gay.

FATHER: I don't want to hear this.

SON: Well I am. I'm gay.

FATHER: I don't want to hear this. You just told me the worst thing in the world.

SON: Thanks Dad. You still love me?

FATHER: Don't ask me that like I'm on trial here.

SON: It's a simple question.

FATHER: You just threw a brick in my face.

SON: Do you still love me?

FATHER: You will always be a part of this family, but in my honest opinion, you belong on the other side of the street in the gutter with the freaks.

SON: So I'm a freak.

FATHER: You're being honest, I'm being honest.

SON: You just called your son a freak.

FATHER: You don't like the truth.

SON: You just threw a brick in my face.

FATHER: Truth hurts don't it.

SON: Do you still love me?

FATHER: You're my son.

SON: I thought I was a freak. (They start the scene again.) NINE The Son rocks. The Father enters, holding his drink.

FATHER: Your mother said you wanted to talk to me.

SON: I'm gay Dad.

FATHER: You can get help you know. (They start the scene again.) TEN The Son rocks. The Father enters.

FATHER: Your mother said you wanted to talk to me.

SON: Dad. I got something I need to tell you.

FATHER: What is it.

SON: Mom already knows.

FATHER: What is it.

SON: This is not easy for me.

FATHER: You can tell me I'm your father. I love you.

SON: Well Dad I'm gay.

FATHER: I'm sorry, what?

SON: I said I'm gay.

FATHER: As in Homosexual.

SON: As in Homosexual. (They jump up, face off.)

FATHER: I thought I knew you.

SON: You do know me. Now you know.

FATHER: No I don't.

SON: Why because I'm gay?

FATHER: No, because you're a goddamn freak that's gonna wind up dead in the gutter at the end of a two-by-four because someday soon you're gonna pinch the wrong behind and he's gonna turn around and rip the eye right outta your friggen head and I hope to God I'm there to see it, goddamn AIDS carrier- (Swings, wings his son.)

SON: I am not an AIDS carrier-

FATHER: You’re a goddamn faggot is what you are and all faggots are AIDS carriers-

(Slams, just missing his son's skull.)

SON: I knew you'd be upset.

FATHER: How the hell are you gonna be happy

SON: How is anyone happy . . . how are you happy-

FATHER: Oh but I am not happy. (Swing and a miss.) I used to think I was happy but see I used to think I kinda knew my son, (Swing and a miss.) I used to think I had something in common with the boy I raised. (Swing and a miss.) I used to think I could teach him something and maybe someday see a little part of me growing up inside of him.

SON: There's a lot of you in me.

FATHER: Don't tell me that!- (Swings, knocking his son to the floor.) I never even suspected-

SON: (Slowly rising.) So what were you seeing? I mean I'm lost here, Dad, if me telling you that I'm gay changes everything, then what was there before that's going to change. You're letting one part of who I am completely change who I was so tell me, really, who was I, who were you seeing all that time that you don't see now-

FATHER: I gotta be honest I got no idea and that's what scares me it's like I'm looking at a big blank like the past twenty years means nothing like all the sweat and blood and worry I put into raising you means nothing like you're spitting in my face and telling me it's all my fault and I should smile and accept and I am sorry kiddo but just because you got my blood in your veins don't mean I got to stand back watchin’ while you piss on everything I built my life around-I am telling you I will not accept!

SON: (Approaching him.) Daddy-

FATHER: I WILL NOT ACCEPT - I am so humiliated my whole life means nothing without a son I can't be a father so who the hell am I and who are you I want my son back and it's all my fault (They start the scene again.) ELEVEN The Son rocks. The Father enters.

FATHER: Your mother said you wanted to talk to--

SON: You stopped loving me when I was three years old and you came home from work and I ran up and hugged your legs because I was so happy to see Daddy because Daddy was so big and so strong and so tall and Daddy always brought home a candy bar hiding in his pocket and so I grabbed it but instead I grabbed *you* didn't I, Daddy, and you knocked me down and beat me black-and-blue didn't you Daddy because I was three years old and I had to learn never to touch another man because it was sick and bad and from that second on you wouldn't even let me hug you because you wanted me to be normal and well-adjusted so you kept pushing me away and pushing me away because you were too scared to let me hug you again -

FATHER: I was just trying to be a good father-

SON: You think this is easy for me-

FATHER: How are you gonna be happy-

SON: How is anyone happy how are you happy-

FATHER: Oh but I am not happy.

SON: Well neither am I. I'm looking back on my life and all I see is a big blank, I don't know who you are Dad what did we ever talk about I can't remember and I want my father back because I feel like I wasn't there, like I was always pretending, sitting around smiling and being the good boy and all the time about to explode with a deep dark perverted secret that no one could understand and made me a freak in the eyes of God and so I became a freak and lived like a freak and treated myself like a freak so I could live up to your expectations drowning in the sewer but I can't live by your rules anymore because I am exploding now and I can't stop and I want my life back and I want to be happy because I am not a freak, Daddy, do you understand me, I am not a freak-

FATHER: It's all my fault-

SON: t's nobody's fault Dad It's not good and it's not bad, it just is-and it is about me, it is not about you-stop being so self-centered and think about what I'm telling you and what I'm going through because I am the one who is going through it, not you, and I need love right now . . . understand, I need love-

FATHER: I wanted to teach you how to fight.

SON: Well you did a good job because that's all I know how to do –

FATHER: (Feebly on his knees.) Your father loves you-

SON: NO . . . I don't know who you are-I have no father. I have only myself. (They
start the scene again.)
TWELVE
The Son rocks in his chair. The Father enters, holding his drink.

FATHER: Your mother said you wanted to talk to me. (Silence. They say nothing.)
```

---

## IC-1071: The Women of Lockerbie

- Title: The Women of Lockerbie
- Author (byline): Deborah Brevoort
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: Dec 2005
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: GEORGE, BILL
- Teaser before the introduction: No
- Spoken words (computed): 787
- Already set (do not supply): none

### Source block (context only)

```text
Author: Deborah Brevoort
ISBN: 978-0822220794
Publisher: Dramatists Play Service
Date (Month/Year): Dec 2005
```

### Introduction (context only: never use it for content warnings)

```text
On Wed. Dec. 21, 1988, Pan Am Flight 103 exploded in midair as it traveled from London to New York City. Before it could reach the Atlantic, a timer-activated bomb detonated inside the plane from its hiding spot in a cassette player packed away in a suitcase. The explosion scattered pieces of the plane and the remains of the 243 passengers and 16 crew members over 850 square miles of Lockerbie, Scotland.

Now, seven years later, the women of Lockerbie want to save the articles of clothing that were scattered from the crash, wash them, and return them to the victims’ families. Their act of compassion is challenged by George Jones, a representative from the U.S Government sent to take care of the situation. He has directions to have all of the clothing, stored in a warehouse as evidence, burned due to contamination. The Women of Lockerbie by Deborah Brevoort
```

### Performance text (classify this)

```text
GEORGE: These women are driving me crazy!
Look.
Let me give you a piece of advice about the women of Lockerbie.
Don’t be fooled by the lace on their collars.
Or the flowers on their teacups.
They’re not the sweet little old ladies they appear to be.
They’re tigers.
And they’re ferocious.
You know what they just did?
They called in the television crews!
The networks.
The American networks.
They’re all down at the warehouse
With their reporters
Waiting for a statement from me!

And that’s not all.
There are two hundred women with them!
Two hundred women!
With candles.
They’re trying to create an international incident, these people

BILL: But I thought Lockerbie was already an international incident.

GEORGE: Lockerbie? Hardly!
The world has forgotten all about Lockerbie
They forgot about it two weeks after the crash.
But if those women get it back in the news . . . !
Well, then it will be. And then I’ll never get out of here!

BILL: You don’t like it here?

GEORGE: What’s to like?
Lockerbie is the Siberia of the State Department!
But.
You have to do your time in places like this
Before you get the better assignments.
Me, I’d rather be someplace else.
You know, places like . . .
Kuwait . . .
Tel Aviv . . .
The hot spots.
And if I handle this right, I just might get there.

BILL: Then why are you doing it, if I might ask?

GEORGE: You mean this business with the clothes?

BILL: Yes.

GEORGE: I have orders from Washington.

They want things wrapped up here.
Quickly.
So that’s what I’m doing.
Look. This whole affair has gone on long enough.
These people should just get over it.
It’s been seven years.
I mean . . . move on, for God’s sake.
Get a life!
I’ve tried telling them that,
But of course, they won’t listen.
They sent the mayor to see me.
They sent the bishop, for God’s sake.
Next, they’ll probably send in a mother!
The mothers are the worst.
They come in clutching the baby pictures.
Johnny blowing out the candles on his birthday cake.
Little Timmy smiling with his mouth full of braces.
The mothers will drive you crazy.
There is always a mother who makes it impossible to do your job.

BILL: What about the fathers?

GEORGE: Oh, I have to deal with them too.
But men . . .
Men are different.
Thank God.
You can always reason with a man.
At least they don’t shove those pictures in my face.

(Bill pulls out his wallet and opens it)

What do you have there?

BILL: My son’s school picture from the sixth grade. Smiling. With his mouth full of braces. Look.

(Bill shoves the picture in George’s face).

GEORGE: (Pause) Was your son . . . uh . . . on board?

BILL: Yes

GEORGE: Oh. (Pause) I didn’t know . . .

BILL: His body was never found. He’s still out here somewhere.

GEORGE: (Pause) I’m . . . sorry. (Pause) Um. What was his name?

BILL: Adam. Adam Alexander Livingston.

GEORGE: Oh, yes. Yes. I, h, seem to recall it . . . .

BILL: And here is a picture when he hit a home run. In the Little League. The game was tied and the bases were loaded.

GEORGE: Yeah?

BILL: Yeah! He brought them all home.
And here . . .
Here is the ticket stub
From the Yankee game I took him to on his last birthday.
I just found this a few minutes ago, in the pocket of my coat.
Funny.
I haven’t worn this coat in years.

(Pause)

Mr. Jones. Do you have children?

GEORGE: No. No, I don’t
Don’t have a wife.
Well, I had one.
Had two, actually.
But we never got around to having kids.
You know.

BILL: Then it might be hard for you to understand The loss that a parent feels . . . .

GEORGE: They say there’s nothing worse.

BILL: They’re right. There isn’t. (Pause) See that hill? My wife is on the other side of it.

GEORGE: Doing what?

BILL: Looking for my son’s remains.

GEORGE: (George rolls his eyes and whistles) Women. You know?

BILL: They’re not the only ones who feel loss. Men do too.

GEORGE: Not like that.

BILL: No, not like that.
That’s the difference, I guess . . .
The women show it and the men don’t
And they show it more because we don’t
It’s not fair. Really, now that I think about it.
The women have to do their own crying
And also, the crying for the men . . .

(Pause. He reflects for a moment on this realization).
When Adam died . . .
I cut off the pain.
I had to.
I couldn’t take it.
But then . . .
I didn’t feel anything else either.
Just now
When I was walking these hills
And found this ticket stub from the Yankees,
I felt something.
For the first time in years.

GEORGE: You did, huh?

BILL: Yes.

(Slight pause) Look at this thing.

(He holds up the ticket stub and looks at it with astonishment.)
It’s a piece of paper
A little piece of paper.
Who would have thought
That a
Little
Piece of paper
Like this
Could have that kind of power?

(Pause)

George . . . those clothes aren’t just clothes.
They’re not things.
They have life.
Just like this piece of paper.
Please.
Reconsider your decision.
Release the clothes to the women.
```

---

## IC-1072: The Zoo Story

- Title: The Zoo Story
- Author (byline): Edward Albee
- Work: The American Dream & Zoo Story
- Publisher: Plume
- Publication date as stated: Oct 1997
- Event as filed: Duo Interpretation
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
ACTOR 1: The Zoo Story by Edward Albee is a confrontation between middle-class America and the outcasts of society.

ACTOR 2: Set in central park, Peter, an average American, is confronted by Jerry, a lonely man from the wrong side of the park.

ACTOR 1: Jerry tries to teach Peter the realities of life that Peter has tried to ignore. He tries to teach Peter the nature of human existence and relationships.

ACTOR 2: Through a serious of failed conversations and misinterpretations of the act of love, Jerry begins his experiment to see if the middle class Americas are animals after all.

TOGETHER: The Zoo Story by Edward Albee
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

## IC-1073: Dis-Orientation

- Title: Dis-Orientation
- Author (byline): Robert W. LaVohn
- Work: Dis-Orientation
- Publisher: Mushroom Cloud Press
- Publication date as stated: August 15, 2024
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1526
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
Taylor, a nervous college freshman, stands before a judge.

Taylor: How do I…plead? I plead with great humility, Your Honor, and I may even cry a little!

(a pause)

Oh, to the charges. How do I plead to the charges? I plead not. I mean, I do plead, but I plead not guilty. Well, actually, I am, technically, guilty of the “destruction of property” part, but the public intoxication is entirely a misunderstanding. I was wearing the champagne, not drinking it. And I did not actually assault the officer, either, but I can understand how he might have gotten that idea.

(a pause)

Yes! Absolutely, I can indeed start at the beginning. I have wanted to be a student at Podunkwa University ever since I was little. My dad would take me to all the football games in the fall and–

(a pause)

Right. The beginning of this particular event. If it’s okay, I do have to go back a little farther to the beginning of Orientation Week. See, when the freshmen arrive on campus, they put us in small groups so we can get to know some of the other freshmen better. Build relationships, strengthen community–that sort of thing. I was in a group with Jade and Tim and Murphy and Celia and Marta and Amir, but we call him Little Amir, because one of the guys in charge of the group who’s an upperclassman is also named Amir, so we call him Big Amir and the freshman Little Amir, and–

(a pause)

Yes, absolutely, I just want to establish the context. So, all of the freshmen groups compete in this huge scavenger hunt at the end of the week. It’s a really important event, and Big Amir really wanted to win. And Jade and Tim and Murphy and Celia and Marta and Little Amir and I didn’t want to let him down, right? So, that’s how we ended up at the wedding at the Cordoba Hotel.

(a pause)

No sir, we were not invited guests.

(a pause)

No, I do not know the DeLisle family.

(a pause)

No sir, I do not know the Monroe family, either. In all honesty, Your Honor, we were completely unaware that a wedding was even taking place there. But you see, sir, one item that was on the scavenger hunt list was a champagne glass from the Cordoba Hotel. That was number seventeen on the list, right between a live catfish and a dozen multicolored golf balls. Now, the golf balls were pretty easy to get from the mini-golf place on highway 43, but the live catfish was a real challenge, and…

(a pause)

No, we couldn’t split up–we had to stay together. That was one of the rules. And that’s why when we got to the Cordoba, Murphy was still holding the cooler with the live catfish inside.

(a pause)

We were afraid that if we left Sylvester in the car that he might flop around and tip over the cooler and then he might die, and we wouldn’t get any points if he died.

(a pause)

No sir, Sylvester wasn’t part of the freshman group. That’s what we named the catfish– you know, after the cartoon cat? Because he’s, well, a catfish. So anyway, we’re all standing there in the lobby of the Cordoba Hotel, and Murphy has the cooler with Sylvester inside, and Little Amir has the bag with a dozen multicolored golf balls.

(a pause)

I’m getting to that, sir. I look inside the open doorway of the Western Zephyr Room, and I see a waiter in a tuxedo carrying a whole tray of champagne glasses. And I figure that they aren’t going to miss just one, right? So I tell everyone just to stay put while I get item number seventeen! But as I’m heading that way, Sylvester starts flopping around, I mean, just going through all sorts of contortions, and water is splashing out the sides of the cooler and stuff, so I tell Little Amir to help Murphy hold the cooler. And that’s when he hands me the bag of golf balls.

(a pause)

Little Amir is not a large person, sir, and frankly he doesn’t handle pressure well. So I took the bag of golf balls from him and headed toward the Western Zephyr Room, leaving him with Jade and Tim and Murphy and Celia and Marta and Sylvester.

(a pause)

No sir, I was alone. See, technically, the rules of the competition say as long as you stay within a hundred yards of the group, you’re still together. In this case, I knew I had to get the champagne glass by myself. Everyone else was busy with the flopping catfish in the cooler or holding on to the other things on the list or just keeping a lookout.

(a pause)

A lookout. In case something went wrong.

(a pause)

Yes sir. Something did indeed go wrong. It went very wrong. The wrongest. As a waiter walked out the door, I slid into the Western Zephyr Room with no problem, and it was at that moment I realized, sir, that the reception for the DeLisle/Monroe Wedding was taking place. I knew that time was of the essence, and I had no intention of causing a disturbance in any way. And so when I saw the champagne glass on the corner of the table, I grabbed it and started to leave.

(a pause)

(a deep sigh, and a hanging head)

No, Your Honor, I was not aware at first that the glass I was taking was part of a champagne tower for the reception. When the entire pyramid of glasses collapsed on top of me, I realized that I had not chosen well.

(a pause)

Well, your honor, I didn’t know quite what to do at that point. I was covered in champagne, and surrounded by broken glass, and everyone was shocked and staring at me while I stood there still holding a bag full of multicolored golf balls in one hand and a champagne glass in the other!

(a pause)

It’s hard to say, sir, it was pretty chaotic, and the events all kind of ran together. At some point my friends came in–

(a pause)

–yes, they were still carrying Sylvester, who had calmed down a little bit by then. So, they came in, and we were all trying to explain to Mr. DeLisle–

(a pause)

I’m sorry, Senator DeLisle–that we would find a way to pay him back for the damages, and it was about that time that Sebastian flopped out of the cooler onto Mrs. Monroe, I think, and she fainted, and–

(a pause)

Yes, the paramedics said she’s going to be fine. And it wasn’t really Little Amir’s fault, I guess. He does not handle pressure well, as I said, and his hands were kind of sweaty, so he couldn’t keep the lid on tightly, so when Sylvester started to flop around again, off popped the lid. You really should have seen the look on Mrs. Monroe’s face when a five-pound catfish landed on her!

(a pause; looks down)

No sir, it was not funny. And yes, we were concerned about Mrs. Monroe, but we had to act fast to get Sylvester back in the cooler.

(a pause)

Yes, as the police report indicates, we did, in fact, put some of the shrimp from the buffet into his cooler, but that’s because Marta said she thought he might be hungry and maybe a snack would settle him down. Anyway, when the police officer that arrived on the scene was trying to take my statement, Sylvester started to flop some more, and I yelled at Little Amir to hold it tighter this time, because we didn’t want another Mrs. Monroe episode, but he and Murphy were really struggling, so I started to go help them, but the officer yelled at me to come back because he wasn’t finished taking my statement, and so I immediately turned around to do what he asked, because I respect the law greatly, Your Honor. Unfortunately, that’s when I slipped on the champagne on the floor and lost my balance, and in trying to maintain my footing, I accidentally hit the officer in the face with the bag of a dozen multicolored golf balls, knocking him out cold.

(a pause)

No, sir. We did not win. Even with all the delay caused by the incident, we had acquired every item we needed. Sadly, however, by the time we returned to Podunkwa and opened the cooler, Sylvester had…passed on.

(a pause)

We believe he..well, he choked on the shrimp, sir.

(a pause)

Yes, Your Honor. I recognize that our poor decisions resulted in this unfortunate outcome. A ruined wedding, a traumatized mother of the groom, an unconscious officer of the law, and…(tearfully) and a dead Sylvester. I take full responsibility.

(a pause)

Really? You went to Podunkwa too? And so did Senator Delisle? AND Mrs. Monroe? Really, what are the odds?

(a pause, during which Taylor’s face goes through multiple

expressions of concern, surprise, and, finally, elation) ad lib

“Uh-huh. Oh! Oh!” etc.

Thank you for understanding, sir. And thank you for dropping the charges. And yes, I have already spoken with Jade and Tim and Murphy and Celia and Marta and Little Amir, and we’re going to be fully responsible for the damages.

(a pause)

What’s that? My major? I was looking at Veterinary Science, but after my experience with Sylvester, I’m not sure that’s a good idea.

(a pause)

My new major? Pre-law.
```

---

## IC-1074: Bad Detective

- Title: Bad Detective
- Author (byline): Brandon Daley
- Work: Bad Detective
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2874
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
Detective: (to audience) It had been a fairly quiet evening. I was at my desk, busy doing online image searches in a desperate attempt to self-diagnose the papules that had recently appeared on my undercarriage when suddenly, fate walked right through my door. (Charlotte enters) Charlotte: Knock knock! Hello there. (Detective starts clicking frantically and typing on his computer, trying to quickly think up an excuse for what he’s doing) Detective: OH! Hey hi sorry I was just uh…looking at…uh, porn…ography. Wait, thats not…what can I do you for? Charlotte: Are you Detective Shlackaluggleberginsteinson? Detective: She had eyes that could cut a diamond; legs that could make the strawberries in the fridge go bad; boobies that were…super nice. I’m talking, like, really nice boobs. (Detective as began ogling her and has forgot to respond to her question) Charlotte: Detective Shlackaluggleberginsteinson? Detective: Oh uh please, Detective Shlackaluggleberginsteinson was my father’s name. Call me Burt. Charlotte: Well, Burt, I have to say, I barely recognized you. You’re much more handsome in person than you are in your picture. (Charlotte holds up a copy of Detective’s ad - his picture is extremely hideous) Detective: Haha, you flatter me. Now what can I do you for Miss- Charlotte: Mrs. actually. But you can just call me Charlotte. I’m here because I think my husband is wrapped up with some questionable people. Detective: Oh yeah? Possibly some gays, huh? Charlotte: Excuse me?

Detective: Gay people. You know…maybe he’s going out on ya. Charlotte: Um…no, that wasn’t the implication. Detective: Oh, sorry, I was just, I’m sorry….Please, tell me more about your husband’s situation. Charlotte: Well- it all started a few weeks ago when he came home all bloody and beaten up. I tried to ask him what happened but I couldn’t get a straight answer out of him. He had some loose narrative about slipping and falling, but I heard him on the phone talking about this man with shaky arms. Now I can’t find him! He seems to have skipped town and I don’t know if he’s alive or if he… (Detective fades Charlotte out and starts monologuing) Detective: (to audience) The woman had quite the way with words; the kind that made your mind wander off and get distracted about halfway through her sentences. I just hoped that my unabashed homophobic tendencies didn’t get in the way of our newfound working relationship. Charlotte: Are you listening to me? Detective: What? I’m sorry. I was monologuing in my head. Can you repeat what you were saying? Charlotte: You don’t seem like a very good detective. Detective: Well, things aren’t always as they seem, are they Miss…oh god, what’s your name again? Charlotte: Charlotte. Detective: That’s right! Charlotte. Sorry, I’m not great with names. Charlotte: I was saying that my husband has disappeared. I need your help to find out where he is and if, god forbid, he’s still even breathing. Detective: Shecky Charlotte. Shacky…shimmy Charlotte. Charlotte: What? Detective: Sorry, I’m trying to come up with a pneumonic device so I can remember your name. Sha, sho, shopping, shoulder- shoulder! Shoulder Charlotte! Hey that’s a pretty good one.

Charlotte: Okay, can we- Detective: Cause you got shoulders and your name is Charlotte. So when I see someone with shoulders, I’ll think, “Hey! That must be Charlotte…” Charlotte: Burt, I’m sorry, but I don’t think this is going to work out- Detective: Oh what, no! Please! I need this. I haven’t had a client in weeks! Charlotte: If you think you can help then go ahead, but you aren’t getting a single dime until I get some answers. Deal? Detective: (to audience) I was in a little bit of a sticky wicket. I needed the money, but the chances of me solving this case were slim to none. None to none even, but that- Charlotte: Burt! Detective: What? Yeah, sorry. What? Charlotte: Here. This is a picture of my husband. (Charlotte hands Detective a picture) Detective: Wow, he’s a lot blacker than I had him pinned. Charlotte: He frequents the Bitter End, the bar down on Rush street. I’d go myself, but they’d recognize me in an instant. It’s not safe for me. Like I said, I’ve heard him talk elusively about someone they call the man with shaky arms. I have a feeling that if you find the man with the shaky arms, you’ll be able to figure out what happened to my husband. Detective: That’s boring. I don’t want to do all that. Charlotte: Please, Burt. I need help. Good private eyes in this town are hard to come by. Detective: Well, I’m not a good private eye. I’m a great private eye, Sharon. Charlotte: Charlotte. Detective: Charlotte.

(to the audience) Detective: That night, I decided to check out the bar that Cheryl had mentioned. I had been planning to go to a bar anyway, as I’m a passably functional alcoholic with a heart full of bigotry and self-hatred, so I decided I might as well do something constructive for my case while I was at it. Bartender: Hey. Whatcha having? Detective: Let me get a beer. Double shot of vodka in it please. Bartender: What? Detective: Haha, just a joke between old friends - say you wouldn’t happen to know this black guy would you? (Detective hands Bartender the picture) Bartender: I don’t know, maybe…why do you ask? Detective: We can talk about it after you get my vodka beer. Put some ice in it too, would ya? Just know I’m trying to keep a low profile, not call attention to myself, ya got me? Bartender: Uh yeah sure. Detective: What am I saying…this guy knows about low profiles. Am I right? (Detective slaps the bartender on the shoulder and starts looking around the bar for backup) Detective: Huh? Am I right! Anybody? This guy knows what I’m talking about. Right? Huh? Do you know what I’m talking about? What about you two, you guys know what I’m talking about? You two guys? On the stools down there. I’m trying to keep a low profile! Say, you guys aren’t gay are you? Is this a gay bar? I don’t ask because I’m gay. I am only asking because I’m highly intolerant. Bartender: Hey man you gotta relax a little bit. Quit yelling so much. Detective: Hey, it’s all good! I’m cool, bro, I’m cool. We’re all old friends here. Isn’t that right gay fellows!? Bartender: Look, is there a reason you decided to come in here today and act all high and mighty and intolerant of Hank and Baxter’s life choices?

Hank: It’s not a choice. Baxter: Damn straight. Detective: My apologies. I don’t want any trouble. I’m just trying to drink my icy vodka beer and find out who this black guy is, okay? Bartender: If I tell you will you promise to shut up and get out of my bar? Detective: (to audience) Well well well…looks like my affixation on race and sexual orientation was finally starting to pay off. But it wasn’t all good news. Turns out some of these people didn’t really agree with my view points all that much. I was sensing a little hostility from the regulars, and by the looks of the bartender, he wasn’t too happy with me either. Then again, I wasn’t very happy with me. You see, I came from a very old-fashioned upbringing, one where the decisions of others are seen as religiously and morally inferior to that of your own- Bartender: Hey! Are you listening to me? Detective: Sorry! Sorry, I was zoning out pretty hard. I’m self-diagnosed with attention deficit syndrome. Bartender: I don’t think that’s a syndrome. Detective: Well I know there’s a lot of doubters out there but there’s enough science at this point to back that A.D.S. is a real thing. Bartender: Look, the guy’s name is Anthony. He used to be a regular here before getting in deep with a few of the sports bookies. Particularly, the Shaky Arms Man. Shaky roughed him up pretty good. Word on the street is Anthony even skipped town. Haven’t seen him in here for a week or two. But listen you go around showing people that picture and you’re going to be guilty by association, you understand? Now I’d tuck that away in your pocket and go home before you get your teeth knocked in over a guy you don’t know, and that’s probably the best advice you are gonna here all night. You got it? (Detective seems to be monologuing in his head, mouthing words to himself while neglecting to catch anything the bartender has just disclosed to him) Bartender: Jesus- Detective: Wha- OH man, sorry, sorry. I definitely was doing it again.

Bartender: Listen man, I tried to help you but you’re on your own.
Detective: Wait- could you just repeat all that-!
(Bartender exits)
Detective: (to audience) Damn- What a shame…the case had fallen right into my
lap, but I was too busy looking at stuff that wasn’t my lap to notice. I had almost
given up hope when suddenly…I saw him.
(Detective sees someone at the bar. He carefully approaches him)
Detective: Um, excuse me. Sir? You wouldn’t happen to be, the Shaky Arms
Man, would you?
(Shaky Arms Man’s arms shake violently)
Shaky: Depends. Whose asking?
Detective: (To audience) Well as fate would have it, the Shaky Arms Man was
back in my lap again, and I liked him in my lap. Not sexually speaking of course,
that didn’t come out right…am I gay?
Detective: (shivering off his internal discussion) Um yes, well, the name’s
Shlackaluggleberginsteinson. Burt Shlackaluggleberginsteinson.
Shaky: That’s the silliest name I ever heard. You aren’t a cop are ya?
Detective: No I’m a detective-- I mean…no.
Shaky: Okay good. I don’t like pigs or narcs or private dicks up in my business.
Detective: With you loud and clear on that one.
Shaky: You see, I’m a well-established bookie in this town and the thought of
someone, whether they be a pig or a narc or a private dick, the thought of
someone interfering with my business makes me feel pretty stabby!
Detective: Stabby? Is that an emotion of some kind or…?
Shaky: It’s the only emotion where I’m from.
Detective: That’s interesting. You see, I was unaware of that, as most of my
knowledge of human emotion stems from studying the various emojis that I find
on my phone, and I don’t think there’s one for “stabby” or at least not currently
there isn’t…
Shaky: Look, I like you kid. You got a real trustworthy vibe to you. Let me buy you
a drink. What are you having? Barkeep!
Bartender: Yeah Shaky?
Shaky: Get this man a drink! I’ll have whatever he’s having!
Detective: Make it a Capris Sun and gin please, barkeep.
Bartender: We don’t have that.
Detective: Capris Sun and tequila then?
Bartender: We don’t have Capris Sun.
Detective: Okay well just another vodka beer on the rocks then please.
Shaky: Oh, god, that’s, really…okay, yeah sure, make it two.
(Bartender serves them some Vodka beers)
Shaky: To new friends.
Detective: To new friends.
(They cheers their glasses and take a sip. Shaky Arms Man is disgusted by his
drink)
Detective: Say, now that we’re old pals and I’m not a detective or anything, you
wouldn’t happen to know this man would you.
(Bartender makes a cutting motion to his neck as Detective reaches into his
pocket. Detective neglects to understand the hand motion and produces the
picture of Anthony anyway. He holds it up for Shaky to see).
Detective: He’s the black one.
Shaky: There’s only one guy in this picture.
Detective: And?

Shaky: Hey wait a minute….I do know him! Hey this guy owes me a lot of money!
What!? Is he one of your friends or something! If he ended up being one of your
friends that’d make me pretty stabby.
Detective: Oh no, no sir. I- uh-
(Detective quickly puts the picture away. Bartender rolls his eyes.)
Shaky: What you come to get revenge for me and my boys beating him half dead
last week!?
Detective: No, no sir…I was just hired to-
Shaky: HIRED!? So what then!? You’re a private dick?
Detective: No no no, no dicks here! I swear!
Shaky: Bartender! Can you step in back for a second, me and my boys have to
take care of a little business.
Bartender: Yes of course Shaky. Just try not to make a mess.
Shaky: Sure thing boss!
(Bartender exits)
Detective: No no no you got it all wrong Shaky! I’m not-
Shaky: Boys! Hold him down!
(The boys from the surrounding bar grab Detective and hold him down).
Detective: NO! NO NO! HELP! ANYONE! Gay fellows! Please! I’m sorry for
everything! I have gay thoughts sometimes even!
Hank: You’re on your own detective.
Baxter: Damn straight.
Detective: NOOOOOO!
(Shaky produces a big knife and stabs Detective repeatedly in the stomach).

Detective: AhhhHHHHHH! PLEASE NO STOP!!! OH MY GOD OH MY GOD- Detective: (To audience) Of all the vodka beer joints in all the world, I had to get stabbed in this one. You know, for my entire life I wanted to be a detective and here I was, getting stabbed in what could possibly be a gay bar. Well, you know what they say- the grass is- uh, excuse me. Well, you know what they say, the green is always- cough cough, you know what they grass. The gay bar is always greener- well, you know grass is greener- that grass is suuuuper green. Man, I’m not feeling so…where did all this blood come from? (Detective loses consciousness, slurring his words as he slowly passes out. His life flashes before his eyes). Dad: Burt, you’re going to grow up to be a great detective son. Detective: Dad? Mom: When you get older, I bet you’re going to be the best detective there ever was. Detective: Mom? Teacher: You’re special Burt. That’s why you’re in this special class. Detective: Mrs. Teacher Lady? Grandpa: Those homosexuals and minorities are decreasing the value of the American dollar! Detective: Grandpapa? Charlotte: You don’t seem like a very good detective. Detective: Who are you again? Shaky: All that’s in this guy’s wallet is a coupon for a free appetizer at Chili’s and an expired condom. What a waste of stab! Detective: Shaky? Shaky: Just leave him in the gutter to die. Let’s get out of here boys! Detective: Oh okay goodbye everybody…

(Detective closes his eyes and falls still. After a few moments of silence, we hear the familiar beep of a hospital life-support device.) Doctor: Burt? Burt? Can you hear me? (Detective wakes up slowly) Detective: Wha- cough cough - where am I? Doctor: I’m Dr. James Conrad. You’re in the hospital Burt. Some people found you outside the Bitter End a few nights ago after having been stabbed over sixty times. You’re lucky to be alive! Detective: Wow, you’re a doctor? But you’re a black guy! Doctor: Um, yes, okay, well… anyway, you’re hanging in there. Seems like most of your vital organs are in a stable condition. We should be able to have you out of here in a couple of days, but you will be wheelchair bound for the foreseeable future. Don’t worry though, my husband is actually a world-renowned physical therapist. I’m going to suggest you see him for a few months and he should have you back walking in no time. Detective: Your husband? Well I’ll be darned, a gay black guy saved my life! Thank you so much doc! Doctor: It was my pleasure, but to be honest, your incessant use of qualifiers about race and sexual orientation are quickly making me regret my decision. Detective: Haha, that’s pretty funny doc. Doctor: There’s a woman here asking to see you. I’d usually suggest against it for someone in your condition but my concern for your well-being is beginning to wane. Detective: What do you mean “wayne?” As in Lil Wayne? Come on homie, no rap talk right now. Let’s keep it professional up in here. This is a hospital, not a Dem Franchise Boys concert, you know what I’m saying? (Detective goes for the fist pump. Doctor is unamused and does not reciprocate the bump.) Doctor: I’ll send her in. (Doctor exits. Shortly after, Charlotte enters the room)

Charlotte: Detective Shlackaluggleberginsteinson. Detective: Oh hey Shoulders! Charlotte: It’s Charlotte. Listen, I’m sorry for how things unfolded at the Bitter End. I should have known better than to send you into such a dangerous environment, especially after realizing how incompetent you are as a detective. Detective: Nahhhhhhh baby, it’s all good. They got me patched up and gave me this cool black fellow to hang out with. You know how we do, haha! Say how’d you know to find me here? Charlotte: Well, to be honest, directly after our meeting the other day in your office, I went and hired another private eye. He not only found out my husband is in Argentina evading a massive gambling debt, but also reported that my other detective had been stabbed multiple times after offending as many demographics as possible. Detective: I mean, it was just the two demographics really… Charlotte: I thought I’d come and give my apologies before catching my flight to South America. I’m not happy with my husband for his decisions, but he’s still my husband and I still love him. Thanks for trying, but you really should look into other professions. Detective: Don’t thank me ma’am; it’s the least I could do. Charlotte: I know that’s a figure of speech, but in these circumstances, I really believe that you did the least humanly possible in terms of helping me resolve this case. Detective: Yeah, I’m glad I could help too. Now, as far as payment goes, I’m thinking maybe a thousand dollars? But I’d also settle for a fifty dollar gift card to a chain restaurant of my choice. Honestly, if you just bring me some good coupons or something, we’ll call it square. I had one for a free appetizer at Chili’s but I seem to have misplaced it… Charlotte: Goodbye Burt. Get well soon. Detective: Oh okay, goodbye Sharon! Charlotte: It’s Charlotte.

(Charlotte exits. Detective starts monologuing) Detective: So everything ended up working out for the best. Cheryl found her man, the Shaky Arms Man got my free appetizer with the purchase of any entrée coupon, and I was left back right where I started, paralyzed from the waist down. Yep, funny how life goes some times. One minute you’re in your office self-diagnosing the skin tags on the underside of your genitals, the next you’re having your prejudices quickly extinguished by a gay black doctor. I don’t know much about this crazy mixed up thing we call life. All I know is that I’m trying to make the best I can out of it.
```

---

## IC-1075: MINUTES FROM THE COUNCIL UNITED FOR WORLD DESTRUCTION (The Council of Doom)

- Title: MINUTES FROM THE COUNCIL UNITED FOR WORLD DESTRUCTION (The Council of Doom)
- Author (byline): Taylor Shann
- Work: MINUTES FROM THE COUNCIL UNITED FOR WORLD DESTRUCTION (The Council of Doom)
- Publisher: Mushroom Cloud Press
- Publication date as stated: 2005
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: BANJO, KNIGHT, SHE-MALE, SEA-MAN, SEA-MAN’S TRANSLATOR, ROBOTO, DOOM, ALL, KNIGHT AND SHE-MALE, GIANT TALKING CUCUMBER, G.T.C
- Teaser before the introduction: No
- Spoken words (computed): 3415
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
Prologue:

Lights up on four shadowy figures, sitting at a table: THE DARK KNIGHT, a renaissance fair refugee; SEA-MAN, self-proclaimed Spanish lord of the sea; SHE-MALE, a muscle woman with sunglasses and an attitude, and ROBOTO, a robot.

There is also BANJO, a girl sitting with a guitar. There seems to be nothing especially evil or bizarre about her.

Yet.

Banjo tunes the guitar, sees the audience. She seems to exist in a different space then the villains.

BANJO:
On a Saturday, in the month of December
Not too terribly long ago.
The world was almost destroyed
By a most Demented Foe

A Madman! A Genius! My friends,
A man not born to push a broom-
A Name soon the world would fear-
Professor Gregory Von Doom!

(she begins to rock out)

DOOM! DOOM! GREGORY VON DOOM!
YEAH! YEAH! MR. DOOM TO YOU!
DOOM! DOOM! GREGORY VON DOOM!
HE MADE ME GO CLEAN UP MY ROOM!

(calms down)

He called for the greatest villains
To help him on his quest
And when they could not make it
He made some calls and got the rest

But who are these fools? Do they not realize
they are but their brides, he their groom?
What evil plot have they fallen into-
The minions of Professor- Gregory-

VON DOOM! DOOM! GREGORY VON DOOM!
HE MAKES ALL THE LADIES SWOON!
DOOM! DOOM! GREGORY VON DOOM!
I’VE RUN OUT OF WORDS TO RHYME WITH DOOOOOOOMMMM!

Lights shift.

Meeting One:

The villains resume action in real time.

KNIGHT: Verily, How was thy trip?

SHE-MALE: The trip was fine. The hour waiting for my f-ing luggage was a bore.

Pause. ROBOTO beeps.

SHE-MALE: Uh huh. Right. (looks at Sea-man) So, what’s your deal?

SEA-MAN: Mi nombre es Seaman!

SEA-MAN’S TRANSLATOR:
(a device that SEA-MAN carries, which comes out in a cherpy, friendly
voice.)
My name is the Seaman!

SEA-MAN: (lustfully) Soy el tyrant del mar!

SEA-MAN’S TRANSLATOR: I am The Tyrant of the Sea!

ROBOTO: One Zero Zero Zero Zero One Zero One.

SHE-MALE: We’re getting paid for this, right?

PROFESSOR GREGORY VON DOOM enters in a grand fashion. He has spent a lot of time on his costume.

DOOM: Gentlemen. Welcome to my lair. I have gathered, from the—(stops) are we all here? (to an empty chair) We’re one short. Banjo, did you- Oh, right. I liquidated Banjo.

BANJO: No, you didn’t.

DOOM: Oh. (thinks) Then who’s in the liquidator?

BANJO: sick bastard (beat) Squeakums… You .

BANJO stalks offstage. DOOM turns back to the group.

DOOM: (to the group) Did anyone see—I know this is, this is not normal but did anyone see a giant talking cucumber in the parking lot. Anyone. Anyone at all. Giant talking cucumber. Hard to miss.

Roboto beeps, opens his stomach drawer and pulls out a plate of sliced cucumber. All stare at it. Doom takes a large breath.

DOOM: Super. Alright. Focus. (closes eyes, to self) You’ve got the touch. You’ve got the power. You are a chestnut of possibility (hums offkey, then opens his eyes and-) I have brought you here for one purpose. talk- There’s been a lot of from a lot of would be-s and never-haves fit in and oh I should but you know my schedule, it’s not going to this week- a lot of talk about destroying the world. I want US… Let’s be the does group that something about it. We shall make the world… QUAKE… WITH…. FEAR!!!!!! (thunder) But first. Banjo? (Banjo enters, with a pot.) Go to the deli and get some dip, please. Wait. What is that?

BANJO: The Dip.

DOOM: I thought we were out.

BANJO: We used to have Squeakums the giant hamster. Now we have dip.

DOOM: I don’t-

BANJO: LIQUIDATOR!

DOOM: …it begins.

DOOM takes the dip and begins to serve out parts of the dead cucumber. BANJO sings a song.

G.T.C.

Giant Talking Cucumber, my G.T.C. Goodbye, my friend, we hardly knew ye

Maybe you were tall, maybe short and fat We won't ever know, and that my friend is that

and that my friend is that and that my friend is that that, my G.T.C., is that

Alas, Alack, you never even made it onstage The writer wrote you, but left you off the page

Rest in peace, G.T.C. I know you had the nerve But now you're in my stomach, a tasty hors d'oeuvre

Meeting Two:

Lights up mid-argument:

DOOM: Red wine!

SHE-MALE: White wine!

DOOM: Red wine!

SHE-MALE: White wine!

DOOM:
your
Is it council untied for world destruction? No. It’s mine. And I
say we’re drinking-

SEA-MAN: Idiota! I hundido el titanic con el spunk en mi pinky!

SEA-MAN’S TRANSLATOR: I am afraid you are mistaken. I am the person who sunk the Titanic with the spunk in my small finger!

KNIGHT:
(grabs the translator, screaming into it)
Would ye stop HOUNDING MY BRAIN like a JACKAL with your DEMON
language?! (begins to weep)

BANJO: How about a Blush wine? A Rose’? Anyone for Rose’. (to ROBOTO) I like Rose’.

DOOM: People, people!

ROBOTO Zero.

DOOM: And Robot. The idiot in the armor has a point. We all need to curse at each other in the same tongue. Otherwise, the forces of good have already won. Some say they already have. That is the purpose of this union! You summon, here’s what you do- you summon, from the farthest corners of the galaxy- the greatest villains of all time-

SHE-MALE: Excuse me?

DOOM: The greatest low life scum, the- yes?

SHE-MALE: Uh, yeah. I’m from Detroit, and, I believe I put that on my resume-

DOOM: Yes?

SHE-MALE: Suburbs of Detroit, actually. The point is, I’m not actually from another, how do I put this- Galaxy? And I don’t believe that was ever on the job posting.

KNIGHT: Verily, I am from the Middle Ages, under the reign of King John. We do not believe in planets.

SEA-MAN: Vengo del país del amor, bebé.

SEA-MAN’s TRANSLATOR: I come from the country named love. Baby.

DOOM: Okay. FINE. This council is made up of a woman from Detriot, a Knight from the Middle Ages, a Fish-Man

SEA-MAN SEAMAN!!!

SEA-MAN TRANSLATOR I am the Sea-Man-

DOOM: A SEAMAN from the deep briny deeps of love, and a Robot from… (stares at the Robot) Well, a Robot. He doesn’t need to be BE from anywhere.

BANJO: And Banjo.

DOOM: Yes, and Banjo. Until she gets liquidated.

BANJO: Oh yeah? Oh yeah? Well maybe you should make yourself the Mayor of JERKVILLE, because you obviously are the FOUNDER! Established in 1898- by Dr. Gregory JERK!

SEA-MAN (to the Knight) Que? “jerk-ville?” No cophrehende.

SEA-MAN’s TRANSLATOR: What is that? I do not understand this ERROR ERROR ERROR

BANJO: I hate you Dad! (runs offstage)

SEA-MAN’S TRANSLATOR: ERROR ERROR ERROR ER-

The Knight grabs the Translator and breaks it in half.

DOOM: Let that be a lesson to all of you. Time travel yields dubious results. You try to go back and fix the Spanish American War, you return with a guitar playing hippy-dippy daughter and one hundred and two years of back-alimony.

ROBOTO: One one one one one one one one one one one one one one one one one one one one Zero.

SHE-MALE: (sighs) Look, can we at least agree that the… ‘council’ needs an immediate deli run? All in favor say Aye.

ALL: Aye.

ROBOTO (after): Yes.

They all stare at it. DOOM stands, contemplating.

ROBOTO: Er. One. Zero.

They all pull their various instruments of destruction. KNIGHT, his sword; SEA-MAN, his fish, DOOM, his Doom Ray, and SHE-MALE, her bitchiness.

ROBOTO: One?

DOOM: (quietly) Sic Semper Falsus Robotum.

Lights go down fast as they move in on him, we can only see Banjo. She strums the guitar, then rocks out hardcore:

ROBOTO

Every Sci-Fi Movie
From Nineteen-Eighty On
Every one worth watching
(Thus excluding Tron)

Makes it very very very clear
To man and boy the same
To Never ever Trust a Robot (Ever Ever Trust a Robot)
This is not a game!

Oooh Oooh Oooh Oooh Oooh

During this part, we see flashes of light as the Four dismantle ROBOTO stylistically-

They'll wait until you sleep at night
They'll crust your pets with Metal Might
(Might! Metal Might!)
They'll grind and clang and rip you up
They'll blaster your master and never stop!
(Never Stop! Never Stop!)

Regarding our little carboard friend-
About his rather unfortunate end-
Consider this his eulogy
I hope you'd do the same for me.
We'll nail a sign up to a tree
And leave there for all to see-

NEVER TRUST A ROBOT
NEVER EVER TRUST A ROBOT
NEVER EVER EVER EVER EVER
AND IF YOU DO…
Serves you right.

Meeting Three:

Beer, Snacks everywhere. Roboto has a bowl of guacamole sitting where his head used to be. SEA-MAN is applying some tape to his translator. SHE-MALE is holding the head. Some wine spritzers have been drunk by all. Especially BANJO.

DOOM: That’s how we deal with interlopers. Got it? No Interloping on my watch. (holding the agenda) Now, when shall we three meet again?

KNIGHT: Are there not four of us? Forsooth, there are.

DOOM: Alright, screw it. (crumples up the paper)

SHE-MALE: It just ripped right off when I pulled at it. (offers it to the Sea-man) Damndest thing.

DOOM: Dark Knight, my friend. We bought that Mutton Jerky, and I must insist you eat it. (as Sea-Man puts on the Robot Head)

KNIGHT: Nay, my good sir. Hast though tried it? Thyne Bowels moveth not for a week.

BANJO: Oh? Did your bowels move when you ate my HAMSTER DIP?

KNIGHT (quietly) Was that not Guacamole?

BANJO: Does Guacamole have a tail?

The KNIGHT throws up in his own helmet, which is worse than it sounds, and shortly afterwards, he falls on the ground begins screaming. DOOM tries to regain control-

DOOM: Moving right along. We can, uh-

SEA-MAN Beeepe! Uno! Nada! Uno!

SEA-MAN’S TRANSLATOR: One! Zero! One!

DOOM: You. Fishboy. Take that off.

SEA-MAN: No estoy usando la cabeza de la robusteza.

SEA-MAN’S TRANSLATOR: I am not using the head of the robot, my Good Man.

DOOM: Spaniard. Listen to me. I will burn you like a child in the strange world of Roahl Dahl.

SEA-MAN: cómame, mi amigo.

SEA-MAN’S TRANSLATOR Eat me! ... my good friend.

DOOM: No abla dead-man. Fishboy.

Beat. Show-down. Knight and SHE-MALE slide back from the table. DOOM knocks the translator out of his hand.

SEA-MAN Hey! I paid thirty bucks for- (stops) Er. No solo… trece de… Radioshack-o…

Sea-Man suddenly bolts, Doom runs after him screaming. Banjo strums the guitar.

KNIGHT: (after a beat, to SHE-MALE) You art the most grotesque, yet ravishing creature I hath ever seen.

She stares at him as the song starts-

Sea-Man

BANJO:

Sea-Man, Sea-Man
The Spanish Faking He-Man
Sea-Man, No more he waves
As we salsa on his grave

Ariba! We urge him on
Andre, to the ocean's son
But what is this? My God, what baloney!
This fishman's nothing but a phony!

One lousy little mutant shark
Where's his Bite? Only Bark!
Not only that, but it gets worse
He knows no Spanish- not one verse!

This Euro trash,
the unshaven scum
Wants to know
just how it's done

We'll teach him how-
'se abla engles?'
Down he goes
To his proper place

Oui Oui, he won't leave this room Until he gets a healthy dose of DOOM!

Meeting Four:

As before. Roboto’s headless body now holds a bowl of guacamole. Sea- Man is propped in his chair, dead. Knight seems recently beaten-up, yet strangely happy about it. SHE-MALE is not amused. Doom is trying to keep it together. He hold’s Sea-Man’s translator in his hand. Many more wine spritzers have been drunk.

DOOM: It was so simple. You get a bunch of people together. You try to take he presses a button over the world. And it all goes to hell. ( .)

SEA-MAN’S TRANSLATOR: Please, my good friend, stop shoving my head into my-

DOOM: he clicks it off, takes a long swig of Spritzer ( ) You know, I blew up a bank the other day. I have them all there, before the, you know, the big boom- and I ask them if they’ve got any last words. Now I’ve heard it all- please don’t kill me, my wife and kids, I never saw the Astrodome, et cetera. But I ask the guy, any last words. He says, “Yeah,” and he turns to his boss and he says, “Bill, I just want you to know. I’ve been stealing the toilet paper from here for years.” And the boss mulls this and says, “Dave, you’re fired.” And then VASHOOM, the another sip whole place was vaporized, just like that.( ) Now that’s a true story.

SHE-MALE Does it have a point?

DOOM: Silence. And YES. It does. People just- I don’t know, it’s a new world out there, a sad world. Used to be, you shoved a death ray in their face, you point a nuclear missle at them, they’d pay attention. Now? Credit card bills and wireless internets and aaaah, I don’t know. Nothing grabs their interest anymore. You’re another blip on their takes a sip radar. ( ) Anyway. So. Where were we?

SHE-MALE: Your plan.

DOOM: Yes. The plan. I worked on it a very long time. I have learned from our ancestors. I watched every episode of G.I. Joe that was commercially beat available ( ) Because, they had some good ideas, but every time, Hubris. Hubris was the flaw. We don’t have that. We have five of the… we have three, three of the biggest, baddest villains out there. Now I say we take this eight point implementation plan of Doom, and we say to beat the World; ‘hey world?? What’s up? Me. Us. That’s what’s up.” ( ) Banjo. Where’s the eight point implenetation plan of doom?

BANJO: The EPIPD? I think, last I saw it, you were stuffing down the fish-man’s throat.

KNIGHT AND SHE-MALE: Sea-Man.

BANJO:
Doom puts his head in his
Sea-Man, right. Yeah. It’s in his carcass. (
hands
) You want me to go get it?

DOOM: I want a lot of things, Banjo. Peace. Love. The World. But I don’t think I’m going to get them.

KNIGHT: pregnant pause Verily, it might have been a good plan, fair and true. ( ) Would it not already be digested. Although I recall, not too terribly long ago, another man with a plan. A demon with an angel’s face- learn well, my friends, that the pen is always mightier than the sword, for when he was done….oh, Chaucer! Why, Chaucer!? I tell ye one little olde story and my good turned to evile! Now I maketh less then $3.75 an hour, and not even a sliver of booty to show for it? Beware… BEWA-

Doom quickly breaks the Knight’s neck. He collapses in the chip bowl. SHE-MALE is stunned. Thunder.

DOOM: bites Bum Bum Bum. Another bites the Dust. Bum Bum Bum. Another one -

Quick blackout. Lights up on Banjo.

KNIGHT SONG-

Sleep sound, sleep tight
My dear, dead, Dark Knight
This Stupid Geek, He saw no wrong
In Bitching Bitching Bitching Bitching
All night long.

Bitching Bitching Bitching all night long Bitching Bitching Bitching all night long.

Why bother to wake the dead
When you’d rather spend all day in bed?
Why carry a big badass blade-
When you’d rather eat those cookies-
-you know the ones with the chocolate and the white chocolate and
they’re kind of gooey and probably really bad for you but who cares-
that my mom made?

Bitching Bitching Bitching all night long Bitching Bitching Bitching all night long.

He bitches and whines and then he mopes
Stays home crying and watching his soaps
He’s very shiny but not all that bright-
My Dear, Dearest, Dead Dark Knight

Bitching Bitching Bitching all night long
Bitching Bitching Bitching all night long.
Bitching Bitching Bitching Bitching
All night long.

Meeting Five:

As before. Knight and Sea-Man are propped in their chairs with chip-bags on their heads. Roboto’s body has now been dismantled to serve as several bowls for chips, dip. SHE-MALE is uneasy, as Doom has clearly gone insane.

DOOM: So, in conclusion… while I considered, for a time, sparing this little planet, you four… (looks around) Well, YOU, have been chosen to witness dismemberment. it’s… To all the citizens of earth… prepare for extermination. I am your new King- Professor Gregory Von-

SHE-MALE: King of who? Me and the headless tin man over here? Look at us- we didn’t even have a unified theme! I’m a Amazon- how was I supposed to work with a demented Medieval Reject? Crush his skull like a grapefruit that’ll and charge admission? Oh, sing an ironic song about our deaths, destroy the world. And the poor bastard Spaniard used all of that ocean garbage to pick up women. The robot wasn’t even a robot- look at him, look his metal is cardboard! Did you even at his references? You didn’t think this through, did you? (beat) Oh God. I killed a man.

DOOM: You’re right. What was I thinking? This is so silly. I’m sorry. Oh, DOOM!! SHE-MALE? (she looks up) It’s Von Doom screams and lunges. A brief struggle. SHE-MALE has the upper hand until a ray gun goes off, killing her. Doom is triumphant. Banjo sings sadly, but with a sick smile.

SHE MALE SONG-

She-Male, She-Male-
Were you even ever Female?
She-Male, She-Male
Now you’re only a dream-mail-

Suddenly, DOOM suddenly lurches over. He stares a Banjo, wild-eyed-

DOOM: You-! (wide-eyed, grasping stomach, enraged) My appendix!?

BANJO: Time travel does funny things. When you went back to stop the Spanish American War, you didn’t just create a daughter with separation issues. never You also created an alternate timeline, where your appendix was taken out …

DOOM: The Appendix Scenario… No…

BANJO: And the prophecy is fulfilled, father… I am your legacy!

DOOM: you cannot… destroy… my… destiny! (dies)

A moment. Then, A GIANT TALKING CUCUMBER enters, looking sheepish, carrying luggage.

GIANT TALKING CUCUMBER:
believe
Sorry I’m so late… you would not what happened to my- (stops)
Ooh. Bad time?

BANJO: Nah. (beat) Hi I’m Banjo.

GIANT TALKING CUCUMBER: Nice to meet you. I’m –

BANJO: Don’t tell me. You’re the Giant Talking Cucumber.

GIANT TALKING CUCUMBER: The one and only.

BANJO: You want some Robot/Hampster Guacamole?

G.T.C: I’d be delighted!

ENDING SONG-

It’s Saturday, in the month of December And the world is safe- for now.

No more Gregory, his appendix did him in But of the Von Dooms, this I vow

That the world with Shiver The governments will Quiver And soon the world will Quake with Fear…

Get ready for…

BANJO! BANJO! BANJO VON DOOM!
SHE’S MS KICKASS VILLAIN QUEEN BADASS TO YOU!
BANJO! BANJO! BANJO VON DOOM!
SHE’S COMING TO KICK YOUR ASS-
AT A THEATRE NEAR YOU!!!!!!

During the final song, the Cucumber eats a piece of cucumber without realizing it- then realizes it, and dies from the horror/shock.

BANJO laughs as evilly as possible. Then she has a piece of Cucumber with dip on it.

Thunder. Fade out. End.

ALL THE OTHER STUFF

Summary: The world was almost destroyed recently by the Committee United for World Destruction (C.U.W.D.). What follows is the account of why the world was spared.

Production Notes: Your first reaction will probably be, “how the hell can we afford all this?” The answer is, don’t. The robot is made of cardboard (literally) the ray gun should be purchased at Wall-Mart and the Cucumber should be nothing more than a man in a green garbage bag. However, it should be knows noted that none of them they’re ridiculous (except arguably the SHE-MALE.) The more seriously the actors play the material, and act in their ridiculous garb, the better. Of course, should you decide to spend money on the project—should the Sea-Man actually have a trident, for instance—I can’t stop you. But it might take away from the overall effect.

Banjo’s songs. Banjo in general. She is the oompa-loompa of this enterprise. Except in the end, she kills Willy Wonka. Let her be just as creepy/awesome/strangely rehearsed.

Should you decide to do it without the songs, again, I can’t stop you. At the time of publication, no music as been written, it’s just lyrics. But any amount of guitar strumming or, basically, anyone with musical talent and a taste for improvisation can make it work.

Finally, the Giant Talking Cucumber can be played by a different actor, but I have structured it in a way so that Roboto can play him/her (as the robot is disabled by the time that the Cucumber arrives.) However, do not list the actor playing Roboto as also playing the Cucumber. If you decide to have a separate cast member play the cucumber, make it a cameo- do not list him/her in the cast. Do not list the Cucumber in program at all, basically, so that no one sees it coming. Especially not the Cucumber. (If you’re worried about people getting that it’s a Giant Cucumber, feel free to put a sticker on the luggage that says “Property of G. Cucumber”, or something to that effect.)

Bio:

Taylor Shann is a jack of all trades, master of some. He writes, he directs, he produces and he often gets drunk and leaves his friends Minutes long, rambling voicemails about what a great person they are. from the C.U.W.D. is by far the most fun he has ever had writing a play. Some of his longer plays are published online by The Mushroom Cloud Press (mushroomcloudpress.com) He lives in New York and works at Samuel French Inc., the oldest play publisher in the world. Graduated Tufts University, 2004.
```

---

## IC-1076: Everything Under the Sun

- Title: Everything Under the Sun
- Author (byline): Bridget Grace Sheaff
- Work: Everything Under the Sun
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: SYNOPSIS, CHARACTERS, SCENE, AT RISE, SUN, JUPITER, MERCURY, EARTH, VENUS, MARS, NEPTUNE, PLUTO, SATURN, URANUS, URUNAS, ALL
- Teaser before the introduction: No
- Spoken words (computed): 2010
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
SYNOPSIS: At an interplanetary meeting, The Sun announces that she needs a vacation. Each of the planets vies for their position as the center of the solar system, with disastrous results. In the end, after a rally of appreciation, The Sun decides to stay.

CHARACTERS: SUN- The leader. Exhausted. Quick-witted, but sometimes lacking in leadership. MERCURY- The brainiac. Talkative and intelligent to the point of being a real pest. VENUS- The flirt. Very feminine. Living up to her name. EARTH- The sassy one. Bold and brash, but loving and caring all the same. “Mother Earth.” MARS- The dark one. Deeply philosophical to a terrifying degree. JUPITER- The jock. Not that bright. Slow. Can be a jerk, but is not aware of his own strength. SATURN- The brawn. Authoritative, stepping out of rank. Keeps the outer planets in line. URANUS- The clown. Constant joking, probably as a defense mechanism because of his name. NEPTUNE- The old one. Too far away. Can’t hear worth a darn. PLUTO- The outcast. Small. Meek. But surprisingly insightful.

SCENE: A conference room, one where an interplanetary meeting is taking place.

AT RISE: The planets are sitting around chatting while SUN moves to the head of the table. JUPITER is holding MERCURY’S glasses above his head as MERCURY tries to jump and grab them. EARTH and VENUS are talking rapidly. MARS sits darkly, arms crossed. NEPTUNE is not even at the table and is sitting very far away from the rest of the group. SATURN keeps glancing at PLUTO threateningly from across the table, as if PLUTO is an insolent child. PLUTO sits complacently, staring at his hands.

SUN: Alright, alright, alright, settle down. Settle down. Jupiter, leave Mercury alone.

JUPITER: Sorry, Sun.

MERCURY: Yeah, Jupiter, why don’t you bother someone with the same relative mass and mean radius as yourself?

JUPITER: … Wha?

SUN: Never mind! Never mind. Can we get this meeting started please… and keep the side conversations to a minimum? Earth, Venus, something you‘d like to share with the group?

EARTH: If I wanted to share it with the group, I wouldn’t have whispered it to Venus, huh? Mm-hmm.

VENUS: Sorry, sunny boy, just girl talk.

EARTH: Like I was saying before we were so rudely interrupted, craters are just part of being a planet. They’re just the death of your complexion.

MARS: Death is the real killer. Death is coming. End of all we know. SUN:… Okay then, Mars… Can we please begin? Please?

NEPTUNE: What?

SUN: (yelling) I said “can we please begin the meeting,” Neptune.

NEPTUNE: What?

SUN: Oh, never mind.

PLUTO: I think…

SATURN: Pluto! What did I tell you about talking? You shouldn’t even be here. You’re not a planet anymore.

PLUTO: I just…

SATURN: Shush! Don’t make me come over there.

URANUS: It's okay, Pluto. Saturn is a bit of a… luna-tic. Get it? Luna? Moon? Because he has so many moons? Get it?

SUN: (sarcastic) As usual, Uranus, your humor is both mature and necessary and makes us all stop and examine our humdrum lives. Can we please start? Please?

JUPITER: Yeah, uh… why are we here?

SUN: Great question, Jupiter. Great question. Let’s begin. I call this meeting, finally, to order. Any old business? Mercury?

MERCURY: You’ll be pleased to know that according to my calculations all orbits are going according to schedule.

VENUS: Oh, Mercury, you’re so smart. What ever would we do without you?

MERCURY: Uh… I… uh…

SUN: Moving on. Any eclipses we need to know about?

MERCURY: None that we haven’t already discussed.

SUN: Excellent. How is the space cleaning process going?

MERCURY: Earth’s atmosphere needs clearing of excess space junk, including the Fox Satellite. The asteroid belt has been inspected and is in desperate need of cleaning.

URANUS: We don’t want to lose the asteroid belt. Our pants will fall down. Get it?

VENUS: (laughs) Oh, that was funny! You’re so funny!

SUN: Venus, let’s keep the flirting to a minimum, okay? Any other old business?

PLUTO: Um, there is…

SATURN: Pluto! Shut up!

MARS: its okay, Pluto. We’re all just objects floating in space. Nothing means anything.

SUN: Um… Mars, I… Anyway, back to the topic at hand… New business. Great. Okay. I called this meeting today because… well to be completely honest with all of you, I’m exhausted.

JUPITER: Exhausted?

SUN: Tired, Jupiter. I’m tired.

NEPTUNE: What?

SATURN: (yelling) Neptune, either move closer or just accept that you can’t hear what’s going on.

NEPTUNE: What?

SUN: Whatever. The point is I am tired and I need a vacation.

VENUS: Oh you poor baby… But, sunny honey, why on Earth are you so tired?

EARTH: Did someone say my name?

MERCURY: Idiomatic phrasing.

EARTH: What have I told you guys about doin’ that?!

URANUS: Yeah, guys, we have no earthly business abusing her name like that. Get it? Get it?

SUN: Uranus, that wasn’t even funny. It was just awkward. Come on. Can we please focus on me for like a minute!?

SATURN: Oh, because revolving around you isn’t enough. By the way you talk, you would think that you are the center of the universe!

URANUS: Don’t worry, Sun. “Galileo Galilei” over here is just jealous.

SUN: Guys, this is actually really important. I am going on vacation. I’m just going to do it. Probably head out to the Andromeda Galaxy for a little rest.

MARS: Rest. To die, to sleep… no more… It’s not going to help. Nothing helps. We sleep and we eventually have to wake up and face our own existence.

VENUS: Why do we even invite Mars? Gives me the creeps. But I could change him…

MARS: What does it matter? We go in circles. Nothing changes. Nothing ever changes.

SUN: The point is that I need someone to take my place while I’m gone. Someone has to be the center of the solar system, right? Right. I’ll only be gone for a little while, so it won’t be that much of a time commitment.

JUPITER: Wait, so… you’re leaving and we’re going to need someone to be you for a while?

SUN: Yep, that’s… That’s exactly it. Good job Jupiter.

JUPITER: See, I’m smart.

SATURN: (sarcastically) Yeah, and humans landed on Earth’s moon.

EARTH: It happened! It did!

SATURN: I still think you’re making it up.

EARTH: I’ll make you up!

NEPTUNE: What?

SUN: (yelling) Just go to sleep, Neptune!

VENUS: I still don’t get why you have to leave.

SUN: Do you realize how exhausting it is being me? I never get to sleep because, well, I’m the sun. It’s always bright. And hot. I have to keep my gravity pretty constant so you guys don’t spin off into oblivion, and I have very little company except for Mercury and he never stops talking.

MERCURY: I didn’t realize that you thought I…

SUN: (exasperated) Shh. Just… Shh…

URUNAS: Couldn’t you, ya know, sleep at night?

SUN: Hilarious.

JUPITER: I don’t get it.

EARTH: He’s the sun, Jupiter. He doesn’t have a night.

SUN: I am leaving. I am going on vacation and I am going to get some well-deserved sleep. That’s that. The real purpose of this meeting is to tell all of you this and to tell you that one of you is going to have to take my place.

URANUS: Oh, I get it, I get it. I humbly accept the position. Thank you, thank you. As my first act as leader-

SATURN: Oh, that’s funny, that’s hysterical.

URANUS: That one wasn’t a joke.

SATURN: I’m not laughing. You really think you can take care of the solar system by yourself, Uranus? You barely make acceptable puns.

EARTH: Oh, snap!

PLUTO: I think…

ALL: Shut up Pluto!

EARTH: I know how to solve all this. I think that I should be in charge.

MERCURY: You?

EARTH: They don’t call me Mother Earth for nothing. I’m all for nurturin’ and lovin’ and takin’ care of people.

VENUS: Oh, please. You? You can’t even take care of yourself.

EARTH: Excuse me?

VENUS: Global warming?

EARTH: Climate change! Climate. Change. It is different.

SATURN: Denial. Regardless of what you call it, it is clear that I should be in charge.

MARS: Clothes don’t make the man.

SATURN: Crazy planet says what?

MARS: Your many rings do not equate to power.

SATURN: Someone better make him shut up.

MERCURY: Don’t you think that if we had that ability we would have already implemented it?

JUPITER: …I don’t know what’s going on.

EARTH: Do you ever know what’s going on?

VENUS: Sunny, you can’t just go on vacation. We obviously can’t handle this. Not without you...

SUN: No, no, guys, it’ll be totally fine. I’ve figured it out. Jupiter is massive. He should be able to keep all of you guys in orbit while I’m gone.

JUPITER: Uh… what?

VENUS: Oh, not this guy. He’s cute and all… but dumb as a rock.

NEPTUNE: What?

EARTH: Ignore him. Just ignore him.

JUPITER: Uh… what is going on? Why am I the Sun?

SUN: No, we did the calculations and it… it works. I swear. It should be fine, right Mercury?

MERCURY: Well, fine is a relative term. SUN:… What?

MERCURY: It doesn’t… quite work out.

SUN: Mercury. You said it worked. You said I could go. I made plans to go. Away. From here.

MERCURY: I made a mistake?

SUN: A mistake?! Well… can we… what about one of the other stars?

MERCURY: They’re too far away. Plus I don’t think we want to mess up the constellations like that, do we?

SUN: But… but…

URANUS: I guess a vacation wasn’t ever in the stars for you, man. Get it? Get it?

SATURN: We always get it!

URANUS: You never laugh…

VENUS: I laugh.

MARS: Humor is all relative. Funny doesn’t matter. Laughing now? Who cares. In ten thousand years-

PLUTO: Shut up, Mars! Shut up everyone!

JUPITER: Woah. Was that Pluto?

EARTH: Oh, snap! What just happened up in here?!

PLUTO: Look, it’s not my fault I’m not a planet anymore, alright guys? But I am still a part of this solar system and I should still have representation. Now Sun, I think it isn’t fair that you can’t take a vacation. But it is also true that we need you. We don’t work well together without you. As for the rest of you, it didn’t used to be like this. We used to get along. We used to be a solar system. Now what are we? We’re just a bunch of rocks, floating along, with no regards for each other’s feelings. I’m ashamed. Of all of you. I used to be proud to be a part of this system. But now… I’m glad I’m not. But we can change that. We just need to go back to what made us great in the first place: a common gravitational pull to this guy right here. And that is one of the strongest bonds of all.

JUPITER: That was beautiful.

SATURN: Yeah, uh, yeah. Well said, Pluto.

VENUS: Pluto, I know you’re not a planet anymore, but I just want you to know… You’ll always be a planet to me.

SUN: Look, guys, I’m sorry that I was going to abandon you all. I just get so stressed sometimes I could super nova.

EARTH: (gasps) We never knew you felt like this!

MERCURY: You can’t leave things like that bottled up! No wonder your percentage of solar flares has dramatically increased!

SUN: No, but, after what Pluto just said, I realize there is no place I would rather be than right here.

NEPTUNE: What?

SUN: (yelling) I said I’m staying, you deaf old geezer!

NEPTUNE: Good!

VENUS: Sunny, we all know how you feel. We all could use a change sometimes.

SATURN: Yeah, but change comes in the most unexpected of places. Who knows? Maybe a black hole will form just outside the galaxy. Maybe we’ll discover that space isn’t infinite and at the edge there is a sign that says “dead end” or something! Maybe we’ll discover life on Mars at some point.

MARS: Life is meaningless.

SATURN: Or maybe not. Probably not.

EARTH: And maybe, when Haley’s Comet comes back around in a couple years, we can throw a big party.

URANUS: You know how you throw a space party? You planet. Get it? Get it?

JUPITER: (laughing ridiculously) I get it! I get it!

PLUTO: Um, guys?

MERCURY: Yes, Pluto?

PLUTO: I just wanted to say thank you… for inviting me.

SUN: I mean, who cares what those folks at NASA think, anyway? It’s not like Earth has the last say in everything.

EARTH: Aw no, child. Those people down there still think my moon is made of green cheese.

MERCURY: Uh, I don’t think anyone thinks that anymore.

VENUS: Oh look guys! A shooting star! Everyone make a wish.

MARS: (surprisingly optimistic) I don’t have anything I want to wish for.

SUN: Me neither, Mars. Me neither.

END PLAY
```

---

## IC-1077: Fast Food Fairytale

- Title: Fast Food Fairytale
- Author (byline): Mitchell Whittenhall
- Work: Fast Food Fairytale
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, BURGER KING, DAIRY QUEEN, KFC, ROBIN, BASKIN, BASIKIN, DUNKIN, WENDY’S, WHOLE FOODS
- Teaser before the introduction: No
- Spoken words (computed): 1123
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
NARRATOR: Let me tell you a story, kids. Once there was a beautiful kingdom known as the Kingdom of Drevthru. In the Kingdom of Drevthru there stood a White Castle atop a mountain overlooking a great empire. The leader of this monarchy was a brave ruler named Burger King who, alongside his wife, Dairy Queen, kept the kingdom in blissful harmony.

Fast Food Fairytale by Mitchell Whittenhall

BURGER KING: Wife! The messenger has arrived!

DAIRY QUEEN: Oh, goodie! Burger King, what news doth Sonic bring?

BURGER KING: Allow me first to observe the disclosed information within. Boy, am I glad that our kingdom has been able to go so long without a single war!

DAIRY QUEEN: What does it say, my liege?

BURGER KING: The Health Nuts have declared war on us.

NARRATOR: The Health Nuts, a threat to the stability of Drevthru for eons since the foundation of its … foundation.

BURGER KING: Summon Colonel Canders! 1

NARRATOR: Colonel Canders, the man who invented one of the most ingenious weapons to fight against the Health Nuts … the fried chicken. It took the health-benefits of simple protein fryed it in liquid grease. His name was Colonel with a K, Fredrick with an F, and Canders with a C – he went by his initials: KFC.

KFC: Yes, my lord, what is thy bidding?

BURGER KING: The Health Nuts have begun an uprising!

KFC: My greasy chicken tenders!

BURGER KING: Our preparations must begin.

KFC: Shall we invite Chick-fil-a?

BURGER KING: No, that’s a Christian company, he’s too controversial to make fun of.

KFC: Ah, good point.

BURGER KING: My queen!

DAIRY QUEEN: Yes, my king?

BURGER KING: It is time to use the One Onion Ring To Rule Them All.

NARRATOR: Preparations began thusly from the top of Mountain Dew to the bottom of the Fanta Sea. The Queen called on her two most loyal servants, Baskin and Robin, commanding them:

DAIRY QUEEN: You must journey to the edge of Drevthru, where food is no longer fast, carrying only this, the One Onion Ring To Rule Them All, and you must –

ROBIN: One Onion Ring To Rule Them All?

DAIRY QUEEN: One Onion Ring To Rule Them All.

ROBIN: One Onion Ring To Rule Them All?

DAIRY QUEEN: Yes Robin, please stop interrupting me, And journey to Mount Dew, which lies in the heart of Vegan Ville, and drop this onion ring into the liquid carbonation of the mount. This will cause the carbonation to fissure and destroy the Health Nuts once and for all … I read that in a book once.

BASKIN: A book?

DAIRY QUEEN: Yes, the ancient scrolls of Diabetica upon which our laws are based.

BURGER KING: Hey! I know I haven’t been in this scene yet, but here’s a map!...

NARRATOR: The two began their journey. Nuff said..

BASKIN: ROBIN, do you think we can make it?

ROBIN: I’m not sure … Dairy Queen will have one heck of a blizzard if we fail.

BASKIN: Oh, that joke was just cheesy.

ROBIN: Extra cheese is fifty cents, Baskin …

BASKIN: Eck! In bad taste …

ROBIN: I actually enjoy the cheese!

BASKIN: Stop joking around! You’re already falling behind.

ROBIN: I guess I have to … ketchup. Sorry. Baskin, where do we go first?

BASKIN: It says on the map we need to cut through some fields on our way to Vegan Ville.

ROBIN: Whoa, this is a massive farm.

NARRATOR: The two are on a massive farm. Are you even listening?

BASKIN: This must field must be Farmer McDonald’s

ROBIN: I’ve heard that once he joined the Drevthru forces child obesity skyrocketed.

BASIKIN: This must be where they harvest the pink goo. Well Robin we must get moving.

ROBIN: It says on the map to head this way.

NARRATOR: After journeying hours in the correct direction, they found themselves. Then, they espied a small hut on the Drevthru - Vegan Ville boarder.

BASKIN: Robin, come! I feel we will find direction in this hut!

ROBIN: I feel you are correct Baskin.

DUNKIN: Hello, fellow fast food friends! My name is Dunkin! More famously known as DUNKIN Donuts, second in the Drevthru military only to Colonel Canders.

BASKIN: Dunkin Donuts! Pleased to meet you, sir.

DUNKIN: Shame you arrived now, for my wife just left.

ROBIN: That is a shame … I’d like to have met her.

DUNKIN: Ah, yes she’s quite a Bell!

ROBIN: What’s her name?

DUNKIN: Taco.

ROBIN: Oh. Ooooh

BASKIN: We’re lost and need directions to Mount Dew.

DUNKIN: Mount Dew! Why on earth would you want to go there? That’s in Vegan Ville!

BASKIN: We’re on a mission from Queen Dairy to drop the One Onion Ring To Rule Them All into Mountain Dew and destroy the Health Nuts forever. Say, where is this little tent?

DUNKIN: This little tent is the frontier against the Health Nuts – y’know, it’s Pizza Hut.

ROBIN: Wow! That’s wigwam Wonderful! Where can we find Mountain Dew?

DUNKIN: Like, how I would get there?

BASKIN: Yes! How would you get there?

DUNKIN: Well, IHOP,

ROBIN: OK!

DUNKIN: You should take the Subway.

NARRATOR: They got off the Subway at Vegan Ville – a dark and desolate place where the food made people feel good about themselves. Ridiculous.

BASKIN: This way, Robin.

ROBIN: Do you think this is right?

BASKIN: No, this is left.

ROBIN: Isn’t that wrong?

BASKIN: No, it’s right.

ROBIN: But you just said it was left.

BASKIN: No, left is right.

WENDY’S: AHHHH

ROBIN: What was that?

WENDY’S: Help! I’m right here!

BASKIN: Who are you?

WENDY’S: My name is Wendy’s and I’m being held hostage here in Vegan Ville!

ROBIN: Why?

WENDY’S: Because quality was my best recipe! ROBIN: Ah, a damsel in distress!

WENDY’S: Yes! In … dis dress!

ROBIN: Baskin, we have to save her!

BASKIN: Robin! We’re already 8 minutes into the speech, we don’t have time for another subplot!

ROBIN: Good point! I can see Mountain Dew, it’s over there!

WHOLE FOODS: Bwahahaha! Behold, I, Whole Food! I put holes in foods … like you!

BASKIN: So that’s how it is! Robin, free Wendy’s! I’ll take on this grass-fed abomination!

WHOLE FOODS: I will smear you like humus.

BASKIN: COME AT ME, BRO!

WHOLE FOODS: We aren’t even related, but kay, bruh! You are stronger than expected! I’ve had a flavor of your fury.

BASKIN: Just one flavor, but I have 31 in all! Narrator: Baskin beats the ever-loving gluten out of Whole Foods.

WHOLE FOODS: You’ve defeated me! How did you do it?

BASKIN: You really want to know?

WHOLE FOODS: Yes, tell me! I must learn from you!

BASKIN: Because I’m Baskin! Ba-na-na-na-na-naaa Baskin!

ROBIN: And Robin … I kind of helped.

NARRATOR: The two, having defeated Whole Foods, marched the rest of the distance to Mountain Dew, a bubbling cauldron of green, acidic sugar. They totally forgot about Wendy’s.

BASKIN: Holy Whoppers, Robin! This is Mount Dew.

ROBIN: Baskin, Dunk in the One Onion Ring To Rule Them All … I mean, you are the hero.

BASKIN: Thanks, Robin. Here we go! This is to destroy our enemies! To remain triumphant! To cure this land of its healthiness and to come out as the victor in this 10-minute war. THIS IS FOR FREEDOM!

NARRATOR: The volcanic explosion that followed, rather than destroy the Health Nuts, combined the two kingdoms’ powers – becoming the all-powerful abomination known only as ‘the church potluck’.
```

---

## IC-1078: Ho, Ho, Ho! A Play by Taylor Shann Copyright 2009 by Taylor Shann

- Title: Ho, Ho, Ho! A Play by Taylor Shann Copyright 2009 by Taylor Shann
- Author (byline): Not specified
- Work: Ho, Ho, Ho! A Play by Taylor Shann Copyright 2009 by Taylor Shann
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: TIMOTHY, ADAM, JOSE
- Teaser before the introduction: No
- Spoken words (computed): 1276
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
OCTOBER 2009

ADAM, TIMOTHY and JOSE sit in various stages of Santa suits. They are waiting.

ADAM is just staring into space, TIMOTHY is looking at a printed script, and JOSE is playing with a digital device.

TIMOTHY: Ho Ho Ho.

Beat.

TIMOTHY: Ho Ho… HO.

Beat.

TIMOTHY: Ho HO Ho…. Ho.

Beat.

TIMOTHY: Ho-

ADAM: Stop. Just. Please, stop.

TIMOTHY: Hi, I’m Timothy. Are you here for the job? Er, audition? No, I guess it’s a job. The-

ADAM: I didn’t just mean, stop Ho-Hoing, I meant, stop talking.

JOSE: (to his digital device) Oh yeah, you LIKE that, Bitch.

ADAM and TIMOTHY look at JOSE, who keeps playing.

TIMOTHY: I’m a little nervous. I’ve never gone out for one of these things before.

ADAM: You’re still talking.

TIMOTHY: But people said I have a Santa laugh. I’m not even sure what that means.

ADAM: Oh my God, you’re still talking.

TIMOTHY: …I’m sorry, am I being rude?

ADAM: I have a migrane. Okay? (quietly) Okay? (mouths, ‘Okay.)

TIMOTHY nods, ADAM closes his eyes and rubs his head, JOSE gets more animated with his device.

JOSE: Yeah. Yeah. I rule you. I RULE YOU! YES! YES! No. NO! SHIT! SHIT! NO! URGH! (hangs his head in disgust, looks at TIMOTHY) I was this close. THISCLOSE. Shit.

TIMOTHY: Hi, I’m Timothy.

JOSE: Jose, man, what’s up. You guys up to play the big man?

TIMOTHY: People say I have a Santa laugh.

JOSE: No shit. People say I need to pay bills. Crazy. (to ADAM) What about you?

ADAM: (in disbelief) Weren’t you listening?

JOSE: Nope. (pulls out a film cannister) Anyone know how long they’ve been in there?

TIMOTHY: They said they need time to deliberate.

ADAM: Are you-?

JOSE: (pulls out rolling papers) I’m partaking. Do you, uh… want to partake?

ADAM: Are you rolling a joint?

JOSE: Are you a dick? (begins to roll a joint)

A door opens, we hear an offstage voice say “NEXT.” ADAM gets up with a huff, looking at them with disgust. TIMOTHY gives a thumbs up. ADAM stomps out for his audition.

TIMOTHY: I’m so nervous!

JOSE: Hey. Relax.

TIMOTHY: Are you an actor, Jose?

JOSE: Nah man, I’m a man of leisure. (looks at his work) You want?

TIMOTHY: No thanks, I shouldn’t have tobacco. It makes it harder to sing. In your throat.

JOSE: We gotta sing for this?

TIMOTHY: Oh, I don’t think so. I’ve never actually acted before. Or auditioned before.

JOSE: (thinks, puts joint in his ear) What do you do?

TIMOTHY: I got a degree in history from University of Indiana.

JOSE: So you’re trying to pay back some loans?

TIMOTHY: No, I’m unemployed. I just want to…. I just want to ROCK THEIR SOCKS. (beat) If you know what I mean.

JOSE: Sure, if you want.

TIMOTHY: You know what they say… or… sing. Hi-diddle-de… an actor’s life for me… do do do do dee dee do do- (he is being stared at) do do do…. De… (beat)

JOSE: You’re, uh, not a New Yorker, are you?

TIMOTHY: I’m from Indiana.

JOSE: Yeah. Yeah, that, uh, yeah. So you just moved?

TIMOTHY: No, I just moved. Three months ago.

JOSE: Alright. Really? (TIMOTHY nods) So what the hell?

TIMOTHY: Well it’s not one’s fault. I was part of this program to teach? To teach and get your degree?

JOSE: Oh yeah, I saw those ads on the subway, and then, uh, I did nothing. Yeah. So what happen, you couldn’t cut it?

TIMOTHY: The program was delayed, it’s no one’s fault. I just have to wait.

JOSE: How long?

TIMOTHY: Two years.

JOSE: (long whistle) Shit.

TIMOTHY: So, I’m just, uh… well. (beat) I’m so nervous!

JOSE: I really wouldn’t sweat it. (pulls out his device, starts playing again)

TIMOTHY: Why would you say that?

JOSE: (shrugs) My uncles the manager. So I’m probably gonna get it. So. Don’t worry about it.

TIMOTHY: (crestfallen) Oh.

ADAM re-enters, sits. TIMOTHY doesn’t move. JOSE keeps playing.

ADAM: Yeah, they want ‘the tall one’ next.

TIMOTHY: Oh. (looks around) Oh! (stands) Well, Good luck, me.

ADAM: You don’t want good luck.

TIMOTHY: What?

ADAM: It’s bad luck to say good luck.

JOSE: Yeah, in Russia, it is. Good luck man.

TIMOTHY: (confused) Thank you? (leaves)

ADAM and JOSE stare at each other.

JOSE: Did you rock their socks?

ADAM: Don’t talk to me.

JOSE shrugs, begins playing his device again. ADAM stares out, taking his hat off.

ADAM: That was the shortest audition I’ve ever had. (pause) I really need this job.

JOSE: You got this game? (not looking up) It ROCKS.

ADAM: I really, really need a job. Any job.

JOSE: They’re hiring at the Taco Hut. (keeps playing) Down in the, ah. Food Court. (keeps playing) There’s a little pamphlet that says, “are you SPICY enough?” (keeps playing) Because, you know, Tacos are spicy. (keeps playing) You gotta be spicy. I guess (keeps playing) Well? Are you?

ADAM: Am I.

JOSE: (stops playing, looks up) Are you spicy enough to sell Tacos at the Taco Hut?

ADAM: I have an MFA in acting.

JOSE: No shit? I got through high school. So what?

ADAM: …. I don’t know.

JOSE laughs.

JOSE: You’re alright, man.

ADAM: I don’t know.

TIMOTHY comes out, with a smile on his face.

JOSE: (playing again) How’d it go man?

TIMOTHY: Well, you know, I gave it my best. And that’s all anyone can ask.

ADAM: Shut up.

JOSE: Hey, man, you shut up.

TIMOTHY: They’re asking for- well, the last but not least-

ADAM: Shut up.

JOSE: You shut up.

ADAM: Shut up!

JOSE: You shut up.

ADAM (grabbing the device) SHUT THE F-

TIMOTHY: (pointing to JOSE) They, uh, they, uh- want-

JOSE: (takes the device back) I lost. Thanks.

JOSE leaves. TIMOTHY takes off his hat, hurt.

TIMOTHY: I don’t understand why you have to be so mean.

ADAM: Oh, grow up.

TIMOTHY: No, that has nothing to do with it. You’re rude. You’re just… rude. And there’s no call for it. Your mother would be ashamed.

ADAM: My mother is a- don’t look at me like that. You can’t look at me like that. You- (tears off santa hat) I hate this. I hate this. I hate I hate I hate that I can’t find work.

TIMOTHY: Acting work?

ADAM: No. (beat) Well, yes but no. Paid actor work is hard, doing a friend a favor for free is easier, but work. The bills, paying the bills work. I had a really shitty office job… that paid enough. You understand? I could check my email and bitch about it all day. I had the HR ladies wrapped around my finger, I would be fired last, you know? Only when the sky was falling. Only when- And I had health care. It was bad health care, but it was enough. And then I could audition and act. And I would watch the tonys every year and drink just awful champagne and just know, know that I was better than all those bitches up there. And I didn’t have to wait tables, which I couldn’t do anyway; and I didn’t have to wear a tie, just a jacket. And… And-

TIMOTHY: It sounds wonderful.

ADAM: It was awful. It was a pain in the ass! (beat) But it was mine. And now I’m here. And I hate Christmas. I hate Santa. I hate that this is what I’m reduced to. I hate that this… is the only place that is hiring.

TIMOTHY: They’re hiring at the Taco Hut.

ADAM: I KNOW THEY’RE HIRING AT THE TACO HUT.

A long silence.

TIMOTHY: I don’t know if this helps, but (puts on his hat)… Ho Ho Ho.

ADAM looks at him. JOSE walks back in, sits and begins playing again. TIMOTHY and ADAM look at him, then each other. Silence. Finally:

ADAM: Well?!

JOSE: (doesn’t look up) What? Oh. (looks up) Yeah, man I got the job. So. Go home.

ADAM: What?

TIMOTHY: (a little crestfallen) Well, congrats to-

ADAM: That’s impossible.

JOSE: Yeah, so. (goes back to playing)

ADAM: No. No. No.

TIMOTHY: ….but, yes.

ADAM: NO.

TIMOTHY: His uncle’s the manager, so, he told me he pretty much had the job.

ADAM stares in disbelief.

ADAM: What? But then- why bother with the audition? If it was staged, why the farce? No one cares. No one cares, it’s Santa, no one cares- I could have been searching, I had an-

ADAM screams. Silence.

ADAM: God damn every part of every molecule of everything.

ADAM storms out. TIMOTHY stares. JOSE doesn’t look up.

JOSE: What a dick.

TIMOTHY: Well, good luck with everything.

JOSE: Hey, man. (beat) They’re hiring elves. I could put in a word.

TIMOTHY: But I don’t look like a elf.

JOSE: I don’t look like Santa. But, hey, 9 bucks an hour. I was going to ask him too, but (shrugs)

TIMOTHY: 9 dollars an hour?

JOSE: (takes the joint out of his ear, searches for his lighter) 9 dollars an hour.

TIMOTHY: (thinks, then looks out the window) It’s snowing.

JOSE: (finds the lighter, with a smile) Ho Ho Ho.

Fade out.
```

---

## IC-1079: Hot Dog Time Machine

- Title: Hot Dog Time Machine
- Author (byline): Alan McGuire
- Work: Hot Dog Time Machine
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2044
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
“Hot Dog Time Machine” by Alan McGuire

(Josh enters through the kitchen door)

Josh: Hey Dad, I--

Dad: Josh, sweetie! Boy does my baby boy have perfect timing. Look--I just knitted you the cutest little outfit! (Hands Josh a onesie)

Josh: A onesie? Dad. I'm 17. I'm exactly 17 times too old for this. Not to mention this onesie is smaller than my face.

Dad: Fine. That's fair. I guess you don't love your father anymore!

Josh: Dad...

Dad: I'll just go throw myself off a bridge and die in a river of fire so I don't have to bother you with my love and affection anymore!

Josh: Dad. There's no such thing as a river of fire. Look, I came in here because me and my friends want to go to this concert tonight, and--

Dad: And you told them 'too bad, I'm watching Matilda with my Daders!'

Josh: Actually, I told them my dad needs to stop calling himself 'Daders'. Seriously, why are you always acting like such a…a...

Dad: A what? I’ll tell you what I told you the first time you played with Legos: spit it out, Josh!

Josh: You always act like a clingy mother!

Dad: (shrieks) Joshua, that is so sexist! I didn't give birth to you just so you could demean women!

Josh: You didn’t give birth to me, Dad! Look. There's no reason I shouldn't be allowed to go to this concert. I'm leaving for college in a few months. When I'm there, I'll be out doing whatever I want without you around, trying to get me to comb my hair every two seconds.

Dad: But it gets so messy! (He licks his hand, fixes Josh's hair)

Josh: (knocks his hand away) Dad. I'm too old for you to treat like a baby anymore! There, I said it. Layin' it all out there. You can stop staring at me like a maniac now.

Dad: Joshua Tree-Trunk Madison. I do no such thing! Treat you like a baby, yeah right. Now hurry up and eat this sliced up hot dog and fish sticks before they get cold. Oh, sorry, I forgot...here's a juice-box to wash it down!

Josh: No! Ah! You! Invalid! I'm not a kid anymore, Dad! You know what I'm going to do? I'm going to go down to the freezer in the basement, get a hot dog, microwave it, and eat it whole—like an adult!

Dad: Joshie-poo--

Josh: My name's Josh! Josh Tree-Trunk Madison! Get it right, ugh!

(Josh storms out of the kitchen, heads down the basement stairs)

Josh: “Joshie-poo”? My dad is re-donk-ulous. (He opens a large freezer) Why would you ever put hot dogs at the bottom of the freezer? They're like the most important food group. (Reaches into the freezer) Come here hot doggie-dogs...ugh, come on, I need to show my dad my manhood. (Can't reach) Son of a bratwurst. Dad must have the wingspan of a pterodactyl! Alright, here goes nothing...

(Josh stretches all the way into the freezer. He reaches so far that he suddenly falls into the freezer)

Josh: WHOA!

(The freezer magically explodes with time travel. Once transported, Josh gets out of the freezer)

Josh: Oh my god. That was the hottest freezer I've ever been in! (Looks around the basement) Wait. Did Dad redecorate the basement while I was in there?

Dad: (From upstairs) Joshie-poo! Your friend Bobby's here!

Josh: Yeah, sure! (Leaving the basement) You're not going crazy, Dad. I'm sure it's my friend Bobby that I haven't seen since I was five because he was so stupid he--

(Josh opens the door. His jaw instantly drops)

Josh: Oh my god it's Bobby.

Bobby: Hi! I brought you a stick. (Hands him a stick) Wait, I forgot...I brought you two sticks! (Hands him another stick)

Josh: Uh, hi. You're a little kid...

Bobby: Do you want to go eat some Legos?

Josh: First of all, yes. Second of all, I'm pretty sure I got locked in that freezer and am hallucinating this entire experience as I drift into a coma. And thirdly, I'll definitely get arrested if I hang out with a little kid.

Bobby: Wait. Little kids can't hang out with little kids? Are we not supposed to hang out with people our own age? Was I supposed to get in that guy's van--

Josh: Hold on shut up a second...you think I'm a little kid? (Laughs elegantly) That is rich! Rich, I say! No dude, I'm seventeen. Just look at my biceps. Plus I almost grew like four hairs on my face the other day. Things are getting pretty serious on my body.

Bobby: That's gross. Do you want to go throw rocks at each other?

Josh: Oh my god, I remember this day. You tried to put a frog in the oven, then I realized that maybe I shouldn't be hanging out with you. Holy sweet lord baby jesus buns...did I go back in time?!

Bobby: (pause) Do you want to go put a frog in the oven?

(Dad enters with a tray of cookies)

Dad: Hello boys! Don't mind me--just about to bake you fellas some cookies!

Bobby: Sorry, we need the oven.

Josh: Dad, this is exactly what I was talking about! You never let me do my own things! Here you come, interrupting my play-date with this moronic five year old just to make us some dumb cookies.

Bobby: But that's the only reason I'm friends with you.

Josh: You...wait, what?

Bobby: I only come over because your dad always makes us cookies. Otherwise, I'd never talk to you. Not after you peed your pants in front of the whole school.

Josh: Oh my god, that was like two times! Alright, look. I'm seventeen now, I've got chest hair on the horizon, I don't need any more of this. I'm out.

Bobby: But...but--

Josh: Just put the frog in the microwave, Bobby! The microwave! It makes a cool explosion and you can still eat your cookies. There ya go, you little moron! Bye! Have fun losing a finger in eighth grade!

Bobby: I think I want my sticks back now.

(Josh stares him down, takes out a stick, breaks it. Bobby gasps, Josh takes out other stick, breaks it. Bobby spazzes)

Bobby: Now how am I supposed to scratch my eyelids?!

Josh: I'll see you in twelve years, Dad.

Dad: But, but...the cookies will be cold by then!

Josh: Well...then...why don't you just throw them in your river of fire!

Dad: Josh, there’s no such thing as--

Josh: (Turning to leave) Back to the future!

Dad: Is a good movie, but--

Josh: BYE!

(Josh exits the kitchen, heads down to the basement)

Josh: Oh my god he is so infuriating. “Let me bake you cookies, Josh. I'm the only reason you have friends, Josh.” Who needs that! (He opens the freezer) Okay, so I just get back in the freezer and it'll take me back to now. Right? Sure. Work your magic, hot dogs!

(Josh climbs into the freezer and is again transported through time. He climbs out of the freezer)

Josh: Wow. I'm gonna smell like hot dogs the rest of my life. (Looks around) Well, the basement looks different...That's a good sign. (Josh walks out of the basement, stops cold when he sees his middle school friend Cheesefish)

Josh: Cheesefish!

Cheesefish: Sup.

Josh: Whoa, I haven’t seen you since middle school! Oh no, come on hot dog-gods...anything's better than middle school!

Cheesefish: Like chainsaws!

Josh: Yes, Cheesefish. Precisely. Chainsaws. Man, I don’t get why my dad ever made me stop hanging out with you. You have the coolest name ever--

Cheesefish: Cheesefish!

Josh: You have creative and awesome ideas--

Cheesefish: Like when I light things on fire!

Josh: And you...have got something in your hands...

Cheesefish: Chainsaw!

Josh: Oh. Cool! Is that for a science experiment, or...

Cheesefish: I really hate trees today. AHH! (He chainsaws down some trees) Stop looking at me, trees! Nobody thinks you’re great!

Josh: Yeah, uh...Dude, that's my favorite game to play too...Woo, yelling at trees. You smell, trees! Go back to...the soil! My middle name is in no way related to you.

Cheesefish: Take that, trees! Not so cocky without your faces, huh?

Josh: Man. I'm sure glad they're letting you handle dangerous machinery again. So...when did they let you out of juvy?

Cheesefish: They didn't.

Josh: See? There's nothing dangerous about being friends with you...Just two normal dudes hanging out, chainsawing things...Ye—yeah! Oh god, now what's that?

Cheesefish: (Holding a firecracker) Firecracker! I'm gonna blow up that cocky treehouse. Stop looking at me, treehouse! I bet you can't even read! (Lights firecracker)

Josh: Cheesefish, no! That's where my dad does his zumba!

Cheesefish: Who cares, you hate your dad like the world hates trees.

Josh: No I don't, leave his treehouse alone! (Rips away firecracker, throws it into distance) My dad was right to make me stop being friends with you. It's taken me seventeen years and a lot of time travel, but I'm finally starting to realize--

Cheesefish: Whoa, sweet throw dude! Right through that cop car's sunroof!

Josh: Oh my god! Cop cars have sunroofs?!

Cheesefish: It's this spoiled generation, man. Oh look, here he comes to say hi! Hi police officer! Yeah, he's the one who made that mad sick throw.

Josh: Stop, what's the matter with you Cheesefish?! You used to be so normal!

Cheesefish: I have an addiction to chaos. It’s a disease. Oh cool look how shiny his gun is!

Josh: AH! Hot dogs, get me out of here!

(Josh runs away, rushes into basement)

Josh: Dad, please forgive me!

(He gets into the freezer, travels through time, gets out of the freezer)

Josh: (Looking around) Seriously? These hot dogs suck at time travel. Is this even our house? (Exits the basement to see...)

Sally: (crying hysterically) Josh! You’re back!

Josh: Uh, yeah. Back to...where I started, right? Present day? Eh?

Sally: I know we both said some hurtful things, and I'm sorry I ate all the ice cream, but I think we’ll have a better marriage because of it--

Josh: Whoa, marriage?! Hold your horses, mamacita. I don’t even know you, plus you look way too old for me.

Sally: WHAT?!

Josh: No! I just mean...I can't really marry you, I'm only seventeen...

Sally: You’re 17?! And you wait until the morning of our wedding to tell me that?!

Josh: Uh...surprise!...?

Sally: I have spent thirteen days falling in love with you! Baking you cookies, baking you pies, baking you cheesecakes...

Josh: All you do is bake?

Sally: That’s not all I do. (Terrifyingly pulls out a knife) I’m also a certified butcher. (raises knife) And someone just ordered a tender-loin.

Josh: AH! DAD HELP! My wife is trying to bake me!

Sally: Butcher you!

Josh: Different words, same result! AH!

Sally: (Approaching menacingly) If I can’t have you, no one can! Except for a hungry customer. I think Steve will like you. Or maybe Janet.

Josh: I don't want Steve or Janet to eat me! DAD! I'm sorry I've been such a jerk when you were always just looking out for me. Please help, I need you and always have! Distract her with some baked goods! A cannoli or a pear tart or some pain au chocolat, for example!

Sally: Who are you talking to? Your dad’s not here anymore. And I hate pain au chocolat.

Josh: AH! She has terrible taste!

(Josh runs down to the basement, gets in the freezer)

Josh: Please, oh sacred hot dog gods, let me talk to my dad again! Hot dogs, time-travel me!

(The freezer explodes with time-traveling magic. Josh then gets out of the freezer)

Josh: Oh my god! Brainfreeze.

Dad: Uh. Why did you just crawl out of the freezer?

Josh: Dad! Am I back?

Dad: No, you’re Josh. (Laughs heartily) Oh, I'm a hoot. How long were you in there for? I doubt you beat my record.

Josh: About 30 years.

Dad: And I've still got the crown. Look, Joshie-poo-honey-pie-bear-sweetie-schnookums, I’ve been thinking. About the concert--

Josh: No Dad, it’s fine. I've been a total jerk recently. You have done so much for me...you made me friends as a kid, you've kept me away from danger...Anyway, I know I don't say this much, but I--

Dad: Oh shush shush shush, stop talking shut your mouth. You've gotta get going; you're gonna miss the show!

Josh: Wait. I can go to the concert now?

Dad: Of course, you precious little angel. I don't want my worrying to make you miss out on such a snazzy night. “Death Bloody Rain Slaughter” used to be my favorite band too, you know! Well, second to ABBA of course.

Josh: Obviously.

Dad: Make sure you buy me a t-shirt though. Extra large this time--I want to be able to live in it.

Josh: I’ll get you a blood-squirting mask too.

Dad: You just get me.

Josh: But seriously Dad...thanks again. For everything.

Dad: You are welcome, my little pumpkin spice latte! Oh, by the way. Ah, I rhymed! (Giggles)

Josh: What Dad.

Dad: Don’t eat the hot dogs at the bottom of the freezer. I'm pretty sure they’ve been in there since the 1850’s and could make your brain hallucinate wildly from any contact.

Josh: Right. Radioactive hot dogs. I should've seen that one coming. Unrelated: can you take me to the hospital?

Dad: Anything for you, my little hot dog!

Josh: Please. No more hot dogs.

The End
```

---

## IC-1080: INVESTIGATOR Q Copyright 2008 by J. J. Allen

- Title: INVESTIGATOR Q Copyright 2008 by J. J. Allen
- Author (byline): Not specified
- Work: INVESTIGATOR Q Copyright 2008 by J. J. Allen
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2042
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
NARRATOR
INVESTIGATOR Q
MR. PRESIDENT
MRS. PRESIDENT
PETCO OWNER
MONIQUE
TRANSLATOR
MRS. WHISKERS
MONICA
FORENSIC EMPLOYEE
KID
DEEP THROAT

NARRATOR. It all started one day in Investigator Q’s office...
INVESTIGATOR Q. I was assigned the case about two months ago, and finally, today, I know who did it.
Who committed this terrible crime they call murder. This was possibly the most complicated and strenuous
case I’ve ever had. The twists of this trial may confuse you. What I did to get some of the information for
this case isn’t my proudest work. But here, Mr. President, is who committed the crime. (Sliding file across
desk).
President: Are you positive this is who killed Mr. Whiskers? (taking the file but NOT opening it!)
INVESTIGATOR Q. I’m positive this is who killed your cat, Mr. President. But let me explain how I
realized who killed Mr. Whiskers, before you open the file. I started by investigating the scene of the crime.
I went straight to the Petco, on 24th avenue. After looking around for a little while, and buying a new litter
box for my cat, I began my questioning. I started by questioning your wife, who was there with him when
he was brutally murdered.
(at the Petco)
MRS. PRESIDENT. (sobbing) Ahhhh! Mr. Whiskers! Mr. Whiskers!!
INVESTIGATOR Q. Mrs. President, please calm down.
MRS. PRESIDENT. How the hell am I supposed to calm down!? My cat is dead. My cat is (sobbing)
dead.
INVESTIGATOR Q. How would you describe your reaction to his death, Mrs. President?
MRS. PRESIDENT. (sarcastically) Well, seeing as he died seven minutes ago, I’m pretty upset.
INVESTIGATOR Q. Understandable..now how would you describe your relationship with Mr. Whiskers?
MRS. PRESIDENT. What do you mean, relationship?
INVESTIGATOR Q. Well was it a friendship, or sexual, or platoni-
MRS. PRESIDENT. What in the world? Are you crazy? What type of nutcase are you!? Sexual relations
with a cat?
INVESTIGATOR Q. Just asking ma’am. Just asking.
INVESTIGATOR Q. I knew that I wasn’t going to be able to get any information out of her, so I
approached the store owner.
INVESTIGATOR Q. How was Mr. Whiskers murdered, sir?
PETCO OWNER. A man with a black mask on ran in here and shot that kitty!
INVESTIGATOR Q. Ok, for this investigation, don’t refer to Mr. Whiskers as kitty. He was a full-grown
cat, with three children! Have some respect.
PETCO OWNER. Sorry? A man came in and shot that cat - I mean Mr. Whiskers, right over there.
INVESTIGATOR Q. So tell me sir, how do you know it was a man? You told me he was wearing a mask.
PETCO OWNER. Well..I don’t know. How he walked?
INVESTIGATOR Q. Oh, so you're able to tell the sex of a person by how they walk?
PETCO OWNER. Um, well not necce-
INVESTIGATOR Q. (pacing very femininely) So tell me, am I a man or a woman? A man or a woman!?
INVESTIGATOR Q. I could tell that the Petco Owner wasn’t going to be of much assistance. I took my
investigation onto someone who was present at the scene of the crime.
INVESTIGATOR Q. Tell me exactly what you saw.
MONIQUE. Well, a guy with a black mask came in and shot that cat.
INVESTIGATOR Q. Which feline sir? We are in a pet store therefore there may be numerous "cats" here.
MONIQUE. The dead one.
INVESTIGATOR Q. Right. So describe this "guy with a black mask" to me.
MONIQUE. Well he had a black mask.
INVESTIGATOR Q. Are you being sarcastic with me.
MONIQUE. No I’m not being sarcastic at all.
INVESTIGATOR Q. Wow, I don’t like your attitude at all.
MONIQUE. I don’t like you at all.
INVESTIGATOR Q. Wow sugar dumplings let’s calm down.
MONIQUE. Did you just call me sugar dumplings.
INVESTIGATOR Q. Yes sugar dumplings, I just called you sugar dumplings. NOW, how would
describe this guy.
MONIQUE. He was probably 6’2, 6’3 pretty hefty guy.
INVESTIGATOR Q. Can you tell me the ethnicity of this man?
MONIQUE. Oh well he was wearing all black so I wasn’t able to really tell.
INVESTIGATOR Q. Oh, so he was an African-American.
MONIQUE. Well, not necessarily.
INVESTIGATOR Q. But you said he was black.

MONIQUE. Well he was wearing all black, I couldn’t see his skin.
INVESTIGATOR Q. Right. Well then, sir, that was probably his skin. He probably was naked. We now
have a naked cat murderer. Perfect.
INVESTIGATOR Q. I took my investigation elsewhere to get a little more background information on Mr.
Whiskers. I wanted to find out why somebody would want Mr. Whiskers dead. First I asked Mrs. Whiskers.
Now as you know Mr. President, Mrs. Whiskers is a cat so she doesn’t speak English. She probably speaks
Spanish or Portuguese or Italian or something foreign like that. So I brought in a translator to help our
interview.
INVESTIGATOR Q. So how many languages can you translate?
TRANSLATOR. About three hundred.
INVESTIGATOR Q. Good, very very good. (opens the door) Hi, Mrs. Whiskers, how are you?
MRS. WHISKERS. Meow...
TRANSLATOR. We’re interrogating a cat?
INVESTIGATOR Q. Do you have a problem with that?
TRANSLATOR. Unless this cat has learned how to speak-
Investigator: Hey, hey, hey. Don’t discriminate against cats who don’t know how to speak English. That
doesn’t make them any less of a cat. Now, let’s get back to the interrogation.
INVESTIGATOR Q. So, Mrs. Whiskers, how long were you and Mr. Whiskers married?
MRS. WHISKERS. (licks herself)
TRANSLATOR. (says nothing)
INVESTIGATOR Q. What did she say?
TRANSLATOR. Nothing.
INVESTIGATOR Q. Then what was all that licking about?
TRANSLATOR. Well she’s a cat.
INVESTIGATOR Q. Is she flirting with me? Because I am very willing to flirt back…..to solve this case.
(begins to lick himself) Do you like this Mrs. Whiskers? Is this what you want me to do?
INVESTIGATOR Q. As I told you, Mr. President, I’m not proud of what I had to do to get the
information, but Mrs. Whiskers provided us with valuable details: Mr. Whiskers was a cat, who sadly could
not speak. The next person I knew I needed to interview was someone who has dealt with presidential
scandals before. Therefore I hunted down Monica Lewinsky for an interview. It was very difficult to find
her, but I did.
INVESTIGATOR Q. (knocks on door) Monica! Monica!
MONICA. (opens door) Hello?
INVESTIGATOR Q. Hi, I’m Investigator Q; I’ve got a few questions for you Ms. Lewinsky.
MONICA. Is this a joke?
INVESTIGATOR Q. Have you ever met Mr. Whiskers?
MONICA. What? Who?

INVESTIGATOR Q. Mr. Whiskers, the president’s feline friend.
MONICA. Ok, how did you even find out where I lived?
INVESTIGATOR Q. Ok, Ma’am. My name is Investigator Q. Your name is Monica. Investigator.
Monica. I am an investigator, therefore I ask the questions ok!?
MONICA. I’m calling the cops.
INVESTIGATOR Q. After two weeks in jail for allegedly stalking Ms. Lewinsky I began to wonder if
there was anything I could do to find out who killed Mr. Whiskers. I had tried everything. But then I
realized that I hadn’t tested any evidence. So I collected the most important items from the crime scene.
Chew toys, fur, Mr. Whiskers himself, and other important items. I took them to a place called "Forensics
Galore". I assumed they did forensic investigations for crime scenes. I was very wrong.
INVESTIGATOR Q. So, can you do some testing for me?
FORENSIC EMPLOYEE. Um..I’m sorry?
INVESTIGATOR Q. I’ve got all the evidence right here, (pulling the items out of the bag, and placing
them on the table). Can you do some basic tests for me?
FORENSIC EMPLOYEE. You just emptied a dead cat on my table dude!
INVESTIGATOR Q. So?
FORENSIC EMPLOYEE. Look dude, if you're looking for a humorous interpretation piece, I can help you
but otherwise-
INVESTIGATOR Q. What, you think this is funny? You think the president’s cat being killed, and me
trying to collect evidence is humorous. You are ridiculous sir. Absolutely ridiculous.
INVESTIGATOR Q. I was struggling to come up with any new leads. I began to ponder. Who knows
animals the best? Kids! First, seeing as I don’t have any kids of my own, I had to find a kid. I pulled up in
my 1998 blue Mazda MPV, to the local elementary school.
INVESTIGATOR Q. Hey you!
KID. Me?
INVESTIGATOR Q. Yeah you! Come here!
KID. Well, I’m not supposed to talk to strangers.
INVESTIGATOR Q. Well I’m Investigator Q. See, now I’m not a stranger anymore.
KID. Well, I don’t know if that counts.
INVESTIGATOR Q. Well it does.
KID. I’m gonna go…
INVESTIGATOR Q. WAIT! Well, just answer one question for me.
KID. Well, what do I get out of it?
INVESTIGATOR Q. I’ve got some candy!
KID. Candy? Candy? Is that it? I mean seriously, candy?
INVESTIGATOR Q. What? I thought kids like candy?
KID. Well yeah but, come on, nowadays we're expecting you to bribe us with a sack of money or a
computer or something nice. Not candy. I mean seriously? I mean you’re already a big enough loser to try
and kidnap little kids. But are you SO cheap that you’re offering us jolly ranchers and junior mints??
INVESTIGATOR Q. After spending two more weeks in jail for assaulting a minor, I had time to think.
But because I’m not very good at that, I called an old informant. Deep Throat. He agreed to meet with me,
disguised of course.
DEEP THROAT. I’ve got some information that I think will help you solve the case.
INVESTIGATOR Q. (laughing) You have a really high voice.
DEEP THROAT. It’s a serious vocal chord disorder.
INVESTIGATOR Q. RIGHT!!
DEEP THROAT. But this news can’t get out...I need it to be confidential. Nobody can know who told you
this.
INVESTIGATOR Q. That’s fine Deep Throat…I mean I don’t even know who you are!
DEEP THROAT. Good, good. Now, I spoke to the Petco Owner and he said he had a tape from the day
Mr. Whiskers was killed.
INVESTIGATOR Q. Wow! Why didn’t I think of that!
DEEP THROAT. I don’t know because you’re stupid.
INVESTIGATOR Q. St…st…stupid? (in disbelief)
DEEP THROAT. Uh…yeah….as in…not intelligent.

INVESTIGATOR Q. After…(crying) I got over the whole…stupid thing , I rushed over to the Petco Store to get the video tape. PETCO OWNER. Oh god, not you again. INVESTIGATOR Q. I can tell you’re glad to see me. Now I need to see the video tape from the night of the crime. PETCO OWNER. Oh, deep…throat told you! Here’s the tape from that night. INVESTIGATOR Q. (placing it in VHS) Um...this looks like a bar mitzvah? PETCO OWNER. Oops! Wrong tape, here you go. INVESTIGATOR Q. Thank you. Did you notice anything strange on the tape? PETCO OWNER. Well, I realized that Mr. Whiskers and Mrs. President weren’t alone that night. Mr. President was with them. MR. PRESIDENT. (nervously) What? No, no, I wasn’t! INVESTIGATOR Q. Yep. I even brought the tape here with me……..(pulls tape out of bag, places in VCR…)…You can be seen right here (pointing at the screen) with your wife, and Mr. Whiskers. You and your wife appear to be getting into an argument. You storm off into the car. Now we don’t see what happens in between, but we can assume you went into the car and placed a mask over your face. Then you came back into the store, shot Mr. Whiskers, and ran away. MR. PRESIDENT. But why would I kill Mr. Whiskers? My best friend?

INVESTIGATOR Q. See, he used to be your best friend. But you became jealous of how much time Mrs.
President spent with Mr. Whiskers, and so you killed him.
MR. PRESIDENT. Well...now that you’ve caught me...I’m going to have to kill you.
INVESTIGATOR Q. with a…
MR. PRESIDENT. What?
INVESTIGATOR Q. Well usually when you kill someone…you kill them with something…..What, you
haven’t thought (starts opening window) about how your going to kill me?
MR. PRESIDENT. Well look I wasn’t expecting to kill anyone..
INVESTIGATOR Q. (slowly getting out window) Oh great so I can now say. I was killed my by the
president, in the white house, with a NOTHING. Great work…
MR. PRESIDENT. Well look I’ll shoot y-
INVESTIGATOR Q. (jumps out window) AHHHHHHHHHH!

NARRATOR. The Investigator rushed to the police office, and told them the whole story. The President was arrested, eventually impeached, and his political career was ruined. But most importantly the case of Mr. Whiskers was solved, and Investigator Q was very, very happy. Very happy indeed.
```
