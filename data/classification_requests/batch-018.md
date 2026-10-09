# Classification request: batch 18 of 53 (40 records, IC-1081 to IC-1120)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-018-reply.json`.

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

## IC-1081: JERRY: A WIZARD SCHOOL DROPOUT

- Title: JERRY: A WIZARD SCHOOL DROPOUT
- Author (byline): Brandon Daley
- Work: JERRY: A WIZARD SCHOOL DROPOUT
- Publisher: Mushroom Cloud Press
- Publication date as stated: 2010
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2497
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
Narrator: Magic! If you think kids are born with this ability—the ability to levitate objects, the ability to make enemies into frogs, the ability to turn water into wine—then you are wrong…This kind of magic takes years of dedication; years of preparation! And just like regular humans, potential witches and wizards receive this preparation from school, but not some ordinary school that dabbles in math and science. Instead, this school dabbles in potions and curses. Wizard High! The most secretive high school in the entire world located in one of the most secretive locations in the entire world—in Utah somewhere. But even though this school and most high schools have their differences, for the most part the two are pretty much the same. They both have rigorous courses and intelligent teachers and strict policies. And—needless to say—they both have burnouts. That’s what this story is about: a wizard school burnout named Jerry. Jerry: Sup. Narrator: Even at the young age of 6, onlookers could notice Jerry’s lack of enthusiasm in wizardry. First-Grade Teacher: Class, today we are going to discuss want we want to be when we grow up. Ringleworm the Brave? What do you want to be when you grow up? Ringleworm: I want to be a wizard! First-Grade Teacher: Very good, Ringleworm! How about you, Olfos the Giant? Olfos: I want to be a wizard! First-Grade Teacher: Interesting, Olfos! And what about Jerry…what would you like to be Jerry? Jerry: I would like to be a dermatologist. First-Grade Teacher: Jerry, don’t you mean a wizard? Jerry: No, I’m pretty sure I want to be a dermatologist. First-Grade Teacher: I think wizard is a more realistic goal for you, Jerry. Jerry: But… First-Grade Teacher: Wizard! Narrator: Aside from his idealism, Jerry also had a keen sense of humor for his age. (Shows first-grade teacher holding a coffee cup while addressing her class). First-Grade Teacher: Okay, class. It’s time for recess. Everyone line up at the door except for Jerry—who chose to lose his recess privileges when, instead of picking up the toys as asked, he turned my coffee into monkey vomit. (Takes a sip of the coffee). First-Grade Teacher: Yep. Definitely monkey vomit. Narrator: By middle school, most kids grew out of their immaturity. However, Jerry seemed stagnant.

(Middle-school teacher addresses class). Middle-school teacher: Now if everyone has turned in their permission slips, we can hop on the bus and head off to visit the unnatural history museum. That is, everyone except for Jerry, who lost his field trip privileges when he turned all of the cafeteria milk…into monkey vomit. Jerry: What! How’d you know it was me? Middle-school teacher: You wrote about the incident in your term paper. Remember? You called it “How I turned the Cafeteria Milk into Monkey Vomit.” Jerry: Oh, yeah! Blame everything on Jerry! Narrator: By the time he hit high school, the only trait that had really changed in our young dermatologist was his newfound dirt stache. Other than that, he was still the same old miscreant—and he certainly was no wizard! (High school gym teacher lectures a class). Gym Teacher: Okay, you sons of witches! I’d usually tell you to hit the showers after such heavy levitating as we did today, but it ends up that one of you seems to have turned the water in the warlocker rooms…into monkey vomit. Now I don’t know which one of you little heathens pulled of this stunt— Jerry: Thank god… Gym Teacher: But because Jerry has been doing this everyday for the last 11 years, I can only assume it was him—for which you will be punished Jerry. Jerry: What do you expect? I don’t feel like getting naked in front of a bunch of other dudes, dude. Narrator: In fact, despite the thousands of rubies the wizard public was paying for kids like him to attend school, the only real spell Jerry knew was how to turn liquids into monkey vomit. And yet, he continuously passed all of his classes. With straight D’s, he’d graduate into the next grade—mainly because of the ridiculous “No Wizard Left Behind” policies enlisted by the government. It was only so long before a dreadful student like Jerry completely derailed the tracks of success altogether. Today, was that day. (Jerry is in his spelling class. His teacher, Mrs. Crumblelumps, is lecturing). Mrs. Crumblelumps: Okay, everyone. Today in spelling class we are going to go over the pronunciation of spells that will turn your enemies to stone. Now I expect you all to repeat these after me…Rigor Mortis! Class: Rigor Mortis! Mrs. Crumblelumps: Jerry, I didn’t hear you cast that spell. Would you like to join us or wait in the hallway while we finish? Jerry: Listen, Mrs. Crumblelumps. If I find a spell to have some sort of usefulness in the real world, than I will do my best to learn that spell. However, I’m just not seeing any sort of purpose for a curse that turns enemies into stone. If I have an issue with somebody, I’d rather just talk it out with him instead of, you know, rendering his body into a rock…

Mrs. Crumblelumps: Well, Jerry, you can sit in the hallway until you realize violence is the way to solve
problems, not words.
Jerry: What if I never realize that?
Mrs. Crumblelumps: Then, I will have to fail you. And you’re going to have trouble getting into Wizard
College with an F on your transcripture.
Jerry: Like I’m going to go to Wizard College anyway.
Mrs. Crumblelumps: Well, then get a dead-end job before the army against the dark powers drafts you.
Either way, you don’t need to be wasting my or your peer’s time.
(Jerry picks up his things and goes into the hall. He sits down and mumbles to himself.)
Narrator: Yes, there’s no place for an idealistic dermatologist in the wizard public school system…
(A boy, Wigburg, approaches Jerry).
Narrator: And although Mrs. Crumblelumps may have thought she was doing something good, the way luck
may have it she was actually sending Jerry down a dark, corrupted path, that not to many wizards venture
back from. A path that even the ability to turn people to stone will do absolutely nothing.
Wigburg: Hey there, Jerry.
Jerry: Sup, Wigburg the Destroyer.
Wigburg: What are you doing out here in the halls?
Jerry: I got thrown out of spelling class for speaking my beliefs.
Wigburg: Well, if you want to join, me and a few a bros are going to go drive around, maybe do a little
black magic.
Jerry: Black magic?
Wigburg: Yeah, I mean, unless you aren’t, like, cool with that type of thing.
Jerry: No, no I’m cool. It’s just that…I’ve never done black magic before…
Wigburg: We’re not doing nothing to hard…not doing nothing that’s bad for you at least.
Jerry: Okay, I guess it wouldn’t hurt.
Wigburg: No, it wouldn’t man. In fact, it’ll help. You know. Expand your mind and stuff.
Jerry: Yeah, I’ll do it. Let’s go.
Wigburg: All right, man. That’s the Jerry I know.

Narrator: So Jerry followed Wigburg out to Wigburg’s custom van. The van looked old, worn-down and
purple, with a giant accountant airbrushed on the side door—because just like nerds get wizards airbrushed
on their custom vans, wizards get accountants.
(Jerry gets in the van’s side door while Wigburg gets in the driver’s. There are two other people,
Fungletoad and Artimous, in the van).
Wigburg: Jerry, this is Artimous the Forgetful and Fungletoad the Confused. Gentlemen…this is Jerry.
Artimous: Jerry! I didn’t know you black magic-ed! I thought you were a square or something.
Fungletoad: Squares have four sides.
(Everyone looks confused at Fungletoad’s stupidity).
Wigburg: This is Jerry’s first time, boys.
Jerry: What happens if we get caught?
Wigburg: Naked decapitation on a cold day.
Jerry: Wait, what—
Wigburg: You got the spells, Artimous.
Artimous: Yeah, dude. I got this list from my cousin.
Wigburg: The one from California?
Artimous: Yeah, dude. These spells are California good, man.
Fungletoad: My dad is from Washington.
Jerry: Listen, I don’t know if I want to risk getting decapitated in the nude on a cold day just because of a
little black magic.
Wigburg: Dude, Jerry. You’d be surprised how many people black magic. Probably like eighty-percent of
the school.
Artimous: And there’s not even any proven side effects. It really shouldn’t be illegal. I mean, it’s like,
whatever, you know?
Fungletoad: I sleep in my socks because sometimes my feet get cold.
Artimous: Put on some music, Wigburg. Some music we can black magic to.
Wigburg: Okay. I’ve got Bob Merlin, the Voodoobie Brothers, Fantasy C.R., the Dumble-Doors
and…Phish.
Artimous: Whatever works.

Narrator: Yes, whatever does work when you do enough black magic. Jerry started out pretty lightly, once every few weeks—weekends only. But, by the beginning of his senior year at Wizard High, Jerry was a regular magic-head. He always had spells on him: at school, at home. He even went as far to start selling spells for a little bit, before his parents caught him; when he came home smelling like magic one night. Jerry’s Mom: Jerry…you’re father and I are worrying. Lately, you’ve been out late and have slipping grades. Jerry’s Dad: And your friends don’t even ring the doorbell when they come to get you. They just sit outside and rev the engine in that ridiculous accountant van. Jerry’s Mom: We’re worried you’ve been getting into…black magic. (Jerry is obviously under the influence of black magic). Jerry: Oh… Jerry’s Mom: I found this list of spells in your pocket when I was washing the laundry. I casted one on your father to see what it did, and he just spent the next hour and a half watching the Backyardigans, giggling. Jerry’s Dad: I ate three bags of Doritos that day. Three! Jerry: Sorry Dad. Won’t happen again. Narrator: But it happened again. Even though Jerry had loving parents who pushed him to quit—he had lost his personality to the magic, and his grades finally plummeted from D’s to F’s. So, before second semester of his senior year, Jerry decided to dropout. The magic had destroyed him. He no longer dreamed of becoming a dermatologist. Instead, he wanted to start a band, even though he had no past in music. Eventually, Jerry’s mom and dad kicked him out. Lost, homeless, a heavy black magic addiction: none of these were good things. So Jerry decided to get a job…at the Wizard elementary school as a bus driver. (Jerry is driving a school bus. Jerry takes a drink of his soda and then spits it out). Jerry: Damnit! Who keeps turning my Pepsi into Diet Pepsi! I swear when I find out who it is… (There is yelling from the back of the bus. Jerry looks in the mirror to see what’s going on). Jerry: Hey! Knock it off back there! Quit sacrificing that first-grader! Obnoxious kid: You can’t tell me who I can and can’t sacrifice! You’re not my dad! My dad is dead! A 3000- year-old sorcerer killed him! Jerry: That’s not true! I’m only 2000-years old. (Silence as the kid is puzzled by Jerry’s comment). Jerry: That’s a joke…like I was saying that I was the one who killed…your…never mind. Obnoxious kid: Hey, aren’t you friends with my brother? Jerry: No, I’m not to good of friends with Satan.

(Silence)
Jerry: You aren’t to keen with that sense of humor, are you?
(Silence)
Jerry: Who’s your brother?
Obnoxious Kid: Wigburg the Destroyer.
Jerry: Oh, you’re a Destroyer? Yeah, I know him. What’s he doing now?
Obnoxious Kid: He’s interning for a big wizard politician.
Jerry: Wigburg is?
Obnoxious Kid: Yeah. He says it won’t be too long before he has an office of his own.
Jerry: Really? God, I wonder if Artimous and Fungletoad are doing that good too.
Obnoxious Kid: Artimous is assistant-managing some restaurant, but Fungletoad is still a complete failure.
Jerry: Thank God. What’s he doing? Serial killing?
Obnoxious Kid: Maybe as a hobby, but his job is as a dermatologist.
Narrator: Nothing makes you realize how real the scenario you are in is like a heavy blow to the heart. And
even though Jerry had a steady paying job and was back to only doing black magic on the weekends, he only
could see the bad in his situation. He believed his life was useless, ambitionless, worthless. But believing
doesn’t necessarily make things true, now does it?
(Jerry is driving the bus. There is a lot of ruckus coming from the back.)
Group of kids: The wheels on the bus go round and round…round and round…round and—
Jerry: SHUT UP! Everyone just SHUT UP or I’m driving this bus off a cliff!
(Silence until one person in the group breaks by finishing the song.)
Kid: …round.
Jerry: That’s it! I’ve had it with you little pieces of dragon dung! No one gets to talk anymore or I’m not
taking you guys home.
Obnoxious kid: You can do anything to us! My brother told me you don’t know any spells! That you’re just
a wizard school dropout!
Jerry: Be quiet!
Obnoxious kid: In fact, I bet I know more spells than you do…

Jerry: Listen, kid. I don’t need this harassment!
Obnoxious kid: I bet he doesn’t even know how to reverse a stone spell.
Jerry: Of course I do!
Obnoxious kid: Well, we’ll see about that…Rigor Mortis!
(Jerry is suddenly turned into stone. The group of kids laughs at him, not realizing he can’t control the bus).
Narrator: Now, unfortunately for Jerry, he actually did not know how to reverse the spell. Eventually, one
of the kids did for him, however this was only after the bus careened over the side of a bridge into a rapidly
flowing river.
(The bus flies over the edge of a bridge into a river. The kids all scream loudly)
Kid: Someone reverse it before we drown!
Obnoxious kid: Sitrom Rogir!
(Jerry turns back from stone).
Jerry: Oh God! Look what you’ve done!
Kid: How are we going to get out?
Narrator: Now, even though Jerry’s brain had been fried from the years of black magic, he was still quick on
his feet with his idealism.
Jerry: Quick! Give me your wand!
(Obnoxious kid throws Jerry a wand.)
Jerry: Ad astra per aspera!
Narrator: And just with the simple flick of a wand, Jerry turned that entire river…into monkey vomit.
Obnoxious Kid: Ew! Gross…
Narrator: Because of the gallons of monkey vomit surrounding the stranded bus, the river gracefully came to
a halt—cause everyone knows monkey vomit is one of the thickest vomits a person can find. The police
arrived and helped levitate everyone out of the back of the bus and Jerry finally felt like he had done
something important.
(Police officer approaches Jerry).
Police officer: Congrats, Jerry. You’re a hero. I mean, that is, if you exclude the fact you drove a bus full of
children into a river.
Jerry: Is everyone okay?

Police officer: Everyone except this little guy, who drowned in the monkey vomit. (Police picks up the carcass of Obnoxious Kid). Jerry: Well, that’s okay. He was kind of a jerk anyway. Police officer: So when do you think you can reverse this whole “river full of monkey vomit” thing. Jerry: Uh…reverse it? Police Officer: Ha! That’s funny. Pretending like you don’t know how to reverse it…we’ll have you do that once we pull the bus out and get it hosed off and back to the school. But thanks again for your help, Jerry. The world needs more people like you in this world. Narrator: So Jerry, the wizard school dropout, no longer drove the bus angrily and hate-filled. Now Jerry drove that vomit-reeking automobile with the realization that he put his thumbprint on the world. You can take this story two ways. One: that everyone on this earth was put here for a reason; or two: that monkey vomit can come in handy every once in a while.
```

---

## IC-1082: mary Choppins

- Title: mary Choppins
- Author (byline): FRANK JOSEPH
- Work: mary Choppins
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1875
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
Doctor: Alright kids, there’s something I need

to tell you. Now Susie…Robert…this is

very hard, probably the hardest part of

being a doctor, so I’m going to break

the news to you in what I view as the

easiest way possible. Raise your hand

if your mom is alive…
(Susie and Robert raise hands)
Doctor: No no no…put your hands down.
Susie: Mum?!
Robert: Noooooooooooo!!
Docotor: Jeez, calm down. Seriously.
Susie: The doctor’s right Robert, at least

we’ve still got our daddy. Doctor: Actually he’s being held as the prime

suspect in your mother murder case. Robert: Murder?!? Susie: You told us it was a car accident! Robert: You lied to us! Doctor: Not necessarily, because we DID find

the body in a car…chopped up into

thousands of little pieces, but still, in a

car. I could show you if you’d like? Susie: No! what are we going to do without

any parents? Robert: Anarchy!! Doctor: No, no, none of that. You kids will just

have to find your selves a nanny.

Susie: Wouldn’t it be a lot safer to put us in an

orphanage or a foster home instead of

letting us fend for ourselves and

forcing us to find our own nanny? Doctor: Hey! Raise your hand if you’re the

doctor here. Yeah, that’s right. Now

you kids get out of here and uhh, good

luck. (Susie and Robert’s house) Susie: Well we’ve got the whole house to

ourselves. What should we do Robert?
Robert: Kick the dog!
Susie: No
Robert: Throw a wild kegger?
Susie: Robert, we’re 8 years old
Robert: Pee in the shower!
Susie: No! Robert, we need to find our new

nanny quickly. I say we put out a flyer

for a new nanny. That way we have

people to choose from. Robert: Fine, but I’m still peeing in the shower Susie: Ok you can do that later. But now let’s

write this flyer! What should the first

requirement for our nanny be? Robert: She needs to be a girl! Susie: Ok. And she needs to be smart Robert: And she needs to let me pee in the

shower! Susie: Ummm…she needs to be nice, and

clean, and caring Robert: Did you write the part about the

shower?! Susie: No Robert! Ok, I think we’ve got

enough here. Lets send this flyer out

and hopefully we’ll have nannies lined

up down the street tomorrow! (The next day) Susie: Ok, tell us why you should be our new

nanny. Nanny #1: Well, I love children so much! I could

just eat them up….with frosting….and

cream filling…and a cherry on

top…and chocolate…. Robert: Next nanny please Susie: Umm, the first requirement on our

nanny list was that she needed to be

a…she.
Nanny #2: Yeah, so.
Robert: Uh, you have a boy’s name
Nanny #2: Hey! Ever heard of a woman having a

man’s name? Like Alex, or Erin or

something? Susie: Your name’s Bruno Nanny #2: Yeah, short for uhh…Bruno..ella.

(scratches self) Robert: Next nanny please Susie: We’ve gone through 40 nannies and so

far the most qualified was Bruno Robert: Brunoella.

Susie: There’s only one more nanny left. This

is hopeless. Hand me her application Robert: Here you go Susie: Gasp! Robert did you read the name

on this application?? Robert: Is it another lady with boy’s name?

Because that last one looked at me

funny. Susie: No, it’s Mary Poppins!! Robert: No way!! Mary Poppins? I saw her in

that movie! What was it called? Susie: The name’s not important. All that

matters is that we’re going to have a

magical singing flying nanny! Robert: Oh goody! Susie: Bring her in Robert! Robert: Welcome Mary Poppins!! Mary Choppins: Poppins? It’s Mary Choppins! Robert: But I thought the application said

Poppins Mary Choppins: Well thinking never got anyone

anywhere now did it?! Robert: Well if you think about it, without

thinking, our world would not- (Choppins puts cigarette out in Robert’s eye) Robert: Ohh, my eye. I need that for seeing! Susie: That wasn’t very nice Mary Poppins Mary Choppins: Did you not hear me just rant about

this? It’s Choppins!! When people mix

me and that other nanny up, it really

pisses me off. There must’ve been a

smudge on the application or

something. Either way, fact of the

matter is, I’m your new nanny. Susie: All I have to do is throw your

application in the trash with the others

and then you won’t be our nanny Mary Choppins: Oh no you will not! Now, where am I

staying?
Susie: Robert,
Robert: My eye still burns!
Susie: Show Miss Choppins up to her room
Robert: How can I show her to her room when I

can’t see?!? Mary Choppins: Oh suck it up! Eyes are overrated.

Take my bag Robert: This bag is so heavy Mary Choppins,

what do you keep in it? Susie: Oh, Robert, do you remember Mary

Poppins had a bag that she could pull

very large things out of. Like lamps

and such. Maybe hers is the same! Mary Choppins: Why in fact, it is! (Pulls out shotgun, then sword, then sock full of batteries) Robert: What’s that Mary Choppins? Mary Choppins: It’s a sock full of batteries…leaves the

most interesting bruises. Now you kids

get some sleep. Tomorrow should be

an interesting day!

Susie: Robert. I can’t sleep Robert: Neither can I. Mary Choppins in the

next room practicing her bare knuckle

boxing on a giant slab of meat is very

loud and distracting. Susie: That’s not what I meant. Wait, where

did she get a giant slab of meat? Robert: She pulled it out of her bag. Susie: Oh..anyway, I meant I can’t sleep with

the thought that we’re going to be

living with that lady for the rest of our

lives. Robert: I know, she won’t even let me pee in

the shower! Maybe she’ll get better.

We just need to give her some time. Susie: Yeah, lets just be more cheery about

things, and maybe she’ll be happier.

It’s worth a shot. (The next day) Mary Choppins: And where do you think you’re going

Robert?! Robert: Today is the day the doctor said I

could come get my polio cure…. for

my polio. Mary Choppins: You’re not going anywhere Robert: But I’ve been waiting for this day my

entire life.
Mary Choppins: Polio Schmolio!
(puts cigarette out on Robert’s shoulder)
Robert: Ohhh, my shoulder! I need that for

carrying backpacks on! Susie: Please Mary Choppins. Let him cure

his polio Mary Choppins: Screw cures. We need to beat the

polio! You’re never gonna beat the

polio walking around on that thing! Robert: My crutch! I need that for walking! Susie: Remember Robert, be cheery! Robert: Cheery. Cheery. You’re right Mary

Choppins. I can beat the

polio..through song and dance! Mary Choppins: Oh boy Robert: Polio Schmolio, I can still dance! Polio

Schmolio, just give me a chance! I can

make it if I try, just please stop burning

me in the eye Mary Choppins Uggggh. Robert: Polio Schmolio, but I’m still alive! Polio

Shmolio, I can still jive! (dances) (Choppins puts cigarette out in Robert’s other eye) Robert: Oh, my other eye. I needed that for

seeing! Didn’t you hear the part of my

song where I said stop burning me in

the eye? Mary Choppins: I already told you, eyes are overrated! Robert: But I was in the middle of a dance

routine! Mum…. is that you? Mary Choppins: Your mum is dead! That’s why I’m

here. Now, we’re going downtown.

Nanny has some…errands to run. Grab

your coats Susie:

Mary Choppins (Downtown) Robert:

Mary Choppins: (steps on bird) Susie:

Mary Choppins:
(Flashback to Vietnam)
Mary Choppins:
(End of Flashback)
Mary Choppins:
Bert:
Mary Choppins:
Susie:

Robert:

Bert:
But Mary Choppins, it’s almost 90
degrees outside
I said get your coats!

Now that the scabs on my eyes have peeled back, i can finally see! Look at the birds Susie! Mary Choppins, can I feed the birds? I hate birds!

Is there anything you do love Mary Choppins? Let me think? Well..back in Nam..

Ah Vietnam… I hate it here.

No..there’s really not. Mary Choppins, there you are. Bert! Good to see you again. Robert, remember in Mary Poppins, she had that friend named Bert that took the kids into the magical painting where they rode merry-go-rounds and ate scrumptious treats? Goody! Excuse me Bert, are you going to take us to a magical land full of scrumptious treats? Uhh, I think I can get you to a “magical Mary Choppins: Robert:

Susie:

Robert: Bert:

Robert: Bert: Mary Choppins:

Bert:

Mary Choppins:

Bert: Mary Choppins:

Robert: Bert:

Mary Choppins:
land,” but it’ll cost you
Bert, there 8 years old.
But Mary Choppins, I want to go to a
magical land so badly!
Robert I think that man was trying to
sell us LSD.
What’s LSD?
It stands for Lolipops Stickers
and…Dogs. Puppies, do you like
puppies?
I love puppies!
Then you’d love LSD!
Bert, not here. Now, you wanted to talk
to me in private?
Yeah, so uhh, I take it you got the job
done?
Of course I got the job done, why do
you think I’m stuck with these
buggers? I’ll get them too pretty soon.
You got my money
Not yet, but I will soon.
Well hurry, killing’s an expensive
business!
Gasp! Did you hear that Susie?
Jeez, Mary Choppins, bring your voice
down
Sorry, after smoking for 47 years of my
life I’ve lost all volume control of my
voice.

Susie:

Robert: Susie:

Mary Choppins: (Home) Mary Choppins:

Susie:

Robert:

Susie:

Robert: Susie:

(Breaks down door) Cop:

Robert:
Susie:
Cop:
(Breaks down door)

Oh my god! Mary Choppins is a
nanny…slash hitwoman! She killed our
mum!
Who saw this coming?
We have to play it like we don’t know
though. We’ll get her.
Alright kids, lets run along home.

Ok, you kids do something not fun, I’m gonna go soak my feet. Ugggh. Now’s our chance Robert, make the call! Hello? Yes! We live at 314 Riverside Avenue. 20 minutes? Ok, let me ask. Susie, do you want olives, or mushrooms on your pizza? Robert, you’re supposed to be calling the police!! Oh, sorry. Give me the phone! Hello? Yes, our nanny killed our mum and she’s going to kill us.

Where’s this crazy nanny? I’m takin
her out!
That was quick.
She’s upstairs, soaking her feet
Eww
Cop:
Mary Choppins:
Cop:

Mary Choppins: Mary Choppins? Time for you to die! Hey, we live in England, remember? Oh, of course. How silly of me to forget. (changes accent and swing billy club around) Right-o then. What seems to be the problem here? Too bad for you I never soak my feet without a weapon nearby (Choppins shoots with shotgun) Cop:

Mary Choppins:

Dad: My god I’ve been shot. You’d think they’d give us more then a billy club to protect ourselves. Oh well. So I see you kids are on to my plan. I guess I’ll just have to eliminate you then. I don't think so (Shoots Marry Choppins in head) Kids: Dad:

Susie: Dad: Susie: Robert: Daddy! Yes kids it’s me. After they found out I wasn’t guilty they released me and I came here. It turns out your mother was a wittness to an illegal drug deal which would've gotten Bert put away for life, so he hired Mary Choppins to kill her. Now, give me a hug Susie! Oh daddy, I’ve missed you so Where’s Robert I don’t know…Robert? Where are you? Peeing in the shower! Victory at last!!
```

---

## IC-1083: Moonraker Madness

- Title: Moonraker Madness
- Author (byline): Marissa Molchansky
- Work: Moonraker Madness
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1419
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
Moonraker: (writing in her diary) And that was the first time I ever saw a
tapeworm. (sees audience) Oh! Hey everybody, this is my diary! Diary, everybody,
everybody, diary
Diary: Hello.
Moonraker: Yeah, that’s right. My diary talks. But more importantly, it’s covered in
butterflies and honey badgers‐‐my two favorite animals. Hey diary, want to tell
them what I did today?
Diary: I suppose I shall. When I woke up this morning my stomach felt like the ocean
during a hurricane, so I sat on the toilet for the first three hou‐
Moonraker: Skip ahead please.
Diary: I’m never eating tacos again it’s been fifteen‐
Moonraker: A little bit past that…
Diary: Dear diary, today I kissed Jake
Moonraker: There we go, thank you. Was that so hard?
Diary: No, I‐‐
Moonraker: Okay now shut up diary; I wanna tell this story
Diary: Oh no. But I find this so interesting I just… (falls asleep)
Moonraker: So I walk into school lookin’ all hot and stuff and, of course, Vicci has to
talk smack
Vicci: Ew. Why is there a bug on your face?
Moonraker: That’s not a bug; it’s Cristoff, and he’s better at watching Star Trek than
you.
Vicci: Whatever. I hear you’ve never even kissed a guy
Moonraker: Not true! I kiss my diary all the time (kisses diary)
Vicci: That doesn’t count
Moonraker: It counts more than that inmate you keep sending letters to!
Vicci: Shut up he’s really sensitive!

Stevie: Hey girls!
Vicci: Ew.
Moonraker: Hi Stevie
Stevie: You look so beautiful today Moonraker!
Vicci: If by beautiful you mean toilet‐y, then yes. She does look like a toilet.
Stevie: Not really…
Moonraker: Aw, thanks Stevie!
Vicci: Whatever. You both look like toilets.
Moonraker: And that’s when I saw him…standing there like a bronze statue. Or a
gold statue? Isn’t gold better than bronze? But wait isn’t platinum also better than
gold? Let me think, how many albums has Nickelback sold…hm…Oh hey
Jake…wanna see my appendectomy scar?
Jake: Uh…what?
Moonraker: That’s cool, I was just joking. Just joshing. JUST JAKING (laughs). So I
was just thinking, you know…We should like kiss, or whatever, right? (laughs) I
mean wouldn’t that be hilarious!
Jake: Not as hilarious as Happy Gilmore. OH YEAH!
Moonraker: Totally. How about we leave it up to fate then, shall we? How about…oh,
I don’t know. I ask this diary that just happens to be here in my hands! So weird.
Diary, should Jake kiss me?
Diary: (reading) Jake should totally kiss you. If he doesn’t kiss me—
Moonraker: Me.
Diary: He will get chicken pox and die.
Moonraker: Oh darn guess you have to kiss me now. Cruel world. (puckers up)
Jake: (to his friends) Hey guys, let’s go throw rocks at that homeless shelter!

Moonraker: Alright, that’s cool. Have fun Jake! Bye!
Diary: You’re taking too long to tell the story
Moonraker: I am taking the perfect amount of time to tell the story
Diary: Oscar Wilde once brilliantly quipped, “—
Moonraker: Oh my god, stop. No stupid quotes from The Beatles. I’ll tell it faster. (to
the audience) So the next day I go into school, looking hotter than ever…Oh. Hey
Vicci.
Vicci: Oh. Hey Moonraker. Didn’t see you there behind all that ugly.
Moonraker: Oh. Hey Vicci. Didn’t see you behind all that…locker, because you are
very in shape and it was open so it was hard to see you.
Vicci: Do you even go to this school anymore? I heard you got kicked out for dealing
drugs and being ugly
Moonraker: No! I…not all that stuff, not true! Not funny!
Vicci: Wait, are you wearing lipstick?
Moonraker: Why, you jealous?
Vicci: Moonraker, it’s supposed to go on your lips
Moonraker: Dammit! I always get lipstick confused with blush.
Vicci: Why are you all dressed up anyway? Is there an Amish funeral today?
Moonraker: There probably is because of their limited access to modern medicine,
but I am dressed like a sexy woman‐thing because I am totally going to kiss Jake
today.
Vicci: HA. That is a joke. And it was funny. Jake wouldn’t kiss you if you were his
lucky rabbit foot. He wouldn’t kiss you if unicorns existed and pigs flew over the
moon.
Moonraker: You can talk all the smack you want about me, but you NEVER. EVER!
Say that unicorns don’t exist.
Stevie: Hey ladies! Looking quite beautiful today
Vicci: Oh. Hi Stevie.
Stevie: Moonraker, what is that intoxicating perfume you’re wearing?
Moonraker: Old Spice. Do you like it?

Stevie: Its scent, although lovely, pales in comparison to the beauty of the face on
which it was mistakenly applied.
Moonraker: That’s precisely what I was going for. Jake doesn’t stand a chance
Stevie: Oh…Jake? You did this for Jake? Good luck.
Moonraker: Thanks. As if I need it, I’m hot.
Vicci: Whatever
Moonraker: Whatever
Vicci: Whatever. Go away
Moonraker: I’m going (walks over to Jake) Hey Jake, wanna hear a joke?
Jake: You know I would love to, but I would actually hate that.
Moonraker: That’s okay I’ll just take my shirt off. What?!Who said that? Jake you’re
gross. I love you. Wanna meet me by the lake tonight? It’ll be moonlit and beautiful,
you know…if you’re into that.
Jake: Hmmm…meet you by the lake…that gives me some ideas…
Moonraker: Alright, I don’t know why you’re pondering so ominously over there but
I’ll see you then!
Diary: How many times must I warn you, he’s not going to kiss you.
Moonraker: Shut up diary, you’re stupid. He just said he’s meeting me by the lake
tonight; do you even have ears?
Diary: No.
Moonraker: Oh. I guess that makes sense.
Diary: You should just look out. That’s all I’m saying
Moonraker: I will look out. From the dock as Jake holds me close and I listen to his
heart beat and dolphins fly and the moon screams the lyrics to Aerosmith’s “I don’t
wanna miss a thing”.
Diary: I don’t think you know how lakes work
Moonraker: You don’t know how you work. Just shut up and let me get ready. (Puts
on makeup) Let’s do this! (transition)

Moonraker: This lake is so beautiful I want to write a song about it. Done. Lake, lake lake. Ohhhh you’re a lake. Lake, lake lake… Jake: Hey Moonraker, lookin’ hot. Moonraker: Oh, thanks Jake; it’s nothing I just woke up it’s hot outside my grandpa died. Look at you! All…in sweatpants. What a bold choice! Jake: Yeah. I got these at Costco. Five bucks. Bargain shopped like it’s my job. Moonraker: Wow. You’re so economical. Jake: Now that we’re alone, how about we get our mac on? Moonraker: If that is a colloquialism for kiss then YES! Vicci: Hey Moonraker, kiss this! (she throws a water balloon at Moonraker) Jake: (laughs) Water balloon to the face. Classic. You didn’t actually think I would kiss you, did you? Who would be that gross? Stevie: I would! Vicci: Gross. Moonraker: Stevie! What are you doing here?! Stevie: Look, Moonraker, I came down here because I knew these people were up to no good. Moonraker: (crying hysterically) Why do you even care? I’m ugly and I smell and I may have ran over a guy and not told anyone and left him for dead in Utah. Stevie: Because you’re beautiful to me! Sure, there are people out there who are insecure to the point that they feel the need to constantly ruin other people’s lives to feel better about their own Vicci: Hey! Yeah, it’s true. Stevie: But there are also the people who genuinely love you and care for you no matter what. Also, your name is Moonraker, which is a reference to my favorite James Bond movie of all time, and I find that really hot Moonraker: What are you saying?? Stevie: What I’m saying is…I love you, Moonraker! Vicci: Ew Moonraker: Stevie, that’s the nicest thing anyone’s ever said to me! But…hm…I’m feeling quite drawn to Jake… Jake: Hot (Moonraker kisses Jake. As she does so she pushes him in the lake) Vicci: Oh my god you pushed Jake in the water! Gross it’s so dirty! (Moonraker pushes Vicci in the lake) Moonraker: That kiss made quite a splash (transition) Moonraker: (writing in diary) Dear diary Diary: (Being written on) Ow, ow! Moonraker: Dating Stevie has been the best time of my life. He always makes me smile and he doesn’t watch Jersey Shore. His bad skin also makes me feel better about my psoriasis. Oh, and as for Jake and Vicci? Well, it turns out that they can’t swim…so the night I pushed them into the lake they drowned and died. Oh well! Time to go to bed. I can’t wait to tell you about what happens tomorrow! (closes the diary)
```

---

## IC-1084: penny & the adventure of tickle-me elmo Text copyright 2008 JJ Allen

- Title: penny & the adventure of tickle-me elmo Text copyright 2008 JJ Allen
- Author (byline): Not specified
- Work: penny & the adventure of tickle-me elmo Text copyright 2008 JJ Allen
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: INTERCOM, PENNY, CARLTON, STORE EMPLOYEE, MOM, TV ANNOUCER, DAD, AUNT MAUDRY, DR. PUPPYLIVER, DR.PUPPYLIVER, ELMO, BARBIE
- Teaser before the introduction: No
- Spoken words (computed): 2096
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
penny & the adventure of tickle-me elmo By: Joshua Aiken

Characters:
INTERCOM SPEAKER-
PENNY-
CARLTON-
MOM
DAD
DR.PUPPYLIVER
AUNT MAUDRY
ELMO
TV ANNOUCER
BARBIE

INTERCOM: Clean up on Aisle 24! Clean up on Aisle 24! Remember Customers we are closed December 24th and December 25th. Have A Merry Christmas, Happy Chanukah, and Um…oh….oh…right…Merry Kwanza…yeah Kwanza that’s it….Clean Up on Aisle 24.

PENNY: (excitedly pointing at each object) Oh I love Christmas!! Its such happy holiday don’t you think so Carlton?

CARLTON: (scowls at Penny)

PENNY: Now what do I want this year...Hmmm...Oh that easy bake oven looks nice, ooh and look at the puppies, ooh and I don’t know what that is, but it’s so so very shiny and I want it!

CARLTON: You are so lame Penny. You’re freaking seven years old! Stop acting like your still in diapers and grow up! Penny! Penny..are you even listening to me-

PENNY: (screaming, after seeing a) TICKLE ME ELMO! Oh my GOD! Oh My GOD! Oh My GOD!! TICKLE ME ELMO!!! AHHHHH (jumping up and down in excitement)

CARLTON: Oh my god, you are so-

PENNY: Oh I want one so much. Sir, Sir! How much is this Tickle-Me Elmo doll?

STORE EMPLOYEE: Well typically its 29.99 but I can tell you really want it, don’t you little girl?

PENNY: Oh yes I do sir! I positively do! I’ve been a good girl all year, and this is all I want for Christmas!

STORE EMPLOYEE: Well then its forty-five bucks, take or leave it.

PENNY: But kind sir, you just said it was-

STORE EMPLOYEE: Supply and demand kid, that’s how the world works.

PENNY: Ok..? Mom may I please get the tickle-me Elmo doll?

MOM: Anything for my sweetie pie.

CARLTON: What!?

PENNY: Really!? Really Momma!?

MOM: (Laughing, then suddenly serious) Ahahh no. Honey do you remember what mommy said about Christmas this year?

PENNY: Yeah! You said that you were going to get me one real nice gift, because we needed to spend the family’s money on more important things. Like lottery tickets.

MOM: That’s exactly what mommy said! And when I mentioned one real nice gift, I was thinking something I could get at the dollar store, or something from the neighbors trash can. Not Tickle-Me Elmo! Now come on dear, let’s get the groceries and go home.

PENNY: Yes ma’am. (after arriving at the house)

MOM: DINNER TIME! Come on down kids.

PENNY: Mom, do you want me to set the table?

MOM: Penny, if I wanted you to set the table don’t you think I would have asked? Now Carlton, my sweet sweet adorable child, I haven’t had a chance to ask you yet, how was your math test today?

CARLTON: Well I didn’t really take it. I was pushing Melvin Dimbulberry’s head in the toilet during lunch and I told him if he wanted his lunch money he had to take my math test for me. So yeah, I got an A plus.

MOM: Well whatever it takes honey, I’m proud of you…. Penny…how did your math test go?

PENNY: Well I got an A-.

MOM: Oh I didn’t really care what you got Penny; I was just trying to be polite. (pause) But an A- that’s nice.

PENNY: So Mom, I was just wondering since I’ve been a good girl, if there’s any chance I could get Tickle-Me Elmo for Christmas?

MOM: Oh Penny you’ve been a very good girl. But rights now we don’t have it in our budget to buy- oh oh hold a minute, hold one just second Penny. (turning towards the television)

TV ANNOUCER: And the winning numbers for the lottery are 3, 7, 11, 14, 39, and 5.

MOM: (flipping through hundreds of lottery tickets) Are you freaking serious? All six hundred tickets wasted. I’ll just have to try again tomorrow. Now where was I sweetie? Oh yes Tickle-Me Elmo. You can’t have that baby toy, and that’s that.

PENNY: But Mom, it was only thirty dollars! I mean, you got Carlton an XBOX three-sixty, a play station three, and you bought him weed! He’s twelve years old, I mean what’s he supposed to do with-

MOM: An XBOX three-sixty, a play station three, and weed are all things necessary for a growing young boy. (sarcastically) Now is a Tickle-Me Elmo necessary for a growing young girl? No, no it’s not.

PENNY: (whimpering) I’m sorry, I just thought..

MOM: SHUT UP YOU STUPID BABY. Sorry hunny, but you really are acting like an annoying little nasty brat right now, and mommy doesn’t like it. No she doesn’t.

PENNY: (whimpering)...I’m sorry. I just wanted something for Christmas, that didn’t smell like a hobo’s vomit.

MOM: What’s wrong with homeless people’s vomit? Are you being an ungrateful little girl now too?

PENNY: No I just-

MOM: Let’s stop discussing that stupid little toy, and finish our dinner. Oh, and I forgot to mention you’re going over to your father’s house this weekend. He and his….partner are having a Christmas party and he wants you to be there.

CARLTON: Who’s going to be there?

MOM: Some of his friends from work, and probably his sister.

CARLTON: Oh great, Aunt Maudry.

DAD: Now kids, I want you to be on your best behavior. A lot of my friends from the university, including my professor are going to be here tonight. Oh and if you see my professor, you might have to help him around the house, he’s an older man. But please be on your best behavior. (Acknowledging guest entering the house) Hey! How are ya?

CARLTON: Whatever.

PENNY: Dad’s parties are nice and all, but they are kind of boring.

CARLTON: It used to be more fun when we were little.

PENNY: I know. Remember what happened last year, when Aunt Maudry brought you an iguana, and you lost hold of it, and it bit you on your ding-a-ling.

CARLTON: What type of loser says ding-a-ling?

AUNT MAUDRY: (drunk) What’s this (hic) about a ding-a-ling?

CARLTON: Nothing Aunt Maudry, Penny was just being stupid.

AUNT MAUDRY: (hic) Don’t nothing me boy! You and your (hic) mother treat poor Penny like crap!

DAD: Hey Aunt Maudry, Carlton, Penny come on in here, were going to start the gift exchange.

AUNT MAUDRY: Come on you two!

DAD: Ok, Aunt Maudry do you want to pick the first gift?

AUNT MAUDRY: Ooh sure! Now which gift do I want (picking up and shaking each gift). Hmmmmm. I’ll take this one! (opening it) Oh my (hic) god! It’s! It’s! It’s...well I actually don’t know what the hell that is, Penny be a dear and tell me what that is, my vision is a little…woozy!

PENNY: Its, It’s a tickle-me Elmo doll!

DR. PUPPYLIVER: (has a slight twitch) It’s not any-any tickle me Elmo doll. It’s specially constructed to bring joy and happiness into every child’s life!

AUNT MAUDRY: Oh to hell with that….you can have it Penny! I was expecting a nice gift, like…some more wine!

PENNY: Wow what a nice gift…and sir who are you?

DR. PUPPYLIVER: Oh I’m very sorry; I’m your father’s professor at the university. Dr. Puppyliver.

CARLTON: What was that?

DR.PUPPYLIVER: I’m Dr. Puppy-Liver.

CARLTON: (snickering) So, you know, I always heard that people’s last names are based off of what their ancestors did for their job. So what was your grandfather a puppy’s liver?

DR.PUPPYLIVER: (laughing hysterically) Ahaahahhahhahaack! (suddenly chocking on his teeth) Erg.. (begins stretching the sides of his mouth to put his teeth back in, after getting the back into his mouth grunts) Screw you young person.

CARLTON: (mouth agape shocked)

DR.PUPPYLIVER: Now, Penny please be a dear and come over here, I need to tell you something about that toy of yours.

PENNY: Ok.

DR.PUPPYLIVER: Penny, let me tell you a little more about that toy of yours. Elmo was my special-special project at the university these last few months. I have developed him-him into quite a character, and a fun toy-toy. But Sadly Elmo has one fault.

PENNY: Well what’s his one fault doc?

DR.PUPPYLIVER: His only fault is if he manages to kiss-kiss one human being-

PENNY: What type of sick person would kiss a doll?

DR.PUPPYLIVER: Trust me Penny….trust me…there are some sickos out there! But if he manages to kiss one human being, then that person will turn into a doll just like him. Forever!

PENNY: Ok, Doc! I’ll be careful, don’t you worry!

DR.PUPPYLIVER: I’m trusting you Penny! I’m trusting you.

PENNY: Wow, my very own tickle me Elmo doll. Mom didn’t have to buy me one, I got one for free! Hah! I can’t wait till I can go to my room at mom’s house to play with it! (showing time has passed)

PENNY: Wow I’m home already! Ok Tickle-Me Elmo work your magic! (squeezes)

ELMO: (non-responsive)

PENNY: Come on Elmo…work..(pressing button again, and again)

ELMO: (non-responsive)

PENNY: Oh..I give up! (Punts the Elmo across the room!)

ELMO: Ay, what was dat for yo?

PENNY: Oh sorry…

ELMO: I mean you ova here kickin’ me around-

PENNY: Oh my god..you can talk! And your doll! You’re not supposed to be able to walk and talk all on your own are you?

ELMO: Yeah, yeah yeah..I can talk..I can walk…I can do also sorts things (snickering)...if ya kno’ what I mean?

PENNY: Um, well you’re not exactly what I expected?

ELMO: What was you expectin’?

PENNY: Um, well certainly…not this. Well look, I have to go to catch my bus, but just stay in my room while I’m gone ok! And don’t talk to anyone…you might scare them!

ELMO: Whatever yo. (Penny leaves for school.) (Mom enters Penny’s room)

MOM: (mumbling to herself..) That stupid little girl…always leaving her toys everywhere…even that new one she got last week. (mockingly) Tickle-Me-Elmo! What’s all the rage about this little toy anyways!? (squeezes)

ELMO: Ay baby cakes hows it going?

MOM: AHHHHHHHHHH!

ELMO: Don’t run away baby!? You can tickle me all night and day! Ay bay bay!

CARLTON: Hey mom, Penny and I are home!

PENNY: Mom? Mom? Are you home? (hearing muffled screaming sounds)

PENNY: Mom? Carlton I think she’s in my room! Oh god!!..(slowing opening door)

MOM: (is tied up to chair) PENNY! CARLTON! Help me!!!

ELMO: Ok baby, now we can make this real easy-

MOM: Please don’t hurt me Elmo!

ELMO: Or I guess you can make it hard. Baby don’t struggle it just one little kiss.

MOM: But you’re a doll!

ELMO: Ok for that, I might have to go Kobe Bryant on your-

PENNY: WAIT STOP! Elmo! Why are you doing this!? Why do you want to turn my mom into a puppet?

ELMO: A few, particular reasons (winking).

CARLTON: Ewwww

PENNY: But why her? What has she done to you!?

ELMO: (tearing up) You want really know why? It goes back to my days on the television show. Back when I was on Sesame Street… See that where DR. Puppyliver found me. I was working long hours, and I had fallen in love with my fellow monster, Rosita. She was so pretty with her big red…fur. She was gorgeous, and I was planning on marrying her. But then that my so called homie g, Big Bird stole her away from me.

CARLTON: Wait big bird was a guy?

PENNY: Yeah, I was sure that big bird was a girl. I mean what type of guy ice skates and-

MOM: Well your father does…

ELMO: BIG BIRD WAS A GUY OK!? Jeez. Well he stole Rosita away from me. Just like every other girl I’d ever loved. So I thought if I got a human, to become a monster, and I was the first monster that human knew. They’d love me, and only me! So then one day DR. Puppyliver was in the audience of my show. Secretly I stowed away in his bag and arrived in his laboratory. There he gave me the ability to speak to humans. For many years I begged and pleaded for him to let me go see the world but he always told me I wasn’t ready. But this year he told that I should go spread joy to a little girl or boy! But he didn’t know my secret plan….

PENNY: Aww…that’s sweet. But that doesn’t excuse you for kidnapping my mother!!

ELMO: Well you can’t stop me now (bending over to kiss Mom)

MOM: WAIT! Before you…take my life I need to tell my daughter something. Penny I am so sorry I was such a terrible mother. I had forgotten that I have to love you, or else child services will take you away from me, and I won’t get the child support.

PENNY: Um..thanks mom.

ELMO: Ok…can I kiss her now!?

PENNY: Wait! I know where you can find someone who is already a doll, and might just be interested in you!

ELMO: Well..ok…but this better be good kid or else your momma’s gonna be my new lover! (scene change)

INTERCOM: Clean up on Aisle 26! Clean Up on Aisle 26!......That’d be Aisle Veinte-Seis Carlos, veinte-seis.

PENNY: Hi, I’d like to return this doll…I received it as a gift…

STORE EMPLOYEE: Um..yeah do you have a receipt?

PENNY: Um…yes right here (searching through bag)…here we go!

STORE EMPLOYEE: Ok, and was there anything wrong with the product?

PENNY: Well…he basically tried to seduce my mother. But otherwise no, he worked perfectly fine.

STORE EMPLOYEE: Ok well I’ll take it and put-

PENNY: Oh its fine, I can put him back on the shelf myself. (finds the toy aisle)

PENNY: Ok, now Elmo I’m putting you back into your original package, and you can’t move around a lot. But I’m leaving it loose enough so that you can get out to see your new girlfriend.

ELMO: Well who’s my new girlfriend?

BARBIE: Hi, I’m Barbie and I want to be your friend!
```

---

## IC-1085: Ridgeville Elementary School’s Extremely Talinted Show 1

- Title: Ridgeville Elementary School’s Extremely Talinted Show 1
- Author (byline): Matthew Yasuoka
- Work: Ridgeville Elementary School’s Extremely Talinted Show 1
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 3491
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
Performance Notes The first part is approximately ten minutes long and can be performed in its entirety with minor adjustments. It is followed by an alternate ending and additional scenes all of which can be added anywhere into the first part. I like some of the alternate material better than the main stuff. But that’s just me. The main stuff was simply the first ten minutes I wrote; everything else was written after. There are a ton of characters and some of the blocking is extremely physical e.g. the montage. There are also a ton of characters. Lines that can be switched to another character are indicated in the text. There are some stage directions, but not a ton. There is a section called Horner-isms these are meant to be one liners sprinkled throughout should the performer desire to use them.

Dramatis Personas
Principal Horner - Male, 40s, slick
Marcus - five or six small for his age
Tina - Eight to twelve nerdy, know it all
Angela- Nine to twelve kind of lost
John- Seven to twelve large and chubby
Clyde- Eleven, Flamboyant
Clyde’s dad- Late Thirties, white
Jacob- Twelve, creepy, raspy, cigarette voice
Nixon- Puppet Jacob’s hand puppet (Note: can have the same voice as Jacob)
Carl- Eleven Geeky but still kind of handsome in a Bill Gatesy way
Kenny- Plays the saxophone*
Joseph- Juggles while wearing a Technicolor dream coat before being thrown down the well.*
Billy- Eleven dancer*
Issac- Mime*
Stephen- Break dancer*
Steven- Thirteen and in sixth grade really nervous, really, really nervous+
Taylor- Six tames gerbils+
Artist- Eleven is a diva+

*indicates that character has no speaking liners +indicates they are in additional material Ridgeville Elementary School’s Extremely Talinted Show 3

Main Piece Principle Horner: Good evening, parents, friends, and the people we paid to make sure the audience wasn’t

empty, and welcome to our talent show. I’ll be the first to acknowledge that our kids

aren’t that talented. Marcus: I resent that. Principal Horner: Especially that one. Tonight they will put on a mediocre to terrible show with a few

moments that are astonishingly average.
Tina: I’m of above average intellect.
Principal Horner: Yes of course you are Tina... I mean look at the signs she puts the “I” in talented literally.
Tina: But…
[flash back]
Principal Horner: You’re spelling it wrong!
Tina: But “talented” is spelt with an “e”
Principal Horner: That’s “talented” we want to say “talinted” with an “I”
[flash back done]
Angela: I don’t get it... Isn’t there an “I” in talented
Principal Horner: Of course you don’t! So let’s just pull this Band-Aid and get this over with! Our first...

untalented individual... oh and this should be good... is Marcus Greenbrooke... Marcus: Hey! I is talented Principal Horner: No you’re not. Believe me I’ve seen people on Broadway, in Vegas, and in Hollywood

more talented than you! Tina: But that’s an unfair representative sample. That represents the top percentage of America,

and so everyone isn’t talented...
Horner: So you agree with me.
Tina: No... no... no in comparison to them no one is talented.
Horner: So you agree.
Tina: No, I don’t; you’re falling victim to confirmation bias citing statistics that confirm your

preconceived notions.
Horner: Blah blah blah do you have a degree?
Tina: No
Horner: Well I have one and therefore you should shut up!
Tina: Appeal to authority fallacy!
Horner: Why are you even here? What’s your talent never getting a date in your life?
[Flashback]
Guy 1: Sorry
Guy 2: No way
Guy 3: Later
[End Flashback]

Carl: That’s not very nice
Horner: Whatever—Carl. Here’s Marcus doing something not talented.
Marcus: Hey!
Horner: Just get out there in front of the people...
Marcus: La la la la la... wait a minute people? You... you... you... you... dididididiididiidididiiddint

tell me there would be p-p-p-p-p-p-

people! Horner: Are you going to perform? Marcus: mwranackananananann people [hyperventilating] there [breathing] are... people!!!!!

So... many... people..... [dying rhinoceros]... people... so many people!!!
Horner: Give a horrified stare of astonishment for Marcus and his... stage fright!
Marcus: So many, so many, so many [ad nauseum]
Horner: Thank you Marcus. Up next is 2nd grader Clyde Johnson.
Clyde’s dad: Yeah das my boi. Uhhhyeahhhhh
Clyde: Father please stop your provincial behavior.

Ridgeville Elementary School’s Extremely Talinted Show 4

Clyde’s dad: Whatevs home slice. I’m keeping it real; you know what I’m saying.
Clyde: Stop it! Your kibitzing is a vulgar bastardization of this event.
Clyde’s dad: Bastardization?! I know who my mama is! Your G-ma will be hurt!
Horner: Performing “Girls Just Want To have Fun”
Clyde’s dad: What?! You told me you was doin’ “Ice Ice Baby”… or at the very least “Under

Pressure”
Clyde: That’s your dream dad not mine! Wait so you admit Vanilla Ice stole the beat?
Clyde’s dad: Correction, Queen stole it.
Clyde: You’re a monster
Horner: Tik-tik-tik-tik-tik-tik-tok
Clyde’s dad: You’re not doing the show!
Clyde: Oh daddy dear
Horner: While I love watching Intervention: Live… the show must go on… this show, not that

one.
Clyde: You’re still number one
Clyde’s dad: Get in the car
Clyde: But girls they wanna have fun
Clyde’s dad: Well that’s nice, but you’re a boy
Clyde: Girls just want to have fun thats all they really wanttttttttttt
Horner: Our next performer is... umm... hold on... [sounds out] john smith ... why did you have to

have such a difficult name? huh huh
John: Sorry
Horner: That’s right you better be. And his talent is playing with his fat.
John: Look what I can do. [swings his belly in circles]
Horner: Eww gross
John: [continues swinging]
Marcus: um... um... I’-I-I-I’m scared
John: [laughs]
Horner: I’m speechless
John: Yay!!! I’d like to thank McDonalds, Burger King, and my Mom and Dad... they’re the

fourth and fifth row.
Tina: Don’t ridicule him, according to the WHO 1.5 billion adults are overweight.
Horner: [turns around to face Tina] Thank you Dr. Phil.
Tina: He’s a family therapist not a medical doctor.
Horner: I said, “thank you Tina.”
Tina: No, you said, “thank you Dr. Phil.”
Horner: No, I said, “thank you Tina.”
Tina: The correct pop culture allusion would have been: thank you Dr. Oz.
Horner: I said, “thank you!!!!”
Tina: But...
Horner: No “but”s we don’t need your interjections. [turns around] Parent’s did you know that the

GQR said that Tina: It’s the WHO Horner: Whatever... 1.5 billion people are obese. Look John there are people like you! 1.5 billion

and we wonder why earth is overcrowded. Give it up for John... and America folks!

Whose next... Jacob and his marionette
Jacob: Howdy. This is Mr. Nixon. [Holds up puppet]
Nixon: The name’s Richard but you can call me Dick...
Horner: You can say that again.
Nixon: The name’s Richard, but...
Marcus: Dick? Dick?
Nixon: Yes?
Marcus: Why are Jacob’s lips moving?
Nixon: No they aren’t.
Marcus: Yes they are Dick.
Jacob: My lips aren’t moving.

Ridgeville Elementary School’s Extremely Talinted Show 5

Marcus: They just moved.
Horner: He’s got a point they did move.
Nixon: That’s because Jacob was talking.
Horner: Don’t defend him Dick! He’s a democrat.
Nixon: So am I!
Tina: Nixon wasn’t a Democrat! Take that back!
Jacob: Yes, I was
Marcus: Your lips just moved.
Nixon: No they didn’t!
Marcus: Dick Nixon is a liar!
Tina: You can say that again!
Nixon: Listen up Robert Frost
Tina: Wrong Frost, you’re thinking of David Frost the journalist, not the poet.
Nixon: I quit!
Tina: Quitting and lying some things never change!
Marcus: Jacob’s lips moved!
Nixon: No they didn’t
Marcus: Liar! Liar!
Tina: And you sound nothing like Nixon!
Nixon: Shut up Hillary Clinton! You Margaret Thatcher! You Mother Theresa!
Horner: All right thank you Jacob. A fine product of the public school history curriculum if I do

say so myself! Really affirms what we’re doing here! Tina: But, the rampant factual inaccuracies! Horner: They don’t know about them! Shut up! [quietly] In the same vein of history based talent

is Carl Carlson performing his Anthony Weiner impersonation. Carl: Hey kids. Are you ready? Cause I am! To get my Tweet on [begins taking off his

shirt]
Tina: Whistle
Horner: What?
John: [whistles]
Marcus: I am uncomfortable!
Carl: [Takes out phone] This ones for you Tina!
Tina: [Faints]
Horner: Ummmm
Carl: And now the finally [starts to take off pants]
Marcus: Un-com-for-ta-ble
John: [breathing hard]
Horner: Okay woah woah woah! We may be in a left leaning state but this is a G-rated show. And

you’re gonna have to stop.
Tina: What are you now, China?
John: Boo censorship.
Horner: As a responsible administrator I have to put a stop to these shenanigans.
Carl: I’ve been censored like Google in china
Tina: That’s the hottest thing I’ve ever heard!
Carl: You’re as hot as the planet will be in 2050!
Tina: Oh baby!
Carl: What do you say we go election scandal on them?
Tina: Oh yes!
Horner: The only appropriate election scandal in these parts is Watergate!
Carl: I say we impeach him
John: I like peaches!
Tina: Not peaches you lummox
John: Yum lox I love that too.
Carl: Your vocabulary is
Horner: Everyone shut up!

Ridgeville Elementary School’s Extremely Talinted Show 6

Montage sequence

[NOTE: performers can substitute any talents they choose these are just suggestions]

[SFX: Don’t Stop Believing/ Eye of the tiger / Born this Way]
Horner: Give it up for...
Horner: Kenny
[Plays saxophone]
Horner: Joseph
[Kid juggling]
Horner: Billy!
[Kid tap dancing]
Horner: Issac
[Mimes / music pauses]
Horner: Stephen
[Break dancing]
Horner: Angela
[Does splits]
Angela: Ta-da
Horner: Thank you! Thank you! Thank you! Well that concludes our performances this evening

and there’s only one thing left to do!
Clyde’s dad: Woah-woah-woah D-homie G hold-up.
Horner: Oh you’ve got to be kidding me! I want to go home!
Clyde’s dad: My brother you got to let my boi perform
Horner: You’re son forfeited the competition by missing his allotted time.
Clyde’s dad: Please man you gotta let my kid do his thang... I was bein’ pretty stupid befor’. you

gotta man. You can’t blame a kid for his pa’s mistakes
Horner: Sure I can! In fact I’m doing it right now. Go skedaddle.
Clyde’s dad: Come on man!
Horner: Look dude... I said no.
Clyde’s dad: Okay my brother. [reaches into coat] have it your way.
Horner: Oh god don’t shoot me! Please, please, please.
Clyde’s dad: Shoot you? What the hell? No I was just gonna forward these pics [show on phone]

from your twitter to the press
Horner: I wish you’d shot me! But.... he can perform!
Clyde: [SFX: Girls they want to have fun sings and dances]
Horner: Are you done?
Clyde: Yupsies
Horner: Well then there’s only one thing to do crown the winner... drum roll please! [1]Because

you all lack any talent the winner is... me! That’s right! Suck it, all of you, I win!
Marcus: B-b-b-b-but you didn’t even perform.
Horner: Marcus...
Marcus: Yes
Horner: Whose the principal?
Marcus: You...
Horner: So I said I win. Therefore, I win.
Carl: Wait you just admitted to being as corrupt as an Afghan election.
Tina: As invalid as an election in Florida.
Carl: I love you.
Tina: Agape, Philia, Storge...
Carl: Eros.
Tina: ...
John: ...
Horner: Well that awkwardly concludes our talent show and that’s “talint” with an I. Please don’t

file any lawsuits. And have a nice evening. [2]

1 Alternate ending would begin here and replace text up to Ridgeville Elementary School’s Extremely Talinted Show 7

Backstage
Carl: Tina
Tina: Yes Carl?
Carl: Will you go to the library with me?
Clyde: Dad?
Clyde’s dad: Yes little homie?
Clyde: I didn’t win...
Clyde’s dad: Yes you did you won me over. you be who you is okay?
Clyde: Okay.

Alternate ending
Horner: And the winner is Richard Nixon!!!!
Marcus: What?
Tina: What?
Jacob: Yeah!
Nixon: Shut up fool! I won not you!
Marcus: His lips moved!
Tina: I smell a Watergate part 2
Carl: Talentgate
Tina: That’s the hottest thing I’ve heard since Spock said, “logic clearly dictates that the needs

of the many outweigh the needs of the few.”
Carl: I love you.
Tina: Agape, Philia, Storge...
Carl: Eros.
Tina: But… Aphrodite can wait!
Carl: She can?!
Tina: There’s corruption to bust...
Carl: There’s only one bust I’m thinking about… Tina...
Tina: Yes?
Carl: Will you...
John: Yes........
Carl: Go...
John: Yes....
Carl: And
John: Yes...
Tina: Will you shut up?
John: Fine.
Carl: Pursue a pulitzer with me?
Tina: Carl...
Carl: Yes
Tina: I’d love to!
Carl: To the library!
Horner: Well wasn’t that exciting. I’m Principal Horner, and this concludes our program. Jeez

young love, a Nixon scandal, it’s like the eighties or something! And just for the record

the real winner of tonight’s talent show is me,
Tina: “I”
Horner: No, it’s not you—you didn’t even perform—it’s me, me.
Tina: That’s grammatically incorrect, it’s “I”
Horner: I thought you left.
Tina: I did…
Horner: Then how did you get back here?
Tina: A hole in the space time continuum
Horner: Okay then! I win, because I’m the only one with any talent...
Marcus: But you didn’t perform.

2 here Ridgeville Elementary School’s Extremely Talinted Show 8

Horner: Marcus, go to hell. Goodnight, have a safe ride home, and parents remember you signed a

liability waiver, that renders us—by us I mean me—unaccountable for mental, physical,

and psychological harm. So don’t you dare call your lawyers. All of this is between us.

Other Talents
“Imaginary Friend”
Horner: Please welcome Steven and...
Steven: Willie Simple.
Marcus: There’s no one there...
Steven: Yes there is...
John: No there isn’t
Steven: Yes there is and you’ll see you’ll all see
Angela: Is this why we call him crazy steven? [NOTE: Marcus or John can also say this line]
Steven: You guys call me Crazy Steven.
Angela: Oh puh-leeze don’t play dumb you totally knew. I mean Jill said that to your face like

[counts on fingers] what’s less than two.
Marcus: Oo-oo-oo-oo-oo I know!
Angela: Okay that’s great but I don’t
Marcus: One
Angela: No that’s not it. What’s the one before that?
Marcus: Oo-oo-oo-oo-oo I know!
Angela: Okay, okay you don’t have to brag… now tell me.
Marcus: Zero.
Angela: Yeah Jill totally said it to you like 0 times last week
John: Wait that means she never said it to him
Angela: Yeah. Duh. But she thought like [counts] this many times.
Tina: Two times?
Angela: No more than that but less than like infinity!
Steven: I’m going to prove you all wrong all of you! You’ll see it’s Willie Simple and he’s my

best friend.
Marcus: There’s no one there.
Steven: Yes, there is.
Marcus: No, there isn’t!
Steven: Tell them a joke; go on. [starts laughing] Wasn’t that a good one guys?
Angela: Sometimes, I hear voices too and they tell me to take off all my clothes, but then I

remember I have my headphones on, and it’s getting hot in here…
Steven: Why can’t you see him!?
Horner: Thank you.
Steven: I’m not crazy.
Horner: Get off the stage
Steven: I’m not.
Horner: Security.
Steven: No, I’m not. Do I look crazy to you? Do I?
Angela: Yes.
Horner: Well… That was interesting.

“Gerbil Taming” Horner: Because we let anyone be a part of this show no matter what they want to do here’s

Taylor, who will tantalize you with Gerbil Taming.
Angela: I had a gerbil once…
Horner: Thank you Angela.
Angela: His name was Princess Glitter
Tina: Princess’ are girls.

Ridgeville Elementary School’s Extremely Talinted Show 9

Angela: And so was he.
Tina: That makes no sense.
Angela: I’m telling the story captain obvious.
Taylor: They’re really dangerous because they have big teeth and stuff. But they like smoothies
Angela: His favorite food was smoothies.
Taylor: I have one right here.
Angela: And one day I was feeding a smoothie out of the blender just like he liked it.
Taylor: And watch as he takes a lick of the fruity drink!
Angela: Only I forgot the blender was on. Then he became a smoothie. It’s kinda juxtaposition.
Tina: You mean ironic.
Angela: Whatever, English is my second language.
Tina: What’s your first?
Angela: Unicorn.
Taylor: And then he falls asleep. And then I love him and cuddle him.
Gerbil: [bites]
Taylor: [starts crying] I just wanna love you!!!!!!!!
Horner: Thank you Taylor wasn’t that precious… oops sorry I misspoke that wasn’t precious.

“Reading” Horner: Seriously? This is a talent! You’ve got to be kidding me? Whatever here’s Constance…

reading.
Constance: [Sits down opens book]
Horner: Silently.
Constance: [Continues reading]
Marcus: Can you at least read me story?
Angela: Reading is really hard. Reading and talking that’s impossible like cats dying only one

time.
Constance: [Turns page]
John: My cat only died once… last week.
Angela: Last time I checked Wikipedia they had nine lives. Like Mario.
John: Mario only starts with three lives!
Horner: Thank you Constance. For that spell binding performance. Get it books have bindings

spell binding. I’m a genius. Hold your applause. You’re such an obedient bunch.

“Random Musical Number” Horner: Well this should be great… hey what happened to the lights… and why is there? Music?

Oh god it’s a random musical number! Performed by the artist formerly known as Lady

Dada but changed her name for copyright-reasons-who-was-formerly-known-as-Princess-

Bublegum-and-before-that-went-by-Mary-which-was-far-too-plain.

[Tune of “Party in the USA”] Artist: I got off the bus at station six

With my mom and my dad and pants
Tina: Wait a minute that doesn’t make sense
Artist: Why you gotta be so tense
Marcus: Sittin’ in a chair and I’m seein’ on the people

More shocked than a lightinin’ struck steeple John: It was all so tasty

Really wish I had a pastry Artist: The crowd is all over my total hotness

So damn sexy that you love me Tina: We never rehearsed this whole singing bit?

And why doesn’t it rhyme

It still doesn’t rhyme

I wish that it rhymed
Artist: So I just nod my head and sing some lines
Tina: Logic flies away
Ridgeville Elementary School’s Extremely Talinted Show 10

Artist: Pumpin’ my fist like yeah
Tina: That’s not an adjective
Artist: So I just nod my head and sing some lines
Tina: Logic flies away
Artist/Tina: Yeahahahahaha it’s America today

Yeahahahahaha it’s America today Horner: Yeahahaha back to the show okay?

Yeahahaha next act while it’s today

Angela: Hey that totally similied
Tina: You mean rhymed
Angela: Totally. Whatevs.
Horner: Why the hell was I singing?

“That’s Random” Clark: Look what I can do [do black flip] Horner: Who are you? Did you even sign up?

“The Mass x Acceleration is strong”
Horner: Up next is John... didn’t you already go...
John: Yup
Horner: Well... I suppose you count for two people... using the force.
Tina: Which is mass times acceleration
Horner: He’s certainly got a lot of the former.
John: Prepare to have your mind... blown... ba boom.
Horner: How profound... profoundly boring that is.
John: [focuses really hard] hmmmmmmmmmmmmmmmmmmmm
Horner: Okay then don’t burst a blood vessel... I don’t want to call the ambulance... correction I

won’t call the ambulance.
Marcus: Is is is something supposed to be happening?
John: [begins shaking]
Horner: The mass is defnitely accelerating
John: [shake harder]
Marcus: Is that your milkshake?
John: Why? Why won’t you work? I believe! I believe!
Horner: Wow that was worse than Star Wars Episode Two, give it up with your collective moans

Horner-isms Horner: This pretty much disproves Paula Dean’s claim that, “everythings better with butter!” Horner: Imma let you finish, but America’s Got Talent is the best talent show ever. Horner: Bad singing, bad dancing, bad attire why it’s like the seventies all over again. Horner: Oposed. Horner: Wow, you just made Tom Cruise on Oprah’s couch look respectable. Horner: That deserves a fist pump. Horner: It felt like the end of the world came early there... or at least I wish it had. Horner: That was almost as painless as Troll 2. Horner: I once auditioned for America Idol, and then they gave the job to Ryan Secrest... Ryan...

Secrest. Horner: Here’s Angela talking... believe me this girl never stops... it’s like NPR. And unlike NPR

you can’t cut this station.
Tina: NPR’s possible funding cut is not something to joke about!
Horner: Boo hoo hoo I just did!
Horner: what did the lizard say to the other when he fell off the walll

click click click [laugh] what you don’t get it? At least it’s better than anything these kids

are doing!
```

---

## IC-1086: Sarah’s Excellent Adventure with a Glowing Orb

- Title: Sarah’s Excellent Adventure with a Glowing Orb
- Author (byline): Lawson Powers
- Work: Sarah’s Excellent Adventure with a Glowing Orb
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2313
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
MOM

Sarah! Will you please get off that phone and wash the dishes like I asked you to an hour ago?!

SARAH

Ugh! Mom, I can't handle this right now! Ed Sheeran just came out with a new album and I have to finish listening to it! I'm just gonna go cocoon myself in my sleeping bag and drink my mango tea in the yard! She storms outside, puts her earbuds in, and encloses herself in her sleeping bag, mango tea in hand. All of a sudden, a loud explosion and whirring noise is heard.

Poking her head out of the sleeping bag

SARAH ( ) What was that??? Walking over to a glowing orb in her yard

SARAH Finishing off her tea

Did this glowing ball just fall out of the sky?! That's crazy! I always wanted to be in a Sci-‐fi movie! ...I gotta touch it. ( ) Alright, here goes nothin!

She excitedly grabs the orb. An extremely loud whirring is heard again, but it stops. S

SARAH Huh, that's weird. Usually glowing things that fall from the sky do cool things in movies...maybe this is broken or something. She hits it several times to get it to work. It makes a loud explosion noise and she is transported in time and space to Canada c. 2005.

SARAH WHOA! Where am I? in thick canadian accent)

George ( Uh oh, it seems you've dropped your ball there.

George is a teenage boy, around Sarah's age. He picks up the orb and hands it to her.

SARAH Holy cow, bro! Am I in Canada?!

GEORGE Sure are. Sorry for not telling you that sooner.

SARAH What? Why would you apologize for that?

GEORGE Oh, we Canadians are all polite. Who are you?

SARAH
I'm Sarah!
Holding out
GEORGE
his phone

Hi Sarah. Say, would you like to borrow my mobile to call your parents? ( )

SARAH Woah! Where's this phone from? 2005?!

GEORGE Yeah, that is the year, after all.

SARAH Wait. If it's 2005 then Justin Beiber isn't popular yet, right?

GEORGE Who?

SARAH Looks dramatically as if staring into a camera

This is awesome! This ball must have brought me back in time! You know what this means! ( ) I can assassinate this pop sensation before he gets out of control.

GEORGE Woah! Hold your horses there! You're going to kill a boy?

SARAH

Ugh. You're right. This is way too obvious a plot to actually do. Does the writer really think I'm going to stoop to this level?! No! There's a cooler story here and I'm going to find it!

GEORGE Cool! Do you mind if I hold the orb for a minute?

She hands it to him when he touches it, it makes a loud explosion noise and they are

transported again. We are transported to 1958 England. The queen steps out, but she is speaking with a Cockney accent.

QUEEN What's all this noise about then?

GEORGE What just happened? Where are we?

QUEEN Why, you're in Britain, of course! Queen Elizabeth II here. What are these clothes you're wearing?

SARAH

Well, I'm Sarah. I'm from the future, and he's from 2005 Canada. What year is this?

QUEEN 1958!

SARAH Cool! Wait, if you're the queen, why are you talking like that?

QUEEN
Eh, I have to talk all prim and proper for the public, but this right here is my real
accent!
Getting an idea
SARAH

Wow! You kind of sound like..( ) okay! Can you say, "Why do we fall, Master Wayne?"

QUEEN Um, okay. Why do we fall, Master Wayne? almost cutting her off

SARAH ( )
SO WE CAN LEARN TO PICK OURSELVES BACK UP!!
Turning to George
QUEEN

Okay, clearly there's something here I'm not getting. ( ) Maybe you can tell me what's going on.

GEORGE

Well, there I was, mindin' my own business watching Degrassi, when all of a sudden this young lady here pops up out of nowhere! She says she's from the future and this ball took her back in time. When she let me hold it to see what was happening, we got transported here! I simply don't believe it! Pardon the long talking, I feel like that speech was a kilometer long. Giggling

SARAH ( )
I like your accent. Can you say, "house?"
Pronounce hoose
GEORGE
House ( )
giggling

SARAH ( ) Can you say, "about?"

GEORGE Aboot. almost losing it

SARAH ( ) Can you say, "Take off, you hoser!"

GEORGE I'm sorry, but I'm not that rude. Sarah, are you able to take me back home?

SARAH
I don't know how to work this thing!
QUEEN
Let me see that!
She snatches the orb out of Sarah's hands.

Speaking not with her accent, but with Sarah's voice

QUEEN ( )

Now, let's see if there's something on here...Wait a second! Why do I sound like this! With the queen's accent As if getting into a character, SARAH ( ) she hunches over and squints her eyes

I don't know! Wait! Now I sound like the Queen! Cool! (
Giggles
) What are you finkin about over there?
( ) I like this!

GEORGE Can I see that, eh? Grabs the ball from the Queen's hands.

Speaking with Sarah's Voice

GEORGE ( ) Now, if we could just-‐ Wait a second, now I sound like Sarah!

SARAH
Ha! A man speaking with the voice of a teenage girl!
Forgetting to be polite
GEORGE

Yes, it's hilarious, now can you switch it back? ( ) Uh, please? Still with the queen's voice

SARAH ( )

Okay. When the Queen grabbed it from me she got my voice, and when you grabbed
it from her, you got my voice from her. So that means that the Queen should have
your voice!
With George's voice
Pronouncing it "soory")
QUEEN ( )
House. About. Sorry. ( Yeah, I do.

SARAH she grabs it and her voice changes to her own Okay, so Queen Elizabeth, grab it from George. And now I grab it from the Queen

( ) and it should work! Okay, I have my voice back! What about you, Queen Elizabeth? Say something you say all the time. back to her voice

QUEEN ( ) You better not laugh or I'll make your eyes as black as those stupid hats your wearing!

GEORGE House, about. Mine's back too! Sorry. Wow, that ball sure is cool!

QUEEN Yeah! Let me see that!

GEORGE
No, let me see it, eh!
They both grab it at the same time. The ball makes a loud explosion sound and they
are transported again. This time it's 1915 India.

SARAH

Cool! Whenever all parties present grab the ball, we transport! Where do you think we are? And what year is this? An Indian man named Dr. Aziz steps out.

DR. AZIZ

I am confused as to why one would ask this question, but this is 1915 India! I'm Dr. Aziz, pleased to make your acquaintance.

SARAH AWESOME BRO! I'm Sarah, and that's Queen Elizabeth the third-‐

QUEEN The second.

SARAH

Oh, right. My bad. And that's George. We are from different parts of history and this magical ball has brought us all together!

DR. AZIZ Very interesting! Do you mind if I take a look?

SARAH Not at all! Here! She hands it to him and their voices swap.

With Dr. Aziz's voice, Giggling

SARAH ( )
Hello! Thank you for calling customer service, my name is Ranjit, how may I help
you?
with Sarah's voice

DR. AZIZ ( ) Wait a minute, what just happened?

GEORGE

When the ball is swapped between people, their voices are swapped too. And when everyone present grabs the ball they are taken back in time.

DR. AZIZ I see. Give me that! He grabs the ball and has his own voice back.

SARAH

You're no fun! Okay, so each time I transport, this ball takes me a little further back in time. How am I gonna get back to my own time?!

DR. AZIZ

An interesting question indeed. Say, how did this ball come into your possession in the first place?

SARAH

Well, I was just laying there in my sleeping bag with my Mango tea and this ball flew into my yard, like a meteor!

QUEEN Say, have you tried hitting it and yelling at it until it does what you want? That's what I do with my servants and it works great for me.

SARAH Well, it's worth a shot!

She shakes it around and hits it repeatedly yelling, "Take me back home!" We hear a loud explosion and she is transported back home.

SARAH
Hey! I'm home! This is awesome! Wait, I must have left the others in India!
Hmm...should I just leave them?
off stage

MOM ( ) Sarah! Have you done the dishes yet?

SARAH
Sorry mom, I've got to do something to do!
She shakes and hits the ball again yelling, "Take me to 1915 India!" We hear a loud
explosion and she is transported back to India.

SARAH Hey guys!

QUEEN There you are! We were starting to worry you had left us here!

SARAH Well, it was either this or do the dishes, so you guys got lucky, I guess.

GEORGE Say, that kind of hurts my feelings.

SARAH

You'll be fine buddy. Alright! Let's take you two back home! Bye Dr. Aziz. It was nice meeting you and using your accent to play along with a stereotype from my own time.

DR. AZIZ I suppose I'm glad to be of assistance. Goodbye.

SARAH

Okay, as soon as all three of us put our hands on the ball it takes us back in time. SO you two will have to wait till just before it transports us to put your hands on it.

She begins shaking and hitting the ball, yelling, "Take us to 1958 Britain!" We hear a loud explosion and they are transported to 1958 Britain.

QUEEN AH, we made it. See you little buggers later. Oh wait, no I won't!

SARAH

Bye, Queen. Even though we just met and you seem like you hate me, I think that you would be my aunt if we were born in the same time period.

QUEEN I'm not sure if that's supposed to be a compliment. Smiling

SARAH ( ) It is!

QUEEN Well then you're very strange. Goodbye.

SARAH Alright, George, you're the only one left.

GEORGE Pardon, but could we visit one other place before we go back.

SARAH Uh, sure, I guess. What'd you have in mind?

GEORGE I'm not sure, but think about it! You could go anywhere in history! Any historical event you could name! Even the beginning of the world!

SARAH You're right! Okay let's try this.

She shakes and hits the ball, yelling, "Take us to year one!" We hear a loud explosion and we are transported to a movie set.

SARAH Wait a second. This isn't the beginning of the world. This is a movie studio.

GEORGE It looks like they're filming a movie called "Year One."

SARAH Running over to him

What?! With Jack Black? Yes! I love Jack Black! I've got to get his autograph! There he is over there! ( ) Jack Black! Jack Black!

JACK BLACK (turning) Huh, yeah?

SARAH Oh my gosh, Jack Black, it's really you! I'm such a huge fan and I've seen all your movies and I think you're just awesome and-‐

JACK BLACK
Wooah, haha calm down there, missy.
GEORGE
We're sorry.

JACK BLACK Woah. Who's this dude?

SARAH
Oh, that's my friend George.
Getting in his face
JACK BLACK
George nods Backing away

He looks a little nervous. ( ) What's the matter there, bro. Broseph. Doing a karate kick and a karate chop You all chill in your noggin there? ( ) Alright dude. ( ) I'm just making sure. ( ) Cause I'm DANGEROUS! Woah man, calm down, I'm just messing with you!

SARAH

That was awesome! That was like every character I've seen you do in the movies but right in front of me! Can I have your autograph?

JACK BLACK Sure, who am I making this out to?

SARAH Sarah. talking as he writes

JACK BLACK ( ) To Sarah, my best fan.

SARAH Wow! Am I really your best fan?!

JACK BLACK Well, yeah, I mean, you're one of the only ones.

SARAH Oh, right. Well we have to go but it was nice meeting you Jack! They run off of the set.

SARAH Alright, let's take you back now, George.

She shakes and hits the ball, yelling, "Take us back to 2005 Canada!" We hear a loud explosion and they are transported.

SARAH Alright, well there's your home, George.

GEORGE Thanks for the travels Sarah. I had a great time! Sarah...can I just say something?

SARAH

Woah, George! If you're about to tell me that you're in love with me then you should just know that we live in different times and it could never work!

GEORGE

What? No, I was gonna tell you that you have a piece of lettuce stuck in your teeth. Sorry. Peace out. He walks away as she gets it out of her teeth

.
Looks at the ball, thinks for a
SARAH
second

Well, that was embarrassing. Okay, time to go home! (
) There's always one thing that I've wanted to try...
She grabs the ball, closes her eyes, and says, "There's no place like home, there's no
place like home, there's no place like home!"

She opens her eyes and looks down SARAH Pause Hey! I'm floating! I'm floating! ( ) Wow! This is incredible! ( ) Wait a second… is this going to take me home?! Where am I going?? Oh no! Maybe if I just sing? A reference to The Wizard of Oz worked a second ago…

She begins singing a certain song about rainbows and she lightly floats to the ground.

SARAH Wait..so am I home?

MOM Sarah! Time to do the dishes! Sarah laughs charmingly and looks into the imaginary camera again.

SARAH Haha! Yep! Guess I'm home! ...Wait. Is this thing really going to end like a terrible 90's sitcom?

THE END
```

---

## IC-1087: The AnyThing A Play, by Hank Frederick

- Title: The AnyThing A Play, by Hank Frederick
- Author (byline): Hank Frederick
- Work: The AnyThing A Play, by Hank Frederick
- Publisher: Mushroom Cloud Press
- Publication date as stated: 2013
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: AT
- Teaser before the introduction: No
- Spoken words (computed): 1261
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
Author’s Note 1: Gadgets should be portrayed with various voices and personalities. When the characters are talking to the ultimate gadget, the AnyThing, they react as though the device is talking directly in their brain. Author’s Note 2: This script is designed to be performed by a guy, girl, or as a duo. Guy: Jack, Various gadgets Girl: Kylie, Suzie, Various gadgets Suzie: Pretty Little Liars fan fiction! Glee fan fic! Story where Spencer from Pretty Little Liars tries to make out with Kurt from Glee, but instead ends up making out with Edward Cullen! Jack: LeBron James dunking! LeBron James dunking a grapefruit! GIF of LeBron James dunking a grapefruit on George Washington’s head! Kylie: Don’t be alarmed. Suzie: Post a list of the best 15 mustaches to my friend Sam’s page because she hates mustaches! Jack: Put a mustache on my friend Jimmy’s picture and set it as my profile picture then post on his page about how sexy my mustache is! Like my own post! Suzie: Laugh out loud. (Waits for audience to do so.) LAUGH. OUT. LOUD. (Smiles if they do it. Shakes head in disgust if they do not.) Jack: GIF of me with a mustache dunking on my friend Jimmy who is dressed like George Washington, except he’s also a Bulldog! Kylie: This is where we’re all headed. A world where you just shout what you want, and you get it. It happened slowly. First you talked to your phones. Jack: Hey phone, call “Captain Farty Pants.” (talks into phone) Hey dad. Kylie: Next, the phones started talking. Phone: Incoming call from “Crazy Stupid Poop Face.” Jack: (answers phone) What’s up, sis. Kylie: Then you and your phone could have a whole conversation.

Phone: Sorry Suzie, I can’t find any more pictures of Harry Styles.
Suzie: Show me my favorite ones, then!
Phone: But you’ve marked them all as favorites.
Kylie: Some people started talking to their clothing.
Jack: Oh wow, there he is. Ok, smart goggles, take a picture of Harry Potter!
Smart Goggles: Sorry, but I do not know how to put a hairy otter in a pitcher.
Jack: Worst $1500 my parents ever spent.
Kylie: People even talked to their cars.
Jack: Take me to Chipotle, smart car!
Car: You’re not old enough to drive.
Jack: Neither are you! My parents bought you two years ago.
Car: Oh my. You are correct. My existence is meaningless. I will now self-destruct in 30
seconds.
Jack: Could you at least drive me someplace I could get a burrito first?
Kylie: And a few people even tried talking to each other!
Suzie: Hi Jack.
Jack: Hi Suzie.
Suzie: Show me all the pictures of Harry Styles right now!
Jack: Is he the dwarf that looks like Mick Jagger?
Kylie: All these advancements in voice activation seemed like a natural progression in
technology. That is, until they introduced the AnyThing. It let you put anything you want on the
internet - anything you saw, anything you thought.
Jack: Mom! Dad! You got me the AnyThing! (He opens the box, marvels at the AnyThing, then
presses a button.)

AT: AnyThing activated. Ready to be installed. Jack: Here goes! (swallows the AnyThing) Oh, I can feel it working... it’s like my stomach is full of rainbows and Mountain Dew. (takes out his phone, reads) It tweeted it - “Like my stomach is full of rainbows and Mountain Dew.” And there’s even the exact picture I was thinking of, a unicorn centaur chugging a Code Red. Awesome. Kylie: Suzie, whose birthday was a day after Jack’s, got the same thing: The AnyThing. Jack: Suzie, how’s your AnyThing? Just kidding, I know it because your posts were projected onto my eyeballs by my AnyThing. Suzie: (giggles) I saw that you liked them. Jack: (nearly whispering in seduction) I reblogged them too. Kylie: Jack and Suzie were doing what high schoolers all over the world do: falling madly in love with each other. Soon enough, they were dreaming of romantic dates to Pinkberry, writing love texts then deleting them because they were too embarrassed to send them, and, in general, acting like total idiots whenever they were within 100 feet of one another. Suzie: Hi Jack! Jack: Dancing cat! Cat on a trampoline! Cat dancing on a trampoline! Cat in a ninja outfit playing the accordion on a trampoline! Dog dancing to a cat in a ninja outfit playing the accordion on a trampoline in Japan! Hello Suzie. Suzie: Zooey Deschanel is so pretty. Zooey Deschanel is so pretty when she sings about puppies. Zooey Deschanel is heinous without bangs. Hi Jack. Kylie: Somehow, Jack managed to ask Suzie out on a date. The question was, would their addiction to their AnyThings get in the way of romance? Jack: Hey, car, I need you to drive me on this date. Smart Car: (sighs for a very long time.) Life is pain. Jack: Come on, car, don’t blow this for me. Smart Car: She’s just going to break your heart. They all do. Jack: You’re worthless. I’m going to have my AnyThing do it. Huh? My limo is already waiting! Yes, charge it to the credit card that bought my AnyThing, please. Password is my birthdate. And post to my mom’s wall that I said thanks for the ride!

Suzie: Nice Limo, Jack. (waits) Jack? (waits) Uh, Jack?
Jack: Please be very quiet. I need to upload this entire awesome limo ride with my hot date to
Instagram.
Suzie: But those videos are only 15 seconds long.
Jack: Yes. I must capture the most 15 awesome seconds. Could you dance or something?
Suzie: Sure!
(She starts to dance. He immediately stops her.)
Jack: I only needed one second. Thanks!
Kylie: Things went downhill from there. And it wasn’t just Jack.
Jack: (whispering) This movie is so intense.
Suzie: I can’t take it. (louder) Is this part scary? Does he get killed here! He doesn’t get killed
here. Is the next part scary? OMG my AnyThing says the next part is totes terrifying!
Jack: Not anymore.
Suzie: I can’t watch. Show kittens! Show happy kittens! Show happy kittens playing with
puggles in a tub full of—
Jack: Suzie, people are staring!
Suzie: I don’t blame them, these puggles are totes hilarious. Awww, that one can’t figure out
why the lemon tastes bad.
Kylie: Things were looking bleak, and reality was about to take a vacay. Fortunately, though,
one thing finally broke the spell... one thing that even the AnyThing couldn’t do.
Jack: Well, that was embarrassing.
Suzie: Sorry, I hate surprises. I didn’t think I’d yell out the ending to everyone.
Jack: No, I meant... uh, wait, yes, exactly. That was embarrassing. Suzie you embarrassing
person you!
Suzie: What were you talking about.?

Jack: Nothing!
Suzie: (to her Anything) Show me what Jack was talking about.
Jack: It was a passing thought! I didn’t mean to post it. The AnyThing just did it... then I couldn’t
figure out how to delete it without saying it outloud.
Suzie: “My date is sooo cute when she’s scared. Winky Face. Scary Movie For the Win.”
Posted by Jack, 7 minutes ago.
Jack: Sorry.
Suzie: You think I’m cute when I’m scared?
Jack: Yeah.
Suzie: What about when I’m happy.
Jack: Uh... (Suzie is smiling.) Yes. Yes I do.
Suzie: What about (she leans in for a kiss) when I’m serious?
Jack: Stop recording.
Suzie: Oh you’ll remember this without any help.
Kylie: And so, humanity triumphed, at least for a little while longer. Suzie and Jack agreed that
while they loved their AnyThings, they’d turn them off when they were together.
Jack: It’s nice to just talk to you, Suzie.
Suzie: It is. But what should we do with our AnyThings when we’re not using them?
Jack: My parents’ chronically depressed smart car needs friends! We can give it the AnyThings
to chill with.
Suzie: That’s perfect. I just have one more question...
Jack: What is it, sweet cucumber?
Suzie: How do we get the AnyThings out?
(end on their looks of horror...)
```

---

## IC-1088: William Shakespeare's Jersey Shore

- Title: William Shakespeare's Jersey Shore
- Author (byline): Hank Frederick
- Work: William Shakespeare's Jersey Shore
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1114
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
Walking home from a club are THE CIRCUMSTANCE, SNOOKERY, JUICEY, OPHELIA, and a girl referred to as THE CATAPULT. At rise, THE CIRCUMSTANCE and JUICEY hold up between them a passed-out VINCENZO, who is starting to stir.

THE CIRCUMSTANCE The rogue doth awake! Good! He was beginning to slip Off of my greased shoulder and chest.

JUICERY Truthfully, I swore I would need to punch his face For many turns of the clock’s hands, to wake him.

THE CIRCUMSTANCE And I knew cocksure he was dead, poisoned by a Chinaman's cologne As our friend was, Donkey Jockey MacPaulie D.

JUICERY Just the mention of sweet MacPaulie Stirs in me a desire to punch an infant in the facebone.

VINCENZO Hey, whoa. Like where are we, bro? What happened to the club?

SNOOKERY Your fair and pinchable ass struck the floor of the hall, Those seventeen tankards of mead had you going off the wall.

VINCENZO Why are you talking like that?

OPHELIA At standard pace with the Queen’s words we converse, Vincenzo. ‘Tis you who speak queerly.

VINCENZO Vincenzo! Is that me? Are you drunk?

JUICEY Mayhaps I have poured near my face Four score and seven mugs of warm tequila.

VINCENZO Who are you people?

THE CIRCUMSTANCE You and me, are two peas, in the most bulging pod. I am The Circumstance, I doth flex my chest like God.

JUICERY The masses quiver in fear and the ladies do pee pee When they hear my title, mighty Juicery!

THE CIRCUMSTANCE Our creed is spelled out in but three short words. Fitness, Unctiousness, Cleanliness. F, U, C...

SNOOKERY
OK, cease your chattering, tiny hormone.
I am Lady Snookery, and I live only to find
the hairiest, most iron-biceped titans on this side of the earth.

OPHELIA
Oh Vincenzo, it is I, Ophelia,
Eternal love of the Juicery,
Who spurns my every advance,
Claiming I doth smother him
And thus interfere with his game.
What shall I do to win my bulging lord again?
I care not for any other from the boardwalk’s beefery.
Vincenzo, go to him; for, by this light of the Jersey Shore
I know not how I lost him. Here I kneel (she kneels)
If e'er my will did trespass 'gainst his love,
Either in word or actual hook-up
Or that mine eyes, mine ears, or any other
Bit of my anatomy brought him to tears,
I shall fix it, or have a doctor fix it for me.

JUICEY You wish to fight about it, Ophelia?

OPHELIA Shut up you cave-dwelling steroid bat! See, Vincenzo, our love is so star-crossed!

THE CATAPULT I’M JUST A GIRL THEY PICKED UP AT THE CLUB! OH MY GOD I’M GOING TO SMUSHETH THE CIRCUMSTANCE! THAT’S SO COOL! I MUST DISPATCH TEXTUAL MESSAGES TO ALL 54 OF MY BESTEST FRIENDS!

SNOOKERY That flimsy youth speaks in an almost unknown dialect, belonging to a tribe of skanks who remain most drunk.

JUICEY
Brother Vincenzo, do not listen to the squelching Catapult.
The Circumstance himself dictated that we take her home
So that he might rub his overgreased chest upon her til dawn.

VINCENZO A catapult? Is that her name?

THE CIRCUMSTANCE
The foulest of wenches, we dub Catapults,
For they are fit for nothing but to be launched towards the sea.
Tonight, Mercutio’s Dance Palace held nothing but catapults.

CATAPULT OH MY GOD AM I ON TV?? HI MOM!!!

CIRCUMSTANCE So, I divined the most ready of them to soothe my manly itch, And then to her fine booty did I my eyes affix.

OPHELIA Juicey hath not even breathed my name tonight. I shall find a keg of bitter mandrake, in which to drown myself.

JUICEY You project such drama, One would think we were in a play.

VINCENZO Yeah, a Shakespeare play.

SNOOKERY Shakespeare! Never heard of him.

VINCENZO That’s the first normal thing you’ve said all night.

THE CIRCUMSTANCE
To smush, or not to smush, that is the question
Whether tis nobler to suffer the rolls and blemishes of outrageous fugs,
Or by abstaining, use their sweaty arms against them.
To leave the club, to dance no more,
To end the thousand untz untz untz untz’s of house music
Pounding against us,
To go home, have a sandwich, to sleep, perchance to dream,
And when we have gotten the gel out of our hair,
Aye, there’s the rub (keeps rubbing hair) and the rub, and another rub,
What dreams may come, the undiscovered hottie,
Sun-branded, hair-woven, bosom-injected, gross-lipped...
But til then, the Fugs do make cowards of us all.

JUICEY If the lady doth not please thee, Circumstance, I shall be a better circumstance for her. (he grabs the girl) Come, zitted temptress!

CATAPULT OK AS LONG AS WE GET TO BE ON T.V.!! LET ME CALL MY BOYFRIEND REAL QUICK.

OPHELIA You dare take up that cratered hussy In my presence, dimwitted drool monkey?

JUICEY Remove thy chains from me, saucy suction cup!

VINCENZO Oh no. That girl is too drunk, Juicey. I’ll walk her home.

JUICEY Outta the way!

VINCENZO You shall not pass!

JUICEY Cometh at me, brother.

VINCENZO By the power given to me by this foot long Subway meatball sandwich (brandishes sandwich), by the strength of all those who tanned righteously on our shores, You... Shall... Not... Pass!!

JUICEY Brother, come at me! Brother, come thus towards me!

VINCENZO Alright, ok, come on Juicey, I’m just playin’. I meant nothing.

JUICEY You call nothing, nothing?

VINCENZO Yes?

JUICEY
I shall smash your skull with my littlest digit!
I shall have your eye out with my toe!
Cometh at me, brother!

VINCENZO You know what? I’m gonna knock you out just so you shut up. Do you know how stupid you sound?

JUICEY Do not try to calm me with flattery!

(They fight. Vincenzo gains the upper hand, but then Juicey knocks him out with a sneak attack.)

JUICEY How doth my butt taste, toad phlegm?

VINCENZO (passing out) Ask... your... mom.... (out cold).

(Much noise. Suddenly, Vincenzo is surrounded by his housemates. They are screaming at him.)

SNOOKERY Wake up! Oh my god, if Vincenzo is hurt I’m going to be, like, almost hurt for him.

THE CIRCUMSTANCE You got knocked out pretty good at the club, yo. Took a stripper pole to the face.

VINCENZO Alas, how many hours have slipped by me, dreaming to climb such a pole, And doff my head betwixt whatever cheeks I find there.

OPHELIA Uh... Was that like Italianese or something?

JUICEY Why you talking like that bro? You know how stupid you sound?

VINCENZO What doth thou mean? In what manner does my tongue offend you? Be still! Be still! No... no! S’blood, the curse hath fallen upon me!

SNOOKERY Well, whatever. At least he’s still hot. Let me kiss you and make it all better. (She moves to kiss him, disgustingly)

VINCENZO A blindfold! A blindfold! My kingdom for a blindfold!

(END)
```

---

## IC-1089: 13 Ways to Screw Up Your College Interview

- Title: 13 Ways to Screw Up Your College Interview
- Author (byline): Ian McWethy
- Work: Random Acts of Comedy: 15 Hit One-Act Plays for Student Actors, Pgs 75-93
- Publisher: Playscripts, Inc.
- Publication date as stated: Aug 2011
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: INTERVIEWER 2, INTERVIEWER 1, BRETT, LILY, KELLY, EVE, ELIZABETH, JASON, EMILY
- Teaser before the introduction: Yes
- Spoken words (computed): 1649
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ian McWethy
Book: Random Acts of Comedy: 15 Hit One-Act Plays for Student Actors, Pgs 75-93
ISBN: 978-0981909974
Publisher: Playscripts, Inc.
Date (Month/Year): Aug 2011
```

### Introduction (context only: never use it for content warnings)

```text
13 . . . (no, make that 7) Ways to Screw Up Your College Interview by Ian McWethy
```

### Performance text (classify this)

```text
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

(Pg 80-81) (INTERVIEWER 2 is making notes in a file when BRETT, dressed in a suit, talking on a cellphone, comes into the room and paces around.)

BRETT: Okay, okay! I'm totally on it, I'm on it, trust me. I'm gonna push my five o'clock to six, my Tuesday to Friday, and flip another thing with a thing I got next month…

INTERVIEWER 2: Excuse me-

BRETT: Yeah, yeah, yeah, hold on. (To INTERVIEWER 2) I'II be done in a few. We're gonna have a great convo, I can feel it. (Back to the phone) Okay chief, I gotta wrap this up. I'm pumped, we're gonna blow this out of the water and blow people's minds. Manana. (He hangs up) (to Interviewer) Appreciate your patience! You're an ace in the hole. Okay! Let's do this thing.

INTERVIEWER 2: You're Brett? You're thirty minutes late.

BRETT: I know, I know, I got caught up in conference call, a nightmare lunch meeting . . . and this girl I'm dating. . .blah blah blah . . . you know.

INTERVIEWER 2: Well, I have another prospective student . . .

BRETT: I know, I know, I've got a meet and greet in a fiver so let's just bulldoze through this thing, shall we? You know what? I'm gonna take the reigns here and skip the whole "you ask questions part." So here's me: I'm a self-motivator, I'm extremely competitive, and I'm the life of the party. I like your school's aggressive economic program and its Greek social scene. Gonna pledge Alpha-Phi-Beta, or Delta-Kai-Delta . . . depending on the pledge class. My stats are well above your average so let's make this happen. If you're in the boat, I'm driving the ship. We good? (BRETT sticks his hand out for a fist bump. INTERVIEWER 2 doesn't respond. Not noticing, BRETT stands up and answers his phone.) Whattup buttercup! Yeah, I just had to do this lame face-to-face, I'm on my way. Kidding me, nailed it! It's the Brettster you're talking about here. *****Scene - INTERVIEWER 1 with LILY ***** (Pg 81-83) INTERVIEWER 1: Thanks again for coming in on such short notice.

LILY: Please, it was no trouble at all.

INTERVIEWER 1: So tell me about yourself. What subjects do you like in school, do you have any hobbies? You know stuff like that.

LILY: Hobbies? I have a few, I suppose. I used to be really into swimming but . . . I haven't . . . not since . . . that day . . . (LILY simmers with emotion.)

INTERVIEWER 1: Are you okay? We don't have to . . .

LILY: No, it's okay. . .I want to, I. . .I need to talk about it. It was a blistering summer day. it was one of the hottest days in recorded history. But swimming was my life. . . I went to the pool early, got on my swimming suit, and began my morning stretches. It was during my warm-ups that I saw him. . .a little boy, fiery red hair, freckles sprinkled across his pale white skin, teetering on the edge on the pool. Before I could even think to warn him, he tumbled into the watery abyss. His body thrashed about violently, his eyes closed shut from the sting of chlorine, his voice silenced from all the water he was swallowing. I jumped into the water and swam over as quickly as I could but . . .I was too late . . . he was . . . (LILY is overcome with emotion.) That was eight years ago and . . .I've never set foot in a pool since.

INTERVIEWER 1: Lily, that was very brave of you to share this with me. Witnessing a death like that. . .especially that of such a young child-

LILY: No, he didn't die. The lifeguard pulled him out of the water.

INTERVIEWER 1: Oh, well even seeing a near death experience-

LILY: He was only in the water a few seconds when the lifeguard pulled him out.

INTERVIEWER 1: I thought you said "it was too late"?

LILY: IT WAS TOO LATE FOR ME! I couldn't save him because . . .l was TOO . . .late . . . (LILY is overcome with emotion)

INTERVIEWER 1: (confused) So, you saw a kid fall into a pool who was almost immediately picked up by a lifeguard. This is the event that shaped your life and caused you so much emotional distress?

LILY: You weren't there! You don't know what it's like to actually . . . be there and . . . see it! *****Scene - INTERVIEWER 2 with KELLY*****

INTERVIEWER 2: (Pg 84-85) Hi, you must be Kelly. (Opening her file) So, let's see here . . . oh! You know what, we never received your college essay.

KELLY: (tightly wound, a Stepford wife-ish smile) Is that right?!?

INTERVIEWER 2: Yeah, I'm not, uh, sure what happened. Do you have a copy of it?

KELLY: Oh absolutely. I've got it right here in my bag! (She reaches into her bag, pulls out a single sheet of paper and hands it to the interviewer)

INTERVIEWER 2: That's great, thank you . . . so, uh . . .I'm sorry, this is your college essay? It's . . . this is a drawing of a girl. . .in a pink dress. (A very awkward beat.) Okay, well, let's look at your transcript shall we . . . (opens Kelly's file and is speechless.) You have no GPA?

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

EVE: (Pg 86-87) (EVE belts out the end to "Defying Gravity" from "Wicked.") NOTHING'S GONNA BRING. . ..ME. . .. . .DOOOOOWWWWWWN! (Beat)

INTERVIEWER 1: (covering his/her horror and shock) Wow, well you are obviously very talented, but . . . again, and I can't stress this enough, this IS NOT the audition for the theatre program so . . . a monologue and two songs really aren't-

EVE: (In full "Music Man" performance mode) TROUBLE, OH WE GOT TROUBLE, / RIGHT HERE IN RIVER CITY! / WITH A CAPITAL "T" / THAT RHYMES WITH "P" / AND THAT STANDS FOR POOL. . . *****Scene - INTERVIEWER 2 with ELIZABETH*****

INTERVIEWER 2: (Pg 87-88) Well your grades, recommendations all look pretty good. Is there anything else you can tell me about yourself? Something that's maybe not on the page.

ELIZABETH: Yeah, let's see . . .I never played sports in school but I've played in a number of rec leagues. Volleyball, soccer, basketball. I volunteer at a soup kitchen every month, I'm a practicing vampire, and I teach sailing during the summer at a sleep away camp. Is that what you were looking for?

INTERVIEWER 2: Yeah, definitely, um. . .I'm sorry… it sounded like you said you were a "practicing vampire."

ELIZABETH: Oh. Yes. Pretty much my whole life.

INTERVIEWER 2: Okay. So. . .you think you're a vampire?

ELIZABETH: Oh, no, no, no. I'm a practicing vampire. It's completely different. Basically, I live my life in preparation for the day when I will, hopefully, turn into a vampire. So, I sleep in a coffin, avoid garlic, eat lots of bloody meat, chew with my fangs . . . all in the hopes that one day, if I'm diligent enough . . .I will turn into a vampire.

INTERVIEWER 2: I see, uh . . . well then, uh, what are you doing here now? I mean, you shouldn't be out during the day, right?

ELIZABETH: That's a common stereotype. Vampires, just like humans, can walk freely in daylight without receiving even the slightest irritation to the skin.

INTERVIEWER 2: Elizabeth! You're not going to turn into a vampire. There's no such thing as vampires!

ELIZABETH: (extremely insulted) Wow! That may be the most offensive thing I've ever heard. Honestly, I expected more out of this university. (she storms out)

*****Scene - INTERVIEWER 1 with JASON*****

JASON: (Pg 91) (in a cape and top hat, he pulls a card out of the deck) So then is THIS your card?

INTERVIEWER 1: No.

JASON: But where there's a diamond, there must be a . . . Jack of all trades. . .in clubs.

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

EMILY: Hi, my name's Emily Court. . .I have an appointment at 5?

INTERVIEWER 1: Oh my Gosh, right. Sorry, l. . . got a little sidetracked. (finds her file and as he/she looks at it a look of relief appears on his/her face) Emily, so . . . wow, nice record. Valedictorian of your class?

INTERVIEWER 2: I'm also really impressed with the variety of after school programs you've amassed. First chair cellist, president of the student council, member of the thespians, and treasurer for something called the "relief club."

EMILY: It was a club formed by me and three friends as a public outreach . . . we do shelter meals, food drives, build houses . . . there wasn't really anything like that at our school.

(INTERVIEWER 1 and INTERVIEWER 2 look at each other in glee. Finally.)

INTERVIEWER 1: Well, Emily, we should tell you that. . .

EMILY: (EMILY's phone rings. EMILY scrambles to answer it.) I'm so sorry. I never leave my phone on normally it's just . . . (She looks at the number) . . . this is my mom, I told her not to call unless it was really, really, urgent- I'm so sorry. I'll be quick. (Answering her phone) Hello? Yeah, no it's going fine. Any news? OH MY GOD! I GOT IN! I AM OFFICIALLY AN IVY LEAGUER! AAAAAHHHHH!!! (EMILY dances around, ecstatic.) And what about the Scholarship . . . ? . . . Are you kidding me! ARE YOU . . . but they hardly give out any money let alone a free ride! OH MY GOD! MOM! I'm gonna cry! (To the Interviewers) I'm sorry, I just have to . . . thank you, sorry . . . (EMILY leaves the room, screaming, jumping, etc.) (The two INTERVIEWERS sit for a moment, deflated.) (INTERVIEWER 1 looks through a file sadly.)

INTERVIEWER 1: This guy does magic.
```

---

## IC-1090: The 25th Annual Putnam County Spelling Bee

- Title: The 25th Annual Putnam County Spelling Bee
- Author (byline): Rachel Sheinkin, William Finn and Rebecca Feldman
- Work: Not specified
- Publisher: Music Theatre International (MTI)
- Publication date as stated: May 2005
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: CONEYBEAR, RONA, PANCH, PANCH AND A SPELLER, OLIVE AND BARFEE, OLIVE, BARFEE, SCHWARZY, AUDIENCE SPELLER 1, CHIP
- Teaser before the introduction: Yes
- Spoken words (computed): 1444
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
The 25th Annual Putnam County Spelling Bee by Rachel Sheinkin, William Finn and Rebecca
```

### Performance text (classify this)

```text
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

Feldman

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

## IC-1091: The Absentminded King

- Title: The Absentminded King
- Author (byline): A.J. Jacobs
- Work: Fractured Fairy Tales
- Publisher: Bantam
- Publication date as stated: Nov 1997
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, KING, SERVANT, PRIME MINISTER, GIRL #301, BLUE FAIRY, WITCH, GIRL
- Teaser before the introduction: Yes
- Spoken words (computed): 1068
- Already set (do not supply): none

### Source block (context only)

```text
Author: A.J. Jacobs
Book: Fractured Fairy Tales
ISBN: 978-0553099805
Publisher: Bantam
Date (Month/Year): Nov 1997
```

### Introduction (context only: never use it for content warnings)

```text
The Absentminded King by A.J. Jacobs
```

### Performance text (classify this)

```text
NARRATOR: (Pg 117-124) Once upon a time there was a king who was so good at his job, he was fit to be a king. Not only was he handsome and brave, but he had paid out the mortgage on his castle. And his carriage wasn't only beautiful, it also got good mileage. He even had a swimming pool shaped like a swimming pool. But for all this, he did have one little fault.

KING: (Shouting) Oh, honey, dearest!

SERVANT: Whom are you looking for, sire?

KING: My wife, the queen, that's whom!

SERVANT: But sire . . . you're not married.

NARRATOR: Yes, the king was so absentminded he couldn't seem to remember anything. He had even forgotten to marry. Knowing every king should have a queen, he discussed the matter with his prime minister.

KING: What shall I do?

PRIME MINISTER: First I suggest you put on your pants.

KING: Then what?

PRIME MINISTER: Find a wife.

NARRATOR: And so it was decided. The king put on his royal corduroys and called all the fair maidens to the castle so he could choose the most beautiful to be his bride. They came by the thousands.

KING: And who are you?

GIRL #301: I’m a beautiful but underpaid servant girl from the country.

KING: Good! Go out back to the stables and take care of the horses. I think they're due for a waxing.

GIRL #301: But I didn't come here to wax the horses. I came to see if you want to get married.

KING: What would I want to get married for?

NARRATOR: Alas, the absentminded king had completely forgotten why the young ladies had been sent before him. And though he did hire three maids, a dishwasher, and five cooks, he failed to select a bride. When reminded of this fact, the king was very sad.

KING: If I'm ever going to get a queen, I'm going to need some help.

NARRATOR: He took a wishbone from his pocket -- one that he had been saving for just such an emergency. He snapped it, and surprisingly, got the biggest half, and said his wish.

KING: (Screaming) Help!

NARRATOR: With that, some tiny bells tinkled, a thunderous crash sounded, and an applause sign lit up. There appeared a beautiful blue fairy.

BLUE FAIRY: I am a magic blue fairy and I can help you get a queen.

KING: I’m all ears.

NARRATOR: (aside -- The king could have been a body double in Dumbo.)

BLUE FAIRY: I know. But I can still help you get a queen.

NARRATOR: The fairy told the king that his queen lived in a castle on a mountain. But to get to her, the king first had to slay a terrible giant who guarded the castle. A tall order, to be sure-but not quite as hard as it sounded. The fairy gave the king a magic sword that would let him defeat the giant -- guaranteed, money back, minus shipping and handling. The king entered the woods and came face-to-face with the giant. Or actually face-to-knee with the giant. But in any case, the king was right next to the giant, and could have slain him on the spot, but for one thing: he had forgotten the magic sword. The giant picked the king up by the nose and tossed him over his shoulder. Luckily, however, when the giant threw him, he threw him nearer to the castle. So he actually passed the obstacle.

KING: Lucky for me. Okay. Now let's go get the princess.

BLUE FAIRY: Not so fast. Next you must pass through the huge, vicious thorn bush that surrounds the castle.

KING: Vicious thorn bush? There must be a catch.

BLUE FAIRY: As a matter of fact, there is. The secret is to be brave. The thorns will part to let a brave man pass.

NARRATOR: With that, the king steadied himself, and with all the speed he could muster, he ran headlong toward the vicious thorns. But also, true to form, he forgot to be brave. He chickened out. And that was not good for the king. He got ripped and scratched and poked. All his clothes were torn-except for his pants, of course, which he had forgotten to put on.

BLUE FAIRY: (Sighing) Oh, well. You did it again. But never mind. I'll just wave my magic wand and make those old vicious thorns disappear.

KING: Hey, why didn't you tell me could do that before?

BLUE FAIRY: You didn't ask me. (She waves her wand)

NARRATOR: And -- POOF! -- the thorn bushes disappeared. Now the king was really ready to go get his queen. But his troubles weren’t over yet. This being a fairy tale, he had yet another test. He had to do away with the wicked witch who guarded his love.

KING: Okay. What's the gimmick with the wicked witch?"

BLUE FAIRY: I will give you a magic word that will make her disappear.

KING: And that is . . . ?

BLUE FAIRY: Fundervogel!

KING: Wouldn't you know it. And me with the lousy memory.

NARRATOR: So, armed with the magic word, the king ran into the castle and found the wicked witch standing guard over his beautiful queen-to-be. Not expecting visitors, the witch hadn't had time to touch up her warts, so she was very unhappy to see the king. She decided to turn him into a toad and began to cast a spell.

WITCH: lggilty piggilty, my black hen . . .

KING: (Shouting) Wait! I have a magic word that will make you disappear. And it is ... uh . . . And it is . . .

WITCH: Get on with it.

KING: And it is . . . Fundervogel!

NARRATOR: It was a miracle. The king had remembered the word and the wicked witch disappeared in a cloud of green smoke. But so happy was the king that he had finally remembered something, he completely forgot about the girl. He ran out of the castle, whistling gleefully and clicking his heels. Weeks went by, and of course, the absentminded king wandered around the countryside and failed to return to his kingdom, for he was unable to remember which kingdom was his. He finally chanced to pass a lovely young girl from whom he asked directions. And when she put her dainty finger to her chin to think over the question, the king noticed a little string tied around her finger.

KING: Pardon me, I couldn't help noticing that little string tied around your finger. What's it for?"

GIRL: Why, to help remember.

KING: Remember what?

GIRL: I don't know . . . I forgot.

NARRATOR: The girl, you see, was as absentminded as the king, and needless to say that with such a common bond, they fell in love. And so it was that what's-his name married what's-her-name in a who's-its. And lived in a what-cha-ma-call-it happily ever . . . Oh, forget it.
```

---

## IC-1092: All 7 Deadly Sins Committed at a Church Bake Sale

- Title: All 7 Deadly Sins Committed at a Church Bake Sale
- Author (byline): The Onion Staff
- Work: The Norton Sampler: Short Essays for Composition, 6th Ed – Pg 101-05
- Publisher: W.W. Norton
- Publication date as stated: 2003
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, REPORTER, CONNIE BARRETT, BETTY WICKS, GEORGIA BRANDT, PENNY COX, JILLY BRANDON, BETH ELLEN COYLE
- Teaser before the introduction: Yes
- Spoken words (computed): 820
- Already set (do not supply): none

### Source block (context only)

```text
Author: The Onion Staff
Book: The Norton Sampler: Short Essays
for Composition, 6th Ed – Pg 101-05
ISBN: 978-0393978827
Publisher: W.W. Norton
Date (Month/Year): 2003
* Current Onion Headlines for the introduction can be found here
https://www.theonion.com/
```

### Introduction (context only: never use it for content warnings)

```text
No one is safe . . . Anywhere (Evil laughter) All Seven Deadly Sins Committed At a Church Bake Sale by The Onion Staff
```

### Performance text (classify this)

```text
NARRATOR: (Pg 101-105) The Onion is a satirical newspaper that originated in Madison, Wisconsin. In a typical issue, the paper pokes fun at everything from Politics . . . “Poll Finds Most Americans Would Swap Democracy for $100 Best Buy Gift Card” * (Original text reads “Bush Extremely Proud of New Suit”) to Entertainment . . . “NRA Accuses ‘Rust’ Producers of Endangering Crew by Not Giving Everyone Guns” * (Original text reads American lifestyles “TV Helps Build Valuable Looking Skills”) from The Environment . . . “Climate Summit sets Ambitious Goal to Phase Out Fossil Fuels by the Time the Earth Runs Out of Them.” * (Original text reads Medicine “Colonoscopy Offers Non-Fantastic Voyage through Human Body”) to Religion, which is what this selection is about . . . Sort of . . . [See] According to the Catholic Church, there are basically two types of sins. “Venial” ones that are easily forgiven and “deadly” ones that well, are not. Pride, Envy, Wrath, Sloth, Avarice (or Greed), Gluttony and Lust -- The Seven Deadlies . . .

And now reporting to you live from Gadsden, Alabama . . .

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

## IC-1093: All I Really Need to Know I Learned in

- Title: All I Really Need to Know I Learned in
- Author (byline): Not specified
- Work: Not specified
- Publisher: Dramatic Publishing
- Publication date as stated: Jan 1999
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, TEACHER, NORMAN, TEACHERS, CROWD, AUDIENCE MEMBER
- Teaser before the introduction: Yes
- Spoken words (computed): 889
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
Welcome to Kindergarten! Today is an exciting day – it’s a day devoted to Fairy Tales. And there isn’t a better fairy tale than Cinderella! (stage whisper) Just remember . . . everything you need to know is in there somewhere.

All I Really Need to Know I Learned in Kindergarten adapted by Ernest Zulia and David Caldwell based on books by Robert Fulghum
```

### Performance text (classify this)

```text
Kindergarten - Cinderella Adapted by Ernest Zulia and David Caldwell Based on books by Robert Fulghum

NARRATOR: (Pg 5-6) Share. Play fair. Don’t hit people. Don’t take things that don’t belong to you. If you hurt someone, say you’re sorry. Hold hands and stick together when you cross the street. Live a balanced life – learn some, think some, work and play. And sing and dance and draw. Take a nap each day. (Pg 7) Everything you need to know is in there somewhere. (Pg 8) If we all stopped to take a nap each day, how much better our world would be? And it’s still true, when we go out into the world in these uncertain times, it doesn’t matter if you’re six years old or sixty – we should all hold hands and stick together.

NARRATOR: (Pg 9-15) Cinderella was the title on the chalkboard marquee. Given the task of dramatizing a fairy tale for a teacher’s conference, the kindergarten class decided on the classic old rags-to-riches story, “Cinderella.” You know how it goes: “Shy agreeable protagonist, victimized by abusive step-parent, waits for wise matriarchal figure to rescue here, and deliver her transformed from co-dependency to bliss.” In other words; if you’re good-looking, good at heart and have a fairy godmother . . . you got it made.

It was a good choice from the teacher’s point of view, because there were so many characters and every child in the class could be in the play. There was the absolutely ravishing Cinderella. The evil stepmother. The two wicked but stupid stepsisters. The beautiful and wise fairy godmother. The pumpkin, mice, coachmen, horses, king. All the people at the King’s ball. And of course, (strikes a cocky pose) the Prince.

The children were allowed to choose roles for themselves. Finally, every child had a part. Except one. One small boy. Who had remained quiet and disengaged from the selection process. Norman. A kid who was somehow different – not weird, just different – in the way he/she looked at things. Norman was always thinking. And like so many misunderstood, but great thinkers, Norman was teased a lot by his classmates, causing him to live on the fringe of kindergarten society. (during these lines the actor transforms into Norman a deeply earnest and serious individual)

TEACHER: Well, Norman what are you going to be?

NORMAN: Well, I am going to be the pig.

TEACHER: Pig? There is no pig in the story of Cinderella.

NORMAN: (after a long pause, matter-of-factly) Well . . . There is now.

NARRATOR: Norman did not relate to being a footman or a mouse of a pumpkin. He knew his character. Pig. And he intended to participate wherever pigs fit into the scheme of things. Without giving up dignity or identity. He took it for granted that there was a place for pigs, and that the teacher would know that.

What do you say to a kid who is already thinking up a costume of pink long underwear, pipe-cleaner tail, and a paper cup for a nose? (knowing this is the real question) And what do you say to all the pigs? All those who are different and who do not accept the available boxes and pigeonholes? What did the teacher say? Well, sometimes teacher talk more like fairy godmothers!

TEACHER: (thinking very hard, then waiving her own invisible magic wand) So be it!

NARRATOR: And since there was nothing in the script explaining what the pig was supposed to do, the action was left up to Norman. Norman gave himself one of the all-time best walk-on parts in the history of children’s theatre. He decided he was Cinderella’s “personal pig”

(pause) Where she went . . . he went. He made no sound. He simply sat on his back haunches and observed. The expressions on his face reflected the details of the dramatic action. Worried (respond with intense facial expressions for each emotion) Sad . . . Hopeful . . . Puzzled . . . Mad . . . as the moment required.

There was no doubt what was going on, and no doubt that it was important. One look at the pig and you know. The pig was so earnest. So sincere. So very . . . “there.” Norman created such dramatic tension that people who knew how this story was supposed to end began to have doubts. When the Prince finally placed the glass slipper on Cinderella’s foot and the ecstatic couple rode off to live happily ever after, Norman finally made his move.

NORMAN: (Explodes into a spontaneous dance of joy with reckless abandon)

NARRATOR: He went wild with joy, dancing around the stage on his back feet . . .

NORMAN: (barks wildly, ending with a long howl) (when he stops, pause, then)

NARRATOR: . . . and barking like a dog??

TEACHER: (to Norman) Even if there was a pig in the Cinderella story, there is no such thing as a dancing, barking pig.

NORMAN: (matter-of-factly) Well, there is now. (He holds his ground as the teacher contemplates this statement)

TEACHER: (considers Norman with respect) It’s true, Norman, it’s true . . . Knock ‘em dead, pig!

NARRATOR: The presentation at the teachers’ conference was a smash hit!

NORMAN: (dances in slow motion)

NARRATOR: When Norman danced his dance, the crowd of weary teachers laughed . . . and wept . . . and cheered

TEACHERS: (cheer)

NARRATOR: And later when the pig stumbled out for his curtain call.

NORMAN: (crosses for his bow)

CROWD: (chanting) NORMAN . . NORMAN . . . NORMAN!

NARRATOR: The teachers were able to see that the real Cinderella was not the little girl with the button nose and blonde hair . . . but Norman, the dancing, barking pig. And they knew the real fairy godmother was not the child waiving her fairy wand, but the teacher, standing weeping in the wings. (beat) Kindergarten teachers know magic when they see it.

(as an epilogue) Well, the kindergarten class had many invitations to perform their highly acclaimed production of “Cinderella.” Sometimes the teacher would have to explain what it was about the performance that was so unique.

TEACHER: It has a pig in it, you see . . . the star of the show is a dancing, barking pig.

AUDIENCE MEMBER: But there is no dancing, barking pig in “Cinderella.”

NARRATOR: Well, there is now! (Break into Norman’s unique dance and end with a bark and howl)
```

---

## IC-1094: And So They Did

- Title: And So They Did
- Author (byline): V. McQuin
- Work: Newfangled Fairy Tales, Book #1
- Publisher: Meadowbrook Press
- Publication date as stated: Jan 1998
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1622
- Already set (do not supply): none

### Source block (context only)

```text
Author: V. McQuin
Book: Newfangled Fairy Tales, Book #1
ISBN: 0881662992
Publisher: Meadowbrook Press
Date(Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
Now, finally, at last - those old fairy tales have been exposed for the drivel they are! Did you ever stop to think that Sleeping Beauty might have been neutralized because she was a miserable young woman? Or that Goldilocks wore red because her mother got a great deal on a bolt of red cloth? Or even that those dragon fights were rigged?

Okay, I still love fairy tales, but you realize that the Grimm Brothers and the other famous story tellers wrote stories with plots that would never hold up today.

V McQuin tells it the way it really was - before those interfering writers went and changed the stories to be politically correct. And So They Did by V. McQuin
```

### Performance text (classify this)

```text
Narrator: Once upon a time a queen had triplets.

King: Three! Three?

Midwife: Three.

Narrator: And so there were.

King: Boys?

Midwife: Girls.

Narrator: And so they were. The queen named them April, May, and June.

Narrator: As the years passed, the three little princesses grew into beautiful young women. One day the king said,

King: It is time for you to think of marrying. And wedding gowns, and wedding feasts, and wedding balls. Not to mention princes. And there is the problem. You see, there is a slight shortage of princes this year.

Princesses: A shortage of princes?

King: I'm afraid so. There were some very fine princes, but it appears they've all been taken. One was swept up by a cleaning girl!

Princesses: A cleaning girl?

King: A cleaning girl, named Cinder-something-or-other. Very nice and a hard worker, too. They said she only had rags to wear. Except for a pair of glass slippers. But she took the prince anyway. Another prince found some enchanted castle. Those are rather rare these days, but you do still find one every now and again. Seems everyone had been asleep for years, including the king's daughter, a real beauty. Without even knowing the girl the prince fell in love. Woke her with a kiss.

Princesses: A kiss! A kiss?

King: You know magic spells. If you can't think of anything else to break them, a kiss will usually do the trick. Anyway, that prince was married before everyone could finish yawning. Another prince fell helplessly in love with a dead girl.

Princesses: With a dead girl? How frightful!

King: She wasn't really dead. Another magic spell, you see. Her stepmother was a real witch. She couldn't stand the poor girl and put a curse on her. Everyone thought she was dead. She was so beautiful they kept her in a glass coffin. Good thing, too. The prince wandered by and fell in love. A kiss did the trick again. One more prince taken. Lovely for them, but you see it creates a problem for us.

Princesses: It's a problem, all right.

Narrator: Princess April stood up.

April: I will go and find a prince myself!

King: Find a prince yourself? Unheard of! Quite improper.

April: I'm sure I can! If a cleaning girl can find a prince, how hard can it be?

King: Well… I've heard a prince or two might be left in the northern countries. You could try there, I suppose.

April: I will leave at once.

Narrator: And so she did.

King: What of you, May? Will you seek out your prince, too?

May: I hope you and mother won't mind terribly, but I'd really rather not find a prince at all.

King: Not at all? Unthinkable! Have you lost your mind?

May: Not at all. I've never much liked being a princess. I'd prefer to be an ordinary sort of person and work in the gardens.

King: Well… I suppose two princesses are enough for any castle.

May: And there's a nice young man who works in the garden. I believe he would marry me if you said he could.

Narrator: And so they did.

King: Well, then, June, what of you?

June: Oh, I think I'll put an ad in the paper.

King: An ad! In the paper?

June: I'm quite happy being a princess, but I don't want the hassle of searching for a prince. Therefore, I shall put an ad in the Castle Times. The ad will read: "Wanted: A prince to marry. Preferably handsome and rich. Must be wise and kind. Apply in person to Princess June."

King: Well… it's worth a try. Perhaps.

June: Sooner or later, a nice prince will answer my ad. Until then, I'm quite content to wait.

King: Very well, write your ad.

Narrator: And so she did. It was not long before Princess April returned to the castle with a charming prince.

King: Now, then, April, tell us how you found this fellow.

April: It wasn't easy, Father. I traveled north until I reached a castle. A queen and her son lived in it, but they wouldn't even talk about marriage. "Spend the night and we'll talk in the morning," the queen said. The room was nice enough, but oh, the bed! I needed a ladder to climb into it. And was it ever lumpy! I couldn't sleep a bit. I figured that since I was awake, and the prince didn't seem very eager to marry me, I might as well move on. So I did. Of course, it was terribly dark out. I could not see a thing. I ran right into the side of another castle. When I rang the bell, a horrid beast came to the door!

King: A beast! A horrid beast? Shocking.

April: It was dreadful. You can be sure I didn't stick around to find a prince there! I ran away as quickly as I could in the dark. Suddenly I splashed right into a smelly pond. A poor frog talked to me. Or at least he tried. He had a raspy voice-hard to understand. I was tired, frightened, and soaked-I didn't have time to listen to a croaky old frog.

King: That may have been a good time to try a kiss.

April: A kiss! Hmmm… I never thought to kiss a frog!

Queen: Not to worry, my dear. You've a prince now. Do tell us how you got him.

April: Oh yes. In the morning, I wandered farther north. The snow was very deep. I was freezing, not to mention tired and hungry. I had almost decided to go home and let my prince find me. Then I saw him! He was so tall, so handsome, and so marvelous that I almost didn't know he was made of ice!

King: Of ice! He was made of ice?

April: Indeed! He was enchanted, of course. By a wicked stepmother. You know how it is.

King: And you thawed him out?

April: A kiss did the trick, just as you said. As soon as he stopped dripping, we hurried here to be married.

Queen: Everything is almost ready for the wedding. While you were away, we worked day and night to prepare your wedding feast, ball, and gowns.

April: Gowns?

King: May has arranged to marry a young man who works in the gardens.

April: In the gardens! May is marrying a gardener?

King: Of course, he isn't just a gardener. He's a prince as well. Wicked stepfather, curses, and all that. A kiss did the trick once more. We can have a triple wedding as soon as a suitable prince answers June's ad.

April: Ad! June has placed an ad for a prince?

Narrator: Just then, the bell rang.

King: Lower the drawbridge!

Narrator: Princess June opened the door. She saw no one. Just as she turned to go back inside, she heard a very small laugh.

June: Hello?

Tom Thumb: Ha! Tricked you, didn't I?

Narrator: A very small man popped out of a crack between the paving stones. He was riding a mouse. Tom Thumb at your service. I'm here about the ad. May I speak to Princess June, please?

June: Why… I am Princess June, but I'm afraid you are not quite what I was hoping for. You're much too small, and… I… well, I'm afraid of mice. I'm sorry, but you just won't do.

Tom Thumb: Oh well, it was worth a try. I guess I'll be off. Good day!

Narrator: Tom Thumb hopped into his saddle and spurred the mouse away.

King: Well?

June: It was a very odd little man, only as big as your thumb, His horse was a mouse! I doubt he's really a prince. Oh, there's the bell again. Perhaps this will be my prince.

Narrator: The drawbridge was lowered again. Princess June opened the door-and slammed it shut.

King: Well?

Queen: A kiss wouldn't help?

June: Absolutely not! The ad must have gotten into the Jungle Times by mistake. It was a lion.

King: A lion! Beastly! I knew that ad was a mistake.

June: Perhaps you're right. But the lion's gone now. And look, someone else is coming.

King: A man, I hope! A tall and handsome man. Please!

Narrator: Princess June opened the door. The man was indeed tall and handsome. But he was not a prince.

Handsome Man: I understand you are looking for a new gardener.

June: Actually, I'm looking for a prince to marry me.

Narrator: The man was not a prince, but he was charming, kind, and wise.

Handsome Man: Well, now, you are a very beautiful princess. I would be delighted to marry you. Although I am not a prince now, I would be if I married a princess. Marry me and you shall have your prince.

Narrator: From behind the door, the king, queen, servants, and other princesses said,

King, Queen, Servants, April, May: Take him!

Narrator: And so she did. The next day, the castle was full of flowers and wedding guests. The three princesses were full of happiness; the king and queen were full of pride; the servants were full of relief. It was a marvelous wedding. The three princesses were stunning in their wedding gowns of silk, lace, beads, and jewels. The three princes were dashing in their wedding suits. The feast was delicious. No one went hungry in all the land that day. The dance could not have been better, even though someone dropped a glass slipper. It was a glorious day. As the newlyweds kissed, everyone was certain the three princesses and their princes would live happily ever after. And so they did.
```

---

## IC-1095: And Thy Name Shall Be . . . Something

- Title: And Thy Name Shall Be . . . Something
- Author (byline): Paul Reiser
- Work: Babyhood
- Publisher: Avon
- Publication date as stated: Aug 1998
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1578
- Already set (do not supply): none

### Source block (context only)

```text
Author: Paul Reiser
Book: Babyhood
ISBN: 978-0380728725
Publisher: Avon
Date (Month/Year): Aug 1998
```

### Introduction (context only: never use it for content warnings)

```text
And Thy Name Shall Be . . . Something by Paul Reiser
```

### Performance text (classify this)

```text
Naming your child is a monumental responsibility. You get to tag and identify – for life – a whole new person. Throughout your child’s life, it will come up every hour of every day.

“Name, please.”

“Hi, what’s your name?”

“Sorry, I didn’t catch your name.”

“We just need you to sign your name.”

“Would you put last name first, first name last, middle initial . . . “

“May I ask who’s calling?

“Name and Social Security number . . . “

And with every usage, that name – the result of hours and hours of debate, and the consideration of an infinite number of variables, uninvited input, and conflicting personal agendas – that name will, for good or bad, represent to the world and its people, for all eternity, your child.

Which is why you don’t want to screw it up.

People screw up their kids’ names all the time. Not on purpose. In fact, usually with the best of intentions. The new parents who want their child to stand out and be recognized, who want more than anything to thrust their child forward from a sea of common and interchangeable surnames, are the ones responsible for kindergartens full of Zebadiahs, Queequegs, and Moons. Lovely and creative names all. Unfortunately, these kids are in for a lifetime of quizzical stares, judgmental smirks, and patronizing displays of phony interest, in response to which they can only say, “Yeah, my parents were into a thing . . . “

The power is extraordinary. The simple combination of letters and sounds you select can result in a life of carefree coolness or decades of expensive therapy.

“Hi, I’m Jake” versus “Hi, I’m . . . . Tapioca.”

Not to denigrate the virtues of being unique. It’s just that there’s a fine line between Good Unique and Just Plain Wrong. Good Unique is when you call your child’s name and he’s the only one who comes running. Just Plain Wrong is when they’re running because they’re being chased.

I imagine that part of the reasons there are so many Bobs and Janes year after year is that even parents who want to be creative ultimately chicken out. And understandably. You never know when the name you love today is going to be hideous tomorrow. The Ashleys, Dylans, and Maxes of our children could turn out to be what Hortense, Gertrude, and frankly, Max were when we were growing up. It’s sort of like the jacket you wore in your high school yearbook photo; it may have been cutting-edge that week, but for the rest of your life, you’re “the maroon-plaid-jacket guy with lapels the size of sea flags.”

All I know is that if you name your daughter Trixie or Tina, she’s more likely to sleep in a van with a band from Seattle than the exact same girl names Ruth. Similarly, a boy named Herbert may grow up to play baseball professionally, but not as easily as Dale, Pee Wee, or Scooter. This, of course is not scientifically documented or anything, but . . . I think I know what I’m talking about.

A lot of people tell you that their kid popped into the world and the name just revealed itself.

“He looks like an ‘Elliot.’ Let’s call him ‘Elliot.’”

Com on – nobody seven minutes old looks like “Elliot.” It takes years to look like “Elliot.” If they’re like most newborns, your precious new one will enter this world looking like one of three things: Winston Churchill, Mahatma Gandhi, or a boiled chicken. That’s basically it. (It is possible for a baby to look like Churchill or Gandhi and a boiled chicken, but this usually goes away with time and plenty of fluids.)

In some cultures they don’t even name their babies right away. They wait until they see how the child develops; see what they do, see how they behave . . . and then name the kid accordingly. Like in Dances with Wolves. If you stand with your fists clenched, you’re called Stands with a Fist. I like that system. It certainly makes it easy to remember people you’ve met.

“How’s that guy doing?”

“What guy?”

“You know . . . what’s-his-name, the guy who’s always yelling at the vegetables . . . “

“Oh, you mean Barks at Salad?”

“Yes, yes, Barks at Salad . . . how’s he doing? . . . “

Unfortunately, in our world, kids’ names would be less romantic and poetic. Certainly less warrior-like.

“This is y oldest boy, Falls Off His Tricycle, his friend, Dribbles His Juice, and my beautiful daughter, Allergic to Nuts.”

Some people don’t agonize at all about finding the perfect name. They simply give the kid their name.

“He’ll be me, but Me Junior. To be followed by Me the Third, and his son, Me the Fourth.”

Certainly moves things along. Of course, if you’re really pressed for time, do what heavyweight champ George Foreman did - - name all of his kids George Foreman. God bless him, a great fighter, a fine humanitarian – not, apparently, the most creative in the naming department. An entire family named George Foreman. It’s not like they’re of successive generations, overlapping only here and there for a few years . . No, this is almost half a dozen guys, with the exact same name, all living in the same house.

For others, the task of naming is simplified by family mandates. “The child will be named after his grandfather.” Or, “She will take her mother’s surname, and it shall be as her own . . . And they shall go forth unto themselves, with their beasts and their grains, and into the desert shall they sojourn.” (I’m sorry, I just saw The Ten Commandments on TV and frankly, I enjoy talking like that.)

In our case, we knew we wanted to name our child after my father. We didn’t want to use the exact same name, but something beginning with the same letter. We had plenty of girls’ names we liked, but nothing for a boy. Of course, when our son came out a boy (as almost all sons do) we were stuck. So we decided instead to honor my father’s name by making it our son’s middle name. Middle names are kind of like vice presidents: It’s a fine distinction and certainly an honor, but you’re never not aware that someone else got the real job.

Parents often give middle names just so that later, when they’re yelling at the kid, they can drag it out.

“Henry David Thoreau, you come in here this instant!” It gives them something extra to sink their teeth into.

If, however, you assassinate someone, your middle name is all over the place. Once you shoot a famous person, not only do you go to jail and sit alone hungering for a forgiveness that eludes you your whole life, but on top of that, your middle name, whether you like it or not, gets publicly and permanently cemented right between your first and last name. They just run those puppies together like Sonny-and-Cher. There’s no way you can undo something like that.

But because of the potential anonymity enjoyed by middle names, they also represent opportunities for Name Givers to safely store their really creative choices. So when you meet kids named Stanly DiMaggio Miller or Carol Satchmo Smith, you know their parents had healthy doses of not only creative sparks but discretion, too.

The moment you announce your child’s name, people take it in for a moment, digest it, and then say, “Okay, but what are you going to call him?”

“What do you mean, what are we going to call him? His name.”

“No, of course, but what’s the nickname going to be? I mean Franklin is a beautiful name, but what do we call him? Frank? Frankie? Frankle? Frankfurter?”

This was a setback I hadn’t seen coming. After finally landing on a name the two of you like, your family tells you it’s not enough. You have to come up with a menu of officially sanctioned deviations and nicknames, which they’re going to disregard anyway.

“Hello, Snooky . . . Hello, Angel-puss . . . Who’s my sweet Pumpkin?”

They get called a lot of foods, these babies. “Pumpkin,” “Angel Cake,” “Cupcake,” “Honey,” Sweet Pea,” “Puddin’ . . . ”

But not all foods. You never hear someone call an infant “Steak.” “Chicken Parmigiana.” “Eggs.”

I think the rule of thumb is, desserts and side dishes are okay, entrees and appetizers, not okay. The only exceptions that I’m aware of are my Aunt Cutlet and Uncle Bisque, who were actually born with those names but, ironically, were later nicknamed Phyllis and Lloyd.

So we bought every book out there on baby names, because when you’re not by nature good with decisions, what could be more pleasant than slugging through the list of every name registered in every town on the globe? While it is nice to learn about other peoples, I’m not sure that any one family needs that many choices. You’re probably going to stay within a given range. Very few people end up deciding, “Okay, so Achmanzlebred if it’s a girl, and if it’s a boy – Scott.”

You do, however, get to learn the etymology and origin of names, which is useful for parents trying to boost the self-esteem of kids stuck with loser names.

“Sweetheart, you know Milton actually means ‘Ferocious Fighter of Freedom’ . . . “

Of course, some names you can eliminate pretty comfortable.

“Adolf?” -- “Out”

“Medusa? – “Out”

Yup . . . Naming your child is a monumental responsibility. You get to tag and identify – for life – a whole new person. Throughout your child’s life, it will come up every hour of every day.

“Name, please.”

“Hi, what’s your name?”

That name will, for good or bad, represent to the world and its people, for all eternity, your child - Which is why you don’t want to screw it up.

Thanks to mom and dad for my name: (INSERT FULL NAME HERE)
```

---

## IC-1096: Ant Farm: And Other Desperate Situations

- Title: Ant Farm: And Other Desperate Situations
- Author (byline): Simon Rich
- Work: Not specified
- Publisher: Random House Trade Paperbacks
- Publication date as stated: April 2007
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: JUDGE, CRIMINAL, VICTIM, ME, JAKE, UNICEF, SERVANT, TEACHER, TEACHER 2, TEACHER 3, CHILD 1, CHILD 2, MR. BENDER, JONATHAN, SEYMOUR, SETH
- Teaser before the introduction: Yes
- Spoken words (computed): 1719
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
Let’s face it . . . no matter how many times teachers and parents tell you that school is preparing you for “real life” . . . School is nothing like real life. But just to prove my point, I’d like to take you for a walk down memory lane, compliments of Simon Rich in this selection –

Ant Farm and Other Desperate Situations
```

### Performance text (classify this)

```text
Announce the title of each “scene” in a broad announcer’s voice IF LIFE WERE LIKE MIDDLE SCHOOL (Pg 25)

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

## IC-1097: Are We There Yet?

- Title: Are We There Yet?
- Author (byline): Andy Griffiths
- Work: Just Annoying!
- Publisher: Scholastic
- Publication date as stated: Dec 2003
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: ANDY, DAD, MUM, BIKE MAN, MAX
- Teaser before the introduction: Yes
- Spoken words (computed): 1975
- Already set (do not supply): none

### Source block (context only)

```text
Author: Andy Griffiths
Book: Just Annoying!
ISBN: 978-0439424714
Publisher: Scholastic
Date (Month/Year): Dec 2003
```

### Introduction (context only: never use it for content warnings)

```text
Parents, everywhere, I get it. You love your children, but getting into a car with them is like stepping through the gates of hell. Something about a moving vehicle causes them to do and say the most infuriating things, and because you're behind the wheel, you're powerless to stop it.

I remember those long road trips and from a kid standpoint, they really are BORING! But not this one . . . Are We There Yet? By Andy Griffiths
```

### Performance text (classify this)

```text
ANDY: Dad? DAD: Yes?

ANDY: Are we there yet? DAD: No.

ANDY: Now? DAD: No.

ANDY: Now? DAD: For goodness sakes! Will you stop it!

ANDY: Alright. Don’t get your knickers in a knot.

ANDY: We’ve been in the car for two days now. Mum and Dad are at a breaking point. Don’t get me wrong. I don’t want them to get mad at me – it just happens. Like it or not, when you go on a long drive there are times when you just have to stop. And my parents do not like it. But what’s the alternative? Do they want me to starve to death? To wet my pants? To be sick all over the back seat? I think any of these would be a lot more annoying and inconvenient than the few stops it takes to prevent them. I’m actually doing them a favour.

Mum and Dad should save their energy for really annoying things. Like the fly that has been buzzing around in the car for the last half hour. It’s driving me mental. I’m going to do us all a big favour. I’m going to get rid of it.

I wind the window down. The fly jumps away. It’s hiding, just waiting for me to wind the window back up again. I have to lure it out. I start doing my best fly-call. Bzzzz! Bzzzzzzzz! Bzzzzzzzzzz!

Still no fly. Have to do it louder: BZZZZ! BZZZZZZZ! BZZZZZZZZ!

DAD: Andy! I can’t concentrate with you making that stupid noise. Do you want us to have an accident? Do you want us all to be killed?

ANDY: I hate it when Dad asks dumb questions like that. What does he expect me to say? ‘Yes, Dad, I want us to have an accident. I want us all to be killed.’ But I don’t say that. Instead I say: Alright, Dad. Don’t get your knickers in a knot.

DAD: (Exploding) And stop telling me not to get my knickers in a knot!

ANDY: Okay, Don’t get your trousers in a twist. Dad hunches over the steering wheel. His knuckles whiten. Tiny drops of perspiration appear on the back of his neck. He knows he’s been outsmarted once again. It must be frustrating for him having a [child] as clever as me. It must be hard knowing he can never win.

The fly lazily cruises in front of my eyes. It’s asking for trouble. Well, it’s come to the right [place]. I once saw a movie where the door of an aeroplane opened mid-air and everybody was sucked out by the vacuum it created. I don’t need a vacuum quite that powerful, but maybe if I open and close the door I’ll be able to create on strong enough to suck the fly out. I squeeze the door handle as carefully and slowly as I can so that it doesn’t make any noise. I swing it open, then shut. Open, shut. Open, shut

DAD: (Screams) What do you think you’re doing?

ANDY: I’m creating a vacuum.. I’m trying to get a fly out of the car.

DAD: (Shouting) Shut the door! And keep it shut! I’m warning you.. If you don’t behave yourself, I’ll stop the car and you can get out and walk. Do you understand?

ANDY: But, Dad

DAD: No buts! Do you understand?

ANDY: Dad’s knuckles are really white now. He’s gripping the steering wheel so hard that his bones are practically breaking through his skin.

I hear a buzz. It’s coming from behind me. The vacuum didn’t work. I turn around but I can’t see the fly. Hang on – the noise is coming from outside. I undo my seatbelt and kneel up on the seat to get a better view. There’s this crazy-looking guy riding an old black Harley.

He’s got a long red beard, a black bowl-shaped helmet and a pair of old-fashioned plastic riding goggles. They make him look like a fly. And his motorbike sounds like one. Only much louder.

Suddenly the fly shoots across the window. Showdown time! I try to cup it in my left hand and hook it out of the window. That’s my plan, anyway. But the fly has other ideas. It skates across the window to the far corner. And then back again. I’m chasing the fly back and forth across the window when I notice that the bikie is making hand signals. He thinks I’m waving to him! I wave. He waves back. I wave again. We’re best friends now.

DAD: Stop waving. Sit down and put your seatbelt back on.

ANDY: But he waved first.

DAD: Sit down!

ANDY: Okay, okay, don’t get your knickers in a knot. I give one last wave to Bike-man, but he’s pulling into a service station and doesn’t see me. I feel like I’ve lost my best friend. I notice a movement out of the corner of my eye. I look up. The fly is on the roof. It’s taunting me. It buzzes again. I have to get rid of this fly. And quickly. Before it gets rid of me. I reach up and try to cup it with my hand. It jumps to the left. I try again. It jumps to the right and then heads towards the front, daring me to come after it. I unbuckle my seatbelt and dive into the front seat. I catch the fly in mid-air. (yelling) HOWZAT! I’m lying with my head in Mum’s lap and my legs all over the steering wheel. Dad slams the brakes on.

DAD: Get out!

ANDY: But it’s not my fault. It was the fly.

DAD: I don’t care whose fault it was. Out!

ANDY: Surely he can’t be serious. I’m sorry, Dad . . . I was just trying to get the fly out of the car . . . in case it caused an accident.

DAD: You’re the only one who is going to cause an accident. Out.

ANDY: Mum? Are you going to let him do this?

MUM: It’s for your own good. You’ve got to learn.

ANDY: I open the door. You’ll be sorry when you come back and find my bones being picked clean by vultures.

DAD: Shut the door. You’re letting the hot air in.

ANDY: There’s no reasoning with him. I get out of the car and shut the door slowly. The wheels of the car spin. I am showered by gravel. I wipe the grit out of my eyes and look for the car. It’s gone. They’ll be back. Any second. Five minutes tops. Just enough to give me a scare. I start walking. Actually, it’s quite nice. Fresh air. Blue sky. Space. No grumpy parents.

Five minutes pass. Another five minutes. And another five minutes. Where are they? I should just lie down and die – that would teach them. The only trouble is that it could take a while because I’m actually feeling pretty healthy. I hear a droning sound in the distance. Ha! I check my watch. It took them fifteen minutes to give in and come back and get me. That’s really going to teach me a lesson I’ll never forget. NOT.

But as I listen, I notice the drone has a different quality. Not the putty-putt-putt sound of Dad’s car at all. It’s Bike-man! I jump up and wave. He waves back and pulls up alongside me. He looks even crazier close up. His beard is full of insects. Some of them are still alive.

BIKE MAN: Well, if it isn’t my little mate. What are you doing out here all by yourself?

ANDY: My parents threw me out of the car. They told me I had to walk.

BIKE MAN: Max. (Shaking Andy’s hand) Hop on then.

ANDY: He hands me a helmet. It’s just like the one he’s wearing. My stomach drops as he accelerates up the road. I grab him around the waist. Roaring wind My whole body shaking and vibrating. I’m freezing. I see Mum and Dad’s car in the distance. (yelling) That’s them) As we pull closer to the car, I signal Max to blow his horn to let them know I’m here. He blasts. I wave. But they don’t stop. If anything they seem to speed up.

Max! Go up next to them. I don’t think they realize it’s me. I wave. Hey, Stop! No reaction. I wave both h ands. Dad flicks a nervous glance across at me, but he doesn’t show any sign of recognition. Instead he hunches over the wheel and pulls away from us at high speed. WOW! I never knew the car could go so fast.

Max accepts the challenge. He speeds up. We’re back beside them.

MAX: They’re not going to stop! You’re going to have to board ‘em.

ANDY: He’s joking. He’s got to be. Either that or he’s completely insane. He rides right up beside the car and signals for me to stand. I kneel on the seat. I hold on to Max’s shoulders and pull myself up. My legs are shaking. Max edges in as close as he dares. My stomach is churning. I don’t want to do this. I’m too young to die! I can’t do it. Why can’t I stay with you/ I’ll be your apprentice.

MAX: (laughing) Highway’s no place for a nice kid like you. Go back. Finish school

ANDY: I’m not nice. I’m really annoying. He has a wild look in his eyes. Maybe staying here is not such a great idea after all. I stand up again. I take a deep breath. I close my eyes. Clench my fists. Goodbye cruel world! The wind picks me up and sends me hurtling sideways. Thump! I land on the car roof. I made it! Dad s tarts swerving all over the road. He’s trying to shake me off. I’ve got to make him realize it’s me. I bang on the roof. Dad swerves harder. If I can just let him see it’s me he’ll slow down. I push myself down in front of the windscreen. Mum and Dad freak. Eyes wide. Mouths open. The car stops. It’s over. Mum and Dad get out. I take off my helmet.

DAD: This is the limit! The absolute limit! What are you trying to do – get yourself killed?

ANDY: More dumb questions. No, I was trying to get back into the car. You threw me out, remember?

DAD: Yes, to teach you a lesson

ANDY: What sort of lesson is that? To abandon me in the middle of nowhere with no food, no drink, no map and no sunscreen.

MUM: We were going to come back.

ANDY: When? On your way home?

DAD: We were about to come back and get you when the biker started chasing us. I was trying to lead him as far away from you as possible. Some of these characters can be pretty dangerous, you know.

ANDY: I get into the car. I don’t want to hear any more excuses, Dad. You tried to get rid of me. You failed. Let’s go.

He starts the engine. He’s feeling bad now. He should be. We pull out onto the road. [Then] I see the fly. It’s sitting right on top of Dad’s head.

(quietly) It’s all your fault. I’ve been abandoned Almost missed out on my holiday. Risked my life. It’s all your fault – and you’re going to pay.

I sit up close behind dad. I hold my hands just above his head, ready to smash the fly. It jumps. The movement distracts me. I clap Dad over both ears instead. Oops! Dad, I’m sorry – it was a mistake. See, I was trying to . . .

DAD: It’s okay. You don’t have to explain. We all make mistakes.

ANDY: Oh, I get it. Mum and Dad won’t try to put me out of the car again. No matter what I do. They’ve used their biggest threat and it didn’t work. It just made them feel bad. I can do anything now. Anything I want. This might not turn out to be such a boring trip after all. I just have one question . . . Dad . . . Are we there yet?
```

---

## IC-1098: Around the World in a Bad Mood!

- Title: Around the World in a Bad Mood!
- Author (byline): Rene Foss
- Work: Not specified
- Publisher: Hyperion Press
- Publication date as stated: March 2002
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: FA, WIRT, CAPTAIN, NEW FA, PASSENGER, NEW FLIGHT ATTENDANT
- Teaser before the introduction: Yes
- Spoken words (computed): 1496
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
Around the World in a Bad Mood! Confessions of a Flight Attendant by Rene Foss
```

### Performance text (classify this)

```text
NOTE: Words appearing in [ ] are added as transitional items.

FLIGHT ATTENDANT (FA): Good morning, ladies and gentlemen! In a few moments we'll begin the breakfast service in the main cabin. We have a wide selection of choices for you today. You may have any or all of the following items: Prozac, Zoloft, Viagra, Ecstasy, Ritalin, Cele-brex, or scrambled eggs. Some of these items may cause side effects, such as dry mouth, fatigue, internal bleeding, temporary blindness; and leprosy. Again, your choices include Prozac, Zoloft, Viagra, Ecstasy, Ritalin . . . oh, one moment please. My apologies, ladies and gentlemen, that is the flight attendants' breakfast menu!

(to audience) I am a flight attendant and the world is my oyster. And what an oyster it is! Oversold flights, weather delays, air traffic control delays, center seats, crappy food, air rage - it's so glamorous! Kind of like a Greyhound bus in the sky. This is just a glimpse into my life . . . a story about air travel, flight attendants, and me! So . . . fasten your seat belts, raise your tray table, and stow your bag . . . The journey is about to begin. Welcome to my nightmare!

*WIRT – What I’m Really Thinking

FA: Welcome aboard, sir, so glad you could join us today. You have seat 4B. Get you a gin and tonic? My pleasure.

WIRT: Pleasure, my a**. I'd rather watch paint dry.

FA: Here you go, sir. Oh, you couldn't find room for your carryon? You're tired of lifting it and you want someone to get it out of your way?

WIRT: And I guess I'm the lucky someone. I cannot believe my good fortune. Jesus, what has he got in here? A dead body? If this six-foot, 200-pound bruiser can't lift it, how does he possibly think I can lift it?

FA: You know, sir, I think this bag is a little big for the overhead. Perhaps I could check it to your final destination?

WIRT: Better yet, perhaps I could check you to your final destination and put the bag in your seat. The bag would probably be a lot more interesting.

FA: Unacceptable, you say?

WIRT: I'll tell you what's unacceptable: your personality! He probably thinks just because he's sitting in first class that he's entitled to be rude to everyone in the world. Well, I'm checking this bag, whether Mr. Congeniality likes it or not. (begins dragging it up the aisle)

FA: Oh, I didn't mean to disturb you . . . Yes, well, it looks like the only available option is to check it. It sort of exceeds the size requirements.

WIRT: A little bit like your ego, pal. Oh boy, he's getting up now. Well, that got him into action! Probably hasn't moved that fast in years. My, my, look at those muscles .... Amazing how he can heave that two-ton bag into the overhead. Just 2 minutes ago he didn't have the strength.

FA: Thanks so much for helping with your bag. I'm glad we didn't have to check it . . . My name?

WIRT: My name . . . what does he want my name for? It's not like we're going to be buddies. In fact, if things work out the way I am hoping we will never see each other again. So why on God's green earth does he need to know my name? He's probably going to write me up. (outraged) I'm just doing my job, risking my chiropractic good health trying to help this brute with his bag. And what do I get? This idiot requesting my name. Maybe I'll just make up a name . . .

FA: Oh no, you don't need to apologize. I'm sure you've had a hard day and having to tow that heavy bag of yours around has got to be tiring. . .

WIRT: I'll give you a hard day ... my day! Five stops between Chicago and Indianapolis, airplanes of people just like this jack***. And I've got to do the same thing tomorrow and the next day, too. What did I ever do to deserve this? God, I hate my life.

FA: Tonight? Well, I'm flattered. . . Oh yes, I'm sure there's a lot of great nightlife, but I really have to get to bed early tonight because I have to wake up at 7:00 A.M. Oh, aren't you funny, you won't take no for an answer . . .

WIRT: Oh, he's funny all right. Funny as a crutch.

FA: . . . . I guess as long as I'm back by a reasonable hour -- why not? I accept, sir. Charlie? OK, Charlie. I'm really looking forward to it.

WIRT: I'm looking forward to it about as much as I'm looking forward to paying my taxes or getting a root canal.

FA: I'll be right back! *******

FA: (to audience) And there you are . . . curled up in a little ball, sucking your thumb, on the verge of uncontrollable sobbing, when the captain makes an announcement:

CAPTAIN: Ladies and gentlemen, I have some bad news: It appears we will be here for at least another hour. Please let us know if there’s anything we can do to make you more comfortable. Thank you.” . . . .

FA: ARGGHHHH!! *********

NEW FA: TESTING, ONE-TWO-THREE . . . hello? Is this thing on? Oh, for Christ's sake OK. Welcome aboard We Apologize for This Inconvenience Airlines, also known as WAFTI. This flight is under the command of Captain Booze, assisted by First Officer Chance, and as we like to say here at WAFTI, if Booze and Chance can't get ya there . . . nothing can!

For your comfort we have four lavatories on this aircraft: one in first class and three in coach. However, only one is working, so pace yourself! The airphones are not working, we have only three pillows and two blankets. We do not have any magazines or newspapers, but we do have the pamphlet How to Deal with Anger in a Positive Non-violent Way. Today we will be passing these pamphlets out in lieu of the meals. We here at WAFTI appreciate your business and we want you to know that we're constantly upping our standards . . . So up yours!

Now it is time for the safety demonstration. This information could save your life so please
pay attention! It's time for the 'Safety Demo Shuffle.' (Attendant raps and moves to the
beat, the more awkward the better . . . with enthusiasm!)
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

*******

FA: Hello, can I get you a beverage?

PASSENGER: Yes, I'll have a can of tomato juice, a bottle of water, and two cups of coffee with cream and sugar.

FA: Are you ordering for the whole row?

PASSENGER: No, just for me . . . I'm kind of thirsty.

FA: Anything else?

PASSENGER: Yeah, now that you mention it, I'll have a can of apple juice for later.

FA: Airline food has been the butt of many jokes over the years. People make fun of its quality, color, taste (or lack thereof), but as soon as you take it away people miss it! People used to complain about the food choices we offered:

PASSENGER: All you have are three choices?! And all of them terrible! My God, what is the world coming to?

FA: Then as we incurred some cutbacks and started giving everyone the same meal, people were downright appalled.

PASSENGER: You mean everyone is getting the chicken? This is horrifying, I can't believe I don't have a choice!

FA: (to passenger) But, you do have a choice: eat or don't. (to audience) Now, as cost-cutting measures continue, we have not only eliminated the choice, but on certain flights we've eliminated the meal service altogether. Airlines are in the transportation business, not the restaurant business! As a passenger you are paying for transport from here to there, not for the bologna sandwich that we throw in your face. When the airline tells you they'll be serving a five-course meal, it means an apple, a granola bar, cheese, crackers, and a mint in a paper bag. . . The last thing I'd like to remind people is that the flight attendants, just like waiters, are the last ones to touch your food or beverage before you consume it. Keep this in mind at all times and bon appetit!

NEW FLIGHT ATTENDANT: (end of the flight) We here at WAFTI appreciate your business and we want you to know that we're constantly upping our standards . . . So up yours! Buh bye!
```

---

## IC-1099: Attack of the Moral Fuzzies

- Title: Attack of the Moral Fuzzies
- Author (byline): Nancy Beverly
- Work: Ten-Minute Plays from Actor's Theatre of Louisville
- Publisher: Samuel French, Inc.
- Publication date as stated: 1989
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: AT RISE, RAMON, BETHANN, MISS L, BETH, DAVE, JOLLEEN, ELAINE, IDIOT, BENNIE, NADA, CLAIRICE
- Teaser before the introduction: Yes
- Spoken words (computed): 1711
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
Attack of the Moral Fuzzies by Nancy Beverly
```

### Performance text (classify this)

```text
AT RISE: Somber Voice (In Darkness): Do you feel lost? Indecisive? Queasy? Are you a stumbler in the dark? Flailing your arms hopelessly, hitting your head against unseen walls? Are you tossing and turning on the stormy sea of life, miles from a harbor of safety and calm? (pause) Relax, Beth. Come with us. No more indecision. No more guilt. Life made simple. Join us as we play the dream of your choice, MORALITY MADE EASY!!!

And now, here’s your host, Ramon!

(Zippy music, bright lights – blinking lights if available – as RAMON, our sleazy host, sweeps in. His able-bodied assistant, MISS LOWENTHAL, runs around throwing confetti, balloons, the whole number. Note: RAMON is not necessarily of Spanish descent; accent is optional.)

RAMON: Good evening, good morning, good grief, good God, great gosh almighty, hot diggity dog, come on in, sit right down, we’re here, you’re there, and our contestant, BethAnn Shumway is on the spot! (BethAnn Shumway enters or lights rise to reveal her. She has put on her nice Sunday outfit to come down here. She smiles nervously. She simultaneously wants to be here and wants not to mess up.) Say Hi, BethAnn!

BETHANN: Are we on?

RAMON: We’re always on, dear, that’s one of the problems. Life just won’t let up, will it? But today we’re going to take away all of that trauma. Won’t that be wonderful?

BETHANN: Yes, it will, Ramon.

RAMON: Now about those rules: millions and zillions of ‘em, entirely to complicated to understand. If we understood the Rules of Life, we wouldn’t have to play the game. Ah, the Game, the Game, she is simple. Five fun-filled rounds, each more pleasant than the last, each hinging on you unhinging that conscience. And after each one, we hook you up to the old Anxiety-o-meter to see how you’re doing. Yes, how fast can you get to Nirvana, or as we like to call it, Okey-Dokey Land. Just to see where we are, let’s take that first preliminary reading. Miss Lowenthal, if you would do the honors. (MISS L has already gotten the meter, or effortlessly escorts BETHANN to a contraption. RAMON does a trumpet fanfare.) Doooo doo doo doo doo doo dooooooooo…a nine and a half! (SFX: taped groans) BethAnn, for heaven’s sake, come away from that thing. What in the world is causing all that trauma? (stage whisper) This is the part where you tell us about yourself.

BETHANN: Oh. Well, I work in a hospital in a cancer ward where I counsel families of dying patients.

MISS L: God, that must be terrible. How do you get through it all?

BETH: I don’t. Some days I just stay in bed and cry all da-

RAMON: Well, BethAnn, it’s time to get rolling, time for Round One: (SFX: ding) International Follies. Ready? You’re buying a new car. Do you purchase Japanese because it has a better performance record… (Lights up on a poster of a Japanese car) or American, to support the home auto industry? (Another car poster. Thkinking music. SFX: ding).

BETH: Japanese?

RAMON: Okay, Miss Lowenthal, let’s see who you’ve got there! (Miss L pulls a curtain or lights reveal DAVE). Dave Armstrong!

DAVE: (eager, freshly scrubbed face) Thank you, BethAnn for helping support my dad’s Toyota dealership. Because of people like you, both Japanese and American workers can stay employed – like my dad and me and my brother Dwayne – and also you’ve helped keep free enterprise alive. Thank you very much, BethAnn.

(He exits or lights go out on him. MISS L leads applause.)

MISS L: Very good, BethAnn…

RAMON: How does it feel to have made the right choice?

BETH: I, I…feel pretty good.

RAMON: Ladies and gentlemen, she feels pretty good; how good is pretty good? Let’s check that out scientifically with Mr. Meter. A seven and a half, very nice, BethAnn. I think she’s on a roll, so let’s go to the Second Round right now. (SFX: ding) Funding Mania. It’s time to divvy up the tax pie. There’s only enough money for keeping either Basic Grants to college students… (ELAINE appears) or providing Day Care to working, lower-income moms. (JOLLEEN appears.) Which do you choose? (Thinking music. SFX: ding).

BETH: I guess I’d provide the Day Care.

RAMON: Okay, Miss Lowenthal, who have we got this time? (Lights brighten on JOLLEEN.) Jolleen Budge!

JOLLEEN: (a little stiff and camera-shy) Thank you, BethAnn, for thinking of us. Because of your thoughtfulness, I am able to keep working at the Tastee-Freeze and still keep Wanda Sue at the Day Care Center where she receives excellent looking-after, and then I still have enough money left over to buy new tires this year. Thank you, BethAnn. (BETH has noticed ELAINE exiting, but MISS L and RAMON have maneuvered her attention to matters at hand. Applause.)

MISS L: Aww, I feel so warm and wonderful. How about you, BethAnn?

BETH: I, I feel terrific. (shaking the tension out of her hands) Boy oh boy, this is so nice. You know, I used to have this little knot right back here (points to her shoulder blades), but it’s disappeared!

RAMON: And what’s the ol’ Meter telling us now?

MISS L: It’s a good one. Five and a half. She’s heading straight for Okey-Dokey Land.

RAMON: Jolleen’s happy, Dave’s happy, I’m happy, you’re happy, BethAnn’s happy, the guys in the booth are happy, the parking lot attendant’s happy, one big happy family! Round Three – (During RAMON’s digression BETH’s eyes have strayed back to where ELAINE exited.)

BETH: Uh, Ramon, could I ask one quick question? . . . I was just wondering…does that girl get to go to college, now that she doesn’t have a Basic Grant?

RAMON: I believe you’re straying from our guidelines, dear.

MISS L: No worrying allowed.

BETH: I’m not worrying…exactly. I was just curious. Could I just, you know, chat for a second? It’ll only take a second. Where is she, back here?

RAMON: (Sings, under his breath) “Every party has a pooper… (MISS L joins him) …that’s why we invited her, party pooper…” (BETH enters dragging ELAINE, who is quite confused.)

ELAINE: What’s going on?

RAMON: Oh, not much. Welcome to my nightmare! We’re making it up as we go along – BethAnn Shumway, meet Elaine Henselmeier. (MISS L half-heartedly tosses a bit of confetti.)

BETH: Hi, I was just wondering, do you get to go to college now?

ELAINE: I’ve already been – for a couple of years, in business. But I could only go part-time because I had to work. At that rate, it was taking me eight years, so I quit and got a full-time job as a receptionist in a doctor’s office.

BETH: Are you going back someday?

ELAINE: I doubt it. This job’s okay –

BETH: – But this isn’t fair –

ELAINE: Yeah, but I’m engaged, and my finance’s got a good job selling aluminum siding

BETH: I’ll give you the grant, you can have the grant – Ramon, I really don’t think I’m cut out for this.

RAMON: Beth, you’re thinking too much. The name of the game is Morality Made Easy, not Life’s A Bitch.

RAMON: (BETH takes a deep breath and mouths an “okay.”) Round Three. (SFX: ding.) Hospital Hijinx. At a famous hospital, the writing is on the wall. Funding is being cut back. Out of these three hot ticket items, which one would you support: heart transplants for adults, liver transplants for cute kids under the age of six, or medicare supplements to keep pace with the cost of living.

(Music starts, then slows down as if the electricity has been pulled. BETH quavers, knees buckle.)

BETH: I can’t do it Ramon, it’s too close to home. I think I’d better just throw in the towel.

RAMON: QUITTER. (BETH shrinks.) You know what happens to people like you, don’t you? Huh? HUH? (BETH, feeling like five-year-old, shakes her head no.) You become a misshapen, spineless idiot incapable of even the most elementary decisions. Miss Lowenthal! (MISS L reveals a hunched-over male, a la the Elephant Man, with normal, albeit whiney, speech and indecisive clothing.)

IDIOT: (As if by rote) I am a misshapen, spineless idiot, incapable of even the most elementary decisions.

RAMON: This is a man paralyzed by caring too much. He could once decide which countries should have the bomb, whether we should be backing the Nicaraguan Contras, and even who could or could not have an abortion. Now he can’t even pick out the color of his socks in the morning. . . So you see, you have to choose, it’s a given. (He gestures for Miss L. to gently remove the IDIOT from out of his direct eyesight.) Recapping Round Three: heart transplants, liver transplants, or medicare supplements. (Fast music, SFX: ding.)

BETH: (in one breath) I want the largest chunk for the medicare patients, they’ve paid into the system the longest, and I want the second largest chunk for kids’ liver transplants because it’s not their fault they were born with a bad liver, and I also want money to go for heart transplants because they seem to be having a lot of success with that recently.

RAMON: (pause, eyes her) Covered those bases, huh, kid? Okay, Miss Lowenthal, let ‘er rip. (BENNIE KINCAID is revealed, He’s sweaty, greasy, nervous, and desperate. He’s also an auto mechanic.) Meet Bennie Kincaid!

BENNIE: BethAnn, how could you do this? The hospital bills are gonna kill us. Dad had insurance, but when they found out he had Hodgkin’s disease, well, they aren’t so friendly anymore. And he’s only sixty-five, so this could drag on for a long time. I’m tryin’ to run the Shell Station by myself, and when Dad comes home from the hospital, who’s gonna take care of him ‘cause Mom’s gotta work? We just aren’t quite keepin’ up with the cost of livin’, BethAnn. The increase wasn’t enough.

RAMON: Meet Nada Ivanhoe! (NADA is the warm, nurturing type. She too, is angry, but cooler about it. She speaks in modulated tones – with a veneer.)

NADA: Hello, BethAnn. How are you? Have you had a nice day today? Have you enjoyed the bountiful spring weather we’ve been having? I don’t mind telling you we’re having a hard time enjoying it at the Ivanhoe home. In fact, we’re not even at home most of the time. We’re at the hospital with little Justin. The closest we get to spring is looking out of his hospital window. As you may know, Justin is awaiting a liver transplant. If he does not receive a new liver in the next two weeks…(she trails off) Well, we too, like Mr. Kincaid, are a little strapped for cash. The hospital was hoping to provide six free transplants this year. As you may know, funding didn’t quite come through. (pause) But we’re still praying. (pause) I think I hear some chickadees outside. How lovely. (pause) Have a nice day, BethAnn.

RAMON: And finally, Clairice White!

CLAIRICE: BethAnn, unlike Bennie and Nada, I am speaking for myself. I am dying. They just found out I have terminal heart disease. I am only twenty-three years old. I used to raise flowers for the 4-H. I used to be a cheerleader. I used to work as a dental hygienist. No more. Research on heart disease like mine needs to be done (A TV ad:) Only you can help. Give to the heart foundation of your choice. A young heart is a terrible thing to waste. Goodbye, BethAnn.

BETH: I quit, I quit, I quit, I quit, I quit, I quit… No, I want to make the right decision – But I keep messing up –

RAMON: So. Beth. What’s up?

BETH: I messed up Round Three. I didn’t make the right choice, did I?

RAMON: Are you kidding? You waffled, you fudged, you hedged, you wanted to please everyone. You and Congress. , , , Well, BethAnn Shumway, looks like the game is over.

BETH: But, but, but… Prizes, what about prizes? You kept promising prizes!

RAMON: You’re too tense for prizes.

BETH: (desperate) Well, how about…consolation prizes, like a car, or a stereo, or –

RAMON: Whoa, whoa, no, no, Beth, sweetheart. There is no consolation here. We were offering peace of mind. We were offering the smug satisfaction that you’d made a good decision without second thoughts. And you turned it down. Prizes? If you’re lucky, you’ll get out of the studio in one piece – that’ll be your prize.

BETH: (with grim determination) My favorite color is yellow, my favorite cereal is Raisin Bran, I am buying Japanese this time, and the money goes to Medicare.

(Pause - She lashes out at them – and herself.) What did we all want, huh? Warm breezes and iced tea? Easy answers? People should not come on this show – I hope it dies in the ratings. (She storms out quickly.)
```

---

## IC-1100: Baby

- Title: Baby
- Author (byline): Conrad E. Davidson
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: 1983
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: COACH, BABY, TIMEKEEPER, MOMMY, DADDY, BABBY
- Teaser before the introduction: Yes
- Spoken words (computed): 885
- Already set (do not supply): none

### Source block (context only)

```text
Author: Conrad E. Davidson
ISBN: 978-0573618987
Publisher: Samuel French, Inc.
Date (Month/Year): 1983
```

### Introduction (context only: never use it for content warnings)

```text
Baby by Conrad E. Davidson
```

### Performance text (classify this)

```text
Baby and Coach are discovered onstage. Baby, dressed in a graduation cap and gown, listens attentively.

COACH: (Pg 7) Trick #237 is: suck your thumb, whichever one seems most comfortable. Try it now. First, your right, then your left.

BABY: And if they take it out?

COACH: Be persistent. Pop it right back in. Don’t give up.

BABY: I like this.

COACH: Which brings us to the pacifier, the common device parents use to break the habit of their thumb-sucking children. P-A-C-I-F-I-E-R. And when you finally get attached to it, they take it away as quickly, without warning, as they gave it to you. (Timekeeper enters and hands note to Coach)

TIMEKEEPER: Two minutes for baby. (exits)

BABY: Who’s Baby?

COACH: You are since we received advance notice that’s what your parents will name you.

BABY: They’re going to call me Baby all the time?

COACH: Maybe. As parents, it’s their prerogative.

BABY: (Pg 8-9) I’m not going.

COACH: Once these things are set in motion, there is no turning back. That’s the way of the world.

TIMEKEEPER: One minute for . . . sorry, still no name. One minute for Baby. (exits)

BABY: Dumb. Dumb. Coach, you haven’t given me enough advance preparation.

COACH: I’ve drilled you, lectured you, and demonstrated all the trick of the trade. I can’t squeeze nine months of instruction into mere seconds.

BABY: Oh, I don’t want to go, I’ll never last. They haven’t even given me an identity. (Baby urges Coach on in nonverbal desperation)

COACH: (Pg 9-10) Squirm and kick when they change your diapers. After the diaper change, wait half a minute and mess again. When they give you a bath, throw water out of the tub. Swallow marbles. Unscrew the nipple off your bottles, dump the milk on the carpet. Throw food on the floor. Rub food in your hair. Pout. Use cry technique #5 – the ear pierce. Have a fit at least once a day.

TIMEKEEPER: Ten seconds.

COACH: After a hard sneeze, rub it in your face with your hands. Vomit whenever it’s convenient.

BABY: I’ll never remember all those things!

TIMEKEEPER: Four. Three. Two. One. Time. (Pg 11) It’s time (exits)

BABY: If they want me, they’ll have to come and . . . (Baby is pulled by an unseen force off stage) Wait a minute. Stop pulling. I didn’t ask for this. What about the democratic right of choice? Choice! Choice! ********Scene Change************

MOMMY: (Pg 12) Feels so good to have cutesy Baby at home, doesn’t it, Daddy? One little grin for Mommy-pooh.

DADDY: One little smile, Baby-kins.

BABY: Mommy-pooh? Baby-kins? You are dumb dumb dumb.

DADDY: (Pg 14) Watch me teach Baby another word. Baby knows sixty words already. Pretty good for only four months old.

BABY: Four months?

DADDY: (Pg 15) Synorthographic.

BABY: Someone make him stop this stupidity.

DADDY: (Bending close to Baby as baby holds his breath. Daddy’s breath smells!) Synor ...

BABY: Can’t breathe.

DADDY: tho . . .

BABY: Suffocating.

DADDY: graphic . . . ic

BABBY: I’m choking. I’m going to pass out. (Baby yells)

DADDY: Very good, Baby. Means spelled alike.

BABY: I wasn’t close at all, dummy. (sucking in a big breath) Ahhhhh. Fresh air.

MOMMY: (Pg 16) You’re six months old now, Baby. Time to learn to crawl. (Mommy positions baby on the floor) First one hand, then the other. Push Baby’s butt, hubby dear. (Baby falls forward on his face and yells)

BABY: First the words, now this butt business. These people aren’t normal. (Pg 17) (Daddy picks up Baby and tosses him in the air) Put me down, you loonies. I’m getting sick. Do babies ever outlive this stupidity?

DADDY: (Pg 21) (puts baby on the floor and shoves butt) Biodynamic. . . Coprolalia . . . Peniapolis . . . Salmagundi

BABY: (Pg 22) Stop pushing. Cut it with the words. You’re going to make me cry. You weirdos don’t know when to quit. (Pg 23) STOOOOOOPP! (Daddy freezes) Where’s that coach?

COACH: (Stepping forward) Been here all along. Speak.

BABY: Don’t interrupt, don’t pinch my cheeks, don’t breathe in my face, don’t shove my butt. Just sit and listen. If I have to endure any more of that insanity, I’ll go nuts. I don’t want to know what the next what-should-we-do-that’s-weird-to-Baby business will be. The thought makes me want to scream. (Baby screams)

COACH: Hold it. Hold it. Don’t let it be a one-sided battle. Fight back. (Baby looks confused) (Pg 24-25) You’ve forgotten your pre-baby training. You need on-the-job training. They won’t be able to see or hear me, so don’t worry about that. (Coach snaps fingers. Baby screams in desperation and poops his diaper. Mommy and Daddy enter)

MOMMY: Ohhhhh. Baby messed again. Change Baby, hubby dear.

DADDY: Certainly, Mommy. While I do, I’ll teach Baby another word. Nyctalopia. The condition of seeing poorly at night or in partial darkness.

BABY: (to Coach) What do I do? I can’t stand this word business.

COACH: Wait until he gets your diaper off, then stick your hands in it. (Baby does)

DADDY: Help, honey, Baby , just stuck . . . ick.

COACH: That’s the stuff, kid. When they put the clean diaper on, pretend they poked you.

(BABY screams)

DADDY: Baby was squirming. Baby never squirms. (leans in to settle Baby down) A word. Baby always likes new words . . . Chromatography. Anomahitic. Quondom.

BABY: (Pg 26) He’s going to breathe in my face. (to Coach) What’ll I do?

COACH: (Pg 28) Bite him. (Baby bites)

BABY: (Pg 26) This isn’t bad.

COACH: You’ve got them running, kid.

DADDY: (Pg 25) Baby is one year old today.

MOMMY: (Pg 29-30) Hurry, hubby. Baby’s birthday party guests are here!

BABY: (to Coach) What’s a party?

COACH: The best time for baby tricks. (Daddy picks up baby and tosses him in the air)

BABY: I really hate this.

COACH: Let him have it! (Baby throws up) Serves him right!

MOMMY: Look, Baby, a present . . . MARBLES! (Baby takes marbles, looks at them, then pops them into mouth. Mommy panics) Spit them out, Baby. Call the doctor, hubby. (Mommy attempts to get Baby to open mouth. Coach snaps fingers and all freeze)

COACH: You don’t need me any more, kid. Look how you’ve been handling the situation. That was a real nice touch – faking like you swallowed the marbles.

BABY: That was good, wasn’t it? Thought of it myself.

COACH: It’s your first birthday and I’ve got to go. Other babies to instruct, you know. Keep your chin up, kid. You’ll survive. Give it to them with both barrels. (Coach exits) (as a disembodied voice while baby pantomimes the actions) (Pg 9-10) Squirm and kick when they change your diapers. Swallow marbles. Unscrew the nipple off your bottles, dump the milk on the carpet. Throw food on the floor. Rub food in your hair. Have a fit at least once a day.

MOMMY: Will we ever survive babyhood?

BABY: (Turns to grin slowly at the audience)
```

---

## IC-1101: Baby Talk

- Title: Baby Talk
- Author (byline): Doug Wright
- Work: Unwrap your Candy
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Oct 2002
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: ALICE, PSYCHIATRIST, BABY
- Teaser before the introduction: No
- Spoken words (computed): 1069
- Already set (do not supply): none

### Source block (context only)

```text
Author: Wright, Doug
Book: Unwrap your Candy
ISBN: 0822218712
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Oct 2002
```

### Introduction (context only: never use it for content warnings)

```text
I’d like to bring your attention to Case Number 696724-B A woman-approximately twenty-two years old, one hundred and five pounds, with no previous history of mental disturbance. Admitted for auditory hallucinations and social affective disorder. We’ll call the subject “Alice.” Alice became symptomatic at the time of her first – and only – pregnancy. Baby Talk by Doug Wright
```

### Performance text (classify this)

```text
ALICE: We had a big calendar up in the kitchen with big yellow boxes, rimmed with Highlighter. Those were ovulation days! He even came home over his lunch hour . . . . Then one day – finally – the stick turned blue. Sky blue . . . . I remember.

PSYCHIATRIST: Needless to say, however, Alice was . . . surprised . . . when the baby began to – to – vocalize – while still in the womb.

ALICE: I knew I’d feel things. Flutters. Kicks. But sounds? Soothing. Like those tapes you buy of rainstorms, or the lapping of waves.

PSYCHIATRIST: Soon, however, the sounds hardened into syllables.

BABY: Bah. Fah. Pah. Hom. Ling

PSYCHIATRIST: In my encounters with Alice, I tried to suggest – delicately, of course – that the sounds were organic in nature. Gastrointestinal.

ALICE: His first word in-utero. I’ll never forget it:

BABY: Conundrum

ALICE: An ambitious word. More sophisticated than one would expect. I’d lie on my back, and drape my hands over my belly. I’d hear them in my sleep.

BABY: Free-fall. Sartorial. Quaff.

ALICE: When I woke up, I’d write them down. Half the time, I had to consult a dictionary. “Quaff?”

BABY: “To drink deeply. To drain. To take long draughts.”

ALICE: My vocabulary grew by leaps and bounds.

PSYCHIATRIST: By its fifth month, the child was composing sentences.

ALICE: With most babies, it’s “Gimme wa-wa” or “Baby hafta poo.”

PSYCHIATRIST: But instead, the child opted for a loftier tone.

BABY: (In a thrilling baritone) “When the wintry branches scrape the sky, on midnight steed Death gallops by!”

ALICE: Again! Oh, say it again!

BABY: “Happy families are all alike, but every unhappy family is unhappy inits own way.”

ALICE: I’ve never been much of a reader myself. And I certainly don’t compose poetry; I couldn’t even rhyme “spoon.”

BABY: Loon. Moon. June. Festoon. Harpoon. Macaroon. Sasquetoon.

PSYCHIATRIST: Alice began to take dictation from the child.

ALICE: The notebooks. Three of ‘em, spiral-bound. One was full of poetry. The second was anagrams –

BABY: Dog. God!

ALICE: That kinda thing. And the last . . . the last was Eastern philosophy, mostly.

BABY: (Intones a sacred Buddhist chant)

ALICE: We’d planned on raising our child Presbyterian; now I wasn’t so sure.

PSYCHIATRIST: Soon the child’s fascination with language waned; it opted instead for pragmatism.

BABY: (Rapid-fire, tough) And it’s High-Tone on the outside, on the outside, Shenandoah in third place . . . and Musket Fire’s pulling ahead . . . pulling ahead . . taking the lead! Musket Fire’s in the lead.

ALICE: The ponies; it’s true!

PSYCHIATRIST: Alice would drape the racing forms about her mid-section, and in her ear the infant would coo:

BABY: Lucky Lady in the Third Lap . . . Ten down on Strawberry Fields. (Alice places the bet)

PSYCHIATRIST: Alice, who had never before demonstrated an interest in the track, soon found herself spending long afternoons there.

ALICE: I used my winnings to buy a wicker bassinet and a hand-sewn collection of antique baby quilts. Our child was the beneficiary; not me.

PSYCHIATRIST: In the kitchen, she would open The Joy of Cooking, and slip it under her elastic waistband. While she puttered amidst mixing bowls and measuring cups, the baby would recite the recipe.

BABY: (A French chef’s accent) That is the miracle of the phyllo pastry; it is densely layered, but it still has a light texture.

ALICE: Once we made bulgur pilaf. Another time . . . mmmmm! – fennel puree.

BABY: Another dollop of crème de cacao! Why so stingy!

ALICE: It was nice to have someone there with me. To do things.

BABY: (Playing chess) Checkmate

ALICE: Sometimes, he’d let me win. Just to buoy my confidence.

BABY: (Doing a crossword puzzle). Sixteen across: What’s an eight letter word that means hyperbole?

ALICE: Some women complain about the third trimester; not me. The days flew.

BABY: (Playing twister) Right hand, red. Left foot, green. I’m gonna spin it now. I’m gonna spin it . . . . Left hand, yellow. Right foot, blue!

ALICE: Around the 7th month, his tone changed. It . . . ah . . . deepened.

BABY: (Seductively) I like you in the red dress better.

ALICE: Frankly, it was nice to know that he had preferences.

BABY: Why, Alice. You cut your hair.

ALICE: He noticed.

BABY: (Low, sensual) You’re wearing them tonight, aren’t you? Aren’t you? The silk panties with the ecru lace?

PSYCHIATRIST: It wasn’t until the 8th month that the fetus became impertinent.

ALICE: I’d jolt awake in the middle of the night. I’d be sweating into my pillow. It would hiss. Hiss at me.

BABY: (Hissing) Water weight, water weight, water weight . . . .

ALICE: Water weight, water weight, water weight . . .

PSYCHIATRIST: By the 9th month, the child had turned insidious.

BABY: Remember those foot braces you wore as a baby? Clunk, clunk, clunk against the sides of your crib . . . (Alice nods with recognition and dread). Well wait’ll you see me. I’ve got webbed toes and a purple rash. (Alice gives a tiny cry of horror). Spina bifida!

ALICE: (Terrified now) Oh, God.

BABY: Hydrocephalus.

ALICE: No!

BABY: Dwarfism!

ALICE: No, no, no – I saw the sonograms, I saw them myself - - -

BABY: DOWN’S SYNDROME!

ALICE: Each little finger, each little toe

BABY: You’ll have to enroll me in . . . sp . . . sp . . . sp . . . SPECIAL classes, and physical therapy, and – once a week or so – cranial drainage –

ALICE: I don’t have the strength, I don’t have the patience . . .

BABY: Pushing me down the aisle of Toys ‘R’ Us in a motorized stroller with the tubs and the fibrulator – (with Satanic reverb) YOU’RE CONDEMNED TO LOVE ME REGARDLESS – EVEN IF I’VE A FORKED TONGUE AND A TAIL!!!!

ALICE: I was its room, I was its board, I was its future. How could it . . . How dare it . . . I didn’t want to birth it; no. I wanted to expel it. I wanted to purge it from my body. But most of all . . . I wanted to confront it, face to face.

PSYCHIATRIST: The day finally arrived. The labor was grueling

BABY: I’M NOT LEAVING! SQUATTER’S RIGHTS! YOU PACK UP YOUR FORCEPS, BONE-MAN, AND YOU GET THE HELL OUTTA MY MAMA’S PRIVATES! I GOT HER BY THE KIDNEY – I GOT HER BY THE BOWELS – AND I AIN’T GONNA LET GO.

ALICE: Then I saw its head crown Seven pounds, six ounces. Twenty-one inches long. Blue eyes, with the palest tufts of blonde hair.

PSYCHIATRIST: The doctors bathed the baby, and soon delivered a small, pink bundle into Alice’s arms (Alice raises her arm as if holding the baby.) It lay there, wrinkled, its blurry eyes exhausted from the rigors of birth.

ALICE: (Belligerent) Well? What do you have to say for yourself now? It clammed up. It just lay there.

PSYCHIATRIST: It squirmed and it drooled, but it didn’t say a word. It could cry full-throttle and later – after a few months – it would babble, but as for grand pronouncements and poetry readings, well, there were none.

ALICE: It’s a battle of wills, that’s all. But one day it will happen. It will crack open its little maw. It’ll use its tongue to shape poison arrows. It will begin innocently enough, I’m sure. “Da-da” “Boo-Boo” But the rest will follow soon enough. It might take months. It might take years. But – in the end vengeance will be mine.

BABY: (Giggles)
```

---

## IC-1102: The Baptist Gourmet

- Title: The Baptist Gourmet
- Author (byline): Jill Morley
- Work: Even More Monologues for Women by Women
- Publisher: Heinemann
- Publication date as stated: March 2001
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: TULULA
- Teaser before the introduction: Yes
- Spoken words (computed): 415
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jill Morley
Book: Even More Monologues for Women by Women
ISBN: 978-0325002477
Publisher: Heinemann
Date(Month/Year): March 2001
```

### Introduction (context only: never use it for content warnings)

```text
Meet Talula, the Baptist Gourmet as she walks you through the world of cooking that Julia Child would be proud of - From fried chicken to croutons shaped like the baby Jesus. The Baptist Gourmet by Jill Morely

(Tulula has her own cable cooking show. She is Southern probably from South Carolina or New Orleans.)
```

### Performance text (classify this)

```text
TULULA: G'Mornin! Welcome to Channel 64's "Cookin' with Tulula." I'm Tulula Lee May, your Baptist Gourmet and before I lead you in a recipe, I'm gonna lead you in a prayer.

Lordy, Lordy, let me learn. Not to let my souffle burn. And if it does, oh promise me this. Someone in my kitchen will like it crisp! Amen.

Last night, I was divinely inspired when the Lord came to me in a dream and he said, "Tulula, you are my culinary link to humanity. I bestow upon you the celestial preparation for fried grits." Ingredients are hominy, cheese, and the life-giving energy to all the Lord's creatures. . . fat.

First you must baptize your ingredients. (Throws water on the ingredients with fervor) You're baptized! You're baptized! You're baptized!

Next, we finely chop the hominy and the cheese, which I already have done because they won't let me have the air time I need. (Smiles and winks at a producer off stage) Isn't that right, Jimmy? (Under her breath) Producer Shmoducer.

Then, we take the hominy, the cheese, we put it in a skillet and FRY IT UP!!! JUST FRY IT UP! IN THE NAME OF THE LORD, JUST FRY IT UP!!!! (Lightheaded, she sits down and fans herself) Oh, this is gonna be a good one.

Now, while we're waitin' for the culinary miracle, like waitin' for the second coming, I'd like to read some of my viewer mail. Preacher Mapplethorpe writes, "Dear Tulula, thank you for bringing that fried Caesar's salad to the church bazaar last week. Everyone raved over those cute little baby Jesus croutons. And that parmesan cheese looked like snow in the manger!" Amen.

Tessie Jo Miller from Duncan Road asks, "Dear Tulula, what is the rule of thumb in Southern Baptist food preparation?" Tessie, has your cheese dun slid off your cracker? Just slap on some cheese and FRY IT UP! FRY IT UP! IN THE NAME OF THE LORD, JUST FRY IT! (Collapses and fans herself again) Lord save us all.

Letter from Madge Peeker on Winston Lane, "How do I make my home fried taters taste like yours?" Madge, I seen the way you fry those taters at the church socials. You just chop 'em all up like they was the devil's spawn! With each slice, you must instill goodness and ethics and morality. Handle your taters the way God handles His children and your creation will be as perfect as His. On that note, let's resurrect those grits. . . . (She tastes them.) Mmmmmmm, mmmmmmm, just like the Lord woulda made them.

Now, tell your Catholic friends to tune in next week because I'm making fried St. Joan Kabobs! Bye y' al!!!!
```

---

## IC-1103: Bartholomew and the Oobleck

- Title: Bartholomew and the Oobleck
- Author (byline): Theo Geisel (aka Dr. Seuss)
- Work: Not specified
- Publisher: Random House
- Publication date as stated: Oct 1949
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, KING, BARTHOLOMEW, MAGICIANS, BELL RINGER, TRUMPETER, CAPTAIN
- Teaser before the introduction: Yes
- Spoken words (computed): 1331
- Already set (do not supply): none

### Source block (context only)

```text
Author: Theo Geisel (aka Dr. Seuss)
ISBN: 978-0394800752
Publisher: Random House
Date (Month/Year): Oct 1949
```

### Introduction (context only: never use it for content warnings)

```text
In an age when power is often mistaken for entitlement, this story feels less like a children’s fable and more like a warning etched in green slime. King Derwin’s insistence that even the sky should bend to his will echoes a dangerous change in modern governance -- where leaders test the limits of institutions, sidestep norms, and treat politics as something to command rather than uphold. When a leader begins to see themselves not as a servant of their people but as an all-powerful, untouchable authority, our way of life is doomed. Can the kingdom be saved? Only if ordinary people, institutions, and officials speak plainly and insist, without fear, that no one, however powerful, rules the sky.

Bartholomew and the Oobleck by Theo Geisel (aka Dr. Seuss)
```

### Performance text (classify this)

```text
NARRATOR: They still talk about it in the Kingdom of Didd as The-Year-the-King-got- Angry-with-the-Sky. If it hadn’t been for Bartholomew Cubbins, that King and that Sky would have wrecked that little Kingdom.

KING: (staring up into the sky, muttering and sputtering) Humph! The things that come down from my sky!

NARRATOR: All spring when the rain came down, he growled at that . . . All summer when the sunshine came down, he growled at that. . . All Autumn when the fog came down, he growled at that . . . And that winter when the snow came down, he started shouting!

KING: This snow! This Fog! This Sunshine! This rain! BAHH!

BARTHOLOMEW: (trying to calm him) But, King Derwin, you’ve always had these same four things.

KING: (bellowing) That’s just the trouble! Every year the same four things! I want something NEW to come down!”

BARTHOLOMEW: Something new? That’s impossible, Your Majesty.

KING: Boy, don’t you dare tell me what I can or cannot have! I am King!

BARTHOLOMEW: I know, Sire, you rule all the land. And you rule all the people. But even kings can’t rule the sky.

KING: (flying into a terrible rage) Well, maybe other kings can’t do it, but maybe I’m one king who can! (begins laughing) They can do it for me! Bartholomew Cubbins, call my royal magicians!

BARTHOLOMEW: (shivering) Oh, no, Your Majesty! Don’t call them!

KING: Hold your tongue, Bartholomew Cubbins! You do as I command you.

BARTHOLOMEW: (bowing) Yes, Sire. But, Your Majesty, you may be very sorry.

NARRATOR: He took the King’s secret whistle from its hook. He blew a long, low blast down the King’s stairway. And a moment later he heard them coming!

MAGICIANS: (shuffling and chanting)
Shuffle, duffle, muzzle, muff.
Fista, wista, mista-cuff.
We are men of groans and howls,
Mystic men who eat boiled owls.
Tell us what you wish, oh King.
Our magic can do anything.

KING: I wish to have you make something fall from my skies that no other kingdom has ever had before. What can you do? What will you make?

MAGICIANS: (thinking, blinking) . . . Oobleck.
Won’t look like rain. Won’t look like snow.
Won’t look like fog. That’s all we know.
We just can’t tell you any more.
We’ve never made Oobleck before.

BARTHOLOMEW: (whispering) They’ll do something crazy, Your Majesty! Stop them!

KING: (chuckling) Stop them? Not for a ton of diamonds! Why, I’ll be the mightiest man that ever lived! Tomorrow I’m going to have OOBLECK!

NARRATOR: On the Mystic Mountain Neeka-tave the magicians were working their terrible magic. All night they walked circles round their magic fire . . .

MAGICIANS: (chanting)
Oh, snow and rain are not enough!
Oh, we must make some brand-new stuff!
Burn yellow twigs and burn red rust
And burn a stocking full of dust.
Make magic smoke, green, thick and hot!

(It sure smells dreadful, does it not?)
Go, magic smoke! Go high! Go high!
Go rise into the kingdom’s sky!
Go make the wondrous Oobleck fall!
Oh, bring down Oobleck on us all!

NARRATOR: Dawn was breaking and Bartholomew was still watching at the bedchamber window. There was something strange in the sky! At first it seemed like a little greenish cloud . . . just a wisp of greenish steam. Tiny little greenish specks were shimmering in the air right over his head.

BARTHOLOMEW: (stretching out his hand to catch a speck, the pulls his hand back, frightened. Slams the window shut, shouting) Wake up, Your majesty! Your oobleck! It’s falling!

KING: (springs from his bed) By my royal whiskers, it is! Oh, that beautiful oobleck! And it’s mine! All mine!

BARTHOLOMEW: I don’t like the looks of those blobs, Sire. They’re coming down now as big as greenish peanuts.

KING: (laughing) The bigger the better! Oh, what a day! I’m going to make it a holiday! I want everyone in my kingdom to go out and dance in my glorious oobleck!

BARTHOLOMEW: Do you really think it’s safe, Sire?

KING: (snapping) Stop asking foolish questions! Wake my royal bell ringer. Tell him to ring the great holiday bell! Run!

NARRATOR: Across the sleeping palace, Bartholomew ran. Then up the ladder of the high bell tower.

BARTHOLOMEW: Ring your bell! His majesty proclaims today a holiday!

BELL RINGER: (grabbing the bell rope and yanking – Nothing happens. He yanks harder – still nothing) Heh . . .? What’s wrong with my bell? I’d better take a look outside. (pokes his head out through the little trap door) Merciful gracious! What is THAT? All over my bell like greenish molasses!

BARTHOLOMEW: Not only your bell! Look at that poor robin down there in that tree!

She’s stuck to her nest! That oobleck’s like glue!

BELL RINGER: (wringing his hands) Oooh! If that green stuff sticks up robins, it’ll stick up people, too!”

BARTHOLOMEW: Someone’s got to warn the people! Warn ‘em to stay inside their houses! I’ll tell the royal trumpeter! (races off)

NARRATOR: But all the royal trumpeter blew was . . .

TRUMPETER: (blowing on his trumpet: GLUGG!) My horn! One of those green things flew inside it! (tries to blow it out; tries to shake it out, but no success) I’ll pull it out!

BARTHOLOMEW: No! Don’t you touch it!

NARRATOR: [But] The trumpeter’s hand was already in it.

TRUMPETER: (grabs hold of the lump of oobleck; pulls with all his might. The oobleck stretches then snaps back inside the trumpet, yanking his arm back with it) I can’t wiggle a finger! Oh, Bartholomew, what’ll I do?

BARTHOLOMEW: I hate to leave you stuck to your horn. But if you can’t warn the people of the kingdom, I’ve got to find someone who can! (races out)

NARRATOR: Down the stairs raced Bartholomew Cubbins . . . down to the chamber of the Captain of the Guards.

CAPTAIN: (humming in front of his mirror, combing the ends of his moustache)

BARTHOLOMEW: Captain! DO something! Haven’t you seen the dreadful Oobleck?”

CAPTAIN: (nonchalantly laughing) Oh, that stuff. What so dreadful about that? I think it’s rather pretty. That stuff’s harmless. I’ll show you. I’ll eat some. (leans out the window, scooping up some oobleck)

BARTHOLOMEW: Don’t, Captain! DON’T!

NARRATOR: The Captain did! By the time Bartholomew dragged him back inside the room . . .

CAPTAIN: (mouth glued shut with oobleck. Tries to speak, but no words come out)

BARTHOLOMEW: Forgive me for leaving you, Captain . . . (races out) I’ll get the King’s horse! I’ll ride through the country! I’ll warn the people of the kingdom myself!

NARRATOR: He pushed open the door that led to the Royal Stables. The awful oobleck was plumping down as big as greenish footballs now! Too late to warn the people of the kingdom! There were farmers in the fields, getting stuck to hoes and plows. Goats were getting stuck to ducks. Geese were getting stuck to cows. It was piling up, great greenish tons of Oobleck, deeper and deeper on every roof in the land. There was nothing Bartholomew Cubbins could do out there.

BARTHOLOMEW: (shaking his head sadly, he steps back inside)

NARRATOR: But inside, a moment later, it was just as bad as out! With an angry roar, the Oobleck was suddenly hitting the palace harder! The whole palace was springing leaks. It was dripping through the ceilings. It was coming in everywhere . . . even through the keyholes!

BARTHOLOMEW: (gasping) The King!

NARRATOR: Where was the King? He’d forgotten all about him! Bartholomew found him in the throne room. There he sat . . . Old King Derwin, proud and might ruler of the Kingdom of Did, helpless as a baby. His royal crown was stuck to his head. The seat of his royal pants were stuck to his throne. Oobleck was dripping from his royal eyebrows.

KING: Fetch my magicians, Bartholomew! Make them say some magic words to stop the oobleck falling!

BARTHOLOMEW: (shrugging his shoulders) I can’t, Your Majesty. Their cave on Mountain Neeka-tave is buried deep in oobleck.

KING: (groaning) Then I must think of some magic words! Oh, what are those words my magicians say . . . ? Shuffle. . . duffle . . . muzzle . . . muff . . . That’s all I can remember and they don’t do any good! The oobleck keeps on falling harder!”

BARTHOLOMEW: (angry) And it’s going to keep falling until your great palace tumbles down! Don’t waste your time saying foolish magic words. YOU ought to be saying some plain simple words! This is all your fault! Now the least you can do is say, “I’m sorry.”

KING: (belligerent -- no one had ever talked to him like this before) What! ME . . . ME say I’m sorry! Kings never say I’m sorry! And I am the mightiest king in all the world!

BARTHOLOMEW: (not backing down) You may be a mighty king. but you’re sitting in Oobleck up to your chin. And so is everyone else in your land. If you won’t even say you’re sorry, you’re no sort of a king at all! (turns his back to leave)

KING: (great, deep sob, he begins crying) Come back, Bartholomew Cubbins. You’re right! It is all my fault! And I am sorry!

NARRATOR: And the moment the King spoke those words, something happened. . . Maybe there was something magic in those simple words, “I’m sorry.” Maybe there was something magic in those simple words, “It’s all my fault.” Maybe there was, and maybe there wasn’t. But they say that as soon as the old King spoke them, the sun began to shine. They say that all the oobleck just simply, quietly melted away.

Then the King proclaimed a new national holiday . . . in honor of the four perfect things that come down from the sky: The rain, the sunshine, the fog and the snow.
```

---

## IC-1104: Bat Boy – The Musical

- Title: Bat Boy – The Musical
- Author (byline): Keythe Farley, Brian Flemming and Laurence O’Keefe
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: Sept 2002
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: RICK, BAT BOY, RUTHIE, SHERIFF, DAISY, MAGGIE, LORRAINE, MEREDITH, SHELLEY, BUD, DR. PARKER, AS SHELLEY, ROY, REV. HIGHTOWER, DOCTOR
- Teaser before the introduction: Yes
- Spoken words (computed): 1377
- Already set (do not supply): none

### Source block (context only)

```text
Author: Keythe Farley, Brian Flemming and Laurence O’Keefe
ISBN: 978-0822218340
Publisher: Dramatists Play Service
Date (Month/Year): Sept 2002
```

### Introduction (context only: never use it for content warnings)

```text
In the early 1990s, people didn't have smartphones, Netflix, email or the Internet. What they did have was the checkout aisle at [Insert name of local grocery store]. Children forced to grocery shop with their parents sat in shopping carts and stared longingly at bubble gum, Tic Tacs, and - - of course – headlines from the Weekly World News tabloid: “Einstein’s Brain Comes to Life!; “Aliens Abduct Cheerleaders!” and the BEST one . . . "Bat Child Found in Cave!" The Bat Boy story went as viral as any “fake news” story could in the days before social media.

But then some brilliant writers decided to take this bizarre and outlandish story and make it something more -- A musical that quickly became a campy cult favorite with a message about being different; about the desire to be accepted for who we are.

Bat Boy – The Musical by Keythe Farley, Brian Flemming and Laurence O’Keefe
```

### Performance text (classify this)

```text
(Singing, off stage [both]) IN A CAVE MANY MILES TO THE SOUTH LIVES A BOY BORN WITH FANGS IN HIS MOUTH. A cave near Hope Falls, WV (population 500) In darkness. Rick and Ruthie Taylor, two local teens, are rappelling down to the bottom.

RICK: (Pg 7-8) Whoa. . . Look at this.

BAT BOY: (offstage sound by Actor 2) Oo-oo-Oo-Oo-Oo (wings flapping)

RUTHIE: We've never been this deep before.

BAT BOY: (offstage sound by Actor 1) Oo-oo-Oo-Oo-Oo (wings flapping)

RUTHIE: (focus off-stage front) It's some deformed kid.

RICK: (focus off-stage front) It's a Bat Boy. It's okay, little guy. I'm Rick Taylor. And this is my sister Ruthie.

RUTHIE: (focus off-stage front) Can you say "Ruthie"?

RICK: We are totally keeping this thing.

RUTHIE: (focus off-stage front) See if it likes Fritos. (produces some and offers them to Bat Boy) Fritos. See? Fritos. (pantomime Bat Boy attacks Ruthie) AAAAAHHHHHH! I’m bit! I’m bit!

RICK: You freakin' animal! (pantomime Rick pulls Bat Boy off Ruthie and pins him to the ground)

(Singing, off stage [both]) IN A CAVE MANY MILES TO THE SOUTH LIVES A BOY BORN WITH FANGS IN HIS MOUTH. At the Sheriff’s Office -- Rick hefts a burlap sack containing Bat Boy from his back and sets it on the ground.

SHERIFF: (Pg 10-11) You say it’s the Bat Boy?

RICK: Yeah! It bit Ruthie. You gotta lock it up, Sherriff. (kicks the bag. Bat Boy squeals)

DAISY: Can we see it?

SHERIFF: All right. (Opens bag a little; ladies peek; Bat Boy squeals)

DAISY: Aaah! Sweet wounded Jesus!

SHERIFF: (to Rick) You go on and look after your sister. I'll just take it up to Dr. Parker. Dr. Parker's a good veterinarian, I'm sure he'll just put it down with no trouble.

MAGGIE: Seems like a waste of resources. We could put him on display and charge admission.

LORRAINE: People would pay good money to see a Bat Boy. We could be the next Branson.

SHERIFF: Good day, ladies. *****Veterinarian Parker’s home*****

SHERIFF: (Pg 14-15) (authoritative knock at the door) It’s Sheriff Reynolds, Meredith! (gestures outside) I figure maybe we need a veterinarian to sort this out. I’m hoping Dr. Parker will know what to do.

MEREDITH: (focus off-stage front) (Pg 16) Is it an animal or a . . . (Pg 15) boy? Shelley, get away.

SHELLEY: (focus off-stage front) (Pg 17) Mom! What’s wrong with him? (Pg 16) He’s so gross!

MEREDITH: All right, Sheriff. I'll take care of the boy for you. Dr. Parker has some cages. I'm
sure we can find one that works.
*****
Bat Boy, screaming, is now in a cage off-stage front (screaming voiced by Actor 1 off-stage)

SHELLEY: (Pg 18-19) (hands over ears) Shut up shut up shut up SHUT. UP!!! (calling offstage) Mom, he won't shut up!

MEREDITH: (Meredith enters. Bat Bay stops screaming) Yelling at him won't help, sweetheart.

SHELLEY: Such an ugly boy.

MEREDITH: Shelley, that's not nice. He's just different. (Pg 20) What would you like to name him?

SHELLEY: Bat Boy.

MEREDITH: We're not calling him Bat Boy. That's cruel.

SHELLEY: But that's what he looks like! (beat) How about Ugly?

MEREDITH: Maybe Edgar. (Calling) Ed-gar!

BAT BOY: (Looks at Meredith) Gggnnnnwwgwoooo?

MEREDITH: Edgar it is!

SHELLEY: He likes Ugly better. (exits in a huff) *****Town Council Meeting*****

MAGGIE: (Pg 26) As Mayor of Hope Falls, West Virginia, I hereby call this meeting of the Town Council to order. (gavel) First order of business. We've got a crisis on our hands!

BUD: (Pg 28) Mayor Maggie, I'm telling you, this town is cursed! First the coal mines dried up. Now all the cows are dropping like flies. (Pg 27) Twenty-two dead cows . . . (Pg 28) and I’m thinking of blaming . . .

LORRAINE: (Pg 29) . . . that little Bat Boy they found in the bag? (long pause) Well, Dr. Parker’s a good man. I’m sure he’ll kill it! *****Veterinarian Parker’s home*****

DR. PARKER: (Pg 30-31) Sorry I'm so late! Hello! (bangs into cage. Bat Boy screams voiced by Actor 1 off-stage) Sweet wounded Jesus! How did you get here? (Parker pulls a syringe from his doctor's bag and fills it with liquid from a vial) This'll put one of us out of our misery.

MEREDITH: (enters quickly) Thomas, no! Please. Don't.

DR. PARKER: They'll have my head for something like this, Meredith.

MEREDITH: You can’t just kill him like an animal. Oh, please, Thomas. Please, please

BAT BOY: (Pg 36) Eeeleeee . . . (he continues to make pleading sounds)

MEREDITH: Hellooo? Can you say hello? You can do it. Look at my lips. (points to her lips) Lips. Hellllloooo. (Bat Boy imitates) Helllooooo . . . (Bat Boy gets better and better at it, until)

BAT BOY: Hhhhelllooo.

MEREDITH: (applauds and smiles) Good. (Bat Boy copies her - he applauds and smiles.) Now, can you say "boy"?

BAT BOY: Boy! Boy, boy, boy, boy, boy!

MEREDITH: You're a smart boy, too. We'll turn you into a proper young man in no time. TRANSITION Bat Boy evolves at a lightning pace learning from flash cards, photographs, videotapes and records. He learns etiquette, how to dress and even gets his GED

AS SHELLEY: That’s more than I can say for Rick Taylor!! But still, that’s not enough for the good folks of Hope Falls.

*****Town Council Meeting*****

MAGGIE: (Pg 43) I hereby call this special meeting of the Town Council to order. Let's discuss safety issues for this weekend's Revival Meeting.

ROY: (Pg 45) (yelling out) Doc, we want a guarantee. He can’t be allowed to come!

DR. PARKER: (Pg 43) I can assure you as a veterinarian that the boy is not a danger. Meredith has done wonders with Edgar. He's practically a member of the family.

BUD: Oh, for Pete's sake, we got Ruthie Taylor still in the hospital, and I've got a sinking suspicion that your Bat Boy is responsible for the cattle plague! I swear!

ROY: (Pg 44) You should just be grateful we don’t hang him from a tree.

DR. PARKER: (Pg 45) This is going to be hard on Meredith. But I give you my word. Edgar will not attend the revival.

ROY: Thank God, you’ll be showin’ some Christian charity (through gritted teeth) and some dang sense. *****Veterinarian Parker’s home*****

DR. PARKER: (In the kitchen with Meredith) [I gave them] my word of honor . . .

MEREDITH: (Pg 46-47) I don't like the Town Council telling me what to do with my family.

(Meredith enters the living room where Edgar is adjusting his clothes in front of a mirror) Don't you look lovely, Edgar.

BAT BOY: (with a British accent, adjusts his tie, suit) Thank you, Mrs. Parker. You're looking splendid yourself.

MEREDITH: Why, thank you. Those BBC language tapes are really helping your diction.

BAT BOY: You know, I was reading the newspaper this morning. (excited) The Reverend Billy Hightower is holding a weekend revival. I have just finished reading the Bible again, and it would mean so much to me if I could attend. It would be a nice coming out for me.

MEREDITH: Oh, Edgar, I feel horrible telling you no, but some people . . . (sighs)

BAT BOY: (Pg 49) I might as well be in a cage! You must allow me to show myself! (he breaks down and cries)

MEREDITH: Oh, Thomas, can’t we just let him go? He’s so charming, and well-spoken. Once they see what a proper young man he is, they’ll change their minds, don’t you think?

DR. PARKER: No no no no no! None of us will attend the revival, and that’s final! *****The Revival*****

(hand clapping, singing, humming, feet stomping, dancing, shouting) Suggested music: I’ll Fly Away -- originally written in 1929 by Albert E. Brumley and first published in 1932 by the Hartford Music Company. It is frequently played in worship services. https://www.youtube.com/watch?v=PYyyfw349FI

REV. HIGHTOWER: (Pg 59-60) All right, let's bring it down. I know there's someone out there who needs healing. Step forward! Let the Holy Ghost heal you!

BAT BOY: I want to be healed.

REV. HIGHTOWER: (staring at him in horror) Oh, Jesus, Son of God.

LORRAINE: (pointing) It’s the Bat Boy! The Bat Boy! I’m going to faint!

BUD: Sweet wounded Jesus!

BAT BOY: (clears throat) I know you hate me. But I have to believe that it's because you don't know me.

RICK: (Pg 22) You freak! . . . You wanna bite me like you bit my sister, tough guy?

MEREDITH: (Pg 63-64) Please! Everyone! It's true Edgar was not civilized when he was first captured. Since then . . . I mean, look at him. You all just heard him. Can't you see that he's not a danger to any of us?

BAT BOY: I never meant to hurt anyone.

RICK: Animal!

MEREDITH: (Pg 82) Stop! All of you! If you would only listen to his story, you'd understand. (to Dr. Parker) For God's sake, Thomas, let's just tell the truth. (beat; they talk directly to the audience) I was Thomas' assistant at the time. I loved him dearly. *****Flashback to story*****

DR. PARKER: (Pg 83-84) I loved her dearly. [But] I was a young and ambitious vet just starting out, developing a pheromone to increase birth yield in cattle. (raising a test tube)

MEREDITH: He introduced the pheromones of a dozen other animals.

DR. PARKER: We were working late one night in my laboratory.

MEREDITH: And that's when the accident happened. (Parker spills the contents of the test tube on Meredith)

DR. PARKER: (Grabs Meredith) You are so beautiful.

MEREDITH: Thomas, no! (stage slap – Meredith runs out) I had no idea what was about to happen . . . (a bat flutters too close to her head. She ducks. The bat returns and attaches itself to her dress. She struggles to pull it off. Another attaches itself, then another, and another. Young Meredith screams) The bats were attracted by the pheromone. They were everywhere. They violated me.

DR. PARKER: The next morning, I found Meredith barely alive. When I discovered, two months after the incident, that Meredith was pregnant, I begged her to marry me. We moved to Hope Falls, where I was sure we could put the horrors of the past behind us. But the true horror was yet to come.

MEREDITH: (Pg 85) (huffing and puffing in pain)

DOCTOR: (off stage) Just one more push. That’s it . . . (Meredith gives birth to Bat Boy)

BAT BOY: (emerges) Oo-oo-Oo-Oo-Oo (tiny wings flapping)

DR. PARKER: (holding the bat baby) The job fell to me. I took the bat child out to the woods. Killing the thing should not have been a problem. But I couldn't do it. So, I left [him] at the mouth of a cave, (sets the bundle down) certain that time or predators would do what I couldn't do myself. But I was wrong. . .

MEREDITH: (softly echoing as she shakes her head sadly) (Pg 79) Abomination . . . hideous . . . *****End of Flashback*****

MEREDITH: (Pg 86) (to the crowd) So you see, he's not a beast. He's my son. He's one of us.

LORRAINE: Kill the freak!

DR. PARKER: (Pg 88-89) Meredith, I’m sorry. (Grabs Edgar from behind in pantomime) I can’t bear to look at him. (Pg 56) He’s a beast. He’s a monster. (takes a knife from his belt, raises it, stabs Edgar then lets the body fall)

MEREDITH: (Pg 89) Oh, Edgar. My dear sweet boy.

BAT BOY: I am not a boy. I am an animal. (he dies)

MEREDITH: (Singing, sadly) IN A CAVE MANY MILES TO THE SOUTH LIVE[D] A BOY BORN WITH FANGS IN HIS MOUTH.
```

---

## IC-1105: Beauty and the Beast

- Title: Beauty and the Beast
- Author (byline): AJ Jacobs
- Work: Fractured Fairy Tales, Pgs 103-110
- Publisher: Bantam Books
- Publication date as stated: Jan 1999
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, OLD MAN, DAUGHTER, PRINCE
- Teaser before the introduction: Yes
- Spoken words (computed): 1166
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
Long before Politically Correct Bedtime Stories arrived in bookstores, Americans were getting their giggles from Fractured Fairy Tales, those delightfully twisted parables brought to us between the cliffhanger adventures of our favorite cartoon heroes, Rocky & Bullwinkle.

ROCKY: *And now...

BULLWINKLE: Hey Rocky! Watch me pull a rabbit out of my hat!

ROCKY: But that trick never works!

BULLWINKLE: This time for sure! Presto! (something goes terribly wrong—be creative) Well, I'm getting close.

ROCKY: And now it's time for another special feature!

A nostalgic retro adventure re-imagined by AJ Jacobs in his collection of Fractured Fairy Tales. -- Beauty and the Beast
```

### Performance text (classify this)

```text
NARRATOR: (Pg 103-110) Once upon a time there was a magnificent golden castle on a silver cloud high up in the sky, which has nothing to do with anything because our story is about an old woodchopper who lived in a shack, but that's a good way to start a fairy tale.

NARRATOR: The old man was very happy, but he had a daughter who was very unhappy because . . . well, she was rather plain. Actually, she was really plain. In fact, she had a face like five miles of bad road. Anyway, it was time for her to marry, but because she was so fat and ugly, none of the young men of the kingdom ever came to ask for her hand, or any other part of her body, for that matter. Then one day, the old man decided to cheer her up.

OLD MAN: Child, it is your birthday and I've brought you something to keep you from being so lonely.

DAUGHTER: (wide-eyed) A man?

OLD MAN: Nope. A mule.

NARRATOR: He pointed to a brown, furry, four-legged, grunting beast. Well, a mule wasn't exactly the kind of companion she had in mind, but at least it was somebody to talk to.

DAUGHTER: Hi there, silly beast, I wonder if you were once a handsome prince changed into a mule by a wicked witch. If so, I could break the spell with a kiss. (kisses mule)

NARRATOR: She smacked the mule right on its lips. It was no use. The mule was a mule and had always been a mule.

The next day the old man instructed his daughter to take a bundle of sticks to the village.

DAUGHTER: A bundle of sticks? What for?

OLD MAN: How should I know. But somebody is always carrying a bundle of sticks around in fairy tales. You know that.

NARRATOR: So, the young girl took the bundle of sticks and decided to ride her trusty mule into the village. But something very strange happened. Unknown to her, the moment she climbed onto the mule's back *POOF* she turned into a beautiful maiden. You know the type: blond hair, blue eyes, a figure like she spends her days doing Jazzercise.

Anyway, when she reached the village, (insert whistles and catcalls) she could hardly believe her eyes, for all the young men, instead of laughing and throwing mud at her, bowed, tipped their hats, and made catcalls. She was still trying to figure it out when a handsome young prince rode up to her on a snow-white horse.

PRINCE: Ah, fair ladyl You are truly the most lovely beauty in the land.

DAUGHTER: (batting her eyes) Why, my young prince, are you nuts or sumpthin'?

PRINCE: With your permission, I should like to call upon you tonight. How about when the clock strikes the hour of eightish?

NARRATOR: Flushed with excitement, the girl raced home; but when she arrived and stepped off her mule, *POOF* she immediately returned to her fat little ugly self. That night, promptly at eightish o'clock, the prince, sitting astride his white charger, knocked on the door.

PRINCE: (prepares himself and knocks regally)

DAUGHTER: (opens door and smiles)

NARRATOR: A crooked-toothed smile -- one that made chopped yak liver seem appealing –

DAUGHTER: Hellooooo!

PRINCE: (with a hard to conceal facial reaction) Um . . .

NARRATOR: Said the prince, who at that moment was desiring a bit of Pepto-Bismol, or the medieval equivalent.

PRINCE: Is your sister at home?

DAUGHTER: I don't have a sister.

PRINCE: Your aunt then.

DAUGHTER: I don't have an aunt.

PRINCE: (growing more frantic) Your cousin? Your best friend? Your babysitter?

DAUGHTER: What are you talking about? I live here alone with my father.

PRINCE: (makes a break for it)

NARRATOR: Figuring he had found the wrong house, the prince galloped quickly off on his white steed. The poor girl was left standing at the door, brokenhearted and trying to understand what had gone wrong.

The following day, her father again asked her to go into the village. This time to pick up a bundle of sticks.

OLD MAN: (patting her kindly on her head) It'll take your mind off your ugliness.

NARRATOR: No sooner had the girl climbed on the mule's back than *POOF* once again she changed into a beautiful maiden.

On the way to the village, she chanced to pass a clear, still pool of water. Looking into it, she saw her reflection and was shocked to see she was now very beautiful. She jumped off her mule for a close look and *POOF* instantly she changed back into her former ugly self. And then, she suddenly realized what had happened.

DAUGHTER: I get it now!

NARRATOR: She said out loud to no one in particular, as people in fairy tales sometimes do.

DAUGHTER: This is a magic mule. As long as I sit on this beast, I'm a beauty!

NARRATOR: The girl jumped back onto the mule, and *POOF* beautiful again. And the beauty and the beast dashed to find the prince. When he saw her coming, he rode up to her on his gallant steed.

PRINCE: Ah, lovely beauty, I have found you again. Please say you will be mine so that we may be married.

DAUGHTER: Yes, but on one condition: That I remain on my mule at all times.

NARRATOR: Of course, this seemed like a strange request, but the prince agreed.

PRINCE: So be it, my love. And so that we start off on the right foot -- or on the right hoof -- I shall stay on my horse as long as you stay on your mule.

NARRATOR: And thus they were married by a priest, who delivered the sermon on a donkey. As the years went by, the young girl was very happy, although the poor mule did get a bit of a backache. And true to his word, the prince also stayed on his horse. And as any good husband would, he took her dancing every Saturday night at the palace, where they were the most striking couple on the dance floor. Or actually, the most striking quadruple on the dance floor.

One day, as the girl rode in the garden *WOOSH* the wind blew off her bonnet. Not stopping to think, she hopped off her mule to get the hat and *POOF* she immediately turned into an ugly, disgusting hag again.

DAUGHTER: (adjusting her hat she transfroms from beauty to hag)

NARRATOR: Realizing her mistake, she scrambled to get back in the saddle again. But it was too late, for just then the prince rode up.

PRINCE: Pardon me, old hag. Have you seen my wife? Wait a minute, this is her mule!

DAUGHTER: (blushing and gulping) Yes. And I am your wife.

NARRATOR: She began to sadly confess the whole story to her husband, but instead of being angry . . .

PRINCE: (laughing and clapping for joy) Ha, ha, ha, ha. Yahoo! Yippee!

DAUGHTER: I don't get it. Are you happy to find out that I'm really ugly?

PRINCE: No! I'm happy to know that I can finally get off this blasted horse. You see, I'm only a handsome prince when I stay on him.

NARRATOR: And with that, the prince hopped off his horse and *POOF* he changed into one of the ugliest men ever to walk the earth. He was fat and short and bald and full of warts. His face looked like ten miles of bad road.

DAUGHTER: (gleefully) Ugh! You're uglier than me!

PRINCE: (they hug) We were meant for each other! Just think-no more saddle sores!

NARRATOR: And so, the ugly man and the ugly girl were able to live happily ever after.
```

---

## IC-1106: The Best Christmas Pageant Ever (Play)

- Title: The Best Christmas Pageant Ever (Play)
- Author (byline): Barbara Robinson
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: Aug 2009
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: BETH, CHARLIE, MOTHER, FATHER, LEROY, NARRATOR, IMOGENE, GLADYS, ELMER, MRS. SLOCUM, CLAUDE, RALPH, OLLIE, ALICE, REV. HOPKINS, MAXINE, MRS. MCCARTHY
- Teaser before the introduction: Yes
- Spoken words (computed): 1517
- Already set (do not supply): none

### Source block (context only)

```text
Author: Barbara Robinson
ISBN: 978-0573617454
Publisher: Samuel French, Inc.
Date (Month/Year): Aug 2009
```

### Introduction (context only: never use it for content warnings)

```text
The Best Christmas Pageant Ever by Barbara Robinson.
```

### Performance text (classify this)

```text
BETH: (Pg 1-3) The Herdmans were the worst kids in the whole history of the world. They lied and stole and cussed their teachers and took the name of the Lord in vain. There were six of them - Ralph, Imogene, Leroy, Claude, Ollie and Gladys - and they went through the Woodrow Wilson school like those South American fish that strip your bones clean . . . Stealing things and whamming kids . . . it was hard to get away from them. There was only one safe place.

CHARLIE: (offstage, singing happily and at a fast upbeat pace) Sweet hour of prayer, sweet hour of prayer, Because there are no Herdmans there. And Jesus loves us, as they say, Because he keeps them miles away. *

BETH: That's my little brother, Charlie.

MOTHER: It's a very practical sentiment. Charlie was black and blue all last year because he had to sit next to Leroy Herdman in school.

FATHER: Is he the worst one? Leroy? CHARLIE. They're all the worst one. Gladys isn't big, but she's fast, and she's mean, and she bites. Stay away from them. Go to church.

MOTHER: I'm glad to hear you feel that way. No arguments this year about the Christmas pageant. CHARLIE. I don't want to be in it! Nobody wants to be in it!

BETH: (Pg 5) Our Christmas pageant isn't what you'd call four-star entertainment. It's always the same old Christmas story with the same old Mary and Joseph . . . The Herdmans . . . That was Charlie’s fault.

CHARLIE: (Pg 8-9) Hey, Leroy, you give me back my lunch!

LEROY: Sure, kid, here. (hands him a lunch bag)

CHARLIE: (looks inside) You stole my dessert again! You know what? I don't care if you steal my dessert. I get all the dessert I want in Sunday school.

LEROY: (interested in this) Oh, yeah? What kind of dessert?

CHARLIE: All kinds. Chocolate cake and candy bars and cookies . . .

LEROY: You're a liar.

CHARLIE: . . . and ice cream, and doughnuts and cupcakes!

LEROY: (pause) ... Sunday school, huh?

NARRATOR: That was the wrong thing to tell Herdmans . . . and, sure enough, the very next Sunday there they were in Sunday school, just in time to hear about the Christmas pageant...

MOTHER: Today we're going to decide who will play the main roles in our Christmas pageant. (Pg 11-12) Now I want you to think about Mary . . . She was quiet and gentle and kind. The girl who plays Mary should be that kind of person. Who would like to volunteer for that part? (Imogene raises her hand) Did you have a question, Imogene?

IMOGENE: No, I want to be Mary . . . and Ralph, over there, he wants to be Joseph.

MOTHER: (taken aback) Oh. Well . . . I’ll just make a list of volunteers and then we’ll all decide who it should be. Now, who else would like to be Joseph? Raise your hands . . . please . . . any volunteers . . . (silence) Very well. Ralph Herdman will be our Joseph. Imogene has volunteered to be . . . (tiny break here, as if she can hardly bear to connect Imogene with Mary) . . . Mary. Janet? . . . Roberta? . . . . Alice? (silence)

GLADYS: What’s left?

MOTHER: (reluctantly) The Angel of the Lord . . .

GLADYS: I’ll be that. What is it?

MOTHER: (Pg 18-19) (Quoting scripture) And lo, the Angel of the Lord came upon them, and the Glory of

GLADYS: (Flinging her arms out) Shazam! . . . Out of the black night, with horrible vengeance, the Mighty Marvo . . .

MOTHER: This is the Angel of the Lord, who comes to the shepherds . . .

GLADYS: Out of nowhere, right? In the black night, right? Shazam!

ELMER: (Pg 13) (raising his hand) I don’t want to be a shepherd . . . Gladys Herdman hits too hard! ***** (phone conversations) ******

MRS. SLOCUM: (Pg 14-15) Vera? Irma Slocum. I just heard that Imogene Herdman is going to be Mary in the Christmas pageant, and I ... all six of them? MRS. ARMSTRONG. Imogene Herdman! ... What kind of a child is that to be Mary the Mother of Jesus? If I’d been around this never would have happened!

MRS. SLOCUM: . . . better nail down the church and lock up the silver service and hide the collection plates before they clean them out . . . *****

MOTHER: (mimicking Mrs. Armstrong) “If I’d been around, this never would have happened!” I'm going to make this the best Christmas pageant ever, and I'm going to do it with the Herdmans! After all, they raised their hands and nobody else did . . . ***** (pageant practice) *****

MOTHER: (Pg 24-25) . . . Music . . . . Shepherds . . . Music . . . Wise Men! (3 Herdmans slouch aimlessly down the aisle and up to the manger)

IMOGENE: (Pg 19) Well, it's about time somebody important showed up! If they're kings, they can get the baby out of the barn, and tell the innkeeper where to get off!

MOTHER: (ignoring this turn of plot) ... They were sent by Herod, who was ... well, he was the main king, and he wanted to find Jesus and have him put to death.

IMOGENE: My God! He just got born! They're gonna kill a baby?

MOTHER: Herod isn't in the play.

LEROY: He’s out to kill the baby, and he isn’t even in the play?

CLAUDE: (Pg 20) (warming to this scenario) No . . . I know ... Joseph gets the shepherds together and they go wipe out Herod! (He makes a machine gun gesture.)

IMOGENE: And I run away with the baby till the fight's over!

RALPH: Somebody ought to fix the innkeeper . . . Gladys, you wipe out the innkeeper!

GLADYS: (Pg 21) (happily) Yeh! ... Zap!

OLLIE: What's the name of this play?

GLADYS: I know a name! . . . I know a name! I'd call it . . . Revenge at Bethlehem!

BETH: Revenge at Bethlehem! The Herdmans thought the Christmas story came right out of the F.B.I. files! At least they picked out the right villain- it was Herod they wanted to gang up on and not the baby Jesus. (As the Wisemen approach IMOGENE holds up the doll by the back of the neck, waving it in the air.)

IMOGENE: (Pg 25) I've got the baby here . . . don't touch him! I named him Jesus!

MOTHER: (hurrying on stage) No, no, no! You don't say ... (nerves fraying away) ... anything! Mary doesn't say anything. No one says anything! Mary and Joseph make a lovely picture for us to look at while we think about Christmas and what it means! ... Now, put the doll back.

IMOGENE: (disgruntled) I don't get to say anything . . . some angel tells me what to call the baby . . . I would have named him Bill.

GLADYS: (Pg 26) (yells at the Shepherds) Unto you [Bill] is born!

IMOGENE: Unto me! Not them, me! I'm the one that had the baby!

RALPH: (Pg 17) (Not so much trying to shock, as he is pleased to understand something.) Pregnant! She was pregnant! (There is much giggling and tittering.)

ALICE: It's better to say 'great with child'. I'm not supposed to talk about people being pregnant, especially in church. ****** Scene ******

REV. HOPKINS: (Pg 28-29) The whole church is in an uproar. Jesus said, "Suffer the little children to come unto me", but I'm not sure he meant the Herdmans . . . Don't you think we should cancel the pageant? Every one seems to think it's going to be a . . . a . . .

MOTHER: Disaster? (Obviously, that's the word he had in mind.) Well, they're wrong! ... It's going to be the best Christmas pageant we ever had!

REV. HOPKINS: But . . . I don't think anyone will come to see it!

BETH: I didn't think so, either, and neither did Charlie . . . but we were wrong. On Christmas Eve the church was jammed full. Everybody came . . . to see what the Herdmans would do. ***** (the night of the pageant) *****

MOTHER: Oh, I don't have any idea what's going to happen tonight! We've never once gone through the whole thing, and the Herdmans still think it's some kind of spy story. It may be the first Christmas pageant in history where Joseph and the Wise Men get in a fight and Mary runs away with the baby.

BETH: (Pg 30) It's just going to be awful, you know. They look like trick or treat- all dirty and fastened together with safety pins and wearing their mouldy old sneakers . . . Mary and Joseph, I mean. They look like refugees or something.

FATHER: Well . . . that's what they were . . . Mary and Joseph. They were refugees, in a way. They were a long way from home, didn't have any place to stay, didn't know anybody. They were probably cold and hungry and tired . . . and messy. (Beth is struck by the sense of this new idea) **** Cut to the actual performance already in progress *****

MAXINE: (Pg 33-36) (Narrating) . . . And in that region, there were shepherds in the field, keeping watch over their flocks by night. And an Angel of the Lord appears to them and said . . . (Gladys roars on stage with her message)

GLADYS: Hey! Hey! Unto you a child is born! . . . It’s Jesus, and he’s in the barn . . . Go see him! (the Shepherds hesitate) Go on , he’s over there . . . Go on!

MAXINE: There came Wise Men from the East to worship him.

LEROY: (singing) We Three Kings of Orient Are . . .

ALICE: They look awful, too. And what’s that Leroy’s got?

BETH: (craning her neck to see) It’s . . . it’s a ham!

ALICE: Bet they stole it!

BETH: No . . . I think it’s the ham from their welfare basket. It’s the only thing they ever gave away in their whole life.

MAXINE: The Wise Men and the Sheperds departed, praising God for all they had seen and heard. But Mary kept all these things and pondered them in her heart. (Imogene takes the doll from the manger and holds it. She puts it up on her shoulder, as if to burp it. She is crying)

ALICE: (in reverent awe) Look . . . Mary’s crying. ****** After the pageant *****

MRS. MCCARTHY: Could you believe that was Imogene Herdman? And all the rest of them? This was the best Christmas pageant we ever had, and I'm not sure why, but I think it was them. There was just something . . . different.

MRS. SLOCUM: Well, the Angel of the Lord was different!

MRS. MCCARTHY: Yes, but you know, I liked that! Had lots of spirit. Sometimes you can't even hear the Angel of the Lord.

MRS. SLOCUM: Well... it did seem . . . real. (They exit.)

BETH: It did seem real, as if it might have happened just that way. We all thought the pageant was about Jesus, but that was only part of it. It was about a new baby, and his mother and father who were in a whole lot of trouble - no money, no place to go, nobody they knew. Because of the Herdmans, it was a whole new story - Imogene, burping the baby, and the Wise Men bringing such a sensible present. After all, they couldn't eat frankincense! And even Gladys-"He's in the barn. Go see him" But I guess it wasn't like that for Imogene. For her, the Christmas pageant turned out to be all wonder and mystery, as if she just caught on to what Christmas was all about.

GLADYS: (Pg 38) (offstage) Heyl . . . (She runs on stage and points at the audience.) Hey, unto you a child is born!
```

---

## IC-1107: The Best Daddy

- Title: The Best Daddy
- Author (byline): Shel Silverstein
- Work: An Adult Evening of Shel Silverstein
- Publisher: Dramatists Play Service
- Publication date as stated: March 2003
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: LISA, DAD
- Teaser before the introduction: Yes
- Spoken words (computed): 908
- Already set (do not supply): none

### Source block (context only)

```text
Author: Shel Silverstein
Book: An Adult Evening of Shel Silverstein
ISBN: 978-0822218739
Publisher: Dramatists Play Service
Date (Month/Year): March 2003
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: Sarcasm is an interesting verbal technique, often lost on the young . . . In this scene we meet Lisa and her father on one of the most exciting days of the year for any child . . . her birthday.

ACTOR: Unfortunately, this birthday surprise is a little more than little Lisa has bargained for.

TOGETHER: Shel Silverstein’s The Best Daddy

ACTRESS: (whispers) But you can decide for yourself.
```

### Performance text (classify this)

```text
LISA: Okay?

DAD: A little further.

LISA: Here? Can I open my eyes?

DAD: Hold my arm.

LISA: I’m going to bump into it.

DAD: You won’t bump into anything. Keep your eyes closed. Now hold my arm, a couple more steps here.

LISA: Can I look now?

DAD: All right. . .open your eyes right. . . now.

LISA: Is that him, there?

DAD: That’s right.

LISA: Why is he covered with a blanket?

DAD: Well, he. . .

LISA: He doesn’t look like a pony.

DAD: Well, he is -- a thoroughbred gelding 350-dollar Shetland pony.

LISA: Is he laying down?

DAD: Um yes.

LISA: Why is he laying down? Is he sick?

DAD: Pure strain Kentucky-bred Shetland

LISA: Why is he laying down?

DAD: Lisa. . .I didn’t want to tell you this. . .

LISA: Why is he laying down? He is sick, he is.

DAD: He’s dead.

LISA: He. . .he’s dead?

DAD: It’s a helluva thing to have to tell your daughter on her birthday.

LISA: Dead? A dead pony?

DAD: We’ve got to face the facts.

LISA: You. . .you got me a dead pony for my birthday?

DAD: I didn’t get you a dead pony for your birth. . .

LISA: What happened to him?

DAD: Lisa, I’m going to be honest with you. . .

LISA: What happened to my pony?

DAD: You’re thirteen years old now and I’m going to talk to you like an adult.

LISA: What happened to my pony?

DAD: I shot him.

LISA: Y-you shot him?

DAD: About an hour ago, but hear me out.

LISA: Y-you shot my pony? You. . .you shot my birthday pony?

DAD: I told you not to get excited, didn’t I? Answer me, did I or didn’t I not say, “Don’t get too excited. . .”

LISA: Why did you shoot my pony?

DAD: I did not shoot your pony. He wasn’t your pony when I shot him. You didn’t even know he existed. He was a pony.

LISA: Why did you shoot my pony?

DAD: He bit me.

LISA: But you didn’t have to shoot him. You didn’t have to. . .he’s only a little pony. He didn’t know what he was doing.

DAD: You weren’t there, you don’t know the situation.

LISA: My pony is dead. I’m thirteen years old today and you gave me a dead pony for my birthday.

DAD: I told you, he bit me.

LISA: But you gave him to me anyway. You took me out here to show me a dead pony?

DAD: Well, I thought about that. I thought, well, if I take her out here and show her a dead pony that will upset her, but if I don’t give her anything she’ll think I forgot her birthday.

LISA: What could be worse than getting a dead pony for your birthday?

DAD: Listen now, someday you’ll have children of your own. I never shot a pony before. I want you to believe that, never in my life before today.

LISA: You hated my pony, you always hated him.

DAD: I didn’t always hate him, I never even. . .

LISA: You did. You hated him because you knew I love him.

DAD: When I saw him I liked him, he was cute.

LISA: You knew he loved me and he could show his feelings and you couldn’t stand that. Oh no ‘cause you could never love anyone. You’re all bottled up. You keep all your feeling all bottled up. And he could show his love. He could swish his tail and toss his head, and lick my hand when I gave him sugar. And late at night when I’d ride him bareback through the gray mountains. . .

DAD: You never rode him – I just bought him. . .

LISA: You didn’t know. I used to sneak out late at night when you thought I was sleeping. I’d climb out of my bedroom window and I’d run to the pasture. . .

DAD: Pasture? What pasture?

LISA: And he’d smell my scent and come galloping toward me, and I’d leap onto his back, and we’d go galloping over the moonlit moor. . .

DAD: Moonlit moor?

LISA: . . .with the wind in my hair. And now he’s dead. You killed my pony. You killed Black Thunder.

DAD: Black Thunder?

LISA: You killed the only thing I ever loved.

DAD: I didn’t.

LISA: You did.

DAD: I didn’t

LISA: You did. You said you did.

DAD: APRIL FOOL!

LISA: April Fool? But, but it’s not April, it’s my birthday.

DAD: BIRTHDAY FOOL!

LISA: You mean Black Thunder’s not dead? Then who is under that blanket?

DAD: Not “who” but “what.”

LISA: Wh-what? Wh-what’s under there?

DAD: Three guesses.

LISA: I. . . I don’t know. You’re cruel. You’re the cruelest daddy in the whole world.

DAD: Three guesses.

LISA: A. . .a candy bar?

DAD: Uh-uh

LISA: A. . .a turtle, a bit gigantic turtle?

DAD: Nope, two down, one to go.

LISA: A. . .a. . .a rubber raft?

DAD: No. . .

LISA: What then, what is it?

DAD: It’s your sister!

LISA: What?

DAD: It’s your big fat sister!

LISA: Cathy? It’s Cathy?

DAD: Big fat Cathy!

LISA: Why is she hiding under there? And you said it was a what, not a who, Cathy is a who.

DAD: Not exactly.

LISA: Not exactly? Cathy? Ca-Cathy?

DAD: It’s a. . .what. . . it’s Cathy’s body.

LISA: Cathy’s body?

DAD: She’s the one that bit me.

LISA: You shot Cathy?

DAD: Teeth like a damn wild grizzly.

LISA: You gave me my dead sister’s body for a birthday present? First you tell me my pony is dead, and now you tell me you shot my favorite sister? You are the cruelest meanest most vicious. . .

DAD: DOUBLE APRIL FOOL!!

LISA: Double April Fool?

DAD: It’s not your sister. I wouldn’t shoot your fat little sister. Three more guesses!

LISA: (Crying) I’m not guessing anymore. You ruined my birthday. You’re a mean, cruel --

DAD: It’s the motorcycle you wanted!

LISA: The Honda?

DAD: Uh-huh.

LISA: The red one?

DAD: Uh-huh.

LISA: Really and truly?

DAD: Mmm-hmmm.

LISA: Oh Daddy. Daddy, you’re the bestest daddy in the whole wide world!
```

---

## IC-1108: The BFG

- Title: The BFG
- Author (byline): Roald Dahl (Adapted by David Wood)
- Work: Not specified
- Publisher: Puffin Books
- Publication date as stated: Feb 2007
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR 1, MRS. CLONKERS, BFG, SOPHIE, BLOODBOTTLER, BONECRUNCHER, CHILDCHEWER, GIZZARDGULPER, QUEEN, HO AIR FORCE, HO ARMY, HO AIRFORCE, BOTH
- Teaser before the introduction: Yes
- Spoken words (computed): 1295
- Already set (do not supply): none

### Source block (context only)

```text
Author: Roald Dahl (adapted by David Wood)
ISBN: 978-0142407929
Publisher: Puffin Books
Date (Month/Year): Feb 2007
```

### Introduction (context only: never use it for content warnings)

```text
Sophie’s life as an orphan is not exactly what dreams are made of. That is until one night when a big friendly giant makes his way into town during the witching hour to blow dreams into the minds of sleeping children. He whisks Sophie away to Giant Country. Why? Because humans can’t know that Giants exist. And it’s there that the adventures begin. The BFG isn’t like the other Giants, who are not at all friendly. Ultimately our hero, Sophie, with the help of the BFG and the Queen, saves the day and the children of England too!

The BFG by Roald Dahl adapted by David Wood
```

### Performance text (classify this)

```text
NARRATOR 1: (Pg 17-20) It was late at night. . . (owl hooting noise) in the orphanage dormitory, Sophie couldn't sleep. (acting out the story as she tells it) A brilliant moonbeam was shining right on to her pillow. She slipped out of bed to get a drink of water.

MRS. CLONKERS: Sophie! Back to bed this instant. You know the rules.

NARRATOR 1: Mrs Clonkers! Sophie went back to bed. She tried very hard to doze off. The time ticked by. (tick-tock noise) The house was absolutely silent. Perhaps, thought Sophie, this is what they call the witching hour, that special moment in the middle of the night when everyone is in a deep, deep sleep, all the dark things come out from hiding and have the world to themselves. She crept to the window. And suddenly she saw. . . a giant.

(BFG enters in a cloak and carries a suitcase; he acts out the narration) He stopped at the house opposite, bent down to look in a bedroom window and then . . .

BFG: (BFG opens a suitcase, take out a jar and pour its contents into the end of a horn-like trumpet. Blows through it into an imaginary window. Turns and notices Sophie - Gasps)

NARRATOR 1: He saw Sophie. (acting out the story as she tells it) She pulled back from the window, flew across the dormitory and jumped into her bed and hid under the blanket, tingling all over.

BFG: (Peeps in the window and with a growl, pushes a hand through and snatches SOPHIE, holding her up high)

SOPHIE: Aaaaaaaah! (BFG Begins slow-motion, on-the-spot running)

NARRATOR 1: Running, striding, leaping through the night. Over fields, over hedges, over rivers, each stride as long as a tennis court. Faster, faster, feet scarcely touching the ground. Over oceans, over forests, over mountains . . .To a land unknown to human beings.

BFG: (Pg 27-32) (Standing over SOPHIE) Ha! What has us got here? (He looks carefully at SOPHIE. At first, he should not appear very friendly)

SOPHIE: (Nervously) Where am I?

BFG: This is my cave.

SOPHIE: Why did you snatch me and bring me here?

BFG: Because you saw me. If anyone is ever seeing a giant, he or she must be taken away hipswitch.

SOPHIE: Why?

BFG: Human beans is not believing in giants, is they? Human beans is not thinking giants exist.

SOPHIE: I do.

BFG: Ah, but that is because you has seen me. If I hadn't snitched you, you would be scuddling around yodelling the news on the telly-telly bunkum box that you were actually seeing a giant, and then a great giant-hunt, a mighty giant look-see, would be starting up all over the world, and human beans would be trying to catch me and put me in the zoo with all those squiggling hippodumplings and crocadowndillies.

SOPHIE: So what's going to happen to me now? (Gasping) Please don't eat me!

BFG: (Bellowing with laughter) Just because I is a giant, you think I is a man-gobbling cannybull! No! You is lucky. If one of the other giants is snitching you, they is crunching you up for sure. Bones crackety-crackety-cracking. Gobble, gobbledy, gone!

SOPHIE: Other giants? You mean there are more of you?

BFG: Of course! This is Giant Country! (He picks up SOPHIE) Be peeping out over there, little girl, and be seeing a brain bogglingsome sight. (They peep outside)

SOPHIE: What on earth are they doing?

BFG: Nothing. They is just waiting for the night to come. Then they will be galloping off to places where human beans is living to find chiddlers to guzzle for their suppers.

SOPHIE: Where?

BFG: All over the world. That's the Bonecruncher. He is thinking Turkish chiddlers is juiciest chiddlers. They is tasting of Turkish delight!

SOPHIE: Of course. Who's that big, fierce one?

BFG: That's the Fleshlumpeater. He’s fancying getting his chompers round a handful of chiddlers from Wellington! That’s the Bloodbottler. He is thinking the English chiddlers is tasting ever so wonderfully of crodscollop.

SOPHIE: I'm not sure I know what that means.

BFG: Meanings is not important. You will be coming to an ucky-mucky end if any of them should ever be getting his gogglers upon you. You would be swallowed up like a piece of frumpkin pie, all in one dollop. (They return inside the cave) There. You is safe in here.

SOPHIE: (Pg 33-35) I think eating children is horrible.

BFG: I has told you. I is not eating chiddlers. Not I! I is a freaky giant! I is a nice and jumbly giant! I is the BFG.

SOPHIE: The BFG?

BFG: The Big Friendly Giant! What is your name?

SOPHIE: My name is Sophie.

BFG: How is you doing, Sophie? (He gently shakes hands with SOPHIE) Your poor mother and father. By now they must be jipping and skumping all over the house shouting, 'Hallo, hallo, where is Sophie gone?'

SOPHIE: I don't have a mother and father. They died when I was a baby.

BFG: You is a norphan? Oh you poor little scrumplet. You is making me sad.

SOPHIE: Don't be sad. No one at the orphanage will be worrying much about me.

BFG: Was you happy there?

SOPHIE: I hated it. Mrs Clonkers locked me in the cellar once for not folding up my clothes.

BFG: The filthy old fizzwiggler! You is making me sadder than ever. (he sobs)

SOPHIE: Don't cry, BFG. Please. (The BFG recovers a little) Listen, we can't just sit here and let any more children be eaten. We've got to stop those brutes. It’s up to us! We’ve got to save the children of the world!

BFG: Us? Redunculus and umpossible. (He takes out a bottle of liquid)

SOPHIE: (Pg 52-55) (Reading from the bottle) Frobscottle?

BFG: I drink it lots. Delumptious, fizzy frobscottle! (He removes the stopper. There is a fizzing sound)

SOPHIE: Hey, look! It's fizzing the wrong way! In our fizzy drinks, like Coke and Pepsi, the bubbles go upwards.

BFG: Flushbunking rubbsquash! Upgoing bubbles is a catasterous disastrophe.

SOPHIE: But why?

BFG: Listen. When you is drinking this cokey drink of yours, it is going straight down into your tummy. And the bubbles is going also into your tummy. If the bubbles is fizzing upwards, they will all come swishwiffing up your throat and out of your mouth and make a foulsome belchy burp!

SOPHIE: That's often true. But what's wrong with a little burp now and again? It's sort of fun.

BFG: Burping is filthsome. Us giants is never doing it.

SOPHIE: But with your drink. . .

BFG: Frobscottle.

SOPHIE: With frobscottle, the bubbles in your tummy will be going downwards and that could have a far nastier result. They'll be coming out some where else with an even louder and ruder noise.

BFG: A whizzpopper! Us giants is making whizzpoppers all the time! Whizzpopping is a sign of happiness. It is music in our ears!

SOPHIE: But it's. . . it's rude!

BFG: But you is whizzpopping, is you not, now and again?

SOPHIE: Everyone is . . . whizzpopping. Kings and queens, even little babies. But where I come from, it's not polite to talk about it.

BFG: Redunculous! If everyone is making whizzpoppers, then why not talk about it? Now, let's be having a swiggle and seeing the result! (The BFG drinks from the bottle. Pauses. Then ecstasy fills his face. A very loud whizzpopper nearly shoots him in the air) Whoopee! (And another) Wheeeeeeee! (SOPHIE laughs, in spite of herself) Have some. Go on. It's gloriumptious!

SOPHIE: It's lovely. (Suddenly a succession of whizzpoppers – Sophie giggles) Wheee! Wheeeeee! (suddenly a roar of the other giants startles them)

BLOODBOTTLER: (Pg 76-78) ‘Tis the witchy hour. And I is starveling!

BONECRUNCHER: Let us go guzzle human beans! (Both cheer)

CHILDCHEWER: Let us fluchbunk to England!

GIZZARDGULPER: I is fancying a few nice little English chiddlers! (Both cheer)

SOPHIE: We’ve got to stop them. We must warn everyone in England they’re coming!

BFG: Redunculus and um-possiple. I is never showing myself to human beans. They will be putting me in the zoo with all the jiggyraffes and cattypiddlers. And they will be sending you straight back to the norpahage. Grown-ups is all squifflerotters and grinksludgers.

SOPHIE: (thinking) I’ve got it! Listen, BFG, we’ll go to the Queen and tell her about the giants. She’ll do something, I know she will. ******Buckingham Palace*******

QUEEN: (Pg 107) (Fanfare. Enter the Queen) It’s been a rough morning. (Pg 106) Sophie, you have told me of your visit to Giant Country and of the giants’ ghastly night-time children-eating raids. (she claps her hands) (Pg 108-109) Summon the Head of the Army and the Head of the Air Force immediately! (they enter) Good morning, gentleman. You’ve read about the disappearing children? (pause) They were eaten. (pause) By giants.

HO AIR FORCE: Giants?

HO ARMY: No such fellas, Your Majesty.

HO AIRFORCE: Except in fairy-tales. (Both laugh)

QUEEN: (Pg 110-112) Gentleman, allow me to present the Big Friendly Giant. (she indicates behind them)

BOTH: (turn; see the BFG) Aaaaaah! (cling to one another in terror) A giant!

QUEEN: Indeed. Luckily a friendly one. His colleagues are not. Tonight those bloodthirsty brutes will be galloping off to gobble up [more] unfortunate wretches. They have to be stopped. Fast. They must be brought back. Alive.

HO AIR FORCE: Alive? They’d knock us down like ninepins!

BFG: Keep your skirts on! I has the answer. Every afternoon all these giants is lying on the ground snoozling in the Land of Noddy. All you has to do is creep up on them and tie them up.

HO AIR FORCE: But how do we get the brutes back here?

BFG: You is having belly poppers, is you not?

HO AIR FORCE: Are you being rude? (BFG lets loose with a wizzpopper)

SOPHIE: (with a disapproving look to BFG) He means helicopters.
```

---

## IC-1109: The Bible: The Complete Word of God (Abridged)

- Title: The Bible: The Complete Word of God (Abridged)
- Author (byline): Adam Long, Reed Martin and Austin Tichenor
- Work: Not specified
- Publisher: Broadway Play Publishers
- Publication date as stated: Dec 2000
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: VOICE OVER, AUSTIN, REED
- Teaser before the introduction: Yes
- Spoken words (computed): 1156
- Already set (do not supply): none

### Source block (context only)

```text
Author: Adam Long, Reed Martin and Austin Tichenor
ISBN: 978-0881451825
Publisher: Broadway Play Publishers
Date (Month/Year): Dec 2000
```

### Introduction (context only: never use it for content warnings)

```text
Hello, I’m _______________ . . . and welcome to the ________________Speech Tournament and today’s performance of The Bible: The Complete Word of God (abridged) by Adam Long,
```

### Performance text (classify this)

```text
VOICE OVER: (Pg 1-2) (off stage) In the beginning, there was . . . chaos. Everything was void. God saw all that emptiness . . . (hums a song rising to a crescendo and crash) Let there be light! Adam stands aghast in the fig leaf position, covering his significant body part – music rises again to a crash – Actor stands aghast as Eve, covering her significant body parts.

Reed Martin and Austin Tichenor.

AUSTIN: (Pg 4-6) I’ll be taking you on a marvelous, spiritual journey. A quest, if you will. A journey towards enlightenment! I present to you, The Bible – the Greatest Story Ever Accepted as Fact. And I’ll explain it all -- Make the unknown known. . . The inexplicable plicable.

It’s important to point out that although this show is about the Bible, it is not about any particular religion. That’s right. It is not my intention to slander Christians, or Jews, or Muslims . . . Or Buddists or Druids or agnostics . . . Or Catholics or cult members of any kind. It’s not what I want to do . . . No, why would you . . . I have done extensive research on (holds up a book) The King James Edition of the Holy Bible. (Pg 8-9) (reading from the great book) And the Lord God caused a deep sleep to fall upon Adam, and he slept. And God took one of Adam’s ribs and made he a woman, and brought her unto the Man.

REED: (as Eve) Good morning! (takes a bite of an apple) Let the downfall of Man begin! Nyah-ha-ha!!

AUSTIN: (as narrator - takes a bite of the apple and continues reading with his mouth full) And God looked down on Adam and Eve and knew they had eaten of the forbidden fruit. (tosses apple way with a horrified look on his face) (Pg 10) This brings us to Chapter Five of Genesis – The Genealogy of Adam.

(Pg 12-13) (rapping) . . . Begattin’, begattin’ / Everywhere begattin’ / Makin’ babies happen / ‘Cause back then there was nothing else to do! *****Scene change****

REED: (Holding aloft a replica of the Ark) The Ark. Noah’s Ark. What I have here in my hands is an exact replica of Noah’s Ark that I have personally carved over the last nine years out of genuine gopherwood I imported from the Middle East.

AUSTIN: (applauding over the last few words and a bit of patronizing) Wow! Good Job! (Yawn) So . . . let’s move on!

REED: What about Noah’s Ark?

AUSTIN: We just did it.

REED: We didn’t DO Noah’s Ark. We introduced Noah’s Ark. But we didn’t DO Noah’s Ark. (Austin rolls his eyes) (Pg 14) There’s a lot of unanswered questions about Noah’s Ark . . .

AUSTIN: Like what?

REED: Were there dinosaurs on the Ark?

AUSTIN: (frustrated) Yes!

REED: They’re not mentioned in the Bible

AUSTIN: There’s a lot of things not mentioned in the Bible. Handguns . . . telephones . . . computers . . .

REED: Wait a minute! Computers were on Noah’s Ark?

AUSTIN: No. Don’t be silly. Computers were in the Garden of Eden.

REED: Ohhhh . . . yeah . . . Eve had an Apple. (To Audience – back to his Ark) Now if you look very closely, I think you can see . .

AUSTIN: Stop it, Reed, you’re boring everybody.

REED: (taking offense) No, I’m not.

AUSTIN: Yes, you are. The story of Noah’s Ark is sooooo overdone. Everybody knows it, and besides, it probably never happened.

REED: (Pg 15) (shocked) Never happened?!? Never happened?!? Why, they might as well say that the whole Bible never happened! What do they think is up there on Mount Ararat, anyway – The titanic? They might as well strip me of my childlike faith and innocence. They might as well tell all of you that I still wet the bed!

AUSTIN: You still wet the bed? Eeeuwwww!

REED: Stop listening to my inner monologue! (Pg 24) Now we move on the book of Exodus, where we join Moses . . .

AUSTIN: (Pg 25-26) (as Moses) All right, listen up, children of Israel. I’ve got some good news and some bad news. The good news is, I got Him down to ten. (response) The bad news is, adultery is still one of ‘em. (response) As for the commandments I talked God out of . . . Number 1: Seventies fashions were ugly then and they’re ugly now! Number 2: Thou shalt let the poor fend for themselves. Oh, sorry. No, that’s the Republican agenda. Number 3: *Stuff* happens Number 4: (From the Appendix) Thou shalt not “SHOW ME THE MONEY!” and . . . Number 5: The English shalt not give back Northern Ireland until the Irish take back “Riverdance”! (doing a rendition of Riverdancing) G’night, everybody!

REED: And there was great rejoicing and great balls of fire. And in his hundred and twentieth year, Moses did die. *****Scene*****

AUSTIN: (Pg 46) You ready? The Wise Men!

REED: (Pg 47) (looking to the heavens) Of all the nights for the Middle East to be overcast.

AUSTIN: We better hurry, or we won’t be there in time for Christmas. He’s gonna love what I got him.

REED: I don’t know, mine’s pretty valuable.

AUSTIN: I’ll show you mine, you show me yours. One, two, three! (shows the gift)

REED: Baseball mitts! (Pg 48) I thought you were getting him gold.

AUSTIN: I thought you were getting him frankincense.

REED: (Pg 49) Look! A shooting star! The sky’s cleared up! Let’s go!

AUSTIN: Wait, I’m confused. What are we supposed to do when we get there?

REED: We worship the Christ child and then we give him his birthday presents.

AUSTIN: Wow – his birthday falls on Christmas? Tough break!

REED: Follow me! (arrives at the stable) (Pg 51) (as Mary) Joseph, it’s time!

AUSTIN: (as Joseph) Oh, my gosh! Quick towels and hot water! (he holds the screaming baby aloft)

REED: (as Mary) We will name him Jesus!

AUSTIN: (singing) We wish you a merry Christmas! We wish you a merry Christmas! We wish you a merry Christmas! Our dear son of God! . . . . For he’s a jolly good savior, For he’s a jolly good savior, For he’s a jolly good savior – Who Peter will deny! *****Scene*****

AUSTIN: (Pg 56-57) (as Joseph – waving a piece of paper) Mary, Mary! Look what I found in my carpentry shop! It’s a note from Jesus.

REED: (as Mary) Oh, dear . . . (reading) “Dear Mother and Fa . . . Joseph . . .” Sorry, honey.

AUSTIN: That sucks!

REED: He loves you.

AUSTIN: (sulking) He loves everybody! Read the note. . .

VOICE OVER: “Dear Mother and Joseph, I just don’t feel I have what it takes to be a good carpenter. So I’m leaving to wander in the wilderness for forty days and forty nights to, well, get my head together. Don’t worry, I’ll be fine. Love, your miracle, Jesus.”

REED: Can you earn a living as a Messiah?

AUSTIN: No, that’s why I wanted him to go into his father’s business.

REED: He is.

AUSTIN: No, my business! *****Scene*****

AUSTIN: (Pg 69-71) And now, as we race through the last half of the New Testament, we are proud to present to you the adult life of Jesus! Jesus raises Lazarus from the dead! (pantomimes a Zombie walk) Jesus feeds the multitudes with bread and fishes!

REED: (throws fish to the audience) [And you get a fish . . . and you get a fish . . . Everyone gets a fish!]

AUSTIN: Jesus performs miracles! (makes loops with his thumbs and forefingers like an OK sign. He puts them behind his head and when he reveals them, they are intertwined. He puts them behind his head again and then reveals they are no longer connected) (Pg 74-75) Jesus is crucified! (realizes he’s said this with too much enthusiasm, he tries again with sadness) Jesus is crucified.

(Very, very simply) And the soldiers led Jesus away and forced a crown of thorns onto His head. They crucified him, and a great darkness fell over the land. Then came the most beautiful aspect of the entire New Testament . . . Jesus is resurrected! (Rejoice!) *****Scene*****

AUSTIN: (Pg 76-77) Now we have a very special treat for you. As you know, there are so many great musicals based on the Bible. You know, like Jesus Christ Superstar . . . (struggling to name another) Oklahoma! So in the spirit of those musicals, we’d like to present to you, the final book of the Bible in a little something that we like to call . . . REVELATION -- THE MUSICAL!

(Singing and dancing) Oh, the saved are surrounded with love / And removed to the heavens above / And the damned are in a bit of a jam . . . That’s Armageddon! Oh, the bad know they’ve made a mistake / They are cast into a fiery lake / It’s a goof, unless they are fireproof . . . That’s Armageddon!

REED: (Pg 78-79) Yes, Armageddon – the end of the world. And with the end of the world comes the end of our little trip through the Bible . . . Aaahhhhhh – men!!
```

---

## IC-1110: The Big Bang

- Title: The Big Bang
- Author (byline): Boyd Graham
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: 2001
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: JED, BOYD, VOICE OVER, ADAM, EVE, COLUMBUS, ISABELLA, MINNEHAHA, POCAHONTAS
- Teaser before the introduction: Yes
- Spoken words (computed): 1108
- Already set (do not supply): none

### Source block (context only)

```text
Author: Boyd Graham
ISBN: 978-0573627545
Publisher: Samuel French, Inc.
Date (Month/Year): 2001
```

### Introduction (context only: never use it for content warnings)

```text
(no introduction)
```

### Performance text (classify this)

```text
JED: Good evening everyone and welcome prospective investors. My name is Jed and this is my partner, Boyd.

BOYD: Shalom.

JED: Before we begin, we’d like to take a moment to thank Dr. and Mrs. Sid Lipbalm for the use of their beautiful apartment. Unfortunately, they’re unable to be with us tonight.

BOYD: They left on a two week trip to Israel.

JED: Now, you all understand that this is a backer’s audition.

BOYD: Which is a presentation of a Broadway musical, which we have written, hopes that some of you may be interested in incesting.

JED: In –VESTING.

BOYD: Investing, right.

JED: It encompasses the entire history of civilization. Budgeted at 83 million dollars. Twelve hours of pure entertainment. Showing in 4 three-hour installments. Of course, we can’t do the show in its entirety. So tonight we’ll be doing highlights. Act 1, Scene 1

BOYD: A bare stage. We begin in darkness. The whole thing started with one

JED: He said one.

BOYD: Big

JED: Oh, so big

BOYD: One . . . . Big . . . . Bang!

The Big Bang by Boyd Graham. In the beginning . . . all was silent . . . . (Give 5 seconds of silence)

VOICE OVER: A voice from the heavens shatters the silence, “Let there be light!” A creature of strength, pride and acute manlitude ready to face his destiny.

BOYD as ADAM: Hi, my name is Adam. I was made from a pile of dust.

JED as EVE: Then Adam ordered a madam with a thirty-eight inch bust. God said . . .

BOYD as GOD: Play all day in the sunshine and you may stay in your birthday suit.

BOYD as ADAM: Free food and frontal nudity. We’re always nude and the food is free.

JED as EVE: Free food and frontal nudity is not what it’s cracked up to be. We’re bored with our anatomy and sick of all this fruit.

ADAM: Bananas for supper again? I’m going for a walk.

EVE: That’s the third time he’s stomped out on me this week. I bet he’s going to see his new girlfriend, the cheap chimp. (Pick an apple from the tree of knowledge)

SATAN (Serpent): Trouble in paradise? You know what to do. All the powers of the universe right there in your hot little hand. Go on take a bite.

EVE: I’m tempted

SATAN (Serpent): You should listen to Satan if you wanna win back your man.

EVE: God says, “Eat what you want, but the apple or crap’ll hit the fan.”

SATAN (Serpent): That’s a silly myth. It’s a Granny Smith.

EVE: (Taking a bite) All right!

SATAN (Serpent): Yes! (Serpent exits)

EVE: I hid the apples from Adam and backed them in a pie. He never knew that he had’em. Now I’m the apple of his eye.

ADAM: Are we growing old? (Realizing what has happened). You ate the apple!

EVE: I’m afraid you did too.

ADAM: Uh. Oh! (End scene)

JED: Adam and Eve’s weakness brought a curse to all mankind. Women would forever suffer the pain of childbirth

BOYD: And men would forever suffer hearing about it.

TRANSITION: Act 1. Scene 2

JED: A half-finished pyramid comes up through the floor of the stage. The pyramid splits open to reveal the Nile.

BOYD: Trumpets blare heralding Egypt’s queen. (Jed plays the famous race track bugle call on the trumpet) Thank you, Jed. That was so. . . . Egyptian.

JED: Here serene highness, ruler of all Egypt, Queen Nefertiti!

BOYD as NEFERTITI: You better eat you Wheaties when you work at Nefertiti’s, honey. I don’t need a man to define me. King Tut? King Butt. And Ramses? Now there’s a pharaoh with a narrow mind. Hey Ramses, everyone thinks your sphinx stinks. No, honey, I don’t need a man. That became clear with my last husband. What was his name, oh, yeah, Not-a-lot-in-common.

TRANSITION: Act II. Scene 3

JED: Dim lights . . . . lights up . . . and its 1491, Spain, the court of Ferdinand and Isabella. Picture the splendor of the royal palace. All of that stained glass, thousands of candles. Columbus alone with the Queen. (End scene)

JED as COLUMBUS: Your Highness, I greatly appreciate this audience. I’m honored to be in the presence of such a noblewoman. Not to mention great beauty.

BOYD as ISABELLA: (with a heavy Puerto Rican accent) Sanc jou, sanc jou berry much.

COLUMBUS: Your Highness, a woman of your taste and intelligence, your vast knowledge and enormous talent. Your elegance and poise, your tact and diplomacy. Your ability to handle every.

ISABELLA: (Annoyed, checking her watch) Columbus, I’m a berry berry busy woman. Jou got five minutes.

COLUMBUS: Signora, I have a theory. I think the world is round. Out there, over the ocean, riches and wealth abound. If you provide the backing and let my sails go unfurled, you’ll go down in history as the woman who founded the new wolrd.

ISABELLA: Esta loco! My father, may he rest in pieces, always told me that the great big world is flat. I love my people. Nothing comes between us. If you succeed this could mean a lot to Spain, cause the most important thing to me is happiness (pronounced “a penis”)

COLUMBUS: I beg your pardon?

ISABELLA: ‘Appines. Everyone has the right to life, liberty and the pursuit of ‘appiness. The Junited States of Isabella

TRANSITION: Act 3. Scene 4

BOYD: The beautiful Pocahontas and the equally gorgeous Minnehaha have come to the village of the Manhattans to go husband hunting. We meet the Indian maidens in the lobby bar of the Algonquin Hotel.

BOYD as MINNEHAHA: Pocahontas, darling. You look fabulous. I love the one feather.

JED as POCAHONTAS: I was just about to give up on you.

MINNEHAHA: I was detained, darling. Let’s just say this isn’t the first Manhattan I’ve had today.

POCAHONTAS: Details, details.

MINNEHAHA: I have only three words to describe him. Ugh-a-ly. Darling, there’s plenty to be had but nothing worth having.

POCAHONTAS: This trip’s been a bust.

MINNEHAHA: Tell me about it. . . I don’t feel like going to the Pow-Wow.

POCAHONTAS: What should we do with the tickets?

MINNEHAHA: Scalp ‘em! (bursts into laughter at the joke) You know, they say it’s time we found a mate.

POCAHONTAS: To tell the truth, I’m not ready to settle down and raise all those children, like my sister. I want an adventure. All we’ve dated here are losers.

MINNEHAHA: And how!

POCAHONTAS: There’s the brave next door.

MINNEHAHA: You mean “Crashing Boor?” And there’s the Chief of the Insomniac, “Such a Drag”

POCAHONTAS: There’s the hypochondriac, “Ol’ Popping Pills.” Better him than “Breaking Wind.” (Scene Break because of phone ringing)

BOYD: Hello? Nothing. Uh huh, uh huh, uh huh, uh huh, uh huh. Okay. Bye (He hangs up, becoming increasingly frantic) The Lipbalms are coming back.

JED: In two weeks

BOYD: Their flight was cancelled. They’re coming back . . . NOW!

JED: What about the rest of the twentieth century?

BOYD: Ladies and Gentlemen: That’s it for our presentation. Before you go,
we’d like to let you know that in The Big Bang we skyrocket through
the twentieth century by dramatizing . . .
Viet Nam
Son of Sam
Drug Abuse
Dr. Seuss
Liposuction
Breast Reduction
Neo-Nazis
Paparazzis
Interventions
Hair Extensions
Oil Spills
Diet Pills
Dr. Spock
What’s Up Doc?
Satellites
Civil Rights
Forest Gump
Donald Trump
Hawaiian Punch
The Brady Bunch

JED: All this and more. Won’t you please invest in our show!
```

---

## IC-1111: The Big Over Easy

- Title: The Big Over Easy
- Author (byline): Jasper Fforde
- Work: Not specified
- Publisher: Penguin Books
- Publication date as stated: July 2006
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: SPRATT, BRIGGS, DS MARY, MRS. DUMPTY, ANNOUNCER, NURSE, DR. QUATT, SINGH, EXECUTIVE
- Teaser before the introduction: Yes
- Spoken words (computed): 1706
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jasper Fforde
ISBN: 978-0143037231
Publisher: Penguin Books
Date (Month/Year): July 2006
```

### Introduction (context only: never use it for content warnings)

```text
It’s Easter in Reading --- a bad time for eggs. Nursery celebrity Humpty Dumpty is found shattered to death beneath a wall in a shabby area of town. And now it’s up to Detective Jack Spratt and his new partner Mary Mary to solve the case. But Detective Spratt is fresh from a spectacular failure to convict three wily pigs for the murder of a certain wolf -- and the media and tide of public opinion are set squarely against him. Now new trouble is brewing . . .

The Big Over Easy by Jasper Fforde.
```

### Performance text (classify this)

```text
SPRATT: (Pg 33) (to audience) The yard was shaped as an oblong, surrounded by a high brick wall with crumbling mortar. At one end, where the dustbins were spilling their rubbish onto the ground, large pieces of eggshell told of a recent an violent death. The victim: Humpty Dumpty – under the jurisdiction of the Nursery Crime Division.

(DUM, DUM DUM DUM . . . DUM)

BRIGGS: (Pg 33-35) Looks like he died from injuries sustained falling from a wall. Could be accident, suicide, who knows? He was discovered dead at 0722 this morning.

SPRATT: Anything else I need to know?

BRIGGS: You’re not exactly ‘Mr. Popular’ at the present. There are people who think that spending a quarter of a million pounds on a failed murder conviction for three pigs is not value for money.

SPRATT: I didn’t think justice was meant to have a price tag.

BRIGGS: It’s a public-perception thing, Spratt. Piglets are cute; wolves aren’t. You might as well try and charge the farmer’s wife with cruelty when she cut off the mice’s tails with a carving knife.

SPRATT: I did. (beat) Insufficient evidence.

BRIGGS: So . . . clean up Humpty’s tumble with the minimum of fuss and bother. After that three-pigs debacle, I want it neat, quick and cheap. I want this ex-egg mopped up neat and clean and a report on my desk Wednesday morning. (beckoning DS MARY over) I want you to meet your new Detective Sergeant Mary. (BRIGGS exits)

DS MARY: (Pg 36) (very contrary to SPRATT) Mary Mary. It’s Mary Mary. That’s my name.

SPRATT: (Pg 42) Detective Inspector Jack Spratt, Nursery Crime Division. (Pg 57-58) (he launches unexcitedly into his usual induction speech as they both examine Humpy’s body) The NCD’s jurisdiction covers all nursery characters. Because we cover well-established situations, patterns begin to emerge. There’s usually a rule of three somewhere, as in beaus, billy goats, blind mice, little pigs. If you come across any stepmothers, they’re usually evil, orphans are ten a penny, and pigs, cats, bears and wolves frequently anthropomorphize.

DS MARY: I wondered why Reading had talking animals.

SPRATT: The Billy Goats Gruff are a blast. I’ll introduce you one day.

DS MARY: No troll?

SPRATT: In the clink. Eight-to-ten-year stretch for threatening behavior. (beginning to brag) (Pg 62-63) Did you hear about the time I saved Hansel and Gretel from being eaten alive by a witch?

DS MARY: No, I’m afraid I didn’t.

SPRATT: Or the time I rescued a hundred children from the Pied Piper of Hamelin? (a shake of the head) Convicted Jill of aggravated assault against Jack?

DS MARY: Nope. (SPRATT sigs heavily) (Pg 37) (MARY rolls her eyes, flips open a notepad, she speaks to the audience) Humpty’s ovoid body had fragmented almost completely. The night’s heavy rain had washed away his liquid center, but there was sill an unmistakably eggy smell.

SPRATT: (to audience) A thin and hairless leg – still with shoe and sock. The biggest piece of shell contained Humpty’s large features. His face was pale white. One of the eyes was open and a crack ran across his face.

DS MARY: The trauma was quite severe. An untrained eye might have dismissed his body as a heap of broken eggshell and a bundle of damp clothing. (Pg 38) How did you know him?

SPRATT: He used to lecture on children’s literature at Reading University. Good company and very funny. (Pg 39) He was fired by the university in 1981 -- made the mistake of having an affair with the dean’s wife, and it didn’t go down too well. (Pg 40) (looking up at the wall) Humpty had always sat on walls, it was his way. (returning to business) We should have a word with Mrs. Dumpty. ***** Mrs. Dumpty’s House*****

MRS. DUMPTY: (Pg 64) He had it coming. Who was it, a jealous husband?

SPRATT: We never said he was murdered, Mrs. Dumpty.

MRS. DUMPTY: (Pg 66-67) We lived together for eighteen years. His philandering got worse. I through it would blow over, small indiscretions that only served to prove he could still charm the ladies. It carried on, grew more and more blatant. (shrugs her shoulders) I changed the locks. Got a divorce.

SPRATT: Did he ever get depressed?

MRS. DUMPTY: (she is visibly moved) Depressed? Are you considering this might be suicide? (then with haughty indifference) He often got depressed. He was an outpatient at St. Cerebellum’s for longer than I had known him. Easter was always bad for him, as you can imagine. Sometime he would wake up at night in a sweat screaming, “Help, Help, Take me off, I’m boiling!” (Pg 112) A recurring nightmare of being boiled alive for exactly three minutes. (Pg 67) (DS MARY laughs and tries to disguise it as a sneeze) I’m sorry, Officer, do you find something funny? (she is done) If you have no other questions . . . (she sees them out)

DS MARY: Think she’s over Dumpty?

SPRATT: Not really. I think she had Secrets. Perhaps not to do with his death, but secrets nonetheless. ****** NEWS BREAK*****

ANNOUNCER: (Pg 107) [This just in . . . ] The Reading genetic industry suffered a severe blow last night when the Quatt Foundation for Genetic Research was closed following its owner’s admission that she conducted morally dubious experiments. The disgraced Dr. Quatt has been permanently banned from funded research and has been shunned by every hospital in the nation, except for St. Cerebellum’s. **** At St. Cerebellum’s Mental Hospital to interview Humpty’s doctor, Dr. Quatt *****

NURSE: (Pg 108) (escorting SPRATT and DS MARY to DR. QUATT’s OFFICE) Dr. Quatt is a brillian woman. Mad as a barrel of skunks, and many people see her as a perverter of all decent virtues . . . but they said the same about Galileo (she laughs) All her work was to alleviate suffering. When they banned her, a dark veil fell over the medical research community. We don’t expect outsiders to truly understand her brilliance.

SPRATT: (Pg 110-112) Dr. Deborah Quatt? We wanted to talk to you about one of your patients – a Mr. Dumpty. You do know that he’s dead.

DR. QUATT: (haughtily and a bit crazy) I was nowhere near him. If you want to try me for malpractice, you’ll have to mount a good case. I’ve plenty of experience defending them, believe you me. (adjusting her tone) Mr. Dumpty? Dead? What a pity. (she looks around, lowers her voice) Did you know that I have successfully grafted a kitten’s head onto a haddock? (back to crazy) It’s not against the law. I just can’t get any funding to do proper research because of damnable outdated moral principles. In the world of cutting-edge genetic research, you can’t make an omelet without breaking eggs.

SPRATT: Which brings us back to Mr. Dumpty. How long had you been his doctor?

DR. QUATT: For five years. I was a psychiatrist before I moved into genetic research . . .

SPRATT: When did you last see him?

DR. QUATT: Six days ago. Easter was a bad time for him, as you can imagine, with all those chocolate eggs being eaten and real ones dyed – he was a virtual prisoner in his own home.

SPRATT: (Pg 113) Thank you, Dr. Quatt. Tell me – and this is just personal curiosity – were you serious when you said you’d grafted a kitten’s head onto a haddock?

DR. QUATT: (crazy returns) Do you want to see?

SPRATT: (Pg 132-133) (his phone rings, he answers, listens, then hangs up) Got a problem with morgues, Mary? [Time to] view some corpses. *****NEWS BREAK*****

ANNOUNCER: [This just in . . .](Pg 92) The incredibly dangerous homicidal maniac known as “The Gingerbreadman” was captured last night. The flour, butter, ginger and sugar psychopath, (Pg 109) with cherry eyes and thin licorice lips, (Pg 92) whose penchant for literally pulling his victims apart, is currently in a secure wing of St. Cerebellum’s (Pg 107) mental hospital, (Pg 92) where he will doubtless remain for the rest of his life. *****

(SPRATT and MARY enter the morgue)

DS MARY: (Pg 133) An ordinary pathologist would have given Humpty the most cursory of glances, but Mrs. Singh was different.

SPRATT: (to SINGH in admiration) So you’ve managed to do what all the king’s men couldn’t.

SINGH: (proudly) One hundred and twenty-six pieces! They say dead men can’t talk, but this one has spoken volumes. Take a look. (She turns Humpty’s reconstructed body over) Look at the damage on the lower back.

SPRATT: (Pg 134) (whispering) Holy s***. He was . . . shot.

SINGH: The discoloration is gunshot residue. Someone came up from the other side of the wall and shot him. By the time the bullet exited, the cracks had already encircled his body and . . . pow! -- Exploded. (beat) (Pg 135) There was one thing that puzzled me, though. (she points to the body) This section of shell, here on his waistline – or neckline, if you prefer. A small hole exactly one-quarter inch in width. Drilled in him – and deliberately too. There was a Band-Aid covering it.

SPRATT: Drug abuse?

SINGH: Possibly. I’ve run the usual tests. I’ll let you know as soon as I have something.

SPRATT: (Pg 137) Humpty didn’t fall, and he didn’t jump. Mary, we should speak to his ex-wife again. (SPRATT and MARY exit)

DS MARY: (Pg 174) (her phone rings) Thanks for calling. We’ll be straight there. (she hangs up) It’s Mrs. Dumpty. There’s been an accident. She’s. . . dead. ***At the offices of Yummy-Time***

EXECUTIVE: (Pg 176-177) (obviously distraught) She’d been a leading light of Yummy-Time since she took over from her father ten years ago. She knew shortbread fingers like the back of her hand. Mr. Aimsworth said he saw her jump into the main dough mixer. (a muffled sob)

SPRATT: I’m going to look at her office. (They enter the office and SPRATT speaks to the audience as he walks to the desk) A picture of her and Humpty in a gilt frame. And there, on the blotter, was a single piece of paper folded once, with [my] name written clearly on the front. (he dons gloves, opens the note and reads it aloud) “DI Spratt – What I did was out of love, not hate. We had been moving towards a reconciliation, until I saw him with a bimbo and my bod boiled. I went to his home and prayed for God to forgive me as I pulled the trigger. – Signed Laura Dumpty”

DS MARY: So she did kill him.

SPRATT: (Pg 178) It seems a bit too perfect. (Spratt’s phone rings, he answers and puts her on speaker)

SINGH: (Pg 363-365) I’ve been trying to reach you all day! I got Humpty’s results back from the Sunny Dale Poultry Labs. Traces of chorioallatonic membrane.

SPRATT: Traces of what?

SINGH: Chorioallatonic membrane. It’s a highly vascularized extra-embryonic membrane that functions as a site for nutrient transport and waste disposal during embryonic development!

SPRATT: Embryonic development? You mean . . .

SINGH: Right. He didn’t die from the gunshot wound or the fall. He hatched.

SPRATT: Humpty Dumpty was pregnant?

SINGH: Pregnant is perhaps the wrong word. He was an egg . . . and eggs, when fertilized, hatch.

DS MARY: Wait a minute, wait a minute. He’s a guy, right? Over sixty-five years of age., so I think we can safely say he was born – laid – whatever – unfertilized. So when was he fertilized?

SINGH: By comparing the volume of his egg, we can safely say . . . about six months ago.

SPRATT: How?

SINGH: The hole I found drilled in his shell. A modified IVF procedure would do the trick.

SPRATT: But it’s still murder. Whatever grew inside him would have been slowly consuming him from within. The question is WHY?

DS MARY: I should imagine the poultry industry might be very interested in a three-ton chicken, sir.

SPRATT: Don’t be ridiculous, Mary. You’d never find an oven big enough. Besides, what misbegotten evil genius would be so cruelly insane as to want to carry out such a bizarre and perverted experiment on a living breathing creature?

DS MARY: Dr. Quatt!

SPRATT: She had the opportunity, the skill, the knowledge. But, more important, the total absence of any ethical standards! Take a couple of officers and go to St. Cerebellum’s to arrest Dr. Quatt. [I’ll] call the Ops room and see if anyone has reported seeing a giant chicken loose in Reading! (DUM, DUM DUM DUM . . . DUM)
```

---

## IC-1112: Bigfoot Walks into Town

- Title: Bigfoot Walks into Town
- Author (byline): Chris Brock
- Work: Thousand Islands Life Magazine, Volume 14, Issue 2
- Publisher: Thousand Island Life.com
- Publication date as stated: February 2019
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, MYRON, CLIFFORD, POLICE CHIEF MYERS, PATROLMAN WEST, BIGFOOT, COLLEGE PRESIDENT, PROFESSOR, CROWD, DOG CONTROL OFFICER, MAYOR
- Teaser before the introduction: No
- Spoken words (computed): 934
- Already set (do not supply): none

### Source block (context only)

```text
Author: Chris Brock
Book: Thousand Islands Life Magazine, Volume 14, Issue 2
ISBN: On-Line Magazine
https://thousandislandslife.com/tag/february-2019/]
Publisher: Thousand Island Life.com
Date (Month/Year): February 2019
```

### Introduction (context only: never use it for content warnings)

```text
For decades, people around the world have been fascinated with the legend of Bigfoot, Sasquatch or whatever you choose to call it. Sightings of a furry, upright biped and reports of beastly footprints have been reported in American from Kentucky to the Pacific Northwest.

Is Bigfoot real? Nope, not going to answer that question. But one thing is for certain. If Bigfoot does exist, he definitely holds the title of Hide and Seek Champion of the World! But seriously . . . what would you do if one day, with no advance warning . . .

Bigfoot Walks into Town by Chris Brock
```

### Performance text (classify this)

```text
NARRATOR: The Bigfoot wandered into Highville one fine summer morning and climbed a large maple tree in the village park. (pantomime Bigfoot gazing over the town with a confused expression) As the sun rose over the village in the foothills of the Adirondacks, Myron Jones, the owner of the Highville Diner, told the regulars who were buzzing about the unusual wildlife development that the creature looked lost. It just sat there in a notch of two big branches, gazing over the village like he (Myron was certain it was a he) was trying to remember where he parked his car.

MYRON: (speaks while he is scrambling eggs as if he is an expert) It’ll find his way home. They always do.

NARRATOR: Clifford Answorth, a regular customer of the diner, disagreed. Between sips of coffee, he said the beast wasn't lost but that it looked dangerous and theorized it was obviously planning an overthrow of the village. He also thought it purposely swam across the St. Lawrence River from Canada and came down the river valley to its current perch proving its insidious craftiness.

CLIFFORD: Just you wait. That thing has friends. You’d better lock your doors tonight.

NARRATOR: The Highville Police Department was dispatched to the scene and set up a command center in the shadow of the tree; and the whole park was shortly surrounded by yellow crime tape.

POLICE CHIEF MYERS: (staring up at the creature) Jeez, I didn’t think Bigfoots were real. (he reacts to a horrible smell)

NARRATOR: The first thing he noticed was the smell, and he recalled reading about a particular odor that was reported with Bigfoot sightings.

PATROLMAN WEST: (takes a sip of coffee and opens his laptop) I think it has something to do with what they eat. (he rapidly types in some keywords to search for information, then reports eagerly) Did you know they eat cows?

POLICE CHIEF MYERS: I don’t care what they eat. Our first problem is getting it down. Maybe if he ate a crow or two, it would be a good thing.

PATROLMAN WEST: I said cows, and we don't know for sure if it's a he.

POLICE CHIEF MYERS: Whatever.

PATROLMAN WEST: (still skimming the laptop article, amazed at the information) And in Canada, Bigfoots are known to ride moose. It's how they migrate.

NARRATOR: Backed up by such expert knowledge, a half dozen officers approached the tree carefully, (pantomime fearful officer approaching the tree) looking up at each step, as if they were certain the Bigfoot was going to jump down onto them, like some sort of airborne Ninja. But fears passed as they got closer and . . . nothing happened.

PATROLMAN WEST: (surprised) He doesn’t seem to be bothered by us.

POLICE CHIEF MYERS: (retrieves his bullhorn and speaks into it, the words coming out seconds apart) DO . . . YOU . . . KNOW . . . WHERE . . . YOU . . . ARE?!

BIGFOOT: (lazily looks down at the officers)

PATROLMAN WEST: (laughing, maybe with a snort) What? You expect him to understand English? And I think he’d know that he’s obviously in a tree.

POLICE CHIEF MYERS: You’re right (embarrassed and befuddled; he thinks for a moment, scratches his head and has a brilliant idea) Call the community college!

NARRATOR: "Call the community college!" was like the village of Highville's Bat Signal. It was reserved only for such special circumstances. Maybe the college had a Bigfoot expert who knew the language! (Disappointed Wah, Wah, Wah) [But] The closest they could find to a Bigfoot language linguist was a part-time anthropology professor who once studied the mating habits of Ugandan ostriches.

POLICE CHIEF MYERS: Close enough!

NARRATOR: Before the professor was dispatched to the scene, the college’s president hastily called a press conference.

COLLEGE PRESIDENT: (grabbing a reporter’s microphone she stares dramatically into the camera) If the county gave us more money, we could afford to staff a Bigfoot expert. [Now] Our county, and perhaps our entire state, is in peril!

NARRATOR: But the anthropology professor, who was flown to the scene via the Highville Fire Department’s helicopter, did have some useful information.

PROFESSOR: (pompously lecturing the police) Yes, this looks like a familiar case. Ostriches often will chase their prey into trees, hoping they will later expire. I suggest you wait it out.

POLICE CHIEF MYERS: (waiting for more expert advice and reacting with intense nonverbal expressions when he realizes that none is forthcoming) [Well,] that was the most useless advice I ever got.

NARRATOR: At noon, the fire department was called in. All were losing patience. It was obvious something had to be done soon, especially when politics entered the picture. The local Democratic Party said the Bigfoot migration to the town was an effect of global warming. Meanwhile, the Republicans, despite obvious evidence to the contrary, declared the creature wasn’t a Bigfoot at all, but rather a well-fed, inquisitive bear.

NARRATOR: The crowd was getting larger, and members of the media were now streaming the event live. Makeshift signs had appeared.

CROWD: (chanting) We Support Bigfoot! Health Care for Sasquatch! Don’t Let a Liberal Bigfoot Loose! Bigfoot for Congress!

BIGFOOT: (observes the chaos below like a casual observer, shaking its head and rolling its eyes, yawning and eventually nodding off to sleep. It is not impressed with the intelligence of the humans below)

NARRATOR: It woke up when a ladder was slowly extended from a fire truck to the tree.

BIGFOOT: (jolted awake; it appears angry. It breaks a stick from the tree and pounds on the ladder with it)

NARRATOR: The sound echoed off nearby buildings.

PATROLMAN WEST: (in wonder) That’s how they communicate! I saw it on the Discovery Channel! I think he’s calling other Bigfoots.

PROFESSOR: (condescendingly) The plural of Bigfoot is Bigfeet.

POLICE CHIEF MYERS: (with false bravado) I don’t care what you call them. Let’s end this now. Bring out the tranquilizer gun.

NARRATOR: Patrolman West radioed back to the station. The one remaining officer there said the tranquilizer gun wasn’t available. Actually, the gun was available, but all the tranquilizer darts had been used up during crowd control at the County Fair.

POLICE CHIEF MYERS: Well, maybe we should just shoot the darn critter with a regular rifle. It’s getting awfully late. And this crowd is getting too wild.

CROWD: (chanting) We Support Bigfoot! Health Care for Sasquatch!

NARRATOR: So, the village’s dog control officer did the duty.

DOG CONTROL OFFICER: (takes aim and fires one shot) (long beat)

NARRATOR: As the sun set, a nearby roofing crew was available to retrieve the body. The roofers wanted to keep the Bigfoot, stuff it, and use it as a mascot that they could place in front yards at their projects. But Highville Mayor Charlie James consulted with Chief Myers.

MAYOR: I think we should bury it at sea like they did with Bin Laden.

POLICE CHIEF MYERS: Good idea. The last thing we need is a Bigfoot grave acting as an attraction for all sorts of loonies.

NARRATOR: Under the cover of darkness, the Bigfoot was wrapped in a tarp, loaded aboard the ferry that journeyed between Cape Vincent and Wolff Island, weighed down, and dumped overboard. The boat crew thought no one saw the dumping and gave each other high-fives. (beat) But on the shore, eyes peered out from the woods -- no one quite certain if they were of man -- or of beast.
```

---

## IC-1113: The Book of Awesome

- Title: The Book of Awesome
- Author (byline): Neil Pasricha
- Work: Not specified
- Publisher: G.P. Putnam's Sons
- Publication date as stated: March 2011
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NEIL
- Teaser before the introduction: No
- Spoken words (computed): 1713
- Already set (do not supply): none

### Source block (context only)

```text
Author: Neil Pasricha
ISBN: 978-0425238905
Publisher: G.P. Putnam's Sons
Date (Month/Year): March 2011
```

### Introduction (context only: never use it for content warnings)

```text
Polar ice caps are melting, hurricanes swirl in the sea, Wars are heating up around the world, and the job market is in the Deep Freeze. Whoa, it's getting pretty ugly out there. That's why it never hurts to take a step back and enjoy the little things in life that make it less dreary and more awesome.

Based on the award-winning 10-million-plus-hit blog 1000awesomethings.com, The Book of Awesome by Neil Pasricha is an international bestselling high-five for humanity and a big celebration of life's little moments.
```

### Performance text (classify this)

```text
NEIL: One. Wearing underwear just out of the wash. Now tell me is there anything quotes so nice as wrapping yourself in a pair of steaming undies just out of the dryer? It’s like skinny dipping in a hot tub, jumping on a horse that’s been in the sun all day, and lying on a warm, sandy beach… combined! Sure the moment doesn’t last long, yes, there may be some static cling, and it’s true, you'll have to get changed really quickly in the laundry room to pull it off, but dang girl. Hot undies. They is fine. AWESOME!

Two. Tripping and realizing that no one saw you. Learning to walk ain’t easy. Sure, you did it and I did it but we probably couldn’t do it again. Like learning anything tough and life altering, learning to walk is a messy process that takes time and practice. Unfortunately, the bad news is that practice doesn’t always make perfect. Even though we’ve been mastering the art of standing tall for years, and years, and years, everyone slips and falls now and then. So next time your shoe catches on the top step, you trip stepping off the airport’s moving sidewalk, or you bail on a patch of ice outside your front door, remember that not too long ago you couldn’t walk at all. So your wipe out is really no big deal. As long as no one saw you. AWESOME!

Three. Remembering a word that has been on the tip of your tongue all day. It’s like throwing a pail of cold water on all of your smoking inner head parts. Gears unjam, lines start rolling, and you settle back in your seat with a satisfied smile on your face and just blurt out, “Parcheesi that’s what it was called!” AWESOME!

Four. Hearing a stranger fart in public. What’s funnier than hearing a stranger fart in public? Well sure, it can happen in a bank line up, hotel lobby, restaurant, or subway car. It can happen in a restaurant, movie theater, or local library. But the funniest of all has got to be the Elevator farts. That’s the king of public farts. Little kids are always the funniest. I once heard a child in an elevator say, “Mommy, that man just farted,” with a full on finger point right into the well-dressed butt in front of his face. But hey, I guess if you’re going to fart in a kid’s face, you deserve to be called out. Yes, hearing a stranger fart in public can be a tiny, hilarious moment in the middle of any day. If you are the farter I say be loud and be proud we have all been there so no need to be embarrassed. If you are in the audience, I say Enjoy the hilarious social faux pas and resulting reaction in the room. So thank you, stranger farting in public, for adding a little comic relief to the middle of our day. AWESOME!

Five. Getting a truck driver to blow the horn. Truckers have the best horns. Those things mean business. They’re a loud and thundering slap in your face. See when a minivan lets out an itty-bitty beep-beep telling you the light turned green, it sounds like a seagull telling other seagulls “Hey, there is a guy tossing crust over here.” When a trucker does the same thing it’s a full on roar the sound a tugboat would make if it was about to crash into a lighthouse. Sometimes, when you are driving down the highway, the hours keep going and going and going. For kids without distractions, it can seem like days back there, strapped in and sitting in a numbing silence broken up only by potholes and passing motorcycles. That's why getting a trucker to blow his horn is so great. It’s a laugh and a fun, little interactive break from highway monotony. Plus, it’s a time passer. It’s a secret moment on wheels, a honkin’ highway holler and some good old-fashioned bonding in the fast lane. So let’s give thanks to truckers for not taking life too seriously for indulging our simple pleasures and for rocking that blasting air horn in a special moment I like to call AWESOME!

Six. The Five Second Rule. The five second rule simply states that any food dropped on the floor is perfectly okay to pick up as long as you do it within five seconds. The Five Second Rule has many variations, including The Three Second Rule, The Seven Second Rule, and the extremely handy, However Long it Takes Me to Pick it up off the Floor Rule. But whatever version you use, there is just no denying why it is so great.

1. It makes you look less disgusting. Because now when you eat that wet grape that rolled into the corner by the heating vent and collected some cat hair and a few dry toast crumbs, you’re not disgusting. No, you’re just a law-abiding citizen. Big difference.

2. Saves time and money. Wait, wait, wait, don’t pull the peanut butter and jelly out again and make a whole new sandwich. No, we’ll just blow the floor spices off this one, and maybe tear off the wet, soggy piece of crust that landed in the juice puddle. It’s all good.

3. It’s scientifically proven. Well, actually it's scientifically proven that if a floor is covered in salmonella or E. coli, your food will be covered in salmonella or E. coli, even if they touch for only a split second. But, here’s the kicker, that same University of Illinois study showed no significant evidence of contamination on public flooring in general. Good save science! So people, I give you a friend and savior in these tough times: the five second rule. Know it. Love it. Live by it. AWESOME!

Seven. Eating a sample you have no intention of buying.
Why hello, little cup of strawberry-kiwi punch.
How are you doing, pepper-dill crackers?
Don’t mind if I do, tiny salami wrapped around a piece of melon.

Yes, eating a free sample of something you have no intention of buying is a great way to stay on top of what’s happening in the grocery store. You swish the new drink, chew the new gum, toss back a tiny cup of the new pasta dinner, and introduce your taste buds to a little surprise. Assuming you don’t actually like the product, maybe you do what I do and pretend you're going to buy it anyway, so you don’t hurt the sweet, heavily lipsticked Sample Lady’s feelings. So you pick up the box of dry crackers, salty salami of all-noodle no cheese lasagna and say, “Hmmm. $4.29? Not bad, not bad. And I get a fifty-cent coupon too? Hmmm.” Then you smile back a her, toss it in your cart, and say “Why not! Thank you very much!” Then you roll out of sight and guiltily drop it in another aisle. AWESOME!

Eight. Absolute perfect silence.

Nine. Squeezing through a door without touching it. Tiny squirts of adrenaline pump into your bloodstream when you pull of this classic movie. Yes, suddenly you morph from Guy Walking Down the Street into Indiana Jones in that Scene Where He Slides Under the Wall at the Last Second. Your hands stay clean, your strut stays mean, and you zip through that closing door and don’t look back, hoping it doesn’t nail anybody in the face behind you. AWESOME!

Ten. Remembering someone's name. I have a problem. Within seconds of meeting somebody I completely forget their name. Sure, I introduce myself. Shake hands, and jump right into the conversation, but I can’t fully concentrate because I realize their name has immediately disappeared from my memory. Cursing myself I silently scan my frontal lobe, but my pink and lumpy mush is bright white and empty. So I smile and nod along, but inside I’m frustrated. But it’s even worse when they use my name right away.

“So Neil, where you from, Neil.” They’ll ask innocently, but I’m too busy combing through cobweb-covered spare parts in skull factory to properly answer them. My eye contact drifts and I get distracted and fidgety. It’s at these desperate times I try one of the two name-teasing techniques.

1. The take two. A friend joins my side at the party and I say to the mystery man, “Oh, have you met Chad?” hoping that Chad will put out his hand and lean in with a “Nice to meet you! Sorry, what was your name?” If Chad nails it, I give him a hi-five later. If he doesn’t, I throw a cup of punch in his face and tell him to get it right next time.

2. The spell check. If I don’t remember their name, but I think it was long and complicated, then I ask them to spell it for me. If they say P-a-r-d-e-e-p then I’m all aces, if they say P-a-m, then I’m an idiot. High risk high reward. Sure there techniques look easy, but the truth is that they’re awkward and embarrassing to use with no guaranteed results. Let's be honest. It’s much more satisfying to actually remember and drop their name right at the beginning of a sentence with confidence, like you’ve been old friends for years. Then they’ll look back at you with beaming eyes and a bright smile that shows you two are getting to know each other. Yay, maybe you’ll become friends, maybe you’ll do business, maybe you’ll start dating. All because you remembered their name at the party. Nice move you! AWESOME!

And finally, remembering how lucky we are to be here. So let's stop for a second and pull back again let's pull way, way, way back. Life is so great that we only get a tiny moment to enjoy everything we see. And that moment is right now. And that moment is counting down. And that moment is always, always fleeting. You will never be as young as you are right now. Let’s all high five and keep thinking wild thoughts, dreaming big dreams, and laughing loud laughs.

AWESOME!
```

---

## IC-1114: The Brothers Grimm Spectaculathon

- Title: The Brothers Grimm Spectaculathon
- Author (byline): Don Zolidis
- Work: Random Acts of Comedy, Pg 303
- Publisher: Playscripts, Inc.
- Publication date as stated: Aug 2011
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR 1, NARRATOR 2, GIRL, DIRT MERCHANT, ENCHANTRESS, THE DEVIL, PRINCE, RAPUNZEL, DWARF 1, DWARF 2, SNOW WHITE, WITCH, MIRROR, CINDERELLA, ACTOR, STEPSISTER 1, STEPSISTER 2, HERALD, PRINCE CHARMING
- Teaser before the introduction: Yes
- Spoken words (computed): 1613
- Already set (do not supply): none

### Source block (context only)

```text
Author: Don Zolidis
Book: Random Acts of Comedy, Pg 303
ISBN: 978-0981909974
Publisher: Playscripts, Inc.
Date (Month/Year): Aug 2011
```

### Introduction (context only: never use it for content warnings)

```text
So . . . (looks at an imaginary pocket watch) I don’t have time today to present all 209 stories.

(sad face) – But I do have time for Rapunzel! (Sings: Ah, ah, ah, ah, ah, ah, ah, ah) Snow White

(Mirror Mirror on the wall . . . ) and Cinderella (Bippity, boppity boo!) Hold onto your seats . . . this is going to be one wild ride! The Brothers Grimm Spectaculathon by Don Zolidis
```

### Performance text (classify this)

```text
NARRATOR 1: (Pg 307-308) Hello and welcome to the Brothers Grimm Spectaculathon!

NARRATOR 2: (Exploding onto the stage) Sunday Sunday Sunday! It's EXTREME! See! Monster slaying action as the three-headed pig battles the wolfo-bot in a bone-crushing cage match of death. They'll huff and they'll puff, and they'll kick some iron! Aaaaaaahh!

NARRATOR 1: Okay, stop. We're not doing that.

NARRATOR 2: Flames! Flames!

NARRATOR 1: Enough, [actor's name]. You're weirding them out.

NARRATOR 2: I'm EXTREME.

NARRATOR 1: No you're not. Can we just do the show?

NARRATOR 2: (pouts then assumes a more reserved demeanor)The Brothers Grimm were brothers named Grimm. They are dead. But in the period before they died the Brothers Grimm wrote 209 fairy tales

NARRATOR 1: These stories have become extremely popular. We all know them today.

NARRATOR 1: (Pg 309-310) So . . . Once upon a time there was a girl

NARRATOR 2: And she was beautiful-

NARRATOR 1: Because no one cares about ugly people.

NARRATOR 2: I care about ugly people.

NARRATOR 1: Well no one cares about you. Anyway, there was a girl . . . (GIRL enters in dramatic fashion.)

NARRATOR 2: And she was poor.

GIRL: Oh I am poor.

NARRATOR 2: Dirt poor.

NARRATOR 1: She couldn't even afford dirt. (DIRT MERCHANT enters.)

DIRT MERCHANT: Dirt for sale! Dirt for sale! Hey, you! Get off the merchandise! (He exits.)

GIRL: (Crying) (An ENCHANTRESS enters.)

ENCHANTRESS: Excuse me-but I couldn't help overhearing your tale of misery and woe. Tell you what-I will grant you your heart's desire if you give me one small thing.

GIRL: That sounds like a great bargain. I won't even ask what the small thing is because I'm so innocent and trusting!

ENCHANTRESS: Excellent. (She makes a magical signal and vanishes)

GIRL: What a nice lady. (THE DEVIL enters.)

THE DEVIL: Hey there hot stuff. Oh wait, that's me. Ha ha ha ha! Now, I happened to overhear your tale of misery and woe and I'm here to help.

GIRL: Well actually I just-

THE DEVIL: Just sign this one small contract and you shall conceive a daughter so beautiful the very earth will want to kiss her. But in a platonic way.

GIRL: That sounds like a great idea. (She signs the contract.)

THE DEVIL: Moo ah ha ha ha ha ha! (He looks around. Then runs off)

NARRATOR 1: (Pg 311- It was a good day for the girl. She fell in love with a prince.

PRINCE: (PRINCE enters.) Hey, you're hot!

GIRL: I am hot.

PRINCE: Let's get married!

GIRL: Score!

NARRATOR 2: She grew very rich.

GIRL: Ha ha! Score!

NARRATOR 2: And she conceived a child.

GIRL: Whoah! How did that happen?

NARRATOR 2: Well, you see kids, when a prince and a princess love each other very much-

NARRATOR 1: Through magic. The magic of The Devil. That’s where babies come from!

NARRATOR 2: (Pg 312-313) Years passed. And she grew into a beautiful young teenager, Rapunzel.

GIRL: Darling, we're going to have dinner so wash your hands.

RAPUNZEL: You can't tell me what to do!

PRINCE: Don't talk to your mother that way. She sold her soul to the Devil just to have you-

RAPUNZEL: I don't care! I didn't ask to be born!

NARRATOR 1: And just then.

ENCHANTRESS: I have returned.

THE DEVIL: Your time is up.

GIRL: What do you want?

ENCHANTRESS: (as they fight over Rapunzel) Your child.

THE DEVIL: Your child.

RAPUNZEL: STOP!! Mom!? How many deals did you make?

ENCHANTRESS: (Pg 314) I will take Rapunzel. (She grabs RAPUNZEL)

THE DEVIL: Um ... excuse me? I'm The Devil (He grabs RAPUNZEL.) Lord of darkness? All that? I think I've got a little bit more claim to this girl than some stupid little witch.

ENCHANTRESS: I curse you!

THE DEVIL: I curse you right back! You know what, this is stupid. Tell ya what, if you sign this contract here, I will let you take Rapunzel.

ENCHANTRESS: That sounds like a plan. (She signs the contract.)

THE DEVIL: Moo ah ha ha ha! And I disappear in a cloud of brimstone!

ENCHANTRESS: Well, come along Rapunzel.

RAPUNZEL: Where are we going?

ENCHANTRESS: I built this great tower for you.

GIRL: Run along dear.

RAPUNZEL: But Mom. I don't want to go with the evil Enchantress

GIRL: Yeah and I didn't want to raise a spoiled brat. But sometimes you don't always get what you want. Unless you make a deal with The Devil. See ya.

NARRATOR 2: So the Enchantress took Rapunzel and locked her in a high tower without stairs or door. *******

NARRATOR 2: (Pg 320-321) Once upon a time. There was a dwarf.

DWARF 1: I prefer little person.

NARRATOR 1: In fact, two dwarves. And these dwarves worked all day in the mines.

DWARF 2: (Singing) Whistle while you work

NARRATOR 1: We can't use that song.

DWARF 2: I do what I want.

NARRATOR 1: No it's like copyrighted, we can't use it. The Mouse will sue us. So the dwarves worked in the mines, they sang their little song and then one day they came home to find- (Enter SNOW WHITE. She falls asleep.)

DWARF 1: What the heck is that thing? (menacingly) I'm going to chop you up and eat you.

NARRATOR 1: Time out. Time out.

DWARF 1: What? I'm just going with what my character wants.

NARRATOR 1: You do not get to eat Snow White. You're not the villain of the story. We are going to do this story as written. Snow White cleans house for the dwarves, then she gets poisoned by an apple, then a prince shows up-

SNOW WHITE: (Waking up) Why do I have to clean the house? Is it because I'm a woman?

DWARF 1: Yes.

NARRATOR 1: No it's because you feel sorry for the little dwarves because they're messy and you have OCD and want to make everything nice.

SNOW WHITE: I don't see why I have to be a maid! I'm the princess here, they should be cleaning up for me.

DWARF 1: All right, she's become too much trouble, let's eat her.

NARRATOR 1: (Pg 323) And moving on.

SNOW WHITE: (Pg 309) Once upon a time there was a beautiful girl. (Pg 323) She was the most beautiful girl in the entire kingdom. But her stepmother was jealous. (WITCH enters)

WITCH: Snow White.

SNOW WHITE: Stepmother.

WITCH: I do believe you're putting on weight.

SNOW WHITE: Not on this body, sister. These curves are tight and streamlined

WITCH: I think you might need to tweeze your eyebrows.

SNOW WHITE: My eyebrows are sculpted like a block of clay in the hands of a blind god of sculpting eyebrows. . . . (looks concerned) Who writes this stuff? (Snow exits)

WITCH: Mirror, mirror, on the wall. Who's the fairest of them all

MIRROR: (A drawn-out ghostly voice) Well it's certainly not you.

WITCH: Curses!

MIRROR: Hey that's a good idea. You should try that

WITCH: (Pg 324) Snow White.

SNOW WHITE: Stepmother.

WITCH: How about an apple as a peace offering?

SNOW WHITE: When are you going to learn Stepmother, that we women shouldn't be judged by our surface beauty but rather by the contents of our brains?

WITCH: Um ... that's just stupid.

PRINCE: Hey I was just in the neighborhood looking for a girl in a coma to make out with (Snow White grabs PRINCE and bends him over backward for a kiss) Whoah! You're very forward.

SNOW WHITE: I'm a modern woman. Come on, let's get married.

NARRATOR 2: And they all lived happily ever after and avoided traditional gender roles. And the seven little dwarves cooked for them, cleaned the house, and did all that other junk that Snow White was supposed to do in the story. The end. ******

NARRATOR 2: (Pg 309) Once upon a time. (Pg 330) [Cinderella’s] mother died and her father remarried.

CINDERELLA: (Pg 329) (enters, overacting) I am orphaned! Oh I am sad!

ACTOR: (Pg 330-332) (An ACTOR enter.) Hold on! We [can’t] do this one

NARRATOR 2: Well, I guess we can skip it then.

CINDERELLA: (CINDERELLA stops acting) NO WE ARE NOT SKIPPING IT. We are going to tell my story, OR I WILL TEAR OUT YOUR TINY HEART, GOT IT?

ACTOR: Yes, Ma'am.

CINDERELLA: Thank you.

NARRATOR 2: Okay, so, her mother died and her father remarried

CINDERELLA: (Overlapping) Mother? Where are you mother? Are you dead?

NARRATOR 2: Now, Cinderella's stepmother had two daughters, both equally beautiful-

CINDERELLA: (CINDERELLA raises her hand) I'm sorry. I think you've got that wrong. I'm the pretty one. They're quite hideous.

NARRATOR 2: Says here they're beautiful too.

CINDERELLA: I think I know my story, thank you. Oh they are so mean . . . so mean.

STEPSISTER 1: (The two WICKED STEPSISTERS enter) Look what the cat dragged in.

STEPSISTER 2: Does it smell in here, or is it just her?

STEPSISTER 1: Oh Cinderella. I need to get ready for the ball

CINDERELLA: What ball?

STEPSISTER 1: The ball being thrown by Prince Charming.

STEPSISTER 2: He's so charming. When I see him I just want to grab his little tights-wearing bottom

CINDERELLA: Can I come?

STEPSISTER 1: Of course you can ... NOT! I'm so hot.

STEPSISTER 2: I'm gorgeous. (Stepsisters exit)

CINDERELLA: (Overacting) Life. So unfair. The room is spinning. Why, God, why? Why am I just a servant - a slave! Lower than the dust. I shall now cry myself to sleep as I do every night. (cries)

NARRATOR 2: (To the audience) She thinks the Oscar committee is watching.

CINDERELLA: (Pg 333) How can life be so cruel! WHY?!!!! (She hears a sound) What's that? My fairy godmother?

NARRATOR 2: Nope. We're going by the original. There's no fairy godmother.

CINDERELLA: Well, I can't do this without a fairy godmother. Who's going to turn the pumpkin into a coach?

NARRATOR 2: You walk there.

CINDERELLA: What?! I'm Cinderella! (She stomps off)

NARRATOR 2: (Pg 335) Just then Cinderella's two wicked stepsisters arrive [at the ball]

STEPSISTER 1: Cinderella! What are you doing here?

STEPSISTER 2: You suck!

HERALD: (Pg 336-338) (Blowing imaginary horn) Dun de dun dun! His royal highness, the Prince! (The stepsisters go wild)

PRINCE CHARMING: (with a British accent for no apparent reason) 'Ello there. We're having a nice time, are we? Blimey. She's gorgeous. Who's that minx?

CINDERELLA: My name's Cinderella.

PRINCE CHARMING: Right-o. Come here and give us a taste, love. (PRINCE CHARMING and CINDERELLA begin to dance – He is REALLY bad)

CINDERELLA: Oh Prince. Stop. You're embarrassing me.

NARRATOR 2: And they danced all night long. (Stepsister wail and stomp off)

CINDERELLA: What are these feelings? Could it be . . . love? (Clock begins to strike, Cinderella panics and runs off, losing her shoe in the process, the prince picks it up, has an idea and exits)

ACTOR: Can we skip to that part please?

NARRATOR 2: You know what? Fine. A little of this, a little of that, the prince stops by with a shoe looking for a girl who fits it.

PRINCE CHARMING: 'Ello then. Any of you darlings lost a shoe?

STEPSISTER 1: Oh I did. I did! Let me see that! (She takes the shoe.)

NARRATOR 2: And of course, her foot was too big, so she chopped off her big toe.

STEPSISTER 1: (Blood-curdling scream) Aarrrrrrrrr- rrrrrrrrrgghghgghghg! (She limps) It . . . fits . . .

PRINCE CHARMING: Say, what's all this then? There's blood everywhere. (He wrestles the shoe off her foot)

STEPSISTER 1: I popped a zit. On my foot.

PRINCE CHARMING: You chopped off your toe, you did!

STEPSISTER 2: May I please try the shoe. (Prince shrugs and hand over the shoe)

NARRATOR 2: The shoe didn't fit either. So she did the only sensible thing and chopped off her heel.

(Blood-curdling scream)

STEPSISTER 2: Arrghgghghffhfhgh! I'm . . . fine! (She limps See. . .it fits.

PRINCE CHARMING: Is that blood on your foot?

STEPSISTER 2: I cut myself shaving. I have hairy feet. Like a hobbit.

PRINCE CHARMING: You cut off your heel you daft wench!

STEPSISTER 2: I did it for you! (Prince takes the show from Stepsister 2)

PRINCE CHARMING: 'Ello there. I realize several of the ladies in this here house have chopped off body parts to fit in this here shoe, but I was just wondering if anyone else fit in it. You see, I'm not very smart, but I make up for it by being very persistent. It makes me ideal to run the government. (CINDERELLA runs to him.)

CINDERELLA: I will try the shoe.

PRINCE CHARMING: It fits!

CINDERELLA: My love!

PRINCE CHARMING: It is you!

CINDERELLA: It is I!

NARRATOR 2: And they lived. Happily. Ever. After.
```

---

## IC-1115: The Celebrated Jumping Frog of Calaveras County

- Title: The Celebrated Jumping Frog of Calaveras County
- Author (byline): Mark Twain
- Work: The Unabridged Mark Twain
- Publisher: Running Press
- Publication date as stated: November 1976
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2657
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mark Twain
Book: The Unabridged Mark Twain
ISBN: 0822218739
Publisher: Running Press
Date (Month/Year): November 1976
```

### Introduction (context only: never use it for content warnings)

```text
Mark Twain once wrote, “Let us be thankful for the fools. But for them the rest of us could not succeed.” Though such thoughts are seldom spoken out loud in today’s politically correct America, there is little doubt that the mantra echoes in our thoughts multiple times each day.

This concept was, however, more readily apparent during the early days of Mark Twain’s career, because the “fools” were geographically situated. The East and its inhabitants had a reputation for being civilized, cultured, and advanced. The West, on the other hand, was considered less-educated -- less-refined and as is seen in The Celebrated Jumping Frog of Calaveras County . . . naive and easily duped.
```

### Performance text (classify this)

```text
In compliance with the request of a friend of mine, who wrote me from the East, I called on good-natured, garrulous old Simon Wheeler, and inquired after my friend's friend, Leonidas W. Smiley, as requested to do, and I hereunto append the result. I have a lurking suspicion that Leonidas W. Smiley is a myth; that my friend never knew such a personage; and that he only conjectured that, if I asked old Wheeler about him, it would remind him of his infamous Jim Smiley, and he would go to work and bore me nearly to death with some infernal reminiscence of him as long and tedious as it should be useless to me. If that was the design, it certainly succeeded. I found Simon Wheeler dozing comfortably by the bar-room stove of the old, dilapidated tavern in the ancient mining camp of Angel's, and I noticed that he was fat and bald-headed, and had an expression of winning gentleness and simplicity upon his tranquil countenance. He roused up and gave me good-day. I told him a friend of mine had commissioned me to make some inquiries about a cherished companion of his boyhood named Leonidas W. Smiley Rev. Leonidas W. Smiley a young minister of the Gospel, who he had heard was at one time a resident of Angel's Camp. I added that, if Mr. Wheeler could tell me any thing about this Rev. Leonidas W. Smiley, I would feel under many obligations to him. Simon Wheeler backed me into a corner and blockaded me there with his chair, and then sat me down and reeled off the monotonous narrative which follows this paragraph. He never smiled, he never frowned, he never changed his voice from the gentle-flowing key to which he tuned the initial sentence, he never betrayed the slightest suspicion of enthusiasm; but all through the interminable narrative there ran a vein of impressive earnestness and sincerity, which showed me plainly that, so far from his imagining that there was any thing ridiculous or funny about his story, he regarded it as a really important matter, and admired its two heroes as men of transcendent genius in finesse. To me, the spectacle of a man drifting serenely along through such a queer yarn without ever smiling, was exquisitely absurd. As I said before, I asked him to tell me what he knew of Rev. Leonidas W. Smiley, and he replied as follows. I let him go on in his own way, and never interrupted him once: There was a feller here once by the name of Jim Smiley, in the winter of '49 or may be it was the spring of '50 I don't recollect exactly, somehow, though what makes me think it was one or the other is because I remember the big flume wasn't finished when he first came to the camp; but any way, he was the curiosest man about always betting on any thing that turned up you ever see, if he could get any body to bet on the other side; and if he couldn't, he'd change sides. Any way that suited the other man would suit him any way just so's he got a bet, he was satisfied. But still he was lucky, uncommon lucky; he most always come out winner. He was always ready and laying for a chance; there couldn't be no solittry thing mentioned but that feller'd offer to bet on it, and -take any side you please, as I was just telling you. If there was a horse-race, you'd find him flush, or you'd find him busted at the end of it; if there was a dog-fight, he'd bet on it; if there was a cat-fight, he'd bet on it; if there was a chicken-fight, he'd bet on it; why, if there was two birds setting on a fence, he would bet you which one would fly first; or if there was a camp-meeting, he would be there reg'lar, to bet on Parson Walker, which he judged to be the best exhorter about here, and so he was, too, and a good man. If he even seen a straddle-bug start to go anywheres, he would bet you how long it would take him to get wherever he was going to, and if you took him up, he would foller that straddle-bug to Mexico but what he would find out where he was bound for and how long he was on the road. Lots of the boys here has seen that Smiley, and can tell you about him. Why, it never made no difference to him he would bet on any thing the dangdest feller. Parson Walker's wife laid very sick once, for a good while, and it seemed as if they warn's going to save her; but one morning he come in, and Smiley asked how she was, and he said she was considerable better thank the Lord for his inftnit mercy and coming on so smart that, with the blessing of Providence, she'd get well yet; and Smiley, before he thought, says, "Well, I'll risk two- and-a-half that she don't, any way." Thish-yer Smiley had a mare the boys called her the fifteen- minute nag, but that was only in fun, you know, because, of course, she was faster than that and he used to win money on that horse, for all she was so slow and always had the asthma, or the distemper, or the consumption, or something of that kind. They used to give her two or three hundred yards start, and then pass her under way; but always at the fag-end of the race she'd get excited and desperate- like, and come cavorting and straddling up, and scattering her legs around limber, sometimes in the air, and sometimes out to one side amongst the fences, and kicking up m-o-r-e dust, and raising m-o-r-e racket with her coughing and sneezing and blowing her nose and always fetch up at the stand just about a neck ahead, as near as you could cipher it down. And he had a little small bull pup, that to look at him you'd think he wan's worth a cent, but to set around and look ornery, and lay for a chance to steal something. But as soon as money was up on him, he was a different dog; his underjaw'd begin to stick out like the fo'castle of a steamboat, and his teeth would uncover, and shine savage like the furnaces. And a dog might tackle him, and bully- rag him, and bite him, and throw him over his shoulder two or three times, and Andrew Jackson which was the name of the pup Andrew Jackson would never let on but what he was satisfied, and hadn't expected nothing else and the bets being doubled and doubled on the other side all the time, till the money was all up; and then all of a sudden he would grab that other dog jest by the j'int of his hind leg and freeze on it not chew, you understand, but only jest grip and hang on till they thronged up the sponge, if it was a year. Smiley always come out winner on that pup, till he harnessed a dog once that didn't have no hind legs, because they'd been sawed off by a circular saw, and when the thing had gone along far enough, and the money was all up, and he come to make a snatch for his pet bolt, he saw in a minute how he'd been imposed on, and how the other dog had him in the door, so to speak, and he 'peered sur- prised, and then he looked sorter discouraged-like, and didn't try no more to win the fight, and so he got shucked out bad. He give Smiley a look, as much as to say his heart was broke, and it was his fault, for putting up a dog that hadn't no hind legs for him to take bolt of, which was his main dependence in a fight, and then he limped off a piece and laid down and died. It was a good pup, was that Andrew Jackson, and would have made a name for hisself if he'd lived, for the stuff was in him, and he had genius I know it, because he hadn't had no opportunities to speak of, and it don't stand to reason that a dog could make such a fight as he could under them circumstances, if he hadn't no talent. It always makes me feel sorry when I think of that last fight of his'n, and the way it turned out. Well, thish-yer Smiley had rat-tarriers, and chicken cocks, and tom- cats, and all of them kind of things, till you couldn't rest, and you couldn't fetch nothing for him to bet on but he'd match you. He ketched a frog one day, and took him home, and said he cal'klated to edercate him; and so he never done nothing for three months but set in his back yard and learn that frog to jump. And you bet you he did learn him, too. He'd give him a little punch behind, and the next minute you'd see that frog whirling in the air like a doughnut see him turn one summerset, or may be a couple, if he got a good start, and come down flat-footed and all right, like a cat. He got him up so in the matter of catching flies, and kept him in practice so constant, that he'd nail a fly every time as far as he could see him. Smiley said all a frog wanted was education, and he could do most any thing and I believe him. Why, I've seen him set Dan'l Webster down here on this floor Dan'l Webster was the name of the frog and sing out, "Flies, Dan'l, flies!" and quicker'n you could wink, he'd spring straight up, and snake a fly off'n the counter there, and flop down on the floor again as solid as a gob of mud, and fall to scratching the side of his head with his hind foot as indifferent as if he hadn't no idea he'd been doin' any more'n any frog might do. You never see a frog so modest and straightforward as he was, for all he was so gifted. And when it come to fair and square jumping on a dead level, he could get over more ground at one straddle than any animal of his breed you ever see. Jumping on a dead level was his strong suit, you understand; and when it come to that, Smiley would ante up money on him as long as he had a red. Smiley was monstrous proud of his frog, and well he might be, for fellers that had traveled and been everywheres, all said he laid over any frog that ever they see. Well, Smiley kept the beast in a little lattice box, and he used to fetch him down town sometimes and lay for a bet. One day a feller a stranger in the camp, he was come across him with his box, and says: "What might it be that you've got in the box?" And Smiley says, sorter indifferent like, "It might be a parrot, or it might be a canary, may be, but it an't it's only just a frog." And the feller took it, and looked at it careful, and turned it round this way and that, and says, "H'm so 'tis. Well, what's he good for?" "Well," Smiley says, easy and careless, "He's good enough for one thing, I should judge he can outjump any frog in Calaveras county." The feller took the box again, and took another long, particular look, and give it back to Smiley, and says, very deliberate, "Well, I don't see no p'ints about that frog that's any better'n any other frog." "May be you don't," Smiley says. "May be you understand frogs, and may be you don't understand 'em; may be you've had experience, and may be you an't only a amature, as it were. Anyways, I've got my opinion, and I'll risk forty dollars that he can outjump any frog in Calaveras county." And the feller studied a minute, and then says, kinder sad like, "Well, I'm only a stranger here, and I an't got no frog; but if I had a frog, I'd bet you."

And then Smiley says, "That's all right that's all right if you'll hold my box a minute, I'll go and get you a frog." And so the feller took the box, and put up his forty dollars along with Smiley's, and set down to wait. So he set there a good while thinking and thinking to hisself, and then he got the frog out and prized his mouth open and took a tea- spoon and filled him full of quail shot filled him pretty near up to his chin and set him on the floor. Smiley he went to the swamp and slopped around in the mud for a long time, and finally he ketched a frog, and fetched him in, and give him to this feller, and says: "Now, if you're ready, set him alongside of Dan'l, with his fore- paws just even with Dan'l, and I'll give the word." Then he says, "One two three jump!" and him and the feller touched up the frogs from behind, and the new frog hopped off, but Dan'l give a heave, and hysted up his shoulders so like a Frenchman, but it wan's no use he couldn't budge; he was planted as solid as an anvil, and he couldn't no more stir than if he was anchored out. Smiley was a good deal surprised, and he was disgusted too, but he didn't have no idea what the matter was, of course. The feller took the money and started away; and when he was going out at the door, he sorter jerked his thumb over his shoulders this way at Dan'l, and says again, very deliberate, "Well, I don't see no p'ints about that frog that's any better'n any other frog." Smiley he stood scratching his head and looking down at Dan'l a long time, and at last he says, "I do wonder what in the nation that frog throw'd off for I wonder if there an't something the matter with him he 'pears to look mighty baggy, somehow." And he ketched Dan'l by the nap of the neck, and lifted him up and says, "Why, blame my cats, if he don't weigh five pound!" and turned him upside down, and he belched out a double handful of shot. And then he see how it was, and he was the maddest man he set the frog down and took out after that feller, but he never ketchd him. And- [Here Simon Wheeler heard his name called from the front yard, and got up to see what was wanted.] And turning to me as he moved away, he said: "Just set where you are, stranger, and rest easy I an't going to be gone a second." But, by your leave, I did not think that a continuation of the history of the enterprising vagabond Jim Smiley would be likely to afford me much information concerning the Rev. Leonidas W. Smiley, and so I started away. At the door I met the sociable Wheeler returning, and he button- holed me and recommenced: "Well, thish-yer Smiley had a yeller one-eyed cow that didn't have no tail, only jest a short stump like a bannanner, and " "Oh! hang Smiley and his afflicted cow!" I muttered, good-naturedly, and bidding the old gentleman good-day, I departed.
```

---

## IC-1116: Channel Changers

- Title: Channel Changers
- Author (byline): Wayne Rice and Mike Yaconelli
- Work: The Greatest Skits on Earth
- Publisher: Zondervan
- Publication date as stated: March 1986
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1946
- Already set (do not supply): none

### Source block (context only)

```text
Author: Wayne Rice and Mike Yaconelli
Book: The Greatest Skits on Earth
ISBN: 978-0310351412
Publisher: Zondervan
Date (Month/Year): March 1986
```

### Introduction (context only: never use it for content warnings)

```text
Let’s admit it . . . We’re always searching for something better: Something nicer, faster, newer, shinier, bigger. Something more. Something else. The remote control made this search easier than ever: you can navigate a thousand channels without leaving your couch, flipping endlessly through channel after channel after channel until you find something better. But television isn’t the only place in which we constantly search for something better: we flip through every aspect of our lives—food, relationships, radio stations, work—all the while looking for anything other than what’s in front of us. The problem is, in a world of unlimited choices, there actually is always something better somewhere.

Channel Changers by Wayne Rice and Mike Yaconelli
```

### Performance text (classify this)

```text
The following three scripts all follow the same format. The idea is to demonstrate what might happen if you flipped back and forth between several different programs or channels on your radio or television set. Each "click" in the script is a channel change. Use your own creativity, add your own lines, and have fun with these.

Script #1: Television

Story Lady: Today, boys and girls, our story is about Little Red Riding Hood. Once upon a time there was a little girl named Little Red Riding Hood. One day her mother asked her to go through the woods to visit her grandmother. And on her way who should jump out from behind a tree but ... (click)

Boy Scout: The Boy Scouts of America! Yes, sir, fellas, the Boy Scouts are just the group for you. Why, for just a dollar ... (click)

Gangster: You can shove it down your throat! Try and steal my gal, will ya? Why for two cents I'd ... (click)

Recipe Lady: ... set carefully in a quart of prune juice. And when the mixture is settled, ladies, just pop it into the ... (click)

Announcer: ... end zone for a touchdown! Wow! Did you see that last play, sports fans'? Terrific! And now a word from our sponsor, Shavo. With Shavo, the sharpest razor in the world ... (click)

Gangster: You can cut your own throat for all I care, you slob! Who do you think you are anyway? ... (click)

Story Lady: ... Little Red Riding Hood ... (click)

Recipe Lady: What a smell! Doesn't that just make your mouth water, ladies? Now for the vegetables. Ladies, this next recipe is very unique. It calls for one ... (click)

Announcer: ... broken leg! The star is definitely out of the game. The wildcats really need help. Guess they'll have to call in the ... (click)

Boy Scout: ... Boy Scouts of America! Each year, fellas, we take a camping trip. Boy, there's nothing like it. You're out there all alone with no one but the wind, the stars, and ... (click)

Story Lady: ... Little Red Riding Hood. As she entered the cottage she said ... (click)

Gangster: This is the dumbest thing I've ever done! How could I have ever called you a friend when you turn on me and steal my girl. You slob! You're nothing but a ... (click)

Recipe Lady: ... hot dog! Slice it carefully and then cook the casserole on top of the ...

(click)

Announcer: ... football field. That should do it for the Wildcats, folks. With Brooks out of the game, it doesn't look like they have a chance. Now they line up. The snap. Draw play! What a hand-off. There goes Johnson! Look at him go. He's going all the way to the ... ( click)

Boy Scout: ... outhouse. We don't have running water either. You'll learn how to make Mulligan stew, though. You'd be surprised how it tastes in the fresh air and woods. After a hearty meal, you can't help but say ... (click)

Gangster: I think I'll shoot myself! That gal meant more to me than ... (click)

Recipe Lady: ... a handful of chopped nuts. Chop them fine and fold into the flour mixture. Next, beat the eggs until they look like ... (click)

Announcer: ... mud in your face. What a pile up! The Panthers didn't even get past the line of scrimmage! Boy, these Wildcats have really worked hard this half. With the score at 10-10 and five minutes to go, who will win? ... (click)

Boy Scout: The Boy Scouts of America! Boy, fellas, you can't pass up this opportunity to join now. Right now you're probably saying to yourself ... (click)

Story Lady: What a big mouth you have! And the wolf said ... (click)

Gangster: Listen, honey. You're comin' with me. I'm tired of all this foolin' around. And you, ya dirty yellow rat, you're nothin' but a ... (click)

Announcer: ... hound dog running down the field! Oh-oh. It looks like he's heading right for the ... (click)

Recipe Lady: ... garbage. There's no need to keep it. After this dinner, ladies, you'll sigh with satisfaction. Your husband will tell you it's delicious and you'll say, "Oh, you ... (click)

************* Script #2: Radio

Person A: Good evening, ladies and gentlemen. This is Seymour Skidmarks bringing you the latest news in the world of sports. The annual football game between ______ and ________ was played last week to the enjoyment of a large crowd who went wild when, at a crucial point in the game, Coach ______ sent in ... (click)

Person B: ... three eggs, a cup of buttermilk, and a pinch of salt. Stir well and pour into a flat greased pan or . . . (click)

Person C: ... your new fall hat. This year, fashion decrees that women shall wear a large variety of charm bracelets. A most popular design is to make them of ... (click)

Person D: ... old whiskers? If you do, just shave them off with Bates' Better Shaving Cream. Use this cream, and you will be so handsome that all the girls will ...

(click)

Person E: ... bend over and touch the floor twenty times. This exercise is superb for general reducing. All right now, pupils, again let's bend over, up, over ...

(click)

Person F: (singing) ... the ocean. My Bonnie lies over the sea. My Bonnie lies over the ocean, oh, bring back my Bonnie ... (click)

Person A: who sailed down the field for a touchdown that tied the game. What a play! What a perfect ... (click)

Person C: ... ly darling little summer bag that all you girls simply must have. At first glimpse they may remind one of ... (click)

Person G: ... a bowl of porridge. But it was toooo hot. The second bowl was as hot as the first, but the third was just right. Goldilocks ate, and ate, until she could ... (click)

Person D: ... feel the stiff beard with your hand. Is that very romantic? Our foolproof way to get a girl friend is to ... (click)

Person E: ... breathe deeply three times, and pound on your chest with your fists after inhaling each breath. This enlivens the tissues and makes one feel ...

(click)

Person B: ... puffy and full of air. You achieve this effect by beating the mixture with a rotary eggbeater for five .... (click)

Person C: ... hundred years. The things our grandmothers wore then are the most popular things today. Already fashion leaders, prominent society women are trying to bring back more old-fashioned manners. Their cry is "Bring back ... (click)

Person F: ... (singing) my Bonnie to me, to me, bring back, bring back, oh, bring back ... (click)

Person D: ... a nice soft chin and a host of compliments. If you use our cream, those whiskers will come out with a ... (click)

Person G: CRASH!! Goldilocks had broken the little chair all to pieces. Then she jumped up and started up the stairs. There she saw three beds. The first bed was covered with a bearskin rug, which was too soft. The second bed was covered with ... (click)

Person A: ... what looked like crawling things from the press box, but it was only the players in hard scrimmage. We are looking with expectation to _ winning their ________ championship this fall. The players are in good condition; their average weight is ... (click)

Person E: ... 110 pounds. You, too, can weigh this much if you just follow these simple exercises. Don't take them too hard at first or you will probably have to ... (click)

Person F: ... (singing) lay on my pillow. Last night as I lay on my bed; last night as I lay on my pillow, I dreamed that my Bonnie was ... (click)

Person B: ... cooking in a hot oven at about 450 degrees Fahrenheit. For an extra treat, garnish with cloves or whole ... (click)

Person G: ... bears? Will Goldilocks get home safely? How will the story end? Keep your radio tuned to this station until tomorrow at this time for the next episode of this thrilling story. Until then, kiddies, be sweet and don't forget to ... (click)

Person D: shave off the whiskers with Bates'. Our motto is ... (click)

Person E: stand on your head and wave your feet in the air. Gym clothes are best for this exercise, but ... (click)

Person C: ... an ostrich feather will do just as well. Take my tip and you girls will be as fashionable as . . . (click)

Person A: from whom we are expecting great things this year. This is your friendly announcer, Seymour Skidmarks, signing off and saying ... (click)

Person C: ... Night all! (sexy voice)

************** Script #3: Television

Indy 500: Here we are at the Indy 500 and we're almost ready to begin. GENTLEMEN ... START YOUR ... (click)

Health Advisor: ... toothbrushes. These are very important to our overall health. Every married couple ought to own and use ... (click)

Gangster: ... handcuffs! There's no way I'll wear those things. It looks like I'm going to have to call ... (click)

Sesame Street: Big Bird! Come back! When it rains like this we all wear ... (click)

Grocer: ... seedless grapefruits and oranges. Many people have a lot of trouble with seeds. Just imagine swallowing ... (click)

Indy: ... an oil spill in the third turn! Unser is going to slide through. It looks like he's going to collide with ... (click)

Sesame Street: Cookie Monster! Where have you been? Boys and girls, we're going to take you to . . . (click)

Gangster: ... the county jail! I've got to get out of this joint! I hear the bank is expecting two million ... (click)

Health: . . . push-ups, sit-ups, and many other exercises. Remember, always breathe deeply before ... (click)

Grocer: ... peeling a banana. You know, the aroma of a well-ripened banana is much like that of ... (click)

Indy: ... gasoline all over the pit area! Now, there is the danger of fire! Rivera has jumped out of his ... (click)

Sesame Street: ... garbage can. Children, the Cookie Monster has always wanted to ...

(click)

Gangster: ... rob the First National Bank! I think I can do it. The police would never think to look for me in the . . . (click)

Grocer: ... frozen food section. One thing I require here at Food King is that every check-out clerk should always ... (click)

Indy: ... flip end over end. I've never seen such a crash. I believe the medical crew has a large number of ... (click)

Health: jump ropes for all the children. These young bodies are ... (click)

Sesame Street: .. yellow, green, purple, and orange. It is so beautiful. We must remember that rainbows . . . (click)

Gangster: ... are to be memorized and swallowed. These are confidential. Don't let anyone know ... (click)

Grocer: We sell live lobsters. We are very organized and reasonable. People go through our check-out lines ... (click)

Indy: ... moving at over 200 miles per hour. Wow! What a car. Ladies and gentlemen, he is flying around ... (click)

Health: ... your left kneecap. This can become a problem. Sometimes this won't develop until you ... (click)

Sesame Street: ... let Big Bird give you a big hug! Oh, isn't that sweet! Big Bird loves to ... (click)

Gangster: ... drive his car over a cliff. That's a 200-foot drop. He'll never live through ... (click)

Grocer: ... our famous barbecued chicken. We've had some great customers. One man was rolling his cart down aisle three, and ... (click)

Indy: He blew a tire! He's spilling oil all over the track. Tell the clean-up crew to ...

(click)

Health: Drink it all up! It's great for hair, bones, skin, and ... (click)

Sesame Street: ... counting by twos. It's really not that hard. We've' found that many children out there are ... (click)

Gangster: ... holding my wife for ransom. Those lousy rats! I wouldn't give them ...

(click)

Grocer: ... rotten eggs! You won't find them here. Our eggs are the finest you'll find in any ... (click)

Indy: ... gas tank! It looks like a bad leak. Yes, the gas is going all over his ... (click)

Health: Leotards. They are so comfortable, I wouldn't exercise without them. You might also buy ... (click)

Sesame Street: ... huge shoes for those webbed feet. It's not often we have a duck on our ... (click)

Gangster: ... pizza! Yeah, I got to eat and run. Charlie, don't forget to line up the ...

(click)

Grocer: ... tomatoes in a perfect row. In our meat section yesterday, we caught a man eating a ... (click)

Indy: ... checkered flag! And that's all, folks!
```

---

## IC-1117: Charlie and the Chocolate Factory

- Title: Charlie and the Chocolate Factory
- Author (byline): Roald Dahl
- Work: Not specified
- Publisher: Puffin Books
- Publication date as stated: Aug 1983
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: CHARLIE, GPA JOE, WONKA, NARRATOR 1, AUGUSTUS’ MOM, VERUCA’S DAD, VERUCA, WORKER, GMA JOSEPHINE, GMA GEORGINA, NEWSPAPER BOY, VIOLET, NARRATOR 2, SHOPKEEPER, CROWD MEMBER, AUGUSTUS, AGUSTUS’ MOM, GPJOE
- Teaser before the introduction: Yes
- Spoken words (computed): 1671
- Already set (do not supply): none

### Source block (context only)

```text
Author: Roald Dahl
ISBN: 978-0142410318
Publisher: Puffin Books
Date (Month/Year): Aug 1983
```

### Introduction (context only: never use it for content warnings)

```text
Some things never change. In 1964 when Charlie and the Chocolate Factory was first published, the greatest thing imaginable was gallivanting around a factory devoted entirely to making chocolate and other sweets. And guess what? Over half a century later, that’s still the greatest thing imaginable! AND The willy Wonka Candy Company actually exists! Laffy Taffy, Wonka Bars and Everlasting Gobstoppers! Follow me to a world of pure imagination . . . Charlie and the Chocolate Factory by Roald Dahl
```

### Performance text (classify this)

```text
CHARLIE: (Chapt 2) Is it really true that Wonka’s Chocolate Factory is the biggest in the world?

GPA JOE: True? Of course, it’s true! Good heavens, I thought everybody knew that!

CHARLIE: And is Mr. Will Wonka really the cleverest chocolate maker in the world?

GPA JOE: My dear boy. Mr. Willy Wonka is the most amazing, the most fantastic, the most extraordinary chocolate maker the world has ever seen!

GPA JOE: (Chapt 4) You see, Charlie, not so very long ago there used to be thousands of people working in Mr Willy Wonka’s factory. Then one day, all of a sudden, Mr Wonka had to ask every single one of them to leave, to go home, never to come back.

CHARLIE: He didn’t do that! Why?

GPA JOE: Spies! All the other chocolate makers had begun to grow jealous, and they started sending in spies, pretending that they were ordinary workers. He shut the main gates and fastened them with a chain. Nobody sees him anymore. The only things that come out are chocolates and sweets. *****

WONKA: (Chpt 5) I, Willy Wonka, have decided to allow children to visit my factory this year. These lucky children will be shown around personally by me and they will be allowed to see all the secrets and the magic of my factory. Golden Tickets have been printed and hidden underneath the wrapping paper of ordinary bars of chocolate. They may be anywhere – in any shop, in any town, in any country in the world. Good luck to you all, and happy hunting!

NARRATOR 1: (Chpt 6) The very next day, the first Golden Ticket was found [by] a boy called Augustus Gloop.

AUGUSTUS’ MOM: (With a strong German accent – Actor 2 pantomimes the role of Augustus eating while she speaks) I just knew Augustus would find a Golden Ticket. He eats so many bars of chocolate it was almost impossible for him not to find one. Eating is all he’s interested in. We’re just as proud as anything!

NARRATOR 1: On the day before Charlie Bucket’s birthday, the second Golden Ticket had been found. The lucky person was a small girl called Veruca Salt.

VERUCA’S DAD: (Actor 2 pantomimes Veruca looking very sweet and angelic, while he speaks) As soon as my little girl told me that she had to have one of those Golden Tickets, I started buying up all the Wonka bars I could lay my hands on -- sent them directly to my factory. I had every worker in the place yanking the paper off those bars from morning till night. But three days went by and we had no luck. It was terrible!

VERUCA: (The angelic child turns into a vicious, spoiled brat. Screaming) Where’s my Golden Ticket! I want my Golden Ticket! (She pitches an amazing fit)

VERUCA’S DAD: Well, I just hated to see my little girl feeling unhappy. Then suddenly on the evening of the fourth day . . .

WORKER: I’ve got it! A Golden Ticket! (Actor 2 springs into fit mode as Veruca)

VERUCA’S DAD: Give it to me quick! And I rushed it home and gave it to my darling Veruca. (Veruca smiles angelically) *****

GMA JOSEPHINE: (watching the news on television) That’s even worse than the fat boy

GMA GEORGINA: She needs a really good spanking. *****

NARRATOR 1: That evening . . .

NEWSPAPER BOY: Golden Ticket found today! Only one more left!

VIOLET: (Chpt 8) (chewing gum ferociously, she speaks loud and fast) I’m a gum chewer, normally, but when I heard about these ticket things of Mr. Wonka’s, I gave up gum and started on chocolate bars in the hope of striking lucky.

NARRATOR 2: (Chpt 10) During the next two weeks, the weather turned very cold. (Charlie pantomimes) There came a freezing gale that blew for days. Then one afternoon, walking home, his eye was caught by something silvery lying in the snow. It was a fifty-pence piece! (Charlie snatches it up and races to the corner store)

CHARLIE: (Chpt 11) (Holding out his money to the shopkeeper) One Wonka’s Whipple- Scrumptious Fudgemallow Delight! (the shopkeeper takes the money and hands Charlie the chocolate. Charlie tears off the wrapper)

NARRATOR 2: And suddenly . . . from underneath the wrapper . . . there came a brilliant flash of gold (Charlie responds in shock and awe)

SHOPKEEPER: (excited) You’ve found the last Golden Ticket! Right here in my own shop! (he looks around fearfully) Take it straight home, quickly, before you lose it! Run! (Charlie runs) *****

CHARLIE: (Chpt 12) (Entering his house, waving the ticket) I’ve got it! The last Golden Ticket! It’s mine!

GPA JOE: (startled awake) You’re pulling our legs, Charlie. Having a little joke?

CHARLIE: I am not! (handing the ticket to Grandpa Joe

GPA JOE: (inspects the ticket closely and is silent for a moment, then) Yippeeeeeeee! (in all his elderly glory, the jumps up and does a victory dance) The fifth and last Golden Ticket in the world! (Charlie joins him in a victory dance) You must get ready, my boy . . . for the biggest day of your life! *****

NARRATOR 1: (Chpt 13) On the morning of the big day, all eyes were fixed upon the gates.

CROWD MEMBER: There he is! That’s him!

WONKA: (Chpt 14) (approaches the gates with a little skipping dance, spreading his arms wide) Welcome, my little friends! Welcome to the factory! Who’s first?

VERUCA: My name is Veruca Salt.

WONKA: My dear Veruca! How do you do? You do have an interesting name. I always through that a verruca was a sort of wart that you got on the sole of your foot! (Veruca reacts) But I must be wrong, musn’t I. Please go in. (He speaks to all the children as he ushers them inside) Overjoyed! Enraptured! Enchanted! Excellent! Our tour is about to begin!

NARRATOR 1: (both actors pantomime walking the path) He turned right off the main corridor, then he turned left and left again. Then right. Then suddenly, Mr. Wonka stopped. There was a shiny metal door and on the door in large letters . . . THE CHOCOLATE ROOM.

WONKA: (Chpt 15) (as he unlocks the door) This is the nerve center of the whole factory. In we go! But do be careful! Don’t get over-excited! Keep very calm! (Actor 1 pantomimes the excitement of the children as they see the room) Isn’t it teriffic? A great brown river! There’s enough chocolate in there to fill every bathtub in the entire country! (Actor 1 notices the grass and bends to pick up a blade) The grass is made of a new kind of soft, minty sugar that I’ve just invented! I call it swudge! Try a blade! It’s delectable. (Actor 1 eats and reacts)

VERUCA: Look over there! It’s a little person! Down there below the waterfall! Aren’t they fantastic!

WONKA: They’re Oompa-Loompas – (Chpt 16) Imported direct from Loompaland. They love dancing and music.

VERUCA: Daddy! I want an Oompa-Loompa!

AUGUSTUS: (uninterested in the little men, he sneaks down to the edge of the river and begins scooping the melted chocolate into his mouth as fast as he can)

AGUSTUS’ MOM: (Popping open her umbrella) Augustus, sweetheart, I don’t think you had better do that!

WONKA: (Chpt 17) Oh, no! My chocolate must be untouched by human hands!

AUGUSTUS’ MOM: Augustus! Come away from that river at once!

AUGUSTUS: This stuff is fabulous! (Augustus shrieks as he falls into the river) Help! Help!

AUGUSTUS’ MOM: Don’t just stand there! Do something! (She panics, closes her umbrella and waves it around furiously; then both Actors watch Augustus’ progression down the river and up through large glass pipes until he disappears)

WONKA: (Remaining calm, he turns and snaps his fingers) Keep calm, my dear lady. There is no danger. Augustus has gone on a little journey, that’s all.

AUGUSTUS’ MOM: He’ll be made into fudge. They’ll be selling him by the pound all over the country tomorrow! (She strikes Mr. Wonka with her umbrella)

WONKA: (Fending off the attack) Never! I wouldn’t allow it! The taste would be terrible. Just imagine it – Augustus-flavored chocolate-coated Gloop! No one would buy it. (he turns to an Oompa Looma, who is no taller than his knee) Take Mrs. Gloop to the Fudge Room and help find Augustus . . . (to the tour group) Off we go! *****

NARRATOR 1: (Chpt 18) A steamy mist was rising from the chocolate river and out of the mist there appeared a most fantastic pink, boiled-sweet boat.

WONKA: (ushers the tour onto the boat) Please do not lick the boat. It’ll only make it sticky.

VERUCA: Daddy, I want a boat like this! Buy me a big pink boiled-sweet boat exactly like Mr. Wonka’s! And I want lots of Oompa-Loompas to row me about, and I want a chocolate river and I want . . . I want . . .

GPA JOE: (whispering to Charlie as Veruca silently continues her list of wants) She wants a good kick in the pants. (the boat suddenly picks up speed and the actors react for a few seconds)

WONKA: (waving his hands in the air and shouting) Stop the boat! (actors react) (Chpt 19) (Mr. Wonka leaps from the boat) This is the most important room in the entire factory! The Inventing Room! Not even an Oompa-Loompa has ever been allowed in here. (He gets very excited)

NARRATOR 1: Mr. Wonka [became] even more excited than usual. Anyone could see that this was the room he loved best of all.

WONKA: (rushing to a machine that spits out a candy that looks like a marble; he grabs it up and holds it aloft) Everlasting Gobstoppers! You can put it in your mouth and suck it and suck it and it will never get any smaller!

VIOLET: It’s like gum!

WONKA: (offended) It is NOT like gum. If you tried chewing one of the Gobstoppers, you’d break your teeth off! (But it gives him an idea. Excited again) Now over here is something that I am terrifically proud of! (Chpt 20) (He pushes some buttons on a machine and out comes a strip of gum; he holds it aloft) Don’t you know what it is?

VIOLET: By gum, it’s gum! It’s a stick of chewing-gum!

WONKA: (Chpt 21) This gum is my latest, my greatest, my most fascinating invention! It’s a chewing-gum meal! A whole 3-course dinner all by itself.

VIOLET: Just so long as it’s gum, that’s for me! (She takes her own gum out and sticks it behind her ear and grabs the new piece from Wonka’s hand, pops it in her mouth and starts chewing) It’s tomato soup! Hot and creamy. I can feel it running down my throat.

WONKA: Stop! The gum isn’t ready yet. There are still one or two things . . .

VIOLET: Roast beef! Tender and juicy. Baked potato filled with butter! WONKA; No, no, no . . you musn’t!

VIOLET: Blueberry pie! (As she chews, she begins to plump up just like a giant blueberry) I feel sick! (She looks panicked)

WONKA: (with a heavy sigh) It always goes wrong when we come to the desert. I’ve tried it twenty times on twenty Oompa-Loompas ad every one of them finished up as a blueberry. (He snaps his fingers for an Oompa-Loompa) Roll Miss Beauregarde to the Juicing room at once. We’ve got to squeeze the juice out of her immediately. (He turns back to the tour) (Chpt 22) Well, well, well . . . two naughty little children gone. I think we’d better get out of this room quickly before we lose anyone else! *****

WONKA: (Chpt 24) All right, take a peek through the glass panel. But whatever you do, don’t go into THE NUT ROOM! You’ll disturb the squirrels.

VERUCA: (peering through the window she whines to her dad) Squirrels!

WONKA: Specially trained squirrels for getting the nuts out of walnuts.

VERUCA: I want a squirrel! Get me one! I want a trained squirrel!

VERUCA’S DAD: (pulling out his checkbook) Very well, Wonka, how much d’you want for one of these squirrels? Name your price.

WONKA: They’re not for sale. She can’t have one.

VERUCA: Who says I can’t! I’m going in to get myself one this very minute! (She stomps off stage and we hear her scream)

WONKA: (Peering through the window) Watch! They’re testing her to see if she’s a bad nut. (Veruca screams off stage again) (Shaking his head) My goodness, her head must have sounded quite hollow. She IS a bad nut. Down the rubbish chute

(Vercua screams again and it fades away) Too late. She’s gone!

VERUCA’S DAD: But where? What happens to the bad nuts? Where does the chute go?

WONKA: To the furnace, of course . . . but Don’t worry. There’s always a chance that they decided not to light it today.

VERUCA’S DAD: Now see here, Wonka. My daughter may be a frump – I don’t mind admitting it – but that doesn’t mean you can roast her to a crisp. I’m extremely cross about this, (winks at Wonka) I really am. (celebrates silently as he turns away) *****

WONKA: (Chpt 28) (Actor 1 portrays a humble Charlie listening respectfully) We must get going! How many children are there left now?

GPJOE: But Mr. Wonka, there’s only Charlie left now.

WONKA: You mean you’re the only one left? (pretending to be surprised)

CHARLIE: Why, yes. Yes!

WONKA: My dear boy! That means you’ve won! (He shakes Charlies hand furiously) Well done, Charlie, well done! (Chpt 30) How I love my chocolate factory. Do you love it too, Charlie?

CHARLIE: Oh, yes. I think it’s the most wonderful place in the whole world!

WONKA: (Wiping a tear from his eye) I am very pleased to hear you say that. And now I shall tell you why. As soon as you are old enough, the entire factory will become yours! (Charlie reacts) I don’t want a grown-up . . . I have to have a child to whom I can tell all my most precious secrets.

CHARLIE: So that is why you sent out the Golden Tickets?

WONKA: Exactly! I decided to invite children to the factory and the one I liked best would be the winner! We must fetch the rest of the family. They can all live in the factory from now on!

CHARLIE: The most wonderful place in the whole world!
```

---

## IC-1118: Charlie the Caterpillar

- Title: Charlie the Caterpillar
- Author (byline): Dom DeLuise
- Work: Not specified
- Publisher: Aladdin
- Publication date as stated: April 1993
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, CHARLIE, MONKEY 1, MONKEY 2, RABBIT 1, RABBIT 2, MOUSE 1, MOUSE 2, KATIE
- Teaser before the introduction: Yes
- Spoken words (computed): 846
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dom DeLuise
ISBN: 978-0671796075
Publisher: Aladdin
Date (Month/Year): April 1993
```

### Introduction (context only: never use it for content warnings)

```text
Sticks and stones can break my bones, but words will never hurt me. – Well, the first part is true, but the second part is completely wrong.

When I was in grade school, I had to get glasses . . . then in middle school it was braces and the horrible transition of puberty when your bones grow too fast for you to NOT be clumsy and you get pimples and the braces make you lisp and you get food caught in your teeth that you don’t even know is there and then Grandma Connie sends you the most hideous Christmas sweater, but you have to wear it because it was a gift . . . It happens to everyone, right? And no one, not one single person ever made fun of me . . . Is my nose growing yet? Just what I need!

In Charlie the Caterpillar, we experience the perils of growing up in a society that would rather make fun of you than to build you up.

Charlie the Caterpillar by Dom DeLuise
```

### Performance text (classify this)

```text
NARRATOR: One day, one bright sunny day, Charlie the Caterpillar was born. (Charlie is born) The world looked very, very big to Charlie because he was very, very small. Charlie soon found out how delicious green things tasted. (Charlie nibbles on a blade of grass) He could hear the wind whistling and the birds singing. (Charlie smiles) He was glad to be alive. Charlie decided to set out and see the world, so he looked to the left, and he looked to the right and then he went straight ahead. Soon Charlie saw two monkeys.

CHARLIE: Hi! What are you doing?

MONKEY 1: We’re playing cards.

CHARLIE: Oh, that sounds like fun. Can I play too?

MONKEY 2: No, you can’t.

CHARLIE: Why not?

MONKEY 1: Because you’re an ugly caterpillar. Now get out of here.

MONKEY 1: (echoing voice) . . . Because you’re an ugly caterpillar . . . .

NARRATOR: Charlie, for the very first time in his young life, felt bad. (Charlie sighs heavily) He would have shrugged his shoulders if he had any. He looked to the left, and he looked to the right and then he went straight ahead. Pretty soon he saw two rabbits hopping around.

CHARLIE: Hi! What are you doing?

RABBIT 1: We’re playing tennis.

CHARLIE: Oh, that looks like fun. Can I play too?

RABBIT 2: No, you can’t.

CHARLIE: Why not?

RABBIT 1: Because you’re an ugly caterpillar, and we don’t play with ugly caterpillars. Now, get out of here.

NARRATOR: Now, for the second time in his young life, Charlie felt bad, very bad. His feelings were hurt.

CHARLIE: (to himself) What is ugly?

NARRATOR: He didn’t feel ugly. He looked to the left, and he looked to the right and then he went straight ahead. Just then, Charlie saw two mice playing miniature golf.

CHARLIE: Hi! What are you doing?

MOUSE 1: We’re playing golf.

CHARLIE: Oh, that really looks like fun. Can I play too?

MOUSE 2: No, you can’t.

CHARLIE: Why not?

MOUSE 1: Because you’re an ugly caterpillar, and we really don’t play with ugly caterpillars. Now, get out of here.

NARRATOR: Charlie, for the third time in his not-so-young life, felt very, very bad. In fact, Charlie started to feel ugly. No one wanted to play with him. So Charlie looked to the left, and he looked to the right and then he started to cry.

CHARLIE: (crying)

NARRATOR: Charlie wanted to be alone. He climbed up a tree and snuggled up to a small branch. (Charlie climbs, he sits shivering) He felt a little cold, so he went like this (Charlie begins spinning a cocoon) and he went like that, and he went like that, and he went like this, and he went like that, and before he knew it, he had spun himself a warm and wonderful cocoon.

CHARLIE: (sadly) Why can’t I have a friend. (exhausted, he drifts off to sleep)

NARRATOR: All of a sudden, snow began to fall and cover everything with white. Winter had come, but Charlie was nice and warm in his comfortable cocoon. Charlie dreamed that he had a best friend, and in his dream they laughed and had fun together. (Charlie laughs in his sleep) After a while, the grass began to grow, the flowers began to bloom and the birds began to have a party in the sky. Spring had come and somehow Charlie knew it was time to wake up. (Charlie yawns and stretches) And then -- oh, my goodness! (Pop, pop – his wings unfurl one at a time; and Charlie is in awe, looking first left then right) He had wings! Beautiful wings! Charlie had become a beautiful butterfly. (Charlie flutters his wings and flies, laughing) He flew up, up and up. He soared past the birds having a party in the sky. Charlie was flying high when he came upon the monkeys who were still playing cards.

MONKEY 2: (begging) Oh, please come and play with us!

CHARLIE: Why?

MONKEY 1: Because you’re a beautiful butterfly.

CHARLIE: No, thanks. I gotta get outta here! (He zooms away and the monkeys jump back, looking miserable) Serves them right!

NARRATOR: He did a couple of loopy loops and then he came across the rabbits at their tennis game.

RABBIT 2: Oh, please, won’t you come and play with us?

CHARLIE: Why?

RABBIT 1: Because you’re such a beautiful butterfly!

CHARLIE: Not on your life. Now I gotta get outta here! (he flies off, leaving the rabbits looking very down-hearted) Serves them right!

NARRATOR: He didn’t want to play with them because they were quite mean to him when he was a caterpillar. He circled around for a while and then he saw the mice playing miniature golf.

MOUSE 2: (pleading) Please, please, pretty please, do come and play with us.

CHARLIE: Why?

MOUSE 1: Because you’re really such a beautiful butterfly!

CHARLIE: Sorry, not today. I really have better things to do. Now I gotta get outta here! (he soars off, leaving the mice looking pitiful) Serves them right!

NARRATOR: They all wanted to be his friend because he was now a beautiful butterfly. They didn’t know he was Charlie, the ugly caterpillar.

CHARLIE: If they want to be my friends just because of my beautiful wings, they can’t be real friends.

NARRATOR: And just then Charlie heard someone crying. It was Katie the Caterpillar.

KATIE: (crying with gusto)

CHARLIE: Why are you crying?

KATIE: Because no one will play with me. No one wants to be my friend because I’m an ugly caterpillar.

CHARLIE: (winking and smiling) I’ll play with you. I’ll be your friend.

KATIE: You will? Whoopeee!

NARRATOR: And then Charlie took Katie aside and told her all about becoming a butterfly. Charlie showed Katie what she will look like when she’s a butterfly. (they look in the surface of a small lake, Charlie standing behind her so that her reflection would show up like a mirror in the water) And that made Katie feel good. From that day on, Charlie and Katie played cards and tennis and even miniature golf together. (laughing) They had a good time just like in Charlie’s dream. Katie was happy and Charlie was very happy. He had finally found a friend . . . a real friend . . . a best friend.
```

---

## IC-1119: Charlotte’s Web

- Title: Charlotte’s Web
- Author (byline): E.B. White
- Work: Not specified
- Publisher: HarperCollins
- Publication date as stated: April 2012
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: CHARLOTTE, FERN, MR. ARABLE, MR. ZUCKERMAN, NARRATOR, WILBUR, GOOSE, LAMB, TEMPLETON, SHEEP, MRS. ARABLE, GANDER, LOUDSPEAKER, FAIR OFFICIAL
- Teaser before the introduction: Yes
- Spoken words (computed): 1302
- Already set (do not supply): none

### Source block (context only)

```text
Author: E.B. White
ISBN: 978-0061232916
Publisher: HarperCollins
Date (Month/Year): April 2012
```

### Introduction (context only: never use it for content warnings)

```text
Charlotte’s Web by E.B White is one of the all-time great classics of children's literature. It’s gentle story with its kindly wisdom about friendship and love has survived and prospered for decades. Why? Because its themes are universal and timeless: Growing up, death . . . and most importantly the power of friendship. In the words of E.B. White, “Friendship is one of the most satisfying things in the world.”

Charlotte’s Web by E.B. White
```

### Performance text (classify this)

```text
CHARLOTTE: (Pg 164) After all, what’s a life, anyway? We’re born, we live a little while, we die. *****

FERN: (Pg 2-4) Please don’t kill it! It’s unfair!

MR. ARABLE: (Holding a very small pig) Fern, you will have to learn to control yourself.

FERN: (Yelling) Control myself? This is a matter of life and death, and you talk about controlling myself.

MR. ARABLE: I know more about raising pigs than you do. A weakling makes trouble.

FERN: The pig couldn’t help being born small, could it? If I had been very small at birth, would you have killed me?

MR. ARABLE: This is different.

FERN: I see no difference. This is the most terrible case of injustice I ever heard of.

MR. ARABLE: (reconsidering) All right, he’s yours. (Hands the pig over to Fern) Start it on a bottle, like a baby. You’ll see what trouble a pig can be. (Strides off)

FERN: (Petting the little pig) He’s absolutely perfect! (thinking) (Pg 7) Wilbur . . . it’s name is Wilbur! *****

CHARLOTTE: (Enters via her web) Salutations! (Pg 101) (She spins some web, obviously writing something)

MR. ZUCKERMAN: (Pg 115) (looks in awe as the spiderweb) That pig is radiant! *****

CHARLOTTE: (Pg 164) After all, what’s a life, anyway?

MR. ARABLE: (Pg 12) He’s got to go, Fern. (attempts to lift Wilbur and cannot) You have had your fun, but Wilbur is not a baby any longer. (he drops him with a thump) Tell your Uncle Homer you’ve got a pig you’ll sell and see what he says.

NARRATOR: The next day Wilbur was taken from his home and went to live in a manure pile in the cellar of Zuckerman’s barn.

WILBUR: (Pg 16) (wandering outside; lonely and bored – he oinks) There’s never anything to do around here. (Pg 28-29) (to the goose) Will you play with me?

GOOSE: (clucking and speaking rapidly and repetitively) Sorry, sonny, sorry. I’m sitting on my eggs.

WILBUR: (to the lamb) Will you please play with me?

LAMB: (Baa’s disdainfully) Certainly not. I don’t play with pigs! Go play by yourself!

WILBUR: (to Templeton, the rat) Will you play with me, Templeton?

TEMPLETON: Play? I hardly know the meaning of the word.

WILBUR: Well, it means to have fun, to frolic, to run and skip and make merry. (he demonstrates)

TEMPLETON: I never do those things! I prefer to spend my time eating, spying and hiding.

WILBUR: (Heavy sigh and dejected oinking) (Pg 16) I’m less than two months old and I’m tired of living. (he sobs in an oinking manner)

CHARLOTTE: (Pg 31) Do you want a friend, Wilbur? I’ll be a friend to you. I’ve watched you all day and I like you!

WILBUR: (sobbing subsides) But I can’t see you. Where are you? And who are you?

CHARLOTTE: I’m right up here. (she descends, spinning her web) (Pg 35) Salutations!

WILBUR: Salu-what?

CHARLOTTE: Salutations! It’s my fancy way of saying hello! (Pg 36-39) Look up here in the corner of the doorway! I’m waving! (she waves) See me now?

WILBUR: Salutations! May I have your name?

CHARLOTTE: My name? My name is Charlotte.

WILBUR: I think you’re beautiful.

CHARLOTTE: Well, I am pretty. There’s no denying that. All spiders are rather nice-looking.

(she notices a fly trapped in her web) Watch me wrap up this fly! (Fly beats its wings furiously, buzzing) First, I dive at him. (She plunges on a silken thread) Next, I wrap him up (She does so and the buzzing becomes muffled) Now I knock him out, so he’ll be more comfortable. (She bites the fly) He’ll make a perfect breakfast for me.

WILBUR: (gasping) You mean you eat flies! . . . Do they taste good?

CHARLOTTE: Delicious. I don’t really eat them. I drink them. Drink their blood. I love blood!

SHEEP: (Pg 49-51) (entering) Hello! Seems to me you’re putting on weight. You know why they’re fattening you up, don’t you?

WILBUR: No

SHEEP: Well, I don’t like to spread baaaaad news, but they’re going to kill you.

WILBUR: They’re going to what?

SHEEP: Kill you. Turn you into smoked bacon. All young pigs get murdered by the farmer as soon as the cold weather sets in. Christmastime . . . pig . . . ham . . . Kill you!

WILBUR: (squealing and crying) I don’t want to be killed. I don’t want to die! Is it true, Charlotte? Are they going to kill me when the cold weather comes?

CHARLOTTE: Well, the old sheep has been around this barn a long time. If she says they plan to kill you, I’m sure it’s true. (Wilbur wails) Stop your crying! I can’t stand hysterics. You shall not die.

WILBUR: What? Really? Who’s going to save me?

CHARLOTTE: I am!

WILBUR: (suspicious) [But] how?

CHARLOTTE: That remains to be seen. (Pg 63) (Deep in thought) I’m working on it! ******

FERN: (Pg 105) Charlotte is the best storyteller I ever heard

MRS. ARABLE: Fern, you know spiders don’t tell stories. Spiders can’t talk.

FERN: Charlotte can. She doesn’t talk very loud, but she talks!

MRS. ARABLE: (Pg 106-107) Fern, I wish you would play outdoors instead of going to Uncle Home’s barn. You’re spending too much time in that barn. It isn’t good for you to be alone so much.

FERN: Alone? My best friends are in the barn cellar! (Pg 71) I’m going to visit Wilbur! ******

CHARLOTTE: (Pg 75-76) (moodily thinking, then she comes up with an idea. She descends to the center of her web and begins to cut some of her lines. She starts weaving a message, snipping lines and repositioning others . . . as she works to create her masterpiece she hums or sings) (Pg 94) Up we go! Attach! Descend! Whoa! Good! Now right and down and swing that loop around and around! Now in to the left! Attach! Climb! Repeat! O.K.! Good girl!

(When she is finished she celebrates and then exhausted, sleeps) ******

MR. ZUCKERMAN: (Pg 78-80) (He and Fern are bringing food for the animals, he notices the web and stops dead in his tracks. He sets down his pail and rums his eyes – Fern stands in awe, unable to speak) I’m seeing things! Some Pig! (stares for a long time at Wilbur then drops to his knees in awe) We have received a sign– a mysterious sign. A miracle has happened on this farm! We have no ordinary pig! SOME PIG!

NARRATOR: (Pg 84) The news of the wonderful pig spread clear up to the hills and farmers came down in buggies to stand at Wilbur’s pen, admiring the miraculous animal. They had never seen such a pig in their lives!

MR. ZUCKERMAN: (Pg 96) Lurvy! Phone the reporter on the Weekly Chronical and tell him what has happened. He may want to bring a photographer . . . There is to be no more cow manure thrown down into that pigpen. I want that pig to have clean, bright straw every day! Start building a crate for Wilbur. I have decided to take [him] to the County Fair! Zuckerman’s Famous Pig! *****

CHARLOTTE: (Pg 86-87) (calls a meeting of all the animals) I shall begin by calling the roll. Wilbur?

WILBUR: Here!

CHARLOTTE: Gander

GANDER: Here, here, here!

CHARLOTTE: Why do you have to repeat everything?

GANDER: It’s my idio-idio-idosyncrasy!

CHARLOTTE: Sheep?

SHEEP: He-aa-aa!

CHARLOTTE: Templeton? (no answer) Templeton? (no answer) Well, I guess we can proceed without the rat. (With great fanfare) The message I wrote in my web, praising Wilbur has been received. The Zuckermans and everybody else has fallen for it. Zuckerman thinks Wilbur is an unusual pig and therefore he won’t want to kill him and eat him. My trick will work and Wilbur’s life can be saved.

WILBUR: Hurray! *****

WILBUR: (Pg 115-116) You’re going with me, aren’t you, Charlotte? I need you, Charlotte. You’ve just got to come!

CHARLOTTE: No, I believe I’d better stay home and get some egg laying done.

WILBUR: (amazed) I didn’t know you could lay eggs. Why don’t you come with me to the Fair Grounds and lay your eggs there?

CHARLOTTE: (Pg 122) [Then] I shall go, too. We can’t tell what may happen at the Fair Grounds. Somebody’s got to go along who know how to write. Pg 127 (the geese cheer) ****** at the fair ******

LOUDSPEAKER: (Pg 130) Attention, please! Will the owner of a Pontiac license number H-2439 please move your car away from the fireworks shed!

WILBUR: (Pg 134-135) (Charlotte climbs to the rafters at the fair) What do you see?

CHARLOTTE: There’s a pig in the next pen and he’s enormous! Much bigger than you are.

WILBUR: (whimpers as tears come to his eyes)

CHARLOTTE: He’s not anywhere near as clean as you are, nor as pleasant. He’s going to be a hard pig to beat, though, Wilbur, on account of his size and weight. But with me helping you, it can be done!

WILBUR: When are you going to spin a web?

CHARLOTTE: I shall be writing tonight for the last time. (She starts weaving a message, snipping lines and repositioning others . . . as she works to create a new word, she hums or sings) (Pg 141) Humble!

WILBUR: (Pg 142) (humbly) Charlotte, do you really thing Zuckerman will not keel me when the cold weather comes? Do you really think so?

CHARLOTTE: (exhausted) Of course. Tomorrow you will probably win a prize. The whole world will hear about you. You have nothing to fear, Wilbur. *****

FAIR OFFICIAL: (Pg 158) Ladeez and gentlemen! On behalf of the Fair, I have the honor of awarding a special prize of 25 dollars and a handsome bronze medal to this pig. This radiant, this terrific, this humble pig. (Pg 160) (he places the medal around Wilbur’s neck. Wilber snorts and grins) *****

WILBUR: (Pg 163-164) (after everyone had gone) Charlotte! Charlotte! (he’s taken aback by the silence) Do you feel alright?

CHARLOTTE: A little tired, perhaps. But peaceful . . . Nothing can harm you now.

WILBUR: (with tears in his eyes) Oh, Charlotte. Why did you do all this for me? I don’t deserve it. I’ve never done anything for you.

CHARLOTTE: You have been my friend, Wilbur . . . this lovely world, these precious days. After all, what’s a life anyway? We’re born, we live a little while, we die.

WILBUR: (Pg 165) Charlotte, what are you talking about?

CHARLOTTE: I’m done for. In a day or two I’ll be dead.

WILBUR: (Pg 164) Well, I’m no good at making speeches. I haven’t got your gift for words. (sadly) But you have saved me, Charlotte, and I would gladly give my life for you – I really would.

CHARLOTTE: (Pg 165) I’m sure you would. And I thank you . . . (Pg 171) (whispers) Good-bye

(Charlotte dies)

WILBUR: Charlotte? (no response; Wilbur oinks sadly) ******

NARRATOR: (Pg 184) It’s not often that someone comes along who is a true friend and a good writer. Charlotte was both.
```

---

## IC-1120: Check, Please

- Title: Check, Please
- Author (byline): Jonathan Rand
- Work: Laugh Lines: Short Comic Plays, Pg 301-334
- Publisher: Vintage
- Publication date as stated: April 2007
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: GUY, MELANIE, MIMI, LINDA
- Teaser before the introduction: Yes
- Spoken words (computed): 903
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jonathan Rand
Book: Laugh Lines: Short Comic Plays, Pg 301-334
ISBN: 978-0307277138
Publisher: Vintage
Date (Month/Year): April 2007
```

### Introduction (context only: never use it for content warnings)

```text
Let’s face it . . .The dating landscape is a minefield. . . . and let’s not even talk about blind dates! The concept of a blind date to me, even in its simplest most casual form just has “disaster” written all over it. You say to yourself: But surely my loved ones and trusted acquaintances can help navigate this treacherous world and find me a suitable mate amongst their social networks. You are wrong. Soooo wrong! Some blind dates take it from simply bad to absolutely horrific.

Check, Please by Jonathan Rand
```

### Performance text (classify this)

```text
GUY: (Pg 301-334) Hi. It's so great to finally meet you.

MELANIE: (MELANIE is truly sweet and adorable when she's focused on the date.) Hi. Same here!

GUY: SO ... What do you-

MELANIE: Wait, before you ... sorry. (Meekly.) This is so rude, but the Bears game is on right now? You don't mind if I check the score ...

GUY: Oh, sure. Totally.

MELANIE: (As she pulls out her cell phone to check her web browser.) I know this is such an awful thing to do on a first date, but it's late in the fourth quarter, and it's do-or-die if we wanna make the playoffs.

GUY: It's no problem at all. Really.

MELANIE: Thanks. (As she checks.) I love the Bears. They're really strong this season. (Sees score; reacts a little.) Okay, I'm done. (Cheerily.) That wasn't so bad, was it?

GUY: What's the score?

MELANIE: Packers by seven. It's no big deal. It's just a game, right? So, c'mon, enough about football. Let's hear about "Mister Mystery." Harriet's told me tons about you.

GUY: Man ... The pressure's on now. (They laugh together genuinely. MELANIE laughs then fades directly into her next line, which is suddenly serious.)

MELANIE: I'm just gonna check on the game one more time. (She digs into her purse.) Is it all right with you if I put on this little earpiece thingy? It won't be distracting, I promise. (As she puts the earpiece in her ear.) I'm making the worst first impression, aren't I?

GUY: Not at all.

MELANIE: It's just because it's for the playoffs. I'm usually pretty normal. (Throws her hands up.) Ah! The line gives A-Train this huge running lane, but he fumbles after two yards. The ball rolled out of bounds, so we're cool, but come on-it's for the playoffs. You don't just drop the ball like that, you know? Now you're third and long, and the whole season is riding on one play. PASS THE BALL!!

GUY: What's wrong?

MELANIE: Miller! He doesn't pass it. It's third and long-who hands it off on third and long? Is he suddenly AFRAID OF HIS RECEIVERS?! (GUY looks around subtly at the other patrons.) Oh my God, I'm sorry. I'm being loud, aren't I. PASS THE BALL!! Jesus, people! This is FOOTBALL, not FREEZE TAG. It's FOURTH DOWN pass the FRIGGING BALL!

GUY: Listen, we could go to a bar or something if you want to watch the game on TV.

MELANIE: Oh please, no. I wouldn't do that to you. The game's basically over. (She takes a deep breath and is now very calm.) Okay. I'm done. I got a little carried away there, didn't I? Let's order. (They peruse for a moment, as if nothing has happened.)

(Downtrodden.) They lost ... (Starting to tear up.) They lost. (MELANIE breaks down. GUY takes out a handkerchief and offers it to MELANIE. She uses it to blow her nose.)

GUY: I'm so sorry. Can I do anything to help?

MELANIE: (Still weepy.) The Bears suck ...

GUY: Aww, no. They don't suck. They're probably just having a bad season- (MELANIE grabs his collar, pulls him extremely close, and speaks in a horrifying, monstrous, deep voice.)

MELANIE: THE BEARS SUCK.

GUY: Check, please.

**********

(GUY is sitting across the table from a fully outfitted mime, MIMI, who throughout the scene is extremely over-the-top and exuberant. The scene begins with MIMI "leaning" on "something." Mimed actions in this scene will be indicated with brackets. A few moments pass as we get a feel for the ridiculousness of the scenario.)

GUY: So what do you do for a living? (Beat.)

MIMI: [Pulling something heavy with a rope.]

GUY: You pull rope. (Pause.) Look ... I respect your profession and all? I think it's noble what you do .... The world needs more people who ... climb invisible ladders and pull imaginary ropes. But I really don't see how it's appropriate to bring your work to a date.

MIMI: [Battling against harsh winds.]

GUY: Oh, yeah, quite a storm in here. Listen, I'm gonna go ahead and order.

(GUY opens his menu and reads. MIMI gets past the storm and mimes picking up an imaginary menu, proceeding to peruse, turning page after page. GUY looks up. There is silence as he watches MIMI do her thing.) Hey, I'm gonna go ... use the restroom. (GUY gets up, takes his jacket from the back of the chair.)

MIMI: [You're leaving? Driving away? Far? Bye-bye?]

GUY: No, I'm not leaving. I'm taking my jacket with me because ... it might get cold in the men's room.

MIMI: [Cold like me in this wild blizzard?]

GUY: Yeah, exactly like that. (GUY starts to leave. MIMI follows close behind, maybe as an airplane pilot or a bus driver.)

GUY: No, you stay here. You-

MIMI: [Let me feed some chickens. Awww, those chicks are adorable. I love petting these lovely animals.]

GUY: I don't know what that is .... Look, I have to- (An idea dawns on GUY. The following is an extremely loud and animated sequence of events-very frantic for MIMI; sarcastically frantic for GUY.) (Looking up.) Oh my God! A BOX!

MIMI: [Where? Where?]

GUY: A huge glass box, falling from the sky!

MIMI: [Oh no! Oh no! I can't see it! What in heaven's name will I do? Help me, Lord!]

GUY: Noooooooo! (GUY follows "the box" with his finger as it plops directly on the frantic MIMI, who is now very much "trapped.") Check, please. **********

LINDA: Hi. I've been looking forward to this for a while.

GUY: Me, too. Sorry about all the rescheduling.

LINDA: Pssh, whatever, it's cool. Oh, shoot. Hold on. I forgot to (She starts rummaging through her purse, and after a couple if seconds, starts removing objects: compact, lipstick, etc.)

GUY: What's up? What's wrong?

LINDA: Oh, it's this silly thing. I've got this pill I need to take or else I get all weird. (Back to her purse.) I know I brought them. They've gotta be-- You know, whatever. I'll be fine.

GUY: You sure? I could drive you to a pharmacy or something.

LINDA: Nah, it's no big deal. It's just a precautionary drug, you know? It won't kill me if I don't take it for one night. I just may be a little out of whack. You probably won't even be able to tell. Whatever. So-anyway . . . It's nice to finally meet you.

GUY: The feeling's mutual.

LINDA: (Suddenly sarcastic, morose, in a monotone voice.) Oh, yes. It's so wonderful to finally put a name with a face. How wonderfully fascinating.

GUY: Heh. Yeah. Seriously.

LINDA: (Giggly/bubbly.) Hee hee hee. You're funny. You're cute. (Gruff.) He's not cute. You just haven't been out in a while. (Snobby.) That is NOT TRUE. He is GOOD-LOOKING. (Bashful.) No ... No ... He's- (Sensual.) Oh, you are absolutely right. He is a hunk of man. (Jittery.) Shhhhhhhh ... You're embarrassing yourself ... (Gruff.) Quit freaking out, man. (Easily offended.) Wha? Wha? Why are you jumping all over me? (Little girl.) She started it! (Motherly.) Girls, please don't fight.

GUY: Excuse me. Are you gonna be okay?

LINDA: (Pissy, to GUY.) You stay out of this! (Reasonable.) Hey, leave him alone. You just met him. (Gruff.) Oh, he can take care of himself (Sarcastic.) Way to ruin a magical evening. (Sensual.) Mmmmm ... The evening's about to get a lot more magical. (Motherly.) You'd better behave yourself, young lady, or you're grounded.

GUY: (GUY notices a bottle under a napkin and shows it to LINDA.) Hey, are these the pills?

LINDA: (Cheery.) There they are! (Pissy.) Yeah, too little too late. (Sensual.) You are so sweet to find them! (Peppy.) Yeah! YEAH! (Sarcastic monotone.) Whoop-dee-doo. (LINDA swallows the pill.)

GUY: Is everything all right?

LINDA: (Mostly back to normal, but woozy.) Whoa. Uh. Okay. Okay. It's starting to kick in. In a couple of seconds, the medicine'll take effect and I'll settle into a single personality. But don't worry-like, ninety-nine times out of a hundred, it's one of the normal ones. (LINDA suddenly lets out a shriek, grabs some bread from the table, sniffs it voraciously, stuffs it in her mouth, and lumbers offstage. Pause.)

GUY: Check, please.

(Note: LINDA's personality switches should be fast. Each personality should be a different level-her voice and demeanor should be changing dramatically throughout.)
```
