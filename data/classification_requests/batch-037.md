# Classification request: batch 37 of 63 (40 records, IC-1441 to IC-1480)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-037-reply.json`.

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

## IC-1441: Soccer Moms (and a Dad)

- Title: Soccer Moms (and a Dad)
- Author (byline): Clint Wooderson
- Work: Soccer Moms (and a Dad)
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: NICOLE, MATT, ABBY, BRITTANY, CHELSEA, TIMMY, REFEREE
- Teaser before the introduction: No
- Spoken words (computed): 1708
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
Synopsis: Matt (the dad) gets talked into coaching his son’s soccer team. While neither the dad nor child are excited about the season, the moms provide enthusiasm, but not always in a productive manner! Join our soccer coach in discovering why little league soccer isn’t all fun and games! A 10-Minute Comedy CAST OF CHARACTERS MATT (m) …...…. A dad that gets volunteered to coach his son’s soccer team. NICOLE (f)........ Matt’s wife tells him to coach. TIMMY (m) ….... Matt and Nicole’s son that only speaks to complain about playing soccer. ABBY (f)……...… A soccer mom that speaks on behalf of her daughter, Sydney. BRITTANY (f)... Another soccer mom that speaks for her son, Chandler. CHELSEA (f) … Another soccer mom that is especially prissy and speaks for her son, William. REFEREE (m)...... Officiates the game.

Scene 1

NICOLE: Guess what?! I got a call from the youth league today and Timmy is signed up to play soccer this spring! Isn’t that exciting!

MATT: Yeah, it will be fun to watch the kids run around the field in a cluster not knowing what the heck they are doing. I sure feel bad for the dad that gets stuck coaching that 5-year-old and under team though.

NICOLE: Yeah...about that. One thing that the league mentioned was that they are short on volunteers and wanted to know if we would be interested in coaching.

MATT: Oh...no. I’m swamped at work and let’s be honest, I’m not very good with little kids. Feel free to volunteer if you want though.

NICOLE: I told them you would coach Timmy’s team.

MATT: You did what?!

NICOLE: You played sports when you were in school.

MATT: I played basketball and ran track! I’ve never played soccer a day in my life!

NICOLE: Honey, they are 3 to 5-year-olds. They know nothing about soccer. I’m sure you’ll be great!

MATT: You played soccer in college! Wouldn’t you be a more logical choice?

NICOLE: I need to be available to organize the moms. You know that the snack rotation is a very important part of little league soccer. I will organize those details if you will take care of the coaching.

MATT: Fine. I guess you are right. I’ve got to know more than preschoolers about soccer. You just make sure to take care of the moms. Scene 2: The First Practice

MATT: Welcome everyone. I’ll be the coach this season. I don’t have a lot of soccer experience, but we’ll focus on having a good time. How about we circle up and each introduce ourselves.

ABBY: Hi! Sorry to interrupt but I’m Sydney’s mom. She is very shy so it would be better if I introduced her.

MATT: Um...ok. The point of this is for the kids to get to know each other though. It might be better if she spoke for herself.

ABBY: No. I will speak for her.

MATT: Well...will you introduce her then?

ABBY: I just said her name was Sydney. Weren’t you paying attention?

MATT: Right. Ok. Moving on. (Points to another child). What’s your name?

BRITTANY: His name is Chandler. I’m his mom.

MATT: Great. Is Chandler able to speak for himself?

BRITTANY: Yes, but I thought the moms were going to be introducing their kids.

MATT: No, I would really like it if the children would introduce themselves so that they could get to know each other better.

BRITTANY: Oh, I like that idea. How about we do some type of introductory activity so that the kids can get to know each other?

MATT: Yes, that is a great idea (sarcastically). Why didn’t I think of that?

CHELSEA: My child’s name is William. I too think that an introductory activity is a good idea. Why don’t we make some bracelets with the kids' names on them so that they will be easily identified?

ABBY: Great idea!

MATT: Yes, great idea, but we are here to play soccer, not do arts and crafts. Let’s scrap the name idea and line up in two lines. Girls on one side and boys on the other side.

BRITTANY: That sounds sexist. My daughter is just as capable as any boy.

MATT: I’m just looking for an easy way to separate the children into two lines. I know that the girls will be just as good as the boys. Ok...kids. I want you to run up to the ball, one at a time, and kick it into the goal. Any questions?

TIMMY: Can I go to the bathroom?

MATT: You went right before we left the house. Try to hold it.

TIMMY: I don’t want to play soccer! I want to go home! (starts to cry)

MATT: The whole reason I’m out here is because it was your idea to play soccer. You can quit after the season is over, but you will endure this with me (said with a snarl in his voice).

ABBY: I don’t appreciate the way you spoke to that little boy.

MATT: It’s my own “little boy” so leave me alone. I’ll speak nicer to your daughter, but I’ll probably have to go through you as her interpreter anyway!

ABBY: Well, I never! I don’t think you are a very good influence on my daughter!

MATT: Sorry (ignoring her / rolling his eyes). Ok, kids let’s practice actually kicking the ball! Scene 3: The First Game

REFEREE: Welcome to the first game of the season. Remember, we are here to have fun. Kids, do your best and play nice. On the whistle, we’ll begin.

MATT: (on the sidelines coaching the kids) Alright guys, let’s have fun.

(The referee blows the whistle) Spread out! Pass the ball! Don’t swarm the ball! You can’t all kick it at once! Spread out! It doesn’t help if you are all in one big group! Spread out!!!

(Moms are in the stands)

ABBY: Why is he being so hard on them? They’re just children!

NICOLE: On behalf of my husband, I want to apologize. He doesn’t have any experience coaching.

BRITTANY: Why did he volunteer to coach? It seems as though it would have been better to get someone that had experience with soccer...and children.

NICOLE: That’s Matt. He’s always signing up for things that are beyond his ability.

CHELSEA: Maybe next year we can get someone that knows what they are doing.

NICOLE: To be fair, it was good of him to volunteer. The community league said that they were short on volunteers.

ABBY: Well, I guess.

BRITTANY: Yeah.

CHELSEA: That’s true.

NICOLE: Now ladies, we need to create a snack rotation. I brought snacks for after the game today.

BRITTANY: Thank you! What did you bring? You know, Chandler has a peanut allergy, so I hope the snack doesn’t have peanuts.

NICOLE: That’s okay, I brought some potato chips and Gatorade.

CHELSEA: Are the potato chips baked? We are trying to watch the types of oil that William eats.

NICOLE: Umm...I don’t think they are baked, sorry. I’d be happy to run to the store quickly and pick something else up though.

CHELSEA: Don’t be silly. We don’t want to be any trouble. I’ll just be sure to be considerate of others when it is my turn to bring snacks.

NICOLE: Excuse me?

ABBY: Don’t be sensitive. Chelsea just means that you probably didn’t know about her son’s condition. Right, Chels?

CHELSEA: Right.

NICOLE: (awkward smile) OK. We can talk more about the rotation after the game. Why don’t we just enjoy watching for now?

CHELSEA: Yes, we can do business after our team’s victory.

(The referee blows the whistle)

MATT: Ok, come over here. That’s the end of the first half. You guys are...trying really hard. Remember, we don’t need everyone on the ball in a cluster. If you guys would spread out you could pass it to each other and you would have a better chance to score.

TIMMY: I want to sit down!

MATT: Okay Timmy, sit down. Chandler, you’re in for Timmy to start the second half.

BRITTANY: Did you hear that? Chandler is going to start the second half! Oh, no! The battery on my phone is about to die. How am I going to record him? Excuse me, Matt?

MATT: Yes?

BRITTANY: Do you think you could film the second half for me since my phone is about to die?

MATT: No! I’m coaching here! I don’t have time to take a video!

BRITTANY: Well, aren’t you snippy! I ask a simple favor from someone that is supposed to be setting an example for our children and you exhibit a very poor attitude.

ABBY: Don’t worry. I’ll share the video I’m taking with you. I have plenty of battery life left.

BRITTANY: Thanks, but I noticed that you are using an android. I would prefer to have a video taken with a higher quality camera.

CHELSEA: Why do they even bother making androids? If a product is not quality, it should not be produced.

ABBY: (snarky) Good news, at second glance I realized that my battery is dying too. I guess I won’t be able to take the video.

(The referee blows the whistle)

REFEREE: Take your places to begin the second half.

MATT: Ok, guys. Remember, spread out and pass each other the ball. It will help you to score if you pass it to one another.

(The referee blows the whistle to start the second half)

MATT: Good! Nice job guys! Chandler, don’t sit in the grass.

BRITTANY: Oh no! There is clover in the field and he is allergic to clover!

MATT: Chandler, don’t lay down!

(Referee blows the whistle)

REFEREE: Sorry coach, but I can’t allow kids to lay down in the field due to safety concerns.

MATT: I understand. Chandler, you’ve got to get up!

BRITTANY: Oh no! Chandler is breaking out into hives! Get him out of the game! Get him out of the game!

MATT: Okay! Okay! Chandler, get up and off to the side. Timmy, you’re back in the game.

TIMMY: I don’t wanna play anymore!

MATT: Get in the game!

TIMMY: No!

MATT: Fine! Ref, my team is on the field. We will just play one player short.

REFEREE: Okay.

NICOLE: Matt! What are you doing? Let Timmy play!

MATT: Let Timmy play? He doesn’t want to play! I’m doing all of this for him and he doesn’t even want to play!

NICOLE: I can’t believe he isn’t playing! You are doing a pitiful job of coaching!

MATT: I’m doing the best I can! I didn’t want to coach in the first place!

NICOLE: Clearly you are proving yourself to be less than qualified. Next year, I’m not going to let you volunteer!!!

MATT: Let me volunteer?! That’s it! I Quit! Have fun coaching, soccer moms! Timmy, good news. I now give you permission to quit. Let’s go home!

TIMMY: Yeah!!! I need to go to the bathroom!

Playwright biography: Clint Wooderson is a high school drama and speech teacher in Missouri. Clint has coached multiple students to state and national competitions in interpretation events. He holds a doctorate in Educational Leadership and strives to provide positive educational experiences for his students.
```

---

## IC-1442: Space Cadets

- Title: Space Cadets
- Author (byline): Brandon Daley
- Work: Space Cadets
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2404
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
(A space ship flies through space dodging meteors)
Narrator: It is the year 2328. After years of improper trash disposal,
overpopulation, deforestation, rising CO2 levels, and other general abuse, Planet
Earth has become uninhabitable. We now join Command Leader Sarah
Bendlestien and her trusty Co-Pilot Becky on their search for a new home,
currently cascading the meteors, black holes and other intergalactic terrors of
Sector 9A14 on their journey to happiness.
Sarah: Ugh…Sector 9A14 is soooo boring.
Becky: Maybe we should get high.
Sarah: Becky! You are the worst co-pilot in the world. Don’t get high until we find
a place to refuel the ship’s gooby perker supply at least. I swear, you would have
no redeemable qualities if you weren’t pretty.
Becky: Awwww - Sarah! You think I’m pretty?!
(Becky takes a big bong rip).
Sarah: Oh my god - I have to do everything around here.
(The ship’s video phone rings.)
Becky: I’ll get it!
Sarah: No just let it ring. It’s probably a space telemarketer.
Becky: What if its other humans?
Sarah: There’s no way that-
(Becky pushes a button to answer it).
Becky: Command Leader Sarah Bendlestien and her trusty Space Cadet Becky
here. May I ask whose calling?
(Command Leader John H. Kelleher and his co-pilot Scott Pockets)
John: Hello! Hello - oh thank god…please - we are in desperate need of help. My
name is Command Leader John H. Kelleher and this is my co-pilot Scott Pockets.

Scott: Hey there ladies! John: We are currently running extremely low on gooby perker supply. Is there anyway we can mount our ship to yours until we get to a safe refueling location? Becky: Oh my goodness! It’s been so long since we’ve talked to other humans! Definitely we’ll extend out the gasoline dock- Sarah: Actually - boys, I hate to break it to you. Space Cadet Becky is a little high right now and has forgotten that we’re running low on gooby perkers ourselves. I don’t think we have enough to spare. Becky: Oh come on Sarah - don’t be like that! (Sarah holds the microphone so the other ship can’t hear her). Sarah: Look, Becky, we have no idea who these dudes are. Gooby perkers aside, are you going to indulge every intergalactic traveller we come across asking to mount us? Becky: Well, yes. Sarah: You have no idea about the unwanted terrors this galaxy can bring. For all we know, these two could be space burglars or serial killers or some kind of improv group or something. And besides they’re not even that cute. Becky: The co-pilot’s kind of cute. (Sarah starts to take her hand off the mic and returns her focus to piloting) Sarah: Please Becky, you can’t be serious, he’s got one of those tiny ponytails on the top of his head. If you’re rocking one of those then we all know you’ve got some serious confidence issues on your hands. John: We can hear you now. You took your hand of the mic. Sarah: Yeah I know, you needed to hear that. Scott: Oh okay sorry thanks yeah the ponytails just something new I’ve been trying out but yeah okay I understand if it doesn’t work for you… Becky: Why do you have to be so mean all the time Sarah!? We’ve been traveling for months and these are the first other humans we’ve come in contact with! Can’t you just be a little grateful for this? Sarah: Becky, you know being grateful’s not my game. Besides, what you say doesn’t even matter. I’m the captain of this ship and what I say goes- Becky: Docking station - (Becky pushes a button on the dashboard) Becky: Engaged! Sarah: God, I always forget how easy it is to engage that docking station. Becky: Okay gentlemen! I’ve just extended out the port and we’re ready for you to mount us! John: Thank you so much ladies. We appreciate you finding the kindness in your hearts to ration a few of your final gooby perkers to some random space strangers. Scott: Yeah, thank you so so much. It’s so awesome you guys could do that. You guys, are like the coolest. Sarah: Keep it in your pants Bronytail. We’re only giving you enough perkers to get you to the nearest place to fill-up. In the meantime, no funny business when you’re aboard our ship. You got that? Becky: Yeah, like please make sure to put the seat down! We get that the gravity makes it float up sometimes but still, we’re trying to keep a tight operation going around here. (Becky takes another bong rip). John: Rodger that, we’ll be aboard in just one second. This is Command Leader John H. Kelleher and my co-pilot Scott Pockets saying over and out, and god bless. Scott: Yeah bye. See you. Gosh you guys are like, so, helpful. I really, wow, yeah, its just like so cool- (Sarah cuts the feed off). Sarah: You’re a piece of work, you know that?

Becky: I’m excited!
Sarah: You better pray they don’t turn out to be an improv group.
Becky: You always assume the worst! The universe can be a dark place if that’s
how you always choose to see it.
Sarah: The universe is a dark place Becky! I’ve been piloting a long time. I’ve
seen how dark this universe can get.
Becky: Well, I’m sure there’s been a lot of light that you’re overlooking as well.
Sarah: Looks like your new friends just docked in your station.
Becky: Oh I didn’t even notice. Maybe I’ll make us up some Tang.
Sarah: Huh - that’s strange. They aren’t accessing the gooby perker port.
Becky: I wonder if they’re having troubles with it.
Sarah: Or maybe…they aren’t here for our gooby perkers-
(Suddenly, the doors to the ship’s cockpit burst open. Command Leader John H.
Kelleher and co-pilot Scott Pockets burst in wielding laser guns).
John: Alright! Nobody say a word.
Becky: Oh my gosh! He’s got a gun!
John: What’d I just say!?
Becky: What did you just say?
John: Yeah-
Becky: You just said what’d I just say.
John: No before that!
Becky: Oh I don’t really remember.
John: You don’t remember?
Becky: Yeah my memory’s not that great.

John: I said nobody say a word. Becky: Well, we’ve both been breaking your rule then! John: No, just stop talking or I’m going to shoot you. Becky: When am I supposed to stop? Like right now? John: Yes. Becky: Okay, sorry, just clarifying, not saying anything more after this sentence that I’m finishing right now after these words I’m saying are done being said… (A moment while everyone waits to see if she’s done talking) Becky: You guys don’t do improv do you? John: SILENCE! Scott: I do a little improv actually. Sarah: I bet you do, don’t you Bronytail. (Scott points to his hair). Scott: I took it out okay! See? Do you see the ponytail anymore? Dang, I was, just trying it out. I don’t always keep it like that. You don’t have to make fun of me so much. Sarah: Folding like the wet self-conscious napkin that you are. Look, I think it’s safe to assume you aren’t here for our gooby perkers so why don’t you take what you want and get off of our ship? John: Truth is its not that easy Command Leader. I’m afraid we’re not actually human. We’re shape shifters from Sector Quad5P! Scott: That’s right, and what we’re here for is far harder to part with than a few gooby perkers. Becky: Oh no! Not the bong! John: No not the- jesus, your brains! We need your brains. Okay? Secret’s out. We’re harvesting the brains of various species so we can interpret scans of the stored information in order to more adequately shape shift into a wider variety of species, all so we can do some intergalactic thing or something, I don’t know. You wouldn’t understand, its kind of hard to understand. Long story short, we’re going to have to cut your heads open. Becky: But we get to keep the bong? Sarah: You can keep the bong Becky. They’re shapeshifters—they don’t have lungs. Becky: Ugh - that’s rough. (she rips the bong) John: Now we can do this the easy way or the hard way. (John and Scott both pull out weapons for scalping the girls) Sarah: Okay well, although I’m flattered that two men are finally interested in us for our brains and not our incredible bodies, I have to politely decline your request and ask you both to leave my ship before things get uglier then Bronytail’s subconscious. Scott: Oh come on! John: Well, sounds like we’ll be doing this the hard way then. (John and Scott put away their weapons and begin to slowly shape shift and change, their bodies eventually morphing together to form a two headed four-legged, four-armed slimy space alien). Becky: Oh my god! A space monster! John: That’s right - we’ve shapeshifted into a collective space monster - modeled after the deadly and venomous Gragoons of Sector 18Q. Unlike humans, they can withstand gunshots and blades and lasers and any other form of defense that you may have access to. Scott: That’s right, you had one opportunity to kill us and you missed it! John: And don’t let the fact that we are now one fool you. This one body still houses two independent minds. Scott: Yes - its double the intelligence all wrapped up in one of the most dangerous creatures in the universe! (A high Becky has wandered off in thought - she suddenly notices the alien again). Becky: Oh my god! A space monster! Sarah: Wait a minute - let me get this straight. If you can shape shift into any thing imaginable, then why did you guys pick such unattractive human alter egos? Scott: Hey! Quit picking on us so much! We worked really hard on those alter egos! John: Don’t listen to her anymore Scott! She’s manipulative and conniving. I’ve come across her type before - they get anything they want from you merely by playing with your emotions using precisely executed word choice, tone of voice and good looks. Scott: I didn’t know such a manipulative specimen existed in this galaxy. Sarah: You’ve obviously never had a girlfriend before then. Scott: I’ve had lots of girlfriends okay! Sarah: You’ve had a lot of girlfriends just like Becky has had a lot of good ideas. Becky: I’ll be your girlfriend! Scott: Just stop making - wait, you would? Wow that’s…haha. Jeesh. Becky: Yeah, I thought you were kind of cute before you morphed into this whole weird space alien thing that can’t be killed. (Sarah realizes Becky may actually be having a good idea even though Becky herself doesn’t realize it. She starts to play along). Sarah: Oh come on Becky - why would you pick Co-Pilot Scott “Bronytail” Pockets when you could have the man in charge? The one and only Command Leader John H. Kelleher - older, wiser, years of experience. John: Oh, haha, well - my human persona isn’t that old, you know. I like to think he does have a whole George Clooney type of vibe thing going on and I appreciate that you recognize that.

Scott: Yeah, I was going for a younger Keanu Reeves type of thing, but I totally respect going more towards Clooney. John: Thank you - and you know I don’t disrespect Keanu one bit. 47 Ronin is a personal favorite of mine. Sarah: Wow you guys have quite the knowledge of human celebrities for being space-traveling shape shifters from an alternate galaxy. Becky: Yeah! That is kind of weird… Sarah: Say - before you do this whole harvesting thing, why not take a quick detour back to your human bodies for a little bit? Eh? What do you say? Maybe we can have a little fun before you extract our brains? Becky: Yeah maybe we can kiss and stuff! (Becky starts to take a rip of her bong) Scott: Haha, oh gosh - well, I mean - it’s a dying girl’s wish John. Maybe we could do a little kissing, don’t you think John? John: Haha, oh well, I suppose I couldn’t reject a dying girl’s last wish of a couple kisses. Plus it would be fun taking those human alter egos for a bit of a test drive, if you know what I mean…haha. Scott: Oh, well, I think I do know what you mean, haha, since we objectively clarified what was meant right before you asked me if you know what I mean. John: Yes, oh yes sorry, please excuse my silly need for the unnecessary chit chat ladies. It’s just that, I get a little nervous as I’ve never kissed a human before. Scott: Well, we had our human alter egos kiss that one time didn’t we-? John: OHH Scott, I think we needn’t bore these beautiful vixens with exhausting anecdotes like that one. Haha, don’t listen to him ladies. Scott: Oh, yeah don’t listen to me, we didn’t kiss each other with our human alter egos. John: Stop saying that!

Scott: What?! I said we didn’t do that! Why would I say we didn’t do that if we did do that. Hahahaha, huh ladies? Does that make any sense to you? Why would I say we didn’t kiss if we actually did kiss? John: Jesus! Just, stop talking, you are so embarrassing - okay, just a second ladies! I’m going to just separate myself from my over-excited partner here- Scott: Partner being a totally platonic and non-experimental term mind you- John: And we’ll be right back into our human forms in just a jiffy. Just…one…second- (John and Scott begin to separate themselves and shape shift back into their normal forms. Becky and Sarah look bored waiting and watching all of their mundane back and forth. After a moment of transformation, John and Scott are now back to their human personas). John: Perfect! Good as new! Haha… Scott: Yes, yes, now, Becky is it? If you wouldn’t mind just coming over here a little bit closer and we can get started - now, do you want the ponytail in or out, I wasn’t 100 percent clear on your stance on the whole thing because your command leader GAH- (Scott suddenly takes a shot to the chest. He falls to the ground). Scott: I’ve been shot! John: Hey, what the- ULGH! (Shortly after, John is shot also. He crumbles to his knees). John: Oh my god I’ve also been shot. (Sarah holds up a space pistol. Becky takes a rip out of a bong. She glances up to notice that the two have been shot). Sarah: Got ya! Becky: My boyfriend! (Sarah grabs the bong out of Becky’s hand and uses it to beat the remaining life out of John and Scott).

Becky: MY BONGGGG!!!! (After a long time of beating, Sarah drops the bong and lets her head drop. She picks up John’s hand and lets go of it to make sure he’s dead. Becky crouches down next to her weeping). Becky: My beautiful bong… Sarah: I’m so sorry Becky - it was for a good cause… Becky: Rippy Bongstockings never did anything to hurt you! Sarah: Aside from decreasing your work efficiency and critical thinking capacity by at least forty percent, you’re right, it never did anything to hurt me. But we sacrificed it for the good of the humanity Becky! And our brains. Mainly our brains. Becky: Forget our brains Sarah! What’s the point of a brain if you can’t mess it up with recreational drug abuse and what’s the point of a life if you’re only boyfriend in the entire universe is a dead shape shifter and I just don’t know how much longer I can continue onwards on these messed up space adventures! Sarah: I know Becky. Unfortunately, this life chose us. And even if you don’t have a shapeshifting boyfriend, you always got me. Becky: Yeah, I guess I so… Sarah: I love you Becky. Becky: I love you too Sarah. Narrator: And so Becky and Sarah continued their travels onwards, cascading through the unknown terrors and obstacles frequently found in Sector 9A14. All that they had in this entire universe was each other, but no matter how close they got during these travels through the empty abysses of space and time, neither could ultimately shake the feeling of being alone. So they beat on, boats against the current, borne back ceaselessly into the gooby perkers.
```

---

## IC-1443: Sports Atheist

- Title: Sports Atheist
- Author (byline): Micah Larson & Brian Sams
- Work: Sports Atheist
- Publisher: Mushroom Cloud Press
- Publication date as stated: December 11, 2023
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1708
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
by

Micah Larson and Brian Sams

Characters: Joey: Our main character. A teen boy trying to convince his parents that there is life without Sports Darren: Joey's dad. Strict believer in Sports Marge: Joey’s mom. Mid-western mom who thinks Sports are life Coach: Joey’s coach. Basically a Sports priest Summary: In Joey’s world, Sports is a religion, and Joey has had enough. When he tells his parents he doesn’t believe in Sports anymore, it hits them hard, especially his dad. Joey tries to convince them that being a Sports Atheist just makes sense for him. Coach arrives and attempts a Sports exorcism, which is unsuccessful. Joey admits to his parents that he’s thinking about participating in Speech, and when his dad discovers it’s a competition, he’s all in, so much so that Joey is left to wonder if he has just created a whole new set of problems for himself. Dad: Jeez, where is that kid? I know he’s awake. (Directed offstage) Joey! Get out here son! It’s Sunday morning and you know what that means! Put on the new outfit your mom got you and let’s get going! We don’t want to be late and have everyone stare at us! Marge, see what you can do... Mom: Yes, dear. Joey! Sweetie! JOEY! It’s very important that we set a good example for the new neighbors, they’re not from around here so we might be able to give them a little nudge in the right direction! Joey: Hey Mom, hey Dad. Mom: Oh, there he is! Joey. Joey, honey. Why aren’t you wearing the jersey I bought you? Dad: And where’s your foam finger son? Are you sick? Do you have a concussion? Joey: Mom, Dad, I’m fine, but I’m not going to Stadium with you. Dad: What do you mean? Of course you’re going! You were raised going to Stadium. Sure you could watch the game on TV, but it’s not the same as being there with the other believers, all united as one, cheering and screaming at the refs. The hot dogs, the spilled beer, the plastic seats...The pee trough, Joey. The pee trough.

Joey: I don’t know how to break this to you, and I wish there was a better way, but…Mom, Dad, I don’t believe in Sports anymore. Mom: Oh, Joey, no! Dad: I think I’m gonna throw up...Oh yeah, I’m gonna throw up. (Dry heaves a few times) I can’t. I haven’t even had any lite beers (or insert any brand here) yet so I can’t! Mom: It’ll come, Darren, it always does. Dad: My own son, a Sports atheist. What’s next? Oh, Favre, don’t tell me you’re a vegan, too? INTRO: Do you have parents? Yeah they're great, but there comes a time in every child's life when they have to decide if they’re going to believe everything that their parents believe. Joey has reached that point, but will he be able to convince his parents that there is life without sports? Sports Atheist, with music from the Fox NFL theme by Scott Shreer. Joey: No, Dad, I’m not a vegan. If anything, I would start as an ovo-lacto vegetarian and then… Dad: What in the name of Belichek (or insert any current coach) is going on here… We did everything right! You memorized the stats, we got you the trading cards, we made the pilgrimages to the Lambeaus, the Wrigleys, Madison Square Garden… Mom: Our Vikings (or insert NFL team here), which art in Minneapolis (or insert city of team here), hallowed be their name. Thy Bowl shall come, it will be won. Indoors as it is outdoors. Give us this Sunday our weekly win. Give us our completed passes, but do not let others pass against us… Dad: Marge, that's not going to work! Say a couple of Hail Maddens! Mom: Oh… Hail Madden! Full of bratwurst… Blessed are you among all coaches and blessed are your Fruit of the Looms. Dad: Joey, did some kids at school talk you into this? Was it those theater kids? I told you to stay away from those heathens! Joey: No Dad, I just woke up one morning and thought, does this make any sense? Ever since I was three years old, I’ve been in at least three Sports a year. I’ve been getting up before dawn every day to go to practice. And we're on the road or at Stadium every weekend for tournaments… Dad: Joey. Are you forgetting the dream? Those who follow the discipline of Sports have a great reward ahead of them! To the vision board! (He runs to the vision board, obviously a prominent item in the house) The scholarships, the draft, the championships, the rings...and someday...if you are worthy...the Hall of Fame! Joey: That’s just it, Dad. I’m not good enough for that. Mom: Oh, Joey, don’t say that! You Sportsed so hard! Joey: Mom, I know you tried. You wore out three SUVs just taking me to practice… Mom: Well, honestly, honey, two of those were totaled ramming some filthy soccer moms off the road... Dad: ...and for what? So you could throw this in our face? No, come on... Next week your team is going to win the city championship, and, well, we were keeping this a secret, but your mother and I have arranged for you to get your first Gatorade baptism! Mom: The blue kind! Your favorite! Grandma and Grandpa are flying in… Dad: And this’ll break their hearts. Say you’ll try. Joey: What are the odds, Dad? Only 2% of athletes ever make a dime from their Sport, then only 1 out of a thousand of those players make it really big… Dad: You think I don’t know that? Salvation was just a touchdown away, but I failed…for all have fumbled and fallen short of the glory of the first down! Now, all I can do is to take those hopes and dreams and fears and failure and just sorta cram it all into you…(sob)…Marge, bring me a beer, I'm ready for throwing up now. Mom: Darren, maybe we should talk to Coach. I already called. He’s on his way. Joey: Aw, man, don't drag Coach into this… Dad: No, your mother’s right. Coach will know what to do. *NFL Fox Theme DOORBELL* Marge: Oh, I love that doorbell! Dad: Forgive me, Coach, it’s been two weeks since my last coaching session… (Makes sign of the cross, muttering "Helmet, Cup, Shoulder Pads.”) Coach: (Coach enters, carrying a smallish cooler, which he sets down as he speaks.) Darren, if this is about Joey’s playing time, I swear….

Mom: Coach, Joey doesn’t believe in Sports anymore!
Coach: Are you sure he doesn’t have a concussion? About half the team have concussions right
now…
Dad: He seems fine.
Coach: Well, then, let me just try this. Joey… (he grabs Joey and shakes him violently) The
Power of Sports compels you! The Power of Sports compels you!
Joey: What are you doing? Stop it! I’m not concussed and I’m not possessed, I just realized
Sports are pointless.
Dad: Oh boy, here it comes… (Dry heaves)
Coach: Whoa, Darren, are you okay? Concussion, am I right?
Dad: No. Too much talkin’, not enough drinkin and pukin’.
Coach: Huh. Okay Joey, I thought it might be something like this…(He goes to his cooler) Joey,
you can drink this blue Gatorade and go back to your old life, or you can drink this red Gatorade
and forget everything you ever knew about Sports. Or you can drink this grape juice and
become a Baptist.
Joey: No thanks. What’s in the Gatorade?
Coach: Nothing Joey, nothing but pure American electrolytes! Because even if you don't
believe in Sports, you do still believe in hydration, don’t you boy?
Joey: Oh, yes, sir!
Coach: And now…

(Coach starts a concussion test by holding out his finger and moving it in a triangle; it is reminiscent of a Catholic blessing.) Joey: Are you blessing me or giving me the concussion eye test? Coach: Oh boy. (Coach focuses on his own finger in a confused manner) I think I might have a concussion. But let's just keep that between the, uh…(counts people in the room while moving his lips) seven of us. (There are four…) Joey: Sure, Coach.

Coach: Welp! You can’t win 'em all, folks. Looks like you got yourself a Sports atheist here. (Retrieves his cooler) Coach Out!...Oh, and may the Sports be with you. (Slams the door on the way out.) Mom: And also with you! Dad: So, that’s it? You’re just gonna sit around after school and on the weekends and do nothing. Joey: (Goes to get his backpack and removes a flyer) Actually, I was thinking about converting to Speech. Mom: Converting? Spetch? Do you have to shave your head and wear a paper dress? Joey: No. No. Nothing like that… It's public speaking, but it also has elements of humor and drama. Dad: Did you get him vaccinated, Marge? I heard vaccinations can make your kid artistic. Mom: Oh, honey, no… Dad: Well then, he must have gotten it from your side of the family, because no one in my family is ever dramatic! Mom: Sure Honey…. Oh, did you hear that the (insert NFL team here) (released or traded)

(insert NFL player)?
Dad: (Falling to his knees - a la Charlton Heston in Planet of the Apes) No! Darn you! You
maniacs! Darn you all to heck!
Joey: Well, um, we have practice after school, could you…
Dad: Practice? You mean there’s a coach I can call or text day and night with random questions
and suggestions?
Joey: Ummm, yeah…
Dad: Oooh! And how do we, I mean, how do YOU win?
Joey: Okay, there are judges…
Dad: Officials! When we disagree with them, can we berate and belittle them?
Joey: Yeah, but in Speech, they do it behind their backs.

Dad: Strange… but it’s getting better. Mom: Honey, do you need new shoes? Joey: Yeah. Slippery ones.

(Joey and Dad quickly execute a series of character pops demonstrating foot movements that
would benefit from slippery shoes.)
Dad: Slippery?
Joey: Slippery.
Dad: Slippery?
Joey: Slippery.
Dad: Seriously?
Joey: Seriously.
Dad: Why slippery?
Joey: No idea.
Dad: Alrighty then… So, when do you start?
Joey: I guess whenever I want…
Dad: Right now! You are gonna be the best…spetcher that there ever was! Top of the teeth, tip
of the tongue!
Joey: What?
Dad: Say it! Louder, faster, crisper!
Joey: Top of the teeth, tip of the tongue!
Dad: That's the ticket! Marge, you go get him some shoes! Extra slippery! I’m gonna get him a
suit…with a pocket square! Let’s go!
Joey: Oh Favre, what have I done?

About the authors: Micah Larson competed at the high school level for 6 years. For 5 of those years he was in Creative Expression. He wrote The Dire Disney Dilemma, Segregation of Students, The Fast Food Felony, The Worst Day Ever, and this script, Sports Atheist, with the help of Brian Sams, of course. Brian Sams competed in high school Speech in the 80's, and has been a Speech coach since 1991. He is a business owner, part time actor, and a writer. Awards: A Minnesota State Champion script
```

---

## IC-1444: Swipe Up!

- Title: Swipe Up!
- Author (byline): Clyde Hendrickson
- Work: Swipe Up!
- Publisher: Mushroom Cloud Press
- Publication date as stated: September 1, 2022
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: VAL, NIK
- Teaser before the introduction: No
- Spoken words (computed): 1321
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
AUTHOR’S NOTES When VAL “swipes up” it causes a physical reaction in NIK that should be repeated whenever the swipe occurs. The script sometimes calls for VAL to use “TikTok voice,” which refers to the robotic female voice that reads on-screen captions within the app. At the point noted it in the script, it is the author’s intent that the performers insert a very recent trending TikTok dance, with two lines of dialogue adjusted by the performers to fit if necessary. It may work without modification, depending on the dance; this section can also be omitted if preferred. VAL and NIK can be played by actors of any gender.

SWIPE UP! [Two actors on a bare stage. The only props are a smartphone and virtual reality glasses, which should look like regular glasses with gizmos on the sides so you can still see the actor’s eyes.)

VAL: Nik! Nik Nik Nik.

NIK: Sup Val.

VAL: Try these new virtual reality glasses!

NIK: What do they do?

VAL: They put you inside the phone.

NIK: Inside?

VAL: Yeah, now you see what I see.

NIK: Wait, whose phone am I going inside?

VAL: Let’s try TikTok.

NIK: Why is my head tingling?

VAL: It’s working! Let’s go!

NIK: Wait… wait… I’m not ready.

[SWIPE UP 1]

VAL: First one… 30 day dance challenge. Day 1.

NIK: [Dancing badly] I’m bad at dancing, so this feels ok…

VAL: And now day 30!

NIK: [Dancing well, but pulled on a string] What is happening to me!!!

VAL: Whoa.

NIK: (still dancing) Ok these might need to be adjusted.

VAL: We gotta try another one.

NIK: What’s wrong with you Val?

VAL: I love new apps.

NIK: You’re addicted to your phone

VAL: And it’s great, Nik. [SWIPE UP 2]

VAL: [TikTok voice] This one weird trick makes you look 20% cuter

NIK: I could go for that…

VAL: (TikTok voice) All you need to do is vape hot sauce into your eyeballs

NIK: What?? (vaping hot sauce into their eyeballs, with increasing resistance) There’s… the vape pen… and it smells like tobacco… Oh no… (eyeball one is vaped) Ahhhhhhh!!!!!

VAL: (TikTok voice) It hurts less with the other eye

NIK: (Vaping other eye, more screaming) No it doesn’t! Who tried this the first time?

VAL: Does it actually hurt?

NIK: Swipe you d--- [SWIPE UP 3]

VAL: Ok, smash or pass.

NIK: Oh. I’m gucci.

VAL: Ezra Miller

NIK: Wow, I--

VAL: SMASH OR PASS

NIK: Smash! Oh no.

VAL: Johnny Depp.

NIK: I don’t like this theme

VAL: (menacing) Smash. Or. Pass.

NIK: Fine. Smash. Please give me an easy one—

VAL: -Your mom!

NIK: Pass. I am so sorry mom, I—

VAL: Your dad!

NIK: Smash!

VAL: What the—

NIK: He’s a cool dude.

VAL: Jennifer Lopez—

NIK: Finally, an easy one, I will—

VAL: With the body of Ben Affleck—

NIK: PASS. Dammit Val.

VAL: Millie Bobbie Brown.

NIK: Is this legal?

VAL: You’re so bad at this. [SWIPE UP 4]

VAL: (TikTok voice) This condiment is so good, you’ll want your food to run you over with its car.

NIK: Like that time with the wiener mobile…

VAL: (TikTok voice) Here’s how we make happy in a jar for $49.99.

NIK: (Strange, hyped voice) For all you Chef Lil S@v@g3 with two ampersands and a three instead of the vowels fans out there, this is What! You’ve! Been! Waitiiiiing for! My signature special RAT SAUCE is available now. It’ll make you screeeeeeammm! When you put it on pizza. (squeals). Tendies (squeals). Ice cream (squeals). Protein bars! (squeals like mad). How’d ya like to have the best tasting meal of your life? Rat sauce is so intense you won’t know if it’s good. None of my family can describe it! My friends didn’t text me back for days after trying it. That’s how good it is! And yeah some had nasty poops but this is the best poop of your life! It’s so intense! (squeals) RAT SAUCE will overrun you with flavor. Squirt it in your face today and you will be slurping down your dreams tomorrow. That’s the Chef Lil S@v@g3 with two ampersands and a three instead of the vowels. We also have it in vape form!

VAL: Ugh.

NIK: (back to regular voice) I need… to use the bathroom… [SWIPE UP 5]

VAL: (TikTok voice) Tell us about a day in your weird life

NIK: (Heavy British accent of some kind): Right mate, this is what it’s like being a bloke who thinks everything smells like poop. I mean everything, from me mum, she’s like a big turd, to me mates, nothing but arsefire, to my favorite meal, just a big bowl of butt gruel. Don’t even really have a favorite meal to be honest, I try to just have slurpees. If you were in this room with me, I’d say did someone let a big sewer snake out of the rear exit of the brownton zoo? Even my hand (smells hand) ah no, that’s rank. Gotta smell something else… which never works… my keys (smells keys from pocket) Bucket of brown sauce! That’s worse. Maybe the wall… (starts retching) Oh it’s really turtle time now… beam me up someone dropped a Shatner… My cat, let me smell you! (reacts) Oh god it’s like a madman took a whole caravan of chocolate hostages… working the turd saw morning noon and night (really retching, keeps going too long, then suddenly normal) Well that’s a day in the life of Ol’ Poopey Pip! Leave a comment for what you want me to smell next.

VAL: Whoa

NIK: Why didn’t you swipe.

VAL: I couldn’t stop watching. Let’s get out of here. [SWIPE UP 6]

NIK: I need relief.

VAL: Dance to Beyonce like you’re a robot.

NIK: I can’t!

VAL: Don’t make me swipe again.

NIK: [Robot Beyonce music as he dances – during this sequence N sings a beyonce song of actor’s choice.]

VAL: Now like you had seven energy drinks!

NIK: [Manic Beyonce music]

VAL: Dance to Beyonce like you’re a potato

NIK: [Potato Beyonce music]

VAL: Dance to Beyonce like your best friend

NIK: [Very bad dancing]

VAL: Hey!

NIK: [Even worse dancing]

VAL: Dance naked to Beyonce

NIK: [Get a devilish grin, starts to move to disrobe….]

VAL: No Nik. No no no no— [SWIPE UP 7 – A trending dance. This portion is optional, but the intention is to add a very recent trending dance from the app. A line can be added to name the dance if necessary, or to describe its features.]

VAL: Oh this is a good one. Brand new.

NIK: I don’t know it.

VAL: You’re good at it.

NIK: I am good at it!

VAL: Maybe you’re getting used to this?

NIK: Being possessed by your phone like a demon? (dance is peaking) Not a chance.

VAL: We need to find safe haven in parent twitter [SWIPE UP 8]

NIK: Ok folks what should I name my kid? (points as though names are appearing on screen) Zaylor? Jennifelx? Bruleén? Kaleb! Exclamation point part of the name! Brydock? Tulum? Crabbe Rangoon? That’s hubby’s favorite food. Cutie Pie? Striker McBatterson? Axe Murder Hellstein? Jort? Big Philip? Small Philip? Just Regular Philip and “Just Regular” is part of the legal name? Leave your idea in the comments AND DO NOT SAY GREG. MY EX WAS NAMED GREG.

VAL: I don’t feel safe. [SWIPE UP 9]

VAL: It’s time for your glow up.

NIK: Do what you will.

VAL: Hair glow up.

(NIK enhances hair)

VAL: Smile glow up.

(NIK enhances smile)

VAL: Face glow up!

(NIK enhances face. They are starting to crack.)

VAL: Botox face glow up!

(NIK’s face grows perkier)

VAL: Another injection!

(NIK’s face grows perky to a demented degree)

VAL: You’ve gone to the gym every day for six months

(NIK screams like on steroids)

VAL: Full. Glow up.

(NIK tries)

VAL: (like Kylo Ren meme) MORE!

(NIK tries)

VAL: MOORRREEE!

(NIK breaks)

NIK: I can’t do it! This is too much. You are on TikTok too much! What can you possibly be getting out of this? You’re wasting your life. Can we not hang out as normal friends??

VAL: I… (almost admits NIK is right, but regains composure.) Just one more swipe.

NIK: You’re a monster.

VAL: I’m an influencer. [SWIPE UP 10]

NIK: Well?

VAL: Oh no… we’re in.. sad TikTok!

NIK: Huh?

VAL: (TikTok voice) Tell us your worst break up story.

NIK: Like, my own?

VAL: (TikTok voice) Tell us your worst break up story.

NIK: I don’t want tell all these people about that ,Val.

VAL: What people?

NIK: All the people out there, watching.

VAL: (TikTok voice) Tell us your—

NIK: Fine. There was… I had a crush. Named G. I finally asked G out. Said yes. I was… over the moon. Last day of school. Whole summer. And G cheated on me.

VAL: Wait… you mean G?

NIK: Last summer. Three times.

VAL: But you two… you’re still with…

NIK: Not anymore.

VAL: Why didn’t you?

NIK: I was going to tell you today. Guess I did. And a lot of other people [PHONE AWAY]

VAL: I’m sorry. I’m sorry I got carried away.

NIK: You did, Val.

VAL: Sorry, Nik.

NIK: Don’t worry about it.

VAL: What would make you feel better?

NIK: There’s one thing.

VAL: Anything.

NIK: [puts headset back on.] Looking at a bunch of dumb stuff on TikTok.
```

---

## IC-1445: Take Care of It

- Title: Take Care of It
- Author (byline): Kevin J. Burgun
- Work: Take Care of It
- Publisher: Mushroom Cloud Press
- Publication date as stated: September 1, 2021
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: AUTHOR’S NOTE, SUMMARY, JERRY, MERCENARY 3
- Teaser before the introduction: No
- Spoken words (computed): 2095
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
CHARACTERS

Alex

Jerry

Scammer 1

Scammer 2

Mercenary 1

Mercenary 2

Mercenary 3

Narrator

AUTHOR’S NOTE: The characters are written so as to be played by any gender.

AUTHOR’S NOTE: Mercenary 2 and 3 can be combined if desired.

SUMMARY: What happens when your wonderful night of sleep is shattered by a text message sent by two dimwitted scammers? Well, if you are a trillionaire, you hire a band of ex-soldier mercenaries to “take care of it”. Whatever “take care of it” means.

Take Care of It 3

(Twilight Zone - esque beginning. Alex is sleeping peacefully during the narrator’s introduction.)

NARRATOR It was a night just like any other night. A cool 71 degrees compared to earlier in the day which saw a high of 93.5. Alex had gone to bed early. 8:47 pm to be precise. And at 2:43 am. Alex got a text. (ding) (Alex jerks awake.)

ALEX This must be an emergency!

NARRATOR A natural thought. For a text at 2:43 am must be an emergency.

ALEX Did the stock market plummet? Did my dad finally decide to talk to me? Does someone want to know if “I’m up”?

NARRATOR But it was none of these things.

ALEX (Reading Text) You have been preapproved for a loan, click here to accept.

NARRATOR (The narrator is responding, or trying to respond to, Alex’s reaction.) The anger started low. Lower. Maybe a little lower. There you go. And then slowly boiled up. Slowly. Okay, fine, quickly boiled up.

ALEX and NARRATOR SPAM TEXT.

NARRATOR There was only one thing to do.

ALEX I need to take care of it.

(Transition music)

SCAMMER 1 That was awesome. 2:43 in the morning loan approval text.

Take Care of It 4

SCAMMER 2 The perfect time to send a text.

SCAMMER 1 No doubt.

SCAMMER 2 They are going to click it and totally give us their credit card information.

SCAMMER 1 And then we can buy stuff.

SCAMMER 2 We are finally going to get HBO Max without commercials.

SCAMMERS Excellent, Excellent

(They high five)

(Transition)

ALEX Listen Jerry, I need you to put together a team to take care of this. Can you track these scammers down?

JERRY Alex, you are a trillionaire, yes, yes I can do that.

ALEX Excellent.

(Transition)

SCAMMERS Excellent, excellent.

SCAMMER 1 What do you think would happen if someone had access to like, a trillion dollars, and used all of those resources to hunt us down because of a spam text we sent?

SCAMMER 2 Whoah. Great question. I never thought about that. Whoah. I mean, how much?

Take Care of It 5

SCAMMER 1 A trillion dollars.

SCAMMER 2 Nothing, I mean nothing we could do, a trillion dollars? No way.

SCAMMER 1 So we are screwed?

SCAMMER 2 Don’t worry. This isn’t a movie. No one is going to use their vast wealth to track down two lowly scammers.

SCAMMER 1 Oh, good point, you are right.

SCAMMER 2 All they need to do is respond with “Stop” and we have to stop. It’s like, the rules.

SCAMMER 1 What if they had access to an elite paramilitary group full of people led by a quiet loner who suffered a personal tragedy which somehow made them even more powerful by accessing the power of staring out the window while it rained?

SCAMMER 2 We are totally safe, there is no way that the exact set of circumstances needed to imperil our safety would ever actually happen.

SCAMMER 1 Because this isn’t a movie.

SCAMMER 2 Exactly. And there is no rain in the forecast.

SCAMMERS Excellent, Excellent.

(TRANSITION)

ALEX
I want this to happen now, Jerry. Remember I have
(Dramatic Pause, mug to audience)
1.68 trillion dollars.

Take Care of It 6

JERRY (Makes beeping noises on handheld device). Found them.

ALEX That was surprisingly quick.

JERRY If we are living in a world in which you have 1.68 trillion dollars, then it is that quick.

ALEX My apologies. I didn’t realize that my having 1.68 trillion dollars would impact reality.

JERRY Yes, I would say that having a gross amount of money creates a different reality for you than most.

ALEX So wait, you are saying that when one person has a lot of money, it impacts how they see and experience the world?

(long pause. As in several seconds. Make it uncomfortable.)

JERRY: Yes.

(Transition)

SCAMMER 1 What are you doing?

SCAMMER 2 Checking out what movies are on HBO Max.

SCAMMER 1 I’m finally going to watch Game of Thrones.

(Transition)

JERRY You have your orders, Captain.

MERCENARY 1 Um, I’m not a captain.

Take Care of It 7

JERRY You have your orders rogue mercenary ex-soldier who suffered a personal tragedy and were convinced to take on a mission even though you retired that only you can lead, despite the fact that you haven’t kept up with training or physical fitness the past six months and have made questionable life choices that would cause one to question your ability to make sound decisions.

MERCENARY 1 You didn’t mention the gambling or drinking.

JERRY I was just lumping that under “questionable life choices”.

MERCENARY 1 Fair enough. What are we getting paid again?

JERRY 250 grand each.

MERCENARY 1 That seems excessive.

JERRY Agreed. But this is the world of the trillionaire.

ALEX Aha! My crackpot team of mercenaries!

MERCENARY 2 Who you calling a crackpot?

MERCENARY 1 Perhaps a crack team of mercenaries?

ALEX Crack?! They are drug addicts, Jerry?

JERRY No!

MERCENARY 1 We just drink. And gamble. And make other questionable life choices.

MERCENARY 3 Like invest in dogecoin.

Take Care of It 8

ALEX There are only three of you?.

MERCENARY 1 There are six total, but we didn’t think you would have time to meet us all, and we thought it might be confusing keeping us all straight, so just the three of us here.

ALEX So, you are crackpots.

MERCENARY 1 A crack team. Crack as in “excellent or first rate” is slang from the 1790’s. A crack team of mercenaries.

MERCENARY 2 Crackpot is derived from “pot” being slang for “head” and “crack” meaning there is a split in it, or it is not whole.

MERCENARY 3 And that dates back to the 1630’s.

JERRY Is etymology part of your training?

MERCENARY 2 Watch who you are calling an etymologist.

MERCENARY 1 It’s important to understand where worlds come from.

MERCENARY 3: And how they are used.

JERRY Are you insinuating that words have power…

ALEX And the history of words hold clues to connotative meaning apart from the denotation or current use in the vernacular?

MERCENARY 1 And shared and understood meaning of words and phrases is important for clear communication.

Take Care of It 9

ALEX Could you be a crack team of mercenary crackpots?

(Long Pause as the mercenaries think. Look at each other. Triple take. Think. Weigh it.)

MERCENARY 1 That works.

JERRY You have your coordinates.

ALEX And you will be taking care of it.

MERCENARY 1 Take care of it?

JERRY and ALEX Take care of it.

MERCENARY 2 So, by take care of it, you mean….

ALEX Exactly.

MERCENARY 3 So?

ALEX Exactly.

MERCENARY 1 Take care of it?

ALEX Take care of it.

(Transition)

SCAMMERS Excellent, Excellent.

Take Care of It 10

SCAMMER 1 We should send another text, because we haven’t gotten any bites yet.

(ALARM SOUNDS)

SCAMMER 2 What is that?

SCAMMER 1 Someone has broken our perimeter!

SCAMMER 2 I told you setting up an elaborate surveillance system to warn us of intruders was a good idea!

SCAMMER 1 This is not the time for “I told you so!”

SCAMMER 2 What do we do?

MERCENARY 1 (Static noise of walkie talkie) Pincer move alpha bravo echo charlie.

MERCENARY 2 (Static noise of walkie talkie) Charlie Foxtrot egress ingress.

MERCENARY 3 (Static noise of walkie talkie) Alpha. Romero.

MERCENARY 2 (Static noise of walkie talkie) Toyota. Corolla.

MERCENARY 1 In position.

MERCENARY 3 What are the ROE’s?

Take Care of It 11

MERCENARY 1 ROE? Of course you are referring to Rules of Engagement, for anyone on the team who is listening who doesn’t know what ROE is and would need to know what it is in order to understand this bit.

MERCENARY 2 We all know what ROE means. We are all former soldiers who have suffered personal tragedies, retired, but then took one last mission that only we could succeed in doing.

MERCENARY 1 Just in case someone didn’t know what it meant. Or forgot. That it is the expectations of how we could conduct ourselves and the amount of force we would use in the field. (Pause) In case someone forgot. (Pause) What it meant.

MERCENARY 2 Cool.

MERCENARY 1 The ROE’s are pretty cool. We are being paid a gross amount of money to take care of the problem.

MERCENARY 3 What does “take care of it” mean?

MERCENARY 1 You know. Take care of it.

MERCENARY 2 But like….

MERCENARY 3 Take care of it?

MERCENARY 1 Exactly.

MERCENARY 2 But exactly what.

MERCENARY 1 No time! ATTACK!!!

(Mercenaries scream, transition to the SCAMMERs screaming.)

Take Care of It 12

SCAMMER 1 and 2 I don’t want to die!

MERCENARY 2 Prepare to be taken care of!

MERCENARY 3 Whatever that is!

SCAMMER 1 I’m too young to die!

SCAMMER 2 I’ll never get HBO Max!

SCAMMER 1 Why? Why are you doing this?

MERCENARY 1 Our employer was woken up at 2:43 in the morning by a spam text message.

SCAMMER 1 That wasn’t us!

SCAMMER 2
No, that was us.
(Scammer 1 gives a look.)
That totally wasn’t us.

MERCENARY 1 Our employer has 1.68 trillion dollars. We know it was you.

MERCENARY 2 And you are toast!

SCAMMER 1 What are you going to do to us?

SCAMMER 2 Are you going to make us cancel our ad-free Hulu subscription and force us to watch ads whenever we watch Hulu????

MERCENARY 1 That seems…

Take Care of It 13

SCAMMER 2 Take my eyes instead.

SCAMMER 1 Wait, if you are doing an eye for an eye, wouldn’t you just wake us up when we were sleeping? Thus robbing us of a good night’s sleep?

SCAMMER 2 Stop giving them ideas!

MERCENARY 1 We are to take care of it.

MERCENARY 2 Whatever that means!

MERCENARY 3 Are we killing them?

SCAMMER 1 KILLING?!

SCAMMER 2 Am I choosing between that and Hulu with ads?

SCAMMER 1 You can’t ever get the sleep back. So, nothing you do will ever get the sleep lost back. Erefore, you can never have revenge. Erefore, you can never fulfill your mission. Erefore….

SCAMMER 2 You need to go back to your employer and say you were given a Sisyphean task.

MERCENARY 2 That’s the dude who rolled the boulder up the hill in hell and it kept rolling back down, right?

SCAMMER 2 What?

SCAMMER 1 Look. What do you want?

MERCENARY 1 To make sure our employer is never bothered by your spam messages again.

Take Care of It 14

SCAMMER 1 What’s the number?

MERCENARY 1 555-555-555 (pause) 3

SCAMMER 1 (types in) Got it. Off the list.

MERCENARY 2 That’s it?

SCAMMER 2 You could have also replied to the original message with STOP. Then we would take it off as well.

MERCENARY That works?

SCAMMER 1 For us at least. Yeah.

MERCENARY 2 Let’s mess them up to leave a message for the other spammers.

SCAMMERS 1 and 2 Whoah whoah whoah whoah whoah whoah whoah whoah (pause) whoah

SCAMMER 2 That is an extreme reaction.

MERCENARY 3 Is it?

MERCENARY 1 They have a point. Our employer is off the list.

SCAMMER 1 Yup.

MERCENARY 1 Let’s get out of here. It’s been taken care of.

Take Care of It 15

MERCENARY 2 Whatever that means.

(TRANSITION)

MERCENARY 1 You will never get a text message from them again.

ALEX You took care of it?

MERCENARY 1 We did.

ALEX Excellent. Now I can finally sleep. Knowing it’s been taken care of. That is all I want. A good night’s sleep.

(Alex falls asleep. Narrator enters to bookend the beginning.)

NARRATOR And so Alex slept the sleep of one who was content in the knowledge that it had been taken care of. But reality can be harsh. Or, in this case, real dumb.

(Transition)

SCAMMER 1 That was a close call. This was a good idea to take a break for a night to clear our heads.

SCAMMER 2 Yeah, right? I think riding dirt bikes that are not street legal and have no mufflers through a random neighborhood at 2:43 in the morning is real relaxing.

SCAMMER 1 Wait. Do you think we should wait until daytime?

SCAMMER 2 No way. We don’t want to bother people and get in their way. Didn’t we learn our lesson?

SCAMMER 1 Good call. At night everyone is inside and out of our way. All asleep.

SCAMMER 2 Take Care of It 16 Right. A perfect time to ride our super loud dirt bikes with no mufflers - which neighborhood should we choose?

(Transition)

(Alex sleeping, narrator standing over)

NARRATOR Vroom vroom.

(Alex wakes up.)

END
```

---

## IC-1446: The Chess Piece Piece

- Title: The Chess Piece Piece
- Author (byline): Tom Mizell
- Work: The Chess Piece Piece
- Publisher: Mushroom Cloud Press
- Publication date as stated: August 1, 2023
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1389
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
The King- A beleaguered ruler
The Bishop- A pretentious clergyman
The Pawns- Nearly identical foot soldiers
The Knight- A horse?
The Rook- A building?
The Queen- A vicious warrior
[The King surveys the battlefield with his advisor, the Bishop, at his side.]
King: It is a dark day for the chess board. Tensions between the kingdoms of Black and White
are at an all time high. War approaches. The battle lines have been drawn. And then battle lines
have been drawn that criss-cross those first battle lines so that we can have nice, neat squares.
Bishop!
Bishop: Yes, my king?
King: How go the preparations?
Bishop: Oh most excellently, your highness. The Holy Order of the White Kingdom has
assembled-
King: Wait. Stop.
Bishop: Sire?
King: The Holy Order of the White Kingdom? Doesn’t that sound a little…? I mean. Yikes.
Bishop: But your highness, for millennia, this has always been the White Kingdom.
King: I mean, sure, but I always thought that was, like, a uniform thing.
Bishop: And as your majesty’s bishop, I lead the Holy Order-
King: Church. Just say church.
Bishop: I lead the church of the Kingdom of White. In order to preserve the values and traditions
of-
King: It’s just- Are we sure about the name?

Bishop: Sire, don’t lose faith! Your people need you. And the White people are a proud people.
King: Stop saying it like that! You know what? The Kingdom. Just say The Kingdom. We’ll win
the war, then we’ll workshop the name.
Bishop: Yes, your majesty.
King: Now, where is my army?
Bishop: Here they come, your majesty. The finest foot soldiers in the kingdom.
[The Pawns enter. They are short, coarse, and nearly identical to one another.]
Pawn A: Hello.
Pawn B: Hello.
Pawn C: Hello.
Pawn D: Hello.
Pawn E: Hello.
Pawn F: Hello.
Pawn G: Hello.
Pawn H: Hello.
Bishop: How dare you, men! This is his highness, The King, Lord and Protector of the realm!
You must address him as “Your Majesty.”
Pawn A: Oh! Sorry, your majesty.
Pawn B: Sorry, your majesty.
Pawn C: Sorry, your majesty.
Pawn D: Sorry, your majesty.
Pawn E: Sorry, your majesty.
Pawn F: Sorry, your majesty.

Pawn G: Sorry, your majesty.
Pawn H: Sorry, your maj-
King: That’s quite alright! Thank you. (Aside) Bishop, who are these strange men?
Bishops: Pawns, your majesty.
King: Pawns?
Bishop: Peasants, your majesty. Farm folk.
King: Desperate times, I suppose. And they're… twins? (Quickly counting them) Octuplets?
Pawn C: Yes, your majesty.
Pawn D: Our mother was in a lot of pain.
Pawn E: Cracked her open like an egg, it did.
King: I can imagine. Well, let’s see how you are on the field of battle. You there! Let’s see you
march.
Pawn G: Aye, sir!
[Pawn G marches a single step forward.]
King: Is that all?
Pawn G: Aye, sir.
King: You only moved one step forward.
Pawn G: Aye, sir.
King: Could you take another step?
Pawn G: I don’t think I can, your majesty. I think I need to stop and process the step I just took.
It was honestly a lot for me to handle.
King: Then, you there! You try marching.
Pawn H: I can’t, your majesty.

King: Why not?
Pawn H: Well, he’s right in front of me, sire.
Pawn G: I am right in front of him, sire. On account of the step I took.
Pawn H: Can’t march forward. He’s in the way.
King: Then step around him.
Pawn H: (mispronouncing) A-rooned?
King: Around.
Pawn H: A-ronned?
King: Around! Step around him!
Pawn H: I’m sorry, your majesty, I don’t know the word! I haven’t done any book learning.
King: Then take a step backward!
Pawn H: Again, you’re going to need to simplify the vocabulary.
King: Forget it! Bishop, we need someone to train these men.
Bishop: Of course, your majesty. I have acquired the services of the finest knight in the
kingdom.
King: Thank goodness for that.
Bishop: Ah, here he is now.
[The Knight appears. He is a horse.]
Knight: (Neighs.)
[The King, lost for words, stares at the Knight. He slowly turns his head toward the Bishop.]
King: Bishop?
Bishop: Yes, your majesty?
King: That is a horse.

Bishop: Yes, your majesty.
King: I asked for a knight?
Bishop: Correct.
King: And that’s a horse.
Bishop: Right.
Knight: (Huffs in affirmation.)
King: Does the horse have a knighthood?
Bishop: He does, your highness. He was awarded a knighthood for bravery in battle.
King: Bravery in battle?
Knight: (Whinnies.)
King: Does he… does he use a sword then? A lance? Does he just kick people?
Bishop: He jumps.
King: He jumps?
[The Knight whinnies and does a little jump.]
Pawn B: Wow. Wish I could do that.
King: I can’t go into battle like this! Isn’t there anyone else?
Bishop: Well, there is the Rook.
King: Who is that? What does that mean?
Bishop: I believe it comes from the Persian “rukh,” meaning chariot, but-
King: A charioteer! Wonderful, just like the Romans. Where is he?
Bishop: Well-
[The Rook is a building. He stands straight, still, and silent.]

Rook: …
King: Oh my god, when did that castle get there?!
Bishop: That would be the Rook, your majesty.
King: This building is the Rook? My charioteer is a brick building?
Rook: …
King: Does it… move?
[The Rook silently steps from side to side.]
Bishop: You can hide behind it if you like.
King: I just might.
Knight: [Neighs.]
Bishop: What’s that? Oh! I believe her majesty the Queen is approaching.
King: The Queen? (Sarcastically) Oh, that’s just what I need.
Queen: Yoo-hoo!
King: Dearest? What are you doing here?
Queen: I’m here for the battle!
King: But sweetheart it isn’t safe!
Queen: Not safe for them. I’m gonna mess some people up.
King: Do you have any combat experience?
Queen: Who cares? I have the itch. The warrior fever. I’m ready to kill.
King: What? Wouldn’t you rather stay in the Rook?
Queen: And miss all the fun? The glory? I don’t think so! I’m out for blood. Anywhere on the
board, I will be there! I am a one-woman slaughter. Get the sausage casings, boys- I am turning
this board into a meat grinder!

Bishop: Your majesty, the time for battle is fast approaching!
King: You’re right. Men… Honey… This is the moment we’ve prepared for. Is everyone ready?
Pawn A: How are we paying for this war? It ain’t coming out of our taxes, is it?
King: Sorry?
Pawn A: I just want to know who’s picking up the check for all this.
Pawn B: It’s not about the check, mate.
King: It is all about the checkmate!
Pawn A: (Whispering aside) Someone’s touchy.
Knight: (Huffs conspiratorially)
Pawn F: I’ve got a question!
King: Fine. What is it?
Pawn F: If I march all the way over there, what do I get?
King: If you march all the way to the enemy base?
Pawn F: Yeah, what do I get?
King: What do you want?
Pawn F: Could I get a new job?
King: A promotion? Certainly, I could make you a knight or a bishop-
Pawn F: Would you marry me?
King: What?
Pawn F: I want to be a queen. I get to the other side, will you marry me?
King: I already have a queen!
Queen: I don’t mind!

Pawn F: Besides, she might die.
Queen: That’s true, dearest, I might die.
King: Then… sure. I guess. But only if you get all the way over there! Now, hush, I can see the
enemy assembling.
[The King looks through a spyglass across the field. He gasps.]
Bishop: What is it, sire?
King: The enemy appears to be… circles.
Bishop: Circles, your highness?
King: Yes, circles. Giant disks. Men, do you know what this means?
Knight: (Whinnies confusedly)
King: They’ve decided to play checkers instead! We’re safe. We can all go home.
Queen: Aww, I wanted to frenzy…
King: Bishop! Let us return to the castle for a feast.
Bishop: Yes, your highness. Men! Follow me!
[All exit except the two pawns, still caught in a stalemate.]
Pawn G: Move! I am trying to go to the castle.
Pawn H: You’re the one in the way, you move.
Pawn G: You move.
Pawn H: You move!
Pawn G: You move!
Pawn H: You move!
[THE END.]
```

---

## IC-1447: The Furious Fists of Julia

- Title: The Furious Fists of Julia
- Author (byline): Kevin Burgun
- Work: The Furious Fists of Julia
- Publisher: Mushroom Cloud Press
- Publication date as stated: September 1, 2022
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: NARRATOR, JULIA, RILEY, TAYLOR, BOSS, HANDLER, BAD GUY 1, BAD GUY 2, OLD LADY
- Teaser before the introduction: No
- Spoken words (computed): 1967
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
(Author’s note: This was written for performers who were interested in exploring unique fight choreography within a DUO. The fights can be as simple or complex as the performers feel best suits their ability.)

(Author’s note: This was written as a semi-parody of the revenge action movie genre. While
there may be vague references to specific movies, knowledge of the movies should not be
necessary for the performance or enjoyment of the piece.)
CHARACTERS (With suggested doubling breakdown)
Julia - Performer 1
Narrator - Performer 2
Riley - Performer 2
Taylor - Performer 2
Boss - Performer 2
Handler - Performer 2
Bad Guy 1 - Performer 1
Bad Guy 2 - Performer 2
Old Lady - Performer 2

(Start with JULIA facing the audience, sitting at a desk, typing away. NARRATOR stands with back to JULIA facing the back wall - upstage)

NARRATOR: It was a Friday like any other Friday. (Julia takes a sip of coffee and continues to work.) Julia seemed unique to her coworkers. She did not mind the drudgery of the job.

JULIA: I actually enjoy the drudgery of the job. Nice and quiet. Not like my…..old life. (Shakes her head to rid her mind of the memories creeping in.)

NARRATOR: Julia embraced the quietness. The simplicity. The simple joys of normalcy.

JULIA: (Looks at watch) Almost time for my midmorning break.

NARRATOR: And Julia’s simplest and most joyful simple joy was her midmorning…

JULIA: Yogurt cup.

NARRATOR: (same time as Julia) With flax seeds and graham cracker crumbles.

JULIA: (same time as Narrator) With flax seeds and graham cracker crumbles.

RILEY: (as grating and annoying as possible) Hey Julia, almost time for midmorning break, huh? Yogurt again, huh?

JULIA: (Tenses and looks annoyed) Riley.

NARRATOR: Riley last name unknown. The bane of Julia’s existence. The one annoyance capable of shattering an otherwise pleasant Friday.

JULIA: (looks at watch) There are still 2 minutes until break.

RILEY: C’mon now, it’s Friday. Get a head start on the ol’ midmorning break-er-eeno. I’ll walk with ya.

JULIA: No thank you.

RILEY: What kind of yogurt did you bring today?

JULIA: (Through gritted teeth.) Key Lime.

RILEY: I’ve never tried that, is it good?

JULIA: It’s fine.

NARRATOR: It was, in fact, Julia’s most favoritest flavor of yogurt from her most favoritest brand. It was, however, always hard to find. And so, when it was found, and she could bring it in to work, it was a particular treat.

JULIA: Now please leave, I still have to work for (looks at watch) one more minute.

NARRATOR: And so Riley left. And exactly one minute later Julia locked her screen, as per company policy, stood up, straightened her outfit, and proceeded to the break room.

TAYLOR: Hey Julia, you just missed Riley.

JULIA: Taylor.

NARRATOR: Julia washed her cup. Opened the cabinet to get her bag with the flax seeds and graham cracker crumbles, and began to walk towards the refrigerator holding her yogurt.

TAYLOR: You know you are supposed to refrigerate those.

JULIA: What?

TAYLOR: Flax seeds. You are supposed to refrigerate them. After opening, I mean.

JULIA: I’ll do that from now on. Thank you.

TAYLOR: No problem-o.

JULIA: (Opens refrigerator. Pauses.) Where is my yogurt?

NARRATOR: There was no yogurt. Of any kind. No raspberry, Or blueberry. No mixed berry. And especially not any Key Lime.

JULIA: Taylor?

TAYLOR: Couldn’t tell ya. (Pause, snaps fingers) Oh, Riley grabbed a yogurt out of the fridge. Said something about you wanting feedback on if it was a good flavor or not?

JULIA: What?

TAYLOR: Yeah, took a couple bites then pitched it in the trash. Said it was tart.

JULIA: (looking in the trash. Picks up yogurt, there is a coffee ground filter on top of it.) My yogurt.

TAYLOR: Oh yeah, I just made a pot of coffee, we need more filters.

JULIA: My yogurt.

NARRATOR: Julia held in her hand her yogurt. Two spoonfuls missing, covered in old coffee grounds. Her simple joy. Robbed from her. By a sniveling, annoying, coward. JULIA; Where’s Riley? Office?

TAYLOR: Nopers. Riley said working was for suckers and decided to take off early. Car is gone. Riley is taking the early weekend. Not like us good eggs. And Riley’s the leader for the promotion, if you can believe that. Makes no sense.

NARRATOR: Julia barely contained her rage.

JULIA: Is the boss in?

NARRATOR: Julia didn’t wait for a reply, she simply walked steadily to the boss’ office.

JULIA: Got a second?

BOSS: Julia! For you? Always. How is my favorite worker bee?

JULIA: I need Riley’s home address.

BOSS: Well, Julia, you know I can’t give out that information.

JULIA: I’m going to ask one more time, I need Riley’s home address.

BOSS: You are scaring me, here. I’ve never seen you like this before, who are you?

JULIA: Who am I? (Dramatic pause. Her face turns menacing.) I’m me.

(JULIA grabs the boss by the hair or tie, slams head to desk, then does it twice more.)

JULIA: The address.

BOSS: Stop! Please! I have a family! Two beautiful golden retrievers!

JULIA: If you want to see your family again, give me the address. I don’t hurt dogs though.

BOSS: You misunderstand, my family is the dogs.

JULIA: Oh. That complicates matters. I guess this is just between you and me. And my fists.

NARRATOR: In that moment, Julia became who she used to be. The person she thought she had buried. But she forgot one thing: You can’t bury fists. (Slight pause.) Because you need them for other things, like eating and typing and showering and scratching that itch that you sometimes get between your shoulder blades.

BOSS: Not the fists!

(JULIA repeatedly punches boss.) BOSS; Her fists are so furious!

JULIA: The address!

BOSS: 1111 Circle Cove Boulevard! Apartment C12!

JULIA: (Lets go of boss) I quit. (Boss falls to ground.)

NARRATOR: The rage had broken through like the phoenix of old. Julia was on a mission. One thought: Revenge.

(Julia exits by standing upstage, back to performer 2.)

TAYLOR: Hey! Are you going to eat this? Guess not. I think I can eat around the coffee grounds here. (Tastes.) It is a little tart….

NARRATOR: Flashback.

JULIA: (On Phone.) Yeah. I’m at the statue in the park. I don’t see you. (Looks at watch) Two minutes out? You’ll be late. You know how I feel about time.

NARRATOR: Five years ago. Griffith, Indiana. It was mentioned in a movie once. Other than that, relatively unknown.

JULIA: Cold.

NARRATOR: Julia has been here for three days. Observing. Gathering intelligence. Now she’s waiting for her handler.

JULIA: Hey.

HANDLER: Protocol, Jules.

JULIA: Kleenex. Xerox. Spongebob. Orange. Four thousand. Red. Ernest Hemingway.

HANDLER: :Pigeon.

JULIA: So, are we a go?

HANDLER: There’s a slight change.

JULIA: I don’t like changes.

HANDLER: Unavoidable.

JULIA: What’s the update?

HANDLER: There’s a dog now.

JULIA: I don’t do dogs. I’m out.

HANDLER: Wait.

JULIA: What?

HANDLER: It needs rescued.

JULIA: I’m listening.

HANDLER: Along with a cat, a ferret, and two gerbils.

JULIA: I’m not good with cats.

HANDLER: You'll make it work.

JULIA: When’s the insertion?

HANDLER: That hasn’t changed. Tonight.

JULIA: After this, I’m out. I’m serious.

HANDLER: Sure you are. Good luck, Jules.

JULIA: (Checks watch) Yeah.

NARRATOR: Later that night. In an old warehouse on Reeder Road.

BAD GUY 1: Cold out. Why are we guarding these animals anyway?

BAD GUY 2: The Boss wants them guarded. We guard them. You know pets are good for overall feeling of well being.

BAD GUY 1: No kidding?

BAD GUY 2: Did you hear that?

BAD GUY 1: No, what. Wait, Yeah. It sounds like. OW! (Bad Guy 1 gets knocked down.)

NARRATOR: It was the sound of an approaching fist. A furious fist.

BAD GUY 2: Where did you go?? Who’s out there?

JULIA: I am.

BAD GUY 2: Do you know who owns this warehouse? The boss never forgets! Revenge will be the focus after this. Everything you love will be taken from you.

JULIA: I don’t care.

(JULIA proceeds to beat up Bad Guy 2. Bad Guy 2 can ad lib painful exclamations.)

BAD GUY 2: Her fists are so furious!

JULIA: (Holding Bad Guy’s head up) Where are the animals?

NARRATOR: Julia successfully rescued the dog, cat, ferret, and two gerbils. There was also a goldfish, but it was like in a 75 gallon tank and that was just unrealistic to carry out. (Awkward Pause). Present Day.

JULIA: (knocking on apartment door) Open up, Riley! Open this door now!

OLD LADY: What’s all of this racket out here now?

JULIA: Sorry, ma’am. Have you seen Riley?

OLD LADY: What do you want with that evil?

JULIA: What do you mean, “evil”?

OLD LADY: Don’t you know?

JULIA: Know what?

OLD LADY: Riley is the overboss of the most powerful crime syndicate in the lower Eastern Western Mid-West.

JULIA: Riley?

OLD LADY: Several years ago, one of Riley’s warehouses was raided and all the pets kept there were stolen. Well, except for the goldfish. Ever since that day, all Riley can think about is revenge. Revenge on the woman who did this.

JULIA: Why are you telling me this?

OLD LADY: Because you are the woman who took those pets. You are the one. And you’ve been hurt, haven’t you? Something has been taken from you just as you took something from Riley?

JULIA: My yogurt.

OLD LADY: What flavor?

JULIA: Key Lime.

OLD LADY: Oh dear.

JULIA: Where is Riley?

OLD LADY: Your fists are indeed, furious, young lady. But Riley is a different creature. Trained all over the world. By the very best. Do you know Mike Tyson?

JULIA: I do.

OLD LADY: Could you get me an autograph?

JULIA: I don’t know him in that way.

OLD LADY: Too bad.

JULIA: Why are you telling me this?

OLD LADY: I’m the older, wiser person who advises the hero. It’s my job. Also, I’m Riley’s mother and Riley told me this morning I was to be put in a home.

JULIA: Where do I go next?

OLD LADY: You need trained. I know someone. They are very good at training montages. And that is what you need if you are to face Riley.

JULIA: It’s too late for training montage.

OLD LADY: It’s never too late. Go to this address. Ask for The Pigeon.

JULIA: Wait.

OLD LADY: Yes.

JULIA: So, I really am back.

NARRATOR: Julia went to the address the old lady gave her. As she feared, it was to her old handler, known only as The Pigeon.

JULIA: Hey.

HANDLER: Protocol, Jules.

JULIA: Enough of that. I need a training montage. I need to finish old business. And new business. All of the business.

HANDLER: Are you ready?

JULIA: I’m ready.

HANDLER: Are your fists still furious?

JULIA: (Holds them up.) Let’s find out.

(TRAINING MONTAGE! You can be as simple or complex as you like. I would choose the extreme of either. If you want simple, have Julia throw like three punches and then move on - silly can work. Or go complex.)

JULIA: (Bent over / Breathing heavily.) Am I ready?

HANDLER: Do you feel ready?

JULIA: (Stands straight.) I’m ready.

NARRATOR: And so Julia headed straight to the warehouse where Riley was. For the final showdown. (Awkward pause for all.) Oh. How does Julia know that’s where to find Riley? Ummm…FLASHABACK!

JULIA: But how will I find Riley when I’m ready?

OLD LADY: Take my phone. I’ve got the GPS tracker on each other’s phones. It’ll show you exactly where to go when you are ready.

JULIA: Thank you so much. This makes things so much easier to explain.

OLD LADY: Get going, time is running out.

JULIA: (Looks at watch.) You respect time.

OLD LADY: At my age, you must.

(JULIA nods.)

NARRATOR: Present Day. Warehouse. Oh, also it’s abandoned, so no innocents. Just Riley, And some total “C” level bad guys. Easy fight before the boss level.

BAD GUY 1: Warm out. Why are we guarding the boss and the goldfish anyway?

BAD GUY 2: The Boss wants guarded. We guard. I once had a goldfish. Won it from a carnival. One of those throw the ping pong balls in the bowl games?

BAD GUY 1: No kidding?

BAD GUY 2: It died three days later.

BAD GUY 1: Tough break.

BAD GUY 2: Did you hear that?

BAD GUY 1: No, what. Wait, Yeah. It sounds like. OW! (Bad Guy 1 gets knocked down.)

NARRATOR: It was the sound of an approaching fist. A furious fist.

BAD GUY 2: Where did you go?? Who’s out there?

JULIA: I am.

BAD GUY 2: Do you know who owns this warehouse? The boss never forgets! Revenge will be the focus after this. Everything you love will be taken from you.

JULIA: I’ve heard that before. But jokes on you, I have nothing left to be taken. My yogurt is gone forever.

(JULIA proceeds to beat up Bad Guy 2)

BAD GUY 2: Her fists are so furious!

JULIA: (Holding Bad Guy’s head up) Where’s Riley?

RILEY: Riley is right here.

JULIA: Riley.

RILEY: Julia.

JULIA: So it comes to this.

RILEY: Betrayed by my own mother.

JULIA: No. You betrayed you. You took my yogurt.

RILEY: It was the perfect plan. Wait until you retire. Get used to a quiet life. Rediscover the simple joys of life. Wait until you focus on one simple joy in particular, then rob you of it.

JULIA: You could never have known.

RILEY: Who left the coupon for yogurt on your desk one day?

JULIA: No.

RILEY: Who had Taylor forward you the article about flax seeds and graham crackers for texture?

JULIA: You monster.

RILEY: Who went into your favorite supermarket every Saturday morning before you got there and bought all of your favorite yogurt so you valued it more?

JULIA: It’s rare.

RILEY: It’s literally not. It’s like the worst flavor of the entire line.

JULIA: Liar! The worst flavor is boysenberry.

RILEY: I forgot about boysenberry.

JULIA: Let’s do this.

RILEY: Revenge!

(They fight. As complex and simple as desired. It should end, as has been the trend, with Julia holding Riley and pummeling with fists.)

RILEY: Her fists are so furious!

(Julia has her fist cocked, about to deliver the final blow.)

RILEY: Go on! End it!

JULIA: Key Lime!

HANDLER: Stop! You left this life.

OLD LADY: I’m Riley’s mother.

TAYLOR: Flax seeds need refrigerated.

BAD GUY 2: I won a goldfish.

HANDLER: You aren’t that person any longer.

JULIA: I am who I am.

OLD LADY: I don’t want to go in a home.

BAD GUY 2: I miss my goldfish sometimes.

TAYLOR: There’s nothing wrong with boysenberry.

HANDLER: You are not defined by your past.

RILEY: Just do it already!

JULIA: (Pause) No. (Let’s Riley go.) I’m done.

NARRATOR: And so Julia walked into the night. In search of a frozen yogurt shop where you can mix in an assortment of toppings. It was that sort of night. As for Riley…

RILEY: (Picks Self Up) Big Mistake. I don’t forget. Get ready for Part 2. Wait, what was that? Did anyone hear that? OW. (Riley gets knocked out.)

JULIA: Treat your mother right, Riley. (To Bad Guy 2) Can you give the goldfish a good home?

BAD GUY 2: Really? Yes. I will love it with all my heart.

JULIA: It’s yours. Remember, you can leave behind who you were. Take the goldfish. Forge a new life.

BAD GUY 2: I will. I won’t let you down.

JULIA: Maybe something good did come from all of this. Now to get that frozen yogurt. And a new job. END PLAY
```

---

## IC-1448: The Ruler

- Title: The Ruler
- Author (byline): Frank Smith
- Work: The Ruler
- Publisher: Mushroom Cloud Press
- Publication date as stated: August 1, 2023
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: JANE
- Teaser before the introduction: No
- Spoken words (computed): 2433
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
A Dramatic Monologue

Written by Frank Smith SCENE I School Auditorium.

(A line of invisible, chattering students, waiting to get their photos taken. But we only see one:) JANE.

(JANE (13), unflappable, smiles too big, posing for a picture. She then stops, rolling her eyes.)

JANE: ‘Sup. I’m Jane. Ready for a hot topic? I hate pictures. Not just school pictures. Those are dumb. Definitely. But there’s something about smiling when you’re not, like, you know, in the mood… that just feels very fake and pointless to me. My best friend, Frederica, she felt the same way I did. Whenever we had to take pictures for school, we would have the ugliest expressions on our faces. That sort of made us feel like it wasn’t as huge a waste of time as it could be. We were showing how we actually felt – which was that we didn’t need to perform for people. And that was our approach to Instagram, too. We made a lot of silly faces that reflected how we actually felt in the moment. I think that’s why Frederica had been my best friend for so long. We didn’t believe in faking how we were feeling. Even when the truth could be pretty unpleasant.

(Jane walks away, and starts to play a portable video game in the corner.)

JANE: Okay, so to backtrack a little. I first met Frederica on Halloween, when we were both five years old. We were both dressed as the costumes every little girl dresses as at that age: Mario and Luigi, the Super Mario Brothers. Spoiler alert: Frederica and I were both huge gamers. Which wasn’t such a common thing for girls in our grade, because boys tried to act like video games were their territory. Which is stupid. It’s like saying ice cream is our territory. No, losers, everyone likes video games. Just like everyone likes food. Boys are dumb. So once we came in dressed in matching costumes, Frederica and I became inseparable. We didn’t have the exact same interests. I was more into band, because I played the drums. Loudly. Which, of course my parents loved. And she was more into dance, which, inevitably, evolved into cheer as she got older. But we supported each other. She came to my concerts, even though classical music was not really her thing. I went to the games at which she cheered, even though sports are not really my thing. But that’s what friends do. They support each other. Through good times, and band.

(Jane loses the game, and groans. She starts up another round.)

JANE: It was really easy to be Frederica’s friend in elementary school, because we spent the whole day together. Every class, we sat right next to each other. And then, we would hang out after school. Practically the only moment we weren’t together was when we went to sleep at night. We spent about half the time at my place, and half the time at hers. Her parents loved me. Her mom, Helga, especially. Maybe a little too much – she would constantly tell Frederica to be more like me. To study just as much, to work just as hard. It wasn’t that Frederica didn’t work hard. I guess I just worked a little harder. But she also wore nicer clothes, and put on make-up sooner. So we each had our strengths, I guess. We were a good match. A great match, even.

(Jane cheers, as she advances to the next level. She puts on a determined face, as the game gets significantly harder.)

JANE: When we got to middle school, that’s when things changed. Our elementary school, Leland, was combined with three other elementary schools in the area: Johnson, Brown, and Ward. So suddenly, there were four times as many kids in the school. And that meant that Frederica and I didn’t have every class together anymore. We shared two out of the eight: Spanish, and Math. Which were two of Frederica’s least favorites, so it’s not like she was in a great mood when we were in those classes. But still, it was always nice to sit next to her, And be able to exchange notes. But then, the other thing that changed was that Frederica told me, school work was a little tougher for her, especially since she didn’t have me in class to whisper things to her, when she didn’t understand. So, she needed more time to do her homework. And we weren’t spending as many days together after school. My mom told me this was normal. Her mom told me that it was just her way of catching up to me, academically. But I really started to wonder how normal this all was, and if the time apart was going to have an effect on our friendship.

(Jane loses the game, but prevents herself from having too emotional a response. She calmly puts the game aside.)

JANE: It did. There was this girl in our math class, Aly, who was basically the Kim Kardashian of middle school. She was rich and famous, but nobody really knew how. She honestly didn’t even say that much. But she walked around with this air about her, like she was so much better than you. And everyone kind of gave into that, and acted like she WAS better than they were. Bow down to Aly, the ruler of 6th Grade. Frederica and I thought that she was incredibly lame, and didn’t really act like all the other kids, worshipping the ground she walked on. At least, not at first. But one afternoon, when we were hanging out, for the first time in a while, actually, Frederica said, “You know, Aly’s not actually that bad.” Kind of out of nowhere. I asked her why she said that. Frederica said, “I don’t know, it seems like everyone’s hard on her. But I’ve been talking to her in the hallway and, I don’t know, I think she’s kind of all right.” I didn’t really believe what Frederica was saying, but I thought, all right, next time we’re in the hallway, I’ll give this Aly girl a shot. Nobody likes to be judged without being known.

(Jane goes to play the game again, but decides to give herself a longer break.)

JANE: The next day, between classes, I saw Aly and Frederica giggling together. There was a crowd of people around them, not really part of the conversation, more like passively, witnessing it. So I walked up to these… parasites would be mean, so let’s say, onlookers… and tried to join the conversation with Aly and Frederica. “Hey, what are we talking about?” Aly was steely. She didn’t say anything to me. Which I figured she’d do. Right as I’m thinking, Frederica is a bad judge of character, I started to say, “Hey Frederica, want to go grab a soda in the cafeteria?” Frederica didn’t say anything back. Which was super unlike her. She always had something she wanted to say. “Frederica, did you hear me?” I asked again. Frederica turned to me and said, steely like Aly, “Give us a minute.”

(Jane stands and starts pacing, irked out of her mind.)

JANE: I’m floored. I didn’t even know what to say to that. Frederica had never talked to me like that, ever. I just turned around, and walked away. And then, I heard Frederica and Aly giggling, which turned into everyone else giggling. I didn’t even want to think what they were saying. That afternoon, I was with Frederica in Spanish. Not Aly, thank goodness – she wasn’t in that class. Frederica immediately came up to me, and said sorry about how she was acting earlier. “Aly is just weird around new people,” she said, “I’ll make an effort to talk you up to her, so she doesn’t act like that next time.” “Okay,” I said, ‘First of all, I don’t really care if Aly likes me or not.” “That’s a mistake,” Frederica said, “She’s an important person to know.” “Right,” I said, “So, I’ve never cared about that. What worries me is how YOU were talking to me.” Frederica smiled and rolled her eyes. “When did you get so sensitive?” she asked. “Sensitive?” I said. “I’m not sensitive. You were being rude.” Frederica rubbed my shoulder and said, “Lighten up, Jane. Mario Kart later?” I thought to myself for a moment… before slowly nodding. It had been a while since we had played together. And when she came over that afternoon, it was totally normal, and we had a great time. It was like nothing had changed. Until Frederica’s mom walked in. And said she hoped that Frederica was on top of her homework, since she was taking all this time to play video games. Frederica shot back, “Why don’t you ask Jane if she’s done her homework yet?” Frederica’s mom replied, “I don’t have to worry about Jane. I always have to worry about you.” It was tougher than Frederica’s mom usually was, when making comparisons between the two of us. And Frederica looked more upset than ever.

(Jane calms down, and sits again.)

JANE: Over the next few days, every time I tried to talk to Frederica in the hall? She ran off before I had the chance to say anything. And in class, she sat far away from me. In Spanish, it was fine – I was able to throw myself into my work. But in Math, I kept getting distracted by how she and Aly would look at me, point, and giggle. At home, I asked my Mom what she thought was going on. She told me the story about a friend she had in middle school, Clare, who found a new friend, Beverly, and never really talked to my Mom after that. I really didn’t want the situation to be like that. My Mom asked if I had tried to talk to Frederica. I said yes, but she wasn’t hearing me. My Mom then offered, do you want me to call Frederica’s Mom, and see what’s up? Maybe she’ll tell me something that Frederica won’t tell you. I knew this was risky, but I was desperate at this point. I wanted my friend back. I needed her back. I overheard the conversation, just to make sure my Mom wasn’t saying anything too embarrassing. But I thought she put it really gently. How I really valued my friendship with Frederica, and how it was wonderful that Frederica was making new friends. Still, I was hoping that, even if we didn’t have as much time together as we used to, if Frederica could try to fit me in a little more. Frederica’s Mom said that all sounded totally reasonable, and thanked my Mom for calling. I thought that that would do the trick. But all it did was make things worse.

(Jane can’t help herself. She dives back into the video game.)

JANE: Now, instead of ignoring me in the halls, Frederica outright made fun of me. Making fun of me for being in band, for my clothes. For playing video games. Things she used to either not mind, or love about me. I never said anything back – what was the point of that? I just retreated. And it wasn’t like I was the only girl that she and Aly were making fun of – there was this really sweet debate student, Micky, who they never had a nice word about, either. I sadly realized that our friendship was over, and I had to move on. But they weren’t making it easy – the more I ignored them, the more they tried to make it personal. Saying how nerdy I was, how ugly I was, how friendless I was. I stayed strong there, cried all the way home, and talked to Mom at night. Then, I got ready for the next day of school. But one day, in Math class, something happened that I couldn’t just ignore anymore. It was a Geometry assignment, and everyone got passed out these 12-inch rulers. Frederica went out of her way to come over, and steal my ruler. I kept asking her to hand it back, and she kept ignoring me. Finally, I demanded that she give it back, loud enough for the teacher to hear. I didn’t go directly through an adult, since I knew that was a trigger of Frederica’s, but I needed help getting through in this moment. Frederica grudgingly handed me back the ruler. But she’d written something on it in Sharpie: “Jane has no friends.” After all these years, after all these memories, after all my grace – this was what I got from her? I took the ruler, stared Frederica in the eye and slammed it down on her desk, so hard it broke in half. The class gasped. I then grabbed the Sharpie out of Frederica’s hand, and scribbled one extra letter on the half of the ruler I still had. Shoved it in her face, so she could see what it said now: “Not friends.” For a few days after that, Frederica and Aly made fun of what a little psycho I was. But for some reason, no one seemed to laugh along with them anymore. I think it was the fact that they had tried to make fun of a few too many people, and those people were people like me, and Micky: nice people. Good people. Which Frederica had decided not to be anymore.

(Jane is surprised to see what a hot streak she’s on with the game.)

JANE: Frederica’s Mom called my Mom, and asked if there was anything to be done. I answered myself: no. Frederica had decided not to be friends with me anymore. And I was choosing to accept her decision. I hung up, confident that I was still nice, that I was still me. And I knew exactly how to prove it – at school, I walked up to Micky in class, and introduced myself. I’d been afraid to do it until now, due to guilt by association. But I knew who my real friends were, and who they weren’t. So did Aly – she moved on from Frederica within the week. People were finally seeing how mean she was, and frankly, how badass I was. Frederica came to me in the hall one day, apologizing, saying she didn’t know what came over her. She asked if we could be friends anymore. I looked her directly in the eye, and said to her: what it said right there, on the ruler – that still stands.

(Jane wins the game, and cheers triumphantly.)

JANE: Micky is great, though. It’s been awesome learning how to debate from her, and she’s way better at Mario Kart than Frederica ever was. I’ve had to really level up my game to be competitive with her. But it’s a fun competition – it doesn’t feel like I have anything to prove, or anything to feel bad about when I lose. I think that’s what real friendship looks like – you better each other. You challenge each other. But you never try to destroy each other. I still have that piece of the ruler that broke. I know that seems weird. But sometimes, in order to know the truth, you have to look directly in the face of a lie. I love my Mom. I love Micky. And I love me. And I sincerely hope Frederica can one day say all those things about herself. I mean that, sincerely.

THE END.
```

---

## IC-1449: The Worst Day Ever

- Title: The Worst Day Ever
- Author (byline): Micah Larson & Brian Sams
- Work: The Worst Day Ever
- Publisher: Mushroom Cloud Press
- Publication date as stated: December 11, 2023
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: DR, NPP
- Teaser before the introduction: No
- Spoken words (computed): 1572
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
By
Micah Larson and Brian Sams
Characters:
Dr. Worst- A man who dreams of being a super villain but always ends up accidentally doing
good things instead
Sam- Dr. Worst’s abducted/adopted son and partner in “crime”
TV Reporter- Over the top doesn’t even begin to describe this guy
Mayor- A self important man who tries to give Dr. Worst the key to the city
Presenter- A mansplainer who tries to present Dr. Worst with the Turing Award
Nobel Peace Prize Guy- Tries to give the NPP to Dr. Worst
Summary: Dr. Jonathan B. Worst has a troubled past - as a genius child who was the victim of
bullying. As such he has sworn to take revenge on the world through a series of evil schemes -
all of which backfire and end up serving humanity in some way. Only his relationship with his
abducted - and then adopted - son can help him to realize his true nature.
Dr. Worst: HAHAHA! And now, just a bit of manganese and smidgin of chromium, perhaps a
drop of giant squid ink for good measure… and we’re done Sam!
Sam: What’s the plan this time, Dad?
Dr: We’re doing evil deeds in our evil lab on Skullcrusher Mountain, Sam....When we’re working,
you are supposed to call me Sir!
Sam: Oh, right. Sorry, Sir. What’s the plan?
Dr: When this formula is released into the city’s water supply system, it will stop all water flow in
the city! If it works here, we’ll go national, and bring this country to its knees! Then, they will
recognize the evil genius of Jonathan B. Worst! And then we’ll have ice cream to celebrate!
Would you like that? Haha! Open the valve!
Sam: Okay… (Opens valve)
Dr: And now we play the waiting game. Or Clue. I love Clue. Where’s my coffee? (Takes a big
sip)

(Cut to the TV turning on) TV Reporter: This just in: the city’s failing water pipes have been miraculously reinforced and the dangerous contaminants are completely gone!

Dr: (Spits out coffee) Reporter: What mysterious hero intervened to save our fair city? Stay tuned as our panel debates who our secret benefactor might be.

DR: (Mutters while he cleans up coffee) Ohhh, I should have gone with my original evil plan and just built a bunch of Dollar Stores. Intro here: Sam: Someone’s at the door, Sir. I’ll get it. (Opens door) Mayor: Hello, I’m the Mayor, I’ve come to present a key to the City to Dr. Worst. Dr.: Ooooh, let me see that…(Walks over to the door, takes the key, chucks it into the lab, and slams the door in the Mayor’s face.) Sam: Jeez, Sir. That was kinda rude. Dr.: There’s a reason we live on Skullcrusher Mountain my boy. Keeps the riffraff away. Look, Sam, as an innocent orphan boy, I made a spectacular science fair volcano. It was supposed to expel lava quite impressively. Instead, it barely erupted at all, and the perfect little children laughed at me and called it the Pimple of Doom. Did anyone care that the lava was also a cure for dandruff? No! On that day I swore to take my revenge and that the world would take me seriously! Sam: And how’s that been going for you, Sir? Dr.: *Sigh* Not so good, Sam. There have been… setbacks.Time for a new plan. Fetch me the Notorious Notecards of Not Niceness, Sam. (Sam gives him the cards) Yes, yes, some very good, I mean very EVIL ideas in here, Sam. Let’s see… Ooh, kidnapping and ransom! Sam: You tried that, Sir. You kidnapped me. Dr.: Oh, yes. Turns out you were in a very toxic and abusive home… Ended up paying those people quite a lot to let me keep you… Ah, remember the Wifi password caper! I added a 1 to everyone’s password. Took them a while to figure that one out!

Sam: Yes, Sir. Everyone spent quality time with friends and family. You and I played frisbee golf and got churros. Dr.: Must you rub salt in my wounds, Sam? …That was a great day. Oho! I forgot about this nugget! Haven’t tried this one yet… The AK-47! Sam: The AK-47? Dr.: It took me 46 failed attempts, (Opens a drawer and removes object - it is not an AK- 47) but the Autocorrect Killer 47 is ready to go with the push of a button! (Holds it out to Sam, then jerks it away) But not that button! That’s the self-destruct button! Push that and oh boy you’ll regret that! Sam: Why is it so much bigger than the start button? Sir, this reminds me of the SuperSpammer 2000… Dr.: Which was supposed to spam call every phone in the world simultaneously with extended warranty offers! Sam: But instead… Dr.: It short circuited every spam calling system worldwide…the peace and quiet was almost unbearable! Just push the button, Sam! No! Not that one! Sam: Just messing with you, Sir. (Pushes button) Dr: Nice one. You got me. TV Reporter: This just in: mobile device users worldwide report that autocorrect no longer wreaks havoc with texts! Experts suspect the work of Dr. Jonathan B…. Dr.: Turn the TV off, Sam! Sam: You programmed it to turn on if there was news related to your plans… Dr.: (Exasperated) Aaaah. (Rubs his temples in frustration)

(Doorbell rings) Sam: The door, Sir.

Presenter: Hello, we are from the Association of Computing Machinery, we’re here to present you with the Turing Award, the world’s most prestigious computer coding award… Dr.: Haven’t we met? Presenter: We tried to give you an award for your Stoplight code… Dr.: That was supposed to turn every stoplight in the world red! Presenter: Instead it made traffic systems 75% more efficient! You saved people time and reduced carbon emissions! Dr. Alan Turing was… Dr.: You don’t have to tell ME who Alan Turing was… Fine. Give it to me. Now, thank you! And get out! (Slams door.) This day keeps getting worse, Sam. We need a game changer! (Flips through notecards) Hmmmm. Do I dare? Sam: What did you find, Sir? Dr.: Remember when we binge-watched Friends (or insert show of your choice here) and you were too tired to go to school? Sam: And you created a snow day with, what was it? The ReFreezinator? We made cocoa. And a snowman. Dr.: And I sang “Let it go” until you got quite annoyed…Well, I sort of scaled up the ReFreezinator… Sam: That doesn’t sound like a very good idea… The door again, Sir. Dr.: Skullcrusher Mountain! Who wants to go to Skullcrusher Mountain? What is wrong with you people?

NPP: Hello, we’re from the Nobel Peace Prize Comm….
Dr.: Shhh! Sit down! Not there, that’s the cat’s chair. She’s not here right now, but she
knows. Now, Sam! The ReFreezinator control!
Sam: Here it is, but Da….Sir, I don’t think…

Dr. : And you. Mr. Nobel Prize! You can have the honor of pushing the button that will bring the world to its knees! No, not the big one! (He jerks the controller away from the presenter, very annoyed) That’s clearly labeled! (Presenter pushes the correct button) Aha! Now, watch as the temperature tanks and the planet is plunged into a new Ice Age! TV Reporter: This just in: Worldwide temperature drops 5 degrees and shocks and delights climate scientists.

NPP: Congratulations, Dr. Worst. The planet is on its knees in thanks for your efforts to
combat global temperature rise…
Dr.: Get. Out. Now. Or I will turn you into a half monkey - half giraffe - half
hippopotamus!

NPP: That’s three halves! Dr.: (Menacingly) Oh…I KNOW!

(NPP Leaves. Dr. is utterly despondent.) Dr.: Why? Why must I face constant failure? Everyone is laughing at me! Sam: (Holding a clipboard with papers) You know Sir, I’ve been going over the data… it seems that almost every time you’ve created an evil plan you’ve forgotten something simple - like to carry the one. So… how much was the temperature supposed to drop? Dr.: 50 degrees. Are you saying I misplaced a decimal? I would never commit an error like that! Sam: I completely agree... But, do you remember when you were attempting to make a witch, and instead raised thousands of dollars for the Make-a-Wish Foundation. Dr.: A simple typo. It could happen to anyone! But can you imagine what it would be like if just one of my plans worked! Glorious! They would all be sorry then! Oh, those kids. The ones who laughed at me. And my poor little Pimple of Doom. Sam: They probably don’t even remember that, Sir.

Dr.: Probably not. Those idiots probably think I’m some sort of Boy Scout do gooder, Fools! Sam: Sir, what if, deep down, you don’t really want to be evil? What if you are a Boy Scout do gooder? Dr.: Not be evil!? It’s my life’s work! I’ve got this lair, and I’ve made up all these notecards…Skullcrusher Mountain! Sure, I mean… We could really make some kid's wishes come true with that Nobel Prize money. But no! I’m too old, and it’s too late. Sam: It’s never too late to become who you really are, Sir. Dr.: Ah… you know, kidnapping you was the smartest thing I’ve ever done. Just, uh, just call me Dad from now on. Sam: Okay, Dad. Now what? (He looks at a notecard) Do you still want to build these Dollar Stores? Dr: I’m not evil anymore, right? Sam: No. Dr.: Then no... but one thing’s for sure: we’re gonna have to rename this stupid mountain!

About the authors: Micah Larson competed at the high school level for 6 years. For 5 of those years he was in Creative Expression. He wrote The Dire Disney Dilemma, Segregation of Students, The Fast Food Felony, The Worst Day Ever, and this script, Sports Atheist, with the help of Brian Sams, of course. Brian Sams competed in high school Speech in the 80's, and has been a Speech coach since 1991. He is a business owner, part time actor, and a writer. Awards: A Minnesota State Finalist script
```

---

## IC-1450: Under a Curtain of Stars

- Title: Under a Curtain of Stars
- Author (byline): Matt Mills
- Work: Under a Curtain of Stars
- Publisher: Mushroom Cloud Press
- Publication date as stated: August 1, 2023
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1098
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
“Under a Curtain of Stars”

by Matt Mills

Former astronaut SAM FOWLER, determined but haunted, wanders their study, trying to focus on reality in front of some guests.

Clouds, trees, mountains, oceans… I’m here, I’m home, I’m back on Earth. Breathe in. Smell the ground, the water, the planet at my feet. Feel the weight of it pulling closer. That great, inescapable weight. Focus, focus… no stars—no, no, not the black abyss. Come back. Get back. Trees, birds, bugs, dirt…

Bring me back. So far, I always manage to come back. But just barely. And a little less every time.

How are you sure where you are at any given moment? Have you never had to think about it? When you can no longer trust your senses, what can you trust? I can only seem to find a little trust in the trees. In the dirt. The grime that once was a nuisance becomes like a friend. A familiar reminder of where you are. This way lie the gross delicacies only our Earth could provide. That inevitable nature, usually so uninvited and unwanted, becomes your only solace. Dirt, bugs, smoke, mud…

I left the planet fifteen months ago; my body returned six months after that, but my mind is still trying to land. It can’t help but drift weightlessly, halfway between space and Earth, the border between the two constantly eroding. I… I feel myself floating through the hallways, struggling to clamp down framed photos, losing control of my momentum…

It’s not news to anybody that astronauts need time for their organs to reacclimate when they return from space, bone densities shifting with our corner of the universe. Muscles returning to bear the load of a life on this heavy planet. But my muscles are fine. My bones are as strong as iron. The last organ I need to reacclimate… is my brain. And I don’t know if I can.

The sun shines so coldly I can hardly wake up. I wheeze for breath but it’s somehow too much and too little at the same time. Food’s no better—it’s all either too intense or it may as well be water. I’m never solid; I’m stuck between two stratospheres, clinging to scraps of a life that I may never be able to live again.

I struggle to trust my family. I’m not sure any of us are the same people anymore. I’m not even sure any of us are actually here… I know I touched my partner’s hand when I came home, and I remember it getting colder and colder until it wasn’t there. It faded and so did my trust of the ground I walk on. Now I’m stuck. Stuck nowhere—just me and the two stratospheres trying to make a home out of confusion.

When was the last time you felt truly alone? Truly lost? When was the last time you doubted you’d ever make it back? Did it make you appreciate the familiar things more? Or did you just keep… floating away? Without a tether. I’ve lost mine. I keep floating away and there’s nothing left to pull me back.

Nothing but clouds, trees, mountains, oceans… it’s all supposed to be familiar, but the more used to this place I get, the stranger I feel. I’m not the same person that was invited here years ago. I feel like an intruder. A separate entity crashing a planetary party, still waiting for an invitation. I’m not sure that it’s coming. Stars, stars…

Flowers, mud, oceans… the first time I laid eyes on our planet I couldn’t believe it. She looked so beautiful from up high, a peaceful blue pool beneath our feet, like the Atlantic was made for us to dip our toes in. The sun shines so… unencumbered and free, looking like an unshakable king of our solar system. Every star still distant, but now, so unique and unafraid. It’s daunting. It’s heartbreaking. That beauty so astounding it’s unlike anything you’ve ever felt before or will feel again. And it becomes your new world. It is our world. It was mine. But I have to get back. I need to focus on the flowers, the mud, the oceans…

Dirt, water, trees… the night is the worst part. Stuck in this black shell of a house with nothing to see from the windows but stars? I’m sent right back to that lonely, cold can thousands of miles away from home. Hundreds of miles away from air. From trees, dirt… The isolation consumes me; it needs me; it feeds on me. Morning always finds me half-eaten—searching for grass, birds, sprinklers, gardens… The white-dotted black curtains of my eyelids always present, even when the gold daylight shines through. Stars, black abyss, galactic dust, no gravity, black abyss, black void, black void… Dirt. Dirt, trees, mountains, cl– clou– cl–...

Swirl of confusion comes to a rest and resets.

Why? Why. Why can’t… Why can’t I just… reprogram my brain? It seems so easy. Just commit to saying, ‘This is the sky high above you; the ground is yours to keep.’ Why-why won’t my mind listen to itself? Why do we live in these… these fragile, lifelong traps? I want to think. I want to feel. I want to breathe. I want to take a step without worrying it’ll be my last. I need to know: I’m home; I’m safe. But it doesn’t feel that way. I don’t feel that way. I don’t feel safe. I doubt I ever will. I feel borrowed. I feel stolen. Ripped from the universe—thrown around to never return again. Why can’t I feel okay?! I have degrees in engineering, mathematics… I can’t figure it out. I can’t solve it. I can’t get out. I can’t trust myself. I can’t trust anything. I can’t escape. There’s nowhere for me to go; this is the end. I can’t… I’ve got to… I’ve got… I’ve got to… stars, black void, black void, black void, black void…

They hyperventilate and drop, catching the edge of a couch to stop the fall.

I apologize… I thought today might be a day for progress. But progress doesn’t seem to be on its way. At least not imminently. But. I appreciate you trying to bring me out of this. I guess… Space isn’t done with me yet. It won’t let me go. Please do return, though—maybe by then, the ground will feel more like my home, and not… I… I… clouds, trees, mountains, oceans. Grass, birds, sprinklers, gardens. Dirt, smoke, mud, flowers, clouds, trees…
```

---

## IC-1451: 13 Things You Don’t Know About Swans 

- Title: 13 Things You Don’t Know About Swans 
- Author (byline): by Clyde Hendrickson
- Work: 13 Things You Don’t Know About Swans 
- Publisher: Mushroom Cloud Press
- Publication date as stated: 2006
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2509
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
Thirteen Things You Don’t Know About Swans

Because You’re a Freaking Idiot

Based on Fact Sheet #1245, Nebraska Public School System

Mike Shackleton, Nebraska School System Copy Editor: Do I have to check all these swan facts? Must life continue to squeeze the blood from my soul, drop by drop, wrenching the very shellack of my spirit from its surface like an old man scrapes the plaque from his gums? Mildread, his secretary: My foot surgery is tomorrow. Shackleton: Mildread, you putrid bag of fast food cultural decline, must you plague me constantly with the chafing tang of your mind’s decay? Mildread: I can only answer one question at a time. Shackleton: I bet a swan could understand a rhetorical question if it heard one. Ah! That’s a great start for today’s fact sheet, which is about swans. Swan Fact Narrator: Actually, swans not only understand rhetorical questions, they pose them on a regular basis. Shackleton: Sounds good. We’re off to a great start. I hope the rest of the day goes just as silky smooth. Mildread: That reminds me, I have to go get my foot blisters popped today at noon. Shackleton: Hmm, that is not the sort of swan-like imagery I need today. Try, if you can, to imagine your life not as a pulsating blob of fatty growth, but as a magnificent white creature of the air and sea. With about your same level of intelligence. Mildread: I love the story of the ugly duckling. Shackleton: It’s a little late for you to still be keeping up that charade, isn’t it?

(A knock is heard.) Mildread: I’ll get it. Shackleton: Of course you will. Do you think I’m paid $35,000 a year plus dental, plus 401k, to rise from my seat at the piddliest of rappings? No! For that king’s ransom I am expected to produce the music of the mind – those individual sheets of Xeroxed paper that all the elementary school children of Nebraska use to learn of their world. George Washington facts hang from an apple tree. Giraffe facts are printed on their sides, along the graceful necks. The War of 1812! Well, actually, there are no illustrations on that because we decided seeing the White House in flames was not a good image for 3rd graders. But still! The facts themselves are an image so powerful, a grown man would weep. Mildread: You did weep. Shackleton: Oh yes, my dittoes are beautiful.

(Mildread finally opens the door.) Mildread: Hello?

(Flap Jackson enters.)
Flap Jackson: Hello, I’m Flap Jackson, the regional intern for educational development, and it is great to
meet you.
Mildread: I’m Mildread.
Flap Jackson: That’s just great.
Mildread: I know.
Shackleton: Ignore the sounds emanating from this aged gorgon, my friend, and let me guide you to the
Ithaca of ditto development – my office.
Flap Jackson: I’m the regional intern for education development, and it is great to meet me.
Shackleton: I know it is. Now, sir, let me say bluntly that I need no intern, so I’d like your resignation soon
so we can avoid a public mess.
Flap Jackson: Is this part of the ditto-making process?
Shackleton: You will never be part of that process, Mr. –
Jackson: Jackson.
Shackleton: Mr. Jackson. I –
Jackson: Flap Jackson.
Shackleton: - Think it would be… would be – your name is Flap Jackson?
Jackson: Yes, Mr. Shackleton.
Shackleton: Flap Jackson.
Jackson: Yes?
Shackleton: Quiet down, Flap. Wow. That is the best name ever. There’s no room for an intern here – but
there might be room for a Flap Jackson.
Jackson: I hope so. Because I was ordered to stay here for a whole day.
Shackleton: And that would be awkward otherwise. Alright, take a seat.

(Jackson picks up a seat.)
Jackson: Where shall I take it too?
Shackleton: A bit literal, aren’t we?
Jackson: When you have a name like Flap Jackson…
Shackleton: Right. Sit down. Today we’re developing a new fact sheet – I mean, fun sheet – about swans.
Flap Jackson: I’m ready! Let’s swan!

Shackleton: Hold on, I’m checking my email. (He does this. It takes more than a minute.) Ok, where do
we start?
Jackson: A title.
Shackleton: You’re good. (A silence.) I got nothing.
Jackson: (after thinking) 13 Things you don’t know about swans.
Shackleton: Yes… (As though struck by something important) Wait… wait!
Jackson: Did you think of something?
Shackleton: No, I need to check my email again. (He does this. It takes more than a minute.) Ok, what
else you got.
Jackson: What was on the old fact sheets?
Shackleton: Mildread! The last swan sheet.
Mildread: Here you go… whoops, just spilled your coffee on it.
Shackleton: Clumsy oaf.
Mildread: I know, I was aiming for your crotch.
Shackleton: Read to me, Flapster.
Jackson: Okay…
Narrator: Vital Swan Information for America, Copyright 1942 Department of War. Fact One. Nazis make
swans cry.
Shackleton: Now that’s what I call a fact.
Narrator: Fact Two: Swan girls work hard in the home when the men are away at war, so Daddy will have a
clean house to come home to.
Shackleton: That’s a terrible thing for children to hear!
Jackson: Yeah.
Shackleton: I mean, can you imagine, doing that today – ending a phrase with a preposition.
Jackson: And they had nowhere to turn to….
Shackleton: Do not end that sentence that way.
Jackson: Because it was more than they had bargained for… what they had gotten into… stuff.
Shackleton: Perfect.
Jackson: Can we put some real facts in this? Such as,
Narrator: Swans eat a variety of snails, water insects, small aquatic invertebrates, and fish. They also eat
some forms of aquatic plants.
Shackleton: Too complicated. I have a better idea. (He makes some changes.)
Narrator: Number three. Swans eat water plants, bugs, and stuff.
Jackson: That’s pretty simple.
Shackleton: Alright, some clarification.
Narrator: Number four. Swans don’t eat rocks.
Shackleton: Think the imbecile masses will be capable of processing that?
Jackson: My kid knows not to eat rocks.
Shackleton: Hmmm…
Jackson: He’s at the zoo today.
Shackleton: Awww, well if that isn’t the most useless thing I’ve ever heard.
Jackson: Fact five: Swans eat fish…
Narrator: So sometimes their breath is a little fishy.
Shackleton: I think it should read –
Narrator: Their breath smells fishily
Jackson: No, that doesn’t sound right.
Shackleton: Maybe this –
Narrator: Fishishily their breath –
Shackleton: No,
Narrator: Fishiliciously delicious those fishy fish.
Shackleton: Perfect.
Jackson: Doesn’t make sense at all.
Shackleton: Exactly. Children need to be challenged.
Jackson: Ok, I think I have fact six.
Narrator: Two swans can make a heart if they bend their necks downwards and touch heads.
Shackleton: Yes, let me just rewrite that a bit.
Narrator: Number six. Flap Jackson, my assistant, is the lamest person alive.

(A long silence)

Jackson: Did you know you can make a great horned owl out of a pine cone?

(Shackleton stares at him silently)
Shackleton: Isn’t there a black swan of some sort? A darkened varietal?
Jackson: Colored, you could say.
Shackleton: Jackson, you racist swine –
Jackson: Oh, I’m sorry! I didn’t realize what I –
Shackleton: - That’ll make a great fact!
Narrator: Number seven. There are black swans and there are white swans. This proves that swans are
racist, just like us.
Jackson: I’m not sure that proves anything.
Shackleton: Have you seen Swan Lake? Did you write your masters’ thesis on postmodern interpretations
of the ugly duckling? Did you?
Jackson: I don’t recall doing either of those things, no.
Shackleton: Well neither have I. But a friend once told me that Swan Lake was pretty sweet.
Mildread: Mr. Shackleton, your wife is on line one. Line one for Mr. Shackleton.
Shackleton: Yes, thank you. (to Flap) We only have one line. (into phone) Hello? HELLO? Are you there?
Hello, I can’t – curses.
Jackson: Bad connection?
Shackleton: No, I don’t have a wife. Mildread, you’ve won this round, but we shall clash anon!
Mildread: Not if my Plantar Warts keep flaring up.
Jackson: I’m going to 7-11. Want anything?
Shackleton: I need a new diet coke with lime. (Throwing away one on his desk, half-full) This one is warm.
Jackson: You threw that away? It was half-full - Children are starving in Africa.
Mike: Well put it in a box and send it to them!

(Jackson leaves. Shackleton is by himself.) Shackleton: (singing to himself) Shake shake shake, shake shake shake, shake your booty…. Shake your booty…

(Mildread shakes her booty) Shackleton: I was not talking to you. Mildread: Your fly is open.

Shackleton: Accursed hydra, if your glance falls again on my nether regions, those fertile grapes shall
surely wither on their girthy vine, and I shall be a man no more. (he zips) There… I have removed the
temptation.
Mildread: My eyesight is restored.
Shackleton: What was that, foul and retched urchin?
Mildread: Just glad to be retiring in three months.
Shackleton: Yes, there is a condo waiting for you at the bottom of the vat of French whore rub you apply
each day… you will never have to leave the perfume factory.
Mildread: Your expense reports are late this month.
Shackleton: (suddenly defeated) Guh. I’ll do them tomorrow.

(Jackson returns.)
Shackleton: Think of anything on your walk?
Jackson: Swans are not friendly. Look, but don’t touch!
Shackleton: Ok.
Narrator: Number eight. Swans hate freedom.
Jackson: That’s not the same at all.
Narrator: Number eight. Swans hate Flap Jackson.
Shackleton: What about this?
Narrator: Swans are dangerous animals that can beat you.
Jackson: Maybe we should put a swan-related activity on the sheet. Like, how to draw one.
Shackleton: Here's the activity: we're going to release a swan in the classroom. Whoever doesn’t get eaten
alive, you win a goldfish.
Jackson: Kids are not responsible with goldfish.
Shackleton: Don’t worry about it. The swan will leave no survivors.
Jackson: Wow, how did you ever get so smart?
Shackleton: I used to teach Quantum Literary Theory at Eastwestern Nebraska State.
Jackson: Eastwestern Nebraska? The old E-W! Where was that again – east, or west?
Shackleton: Right in the middle. (He takes a dramatic swig) All got fired when the school was flooded out
by the Mississippi. Remarkable since the Mississippi does not flow through Nebraska.
Jackson: Remarkable.

Shackleton: I’m a remarkable man. Luckily I had good friends, too – and I landed this sweet job with
health insurance and indoor plumbing.
Jackson: Wow, health insurance.
Shackleton: That would help your crippling anal fissures.
Jackson: It sure would. I can only hope to have what you have someday.
Shackleton: You should hope for more (swig) though you won’t get it.

(Jackson gets a phone call)
Jackson: Hi honey, how’s S.D. What? What? (to the office) My kid fell in the swan pit at the zoo. (To the
phone) What’s the situation? 50 to 75? All adults. My God. And they’re – (to the office) They’re circling
for the kill.
Shackleton: Classic swan tactics. I bet they’re flapping and squawking in order to build a cloud of
confusion.
Jackson: The swans are going nuts!
Shackleton: Exactly.
Jackson: This is the end for Little S.D. Jackson.
Shackleton: S.D.?
Jackson: Silver Dollar.
Shackleton: (Stunned, then energized) That’s amazing. What a great name. Alright, alright, we have to
save this kid. Mildread – your assistance, please.
Mildread: Get bent.
Shackleton: Now Flap – can I call you Flap?
Jackson: Absolutely.
Shackleton: Flap, ask the boy where he is.
Jackson: The zoo.
Shackleton: You’re under duress, so I’ll let that slide. I need location IN the zoo, man.
Jackson: Ok – S.D., what are you near? (to Shackleton) The cougars.
Shackleton: No good.
Jackson: The otter pit.
Shackleton: Otters are complete jerkwads. No help.
Jackson: That’s all he saw.
Shackleton: Mildread! The map of the Nebraska Eastwestern Zoo, posthaste.

Mildread: Hold your horses. (She gets it very slowly) There you go. Shackleton: Truly inspiring performance. Let’s see… swans, otters, cougars, african ungulates… wait. African Ungulates. Jackson – are there giraffes. Jackson: S.D., were there giraffes by you? Yes! Shackleton: Ok. We’ve got a chance to get him out. It’s going to take all the luck we’ve got. But I’ve seen the Mississippi flood in Nebraska, and I’ve seen swans eat children alive… anything is possible. All we’ve got to do is hope to dream to dare. Can you do that, Jackson, for S.D. – nay, for all of Nebraska? Jackson: Sweet Christmas Almighty, I sure can. Shackleton: Peaches and cream. Mildread! The giraffe fact sheet from 1984! Ditto number 680B! Quickly now! (Mildread slides over) Curse your bunion encrusted feet, I need that ditto. (Finally she shoves it at him) Yes, yes. I know there’s something in here about calling giraffes to your aid in crisis situations. Item one… Narrator: Número uno. Los giraffes tienen el mismo número de huesos en sus cuellos como hámsteres. Shackleton: What the…? Narrator: Número dos. Parecer de los giraffes árboles. Shackleton: Mildread! How many times must I tell you, keep the spanish ones separate from the english ones. Are you daft, woman? I was preparing you for this day of crisis. Mildread: Usted es una cabeza del poop. Shackleton: I’ll get the file myself – the Nebraskan way. (He throws the cabinet to the ground and randomly pulls out a piece of paper). Groovy Giraffes, 1974. Excellente. Let’s see… (reading.) Yes. Flap, tell your boy to make a sound like an Acacia tree. Jackson: How do you do that?

(Shackleton demonstrates the sound) Jackson: Alright… S.D., make this sound. (he repeats it into the phone. A tense silence follows.) He says there’s a giraffe leaning over the pit. Shackleton: (taking the phone) Grab on, SD! Snatch his big black tongue and hang onto that shaft of deliverance like all Nebraska depends on it! Yes Yes! YES! (to the office) He’s out!

(Everyone cheers. Shackleton pours diet coke over his head.)
Shackleton: My years as a primary education copy editor have all paid off. I’m so happy. (he begins to
weep) I’m just so happy.
Jackson: Well, you’re about to happier.
Shackleton: That’s simply not possible.
Jackson: Oh it is, because you see, Mr. Shackleton, I am not merely an intern from the department of
internal affairs.

Shackleton: You’re not? You liar!
Jackson: No, I am an intern from the department of internal affairs at East-Western Nebraska State.
Shackleton: The Old E-W… it still exists?
Jackson: Yes. I’m afraid after the flood… they were worried about rehiring you. Based on all the
complaints.
Shackleton: Complaints?
Jackson: You once bludgeoned a student with his own fake leg because he made fun of Andrew Jackson?
Shackleton: Someone complained about that? I’ll beat them senseless.
Jackson: That’s in the past. The point is… you’ve been reinstated. Based on your fanatical devotion to
education, as evidenced by your years of service here.
Shackeleton: How marvelous! And Mildread, you played along with this? You helped me?
Mildread: I would like nothing more than to see you move on.
Shackleton: Oh bless you, my sweet tub of transfatty love! (He embraces her.) Mwah. I love you too,
Mildread.
Mildread: (still being embraced) When does he start?
Jackson: Actually, his first class is in 15 minutes.
Mildread: Here’s your lunch, then. Get out of here.
Shackleton: What am I teaching?
Jackson: Advanced Ditto-writing.
Shackleton: Oh, this is so thrilling.
Jackson: I’ve got your University car waiting outside. It’s a jaguar.
Narrator: Jaguars are south american animals with big, scratchy tongues. They can crush your skull with a
single bite.
Shackleton: Just one more thing to do before I go.
Mildread: If you hug me again, I will end you.
Jackson: Make it snappy.
Shackleton: Yep! I just need to check my email.
Narrator: Fact Thirteen: Swans rarely, if ever, make sense. Try not to put too much weight on any stories
you hear about them. Alright, I’m out of here. Anyone got a cigarette? Anyone? Anyone? Geesh. Fact
Fourteen: You people are jerks. And fact fifteen: I am the most awesome narrator ever. Yeah, that’s right.
Put that in your swan and smoke it. Fact Sixteen: Swans will not get you high…. Or will they?
FIN.
```

---

## IC-1452: Beneath the Puppet Stand

- Title: Beneath the Puppet Stand
- Author (byline): Michael Beede
- Work: Beneath the Puppet Stand
- Publisher: Mushroom Cloud Press
- Publication date as stated: 2001
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1228
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
CHARACTER LIST IN ORDER OF

APPEARANCE

Narrator A stodgy British man too interested in the affairs of others

Kermit Kermit the Frog

Oscar Oscar the Grouch, a short green furry creature with an oblong head. Lives in a garbage can

Ernie Ernie of Sesame Street. Short fat man, slightly over-attached to a rubber ducky

Mr. Rodgers Fred Rodgers of Mr. Rodgers Neighborhood. A tall slender elderly gentleman in a cardigan.

Telletubbie: Large purple creature resembling a heroine user

Letter G: A speaking letter G who sounds like a stereotypical gang affiliated Hispanic man

The Count: Transylvanian vampire muppet

Big Bird: An extremely oversized and whiny canarie.

Beneath The Puppet Stand

Narrator: Every morning, day after day, you watched the cute, cuddly, puppets of PBS as they taught you your ABC’s, your 123’s, and how to rhyme. But when the cameras were shut off and credits rolled, felt and yellow feathers flew. Tonight, for the first time in thirty years, the residents of Sesame Street and Mr. Rogers’ Neighborhood reveal what really happened beneath the puppet stand. Kermit the Frog told us daily that “It’s Not Easy Being Green.” If the children only knew why…

Kermit: Kermit the frog here. Everything was just fine. For years Piggy and I were happy as clams in our little world. I should have never let her come to the set. We were all just fine until she decided she wanted to be more than just a muppet; she had to be character on sesame street, too. So I asked Jim Hensen if she could have a shot at being on the team. Two weeks after she gets cast, she tells me that she’s pregnant. I’d been doing shows for 3 year olds for the past twenty years; so I have no idea what pregnancy even is. So, of course it isn’t mine. It was that Oscar the Grouch. He’s the father. I should have known better when he said that he was going to give Piggy a tour of his can. His trash can I mean, not his rump.

It was the ugliest baby I’ve ever seen. You remember that guy Telly? Purple, with yarn or something coming out of his head? That’s him. Oscar obviously couldn’t provide for them-- he lives in trash can for goodness sake! So I raised the kid, and things kept quiet, but that’s where all the tension started.

Narrator: Oscar the Grouch, born Oscar Grouchawitz, died of salmonella poisoning in 1996. Just after what became known as Porkergate however, he said this to Regis and Kathy Lee:

Oscar: Piggy and I have separated due to domestic differences. She lives like a pig! beat Get it? beat No? beat Sorry. beat She and Kermit are now trying to reconcile their differences. Last I heard they went to couples therapy, and have worked it out, for now. She’ll come back to me though… they always do.

Narrator: On the surface, Bert and Ernie looked like television’s happiest duo with… an alternative lifestyle. Sesame Street had never seen two men living together in the same home sharing bed and bathtub alike. But their alternative lifestyle led to a near tragedy that shook the entire Muppet Community.

Ernie: Yeah, Bert and I were pretty good friends. We had our differences though. He wanted soap suds. I wanted bubble bath. He kept saying, “Oh Ernie. Oh Ernie.” I didn’t hear him say, “Oh Ernie” as I shoved him in the trunk of a car I drove off a bridge. But, he survived and the show went on because it’s all about the kids. After that, I didn’t hear anymore comments about my rubber ducky being too small or blowing too many bubbles. It’s just brother stuff you know.

Narrator: But we always thought that… you know…

Ernie: You thought that I was… and that… NO! I’m straight! Not that there is anything wrong with that, but… No!

Narrator: Ernie was acquitted of charges of attempted murder, public lewdness, and eating crackers in bed. two beats Mr. Rogers was the beloved puppeteer who made his way into every child’s home. But did he make his way… elsewhere? This is his last known recording.

Mr. Rogers: Hey kids, who wants to be my neighbor? (taking off shirt) Can anyone point out to me where little boys and girls aren’t supposed to touch grown ups? That’s right. Oooooh, that’s right. That’s so right. Go see King Friday! He’s waiting for you in the Kingdom of Make-Believe.

Narrator: The “Beneath the Puppet Stand” producers thought it’d be inappropriate to over hype the addictions of the Telletubbies’ cast members, so you can just see for yourself. Our lawyers will only allow us to show you this clip from a recent episode.

Telletubbie: (Slapping arm with two fingers, shoots heroin) Bye bye. Bye bye.

Narrator: The Letter G. In his own words.

Letter G: Yo watup! Since the show, everyone comes up to me, “Watup up, G? Wats going down, G? I’m your G-dog! G? G?!” My name is Geraldo! This show is bull, man! Beneath the puppet stand? Beneath the puppet stand, why not G-neath the puppet stand? I get stuck with gangster rap crap, meanwhile Kermit is starring in Muppet movies? I’ve got a story for you. So one day I was rolling down the street with my nine. You know, number nine. This vato comes up to us man, he’s like, “Hey, watup, G? Watup up, Nine?” Nine just got pissed, and the vato says to us, “Hey man, it should be K-9.” Nine flips out and pulls out a nine…millimeter, he pulls out a nine millimeter and he shot the guy. Nine got sent upstate, for nine years. Irony, no? Now we can’t use him on the show. Who are they going to replace him with? Eight? Eight is a pansy! So they brought in 11, man. A double digit. A dirty little double digit. But the show went on. For the kids, man. It’s all about the kids.

Narrator: Big Bird, the centerpiece of Sesame Street. His struggle with LSD may have been the most tragic fall and triumphant redemption of anyone in the entire neighborhood. By the time that Big Bird’s imaginary friend, Snuffleupagus, began to manifest himself on the show, the producers knew that he had hit rock bottom. The count tells his story.

The Count: I used to deal to the Bird, ah ah ah. Three, three hits of acid, ah ah ah. He used to wake up in dumpster at four, four in the morning, ah ah ah.

Narrator: We will allow big bird to defend himself.

Big Bird: Day in, day out, I did the same stupid show about the same twenty-six letters and ten numbers for twenty years. OK! OK! I took the drugs! If I didn’t I would just go off the deep end. Nobody, muppet or otherwise, can stay that happy all the time without some sort of chemical assistance. I’m a good person, I didn’t want to do drugs, but without them I never could have done that show, but the education of America’s youth was worth much more than my own health, my social life, or even my sanity. This confession was brought to you by the letters G, C, and D, and I’m giving a shout out to number nine, you’ll be out soon.
```

---

## IC-1453: Calvin Coolidge The Dinosaurs Vs. Copyright 2005 by Clyde Hendrickson.

- Title: Calvin Coolidge The Dinosaurs Vs. Copyright 2005 by Clyde Hendrickson.
- Author (byline): Not specified
- Work: Calvin Coolidge The Dinosaurs Vs. Copyright 2005 by Clyde Hendrickson.
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: RONALD, ELVOR
- Teaser before the introduction: No
- Spoken words (computed): 4453
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
Characters.
SIMON. A mad scientist.
ELVOR. Simon’s one-armed, hunchbacked assistant
RONALD. An alcoholic, washed-up general.
BOOBY. A brown noser.
CALVIN COOLIDGE. President of the U.S. Very stoic.
BILL CLINTON. Good ol’ boy.
RAPTOR TIM. A preppy, elitist snob. Also a dinosaur.
REXINA. A very feminine T-Rex.
VARIOUS OTHER DINOSAURS.
SOME OTHER PEOPLE.

Places. The 1920’s and the prehistoric past.

Calvin Coolidge vs. The Dinosaurs

SIMON. Elvor, fetch me a beaker of spleen juice, will you?
ELVOR. No! I won’t do it master, it’s not right!
SIMON. Not this again. Look, I’m a mad scientist. I have a different set of morals than you.
ELVOR. Elvor not care! What master do is evil.
SIMON. Let me spell it out. I bring the dead back to life. I build zombie hamsters out of puppy parts. I
clone electric eels just to drop them in the neigbors’ koi pond. I listen to Mandy Moore. And I do that sort
of crazy, messed up crap because I’m a Mad Scientist. It’s my job.
ELVOR. Then why you no make Elvor dream come true?
SIMON. Nothing would justify removing your head from your neck and attaching it to your hips. I have
limits.
ELVOR. It would be so cool!
SIMON. Yeah, until the first time you had an itch and you poked your eye out.
ELVOR. Elvor no itch. Elvor use gold bond.
SIMON. Thank you for updating us all on your personal hygeine. Besides, I replaced your Gold Bond
with powdered sugar a long time ago.
ELVOR. That why birds no leave Elvor alone.
SIMON. Is that why there’s a pelican in your shoe?
ELVOR. (pulls out pelican) He Elvor’s first friend.
SIMON. Aww, Elvor, I’m sorry.
ELVOR. Me too.
SIMON. Sorry that you’re a retchid mound of ooze that kills through sheer hideousness.
ELVOR. (sobs)
SIMON. (sighs) I’m not going to get my spleen juice now, am I?
ELVOR. Not until Elvor feel special again.
SIMON. How do we make Elvor feel special again?
ELVOR. You know how.
SIMON. No, really, I don’t – wait, Elvor, no…
ELVOR. Acid fight!

SIMON. Elvor, come on, I only like acid fights when they’re between orphans. And I can bet money on it. ELVOR. If your face ain’t smokin, then you’re not having fun! Acid! (he throws it onto Simon) SIMON. I just washed this cape! And it was my most mysterious one… ELVOR. Never put acid in your eye! (throws more) SIMON. Ow! Oooh, hey, actually that feels kinda cool. All tingly and stuff.

(simon thinks, then takes the beaker and pours some in his pants. He looks pleased and shakes his head at
the audience while smiling.)
ELVOR. Now Elvor try!
SIMON. Uh…

(knock on door)
SIMON. Elvor, get the door.
ELVOR. Yes, mistress.
SIMON. Whatever.

(The door opens. Ronald stands there, looking serious.)
RONALD. Hello, I’m General Ronald –
ELVOR. McDonald?! (He leeps and grabs on to the general’s arm, trying to eat him.)
RONALD. (stares at Elvor for a moment) Is this thing contagious?
SIMON. You’ll want to wash your hands afterwards. The goo sometimes leaves a rash.
RONALD. I assume you’re Doctor Tonguewart.
SIMON. Yes. Number one on the angry mob charts for two years running.
RONALD. Dr. Simon Tonguewart, I am hereby commanded to appoint you to be the Secretary of Defense
of the United States of America.
SIMON. Ok. (silence. Elvor keeps trying to eat general) Why?
RONALD. It’s what the president wants.
SIMON. President Coolidge?
RONALD. No, President Van Buren. Of course President Coolidge.
ELVOR. You no secretary! President must be crazy!
SIMON. Now Elvor, I’m sure the president has a very good reason for appointing me secretary of War.
RONALD. No, actually, he’s just a retard.

SIMON. Oh.
RONALD. Well, come on, let’s get this pathetic goober circus on the road. Are you bringing that? (He
points to Elvor.)
ELVOR. (looks at pants) Yes, it’s best part of Elvor.
SIMON. He goes where I goes.
ELVOR. Not true. Elvor sometimes go other place. Elvor go on tree, Elvor go in pool, Elvor go all over
neighbor’s koi pond.
RONALD. Right, whatever. Let’s get out of here.
ELVOR. Do you have… hemorroid cream? Long journey chafe Elvor.
RONALD. I really hate my life.
SIMON. To the white house! We’ll take my teleporter.
RONALD. I don’t believe in witchcraft.
SIMON. You don’t believe in SHUT UP. Teleporter on!

(They teleport with cheesy sound effects the White House.)
ELVOR. Oooh, Fancy. This place must have real toilets.
SIMON. We have real toilets, Elvor.
ELVOR. We do? Elvor never find.
SIMON. That explains the stain on that ottoman.
RONALD. Please wait here. President Coolidge will be in shortly.
SIMON. Aren’t you staying?
RONALD. No, I’m way too drunk for that.

(he leaves. HFB man walks in.) HFB man: Historic Fact Break! President Calvin Coolidge was the last of the Eldar, the earliest race of middle earth. After freeing the slaves, he transformed into Batman and liberated several other minorities, who’s names I can’t recall because the all later were killed when Superman (he’s elbowed in the chest by Booby) BOOBY. We have an intruder in the President’s office, over. (pause) Yes, it’s him again, the historian. (pause) Bring me the enema gun. HFB Man: Oh god, not the enema gun again. SIMON. Uh, Mr. President? CALVIN COOLIDGE. Are you talking tome?

SIMON. I think so.
CALVIN COOLIDGE. That’s good, because I’m the president. How are you, Gentlemen.
SIMON. Good.
ELVOR. Horny.
CALVIN COOLIDGE. Good.
BOOBY. *Ahem*
CALVIN COOLIDGE. Who are you?
BOOBY. Undersecretary for the secretary of the development of the secretary’s undersecretary, John B.
Booby.
ELVOR. Booby! (he reaches for them)
CALVIN COOLIDGE. Why are you here, Booby?
BOOBY. Mr. President, I’ve been working on this plan with you for months. Dr. Tonguewart, it’s nice to
finally meet you. The President and I have been developing an executive course of action over the last few
weeks, and -
CALVIN COOLIDGE. I thought I’d been in a typhoid coma since late last year.
BOOBY. No, sir, you’ve been President. Yesterday you invaded Cuba.
CALVIN COOLIDGE. Did you find my watch?
BOOBY. Sir?
CALVIN COOLIDGE. My watch, Booby. That was left in Cuba.
BOOBY. No, sir, you’ve never been to Cuba.
CALVIN COOLIDGE. Then how could I leave my watch there?
BOOBY. Sir, you’re the commander in chief.
CALVIN COOLIDGE. I see. (To simon) Have you found my watch?
SIMON. Can’t say that I have.
CALVIN COOLIDGE. I’m sorry to hear that. Thank you for coming.
SIMON. Ok… can we leave?
BOOBY. No! Mr. President, don’t you remember the threat? The plan?
CALVIN COOLIDGE. You’ll have to remind me. I’m recovering from a typhoid coma. My memory’s
not what it used to be.
SIMON. That disease is contagious.

BOOBY. No one has typhoid. No one’s getting typhoid. We have a much graver threat at hand. CALVIN COOLIDGE. Well, spit it out man. I’m the President, I need to hear these things. BOOBY. We have evidence that the dinosaurs are in possession of weapons of mass destruction. SIMON. Really? BOOBY. Well, no. They have the materials with which to prepare preparation for the consideration of building facilities with which they could construct weapons of mass destruction. SIMON. Ah. Practically the same thing. BOOBY. Exactly. SIMON. So, what would you like us to do? BOOBY. You’re essential to our proactive disarmament strategy. Mr. President, would you like to take over the briefing from here? CALVIN COOLIDGE. Ok.

(Silence.)
BOOBY. Sir?
CALVIN COOLIDGE. I like puppies.
BOOBY. Moving on.
CALVIN COOLIDGE. Dead puppies.
ELVOR. That Elvor’s favorite puppy too!
CALVIN COOLIDGE. Good. Booby, these men will do.
BOOBY. Thank you sir. Gentlemen, we need to confront the dinosaurs head on. We must invade the
prehistoric earth! Something only you could arrange for us, doctor.
SIMON. You don’t mean….
BOOBY. I do. A timewarp device.
SIMON. A timewarp device? That’s ridiculous. What do you think I am? I’m a mad scientist, not some
crazy wacko like Einstein or Oprah.
BOOBY. So… you can’t build us a time machine.
SIMON. Oh. Oh no, I said I don’t have a time warp device. I do have a time machine. It’s right here.

(He activates it) BOOBY. It didn’t work. We’re still in the oval office. SIMON. Yes, but we’re in the oval office… of the future!

ELVOR. You sure this future?
SIMON. Completely.
ELVOR. (sighs) I thought Elvor other arm would grow back in future…
BILL CLINTON. Mornin’ kids. You just time travel in?
BOOBY. Yes… Mr. President?
BILL CLINTON. I know, I can’t believe it either! Want some jerky?
SIMON. No thank you.
ELVOR. Is it kitten jerky? Elvor like that.
BILL CLINTON. (chuckles) Hey there, lil’ Feller. What can I do ya for?
ELVOR. You have dead kitten? Elvor hungry.
BILL CLINTON. No, but I got some hookers ‘round back.
ELVOR. Dead hookers?
BILL CLINTON. Nope, only live ones.
SIMON. No dead hookers? I guess you’re not a Republican.
BILL CLINTON. Well this visit has been delightful, boys, but I gotta go feed the doggies. Can I offer you
a souvenir? Maybe a sno-globe?
SIMON. I’d like a Lollipop.
BILL CLINTON. I love a good sucker! Here’s a grape one.
ELVOR. Bye bye, smelly man.
BILL CLINTON. See ya later, lil’ feller.
SIMON. Time warp, activate! (They arrive back in the past)
BOOBY. I thought it wasn’t a timewarp machine.
SIMON. Actually, it’s a shut up machine. But it’s apparently broken.
CALVIN COOLIDGE. Ah, puppies.
BOOBY. President Coolidge, Sir, the test was successful. We can invade… I mean, confront the
dinosaurs, just as we wanted.
CALVIN COOLIDGE. Dinosaurs, eh?
BOOBY. Yes, sir.
CALVIN COOLIDGE. Not puppies?

BOOBY. No, sir. There are no puppies. CALVIN COOLIDGE. I must sit here and think. Make small talk. BOOBY. Uh…

(they fidget for a while)
SIMON. So, Mr. Booby, did you always want to be undersecretary… of… the vice developed… of
under… down under… with the… guy and the underpants… whatever it is you do now.
BOOBY. It was high on my list of career options, yes, although I – well, can I trust you with a secret?
SIMON. Definitely not.
BOOBY. I always aspired to be a topless dancer. A showgirl! I think if you can be a stripper, then you
can do anything!
SIMON. Your notions frighten and disturb me, which in turn arouses me. Perhaps you are on the right
track, Booby.
ELVOR. Booby track!
SIMON. What?
CALVIN COOLIDGE. Excellent, I’ll have mine with mayo.
BOOBY. Enough of this. We’re ready to go, sir. Mr. President, say the word.
CALVIN COOLIDGE. Puppies.
SIMON. Good enough for me! (He activates the machine.)

(The atmosphere changes. Mugginess, swamp sounds, trees. They have arrived in the past. Elvor’s stump
has switched arms, but he only notices the regrown one)
ELVOR. I am cured! Elvor’s arm come back!
BOOBY. Not really. It looks like your stump just switched sides.
ELVOR. (sarcastically) Oh. Thanks for pointing that out, Mr. Boobypants. Now Elvor even happier.
SIMON. What do we do now?
BOOBY. You’re the mad scientist. You tell me.
SIMON. I generally just mutate things. Like orchids, or orphans.
BOOBY. Well, it could look like anything… like… that rock. Oh my god! That rock!
SIMON. What about it?
BOOBY. It might be a bomb!
SIMON. Doubtful.

ELVOR. Here dino dino dino…
SIMON. Good, Elvor. Great initiative in the “getting us all slaughtered immediately” department.
BOOBY. We need to find the dinosaurs, though. As much as that makes me sweat.
SIMON. I have a feeling we won’t have to.
BOOBY. What do you mean, doctor?
SIMON. Do you see this? Beer cans. Kid Rock CDs.
BOOBY. What does it mean?
ELVOR. Dinosaurs trashy like neighbors in trailer?
SIMON. No. See this? Plaid Dinosaur pants. It means… they’re hunting us.
BOOBY. Oh god… Oh my god… I can feel one’s breath right now! He’s next to me!
ELVOR. Ah!!!!
BOOBY. Ahh!!!
ELVOR. Oh, no, that was just Elvor being friendly.
BOOBY. By breathing in my ear?
ELVOR. Ear full of delicious wax!
SIMON. Elvor! Down!
ELVOR. But…
SIMON. No wax before dinner.
ELVOR. Awww…
BOOBY. Don’t do that again.
ELVOR. Elvor not need too. Real dinosaur over there.

(Tricera’s head appears, then disappears)
BOOBY. Augh! It’s a raptor, I know it. They’re moving in for the kill strategically. It’s just like that
movie!
SIMON. What movie?
BOOBY. You know, Citizen Kane.
SIMON. The dinosaurs in that scared the crap out of me too.
TRICERA. (roars)
BOOBY. Don’t eat me! I have warts!

ELVOR. Mmmmm, hairy ones?
TRICERA. I’m a velociraptor! Look at me! I’m a raptor! Roar! I’m smart and I talk! Roar! Raptor! Yeah
Go Raptors!
SIMON. Wait, you’re not a raptor.
TRICERA. Yes I am. I’m a raptor. A great one. Evil and cunning. Working in groups. Shut up. I hate
you.
SIMON. You’re a triceratops.
TRICERA. Yes, ok? There are no velociraptors. Some annoying pansy director made them up because
the rest of us JUST WERENT GOOD ENOUGH for him, were we? Three horns to gore you? No, better
make them SMART too. What a cocky bastard. Anyway, we didn’t want to disappoint guests from the
future… so here I am. Roar. Watch as I devour you… with my brains.
SIMON. Why do you care about disappointing us? You could just gore the lot of us.
BOOBY. Shhhh…. Maybe he’s forgotten!
TRICERA. Yes, it’s really easy to forget horns when they’re constantly getting stuck in trees all day.
Anyway, we need the future to have a good impression of us. Otherwise, it hurts book sales.
BOOBY. You care about book sales?
TRICERA. Most of us live off of the photo royalties.
SIMON. I didn’t know your society was so advanced.
TRICERA. Meh. Just because we’re rich doesn’t mean we’re smart.
BOOBY. So are you going to eat us?
TRICERA. No, I’m a vegan.
ELVOR. Elvor is virgin too!
TRICERA. I’m sure the T-Rex behind you will fulfill all your devouring needs.
REXINA. Roarrrrr!
BOOBY. The secretary’s undersecretary has wet his pants, sir.
ELVOR. Oooh, now pants delicious.
REXINA. You all are so cute, I could just gobble you up!
BOOBY. Don’t eat me! I’m having an identity crisis and I never got to take pole-dancing lessons.
REXINA. Pole-dancing? You don’t say! Let’s see it.
BOOBY. W…what?
SIMON. You have got to be joking.

BOOBY. No, no, I’m not ready.
REXINA. Ok, well then, get ready to be digested! Finally, some low-carb snacks that taste good!
SIMON. (sigh) Booby… I never thought I’d say this to anyone, but you’re going to need to pole-dance to
save our lives.
ELVOR. You say that to Elvor before.
SIMON. I’ve never said it sober.
ELVOR. Elvor feel used.
BOOBY. I’m not sure. I’ve never tried it since I was a little girl – I mean boy. In my mom’s closet. She
had this leather corset. And these spiked collars. And I put them on and I felt free, in a new world. I was
just ready, I could take on anything. Evil, Hatred, or a bar full of sweaty firefighters. I could beat
anything.
SIMON. Even a strangely aroused tyranosaurus rex?
BOOBY. Anything. (He looks at the Dinosaur, then to Elvor) Hit it, freak boy.
ELVOR. One block rockin’ beat, comin’ up! (He beat boxes.)

(Simon pole dances for Rexina, who is impressed.)
REXINA. Well, that got me all hot n’ bothered. I have to eat something more substantial now. Maybe
some ribs. Skedaddle, you little goblins.
RAPTOR TIM. (on his cellphone) Oh yeah, I was hooking up with this stegasaurus chick the other day…
Man she had the biggest plate armor ever!
REXINA. Oh no! The raptors!
BOOBY. What should we do?
REXINA. You’re basically dead. See ya! (She leaves.)
BOOBY. Well, are we going to die?
RAPTOR TIM. Oooh, fresh meat. Get in my belly! Ahahahahah I am so funny!
ELVOR. This dinosaur annoying.
BOOBY. I thought there weren’t supposed to be any real raptors?
SIMON. It’s a dinosaur story. People don’t care about continuity.
BOOBY. Maybe…
SIMON. So, Mr. Dinosaur. How do we know you’re a Raptor?
RAPTOR TIM. Cause my collar’s flipped up! I must be the most awesome dinosaur ever!

BOOBY. Oh my god, he is so hot. Can I hook up with you in your nest?
SIMON. Booby! Stop being a tramp. He’s probably got diseases.
RAPTOR TIM. You know it! Who brought the keg?
SIMON. There’s no keg.
RAPTOR TIM. (suddenly changing moods) No Keg, eh?
SIMON. I’m sorry.
RAPTOR TIM. (snarling and tapping talons) Not as sorry as you’re about to be, geek.
ELVOR. Here, look!
RAPTOR TIM. (snorts flask) Tequila! You’re lucky, nostradamus.
SIMON. Nostradamus?
RAPTOR TIM. Wasn’t he the hunchback of notre dame?
SIMON. You’re an english major, aren’t you?
RAPTOR TIM. I am so wasted! Let’s go watch the O.C. Because that is so like my life.
SIMON. The O.C. is so last year. Or, in this case, that is so 64 million years in the future.
RAPTOR TIM. What was that? (a dozen or so raptor heads appear from the bushes, threatening.)
SIMON. Nothing.
RAPTOR TIM. Well. It looks like we’re at an impass.
SIMON. We are?
RAPTOR TIM. I want to eat you, and I assume you don’t want to be eaten.
BOOBY. No, I’m quite bitter.
RAPTOR TIM. We’ll settle this the old fashioned dinosaur way, then?
SIMON. And how is that? A mauling? Disembowling?
BOOBY. A dangly-parts severing?
RAPTOR TIM. Not quite, it’s
RYAN. Hello I’m Ryan Seacretaceous, and welcome to Dinosaur Idol!
BOOBY. I’ve always wanted to be on this show!
RYAN. Who will be participating from your group?
SIMON. I only know Mandy Moore songs.

RYAN. So definitely not you! Who else?
BOOBY. Can I strip?
RYAN. Absolutely not.
ELVOR. Elvor do it… he sing in college Glee Club.
RYAN. Great. Now, let’s get things fired up with our first contestant. He’s a stylish competitor from the
heart of the jungle – and the girls love him for his big brain! Please welcome Raptor Tim!
RAPTOR TIM. (sings some annoying song)
RYAN. Judges, what do you think. Simon?
SIMON THE JUDGE. Not bad, but why is your collar flipped up? Honestly, you look like a total tool.
PAULA. And simon knows tools!
RYAN. Oh, Paula! What did you think?
PAULA. You showed a lot of courage, Tim, and your voice has really improved. Great job!
RYAN. And our last judge, the blood thirsty Allosaurus?
ALLOSAURUS. Raaaaaarrrr!
RYAN. Not bad, Tim. We’ll see if you “collared” the other contestants! They don’t even write this stuff
folks, I’m just that funny. Now, our next competitor hails from the inner city. He’s a public television
performer looking for a basic cable break! Let’s give him a nice round of applause.
BARNEY. I love you, you love me, we’re a happy family with a great big hug.
SIMON THE JUDGE. I’ve heard enough. You are absolutely the most horrible singer ever. Did you
swallow a bag of phlegm before you came?
PAULA. Yeah, I thought he sucked too.
ALLOSAURUS. RAAAAAARRR (He bites off Barney’s head.)
RYAN. Oh! Come on guys, don’t bite his head off. And now, for our final contestant, Elvor!
ELVOR. I… not sing… much good. … yeah.
RYAN. Hit it, boys!

(The Music starts. Elvor proceeds with a perfect rendition of “I wanna dance with somebody” by Whitney Houston.) SIMON. America needs more humped stars. You remind me of a young Justin Timberlake, but with less drool. PAULA. You have a big heart and a beautiful voice, I really hear how much you love this song. Great job! RYAN. Two for two. But what do you say, bloodthirsty allosaurus?

ALLOSAURUS. (perfectly eloquent) It was mediocre, but I’d let him through to the next round.
PAULA. You can talk?
ALLOSAURUS. RAAAARRRR (He bites off her head.)
RYAN. Oh you two, get along! That does it for this edition of Dinosaur Idol. Seacretacious, out!

(They leave. Raptor Tim stares dejectedly.)
SIMON. Well ?
RAPTOR TIM. Whatever, dude. I’m gonna go race poor people in my BMW. Peace out.
SIMON. I never thought dinosaurs could be as annoying as humans. I’m glad I didn’t take that job as an
evil paleontology professor at Brown.
ELVOR. We go. Elvor hungry, but no kittens to eat.
SIMON. I concur. Let me turn this on. (He gets out the time machine.)
BOOBY. No! We can’t go yet.
SIMON. We’ve determined the dinosaurs to be as insecure as college freshmen. They couldn’t win a
trout fight with a haddock. I think the threat has evaporated.
BOOBY. Yes, the threat for me. But the threat to you has grown to prehistoric proportions, Tonguewart.
SIMON. What an ominous thing to say!
BOOBY. The only way you’re getting back to the future
HFB Man: The phrase back to the future is copyright steven speilburg. It is used without permission. If
product gets in eye, flush them immediately.
BOOBY. The only way you’ll return to the present is as a fossil. Haha!
SIMON. What are you saying?
BOOBY. I am actually Sleezius Booby, your archnemesis from your days in the Malevolent Chemistry
department at Yale!
SIMON. I suppose I should have realized that, since you look like, act like, and have the same name as
Booby. You even has his painfully obvious inflamed neck glands.
BOOBY. Those are hickies! I got them scoring with twenty chicks last night.
SIMON. That was always your explanation, Booby. It might have seemed plausible back at Yale, which
has plenty of drunken floozies, but now it’s just ridiculous.
BOOBY. Well your neck glands are inflamed too.
SIMON. No, that’s an oversized jurassic leech. (He pulls it off.) See?
BOOBY. You always had to act like you were better than me.

SIMON. Let’s play a game. It’s called: catch the giant prehistoric leech with your face! (he hurls a huge leech at Booby, and it latches on to his face) Dr. BOOBY. Ahhh! It burns! Ouch, ow! Although, it’s doing wonder for my pores. Oh God, the pain, the pain! (rips it off, face is somewhat disfigured) I’m ruined. How can I ever dance topless now? SIMON. Alone in your jail cell? Dr. BOOBY. You poppycock! I can’t believe I was thinking of asking you out instead of killing you. SIMON. I can’t believe it either. Dr. BOOBY. Looks like you won this time. SIMON. Yes… just like last time, when I thwarted your attempt to clone the biology professors at Yale and have them fight to the death in a ring full of jello. Dr. BOOBY. But there’s one difference, this time. SIMON. This time you’re wearing pants? Dr. BOOBY. NO! Well, yes. Whatever. The difference is… this time… I have your time machine. ELVOR. Ohhh, now we in some deep shi-

(Booby actives timewarp device, cutting him off. They reappear in the same place, next to their clones from
five minutes ago. The only difference is that the old Booby has not yet revealed himself and been
disfigured. The older Elvor has his stump on the opposite side, as well.)
ELVOR FUTURE. Hey, nice stump.
ELVOR PAST. Thanks.
SIMON PAST. Oh my god.
SIMON FUTURE. Oh my god.
SIMON PAST. Do I really…
SIMON FUTURE. Did I really…
SIMON PAST. Look so fat in the future?
SIMON FUTURE. Look so fat in past?
BOOBY FUTURE. Yes, we’re all quite fat. But now…. wow, am I this smokin’ hot in the future, too?
BOOBY PAST. Of course you are, you handsome devil.
ELVOR PAST. Oooh, Elvor itch. But Elvor can’t scratch, until now!
ELVOR FUTURE. You scratch Elvor too?
ELVOR PAST. Oooh.

(They scratch each other’s backs and moan in ecstasy.)
SIMON FUTURE. What on earth was the purpose of bringing us back five minutes in time?
BOOBY PAST. Now, you see, there’s two of us!
BOOBY FUTURE. We’re almost too beautiful. It should be a sin.
SIMON PAST. Uh, there’s two of us now, too.
SIMON FUTURE. Yeah, and now Simon Past has the time machine.
BOOBY FUTURE. I have one too!
SIMON PAST. But you don’t know how to use it!
BOOBY FUTURE. Besides, now I have four arms, instead of two!
SIMON FUTURE. …And we have eight.
ELVOR PAST. Six.
SIMON FUTURE. Close enough.
SIMON PAST. Face it, Booby. You screwed up. You didn’t want to end up here.
BOOBY FUTURE. Alright, I admit it. I was trying to warp you into an active volcano.
SIMON PAST. Well, you’ll have plenty of time to practice. I’m taking Elvor and I back to the oval
office. (He fiddle with machine.)
BOOBY FUTURE. Oh really… well, I have one thing to say about that.
SIMON PAST. What’s that?
BOOBY FUTURE. Catch! (He throws the time machine at Simon, who bobbles the one he is holding and
drops it. Booby Past catches Simon’s machine. Simon himself is left holding the Boobies’ device.)
BOOBY PAST. Now we’ll be back in the oval office.
SIMON PAST. You sure will!
SIMON FUTURE. Oh no! Get them! (Simon Past restrains him.)
BOOBY FUTURE. Enjoy the leeches, gentlemen! (They warp.)
SIMON FUTURE. Why did you let them get away?
SIMON PAST. I figured they’d try and steal my time warp device, so I set it to the year 3000. I hope they
enjoy doing strip teases for robots.
SIMON FUTURE. You clever girl!
SIMON PAST. Hey, I know an evil scheme when I see one.

SIMON FUTURE. We must leave you now, past selves. But don’t worry. In five minutes you’ll be back
here again.
SIMON PAST. I look forward to meeting you again.
SIMON FUTURE. For the first time.
SIMON PAST. Indeed.
ELVOR PAST. I want to give you gift, other-armed brother
ELVOR FUTURE. You always know my soft spot.
ELVOR PAST. It very hard to miss. But there’s something I won’t need anymore…
ELVOR FUTURE. What that?
ELVOR PAST. Take my arm.
ELVOR FUTURE. You mean it?
ELVOR PAST. Now, you have arm, where before there was only stump.
ELVOR FUTURE. Oh, Elvor so happy! (He takes arm and attaches it to crotch.)
ELVOR PAST. Elvors happy!
SIMON. Let’s go, happypants. (He activates the warp)
ELVOR FUTURE. It have new meaning now… (time warp finishes. all is restored. they are sitting in
the president’s office.)
CALVIN COOLIDGE. Gentlemen, welcome back. Where’s my sandwich?
SIMON. Uh… they were out of sandwiches. But we did disarm the dinosaurs.
CALVIN COOLIDGE. And the pathetic stripper tag-along? Where’s he?
SIMON. Calculating pole dances for cruel mechanical masters.
CALVIN COOLIDGE. Splendid. That’s just what I intended.
SIMON. What do you mean? You wanted to get rid of Booby?
CALVIN COOLIDGE. Definitely. That’s why I developed this whole fake “WMD” threat.
SIMON. Why did you send us back in time to do it?
CALVIN COOLIDGE. I sent you somewhere?
SIMON. To the past. To fight dinosaurs.
CALVIN COOLIDGE. Oh, yes. Did you find my watch?
SIMON. No.

CALVIN COOLIDGE. Are you sure, I left it there.
SIMON. No offense, Cap’n, but how could you leave your watch 65 million years in the past?
CALVIN COOLIDGE. At my girlfriend’s house.
SIMON. Your girlfriend is 65 million years old?
CALVIN COOLIDGE. Meet my wife, Rexina.
REXINA. Mwah! Good morning, Mr. President! Oh I just love saying that.
CALVIN COOLIDGE. I am very deeply moved.
SIMON. This doesn’t look like love to me.
ELVOR. What is love?

(Rexina takes a bite out of Pres. Coolidge)
CALVIN COOLIDGE. Baby don’t hurt me, no more.
REXINA. Sorry.
CALVIN COOLIDGE. Gentlemen, the mystery is solved. The weapon of mass destruction… is love.
SIMON. Oh God, no.
CALVIN COOLIDGE. It has broken down barriers, melted my heart, and brought me back my watch.
And this is a damn fine watch.
SIMON. I cannot believe I was involved with such a non-evil enterprise.
ELVOR. Elvor think it sweet. Elvor going to cry.
REXINA. Here, have a tissue.
ELVOR. (taking giant tissue) Thanks!
SIMON. I need some cheering up. I’m going back to my lab to clone Martha Stewart so I can feed her to a
giant, mutated clone of Oprah.
ELVOR. Ooh, Elvor having koi for dinner.

(Ronald stumbles in, drunkenly.)
RONALD: Do you guys have any grain alcohol?
ELVOR: Smelly man! Why you so extra-smelly?
RONALD. I've been fired.
SIMON. For drinking on the job?
RONALD. Apparently, I used the entire first armored division to invade an orphanage.

SIMON. What’s wrong with that?
RONALD. It was an orphanage for crippled deaf-mutes.
SIMON. I'm sorry I missed that.
RONALD. They tried to raise the white flag... but they didn't have any arms.
ELVOR. Elvor feel their pain.
RONALD. I may need a place to sleep tonight.
ELVOR. Awwww... Elvor give you his bed.
SIMON. Elvor, Just because you sleep in that ditch doesn't mean it's yours.
RONALD. That’s ok. I think I’ll just pass out here. (He does so.)
SIMON. (sighs) I guess there’s only one worse way this could have ended…
REXINA. Don’t say it!
RAPTOR TIM. Pop the collars, yo! That is hot!
CALVIN COOLIDGE. You lose. (Cocks shotgun, blows away Raptor Tim)
RAPTOR TIM. Bury me…. in a polo shirt….
CALVIN COOLIDGE. Oh yeah! Can you smell what the Coolidge is cookin’?

(There is a silence. Elvor creeps over to Tim’s corpse.) ELVOR. Anybody going to eat that?

The end.
```

---

## IC-1454: CAMP Copyright 2006 by Frank Joseph.

- Title: CAMP Copyright 2006 by Frank Joseph.
- Author (byline): Frank Joseph
- Work: CAMP Copyright 2006 by Frank Joseph.
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2026
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
Characters
Timmy- main character, a perky Boy Scout
Father- Tim’s dad, thinks he is a Nazi, has hand up to face as if a mustache
Tony- Camp Director
John- Tim’s “mentor”, another camp staffer
Deon- staff member, a “gangsta” Boy Scout
Adam- staff member, a gay Boy Scout
Ron- staff member, a blind Boy Scout
Alex- staff member, a four armed freak Boy Scout
Mom- Tim’s mom
Kid 1- a camper
Kid 2- a camper
Scoutmaster- a troop scoutmaster
Robert- new staffer the next year

Scene: Timmy is in his Dad’s car, on the way to Boy Scout camp Father So, you’re gonna be workin’ up at Boy Scout Camp for the

Next 6 weeks? Timmy Sure am! Father Boy Scout Camp…back in my day, we worked at

Concentration Camps! Timmy DAD!! Father Remember Timmy, from 1939 to 1945, Germany was on

vacation. Oh and… we didn’t invade Poland… they

invited us. Timmy (to audience) This, is my dad. For some reason he thinks he’s a Nazi. He

wanted to make me a Nazi too, but Mom wasn’t really up

for it. I mean, you’re looking at Timmy Adolf Johnson. So,

instead of me hanging around my house in the summer,

and listening to my dad’s crazy Nazi rants, I work at Boy

Scout camp.

Timmy Dad, why do you always have to have your finger up to

your lip like that? Father It’s a mustache! Alright, we’re here. Remember, brush your

teeth…
Timmy Alright Dad
Father Change your underwear…
Timmy O.K. Dad
Father AND SHOW NO MERCY!
Timmy DAD! Alright!

(Timmy gets out of the car, grabs his bag and walks up to a door)
Timmy
*reading sign on door* Camp Director’s office…Sign in here! Oh boy!
Tony Hey! Are you from KF freakin’ C?
Timmy uhh…no, I’m here to sign in. I’ll be working for you this

summer. I’m your new employee, or as I like to say,

employWEE! (laughs)
Tony Oh…wow…sooo… you didn’t bring any freakin’ chicken?
Timmy No, was I supposed to?
Tony um, what? Oh, no… umm… here’s your freakin’ uniform,

freakin’ nametag, and any other freakin’ materials you’re

gonna need. You can go ahead up to the freakin’

campsite so you can find your freakin’ tent.
Timmy Thanks… um, wait. You got my nametag wrong.
Tony What? What’s wrong with it?
Timmy Well, my name is Tim, but the nametag says Tit.
Tony What, I can’t read it!
Timmy It says Tit.
Tony It says freakin’ what??
Timmy tit
Tony What, I can’t freakin’ hear you!?

Timmy TIT! My name is Tim but it says Tit. Tony What? Tim? What kind of a crazy freakin’ name is that? I

thought your name was Titty Johnson…freakin’ Tit for short!

Oh well, we can’t freakin’ change it now… but don’t

worry, no one will freakin’ notice. Now go along up to your

freakin’ tent, and don’t come back without no freakin’

chicken!
Timmy Okay, thanks Boss. Teehee!
Tony Jesus freakin’ Christ
Deon Yo, John, check this new kid out! He’s straight up trippin’

yo! John Yeah, I guess… Deon Check this out… Hey Yo, umm Tit! ‘Sup G? We’re gonna be

sharin’ a tent ‘aight?
Timmy Goody! Oh, and my name is actually Tim.
Deon Whatev. SO I Need to talk to you about the tent fee.
Timmy What tent fee?
Deon Say What?? You didn’t know about the tent fee? Well,

since your gonna be sharin’ a tent with me, I’m gonna

need five bucks a week. Oh, and um.. ten bucks up front. Timmy Awww schucks! I was gonna use this money to buy

medicine… but, Oh well, here you go!
Deon ‘Aight man, I know it’s whack, but, It’s the way things work.
Timmy I guess it is… whack. Ha! Whack!
John Hey kid come over here. I see you don’t know how it works

up here at camp. Timmy Yeah! I had no clue I had to pay a tent fee! Lucky for me I

brought up five hundred Dollars! Deon Gawd Dammit! John No, that’s not what I meant. But don’t worry man, I can

show you the ropes. Timmy And I’ll tie them in forty different knots! (laughs) Boy Scout

Joke… get it? ‘Cuz, you hand me the ropes and I…

John That’s not what I meant…Well anyways, let me introduce

you to the rest of the staff.
Timmy I just peed my pants a little
John You’ve already met Deon
Deon Whicka Whicka!
John There’s Adam over there…
Adam Well, Helloooo!
Timmy He sure is friendly!
John He’s gay…
Timmy But, I thought that…
John Don’t ask, don’t tell… Oh, and there’s Ron
Timmy Is he…
John Blind? Yes.
Timmy Oh, and what is he teaching up here?
John Rifle Merit Badge.
Timmy Hmmmmm…
John And there’s Alex, but we just call him Four Arms.
Timmy Why do you call him that?
Alex AHHHHHHRGLRLE!!
Timmy Oh.
Nathan Hey you kids… come down here or something….(sigh)
Timmy Who’s that?
John That’s the Program Director, Nathan. He’s emo.
Timmy Emo? What’s that?
John Ever heard of cross dressers?
Timmy Yeah.
John Picture that, only with tighter pants and darker colors…

Timmy Wow.

(To audience)

So, I guess you could say me and John were…buds! So now

that I was introduced to the staff, it was time to head down

to the lodge for First Aid and Youth Protection Training. Tony Alright, sit down. Nathan here is gonna teach you about

First Aid, so SHUT UP AND LISTEN! Nathan First things first, don’t cut down… cut across… Tony Yeah, Alright… First Aid Certified! Now it’s time for the Youth

Protection Video…

(the video begins with a narration)

This is Jimmy. Jimmy likes to play. Look at what a nice fun

loving young boy Jimmy is. If he keeps this up, he will live a

perfect life. There’s only two things that can screw that up.

One is drugs….but we’re not gonna worry about that.

What we’re worried about is….SEXUAL HARRASSMENT!!

Recent studies show that 94% of people between ages 0

and 125 don’t like to be touched in what we call….the

danger zone. SO DON’T DO IT OR THE CAMP GETS SUED!

Here’s a real life confessional of what happened Willy was

SEXUALLY HARASSED!

(the video continues with Willy’s confessional)

Well, this kid in our troop who didn’t have many friends told

me to come with him to get fire wood. We walked and

walked deeper into the forest. When I complained about

how far we were going or how dark it was getting he just

told me I was a wimp and should move to France. He said

he knew the perfect tree that had real good firewood. We

finally got to the tree and he said we should play monkeys!

I was really excited until he told me that monkeys didn’t

wear clothes. Then he said monkeys did other things…..you

know….sex things? And then he told me that if I ever told

anybody what happened, he would hurt my little brother

!(cries hysterically)

So if this video teaches you anything, it is that unless you

are confronted with the 6% that enjoy it, NO TOUCHING!

EVER!……that means you Adam!!

(end of video) Adam (sigh) Every year…

Tony Alright, your all certified for all that crap. Now Troops start

arriving tomorrow so make sure everything is ready. Yeah,

go. Timmy (to audience) I was so nervous for the next day, when I would be

teaching all the youngsters about American History, that I

set up my entire area, and I could barely sleep… Well, I

also couldn’t sleep because Deon raps in his sleep… Deon Yeah, Yeah! What you want, Boy? My name is Deon, but I

ain’t neon! Timmy (To Audience) But, I did finally get to sleep, and the next day I was sooo

excited to see all the troops arrive. But before they had a

chance to arrive, I actually got a letter in the mail from my

mom! I was so excited to read it!! Mom Hello, Son. I was going to wait and tell you when you got

back, but I just can’t hold it in. Your Grandma died. It was a

stroke. And your little sister, Susie, stepped in front of a bus.

She’s dead too. Oh, and your father and I are getting a

divorce… that crazy Nazi bastard. Well, see you in a few

weeks! Love, Mom Timmy (to audience) Well, actually, I guess that was bad news, it actually kind of

lowered my scout spirit levels. I decided that I should

probably take out my ring…. (takes out ring) With this ring, I,

Timmy Adolf Johnson, hereby up my Scout Spirit! (thrusts

ring in air)… Also, I knew that the arrival of the troops would

put me in a better mood. After waiting for just a while

longer, I saw the troop I was assigned to help for the week

pull up, and I went over to greet them. Scoutmaster Alright, Men, line up. No slackers this week, you call

everyone over the age of 18 Sir, do I make myself clear? Kid 1 Yes, Sir! Timmy Uh, hi, I’m Tim…and um no whips in camp…we kind of got

screwed over… I’ll be your guide this week. Scoutmaster Ah yes, Private. Well here is a list of merit badges my men

will be taking this week.
Timmy Okay…Um… Your boys..
Scoutmaster Men
Timmy Sorry. Your men will be taking three merit badges. We offer

Rifle and Wilderness Survival, but the third one, How to Kill a

Man with Your Bare Hands, we don’t offer that one.

Scoutmaster WHAT? Why the Hell not, Private? Aren’t you aware that

Boy Scouts is designed to train these men so that someday

they can protect our country in the Army?
Timmy That’s not all Boy Scouts is for…
Scoutmaster Yes it is, Private! Now, stand down!
Timmy (to audience) At that moment, I remembered that John told me to stick

up for myself
John (mystically) Stick up for Yourself…..Yeah, that’s it.
Timmy (to audience) So I knew that there was only one thing to do.
(Timmy assumes a Karate position)
Timmy NO IT ISN’T!

(a large fight scene breaks out, and ends with Scoutmaster on knees, Timmy holding a

sword to the back of his neck, ready to execute him) Timmy Now that I have defeated you, you must die and

honorable death…by sword!

(as Timmy is raising up sword, Deon enters flashing an FBI badge and a gun)
Deon NOW HOLD UP! HOLD UP! FBI, fools!
Timmy WAIT!...(looks puzzled) what just happened?
Deon (looks around) I…I...don’t know…
Scoutmaster Would you take us on the tour now?
Timmy (to audience) Well, the weeks passed and learned a lot of cool stuff, like

public showers with Adam…
Adam How YOU doin’?
Timmy (to audience) How to sing campfire songs…
John Let’s sing a campfire song!
Timmy Okay, I know Home on the Range
John No… we sing… different campfire songs
John (rapping) Hump…de Dump… Hump Hump… de Dumpty Dumpty…

Hump… de Dump… Hump Hump… de Dumpty Dumpty…

Humpty Dumpty Sat on a wall, Humpty Dumpty had a

great fall. All the King’s horses and all the King’s men and

HUH! Ain’t that funky now? Hump…de Dump… Hump

Hump… de Dumpty Dumpty… Hump… de Dump… Hump

Hump… de Dumpty Dumpty… Little Miss muffet sat on her

Tuffet eating her curds and whey. When along came a

spider who sat down beside her, and HUH ain’t that funky

now?
Timmy (To audience) To just plain old teaching kids about America’s history.
Timmy …But unfortunately, Abraham Lincoln was assassinated.
Kid 1 assassinated?
Timmy Yes, he’s dead.
Kid 1 Dead? Why?
Timmy Because someone shot him.
Kid 1 Oh… so, Is he dead?
Timmy Yes, he was shot and killed.
Kid 2 And now he’s in the ground.
Timmy Yes, they buried him in the ground after he died.
Kid 1 What? Why was he buried in the ground?
Kid 2 Cuz we all go in the ground after we die, stupid.
Timmy Now kids…
Kid 1 But, what if we wake up?
Kid 2 Or worms eat us?
Timmy Kids!
Kid 1 Or we wake up while worms are eating us!!!??
Timmy KIDS!!!!

(pause) Kid 1 So, wait, is he dead? Timmy (to audience) It turned out to be a great year, I learned so much,

especially from John. I can’t wait until next year….

(transition into the year after, Timmy is standing with a new staffer, Robert) Timmy Hey, you the new kid?

Robert Yes, I am Robert Willingham the Third Timmy I’m Tim. Robert Nice to meet you, Tim. Timmy Hey, I’ll help ya get set up… but first, let’s talk about your

tent fee. Robert Tent fee? End.
```

---

## IC-1455: DEPRESSED WHITE GIRL: THE WORLD’S WORST D.I. (Dramatic Interpretation)

- Title: DEPRESSED WHITE GIRL: THE WORLD’S WORST D.I. (Dramatic Interpretation)
- Author (byline): Brandon Daley
- Work: DEPRESSED WHITE GIRL: THE WORLD’S WORST D.I. (Dramatic Interpretation)
- Publisher: Mushroom Cloud Press
- Publication date as stated: 2010
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1735
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
(Depressed White Girl enters and talks to audience)
Depressed White Girl: It was about five o'clock when I got the call.
(Clock dings five times and then the phone rings. Girl picks it up.)
Depressed White Girl: Hello?
Phone Operator: Hi, is Depressed White Girl available?
Depressed White Girl: This is she.
Phone Operator: Hello, Depressed White Girl, this is Happy-Go-Lucky Phone Operator—from “Baby or
Beer Belly? Test Facilities.” Your test results have come in. You’re pregnant.
Depressed White Girl: What? Oh my, I can’t believe this.
Phone Operator: Congratulations. Would you like to schedule a follow-up appointment?
Depressed White Girl: How accurate are the tests?
Phone Operator: They are never wrong. Now would you like to schedule a follow-up?
Depressed White Girl: I think first I need to talk to my boyfriend…
Phone Operator: Well, how about—
Depressed White Girl: …or maybe the football team captain…or possibly my English teacher…
Phone Operator: Yes, that should be in order. But would—
Depressed White Girl: …or the school Janitorial staff…or maybe—
Phone Operator: Okay! That’s enough of that,
Depressed White Girl: You’re right. I should probably just talk to all of them. Better safe than sorry is what
I always say.
Phone Operator: Right…Now would you like to know the sex of your baby?
Depressed White Girl: Oh, no. I’d like that to be a surprise. I hope it’s a girl—
Phone Operator: Well, it’s not.
Depressed White Girl: Oh…Are you sure?
Phone Operator: That test is even more accurate than the pregnancy tests. Thank you for your business and
we hope to see you again soon.
(Depressed White Girl hangs up the phone. She begins talking to the audience again.)

Depressed White Girl: Oh goodness! I was pregnant! Gosh, what are my parents going to say!
(Mom and Dad enter suddenly)
Mom: Dear, we heard you talking regretfully, what’s wrong?
Dad: Yes darling, you haven’t done anything that would make us abuse you again—like we did when you
were only this tall.
(Dad holds his hand out to show how tall. Mom and Dad both giggle reminiscently).
Depressed White Girl: Oh Mom, Dad…it’s nothing…
Mom: Oh, honey. You know you can tell us anything.
Dad: Yeah, I mean, unless it’s something extreme like you being pregnant—which, like I mentioned earlier,
would send me into a fit of rage like when you were only this tall.
(Dad holds his hand out again to show how tall. Mom and Dad both giggle reminiscently).
Depressed White Girl: Um…well…uh…
(Mom looks at the phone).
Mom: Dear, why is Unplanned Parenthood on our caller ID under past-received calls. Were you talking to
them?
Depressed White Girl: Oh, you guys! I’m so sorry!
Mom: I told you to not screen phone calls for me!
Depressed White Girl: No, mom. It wasn’t for you this time. I’m…. pregnant.
(Silence)
Dad: Excuse me—did you say you had a head dent or that you were pregnant.
Depressed White Girl: Pregnant…
Dad: OH GOD! I’M GOING TO HURT HER! I CAN’T CONTROL MY ANGER! YOU KNOW THIS!
HERE IT COMES!
(Dad gaily slaps at his daughter’s shoulder)
Depressed White Girl: Stop it! You’re bringing back repressed memories of my childhood!
Mom: I mean a head dent we could fix! Are you sure it’s not that?
Depressed White Girl: I’m as positive as my pregnancy tests.

Dad: I can’t believe you’re pregnant again!
Depressed White Girl: Dad! I’ve never been pregnant before! You’re thinking of Mom!
Dad: Is that where you get this behavior! Your mother?
Mom: Oh my gosh! I feel so horrible!
Dad (to mom): Great, first you burn dinner and now you get our daughter pregnant!
Mom: I’m sorry honey, I really am!
Dad: Sorry isn’t going to kill this baby!
Mom: I guess it won’t be so bad if it’s a grand daughter as opposed to a grand son.
Depressed White Girl: But it’s a boy!
(Mom screams)
Mom: This sickens me.
Depressed White Girl: Look guys! I’m old enough to make my own decisions. And if accidentally
impregnating myself by sperm of some random member of my school’s janitorial staff is what I want, then I
need you guys to support that!
Mom: No really, this is making me sick! I think I may be clinically sick because of this! My heart hurts and
my skin is inflaming!
Dad: That sounds like Lupus to me! Damnit sweetie! First you get knocked up and now you’ve gone and
given your mother Lupus! We need to get her to a hospital. Watch the house while we’re gone.
Depressed White Girl: Wait! I want to come with!
Dad: A hospital is no place for a pregnant girl to be hanging around at! Watch over the house while we’re
gone—and try to keep from having any sex!
Mom: If you get hungry there’s leftover lasagna in the fridge.
Dad: Come on! Let’s get out of here!
(Dad picks up Mom and the two exit. Depressed White Girl addresses audience).
Depressed White Girl: Gosh! This baby has brought back awful memories of child abuse from when I was
younger and has given my mom lupus. I need to get rid of it!
(Depressed White Girl picks up the phone and dials a number)
Phone Operator 2: Oops I Did It Again Abortion Clinic—this is Medical School Dropout speaking. How
may I direct your call?

Depressed White Girl: Hi, I’m Depressed White Girl and I need to make an appointment.
Phone Operator 2: Okay, our next opening is in nine months. Does that work for you?
(Depressed White Girl flips through her planner)
Depressed White Girl: I don’t see any scheduling conflicts in my planner. How much does this cost?
Phone Operator 2: An abortion costs between a fajillion to three fajillion dollars.
Depressed White Girl: Three fajillion dollars! Where am I supposed to find that kind of money!
Phone Operator 2: You could ask your parents.
Depressed White Girl: I can’t!
Phone Operator 2: Oh, did you tell them about the pregnancy and now your Mom has Hepatitis?
Depressed White Girl: Lupus, actually.
Phone Operator 2: Well, you could always sell your body.
Depressed White Girl: What! That’s how I got in this situation in the first place!
Phone Operator 2: No silly, I mean your organs. A kidney is going for about half a jillion dollars. You could
sell six of your kidneys to get the money.
Depressed White Girl: I don’t have six kidneys though!
Phone Operator 2: What about lungs—do you have lungs?
Depressed White Girl: Yes, I believe so.
Phone Operator 2: A set of lungs goes for approximately three jillion dollars. Do that and then you’d have
the money for the abortion.
Depressed White Girl: Oh thank you for your help, mam.
Phone Operator 2: Not a problem. I’ll see you later.
Depressed White Girl: Thanks! Goodbye.
(Depressed White Girl hangs up. She talks to the audience again.)
Depressed White Girl: So that’s what was going to happen. I was going to sell my lungs in order to get the
money for the abortion, in turn curing my mother’s lupus and re-repressing those memories of domestic
violence from my childhood. I looked up the local organ buying black market’s number in the phone book
and made an appointment. They said they could see me immediately. The man I talked to, Rufio, suggested I
eat something before the surgery—to prevent death. I decided to heat up the lasagna, but I was so excited
about getting my organs harvested in turn for baby removal services, I thought I could run to the facilities
and eat at the same time. That’s when…it happened. I ran and ran and ran until…my foot…(weeping)

landed on a toaster strudel that had been abandoned on the ground. Just abandoned! No one in sight! Just this damn toaster strudel lying there in the middle of the sidewalk! (Trying to fight tears) Well, when my foot landed on it, I slid…and the lasagna went all over me! I was just covered with lasagna! It was awful…I kept walking though…I kept walking! And then I saw it—the place that would buy my lungs! I was so excited I…I didn’t even see the bear running at me from my left. My mom used to always tell me that bears loved lasagna…but I didn’t believe her…at least, I didn’t believe her until it was to late. (Completely crying) That day, in the parking lot of the organ-harvesting facility a full-grown bear mauled me… (Depressed White Girl is heartbroken with over the top bawling. She pauses and then looks at her stomach. She grabs her stomach area with her hands and then looks back up slowly.) Depressed White Girl: I mean…a full-grown bear…mauled…us. (Depressed White Girl’s eyes close as she passes out with her hands on her stomach. Then she slowly opens her eyes.) Depressed White Girl: Where…where am I? (She looks up and sees her Dad). Depressed White Girl: Dad? Where am I? Where’s mom! Dad: Calm down, honey. You’re in the hospital. And your Mom’s fine too—I mean she’s dead because you killed her with lupus, but I’m sure wherever she is (points down at Hell and kind of giggles) she’s happier than she was with her sex-craving daughter. Depressed White Girl: She’s dead? Dad: No, I’m just kidding. She’s across the hall. Depressed White Girl: Oh thank goodness. (Dad’s cell phone rings) Dad: Hello…oh, okay. Thank you. Goodbye. (Hangs up) Dad: Okay, now she is actually dead. Depressed White Girl: Oh goodness…first I get pregnant, than I get mauled by a bear, and now I killed my mom. Dad: That bear that took you down has been shot and maimed though. He won’t hurt anyone else. Depressed White Girl: That’s good to know. Dad: Yes, however, the PETA folk called it cruelty to animals, so he’s actually here in the bed next to you getting healed.

(Dad pulls back curtain separating the two halves of the room to reveal the bear lying in the bed next to
her).
Dad: He just ate your doctor too, so I’m not sure what kind of condition you’re in.
Depressed White Girl: I guess if all this has taught me anything it’s that life will always keep you down. No
matter how much you think things are looking up, travesty is just around the corner—whether in the form
of a toaster strudel or lupus. So I guess there’s no reason to expect anything more than a dead mom and a
split hospital room with a bear that just mauled you on the other side.
Dad: Not to mention I ate your lunch while you were passed out, so you probably won’t be eating for
another good six or seven hours.
Depressed White Girl: Bad stuff—impossible to avoid, but possible to accept.
(Enter a nurse reading a chart)
Nurse: Hello, are you Depressed White Girl.
Depressed White Girl: Yes I am.
Nurse: Well, I’m afraid we have some good news and some bad news.
(Dad and Depressed White Girl laugh and exchange glances about the irony).
Depressed White Girl: Go ahead Nurse; I’m up for anything.
Nurse: The good news is your condition seems stable so you can leave whenever you’d like.
Depressed White Girl: That’s good to hear…and the bad news?
Nurse: Well, the baby in your stomach isn’t a girl.
Depressed White Girl: Ha, I know that already, but thanks anyway.
Nurse: Yes, but it’s not a boy either. It’s an alien baby. Aliens impregnated you.
(Silence)
Depressed White Girl: Well…I guess it can’t turn out anymore ugly than the janitorial staff.
(Everyone laughs, but Dad stops after a moment.)
Dad: Wait, you slept with the janitorial staff?
```

---

## IC-1456: Finding Ryan Copyright 2009 by Dave Cameron

- Title: Finding Ryan Copyright 2009 by Dave Cameron
- Author (byline): Dave Cameron
- Work: Finding Ryan Copyright 2009 by Dave Cameron
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1424
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
Character list:
Narrator
Ryan
Krishnov
Tyrone
Ashley
Dad
Narrator: Life sucks. To tell you the truth, the hardest part of life is growing up and trying to become successful.
Especially for a young boy named Ryan.
Ryan: Hi, I’m Ryan
Narrator: Ryan is just a kid with too much brains.
Ryan: I had a 4.6 GPA
Narrator: In 2nd grade. Anyways, Ryan has too much brains and not enough friends.
Ryan: I have no friends! (Smiling at first. but then realizes the comment he made)
Narrator: More than anything, Ryan wants to fit in with the crowd. This is the story of Ryan, just a boy who learns
the struggles of growing up the hard way.
Ryan: Its so hard.
Narrator: That’s what she said. No, seriously though. Life is tough. Ryan just got a taste of this toughness when he
tried to make friends.
(Change of scene)
Ryan: Hey want to be my friend?
Tyrone: No
Ryan: Awh come on Tyrone! We can be good friends!
Tyrone: I said no. Dang, what is with these new kids.
Ryan: Man I hate being the new kid. (To Ashley) Will you be my friend Ashley?
Ashley: No, sorry its against cheerleading rules for us cheerleaders to be friends with geeks. Especially geeks that
are new kids.
Ryan: Awh man.
Narrator: Ryan, couldn’t deny this because he was, in fact a new kid, and he was a geek.

Ryan: Well I am a geek and I am new to the school and I do not want to break any rules, therefore I cannot be
friends with her. I wish I had a friend, just one friend.
Krishnov: Yello. My name is Krishnov. I am new kid also.
Ryan: Hi what do you what from me?
Krishnov: I would like companionship if you please.
Ryan: You mean a friendship?
Krishnov: Yes, an alliance.
Ryan: Okay! I made a friend! I’m so happy!
Narrator: A happy day it was for Ryan. He had made friends with the foreign exchange student,
Krishnov. He only had one friend though, but Ryan and Krishnov were inseparable. They did everything together,
because no one else would be their friend. However, they both tried their hardest to fit in and be accepted with the
crowd.
(scene change)
Ryan: The crowd goes crazy as Ryan dribbles to take the shot. Ryan shoots! (Misses terribly)
Tyrone: Dang Ryan you suck at basketball.
Ryan: I know, don’t rub it in Tyrone.
Tyrone: Try another sport man. Try ping pong. Geeks are always good at ping-pong. Yo go pick up that paddle I’ll
play you in ping pong.
Ryan: Umm okay, I’ll try.
(Tyrone and Ryan have a ping pong game. Ryan is terrible, Tyrone is good.)
Tyrone: Man if you are bad at a game designed for nerds, you must suck at all sports.
Ryan: Awh man. If I can’t play a sport I will never fit in.
Krishnov: In home country, Krishnov best on goose hunting team.
Ryan: Krishnov, that’s not a sport in America.
Krishnov: Mouse chasing?
Ryan: No
Krishnov: Elephant racing?
Ryan: No.
Krishnov: Peacock fighting?
Ryan: Krishnov stop. We really need to find a way to fit in.
Krishnov: Maybe we try out for school play?

Ryan: Good idea Krishnov
(at the school play)
Ryan: Alright Krishnov, you go first. They want you to give a monologue from a play.
Krishnov: Okay. Hello. My name Krishnov. I am auditioning. Here is monologue: Where art thou Hamlet? To be or
not to be lending me your ears. All the world’s a Romeo. Et tu, Shakespeare? Good? Do I get part?
Ryan: Krishnov, you just mixed like six plays. You do not get the part.
Krishnov: You try giving mono to director.
Ryan: Mono? You mean monologue?
Krishnov: Yes this is what I mean, go ahead and try.
Ryan: No, I don’t want to. This is useless. I give up! We’ll never fit in.
Narrator: It was hard times for Ryan. He fell into depression. He only had one friend and he didn’t fit in anywhere.
The next step on the bumpy road for Ryan was learning about love. Ryan had never been in love. But for the first
time ever, he thought he had fallen in love.
(change scene)

Ryan: (Looking at computer) Awh I love her. I just wish Ashley would notice me. You know what, I’m going to
write her a long, meaningful love letter and put it in her locker!
(Scene change. Ryan puts letter in locker and walks away)
Ashley: (Pulls out letter and reads aloud) “Dear Ashley, I love you, from Ryan” Eww.
Ryan: (with flowers) Hey Ashley, I see you got my letter. I was wondering, since I’m no longer the “new kid” at
school, will you go to prom with me?
Ashley: Sure
Ryan: Really?
Ashley: No, sorry. I’m too shallow. I would only go to prom with the captain of the football team. I mean I might
consider you if you were like captain of the ping pong team or had friends or fit in somewhere. But your not captain
of anything. Except maybe captain of loners.
Ryan: Awh man.
Krishnov: Its okay Ryan. Let me try asking girl to prom. (to teacher) Hello, will you make me happy, like when
mouse sees cheese, and go to prom with me?
Ryan: Krishnov! That’s the teacher! You can’t ask her to prom!!
Krishnov: Oh. You are right. No one likes us, we do not it fit in with any group. We are geeks.
Ryan: I know.

Narrator: No one liked Ryan, or so it seemed. Ryan had forgotten about his family. Ryan was scared to talk to his parents, especially his father. Ryan was scared to talk his father because his father was the most successful doctor in the country. As a kid, Ryan’s father knew exactly what he wanted to be when he grew up, and he ended up becoming just what he wanted to be – a doctor. Ryan: (to himself) What to be when I’m older?! A doctor? Lawyer? Businessman? Krishnov: How bout a Gigolo? Look Ryan, you are smartest boy in grade. You can be any profession you desire. Just choose one. Ryan: I just don’t know what to do with my future. My dad knew since he was a kid and I just don’t know. Krishnov: How bout Gigolo? Ryan: Krishnov that is a terrible idea. I want to be successful, like my dad. Krishnov: Why don’t you ask your father for advice Ryan: You know, as scared as I am to do this, I think I have no choice. I’m just to upset to care I’m going to ask my dad. (to Dad) Dad? Dad: Who are you? Ryan: Ryan… your son? Dad: Just joking, you like never talk to me so I was surprised, what’s up kid? Ryan: I don’t know what to do with my future. Dad: What do you mean? Ryan: I know I’m the smartest kid in the grade, but I have no friends, no girls like me, I don’t fit in anywhere. Life just sucks. I feel like my future is going to be terrible, especially since I don’t know what to do with my life. Dad: Listen here son. You don’t have to know what you want to be when you grow up already. You’re just in high school. Ryan: But Dad, you knew you wanted to be a doctor since you were a kid, now you’re the most successful doctor in the country. Dad: I was a dweeb. Don’t follow my example. Listen to me. You can be anything you want and I will support you. Ryan: But I want to live up to everyone’s expectations and be as successful as you. Dad: Listen, the only thing that defines success is how you feel in your heart after you do something. So whatever you do, even if you have no friends to support you, no girls like you, and you just don’t fit in anywhere, just know that your dad will always be here for you. Just live your life and let the chips fall where they may. Ryan: It was at that moment, when my dad said those words to me; I realized the most important in the world. I realized no matter what path I choose for life, I would always have the support of my dad… and I guess Krishnov and that everything would work out, no matter what I did. Narrator***: And as I got older, and older, and older and grew up. I realized that what my dad said, was right. And everything was okay. Yes, life sucks. But in my heart, it was successful. And the story of Ryan, ended happily.

***Ryan becomes the narrator while saying this last line. The narrator throughout the story is a grown up version of Ryan, and this is revealed to the audience in this line.
```

---

## IC-1457: Gerald the Life-sized Talking Spork

- Title: Gerald the Life-sized Talking Spork
- Author (byline): Spill Major
- Work: Gerald the Life-sized Talking Spork
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1511
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
Gerald the Life-sized Talking Spork.

Hello, I’m Gerald, the life-sized talking spork. You have no idea how many pills I have to take just to say that without crying. My life is a sick joke. Please, please help me.

Who wants to learn about sporks today? Wow, there’s a lot of you. Well you’re all freaking crazy. But here it goes anyhow. (He drinks from a flask – clearly has a special pocket in his costume just for this. Then, he is suddenly animated.) I’m here today to tell you about the amazing history of me, the spork! The spork was first invented around 3000 B.C., but of course that’s because someone carved one out of a stone on accident. Not knowing what to do with it, scientists speculate that cavemen probably tried it out as a comb, a pubic comb, a tongue depressor, and a nose piercing before finally settling on using it gouge out other cavemen’s eyes. And it is from those days that we get our current use of the spork – because once the cavemen gouged out the eye, they realized could then use the spork to devour it! (He is handed a card from offstage) What’s this? Gerald, read what’s on the cards or we will take you off the health plan. Well folks, I guess we know who’s the boss around here: that’s right, Mr. Codine Co-pay! So, because I can’t take having my friends at the rehab center see me in this pathetic costume, here’s the real history of… The Spork.

The modern day spork actually started with the chopstick. No, I’m not saying they had sporks back in the ancient Orient; they were much too smart for that. But then, of course, an American had to come along – in this case, General… H … X… niner… should know his full name… McArthur, who was in charge of occupied Japan after World War II. As an American who naturally feared the presence of any culture or tradition, the good General banned all chopsticks, decreeing them uncivilized. However, the common “fork” was seen as a dangerous weapon of insurrection, so the Japanese could not be switched over to traditional, deadly American silverware. Since my two-year-old spends the 3 hours per week I have with him jabbing me with objects like chopsticks, forks, and desk lamps, I can’t say I blame ol’ Mickey A.

Well, as you no doubt guessed cause you just couldn’t wait for the me to tell you, you impatient people you, the compromise the army reached between eating utensil and deadly weapon was the spork. It was tough enough to dig into teriyaki chicken, but not so tough as to be used to repel an occupying force of several million troops. I know, I know, it’s a fine line, like the line between social drinking and pathetic self-loathing alcoholism (drinks). My probation officer says drinking straight from the handle of rum in the donut store at 9am counts as the latter, but I say, hey, I was just being social with that nice donut-serving lady. Although, I guess when the manager asked me to leave and I tried to drown him in the vat of icing, that wasn’t so social. Oh well, you live and you learn. Like us, right? I’m learning about how terrible life can be, and you’re learning about sporks.

Here’s something that combines both. When researching this little spiel, the nice people here at Billinson’s Plastic Works found out that the largest spork on record belongs to the U.S. Navy, who use a metal version almost six feet long for preparing food. Then they saw me. In my costume. And they realized that I, in fact, am the largest spork on record. Yes friends, that’s right, you’re witnessing history. Spork history. Right here in front of you. Isn’t that great?

I’ll give you a hint. No. It’s not great. It’s awful. Sometimes, I look in the mirror. I look real deep, past the spork, past the bags in my eyes, the sores on my lips. I look deep in that mirror and I see myself, a young boy, 11 or 12. Sure, I’ve used sporks in restaurants. Maybe I even enjoyed it. But my life is free, it’s open, it’s not bound by any utensils. I think about that boy, with his precious freedom, and I weep. Not just for me, but for all of humanity. Ok, well, really, I just weep for me.

You’re not interested in me. You’re here at the Billinson Sporkworks because you’re interested in sporks. Obviously, there’s something wrong with you. But you’ve learned a lot about them. I hope you care, I sure don’t. I care about paying my ex-wife to support her new boyfriend… they can afford real forks and spoons, I assure you.

Now, because this is America and you can’t learn anything without also being persuaded to buy something, I will tell you a little bit about the history of our company, Billinson Sporkworks.

Billinson started off as Billinson Badgers. For some reason, during the Great Depression, the federal government paid Bill Boxer Sr. an awful lot of money to farm badgers on the great plains. For what purpose the badgers would be used, it was never clear, but it was judged somehow useful to have a stockpile of badgers on hand. They just sold them right back to the government, Lord knows what they did with them. This continued until one fateful night in the late 40’s, if you consider the destiny of a spork factory to be anything that fate remotely cares about.

On that night, Bill Sr. made a desperate run to the outhouse right as a big Plains-country storm was rolling in. He wanted to take care of business before the lightning started. Ol’ Bill mistimed it, you see, and he was trapped in the outhouse as rains blew and thunder bellowed around him. He underestimated the storm, though, and there was a flash flood. He worried about the badgers, though they seemed to have a place to hide during the storm. Bill was about to find out where.

He heard it first. A rumbling below him. Then, the outhouse started to shake, the pipes clanking and whining. A huge jolt shot Bill off the can, and just in time. The toilet literally lifted off the ground and shot out of the ground on a column of sewage and flood water. That wasn’t all, though. Then the badgers emerged. Hundreds. Bill was in the storm now, watching in amazement as his entire stock of badgers were flooded out from their storm shelter, his septic system. Bill could only assume that they had created great caves around the original tank; that would explain why he had never needed to have it drained.

This thought lasted only a second. The next second, Bill was fleeing a horde of angry, smelly badgers. You can’t make this up.

Then, wouldn’t you know it, Lightning struck one of the hordes. The sewage protected the badgers, but the outer layer of sludge on them was burning. A mass of flaming, poop-covered badgers pursued Bill back to the house. Wilma, his wife, was waiting at the door, and thank goodness. She had the garden hose going full blast, nearly drained the whole reservoir. But it kept the badgers at bay until Bill Jr. could marshal them with a tractor towards the barn. Bill Sr. watched with wild eyes, panting and cursing.

The next day, Bill saw a story about sporks in a newspaper. “That’s what we’re making from now on, son. Sporks.” And now you have me, up here, the saddest utensil alive.

Sometimes, I look in the mirror, when I have my costume on, and I don’t entirely hate myself. There’s something beautiful in the spork, or at least in its simplicity. Two ideas, turned into one. That’s a rare thing in a world that keeps getting more complicated. It gives you hope, for a minute, that people might figure something out. But then the next minute, I’m still in the spork costume.

I know a lot of you will go away from this night and remember the sporks. As chief representative of sporkkind, allow me to say this: please reconsider that decision. Please, please reconsider. Forget us. Forget me. Don’t speak of this night to anyone… ever. If you do, I’ll slash your tires. Hard as that is to do with a spork, but, I’ve got a pretty big spork.. Oh God, please, why won’t you reconsider?

No? Well, Fork you. Fork you and spoon you.

And look at this… (brings on baby doll in spork costume) We don’t even know who the father is. Hell, we don’t even know if it’s a father he’s missing. Who can tell?

They’re giving me that look now, so I guess I’m done. I’ll see you at the end of the show. (walking off) If I don’t set it on fire first. (looks at someone offstage). I know, I know, if I set it on fire I won’t get my paycheck, and then my ex-wife gets my house, I understand. You’re a real pain in the ass. Or stem. Whatever I have. (back out) Buenas Noches, losers.
```

---

## IC-1458: (girls)

- Title: (girls)
- Author (byline): jason chou
- Work: (girls)
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: NARRATOR, GIRL, LOUDSPEAKER, VICTIM, OBSERVER, GIRL2, GUY, GIRL1, GUY1, GUY2, BOY
- Teaser before the introduction: No
- Spoken words (computed): 1002
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
♀

NARRATOR:
What are little boys made of?
Frogs and snails
And puppy dog tails
That’s what little boys are made of.
What are little girls made of?
Sugar and spice
And all things nice
That’s what little girls are made of.
It’s a pretty cute rhyme…cute considering it’s festering with lies!! (sudden volume and
temperament change) For there is something that the nursery rhyme scholars forgot to
mention. Girls are MESSED UP! And today it is up to me…the sultan of suave to lead all
of you to a better understanding of the inner workings of girls.
First, appearance, something that all girls are never satisfied with yet still love to show.
No matter what a girl says, she wants to have her picture taken.

GIRL: Nonono I don’t want to be in it…I don’t want…i look so gross…

(GIRL gives in and poses while giggling)

NARRATOR: And once a memorystickfull of pictures are taken, you know she’s going to put them on her xanga…or her shutterfly…or her myspace…or her livejournal. And if a girl is going to post her pictures online, you know there will be little captions depicting her hatred towards her own appearance.

GIRL: (typing) OMG...I hate this picture…everyone in it looks so cute but me! Oh my god...what am I doing with my face? my arm looks so fat...

NARRATOR: When trying to characterize a girl, one quality always seems to show through…a love for shopping. Now let me first clear the mists of doubt in the air by saying the myths are true ladies and gentlemen. Girls do do preshopping. They do do it! THEY DO DO IT! What is preshopping you may ask? Let me show you. Meet Nancy...

GIRL: Hello!

NARRATOR: Nancy is your average everyday schoolgirl.

GIRL: I am your average everyday schoolgirl!

NARRATOR: So one day Nancy decides that she wants to go shopping.

GIRL: I’m going shopping shopping shopping lalalala

NARRATOR: She scans the shelves and racks for the newest clothes

GIRL: (looking at clothes) ooo cute …cute…cute...cute…adorable!

NARRATOR: Then, Nancy goes home…empty-handed-handed-handed-handed (echo). How is that possible!!! Do not fret, it is all part of her plan.

GIRL: That’s right.

NARRATOR: Nancy goes to her room and takes out all of her clothes. And then, she thinks.

GIRL: Uhhhhhhhhhhhhhhhhhhh….

NARRATOR: She thinks about all the clothes she saw at the mall and how they would match the clothes she already has at home.

GIRL: Oh my god! That cute pink tank top I saw would totally go with this skirt….and those shoes!! It’s so perfect!

NARRATOR: Upon finding the perfect match, Nancy then returns to the mall…on the same day-day-day-day (echo). Why do girls do this? Why do they put themselves through the torture of parking at the local mall twice in one day on a Sunday afternoon?

GIRL: Duh. Because I’m worth it.

NARRATOR: If girl were a religion, then mall would be her temple, or pagoda, or maybe even a mosque. Let’s watch in the Passion of Christ-ina. (sing while opening and closing the doors of the mall) Hallelujah! Hallelujah! Hallelujah! Hale-i-lu-jah!

(GIRL walks inside)

LOUDSPEAKER: Attention all shoppers, there is a sale at Abercrombie and Fitch.

(sing heavy action music. GIRL runs passionately and elbows someone out of the way)

VICTIM: My baby!

GIRL: Sorry!!!

(continue singing)

OBSERVER: Orange Julius? (He offers to Girl)

GIRL: Thank you!!!

(continue singing while GIRL splashes water on face)

OBSERVER: Watch out wet floor!!

GIRL: Nooooo!!

(GIRL jump and flying action. After landing, GIRL’s cell phone goes off)

GIRL: Hello?

GIRL2: Hi Christina! Guess who I just saw? I just saw Amanda and she’s totally wearing Abercrombie and Fitch!

GIRL: Yea…so?

GIRL2: Well no one wears Abercrombie and Fitch anymore duh!

GIRL: Oh right, duh…

GIRL2: Yea…so where are you right now?

GIRL: Oh. I’m at the mall...inside every single store but Abercrombie and Fitch. Okay gots to go, kisses!

NARRATOR: Heaven to some, hell to others, Sephora…the perfume and makeup shop in every mall where a girl goes to punish her boyfriend. From a girl’s perspective...

GIRL: Oh my god sephora!! It smells so good in here … honey how does this look on me?

(grab lipstick and try it on)...ooo look blueberry (pick up fragrance bottle and try it)…ooo with a hint of cloud… you should try it! It’ll be cute! Just try it (spray boyfriend)…kiwi! Try it! Mango! Try it! Passion fruit! Passion (seductively after glancing at boyfriend) (Water gun pumping noise and action) (Sprinkler spray action)

NARRATOR: From a guy’s perspective...

GUY: Holy (censor beep) sephora…(walk with bass beat…suspense…christian hand movement)...yea honey…that’s a great color, how about we get it and leave? ..now…no it’s really okay…no I know it’ll be cute but really ahhhh…my eyes!! stop it!!! I smell like demon!! What are you doing? No, three pumps is enough! Nooo... (GUY falls back)

NARRATOR: Theorists claim that girls and boys will never understand each other. And this is very true, girls and boys even listen to different kinds of music.

(GIRL puts in earplugs…scroll ipod with tongue click) (GIRL sings) I love you...everytime I sleep you’re in my dreams you give me wings...butterfly kisses...caterpillar nibbles...you’re fuzzy and cute...I love love love love love you...

(GUY picks up boombox, GUY sings)

NARRATOR: Boys and girls even care about different things

GIRL1: Oh my god! Did you hear the news? Brad Pitt and Jennifer Aniston totally broke up!

GIRL2: (in crying pain) Noooo...no they didn’t…they were so beautiful together….what about their beautiful future babies!!!

GUY1: Dude…did you hear the news? Kobe and Shaq aint playing together next year man.

GUY2: Nooo...no way man…they were so beautiful together….

NARRATOR: And one final quality of girls is their power to ruin a guy’s life through the employment of a conversation deception. This form of trickery is so hard to explain that mathematicians have struggled for years to think of a way to classify it. And they have, with the simple equation of y=0. Y=0 where y is how much a girl truly cares about you.

GIRL: Oh my god I haven’t seen you for like two weeks. I’m so interested in all that you did over break!

BOY: Well…I found a cure for ca...

GIRL: (interrupts) Oh my god I hate Charlotte…I mean…I didn’t hate her before..but now she just really t’s me off…

BOY: Well. I guess we could talk about Charlotte...

GIRL: Yea we definitely should.

NARRATOR: That is all the time I have for today. I know that you may think I sound like a bitter male chauvinist, but I can bet that every single girl in this room can relate to every single scenario that I have presented today...And every single guy in this room is now very uncomfortable by your presence.
```

---

## IC-1459: Lawrence Atkinson’s Great Ideas Text copyright 2003 Lawrence Atkinson.

- Title: Lawrence Atkinson’s Great Ideas Text copyright 2003 Lawrence Atkinson.
- Author (byline): Not specified
- Work: Lawrence Atkinson’s Great Ideas Text copyright 2003 Lawrence Atkinson.
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 884
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
Set:

Simple. Typewriter, chair.

Movie screen:

Can be real or fake. Action can be live or recorded.

Characters:

BEN. A young, struggling screenwriter. Clearly poor. ALL OTHER CHARACTERS. Can be modified to follow (or not follow) the movies from which they are molded.

(Lights Down. The THX SOUND is played, along with something mocking its slogan, “ the audience is listening.” Lights up on Ben at typewriter.)

BEN This sucks. It's a screenplay in progress. Of course it's going to suck to begin. Oh, I just can't think of anything. Okay. I got one. A cyborg is sent back through time to kill the mother of his future enemy.

START OF MOVIE SEQUENCE 1

EXT. HOUSE. DAY.

BEN
A knuckled hand reaches up and knocks on the door of the house. A
'WOMAN' appears and opens the door a little. Through the crack in the
door, a MAN wearing sunglasses and a black leather jacket stares back at
her.

MAN (Austrian accent) Sarah Conner?

'WOMAN' Ummm. No.

MAN My mistake.

BEN
The man turns around and walks a little way from the door, before
stopping to look at a piece of ripped out phone page. He turns around
and walks toward the door again.

INT. HOUSE. DAY.

MAN (O.S.)

Sarah Conner?

‘ WOMAN’ Nope sorry. That’ s still not me.

MAN (O.S.) Jehovah's witnesses.

'WOMAN' Oh, thank Jehovah.

(He pulls out a gun and the woman falls to the floor. He then put the gun away and stands over the helpless 'woman'. He reaches out his hand.)

MAN Get down! You need to come with me if you want to live.

WOMAN I’ m sorry; I’ m waiting for an important phone call.

MAN I'll be back.

END OF MOVIE SEQUENCE 1

BEN No, How about a guy sitting on a bench, talking about life.

START OF MOVIE SEQUENCE 2

(A guy sits on a park bench eating chocolates. Another MAN is next to Him.)

GUY
(Southern Accent)
Mama always said, "life is like a box of chocolates. You never know what
you're gonna-
(Before he can finish, the Man sitting next to him punches him in the
Face and steals his chocolate.)

GUY Lieutenant Dan!

Man wheels away

LIEUTENANT DAN Run Forest Run, HAHAHA

END OF MOVIE SEQUENCE 2

BEN No. People won’ t want to see a movie like that. What about action? A geeky software developer, I can probably see Keanu Reeves in the role, is contacted by a master hacker, who tells him that the world he's living in is not the real world, but rather a computer generated dream world created by computers in the real real world.

START OF MOVIE SEQUENCE 3

INT. OFFICE CUBICLE. DAY.

(A GEEK is sitting in front of a computer screen typing furiously. He is
dressed in black clothing with a black overcoat, and he is wearing
black sunglasses. We cannot see the monitor, but the Geek continues to
type furiously. A DELIVERY MAN appears with a package.)

DELIVERY MAN Thomas A. Anderson?

THE GEEK Yeah, that's me.

(The Delivery Man hands him a package and a clipboard.)

DELIVERY MAN Okay. Please sign here, and here, and here, initial here and here, girlfriend's number here, PIN number here, and credit card number here.

THE GEEK Hey, wait a minute!

(The Delivery Man stops.)

THE GEEK What about my insurance number?

(The Delivery Man comes back.)

DELIVERY MAN Oh yeah...Insurance number here.

(The Geek signs the form.)

DELIVERY MAN Thank you. Goodbye, Mr. Anderson.

(The Geek picks up the package. Instantly it begins to ring. The Geek stands up.)

THE GEEK Hello?

(The package continues to ring. The Geek shakes it and a small cell phone falls onto the floor.)

THE GEEK Whoa.

(The Geek picks up the phone and answers it.)

THE GEEK Hello?

THE VOICE (O.S.) Hello Neon, do you know who this is?

THE GEEK God?

THE VOICE (O.S.)
No, you moron. My name is Marpheass. I had to revoke my proper name due
to copyright issues. You will be called Neon...Due, also, to copyright
issues.

THE GEEK Whoa.

THE VOICE (O.S.) They're coming for you Neon. They're coming and I don't know what they're going to do.

THE GEEK Who's coming?

THE VOICE (O.S.) Stand up and see for yourself.

THE GEEK But I'm already standing up.

THE VOICE (O.S.) Then...Sit down, and then stand back again.

THE GEEK What? Right now?

THE VOICE (O.S.)

Yes. Do it slowly. The elevator.

THE GEEK What elevator?

THE VOICE (O.S.) The elevator that does not exist. I'll give it to you straight Neon. The world You're living in is not the real world, but rather a computer generated dream world built by computers in the real real world.

THE GEEK Whoa. So where are you?

THE VOICE (O.S.) Right beside you.

MARPHEASS Come Neon. See for yourself.

THE GEEK But I have a dungeons and dragons game in five minutes

MARPHEASS Neon! Behind you!

(A man comes from the background and fires three shots at Neon. Neon bends back and dodges all three bullets. The man takes four more shots. Neon stops everything and puts it in slow motion. Neon picks a bullet out of the air and drops it.)

NEON I know kung fu

END OF MOVIE SEQUENCE 3

INT. COMPUTER ROOM. DAY.

BEN And there's some shocking twists, slow-motion bullets and fighting. And how about this for a title: "The Mad Tricks". Oh My God... How about dinosaurs?

START OF MOVIE SEQUENCE 4.

EXT. FIELD. DAY.

(One man sitting in a car. The man starts to drive. A cute dinosaur appears in the back of the car. The man tries to pet it, the dinosaur hisses at him. The man grabs the dinosaur and throws it out the window. The man starts to drive again. Suddenly a T-Rex chases the car for a short time. The man looks up and lets out a scream just as a dinosaur eats him.)

T-REX (British Accent) OH MY! Those humans do you give you the bloody heartburn. I’ ll grab one of my Rolaids.

T-REX drops his Rolaids

T-REX OH MY! Charlie could you pick that up for me.

(The other dinosaur hisses)

T-REX Well fine. I’ ll just grab another one.

END OF MOVIE SEQUENCE 4

BEN You know what that can’ t be any good. We’ d almost have to have 2 sequels to make any money off of it. How about I just do a slasher flick. I got a great idea...

START OF MOVIE SEQUENCE 5.

INT. HOUSE KITCHEN. NIGHT.

(A young teenage 'GIRL' is preparing a meal, when suddenly the phone rings. )

'GIRL' (Normal voice) Hello?

THE VOICE (O.S.) Hello Neon. I was wondering if you would like to know more about 'The Mad tricks'?

'GIRL' Who's Neon?

THE VOICE (O.S.) Oh. I'm sorry, I must have the wrong number. Excuse me.

(The 'Girl' hangs up and puts the phone back down on the table. Suddenly the phone rings again)

'GIRL' (Pleasantly) Hello?

GHOSTFACE Hello Sarah. Do you like scary movies?

‘ GIRL’ Who is this?

GHOSTFACE I can see you.

‘ GIRL’ Leave me alone you psycho!!

(She hangs up.)

(The doorbell rings right after SARAH hangs up the fun. SARAH answers the door and a man is standing there)

THE TERMINATOR Sarah Conner?

'GIRL' Yes.

(The Terminator cocks his gun and blows the 'Girl' away.)

TERMINATOR I was back

END OF MOVIE SEQUENCE 5.

Ben NO! NO! NO! NO! NOOO! Hey, why don't I leave this until tomorrow. I’ ll go get a bite to eat or something and forget about making a movie. Or what about a man trapped on a planet full of Apes. Nah... that one’ s already been done.

(Lights down)
```

---

## IC-1460: iWant Copyright 2008 by Mann Hoff

- Title: iWant Copyright 2008 by Mann Hoff
- Author (byline): Not specified
- Work: iWant Copyright 2008 by Mann Hoff
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: MOM
- Teaser before the introduction: No
- Spoken words (computed): 1443
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
iWant

Prologue Jessica: (Looking in at an iPod in a store) Oh my g-d, oh my g-d you guys, Look that iPod just became alive, and now it opened up another chapter in my life you guys, oh my g-d u guys (Like Legally Blonde the Musical)

Narrative
Jessica: I just fell in love with the most awesomest thingy-ma-bobber ever! The iPod. I’m
sure you heard of it, everyone has. I’m hoping my daddy will let me get one. We’re rich,
so I don’t think he’ll mind.
Reality
Jessica: Mom, can I have money for the mall
Mom: oh sure sweety, how much?
Jessica: Ummmm, $300.00.
Mom: Why do you need $300.00. Is it for drugs? I’ve always told you pot was bad. I kept
telling myself you listened as I talked. But I guess not. Gerald, we have a problem our
daughter is smoking weed.
Gerald: What’s the problem, we did it all the time in the seventies.
Mom: Yes, but that was when it was socially acceptable, now we can’t go on raising a
pot head now can we.
Jessica: MOM, DAD, I’m not getting pot.
Mom: Mj?
Jessica: No, I DON’T DO DRUGS.
Gerald: Are you gonna hire a homo to get you alcohol?

Mom: That’s hobo sweety pie, hobo
Jessica: NO, I JUST WANT AN iPOD!!!!!
Gerald: AN iPOD!!!!
Mom: NO.
Gerald: NO.
MOM: NO, (aside) I was hoping she’d ask us to get beer for a party, but an iPod. Oh my
goodness.
Gerald: You know we don’t allow anything with that apple on it, the only apples in this
house are the ones we eat. I mean honey, I am the CEO of Microsoft, the biggest arch
enemy of Apple. I can’t buy you anything from apple, but a Zune is fine, right?
Jessica: But daddy, you always get me what I want. All the cool kids have one. I thought
I was your little princess.
Gerald: You are my little princess.
Jessica: And I thought you never like to see me unhappy.
Gerald: I like seeing you sad. But I can’t change my mind.
Jessica: So then now I’m gonna be a loser, sit alone at the lunch table, and get picked on.
Thanks dad for making me a loser
Arnie: Yeah, ha ha ha, LOSER
Jessica: ARNIE, I thought you were at soccer.
Arnie: I quit so I could go to ballet class.
Jessica: And you say I’m a loser, THIS FAMILY IS SO WEIRD!!!!!

At starbucks with becky Jessica: Oh my god becky, you wouldn’t believe what my parents are doing. Becky: What?!?!

Jessica: One caramel macchiato with a little half and half. I want it iced and I want it
good. I want it with whipped cream and I want it with the chocolate syrup that makes it
look really cool. (To Becky) They won’t…… let me get……… an iPod!
Becky: No
Jessica: yes
Becky: No
Jessica: yes
Becky: O-M-F-G
Jessica: I know
Becky: You can’t be the only girl with out one, you’ll be a loser, an out cast, a ….
Jessica: Calm down, we just need to think of a way.
Becky: hmmm, nothing,
Jessica: I was dreading this but I might have to …. Get…. A… job.
Becky: but that’s social suicide
Jessica: I know, but it’s what has to be done.
Becky: There’s a paper, look for job listings.
Narrative
Jessica: As you see, my life has officially come to an end. I actually have to work. Ugh.
The thought alone makes me shiver. I mean, I’m usually one of those girls who gets
everything I would want with out a problem. I hope I could find a job that suits me.
Reality
Jessica: (reading the paper) Mom, What’s an ac-ro-bat?
Mom: I don’t know sweety, who do you think I am, a genie?
Gerald: That’s genius honey, does she think you’re a genius.
Mom: Oh, he’s right, how smart do you think I am?

Narrative
Jessica: Not very, well, anyway, I went to the tent where this job was and it looked cool.
There were funny people with red noses there. They had wigs on. I thought it was like a
show so I stayed to see if I liked it. Before I knew it I was on the tight rope, hoping I
wouldn’t die.
Reality
Jessica: Help, get me down, I want out, Ahhhh, help, please, somebody
Narrative
Jessica: then I fell
Reality
Jessica: Ahhhhhhhhhh (falling into a net)
Narrative
Jessica: Turns out an acrobat is someone in a circus. Ugh. I couldn’t stand heights and the
fall also wasn’t the biggest highlight, I mean, I broke a nail. Although, I did meet a cute
boy. He’s a clown in the circus, but without the make-up, he’s so hot!
Reality
Jessica: So Becky, the first job was a bust.
Becky: Oh, Hold on, let me just shut off my iPod. Okay, so, what’d you say?
Jessica: My job was too hard and…. Like…. bad.
Becky: OMG, I just remembered, my cousin is a big Hollywood producer. I might be
able to get you an audition.
Narrative
Jessica: So, I got the audition, but whether I got the part I wanted was a different story.
Another thing I didn’t know was that it was for a TV show and my audition was apart of
the show. The show was American Star. I’ve never seen it before.
Reality
Jessica: Hey, I’m gonna read a poem I wrote for you today
Simon: Okay great.
Jessica:
The Birds and the bees,
Don’t compare to your knees,
The light in your eye,
Reminds me of my mother’s pie,
(starts Singing)
Please, I miss you so,
I wish you, clown, would not go,
Please, I miss you now,
Can we have just one more pow wow
Randall: WOW
Slimon: You’ve made me reach a new disgust in the talent of Hollywood, You made me
want to vomit through my nose. Ugh, that was DREADFUL.
Pauly: Shut up Slimon, I thought it only sucked a little, but it was kinda cute.
Narrative
So that didn’t go so well. I wonder if it was the poem on a singing show or just the part
about my clown boyfriend. Whatever. They don’t need me or my talent. I’m just do good
for them. This is when I have to decide that it ‘s time to lower my standards on a job. I
have to do something normal, Not eccentric or stupid. Something safe, just to get me
money. Oh my gosh, I sound like a poor lady. Ahhhhh.
Reality
(check-out lady at stop and shop)
Jessica: Honey, you do not want that.
Customer: Excuse me
Jessica: That sour cream.
Customer: Why don’t I want that?
Jessica: Sorry, don’t mind me, I’m just thinking about those thighs.
Customer: How rude!
1 week later
Jessica: This is soooooo boring.

Check-out lady: Tell me about it. I’ve been doing this for 30 years. I just wanted that
Wurlitzer, but now those are out of style, so I got the cheaper thing, and iPod. They’re
AMAZING. But my thirty years only got me 2 iPods and 2 apartments, one in manhattan
and one here in California. You know those iPods are FANTASTICK
Jessica: I know.
Check-out lady: They are so cool and work so well. Also, my first one was pink so it goes
with so much of my wardrobe.
Jessica: I KNOW (getting mad)
Check-out lady: Jesse Louise
2 weeks later
(Jessica is reading a magazine)
Jessica: (Whistling)
Boss: Jessica stop slacking, get back to work!
Jessica: Okay, I can not deal with this anymore, I quit!
Narrative
Jessica: So that’s how I got the money. I made just enough in those 4 weeks of work at
the super market to get the iPod. I made that $300.00. I’m so happy. So Saturday, Becky
and I are going to the mall and getting the iPod Touch, the one that I want, Yay, I’m so
excited!
Reality
Becky: You did it, you finally got your iPod!
Jessica: I know, let’s try it out on your computer and download your music.
Becky: Sure
Jessica: Oh my g-d, it’s AMAZING! The sound quality is so good!
Becky: Yeah, Okay, so how much money do you have left from the jobs?
Jessica : $100.00, I didn’t know about the rebate before I started saving. So now we can
go back to the mall next Saturday.

Saturday Jessica: Becky Becky: Jess Jessica: No way Becky: After all that Jessica: After all the hard work Becky: A new iPod the next week! Jessica: I can’t believe this, and it says right there, no trade-ins, this sucks. Back to the supermarket. Nooooooooooo! Narrative Jessica: So just remember, hard work can only lead to one thing, having to work harder.
```

---

## IC-1461: May the Best Man Win

- Title: May the Best Man Win
- Author (byline): Max Alanson
- Work: May the Best Man Win
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1716
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
(Ben, a generic late 20-something year old man, walks towards the front door of his father’s house, guiding his girlfriend Amy towards the front door.)

Ben: Stop worrying, everything’s gonna be fine! Believe it or not, you’re the first girlfriend I’ve introduced to my dad since...well… Amy: ...Ever? Ben: Yeah. So, the bar is so low that it doesn’t even exist! Amy: Okay, I believe the part about you not having girlfriends, but I don’t know...It’s Thanksgiving! What if your dad hates me? Ben: He’s not going to hate you, just watch. A few minutes from now, I bet he’ll already be in love with you.

(He opens the door and calls out.) Ben: Dad! We're here!

(A loose pile jolts awake in a living room chair—it's Ben's dad.)
Dad: Huh? Who’s there?! Burglars?!
Ben: No dad, it’s me Ben! And my girlfriend Amy!
Amy: Hi Mr. Aldridge!
Dad: (waking up) You said...that...that that's...Amy? Oh god, what a disgusting name.
Ben: Dad!
Dad: Just kidding! It’s beautiful, just like you. (stands, now energetic) Hi, I’m Harry, welcome to my
humble abode...
Amy: Oh. Well, thank you! I don’t think it’s so humble. This is probably one of the better abodes I’ve
been in!

(Amy laughs. Dad picks up on it, even louder.) Dad: Oh Amy you are a real hoot. Come on in, take a seat! Close to me, please. (pulls a chair) There ya go.

(They all sit around the Thanksgiving dinner table.)
Ben: Wow Dad. You know, when we first came in here I thought you were gonna act all weird today, but-
-
Dad: What? Me? Weird? No, no no no, just wanted to play a little joke like I was all sleeping over there.
Nailed it. So, anyway, Amy...how long have you two been dating?
Amy: Oh. Well, I guess officially we’ve been together for...almost a year now?
Dad: I see, I see. And what is it that you do?
Amy: I'm actually a grad student, I'm in my first year of--
Dad: Wow, wow wow. That's so interesting. And did you know that Ben can’t bench press a hundred
pounds?
Ben: Uh…okay Dad, funny.
Dad: Because I can bench press at least like...a hundred and ten. So...
Amy: Um…I’m not sure I get what you’re getting at...
Dad: Does Ben even have a bench to press?
Ben: Dad, what are you doing?
Dad: (flexes) Come on. Look at that muscle and honestly say you wouldn’t rather be dating me.
Amy: Um…
Ben: DAD!

Dad: Eh? I mean, yeah. Amy: Well...you were right about your dad loving me!...

(Ben sits across from his spaced out friend Percival in Percy's living room.)

Ben: (mid-conversation) So, yeah. Do you think you could do that for me? I’m only in town for a few days and you’re one of the only people I’m still friends with. Plus I can’t really ask my dad because...uh, he’s got a bad back... Percival: Oh totally Ben-friend, I got’ch’er back! Ha, not your dad’s back though! Because you said that it is whack, so I don’t want his back.

(Percial initiates an intricate and bro-y handshake.) Ben: Oh! We’re doing this, okay…

(Doorbell.)
Percival: Whoa whoa bro, who’s at my do’?!
Dad: (entering) Knock knock my Brosef Stalins! What’s good in the hood!
Percival: Ah man, I’m all out of rhymes.
Ben: Dad??
Dad: Ooh, did I miss out on a handshake?! Let me get in on that goodness, yo! (he smacks his hands
wildly) Huh? YOLO swaaag, up-five!
Ben: High-five, Dad. It’s called a high-five, everybody who has ever existed knows--nevermind. What the
hell are you doing here?!
Dad: Whaaat? Why wouldn’t I be hanging out with my peeps! You’re my boys, ...boys! Chad, how are
things? Huh? Things be ballin, Chad?
Percival: My name is Percival, dude.
Dad: Oh...Alright, Percival. Good catchin’ up with ya. And now that we’ve played catch-up, why don’t
we play catch! Ben-jammin’, go deep!

(Dad pulls out a football, bounces around like he's Peyton Manning or something.) Ben: Dad, I’m 28 years old. I stopped going deep...forever ago. Dad: Oh. Well...think fast, butthead!

(He whips the football at Ben’s head.)
Ben: Ow! Did you just call me a butthead?!
Percival: Yo, what’s wrong with your dad though, brah?
Dad: Whoa. Percival. Not cool bro. Thought we were bros, bro.
Ben: Dad, Percival’s right! There’s something seriously wrong with you, and I say that completely out of
love. The kind of love that has experienced a lifetime of you trying to one-up me at everything I do!
Dad: What?! When have I ever done that!
Ben: Well, today. Twice, actually, and it’s not even four--
Dad: Okay, yeah, but...when else?!
Ben: Oh, I don’t know. How about, every day in elementary school…

(Flashback to a first grade classroom. A mustached teacher lifts a giant orange ball.) Teacher: Okay class, this is the sun. Ain’t that neat? Big ole’ ball of light that toasts us up like the fireplace of our solar system that we just wiggle our toes by on a cold winter’s eve. Now...Ben! Do you know exactly how the sun gets itself all hot and toasty?

Little Ben: Uhm...no.
Dad: (from nearby desk) HA! This idiot’s’ such an idiot, let’s all laugh at him! Hey, where's the idiot? Oh
look, look there he is! Found him! I found the idiot!
Little Ben: Dad?!
Dad: Whoa, don't call me that here. I don't want them to know we're related.
Little Ben: I...I...Why are you doing this to me?
Dad: Hey hey hey, whoa whoa. Whoa. Don’t blame me for you getting the question wrong.

(Back to the present...)
Ben: Remember?
Dad: Okay, yeah, sure, but that was one--
Ben: Or when I was taking my driving test…

(Flashback to teen Ben tightly gripping the steering wheel.) Ben: Alright. I’m taking a left turn at this intersection… Dad: (popping out) Backseat driver surprise!!!!

(Dad rips the steering wheel all the way to the right.) Ben: AH, Dad no we’re going to crash!!! Dad: But it'll be such a funny story!!!

(Back to the present.)
Ben: Then there was also that time--
Dad: Okay okay you can stop listing examples of awesome parenting. I mean, I know you’re not quite as
bright as me, but this theory of yours is just bull-noogy! That’s right, I said. Bull-noogy.
Ben: AghhhAHH! Look Dad, I need to be alone for a little while, okay? Please. Don’t follow me.
Dad: But…
Ben: Percival, meet you at that place for that thing we discussed?
Percival: Uh...what? Oh, yeah! You’re talking about when I’m going to help you pr--
Ben: Shhh, Percival!

(Ben storms out.) Dad: Thank god he's gone.

(Percival stares at him for a moment. Dad gets the hint, walks out.)

(Ben walks Amy along a trail next to a beautiful lake.)
Ben: Believe it or not, I caught my first fish right over there. Unfortunately, it also caught me. By the
shorts. And that was the day half the world saw my bottom half.
Amy: I’m surprised your dad didn’t try to out-flash you or something.
Ben: Oh...but he did. But. He did...
Amy: Hey...isn’t that your friend in the water? Uh...what’s his name?
Ben: Percival?!
Percival: Hey bro!

(We see Percival standing in water that doesn’t even go up to his waist.) Amy: It looks like he’s in trouble!

Percival: I uh, I need your help man! I’m going under, I can’t breathe, man!

(He slaps at the water, tries dipping his body under, does an overall poor job of pretending he's
drowning.)
Amy: Somebody save him!
Ben: Don’t worry Percival, I’m coming!

(Ben rushes, yanks him out of the lake and drags his heavy body onto the shore.)
Ben: Holy crap dude, stop eating so many Cheetos.
Percival: Never!
Amy: You saved him!
Ben: Yeah. And it was such a close call...
Amy: Oh wait, look! Something just fell off of him!
Ben: Yeah, I thought I saw something...let me see...oh. There it is.

(Ben kneels, finds the object. It's a ring case. He turns to face Amy on one knee.)
Ben: Amy Drackledorf-McHam....would you make me the happiest man in the world and be my--dad is
here?!?!
Dad: Yeah he is!
Ben: What the hell Dad?! How did you find me?!
Dad: Benjamin Rockem Sockem Smith, you are proposing to your girlfriend, do you think I would miss
this for the world?
Percival: (eating popcorn, watching excitedly) I know I wouldn’t!
Dad: See? Chad catches my drift.
Percival: My name’s Perciv--UGH!

(Percival gulps, but something's wrong. His throat is lodged! He grabs at it, screaming muffled,
unintelligible words.)
Amy: Oh my god, he’s choking! Somebody help!
Dad: I’ve got it I’ve got it, hold your horses. Now Percy, I’m gonna have to get uncomfortably close to
your backside for this…
Percival: MM?!?!
Dad: Come here Perce.. (gets in Heimlich formation) Releasing obstruction in three...two...one!

(With a big pull into Percy’s stomach, Percival coughs out a big lodged projectile.) Percy: Oh my god, thank you! Oh thank you thank you thank you! Bro for life, man! Bros for life!!!

(They perform and intricate handshake.)
Amy: Oh my gosh I can't believe you saved him!
Dad: Oh believe it pretty mama. Now, let’s just see what caused the problem…(looking) Oh. There it
is…funny, it was a ring!

(He kneels, turning to Amy with a ring in his hands.) Amy...ever since I met you earlier today, when my son brought you home, I haven’t been able to get you out of my mind. Would you do me the honors of becoming my wife? Please? (looks) Benjamin...why are you charging at me with that trash barrel raised above your head? Ben: (charging) AGHHH I’M GOING TO KILL YOU!!!

Amy: Wait wait stop! There’s got to be a more reasonable way to fix this without resorting to Donkey Kong levels of violence, okay? So just put down the barrel and talk to your father...(whispered) who clearly needs some help...

(Ben stops, reluctantly lowers the barrel.) Ben: Yeah, yeah you’re right. Look Dad...you can’t keep trying to steal my thunder with everything I do. This was supposed to be the happiest moment of my life and you just had to come in and take it for yourself. Dad: Oh Ben...Benny Ben Ben ben, I didn’t know you felt that way! I’m not trying to take your life, I’ve just been...I don’t know. I just wanted to be close to you. You know, you’re probably too young to remember it, but after your mother passed, well…I guess I got a little lonely. Pretty lonely, actually. I guess all these years I was just trying to show you that I could be just like you...maybe make you want to hang out with me more. Dumb, I know. So me, l.m.f.a.o.r.o.f.l.o.l. Ben: Aw, Dad, that’s not dumb at all. I’m sorry I didn’t realize. Look, let’s hang out more, okay? I’ll visit as much as I can. Dad: You mean it? Ben: Absolutely. And we can have our own secret handshakes too. Dad: Ooh, yes! What about this one, huh?

(Smacks Ben hard in the hands.)
Ben: OW! Stop!
Dad: Sorry!
Ben: And Dad, if you don’t mind…(turning) Amy…
Amy: Yes of course! Yes yes yes!!

(She flails, hugs Ben with unyielding excitement.)
Dad: I’m always the bridesmaid, never the bride.
Ben: Well Dad, I am gonna need a best man…
Percival: And I will gladly accept your generous nomination--
Ben: Percival. I want my dad to do it.
Percival: Oh. Okay then guess I drowned and choked for nothing!
Dad: You...you want, I...me...the best, of men…
Ben: So, what do you say?
Dad: I say...that means I must be better than you, so I’m the best. Thank you! I win.
Ben: It’s not a competition, Dad--
Dad: But I won? Or…
Ben: We won.

(They bump knuckles up, down,, finish the handshake with an explosion.) Dad: Bros for life? Ben: Bros for life.
```

---

## IC-1462: The Merchandise King

- Title: The Merchandise King
- Author (byline): Clyde Hendrickson
- Work: The Merchandise King
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2543
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
The Time: Present
The Place: An uncivilized savanna in Africa
Characters:
SIMBA. A young, naïve lion cub destined to one day rule the land.
DAD. Simba’s father, the current king.
MOM. Simba’s mother, the current queen.
SCAR. The evil uncle of Simba. He is determined to wrest control of the kingdom from his
brother.
RAFIKI. Crazy Buddhist monkey, adviser to Simba and Dad.
TIMON. A mongoose-like creature who lives outside of the kingdom.
PUMBA. Timon’s faithful warthog companion.
CHARLES. An exploited sea cucumber.
LAWYER. One of many who run wild in packs on the African plains.
RAPPER. Lays down phat beats.
ANTELOPE. An offstage rabble rouser.
STEVE IRWIN, CROCODILE HUNTER. Fearless Australian explorer.
WALT. Evil corporate tyrant and theme park builder.
WILL. Victimized playwright.
Various featured animals may or may not be included, such as the squirrel, the octopus, and
additional antelope.

Set: The play is designed to be carried out on a relatively empty stage. Different parts of the stage should represent different places. Anything which adds to the correlation between the play and a certain animated movie is encouraged. However, copyright laws are strict, so the ties must be loose. Amount of fake blood to be used is at the director’s discretion.

The Merchandise King Scar enters to make preshow announcement. SCAR. Oh, you all look like such delicious people! Good evening. I’m Scar, your evil villain and irresistible corporate sellout figure. Before we get started here tonight, there are a few things you need to be reminded of in the case of an emergency. If, for some awful reason, you spill the bootleg whiskey you smuggled past the minimum wage ushers, T-shirts can be purchased in the lobby. If you simply cannot bear to be without plush imitations of any of the adorable animals in tonight’s performance, dolls and stuffed animals can be found at Emergency Compulsion Aid Stands in the lobby. If the person next to you seems uninterested in buying any of our merchandise, feel free to beat them mercilessly until they do. Everything is priced exorbitantly, of course, because how else can you get that free market fix you so desperately crave? Food from the concourse shops must be purchased and eaten quickly, as all food inside the theater must come with a special pass, which can be obtained for a large premium. If you’re a big eater, as I see several of you are, we’ll be selling antelope ribs for 15 dollars per pound! Just kidding, we’d never sell them for less than twenty five. We will also stamp your hand for five dollars. This stamp does nothing but put the words “I am special” on your skin in a medieval gothic font, but I’m sure people will think you’re important anyway. And tonight, as a special treat for you, you can buy an actual piece of Walt Disney’s frozen skin from our ice cream vendors. Now, you may find it suspicious that we have 37 square miles of old Walt to sell, but let me assure you: he was indeed larger than life. Well, it looks like our performers are ready to come on, so without further ado, I give you the awesome, expensive spectacle that is The Merchandise King. (Begins to walk off, stops.) Oh, Sir? Excuse me, it looks like your wallet is too fat for theater regulations. You’re going have to empty most of it into my paws. It’s for everyone’s safety, especially if you consider me buying a third house in Barbados essential to your safety. GUY. Not really SCAR. (pulling gun) Oh believe me, it is. (Guy in audience empties bills, credit cards.) Thank you, and enjoy the show. Imitation of Lion King music, “The Circle of Life,” begins. Interrupted by DJ scratching. RAPPER. (To the tune of Paul Revere by the Beastie Boys) Now here's a little story that I've got to tell, About one bad lion you know so well. It started way back in history, With Scar, Simba, and his mommy and his daddy. Then Disney got the rights and it all went bad, Soon Pumba’s pushing Wendy’s and Simba’s in an Apple ad. Yeah so we’re here to straighten out all this messed up crap

THE MERCHANDISE KING In a simian satire and a bad rhino rap.

(spoken) Word to your herd, fool.

(lights fade from RAPPER. SIMBA and DAD enter from right.)
SIMBA. Dad?
DAD. Yes, Simba?
SIMBA. We lions rule over all the animals, right?
DAD. Yes, my son, the lions rule over all the animals of the pridelands, from the
mightiest elephant to the tiniest grasshopper.
SIMBA. Even the African clicking squirrels?

(squirrel appears) DAD. Yes, son, even the African clicking squirrels. SIMBA. And the octopus?

(octopus appears) DAD. Oh yes. SIMBA. Including Uncle Feelyhands?

(octopus pretends to feel someone up with tentacles)
DAD. Even him, son.
SIMBA. But…but what about the antelope?
DAD. Well, of course the lions rule over the antelope.
SIMBA. But don't we eat the antelope?
DAD. Yes, and that is the circle of life. Kinda brings a tear to your eye, doesn't it?
SIMBA. But dad, my best friend Jeffrey is an antelope.
DAD. (nervous) Oh, don't worry, I'm sure he'll be fine.
SIMBA. Okay. Say, speaking of which, can I go over to Jeffrey's to play?

THE MERCHANDISE KING

DAD. Of course. Oh, but be sure to ask your mother first.
SIMBA. Okay. (walks) Hey mom, can I go over to Jeffrey's to play?
MOM. No!
SIMBA. Why not?
MOM. Cause I ate him.
SIMBA. (disturbed) Oh, okay.
DAD. Gee, that's too bad, son. I know, why don't we go for a walk around the kingdom.
I'm sure that'll cheer you up. (they walk). Oh look son, a horde of lawyers! You know, we
never did get an ok for this satire. Why don’t you go ask them about it?
SIMBA. Ok, pops. Uhm, excuse me, Mr. Lawyer Esquire Sir?
LAWYER. Yes, how may I extort AHEM help you today?
SIMBA. Yeah we’re doing this satire, and we want to know if it’s legal. (hands over
script)
LAWYER. Ok… (takes script) What’s this a satire of?
SIMBA. A Disney movie.
LAWYER. (suddenly desperate, high pitched) A Disney movie?!
SIMBA. Yeah, why are you so scared?
LAWYER. Have you ever been beaten by a six-foot-tall man in a mouse suit?
SIMBA. No…
LAWYER. Have you ever been dragged across a briar patch by seven doped up elves?
SIMBA. Well, I can’t say that I have…
LAWYER. Have you ever been tied to a chair and forced to listen to Angela Lansbury
sing for hours on end about being her guest?
SIMBA. No…

THE MERCHANDISE KING
LAWYER. (quiet, intense) Keep in mind that Angela Lansbury is dressed like a dancing
teapot.
SIMBA. Uh..
LAWYER. (in Simba’s face, loud) A teapot!
SIMBA. Ahhhh! (runs away).
DAD. What’d they say, my little yellow rutabaga?
SIMBA. They said, uhm… They said… They said that it was such a good idea, Angela
Lansbury would sing about it!
DAD. Excellent. Let’s continue our walk. Oh, look, the Sea Cucumber Tank!
SIMBA. Why do we have sea cucumbers in the savana?
DAD. Oh, it’s not that unusual. Why don’t you ask Charles over there?
CHARLES. Hello, I’m Charles the… (sigh) sea cucumber.
SIMBA. Charles? That’s an odd name for a sticky urchin.
CHARLES. Well, gotta relate to the little kids somehow. Now, if you’ll excuse me, I
have to stick to your leg.
SIMBA. Ahh… Ahhh! Get off my leg! (tries to shake him off)
CHARLES. No, I’m afraid non-toxic mucus squirting is just one of my many gimmicks.
SIMBA. You were created just for gimmicks?
CHARLES. Yes. I can’t wait to be mass-produced and covered with suction cups.
SIMBA. Wow, I didn’t know my kingdom was so capitalist.
CHARLES. You haven’t seen anything yet. Ok, now I have to slug off to my next
victim… or perhaps an actual ocean.
SIMBA. Good luck Charles! I promise, when I’m king, your life will have meaning!
DAD. Did you learn something, son?
SIMBA. Well…

THE MERCHANDISE KING
DAD. Good! Well, here we are in this narrow, secluded valley with no hopes of escape.
Why look, here comes a herd of antelope. They must want to greet us.
SIMBA. Gee, I dunno, dad. They look like they're coming at us pretty fast.
DAD. Um... yeah, you guys might want to slow down just... a... little...
ANTELOPE. Down with the bourgeois lion oppressors!

(Sounds of antelopes charging grow louder. Lights fade as they reach the lions. When they have passed, the lights come up again, and SIMBA is alone.) SIMBA. Dad! No! Ooh... Ow... (flinches and wipes blood off) Geez... (during the next lines, Simba looks at many different spots, obviously conveying the fact that his dad is in many different pieces.) Dad are you? Dad… oh no dad… Dad are you ok? (Scar appears from behind him) SCAR. Hello, Simba. SIMBA. Oh, hi Uncle Scar. I'm sure that despite your obviously evil name and appearance that you're really a good guy. SCAR. ...Right. Simba, you killed your father. SIMBA. Um... but what about the antelope? SCAR. Shut up! If you don't get out of here you'll be... shot dead by evil German poachers.. Now go! Now, you miserable little prairie rat! SIMBA. Okay, fine, I wouldn’t want to have to talk to any Germans, I guess. (runs) Geez, this really sucks. I guess it’s a necessary plot development (stops) Oh, hi there. TIMON. Hey there, man, I'm Timon. (takes sip from a flask) SIMBA. Hi, Timon, I'm Simba. TIMON. And this is Pumba.

(PUMBA snarls)
SIMBA. Agh! Heh.. heh.. hi, Pumba. You guys must make excellent plush toys… I
mean, uh, supporting characters.
TIMON. You got it, dude.
SIMBA. Say, what's that you're holding, Timon?

THE MERCHANDISE KING

TIMON. This? This is... uh... hakuna matata! Here, (offers flask) try some.
SIMBA. My dad told me not to take things from strangers, but, he’s dead. Okay. (takes
sip from flask) Wow! This is better than sniffing zebra dung! Dad? (SIMBA has seen his
father in a hallucination)
DAD. Simba.
SIMBA. Hi dad! (waves energetically)
DAD. Luke, I am your father.
SIMBA. Uh...
DAD. This is CNN.
SIMBA. Okay...
DAD. Simba, you must return to the pridelands to avenge my murder at the hands of
your Uncle Scar.
SIMBA. But... but didn't the antelope...
DAD. Quiet! Along the way you will meet a monkey who is insane. He will guide you
on your quest. Goodbye, my son.
SIMBA. Wait! Dad, before you go there's something I want to tell you.
DAD. What is that, my son?
SIMBA. Mom already knows.
DAD. I’m your father, Simba. Tell me.
SIMBA. Well... Dad... I'm gay.
DAD. (pauses) That’s cool. But you still have to kill your uncle.
SIMBA. Oh, okay. Bye dad! (waves energetically) Okay, I'm pumped. I'm gonna kick
Scar's ass. I'm gonna...
RAFIKI. Hello, Simba! I am Rafiki!
SIMBA. Oh, hi, you must be the monkey my dad told me abou... (he is hit) Ow! You hit
me!

THE MERCHANDISE KING

RAFIKI. Rafiki test Simba! SIMBA. Ok, what do I have to do? RAFIKI. See funny man over there? SIMBA. Where? STEVE IRWIN, CROCODILE HUNTER. Oh my goodness! We are right here in the lion’s den, with no medical help in sight. I have covered myself in bloody elk meat, in order to attract as many of the ferocious cats as possible! Let me reinforce again that I am in no real danger. RAFIKI. Simba, where is killer instinct? SIMBA. I dunno, I’ve never liked hurting people. All those guts are kinda mushy and ucky. RAFIKI. Simba a wuss then? SIMBA. I think it has something to do with my mother eating all my best friends when I was young. RAFIKI. Whine whine. Let me dial whine one one for freaking whambulance. Child abuse is lame excuse! Kill the silly Australian! SIMBA. Well, here it goes nothing… (leaps at him). STEVE IRWIN, CROCODILE HUNTER. I am in absolutely nooooooh! My legs! I’m being ruthlessly devoured! My liver is lying exposed on the hard jungle floor. But folks, I am not in any danger of physical harm. SIMBA. Mmmm… Tastes like egret. (attacks again) STEVE IRWIN, CROCODILE HUNTER. Let’s see if the little bugger will let me pet him… Oh god, my hand! My hand has been chewed off like a kitty’s play toy! Now the beast is batting my stomach and intestines as if they were a ball and string! But I remind you that I will be completely ok…. (dies). SIMBA. That was relieving. What’s next? RAFIKI. Most important lesson. Look over there! SIMBA. (Looks away from Rafiki) Where?

THE MERCHANDISE KING

(Rafiki laughs maniacally, beats Simba with cane) SIMBA. Ooh, eeh, ow, eeh, ooh. (rubs head in daze) Geez... (feels pocket) he took my wallet. Ooh... I've gotta get that jerk. That's it! That's the monkey's lesson! I've gotta get that jerk, Scar. That’s a pretty vengeful lesson. I guess the other lesson is “never trust a monkey with a stick.” Come on, Timon! Come on, Pumba! We're gonna get my uncle! (runs, arrives at prideland) Gee, that was fast and convenient. Wow, that's a lot of hyenas! TIMON. Come on, Pumba, let's get them! SIMBA. Yeah! Go Timon! Go Pumba! Beat those... Ooh.. Ow... (flinches and wipes blood off) Geez... Heh... heh... this might be harder (undergoes puberty, voice gets much deeper) than I... Wow! I just went through puberty! These hyenas have got nothing on me. Growl. Grr. (kicks hyena butt) Hey ladies, wanna stroke this mane? SCAR. So, Simba, you have returned as I knew you would: hairy and strangely arousing. SIMBA. Yeah, and I'm here to end your evil rule, Scar. Lions and inferior hyenas should be segregated! Hmmm, that doesn’t sound so good when you say it out loud. Whatever, prepare to die. SCAR. Wait! Before we battle there is something I must tell you. I am not your Uncle Scar, (removes mask) I am Ulysses S. Grant, Commander of the Northern Army. SIMBA. You might have been a good general, Ulysses (bites Scar in “nads”), but you were a terrible President. SCAR. Ooh! There goes the Union. (dies) SIMBA. (young voice) Yeah! I did it! I beat the bad guy! I saved the day! I... I... I regressed through puberty. DAD. Simba, you have avenged my death. Thanks. I may now ascend into heaven. SIMBA. Gee, this plot sounds familiar. Only in what I'm thinking of, I should die in the end. WILL. Darn straight it soundeth familiar. I’m William Shakespeare, and this is the exact plot of my play Hamlet, evil uncle and all. Give me backeth my script. WALT. Not so fast, Shakespeare, I bought the rights to you fair and square. WILL. Walt Disney! Oh Anne, how couldest thou sellest me outeth?

THE MERCHANDISE KING
WALT. In fact, I may even swing you around my head as a plaything, if I choose. It says
here right in my contract.
LAWYER. That’s correct sir.
WALT. Quiet you, or it’ll be Lansbury and Robin Williams next time.

(LAWYER cringes) WILL. Only a beast as foul as you, Disney, could make me sayeth “eth” after all my verbs henceforth. How cheesy thou art. WALT. Now, I take great pleasure in ending this story… MY story… myself. Come here, Will. I shall now wield you as a saber. (throws WILL over shoulder, wields leg or arm as a saber) WILL. Careful! That doth be my writing hand. WALT. Now Simba, will you return to the cheap, commercial script my writers have contrived? SIMBA. No. I stand by my beliefs, and I will rule this jungle with a pansy paw of whiny justice. WALT. Then I shall beat you all the way back to the magical kingdom! (begins to beat SIMBA with Shakespeare-saber) SIMBA. Oh dearest me… there go my principles… If only I wasn’t voiced by a 13- year-old prepubescent weakling like Jonathan Taylor Thomas! WALT. When I’m through with you, you’ll think you’ve gone back to the land before time! (finishes killing him) Well, that does it. Come on Will, we’ve got a space-based musical with dancing donkeys to write. WILL. Can Anthony Hopkins play the lovelorn donkey herder? WALT. I’m sorry, Mark Wahlberg is already onboard. WILL. Oh, the dramatic irony… (they leave). RAFIKI. Well I guess we learned an important lesson today, kids: Somewhere, Walt Disney’s cryogenically frozen head is trying to take over the world… and you’ve got to stop him. (Begins to sing). It’s the circle… SIMBA. I’m still alive…

THE MERCHANDISE KING

(RAFIKI hits SIMBA with the stick.) RAFIKI. (still singing) …the circle of life! SIMBA. Ooh...
```

---

## IC-1463: Not specified

- Title: Not specified
- Author (byline): Not specified
- Work: Not specified
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1579
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
A New Leash on Life

Scene One

(Scene opens up on Dad, at home, calling for Kevin to go to school)
Dad: Kevin, hurry! Or else you'll be late to school!
Kevin: (Behind the stage) Im coming Dad! Just have to grab my backpack! (Runs on stage, Jacket in hand and
backpack on his back)Im so excited for school today! We have a guest speaker! He is a Scientist! Thats so cool,
right dad?
Dad: (Not really paying attention) Yeah, sure Kevin.
Kevin: Then there's a contest, and whoever wins gets to help him in his lab! I really want to win!
Dad: (Still not paying attention) I'm sure you will.
Kevin: Alright, I love you Dad!
Dad: (Not hearing Kevin) Yeah
Kevin: Bye Dad!

(Lights out)

Scene Two

(Lights on a classroom, there are a few students in desks There are three students watching from where children are
sitting. They are talking loudly between eachother)
Teacher: Alright kids, settle down, settle down. It is now time for today’s lesson! (Teacher is talking about a
complete nonsense topic...LIKE CALCULUS!)
Kevin: Guys! I heard that a SCIENTIST is coming to talk to us! Isn’t that really cool!!!
Chad: I don’t know Kevin... I like astronauts better...
Alexis: KEVIN! YOU ARE RIGHT! I want to be a scientist when I grow up!
Kevin: Me too!
Chad: Actually guys...I want to be an astronaut...
Alexis: NO WAY CHAD! SCIENTISTS RULE!
Teacher: All right class, and now it is the moment you are all waiting for!! Our Guest speaker! Dr. Madd! The
Scientist!

(The children whoop and holler... Whatever that means...Dr. Madd enters the stage, and starts talking to the
children)
Dr: Hello children! I, am Dr. Madd. I work in a beautiful lab, with test-tubes and beakers. I, however, need help with
my newest experiment! So we will have a class drawing to find who shall assist me in my experiments!! (Draws
name) and it is...(Dramatic Pause)...KEVIN!(Kevin cheers and goes to the front of the room) Today after school,
you shall assist me in creating, a new breed of dog!
Kevin: I LOVE DOGS!
Dr: Yes you will, Muahahahahahahahhaha! (Dr.Madd Leaves)
Teacher: Congratulations Kevin Now back to our lesson children! (Kevin returns to his desk)
Alexis:OH MY GOSH YOU WON! Im so jealous of you right now! You get to go help a SCIENTIST!
Chad: My Dad is bringing me to space camp...
Kevin: I know Alexis! Im so excited! I wish that you could come with though...
Alexis: Me too! I love dogs! I wonder how Dr. Madd is going to do it!
Kevin: Me too!
Chad: I’m more of a cat person....
Both: Be quiet Chad!

(Bell Goes off, children rush to get going) Teacher: (Calling after the kids, following them behind the curtain) Alright children, that is all for today’s lesson, your homework for tonight is page 54 in your green book. Have a great rest of your day, and I will see you all tomorrow.

(Lights Down)

Scene 3

(Lights up on laboratory, beakers on table filled with mysterious liquid. Mysterious Machine in the back of room) Dr: Kevin, this is my laboratory! I create experiments! Would you like to help me create the new type of dog?

Kevin: Yes sir! Dr: Well this is paws-itivly exciting. Here, step into this large and scary-looking machine. It is indeed terrier-fying isn't it? Alright, now that you are inside the machine, Ill just makes some changes (Touches the dials, and moves some levers) Are you ready Kevin? Kevin: Not really...I’m kinda scared... Dr: Its okay, you really don’t have a choice, muhahahahaha! (Pushes button, machine starts, Spins, then ends) Its finished! It has worked! I have successfully turned a human into...A DOG! Muhahahahhahah! You can say, that you really have gone to the dogs. (Laughs) (Kevin, with dog ears, and some other form of costuming, stumbles out of the machine) Kevin: Man, that was ruff...what happened? Dr: You are the first human to be successfully turned into a dog, and still be able to speak, or I should say...Bark, English! Kevin: What's going to happen to me? Dr: I have invited someone to come and see you...Come in!! Dad: (cant see his "son" even though he is right in front of him.) Kevin? Dr.Madd where is my son. Dr.: Why he is right in front of your nose. Dad: Doggone it...Doesn't that kid know that it is rude to play hide and seek in someone else's laboratory... Kevin: Dad!!! I'm right here! Dad: What is that dog mutt-ering about? Also, Dogs can’t talk! What’s going on!? (sudden realization) KEVIN!!? Dr.: Well, it seems that my machine has broken-down and I can’t turn you back Kevin! Looks like you will have to live out the rest of your days...in a collar!! Muhahaha! Dad: Please Doctor, I cant go out into public with a son... that also happens to be a dog! Dr: Well! That’s too bad now isn’t it! Now leave! Before I sick the hounds on you! (Kevin and Dad leave as quickly as possible, as Dr. Madd chases them.)

Scene 4: The Park

(Kevin and his father are sitting on a park bench with a few trees around them for scenery)
Dad: Kevin, what are we going to do!?
Kevin: I don't know Dad! We need to figure out how to get back to Dr. Madd’s Lab! And then try to fix his
machine. Can we play fetch? It helps me think...
Dad: Uh...Sure Son. (Throws ball to his son)
Kevin: (Chews on Ball) Wait! I think I got it! Dad, I know how to work with machines, Ive always wanted to be a
scientist!
Dad: You’ve wanted to be a scientist?
Kevin: Yeah! Haven’t you ever noticed?
Dad: Well...Uh, not really...
Kevin: But I think that if we got into the Doctors lab, I could fix the machine and turn myself back into a human.
Dad: But Kevin, you don’t have thumbs...
Kevin: I can make it work Dad!
Dad: But Kevin...
Kevin: Dad it has to be done!
Dad: But what happens if it doesnt work?
Kevin: Well. That’s just a risk that we’ll have to take...but how are we going to get in... (Thinks for a moment) IVE
GOT IT! (Takes out Whiteboard) We can sneak in through one of his windows, you have to stall the hounds. We
can stop by the store and buy some steaks. The steaks will distract them long enough for them to consume the sleep
medicine that we will inject into the meat. Once the hounds are in a deep slumber, we will open the disable the laser
beams that protect the machine by sneaking in ninja style, and pressing the big red button on the side wall. Once the
laserbeams are disabled we will need to block the door behind us by moving some furniture, this is so the doctor
cant sneak up on us while Im fixing the machine!
Dad: Wow. Thats a great idea Kevin!
Kevin: Thanks Dad. Now lets do this!!!

Scene 5: Back to the Lab

(Back in the Lab) Kevin: Im glad that plan worked Dad! Dad: Me too son! Now quickly fix the machine! I’ll move some of this furniture so Dr. Madd cant get in!

Kevin:Okay Dad! (Kevin begins to work on the machine fixing wires and such. Dad moves all the furniture against the door. Then, all of a sudden they can hear Dr. Madd coming) Dr: Puddles! Poogle! Where are you? Ive been looking for you everywhere! Are you in the Lab? Because you know that I have always said that you cant be in there!!! (Tries to open door) Hey! What is happening! Who is in my lab!? Puddles, Poogle! Dont worry! Daddy is coming!!! (Steps running off) Dad: Hurry Kevin! We don’t have much time! Kevin: I’m almost done! Just stall him for a few seconds longer. Dad: Okay son. I believe in you.

(All of a sudden, The Doctor appears with a shrink ray in hand, he blasts the door open. finally revealing Kevin and his Father.) Dr: Ahh. I see. You have come to put things “right”? Well maybe a taste from this shrink ray will teach you. Dad: Wait no! (Stalling) If you shrink us, who will see the proof that you, Dr. Madd, are the genius that turned my son into a dog? Dr: Hmmmm... You have a point there... Kevin: Dad! I fixed the machine! I can turn myself back! Dr: Haha! Freeze! (Changes the setting from Shrink to Freeze, and Shoots Kevin) Well, now that my machine is finally fixed I think that you should step into the machine! (Points gun at the father) Dad: Wait, you dont know what you are doing! Dr: Of course not! I am MAD after all! (Shoves Dad into the machine and turns it on, turning dad into a dog) My second experiment is complete! Muahahaha! Now nothing will stop me from creating the perfect world! Only me, and dogs, forever! I must go inform the Great League of Elite Evilists! Puddles, Poogle, meet your new friends!

(Unfreezes Kevin)
Dad: No! Please turn us back! (Dr. Madd Exits)
Kevin: Now what do we do Dad?
Dad: I don’t know son (Growling and Barking from P and P) Uh-oh I think we have company...
Pugs: Do you smell that Poodle? Smells like...Fresh Meat.
Poods: Yeah Boss, Fresh Meat.
Dad: I do not know who you are, but I can guarantee that we are not dog food.
Pugs: Well you sure look like it, don’t they Poodles.
Poods: Yeah, they sure do boss. Can I have the first nibble?
Pugs: No Poodles, I always get first nibs.
Poods: Oh yeah, sorry boss.
Kevin: Wait why do you want eat us?
Poods: Because our Master told us, we always do what Master tells us!
Kevin: Yeah, but why? I mean, he gets you to do all the mean jobs, he isnt treating you right in my opinion.
Pugs: What are you saying kid?
Kevin: Well, if I were you, I would try not listening to him and do what you want!
Poods: He has a point boss.
Pugs: Yeah I hear him. I want to give our master a piece of my mind. (Begins to bark)
Dr: Puggles! Whats wrong? Daddy is on a very important phone call! (Barking Continues) Fine I’m coming, I’m
coming! What wrong!? Is it the prisoners?
Pugs: (barks and bites Dr. Madd)
Poodles: (bites Dr. Madd as well)
Dr. Madd: (Screams)
Dad: Quick Kevin! Schnauz-our Chance! (Kevin and Dad get into the machine and press the button.)

(Kevin and Dad walk out of the machine, normal)
Dr: Oohhhhh nooooo!!!!! (Falls into the machine, which starts up again)
Kevin: Dad! We did it! Im normal again!
Dad: Thats right son. We did do it.
Kevin: Where is Dr. Madd?
Dr. Madd: Ruff. (Is chased by Pugs and Poods)
Dad: Lets just say that he will have his nose in the dirt for awhile. Come on Son. Lets go home.

Scene 6: Back to School

(Back to original school positions) Alexis: Hey Kevin how was working with the scientist?? I bet it was fun?

Chad: Yeah, way cool! I want to be a scientist now! Kevin: Not really guys...It was nothing that I expected. I dont think that I ever want to go through that ever again! I think...I would rather be an astronaut.

(Teacher recieves a note.) Teacher: Kevin, your father is here to see you. (The kids in the room snicker as Dad enters the room) Dad: Kevin, you forgot your lunch at home! Kevin: Oh! Thanks Dad. You can go now... Dad: Not quite (Gives Kevin a Hug) Im proud of you son, Ill see you when you get home, and then maybe... we can play some catch.

~FIN
```

---

## IC-1464: PHYSICALLY IMPOSSIBLE The Keisha Story Copyright 2009 by Josh Cohen

- Title: PHYSICALLY IMPOSSIBLE The Keisha Story Copyright 2009 by Josh Cohen
- Author (byline): Not specified
- Work: PHYSICALLY IMPOSSIBLE The Keisha Story Copyright 2009 by Josh Cohen
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2169
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
Narrator: It’s a spring Saturday morning as Keisha slowly stirs from her night’s sleep. The birds are

aflutter and the flowers are in bloom as they were the day before, and as they’d be the

day after. But while the world would remain largely the same, Keisha’s life would never

be the same.

(Keisha wakes up and yawns, not yet aware of what has happened to her overnight.) Narrator: She tries to pull off her blanket, but she can’t. She tries to open the window to see the

birds aflutter and the flowers in bloom, but she can’t. What could the problem be? Keisha: Well, this is very peculiar. Narrator: Very peculiar indeed. Keisha senses something is wrong, but she can’t put her finger on

what. In fact, it doesn’t seem as if she has a finger to put on anything, for that matter. She

can’t even manage to scratch her head and wonder. Keisha: What could be wrong?

(Keisha is pondering when she glances down and realizes the problem.) Narrator: And that’s when it hits her. Keisha: Why, I don’t have any arms! What am I going to do?

Narrator: What indeed. And this is where Keisha’s fascinating story begins, a story we hear far too

rarely: how a perpetual optimist awakens to discover she has lost both of her arms.

(Singing) Keisha, she’s so thoughtful, Keisha, she’s got charm. Keisha, the optimistic girl

with no arms Narrator: It’s now Monday morning, and Keisha is getting ready for her first day of school. Word

gets around fast in Smalltown, Nebraska, and the news of Keisha’s condition has spread.

This week is a big week for Keisha. She has an English paper due Friday, the same day as

the big state championship soccer match and the Spring Dance. Smalltown High is very

concerned about all of this. Mr. Cohen: How is Keisha going to finish her English paper without any arms? I don’t have it in me

to fail someone as thoughtful and optimistic as she is. Coach: How is Keisha gonna play in the game Friday night? This is our first chance to win

States, and now our all-state goalie has no arms! She’s led this team here, but I can’t let

her play.
Lindsay: Tom, are you really taking Keisha to the Spring Dance?
Tom: I don’t know, Lindsay. I mean, I really like her, but-
Lindsay: (Grabbing Tom’s face) Tom, look at me. She’s a no-armed freak! Do you know what

she’d do for your reputation? Tom: Well… I… Yeah, I guess you’re right. Narrator: Yes, it’s going to be a difficult week for Keisha, a week she won’t soon forget. The

trouble starts in Mr. Cohen’s English class. Mr. Cohen: Keisha, you didn’t really participate at all in class today. You usually always have

something very thoughtful to contribute to the class. Keisha: I’m sorry, Mr. Cohen. I really wanted to, but you never called on me. Mr. Cohen: Well maybe if you raised your- (Realizes what he’s about to say) never mind that. I just

wanted to tell you that I talked to the English chairman, and I’m not allowed to give you

any preferential treatment, regardless of your… um… capabilities. So you’ll still have to

turn in your paper this Friday. Keisha: I understand, Mr. Cohen. I don’t want to be treated any differently now than I was before. Mr. Cohen: Don’t get me wrong, I really fought for you, but the chairman tends to be very heavy-

handed- ugh, I’m sorry, Keisha, I mean there’s really nothing I can do; he’s twisting my

arm on this one- dammit, you know what I’m trying to say.

Narrator: It looks like Keisha’s not going to get any slack on her English paper. And soccer

practice won’t be any better.
Lindsay: Keisha? What are you doing here? You don’t play soccer.
Keisha: What do you mean? I’m the goalie. I’ve been the goalie all year.
Lindsay: Oh, sorry, two-armed Keisha played goalie. No-armed Keisha has no place on this team.
Keisha: You’re the most hurtful person I’ve ever met, Lindsay. How can you judge me like that?

I’m still the same Keisha. Lindsay: Psh, please. You’re a couple of limbs short of being the same Keisha. We’d be better off

having Nelson Mandela in goal. Keisha: I… wait, I don’t get it. Lindsay: It doesn’t matter whether you get it or not, you don’t have any arms. Tell you what,

Keisha, raise your hand if you think you can still play goalie. Keisha: I… you… bitch… Lindsay: My, we don’t have a very optimistic outlook, now do we? Coach, did you hear that?

Keisha doesn’t think she can still play goalie. Coach: Keisha, I can’t discriminate against you because of your… um… condition, but if you

don’t have faith and optimism in yourself, then I can’t in good conscience let you play. Keisha: Coach, you can’t do this to me. I’m an all-state goalie. You can’t take this away from me. Lindsay: Oh, sorry, Keisha, but his hands are tied. You’re just not the same Keisha. Keisha: You know what? Fine. (Keisha storms off) Lindsay: Freak.

Narrator: Things are bad for Keisha, real bad. She had never been faced with such harsh

discrimination before. And with nowhere to turn, Keisha did the only thing she could

think of: she sat down on the curb and started to cry.
Heroin Joe: Keisha, what’s the matter?
Keisha: Oh, hey Heroin Joe. It’s nothing. Don’t worry about it.
Heroin Joe: You know you can talk to me about anything. Come on, tell me.
Keisha: Well, ever since I lost my arms, people have been treating me as if I was a different

person. No one thinks I’m thoughtful or optimistic anymore. They don’t see Keisha, they

just see a no-armed freak.
Heroin Joe: Well, do you still feel thoughtful and optimistic?
Keisha: I… I don’t know anymore.
Heroin Joe: Keisha, not many people know this, but before I was known as Heroin Joe, I was world-

renowned for my studies on the true effects of illegal drugs on people. But then there was

a shortage of willing research participants, so I had to test the heroin on the one person

who would allow it: myself. I developed an addiction, and now I’m Heroin Joe. Keisha: That’s awful, Joe, but I don’t see what this has to do with me. Heroin Joe: I’m getting to that. When you make the jump from respected scientist to heroin addict,

people begin to look at you differently. Because how can a drug addict still have a

brilliant mind? But between you and me, I still sneak into my old lab and do experiments,

and I just got some work published under the name Chester A. Arthur. Keisha: Your pseudonym is the name of a former president? Heroin Joe: Never mind the pseudonym. The point is that I don’t let people tell me who I am. You

say you’re still the same Keisha, then be the same thoughtful, optimistic Keisha. Keisha: Yeah, but what if I don’t feel very optimistic about people right now?

Heroin Joe: Don’t worry about people, Keisha. There’s some bad ones, but the good ones will do the

right thing in the end.

(Tom enters, looking a slightly nervous, but not in a way that shows any nerves about Keisha’s lack of
arms.)
Tom: Hey, Keisha, where were you today? I didn’t get to see you at school.
Keisha: Oh, hey Tom, sorry. It’s been a pretty weird day for me.
Tom: So… you want to go to the Spring Dance with me Friday?
Keisha: Sure, I’d love to.
Tom: Great, it’s gonna be a blast.

(Tom exits, leaving only Keisha and Heroin Joe.)
Heroin Joe: See? Just give people a chance, and they’ll do the right thing.
Keisha: Thanks, Heroin Joe.
Heroin Joe: Anytime, Keisha. Now if you’ll excuse me, I have to go pass out in that dumpster.
Narrator: That pep talk from Joe was exactly what Keisha needed. She had the confidence to be

Keisha again, and that meant winning back her position as goalie of the soccer team.

Tuesday’s soccer practice was the beginning of a fresh start for her. Keisha: Coach, I’m the goalie that got us to the championship game, and I’m the goalie that’s the

best bet to win States. I’m still Keisha, just give me a chance to prove it. Coach: Hmm, well you definitely seem to have regained your optimism since yesterday. Alright,

let’s give you a workout just to be sure. Lindsay, come here please. Lindsay: What’s up, Coach? (Noticing Keisha) Ew, what’s that doing back here? Keisha: My name is Keisha, and I’m the Smalltown High starting goalie.

Coach: Lindsay, I’m gonna set up a few balls, just take some shots at Keisha, give her a workout. Lindsay: Will do, Coach. (Under her breath, to Keisha) Let’s see what you can do, freak.

(Keisha prepares for the shot. Lindsay shoots at the top corner of the net, but Keisha manages to jump and
deflect the shot with her head. Lindsay is stunned and Keisha dizzy, but both shake themselves out of it.
Lindsay tries another shot high with the same result. Finally, Lindsay kicks the ball with all her might, and
Keisha kicks the ball right back, hitting Lindsay in the face.)
Lindsay: Ow, my nose! I think it’s broken.
Coach: Yep, that’s our Keisha. And she’s ready.
Lindsay: Will someone help me?
Keisha: You know I’m ready.
Lindsay: I hate you all. (Lindsay runs off, clutching her nose)
Coach: Keisha, I want to work with you all day, every day this week. You’re definitely ready to

play, but we need to be sure that you’re ready to win. Keisha: I’d love to Coach, but Mr. Cohen already said there’s no way I can get out of doing my

English paper by Friday.

(Flashback to Heroin Joe.) Heroin Joe: Just give people a chance, and they’ll do the right thing.

(End Flashback.) Keisha: You know what, I think I’ll go ask Mr. Cohen again. Narrator: Keisha sure hopes Heroin Joe knew what he was talking about, or there was no chance

she’d get to play. But fortunately for her, Heroin Joe was just as wise as he was

intelligent.

Keisha: Mr. Cohen, can I talk to you for a minute? Mr. Cohen: Yes, Keisha, I was meaning to talk to you. Shut the door, would you? (Beat) Actually, I’ll

get it. Keisha: (Closing the door with her foot) It’s ok, Mr. Cohen, I can handle it. What did you want to

talk to me about? Mr. Cohen: Keisha, your coach called and told me that you were still playing goalie this Friday. Is

this true? Keisha: Yes, but I won’t have time to write your paper and prepare for the game. Mr. Cohen: That’s what I wanted to talk to you about. Keisha, I’ll be blunt. Your story is remarkable,

and if you win this game Friday, it will be the stuff that books get written about. I can see

it now: Girl overcomes lack of arms to lead team to victory. It’s Physically Impossible:

The Keisha Story. You win that game, you let me write your story, you get an A on your

paper. Keisha: Don’t worry Mr. Cohen, we’ll win. But what about the chairman? Mr. Cohen: Keisha, if I can write this book, you won’t see me teaching anymore. It’ll be all book

tours and a villa in the wine country from here on out. Narrator: And just like that, everything seems to be going Keisha’s way. After spending the rest of

the week practicing, it was time for the moment of truth: the state championship game. Chip: Hello, and this is Chip Lafferty coming to you with live coverage of this year’s Nebraska

Girl’s Soccer High School Championship. With me as always is my color commentator,

Heroin Joe. Heroin Joe: Good to be here, Chip. The story of tonight’s match has been the goalkeeping. After 90

minutes of regulation and an overtime period, the score is still tied 0-0.

Chip: As per Nebraska State soccer rules, we now go to a sudden death penalty shootout.

Smalltown High came into the season with the better record and will shoot first.

Smalltown’s best scorer, Lindsay, will step up to take the shot, broken nose and all.

(Lindsay shoots at the top corner of the net. The ball gets past the outstretched arms of the opposing goalie.) Chip: And she scores! Smalltown now leads 1-0 in the shootout. Heroin Joe: It’s all up to Keisha now. If she stops this shot, the game is over and Smalltown wins. Chip: Right you are, Joe. The small town of Smalltown’s hopes are riding on the thoughtful,

optimistic girl with no arms. Coach: (To himself) Come on, Keisha, you’ve been working all week for this. You can do this. Mr. Cohen: (To himself) Come on, Keisha, this is the only way I can pass you. You have to do this. Keisha: (Sighs and prepares for the shot) I can do this.

(The opposing player shoots at the same spot Lindsay did at practice, and once again, Keisha manages to
deflect the ball with her head.)
Coach: Yes!
Keisha: (Still dizzy from the save) I did it!
Mr. Cohen: Hello, wine country.
Chip: And she’s done it! Keisha stops the penalty shot to preserve the shutout and the state

championship! She is truly the most valuable player of this game, and a heroine to all of

Smalltown. Heroin Joe: Heroin? Where’d you see heroin? Chip: Not the drug, you deadbeat, it’s a female hero. And who let a drug addict be my color

commentator anyway?

Heroin Joe: Hey, I know my girl’s high school soccer. And you can’t talk to me like that, I’m Chester

A. Arthur. Narrator: And such ends Keisha’s long week and all of its twists and turns. Later tonight, Tom will

escort Keisha to the Spring Dance, he in a tuxedo and she in a sleeveless dress. And no

one will make a joke about this, because everyone knows she’s still the same old Keisha.

(Singing) Keisha, she’s so thoughtful, Keisha, she’s got charm. Keisha, the optimistic girl

with no arms.
```

---

## IC-1465: Rhymes with Orange Copyright 2007 by Lauren Bouchard.

- Title: Rhymes with Orange Copyright 2007 by Lauren Bouchard.
- Author (byline): Lauren Bouchard
- Work: Rhymes with Orange Copyright 2007 by Lauren Bouchard.
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1454
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
Fay
Roses are red
Dandelions are orange
I think you’re special
Sometimes I …porange…sporange…rorange… (crumples paper)
Red fish
Blue Fish
One fish
Orange fish…one fish…Hornage fish corn fish… (crumples paper)
Gahhh!!!!

Hello I say. My name is Fay. I like to write and rhyme all day. You could say I’m odd or slightly daffy or simply filled up on sugary taffy. But this is normal speech for me. This is all that I can be. Because as a poet with OCD I like to rhyme all things I see. This leaves me in quite a bind as my other obsession leaves some people blind. It’s the color of happiness, the sun, and (beat) construction cones, I’m almost quite sure it goes straight down into my bones. But enough with this chatter I have to leave the house in quite a clatter… I’m late for work you see at the Orange Julius is where I’ll be!

Narrator Here we observe Fay in her natural environment. The Orange Julius. She has to work there on the side because her career as a poet isn’t exactly flourishing. Not until she can find that magical “orange-rhyming” word. She can’t write a decent poem until she can get that out of her mind. The Orange Julius was the only habitat that was semi-compatible with Fay’s temperament. Her interaction causes disarray and hostility with other organisms.

Fay Here’s your change sir, have a nice night! I hope you’ll come back again for a bite!

Man …yeah whatever freak…

Fay Can I help the next customer purchase their needs? With every purchase of 10 dollars or more there’s a free pair of orange beads!

Woman Yeaahh Hi. Can I get uh...um… uh… what’s good here?

Fay Well our Original Orange smoothie is one to please the orange Julius was named after it in the 1920’s!

Woman Mm…nah. I want something fruitier. Strawberry mango tango sounds good doesn’t it?

Fay
Blegh!! Heck no! That’s terrible. I wouldn’t come here for something so spar able. The
orange is much better you really must try if you don’t order the orange smoothie I’ll tell you
goodbye.

Woman Fine! I’m just going across the way to Smoothie King!

Fay
That woman was negative…I didn’t like her one bit I didn’t expect her to throw such a fit!
(looking around) The Business is slow today…I can’t imagine why if people don’t start
coming I might start to cry! Oh I guess I can work on some poetry as long as no customers
come hungry. Orange-zornage-gornage…

Narrator
Fay was upsetting the food court smoothie business. If the Orange Julius had any chance
of surviving in the dog eat dog world that was the Ryland Mall food court, her behavior had
to change. Here we see the manager enter her precarious habitat.

Manager Um…Fay can I talk to you a bit?

Fay Of course we can talk I’m working for you! Please let me know if there’s anything I can do.

Manager Oh well…about that. Well we’re losing a lot of customers to the Smoothie King there yonder…maybe you can start suggesting other food items to the customers?

Fay
Well you see sir, I thought we could chat about the products and Smoothie King and this
and that. Our products are lousy we could really use flair compared to their new drinks our
cupboards look bare!

Manager
(Slightly annoyed) Fay I have no control over what they sell at the smoothie king. All I know
is that we need to start selling more than plain old Original Orange smoothies. What about
our special edition Tropical smoothies?

Fay But sir Original Orange is the only product we have really worth selling the rest of those drinks are for show and telling.

Manager (Angry) Listen Fay last time I looked my name badge said man-a-ger. And that means you do what I say when I say it.

Fay
(Under-breath) Wow, I’m surprised you can see it over your oversized chin…hah that’s
funny…makes me grin. (Sarcastically) Alright Mr. Manager I heard you loud and clear. Ya
know, if he wants to sell more drinks he should start selling beer. I’ll get right on it sir! As
fast as I can! Some one should really hit him over the head with an iron pan.

Narrator
As we can see Fay was awfully upset by the manager’s inability to understand her
predicament. As she sulks about her recent encounter, her mood is worsened by a rival
from across the food court.

Fay Oh my gosh a smoothie king guy is coming over right now…he better be careful I might have a cow!

Felix Hi….i’m Felix I work right over there, at the smoothie king?

Fay (coldly) Hi…can I get you something to drink? A smoothie to please? …and by the way with every purchase of ten dollars you get a free pair of orange beads…

Felix Well uh…I didn’t come over to get a smoothie…I mean I’m around them all the time…you just looked sort of lonely over here…how bout some coffee later? When do you get off?

Fay …Coffee? Why would I want that!? Not with a guy who looks like a rat!

Felix
Ouch! I wondered why no one came over here…but now it makes sense…I’m glad I didn’t
make the mistake of actually go on a date with you! That would be so embarrassing! I can’t
wait till this place goes out of business!!

Fay
Gawd…what a jerk! No wonder it must be a smoothie king perk! Gosh talk about rude…that
really put me in quite a bad mood. Bad mood…no customer… perfect time for a break! One
time when I can enjoy my own orange shake! (pantomime drink) Mmm…this is luscious it’s
just a luxury…it reminds me of (breaking into song) O- IS FOR THE ONLY COLOR I LOVE!
R-is for the dreamy richness from above! AAAAAAAAAAA--Oh we have a customer!
(Slightly embarrassed) Can I offer you a ora—(remembering) something new to excite? We
have yummy tropical smoothies that will tickle your senses and put you on a mini vacation
for very small expenses.

Old Woman No thank you dear, I think I’ll just take an original orange Julius.

Fay Well maam, would you say you are a true orange devotee? Considering your orange smoothie affinity?

Old Woman Well…I would say that I like the flavor of orange…I grew up on South Broadway where I tried the original…these remind me of my childhood… (Trailing off)

Fay Yeah yeah lady I hate to disagree but I have an important question that’s been bothering me. If you’re not too old to answer this tell me it now give me a word that rhymes with…

With…

With…

Give me a word that rhymes with…how the sun sets softly on the eastern corral…

Old Woman (Confused) On the eastern corral?

Fay Well…what I mean to say is the color it makes…it’s also the color that macaroni and cheese bakes…

Old Woman If I’m not mistaken macaroni and cheese is yellow…

Fay (Patronizing) No ma’am you’re wrong. It doesn’t bake yellow that’s the stupidest answer! I’d only accept it from a blind fellow!

Old Woman That’s ridiculous. My orthopedist says I’m twenty-twenty. But where is the eastern corral?

Fay No maam! You see that’s a metaphor I used! I’m trying to convey to you with out being abused!

Old Woman Just ask me the question, and give me my smoothie. I bet they don’t give you such a test at the smoothie king!

Fay A TEST?! YOU’RE THE ONE THAT’S BEING A PEST! I’M TRYING TO EXPLAIN MY BEST SO I SUGGEST YOU GIVE IT A REST! I’M MERELY TRYING TO ASK THIS TIME ABOUT A WORD THAT WOULD RHYME WITHOUT HAVING TO MIME ABOUT THE COLOR THAT IS MOST SUBLIME!!

Old Woman

(More confused) What?

Fay (About to explode) Give me a word that rhymes with…uh…WITH WITH A WORD THAT RHYMES WITH…WITH…WITH ORANGE!!!!

Narrator She slammed her head against the cash register and on the ground she lay still…the little old lady took her smoothie and ran off without paying the bill.(surprised) It was chaos at the Orange Julius without her running the line. Later she awoke, took a look around and realized that she was fine! (cover mouth) She no longer had the urge to rhyme in every way. A blessing in disguise is what the doctors (apprehensive) say. So now Fay has a nice apartment on South Broadway where she sits and writes her remarkable poetry to pass the day (reluctant) away. But of course, she still visits the Orange Julius at least four times a day.

(Sighs from the realization that he has caught the rhyming bug)
```

---

## IC-1466: SESAME : life on the street Text copyright 2008 Andrew Messer.

- Title: SESAME : life on the street Text copyright 2008 Andrew Messer.
- Author (byline): Not specified
- Work: SESAME : life on the street Text copyright 2008 Andrew Messer.
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: SESAME, B.B, BB, B.B.
- Teaser before the introduction: No
- Spoken words (computed): 1354
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
SESAME : life on the street

Detective: I had just wrapped up a long day at the office when my secretary, Doris, came in…

Doris: Sir, you have a phone call.

Det: …and told me I had a phone call.

Doris: Yes, sir…you do…line four, and he said it was urgent.

Det: Right. (phone) Hello? Yes. Murder you say? And where are you? I’ll be right there! (hangs up) This night was about to get a lot more interesting. I quickly grabbed my hat, said goodnight to Doris…

Doris: Goodnight, sir!

Det: Goodnight, Doris.

Doris: (same inflection, but more confused) Goodnight, sir!

Det: And I went for the door. But the hallway was full of coats.

Doris: Sir, why are you in the closet?

Det: I’m…not in the closet, Doris. (slowly closing door) Right. Doris, can you tell me how to get…

Doris: How to get to?

Det: Sesame Street.

Det: The caller had said to meet right here, at the corner of Sesame Street and Avenue Q. It turns out my client was a bird. A…big…bird…

Big Bird: That’s right… Let’s get out of the light, I’m trying to keep a low profile…

Det: Good luck with that. So you told me there’s been a murder?

B.B: Yeah, up the street (motion with beak) I’d take you all the way to the body, but there are police officers and news reporters everywhere…

Kermit: This is Kermit the Frog here with a Sesame Street News Flash. We’re here live on the scene of a horrific murder. It seems the body of long time resident Snuffalupagus has been found in an alley off Sesame Street. The police are actively searching for winged suspects with bright yellow feathers, as bright yellow feathers were found near the body. Due to this feather threat, the Sesame Street Terror Threat Level has been elevated to Fuschia, as it appears that this bird flew. Bird flu? AHHH!

Det: So that’s why you called me. And you didn’t do it?

B.B: Of course not! Snuffy was my best friend! I was molting when I found his body this morning…you have to help me find out who killed him so I can clear my name and solve Snuffy’s murder!

Det: Well, when was the last time you saw Mr. Snuffalupagus…alive?

B.B: Last night…he said he had a birthday surprise for Elmo.

Det: Well, then…it’s off to Elmo’s. (Elmo plays with tickle me elmo dolls, rips the head off one)

Elmo: Stupid doll… (knocks)

Elmo: Hello? Who is it?

B.B: It’s me, Elmo! Big Bird!

Elmo: Just a minute! (hides doll, goes to door) Hi! What’s wrong, Big Bird?

B.B: Snuffy’s dead.

Elmo: Oh no…Elmo sad!

Det: Technically, Elmo, that sentence needs a verb. It would be Elmo is sad... You know what, nevermind... Did you see Snuffy last night?

Elmo: No…but when Oscar wished me a happy birthday he said he thought Snuffy’s surprise was stupid. I didn’t know what he meant.

B.B: Maybe we should go talk to Oscar.

Det: Oh, well then we’re sorry to have bothered you and your, ah…dolls. Bye now!

Oscar: (opens can lid) Ugh. (closes lid)

B.B: Oscar, wake up!

Oscar: Ugh, what do you want? You’re not here to evict me, are you?

B.B: We don’t want your can, Oscar! Snuffy’s dead!

Kermit: This is Kermit the Frog here with another Sesame Street News Flash on the scene of the murder of Snuffalupagus. The police have just released information stating that a mashed piece of birthday cake and several candles were found near the body. Due to this baked good threat, the Sesame Street Terror Threat Level has been elevated to Neon Goldenrod.

Det: Look, we need to get moving on this. Tell us what we wanna know, grouch, or it’s the trash compactor for you!

Oscar: Agh. Fine. I saw him last night. He was carrying a lopsided, smelly cake cut into a lot of slices, he said it was a surprise for Elmo.

Det: Oh? How many slices?

Oscar: Definitely more than three...

Det: How can you be so sure?

Oscar: Because that’s as high as I can count...

B.B: I know someone who can help us with numbers!

Det: Lead the way, birdie!

Count: HA, HA, HAAA….Big Bird! And a friend! One! Two!

B.B: Hi, Count.

Det: Count, we have a few questions for you.

Count: Ah, a few? Is that two? Three? Two-thousand four-hundred and ninety-six?

B.B: (whispers) We don’t have two-thousand four-hundred and ninety-six questions, do we?

Det: No, Birdie, we don’t. We have two.

Count: Ah, two. One. Two.

Det: That’s right. First, did you see Mr. Snuffalupagus last night?

Count: Ah, yes. He had a cake cut into many slices. I helped him count the slices!

Det: I see. And how many slices were there?

Count: Thirty-six. One. Two. Three.

BB: Just use a calculator, Count, it’s much faster...

Count: I can’t afford educational technology...ha ha ha. Oh no! I lost count! One... two...

Det: Thirty six pieces of birthday cake? Birdie, I think the count just solved our case... it’s back to Elmo’s!

B.B: Wait, you think Elmo killed Snuffy?!

Det: Run with me on this one. (they start running) You heard the Count... there were 36 slices of cake...

B.B: Yeah? So?

Det: But there were only 35 at the scene of the crime... I think Elmo killed Snuffy, ditched the body along with the cake, but couldn’t resist having a slice first...

B.B: But why?

Det: Because everybody loves cake...

B.B: No, I mean why would Elmo kill Snuffy?

Det: That’s what we’re about to find out. (stops running, opens door)

Det: Start talking, Elmo! You did see Snuffy last night, didn’t you?!

Elmo: Elmo doesn’t know what you’re talking about! Elmo didn’t see Snuffy or eat his cake!

Det: Oh? Then how’d you know there was a cake?

Elmo: A lucky guess?

Det: I think that cake tickled your fancy, just like those little red dolls...

Elmo: These dolls are stupid! Come on, Tickle Me Elmo? Whose brilliant idea was that? Did anybody ever ask Elmo if he liked being tickled? No... but if you rip the stuffing out there is a lot of space inside and the dogs can only smell the fur... uh oh...

Det: Toss me one of those dolls, Birdie! ‘Tickle Me Elmo, Tickle Me Elmo’ (sfx) (rips doll’s head off, tastes contents) This is pure Colombian!

B.B.: WHAT?!

Det: You know, Bogota Bang Bang, Amazon Angeldust, Shanghai Susan, the Devil’s Dandruff…

B.B.: Yes, I know what you meant! I was saying “what” to express shock and horror!

Det: I think Snuffy walked in on your little operation and had to be silenced! You’ve been caught red-handed, Elmo! Why’d you do it?

Elmo: ARRRGHH! I thought it was the feds and I just started shooting!

Det: I mean why’d you start smuggling the Chippy Chum?

Elmo: Ever since they started cutting the funding for PBS, Elmo’s been struggling just to get by... we all have! Take a look around this street! Bad housing, bad schools, no jobs and no hope... it’s like the people on Easy Street forgot about Sesame Street...

Det: You make a point, Elmo... it shouldn’t take a murder for us to see the poverty right in front of our eyes. But that doesn’t justify what you did to Snuffy... you took a life, Elmo... and now you have to face the consequences.

Elmo: No, I won’t! Freeze, detective! You, too, Big Bird! (pointing gun)

Kermit: This is Kermit the Frog here with another Sesame Street News Flash. We’re here (gulps and looks around) live on the scene of a hostage situation. It seems the Snuffalupagus killer has taken hostages on Sesame Street! Due to this tense situation, the Sesame Street Terror Threat Level has been elevated to Ultra Bright Neon Green! (looks down) Uh oh!

Det: Hey, can we have a little help here, Kermit?!

Elmo: Hold it right there, frog! (turns his head)

Det: Tickle his feet, Birdie! (tickles)

B.B: This one’s for Snuffy! (kung fu tickle)

Elmo: Okay, okay! Elmo surrenders!!!! (handcuffs)

Det: I walked back into the office full of confidence after solving the case...

Doris: Sir! You solved the case?!

Det: Hey Doris, I solved the case!

Doris: Yes sir, you just... nevermind. Oh, by the way, you have a call holding.

Det: Brick Laine, private eye. Breaking and entering? In your neighborhood? And the name? Rogers? I’ll be right there. (hangs up) Doris, get me a cardigan, I’m goin’ undercover.
```

---

## IC-1467: Single White Female A Play by Kaitlin McCoshen

- Title: Single White Female A Play by Kaitlin McCoshen
- Author (byline): Kaitlin McCoshen
- Work: Single White Female A Play by Kaitlin McCoshen
- Publisher: Mushroom Cloud Press
- Publication date as stated: 2013
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1234
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
Single White Female by Kaitlin McCoshen

(Sarah is in a coffee shop alone; Craig comes over and sits down next to her)
Craig: *slicks back hair* Hi.
Sarah: Umm...hello?
Craig: I’m Craig.
Sarah: Craig?
Craig: Yeah! Craig from Craigslist!
Sarah: Oh, so you like invented Craigslist?
Craig: No of course not.
Sarah: ...alright I’m sorry Craig I don’t mean to be rude but I’m kind of in the middle of my
morning routine and-
Craig: Oh so does that mean you come here often?
Sarah: Yes I come here everyday that’s what a routine is Craig.
Craig: Well, your ad didn’t say you were this rude!
Sarah: ...What ad?
Craig: *hands her the ad* the ad you put of yourself on Craigslist!
Sarah: *reads off of paper* “Single White Female ready to mingle”?
Craig: I’m sorry obviously you didn’t write this yourself.
Sarah: No it’s fine you wouldn’t have known.
Craig: She did tell me to meet her here though, I wonder if she’s around.
Sarah: Careful it might not be a she.
Craig: *awkward laugh* True. Well I think I’m going to head out, here’s my number just in case
anyone stops by for me. *hands her his number*
Sarah: Thanks I’ll keep an eye out I guess. *drinks coffee*
Ursula: OMG ISN’T HE PERFECT.
Sarah: Who are you??

Ursula: I’m Ursula.
Sarah: Oh you poor unfortunate soul...wait are you the person that used my picture on
Craigslist?
Ursula: Yes.
Sarah: You aren’t even going to deny it.
Ursula: No, you’re pretty and I want a boyfriend.
Sarah: That doesn’t give you the right to use someone else’s picture... Ursula how did you get
my picture?
Ursula: Well I’ve been stalking you! And I see that you come here every day and when my ad
wasn’t working out, I decided to take a picture of you instead! And then that MAN
responded...Craig.
Sarah: Ok, well...you know that’s not what dating is all about, dating is about being yourself,
and finding someone who really appreciates you for you, and you know it’s probably not
because of your picture. You really aren’t that ugly.
Ursula: My name is Ursula and I look like a troll.
Sarah: No...It’s probably because of some of the things you wrote about yourself in this ad!
Ursula: What do you mean? My personality is flawless.
Sarah: You wrote about how you consumed 34 sloppy joes in 10 minutes, to win a competition.
Ursula: Well I hear that competition is important in relationships.
Sarah: You also wrote about how you have a foot fetish?
Ursula: It told me to list my interests!
Sarah: You also wrote about how you like to braid your back hair?!
Ursula: Well everyone has passions.
Sarah: Ok...Ursula...I’m sorry but I really don’t know what you want from me-
Ursula: You got his number didn’t you?
Sarah: Well, I guess.
Ursula: Then you can call him.
Sarah: What?

Ursula: And you can make him love me!
Sarah: You’re crazy!
Ursula: Crazy....IN LOVE.
Sarah: Alright... you know what fine. I will call him. *picks up phone and begins calling him*
Craig? It’s Sarah from the ad. Listen I just met the crazy. Yes it’s a she. Alright i’ll see you then.
Ursula: WHAT DID HE SAY? WHAT DID THE ANGEL SAY? WILL HE PUT A RING ON IT?
Sarah: Excuse me?
Ursula: IF HE LIKED IT THEN HE SHOULD HAVE PUT A RING ON IT, IF HE LIKED IT THEN HE
SHOULD HAVE PUT A RING ON IT WAOOO O O
Sarah: ...don’t do that. Listen, I’m going to meet up with him tonight.
Ursula: ...you? Not...me?
Sarah: It’s only going to be for a few minutes, I’m just going to tell him to give you a shot.
Ursula: Yes. My loins are blazing for him.
Sarah: good one. Here! I have an idea how about you come over later tonight, and I can try to
give you a new look and who knows? Maybe then Craig will see the real you!
Ursula: Yes! This is the best day ever!
Sarah: Here let me write down my address!
Ursula: No need!

LATER THAT NIGHT
Ursula: I’m here, and I’m ready to be beautiful.
Sarah: Hi, Ursula, here sit down and we can start.
Ursula: This will be the greatest makeover montage in history! Way better than Anne
Hathaway’s in the Princess Diaries.
Sarah: What?
Ursula: Well all they did was take off her glasses.

Sarah: I meant about the montage.
Ursula: Yeah! I’m going to try on a bunch of your clothes while upbeat music plays in the
background right?
Sarah: No. Honestly Ursula, I was just going to shave your back hair.
Ursula: NOT MY BABIES...well...if you must...go ahead...
Sarah: *lifts shirt* DEAR LORD URSULA
Ursula: Yeah I know...you might need an electric razor...
Sarah: *takes out electric razor* Jesus take the wheel *begins shaving*
Ursula: THE BREEZE THE BEAUTIFUL BREEZE
Sarah: *stops shaving* Ok...I think that’s enough for tonight.
Ursula: *picks up mirror* WHERE’S JAMES BLUNT TO TELL ME I'M BEAUTIFUL
Sarah: Ok I need to go meet Craig. I will try my best Ursula.
Ursula: My body is a wonderland.
Sarah: That makes one of us.

THE NEXT DAY
Ursula: So!?! When’s the wedding?
Sarah: Hi, Ursula.
Ursula: I ALREADY PICKED THE DATE. July 10th, a summer wedding. Did you know July 10th is
Tom Hanks’ birthday and well, we’ve both been in love with volleyballs.
Sarah: Ursula, I really don’t think it’s going to happen.
Ursula: Oh I should have known he probably burns so easily, well I guess we can wait until the
fall-
Sarah: WE MADE OUT.
Ursula: does he have a large tongue? He looks like a man that would have a large tongue.
Sarah: Excuse me!

Ursula: What? I’m just trying to make sure all the bases are covered. Literally.
Sarah: Ok, you know what Ursula this is what you deserve.
Ursula: What do you mean?
Sarah: You can’t just use someone else’s picture online!
Ursula: Yes I can and I’m going to keep using your picture until I get a boyfriend!
Sarah: It’s ILLEGAL.
Craig: Ladies!
Sarah: Craig?
Ursula: Speak my love speak!
Craig: I am not your love.
Ursula: What?
Craig: Well I could have been, if you had only been yourself instead of using someone else’s
picture online.
Ursula: Are you saying that if I had used my own picture, you would have been my boyfriend?
Craig: Well probably not. But this isn’t how a real relationship starts. I know it might seem like
just a picture, but how can you expect someone to meet the real you if you don't show them? A
real relationship is built off of trust, and if you try to start with a lie it will never work.
Ursula: Really?
Craig: That and it’s illegal.
Ursula: I’ve never thought about it like that. You know what? I want my future man to love me;
actually I want him to love all of me...literally.
Craig: Go home Ursula, make your own ad I’m sure it will work out for you this time.
Sarah: Craig you don’t know if it will work out for her.
Craig: Oh trust me it will.
Sarah: Why do you say that?
Craig: *hands Sarah a picture* I told my friend to check her out.
Sarah: Oh...”Single Male looking for troll-like woman with a foot fetish”... Perfect.
```

---

## IC-1468: i Snow White Gucci Stiletto and the a play by B. L. Houchen

- Title: i Snow White Gucci Stiletto and the a play by B. L. Houchen
- Author (byline): Not specified
- Work: i Snow White Gucci Stiletto and the a play by B. L. Houchen
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: TIME, PLACE, SETTING
- Teaser before the introduction: No
- Spoken words (computed): 2050
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
ii

Cast of Characters

VOICE . . . . . . . . . . Narrator

SNOW WHITE . . . Young Woman, 20s

CAT . . . . . . . . . . . . Carnie, 20s

MAN . . . . . . . . . . . .Salesman, 30s

PAULINE PETER . .Saleswoman, 30s

CINDY . . . . . . . . . . .Young Woman, 20s

TIME: Spring, afternoon.

PLACE: The Land of the Never Ending Where Rhymes of People That Never End Live in the Never Ending Land, and later, Cindy’s front yard.

SETTING: The downstage is an empty area used for the scenes between Snow White and Voice. The upstage area is first a carnival, and later, a very typical suburban home.

Snow White and the Gucci Stiletto

(At rise, stereotypical fairy tale music plays. The curtain remains closed. There is a low, ominous voice, much like a cross between James Earl Jones and Michael Clark Duncan.)

VOICE

(reading from script, OS) Once upon a time, in a land not so far, far away, there lived a princess named Snow White (pause, music fades) for she was albino.

(Enter SNOW WHITE. She pops her head out from the middle of the curtain.)

SNOW WHITE

(a childish voice, to audience) Hel-lo!

(SNOW WHITE walks to C. She is in her twenties and wearing a skirt and a white blouse. She smiles a big overly cheerful smile. She physically reacts to everything VOICE is saying.)

VOICE Snow White lived in a castle with her mother, the Queen, until one day, the evil-lazy-eyed-double-double-toil-and-trouble-yet-oddly-arousing Queen had a nervous breakdown and started to do mean things to her daughter.

SNOW WHITE

(up and out over the audience, to voice) Nuh-uh.

VOICE Yes, huh.

SNOW WHITE She wouldn’t. She loves me.

VOICE Nope, she’s mean. Who do you think killed your pony?

(SNOW WHITE gasps.)

The Queen ordered Snow White to leave the castle forever.

SNOW WHITE But I have nowhere to go.

VOICE Get over it kid.

(SNOW WHITE scowls “at” VOICE and starts trudging stage R.)

She walked for a while, but (realizing what SNOW WHITE said is in his script) Snow White didn’t have anywhere to go.

SNOW WHITE Told you so.

VOICE Ah, shut it!

(SNOW WHITE, startled, turns and starts walking back across the stage.)

After a while, she met some short guys with adjectives for names. She told them she had run away, and they allowed her to live in their quaint three bedroom dwelling on the upper-east side as the maid.

(SNOW WHITE gets down on her hands and knees and mimes scrubbing the floor.)

Day in and day out, it was the same routine: scrub the floors, do the laundry, clean the stepstool in front of the toilet, wash the windows . . .

(SNOW WHITE stands and mimes washing the windows.)

Three months later she decided she had had enough.

SNOW WHITE

(throwing down her “rag”) I’ve had enough!

(SNOW WHITE mimes opening the window)

VOICE She decided to sneak out –

(SNOW WHITE crawls out onto the ground. *Sound effects of the VOICE turning a page of the script.*)

of their third story apartment.

(SNOW WHITE looks down, shrieks, and mimes falling, or mimes falling and yelling “Nooooo” in slow motion.)

VOICE Luckily, she fell into the arms of Prince Charming, who had been climbing the fire escape ladder to peep in her window late at night for his own auto erotic pleasure. They fell in love, got married, and moved to Beverly Hills. After three years of marital bliss, they were named Fairy Tale Weekly’s Most Beautiful Couple.

(SNOW WHITE strikes a few poses.)

Prince decided to become an actor and made a movie with Rumpelstiltskin. He fell in love with him after correctly guessing his name, came out of the closet, and ditched Snow White.

SNOW WHITE I was thrown to the way-side faster than a fried chicken wing by Nicole Richey . . .

VOICE Natura-

SNOW WHITE . . . or Lindsey Lohan . . . or Calista Flockhart . . .

VOICE

(pause) Are you done -

SNOW WHITE . . . or the Olsen twins . . . or Misha Barton . . .

VOICE Finished?

SNOW WHITE . . . or Jack Sprat.

VOICE Naturally, she wanted to get even with Prince Charming, so she quit taking her Midol, waited twenty-eight days, then huffed and puffed and blew his house down. Snow White did not want to die an old maid and end up as a card game. She vowed that she would find her one true love. So, she got a Botox injection and went on her way. She traveled for hours and hours. She hadn’t packed a lunch so she snacked on a trail of breadcrumbs.

SNOW WHITE

(eating a crumb, to herself) Euh . . . Stale.

(SNOW WHITE walks back and forth across the stage.)

VOICE The sun beat down on her . . . the wind made her weary . . . and she stepped in a dog turd. (SNOW WHITE scowls at VOICE.) Finally, she was so exhausted she felt she could not take another step. Then she saw it: The Land of the Never Ending Where Rhymes of People That Never End Live in the Never Ending . . . Land . . . which, ironically enough, slightly resembled Beaver City, Nebraska.

(The “Hallelujah Chorus” plays as the curtain starts to rise. SNOW WHITE turns upstage. The set is a carnival in the town. There are four booths. First, is a pumpkin booth with a woman inside a pumpkin behind the counter. She could be wearing a pumpkin Halloween costume. Her sign reads “PAULINE PETER’S PUNKINS.” Next to it is a booth with small vials of colorful liquid. The vendor is MAN, wearing a suit and tie. His sign reads “W.O.O.L.” The next booth has five children sitting at it, with one plump, overweight woman. Her sign reads: “KIDS” Throughout the following a customer will choose a kid and walk offstage with him/her. Lastly, is a booth with a man/woman in a cat suit with a fiddle. In front of each booth is a bale of hay for customers to sit on. There are a few customers wandering from one booth to the next.)

CAT Step right up! Step right up! Come see my cow jump over the moon! And for just one silver coin, (insinuatingly) I’ll let you diddle diddle on my little fiddle.

(SNOW WHITE walks up to MAN. She uses his booth to hold herself up. Throughout the following she gets weaker and weaker.)

SNOW WHITE

(exhausted) Excuse me, I’ve been walking for a very long time. I am very tired.

MAN Well, I’ve got just the thing! (He pulls a vial from the booth.) This will give you the oomph you need. You’ll be nimble and quick; you can even jump over a candle stick!

SNOW WHITE Really? What is it?

MAN The newest energy boosting pharmaceutical from The Black Sheep Foundation: Wavenite Oxy- Olivay Lycopenate. (points to sign) W.O.O.L.! (pronounced “wool”)

SNOW WHITE Wool? Well, it sounds like it’ll do the trick . . . Wait, does it have any side effects?

MAN It does, but they’re all pretty standard side effects: a little chest congestion, blurred vision, runny nose, watery eyes, constipation, homosexuality . . .

SNOW WHITE That sounds like more of an effect, really.

MAN Oh, you’ll be fine. Just eat plenty of Miss Muffet’s Curds and lay off the gingerbread men.

SNOW WHITE Hmmm, I donno.

(SNOW WHITE slumps to the ground.)

MAN Honey, you need some fast!

(MAN pours the vial into SNOW WHITE’S mouth. *Creative sound effect, preferably the Popeye theme song.* SNOW WHITE jumps back to her feet, revitalized.)

SNOW WHITE

(smacking her lips) WOOO! That’s the shit! (reading the vial’s label) Side effects of the side effects: guaranteed to bring you true love and happiness. (She slaps MAN on the arm.) Well, why didn’t you just say so!?! (burps) Love, here I come!

(SNOW WHITE moves on to the booth with the pumpkins. PAULINE PETER is finishing up with CINDY who is dressed similarly to SNOW WHITE. SNOW WHITE gawks at CINDY.)

PAULINE PETER So, Cindy, what it comes down tuh is zis: ya got yur gords an yur punkins. Gords is more fer decoratin, an punkins is fer . . . well storage. I mean jess look – hey – where –

(CINDY looks at her watch, jumps up, and starts to run offstage. She stops half-way across, turns to come back, but finally exits.)

SNOW WHITE

(picks up a shoe from in front of the bale, calling after her) HEY! You forgot your Gucci stiletto!

PAULINE PETER Child, from the frantic look on her face, I don’t thank she’s gun-be comin back no time soon.

SNOW WHITE Oh yeah. I did see her face . . . (lustfully) it was gorgeous! (pause, in disbelief) What did I just say?

PAULINE PETER

(leary) Ya said she was purty.

SNOW WHITE *Guaranteed to bring you true love and happiness* (This can be a recording or SNOW WHITE saying it to herself, remembering. SNOW WHITE comes to a realization) She must be the one! She is my true love!

PAULINE PETER Well then, ya betta git yurself a punkin.

SNOW WHITE A pumpkin? Why?

PAULINE PETER Cuz. They’s good fer storin thangs in. Specially people. Why else you thank I’s in this thang, cuz it brings out the color in my eyes?

SNOW WHITE

(gazing into her eyes) Well it does . . .

PAULINE PETER Down, Bessy!

SNOW WHITE How did you get in there, anyway?

PAULINE PETER My no good husband, Peter Peter. He put a spell on it and when I went tuh pick-i-tup, danged if I didn’d git trapped inside. But I do declare, it has kep me very well. I look purt near twenny-five!

SNOW WHITE He put a spell on it?

PAULINE PETER He shore did.

SNOW WHITE Oh, I just love magic! I wish I could have lived back in the days when they used magic all the time. You know, the middle ages, when there were wizards, and trolls, and dragons and virgins . . . and all those other mythical creatures!

PAULINE PETER Girl, you better wake up and smell the four-and-twenty black bird pie! No one knows magic no mo, and eva since Little Boy Blue got a piece of tail ain’t no one a virgin.

SNOW WHITE

(pointing the direction of CINDY’S exit) I bet that blond bombshell who just took off still is - oooh! I’m getting tingly just talking about her! I’m going to find her!

VOICE And so it began.

SNOW WHITE Yes, it did!

(SNOW WHITE goes upstage C. as the curtain starts to close.)

VOICE Snow White set out to find the woman who had left her stiletto at Pauline Peter’s Punkin stand. (aside) Why? I don’t know. I thought she was rather homely, myself. Although, if she bought me a few beers, I was cross-eyed, she had a bag over her head and a Little Red Riding Hood costume – grrrrrr . . . (clears his throat) But, uh, Snow White set out to find Cindy nonetheless.

(SNOW WHITE walks stage R.)

SNOW WHITE I just know that the lady who left this shoe is going to be my soul mate. (She takes a long sniff of the shoe.) I can just smell it!

VOICE Snow White did not know where Cindy had scampered off to, so she just went in her general direction. After a few minutes she ran into Humpty Dumpty and put out –

(*Sound effects of VOICE turning a page of the script and then turning it back and forth.*)

uh . . .hmmm. I think I’m missing a page.

SNOW WHITE No. That’s right. I put out.

VOICE What!?!

SNOW WHITE Yeah . . . the same thing happened when I stumbled across a Cheese, standing alone.

VOICE You’ve got to be kidding!

SNOW WHITE I was in my Anne Heche stage –

VOICE Snow White continued to walk east! (SNOW WHITE walks stage L.) She was lost in no time. But, she stopped at a bridge to get directions from three billy goats, and continued on her way. The closer she got to Cindy’s house the more she felt like cutting her hair, washing off her make-up, and learning to rewire an electrical outlet. The sun was shining . . . there was a gentle breeze . . . birds happily chirped as she passed . . . and she stepped in a dog turd.

SNOW WHITE Oh, here we go again with the dog turd! I hate stepping in poop!

VOICE Fine! (beat) She stepped on a crack and broke her mother’s back.

SNOW WHITE What!?! Like that’s any better!

VOICE Okay! Snow White returned home to the evil Queen and was brutally beaten with Rapunzel’s braid!

SNOW WHITE VOICE Why, I oughta - You know, I’m about sick (coming in after SNOW WHITE’s “I’m and tired of you ruining my life! Every time I about”) turn around it’s Snow White this and Snow Oh, give me a break! If it wasn’t for me White that! I’m going to be in charge of my you’d still be back in that horrible castle own life from now on, so just shut up! getting treated like dirt! You’re lucky I can’t come down there and make you shut up!

(They both end at the same time. Snow White turns downstage in a huff.)

SNOW WHITE Hey! This is the place!

VOICE What makes you say that?

SNOW WHITE There’s a mailbox with her name on it, jackass.

(The curtain rises. There is a house: brick, one level, small porch, attached one car garage L, etc., the typical suburban home. This can be a backdrop, a projected image, or just implied with curtains. There is a mailbox that says “CINDY” and a tree in the front yard R.)

VOICE Be careful. This place gives me the creeps.

(SNOW WHITE goes to the front door and rings the door bell. No answer.)

SNOW WHITE Awww, fiddle sticks and fish fur! I guess I’ll just have to try again later.

(SNOW WHITE crosses to front of tree. After a moment CINDY answers the door. Suspicious, she ventures out into the yard.)

SNOW WHITE

(peering around the tree, to herself) Oh, man! There she is! Here I am about to meet my destiny and I’m dressed like this! It’s a shame I’m not wearing any flannel.

(CINDY catches a glimpse of SNOW WHITE.)

CINDY Who’s there?! Who is it? If you’re from Veggie Tales I’ll beat you with your own Bible!

SNOW WHITE It’s okay! (stepping out from behind the tree.) I just wanted to return your shoe . . .

CINDY

(gasps) You found it?!? Oh, thank you, thank you, thank you! When I woke up this morning I thought (singing) oh, what a beautiful morning! (pause) Of course, I have a hangnail, my electricity got turned off, I lost my frickin’ shoe at that dang carnival, and my dish ran away with a spoon. This day sucks! But, now that I have my Gucci Stiletto – (squeals, reaches for shoe, both hold onto it.) Oh! By the way, my name is Cindy.

SNOW WHITE I’m Snow White.

CINDY

(captured by SNOW WHITE’S beauty.) Yes, you are . . . You should use a tanning bed. (She takes back the shoe. pause) My, what delicate ears you have.

SNOW WHITE

(caught off guard) The . . . better to . . . hear . . . you with.

CINDY And what pretty brown eyes you have.

SNOW WHITE

(flirting) The better to look at you.

CINDY And what beautiful teeth . . .

SNOW WHITE Mmmm, the better to –

VOICE Let’s keep this PG-13!

CINDY Do you want to come in? I’m making curds and whey.

SNOW WHITE I love whey!

CINDY No way!

SNOW WHITE Way!

(SNOW WHITE and CINDY embrace.)

VOICE It was a match made in a-land-not-so-far-far-away-behind-a-castle-near-an-enchanted-forest. Snow White loved being able to talk to Cindy about anything, and Cindy . . . well, Cindy loved the great sex. She enjoyed talking to Snow White, cooking for her, and watching Fairy Tale Idol . . . but, mainly it was the sex.

(Arm in arm, SNOW WHITE and CINDY start walking L. to exit.)

Their love was stronger than Babe the Blue Ox. Snow and Cindy strolled through the town . . . they scampered about the house . . . they skipped through the woods . . . and they stepped in a dog turd.

(Lights out. Curtain.)
```

---

## IC-1469: Table for 2, Party of 4 Text copyright 2006 Andrew Messer.

- Title: Table for 2, Party of 4 Text copyright 2006 Andrew Messer.
- Author (byline): Not specified
- Work: Table for 2, Party of 4 Text copyright 2006 Andrew Messer.
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: ID, S.EGO
- Teaser before the introduction: No
- Spoken words (computed): 1104
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
Table for Two, Party of Four

John: ARGH! Will you please just stop?! I’m nervous enough as it is, and I don’t need you screwing this up for me!

ID: (raspy, smoking) Screwing it up for you? When have we ever screwed anything up for you?

S.EGO: (sophisticated, elitist) Yes, we’ve been with you on every first date you’ve ever been on! John: Yes, that’s right! And have either of you noticed that I’ve never had a SECOND date?!

ID: That’s probably you’re constantly ignoring our advice.

S.EGO: Or, at least my advice. John: Look, will you both knock it off? I can handle tonight on my own. Now when she gets to the table, I think you both should... Cheryl: Um, hi. John? John: Oh, you must be Cheryl! It’s a pleasure to meet you, would you like an hors d’eouvre or a cocktail, or something? Cheryl: Actually, John, I’m going sneak off to the ladies room for just a minute…I’ll be right back. John: Oh, okay. I’ll just be here examining the menu! (sighs, starts looking over menu)

ID: Whoa, she’s hot!

John: Yeah, I know.

S.EGO: Yes, you’ll definitely want to impress this one…
John: Yes, I DO want to impress her, ALONE. Now, she’s coming back, stop!
Cheryl: Stop what?
John: Nothing, nothing at all. Cheryl, would you like to take a look at the wine list?

ID: Wine? Good idea! Ask her if she wants to do shots later!

S.EGO: Oh, we’re off to bad start. Do you want to get her intoxicated? I’ll bet she thinks so. John: Um, they have some nice red wines. I’ll just um, peruse the entrées, while you look. (looks down shyly)

S.EGO: Yes, good! Choose as though price means nothing! Tell her you’ll pay for dinner, no matter what it costs!

ID: Yeah, that’s a good way to get her into bed! John: Oh, and Cheryl, price means nothing…I’ll pay to get you into bed, no matter what it costs. Cheryl: What?! John: NOTHING! Nothing. Um, did you happen to notice what the specials were tonight? Cheryl: Oysters, I think.

ID: Oysters? Forget oysters. Seafood allergies can strike at any time. And ah, swollen lips are DEFINITELY not a plus during make out sessions. John: Oh, well…maybe a steak?

S.EGO: Red meat could kill you!

John: On second thought, I’ll…just have pasta. (closes menu) So, Cheryl, what do you do, you know, to pay the rent? Cheryl: I’m a physical therapist.

ID: I could use some physical therapy!

S.EGO: Oh, good lord. Cheryl: And what do you do?

ID: Come up with something impressive!

S.EGO: No, no, don’t lie to her! Tell her the truth, you’re a teacher!

ID: Oh, that’s wonderful! Tell her you only make twenty grand a year, I’m sure that’ll impress her… John: I make thirty grand a year! Cheryl: Okay, doing what?

ID: You’re a cardiologist!

S.EGO: Teacher!

ID: Lawyer!

S.EGO: Teacher!

ID: Architect!

S.EGO: Teacher!

ID: You’re a GIGOLO! John: A gigolo?!

Cheryl: A GIGOLO?
John: No, no. I’m a math teacher. A high school math teacher.
Cheryl: Oh, that’s great! Well, when you aren’t teaching, what do you like to do? You know, hobbies,
favorite movies…I’m a big music fan, myself…I mean, who’s your favorite singer?

ID: Barry White! Just say it, Barry White!

S.EGO: Oh, Barry White is SO passé! Think of something more sophisticated! Such as…oh, London opera star Jane Marie Manilow!

ID: Barry White! Just trust me on this one!

S.EGO: Jane Manilow!
John: I like Barry Manilow…a lot.
Cheryl: Oh, well that’s interesting.
John: How about you?
Cheryl: Oh, I’m a BIG U2 fan! I just love their smooth sound, and…

ID: U2? I don’t know anything about ‘em!

S.EGO: Me either. Oh, weren’t they big in the nineteen eighties? Cheryl: …and Bono is a wonderful humanitarian. What’s your favorite U2 song?

ID: Oh, crap.

S.EGO: Oh, blast…tell her….after all these years, you still haven’t found only one favorite! John: You know, after all these years…I still haven’t found— Cheryl: WHAT I’M LOOKING FOR?! Mine too!

S.EGO: Advantage, John! John: Wow, that’s um…ironic. Cheryl: So, which of their concerts have you been to? I mean, which tour was your favorite?

S.EGO: Oh, this isn’t good! You need to change the subject!

ID: Yeah, you’re way out of your league on this one. You need something drastic to turn the conversation
around…ah…tell her your mother just died.
John: My mother died?
Cheryl: Oh, your mother died?
John: Yes! No. Well, more in spirit, really…when she found out that I…
Cheryl: That you what?
John: That I, uh…
Waiter: Are you ready to order, sir?
John: YES! Yes. I’d like the pasta primavera, please.
Waiter: Excellent, and for your wife?

ID: You mean one night stand!

S.EGO: Oh, good! This is the perfect opportunity to show her you’re the man! Order for her! John: (sighs) She’s not my wife, and she’s very capable of ordering for herself.

ID: I like your style…putting her in control! Cheryl: I’d like the chicken caesar salad, please…Thank you. Where were we, John?

ID: You were just about to tell her what a great partner you’ll make in the bedroom!

S.EGO: Oh, that’s disgusting! Why don’t you tell her about all your personal achievements! Cheryl: John? John: Oh, um, we were just talking about all the personal partners I’ve had! I MEAN, about my achievements in the bedroom! I mean...uh…

ID: Oh, that was smooth.

S.EGO: Way to go, Romeo. Cheryl: John, you seem really nervous…are you alright? John: No, Cheryl, I’m not alright! I AM kind of nervous, because—

ID: You haven’t had anyone up to your apartment in six months!

S.EGO: You really need to have a successful love life…so you can go back to your twentieth high school reunion and brag to all the chaps!

ID: You haven’t been on a date in so long, you’re afraid you’re losing your touch…

S.EGO: You desperately crave the companionship that can only be found in the lifelong institution of MARRIAGE!

ID: NO! Under no circumstances are you to ever utter that word! You just got dumped. By your last girlfriend…For another woman!

S.EGO: Oh, that’s good. Play the pity card! John: Ugh, shut UP already! Cheryl: Oh…okay…

John: No, not you, Cheryl. I love talking to you. I would like to talk to you for the rest of the night…It’s just that, I am nervous, because I’m afraid you’re not seeing the real me, you know? And I want you to like me. The real me. Cheryl: Oh, that’s…sweet. I’d like to get to know the real you. John: Whew, thank you. I promise you’ll have my full attention for the rest of the night. Without ANY disctractions. Cheryl: Okay. I tell you what…when the entrées arrive, we can start over…with a clean plate?
```

---

## IC-1470: the Bo Show Text copyright 2004 Betty Gerard

- Title: the Bo Show Text copyright 2004 Betty Gerard
- Author (byline): Not specified
- Work: the Bo Show Text copyright 2004 Betty Gerard
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: BO, RASPBERRY
- Teaser before the introduction: No
- Spoken words (computed): 2352
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
The Bo Show is a small girl’s fantasy of a television talk show that takes elements from Oprah, Jerry Springer and Maury.

Characters:
Mommy
Katie, her daughter
Bo Peep, the talk show host
Missy Muffet
Dixie, her baby
Raspberry, a spider
Ruthann Dumpty, Humpty’s widow
Sergeant William Winkie, a boot camp sargeant
Egg Girl, one of Ruthann’s children
Jack Spratt
Jill Spratt, his wife

The Bo Show

A typical nursery room. MOMMY is reading a book of Mother Goose’s Nursery Rhyme to her daughter, KATIE.

MOMMY Little Miss Muffet sat on her tuffet-

KATIE Mommy, what’s a tuffet?

MOMMY (laughs, thinks, pauses unknowingly) …eating her curds and whey, but along came a spider and sat down beside her, and frightened Miss Muffet away!

KATIE Yeah! Mommy, one more! Please!

MOMMY Okay, Katie (reading). Humpty Dumpty sat on a wall, humpty dumpty had a great fall…

KATIE Mommy—

MOMMY Yes, Katie?

KATIE What’s a junky-ho?

MOMMY (beat) Where did you learn that word?

KATIE I heard it on the TV show?

MOMMY Katie! Daytime smut is not for little girls!

KATIE Oh, sorry Mommy.

MOMMY That’s okay sweetie. And all the king's horses and all the king's men…

KATIE falls asleep, and we see her dream sequence, which takes place in a studio of a television talk show. We first see Bo Peep, who speaks in an intense, Oprah-like manner

BO Welcome to “The Bo Show!” I’m Bo Peep, and I though I may be little, I got a big personality. (laughs, suddenly serious) But on a serious note, the search continues for my missing sheep. They are said to be fluffy, adorable and wagging their tails behind them. In times like these, there is one thing that can raise my spirits, and that is the sheer exuberance that one can only come from the exploitation of… other people’s problems. (beat) Now let’s get started!

BO Our first guest is a young mother named Missy, who says that her ex boyfriend Raspberry seemed like a perfect guy, but turned out to be a perfect pest. Missy, welcome to the show.

MISSY is slow and aloof. She appears unshowered and distracted.

MISSY Hey Bo. Sorry about your sheep, girl. And thanks for the snacks in the green room. I mean, string cheese is, like, my fourth favorite food, yo.

BO Missy, tell us what happened.

MISSY Well I was sitting on my tuffet, and—

BO Your tuffet?

MISSY What?

BO Go on.

MISSY Well along came Raspberry, and, well, we had, like, a connection, you know. Like, ICUT “I” we both really liked curds and whey, and we both liked to weave things…

BO So what went wrong?

MISSY He just got all up beside me and in my business. His butt would do this weird thing, and then messages would appear in his web. They started out nice like “I like the way it feels when I hold your hand.” But then they got scary. Real scary. You know, like, “I want to squeeze you until your brain explodes.” Things like that. Scary.

BO So what did you do?

MISSY I up and left.

BO You go girl.

MISSY But then…

BO Uh oh…

MISSY I had my son Dixie.

DIXIE Wah!

MISSY And now I’m raising his kid, and he won’t give either of us the time of day!

BO Lets see what Raspberry has to say about that.

Raspberry appears on a monitor. A spider, he wears a dark hooded sweatshirt and several golden chains.

RASPBERRY My name’s Raspberry and I’m the baddest spider in town. I may be itsy bitsy, but I don’t take nothing’ from nobody, and I don’t front. I’m a hundred and fifty percent sure I’m not the father. That kid don’t look nothing like me! And besides, Missy was cheating on me the whole time. She’s nothing but a no good pain in the tuffet. I don’t front.

BO He doesn’t front. Let’s bring him out. Raspberry!

RASPBERRY Naw! Naw! You don’t know me! You don’t know!

MISSY You’ve got to get off your tuffet and take care of your baby!

RASPBERRY I ain’t your baby daddy!

BO Raspberry, welcome to the show. Now, you said you were certain that you were not Dixie’s father.

RASPBERRY He don’t look nothing like me.

MISSY He has eight legs.

DIXIE Wah!

RASPBERRY So?

MISSY He has an exoskeleton.

DIXIE Wah.

RASPBERRY Psshhh, that don’t prove nothing. Besides, she cheated on me, Bo!

BO Well, Raspberry, are you suggesting that Missy was unfaithful to you?

RASPBERRY Bo, I caught her in the act!

MISSY What?

RASPBERRY I saw her kissing Georgie Porgy.

BO Missy, is this true?

MISSY Georgie Porgy kisses everybody.

BO I hold in my hands the shocking results of the is-this-spider-baby-the-offspring-of-this-spider test.

RASPBERRY I ain’t your baby daddy.

MISSY We’ll just wait and see.

DIXIE Wah!

Bo begins to open the envelope, then stops.

BO I should explain that these tests are only 99.9% accurate and there is always a chance that—

RASPBERRY Just read the damn thing.

BO (reads) When it comes to three-month-old Dixie, Raspberry, you are the father.

RASPBERRY Naw, shoot man! Naw!

MISSY I told you! I told you!

RASPBERRY How am I supposed to take care of a freak like that!

DIXIE Wah!

MISSY He ain’t no freak… he’s your baby. (Hands Raspberry the baby)

DIXIE Waaa---dada!

RASPBERRY (Blushing) Aw, shoot.

BO Raspberry, Missy, and Dixie, we hope you all are very happy! You know, every once in a while on the Bo Show, we like to feature someone who has found her spirit in the face of tragedy. In light of my lost sheep, it was the story of Ruthann Dumpty that inspired me to remember my spirit. A mother of seventeen, Ruthann lived with her husband, Humpty, and seventeen children in a giant shoe. In November of last year, Ruthann lost her husband in a tragic accident, but has found herself through prayer, mourning, and a monthly subscription to Bo Magazine. Welcome to the show, Ruthann.

RUTHANN Hi Bo, great to be here. I am so sorry about your sheep; your bravery is really inspiring.

BO Yes. Yes it is. So, Ruthann, take us back to that day.

RUTHANN Well I was back home in the shoe, vacuuming the heel, when I got a phone call. I asked who was calling, and the man on the line said the [that] he was one of the kings men, which seemed like an oddly vague description at the time, but— BO Go on…

RUTHANN …then he said that my husband had-- (crying)

BO Yes…

RUTHANN He had…

BO Yes???

RUTHANN A fall.

BO (confused) A fall?

RUTHANNE A great fall.

BO: Huh?

RUTHANNE A fall from a wall.

BO I still don’t really see how—

RUTHANNE He’s a giant egg, okay?

BO: Oh I see. And how did you deal with this.

RUTHANNE I did a lot of soul searching, and finally I told myself to wake up. I said, “Ruthann, even if the man you loved more than anything in the world may be shattered into thousands of tiny pieces without any hope of being put back together again, you can still put back together the shattered pieces of your life.

BO Wow. That’s really beautiful.

RUTHANNE I know.

BO So what did you do?

RUTHANNE I chunked my hair, lost fifteen pounds, and started to face the woman I am: a middle-aged stay-at-shoe mom who lives in a giant sneaker with seventeen egg-children and the fading memory of her dead husband.

BO You go girl. But how have the children dealt with the trauma?

RUTHANNE Well, Bo, you have experienced a great loss…

BO You bet your tuffet I did.

RUTHANNE And you know that along with grief comes a lot of anger.

BO Of course.

RUTHANNE And with anger comes cussing and sassiness.

BO Like…

RUTHANNE Like staying out past 8 o’clock.

BO So what did you do, Ruthann?

RUTHANNE Bo, I sent the whole mess of ‘em to Sergeant Willie Winkie’s all night boot camp for sassy teen-agers who stay out past 8 o’clock.

BO Let’s take a look.

The seventeen egg children are seen at bootcamp. Sergeant William Winkie paces from side to side in a drill sergeant manner. He is overly muscular, and wears a tight muscle shirt and a nightcap.

WINKIE When I address you, you will respond “Sir yes sir!” Do you hear me?

EGG GIRL Sir yes sir!

WINKIE My name is Sergeant William Winkie, and you disgust me.

EGG GIRL Sir yes sir!

WINKIE You’ve got to learn some respect! You kids have it so easy!

EGG GIRL There are seventeen of us, sir! We live in a shoe, sir!

WINKIE When I was growing up I had twenty-eight brothers and sisters and we lived in an earmuff! I am gonna work you harder than you have ever worked. You are gonna do two hundred pushups a day!

EGG GIRL But we don’t have any arms, sir.

WINKIE Then you’ll do three hundred, you over-easy embry-HO.

EGG GIRL (crying) Why are you doing this to us! Our dad fell of a wall!

WINKIE Cause it’s a scrambled up world out there, and you got to be hard-boiled to survive.

EGG GIRL

(sings)
It’s a hard-boiled life for us.
It’s a hard-boiled life for us.
When we fall down we get broke,
‘Cause we’re made of shell and yolk,
It’s a hard-boiled life!

WINKIE Shut up or I will shut you up! Don’t you think for a moment that I won’t go completely benedict on yo--

EGG GIRL

(sings)
I’ll be sunny side up, tomorrow
Sizzlin’ in a non-stick pan, tomorrow
Come what may…
Tomor--

WINKIE Oh, that’s it.

Winkie smacks the Egg Girl and she cracks open onto the floor.

WINKIE Oh, tuffet.

Back in Studio

BO Wow. That was really powerful stuff.

RUTHANNE [Ruthann] Powerful my tuffet! That man just cracked open my baby!

BO Yes. Yes he did. Thank you for being with us Ruthann, and best of luck to you and your family. My next guest is a man who says that his wife Jill’s disgusting eating habits are ruining their marriage. Welcome to the show, Jack Spratt!

JACK Bo, you look great.

BO Oh, thank you. All the grieving over my lost sheep has done wonders for my waistline. Plus, I am on an all-lean diet

JACK Me too.

BO So what’s the problem.

JACK My wife has a bit of a weight problem, but she’s confident about her body. She eats pudding by the quart, and doesn’t give a tuffet how she looks. How’s she ever going to lose any weight with all of that self-confidence?

BO Let’s bring her out. Jill!

JILL Look at you! Look at you! You know you’re jealous.

JACK She’s out of control. Just look at her!

JILL What? I look good. I’m big and beautiful.

BO Well, one out of two isn’t bad.

JILL Jack, you’ve got to realize that beauty is in the eye of the beholder.

JACK Well this beholder says that you look like a beached whale.

BO It’s true, Jill. You are only as beautiful as we think you are. Which brings us to an interesting question. How does one get to a point of such obesity?

JACK Well, she eats no lean.

BO No lean?

JACK But it’s not just the lean she won’t eat, Bo. It’s anything remotely nutritious.

JILL What?

BO So, you wouldn’t eat a bowl of cereal?

JILL No

BO Grapes?

JILL No.

BO Peas?

JILL No.

BO Celery?

JILL Maybe if it was dipped in puddin’.

BO So what do you typically eat for breakfast.

JILL I don’t know, twelve eggs.

RUTHANN That’s murder!

BO Twelve eggs! You eat a dozen eggs every morning?

JILL It dudn’t look like that much when it’s scramble.

BO Now, is it true that your fighting has actually escalated into something even more serious?

JACK If by something serious you mean she tried to murder me.

JILL Oh, my tuffet I tried to murder you.

BO Jack, take us back to that day.

JACK Well, it was time to fetch some water from the hilltop.

JILL Only you didn’t tell me we was just fetching water.

BO What did you think you were going to fetch?

JILL Puddin’.

BO I see. You believed you went up the hill to fetch a pail of pudding.

JILL And he lie, Bo! He lie so bad!

BO So you assaulted him.

JACK She pushed me down the hill.

BO You pushed him down the hill.

JILL That’s right. And I shouted, “get me some puddin’, skinny!”

JACK (Beginning to tear) And during the fall…

BO Yes?

JACK I broke my crown.

BO He broke his crown.

JILL Why you always wearin’ a crown, anyways? Who do you think you are?

BO Jill, here on the Bo Show, we believe that problems can be fixed from the outside in. And so, for an obese, manic-depressive spouse-pusher like you, Jill…

JILL Jealous?

BO …there can be only one answer: make-over!

JACK Sorry, Bo, but I don’t think the best hair and makeup in the world could fix this one.

BO We’ll take the fat from her stomach and put it in her lips! We’ll take the fat from her legs and put it in her breasteses. And we’ll shrink her stomach down to the size of a chestnut so she won’t gain an ounce.

RASPBERRY Wait!

BO Yes?

RASPBERRY I think she look good the way she is!

BO What?

RASPBERRY: I like my girls with a little extra junky-junk in the badunkadunk.

Suddenly we see Mommy, who is waking up Katie.

MOMMY Katie, Katie?

KATIE (opens her eyes) Mommy?

MOMMY Katie, did you have a nice nap?

KATIE I had a dream about the mother goosey book!

MOMMY Did you?

KATIE Can you read me some more? I think that’s the best book in the whole world.

MOMMY (laughs) Oh, you think so?

KATIE Straight trippin’.
```

---

## IC-1471: The Disappointing son Text copyright 2004 Clyde Hendrickson.

- Title: The Disappointing son Text copyright 2004 Clyde Hendrickson.
- Author (byline): Not specified
- Work: The Disappointing son Text copyright 2004 Clyde Hendrickson.
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2923
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
Setting.

A simple kitchen, with details, some realistic, some surreal. Action takes place in and around the kitchen table.

Characters.

SON. Ages from 10 to 15 during the play. Naïve, but not stupid. DAD. Middle-aged. MOM. Looks older than she is.

The Disappointing Son

(The play opens. Dad is counting several large stacks of bills.)
SON. Wow, Dad, where did you get all that money?
DAD. Oh, you know, a little saving here, a little mercenary work there… it adds up.
SON. What does it add up to?
DAD. A new, prettier mommy for you and me.
SON. Huh?!
DAD. Just kidding! I’m sure I’ll blow this money at the cockfighting ring by the end of the week.
SON. But you have lots more saved up so I can go to Harvard, or Georgetown, or Kansas State, right?
DAD. (looks guilty) Uh, yes… of course I do… (changing subject) It’s remarkable how many kids go to

work at a young age these days.
SON. Huh.
DAD. I know several of my colleagues who already have children in the mines.
SON. Wow, do they meet monsters?
DAD. Monsters! What a silly boy you are. Those young chaps die long before they reach the monsters.
SON. Darn.
DAD. If you really want to see a monster, know what you can do?
SON. (excited) What??
DAD. You can try waking up next to your mother every morning for 15 years. It's like medusa spawned

with a ball of kelp and deposited the afterbirth at my bedside.
SON. Oh.
DAD. Don't worry, you'll understand our relationship someday, Son.
SON. I think I reached that point, Dad, when I watched mom burn all your socks, one by one, after

painting little frowny faces on them. DAD. That was just for show. SON. So your marriage is just an act? A show?

DAD. No! Your mother and I would never do that to you.
SON. (relieved) Really?
DAD. Of course - we never do anything for your benefit.
SON. Was Mom ever beautiful, Dad?
DAD. Yes she was, son, until I sobered up. Who knew a Mexican marriage license was so tricky to

escape? (He looks offstage.) Here comes your mother. Pretend we were talking about something

else. SON. Ok… uh, gee, Dad, thanks for talking me out of smoking! What an awful habit. What was I

thinking.

(Mom has entered during this line, visibly smoking a cigarette) DAD. (whispering) No! No! Now you’ve screwed us. Red Alert, Captain Witless! (to Mom) Hah! That

son of ours, what a joker. MOM. It’s alright, go ahead and judge me. (she takes a long drag) I learned to stop caring what your

father thought, it won’t be that hard with you.
SON. Mom! When did you start smoking?
MOM. As soon as I figured out that it would help you and your father die faster, dear.
DAD. Your mom’s great, son. She’s always thinking about our welfare.
SON. Do I get to join the make-a-wish-foundation?
DAD. What could you want besides a loving home and full childhood?
SON. Well… I guess that was my point, Dad.
DAD. (taken aback) Oh. (For revenge) Remember when your cherished baby blankie “disappeared”?
SON. Yeah…
DAD. That’s because I put it in the food processor in a drunken stupor. Yes, you and that blanket were

inseparable until I made it into a milkshake, which I later… deposited on our neighbor’s porch. SON. But the neighbor’s house burned down 4 years ago. Wait, that’s right when I lost my blankie. MOM. Shh… we’re still not sure the Arson Unit didn’t bug the house. DAD. Oh… right. Mum’s the word! SON. At least I still have my tiddlywinky doll! It laughs and jiggles, see! (He turns the doll on, and it

vibrates.) MOM. Awww. (She takes the doll from him and puts her cigarette out on its face. It stops vibrating. She

then hands it back.) SON. Tiddlywinky!

MOM. Where did you get that filthy heathen idol, anyhow? DAD. It was my mistake. He got an A on a test, and I felt that I should reward him. It was a moment of

weakness, it won’t happen again.
MOM. An A, huh?
SON. Yeah. Here it is! The teacher even drew a smiley face.
MOM. Oh she did, did she? Let me take that.
SON. Are you gonna put it on the fridge, next to daddy’s bail bond?
DAD. Now that deserves a smiley face.
MOM. No, no, I have a better place for it. (She lights the cooking range.) Burn, you smiling little

bastard, burn.
SON. But… but…
MOM. Look at his little grin crinkle up as he dies his painful death.
SON. My A!
MOM. I guess it’s an A+ now.
SON. Can I have the ashes, at least?
MOM. (hands him the ashes) Here. Put that on your fridge and smoke it.
SON. Maybe I will start smoking. (gathers up ashes) I’m going to put these in the urn that has Mr.

Kitten’s remains.
DAD. (laughs) That’s not Mr. Kitten. That’s a bunch of eggplants I burned for tax purposes.
SON. What? Where’s Mr. Kitten?
DAD. In cat hell. He ate my prize rooster.
SON. Did you kill him?
DAD. Sure I did.
SON. Why?
DAD. So you would build character when I told you about it in a shocking scene, years later.

Congratulations… you are now a man.
SON. But I’m only 10.
DAD. Whining already? Try not to be such a wimp, girlie man.
SON. Yes sir. I’ll try to be more manly. (He makes an attempt.) So, woman, any meat for dinner?
MOM. We’ve got some Mr. Kitten pie left over in the fridge.

DAD. (uncontrollably laughing) Oh my dirty little ferret, I love it when you’re sadistic.
MOM. There’s more where that came from, if you can ditch the Mr. Whiny here.
DAD. Of course. (thinks quickly) Son, I believe it’s time for you to go to your electroshock therapy.
SON. Awww, but Dad, I don’t wanna (twitches) I don’t wanna (twitches) I don’t wanna go to my

electroshock therapy.
DAD. Nonsense. It builds character.
SON. I do feel more prepared for the painful things in life… and life is pretty painful around here.
DAD. You should get better at wildly convulsing and flailing.
SON. Even if I hit people?
DAD. That’s how you’ll meet the girl of your dreams!
SON. How did you and Mom meet?
DAD. Well, that’s a sad story. I was young, carefree, and had my whole life ahead of me. So, of course, I

was playing the field. Your mom got pregnant… and, well, when it became clear that there

weren’t any buyers for you, we bit the bullet and got married. SON. Wow, you changed your whole life for Mom? That sounds really hard. DAD. Nah, I was drunk. Still am, really. So it’s not too bad. I’d compare it to… being run over by a

luxury cruise ship while hornet larvae simultaneously devour your brain. SON. Am I the ship, or the hornets? DAD. You’re a little of everything, kid.

(Lights down. They come up again on DAD, alone on stage. He is smoking. His son’s baby blankie is

propped up on a chair, and DAD addresses his speech towards it.) DAD. I have a secret. No, that's too obvious. Let's try... I have a turkey. But it's a little turkey. Inside of me. And it's growing and clawing and trying to tear its way right out! Yes, that's better. A turkey. Frankly, I’m tired of being “Dad” for everyone else. If I am to go out and spend all $200 of the grocery money on beer and corn chips and avocados, who is my family to judge me? I am the FATHER! And do not accuse me with your silence, blanket! You would do no differently. If you had a digestive track and so forth, which you don’t. You really are missing something with the corn chips. I wish I had some fritos right now… but my SON ate them all. Imagine that. If he was a hyena, I would eat him for eating them. I tried once, actually, but unfortunately our oven can be opened from the inside, and the boy panicked quickly. That’s another of his weaknesses – he’s not too cool under pressure. (He grabs his stomach, as if in pain) Oh, my little turkey, sweet secret turkey, I want to let you out. Why must you torment me so? So Blanket, you have a family, right? Grandma Yarn and Uncle Two-stich and what have you. You know that feeling, at christmas time, assuming Jesus loves blankets which I can’t say for sure, when you’re with your family, they’re three sheets to the wind, and you think “these people are so crazy, they can’t possibly be related to me!” Well, I say you’re right. There is no way these people are related to me. Look at me - I’m the cock of the walk - an intellectual powerhouse and a very handsome man. My placement with these plebians must be a joke. A sick joke. Which is not to say I don’t get the joke - I admit that at times I find myself laughing at our situation, and I think, “Good one, universal power!” Then I see my boy, a smile on his face, a glimmer in his eye, and the horror of the situation comes crashing down on me like a flaming mass of deadly pit vipers. Why should my son have all the hope? Why should he inherit the future? He’s just a stupid boy. I’m the one whose fought through a lifetime of hardship, I should be the one with the energy of ten coke-addicts at a columbian strip club, not him. So here I am, with a blanket as my only friend. This is what my blanket tells me: My family was brought together, artificially, to learn, to live, and most importantly, to kill each other. What could be more sick and entertaining? It’s the type of thing liberals and scientists get off on. I suspect they’re behind this. Or possible a greek god, like Zeus or Neptune. Yes, this seems like the type of thing they’d get involved with. And there’s nothing left but to let their little drama play out – but we can make sure it plays out our way. You and me, blanket. We’re one in the same. You’re supposed to provide warmth and comfort, and what do you get in return? A half hour in the heavy duty cycle with old socks and underwear. That’s my life, except it’s more of a permanent press. My god, even metaphorically speaking I’m a genius. What poetry! But you’re a blanket, of course, so you don’t understand poetry But you can understand this: I won’t put up with it for much longer! My hopes and dreams shall not be sacrificed for silly things like love, family, or commitment. We’ll ditch these losers and go start that tequila farm we’ve always dreamed about. Agave and cockfights, as far as the eye can see! It’ll just be you and me and the turkey and probably a lot of prostitutes. Be patient a little longer… and remember, say nothing to no one, especially the boy! A person with such a promising future simply can’t be trusted.

(Lights down as Dad grabs the blanket and exits.)

A BOOMING VOICE. Five years later!

(Lights up. Only a few things have changed – the positions of a few items, the color of the mother’s wig,

the son’s hat. Dad and Son are now smoking as well.)
SON. Man, I can’t wait for dessert.
MOM. I guess laying all that concrete for our gazebo makes you hungry.
SON. Sure does.
MOM. You’re so nice, to suffer for your mother’s whims.

(Suddenly, Dad slams his dinner plate aside) DAD. Let the Ritual of Dessert begin!

(Mom sets out the pudding dishes. They gather around the table, holding hands.)
DAD. Sing the carol of thanksgiving, son.
SON. (singing to the tune of ‘Deck the Halls’)
Deck the Halls with Gasoline,
Light a match and watch it gleam,
See your school burn down in ashes
Aren’t you glad you played with matches?
DAD. That’s enough. Sugarthighs, will you bless the pudding?
MOM. In the name of Hulk Hogan, The Rock, and the spirit Stone Cold Steve Austin, I pepper this

pudding. (She sprinkles some pepper on each pudding) DAD. Amen! Dig in, you filthy swine!

(They all eat ravenously, smoking between bites. Suddenly, the son starts choking, and he spits out his

pudding)
DAD. No, no! Eat up son!
MOM. Yes, all that healthy vitamin C.
SON. (between gagging) Vitamin C makes you choke?
MOM. It does when the C stands for Cyanide!
SON. You poisoned my pudding? What in the name of macho man randy savage is going on here?
DAD. I can explain. If you’ll just give me time to gather a rag and some chloroform, I can explain

everything. SON. No! I’m not spending another fortnight in the basement. This poisoned pudding is it. This family is

too stupid to live in.
DAD. It was just a little joke, son. Totally harmless. Well, except for you dying.
SON. My death is a joke to you?
DAD. Your Mom and I had a bet to see which of us could off you first. Looks like my little sugarbum

here almost won!
MOM. Darn it.
SON. (suddenly calm) … Yes. May I be excused. I have some homework to do.
DAD. Sure.
SON. I need the key to your gun rack.
DAD. Why?
SON. Uh, I left my homework in it.
DAD. Dumb kid. Here ya go. (He tosses him the keys.)
SON. Thanks! (He exits quickly.)
MOM. Do you think we did the right thing?
DAD. Yes, my little parsnip. But it was a tremendously good thing that we got drunk before we did.

MOM. Maybe it’s the Mezcal talking, but have you grown a foot taller and started to look like a Caucasian

Antonio Banderas? DAD. You noticed. I wanted to surprise you. MOM. Come here, my great white Zorro.

(They begin to canoodle.) DAD. Careful! You don’t want to aggravate my hemorrhoids!

(Canoodling continues. Son re-enters, carrying a shotgun.)
DAD. By the spirit of stone cold Steve Austin, what are you doing?
SON. I’m becoming a man, like you always wanted me to be, Dad!
DAD. No! That’s not true! I didn’t want anything for you. I was just faking to get you to go away and

stop bothering me.
SON. Well you had me fooled! And Mr. Kittens, too.
DAD. Mr. Kittens is here?
SON. Yeah, (cocks shotgun) remember what he did to your rooster? What til you see what he does with

your other co- (He is struck from behind). MOM. (holding a big stick) Got him! DAD. Oh no! You’ve become a horrible stick monster!

(Dad takes stick, strikes mom with it.) DAD. I feel positively emancipated. To the broom closet!

(He picks up shotgun, cocks it, and leaves. Son groggily awakes.) SON. Where… what… Mr. Kittens…

(Dad enters, his arm around a donkey. He is trying to sneak past the son.)
SON. Is your arm around a donkey?
DONKEY. Hee-haw!
DAD. This is awkward.
SON. It does look uncomfortable.
DAD. No, no, not the donkey. He’s actually quite plush. What’s awkward is that I’m leaving.
SON. For the store?
DAD. For Mexico, Son.
SON. On a trip?

DAD. Yes! SON. Oh, ok. DAD. What I mean is, It’s quite a trip that I’m leaving my old life behind to go live on a Mezcal farm in

Guadalajara. Ha ha!
SON. So you’re outta here, just like that. Leaving me and mom behind.
DAD. Oh, your mother’s coming too! (He hoists her up on the donkey.) It’s you we’re leaving.
SON. No, you can’t! I’m still making a stand. I’m still filled with a murderous rage. It’s palpable. Feel

it? (Puts Dad’s hand on his forehead)
DAD. Hmmm… seems to be just a slight fever. Maybe you came down with measles.
SON. It’s palpable rage! I’m steaming with it. It’s practically boiling off of my groin.
DAD. It’s natural for a boy your age to go through periods of awkwardness. I wouldn’t worry about it if I

were you. Of course, if I were you, I would have killed me ages ago to get my priceless

assortment of collectible screwdrivers and rickshaws. But I guess I didn’t raise you well enough

to take advantage of your situation.
SON. Raise me well enough to kill you, you mean?
DAD. Yes, son, to slay your father dead. It’s every parent’s dream.
SON. Actually, I did just try.
DAD. You call waving that loaded shotgun around in the kitchen an attempt to kill your parents? Try

again, measlegroin.
SON. Your donkey’s about to feel my awkward measles. (makes threatening gestures)
DONKEY. Hee haw?
DAD. It’s ok, Mr. Honkeybutt. I won’t let him touch you or your luscious, luscious donkey coat. (strokes

donkey very thoroughly) Oh wow… now that’s living. MOM. (waking up) What, what’s going on? Why am I riding this shag carpet? (strokes donkey) Ooooh…

so plush. DAD. You’re riding our new son, dear. Let’s be off, the flight for Cancun leaves in an hour. MOM. Ok. Former son, take care of the house, or burn it down, or something. And abandon this donkey

somewhere that I won’t have to see it again.
DAD. I was going to take that donkey with me. To tequilatown.
MOM. Just leave them. We’ve almost shook the boy.
DAD. No…. no, it’s clear to me now. We’ll have to stay, all of us: men, women, and beasts.
MOM. Are you crazy? I hate it here!

DAD. I hate it here too, sugarplum. But a man must stick to his decision.
MOM. You’re not sticking to anything. You’re waffling like a hungry minority outside of Denny’s.
DAD. Look, we’ll compromise. Let’s take a vacation together.
MOM. Vacation! The last vacation you took us on, you drugged the boy and I and spent 3 days at an

Indian casino.
SON. So I didn’t have a vicious case of Alzheimer’s that miraculously receded!
DAD. I was thinking of a more… wholesome trip. Maybe we can all stay awake this time.
SON. Then we can get to know each other.
DAD. (turning to Mom) Or, at least you and I can stay awake.
MOM. Let’s go to the holy land.
DAD. I’ll mount your temple mount.
MOM. I’ll wail at your wall.
DAD. I’ll….
MOM. I love it when you pray dirty.
SON. What about me?
DAD. Sit down, son.
SON. I am sitting down.
DAD. Well then sit down some more. (Son tries to do this.) You’ve been a good son to us.
MOM. Really, quite tolerable.
DAD. And you’ve learned a lot of useful skills. Times are tough, though, as you’ve seen firsthand.
SON. I’ll say.
DAD. Say what?
SON. … That times are tough.
DAD. I’ve already said that. Don’t repeat things. It’s annoying.
MOM. He’s always doing annoying things like that, from wetting the bed to starting puberty! Growing all

that hair… the nerve of this kid. DAD. It’s ok, my potato pie. I’m taking care of it. (back to son) I think it’s best we moved on, son. All

of us. SON. So what you’re saying is… DAD. This is hard. You better sit down.

SON. (scrunches down even more) Ok. DAD. Son… You’re fired.

(Lights down immediately.)
```

---

## IC-1472: Virtually Dateable 2010 Josh Danz ©

- Title: Virtually Dateable 2010 Josh Danz ©
- Author (byline): Not specified
- Work: Virtually Dateable 2010 Josh Danz ©
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1233
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
Jessica: Amanda, I can’t believe you actually wanna do this. No one actually finds any good guys

on the Web. Amanda: Ok Jessica, then what do you propose I do? Go find guys at closing time at the liquor

store like you do? Jessica: Hey, don’t judge me! You know what? Fine. You wanna whore yourself out over the

Internet? Just be my guest. But don’t use one of those sites you see in the TV

commercials. I just don’t trust them. There’s no way any real couple can be that happy

without some sort of substance abuse. Amanda: Ok fine. Let’s just see what dating sites are out there… (types some things into her

computer) how about this one? It’s called “singlesromancesearch.com.” This looks good. Jessica: (Filing nails and acting uninterested) Sure. Sure. Whatever you say. Amanda: Ok. Time to make a profile. Name: Amanda Turner. Age: 29… (thinks a second, then

changes her mind) let’s go with 26. Seeking: A decent guy for a relationship. Now I just

add a picture and enter in my credit card information… Jessica: Wait, that’s it? You just fill in your name and age and you’re ready to give them personal

information? You’re crazy! Amanda: Have a little faith, Jessica. It’s worth a shot for $2.99 a match. (glances back at computer

screen) Wow! They sent me a match already! Jessica: (Pushing Amanda out of the way) Move over! I wanna see the creep that money bought

you. Name: Mitch Cooper. Age: 31. Seeking: A young woman for a relationship.

Amanda, I can’t believe I’m saying this, but this guy actually looks dateable. Amanda: You think so? I think I’m gonna go meet this guy. Jessica: Tell me how that goes for you. I wanna know how much your expectations are crushed. Amanda I thought you said he looks dateable!

Jessica: I’ve been wrong before. Just call me after, OK?

(Cut to Amanda knocking on Mitch’s door. Mitch answers the door.)
Mitch: Hello there, you must be Amanda. Come in and sit down.
Amanda: (Uneasily) Ok then… it’s nice to meet you.
Mitch: Can I get you something to drink? Water? Coffee? Roofie? Soda?
Amanda: What was the middle one?
Mitch: Coffee?
Amanda: (Nervous, slightly afraid) No thanks. I’m really Ok.
Mitch: You know, sweetheart, I’m not used to female callers so (Breathes in lustily) mature.
Amanda: (Disturbed) Thank you?
Mitch: So do you use Internet dating sites often?
Amanda: No… it was my first time.
Mitch: Oooh, I love it when it’s their first time.
Amanda: Excuse me?
Mitch: I didn’t say anything. I use Internet dating sites all the time. I used to use Myspace but

other sites seem to be… safer. Amanda: What do you mean by safer? Computer viruses and stuff? Mitch: Yeah… computer viruses.

Amanda: You know what, Mitch? I feel like I’d seen you before when you came up as my match.

Have you been on TV or something?
Mitch: Do you watch To Catch a Predator?
Amanda: Yeah!
Mitch: (Loudly and defensively) Well I was set up! I had nothing to do with it! (Clearing his

voice) But enough about me. Tell me about you. What’s it like to be a teenager

nowadays?
Amanda: (Confused) You think I’m a teenager?
Mitch: Your profile said you were 16.
Amanda: No, I’m 29… I mean 26.
Mitch: (Growing disinterested) So you’re in your 20’s… that’s… good. (Yawns loudly) Boy, it’s

getting pretty late. You should probably get going. Amanda: It’s still light out. Mitch: Yeah, well I need to wake up early so you have to go now. (quickly gets Amanda out of

the house) Have a nice life!

(Amanda takes out cell phone and calls Jessica.) Jessica: Hello? Amanda: Hey Jessica, it’s Amanda. My date didn’t go too well. I think that guy was a pedophile or

something. Are you home?
Jessica: Yeah. You wanna come over and talk about it?
Amanda: Yeah, I’ll be over in a couple of minutes.
Jessica: Ok bye.

(Cut to Amanda knocking on Jessica’s door. Jessica answers the door.) Jessica: Oh, good, you’re here. Now what did I- Amanda: (Quickly interrupting) Where’s your computer? I’m going back on that site and getting a

new match right now. Jessica: Are you insane, Amanda? After the pervert they matched you with the first time? Amanda: Look. It’s still early, and there’s a buy one get one free deal on that site. (types some

things on the computer) Ok. I got another match. Brett Daniels. Age 28. Seeking an

exciting woman. (standing up) Sure why not? Jessica: You’re actually gonna go out with this guy. Amanda: (Angrily) I gave that site money and damn it, I’m gonna get something out of it!

(Cut to Amanda sitting in a bar waiting for Brett to show up.) Amanda: (To herself) Ok this guy says to meet here at 8:30 and it’s 5 after 9 now, so how much

longer do I sit here? Brett: (To bartender) Hey, barkeep! I’m supposed to be meeting a chick here. Brunette, looks

easy, you know the type. You seen her? (glances over at Amanda and is immediately

interested) Hey baby, I was meeting someone here but I’d much rather just have a drink

with you. Amanda: (Put of, indignant) You must be Brett then. I would be the easy brunette you were talking

about. And by the way, I have a name. It’s Amanda, and-
Brett: (Interrupting) Shhhhhhh, too many unimportant details
Amanda: Why you arrogant son of a-
Brett: (Interrupting again) Shhhhhhh, Shh. Listen Ilana-
Amanda: (Offended) It’s Amanda!
Brett: Whatever Emma. Anyway, it’s getting kinda late. Why don’t we make like a drum and

head back to my place? Amanda: I’m not going anywhere with you, jerk. Get away from me! Brett: Fine. (looking to the other end of the bar) Hey baby. How would you like to find a booth

for the three of us: you, me, and a bottle of Jäger. Amanda: Oh, god, I need a drink (cell phone rings and Amanda answers) Hello? Jessica: Hey, Amanda, it’s Jessica. I’m just calling to make sure your second date is going better

than your first one. Amanda: I swear, Jessica, I’m this close to giving up on men altogether. Jessica: You’ll figure it out, Amanda. You just have to figure out where to look. And the Internet

is not the place to look. Amanda: (Dejectedly) Yeah, I guess you were right all along. Are you gonna be at the liquor store

tomorrow night? Jessica: I was planning on it. Amanda: I guess I’ll see you at closing time then.

(Cut to Amanda looking around bar in effort to find Jessica.) Amanda: (To herself) I can’t believe I’m doing this… am I really this desperate?… and where the

hell is she?... Jessica: Hey, where’ve you been? Amanda: Where’ve I been? You’ve been here this whole time?

Jessica: Yeah, I’ve been finding some good guys for you in there. I remember how hard it was for

me when I was a rookie…
Amanda: Jessica, can you focus for once in your life?
Jessica: What? Oh right. Hey! Kurt! Come meet the girl I was talking about!
Kurt: (Drinking from bottle of tequila and visibly drunk) Hey honey (belches loudly) do y’all

know where I can get some good moonshine? This (squints at bottle and mispronounces

tequila) te-quill-a isn’t strong enough for the likes of good ol’ Kurt.
Amanda: Please tell me this wasn’t the best you could find…
Jessica: (Unconvincingly) Come on… he’s not that bad…
Kurt: (Looking in bottle of tequila) Hey! There’s a gummy worm in the te-quill-a! (Downs the

remainder of the tequila) Gummy worm’s done gone bad… (belches loudly again) Amanda: Jessica, have any idea what standards are? Jessica: (Puzzled) What now? Amanda: That’s it. I need something to take the edge off. You got a smoke? Jessica: (Taking out a pack cautiously) Yeah, but you don’t smoke cigarettes, Amanda. Amanda: (Taking the pack from Jessica) Yeah, well I do now.

(Cut to 25 years later. Amanda has been a smoker for many years now and has the voice to prove it. She is talking to her 12-year old child.) Amanda: (Takes a drag on a cigarette, then sighs) …And that’s when I started smoking. Sammy: So did you ever find the decent guy you were looking for, mommy? Amanda: No, Sammy, after that night at the bar I gave up on men altogether. That’s why I had to

adopt you to end the loneliness.

Sammy: (Shocked) I’m adopted?!?!? Why didn’t you ever tell me?!?!? Amanda: I thought it was kind of obvious seeing as you have no father. Well, it’s good that you

know now. I’m gonna go make dinner. You like pork, don’tcha?

(Ends with Sammy still shuddering after hearing that he was adopted.)
```

---

## IC-1473: My Mother Named me Hamlette

- Title: My Mother Named me Hamlette
- Author (byline): Anthony Doyle
- Work: My Mother Named me Hamlette
- Publisher: SpeechGeek
- Publication date as stated: 2017
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1848
- Already set (do not supply): none

### Source block (context only)

```text
My Mother Named Me Hamlette by Anthony Doyle
ISBN. 978-1-61387-112-6
Copyright 2017 by SpeechGeek.
Free performance of this play for high school and college level competitive forensics is
permitted. All other rights reserved.
This PDF version of this selection, e-published in 2015, is identical to the printed published
version of this same publication dated 2015. This statement along with the entire printed
PDF of this publication must be presented at any National Speech and Debate Association
District or National event for the script to comply with NFL rules per the request of the
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
[A SCHOOL HALLWAY]

MOM. Good morrow, Hamlette! Tis your first day of a new school year. HAMLETTE. This is an absolute nightmare. MOM. Goodly daughter Hamlette, why dost thou hide thy face in these

hallowed halls of education? HAMLETTE. In case you had not noticed, it is the first day of school and I am

on parade with my Shakespearean scholar mother and my

sickeningly smart and adorable little sister.
DESDEMONA. Hi.
HAMLETTE. Any hope I had of a normal, non-outcast year is gone.
MOM. Take heart, my dear Hamlette. For while thy face doth blush for

thy mother, ‘tis but a day that I intrude. HAMLETTE. You know, that's true. You will leave soon and if it were that

simple, I think I could get over it. But it isn't! MOM. Hamlette! What have I told thee about using contractions? DESDEMONA. “That it is commoner's speech, mother. It is a vernacular unfit for

the ears of a superior child such as I. That it shall be absorbed

and imitated, thereby hindering the development of my genius.”
HAMLETTE. That's exactly what I'm talking about!
MOM. Hamlette!
HAMLETTE. That is exactly what I am talking about.
MOM. Much better. Now then, Hamlette, thy sister, Desdemona, needs

additional social development before she casts off this mediocre

coil and matriculates to university. HAMLETTE. Right. You have to enroll my 7-year-old freaky smart sister in all

my classes because she needs to make friends. Except that she

(points)— DESDEMONA. (scribbling in a notebook and gawking at other kids) Fascinating!

It is the adolescent sociological phenomenon at work.
HAMLETTE. —Is like friend repellent…for me!
MOM. Thou art dramatic, Hamlette.
HAMLETTE. And whose fault is that. you named me Hamlette!
DESDEMONA. Hark! The bell hath rung! And we have reached my first class!

Huzzah! MOM. Huzzah! HAMLETTE. And so begins the great tragedy of my life.

Margaret Mead once said, “Sister is the most competitive relationship in the family, but once the sisters are grown, it becomes the strongest relationship.” While Mead’s words may eventually prove true for Hamlette and her baby sister Desdemona, when it comes to the growing up part…aye there’s the rub. As they navigate the drama of middle school, friendships and Shakespeare, they each learn the blessing and burden of sisterhood and both are reminded this above all, to thine own self be true. My Mother Named me Hamlette by Anthony Doyle

[A SCHOOL HALLWAY, MOM HAS JUST LEFT]

DESDEMONA. Farewell, Mother. Parting is such sweet sorrow.

HAMLETTE. Whatever. Look, Dez, don’t get me wrong. I love you and we

actually get along DESDEMONA. Mostly because we do not have much in common. HAMLETTE. Exactly. I mean, really—what am I going to do, steal your math

textbooks? DESDEMONA. Haha, no. You wouldn’t understand them. HAMLETTE. The point is I want you to get along at school. For your sake and

mine. So here are the ground rules— DESDEMONA. Oh, Mother and I already discussed the skills I will need.

[FLASHBACK TO THE PREVIOUS NIGHT]

MOM. Now, Desdemona, pray thee let us try it again. “Good morrow,

new student. That is a nice book bag you have there.” DESDEMONA. Thank you MOM. “Would you like to buy some drugs? They will make you

smarter.” DESDEMONA. No thank you. Drugs are incongruous with my health and life

goals. Perhaps we could partake in some dry roasted almonds,

instead? MOM. Huzzah!

[FLASHFORWARD TO PRESENT]

HAMLETTE. Ugh. DESDEMONA Is that incorrect? My research shows a high favorability for

adolescents and dry roasted almonds— HAMLETTE. Dez, here is a simple rule of thumb. Just…don’t be you. Can you

do that? DESDEMONA. Although I cannot fully comprehend the necessity of

compromising myself for the sake of assimilating to the group, I

trust your experience in the matter.

[THEY ENTER THE CLASSROOM]

TEACHER. Brittannie Gwen?
BRITTANI. Here!
TEACHER. Stefani Gwen?
STEFANI. Double here.
HAMLETTE. Ugh, the Gwens? I can’t even believe they made it to eighth

grade.
STEFANI. I know, right? I mean, hey!
BRITANI. A little late, aren’t we, Spamlet?
TEACHER. Late on the first day, Hamlette? Not an auspicious start to the year
DESDEMONA. I agree sir, better three hours too soon than a minute too late.
TEACHER. Ah, quoting Shakespeare! Very good young lady.
DESDEMONA It is a reflex.
HAMLETTE. Sorry Mr. S. We won’t let it happen again.
TEACHER. And who is your friend?

DESDEMONA. Desdemona Richards. Newly matriculated.
HAMLETTE. Don’t curtsied.
TEACHER. Desdemona! Do you go by any other names?
DESDEMONA. A rose by any other name would—
HAMLETTE. Dez! She’s goes by Dez.
BRITTANI. Is it “bring your dorky sibling to school day?”
HAMLETTE. Yeah, that’s why your sister brought you.
STEFANI. Nah-uh. Mom made me.
TEACHER. Now, now kids, either you quit all that or I’m sending you to the

office. What’s it to be?
DESDEMONA. (gasps) To Be or—
HAMLETTE. (covers her mouth) She has tourettes. We’ll just sit down now.
TEACHER. Well, I’m glad you’re all sitting because I think you’ll all be

particularly interested in our inter-disciplinary project this term.

Especially you and your sister, Hamlette. HAMLETTE. Uh-oh. TEACHER. We’ll be doing an eight-week segment on A Midsummer Night’s

Dream. Written by…
DESDEMONA. Ooooooh!
HAMLETTE. No.
TEACHER. William Shakespeare!
DESDEMONA. Huzzah!

[HAMLETTE AND DESDEMONA’S HOUSE, LATER THAT DAY]

HAMLETTE. That was a complete disaster! MOM. (sword fighting for fitness) Anon! My scholars are returned!

HAMLETTE, why dost thou face hang low and foul?
HAMLETTE. Why not ask my brilliant little sister?
DESDEMONA. I know not of what you speak, dear sister.
HAMLETTE. Oh, you “know not?” How about the scene you pulled in science?
SCIENCE TEACHER. The skull is a very important bone in your body…
DESDEMONA. Alas, poor Yorick…Hamlette, I knew him…
HAMLETTE. Or home-ec?
DESDEMONA. What light through yonder window bakes? It is the yeast! And

Juliet has the buns! JULIET. (as she eats the buns) Lay off me, I’m starving! HAMLETTE. And I don’t even want to mention what happened during

dodgeball DESDEMONA. What, art thou drawn among these heartless hinds? Turn thee,

Benvolio, look upon thy death. MOM. Methinks these seem perfectly reasonable responses. HAMLETTE. Says the woman doing ye olde aerobics Ugh. It was bad enough

when I just had to deal with you two at home. Why can’t you just

act normal? DESDEMONA. Because I am not what one would consider normal due to my age

and intellect. It would be contradictory for me to act in the way of

a standard student. HAMLETTE. Ugh!

DESDEMONA. Oh, Mother! Before I should forget, I have news! Among my

adventures today, I made two friends.
MOM. How fortuitous!
HAMLETTE. Wait, what? WHO?
DESDEMONA. Brittannie and Stefani.
HAMLETTE. The Gwens? Hahahahaha. No, Dez. They aren’t your friends.
DESDEMONA. Yes, yes they are. I was paired with them in a group assignment.

We got along like crusty bread and mead! HAMLETTE. Dez –

[DOORBELL RINGS]

STEFANI. Yoo-hoo
BRITTANI. We are outside the front door.
HAMLETTE. No way. (opens door) Seriously?
BRITTANI. Seriously.
HAMLETTE. Dezzie, you can’t be friends with them.
STEFANI. And why not, Spamlet?
HAMLETTE. Because you are not friends with people like us. You don’t even

talk to people like us. Not unless you count your repeated

renditions of “Spamlet’s Mommy wears a cape like Batman” BRITTANI. Oh my god, I love that song. DESDEMONA. I do not understand why you are so upset with me, Hamlette. I am

making friends! STEFANI. Bestie friendsies. Like Hermia and Helena in the Middle

Summer’s Ice Cream.
BRITTANI. Mmmm, Ice Cream.
DESDEMONA. No, that is incorrect.
STEFANI. Oh right, cuz they aren’t besties in the play. Cuz when Dmitri and

Lysol- DESDEMONA. Demetrius and Lysander. STEFANI. Whatever. When they both start liking Helena, Hermia gets mad

at her. And they get in this huge fight. It’s not Helena’s fault that

they like her. Right? HAMLETTE. Whoa. That question sounds A LOT like the homework

assignment on character relationships in the play.
DESDEMONA. Hermia thinks that they are playing a mean joke on her.
HAMLETTE. Gasp! You’re using Dezzie to get ahead in English!
STEFANI. Pfft. Fftt. Shhhht. Pfft.
BRITT. God Bless You.
STEFANI. Dezzie, do you think we could have some privacy?
DESDEMONA. Oh, of course. You may leave us now, Hamlette.
HAMLETTE. Dezzie! They aren’t your friends. They probably just want you to

give them the answers for their stupid presentation! DESDEMONA. How would you know? You don’t like them. It is obvious that you

are envious of their social stature and, thus, my interaction with

them. HAMLETTE. That’s not it. I’m trying to help you.

DESDEMONA. By telling me not to be me? By telling me I cannot speak or

participate or make friends? I do not need your help anymore.

Hamlet, I am doing just fine on my own.
HAMLETTE. And just like that, my genius little sister became an idiot.
DESDEMONA. You would know.
HAMLETTE. Wherefore was I to this keen mockery born? When at your hands

did I deserve this scorn?
DESDEMONA. Get thee to a nunnery, Spamlette.
HAMLETTE. You curly-haired wretch!
DESDEMONA. Fair thee well!
BRITT. What just happened…?
STEFANI. I think it’s like Hippolyta. Right, Dezzie? Cuz she’s such a good

representation of Shakespeare’s feelings of the female as a slave? DESDEMONA. Hmmm…?

[THE CLASSROOM, A WEEK LATER]

TEACHER. For our first presentation, Stefani and Brittani Gwen will introduce

the life of the Bard. HAMLETTE. I bet they didn’t come up with a single word of this. STEFANI. William Shakespeare was born in 1564, in Strapping-Up-An-oven,

New England.
HAMLETTE. Pfft.
BRITTANI. Bless you.
STEFANI. As a child, he enjoyed horseback riding and playing the

accordion. HAMLETTE. Ffft – wait, what? BRITTANI. Yeah, and his famous friends included Benjamin Franklin,

Leonardo DaVinci, and Mozart. And most people think he was

just a writer, but he also discovered Oregon and named

Williamette valley after himself. STEFANI. An excellent point, Britt. I also believe our lives would be totally

unliveable if the Bard had not invented Bardbie dolls…
TEACHER. Ladies! That is quite enough.
STEFANI. What?
TEACHER. You’re just making things up. And that’s an insult to the bard and

to my class. You should be ashamed.
STEFANI. No wait, we…but…Dezzie…
DESDEMONA. Though she be but little, she is fierce.
HAMLETTE. Huzzah! And my Mommy wears a cape…because she’s better

than batman! TEACHER. Stefani and Brittani. Come with me please. HAMLETTE. Dezzie! That was amazing. They hadn’t even double-checked to

make sure that your information was accurate!
DESDEMONA. Mmmhmmm, I can be wrong. Sometimes.
HAMLETTE. We all can be wrong sometimes.
DESDEMONA. I think I’ve known they were using me for a while, but I wanted

you to be wrong. Even though that’s not logical. Are you mad at

me?

HAMLETTE. No, Dez, I’m not mad at you. I’m proud of you. Just the way you

are. But I am sorry. I know you wanted them to be your friends. DESDEMONA. Who needs them? I’ve got you. HAMLETTE. Having a brainiac little sister is tough enough, but when she’s not

only smart, but you kind of like her, that makes it even worse. DESDEMONA. Huzzah! HAMLETTE. …huzzah.
```

---

## IC-1474: Next of Kin

- Title: Next of Kin
- Author (byline): Jane Nicolaas
- Work: Next of Kin
- Publisher: SpeechGeek
- Publication date as stated: 2011
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2027
- Already set (do not supply): none

### Source block (context only)

```text
Next of Kin by Jane Nicolaas
ISBN: 978-1-61387-033-4
Copyright 2011 by SpeechGeek.
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
SARAH. Wake up. It’s time to eat.
JANE. I don’t want to.
SARAH. Well, sorry. You have to.
JANE. Like you care.
SARAH. About you? No. About your husband? Yes.
JANE. How is he? Where is he?
SARAH. He’s stable. But still in the ICU.
JANE. How long will he be in there?
SARAH. Until he gets better.
JANE. Why are you here, Sarah?
SARAH. Because I can’t be in there, Jane. Now…

(gestures to the food) JANE. I didn’t see the truck. SARAH. I know you didn’t see the truck. If you would

have seen it, you wouldn’t have hit it. JANE. You still think this is my fault. SARAH. You know, of all the things that I blame you for,

this is shockingly not one of them. JANE. Thank you…I guess. SARAH. I’m not doing it for you.

INTRO

JANE. I don’t like uncomfortable silences. SARAH. Then go to sleep. JANE. I’d like to talk. With you. I mean, I know it’s not a

great time to do this, but I’d like to just the same.

I have questions.
SARAH. Such as?
JANE. Did you ever worry that he was cheating on you?
SARAH. You mean, “Did I worry while he was cheating on

me with you?” Not particularly. I was always

busy and I wasn’t around much, so I didn’t have

a lot of free time to speculate and suspect.
JANE. I’ve worried about it.
SARAH. Makes sense.
JANE. I’ve worried about it with you. I mean, he still

loves you. He always will. Even all that hatred

during the divorce was only possible because of

how much you meant to each other. And with

you two recently becoming close again…
SARAH. I told you it made sense.
JANE. Way to put my mind at ease, Sarah.
SARAH. That’s not why I’m here. But there’s nothing to be

jealous of. JANE. Easy for you to say. You don’t know what it’s like

to be married to Sarah’s ex-husband. SARAH. Yeah, sure. JANE. He tells me stories sometimes. Like how he

proposed. How he hid the ring in a chocolate

covered strawberry. How you cracked your

tooth on it when you bit down. How you said you

would only marry him if he could find you a

tweny-four-hour dentist. Not an easy act to

follow. SARAH. You make it sound like Grey’s Anatomy. It wasn’t

romantic at the time; it was painful and he was

ticked off about it. JANE. He never said that. SARAH. Well, you know as well as I do that Sam’s

memory is somewhat selective. Besides, he told

me that he proposed to you on a bridge on

Christmas Eve with a puppy.
JANE. I told him I didn’t want a ring.
SARAH. Clearly he had some romance left over for you.
JANE. I was allergic to the dog. We had to give him

away. SARAH. His romance is a very rare vintage.

(pause) JANE. Did he…ever tell you how we met? SARAH. No. I don’t know if I was ever brave enough to

ask.
JANE. It was at a book signing for Francis Anderson.
SARAH. Francis Anderson?
JANE. Yeah, it was for you. He told me while we were

waiting in line. Said he hated Anderson with a

passion and the only reason he could even stand

to be in the same room with the windbag was to

get a signed book for his wife. For Christmas. SARAH. Yeah. JANE. I fell in love with him then. A man who would

stand in line for hours on end waiting on an

author he hates just for a scribble for the woman

he loves.

SARAH. He gave it to me the second he got home.

Couldn’t wait until Christmas, I guess. JANE. I know. He said he worried that you would go

get the book yourself so…he had to ruin the

surprise. SARAH. Thank you. I…I didn’t know that part of the story.

God, I even remember the fight we had about

that book. I didn’t get what the big deal was and

I had to go to a meeting and… It’s weird to know

the day you started seeing my husband. JANE. It wasn’t like that. We really were just friends. SARAH. Until you weren’t. JANE. Until we weren’t. Sorry. SARAH. Bit late for that. JANE. But you two are hanging out again, right? SARAH. Not really the word for it. We have lunch once a

week. It’s…nice. JANE. Just nice? SARAH. Honey, sometimes familiar and nice are the best

a thing can be. When you’re done being twenty-

six and get a little closer to my age, I think you’ll

understand that.
JANE. Fifteen years is not all that much of a difference.
SARAH. Fourteen.
JANE. It’s just time. That’s what Sam always says, “It’s

just time.”
SARAH. Ha! As if Sam was a reliable source on this one.
JANE. Meaning?
SARAH. Ok, who were you fifteen years ago?
JANE. An eleven-year-old.
SARAH. Uck. Whatever. Was that person the same

person you are now? JANE. Legally. SARAH. No way. You and that girl wouldn’t even know

each other face-to-face. Time is the decisions

you make, the mistakes, the relationships, the

days, the trips, the scars. I don’t expect that to

make sense to you yet.
JANE. You don’t have to be old…
SARAH. (gives her a hard look)
JANE. …er to understand that. Time is the only thing

that separates you from being dead. SARAH. Exactly. Time is what it takes to grow up, to grow

apart. JANE. Or to grow back together?

SARAH. Huh? JANE. He’s been happier lately. I can see it. SARAH. And you think it’s me? Believe me, Sam’s

happiness has rarely--if ever--been the result of

me.
JANE. You two…you’re…in love again.
SARAH. No, we’re not and we won’t be.
JANE. Why not?
SARAH. Why are you even asking that?
JANE. Because you love him.
SARAH. Of course I do. Do you honestly think I’d be

nursing my ex-husband’s mistress-slash-new

wife if I didn’t still love him?
JANE. So…?
SARAH. So what? What do you want me to do?
JANE. Admit it. Admit that you love him.
SARAH. I have. I do.
JANE. And admit that you think this whole thing is my

fault. SARAH. Fine. JANE. And that you’re hoping that you can use this to

make him come back to you.
SARAH. Jane. No.
JANE. It’s ok. I totally get it.
SARAH. Clearly you don’t.
JANE. You’re fighting to get him back.
SARAH. Nope. Already tried that. I lost. Remember?
JANE. So you just give up? You quit?
SARAH. Look, I don’t know what kind of brain damage

you sustained in the crash, but you do realize

you are actively coaching me to try to steal your

husband, right? JANE. So you’re thinking about it then? You’re thinking

about doing it? SARAH. Just shut up. Ok? Shut up. This may be hard for

you to understand, but sometimes it’s not about

winning or stealing. Sometimes it’s just about

fighting for someone’s happiness…even if it’s

not your own. You make Sam happy. I’m trying

to keep you alive and calm until he comes out of

that stupid ICU. Simple as that. JANE. Simple as that? You expect me to just accept that

you are here out of some weird altruism? Sorry,

nobody is that selfless.

SARAH. Well, it’s selfless or helpless and either way I’m

less for it. JANE. That was weirdly poetic. SARAH. Yeah, well, I’ve been looking at get well soon

cards all morning, sort of short-circuits your

sentiment maker.

(pause) JANE. I have to tell you something. SARAH. Is that something the reason why you are

pursuing this ridiculous conversation?
JANE. I know you blame me for your marriage failing.
SARAH. God, do you ever shut up?
JANE. Neither of us–him or me--we never wanted to

hurt you. SARAH. Ok, you’ve said your something. Asked your

questions. I think it’s time for you to stop talking

now.
JANE. I want your forgiveness.
SARAH. Why?
JANE. Because I think…if you can forgive me. Then I’ll

know you’re not trying to steal my husband. SARAH. You mean steal back my husband? And what if I

am? What if that’s exactly what I’m doing here?
JANE. I can’t say I’d blame you.
SARAH. What would you say?
JANE. I’d say, “I told you so.”
SARAH. Look Jane, I give up, ok? Obviously I can’t tell

you this in a way you’ll believe. So… JANE. Just promise me you’ll take care of him. SARAH. God, you’re like a stubborn two-year-old. I am

not trying to— JANE. Promise me that you’ll take care of him and that

you’ll keep him safe. SARAH. Safe? God, you sound like you’re trying to give

your husband to me. JANE. It’s just like you said. When you love someone

you fight for his happiness. SARAH. Jane, grow up. Get your head out of your ass. JANE. Of all people I would think you would

understand this. SARAH. Well, I don’t. Do you think he’s just some puppy

you can give away? JANE. No. SARAH. You think that since you stole him so easily he’s

easy to pass around?

JANE. No. SARAH. You’re damn right no. Sam is impetuous and self-

righteous and overly sentimental, but he’s a

good guy. He deserves better than to be put up

for some sort of husband adoption. JANE. What do you want me to do, Sarah? I’d rather

give him up willingly than watch him leave. I

don’t want… SARAH. What? JANE. I don’t want to become you! Some pissed off

woman who hangs around her ex’s new wife for

some weird feeling of superiority. SARAH. That’s not what I’m doing. JANE. What is it, then? Are you here to tell me how

stupid he was? How much better off he’d be with

you? ‘Cuz I know all of that. You think a stupid

woman who drives into a parked car doesn’t

know how much better off her husband would’ve

been if she had just let him stand alone at a book

signing? I already feel guilty. SARAH. For God’s sake, so do I! Why is this all about

you? Why must it be about Sam? Maybe I didn’t

want to become me either. Nobody wants to be

the pissed off woman who was too busy for her

own marriage. Hate to break it to you missy, but

letting him go willingly and watching him

leave…I’ve done both and they both suck. So

just…shut the hell up, ok? JANE. (realizes) You’re not here to steal him back.

You’re here because…because you weren’t

there before. Is that is?
SARAH. Congratulations. What do you want, a prize?
JANE. Wow.
SARAH. Better late than never, right?
JANE. That’s really…amazing.
SARAH. Don’t go nuts, ok? It’s not like I’m giving him a

kidney or something. I’m just…here. JANE. Sometimes here is the best a person can be. SARAH. Yeah.

(pause)
JANE. I’m sorry I yelled at you.
SARAH. Don’t worry about it.
JANE. And thank you for yelling at me. I guess I

needed that. SARAH. Don’t mention it.

JANE. And I’m sorry I tried to…give you my husband. SARAH. Ha. Definitely don’t mention that one. Sam’d be

pissed.
JANE. He’d be livid.
BOTH. He’d probably cry.
SARAH. Maybe we’ll call it temporary insanity.
JANE. Or a head injury.
SARAH. Or a medicinal side effect.

(both laugh) JANE. We were both wrong before, you know. You’re

not just a pissed off ex-wife. You’re a good

person, Sarah. I can see why he loves you so

much. SARAH. And you are a pain in the ass. I can see why he

loves you so much. JANE. I’m glad you’re here. SARAH. Strangely, me too. And as far as that forgiveness

thing goes. No, you can’t have it. You don’t need

it. You were there when I wasn’t. No wrong in

that. JANE. Thank you. SARAH. Yeah, well. Like I said, I’m not doing it for you.

Not just for you, anyway.
```

---

## IC-1475: Non Omnis Moriar

- Title: Non Omnis Moriar
- Author (byline): Kevin Cochran
- Work: Non Omnis Moriar
- Publisher: SpeechGeek
- Publication date as stated: 2014
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: OPEN, FLASHBACK, FLASHFORWARD
- Teaser before the introduction: No
- Spoken words (computed): 1742
- Already set (do not supply): none

### Source block (context only)

```text
Non Omnis Moriar by Kevin Cochran
ISBN: 978-1-61387-069-3
Copyright 2014 by SpeechGeek.
Free performance of this play for high school and college level competitive forensics is
permitted. All other rights reserved.
This PDF version of this selection, e-published in 2014, is identical to the printed published
version of this same publication dated 2014. This statement along with the entire printed PDF of
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
OPEN: CATHOLIC CHURCH FOYER. JUST AFTER SUNDAY MASS.

(FATHER LUCAS is shaking hands with parishioners and visitors.)

HENRY. Father Lucas, wonderful service. Just wonderful. LUCAS. (laughs) Well, thanks, Henry. HENRY. Listen, I brought a friend with me and I’d love to introduce you. He’s in town for the week. Church isn’t really his thing, but he’s the nicest guy. LUCAS. I’d love to meet him. HENRY. Sure let me find him. (leaves to find him) Ben? Ben?

(BEN enters. LUCAS’S face falls.)

HENRY. Father Lucas, I’d like you to meet…

FLASHBACK: COLLEGE PARTY. 10 YEARS EARLIER LUCAS and BEN meet. It is love at first sight.

BEN. (smiles warmly) Ben. LUCAS. (smiles dumbly, as they shake hands) Lucas.

FLASHFORWARD: CATHOLIC CHURCH FOYER.

(LUCAS and BEN shake hands. It is betrayal and heartbreak and shock at first sight.)

LUCAS. (struggles) Nice…To meet you.

INTRO

FLASHBACK: COLLEGE PARTY

LUCAS. I have to go.
BEN. You have to? You didn’t know this was a gay party?
LUCAS. No. I didn’t. I…I just thought it was a party.
BEN. With the theme “no girls allowed”…?
LUCAS. Well, some people say that’s the theme of Catholicism.
BEN. You thought it was a Catholic party?
LUCAS. I really should go. (Long moment. Lucas can’t make himself
leave. BEN smiles in triumph.) Sorry.
BEN. So cute.
LUCAS. I’m sorry?
BEN. You don’t have to keep apologizing.
LUCAS. No, I didn’t hear you. I mean, I thought you
said…something.

BEN. Tell me about this (picks the cross pendant up off LUCAS’S
chest)
LUCAS. It’s a cross. I was raised Catholic.
BEN. You were raised Catholic, or you are Catholic?
LUCAS. Um, both?
BEN. Then why wear the cross?
LUCAS. I’m going to seminary next year.
BEN. But if you’re Catholic – or really any type of Christian –
isn’t this an incredibly depressing fashion statement?
LUCAS. Ha. I never thought of that. I guess… well, it’s a reminder
of sacrifice. A symbol. It keeps me connected to a spirit of
love and keeps me in comfort.
BEN. Yeah…that’s the same reason I wear Calvin Klein’s (shows
underwear).
LUCAS. You’re mocking faith or me?
BEN. A little of both.
LUCAS. Mind if I ask why?
BEN. Mind if I ask for your number?

FLASHFORWARD: INSIDE THE CHURCH RECTORY.

(BEN enters nervously.)

LUCAS. Ben?
BEN. I, um, came to apologize about the other day. I really
didn’t even think about looking at who the priest would
be. I mean, I stopped checking years ago…I shouldn’t
have said that out loud. Sorry… I probably should have
called first.
LUCAS. That’s not necessary.
BEN. The call or the apology?
LUCAS. …
BEN. (sigh) Look, maybe we just need to talk?
LUCAS. Yes. But I’m not sure if here is the right place.
BEN. Why? Because we’re in “the big room?”
LUCAS. Yes.
BEN. Afraid your God will throw lightening bolts?
LUCAS. He’s not my God.
BEN. Well, he’s certainly not mine.
LUCAS. I see some thing’s never change.
BEN. And some things seem to change completely. Talk about a
boy who can alter.
LUCAS. (shakes his had, but smiles) Ben.
BEN. Lucas…
LUCAS. Most people call me Father now.

BEN. Well that would just seem dirty coming from me, don’t you
think?
LUCAS. (innocently) Don’t gloat.
BEN. Gloat?
LUCAS. Maybe that was the wrong choice of word, but you know
what I mean.
BEN. No, I actually don’t. Shocking, I know, to not know what the
hell you’re saying. But…
LUCAS. Please watch you’re language.
BEN. Why?
LUCAS. We’re in God’s house.
BEN. No, we’re in a house for God that people built. It’s no more
holy than a condo on 8th or a barn. After all, that’s where
Jesus was born.
LUCAS. Jesus wasn’t born in a condo on 8th. He was the miracle on
34nd street. No… wait…that was Santa.
BEN. Did you just make a joke?
LUCAS. …maybe.
BEN. You’re allowed to do that?
LUCAS. (joking again) It’ll cost me some Hail Mary’s, but yeah.
BEN. …I’m just a little caught off guard. And…I don’t know, lots
of big feelings.
LUCAS. Yeah, we’re sort of used to that in this place.
BEN. So anyway, I’m sorry. I bet you hear that a lot, too.
LUCAS. From myself and others, yes.

FLASHBACK: COLLEGE COFFEE SHOP

(Lucas has been rambling for quite some time.)

BEN. (spills coffee) Oops, I’m so sorry.
LUCAS. It’s fine. No use crying over spilled latte.
BEN. Guess not. Thanks for hanging out with me, I’ve had a
great time.
LUCAS. Me too. Although, I don’t usually talk so much.
BEN. It’s alright. I only had to remind you to breath three times.

(Offers him fruit) Apple?
LUCAS. (Looks at fruit for a moment) Ben, can I ask you something?
BEN. You just did.
LUCAS. How did you know you were gay?
BEN. (shrug) I think it’s the same way you know you believe in
God.
LUCAS. (fiddles with his necklace) Explain, please.
BEN. I don’t know. I guess it’s like your faith. It’s such a vital
part of you.
LUCAS. Think so?

BEN. Yeah, it is. It’s like this beautiful force that lights you up. It’s like…seeing you at your most alive. That’s what it’s like for me. Gay isn’t just what I am; it’s part of who I am. What does your God say about that? LUCAS. I bet. (takes off his necklace and puts it in LUCAS’S hand) He’s very happy to have made you. Just the way you are.

(They both look at their hands on one another. A charged moment passes.)

FLASHFORWARD: INSIDE THE CHURCH RECTORY.

BEN. You haven’t told any of them, have you? Your “flock.” Nobody knows. LUCAS. I don’t see the relevance. BEN. You’re joking, right? I mean, come on! You’re terrified they’re going to bring out the fire and brimstone and burn you at the stake, right? LUCAS. And why would they do that? BEN. Because you’re gay, Lucas! LUCAS. No. I’m a priest. BEN. And a priest can’t possibly be gay? LUCAS. I’m not saying that. I’m saying sexual orientation doesn’t matter when you’re married to the church. BEN. You can say that with a straight face? LUCAS. Not a straight face, no. BEN. This is nuts. You’re gay and you standing there in the uniform of your own oppressor and you’re cracking jokes— LUCAS. That’s really what you think? That I am some raging homophobic cliché, swimming around in self-loathing and hoping God will save me from my base urges? BEN. Aren’t you? LUCAS. No! There is a difference between letting religion hide you and letting faith define you, Ben. BEN. Look, hide yourself in whatever church closet you want. What’s it to me? LUCAS. I was always going to seminary. I was always meant for this life. BEN. You may have always been headed here, but you ran away from me and you know it.

FLASHBACK: COLLEGE CAMPUS BEN. Hey, wait up. I need a moment of your time, good sir. LUCAS. I can’t right now, I have to go.

BEN. Ok…is everything ok? I feel like you’ve been avoiding
me.
LUCAS. No.
BEN. No, you haven’t been avoiding me, or no, everything’s not
ok.
LUCAS. I don’t know.
BEN. What’s going on with you?
LUCAS. Ben, I’m really busy and stressed out and I can’t give you
what you want.
BEN. What I want? What’s that?
LUCAS. (very awkward moment)…time. A moment of my time. You
just said that.
BEN. Oh. Right.
LUCAS. I better leave. It’s just…
BEN. Yeah?
LUCAS. Nothing. It’s all nothing.

FLASHBACK: BEN’S COLLEGE DORM

(Lucas is drunk and throws a pebble/rock at Ben’s window. No sound.)

LUCAS. Dammit. Oh fine. Ben! BEN!
BEN. (half asleep) Lucas? What are you doing?
LUCAS. I am throwing pebbles at your window. I could’ve sworn I
hit it a few times.
BEN. The window is open.
LUCAS. That explains it.
BEN. Saint Lucas, are you drunk?
LUCAS. …Maybe.
BEN. Hang on. (leaves the window)
LUCAS. (to himself) Leave. Leave now. Turn and go, you idiot.
BEN. (Opens the door) Hey, come on in.
LUCAS. No.
BEN. It’s freezing out here.
LUCAS. I can’t stop feeling it.
BEN. You can. Just come inside and thaw out.
LUCAS. No, you don’t understand.
BEN. What’s going on?
LUCAS. …Nothing. I shouldn’t have come here. (Turns to go.
Stumbles. BEN catches him easily. LUCAS clutches him in an
embrace. After a tender and charged moment, LUCAS kisses
BEN softly, then retreats abruptly.)
BEN. Lucas, I think I love—

(LUCAS punches BEN in the face and runs away.)

FLASHFORWARD: INSIDE THE CHURCH RECTORY.

BEN. Then you just…disappeared. I asked all your friends, I tried to find your folks, I even looked up seminaries and started cold-calling them pretending to be an estates attorney. LUCAS. I needed to go. Or I wouldn’t have left. BEN. And that would have just been awful, would it? You told me you thought God loved me for being gay, but apparently not you, huh? Needed to cleanse yourself of me and my impurities? LUCAS. No. I didn’t condemn myself to this; I chose it. BEN. Whatever helps you sleep at night, Father. LUCAS. Why is that so hard for you to understand? BEN. Because you gave up something real. You gave up something real and sacred and ran away. LUCAS. I don’t see it like that. Wait, that came out wrong. What I meant— BEN. No, it’s fine. I think I finally understand you. (leaves) LUCAS. Ben!

FLASHFORWARD: CATHOLIC CHURCH CONFESSIONAL BOOTH

BEN. Bless me father, for I have sinned. LUCAS. (sighs) Ben. BEN. I thought this was supposed to be anonymous. LUCAS. I am glad you came back, let’s go— BEN. I’m just here for confession. And then I’m going. LUCAS. Ok, but you’re not Catholic. Confession won’t absolve you of your sins. BEN. You might be surprised. It might absolve us both. So, how do I do this? LUCAS. You admit your sins and then you are forgiven and we…we forget. BEN. Promise? LUCAS. (long moment of silence. No one knows what to say.)…I knew. BEN. What? LUCAS. I knew it wasn’t a Catholic party. In college. I knew. BEN. …Yeah. I just…I need to know…are you happy? LUCAS. I am happy here. I love my work and I love the Church. BEN. That’s…good. LUCAS. You’re wrong if you think you’re the reason I left.

BEN. Forgive me, Father… I have loved you every day. Every moment. LUCAS. No one needs forgiveness for love, Ben. And I promise you, I have never asked for forgiveness for loving you. I have asked for patience, I’ve asked for strength, I’ve asked for comfort…because I don’t think I’ve ever loved anything like I loved you. Like I will always love you. BEN. Always, huh? LUCAS. Always. BEN. Couldn’t you have lied, just this once? LUCAS. Some things never change. BEN. I guess not. But then again, some things have to.

OPEN: CATHOLIC CHURCH

LUCAS. (LUCAS delivers his sermon while BEN enters, removes the necklace that Lucas gave him years before and sets it down on the pew as Lucas delivers his sermon.) Friends, Paul said there are many types of love. There is the kind we feel for our friends and community, the passion we feel for our partners and spouses, and then there is the love we feel for God. It is self-donation without concern of cost or reward. Believe me when I say that this is the most challenging kind of love. But no matter the love we feel, or the people we feel it for, it is imperative that we remember that love is a gift and it is a blessing, in all its forms. It is the greatest of all things.
```

---

## IC-1476: Off-Stage

- Title: Off-Stage
- Author (byline): Matt Mills
- Work: Off-Stage
- Publisher: SpeechGeek
- Publication date as stated: 2015
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1301
- Already set (do not supply): none

### Source block (context only)

```text
Off-Stage by Matt Mills
ISBN: 978-1-61387-089-1
Copyright 2015 by SpeechGeek.
Free performance of this play for high school and college level competitive forensics is
permitted. All other rights reserved.
This PDF version of this selection, e-published in 2015, is identical to the printed published
version of this same publication dated 2015. This statement along with the entire printed
PDF of this publication must be presented at any National Speech and Debate Association
District or National event for the script to comply with NFL rules per the request of the
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
(Rich wearily addresses an audience from his stage.)

RICH. Do you want to hear a joke? The seven worst words in the English language. Right? Have you seen the looks on people's faces when they get asked that? “Do you want to hear a joke?” It's like you've offered them a roadside colonoscopy from a grizzly bear. Truthfully, I think people would prefer bears invading their body rather than jokes invading their ears. What's with that? We live in a world where ten bucks is a fair price for a cup of coffee, but is too much to spend on art? I swear we're all going to be completely illiterate one day.

I am, unfortunately, a stand-up comedian; but no, I do not ask people if they want to hear a joke. That's kind of implied with my line of work. People come and they pay money to sit in a dark room where they have to listen to me say whatever I want! For exactly five minutes, because when that red light goes on you better stop talking. They're serious about that red light, you know. There are “Roxanne” levels of red-light-drama in stand-up.

I started doing shows when I was a kid. When I was only nine months old! (He looks the audience over.) Of course not, you jerks! Just because I have a stage doesn't mean you should listen to everything I say! The moon landing was staged! Clinton killed Kennedy! Unicorns exist! Man, I love the gullible.

You know, growing up, my dad introduced me to all the greats...Johnny Carson, Richard Pryor, Lenny Bruce. He was always trying to give me a laugh after he'd given me a bad beating the night before. You see, he worked all day in the mine and would come home drunk and frustrated. The next morning, he'd be a father again. His favorite thing to do was just, well, he'd look at me and say "chin up". Chin up. But it's hard to keep your chin up when you keep getting knocked down.

I was 16 when I actually started doing stand-up in the city. My entire set was based around gym class and my, uh...self-enjoying habits, we'll call it... I quickly fell in love. Both with stand-up and...Jill (waves hand). I couldn't be stopped...doing stand-up, I mean! Oh man, that feeling when you get on that stage and the light hits you... It feels so warm; it just hypnotizes you. It can fool you into feeling like you belong. It gets addictive.

By 19, I had already done 200 shows. I know, I know—try to keep calm, ladies. Because in spite of all my hard work, those shows got me nowhere. Nothing. I never saw a dime or even an opportunity for one. Every time it was just “good job” but “better luck next time.”

I worked full-time down at the docks just to pay rent, and that didn't even leave any money for food…or anything else for that matter. No friends, no fun, no free-time, no joy… Just work and stand-up. My life was one constant struggle to survive. I needed to catch a break just to stay alive.

I entered contest after contest, amateur showcase after amateur showcase. But despite the hard work...the sleepless nights, the paralyzed mornings, that shaky feeling you get when something's wrong...only I had that feeling all day. Every day. Every minute, every second...I couldn't take it. I remember walking up to a producer...

“You know, I've been doing shows here forever. I bring in a crowd, maybe not the biggest, but I know I can do this for real. Please just give me a paid slot. I'm worth the money! Please. I need this. Let me prove it to you.”

But I didn't get the chance. Maybe it was the hunger pangs in my stomach, but I just started to get this sick feeling that no one was looking out for me and that everyone was using me. I quickly began to realize I was truly and completely alone— like I didn't belong in the world, like the world doesn't want me to belong. I'd leave the clubs, look up at the expensive skyscrapers above me, and for the first time in a while, I felt entirely hopeless.

That's when I got the call. There was this audition. The audition. Anyone invited had a shot to show a few club owners that they can hack it professionally. One chance to make it to the big leagues. My big break. All I had to do was go up there, win over the crowd, and they'd start giving me paid shows. Win over the crowd and I'd be able to eat for a little while. Who knows? Maybe I'd even become a success.

I worked on my material for weeks, breathed it in, slept, and had dreams about what I'd say. I imagined the best crowd, the worst crowd, short crowds, tall crowds, white crowds, purple crowds... Down at the docks I'd tell jokes to the guys, use them as a test audience. I'd tell a joke to the street-sweeper as I walked by or the policeman on the corner. There wasn't a second I didn't prepare, because I had no choice. It was either make it or starve.

Finally, the night of the show arrived. They called my name and I'm transported to another world. Like I'm in a trance, I walk on stage, look out at the audience, and give them the best performance of my life. I mean, you should've seen it; it was absolutely incredible. Guys were doing spit-takes and girls were laughing like they were split in half. It didn't seem real. I thought I was in a movie or something. It was my moment. My five minutes of paradise.

After the show, I walked up to the owners to ask what they thought. They just looked at me and said...

(We see Rich react to the owners speaking...)

Better luck next time? Next time? No, you don't understand. There is no next time! This was it. This was my time! Didn't you see them out there? They loved me! They loved me! I got on that stage tonight, and I mattered! No, you don't understand! I haven't eaten this week; my hands are bloody and overworked, I...what did you just say? Chin up? I should just...chin up? I'm a failure. And if there's one thing I've learned, it's that failures don't get to chin up. Failures don't get anything. Failures don't belong in this world, failures get...

(Rich grabs an owner, slams him to the ground and viciously beats him, repeatedly smashing his fist into the owner's skull.) ...beaten and beaten and beaten until they understand they should have never been born!

(Rich gets pulled off the owner, stumbles back, shocked by what he just did. Rich looks to the audience in awe. He looks down to his hands, realizes he's cuffed in a prison cell.)

That was it for me. The end of my career. What career. It was the end of my life. I've been in here for ten years now, and if I promise to be really good, I'll only have ten more. Which sounds pretty easy, since in prison “good behavior” just implies a lack of bad behavior. As if that's what makes you a good person. The lack of evil. But there are good people who do evil things. When all it takes for evil to succeed is for good men to stand by and do nothing...at least I did something.

It's not too bad in here though. I've made some friends I can tell jokes to. Every Friday we have a little open mic here in our cell. It's just a two person open mic, but it's better than nothing. At least in here there are no buildings to stare down at me. Nobody to tell me I don't belong. To chin up. I'm just in here trying to find the beauty in everything. I'm finding it's a lot easier when nobody's holding your eyes shut.
```

---

## IC-1477: Pinky’s Big Break

- Title: Pinky’s Big Break
- Author (byline): Brooke Anderson
- Work: Pinky’s Big Break
- Publisher: SpeechGeek
- Publication date as stated: 2017
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: PINKY, INDEX
- Teaser before the introduction: No
- Spoken words (computed): 1109
- Already set (do not supply): none

### Source block (context only)

```text
Pinky’s Big Break by Brooke Anderson
ISBN: 978-1-61387-306-9
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
```

### Introduction (context only: never use it for content warnings)

```text
(no introduction)
```

### Performance text (classify this)

```text
Facebook: www.facebook.com/speechgeek

PINKY. Hi! My anatomical name is Digitus minimus manus. My friends call

me Pinky. JEN. Good morning! (waves her hand) PINKY. (waving back and forth) Oh! I love the good morning wave! That’s

Jen. I am on her right hand. And every day me and the rest of the

righties do our best to help Jen out. Wanna meet the team?

They’re a handful! First, there’s Jen’s opposable thumb. THUMB. Alright! Look at me! This is awesome! You’re awesome! PINKY. He’s our team cheerleader. He’s strong, and confident, and he is

awesome at hitching us a ride. But he’s kinda far away. Then,

there’s Jen’s index finger. INDEX. YOU! What are you looking at? Get back to work! PINKY. He’s our number one! He’s the director. He’s very

encouraging…and accusatory. It’s complicated. Then there’s

Jen’s middle finger. He’s the conflict manager… MIDDLE. AHHHHH! PINKY. We don’t talk to him much. And then we have Jen’s ring finger. RING. Hi, you wanna be friends? Wanna be…more than friends? PINKY. She’s the relationship expert. And then there’s me. My job

is…well, that’s just the problem: I don’t really do anything. But all

that changes today. Because today is the day that I, Jen’s right

Pinky, take over the world! Or at least become more handy.

We all know what it means to overlook our own greatness and to sacrifice our identity to be popular. I mean, we all know it, but what about (looks at hand)...them. For one little pinky finger who is tired of experiencing life second-hand, the time has come, to rise...and be counted. Pinky’s Big Break by Brooke Anderson

THUMB. Hey, Pink, what’s that you’re saying?
PINKY. You heard me, Thumb. I just can’t take it anymore.
INDEX. Aren’t you being a little dramatic?
PINKY. No, I’m not. Need I remind you of what happened yesterday?

FLASHBACK

JEN. Yeah, thanks for calling. (hangs up phone) Man, I’ve got

something in my ear… (starts to put pinky in ear to scratch it)
PINKY. NO!!!!!
JEN. Nope. Just wax, I guess.
PINKY. Ugh. It’s like there’s Vaseline everywhere.

FLASHFORWARD

INDEX. Now that…was very gross. PINKY. I’m aware. THUMB. Aw, chin up, Pinky. It’s not always that bad. There was that one

time you got to wear that cool metal cape for a while!

PINKY. You mean when someone slammed me in a car door and I was

broken in three places? THUMB. Oh, right. Well, at least things can’t get any worse than that! And

hey, we’re going to see Annie later this week! PINKY. Annie! Annie is Jen’s niece. She’s the greatest. She’s the only one

who loves me. When they drink tea like proper English women,

that’s my shining moment. But Annie’s getting older. She’s almost

eight and tea parties hardly ever happen anymore. RING. And then you’ll be all alone. Like me. I JUST NEED LOVE! PINKY. See, Ring gets it! If I don’t assert myself and become more useful,

I’ll shrivel up and die. THUMB. Okay, so what’s your plan? PINKY. Well, the way I see it, there are three main criteria for a proper

digit: utility, communication, and dexterity. Currently, I...possess

none of these. But just you wait, soon the world will be wrapped

around this little finger.

TRANSITION – JEN’S BED

JEN. (Sleeping. The alarm goes off.) PINKY. It’s time! (Pinky moves as if possessed, hits the alarm. The

alarm changes to a more annoying sound. Pinky panics and

hits it again. It becomes the radio.) JEN. (finally wakes up) Huh!? What was that? PINKY. A strong start, that’s what that was! Already I’m feeling like the

favorite. Righties, did you see me? Did you see me? INDEX. Yeah, I saw you. You hit every button except snooze. You didn’t

even know which button to push. THUMB. Easy there, Pointer. Pinky’s doing a great job. I mean, totally

wrong, but still great. PINKY. Well, just you wait. I’ve got plenty of utility to pack into these

knuckles!

TRANSITION – JEN’S KITCHEN

JEN. (on the phone, making breakfast) Yeah, I’ll be in right after

breakfast, Gary. No, I just woke up late. Something weird

happened with my alarm clock and… (goes to push the

microwave button, but it’s Pinky again)
PINKY. (ramming his head into the button) Utility! Utility! Utility!
JEN. I don’t even know what’s going on today...
INDEX. Pinky! Did you just do my job? No one does my job.
PINKY: Don’t get all bent out of shape.
INDEX: No, that’s your job apparently. I’m the king of the microwave

buttons! Except when I have a hang nail, and then middle finger

does it. MIDDLE. AHHHHH! PINKY. Okay, I’m sorry. I didn’t mean to intrude. I just wanted to be more

useful.

INDEX. Well, be useful somewhere else.
PINKY. Okay. So utility isn’t my thing.
THUMB. There’s more to being a finger than utility, Pinky.
PINKY. You’re right! Like communication! Maybe a pinky could be great

for gestures and stuff. Might as well try my hand at it…

TRANSITION – JEN’S CAR

JEN. Ugh, I’m so late for work. I just can’t even. Yikes! (almost gets hit

by a car) - AH! - You jerk! (flips off the driver, but Pinky jumps up

too) What the?
PINKY. I TOO FIND FAULT WITH YOUR DRIVING, SIR!
MIDDLE. AHHHH! What are you doing?
PINKY. I was adding emphasis.
MIDDLE. I AM EMPHASIS.
PINKY. Well, maybe he thought it was a gang sign and he will freak out.
MIDDLE. I hope you get a paper cut.
PINKY. That’s a horrible thing to say.
THUMB. Don’t listen to him, Pinky. He’s just…him. I tell you what, why

don’t you and I team up. PINKY. Do you mean it? THUMB. You bet. After all, dexterity is a team sport!

TRANSITION – JEN’S OFFICE

JEN. I’ll have that report to you ASAP, Gary. Just having a rough day.
THUMB. Ready, Pinky?
PINKY. Ready!
THUMB. LET’S DO THIS!
JEN. (Jen writes, but with the thumb and the pinky. It’s awkward.) I

can’t…what the…ENOUGH! (looks at hand) What is going on?
PINKY. She’s looking right at me.
JEN. Quit being weird!
PINKY. Oh, okay.
THUMB. Awww, buddy. I’m sorry.
INDEX. Pinky, you’re just not meant to do all that stuff.
RING. Maybe it’s okay that no one loves you.
PINKY. Yeah. Maybe…

TRANSITION – JEN’S HOUSE

THUMB. Hey look, Annie’s here!
ANNIE. Hi, Auntie Jen.
JEN. Hi, kiddo! How’ve you been?
ANNIE. I don’t think anyone in my class likes me.
JEN. What? I’m sure that’s not true.
ANNIE. Yea-huh. I’m not strong, or good at talking to people, and I don’t

write good. PINKY. Preach it, sister.

ANNIE. And Ralphie Pederson said I was weird.
JEN. Well, I happen to think you have a lovely writing.
ANNIE. You do?
JEN. Yes, I do. People are good at different things, but nobody can tell

you how valuable you are. You just have to be you because that’s

my favorite.
ANNIE. Promise (holds up her pinky for a pinky promise).
PINKY. Guys, looks! Look what she’s doing!
ANNIE. It’s a pinky promise. It means you swear forever. No matter what.
JEN. I promise.
PINKY. (leans forward and completes the promise) Wow. So I may not be

the strongest, coolest, or most useful, but I am the best version of

me there is. Hands down.
```

---

## IC-1478: Proud to be a B

- Title: Proud to be a B
- Author (byline): Juniper Mariat
- Work: Proud to be a B
- Publisher: SpeechGeek
- Publication date as stated: 2017
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 377
- Already set (do not supply): none

### Source block (context only)

```text
Proud to be a B by Juniper Mariat
ISBN: 978-1-61387-113-3
Copyright 2017 by SpeechGeek.
Free performance of this play for high school and college level competitive forensics is
permitted. All other rights reserved.
This PDF version of this selection, e-published in 2015, is identical to the printed published
version of this same publication dated 2015. This statement along with the entire printed PDF of
this publication must be presented at any National Speech and Debate Association District or
National event for the script to comply with NFL rules per the request of the Executive Director.
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
Proud to be a B

When I
stand up for myself
and my beliefs,
they call me a ...

When I
stand up for those
those I love,
they call me a ...

When I
speak my mind,
think my own thoughts,
or do things my own way…

I’m defined.

When I refuse
to tolerate
injustice and hate
They say
I am hysterical
PMS-ing
Delicate female
Overstressing

But I’m just tough I’m just tough I’m just tough like heavy like rawhide like the hollowed out hull of a metal? Knotted, stretched, war ship Like the stuff at the bottom of dried out and hardened All cannons, no cargo the periodic table No predators want to use you middle finger sails high in Complex, rare, irradiated as a toy the sky and man-made

Tough like the mountains I’ve climbed to be seen Tough like the scars I hide and the layers built up inside

Because life is such a… And so am I, you say.

If you call me a b-word, then at least be creative.

Call me
Brazen for being loud
Buxom for being round
Brutish
Bratty
Breathless
Bulletproof
Ballsy by compare,
but Beware

Baptized in the fires of feminine repression,
obsession,
and progression
You can try to stomp,
stop,
or stunt me,
intimidate me
or frighten me.
douse my inner flame with more
handcuffs or hand granades
crush my spirit
or squash the beauty I hold within me.

But you won't succeed.

As women before me and beside me have proven
The soul of a woman doesn't crack
It's not the ball, it's the bat
It's the steady ready stance of a bull,
it's a trance
that keeps
you still
and safe.
Your soft parts erased.
Your demons replaced
With the hulking fire mouthed, steel scaled dragon that knights look at at say,
"Damn that’s one tough..."

Because we ought to be. Because we fought to be.

And if that makes me a bitch

so be it.

I embrace the title and I'm proud to stand up for myself, and my belief
Stand up for those, those I love
Speak my own thoughts, do things my own way
I’m proud to bear it.

Then call me a… Then call me a… Then call me a...
```

---

## IC-1479: Ricochet

- Title: Ricochet
- Author (byline): Jane Nicolaas
- Work: Ricochet
- Publisher: SpeechGeek
- Publication date as stated: 2015
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1779
- Already set (do not supply): none

### Source block (context only)

```text
Ricochet by Jane Nicolaas
ISBN: 978-1-61387-089-1
Copyright 2015 by SpeechGeek.
Free performance of this play for high school and college level competitive forensics is
permitted. All other rights reserved.
This PDF version of this selection, e-published in 2015, is identical to the printed published
version of this same publication dated 2015. This statement along with the entire printed
PDF of this publication must be presented at any National Speech and Debate Association
District or National event for the script to comply with NFL rules per the request of the
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
MAYA. Excuse me, Doctor Keller?
ELI. Ms. Miller?
MAYA. Maya, please.
ELI. Maya. It’s nice to see you. How’s your father?
MAYA. He’s great, well, thanks to you.
ELI. I don’t know about all that.
MAYA. No, I’m serious. You made all the difference.
ELI. (blushes) Well, I’m just glad I could help.
MAYA. Well, look…I came here because, well…I saw that you had a St. Louis

Rams cover on your phone and I…I bought two tickets to the game this

Sunday. I thought maybe we could go, if you wanted.
ELI. Maya, wow. I’m flattered, but…uh…
MAYA. You’re married.
ELI. No.
MAYA. Girlfriend?
ELI. No.
MAYA. Gay?
ELI. No! It’s just… I’m not supposed to date patients.
MAYA. Oh… Then I guess it’s a good thing my dad isn’t asking you out.
ELI. Okay. Sunday. You and me. That sounds fun. Can I come pick you up?
MAYA. Sure, that’d be nice, Doc.
ELI. Are you in downtown St. Louis? Or where do you live?
MAYA. I live in over in Ferguson.

INTRO

ELI. Knock, knock? Maya?
MAYA. Hey. I’m in back.
ELI. Wow. The shop looks amazing. It’s really coming together.
MAYA. Think so?
ELI. It’s wonderful. The grand opening is going to be one heck of a party. Am

I invited?
MAYA. Of course you are, silly.
ELI. Well, it’s just that I don’t want to be a distraction.
MAYA. Why? Cuz you’ll be the only white guy?
ELI. No. I meant I’d be a distraction to you.
MAYA. Right, of course. Ignore me. I’m just stressed out about inventory.
ELI. I could never ignore you. In fact… (pulls a bunch of flowers from behind

his back) These are for you. Happy anniversary!
MAYA. You are such a nerd.
ELI. Yeah.
MAYA. Well, thanks, Doc.
ELI. We’ve been together for six months. Don’t you think you could call me

by my name instead of my title?
MAYA. But you paid so much for it.
ELI. Ha.
MAYA. Eli, I’ve been thinking about something…
ELI. Okay.
MAYA. I’m…I’m in love with you.

ELI. Don’t sound so thrilled. MAYA. No, no it’s not that. I am thrilled. You’re amazing. It’s all the other stuff

that worries me. ELI. Other stuff? MAYA. It’s just…the stares on the street, the way waiters always ask if we’ll need

separate checks, your neighbors never— ELI. Hey, listen to me. All of that is crap. This. You and me. That’s what’s real.

Maya, I look at you and I don’t see the color of your skin. I see a beautiful,

smart, kind, and lovely woman whom I…well, you can read the card with

the flowers. MAYA. (She does. It says he loves her.) Hmm. Such a nerd. ELI. Indeed. Now then, how about you find a vase for those and I’ll pop the

cork on some wine, find a good song on the radio and I’ll help you stock

inventory. MAYA. Happy six month anniversary? ELI. The happiest. (He kisses her and she leaves. He turns the radio on.)

RADIO. And in local news, a police shooting has left an 18-year-old black teenager

dead. While the details of the case have not been released, it has been

reported that the 18-year-old, Michael Brown, was unarmed.

MAYA. (enters) God. That’s awful. ELI. It is. Terrible. But I think… (he switches the radio to music) This isn’t so

bad. (he pulls her to him and starts to dance) MAYA. Eli… ELI. One dance, and then we’ll do inventory. Promise.

TRANSITION RADIO. Rioting continues in Ferguson as citizens demand justice for the slain

Michael Brown. Severe damages and looting has been reported. The

National Guard has been called in.

MAYA. Eli?
ELI. Thank god. I’ve been trying to call you for hours.
MAYA. Why?
ELI. Here. Take my keys. Get your Dad, and go to my house.
MAYA. No, it’s fine.
ELI. You’ll be safe there. I’ll be home as soon as I can, but the emergency

room has been flooded with these idiot rioters. MAYA. I don’t want to hide in your apartment. ELI. We’ll go by the shop once this insanity calms down. I’m sure

everything’s fine, but you never know with mobs of people running

around and causing all kinds of—what are you wearing? MAYA. “Hands Up, Don’t Shoot” It’s the protest slogan. ELI. Yeah. I’ve heard it on the radio. Is that where you were? You were out

there in that craziness? MAYA. It wasn’t that crazy. I mean, I know the news makes it look bad, but most

of us are just marching and peacefully demonstrating. ELI. Most of “us?”

MAYA. Yeah. My dad is out there with me and my neighbors. There’s a lot of

people who are standing up to this.
ELI. (uncomfortable) Okay...
MAYA. Maybe you can join us after work?
ELI. I won’t be done until morning.
MAYA. Something tells me we’ll still be out there. (kisses his cheek) Bye. (she

leaves) ELI. Love you, too.

TRANSITION RADIO. The Justice Department announces that it will open a broad civil rights

investigation. Citizens have been galvanized by the inquiry and are calling

for sweeping changes to the police force and the community at large

declaring “Black Lives Matter.”

ELI. (on the telephone) Maya?
MAYA. Eli?
ELI. Where are you? I can barely hear you.
MAYA. Eli? Hang on. Sorry, we are outside the courthouse.
ELI. I’m at the restaurant.
MAYA. You didn’t get my email?
ELI. The one about you not coming to the restaurant? I guess not.
MAYA. Are you mad?
ELI. I just—
MAYA. Look, I am sorry. This is important.
ELI. So am I.
MAYA. What? Look, I can’t hear you, Doc. I’ll call you back later.

TRANSITION RADIO. The grand jury still hasn’t reached a decision around whether or not to

indict Officer Darren Wilson in the shooting of Michael Brown. But both

racial tensions in Ferguson have reached a fevered pitch.

ELI. (turns off the radio) God, isn’t there anything else to talk about?
MAYA. …
ELI. I just meant, you know. It’s been three months.
MAYA. And you’re ready to move on.
ELI. Yes. I mean, no. That sounds callous.
MAYA. Yes, it does.
ELI. Hey, come on. I didn’t mean it like that. I just hate seeing everyone so

unhappy. Especially you. I mean, when was the last time I got you to

laugh, huh?
MAYA. I don’t really feel like laughing. This isn’t something you can laugh off.
ELI. (gives up and gets frustrated) Okay. Fine.
MAYA. 92% of all people arrested in Ferguson last year were black.
ELI. Right.
MAYA. Despite the fact that only 65% of the community is black.
ELI. Are you done?

MAYA. And nationally, 98.9% of excessive force allegations are ultimately ruled

as justified.
ELI. Maya, stop it!
MAYA. Why? Does it make you uncomfortable?
ELI. Hey! It is awful what happened. A cop, taught to shoot first, and a kid who

got caught in the crossfire. It’s all awful, but I don’t—
MAYA. A white cop taught to shoot first at a black kid.
ELI. Yeah…and?
MAYA. You don’t think that has anything to do with you and me?
ELI. Just because there are ignorant people in the world doesn’t mean you

and I change.
MAYA. Eli—
ELI. Yes, racism is real. I get that.
MAYA. Eli—
ELI. But I’ve told you before, I don’t see color.
MAYA. Maybe you should! I am black! It’s not something you should ignore.
ELI. What?! Because I don’t pay attention to your race, I’m a racist?
MAYA. I didn’t say that. But all you white people act the same around this…
ELI. Us white people?!
MAYA. Like racism is some bad penny that keeps showing up in your pocket. “I

thought we got rid of this,” you say. So you shove it down and bury it, but

it doesn’t go away.
ELI. It doesn’t go away because people don’t let it go away.
MAYA. People?
ELI. Well, it certainly isn’t “us white people.”
MAYA. Now you’re just being a jackass.
ELI. Oh, am I?
MAYA. Yes, you’re being an ignorant jackass.
ELI. Well, it beats being a martyr. I am sorry, but I am not going to stand here

and have you tell me that I am racist meanwhile you’re the one who can’t

stop talking about the color of my skin.
MAYA. I can’t stop talking because you won’t start talking, Eli.
ELI. What do you want from me, Maya?
MAYA. I don’t know… I want you to acknowledge that there is a problem and

that it involved everybody.
ELI. Why do you want that?
MAYA. Because I want to make a difference. Don’t you?
ELI. No! I don’t want to make a difference. I want a relationship. But it sure as

hell looks like that’s not happening.

TRANSITION RADIO. Protestors have restlessly gathered outside the courthouse and the

Ferguson police station in anxious anticipation of the grand jury’s verdict.

ELI. Maya?
MAYA. What are you doing here?
ELI. Look, I know that you’re probably still mad at me.
MAYA. Probably?

ELI. Okay. You’re pissed. But…look, I thought about what you said. You were

right. I figured I wasn’t part of the problem and that made me part of the

solution, but that’s not true. I get that now. MAYA. You do? ELI. I tried to put myself in your place. I tried to see all of this from your eyes,

but I couldn’t. I didn’t understand it, so I just…ignored it. But that’s just it,

isn’t it? Evil stuff doesn’t happen because the world is full of evil people.

It happens because the world is full of passive people who think that the

bad stuff has nothing to do with them. I don’t want to be passive. I don’t

want to be ignorant. I…I don’t know what to say. I don’t know a lot of

things. But I do know that you being black isn’t just something I tolerate.

It’s part of who you are, and who you are is who I am desperately in love

with. MAYA. Good speech. ELI. Yeah? I thought it got a little rough in the middle. It was better when I

practiced in the car.
MAYA. You’re such a nerd.
ELI. I am.
MAYA. This isn’t something that goes away, Eli. This is a conversation we will

always have – consciously and unconsciously. ELI. Okay. I can accept that. As long as you’re willing to accept that I won’t

know what to say a lot of the time.
MAYA. So, sorta how most of our other conversations go anyhow?
ELI. Ha.
MAYA. You might not know what to say, but that doesn’t mean you stop talking,

okay?
ELI. I promise.
MAYA. I do love you, Doc.
ELI. I love you, too.

RADIO. No matter the outcome of the grand jury decision, one thing is certain: the

world should and will be a different place after today.
```

---

## IC-1480: Scared to Death

- Title: Scared to Death
- Author (byline): Doug McConnaha
- Work: Scared to Death
- Publisher: SpeechGeek
- Publication date as stated: 2016
- Event as filed: Not specified
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1430
- Already set (do not supply): none

### Source block (context only)

```text
Scared to Death by Doug McConnaha
ISBN: 978-1-61387-098-3
Copyright 2016 by SpeechGeek.
Free performance of this play for high school and college level competitive forensics is permitted. All
other rights reserved.
This PDF version of this selection, e-published in 2016, is identical to the printed published version of this
same publication dated 2016. This statement along with the entire printed PDF of this publication must
be presented at any National Speech and Debate Association District or National event for the script to
comply with NSDA rules per the request of the Executive Director.
This and other selections of quality performance literature for competitive oral interpretation are
published by SpeechGeek.
For more information and performance rights, contact SpeechGeek.
SpeechGeek
248 Arlington Park Dr.
Hot Springs, AR 71901
Phone: 1-888-742-2028
Email: thegeek@speechgeek.com
Web: www.speechgeek.com
Facebook: www.facebook.com/speechgeek
2
```

### Introduction (context only: never use it for content warnings)

```text
(no introduction)
```

### Performance text (classify this)

```text
The first time I remember being really scared was the summer when I was seven years old. My older sister and I had decided to camp out in the back yard in a tent. My folks came out and tucked us in. My dad stayed long enough to tell us a scary story about a ghost with an axe who wandered around looking for his head. Dad was holding the flashlight under his face as he told us how the ghost would chop off heads and try them on to see if they fit.

I knew that dad made the story up, and that there wasn’t really a ghost. He even finished up classic line, “and to this day, the ghost wanders around, looking for his head.” Then he did his best scary face and said in a creepy voice, “Goodnight, pleasant dreams.” And then he turned off the flashlight and went inside. My sister and I were scrunched way down in our sleeping bags, giggling and being silly.

After a few minutes though, my sister was asleep. There I was in the tent, alone and wide-awake. I don’t know how long I lay there before I realized that something was outside the tent. At first, I thought that I was just hearing the wind, or a cat, but then I heard a definite thump, like something hitting the ground. I didn’t move at first. I just froze and listened. Every few seconds I would hear the thump, and it was getting closer to the tent. I tried to wake my sister up, but she was sound asleep. I pushed on her and pushed, but she just kept sleeping. I was really scared by now, and starting to cry. I knew that if I was too loud, then whatever was outside the tent would hear me. I lay there in that dark tent, perfectly still. My muscles were aching from trying not to move or even breathe.

After what seemed like forever, I turned my head slowly and looked at the shadowy shapes on the side of the tent. Then, one of the shadows moved. Not like a dog or cat, but like someone who was squatting down low, trying to be hidden.

I took a deep breath and let out a scream that I didn’t expect. I screamed and screamed and screamed. My sister woke up, screaming at the top of her lungs. There we were, two scared little girls, screaming as loud as we could. Me screaming because there was something outside the tent moving, and my sister screaming because there was someone inside the tent screaming.

My mom came running out the door with a flashlight, and she was screaming loudest of all. She shined her flashlight on the moving shadow, just in time to catch my dad, creeping towards us with a Halloween mask on.

Needless to say, nobody thought that it was very funny, least of all my mother. She hauled us inside and put my sister and I in our own beds. Mom and dad had an awful fight. Mom yelled at dad, called him “stupid and cruel,” said that she couldn’t believe that he would do something like that.

3 Dad yelled back, told her that she was overprotective and didn’t have a sense of humor. He said that just because his grown-up wife was afraid of the dark that his daughters didn’t have to be.

I heard my mother slap my father. I actually heard the sound of her hand striking his face, hard. Silence followed. Then I saw him move past my door; go down the hall and outside. I thought that he was going out to get the tent or our stuff we left out there. Instead, he got into his car and tore out of the driveway.

Mom was in tears and my sister was crying over on her side of the room. I knew that mom and dad had argued before, but I never heard a fight as bad as this.

Dad didn’t come home that night. I found out later that he spent the night in his car in a parking lot. He walked into the house as we were sitting down to a very quiet breakfast. He looked terrible. His face was all dirty and his eyes were red. Like he had been crying.

He came into the kitchen, got down on his knees, scooped my sister and me into his arms and kept saying “I’m sorry, I’m so sorry,” over and over. My mom came around the table and put her arms around all of us and we all cried together. My dad promised never to scare us again, and he never did.

And none of us ever talked about that night until now.

But I’ve always been afraid of the dark since that night.

As a teenager, I began to have strange dreams. Sometimes I would dream that I had an axe, and that I was wandering around looking for a victim. In other dreams, I would be running from a figure that was chasing me, and I would trip over something, look down and see my own head on the ground. That dream would wake me up, shaking, and I could never get back to sleep after that one.

The dreams tapered off in college, and I soon forgot all about them. Then, I met Peter. We were married right out of college. He was so good to me at first, but he had a temper that I began to fear. That fear must have tapped something in my memories – maybe it was the way Peter would laugh after playing one of his cruel jokes on me; I don’t know.

But, I do know that the dreams started again. Some nights I would take a couple of sleeping pills just to get back to sleep after a nightmare. Then, two weeks ago, on Halloween, Peter decided to play one of his... his little jokes on me. First, he took me to the movies and made me watch one of those horrible stories about a deranged killer with a knife who was chasing teenagers.

4 Every time I would turn my face away from the screen, he would put his hand on the back of my neck, and force me to look. He leaned over and whispered, “Come on, don’t be such a chicken. It’s only a movie.”

That night, I couldn’t sleep; actually, I was afraid to close my eyes. I knew the nightmares would come, and I was so scared. Peter was getting angrier with me for not turning off my bedside lamp, and I was on the edge of tears. Desperate, I took four sleeping pills and tried to go to sleep, but not to dream.

It didn’t work. I remember the dream so vividly. I remember dreaming that I was in the house, in bed, but that there was something in the room with me. I remember getting out of bed to turn on a light, but the lights wouldn’t work. The only light was coming from the strange glow around the window. I felt my way along the wall in the dark, and my foot kicked something on the floor.

I knew what I would see if I looked down! I knew I’d see my head with an axe on the floor next to it!! I forced myself from somewhere inside my conscious mind to say, “This is just a dream.” But I couldn’t stop myself from looking down. Slowly, I looked at what I had kicked in my dream, and then I froze. On the floor was an axe, but it was Peter’s head next to it! I stepped back, and the eyes opened and Peter’s mouth moved. That head on the floor said, “Come on, it’s only a dream.” I screamed and picked up the axe and began hitting the head, harder and harder. It kept changing from Peter’s face to a Halloween mask and back to Peter.

Finally, I woke up. I woke up to find myself standing over my bed, holding a hammer, covered in blood. Peter was laying there, dead. I screamed and screamed and screamed, and finally, the police came. My nightmares have come true.

(Loud sobbing that slowly turns into laughter.)

How was that? Do you think the jury will buy that story? That’s right, the poor, little girl who was traumatized as a child can’t be blamed for turning into the poor adult who killed her no-good husband.

The jury will eat it up.

5
```
