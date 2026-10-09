# Classification request: batch 23 of 53 (40 records, IC-1281 to IC-1320)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-023-reply.json`.

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

## IC-1281: New York Regional Mormon Singles Halloween Dance

- Title: New York Regional Mormon Singles Halloween Dance
- Author (byline): Elna Baker
- Work: Not specified
- Publisher: Dutton Adult
- Publication date as stated: Oct 2009
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: ELNA, MOTHER, FATHER, FRIEND, RANDOM MALE, CHURCH MAN, DAVE
- Teaser before the introduction: Yes
- Spoken words (computed): 1924
- Already set (do not supply): none

### Source block (context only)

```text
Author: Elna Baker
ISBN: 978-0525951353
Publisher: Dutton Adult
Date (Month/Year): Oct 2009
```

### Introduction (context only: never use it for content warnings)

```text
New York Regional Mormon Singles Halloween Dance by Elna Baker -- where the costumes are creative, the rules are strict, and the dating pool is deeply committed to not touching you.
```

### Performance text (classify this)

```text
(hum or sing “Party in the USA” by Miley Cyrus *)

ELNA: (Pg 12) (stuffing a cookie in her mouth) [Welcome to the] New York Regional Mormon Singles Halloween Dance. That’s right -- it’s a Halloween dance for all the single Mormons between the ages of 18 and 30 who live in the tristate area. That’s a lot of virgins in one room. And I’m one of them.

Tonight I’m dressed like a Queen Bee. The best part of my costume is my stinger. I bought a black funnel from the hardware store and stuck it on my butt. (turn and wiggle) Genius! I was certain that some Mormon guy was going to see me and fall head over heels in love. I joked to my friends that the Queen Bee was going to find a drone. Instead, I’m by myself at the punch bowl stocking up on Oreo cookies. When I’m wrong, I’m wrong and strong.

The worst part is, I should’ve known better. This is my 4th New York Regional Mormon Singles Halloween Dance in a row -- a lame dance held in a church gym. Every year, I come hoping to meet “The One.” And every year, I leave by myself, vowing never to come again. But by the time 365 days have passed, I’ve completely forgotten this commitment. In the end, I am here for one reason and one reason only: I want very much to fall in love.

ELNA: (Pg 12-13) [That’s right!] The dance rules. The most important one, announced over the pulpit on Sunday, is that there is to be no cross-dressing or wearing of masks. I understand the logic behind no cross-dressing, though I doubt that if a man were to dress like a woman at this function he would suddenly realize his true identity. But masks? Two: there is to be no inappropriate dancing or lascivious behavior. That’s why there are too many lights overhead and only “safe” songs like “Cotton-eyed Joe” on the sound system. (**dance and sing/hum a few lines from the song). When slow songs do play people joke that you should be able to fit Old Testament, New Testament, The Book of Mormon, Doctrine and Covenants, and Pearl of Great Price between you and your partner. . . or you’re dancing too close.

If it weren’t already painfully obvious, these events are organized to facilitate marriage. How else would we Mormons meet, marry, then make more Mormons? (Take that, Sally and your seashells on the seashore.) Contrary to popular belief, there are Mormons who live in New York City. I don’t know how many of us there are all together, but there are probably 800 single Mormons and at least 20,000 former Mormons.

I moved to New York to go to NYU for acting (strike a dramatic pose) (Pg 14-15) My parents wanted me to go to BYU, Brigham Young University, in Provo, Utah. They were worried that if I didn’t go to BYU, I’d stop being Mormon, and I wouldn’t meet anyone to marry. Well, they were right about the second part. When I got my letter of acceptance to NYU, my mother was terrified, so she sat me down for a mother-daughter talk. (they begin packing Elna’s suitcase)

MOTHER: (nervously) Elna, the first thing that will happen when you move to New York is, you might start to swear. And swearing will lead to drinking. And drinking will lead to doing drugs. (beat) And Elna, (pursing her lips) what would you do if a lesbian tried to make out with you? (crosses her arms, waiting for an answer)

ELNA: (holding back laughter) I was used to her saying words like church calling and relief society. Not the word lesbian, let alone lesbian and make out in the same sentence. It was awesome!

If you followed my mother’s logic, each step was a progression toward becoming more of a sinner. First I’d swear, then I’d drink, then I’d do drugs. By that point I was getting used to the narrative, so I assumed sex with men would be next. But no—my mother skipped that altogether and jumped to my becoming a lesbian. Did my mother honestly think that I had a better chance with a woman than a man? (composing herself; to mother) I’d say, ‘No, thank you . . . lesbian.’

MOTHER: (rolling her eyes) There are these clubs in New York where men pay larger women to dance with very little clothing on; don’t do that.

ELNA: (to audience) Great, my mom thinks I’m moving to the big city to become a lesbian stripper. Apparently, when she told me I was “special,” this is what she meant. (Pg 16) That’s when my mother saw it, among my tightly folded clothes: a rainbow scarf. It reminded me of Punky Brewster in a retro eighties sort of way.

MOTHER: (snatching it out) You can’t wear this in New York! Everyone will think that you’re gay.

ELNA: (to audience) My mother thought gay people had a monopoly on rainbows. In my opinion rainbows are for everyone, like unicorns. (to mother) Mom, I’m not gay.

MOTHER: I know, but you should avoid the appearance.

ELNA: (to audience) I tried to get my scarf back. I explained how cold I would be without it. I even tried to usher her into this century by explaining that wearing rainbows didn’t automatically mean a person was gay. The Lucky Charms leprechaun was not necessarily a homosexual. The Care Bear with the rainbow on his tummy did not have a life partner. He didn’t even have genitals. Eventually my mom gave me money to buy a new scarf. But she was not, under any circumstances, going to let me take the rainbow scarf to New York City.

(Pg 15) My father sat me down a few days later for another leaving-the-nest talk. His advice was a little different.

FATHER: Elna, never forget these three things. Number One: Never wear a dead man’s socks. Number Two: Never let ’em see you sweat. And Number Three: Never touch a fat man’s stomach.

ELNA: (exaggerated confused look) That was all the advice I was given before moving to New York City. (Pg 17) When I walked into my dorm room, the first thing I noticed was a big rainbow flag hanging on the wall. The only way it could have possibly gotten better would have been if my roommate walked in smoking a cigarette and offered to give me a lap dance. I’d never actually met a lesbian until I met Lisa. It turned out Lisa had never met a Mormon until she met me. And despite all the things we were supposed to be, we hit it off right from the start.

(Pg 18-19) I guess this probably isn’t the kind of stuff most Mormons would even acknowledge. But then again, I’ve always been different from most Mormons. Mormonism can sound pretty farfetched: Joseph Smith digs up golden plates and translates them into a book, The Book of Mormon. This book ends up being a history of the ancestors of the Native Americans, who originated in Jerusalem and believed in Jesus. When you write it all out like that you can’t help but reconsider. Once I tried explaining it to a friend. I went into all the things that I believed. I thought I was doing a good job explaining everything until he said . . .

FRIEND: So basically according to you, Pocahontas was actually a Jew?

ELNA: (Pg 123-124) (distracted by events at the dance) Ohhhh! It’s time for the talent show!

RANDOM MALE: (rapping with a microphone) Hey brothers and sisters, Listen to me,
I’m talking to you religiously,
My Mormon Rap will make you see,
That I’m as funky as Donny and Marie.
Mormon, Mormon Rap, Do the Mo-mo-mo-mo- mormon Rap.
I’m a fine young man, I’m living clean,
Don’t smoke, Don’t drink, If you know what I mean.
Flipp’n, fetch’n, scruddle-dee-me,
Jiminy cricket, and fiddledy-dee!

ELNA: (clapping politely, then turns to the audience) [Where were we? . . . Oh yes,] (Pg 19) The miracles one is expected to believe in the Mormon faith are no different from the miracles you are supposed to believe in any faith. My problem is I was always a skeptic.

When I was four and my mom first told me the story of Moses parting the Red Sea with his hands, I looked at her and said, “Yeah right, Mom.” My mother tried to convince me that Moses had indeed parted a sea just by lifting his arms. I rolled my eyes and patted her on the knee like she was a crazy person.

By the age of six, I was already asking my mother, “When do we graduate from church?” To my dismay I was told that the word to describe being done with church was not “graduate” – it was death.

And I wasn’t exactly enthusiastic about getting baptized. Mormons are baptized at eight years old. According to my parents and teachers, when you were baptized you were washed clean. So why get baptized at eight? None of us had done anything. Why not wait until we were seventy? That way you could lead a fun life, do whatever you wanted to, and have a Get Out of Jail Free card at the end.

(Pg 21-22) When I was 19, I read The Book of Mormon cover-to-cover for the first time. And while I was reading it, I felt like I was leading a better life and making better choices. But [if] I’m being honest. I think most religious people experience just as much doubt as they do faith. And I don’t think doubting makes you bad. I think it makes you smart. (Pg 144) If everyone based their faith on common sense no one would be religious—faith is totally illogical.

(Pg 22) A few Sundays ago, some idiot stood up in church and started talking about how we were having such a mild autumn. He went on and on about how pleasant the weather was and then jumped to,

CHURCH MAN: So really if you think about it, it’s a sign that Jesus Christ [is] coming soon.

ELNA: And so began my usual downward spiral: The weather is warm because of climate change not because Jesus is on his way. How can I belong to a church where people believe such crazy things? I mean, nowhere in The Book of Mormon does it say mild autumn equals Jesus, but technically I’m supposed to believe in the second coming. Do I? I don’t know. How can I possibly sign my name to something I don’t entirely agree with?

(distracted again) Oh, hold on. A guy, Dave, totally hot, just made eye contact with me. He’s dressed as Paul Bunyan, which would be cool if 2 other guys hadn’t also thought of it. Wait, I think he’s walking in my direction. Oh, my gosh, he is. What do I do? Okay. Just play it cool. Show him your stinger. (adjust slightly and wiggle stinger)

DAVE: (Pg 23) How’s it going?

ELNA: (flirting awkwardly) Fine. Where’s Babe?(Dave looks incredibly confused) Paul Bunyan traveled with a blue ox.

DAVE: I’m not Paul Bunyan. (annoyed) I’m Brigham Young! (struts off)

ELNA: (choking on a cookie and calling after him) Sorry, the fake beard threw me off. (to audience) I should’ve stopped there, but instead I added . . . (calling after Dave) So the women who’ve been congregating around you all night, they weren’t your multiple wives? (to audience) I thought this was pretty funny. Dave didn’t even laugh. Mormons don’t know how to laugh at themselves. (beat)

(Pg 25-26) After four years of being a Mormon in New York, I’ve become a reluctant spokesperson for my faith. I’m constantly answering questions or explaining my religion. Every question is about whether I’m a polygamist, whether I’ve had sex, whether I wear magic underwear, and whether I believe in dinosaurs. For the record: I’m not a polygamist, I have not had sex, I don’t wear magic underwear, and I do believe in dinosaurs.

[But] There are Mormon stereotypes: Mormons have big families; they’re from Utah; they wear modest clothes; they’re friendly, naive people; they have white teeth; and they’re Republican. But that list only scratches the surface.

(Pg 29) I [just] am a Mormon in New York. A Mormon in New York seeking another Mormon in New York. Which brings me back to: The New York Regional Mormon Singles Halloween Dance. (Pg 161) [This is] the year I meet the Morman man of my dreams. (digs down deep for courage . . .) (Pg 89) Let’s Dance! (sing and do a few dance moves to the Macarena***)
```

---

## IC-1282: The Odd Couple (Female Version)

- Title: The Odd Couple (Female Version)
- Author (byline): Neil Simon
- Work: Not specified
- Publisher: Random House, Inc.
- Publication date as stated: June 1971
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: FLORENCE, OLIVE
- Teaser before the introduction: Yes
- Spoken words (computed): 1274
- Already set (do not supply): none

### Source block (context only)

```text
Author: Neil Simon
ISBN: 978-0573618284
Publisher: Random House, Inc.
Date (Month/Year): June 1971
```

### Introduction (context only: never use it for content warnings)

```text
2 roommates: Olive who has to be the most UN-sensitive, UN-organized, UN-appreciative, UN-couth, woman (and I use that term loosely) on the planet. ARGHHH! And Ms. Manners, also known as Florence, will probably die of exhaustion, excessive neatness and then demand to organize her own funeral. They drive each other crazy! Yup, of all the possible roommate combinations they are definitely

The Odd Couple by Neil Simon
```

### Performance text (classify this)

```text
(Florence is vacuuming, and Olive comes in. Olive sees her vacuuming and unplugs it. Florence begins winding up the cord, then Olive steps on it. After two tugs at the cord, Olive lifts her foot before the third. Florence falls while Olive laughs. They glare at each other and then turn their heads at the same time. Olive then sits down and picks up a newspaper from underneath the chair. Florence takes the vacuum into the kitchen and returns with a plate of spaghetti. She sits down and begins eating. Olive smells the spaghetti and goes into the bathroom. She comes out with a can of deodorizer, and she then sprays the spaghetti and slams the can on the table. Olive freezes as Florence continues into the introduction.)

FLORENCE: All right, how much longer is this going to go on? Are you going to spend the rest of your life not talking to me?

OLIVE: You had your chance to talk last night. I begged you to come upstairs with me. I was looking for romance, and instead I got a petrified woman standing in my doorway. I don’t want to hear the sound of your voice, do you understand?

FLORENCE: Si, Yo comprendo. Gracias.

OLIVE: (gets a key out of back pocket and slams it on the table) There! There’s a key to the back door. Stick to your room and the hallway and you won’t get hurt. (turns to leave)

FLORENCE: Oh Olive! Need I remind you, I pay half the rent and I’ll go into any room I want!

OLIVE: Not in my apartment! Fine, but I don’t want to see you! Cover the mirrors when you walk through the house. . . and I am sick and tired of smelling your cooking. I have had it up to here with your polyunsaturated oils. Now, get that spaghetti off of my table.

FLORENCE: (laughing hysterically) That’s funny. . . that’s really funny. . .

OLIVE: (getting angry) what is so funny about that?

FLORENCE: It’s not spaghetti, it’s linguini.

OLIVE: (looks at her like an insane person. She then grabs the plate of linguini and throws it at the opposite wall)

FLORENCE: Are you crazy! Look at that mess! I’m not cleaning that up, it’s your mess. Look at it hanging all over the walls.

OLIVE: I like it.

FLORENCE: You’d just leave it there wouldn’t you, until it turns all brown and hard. . . yich! I’m cleaning it up.

OLIVE: (grabbing her and putting her hands on her head) If you touch one strand of that linguini. . . I will break every sinus in your head.

FLORENCE: Why? What did I do this time? What’s bothering you? Is it the cooking, the cleaning, the crying?

OLIVE: I’ll tell you exactly what’s bothering me. It’s the cooking, the cleaning, and the crying. It’s the moose calls that open your ears at two o’clock in the morning. I can’t take it anymore Florence, I’m cracking up. Everything you do irritates me, and when you’re not here the things I know you’re going to do when you come in irritate me. You leave me little notes on my pillow; we’re all out of cornflakes F.U. It took me three hours to figure out that F.U. was Florence Unger! It’s no one’s fault Florence; we’re just a rotten pair.

FLORENCE: I get the picture.

OLIVE: That’s just the frame. The picture I haven’t even painted yet. Every night in my diary, I write down the things you did that day that aggravate me. . . this is June, and so far I’ve filled it up till January. I haven’t even put in about the Gazpacho Brothers yet.

FLORENCE: Oh! Is that what’s bothering you. . . that I loused up your sex life?

OLIVE: What sex life, I can’t even have dirty dreams, you come in and clean them up!

FLORENCE: (pointing a finger at her) I warned you not to make that date in the first place.

OLIVE: (grabbing finger, attempting to bite it) Don’t point that finger at me unless you intend to use it.

FLORENCE: Alright Olive get off my back. . . OFF! Do you hear me!

OLIVE: What’s this? A display of temper? I haven’t seen you really angry since I dropped my eyelashes in your pancake batter.

FLORENCE: Okay Olive, there’s something I don’t want to say, but if I say it. . . I think you’d better hear it.

OLIVE: I’m trembling all over. . . look how I’m trembling all over.

FLORENCE: You’re a wonderful girl Olive. You’ve done everything for me. You took me in here, gave me a place to live and something to live for. If it weren’t for you, I don’t know what would have happened to me. You’re the tops with me Olive.

OLIVE: If I’ve just been told off. . . I think I may have missed it.

FLORENCE: It’s coming now.

OLIVE: Good.

FLORENCE: You’re also one of the biggest slobs in the world.

OLIVE: I see.

FLORENCE: Unreliable,

OLIVE: Is that so?

FLORENCE: Undependable,

OLIVE: Is that it?

FLORENCE: And indescribably inefficient. There I’m done, now you’ve been told off. How do you like that?

OLIVE: Good, because now I’m going to tell you off. For eight months, I lived in this apartment. I thought I was miserable, I thought I was lonely. I took you in here because I thought we could help each other, but after three weeks of close personal contact. . . I have hives, shingles, and the heartbreak of psoriasis. I am growing old at twice the speed of sound. I have seven new liver spots on the back of my hand that look like the Big Dipper. Do me a favor Florence, move into the kitchen, live with your pots, your pans, your ladle, and your meat thermometer. I’m going to lie down now, because my teeth are coming loose, and I’m afraid if I drop them in here, you’re going to get out your vacuum cleaner again. (turns to bedroom)

FLORENCE: (after a pause) Walk on the papers in there. . . I just cleaned the floors.

OLIVE: (looks at her with a crazy glare) In the kitchen! I want to get your head in the oven and cook it like a capon! (chasing her)

FLORENCE: (squeals; runs into the bathroom and locks it) You’re going to find yourself in one nasty lawsuit!

OLIVE: It’s no use running Florence, there are only six rooms and I know all of the shortcuts. (goes through the bedroom and through a different door to the bathroom. Florence runs out of the door Olive just came in)

FLORENCE: Is that how you settle your problems, like an animal? (reaches for her purse) This is tear gas. . . you lay one finger on me and you’ll be using eye drops for the rest of your life!

OLIVE: You want to see how I settle my problems? I’ll show you how I settle my problems! (goes into the bedroom)

FLORENCE: Alright! I warned you, I’m getting out my siren. (pulls a siren out of her purse. Then she lifts it in the air and pushes the button. Nothing happens. She holds it to her ear, again nothing) Olive? Have you been playing with my siren? (banging it on the table) Twenty-two fifty for a piece of Japanese-

OLIVE: (slamming a suitcase on the table) There! That is how I settle my problems!

FLORENCE: Where are you going?

OLIVE: Not me, you idiot! YOU! You’re the one who’s leaving! I can fix your siren so it will whistle for a cab!

FLORENCE: What are you talking about?

OLIVE: (going to the kitchen, she gets pots and pans) The marriage is over Florence. We’re getting an annulment. I don’t want to live with you anymore. I want you to pack your things, tie them up with your Saran Wrap, and get out!

FLORENCE: You mean actually move out?

OLIVE: Actually, physically, and immediately! (puts the pots in the suitcase, then takes the case to the door and sets it down) There! You’re all packed.

FLORENCE: You know, I have a good mind to really leave.

OLIVE: (looking heavenward) Why doesn’t she hear me? I know I’m talking; I recognize the sound of my voice.

FLORENCE: Okay, but let it be on your conscience.

OLIVE: Let what be on my conscience?

FLORENCE: Get out of my house is what you said. I just wanted to get the record straight. Whatever happens to me is your responsibility, and may it be on your head!

OLIVE: Let what be on my head? Don’t put things on my head! Take it off!

FLORENCE: I left you plenty of food, all you have to do is heat it up. You can ask one of the neighbors how to light a match.

OLIVE: You’re not leaving until you take it back!

FLORENCE: Take what back?

OLIVE: Let it be on your head. . . what is that, the curse of the cat people?

FLORENCE: I’d like to leave now.

OLIVE: Florence, we’ve been good friends for too long to end it this way. We’re civilized people, let’s just shake hands and part like gentlemen.

FLORENCE: (looks at the outstretched hand and spits in it)
```

---

## IC-1283: Personality

- Title: Personality
- Author (byline): Gina Wendkos and Ellen Ratner
- Work: Women Heroes: Six Short Plays from the Women’s Project
- Publisher: Applause Theatre Book Publishers
- Publication date as stated: 1987
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: ELLEN, LORETTE, ELLEN AS JAKE OR RICK OR TONY, GAME SHOW LADY, SPANISH CHA-CHA GIRL, VIDEO GIRL, MISS AMERICA, HOUSEWIFE, WAITRESS
- Teaser before the introduction: Yes
- Spoken words (computed): 1935
- Already set (do not supply): none

### Source block (context only)

```text
Author: Gina Wendkos and Ellen Ratner
Book: Women Heroes: Six Short Plays from the Women’s Project
ISBN: 978-0936839226
Publisher: Applause Theatre Book Publishers
Date (Month/Year): 1987
```

### Introduction (context only: never use it for content warnings)

```text
Personality by Gina Wendkos and Ellen Ratner
```

### Performance text (classify this)

```text
ELLEN: In America, you look around and you see all these images of people who you should be. People with long hair down to their waist, people with eyes that sparkle, people with clever accents, people who tell witty stories, people who have courage, people who make shyness an art form. There are so many images of people to choose from . . . everywhere.

(Lights up on woman sitting in chair, downstage, lighting cigarette. Her posture and accent is that of "Lorette," her mother, a Jewish cartoon figure of 54 years old. Lorette speaks to imaginary husband "Sol." He is stage left and never seen. Lorette speaks very stylized New York Jewishese.)

LORETTE: In America if you are not famous you are nothing more than a slimy cockroach, and you are quickly forgotten. When you are famous life is easy. Everyone wants to be your friend. They invite you to the right parties, they ask your opinion. Basically it is all of you that is enviable -- your hair, your smile, your figure, your face, your personality, everything. With her personality she should be listening. Ellen, are you listening to me? Ellen! (With a slight change in posture woman becomes Ellen, Lorette's daughter. She is 30 years old, no strong accent.)

ELLEN: Confidence? Please, that's easy. . . let's face it. We're living in New York City. Right? City of heroes. Isn't everyone here exactly the kind of person you want to be? Who should I be? I mean, I get along. I don't have all that much of a problem making friends. No, really I don't. They say, "Hi Ellen, how's life'!", and I say "Hi gang, life is swell." You see that's an attitude you have to have in N.Y.C, that things are swell. Just say it with me, things are swell. See! If you say it enough, it starts to have a nice ring to it. Things are swell. And when things aren't, if you want my opinion, say they are anyway. Because that's exactly what gets you over. There isn't a single person in this city that wants to hear, things suck. (phone rings, Ellen picks up) Hello, hi Ma. Yes, I got the invitation. They're real nice. . .is Eileen happy with them? Well, I'm not sure yet. . . can't I come alone? No one right now. . . there is this one guy, but. . .well, I don't think it's really right, cause we just met. . . yeah, He’s real nice. I'm sure he works. .. I don't know. . . I didn't ask him. . . if we see each other one more time I'll ask him ... about 5'11" maybe 6'. Yeah, he's handsome... like a Robert Deniro type. Ma, what is wrong with Italian? Why would that embarrass you? Tell me. Why?

LORETTE: I remember a few years ago, there was this bar mitzvah. Ellen was a little heavy then. So I said to her whatever you do, do not wear white. What color do you think she wore? White. She looked like a blimp. To this day people from that bar mitzvah still ask me, how is Ellen? Is she still a little chunky'!

ELLEN: I always wanted to wake up one morning with some guy and hear him on the phone. I wanted to lie in bed pretending to be asleep. I’ll move my hair so that it covers the pillow but still shows my face and I'd lift up my hips so my waist looks smaller just like in the photos and I'll listen to this Jake or Rick or Tony guy on the phone, talking to one of his friends.

ELLEN AS JAKE OR RICK OR TONY: "Hey, buddy, how ya doin'? Listen I've got this girl here. Huh? Her name is Ellen. One of those round, hot Italians. Nah, met her on the street. I went up to her and said I've never wanted anyone like you, and she just looked at me and smiled. I knew once I touched her I'd never leave. Yeah, she's really something else. I could get lost in her hair alone, it's so long and gets everywhere but I want it."

ELLEN: That's the kind of conversation I imagine. Then this Jake or Rick or Tony guy would come in and see me posed like that. Even if he knows it's arranged he'll like it. He'll just look at me. Forget the personality for a minute. Sometimes I want to be wanted just for the way I walk.

LORETTE: There are a lot of pretty girls in this world, a lot of competition. So, it would seem to me that, it would be very difficult, if you're not so good looking, to get a man to take care of you. I told Ellen she should get a skill.

ELLEN: Money. Sure, got lots of it. Can't you tell? I never understood how to have money. . . the idea of becoming a career girl always seemed so stupid to me . . . of all the stupid advances of women, that has got to be the worst. What the hell is so liberating about leaving the home and kids for some stupid desk job. . .? (Phone rings and Ellen picks up)

Hello, Hi Mom. Yeah, we had a great time.. Y'know one of those really fun nights, where everything went well. Mom, why do you ask me stuff like that? Cause I think it's sort of personal. No, I am not ashamed. . . it's just really personal. So what if he did? What difference does it make? What if he did sleep over, what does that mean?

LORETTE: Four men is the limit for a woman to sleep with before she gets a bad reputation. Number one is the one you lost your virginity to; it was summer, he had a nice car. Number two, that one's because you kind of forgot what it was like the first time. You were a little nervous. The third one is like practice - makes perfect. You're preparing yourself for number four, the one you're gonna marry. I tell Ellen the number is four. After that they call you a used car.

ELLEN: Pretty strict rules in this woman biz. As a kid it never mattered, you could climb trees and giggle. But now only one of those attitudes is allowed or you don't get over. It's OK. If you want to act tough, then people know who you are . . . on, she's a tough broad, watch out. And it's cool if you have pert breasts and giggle, then people know the score. But make a sexy girl tough and no one knows the right response. So you see, some days I'm a giggly type. I laugh at everything. I'm coy. I'm sweet. I'm available. And other days I'm a tough broad. That's where things get pretty confusing for the world at large.

LORETTE: Ellen. Ellen, Ellen, Ellen. She's thirty years old. She doesn't know what she wants to do with her life. When I was her age, I had two children, a home I could basically call my own and I was president of the P.T.A. Ellen never has any money. I told her a good job for her is word processing. You work in an office, you meet nice people. She won't investigate it. She's lazy and she's sloppy. She is not pretty per se. What man is gonna want her? You know what her problem is? She is not aware. Ellen would never have had such a lousy personality if she listened to me.

ELLEN: And the tension, the tension. It winds me up so bad. I'm pissed off. Real pissed off. So pissed off that I want to start a fight. I’m so finished with being that ugly, skinny little thing. All the Frenchmen in the cafes, all the Italians in the gondolas, all the Indians on the reservations, all the children hiding under the swings, all the old people hiding under wrinkles. It's them, all of them. . . whispering things to me . . . (phone rings) they make me who I am. (Ellen picks up) Hello. No, Ma, he didn't call. . . how do I know? Huh, are you satisfied. . . you said he wouldn't and he didn't. So do you have the balloons out?? Are you throwing a party? Huh? Did you make a cake while you're at it? No, no! I'll say whatever I want at this point. I am sick and tired of hearing how I should do it, how I should say it, how I should act it . . . My personality, Ma. WHAT IS WRONG WITH MY PERSONALITY? WHO DO YOU WANT ME TO BE? HUH? WHO?

(Ellen flashes through a number of “PERSONALITIES”)

GAME SHOW LADY: (Midwest accent) I'm going to be on the 10,000 Dollar Pyramid. I'm so excited. You see I read everything. Books, magazines, backs of cereal boxes. Just ask me anything. "What is the capital of Burma?" "Rangoon." "How does the whojoo bird protect itself?" "Its fur inflates into a protective covering." I know it all. Animal, vegetable, and mineral. They also like me on TV because I have a bubbly personality…

SPANISH CHA-CHA GIRL: (Low-class Spanish accent) Maria, conyo, Julio, si. I love this place. Mongo Santa Maria (dances and sings) Julio get me a gin and tonic. Julio, he's my boyfriend. He and I are going to be in a contest and we're going to win. Julio thinks the prize is fifty dollars but I'm going to surprise him. The prize is going to be me. And I'm not going to use birth control. So that way I get the ring, the car, and Julio.

VIDEO GIRL: (Brooklynese accent) Hey, hi guys, hi Rusty. How ya doin'? Slap me five. Hi Pee Wee. How ya doin'? (Pantomimes playing PacMan) Oh boy, 500 points, I don't believe it. Better watch out you're gonna be eaten. Better watch out. Told you. (Makes the sound of Pac Man) See I do this game better than I know anything else. See. People say I could go pro at this game. Then I could quit school.

MISS AMERICA: (Southern drawl; sings "Here She Comes Miss America") Thank you all, thank you so much. It's been a wonderful year being Miss America. I traveled around the world and saw so many underprivileged people. You should see how these poor darlin's live. They have animals right in the house, So I turned and said (sings) "We are the world. We are the children." That's just one of the many things I've done as Miss America.

HOUSEWIFE: (Nancy Reagan accent) I take pride in the things I do. Every single one of them. Some women keep their homes in horrible condition. They serve jelly from the jar and it develops and unsightly crust around the rim. Oh yes, and they use paper napkins. REALLY! Paper napkins. (screams at kids) TOMMY, JIMMY, GET AWAY FROM THAT REFRIGERATOR BEFORE I CUT YOUR HANDS OFF. (resumes Nancy Reagan personality) I use cloth napkins only. I have several patterns. Checkers, stripes, floral prints, even polka dots.. (screams at kids) DID YOU HEAR WHAT I SAID? GET UPSTAIRS WITH YOUR BROTHER.

WAITRESS: (low-class urban accent) Hi, hon, coffee? How ya doin' today? What's it gonna be? Whole wheat, white or rye? Cole slaw or French-fries? Anything to drink? Coke. Here you go.. I run this counter like clockwork. By the time they have their cigarettes out of their pocket I get a cup of java in front of their face. (ding) When I hear that bell I run. I don't care what anyone says anything made with cheese gets soggy under these lights. I have a lot of miles on these feet. But when my customers come in they know they're gonna get quick courteous service. Not many people give you that at all.

(Medley and frenzy of characters blends into a cacophony of all characters until final frenzy-woman switches accents and characters.)

GAME SHOW LADY: uh. (buzz) Kentucky. Tennessee I always get that one right.

SPANISH CHA-CHA GIRL: What do you mean you're dancing with someone else Julio?

VIDEO GIRL: Hey, what's the matter with this machine? I never lose my quarter.

MISS AMERICA: Let me keep the crown just one more year. I promise I'll give it back. Just one more year.

HOUSEWIFE: I only have paper napkins. I only have paper napkins.

WAITRESS: What do you mean my coffee is bitter? This is a fresh pot. Why don't you go somewhere else buddy?

(Frenzy flip out-shaking-etc. Pause, breathe. Switch to ELLEN)

ELLEN: What is a personality? Huh Ma? What is a personality? So, I said to the Frenchmen in the cafes, the Italians in the gondolas, to the Indians on the reservations, so I said to her, I'm lazy, I'm sloppy, and I have flat feet. Take me or leave me. Hopefully she'll take me.
```

---

## IC-1284: POTUS

- Title: POTUS
- Author (byline): Selina Fillinger
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: Aug 2022
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: CHARACTERS, SETTING, JEAN, HARRIET, MARGARET, CHRIS FROM THE TV, CHRIS, DUSTY
- Teaser before the introduction: Yes
- Spoken words (computed): 1479
- Already set (do not supply): none

### Source block (context only)

```text
Author: Selina Fillinger
ISBN: 978-0573709999
Publisher: Samuel French, Inc.
Date (Month/Year): Aug 2022
```

### Introduction (context only: never use it for content warnings)

```text
One four-letter word is about to rock 1600 Pennsylvania Avenue. When the President unwittingly spins a PR nightmare into a global crisis, the brilliant and beleaguered women he relies upon risk their sanity to keep the commander-in-chief out of trouble.

For any woman who’s ever found herself the secondary character in a male farce . . . This is POTUS by Selina Fillinger
```

### Performance text (classify this)

```text
CHARACTERS: Harriet (Chief of Staff), Jean (Press Secretary), Margaret (First Lady), Chris

(a journalist), Dusty (POTUS’ pregnant dalliance)

SETTING: The White House – Perhaps not the current administration, exactly, but broad strokes of past presidents combined with stress dreams of future ones. And if we’re being honest, an amalgamation of them all . . .

JEAN: (Pg 1- 3) He said the words, “My wife’s a ****?” (expletive should be mouthed or indicated with a broad gesture rather than spoken) (beat)

HARRIET: He said, “Please excuse my wife’s absence. She’s having a *****-y morning.”

JEAN: Publicly? Who exactly was there?

HARRIET: Washington Post, CNN, New York Times, BBC, and three Chinese diplomats. Everyone heard it, everyone got it, two people gasped.

JEAN: Well, that’s not so bad.

HARRIET: Wow.

JEAN: It’s not! We can contain that. We all have ****-y mornings sometimes. My son has them every week.

HARRIET: Margaret wasn’t absent, she was in the room.

JEAN: Why didn’t he see her?

HARRIET: She was sitting.

JEAN: And therefore invisible?

HARRIET: He was standing, so the diplomats felt like it would be rude to sit, so they were all standing in front of her, blocking his view.

JEAN: He stood for the entirety of the meeting?

HARRIET: He can’t sit right now because of (pause) the thing on his . . .

JEAN: The abscess on his – right. I thought they were removing it.

HARRIET: They couldn’t because (Pg 4-5) he’s booked, Jean! His friend Jerry, from college, said he had the same thing and he should just rub tea tree oil on it.

JEAN: (Pg 6) I don’t want to know! (Pg 11) I’m going into the press room right now and (Pg 6) I’m trying to figure out if my biggest problem today will be explaining why the President of the United States used the word ***** to describe his wife to three diplomats – OR if there is something MORE awful I need to know about.

HARRIET: (Pg 11) (with a week cheer) Go get ‘em! Wooohhh!

JEAN: Oh, shut up . . .

MARGARET: (Pg 7) (seething) I’m gonna punt that man’s abscessed ass across the South Lawn and if you don’t get out of my way I will shred you like the sad cardigan you are.

HARRIET: (Pg 9-10) (blocking the door) He didn’t mean it. He’s in a lot of pain and it’s clouding his judgment.

MARGARET: Dammit, Harriet, you cannot prevent me from having a marital discussion with my husband!

HARRIET: I absolutely can, especially today, when he has a nuclear non-proliferation meeting, a gubernatorial candidate endorsement and an oozing pustule on his . . . I finally got him calmed down from your argument this morning

MARGARET: It wasn’t an argument

HARRIET: When you told him to stop behaving like his father, grow a pair and have the procedure without anesthesia?

MARGARET: I had two natural births and one root canal with no drugs, he can certainly

HARRIET: (Pg 57) Wait! I can’t hear the TV!

CHRIS FROM THE TV: . . . President reportedly stormed out of the nuclear non-proliferation discussions after a fiery exchange with the Prime Minister of Bahrain.

HARRIET: No, no, no!

CHRIS FROM THE TV: Sources within the White House say the President refused to sit for the duration of the negotiations, which the Prime Minister and several other world leaders interpreted as, quote ‘an aggressive power move.’ The Prime Minister says there will be, quote, ‘regretful consequences.’ ****** FLOTUS interview with CHRIS*****

MARGARET: (Pg 25-26) Well there is no typical, Chris. My daily work is determined by the ever-shifting needs of my five non-profits, two children, and of course, one and only president. The truth is, even before I was First Lady, after graduating from Stanford and then Harvard, I managed to keep busy with my law firm, my talk show, my book, my other book, my gallery and Taekwondo.

CHRIS: (joking) Why aren’t you president? (they both laugh for a moment then fall into silence) ****** In the Hallway*****

DUSTY: (Pg 28) (flags down Jean who is in a rush) Wait, hi, hi, I know you, you’re on TV!

JEAN: Ask one of the other interns . . . I can’t

DUSTY: Could you just point me towards the president? I’m Dusty. (Pg 18) I was told to be discreet. I’m here about the position. (she winks)

JEAN: (Pg 29) You’re meeting with Harriet? (struggling to comprehend) But you’re here to see the president?

DUSTY: He sent a private jet! I’m only here until tomorrow night and then I’m flying back to the farm.

JEAN: Hang on. . . The farm?

DUSTY: In Iowa.

JEAN: (with dawning horror) And you’re pregnant.

DUSTY: Eighteen weeks! Big as a bell pepper.

JEAN: (Pg 30-31) (to herself) What’s happening – how is this happening!

DUSTY: The president and I are in love . . .

JEAN: LOWER your voice, oh my god. SHUT UP!

DUSTY: (Pg 37) Ma’am, I’m going to need you to take a deep breath

JEAN: YOUR NAME IS AN ADJECTIVE: DON’T TELL ME WHAT TO DO!

HARRIET: (Pg 34) (entering) What the hell is going on here?

JEAN: (Pg 38-39) YOU are Chief of Staff. YOUR job is to contain situations. I’m the PRESS SECRETARY. MY job is to contain STORIES, and I can’t contain stories if I don’t KNOW the STIUATION, so perhaps you’d like to explain THIS SITUATION. (she motions to Dusty’s pregnant belly)

(The door to the interview room opens and CHRIS and MARGARET enter the hallway- Chris immediately turns on her phone to record)

MARGARET: (Pg 40) (regarding DUSTY) What is this?

HARRIET: (Pg 42) No, no, no, no . . .

MARGARET: If you think you can show up here, unannounced and blackmail the president

DUSTY: What? No, POTUS invited me. I’m here to celebrate our little president-to-be.

CHRIS: (Pg 14) (softly into her phone) I don’t need to stir shit up: we got a president throwing his feces at the wall.

JEAN: (Pg 42-43) Oh shit.

DUSTY: When I sent him a pic of the ultrasound he texted me that I should come in to celebrate.

HARRIET: Nope, that was me. POTUS is really busy, so you and I are just gonna have a quick little chat and

JEAN: (whispers to Harriet) Here . . . You’re doing this IN the White House?

HARRIET: (whispers to Jean) Where else am I gonna do it? A back alley? You don’t think that’d make her a bit suspicious? (to Dusty) Okay, honey, here’s the thing: as much fun as I’m sure you and the president had together.

DUSTY: We’re in love.

MARGARET: (cackles bitterly)

HARRIET: The thing is this pregnancy is not, um. Happening. (Pg 44) See, the way it works is we give you money and, in exchange, the pregnancy isn’t – it it it goes away. We’re talking about the President of the United States, right? The married president.

MARGARET: (cackles bitterly- to Harriet) (Pg 9) Your loyalty to my husband is admirable. I hope you continue to feel fulfilled by your choice to trade youth and beauty for a life of service to him.

HARRIET: (Pg 44) (ignoring Margaret) Do you see how that could make from some icky headlines?

CHRIS: (Pg 12) (into her phone) What a time to be alive, isn’t it! (suddenly everyone notices Chris who has been recording everything with her phone - Pandemonium ensues – a wild and epic chase)

MARGARET: (Pg 45-47) GET HER!

JEAN: I GOT HER PHONE!

HARRIET: DON’T LET HER LEAVE!

CHRIS: (grabs a bust from a pedestal in the hallway and raises it over her head) Give me my phone and get out of my way or I will break this into a million pieces

MARGARET: That is notable suffragist Alice Paul!

CHRIS: I will break her ugly face! . . . One . . . Two . . . Three

(she hurls the bust just as the office door opens. It sails through the doorway offstage. There is a thunk of the bust colliding with an unseen person’s head and the thud of a body hitting the floor. Silence – The women are frozen in shock sharing through the open door at the body on the ground)

DUSTY: (Pg 48) YOU KILLED HIM. YOU AND YOUR MEAN FRIENDS KILLED MY LOVE!

CHRIS: I’m going to go away for life. They’re going to send me to Guantanamo!

MARGARET: (Pg 50) Chris, stand up. Jean, go tell the secret service that the president is going to be a bit.

CHRIS: A bit? He’s going to be more than a bit.

MARGARET: Oh, I’m sorry, do you have a better idea? Because I though your contribution ended at death by discus!

HARRIET: Now, Jean, before we go down in history next to Booth and Oswald!

CHRIS: (Pg 52) This is a matter of national security! We need to notify the vice president right now.

MARGARET: That man is as useful in a crisis as a turnip.

CHRIS: Someone else, then. We murdered the president.

JEAN: You mean YOU murdered the president.

CHRIS: Don’t. You. Dare. If he was doing his job he would be across the White House right now making peace treaties! He should not be living in this house, he should not be running this nation and you know it! He’s the pyromaniac, but you gave him tmatches. You figured he’d burn his fingers and learn his lesson – Well he didn’t, and now the whole world is on fire! So we douse those flames, or we will burn in them together, but don’t think for one second I am marching to that stake by myself!

DUSTY: (inspired) Why isn’t SHE president?

JEAN: (launches the plan) (Pg 58-59) We can still contain this. Stay visible, don’t talk to each other. Then tonight, right when he’s supposed to be onstage for his speed, POTUS will be found with a suicide note in his hand. He was unwell. He can’t be responsible for his words, or his actions, he can’t be held to etiquette – he was sad!

HARRIET: (sobbing) It’s too much. I’m too tired

JEAN: This is what you do, Harry. You’ve done it for years. You clean up his messes, you make excuses, you do his job and then you wake up and do it all over again. But what if this is the last mess of his you ever have to clean? ****** Dream vision of Harriet, Jean and Margaret in control******

HARRIET: (Pg 61) (on the phone) What do you mean, “Why would Norway involve itself? Because that’s what allies do. You back us and in exchange we give you things that Norway needs, like peanut butter and genetic diversity . . .

JEAN: (addresses the press) Do I seem worried? No, like I said, the talks did not stall, they just broke for lunch. No, Eric, don’t speak until I call on you . . .

MARGARET: (Pg 67) (addressing the press) Which is why it is with great pride and joy that the president and I endorse Leslie Hopper as the next governor of . . . ****** Dream ends – back to reality******

JEAN: (Pg 77) We can’t just leave the body . . . What if something happens to it?

HARRIET: What’s he going to do – stand up and walk out? (a long loud moan from the president - the women scream)

MARGARET: (Pg 84) He’s awake! (long beat, then to audience) We told him he took too many pain meds, backed out and hit his head. Idiot totally bought it.

HARRIET and JEAN: *****! (beep can censor this expletive)
```

---

## IC-1285: Property of the Rebel Librarian

- Title: Property of the Rebel Librarian
- Author (byline): Allison Varnes
- Work: Not specified
- Publisher: Random House Books
- Publication date as stated: Sept 2018
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: ANNOUNCEMENT, JUNE, DAD, MOM, STUDENT, OFFICER, MR. BEELER, MR. HAWKINS, MOIRA ROBERTS, SCHOOL BOARD CHAIR
- Teaser before the introduction: Yes
- Spoken words (computed): 1780
- Already set (do not supply): none

### Source block (context only)

```text
Author: Allison Varnes
ISBN: 978-1524771478
Publisher: Random House Books
Date (Month/Year): Sept 2018
```

### Introduction (context only: never use it for content warnings)

```text
Property of the Rebel Librarian by Allison Varnes
```

### Performance text (classify this)

```text
ANNOUNCEMENT: (Pg 59) Effective immediately, Dogwood School Libraries will no longer house texts that contain profanity, drugs, violence, rock/rap music, witchcraft, drinking, smoking, or rebellion of any kind. They are hereby banned for unsupervised distribution. Students in possession of unapproved texts will face disciplinary action. Teachers in violation of this resolution will be terminated.

JUNE: (Pg 58) Since when does this school get so worked up about books? (Pg 59-60) I’m going to be sick. I mean, who thought books would be cause for punishment? (Pg 2-4) I walk home from school (June opens the door to her house and is confronted by her father)

DAD: (holding up a book) Would you care to explain this?

JUNE: (shrugging) Um, it’s a book?

DAD: (disapprovingly) Yes, The Makings of a Witch. One that we don’t approve of. What concerns me more than anything is that it’s from the Dogwood Middle library, of all places.

JUNE: (to audience) I can’t watch TV or use the family computer without someone looking over my shoulder, but books have always been safe. (to Dad) Dad, if you’d just . .

DAD: No. This sort of thing won’t happen again. You’re grounded. No TV. No phone. No internet.

JUNE: What? (Pg 8) Being grounded for reading? That’s a new one.

JUNE: (Pg 30) I haul my bags up to my room. (she reacts with shock) The bookshelf in the corner. It’s empty. Every. Single. Book. Gone. (racing downstairs) What did you do with my books? (Mom and Dad are reading her books)

DAD: They’re in safekeeping until we can make sure they’re quality reading material. You will request books through us. If we have read a book and approve, we will release it to you.

JUNE: What? You can’t be serious! (June exits in huff)

MOM: (Pg 33) I never dreamed we’d need to monitor kids’ books. The look on her face. Our child hates us.

JUNE: This doesn’t make sense. Nothing makes sense.

DAD: Our house, our rules. She’ll get over it. *****Scene – The Next Day at School*****

JUNE: (Pg 56-57) [The next day when I get to school] two moving trucks are parked in the pickup/drop-off circle. I wander off to the library. CLOSED FOR INVENTORY – and the door is locked. I’m about to turn away when the door creaks open, revealing a heaping cartload of books behind it. I hold the door while two older men wheel the cart into the hallway. Then I slip inside. The space is almost unrecognizable. Huge gaps linger on the shelves where large quantities of books used to be. Dad! What are you doing?

DAD: It’s called a book extraction. It’s necessary for quality control.

JUNE: (Pg 3) Dad is president of the PTSA, and he keeps his thumb on everything at Dogwood Middle. (Pg 59) Now I’m going to be sick. Just like that, I can’t read a book at home or in the library. (Pg 70) I set off down the hall. (she gazes at the walls) New posters with phrases like COMMUNITY STRONG, PROTECT OUR CHILDREN, and STUDENTS FOR A MORAL FUTURE. It’s signed by the Student Club for Appropriate Reading. SCAR (groans) (Pg 121) There’s a picture of a homeless kid on a street corner smoking and drinking beer. Below it, it says DO YOU KNOW WHAT YOUR KIDS ARE READING? Who came up with this? There isn’t even a book in the picture. (she rips it down, wads it up) *****Scene – The Next Day *****

JUNE: (Pg 54-55) [Walking to school] the stop sign looms ahead. Except this time, I don’t go where I always go. I turn left onto Maple Lane – the long way to school. Midway down the street, balanced on a tall wooden post, right by the curb is some sort of dollhouse. I’ve never seen anything like it. Below its top two windows, a glass door protects books on the other side. LITTLE FREE LIBRARY is engraved in a metal plate at the top. I feel like I just found a wad of cash, but better. (Pg 269-270) Roll of Thunder, Hear My Cry by Mildred D. Taylor, The Lightning Thief by Rick Riordan, Diary of a Wimpy Kid by Jeff Kinney, Because of Winn-Dixie by Kate DiCamillo, and the first Harry Potter book! (she stuffs the books in her bookbag excitedly)

ANNOUNCEMENT: (Pg 59) (echoing) Students in possession of unapproved texts will face disciplinary action.

JUNE: (Pg 88) But what if nothing is found in my possession? Rule #1: Don’t get caught. (Pg 93) I have to wait until lunch to visit my locker. (Pg 69-70) [When] I slam my locker shut, the impact pops open the locker next to mine – candy wrappers and a few wadded-up balls of paper – nothing else. (Pg 90) And then I stop. [The perfect place for] a library! (Pg 94) (she glances down the hall, clears the debris from the locker and transfers the contraband books from her bookbag into the empty locker) One book can change everything. And I know where I can get more! (she pulls a notebook from her bookbag and a black sharpie she writes) (Pg 98) PROPERTY OF THE REBEL LIBRARIAN (she stands up taller with confidence) (Pg 90) Rule #1: Don’t get caught. I mean it. Rule #2: Don’t squeal. You just found this book. I had nothing to do with it. Rule #3: Give it back to me when you’re done. (Pg 97) I’m going to use code names to keep track of everything. You know, just in case. (she removes the combination lock from her locker and puts it on the new library locker) (Pg 103) Locker 319 is secure! **** A few weeks later****

JUNE: (Pg 269-270) Bridge to Terabithia. . .The Outsiders. . .Matilda. . .Number the Stars. . . Coraline. (Pg 119) Everywhere I look, kids line the hallways with oversized textbooks in their laps. Lunchtime, after school, their sneakers dangle off sidewalk benches. I don’t have to look to see what they’re doing I already know. Reading! And Dan Fuller, the most popular guy in school, high-fives me in the lobby. (air high-five and happy dance) This is no longer the same Dogwood Middle. It’s an alternate reality where reading is the coolest thing you can do and I, June Harper, am the leader of the cool kids – of the rebellion.

6th Grader: (Pg 129-130) (in a whisper) Hey, June? Do you have any Captain Underpants books? It’s not for me. My little brother loves those books, but his school said they weren’t good for kids.

JUNE: You’re kidding, right. What’s so wrong with a superhero saving the day in his underwear? It’s not going to make kids refuse to put on pants or anything. What did the school think is wrong with them? 6th Grader: They said they were offensive and couldn’t believe something with underpants in the title was in the school library.

JUNE: Oh no, not underpants! I do declare, what happened to decency? ***** At June’s Home****

MOM: (Pg 141-143) Honey! Come down here a sec! We thought it was time we return some things to you.

JUNE: (excited) My books? They’re all here?

DAD: More or less. It took us forever to read them all, but we finally did it.

JUNE: I have to take them an armload at a time. Ten of them, actually. Surrounded by my collection I sift through the piles. Old Yeller first. One of the pages toward the end feels thicker than the others. A white index card has been glued over the existing page. Travis is supposed to pick up his shotgun here, but instead it reads “And then Old Yeller was cured of rabies and lived happily ever after. That’s it. The rest of the pages have been ripped from the spine. (her jaw drops and she reaches for another book) Diary of a Wimpy Kid -- Card stock glued over the fart jokes. The same edits are in my other books. Someone took great care to cut out tiny black rectangles and past them over certain words. This is exactly what Locker 319 exists! ***** At school****

JUNE: (Pg 195-196) The last thing I want to see when it’s pouring raining and freezing is a line of students waiting to get into the building (to another student) Is there a reason we’re standing out here?

STUDENT: Some kind of random search. It’s probably about books.

JUNE: (nonchalantly) Yeah. I heard books have been a big problem lately. (Pg 199-200) (to audience) The line leads to a table staffed by two security officers.

OFFICER: Bags down first, ladies. One at a time.

JUNE: A trash bin overflows with novels. My novels. Mr. Beeler, the principal, stands with his arms crossed, his eyes growing bigger with each book added to the pile. They found what they were looking for. ***** AFTER SCHOOL ASSEMBLY****

MR. BEELER: (Pg 203) There will be an emergency PTSA meeting Immediately following 6th period today. (Pg 206) We will begin promptly at 3:45. (Pg 209 – 210) As many of you have heard, we collected two hundred forty-two novels from the student body this morning. This isn’t an isolated case of one or two books. This is a – a movement that has gripped out students. All lockers are being searched by the safety committee at this very moment.

JUNE: (covering her smile and faking a yawn)(to audience) They’ll have a field day with Locker 319. No one has any ties at all to the locker. Not even me. Even if the notebook turns up, so what? Our names aren’t in it.

MR. HAWKINS: (Pg 212) (rushing in from the back of the auditorium) We found it! (he whispers frantically to Mr. Beeler and hands him a green notebook)

MR. BEELER: Parents. It appears we have our answer. Locker 319. Unfortunately, there is no registered owner of this locker, which makes the offense even more serious. (Pg 214-215) I had hoped for the name of the person responsible for this. I don’t see one actual student name in this entire book. It’s one thing to run an illegal library on public property. But to write this on the cover? (He holds up the green notebook) PROPERTY OF THE REBEL LIBRARIAN

JUNE: (looking at the notebook with her best bored expression) There will be no confession tonight. Rule #1: Don’t get caught.

MOM: (stiffens and looks over at June, she speaks loudly) Alma June Harper. How could you!

JUNE: (aghast) My handwriting! *****Scene*****

MOIRA ROBERTS: (Pg 217) Hi, I’m Moira Roberts, and this is the news at six. Tensions are running high today in the halls of Dogwood Middle. Classic literature was confiscated on the basis that it was not morally sound for young people. But they couldn’t collect all of it. What school officials did not anticipate is that students would find a way to fight back. Not everyone is in agreement with the limits put on student freedom. But will the school board listen? Find out tomorrow night when I report live at Six. I’m Moira Roberts, and this is your Dogwood. *****Scene*****

JUNE: (Pg 216) Suspension. (Pg 220-221) And the school board is holding an emergency session to deal with everything. My parents have arranged for me to publicly apologize. I’m not sorry. I didn’t commit a crime. I opened a library!

MOM: (firmly) What you did was wrong, and when you’re wrong, you apologize. End of discussion. (Cut to school board meeting)

SCHOOL BOARD CHAIR: (Pg 237) Alma June Harper . . . You have five minutes (June steps to the mic)

JUNE: (Pg 238-240) Adults are always saying how we need to be responsible citizens, but how can we even learn what that means if you put the library on lockdown. I thought about that. And when I found a book I wanted to read, I read it. Then other people asked to read it, so I said yes. It got bigger. Before I knew it, I had dozens of books and an empty locker to put them in. And you know what? Everyone started reading. I’ve never seen more students read at school in my life. All because you said we couldn’t. Are you going to keep punishing the whole school because we thought outside the box you tried to put us in. Will you do it in front of the entire nation? They’re watching. I’m not some troubled kid trying to destroy the community. I am outraged. I am censorship gone wrong. (she takes a deep breath, squares her shoulders, looks directly into the cameras) (Pg 246) I believe in the freedom to read. Most people around here would call that rebellion, so I thought I’d beat them to the punch. Don’t tell me what to read. (Pg 240) I am the Rebel Librarian.
```

---

## IC-1286: Ravenswood from Bad Habits

- Title: Ravenswood from Bad Habits
- Author (byline): Terrance McNally
- Work: Terrence McNally 15 Short Plays
- Publisher: Dramatists Play Service
- Publication date as stated: June 1994
- Event as filed: Humorous Interpretation
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
Let's face it, all of us have our own bad habits. We may bite our nails or crack our knuckles. Some of us interrupt people often or procrastinate. All these nasty habits are hard to break. But have no fear! Ravenswood is a special facility that has the answer! With daily injections . . ., all of your bad habits can be resolved. No pain, no work, no suffering. Call it a quick fix, if you will.

Ruth Benson, former patient and now a nurse at the facility is the poster child to prove the program works. Once she was an overweight slob with a horrible drinking and smoking habit . . . but now she’s committed her life to helping others . . . and today is her lucky day. The love of her life, Hugh Gumbs, has checked himself into Ravenswood from Bad Habits by Terrance McNally.
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

## IC-1287: The Role of Della

- Title: The Role of Della
- Author (byline): John Wooten
- Work: Plays for Actresses
- Publisher: Vintage Books
- Publication date as stated: March 1997
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: ELIZABETH, EMMA, WOMAN
- Teaser before the introduction: No
- Spoken words (computed): 1327
- Already set (do not supply): none

### Source block (context only)

```text
Author: John Wooten
Book: Plays for Actresses
ISBN: 978-0679772811
Publisher: Vintage Books
Date (Month/Year): March 1997
```

### Introduction (context only: never use it for content warnings)

```text
An acting audition can cause a lot of stress for aspiring actors and actresses. Finding a good acting audition can be hard enough, getting invited to an audition is even harder, and the actual act of auditioning for the role is sometimes the biggest moment of an actor’s life. So here are some tips:

The judges will look into more than just your facial expressions. Basics, such as, were you on time? Did you show an extravagant personality when you were walking into the room? Make them remember your name!

Use your own creativity to do this (be professional, don’t go crazy), but there’s something to be said about making a lasting impression on someone. If it’s close between you and another star actor or actress then it could be your ace in the hole.

Make sure you follow direction well. You will be so focused on your own monologue or whatever you have to do for your audition that you might forget an important factor. Listen to your casting director during your acting audition!

As long as you are sure your casting director is REALLY a casting director. The Role of Della by John Wooten
```

### Performance text (classify this)

```text
Lights up on an audition studio. EMMA stands in front if a table. She carefully examines a few head shots, which are spread about the table. She notices one if interest and slowly sits down in a chair in front if the table. ELIZABETH slowly sticks her head into the room.

ELIZABETH: Excuse me. (Startled, Emma quickly puts the head shot on the table. She begins to rise.) No, don't get up. I'm a little early. There was no monitor out front. I saw the door open. I didn't know if I should come straight in ... or if I should wait ... I'll come back in a few minutes. (Starts out)

EMMA: Do you have your audition card?

ELIZABETH: Oh, yeah. (With a smile.) I wouldn't lose this. I had to get here at 6 A.M. to wait in line and I still barely got a slot. Some girl offered me fifty dollars for this card. Just for a chance to audition. It's like a zoo out there.

EMMA: Hand it to me, please.

ELIZABETH: Sure. (She crosses to her. Offers hand.) I must say it's a great pleasure to meet you, Ms. Stewart. I've heard great things about your theatre.

EMMA: (Shakes hand.) Thank you. The card.

ELIZABETH: Oh, right. (She hands Emma the audition card.) Sorry. Just a little nervous.

EMMA: That's all right. I understand.

ELIZABETH: John Wyatt says hello.

EMMA: Really.

ELIZABETH: He's doing great. He just booked ...

EMMA: Do you have a head shot and resume?

ELIZABETH: Of course. (She hands EMMA her resume.)

EMMA: (Takes a moment, looks at the headshot.) No, I need your headshot. (ELIZABETH laughs.) Is something funny?

ELIZABETH: I don't understand.

EMMA: (Deliberately slow.) I need your headshot.

ELIZABETH: This is my headshot.

EMMA: No.

ELIZABETH: Yes, that's me.

EMMA: Really? You've gained a few pounds since this picture was taken, haven't you?

ELIZABETH: I beg your pardon?

EMMA: What role are you interested in?

ELIZABETH: Della.

EMMA: Della? Really? The young ingenue?

ELIZABETH: (A beat.) Yes.

EMMA: (Chuckles to herself.) Okay. Why not. What piece are you doing?

ELIZABETH: Uh ... Today, I

EMMA: Can you move back a little, please?

ELIZABETH: Sure. Sorry. (She moves back, away from table.) Good morning. My name is Elizabeth Ryan. Today, I will be doing a selection from ...

EMMA: Just do the monologue.

ELIZABETH: Right.

EMMA: You only have two minutes, you know?

ELIZABETH: Yes. (She turns and takes a breath. She turns back around, and begins.) "Oh, we would get into terrible arguments, my mother and I."

EMMA: Do I have something on my face?

ELIZABETH: Pardon?

EMMA: Why are you looking at me?

ELIZABETH: Is it okay if I direct my piece to you?

EMMA: What do you think?

ELIZABETH: (Begins again, awkwardly directing piece to chair.) "Once, when I was twelve or thirteen, I told her that God was a moronic fairy tale-I think I'd spent an entire night ... "

EMMA: Do you have anything else?

ELIZABETH: Excuse me?

EMMA: Do you have another monologue? (ELIZABETH looks confused.) Anything? ... I've already heard that twice today.

ELIZABETH: Really?

EMMA: Yes, and I was glad Agnes killed the baby.

ELIZABETH: (Taken aback.) I'm sorry. If you'd like to give me a direction with it, I'd be happy to ...

EMMA: This is not an acting class, Elizabeth. Besides, what you need is an interpretation class. Agnes of God is not a melodrama.

ELIZABETH: No, of course not. I wasn't trying to ...

EMMA: Don't make excuses. Just do something else.

ELIZABETH: I don't have anything else prepared. I thought that piece was appropriate.

EMMA: Actors do not think, Beth. They act. Those who think, think. Those who act, act. Those who think they can act, spend more time thinking than acting.

ELIZABETH: Of course. Can I please try again?

EMMA: No. Tell me a story ... Something funny.

ELIZABETH: Funny?

EMMA: Yes. Make me laugh.

ELIZABETH: Just like that?

EMMA: You want this job, don't you? You want to play Della?

ELIZABETH: Of course.

EMMA: Then make me laugh. Are you an actress or aren't you?

ELIZABETH: Okay ... Let's see ... When I was a little girl, my friend Carol and I found this old doll's house in her attic. We sneaked it carefully downstairs and cleaned it off. Carol had a pet mouse, Binkey. So we dressed Binkey up in this white Barbie dress and ...

EMMA: (Ignoring her.) So, I see here that you've listed Sandy in Grease as one of your credits.

ELIZABETH: Oh, yes. It was a great experience. Working with Paul Jones. Do you know him?

EMMA: Didn't anyone ever tell you not to lie on your resume?

ELIZABETH: I didn't.

EMMA: Oh, come now.

ELIZABETH: I didn't. I swear I didn't.

EMMA: There's no character listing here by The Glass Menagerie. Was it done in the absurdist style or did you play the gentleman caller?

ELIZABETH: I played Laura.

EMMA: That must have been some time ago.

ELIZABETH: Last summer.

EMMA: I'm sorry, I didn't mean to interrupt your little story.

ELIZABETH: That's okay ... Uh, where was I ... So, after we dressed Binkey up in the Barbie costume, we placed him inside the doll house and he crawled right into the miniature bathroom as if he wanted to take a bath ...

EMMA: Add a Southern accent.

ELIZABETH: (Adding a Southern accent.) ... Then he got stuck in the miniature hall closet and we had to shake the doll house up and down and then Binkey popped out but he was all hyper and we couldn't catch him so he ran downstairs and Carol's mom was having this big ritzy dinner party and Binkey ran right at ...

EMMA: Let's see a little Spanish.

ELIZABETH: ... la grande jefe de mi madre, pero cuando la senorita jefe ...

EMMA: No. I don't want Spanish dialogue. I want a Spanish accent. Comprende?

ELIZABETH: Oh ... I can't do a Spanish accent.

EMMA: Then at least show me you have some energy ... Act the story out.

ELIZABETH: (A beat. Elizabeth proceeds to act out everything she says.) So, Carol's mother's boss screamed, leaped up onto the couch and pulled up her dress. Well, she wasn't wearing underwear ...

EMMA: Faster.

ELIZABETH: ... Then Carol's mother's boss's husband tried to grab her but instead he knocked her off into the double salsa sour cream dip and ...

EMMA: Faster!

ELIZABETH: ... and Binkey got scared and ran out into the front yard and the whole party went outside to look for him except Carol's mother's boss's husband and Carol's mother's boss who was crying, not because of the double salsa dip or even the flashing incident.

EMMA: No words!

ELIZABETH: Pardon?

EMMA: No words. (Completely enthralled in the story, Elizabeth then acts out the rest of the story without words. This includes a chase scene, fainting, a cat, a dog, maybe even death. Elizabeth finishes with a loud laugh. She can't help but applaud herself.)

EMMA: (A beat. Dryly.) Couldn't think of anything funny, huh?

ELIZABETH: (A long beat. On the verge of tears) Why are you being so rude to me.

EMMA: (Innocently.) Rude. Am I being rude? I'm sorry, Elizabeth. Please continue your quaint little rodent story.

ELIZABETH: I don't want to. I'm leaving.

EMMA: Leaving. You sure? You still have a few seconds left.

ELIZABETH: If you didn't think I was right for the role you should have just said so.

EMMA: Right? You're perfect. I just wanted to make sure you could handle all the terrible things Della must endure.

ELIZABETH: Really?

EMMA: Sure.

ELIZABETH: And?

EMMA: There is no doubt in my mind that you think you would be perfect for this role. I don't think I've ever seen an actress quite like you before.

ELIZABETH: Thank you!

EMMA: But out of fairness I have to finish out the day. I'll call you tomorrow. Mind you, it will be late. Between midnight and 4 A.M. Make sure you're awake and by the phone. If you don't pick up after the first ring, I'll offer Della to someone else.

ELIZABETH: Don't worry. I won't sleep a wink.

EMMA: Good.

ELIZABETH: Anything I should know about the character? Keep in mind?

EMMA: Leave the wig at home. It doesn't fit.

ELIZABETH: Wig?

EMMA: And learn a Spanish accent and combine it with the Southern. You can talk faster too.

ELIZABETH: Even faster?

EMMA: Pace is everything.

ELIZABETH: Okay. I'll work on it tonight.

EMMA: Alright. Run along now. I'll be in touch ... (ELIZABETH smiles and turns to go.) Wait! Your number is 555-8798?

ELIZABETH: Yes.

EMMA: Just wanted to make sure.

ELIZABETH: Thank you. Thank you so much!

EMMA: No, thank you. (ELIZABETH exits. EMMA watches her off. She picks up ELIZABETH's head shot, crosses to the waste basket and throws the head shot away, giggling to herself. A woman enters with coffee and takeout bag.)

SCENE

WOMAN: Hi, can I help you?

EMMA: (Startled.) Yes. (A wide-eyed smile suddenly appears.) Hi, I'm a little early. I saw the door open. Should I wait outside? ... I'll wait outside.

WOMAN: No, that's okay. Do you have your audition card?

EMMA: Yes. (Hands her ELIZABETH’S card.) Here you go ... I must say it's a pleasure to meet you, Ms. Stewart. I've heard great things about your theatre.

WOMAN: Well, thank you. We try.

EMMA: (Trying to be sincere.) John Wyatt says hello.

WOMAN: John! How is he?

EMMA: Great.

WOMAN: Do you have a picture for me?

EMMA: Sure do. (Crosses to bag and pulls out her resume.)

WOMAN: It's like a zoo out there.

EMMA: I know. I had to get here at 6 A.M. just to get an audition card. I didn't think I was going to get to see you. (Elizabeth hands the woman her resume.)

WOMAN: What piece are you doing?

EMMA: A short selection from Agnes of God.

WOMAN: (Smiles.) In that case, you better move back a few steps.

EMMA: Of course. (Emma backs up.) Good morning. My name is Emma Winns.

WOMAN: Wait ... Uh, what role would you like to be considered for, Emma?

EMMA: (A beat.) Della.
```

---

## IC-1288: Ruthless!

- Title: Ruthless!
- Author (byline): Joel Paley
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: July 2016
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: SYLVIA, JUDY, TINA, MISS THORN, LOUISE, NEWSCASTER
- Teaser before the introduction: Yes
- Spoken words (computed): 1347
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joel Paley
ISBN: 978-0573704680
Publisher: Samuel French, Inc.
Date (Month/Year): July 2016
Revised in August 2015 to reflect the 2015 Off Broadway production.
```

### Introduction (context only: never use it for content warnings)

```text
What do you get when you mix a struggling talent agent, a 1950’s style stay-at-home mom, an elementary school teacher who has written her own (probably illegal) version of Pippi Longstocking, and a 3rd grader who knows what she wants and will do anything to get it? You get a parody of the original Bad Seed! You get . . . Ruthless! by Joel Paley
```

### Performance text (classify this)

```text
SYLVIA: (Pg 9) Good evening, my name is Sylvia St. Croix. Where does talent come from? Meet Judy Denmark. (Pg 11) A wife and mother leading an idyllic suburban life, and although Judy has absolutely no talent whatsoever, her only child, her daughter Tina has been blessed with a great deal of talent. Blessed, or dare I say, cursed? But I get ahead of myself.

(Scene opens with Judy answering the telephone – Phone rings)

JUDY: (Pg 12-13) Tina’s mother. . . Hello, Pastor Peters Tina has a choir solo Sunday? Oh, she just loves to sing and yes, she loves to pray. She’s good at everything! She’s positively heaven-sent. My kid’s the perfect 8-year-old. Yes, she’s enthralling. Thank you for calling. Good bye. (She hangs up. Doorbell – Judy answers) Won’t you come in. (Sylvia hands her a business card) Miss St. Croix.

SYLVIA: Please, call me Sylvia. (Pg 14) This lovely home, and of course the very reason I’m here . . . your daughter, Tina. I caught her performance last Saturday at The Rolling Hils Twilight Home for the Elderly. Sensational.

JUDY: We’re very proud of our daughter. (Pg 15) Would you like to meet her? She’s out in the garage breaking in her new tap shoes. (calls off stage) Tina! We have company. (Tina enters) Darling, say hello to Ms. St. Croix.

TINA: (performs a jazzy dance combination) Hi!

SYLVIA: (claps enthusiastically) (Pg 16) Tina, how would you like to be a star?

TINA: Why, it’s all I’ve ever wanted! More than anything in the whole wide world!

SYLVIA: That’s why I’m here. I work with specially gifted children. (to Judy) You are planning a theatrical career for your daughter, are you not?

JUDY: (Pg 17) We want our daughter to have a normal childhood.

TINA: I’ve had a normal childhood! It’s time to move on. (Pg 18) Oh, Mama, please say yes. Please?!

JUDY: Well, I suppose some coaching can’t hurt, but only after school.

SYLVIA: We start this afternoon!

TINA: (shaking her head) Today’s the audition for the school show. I’m trying out for the lead.

SYLVIA: Oh, Judy, you must be so proud. I wish I had a little girl.

JUDY: Don’t you have any children, Sylvia?

SYLVIA: Let’s just say she didn’t have any talent. (Pg 19) Oh, she used to jump around the living room. “Look, Mama, I’m dancing!” But she was merely jumping. It was embarrassing! ******* The Turner School Auditorium – Later that afternoon *******

MISS THORN: (Pg 20) Good afternoon, students. I’m Miss Thorn, and after directing last year’s riveting production of Who’s Afraid of Virginia Woolf, I’m delighted to announce this year, the Turner School will present “Pippi in Tahiti,” the musical written and directed by me (gesturing to herself) Myra Thorn! (Pg 21) And now . . . the starring role of Pippi Lingstocking will be played by . . . Louise Lerman! (Tina clearly is disappointed) ******* The Denmark Living Room – later that afternoon *******

SYLVIA: (Pg 22) You had your heart set on playing Pippi, didn’t you?

TINA: It’s the best part in the show! I don’t understand.

JUDY: Oh, so what if Louise Lerman is playing Pippi -- You get to play Puddles!

TINA: (Showing her true nature) I don’t want to play a dog. I mean, look at me. I was born to play Pippi Longstocking! (She stomps her feet) And Louise Lerman can’t act!

JUDY: Now you listen to me, young lady, do you want to stay in showbusiness?

TINA: (angelic) You’re right, Mother. What would you give me for a bucket of kisses? [doorbell] (Pg 23) I’ll get it. (Opening the door) Why, good afternoon, Miss Thorn. Haven’t changed your mind, have you?

MISS THORN: I’m afraid not. (Tina pouts)

JUDY: Miss Thorn, the reason I’ve asked you here is because Tina’s awfully upset about not playing Pippi.

MISS THORN: I must admit, Mrs. Denmark, I’ve never known anyone to want a part so desperately.

SYLVIA: (Pg 26) My dear Miss Thorn, might you considered letting Tina be the Lerman girl’s understudy?

MISS THORN: We’re only giving one performance, but if it makes you happy then, yes, Tina can be Louise’s understudy.

TINA: Wait a minute. You expect me to learn all of Pippi’s songs and all of Pippi’s lines -- and there’s still a chance I don’t even get to play Pippi?

MISS THORN: (Pg 27) That’s correct.

SYLVIA: Unless, of course, something were to happen to Louise. (she looks knowingly at Tina)

TINA: (Tina gets the message) I’ll do it! ******* The Turner School Auditorium – 6 weeks later *****

MISS THORN: (Pg 32) Okay, let’s take it from after the storm at sea. Rachael Hobbs, stop giggling. This is a theater, not a playground. We’re not here to have fun. Okay, here we go. Take your places for scene five. Go music!

LOUISE: (enters dressed as Pippi Longtocking; looks around in awe) This must be Tahiti! And I’m Pippi! Pippi Longstocking! I’d like you to meet my best friend, Puddles! (An unhappy Tina enters as the dog) (Pg 33) Puddles and I were in a terrible storm. Our boat tipped over and everyone got drowned. But Puddles saved my life and brought me to this tropical paradise. Way to go, Puddles! Shake! (holds out her hand) You’re supposed to shake my hand.

TINA: (with an attitude) Look! I don’t think Puddles would want to shake hands here, ok? Not after being shipwrecked and having to doggy-paddle fifty miles!

LOUISE: I’m sorry, I can’t act with this. (gestures to Tina)

TINA: You can’t act period. The only reason you got the part is because Mommy and Daddy bought it for you.

LOUISE: (Pg 34) Do you honestly think I want to be in this stupid play? It’s embarrassing. But it makes my parents happy, and when Mike and Betty are happy, I’m happy. Got it?

TINA: But I’ve got to play Pippi!

LOUISE: You don’t have the range! (Louise flippantly leaves the stage)

TINA: (menacingly) I ASKED POLITELY. I SAID PLEASE . . . Now there’s nothing left to do but . . .

(Sweetly) Oh, Louise! (exits after Louise) ********* The Denmark Living Room – Later that afternoon*******

NEWSCASTER: (Pg 35) (voice over) Time for the local news. One of the students attending Turner Elementary School accidentally hung herself with a jump rope after falling from a catwalks high above the auditorium. The child’s name is being withheld until parents can be notified. In other news . . .

JUDY: (Pg 36) That poor little girl.

TINA: Tina enters from school) Hello, Mother. We didn’t have our lunch because something bad happened to Louise Lerman. (smiling) Can I have a hamburger?

JUDY: Of course. Now, sweetheart . . . if you want to go to your room . . . if you want to cry – or even stop smiling, I’ll understand.

TINA: Why should I cry? I didn’t get killed. (Tina exits, then doorbell)

MISS THORN: (obviously shaken) Hello, Mrs. Denmark.

JUDY: (Pg 37) Come in, Miss Thorn. Of course, the play has been canceled.

MISS THORN: Whatever gave you that idea? I think this is an excellent opportunity for the children to learn that the show must go on!

JUDY: (Pg 38) But it’s wrong. Shockingly wrong!

MISS THORN: (Pg 37) How’s Tina. She is the understudy. (losing it) (Pg 38) Look, Mrs. D! That talented little girl of yours better be in costume and in place by show time, or I shall be forced to go to the police!

JUDY: The police?!

MISS THORN: It seems the Pippi wig is missing. Now, Tina was seen chasing Louise and snatching at the wig. But, I suspect nothing. Not a thing.

JUDY: Why don’t you just come out and say it? Look me straight in the eye and tell me that my eight-year-old child killed for a part in the school play.

MISS THORN: Not just any part, Mrs. Denmark. The lead! (she storms out) *********

JUDY: (Pg 39) [Judy notices Tina’s school bag by the door, she unzips it and pulls out the Pippi wig andwhispers in horror) Tina!

TINA: Did you call me, Mother?

JUDY: What are you doing with Louise Lerman’s Pippi wig? And don’t lie.

TINA: (with feigned innocence) I found it after Louise had her. . . accident. I was afraid to give it to Miss Thorn. Afraid Miss Thorn would think I was naughty.

JUDY: Were you naughty, Tina?

TINA: (innocently) Oh, no, Mommy. I wasn’t naughty. I found the wig and put it in my bag so it wouldn’t get lost. (Pg 40) [Besides] It’s my wig and it’s my part! (beat) I love you and I think you’re the best mother in the whole wide world. That’s what I tell everyone.

JUDY: Knock it off, Tina. You’re not that good! You did it, didn’t you? You killed Louise Lerman for a part in a play?

TINA: Not just any part, Mother! The lead! I told Louise I had to play Pippi. But she said I didn’t have the range. So, I chased her up onto the catwalk. That’s when she gave me the wig. I asked her if that meant I could play Pippi and she said . . . “Yeah, over my dead body!” So I wrapped the jump rope around her fat neck and pushed her over the side.

JUDY: Oh, Tina, Tina!

TINA: I wanted the part. What could I do?

JUDY: You could have hurt her. You didn’t have to kill her.

TINA: (Pg 41) I wasn’t thinking. I was tired and I didn’t have my lunch.

JUDY: Look at me, Tina. You did a bad thing, a very bad thing. You killed that little girl Do you know what that means?

TINA: (beat and then with an evil smile) Yeah, it means I’m playing Pippi!
```

---

## IC-1289: Saving Grace

- Title: Saving Grace
- Author (byline): Cynthia L. Cooper
- Work: Elvis Monologues
- Publisher: Heinemann Drama
- Publication date as stated: Dec 1997
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1473
- Already set (do not supply): none

### Source block (context only)

```text
Author: Cynthia L. Cooper
Book: Elvis Monologues
ISBN: 0435070444
Publisher: Heinemann Drama
Date(Month/Year): Dec 1997
```

### Introduction (context only: never use it for content warnings)

```text
We the undersigned, in our enduring love for Elvis, implore all those involved in cloning to hear our plea. One cell would allow future generations to witness his presence. The technology is here, and this petition is a testament to our will. Bacteria, sheep, monkeys—all cloned! Some fear the possibilities. I urge you to seize them. Americans for Cloning Elvis (ACE) requests your support. Make your view known around the world by signing our petition.

Seriously, the organization exists and likely prompted this monologue in response . . . Saving Grace by Cynthia L. Cooper

(JANEANNE, wearing a lab coat, sits at a bare unadorned desk, leaning across. Unseen is an investigator, to whom she speaks. She suddenly leans back, closes her eyes for a moment, and begins to sway in her seat. SHE takes a deep breath, opens her eyes and begins to sing, demonstrating great feeling if minimal ability.)
```

### Performance text (classify this)

```text
Characters: JaneAnne – a mature woman lab worker with a reasonable respect for Elvis. She speaks to an unseen investigative agent.

"Love me tender, love me true ..." 1956. Title of Elvis' first movie, too; same year. (SHE hums.)

So you don't like my singing. I can tell by the way you look down at your pad, pretending there's some very important information you have to write down for the captain. Well, you don't like my singing, and I didn't like what they were doing to Elvis. So that's why I did something about it.

Oh, I heard when you said it's not about arrest. "You're merely conducting an investigation into potentially improper expenditure of government funds." What are you? FBI? Or was it the Food and Drug Administration -- the FDA? Or did you say the FTC? Or the CDC? All those people in all those agencies with all those letters who are all interested in investigating DNA. And Elvis. And little old me.

Well, you can bust me if you want to. I don't care. All those letters get right to the heart of the problem. I saw it when I first went back into biology. I discovered that people had lost the feel of things.

Like take DNA. That's all wrong. Three lousy letters. It's deoxyribonucleic acid. God, I love the sound of it so much. Deoxyribonucleic acid. Deoxyribonucleic acid. I feel like I'm making beautiful music every time I say it. And it's just one part. When you really get behind deoxyribonucleic acid -- put your body and feeling and emotion under DNA -- deoxyribonucleic acid -- ahhh ...that is fine. Really, really fine.

(SHE says the last line as if SHE is in love.) But even really fine things need tender loving care. (SHE stands, as if stepping back into the lab.)

The director gave a little seminar to all of us new people when I was first hired at the lab. (SHE becomes the director.)

"One day because of our work on something invisible to the eye -- DNA -- we will begin to know the complete identity of humans. We will know every nucleotide, every A, C, G and T inside the human body, all three billion elements of the interior code that defines a person completely, making an exact blueprint for every human being."

Suffice to say, I was about the oldest one there. I'd come back to biology after having two kids. So maybe my understanding of history was a little different -- at least on certain points. I'd sit and listen at lunch hour. (She becomes three other technicians.)

"Imagine," said one, "if we could figure out the complete DNA code of one really famous person."

"Yeah," said another, "even if DNA has three billion elements, that's still quantifiable. It's not infinity."

"And there is money in it. People are willing to put up investment capital for DNA banks, that kind of thing."

"But you'd need one really famous person."

"There's Einstein ..."

"Not splashy enough."

"Queen Elizabeth."

"No one really cares."

"Shakespeare."

"Too esoteric."

(To investigator.)

These names went round and round like a hound dog crying all the time, and, as I recall, that's when Elvis first came up.

(As the characters.)

"Think about all the Elvis imitators."

"If -- we could actually discover Elvis' complete DNA code..."

"and alter a person's genes to make a new Elvis, a real Elvis, someone with the exact genetic makeup of Elvis, we'd be ..."

"Rich."

(To investigator.)

"Rich." That's what they said. How could they understand? Watson and Crick only discovered the double helix one year before "That's All Right, Mama." The people in the labs were so-o young. They had no perspective.

Think of it. If these people really understood DNA -- or Elvis -- they would listen to the words -- roll them around in their mouths, let them melt under their tongues, and then let them out gently, mellifluously, with tenderness. Take the DNA bases. Even the director called them by their initials: A or G or C or T. When the words are so marvelous -- "Adenine." "Guanine." "Cytosine." "Thymine." But all the people in the labs say are A or G or C or T. As if you could sing 'Don't be C' and that would suffice for "cruel" or 'don't step on my B Suede Shoes' and that would make up for "blue." No, I believe that people in the labs have no concept of the artistic.

Still, I didn't pay much mind. I took the lunch discussions as idle chatter. Because it didn't seem really possible. And then more and more things kept happening. New testing. New equipment. Funding. Grants. More genes on the genome were identified. The pace accelerated. And then one day people were huddled in a corner.

(Acting as other characters.)

"If someone pretended to be a journalist and got an interview with Lisa-Marie, and then Lisa-Marie had something to drink, and we got the saliva off the rim of the glass, and extracted DNA ..."

"You'd still only have offspring with Elvis and Priscilla's DNA. There's a better way. Elvis had a twin, but the twin died at birth. No one knows exactly where the twin is buried. But twins, if they are identical, have the same DNA. So if we went down to Tupelo with one of those laser probes, and found the body of ..."

"Wait. We can keep it simple. If one of us visited Graceland and got a swab off an item of clothing -- where he sweated, the armpits or collar, for example on the gold lame suit or the karate robe -- we could test that."

(To investigator)

I still didn't think anything of it. But then one day, one of the technicians mentioned that he was taking a vacation in Memphis. Everyone else nodded and smiled.

I'm not paranoid. I saw it with my own eyes. My back stiffened. Elvis' song, "Don't," started pumping through my brain, as if he were singing to me personally.

(Confidentially.) They were working on a secret plan to identify the entire genetic code of Elvis, which they planned to sell to a commercial entity for harvesting -- to recreate Elvis. And it was happening right here in a research lab supported with government money.

(More voluble.) I want you to understand one thing. I am not a fanatic. I am not one of those people who celebrates Elvis' birth and memorializes his death. I don't make pilgrimages to Graceland. But they didn't understand Elvis at all.

See, DNA, genes -- they don't tell the whole story. Because you could know every vowel in "Love Me Tender" and sing every note, like I do. But you still wouldn't be Elvis. You still wouldn't have that wonderful curl at the end of a phrase, that little hiccup of delight that injects surprise, that deep boom and slow slide up, the saving grace, that made Elvis. Notes don't make a song, and you could name all the genes in a person's body, but you wouldn't have a singer. You wouldn't have his smile; the eyes that could take in an audience; his soul.

After this technician came back, my suspicions grew. I noticed a group of people working late each night. There were hushed conversations, passed notes, winking and blinking. They always seemed intent on ushering me out the door as soon as possible at the end of the work day.

I watched this for several days. And then I couldn't take it anymore. While they were at lunch, I snuck to the back and stole the key to the locked refrigerator from one of the drawers. Then I opened the refrigerator. And just as I suspected there were fresh vials in there. Vials marked "E," like "E-1," "E-2," E-3." You know what that meant.

And there were notes on one of the tables. Had "G Information" on them, and that stood for Graceland. My suspicions were confirmed.

After that, I didn't waste any time. I knew what I had to do. I had to save Elvis.

I took the "E" "1-2-3" vials, stuck them in my shirt, checked out with the guard, flashing my badge, of course, and walked out the door, down to the strip -- the commercial strip -- looking for the right place. I came to a toy store and I knew that's what he wanted. I could hear him singing to me, "I only want to be your teddy bear." I poured out the vials on the sidewalk. 1-2-3. And then I smashed the vials. 1-2-3. I destroyed private property. And then I tore up the notes into little bits, and destroyed some more.

And I'm the one left all those no-name messages with you and every other high-'faluting agency I could think of and said there was something you ought to know. You're just the first to show.

But I don't care if you know my name anymore. "I don't care if the sun don't shine." Because there will be only one King.

(Hums 'Love Me Tender.' Sits back down.) The name'sJaneanne. So does that answer all of your questions?
```

---

## IC-1290: The Search for Signs of Intelligent Life in the Universe

- Title: The Search for Signs of Intelligent Life in the Universe
- Author (byline): Jane Wagner and Lily Tomlin
- Work: Not specified
- Publisher: HarperCollins Publishers, Inc
- Publication date as stated: March 1991
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: TRUDY
- Teaser before the introduction: Yes
- Spoken words (computed): 1210
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jane Wagner and Lily Tomlin
ISBN: 978-0060920715
Publisher: HarperCollins Publishers, Inc
Date (Month/Year): March 1991
```

### Introduction (context only: never use it for content warnings)

```text
Searching for Signs of Intelligent Life in the Universe by Jane Wagner
```

### Performance text (classify this)

```text
TRUDY: Here we are, standing on the corner of “Walk don’t walk.” You look away from me, trying not to catch my eye, but you didn’t turn fast enough, did you? You don’t like my raspy voice, do you? I got this raspy voice ‘cause I have to yell all the time ‘cause nobody around here ever LISTENS to me.

You don’t like that I scratch so much; yes. And excuse me, I scratch so much ‘cause my neurons are on fire. And I admit my smile is not at its Pepsodent best ‘cause I think my caps must’ve somehow got osteoperosis. And if my eyes seem to be twirling around like fruit flies, the better to see you with, my dears!

Look at me. You mammalian-brained LUNKHEADS! I’m not just talking to myself, I’m talking to you, too. And you And you And you And you and you and you!

TRUDY: I know what you’re thinking, you’re thinkin’ that I’m crazy. You think I give a hoot? You people! Look at my shopping bags. Call me crazy, cause I save this junk. What should we call the ones who buy it?

It’s my belief we all, at one time or another, secretly ask ourselves the question: Am I crazy.. In my case, the answer came back: A resounding YES!

In my case, the symptoms are subtle but unmistakable to the trained eye. For instance, here I am, standing at the corner of “Walk, Don’t Walk.” Waiting for these aliens from outer space to show up. I call that crazy, don’t you? If I were sane, I should be waiting for the light like everybody else.

They’re late . . . as usual. You’d think, as much as they know about time travel, they could be on time once in a while. I could kick myself. I told ‘em I’d meet ‘em on the corner of “Walk, Don’t Walk” ’round lunchtime. Do they even know what “lunch” means? I doubt it. And “round” -- why did I say “round” Why wasn’t I more specific?

Now they’re probably stuck somewhere in time, wondering what I meant by ”round lunchtime” And when they get here, they’ll be dying to know what “lunchtime” means. And when they find out it means going to Howard Johnson’s for fried clams, I wonder, will they be just a bit let down. I dread having to explain tarter sauce.

I know what you’re thinking, you’re thinkin’ that I’m crazy. But frankly, goin’ crazy was the best thing that ever happened to me. I don’t say it’s for everybody; some people couldn’t cope. But for me it came at a time when nothing else seemed to be working. I got the kind of madness Socrates talked about, a divine release of the soul from the yoke of custom and convention. I refuse to be intimidated by reality anymore.

After all, what is reality anyway. Nothin’ but a collective hunch. My space chums think reality was once a primitive method of crowd control that got out of hand. In my view, it’s absurdity dressed up in a three-piece business suit. Reality is the leading cause of stress amongst those in touch with it. I can take it in small does, but as a lifestyle, I found it too confining. With all I have to do, I had to let something go.

Now, since I put reality on a back burner, my days are jam-packed and fun-filled. Some days, I go hand out around Seventh Avenue; I love to do this old joke: I wait for some music-loving tourist from one of the hotels on Central Park to go up and ask someone, “How do I get to Carnegie Hall.” Then I run up and yell, “Practice!” The expression on people’s faces is priceless. I never could’ve done stuff like that when I was in my right mind. I’d be worried people would think I was crazy.

When I think of the fun I missed, I try not to be bitter. See, the human mind is kind of like a piñata. When it breaks open, there’s a lot of surprises inside.

I was not always a bag lady, you know. I used to be a designer and creative consultant for big companies! Who do you think thought up the color scheme for Howard Johnson’s? At the time, nobody was using orange and aqua together with fried clams.

Laugh tracks: I gave TV sitcoms the idea for canned laughter. I got the idea, one day I head voices and no one was there.

Who do you think had the idea to package panty hose in a plastic goose egg. One thing I personally don’t like about panty hose, when you roll ‘em down to the ankles the way I like ‘em, you can’t walk too good. People seem amused, so what’s a little loss of dignity. You got to admit: It’s a look!

The only idea I’m proud of -- my umbrella hat. Protects against sunstroke, rain, and muggers. For some reason, muggers steer clear of people wearing umbrella hats. So it should come as no shock. I am now creative consultant to these aliens from outer space. They’re a kinda cosmic fact-finding committee. Amongst other projects, they’ve been searching all over for sign of intelligent life. It’s a lot trickier than it sounds.

We’re collecting all kinds of data about life here on Earth. We’re determined to figure out, once and for all, just what the hell it all means. I write the data in these Post-its and then we study it. Don’t worry, before I took the consulting job, I gave ‘em my whole psychohistory. I told ‘em what drove me crazy was my last creative consultant job with the Ritz Cracker mogul, Mr. Nabisco. It was my job to come up with snack inspirations to increase sales. I got this idea to give Cracker Consciousness to the entire planet.

I said, “Mr. Nabisco, sir! You could be the first to see the concept of munching to the third world. We got an untapped market here! These countries got million and millions of people don’t even know where their next meal is coming from. So the idea of eatin’ between meals is somethin’ just never occurred to ‘em!”

Must’ve been when I went off the deep end. I woke up in the nuthouse. They were hookin’ me up. One thing they don’t tell you about shock treatments, for months afterwards you got flyaway hair. And it used to be my best feature. See, those shock treatments gave me new electrical circuitry (I think one of the doctors. hands must’ve been wet). I started having these time-space continuum shifts, I guess you’d call it. Suddenly, it was like my central nervous system had a patio addition out back. Not only do I have a linkup to extraterrestrial channels. I also got a hookup with humanity as a whole. Animals and plants, too. I used to talk to plants all the time; then, one day, they started talking back. They said, “Trudy, shut up!”

(mutters to herself for a moment, then peers at the sky) I told ‘em I’d meet ‘em on the corner of “Walk, Don’t Walk.” They’re late . . . as usual. You’d think, as much as they know about time travel, they could be on time once in a while. (mutters again and shuffles off)
```

---

## IC-1291: Seriously, Cinderella is So Annoying!

- Title: Seriously, Cinderella is So Annoying!
- Author (byline): Trisha Shaskan
- Work: Not specified
- Publisher: Capstone Press
- Publication date as stated: August 2011
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: STEPMOTHER, HUSBAND, CINDY, NARRATOR, STEPSISTER 1, STEPSISTER 2, FOOTMAN, STEPSISTERS
- Teaser before the introduction: Yes
- Spoken words (computed): 718
- Already set (do not supply): none

### Source block (context only)

```text
Author: Trisha Shaskan
ISBN: 978-1404870482
Publisher: Capstone Press
Date (Month/Year): August 2011
```

### Introduction (context only: never use it for content warnings)

```text
Every story has two sides. It just so happens that we usually hear from the victim’s or protagonist’s point of view. In the classic retelling of the Cinderella story, the Stepmother has her own opinion of miss goody-two-shoes in. . .

Seriously, Cinderella is So Annoying!: The Story of Cinderella as Told by The Wicked Stepmother by Trisha Shaskan.
```

### Performance text (classify this)

```text
STEPMOTHER: You must have heard of me. The wicked stepmother? That’s not true. It’s just another one of Cinderella’s wild stories. Not as wild as the one about the pumpkin, or the one about the fairy godmother. The real story, the true story, began with some chatter- and some dust.

STEPMOTHER: All I ever wanted was a husband and a mansion. Before I married Cindy’s father, my two darlings and I had met Cindy only a few times. The girl had seemed normal then. After I married Cindy’s father, my darlings and I moved in. When I had just one foot on the front step, my dear husband kissed me and said,

HUSBAND: I’m off on business!

CINDY: He’s often away, but the animals stay put. They talk. They joke. They sing. They even help out - especially the bluebirds.

STEPMOTHER: Now, I don’t mind a good story but I do prefer facts to fiction. Soon, the girl was talking all kinds of nonsense.

CINDY: Once upon a time, one of the bluebirds became blue. Not the color. The feeling. His friend had flown south . . . .

STEPMOTHER: My darlings and I were stuck near the front door. I just wanted to put away my bags. That’s when I saw it: dust. (To Cindy) Dear, is the whole house this dusty?

CINDY: I don’t know. I’ll give you a tour!

STEPMOTHER: In the dining room, Cindy told stories. . . In the study, Cindy told stories. Non-stop. (To the girls) Girls, time to get to work. This place needs a good cleaning.

CINDY: Once upon a time when I was cleaning . . .

STEPMOTHER: Oh dear. Cindy mopped the floor. She finished so fast! My darlings had barely started.

CINDY: Did you know robins and sparrows are my friends? The sparrows don’t like the robins, though. Silly creatures! Once upon a time, one of the robins . . .

STEPMOTHER: Cindy, dear, why don’t you go and wash the clothes now, hmm? (To audience) Cindy washed them so fast! How on Earth did she do it? I had to find her another chore, just to keep her busy.

CINDY: If there’s one thing squirrels love, it’s washing clothes. The rats, though, would rather iron. You know, I . . . ”

STEPMOTHER: Squirrels and rats doing laundry? (To Cindy) Stop telling such foolish stories!” (To audience) Time passed but nothing changed. In the garden, Cindy told stories. In the kitchen, Cindy told stories. At dinner I could hear myself think. (To Cindy) Dear please, STOP TALKING! (To audience) Cindy didn’t stop.

NARRATOR: One day, a letter arrived. It was an invitation to the king’s ball. The prince would sure fall in love with one of my darlings. then they would marry, live in a beautiful castle and be the king and queen of the land!

CINDY: Oh Stepmother, I want to go too! Once upon a time a girl and a prince . . .

STEPMOTHER: Then just like that Cindy lost her voice. Imagine! It had to be from all that storytelling. Well, what could I do? I told her she had to stay home for her health. She cried, of course. Still, a ball was no place for a poorly girl. She needed rest. Sometimes it was hard being a stepmother.

NARRATOR: At the ball my darlings twirled, they whirled. Then a strange girl walked in. Her gown was magnificent. I couldn’t take my eyes off it. I wondered how much it would cost if my seamstress could copy it for me.

The prince and the girl danced and pranced while my darlings were left prince-less A few days later, the prince made an announcement: a glass slipper was left at the castle. The prince would marry the girl whose foot it fitted. Our big chance! After visiting every other mansion in the city, the prince’s footman arrived at the door.

STEPSISTER 1: Me! Me!

STEPSISTER 2: NO! Me me.

FOOTMAN: One at a time.

STEPMOTHER: Each girl tried, but the shoe didn’t fit. Then Cindy croaked out a whisper. . .

CINDY: P . . . P . . . please let me try.

STEPMOTHER: The shoe fit! Cindy pulled out the other glass shoe from her apron pocket.

STEPSISTERS: WHAAAT!

STEPMOTHER: Cindy croaked again. She said something about a pumpkin and mice that turned into horses. She even added something about a fairy godmother. PLEASE, there is no such thing! I must say, I still don’t know where she got those shoes . . . A few days later, the prince married Cindy - the poor man had no idea what he was getting himself into. We, on the other hand, lived happily ever after.
```

---

## IC-1292: She Kills Monsters

- Title: She Kills Monsters
- Author (byline): Qui Nguyen
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: Oct 2012
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, TILLY, AGNES, CHUCK, KALIOPE, LILITH, EVIL TINA, EVIL GABBI, ORCUS/RONNIE
- Teaser before the introduction: Yes
- Spoken words (computed): 2129
- Already set (do not supply): none

### Source block (context only)

```text
Author: Qui Nguyen
ISBN: 978-0573700569
Publisher: Samuel French, Inc.
Date (Month/Year): Oct 2012
```

### Introduction (context only: never use it for content warnings)

```text
One day as Agnes, a teacher at Tilly’s high school, is going through her sister’s things, she finds a notebook -- a Dungeons and Dragons notebook. It becomes her mission to find out more about her sister Tilly by deciphering the contents of that notebook. And thus a quest begins . . . a quest that forges a link between Agnes’ reality and Tilly’s fantasy. She Kills Monsters By Qui Nguyen
```

### Performance text (classify this)

```text
NARRATOR: (Pg 7-8) In a time before Facebook and Worlds of Warcraft, there once existed simply a game -- Forged by the hands of nerds and crafted in the minds of geeks. And here in the land of Ohio during the year of 1995, one of the rarest types of geeks walked the earth -- Tilly Evans. Lights up on TILLY, a teenage girl decked out in full D&D armor with a sword in hand. She is surrounded by a horde of goblin-like creatures. Suddenly they attack! TILLY slays each of the monsters with grace and efficiency. She stands poised over their dead bodies as the NARRATOR continues. . .

NARRATOR: But this story isn’t about her. . . This story is about her sister Agnes, the girl who never left home. . . Agnes Evans grew up average. She had average parents and grew up in the average town of Athens, Ohio with her little sister Tilly. Tilly however was anything but average.

TILLY: What are you doing?

AGNES: Talking on the phone. What are you doing?

TILLY: Trying to re-animate a dead lizard with the power of electricity.

AGNES: Oh, okay. . . WHAT!?!

NARRATOR: Being a bit more than half a decade apart in age, the two girls had very little in common. Agnes was into more typical things such as boys, music, and popular television programs, while her sister Tilly became fascinated with the dark arts - magic, dragons, and silly costumes . . . As Agnes grew, she became more engrossed with transcending her averageness and made one grand wish on the night of her college graduation that she would forever regret.

AGNES: I wish my life was less boring.

NARRATOR: And so the Gods answered her wish by smiting down her loved ones in a single car crash. But this isn’t the story of those tragedies. It is a story about how Agnes, the girl who never left home, finally found a way out. . .

Lights come up on CHUCK, a nerdy teen working the counter of a “RPG Gaming Store”

CHUCK: (Pg 9-11) (Singing to himself - Agnes enters and pokes his shoulder which startles him) WHOA, WHAT THE . . .

AGNES: Sorry, I didn’t mean to scare you – I’m looking for a Chuck Biggs?

CHUCK: You’re looking at him! So what can I do for you?

AGNES: Rumor has it you know a thing or two about D&D. I have this thing. I’m not quite sure what it is.

CHUCK: Well, lemme checkity check it out! (AGNES hands CHUCK the notebook) It’s like a map for a D&D game. An adventure. – whoa, wait just a minute. Tillius the Paladin? Was this written by Tilly Evans?

AGNES: You know her?

CHUCK: You kiddin’, right? Every player here in Athens has been on a campaign with her. How’d you get ahold of this?

AGNES: She’s, um, my sister. So can you help me figure out what it all means? I want to play it. . .

TILLY: (Pg 13) (only Agnes can hear) You’re going to suck at this. You don’t even know the difference between a mage or a wizard. You’re going to die five seconds into it.

AGNES: Well, you’re already dead, so we’ll at least have that in common. Chuck. Go. (the scene changes to one of pure fantasy)

CHUCK: (Speaking all-wizard-y on a lower octave) Greetings, Adventurer! I am Chuck Biggs and I will be your Dungeon Master! (Pg 15) Welcome to the Quest for the Lost Soul of Athens. Your mission is find and free the Lost Soul before it is devoured by the dark forces of darkness forever.

TILLY: (Pg 14-15) Fine! If you’re serious about this, then I guess you’re going to have to meet the rest of the team.

AGNES: What team?

TILLY: Every adventurer has a party. This one’s mine. (The Actress playing Agnes portrays each member of the party as they are introduced: Suddenly, a leather-clad warrior LILITH appears -- red eyes, vampire fangs, with a very large battle axe) First up is Lilith Morningstar. Class: Demon Queen. She acts as our squad’s muscle -- a perfect combination of both beauty and brawn. (Next, a very pale, white-haired elf -- tall, lean, and armed with an wooden staff. She looks like a super model) Next up is Kaliope Darkwalker. Class: Dark Elf. Along with her natural Elvin athleticism and a**-kicking abilities, she’s also a master tracker and has a few magical surprises up her sleeves. And then there’s me. I’m the brains of this operation. Name: Tilly Evans aka Tillius the Paladin, healer of the wounded and the protector of lights. Class: Awesome! (both actresses do poses with their weapons as if they’re at a photo shoot)

TILLY: (Pg 16-17) Kaliope, any word on Orcus’s location?

AGNES: What’s an Orcus?

TILLY: Orcus is a demon overlord of the underworld. If there’s a lost soul, he’ll either have it or at least know where it is. So, Kaliope, location?

KALIOPE: The entrance to the cave of Orcus is at the next bend.

TILLY: Actually, Agnes, before we can go any further. We’re going to have to build you a character. I mean you can’t just walk around looking like that. You’re going to at least need a shield. . . And your alignment.

AGNES: My what?

LILITH: Are you good, lawful, chaotic, unlawful, evil?

AGNES: I’m a Democrat.

TILLY: No, what will be your character name?

AGNES: Agnes.

TILLY: Stop being an ass-hat, Agnes.

AGNES: No, I want to just use my name. Agnes.

LILITH: Fine, then it is decided, you are Agnes the Ass-hatted. (Pg 32-33) (Lilith kisses Tilly)

AGNES: Whoa! Wait just a minute! You two are a couple? (To Tilly) Oh, I get it. You two are dating because Tillius is a guy character.

TILLY: No. Tillius is a D&D name. I’m female, she’s female.

AGNES: So your character’s gay?

TILLY: Does that bother you, Agnes? Wow, I never took you for a homophobe.

AGNES: I’m not a homophobe! I thought I knew you, Tilly. At least good enough to know whether you dug boys or girls at this point in your life.

TILLY: You were busy.

AGNES: Not too busy to know this! Tilly, I’m your sister. I shouldn’t have to learn about you through a role-playing game.

TILLY: At least you’re getting to learn something about me.

NARRATOR: (Pg 18-19) And so it was that Agnes the Ass-hatted and Tillius the Paladin ventured forth into the dark dwellings of the truly evil in search for the lost soul of Athens. (The girls jump out from hiding with weapons drawn.)

TILLY: It is I, the great Paladin Tillius, healer of the wounded, defender of lights, and I have come here to free a soul. . . Mine.

AGNES: Wait, you’re the lost soul of Athens? Explosive lights and sound as two cheerleaders walk onto stage. They look like normal cheerleaders, except they have sharp teeth, bat wings, and blood all over their mouths. Clearly a scene Tilly experienced at school written into her D&D campaign

EVIL TINA: (Pg 35-36) (to Tilly) Were you just looking at me?

EVIL GABBI: I think the reason why she was looking at you, Evil Tina, is because she has the hots for you.

TILLY: That’s not true.

EVIL TINA: Are you saying I’m ugly?

TILLY: No.

EVIL TINA: Then do you think I’m pretty? Of course you think I’m pretty . . . I knew you were gay!

AGNES: (AGNES marches up to the two bullies) (Pg 37) And you two going to die! (Both cheerleaders smile and begin laughing. Their laughter consumes AGNES and TILLY. Their laughter becomes painful and then becomes agony)

EVIL TINA: We’ll see you around. Lesbians. (They skip away)

AGNES: Are you okay? (Pg 41) Did that sorta stuff really happen? I mean in real life?

TILLY: I was a dorky fifteen-year old closeted lesbian, what do you think?

AGNES: So how come you had to make a game to tell me all this?

TILLY: I didn’t want to tell you all this! This game was supposed to be private. *******

(Scene change back to the real world. Agnes is at school, working in her classroom. EVIL TINA and EVIL GABBI enter. Except they aren’t evil this time, they’re just students. No wings or horns or bloody mouths, just regular cheerleaders. And they’re super chipper and nice.)

EVIL TINA: (Pg 51-52) Hello, Miss Evans!

EVIL GABBI: Do you have a moment?

EVIL TINA: We’re selling Ads for this year’s yearbook and we were wondering if you’d be interested in buying an Ad? It could just be a “Congratulations to the Class of 95!” Or a dedication to a loved one who would be graduating this year. . .

EVIL GABBI: (whispers) TINA!

EVIL TINA: (to GABBI) Shhh. (to AGNES) So what do you think?

AGNES: You were in the same class as my sister, right?

EVIL TINA: We were both just devastated when we found out. I mean we didn’t hang out after school alot, but –

EVIL GABBI: We’d both consider her a very close friend.

AGNES: Is that right?

EVIL TINA: Not to be too bold, but I think buying a full page AD for Tilly would be. . . just amazing.

AGNES: Can I see your yearbook there? (Agnes violently throws it) GET THE HELL OUT OF MY CLASSROOM!!! (The two girls run out; Agnes calms herself) Am I going crazy?

TILLY: (appears from nowhere) That seemed really effective

AGNES: What am I supposed to do, Tilly? I can’t beat up students.

(Pg 57) Explosion. Evil Tina and Evil Gabbi are back in their evil forms. (TILLY and AGNES fall into defensive stances)

EVIL GABBI: Oh my God, Evil Tina, look! An impenetrable wall of losers.

EVIL TINA: (Pg 58) (they corner Tilly) Awww, look at the little nerd girl.

AGNES: Tilly, shoot them with a magic missile.

TILLY: (cowed) I can’t. I forgot the spell.

EVIL GABBI: Are you going to pee your pants.

EVIL TINA: Say good-bye, lezzie. (Pg 59) You can’t hope to beat us.

EVIL GABBI: We’re way too powerful for you.

KALIOPE: There’s only one way to beat a succubus.

AGNES: [I] challenge you. . . to a dance battle.

CHUCK: BONUS ROUND: AGNES VERSUS THE EVIL SUCCUBUS CHEERLEADER!!! Music fills the house as AGNES and EVIL GABBI go at it in a full-on cheerleader’esque dance battle. AGNES starts it out. She looks good. . . comedic and funny, but still good. EVIL GABBI is unimpressed by AGNES’s skills. She smiles, steps in and starts doing an elaborate Cheerleading/hip-hop fusion routine that completely kills it. Thinking she’s won, she raises her arms in victory. When she does, AGNES picks up her weapon and drives it through GABBI while she isn’t looking!

AGNES: (smiles coyly) What? You really thought we were gonna dance battle you to death. Wow, I guess my sister’s right. Cheerleaders are dumb. (Agnes kills them both then breaks into tears)

TILLY: (Pg 61) Stop. It’s just a game.

AGNES: I was getting to know you. I was just starting to get to know you.

TILLY: My character’s not dead.

AGNES: But you are. This is a stupid game and you’re not real and none of this matters because you died. I’m done. I’m done talking to ghost. *******

(Scene changes back to reality. Agnes is at home sorting through Tilly’s D&D things) AGNES:(Pg 62-63) (to audience) That game was all I had of her. Just a stupid character sheet and whatever she left scribbled out in that notebook. . . My memories are shit. This little nerdy girl who I never talked to, who I ignored, who I didn’t understand because she didn’t live in the same world as I did. Her world was filled with lesbian demon queens while mine . . . had George Michael and leg-warmers. I didn’t even know she didn’t like boys. I didn’t know her. That breaks my heart. (a knock at the door) What are you doing here, Chuck?

CHUCK: I just wanted to show you something. It’s something of Tilly’s.

AGNES: What? AGNES gets up and follows CHUCK. A door appears. CHUCK knocks on it.

CHUCK: (Pg 64-66) I just wanted you to meet some of Tilly’s friends. Ronnie, this is who I was telling you about. So is your sister around?

ORCUS/RONNIE: Yeah. Lemme get her. You guys can come in if you want, just don’t touch the TV, I’m recording Power Rangers! They enter his house.

NARRATOR: Ronnie (ORCUS) returns with his sister Kelly (KALIOPE). She’s wheel-chair bound.

KALIOPE: What? Do I have something on my face?

AGNES: Um, no, it’s just. . .You play D&D with these guys?

KALIOPE: Yeah, well. It was actually your kid sister that convinced me give it a shot. Your sister was awesome, Miss Evans. We loved her. We really miss her.

AGNES: Me too. (TILLY enters)

TILLY: What are you doing?

AGNES: I’m getting to know your friends.

TILLY: I know they’re geeky, I’m geeky, we’re all geeks.

AGNES: Why do you think I care about that stuff?

TILLY: Everyone else does or did. I mean until I died in a car crash and then suddenly, wow, I’m the most popular girl in school.

AGNES: Is that why all you guys play this?

TILLY: No, we play it because it’s awesome. It’s about adventures and saving the world and having magic. And maybe, in some capacity, it might have a little to do with wish fulfillment. Kelly gets to walk again and Ronnie gets to be super strong . . . and me? I get the girl. Lights come up on the “real life” high schooler LILITH. AGNES approaches.

AGNES: (Pg 66-67) Can we talk for a minute? Look, I know you’re not gay or . . . You were at her funeral.

LILITH: I mean, she wasn’t my girlfriend, but I always knew she was, you know, interested. Tilly was my first kiss. I’m pretty sure I was hers too. I thought you’d might want to know that about your sister. And Miss Evans - I loved her. (Lilith exits)

TILLY: (Pg 70-71) Good job.

AGNES: Tilly? (sadly resigned) You’re not real. You’re gone.

TILLY: But this story remains. And isn’t that all that life is - a collection of stories? This is one of mine. . .

(TILLY speaks the next lines, assuming the character voices that she created) AS KALIOPE: . . . and not just some story that I experienced like a party or a dance, but something I dreamt – AS

LILITH: Something far more personal and important than happenstance. This story came from my soul and by breathing life into it, who knows? AS ORCUS: Maybe a bit of my soul gets the chance to breathe for a moment once again. AS CHUCK: I love you, my sister. AS TILLY: I’m sorry I can’t be there. AS CHUCK: I have no idea why you had to experience this adventure alone without me. But I hope it gave you a glimpse into me the way I wanted you to see me – AS ORCUS: Strong... AS LILITH: Powerful... AS KALIOPE: And magical. AS CHUCK: Congratulations, you have finished the Quest for the Lost Soul of Athens.

NARRATOR: And so . . . Agnes the Ass-hatted accomplished her very first quest. Tilly was never forgotten, and eventually the world finally embraced nerds not as outsiders, but as awesome. Agnes moved out of that old house and brought the many memories of an average life with her. And this made her happy.
```

---

## IC-1293: The Sims

- Title: The Sims
- Author (byline): Lori Notaro
- Work: I Love Everybody (and Other Atrocious Lies)
- Publisher: Villard
- Publication date as stated: July 2002
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: HUSBAND, WIFE, CLERK
- Teaser before the introduction: Yes
- Spoken words (computed): 1606
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lori Notaro
Book: I Love Everybody (and Other Atrocious Lies)
ISBN: 978-0812969009
Publisher: Villard
Date (Month/Year): July 2002
```

### Introduction (context only: never use it for content warnings)

```text
"The Sims" is a fun simulation game that gets some parts of life right. We all get cranky if we don't have enough fun, food, and rest. But when it comes to marriage, the game is very different. Especially if Lori Notaro is the Grand Puppetmaster running the show. . . . Who said video addition can destroy a marriage? Sometimes it happens the first time you play! The Sims by Lori Notaro.
```

### Performance text (classify this)

```text
HUSBAND: What is that? "What IS THAT? What is that thing right near the fireman's foot in the front yard? Oh my God. Oh my God. What ... what have you done?!!

WIFE: Honestly, it really wasn't my fault. . . . I don't know, maybe it really was my fault. After all, after my husband bought me the computer game called "The Sims," the clerk at the Apple store was very careful to give me a stern warning as he handed my new game over.

CLERK: Now, since you get to create your own characters in this computer game, many people are tempted to duplicate themselves and their spouses. DON'T DO IT. No matter how tempted you are, DON'T DO IT. You'll almost always end up getting divorced.

WIFE: For those of you unfamiliar with this game, briefly, this is the point: You create people, build houses for them, create a neighborhood, and watch how they coexist domestically and within the neighborhood. In short, it's like making your own soap opera, and you get to play the almighty deity and Grand Puppetmaster, I thought, this is a powerful game. I went immediately home and created a Laurie character and a Laurie's Husband character. I mean, it certainly was tempting to see what would happen between Laurie and Laurie's Husband when left to their own devices-it was like watching an ant farm, in a sense, only the ants had human heads that looked like you and your husband. I mean, honestly, what was the worst that could happen?

After I created Laurie and Laurie's Husband, I moved them into a house and started the game. As Laurie and Laurie's Husband walked around in their house, it was my job to take them to the bathroom when they needed to pee, make sure they ate when they were hungry, make them take a shower when they got dirty, go to sleep when they got tired, and clean up after themselves. In short, it was like having an electronic pet, and to tell you the truth, I was not truly finding the game a whole lot of fun at all. Where was the action, where was the pull, the attraction to this game?

One thing is for sure, however; Laurie and Laurie's Husband were pigs. And I mean pigs! When she was done eating, she would simply throw the food on the floor, and one time I actually caught him leaving a turkey leg in the front yard. Okay, it's true, I gave him a mullet and armpit stains, but the last thing I expected was an automatic lapse into "Livin' in the Holler." Finally, I made them get jobs-which, in the Sims' world, is as easy as picking up the newspaper-but making sure that both of them were up, washed, dressed, and fed before the car pool came was nearly impossible. After I would wake up Laurie's Husband, I'd be getting her ready and off to work, only to find out that he went back to sleep,just like in real life. Eventually, after missing his ride to the office for three days in a row because, he lost his job. I could have told you that was going to happen.

Laurie, it was obvious, wasn't too happy with him, either. She came home from work, found the house buzzing with flies, him watching TV, a pile of turkey legs by the front door, and she started stomping her foot and shaking her fist at him. He retreated into the bedroom, where he sat on the edge of the bed, put his head in his hands, and began to sob.

Oh, this is ridiculous, I thought, so I decided that he definitely needed to get another job, one he was actually going to go to this time. So I made him get the newspaper, and then, to my surprise, he looked at me, a bubble came out of his mouth, and there were words inside it that said, "I don't want to look for a job right now. I am too depressed." And then he gave me a sad face.

Well, that may have worked in real life, buddy boy, but this is MY game and I AM THE GRAND PUPPETMASTER. I will do in my pretend universe what I apparently cannot do in reality! I command you to get a job!

HUSBAND: Who are you commanding to get a job now? Who is that fatty? Without the gut, he looks like Shaggy from Scooby-Doo."

WIFE: No. It's not Shaggy. It's you."

HUSBAND: Oh, great, you made me a barrel-shaped, Schlitzguzzling mechanic so I wouldn't cheat on you, huh? What is up with my hair? I look like a member of REO Speedwagon.

WIFE: I'm just trying to control my simulated universe.

HUSBAND: And who's that? That looks like Julia Roberts.

WIFE: Why, thank you, kind sir. That's not Julia Roberts, it's me!

HUSBAND: Why is the REO Speedwagon Shaggy crying?

WIFE: He's depressed. He lost his job and now he's too depressed to get another one.

HUSBAND: Oh, he's not doing well. He needs to socialize, to clean up, and he's hungry. Maybe if you make him do those things, he'll be happy enough to get a job.

WIFE: It would be easier to slip him Prozac, but I'll try it.

HUSBAND: Maybe they can socialize and have fun while they make dinner together."

WIFE: My husband pulled up a chair next to mine and sat down. So I put Laurie and Mr. Sad Sack to work in the kitchen to interact and raise his spirits, and everything seemed to be going fine. I made her tickle him, which he liked, and then she told him some jokes. His "fun" level was rising, which was a very good sign. Laurie was making dinner, things were looking up, and at least he had stopped crying. I thought things were going well, until my husband pointed to the computer screen and said

HUSBAND: What's ... that?

WIFE: It took me at least a couple of seconds to realize it was a fire. Sad Sack had put the newspaper too close to the stove where Laurie was making dinner, and a small fire had erupted. And Laurie and Laurie's Husband were just standing there, watching it.

HUSBAND: Make them pick up the phone to call 911!

WIFE: I clicked on the phone, and clicked, and clicked, but neither one of them made a move. This was primarily because Sad Sack just shook his stupid head and gave me another sad face, and Laurie couldn't get to the phone, well, because she was now entirely engulfed in flames. I'm on FIRE! I'm on FIRE!! I searched the screen frantically for a garden hose or anything to put the fire out.

HUSBAND: Click on the flames and see if you get an option!

WIFE: Immediately, I clicked on the flames, and what popped up but the option to extinguish, and that's when Sad Sack finally coughed up a fire extinguisher and sprayed it all over the kitchen. The fire subsided. But it was too late. A computerized version of the Death March was heard, and when the fire extinguisher spray had cleared, Laurie was gone. Where she had stood just moments ago was now a small, gray urn. A message from the game popped up on the screen. "Laurie Notaro has died," the box said.

This is all his fault . . . . You! You just stood there as she sizzled like a Jimmy Dean sausage link!

HUSBAND: Click on the urn. Maybe there's a way to bring you back."

WIFE: So I clicked on the urn, but the only thing that happened was that an option to "mourn" popped up. So I took it. And then, a beautiful thing happened. Someone started to cry. Laurie's Husband wailed. I clicked on my urn again. Mourn. And again. Mourn. And again. Mourn. Cry, you big baby, cry! Look what you did to her! I'm going to keep you so depressed you'll never be able to get a job, have a normal life, or marry anyone else! He deserved it. You know he did.

That's when the fireman finally showed up, and Laurie's Husband moaned all the way out to the front yard to greet him as the fireman stood next to a bunch of decomposing turkey legs. "HOO HOO HOOOO!" I made him say to the fireman. "HOO HOO HOOOO!!"

HUSBAND: Come on, quit clicking on the urn. I've been through enough. Don't you want me to get on with my life? Hey, can we make a fake girl who looks like Kate Winslet?

WIFE: NO! I'm sorry, but did you or did you not just see me being incinerated like a Duraflame log? Huh? Did you? And then I clicked the urn numerous additional times to emphasize my point.

HUSBAND: What IS THAT? What is that thing right near the fireman's foot in the front yard? Oh my God. Oh my God. What ... what have you done?!!"

WIFE: And then I saw what my husband saw. A big, spreading puddle right at the tip of the fireman's boot.

HUSBAND: I hope you're happy! LOOK AT THAT. I've peed my pants!! I've wet myself in front of a fireman!"

WIFE: Yes, you certainly have.

HUSBAND: You were so busy making me cry and mourning you that you didn't bother to notice that my bladder needs were at alarming levels!

WIFE: Well, it's not my fault. Maybe if you realized you had to tinkle when I was a bonfire, I might still be alive!

HUSBAND: Actually, now that I'm thinking about it, I do need to use the rest room. And all of that mourning has made me hungry! What are we making for dinner?

WIFE: Not on your life!
```

---

## IC-1294: Sixteen

- Title: Sixteen
- Author (byline): Maureen Daly
- Work: Twenty Grand Short Stories
- Publisher: Bantam
- Publication date as stated: 1963
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1501
- Already set (do not supply): none

### Source block (context only)

```text
Author: Maureen Daly
Book: Twenty Grand Short Stories
ISBN: B000MOQK3U
Publisher: Bantam
Date(Month/Year): 1963
```

### Introduction (context only: never use it for content warnings)

```text
One could fall in love many times during the course of a lifetime, but the first rush of love always holds a special place in our hearts. The novelty of the feeling, like the first drops of dew on an untouched leaf, makes it special and unforgettable. Author Maureen Daly (only sixteen herself) wrote the short story Sixteen which subsequently won the O. Henry award for literature. Set in the 1950’s, the same period in which she was a teen, she speaks from the heart as she paints a vivid portrait of first love. Many assume that her work is autobiographical. Sixteen by Maureen Daly.
```

### Performance text (classify this)

```text
N

ow don't get me wrong. I mean, I want you to understand from the beginning

that I’m not really so dumb. I know what a girl should do and what she shouldn't. I get around. I read. I listen to the radio. And I have two older sisters. So you see I know what's what. I know it's smart to wear tweed skirts and tight fitting sweaters and ballerina shoes. And I know that your hair should be short with that look of careful carelessness, and the peasant hankie should be draped cleverly around your neck, fastened with a ring. Now, me, I never wear a hankie, it makes my face seem too wide. I'm not exactly too small-town either. I read the Broadway columns. You get to know what New York boy is crazy about what Hollywood actress on the West Coast and what starlet is currently the prettiest and who eventually, will play Joan of Arc. It gives you that worldly feeling. I know that it is absolutely forbidden to wear colored ankle-socks with high-heeled shoes or use Evening in Paris perfume with a tweed suit. But this isn't what I wanted to tell you. I just wanted to give you the general idea that I'm not so dumb. It is important that you understand that.

You see, it was funny how I met him. It was winter night like any other night. And I didn't have my chemistry done either. But the way the moon silvered the twigs and the snow-drifts, I just could not stay inside. The skating rink isn't far from our house - you can make it in five minutes if the side walks aren't slippery, so I went skating. I remember it took me a long time to get ready that night because I had to darn my skating socks first. I don't know why they are always wear out so fast - just in the toes, too. And then I brushed my hair hard, so hard it clung to my hand and stood up around my head.

My skates were hanging by the back door all nice and shiny, for I'd just gotten them for Christmas and they smelled so queer. My dog walked with me as far as the corner. She panted along beside me and her hot breath made a frosty little balloon on the end of her nose. The night was breathlessly quiet and the stars winked down like a million flirting eyes. It was all so lovely.

It was all so lovely; I ran most of the way and it was lucky the sidewalks had ashes on them or I would have slipped.

I had to cut across someone's back garden to get to the rink, and I was out of breath when I got to the shanty - out of breath with running and with the loveliness of the night. Shanties are always such friendly places. There was a delicious smell from the iron stove. Girls burst through the door laughing with snow on their hair. A boy grabbed the hat from a blonde and stuffed it into an empty shoe.

It didn't take me long to get my own skates on and I put my shoes under the bench - far back where they wouldn't get knocked around and would be easy to find when I wanted to go home. I walked out on my toes into the night air.

It was snowing a little outside - quick, eager little flakes that melted as soon as they touched your hand. I don't know where the snow came from for there were stars out. Or maybe the stars were in my eyes and I just kept seeing them every time I looked up into the darkness. I waited a moment. You know, to start to skate at a crowded rink is like jumping on a moving merry-go-round. Once in, I went all right. At least, after I found out exactly where the rough ice was. It was "round, round, jump the rut, round, round, jump the rut, round, round - ."

~ II ~

A

nd then he came. All of sudden his arm was around my waist so warm and tight

and he said, "Mind if I skate with you?" and then he took my other hand. That's all there was to it. Just that and then we were skating. It wasn't that I had never skated with a boy before. Don't be silly. I told you before I get around. But this was different. He was smooth! He was a big shot up at school and the best dancer in town. Don't you see? This was different.

At first I can't remember what we talked about, I can't even remember if we talked at all. We just skated and skated and laughed every time we came to that rough spot and pretty soon we were laughing all the time at nothing at all. It was all so lovely.

Then we sat on the big snow bank at the edge of the rink and just watched. It was cold at first, even with my skating pants on, sitting on that hard heap of snow, but pretty soon I got warm all over. He threw a handful of snow at me and it fell in a little white shower on my hair and he leaned over to brush it off. I held my breath. The night stood still.

Then he sat up straight and said, "We'd better start home." Not "shall I take you home?" or "Do you live far?" but "We'd better start home." See, that's how I knew he wanted to take me home. Not because he had to but because he wanted to. He went to the shanty to get my shoes. "Black ones", I told him. "Same size as Garbo's." And laughed again. He was still smiling when he came back and took off my skates and tied the wet skate strings in a knot and put them over his shoulder. Then he held out his hand and helped me up from the snow bank. I brushed off the seat of my pants and we were ready.

It was snowing harder now. Big, quiet flakes that clung to us lovingly. It was all so lovely that I was sorry I lived only a few blocks away. He talked softly as we walked as if every little word was a secret. "Did I like swing and did I plan to go to college next year and had I a cousin who knew his brother?" A very respectable sort of conversation and then finally - "How nice I looked with snow in my hair and had I ever seen the moon - so close?" and then we were home.

The porch light was on. My mother always puts the porch light on when I go away at night. And we stood there a moment by the front steps and the snow turned pinkish in the light and a few feathery flakes settled on my hair. Then he took my skates and put them over my shoulder and very, very close to my cheek softly said, "Good night now. I'll call you," he said.

I went inside then and in a moment he was gone. I watched him from my window as he went down the street. I could hear him whistling softly and I couldn't tell if it was he or my heart whistling out there in the night. And then he was gone, completely gone.

I shivered. Somehow the darkness seemed changed. The stars were hard little lights up in the sky and the moon had a sharp yellow glare. The air was suddenly cold and the wind wiped out his footsteps. Everything was quiet.

But he'd said, "I'll call you." That's what he said, "I'll call you." I couldn't sleep all night.

And that was last Thursday. Tonight is Tuesday. Tonight is Tuesday and my homework is done and I darned some stocking that really didn't need it, and I worked a cross-word puzzle and I listened to the radio and now I'm just sitting. I'm just sitting because I can't think of anything else to do. I can't think of anything, anything but snowflakes and ice skates and a yellow moon and Thursday night. The telephone is sitting on the corner table with its old black face turned to the wall. I don't even jump when it rings any more. My heart still prays but my mind just laughs. Outside the night is still - so still I think I'll go crazy. And so I'm sitting here and I'm not feeling anything. I'm not even sad because all of a sudden I know. I can sit here now and forever and laugh and laugh while the tears run salty in the corners of my mouth. For all of a sudden, I know, I know what the stars knew all the time - he will never, never call - never.
```

---

## IC-1295: Tables and Chairs

- Title: Tables and Chairs
- Author (byline): Stanley Rutherford
- Work: Scenes and Monologs from the Best New Plays
- Publisher: Meriwether Publishing
- Publication date as stated: Sep 1992
- Event as filed: Humorous Interpretation
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
Every marriage starts with a lot of hope and dreams about a life-long association filled with love and togetherness. . . . . . . HOWEVER . . . . committing to a long term relationship like marriage solely on the basis of that feeling of love is a mistake. Or maybe it’s not. Howard and Alice are like . . . . like Peanut Butter and Jelly, like Ham and Eggs – like . . . . Tables and Chairs by Stanley Rutherford.
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

## IC-1296: There Was Once / Unpopular Gals

- Title: There Was Once / Unpopular Gals
- Author (byline): Margaret Atwood
- Work: Good Bones and Simple Murders
- Publisher: Coach House Press
- Publication date as stated: 1992
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: A, B, C, THE UGLY STEP SISTER, THE EVIL STEP-MOTHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1518
- Already set (do not supply): none

### Source block (context only)

```text
Author: Margaret Atwood
Book: Good Bones and Simple Murders
ISBN: 0889104425
Publisher: Coach House Press
Date (Month/Year): 1992
```

### Introduction (context only: never use it for content warnings)

```text
There Was Once by Margaret Atwood
```

### Performance text (classify this)

```text
A: "There was once a poor girl, as beautiful as she was good, who lived with her wicked stepmother in a house in the forest."

B: "Forest? Forest is passé, I mean, I've had it with all this wilderness stuff. It's not a right image of our society, today. Let's have some urban for a change."

A: "There was once a poor girl, as beautiful as she was good, who lived with her wicked stepmother in a house in the suburbs."

B: "That's better. But I have to seriously query this word poor."

A: "But she was poor!"

B: "Poor is relative. She lived in a house, didn't she?"

A: "Yes."

B: "Then socio-economically speaking, she was not poor."

A: "But none of the money was hers! The whole point of the story is that the wicked stepmother makes her wear old clothes and sleep in the fireplace-"

B: "Aha! They had a fireplace! With poor, let me tell you, there's no fireplace. Come down to the park, come to the subway stations after dark, come down to where they sleep in cardboard boxes, and I'll show you poor!"

A: "There was once a middle-class girl, as beautiful as she was good-"

B: "Stop right there. I think we can cut the beautiful, don't you? Women these days have to deal with too many intimidating physical role models as it is, what with those bimbos in the ads. Can't you make her, well, more average?"

A: "There was once a girl who was a little overweight and whose front teeth stuck out, who-"

B: "I don't think it's nice to make fun of people's appearances. Plus, you're encouraging anorexia."

A: "I wasn't making fun! I was just describing-"

B: "Skip the description. Description oppresses. But you can say what colour she was."

A: "What colour?"

B: "You know. Black, white, red, brown, yellow. Those are the choices. And I'm telling you right now, I've had enough of white. Dominant culture this, dominant culture that-"

A: "I don't know what colour."

B: "Well, it would probably be your colour, wouldn't it?"

A: "But this isn't about me! It's about this girl-"

B: "Everything is about you."

A: "Sounds to me like you don't want to hear this story at all."

B: "Oh well, go on. You could make her ethnic. That might help."

A: "There was once a girl of indeterminate descent, as average-looking as she was good, who lived with her wicked-"

B: "Another thing. Good and wicked. Don't you think you should transcend those puritanical judgmental moralistic epithets? I mean, so much of that is conditioning, isn't it?"

A: "There was once a girl, as average-looking as she was well-adjusted, who lived with her stepmother, who was not a very open and loving person because she herself had been abused in childhood."

B: "Better. But I am so tired of negative female images! And stepmothers-they always get it in the neck! Change it to stepfather, why don't you? That would make more sense anyway, considering the bad behaviour you're about to describe. And throw in some whips and chains. We all know what those twisted, repressed, middle-aged men are like-"

C: "Hey, just a minute! I'm a middle-aged-"

B: "Stuff it, Mister Nosy Parker. Nobody asked you to stick in your oar, or whatever you want to call that thing. This is between the two of us. Go on."

A: "There was once a girl-"

B: "How old was she?"

A: "I don't know. She was young."

B: "This ends with a marriage, right?"

A: "Well, not to blow the plot, but-yes."

B: "Then you can scratch the condescending paternalistic terminology. It's woman, pal. Woman."

A: "There was once-"

B: "What's this was, once? Enough of the dead past. Tell me about now."

A: "There-"

B: "So?"

A: "So, what?"

B: "So, why not here?"

THE UGLY STEP SISTER: Everyone gets a turn, and now it's mine. Or so they used to tell us in kindergarten. It's not really true. Some get more turns than others, and I've never had a turn, not one! I hardly know how to say I, or mine; I've been she, her, that one, for so long.

I haven't even been given a name; I was just the ugly sister; put the stress on ugly. The one the other mothers looked at, then looked away from and shook their heads gently. Their voices lowered or ceased altogether when I came into the room, in my pretty dresses, my face leaden and scowling. They tried to think of something to say that would redeem the situation-Well, she's certainly strong-but they knew it was useless. So did I.

You think I didn't hate their pity, their forced kindness? And knowing that no matter what I did, how virtuous I was, or hardworking, I would never be beautiful. Not like her, the one who merely had to sit there to be adored. You wonder why I stabbed the blue eyes of my dolls with pins and pulled their hair out until they were bald? Life isn't fair. Why should I be?

As for the prince, you think I didn't love him? I loved him more than she did. I loved him more than anything. Enough to cut off my foot. Enough to murder. Of course I disguised myself in heavy veils, to take her place at the altar. Of course I threw her out the window and pulled the sheets up over my head and pretended to be her. Who wouldn't, in my position?

But all my love ever came to was a bad end. Red-hot shoes, barrels studded with nails. That's what it feels like, unrequited love.

She had a baby, too. I was never allowed.

Everything you've ever wanted, I wanted also.

THE WITCH IN THE GINGERBREAD HOUSE: A libel action, that's what I'm thinking. Put an end to this nonsense. Just because I'm old and live alone and can't see very well, they accuse me of all sorts of things. Cooking and eating children, well, can you imagine? What a fantasy, and even if I did eat just a few, whose fault was it? Those children were left in the forest by their parents, who fully intended them to die. Waste not, want not, has always been my motto.

Anyway, the way I see it, they were an offering. I used to be given grown-ups, men and women both, stuffed full of seasonal goodies and handed over to me at seed-time and harvest. The symbolism was a little crude perhaps, and the events themselves were-some might say-lacking in taste, but folks' hearts were in the right place. In return, I made things germinate and grow and swell and ripen.

Then I got hidden away, stuck into the attic, shrunken and parched and covered up in dusty draperies. Hell, I used to have breasts! Not just two of them. Lots. Ever wonder why a third tit was the crucial test, once, for women like me?

Or why I'm so often shown with a garden? A wonderful garden, in which mouth-watering things grow. Mulberries. Magic cabbages. Rapunzel, whatever that is. And all those pregnant women trying to clamber over the wall, by the light of the moon, to munch up my fecundity, without giving anything in return. Theft, you'd call it, if you were at all open-minded.

That was never the rule in the old days. Life was a gift then, not something to be stolen. It was my gift. By earth and sea I bestowed it, and the people gave me thanks.

THE EVIL STEP-MOTHER: It's true, there are never any evil stepfathers. Only a bunch of lily-livered widowers, who let me get away with murder vis-à-vis their daughters. Where are they when I'm making those girls drudge in the kitchen, or sending them out into the blizzard in their paper dresses? Working late at the office. Passing the buck. Men! But if you think they know nothing about it, you're crazy.

The thing about those good daughters is, they're so good. Obedient and passive. Sniveling, I might add. No get-up-and-go. What would become of them if it weren't for me? Nothing, that's what. All they'd ever do is the housework, which seems to feature largely in these stories. They'd marry some peasant, have seventeen kids, and get 'A dutiful wife' engraved on their tombstones, if any. Big deal.

I stir things up, I get things moving. 'Go play in the traffic,' I say to them. 'Put on this paper dress and look for strawberries in the snow.' It's perverse, but it works. All they have to do is smile and say hello and do a little more housework, for some gnomes or nice ladies or whatever, and bingo, they get the king's son and the palace, and no more dishpan hands. Whereas all I get is the blame.

God knows all about it. No Devil, no Fall, no Redemption. Grade Two arithmetic.

You can wipe your feet on me, twist my motives around all you like, you can dump millstones on my head and drown me in the river, but you can't get me out of the story. I'm the plot, babe, and don't ever forget it.
```

---

## IC-1297: The Throne of Fire

- Title: The Throne of Fire
- Author (byline): Rick Riordan
- Work: Cutting is from (Chapter 8)
- Publisher: Disney Hyperion
- Publication date as stated: Aug 2012
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: SADIE, BES, LIZ, NEKHBET
- Teaser before the introduction: Yes
- Spoken words (computed): 1418
- Already set (do not supply): none

### Source block (context only)

```text
Author: Rick Riordan
Book: Cutting is from (Chapter 8)
ISBN: 978-1423142010
Publisher: Disney Hyperion
Date (Month/Year): Aug 2012
* Cutting compliments of Heidi Trevithic of Denver, Colorado
```

### Introduction (context only: never use it for content warnings)

```text
Of course Sadie had seen stranger things . . . that tends to happen when you are one of the most powerful descendants of the ancient Egyptian pharaohs to be born in centuries!

Sadie is on a mission to revive the sun god Ra who can stop the god of Chaos and his minions from rising and destroying the world. (Where was she when we needed her in the years leading up to the 2016 Presidential Election?)

In this selection, Sadie finds an ally in Bes, the dwarf god (Think Tirian Lannister from Game of Thrones), who helps her defeat two of Chaos’ minions: Nekhbet, the Vulture Goddess, and Babi, a blood-thirsty god of the underworld.

Will Sadie and Bes prevail or will Chaos reign? Throne of Fire by Rick Riordan.
```

### Performance text (classify this)

```text
*NOTE: Sadie and Liz should have pronounced British accents Nekhbet appears as a woman that is a hundred years old. The skin around her face, neck, and earlobes sag and her body is hunched over and emaciated. She is almost bald, with just a few clumps of greasy black hair on her head. She wears a "lush" black dress made entirely of feathers.

SADIE: (To Audience) I’d never been in a limousine before. I hope most are nicer than the one we took. The backseat was littered with take-away curry containers, old fish-and-chip paper, crisps bags, and various dirty socks. Despite this, Liz and I crammed together in the back, because neither of us dared ride up front.

You may think I was mad to get in a car with a strange man. You’re right, of course. But the gods had promised us help and a driver. The fact that our promised help was a little man with bad hygiene and a magical limousine did not particularly surprise me. I’d seen stranger things.

.

SADIE: (To Audience) He was shorter than me by half, and uglier than anyone else on the planet. His facial features were positively Neanderthal. Under his thick furry mono-brow, one eye was bigger than the other. His beard looked as if it had been used to scrape greasy pots. His skin was poxy with red welts, and his hair looked like a bird’s nest that had been set on fire then stomped out. When he saw me, he scowled, which did nothing to help his appearance.

BES: About time! (American accent, belching into his fist). Sadie Kane?

SADIE: Um . . . possibly. By the way, we have two gods trying to kill us.

BES: (Turning toward the curb and yelling,) BOO!

SADIE: (To Audience) A black Mercedes limousine appeared out of nowhere, as if it had been scared into existence.

BES: (Glancing at Sadie and arching his brow.) Well? Get in!

SADIE: (To Audience) The chauffeur started whistling a tune that sounded like “Short People.” His head barely reached the headrest. All I could see of him was a grubby nest of hair and a set of furry hands on the wheel.

Stuck in the sun visor was an identification card with his picture – sort of. It had been taken at point-blank range, showing only an out-of-focus nose and a hideous mouth, as if he’d been trying to eat the camera. The card read: Your Driver is BES. (To Bes) You’re Bes, I guess?

BES: Yes.

SADIE: Your car’s a mess.

LIZ: If one more person rhymes, I’ll throw up.

SADIE: (To Bes) Is it Mr. Bes? (To Audience) I tried to place his name from Egyptian mythology. I was fairly sure they hadn’t had a god of chauffeurs. (To Bes) Lord Bes? Bes the Extremely Short?

BES: Just Bes. One “S”. And no, it’s NOT a girl’s name. Call me Bessie, and I’ll have to kill you. As for being short, I’m the dwarf god, so what do you expect? Oh, there’s bottled water for you back there if you’re thirsty.

SADIE: (To Audience) Rolling about at my feet were two partially empty bottles of water. One had lipstick on the cap. The other looked as if it had been chewed on. (To Bes) Not thirsty.

LIZ: You’re really a god?

BES: Huge! I’m huge in the world of gods.

LIZ: A huge god of dwarves. You mean as in Snow White, or –

BES: All dwarves. Egyptians were smart. They honored people who were born unusual. Dwarves were considered extremely magical. So yeah, I’m the god of dwarves.

LIZ: (clearing her throat.) Isn’t there a more polite term we’re supposed to use nowadays? Like . . . little person, or vertically challenged, or –

BES: I’m not going to call myself the god of vertically challenged people. I’m a dwarf! Now, here we are just in time.

SADIE: (To Audience) He spun the car to a stop in the middle of the bridge. Looking behind us, I almost lost the contents of my stomach. A winged black shape was circling over the riverbank. At the end of the bridge, Babi was taking care of the barricade in his own fashion. He was throwing police cars into the River Thames while the officers scattered and fired their weapons, though the bullets seemed to have no effect on the baboon god’s steely fur. (to Liz) Liz, we’re getting out.

LIZ: (whimpering) Getting. . . out?

BES: (stifling a yawn.) Need my help?

SADIE: Um . . . (To audience) Babi was lumbering towards us. Nekhbet circled over him, shrieking orders. I didn’t see how a dwarf god could stand against those two, but, (To Bes) Yes, I need help.

BES: Right. (cracking his knuckles.) So get out.

SADIE: What?

BES: I can’t change clothes with you in the car, can I? I have to put on my ugly outfit.

SADIE: Ugly outfit?

BES: Go! I’ll be out in a minute.

SADIE: (To Audience) It didn’t take much encouragement. Neither of us wanted to see any more of Bes than we had to. We got out, and Bes locked the doors behind us. The windows were heavily tinted, so I couldn’t see in. For all I knew Bes would be relaxing, listening to music while we got slaughtered. I certainly didn’t have much hope that a wardrobe change was going to defeat Nekhbet and Babi. (To Liz and Bes) We’ll make our last stand here.

LIZ: Oh, no, no. I really don’t like the term “last stand.”

SADIE: (To Audience) Nekhbet must’ve seen the desperation in my face. She was a vulture. She specialized in knowing when her prey was finished.

NEKHBET: A good last effort child, but you have nothing left. Babi, attack!

SADIE: (To Audience) The baboon god reared up on his back legs. I got ready to charge and deliver one final burst of energy – to tap into my own life source and hopefully vaporize the gods. Then the limo’s door opened behind me.

BES: No one is attacking anyone! Except me, of course.

SADIE: (To Audience) Nekhbet shrieked in alarm. I turned to see what was going on. Immediately, I wished I could burn my eyes out of my head.

LIZ: (making a gagging sound.) Lord, no! That’s wrong! Make him stop!

SADIE: (To Audience) Bes had indeed put on his ugly outfit. He climbed onto the roof of the limo and stood there, legs planted, arms akimbo, like Superman – except with only the underwear.

For those faint of heart, I won’t go into great detail, but Bes, all of a meter tall, was showing off his disgusting physique – his potbelly, hairy limbs, awful feet, gross flabby bits – and wearing only a blue Speedo. Imagine the worst looking person you’ve ever seen on a public beach – the person for whom swimwear should be illegal. Bes looked worse than that. (To Bes) Put on some clothes!

BES: (laughing loudly in a sort of guffaw that says “Ha-ha! I’m amazing!”) Not until they leave. Or I’ll be forced to scare them away.

NEKHBET: This is not your affair, dwarf god! (snarling and averting her eyes from his hideousness.) Go away!

BES: These children are under my protection.

SADIE: I don’t know you! I never met you before today.

BES: Nonsense. You expressly asked for my protection.

SADIE: I didn’t ask for the Speedo Patrol! (To Audience) Bes leaped off the limo and landed in front of me, placing himself between Babi and me. The dwarf was even more horrible from behind. His back was so hairy it looked like a mink coat. And on the back of his Speedo was printed DWARF PRIDE.

Bes and Babi circled each other like wrestlers. The baboon god swiped at Bes, but the dwarf was agile. He scrambled up Babi’s chest and head-butted him in the nose. Babi staggered backward as the dwarf continued pounding away, using his face as a deadly weapon.

Babi slumped against the railing. He blinked, trying to regain his bearings, but Bes breathed on him, and the smell of curry must’ve been too much. The baboon’s knees buckled. His body shimmered and began to shrink. Then Bes turned toward the vulture goddess.

BES: Now it’s your turn, Nekhbet. Leave.

NEKHBET: I stole this body fair and square! (wailing) I like it in here!

BES: You asked for it.

SADIE: (To Audience) Bes rubbed his hands, took a deep breath, and did something I will never be able to erase from my memory. If I simply said he made a face and yelled BOO, that would be technically correct, but it wouldn’t begin to convey the horror. His head swelled. His jaw unhinged until his mouth was four times too big. His eyes bulged like grapefruits. His hair stuck straight up. He shook his face and waggled his slimy green tongue and roared BOOOO! so loudly, the sound rolled across the Thames like a cannon shot. This blast of pure ugly blew the feathers off Nekhbet’s cloak and drained all the color from her face. It ripped away the essence of the goddess like tissue paper in a storm. The dwarf’s face went back to normal – well, normal ugly, at least – (To Bes) Thank you. Now, will you please put on some clothes? (To Audience) He gave me a toothy grin, which I could have lived without.

BES: You’re all right, Sadie Kane.
```

---

## IC-1298: The Waltz

- Title: The Waltz
- Author (byline): Dorothy Parker
- Work: The Portable Dorothy Parker, Pgs 47-51
- Publisher: NTC Penguin Classics
- Publication date as stated: Mar 2006
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: WOMAN
- Teaser before the introduction: Yes
- Spoken words (computed): 2007
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dorothy Parker
Book: The Portable Dorothy Parker, Pgs 47-51
ISBN: 978-0143039532
Publisher: NTC Penguin Classics
Date (Month/Year): Mar 2006
```

### Introduction (context only: never use it for content warnings)

```text
The Waltz by Dorothy Parker
```

### Performance text (classify this)

```text
WOMAN: (Pg 47-51) Why, thank you so much. I'd adore to.

I don't want to dance with him. I don't want to dance with anybody. And even if I did, it wouldn't be him. He'd be well down among the last ten. I've seen the way he dances; it looks like something you do on Saint Walpurgis Night. Just think, not a quarter of an hour ago, here I was sitting, feeling so sorry for the poor girl he was dancing with. And now I'm going to be the poor girl. Well, well. Isn't it a small world?

WOMAN: And a peach of a world, too. A true little corker. Its events are so fascinatingly unpredictable, are not they? Here I was, minding my own business, not doing a stitch of harm to any living soul. And then he comes into my life, all smiles and city manners, to sue me for the favor of one memorable mazurka. Why, he scarcely knows my name, let alone what it stands for. It stands for Despair, Bewilderment, Futility, Degradation, and Premeditated Murder, but little does he wot. I don't wot his name, either; I haven't any idea what it is. Jukes, would be my guess from the look in his eyes. How do you do, Mr. Jukes? And how is that dear little brother of yours, with the two heads?

Ah, now why did he have to come around me, with his low requests? Why can't he let me lead my own life? I ask so little -- just to be left alone in my quiet corner of the table, to do my evening brooding over all my sorrows. And he must come, with his bows and his scrapes and his may-l-have-this-ones. And I had to go and tell him that I'd adore to dance with him. I cannot understand why I wasn't struck right down dead. Yes, and being struck dead would look like a day in the country, compared to struggling out a dance with this boy. But what could I do? Everyone else at the table had got up to dance, except him and me. There was I, trapped. Trapped like a trap in a trap.

What can you say, when a man asks you to dance with him? I most certainly will not dance with you, I'll see you in hell first. Why, thank you, I'd like to awfully, but I'm having labor pains. Oh, yes, do let's dance together -- it's so nice to meet a man who isn't a scaredy-cat about catching my beri-beri. No. There was nothing for me to do, but say I'd adore to. Well, we might as well get it over with. All right, Cannonball, let's run out on the field. You won the toss; you can lead.

Why, I think it's more of a waltz, really. Isn't it? We might just listen to the music a second. Shall we? Oh, yes, it's a waltz. Mind? Why, I'm simply thrilled. I'd love to waltz with you.

I'd love to waltz with you. I'd love to waltz with you. I'd love to have my tonsils out, I'd love to be in a midnight fire at sea. Well, it's too late now. We're getting under way. Oh. Oh, dear. Oh, dear, dear, dear. Oh, this is even worse than I thought it would be. I suppose that's the one dependable law of life -- everything is always worse than you thought it was going to be. Oh, if I had any real grasp of what this dance would be like, I'd have held out for sitting it out. Well, it will probably amount to the same thing in the end. We'll be sitting it out on the floor in a minute, if he keeps this up.

I'm so glad I brought it to his attention that this is a waltz they're playing. Heaven knows what might have happened, if he had thought it was something fast; we'd have blown the sides right out of the building, Why does he always want to be somewhere that he isn't? Why an't we stay in one place just long enough to get acclimated? It's this constant rush, rush, rush, that's the curse of American life. That's the reason that we're all of us so -- Ow! For God's sake, don't kick, you idiot; this is only second down. Oh, my shin. My poor, poor shin, that I've had ever since I was a little girl!

Oh, no, no, no. Goodness, no. It didn't hurt the least little bit. And anyway it was my fault. Really it was. Truly. Well, you're just being sweet, to say that. It really was all my fault.

I wonder what I'd better do -- kill him this instant, with my naked hands, or wait and let him drop in his traces. Maybe it's best not to make a scene. I guess I'll just lie low, and watch the pace get him. He can't keep this up indefinitely -- he's only flesh and blood. Die he must, and die he shall, for what he did to me. I don't want to be of the over-sensitive type, but you can't tell me that kick was unpremeditated. Freud says there are no accidents. I've led no cloistered life, I've known dancing partners who have spoiled my slippers and torn my dress; but when it comes to kicking, I am Outraged Womanhood. When you kick me in the shin, smile.

Maybe he didn't do it maliciously. Maybe it's just his way of showing his high spirits. I suppose I ought to be glad that one of us is having such a good time. I suppose I ought to think myself lucky if he brings me back alive. Maybe it's captious to demand of a practically strange man that he leave your shins as he found them. After all, the poor boy's doing the best he can. Probably he grew up in the hill country, and never had no larnin'. I bet they had to throw him on his back to get shoes on him.

Yes, it's lovely, isn't it? It's simply lovely. It's the loveliest waltz. Isn't it? Oh, I think it's lovely, too.

Why, I'm getting positively drawn to the Triple Threat here. He's my hero. He has the heart of a lion, and the sinews of a buffalo. Look at him -- never a thought of the consequences, never afraid of his face, hurling himself into every scrimmage, eyes shining, cheeks ablaze. And shall it be said that I hung back? No, a thousand times no. What's it to me if I have to spend the next couple of years in a plaster cast? Come on, Butch, right through them! Who wants to live forever?

Oh. Oh, dear. Oh, he's all right, thank goodness. For a while I thought they'd have to carry him off the field. Ah, I couldn't bear to have anything happen to him. I love him. I love him better than anybody in the world. Look at the spirit he gets into a dreary, commonplace waltz; how effete the other dancers seem, beside him. He is youth and vigor and courage, he is strength and gaiety and -- Ow! Get off my instep, you hulking peasant! What do you think I am, anyway -- a gangplank? Ow!

No, of course it didn't hurt. Why, it didn't a bit. Honestly. And it was all my fault. You see, that little step of yours -- well, it's perfectly lovely, but it's just a tiny bit tricky to follow at first. Oh, did you work it up yourself? You really did? Well, aren't you amazing! Oh, now I think I've got it. Oh, I think it's lovely. I was watching you do it when you were dancing before. It's awfully effective when you look at it.

It's awfully effective when you look at it. I bet I'm awfully effective when you look at me. My hair is hanging along my cheeks, my skirt is swaddling about me, I can feel the cold damp of my brow. I must look like something out of the "Fall of the House of Usher." This sort of thing takes a fearful toll of a woman my age. And he worked up his little step himself, he with his degenerate cunning. And it was just a tiny bit tricky at first, but now I think I've got it. Two stumbles, slip, and a twenty-yard dash; yes. I've got it. I've got several other things, too, including a split shin and a bitter heart. I hate this creature I'm chained to. I hated him the moment I saw his leering, bestial face. And here I've been locked in his noxious embrace for the thirty-five years this waltz has lasted. Is that orchestra never going to stop playing? Or must this obscene travesty of a dance go on until hell burns out?

Oh, they're going to play another encore. Oh, goody. Oh, that's lovely. Tired? I should say I'm not tired. I'd like to go on like this forever.

I should say I'm not tired. I'm dead, that's all I am. Dead, and in what a cause! And the music is never going to stop playing, and we're going on like this, Double-Time Charlie and I, throughout eternity. I suppose I won't care anymore, after the first hundred thousand years. I suppose nothing will matter then, not heat nor pain nor broken heart nor cruel, aching weariness. Well. It can't come too soon for me.

I wonder why I didn't tell him I was tired. I wonder why I didn't suggest going back to the table. I could have said let's just listen to the music. Yes, and if he would, that would be the first bit of attention he has given it all evening. George Jean Nathan said that the lovely rhythms of the waltz should be listened to in stillness and not be accompanied by strange gyrations of the human body. I think that's what he said. I think it was George Jean Nathan. Anyhow, whatever he said and whoever he was and whatever he's doing now, he's better off than I am. That's safe. Anybody who isn't waltzing with this Mrs. O'Leary's cow I've got here is having a good time.

Still if we were back at the table, I'd probably have to talk to him. Look at him -- what could you say to a thing like that! Did you go to the circus this year, what's your favorite kind of ice cream, how do you spell cat? I guess I'm as well off here. As well off as if I were in a cement mixer in full action.

I'm past all feeling now. The only way I can tell when he steps on me is that I can hear the splintering of bones. And all the events of my life are passing before my eyes. There was the time I was in a hurricane in the West Indies, there was the day I got my head cut open in the taxi smash, there was the night the drunken lady threw a bronze ashtray at her own true love and got me instead, there was that summer that the sailboat kept capsizing. Ah, what an easy, peaceful time was mine, until I fell in with Swifty, here. I didn't know what trouble was, before I got drawn into this danse macabre. I think my mind is beginning to wander. It almost seems to me as if the orchestra were stopping. It couldn't be, of course; it could never, never be. And yet in my ears there is a silence like the sound of angel voices. . . .

Oh they've stopped, the mean things. They're not going to play anymore. Oh, darn. Oh, do you think they would? Do you really think so, if you gave them twenty dollars? Oh, that would be lovely. And look, do tell them to play this same thing. I'd simply adore to go on waltzing.
```

---

## IC-1299: Wanda’s Visit

- Title: Wanda’s Visit
- Author (byline): Christopher Durang
- Work: Durang/Durang: Four Short Plays by Christopher Durang
- Publisher: Smith and Kraus
- Publication date as stated: June 1996
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: JIM, MARSHA, WANDA
- Teaser before the introduction: Yes
- Spoken words (computed): 1883
- Already set (do not supply): none

### Source block (context only)

```text
Author: Christopher Durang
Book: Durang/Durang: Four Short Plays by Christopher Durang
ISBN: 978-0822214601
Publisher: Smith and Kraus
Date (Month/Year): June 1996
```

### Introduction (context only: never use it for content warnings)

```text
Wanda’s Visit by Christopher Durang

(Offstage we hear great whooping and enthusiastic cries of "Jim! Jim!" WANDA is also late thirties, early forties, but unlike JIM and MARSHA, she is not in as good shape. Her clothes are a little gaudy, her hair looks odd or messy, and she carries a sense of emotional disarray with her. But she also looks kind of fun and colorful.)

WANDA: (With longing.) Jim!!! (WANDA throws her arms around JIM with great abandon,

and then holds this embrace as if her life depended on it. MARSHA goes closer to

them and waits patiently for the appropriate moment to be introduced.) (Still
```

### Performance text (classify this)

```text
This is the home of JIM and MARSHA. They enter and come to speak to the audience. They are attractive, in their mid- to late thirties. Their manner in talking to the audience is that of telling a story, but also, perhaps, of explaining themselves to a marriage counselor.

JIM: Our lives had been seeming dull for a while. You know, nothing major, just sometimes being quiet at dinner. And then the next week I got this letter from this old classmate of mine.

MARSHA: Wanda. He'd never mentioned her.

JIM: Well, she was just some girlfriend. You know. High school.

MARSHA: Wanda.

JIM: And Wanda wrote me, saying she'd like to visit. And I asked Marsha if she'd mind.

MARSHA: I have trouble saying no, most women do, I think. It's not pleasing or something.

JIM: And I asked you if you'd mind, and you said, it would be fine. I thought it would be fun. You know, to mull over the old high school days . . . So I wrote Wanda back, and told her we'd love to have her visit. In high school Wanda had been quite a looker.

MARSHA: To meet an old high school fantasy. Lucky me.

JIM: And so we waited for her visit.

embracing him.) Jim. Jim. Oh, Jim, Jim.

MARSHA: (Since the embrace doesn't seem to be ending.) Hello. I'm Marsha, Jim's wife.

WANDA: (Breaking from the embrace.) Oh, hello. Nice to see you. I was just so excited at seeing this guy. Hey, guy. Hey. How ya doin'?

JIM: I'm fine. (A little uncertain he recognizes her.) Wanda? -- didn't you used to be blond?

WANDA: Yeah, and I didn't used to be fat either-although I'm not really fat, my woman's group doesn't let me say that, I just have a food problem and some of it shows. But really I just lost twenty pounds. You should have seen me last month. Oh, give me another hug, guy. (WANDA gives JIM another bear hug.) Hrrrrrrrrrrrrrr. (To MARSHA; with sudden focus.) Do you have anything to eat? Pretzels or something?

MARSHA: Would you like some pate?

WANDA: Pate? (To JIM.) Where'd you get her, honey, the back of The New Yorker? (To MARSHA.) Sure, honey, I can eat pate as long as you have crackers with it. And maybe some pretzels.

MARSHA: Fine. I'll be right back. (Exits to kitchen area.)

WANDA: Oh, Jimbo, she's a jewel. An absolute jewel.

JIM: You know, I hate to say this, but I don't recognize your face actually.

WANDA: That's very perceptive, Jim. I've had plastic surgery. But it wasn't the fancy-schmancy kind to make your face look better, it was so they couldn't find me. (WANDA squeezes his *arm*. MARSHA comes in with the pate, and notices the *arm*-squeezing.)

MARSHA: Here is the pate. Would you like a drink? (WANDA pauses for a moment, and then begins to sob, very genuinely.) (At a loss what to say.) Don't feel you have to have a drink.

JIM: Wanda, what's the matter?

WANDA: (Through sobs.) Oh, I don't want to burden you. Or your wife.

MARSHA: That's all right, I'm sure we'd love to be burdened. I mean, if it would help you.

WANDA: (WANDA pulls herself together, and tries to explain why she felt so upset.) Well it all started the summer after high school graduation. (To MARSHA.) Jim and I had gone to the prom together, and though of course nothing had been said, everyone just kind of presumed he and I would get married. My mother, my father, me, everyone. We were inseparable. From about February of senior year to June senior year, we spent every spare moment together. You gave me your class ring. Look, I have it right here.

(Looks through her purse.) Uh-huh. Now, where is it? (WANDA dumps out the messy contents of her purse; looks through the mess.) No. No. Here's the prescription for Seconal I always carry with me in case I feel suicidal.

MARSHA: I don't think any of the pharmacies are open this late. (WANDA stares at MARSHA for a moment, like a child who's crying and has suddenly been distracted.)

JIM: Forget about the ring, Wanda. Tell us why you cried a few minutes ago.

WANDA: Isn't it obvious? Seeing the path not taken. I could have had a happy life if I married you. So anyway, you and I went to different colleges, and then when you didn't write me, I was heartbroken.

JIM: Wanda, if you felt this way, why didn't you tell me at the time? You haven't said anything in twenty years.

WANDA: Well, I've been very busy, (Chomps on a cracker.) So then I went to Ann Arbor, and oh, Jim and Marsha, I'm so ashamed to tell you this-I was promiscuous.

MARSHA: Really?

WANDA: It was awful. I became a campus joke. SO anyway, the campus minister once had to give a whole sermon against me, which made me feel just awful. (To JIM.) And all because I was pining for you. (weeps copiously.) (JIM and MARSHA stare at her for a little while.) And then my second husband gave me herpes, and every time the first one would call to threaten my life, it would trigger an outbreak . . .

MARSHA: Doesn't anyone want dinner yet?

WANDA: (Suddenly switching moods.) Marsha sounds hungry. Sure, honey, let's go eat.

(WANDA bounds up and moves to the dining room table.) Oh, the dinner looks beautiful. Now where was I? Uh-huh. So then there was that guy from prison. And then there was his father, Fred. Did I tell you about Fred? Well, Fred said to me, I married you because I thought you would be my anchor in the port of life, but now I think you're stark raving mad . . .

MARSHA: Could I have the salt, please? (JIM passes MARSHA the salt.)

WANDA: (Continues on with story.) So one day the washing machine blew up, and Fred said to me, you did that, everything about you is chaos, I'm leaving and I'm taking Tranquility with me.

JIM: He actually said "tranquility"?

MARSHA: (Muttered.) Don't ask her questions.

WANDA: (Explaining.) Tranquility was our dog. And I said, I'm the one who fed Tranquility, and walked her and took care of her worms, and she used to throw up on the rug, and, of course, you can't just leave it there ...

MARSHA: Excuse me, I'll be right back.

WANDA: I hope my talking about vomit didn't make you feel sick.

MARSHA: (Nearly out if the room.) No, it's fine. (MARSHA holds her head in pain. She just couldn't stand to be at the table for a minute longer)

JIM: I think she had a hard day.

WANDA: What did she do? Spend it making up the guest room for me? Really, I can sleep anywhere. I think I'm being evicted tomorrow anyway, so I'd prefer not to be there.

JIM: That's too bad. . . . Uh-huh. Hold on to the thought. I'll be right back.

(JIM exits and finds MARSHA still clutching her head.) Why are you hiding in the bathroom?

MARSHA: I needed aspirin. When is she leaving?

JIM: I think she's staying overnight.

MARSHA: Did she say that or did you say that? (WANDA, bored alone, bounds into the bathroom area with them.)

WANDA: What are you two talking about? When you live with someone, you don't have any secrets. I remember David said to me, why didn't you tell me you had herpes, and I said, I forgot, okay? People forget things, all right? And he said, not all right, I'm going to have this for life, and I said so what, you have your nose for life, is that my fault?

MARSHA: (Tired, but sort annoyed of by the logic.) Yes, but his nose wasn't your fault. .

WANDA: What? SO then I thought I'd stay out of relationships for a while, and I went to work for this lawyer, only he wasn't a regular lawyer, he was a kingpin of crime, only I didn't realize it. Eventually, of course, I had to get my face redone so they couldn't find me.

MARSHA: (Trying to tell her no.) Jim says you were expecting to stay overnight ...

WANDA: Thank you, I'd love to! I feel I'm just starting to scratch the surface with old Jimbo here. (A little girl.) I hope there's a quilt. I love quilts.

MARSHA: I'll look for one. (WANDA stares at her, happy, but doesn't get out of the way.) You have to move or I can't get out of the bathroom.

WANDA: (Serious.) I'm holding you hostage.

MARSHA: What?

WANDA: (Shifting, cheerful.) Isn't it awful the way they take hostages now?

(Cheerfully leaves the bathroom, talking away.) Reminds me of my life with Augie. He was really violent, but he was really little, so I was able to push him down the stairs. (JIM and MARSHA look at one another, a little alarmed by the "hostage" exchange. *****************

WANDA: (Happy.) Oh, you guys, it's been a great evening. I can't believe we played games for four hours! I'm sorry I broke the lamp. Well, good night, you two. See you in the morning.

MARSHA: Good night. (WANDA exits to the guest room. JIM and MARSHA go to their bedroom. They're too tired to talk. They kiss each other briefly and close their eyes to sleep. WANDA enters, wrapped up in a quilt.)

WANDA: Oh, is this your bedroom? Oh, it's so pretty. (JIM and MARSHA open their eyes, very startled.)

MARSHA: Is something wrong with your room?

WANDA: No, it's lovely. Although not as nice as here. It makes me never want to leave. (WANDA pulls up a chair right next to their bed. Keeps wrapped in her quilt.)

MARSHA: Wanda, I'm sorry. I really think I need to sleep.

WANDA: You can sleep, I won't be offended. (Clock ticks. Time passes. JIM and MARSHA change positions in bed.) (Coquettish.) And I said, "Billy, why didn't you tell me you were sixteen?" (Clock ticks.) (Chatty voice, just telling the facts.) Teary voice, telling a tragic turning point.) And Leonard said, Wanda, you are a worthless piece of trash. And I said, don't you think I know that? Do you think this is news? {Clock ticks.) (Energized, telling a fascinating story.) And Howard said he wanted me to kill his mother, and I said, "Are you crazy? I've never even met your mother." And he said, "All right, I'll introduce you. (JIM and MARSHA have closed their eyes, either asleep or pretending to be. WANDA looks over at them, suspicious.) Are you asleep? Jim? Marsha? (WANDA looks to see if they're asleep. She shakes their shoulders a bit, to see if she can wake them.) Jim? Marsha? You're not pretending to be asleep, are you? (WANDA opens MARSHA’s eyelid with her finger.) I was just checking if you were asleep. Good night. (WANDA takes her comforter and curls up at the bottom if their bed. Then she pulls their blanket off them and onto her.) **************** JIM and MARSHA wake up, and abruptly leave the bedroom for the dining room area.)

MARSHA: Oh God, why did she sleep on our bed? She seemed like some insane nightmare Golden Retriever. Was she always this way?

JIM: Well, she was always vivacious.

MARSHA: I see. High school prom queen. Girl Most Likely to Get Herpes.

JIM: Lots of people get herpes.

MARSHA: Yes, but they don't talk about it for three hours. Are you attracted to her?

JIM: Now come on, Marsha, she's an emotional mess.

MARSHA: You're putting up with it very patiently. Why is that?

JIM: Well, that's because . . . I feel sympathy for her. She's someone I knew once who had a life, and look what's happened to her.

MARSHA: Well, fine. I understand. I think I'll make a trip to the nearest loony bin and find some mental patient who finds me attractive. Then I'll bring him home and make you suffer through a forty-eight-hour visit while he drools on the carpet.

WANDA: (Entering from the bedroom . . . Loudly.) Hey! I have an idea! Why don't I cook dinner for you guys tonight? Do you like octopus?

MARSHA: Thank you, Wanda, no. I thought we'd go to a restaurant tonight. The walls in this house are starting to vibrate. ******************

(Lights change. JIM, MARSHA, and WANDA sit at a table in a restaurant)

WANDA: This is such a pretty restaurant. Ohhh, I think I know someone. (Waves, calls out to imaginary table.) Hi, there! Oh, no, I don't know them. (Calls out again.) Never mind! I thought you were my gynecologist. You know, Jim, tomorrow we should get out the old yearbook. You know, Marsha, you wouldn't believe how dashing he was back then.

JIM: You're sure a shot for my ego.

MARSHA: I'd like to shoot your ego . . . (Closes her eyes, puts her arms loose by her side, tries to relax her body.) (With eyes closed; chant-like.) I am sitting by a tree, and there's a lovely breeze.

WANDA: This restaurant is so adorable. This whole town. You know what I'm thinking? I'm thinking of maybe moving up here to the country with you all, finding a little house to rent. Nothing's happening in my life right now; this might be just the change I might need.

MARSHA: So you're going to move up here, are you? Going to sweep up and stick your feet in the ground and root yourself in our "little neck of the woods," are you? . . . I don't want you moving here, is that clear? I don't want you invading my life with your endless ravings anymore, is that clear? (WANDA keeps eating, seemingly just listening to what's being said, finding it interesting rather than upsetting.) (To JIM.) Don't you realize she's insane? (Almost on cue, WANDA starts choking JIM, MARSHA, look at her, shocked for a moment.)

JIM: Shouldn't one of us do the Heimlich maneuver?

MARSHA: I don't want to do it, I don't like her. (WANDA looks startled, even in the midst of her choking. She keeps choking and pointing to her throat.) (After a second.) Oh, for God's sake. (MARSHA gets up, She stands behind WANDA, puts her arms around WANDA’s lower stomach and then rather violently and suddenly pulls her hands into WANDA’s lower stomach. WANDA sits back down, exhausted) ******************

JIM: (To audience.) Well, all that happened a few weeks ago. But some good came out of it.

MARSHA: Yes. We had a big argument, and that was good. I said what I was feeling, and it was mostly negative, but it was good to say it.

JIM: And we're going to a marriage counselor who specializes in breaking down fear of intimacy in people who've known one another for over ten years . .

MARSHA: All told, I guess Wanda's visit helped to stir us up in a good way. Now if only we were happy.
```

---

## IC-1300: Warning Signs

- Title: Warning Signs
- Author (byline): Allie Brosh
- Work: Hyperbole and a Half (Pg 1-18)
- Publisher: Touchstone Books
- Publication date as stated: Oct 2013
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: ALLIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1987
- Already set (do not supply): none

### Source block (context only)

```text
Author: Allie Brosh
Book: Hyperbole and a Half (Pg 1-18)
ISBN: 978-1451666175
Publisher: Touchstone Books
Date (Month/Year): Oct 2013
```

### Introduction (context only: never use it for content warnings)

```text
Looking back . . . it should have been one of those very clear WARNING SIGNS. Parents, get your child to a therapist NOW! Warning Signs from Hyperbole and a Half by Allie Brosh
```

### Performance text (classify this)

```text
ALLIE: (Pg 1-18) When I was ten years old, I wrote a letter to my future self and buried it in my backyard. Seventeen years later, I remembered that I was supposed to remember to dig it up two years earlier. I looked forward to getting a nostalgic glimpse into my childhood— perhaps I would marvel at my own innocence or see the first glimmer of my current aspirations. As it turns out, it just made me feel real weird about myself.

ALLIE: The letter was scrawled in green crayon on the back of a utility bill. My ten-year-old self had obviously not spent much time planning out the presentation of it. Most likely, I had simply been walking through the kitchen and suddenly realized that it was entirely possible to write a letter to my future self.

The overwhelming excitement of this realization probably caused me to panic and short-circuit, making me unable to locate proper writing implements. There was no time for that kind of thing.

I did, however, manage to fight through the haze of chaos and impulse long enough to find a crayon stub and a paper surface to mash it against.

The letter begins thusly: Dear 25 year old [note: not “Dear 25-year-old me” or “Dear 25- year-old self,” just “Dear 25 year old”]

Do you still like dogs? What is your favarite dog? Do you have a job tranning dogs? Is Murphy still alive? What is youre favarite food?? Are mom and dad still alive?

I feel it’s important to note the order of those questions. Obviously, dog-related subjects were my chief concern (Murphy was my family’s dog), followed closely by the need to know my future favorite food (I feel that the double question marks speak to how important I thought that question was). Only then did I pause to wonder whether my parents had survived.

The letter continues with a section titled “About me”: My name is Allie and I am ten years old. I have blound hair and blue eyes. My favarite dog is a german shepard. My second favarite dog is a husky. My third favarite dog is a Dobberman Pincher.

This is troubling for a number of reasons, the first of which is that I apparently thought my future self wouldn’t be aware of my name or eye color. “Who. What if – in the future – I’m not even me any more. I won’t know what I am.”

The second thing is the fact that I just tacked on my favorite dog breeds at the end there, like it was every bit as important to my identity as the other things. As if my past self had imagined my future self standing in the yard above the upturned earth, clutching my letter and screaming, “BUT WHAT DOGS DID I LIKE??? HOW AM I SUPPOSED TO UNDERSTAND MY IDENTITY WITHOUT KNOWING WHAT DOGS I LIKED WHEN I WAS TEN???”

I took a break from writing at that point to draw several pictures of what appear to be German shepherds.

Below the German shepherds, I wrote the three most disturbing words in the entire letter—three words that revealed more about my tenuous grasp on reality than anything else I have uncovered about my childhood. There, at the bottom of the letter, I had taken my crayon stub and used it to craft the following sentence: Please write back.

Judging by the thick, purposeful lines in each letter, I was applying a truly impressive amount of pressure to the crayon. The sincerity of the request is unmistakable. When I asked my future self what my favorite dog is or whether my mom and dad were still alive, I actually expected to get answers. And, apparently, I still expected to be ten years old when I got those answers. Please write back. I imagine myself patiently standing in the yard, day after day, thinking, Any time now . . . It’s going to happen soon, I just know it . . . 1, 2, 3, now. 1, 2, 3, NOW! 1, 2, 3, NOW

Time travel is a complex subject that I don’t expect a ten-year-old to fully understand, but this is more than just a basic misunderstanding of time travel.

ROUGH APPROXIMATION OF TEMPORAL CONTINUITY, AS IMAGINED BY A 10-YEAR-OLD: Person . . . . Undergoes mitotic event at age 10. One “me” Stays 10 . . . One “me” continues to the future *possibly no longer aware of self . . . . . 15 year later, writes letter and sends it to the past to inform self about favorite dog.

I’m almost definitely not a time traveler, but in case I am, I decided to write back. In fact, I decided to write letters to several iterations of my past self, because I felt there were important things I could explain to myself or things I could warn myself about.

Allow me to begin with a letter to my two-year-old self: Dear two-year-old: Face cream is not edible—no matter how much it looks like frosting, no matter how many times you try—it’s always going to be face cream and it’s never going to be frosting. I promise I wouldn’t lie to you about this. It’s honestly never going to be frosting. . . . For the love of *Pete*, please stop. I need those organs you’re ruining.

Dear four-year-old: Allow me to preface this by saying that I don’t know why you started eating salt in the first place, but regardless of the precipitating circumstances, there you are. As soon as you became aware that eating huge amounts of salt is really, really, uncomfortably salty, you should have stopped eating salt. That’s the solution. The solution is not to begin eating pepper to cancel out the salt. You’ve found yourself in this predicament several times now, and every time you get trapped in this totally preventable cycle. You’ve done more than enough experimenting to come to the conclusion that pepper is not the opposite of salt all by yourself, but somehow you seem to remain stubbornly unaware of this fact. . . To reiterate, no matter how much pepper you eat, it won’t undo the ludicrous amount of salt you ate before it. The only thing you are accomplishing by eating pepper is making your mouth taste like pepper AND salt. Similarly, switching back to salt again won’t cancel out the burning from the pepper you ate to cancel out the original salt. How is this so difficult to understand? You can stop whenever you want to. As a side note, you really need to start learning from your mistakes. Believe me, I know what happens when you discover electric fences next year, and you could do without that seventh jolt of electricity.

Dear five-year-old: What is wrong with you? Normal children don’t have dead imaginary friends. Normal children don’t pick open every single one of their chicken pox scabs and then stand naked and bleeding in the darkened doorway to their bedroom until someone walks past and asks what they are doing. Furthermore, normal children don’t respond by saying, “I wanted to know what all my blood would look like.” Normal children also don’t watch their parents sleep from the corner of the room. Mom was really scarred by The Exorcist when she was younger, and she doesn’t know how to cope with your increasingly creepy behavior. Please stop. Please, please stop.

Dear six-year-old: You’re having an absurdly difficult time learning the letter R. You practice all the time, and you have mastered every other letter in the alphabet—both uppercase and lowercase—but for reasons beyond my comprehension, R just destroys you. Look at this: (draw each “R” shown below in the air . . . graphically)

How does that happen?? How do you mess something up that badly? The first one is understandable, but what’s going on with that middle one? How did that extra protrusion get there? And look at the tiny one on the right—that one has four protrusions. I’m not an expert on protrusions, but that’s way too many. I think if you took some time to relax and really look at the letter R, you’d see that it’s not nearly as complicated as you’re making it.

Dear seven-year-old: Look at the other children around you. Do you see how they’re wearing clothing? That’s because they’re seven years old and they’ve all realized that it is no longer appropriate to take their clothes off in public. But you haven’t realized that, have you. People have tried to explain it to you. Your teachers have tried, your parents have tried, even the other students have expressed discomfort with your persistent and inexplicable nakedness. But you just don’t stop.

Why do you want to be naked so badly? DO you even know why? Are you overtaken by forces beyond your control that make you do this? Regardless, clothing is a reality that you need to accept. There are no loopholes to this. You can’t take your clothes off and hide in the corner hoping no one notices. You can’t trick the teachers into letting you be naked by burying yourself in the sandbox – your clothes are in a pile next to you. They know.

Dear 10-year-old: Wow, you really like dogs. In fact, you like dogs so much that I’m not even sure it’s emotionally healthy. It might be normal to love dogs a lot, or to be really interested in dogs, but you go way, way past that. Normal children don’t walk around pretending to be a dog nearly as much as you do, for example. You’re ten. It makes people wonder about your developmental progress when you growl and bark at them.

An even more concerning issue is the obstacle course. Fine, you want to train your dog to run through an obstacle course. That’s pretty normal. What isn’t normal is making your mother time you as you crawl through the course on all fours, over and over and over again. You’re making Mom think that she did something wrong to make you this way.

Now that we’ve gotten that out of the way, allow me to answer your questions:

Do you still like dogs? Yes, but not as much as you do. I’ve developed a healthy relationship with dogs.

What is your favarite dog? I don’t know. This may come as a surprise to you, but knowing exactly where each dog breed ranks on my list of favorites isn’t the pressing issue that it used to be.

Do you have a job tranning dogs? No. I can’t even train my own dogs, let alone the dogs of other people.

Is Murphy still alive? Of course not. I don’t know whether you’re being optimistic or you actually don’t understand that dogs usually don’t live to be twenty-five, but you really set yourself up for a lot of disappointment there.

What is youre favarite food? Nachos. Which is fortunate, because in the future, you’re dysfunctional and you don’t take care of yourself, so you end up eating a whole lot of nachos.

Are mom and dad still alive? Actually, you turned out to be Batman, so we had to have them put down for story-line purposes.

Dear 13-year old: I think everyone was relieved when you started to grow out of your unhealthy obsession with dogs. Unfortunately, now you think you are a wizard. I know this because I found your collection of spells.

Tell me, how does mixing Dijon mustard with sand and then eating it make someone love you? First of all, I though your extensive early experiences with ingesting non-food substances would put you off of attempting something like this. Secondly, no one is going to love you until you stop doing things like trying to make them love you by eating mustard-sand.

Dear other iterations of my past self: Thank you for not being so goddamn weird that I felt I had to address you personally in a letter form the future. I commend you.
```

---

## IC-1301: Wonder of the World

- Title: Wonder of the World
- Author (byline): David Lindsay-Abaire
- Work: Not specified
- Publisher: Overlook Press
- Publication date as stated: Oct 2022
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: CASS, KIP, LOIS, JANIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1868
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Lindsay-Abaire
ISBN: 978-1585673117
Publisher: Overlook Press
Date (Month/Year): Oct 2022
```

### Introduction (context only: never use it for content warnings)

```text
Cass and Kip . . . the perfect marriage; or so it seemed. Until Cass upset the apple cart and heads off to Niagara Falls, bucket list in hand and eager to explore (beat) by herself. Wonder of the World by David Lindsay-Abaire
```

### Performance text (classify this)

```text
CASS: (Pg 27) My name’s Cass. And I just left my husband. (hum the Newlywed Game Theme Song)* *****FLASHBACK*****

(Cass is packing a suitcase. A door slams off stage. Cass looks up, frozen)

KIP: (Pg 17-22) (Off-stage) Hey Sweetie! Guess who’s home for lunch?! (Cass futilely tries to hide the suitcase) Cass? Where are ya? (Kip enters)

CASS: ince when do you come home for lunch?

KIP: (notices the suitcase) What’s that? Are we going on a trip?

CASS: Not exactly, no. I’m leaving you.

KIP: You were just gonna run away without telling me?

CASS: I was gonna leave a note. Can you just stand in the corner until I’m done? (goes back to packing)

KIP: Is this about what I told you last night? (no answer) Just last week we played Yahtzee. I thought we were happy.

CASS: Yeah, that was a lot of fun. (beat) Really, this has nothing to do with you.

KIP: Then what happened?

CASS: Nothing. I just . . . I think I made a mistake. Remember that time you proposed, and I said yes?

KIP: That wasn’t a mistake.

CASS: But what if it was? Look, I agreed to marry you based on what I knew to be true. Kip equals X. X will make me happy. Everything added up. Seven Years later I find out you’re not X at all, you’re Z. I did the math wrong. Z is no good. I would never have said yes to Z. (beat) This is turning into a scene.

KIP: (Pg 23-24) I thought this wasn’t about me.

CASS: I was lying when I said that. (beat) Why are you making me sad? I don’t want to be sad. I’m a new person today. Happy! Bubbly! I’m starting a new life and brimming with expectation! There are possibilities where I’m headed!

CASS: (back to present day) (Pg 27) (Carries her suitcase to the door of a motel, sets it down as she fumbles with the lock. She picks ups the suitcase and heads inside as she talks to the audience) I’ve never been to Niagara Falls before. I almost went once. A family trip. But then Kip proposed, so I stayed behind to plan our wedding, and my parents went without me. They hit a beaver on the drive up, lost control of the car, and drove into a ditch. My mother was killed and my father’s legs were crushed.

LOIS: (speaks as the voice of Cass’s conscience) That man saved your life, you know. If he hadn’t proposed, you would’ve been in that car wreck.

CASS: You know what? I thought the same thing for a long time, but now I think if he hadn’t proposed, I would’ve gone with my parents, and yelled, “Dad, look out for that beaver!” And my mother would still be alive, and we would’ve gone on to see Niagara Falls, and maybe I would’ve met another man, the one I was meant to be with, instead of that two-faced deviant I married. (Pg 28) I had this list of all the things I wanted to do in life, but for some reason I put it away when I married Kip. P.S. BIG MISTAKE. (pulls out a list) Here it is. Number one is “Find your soul mate.” Ignore the checkmark. That one’s a do-over. Number two: Learn Swedish. Wear a large wig. (She takes a moment to put on a large wig) (Pg 29) Then we’ve got Have a baby. Wear overalls. Go parachuting. Become friends with a clown. Kips afraid of clowns, so . . Go on the Newlywed Game. Only Kip refused to audition. (beat, she gets lost in a memory) (Pg 38) In high school, I was a lifeguard and the only person I ever saved from drowning was Kip. That’s how we met. I saved his life. I used to think that was fate, but now I think it was just a coincidence. A coincidence that eventually led to the death of my mother. (embarrassed) (Pg 50) I used to speak lucidly. But someone disappointed me in unspeakable ways, and now my synapses don’t work all the way. (beat) (Pg 81) People used to say that Kip and I were a sweet couple. We were like yummy little bon-bons. (heavy sigh as she decides to reveal the truth)

(Pg 82) Kip has a sweater drawer. And I noticed that he was always wearing the sweaters from the front of the drawer, but never the ones from the back. So, I thought I’d rotate the sweaters. And while I was rotating. I found a box. A carved wooden box that we had bought on our honeymoon in Mexico. And it brough back all these nice memories of beaches and Mayan temples. And then I opened it. (beat, obviously distraught) And inside . . . were Barbie heads. (Pg 83) Detached. Eleven of them. And they all had crazy mangy hair. And dulled faces. And a strange disinfectant smell. And I thought, “Well, this is strange.” (beat) Not just the Barbie heads exactly, but the fact that Kip had a secret. (beat) That night I held out the box and I said, What is this?” And his eyes got real big and he started sweating and then he cried. And I thought, “Well this can’t be good.” (beat) And after an hour of utter silence he proceeded to tell me that he had started collecting the heads and cleaning them and naming them, and what I found was his little collection. (pulls out a mangy Barbie head) (Pg 84) This one is Vivian! (defiantly) I stole one. I carry it as a reminder. Every time I miss Kip or think of going back to him, I pull out Vivian and it all comes flooding back to me. (puts head away) All those years, while I was folding our clothes, he was living this strange secret life, totally separate from me. What else has he not told me? He made me feel so empty. Because I had no secrets. (spins around with arms outspread) And that’s why I came here. To fill myself up. To stuff myself with whatever I want. Gorge myself until I’m ready to burst. (Pg 110) Why can’t people just be who you want them to be? (A knock at the door – she peers though the peephole) (Pg 87) It’s Kip.

KIP: (Pg 88) (knocking while balancing a box on his hip) Cass, are you in there? Please let me in.

CASS: (Pg 89) (opens the door to confront Kip) Kip, go home. You’re gonna muck everything up.

KIP: After you left, I had an anxiety attack.

CASS: (sarcastically) Why, you have to empty the dishwasher yourself?

KIP: (Pg 90) Why are you being so mean? (notices her wig) And what is that?

CASS: It’s a wig.

KIP: Why would you wear a wig? Your hair is so nice. Your hair is probably my favorite thing about you. (a lightbulb goes off) (Pg 91) This was a test, wasn’t it? I was supposed to prove something back at the house; and I didn’t, I just let you go. But really you wanted me to fight for you. (Excited now, he begins to pull items from the box) I ‘ve brought some things. It’s evidence. See? Our photo album, champagne glasses from the wedding, my swim trunks from the day we met.

CASS: It’s just stuff, Kip.

KIP: I’m sorry, but you can’t just wake up one day and say our marriage didn’t exist. (Pg 92) Why are you doing this to me?! Can’t you see I’m having a breakdown?!

CASS: I’m not your lifeguard anymore. I’m not gonna jump back in the pool just because you’re splashing around.

KIP: I’ll see a specialist. I’ll get that (beat) thing (beat) taken care of.

CASS: (Pg 93) See, it’s always about you, Kip. What you did. What you want. What’s the matter with you?

KIP: (Pg 94) (Collapses, sobbing) I’m sorry! Okay?! What else do I need to do? Just tell me and I’ll do it. I know I was dishonest. I know you’re disappointed but give me another chance.

CASS: (Pg 96) Excuse me! (whips out the doll head and shakes it at him) Excuuuuuuuse me!

KIP: I was wondering where Vivian went. I wanted to dispose of her. As I did the other.

CASS: Go home, Kip. You’re wasting your time here.

KIP: (Pg 111) I called a marriage counselor on our behalf. (Pg 112) Glen says this therapist is a miracle worker.

CASS: Well, that’s swell, but I’m not a blind deaf mute.

KIP: Just give it a chance. She said she’d get here ASAP.

CASS: Get here? This is my room! You can’t just invite people over! (beat) (Pg 115) If we sit down with the counselor and talk, are you gonna stop acting like a crazy person.

KIP: Yes. Of course. If she counsels us to the best of her ability, and you still feel . . .

CASS: Contempt and loathing.

KIP: Okay. If you still feel those things, then I’ll go home.

JANIE: (Pg 121) (enters, dressed as a clown, big shoes; the works) Hello! (honks horn)

KIP: (terrified, screams) She’s a clown! (Cass laughs)

JANIE: (very professional in manner, no funny voice or anything silly) Only part-time. (gesturing to her costume) for the kids at the hospital.

KIP: (Pg 122) (composing himself) I’m the one who hired you. Don’t you wanna change?

JANIE: Nah, I’m good. The fact that you have the money, and you’re the husband, means *nothing* to me. Now sit down and we can get started. (Shaking hands with Cass) My name is Janie McShane.

CASS: You know what’s great, Janie? I was kind of dreading you, but now that you’re here, it feels totally right. I have this whole conundrum about fate, and one of the things on my list is become friends with a clown . . . and here you are!

JANIE: Okay. I’m guessing you’re a little unbalanced. Am I right.

CASS: Is that what Kip told you?

JANIE: You see these things on the side of my head? They’re called ears. And they pick up crackpot real clear. Now have a seat next to that gnome you call hubby. (Cass and Kip set and Janine gets to work) (Pg 126) What do you want from your husband right now?

CASS: I want him to . . . disappear.

JANIE: Good. Good. Next? (She turs to Kip)

KIP: (clears his throat, stand up to present as if at an AA meeting) My name is Kip, and my wife left me because I am a deviant. And I want things to be the way they used to be.

JANIE: Well, that’s impossible, you moron. No wonder your wife left you. (Pg 129) It’s too early to determine who does and doesn’t belong together. First, I have to find out how well you know each other. And in order to do that we need to play the Newlywed Game. (honks her hand horn)

CASS: (giddy) Oh, I love that game! (hum the Newlywed Game Theme Song)*

KIP: (Pg 130) That’s it! The whole thing is off! I don’t like games! And I don’t like clowns! This is everything I don’t like!

CASS: And everything I do like, Kip. I’m sorry she’s not what you had in mind, but sometimes that’s what happens in life. If you want to call it off, then we’re done. It’s up to you.

KIP: (defeated pause) Okay. Let’s play.

JANIE: Now I’m gonna pass out some questions and I want you to write down the answers on these cards. No peeking. (passes out cue cards, markers and questions) (Pg 131) Each question is worth twenty points. Question Number 1: What is your husband’s pet name for you? Cass?

CASS: Well, there are a few, but mostly he calls me lifesaver.

KIP: (flips his card and pumps his fist in the air) Yes! Lifesaver it is! (Cass smiles)

JANIE: (Pg 133) Cass, Kip’s first words to you?

CASS: I believe he said . . . “Help, help. I can’t swim. Holy crap, I’m drowning.”

KIP: (flips card and grins, bell rings) (to Cass) And you said we were strangers.

JANIE: (Pg 134-135) Now it’s the husband’s turn. Okay one question left, and it’s a bonus question worth 35 points. Kip, If you had to describe your wife as a fairytale character, which one would it be? (Pg 136) You need to get this right, or you go home empty-handed.

KIP: I understand. Well . . . (to Cass) Remember in high school you had that long hair? Rapunzel! My answer is Rapunzel.

JANIE: (Pg 137) Flip the card please.

CASS: (sadly) Rapunzel is locked away in a tower, cut off from the rest of the world. (She flips the card) (Buzzer sounds)

KIP: Wait! Do over! She didn’t understand the question! She said Jack! (to Cass) Jack and the Beanstalk Jack? (Pg 138) That’s not even a girl. How was I supposed to guess that? How is Jack better than Rapunzel?

CASS: Jack steals eggs and kills giants and chops things down! Jack does things. Jack lives life! Rapunzel sits around combing her hair all day.

KIP: She gets out of the tower eventually. The prince frees her or something.

CASS: (beat) But you’re not the prince, Kip. You’re not the prince in this story!

KIP: (Pg 139) This is just a game!

CASS: It’s not just a game. Things have meaning, Kip. Or at least they should. My life should have meaning. And I don’t think it does when I’m with you. You could’ve said anything. You could’ve said something wonderful and changes my mind. God, I would have loved that. But you said Rapunzel. After everything, you still don’t – I mean look at me! Do I look like a Rapunzel. [I’m Jack] Jack does things. Jack lives life! (whips out her list again) (Pg 29) Eat venison . . . (shakes her head) Visit a prison (shakes her head) Go parachuting! YES! (she honks Janie’s horn and exits with a flourish)
```

---

## IC-1302: 1984

- Title: 1984
- Author (byline): George Orwell
- Work: The 5-Minute Iliad and Other Instant Classics, Pgs 171-182
- Publisher: Gallery Books
- Publication date as stated: Aug 2000
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, WINSTON, TELESCREEN, O’BRIEN, STRANGER
- Teaser before the introduction: Yes
- Spoken words (computed): 1063
- Already set (do not supply): none

### Source block (context only)

```text
Author: Greg Nagan
Book: The 5-Minute Iliad and Other Instant Classics, Pgs 171-182
ISBN: 978-0684867670
Publisher: Gallery Books
Date (Month/Year): Aug 2000
```

### Introduction (context only: never use it for content warnings)

```text
Today we are seeing new limits on the rights and privileges of Americans. Gun control, abortion, LGBTQ rights, book banning, free and fair elections, immigration and asylum. The list of political battleground issues continues to grow.

A few years ago, no one would have believed that the government had the power to close businesses and schools for over a year because of COVID-19; but it happened. The country came to a standstill because “Big Brother” was the only one who was wise enough to protect us from ourselves. Right?

1984 by George Orwell as reimagined by Greg Nagan
```

### Performance text (classify this)

```text
By Greg Nagan

NARRATOR: (Pg 171) In 1949, when George Orwell wrote his infamous novel 1984, most of Western Civilization was struggling against totalitarianism – the political theory that the state should have total control over every citizen. Orwell set out to show that the tyrannical subjugation of the masses by torture and brainwashing was, indeed, a bad idea.

NARRATOR: (Pg 171-173) It was a bright cold day in April, and the clocks were striking thirteen: it was the future, and everything sucked. Winston Smith hurried upstairs to his apartment. In the hallway he passed a big poster of a handsome man whose eyes appears to be following you. (They used to have those jiggly eyes – those had been fun – but the Party had eventually settled on an iron-clad policy of NO FUN) Below were the words BIG BROTHER IS WATCHING YOU. This was also a recent innovation, ten years ago [it] replaced the original slogan, YOU’RE UNDER CONSTANT SURVEILLANCE, MAGGOT.

Winston let himself into his room and looked out the window at the Party ministries with rose imposingly above the city: The Ministry of Peace, which dealt with war; the Ministry of Love, which dealt with punishment; the Ministry of Truth, which dealt with propaganda; and the Ministry of Cute Little Puppy Dogs, which dealt with cats.

Slogans were etched into the windowless sides of the mammoth Ministry of Love: WAR IS PEACE; FREEDOM IS SLAVERY, IGNORANCE IS STRENGTH; BUT DIAMONDS ARE A GIRL’S BEST FIREND.

Winston worked in the Ministry of Truth and Hate Week was not far off. He had come home on his lunch hour to commit an act of enormous defiance – of rebellion. He stepped into an alcove beside the telescreen – it was on, of course – it was impossible to turn off – the alcove was the only part of his cramped and dreary little apartment into which the telescreen could not see.

He withdrew from his desk a diary and fountain pen which he had bought from an illegal diary and fountain pen dealer. Against all laws and regulation, he began to write:

WINSTON: (speaking as he writes) I hate the future: everything sucks. I hate my job because everything really does suck . . .

NARRATOR: The worst crime of all was thoughtcrime. It was only a matter of time before he would be caught.

WINSTON: (speaking as he writes) I’m a doomed man. Doom sucks.

NARRATOR: The next day at the Ministry of Truth he spent his morning rewriting old newspaper and history books to reflect the truth as adjusted by the Party. That was his job.

WINSTON: It sucks.

NARRATOR: He had lunch with people he didn’t like. While they ate . . .

TELESCREEN: The standard of living has risen another 20 percent.

WINSTON: (Applause)

TELESCREEN: Another battle has been won against Eurasia.

WINSTON: (Applause)

TELESCREEN: Big Brother wants everyone to stand up.

WINSTON: (Stands up)

TELESCREEN: Big Brother wants everyone to sit down.

WINSTON: (Sits down)

TELESCREEN: Everyone should stand on one leg.

WINSTON: (Starts to, then stops)

NARRATOR: A few people did, and they were taken out and shot because Big Brother hadn’t said to.

WINSTON: (thumbs up to the audience with a big smile and a fake wiping of sweat from his brow)

NARRATOR: (Pg 175-177) One day Winston’s section chief approached his cubicle. O’Brien was the Inner Party man Winston suspected of secretly sharing his view that everything sucked.

O’BRIEN: (in a suspicious manner) I’ve been reading your columns . . . Come by my house. (he hands Winston a piece of paper) Here’s my address. Come by any time. (he exits)

WINSTON: (to audience) Awfully clever. The Party would suspect nothing.

NARRATOR: And yet it was clear O’Brien was inviting Winston to come by his house and talk privately

WINSTON: About how much everything sucked!

NARRATOR: And maybe, just maybe, he’d invite Winston

WINSTON: To join the Brotherhood! (awkward non-verbal celebration) *****A Few Weeks Later / O’Brien’s Study *****

O’BRIEN: Why are you here?

WINSTON: I want to join the Brotherhood and dedicate my life to fighting the Party.

O’BRIEN: I see. Very good. (Taking out a checklist) Are you willing to die for the Brotherhood?

WINSTON: Yes.

O’BRIEN: Would you put a kitten into a blender for the Brotherhood?

WINSTON: Yeeessss?

O’BRIEN: (switching over to a baby voice) Even if it was an adorable little kitty-cat looking at you with those big eyes and going meow, meow and just so cute you could scream?

WINSTON: (with resolve) Yes!

O’BRIEN: Really? Wow. That’s good to know. Now go home and pretend nothing has happened. You’ll never meet any other members; you’ll never know that anything’s different at all. Some time when you don’t expect it a man will hand you a briefcase, and in that briefcase will be a cove of THE BOOK which explains everything. Leave now. *****

WINSTON: (Pg 178) HATE, HATE, HATE! (stomping, thrusting his fist in the air)

NARRATOR: Hate Week came at last and all of Oceania lathered itself into a frenzy chanting hate for all enemies of Big Brother.

WINSTON: HATE, HATE, HATE! (stomping, thrusting his fist in the air)

NARRATOR: And then . . . suddenly . . .

WINSTON: (he notices the large telescreen and makes a mad scramble to grab and place various hats on his head, pushing, shoving invisible others)

NARRATOR: There was a mad panic; everyone had to have a hat and had to have it at once. There was violence, rioting. Apparently, there’d been a typo and the telescreens were suddenly telling everyone to celebrate HAT WEEK. Anyone not wearing a hat was taken out and shot.

STRANGER: (to Winston, slyly) I think you dropped your briefcase.

WINSTON: I didn’t bring my briefcase.

STRANGER: I think you did.

WINSTON: I’m pretty sure I didn’t. (exasperated, the stranger motions with the briefcase; Winston finally remembers the directive from O’Brien) Sorry! (he takes the briefcase)

NARRATOR: At last he would have a chance to read THE BOOK. ***** A few days later *****

WINSTON: (Pg 179-181) (reading aloud) THE THEORY AND PRACTICE OF OLIGARCHIC COLLECTIVISM (makes exaggerated excited and somewhat scared face) Chapter One: Ignorance is Strength – Since the dawn of man, there have been three varieties of human kind: the idiots, the morons and the bastards. (reacts to the sentence; flips pages, skimming for the answers he wants) Perpetual state of warfare . . . easier for the governments to suck and to make life suck for their people . . . everything sucks for everyone forever. (nods head; book is affirming that he was right)

NARRATOR: He read how there could never be any more revolutions because there were no longer any unhappy people. At the first signs of unhappiness people were taken out and shot.

WINSTON: That sucks!

NARRATOR: [And] Before he had a chance to . . .

WINSTON: The apartment was invaded by Thought Police! It has all been a setup!

(Winston takes blow after blow from the Thought Police)

NARRATOR: They beat the crap out of him. Not very futuristic, but effective. [He] woke up in jail. Days went by; weeks, months, maybe even years. Thought Police would come in at erratic intervals and beat him or tickle him until he wet his pants.

O’BRIEN: I’m going to torture you until you realize that Big Brother loves you, and that you love Big Brother.

WINSTON: Big Brother Sucks! (succumbing to tickle torture with an embarrassed look as he wets himself)

NARRATOR: He could take no more.

WINSTON: Don’t torture me. I don’t care, just leave me alone!

O’BRIEN: I was hoping you’d say that. You’re free to go.

NARRATOR: (Pg 182) A few months later, Winston was sitting alone at a café.

WINSTON: (with a vacant look on his face attempts to drink from a coffee cup, but spills it down his front; it’s clear that the beatings have had an effect on his intellect)

NARRATOR: Once in a while he’d look up at the poster BIG BROTHER IS WATCHING YOU and feel a certain reassurance. (Winston looks up and smiles creepily) It was sort of comforting to be watched. He liked the idea that someone was looking out for him.

He felt filled with warmth. (Winston wets his pants, notices, but is not embarrassed, he just smiles) The future didn’t suck after all. He loved Big Brother. Maybe love was too strong a word. But he liked him. He really, really liked him.
```

---

## IC-1303: 24: The Ultimate Script

- Title: 24: The Ultimate Script
- Author (byline): Dave Barry
- Work: I’ll Mature When I’m Dead: Dave Barry’s Amazing Tales of Adulthood, Pgs 127-156
- Publisher: Putnam Adult
- Publication date as stated: May 2010
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, THE PRESIDENT, THE VICE PRESIDENT, FBI DIRECTOR, GENERAL, CHIEF OF STAFF, DOCTOR, JACK, CHLOE, FIRST TERRORIST, SECOND TERRORIST, TERRORIST, JACK'S HEAD, JACK BAUER'S VOICE
- Teaser before the introduction: Yes
- Spoken words (computed): 1507
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
Personally, I gave up on 24 during the second season, when Jack Bauer's daughter was menaced by a cougar, but the show lasted a blockbuster eight years. Or, in show terms, eight days. See each episode only covers 1 clock hour in Bauer’s rather mundane life . . . Each season shows only 1 24-hour day . . . Eight years = 8 days. . . but over those eight days secret agent Jack Bauer had to use a lot of excessive force to save the country. How much excessive force? He killed TWO HUNDRED SIXTY-SEVEN PEOPLE in eight days. In case you haven’t seen the series . . . I’ve prepared a trailer for you . . . 1 hour in less than 10 minutes! Move over Chuck Norris, the new man of the house is Jack Bauer.

This is . . . 24: The Ultimate Script by Dave Barry
```

### Performance text (classify this)

```text
NARRATOR: (Pgs 127-156) 6 A.M. -- THE WHITE HOUSE SITUATION ROOM -- The president, seen only in silhouette, sits at the head of a conference table. Seated around the table are the vice president, the Joint Chiefs of Staff, and various important-looking extras. The lighting is dim.

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

## IC-1304: Ace Lacewing: Bug Detective

- Title: Ace Lacewing: Bug Detective
- Author (byline): David Biedrzycki
- Work: Not specified
- Publisher: Charlesbridge
- Publication date as stated: July 2005
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: ACE, MAYOR, XERCES, SGT ZITO, MAGGOT, TWIG, ROACH, DRONE BEE, MANTIS, UNIDENTIFIED DRONE, PRINCESS POLLEN
- Teaser before the introduction: Yes
- Spoken words (computed): 1673
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
He’s tall, he’s handsome and he has two antennae. He’s Ace Lacewing, Bug Detective by David Biedrzycki
```

### Performance text (classify this)

```text
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

## IC-1305: The Actor’s Nightmare

- Title: The Actor’s Nightmare
- Author (byline): Christopher Durang
- Work: Sister Mary Ignatius Explains It All for You and The Actor's Nightmare
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: June 1999
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: GEORGE, MEG, ELLEN, VOICE, SARAH, EXECUTIONER
- Teaser before the introduction: Yes
- Spoken words (computed): 1777
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
We’ve all had dreams spurred by anxiety . . . Perhaps the lawyer who gets up to begin his opening statement and can’t find his papers? Or when he does, they’re in German? The emergency doctor who goes to make an incision and his instruments have turned to rubber? Still, it seems the cruelest forms of these nightmares are those that dog the poor actor. The Actor’s Nightmare by Christopher Durang
```

### Performance text (classify this)

```text
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

## IC-1306: Adaptation

- Title: Adaptation
- Author (byline): Elaine May
- Work: Not specified
- Publisher: Dramatist's Play Service
- Publication date as stated: 1970
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: ANNOUNCER'S VOICE, GAMES MASTER, MOTHER, PHIL, PRINCIPAL, ASHLEY, MARK, IRVING, PROFESSOR, DORIS, AFTER DINNER SPEAKER
- Teaser before the introduction: Yes
- Spoken words (computed): 1072
- Already set (do not supply): none

### Source block (context only)

```text
Author: Elaine May
ISBN: 978-0822200093
Publisher: Dramatist's Play Service
Date (Month/Year): 1970
```

### Introduction (context only: never use it for content warnings)

```text
by Elaine May
```

### Performance text (classify this)

```text
ANNOUNCER'S VOICE: (Pg 5) Good evening, ladies and gentlemen. You are about to watch a new version of an old game that all of you have played, and some of you may recognize--ADAPTATION - an exciting contest in which anyone can win simply by figuring out the rules and overcoming the odds. Watch closely, as tonight's first contestant, Phil Benson, attempts to win the Adaptation Prize by reaching the Security Square concealed somewhere on our gameboard. [Now let’s play . . .] ADAPTATION!!!!!!!

GAMES MASTER: (Pg 6) You are born. Move three spaces forward. You are now the son of, liberal, middle-income, Protestant, white, parents.

MOTHER: Harry, It’s a boy. I’m going to name him Phil.

GAMES MASTER: (Pg 7-8) You are [now] five [years] old. Score one Point for Maturity and advance to your nearest Health Through Information square.

PHIL: Mommy, how does the baby get into the mommy's stomach?

MOTHER: Via sexual relations between man and woman, Phil. (Buzzer sounds. When it stops, Phil has become a year older.)

PHIL: Mama, what's sex?

MOTHER: Sex is a term that defines the . . . (Buzzer sounds again. When it stops, Phil has become another year older.)

PHIL: Mom, what's a Negro?

MOTHER: Phil, do you know how when you see a flower sometimes there's a white flower and sometimes there's a dark flower. Bees go to both of them because bees like dark flowers as much as they like white. And that's why when we say the word Negro we must think of it as something very, very beautiful. And we must try not to use the word outside the context of a sentence that has to do with social justice.

GAMES MASTER: You have learned to Dissemble. Score two Points for Maturity and advance to Public School. (Phil looks around in awe at the new larger world he is inhabiting when an announcement comes over the intercom from the PRINCIPAL)

PRINCIPAL: Any student using the elevator without an official pass from the dean will be graded down ten points in Living With Others. Remember, you are only second graders but any bad mark you receive on your school record now may keep you from getting into the college of your choice.

PHIL: (Phil walks down the hall, aging in mannerisms as he does so – he notices a line on the ground, which he hesitates to cross – He stops, unsure of himself)

GAMES MASTER: (Pg 9-10) And now--take a giant step into Prepubescence.

PHIL: (Phil lurches forward as if pushed from behind; once on the other side of the line, he flexes his muscles, pops a couple of pimples on his face and feels his chin for growing facial hair.)

GAMES MASTER: Your mother is called to school for a conference with the school princi-pal. Go to your nearest Isolation Square. (Phil turns to stand in the corner)

MOTHER: What did he do, Mr. Ashley?

ASHLEY: He wrote something on the walls about one of the students - who happens to be colored. (Reading from a slip of paper.) "Jim is a dark flower." We're trying to appease his mother now, but she's threatened to release the story to the New York Post ... which would destroy the image we have tried to build up for this school as sub-standard but equal. Frankly, Mrs. Benson, it's a dilemma.

GAMES MASTER: You are sent to a progressive, private [high] school. Advance three squares to Social Inflation.

PHIL: (Pg 11-12) (Phil makes an abrupt right turn and speaks with some friends) What are you choosing as an extra-curricular activity, Mark?

MARK: I'm joining the Drama Society. (in an overly dramatic voice) If I learn to speak with feeling it will help me get girls.

PHIL: What are you choosing, Irving?

IRVING: I've decided to become a safety patrol boy. There's been too much bloodshed. Too many good kids gone. I [want] to make the corners of this city a place where kids can cross without fear.

PHIL: (Phil speaks to the audience) A safety patrol . . . Have I changed myself enough to change the world? Do I have the right to stop traffic? (Suddenly ... he jumps to save a wayward child and says in a deep voice.) Watch it there! You're safe now, kid. (Phil assumes the role of the child and in a childlike voice says) Thank you, Safety Patrol Boy. (In his normal voice, to the audience) Do I dare?

GAMES MASTER: (Pg 16-18) Start to think about your college and advance to your nearest Probable Long Term Goals Square.

PHIL: It's between Berkeley . . .

GAMES MASTER: (Hands Phil a letter, shaking his head) You have been rejected by Berkeley.

PHIL: or Yale . . .

GAMES MASTER: (Hands Phil a letter, shaking his head) You have been rejected by Yale. Retreat to the nearest Panic Square.

PHIL: (In a panic, he desperately tries to think of another option . . . ) I think I'll try the University of Miami?

GAMES MASTER: (Smiling broadly) You are accepted by the University of Miami. Advance to your nearest Commitment Square and begin to examine your potential.

PHIL: I'm not sure what to major in, I'm torn between Hotel Management and [Drama]. But I've always had a dream that someday I'd make it . . . in hotel management like some of the great ones. Hilton, Sheraton . . . [Trump]. (Phil takes his place in his first college class, prepared to take notes)

PROFESSOR: Good morning, gentlemen. My name is Professor Olsen, o-l-s-e-n, and I will be teaching the first semester of Hotel Management 101 - Organization, Administration and Management. Or as we in the field have come to call it, O.A.M. O! A! M!

PHIL: (chanting) O! A! M! O! A! M!

GAMES MASTER: (Pg 22-24) You have made an "A" in O.A.M. Advance to Find the Right Girl.

PHIL: (Takes a step to the left and speaks to Doris) I love you. Do you love me?

DORIS: I want to know where I stand, Phil. You know what I mean.

PHIL: Listen, Doris, if I thought marriage would solve it . . . I mean, I know that I enjoy being with you and if I were going to make the move you'd be the first one I'd call. I hope someday to love and have a home. But right now. . . . I don't know.

DORIS: Then I'm leaving. I'm sorry, Phil.

PHIL: You’re leaving me? Don't tell me you're sorry. Just tell me where I stand.

DORIS: Listen, if I thought marriage would solve it . . . PHIL. (Dropping to one knee to propose) It will. It will.

GAMES MASTER: You are Engaged.

PHIL: Oh, my God.

GAMES MASTER: (Pg 25) You go into debt and become a Homeowner. Take a Credit Card and advance towards Upward Mobility.

PHIL: (Pg 24) Oh, my God.

GAMES MASTER: (Pg 26) You are transferred to a larger city and have your first child. Advance to Fatherhood.

PHIL: (Pg 24) Oh, my God.

GAMES MASTER: (Pg 27) (Buzzer.) Advance to Middle Age.

PHIL: Wait a minute!

GAMES MASTER: The world is getting faster. Take out an Insurance Policy and advance to Political Involvement.

PHIL: Doris! Doris! The Chicago Hilton is going to be used by the Democrats for the National Democratic Convention-and guess who's going to be in charge. Yours truly. I can't wait. Caucuses, smoke-filled rooms, favorite sons ... Doris, this is the moment I've been preparing for all my life. This is what it's all about. This is O.A.M. [But it’s all moving so fast!]

GAMES MASTER: You have reached a Long-Term Goal. Advance to Emotional Fulfillment and take another step toward Success.

AFTER DINNER SPEAKER: (Pg 29-30) And so, to Phil Benson, the Hilton Hotel Chain awards this solid gold engraved master key that fits the utility closet of any Hilton hotel on the Eastern Seaboard.

GAMES MASTER: You have retired with moderate wealth. Take two steps sideways toward Security and . . . . have a Coronary.

PHIL: (Has a heart attack and speaks with difficulty) I had so many dreams I wanted to earn a Super Bonus Card and have a house in the country And I wanted to be on intimate terms with a congressman or a movie star so that my father would be proud of me and my mother would think I was somebody. If I could have played a little longer, I know I could have found the Security Square . . . Where did I go wrong? (Phil dies)

GAMES MASTER: You have spoken your last words. Remain where you are and die.
```

---

## IC-1307: Adolf Hitler: The Larry King Interview

- Title: Adolf Hitler: The Larry King Interview
- Author (byline): Jon Stewart
- Work: Naked Pictures of Famous People (Pg 139-150)
- Publisher: Harper Collins
- Publication date as stated: Oct 1999
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: KING, HITLER, ITLER
- Teaser before the introduction: Yes
- Spoken words (computed): 1453
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jon Stewart
Book: Naked Pictures of Famous People (Pg 139-150)
ISBN: 978-0688155308
Publisher: Harper Collins
Date (Month/Year): Oct 1999
```

### Introduction (context only: never use it for content warnings)

```text
One of the beautiful aspects of our culture is the capacity we have to forgive, especially those in the public eye. This grand compassion was put to the ultimate challenge when in the fall of 1999 an astonished world watched as a historical figure long thought to have died in World War 2 resurfaced. This disgraced dictator, swayed by a beautifully arranged fruit basket and handwritten note, went on CNN's Larry King Live. The Hitler interview, as it became known, aired on October 23, 1999. The following is an uncensored transcript of that historic interview.

Adolf Hitler: The Larry King Interview by Jon Stewart
```

### Performance text (classify this)

```text
KING: (Pg 139-150) (Larry King Live Music*) Good evening, ladies and gentlemen. Tonight we bring you perhaps the most controversial show in the history of Larry King Live. He began his career as president of the fledgling National Socialist party, the Nazi party, in Germany. After a failed coup, some prison time and a bestselling book, he reestablished himself in the German hierarchy, first as chancellor. . . then as Fuhrer. The next ten years under his watch saw Germany's return to power, shame at the Munich Olympics, a failed marriage and finally, one helluva World War complete with what was thought to be a cowardly demise by his own hand. Tonight, risen from the proverbial dead, we welcome Adolf Hitler.

KING: Well, Chancellor Hitler, I have-

HITLER: Please call me Adolf.

KING: Adolf. First of all, I have to say. . . quite frankly, we were very reluctant to have you on.

ITLER: I can't say I blame you for that. I mean, you hear the name Hitler ...

KING: What do you say to all the people out there, the people who view you as a demon, the perpetrator of the most vicious-

HITLER: Guilty as charged, Larry. Look, I was a bad guy. No question. I hate that Hitler. The yelling, the finger pointing, I don't know. . . I was a very angry guy.

KING: And this. . . new Hitler?

HITLER: I get up at seven, have half a melon, and do the Jumble in the morning paper. Some days I’ll fish, maybe hit the mall for an Orange Julius. The other day I spent seven hours in the park watching ants cart off part of a sandwich. Me!! The inventor of the Blitzkrieg. . . When you stop having to control everything, it's very freeing.

KING: Why did you do it?

HITLER: Whooo boy. The $64,000 question. I don't know. . . I wasn't a happy kid. I mean, I'm not trying to make excuses, but you go through high school with the nickname S***ler I'm sorry, they can bleep that, right? After a while you get sick of it. One day you just snap. It started out as the typical "Someday you guys will be sorry," and then . . . I don't know. It just got away from me.

KING: Did you ever see the despicable nature of your actions? Was there any remorse?

HITLER: Oh sure, but denial is a powerful thing. . . I always thought I could stop any time I wanted. "If I could just get Czechoslovakia, that'll be the end of it. I'll be happy then." And I'd get it and think, well geez, Poland's just up the road a piece and. . . you know the rest. I think admitting to myself that there was a problem was the toughest part.

KING: And when was that?

HITLER: Well. . . I'm not going to lie to you, it took a while. There were moments all along where I knew something was wrong. I remember one time. . . I think it was in Munich in 1942. We were having a rally. 100,000 people all chanting my name. The bonfires were going. The whole shebang. It should've been a crowning moment but I clearly remember thinking, What am I doing here? I hate crowds. But I didn't hit rock bottom until, as you know, 1945.

KING: Yes, tell us about those final days in the Berlin bunker, where, until now, we had assumed you had killed yourself.

HITLER: (takes a sip of water) Right, well. Funny story. Everyone thought I went into the bunker to escape . . . [but] No. Actually, as the Allied Forces were closing in I was still in denial. I really thought we were gonna rally, you know, make an end run around Switzerland and flank 'em. So I'm planning furiously and snapping at people-as my therapist says, "playing the dictator." So Eva calls me down to the bunker for some "emergency" with the generators. Anyway, I go down and there's Eva and Himmler and two of my other closest friends. I'll never forget. I walk in and Eva takes my face in her hands, looks me in the eyes and says "Adolf, we all love you very much, but if you don't stop with this conquer and purify thing, no one in this room will ever talk to you again."

KING: And that snapped you out of it?

HITLER: Not quite. You have to understand I'd been running with this thing for about fifteen years at that point. (beat, then nonchalantly) I shot them. Back then we didn't know [about] interventions. I just figured they were betraying me. Anyway, I threw on Eva's clothes and snuck out into the night. I lived like an animal for weeks, doing what I had to do to get by. One day a group of boys were making fun of the lady with the mustache, and I got a look at myself in the reflection of a window and realized they were talking about me. It was then I knew I had to get my life together.

KING: Interesting. Now tell me about your relationship with Eva. She was a beautiful woman. Do you think she was mesmerized by your power?

HITLER: Well, all I can say is (breaks into a broad smile) Look, Larry. I learned long ago that Bavarian art majors with oily hair and weasely mustaches weren't getting the ladies. Of course, that was the only reason Eva went out with me. Women love power and fame.

KING: (changing the subject) Scientists recently cloned a sheep . . . Dolly I believe was her name. You've always had an interest in things genetic. Your take on this scientific breakthrough?

HITLER: Well, Larry, "transgenics," as that branch of genetic research is known, is an exciting specialty, and the Roslin project, the sheep cloning, is an exciting advance. But I certainly wouldn't qualify it as a breakthrough.

KING: You must admit there are real ethical questions that go along with the cloning of humans.

HITLER: Well, Larry, the big fear here is that some evil guy gets a hold of this stuff and makes another me. (beat, shaking his head) People will never be cloned. Superficially perhaps, but personality, character, even intelligence cannot be genetically duplicated. Only tendencies. I'm a big environment convert. Nurture over nature. You could duplicate my genes, but you wouldn't get me unless you duplicate my upbringing. You'd have to get some older children to tease this new Hitler mercilessly, giving him constant wedgies . . . (Hitler begins to cry.) Excuse me, I believe some dust is in my contacts. (Hitler wipes his eyes.)

KING: Was the Third Reich working on cloning?

HITLER: (sips some water) Oh, sure, we gave it a shot. We created some chickens that vaguely resembled each other. And one of our top guys cloned a replica of your heroic dog Lassie-but after some checking, we found out it was just a reassembled Corgi. All involved were put to sleep. Our guys just weren't up to the task.

KING: You had certainly made science a priority . . .

HITLER: Which brings up an interesting irony. Here I was, a guy with a plan to create a master race, dominate the world by blending brute force with cutting-edge technology. So what do I do? I deport or kill all my best scientists. The Jews were some of my best technical people. It's classic fear of success. I create something, then sabotage its chances of ever actually working. It's a pattern I've repeated over and over again. I'm defeating all challengers on the Western front, couple more weeks, I got the whole thing sewn up. So what do I do? Attack Russia?!! (Hitler taps his finger on his temple.) Way to go, genius!!

KING: But you got away with it. After all these years, why resurface?

HITLER: My therapist challenged me to put up or shut up. To prove to myself that I could take responsibility for my life. So here I am.

KING: (holding up a book) We've been talking with Adolf Hitler, the book is-

HITLER: . . . The book is called Mein Comfortable Shoes-get it? It's about an angry man who learns to appreciate the little things in life. It's about acceptance.

KING: And it's a terrific read. Folks, if you read no other book this summer, make it Mein Comfortable Shoes. What's next for Adolf Hitler?

HITLER: I'll be doing Politically Incorrect next Thursday, and as always you can see my old work on the A&E network. And in two weeks, I'll be appearing on Court TV as I stand trial for crimes against humanity.

KING: Right, that is coming up. What kind of defense will you be offering?

HITLER: Not much. I fully expect that by this time next year, I'll have been convicted and possibly put to death. I'm going to represent myself, though. From now on the blame goes here (pointing to chest). The only one to blame for Hitler . . . is Hitler. Besides, who wants to get involved with a bunch of phony-baloney defense lawyers. . . I mean, talk about evil.

(Both laugh.)

KING: Well, Adolf, thanks for coming by.

HITLER: Thank you. CLOSING

KING: Stay tuned next week when we get up close and personal with another “man-about-town” -- Former President Donald Trump! (Larry King Live Music*)
```

---

## IC-1308: The Adventures of Captain Neato-Man

- Title: The Adventures of Captain Neato-Man
- Author (byline): Timothy Scott Harris
- Work: Off-Off Broadway Festival Plays – 15th Series
- Publisher: Samuel French, Inc.
- Publication date as stated: July 2017
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: LARRY, MOTHER, CAPTAIN
- Teaser before the introduction: Yes
- Spoken words (computed): 1545
- Already set (do not supply): none

### Source block (context only)

```text
Author: Timothy Scott Harris
Book: Off-Off Broadway Festival Plays – 15th Series
ISBN: 978-0573692406
Publisher: Samuel French, Inc.
Date (Month/Year): July 2017
```

### Introduction (context only: never use it for content warnings)

```text
The Adventures of Captain Neato-Man by Timothy Scott Harris reminds me of the things my brothers and I would make up when we were kids. Hopping from the couch to the coffee table as if we were leaping across rooftops in pursuit of dastardly criminals. I even had my own cape made out of one of mom’s dishtowels.

The Adventures of (DUH-DU-DUH!) Captain Neato-Man (echo, echo, echo) by Timothy Scott Harris
```

### Performance text (classify this)

```text
LARRY: (leans through an open door as he rings the buzzer) Hello?

MOTHER: (Off -- Screaming) Who’s there?

LARRY: I’m sorry. I’ve come for . . .

MOTHER: (Enters) What?!

LARRY: (Enters cautiously, carrying a newspaper clipping in his hand) I’m sorry. I must have the wrong. . .

MOTHER: I’m an old woman. I need my rest. Are you here for the ad?

LARRY: Uh, yes.

MOTHER: Why didn’t you say so? Son! Horatio is here!

Captain Neato-Man bounds onto the stage. He wears high boots, tights, a Speedo with a belt around it that carries his special gadgets, a tight-fitting shirt, and a cape with his name on it.

CAPTAIN: Horatio, my boy, you’re alive, alive! You don’t know how long I’ve waited for this moment. Stick with me and you’ll be a man. We shall tackle the cosmos together and our names shall live as one.

LARRY: I’m sorry, my name is Larry. Larry Friedman. I . . .

CAPTAIN: Larry. Horatio. What’s the difference? You answered the ad, didn’t you? Well, there you go. What are you complaining about?

LARRY: I thought this was a typing job.

CAPTAIN: Are you a communist?

LARRY: No.

CAPTAIN: Then you’re on my side. You are perfect, Horatio. Say you’ll join my team.

LARRY: What’s going on here?

CAPTAIN: Quick. If you looked up and noticed a baby falling right towards you. What would you do?

LARRY: Catch it?

CAPTAIN: It took me two weeks to pass the baby test, and you did it on the first try!

LARRY: Aw, it was nothing.

CAPTAIN: Modest . . . a superhero’s most important virtue. Do you understand how incredible our potential can be if we band together?

LARRY: No.

CAPTAIN: The fame.

LARRY: (sarcastic) Right.

CAPTAIN: The glory.

LARRY: (sarcastic) Right.

CAPTAIN: The women.

LARRY: The women?

CAPTAIN: Yes, thousands of adoring beauties clamoring for you to write personal inscriptions on their [bodies].

LARRY: Wow.

CAPTAIN: And the monetary rewards are incredible.

LARRY: Money?

CAPTAIN: Sure. You can make a fast fifty just for saving a fat lady’s cat.

LARRY: I’m good with animals.

CAPTAIN: And if you do really well, the mayor will give you the key to the city . . . Exciting, isn’t it?

LARRY: Great. What do I have to do for all that?

CAPTAIN: Simple, just jump off a tall building. . . or walk through a blazing fire.

LARRY: But I’d burn.

CAPTAIN: Not if you’re a superhero.

LARRY: I’m not.

CAPTAIN: That’s because you don’t believe in yourself. Say you’ll do it. Say it!

LARRY: I really appreciate the offer, but I’m not the type.

CAPTAIN: Type. There is no such thing as type. It’s not what you are, but who you are. How does a caterpillar turn into a butterfly? How does a seed turn into a flower? How does a larva turn into a leech? They change from the inside. Only you can decide who you are. You can go on being Larry the Larva, or you can be “Horatio” the defender of justice and sidekick to . . . “Captain Neato Man.”

LARRY: That all sounds wonderful. It’s just that I’m not qualified.

CAPTAIN: What have you done?

LARRY: Mowed lawns, baby sat, worked at McDonald’s.

CAPTAIN: McDonald’s. The epitome of the American dream. It was fate that brought you here.

LARRY: But I liked McDonald’s. They were going to make me assistant manager soon.

CAPTAIN: Then why did you answer the ad? The ad clearly states, “Be a real life superhero.”

LARRY: Please, I thought it was time for a change, but I was wrong. I’m afraid I’ll have to . . . leave.

CAPTAIN: You can’t leave.

LARRY: Why? (pause)

CAPTAIN: Because the door is locked and only I can open it.

LARRY: Let me out or I’ll scream.

CAPTAIN: Nobody will hear you. The walls are soundproof.

LARRY: If you don’t let me out, I’ll hit you, I swear.

CAPTAIN: (laughing) With my superpowers? Besides, you’re too nice. (They face off until Larry backs down)

LARRY: Ok. Ok. I’ll give you a chance. I’ll stay . . . I’ll stay . . . (Larry picks up the phone and tries to dial, but there is no dial tone) Operator. Operator.

CAPTAIN: That’s a special phone. It only takes incoming calls. The police commissioner has the number. Whenever there is a problem he can’t handle, he calls me.

LARRY: Oh, I see. How often does he call? . . . On the average . . . how many times a week?

CAPTAIN: I can’t give that information out to just anyone.

LARRY: He never calls. Does he?

CAPTAIN: He knows I’m here. He’s just a very busy man. As a matter of fact, he sent some people over just last week to talk with me.

LARRY: He thinks you’re crazy.

CAPTAIN: You don’t know. You weren’t here. I’m a superhero!

LARRY: Then prove it to me, and I’ll stay.

CAPTAIN: Neato! You won’t be sorry, Horatio. That’s the spirit. Now try on your suit!

LARRY: You haven’t proven anything yet.

CAPTAIN: Oh, still uptight, are we? You know, without your suit, your superpowers are greatly diminished. The special fabric is a unique nylon and acrylic blend. It’s resilient to blows which would otherwise be fatal . . . Jeez. How much proof do you need?

LARRY: Anything. Show me anything.

CAPTAIN: I see. I was going to save this ‘til later, but if you insist . . . My secret weapon!

(Captain pulls two identical toy guns out of a box. They look incredibly cheap and plastic. He hands one to Larry and puts the other in his belt.)

LARRY: Where did you get these? A box of Cocoa Puffs?

CAPTAIN: I saved box tops for six months.

LARRY: You are insane.

CAPTAIN: No. You don’t understand. The shape and size of this toy gun was exactly what I needed to create the perfect weapon. With a few minor alterations it became . . . THE LAZOMATIC! This baby can shoot a laser beam accurately up to 3,000 feet, annihilating anything in its path.

LARRY: Ooohhh. Wow.

CAPTAIN: Want to test it? OK. Aim at that plant. What are you waiting for? Shoot the fern.

(Larry aims at the fern and shoots. The gun makes a funny noise. Nothing else happens. He looks at the gun and tries again. Still nothing. He shoots at his head. Same thing. Captain grabs the gun and starts fiddling with it)

LARRY: It doesn’t work. It’s a toy.

CAPTAIN: That’s because you didn’t believe

LARRY: I’m not an idiot . . .

CAPTAIN: It just needs a few adjustments, that’s all.

LARRY: I know you’re crazy, but you can do this on your own. You don’t need me. Give it a try. What are you afraid of?

CAPTAIN: I fear nothing. I’m a superhero! . . . I think it’s best to have a partner, that’s all. I mean sure I could do it myself, but I’ve been waiting for a partner.

LARRY: Then why don’t you team up with . . . Superman?

CAPTAIN: What are you? Some kind of lunatic. There is no Superman. That’s make believe. It’s only a story.

LARRY: What about Batman?

CAPTAIN: Batman’s real, but he’s getting old. He can’t do it all on his own, and you know about Robin.

LARRY: You see. I don’t care. I just don’t care.

CAPTAIN: He sold out. Went into real estate. Look, it’s up to us now. We are the world’s only hope. You can’t walk away from your duty. The crime rate is outrageous. Disney is making horror pictures, and you don’t care?

LARRY: Oh, please.

CAPTAIN: You want to believe me. Deep down you’re intrigued. Admit it. Why did you answer the ad?

LARRY: I don’t have a job.

CAPTAIN: You quit McDonald’s.

LARRY: No.

CAPTAIN: Then they fired you!

LARRY: Yes.

CAPTAIN: McDonald’s fired you? What a loser . . . No . . . It was meant to be. That’s why you’re here.

LARRY: Let me go. You don’t need me. A tough guy like you can handle this job on your own. I’m worthless. I would only get in the way.

CAPTAIN: Nonsense, Horatio. You see, every superhero needs a sidekick to share in the pure joy of his manly virtues.

LARRY: Couldn’t your Mother do that?

CAPTAIN: Of course not. In order for our duo to work at its most effective level, it is essential they share a common bond. The kind of bond only a man can experience with another man. Say you’ll bond with me and glory will be yours. History will record us as the two heroes in bondage together. Don’t be afraid of chance. Try it . . . You like doing nothing, don’t you. It’s your life. Letting time slip away. Just slip away . . .

LARRY: How dare you say that about me. Look at you. You’re a fake. A fool. Your life is no better than mine. Look at this place you live in. It’s a dump. A dump.

CAPTAIN: You’re right. It’s a dump, but it’s my dump and everything in my dump has a purpose. I’m here because I choose to be here. You’ve never chosen anything in your life. You’re taking the easy way out.

LARRY: You’re the one who’s taking the easy way out.

CAPTAIN: Easy! You think it’s easy being a superhero? You think I like walking through brick walls? Don’t let this suit fool you. It’s no picnic, and no magic fairy endowed me with superpowers, either. It took hard work and determination. You should know what that is. You worked at McDonald’s.

LARRY: But don’t you see, I even failed at that.

CAPTAIN: Horatio. I know.

LARRY: What do you know?

CAPTAIN: I know what it’s like to be nothing. I was a failure too. I’ve spent most of my life feeling alone. Wishing I were dead, or just that I could be somebody else, anybody else. And when I thought there was no hope left, something happened. All at once I came alive.

I realized my whole life was a test. And at that moment, I began shaping the great man you see today. I got off my butt and started exercising. I built my body into the perfect machine and now I’m ready to save the world. Who’s the bravest in the land?

LARRY: CAPTAIN NEATO-MAN!

CAPTAIN: I know you think I’m crazy. Maybe I am, but for the first time in my life I’m happy, and I know you can’t say the same.

LARRY: But this stuff isn’t real.

CAPTAIN: Anything can be real. We create realities all the time. How can you cling so desperately to your truth without knowing what truth is.

LARRY: We could die.

CAPTAIN: Be a hero, Horatio. I need you.

LARRY: No, I’m Larry . . . Larry . . .

CAPTAIN: Let go, Horatio. We could go down in history. (he strikes his superhero pose and Larry wavers)

LARRY: (voice cracking) Horatio! My name is Horatio (Larry joins the Captain in a superhero pose)
```

---

## IC-1309: Albuquerque

- Title: Albuquerque
- Author (byline): “Weird Al” Yankovic
- Work: Weird Al: The Book by Nathan Rabin with Al Yankovic, Pgs 166-167
- Publisher: Scholastic
- Publication date as stated: Jan 2016
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1249
- Already set (do not supply): none

### Source block (context only)

```text
Author: “Weird Al” Yankovic
Book: Weird Al: The Book by Nathan Rabin with Al Yankovic, Pgs 166-167
ISBN: 978-1419722738
Publisher: Scholastic
Date (Month/Year): Jan 2016
```

### Introduction (context only: never use it for content warnings)

```text
by “Weird Al” Yankovic
```

### Performance text (classify this)

```text
(Pg 166-167) Way back when I was just a little bitty boy living in a box under the stairs in the corner of the basement of the house half a block down the street from Jerry's Bait shop You know the place well anyway, back then life was going swell and everything was just peachy

Except, of course, for the undeniable fact that every single morning My mother would make me a big bowl of sauerkraut for breakfast

A big bowl of sauerkraut Every single morning It was driving me crazy

I said to my mom . . . "Hey, mom, what's with all the sauerkraut?"
And my dear, sweet mother
She just looked at my like a cow looks at an oncoming train
And she leaned right down next to me
And she said "IT'S GOOD FOR YOU"

That's when I swore that someday
Someday I would get outta that basement and travel to a magical, faraway place
Where the sun is always shining and the air smells like warm root beer
And the towels are oh so fluffy
Where the Shriners and the lepers play their ukuleles all day long

Well, let me tell you, people, it wasn't long at all before my dream came true
Because the very next day, a local radio station had this contest
To see who could correctly guess the number of molecules in Leonard Nimoy's butt
I was off by three, but I still won the grand prize
That's right, a first-class one-way ticket to . . . Albuquerque!

You know, I'd never been on a real airplane before
And I gotta tell ya, it was really great
Except that the little kid in back of me kept throwin' up the whole time
The flight attendants ran out of Dr. Pepper and salted peanuts
And, oh yeah, three of the airplane engines burned out
And we went into a tailspin and crashed into a hillside
And the plane exploded in a giant fireball and everybody died
Except for me
You know why?

'Cause I had my tray table up
And my seat back in the full upright position
Had my tray table up
And my seat back in the full upright position

So I crawled from the twisted, burnin' wreckage
I crawled on my hands and knees for three full days
Draggin' along my big leather suitcase and my garment bag
And my tenor saxophone and my twelve-pound bowling ball
And my lucky, lucky autographed glow-in-the-dark snorkel
But finally I arrived at the world famous Albuquerque Holiday Inn
Where the towels are oh so fluffy
Well, I checked into my room and I turned down the A/C
And I'm just about to eat that little chocolate mint on my pillow
That I love so very, very much when suddenly, there's a knock on the door

Well now, who could that be?
I say "Who is it?"
No answer
"Who is it?"
They're not sayin' anything

So, finally I go over and I open the door and just as I suspected
It's some big fat *guy* with a Flock-Of-Seagulls haircut and only one nostril
So anyway, he bursts into my room and he grabs my lucky snorkel
And I'm like "Hey, you can't have that"
"That snorkel's been just like a snorkel to me"
And he's like "Tough"
And I'm like "Give it"
And he's like "Make me"
And I'm like "'Kay"
So I grabbed his leg and he grabbed my esophagus
And I bit off his ear and he chewed off my eyebrows
Yes indeed, you better believe it
And somehow in the middle of it all, the phone got knocked off the hook
And twenty seconds later, I heard a familiar voice
And you know what it said?
I'll tell you what it said

It said . . . "If you'd like to make a call, please hang up and try again" "If you need help, hang up and then dial your operator"

Well, to cut a long story short, he got away with my snorkel
But I made a solemn vow right then and there that I would not rest
I would not sleep for an instant until the one-nostrilled man was brought to justice
But first, I decided to buy some donuts

So I got in my car and I drove over to the donuts shop
And I walked on up to the guy behind the counter
And he says "Yeah, what do ya want?"
I said "You got any glazed donuts?"
He said "No, we're outta glazed donuts"
I said "Well, you got any jelly donuts?"
He said "No, we're outta jelly donuts"
I said "You got any cinnamon rolls?"
He said "No, we're outta cinnamon rolls"
I said "Well, in that case - in that case, what do you have?"
He says "All I got right now is this box of one dozen starving, crazed weasels"
I said "OK, I'll take that"

So he hands me the box and I open up the lid and the weasels jump out And they immediately latch onto my face and start bitin' me all over

(rabid gnawing sounds)
Oh man, they were just going nuts
They were tearin' me apart
Oh, oh God, oh God
Oh, get 'em off me

(more screaming)

I ran out into the street with these flesh-eating weasels all over my face
Wavin' my arms all around and just runnin', runnin', runnin'
And as luck would have it, that's exactly when I ran into the girl of my dreams
Her name was Zelda
She was a calligraphy enthusiast with a slight overbite and hair the color of strained peaches
I'll never forget the first thing she said to me
She said "Hey, you've got weasels on your face"

That's when I knew it was true love
We were inseparable after that
We ate together, we bathed together
We even shared the same piece of mint-flavored dental floss
The world was our burrito
So we got married and we bought us a house
And had two beautiful children - Nathaniel and Superfly
Oh, we were so very very very happy

But then one fateful night, Zelda said to me
She said "Sweetie pumpkin? Do you wanna join the Columbia Record Club?"
I said "Woah, hold on now, baby"
"I'm just not ready for that kinda commitment"
So we broke up and I never saw her again
But that's just the way things go . . . In Albuquerque

Anyway, things really started lookin' up for me
Because about a week later, I finally achieved my lifelong dream
That's right, I got me a part-time job at The Sizzler
I even made employee of the month after I put that grease fire out with my face
Aw yeah, everybody was pretty jealous of me after that
I was gettin' a lot of attitude

Anyway I, I know it's kinda been a roundabout way of saying it
But I guess the whole point I'm tryin' to make here is . . . I! HATE! SAUERKRAUT!
That's all I'm really tryin' to say
And, by the way, if one day you happen to wake up
And find yourself in an existential quandary
Full of loathing and self-doubt
And wracked with the pain and isolation of your pitiful meaningless existence
At least you can take a small bit of comfort in knowing that
Somewhere out there in this crazy ol' mixed-up universe of ours
There's still a little place called . . . Albuquerque

I said "A" - "L" -"B" - "U" - "querque" Albuquerque
```

---

## IC-1310: Alexander and the Terrible, Horrible, No Good, Very Bad Day

- Title: Alexander and the Terrible, Horrible, No Good, Very Bad Day
- Author (byline): Judith Viorst
- Work: Not specified
- Publisher: Atheneum Books
- Publication date as stated: June 1972
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: ALEXANDER
- Teaser before the introduction: No
- Spoken words (computed): 744
- Already set (do not supply): none

### Source block (context only)

```text
Author: Judith Viorst
ISBN: 0689300727
Publisher: Atheneum Books
Date(Month/Year): June 1972
```

### Introduction (context only: never use it for content warnings)

```text
Ever had one of those days or a day when lots of “THOSE DAYS” gang up on your all at onece? Alexander is only 8, but today, he’s faced a barrage of bummers worthy of a country- western song: getting smushed in the middle seat of the car, a dessert-less lunch sack, a cavity at the dentist's office, stripe-less sneakers, witnessing kissing on television, and being forced to sleep in railroad-train pajamas. When it comes right down to it . . . it’s all in your perspective.

Alexander and the Terrible, Horrible, No Good, Very Bad Day by Judith Viorst.
```

### Performance text (classify this)

```text
ALEXANDER: I went to sleep with gum in my mouth and now there’s gum in my hair and when I got out of bed this morning I tripped on the skateboard and by mistake I dropped my sweater in the sink while the water was running and I could tell it was going to be a terrible, horrible, no good, very bad day.

At breakfast Anthony found a Corvette Sting Ray car kit in his breakfast cereal box and Nick found a Junior Undercover Agent code ring in his breakfast cereal box but in my breakfast cereal box all I found was breakfast cereal. I think I’ll move to Australia.

In the carpool, Mrs. Gibson let Becky have a seat by the window. Audrey and Elliott got seats by the window too. I said I was being scrunched. I said I was being smushed. I said, if I don’t get a seat by the window, I am going to be car sick. No one even answered. I could tell it was going to be a terrible, horrible, no good, very bad day.

At school Mrs. Dickens liked Paul’s picture of the sailboat better than my picture of the invisible castle. At singing time, she said I sang too loud. At counting time, she said I left out sixteen. Who needs sixteen? I could tell it was going to be a terrible, horrible, no good, very bad day.

I could tell because Paul said I wasn’t his best friend anymore. He said that Phillip Parker was his best friend, and that Albert Moyo was his next best friend and that I was only his third best friend. I hope you sit on a tack, I said to Paul. I hope the next time you get a double-decker strawberry ice cream cone the ice cream part falls off the cone part and lands in Australia.

There were two cupcakes in Phillip Parker’s lunch bag and Albert got a Hershey bar with almonds and Paul’s mother gave him a piece of jelly roll that had little coconut sprinkles on the top. Guess whose mother forgot to put in dessert? It was a terrible, horrible, no good, very bad day.

That’s what it was, because after school, my mom took us all to the dentist and Dr. Fields found a cavity just in me. “Come back next week and I’ll fix it,” said Dr. Fields. “Next week,” I said, “I’m going to Australia.”

On the way downstairs the elevator door closed on my foot and while we were waiting for my mom to go get the car, Anthony made me fall where it was muddy and then when I started crying because of the mud, Nick said I was a crybaby and while I was punching Nick for saying “crybaby,” my mom came back with the car and scolded me for being muddy and fighting. I am having a terrible, horrible, no good, very bad day.

I told everybody. No one even answered. So then we went to the shoe store to buy some sneakers. Anthony chose white ones with blue stripes. Nick chose red ones with white stripes. I chose blue ones with red stripes, but the man said, “We’re all sold out.” They made me buy plain old white ones, but they can’t make me wear them.

When we picked up my dad at his office, he said I couldn’t play with his copying machine, but I forgot. He also said to watch out for his books on his desk and I was careful as could be except for my elbow. He also said don’t fool around with his phone, but I think I called Australia. My dad said please don’t pick him up anymore. It was a terrible, horrible, no good, very bad day.

There were lima beans for dinner, and I hate limas. There was kissing on TV, and I hate kissing. My bath was too hot, I got soap in my eyes, my marble went down the drain, and I had to wear my railroad-train pajamas. I hate my railroad-train pajamas. When I went to bed, Nick took back the pillow he said I could keep, and the Mickey Mouse night-light burned out and I bit my tongue. The cat wants to sleep with Anthony, not with me. It has been a terrible, horrible, no good, very bad day.

My mom says some days are like that even in Australia.
```

---

## IC-1311: All About Al

- Title: All About Al
- Author (byline): Cherie Vogelstein
- Work: The Best American Short Plays 1998-99
- Publisher: CreateSpace Independent Publishing Platform
- Publication date as stated: May 2001
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: LENNY, GIL
- Teaser before the introduction: Yes
- Spoken words (computed): 2205
- Already set (do not supply): none

### Source block (context only)

```text
Author: Cherie Vogelstein
Book: The Best American Short Plays 1998-99
ISBN: 978-1557834256
Publisher: CreateSpace Independent Publishing Platform
Date (Month/Year): May 2001
```

### Introduction (context only: never use it for content warnings)

```text
All About Al by Cherie Vogelstein
```

### Performance text (classify this)

```text
GIL, very handsome and cool, sits with his back to us in an empty coffee shop, reads the sports section. LENNY, downtrodden and uncool, enters in raincoat and galoshes, furtively looks around, spots GIL, quickly looks away, orders coffee. Nonchalantly, LENNY takes cup and saunters by GIL's table. Suddenly, he stops, pretends to notice GIL for first time. Their initial conversation should be slightly awkward: the way it is when casual friends meet after not speaking for awhile: full of sound and excitement, signifying nothing.

LENNY: Gil! [Practically spills cup.]

GIL: [Looks up, friendly.] Hey... Lenny!

LENNY: What a surprise, what a coincidence!

GIL: Yehah - how ya doin', buddy?

LENNY: How are you? You look great!

GIL: Yeah? Well I'm doin' okay, you know, hangin' in there. [Awkward pause, then with some concern.] . . . how uh . . . how are YOU doin', Len?

LENNY: [Jovially.] Me? Well, I'm fine . . . alright, you know . . . not so good - [Totally serious.] - suicidal - I'm suicidal, Gil.

GIL: [Sympathetic.] Yeah, heard about you and Cindy. I'm sorry, man, we shoulda called.

LENNY: No, no I should've called you guys . . . it's just I've been so preoccupied, you know, with death, I haven't had any time. [Cheery.] So how's Allison?

GIL: Allison? She's real good . . . yeah, she should be comin' here

LENNY: [Excited.] Really?!

GIL: Yeah.

LENNY: Here? Really? [GIL nods.] That's great, that is so great!

GIL: [Puzzled by LENNY's enthusiasm.] Yeah . . . any minute.

LENNY: [Elated.] I - I can't wait to see her, I mean what good luck . . . that is so fantastic, just terrific . . . incredible really. . .

GIL: [Beat.] You're not gettin' out much, are ya, Len?

LENNY: [Instantly sad, sits, cradles his head.] It's hopeless, Gil. I'm miserable, a wreck; all alone during allergy season with my hair falling out and my gums big and bleeding - may I join you?

GIL: [Looks around uncomfortably.] Uh

LENNY: - I mean you don't know how lucky you are - wow to have a woman like Allison, kind, darling, beautiful Al

GIL: - I think we're breakin' up.

LENNY: [Shocked.] What?

GIL: [Beat.] Yeah.

LENNY: [Devastated beat.] No.

GIL: Yeah.

LENNY: [2 Beats.] No.

GIL: [Annoyed.] LENNY!

LENNY: I'm sorry but I . . . can't believe it . . . I mean I just can't believe it - you and Allison, Allison and you . . . you're like Romeo and Juliet. . . Antony and Cleopatra . . . Lawrence Olivier and Danny Kaye

GIL: Well, listen . . . I'm just tellin' ya cuz maybe, you know, it's not such a good idea for you to be around when I tell her

LENNY: Why, Gil? I'll be very quiet

GIL: Right but uh . . . even though it's a cafe deal and I'm hopin' she'll keep the cryin' down to a minimum . . . I'll tell ya, Len, things might get pretty wacky - I mean, it's not easy breakin' a girl's heart. . . ya know?

LENNY: No . . . I don't know. . . I've dreamt about it ... [Assumes the mannerisms of a girl]

GIL: Yeah, well so anyway. . . I think that's what I'm gonna do. [Pause.] Oh! [Laughs.] No offense, Len but you make a real ugly girl.

LENNY: [Sticking to his role, falsetto.] Did you want to speak to me about something?

GIL: O.K., O.K. yeah . . . [Serious.] . . . I did . . . listen, Al, I haveta tell you something

LENNY: [Coquettishly.] I love you, Gilly

GIL: Yeah, I love you too. It's over. We have to break up.

LENNY: What?! Why?!

GIL: Why? [Thinks.] Honestly? Because . . . I have a brain tumor

LENNY: [Falsetto] Oh my God! You do?

GIL: No, no, no - seriously? We have to break up because . . . I'm not good enough for you, Al, I think you deserve better

LENNY: [Falsetto.] I do but I don't want better, I want you, YOU [Almost to himself] - moronic, greasy

GIL: [Oblivious.] Yeah, but the thing is . . . I don't think I can measure up to this . . . this IMAGE you have of me, ya know? I mean, sure we might be good today, we might be good tomorrow but ultimately, I don't have what it takes to fulfill a woman like you. And one day, one day I'm gonna look into your eyes and I'm gonna see - insteada the love - I'm gonna see somethin' else - I'm gonna see all the respect drained out and gone with only the hate left. And that's gonna break my heart, Al- [Sobs.]

LENNY: [As himself] Wow. Is that true?

GIL: No but it sounded good, right? [Beat.] I mean, you can't tell her the real stuff. . . Well it's no big deal really, just this thing she does sometimes when . . . when we're lyin' there . . . ya know, in bed . . . and I'll be gettin' all comfortable, I'll be startin' to doze off - and allofa sudden, outta nowhere, I'll feel this leg swingin' over on top of me, right over my body while I'm tryin' to sleep.

LENNY: Is it her leg?

GIL: Of course, it's her leg that's not the point - the point is while I'm tryin' to sleep, I don't need some weight pinnin' me down to the mattress, you know what I mean?

LENNY: Cindy bought a bunk bed when I moved in

GIL: I mean, I'm not sayin' I don't appreciate Al's affection - I'm not saying that at all - but there's a time and a place and [when I’m trying to sleep] . . . I do NOT like to be touched, ya know?

LENNY: Cindy said [all touching] should be kept to a minimum.

GIL: Listen, Len, can I just say? - she did you the biggest favor in the world when she dumped you

LENNY: I know, I know. That's the one favor women always want to do for me - [With sudden emotion.] - which is why I'm telling you it's lonely in New York, Gil- Allison is special-

GIL: Yeah, I know she's special but . . . but . . . it's not just the leg thing, Lenny. . . it's more than that. . .

LENNY: You mean like a leg/arm kind of thing?

GIL: I mean like. . . like - [Thinks of something.] -like the way she's so obsessed with her weight! I mean, all she ever does is ask me about it all the time: Like I won't have seen her for a day and I'll pick her up and first thing when she opens the door, she'll say, "Hi, Gil, do I look like I gained weight?"

LENNY: So?

GIL: So I'll say - No, Al, you look great - and she'll say – are you sure? - and I'll say - positive - and she'll say - no you're lying -and I'll say - why would I lie? - to make me feel good - no, no way - yes, I see it in your eyes - no, that's my contact lens Al, ya haven't gained an ounce since the day you were born - you promise? - I swear - you'd tell me if I did - of course - you promise you would tell me? – I promise - you promise you promise - I promise, I swear, I swear on my life now give me a stake to put through my head cuz I can't take it anymore, Lenny, it drives me nuts!

LENNY: Why? [GIL rolls his eyes in frustration.] You mean because she's a little insecure about her figure . . . needs a little reassurance, a little positive assessment of her weight?

GIL: Yeah, but like . . . why doesn't she just invest inna scale? Ya know what I mean? Why's it havta be such a big mystery all the time?

LENNY: Gil, Gil, YOU'RE her scale, Gil, YOU

GIL: But that's the thing - to me she looks great-so what's she so worried about?

LENNY: [Shrugging.] Maybe she's afraid if she got fat, you'd break up with her.

GIL: [Softens.] Well, yeah . . . I would - but that doesn't mean she has to like "dwell," ya know? [Guiltily.] I mean, come on, Len every guy wants his girlfriend to have a nice body, right?

LENNY: [Nodding.] Cindy gained 60 pounds while we were together.

GIL: God, I know - how'd you deal with that, man?

LENNY: I loved her for what was inside

GIL: Deep, deep inside

LENNY: [Impassioned.] Look, a good woman is hard to find

GIL: Cindy's not hard to find - [Spreads his arms wide.] [Looks around, then at his watch.] I wonder why Al's so late.

LENNY: Cindy was always late, Cindy

GIL: Cindy, Cindy, will you forget Cindy!

LENNY: It just ended last week, Gil.

GIL: Yeah, well get over it already, alright? Get over it!

LENNY: [Repeats to himself.] Get over it.

GIL: -what you need is somebody nice, somebody sweet, a girl who gives ya support, makes ya feel good, really LIKES you

LENNY: [Like a kid at a toy store.] They have that?

GIL: Yeah, yeah, ya just gotta give yourself a break, buddy, ya know what I mean? Ya gotta ... go for it, ya know? [Beat.] Just go for it! [Pause.]

LENNY: Gil?

GIL: Yeah, Len?

LENNY: When uh when Allison gets here. . .

GIL: Yeah?

LENNY: When Allison gets here . . .

GIL: [Very calm.] Finish the sentence, Len.

LENNY: Can I . . . have her?

GIL: What?

LENNY: Well not "have her," "have her" is a silly expression but you know what I mean - could I ask her out - would you mind?

GIL: Would I mind? If you asked Allison out? [Beat.] My Allison, right? You mean Allison Kramer.

LENNY: Listen, if it's a problem

GIL: No, it's no problem

LENNY: - then I won't

GIL: Lenny. I said it's not a problem, okay?

LENNY: Okay. [Beat, smiling broadly, happily.] Thanks, Gilly.

GIL: Don't call me Gilly, alright? [Beat, scowling.] But I'm just thinkin' ...

LENNY: [Serious.] Uh-huh, good, O.K.

GIL: Ya know . . . what about "Cindy?"

LENNY: Oh. Well you said to forget her.

GIL: And that's it? That's all it takes - I say forget her and you're done?

LENNY: Well, Gil, I thought you gave me some very excellent advice and so I'm trying to follow up on it, is all

GIL: Yeah, well, okay . . . good. But I haveta tell ya, Len, maybe this is sicka me an' all, but it kinda does bother me, ya know? [Annoyed and confused.] I mean you askin' Allison out! I mean cuz like . . . here you are, and and like . . . the body's still warm, ya know what I'm sayin'?

LENNY: Yes but in a way, isn't that better? [Smiles broadly.] I mean, that way she won't have time to mourn over the loss of you because I'll be right there to console her

GIL: [Getting angrier.] Yeah but what I'm sayin' is I don't really want you there to console her

LENNY: But . . . Why, Gil? I mean, do you want to see her suffer?

GIL: Not at all. But I even more don't want to see her with you

LENNY: But that's not very fair, is it? I mean, here you don't want her anymore

GIL: I never said I didn't "WANT" her, Lenny

LENNY: Well, you said you were breaking up

GIL: I said I was thinkin' of breaking up - that the little, dancin' thought had walked my mind! But I mean I didn't realize that automatically gave YOU the green light to pounce? [Rises, angry.] All your concern for the what, why, why were you just, ya know, circlin' the area till you could swoop down -like some little galosh-wearin' vulture

LENNY: [Backing away.] That's not a very flattering characterization, Gil

GIL: - and . . . and what? just feast on my leftovers?! - and . . . and I mean Allison, no less - Allison of all girls - don't you know how outta your league Allison is?

LENNY: Yes of course, but - but you said to go for it!

GIL: It. IT. Not HER, you [jerk]!

LENNY: [Summoning up his courage.] But why not? [Rises.] Why not her?

GIL: Because . . . because

LENNY: [Hitting his stride.] Because what, Gil, HUH?! All my life I've watched the Leonards of this world lose the Allisons of this world to the Gils of this world and the Gils don't even care! [He throws saucer against wall.] I'm sick of it, I tell you! I'm sick, sick, sick! It's men like you who destroy women for the rest of us; abusing and demeaning and rejecting them till they so totally lose their sense of selves they actually believe the REAL men are the men who treat them that way -- when in fact you're not real at all, you're just scared, scared of growing up, scared of yourself, scared that - just like you said in that speech - that one day you're gonna look into her eyes and see the hate because deep down you believe once Allison sees you, once she really sees Gilly for who he is, she'll see THERE'S NOTHING TO SEE!

GIL: Yeah? [Rises.] Well- [Trying to find the right words] –Shut up, Lenny! Shut up! [Screams, grabs his collar.] SHUT UP! [Silence, GIL lets go.]

LENNY: I think I've offended you Gil- [Sits.] -I'm sorry

GIL: No, don't be sorry, don't be sorry - who wants your sorry, Lenny? Allison's a GIFT, a PRIZE - who loves me! And so that's a VERY scary thing [Lenny covers his face.] - I mean, it's alotta pressure - alotta - who wants to deal with dissappointin' a girl like that, ya know? ! We're not talkin' some whale beast like Cindy - we're talkin' Allison Kramer! And so even if a part athat - if part awhat you said fear - whatever you said - even if it's something involved with that. . . so what? I mean - what does that prove? That I'm no good? Because I'm - I'm human? That I may be scared of rejection deep down? Alright! So what, ya know? Deep down everybody's scared of rejection! Everybody!

LENNY: [Puffing up his chest.] I'm not!

GIL: Yeah? Well that's just cuz you're so used to it

LENNY: Damn straight! Damn straight I am! [Rises, speaks quietly.] Take a look at a real man, Gil- a man who's not afraid of rejection, of intimacy, of commitment, the dark - well okay I am a little afraid of the dark - but I'm not afraid of love! Love I embrace unguarded - and I love Allison! I want her, Gil!

GIL: [Also rises.] Yeah, well so do I!
```

---

## IC-1312: Alvin Ho: Allergic to Girls . . .

- Title: Alvin Ho: Allergic to Girls . . .
- Author (byline): Lenore Look
- Work: Not specified
- Publisher: Yearling
- Publication date as stated: May 2009
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: ALVIN, DAD, ALIVN, MISS P, FLEA, ELI, PINKY, JULES
- Teaser before the introduction: Yes
- Spoken words (computed): 2197
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lenore Look
ISBN: 978-0375849305
Publisher: Yearling
Date (Month/Year): May 2009
```

### Introduction (context only: never use it for content warnings)

```text
Alvin Ho: Allergic to Girls, Schools and Other Scary Things by Lenore Look.
```

### Performance text (classify this)

```text
ALVIN: (enters rooms shyly . . . already in character) (almost whispering at the beginning but gradually growing louder after his list of fears) The first thing you should know about me is that my name is Alvin Ho. I am afraid of many things. Elevators. Tunnels. Bridges. Airplanes. Thunder. Substitute teachers. Kimchi. Wasabi. The dark. Heights. Scary movies. Scary dreams. Shots. School. If there were no school, my troubles would blast away, just like that. I would dig holes all day. I would watch cooking shows. I would keep an eye on things. It would be fantastic!

ALVIN: The second thing you should know about me is that I have a dog named Lucy and a brother named Calvin and a sister named Anibelly, who messes with my sticks and toys; eats my food, drinks my chocolate milk and gets in my way. I am not as big as Calvin, but I am bigger than Anibelly, who isn't a baby anymore but doesn't go to school yet. I am sort of nearly almost medium . . . when I stand on tiptoe and stretch at the same time, I am finally almost visible in my class picture!

The third thing you should know about me is that I love Plastic Man, Wonder Woman, the Green Lantern, Concrete Man, Aquaman, King Henry V and all the superheroes in the world. I know them from reading with my dad every night while my mom runs on the treadmill like a hamster on a wheel. My dad is a great reader for his age, which could be fifty or one hundred, it's hard to tell. He wears reading glasses and always puts one arm around me and his other arm around Anibelly and Calvin for support, on account of when you get to be that old, it is hard to do anything by yourself

The fourth thing you should know about me is that once upon a time, before I went to school, I was a superhero. I was Firecracker Man! I ran around our house, full speed ahead, screaming at the top of my lungs while beating on a garbage can lid. I was as noisy as a firecracker on Chinese New Year! But now I am Firecracker Man only on weekends and holidays. There's just no time for it. Being a superhero is hard work. You have to save the world. But going to school is even harder. You have to save yourself. Most days I can hardly even make it to the school bus. And when I arrive at school, I can't think. I can't read. I can't smile. I can't sing. I can't scream. I can't even talk.

The fifth thing you should know about me is that I have never spoken a word in school. Even when I try with all my might, I always manage to say nothing at all. My voice works at home. It works in the car. It even works on the school bus. But as soon as I get to school I am as silent as a side of beef. It is true. No one really knows why I lose my voice at school, since I come from a long line of farmer-warriors who haven't had a scaredy bone in their bodies since 714 AD. In China my ancient grandpas and grandmas and aunts and uncles fought off leopards and tigers in their gardens the way Calvin and Anibelly and I fight off mosquitoes at Walden Pond. They weren't afraid of anything. I am afraid of everything.

DAD: When I was your age . . . I was scared of school too. Worse, I was never a superhero before I went to school, so it was very rough.

ALVIN: My dad is not superhero material, but he has read practically everything ever written about superheroes and so knows us from beginning to end, which explains a lot about him.

DAD: Just hold your head high and be a gentleman.

ALVIN: But I feel sick. (to audience) My dad put a hand on my forehead.

DAD: No fever.

ALIVN: Are you sure? (to audience) I looked at his hands. They are thick like baseball mitts. It was a wonder he could feel anything through them.

DAD: Where does it hurt?

ALVIN: All over. (to audience) It was true; I was not making it up. I gave a little moan.

(moans pitifully)

DAD: Hmmmmm (Alvin moans again even more pitifully) You are not sick.

ALVIN: But I will be. I will be very, very sick. I'm allergic to school, severely allergic."

DAD: Alvin. (coming down to Alvin’s level and putting one of his mitts on Alvin’s shoulder) You will be okay, son.

ALVIN: I love it when he calls me that. Son. I felt a little better. Maybe my dad was right, maybe I would be okay. A good word from my dad changes everything. Besides, if I missed the bus, my dad might have a few other words for me. So I dashed out of the house and caught up with Calvin just as the bus was pulling up to the end of our driveway. We waved and climbed on. I was okay. "You will be okay, son," my dad's voice echoed between my ears. I smiled at Calvin. And Calvin smiled back. I was okay.

Then we arrived at school. My sneakers landed like a couple of cement blocks when I got off the bus. Pfuump, pfuump. My stomach turned like a washing machine when I got inside. I found the door that said "Second Grade, Miss Pestalozzi." My throat tightened.

MISS P: Welcome. I'm Miss P.

ALVIN: I stopped dead in my tracks. Her hair was shiny and her skin was clean. She smelled like fresh laundry out of the dryer. She smiled at me. But I did not smile back. I hardly even looked at her. I felt dizzy. Everything whirled around me. I was in the middle of it, but I was not in it at all. So far, second grade wasn't any different from first grade, which wasn't any different from kindergarten. I was thinking about running and hiding, when ...

FLEA: Wanna be desk buddies again?

ALVIN: It was Flea. She was my desk buddy in first grade. She is ·a girl. I wanted to say no way. Nobody wants a girl desk buddy, except for maybe a girl. The scary thing about girls is that they are not boys. They can't punch. But they can kick, which hurts. They skip rope too fast. They are boring. I opened my mouth to tell her all this, but . . . My tongue turned into sandpaper. Nothing came out.

FLEA: C'mon. You can sit with me and Esha.

ALVIN: Everyone was choosing their seat and sitting down. Soon it would be too late to sit with the boys. I opened my mouth. I wished for my voice. I wished and wished and wished. But nothing came out. Finally, I slumped into the chair. I was not okay. I was so allergic to school, but I was even more allergic to girls!

TRANSITION So Alvin began to concoct a plan . . . Obviously moaning and claiming to be sick didn’t work. His dad was too smart to fall for just pretending to be sick. The best way to avoid school, as everyone knows is to really, truly get sick!!

ALVIN: But not all sicknesses are created equal. Some are better than others. Tonsillitis, for example, is pretty good. You get all the Italian ice you want. It is my dream to have tonsillitis someday. Appendicitis is good too, but not as good as a burst appendix, which gets you a ride in a wailing ambulance speeding through all the red lights on Route 62 to Emerson Hospital. This happened when Calvin's appendix burst and our mom found him on the kitchen floor. He has all the luck!

The flu is okay, but it's not great. You only get ginger ale and crackers, which is a real rip-off, but usually you get to watch all the cooking shows and cartoons you want. The common cold? One bad-tasting zinc drop, some tissues and you're back in school the next day.

Medical mysteries? If you get foreign-accent syndrome or barking madness or squeaky chalk phobia, forget it. You're back in school the same day. So you have to be patient. It's like choosing a car, or a house; my mom says you shouldn't jump at the first offer because a better deal might be right around the corner.

And it was. One day, Jules was out-with chicken pox.

MISS P: Don't go near Jules's house. It'll take two weeks for all the blisters to scab over completely. Until then, Jules 1s highly contagious.

ALVIN: Highly contagious? I felt like dancing! I nearly burst like fireworks! But I didn't. I had to wait until after school. It was hard not to go near Jules's house. It is on the way to everything. It is as though Jules's house is a big magnet and I am an iron filing, and every time I so much as step out of my house, I am yanked toward it, just like that. That was exactly what happened! I was sucked by such a powerful force toward Jules's house that I could barely even pick up the fat frog in the gutter on my way. And when I got to Jules's house, there was already a line behind the tall bushes in front, just like the line at the cinema when there's a scary movie playing. (to the kids in line) Hey, guys!

ELI: (hiding in the bushes) Shhhhhhhh! Stay low or Jules's mom will see us and we'll all get sent home.

ALVIN: Before I knew it, it was my turn. I caught my frog, rushed around the side of the house and ran right into Pinky under Jules's window.

PINKY: Watch where you're going! (holding out a coffee can)

ALVIN: He held out a can. On the can was a label: One-minute visit: 50¢ Jump into bed· $1

PINKY: You got a dollar?

ALVIN: I gasped. Normally, Pinky does not speak to me. Usually I do not show up on his radar, not one bleep, not even a flicker. But I was flickering now! (shaking his head no)

PINKY: You got fifty cents?

ALVIN: No. (to Pinky) Wait! (to audience) I remember[ed] an unchewed piece of gum in my back pocket. I took it out. It was warm and soft. Pinky grabbed the gum, unwrapped it and stuffed it into his cheek.

PINKY: (speaking around the wad of gum) Okay. You get a minute.

ALVIN: I took my frog and hopped through Jules's window. Jules was in bed. (to Jules as he look around the room and under the bed) So where's the chicken?

JULES: I was wondering that myself. I wish I knew.

ALVIN: I was really disappointed. How do you catch chicken pox without first catching a chicken? (To Jules) I came to catch the chicken pox. Not the plain pox. (to audience) But the plain pox wasn't too shabby. It had turned Jules's head into a potato covered with red eyes. Some eyes were crying, others were crusty like sugar on a cookie. It was great! Jules had never looked scarier!

Jules was scratching like crazy. I do not know if Jules is a girl or a boy. Sometimes Jules plays with the boys, and other times Jules plays with the girls.

“Jules" could stand for "Julian'' or it could stand for "Julia." It is hard to tell. The blisters didn't help either. In fact, they made Jules look like neither boy nor girl. Instead, Jules looked a good deal like an alien. A real live alien potato fresh off a UFO. (to Jules) You're so lucky! I'd love to look like that.

JULES: (scratching like crazy) Yeah, It's really great except for the itching.

ALVIN: You got any you can't reach?

JULES: (squirming) Yeah, right up the middle of my back.

ALVIN: So I gave Jules a hand. I think it is one of the rules of being a gentleman, but I don't really know, I can't remember.

PINKY: Time's up! (hissing from the window)

ALVIN: [But] None of us caught a chicken or even saw one. So none of us broke out with the chicken pox that day. Or the plain pox either. It was a terrible disappointment.

Then a long time later . . . just when we'd forgotten all about Jules and the chicken pox, and none of us were trying to catch anything anymore . . . a miracle happened. Our art teacher, Mr. Gruenert, was showing us famous self-portraits one warm afternoon. Frida Kahlo looked a little itchy to me with branches coming out of her hair. Paul Gauguin looked a bit feverish because he was in Tahiti, where it's really hot. And Vincent van Gogh, in his scratchy straw hat, definitely looked itchy. . . . Very itchy.

Then we got mirrors and brushes so that we could paint our own self-portraits. My self-portrait was going to be a masterpiece, but strangely . . . I didn't feel like painting. I didn't feel like doing anything at all. I felt strange.

Then I looked into the mirror. Something scary stared back. (screaming)

Aaaaaaaaaaaaaaaaaaaaaaack! Then Flea, who was next to me, looked at me.

FLEA: Aaaaaaaaaaieeeeeeeeee!"

ALVIN: The other girls screamed too. Some ran fast. Others ran faster. You'd think we were a bunch of aliens or something. School shut down for two weeks and a half after that. There was a story about us in the newspaper so that people as far away as Andover, Massachusetts, read about the great chicken pox epidemic in Concord. We were famous! The newspaper said ... The first victim had been carefully quarantined. All the children had been warned to keep away. How the epidemic ever got started was a complete mystery. (Alvin smiles proudly and knowningly and raises his hands in the air in victory)

[The sixth thing you should know about me is that my name is Alvin Ho and I caught the chicken pox!!]
```

---

## IC-1313: American Born Chinese

- Title: American Born Chinese
- Author (byline): Gene Luen Yan
- Work: Not specified
- Publisher: First Second
- Publication date as stated: Sep 2006
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: MELANIE, DANNY, DANNY’S MOM, CHIN-KEE, TEACHER 1, TEACHER 2, TEACHER 3, TEACHER 4, TEACHER 5, STEVE
- Teaser before the introduction: Yes
- Spoken words (computed): 1233
- Already set (do not supply): none

### Source block (context only)

```text
Author: Gene Luen Yang
ISBN: 978-1596431522
Publisher: First Second
Date (Month/Year): Sep 2006
```

### Introduction (context only: never use it for content warnings)

```text
Warning . . . . this selection contains extreme negative stereo-types of Asian Americans – but sometimes the best way to confront these stereotypes is through humor. In fact, according to the author, Gene Luen Yan, who IS an Asian American, approaching this stereo-type head-on may, in fact, begin to bring us closer together. In a recent interview he said: “I hope that a kid who has never felt part of the majority, a kid who has always felt like an outsider, will understand, regardless of what it is that makes them an outsider, that that is not an experience that’s unique to them. Actually, more of us feel like outsiders than insiders”

So don’t be afraid to laugh, but in the back of your mind, mull around the overly stereo-typed character of Chin-Kee. American Born Chinese by Gene Luen Yan
```

### Performance text (classify this)

```text
(Scene: Danny’s kitchen table)

MELANIE: Van der Waals forces of attraction are stronger when more of WHAT are present?

DANNY: Mmm . . .

MELANIE: Danny, you’re drooling.

DANNY: What? Oh! Well, I – that happens when I’m really concentrating on your – I mean – CHEMISTRY.

MELANIE: Will you please stop fooling around? If we don’t get this attraction stuff down by tomorrow --

DANNY: You know, Melanie, since we’re on the topic of attraction, I’ve been meaning to talk to you about something…

MELANIE: (blushing) I’ve actually been hoping –

DANNY’S MOM: Danny!

DANNY: (Sigh) Hold that thought. Yeah, Ma?!

DANNY’S MOM: I have some exciting news! Guess who’s coming to visit?

DANNY: Who?

DANNY’S MOM: Your cousin Chin-Kee!

DANNY: (Danny drops textbook and looks terrified)

DANNY’S MOM: I knew you’d be excited! Your father went to go pick him up at the airport! He should be here any minute now!

MELANIE: Danny, who’s cousin Chin-Kee?

CHIN-KEE: (Chin-Kee barrels into room) Harro Amellica! Cousin Da-Nee! Rong time no see! Chin-Kee happy as GINGER ROOT pranted in nutritious manure of WELL-BRED OX!

DANNY: (whispers, in horror) Hi Chin-Kee.

CHIN-KEE: (Chin-Kee notices Melanie) WHA--?! Confucious say, “Hubba-Hubba!” Such pletty Amellican girl wiff bountiful Amellican bosom! Must bind feet and bear Chin-Kee’s children! (Chin-Kee notices Danny’s angry reaction) Oh no! Chin-Kee so vely solly! Dis pletty Amellican girl wiff bountiful Amellican bosom must berongs to cousin Da-Nee! Perhaps Chin-Kee can find pletty Amellican girl for hisself when he attend Amellican school tomollow wiff cousin Da-Nee!

DANNY: Ma?!

DANNY’S MOM: Oh you two are going to have so much FUN together!

(Scene: Oliphant High School, the first period bell is already ringing)

CHIN-KEE: Why cousin Da-Nee bling Chin-Kee to school so rate? Other student already in crass!

DANNY: Just hurry up. And stay QUIET!

CHIN-KEE: AH-SO! What big, bootiful Amellican school! Chin-Kee Rike! CHIN-KEE RIKE VELY MUCH!

(Scene: Government classroom)

TEACHER 1: Come on people! LOOK ALIVE! Didn’t ANY of you do the assigned reading last night?! Let’s try this one more time. The three branches of the American government are . . .

CHIN-KEE: OHH OHH! Chin-Kee know dis one!

DANNY: Put your hand DOWN!

TEACHER 1: Go ahead . . . Ah, Chin-Kee, was it?

CHIN-KEE: Judicial, executive and regisrative!

TEACHER 1: Good Chin-Kee! Very good! You know people – it would behoove you all to be a little more like Chin-Kee.

CHIN-KEE: See, cousin Da-nee? Chin-Kee tol’ you! Chin-Kee know!

(Scene: History classroom)

TEACHER 2: The Nina, the Pinta and the –

CHIN-KEE: --Santa Malia!

(Scene: Science classroom)

TEACHER 3: The ulna is connected to the –

CHIN-KEE: --Humelus!

(Scene: Math classroom)

TEACHER 4: R squared is greater than six R—

CHIN-KEE: L is less than or equal to zero or L is greater than or equal to six.

(Scene: Spanish classroom)

TEACHER 5: En esta historia, el perro de jose es –

CHIN-KEE: --Branco y muy glande!

(Scene: Cafeteria)

CHIN-KEE: Would cousin Da-nee rike to tly Chin-Kee’s Clispy flied cat gizzards wiff noodle?

DANNY: Leave me alone.

STEVE: Dan the man!

DANNY: Steve!

STEVE: Hey, props on making the legendary Oliphant High Varsity basketball team, kid!

DANNY: Come on, now. We both knew it was inevitable.

STEVE: Well, being as how you’re a transfer from Hughes Academy, I’d say it was anything BUT inevitable. What were you scrubs called again? The “water lilies?”

DANNY: Oh, PLEASE. I’ve got a jump-shot that’ll make you cry like a little sissy girl.

STEVE: Ha, ha, we’ll see about that at practice today, kid. So, ah…you hangin’ with a new crowd?

DANNY: NO! This is my cousin Chin-Kee.

CHIN-KEE: Harro!

DANNY: He’s just visiting.

STEVE: So how long you in town for, Chin-Kee…

DANNY: Hey, you… you happen to have an extra copy of the game schedule?

STEVE: Why? Gimme a sec… Ah! There you go. That’ll be $100, plus a date with your fly girlfriend. Oh, wait… you don’t have a fly girlfriend!

DANNY: Ha ha. Thanks, man.

STEVE: You gonna be at practice today?

DANNY: How else am I gonna make you cry like a little sissy girl?

STEVE: (laughs) See you then, kid.

DANNY: All right.

CHIN-KEE: Hee-hee-hee HA HA HA HA HA HA HA HA!

DANNY: What’s your problem?!

CHIN-KEE: Me Chinese, me play joke! Me go pee-pee in his Coke!

STEVE: BLARF! What the heck’s wrong with my Coke?!

(Scene: Cafeteria)

DANNY: Listen, Melanie, I’m sooo sorry about all that stuff my cousin said –

MELANIE: No. I shouldn’t have left in a huff like that last night. It wasn’t your fault. I mean, in some ways, it’s kind of flattering.

DANNY: So, does that mean you’d be up for catching a movie with me on Saturday?

MELANIE: …I actually wanted to talk to you about that, Danny. We’re good friends, and I really LIKE being friends. I don’t want to do anything to mess that up.

DANNY: I’m not like him, Melanie. I’m nothing like him! I don’t even know how we’re related!

MELANIE: Calm down, Danny! Geez! This isn’t about that, okay? It’s about us being friends, and me not wanting to jeopardize that!

DANNY: Whatever.

MELANIE: I’ll see you around okay?

STEVE: Hate to tell you this kid, but practice ended twenty minutes ago.

DANNY: I know. I had detention.

STEVE: Too bad. You missed the three-pointer of the century – made by yours truly, of course. You all right, Danny?

DANNY: Can I tell you something, Steve?

STEVE: Sure, man. What’s up?

DANNY: You know how I transferred from Hughes Academy at the beginning of the year? Well, the year before that I transferred from Rohmer High.

STEVE: How come?

DANNY: I’m only a junior and I’ve already been to three different schools. (Sigh) Every year around this time, I finally start getting the hang of things, you know? I’ve made some friends, gotten a handle on my schoolwork, even started talking to some of the ladies. I finally start coming into my own. Then he comes along for one of his visits.

STEVE: Who?

DANNY: Chin-Kee. My cousin. He’s been visiting me once a year since the eighth grade. He comes for a week or two and follows me to school, talking his stupid talk and eating his stupid food. Embarrassing the crap out of me. By the time he leaves, no one thinks of me as Danny anymore. I’m Chin-Kee’s cousin. It gets so bad by the end of the school year that I have to switch schools.

STEVE: Come on, kid. It ain’t gonna go down like that here.

DANNY: How do you know?

STEVE: People here aren’t like that. No one ever says anything about my weight. Well, maybe that’s because I broke Todd Sharpnack’s nose for calling me “Mr. Jiggles” when we were freshmen. But, whatever. People here are different. You’ll see. Heck, if anyone ever gives you troubles, I’ll break his nose.

DANNY: You’re probably right. Thanks, Steve.

STEVE: Come on, kid. I’ll buy you a Coke.

DANNY: A Coke? What, so I can pee in it?

STEVE: That’s what happened to my Coke? He peed in it? BLAAAARGFFF!

(Scene: Library)

CHIN-KEE: (Singing) Talk to me, terr me yo’ name! You brow me off rike it’s all da same! You rit a fuse, I am ticking away rike a bomb! Yeah baby! She bang! She bang! Yeah baby! She move! She move! I go clazy! ‘Cause she rook rike frower but she sting rike bee! Rike evely girl in histoly! She bang! She bang!... (Sees Danny) WHA? --?! Ah-so! Harro! Cousin Da-nee finarry come! Riblaly boling, so Chin- Kee entertain ferrow patlons wiff rivery song! Cousin Da-nee just in time for second set!

DANNY: I’m sick of you running my life, Chin-Kee! I want you to pack up and go back to where you came from!

CHIN-KEE: Ha! Ha! No, cousin Da-nee! Chin-Kee visit not over yet. Chin-Kee no reave until visit over!

DANNY: Go away!

CHIN-KEE: Chin-Kee stay.

DANNY: (Smack)

CHIN-KEE: Cousin Da-nee, prease! No understand—

DANNY: (Smack)

CHIN-KEE: Prease! No more!

DANNY: (Smack)

CHIN-KEE: Cousin Da-Nee no risten, now must suffer unmitigated fully of spicy Szechuan Dragon! WA-TA! Sirry Cousin Da-nee. Chin-Kee ruv Amellica. Chin-Kee rive for Amellica. Chin-Kee come visit evely year. Forever. Forever!
```

---

## IC-1314: Angela’s Ashes

- Title: Angela’s Ashes
- Author (byline): Frank McCourt
- Work: Not specified
- Publisher: Scribner
- Publication date as stated: May 1999
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: FRANK, PRIEST, GRANDMOTHER, GRANDMA, GRANDMOTER, MOTHER, MIKEY
- Teaser before the introduction: Yes
- Spoken words (computed): 1366
- Already set (do not supply): none

### Source block (context only)

```text
Author: Frank McCourt
ISBN: 978-0684842677
Publisher: Scribner
Date (Month/Year): May 1999
```

### Introduction (context only: never use it for content warnings)

```text
Crossed-eyed Mikey Molloy is eleven years old. He knows about the female body and “Dirty Things in General.” Mikey tells Frank a story of Irish mythology about the great Cuchulain’s wife, Emer, who was the “champion woman pisser of Ireland.” Uh – oh – And thus begins the story of Frank McCourt’s first confession and communion.

Angela’s Ashes by Frank McCourt.
```

### Performance text (classify this)

```text
FRANK: It’s my turn. The confession box is dark and there’s a big crucifix hanging over my head. I can hear a boy mumbling his confession on the other side. I wonder if there’s any use trying to talk to the Angel on the Seventh Step. I know he’s not supposed to be hanging around confession boxes but I feel the light in my head and the voice is telling me, Fear not. The panel slides back before my face . . . (to Priest) Bless me, Father, for I have sinned. This is my First Confession.

PRIEST: Yes, my child, and what sins have you committed?

FRANK: I told a lie. I hit my brother. I took a penny from my mother’s purse. I said a curse. . . I, I listened to a story about Cuchulain and Emer.

PRIEST: Surely that’s not a sin, my child. After all we are assured by certain writers that Cuchulain turned Catholic in his last moments.

FRANK: ‘Tis about Emer, Father, and how she married him. (whispering) She won him in a pissing contest. (to audience) There is heavy breathing. The priest has his hand over his mouth and he’s making choking sounds and talking to himself, Mother o’ God.

PRIEST: (trying to control is laughter) Who, who told you that story, my child?

FRANK: Mikey Molloy. He read it in a book, Father.

PRIEST: For your penance say three Hail Mary’s, and three Our Fathers.

FRANK: Father, was that the worst sin? Am I the worst of all the boys, Father?

PRIEST: No, you have a long way to go. God bless you, my child.

FRANK: First Communion Day is the happiest day of your life because of The Collection and James Cagney at the Lyric Cinema. The night before I was so excited, I couldn’t sleep till dawn. I’d still be sleeping if my grandmother hadn’t come banging at the door.

GRANDMOTHER: (knocking at the door) Get up! Get up! Get that child outa the bed! Happiest day of his life an’ him snorin’.

FRANK: I ran to the kitchen. I took off [my] shirt and she pushed me into a tin tub of icy cold water. They dressed me in my black velvet First Communion suit with the white frilly shirt, the short pants, the white stockings, the black patent leather shoes.

GRANDMOTHER: Come here till I comb your hair. Look at that mop, it won’t lie down. (she spits on his head to control the hair) You didn’t get that hair from my side of the family. That’s that North of Ireland hair you got from your father. That’s the kind of hair you see on Presbyterians. If your mother had married a proper decent Limerickman you wouldn’t have this standing up, North of Ireland, Presbyterian hair. (she spits on his head again)

FRANK: Grandma, will you please stop spitting on my head.

GRANDMA: If you have something to say, shut up. A little spit won’t kill you. Come on, we’ll be late for the Mass.

FRANK: We ran to the church. My mother panted along behind with Michael in her arms. We arrived at the church just in time to see the last of the boys leaving the altar rail where the priest stood with the chalice and the host. (Priest assumes glaring stance) (Frank opens his mouth to receive communion and speaks with his mouth full) Then he placed on my tongue the wafer, the body and blood of Jesus. At last, at last! (look of surprise as the wafter sticks) It stuck! I had God glued to the roof of my mouth! I could hear the master’s voice:

PRIEST: Don’t let the host touch your teeth for if you bite God in two you’ll roast in hell for eternity.

FRANK: I tried to get God down with my tongue (tries to dislodge the wafer)

PRIEST: (hissing) Stop that clucking and get back to your seat.

FRANK: God was good. He melted and I swallowed Him and now, at last, I was a member of the True Church, an official sinner.

When the Mass ended, there they were at the door of the church, my mother and my grandmother. They each hugged me and told me it was the happiest day of my life. They cried all over my head and after my grandmother’s contribution that morning my head was a swamp. (to Mom) Mam, can I go now and make The Collection?

GRANDMOTER: No. You’re not making no collection till you’ve had a proper First Communion breakfast at my house. Come on.

FRANK: We followed her. She banged pots and rattled pans and complained that the whole world expected her to be at their beck and call. I ate the egg, I ate the sausage, and when I reached for more sugar for my tea . . .

GRANDMOTHER: (slapping his hand) Go aisy with that sugar. Is it a millionaire you think I am? An American? Is it bedecked in glitterin’ jewelry you think I am? Smothered in fancy furs?

FRANK: The food churned in my stomach. I gagged. I ran to her backyard and (he throws up). Out she came.

GRANDMOTHER: Look at what he did. Thrun up his First Communion breakfast. Thrun up the body and blood of Jesus. I have God in me backyard. What am I goin’ to do? (thinking) I’ll take him to the Jesuits!

FRANK: She dragged me through the streets of Limerick. She told the neighbors and passing strangers about God in her backyard. She pushed me into the confession box. (to the Priest) In the name of the Father, the Son, the Holy Ghost. Bless me, Father, for I have sinned. It’s a day since my last confession.

PRIEST: A day? And what sins have you committed in a day, my child?

FRANK: I overslept. I nearly missed my First Communion. My grandmother said I have standing up, North of Ireland, Presbyterian hair. I threw up my First Communion breakfast. Now Grandma says she has God in her backyard and what should she do?

PRIEST: (struggling to control his laughter) Ah … ah … tell your grandmother to wash God away with a little water and for your penance say one Hail Mary and one Our Father. God bless you, my child.

FRANK: Grandma and Mam were waiting close to the confession box.

GRANDMOTHER: Were you telling jokes to that priest in the confession box? (gives him a slap on the back of the head) If ’tis a thing I ever find out you were telling jokes to Jesuits I’ll tear the bloody kidneys outa you. Now what did he say about God in me backyard?

FRANK: He said wash Him away with a little water, Grandma.

GRANDMOTHER: (thinking) Holy water or ordinary water?

FRANK: He didn’t say, Grandma.

GRANDMOTHER: Well, go back and ask him. (pushing him back into the confessional)

FRANK: Bless me, Father, for I have sinned, it’s a minute since my last confession.

PRIEST: A minute! What is it now?

FRANK: (embarrassed) My grandma says, Holy water or ordinary water?

PRIEST: Ordinary water, and tell your grandmother not to be bothering me again.

FRANK: (exiting the confessional) Ordinary water, Grandma, and he said don’t be bothering him again.

GRANDMOTHER: Don’t be bothering him again! That bloody ignorant bogtrotter!

FRANK: Can I go now and make The Collection? I want to see James Cagney.

GRANDMOTHER: You can forget about The Collection and James Cagney because you’re not a proper Catholic the way you left God on the ground. Come on, go home.

MOTHER: Wait a minute. That’s my son. That’s my son on his First Communion Day. He’s going to see James Cagney.

GRANDMOTHER: (throwing her hands up) Take him then to James Cagney and see if that will save his Presbyterian North of Ireland American soul. Go ahead. (she exits in disgust)

FRANK: We met Mikey Molloy on Barrington Street. He asked if I was going to the Lyric and I said I was trying.

MIKEY: Trying? You don’t have money? That’s all right. I’ll get you in. I’ll create a diversion.

FRANK: What’s a diversion?

MIKEY: I have the money to go and when I get in, I’ll pretend to have the fit and the ticket man will be out of his mind and you can slip in when I let out the big scream. (demonstrates the scream) I’ll be watching the door and when I see you in, I’ll have a miraculous recovery. That’s a diversion. That’s what I do to get my brothers in all the time.

MOTHER: Oh, I don’t know about that, Mikey. Wouldn’t that be a sin and surely you wouldn’t want Frank to commit a sin on his First Communion Day.

FRANK: Mikey said if there was a sin it would be on his soul, and he wasn’t a proper Catholic anyway so it didn’t matter. He let out his scream and I slipped in. The ticket man was so worried over Mikey he never noticed! (triumphant grin that turns to horror as he realizes he has sinned again. He arrives at church the next day and enters the confessional)

(to the Priest) In the name of the Father, the Son, the Holy Ghost. Bless me, Father, for I have sinned. It’s a day since my last confession.
```

---

## IC-1315: Animals

- Title: Animals
- Author (byline): Simon Rich
- Work: Spoiled Brats, Pg 1-18
- Publisher: Little, Brown and Company
- Publication date as stated: Oct 2014
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: PRINCESS JASMINE, HAILEY, MS. HUDSON, SIMON, ALYSSA, PRINCIPAL DAVENPORT, SIMON’S MOTHER, CARLOS, GIRL 1, GIRL 2, GIRL 3
- Teaser before the introduction: Yes
- Spoken words (computed): 1427
- Already set (do not supply): none

### Source block (context only)

```text
Author: Simon Rich
Book: Spoiled Brats, Pg 1-18
ISBN: 978-0316368629
Publisher: Little, Brown and Company
Date (Month/Year): Oct 2014
```

### Introduction (context only: never use it for content warnings)

```text
By the time Simon Rich graduated from Harvard he had a two-book deal from Random House. He also spent four years writing for Saturday Night Live (the youngest writer SNL ever hired) and about two years at Pixar and is now at work on a film and a television series. His stories eccentric, universally hilarious and often built on an unusual premise, or told from a surprising angle. This tale takes a looks at a typical week in a 2nd grade classroom of a elite private school . . . but the twist? Our narrator is a widowed hamster named . . . (wait for it) PRINCESS JASMINE!

Animals by Simon Rich
```

### Performance text (classify this)

```text
PRINCESS JASMINE: (Pg 1-18) They buried my wife in a shoebox in Central Park. I like to imagine that the service was respectful, that her body was treated with a modicum of dignity. But of course, I’ll never know. I wasn’t invited to her funeral. Instead, the guests of honor were the students of homeroom 2K . . . Her killers.

Hailey, I noticed, was crying. The irony. It was her responsibility to refill our water bottle last week. Instead, she spent all her free time with Alyssa, practicing a clapping game called “Miss Mary Mack.”

HAILEY: (with enthusiasm) Miss Mary Mack, Mack, Mack! All dressed in black, black, black!

PRINCESS JASMINE: It was that inane chant that provided the score to my wife’s final moments. . . Pocahontas was her name.

PRINCESS JASMINE: My name is Princess Jasmine. I am a male, so this name is humiliating, but I’m aware that my situation could be worse. The other homeroom, 2R, has a guinea pig named Homer Simpson and an elderly turtle named New Kids on the Block. Pocahontas left me with three sons, and it’s for their sake alone that I keep up my struggle. Their names are Big Mac, Whopper, and Mr. T. It’s morning now. The square of sunlight on the blackboard grows and grows. Soon the gremlins will run in howling, hopped up on Pop-Tarts and primed for violence. It turns out this school is a private one, an “elite” institution for the children of millionaires. I can hear the nannies muscling their way through the lobby, dragging their little terrors toward my family. The bell clangs harshly. The nightmare has begun. Monday

MS. HUDSON: What time is it?

SIMON: Jobs time!

PRINCESS JASMINE: My fur bristles as Ms. Hudson takes out the Jobs Board. This laminated poster, with its seventeen colorful squares, rules my family’s existence. It determines everything: whether we feast or starve, live or die. I rub my paws impatiently while Ms. Hudson assigns the week’s tasks. . . Pencil organizer . . . . Table Wipers . . . Eventually, she gets to the one job that matters.

MS. HUDSON: Hamster feeder is…

PRINCESS JASMINE: I scan the room. There are still some good candidates left. Maybe we’ll get lucky and end up with Caitlin? Last time she gave us double portions. It’s while I’m enjoying this fantasy that Ms. Hudson clears her throat and—with one little word—sentences my family to death.

MS. HUDSON: …Simon.

PRINCESS JASMINE: My eyes widen with horror.

SIMON: (shouting) Hamster feeder? Whatchu talkin’ ’bout Willis!

PRINCESS JASMINE: The other children laugh hysterically. My God, I think. This is it. This is how it ends.

PRINCESS JASMINE: 11:25 am . . . I sigh with relief as Simon finally walks over to our cage. He doesn’t feed us, though, or replenish our water. Instead, he picks me up by my tail, which is connected directly to my spine. He swings me through the air drops me back into my cage. My sons poke their heads through the newspaper. They look around confusedly, then stare at me in dismay. They’re used to receiving food at this hour, but I have none to give. Simon has forgotten to do his one basic task. Our long, slow death march has started.

Tuesday

PRINCESS JASMINE: I awake to the sound of screeching laughter. Sophie and Alyssa have made a dress out of pink construction paper and taped it to my sleeping body.

ALYSSA: You’re a pretty girl, Princess Jasmine! A pretty, pretty girl!

PRINCESS JASMINE: I try to remove the costume, but the tape is double-sided and my paws are too weak to detach it. I must wear this “dress” indefinitely, in the presence of my own sons. I avoid their eyes, and they avoid mine. Whatever dignity I had is long gone. I can feel myself on the verge of becoming insane. When the final school bell rings. Carlos, the janitor walks from table to table, cleaning up after the beasts. The Jobs Board is a total farce, I think, as he sponges up their filth. Kristen and Sophie are table wipers in name only. At the end of the day, every job on the board belongs to Carlos. When Carlos sees us, he curses under his breath. I avert my eyes with shame. Our cage is full of feces. I know we’re not responsible for the condition of our prison, but it’s hard not to feel mortified. I look on with pity as the janitor collects our soiled newspaper. He refills our water bottle, and, for the first time in days, I allow myself to feel hope. Before he can find our feedbag, though, Principal Davenport has run into the room.

PRINCIPAL DAVENPORT: Carlos, there you are! A kindergartener [soiled] himself in dance. Would you please take care of it?

PRINCESS JASMINE: Carlos forces another smile and reaches for his mop. Wednesday

PRINCESS JASMINE: The water tastes so rich it brings tears to my eyes. As I drink it, I can feel it coursing through my body, giving my parched veins life. I look over at my sons, asleep in their clean cage, their wet little noses twitching with contentment. Carlos has saved our lives. But for how long? Mercifully, the children are gone this morning. They’ve been given a break from their arduous studies to enjoy a “field day” at Randall’s Island. The classroom is blissfully quiet until lunchtime, when the hobgoblins return. Their red faces are streaked with grime and sweat. The smell is almost unendurable. Every child has somehow won an athletic trophy.

SIMON: (Raising his golden prize over his head, he shouts) Boom shaka laka!

PRINCESS JASMINE: When he walks by my cage, I peak at the engraving on his trophy. “Participation,” it reads. I wonder if Simon is aware that his trophy has no meaning, that all he participated in was a mass delusion?

MS. HUDSON: Great job, everybody. That was some great teamwork today. Don’t forget to do your jobs!

PRINCESS JASMINE: Simon doesn’t even look in our direction. This makes three straight days without food. It’s official: we are going to starve to death. Thursday

PRINCESS JASMINE: As the sun rises on another hellish day, I gather my sons around me. I’ve rehearsed my speech all night, but it’s still hard to utter it. Eventually, with painful effort, I manage to force the terrible words through my lips. “If Simon forgets to feed us one more time… I want the three of you to eat my body.” Mr. T breaks down and weeps. But Big Mac and Whopper merely nod. They know it’s the only solution we have left. I can hear Simon’s voice before he even enters the classroom, as piercing and abrasive as a siren.

SIMON: Whatchu talkin’ ’bout Willis! (As he presses his face against the bars of the hamster cage, he chants again and again) Whatchu talkin’ ’bout! Whatchu talkin’ ’bout! Whatchu talkin’ ’bout!

PRINCESS JASMINE: His noxious Dorito breath engulfs me and I can feel the fury mounting in my chest. I think of the sound of my son weeping and the look my wife gave me as she drew her final breath. I have only a little strength left. But it’s enough to rise up and sink my teeth into the monster’s flesh. Friday

PRINCESS JASMINE: Our cage has been moved to the principal’s office,

PRINCIPAL DAVENPORT: Words can’t express how sorry I am! Safety is our top priority—I’m as appalled as you are that something like this could occur at our school.

SIMON’S MOTHER: He had to get three stitches! The plastic surgeons say that the scar could be visible for months!

PRINCESS JASMINE: I roll my eyes as Simon’s mother starts to cry.

SIMON’S MOTHER: He’s just a little boy. And you let him be exposed to wild animals! I’m considering pressing charges. My lawyer says I have a real case. Simon had to take a rabies test, and when the nurse pricked his thumb, he cried and cried. The doctor said he’d never seen a boy cry like that.

PRINCESS JASMINE: I smile proudly, thinking of this scene. [Then] Simon’s mother turns toward our cage, her eyes narrowing with rage.

SIMON’S MOTHER: I want those animals out of the classroom . . . I want them destroyed.

PRINCIPAL DAVENPORT: (clearing his throat) Of course. (He picks up a phone and calls for a janitor)

PRINCESS JASMINE: Carlos arrives within seconds, mop in hand . . . . I can smell the Dumpster before I see it, an overflowing bin of putrid trash. My nose twitches painfully as I process all the stenches: decomposing Dunkaroos and mold-encrusted Pop-Tarts; rancid, soggy Lunchables and spoiled Nesquik. The monsters have accumulated so much waste this week, and now we’re to be added to the pile.

CARLOS: (whispering) Sorry, little guys. (He scans the alley to make sure no children are watching, then tucks the cage under his arm and runs) Saturday

PRINCESS JASMINE: I awake to the sight of three girl humans, gobbling pancakes and chatting rapidly.

GIRL 1: What do we name the babies?

GIRL 2: Snap, Crackle, and Pop!

GIRL 3: The mommy should be Mrs. Fluffy, or Mrs. Furry, or…

CARLOS: (interrupting) It’s not a mommy. It’s a daddy. And we’re going to call him Hercules.

GIRL 1: (laughing) Hercules! Why?

CARLOS: (Crouching down and looking into Hercules’ eyes) Because he’s tough. And strong. And he works long hours, even though it’s a living nightmare. (There is a sense he is talking about himself too)

GIRL 2: (looking around nervously, she whispers) O.K. We’ll call him Hercules.
```

---

## IC-1316: Anxiety with Tic Tacs From Drums, Girls and Dangerous Pie

- Title: Anxiety with Tic Tacs From Drums, Girls and Dangerous Pie
- Author (byline): Jordan Sonnenblick
- Work: Drums, Girls and Dangerous Pie
- Publisher: DayBue Publishing
- Publication date as stated: May 2004
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2238
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jordan Sonnenblick
Book: Drums, Girls and Dangerous Pie
ISBN: 096689409X
Publisher: DayBue Publishing
Date (Month/Year): May 2004
```

### Introduction (context only: never use it for content warnings)

```text
In this excerpt from Drums, Girls and Dangerous Pie . . . Steven relates the difficulty he has on a day that will always hold significance in his life. A day much like any other . . . a day when he was supposed to be watching his younger brother Jeffrey and making him breakfast . But accidents do happen and this particular morning Jeffrey had climbed up on a stool to watch the breakfast making activities. A slip, a fall, a rush of blood. It all happened so quickly. And as Steven was sent off to school, his mother took Jeffrey to the hospital just to make sure everything was OK. Anxiety with Tic Tacs by Jordan Sonnenblick.
```

### Performance text (classify this)

```text
I don't know about any of you, but when I'm nervous about something, I tend to think about it all day, unless I come up with a complicated mental trick to distract me. And even then, I'm still actually thinking about the thing by NOT thinking about it, if that makes any sense. It's like, if someone came up to you and said, "All right, now whatever you do, DON'T think of the color red." You'd try to picture a different color, or repeat a recipe over and over in your head, or count to a hundred and fifty-nine, but somewhere in the back of your mind, you'd be going, "Yellow. . . orange. . . red. . . DOH! Three eggs, separated. . . five slices American Cheese. . . red. . . DANG! One hundred seventeen. . . one hundred eighteen. . . look at Renee's red lipstick. . . ARGHH!"

And that's how my October 7th went. I worked mightily to think about anything other than Jeffrey's gushing nose, but the distractions were truly pointless. In homeroom, after I figured out that my breath was going to present a challenge, I looked in the pocket of my Trapper Keeper for my box of Tic Tacs, and found that it was about three-quarters full. I quickly popped in a Tic Tac (orange, which I'm not even sure helps your breath anyway), and ran off to first period -Miss Palma's class. I did all the usual take-out-your - notebook stuff, but then became lost in my own little "Don't Think About Jeffrey" world.

I used a trick that is pretty powerful for me; I came up with a really complex math problem to solve in my head:

"A boy has a box of forty Tic Tacs, and the box is three quarters full. The Tic Tacs need to last through an entire school day and a bus ride home. The school day has seven periods. Each period is forty-four minutes long, with three minutes for passing between classes. Additionally, there is a twenty-two minute lunch period, and a four-minute after-noon homeroom period. The bus ride takes fifteen minutes, including the wait for the bus, boarding, and the actual time-in-transit. If the boy wants to make his Tic Tacs last until he arrives at home, how many minutes must he wait between Tic Tacs?"

So while everybody else was writing whatever the day's journal was supposed to be, I was agonizing over the details of this math problem: "OK, there are HOW many three minute passing times? Seven, not counting the one before lunch. So eight. Eight times three is twenty-four. Plus the time in class, which is forty-four minutes times seven. . . ummm . . . OK, that's three hundred and eight minutes right there. And lunch is another twenty-two minutes, plus the bus is, like fifteen minutes. . . WAIT! Do I have to eat Tic Tacs during class? Who cares about my breath when I'm alone at my desk? But there IS group work in some. . ."

Steven! Would you like to read your journal entry aloud?

No, thank you, Miss Palma.

Steven, I know I phrased that as a question, but it was really a command.

Yes, but mine….well, it’s private.

PRIVATE, Steven? (Again with the capital letters!)

Yes, private.

Through my haze of math and memory, I gradually noticed that the class was cracking up.

Steven, I respect privacy but how private can your thoughts on this subject BE?

Well. . . I . . .

As it turns out, the topic was, "Should Foreign Languages Be Taught in Middle School?"

Things like that happened all day. After math, just as I popped in my seventh Tic Tac, Renee Albert said to me, Steven, you are, like, out of, it today. Are you recovering from some kind of traumatic head injury, or somethinq?

Well, sort of.

Are you sort of remembering or faking some sort of an injury?

Both. I fell off a stool this morning and. . .

Oh, sorry, Stephen. I have to go talk to Jenna and Steph. Wait upl

While Renee was attractively speed-walking away, Annette suddenly appeared next to me. It wasn't the first time I noticed this - how Renee kind of swished around in a cloud of perfume, and Annette just popped up like some spastic hand-puppet.

Stephen, I heard about Jeffery, what happened? Annette sometimes watches Jeffrey on weekends.

Well, his, head hit the counter in the kitchen, and it started bleeding.

A lot?

Yeah. My mom is going to the hospital with him. They went to the emergency room. And now I’m going to be in trouble but I didn’t even do …

Is he okay? I bet he’s really scared!

I don't know.

And the bell rang, which meant I'd be late to social studies, and Annette would be late to science. While Annette ran away down the empty hall it suddenly hit me that I hadn't even thought about how Jeffrey was feeling about this. And I didn't really want to think too hard about it, because I knew he'd be terrified. Plus, now I had to go get a late pass, which probably meant I'd get a detention. So Jeffrey was getting me in trouble again, as usual.

The high point of my day was my drum lesson. We have this thing called "Opportunity Period," or "O.P." It's the last period of the day, and if you don't owe work in any of your classes, or need tutoring, or have detention, you get to do fun stuff. Most of the kids like to go to gym during O.P. -the track, the weight room, and the pool are all open, and you can play basketball or volleyball, too. But some go to art or choir. And, of course, every chance I get, I go to the band room. A few times a week. I used to get individual lessons on the drum set with the band teacher, Mr. Watras, during O.P. On this particular day, Mr. W. got called to the office for something, so I had about fifteen minutes to just play drums, with nobody else around. I started out with some simple beats. When my hands and feet started to loosen up, I switched over to this really complicated Latin rhythm I'd been working on. It took a lot of concentration to keep all four limbs moving independently of each other, which was perfect. It meant I wasn't thinking about Jeffery's fall, or late passes, or even Renee Albert. I was just playing.

After keeping the beat going for five minutes or so, I burst into a big solo. I always think of it that way: "Here comes Steven, bursting into his Big Solo. Watch those hands-they're too quick to follow. Holy cow, this kid is a magician!" Like there's a Monday Night Football commentator standing over my left shoulder. Anyway, I really was flying. I started with both hands doing a kind of shuffled march on the snare drum, pretty quietly. As I gradually got louder, I started flicking little quick shots at the high toms. Then I threw in some big "bombs" with my bass drum foot. Soon, I had an incredibly fast paradiddle going between my left hand and my right foot, while my left foot was keeping time on the high-hat cymbals and my right hand was going back and forth between the ride cymbal and the floor tom.

The door opened, and I opened my eyes and looked up (I never open my eyes when I'm practicing by myself-my private teacher always used to say if you don't know where the drums are, you're probably playing the wrong instrument). Mr. W was back. Behind him, I could see a few kids I didn't know-probably sixth graders on their way somewhere -looking in. They started clapping when I looked their way, which was pretty cool. I hadn't been showing off on purpose, but I can't say I minded the applause. I stood up and took a quick bow for them. Mr. W. smiled and complimented me on my "showmanship." That's yet another cool thing about music: if you show off in sports you're a "hot dog," if you show off in class, you're a "brainiac," but if you show off in drumming, people love it.

Mr. W. told me that my Latin rhythm was sounding a little stiff, and put on a CD for me to listen to. It was this old jazz album by Dizzy Gillespie.

This should help you out. It's by a cat named Dizzy. Yes, he said "cat." Music teachers have their own lingo.

Dizzy Gillespie, the trumpet player, right? My grandfather once told me about him.

The tune’s called “Cubano Be, Cubano Bop.”

When the tune came on, I couldn't believe it. There were probably about five drummers on the track, and they were going crazy! The conga drum player was especially wild, playing insane fill-ins all over the place. At the same time, the trumpets were blasting like a herd of elephants, with Dizzy's horn flying high above everything else. Then, just when it seemed there couldn't possibly be any way to get more energy into the music, everyone stopped playing except the conga guy, and a man's voice started chanting in what sounded like Spanish. The chant got faster and faster, the congas got louder and louder, a whole chorus of men came in, shouting "Cubano be, Cubano bop" over and over, and the horns all roared back to life. Then, with one last explosion from the conga player, the song was over.

Could you feel that, Pez?

Mr. W. is the conductor of the All-City High School Jazz Band, which is how I got in. He knew that the nickname "Peasant" bugged me, so one day he started calling me "Pez" for short, which was much better.

Could I feel it? That’s just the coolest thing I’ve ever heard in my life!

Good. I hope that later in the month you can get that conga part down.

What do you mean?

Well, I’ve decided that the spring concert is going to be all Latin and this song is going to be the finale! Would you like to play conga on it?

Of course, I was dying to play that part, but Mr. W is one of those rare teachers who can actually take a joke.

Oh I don’t know Mr. W, I was really hoping to play cowbell on it….or maybe…triangle?

Get out of here kid! You’re going to miss your bus!

I triumphantly popped my second-to-last Tic Tac into my mouth and strolled out of the room, whistling "Cubano Be, Cubano Bop."

My temporary good cheer lasted until I got on the bus. Renee Albert caught my eye (well, OK, she always catches my eye), and spoke:

How’s the brain injury?

Which brought me back to reality really, really fast. I kept going toward the back of the bus without saying anything to Renee, and sat down next to Annette. I had planned to tell her all about "Cubano Be, Cubano Bop," but now my mind was back on Jeffy.

I heard that Steven. It’s really cool that you were confident enough to just ignore her.

Ignore her? I didn’t ignore her, I was just too stupid to think of a comeback. And now I’m going to go home and find out what happened with my brother and how long I'LL be qrounded for making breakfast.

What?

Long story. When Jeffy fell this morning I was making him oatmeal. I had him up on the stool, and my mom thinks he shouldn’t be on there unless someone is like an inch and a half away. I thought I was being NICE by making him what he wanted while the rents were SLEEPING. I'm going to get maimed.

Well, your mom was right in a way.

What do you mean?

He DID fall, right?

Thanks Annette. Thanks a Lot. That’s exactly what I needed to hear right now. You’re a very inspiring person, you know that?

I was just trying to…

Trying to what? Show me what a horrible brother I am?

I didn't mean to make you. . .

Feel bad? Well, you did. I've been worrying about it all day!

By this point, we were pulling up to my stop. I got up to storm off the bus, but had to wait while Renee got her stuff together in the middle of the aisle. Plus, Renee took her time walking off, too, so I had to plod along behind her. It's hard to storm and shuffle at the same time, let me tell you.

When I got off the bus, I watched Renee walk - no, glide - away. Then I looked up at Annette as the bus started to move. Maybe it was the slanted fall sun glaring off the window, but it almost looked like she was crying. Great.

I let myself into my house and found my mom standing in the foyer, like she had been waiting for me. When I might be in trouble, I usually try to speak first, before the 'rents start in on me. So I plunged right in. Mom, I’ve been worried all day. Is Jeffrey okay? She said, in this strange, soft voice: Steven, your brother is really sick. Sick? Was it because he. ..? The fall this morning had nothing to do with it. Whew! I'm off the hook. But he's really. . .sick.

And this was the absolute worst thing about last October 7th, the one moment I’ll never forgive myself for. When my mother began to tell me that my baby brother had leukemia, my first feeling was relief.
```

---

## IC-1317: Arsenic and Old Lace

- Title: Arsenic and Old Lace
- Author (byline): Joseph Kesselring
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: June 1995
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: ABBY, MINISTER HARPER, TEDDY, MARTHA, MORTIMER, ROONEY, ELAINE, WITHERSPOON
- Teaser before the introduction: Yes
- Spoken words (computed): 1470
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joseph Kesselring
ISBN: 978-0822200659
Publisher: Dramatists Play Service
Date (Month/Year): June 1995
```

### Introduction (context only: never use it for content warnings)

```text
Martha and Abby; two elderly sisters. The epitome of grace, community service and decorum. After all they’ve cared for their delusional nephew Teddy for years now, and what is more commendable than that?

Enter Mortimer Brewster, another nephew, who uncovers the true extent of Martha and Abby’s community service -- helping lonely, unhappy men find peace with a little glass of elderberry wine.

Arsenic and Old Lace by Joseph Kesselring
```

### Performance text (classify this)

```text
ABBY: (Pg 6-7) My sister Martha and I have been talking about your sermon last Sunday. Living here next to the church all our lives, we’ve seen so many ministers come and go. [And now] with the war trouble, I’ve almost come to the conclusion that this Mr. Hitler isn’t a Christian.

MINISTER HARPER: I must admit, Miss Abby, that war and violence seem far removed from these surroundings.

ABBY: It is peaceful here, isn’t it?

MINISTER HARPER: Yes – peaceful. The gentle virtues that went out with candlelight and good manners.

TEDDY: (Pg 12) (Enters the room with sweeping strides) CHARGE! (blows his bugle) Charge the blockhouse!

ABBY: (Pg 7) Teddy, your brother Mortimer will be here a little later.

TEDDY: (baring his teeth in a broad grin) Dee-lighted! (exits with another bugle blow)

MINISTER HARPER: (Pg 12) Have you ever tried to persuade him that he wasn’t Teddy Roosevelt?

MARTHA: He’s so happy being Teddy . . .

ABBY: Once, a long time ago, we thought if he would be George Washington, it might be a change for him.

MARTHA: But he stayed under his bed for days and just wouldn’t be anybody.

ABBY: And we’d so much rather he’d be Mr. Roosevelt than nobody. (to Martha) Martha, dear, Dr. Harper has made all arrangements for Teddy to go to Happy Dale Sanitarium after we pass on (Pg 13) and arranged for Mr. Witherspoon.

MINISTER HARPER: He’s the Superintendent of Happy Dale . . .

ABBY: To drop in tomorrow to meet Teddy.

TEDDY: (racing into the room again) That’s bully! Just bully!

MORTIMER: (Pg 15) (Mortimer Brewster enters) Hello, Aunt Martha, Aunt Abby (Air kisses)

TEDDY: (Pg 18) Hello, Mortimer!

MORTIMER: (gravely with a salute) How are you, Mr. President?

TEDDY: Bully; thank you. Just bully! What news have you brought me?

MORTIMER: Just this, Mr. President, the country is squarely behind you.

TEDDY: (beaming) Yes, I know. Isn't it wonderful? (beat) Well, good-bye. [I’m off to] Panama!

(He exits to cellar)

MARTHA: (Pg 41) We let him dig the Panama Canal in the cellar.

MORTIMER: (Pg 18) (knowingly) Panama's the cellar. (he crosses to the desk and looks through drawers as he speaks to the aunts) (Pg 20) By the way, I left one of the chapters of my book on Thoreau here. Now where could I have put that?

ABBY: (Pg 21) (turned away, arranging the afternoon’s tea service) I do hope the play tonight will be something you can enjoy for once. What’s the name of it?

MORTIMER: "Murder Will Out.'' (he continues searching as he speaks) When the curtain goes up the first thing you'll see will be a dead body! (he lifts the window-seat and sees a dead body; not believing it, he drops window-seat then throws it open and stares in. In a strained voice) Aunt Abby!?

ABBY: (at sideboard) Yes, dear?

MORTIMER: You were going to make plans for Teddy to go to that . . . sanitarium . . .Happy Dale?

ABBY: Yes, dear, it's all arranged. Dr. Harper was here today and brought the papers. Here they are. (He takes them from her)

MORTIMER: Teddy's got to go to Happy Dale now. Tonight!

MARTHA: (enters with table settings) There's no such hurry as that.

ABBY: (Pg 22-23) No. When Teddy starts working on the canal you can't get his mind on anything else.

MORTIMER: Right away, I tell you! Right away!

ABBY: (turning to Mortimer) Why, Mortimer, how can you say such a thing?

MORTIMER: (Trying to be calm) Listen, darlings, I'm sorry, but I've got some shocking news for you. You know we've humored Teddy because we thought he was harmless.

MARTHA: Why he is harmless!

MORTIMER: He was harmless. You've got to know sometime. It might as well be now, Teddy's killed a man! He has to be confined. (he points to window seat) There's a body in the window-seat!

ABBY: Yes, dear, we know.

MORTIMER: You know?

MARTHA: Of course, dear, but it has nothing to do with Teddy.

MORTIMER: But who is he?

ABBY: His name's Hoskins. Adam Hoskins. That's really all I know about him -- except he's a Methodist.

MORTIMER: Well, what's he doing here? What happened to him?

MARTHA: He died.

MORTIMER: Aunt Martha, men don't just get into window seats and die.

ABBY: [Silly boy] No, he died first.

MORTIMER: Well, how?

ABBY: Oh, Mortimer. The gentleman died because he drank some wine with poison in it.

MORTIMER: How did the poison get in the wine?

MARTHA: Well, we put it in wine because it's less noticeable. When it's in tea it has a distinct odor.

MORTIMER: You put it in the wine?

ABBY: Yes. And I put Mr. Hoskins in the window-seat because Dr. Harper was coming.

MORTIMER: So, you knew what you'd done! You didn't want Dr. Harper to see the body!

ABBY: Well, not at tea -- that wouldn't have been very nice. (Mortimer is speechless)

MARTHA: (Pg 24-25) Dear, stop being so excited.

ABBY: And for pity's sake stop worrying. We told you to forget the whole thing.

MORTIMER: Well, you can't leave him there.

MARTHA: We don't intend to, dear.

ABBY: No, Teddy's down in the cellar now digging.

MORTIMER: You're going to bury Mr. Hotchkiss in the cellar?

MARTHA: Yes, dear, that's what we did with the others.

MORTIMER: Others? More than one others?

MARTHA: Oh, yes, dear. Let me see, this is eleven. Isn't it, Abby?

ABBY: No, dear, this makes twelve. Well, anyway, they're all down in the cellar.

MORTIMER: (floored) Who was the first one?

ABBY: Mr. Midgely. He was a Baptist.

MARTHA: Of course, I still think we can't claim full credit for him because he just died.

ABBY: Martha means without any help from us. You see, Mr. Midgely came here looking for a room . . .

MARTHA: (Pg 26-27) He was such a lonely old man. . .

ABBY: All his kin were dead and it left him so forlorn and unhappy -- And then when his heart attack came -- and he sat dead in that chair (Pointing) looking so peaceful, we made up our minds then and there that if we could help other lonely old men to that same peace, we would!

MARTHA: (giggling)Teddy had been digging in Panama and he thought Mr. Midgely was a Yellow Fever victim.

ABBY: That meant he had to be buried immediately.

MARTHA: So, we all took him down to Panama and put him in the lock.

MORTIMER: And that's how all this started -- that man walking in here and dropping dead.

ABBY: Of course, we realized we couldn't depend on that happening again. So . . .

MARTHA: You remember those jars of poison that have been up on the shelves in Grandfather's laboratory? Well, dear, for a gallon of elderberry wine I take one teaspoonful of arsenic, then add a half teaspoonful of strychnine and then just a pinch of cyanide.

MORTIMER: Should have quite a kick.

ABBY: Yes! As a matter of fact, one of our gentlemen found time to say "How delicious!"

MORTIMER: (Pg 31) (sputtering) You can’t do things like that! It’s not only against the law. It’s wrong! It’s not a nice thing to do.

ABBY: Mortimer, we don’t try to stop you from doing thing you like to do. I don’t see why you should interfere with us.

TEDDY: (Pg 39) (enters from cellar, blows a terrific blast on his bugle) CHARGE!

ABBY: (Pg 45-46) Teddy! Teddy, there’s been another Yellow Fever victim. (with a finger to her lips) We must keep it a secret.

TEDDY: A state secret? (he’s excited) You have the word of the President of the United States

(crosses his heart)

ABBY: Go back down in the cellar and when it’s all dark, you come up and take the poor man down to the Canal.

MARTHA: And we’ll come down later and hold services.

TEDDY: Where is the poor devil?

MARTHA: He’s in the window seat.

TEDDY: It seems to be spreading. We’ve never had Yellow Fever there before. (blows his bugle and exits) ***** [Spoken Transition: The next day after reports of horrendous bugle blowing from the neighbors, police officer Rooney arrives at the Brewster residence] ****

MORTIMER: (a knock; Mortimer answers the door) (Pg 84) Captain, I'm Mortimer Brewster.

TEDDY: (Pg 83) (butting in) There are bodies in the cellar.

ROONEY: Who are you?

TEDDY: I’m President Roosevelt

MORTIMER: (Pg 84) My brother Teddy -- the one who blew the bugle.

ROONEY: (to Teddy) (Pg 83) Well, you’ve blown your last bugle. (to Mortimer) (Pg 84) He's got to be put away!

TEDDY: (Pg 83) (interjecting) All the bodies in the cellar are Yellow Fever victims.

MORTIMER: (Pg 84) I quite agree with you. ln fact, it's all arranged for.

ROONEY: Where's he going?

MORTIMER: Happy Dale.

ROONEY: All right, I don't care where he goes as long as he goes!

MORTIMER: Oh, he's going all right. But I want you to know that everything that's happened around here Teddy's responsible for. Now, those bodies in the cellar . . .

ROONEY: (thinks this is a joke) Yeah, yeah, those bodies in the cellar! It ain't enough his disturbing the peace with that bugle, but can you imagine what would happen if that cock-eyed story about bodies in the cellar got around? And now he's starting a Yellow Fever scare. (shakes his head and chuckles)

MORTIMER: (Greatly relieved, with an embarrassed laugh) Bodies. Do you think anybody would believe that story? (a knock the door)

MORTIMER: Will you excuse me? (He goes to door and admits Elaine and Mr. Witherspoon, an elderly, tight-lipped disciplinarian)

ELAINE: (Pg 85) This is Mr. Witherspoon, the superintendent of Happy Dale. He's come to meet Teddy.

ROONEY: (introducing himself) Lieutenant Rooney. I'm glad you're here, because you're taking him back with you today!

WITHERSPOON: Today? I had no idea it was this immediate.

ROONEY: The papers are all signed, he goes today! There's your man! (pointing at Teddy)

TEDDY: (livid) Complete insubordination! You men will find out I'm no mollycoddle. When the President of the United States is treated like that -- what's this country coming to?

MORTIMER: (trying to calm things down, he speaks to Teddy as to a child) Mr. President, I have very good news for you. Your term of office is over.

TEDDY: (thinking) OH! Now I go on my hunting trip to Africa! Well, I must get started immediately. (he looks at Witherspoon suspiciously) Is he trying to move into the White House before I've moved out?

MORTIMER: Who, Teddy?

TEDDY: (pointing at Witherspoon) Taft!

MORTIMER: This isn't Mr. Taft, Teddy. This is Mr. Witherspoon. (enthusiastically) He's to be your guide in Africa.

TEDDY: (Shakes hands with Witherspoon) (Pg 86) Bully! Bully! (he turns to the Aunts) Good-bye, Aunt Abby . . . Aunt Martha. I’m on my way to Africa – isn’t it wonderful? CHARGE! (Teddy and Mortimer exit upstairs and Rooney exits outside to wait)

ABBY: (Pg 93) Mr. Witherspoon? Does your family live with you at Happy Dale?

WITHERSPOON: I have no family.

MARTHA: Well, I suppose you consider everyone at Happy Dale your family?

WITHERSPOON: As head of the institution, I have to keep quite aloof.

ABBY: That must make it very lonely for you. (with a knowing nod to Martha) Well, Martha, I think we should at least offer Mr. Witherspoon a glass of elderberry wine.

MARTHA: (pouring a glass) We make it ourselves.

WITHERSPOON: Why, yes . . . You don’t see much elderberry wine nowadays. (He takes the glass and toasts the ladies; then keels over)

TEDDY: (off stage) (Pg 85) CHARGE! (Bugle blast)
```

---

## IC-1318: Babel’s In Arms

- Title: Babel’s In Arms
- Author (byline): David Ives
- Work: Time Flies and Other Short Plays
- Publisher: Grove Press
- Publication date as stated: March 2001
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: GORPH, CANNAPHLIT, BOTH, BSWOMAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1233
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Ives
Book: Time Flies and Other Short Plays
ISBN: 978-0802137586
Publisher: Grove Press
Date (Month/Year): March 2001
```

### Introduction (context only: never use it for content warnings)

```text
Babel’s in Arms by David Ives
```

### Performance text (classify this)

```text
Enter two workers, GORPH and CANNAPHLIT Primitive tools hang from their belts. They are carrying between them an enormous rectangular building stone, maybe five feet long and two feet high. They inch slowly toward center with it, as . . .

GORPH: (groaning under the stone's weight) Okay. . .Okay. . . Okay. . .Stop. (A moment, as they catch their breath.)

CANNAPHLIT: Okay?

GORPH: Go.

BOTH: (ad lib, moving toward center) Okay. Okay. Okay. Okay.

GORPH: Stop. (They catch their breath a moment.) Go. (They move a few inches.) Stop. (They stop to catch their breath) Go.

CANNAPHLIT: (at center now) Stop.

GORPH: Okay. Down. (They slowly lower the stone.) Down. Down. Down. Down. Down. Stop. (looks at it.) Behold! . . . . It’s backwards. (They go in a circle.) Circle

CANNAPHLIT: Circle.

GORPH: Stop. Okay. Down. . . Down. . . Down. . . Stop. (They now have it an inch over the ground.) One. Two. Five. Go! (They drop the stone to the ground.) Behold the stone!

CANNAPHLIT: Behold the stone! Big stone. (They moan, they groan, they stretch, they wipe sweat from each other's foreheads.) But what is a "stone," O, Gorph, son of Khlekhmalekhm?

GORPH: That heavy thing there. That is a stone, O, Cannaphlit, son of Bob.

CANNAPHLIT: Ah, so that is a stone. But is this stone in the right place, O, Groph, son of Khlekhmalekhm?

GORPH: I will consult the plans, O, Cannaphlit, son of Bob. (He takes out a large parchment roll.) Behold the plans.

CANNAPHLIT: Behold the plans! (GORPH unrolls a blueprint-a large blue sheet of paper with just a single white rectangle in the middle.)

GORPH: (After inspecting the plans) The stone must move one sixteenth of an ell to the north!

CANNAPHLIT: One sixteenth of an ell! How far is that?

GORPH: About an inch.

CANNAPHLIT: (as GORPH takes out the crowbar) O my friend? What is that?

GORPH: This item has no name, for humanity is young and has not words yet for every item. Basically, it's a rigid rod that pivots about a fulcrum and is used to move an object at point A by applying force at point B. . . . I call it a lever.

CANNAPHLIT: Behold the lever!

GORPH: (With a huge grunt, he levers the stone an inch to the lift; that done, he checks, and nudges it with his toe one last small bit.) The stone is now in place.

CANNAPHLIT: The stone is in place! (They snort, high-five, shake hands, flex muscles, grab crotch, and generally male-display.) So what is the stone for, O, Gorph?

GORPH: This stone? This stone is for. . . You mean thou dost not know?

CANNAPHLIT: I dost not know. (They regard, the stone a moment.) A BUSINESSWOMAN in a killer suit with a large sword in a scabbard, enters sets up a sign that says "FUTURE HOME OF BABEL."

GORPH: (reading the sign) "Future Home of Baybel."

BSWOMAN: Babble. It's not "Baybel." It's Babble. Now listen up, you rotten stinking men.I represent a consortium of off-desert investors who want to develop this property. Our mandate is to build a tower whose top will reach to the very heavens, indeed, into heaven, indeed, as high as God. This in order to show that we are equal to same aforesaid God.

GORPH: That we are equal to God?

BSWOMAN: No, that we, not you, are equal to same aforesaid God. You are nothing. You are scum, but you build the tower. Have you got that?

GORPH: We're scum. We build the tower.

BSWOMAN: In the event that same aforesaid God is not pleased, the consortium is not responsible for any long-term apocalyptic events. Sign here. (presents a parchment; Gorph and Cannaphlit sign and she immediately takes it away) Understood. Now. The most important thing. And this is absolutely crucial. Are you listening? (They nod.) Do not - under any circumstances - khlumnafluffa himnaflekh.

CANNAPHLIT: Do not khlumnafluffa bimbaflekh?

BSWOMAN: Himmm-naflekh.

CANNAPHLIT: Himmmmm-naflekh.

BSWOMAN: (pulls sword from its scabbard) Instructions clear? Or else you die.

GORPH: Mm-hm... Oh yeah. . . I think so . . . Very clear. . .

BSWOMAN: One last crucial thing. Did you bring the shpoont?

GORPH: Oh, the shpoont.

CANNAPHLIT: I think we have the shpoont.

GORPH: The shpoont was here a moment ago.

BSWOMAN: Do not proceed without the shpoont. (takes out the sword) Or else you die. I'll be checking in very soon. Now get to work. (Businesswoman exits.)

GORPH: Khlumnafluffa himnaflekh . . .

CANNAPHLIT: Khlumnafluffa himnaflekh. . . .

GORPH: What the heyyyyy is that?

CANNAPHLIT: That was a little vague. The other instructions were pretty clear.

GORPH: Oh yes? Repeat the instructions. Refresh my memory.

CANNAPHLIT: Build a tower whose top reaches to the very heavens, indeed, into heaven, indeed as high as God. Proving that they - not we because we are scum - that they are equal to same aforesaid God.

GORPH: That's very clear.

CANNAPHLIT: And don't khlumnafluffa himnaflekh, or you die.

GORPH: And don't forget the shpoont. (They look at each other and shrug)

CANNAPHLIT: Maybe we could put a portico on the tower, in pink, do a rich pink ceiling, maybe use that sponging technique. . .

GORPH: But consider this, O son of Bob. Putting the pink portico aside for a moment. Why? Let us nail down why. Name an attribute of God. Go ahead. Just pick an attribute, any attribute.

CANNAPHLIT: God is fairly powerful.

GORPH: Powerful. Mm-hmm . . .. Any other attributes?

CANNAPHLIT: I'd say God is eternal and infinite.

GORPH: Infinite. Let's pause there for a nanosecond. How high would a tower have to be to meet an infinite God?

CANNAPHLIT: Hmmm. (He ponders that a moment, then raises his hand like a student.)

GORPH: (teacher) Cannaphlit?

CANNAPHLIT: Infinitely high?

GORPH: Infinitely high. So you're going infinitely high – how broad would the base of same aforesaid tower would have to be? Just gimme a rough guesstimate. (Pause as Cannaphlit ponders that. Then he raises his hand again like a student.)

GORPH: (teacher) Cannaphlit?

CANNAPHLIT: Infinitely broad?

GORPH: Innnnfinitely broad. How many stones would we have to use? An innnnnnfinite number of stones. And how long did it take us to get this stone here?

CANNAPHLIT: Two years.

GORPH: So our task is to build a tower infinitely high, infinitely broad, from an infinite number of stones, shake hands with God AND - do not khlumnafluffa himnaflekh while using the shpoont.

CANNAPHLIT: It's gonna be work.

GORPH: It's gonna be work.

CANNAPHLIT: (brilliant idea) Maybe we should get out of it!

GORPH: But how, O brilliant Son of Bob? We just say no? But we need a reason. So when they ask us why we've laid down our tools, we say. . . ?

CANNAPHLIT: We could tell them God doesn't exist.

GORPH: I love it! It's simple. It's elegant.

CANNAPHLIT: What could they do?

GORPH: Cut off our heads! (They ponder the dilemma for a moment, grunting)

CANNAPHLIT: Wait a minute. Who says God is in the sky?

GORPH: Yeah! Where did this arcane idea come from?

CANNAPHLIT: Maybe God isn't up, maybe God is down.

GORPH: Oh, man, it's brilliant. Brilliant!

CANNAPHLIT: We don't have to build a tower infinitely high and infinitely broad! We just have to dig a big hole! (They celebrate, but then realize)

BOTH: An infinite hole. . .

CANNAPHLlT: Wait a minute. (tapping his head with a brilliant idea) Candlepower! Candlepower!

GORPH: What've you got? What. What. What.

CANNAPHLIT: We tell them God is everywhere. If God is everywhere, you don't have to build a tower or dig a hole or nothin' !

GORPH: Because we're already there. (They celebrate wildly for a moment, then stop suddenly.) Is it true?

CANNAPHLIT: I don't know. We could say it. (They go back to celebrating.)

BOTH: Whoo-EEEEE!

CANNAPHLIT: We're there, buddy! GORPH: We did it!

(They snort, high-five, shake hands, flex their muscles, grab their crotches, and generally male display. The Businesswoman comes in and watches them celebrate.)

BSWOMAN: So how are we doing?

GORPH: Good. Good. We're doing good. Excellent.

CANNAPHLIT: There it is.

GORPH: (arms wide over the audience) Behold!

CANNAPHLIT: (arms wide over the audience – a pause) The tower!

GORPH: Shake hands with God, baby. 'Cause we are DONE.

BSWOMAN: (draws the sword) Explain this to my trusty sword.

CANNAPHLIT: Well... You don't need a tower because God is everywhere. You see?

BSWOMAN: I see nothing. And my sword sees nothing.

CANNAPHLIT: Maybe you're not looking hard enough. (points) God is here. (points elsewhere) God is here . . .

GORPH: God's up there, God's down there. I swear to God. Who is everywhere. As you see. (Silence.)

BSWOMAN: Did you khlumnafluffa himnaflekh?

BOTH: Oh no. No, no. Uh-uh. Never. Not at all. Mmmm. Don't think of it. Nope. No way.

BSWOMAN: Did you use the shpoont?

GORPH: Constantly.

BSWOMAN: I don't believe you. Prepare to die. (She raises the sword.)

CANNAPHLIT: We saved your life! The tower you wanted would've taken an innnnnfinite number of stones which would've cost an innnnfinite number of schmootzkels. Consortium calls you in! You’re cold cuts, babe. (The Businesswoman considers that a moment.)

BSWOMAN: Gentlemen - I LOVE THIS TOWER. It's beautiful! It's got balance, it's got harmony.

GORPH: Put together an infinite number of nothing - eventually, you get this.

CANNAPHLIT: How do you like the portico?

BSWOMAN: The portico is my favorite part! Congratulations! (Now all three of them snort, Flex, shake hands, etc.) Well you guys did a terrific job and the Consortium thanks you. So as a bonus here's a bag of cow manure for you.

(Gives a dripping bag to Gorph and another to Cannaphlit) And a bag of cow manure for you.

GORPH: Golly. Thanks a lot. That's cow manure all right.

CANNAPHLIT: Nice and fresh too.

BSWOMAN: As an option you could be castrated and be sacred eunuchs.

BOTH: (ad lib) Oh, that's all right. . . I think the cow manure is enough. . .

BSWOMAN: We won't forget this. Thank you.

CANNAPHLIT: Our pleasure.

BSWOMAN: Don't spread that all in one place. (Businesswoman exits.)

GORPH: Tower to God, huh. Easier than I thought.

CANNAPHLIT: (lifting up his bag of manure) This is where thinking'll get you!

GORPH: So listen. Now we found God - you wanna invent the wheel?

CANNAPHLIT: Yeah. What's a wheel?
```

---

## IC-1319: The Bad Guys

- Title: The Bad Guys
- Author (byline): Aaron Blabey
- Work: Not specified
- Publisher: Scholastic Press
- Publication date as stated: Dec 2016
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: MR. WOLF, POLICE OFFICER, MR. SNAKE, MR. PIRANHA, MR. SHARK, SECURITY GUARD, MR. PIRAHNA, DOG 1, DOG 2, DOG 3, DOG 4
- Teaser before the introduction: Yes
- Spoken words (computed): 1096
- Already set (do not supply): none

### Source block (context only)

```text
Author: Aaron Blabey
ISBN: 978-0545912402
Publisher: Scholastic Press
Date (Month/Year): Dec 2016
```

### Introduction (context only: never use it for content warnings)

```text
The Bad Guys. They’re scary and dangerous and well . . . just bad. But these guys want to be heroes. And they’re going to prove it by breaking every last dog out of the pound. The Bad Guys are ready to do some good . . . whether you want them to or not!

The Bad Guys by Aaron Blabey
```

### Performance text (classify this)

```text
MR. WOLF: Pssst! Hey, you! Yeah, you. What’s the problem? Oh, I see. Yeah, I get it . . . You’re thinking, “Ooooooh, it’s a big, bad, scary wolf! I don’t want to talk to him! Heas a MONSTER.” Well, let me tell you something, buddy – Just because I’ve got big pointy teeth and razor-sharp claws . . . and I occasionally like to dress up like an old lady, that doesn’t mean . . . I’m a bad guy.

POLICE OFFICER: SUSPECT RAP SHEET – Mr. Wolf aka Big Bad, Mr. Choppers, Grandma

Criminal Activity: 1. Blowing down houses (the 3 pigs involved were too scared to press charges) 2. Impersonating sheep 3. Impersonating old women 4. Attempting to eat old women [and] relatives of old women 5. Theft of night gowns and slippers. Status: Dangerous. DO NOT APPROACH.

MR. WOLF: It’s all lies, I tell you. But you don’t believe me, do you? Because I’m the Bad Guy, right? Wrong. I’m a great guy. A nice guy, even. But I’m not just talking about me . . . I’ve got some buddies who have the same problem, so I’ve asked them to join us. They’re great guys. But just like me, they are misunderstood.

MR. WOLF: Are you ready to learn the truth? You’d better be, baby. (Knock! Knock! Knock) Let’s see who’s here, shall we? (Opens door) Heey! It’s my good pal, Mr. Snake. You’re going to love him. He’s a real . . .

MR. SNAKE: Sssssswwwweeetheart!

POLICE OFFICER: SUSPECT RAP SHEET – Mr. Snake aka The Chicken Swallower. Criminal

Activity: 1. Broke into Mr. Ho’s Pet Store 2. Ate all the mice, canaries [and] guinea pigs at Mr. Ho’s Pet Store 3. Tried to eat Mr. Ho. Status: Very dangerous. DO NOT APPROACH.

MR. SNAKE: Will this take long, man? I’ve got mice to eat.

MR. WOLF: (Laughs) What a joker this guy is! “I’ve got mice to eat!” That’s a good one.

(laughs) (Knock! Knock! Knock!)

MR. SNAKE: Hey! Who’s that? What’s going on here?

MR. WOLF: Take it easy. Have a cupcake.

MR. SNAKE: A cupcake? You got any mice?

MR. WOLF: Enough with the mice, or I’ll eat you! (notices audience) I mean . . . Goodness, I wonder who could be at the door? (opens door) Well, if it isn’t Mr. Piranha. Now if anyone has a bad reputation, it’s this guy . . .

MR. PIRANHA: Hola.

POLICE OFFICER: SUSPECT RAP SHEET -- Mr. Piranha aka The Butt Biter. Criminal Activity: Eating tourists. Status: EXTREMELY dangerous. DO NOT APPROACH.

MR. WOLF: Hey, Mr. P! I know a sweet guy like you wouldn’t say no to a cupcake . . .

MR. PIRANHA: I’ve come all they way from Bolivia, hermanos. And I’m hungry! Where’s the meat?! (Knock! Knock! Knock!)

MR. WOLF: Aha! Now I know this guy like cake . . . (opens door) Hey there, Mr. Shark. How’s it going?

MR. SHARK: I’m hungry. You got any seals?

POLICE OFFICER: SUSPECT RAP SHEET – Mr. Shark aka Jaws. Criminal Activity: Will literally eat ANYTHING or ANYBODY. Status: RIDICULOUSLY DANGEROUS. RUN! SWIM! GET OUT OF HERE!!!

MR. WOLF: This is what I’m talking about! How will anyone take us seriously as Good Guys if all you want to do is eat everyone?

MR. SNAKE: Good guys? What’s he talking about?

MR. PIRANHA: Beats me . . .

MR. WOLF: This is the very first meeting of The Good Guys Club! That’s right! The Good Guys Club!

MR. SHARK: I beg your pardon?

MR. WOLF: Aren’t you tired of being the villain? Aren’t you tired of the screams? Aren’t you tired of the fear?

MR. PIRANHA: Not particularly.

MR. WOLF: Of course you are! And I have the solution! Pop Quiz . . . Let’s say we find a cat stuck in a tree. What do we do?

MR. SHARK: Eat it?

MR. WOLF: No! We rescue it!

MR. PIRANHA: I came all the way from Bolivia for THIS?

MR. WOLF: (gathering his patience, he tries again) [Look] If we’re going to be heroes we need to be able to smell trouble! (sniffs) In fact . . . I think I can smell trouble right now . . . (sniffs) Wow, it’s really strong . . . (sniffs) Hang on. That’s not . . . Aw, who farted?! (Mr. Snake reacts) (gathering his patience, he tries again) It’s time for OPERATION DOG POUND! 200 puppies are locked up in the Maximum Security City Dog Pound. Their hopes and dreams are trapped behind walls of stone and bars of steel. But guess what? We’re going to set them free . . . with this! (he holds out a dress on hanger)

MR. SNAKE: Are you going to dress up like an old lady AGAIN? It doesn’t work, man. You ALWAYS get caught!

MR. WOLF: Who said anything about me? (looks meaningfully at Mr. Shark)

MR. SHARK: He’s completely lost his mind ****** AT THE POUND ******

SECURITY GUARD: (Ring, Ring - answering phone) Hello? Oh, certainly, miss. I’ll buzz you in.

(pushes buzzer to open door – Mr. Shark enters disguised as a young girl) Now what can I do for . . . uh . . . you?

MR. SHARK: I’m just a pretty young lady who has lost her dog. Please, oh please, can you help me sir?

SECURITY GUARD: (smitten) Well, of course! Anything for such a lovely young lady.

Mr. SHARK: Cool.

****** OUTSIDE ******

MR. WOLF: He’s in! I knew this would work. Now, you know what to do. Once those cages are open, we won’t have long, so don’t mess it up. (he takes out a grappling hook with a length of rope)

MR. SNAKE: What’s that thing for?

MR. WOLF: Climb aboard, fellas! (Mr. Snake and Mr. Pirahna climb onto the grappling hook) Hold on tight. And remember – once Mr. Shark gives me the signal, I’ll get you inside and all you have to do is tell the dogs which way to run. Got it?

MR. PIRANHA: Yeah. But how do we get inside?

MR. WOLF: I’m just going to throw you through that tiny little window. (points) But don’t worry! I have excellent aim and I’m 85% sure I’ll get you in on my first throw!

MR. SNAKE: Hey man, can we talk about this for a second? ****** AT THE POUND ******

SECURITY GUARD: I wouldn’t normally open all these cages at once, but since you asked so nicely. . . Well, here’s the last cage. Is THIS your dog?

MR. SHARK: No. Oh, woe is me! I shall never find my dog! (cries loudly) ****** OUTSIDE ******

MR. WOLF: That’s the signal! No time to talk! Hold on tight little buddies. (swings the grappling hook like a lasso) (Mr. Snake and Mr. Pirahna twirl around dizzily) It’s time to go be a hero! (he throws the hook)

MR. PIRAHNA: (in mid-air) It we survive this, I’m going to eat that wolf.

MR. SNAKE: Not if I do it first! (Clank! the hook catches on the bars of the window and Mr. Snake and Mr. Pirahna leap to the floor)

MR. PIRAHNA: This is your lucky day, hermanos! We’re getting you out of here!

MR. SNAKE: Everyone, follow us!

DOG 1: Is that what I think it is?

DOG 2: That’s a snake, dude.

DOG 3: But what’s that other thing?!

DOG 4: I think it’s a . . . sardine maybe.

DOG 1: (running for their lives, barking and howling) HELP! There’s a snake!

DOG 4: And some kind of weird sardine thing! HELP!

MR. SHARK: (looming threateningly) You’re running the wrong way!

DOG 3: (reversing direction) HELP! SHARK!

MR. PIRAHNA: OK, Mr. Wolf . . . Hit it!

MR. WOLF: (blows a hole in the side of the dog Pound) Let’s give those puppies their freedom!

DOG 2: (as they race away from the pound) Help! A wolf!

DOG 1: And a shark!

DOG 3: And a snake!

DOG 4: And some kind of vampire sardine!

MR. WOLF: Look at them, guys! We’ve changed their lives! They’ll love us forever! ****** LATER THAT DAY ******

MR. SHARK: Well, they certainly didn’t seem very grateful, did they?

MR. PIRAHNA: They called me a sardine!

MR. WOLF: You’re missing the point, guys. We did it! We gave 200 dogs a whole new life. Doesn’t that make you feel awesome?!

MR. SNAKE: I thought you were a sardine.

MR. WOLF: Today is the first day of our new lives. We are not Bad Guys anymore. We’re Good Guys! And we are going to make the world a better place. For the first time in my life . . . the future smells sweet! (sniffs) Wait a second – That doesn’t smell sweet . . . Piranha, did you fart?

MR. PIRAHNA: Just deal with it, chico. I get gassy when I’m upset. They called me a sardine.
```

---

## IC-1320: Bar Mitzvah Boy

- Title: Bar Mitzvah Boy
- Author (byline): Samara Siskind
- Work: Shorter, Faster, Funnier: Comic Plays and Monologues
- Publisher: Knopf Doubleday Publishing
- Publication date as stated: 2011
- Event as filed: Humorous Interpretation
- Record type: Cutting
- Speaker labels in the text: STACIE, SAMUEL
- Teaser before the introduction: Yes
- Spoken words (computed): 1129
- Already set (do not supply): none

### Source block (context only)

```text
Author: Samara Siskind
Book: Shorter, Faster, Funnier: Comic Plays and Monologues
ISBN: 978-0307743350
Publisher: Knopf Doubleday Publishing
Date (Month/Year): 2011
```

### Introduction (context only: never use it for content warnings)

```text
(In a very geeky manner) MY BAR MITZVAH – The huge party when my family announced to the world that I am a Man. A man . . . who girls LOVE! This is how it happened: I make eye contact with the hottest girl in the 7th grade and give my straw a little tongue action so she knows I mean business. A slow song comes on and I strut over to her, not even asking if she wants to dance. I give her the look, and suddenly the two of us engage in a passionate make out session in the middle of the dance floor. Well, maybe that’s not EXACTLY what happened. But it’s the way I like to remember it . . . Bar Mitzvah Boy by Samara Siskind
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
