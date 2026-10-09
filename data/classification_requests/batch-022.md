# Classification request: batch 22 of 53 (40 records, IC-1241 to IC-1280)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-022-reply.json`.

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

## IC-1241: The Book of Leviticus Show

- Title: The Book of Leviticus Show
- Author (byline): Christopher Durang
- Work: Twenty-Seven Short Plays, Pgs 110-113
- Publisher: Smith and Kraus
- Publication date as stated: Jan 1995
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: VOICE OVER, LETTIE LU, GRANDMA
- Teaser before the introduction: No
- Spoken words (computed): 1014
- Already set (do not supply): none

### Source block (context only)

```text
Author: Christopher Durang
Book: Twenty-Seven Short Plays, Pgs 110-113
ISBN: 978-1880399897
Publisher: Smith and Kraus
Date (Month/Year): Jan 1995
```

### Introduction (context only: never use it for content warnings)

```text
(Solemnly) Leviticus 19:18 “Thou shalt love they neighbor as thyself.” But that’s only one nugget of wisdom found in the Bible. There’s so much more about how humanity must live to be right with God and one another. But, really, who reads anymore? *According to the National Literacy Institute, 21% of adults in the US are illiterate and 54% read below the 6th grade level. Maybe there should be a TV show (or at least a Podcast, Tick Tock or You Tube video series) to keep us on track . . .

(Announcer’s voice) Welcome to Channel 61 in Wheeling, West Virginia! If you’ve ever wondered what would happen if the FCC, the Good Book, and a clearance-sale camcorder teamed up for a revival meeting in a roadside motel, you’ve found the right channel! Broadcasting live -- the premiere episode of “The Book of Leviticus Show!”

The Book of Leviticus Show by Christopher Durang
```

### Performance text (classify this)

```text
VOICE OVER: (Pgs 110-113) The West Virginia Community Public Access Station is in no way responsible for the content of any program on this channel. The views expressed belong to the public access individual producers. By law we must broadcast whatever people want to say. If we could shut down this entire public access station, we would be glad to. But by law we can't.

(A rundown motel room in West Virginia. A bed with an elderly Grandma asleep on it. An empty bird cage. Suitcases around, opened, not quite unpacked. Lettie Lu is wandering around with lots of nervous energy. Her husband Tommy is running the camera)

LETTIE LU: (to the camera) Are we on the air? Hello there. Can you hear me? If you can't hear me, call 556- 421, and ask for Lettie Lu in Room 12, and then I'll talk up. This here is our first show, and so I don't know if I need to shout.

And this is Momma. (Grandma snores obnoxiously) Momma is eighty-three years old and she brought me up all her life in West Virginia and she's a good woman. I'm Lettie Lu and this is the first Book of Leviticus Show installment. (sing a few lines from a hymn)

Now I was minding my business back in Tommy's and my house in West Virginia. The children had growed up, one of them is a country Western star, one of them is a teller in a bank. Jimmy, he hasn't found himself yet, he don't do nothing. But we were havin' our quiet life when God set our house on fire. Well, it wasn't God really, it was Momma; leastwise, we think it was Momma, she denies it, but who else was up cookin' at two in the morning, not me or Tommy, we wuz asleep.

But our house burned to the ground, all of it; and we wuz real bitter. We slept in the truck for a couple of nights, but then I said to Tommy, "What are we complainin' about, we got our lives. God gave us our lives, and we have got to be grateful."

And then we took the Bible out of the glove compartment, and I said, "Tommy, this is God's word, and it will comfort us." (picks up the Bible and shows the camera) You know, you can open up the Bible to any old page and it will have a message for you.

(chooses a section at random) Like here, in the Book of Numbers: (reads with difficulty) "And the names of the men are these: of the tribes of Judah, Caleb the son of Jephunneh. And of the tribe of of Simeon, Shemeul, the son of Annihud. . . " Well, this here don't mean a thing!

But then we read that lovely passage about the Lord is thy shepherd and the green pastures . . . and we had some money in the bank, so we thought we'd just come on over to this motel, where the owner is a good Christian woman and her daughter with the harelip, but really it doesn't look bad if you don't look at it. And then Tommy said, "Lettie, read another passage from the Bible."

And then I turned to the Book of Leviticus. (reads with great importance) "And the man that committeth adultery with another man's wife, even he that committeth adultery with his neighbor's wife, the adulterer and the adulteress shall surely be put to death."

Well, that made a lot of sense to us because in all our years of marriage, and I married Tommy when I was fourteen or something just like Loretta Lynn did 'ceptin' I don't sing none; well, in all that time, Tommy and I has never been unfaithful to one another because we believe in God and religion and marriage. And I got to thinkin' about how people say they believe in the Bible but they don't follow through and do nothin' about it.

(flips through the Bible again) Oh yeah. This is from the same page as the thing about adul-tery. (reads) "And if a man also lie with mankind, as he lieth with a woman, both of them have committed an abomination, they shall surely be put to death." (slams the Bible shut)

Well, we checked with the minister about the wordin' just to make sure we understood, but what we thought was true was true: This is about (whispers) homo[sexuals]! And notice that God says surely someone will put them to death. He just presumes somebody's gonna do it for him!

We've gotten mighty far from followin' God's commands.

So what we done is, we went to Sally Bowden's house, and she's got herself two strappin' big sons, Big Jake and Big Harry, and we went into town and Big Jake and Big Harry went out and they captured an adulteress and a homo[sexual] for us, and they tied 'em up and brung 'em here. I mean, they're here right now. (Lettie Lu moves a screen. Behind it, tied up on the floor and with gags in their mouths, are a Woman and a Man) See? I kept 'em behind the screen to add to the suspense. I hope you like our show.

So now we're going to follow the teachings of God in the Book of Leviticus. Wake up, Momma. (goes over to Grandma, tries to wake her; to Grandma) Momma. God, I hope she's not dead. (Grandma snorts) Oh, there she goes. You havin' a dream, Momma?

GRANDMA: Where's my teeth?

LETTIE LU: Well, did you go to sleep with them in your mouth, or did you take them out first?

GRANDMA: I don't know where they are.

LETTIE LU: We know that, Momma. We are on television, and nobody out there wants to hear about your teeth.

GRANDMA: I had a dream about pancakes.

LETTIE LU: Pancakes? Oh, Momma, you're irritatin' everybody. (gets a gun from somewhere easy) Old age is a terrible thing. (gets in a position, aims at the two people on the floor. Aims, but maybe looks the other way; she's not bloodthirsty, just doing her best to follow the Bible) Pay attention now, Momma, we're gonna kill 'em. (Grandma puts her fingers in her ears) In the name of God's will, you shall surely be put to death. (fires the gun twice)

GRANDMA: Do we know these people?

LETTIE LU: (annoyed to explain it again) We met 'em in town, Momma, Jake and Harry tied 'em up, and I read in the Bible that God wanted somebody to kill 'em.

GRANDMA: (understanding) Oh.

LETTIE LU: (to camera) Well, I'm gonna sign off now. Read your bible, follow everything it says. And next week, we're gonna do the part from the Book of Leviticus about how to sacrifice turtle doves to please God.

GRANDMA: Where we gonna get a turtle dove?

LETTIE LU: I don't know. Maybe Woolworths'll have one of those 98 cents parakeets and then I'll kill that.

GRANDMA: Kill the parakeet?

LETTIE LU: That's what it says in the Bible. God, you can't follow anything! It's amazing I grew up to be as smart as I am. (to camera) Good-bye, all! God bless you! Tune in next week for more readings from the Book of Leviticus Show! (waves at the camera. So does Grandma)
```

---

## IC-1242: Boxing It

- Title: Boxing It
- Author (byline): Christine Emmert
- Work: One on One
- Publisher: Applause Theatre and Cinema Books
- Publication date as stated: 2007
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: SCENE, TIME, WOMAN
- Teaser before the introduction: Yes
- Spoken words (computed): 965
- Already set (do not supply): none

### Source block (context only)

```text
Author: Christine Emmert
Book: One on One
ISBN: 1557837007
Publisher: Applause Theatre and Cinema Books
Date (Month/Year): 2007
```

### Introduction (context only: never use it for content warnings)

```text
Street performances are an exciting part of city life, and choosing to become a street performer could be your ticket to fame. Many famous artists got their start as buskers, an industry term for street performers. You need just two things: an act and a street performer permit and maybe an imaginary box . .. Boxing It by Christine Emmert.
```

### Performance text (classify this)

```text
A very large young woman stands before a tiny clear box. SHE is a street entertainer. SHE surveys the invisible crowd passing her by for a long minute.

SCENE: The Circular Quay at Sydney Harbor

TIME: The present

WOMAN: That's all right. Go about your business, it's a beautiful morning for it. For missing what is just under your nose. Yes, sir, that's right. It's me. Just under your nose. Keep walking. Keep moving. Don't stop to see something you won't see again in a blue moon. (SHE stands still a long minute.) Come on, all you need is ten minutes of my time. You can spare ten minutes, eh? What's ahead of you? A bloody day where you are tyrannized by a bloody boss. That's all. And then, the Pub. Drinks all round. Home to the telly. I might be the most exciting thing you encounter all week, all month. (SHE gives up. Tries another side.) Do you want to see something truly astounding? Not something like in the movies... but real. Here. In the sunlight. Just me and a box. What do you imagine we could do together? (Smiles.) Oh, you are a curious one. In fact, you're a naughty one. I like you. It's people like you change the world. (Looks around and runs to other edge of stage.)

Yes, yes. I like a good crowd. Stay ten minutes. You won't be disappointed. I'm going to do something that will not even make you sorry you parted with money. Oh, don't hold on to your wallet. I'm just warming up the crowd. Gathering the crowd. (Looks around happily.) Yes, some more of you arrived. See me? See the box? That's the whole act. The whole routine. The box is there. I am here.

We need to get together, this box and 1. We need to become one. How very Zen! Yes, I will fit myself into that little box. Great big me. Condensed. You laugh! I can see the smiles. You doubt that I can do it. I know you've heard of one born every minute. (Listens.) No, mate, I meant me. I meant I'm the one born every... oh, forget it! Got a chip on your shoulder, that's what you've got. Got out of bed on the wrong side... or alone. (Laughs.) That's what we like. To hear the laughter. In the morning. On the Circular Quay. So... (Pauses a minute.) Before I start trying to get this massive flesh in that little container, got to do some warm-ups. You don't think I could do this unless I got my muscles going, do you?

Meanwhile I'll put a hat here for some preliminary palm-greasing. (Puts the hat down and waits.) Oh shy are we? How shy? I take all kinds of dollars. Yankee, Canadian, Aussie. I take Pounds, I take Euros. Rubles. Zlotys. Don't stop me now. I am a global taker! (Looks to hat.) Thanks. Ta. Let's get the pot started here. Just some encouragement for a poor starving sheila. (Listens.) What do you mean I don't look like I'm starving? Are you implying I'm well-nourished? Much nourished? I like to eat. That's why I've developed my talent. To earn my daily bread... Looks can be deceiving. I can be deceiving. I mean, the whole bloody point is that to look at me you'd never think I could fit in there. (Points to the box.) It took a lot of work. A lot of training to get this old body in that little space.

A physicist would say it couldn't be done. (Angrily.) Oh, and are you a physicist? Oh you are. Well, you can pay up when I show you. But first, my warm-ups. (SHE puts on music from a boombox and goes through a series of useless contortions.) Fine, fine. Have your laugh. I'd like to see you fit in there. (Points to box.) I used to have a boyfriend that couldn't fit into a thing, if you get my meaning. Well, no need to get huffy. I didn't mean you. You're a bit past it to be my boyfriend. Now it will just take a minute. (Looks in hat.) Oh, I see we're being generous this morning. Two of us anyway. (Sighs.) Well, can't wait all day. Let me first say... (SHE starts to put a toe into box.) Just testing the waters. (Stands in box.) Oh, it's almost comfy. Well, it will be. Let me tell you that it wasn't easy at first. How did I get the idea?

(Jumps out of box.) I have to admit I was a little thinner then. Easier. I started learning this trick in India where my boyfriend lived. No, that's the boyfriend who didn't fit. This boyfriend used to tell me if I learned to put myself into a box I would have the discipline to see God. That's right! God! And since I'd never seen God, I thought-well now, let's give it a go.

The thing about the box is that you can't look at it as your enemy. You have to think of it as-well, a dancing partner. It's Fred and I'm Ginger. The music has begun. .. (Changes music in boombox to something like a dance of old. ) You look at your partner. He takes your hand and... (The lights change.) It's rhythm, it's harmony... well, in actual fact, it's life at its finest. (SHE starts to shrink and twist. At no time does SHE ever touch the box.) Like all good efforts, it needs audience for appreciation. Don't go away or the illusion will evaporate. And wait with the questions! I'm in the process of transforming my molecules.. . into. . .

(Shrinks lower and lower until SHE is as compressed as SHE can be.) There! Moving those atoms around. Shrink-wrapped. Shrinking. (Mutters.) I need a shrink. (In a little voice.) My kingdom for a shrink! (Lights flashing.) All right. Take your pictures. Show it around. Drop some money for me. There now. It's done. (Lights come up.) Done, I say. (Looks in hat.)

Oh, loverly, luv. That should get me some shrimp on the barbie. What's this? A condom? Hey, mate. I don't need a . .. Never mind. It's a beautiful day at Sidney Harbor. I can take a little fun. A little protection. Tell your friends. They'll never believe it. (TO someone who comes up to her.) How did I do it? Mind over matter, of course. (Counts the money, sitting on the box after turning it over.) Christ, I got to get me a real job. This one needs some thinking. . . thinking outside the box. (Laughs.) Yeah. That's what it is. Outside the box. Inside the box.

Boxing it. (SHE takes her boom box, her box and her hat and goes off whistling.)
```

---

## IC-1243: Brimstone and Marmalade

- Title: Brimstone and Marmalade
- Author (byline): Aaron Corwin
- Work: Not specified
- Publisher: Rector Magazine
- Publication date as stated: Oct 30, 2013
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, MOTHER, MATHILDE, FATHER, PRINCIPAL, NANA, SHOP KEEPER, IX’THOR, BECKY, ROBBY
- Teaser before the introduction: Yes
- Spoken words (computed): 1028
- Already set (do not supply): none

### Source block (context only)

```text
Author: Aaron Corwin
On-line Transcript at: https://reactormag.com/brimstone-and-marmalade-aaron-corwin/
Publisher: Rector Magazine
Date (Month/Year): Oct 30, 2013
```

### Introduction (context only: never use it for content warnings)

```text
When I was little, I desperately wanted a pot-belly pig – But my parents in all of their wisdom gifted me with BURBLES – the goldfish. BURBLES didn’t last very long, and I remember hosting my own little funeral service as we flushed him to his watery resting place.

BURBLES was followed by a succession of other small creatures – 4 more fish, a hamster, and a bunny. At least I wasn’t condemned to own a pet rock!

In this fantasy selection, Mathilde doesn’t get the pony she wants; but a miniature demon named Ix’Thor. Take that, BURBLES.

Brimstone and Marmalade by Aaron Corwin
```

### Performance text (classify this)

```text
NOTE: The humor from this selection comes from the characterization and voice qualities of the characters. Go big and have fun!

NARRATOR: Mathilde didn’t want a demon. She wanted a pony.

MOTHER: Ponies are expensive. How about a nice little demon instead?

MATHILDE: (stamping her foot) I don’t want a demon! Demons are ugly and creepy and they smell bad!

FATHER: We’ll see.

MATHILDE: (to audience) When a grown-up said “we’ll see,” it really meant “never.” Peter Voorhees brought his demon to school. It was scaly and slobbery, not sleek and pretty like a pony. How could anyone think that a demon was better?

NARRATOR: The day before Mathilde’s birthday in September . . .

PRINCIPAL: Mathilde, your parents called. Your grandmother is picking you up.

MATHILDE: Nana’s here for my birthday? Nana always brought presents. (to Nana) Nana!

NANA: Look at you! My little Matty-Patty’s all grown up!

MATHILDE: (giggling) Where are we going?

NANA: You didn’t think I’d come all this way and not bring you a present, did you? The sort of present you’d better pick out for yourself!

NARRATOR: Mathilde could scarcely believe it. After all this waiting, she was finally going to get a pony of her very own. But when the car stopped, it was in front of a store covered in steel plates and the air smelled just a little bit like rotten eggs. It was very dark inside.

MATHILDE: This isn’t a pony store! This is a demon store! I don’t want a demon! I want a pony!

NANA: When I was a girl, we had a Belgian Muncher on the farm. Smart as a whip if you train ‘em right. You know the best thing about demons? They’re great for convincing parents that little girls are responsible enough to take care of a pony. If you prove you can take care of a demon. . . then we can see about that pony. (Nana and Mathilde enter the store)

SHOP KEEPER: Well, hello there! Are you here for a new demon?

NANA: Yes. It’s her birthday.

SHOP KEEPER: (to Mathilde) I see! What sort of demon were you looking for?

MATHILDE: The kind with the pretty eyes and the long, shiny mane!

NANA: (sighing heavily) That’s a pony, dear.

MATHILDE: Well, that’s what I want!

SHOP KEEPER: Oh, I think I have just the one for you. (he pulls out a small glass cage)

NARRATOR: The demon inside didn’t have a long, shiny mane. It didn’t have any hair at all, just a tiny, black hooded robe. Its eyes were two red stars that twinkled in the darkness of its hood like Christmas lights.

SHOP KEEPER: He’s a Miniature Dark Lord.

NANA: (shaking her head) A Dark Lord? I thought they had great big horns!

SHOP KEEPER: Normally. But this poor little guy was born without any. All the other Dark Lords rejected him.

MATHILDE: (feeling a connection with rejection) What’s your name?

IX’THOR: (raising his arms over his head) I AM IX’THOR, MASTER OF THE VENOMOUS PITS OF KARTHOOM! BOW BEFORE YOUR MASTER!

SHOP KEEPER: How about that! He told you his name first thing. He must really like you.

MATHILDE: (pouting) Well, I don’t like him . . . (IX’THOR is deflated, lowers his arms and hangs his head) But I guess he’ll do.

NARRATOR: Mathilde had a hard time sleeping that night. Her thoughts kept drifting toward the pony she would have someday. How long would she have to take care of a stupid demon, anyway?

MATHILDE: (sleeping . . . she snores lightly)

IX’THOR: (pokes MATHILDE on the chin, she swats him away, but he continues to poke)

MATHILDE: (awakens with a start)

IX’THOR: KNEEL BEFOR YOUR MASTER, MORTAL!

MATHILDE: Aaaaaah! Mom! (IX’THOR squeals and quickly hides)

MOTHER: How did he get out of his cage? (looks around the room for the demon)

MATHILDE: (also looking, she sees a dark shape dart under her bed and grabs a flashlight) He’s right here! (she reaches under the bed and grabs his little body) I’ve got him!

IX’THOR: (slashing has her hand with his claws)

MATHILDE: EEEEEEE! (abruptly drops him, crying) I hate demons! I want a pony!

MOTHER: Oh, sweetie. It’s just a tiny little cut. He was just scared, that’s all. You have to be careful with animals. When they’re scared they lash out. They don’t know any better.

MATHILDE: (belligerently) I don’t want him in my room!

NANA: (clearly disappointed) I’m sorry. I’ll take him back to the store tomorrow.

MATHILDE: (she remembers her pony and backpedals) Wait! I didn’t mean it. He can stay.

MOTHER: This is your last chance. If you say you don’t want him one more time, we’ll give him to someone who does. *****

NARRATOR: [The next day – Mathilde’s Birthday]

MATHILDE: (excited) There was cake! Chocolate with white frosting and candy sprinkles. And presents! A camera and a unicycle and (sadly) eleven different kinds of TOY ponies. (to the kids at the party) I did get another present . . . You want to see him? (she leads them to her bedroom) You have to turn the lights down. (as she dims the lights) He doesn’t like light.

BECKY: It’s not a snake is it?

MATHILDE: Shhh! It’s not a snake. (She lifts the cover from the cage)

IX’THOR: WELCOME TO MY DOMAIN. FOOLS! DID YOU THINK YOU COULD DEFEAT ME?

ROBBY: Wow! That’s cool!

MATHILDE: (with a real smile of pride) He’s a Dark Lord.

ROBBY: Does he do any tricks?

IX’THOR: BOW BEFORE ME!

MATHILDE: You shouldn’t actually bow. That just encourages him.

BECKY: It’s just a demon. What good is a demon who doesn’t even do anything? I bet he bites.

IX’THOR: FOOLISH MORTALS. NOW BEHOLD MY TRUE POWER! (he waves his arms and emits a bust of fire from his hands)

ROBBY: WOW! You said he didn’t do any tricks!

IX’THOR: GIVE ME YOUR SOUL AND I WILL GRANT YOU LIMITLESS POWER.

MATHILDE: Mom says I can’t have limitless power until I’m older. But you can have a grub soul.

NARRATOR: [Mathilde takes out] a small, softly glowing ball, about the size of a pea from the big plastic bag Nana had bought. The bag said things like “Nutritionally Balanced” and “Now with extra innocence for a health glow!”

IX’THOR: EXCELLENT (racing to the side of the cage, he stands with his arms outstretched) IX’THOR ACCEPTS YOUR SACRIFICE. (he devours the pellet) NUM NUM NUM! *****

NARRATOR: [Soon it was Halloween] A witch came to the house with a black pointy had, a broomstick, green skin and a big, warty nose.

MATHILDE: Nana!

NANA: (in a big witchy voice) Happy Halloween! Eee-hee-he-hee! How’s my little angel?

MATHILDE: I’m not an angel (raises the hood to her robe and speaks in an Ix’Thor voice) I’m a Dark Lord. Bow before me, mortals!

NANA: (feigning fright) Oh, my! I think I felt the earth tremble for a moment.

MATHILDE: (mimicking IX’THOR) Excellent. It is just as I have foretold. (She picks up a traveling crystal ball and holds it up) Ix’thor’s coming with us! He says fear keeps the peasants in line.

NANA: Mathilde . . . you know not everything Ixthor says is a good idea, right?

MATHILDE: (rolling her eyes) Well, duh!

IX’THOR: MWA HA HA! NOTHING CAN STOP US NOW!

MATHILDE: (mimicking IX’THOR) I’ll take my revenge when I rule the world. Mwa ha ha.

(Mathilde starts to walk toward the street, trips and falls forward. The crystal ball holding Ix’Thor launches from her hand and tumbles through the air into the street – there is the sound of squealing brakes and then shattering glass)

MATHILDE: No! (she races to Ix’thor) Ix’thor! Please!

IX’THOR: THIS . . . CANNOT . . . BE. I AM IN . . . VINCIBLE . . . ***** At the demon store *****

NARRATOR: [The family rushes Ix’thor to the demon store, hoping the shop owner can save him]

FATHER: Demons are pretty strong, right? Almost impossible to kill?

SHOP KEEPER: Dark Lords are weaker in direct sunlight. Much weaker. I did all I could.

MATHILDE: (crying)

MOTHER: Oh, sweetie. It wasn’t your fault. There was nothing anyone could have done. (more sobbing from Mathilde) Father and I were talking to Nana. If you still want one . .

MATHILDE: (defiantly) I don’t want a pony! I want Ix’thor. But I can’t have him back, can I?

MOTHER: No, I’m sorry.

MATHILDE: Then . . . can I get a pony with glowing red eyes and crush the skulls of my enemies beneath his flaming hooves?

MOTHER: (laughing) One with glowing eyes!

MATHILDE: (in her best Ix’thor voice) Excellent! It is just as I have foretold . . .
```

---

## IC-1244: Damned

- Title: Damned
- Author (byline): Chuck Palahniuk
- Work: Not specified
- Publisher: Anchor
- Publication date as stated: October 2012
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: MADISON, DEMON, EMILY
- Teaser before the introduction: Yes
- Spoken words (computed): 1584
- Already set (do not supply): none

### Source block (context only)

```text
Author: Chuck Palahniuk
ISBN: 978-0307476531
Publisher: Anchor
Date (Month/Year): October 2012
```

### Introduction (context only: never use it for content warnings)

```text
Madison has problems: she's overweight, ignored by her parents, and she's dead. But not just dead. Madison is in Hell, which really does exist! It’s a place where your only career choice is telemarketer, and the only currency is Halloween candy. This is the afterlife as only Chuck Palahniuk could imagine it: a twisted inferno where The English Patient plays on endless repeat, and roaming demons devour sinners limb by limb. He makes eternal torment, well, simply divine.

Damned by Chuck Palahniuk
```

### Performance text (classify this)

```text
MADISON: (Pg 3-4) Being dead-dead means nonstop, twenty-four/seven, three hundred sixty-five days a year . . . forever. Probably I shouldn’t even tell you I’m dead, because no doubt now you feel awfully superior. Nevertheless, here it is: my Hideous Admission. In a world where people say you’re lazy for not shaving your legs, being dead seems like the ultimate character flaw. [But] I’ll fess up and come clean. I’m out of the closet. I’m dead. (Pg 8) Disregard my account of Hell at your own peril.

MADISON: (Pg 8) First off, you wake up lying on the stone floor inside a fairly dismal cell composed of iron bars. The bars look a tad slimy with mold and someone else’s blood. Don’t touch anything. And do NOT eat the candy you’ll see scattered everywhere on the ground. (Pg 104) [See] Jewls and cash are worthless here. The currency is candy., and marshmallow peanuts are accepted as payment for all bribes and debts. The hellish equivalent of pennies are popcorn balls . . . black licorice . . . was lips . . . and these are cast aside in disdain. [But] Root Beer Barrels are as valuable as rubies.

(Pg 16) Are you there, Satan? It’s me, Madison. Please don’t feel hurt, but my parents raised me to believe you didn’t exist. [They] said you and God were invented in the brains of hillbilly preachers and Republican(s). (Pg 83) You can’t turn around in Hell without elbowing somebody important. Marilyn Monroe, Clarence Darrow, John F. Kennedy, John Lennon. (Pg 108) 98.3 percent of lawyers end up in Hell, and [while] a trace number of politicians ascend to Heaven, statistically speaking, 100 percent of them are cast into the fiery pit. As are essentially 100 percent of journalist and redheads. (Pg 83) If he knew the networking opportunities here, my dad would immediately gulp down rat poison. (Pg 90) As it turns out, my damnnation records have been lost . . . or accidentally destroyed. (Pg 94) It seems only fair that I ought to appeal my own eternal sentence. (Pg 185) [I] trudge across the Great Plains of Broken Glass, [wade] the River of Steaming-hot Vomit, [trek] across the vast Valley of Used Disposable Diapers toward the headquarters of Hell, [where] (Pg 90) I’m forced to start from scratch, assigned to take a basic lie-detector test. (Pg 86) Are you there, Satan? It’s me, Madison. I’ve never been very adept at taking tests. A demon with cat’s claws and folded leathery wings leans close to adjust a blood-pressure cuff which is wrapped around my upper arm. (Pg 90) You might recall this same demon from the classic Hollywood masterpiece the Exorcist.

DEMON: (Pg 92-94) Do you believe the Bible to be the one and only true word of God?

MADISON: Does that include the way-crazy, loony parts of Leviticus?

DEMON: In your honest opinion, does life begin at conception?

MADISON: (nervously wipes the sweat from her brow, grinds her teeth, clenches her fists, she cautiously answers) Yes?

DEMON: Do you view sexual acts between individuals of the same gender to be an abomination?

MADISON: Can we come back to that question later?

DEMON: I’ll take that as a “no”

MADISON: (to audience) Yes, I do want to go to Heaven – who doesn’t? – but not if it means I have to be a total ass.

DEMON: Do you approve of marriage between individuals of differing racial backgrounds? (without waiting for answer) Should the Zionist state of Israel be allowed to exist?

MADISON: (to audience) I’m stumped. Even fingers crossed. The paradox: Is God a racist, homophobic, anti-Semitic ass? Or is God testing to see if I am? [Then] in the same tone that a fast-food server would ask, “Do you want fries with that?” the demon asks . . .

DEMON: Are you, yourself, a virgin? (Madison freezes and refuses to answer, a guilty look on her face)

MADISON: [Who knows how long it will take to get my results] *******

MADISON: (Pg 104-105) The dirty little secret about Hell is that the demons are always running tabs on you. If you breathe their air, the powers that be are constantly dinging you for the cost. No, it’s not fair, but the demons charge you for your upkeep. Most people are condemned for only a few eons, but they accrue additional time simply by occupying space in Hell. [So] if you have any aspirations to earn your daily Junior Mints, you need to find a career and get working! (Pg 103) Are you there, Satan? It’s me, Madison. I’m proud to say that I’ve obtained full-time employment. A genuine job. As of now I’ a regular working stiff – if you’ll pardon the terrible pun. The work which most people do in Hell is – telemarketing. The dark forces are constantly calculating when it’s dinnertime and a computer autodials those phone numbers so I can interrupt everyone’s meal. I just ask if you have a few seconds to take part in a market research study identifying consumer trends in chewing gum. In mouthwash. In dryer fabric-softener sheets. I get to talk to real-live people – like yourself – who have no idea that I’m dead and phoning them from the Afterlife. Trust me, the vast majority of telemarketing people who ring you up, they’re dead. (Pg 109-110) [But] even as a telemarketer, it’s best not to enjoy yourself too much. If you don’t look miserable, the demons will reseat you next to someone who whistles. Then next to someone who farts.

(Pg 122) Are you there, Satan? It’s me, Madison. Over the phone today, I made a new friend. She’s not dead, not yet, but I can tell we’re going to be way-total best friends. (Pg 124) (On the telephone) If the Big C does kill [you] and [you] end up in the pit. Look me up. I’m Maddy Spencer, Phone bank number 3, 717, 021, position 12. Good luck with [your] chemo. Now remember, ask for Madison Spencer. I’ll show you the ropes!

(hangs up and the autodialer connects her with the next caller) (Pg 125-126) We’re conducting a consumer survey to track purchase patterns for common household items . . . (Pg 109) Would [you] consider purchasing toothpicks artificially treated to taste like chocolate? (Marks sheet) Like beef? (marks sheet) Like apples (marks sheet) (to audience) (Pg 126) I meet a girl about my same age, who’s dying from AIDS. Her name is Emily. [She won’t believe me at first] Either about being her same age or about being dead. It ought to break my heart, talking to a girl who’s dying of AIDS with both her parents at work while she watches television and feels weaker every day, but at least Emily’s still alive.

EMILY: Not only [am I] still alive, but [I] have no intention of ending up in Hell.

MADISON: [Have you] ever used the word “ain’t”? [Have you] ever fixed a hem with a safety pin or tape? Well, I’ve met mobs of people condemned to eternal hell fire for just those very slipups. Best not count [your] chickens before they’re hatched. 100 percent of people who die of AIDS are consigned to Hell. And all people killed by drunk drivers This is Hell – don’t ask for too much logic.

EMILY: (continually coughing) AIDS isn’t [my] fault. Besides that, [I’m] not going to die, not for a long, long time. (She coughs again, which turns into sobs, sniffing and weeping) You’re lying!

MADISON: (without any emotion) It’s not fair. You’ll see. (Emily hangs up on her, and Madison is offended. Phone immediately rings on Madison’s desk, she answers) (Pg 134-136) Hello?

EMILY: Is this Maddy? Are you Madison Spencer?

MADISON: Who’s calling?

EMILY: Emily.

MADISON: (covering the receiver to speak to the audience) She *69’d me!

EMILY: My parents want me to see a new shrink. Do you think I should go?

MADISON: (Shaking her head) No way. And don’t let them feed you full of Xanax, either! What’s is like to have AIDS?

EMILY: (Rolling her eyes) It’s like being Canadian. You get used to it.

MADISON: (Trying to sound impressed) Wow. I guess people can get used to pretty much anything.

EMILY: How did you die?

MADISON: I’m not all together certain. (uncomfortable talking about herself, she changes the subject) (Pg 127) Look me up once [you] arrive. We’ll make a bet. Ten Milky Way bars says [you’re] down here with me faster than [you] can imagine. Ask anybody for directions. The name’s Maddy Spencer, and [you] need to make sure and die with ten candy bars in [your] pocket. Ten! Not snack-size! ******

MADISON: (Pg 224) Are you there, Satan? It’s me, Madison. I [am] planning a little pilgrimage back to hobnob among the living. And to plunder the earth for its wealth of candy. Halloween is the only regular occasion on which the dead of Hell can revisit the living on earth. From dusk until midnight, the damned may walk – fully visible – among the living. The fun ends with the stroke of midnight; and like Cinderella, missing that curfew merits a special punishment. Any tardy souls are forced to wander the earth for a year, until dusk of the next Halloween – loitering among the self-obsessed living for twelve boring months. (Pg 184) Anytime your stomach is rumbling, or when you feel a sudden craving to eat something sweet, that’s someone in the afterlife who’s attempting to communicate with you. Cold sores on your lips . . . a bouncing, restless leg . . . ingrown hairs – all methods that dead people use to gain your attention. (Pg 226) [But] on Halloween, custom requires the dead to not merely revisit the earth, but to do so in the guise of their former lives.

EMILY: Forget that! I’m not trick-or-treating as a dumb Canadian girl with AIDS. I’m going to be a fairy princess.

MADISON: [Since] (Pg 90) my damnnation records have been lost, (Pg 226) I consider appearing as some stock character: a genie or angel or ghost. This is the first Halloween since my demise . . . (Madison pushes the doorbell on a house and waits impatiently for it to open) (Pg 237) Trick or treat! (Looking in her bag) (Pg 224) Candy corn! Tootsie Rolls! Bit-O-Honey! *******

MADISON: (Pg 246-247) To anyone who isn’t already dead, I wish you luck. Honestly, I do. You just keep swallowing your vitamins . . . Keep jogging around reservoirs and voiding secondhand cigarette smoke. Cross your fingers . . . maybe death won’t happen to you. Please don’t be afraid. If you go to Heaven, bully for you. But if you don’t – well, look me up. The only thing that makes earth feel like Hell, or Hell feel like Hell, is our expectation that it ought to feel like Heaven. Earth is earth. Dead is dead. [It’s almost midnight, so I have to go] (Madison stuffs a candybar in her mouth and talks with it full) (Pg 1) Are you there Satan, it’s me Madison.
```

---

## IC-1245: Darcy’s Cinematic Life

- Title: Darcy’s Cinematic Life
- Author (byline): Christa Crewdson
- Work: Random Acts of Comedy
- Publisher: Playscripts, Inc.
- Publication date as stated: Sept 2011
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: DARCY, MOM, BROTHER, LIZA, CHAD, TEACHER, BAILIFF, LAWYER, DAD, TOWNSPERSON 1, TOWNSPERSON 2, TOWNSPERSON 3, STUDENT 1, STUDENT 2
- Teaser before the introduction: Yes
- Spoken words (computed): 1622
- Already set (do not supply): none

### Source block (context only)

```text
Author: Christa Crewdson
Book: Random Acts of Comedy
ISBN: 978-0981909974
Publisher: Playscripts, Inc.
Date (Month/Year): Sept 2011
```

### Introduction (context only: never use it for content warnings)

```text
Darcy’s Cinematic Life by Christa Crewdson
```

### Performance text (classify this)

```text
DARCY: (Pg 97-98) I'm Darcy. Some people think I'm . . . .

MOM: Darling.

DARCY: I like to think of myself as a highly creative citizen of the universe. And in addition to my above average intelligence, I have what people call...

MOM: An overactive imagination.

DARCY: I prefer to think of it as my mind creating little movies in my head. You see, I get to thinking of something and my mind just takes over. Thoughts come to life, right before my eyes. It's...

MOM: An overactive imagination.

DARCY: That's my Mom. I also have a ...

BROTHER: Dork.

DARCY: Little bother. And a nemesis, an arch enemy ... Liza.

LIZA: Liza.

DARCY: Liza. Who pronounces it that way? Liza and I have had issues since kindergarten. She's one of the perfect people. In other words she's a ...

MOM: Nice girl. Why don't you invite her over?

DARCY: Like in any good story, there is also a true love. Chad. I have been in love with Chad since preschool. But he, well...

CHAD: Hi, Katie.

DARCY: (Pg 100-101) It's Darcy. He doesn't really feel the same way. (Beat) Every school day is the same. It's like that movie Groundhog Day. Liza is mean to me, Chad ignores me and I try to find ways to amuse myself in this institution of monotony. (Beat) Anyway, I have to confess that for the first time in my life I am grappling with a problem. A ... ugh ... teen problem. The impending class trip to the art museum. To a semi-outcast like myself, it is a major deal. (Bell rings) Homeroom.

LIZA: (Pg 101-102) Is this field trip tomorrow going to be lame or what?

DARCY: Actually, the Art Institute is one of the most famous museums in the world. It houses many famous works including Georges Seurat's A Sunday on La Grande Latte.

LIZA: Who? La what?

CHAD: Hey, were you guys talking about that painting with the dots? That painting is awesome. It's pretty tripped out. Art is cool.

DARCY: Ok, I am aware that Chad is not an intellectual, and I am perfectly content with that. I am smart enough for the two of us. The sound of his voice invokes a movie-one I have seen many times before . . . *********

(Flash to prom scene where Darcy and Chad are dancing)

CHAD: Darcy, these past four years have been the best of my life.

DARCY: Mine too!

CHAD: I want to give you this. (Hands her a ring.)

DARCY: Oh Chad, it's beautiful. . . . . to the future our wedding. (Hums wedding processional as they proceed down the aisle) Then twins! (pantomime babies in arms) And we spend our twilight years sipping lemonade on the porch. In our home, home, home. (Bell rings)

LIZA: (Breaking into Darcy’s daydreams, she speaks snarkily) Homeroom is over, Darcy! **********

DARCY: Science class. This is the one place I have a little clout because of my superior knowledge in this particular field. I am always flooded with offers of...

LIZA: Will you be my lab partner?

TEACHER: Projects are due today as you know.

LIZA: (To Darcy) You did the project, right?

DARCY: I know I'm being used, but it might secure me a seat on that bus. (Insert Law and Order Theme Song) **********

BAILIFF: (Pg 106-107) Case number 261, Darcy versus Liza.

LAWYER: Ladies and gentlemen of the jury, I shall prove beyond a shadow of a doubt that Liza has caused years of emotional suffering for my client, Darcy. Although Darcy is an extremely successful, well-adjusted young woman, she is here today to stand up for all highly intelligent, above average, citizens of the universe that are tormented by the perfect people! I call Liza to the stand.

LAWYER: How do you know Darcy?

LIZA: We go to school together.

LAWYER: Haven't you been lab partners? Didn't you take credit for work she did.

LIZA: I helped!

LAWYER: What were the projects you helped with?

LIZA: The one with the thingy.

LAWYER: Isn't it true that you were hanging out with your friends while Darcy did all the work? Isn't it true that you have done nothing but torment Darcy since kindergarten?

LIZA: (Defiantly) NO! LAWYER. Isn't it true that inside you are an empty, insecure person, and that's why you torment others-to make yourself feel better? Isn't it? Isn't it?!!!!!

LIZA: (Liza is crushed by the truth – She breaks) Yes, yes, it's all true!

LAWYER: I rest my case. (Bell rings) ********

DARCY: (Pg 103-106) T-minus 22 hours and counting until the field trip. As I stand upon the precipice of the school curb, I await my next horror: the dreaded clothes shopping with mom!

MOM: How was your day? Anything new?

DARCY: The mall. The most horrific place on earth. I would rather travel 100 miles to Indiana to shop rather than come here where everyone shops. With my luck I always run into ...

MOM: Isn't that your friend Liza?

DARCY: Mom, she's not my friend.

MOM: Darcy, she's walking this way, it's rude not to say hello. Hello, Liza.

DARCY: Well, we really have to go. Right mom?

MOM: Bye. Nice to see you. (To Darcy) I don't know what your problem is with her. She seems like such a nice person. Oh! Look at this!

DARCY: Mom's idea of fashion is .. .is ... well...even my superior vocabulary can't find the right word, so I'll use my little brother's favorite word “dorky.” If she had her way, I'd be all buttoned up and in plaid or some other monstrosity. Cut to the first scene in the next movie - The Mom Fashion Show . . . . (Walks the runway in very nerdy clothes with lots of attitude. A song plays throughout.) *****

DARCY: T-minus 18 hours to the field trip. Dinner -- "a time where families sit down together to eat and try to make their dull, boring lives sound interesting." I wish my family was one of those loud families in the movies where everyone is animated, and emotions fly around the room. Now that would be exciting! *******

(Family is a loud, Sopranos-like boisterous family.)

DAD: This pasta is perfect!

MOM: Of course, it is. It's Mama's recipe. God rest her soul.

DAD: So, guess who sold the Thompson house today? Pete Piker did. I was so close to selling that worthless piece of ...

MOM: Mario! Watch your language. The children!

BROTHER: I've heard it all before.

DAD: Where? I bet that little weasel friend of yours Benito says stuff like that.

DARCY: Benito is cute.

DAD: Cute? If I ever see you so much as look at that no good ...

DARCY: I'll look at who I want!

DAD: Oh no you won't! Not as long as you live under my roof!

DARCY: Well maybe I'll move out!

DAD: You're 13! Where are you going to go? (Alarm clock rings, waking Darcy) *******

DARCY: (Pg 107-108) T-minus 3 hours until the trip. Morning. Mornings around here are pretty typical. Lots of rushing, complaining, scarfing down food and running out the door.

MOM: (To Darcy) Honey, go back upstairs and put on that nice outfit we bought yesterday. For heaven's sake you're going to the Art Institute today! You need to dress appropriately!

DARCY: Mom, no one else is going to be dressed up. I'll look ridiculous! . . . . (a stern look from Mom) Fine! (as she is changing) I've always loved those movies where there's a scene that takes place in the morning and introduces you to the quaint little town. (She opens the door and steps outside) I wish that mornings were like that around here. *******

(Music plays . . . Perhaps Belle’s opening song from Beauty and the Beast or Good Morning, Baltimore from Hairspray)

TOWNSPERSON 1: (Pg 109) Morning, Darcy

TOWNSPERSON 2: Be sure to tell your mother I said hello!

TOWNSPERSON 3: You sure do look pretty today, Darcy!

DARCY: (Music stops) Then there’s reality.

LIZA: (Bumps into Darcy on purpose; sarcastically) Sorry, I didn't see you. Oh, did you buy that cute little outfit at the mall yesterday?

DARCY: Well, at least I made an effort to look like I am going to a museum, not a Britney Spears concert.

LIZA: Well, excuse us. I guess we don't know what to wear to go stand in front of a painting and look at a bunch of dots! ******

DARCY: (Pg 109-110) T-minus 13 minutes until the trip. I can't do it. I have to think of some way out! I could cut off my leg with a pencil. No, that would take too much time. I could fake a demonic possession. No, too Hollywood. I have to face the music, I'm going to have to get on that bus. (Bus doors hisses open) Oh yellow nemesis of mine. I have been awaiting your cruel fate. Ok, this is it. I have exactly 8.5 seconds to survey the seating choices. (DARCY stands in the aisle surveying the seats and the kids. She characterizes her options in pantomime) Choice one-Lenny the loner. Choice two-Renee the mooch. Choice three-Mr. Donovan, a chaperone. (She sits down gingerly on the very edge of the bus seat and looks miserable.) Finally the museum! (Bus door hisses open) I've been here many times so I know exactly where all the exhibits are. I'll try to share some of my knowledge of art with my fellow classmates. (to Classmate while gazing in awe at a painting) Monet attempted to capture conditions of light and atmosphere with bright colors and lively, broken brush strokes.

STUDENT 1: I wonder where the snack bar is? (Darcy moves to the next painting)

DARCY: Van Gogh's self-portraits reveal the profound insecurity and frustration of a gifted man!

STUDENT 2: I think this is the dude that cut off his ear.

DARCY: I give up. (Notices Chad by himself looking at a painting – She gathers her courage and walks over to him and gazes at the painting)

CHAD: I wonder who this is a picture of?

DARCY: No artist has dominated the 20th century in the way Pablo Picasso has. His subjects were society's outcasts, lonely figures. Maybe no one understands him. Maybe he feels like he was born during the wrong time or place. He's just waiting to find where he belongs.

CHAD: (In awe) You get all that from just looking at the painting?

DARCY: (Making a true connection with Chad) Kind of. That's just my interpretation though. Why do you think he looks so sad?

CHAD: (They lock eyes, and the rest of the world disappears) Maybe he wants to be alone, so he can be himself. Maybe he's sick of everyone always expecting him to be their friend, to be nice, to be funny, to be perfect. Maybe being everything to everyone makes him really lonely. (The moment is interrupted by… )

LIZA: (Enters and speaks in a flirty voice) Hi, Chad!

CHAD: Hey. Seeing some good stuff?

LIZA: I am now.

DARCY: Ugh. (Darcy gags)

LIZA: Did you say something?

DARCY: No, I have a hairball, that's all. Better move, I don't want to cough it up on you!

LIZA: Gross. Let's go. (She and Chad exit)

DARCY: (Pg 112) Cut to a scene from an adventure movie. I play the hero and Chad, the helpless lad who has been caught in the clutches of the evil dragon. I have to slay the mighty beast in order to save him. But she is the mighty beast. (pantomime fight scene with Liza in slow motion) I slay the dragon and free the lad who is eternally grateful. We ride off into the sunset to ... (Her daydream is interrupted by . . . )

TEACHER: Darcy, the bus is leaving!

DARCY: Right, the bus. Just as bad as a dragon. This is one beast I can't conquer. I know my fate. Doomed forever to sit alone or with . . . (Again surveys her options and characterizes her options in pantomime) Ugh.

CHAD: Hey! (He waves her over to sit next to him) (Darcy beams)

DARCY: (to audience) There will come a time when you believe everything is finished. That will be the beginning!
```

---

## IC-1246: The Dianalogues

- Title: The Dianalogues
- Author (byline): Laurel Haines
- Work: Women Playwrights: The Best Plays of 2003, Pg 59+
- Publisher: Smith & Kraus
- Publication date as stated: April 2004
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: DIANA IMPERSONATOR, CANDY
- Teaser before the introduction: Yes
- Spoken words (computed): 1513
- Already set (do not supply): none

### Source block (context only)

```text
Author: Laurel Hains
Book: Women Playwrights: The Best Plays of 2003, Pg 59+
ISBN: 978-1575253787
Publisher: Smith & Kraus
Date (Month/Year): April 2004
```

### Introduction (context only: never use it for content warnings)

```text
Not ALL fairy tales end "happily ever after." Especially not if you are an aging Princess Diana impersonator struggling to make ends meet in the Big Apple. But life is about to get a little stranger for our damsel in distress. As she leaves her late-night gig, she hails a cab driven by Candy, another New Yorker a bit obsessed by the 20th century fairytale life and death of Princess Di. Well, maybe obsessed isn’t exactly the right word . . . because Candy has a few problems of her own. It’s time to meet the ladies!

The Dianalogues by Laurel Haines
```

### Performance text (classify this)

```text
DIANA IMPERSONATOR: (Pg 59 +) Every once in a while, I need to take a drag on a cigarette and remember who I am. I swear to God, if one more person tries to kiss my hand, I think I'll scream. I shouldn't complain. It's a good living. It's just that I get in the middle of these parties with everybody wanting something from me, and wanting me to be something I'm not, and it used to be fun, but now it just tires me out. Jesus. I can't stop talking in this stupid accent. Bleah!

DIANA IMPERSONATOR: You know what just happened in there? I got propositioned. They think I'm a hooker. I guess they think if I'm willing to dress up like this I'll do anything. He was a short man. Kept trying to jump up and grab my tiara. So, I had to get out of there. He wanted me to go home with him and play Royal Court. Believe me, there was a time when I would have taken him up on it. In leaner years. But I've gotten rich off this gig. I couldn't stop, even if I wanted to. I can't do anything else. Oh, I can act, but nobody wants me to do that anymore.

I mean, really. . . Sometimes I look in the mirror and I'm not sure what I see. I've played this woman every weekend for the past eighteen years. I think I might play her for the rest of my life. I walk like her, I talk like her, I dress like her. I have more of her clothes than my own. Of course, someday I'll get too old to play her. That's the problem with impersonating someone who's dead. You change while they stay the same.

I don't know what I'll do when this is over. I figure I have another five, ten years in me. Dead icons are the best business. Marilyn, Elvis, you wouldn't believe it, but Nixon is a big one. I heard about a woman in Bel Air who will hire six or seven Nixons at a time, just for herself. Don't ask. I guess I could go back to temping. (shudders.) Or telemarketing. I'll still have her voice. Maybe there's a 900 number that would hire me. (breathy and British.) Oh, yes, baby, you really move me, you make me feel so wild, so unrepressed, so Scandinavian. (back to normal voice) And then I'll take out my dentures.

You know what they should do? They should make an old folks home just for us. So people can come and laugh at us as we get old. Sure, I'm sure there's some freaks out there who would want to see what Diana would have looked like at seventy. Or James Dean at ninety. Not to mention anyone who still thinks Elvis is alive. There's probably weirdos who would take care of us for free. They can come and feed us creamed corn and push us around in our golden wheelchairs. (She is half-laughing, half-crying.) Oh God, that's sick.

TRANSITION

In this scene, a cab driver, CANDY, believes that her passenger is none other than Princess Diana, and offers some marital advice.

CANDY: Where to? Around? Lady, I don't just drive around, I ain't a sightseeing tour, you know what I'm saying? This is a cab. I go from here to there, I don't just... (turns back to audience holding a wad of bills.) OK, you got it. I'll drive you around. (drives)

You from out of town or something? (pause) OK, not the talkative type. You know, you really don't need to wear those sunglasses, my windows are tinted. Only people I know who wear sunglasses indoors are movie stars and my Uncle Rick. He got an eye shot out. Hey, wait a minute, you are a movie star! I know I've seen you before. Wait, wait, don't tell me. Melanie Griffith! No? OK, give me another chance. You're not a porn star, are you? Holy shit! I know who you are! You're Princess Diana! Holy shit! I've got Princess Diana in my cab! (turns fully around in her excitement) What the hell are you doing here? Huh? (faces forward and jerks the wheel) Hey! Watch where you're going! Oh my God. OK, OK, I'm cool. Princess Diana! (listens) Yeah, sure you're not. I know Princess Diana when I see her, and you're her. OK, fine, you want to pretend like you're not who you are, that's cool. I can do that. I won't say another word. (silence)

So, like, what, you just wanna get out of the castle for a while, see a few sights? Figured you'd come to New York for some action? (pointing) Bet you don't see freaks like that at Buckingham Palace, do ya? OK, OK, I'll stop. I know what it's like for you royalty, always getting bugged by people. You probably just want some time alone. Hey, that's what's going on! You wanna get away from that husband of yours. Yeah, it's been all over the news. He's having an affair with that lady, whatsername, Camilla! Calling her on the phone and shit. Oh man, let me just say he must have his head up his ass. I mean, she is one ugly bitch! And you, you're beautiful, and glamorous. You're like, a princess! Hey, you're not thinking about getting back at him, are you? I mean, that's not why you're cruising around, is it? Because there are some real weirdos in New York; you should be careful who you pick up. Some guys look real nice, but they're psycho. The Wall Street types especially. It's always the clean-cut looking guys who turn out to have bodies in their refrigerators. I won't pick' em up. And in this part of town, forget about it. Drug dealers and whores, that's all you got on this street. Hey, wait a minute, that's my cousin Denise! Denise!

(turning her head, she nearly runs into a truck and slams on the brakes) Whoa! That was a close one. What were we talking about? Oh yeah, I mean, what guy gives up a princess for some butt-ugly broad? But you know something, it don't surprise me. I mean, men will (gestures.) you know, anything that moves. You got to keep your eye on them. I got a lot of experience with that. My guy, James, when we first met he was like, oh Candy, I love you, you're so beautiful, you're my queen, right? And every day, he's going on about how gorgeous I am, and how I should be a model, and I'm like, yeah, you're beautiful too, James. And he's like, no baby, I got my face burned in a fire, I ain't beautiful, and I'm like, yeah, but James, you're beautiful inside. And he's like, no Candy, no, you, you're beautiful, you are, you, you are beautiful. And I'm like, OK, I'm beautiful. So we move in together, and we're in love, and we decide we're gonna get married as soon as I can get a divorce from my last husband. Well you can guess the rest of the story. One day, I come home from work, walk in the door, and he's on the floor with the deaf-mute girl from the dry cleaners. And she is a dog. I mean, worse than Parker-Bowles. This woman's face looks like scrambled eggs. And I'm so confused. Because I thought I was supposed to be so beautiful, and here he's been banging a circus freak. And he's like, (as James) oh baby, I'm sorry, I don't know what happened, please forgive me, and I'm like, oh no, no you don't. (as James) But baby, baby, I can explain. (as herself) Oh no, baby. I can explain. And I got my knife and - huh? Oh no, I didn't kill him. I just cut him up a little. Not a lot, just to scare him. That's what you gotta do with men, scare them. He don't fool around no more. (beat) That's what you gotta do with your husband. Just cut him a little. I bet he won't be expecting it from you. That's what'll make it twice as good. Dontcha think? Yeah, like one time when the two of you are eating your tea and crumpets and shit, and he gets up to make another phone call, you just go chk chk chk (makes a stabbing gesture) He won't be making no more phone calls after that, believe me!

(horn honk.) Oh, go screw yourself! (to the passenger) Huh? You wanna get out here? Oh no, you don't. This is not a good area of town. Believe me, you don't want to be walking around here at night, especially a gal like you. They'll eat you alive. No. I'm sorry. I can't let you out. I cannot be responsible for your certain rape and death. Or worse, one of these pimps might decide he likes you. "Princess Diana found turning tricks on Avenue C." No way. That's not gonna be on my shoulders. Well, yeah, by law I have to let you out wherever you want, but that don't mean I'm gonna. Yeah, you paid me. It's your ride. OK. OK, I'll let you out on one condition. You gotta take this. (holds out a knife) For protection. And whatever else you wanna use it for. Come on, take it. Yeah, there you go. (passenger exits the cab -- to herself) Jesus. (rolls down her window.) Hey, good luck, you know? I'm rooting for ya!
```

---

## IC-1247: Disney Heroine Round Table

- Title: Disney Heroine Round Table
- Author (byline): Peter David
- Work: But I Digress #1 (Comics Buyer's Guide); Issue 998, Pg 187+
- Publisher: Krause Publications
- Publication date as stated: Jan 1994
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: SNOW, JASMINE, BELLE, ARIEL, ARIEL AND JASMINE, EILONWY, RAJAH, SEBASTIAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1714
- Already set (do not supply): none

### Source block (context only)

```text
Author: Peter David
Book: But I Digress #1 (Comics Buyer's Guide); Issue 998, Pg 187+
ISBN: 978-0873412865
Publisher: Krause Publications
Date (Month/Year): Jan 1994
Also available on the author’s website at
https://www.peterdavid.net/2010/04/19/disney-heroines-roundtable/
```

### Introduction (context only: never use it for content warnings)

```text
Welcome to The Disney Heroine Round Table by Peter David
```

### Performance text (classify this)

```text
(Transcript of the Disney Heroine Round Table, 1992 Edition, held in King Stefan's Banquet Hall at Disney World on Dec. 1, 1992, Snow White moderating.)

SNOW: (Pg 187+) Well, this is all tremendously exciting. Every decade or so, the nice folks at Disney sponsor a get-together with all the lead actresses of recent animated features. This gives us a chance to chat, exchange tips on how to clean house

JASMINE: Allah, give me strength.

SNOW: . . . and, over all, just get to know each other as girls.

BELLE: Women.

SNOW: Since I was the first full-length Disney heroine, they generally ask me to moderate. And I'd like to welcome this year's guests - Princess Jasmine from Aladdin . . .

JASMINE: Is this going to take long?

SNOW: Belle from Beauty and the Beast - and congratulations again on that Best Picture nomination.

BELLE: Thank you. We were robbed. Losing to a cannibal - now, what does that say about society and its priorities? In the words of Sartre . . .

SNOW: And, of course, Ariel from The Little Mermaid.

ARIEL: It's exciting to meet you, Snow.

SNOW: Thank you. Uhm, you're dripping on my clean floor.

ARIEL: Oh. Sorry.

SNOW: We were also going to be joined by Olivia Flaversham, the plucky little heroine from The Great Mouse Detective. But we had a bit of a mishap, because someone on the panel couldn't control her rather large kitty cat.

JASMINE: Look, I already said I was sorry. I'm no happier about it than anybody else. If the damned invitation had said there were going to be mice running around, I wouldn't have brought Rajah along in the first place. OK? Let's move on.

SNOW: I must say, before we start, that I admit my breath is a bit taken away by the changes in clothing styles for Disney heroines. With your little harem outfit, Jasmine, and you, Ariel, with your - shells - and both of you with all that skin hanging out: It seems a trifle - what's the word?

BELLE: Sluttish?

ARIEL: Oh, well, thanks a lot! Big talk from someone whose idea of a good time is sitting around in an apron talking to sheep.

BELLE: You talk to fish.

ARIEL: But they talk back.

SNOW: Actually, I was going to say "daring" rather than "sluttish." But this really brings us to our first point of discussion: Namely, what do you think our role in movies today should be?

JASMINE: I'll tell you what it shouldn't be. It shouldn't be sitting around waiting for someone to "take you away from it all." I mean, come on. Could you see me singing, "Some day my prince will come"? Ack ack ack.

SNOW: You don't have to stick your finger down your throat and gag, Jasmine. It happens to be a lovely song.

ARIEL: Jasmine's right. Life isn't something that happens to you. Life is what you make happen. You have to take control. That's what I did.

JASMINE: Me, too.

BELLE: So did I.

JASMINE: Oh, sure. Right.

BELLE: I did! Really!

ARIEL: Sure you did. First you walked around town, looking down your nose and talking about how provincial all these hard-working villagers are and how there has to be more to life than that. If Cruella De Vil had sung the exact same thing, people would have said it was the most arrogant song ever written.

BELLE: But . . .

JASMINE: And, while you said you want more out of life, you didn't do anything to get it.

BELLE: Yes, I did! I gave up my liberty, sacrificing for my father! I promised I'd stay a prisoner in the Beast's castle, forever!

ARIEL: Uh huh. And how long was it before you went running out the front door saying, "Promise or no promise, I can't stay here another minute?" A week? A month? A year?

BELLE: Uhm . . . well, actually . . . about three, four hours, maybe. But there are such things as promises made under duress, and they're not always binding. Perhaps it's Machiavellian, but even so -

JASMINE: Well there's a woman of her word. Some heroine.

SNOW: Ladies, I think we're getting off the topic.

JASMINE: Me, I defied my father. I had the guts to go against what he said and run off.

ARIEL: Your father. Heh.

JASMINE: What's that supposed to mean?

ARIEL: The two of you with your fathers. You defied yours, she sacrificed for hers. And you've both got these roly-poly, cute, comedy-relief fathers. Me, I've got the King of the Sea for mine. He throws around energy bolts and can bench press a whale. I'm the only one with real guts here.

BELLE: More guts than brains, that's for sure. Cutting deals with the Sea Witch. There was a smooth move. Obviously, if you'd ever read anything by Marlowe, you'd've realized the folly of that.

SNOW: Belle, who are all these people you're talking about?

BELLE: Authors. Playwrights. Philosophers. Crack open a book, why don't you? You, too, Miss Turkish Trunks. And you too, Fishy.

ARIEL: I read books. Human books.

BELLE: Oh, right. You can't remember tough words like "feet" and you don't know why fire burns. How'd they miss having you on Jeopardy, I wonder. Oh, and here's a news flash for you: It's a fork, OK? A fork. You eat food with a fork. You don't comb your hair with it. If you combed your hair with it, it would be called a comb, not a fork. All right, Einstein?

JASMINE: Some of us have royal duties to attend to and don't have a lot of time for books.

BELLE: That is so typical. You three are just typical elitist examples of the societal class structure. All of you, born to royalty. Bored children of privilege.

SNOW: But you're royalty, too! At the end of the movie, you married . . . uh . . . what was his real name?

BELLE: I . . . don't know. Besides, I was talking about being born to entitlement. You lived your lives in castles, children of kings and queens - or at least kings, since there never seem to be any queens in Disney films. So you endured a couple of days of hardship, dabbling in the sort of life that I lived every single day, before you settled down with your prince. It's disgusting. Particularly you, Ariel, who totally subverted everything she was in order to be part of her man's world.

ARIEL: Oh, yeah? You looked pretty comfortable strutting around in that big yellow gown at the end. I didn't see you fighting to remain a peasant.

BELLE: That's all the underprivileged masses are to you, aren't they? Peasants? The Proletariat. In the words of Karl Marx -

ARIEL: Oh, Lord, here she goes again.

SNOW: Actually, this presents us with a topic that might not cause such bickering: Namely, what do you look for in a prince?

ARIEL: Well, for me, it was love at first sight. I watched him dancing, and talking, and . . . I just knew.

JASMINE: "I just knew. I just knew." A guy flashes a smile and a royal title at you, and you get mushy. Love at first sight is a convenient excuse not to think.

SNOW: Some of us, Jasmine, are fortunate enough to meet our prince and be drawn to him immediately. Others of us turn princes into kitty treats for our tigers.

JASMINE: Some of us, Snow, prefer thinking. Ariel, your prince was heroic enough, but about as thick as a brick.

ARIEL: Why, you . . .

JASMINE: And you, Snow, You never so much as spoke to the guy. How could you possibly have known he was the man for you? What about him could possibly have drawn you to him?

SNOW: If you want to know why I love him so, it's in his kiss.

JASMINE: That's where it is?

BELLE: You're really pathetic, Snow, you know that? Not that I can stand Ariel or Jasmine, but Eric defeated Ursula, and Ariel went off with him. Aladdin defeated Jafar, and Jasmine married Aladdin. But the dwarves . . .

SNOW: Dwarfs.

BELLE: Whatever. . . . risked their lives for you - they adored you - and then some jerk prince comes along, gives you three seconds of liplock, and you abandon the dwarves . . .

SNOW: Dwarfs.

BELLE: Whatever! . . . and go riding off with him. What an ingrate.

SNOW: *Sniff*

ARIEL: Oh, great. Now you made her cry.

JASMINE: She's a big girl. She can take it.

ARIEL: That's about the kind of empathy I'd expect from someone who walks around in her pajamas all day.

JASMINE: Fish Face.

ARIEL: Baklava Breath.

BELLE: Ah, the upper class, displaying their typical -

ARIEL AND JASMINE: Shut up! (a young blonde girl enters)

EILONWY: Excuse me? Am I too late for the meeting?

SNOW: Who (sniffle) who are you?

EILONWY: I'm Eilonwy. I'm a princess.

BELLE: Oh, terrific. Another example of the -

JASMINE: I'm warning you,

BELLE: Rajah's still hungry.

SNOW: I'm sorry, dear. You're who?

EILONWY: Princess Eilonwy.

SNOW: Well . . . I don't know who sent you here, but this is for Disney heroines.

EILONWY: But I am a Disney heroine. I was in The Black Cauldron. (blank stares from everyone)

ARIEL: The what?

EILONWY: Based on "The Chronicles of Prydain" books . . .

SNOW: Books? Belle, I hate to ask . . .

BELLE: Oh, right, now they come groveling.

JASMINE: Rajah! Time for din -

BELLE: OK, OK. It was a fantasy series by Lloyd Alexander.

EILONWY: Right! And I was in the movie!

JASMINE: What movie?

EILONWY: Oh, come on, didn't anyone see it? 1985? 80 minutes long? Supposed to usher in a new era of Disney animation?

ARIEL: Actually, my film did that.

JASMINE: Oh, aren't we full of ourselves.

EILONWY: Sword-and-sorcery epic? There was me and Taran the assistant pig-keeper, and Fflewddur Fflam . . .

JASMINE: You must be joking.

SNOW: No, wait! I remember now. I got a ticket for an advance screening. But I was busy that night, so I sent Happy instead.

EILONWY: What did he think?

SNOW: He hated it. I've never seen Happy complain that much - or at all. But he just kept talking about how awful it was. Grumpy finally had to slap him.

EILONWY: That's not fair! We were groundbreaking!

BELLE: Poor spoiled princess, just like all the others. Boo-hoo.

JASMINE: That's it. Rajah!

RAJAH: Rawwrrrrr!!

BELLE: Eeeeeekk!! (Sebastian walks in)

SEBASTIAN:Ariel, da king wants to know how long - eeepp!

RAJAH: Raarrrr!

BELLE: Let me out! Let me out!

SEBASTIAN: Ohhh, mon!

ARIEL: Put him down! I mean it!

JASMINE: Pajamas, huh?

SNOW: You know, these discussion groups used to be fun. Me and Cindy, we'd sit and chat for hours. Sure, Aurora would keep dozing off . . .

BELLE: Shut up! Knock off that high-pitched little-girl voice! It's making me nuts! And get me the hell out of here!

SNOW: Well, I hope you'll all join us for our next discussion group -

SEBASTIAN: Arrrieellll!

RAJAH: *Chomp* *Chomp*

ARIEL: Jasmine! Make him spit him out! Right now!

SNOW: It's going to be called, "Life's a Bitch, and So Am I." Participants will be Lady from Lady and the Tramp, Perdita from 101 Dalmatians, and Georgette from Oliver and Company. I'm sure the fur will really fly. Thanks for coming. Hi ho, hi ho.

RAJAH: *Urrrp*
```

---

## IC-1248: Disneyland

- Title: Disneyland
- Author (byline): Laurie Notaro
- Work: I Love Everybody (and Other Atrocious Lies) Pg 133-150
- Publisher: Villard Books
- Publication date as stated: June 2004
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: LAURIE, ANGELINA-CHARLIZE, NICOLAS, OTHER CHILD, MAD HATTER, MAD HATTAR, CONDUCTOR, NICHOLAS
- Teaser before the introduction: No
- Spoken words (computed): 2151
- Already set (do not supply): none

### Source block (context only)

```text
Author: Laurie Notaro
Book: I Love Everybody (and Other
Atrocious Lies) Pg 133-150
ISBN: 978-0812969009
Publisher: Villard Books
Date (Month/Year): June 2004
```

### Introduction (context only: never use it for content warnings)

```text
According to literally everybody on planet Earth, it’s impossible for a person to make it to 30+ years of age without ever having been to the most magical place on Earth.

In fact, whenever you tell a person you’ve never been to Disneyland, they go through at least seven different stages of stunning disbelief before telling you that you have to — no, listen: YOU. HAVE. TO. — get in a car and drive to Disneyland immediately.

Hours later, you find yourself in a car bound for the magical land of Disney, and there’s no going back. You’re going to Disneyland for the first time, as a grown adult, and there’s nothing you can do about it.

Disneyland by Laurie Notaro
```

### Performance text (classify this)

```text
LAURIE: (Pg 133-151) Everywhere we went in Disneyland at least two out of five kids were sobbing, screaming, or hyperventilating, having either been recently smacked, recently yelled at, or recently threatened with being "sent back to the room."

I, however, was having a grand time. Somehow, either I had arrived on the perfect day or I had traveled through some sort of self-esteem time warp, but I was one of the prettiest people at Disneyland. Now, honestly, that's not saying much about me, but I will admit that every time I saw two honey-baked hams swinging out the armholes of a tank top, my self-esteem skyrocketed. A size sixteen anywhere else in the free world translated to a size four here, and I never felt so liberated.

I loved Disneyland. I LOVED IT. I had no idea I was going to have such a good time when my sister had asked me to accompany her and my nephew Nicholas to celebrate his fourth birthday. I mean, it's Disneyland, and it has very little appeal for a childless woman in her thirties, unless her intelligence level is significantly below average. I agreed to go on this trip for two reasons:

1. I try really hard to be the cool aunt . . . going on this trip would give me the opportunity to have fun with my nephew, bond even closer with him, and build his trust in me so that I might wield him like a puppet and mold him into the child I absolutely knew we both wanted him to be.

2. I was also at Disneyland paying penance for "embarrassing and traumatizing him in front of twenty of his little friends," as a helper in Nicholas's preschool classroom for the Harvest Festival or, what they used to call in less stringently politically correct days of yore, Halloween.

Now, I will admit that perhaps I had some responsibility in the matter, but what unfolded that afternoon was in no way entirely my fault . . .

After the teacher introduced me as Nicholas's Aunt Laurie, she assigned me to the spider - web table, where I was supposed to help little kids make a spider web on a piece of paper with glue and string. And that was all going fine until the first little girl I was supposed to help, Angelina-Charlize, didn't want to make a spider web, she just wanted to write her name. I was cool with that. That was fine. No skin off my nose. Go ahead and write your name, you know? So Angelina-Charlize wrote her name, complete with a backward r. ln an attempt at helping, I told her that we should try turning the r around a bit, and that's when she openly mocked me.

ANGELINA-CHARLIZE: (chanting) Aunt Gloria doesn't know how to make an “r” . . . That's so sad for a grown-up.

LAURIE: No, really, the r needs to face the other way -- Would you like me to show you?

ANGELINA-CHARLIZE: There's an r in my name, so I should know. Aunt Gloria can't make an r, Aunt Gloria can't make an r!

LAURIE: Actually, it's Aunt Laurie, and I've been writing for a long time, so maybe I should know.

ANGELINA-CHARLIZE: If you know, then why can't you make one? Because you can't! You can't you can't you caaaan't!"

LAURIE: "You know," I wanted so desperately to tell them, "you girls keep writing in your little chimpy hieroglyphics that only a mirror can read and I'll be more than happy to write you a recommendation to Klown Kollege when the time comes, because you will indeed need it."

Instead, I just smiled and said: March to your own dyslexic drum, Angelina Calista Jennifer Aniston Lopez Drew Barrymore. I just really hope you like the circus.

That was pretty much the moment that Nicholas's teacher came over, leaned into my ear and whispered, "Maybe we should try the play area, where it's not so structured."

I had been fired from the spider web table. I had just totally gotten fired from the spider web table, and unjustly so!

Whatever, I said to myself, I'll show them what I can do in the play area, I'll show them. Much to my relief, I saw my nephew in the play area, running what appeared to be an invisible grocery store, using his creative imagination, just like his Aunt Laurie had taught him.

NICOLAS: And there you go. [Nicholas said to another little boy as he handed him a big fistful of air.]

LAURIE: Hello, sir. I would like an apple. Do you sell apples, Nicholas?"

NICOLAS: Yes, I do," [handing me absolutely nothing] And my name is Mr. Booley when I'm at my store . . . It's forty dollars, please.

LAURIE: Well, that's a little steep, don't you think? Safeway has apples for ninety-nine cents a pound, and I can actually see those!"

NICOLAS: Well, then, maybe you should go to Safeway.

LAURIE: Okay, okay, I get it [putting out my hand with nothing in it.] Here's your forty dollars.

NICOLAS: [Scoffing] My store only takes credit cards.

LAURIE: Did he give you a credit card? [pointing to the customer before me]

NICOLAS: He's a little boy, Aunt Gloria. He doesn't have credit cards. Are any of your credit cards still good?"

LAURIE: I think maybe you've been talking to Grandma about my credit status, but let me assure you that it is almost cleared up now. Maybe I will go to Safeway! And you know my name is Aunt Laurie!"

NICOLAS: [yelling and pointing] Aunt Gloria shoplifted! She shoplifted my apple!

LAURIE: I did not! And his prices are highway robbery! Would you pay forty bucks for an apple? Plus twenty-one percent interest? . . . Wait . . .There is no apple! [showing everyone empty, appleless hands] You can't steal something that doesn't exist! There is no apple!"

OTHER CHILD: I saw her take a banana, too!

LAURIE: So that was why I was at Disneyland. I thought it would make up for the alleged, imaginary fruit thievery incident.

Now, I was at the "Character Breakfast" in Goofy's Kitchen ($35 to have the Mad Hatter hop around your table like a flea as you're trying to eat your Mickey Mouse waffles).

MAD HATTER: Hey, how are those waffles? They should make Mad Hatter waffles! Mad Hatter waffles! Waffles with a big hat! Those are the kind of waffles I'd eat!"

LAURIE: You know, we could have grabbed a bagel outside for two bucks, but then the delight of having a neurotic midget dressed as Oscar Wilde buzz around us like a palmetto roach would have been lost forever.

NICOLAS: [squealing] Goofy! Goofy!! Over here, Goofy, over here! It's my birthday!

LAURIE: I turned around, and there he was; that giant dog thing or walrus or whatever he is suddenly appeared, pulling the little children toward him like safety pins to a magnet.

MAD HATTER: It's my un-birthday! Come to my tea party!"

NICOLAS: "I love Goofy!" [hugging Goofy]

MAD HATTAR: Goofy thinks he's all that, but he's not. You'll hug Goofy but you won't hug me. But let me tell you something, Goofy is not as hot as he thinks he is. Are you, Goofy? Are you?"

LAURIE: And then, as I turned to look at Goofy and Nicholas, Goofy's middle finger-and I mean there was no mistaking it, since he only has three of them-was vividly scratching his nose. Goofy flipping off the Mad Hatter? That is the coolest thing I've ever seen. I'd totally give them both fifty bucks to fight. *******

NICOLAS: I love Gadget's Go Coaster! You'll ride, too, won't you, Aunt Laurie?

LAURIE: Of course. It's your birthday, how could I not? (to audience) The whole ride, which was a basic, no-frills kiddie roller coaster sporting props of oversize combs, and a couple rather large stationary frogs, lasted no more than a minute, so when the train pulled to the boarding platform at the end, Nicholas said he wanted to go again.

Before I could even say anything, the train took off and I was trying to concentrate on his fun when we turned a bend in the ride, and then suddenly out of nowhere, something hard and fast struck me in the side of the head. I grabbed my skull, which was now wet with a liquid I was really hoping was not a body fluid, like blood, and that's when I saw it -- a seemingly placid, peaceful, unaggressive frog statue until it decided to spit at you with a fire hose of water that was conveniently hidden from view. I was still trying to wipe the water from my face when we pulled into the boarding station next to an empty platform.

CONDUCTOR: Wanna go again?

LAURIE: And the conductor took off for our next round without even stopping. (to conductor) Hey! I'm done with this ride! Aunt Laurie is done!

PPPLLLLTTT!! went the frog as I passed him again, hard and fast like the first time and just as wet. And there I was, there I was, a wet, childless woman in her thirties, trying to wipe water out of her eyes, one side of her head dripping with frog spit, as she went around and around and around the Go Coaster. Finally, THANK GOD, someone was on the platform when we came around the last time.

[to Nicholas] The frog on your ride hocked on me, you know, and wrecked my pretty supermodel hair. And I think it also left a hematoma where the spray hit me in the head. It's all soft and squishy in that spot now."

NICOLAS: Gadget's Go Coaster made me ready for Splash Mountain! Can we go?

LAURIE: Oh, come on, dude! [stomping my foot] I already look like a sponge! Splash Mountain? Let's go back to the hotel and eat room service stuff, okay? Eighteen-dollar grilled cheese sandwiches!

NICOLAS: [shaking his head] Splash Mountain!

LAURIE: Okay, fine. I am here to pay for my sins. Before I knew it, I was hustled into a log, sitting in the second seat behind one of the almost teenage sons of the guy ahead of us in line. He looked at the wet side of my head and gave me a pained smile.

(to pre-teen) I know you were hoping to be straddled by a skinny blonde cheerleader with perfect skin and a Crest Nighttime Whitening Strips smile. But an hour ago, I was the hottest chick in this park.

He grimaced visibly and moved forward on the log before we lurched and then took off. I heard my nephew squeal with anticipation directly behind me. We reached the top, paused for a moment, and then dropped furiously downward, and that's when I gasped.

Because that's when it hit me: When you're about to dive into a pool of water from four stories up going roughly 30 to 40 miles per hour and you're wearing a white T-shirt with a white nylon bra underneath it, there's a very good reason to try to get the hell out of that car. A very good reason.

NICOLAS: Why are your arms crossed? Are you mad?

LAURIE: I'm not sure if 'mad' is the word, Nicholas. I'm just trying to keep our little trip here at a G rating. If I uncross my arms, either I'd get taken away by or I'd pop up in the latest version of Totally Ugly Girls Gone Wild. I started out so great this morning, and now I look like a used Bounty paper towel.

NICHOLAS: Let's go to Tom Sawyer Island!"

LAURIE: Fine with Aunt Laurie. She needs to find some sun before she gets nominated for adult entertainer of the year.

Over on the island, I tried my best to keep up, but I lost [him] in the labyrinth of Injun Joe's Cave, being that I couldn't move very freely without exposing myself to a random child. In favor of keeping my balance and remaining upright, I decided to try and backtrack my way out and then find a nice sunny spot where I could dry out and enjoy the benefits of opaque clothing again. Finally, I saw the opening of the cave and headed toward it, and as I entered daylight, I suddenly saw the tumble of sky, the sun, glimpses of blurry faces, and finally, a big patch of brown all tossed in front of me like a salad.

When I looked up, I heard a chorus of tiny giggles and saw a bunch of rotten kids above me on the mountain, peering over and cackling like Children of the Corn. I had totally eaten it on Tom Sawyer Island, which wasn't surprising since my arms were entirely useless. As I got up from my full-body dirt sprawl, grasping at the base of the mountain, I tried to act cool, like it was no big deal, while the kids still chortled.

I looked down at myself, and I saw three mud circles, one formed perfectly over each already wet boob, then a particularly large one that covered the spot where my big, fat belly is.

Well, I thought, at least I'm not naked anymore. I am emotionally destroyed and physically devastated, but I am no longer flashing.

I HATE DISNEYLAND.
```

---

## IC-1249: Drop Dead Gorgeous - Screenplay

- Title: Drop Dead Gorgeous - Screenplay
- Author (byline): Lona Williams
- Work: Not specified
- Publisher: New Line Cinema
- Publication date as stated: 1999
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: GLADYS, BECKY, TESS, AMBER, VOICE OVER, JOHN, HAROLD, JEAN, LESLIE, IRIS, LISA, MAYOR, PASTOR
- Teaser before the introduction: Yes
- Spoken words (computed): 1144
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
In the heart of small-town Minnesota, where the American Dream wears a sash and heels, the American Teen Princess Pageant isn’t just a competition — it’s survival. Every year girls with big hair and even bigger dreams take the stage. For some, it’s tradition. For others, it’s escape. For one… it’s destiny. And somewhere between patriotic speeches, talent routines, and suspicious “accidents,” we begin to realize that in Mount Rose . . . Winning isn’t everything. It’s the only thing.

Welcome to Drop Dead Gorgeous; screenplay by Lona Williams — where the smiles are bright, and the competition is fierce.
```

### Performance text (classify this)

```text
GLADYS: (Pg 48) Welcome to the Mount Rose American Teen Princess Pageant. Every contestant you'll meet tonight is special and unique, [and] they all have one thing in common. They're all "Proud - to - be - an - American!" (Pg 4-5) I know what some of you say, "Pageants are old fashioned" and "demeaning" to the girls -- things are different here in Mount Rose! (Pg 9-10) When I was seventeen, I was crowned American Teen Princess. And this year. . . drum roll please, my daughter, Rebecca Ann Leeman is competin'.

BECKY: (holding a 9 mm which she loads while she is speaking) Hi, I’m Rebeca Leeman, [president of the] Lutheran Sisterhood Gun Club. My mom gave me this nine-mil for my 13th birthday. I'll always remember what she wrote in the card: “Jesus loves winners.” That’s why, no matter what I do . . . (shoves magazine back into her pistol) I aim to win. (smiles to camera, then kisses her 9 mm)

TESS: (Pg 11) (holding a dachshund) Tess Weinhaus (fake smile as Kenny licks her face) This is Kenny. Spike, my German Sheperd, went to live with on a farm after he attacked me. (quick to reassure) It wasn't his fault. I had beef jerky in my front pocket. (pulls up shirt) They re-made my belly with skin from my butt.

AMBER: (Pg 9) (sweet as pie, with a wide-eyed expression) Hi, I'm Amber Atkins. (Pg 20-21) I got dreams of getting’ out of Mount Rose and bein’ a big-time reporter like Diane Sawyer. I mean, guys get out of Mount Rose all the time for hockey scholarships or prison. But the pageant’s kinda my only chance. (she’s interrupted)

AMBER’S MOM, ANNETTE: (off stage, yelling, coughing) Hey, Amber, y'get my smokes?

AMBER: (fake smile) That’s my mom. (yelling offstage) I'll get them in a sec!

GLADYS: (Pg 46) Tomorrow night, all but one of these girls will walk out of here a loser.

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

AMBER’S MOM, ANNETTE: Let me tell you “scary,” Amber. Look at me. I’m a “lifer” here. Best I can hope for is to end up in a decent “raisin ranch” where they’ll change me twice a day. (smiling) Amber, this pageant is your ticket out of here. I know you can win! I love you so much. ***** Back on-stage******

GLADYS: (Pg 60) (pauses as Iris runs on stage and whispers something in her ear) I was just told that contestant number 7, Lisa Swenson, has quit the pageant.

LISA: (runs out on stage) (Pg 59) And since my costume was okay’d a month ago, I’m givin’ it to Amber!

GLADYS: (with no other option) (Pg 61) . . . Number 8, Amber Atkins . . . (Music)

AMBER: (steps to center stage and performs an amazing tap dance routine. May include moon walking, River Dancing and moves never seen before. Make this hilarious)

**** Final Awards Ceremony in progress****

GLADYS: (Pg 63) (DRUM ROLL; opens envelope) And the 1st runner-up is . . . contestant #8, Amber Atkins. (shock and disbelief, but then Amber steps forward to take the trophy)

AMBER: (Pg 65) (tearing up) Well, at least, y’know, I got to perform. And Mom got to see me.

GLADYS: (Pg 63-64) (ushers Amber aside) And finally, the moment I know I've been waiting for . . . she'll be competin' for the title of Minnesota American Teen Princess . . . my daughter – Number 7, Rebecca Ann Leeman!

BECKY: (Pg 65) (almost manically rushes forward) Goodness-gracious, it hardly seems real, y'know? I mean, I won! I'm the winner! (with each photo she changes her smile and expression. She loves this) AMBER’S MOM, ANNETTE: (Pg 64) (from the audience, still chain smoking) We was robbed! ***** The next day: Main Steet – Pageant Parade*****

MAYOR: (Pg 67) (into bullhorn) Welcome to our first ever American Teen Princess Parade – which also happens to be the unveiling of our new sewer system! While Becky gets on her float, any questions about the new sewer?

BECKY: (Pg 68) (as Gladys helps her climb onto the float) It smells funny. Like gasoline. My dress’ll reek.

GLADYS: C’mon, Rebecca. This [swan float] cost your dad a pretty penny. Now get your a** up there and show me some teeth! AMBER’S MOM, ANNETTE: (Pg 64) (near the float, still chain smoking) We was robbed!

(creepy, sinister smile; then takes out lighter to light another cigarette) . . . (Suddenly, like a gasoline soaked pinata, the float EXPLODES!) ***** Days later – Funeral*****

PASTOR: (Pg 71-72) That’s why, dear Lord, it’s with such great sorrow that we turn over to you a young woman whose dream of ridin’ on a giant swan brought about her untimely death.

IRIS: (approaches Amber) As actin’ President of the Mount Rose Civil Servettes, it’s my duty since Becky can’t fulfill her duties – cause she’s dead-n-all – to make you Mount Rose American Teen Princess. (puts tiara on Amber)

AMBER: (Pg 73) Oh my God . . . Okay, okay . . . (squeals) I only got four days . . . I gotta practice! (turns to cameras) (Pg 49) Living in a country where no matter who you are or where you come from, you can grow up and become what you've always dreamed of, makes me, Amber Atkins, proud to be an American!

AMBER’S MOM, ANNETTE: (off stage, yelling, coughing) Hey, Amber, y'get my smokes?
```

---

## IC-1250: Fangs of Endearment

- Title: Fangs of Endearment
- Author (byline): Dave Barry
- Work: I’ll Mature When I’m Dead
- Publisher: Berkley Trade
- Publication date as stated: April 2011
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: BELLA, STEWART, PHIL, PETE
- Teaser before the introduction: Yes
- Spoken words (computed): 2011
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dave Barry
Book: I’ll Mature When I’m Dead
ISBN: 978-0425238981
Publisher: Berkley Trade
Date (Month/Year): April 2011
```

### Introduction (context only: never use it for content warnings)

```text
Twilight . . . Who doesn’t love a good vampire vs werewolf saga, right? As proof, Stephenie Meyer’s Twilight series has sold over 100 million copies. But the question is . . . why? I apologize in advance to Team Edward and Team Jacob, but let’s face it . . . the writing is . . . bad, laughably bad.

Have you ever heard of “purple prose” – It consists of words and phrases that sound stilted, overly descriptive or cliché. No? Let me show you what I mean. This is Dave Barry’s Fangs of Endearment - a humorous tribute to the writing style of Stephenie Meyer. . adjectives and adverbs and similes, Oh, my!
```

### Performance text (classify this)

```text
BELLA: With a feeling of ominous foreboding, I turned my battered old pickup truck into the last remaining parking spot outside Creepstone High School. I glanced in the rearview mirror and scrunched my forehead in dismay as I realized for the millionth time that I do not consider myself at all attractive, although roughly 85 percent of the male characters I encounter either fall in love with me or want to kill me, or both, and in the movie version I am portrayed by a total babe.

Chapter 1: Warning

BELLA: Heaving a sigh of exasperation, I creaked open the truck door, and with my trademark charming clumsiness, fell out face-first. But before I hit the asphalt, Phil [aka Team Edward] was there to catch me, having covered the 75 yards from his luxury car to my truck in 2/10ths of a second. Fortunately nobody noticed this because Phil is brilliantly clever, and the other students at Creepstone High have the observational skills of boiled ham.

Phil swooped me into his arms using the super vampire strength that he has in addition to his super vampire speed and his ability to read minds, perform complex mathematical calculations in his head, assemble a working nuclear submarine entirely from clock p arts, and recite all the lyrics to Guys and Dolls . . . backward.

Phil, a gorgeous brilliant wealthy sophisticated centuries-old vampire posing as a high-school student for reasons that are never totally clear, gently set me down on the parking lot and took my hand in his strong and perfect hand. As we entered the school I felt Phil’s grip tighten. Possibly fracturing my ring and index fingers. Looking up I saw the reason: Stewart [aka Team Jacob] was striding toward us in an ominous way. Stewart is a member of an indigenous tribe of Native Americans who become werewolves at puberty, in addition to developing acne. They do not get along with the vampires. One time in Boys’ phys. Ed. The two sides played each other in volleyball, and before it was over seven civilian students had been disemboweled. This could have created a real stink had not the Creepstone High authorities, who are even less observant than the student body, concluded that the cause was an unusually fast-acting stomach flu. (to Stewart) “Hello, Stewart” (to audience) He looked at Phil with a look of pure lanky indigenous hatred before turning to me and replying, with a voice drenched in the aching and smoldering longingness of a powerful emotion that I knew he could never express in words. (to Stewart) “What is it?”

He looked at me with his dark lanky eyes. Suddenly his expression changed to one of dark foreboding.

STEWART: (whispering hoarsely) If you go out in the woods today, you better not go alone.

BELLA: (to Stewart) “What . . .” (to audience) I protested elliptically. But Stewart was already striding lankily away. Finally finding my voice, I inquired, (to Phil) “What did he mean by that?”

Phil turned his perfect gaze upon me, causing me to be struck by how unbelievably handsome he is, with his perfect face and chiseled cheekbones, and his gorgeous eyes that change color depending on how recently he has sucked all the blood out of a live bear, and his perfectly teased hair tousling down over his broad gorgeous forehead.

PHIL: I’m sure it’s nothing. I’m especially sure it’s not Denise the vengeful psychopathic female vampire from the previous book who has vowed to hunt you down and torture you to death and who has been sighted recently in the woods around Creepstone. There is definitely no need to worry about that.

BELLA: Despite Phil’s reassurance, there was something in his tone that troubled me. But what was it? What had Stewart been trying to tell me? Was something bad about to happen? Would I soon find myself in yet another dramatic plot situation filled with peril? And why did everybody find me so attractive?

Chapter 2 – Decision

PETE: “How was school today?”

BELLA: inquired my father, Pete [aka Charlie]. Pete is chief of police of Creepstone, but he is not exactly Sherlock Holmes, if you catch my drift. He has so far failed to pick up on the fat that my boyfriend is a vampire who spends every night in my room, and that y other boyfriend is a werewolf, and that Creepstone, not to mention the entire state of Washington, is teeming with violent homicidal supernatural creatures, about 60 percent of whom are trying to kill me personally.

(to Pete) “Fine.” (to audience) Satisfied, Pete grunted and returned to his paper. Then remembering something in his mind, he looked up again.

PETE: By the way, I want you to stay out of the woods.

BELLA: (with a gasp and air of foreboding) Why?

PETE: In the past two days, 158 hikers have been killed in the woods around Creepstone.

BELLA: (to Pete) Killed? (to audience) I felt a cold feeling shoot through my veins like an intravenous Slushie. (to Pete) How?

PETE: It’s the darnedest thing. All of them were violently dismembered, apparently by someone or something with incredibly savage strength. Some of the victim’s limbs were found as far as two football fields away from their bodies.

BELLA: I stared at him with a facial expression of shock. (to Pete) “But how . . .” (to audience) I searched for the words to complete the question that was even then forming in my brain. (to Pete) “How did two football fields get into the woods?” (to audience) Pete shook his head and shrugged, raising and lowering his shoulders to indicate he didn’t know the answer.

PETE: That’s got us stumped so far. Right now we’re working on the theory that it could be a bobcat, or a pack of unusually aggressive squirrels. But until we get this thing figured out, I don’t want you going out in the woods, OK?

BELLA: My forehead puckered into a frown as I remembered that Phil has mentioned that Denise the psychopathic vampire had been sighted recently in the woods. Could she have something to do with the 158 slain hikers? Should I mention any of this to Pete? Nah. The more I thought about it, the more I knew what I had to do: I had to go out into the woods alone. That’s what I always do with my trademark stubbornness: I place myself in grave plot peril when there is no coherent reason to do so. Some people may call this ridiculous, but I am guessing that “some people” have not sold [100] million books to date.

I prepared to go out into the woods with nothing to protect me except my various attractive supernatural boyfriends. I did not know what peril I was about to face. All I knew was one thing, the most important thing of all: Whatever happened, it would involve me.

Chapter 3: Peril

BELLA: I stumbled through the woods, tripping with clumsy endearingness over the logs that lay everywhere, like the corpses of dead trees knocked down by gravity. It was getting dark, and I knew that Phil would be out looking for me with his tawny eyes nestled in the perfection of his face. Stewart would also be looking for me in his lanky way with his bulging, rippling muscles or giant snout, depending on what form he was in.

I came to a clearing completely surrounded on all sides by the dark forbidding words. I walked into the clearing as the cold wind blew my hair around into a big trademark mess, although fortunately I don’t care about hair or makeup because the last thing I need to do is make myself even more irresistible. With a feeling of even greater foreboding than usual, I kept walking forward, putting one leg in front of the other in an alternating sequence.

Suddenly, I saw movement at the far edge of the clearing. I stopped and stared. A chill slithered up my spine like an ascending iguana wearing tiny booties made from pieces of Fudgsicle as I saw the terrifying shadowy figure step menacingly into the clearing. With a shock of recognition I recognized who it was: Denise. She bared her teeth, revealing her needle-like fangs, which glinted brightly in the moonlight like some kind of sharp highly reflective things used in a simile. I squinched my eyes shut, preparing myself to be killed in a horrible manner. The dramatic tension mounted to a fever pitch as I waited to feel Denise’s teeth plunge vengefully into my neck and suck my blood out like a giant supernatural mosquito. I wondered how much it would hurt, and how long it would last before I was dead, and who, if anybody, would take over as narrator.

And just then it happened, a dramatic turn of events so unexpected and shocking that nobody could have predicted it in a million years without having read the previous books. I heard a snarling sound and opened my eyes to see that Denise, instead of attacking me, was fighting for her life. And the person she was fighting against – the person who, against all odds, had appeared at the last possible instant to rescue me, was: [Donald Trump] *the text says “Barbara Walters”, but Donald Trump may be more fun and more relevant*

No, I am leavening the narrative with humor. It was really Phil. His eyes flashed me an alarmed look of tawny ominousness.

PHIL: (urgently) Run away; they’re coming!

BELLA: He pointed toward the edge of the clearing. I looked in that direction, and my mouth gaped open as I saw them emerging from the woods: [Phil’s] vampire family: Grover, Buck, Scooter, Eldrigede, DeeDee, Trixie and Skeeter. Grover nodded to Phil with a special code vampire nod, indicating something ominous was about to transpire.

PHIL: Stay here. Stay perfectly still. Whatever you do, don’t do anything to draw attention to yourself.

BELLA: An incredible battle had erupted between the werewolves and the various attractive sets of vampires. There were snarls and roars and hideous supernatural screams. It was incredibly exciting and terrifying, although because of my trademark inability to describe action in anything except very general terms you are just going to have to take my word for this.

As the battle raged on, an alarming thought crept into my mind: I was not playing a central role. I realized that I needed to do something. But what could I, a mere human, although a highly endearing one, do? Then it struck me: I could draw attention to myself.

Frantically I looked around, searching for a sharp object. Suddenly I saw it, lying on the ground, clearly visible in the bright moonlight: A sharp object. I picked it up and stabbed at myself. Blood streamed redly down my leg. Suddenly there was a vampire stampede coming my way at the speed of vampire, with the werewolves right behind.

They were almost on me, dozens of blood-crazed vampires and enraged werewolves. I knew there was no way I could be saved. And then, at the absolute climactic height of the action sequence, everything went dark.

Chapter 4: Resolution

PHIL: She’s coming around. . .

BELLA: (to Phil) What happened? (to audience) Phil shook his head lovingly.

PHIL: You almost got yourself and all of us killed because of your unbelievably irresponsible, deranged, and self-centered behavior, but that just makes me desire you more, you crazy, quirky, irresistible woman, you.

BELLA: But how did you win the climactic fight?

PHIL: Through a lot of action.

BELLA: Wow. That must have been incredibly exciting. (sighing in resignation) Well, at least our other troubles are over. (to audience) Phil looked at me with an expression of not totally agreeing with my assertion. (to Phil) What is it? Is something wrong?

PHIL: It turns out that all those recent hiker deaths were not caused by Denise, but by a long-dormant supernatural race of giant homicidal pine cones who have been awakened by global warming and now prowl the woods around Creepstone each night, savagely attacking every living thing in their path!

BELLA: I thought that was just a Native American legend.

PHIL: If only. It’s only a matter of time before they come into town and are attracted to you. And on top of all that, there’s also the fact that Stewart and I are still mortal enemies who could very well kill each other in our relentless struggle to possess you.

BELLA: Until the next book . . . .
```

---

## IC-1251: Fifteen Minutes

- Title: Fifteen Minutes
- Author (byline): Dave de Christopher
- Work: Best American Short Plays 1998-1999
- Publisher: Applause Theatre & Cinema Book Publishers
- Publication date as stated: April 2001
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NANCY, ANTHONY, LIBBY, DR. BLEDSOE
- Teaser before the introduction: Yes
- Spoken words (computed): 1703
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dave de Christopher
Book: Best American Short Plays 1998-1999
ISBN: 1557834296
Publisher: Applause Theatre & Cinema Book Publishers
Date (Month/Year): April 2001
```

### Introduction (context only: never use it for content warnings)

```text
(no introduction)
```

### Performance text (classify this)

```text
NANCY: Welcome to "Nancy After Dark". Tonight we're talking about infidelity - who does it, who they do it to, and what about the children? Stay tuned. [She strikes an animated pose, freezes for a few seconds.]

15 minutes of fame (or famous for 15 minutes) is an expression coined by American artist Andy Warhol. It refers to the fleeting condition of celebrity which then passes to some new object as soon as the public's attention span is exhausted. Like it or not; consumed by the craze of struggling to avoid it . . . In today’s world, reality TV is the hottest thing going. But have we gone too far by showcasing vulnerable people so we can "catch them in the act" and "scold" them publicly? Dave de Christopher takes the current Reality TV phenomenon one step further in his play Fifteen Minutes.

ANTHONY: What? What are you doing? [ANTHONY: turns on lamp on his bedside table. Stage lights come up full. Person in downstage corner is a woman in a pink jogging suit, hereafter known as AUDIENCE.]

NANCY: Shhhh! Okay, we're clear. [She begins stretching her mouth in various directions, then rattles off some tongue twisters.] Red leather, yellow leather, red leather, yellow leather, red leath

ANTHONY: [Still groggy.] What are you doing?

NANCY: My lip-loosening exercises. I need to improve my diction if I want to go national.

ANTHONY: National what?

NANCY: Only syndicated, not network. But the Viacom guy is supposed to come to the show on Thursday, then take a meeting with me.

ANTHONY: What show?

NANCY: Go back to sleep, Tony. My talk show "Nancy After Dark".

ANTHONY: You ... pfffft ... you don't have a talk show.

NANCY: [With patronizing patience.] Practically everybody has a talk show nowadays. There are five in the neighborhood already.

ANTHONY: This has got to be a dream ...

NANCY: [Sharply.] Yes, it's a dream, go back to sleep. We're coming out of commercial soon, so you'll either have to be quiet or pull the covers over your head and pretend you're sleeping. You're good at that, aren't you?

ANTHONY: How can I sleep with all this talking, and with that [person] watching and with the lights on?

NANCY: Look, this is our twenty-third show in the new time slot, and it's the very first time you woke up, so you tell me. [Pause.]

ANTHONY: I don't believe you. SO where's the camera?

NANCY: It's hidden. [Gesturing.] In the right eye of... that red-headed girl ...in the sad eyes painting

ANTHONY: No ... no, it's not. Why am I arguing with you?

NANCY: Alright, it's not. Go back to sleep, Tony.

ANTHONY: Did you ... [Getting a sudden idea.] Is this supposed to spice up our sex life?

NANCY: No, but if you have an idea for a show, you can call and leave a message at 1-800-GO- NANCY. [Strikes a pose. To AUDIENCE.] We're back ... talking about infidelity.

ANTHONY: Infidelity?

NANCY: That's Tony, my husband. [With an artificial laugh.] Ha, ha, go back to sleep, honey. Our first guest is no stranger to infidelity. Meet Libby. [Warmly.] Welcome to my world.

LIBBY: Thank you, Nancy.

NANCY: [Gentle voice.] So. Tell us what happened.

LIBBY: 'Kay. He was my boss ... [She sniffs.] ... At the plant ... [She sniffs. ] And he'd say nice stuff about my hair and my clothes.

NANCY: That's how it started?

LIBBY: That ... [Eager to fall in with NANCY's scenario.] ... Yeah! Yeah, that's how it started, Nancy. That's how it started.

NANCY: [Taking her hand.] Go on, please.

LIBBY: And one thing led to another.

NANCY: [Suddenly sassy] No, no, girlfriend. I don't think so. [Warm again.] We're trying to feel your pain, so be specific.

LIBBY: Well ... he went from complimenting my clothes and my hair to complimenting my body.

NANCY: [Pretending not to understand. ] Your body? Well what did he say?

LIBBY: He said ... [She sniffs.] ... "Nice rack." Nancy, which part is the rack?

NANCY: SO he complimented you and you had sex with him?

LIBBY: Yes. No! hat's just how it started. I was trying to explain what he's like.

NANCY: You're leaving something out though, aren't you, Libby? [Pause.] He's married, isn't he?

LIBBY: Yes. But it wasn't like that. I didn't know he was married.

NANCY: He never told you ...?

LIBBY: He didn't wear a ring.

NANCY: We're coming up to a break, so cut to the chase.

LIBBY: He blackmailed me.

NANCY: Really? Wow! How?

LIBBY: He said he'd fire me if I didn't ... submit to him.

NANCY: He wanted you to give it up.

LIBBY: Yeah, he wanted me ... He made me give it up, Nancy!

NANCY: Audience, would you like to meet this guy? Well we will, right after this break. [NANCY strikes a pose and holds it for several seconds.] Okay we're clear.

LIBBY: Nancy, I just want to say thank you

NANCY: I'm sorry I'm not allowed to talk to you during the break; it takes the spontaneity out of the interview, [Quietly.] What a to-do to die today at a minute or two to two. A thing distinctly hard to say but harder still to do. For they'll beat a tattoo - of course... [She strikes a pose.] ... at twenty to two '" Doctor, you're on deck!! Okay, we're back in five ... [She strikes a pose.] ... four ...three ... [She mouths "two, one."] ... We're back with Libby. Libby has spent some time with our resident therapist and now feels ready to confront the married boss that she had an affair with. Isn't that right, Libby?

LIBBY: Yes, Nancy.

NANCY: Well, I've got a surprise for everybody! [She hits ANTHONY:.] Wake up! [ANTHONY: bolts up in bed. LIBBY gasps.]

ANTHONY: What!? [His eyes are barely open.]

LIBBY: [A sad wail.] Tony...

NANCY: SO now you recognize him?

ANTHONY: [He turns on bedside lamp. Lights come up full.] Elizabeth? What are you doing here?

LIBBY: [To NANCY.] I didn't really look at him before. I was talking to you.

NANCY: [To AUDIENCE, instantly plaintive.] Yes, it's true. Tony is the one. Tony is the adulterer. I am sharing my pain.

ANTHONY: How could you do this?

NANCY: It's sweeps week. We need to get high ratings.

ANTHONY: How could you do this to me?

NANCY: [Boldly.] I'm doing it to me, too. My life is an open book. [Pause.] Confession is good for the soul.

ANTHONY: Maybe it's time to get it out in the open.

NANCY: Air our dirty laundry.

LIBBY: Get ... get it off our chests.

NANCY: [Seriously.] So, Libby, let's first get straight, Tony calls you ... Elizabeth?

LIBBY: It's my professional name.

NANCY: I thought it was your slut name. I'm sorry. I don't know what's happening to me. My talk show host self is warring with my talk show guest self, and I feel very volatile ... [Turning to AUDIENCE.] ... and you're seeing it live on tape. Libby, is there anything you'd like to say to Tony?

LIBBY: Why did you lie? I feel so guilty, dirty, cheap ...

NANCY: We can all understand that.

LIBBY: Why? [She sniffs] Why?

NANCY: Tony... why?

ANTHONY: [As if it's an amazing phenomenon.] I don't know... we were drawn together ...

NANCY: It just happened.

LIBBY: But why? Not how, Tony? Why?

NANCY: Good question, Libby. And we'll answer it right after this break. [NANCY strikes a pose, holding it for five seconds. LIBBY stares at the floor.

ANTHONY: considers his options.] We're clear. [Calling offstage.] Doctor, get ready!

DR. BLEDSOE: [Off] I have counted the tiles on your shower wall four times! Just introduce me, and don't forget my hyphen.

NANCY: QUIET! [She strikes a pose.] We're back in five, four, three ... [She mouths "Two, one.'1 ... We're back. I couldn't get Libby and Tony to talk during the break, but maybe our resident therapist can help. Please welcome Doctor Allegra Shayne-Bledsoe. Welcome to my world.

DR. BLEDSOE: Thank you, Nancy. I'm feeling a lot of tension in this room.

NANCY: Anger, yes, I can feel it too.

DR. BLEDSOE: No, I think it's sexual tension, Nancy. [She sits and takes ANTHONY:'s hand.] Tony... may I call you Tony?

ANTHONY: Yes.

NANCY: There are a few other things I'd like to call you.

DR. BLEDSOE: [Sharply.] Please, I'm trying to work here!! [to ANTHONY:.] Tony, what do you want?

ANTHONY: A good night's sleep?

DR. BLEDSOE: Humor is a very common defense mechanism.

ANTHONY: All right. I'd like to put this behind me ...And get on with my life.

DR. BLEDSOE: Good work, Tony. That's a very healthy need. But I think that's up to Libby and Nancy. Gals, what do you think? Libby? Do you think you can put this behind you?

LIBBY: I guess so. But what about our baby? [Crying.] What about little Toni?

DR. BLEDSOE: You and Tony have a son?

LIBBY: A daughter; Toni with an "i" ya know? She needs her daddy. Tony hasn't seen her in four months, and he hasn't sent us any money in almost a year.

DR. BLEDSOE: How old is little Toni with an "i"?

LIBBY: She'll be two in October.

DR. BLEDSOE: SO Nancy... what are you feeling now?

NANCY: [To DR. BLEDSOE.] I'm not sure. [To LIBBY.] Haven't you ever heard of adoption? [To DR. BLEDSOE.] I don't think I'm in touch with my feelings. [To LIBBY.] Haven't you ever heard of birth control? [To DR. BLEDSOE.]

No wait... something's coming. [To LIBBY.] Haven't you ever heard of self-control? [To DR. BLEDSOE.] I feel bad ... angry ... powerless ...

DR. BLEDSOE: And what do you want to do?

NANCY: I'd like to kill her ... [This is a guilty pleasure.] ... I think. Is that wrong?

DR. BLEDSOE: Feelings are not right or wrong. They just are.

NANCY: Well, I do. I feel like killing her ... Doctor? Men stray... And I think Tony and I have a chance to heal our wounds. Don't you, Tony?

ANTHONY: Absolutely.

NANCY: So thank you for your feedback, but I'm going to be sticking with Tony, and focusing my revenge on Libby.

DR. BLEDSOE: Good work, Nancy. In the words of Stephen Sondheim, the choice may have been mistaken, but the choosing was not.

NANCY: And unfortunately we're out of time. SO I guess we'll all have to wait until tomorrow to find out what that revenge is.

DR. BLEDSOE: Well, it is sweeps week.

NANCY: Libby, can you come back tomorrow?

LIBBY: I can't come back tomorrow. I'm a guest on "Desiree 'Til Dawn" down the street. My husband is a cross-dressing priest.

NANCY: All right, all right. Let's compromise. [NANCY opens drawer of night table, pulls out black glove and puts it on quickly.] A perfect fit! [NANCY pulls knife from drawer and stabs LIBBY in shoulder. LIBBY screams.] Stop being such a baby it's just a flesh wound. [To AUDIENCE.] Thanks for coming into my world. I hope you'll visit "Nancy After Dark" tomorrow. Sleep tight. [NANCY strikes a pose]
```

---

## IC-1252: French Fries from Talking With

- Title: French Fries from Talking With
- Author (byline): Jane Martin
- Work: Talking With
- Publisher: Samuel French, Inc.
- Publication date as stated: April 1983
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: ANNA MAE
- Teaser before the introduction: No
- Spoken words (computed): 972
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jane Martin
Book: Talking With
ISBN: 0573630216
Publisher: Samuel French, Inc.
Date(Month/Year): April 1983
```

### Introduction (context only: never use it for content warnings)

```text
Forget the Seven Wonders of the World. Globally, the Golden Arches are surely the most infamous man-made landmark. For over 50 years, more consumers have chosen McDonald's as the site of their McConsumption than any other fast food chain. With over 25,000 restaurants worldwide, McDonald's has certainly achieved an overwhelming presence. Could we live without McDonalds? Oh sure, we say we could live without Micky D's, but when push comes to shove we've all got Big Mac on the mind. Come on, admit it, you want one right now don't you? Meet Anna Mae . . . she’s attached to McDonald’s and here’s why. . . French Fries from Talking With by Jane Martin.
```

### Performance text (classify this)

```text
She is an old woman in a straight-back chair holding a McDonald’s cup. She is surrounded by several bundles of newspapers. She wears thick glasses that distort her eyes in the viewer.

ANNA MAE: If I had one wish in my life, why I’d like to live in McDonald’s. Right there in the restaurant. ‘Stead of in this old place. I’ll come up to the brow of the hill, bowed down with my troubles, hurtin’ under my load and I’ll see that yellow horseshoe, sort of like part of a rainbow, and it gives my old spirit a life. Lord, I can sit in a McDonald’s all day. I’ve done it too. Walked the seven miles with the sun just on its way, and then sat there on the curb till vie minutes of seven. First one there and the last to leave. Just like some ol’ French fry they forgot.

I like the young people workin’ there. Like a team of fine young horses when I was growin’ up. All smilin’. Tell you what I really like though is the plastic. God gave us plastic so there wouldn’t be no stains on his world. See, in the human world of earth it gets all scratched, stained, tore up, faded down. Loses it’s shine. All of it does. In time. Well, God gave us the idea of plastic so we’d know what the everlasting really was. See if there’s plastic then there’s surely eternity. It’s God’s hint.

You ever watch folks when they come on in the McDonalds? They always speed up, almost run the last few steps. You see if they don’t. Old Dobbin with the barn in sight. They know it’s safe in there and it ain’t safe outside. Now it ain’t safe outside and you know it.

I’ve seen a man healed by a Big Mac. I have. I was just sittin’ there. Last summer it was. Oh, they don’t never move you on. It’s a sacred law of McDonald’s, you can sit for a hundred years. Only place in this world. Anyway, a fella, maybe thirty five, maybe forty, come on in there dressed real nice, real bright tie, bran’ new baseball cap, nice white socks and he had him that disease. You know the one I mean, Cerebral Walrus they call it. Anyway, he had him a cock leg. His poor old body had it two speeds at the same time. Now he got him some coffee, with a lid on, and sat him down and Jimmy the tow-head cook knew him, see, and he brought over a Big Mac. Well, the sick fella ate maybe half of it and then he was just sittin’, you know, suffering those tremors, when a couple of ants come right out of the burger. Now there ain’t no ants in McDonald’s no way. Lord sent those ants and the sick fella he looked real sharp at the burger and a bunch more ants marched on out nice as you please and his head lolled right over and he pitched himself out of that chair and banged his head on the floor, loud. THWACK! Like a bowling ball dropping. Made you half sick to hear it. We jump up and run over but he was cold out. Well those servin’ kids, so cute, they watered him, stuck a touch pepper up his nostril, slapped him up right smart, and bang, up he got. Standin’ an’ blinkin’. .Well how are you, we say. An’ he looks us over, looks tight in our eyes, and he says, I’m fine.. And he was. He was fine! Tipped his Cincinnati Reds baseball cap, big, jus’ swallowed the canary grin, paraded out of there clean, straight like a polebean poplar, walked him a plumb line without no trace of the walrus.. Got outside, jumped up, whooped, hollered, sang him the National Anthem, flagged down a Circle Line bus, an’ rode off up Muhammad Ali Boulevard wavin’ an’ smilin’ like the King of the Pharaohs. Healed by a Big Mac. I saw it.

McDonald’s. You ever see anybody die in a McDonald’s? Nor sir. No way. Nobody has ever died in one. Shoot, they die in Burger Kings all the time. Kentucky Fried Chicken’s got their own damn ambulances. Noooooooooo, you can’t die in a McDonald’s no matter how hard you try. It’s the spices. Seals you safe in this life like it seals in the flavor. Yesssssssss, yes!

I asked Jarrell could I live there. See they close up around ten, and there ain’t a thing goin’ on in ‘em till seven A.M. I’d just sit in those nice swingy chairs and lean forward. Rest my head on those cool, cool, smooth tables, sing me a hymn, and sleep like a baby. Jarrell, he said he’d write him a letter up the chain of command and see would they let me. Oh, I got my bid in. Peaceful and clean.

Sometimes I see it like the last of a movie. You know how they start the picture up real close and then back it off steady and fat? Well, that’s how I dream it. I’m living in McDonald’s and it’s real late at night and you see me up close, smiling, and then you see the whole McDonald’s from the outside, lit up and friendly. And I get smaller and smaller, like they do, and then it’s just a light in the darkness, like as star, and I’m in it. I’m part of that light, part of the whole sky, and its all McDonald’s, but part of something even bigger, something fixed and shiny. like plastic.

I know. I know. It’s just a dream. Just a beacon in the storm. But you got to have a dream. It’s our dreams make us what we are.
```

---

## IC-1253: A Girl Named Zippy

- Title: A Girl Named Zippy
- Author (byline): Haven Kimmel
- Work: Not specified
- Publisher: Doubleday
- Publication date as stated: March 2001
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1718
- Already set (do not supply): none

### Source block (context only)

```text
Author: Haven Kimmel
ISBN: 978-0385499828
Publisher: Doubleday
Date (Month/Year): March 2001
```

### Introduction (context only: never use it for content warnings)

```text
A kindergarten report card summed up the young Haven Kimmel as someone who "is disruptive in class. Colors outside of the lines. Talks out of turn." Instead of registering disappointment, her parents promptly congratulated her for this achievement. Encouraged, their daughter developed a distinctive personality through her own characteristically sprightly rules. Affectionately nicknamed after a roller-skating chimpanzee, Zippy Jarvis finds her whimsical name only the beginning of her unique adventures in tiny Mooreland, Indiana.

A Girl Named Zippy - Growing Up Small in Mooreland, Indiana. By Haven Kimmel.
```

### Performance text (classify this)

```text
Zippy: (Looking through binoculars at a woman named Edythe who lives across the street.) My sister says she eats a stew made out of puppies.

Julie: Nuh uhn. (spoken as if she wants to hear more)

Zippy: Melinda says she takes the puppies when they’re at their cutest, when they’ve got all that extra skin, and just tosses them in a pot of boiling water with some carrots, and that’s her dinner.

Zippy: (spoken directly to the audience) When I told my mom about the puppy stew she just said pshaw. I asked her wasn’t it a fact that Edythe was all the time trying to kill my best cat, PeeDink, and she said Edythe just didn’t like cats in her yard, and that PeeDink always got away safely. I asked her wasn’t it true that at our last church picnic Edythe had brought cookies that appeared to be covered in snot?

Mom: Now you’re just being ridiculous. (trying to shoo her outside)

Zippy: What were they made of, then?

Mom: Well. I’m sure I can’t say. But only because I didn’t taste them.

Zippy: Ah ha! You didn’t taste them because they came out of Ede’s nose, that’s why!

Mom: (snorting) You’re shameless. We should feel nothing but pity for that old woman.

Zippy: (Pushed out the door by her mom. Spoken directly to the audience) I was convinced Edythe ate puppy stew in order to give her strength to put spells on people. I thought this because my sister had also mentioned, in passing, that if Edythe got me in a hard-core eye-lock she could draw me right into her house. When I pressed for the details of what Edythe would do to me once she had me, my sister Melinda became uncharacteristically silent. (To Melinda) Tell me! I have to know! I have to know how to protect myself!

Melinda: Well, sweetheart, (gently trying to press down a clump of Zippy’s gravity-defying hair) you know she hates all of us, but especially you. There isn’t really anything you can do.

Zippy: Why?! (wailing) Why does she hate me so much? I’ve never done anything to her!

Melinda: She hates you because she and Mom used to be best friends, and then you came and broke up their friendship by demanding so much attention. Also she just hates little kids. But especially babies. Especially you.

Zippy: (sitting, defeated) But didn’t she know I was going to get born when Mom was pregnant for me? Couldn’t they have just worked something out then?

Melinda: (looking off in to the distance, still patting the top of Zippy’s head)

Zippy: What? Lindy. What.

Melinda: I don’t think I should be the one to tell you.

Zippy: Aaaaaahhhhh! Tell me what?!

Melinda: Mom doesn’t want you to know yet, but I think you’re old enough. (Pausing for dramatic effect) You’re adopted. Mom was never pregnant for you.

Zippy: (speaking to the audience) Oh. This explained so many things. I couldn’t think of any right off-hand, but I knew my life was about to become tragically clearer to me. (runs inside) Mom! Mom! How could you not tell me I was adopted?! Don’t you think I have a right to know? And who were my real parents anyway? (trying to be mature, but spit flies)

Mom: (reading a book and not looking up) Gypsies, honey.

Zippy: Gypsies? Really? (sits down)

Mom: Yes, I thought we managed a very wise trade.

Zippy: Gypsies? In Mooreland?

Mom: They were just passing through. We heard them long before they arrived, because their horses and their wagons are all covered with bells. It’s quite lovely. And they were led into town by a pack of wolves, who, during the full moon, stand up and preach. (Looks up from her book for a moment.) They were such a sight.

Zippy: What did you trade for me?

Mom: (Looking at her lovingly.) A green velvet bag.

Zippy: A velvet bag?! Who wants a stupid bag?

Mom: Well, it was a very special bag. It had no bottom.

Zippy: Ha! Joke’s on them! (tipping over a little to laugh at the gypsies, then straightening back up as she realizes she’s laughing at her own family.)

Mom: Oh, it looked like it had a bottom. It looked just like a normal bag, except that you could just keep putting stuff in it. It was like the human heart, sweetie: there was no end to what it could hold.

Zippy: If you had such a great bag, then why did you trade it for me?

Mom: The gypsies were camped out down at the school playground, and one night your dad and I were drawn by the preaching wolves. And just before we left, we peeked inside one of the wagons, and there you were, lying on a sheepskin rug in a pool of lantern light. And we took one look at you and it was just like falling in love.

Zippy: Ugh (makes a little throwing-up face)

Mom: (Picking up a few pieces of popcorn, and looking back down at her book.) Plus, you were born with a tail. (Zippy looks at her mom and is speechless, her mouth hanging open.)

Mom: We had it removed so your pants would fit. Also we didn’t want you to suffer in school.

Zippy: (Jumps up and heads for the door) Okay, thanks, that’s good enough for me, I’m just going outside for a minute and . . .

(spoken directly to the audience) I stood on the front step for a moment, contemplating the news. Mom and Dad picked me up from the gypsies and Mom had to tend to me, plus there was all the trouble of having my tail removed, and Mom and Edythe couldn’t talk as much anymore, and Edythe got really mad and jealous. And Edythe had gone on hating me just as much as the day I arrived in the caravan, and nothing would ever stop it, unless she could lure me into her house with the evil eye and squeeze my thumbs. The story snapped itself clear in my mind, like a mousetrap. The most important thing of all was, of course, that I was a gypsy.

I stepped off the front porch and headed for the drugstore for a lemon phosphate. I took my gypsy blood and my tail and walked right past Edythe’s house instead of crossing the street like I always did, but just as I reached the edge of her yard, Edythe stepped out her front door whistling and I had to take off running for my life.

The drugstore was owned by a man named, no kidding, Doc Holiday. Many people found Doc Holiday’s personality objectionable, but I appreciated how one always knew where one stood with him, which was too close and making too much noise. He never even looked at people as he shouted at them. Asking Doc for advice was a mistake. I was once in the drugstore when a woman asked if Bag Balm was good for diaper rash.

Doc: I don’t know! What are you asking me for?! (bellowing, looking north)

Zippy: Doc was not in the business in meddling in other people’s affairs. He didn’t step into fights or defend small children from bullies. The bottom line for me was that I wasn’t safe in his establishment, particularly not from Edythe. At the Marathon station, all the mechanics were on full alert when I was there, and would tell me exactly where Edythe was if they saw her approaching, and Big Dave had even figured out a way for me to climb into a little filthy tool closet if it looked like she was actually coming into the station.

But Doc Holiday was a man of no sympathy. Once when Edythe was chasing me I had blindly run behind the counter, and he instantly picked me up by the back of my shirt and plopped me right back in harm’s way.

To be perfectly candid, Doc and I had a history.

My third-grade teacher had been, in my opinion, the meanest woman in the history of the Mooreland Elementary School, and a bad teacher besides. One day in the spring a tornado came, and our classroom was on the second floor, and when we could actually see the tornado in the distance we turned to our teacher to find out what to do and she was completely gone. I had to drag Julie under a desk, using my unexpected emergency strength, which I now know came from the gypsies.

So one afternoon in the summer after my third-grade year I was standing at the drugstore counter waiting Doc Holiday make my lemon phosphate, when in came my wretched, former teacher. I leaned across the counter and said, “Speaking of the Wicked Witch of the West, huh? There’s no place like home, is there?”

(Spoken directly to the audience) For the first and only time in my life, Doc looked me in the eye.

Doc: She’s my wife.

Zippy: (Spoken directly to the audience) He was very quiet, and so, in fact, was the whole planet. (To Doc) She is? (whispering)

Doc: What’s her name? (drilling holes into her head with his glance)

Zippy: Mrs. Holiday. (muttering, swallowing, can’t look at him.) (spoken directly to the audience) I wished for blindness.

Doc: (Handing her the drink.) That’s 26 cents.

Zippy: (Spoken directly to the audience.) I knew that in an emergency I could never count on Doc, and so I tried to keep my guard up at all times, but sometimes I got sorely distracted, notably when the new Josie and the Pussycats comic came out, which it had on this particular afternoon.

I was standing in the corner behind the magazine rack, trying to read a comic I had no intention of purchasing. When my instincts kicked in and I finally looked up, Edythe was heading straight for me. She was staring right at me and grinning. (stands frozen) I began to pray to the baby Jesus that it would just be over quickly, that she would completely hypnotize me and drag me down to her terrible house and finish me off in whatever way she had planned, and that I would not feel any of it, like a gazelle being eaten alive by a hyena on Wild Kingdom.

Edythe leaned closer to my face. She got closer and closer, and when she was only about three inches from my nose she quickly and sharply clacked her false teeth together like a castanet, which in turn waggled her dreadful and fascinating whiskers and caused her seven chins to undulate in dray waves.

As my vision dimmed and my knees began to melt, I heard Doc Holiday say quite loudly to the ice cream freezer:

Doc: That’s enough, Edythe.

Zippy: (Spoken directly to the audience) Still looking right at me, she straightened up and laughed out loud, clapping her hands in front of her like a child at a carnival. She marched out of the drugstore whistling “What a Friend We Have in Jesus.”

I slid limply into a booth at the back of the store and put my head down, trying to catch my breath. Before I knew it, Doc Holiday was standing over me, offering me a lemon phosphate.

Doc: Talk about the Wicked Witch, huh? (spoken grimly)

Zippy: That woman is going to be the death of me. (staring at her shoes)

Doc: Well, what are you telling me about it for? (bellowing) That’s 26 cents.

Zippy: I slipped the change out of my pocket and placed it gently in his dry, old hand.
```

---

## IC-1254: A Girl’s Guide to Bragging and Lying

- Title: A Girl’s Guide to Bragging and Lying
- Author (byline): Susan Jane Gilman
- Work: Hypocrite in a Pouffy White Dress
- Publisher: Grand Central Publishing
- Publication date as stated: 2007
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: SUSIE, TEACHER, CARMEN, SARA, ROBIN, BATMAN, MOTHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1429
- Already set (do not supply): none

### Source block (context only)

```text
Author: Susan Jane Gilman
Book: Hypocrite in a Pouffy White Dress
ISBN: 978-0446510585
Publisher: Grand Central Publishing
Date (Month/Year): 2007
```

### Introduction (context only: never use it for content warnings)

```text
"This child has a great imagination, but where do I draw the line between imagination and lying?"

It’s a dilemma of parents and elementary teachers everywhere. A wild story here, a crazy answer there, a child fueled by imagination can spout unbelievable tales! Little Susie Gilman learned the difference between the truth and a lie when she was in kindergarten.

A Girl’s Guide to Bragging and Lying by Susan Jane Gilman
```

### Performance text (classify this)

```text
SUSIE: (Pg 24) The day I started kindergarten I made a jarring discovery: all the other girls wanted to be just as fabulous as I did.

TEACHER: (brightly) Now, we’re all going to say our names and what each of us wants to be when we grow up.

SUSIE: (Pg 25) (Raising her hand) Mrs. Mutnick, my name is Susie Gilman, and when I grow up, I want to be a ballerina, and a model, and a movie star, and a director, and a stewardess.

Then I leaned back with a sort of “tah-dah!” look on my face that would eventually endear me to my fellow classmates.

TEACHER: (Pg 26) Carmen, what about you? What do you want to be?

CARMEN: (putting a finger on her chin) Hmmmm. I want to be . . . let’s see . . . a singer . . . and a fashion designer . . . and a trapeze artist . . . and a bride.

SUSIE: I wanted to hit Carmen. Not only was she clearly copying me, but her answers were generally better than mine.

TEACHER: Sara, what about you?

SARA: I want to be a ballerina, too, and a bride, too, but also a princess, a nurse, a gymnast, and a drum majorette.

SUSIE: Oh, me too! I also want to be a princess and a nurse. I forgot to say!

What strikes me now, of course, was how stereotypical our choices were. Not a single girl longed to be a mathematician or a pulmonary cardiologist. (Pg 27) What it really boiled down to [for me], was the “-ess” in the word “stewardess.” It was the culmination of all things feminine and highly desirable. Princess, goddess, actress . . . stewardess. “- Ess” made any profession sound glamorous. If someone had only been enterprising enough to call female MDs “Doctresses” and female scientists “nuclear biolgesses,” I would have been equally enthusiastic about becoming those too.

No matter. After my classmates and I recited our career litanies about a zillion times each, they began to lose their luster. So, we began transforming ourselves. (Pg 28-29) We soon began staking out starring roles for ourselves in an even more fantastic world: Television.

“I call, I’m Ginger!” we’d yell, lunging at the television, trying to be the first one to press her palm over the seductive smile of Tina Louise before the picture flashed to the infinitely duller Professor and Mary Anne. The rule was: Whoever touched a character first got to “be” her for the duration of the show. “I call, I’m Marcia!” we’d shriek, leaving the losers to fight over Cindy and Jan. Cartoons were equally fair game. We “called” Daphne, Veronica, Wonder Woman, and Judy on the Jetsons.

For me one character was the apotheosis of all I admired and hoped to be. By day, Barbara Gordon was the brainy daughter of Gotham’s police commissioner; yet, with one flick of the switch, her vanity table rotated around and she was transformed into Batgirl! - - a crime fighter with stiletto heels, a peak-a-boo black mask and sparkling body suit that made it look like she had been dipped in liquid rubber.

For BatGirl’s big “fight move,” Batman and Robin would lift her off the ground like two chorus boys and Wham! Bap! Batgirl would swing her pointed boots right into the jaw of an oncoming henchman. And once the battle was over and the Riddler and his sidekicks were left d4owning in their own vat of pancake batter, BatGirl whirled around and vanished. Leaving Batman and Robin awestruck in her wake.

ROBIN: Batman, who do you think she really is?

BATMAN: We’ll ever know Robin. I believe we’ll never know.

SUSIE: They’d never see her, but we – the audience – would riding her electric purple Batcycle into the sunset with the wind in her hair while a groovy chorus sang: Batgirrrrrl, Batgirl! Yeah, whose baby are you? * Pretending to be her made me almost dizzy with yearning. There was only [one] small problem . . . She was fictional.

(Pg 33) One day [in show and tell] I planned to show a pair of maracas my grandparents had bought on their honeymoon. Yet when my turn came, I discovered I’d left them at home. Determined not to give up my slot, I informed Mrs. Mutnick that I had something to “tell” instead. (standing in front of class) Tomorrow, my parents are changing my name to Rhinestone. – Rhinestone Gilman! (to audience) But hearing it said aloud with my last name attached, it suddenly sounded a lot stupider than I’d imagined. (to class) (Pg 34) No, wait, I mean Sapphire. They’re changing my name to Sapphire. Sapphire Gilman! (to audience) Yes, that was much better. Plus, I got to keep my initials.

That was the moment it dawned on me that the real purpose of Show ‘n’ Tell was not to show off Frisbees or spoon collections, but to provide me, personally, with a forum for passing off all of my wildest fantasies as bona fide truths. The next day, when Mrs. Mutnick asked who had anything for Show ‘n’ Tell, my hand went up again.

My family and I are moving to Passaic. (Pg 35) For my birthday. We’re going to have a pink bathroom and a swimming pool and a pink fake fur toilet seat cover!

The next day for Show ‘n’ Tell I informed my classmates that I would be dancing that weekend in the Nutcracker Suite Ballet at Lincoln Center. By Monday morning, I’d forgotten my whopping lies of the previous week and had even better things to share.

(Pg 36) (raising her hand again) This weekend, my mommy had another baby! It’s a girl. A girl like me. Her name is Sylvia Goldia. Sylvia Goldia Gilman. I got to pick out her name!

My life from then on was a dream. I danced around the playhouse with my friends, instructing them in proper ballet technique, which they now looked to me for, seeing as I had appeared at Lincoln Center. Everybody called me Sapphire and inquired thoughtfully about my new baby sister. Everything was going perfectly – I was even contemplating what to say next for Show ‘n’ Tell – Christmas in Hawaii? That I was going to appear as a guest star on Captain Kangaroo? – when, suddenly, my mother walked through the door.

TEACHER: (Pg 37) Oh, Ellen, congratulations! I’m so surprised to see you. They let you out of the hospital so early! Sapphire said you’d given birth to a baby girl over the weekend.

MOTHER: (confused) Sapphire? Who’s Sapphire?

SUSIE: I suddenly realized it would be a very good idea to develop an interest in the chalk tray right about then.

TEACHER: Oh, dear. I’m guessing there’s no house in Passaic? And she didn’t dance in the Nutcracker Suite Ballet this weekend either?

MOTHER: (laughing until tears come to her eyes – she wipes them on back of her hand) Just out of curiosity, what did she say her new baby sister’s name was? . . . Sylvia Goldia?

SUSIE: (Pg 38) For a moment I assumed I was off the hook. But the next thing I knew, the other kids had all gone home and my mother had taken me out of my winter coat and she and Mrs. Mutnick were sitting me down at the table and they were reading me a book. --- “The Boy Who Cried Wolf.” You all know the story . . .

MOTHER: So, Susie, do you understand why it’s bad to tell lies?

SUSIE: (nodding seriously) Because you don’t want to get eaten by wolves.

MOTHER: (sighing) Good enough.

SUSIE: The next day, newly chastened, I came to school as Susie again and raised my hand for Show ‘n’ Tell.

TEACHER: (proudly) Susie has something very important to tell the class, don’t you, Susie?

SUSIE: (nodding with her hand in the air) Last night my mother was hit by a truck! This time, Mrs. Mutnick didn’t wait for the end of the day. She telephoned my mother, and during Juice and Cookie Time, they sat down with me again. Out came “The Boy who Cried Wolf” again, and again we had the discussion roughly titled “Why It Is Bad to Lie.” (Pg 39) When we got home from school, [mother] said:

MOTHER: Why don’t we try to come up with the most interesting true thing for you to share? That way, you can show everybody at school how smart you are.

SUSIE: The next day, I trooped into kindergarten armed with my maracas. (in front of the class) Today (shakes maracas) I’m going to tell you about something (shakes maracas) true. (shakes maracas) Today I’m going to tell you about the Cuban Revolution. What’s a revolution? Sometimes, my mommy said, it’s when people in a country don’t like the way the country is. Sometimes lots of people are poor, and only a few people are rich. . .

(Pg 40) Mrs Mutnick was beaming. I had everyone’s attention. Everybody was focused on me. Not because of my costumes, or who I was pretending to be, but because of what I had to say. It was my moment. Finally, I was a stewardess, I was a prima ballerina. I was BatGirl! And I couldn’t help myself . . .

SUSIE: The Cuban Revolution was led by a man named Fidel Astro. He was named after the dog on the Jetsons!
```

---

## IC-1255: The God of Cake

- Title: The God of Cake
- Author (byline): Allie Brosh
- Work: Hyperbole and a Half, Pg 54-75
- Publisher: Touchstone Books
- Publication date as stated: Oct 2013
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: ALLIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1141
- Already set (do not supply): none

### Source block (context only)

```text
Author: Allie Brosh
Book: Hyperbole and a Half, Pg 54-75
ISBN: 978-1476764597
Publisher: Touchstone Books
Date (Month/Year): Oct 2013
```

### Introduction (context only: never use it for content warnings)

```text
Will little Allie get her sugar fix and ride the marshmallow giraffe of awesome or will the grown-ups keep her from her ultimate goal of becoming . . . The God of Cake by Allie Brosh
```

### Performance text (classify this)

```text
ALLIE: (Pg 54-75) My mom baked the most fantastic cake for my grandfather’s birthday. [It] was slathered in thick frosting and topped with creatures my mom crafted out of mini-marshmallows and toothpicks. To a four-year-old, it was a thing of wonder—half toy, half cake, and all glorious possibility. (mimics Mom) “This is for Grandpa, not for you!”

Mom knew that it was extremely important to keep the cake away from me because if I was allowed even a tiny amount of sugar, not only would I become intensely hyperactive, but the entire scope of my existence would funnel down to the singular goal of ingesting more sugar. Cake. Caaake. Cake. Cake. Cake. Cake.

I managed to climb onto the counter and grab a handful while my mom’s back was turned, [and] an irreversible chain reaction was set into motion. Cake. Cake. Cake. Cake. Cake. I had tasted cake and there was no going back. My tiny body morphed into a writhing mass of tenacity encased in desperation. Cake is the only thing that matters!

ALLIE: Mom had prepared the cake early in the day to get the task out of the way. She thought she was being efficient, but really she had only ensured that she would be forced to spend the whole day protecting the cake from my all-encompassing need to eat it. I followed her around doggedly, hoping that she would set the cake down—just for a moment.

Mom quickly tired of having to hold the cake out of my reach. She tried putting [it] on top of the refrigerator, (climbing like a mountain goat) but my freakish climbing abilities soon proved [that] to be an unsatisfactory solution. (Mom sweeps in to grab Allie down from a precarious perch and Allie throws a fit)

Her next attempt at cake security involved putting the cake in the refrigerator and placing a very heavy box in front of the door. The box was far too heavy for me to move. When I discovered that I couldn’t move the box, I decided that the next-best strategy would be to dramatically throw my body against it. (demonstrates) Surprisingly, this tactic did not garner much sympathy. (mimics Mom, unimpressed, arms crossed) “Get up. Go play with your toys.”

I went and played vengefully with my toys for the rest of the afternoon, (pantomimes playing with toys, nicely at first, but turning violent) but I did not enjoy it. All of my toys died horrible deaths. But I never lost sight of my goal. Mom finally came to get me. She handed me a dress because we were leaving for the party soon. (smiling mischievously) I put the dress on backward just to make her life slightly more difficult. I was herded into the car and strapped into my car seat.

As if to taunt me, my mom placed the cake in the passenger seat, just out of my reach. We arrived at my grandparents’ house and I was immediately accosted by my doting grandmother while my mom walked away holding the cake! (struggling against grandma) I could see my mom and the cake disappearing into the hallway as I watched helplessly. I struggled against my grandmother’s loving embrace, but my efforts were futile.

I heard the sound of a door shutting. Mom had locked the cake in the back bedroom. How was I going to get to it now? I hadn’t yet learned the art of lock-picking and I wasn’t strong enough to kick the door in. (wailing) My life’s aspirations were slipping away in a landslide of tragedy. How could they do this to me? I couldn’t take it. My little mind began to crumble. And then, right there in my grandmother’s arms, I lapsed into a full-scale psychological meltdown. (stage 4 non-verbal temper tantrum)

It was unanimously decided that I would go play outside until I was able to regain my composure. I was banished to the patio. (looks through the glass, as pitiful as possible)

I knew the cake was locked in the bedroom; if I could just get them to let me inside . . . maybe. Maybe I could find a way to get to it. I could build an explosive device or some sort of pulley system. I had to try! But at that point, my only real option was to manipulate their emotions so they’d pity me. (crying loudly into the glass door, with pauses to see if they are watching)

I carried on until mom, instead of taking pity on me and inviting me back inside, told me to go play in the side yard because I was fogging up the glass and my sobbing was upsetting my grandmother. (stomps off, glaring over her shoulder) Mom would be sorry if I were to die out there. She’d wish she would have listened. She’d wish she had given me a piece of cake. But it would be too late. (mimics Mom) “My poor baby! If only I had given her more cake . . . maybe she’d still be alive.”

But as I rounded the corner, the personal tragedy I was constructing in my imagination was interrupted by a sliver of hope. Just above my head, there was a window. On the other side was the room in which my mom had locked the cake. (excited) The window was open! (shrugs) -- covered by a screen, but Dad had shown me how to remove a screen as a safety measure in case I was trapped in a fire and he couldn’t get to me and I turned out to be too stupid to figure out how to kick in a screen to escape death by burning.

(pantomime as she speaks) I clambered up the side of the house and pushed the screen with all my strength. It gave way, (jumps into the room) and suddenly there I was—mere feet from the cake, unimpeded by even a single obstacle. I couldn’t fully believe what had just occurred. I crept toward the cake, my body quivering with anticipation. It was mine. All mine.

(proudly, and a little nauseous) I ate the entire cake. At one point, I remember becoming aware of the fullness building inside of me, but I kept eating out of a combination of spite and stubbornness. No one could tell me not to eat an entire cake—not mom, not Santa, not God—no one. It was my cake and everyone else could go *kick rocks.* Meanwhile, in the kitchen, my mother suddenly noticed she hadn’t heard my tortured sobbing in a while. It was unusual for my tantrums to stop on their own like that, so she went looking for me. When she couldn’t find me anywhere, she finally thought to unlock the bedroom door and peek inside. And there I was!

I spent the rest of the evening, alternately running around like a maniac and regurgitating the multicolored remains of my conquest all over my grandparents’ carpet. I was sooooo miserable! But my suffering was small compared to the satisfaction I felt every time my mother had to watch me retch up another rainbow of sweet, semi-digested success.

This is for you, Mom. This is what happens when you try to get between me and cake It didn’t matter how violently ill I felt; in that moment, I was a god (hands on hips, triumphant) —The God of Cake! —and I was unstoppable! (quickly covers mouth and turns to throw up)
```

---

## IC-1256: Heritage, Her-i-tage, and Hair-i-tage

- Title: Heritage, Her-i-tage, and Hair-i-tage
- Author (byline): Adrienne Dawes
- Work: Laugh Lines: Short Comic Plays, Pgs 91-98
- Publisher: Vintage
- Publication date as stated: April 2007
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: REBEKAH, NPO 1, NPO 2, VOICE ON WALKIE-TALKIE
- Teaser before the introduction: Yes
- Spoken words (computed): 797
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
Despite the natural hair movement of the past decade which has led black and mixed-race women to abandon chemical straighteners, for some women, dealing with curly and tightly coiled hair feels like a daily chore. Mothers teach their daughter the best way to deal with this very specific type of hair . . . at least most mothers do. Not Rebekah’s though. Rebekah has been left to figure it out for herself. That is . . . until the Nap Patrol arrives on the scene.

Heritage, Her-i-tage and Hair-i-tage by Adrienne Dawes
```

### Performance text (classify this)

```text
(Pg 91-98) (REBEKAH, sixteen, confronts herself in the mirror. Mounds of bobby pins, barrettes, rubber bands, a variety of creams, oils, combs, brushes, and spray bottles litter the floor. REBEKAH attacks her mass of thick curls, running a huge comb through it awkwardly. Large clumps of curls fall around her. REBEKAH snatches them disgustedly.)

REBEKAH: Eww ... nasty.

(REBEKAH throws the clumps away and returns to. the mirror. She waters her hair down with a spray bottle of moisturizer, then coughs loudly from the fumes. Determined, she dips her fingers into a huge jar of curl activator and glops it onto her scalp. Large puddles of golden glop fall around her. She begins to lose her patience as she tries to mold her goopy, damp hair into a ponytail.)

REBEKAH: (on the verge of tears.) Maybe I should just cut it all off!

(As REBEKAH reaches for a pair of scissors, loud sirens flare. Nap Patrol Officer (NPO) 1 enters stage left, dressed in a police uniform, her pressed hair greased and molded in an intricate bun on the top of her hair. Various black hair supplies hang from her belt like weapons. NPO 1 points a hair dryer at REBEKAH menacingly.)

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

## IC-1257: Hillary: A Modern Greek Tragedy With a (Somewhat) Happy Ending

- Title: Hillary: A Modern Greek Tragedy With a (Somewhat) Happy Ending
- Author (byline): Wendy Weiner
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: Oct 2009
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: CHORUS, ATHENA, APHRODITE, HILLARY, BILL, NEWSCASTER, ACTRESS 2, ACTRESS 1
- Teaser before the introduction: Yes
- Spoken words (computed): 2187
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
Hillary Rodham Clinton - a woman determined to succeed and achieve her dreams in a world in which the deck is stacked against her and the rules of the game thwart her at every turn. Today we call it “karma” . . . in ancient Greece, they called it “the power of the gods.” Perhaps it is as author Wendy Weiner envisions it, a bit of both.

Hillary: A Modern Greek Tragedy with a (Somewhat) Happy Ending by Wendy Weiner
```

### Performance text (classify this)

```text
CHORUS: Bolt the doors. / Close the curtains. / Turn off your cell phones. / For you are the few selected to finally hear the truth. / In a time before Travelgate / And even Watergate, / When humans knew that it was not they - / but the gods - who ruled the earth, / There was a pair even more famous than Hillary and Bill. / More talked about. / More dissected. / We know - it doesn't seem possible.

(Gesture to the heavens. Lights come up on Olympus. In two separate areas stand the goddesses: Athena, strong and majestic, wearing a breastplate and holding a spear. Aphrodite, exquisitely beautiful, in golden toga and sandals. The Chorus introduces them.)

CHORUS: Athena –

ATHENA: Goddess of wisdom, victory - and olives.

CHORUS: And Aphrodite -

APHRODITE: The goddess of love and beauty. Obviously.

CHORUS: That's cool, you might be thinking, / But what does it have to do with ME? / Let us take you then, to our tale, / Which does not unfold in ancient Greece / But in the United States of America. / A country which espouses freedom, liberty, and happiness for all / Yet also a place where a woman has never been president / In this land lived a girl who, at fourteen, / Was desperate to know all there was to know, / She wrote a letter to her country's prestigious space-travel program / Asking them how to apply to become an astronaut. / The letter she received back told her not to bother – girls could not apply.

(Lights come up on Hillary, at age fourteen)

HILLARY: (Letter in hand.) This is so unfair! . . . I'm not crying! I never cry!

CHORUS: It was then that Hillary came up with her mantra. . .

HILLARY: Emotions are stupid and I am smart, Emotions are stupid and I am smart, Emotions are stupid and I am smart . . .

CHORUS: Hillary walked many miles to Illinois' famed shrines / Where the altars of Athena and Aphrodite sat side by side.

(As Hillary arrives at the shrines, both goddesses go on alert to see whose shrine she'll go to. After some hesitation, Hillary goes to Athena's shrine and looks at it solemnly. She kneels in front of the altar.)

HILLARY: O, Athena, Please help me make our world a place where girls can use all the gifts given to them by the gods and become doctors and presidents and even (Painful for her to say.) astronauts. Help me ascend to the male seat of power, The White House.

(Sound of a lightning bolt. Hillary and Athena react.) Get me to Washington and let me rule and I promise to protect girls and right our world's wrongs against them.

(Lights fade on Olympus as Athena descends to earth. She stands in front of Hillary, accompanied by a blaze of glorious light. Hillary is dazzled)

ATHENA: What you want, Hillary, is not something the world wants for you. Do you understand that?

HILLARY: That doesn't scare me.

ATHENA: It should. For deep-rooted beliefs are a far more insidious enemy than any dragon and change is far more frightening to the human spirit than a twenty-foot woman with snakes for hair.

CHORUS: With her fine mind and Athena's guidance, / Hillary easily obtained entrance to Wellesley, / Where she became the first student speaker at a college graduation in the history of the country. / Hillary and her speech appeared in the pages of Life magazine/ So when she arrived at Yale Law School, / She was already a bit of a star./ All was going exceedingly well for young Hillary / Until one night: (Hillary, with her hair pulled back and wearing thick glasses, sits reading and taking notes on a legal pad. Aphrodite enters.)

APHRODITE: Behold Aphrodite, goddess of love and beauty!

HILLARY: (Looking up only briefly.) I don't have time. (Aphrodite is shocked. She's never received such a greeting.)

APHRODITE: Perhaps you didn't hear me. I said- Behold

HILLARY: Ssssshhhh! This is a library. I don't know how information is disseminated in Olympus, but I've devoted myself to Athena. Alone.

APHRODITE: (Excited.) Do you realize that, with a small makeover and a few lessons in the social graces, I could get you any man on this campus?

HILLARY: That is so sexist. It's the 1970s, Aphrodite. Get over yourself.

APHRODITE: How dare you! (Hillary shakes her head as she puts her glasses back on.) No woman defies the call of Aphrodite!

HILLARY: News flash: I'm not interested in being a wife, I'm interested in being a leader.

APHRODITE: You'll regret this. (Hillary rolls her eyes.)

CHORUS: And so Hillary had made her first political mistake. / For Athena was not the only goddess / Who had been grooming mortals in her own image. /Aphrodite had her own disciple . . . (Aphrodite sticks an arrow in Hillary's back.)

HILLARY: Ow! (Hillary pulls the arrow out of her back and looks at it quizzically, then looks up and sees Bill. She is immediately lovestruck.) Who's that?

CHORUS: William Jefferson Clinton. / Bill and Hillary started studying together. And then things got even hotter:

HILLARY: Bill, the exam is tomorrow.

BILL: Like you even need to study. You're smarter than every other student here. And when you smile, you're just about the most beautiful thing I ever seen.

CHORUS: No one had ever called Hillary beautiful before. / Attractive, yes. Pretty, sometimes. Sturdy, sure. But beautiful? No.

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

CHORUS: Hillary's time in Arkansas / Stretched out into eighteen long years. / As Bill was elected governor four times / And she stood behind him for speech after speech / Smiling, nodding, waving, smiling, / All the while preparing themselves / For an election only they believed they could win: / The presidential campaign of 1992. / But just as it looked like they might have a real chance, / Aphrodite decided it was time to remind Hillary who was really in charge ... (Aphrodite, wearing a wig of big blonde hair, stands behind a microphone, at a press conference.)

APHRODITE: (With strong Southern accent.) My name is Gennifer Flowers, and presidential candidate Bill Clinton and I have had an affair. (Hillary watches Aphrodite in horror.) We have made sweet sweet love in my bedroom, in my foyer, on my kitchen table, in my pantry

HILLARY: It's lies! Republican lies! (to Athena) I can't bear listening to that woman. I can't worry that every time my husband leaves the house, he is - there must be some way you can help me! (Pause.)

ATHENA: I didn't want to do this. And yet, maybe it is still what a woman needs to do to succeed in this world. I can remove half your heart. In its place will be anger. An anger all heroes have felt, and it will serve as fuel for your journey. But it has other effects as well.

HILLARY: Such as?

ATHENA: Your ability to compromise . . . The classic female arts that give you social graces, the right tone of voice, the ability to hide a sword behind a smile, those things Lady Bird and Jackie were so very good at, these are strengths you will no longer have. You'll be a warrior. (Athena looks at Hillary. Hillary nods her assent.)

CHORUS: And so that night the ravens came. / Their beaks sharpened by all the cruelty in the world. / Their cold, taloned feet perched on Hillary's chest / As they fought each other towards the prize: Half of her embattled heart.

HILLARY: (Colder and harsher than we've seen her before.) You know, I'm not sitting here - some little woman standing by my man like Tammy Wynette. I'm sitting here because I love him - and I respect him. And you know, if that's not enough for people, then heck, don't vote for him.

CHORUS: And so it was with Great sacrifices / And a little celestial help - A lot of celestial help / Bill and Hillary made it to the White House at last. / Which is when Hillary's problems really began.

HILLARY: (Stiff ) Right now, thirty-seven million Americans do not have health-care. My plan will establish corporate "regional alliances" of health providers. My plan will ensure that, for the first time, women's health-care gets the same attention as men's. My plan -

CHORUS: Her thirteen-hundred-page health-care plan died an ugly death on the floor of Congress.

HILLARY: Scum-sucking misogynist money-grubbing REPUBLICANS! I'm trying to stop people from DYING!

ATHENA: We misread our enemy. Politics isn't like the battlefield. You have to fight your enemy with one hand and stroke him with the other. (She pulls out a mass of computerized data.) According to my polls, right now, they describe you as: strong, intelligent -

HILLARY: (Pleased.) Really?

ATHENA: . . . dishonest and a bitch. (A dead raven with a rolled-up paper in its claws; it lands heavily at Hillary's feet.) A dead raven.

HILLARY: That doesn't seem like a good sign.

ATHENA: Traditionally . . . no. (Athena reaches over, picks up the bird, and pulls out the paper from its claws. She reads its contents.)

HILLARY: What is it?

ATHENA: It's a front-page story about the president and a ... young lady.

HILLARY: What?! (scene change – Hillary confronts Bill) Tell me it's a lie. (No response from Bill.) This girl is only a few years older than Chelsea. (In a cold, attorney-like tone.) Who is she? Do you know her?

BILL: Of course. She's an intern at the White House. And a - a troubled young lady . . I swear. I did not have sexual relations with . . . that woman.

HILLARY: (Giddy with relief) Of course you didn't! What kind of idiot would believe you would take these kinds of risks when the Republicans are just WAITING for something to bring you down? Who would believe any man would throw away his family, his career, his country for - a moment of sleazy pleasure. That's exactly what I'm going to tell the press. (Lights down on them, then up on . . . Hillary sitting stiffly in a chair. A Newscaster, sits next to her.)

NEWSCASTER: (To Hillary.) The president has described to the American people what this relationship with Monica Lewinsky was not. Can you tell the audience watching today: What was it?

HILLARY: An intense political agenda at work! The true story is this vast right-wing conspiracy that has been conspiring against my husband since the day he announced for president.

NEWSCASTER: Let me take your husband out of this for a second . . . if an American president had an adulterous liaison in the White House and lied to cover it up, should the American people ask for his resignation?

HILLARY: Yes. That would be a very serious offense. In fact, what I implore the Congress to do - is appoint a special prosecutor to look into this. Let them unturn every rock, read every letter my husband has sent, ask every oracle! And if I am wrong, may I be struck down by the gods! (A thunderbolt. Hillary and the Newscaster start in surprise.)

CHORUS: It was the first grand jury subpoena for a sitting president's testimony in U.S. history.

The country was lit up from coast to coast by the sickly blue of television screens / As people waited to hear the truth. (Hillary stands alone.)

HILLARY: (To herself.) I will not cry. I will not show humiliation. I will be as strong as a man. I will be a block of marble. (Hillary goes to Bill.) Remember, only answer what they ask you. They're going to try and trip you up. If they can create even the appearance of perjury, it could cost us the presidency. Just keep it brief and stick to the truth and you'll be fine.

BILL: (to the cameras) It depends on what the meaning of the word "is" is. Now, if someone had asked me on that day, are you having any kind of sexual relations with Ms. Lewinsky, that is, asked me a question in the present tense, I would have said no. And it would have been completely true.

CHORUS: Everyone in the country- and the world - Was buzzing with word of Hillary's humiliation.

HILLARY: Fear is stupid, and I am strong. Fear is stupid and I am strong. Goddamn you, Bill. I will not cry.

CHORUS: One single tear. Fell to the ground / And was quickly drunk by the thirsty earth. *****Time passes *****

CHORUS: New York's next senator: Hillary Rodham Clinton! (The sound of raucous applause, hooting and howling. Hillary is loving it.)

HILLARY: Thank you all so much. This is amazing, thank you. There are people who said I couldn't do this, but they weren't counting on you. (Raucous applause.)

CHORUS: Back in that spot / In the White House Rose Garden / Where Hillary's tear had fallen / Something happened to the flowers. / Their beauty grew sharper / And so did their thorns / Put there to protect their splendor / From an often unwelcoming world. / If you stand in the Rose Garden, even today, / And listen very closely, / You can still hear the faintest sound / Of a woman's voice:

HILLARY: . . . There was a time when a woman's dream of being a senator would have been called impossible. The year I was born, 1947, there were no women in the senate. But now I'm here. And I do believe that, one day, whether it be my generation or the next, we will have a female president. CLOSING

ACTRESS 2: And we all know how that turned out!

ACTRESS 1: Close . . . but no cigar!!

ACTRESS 1: Michelle Obama for PRESIDENT!
```

---

## IC-1258: How to Stay Bitter Through the Happiest Times

- Title: How to Stay Bitter Through the Happiest Times
- Author (byline): Anita Liberty
- Work: Not specified
- Publisher: Villard
- Publication date as stated: June 2006
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1571
- Already set (do not supply): none

### Source block (context only)

```text
Author: Anita Liberty
ISBN: 978-0812976199
Publisher: Villard
Date (Month/Year): June 2006
```

### Introduction (context only: never use it for content warnings)

```text
Humiliating her ex-boyfriend Mitchell in public was a perfectly satisfying career for Anita Liberty, but then she had to go and do something she swore never to do — she got over it. Then, to make matters worse, she fell blissfully in love. And now she’s really got problems. What do you do when you are "an angry performance poet" who suddenly finds herself "perilously close to true happiness?"

How to Stay Bitter Through the Happiest Times by Anita Liberty
```

### Performance text (classify this)

```text
(Pg 3) I am Anita Liberty – Anita Liberty! I am the mouthpiece for the scorned masses. I

am the self-appointed spokesperson for the bitter. I am the performance poet who made

a name for herself by devoting her entire career to humiliating her ex-boyfriend, Mitchell,

in public when he left her for a woman named Heather. I’m a cult heroine, dammit! But

now I’m totally messed up.

(Pg 16-17) He seemed nice

He was smart

And funny.

And cute.

I liked his clothes.

So . . . you had one good date. With someone who seemed normal. But seemed is the

operative word here. You never know. You just never know. I dated someone for three

and a half years who seemed normal. And then he wasn’t anymore. In fact, he turned out

to be extremely abnormal. First impressions mean nothing.

(Pg 18-19) He called the next day.

He left me a message saying that he had a really nice time and asking when he could see

me again. Huh? I’m confused. I just seems so . . . so . . . normal.

(Pg 20) He cooked me dinner.

Which was good.

And nothing he said irritated me.

Not slightly.

Not once

And he kissed me.

That felt nice.

(Pg 23) We saw a movie and he held my hand.

He smiled at me a lot.

He told me I was beautiful.

He bought me a bottle of ginger ale

On the way home.

That’s my favorite soda.

Guess what?

It’s his, too.

(Pg 38) I’m confused. It’s been so long since I’ve even wanted to pursue a relationship

that I’ve forgotten how to proceed. It’s all making me very, very tense.

(PG 42) Thing I wanted before I don’t want anymore because they don’t’ involve him.

I want to pay his rent.
I want to lik his stamps
and scramble his eggs.
I want to gae at him adoringly,
Even though if anyone sees me
it will completely ruin my reputation.

I want to write the kinds of poems he deserves to have written about him.

Poems that exalt him. Poems that boost his confidence. Poems that publicly glorify him.

I walk down the street And think about how much I love him and I feel good about all humanity.

Who the hell am I ?!?!!!!!?
I don’t recognize myself.
I’m not the same person I was before I met him.
I‘m totally losing my identity.

(Pg 44-45) Well. I’m allowed to enjoy the fact that I’m so close to being happy. I know it

won’t last and maybe that’s why I’m savoring it. These rose-colored glasses will shatter.

Problems will arise. Flaws will surface. Reality will set in. I would be nervous, but I’ve

never been one to shy away from reality.

(Pg 48) I performed tonight for the first time in front of Good Date. Afterward, people

gathered around me, praising, adulating, fawning. I appreciated the accolades, but I

wanted to find Good Date. I wanted his adulation, his fawn. I approached him and silently

practiced a humble response to his reverence:

“No, really, you really liked it?

You thought it was amazing?

Come on, the best thing you’ve ever seen on stage?

That can’t be true . . .

When I got to him, he took me in his arms and kissed me deeply.

“So, what’d ya think?” He tells me he thought it was great.

“And?” I smile.

“And I have a few notes.

“NOTES?”

“Yeah,” he says. “We can talk when we get home.”

We’re gonna talk when we get home, all right. Because clearly he doesn’t

understand that the last person who tried to give me notes . . . was the first person who

tried to give me notes.

(PG 50-51) . . . he said he wasn’t criticizing, he just had a few “suggestions.” I told him it

was too early in our relationship for him to be giving me advice about my work, when I’d

been doing my work just fine without him for years. He said that maybe I just couldn’t

handle constructive criticism and hat that was a good thing to know about me. I said that

maybe he was just threatened by my talent and my success and that that was a good thing

to know about him. I then asked him what “suggestions” he had. And, ya know, they

weren’t bad. The guy actually had some good ideas. He then went on to tell me, in detail,

how funny and smart I was, etc.

(PG 55) I’m the poster girl for the Society to Mistrust the Longevity of a Romantic

Relationship (better known as SMLRR) And, yet, here I am. Trusting again. Loving again.

They’re going to revoke my membership. And getting reinstated is a bitch.

(Pg 119) We moved in together. No proposal. No promises. Nothing. He told me not to worry, that he wasn’t going anywhere. Whew. That’s a relief. I just feel like I’m having relationship déjà vu.

I’ve been here before.
I’ve given up my apartment.
I’ve trusted my instincts.
I’ve trusted someone.

Boyfriend’s right. There’s no reason to worry. Why would I worry? IT’S NOT LIKE THE LAST

TIME I MOVED IN WITH SOMEONE HE TURNED OUT TO BE A SOCIOPATH OR ANYTHING.

(Pg 120) I’m going crazy. Every week that goes by, every romantic dinner, every time Boyfriend reaches for me lovingly, I think, “this is it. It’s about to happen. He’s going to . . .

ask me to marry him.” I can’t help myself. I can’t stop the train I’m on. I loathe the

woman I’ve become.

(Pg 134) I told you so. What is it about those four words that makes Them roll so deliciously off the tongue?

I told you so I told you so.

Left over from the playground
taunting other kids,
Recognizing the position of power
That being able to see into the future affords you.

I knew it!
I was right!
I’m psychic.
I saw it coming, even if no one else did.
Especially if no one else did.

(Pg 133) We’ve decided to take a break. I said I didn’t want to go on if this wasn’t the real

deal. He said he didn’t want to feel pressured into making one of the biggest decisions of

his life.

(Pg 139) If you’re in a great relationship

with someone who respects you

and you’re ready to get married,

But the person you’re with isn’t,

Break up with him.

That way you’ll eliminate

Any possibility of getting hurt.

Or being happy

(Pg 142) I have to give him his space. I’m not going to call him. He’ll call me when he’s ready. Right? I just have to patient and wait. (Long pause) Okay. I called him. What? I

waited. For sixteen whole minutes. He’s coming over tonight.

(Pg 145) . . . . I’m engaged!
I have a fiancé.
I’m going to have a husband.
But first I’m going to have a wedding!!!
I’m getting married.
I’m getting married!

(Pg 152) And I’m understandably concerned about how that will affect my work.

(Pg 176) All of a sudden, this whole “getting married” thing seems like a terrible idea.

[Why? Because] Our parents must meet. The deal must be approved, notarized and

ordained. Fiancé and I would literally rather eat spoonfuls of live ants than sit through an

evening of polite conversation with the four people who are responsible for our existences.

What if they hate each other? Or, worst-case scenario, what if they get along? Plech. I

don’t want our parents to be in cahoots with one another. Cahoots make me cringe.

(Pg 177) I was starting to have time to waste in therapy.
Filling forty-five minutes was becoming difficult.
Now I won’t have to worry.
Nifty.

(Pg 199) Everyone is annoying me. Everyone.

My family, my friends and oh, the King of Infuriation . . . Fiancé. They can all just go to hell.

I don’t want to have a wedding anymore Fiancé and I are fighting like howler monkeys and

I just can’t imagine that I’m going to look over at him on our wedding day and think, “I’m

so lucky to be marrying you” More likely I’m going to look at him and think, “You’re and

ass-clown. Why am I marrying an ass clown?” I hate Fiancé because he asked me to marry

him and it now seems like some horrible, awful mistake.

We started writing our vows last night. . .

(Pg 200) [Here’s what I came up with]

I don’t know what you’re expecting from me, but I can’t promise to be nice and supportive for ever

and ever in every possible scenario and situation. I just can’t. You know I don’t like to make promises I

can’t keep.
However, I can vow to try.
And I will try. Hard.
I vow that I will try to be nice and supportive.
Although, if I’m being completely honest,
some days I might try harder than others.

(Pg 210) My wedding day was a perfect day
Our wedding day was a perfect day.
It was transcendent and pure.
That day changed my standards dramatically.
Because now I know what it’s like to experience a

perfect day. Not alone. Together.

(Pg 3) I have no reason to be angry anymore. And that makes me angry. I built my entire

career on being angry. It’s what I do. It’s who I am. What was I thinking?? I was thinking

what society wanted me to think – that happy was the goal. Little did I know that being

happy would make me so miserable.

(Pg 215) . . . this time the end is a happy one. A terribly, terribly happy one.

[Oh, calm down. I’ll be back. Just imagine what I’ll be like when I have someone camped

out in my uterus for nine months . . . It won’t be pretty!]
```

---

## IC-1259: I Know Why the Caged Bird Sings

- Title: I Know Why the Caged Bird Sings
- Author (byline): Maya Angelou
- Work: Not specified
- Publisher: Bantam Books
- Publication date as stated: May 1983
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: MAYA, MINISTER, SISTER MONROE, DEACON JACKSON, BAILEY, REVEREND THOMAS, MOMMA, UNCLE WILLIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1554
- Already set (do not supply): none

### Source block (context only)

```text
Author: Maya Angelou
ISBN: 978-0553279375
Publisher: Bantam Books
Date (Month/Year): May 1983
```

### Introduction (context only: never use it for content warnings)

```text
Sitting in church patiently and quietly is tough for children at the best of times, but sometimes events unfold (even during church) that stretches the limits of any child to remain solemn and serious.

You know what I’m talking about: Church Giggles. And once you get the Church Giggles, it’s hard to stop! You immediately try to think about something serious . . . like Moses. That guy had a serious beard . . . Think about Moses. For the love of Moses’ beard, stop laughing!

And you win, for about 30 seconds. But then you spot a comrade – someone else trying to hold in the Church Giggles and you lose all hope of recovery.

I Know Why the Caged Bird Sings by Maya Angelou
```

### Performance text (classify this)

```text
Note: Items in brackets or parentheses are to be acted out, not spoken.

MAYA: In the Christian Methodist Episcopal Church the children’s section was on the right, cater-cornered from the pew that held those women called the Mothers of the Church. On Sundays, it was ordained by Momma that Bailey and I occupy the first row, called the mourners’ bench. I thought we were placed in front because Momma was proud of us, but Bailey assured me that she just wanted to keep her grandchildren under her thumb and eye.

MAYA: People spoke of Momma as a good-looking woman and some said she used to be right pretty. I saw only her power and strength. She was tall, and her hands were so large they could span my head from ear to ear. Each Sunday the minister would announce,

MINISTER: We will now be led in a hymn by Sister Henderson.

MAYA: And each Sunday she looked up with amazement at the preacher and asked,

SISTER HENDERSON (MOMMA): Me? [After a second of assuring herself that she indeed was being called upon, she laid down her handbag and slowly folded her handkerchief. This was placed neatly on top of the purse, then she leaned on the bench in front and pushed herself to a standing position, and then she opened her mouth and the song jumped out as if it had only been waiting for the right time to make an appearance.] [Insert hymn phrase of your choice here]

MAYA: That Sunday Reverend Thomas took his text from Deuteronomy. Deuteronomy was my favorite book in the Bible. The laws were so clear, that I knew if a person truly wanted to avoid being roasted forever in the devil’s fire, all she had to do was memorize Deuteronomy. I also liked the way the word rolled off the tongue. Deuteronomy.

Bailey and I sat alone on the front bench, the wooden slats pressing hard on our behinds. I would have wriggled just a bit, but each time I looked over at Momma, she seemed to threaten, “Move and I’ll tear you up,” so, I sat still. The church ladies were warming up behind me with a few “hallelujahs” and “Praise the Lords” and “Amens“, and the preacher hadn’t really moved into the meat. It was going to be a hot service.

I saw Sister Monroe, her gold crown glinting when she opened her mouth. She couldn’t get to church every Sunday, so she made up by shouting so hard when she did make it that she shook the whole church. It took three women and sometimes a man or two to hold her.

Once when she hadn’t been to church for a few months she got the spirit and started shouting, throwing her arms around and jerking her body, so that the ushers went over to hold her down, but she tore herself away from them and ran up to the pulpit.

SISTER MONROE: [She stood in front of the altar, shaking like a fresh caught trout. She screamed at Reverend Taylor.] “Preach it. I say, preach it.”

MAYA: Naturally he kept on preaching.

SISTER MONROE: [Then she screamed an extremely fierce] “I said, preach it”

MAYA: . . . and stepped up on the altar. The Reverend kept on. Sister Monroe made a quick break and caught the minister by the sleeve of his jacket and his coattail, then she rocked him from side to side.

I have to say this for our minister, he never stopped giving us the lesson. The usher board fairly ran to the minister’s aid. Two of the deacons, in their shiny Sunday suits, joined the ladies in white on the pulpit, and each time they pried Sister Monroe loose from the preacher he took another deep breath and kept on preaching, and Sister Monroe grabbed him in another place, and more firmly. Reverend Taylor was helping his rescuers as much as possible by jumping around when he got a chance. His voice at one point got so low it sounded like a roll of thunder, then

SISTER MONROE: Preach it!

MAYA: Then the pandemonium spread. The spirit infused Deacon Jackson and Sister Willson, the chairman of the usher board, at the same time. Deacon Jackson gave a scream

DEACON JACKSON: [like a falling tree,] Aaaaahhhh!

MAYA: . . . and punched Reverend Taylor on the arm. It must have hurt. Reverend Taylor jerked around surprised, and punched Deacon Jackson. Then Sister Willson caught his tie, looped it over her fist, and pressed down on him. Next thing all three of them were down on the floor behind the altar. Their legs spiked out like kindling wood. Sister Monroe got up and walked off.

SISTER MONROE: (singing) I came to Jesus, as I was, worried, wound, and sad, I found in Him a resting place and He has made me glad.

MAYA: The minister took advantage of already being on the floor and asked in a choky little voice if the church would kneel with him to offer a prayer of thanksgiving. He said we had been visited with a mighty spirit, and let the whole church say “Amen.”

On the next Sunday, Sister Monroe’s fuse was already lit, and she sizzled somewhere to the right behind me. I saw the ushers from the left side of the church near the big windows begin to move discreetly, like pallbearers, toward Sister Monroe’s bench. Bailey jogged my knee. When the incident with Sister Monroe, which we always called “the incident,” had taken place, we had been too astounded to laugh. But for weeks after, all we needed to send us into violent outbursts of laughter was a whispered “Preach it” Anyway, he pushed my knee, covered his mouth and whispered,

BAILEY: I say, preach it.

MAYA: I looked toward Momma over the collection table, hoping that a look from her would root me safely to my sanity. But Momma was staring at Sister Monroe with a severe look. But Sister Monroe’s voice had already reached the danger point.

SISTER MONROE: Preach it!

MAYA: Bailey nudged me again.

BAILEY: [in a whisper] I say, preach it

SISTER MONROE: (echoing him loudly) I say, preach it!

MAYA: Two deacons wedged themselves around Brother Jackson as a preventive measure and two large determined-looking men walked down the aisle toward Sister Monroe. Elder Thomas made the regrettable mistake of increasing his volume. Then suddenly, Sister Monroe broke through the people trying to hem her in, and [ran] up to the pulpit.

SISTER MONROE: I say, preach it!

BAILEY: Hot dog . . . Damn . . . She’s going to beat his butt.

MAYA: But Reverend Thomas didn’t intend to wait for that, so as Sister Monroe approached the pulpit from the right, he started descending from the left, preaching and moving. He finally stopped right in front of the collection table, which put him almost in our laps, and Sister Monroe rounded the altar on his heels, followed by the deacons, ushers, some unofficial members and a few of the bigger children. Just as the elder said . . .

REVEREND THOMAS: Great God of Mount Nebo . . .

MAYA: Sister Monroe hit him on the back of his head with her purse. Twice. Before he could bring his lips together, his teeth jumped out of his mouth and landed right by my foot. Bailey pinched me and said without moving his lips,

BAILEY: I’d like to see him eat dinner now.

MAYA: Now, I dreaded laughing in church. If I lost control, two things were certain to happen. I would surely pee, and just as surely get a whipping. And this time I would probably die because everything was funny — Sister Monroe, and Momma trying to keep her quiet with those threatening looks, and Bailey whispering

BAILEY: Preach it

MAYA: . . . and Elder Thomas with his lips flapping loose like tired elastic.

REVEREND THOMAS: (gummed without his teeth) Naked I came into the world, and naked I shall go out.

MAYA: Bailey’s laugh had worked its way up through his body and was escaping through his nose.

BAILEY: (Snort. Snort. Snort)

MAYA: I didn’t try any longer to hold back the laugh, I just opened my mouth and released sound. [Laughs] Momma said,

MOMMA: Sister!

MAYA: . . . but the bench was greasy and I slid off onto the floor. There was more laughter in me trying to get out. I didn’t know there was that much in the whole world. It pressed at all my body openings, forcing everything in its path. I cried and hollered, passed gas and peed.

I didn’t see Bailey descend to the floor, but I rolled over once and he was kicking and screaming too. Each time we looked at each other we howled louder than before, and though he tried to say something, he was only able to get out

BAILEY: I say, preach.

MAYA: . . . And then I rolled over onto Uncle Willie’s rubber-tipped cane.

UNCLE WILLIE: [The one side of his mouth pulled down as it usually did when he cried (it also pulled down when he laughed). He stuttered,] I’m gonna whip you this time myself.

MAYA: I have no memory of how we got out of church and into the parsonage, but in that parlor, Bailey and I received the whipping of our lives. Uncle Willie ordered us between licks to stop crying. I tried to, but Bailey yelled so loud and disturbed what was left of the service, the minister’s wife came out and asked Uncle Willie to quiet us down.

For weeks after that I stood on laughter’s cliff and any funny thing could hurl me off far below.

Each time Bailey said “Preach it” to me, I hit him as hard as I could and cried.
```

---

## IC-1260: I Love Everybody

- Title: I Love Everybody
- Author (byline): Lori Notaro
- Work: I Love Everybody (and other Atrocious Lies); Pgs 113-132
- Publisher: Villard
- Publication date as stated: June 2004
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: LORI, SAMPLE LADY, BIG HAIR LADY, BAKERY LADY
- Teaser before the introduction: Yes
- Spoken words (computed): 1895
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lori Notaro
Book: I Love Everybody (and other Atrocious Lies); Pgs 113-132
ISBN: 978-0812969009
Publisher: Villard
Date (Month/Year): June 2004
```

### Introduction (context only: never use it for content warnings)

```text
It’s something that we struggle with daily -- it eats us up and causes stress and anger -- annoying people. You know those people. They cut in line, are rude to you in the office or at the restaurant, cut you off in traffic, talk loudly about obnoxious things, play loud music when you’re trying to concentrate, interrupt you. I could go on and on. Lori Notaro decided that a new perspective on others would solve her problem. Her new mantra . . . “I Love Everybody.” Let’s see how it works out!

I Love Everybody by Lori Notaro
```

### Performance text (classify this)

```text
LORI: (Pg 113-132) I was about to do a bad, bad thing. I knew it. I just couldn’t help it. As soon as I saw that big fat hand reach up and grab the last two chocolate chip cookie nuggets from the sample tray, I knew it was my signal. I was going in for the kill. I’m a bad girl. And I can prove it.

LORI: I am not exactly a people person. Not exactly. You see, when I was born, God gave me an ounce of patience that was supposed to last me a lifetime, but it turns out I used all of it up during the first week.

I am not indiscriminately mean; I must be provoked first. I would classify myself as a Pointer-Outer of Extraordinary Acts of Incredible Foolishness. Some people would call these experiences meltdowns, but I would rather consider them Opportunities to Enlighten. For example: • If you are sitting behind me in a movie and you feel the need to converse as freely as if you are in your living room, I will "Shhhh!" you and then I will ask you for ten dollars. I cannot grasp the need to talk in a movie theater. • If you cut me off in traffic like you've got someone in the passenger seat whose severed limb is floating in an Igloo cooler on his lap, then suddenly and inexplicably slam on your brakes for no apparent reason, I will scream, maniacally, and point my finger at you. This • If you try to sneak two weeks' worth of groceries through the express line and think that no one will notice, I will look at your cart, look at you, and then shake my head in utter and obvious disgust. I'm done tolerating your type. I mean it. I have the ability to count to fifteen and I will USE IT ON YOU. • If I happen to be looking out the window and see you allow your dog to take a *poop* in my yard, I will run outside with a pen and a piece of paper and query, "Hey, can I have your address? Because my dog will probably have to crap in the next hour or two, and I'm bringing her to your house to do it."

So I guess I am mean, I can admit that much . . . [And then in that millisecond of reflection] I hatched a brilliant, brilliant, magnificent plan: I would immediately embark on a life as a Nice People Person Person.

Really, I said to myself, how much energy could it take to be nice? A whole lot less than being angry, hostile, and frustrated nearly every time you encountered one of the Foolish, which could realistically be sixty times in one single minute if you were at the movies, the grocery store . . . . driving someplace. All you had to do to be nice was smile and nod your head. Smile and nod. And sometimes toss in a "My, what a pretty dress!" or an "Aren't you delightful?"

So I practiced smiling and nodding, and what a piece of cake! To think I could have been doing this all along! After a couple of hours, I felt I was ready to start a new phase in my life, appropriately titled "I Love Everybody," and it was going to be a good day to test out my new niceness, especially as I was headed to Costco to pick up my nephew's birthday cake before his party.

I Love Everybody

LORI: Two miles from Costco, all is going well until a Chevy two-ton crosses two empty lanes of traffic to squeal in front of me and then reduces its speed to that of a Fred Flintstone car. As I passed the truck, I smiled and I nodded. "Aren't you delightful?" I said, to which he stuck his big, filthy tongue into his cheek and vigorously moved it around as he raised his eyebrows repeatedly. I laughed and said through my smiling, clenched teeth, “Nice.” I Love Most Everybody

LORI: "Hi, how are you?" I said to people passing by who smiled at me, had some sort of visible ailment or challenge, or were in my way, which I figured would earn me more karma nice points, as I had a lot of catching up to do.

It was almost noon, and in Costco, that translates into a free hors d'oeuvres lunch. So I got in line, waiting for my free whatever it was. It was almost my turn, there were only two girls, who looked to be in their very early twenties, ahead of me.

At that precise moment, a sharp, high-pitched noise erupted in front of me that used my
ear as a portal to repeatedly stab at my brain: Brrrring! Brrrring!
1st GIRL: That’s you! Brrrring! Brrrring! Stab! Stab!
2nd GIRL: It is so totally not me! Brrrring! Brrrring! Stab! Stab!

LORI: Answer the stupid phone, I said silently as I tried in vain to turn my head to avoid the auditory assault -- finally forced to cup my hands over my ears. Then the first girl finally opened up her fishing net of a purse and began to dig through it to find the source. She grabbed it, unfolded it, and held it up to her ear. 1st GIRL: Hel-lo! HEL-LO-OH! . . . . (looks sadly at her friend) They hung up. 2nd GIRL: Ohhhhhh . . . . maybe they’ll call back!

SAMPLE LADY: Cherry, raspberry, peach or blueberry? 1st GIRL: I don’t know. What’re you going to get? 2nd GIRL: I don’t know. What’re you going to get?

LORI: THE BLUEBERRY IS THE BEST! JUST GET THAT, PLEASE, YOU TWO VERY DELIGHTFUL GIRLS IN PRETTY DRESSES! I said as I felt the uncontrollable desire to cover my head and rock back and forth. 1st GIRL: This is a skort, not a dress!

LORI: BLUEBERRY! The sample lady handed them the little paper pill cup and they walked away.

I Love Everybody, but Some People Are Simply Undeserving of the Love

LORI: I needed to hurry. I got to the bakery counter, and as the baker was in the process of getting my cake, another customer, a lady with big hair, frosted in chunks, wearing a sleeveless oxford shirt with very tanned arms like tree trunks and far too much pungent perfume, came to the counter and yelled, waving her diamond-encrusted hand at the bakery lady.

BIG HAIR LADY: Ma'am! Ma'am! I only have a question, this will only take a second!

BAKERY LADY: I’ll be right with you.

BIG HAIR LADY: I'm sure this girl can wait, this will only take a second, and it's important. That carrot cake you have over there, do you have any without walnuts? I can't eat walnuts. I am peanut sensitive.

LORI: I took a deep breath.

BAKERY LADY: Those aren’t our cakes. I don’t know what they have in them. They come from other vendors.

BIG HAIR LADY: But my tongue gets big, very swollen. I have a reaction because of an allergy and it could almost kill me.

BAKERY LADY: Maybe you should try a chocolate cake, then.

BIG HAIR LADY: No, I can't, I'm on a diet.

LORI: The big-armed peanut hater turned her cart and rolled away before I could walk over and punch her. Now, finally, with cake in hand, I sped toward the exit. I was making really good time. I was almost through the freezer section when my speedy progress came to a complete halt due to a lady in front of me, pushing her cart at a snail's pace, her arms crossed over the handle of the cart as she leaned on it like the very lazy person she apparently was. I tried to get around her several times, but oncoming traffic in the freezer section was at a bottleneck. I couldn't get around her, and she was making no effort whatsoever to pick up the pace, and I was stuck.

I tightly clutched the handle of my own cart, chanting with a clenched jaw over and over again like a mantra, "I Love Everybody, I Love Everybody, I Love Everybody, I Love Every-body," until I saw a break in cart traffic ahead and geared myself, getting ready to make a break for it.

I jerked forward, clipping the slow, lazy lady's heel in the process. When I was merely two steps behind her, I could no longer hold it in; my Bounty paper towel of patience could sop up no more. I had had enough of the walnut lady, the cell phone girls, the truck guy, and now the slow walker, and I could take no more. And I let it out, loud and clear, so the slow walker would absolutely hear -- "Here's an idea! Why don't you just drop to all fours and crawl through the store! That just might be slower!"

And it worked. She did indeed hear me. She turned to look at me, although she couldn't turn too much because that would have ripped the tube that was connected to her oxygen tank, which was sitting in her cart, right out of her nose. Right out of her nose. And both nostrils, too. Those tubes looked pretty short to me, as she leaned over to make sure they stayed in to keep her, well, alive.

I knew I had just RSVP'ed for my own personal spot in hell, right next to the Skin Pit, across from the Pool of Sin. Forty minutes into my nice-person experiment and I was already out of the game. I ducked down a side aisle, waiting until all witnesses to my meltdown had dispersed throughout the store. I should be ashamed of myself. I couldn't even be nice for a whole hour.

That's when I finally looked up and found myself right back at the freezer department, square in front of the sample ladies, who were busy frying, toasting, and handing out free food. Free food. Well, why not? I said to myself, and walked over to the sample lady whose crowd was the smallest, although I couldn't help but notice a big, frosted head sticking out like a sore thumb. I smiled the biggest grin I had all day when I saw the sample lady was cutting up delicious-looking cookies, and I nodded at her as I helped myself to one.

Someone from behind suddenly bumped me, and without an "Excuse me" or "Pardon me," I saw a big, tanned, diamond encrusted arm that looked awfully familiar reach up to the sample tray and grab two cookie pieces like a goblin then suddenly retreat, almost if on cue.

I turned around and there she was -- her big, frosted head opening wide to pop in the cookie bits. I waited until she chewed a couple of times and I saw her swallow.

I was a bad girl. A bad girl with nothing to lose.

"These are the most wonderful cookies I have ever eaten in my life!" I said as loudly as I could, then turned to the frosted chewing head, who nodded vigorously in agreement. It was then that I embarked on a huge Opportunity to Enlighten with a bold-faced, nutty lie. "Don't you just love chocolate chip walnut cookies? I am crazy about these walnuts!!"

I Tried to Love Everybody, but Sometimes, You Just Have to Hate a Little Too.

LORI: And, with that, I turned back to the sample lady and smiled. "That is a delightful hair net and apron you're wearing."
```

---

## IC-1261: Ida Mae Cole Takes a Stance

- Title: Ida Mae Cole Takes a Stance
- Author (byline): Lynne Nottage
- Work: Life's a Stitch: The Best of Contemporary Women's Humor
- Publisher: Random House
- Publication date as stated: April 2002
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: IDA
- Teaser before the introduction: Yes
- Spoken words (computed): 939
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lynne Nottage
Book: Life's a Stitch: The Best of Contemporary Women's Humor
ISBN: 978-0375719707
Publisher: Random House
Date (Month/Year): April 2002
```

### Introduction (context only: never use it for content warnings)

```text
Do you think black women have attitude problems? I know everyone has their "bad'' days . . . but I've been studying behavior and body language of black women at home, at school, on the bus, wherever (including myself). And I have noticed a lot of "us" have some attitude problems. It might not be on an everyday basis. Sometimes it's there for a second and gone the next. Case in point . . .Ida Mae Cole.

No, I won’t tell you about her. I’ll show you. After all body language is the single most powerful form of communication. More than voice or even words, nonverbal communication cues you in to what’s on another person’s mind. Ida Mae Cole Takes a Stance by Lynne Nottage.
```

### Performance text (classify this)

```text
Ida Mae Cole stands at the bus stop counting the change in her purse. She snaps her gum furiously then sucks her teeth when she realizes that she is twenty-five cents short. Ida stops abruptly to gave at the passersby, cutting her eyes as she meets unwelcome stares. Her clothing is overstated, though clearly color coordinated.

IDA: Go on look! Go on! Does anybody know if this is the bus that go downtown, ‘cause if it is I need another quarter. Anybody got an extra quarter? Well? WELL? CAN’T ANYBODY HEAR ME?

I’m one of those loud-speaking women you always fear on the bus… The women you walk around and say excuse me to at least three times… I dare any of you to tell me otherwise… Yeah! ‘cause you see… I’m the loud-speaking woman who pushes her way forward and always grabs the last potato… peel it, slice it and eat it right there so that everybody knows that it’s mine… Ain’t no trace of attitude here, ‘cause attitude is passé. What I got is Posture! Punctuated! Assume… Numero Uno. Head cocked, eyebrows arched, lips pursed, hand on hip, finger pointed and a waving. This is the tell me why I was docked a days’ pay for coming in an hour late ‘cause my daughter had a fever. This is the get off my stoop and go on home position. This is the try me stance, the tell me stance, the why don’t you take your fingers off me stance.

Lawd, I stepped on into this posture just the other day. I’d pulled number twelve down at the health clinic, and then had to wait eight hours for the doctor to tell me he… ain’t… gonna… see… me… Well, I marched on in his office, I stripped down to the paper robe, oh yes, which covered everything but the bootie. MMM! … You have to leave, he said like he’d just been served the last pig’s foot in the jar, and you know how that taste after it been sitting in the sun for a few months. Try me! I said… And he did, he tried me … And you know what happened … I GOT EXAMINED! The first time in four years, too, and waited eight hours for the doctor to feel my ti… toddlytutus and ask me how come I hadn’t come in sooner, sooner? Sooner! Only day off in the last year and he’s going to ask me how come I didn’t come in sooner … Shoot …

Posture number two. Legs spread, smile taut, head swaying … The go ‘head ask me girl, I won’t tell. The oh really, the oh no, oh but it ain’t true that he wears her panties beneath his suit. That’s what I told her, least five times that he was no good, ‘cause I know his type. He gonna make you clean up, then won’t show. He gonna make you full up, then won’t stay, make you pay out, then won’t go. And I know what I’m talking about ‘cause if you shift the posture on just one foot it becomes a welcoming posture, a thank you posture, the yes I will marry you, the no, I love only you … The where were you, the what do you want looking at me that way? I need you, I’m sorry, I’m here stance … The one that receives the drunken blows and the casual insults, that took an extra shift in the factory to pay for his new suede coat from Vim’s, that prayed the siren wasn’t going to bring me no bad news about my child, that … Shucks … that don’t forget, no punctuation needed …

Not even that time on the bus when … when … I turned my head, and here comes one of them big-thighen women traveling in my direction, and I’m not in the mood to move … bump! She slaps one of her thighs up against mine and the vibration sends a tremor on through my body. Excuse me! We say in unison. I strike posture number one. She don’t move. I don’t move. Her finger starts waving, my finger starts a waving. Her head starts a moving, my head starts a moving. You going to let me by? She says, deep like Barry White. No place to go! I say smooth like Anita Baker. I eased on into posture number two to let her know I’m flexible.

Then she had the nerve to pull a posture on me I’d never seen before. So I tried all variations. And she kept throwing them back at me. We locked eyes, and I thought oh lawd we’re gonna throw down right here on the bus heading out to Kings Highway. Then I saw in her eyes the night she’d gotten drunk, the vacationless year, the death of her youngest child, the mammogram results she hadn’t told anybody about, and the new suede coat she bought at VIM’S for her man … I turned away quick, if we didn’t have the same posture, if we didn’t. I took two steps to the side, and said GO ON SISTER! GO ON! And that big-thighed sister shoved on down to the back, until she disappeared behind a bus full of attitude.

And it all leads to head tilted, muscles relaxed, arms crossed and feet firmly planted, this is the just so position. It’s the just so position you see on the bus …

Yes, I’m the loud-speaking woman you avoid on the bus, with the steadfast posture you can’t get around. Anyone got a quarter? I don’t have enough change. I said does anybody got a quarter?
```

---

## IC-1262: Indoor/Outdoor

- Title: Indoor/Outdoor
- Author (byline): Kenny Finkle
- Work: Not specified
- Publisher: Broadway Play Publishing
- Publication date as stated: 2006
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: SAMANTHA, SHUMAN, MOUSE, OSCAR
- Teaser before the introduction: Yes
- Spoken words (computed): 1825
- Already set (do not supply): none

### Source block (context only)

```text
Author: Kenny Finkle
ISBN: 978-0881453300
Publisher: Broadway Play Publishing
Date (Month/Year): 2006
```

### Introduction (context only: never use it for content warnings)

```text
As is true with most cats, Samantha didn’t have an easy childhood. She was ripped away from her mother as soon as she was old enough to eat real food and dropped at the animal shelter.

(Thunder clap and or ominous music) Don’t they kill cats at the Animal Shelter. (Thunder clap and or ominous music) You get five days. Five days to find your “forever home”. And then . . . . Well, let’s not think about that. How in the world do you do that when you are 1 of a gazillion stray cats? Indoor/Outdoor by Kenny Finkle
```

### Performance text (classify this)

```text
SAMANTHA: (Pg 1) (Lights up on SAMANTHA by herself) (To audience) Hi. My name's Samantha (Just then SHUMAN appears on stage, looking for SAMANTHA.)

SHUMAN: Samantha? SAMANTHA?? (He wanders off.)

SAMANTHA: That's Shuman. I live with him. He's looking for me right now. We'll get to him in a minute. First though, you need to know me. I suppose this is as good a time as any to tell you . . . I'm a cat.

SAMANTHA: (Pg 4) (To audience) The Animal Shelter was totally horrible. Think Amistad meets Schindler's List. I wanted to find true love. But I didn't know how to go about it. How do you find your true love? Especially in an animal shelter where you only have five days to do it. (Pg 6-8) And it was at that exact moment that Shuman fell into my life. (SHUMAN enters.) From across the crowded shelter our eyes met. (He sees SAMANTHA. They look at each other.) BAM! A connection! It knocked us both off our feet! (They both fall backwards.) Then, he got up, walked to my cage, and a second later I was in his arms. He was so warm and strong. And then he put his hand under my chin and started scratching and I, for the first time in my life, started to purr.

SHUMAN: You're purring. Are you happy?

SAMANTHA: Yes very. (To audience) And if I didn't know then that he was my true love. What he said next sealed the deal.

SHUMAN: Hi. I guess you're coming home with me. You're beautiful. Your name is . . .

(He looks deeply into her eyes) Samantha.

SAMANTHA: (To audience) Shuman named me.

SHUMAN: You don't have to be scared anymore, I'll love you like you are supposed to be loved until the day I die.

SAMANTHA: (To audience) And Shuman took me to his home. And became my true love. And it was everything I dreamed it would be. For a while at least . . . (Pg 10-13) Before we go any further, I think that this may be a good time to tell you more [about] Shuman, the man. (We are now in SHUMAN's office; he is working at his computer) Shuman works from home, doing web design. In case you didn't notice, Shuman is very sensitive and cries over almost anything.

SHUMAN: Save. Save! SAVE! SAVE!!!! Why won't you save? I, I, I, I- (He starts crying hysterically).

SAMANTHA: Every morning Shuman gets up and talks to himself in the mirror.

SHUMAN: I am worthy of success. I am worthy of love. I am worthy of hope. I am worthy of dreams. I am worthy of Samantha. I am worthy of this day. Good morning.

SAMANTHA: (To audience) One of Shuman's favorite things to do is put on music really loud and sing and dance to it. Sometimes he even lets me dance with him.

SHUMAN: Everybody dance! (SHUMAN scoops up SAMANTHA and sings and dances to Madness' song Our House.) Our house in the middle of our street. Our house in the middle of our ... Our house ... (To Samantha) Oh Sammy! You are the greatest thing that's ever happened to me!

SAMANTHA: (To audience) And it was at this exact moment that I noticed Shuman had a crumb of food on his upper lip. Shuman noticed me staring at him and he said-

SHUMAN: You're trying to look into my soul aren't you?

SAMANTHA: No . . . I'm not. You have a crumb on your lip and its driving me crazy! (To audience) And for the first time I realized that maybe Shuman didn't always understand me. Just as clarification, I think I should say I speak in Cat. This is what I really sound like. Meow wowo, memeo, meowwww. So I suppose it shouldn't be all that surprising but still, sometimes he'd be so far off the mark it'd be shocking! (Pg 23-24) [Case in point . . . ] one night, I heard a rustling in the kitchen and I had to see what it was. I ran into the kitchen and found a mouse rifling through the cabinets. (A MOUSE appears)

MOUSE: Oh sh**, a cat.

SAMANTHA: (To audience) No one had ever told me about mice before, but somehow I instinctively knew that mice were evil and that I was to rid the house of them. So that's what I attempted to do. All night long. (SAMANTHA chases the MOUSE) Finally, I got the mouse under my paw.

MOUSE: Ow.

SAMANTHA: Shut up. (To audience) And I started toying with it. Like so. (To MOUSE) Should I let you go?

MOUSE: Yes, please, I didn't mean to be here anyway, I must have taken a wrong tum in Albuquerque-

SAMANTHA: (To audience) For those of you that are weak of heart, I'll refrain from illustrating the rest of what happened. For those of you that aren't weak of heart, think Texas Chainsaw Massacre meets Nightmare on Elm Street! However, suffice it to say, eventually I killed it. . . Killing. Chasing. Using my instincts like that. It came so naturally. And it felt so good! I felt like a wild tigress!

And I never wanted to feel any different! The whole next day I carried the mouse around in my mouth. I started to walk with more confidence.

(Confident SAMANTHA shows us her more confident walk. Shuman notices she has a mouse in her mouth and tries to take it from her)

SHUMAN: (Pg 25-29) Oh, Sammy, let go. Ew. Oh my god. Ew. Ew. Ew. This is so . . . disgusting.The mouse has to be thrown away.

SAMANTHA: No! The mouse is mine. I killed it. You can't just throw it away. Its mine! MINE! (SHUMAN picks SAMANTHA up. She flails.) No! SHUMAN GET OFF ME! THE MOUSE IS MINE! GIVE ME BACK MY MOUSE! (To audience) But he didn't listen to me and he threw the mouse away. After that I snuck out of bed every night and roamed the house looking for danger or excitement or both. And then one night, while stalking through the kitchen, the very thing I'd been looking for found me. And his name was Oscar the cat. (OSCAR the Cat appears. He is one cool cat.) I first spotted him through the sliding glass door. I was frozen to the spot. I couldn't move. I couldn't breathe.

OSCAR: Hey ... sup sweetheart? I'm Oscar. I'm an alley cat. Moved up here from the city a few years back. You're cool. Do you like living inside? I've never done it. Can't imagine what it’s like. Outside is the only place I've ever lived. Born and bred. If you ever got out here, I'd show you all these cool places. Like there's a little garden just down the road. In the afternoon I lay out there and get sun. Have you ever felt sun on your coat? It's heaven.

SAMANTHA: (To audience) And I started to wonder why hadn't Shuman ever taken me outside? Why was I an indoor cat?

OSCAR: You know where I wish I could take you? The beach. Do you know its only sand and water? Just water and sand. It's like a giant litter box. And sand, oh man, sand is supposed to feel like heaven underneath your paws. Sure during the day people are around but at night, it'd be ours.

SAMANTHA: (To audience) Ours. He said ours. I'd never thought of there being another "ours" besides me and Shuman and then there was Oscar saying "ours" and I couldn't help but think that it sounded right. Like I was really supposed to be with Oscar outside and not with Shuman inside. But I loved Shuman. Or maybe I didn't. I didn't know anymore.

SAMANTHA: (awkwardly flirting) (Pg 34-39) My name's Samantha . . . I killed a mouse once.

OSCAR: Samantha. Sa-man-tha. I like that. You're a beast! You're a goddess! You're a tigress! You're-you're so unbelievable! (Suddenly SHUMAN enters the kitchen and flips on a light.)

SHUMAN: Samantha? Who's this? What's going on? Where'd she come from? You two friends? That's so sweet. Come on, let's go to bed

SAMANTHA: No. I'm not going to bed with you Shuman. I want to stay here. I want to stay with Oscar!

SHUMAN: You want me to pick you up? (SHUMAN picks SAMANTHA up in his arms.)

SAMANTHA: (To audience) And I was so angry at him for picking me up and disturbing me and Oscar that I-well I did something I'd never done before. (SAMANTHA bites SHUMAN' s arm.)

SHUMAN: OW!!!! GOD DAMN IT!!!!!! OW!!!!! (SAMANTH, hissing, jumps out of SHUMAN's arms.) I can't believe you bit me! Bad girl! Bad BAD GIRL! You will not be allowed in bed tonight! You can stay out here and think about what you did! (SHUMAN exits. SAMANTHA turns to OSCAR.)

SAMANTHA: So, where were we?

OSCAR: Look, save your breath. I'm an alley cat, 0K? I know how this goes. So I'm just gonna back away now. Real slow. And then it'll be like I wasn't ever here and it'll all be cool. (He starts to leave.)

SAMANTHA: No! Oscar! I want to bust out of here. I'm going to figure something out. I promise. (To audience). Maybe if I started to act wild around the house, Shuman would get the idea and let me out. So I started doing these really complex and bizarre running patterns all around the living room.

(SAMANTHA does a bizarre running pattern. SHUMAN follows, talking as he runs.)

SHUMAN: Sammy? Sammy! Stop! Hey!

SAMANTHA: I then proceeded to destroy everything I possibly could. (As she continues to run, SAMANTHA starts knocking off plants, books, anything in her way. SHUMAN attempts to pick up the pieces behind her.)

SHUMAN: Stop it Sammy! No! That’s expensive! Whay are you doing this? OK. OK. You win. Just go ahead. I need to sit. I need to sit and . . . breathe. (He sits and breathes to calm himself – he may even be crying a little)

SAMANTHA: [But] I knew I had to take things further if I wanted Shuman to kick me out. Finally one morning while in my litter box, it hit me. If you catch my drift... I decided that the best place to do it would be on his computer. After all he spent so much time there and if I really did it right, he would possibly have to get a whole new computer. Soon enough, Shuman discovered it. (SHUMAN enters and sees the computer.)

SHUMAN: No. Ew. SAMMY!!!!!???

SAMANTHA: (To audience) I went right up to him and stared at him with a look of defiance. (SHUMAN picks up SAMMY roughly by the scruff of the neck)

SHUMAN: I've had it with you. Do you hear me? You've destroyed everything in this house! I'm throwing you out. Out into the forest so you can get attacked and killed and eaten by wild animals. (He sets her down to open the door) So, goodbye! And don't come back asking for food. Because I'm not giving you any. (He starts to open the door)

SAMANTHA: (To audience) [I was] so close. And then . . .

SHUMAN: (Stops, takes a breath to calm himself and turns to audience) (Pg 45) She’s a cat! She’s supposed to be simple. That’s why I got a cat! I wanted simple. I’m good at simple. I’m not good at the other stuff. (sadly to SAMANTHA) (Pg 49) No matter what I do you’re not happy.

SAMANTHA: (Still angry) You never listen to me.

SHUMAN: (Pg 51-53) [But] I feel like I know you. (all of a sudden, Shuman can actually hear what Samantha is saying, and a look of amazement passes over his face)

SAMANTHA: If you did, you wouldn’t have thrown my mouse away.

SHUMAN: Your mouse?

SAMANTHA: Yes my mouse! I killed that!

SHUMAN: I know you killed it. It was going to start smelling so I threw it away. It was dead!

SAMANTHA: I loved that I killed that mouse and if you knew me at all you would have known that. (to audience) He thinks I’m simple! (yelling at SHERMAN) I’m not simple! I’m complicated. (Shuman starts to cry, but SAMANTHA is resolute) Your crying isn’t real. You’re a fake. You have no backbone. You are a miserable lonely person. Let me leave!

SHUMAN: (Pg 60-61) (SHERMAN opens the door slowly) Samantha, if you want to go. . Go. I can’t keep you. I don’t want to fight anymore. (Samantha and Shuman stare at each other.) I just wish I were enough for you. But if I can’t be, then I can’t. (Samantha begins to leave, but then hesitates)

SAMANTHA: (pg 68-69) (to audience) And I realized in that moment that by letting me outside, Shuman had told me that he loved me unconditionally. And I knew then that this was my home. (Meows loudly) And I looked Shuman right in the eyes and I said: Sometimes you won’t get me and sometimes I won’t get you, but I’ll love you. And for a second I wasn’t sure if he understood, but I was home. And it was enough. (Pg 71) And soon after that Shuman installed a new front door that had a flap in it, so I could come and go as I please. (She goes through the door) Yeah, I’m outside! (She goes back though the door) Yeah, I’m inside! . . . . (Pg 76) Maybe life is just this. Just this. This brief moment we have together where we’re inside each other and outside ourselves and we can all just let go.

SHUMAN: Oh, Samantha. I love you.

SAMANTHA: Meow!
```

---

## IC-1263: Investment Dating

- Title: Investment Dating
- Author (byline): Ira Brodsky and Barbara Lhota
- Work: Duo Practice and Competition: 35 8-10 Minute Original Comedic Plays for Two Females
- Publisher: Smith & Kraus
- Publication date as stated: September 2004
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: MEG, IRIS
- Teaser before the introduction: Yes
- Spoken words (computed): 1970
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
Two best friends make plans for Homecoming - but when Iris finds out that the plan involves double-dating with Meg's new flame, a NERD, and his best friend; she decides that it will take more than friendship to make her go along with the plan. It will take CASH! Investment Dating by Ira Brodsky and Barbara Lhota
```

### Performance text (classify this)

```text
MEG: (Speaking in hushed tones, with contained excited.) Oh wow. Oh wow. Oh. Wow. I think I'm going to faint. I'm not kidding. You're not going to believe what just happened.

IRIS: (Dryly.) Sister Jaye had you dissect a cow eye again?

MEG: What? No. What are you talking about?

IRIS: Last time you said "You're not going to believe what just happened," Sister Jaye had you dissect a cow eye and then you passed out.

MEG: No, I didn't. Elizabeth Holt passed out. Why do you always make me out to be such a wuss?

IRIS: I don't always make you out to be a wuss. I don't need to. You are a wuss.

MEG: I just felt wobbly and pretended to faint to get out of class early.

IRIS: (Nods and smiles.) Uh-huh. And I suppose you had an incredible need to smash your face into the floor pattern when you watched me get my ears pierced too?

MEG: (Cringes.) Well, it ... was hot in there.

IRIS: Just admit it, Meg. You have a weak stomach. You pass out. No big deal.

MEG: But I don't! I don't have a weak stomach. I'm cool!

IRIS: I didn't say you weren't cool. You're a cool person who faints. 'Member when they forced us to watch that National Geographic wildlife special and the mountain lion tore the guts out of the-

MEG: All right! I remember. Ewww. Let's think about something else. (Trying to get the image out of her mind. Singing.) La, la, la!

IRIS: (Soothing her by patting her back.) I can just imagine how you felt when Sister Jaye put her scalpel into the cow's

MEG: All right! You're doing this on purpose. How did we get here? I was telling you about my good thing and suddenly we're dissecting cow eyes and wandering down woozy lane.

IRIS: Feeling fainty is a good thing?

MEG: You know very well that I was being ... I was exaggerating. I'm excited. I'm not actually feeling fainty. I just have this incredible feeling. It's like I've lost all my senses.

IRIS: And this is a happy thing? To lose your senses?

MEG: (She smiles.) Yes, it is.

IRIS: No wonder there are so many happy Republicans [Democrats] right now.

MEG: Don't be so cynical, Iris.

IRIS: So don't be so sappy. It encourages my cynical-ness. I have to counterbalance the "S" factor. So what is it exactly, not that I really want to know?

MEG: Well. (Quietly, out of the side of her mouth.) You-know-who (Nodding her head in a backward direction very subtly.) asked me to you-know-what.

IRIS: Well, that clarifies things. (Looking over toward her nod.) Which who? Which what?

MEG: (Grabbing her.) Well, don't look!!

IRIS: How am I supposed to know who the (Quietly.) you-know-who is then?

MEG: How can you be so remedial? How many you-know-who's have I mentioned? (Iris gives Meg a look.) OK. Good point. But this is the you-know-who that has been the you-know-who since forever.

IRIS: Really? You're kidding? (Eyes widening. Mouth drops. Beat.) Are you telling me you have a date with (Whispers with reverence.) Kevin? The guy? Mason?

MEG: Oh. No, no. Not that forever. That's last month's forever! Think more recent, more do-able, and more short.

IRIS: (Thinks.) Jason Harley?

MEG: Not Oompa-loompa! Short. Less wow than Kevin Mason, but more smart. My guy sang in the talent show. He always rests his feet on the back of my chair. He gave me his eraser a couple days ago. To keep. Remember? (Iris has no idea.) He blinks a lot and he has this cute dent in his face.

IRIS: Dent? In his face? I'm sure if you mentioned this guy, you didn't mention this dent thing. That I would have remembered.

MEG: The dent crinkles so cute when he smiles.

IRIS: So it's like a dimple or more of a full-size crater?

MEG: Yeah, well, I guess it is more like a dimple

IRIS: OK, erasing the Elephant Man image.

MEG: He's got a great personality, but he doesn't talk really.

IRIS: At all?

MEG: Very little. I mean, how much is really necessary?

IRIS: (Nods.) Some. For instance, if I were in a crisis situation ... like maybe my house was burning or my mother was angry because my boyfriend and I were coming home late from a date. I wouldn't want a strong, silent type. I'd rather have a wimpy talker. A guy who could come up with "Well, we both got food poisoning from something we ate at the salad bar at Denny's. We had to stop at my friend's house right away, Ms. Hemchak so we could ... you know. Otherwise we would have been home on time."

Or, in the burning house situation, a loud, decisive "Help! Follow me!" might be good too.

MEG: Well, sure. In a crisis, but otherwise ... Personally, I don't want a boyfriend who blabbers on and on and on. That's why I have you.

IRIS: Thanks. So let me ask you this. How do you know he has such a great personality if he doesn't talk?

MEG: He doesn't even have one zit!

IRIS: You’re kidding? Find out what he washes with!

MEG: OK, but can we get back to the point.

IRIS: I think I'm lost on the who. Maybe we should start with the you-know-what instead.

MEG: The homecoming dance, Iris! I've been talking about it for the last two weeks!

IRIS: That was anticlimactic. Let's hope the "who" has a little more umph.

MEG: Well, he has the goldfish. (Iris looks terribly confused.)

IRIS: "The" goldfish. (Meg nods.) Is this the only one left in the international community?

MEG: It's the goldfish in the science lab. He won the goldfish last year in the spelling contest and donated it. (Iris is still perplexed.) His last name is also the name of an animal.

IRIS: The fish?

MEG: No! The guy who asked me to homecoming. Look. It's (Mouths "Alex Fox" several times as Iris tries to guess.)

IRIS: Hal Thomas? Our Spanish teacher? That's sick! Although potentially advantageous.

MEG: No, no. (Continues to mouth "Alex Fox.")

IRIS: AI. Al-Ia. Alan? Allan Nicholson?! Oh? (Thinks.) He's cool.

MEG: No, Iris. Nicholson is not the name of an animal!

IRIS: OK, animal last name not last name of an actor who wears sunglasses and dates woman younger than his socks. Oh my gosh-animal? Is it Robin Anto-

MEG: No! His last name is an animal, not his first name. It's (Very quietly, out of the corner of her mouth.) Alex Fox.

IRIS: What did you say? (Meg says "Alex Fox" again very quietly, almost inaudibly.)

IRIS: Huh?

MEG: (Singing.) I just called to say, I love you. (Iris' curiosity is piqued. The name sounds familiar, but she's still unsure. She thinks. Meg does some weird dance move with her hand.}

IRIS: (Yells.) Alex Fox!

MEG: (Grabbing Iris' face to stop her yelling. Meg speaks from the side of her mouth.) Stop! (Pulling her into a huddle.) He'll hear you. He's right over there.

IRIS: Where? (Looks. Meg pushes her arm to stop the head turning.) He can't hear us over there. That's all the way across the cafeteria.

MEG: Don't look! He'll think we're talking about him. He probably just heard you.

IRIS: No, he didn't, but he's going to know we're talking about him because you're doing that thing again.

MEG: What thing?

IRIS: That thing you always do when you think people can hear you when they can't. That side-of-the-mouth thing that makes you look like you have palsy or something.

MEG: (She does it.) I'm not doing anything with my mouth. I'm just talking quietly.

IRIS: (Imitating Meg.) Yes, you are. You just don't know it.

MEG: Oh my God. That does look bad. (She stops the mouth thing.}

IRIS: So Alex Fox, huh? He's kinda boring. I mean, he doesn't talk. At all.

MEG: He sings.

IRIS: True. But not well.

MEG: I thought he was great in the talent show. And cute. All the girls did.

IRIS: What girls?

MEG: Well, I don't know. I thought he was cute.

IRIS: He was. Sort of. For an awkward pubescent white boy with no pitch, no confidence, and no sense of rhythm.

MEG: That's not true! He had confidence. He was probably downright cocky or he wouldn't have gotten up in front of everyone to, to ...

IRIS: To embarrass himself so completely? (Patting her.) Anyway, I'm happy for you, Meg. Have fun.

MEG: No, don't do that talking down to me thing. You sound like I've stooped.

IRIS: Well, obviously you don't mind stooping.

MEG: I do mind stooping. I don't want to live with this feeling that I'm just some big stooper and that's it. I thought this was good-going to the dance.

IRIS: I just think if you were going to agree to go with Alex Fox, you might as well stoop down into the depths of desperation, do some more charity work, and pick up Fred Murphy on the way.

MEG: (Laughs.) Well, that's funny.

IRIS: What? What's funny?

MEG: Well, Alex and Fred are pretty good friends. Funny you mention Fred.

IRIS: Uh-huh. So? Where does the funny come in?

MEG: Didn't you say once ... ? I remember. You said that Fred, although a bit of a cretin, was ... funny, ... special, and ... specially funny.

IRIS: (Beat.} I did not.

MEG: I know you did. You definitely said he was funny and special.

IRIS: Well, I might have used the word ... funny. Perhaps I even used the word special, but you must have misinterpreted my meaning.

MEG: Well, see?

IRIS: See what?

MEG: Maybe I misinterpreted, or maybe you meant it in multiple ways. Because maybe Fred is special to you in some ways.

IRIS: He is. In a mock-and-make-fun-of sort of way. Where is this heading, Meg?

MEG: Well, guys don't like to go to dances alone.

IRIS: True. They don't know where to pin the corsage.

MEG: No, I mean they like to go in a group with a date and a best friend.

IRIS: OK, you know what? I'm late for Spanish.

MEG: (Grabbing her.) Wait, Iris! You've got to do this.

IRIS: Ohhhhhh. Nooooo! I don't have to do anything, Meg. I'm not being pulled into another Bob Alberts fiasco.

MEG: He wasn't that bad!

IRIS: He tried to French kiss me with gum in his mouth. I had a spontaneous and relentless gag reflex and almost choked to death!

MEG: But Fred wants to take you so bad. He likes you. He really likes you!

IRIS: No, he can't! I won't let him! Don't you let him! Uh! Me? Me?! (She points to herself. Meg nods.) Why is this happening? What is it about me that's such a magnet for the festering warts of humanity?

MEG: You're funny and a vegetarian and read philosophy.

IRIS: (Hitting her hand.) That was a rhetorical question!

MEG: You're different, Iris, and lots of guys like that. Not easy to peg.

IRIS: (Beat. Sweetly.) You're different too, Meg. In a rotten, horrible, nightmarish, diabolical way. Now, leave me alone in my misery,

MEG: So will you at least think about it?

IRIS: I'm saying I would rather hang from the gym by my fingernails, be mocked by my fellow art students, and forced to listen to my sister's Britney Spears CDs for twenty-four hours than go to the dance with you and Alex Fox and Fred Murphy.

MEG: Oh please, please, Iris. Just this once. I promised Alex we'd double-date.

IRIS: So un-promise him.

MEG: I can't. I told him it was a sure thing. (Begging.) Oh please. Pretty please. (Iris shakes her head no.) Don't do this to me. This is my life at stake.

IRIS: Well, if Alex is your life, you deserve to perish.

MEG: What if I pay you?

IRIS: (Shocked.) What? Are you serious? (Meg nods.) Sell my company for ... Sell my body, my spirit like some cheap call girl! That's disgusting! How much?

MEG: How much is necessary?

IRIS: (Beat. Taking this in.) How much you got?

MEG: Twenty? (Iris shakes her head with disapproval.) Twenty-five? Come on!

IRIS: For a whole night with a guy who will ruin my reputation for years to come? I don't think you're accounting for the long-range ramifications. I'd consider forty.

MEG: Forty?! I don't have forty, Iris! I've never had forty, ever! Uh! OK, thirty-seven fifty. And that's the best I can do. I'll have to borrow the two fifty from my brother, which you know I can't stand. So what do you say? (Getting on knee.) Please? Please?!

IRIS: (Thinks. Sighs.) I'm such a good friend to you, Meg.

MEG: (Jumping for joy.) Yah! All right! You'll probably even have fun! Fred seems really nice.

IRIS: He ate glue, Meg.

MEG: He was just trying to see if it would kill him. He's scientific!

IRIS: He's disturbed.

MEG: He's one of those late bloomers who will probably be a looker in early college ... or maybe not, but he'll invent some incredible computer program that will change the way we do business for years to come. He'll be a multi-millionaire in a few years and with some help, perhaps from a psychologist or even Dr. Phil, he may become a full-fledged well-rounded human being who you can write about in your depressive autobiography when you get about twenty something.

IRIS: He ate glue, Meg. He ate glue. (Puts out her hand.) So pay up!
```

---

## IC-1264: Just be Frank

- Title: Just be Frank
- Author (byline): Caroline Williams
- Work: Humana Festival 1999: The Complete Plays
- Publisher: Smith and Kraus Publishers
- Publication date as stated: 1999
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: CHARLENE, DIANE, JAN, SECRETARY, MR. ROSS
- Teaser before the introduction: No
- Spoken words (computed): 1559
- Already set (do not supply): none

### Source block (context only)

```text
Author: Caroline Williams
Book: Humana Festival 1999: The Complete Plays
ISBN: 978-1575252070
Publisher: Smith and Kraus Publishers
Date (Month/Year): 1999
```

### Introduction (context only: never use it for content warnings)

```text
Tired of all the game playing and political correctness? Have you ever wished that everyone would simply, “speak the truth . . . be blunt . . . be brutally honest?” It sure would make things a lot easier, right? No second guessing or trying to figure out ulterior motives. Theoretically, life would be so much easier if everyone would Just be Frank by Caroline Williams. . . . Be careful what you wish for . . . you might just get it!
```

### Performance text (classify this)

```text
[Lights up, Morning in a busy office.]

CHARLENE: [strikes a pose in her new attire] It looks expensive, doesn’t it? I won’t say how much . . . but let me just tell you . . . if you even knew, you would die. [beat] Five hundred dollars! The saleslady said it looked incredible on me. You don’t think it’s too loud, do you? She said I’d definitely stop traffic . . .

DIANE: You are hard to miss. I mean, it is . . . pink.

CHARLENE: It’s not pink, it’s salmon. I want to look professional when I approach the boss. I really think this suit says, “I’m a woman. I’m not afraid to wear a salmon suit. I can be a valuable asset to this company.” That promotion has my name written all over it.

DIANE: You mean the Beefy-Treat account? I’m up for that promotion . . . I mean, I was thinking of applying. I thought since my proposal saved the Ferber Cheese-Stick account last year . . .

CHARLENE: Oh, that was you? Well. You should know that Ferber Cheese was child’s play compared to Beefy-Treats. You wouldn’t want to be in over your head.

DIANE: [dejected] I guess you are more assertive than I am . . . and confident. [a beat as she looks at Charlene] And you stand out . . .

CHARLENE: Listen. Since you and I are friends—I’ll be frank. This is the cutthroat world of business. You simply don’t have any killer instincts and rarely do you ever have anything exciting to say. Not that those are bad qualities— you just lack verve.

DIANE: Verve?

CHARLENE: Don’t worry—you still fulfill a very important role here. Where would people like me be without people like you? You’re punctual and efficient and—meek.

DIANE: [on the verge of tears] Mm—meek?

CHARLENE: [big fake smile] In fact, you’re lucky we’re such good friends that we can be honest with each other because, for the most part, Diane, there is no place for honesty in business, and not everyone will be as helpful as I am. Come to think of it, when I become president of this company, my first decree will be to have all of my people be completely honest—all the time. It will revolutionize the world of business. [beat – The tinkingly sound of a wish being granted fills the air- insert sound effect here] Sometimes my brilliance takes even me by surprise. [Charlene stares out in wonderment of her genius] Anyway, my suit is sensational, isn’t it?

DIANE: What do I know—I’m MEEK!

CHARLENE: No need to thank me—

DIANE: [calling out after her as she walks away] Oh yeah, THANKS! [Diane turns back to her computer and furiously types away. Meanwhile, spotlights follow Charlene to the water cooler where fellow employee, Jan, is standing alone. Her face is an expressionless mask of resigned irritation and nausea.]

CHARLENE: Good morning, Jan. How was your weekend?

JAN: Absolute crap.

CHARLENE: Excuse me?

JAN: I got stood up, my minivan blew a tire, and I have a canker sore. Do you mind? I’m trying to look inconspicuous here and you’re standing next to me like a flashing pink bottle of Pepto-Bismol.

CHARLENE: Actually, this suit is not pink, Jan, it’s salmon. What’s gotten into you anyway? I’m counting on you to nominate me for the new account. You’re the only one the old windbag ever listens to. . .

JAN: Actually, Charlene, I’d feel better about myself if you’d continue to earn substantially LESS than I do.

CHARLENE: [still confused] Are you trying to say you’re not going to give me the recommendation?

JAN: Listen, I’ll be blunt. I don’t like you. I’ve never liked you. The way you are constantly waving at me from your desk—I have to pretend like I’m writing or looking for something just to avoid acknowledging you—but you don’t get it . . . you wave, I ignore you and you keep flappin’ away like . . . some kind of—large, flightless bird.

CHARLENE: Well! Excuse me, JAN!

JAN: [ignoring Charlene] And I hope I never have to sit next to you at a lunch meeting again . . . watching you eat could drive a person insane—it’s like watching one of those pointy-faced rodents—incessantly picking and pecking and . . .

CHARLENE: [seething] Of all the rude . . .

JAN: [continuing] . . . and speaking of chewing—your last presentation was so mind-numbingly boring I actually had to work to keep from gnawing off my own arm.

CHARLENE: I have heard just about ENOUGH thank-you-very- much! [Charlene turns to leave.]

JAN: Oh, in that case---before you go, the next time I flirt with the boss in order to advance my own career, I’ll be sure and let slip that you called him a windbag . . . .Good luck! [Jan abruptly walks away.]

CHARLENE: [calling after her] If that’s the way you feel, then FINE—I’ll meet with him myself! [Charlene stalks off to a large reception desk in front of a closed door with the word PRESIDENT printed on it. She addresses a perky secretary. Everything the secretary says is delivered with a cheerful voice and genuinely eager, helpful attitude.]

SECRETARY: [smiling throughout] Hello, Mrs. Parker. How can I kiss your butt today?

CHARLENE: . . . excuse me?

SECRETARY: Would you like some coffee? This is regular but if you’d like decaf, I’ll just leave and come back with the same pot—you’ll never know the difference.

CHARLENE: [confused] Uh—no. I just want to make an appointment with Mr. Ross ASAP.

SECRETARY: [checks appointment book, then looks up, still smiling] I’m sorry but I don’t think he can squeeze your big pink caboose in today. [cheerfully] Is there anything else I can help you with? [Charlene is just about to answer when the phone rings] Just a moment . . . [she holds a finger up to Charlene who waits, fuming] Burton and Ross, may I help you? . . . today? . . . with Mr. Ross? . . . how about 2:15? . . . all right then, buh-bye. [back to Charlene] As I was saying, are you sure there isn’t anything else? I could go fetch some Post-its? Your dry-cleaning, perhaps? After all, what am I here to do if not your mindless, tedious busywork. I do whatever you and all your over-educated colleagues with reserved parking and big pink suits think you’re just too good for.

CHARLENE: [enraged] FOR YOUR INFORMATION the suit is SALMON and I don’t know what your problem is but I thought you said Mr. Ross was busy all day [points at the phone] What was that!?

SECRETARY: No, I didn’t say he was busy—I said I couldn’t squeeze you in. He’s actually free until 2:15. But, due to my inferiority complex and because this appointment book makes me drunk with power, I’ve decided to act out my passive-aggressive rage against you.

CHARLENE: Excuse me but I will not tolerate a secretary with that kind of attitu—

SECRETARY: [interrupting] That’s administrative maintenance engineer and I would care what you were saying if you had any power at all in this company. Since you don’t, I’ll just smile and nod while I look for somebody important to suck up to. . . Oh! There’s an executive! If that will be all Ms. Parker. . . [She grabs the coffee pot and rushes off.]

CHARLENE: What is wrong with you people? [Charlene hesitates and then walks through the door to find Mr. Ross, an older gentleman in a business suit, sitting behind his desk looking over some documents.]

CHARLENE: Mr. Ross?

MR. ROSS: [looking up] Yes? Come in.

CHARLENE: Hi, I was wondering if I could talk to you for a few minutes about a possible promotion on the new dog-treats account? Last month you had mentioned how I was really up to speed and I was thinking, what with my. . .

MR. ROSS: [cutting her off] Hmmmm—yes, the Beefy-Treats. You know, this is quite fascinating. I don’t doubt that you do, in fact, work here, and I may, indeed, have commented on your work…I just can’t for the life of me seem to remember who in the world you are. What department did you say you work in?

CHARLENE: Um. . . marketing and development.

MR. ROSS: Right, right—marketing. You must perform one of those benign tasks that, apparently, I see fit to dole out some measly, pathetic salary for… [cheerfully] in which case I suppose I should hear you out. You were saying?

CHARLENE: Uh. . . well, I had actually come in here about a promotion but maybe now’s not exactly the right time . . .

MR. ROSS: Wait a minute! I do remember you—your desk is just across the way there. . . [he points out there door]

CHARLENE: [excited] Yes! That’s me! Did you recall how I typed up those reports last term?

MR. ROSS: [cheerful and professional] Heavens no! I do recall, however, that I quite enjoy looking at your legs on my way in here each morning…and, considering that my taxes alone are probably twice what you make in an entire year—I suppose it wouldn’t hurt to hand over an account I’ll probably take credit for anyway. Congratulations Miss…

CHARLENE: Parker . . . Charlene Parker.

MR. ROSS: Of course. Congratulations Miss Proctor, the promotion is yours. [earnestly] Good luck and nice rump! [Mr. Ross gives Charlene a friendly thumbs up and goes back to his paper work. Charlene walks back to her desk, slightly disturbed.]

DIANE: [bitter] So, how’d it go?

CHARLENE: GREAT, DIANE! As a matter of fact—WONDERFUL [grotesquely enunciating each word] Did I not explain to you that a salmon suit like this would command RESPECT! [Diane looks at Charlene like she is insane. After a moment, they turn to their respective computers and get to work.]
```

---

## IC-1265: The Kitchen Witches

- Title: The Kitchen Witches
- Author (byline): Caroline Smith
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: Nov 2012
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: ISOBEL, DOLLY, VOICE OVER - ISOBEL, VOICE OVER - DOLLY
- Teaser before the introduction: Yes
- Spoken words (computed): 1346
- Already set (do not supply): none

### Source block (context only)

```text
Author: Caroline Smith
ISBN: 978-0573632860
Publisher: Samuel French, Inc.
Date (Month/Year): Nov 2012
```

### Introduction (context only: never use it for content warnings)

```text
Isobel Lomax and Dolly Biddle are two “mature” cable cooking show hostesses who have hated each other for 40 years. Ever since Larry Biddle dated one and married the other. Now fate has intervened and put them together on a reality TV show. Hold on to your hats, ladies and gentlemen! It’s. . .

The Kitchen Witches by Caroline Smith
```

### Performance text (classify this)

```text
ISOBEL: (Pg 57) Dolly was my best friend. Yep, we were as close as sisters, Dolly and I, all the time we were growing up. We spent every second together – sat next to each other in school, talked for hours on the phone, had sleep-overs. [Then . . . ] our last year of high school we met Larry Biddle. What a character . . .

ISOBEL (VOICE OVER): (off-stage) (Pg 13-14) Dear Babcha, I have been watching you since the other cooking show was cancelled last month. I was wondering do you know Isobel Lomax, the hostess of “Busy Izzy” and if so, can you get me her recipe for Steak and Kidney Pie?

DOLLY: (in a decidedly fake Russian accent and smiling dangerously into the camera) Hello, Jane dear! Of course I know that person you mention. But you sound like nice lady, so I do nice thing. I don’t get you recipe for Snake and Pygmy pie. But I tell you reasons why Busy Izzy show was cancelled. One. Stupid name. Two. Stupid food. Three. Stupid woman. . . .

ISOBEL: (Pg 14-15) (making her way to the sound stage) Ha! . . . I said ha!

DOLLY: Who is . . . (She gasps) . . . Isobel Lomax! What on earth are you doing here?

ISOBEL: Over the past few weeks I have ben watching this . . show. I thought it time I came down in person and let you know I have had enough of this constant slander. Dolly Biddle, you have publicly insulted me for the last time. You can expect a call from my lawyer on Monday. (starts to leave, then turns) Does your viewing audience know that “Babcha from Ukraine” is really Dorothy Plotznik from Sudbury? (Dolly gasps, pans for the camera and then runs off-stage to her dressing room)

ISOBEL: (Pg 16-17) (Taking over the show) Hello folks – Busy Izzy here! I’ll just fill in for a bit – after all, that’s what bosom buddies are for! Now let’s just clear off our counter and start fresh. (She dumps all of Dolly’s cooking into the garbage can) We’ll start by making Izzy’s Perfect Shortcrust Pastry. (begins preparation) Our friend Babcha is really Dolly Biddle, and she was born, not far, far away in the Ukraine but in beautiful downtown Sudbury! How do I know this? Why we grew up together, Dolly and I!

DOLLY: (Emerging from her dressing room without her accent) What do you think you’re doing?

ISOBEL: She was Dorothy Plotznick. Biddle is her married name . . .

DOLLY: At least I go married! At least I had a husband.

ISOBEL: You know perfectly well I dated Larry Biddle first.

DOLLY: In your dreams! I was going steady with Larry long before you oozed onto the scene! Who did he take to the Senior Prom, huh?

ISOBEL: Well, Larry may have married you, but I was the one who made him happy!

DOLLY: That man was never happy!

ISOBEL: How could he be living with you? (pointing with her ring hand)

DOLLY: What is that? (Isobel holds up her hand, showing off a flashy ring)

ISOBEL: What – this?

DOLLY: That’s . . . that’s the Biddle family heirloom ring!

ISOBEL: Larry gave it to me when we were dating.

DOLLY: He told me he lost it! That ring should be mine!

ISOBEL: You can pry this from my cold, dead hand!

DOLLY: (Picking up a chopping knife) Fine by me! (then notices the cameras are still running) (Pg 19) (resumes her poise and In her Russian accent) Well, it’s been so nice sharing time with you each week, peoples, and Babcha is so sorry to say goodbye. So – everybodys . . . remember to eat good, enjoy life and most important . . wash your hands! This is Babcha . .

ISOBEL: (Butting into the camera range) And Busy Izzy!

DOLLY: Saying goodbye!

ISOBEL: And good cooking! (Both wave to the camera until the audience is “gone” – Then the two glare at each other as a phone rings – Dolly picks it up)

DOLLY: (Pg 21) (Still in a Russian accent) Hello? (to Isobel) It’s the Elm Street Bridge Club . . . (listens) Really? You did? What? (to Isobel as she hangs up the phone) They say that was the funniest show they’ve ever seen, they loved it. (a look of shock from both ladies)

ISOBEL: (Pg 22) On the air again?

DOLLY: Together?

ISOBEL: We can’t share a show – within five minutes one of us would be dead . . .

DOLLY: And the other charged with murder! We’ve hated each other almost forty years!

ISOBEL: Well, it’s a ridiculous idea. I have no intention of continuing to air my personal affairs in public.

DOLLY: (laughing) You’ve always opened your big fat cakehole to anyone who would listen!

ISOBEL: That is an outright lie! I am an extremely private person!

DOLLY: Ha! You’re about as private as Madonna’s cleavage. (Pause as both contemplate a future show together) (Pg 23-24) Let’s try it.

ISOBEL: Count me in! The Izzy and Dolly Show!

DOLLY: You mean the Dolly and Izzy show.

ISOBEL: Why should you get first billing?

DOLLY: It’s always alphabetical.

ISOBEL: (Pouts in frustration then a has an idea) . . . [How about] Kitchen Witches!

DOLLY: Oh, I don’t think you can describe me as a witch . . .

ISOBEL: Unless you spell it with a “B” . . . (Pg 34) “Good morning everyone and welcome to the Kitchen Witches Show.” (shakes her head) That’s pretty bland. (In a “wicked witch” voice) A witchy welcome to one and all!

DOLLY: Oh, that is better – although I think it would be stronger if we both said it!

ISOBEL: A witchy welcome to one and all!

DOLLY: And we could cackle a little . . . (they do)

ISOBEL: And how about if we had a cauldron here on the counter, kind of smoking . . .

DOLLY: Ooo, yes!

**********

VOICE OVER - ISOBEL: (Pg 38) (Off-stage) Your Community Service Station is proud to present the premiere broadcast of . . . The Kitchen Witches!

(Jingle - See link for a sample “tune” to use for the jingle at the bottom of this selection or create your own)

VOICE OVER - DOLLY: Let’s turn up the heat and bring this show to a boil With two ladies who mix as well as water and oil!

VOICE OVER - ISOBEL: Now here is the twosome who’ll keep you in stitches It’s Isobel and Dolly . . . The Kitchen Witches! (Witch-like cackle)

(Dolly enters in a Scarlett O’Hara inspired hoop skirt, Isobel is off stage)

DOLLY: (in a bad southern accent) Well, I declare, ain’t this just the prettiest audience I’ve evah seen! Today we’ll be doin’ our salute to the Old South, an’ cookin’ up some mighty tasty vittles, like Burnin’ of Atlanta Spare Ribs and somethin’ that I like to call Rhett Butler Ham Steak!

ISOBEL: (Pg 32) (offstage) What the hell is that? I’m not wearing that!

DOLLY: (Pg 37) (In a soft voice to the audience) She won’t have a choice. While she was in the shower, I swiped her clothes. (louder so Isobel can hear) (Pg 38-41) I seem to be missin’ something . . . My deah friend and cooking partner! (Isobel enters dressed as “Mammy.” She is not happy at all) Well, I declare! It’s Mammy! Now, no salute to Southern Cooking would be complete without Mammy’s famous Buttermilk Biscuits. She makes them so good you’ll think you’ve just died and gone to heaven!

ISOBEL: Somebody gonna die and go straight to hell . . . (Shakes it off and tries to make the best of things and adopt a southern accent to match) Give me that bowl – you don’t know nothin’ about birthin’ no biscuits! Go over there and start the chicken!

DOLLY: (Mimes preparing chicken and hums or sings “Shortnin Bread” [see link to this song at the end of the selection] while ISOBEL continues)

ISOBEL: Now it is true that I make the lightest, fluffiest buttermilk biscuits you’ve ever tried. It’s a mighty sticky dough, so make sure you remove valuable jewelry before you start. (Isobel takes off her watch and her heirloom ring and puts the to the side) Now. You just take a half cup of shortening . . . cut into tiny little bits . . . and rub it well into the flour mixture . . . adding a cup of buttermilk . . . until you have a sticky mass of dough . . . (to Dolly) Will you please shut up!!!!!

DOLLY: (continuing with her chicken preparations) Well! Wait ‘til I tell Rhett about this!

ISOBEL: Frankly, my dear, I don’t give a damn!!

DOLLY: Well, I nevah! I’ll thank you to keep a civil tongue in your head and get back to your biscuits, Mammy!

ISOBEL: To hell with the biscuits! I am not your Mammy and I refuse to continue this ridiculous charade! I did not study at the Cordon Blue for four years just to end up on a tacky show, wearing an offensive costume and being made a fool of by some overstuffed Atlanta bell!

DOLLY: (Whisking her marinade) Who are you calling overstuffed?

ISOBEL: Honey, we could fill you with helium and rename you Zeppelin! (Pg 45-47) (notices they are still on air and becomes instantly cheery again) Oh! Is it viewer mail time already?

DOLLY: Time goes to quickly on the show, doesn’t it. Alright! Let’s check our cauldron for viewer mail.

ISOBEL: Hubble bubble, snow and hail Show us lots of witchy mail!

DOLLY: Toil and trouble, hail and snow, Tell us what you want to know!

ISOBEL: One, two . . . three! (They each pull out a letter)

DOLLY: Would you like to go first, Izzy dear?

ISOBEL: No, dear – after you.

DOLLY: All right. This is a letter from Lucy. She writes

ISOBEL (as Lucy): Dear Kitchen Witches, you have so many interesting recipes – are there any plans for a cookbook? Yours witchily, Lucy M.

DOLLY: Lucy, we have wonderful news for you. We have just signed on with Edibles Publishing. The Kitchen Witches Cookbook is going to be available everywhere by Thanksgiving! (Dolly suddenly winces in pain and holds her stomach – She passes gas loudly)

ISOBEL: (embarrassed) What’s the matter with you? We can discuss the cookbook later.

DOLLY: You bet your ass. . . paragus we will. I just had too much prime rib last night . . . my tummy’s a little unsettled . . . (another great poof of air)

ISOBEL: Great (panning for the camera) I’m working with Emeril LeGassy.

DOLLY: It’ll pass in a minute.

ISOBEL: ell don’t pass it over here! (Dolly continues to struggle and pass gas loudly) Don’t get too close. The woman is powered by methane.

DOLLY: This is all your fault!

ISOBEL: My fault? Nonsense! If you didn’t snack constantly, you wouldn’t have all these digestive upsets! (Pans to the camera again) (Pg 31) It’s hard to soar like an eagle when you work with a turkey.

DOLLY: (escalating quickly – she goes nose-to-nose with Isobel) Who are you calling a turkey, you scrawny-necked buzzard?

ISOBEL: (Pg 39) Why don’t you go take a flying f . . . idle dee-dee! (then realizes they are still on air) (Pg 41) It’s time we admitted that his was a bad idea from the beginning! We were fools to think it could ever work. Sorry to disappoint you folks, but this show has just been cancelled! (Isobel storms off stage)

DOLLY: (Passes gas loudly – an ending exclamation point)
```

---

## IC-1266: Lerlene Escapes the Bubbas from Alter Egos

- Title: Lerlene Escapes the Bubbas from Alter Egos
- Author (byline): John McGovern
- Work: Best Student One Acts: Volume 4
- Publisher: Dramatic Publishing
- Publication date as stated: 2000
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: LERLENE
- Teaser before the introduction: No
- Spoken words (computed): 1009
- Already set (do not supply): none

### Source block (context only)

```text
Author: John McGovern
Book: Best Student One Acts: Volume 4
ISBN: 978-0871299123
Publisher: Dramatic Publishing
Date (Month/Year): 2000
```

### Introduction (context only: never use it for content warnings)

```text
You know you’re “trailer trash” when . . . 1) The Halloween pumpkin on your porch has more teeth than your boyfriend. 2) You wonder how service stations keep their restroom so clean. 3) You have to go outside to get something from the fridge or 4) Your name is Lerlene and you just escaped from the Bubbas.

Lerlene Escapes the Bubbas from Alter Egos by John McGovern.
```

### Performance text (classify this)

```text
LERLENE: Ohmigod! I just had this – epiphany – I think that’s the word – it was like a flash of just knowin’ – I had to get out! So, I just ran out of my trailer fast as I could – I only took my Merry-Go-Round handbag and my two little dogs. I had to get out! The Bubbas were drivin’ me crazy! When I say the Bubbas I mean my boyfriend Bubba and his two kids. (Pause as the emotion builds inside of her.)

Bubba (On the pouty verge of tears) and Bubba – the man named his two sons the same thing – which woulda been fine if they hadn’t been twins! Oh those kids! Always wantin’ somethin’ – attention . . . Food! Water! I can’t be bothered with that – especially not durin’ my soap-opera slash talk-show hours! First of all . . .

(Her voice moves into her seductive range) I’m gonna be an actress. So soap operas are like crucial actin’ lessons for me . . .

(A sudden switch back to the loud Lerlene we’ve met before) . . . and second, I need to see the talk shows ‘cause sometimes that’s the only way I get to see my family! I mean, last week I missed my cousins BaSita and FaNita on Jerry Springer! Anyway, the main reason I left is . . . ‘cause . . . well . . .

(Does a Wonder Woman-style twirl) I’m gon’ be famous! . . . a supermodel/ singer/actress – triple threat! And I need to be in a situation with a man who is going to support me in my career! ‘Cause I’m on my way . . . I’m in training, I practice like, um, runway walkin’ here in the trailer park . . . it’s like . . . watch . . .

(Runs upstage and strikes her starting pose, then begins to walk) One-two-work it one-two and look and look and look and look. . . I do Vogue covers, it’s like . . . chick chick (She poses)

Chick chick (Another awful pose halfway between a cheerleading pose and a porno still.)

I’m ready . . . ready to be . . . discovered. (She throws one hand in the air in a glamourous pose, but then breaks down.)

But Bubba, Bubba and Bubba didn’t want to let me go! Old Bubba just wanted us to get married and for me to get fat and pregnant! Now first of all, if I’m gonna be a supermodel I can’t be fat, I gotta make sure to stay thin. I sometimes eat nuthin’ but Slim Fast for days – fried Slim Fast, Slim Fast fricassee, baked Slim Fast, Slim Fast ice cream, Slim Fast muffins – you know, ‘cause I know that Naomi Campbell don’t have no cellulite so I better not neither! (Slaps her butt)

I work out too! I don’t have ‘nuff money to join no gym so I do my workout anywhere I can. I love doing that Stairmaster but I can’t get on them big-ass machines, so I just do the low-cost Stairmaster. I go to a really tall building and I just run up and down the stairs . . . (Starts feigning her workout) . . . till I’ve burned at least a thousand calories and then I just drop! (Falls dramatically to the ground.)

Then I just hope that some cute businessman or security guard will call me an ambulance, ‘cause then I get a free ride home! I’ve done other stuff too – I’ve made one o’ them, um, ab-isolators, you know? Outta a wire hanger and two tin cans. I been ingenious ‘bout it! I should be one of those girls on TV. I should be one o’ them Spice Girls! We need some American Spice! I could be . . . Southern Spice! Or Kentucky Fried Spice! I could do that! I should be selling stuff on TV. That’s what I should be doing! I could be one o’ them girls on those infomercials! Like, um . . .

(Runs to one side of the stage and mimes a very sexual selling technique rubbing the appliance) Buy this . . . .

(Runs to the other side and repeats it in an even “hussier” manner) Buy THIS! But . . . I gotta get me a better wardrobe! I been stealin’ all I can --- hence my Merry-Go-Round handbag. But I can’t do it no more – ‘cause I got myself caught last time I was at . . . Contempo Casuals . . . and they had this 89.95 leather skirt and I tried to like crush it up in my purse, just, you know, squish it down in there . . . (Pause) . . . they weren’t amused . . . the cops came and got me – the fuzz . . . and they just threw me up against the wall and frisked me, I felt just like Miss Alyssa Milano in a bad movie of the week . . . I just wouldn’t know what to do if I got caught again . . . Now . . . what I need is for a good man ta buy me thangs ‘n’ make me famous . . .

(To someone in the audience) Go ahead – call me a gold digger, I don’t care!! Hell, gold is in this season! (She sashays to the other side of the stage and cozies up to a different audience member) Actually, right now I’m just a digger . . . (Back to the other person) . . . but when I hit the gold I know you’ll be jealous, girl! Right now I’m livin’ off the tiny paychecks I get from the lottery – no I didn’t win nuthin’, I wish – I’m the girl who picks up the numbers and says ‘em to the camera. (Miming what she does on the show in a sexually charged, slow and sensual manner.)

Like “One . . . Fifteen” . . . See, it’s a good job because it really fulfills part of my triple-threat training: supermodel – ‘cause I’m modeling the numbers, actress – ‘cause I gotta act like I care who wins if it ain’t me and singer – ‘cause, well, I hum tunes to maself when I get bored on the set. But I need somethin’ better than that! So that’s why I left. I mean Bubba means well, he makes a great tuna salad sandwich and he can play Janet Jackson songs doin’ that underarm fart thing. But I need a more upwardly mobile-supportive environment. I can’t settle! And I’m not gonna take care o’ no kids till I’m ready! So that’s why after my epiphany! I just know it’s time to get outta here. So I’m goin’ down to the Motel 6 and I’m gon’ stay there until I can get enough money to go to Hollywood. And I’m changin’ my name too . . . To Lerlene Famoos. . . see, you pronounce it Famoos but you spell it F-a-m-o-u-s so when you write it you see Lerlene FAMOUS! You know what else I did? I got me the same motivational book as Demi Moore says she had! She said it was the key to her success. I mean . . . I didn’t read it yet, but . . . I put it in the corner of my trailer and the vibes it gives off make me feel stronger! I know if I focus, am really nice to people and get the right pair of shoes – I’m gonna make it. I just gotta be famous!
```

---

## IC-1267: Live and in Color

- Title: Live and in Color
- Author (byline): Danitra Vance
- Work: Moon Marked and Touched by Sun (ed Sydne Mahone)
- Publisher: Theatre Communications Group
- Publication date as stated: Feb 1994
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: WOMAN GUEST, HOST, VOICE OF THE DIRECTOR
- Teaser before the introduction: No
- Spoken words (computed): 1574
- Already set (do not supply): none

### Source block (context only)

```text
Author: Danitra Vance
Book: Moon Marked and Touched by Sun (ed Sydne Mahone)
ISBN: 978-1559360654
Publisher: Theatre Communications Group
Date (Month/Year): Feb 1994
```

### Introduction (context only: never use it for content warnings)

```text
Danitra Vance was an American comedienne and actress best known as a cast member on the NBC sketch show Saturday Night Live. Diagnosed with breast cancer in 1990, Vance underwent a single mastectomy. The cancer recurred in 1993 and she died of the disease the following year. In Live and in Color we get to experience her unique form of humor as she address some very serious topics: PMS and it’s impact on women, AIDS and the very cancer that ultimately killed this very talented performer. Live and in Color by Danitra Vance.
```

### Performance text (classify this)

```text
Sometimes I wake up screaming. Sometimes I believe I'm clinically depressed. Maybe my show is on. (She turns on the TV using the remote control) Naaaa. (She turns off the TV with the remote. She picks up the Singleton Maxwell notebook and reads) Singleton Maxwell M.D./Midol Junkie This message is for women only because men really don't have a clue, do they. Adam was not a rough draft, Adam was a doodle. Ladies, I am Singleton Maxwell M.D., the woman gynecologist that designed the O.B. Method. I am currently on a lecture tour, with a presentation entitled WARNING: THE DANGER OF BEING A WOMAN. I have spoken before many prestigious groups including most recently a joint meeting of the League of Women Intellectuals and the Sluts Against Smut. I became a gynecologist because of my gynecological mysteries.

Our combined gynecological mysteries prompted me to write a pamphlet (Shows cover) Between Your Legs and You. You can pick it up almost anywhere. In the book, I postulate: "Is there a Capitalist plot against women?" I mean to say ... Why is it that whenever I have monthly pain the first thing I think of is, Give me strength, give me antiprostaglandins, give me antispasmodics, give me drugs.

(She puts on her sunglasses. Traditional blues music underscores the following monologue. She
sings:)
In the kitchen barefoot expecting my eighth child I must take my Midol, so I don't
go wild
I'm a Midol junkie and I don't know why
Keeps me feeling funky so I take it all the time
It helps before, during and after
Gives me laughter through my tears
I've been on it for years
It helps my lower back pain
Takes away the strain of being a Woman Woman Woman WOMAN, WO-O-O-M-A-
A-A-N
Yes I'm a Woman W-O ... W-O (Forgets lyrics) Yes I'm a Woman W-O (Still can't
remember)

(Spoken) Baby, you don't know me. I killed my first husband. It wasn't really my fault, though. It all happened the night before my *monthly* was supposed to start and I am sure it was the hormonal imbalance that led me to commit murder. "Did I have to kill him?" "Did I have to kill him?" "Did I have to kill him?" Yes, I had to kill him. He hit me, and I always told myself I would never stay with anybody who hit me. While I packed, the scenario unfolded. I leave him, he finds me, he looks pitiful and boyish, I forgive him, we spend six blissful months together. He hits me again, harder, then he says, "I'm sorry, Baby, I love you more than life itself, doesn't six months of bliss mean anything to you?" He cries, I cry, a year of happiness until he loses his job, bam bam bam, he buys me a puppy, a cute little black springer spaniel, he kicks the dog ... I'm living the life of the battered wife. I watch Oprah and Phil and Sally and Shirley and Jane and Wilma and Betty and Veronica ... I started to wonder who would play me in the made-for-TV version of my life. My lawyer said for me to plead insanity, and I said I thought that was just for men. I went to prison.

(Singing:)
W-O ... W-O ... Oh you know,
Oh you know, o. u. know, all of you know. I may not be able to spell my name
but Midol keeps me tame
when I'm feeling evil.
(Spoken) Take only as directed.

TRANSITION Today there is more feeling than ever that television is cheapening the news and that the audience is allowing this to happen and even encouraging it by giving high ratings to so-called trash television--tabloid news programs and sensationalistic talk programs. We interrupt this life to take you “LIVE AND IN COLOR” -- the very type of reality television show – The American Talk show – that dominates the lives a millions of stay-at-home mothers throughout the nation.

Television Talk Show

WOMAN GUEST: When I got to LAX, there was no one there to meet me, so I took the shuttle. By the time I got off at Phil and Chris's, a guy there told me Chris had to go to the emergency room and when they came home, Chris went to bed. Phil told me that Chris had AIDS and that he, Phil, was HlV positive. I thought to myself, it's a good thing I am who I am or this could be ... not too cute. I didn't know a lot about AIDS. I shook hands with a person with AIDS before 1 knew what it was. What I'm saying is I never lived with someone with AIDS. I never lived with someone HIV positive and I was afraid. I was afraid I'd turn stupid. Part of me thought I might throw up my hands and run screaming from the house. I mean part of me wanted to want to do that. That was a few years ago and AIDS was in the paper and on the news every day and everyone seemed to be a little hysterical. I guess I'm not a hysterical person.

HOST: You say you're not a hysterical person. If there was a time for hysteria, it would have been then. Had you seen something or read something that-

WOMAN GUEST: I had seen you on your talk show.

HOST: You know, I always like to think this show performs a public service, that it enlightens and educates-

WOMAN GUEST: No. You had a PWA on your show and the entire audience hated him. And you never touched him. You didn't shake his hand. You even sat in a chair or two away from him and stretched your microphone over to him. You could have taught this country to be humane but you seemed to side with ignorance. Even your expert doctor said he couldn't guarantee these were the only ways to get the virus. I knew I didn't want to be like you.

HOST: You seem to ... You've given us so much ... Let's go to a commercial right now. (Camera is turned off.) I don't know who you think you are, but this is my show. How dare you get up on national television and humiliate me!

WOMAN GUEST: How dare you get up on national television and dehumanize every person with AIDS. Where was all that compassion and intelligence you talk-show hosts are supposed to have?

HOST: Let me tell you something, Miss Holier Than Me, I am famous for my compassion, my sympathy, my empathy, my Ph.D. People magazine named me one of this year's "Most Fabulous People" because of my warmth and compassion.

WOMAN GUEST: I used to feel the same way until I saw that show.

HOST: We're coming back from commercial in about one minute and I want you to tell the viewing audience you saw that on someone else's show. Tell them I didn't do that.

WOMAN GUEST: Honey, when you come back from commercial, you won't have a guest to talk to. I didn't come here for this.

HOST: Oh! Believe me, I can run this show without you or any other guest. But let's see how you run the show without me. (Walks off the set)

WOMAN GUEST (To audience): How many of you saw that show? It was a few years ago. (No response) If the host doesn't come back, will some of you go to the microphones and ask me questions about living with someone who has AIDS or-

VOICE OF THE DIRECTOR: We're back!

(Woman Guest looks blank, clueless, lonely. She looks toward the wings for the Host. She looks toward the audience. "Help" is written in her eyes. If an audience member gets up, we'll take the question. If not .. .) You're turning stupid

WOMAN GUEST: I didn't want to turn stupid. I gave Phil a big real hug. Not a cheek-to-cheek, hand-on-the-shoulders hug, a real hug. And I hugged Chris the same way. But stupidity always lurked somewhere. (Screams) The toilet seat! I always put tissue on the seat. That's how my grandmother raised me. Maybe I should sit on the bare seat to prove I wasn't afraid of AIDS. Prove to who? (Screams) The shower! I can't get it from taking a shower. EEK! The razors! I don't use other people's razors anyway. Dishes! Couldn't I be the first, the very first person to contract AIDS in some odd, unusual way? I mean, doctors and nurses in hospitals wear gloves and masks and stuff. Yes! No! Maybe. Yes! No! Stop it! I wasn't having sex with them. I had never had a blood transfusion. I was not an IV drug user. If there was some other way for me to get AIDS, some other way no one knew about, then okay. I would be an innocent victim just like Phil and Chris and everyone fighting this syndrome or that disease or any other malady.

Not long after that, I found this lump in my breast. I had a mastectomy. Then I started this book. All proceeds go to the National Fund for Sick People. Funny Things People Say to People That Are Sick:

"I thought you were dead." "Why don't you have the other one removed?" "How are you?" You can ask me questions now. (Questions from audience. Pause.)

Oh, okay, nobody wants to talk to me. I can see some of you are wearing red ribbons. Big deal. What difference does that make? Go hold a crack baby. Go hold an AIDS baby. You want a medal for that? If that ribbon was made out of ten pounds of steel that you had to sling over your shoulder, that might say something. "Count me, too. I'm struggling, too." Fifty thousand women die every year of breast cancer. Wear a ten-pound ribbon for them and one for lupus and one for diabetes and every other life-threatening, life-altering- Since this is a talk show, and since this is my talk show. That's all I have to say.
```

---

## IC-1268: Lives of the Great Waitresses

- Title: Lives of the Great Waitresses
- Author (byline): Nina Shengold
- Work: Plays for Actresses
- Publisher: Vintage
- Publication date as stated: March 1997
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: KAY, TAMMIE SUE, YETTA, MELISSA
- Teaser before the introduction: Yes
- Spoken words (computed): 1451
- Already set (do not supply): none

### Source block (context only)

```text
Author: Nina Shengold
Book: Plays for Actresses
ISBN: 978-0679772811
Publisher: Vintage
Date (Month/Year): March 1997
```

### Introduction (context only: never use it for content warnings)

```text
Being a great waitress is a real accomplishment. There is a huge difference between a good and a "GREAT" waitress. I have seen and worked with many good waitresses over the years, but I've only run into a few great ones. There are many little techniques that veteran waitresses learn that improve their efficiency, get them larger gratuities, and elevate them to the top of the heap. However, there seems to be a large mental shift that a waitress must make before she can truly be a great waitress. Well, actually, I know of some people who can show you what I mean much better than I can tell you. Let me introduce you to Kay, Tammie Sue, Yetta and Melissa from Lives of the Great Waitresses by Nina Shengold
```

### Performance text (classify this)

```text
YETTA, KAY, TAMMIE SUE, prepping the breakfast shift. All in pink uniforms.

KAY: You either got it, or you don't. If you don't, you won't ever. So don't even bother. Don't strain. Oh, there's things you can learn, sure. The fine points. The stance. "Heat that up for you?" "Toasted?" But honey-scratch that, make it hon-a truly great waitress is born. You get what I mean? It's a feel thing. Deep under the bones of your bones. In your cells. Some reporter once asked Louis Armstrong what "swing" meant. Louis looked the guy dead in the eyeball and said, "If you gotta ask, you'll never know." He would've made a great waitress. My very first diner, we had one. Flo Kelly. A goddess in Supp-hose. Flo was all waitress. She could fill two dozen shakers one-handed and never spill one grain of salt. She could carry eight Hungry Man specials lined up on her arm like a charm bracelet. Flo could serve pie a la mode so it looked like Mount Everest topping the clouds. She poured gravy like tropical rain. In Flo's maraschino-nailed fingers, the short-order carousel spun like the Wheel of Fortune, and never, not once, did a customer's coffee get cold. Well, I mean to tell you, that diner was hers. If Jesus Himself Amen came in and sat down to supper, he would've tipped double. Then one Blue-Plate Special, right after the lunch rush, Flo hung up her hairnet, cashed in her checks, and went sunny-side up. And that's when the Lord took my order. I knew what I was. I was called. (She steps closer.) Look in my eyes. I know mysteries way beyond menus. I have felt the Lord's love pierce my heart like a skewer through gyros. I have seen Jesus weep ice-kold milk with a K. (She holds out her hand.) Heat that up for you? Han?

(BLACKOUT. LIGHTS UP on TAMMIE SUE, filling up sugar shakers. Forties, dithery, slight Southern twang

TAMMIE SUE: SO this fella sits down at my counter. Scrawny, beat, banty thing, ugly as yesterday's homefries, and he's got the look. You all know that look. (She demonstrates.) There's this puppy dog whimpering back of his eyes, means he's looking for more than two eggs on a raft, wreck 'em, cuppa joe light. So I do what a girl's gotta do. I ignore him. No warmups, no sass, save my smile for the grandpas and wedding rings in the next booth. Comes the end of my shift, and this shriveled-up walnut, this cottage cheese curd, this crust of burnt toast is still sitting there. Dog in his eyes rolls right over and begs. So I give him the deep-freeze. I shoot him a look that would flatten meringue. (She demonstrates.)

And what's he do? Smiles at me. Smiles. Gatty teeth, great big space in the middle, looked just like a little ole kid with skinned knees on the playground. Well, hell. That did melt me up. Kay's always telling me I got a heart as big as a Butterball turkey, and besides it's been way, way too long since my griddle got greased. So we go to the motor home up top his semi. Well. I tell you that man had a mouth that could melt you like butter and syrup on top of a short stack of buckwheats. He did things with his fingers that should be illegal, or fattening. That little runt had him a secret self under his outfit. We've all of us got one, but this was a secret worth spreading around. And he did. He most certainly did. He could love you up one side and back down the other and still leave the middle part gasping for more. That man had a gift. Mashed potatoes and gravy. I left him a tip, that's the God's honest truth. So the next time you find yourself checking out someone's dessert case, remember, it isn't the Dream Whip that counts. It's the peach in the pie.

(She pours sugar straight into her hand, sticks her tongue in it. BLACKOUT. LIGHTS BACK UP on YETTA, drying her feet and pulling on flesh colored knee-highs and nurse's shoes.)

YETTA: We got us a new one today. Little blondie thing. Brains like a dishrag. Marty says to me, Yetta, give her a try. What try. Way she walks into the room I can tell you the broad ain't no waitress. She's got this two hundred and ninety pound bag slung over her shoulder, you just know that it's gonna be full of her face eight by ten. You know that she's gonna be hocking the customers, "Hi! I'm-"

(MELISSA, twenty, walks on with a musical comedy smile. Brand new uniform.)

MELISSA: (Overlapping.)-I'm Melissa. Our specials tonight are a light cappellini with sauce Margherita-

YETTA: Spaghetti and meatballs.

MELISSA: -a baked beef and pork terrine,

YETTA: Meatloaf

MELISSA: -and I want to thank my parents, my agent, and God for believing in me.

YETTA: A question. Does anyone care what's the name of the person who's pouring your coffee cup? Thank you.

MELISSA: Gemini. Capricorn rising.

YETTA: My breakfast is rising.

MELISSA: "The quality of mercy is not strained." (Bright smile, starts to sing) "Brigadoon, Brigadooooonn ... "

YETTA: Am I right or right? Hopeless. First lunch rush, her head'll be spinning around like the milkshake machine. But she bats her big blues up at Marty and tells him yes, she's got experience. Marty, being A) dense and B) male, does not ask her what kind. So it's up to yours truly to break the kid in. Never mind I got migraines in both of my feet. Tammie Sue knows her ass from her elbow on good days, and Kay's gonna try to convert her. Born once, she can just about handle, forget born again. So I give her the counter, okay? Let her piss off the regulars. Marty's there working the register, maybe he'll know from "experience" next time around. Which I bet you good odds is the end of this shift.

(MELISSA takes pad and pencil out of her apron, approaches an imaginary customer on the fourth wall with a big nervous smile.)

MELISSA: Hi. Can I get you some breakfast? Um, coffee? Uh huh ... (She writes on her pad, very slowly and clearly.) Is that "regular" meaning not decaf, or regular with cream and-Right. What? Oh, menus, I'm sorry ... Right back. (She scuttles out. YETTA smirks.)

YETTA: And we're off. And it doesn't get better. Clear through to the lunch rush she's mixing up eggs over easy supposed to be scrambled. She's bringing the Western the wattles. She's dropping forks right, left, and center. The decaf goes dry. Then she loses an order, a party of six, and they walk without paying.

(MELISSA rushes out, breathless.)

MELISSA: I'm sorry it's taking so long, I'm- ... Hello? (She looks towards the exit, near tears.)

YETTA: SO I look over at Marty like, hey, get the hook, because Miss Eight by Ten flunked her audition. And Marty just flashes his not-quite-so-pearlies-the breath on that man, it could kill you-and says, "Listen, everyone'sgotta start somewhere." I'll tell him where I'd like to start. With his head on a plate. A klug of him. I need a cigarette. (She reaches for one. BLACKOUT. LIGHTS UP on MELISSA, untying her apron, alone.)

MELISSA: This is my first day of work. Not here. Ever. My family had money and nobody made me. I came to this city to look for a job and nobody would hire me. It's kind of like being a virgin-I'm not any more, but I was-and I'm telling you, nobody wants to be first. Too much pressure. My roommate said, "Lie." So I did. (She sits.) People think if you haven't done something before, you're an idiot. People can't know what's inside you. You don't know yourself till you're given a chance. Then all of a sudden this new personality starts to swell under your skin, bursting through where you'd never expect it, and nothing you thought you were makes any sense. You're elastic. You're putty. You've been up for hours, making love to a man whose back ripples with muscles you've never felt, feeling your body expand and explode and dissolve into air, into something like stars, and it doesn't seem possible that you could open your eyes to the same old alarm clock and fit in the same pair of shoes. I don't want to lose this. This newness, this urgent, sharp knowledge that everything matters. That being good matters. I want to do everything well. I know, I'm a waitress. It's not what I've dreamed of, what anyone dreams of, but I make a difference. I do. There are lives on each stool at that counter. The old man who's ordered his Sanka and shredded wheat every morning for twenty-five years. (She nods toward someone in the audience.) Otto. The woman who fought with her husband last night and treated herself to French toast with her friend who just had a mastectomy. Velma and Ruth. The man who panhandled the price of his coffee. Muhammed. I touch them. I give them the quiet sensation that once in their sad, uncontrollable lives, they wanted a small thing and got it. I brought it. I bore them a gift. And that matters. (She hangs up her apron, on a transparent hook hanging down from clear fishing line.) You watch me. I'm going to be brilliant. I'm going to be one of the greats.
```

---

## IC-1269: Making Friends with Girls

- Title: Making Friends with Girls
- Author (byline): Jenny Lawson
- Work: Let’s Pretend This Never Happened
- Publisher: Berkley Trade
- Publication date as stated: March 2013
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: JENNY, ME, LAURA, KAREN, EVERYONE, WOMAN 1, WOMAN 2, WOMAN 3, WOMAN 4
- Teaser before the introduction: Yes
- Spoken words (computed): 1966
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jenny Lawson
Book: Let’s Pretend This Never Happened
ISBN: 978-0425261019
Publisher: Berkley Trade
Date (Month/Year): March 2013
```

### Introduction (context only: never use it for content warnings)

```text
Making Friends with Girls by Jenny Lawson
```

### Performance text (classify this)

```text
JENNY: For the majority of my life I lived with a small, terrible secret: I’ve never really liked girls. I realize this is stereotypical and hypocritical, since I am one myself, but to be fair, I probably wouldn’t choose to hang out with myself if given the option.

It’s always been this way. I was too much of an anxious misfit to properly bond with girls when I was young, and I never really got the hang of it. I consoled myself by thinking of how much money I saved on Christmas gifts for friends that I never made. Whenever I hear of women who are still best friends with the girls they went to school with, I always make a mental note to avoid them, because I assume they’re compulsive liars.

Even as an adult I had mostly male friends, and I looked at most girls as judgy, cruel, fickle, and likely to borrow your Cabbage Patch doll and never give it back. Victor always pushed me to find girlfriends, but I’d convinced myself that girls are like small bears: cute to look at, but far too dangerous to have lunch with.

This all changed when I discovered blogging and found other people online who were misanthropic misfits like me.

JENNY: I decided to get out of the house and meet a fellow mom blogger named Laura for lunch, Laura tried to convince me that there were actually interesting and fairly nonjudgmental women who wouldn’t make fun of the fact that I often had to hide under tables when I was overwhelmed. I didn’t believe her, but I took a deep breath and decided to trust her, because if nothing else, this would be the perfect experiment to prove my theory that most grown women are just as dangerous as the kids on the playground who wouldn’t let you play tetherball with them because you didn’t have Wonder Woman Underoos.

Over the next two years, I became tentative friends with the bloggers Laura introduced me to, and I was eventually invited to go to a weekend all-girl retreat in California wine country for a small group of bloggers.

A conversation with my sister two days before the event:

ME: Okay, I just saw the invitation list, and I’m completely freaked about this party. It’s like everyone else there is part of the cheer squad, and I’m that weird girl with the back brace who ate too much glue.

LAURA: You need to stop freaking out about this. It’s going to be super laid-back and casual, and you need to relax and have fun. Just bring a few pairs of jeans and some shirts and you’re set.

ME: I don’t own any jeans.

LAURA: You’re a damn liar.

ME: How many years have you known me? Have you ever seen me wear jeans?

LAURA: Wow. No. There might be something wrong with you.

ME: This is exactly what I’ve been trying to tell you.

JENNY: The day before the event: Karen (a wonderful and sweet blogger whom Laura had introduced me to) found out that I didn’t own jeans, and decided to have a shopping intervention.

KAREN: I can’t believe you don’t wear jeans. Jeans are fabulous, and crazy comfortable. Ooh. See? Those are cute jeans. You should get them.

ME: Mmm. No. My knees look fat in these. You wouldn’t understand, because you’ve always been thin, but when you’re fat your kneecaps get tired of supporting all of your weight, and so when you lock your knees they bend backward. That’s why I always concentrate really hard on always bending slightly at the knee, so that I don’t have fat-girl kneecaps.

KAREN: I love you, but I can’t even tell you how insane you sound right now. Like, most of the time you’re fine, but right now? Totally insane.

ME: You probably just weren’t listening those other times.

JENNY: The first day of the party, on the plane: You know when the captain comes on over the overhead speaker and says, “We’re going to take off in a few minutes, but we’re going to be without air-conditioning for a bit because we don’t have auxiliary power, and we’re having problems with one engine so we’re going to have to get out on the runway before we can get it started”? That’s when you should probably just get off the plane. But I couldn’t, because I was too terrified to move, so instead I just asked the guy next to me whether he thought this was some sort of joke. He didn’t, and told me it was nothing to worry about. “Yeah,” I said, my voice becoming shrill with fear, “but they just said we don’t have both engines working. I’m pretty sure two engines are preferable.”

He rubbed my hand patronizingly and told me I’d be fine, and I assumed he was hitting on me, so I said, “I’m married.” Then he looked at me strangely and said, “Congratulations?” He probably wasn’t hitting on me at all. More likely he just wanted me to shut up. Then the stewardess came on the speaker, and instead of saying, “At this time we ask you to turn off any portable equipment,” she said, “If you’re on a cell phone, tell them good-bye.” And I’m all, “Why did she say ‘Good-bye’ with such an air of finality?” The guy sitting next to me didn’t respond. Probably because he knew we weren’t going to make it out alive.

Amazingly enough, we landed. I was wearing the jeans Karen had persuaded me to buy, and a 1930s-style black hat that I’d hoped screamed, “I’m a bohemian vintage shopper.” Then I realized that there was an orange Target price tag stuck to the back that said “Now $7.48.” Awesome. Plus I was very aware how fat my kneecaps looked in these jeans. I needed to lie down.

Pajama-party time. Except it was cold, and I don’t own pajamas. Everyone was in adorable matching sets with robes. Our hostess, Maggie, was wearing a red silky robe over what looked to be a wedding dress, and she had fluffy slippers on. She looked like she’d just come from Wardrobe. I was wearing a muumuu with sweatpants on underneath, a giant men’s hoodie, and my red confidence wig. I’d started wearing a wig in social situations for several reasons: (1) It makes me feel like someone who isn’t terrified of people, and (2) if I really *mess* something up I can excuse myself, pull off the wig, and say, “Who was that weird redhead. The wig is a form of protection, a sort of talisman, allowing me to pretend that I’m anyone else who isn’t me. Except that I can’t afford an expensive wig, so mostly I just look like I’m pretending to be a cancer patient.

Four a.m. I decided it was late enough in Texas to call [my husband] Victor. But about ten minutes into the call I got attacked by a giant bear. Except not really, but it felt like it. Basically I was on the phone and this big animal walked into the pool area from the forest, and I whispered, “I’M GOING TO BE EATEN BY A COUGAR. Wait, are there cougars in California?” But the animal was edging closer, and although it was dark I could see it didn’t have a tail, so I whispered, “Bobcat! I’m going to be attacked by a bobcat. Or a cougar that lost its tail. Probably because it got gnawed off by a vampire. And now it’s a vampire cougar. But I said all that in my mind, because I was being quiet so that I wouldn’t attract its attention. It looked up, saw me, and then slunk off.

Six a.m.:

ME: OH MY GOD, LAURA, WAKE UP. I totally just got attacked by a cougar! . . . It might have been a bobcat.

LAURA: YOU SAW A BOBCAT?

ME: It was small, though, so probably a baby bobcat. It might have been a house cat. BUT IT WAS ENORMOUS. And it totally looked at me in a threatening way. [to the ten people eating an early breakfast the next morning] Did Laura tell you I got attacked by a bear last night?

EVERYONE: WHAT?

LAURA: She did not get attacked by a bear.

ME: Bear . . . cougar. Same difference.

LAURA: There was no attack. She’s fine.

ME: I think someone should ask the owners how many cougars they keep on the property.

LAURA: I already asked the owners what it could have been, and they said there are some feral cats around.

ME: I’m pretty sure “feral cats” is code for “vampire cougars.” [to everyone else who came to breakfast one hour later] So last night I was attacked by Sasquatch. It was like a smaller version of the Loch Ness monster. But on land. So, yeah. It was pretty terrifying.

JENNY: No one really responded, but it didn’t surprise me, because it’s hard to know what to say in those situations.

That morning I found out that we were all going to wine education class. I felt like I was in some kind of finishing school and I’d missed all the prerequisites.

By my tenth glass of wine I started to wonder whether there was something wrong with my palate. Everyone else was marking the wine list with notes like “Pleasant finish. Robust spices.” Meanwhile, I was doodling pictures of vampiric cougars. Then I noticed people staring at my doodles, and so I started writing notes next to the wine. Things like “Tastes of NyQuil, but in a good way,” and “I can’t feel my feet anymore.” “Did I leave the garage door open? I wonder whether the cat is on fire. I should probably stop drinking now.” Everyone else there had a sophisticated palate. I had one that needed therapy, and possibly an intervention.

The final morning we all sat around by the pool, wrapped in blankets with mussed hair and no makeup, and I listened to the conversations around me the same way I had in high school, but instead of trying to block them out or sneer at them internally, I smiled and nodded. I forced myself to join in and listen to all the conversations going on around me, rather than hide my head in a book to avoid rejection. And I realized just how awesome girl conversations could be. Random snippets of overheard conversations:

WOMAN 1: “You know when you’re in Nepal and there are all these Japanese people around and it’s two a.m. and you’re in a basement and you’re trying to find breakfast and suddenly a magician shows up?”

WOMAN 2: “Oh, I know exactly what you’re talking about.”

WOMAN 3: “My dad had anger problems, so his doctor recommended he go to mime school to learn how to deal quietly with his emotions. It wasn’t until I grew up that I realized that everyone doesn’t have this memory of taking mime classes with their angry dad.”

WOMAN 4: “I don’t like mimes. I don’t like the fact that they fake a disability.”

WOMAN 3: “Right? Why stop at mimicking the mute? Where are the clowns pretending to have polio?”

JENNY: The final hour: As we all dragged our luggage out to the waiting vans, I looked with a surprising amount of affection on these women who only days ago I would have immediately dismissed as being snobby or mean, but who all turned out to have backstories and struggles just as damaged or bizarre as my own.

I was leaving behind my assumptions that only snobby, rich people liked wine, and that everyone would immediately break into cliques based on who had owned the right kind of underwear. And most important, I was leaving behind the idea I’d been carrying around for years that girls were not to be trusted. Women were great and relatively harmless. It’s the four a.m. vampire cougars in the woods you really need to be worried about.
```

---

## IC-1270: Malfeasance

- Title: Malfeasance
- Author (byline): James Canon
- Work: Malfeasance
- Publisher: SpeechGeek
- Publication date as stated: 2015
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1627
- Already set (do not supply): none

### Source block (context only)

```text
Malfeasance by James Canon
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
Author’s note: The 3 fairies may be combined into two or one fairy, depending on the performer’s preference.

MALEFICENT. (rehearsing) Listen up! No, too informal… You fools! Listen to me

while I curse your baby… No, too rhyme-y… Hey, listen to this!...

Too cheerful. DIAVAL. (as a crow) Caw! Caw! MALEFICENT. Oh, thank evilness! Diaval… Into a man. (casts a spell and turns

crow into a man) DIAVAL. Ugh, my lady. I know you can transform me into anything—a dog,

a dragon…there was that awkward toothbrush incident—but I am

a crow and I wish you would just let me be.
MALEFICENT. Oh, stop whining and help me.
DIAVAL. Working on the curse for the princess’ party.
MALEFICENT. Yes. What to do? What to do? I could steal her voice, give her

boils, ruin her finances, give her “front butt”… DIAVAL. Well…sounds like you’ve got a lot of ideas. Why don’t you just,

you know, give from the heart? Just go with the evil flow. MALEFICENT. Hmmm…very good. (spell) Into a writing desk. DIAVAL. What? No! I— (changes) MALEFICENT. Hahahaha. I know why a raven is like a writing desk. DIAVAL. (as a desk) I’m a crow!

TRANSITION
FAIRY 1. Happy birthday Princess!
FAIRY 2. Happy birthday to the princess!
FAIRY 1. Happy birthday to…who?
KING. Happy birthday to my daughter! My people, I have been a great

king for you. PEASANT. Actually, sir— KING. Death! But seriously, you’re lucky to have me. Now then, who

brought presents for my daughter?
OLD MAN. I have brought her a frock made of gold… It’s heavy.
CHILD. I’ll play my drums for her ba rump ba bum bum.
KING. Yes, yes, all very good… What? What’s going on? Who brought

all this thunder and smoke?
MALEFICENT. Now listen well, ye foolish fooly fools!
DIAVAL. Overdid it.
MALEFICENT. Dang it. Nevertheless! I am Maleficent, and I am here to curse

your beloved princess. She will have beauty and she will have

riches…
KING. This sounds like one heck of a curse.
MALEFICENT. BUT!
KING. Spoke too soon.
MALEFICENT. On the eve of her eighteenth birthday she will…prick her finger

on a spinning wheel! KING. No! Wait, what? MALEFICENT. Yes, it will sting worse than a papercut. It will itch more than a

bug bite. It will bleed slightly less than an actual cut.

DIAVAL. …and then?
MALEFICENT. And then? Oh, and then…she will fall asleep… Forever!
KING. No! That’s a long time!
MALEFICENT. And nothing can save her except for true love’s kiss, because

that’s not real! Muahahaha-boohoohoo! (laughter turns into tears) DIAVAL. Maleficent? MALEFICENT. Oh, sorry. Too real. Now then, I have spoken and so it shall be! KING. Death! Seize her and give her death! DIAVAL. Time to go. MALEFICENT. Yes. Ok, Diaval, into a getaway! (He transforms and she buzzes

away.) KING. Dang it! Fairies! Surely you can do something! FAIRY 1. We can take her to the forest. Raise her far away from all

spinning wheels. FAIRY 2. We’ll return her on the day after her eighteenth birthday. Then

she will have defied the curse, and she’ll be safe. FAIRY 3. And we’ll be old! FAIRY 1. She will not know of the curse or her true identity. We’ll tell her

on her eighteenth birthday. KING. That’ll be one big birthday surprise. All right, that’s the plan. In

the meantime, we shall hunt Malefaction.
FAIRY 1. Maleficent.
KING. Malignancy?
FAIRY 2. Maleficent.
KING. Malnutrition?
FAIRY 1. Close enough.

TRANSITION
DIAVAL. (as a crow) Caw! Caw!
MALEFICENT. (spell) Into a narrator!
DIAVAL. (transforms to a narrator) And so seventeen years passed with the

King hunting Maleficent and the princess blossoming under the

watchful eyes of the fairies. However, the princess and

Maleficent’s path were soon to cross again, on the eve of Aurora’s

eighteenth birthday... AURORA. (singing) LA LA LA LA-A-A-A-A! MALEFICENT. Ahh! What is that awful joyous noise? It offends my ears. It

scorches my soul. It chafes my unmentionables!
AURORA. Oh, hello! I was just singing to the trees and rocks.
MALEFICENT. You were…what?
AURORA. You see: the trees and the rocks are my only friends. I had a

squirrel friend once, but well, he was nuts. MALEFICENT. Who and what are you? AURORA. My name is Princess Aurora. It’s a strange name for a peasant girl

being raised by three winged aunts in the dead of the forest, but

there you have it. MALEFICENT. Princess (hisses…then tries to cover it up with a cough) how lovely

to meet you.

AURORA. And you as well! What an incredible day I’ve had: meeting two
new friends.
MALEFICENT. Two? Who was the other?
AURORA. A prince!
MALEFICENT. A prince? This cannot be. (casts a spell at AURORA)
Go…unconscious.
AURORA. Why that’s a silly thing to—(unconscious)
MALEFICENT. Diaval?!
DIAVAL. Maleficent was furious, for she knew that princes had a nasty

habit of breaking curses and—
MALEFICENT. What are you doing?
DIAVAL. She had forgotten that she had turned the handsome little crow
into a narrator.
MALEFICENT. Stop it.
DIAVAL. But he was unable.
MALEFICENT. I said stop it!
DIAVAL. And still, he was unable.
MALEFICENT. Ugh! Into a chair.
DIAVAL. Oh no, he thought— (into a chair)
MALEFICENT. (sits down) What am I going to do? If she meets that no good

prince, all my plans are ruined. Why do these things always

happen to me!?
AURORA. (wakes) Oh dear, why are you crying?
MALEFICENT. Oh great, now you’re awake. Ugh, my magic never goes right.
AURORA. Did you say magic?
MALEFICENT. Yes, I said magic. What, have you gone deaf and dumb? Have

you gone and hit your head on one of your little rock friends? AURORA. Why then you must be my fairy godmother! MALEFICENT. (mimics) Well then you must be my fairy god—what? AURORA. It’s true. Finally, a fairy godmother of my very own. I knew

someday I’d meet you and you could guide me to true happiness. MALEFICENT. True happiness? AURORA. Yes. Like which dresses to where and what apples are poisoned

and who my true love is. Oh you will help me, won’t you? MALEFICENT. (to herself) Fairy Godmother? I can work with that. (to AURORA)

Ah, yes my dear. That’s exactly what I am. But I’m your secret

Fairy Godmother. My magic only works as long as you keep me

an absolute secret. AURORA. Don’t worry, I won’t tell the rocks or the trees. MALEFICENT. Now then, I have a gift for you. (conjures) It’s a spinning wheel…

Mu ah ah ah ah! AURORA. What’s so funny? MALEFICENT. What? Nothing. No, I was just thinking of this one time I conned

an idiot into certain death. Come now, come now. You trust your

dear sweet wonderful Fairy Godmother, don’t you?
AURORA. Well, the spinning wheel is lovely. How does it work?
MALEFICENT. Simple, you hold out your hand.
AURORA. Alright.
MALEFICENT. That’s it. Perfect. Right there. (stabs her) Ha!

AURORA. Oh dear. MALEFICENT. Victory! And once we dispatch her true love, little sleeping

beauty here will never awaken! Come, Diaval, we’ve got a prince

to find.

TRANSITION
FAIRY 1. Aurora!?
FAIRY 2. Aurora?
FAIRY 3. Borealis!
FAIRY 1. Where on earth could she be? (trips over her) OOF!
FAIRY 3. Hey, someone left their princess just laying around.
FAIRY 1. Oh, no! It’s Aurora. She’s pricked her finger, and now she’s
asleep.
FAIRY 2. Now she’ll sleep forever.
FAIRY 2. What about true love?
FAIRY 3. I love that show. Vampire Bill is my favorite.
FAIRY 1. You’re an idiot. We must go and fetch the king!
FAIRY 2. What about her?
FAIRY 3. She’s not going anywhere.

TRANSITION
PRINCE. Princess Aurora? Princess Aurora?
MALEFICENT. Looking for someone?
PRINCE. No. I just go around singing her name. Who are you?
MALEFICENT. I’m her fairy godmother. Mal-er-uh, Magnificent
PRINCE. Really? Well, it’s nice to meet you Malera Magnificent. My name

is Prince Phillip. MALEFICENT. Isn’t it pronounced “Phillip?” PRINCE. No, it’s more phonetic. Phillip. Yes, I was just on my way to the

castle where I am to wed the daughter of the king. But then, oh, I

met a beautiful country girl named Princess Aurora. And now my

heart is split in two between the duty to marry the king’s

daughter and desire to marry Princess. MALEFICENT. …you do know what the word Princess means, don’t you? PRINCE. Why yes, of course…oh! Oh! Oh! She’s a princess! I can marry

her! MALEFICENT. Ha! Not so fast ye foolish fool hearted fool. For you have been

fooled by my foolproof plan!
DIAVAL. Overdid it.
MALEFICENT. Dang it!
PRINCE. Wait…so you’re not Princess Aurora’s fairy godmother?
MALEFICENT. No, I am…
KING. Malemuit!
MALEFICENT. No, it’s…
KING. Mellifluence!
MALEFICENT. MALEFICENT. Mal-ef-i-cent. You’ve had 18 years to practice.

How hard is it really? PRINCE. Fear not, my king. For I will dispense with this fiendish friendly

fiend. I will fiend it within myself to Fien-nish this.

KING. Overdid it.
PRINCE. Dang it.
MALEFICENT. Bring it on, lover boy.
PRINCE. Oh, crap.
KING. Great. While you were having a soliloquy she turned into a
dragon!
MALEFICENT. I don’t mean to be a drag, but drag–gone it feels good to let loose

my fiery side. Hahahahaha…cough cough…heart burn. PRINCE. This one’s for Princess Aurora! Ha! (sword gets batted away) MALEFICENT. Nothing can stop me! (gets hit) I am… (gets hit again) What the devil? PRINCE. Fly Princess Aurora’s friends! Avenge her! (throws a rock) MALEFICENT. You’ve got to be kidding me. Ow. Ow, stop that! PRINCE. And you, too, trees! (uses a tree as a weapon) MALEFICENT. Ow! Come on! Fine! (breathes fire on everything) KING. Ah! Fire. Prince! You’re on fire. PRINCE. You bet I am. Yes! Behold the power of my true love. (He strikes

with some clever use of fire, a sword, a rock or something else.) MALEFICENT. Noooooooooo! Dang it. Diaval! Into a getaway. DIAVAL. Caw! (transforms into a getaway and they run off together) MALEFICENT. This isn’t over! This isn’t over!!!! PRINCE. (to Princess Aurora) And now, my love. Our time has come. (kisses her) AURORA. Oh my Prince! I knew my fairy godmother would bring you to

me, and so she has. Do you think I shall ever see her again? KING. Not likely. PRINCE. Only if she’s some kind of foolish fooly fool.
```

---

## IC-1271: Mean Girls – Original Screenplay

- Title: Mean Girls – Original Screenplay
- Author (byline): Tina Fey
- Work: Not specified
- Publisher: Scriptfly.com
- Publication date as stated: Revised June 3, 2003 (Slightly Different than the Movie)
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: CADY, SPAZZY GIRL, KAREN, GRETCHEN, DAMIAN, JANIS, MR. DUVALL, REGINA, MRS. GEORGE, VOICE OVER, GIRL 1, GIRL 2, GIRL 3, TOGETHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1482
- Already set (do not supply): none

### Source block (context only)

```text
Author: Tina Fey based on the book Queen Bees and Wannabes by Rosalind Wiseman
ISBN: N/A
Publisher: Scriptfly.com
Date (Month/Year): Revised June 3, 2003 (Slightly Different than the Movie)
Original can be purchased from Scriptfly.com at
https://www.scriptfly.com/searchpage/resultpage.php?search=m
```

### Introduction (context only: never use it for content warnings)

```text
Cady Heron may be a world traveler, but she has a lot to learn about navigating the treacherous outback known as high school; filled with back-stabbing, sarcasm, and vicious cliques – especially if you’re a girl! Fortunately, on the very 1st day of school, she meets Damian and Janis who explain the social pecking order led by The Plastics and Queen Bee Regina George.

Mean Girls – The Original Screenplay by Tina Fey
```

### Performance text (classify this)

```text
(offstage) African Music from Lion King

CADY: (Pg 6) (to audience) Hi, my name is Cady Heron. (Pg 2) I’m 15, and until today, I was homeschooled. That means my mom was my only teacher and my Dad was the only sub. I know what you’re thinking. Home-schooled kids are freaks. Cut to the Scripps Howard Spelling Bee

SPAZZY GIRL: (at microphone, speaking loudly) X! Y! L! O! CI A! R! PI Xylocarp!

CADY: Or that we’re weirdly religious or something. 8-YEAR-OLD-KID: And on the third day God created the Remington bolt action rifle so that man could fight the dinosaurs.

CADY: (Pg 3) But my family’s totally normal. Except that both my parents are research zoologists and we’ve spent the last four years in a hut in Namibia.

KAREN: (Pg 16) So, if you’re from Africa, why are you white?

GRETCHEN: Oh, my God, Karen. You can’t just ask people why they’re white!

CADY: (Pg 4) Then it happened. My mom’s articles about large cats earned her a full professorship at Northwestern University. So it was goodbye, Africa. Hello, Evanston, Illinois.

DAMIAN: (Pg 10-11) [Hi, I’m Damian and] I am so going to mentor you. The cafeteria is terrible. Buy your lunch at the school store. I recommend the white cheddar cheezits. What else? Oh! Spring Fling! (sees a gym class trudging out onto the field) In the name of all that is holy. Look at Karen Smith’s gym clothes!

JANIS: Karen is one of the dumbest girls you will ever meet. Damian sat next to her in English class last year.

DAMIAN: She asked me how to spell orange!

JANIS: And that little one next to her? That’s Gretchen Wieners. She’s rich cause her Dad invented Toaster Strudel.

DAMIAN: She is a little Gucci Hootche – A girl with a $1,000 of designer clothes on a $2.00 body.

JANIS: (Pg 17) (pointing and whispering) [That’s] Regina George. She is the most plastic of all The Plastics.

DAMIAN: She is fabulous, but she is evil. ***** Later that Day in the Cafeteria *****

MR. DUVALL: (Pg 15) Please give a round of applause for the head of the Student Activities Committee Miss Regina George!

REGINA: Thank you! Under my rule the SAC will do more than just sell candy canes and sponsor stuff like recycling. It’s gonna be about being kind to the less fortunate. Where’s that new student? (she spots Cady in the crowd) Come here! (Cady joins her on stage) I’m going to make it my personal responsibility that by the end of the year, she thinks Evanston High school is totally rad. A few minutes later – Cady is sitting with Regina, Karen and Gretchen (The Plastics)

CADY: (Pg 16) And we only moved here two weeks ago—

REGINA: (Regina grabs Cady's arm) Where did you get that bracelet? I love it.

CADY: Africa.

GRETCHEN: It's so fetch.

REGINA: (disdainful) What is "fetch?"

GRETCHEN: (withering) It's, like, slang . . . from England . . .

REGINA: (Pg 27) (rolls her eyes) You know what, Cady? You're, like, actually really pretty.

CADY: Thank you.

REGINA: (snarky) So you agree?

CADY: What?

REGINA: You think you're really pretty.

CADY: I didn't say that. (to audience) What just happened?

REGINA: (Pg 16-17) (haughtily) Cadv, could you give us some privacy for, like, one second? (huddles and whispers with the other two plastics) Okay, let me just say that we don't do this a lot, so you should know that this is, like, a huge deal.

GRETCHEN: We want to invite you to have lunch with us every day for the rest of the week. So we'll see you tomorrow.

KAREN: On Tuesdays we wear pink!

CADY: (Pg 19) (to audience) Having lunch with the Plastics was like leaving the actual world and entering "Girl World." And Girl World had a lot of rules.

KAREN: We only wear jeans or track pants on Friday.

GRETCHEN: You can't wear a tank top two days in a row.

REGINA: You can only wear your hair in a ponytail once a week. So, I guess, you picked today. (Pg 80) I’m starving. (leaves to get lunch)

GRETCHEN: (Pg 19-21) And if you break any of these rules you can't sit with us at lunch. I mean, not just you, any of us. Like, if I was wearing jeans today, I would be sitting over there with the art freaks. (points to Janis and Damian’s table)

KAREN: You have to be considerate of the rest of the group. I mean, you wouldn't buy a skirt without asking your friends first if it looks good on you. It's the same with guys. You may think you like someone, but you could be wrong. Have you seen anyone that you think is cute yet?

CADY: Actually, there's a guy in my Calculus class. His name is Aaron Samuels—

KAREN: No, no no.

GRETCHEN: No. You can NOT like Aaron Samuels. He's Regina's ex-boyfriend. And then he broke up with her for no reason.

KAREN: Because she cheated on . . .

GRETCHEN: Regardless. Ex-boyfriends are off limits to friends. Don't worry. I will never tell Regina what you said. It'll be our secret. (Regina enters with her food)

REGINA: Ugh. There's gonna be a fire drill in, like, two seconds. (Fire alarm goes off) I told Coach Farr we had to skip it cause Karen might be pregnant.

KAREN: (laughs, then) I'm not though, right?

GRETCHEN: (Pg 23-24) Oh, my god, there’s Jason! . . . (heartbroken) He’s with Taylor Wedell.

REGINA: (outraged) Wait. No. He cannot blow you off like that. Gimme your phone. (dials) Wedell on South Boulevard (pushes another button on phone – then in a mature voice) Hello, may I speak to Taylor Wedell please? This is Susan at Planned Parenthood. I have her test results. Have her give me a call. Today, if she can. It’s urgent. Thanks. (she hangs up, Regina and Gretchen laugh) She is not going out tonight!

CADY: (wide-eyed to audience) I could see why it was good to have Regina as a friend. (beat) I guess the Plastics liked having me as a pet, cause by Friday I was invited to Regina's house after school. (to Regina) Regina, your house is really nice. REGINA I know, right?

MRS. GEORGE: (Pg 25) You want anything, don't be shy, honey. There's no rules here. I'm not like a regular mom, I'm a cool mom, right, Regina?

REGINA: (exiting) Please stop talking. (Regina opens the door to her huge bedroom) This is my room (The girls settle in which involves looking at themselves in the many mirrors)

KAREN: (Pg 23) So how was your first week?

CADY: Good. I'm joining the Mathletes.

REGINA: No, no, no. That is social suicide. You are so lucky you have us to guide you.

GRETCHEN: (Pg 26-27) I never should have bought these capri pants.

REGINA: How many times do I have to tell you? The Gap is for old people.

GRETCHEN: I hate my calves.

KAREN: God, my hips are so huge.

CADY: (to audience) Before I met the Plastics, I thought there was just fat and skinny. Apparently there's an infinite number of things on your body that can go wrong.

GRETCHEN: My hairline's weird.

REGINA: My pores are huge.

KAREN: My nailbeds suck. (The girls look at Cady. It is her turn.)

CADY: (struggling to come up with something) I have really bad breath when I wake up in the morning.

REGINA: (Pg 33-34) (cattily) Gretchen told me that you like Aaron Samuels.

CADY: (terrified) What are you talking about?

REGINA: I mean, I don't care. (obviously cares) Do whatever you want. But wait. Aren't you so mad that Gretchen told me about this?

CADY: (looks at Gretchen) I’m not mad. (trying to assume the attitude of “A Plastic”) She’s just immature.

GRETCHEN: (stomps her foot and pouts) I can't believe you think I'm immature!

CADY: (Pg 39) (to audience) I knew how this would be settled in the wild. (Regina leaps like a cheetah at Cady who chatters and howls like a monkey) But in Girl world, all the fighting had to be invisible. (shakes head) ***** The Next day at the Mall ***** Damian and Cady go to visit Janis at Bath and Body Works where she is behind the counter working.

CADY: (Pg 30-31) And they have this book, this "Burnbook" where they write mean things about the girls in our grade.

DAMIAN: Rosemary Mint Foot Spray?

JANIS: It makes your feet smell like a salad. (to Cadv) Cady, you've got to steal that book. We could publish it and then everyone would see what an ax-wound she really is!

CADY: No way! I don't steal.

JANIS: There's two kinds of evil people, Cady. People who do evil stuff. And people who see evil stuff being done and don't do anything to stop it. (Pg 79) You’re the worst. At least Regina George knows she’s mean. You act like you’re so innocent. (imitating Cady) I used to live in Africa with the birds and the monkeys.” You’re plastic! Solid, durable, molded plastic!

***** Principal’s Office Monday Morning ***** Regina is fake crying to MR. DUVALL. He is reading the "Burnbook."

REGINA: (Pg 81) I found it in the girls' bathroom. It's so mean, Mr. Duvall.

MR. DUVALL: (shocked) Good Lord. What does that say? (reads aloud) Regina George is the nastiest (clears throat) I ever met. Do not trust her! She is an ugly (clears throat) . . .

REGINA: (fake sobs) Why would somebody write that? It's so mean!

MR. DUVALL: Okay, take a breath. We'll find out who did it.

REGINA: (suddenly ice cold) There's only three girls in the whole grade who aren't in it. [Inserted as transition]

VOICE OVER: (Intercom off-stage): Cady Heron, Gretchen Wieners, and Karen Smith report to Mr. Duvall’s office immediately. Cady Heron, Gretchen Wieners and Karen Smith report to Mr. Duvall’s office. ***** Scene Change*****

CADY: (Pg 93) (to audience) Ms. Norbury had us write out apologies to people we had hurt in our lives. (The girls read written "apologies" out loud)

GIRL 1: Alyssa, I'm sorry I called you a gaptoothed b****. It's not your fault you're so gap-toothed.

GIRL 2: Laura, I don't hate you because you're fat. You're fat because I hate you.

GIRL 3: I iust wish we could all get· along like we used to in Middle School. I wish I could bake a cake made out of rainbows and smiles and we'd all eat it and be happy—

DAMIAN: She doesn't even go here!

CADY: (Pg 113) (to audience) I guess the biggest thing I learned at Evanston was that tearing other people down will not make your life any better. Calling somebody else fat will not make you any thinner. Telling someone they're stupid does not make you any smarter. (Pg 117) My first year of "real" school was like treading water in a shark tank, but now, I just float.

TOGETHER: Do-Wap Baby Shark music and dance to end selection
```

---

## IC-1272: Medea

- Title: Medea
- Author (byline): Christopher Durang and Wendy Wasserstein
- Work: 27 Short Plays
- Publisher: Smith and Kraus Publishers
- Publication date as stated: Feb 1996
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTRESS, CHORUS, MEDEA, JASON, MESSENGER, ANGEL
- Teaser before the introduction: Yes
- Spoken words (computed): 1100
- Already set (do not supply): none

### Source block (context only)

```text
Author: Christopher Durang and Wendy Wasserstein
Book: 27 Short Plays
ISBN: 978-1880399897
Publisher: Smith and Kraus Publishers
Date (Month/Year): Feb 1996
```

### Introduction (context only: never use it for content warnings)

```text
Medea by Christopher Durang and Wendy Wasserstein

Enter the Chorus. In the style of the piece, they are over-dramatic and over-wrought. But most of the time they should act their lines as if they are the words from genuine Greek tragedy, full of intonation and emotional feeling. Don't send them up, or wink at the audience. Let the juxtaposition of Greek tragedy acting style and the sometimes silly lines be what creates the humor.
```

### Performance text (classify this)

```text
The actress who is to play Medea comes out and makes the following introduction.

ACTRESS: Hello. I am she who will be Medea. That is, I shall play the heroine from that famous Greek tragedy by Euripides for you. I attended a first rate School of Dramatic Arts. At this wonderful school, I had classical training, which means we start at the very beginning, a very good place to start. Greek tragedy.

As an actress who studied the classics, one of the first things you learn in drama school is that there are more roles for men than for women. This is a wonderful thing to learn because it is true of the real world as well. Except for Thelma and Louise. At drama school, in order to compensate for this problem, the women every year got to act in either The Trojan Women or The House of Bernardo Alba. This prepared us for bit parts on Designing Women and Little House on the Prairie. Although these shows are cancelled now, and we have nothing to do.

I would like to present to you a selection from one of the most famous Greek tragedies ever written, The Trojan Women, translated from the Greek by George Stephanoulous, here is a scene from this terrifying tragedy.

CHORUS: (In unison.) So pitiful, so pitiful your shame and lamentation. No more shall I move the shifting pace of the shuttle at the looms of Ida. - (Echoes.) Looms of Ida. Can you not, Queen Hecuba, stop this Bacchanal before her light feet whirl her away into the Argive camp? (Echoes.) Argive camp. O woe, O woe, O woe, So pitiful, so wretched, so doomed, Women who run with wolves Women who love too much, Whitewater rapids, how did she turn $1000 into $100,000? O woe, O woe, O woe, Here she comes now. Wooga, wooga, wooga.

(Enter Medea in a dramatic, blood red toga. She is in high, excessive grief and fury.)

MEDEA: Come, flame of the sky, Pierce through my head!
What do I, Medea, gain from living any longer? Oh I hate living! I
want
to end my life, leave it behind, and die.

CHORUS: (In unison; chanted seriously.) But tell us how you're really feeling.

MEDEA: My husband Jason - the Argonaut - has left me for another woman.

Debbie.

CHORUS: (In unison.) Dreaded Debbie, dreaded Debbie. Debutante from hell.

MEDEA: She is the daughter of King Creon, who owns a diner on 55th Street and Jamaica Avenue. Fie on her! And the House of Creon! And the four brothers of the Acropolis. I am banished from my husband's bed, and from the country. A bad predicament all around. But I am skilled in poison. Today three of my enemies I will strike down dead: Debbie and Debbie's father and my husband.

CHORUS: (In unison.) Speaking of your husband, here he comes.

(Enter Jason, dressed in a toga, but also with an armored breast plate and wearing a soldier's helmet with a nice little red adornment on top. Sort of like a costume from either Ben Hur or Cleopatra. He perhaps is not in the grand style, but sounds more normal and conversational.)

JASON: Hello, Medea.

MEDEA: Hello, Jason.

JASON: I hear you've been banished to China.

MEDEA: (Suddenly Noel Coward brittle.) Very large, China.

JASON: And Japan?

MEDEA: Very small, Japan. And Debbie?

JASON: She's very striking.

MEDEA: Some women should be struck regularly like gongs.

JASON: Medea, even though thou art banished by Creon to foreign shores, the two innocent children of our loins, Lyle and Erik, should remain with me. I will enroll them at the Dalton School. And there will they will flourish as citizens of Corinth under the watchful eye of Zeus and his lovely and talented wife Hera.

MEDEA: Fine, walk on me some more! I was born unlucky and a woman.

CHORUS: (In unison.) Men are from Mars, women are from Venus.

JASON: Well, whatever. I call the gods to witness that I have done my best to help you and the children.

MEDEA: Go! You have spent too long out here. You are consumed with craving for your newly-won bride, Debbie. Go, enjoy Debbie! (Jason shrugs, exits.) O, woe, O, woe. I am in pain for I know what I must do. Debbie, kill for sure.

CHORUS: (In unison.) Debbie's done, ding dong, Debbie's done. Done deal, Debbie dead. Dopey Debbie, Debbie dead.

MEDEA: But also my sons. Never shall their father see them again. I shall kill my children. (Ferociously, to the Chorus.) How do you like that????

CHORUS: (In unison.) Aaaaaaagghghghghghghgghhhhh! A smart women, foolish choices. Stop the insanity! Stop the insanity! You can eat one slice of cheese, or 16 baked potatoes! Make up your mind.

MEDEA: Why is there so little Trojan Women in this, and so much of me?

CHORUS: (In unison.) We don't know The Trojan Women as well as we know Medea.

(Spoken, not sung.) Medea, we just met a girl named Medea. And suddenly that name Will never be the same.

MEDEA: Bring my children hither.

CHORUS: (In unison.) O, miserable mother, to destroy your own increase, murder the babes of your body. The number you have reached is not in service at this time. Call 777-FILM.

MEDEA: (In a boiling fury.) I want to kill my children. I want to sleep with my brother. I want to pluck out the eyes of my father. I want to blow up the Parthenon. I need a creative outlet for all this anger. (Enter the Messenger, carrying a head. He kneels before Medea.)

MESSENGER: I am a messenger. Caesar is dead.

CHORUS: (In unison.) Caesar is dead. How interesting. Who is Caesar?

MESSENGER: I am sorry. Wrong message. (Reads from piece of paper.) Lady Teazle wishes you to know that Lady Windermere and Lady Bracknell are inviting you and Lady The-Scottish-Play to tea with her cousin Ernest, if he's not visiting Mr. Bunberry.

MEDEA: Mr. Bunberry? I do not need a messenger. I need a deus ex machina.

(Elaborate music. Enter an Angel with great big wings. Descending from the ceiling, or revealed on a balcony. Or dragging a step ladder that he stands on. Very dramatic whatever he does.)

ANGEL: O, Medea, O, Medea.
I am a deus ex machina.
In a bigger production, I would come down from the sky in an angel's
outfit, but just use your imagination. Theatre is greatly about
imagination, is it not.
I am an angel.
I I I I I I I, yi yi yi.
I I I I am the Bird of Greek Tragedy.
Do not kill your children. Do not sleep with your brother.
Rein in your rage, and thank Zeus. I come with glad tidings. Debbie is
no more a threat. She's been cast in a series. She has a running part
on Home Improvements.

CHORUS: (In unison.) Home Improvements.

ANGEL: Jason will return to you. He sees the error of his ways. He has been lobotomized.

CHORUS: (In unison.) O fortunate woman, to whom Zeus has awarded a docile husband.

MEDEA: O, deus ex machina, O, angel: O, Hecuba, oh, looms of Ida.

CHORUS: (In unison.) Ida Ida Ida Ida.

MEDEA: I am eternally grateful to you.

CHORUS: (In unison.) The things we thought would happen do not happen. The unexpected, God makes possible.

(Spoken, not sung.) The camptown races sing a song, Do da, do da.

CHORUS and MEDEA: (Switch to singing now.) Medea's happy the whole day long,
Oh the do da day!
Things will be just fine,
Things will be just great
No need to kill her children now, Oh the do da ...

(Big musical coda:)
Oh the do da, Zeus and Buddha, They're as nice as Dionysus,
Oh the do da Work it though da
Oh the do da, do da, do da Day!

(Medea and the Chorus and the Angel strike a happy and triumphant pose.)
```

---

## IC-1273: Dinosaurs Love Chips

- Title: Dinosaurs Love Chips
- Author (byline): Matt Mills
- Work: Dinosaurs Love Chips
- Publisher: Mushroom Cloud Press
- Publication date as stated: August 1, 2023
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1469
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
“Dinosaurs Love Chips”

by Matt Mills

A bubbly, rambunctious, but unprepared fifth grader, ELLIE FAE, walks up to the front of her classroom.

Thank you, Miss Anderson. And thank you all for listening to my big important fifth grade science report that I definitely remembered to do.

Okay. So. What am I going to talk about today? That is a great question, Ellie Fae. Thank you, Ellie. You’re welcome, Ellie. So, Ellie—what are we going to talk about today? …I’m not actually asking this, of course, because I know the answer. It’s just you that don’t. Uh. Know what I’m going to talk about today. That is… okay, what we’re—I’m about to say what I’m talking about today, because it is… um… dinosaurs!

Yeah. Bet you didn’t see that coming. Well you should’ve, ‘cause I’ve known for a very long time of research and time that my project is about dinosaurs. So here it uh, finally goes… in a minute. After I’m done, uh. Transitionaling. Yeah. Just one more transitional and then I’ll start, okay? Okay. I say it’s okay. Okay. Ready? Okay. Here it goes. In three. Two. One. Now here it goes. …Okay here it is. Finally. For real. Here’s how my science report goes… this is it. Listen. I’m starting now…

Dinosaurs were born a really, really long time ago. Like, before the 1980s. Dinosaurs are so old they aren’t allowed to vote. If they did, they would only vote for Godzilla, and that is really unfair.

Ellie uses blank easel paper as a visual aid.

As you can see here, this blank page shows that dinosaurs live in a democracy, which means that once a week they get together and vote on who gets to eat the most cats. Dinosaurs eat meat, but they also eat vegetables and chips and tomatoes, so science considers them alleatvores. Dinosaurs are bad at chopsticks, but they’re also bad at forks. They eat with their teeth and anything they can’t pick up gets blended into a shake for dessert. Ummm… what else. I just—my brain is so full of dinosaur knowledge! It’s hard to get it all out. Yeah. It’s like… when there’s too much stuff in a drawer. Does that ever happen to you? Dinosaurs don’t have drawers. That’s a fun fact. Hmmm…

Ellie spots the world map dropdown, rushes over to it, and unfurls her new visual aid.

As you can see here on this map, dinosaurs rode an asteroid to Earth during the Crustaceans period. Then they settled all over, bringing their love of fast food and opera to the whole planet. It was easy for them, too, because their legs were taller than mountains, and they liked the way the trees itched their legs when they walked. Stepping in lakes didn’t bother them as much as it bothers my brother, either. Dinosaurs are good at walking and hate couch potatoes. They hate couch potatoes so much that they don’t even eat them—they just chew on them like greasy gum. Dinosaurs don’t chew gum, but the world would be a better place if they did, because their breath smells.

Dinosaurs believe in cannibalism, which is where rich people get to make money and poor people get to work. They don’t like taxes but they do them anyway. One time, a dinosaur tried to not pay his taxes, but a nice older dinosaur talked him into it. Dinosaurs have a strong sense of community and they always talk about their problems with people who know better.

Dinosaurs made a bunch of our land usable by building basketball courts, skate parks, and jungle gyms. Even though they’re too busy at the office to have fun, they still like building fun things so they can feel fun, even though they’re not. In fact, dinosaur brains are missing the part where fun happens. They also can’t cry, but some dinosaurs have learned how to cry from watching Disney movies. Dinosaurs love life and all of the feelings that come with it. They will hunt and gather all of the feelings they can find, even though one of their first presidents was like, “Should we really be hunting and gathering feelings all the time?” But the rest of the dinosaurs were like, “Yeah, man. I never get sick of hunting and gathering feelings. It’s really fun, even though I don’t know what fun is because I’m a dinosaur and I’m missing that part of my brain. Sign me up for all of the hunting and gathering field trips we got!” Uh, so dinosaurs expanded and expanded across the world, building and eating and building and…

Ellie brainstorms a moment, then sets her whole body to acting out her “report”.

But! But when the dinosaurs ran into SeaWorld, the dolphins attacked back! Armed with seals and very loud whistles, they invaded DinosaurLand and made the dinosaurs give up their sports gambling, even though it was an important part of their culture. But the dinosaurs were brave and hungry, and bought humvees to drive over to SeaWorld’s house and tell SeaWorld, “Hey! Cut it out! The whole world isn’t SeaWorld! This is all of our world, not just the sea’s!” So the dinosaurs scared the dolphins with facts and logic, and that’s when SeaWorld decided to only be at a few locations and none of them are close to my house, even though I wrote them a letter asking them to change their mind. Peace deals are a very big deal, especially to the dinosaur army.

Ellie settles and resets. She flips the easel to a new blank page.

After the great SeaWorld war of the 1980s, dinosaurs had enough time and scientists to invent the French Industry Revolution, where their cars went from being powered by dumb cavemen’s feet to putting bombs in the engine so they could fly to Florida to visit their grandparents every winter, even though their grandparents don’t have any teeth. Dinosaurs are very family-oriented and if you have a problem with one dinosaur, good luck traveling the globe, buddy. Ummm…

Ellie looks around desperately. She grabs some classroom tools.

Dinosaurs have bigger feet than us, so if you look at this ruler—this foot-long ruler— imagine a bunch of these put together and that’s a dinosaur’s foot! Crazy, right?! That’s a lotta footpower. Ummm… Also, dinosaurs invented the stapler during the 90s when their printer kept printing stuff and they couldn’t figure out how to turn it off so they had to put the papers together somehow before they flew away and littered all of their moving walkways. Ummm scissors… were invented by humans.

She tosses the scissors, thinks, then flips over a new blank page on the easel.

Dinosaurs spent their not-2000s years creating all of our greatest technologies, from the iPhone to the air fryer. But when one dinosaur family took a vacation to Peru, they accidentally knocked over a tiger’s coffee mug, and she said, “Hey! I’m turning some of you into fossils and the rest of you I’ll leave alone!” And the dinosaur family couldn’t argue because they signed an agreement not to argue in Peru. So that angry tiger made some really neat fossils out of that dinosaur family and sold the fossils to gift shops around the world, and dinosaurs decided to leave Peru alone forever and continue on with their lives around the rest of planet Dinosearth.

Ummm… soooo… for years the dinosaurs lived in peace, building malls and teaching their kids how to go to college and find a boyfriend. But that all changed one fateful day, when the aliens arrived. Seeing the planet ruled by these cool people that look like walking snakes, the aliens told their friends, “Hey guys! I need some backup, can you come help me please?!” So then a bunch of aliens visited Earth, but they did not have a good time. They asked the dinosaurs, “Why isn’t Earth a better time?” And the dinosaurs were like, “Well, it was a better time before you guys showed up. No offense.” But the aliens took offense. The aliens took so much offense that they took the dinosaurs as hostages to go answer for their crimes in space court, and while they’re there, the space judge was like, “What?” But us humans living on the moon were like, “Sweet! Free planet!” So we hopped off the moon and invented paper and cleaned all of the malls and put silly names on them and invented tofu and the sun and sadness and…

Something catches Ellie’s eye, stopping her in her tracks.

Oh! Miss Anderson, you took your earbuds out! Because my science report is so good, right? …Oh. Okay. Why? Does the principal want to hear my presentation too?! …Oh.
```

---

## IC-1274: KTD’s

- Title: KTD’s
- Author (byline): Elizabeth Bogle
- Work: KTD’s
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1414
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
(In blackout with curtains closed)
GLORIA
What is going on here?!
CASSIE
Ew, Gloria, why are you out here?
GLORIA
Am I not allowed to enjoy a stroll around the lake without seeing two CHILDREN
DESECRATING THE SANCTITY OF MARRIAGE AND OF THIS CAMP?!
MARCUS
(A typical high school jock type)
What?
CASSIE
Chill, Glor. We’re not even doing anything.
GLORIA
Chill? CHILL?! I’ll have you know I have not “chilled” since ’76! Now you two are in huge
trouble, come here!
CASSIE
AHH! What the heck, Gloria?!

(To MARCUS)
RUN! SHE CAN’T GET US BOTH!
GLORIA
I CAN TRY! COME HERE!
(Curtain opens)

Scene: Lights up on a bored teen (CASSIE) and chipper camp counselor (GLORIA). CASSIE sits
cross-legged while GLORIA tries to remain calm. Her chipper voice could crack as she gets
angrier, but it is up to interpretation.
GLORIA
(Frantically pacing in front of CASSIE)
Ya know, Cassie, Jesus doesn’t like sinners.
CASSIE
(Blasé, nonplussed, and uninterested)
So I figured.
GLORIA
In fact, I wouldn’t be surprised if he sent you straight to Hell right now. Here, I’ll ask him.
(Yelling at the sky)
Hello? Jesus? JESUS! Are you there? My friend Cassie here wants to talk to you!

CASSIE
I’m not your friend.
GLORIA
(Ignoring CASSIE)
Cassie wants to know if you’ll send her to Hell for kissing a boy! She’s not even married to him,
Jesus! She’s going to get a KTD! Maybe a few considering they kissed more than 5 seconds!
CASSIE
What’s a KTD?
GLORIA
(To CASSIE)
A Kiss-Transmitted Disease. Try to keep up, honey.
(Back to the sky)
Ya know, I tried to get the boy too, but he ran away.
CASSIE
At least he got away.
GLORIA
(Back to CASSIE)
Excuse you, young lady. You’ve said enough. You’re just damning yourself even further.

CASSIE
Suuuuuuuure, Gloria.
GLORIA
(Frantically)
Boom! That’s another layer of Hell for you! I can already hear your sizzling flesh from the
Devil’s flames! And actually… BOOM!
(Pokes CASSIE’s cheek)
That’s for calling me Gloria. You know I like Mama Sunshine at this camp!
CASSIE
Mama Sunshine?
GLORIA
It creates a familial and familiar bond between myself and my campers. It makes us kindred
souls, sister spirits, brother—
CASSIE
(Cutting GLORIA off)
Screw this.
(Kicks down her chair and storms out past GLORIA)
GLORIA
THAT’S ANOTHER LAYER MISSY! JESUS WILL NOT APPRECIATE THIS! HE DOESN’T
LIKE YOUR FOUL WORDS!
CASSIE
(From offstage)
SCREW SCREW SCREW!!!!!
(GLORIA EXITS in frustration)
(END scene.)

Scene: ANGELS stand around CASSIE’s bed while she sleeps. Perhaps they are singing.
Throughout this “mini-scene”, the white-clad ANGELS dance about when not interacting with
CASSIE’s dream. DREAM CASSIE can either be a different actress while CASSIE remains
asleep, or just be CASSIE white-clad, like the ANGELS.
ANGEL
(Ghost-like)
Cassie… Cassie…
DREAM CASSIE
Who are you?
ANGEL
We are your personal “plot devices”.

DREAM CASSIE
Wow!
(pause)
What’s that?
ANGEL
We’re here to move along the story you’re currently in!
DREAM CASSIE
Cool!
ANGEL
Not at all because…
ANGEL
We’re giving you…
ANGEL
A KTD!
DREAM CASSIE
What?
(The ANGELS surround CASSIE and furiously work. At this point, DREAM
CASSIE, if a different actress, EXITS, and the ANGELS work to give CASSIE a
swollen lip and help her through a costume change. If DREAM CASSIE and
CASSIE are the same, a quick costume change as well as the quick “swollen lip”
are applied. Throughout this, CASSIE may choose to yell “No” and “Stop” and
other expletives. As soon as they are done, the ANGELS disperse and reveal the
newly-infected CASSIE. Lights out on CASSIE’s confused face)
(END scene)

Scene: Lights up on a typical bunk for a couple teenage girls at a Bible camp. Perhaps bras are
strewn about. At least a chair and some kind of vanity with a “mirror” are needed. Lights up on
CASSIE frantically pacing around her room, mulling over her now swollen lip. Perhaps the
actress checks herself out in the mirror, disappointed with the new addition to her face.
CASSIE
I can’t go to breakfast looking like this! Someone will think I got into a fight!
(Scouring the area)
Lipstick?... Gloss?... Chapstick?... Anything?!
(Suddenly discovers a bunkmate’s lipstick)
Aha!
(After applying the lipstick)
Maybe no one will notice.

(CASSIE EXITS with any props she had with her as well as moving the chair
from earlier as GLORIA ENTERS with OTHER CAMPERS. The actress for
GLORIA may choose to pace as she’s speaking)
GLORIA
Good morning campers! I hope you all slept splendidly last night. I trust that the Good Lord
above blessed each and every one of your dreams. I know he sure blessed mine! In fact, last
night I dreamed my husband wasn’t cheating on me and that he found religion and we went to
Heaven together, in love like we once were. But that’ll never happen because his mistress has a
yacht. I’d leave me for a yacht, too! In fact, I’d leave me in general. I’m grossly undesirable.
Isn’t that right STEVE?! YOU THINK I DON’T KNOW ABOUT THAT 20-YEAR-OLD
PROSTITUTE YOU”VE BEEN SLEEPING WITH! WELL GUESS WHAT? I DO! AND SHE
IS GORGEOUS! BUT, NO MATTER! I’LL BE LAUGHING WHEN YOUR AFFAIR LEADS
TO MURDER AND HELL! MURDER, STEVE! YOU CAN’T TRUST HER! WHY WOULD
SHE GO FOR YOU?! YOU’RE OLD, FAT, AND BALDING. YOU PROBABLY LOOK LIKE
HER GRANDPA!
(As the actor continues adlibbing as GLORIA, CASSIE ENTERS. Unless deemed
fit in performance, CASSIE will not try to blend in or be discreet. If anything, she
is likely to make a show of herself as though she’s late on purpose)
Look who decided to show up! Cassie, would you mind telling us why you’re late for morning
prayer and breakfast?
CASSIE
I just am, man. Just am.
GLORIA
And would you mind telling us why on earth you have a lip fatter than a whale?
CASSIE
(Grabbing at her lip self-consciously)
What lip fatter than a whale?
GLORIA
The one you’re failing to hide with your little hands.
CASSIE
(Uncovering her lip to gesture with her hands)
My hands are not small!
GLORIA
Neither is your lip.
CASSIE
(Indignantly)
I do not have a fat lip!
GLORIA
(Nodding emphatically)
Yes, you do.
CASSIE
Oh. OH! You mean this fat lip? Yeah, that’s a great story I’d love to tell if it wouldn’t interrupt
your riveting yelling about your husband’s amorous affair.
GLORIA
No, please. Do tell.
CASSIE
I couldn’t impose.
GLORIA
(Shouting from deep within her chipper body)
TELL THE STORY, CASSIE!
CASSIE
(As though this is the most exciting story)
I, uh, ran into a wall.
GLORIA
Oh did you? Or is that a KTD?!
CASSIE
No! No one even knows what a KTD is!
CAMPER
It’s a kiss transmitted disease! Miss Dart taught us about it last year after—
CASSIE
I didn’t need a stupid answer!
CAMPER
I was just –
CASSIE
SHUT UP!
GLORIA
Irritability is a huge symptom of any KTD.
CASSIE
You lie, Gloria.
GLORIA
Do I?
CASSIE
(Begins to feel a bubbling in her upper lip as it starts to swell as well)

(Muffled due to two swelled lips)
It’s not a KTD! I swear!
OTHER CAMPERS
(In confusion)
What’s a KTD? Do I have one? Do you have one? Is it a sign of the end of the world? IS THE
RAPTURE COMING?! I’M SCARED!
GLORIA
(Speaking loudly over the OTHER CAMPERS’ rising shouts)
Oh, honey. You’re so naïve. I’ve seen many KTD’s in my time as a counselor here.
(Stepping closer to CASSIE)
And you by far have one of the worst cases I’ve seen. Tell me. How long were you kissing this
boy?
CASSIE
That’s none of your business!
GLORIA
Then somebody doesn’t want to get better.
CASSIE
And how is telling you how long Marcus and I kissed gonna help me get better?

GLORIA
It wouldn’t. I just needed his name.
(Turning out)
MARCUS!!!
(MARCUS stands and runs into the HOUSE. GLORIA whips towards him. At
this point, CASSIE tries to make a break for it, but GLORIA grabs her and pulls
her offstage, signaling a blackout.)
(END scene.)

Scene: Lights up as GLORIA paces in a frantic circle around the bored, but breaking out and swelling CASSIE. The counselor is nearly hyperventilating and is not fighting to stay calm. Perhaps the actress makes wild hand gestures that don’t even relate to what she’s saying. MARCUS sits in a chair next to CASSIE, glaring at GLORIA for finding him out, and ignoring CASSIE’s attempts at conversation. CASSIE (Pleading) Marcus, I’m sorry. I’m weak. It wasn’t supposed to slip out. MARCUS (Disconnected) Of course it wasn’t. But it did.

CASSIE (Unsure of what to say) I’m sorry?

Don’t bother.

MARCUS

GLORIA (Chuckling at CASSIE) This is your own doing, Cassie.

My doing? How is this my doing?

You kissed the boy, I didn’t.

(Rolling his eyes) Trust me, it won’t happen again

(To MARCUS)

CASSIE

GLORIA

MARCUS

CASSIE Why was it not good? (GLORIA clears her throat, and CASSIE looks at her) But I hadn’t even heard of KTD’s before you spewed about them! GLORIA They teach about them in school. Maybe you should’ve studied harder. MARCUS Wait they did? GLORIA (Nodding passionately) Whole little unit, right after STDs. CASSIE Bull. They’ve never said anything about some made up kiss disease! CAMPER (Peeking in) Don’t mind me, but we really did learn about— CASSIE Where did you even come from?!

A uterus, I think.

Ew! I didn’t mean—never mind.

Can you just… leave?

Please do.

Sorry. (CAMPER EXITS)

So wait, do I have this disease too?

Don’t encourage her! It’s not real!

CAMPER

CASSIE

MARCUS

CASSIE

CAMPER

MARCUS

CASSIE

GLORIA If it’s so made up why do you have symptoms?

MARCUS
Good point!
GLORIA
Thank you, Marcus!
CASSIE
Hello? Suffering from a made-up disease here!
GLORIA
Oh, right!
(GLORIA examines CASSIE as though she is a doctor. MARCUS stares off into
the distance, thinking about nothing. After a brief pause, GLORIA stops and
begins rummaging in a bag)
I do know how to help you, you know.
CASSIE
You do?
GLORIA
(Still rummaging)
Of course I do. I’ve been a counselor for over 20 years. Your messing around is nothing new.
There’s just a little shot.

CASSIE
That’s great! Can I have the shot?
GLORIA
Of course!
(Pulls out a wickedly large needle that glints maliciously)
(CASSIE flinches as it nears her, meanwhile, MARCUS has run offstage, afraid
of the giant needle. The actor finally gets to express for this expressionless
character)
(Lights out just as GLORIA is about to inject CASSIE)
CASSIE
AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!!!!!!!!!!
GLORIA
(Over CASSIE’s screams)
TRUST YOUR MAMA SUNSHINE!!!!
(END play)
```

---

## IC-1275: Lover’s Island

- Title: Lover’s Island
- Author (byline): Stephanie Christensen
- Work: Lover’s Island
- Publisher: Mushroom Cloud Press
- Publication date as stated: December 11, 2023
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2145
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
Humorous Interpretation- F or M

Host (highly enthusiastic): Welcome to Lover’s Island– an arm-tingling new TV show that mimics– no, OUTSHINES, your favorite trash reality TV show Love Island! (stares directly at an audience member) No rights reserved, copyright infringement NOT intended, please do not sue me, I’m just a broke 37-year-old trying to make it as a Hollywood actor. ANYWAYS… On OUR show, Lover’s Island, not only are these hot singles here to find love, but what they DON’T know is that they’re here to find survival too. That’s right. With absolutely zero help from the TV show producers, cameramen, or me, 12 stupid yet attractive singles must learn to fend for their lives in the brutal hurricane season of the pacific ocean on a desert island AND flirt at the same time. Man, they don’t have a clue what’s in store! … Let’s meet our lucky contestants! Mikayla: HI! I’m Mikayla! I’m from Southern California, but don’t be fooled… I’m a laguna beach babe, not a burbank bummer. I said yes to Lover’s Island to find the love of my life! A guy with strong arms, dangerous-looking tattoos, and a cruel sense of humor that makes me question his loyalty to me. Wait, no, that was the OLD Mikayla. The new year new me Mikayla is NOT falling for toxic love anymore. I’m not here to be a side chick. I’m here because I’m wifey material. Host: WOW! Welcome Mikayla! What a bombshell! Next up, it’s time to meet our first guy… Gerald! Gerald: Hey. I’m Gerald. Host: Tell the audience about yourself, Gerald! This is your intro interview, after all. Gerald: There’s not much to say. I like free trips to the beach. Host: But this is an island, Gerald. Gerald: I like free trips to islands. They seem like the beach. Host: Uh huh…

Gerald: She’s hot. Host: ALRIGHT. I think maybe Gerald is an onion– off-putting and smelly on the outside but just needs a little peeling of his layers to get to the true delicious personality inside. Gerald: Yeah. That’s what makes me Gerald. Host: And the next boy you’ll be meeting is Ryan– a surfer from Pacific City Beach, Oregon. Ryan: What’s up man! My name is Ryan! I love adventures and I love life! Life is full of so many joyous surprises, man! I’m a MASSIVE surfer and surfing is a part of everything I do– just like my search for love! Host: Tell us more, Ryan! Ryan: I look for love in every person and thing I meet. You’re nice to me in a grocery store? Love. You honk at me in traffic because I was texting instead of watching the light turn green? Love. You turn the TV volume up so we can watch football together instead of talking? THAT’S LOVE! Even if I see a wilted fern that needs to be watered or a deceased possum who couldn’t quite safely cross the street, I know there’s love in those things too. Host: Welp. That’s both nice and really disgusting. Welcome to the show, Ryan! And finally, let’s meet our last two contests– two strong women. On Lover’s Island, we like to make our ratio three women to two men to both INCREASE competition and increase the odds of survival for our cohort. Usually more women means better outcomes. Meet Jerry Ann and Symphony! Jerry Ann: Hello! Symphony: I’m honored to meet me, too, I know. Jerry Ann: My name’s Jerry Ann. I’ve been an investment advisor at a tax firm for the past 20 years. Ryan: YIKES you’re old! Jerry Ann: Alright, barbie doll ken. I may be seasoned, but that helped me learn how to be a great life partner through several failed relationships. I work remote so I have plenty of flexibility in my schedule. And I’m looking for someone quiet and wise… like Gerald. Gerald (nods): I’m Gerald. Jerry Ann: Hubbah hubbah. Symphony: Alright, enough about you– HI EVERYONE, I’m Symphony, and I just know you all already know who I am.

Mikayla: Uh sorry, not to be rude– you know, women support women and all, but I have no idea who you are. Symphony: (huffs) I’m Symphony?! Like “Let’s Sing A Symphony”? I’m the fourteenth most followed influencer on the bird app. Mikayla: Oh, chirper? I love that app! Ryan: Radical! I see a lot of love… in your love for being a chirper influencer, Symphony. Symphony: Thanks, Ryan. I would love for you to teach me how to surf on this beautiful island. Ryan: Hey man, I’m open to that. You and Mikayla are both my type. Host: ALRIGHT, Enough socializing, you five… It’s time for me to tell you the PLOT TWIST of a century! You won’t be able to control your pretty little brains! Mikayla: Eeeee! I hope it’s a couples’ challenge! Or a round of meet and greet truth or dare! Host: Oh no, it’s nothing like that, sweet Mikayla. Jerry Ann: See? It’s going to be something much more mature. For a mature seasoned audience. Host: Indeed, Jerry Ann. On Lover’s Island, you’ll have 14 days to flirt and find your perfect love match here. By the end of day 14, the couple who America loves the most will be voted TOP SURVIVALIST LOVERS! Mikayla: Ooooohh! Host: But the SURPRISE of Lover’s Island is that you will also be fending for your lives, attempting to survive here on this island, just the five of you, with NO additional survival supplies or help from outside people. Jerry Ann: [looks appalled/mad] What the– Symphony:What does that mean, no additional supplies?! You promised I could have my full 28 sets of affiliate marketing bikinis?!? I promised my advertisers I would wear them! Host: Sorry Symphony, but you’ll have 1 swimsuit and 1 swimsuit only. Symphony: FOR FOURTEEN DAYS???? Ryan: I can kinda see the tough love in this.

Gerald: Gerald is not happy. Host: Alright everyone! Good luck and have fun! Don’t try to call… cause there’s no failsafe way out of here! Bye now! Ryan: Wow. That was really unexpected. What do we do now? Jerry Ann: Try to fish for dinner, I guess? [Transition] Host: WELCOME BACK to LOVER’S ISLAND, where we have been watching our lovers flirt and barely feed themselves for five days now… let’s check in on our favorite singles! Mikayla (ragged): water– do you have water? Host: Oh Mikayla, yes I have water! But none for you, silly! How is everyone else? Any love connections? It looks like Jerry Ann and Gerald are getting cozy under a palm frond. Jerry Ann: Gerald, do you think you can use your big arms to lift me up to reach a coconut for dinner today? Gerald: Yes. I am coco-nuts about you. Jerry Ann: Awww, Gerald! Host: Well aren’t they cute! Keep your eyes on them, America. Has anyone seen Symphony? … Symphony? Oh Symphony, where art though Symphony? Symphony: IF YOU DON’T GET MY NAME OUT OF YOUR TREACHEROUS MOUTH Host: WHOA! She is coming in hot over here. Good thing the contestants can’t reach me or evoke physical violence, as I’m floating on a horse-sized drone twenty feet in the air called… [advertisement-like] DRONE-HORSE. The new transport of the future. Available for pre-purchase on Cool Tech Gear dot Com. Symphony: It was one thing for me to be without my phone – the heart and SOUL of my content creation– for 14 days! That I sacrificed, figuring my exposure to national television fame was worth the temporary pause… but to be FIGHTING FOR MY LIFE. I have salt water in places I shouldn’t have salt water! No makeup! No ability to create! I’m dying out here! Host: Dating is about conquering real life together, Symphony. [to the audience] Good thing she’s got a lot of fans at home, cause I don’t think she’d win the popularity vote otherwise. Ryan: But she’d win my popularity vote, man.

Symphony: Ryan is literally the only thing keeping me hanging on right now. Mikayla: Me too. He is this California babe’s love. Symphony: No, he is this Chirper babe’s true love. Ryan: Ladies, ladies, what do I tell you every time we go digging for hermit crabs to eat? Mikayla: [sighs] love is all around Symphony: Right… love is all around… except for you, host. I hope you and the producers never find love. Host: Yow! What a zinger! America, we have got a DRAMA-FILLED show tonight. Stay tuned for the next hour. [Transition] Host: And we’re back, on day 12 of 14. Our survivalists are almost done creating their strongest love bonds ever. What will we find when we fly our drone over this morning? Let’s see now… [drone flying noises/transition] Uh… this doesn’t look good… Symphony: HELP! HELP!! Host: What’s going on? Symphony: Mikayla’s been attacked by a hawaiian monk seal! It ripped off her left forearm! Mikayla: [screaming and waving arms frantically] AHHHHHH! MY FRENCH DIP MANICURE IS RUINED!!!! [stops, looks down at left arm, shocked, then starts screaming again] AND I’M GOING TO DIE! Host: Whoa whoa whoa! We’ve always talked about it but never in history has a Lover’s Island contestant actually died. What do we do? We aren’t supposed to intervene in their survivalist adventures! Mikayla: A MONK SEAL RIPPED MY ARM OFF! IT ATE MY ARM FOR A MID- MORNING SNACK! Host: Well, America, I guess your favorite couple choice will have to be between Gerald and Jerry Ann and Ryan and Symphony. Symphony: Just because Ryan and I like each other, doesn’t mean we can let Mikayla die! Ryan: Yeah man, that’s so not love-centered!

Gerald: Gerald is ANGRY!!!
Host: Listen guys, I don’t make the rules, I’m just here to make my fame and my
paycheck.
Symphony: And so am I!
Jerry Ann: Symphony, you used to be a cheerleader right?
Symphony: Yes, I did! That’s SO not relevant right now, Jerry Ann.
Jerry Ann: [whispers in Symphony’s ear]
Symphony: OHHHHH
Jerry Ann: [turns to look at Gerald] Gerry-bear? A

Gerald: Yes, female Jerrybear? Jerry Ann: Remember what we’ve been planning for the last 10 days? Remember how we got the coconuts down so we wouldn’t starve to death? Gerald: That’s the best part of flirting with you, female Jerry-bear. Jerry Ann: We’re going to do it again, but this time with Symphony [turns to Ryan]… Ryan– hand Symphony your makeshift tree bark surf board. Ryan [to Symphony]: Fine… but be careful with it, my love. Symphony: Got it! Host: [laughs nervously] Heh… I don’t know what they’re doing. Some sort of viking’s funeral for Mikayla’s impending doom? Maybe they’re going to use coconut water to nurture her back to health! Mikayla: [slowly fading to unconsciousness] I actually think coconut water might help right now… Jerry Ann: You’re going to jump on the count of three, Symph. Host: Uh, jump? Symphony: [under breath] I love you, national television fans… Ryan: [under breath] They love you too, Symphony. Jerry Ann: One… two… three… CHIRPER! Symphony: CHIRPER!

Gerald [gets in position with hands clasped together for Symphony to step into his hands and be boosted up into the air] … And Gerald LAUNCHES the skinny human into the air! Symphony: AHHHHH! EAT SURFBOARD, HOST! Host: WHOA, how are you – uh, cameramen?! She is flying pretty high from that cheerleader launch… can you– can anyone– SOMEONE INTERVENE Symphony: HAY- YAH! [smacks host with surfboard] Host: OUCH! She hit me! I’ve got a surfboard welt! I’m losing my balance… I’m toppling off the DRONE-HORSE. Symphony: Sorry, host. The staff doesn’t intervene around here. Host: WHOOAAAAHH!!! [splash into the ocean] Symphony: Alright survivors, I’m landing the DRONE HORSE on the beach. Let’s load Mikayla on and then we can grab our coconuts and go after those cowardly cameramen… Ryan: That was RADICAL, Symphony. Gerald: Yeah! Beaches suck! Mikayla: BUT WAIT– PLEASE! Jerry Ann: Yes, what is it, Mikayla? Anything you need… we’ll help you! Do you have any last wishes in case we don’t make it to a hospital? Mikayla: In case I don’t make it?!? Jerry Ann, get the toxic negativity out of here! A laguna beach babe is built to survive! We have seal attacks all the time there. This is the second time they’ve sown my arm back on… Jerry Ann: Oh, gross. Mikayla: But I do have one question. Symphony: Make it fast, I don’t know how much fuel is left in this DRONE-HORSE. And I really want to livestream my behind-the-scences experience on Chirper as soon as possible. Gerald: Gerald is ready to answer the question. Mikayla: Who do you guys think will win America’s favorite couple? Maybe me and the seal? Ryan: Man… let’s just get off this lover’s island. Symphony: I agree, Ryan. I really don’t feel the love here.
```

---

## IC-1276: Talking to Teddy

- Title: Talking to Teddy
- Author (byline): Jillian Carpenter
- Work: Talking to Teddy
- Publisher: Mushroom Cloud Press
- Publication date as stated: August 15, 2024
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2387
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
Oh… hello! I’m Mary. It’s nice to meet you. You'll have to excuse me a little bit. I haven’t had guests over in quite some time. (show picture) This is Robert. I know I know we look “just like twins.” He used to hate when people said that about us. He always wanted to look just like his father. Of course, there’s nothing wrong with that but you know. Still burns a little bit. Never really was a mama’s boy. Oh, I almost forgot. This is Teddy, Robert’s best friend. He took him everywhere with him. School, home you name it. As a matter of fact, I used to have to fix Teddy a small plate of dinner, make sure Teddy's teeth were brushed every night, make sure he was ready for school… everything. He loved that bear so much that that crazy boy took him in the bath when he was little so Teddy wouldn't be alone for a second. He loved that bear so much. He would talk to him about anything and everything and sometimes when it was just us in the house, I almost think I could hear Teddy respond. I promise I am not crazy. You can probably spot Teddy in every picture I have of Robbie when he was little. They were best friends. Practically brothers. But as he got older and older, people started to get concerned about him.

“Mary, that boy is 16 years old, and he still carries that thing around? Isn’t that a little strange?” Or “When my son wouldn’t give up his pacifier, the doctor said it might be best to take it from him. Think you should do that with that bear?”

People all over town would worry and worry about him...but I wasn’t gonna take it away. That was his best friend… his outlet.

You see… Robert had a hard time during school. His grades were…okay, I guess. But that wasn’t what I was worried about. He… my baby didn't have any friends. He wasn’t a social butterfly and the other kids saw that. He tried so hard to make friends with them but…nothing. There were no playdates or study groups. Every birthday came and went without a party full of friends. It was always just him and Teddy.

I used to get so upset when we’d see kids from school hanging out without him. Like they would always say no to my son but make plans with their little buddies to exclude him. I don’t think it bothered him as much as me though. He used to see how frustrated I’d get and say “Mama don’t be mad. I don’t need them. I’ve got you and dad and Teddy and that’s all I need.” I love how clever he is.

Like I said earlier his grades were… okay. He wasn’t failing terribly but I don’t think that Harvard was gonna be knocking on his door anytime soon. His counselors at school called me in one day to discuss his grades and his future, and as they told me how concerned they were about him; I couldn’t help but look back at my son. His sweet little innocent happy face said everything to me. He was trying so hard, and they were not seeing it. They would say things like

“Maam we are really worried about Robert. If he keeps this trend up his future is not gonna look bright.”

With this, I could only stop and listen. They went on and on and on about how he was not gonna amount to anything or how I should probably search his bedroom for drugs or some such nonsense. But I knew that if I started to fight back, I would say something I regretted. So, I didn’t. I was raised better than that.

This all went on for months. Week after week Robbie would come home disappointed because his tests were not what he thought they would be, but I tried to get him to look on the bright side. While they weren’t what he thought they were, they definitely got better. He would come home every day from school and try to get Teddy to help him with his homework. Who knows, maybe it helped? People started planning graduation parties and we only got one invite from my friend Janet. Her daughter was head of the soccer team and she felt bad leaving him out. I tried to get him to go just so he could enjoy his last night out with his class, but he refused. He wanted to spend it watching movies with me and Teddy. I love him so much.

Finally, after days turning into weeks of waiting for an answer on whether he would graduate, the counselors called me in and told me the most amazing thing, he passed.

I was so excited for him. He worked so hard, and he finally made it. I called his father and let him know the good news and went straight to work trying to find out what college he would go to. But then he surprised me (he was always so good at that.) When I brought up the colleges, he showed me a handful of pamphlets he had picked up from the counselor. She recommended the pamphlets and said they would be good for his future I didn’t think he would have already been too interested but he seemed really excited about it.

Summer went by, and I spent it trying to ensure Robbie was prepared to be away from home. The moms in my support group thought I was crazy to send him away so soon, but I brushed them off. Told them it would be good for him to get some real-world experience. He certainly did not need me there his whole life. It’s good to give your children some space. But when he left, I don’t know, I… I guess I didn't expect it to hit me so hard. I remember I went back to his room and grabbed ahold of Teddy. I couldn't believe he actually left him behind. But he told me he didn't want the other guys making fun of him for carrying around a teddy bear. I could tell that it hurt him to leave Teddy behind, but I promised we would take good care of each other.

Like I said earlier I joined a mom's support group near the end of his senior year. I kind of just did it originally to spend time with my mama friends but now that my baby was gone, they were my support systems. Some of them wept with me while others couldn't help but share their insight on my baby's plans to leave. I know they didn’t think that he could handle it out there, but he tried and that was all that mattered to me.

Somehow, they all concluded that I should write to him. Let him know how I feel. But I didn’t need him to worry. I guess technically, I didn't want him to worry. They came up with so many solutions to my grief but none of them worked.

“Mary get a dog” or “Mary, try and plan a trip with your husband.” Sure, I could do all of that, but none of it would bring him back here to me. Finally, they tried to reason with me and tried to get me to get my feelings out. I’ll never forget what they said. They told me to think back to when he first left and try to think about what I would say to him. “If you could go back in time and tell your son one thing right before he left, what would it be?”

I didn't have an answer for them at the time. I just missed him so much. But now looking back, if I could tell him one thing, I would tell him not to enlist.

I would tell him that me and that counselor would have a few choice words for recommending him to join the army.

I would tell him to not be so excited about those pamphlets because they would end up taking him from me

I would tell him that he was not gonna make a difference in the world and that he wasn't going to prove all of those people at school wrong

I would tell him that his mama was labeled as a killer because of his decision.

I would tell him that his mother has to go back to his room and hold onto that goddamn bear hoping and praying to God that he can hear me when I talk to it

I would tell him that his father and I would hate each other because he didn't want to be married to the person who murdered his son.

But if I could tell him just one thing. I would tell him I’m sorry for being a terrible mother.

He came to me with those pamphlets one day and I just saw one thing:

“U.S Military. We Want You!”

And my selfish heart told him to do it. I was the one who said it would be good for him. He came to me so excited saying that he could make a difference in the world, and I told him yes. Why wouldn’t I? There is nothing wrong with a little discipline in a kid’s heart and all of his schooling would have been paid for. Yeah, I said it would be good for him because I am his mother, and I know what is best for him.

When the news came out that he had passed every single one of those women in my group turned on me. Called me evil. Said that no good mother would send their child off to war. But they don’t know what they're talking about. Their children were all pretty, popular, honors students who didn't have to worry about their futures. They didn't have to worry about affording college because they all had financial aid. They didn't have to sit back and watch every last one

of their classmates exclude them from everything, to where they don’t think they have a purpose in life.

So yeah, I said yes. I said the army would have been good for him. Wouldn't you all have said that if your child was struggling in school? If you were scared that if they didn't find this “life purpose” then they would want to try and end their life? And yeah, I technically don’t owe any of you an explanation on my parenting, but I will tell you... that before you all jump in and criticize me just know that if I had known what was gonna happen to my sweet little angel baby then I wouldn't have sent him off. I may not be a perfect mother, but I am still his mother. Not you, not any of you. You didn't know him like I did and if any of you were in my shoes you would have said the exact same thing.

The people in my group and at church would tell me that he was in a better place. That this was all a part of God’s plan. But you know what, I am done with hearing that. I have been praying and giving back to the church for as long as I can remember and yet this is what happens. All of my time and energy went into serving my family and my community for the sake of God and this is how I am repaid. I am sick of everyone saying it is all a part of God’s plan. God planned that he was gonna be bullied his whole life. God planned that he struggled in school. God planned that he would leave my home. God planned that he would pass away. God planned that I was never gonna see him again. If this is all a part of God’s plan… then why was his plan to make me more miserable than anyone I knew? He could have done this to anyone why did he have to choose me and my family? It was his way of telling me I was not a good enough Christian, a good enough mother, or a good enough person. I tried but I failed. And that in God’s mind, I am a disappointment.

You know… I'm not mad at him. Why would I be? It wasn’t his fault. I'm not mad at all of those people who I thought had my back when he died. I’m not mad at those counselors or classmates who made him want to join the army. Heck, I’m not even mad at the army. People told me to channel my anger at them but why would I? They fight for a good cause that my son wanted to be a part of. They didn't know that he was destined to die. I’m not even mad at his father for the divorce.

If anything,… I’m mad at myself.

I’m not perfect, I don’t claim to be perfect or a perfect mom. I made a mistake. I ruined lives because I made one simple mistake. I said yes. I could have said no and found a way to help him pay for college and get him more involved in the community. But then I would have been accused of “coddling him.” Forget that. I don’t care what they think. I care about him. And I know that if I could give anything, I would give my whole life to the Lord if it meant that he was here, and I wasn’t.

A killer must be punished, and I was. I killed my son. My one reason for living is gone. So, I guess I deserve it.

(to Teddy) It’s just you and me bud. I am so sorry I killed your best friend. I didn’t mean to, but I did and I am so sorry. I miss him too, but all we have is each other. And you know what… I’m happy with that. I think you know Robert better than anyone in this world. You always had an easier time getting him to open up than I did. You two were brothers. Could you tell me about him?
```

---

## IC-1277: We Had Chemistry

- Title: We Had Chemistry
- Author (byline): Tracy Nuss
- Work: We Had Chemistry
- Publisher: Mushroom Cloud Press
- Publication date as stated: August 15, 2024
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1110
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
For Jayla C.

Synopsis: A high school girl finds herself in the school counselor's office to recount the day's events. Normally, she’s the peak of near perfection but today she found herself distracted by… a boy. She proceeds to tell the story of one comedic disaster after another that happened in Chemistry class that day.

Ms. Smith, as a school counselor, have you ever seen a perfectly, intelligent girl suddenly go dumb because of a boy? Take any girl and ask her the capital of Nicaragua and she'll tell you the correct answer in the blink of an eye. Ask her to add two plus two in front of a boy and she'll tell you five... It's the most insane thing ever. I can't stand it when I watch my friends completely forget themselves anytime a 6-foot bag of muscles with brown hair and blue eyes walks up. Long ago, I made myself a promise I would never be that girl. To this day, you know that I've carried a 4.0 grade point average. I scored a 35 on the ACT. As a junior, I've already been accepted into four different universities and have been offered several substantial scholarships. So, Ms. Smith, you have to believe me when I say, I have no idea what happened during 5th hour...

Let me set the scene for you. (She begins to act out the scene in the office) We had a lab in Chemistry. Something simple. It was a standard single replacement reaction where we were supposed to combine magnesium and hydrochloric acid which would produce a gas. Then we had to light a small wooden stick on fire and introduce it to the gas to get it to pop which would confirm it's hydrogen gas. Like I said, easy. The problems all started when Casey, my bff, decided to be sick today. It left me without a partner and Mr. Daniels decided that it would be best that, despite my protests, I should have a new partner instead of working on my own. Mr. Daniels decided to put me with Steven of all people... I mean, he's alright but he's no Casey. She and I had the two highest grades in the class. I trusted her... Why was I supposed to trust my lab score with this six-foot-tall bag of muscle, with brown hair, and blue eyes, that I've had a crush on since the 4th grade?... (she immediately catchers her slip) I've never said that out loud before... See Ms. Smith, something’s wrong with me.

Anyway, we divided up the work. I sent him to get the lab supplies while I prepared the burner. I turned on the gas and started adjusting the airflow when I found myself watching Steven walk away. I want to say it's because I didn't trust him to grab the right materials and the right amounts, and, honestly, that was mostly the reason. But Ms. Smith, I found myself looking at... his b.... his buh... Ms. Smith, I've taken anatomy. I know the proper terminology for 98% of the parts of the human body. I was the only one in my class who could list off EVERY part of the reproductive system without turning red or giggling... Right now, I can't even say the general term for the space between Steven's lower back and his hamstrings. During this time, I must have absent-mindedly adjusted the airflow a little much. As I lit the burner, there was this huge fireball! It ignited part of the counter, the ceiling tiles, and worst of all, my trigonometry homework! I spent three hours working on it the night before and I couldn't have it, literally, going up in flames! I quickly grabbed a fire extinguisher and put it out. In a few short bursts, I had most of it put out and then it got worse.

As I was just about to finish up, I was startled by a tap on my shoulder. I jerked around and at the same time, I squeezed the extinguisher one more time. I fired it directly at Steven who was trying to get my attention... while he was still holding concentrated hydrochloric acid... which he then proceeded to dump all over himself. I heard it start to sizzle... According to Mr. Daniels, in 23 years of teaching, he has never had to use the safety shower... until today. Ms. Smith, do you know the protocol for a chemical spill? You have to remove any affected clothing! Mr. Daniels comes over and gets Steven to take off his shirt and positions him under the shower. Steven is now shirtless… under a shower in the classroom... I couldn't look away... Ms. Smith, it was bad and so embarrassing. I wish I could say it ended there...

I felt compelled to tell Steven that I was sorry. I walked over to him forgetting that the floor was wet from the shower... I slipped... into him. He caught me and we both fell to the ground. When I opened my eyes, I was on top of him. I waited what seemed like hours for Steven to open his eyes. He didn't. I must have knocked him out! Ms. Smith, I'm trained in CPR. I've worked as a lifeguard. My instincts kicked in. I was going to have to start rescue breaths! I brought my mouth in close to give the breath of life... or a kiss. I don't really know any more at this point. I was about a centimeter away from contact when he opened his eyes... It turns out the time that passed was only about 5 seconds... He was fine. I got up and sprinted out of the room and now two hours later, I'm here.

So, needless to say, Ms. Smith, I'm here to formally request you start the paperwork so I can transfer to a new school. First of all, I cannot show my face around here ever again and definitely cannot show my face to Steven ever again. Second of all, I cannot have these types of distractions with the kinds of goals I have in mind. Never in my right mind did I ever think I would behave like this. I think there's an all-girls school on the other side of the city. Anyway, thanks for listening Ms. Smith. I have a detention I need to go serve. Mr. Daniels said it should only take about an hour to clean up the lab and then I can go home... Oh, Ms. Smith? If you happen to see Steven, can you tell him I'm sorry, and if he's not doing anything in about 8-10 years I'll look him up?
```

---

## IC-1278: My Boyfriend’s Back and There’s Gonna be Laundry

- Title: My Boyfriend’s Back and There’s Gonna be Laundry
- Author (byline): Sandra Shamas
- Work: Sandra Shamas: A Trilogy of Performances
- Publisher: Mercury Press
- Publication date as stated: Mar 1998
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: SANDRA, GUSHING WOMAN, FRANK
- Teaser before the introduction: Yes
- Spoken words (computed): 2066
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sandra Shamas
Book: Sandra Shamas: A Trilogy of Performances
ISBN: 978-1551280448
Publisher: Mercury Press
Date (Month/Year): Mar 1998
```

### Introduction (context only: never use it for content warnings)

```text
Being single sucks. Feeling as if you are not wanted, wondering if you are, in fact, too needy, expect too much, or aren’t worthy of being with anyone period. It’s a battle virtually every woman has had to conquer. But Sandra Shamas brings this single-womanhood dilemma home better than anyone else. Join me for a couple of weeks in the life of a single woman and I think you’ll recognize exactly where she’s coming from.

My Boyfriend’s Back and There’s Gonna be Laundry by Sandra Shamas
```

### Performance text (classify this)

```text
SANDRA: I'd like to start the evening off by offering you a performance art piece. I'm holding in my hands a sturdy pair of men's cotton briefs. Now, many of you won't even recognize these; so nice and flat and white, like this. Maybe I can help you recognize them, if I wad them up into a tight angry little ball. Maybe you'll recognize them better in their natural habitat: the floor.

SANDRA: Now, when you go to the magazine rack and you see the entire world of magazines that are available to women, all these magazines are pretty much the same. There's a wide variety of topics on each cover. You find "Fashion Tips," "Thin Thighs in 30 Days," "Lose 30 Pounds in Two Weeks," or little psychological pieces like "Five Things Men Fear." Inevitably, on the front cover of one of these magazines, there'll be an article entitled something like, "The Joy of Being Single." Biggest oxymoron in the world. A contradiction in terms. Like "jumbo shrimp," or "military intelligence.”

Now, these articles are there to help you be better at being single. 'Cause you're just not doing a good enough job. And they make suggestions to single women like, "take brisk walks," and "don't be afraid to dine alone." Have you ever done this? Have you ever dined alone? Okay. You go. You're upright. You're bathed. You're dressed.

You're standing in front of the "Please wait to be seated" sign. The hostess comes over with a fan of menus, and she gives you that "Oh, you-poor-piece-of-s***, you-couldn't-find-anybody-to-eat-with-you" look, takes you to a table for two by the toilet, hands you one menu, and then abandons you. Because whatever you've got might be catching.

I eat over the sink. I dine alone with the sink. The nice, stainless steel placemat for one. I take the pot off the stove. I go to the sink. And I dine alone! But when I decided to be single, I envisioned my singledom to be a lot more romantic. In my singleness, I was a little taller, and willowy. And I wore a lot of white, gauzy cotton clothes that wafted around me. And my hair was shorter, but tawny-coloured. And I don't even know what colour that is. But whenever I read a Harlequin romance, the heroine always has "green, flashing eyes, and tawny hair." I WANT IT! So, what happens? What happens? You know, I turned my head away for a second, and into my life walks this guy. The one. He was, the one. How did I know he was the one? Because when I looked at this guy, I heard an operatic version of Star Trek music in my head. He was tall and lean and blond, blue-eyed, funny, bright, articulate . . . and younger. You get them young, you can train them. And his name was Frank. I fell in love with Frank. Now, I don't know about you, but when I fall in love, I give my brain . . . AWAY.

Nobody -- especially other single women -- wants to be around a woman who has just fallen in love. No. Well, you know why. It's because her voice goes up three octaves, it takes on a sickening sing-songy quality, and the sum total of her conversation is:

GUSHING WOMAN: And then you know what else he said? And he's so funny, and he's so smart. And, also, he's not like any man I've ever met before in my whole life. And he's so smart and he's so funny. You know what he said?

SANDRA: AH, SHUT UP! So there I was. I was in love love love love love. So, one day, the phone rings. "Hello." (It's Frank.) "Hiyee. How are you? What? Oh, I'd love to get together. It's so funny' cause I was just thinking about you and then the phone rings.

Weird, eh? .. What? No, let's get together. I'd love that. Let's have coffee. Yeah . . . I know where it is . . . Yeah. I can be there in fifteen minutes . . . No problem. Okay. Bye . . . What? Oh, I'd love to talk to you, too . . . Okay . . . I'll see you there in fifteen . . . Okay. Bye-bye. . ." (pause) "Uh? No, you hang up first. Okay, we'll count together. "One . . . two . . . " I go to the cafe. Frank is already there. He is already sitting at a table for two. He has already ordered coffee. He's very handsome. And so I go and sit across from him. "Hello!" And he says seriously,

FRANK: Hi . . . um . . . thanks, ah . . . thanks very much for coming.

SANDRA: No trouble.

FRANK: Look, um . . . there's no easy way for me to say this . . .

SANDRA: Oh, then don't say it.

FRANK: Yeah, um . . . you know, ah . . . you know, I've, ah . . . I've been doing some thinking. . . and, ah. . . something I want you to know, it's not you, you know. But I really feel like things are going way too fast for me right now and I'm not ready, at all, to make any kind . . . of emotional . . . com . . . mit. . . ment.

SANDRA: Well, sing along if you know the words. Right away all the blood in my body went right into my head, and I could hear my heart in my ears. And nausea. And I'm looking right at him as hard as I can, I'm looking dead at him, and all I see is his mouth moving and no sound coming out. That voice in my head and says,

VOICE IN S’s HEAD: "DON’T LET *HIM* SEE YOU CRY!”

SANDRA: Tears come. (to herself) I can't help it. I can't help it.

VOICE IN S’s HEAD: STAND UP!

SANDRA: Okay. I'm up . . .

VOICE IN S’s HEAD: GO TO THE DOOR!

SANDRA: I don't know where the door is!

VOICE IN S’s HEAD: IT'S OVER THERE!

SANDRA: Oh, please. Please. What if he changes his mind?

VOICE IN S’s HEAD: HE HASN'T GOT A MIND TO CHANGE! GET OUTTA HERE!

SANDRA: So, where do you go? Where do you go when somebody says, "I'm not here for you anymore? Sorry!" Where do you go? Well, I don't know about you, but I like to turn my head down the path of self-destruction.

I'm diggin' in. I'm diggin' in for Stinky Pyjama Time. Stinky Pyjama Time. Maybe you know it. It does not have to be pyjamas. It can be bad track pants. Regardless, the outfit is a legged garment with the crotch way down around your knees. And you wear that with a completely mismatched top. Oh, [and] we never bathe during Stinky Pyjama Time. We never shave our legs. And if you're in SPT long enough, you can actually get the hair on your legs to start doing that giant kelp action in the tub.

Two weeks. Two weeks go by, and every day, I walk up and down the hall, crying. Sometimes, the phone would ring. I would answer it, but before I could talk I'd have to cough up a big hairball so the words could come out.

(on the phone) Hello? Oh, hi, Maria . . . No, no, man, I can't go out. . . Oh, yeah? . . . Yeah? . . . Where did you see him? . . . Oh, you had a party? At your house? . . . I didn't know you were having a party . . . Oh, yeah? . . . Maria, did it look like he was with somebody? . . . Oh, yeah? . . . Did it look like he'd been crying for two weeks?"

No.

Now, whenever I want to take my mind off love lost, I do the laundry. I don't know what it is; I think it's just my need to be clean or to be in the basement communing with trolls. One or the other. Or both.

Now I'm still deep in Stinky Pyjama mode, but the light at the end of the tunnel comes by way of a fresh basket of laundry I've just done. So, the ironing board goes up. The iron starts getting hot. And I'm rummaging around in the basket . . . and whose shirt comes out? Frank's.

So, I lay it really lovingly on the ironing board, and I think, Okay, he'll see that this shirt is not at his house, and he'll come here. And he'll come here and he'll see that it's here and that I ironed it, and he'll say, "Oh, Sandra, I should never have left you because you're such a good ironer.

NEVER! Never, never, ever has a man gone for a woman because of her domestic prowess.

So, I'm at the board and I'm feeling so sad. And I'm crying and crying, and I'm thinking, It's me. It's because if me. If I were way more excellent, he would never have left. That's it. If I were way more excellent, he would never have left.

Think of something else! Think of something else . . . The phone rings. I shuffle over. "Hello." (It's Frank) "Oh, hello . . . No, I don't mind you calling . . . No, I wasn't doing anything, I was just, um . . . standing . . . How am I? Oh, I'm fine . . . Couldn't be better . . . Meet you for coffee? .. Yeah, I suppose I could meet you. . .in fifteen minutes . . . " (I catch a whiff of myself) "Make it sixteen . . . Okay . . . Bye."

Come on, Sandra, pull yourself together . . . C'mon. You can do it. . . I wanna go because I wanna see him but I don't wanna go because I'm afraid. No, I'm gonna cry . . . No. No. No crying. No crying!

So, I'm out the door, going towards the cafe, and I'm doing that shuffling, crying s***, you know, where there's heavy snot bubble action. I'm afraid to see him, but then I figure, he can only dump me once. I get to the cafe, and Frank is already sitting there at our table for two. He's already ordered coffee. He's very handsome, and he's beckoning for me to join him, so I do.

So, I sit across from him, and he says,

FRANK: Hi. Hi. It's really good to see you. You know . . . the last two weeks have been pretty hard on me. I was at the bookshop and I saw a book you were looking for and I knew you would love it and . . . uh . . . I couldn't call you. And late at night if I couldn't get to sleep, I'd go for a walk and sometimes I'd pass in front of your house and I'd see the light on in the living room and I'd think, maybe if I just looked in the window, I'd get to see her. . . . the truth of it is . . . I didn't expect to miss you . . . and I did. And I know I've got no right to ask, and I know I sound like a jerk, . . . but, is there any way you can see past what's happened and maybe give us a second . . .

SANDRA: "YES!" . . . chance?"

SANDRA: You know, I like to think I hesitated a milli-second on that. So, we sat and we talked and talked and talked and talked and when the waitress came over, I put my brain on her tray. We had coffee after coffee after coffee and Frank quickly said

FRANK: Listen, do you want to go for a walk?

SANDRA: And we went out into that near perfect autumn night: clear, stars, crisp, beautiful. We walked and talked and walked and we ended up in front of my house. (to Frank) Gee, Frank, you know . . . do you feel like coming in and having a coffee? (to audience) So, we both go into the house and it's incredibly awkward. A remarkably awkward moment: we're standing in the living room and we both have our coats on. So Frank says, in an effort to break the ice,

FRANK: Why don't we see what's on TV?

SANDRA: Yeah, that's a great idea. (to audience) And we both reach down for the converter at the very same time, and our hands touch, and there's like this arc of electricity. Frank says,

FRANK: THE LAST ONE TO THE BEDROOM'S A DIRTY ROTTEN EGG!

SANDRA: And the bed has fresh sheets. I just did the laundry. Sometimes, God says "Yes."

The next morning, he had an early call, and he was gone at about seven. So I was alone in bed, and I was in that warm, rosy glow that only women really know. And I was so happy that my boyfriend was back. (Yay! Yay!) And I sat up in bed to start my day, and I just happened to look down on the floor. And there, there in the corner of the bedroom, on the floor, was his dirty underwear. And I thought to myself, Oh, I get it. My boyfriend's back, and there's gonna be laundry.
```

---

## IC-1279: My Stepmother, Myself

- Title: My Stepmother, Myself
- Author (byline): Garrison Keillor
- Work: Happy to Be Here
- Publisher: Penguin Books
- Publication date as stated: April 1990
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NEWSCASTER, SNOW, GRETEL, CINDERELLA
- Teaser before the introduction: Yes
- Spoken words (computed): 1450
- Already set (do not supply): none

### Source block (context only)

```text
Author: Garrison Keillor
Book: Happy to Be Here
ISBN: 978-0140131826
Publisher: Penguin Books
Date (Month/Year): April 1990
```

### Introduction (context only: never use it for content warnings)

```text
My Stepmother, Myself by Garrison Keillor
```

### Performance text (classify this)

```text
NEWSCASTER: (Pg 183-188) Recently in Pennsylvania, a woman was dismissed from her job and driven over a cliff by an angry mob of villagers carrying flaming torches and hurling sharp rocks after they learned that she was married to a man who had custody of his three children by a previous marriage.

In California, soon after her marriage to a prince, Sharon Mittel was shut up in a dungeon under the provisions of the Cruel and Unnatural Parent Act, which allows the immediate imprisonment of a stepparent upon the complaint of a stepchild. The prince's oldest daughter accused Sharon of slapping her. She now faces a series of tests to prove her innocence. She also must answer some riddles.

Are these merely two isolated incidents? Or are they, as a new and exhaustive report on stepmothers points out, fairly indicative?

"The myth of the evil stepmother is still with us. Stepmothers are still associated with the words cruel and wicked, which has made them easy targets for torture and banishment as well as severely limiting their employment, particularly in professions such as nursing, social work, and education. In general, stepmothers are not only underpaid and underemployed but also feared and despised."

Recently, three stepdaughters whose relationships with their stepmothers are well known agreed to speak out and set the record straight. Because each has suffered from publicity in the past and is trying to lead a normal a life, only first names will be used.

SNOW: The story the press told was that I was that I escaped from stepmother and was taken in by dwarves and she found me and poisoned me with an apple, and I was dead and the prince fell in love with me and brought me back to life and we got married, et cetera, et cetera. And this is what I believed right up to the day I walked out on him. I felt like I owed my life to Jeff because he had begged the dwarves for my body and carried it away and so the apple was shaken loose from my throat. That's why I married him. Out of gratitude.

As I look back on it, I can see that that was a very poor basis for a relationship. I was traumatized, I had been lying in a coffin under glass for years, and I got up and married the first guy I laid eyes on. The big prince. My hero.

Now I can see how sick our marriage was. He was always begging me to lie still and close my eyes and hold my breath. He could only relate to me as a dead person. He couldn't accept me as a living woman with needs and desires of my own. It is very hard for a woman to come to terms with the fact that her husband is a necrophiliac, because, of course, when it all starts, you aren't aware of what's going on -- you're dead.

In trying to come to terms with myself, I've had to come to terms with my stepmother and her envy of my beauty, which made our relationship so destructive. She was a victim of the male attitude that prizes youth over maturity when it comes to women. Men can't dominate the mature woman, so they equate youth with beauty. In fact, she was beautiful, but the mirror (which, of course, reflected that male attitude) presented her with a poor self-image and turned her against me.

But the press never wrote the truth about that. Or about the dwarves. All I can say is that they should have been named Dopey, Sleepy, Slimy, Sleazy, Dirty, Disgusting, and Sexist. The fact is that I knew the apple was poisoned. For me, it was the only way out.

GRETEL: When Hansel and I negotiated the sale of book rights to Grimm Bros., he and I retained the right of final approval of the manuscript and agreed to split the proceeds fifty-fifty. We shook hands on it and I thought the deal was set, but then his lawyers put me under a spell, and when I woke up, they had rewritten the contract and the book too! I couldn't believe it! Not only did the new contract cut me out but the book was pure fiction.

Suddenly he was portrayed as the strong and resourceful one, a regular little knight, and I came off as a weak sister. Dad was shown as a loving father who was talked into aban-doning us in the forest by Gladys, our "wicked" stepmother. Nothing could be further from the truth.

My brother was a basket case from the moment the birds ate his breadcrumbs. He lay down in a heap and whimpered, and I had to slap him a couple times hard to make him walk. Now the little wiener makes himself out to be the hero who kept telling me, "Don't cry, Gretel." Ha! The only crying I did was from sheer exhaustion carrying him on my back.

As for Dad, he was no bleeding heart. He was very much into that whole woodcutter/ peasant/ yeoman scene -- cockfighting, bullbaiting, going to the village to get drunk and watch a garroting or a boiling -- don't kid yourself! Gladys couldn't send us to our rooms without his say-so. The truth is that he was in favor of the forest idea from the word go.

What I can't understand is why they had to lie about it. Many parents left their children in the forest in those days. It was nothing unusual. Nowadays, we tend to forget that famine can be a very difficult experience for a family. For many parents, ditching the kids was not only a solution, it was an act of faith. They believed that ravens would bring morsels of food, or that wolves would take care of the kids, or a frog would, or that the fairies would step in. Dwarves, a hermit, a band of pilgrims, a kindly shepherd, somebody. And they were right.

I don't mean to say that it wasn't a trying experience, an emotional experience. It was. And yet there isn't a single documented case of a child left in the forest who suffered any lasting damage. You look at those children today and you will find they are better people for having gone through it. Except for my brother, that is. The little jerk. He and my father live in luxurious manors, and I live above an alchemist's shop in a tiny garret they call a condo. As for Gladys, she was kicked out without so much as a property settlement. She didn't even get half of the hut.

I guess, back then, I wasn't prepared to see that Gladys, in proposing the forest as a viable alternative, was offering me independence at a very early age. I wish I had been able to thank her.

CINDERELLA: A woman in my position does not find it easy to "come out of the palace," so to speak, and to provide intimate details of her personal life. I do so only because I believe it is time to put the Cinderella myth to rest once and for all -- the myth that one can escape housework by marrying a prince.

The truth is that I am busier than ever. Supervising a large household staff -- cooks, maids, footmen, ladies-in-waiting, a bard or two -- is hard work. Often I find myself longing for the "good old days" when my stepmother made me sweep the hearth.

We see each other almost every day -- she comes up here and we play tennis or I go down there for lunch -- and we often reminisce and laugh about our little disagreements. She is one of my best friends. Other people treat me like royalty, but she treats me like a real person. My husband won't let me touch a broom, but I go to her house and she puts me to work! I love it. I tell her, "Mother, you're the only one who yells at me. Don't ever stop." And I mean it. Anger is real. It's honest.

Honesty is a rare commodity in a palace, and that is why so many "fairy-tale" marriages end up on the rocks. You wouldn't believe the amount of fawning and flattering that goes on! Between the courtiers bowing and scraping and the suppliants and petitioners wheedling and whining, and the scheming of bishops and barons, not to mention the sorcery and witchcraft, the atmosphere is such that it's terribly hard for a man and a woman to establish a loving, trusting, sharing type of relationship . . . It's true that we lived happily ever after, but believe me, we have had to work at it!
```

---

## IC-1280: Naomi in the Living Room

- Title: Naomi in the Living Room
- Author (byline): Christopher Durang
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Jan 1998
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NAOMI, JOHN, JOHNNA
- Teaser before the introduction: No
- Spoken words (computed): 1695
- Already set (do not supply): none

### Source block (context only)

```text
Author: Christopher Durang
ISBN: 978-0822214489
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
Sometimes one of the most difficult things about being married is not the marriage itself, but the in-laws that come with it. If you have been having a hard time dealing with your mother-in-law, you haven’t seen anything yet. Meet Naomi . . . Joanna’s mother-in-law. One moment she’s nice as pie, the next she’s jumping on top of furniture, pulling out her hair, and screaming at the top of her lungs. Poor Johnna finds herself trapped in the absolute craziness of the family she married into during a visit with . . .

Naomi in the Living Room by Christopher Durang

SCENE: A living room. Enter NAOMI, followed by JOHN and JOHNNA, an attractive young couple. JOHN has a moustache and is dressed in a suit and tie. JOHNNA is wearing a dress with a string of pearls. NAOMI, though, looks odd. NAOMI plants herself somewhere definitive - by the mantelpiece, for instance - and gestures out toward the room.
```

### Performance text (classify this)

```text
NAOMI: And this is the living room. And you've seen the dining room, and the bedroom, and the bathroom.

JOHN: Yes, I know. I used to live here.

NAOMI: The dining room is where we dine. The bedroom is where we go to bed. The bathroom is where we take a bath. The kitchen is where we ... cook. That doesn't sound right. The kitchen is where we ... collect kitsch. Hummel figurines, Statue of Liberty salt and pepper shakers, underpants that say Home of the Whopper, and so on. Kitsch. The kitchen is where we look at kitsch. The laundry room is where we do laundry. And the living room is where Hubert and I do all of our living. Our major living. So that's the living room.

JOHNNA: What do you use the cellar for?

NAOMI: [suspicious] What?

JOHNNA: What do you use the cellar for?

NAOMI: We use the cellar to . . . we go to the cellar to . . . replenish our cells. We go to the attic to . . . practice our tics, our facial tics. [face contorts] And we go to the carport, to port the car. Whew! Please don't ask me any more questions, I'm afraid I may not have the strength to find the answers. [laughs] Please, sit down, don't let my manner make you uncomfortable. Sit on one of the sitting devices, we use them for sitting in the living room. [JOHN and JOHNNA go to sit on the couch]

NAOMI: [screams] DON'T SIT THERE, I WANT TO SIT THERE!!! [JOHN and JOHNNA look frightened. NAOMI charges to the couch] Shits! Ingrates! It's my house, it's my living room. I didn't ask you, I can ask you to leave. [JOHN and JOHNNA start to edge out of the room] No, no, sit down. Please, make yourselves at home, this is the living room, it's where Rupert and I do all our living. [JOHNNA sits in the chair, and JOHN stands behind her --NAOMI stretches her arms out on the couch] Wow. Boy oh boy. I need a big couch to sit on because I'M A BIG PERSONALITY!!!! [laughs] Tell me, are you two ever going to speak, or do I just have to go on and on by myself, or WHAT!!!!!! [stares at them intensely; they hesitate but then speak]

JOHNNA: This is a very comfortable chair. I love it.

NAOMI: Go on.

JOHNNA: Ummmm, this morning I washed my hair, and then I dryed it. And we had coffee in the kitchen. [pause, doesn't know what to say] And I love sitting in this chair.

NAOMI: I think I want to sit in it, get up, get up. [charges over, JOHN and JOHNNA move away, uncomfortable. NAOMI sits and moves around in the chair, luxuriating in it] Hmmmm, yes. Chair, chair. Chair in the living room. Hmmm, yes. [shouts at them] Well, go sit down on the couch, you morons! [screams off-stage] Leonard! Oh, Leonard! Come on in here in the living room and have some conversation with us. You don't want me to soak up everything our son says all by myself, do you? [stands and walks over to the couch. Smiles at JOHNNA] You probably didn't know John was Herbert's and my son, did you?

JOHNNA: Yes, he told me. I've met you before, you know.

NAOMI: Shut up! [calls out] Hubert! Rupert! Leonard! [to them] I hope he's not dead. I wouldn't know what room to put him in. We don't have a dead room. [smiles; screams] AAAAAAA- AAAAHHH! [looks at them] Goodness, my moods switch quickly. Tell me all about yourselves, do you have children? [listens attentively]

JOHNNA: We had five children, but they all died in a car accident. The babysitter was taking them for a ride, and she was drunk. We were very upset.

NAOMI: Uh huh. Do you like sitting on the couch?

JOHN: Mother, Johnna was telling you something sad.

NAOMI: Was she? I'm sorry, Johnna, tell it to me again.

JOHNNA: We had five children . . .

NAOMI: [Tries to concentrate, but] Wait a minute, something's bothering me!!!! [rushes over to a stuffed Santa pig on the mantel, snatches it up and throws it against the wall in a fury] This belongs in the kitchen, not in the living room. The living room is for living, it is not meant for sincerely designed but ludicrously corny artifacts! Kitsch! Do you like Hummel figurines?

JOHN: Very much. Now that the children are dead, Johnna and I have begun to collect Hummel figurines.

NAOMI: Uh, huh, isn't that interesting? Excuse me if I fall asleep. I'm not tired yet, but I just want to apologize in advance in case your boring talk puts me to sleep. I don't want to offend you. [screams] AAAAAAAAAAAAHHHHHHHH! I'm so bored I could scream. Did you ever hear that expression? AAAAAAAAAAAAHHHHHHHH!

JOHN: Excuse me, I want to change my clothes. I'm tired of my color scheme. I'll be right back. [exits]

JOHNNA: He's constantly talking about his color scheme. It's my cross to bear, I guess. That and the death of the children.

NAOMI: So who are you, anyway?

JOHNNA: I'm Johnna. I'm married to your son. All our children recently were killed.

NAOMI: Stop talking about your children, I heard you the first time. God, some people can't get over their own little personal tragedies, what a great big crashing boor. Lots of people have it worse, girlie! [calls off-stage] Hey, John, where did you get this turd of a wife, at the Salvation Army? I'd bring her back! [laughs maniacally]

JOHNNA: I think I want to go.

NAOMI: Boy, you can't take criticism, can you? This is the conversation pit. You can't leave the pit until you converse on at least five subjects with me. Starting now, go: [waits expectantly]

JOHNNA: I was reading about Dan Quayle's [Replace with current VP] grandmother the other day.

NAOMI: That's one. Go on.

JOHNNA: She said there should be prayer in the schools ...

NAOMI: That's two. [starts to massage her feet]

JOHNNA: And that we should have a strong defense ...

NAOMI: That's three.

JOHNNA: And that the Supreme Court should [was right to] repeal the Wade vs. Roe ruling that legalized abortions.

NAOMI: That's four.

JOHNNA: And that even in the case of pregnancy from incest, the woman should be forced to carry the child through to term.

NAOMI: That's four-A

JOHNNA: And then she said she hoped the mother would be forced to suffer and slave over a horrible job and take home a tiny teeny paycheck to pay for some hovel somewhere, and live in squalor with the teeny tiny baby, and that then she hoped she'd be sorry she ever had sexual intercourse.

NAOMI: That's still four-A.

JOHNNA: Don't you think she's lacking in Christian charity?

NAOMI: That's five, kind of. Yes, I do. But then so few people are true Christians anymore. I know I'm not. I'm psychotic. Get up off the couch, I want to sit there. [rushes over, JOHANNA has to vacate fast. NAOMI starts to luxuriate in sitting in the couch, moving sensuously] Oh, couch, couch, big couch in the living room, you are my manifest destiny. Mmmmm, yes, yes. [to JOHNNA] Tell me, can you switch moods like I can? Go ahead, try.

JOHNNA: Very well. [happy] I'm so happy, I'm so happy. [screams] AAAAAAAH! Do you have chocolates for me? [desperate] I'm so sad, I'm so sad. Drop dead! [laughs hysterically] Aha-hahahahahahaha! That's a good one!

NAOMI: Very phoney, I didn't believe you for a moment. [changes subject abruptly] I don't understand politics, do you?

JOHNNA: Politics?

NAOMI: Politics, politics! What, are you deaf? Are you stupid? [Enter JOHN dressed just like JOHNNA - the same dress, pearls, stockings, shoes. He has shaved off his moustache, and he wears a wig with a bow in it like the one she has in her hair. They look very similar]

NAOMI: You took off your moustache.

JOHN: I just feel so much better this way.

JOHNNA: [embarrassed] John and I are in couples therapy because of this. Dr. Cucharacha says his cross-dressing is an intense kind of co-dependence.

NAOMI: If this Dr. Cucharacha cross-dresses, I wouldn't see him. That's what John here is doing. Too many men in women's clothing, nothing gets done!

JOHNNA: Why do you humiliate me so this way?

JOHN: [to Johnna] I want to be just like you. Say something so I can copy you.

JOHNNA: Oh, John. [looks away with a feminine gesture]

JOHN: Oh, John. [imitates her gesture] That doesn't give me much. Say something else.

JOHNNA: Maybe it's in your genes.

JOHN: Maybe it's in your genes.

NAOMI: This is a disgusting sight. I find this uncomfortable. Makes me want to vomit.

JOHNNA: Maybe we should go.

JOHN: Maybe we should go.

NAOMI: [upset] How come you don't dress like me? How come you dress like her?

JOHN: I want to be noticed, but I don't want to be considered insane.

JOHNNA: John, please, just stay quiet and pose if you must, but no more talking.

NAOMI: Insane? Is he referring to someone in this room as insane? [calls] Sally! Gretchen! Marsha! Felicity! [to them] I'm calling my army in here, and then we'll have some dead bodies.

JOHNNA: Maybe we should go.

JOHN: Maybe we should go. [keeps imitating JOHNNA's movement]

JOHNNA: Will you stop that?

NAOMI: Insane, I'll give you insane! What's the capital of Madagascar? You don't know, do you? Now who's insane? What's the square root of 347? You don't know, do you? Well, get out of here, if you think I'm so crazy. If you want to dress like her and not like me, I don't want you here. [JOHN begins to walk back and forth around the room, pretending he's on a fashion runway. JOHNNA covers her eyes] I can have Christmas by myself, I can wait for Santa by myself. I can bob for apples. By myself! Do you get it? You're dead meat with me, both of you. Leave here. I don't need you, and you're dead! [pause]

JOHNNA: Well, I guess we should be going.

JOHN: Well, I guess we should be going. [JOHNNA and JOHN, looking the same and walking the same, leave the house. NAOMI chases them to the door]

NAOMI: *Nuts to* you and the horse you came in on! [JOHN and JOHNNA exit. NAOMI comes back into the room and lets out enormous, heartfelt sobs. When they subside she seems to be fairly content] Well, that was a nice visit.
```
