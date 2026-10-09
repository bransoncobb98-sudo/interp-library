# Classification request: batch 3 of 53 (40 records, IC-0481 to IC-0520)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-003-reply.json`.

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

## IC-0481: Aunt Leaf

- Title: Aunt Leaf
- Author (byline): Barbara Wiechmann
- Work: Not specified
- Publisher: Dramatic Publishing
- Publication date as stated: 2012
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: VOICE 1, VOICE 2, FATHER, FAMILY, AUNT LEAF, ANNABELLE, MOTHER, TEACHER, SISTER
- Teaser before the introduction: Yes
- Spoken words (computed): 1721
- Already set (do not supply): none

### Source block (context only)

```text
Author: Barbara Wiechmann
ISBN: 978-1583427798
Publisher: Dramatic Publishing
Date (Month/Year): 2012
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: When you have an idea, how do you share it with someone else?

ACTOR 2: Wait, wait. I know the answer. You text them or email them.

ACTOR 1: Because technology is everything. It’s fast, it’s efficient. But somehow, it loses something in the translation.

TOGETHER: True human connection.

ACTOR 2: That’s why we struggled so much during COVID when ALL forms of connection went digital.

ACTOR 1: Even these types of competitions – we missed the connection.

ACTOR 2: Jimmy Neil Smith, the Director of the International Storytelling Center explains: “There isn’t a stronger connection between people than storytelling.

ACTOR 1: “Stories make us more alive, more human, more courageous, more loving.” -- Madeleine L’Engle

ACTOR 2: “That’s what storytellers do. Restore order with imagination. Instill hope again and again.” – Walt Disney

ACTOR 1: Living things are filled with stories. When you sink your toes in the mud you're sinking in stories. When you lie breathing in the dark, you're breathing stories . . .

ACTOR 2: So today, we’re going to tell you a story . . . A story about stories.

TOGTHER: Aunt Leaf by Barbara Wiechmann
```

### Performance text (classify this)

```text
Note from the Author: (pg 7-8) Aunt Leaf is a story about storytelling. It was never my intent to have one actor play one role. In the original production, three performers “shared” the entire script, shared the story. All performers played all roles, completely unbiased as to gender, race and age. A storyteller can play anything. If you envision the play as a solo performance or a storytelling play for 20, give it a try. The only limit should truly be your imagination.

VOICE 1: (Pg 11-12) Do you know this story? Do you know the story of Aunt Leaf?

VOICE 2: The story of Aunt Leaf is also the story of a little girl. Annabelle Wood.

VOICE 1: Annabelle lived one hundred years ago in a house surrounded by trees on the banks of the Hudson River.

VOICE 2: In those days the river was just as wide and glittering as it is today, but the forests were thicker, wilder, more dangerous and more mysterious.

VOICE 1: Annabelle did not worry about this. She was 11 years old . . . she fished along the riverbank, climbed the branches of a big tulip tree and lived safe inside the house with her cheerful and talkative family.

VOICE 2: Annabelle rarely talked at all [and her] silence concerned her family.

VOICE 1: (Pg 13) One morning at breakfast Annabelle's father made an unusual announcement:

FATHER: My Great-Aunt Leaf has slipped on an acorn in that crazy house of hers in the woods. It isn't safe for her to live alone anymore! She'll have to come live with us.

VOICE 1: And so Aunt Leaf came.

VOICE 2: Annabelle's father opened the passenger-side door. . . Slowly, slowly out came a pile of blinking black rags.

VOICE 1: Aunt Leaf could have been eight trillion years old. Gnarled hands with long grey fingers stuck out of the sleeves of her stiff dress like twigs on a winter tree. She smelled like a swamp.

FAMILY: (Pg 14-15) (except for ANNABELLE, in a sudden rush and overlapping) Hello, Aunt Leaf! You must be tired. Are you hungry?

Do you like dolls? Do you know any riddles? Do you like pie?

AUNT LEAF: I want to go home! Take me home! Take me home!

VOICE 1: Annabelle's mother tried her best to make Aunt Leaf happy.

VOICE 2: She planned spontaneous family sing-a-longs

VOICE 1: Stuffed Aunt Leaf in a canoe and paddled her downstream for a picnic.

VOICE 2: Made exotic meals for Annabelle and her sisters to take up to her on decorative trays.

VOICE 1: But Aunt Leaf did not want any of it. Day by day she grew thinner. If she spoke at all it was to complain.

AUNT LEAF: The room is too hot!! The house has too many doors! My skin is just a bruise!

VOICE 1: One morning she just screamed.

VOICE 2: Only Annabelle continued to bring up the meals. Every morning silently up the stairs. And every evening down again with the untouched tray.

VOICE 1: It was the same every day. Every day. Till one night something different happened.

VOICE 1: (Pg 15-16) That night long after the rest of the family had fallen into deep sleep . . .

AUNT LEAF: (calling far off) Annabelle! ANNABELLE!

VOICE 1: Annabelle hearing her calls jumped out of bed and ran to Aunt Leaf's room. Aunt Leaf met her at the door. Her twiggy fingers pinched Annabelle's wrist.

AUNT LEAF: Go! Quick Quick! Go-outside-see if you see! See if you see! Quick! Quick!

VOICE 1: So Annabelle ran down the stairs, out the back door, and into the dark of the lawn and the woods. (she stands looking around in the dark)

AUNT LEAF: (Pg 17-19) What do you see? What do you see?! (ANNABELLE says nothing) Anything!?

ANNABELLE: Nothing.

AUNT LEAF: I heard your Great-uncle Greenleaf whistling on the lawn. Just the way he used to. Whistling to his dog. Did you hear? (ANNABELLE shakes her head) He'll come back. You'll see him next time. If you move fast enough.

ANNABELLE: Aunt Leaf, I don’t think so. I've been to the cemetery. I’ve seen his grave!

AUNT LEAF: (pause) People come back.

ANNABELLE: That's not real. That's only in stories.

AUNT LEAF: This is a story. (beat) Everything is a story.

ANNABELLE: This isn't a story.

AUNT LEAF: Yes, yes, yes, it is! Spiders, rocks, pinecones. Living things are made of stories -- filled with stories. When you sink your toes in the mud you're sinking in stories. When you lie breathing in the dark you're breathing stories . . . I heard my husband.

VOICE 1: Later that night Annabelle lay in bed thinking and rethinking.

ANNABELLE: What could it hurt to tell one little story. (beat) If it makes someone happy. . . What could it hurt to tell one tiny lie. . .

VOICE 1: (Pg 20-21) Day after day Annabelle's family talked and talked and Annabelle barely spoke at all, but now sometimes during the night she would wake up --

AUNT LEAF: Annabelle! Annabelle!

VOICE 1: -- run silently down the stairs, ghost like out the back door and began to do something she had never done before; she began to make things up:

ANNABELLE: (reporting back to AUNT LEAF, tentatively at first, but with more and more confidence) The clouds were moving very fast. (AUNT LEAF nods) I heard a dog bark across the river.

AUNT LEAF: That's a sign . . . What else?

ANNABELLE: (Pg 22-23) I found a bootprint in the mud!

AUNT LEAF: Yes! Yes!

ANNABELLE: I saw a shadow! Ripple across the grass in the moonlight- and something else. Smoke! Curls of blue smoke

AUNT LEAF: From his pipe tobacco drifting through the branches

ANNABELLE: Yes! It was him. Uncle Leaf. I saw his shadow. It was him! It was him!

AUNT LEAF: (softly) Bring me something from outside.

VOICE 1: (Pg 24-25) She pinned a swamp buttercup in Aunt Leaf's hair. Didn't Aunt Leaf look lovely? Didn't she seem young? Wasn't she happy?

AUNT LEAF: He built our house in the woods. Every morning he walked into the forest with his ax. Cut away the dead wood, made room for the new growth. Every night I waited for his footsteps. I have lit the fire for supper. I am wearing my new blue dress.

VOICE 1: (Pg 26-27) In the dark by herself Annabell began to see. The more she saw the more she wondered. The more she wondered the more she imagined. The more she imagined, the more she told.

ANNABELLE: I saw a pair of tall boots disappear into the twilight. I saw a wagging tail and the back of a dog. It was huge. . . as big as a pony. . .

VOICE 2: All that July, Aunt Leaf grew fat and hopeful on the small fibs Annabelle fed her.

AUNT LEAF: Wash my face. Hook my pearls. VOICE 1: All that August, Annabelle looked at Open the window. The air smells sweet. the way the fish jumped in the river, the I'll tell you a story . . . This is the story of way the screech owl sat on his branch in the Uncle Leaf and the summer the spiders dark. She looked for her Uncle Greenleaf’s came. . . This is the story of Uncle Leaf handsome eyes in the leaves and began to and the blizzard that covered the house . wish her own stories were true. Uncle Leaf . . Uncle Leaf and the witch of the hides himself in the shapes of animals and Athens woods. . . Uncle Leaf and the birds . . . Uncle Leaf knows the secret Bullfrog children . . .The mysterious lights language of the crows . . . Uncle Leaf knows . . . The water snake . . . the black ice . . . every story ever told the fire ball . . . the wolves. . .

VOICE 1: (Pg 29) Voices from the daytime world called to her as if through the thickness of dream . . .

MOTHER: Annabelle! You look pale. Are you all right?

TEACHER: Miss Woods! It is rude to yawn.

SISTER: Annabelle! Get up! We’re late for school!

VOICE 2: (Pg 31) But Annabelle paid no attention . . . She was busy listening to another voice. A new one. Her own.

VOICE 1: And when October came, Annabelle was wandering farther and farther into the forest, staying out longer and longer. Bringing stories from the night to share with Aunt Leaf.

VOICE 2: (Pg 33) But as the leaves turned yellow and fell one by one onto the grey earth, Aunt Leaf herself spoke less and less.

VOICE 1: Sometimes she spoke and made no sense at all . . .

AUNT LEAF: Bats in the grass! Stop pinching me! Don't eat that egg! Poison! Poison!

VOICE 1: (Pg 34-35) But Annabelle didn't care. She came back from the woods every night shining and shivering, climbed the stairs to where Aunt Leaf was waiting and told stories till the old woman fell asleep.

ANNABELLE: (very softly) This is the story of the blue pebble. This is the story of the dark. This is the story of the deep river. This is the story of the moon. *****

VOICE 2: Now came the bitter cold and one freezing night . . . Annabelle was not in her room.

FATHER: (Pg 36-37) Annabelle! Annabelle! My little girl is missing. My child is lost!

VOICE 2: Soon men arrived with lanterns and torches. They rowed out onto the river. They crisscrossed the fields on horseback. And they walked deep into the woods. . .

VOICE 1: Annabelle's mother put a vat of spiced cider on the stove and stirred and stirred so she would not be afraid.

SISTER: People come back. They do come back . . .
TRANSITION
They found Annabelle clad only in her nightgown, skin so white it was almost blue – almost
green. They brought her home and bundled her into bed.

VOICE 2: (Pg 40-41) What is real and what is not?

VOICE 1: Annabelle did not know anymore. [She] was so sick that dreams overtook her. She slept and woke and slept but could not tell which was which. She thought she heard Aunt Leaf call – but was too weak to get up.

VOICE 2: What is real and what is not? [Finally she got better]

ANNABELLE: (Pg 42-46) (rousing to look out the window) What has happened? Weren’t there leaves? Weren’t the woods filled with animals and birds? Didn't we spend all night telling stories? Aunt Leaf! Aunt Leaf?!

VOICE 2: But only the snow answered, softy brushing the window with its icy crystals.

ANNABELLE: Aunt Leaf? (long pause) What happened? I made it up. Aunt Leaf is just an old woman asleep upstairs. I was sick and now I'm better. And I am almost 12. I made everything up! Aunt Leaf!

VOICE 2: Annabelle stood in Aunt Leaf's dark room. . .

ANNABELLE: Did you know it was snowing? I went out in the snow. I went out because I heard a man chopping trees. I knew who he was. Uncle Greenleaf! I saw him walk to the tulip tree and I was afraid. No! No! You can’t have that one. It’s mine! It’s mine! One chop and it fell. Quiet. Like a cloud falling. It made no sound. He looked at me. Then he whistled for his dog and they walked back into the woods. But it was real. It was more than a story. Aunt Leaf! Aunt Leaf!

VOICE 2: Aunt Leaf did not move. (ANNABELLE puts her hand up to AUNT LEAF's cheek)

VOICE 1: Some things do not change when morning comes. Some things are not a dream. Annabelle sat looking out the window at the foggy world.

VOICE 2: Outside, the Tulip Tree lay on the white snow.

VOICE 1: Downstairs, Aunt Leaf’s body lay in a long black box.

VOICE 2: Do you know this story? Do you know the story of Aunt Leaf?
```

---

## IC-0482: Baby

- Title: Baby
- Author (byline): Conrad E. Davidson
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: 1983
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 2, COACH, BABY, TIMEKEEPER, MOMMY, DADDY, BABBY
- Teaser before the introduction: Yes
- Spoken words (computed): 894
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
NOTE: This cutting asks one student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles: ACTOR 1: Coach, Timekeeper, Mommy, Daddy

ACTOR 2: Baby Baby and Coach are discovered onstage. Baby, dressed in a graduation cap and gown, listens attentively.

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

## IC-0483: Baby Talk

- Title: Baby Talk
- Author (byline): Doug Wright
- Work: Unwrap your Candy
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Oct 2002
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ALICE, PSYCHIATRIST, BABY
- Teaser before the introduction: Yes
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
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

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

## IC-0484: Bartholomew and the Oobleck

- Title: Bartholomew and the Oobleck
- Author (byline): Theo Geisel (aka Dr. Seuss)
- Work: Not specified
- Publisher: Random House
- Publication date as stated: Oct 1949
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR 1, KING, BARTHOLOMEW, NARRATOR 2, MAGICIANS, BELL RINGER, TRUMPETER, CAPTAIN, TOGETHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1348
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
ACTOR 2: In an age when power is often mistaken for entitlement, this story feels less like a children’s fable and more like a warning etched in green slime.

ACTOR 1: King Derwin’s insistence that even the sky should bend to his will echoes a dangerous change in modern governance

ACTOR 2: Where leaders test the limits of institutions, sidestep norms, and treat politics as something to command rather than uphold.

ACTOR 1: When a leader begins to see themselves not as a servant of their people but as an all-powerful, untouchable authority

TOGETHER: Our way of life is doomed.

ACTOR 2: Can the kingdom be saved?

ACTOR 1: Only if ordinary people, institutions, and officials speak plainly

ACTOR 2: And insist, without fear, that no one, however powerful, rules the sky.

TOGETHER: Bartholomew and the Oobleck by Theo Geisel (aka Dr. Seuss)
```

### Performance text (classify this)

```text
Suggested Roles: Actor 1: Narrator 1, Bartholomew, Magicians

Actor 2: King, Narrator 2, Bell Ringer, Trumpeter, Captain

NARRATOR 1: They still talk about it in the Kingdom of Didd as The-Year-the-King-got- Angry-with-the-Sky. If it hadn’t been for Bartholomew Cubbins, that King and that Sky would have wrecked that little Kingdom.

KING: (staring up into the sky, muttering and sputtering) Humph! The things that come down from my sky!

NARRATOR 1: All spring when the rain came down, he growled at that . . . All summer when the sunshine came down, he growled at that. . . All Autumn when the fog came down, he growled at that . . . And that winter when the snow came down, he started shouting!

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

NARRATOR 2: He took the King’s secret whistle from its hook. He blew a long, low blast down the King’s stairway. And a moment later he heard them coming!

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

NARRATOR 2: On the Mystic Mountain Neeka-tave the magicians were working their terrible magic. All night they walked circles round their magic fire . . .

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

NARRATOR 2: Dawn was breaking and Bartholomew was still watching at the bedchamber window. There was something strange in the sky! At first it seemed like a little greenish cloud . . . just a wisp of greenish steam. Tiny little greenish specks were shimmering in the air right over his head.

BARTHOLOMEW: (stretching out his hand to catch a speck, the pulls his hand back, frightened. Slams the window shut, shouting) Wake up, Your majesty! Your oobleck! It’s falling!

KING: (springs from his bed) By my royal whiskers, it is! Oh, that beautiful oobleck! And it’s mine! All mine!

BARTHOLOMEW: I don’t like the looks of those blobs, Sire. They’re coming down now as big as greenish peanuts.

KING: (laughing) The bigger the better! Oh, what a day! I’m going to make it a holiday! I want everyone in my kingdom to go out and dance in my glorious oobleck!

BARTHOLOMEW: Do you really think it’s safe, Sire?

KING: (snapping) Stop asking foolish questions! Wake my royal bell ringer. Tell him to ring the great holiday bell! Run!

NARRATOR 1: Across the sleeping palace, Bartholomew ran. Then up the ladder of the high bell tower.

BARTHOLOMEW: Ring your bell! His majesty proclaims today a holiday!

BELL RINGER: (grabbing the bell rope and yanking – Nothing happens. He yanks harder – still nothing) Heh . . .? What’s wrong with my bell? I’d better take a look outside. (pokes his head out through the little trap door) Merciful gracious! What is THAT? All over my bell like greenish molasses!

BARTHOLOMEW: Not only your bell! Look at that poor robin down there in that tree! She’s stuck to her nest! That oobleck’s like glue!

BELL RINGER: (wringing his hands) Oooh! If that green stuff sticks up robins, it’ll stick up people, too!”

BARTHOLOMEW: Someone’s got to warn the people! Warn ‘em to stay inside their houses! I’ll tell the royal trumpeter! (races off)

NARRATOR 1: But all the royal trumpeter blew was . . .

TRUMPETER: (blowing on his trumpet: GLUGG!) My horn! One of those green things flew inside it! (tries to blow it out; tries to shake it out, but no success) I’ll pull it out!

BARTHOLOMEW: No! Don’t you touch it!

NARRATOR 1: [But] The trumpeter’s hand was already in it.

TRUMPETER: (grabs hold of the lump of oobleck; pulls with all his might. The oobleck stretches then snaps back inside the trumpet, yanking his arm back with it) I can’t wiggle a finger! Oh, Bartholomew, what’ll I do?

BARTHOLOMEW: I hate to leave you stuck to your horn. But if you can’t warn the people of the kingdom, I’ve got to find someone who can! (races out)

NARRATOR 1: Down the stairs raced Bartholomew Cubbins . . . down to the chamber of the Captain of the Guards.

CAPTAIN: (humming in front of his mirror, combing the ends of his moustache)

BARTHOLOMEW: Captain! DO something! Haven’t you seen the dreadful Oobleck?”

CAPTAIN: (nonchalantly laughing) Oh, that stuff. What so dreadful about that? I think it’s rather pretty. That stuff’s harmless. I’ll show you. I’ll eat some. (leans out the window, scooping up some oobleck)

BARTHOLOMEW: Don’t, Captain! DON’T!

NARRATOR 1: The Captain did! By the time Bartholomew dragged him back inside the room . . .

CAPTAIN: (mouth glued shut with oobleck. Tries to speak, but no words come out)

BARTHOLOMEW: Forgive me for leaving you, Captain . . . (races out) I’ll get the King’s horse! I’ll ride through the country! I’ll warn the people of the kingdom myself!

NARRATOR 2: He pushed open the door that led to the Royal Stables. The awful oobleck was plumping down as big as greenish footballs now! Too late to warn the people of the kingdom! There were farmers in the fields, getting stuck to hoes and plows. Goats were getting stuck to ducks. Geese were getting stuck to cows. It was piling up, great greenish tons of Oobleck, deeper and deeper on every roof in the land. There was nothing Bartholomew Cubbins could do out there.

BARTHOLOMEW: (shaking his head sadly, he steps back inside)

NARRATOR 2: But inside, a moment later, it was just as bad as out! With an angry roar, the Oobleck was suddenly hitting the palace harder! The whole palace was springing leaks. It was dripping through the ceilings. It was coming in everywhere . . . even through the keyholes!

BARTHOLOMEW: (gasping) The King!

NARRATOR 2: Where was the King? He’d forgotten all about him! Bartholomew found him in the throne room. There he sat . . . Old King Derwin, proud and might ruler of the Kingdom of Did, helpless as a baby. His royal crown was stuck to his head. The seat of his royal pants were stuck to his throne. Oobleck was dripping from his royal eyebrows.

KING: Fetch my magicians, Bartholomew! Make them say some magic words to stop the oobleck falling!

BARTHOLOMEW: (shrugging his shoulders) I can’t, Your Majesty. Their cave on Mountain Neeka-tave is buried deep in oobleck.

KING: (groaning) Then I must think of some magic words! Oh, what are those words my magicians say . . . ? Shuffle. . . duffle . . . muzzle . . . muff . . . That’s all I can remember and they don’t do any good! The oobleck keeps on falling harder!”

BARTHOLOMEW: (angry) And it’s going to keep falling until your great palace tumbles down! Don’t waste your time saying foolish magic words. YOU ought to be saying some plain simple words! This is all your fault! Now the least you can do is say, “I’m sorry.”

KING: (belligerent -- no one had ever talked to him like this before) What! ME . . . ME say I’m sorry! Kings never say I’m sorry! And I am the mightiest king in all the world!

BARTHOLOMEW: (not backing down) You may be a mighty king. but you’re sitting in Oobleck up to your chin. And so is everyone else in your land. If you won’t even say you’re sorry, you’re no sort of a king at all! (turns his back to leave)

KING: (great, deep sob, he begins crying) Come back, Bartholomew Cubbins. You’re right! It is all my fault! And I am sorry!

NARRATOR 1: And the moment the King spoke those words, something happened. . . Maybe there was something magic in those simple words, “I’m sorry.”

NARRATOR 2: Maybe there was something magic in those simple words, “It’s all my fault.” Maybe there was, and maybe there wasn’t. But they say that as soon as the old King spoke them, the sun began to shine.

NARRATOR 1: They say that all the oobleck just simply, quietly melted away.

NARRATOR 2: Then the King proclaimed a new national holiday . . . in honor of the four perfect things that come down from the sky:

TOGETHER: The rain, the sunshine the fog and the snow.
```

---

## IC-0485: Bat Boy – The Musical

- Title: Bat Boy – The Musical
- Author (byline): Keythe Farley, Brian Flemming and Laurence O’Keefe
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: Sept 2002
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: RICK, BAT BOY, RUTHIE, ACTOR 2, ACTOR 1, TOGETHER, SHERIFF, DAISY, MAGGIE, LORRAINE, MEREDITH, SHELLEY, BUD, DR. PARKER, AS SHELLEY, ROY, REV. HIGHTOWER, DOCTOR
- Teaser before the introduction: Yes
- Spoken words (computed): 1500
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
ACTOR 1: In the early 1990s, people didn't have smartphones, Netflix, email or the Internet.

ACTOR 2: What they did have was the checkout aisle at [Insert name of local grocery store].

ACTOR 1: Children forced to grocery shop with their parents sat in shopping carts and stared longingly at bubble gum, Tic Tacs, and -- of course – headlines from the Weekly
```

### Performance text (classify this)

```text
Suggested Roles: Actor 1: Rick Taylor, Daisy, Mayor Maggie, Meredith Parker, Roy, Rev. Hightower

Actor 2: Ruthie Taylor, Sherriff, Lorraine, Shelley Parker, Bat Boy, Bud, Dr. Thomas Parker, Doctor

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

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

World News tabloid

ACTOR 2: “Einstein’s Brain Comes to Life!

ACTOR 1: “Aliens Abduct Cheerleaders!” . . . and the BEST one . . .

ACTOR 2: "Bat Child Found in Cave!"

ACTOR 1: The Bat Boy story went as viral as any “fake news” story could in the days before social media.

ACTOR 2: But then some brilliant writers decided to take this bizarre and outlandish story and make it something more –

ACTOR 1: A musical that quickly became a campy cult favorite with a message about being different; about the desire to be accepted for who we are.

TOGETHER: Bat Boy – The Musical

ACTOR 2: by Keythe Farley, Brian Flemming and Laurence O’Keefe

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

MEREDITH: You're a smart boy, too. We'll turn you into a proper young man in no time. TRANSITION

ACTOR 1: Bat Boy evolves at a lightning pace learning from flash cards, photographs, videotapes and records.

ACTOR 2: He learns etiquette, how to dress and even gets his GED.

AS SHELLEY: That’s more than I can say for Rick Taylor!!

ACTOR 1: But still, that’s not enough for the good folks of Hope Falls.

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

(hand clapping, singing, humming, feet stomping, dancing, shouting) Suggested music: I’ll Fly Away -- originally written in 1929 by Albert E. Brumley and first published in 1932 by the Hartford Music Company. It is frequently played in worship services.

https://www.youtube.com/watch?v=PYyyfw349FI

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

## IC-0486: The Bible: The Complete Word of God (Abridged)

- Title: The Bible: The Complete Word of God (Abridged)
- Author (byline): Adam Long, Reed Martin and Austin Tichenor
- Work: Not specified
- Publisher: Broadway Play Publishers
- Publication date as stated: Dec 2000
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: VOICE OVER, REED, AUSTIN, MATT-2, MATT-1, TOGETHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1230
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
ACTOR 1: Hello, I’m _______________

ACTOR 2: I’m ____________

ACTOR 1: . . . and welcome to the ________________Speech Tournament and today’s performance of The Bible: The Complete Word of God (abridged) by Adam Long,
```

### Performance text (classify this)

```text
NOTE from the Authors: Written for 3 characters (Austin, Matt and Reed) However, each cast member should use his/her own real name when performing the show. We encourage each production to change the topical references in the script to keep them as up-to-date as possible.

Suggested Roles: Actor 1: Adam, Austin, Matt-1(shared role)

Actor 2: Voice Over, Eve, Reed, Matt-2 (shared role)

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

VOICE OVER: (Pg 1-2) (off stage) In the beginning, there was . . . chaos. Everything was void. God saw all that emptiness . . . (hums a song rising to a crescendo and crash) Let there be light! Adam stands aghast in the fig leaf position, covering his significant body part – music rises again to a crash – Both actors stand aghast as Adam and Eve, covering their significant body parts.

Reed Martin and Austin Tichenor

REED: (Pg 4-6) We’ll be taking you on a marvelous, spiritual journey. A quest, if you will.

AUSTIN: A journey towards enlightenment! We present to you, The Bible – the Greatest Story Ever Accepted as Fact.

MATT-2: And we’ll explain it all -- Make the unknown known.

AUSTIN: The inexplicable plicable.

REED: It’s important to point out that although this show is about the Bible, it is not about any particular religion.

AUSTIN: That’s right. It is not our intention to slander Christians, or Jews, or Muslims . . .

MATT-2: Or Buddists or Druids or agnostics . . .

AUSTIN: Or Catholics or cult members of any kind. It’s not what we want to do . . .

REED: No, why would you . . . I have done extensive research on (holds up a book) The King James Edition of the Holy Bible. (he tosses the Bible to Austin and exits)

AUSTIN: (Pg 8-9) (reading from the great book) And the Lord God caused a deep sleep to fall upon Adam, and he slept (Reed pantomimes as Austin speaks) And God took one of Adam’s ribs and made he a woman, and brought her unto the Man.

REED: (enters as Eve) Good morning! (takes a bite of an apple and tosses it to Austin) Let the downfall of Man begin! Nyah-ha-ha!!

AUSTIN: (takes a bite of the apple and continues reading with his mouth full) And God looked down on Adam and Eve and knew they had eaten of the forbidden fruit. (tosses apple way with a horrified look on his face) (Pg 10) This brings us to Chapter Five of Genesis – The Genealogy of Adam.

REED: (Pg 12-13) (rapping) . . . Begattin’, begattin’ / Everywhere begattin’ /

AUSTIN: Makin’ babies happen / ‘Cause back then there was nothing else to do! *****Scene change****

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

MATT-2: Wait a minute! Computers were on Noah’s Ark?

AUSTIN: No. Don’t be silly. Computers were in the Garden of Eden.

REED: Ohhhh . . . yeah . . . Eve had an Apple. (To Audience – back to his Ark) Now if you look very closely, I think you can see . .

MATT-1: Stop it, Reed, you’re boring everybody.

REED: (taking offense) No, I’m not.

MATT-1: Yes, you are. The story of Noah’s Ark is sooooo overdone. Everybody knows it, and besides, it probably never happened.

REED: (Pg 15) (shocked) Never happened?!? Never happened?!? Why, they might as well say that the whole Bible never happened! What do they think is up there on Mount Ararat, anyway – The titanic? They might as well strip me of my childlike faith and innocence. They might as well mock (insert name of Actor 1) because he’s never kissed anyone! They might as well tell all of you that I still wet the bed!

AUSTIN: You still wet the bed? Eeeuwwww!

REED: Stop listening to my inner monologue! (Pg 24) Now we move on the book of Exodus, where we join Moses . . .

AUSTIN: (Pg 25-26) (as Moses) All right, listen up, children of Israel. I’ve got some good news and some bad news. The good news is, I got Him down to ten. (response) The bad news is, adultery is still one of ‘em. (response) As for the commandments I talked God out of . . . Number 1: Seventies fashions were ugly then and they’re ugly now!

Number 2: Thou shalt let the poor fend for themselves. Oh, sorry. No, that’s the Republican agenda. Number 3: *Stuff* happens Number 4: (From the Appendix) Thou shalt not “SHOW ME THE MONEY!” and . . . Number 5: The English shalt not give back Northern Ireland until the Irish take back “Riverdance”! (they both do their rendition of Riverdancing) G’night, everybody!

MATT-2: And there was great rejoicing and great balls of fire. And in his hundred and twentieth year, Moses did die. *****Scene*****

AUSTIN: (Pg 46) You ready? The Wise Men!

MATT-2: (Pg 47) (looking to the heavens) Of all the nights for the Middle East to be overcast.

AUSTIN: We better hurry, or we won’t be there in time for Christmas. He’s gonna love what I got him.

MATT-2: I don’t know, mine’s pretty valuable.

AUSTIN: I’ll show you mine, you show me yours. One, two, three! (they show their gifts)

TOGETHER: Baseball mitts!

MATT-2: (Pg 48) I thought you were getting him gold.

AUSTIN: I thought you were getting him frankincense. (both shrug)

MATT-2: (Pg 49) Look! A shooting star! The sky’s cleared up! Let’s go!

AUSTIN: Wait, I’m confused. What are we supposed to do when we get there?

REED: We worship the Christ child and then we give him his birthday presents.

MATT-1: Wow – his birthday falls on Christmas? Tough break!

REED: Follow me! (they arrive at the stable)

MATT-2: (Pg 51) (as Mary) Joseph, it’s time!

AUSTIN: (as Joseph) Oh, my gosh! Quick towels and hot water! (he holds the screaming baby aloft)

MATT-2: (as Mary) We will name him Jesus!

TOGETHER: (singing as the wisemen) We wish you a merry Christmas! We wish you a merry Christmas! We wish you a merry Christmas! Our dear son of God! . . . . For he’s a jolly good savior, For he’s a jolly good savior, For he’s a jolly good savior – Who Peter will deny! *****Scene*****

AUSTIN: (Pg 56-57) (as Joseph – waving a piece of paper) Mary, Mary! Look what I found in my carpentry shop! It’s a note from Jesus.

MATT-2: (as Mary) Oh, dear . . . (reading) “Dear Mother and Fa . . . Joseph . . .” Sorry, honey.

AUSTIN: That sucks!

MATT-2: He loves you.

AUSTIN: (sulking) He loves everybody! Read the note. . . (freeze for the voice over)

VOICE OVER: “Dear Mother and Joseph, I just don’t feel I have what it takes to be a good carpenter. So I’m leaving to wander in the wilderness for forty days and forty nights to, well, get my head together. Don’t worry, I’ll be fine. Love, your miracle, Jesus.”

MATT-2: Can you earn a living as a Messiah?

AUSTIN: No, that’s why I wanted him to go into his father’s business.

MATT-2: He is.

AUSTIN: No, my business! *****Scene*****

AUSTIN: (Pg 69-71) And now, as we race through the last half of the New Testament, we are proud to present to you the adult life of Jesus! Jesus raises Lazarus from the dead! (Reed pantomimes a Zombie walk) Jesus feeds the multitudes with bread and fishes!

REED: (throws fish to the audience) [And you get a fish . . . and you get a fish . . . Everyone gets a fish!]

AUSTIN: Jesus performs miracles! (Reed makes loops with his thumbs and forefingers like an OK sign. He puts them behind his head and when he reveals them, they are intertwined. He puts them behind his head again and then reveals they are no longer connected) (Pg 74-75) Jesus is crucified! (realizes he’s said this with too much enthusiasm, he tries again with sadness) Jesus is crucified.

REED: Crucified . . .

AUSTIN: (Very, very simply) And the soldiers led Jesus away and forced a crown of thorns onto His head. They crucified him, and a great darkness fell over the land. Then came the most beautiful aspect of the entire New Testament . . . Jesus is resurrected! (They both rejoice) *****Scene*****

AUSTIN: (Pg 76-77) Now we have a very special treat for you. As you know, there are so many great musicals based on the Bible. You know, like Jesus Christ Superstar . . . (struggling to name another) Oklahoma! So in the spirit of those musicals, we’d like to present to you, the final book of the Bible in a little something that we like to call . . . REVELATION --

TOGETHER: THE MUSICAL!

REED: (Singing and both dancing) Oh, the saved are surrounded with love / And removed to the heavens above / And the damned are in a bit of a jam

TOGETHER: That’s Armageddon!

AUSTIN: (Singing and both dancing) Oh, the bad know they’ve made a mistake / They are cast into a fiery lake / It’s a goof, unless they are fireproof

TOGETHER: That’s Armageddon! (Austin continues to hum and dance weirdly by himself while Reed speaks to the audience)

REED: (Pg 78-79) Yes, Armageddon – the end of the world. And with the end of the world comes the end of our little trip through the Bible . . .

TOGETHER: Aaahhhhhh – men!!
```

---

## IC-0487: The Big Bang

- Title: The Big Bang
- Author (byline): Boyd Graham
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: 2001
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: JED, BOYD, VOICE OVER, ADAM, EVE, COLUMBUS, ISABELLA, MINNEHAHA, POCAHONTAS
- Teaser before the introduction: Yes
- Spoken words (computed): 1109
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
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

JED: Good evening everyone and welcome prospective investors. My name is Jed and this is my partner, Boyd.

BOYD: Shalom.

JED: Before we begin, we’d like to take a moment to thank Dr. and Mrs. Sid Lipbalm for the use of their beautiful apartment. Unfortunately, they’re unable to be with us tonight.

BOYD: They left on a two week trip to Israel.

JED: Now, you all understand that this is a backer’s audition.

BOYD: Which is a presentation of a Broadway musical, which we have written, hopes that some of you may be interested in in-cesting.

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

## IC-0488: The Big Over Easy

- Title: The Big Over Easy
- Author (byline): Jasper Fforde
- Work: Not specified
- Publisher: Penguin Books
- Publication date as stated: July 2006
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 1, ACTOR 2, SPRATT, BRIGGS, DS MARY, MRS. DUMPTY, ANNOUNCER 1, NURSE, DR. QUATT, ANNOUNCER 2, SINGH, EXECUTIVE
- Teaser before the introduction: Yes
- Spoken words (computed): 1723
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
ACTOR 2: It’s Easter in Reading --- a bad time for eggs. Nursery celebrity Humpty Dumpty is found shattered to death beneath a wall in a shabby area of town.

ACTOR 1: And now it’s up to Detective Jack Spratt and his new partner Mary Mary to solve the case.

ACTOR 2: But Detective Spratt is fresh from a spectacular failure to convict three wily pigs for the murder of a certain wolf -- and the media and tide of public opinion are set squarely against him.

ACTOR 1: Now new trouble is brewing . . .

TOGETHER: The Big Over Easy by Jasper Fforde.
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles:

ACTOR 1: Spratt, Announcer 1

ACTOR 2: Briggs, DS Mary, Mrs. Dumpty, Announcer 2, Nurse, Dr. Quatt, Singh, Executive

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

ANNOUNCER 1: (Pg 107) [This just in . . . ] The Reading genetic industry suffered a severe blow last night when the Quatt Foundation for Genetic Research was closed following its owner’s admission that she conducted morally dubious experiments. The disgraced Dr. Quatt has been permanently banned from funded research and has been shunned by every hospital in the nation, except for St. Cerebellum’s. **** At St. Cerebellum’s Mental Hospital to interview Humpty’s doctor, Dr. Quatt *****

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

ANNOUNCER 2: [This just in . . .](Pg 92) The incredibly dangerous homicidal maniac known as “The Gingerbreadman” was captured last night. The flour, butter, ginger and sugar psychopath, (Pg 109) with cherry eyes and thin licorice lips, (Pg 92) whose penchant for literally pulling his victims apart, is currently in a secure wing of St. Cerebellum’s (Pg 107) mental hospital, (Pg 92) where he will doubtless remain for the rest of his life. *****

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

## IC-0489: Blue Front

- Title: Blue Front
- Author (byline): Martha Collins
- Work: Not specified
- Publisher: Graywolf Press
- Publication date as stated: May 2006
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 1, TOGETHER, ACTOR 2
- Teaser before the introduction: Yes
- Spoken words (computed): 1387
- Already set (do not supply): none

### Source block (context only)

```text
Author: Martha Collins
ISBN: 978-1555974497
Publisher: Graywolf Press
Date (Month/Year): May 2006
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Martha Collin’s father, as a five-year-old boy, sold fruit in front of the Blue Front Restaurant in Cairo, Illinois, in November 1909.

ACTOR 2: What he witnessed there and then, along with the reported 10,000 spectators, is shocking.

TOGETHER: Blue Front by Martha Collins
```

### Performance text (classify this)

```text
ACTOR 1: (Pg 3) He was five. ACTOR 2: He sold fruit on the street He sold fruit. People came came to see him came to see him

TOGETHER: make change TOGETHER: make change

ACTOR 1: (Pg 14) Welcome to Cairo

ACTOR 2: (Pg 4) the street was Commercial

ACTOR 1: Dowling Pressing

ACTOR 2: Saloon Drugstore Opera House

ACTOR 1: Three States Buggy Champion Tools

TOGETHER: Blue Front Restaurant

ACTOR 1: (Pg 5) a town where people lived

ACTOR 2: together black and white

ACTOR 1: (pg 64) Eleven White churches

ACTOR 2: Eleven black churches

ACTOR 1: (pg 5) couldn’t look out the same window

ACTOR 2: couldn’t read the same books

ACTOR 1: laundry couldn’t be washed in the same machines

ACTOR 2: water came from the same source

ACTOR 1: but couldn’t be drunk from the same fountain

ACTOR 2: (pg 13) couldn’t be sworn in on the same Bible

ACTOR 1: (Pg 28) couldn’t read the same books read only the others’ old

ACTOR 2: couldn’t be served in restaurants only backdoor take-out kitchens

ACTOR 1: couldn’t swim in the swimming pool or skate at the skating rink

ACTOR 2: (Pg 8) Springfield in 1908

ACTOR 1: [247 miles away and a year earlier]

ACTOR 2: a black was accused of killing a white

ACTOR 1: another black of raping a white

ACTOR 2: a mob finding the prisoners gone burned the transporting car

TOGETHER: destroyed

ACTOR 1: 24 black businesses

ACTOR 2: 40 black homes

ACTOR 1: killed 2 successful black and also

TOGETHER: accidentally

ACTOR 2: 4 whites

ACTOR 1: in 1908 events occurred that led a 1909 Cairo paper to say its citizens were

ACTOR 2: not moved by race prejudice, nor did they permit themselves to be led into wanton destruction of property, or the taking of innocent lives, as in Springfield

ACTOR 1: (Pg 9) my father he sold fruit on the street

ACTOR 2: (pg 16) he sold fruit in front of the Blue Front

ACTOR 1: he was five

TOGETHER: he could make change

ACTOR 2: (pg 10) someone must have held him up his uncle

ACTOR 1: his father’s shoulders

TOGETHER: so he could see

ACTOR 2: (Pg 17) 10,000 including children on parents’ shoulders

ACTOR 1: who saw what occurred in November 1909

ACTOR 2: (next 8 lines in newscaster’s voices) (Pg 19) it is supposed that

ACTOR 1: it is believed that Miss Anna Pelly

ACTOR 2: Miss Annie Pelley

ACTOR 1: Miss Anne

ACTOR 2: Miss Pelly age 24

ACTOR 1: age 22

ACTOR 2: who worked In the Pupkin Dry Good store and lived

ACTOR 1: an orphan who lived with her married sister

ACTOR 2: (Pg 9) my father (Pg 19) was five

ACTOR 1: would not have seen

ACTOR 2: he could have known the little girl who found

TOGETHER: the body

ACTOR 1: she was seven

ACTOR 2: or three

ACTOR 1: but that would not have been till the next day

ACTOR 2: (next 9 lines in newscaster’s voices) It is supposed she was assaulted on Elm near her home

ACTOR 1: it is believed she struck (Pg 20) her assailant

ACTOR 2: who gagged with such cruel force

ACTOR 1: it is thought he carried her into the alley

ACTOR 2: the ground showed she was dragged

ACTOR 1: it is known she was outraged

ACTOR 2: not a doubt

ACTOR 1: and strangled

ACTOR 2: a virgin unquestionably pure

ACTOR 1: (Pg 21) said him because she was large

ACTOR 2: and he was larger he was large enough

ACTOR 1: said him because she was white

ACTOR 2: and he was black and could have therefore

ACTOR 1: must have necessarily

TOGETHER: him . . . . because

ACTOR 1: Was what they said it always was

ACTOR 2: was why they said they had to

TOGETHER: must

ACTOR 1: but it wasn’t always rape

ACTOR 2: (alleged)

ACTOR 1: it wasn’t always murder

ACTOR 2: (alleged)

ACTOR 1: it wasn’t always even alleged

ACTOR 2: (Pg 22) bloodhounds got the scent from the flour-sack cloth found in the mouth

ACTOR 1: led authorities to Poplar Street

ACTOR 2: then more hounds

ACTOR 1: more to the same place

ACTOR 2: and later all the way to the city jail

ACTOR 1: Where Will ‘Froggie’ James

ACTOR 2: Will the Frog

ACTOR 1: Will alias Frog who drove for Cairo Ice and Coal

ACTOR 2: Who stayed with Loving Green

ACTOR 1: who stayed with Georgia Cooper

ACTOR 2: To Poplar Street the house of Loving

ACTOR 1: Lovey

ACTOR 2: Lovie Green a negress of

TOGETHER: bad repute

ACTOR 1: where James stayed she was found Washing a cloth that exactly matches

ACTOR 2: no . . . a similar cloth

ACTOR 1: Will James was arrested while driving his wagon

ACTOR 2: (Pg 23) no scratches blood

ACTOR 1: no missing items

ACTOR 2: But Anna Pelley’s sister said he delivered ice last summer

ACTOR 1: he was insolent

ACTOR 2: she had complained

ACTOR 1: (Pg 44) he was seventeen

ACTOR 2: once too he could have gone to school Sumner High

ACTOR 1: (colored)

ACTOR 2: had been in town since the 1883 protests

ACTOR 1: But we do not know if he went to school

ACTOR 2: above average intelligence says a 1910 book but adds

TOGETHER: for one of his race

ACTOR 1: (in newscaster’s voice) (Pg 23) authorities are taking extraordinary
precautions
to protect their prisoners because excitement
is high in all parts of Cairo

ACTOR 2: (Pg 3) [My father] was five. (Pg 32) he wouldn’t have seen the train
make an extra stop for the prisoner
who was spirited away from jail
and into the sheriff’s hands

ACTOR 1: mutterings of lynchings heard all day

ACTOR 2: would he have heard?

TOGETHER: there may be a lynching tonight

ACTOR 1: (Pg 33) at nine the mob went to the city
jail they searched the cells wooden and steel
struck matches threatened to lynch the police
chief and jailer if they would not produce

ACTOR 2: the mob was composed almost entirely of strangers

TOGETHER: (Pg 32) there may be a lynching tonight

ACTOR 1: (Pg 38) hang

As a mirror on a wall, or the fall of a dress. to fasten to dry.

ACTOR 2: so the act of doing it changes the verb, tense not quite right.

ACTOR 1: With rope, like a swing from a tree, from a pole, like a flag

ACTOR 2: In the night,

ACTOR 1: in the air

ACTOR 2: (Pg 50) the victim hanged, though not on a tree

ACTOR 1: There were trees on those streets

ACTOR 2: trees that shaded the fenced-in yards of the large Victorian houses

ACTOR 1: trees that were known to the crowd

ACTOR 2: Not on a tree

ACTOR 1: they used a steel arch with electric lights, and later a lamppost, this was a modern event,

TOGETHER: the trees were not involved.

ACTOR 2: (Pg 51) a crowd waited at Union Depot four doors down from the Blue Front

ACTOR 1: (Pg 9) my father he sold fruit on the street

ACTOR 2: (pg 16) he sold fruit in front of the Blue Front

ACTOR 1: (pg 51) the prisoner dragged to Eight and Commercial

ACTOR 2: would his father and uncle have carried him

ACTOR 1: joined men women and children

ACTOR 2: *Overlap* (women and children) filled from side to side the entire width of the 100-foot street

ACTOR 1: a wild rush

ACTOR 2: flashes of gunfire

ACTOR 1: shouts

TOGETHER: Would he have understood

ACTOR 2: as they neared the arch 10,000 people massed together a great angry wave of humanity shouted

ACTOR 1: ‘You dog! You black brute! Kill him! Burn him!’

TOGETHER: Would he have understood

ACTOR 2: (pg 52) when someone turned on the lights on the arch flooding the street the victim the crowd

ACTOR 1: He would have clearly seen

ACTOR 2: When they raised the victim when the rope broke and the living body fell

TOGETHER: he would have seen

ACTOR 1: when they dragged the victim fifty feet shot 500 bullets into him

ACTOR 2: dragged him heavy to throw to the river but changed their minds

TOGETHER: He would have seen

ACTOR 1: When a woman lit the fire while the crowd danced and shrieked

ACTOR 2: And while the body was burning they cut off the half-burnt head

ACTOR 1: cut open the chest cut out the heart for souvenirs

TOGETHER: He would have seen

ACTOR 2: When they placed the half-burnt head in a park on a hitching post /

ACTOR 1: a tire stick / a pole

TOGETHER: He would have seen (pg 55)

ACTOR 2: he was five

ACTOR 1: (pg 59) Children were often there they were being taught.

(pg 63)

ACTOR 2: [The Belleville Illinois News Democrat reported it this way on November 12, 1909]

ACTOR 1: (next 5 lines in newscaster’s voices) In ferociously dramatic fashion the infuriated populace staged a tragedy.

ACTOR 2: The pent-up fountains of human passion, human resentment, and human revenge broke forth.

ACTOR 1: A so-called mob outbreak is as much a magnificent and grand natural phenomena as a cyclone or an earthquake, or a thunderbolt or a flood is, and it is much more unerring, more just and more terrible.

ACTOR 2: The curtain has dropped. The band has ceased to play, the crowd is gone, the lights are out, the house is dark and it is over.

ACTOR 1: The outburst has done its work of purifying and of cleansing, and in that way it has fully accomplished its heaven-destined purpose.

ACTOR 2: (pg 64) Eleven White churches

ACTOR 1: Eleven black churches

ACTOR 2: Eleven white churches heard . . .

ACTOR 1: (in a preacher’s voice) The failure of civil authorities to maintain law and order

ACTOR 2: (in a preacher’s voice) the lynchings it seems were necessary to arouse the people to startle

ACTOR 1: (in a preacher’s voice) the worst class of criminal
is the criminal negro, the worst
creature on earth, the politician
has patted this class on the head as one
pats a dog but you would not pat a mad
dog with your hand, you would use a club

ACTOR 2: The papers did not record what was said in eleven black churches

ACTOR 1: (Pg 9) my father he sold fruit on the street

ACTOR 2: (pg 16) he sold fruit in front of the Blue Front

TOGETHER: He would have seen

ACTOR 1: (pg 55) he was five

ACTOR 2: (pg 77) And the last day

ACTOR 1: [the day before my father died] he said

ACTOR 2: (in the voice of the father) You know this would could be

A better place just

Promise me that you will help

ACTOR 1: he waited

(pg 16) he sold fruit in front of the Blue Front

TOGETHER: (pg 77) he made change

ACTOR 2: (in the voice of the father as a little boy at the fruit stand) may I help you please . . . . .

TOGETHER: make change
```

---

## IC-0490: The Book of Awesome

- Title: The Book of Awesome
- Author (byline): Neil Pasricha
- Work: Not specified
- Publisher: G.P. Putnam's Sons
- Publication date as stated: March 2011
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 1, ACTOR 2, BOTH
- Teaser before the introduction: No
- Spoken words (computed): 1711
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
ACTOR 1: Polar ice caps are melting, hurricanes swirl in the seas, wars are heating up around the world, and the job market is in the deep freeze.

ACTOR 2: Whoa, it's getting pretty ugly out there.

ACTOR 1: That's why it never hurts to take a step back and enjoy the little things in life that make it less dreary and more awesome.

ACTOR 2: Based on the award-winning 10-million-plus-hit blog 1000awesomethings.com, The Book of Awesome by Neil Pasricha is an international bestselling high five for humanity and a big celebration of life's little moments.
```

### Performance text (classify this)

```text
ACTOR 1: One. Wearing underwear just out of the wash.

ACTOR 2: Now tell me is there anything quotes so nice as wrapping yourself in a pair of steaming undies just out of the dryer?

ACTOR 1: It’s like skinny dipping in a hot tub,

ACTOR 2: jumping on a horse that’s been in the sun all day,

ACTOR 1: and lying on a warm, sandy beach. . .

ACTOR 2: combined!

ACTOR 1: Sure the moment doesn’t last long,

ACTOR 2: yes, there may be some static cling,

ACTOR 1: and it’s true, you'll have to get changed really quickly in the laundry room to pull it off,

ACTOR 2: but dang girl. Hot undies. They is fine.

BOTH: AWESOME!

ACTOR 2: Two. Tripping and realizing that no one saw you.

ACTOR 1: Learning to walk ain’t easy.

ACTOR 2: Sure, you did it and I did it but we probably couldn’t do it again.

ACTOR 1: Like learning anything tough and life altering, learning to walk is a messy process that takes

ACTOR 2: time and practice. Unfortunately, the bad news is that practice doesn’t always make perfect.

ACTOR 1: Even though we’ve been mastering the art of standing tall for years, and years, and years,

ACTOR 2: everyone slips and falls now and then.

ACTOR 1: So next time your shoe catches on the top step, you trip stepping off the airports moving sidewalk,

ACTOR 2: or you bail on a patch of ice outside your front door, remember that not too long ago you couldn’t walk at all.

ACTOR 1: So your wipe out is really no big deal. As long as no one saw you.

BOTH: AWESOME!

ACTOR 1: Three. Remembering a word that has been on the tip of your tongue all day.

ACTOR 2: It’s like throwing a pail of cold water on all of your smoking inner head parts.

ACTOR 1: Gears unjam, lines start rolling, and you settle back in your seat with a satisfied smile on your face and just blurt out,

ACTOR 2: “Parcheesi that’s what it was called!”

BOTH: AWESOME!

ACTOR 2: Four. Hearing a stranger fart in public.

ACTOR 1: What’s funnier than hearing a stranger fart in public? Well sure, it can happen in a bank line up, hotel lobby, restaurant, or subway car.

ACTOR 2: It can happen in a restaurant, movie theater, or local library.

ACTOR 1: But the funniest of all has got to be the Elevator farts.

ACTOR 1: That’s the king of public farts.

ACTOR 2: Little kids are always the funniest. I once heard a child in an elevator say, “Mommy, that man just farted,” with a full on finger point right into the well-dressed butt in front of his face. But hey, I guess if you’re going to fart in a kid’s face, you deserve to be called out.

ACTOR 1: Yes, hearing a stranger fart in public can be a tiny, hilarious moment in the middle of any day.

ACTOR 2: If you are the farter I say be loud and be proud we have all been there so no need to be embarrassed. If you are in the audience, I say Enjoy the hilarious social faux pas and resulting reaction in the room.

ACTOR 1: So thank you, stranger farting in public, for adding a little comic relief to the middle of our day.

BOTH: AWESOME!

ACTOR 1: Five. Getting a truck driver to blow the horn.

ACTOR 2: Truckers have the best horns. Those things mean business.

ACTOR 1: They’re a loud and thundering slap in your face.

ACTOR 2: See when a minivan lets out an itty-bitty beep-beep telling you the light turned green, it sounds like a seagull telling other seagulls “hey, there is a guy tossing crust over here.” When a trucker does the same thing it’s a full on roar the sound a tug boat would make if it was about to crash into a lighthouse.

ACTOR 1: Sometimes, when you are driving down the highway, the hours keep going and going and going. For kids without distractions it can seem like days back there, strapped in and sitting in a numbing silence broken up only by potholes and passing motorcycles.

ACTOR 2: That's why getting a trucker to blow his horn is so great. It’s a laugh and a fun, little interactive break from highway monotony. Plus, it’s a timepasser. It’s a secret moment on wheels, a honkin’ highway holler and some good old-fashioned bonding in the fast lane.

ACTOR 1: So let’s give thanks to truckers for not taking life too seriously for indulging our simple pleasures and for rocking that blasting air horn in a special moment we like to call

BOTH: AWESOME!

ACTOR 2: Six. The Five Second Rule. The five second rule simply states that any food dropped on the floor is perfectly okay to pick up as long as you do it within five seconds.

ACTOR 1: The Five Second Rule has many variations, including The Three Second Rule, The Seven Second Rule, and the extremely handy, However Long it Takes Me to Pick it up off the Floor Rule. But whatever version you use, there is just no denying why it is so great.

ACTOR 2: 1. It makes you look less disgusting. Because now when you eat that wet grape that rolled into the corner by the heating vent and collected some cat hair and a few dry toast crumbs, you’re not disgusting. No, you’re just a law-abiding citizen. Big difference.

ACTOR 1: 2. Saves time and money. Wait, wait, wait, don’t pull the peanut butter and jelly out again and make a whole new sandwich. No, we’ll just blow the floor spices off this one, and maybe tear off the wet, soggy piece of crust that landed in the juice puddle. It’s all good.

ACTOR 2: 3. It’s scientifically proven. Well, actually it's scientifically proven that if a floor is covered in salmonella or E. coli, your food will be covered in salmonella or E. coli, even if they touch for only a split second. But, here’s the kicker, that same University of Illinois study showed no significant evidence of contamination on public flooring in general. Good save science!

ACTOR 1: So people, I give you a friend and savior in these tough times: the five second rule. Know it. Love it. Live by it.

BOTH: AWESOME!

ACTOR 1: Seven. Eating a sample you have no intention of buying.

ACTOR 2: Why hello, little cup of strawberry-kiwi punch.

ACTOR 1: How are you doing, pepper-dill crackers?

ACTOR 2: Don’t mind if I do, tiny salami wrapped around a piece of melon.

ACTOR 1: Yes, eating a free sample of something you have no intention of buying is a great way to stay on top of what’s happening in the grocery store. You swish the new drink, chew the new gum, toss back a tiny cup of the new pasta dinner, and introduce your taste buds to a little surprise.

ACTOR 2: Assuming you don’t actually like the product, maybe you do what I do and pretend you're going to buy it anyway, so you don’t hurt the sweet, heavily lipsticked Sample Lady’s feelings. So you pick up the box of dry crackers, salty salami of all-noodle no cheese lasagna and say, “Hmmm. $4.29? Not bad, not bad. And I get a fifty-cent coupon too? Hmmm.” Then you smile back a her, toss it in your cart, and say “Why not! Thank you very much!” Then you roll out of sight and guiltily drop it in another aisle.

BOTH: AWESOME!

ACTOR 2: Eight. Absolute perfect silence.

ACTOR 1: Nine. Squeezing through a door without touching it.

ACTOR 2: Tiny squirts of adrenaline pump into your bloodstream when you pull of this classic movie.

ACTOR 1: Yes, suddenly you morph from Guy Walking Down the Street into Indiana Jones in that Scene Where He Slides Under the Wall at the Last Second.

ACTOR 2: Your hands stay clean, your strut stays mean, and you zip through that closing door and don’t look back, hoping it doesn’t nail anybody in the face behind you.

ACTOR 1: AWESOME!

ACTOR 2: Ten. Remembering someone's name.

ACTOR 1: I have a problem. Within seconds of meeting somebody I completely forget their name. Sure, I introduce myself. Shake hands, and jump right into the conversation, but I can’t fully concentrate because I realize their name has immediately disappeared from my memory. Cursing myself I silently scan my frontal lobe, but my pink and lumpy mush is bright white and empty. So I smile and nod along, but inside I’m frustrated. But it’s even worse when they use my name right away.

ACTOR 1: “So Neil, where you from, Neil.”

ACTOR 2: They’ll ask innocently, but I’m too busy combing through cobweb-covered spare parts in skull factory to properly answer them. My eye contact drifts and I get distracted and fidgety. It’s at these desperate times I try one of the two name-teasing techniques.

ACTOR 1: The take two. A friend joins my side at the party and I say to the mystery man, “Oh, have you met Chad?” hoping that Chad will put out his hand and lean in with a “Nice to meet you! Sorry, what was your name?” If Chad nails it, I give him a hi-five later. If he doesn’t, I throw a cup of punch in his face and tell him to get it right next time.

ACTOR 2: The spell check. If I don’t remember their name, but I think it was long and complicated, then I ask them to spell it for me. If they say

ACTOR 1: P-a-r-d-e-e-p

ACTOR 2: then I’m all aces, if they say

ACTOR 1: P-a-m,

ACTOR 2: then I’m an idiot. High risk high reward. Sure there techniques look easy, but the truth is that they’re awkward and embarrassing to use with no guaranteed results. Let's be honest. It’s much more satisfying to actually remember and drop their name right at the beginning of a sentence with confidence, like you’ve been old friends for years. Then they’ll look back at you with beaming eyes and a bright smile that shows you two are getting to know each other. Yay, maybe you’ll become friends, maybe you’ll do business, maybe you’ll start dating. All because you remembered their name at the party. Nice move you!

BOTH: AWESOME!

ACTOR 1: And finally, remembering how lucky we are to be here. So let's stop for a second and pull back again let's pull way, way, way back.

ACTOR 2: Life is so great that we only get a tiny moment to enjoy everything we see. And that moment is right now.

ACTOR 1: And that moment is counting down.

ACTOR 2: And that moment is always, always fleeting.

ACTOR 1: You will never be as young as you are right now.

ACTOR 2: Let’s all high five and keep thinking wild thoughts, dreaming big dreams, and laughing loud laughs.

BOTH: AWESOME!
```

---

## IC-0491: The Brave Little Toaster

- Title: The Brave Little Toaster
- Author (byline): Thomas M. Disch
- Work: Not specified
- Publisher: Doubleday and Company
- Publication date as stated: April 1986
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR 1, NARRATOR 2, TOASTER, VACUUM, BLANKET, LAMP, RADIO, SQUIRREL, BOAT OWNER, MISTRESS
- Teaser before the introduction: Yes
- Spoken words (computed): 1485
- Already set (do not supply): none

### Source block (context only)

```text
Author: Thomas M. Disch
ISBN: 978-0385237383
Publisher: Doubleday and Company
Date (Month/Year): April 1986
```

### Introduction (context only: never use it for content warnings)

```text
Actor 1: You would think that in being a talking appliance you would not have anything to worry about.

Actor 2: Unfortunately for these five friends that is not the case.

Actor 1: They have been left to fend for themselves in the wilderness by their now “grown up” master.

Actor 2: As they set out into the world to try and find him they find adventure, ghosts, and what kind of wiring they are truly made of.

TOGETHER: The Brave Little Toaster by Thomas M. Disch
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

(Division of characters and narration duties should be equally divided between the actors – However, each actor should maintain character consistency throughout: If you start out as the TOASTER, always be the TOASTER)

NARRATOR 1: They lived in a cottage, deep in a forest unreachable by civilization. They were very devoted to their master -- that was just their nature as appliances.

NARRATOR 2: There was an old vacuum, the leader (I’m a Hoover).

NARRATOR 1: The off white plastic alarm clock radio (AM only),

NARRATOR 2: A cheerful yellow electric blanket (wanna cuddle?)

NARRATOR 1: And a neurotic tensor lamp (“I’m the outsider I have no friends)

NARRATOR 2: Finally, there was the toaster, a bright little Sunbeam (cute little “hi”).

NARRATOR 1: But living so long in the woods had changed them in some nice, indefinable way that made the thought of any alternate lifestyle unthinkable . . .

NARRATOR 2: Or so they thought!

TOASTER: We can’t go on like this; it isn’t natural for appliances to live all by themselves. We need people to take care of; we need people to take care of us. Soon one by one we will all ware out and no one will fix us because no one will know what has happened to us. There’s nothing else to do but to find the master.

VACUUM: The toaster’s right, something must be done. Do you have any suggestions?

TOASTER: Don’t you remember just last week there was a story that the radio was telling us about a dear little fox terrier who had been accidentally left behind at a cottage just like us. And found his master thousands of miles away in a city somewhere in Canada.

BLANKET: That’s it that’s how we’ll find our way! But dogs have legs.

TOASTER: The vacuum shall be our legs!

VACUUM: I beg your pardon?

TOASTER: I meant to say our wheels.

LAMP: And build a kind of carriage!

RADIO: And ride all the way there!

TOASTER: The question is…will you be able to? (Vacuum rumbles)

NARRATOR 1: One Friday, the Hoover as usual, had been grumbling about the old metal wheelie chair that stood in front of the Master’s desk. The toaster had an idea.

NARRATOR 2: They tied the Hoover’s cord to the base of the chair and hopped on. They set out to find their master as the Hoover pulled them along. Soon the dear little summer cottage was lost from sight behind the leaves and branches of the forest trees.

NARRATOR 1: As the day worn on the Hoover was obliged to stop more and more frequently.

VACUUM: Can you believe how filthy the forest is?

BLANKET: On the contrary, it’s thoroughly agreeable. The air’s so fresh, and just the feel the breeze! I feel renewed, as if I’d just come out of my box. Oh why, why, why don’t they ever take electric blankets on picnics? It isn’t fair!

RADIO: Enjoy it while it lasts, kiddo. According to the latest weather and traffic roundup, we’re in for rain.

LAMP: Won’t the trees act like a roof? They keep the sunlight out well enough.

NARRATOR 1: None of them knew the answer to the lamps question, but as it happens, trees do not work like a roof. And it started to rain.

NARRATOR 2: The electric blanket spread out and sheltered the other four appliances. Later the toaster woke from a terrible nightmare. Thunder was thundering and lightning was streaking the sky. With Dismay the toaster realized that the electric blanket had disappeared.

LAMP: Where’s the blanket?

RADIO: Blown away, blown off to the far end of the forest.

LAMP: I should have known I should have known, we should have never left home.

VACUUM: It’s not our fault.

NARRATOR 1: In a flash of lightning they saw the blanket tangled in a tree.

TOASTER: BLANKEEEEEEEEEE….t.

RADIO: You can come down now!

BLANKET: I can’t I’m stuck.

VACUUM: Don’t be a wet blanket

BLANKET: I can’t get down, There’s a great rip right through the center of me. I hurt.

SQUIRREL: “What the deuce is all the racket about.”

NARRATOR 2: Spoke a squirrel stepping forward from his nest high in the trunk of the oak. The appliances apologized and with the help of the squirrel they got blanket down (Squirrel and blanket interaction).

TOASTER: How shall we ever be able to repay you?

SQUIRREL: Well, I can’t remember whether or not you said you were nuts, I mean if you had any nuts.

VACUUM: Believe me, if we did you would have them all. But you can see for yourself that my bag contains nothing but dust (empty hoover)

NARRATOR 1: And they continued on their way. And what a long and wary way it was! (pantomime section)

NARRATOR 2: Toward evening…

RADIO: I’m receiving interference from a source quite nearby. Just on the other side of that river.

LAMP: Hurrah! (appliance dance) –hits boat—AHHHH! I’ve found a boat!

VACUUM: You don’t intend for us to use the boat, do you?

TOASTER: Of course! This will take us directly across the river.

BLANKET: It doesn’t belong to us. If we were to take it, we’d be no better than…than pirates!

RADIO: Pirates! Us? Who ever heard of an appliance that was a pirate?

TOASTER: We wouldn’t keep it. We’d just borrow it.

NARRATOR 1: With courage renewed and determination strengthened they set out. BUT! Something made it stop. The owner of the boat had returned.

BOAT OWNER: Why what’s this? It seems we have some visitors!

NARRATOR 1: He said so much more than this, but in a manner so rough and ill mannered that it is better not to repeat his words verbatim. The sum of it was- the owner of the boat believed the owner of the appliances had been about to steal his boat, and so he intended by way of retaliation to steal the appliances, and brought them to the city dump!!!!

BOAT OWNER: It’s junk…all of it.

RADIO: It’s true.

BLANKET: That’s all I am now—junk! Look at me!

LAMP: My bulb! My poor, poor bulb!

VACUUM: This is where I belong…

TOASTER: Pull yourselves together, all of you! There’s nothing wrong with us! Now here is my plan. We’ll frighten him, and that will make him run away.

LAMP: But what if the gate is locked? It is now!

TOASTER: No, because he will have to unlock it to get out himself, and he’ll be too frightened to remember to lock it behind him.

RADIO: It’s a very good plan, but what I don’t understand is—how we are going to frighten him?

TOASTER: Well, what are people afraid of the most?

VACUUM: Getting run over by a steamroller

TOASTER: No, scarier than that.

BLANKET: Moths

TOASTER: No, they are afraid of ghosts.

BLANKET: What are ghosts?

TOASTER: Ghosts are people who are dead, only they’re also sort of alive.

VACUUM: Don’t be silly, either they are dead or they aren’t.

BLANKET: Yes, it’s as simple as on and off. If you are turned on you can’t be turned off.

TOASTER: The point is this—people are afraid of ghosts. And so we’re going to pretend to be one.

VACUUM: How?

TOASTER: Let me show you.

NARRATOR 2: After an hour’s practice of pretending to be a ghost, they decided they were ready. The blanket draped over the vacuum in a roughly ghostlike shape with a kind of hood at the top through which the toaster was able to peer out, adjusted its folds one last time.

TOASTER: Ready?

VACUUM: Ready.

BLANKET: Ready.

TOASTER: Then let’s start haunting.

TOASTER: Whoo!

BOAT OWNER: Who’s there?

TOASTER: Whoo—oo!

BOAT OWNER: Whoever you are, you’d better go away.

TOASTER: Whoo—oo—oo!

BOAT OWNER: If you won’t say who you are, I’m going to come out there and find out!

TOASTER: WHOOOOOOOO!

BOAT OWNER: I’m warning you! (Toaster comes around, scares owner “AHHHHH!!!” run around in circle)

NARRATOR 1: They then drove off as fast as their wheels would revolve. As luck would have it, they didn’t have far to go: where the master lived on Newton Avenue was only a mile or so from the dump. They reached his apartment building early in the morning

TOASTER: You see, in the end everything really does work out for the best.

NARRATOR 1: Alas their tribulations were not yet at an end, and not everything…would work out for the best. When they reached the apartment they were greeted by the “new” appliances who informed the five friends that the master means to sell the cottage in the woods and auction them off.

TOASTER: Come all of you come. We are not wanted here. We’ll return…to…

BLANKET: The Dump…

RADIO: No…there’s another way.

NARRATOR 2: The next afternoon at five o’clock the radio’s alarm went off, and everyone became very silent.

BLANKET: What is it?

RADIO: Hush. It’s time for the swap shop. It’s a program on listener radio station KHOP! That is going to find a new home for us! I told you not to worry, didn’t I? I told you I’d think of something?

(mumbo jumbo radio announcer)

RADIO: Didn’t he make us sound super! Come over here by the telephone.

NARRATOR 1: All of the appliances gathered about the telephone and waited for it to ring. (The phone rings).

VACUUM: Now whatever you do don’t say yes to the first person who happens to call. Find out something about him first.

RADIO: Right.

TOASTER: And remember to be nice.

RADIO: Hello?

MISTRESS: Is this the person with five appliances?

RADIO: It is! Oh my goodness yes indeed it is!

NARRATOR 1: And so the appliances went to live with their new mistress, for as it happened it was a woman who’d phoned them first and not a man. The appliances were very happy.

NARRATOR 2: It felt so good to be useful again!

NARRATOR 1: And so the five appliances lived and worked happy and fulfilled, serving their dear mistress and enjoying each other’s companionship, to the end of their days.

TOASTER: You see, in the end…everything really does work out for the best.
```

---

## IC-0492: The Butter Battle Book

- Title: The Butter Battle Book
- Author (byline): Theodore Geisel (aka Dr. Seuss)
- Work: Not specified
- Publisher: Random House, Inc.
- Publication date as stated: March 1984
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: GRANDSON, GRANDFATHER, CHIEF YOOKEROO, VANITCH, CROWD, RIGHT-SIDE-UP-SONG-GIRL, VOICE, MIZ YOOKIE-ANN SUE, GRANSFATHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1451
- Already set (do not supply): none

### Source block (context only)

```text
Author: Theo Geisel (aka Dr. Seuss)
ISBN: 978-0394865805
Publisher: Random House, Inc.
Date (Month/Year): March 1984
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: The pettiness behind the conflict of the Cold War is Dr. Seuss's vehicle for conveying the astounding destructive potential behind a war where the enemies lose sight of their true goals and meaninglessly try to "out do" each other.

ACTOR 2: The “war” ends up being fought for the wrong reasons and becomes something that we will forever regret.

ACTOR 1: While the arms race between the United States and Russia no longer exists, The Butter Battle Book by Theodore Geisel (aka Dr. Seuss) still explores the important issue of escalating violence

ACTOR 2: And the "an eye-for-an-eye" mentality that not only exists at an international level but also in the cities, schoolyards, and homes of some to this day.

TOGETHER: The Butter Battle Book by Theodore Geisel (aka Dr. Seuss)
```

### Performance text (classify this)

```text
Suggested Roles: Actor 1 – Grandson Actor 2 – All other parts

NOTE: This cutting asks one student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

GRANDSON: On the last day of summer, ten hours before Fall . . . my grandfather took me out to the wall. For a while he stood silent. Then finally he said, with a very sad shake of his very old head,

GRANDFATHER: As you know, on this side of the Wall we are Yooks. On the far other side of this Wall live the Zooks.

GRANDSON: Then my grandfather said,

GRANDFATHER: It’s high time that you knew of the terribly horrible thing that Zooks do. In every Zook house and in every Zook town every Zook eats his bread with the butter side down! But we Yooks, as you know, when we breakfast or sup, spread our bread,

GRANDSON: Grandpa said,

GRANDFATHER: with the butter side up. That’s the right, honest way!

GRANDSON: Grandpa gritted his teeth.

GRANDFATHER: So you can’t trust a Zook who spreads bread underneath! Every Zook must be watched! He has kinks in his soul!

GRANDSON: That’s why, as a youth, I made watching my goal, watching Zooks for the Zook-Watching Border Patrol! In those day, of course, the Wall wasn’t so high, and I could look any Zook square in the eye. If he dared to come close I could give him a twitch with my tough tufted prickely Snick-Berry Switch.

GRANDFATHER: For a while that worked fine. All the Zooks stayed away and our country was safe.

GRANDSON: Then one terrible day a very rude Zook by the name of VanItch snuck up and slingshotted my Snick-Berry Switch! With my broken- off switch, with my head hung in shame, to the Chief Yookeroo in great sorrow I came. But our leader just smiled. He said,

CHIEF YOOKEROO: You’re not to blame. And those Zooks will be sorry they started this game. “We’ll dress you right up in a fancier suit! We’ll give you a fancier slingshot to shoot!

GRANDSON: And he ordered the Boys in the Back Room to figger how to build me some sort of triple-sling jigger. With my Triple-Sling Jigger I sure felt much bigger. I marched to the Wall with great vim and great vigor, right up to VanItch with my hand on the trigger. “I’ll have no more nonsense,” I said with a frown, “from Zooks who eat bread with the butter side down!”

GRANDFATHER: VanItch looked quite sickly. He ran off quite quickly.

GRANDSON: I’m unhappy to say he came back the next day in a spiffy new suit with a big new machine, and he snarled as he said, looking frightfully mean,

VANITCH: You may fling those hard rocks with your Triple-Sling Jigger. But I, also, now have my hand on a trigger! “My wonderful weapon, the Jigger-Rock Snatchem, will fling ‘em right back just as quick as we catch ‘em. We’ll have no more nonsense. We’ll take no more gupp from you Yooks who eat bread with the butter side up!

GRANDSON: “I have failed, sir,” I sobbed as I made my report to the Chief Yookeroo in the headquarters fort. He just laughed.

CHIEF YOOKEROO: You’ve done nothing at all of the sort. Our slingshots have failed. That was old-fashioned stuff. Slingshots, dear boy, are not modern enough. All we need is some newfangled kind of gun. My Boys in the Back Room have already begun to think up a walloping whiz-zinger one! My Bright Boys are thinking. They’re on the right track. They’ll think one up quick and we’ll send you right back!

GRANDFATHER: They thought up a great one! They certainly did. They thought up a gun called the Kick-a- Doo Powder and ant’s eggs and bees’ legs and dried-fried clam chowder. And they carefully trained a real smart dog named Daniel to serve as our country’s first gun-toting spaniel.

GRANDSON: Then Daniel, the Kick-a-Poo Spaniel, and I marched back toward the Wall with our heads held up high while everyone cheered and their cheers filled the sky;

CROWD: “Fight! Fight for the Butter Side Up! Do or die!”

GRANDSON: Well . . . We didn’t do. And we didn’t quite die. But we sure did get worsted, poor Daniel and I. VanItch was there too! And he said, the old pig,

VANITCH: The Boys as in my Back Room invented this rig called the Eight-Nozzled, Elephant-Toted Boom- Blitz. It shoots high-explosive sour cherry stone pits and will put your dumb Kick-a-Poo Kid on the fritz!

GRANDSON: Poor Daniel and I were scared out of our witz! Once more, by VanItch I was bested and beat. Once again I limped home from the Wall in defeat. I dragged and I sagged and my spirits were low, as low as I thought that they ever could go, when I heard a Boom-Bah! And a Diddle-dee-Dill! And our Butter-Up Band marched up over the Hill! The Chief Yookeroo had sent them to meet me along with the Right-Side-Up Song Girls to greet me. They sang:

RIGHT-SIDE-UP-SONG-GIRL: “Oh, be faithful! Believe in thy butter!”

GRANDSON: And they lifted my spirits right out of the gutter!

CHIEF YOOKEROO: My boy,

GRANDSON: smiled the Chief Yookeroo,

CHIEF YOOKEROO: we’ve just voted and made you a general! You’ve been promoted. Your pretty new uniform’s ready. Get in it! The Big War is coming. You’re going to begin it! And what’s more, this time you are certain to win it. My Boys in the Back Room have finally found how. Just wait till you see what they’ve puttered up now! In their great new machine you’ll fly over that Wall and clobber those Butter- Down Zooks one and all!

GRANDSON: Those Boys in the Back Room sure knew how to putter! They made me a thing called the Utterly Sputter and I jumped aboard with my heart all aflutter and steered toward the land of the Upside-Down Butter.

GRANDFATHER: This machine was so modern, so frightfully new, no one knew quite exactly just what it would do!

GRANDSON: But it had several faucets that sprinkled Blue Goo which, somehow, would sprinkle the Zooks as I flew and gum up that upside-down butter they chew. I was racing pell-mell when I heard a voice yell,

VOICE: If you sprinkle us Zooks, you’ll get sprinkled as well!

GRANDSON: VanItch had a Sputter exactly like mine! And he yelled,

VANITCH: “My Blue-Gooer is working just fine! And I’m here to say that if Yooks can goo Zooks, you’d better forget it. ‘Cause Zooks can goo Yooks!

GRANDSON: I flew right back home and, as you may have guessed, I was downright despondent, disturbed, and depressed. And I saw, just as soon as I stepped back on land, so were all of the girls of the Butter- Up Band. The Chief Drum Majorette, Miz Yookie-Ann Sue, said,

MIZ YOOKIE-ANN SUE: That was a pretty sour flight that you flew. And the Chief Yookeroo has been looking for you!

GRANDSON: I raced to his office. The place was a sight.

CHIEF YOOKEROO: Have no fears,

GRANDSON: said the Chief.

CHIEF YOOKEROO: “Everything is all right. My Bright Back Room Boys have been brighter than bright. They’ve thought up a gadget that’s Newer than New. It is filled with mysterious Moo-Lacka-Moo and can blow all those Zooks clear to Sala-ma-goo. THEY’VE INVENTED THE BITSY BIG-BOY BOOMEROO! “You just run to the wall like a nice little man. Drop this bomb on the Zooks just as fast as you can. I have ordered all Yooks to stay safe underground while the Bitsy Big-Boy Boomeroo is around.

GRANDSON: As I raced for that Wall, with the bomb in my hand, I noticed that every last Yook in our land was obeying our Chief Yookeroo’s grim command.

GRANDFATHER: They were all bravely marching, with banners aflutter, down a hole! For their country! And Right-Side-Up Butter!

GRANDSON: That’s when Grandfather found me! He grabbed me. He said,

GRANDFATHER: You should be down that hole! And you’re up here instead! But perhaps this is all for the better, somehow. You will see me make history! RIGHT HERE! AND RIGHT NOW!

GRANDSON: Grandpa leapt up that Wall with a lopulous leap and he cleared his harse throat with a bopulous beep. He screamed,

GRANDFATHER: Here’s the end of that terrible town full of Zooks who eat bread with the butter side down!

GRANDSON: And at the very instant we heard a klupp-klupp of feet on the Wall and old VanItch klupped up! The Boys in HIS Back Room had made him one too! In his fist was another Big-Boy Boomeroo!

VANITCH: I’ll blow you,

GRANDSON: he yelled,

VANITCH: into pork and wee beans! I’ll butter-side-up you to small smithereens!

GRANDSON: “Grandpa!” I shouted. “Be careful! Oh, gee! Who’s going to drop it? Will you . . . ? Or will he . . . ?

GRANSFATHER: Be patient,

GRANDSON: said Grandpa.

GRANDFATHER: We’ll see. We will see . . .
```

---

## IC-0493: Channel Changers

- Title: Channel Changers
- Author (byline): Wayne Rice and Mike Yaconelli
- Work: The Greatest Skits on Earth
- Publisher: Zondervan
- Publication date as stated: March 1986
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1963
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
ACTOR 1: Let’s admit it . . . We’re always searching for something better: Something nicer, faster, newer, shinier, bigger. Something more. Something else.

ACTOR 2: The remote control made this search easier than ever: you can navigate a thousand channels without leaving your couch, flipping endlessly through channel after channel after channel until you find something better.

ACTOR 1: But television isn’t the only place in which we constantly search for something better: we flip through every aspect of our lives—food, relationships, radio stations, work—all the while looking for anything other than what’s in front of us.

ACTOR 2: The problem is, in a world of unlimited choices, there actually is always something better somewhere.

TOGETHER: Channel Changers by Wayne Rice and Mike Yaconelli
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

The following three scripts all follow the same format. The idea is to demonstrate what might happen if you flipped back and forth between several different programs or channels on your radio or television set. Each "click" in the script is a channel change and should be presented by the actors in an alternating sequence without regard to the character listed. Use your own creativity, add your own lines, and have fun with these.

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

Announcer: ... football field. That should do it for the Wildcats, folks. With Brooks out of the game, it doesn't look like they have a chance. Now they line up.

The snap. Draw play! What a hand-off. There goes Johnson! Look at him go. He's going all the way to the ... ( click)

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

Sesame Street: ... garbage can. Children, the Cookie Monster has always wanted to ... (click)

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

Indy: He blew a tire! He's spilling oil all over the track. Tell the clean-up crew to ... (click)

Health: Drink it all up! It's great for hair, bones, skin, and ... (click)

Sesame Street: ... counting by twos. It's really not that hard. We've' found that many children out there are ... (click)

Gangster: ... holding my wife for ransom. Those lousy rats! I wouldn't give them ...

(click)

Grocer: ... rotten eggs! You won't find them here. Our eggs are the finest you'll find in any ... (click)

Indy: ... gas tank! It looks like a bad leak. Yes, the gas is going all over his ...

(click)

Health: Leotards. They are so comfortable, I wouldn't exercise without them. You _might also buy ... (click)

Sesame Street: ... huge shoes for those webbed feet. It's not often we have a duck on our ... (click)

Gangster: ... pizza! Yeah, I got to eat and run. Charlie, don't forget to line up the ...

(click)

Grocer: ... tomatoes in a perfect row. In our meat section yesterday, we caught a man eating a ... (click)

Indy: ... checkered flag! And that's all, folks!
```

---

## IC-0494: Charlie and the Chocolate Factory

- Title: Charlie and the Chocolate Factory
- Author (byline): Roald Dahl
- Work: Not specified
- Publisher: Puffin Books
- Publication date as stated: Aug 1983
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 1, ACTOR 2, CHARLIE, GPA JOE, WONKA, NARRATOR 1, AUGUSTUS’ MOM, VERUCA’S DAD, VERUCA, WORKER, GMA JOSEPHINE, GMA GEORGINA, NEWSPAPER BOY, VIOLET, NARRATOR 2, SHOPKEEPER, CROWD MEMBER, AUGUSTUS, AGUSTUS’ MOM, GPJOE
- Teaser before the introduction: Yes
- Spoken words (computed): 1719
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
ACTOR 2: Some things never change.

ACTOR 1: In 1964 when Charlie and the Chocolate Factory was first published, the greatest thing imaginable was gallivanting around a factory devoted entirely to making chocolate and other sweets.

ACTOR 1: And guess what? Over half a century later, that’s still the greatest thing imaginable!

ACTOR 2: AND The willy Wonka Candy Company actually exists!

ACTOR 1: Laffy Taffy,

ACTOR 2: Wonka Bars and…

ACTOR 1: Everlasting Gobstoppers!

ACTOR 2: Follow us to a world of pure imagination . . .

TOGETHER: Charlie and the Chocolate Factory by Roald Dahl
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles: This is cast as non-gender specific – Any gender can plan any role. Pronouns when used remain true to the text.

ACTOR 1: Charlie, Narrator 1, Augustus’ Mom, Veruca, Worker, Grandma Josephine, Violet, Crowd Member

ACTOR 2: Grandpa Joe, Wonka, Veruca’s Dad, Grandma Georgina, Newspaper Boy, Narrator 2, Shopkeeper, Augustus

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

## IC-0495: Choices

- Title: Choices
- Author (byline): James McLindon
- Work: The Best New Ten-Minute Plays 2020, Pg 39
- Publisher: Applause Theatre and Cinema Books
- Publication date as stated: Oct 2020
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: PROSPECTIVE CLIENT, DEBT COUNSELOR
- Teaser before the introduction: No
- Spoken words (computed): 1371
- Already set (do not supply): none

### Source block (context only)

```text
Author: James McLindon
Book: The Best New Ten-Minute Plays 2020, Pg 39
ISBN: 978-1493053278
Publisher: Applause Theatre and Cinema Books
Date (Month/Year): Oct 2020
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: According to the Federal Reserve Bank of New York, in 2020 student loan debt reached an all-time high,

ACTOR 2: Nearly $1.6 trillion among more than 40 million Americans, making the Department of Education the country's biggest consumer lender.

ACTOR 1: Furthermore, according to the U.S. Department of Education, about 1 in every 5 borrowers are in default.

ACTOR 2: Student loan debt is out of control.

ACTOR 1: Heck, there’s even a television trivia game show called Paid Off with Michael Torpey where the winner has the chance to win the sum of their student debt in cash.

ACTOR 2: We have entered the theatre of the absurd . . .

ACTOR 1: But James McLindo,n in his short play Choices, takes it one step further.

TOGETHER: Choices by James McLindon

(Pg 39 – 46) A modest living room (think poor graduate student), the present. The PROSPECTIVE CLIENT sits at her/his coffee (or dining room) table across from the DEBT COUNSELOR, who has the calmness and patience of a funeral home director for the most part, there to help and alert to steer clear of any heaviness with a ready euphemism. All of that is underlaid with an enthusiastic love of her/his product. The PROSPECTIVE CLIENT is a little anxious, really needing this to work. The DEBT COUNSELOR has been waiting for the PROSPECTIVE CLIENT to finish reading a pamphlet. The PROSPECTIVE CLIENT now looks up, perplexed.
```

### Performance text (classify this)

```text
PROSPECTIVE CLIENT: I'm sorry, I just don't get it.

DEBT COUNSELOR: It's pretty simple. It's just ... disruptive.

PROSPECTIVE CLIENT: No, I know, it sounds simple ....

DEBT COUNSELOR: Think of it as a choice. We're all about choices. You can choose this. Or not.

PROSPECTIVE CLIENT: No, no, I want to choose this, believe me. I feel like I'm on a hamster wheel just trying to keep up with the payments, but ... this just seems too good to be true.

DEBT COUNSELOR: That's often what disruption looks like. Remember all the things you used to have to pay to read, like newspapers, magazines? Now you get them on-line for free. We're disrupting the entire debt consolidation industry, sort of like that.

PROSPECTIVE CLIENT: Okay, but ... I still don't get it.

DEBT COUNSELOR: Tell me what you don't get.

PROSPECTIVE CLIENT: So, you pay off my student loans...

DEBT COUNSELOR: Your crushing student loans.

PROSPECTIVE CLIENT: Yes, thank you, my 247,000 dollars in student loans, and all I have to do is pay you seventy-two dollars a month?

DEBT COUNSELOR: Yes.

PROSPECTIVE CLIENT: For twenty years.

DEBT COUNSELOR: Yes.

PROSPECTIVE CLIENT: And that's it. That's all I ever have to pay you.

DEBT COUNSELOR: That's all you ever have to pay us. (The PROSPECTIVE CLIENT calculates in her/his head.)

PROSPECTIVE CLIENT: Okay, so I'm not really great at math, but I think that's only, like, $170,000?

DEBT COUNSELOR: It's actually about $17,000.

PROSPECTIVE CLIENT: Only 17,000 dollars!? Okay, now I don't get this even more.

DEBT COUNSELOR: Tell me what you don't get.

PROSPECTIVE CLIENT: What don't I...? You give me 247,000 dollars to pay off my debt today and all I have to give you is 17,000 dollars over twenty years?

DEBT COUNSELOR: Right. Mainly to keep you focused.

PROSPECTIVE CLIENT: So you lose money.

DEBT COUNSELOR: No ...

PROSPECTIVE CLIENT: Yeah, you lose money. Nobody sets up a business to lose money, unless they're, like, money laundering or something. Wait, are you guys money laundering?

DEBT COUNSELOR: No.

PROSPECTIVE CLIENT: What are you doing?

DEBT COUNSELOR: We're providing choices. (Pause.) I think maybe you skipped footnote seven.

PROSPECTIVE CLIENT: I didn't read the footnotes.

DEBT COUNSELOR: You should read the footnotes.

PROSPECTIVE CLIENT: I never do.

DEBT COUNSELOR: You always should.

PROSPECTIVE CLIENT: Okay, fine, what does footnote seven say?

DEBT COUNSELOR: It answers this question.

PROSPECTIVE CLIENT: About whether you're money laundering?

DEBT COUNSELOR: About how we get paid. (Beat.)

PROSPECTIVE CLIENT: So how do you? I mean, after I finish my payments you'll be short about 230,000 dollars. Not to mention any interest. So where do you get the rest (from) ... ? Oh, there're a bunch of hidden fees, aren't there?

DEBT COUNSELOR: There are no fees at all.

PROSPECTIVE CLIENT: Then c'mon, how do you get your money back from me?

DEBT COUNSELOR: We don't get it back from you.

PROSPECTIVE CLIENT: You don't?

DEBT COUNSELOR: We don't. (Pause.) From you.

PROSPECTIVE CLIENT: Who do you get it back from?

DEBT COUNSELOR: The insurance company.

PROSPECTIVE CLIENT: What insurance company?

DEBT COUNSELOR: You should really read footnote seven ...

PROSPECTIVE CLIENT: Just tell me, what insurance company!?

DEBT COUNSELOR: Your insurance company.

PROSPECTIVE CLIENT: Why would my car insurance company pay you?

DEBT COUNSELOR: Not your car insurance company.

PROSPECTIVE CLIENT: Well, that's the only insurance I have. I sure don't have homeowners because you can't afford to buy a house when you owe $247,000 ...

DEBT COUNSELOR: Your life insurance company. (Beat.)

PROSPECTIVE CLIENT: I don't have life insurance.

DEBT COUNSELOR: Footnote seven.

PROSPECTIVE CLIENT: I have to get life insurance?

DEBT COUNSELOR: We pay for it.

PROSPECTIVE CLIENT: What good does life insurance do anyone?

DEBT COUNSELOR: It depends.

PROSPECTIVE CLIENT: Unless I die.

DEBT COUNSELOR: Read footnote seven.

PROSPECTIVE CLIENT: Oh my God. You've looked at my DNA! You have, you totally have! That DNA company that said I was 2.3% Neanderthal sold you my data and you looked at it and you know I have a genetic abnormality and I'm going to die young, so that's how you ... What are you writing down?

DEBT COUNSELOR: No, please, go on, that's a really interesting business model.

PROSPECTIVE CLIENT: Stop it! That's not your business model?

DEBT COUNSELOR: No, but it's pretty good though. Way disruptive.

PROSPECTIVE CLIENT: So I'm not going to die in the next twenty years?

DEBT COUNSELOR: Well, how would I know that?

PROSPECTIVE CLIENT: There's no DNA stuff in your file on me?

DEBT COUNSELOR: All we have is what you gave us.

PROSPECTIVE CLIENT: (Exhaling.) I'm not going to die young.

DEBT COUNSELOR: Well, not in the next twenty years. As far as I know.

PROSPECTIVE CLIENT: Do you qualify everything you say?

DEBT COUNSELOR: When it needs to be. Because we're totally honest. With our clients.

PROSPECTIVE CLIENT: So how do you make money from my life insurance?

DEBT COUNSELOR: How does anyone make money from life insurance?

PROSPECTIVE CLIENT: Somebody has to die. (Pause.) But you just said I wouldn't!

DEBT COUNSELOR: I said I don't know anything about your DNA. Or your health at all for that matter. We don't worry about that. Please. Read footnote seven.

(PROSPECTIVE CLIENT stares at DEBT COUNSELOR, who stares back. A beat.) Please.

PROSPECTIVE CLIENT: Okay, fine. (PROSPECTIVE CLIENT returns to reading the pamphlet. Then PROSPECTIVE CLIENT looks up at DEBT COUNSELOR, stunned.) Oh my god!

DEBT COUNSELOR: (Excited for the first time.) I know, right!? The first time I read it, I was like, Whaaaaat!? But the more you think about it, the more genius it is. Dis! Effing! Ruption! Amiright!? (Catching himself, quieting.) Sorry. I just love this product so much.

PROSPECTIVE CLIENT: I'm not going to agree to this! Does anyone ever agree to this?

DEBT COUNSELOR: No. (Pause.) Not at first. But then they think about it. And they think, well, when I took out my crushing student loans, I knew that they would impact my life. Severely impact my life. For a whole lot of my life. Decades and decades. And see, that's all this is really. You just assumed that the impact would be frontloaded. And all we do is ... backload it for you.

PROSPECTIVE CLIENT: Me dying at (whatever age is about twenty years older than actor) in twenty years, that's what you call "severely impacting" my life?

DEBT COUNSELOR: Well, it seems severe to me.

PROSPECTIVE CLIENT: No, it's severe, it's very severe!

DEBT COUNSELOR: Yes. But. What a much better life it will have been. These next twenty years anyway. Which, after all, is your prime.

PROSPECTIVE CLIENT: How do you ... you know...do it?

DEBT COUNSELOR: Do what?

PROSPECTIVE CLIENT: Make it so you get to, you know, collect. (Pause.)

DEBT COUNSELOR: Before we get into the details, I think it's best that you get comfortable with the concept (first) ...

PROSPECTIVE CLIENT: How!?

DEBT COUNSELOR: Well, it's up to you. See? Choices. Most people opt to handle matters themselves. We'll give you some recommendations and how-tos in the next brochure it's under "Self-Termination." A lot of people, though, find they're too ... squeamish? for Self-Term when push comes to shove and for them we offer Appointment Service. You know how you can schedule a caesarian these days? Well, this is sort of ...

PROSPECTIVE CLIENT: The exact opposite.

DEBT COUNSELOR: Yes. The App Serv team is excellent, guaranteed painless and they can make anything look like an accident. And finally, there are some people who are squeamish, but who also find that having an actual appointment makes them ...

PROSPECTIVE CLIENT: Freaking terrified?

DEBT COUNSELOR: Mmm, anxious. For them we offer a third approach, a service where you just go about your business and we ... take it from there. That one's called Dealer's Choice. (Pause.) You don't have to decide that now.

PROSPECTIVE CLIENT: A lot of people must just run when their time is up.

DEBT COUNSELOR: Oh, people are surprisingly ethical about it. Also, we implant a chip that sends us your GPS coordinates.

PROSPECTIVE CLIENT: What if I dig the chip out?

DEBT COUNSELOR: We don't put it anywhere too ... accessible? And if you did get it out, we always have the Recovery Team.

PROSPECTIVE CLIENT: The chips are that valuable?

DEBT COUNSELOR: You're that valuable. You know how the Coast Guard has rescue and recovery units. This is more recovery and ... not rescue. (Beat.) You can always say no. We're all about choices. (Suddenly, the DEBT COUNSELOR has an edge, a subtle darkness. Maybe there's a lighting change for his/her next speech.) Quantity or quality. You can live in your run-down studio apartment if you want. With a roommate. And drive a fifteen-year-old beater. And eat ramen noodles. And never take a decent vacation. And waste a lot of your life living on the shoulder of poverty.

PROSPECTIVE CLIENT: Or I can have only twenty years left.

DEBT COUNSELOR: Twenty debt-free years to keep and spend your money. To travel, buy a house, have a life, whatever that means to you. And do you really want to live longer than that?

PROSPECTIVE CLIENT: My parents got to.

DEBT COUNSELOR: But do you want to? With the rising tides of climate change lapping at your ankles and blowing down your little garret. With the last shreds of our democracy fraying before your eyes, while the old-world order collapses. I don't think it's too much to say that the ones who choose to go with us are in many ways the lucky ones. (Pause; brighter again.) Hey, it's a big decision, so you take your time, talk to your friends, your family. And if you do choose to go with us, just give me a call. (The DEBT COUNSELOR hands the PROSPECTIVE CLIENT a card, shakes hands, and begins to leave.)

PROSPECTIVE CLIENT: Wait. Are ... are you a client? (The DEBT COUNSELOR turns back, smiles and pulls up his/her shirt.)

DEBT COUNSELOR: There's my GPS scar. Take a look around on the beach this summer. You'll be surprised. (Smiling.) Call me. (Exits.)

(The PROSPECTIVE CLIENT looks at the card, snorts in derision, throws it in the trash can, then sits down and thinks for a few moments. She/he picks the trash can up, starts to reach in to remove the card, and then stops. Still holding the can, she/ he looks up, uneasy, thinking.)
```

---

## IC-0496: Cinderella Wore Combat Boots

- Title: Cinderella Wore Combat Boots
- Author (byline): Jerry Chase
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Jan 1998
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: KING, PRINCE, GODZELLA, MAZZARELLA, TOGETHER, CINDERELLA, MAZARELLA, MAZARRELLA, M & G, FGP, CINDERELLA & PRINCE
- Teaser before the introduction: Yes
- Spoken words (computed): 1799
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jerry Chase
ISBN: 978-0822202134
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
TOGETHER: Cinderella Wore Combat Boots by Jerry Chase
```

### Performance text (classify this)

```text
Suggested Roles:

Actor 1: King, Godzella, Cinderella Actor 2: Prince, Mazzarella, Fairy God-Person

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

KING: Hello! I’m King Charming. This is a wonderful kingdom and I am a wonderful King. But I do have one big problem – my son! My son will be King one day, but he won’t settle down and take any responsibilities. All he does is hunt dragons. The only way we’ll get him to the altar is by draggin’ him there. Here. I’ll let you meet him. Son! Prince Charming!

PRINCE: Hi, dad! Ready for the dragon hunt?

KING: Knock it off, son. We’ve got to have a serious talk.

PRINCE: Okay . . .

KING: You’ve got to think about taking over the kingdom someday. After all, I’m not going to last forever – someday I’ll be gone and . . .

PRINCE: Dad! Don’t talk like that!

KING: No, son, it’s true. One day you will wear this crown. Here, try it now –

PRINCE: No! Dad, that’s yours. I couldn’t . . .

KING: Son, I command you to take it (Prince takes crown and puts it on) Now, how does that feel?

PRINCE: Hey! That feels pretty good!

KING: I’m not dead yet! You’ve got to start thinking about something besides dragons. It’s time you settled down –

PRINCE: But dad, I’m only thirty-eight!

KING: It’s time! You’ve got to start a social life. Meet some girls . . .

PRINCE: Aw, dad, girls have cooties . . . Right?

KING: Oh, shut up, Prince. Now listen; I’m going to throw a ball . . .

PRINCE: Okay, Dad. I’ll catch it!

KING: Not that kind of a ball, you doofus. A big party . . . with a band, lots of food . . . dancing . . . you’ll meet lots of girls . . .

PRINCE: Aw, Dad, do I have to?

KING: I proclaim a royal ball! All the maidens in the kingdom will be there. The Prince will dance with each and every one. And, the one he likes the best shall marry him and become the new Queen. I have spoken!

GODZELLA: Hi! I’m Godzella and I work hard at being beautiful. Of course, you’re wondering how I got this way. I don’t blame you. Well, I’ll tell you. It’s the right clothes, the right deodorant, and, of course, you must eat in the right restaurants. I think I’ll sit here and just be lovely.

MAZZARELLA: Hi! I’m Mazzarella, and I know what you’re thinking . . . if she’s that pretty, she must be dumb. But I’m not just pretty. Inside this head is just full of knowledge. I think I’ll sit with my mirror and gaze at how beautiful I am.

GODZELLA: Oh! I dropped my comb.

MAZZARELLA: She dropped her comb!

TOGETHER: Cinderella! Cinderella!

CINDERELLA: Yes, what can I do? I love to help.

GODZELLA: Cinderella, I dropped my comb. (looks to audience) She’s so slow and stupid.

MAZARELLA: She certainly is. Oh! I dropped my brush.

GODZELLA: She dropped her brush!

MAZARRELLA: Pick it up at once!

GODZELLA: Cinderella, you’ve fooled around enough cleaning the oven. Go clean the bathroom before you fix our lunch.

CINDERELLA: Yes, of course. Thank you.

GODZELLA: I wish I could have a new stepsister! Cinderella is so icky and skeevy.

MAZARELLA: Me too. I want one that’s slower and dumber than Cinderella because I love to nag and holler. (Knock, Knock, Knock)

M & G: Someone’s at the door! Cinderella! Cinderella!

CINDERELLA: It’s a messenger from the King.

M & G: Squeal! Squeal! A messenger from the King! Squeal! Squeal!

CINDERELLA: (reading message) Hear Ye! Hear Ye! The King is having a ball. (M & G squeal)All the maidens in the kingdom are summoned to the palace this very evening. Each and every maiden will dance with Prince Charming! (M & G squeal) And the one he likes the best will marry him and become the new Queen!!

GODZELLA: I’m gonna marry the Prince!

MAZZARELLA: I’m gonna be the Queen! We must get ready, Cinderella! Get my gowns and wigs and stuff.

GODZELLA: Cinderella! I need a perm, a nose job, and . . .

MAZZARELLA: Get me my platform shoes, my smelliest perfume, and don’t . . .

GODZELLA: I need my lifts, my props, my aids . . .

CINDERELLA: I hope I have time to get ready as well. . .

GODZELLA: (finally dressed and ready) Now I ask you . . . Could anyone resist?

MAZZARELLA: Put your money where your mouth is, Sisster. You had to put more make up on than a clown to look good.

M & G: Cinderella, call the carriage.

CINDERELLA: The carriage is called.

GODZELLA: What do you call that?

CINDERELLA: These are the clothes my real mother left me.

MAZZARELLA: And where do you think you’re going?

CINDERELLA: Why . . . to the ball. (M & G laugh)

GODZELLA: Cinderella, don’t be ridiculous! You’re too dirty and stupid to go to the ball. Suppose the Prince saw you and found out we knew you. You’d spoil our changes to marry the Prince.

MAZZARELLA: You must stay here and clean the fireplace, and beat the rugs and slop the pigs . . . or is it slop the rugs and beat the pigs? Oh, well, it doesn’t matter . . . Come sister, our carriage awaits. (Stepsisters leave. Cinderella starts crying. Fairy God-Person appears)

FAIRY GOD-PERSON (FGP): Dear, what could possibly be wrong?

CINDERELLA: My stepsisters went to the ball without me. Who are you?

FGP: I’m your fairy god-person. I’ll always come to help you if you really need me.

CINDERELLA: But how can you help me? I’m too dirty and ugly and dim-witted . . . I’d ruin my sister’s changes to marry the Prince.

FGP: Who told you those things?

CINDERELLA: My sisters.

FGP: I think you should go to the King’s party.

CINDERELLA: Oh, I couldn’t do that. Not looking like this. I don’t even have a dress to wear. Do you think a different dress would help?

FGP: Bibbity Bobbity Boo!

CINDERELLA: Hey! What’s happening! Wow! Look at this dress! I can go to the palace and see the people and everything . . . (looks at feet) Oh, Gee . . .

FGP: What’s the matter, dear?

CINDERELLA: I can’t go without shoes; all I have left are the combat boots my father left me.

FGP: Then by all means . . . wear them. You look great!

CINDERELLA: I don’t know how to thank you.

FGP: Your happy face is thanks enough. Go have a good time.

CINDERELLA: (starts then stops) Oh! (looks at floor)

FGP: What’s the matter, dear?

CINDERELLA: I’ll need money for the bus.

FGP: What’s the matter with me? You can’t go on the dirty, crowded bus in those clothes. Look out the window. What do you see?

CINDERELLA: You mean that pumpkin and those six white mice?

FGP: Bibbity Bobbity Boo! Now what do you see?

CINDERELLA: Hey! It’s a coach and six white horses!

FGP: Now are you ready to go to the ball. Wait! Don’t let me forget the most important thing! You must be home by midnight. That’s the time that all the magic disappears.

CINDERELLA: Oh, I’ll be home by then. I’m not going to dance or anything. I’m just going to look around, maybe take a few notes, and come right back.

FGP: Don’t forget the time! (to audience) Well! I bet the ball is in full swing. I wonder if everyone is having a great time . . . *****At the ball*****

PRINCE: Parties are a drag.

KING: (talking to a random woman) All right, honey, I’ll meet you by the buffet. (to Prince) Hi, son. Isn’t it a great party? Are you meeting all the maidens?

PRINCE: I’m working up to it.

KING: Hey! Here comes one now, son. She’s a real beauty. Okay, now, cool and suave, remember (to audience) You watch him . . . cool and suave.

GODZELLA: Wow! There’s the Prince. I’ll win him over. You just watch.

PRINCE: Hello.

GODZELLA: Hello? He said “hello.” (laughs) You’re funny. You wanna dance?

PRINCE: Yeah, sure.

GODZELLA: Hit it! (starts awkwardly fast dancing) Do you like dragons?

PRINCE: Yes, I do . . . I . . .

GODZELLA: Ohhhhh! That’s really funny. Don’t you think I’m sort of awesome? All my friends say I’m awesome.

PRINCE: Yes, I could see maybe a sort of . . . . Say, would you like a cup of hot chocolate? I’ll get it for you. (leaves quickly.

GODZELLA: Hey! Wait for me!

KING: (talking to another woman) Don’t go away, sweetheart. I’ll be right back. (to Prince) Oh, there you are, son. How was she?

PRINCE: I found her a bit aggressive.

KING: All right, now, son, listen to me. You can’t give up . . . as long as you keep trying, you’ll . . . . Wait! There’s another one. OK, don’t forget. Suave and cool.

CINDERELLA: Oh! Just look at everything. The rooms are so huge – and the people – and dragon heads everywhere . . . I wonder . . .

CINDERELLA & PRINCE: (bumping into each other) Oh! Excuse me. I didn’t see . . .

CINDERELLA: Wow! I wonder who he is.

PRINCE: Wow! I wonder who she is.

CINDERELLA: I wonder if he’s going to ask me to dance.

PRINCE: May I have a dance with you?

CINDERELLA: Nothing would please me more.

(Price starts fast dancing awkwardly, Cinderella follows with the same awkward dance)

CINDERELLA: He’s so big and strong. I know he can take care of me.

PRINCE: She’s so big and strong. I know she can take care of me

CINDERELLA: Say, would you tell me who you are?

PRINCE: I – uh – sure – I’m – You know – Hey, those are great boots. Where did you get them?

CINDERELLA: From my dad. They’re really comfortable. Here take a look.

PRINCE: Yeah, these are good. (to audience) Oh, my gosh, she’s perfect. I don’t think I have to look any more. (Drops to one knee – to Cinderella) Listen, I know that you’re some Princess or something, and I’m just Prince Charming from this kingdom . . . but I love you, and I must ask you a very important question . . .

CINDERELLA: (to audience) I didn’t know he was the prince

PRINCE: Will you marry me and be our Queen?

CINDERELLA: (to audience) But he doesn’t even know who I am. What should I do?

PRINCE: Say yes!

CINDERELLA: Okay, my answer is . . . (Clock begins to strike 12:00 – Bong, bong, bong) Oh! I can’t stay (Bong, bong, bong) I have to go! (runs off) (Bong, bong, bong) Oh, I’ve got to get home. (Loses boot)

PRINCE: (chasing after Cinderella) Wow! She’s fast (finds boot) Wait!

KING: What are you doing with that boot, son?

PRINCE: Dad! I found her! The one we were hoping for. She’s fantastic – I love her – but I don’t know who or where she is. All I have left is this boot.

KING: Wait a sec. You’re telling me that the girl you live fits inside that boot?

PRINCE: Just her foot, Dad. All we have is the boot. How can we find her?

KING: I have it! A Charming Proclamation! Tomorrow we shall go to every house in the kingdom and try this boot on the foot of every maiden in the land. ***** The next day*****

GODZELLA: (yawning, just waking up) Boy, what a night. I’d sure like to get hold of that twit who stole the Prince. I’d shake her to pieces and kick her and stomp on her -- but I don’t know who she is or where she is.

MAZZARELLA: Yeah, if I had that strumpety hussy here, I’d punch her and push her and kick her until she couldn’t get up -- but I don’t know who she is or where she is.

GODZELLA: Cinderella, go fix our breakfast. Then afterwards, scrape the furnace, fix the roof, dig a new cesspool, and clean the dishes.

CINDERELLA: Yes, of course. Have a nice day. (Knock, knock, knock)

KING: Make way for the King!

M & G: The King! (bows, holds)

KING: Hear Ye! Hear Ye! The maiden whose foot fits this boot will marry my son, the Prince, and be our new Queen.

GODZELLA: It’s me! It’s me! Put it on. (tries it on, but doesn’t fit)

MAZZARELLA: Ha! (takes boot) I knew it was me. (tries it on, but doesn’t fit)

CINDERELLA: Hey everybody! Come and see the new cesspool.

KING: What is that? Is that a girl?

MAZZARELLA: No, that’s Cinderella. She’s our dumb stepsister.

GODZELLA: She’s nothing.

KING: Well, we said every maiden. I guess that includes her. (tries it on)

KING: Look! It fits!

M & G: (can’t believe it) IT FITS?!

KING: Son! Come here! Prince Charming!

PRINCE: It’s no use, dad. We’re never going to find her. We might as well . . . (gasps) It’s you!

CINDERELLA: It’s you.

PRINCE: It’s us.

CINDERELLA: It’s we.

GODZELLA: Great. . . now they’re going to go live happily ever after or something.

MAZZARELLA: That’s usually how these things go . . .
```

---

## IC-0497: Clash of the Titanic

- Title: Clash of the Titanic
- Author (byline): Eric D. Snider
- Work: Snide Remarks ASIN: B000REH4ZS (available through Amazon.com)
- Publisher: Eric D. Snider
- Publication date as stated: January 1998
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR 1, NARRATOR 2, KATE WINSLET, KATE’S WEASELLY FIANCE, KATE, LEONARDO DICAPRIO, LEONARDO, WEASELLY FIANCE, AUDIENCE, FIRST MATE, CAPTAIN, ICEBERG
- Teaser before the introduction: Yes
- Spoken words (computed): 924
- Already set (do not supply): none

### Source block (context only)

```text
Author: Eric D. Snider
Newspaper: 1st Published in the Brigham Young University Newspaper, The Daily Universe,
February 9, 1998
Website: Now available at https://www.ericdsnider.com/snide/clash-of-the-titanic/
Snide Remarks #26
ISBN: N/A
Publisher: Brigham Young University Press / Eric D Snider.com
Date: February 9, 1998
Also Published in
Author: Eric D. Snider
Book: Snide Remarks
ASIN: B000REH4ZS (available through Amazon.com)
Publisher: Eric D. Snider
Date: January 1998
```

### Introduction (context only: never use it for content warnings)

```text
TOGETHER: Clash of the Titanic by Eric D. Snider
```

### Performance text (classify this)

```text
Suggested Roles: Actress: Narrator 1. Kate Winslet, Kate’s Weaselly Fiancé, First Mate, 150-Year-Old Kate

Actor: Narrator 2, Leonardo DiCaprio, Audience, Captain, Iceberg

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

NARRATOR 1: Many of you have seen the film “Titanic,” which is about a great big boat that sank like a thousand years ago that for some reason everyone is just now getting worked up about.

NARRATOR 2: Some of you—I am speaking to the women here—have seen this movie several times. And I would like to know why. You think there’s a chance the movie will end differently if you see it again? Do you think this is a “Choose Your Own Adventure” movie? It’s NOT!

NARRATOR 1: No matter how many times you see it, the boat is going to sink, and the same people are going to die.

NARRATOR 2: This movie is entirely too long. The actual sinking of the Titanic took only four hours; the movie is easily three times that long.

NARRATOR 1: [So] as a public service, [we are] offering this much-shortened screenplay . . .

(Scene 1)

KATE WINSLET: Why, this is a fancy boat, isn't it?

KATE’S WEASELLY FIANCE: Yes, it certainly is. Here is the art you asked for. It is by an artist named "Picasso." I am certain he will amount to nothing.

KATE: Ha ha ha. That is very funny to our audience, because of course Picasso later amounted to quite a bit, after this boat sank.

LEONARDO DICAPRIO: Hello, I'm Leonardo DiCaprio. Perhaps you have seen the many Internet sites dedicated to the worship of me. You are very pretty.

KATE: Thank you. So are you.

LEONARDO: I know. Prettier than you, in fact. I am going to put on my "brooding" face now, to ensure that women will keep coming back again and again to see this movie. Later, my white shirt will be soaking wet.

KATE: While you're doing that, I will concentrate on standing here and looking pretty, to keep the men in the audience interested until the boat sinks and people start dying.

WEASELLY FIANCE: Excuse me. I do not like you, Leonardo, even though you saved my fiancée's life. I am going to sneer at you and treat you like dirt because you're poor, and then I'll probably be physically abusive to my fiancée, and then, just to make sure the audience really hates me, and to make sure my character is entirely one-dimensional, perhaps I'll throw an elderly person into the water.

AUDIENCE: Boo! We hate you! Even though all real people have at least a few admirable qualities, we have not been shown any of yours, and plus, you're trying to come between Leonardo and Kate, and so therefore we hate you! Boo! (Even though technically it is Leonardo who is coming between you and Kate. But Leonardo is handsomer than you, even though he is only 13, so we are on his side. Boo!)

(Scene 2)

LEONARDO: I'm glad we snuck away like this so that you could cheat on your fiancé.

KATE: So am I. Even though I am engaged to him and have made a commitment to marry him, that is no reason why you and I cannot climb into the back seat of a car and steam up the windows together. The fact that I am the heroine of the movie will no doubt help the cattle-like audience forgive me of this, though they would probably be VERY angry indeed if my fiancé were to do the same thing to me.

AUDIENCE: Darn straight, we would! Moo! We mean, Boo!

LEONARDO: I agree. First, I would like to draw you, though, so of course you have to take off all your clothes.

KATE: But can a movie with five minutes of continuous nudity be at all successful in, say, Provo, Utah, where the audiences might not stand for that sort of thing?

LEONARDO: I would be willing to bet that for the first three weeks the film is in release, every single showing at the Wynnsong Theater in Provo will sell out.

NARRATOR 2: According to Wynnsong manager Matt Palmer, that is exactly what happened.

KATE: All right, then. (sound of clothes hitting the floor)

(Scene 3)

FIRST MATE: Captain, we're about to hit an iceberg!

CAPTAIN: Great, I could use some ice for my drink. (sound of drinking)

ICEBERG: (hits boat)

FIRST MATE: That can't be good.

CAPTAIN: Bottoms up!

AUDIENCE: Huh?

FIRST MATE: That was irony, you fools.

AUDIENCE: Baa! Moo! Where's Leonardo?

(Scene 4)

LEONARDO: I have been informed that this boat is sinking.

KATE: That is terrible.

LEONARDO: Would you like to engage in some more immoral-but-justified behavior?

KATE: Certainly.

AUDIENCE: Boo! Boo!

WEASELLY FIANCE: (aside) I'm getting the raw end of the deal here. (to Leonardo) Listen, Leonardo, to cement my morally-dubious-yet-somehow-less-annoying-than-you personality, I am going to handcuff you to this pipe, here in a room that will soon be filling with water, due to the fact that we are sinking, which I believe has been mentioned previously.

LEONARDO: Why don't you just shoot me?

WEASELLY FIANCE: Because then you wouldn't be able to escape and save Kate from me. Of course, you're going to die anyway --

AUDIENCE: Don't spoil it for us! Booooooo!!

LEONARDO: He's right, though. I am doomed.

AUDIENCE: Aww, look how cute he is when he's doomed!

WEASELLY FIANCE: I hate you people.

(Scene 5) 150-YEAR-OLD-KATE: (Actor 2 assists elderly Kate) And that's when Leonardo rescued me from my evil fiancé and helped me float on a board in the water. Of course, if it hadn't been for having to rescue HIM, I could have gotten on an actual lifeboat, and frozen my legs nearly off. Anyway, he's pretty much dead now, and I'm well over a thousand years old, and who's making my supper? I need a bath. Turn down that Enya music, it's making my ears hurt. You kids today, with your loud music. Why, when I was (Actor 2 begins to leave) -- hey! Don't you walk away from me, Mr. Snooty-Patootie! I'd turn you over my knee, if I had one. I'll beat you in the head with this huge diamond! Come back here!

(FADE TO BLACK; roll credits; annoying Celine Dion song [Actor 2 hums theme from Titanic])
```

---

## IC-0498: The Complete History of America (Abridged)

- Title: The Complete History of America (Abridged)
- Author (byline): Adam Long, Reed Martin and Austin Tichenor
- Work: Not specified
- Publisher: Broadway Play Publishing
- Publication date as stated: June 2000
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: REED, ADAM, AUSTIN, VESPUCCI, SOPHIA, PASTOR, ANNOUNCER, MINUTE MAN, MADISON, FRANKLIN, SOLDIER, SARGE, FDR, HITLER, ROCK FURY, EVA BRAUN, HAWKEYE PIERCE, ANNOUNCER 2, GAME SHOW HOST, CONTESTANT, SPADE, CONSPIRATOR GUY
- Teaser before the introduction: Yes
- Spoken words (computed): 1714
- Already set (do not supply): none

### Source block (context only)

```text
Author: Adam Long, Reed Martin and Austin Tichenor
ISBN: 978-0881451481
Publisher: Broadway Play Publishing
Date (Month/Year): June 2000
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: The Complete History of America (abridged) ACTOR 2: by Adam Long, Reed Martin and Austin Tichenor
```

### Performance text (classify this)

```text
Suggested Roles:

Actor 1: Reed, Austin, Sophia, Pastor, Franklin, Soldier, FDR, Hitler, Eva Braun, Hawkeye Pierce, Announcer 2, Contestant, Spade

Actor 2: Adam, Vespucci, Announcer, Minute Man, Madison, Sarge, Rock Fury, Game Show Host, Conspirator Guy

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Notes from the Authors: Although we use the names Adam, Reed, and Austin within the script, each cast member should use his own real name when performing the show. There are topical references in the script. The humor and relevance of these will fade over time, so we encourage each production to change these references to keep them as up-to-date as possible. [References have been updated for performances in 2026; changes appear in red] ************

REED: (Pg 3-4) Good morning/afternoon/evening! I’m [insert name] and tonight we explore the history of a great nation.

ADAM: [After all] it is only through remembering our past that we can learn from our mistakes, or at least blame them on somebody else, and then move on . . . into a better future.

AUSTIN: (Pg 5) [Today] many Americans are at best uninformed or at worst embarrassed about our own history.

REED: Well, damn it, we’ve got nothing to be embarrassed about! We brought the world its first democracy . . . a man on the moon . . . McDonalds, Big Bird and Bart Simpson!

ADAM: Let’s do it!

REED: (Pg 5) We begin at the beginning: 1492 Spain! The first chapter of the history of America is about to be written by that legendary Italian explorer . . . (fanfare) Amerigo Vespuchi! We join him now in his humble map shop.

VESPUCCI: (bad Italian accent and flamboyant hand-gestures) Ring-a! Ring-a! (Answering his hand) Hello, Maps-R-Us. Amerigo Vespucci here . . .

SOPHIA: Amerigo!

VESPUCCI: (Pg 6) Shaddup, woman! I’m on the telephone!

SOPHIA: My parents told me not to marry you. They said, “Marry a nice boy, like that Christopher Columbus. He’s going places!

VESPUCCI: (Looks into phone) Hello? (He hangs up) Great! You just lost me a customer. I hope you’re happy, Sophia!

SOPHIA: (Pg 7) Let’s face it, Amerigo, nobody buys your maps because they’re crap!

VESPUCCI: I can’t stay here any longer. I’m off to discover a larger world. You will never see me again!

SOPHIA: Amerigo!!!!!

REED: (Pg 8) In 1502, after two long, treacherous voyages, Amerigo concluded that what everyone had thought was India was actually a new world. Eventually it bore his name AMERICA!

ADAM: (Pg 10) Hey! [What about] Christopher Columbua? He discovered the New World!

REED: Well, his name really wasn’t Christopher Columbus, it was Christobal Colon. And he bumped into the New World by mistake. He wasn’t even the first one here! There was a native population of over 90 million people here before he arrived.

AUSTIN: Yeah, but in fairness to Columbus, though, he was the first man to slaughter and enslave the native population AND he became very wealthy in the process. So in that sense, he was the first true American!

ADAM: (Pg 13) Hey, can I do that poem I wrote? I wrote a poem about the first English settlement in North America

REED: [FLASH FORWARD TO 1607] (Shrugs . . .)

ADAM: (Pg 14-15) 'Twas 1607, in the fine month of May, That three proud ships land at Chesapeake Bay

Jamestown was born, so the story was told, To spread our Lord's word and for mining of gold.

The livin' was harsh for those brave men and women. They toiled and they sweated and rarely went swimmin'.

The new world was tamed by men who were brave And men who were strong and six million slaves

(shocked expressions and the raps peters out) And indentured servants and the Iroquois nation Who gave up their land without compensation

(Trying to regain momentum) So the Pilgrims perfected the art of good livin',
They carved up the land and invented Thanksgivin'
And lickety split, just as quick as you please,
Wham barn ma'am there were thirteen colonies

PASTOR: Hello, and welcome to our weekly meeting of Salem’s First Church of Tolerance and National Witchhunter’s Association. I am your pastor, the Reverend Orwell. Last night the Lord came to me and He said . . . You and your followers need to kill 100 witches this week or I’m going to call you home! So I urge you to hunt the good hunt. And don’t forget that this witch-hunt will begin an American tradition that will carry on well into the twentieth century! Here’s how you spot a real witch: They melt when you throw water on them, they’re surrounded by flying monkeys and they may actually run for president someday!

AUSTIN: (Pg 16) Hey! The king has doubled our taxes and we’re putting together a people’s army to fight him right now. We’re off to throw tea in the harbor!

ANNOUNCER: (Pg 17) Paul Revere and the Raiders number on the charts with “The British are Coming”

ADAM: Listen, my children, and you shall hear of the midnight ride of Paul Revere!

AUSTIN: (Pg 18) And a full-fledged revolution was underway. The colonists wanted to stop the British government from imposing unfair taxes, so that the American government could impose unfair and exorbitant taxes. George Washington commanded a tiny contingent of fighters known as the Minute Men – fighting for American liberty.

MINUTE MAN: (Pg 20) (reading from flyer) Expel the Evil Empire from North America and meet chick. High frostbite tolerance a plus. No tea drinkers, please. Be all that you can be. Apply in person – Valley Forge

REED: (Pg 18) (singing) We represent the Lexington League
The Lexington League
The Lexington League
And in the name of the Lexington League . . .
We wish to welcome you to Valley Forge!

ADAM: (Pg 22) So the rebel troops brought the Brits to their knees! And finally in Yorktown in Fall ’81, the British surrendered – The Yankees had won!

REED: imme an M! Gimme an E! Gimme an R! I! C! Gimme an A! Whtzzat spell? ‘MURRICA! ******

MADISON: (Pg 23) I can’t believe the Bill of Rights is due tomorrow.

FRANKLIN: Now, as the world’s first democracy, I think we should guarantee Freedom of Religion, Freedom of the Press, and Freedom of Speech.

MADISON: If you guarantee all those rights, people are going to be saying all kinds of crazy stuff and pissing each other off.

FRANKLIN: Well, then, let’s give everyone the right to carry a gun to shot each other, and the right to a fair and speedy trial by a jury of their peers after they do. Are we in agreement?

MADISON: Totally! . . . . [Until . . . . }

REED: (Pg 31) The Civil War!

ANNOUNCER: (Pg 33) The war was the bloodiest in the history of the nation. At the heart of the fighting was the issue of slavery. And when abolitionist Abraham Lincoln (cough “Republican”) became President in 1861, the South seceded from the Union. (Pg 34) But in the end, the South surrendered, and they all lived happily ever after. Except for Abraham Lincoln who was shot in the head by John Wilkes Booth.

******

(Pg 37-38) (Marching in place while saluting, hum a few bars of “Over There” *)

SOLDIER: World War I – The Trenches (jumps into a trench somewhere in France. Mime a gun and peak out grimly over the edge of the trench) You think they’re still out there, Sarge? It’s pretty quiet out there.

SARGE: Yeah. Too quiet . . . They’re out there. Every last one of them! (he peers through binoculars) My God!

SOLDIER: We’re outnumbered a hundred to one! (Pg 39) (Panicking) I gotta get outa here! I’m too young to die!

SARGE: Calm down, soldier! (Slaps him) (Pg 37) We’re expendable. We got a job to do and we do it. Case closed!

SOLDIER: But don’t you see?! We’re trapped! We’re just cannon fodder for the military-industrial complex!

SARGE: (Pg 40) All right, we’re going over the top! Let’s go!!! (He leaps out of the foxhole and is instantly struck down) ******

ANNOUNCER: (Pg 41) Dateline 1919. The Treaty of Versailles is signed. The Great War is over. 18th Amendment ratified, creating Prohibition. And the Golden Ae of Radio unites the country from sea to shining sea! Until . . . .[World War II] (Pg 46) Suddenly, over the hills in a cloud of dust and the sound of a thundering wheelchair, appears Franklin Delano Roosevelt!

FDR: My fellow Americans, the only thing we have to fear is fear itself. We hereby declare war on the Axis powers!

ANNOUNCER: . . . and now back to the exciting conclusion of Rock Fury, Super GI!

HITLER: Look! Ze alies are marcing into Berlin. Zey are falling right into my trap. Now I wll press zis button, firing the secret Uberveapon zat vill vipe out ze whole Allied force. Ha-ha-ha-ha! (Woosh sound, the sound of a man flying) (Pg 47) Ach, Vut is zat noise? Oh, no! It’s a bird, it’s a plane . . .

ROCK FURY: No! It’s Rock Fury, Super GI! Your jib-dancing days are over, little man! In its greed and lust for power, Germany has tried to take over an entire continent.

HITLER: But isn’t zat vut ze US did in Norze America?

ROCK FURY: We didn’t try to wipe out an entire race of people!

EVA BRAUN: Vut about ze Indians?

ROCK FURY: Well, we don’t lock people away in concentration camps.

EVA BRAUN: Vut about ze Japanese-Americans on the Vest Coast?

ROCK FURY: (Unable to answer, he addresses the audience) (Pg 48) Well, thank goodness we won this war; otherwise, the German and Japanese economies would dominate the world!

HAWKEYE PIERCE: Help, Help!

ROCK FURY: Wait! My super hearing is picking up Alan Alda calling for help in Korea. Rock Fury, Super GI is off once again to battle for truth, justice and American markets! (Whoosh sound as he flies away, followed by a news ticker sound)

ANNOUNCER 2: This just in. Atom bombs dropped on Hiroshima and Nagasaki. Over two hundred thousand dead. That report in just a moment, but first it’s time to play Queen for a Day! – The Game show which celebrates the achievements of American women! (cheering and game show music) *****

GAME SHOW HOST: (Pg 50) Name the brave seamstress from Montgomery, Alabama, who refused to move to the back of the bus and jump-started the American civil rights movement?

CONTESTANT: (Pg 51) Whoopi Goldberg? (buzzer sounds) *****

ADAM: (Pg 54-55) Okay . . . Postwar America – Film Noir Ending! (dons an overcoat and fedora and steps out of the scene, noir style)

SPADE: The name’s Diamond, Spade Diamond. I’m a private eye! (steps back into scene)

CONSPIRATOR GUY: (Pg 55) If you know what’s good for you, you’ll drop this case before you start it. Unless you want to find out the truth!

SPADE: (Pg 60) Who are you!?

CONSPIRATOR GUY: (Pg 55) Just call me the Conspirator Guy. (Pg 68) You want to know who caused the Cold War? Who benefited? (Whispering) The Generals!

SPADE: The military?

CONSPIRATOR GUY: No! No! General Motors, General Electric. They caused the Cold War! And . . . And . . . I shot JFK, not Lee Harvey Oswald! (Pg 69) I shot Bobby Kennedy, too. And Martin Luther King. And Malcolm X!

SPADE: Wow.

CONSPIRATOR GUY: And I shot Jr, and invented the AIDS virus and I whacked Nancy Kerrigan on the knee . . . It’d whack her again if I had half a chance . . . and I shrank the bloody glove so it wouldn’t fit OJ anymore, and I told President Clinton “Go ahead! She’s an intern! Who cares?” (Spade shoots Conspirator Guy with his finger gun)

SPADE: (Steps our of the scene) I had to put him out of my misery. So there it was. The Cold War was over and Communism was dead . . . well, except for a billion people in China. *****

REED: (Pg 70) Thank you. Thank you. That was the Complete History of America! Is there anything we need to add here historically?

ADAM: Well, we left out a few people. Kristi Noem, Pam Bondi, Pete Hegseth, Donald Trump, Jeffrey Epstein?

AUSTIN: (Considers for a moment) Not that important.

ADAM: COVID-19? Constitutional rights? Immigration Enforcement by ICE?

AUSTIN: To mask or not to mask . . . that is the question!

ADAM: (PG 71) I’m [insert name]

AUSTIN: And I’m [Insert name] and that’s history!
```

---

## IC-0499: The Complete Works of William Shakespeare (abridged) [revised]

- Title: The Complete Works of William Shakespeare (abridged) [revised]
- Author (byline): Adam Long, Daniel Singer and Jess Winfield (The Reduced Shakespeare Co)
- Work: The Reduced Shakespeare Company’s The Complete Works of William Shakespeare
- Publisher: Applause Theatre Books
- Publication date as stated: 1994
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: PLAYWRIGHTS’ NOTE, ACTOR 1, ACTOR 2, TOGETHER, JESS, A/JULIET, D/NURSE, J/FRIAR, D/ROMEO, DANIEL, ADAM, D/WITCH, J/MACBETH, A/MACDUFF, D/CAESAR, A/SOOTHSAYER, J/ANTONY, D/RICHARD II, A/HENRY VI, D/ANNOUNCER, A/ANNOUNCER, D/LEAR, D/RICHARD III, TOGETHER/CHEERLEADERS, ALL
- Teaser before the introduction: Yes
- Spoken words (computed): 1736
- Already set (do not supply): none

### Source block (context only)

```text
Author: Adam Long, Daniel Singer and Jess Winfield
ISBN: 978-1617741555
Publisher: Applause
Date (Month/Year): Feb 2011
Four Lines on Page 4 were taken from the original version of this play
Author: Jess Borgeson, Adam Long and Daniel Singer, edited by Professor J.M. Winfield
Title: The Reduced Shakespeare Company’s The Complete Works of William Shakespeare
(abridged) (Pg 36)
ISBN: 978-1557831576
Publisher: Applause Theatre Books
Date (Month/Year): 1994
```

### Introduction (context only: never use it for content warnings)

```text
(no introduction)
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

PLAYWRIGHTS’ NOTE: The script is written for three actors. In performance, the actors should substitute their own names for “Adam,” “Jess,” and “Daniel.” Where Shakespearean characters appear in the script, the character name is preceded by the actor’s initial (ie A/Juliet means Adam is playing Juliet, etc.) “Shakespearean” dialogue appears in double quotation marks (“”). Because the show comments on contemporary events to place Shakespeare’s works in a modern context, it’s absolutely essential to keep the show fresh and timely by updating the many topical references as events warrant. Have some fun and come up with your very own put-downs of annoying famous people where required . . . And do it FASTER!

ACTOR 1: (Pg 1-2) Hello and welcome to this performance!

ACTOR 2: We are about to attempt a feat which we believe to be unprecedented in the history of civilization.

ACTOR 1: To capture, in a single theatrical experience, the magic . . .

ACTOR 2: The genius . . .

ACTOR 1: The towering grandeur of ‘The Complete Works of William Shakespeare.’

ACTOR 2: Yay . . . (with limited enthusiasm)

ACTOR 1: [Now, we know that] (Pg 4) our society’s capacity to comprehend the genius of William Shakespeare has been systematically *compromised* by soap operas . . .

ACTOR 2: and vandalized by video games . . .

ACTOR 1: But have no fear! (In the manner of a fire-and-brimstone evangelist) We are on a mission from God to spread the holy word of the Bard to the masses.

ACTOR 2: (Pg 6) Now, without further ado, we are proud to present

TOGETHER: The Complete Works of William Shakespeare (abridged)[revised] by Adam Long, Daniel Singer and Jess Winfield.

JESS: (Pg 14) From Tybalt's death onwards, the lovers are curs’d, despite the best efforts of Friar and Nurse; their fate pursues them, they can't seem to duck it. . . And at the end of Act Five, they both kick the bucket. (Juliet and Nurse enter)

A/JULIET: (Pg 15) “O, it is my nurse. Now nurse, what news?”

D/NURSE: Alack the day! He’s gone, he’s kill’d, he’s dead! O Romeo! I saw the wound with my own eyes.

A/JULIET: Is Romeo slaughter’d and is Tybalt dead?

D/NURSE: No, Romeo kill’d Tybalt, he is banished!

A/JULIET: God! Did Romeo's hand shed Tybalt's blood?

D/NURSE: “It did, it did, alas the day it did." (She wails hysterically, runs two small laps around Juliet and exits – Jess enters as FRIAR LAURENCE)

A/JULIET: O, Friar Laurence! Romeo is banished and Tybalt is slain and . . .

J/FRIAR: (bored, he interrupts) “Take thou this vial, and this distilled liquor drink thou off. And presently though thy veins shall run a cold and drowsy humor.”

A/JULIET: (Pg 16-17) (Takes bottle and drinks) O, I feel a cold and drowsy humor running through my veins . . . (Friar exits. Juliet becomes dizzy) Mm, pretty colors! Uh-oh . . . (Juliet vomits) There, I feel much better. (Collapses suddenly. ROMEO enters. He sees JULIET and rushes to her prone body, accidentally stepping on her crotch while doing so)

D/ROMEO: “O, no! (Adam clutches his privates in agony) / My love, my wife! / Death, that hath suck'd the honey of thy breath, / Hath no power yet upon thy beauty. / Juliet, why art thou yet so fair?”

A/JULIET: Dunno, lucky I guess.

D/ROMEO: “Here's to my love. (He drinks from his poison bottle.) / O true apothecary! Thy drugs are quick. / Thus, with a kiss, I die ... (Just as Daniel leans in to kiss Adam, Adam burps. Now Daniel has no wish to kiss Adam. He struggles with the problem for a moment, takes another swig of poison, and finally kisses him) Thus with a kiss, I die.” (ROMEO dies. JULIET wakes up, stretches, scratches her butt, and looks around.)

A/JULIET: Good morning. “Where, O where is my love? (She sees him lying at her feet and screams) "What's this? A cup, closed in my true love's hand? Poison I see hath been his timeless end. O, churl. Drunk all and left no friendly drop to help me after? Then I'll be brief. O happy dagger! This is thy sheath." (She unsheathes ROMEO'S dagger and does a doubletake: the blade is tiny) That's Romeo for ya.

(JULIET stabs herself. She screams, but, to her surprise, she does not feel injured. She looks for a wound and can't find one. Finally, she realizes that the blade is retractable. This is a cause for much joy. She stabs herself gleefully in the torso and on the crown of the head. Finally, she flings her happy dagger to the ground)

A/JULIET: “There rust and let me die!”(Dies)

JESS: Epilogue!

DANIEL: “For never was there a story of more woe / Than this of Juliet and her Romeo”

TOGETHER: (singing) And Romeo and Juliet are deeeeaad . . . ! TRANSITION

ACTOR 1: We shall now move on to explore the genius evident in Shakespeare's more mature plays, as we present his dark and brooding tragedy, 'Othello, the Moor of Venice.’

ADAM: (He beat-boxes, then raps) (Pg 21-24) Here's the story of a brother by the name of Othello / He liked white women and he liked . . . limoncello.

JESS: (catching on quickly) Oh, yeah, yeah. Uh . . . / And a punk named Iago who made hisself a menace / 'Cos he didn't like Othello, the Moor of Venice.

ADAM: Now Othello got married to Des-demona,

JESS: But he took off for the wars and he left her alone-a.

ADAM: It was a moan-a

JESS: A groan-a

A and J: He left her alone-a.

DANIEL: (finally catching on and joining in) He didn't write a letter and he didn't telephone-a! /

(They all get into it, making boom-box noises and adopting a hip-hop attitude) Now Othello loved Desi like Adonis loved Venus.

JESS: And Desi loved Othello cuz he had a big . . .

DANIEL: SWORD!

ADAM: But Iago had a plan that was clever and slick / He was crafty

JESS: He was sly

DANIEL: He was sort of a _____ (Not wanting to say it)

ADAM: He say 'I'm gonna shaft the Moor.'

DANIEL: How you gonna do it? Tell us!

ADAM: Well, I know his tragic flaw is that he's

TOGETHER: Too damn jealous!

ADAM: I need a dupe / I need a dope / I need a kind of a shmoe . . .

JESS: So he find a chump sucker by the name o' Cassio.

DANIEL: And he plants on him Desdemona's handkerchief

ADAM: So Othello gets to wonderin’ just maybe if . . . While he been out fightin’

DANIEL: Commandin’ an army

JESS: Are Desi and Cass playin hide the salami?

TOGETHER: Sa-sa-sa-salam Salaaammii!

DANIEL: So he come back home an’ he mother the beeyotch. (Can “bleep” out this word”)

JESS: An’ he thinks he pulled it off, without a heeyotch.

ADAM: But there's Emilia at the do’.

JESS: Who we met in Act Fo’.

DANIEL: Who say, 'You big dummy, she weren't no whore. She was JESS: Pure

DANIEL: She was JESS: Clean

DANIEL: She was JESS: Virginal, too,

TOGETHER: So why'd you have to go and make her face tum blue?

ADAM: And Othello say:

JESS: ‘Damn, this is getting’ pretty scary.'

DANIEL: So he pulled out his blade and committed hari-kiri. (Jess mimes hara-kiri on himself and twitches in death throes) [NOTE the following 4 lines are from the original (Pg 36), rather than the revised script]

ADAM: Iago got caught, but he prob'ly copped a plea,

JESS: (Singing) [And he] Loaded up his bags,

DANIEL: And moved to Beverly . . .

TOGETHER: . . .Hills, that is. (Bows and elaborate handshakes all round.)

ADAM: (Raised-fist salute) (Pg 28) Tragedies! (Daniel clears his throat because that was inappropriate; Adam with a much smaller fist-salute) Tragedies.

DANIEL: ‘The Scottish play!’

ADAM: Oh yeah! Mac –

DANIEL: Shhhhh! Don’t say it! It’s cursed. It’s bad luck to say the name of that show unless you’re performing it. That’s why we refer to it is ‘The Scottish Play.’

ADAM: But we are performing it.

DANIEL: (Pg 29-31) (shrugs) We now present our authentically Scottish production of . . . Macbeth!

D/WITCH: “Double, double, toil and trouble.” (In nearly impenetrable Scottish accents)

J/MACBETH: Stay, ye imperrrfect macspeaker. Tell me more.

D/WITCH: Macbeth, Macbeth, beware Macduff. / None of woman born shall harm Macbeth / Till Birnam Wood come to Dunsinane, don't ye know. (WITCH exits. ADAM enters as MACDUFF)

J/MACBETH: Och, that's dead great. Then macwhat macneed macfear of Macduff?

(MACDUFF wields his sword and throws a two-fingered gesture at MACBETH)

A/MACDUFF: See YOU, Jimmy, (a popular Scottish oath) and know / That Macduff was from his mother's womb untimely ripped!” / What d'ye think about that? (They spar)

J/MACBETH: Och! I do nae like it, but I support a woman’s right t’choose! Lay on, ye great haggis-breath! (They fence)

A/MACDUFF: Ah, Macbeth! Ye killed my wife, ye murdered me wee bairns, and ye did poop in my soup.

J/MACBETH: Och! I didnae!

A/MACDUFF: Och, aye, ye did. I had t' throw half of it away. (MACDUFF chases MACBETH offstage where MACBETH'S scream is abruptly cut off. MACDUFF re-enters carrying a severed head) “Behold where lies the usurper's cursed head.” Macbeth, yer arse is out the windie. (Dropkicks the head offstage.) And know, That never was there a story of blood and death / Than this, o' Mister and Mrs. Macbeth. Thankee. (Exits)(JESS enters)

JESS: Meanwhile, in ancient Rome, Julius Caesar was a much beloved tyrant. (ADAM enters)

TOGETHER: All hail, Julius Caesar! (DANIEL enters as JULIUS CAESAR)

D/CAESAR: Hail, citizens!

JESS: . . . Who was warned by a soothsayer . . .

A/SOOTHSAYER: "Beware the Ides of March."

JESS: The great Caesar, however, chose to ignore the warning.

D/CAESAR: What the h*** are the Ides of March?

A/SOOTHSAYER: The 15th of March.

D/CAESAR: Why, that's today. (ADAM stabs him repeatedly. He falls) “Et tu, Brute?” (CAESAR dies. JESS becomes MARK ANTONY, orating over the body.)

J/ANTONY: Friends, Romans, countrymen, lend me your ears. I come to bury Caesar.

ADAM: (Pg 34-38) Bo-ring!

DANIEL: This is the kind of stuff that kids hate to study in school because it's so boring.

ADAM: I'm sorry, guys, but I promised I would not do dry, boring Shakespeare. I love these people, and I don’t want to see them get turned off to Shakespeare. (gesturing to audience) That's what happened to me. When I was in school, and we were supposed to be studying Shakespeare, I'd be looking out the window at all the kids playing ball, and I'd be thinking to myself, 'Why can't this Shakespeare stuff be more like sports?'

DANIEL: How do you mean?

ADAM: Well, sports are exciting. Engaging. I mean, take the histories, for example. With all those kings knocking each other off, running up and down the field, the throne passing from one guy to the next – it’s exactly like football, but you do it with a crown.

DANIEL: Hey, they are kinda similar, aren’t they? Okay, line 'em up. Let's kick some royal . . .

(Jess pulls out a whistle and blows it)(They line up in a football formation – then like a quarterback calling signals) Twenty-five! Forty-two! Richard the Third! Henry the Fourth, Part One, Part Two . . .

TOGETHER: HUT!

JESS: . . . And the crown is snapped to Richard the Second, that well-spoken fourteenth-century monarch. He's fading back to pass, looking for an heir downfield, but there's a heavy rush from King John. (JESS as KING JOHN stabs DANIEL as RICHARD)

D/RICHARD II: "My gross flesh sinks downwards!"

JESS: The crown is in the air, and Henry the Sixth comes up with it!

A/HENRY VI: Victory is mine!

D/ANNOUNCER: But he's hit immediately by King John. Oh no! He’s cutting Henry the Sixth into three parts, that’s gotta hurt! (KING JOHN slices up HENRY) This could be the end of the War of the Roses cycle! (KING JOHN grabs the crown and runs in place with it)

A/ANNOUNCER: King John is in the clear . . . He's at the forty, the thirty, the twenty – (DANIEL sneaks up from behind and pantomimes pouring something into JESS’s mouth) -- ooh, but he's poisoned on the ten yard line! (DANIEL snatches the crown and puts it on. JESS exit.) Looks like he's out for the game. Replacing him now is number seventy-two, King Lear.

D/LEAR: To Regan and Goneril I hand off my kingdom. Cordelia, you go long . . . (JESS re-enters as referee, throwing a penalty flag and blowing a whistle.)

A/ANNOUNCER: There’s a penalty marker! (JESS makes a hand signal and points at LEAR) Fictional character on the field. Lear is disqualified, and he's not happy about it.

D/LEAR: (Disappointed) Bastards! (Jess “bleeps” the profanity)

ADAM: Lining up now is that father-son team of Henry the Fourth and Prince Hal. Center snaps to the quarterback . . . quarterback gives to the hunchback. It looks like Richard the Third's limp is giving him trouble.

D/RICHARD III: "A horse, a horse! My kingdom for a horse!"

A/ANNOUNCER: There’s a pile-up on the field.

D/ANNOUNCER: FUM-BLE!!! And Henry the Eighth comes up with it. He's at the fifteen, the ten. . . He stops at the five to chop off his wife's head . . . TOUCHDOWN for the Red Rose! Oh, my! You gotta believe this is the beginning of a Tudor Dynasty!

TOGETHER/CHEERLEADERS: Henry the Fifth, Richard the Third, the whole royal family’s frickin’ absurd! Goooo, [insert local sports team] Yay!

ADAM: Can I have some house lights please? (consults a large book of SHAKESPEARE PLAYS)

DANIEL: What are you doing?

ADAM: I just want to check the list of plays. I think we might have done' em all already. Yea, see, we did all the histories just now. 'Romeo and Juliet' we did-

DANIEL: (looking over his shoulder) 'Julius Caesar,' right-

ADAM: We rapped 'Othello,' Lear was in the football game, 'Macbeth' we did with Scottish accents.

DANIEL: The comedies ? . . . .

ADAM: Eh . . . let’s skip [them]. And that’s it, right? That’s all of them!

JESS: Hey, no, you guys . . . (Points to a title on the list)

ALL: Hamlet!

ADAM: Shakespeare didn’t write Hamlet. (Shocked looks from the others) What’s it about?

JESS: You know, the young prince struggling with his conscience after his uncle murders his father?

ADAM: Dude, that’s The Lion King. (Pg 39) I don’t wanna do it!

JESS: Look, our show’s called The Complete Works of William Shakespeare.

ADAM: Okay, so we'll call it 'The Complete Works of William Shakespeare Except Hamlet.'

(Looks from the others)

ADAM: You can't make me do it! You can't! (Pg 40) (ADAM springs toward the exit)

JESS: Get back here, you Shakespeare weenie!
```

---

## IC-0500: Coraline

- Title: Coraline
- Author (byline): Neil Gaiman
- Work: Not specified
- Publisher: HarperCollins
- Publication date as stated: July 2002
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 2, NARRATOR, MRS. SPINK, CORALINE, COM, MOTHER, FATHER, COM., OTHER MOTHER, MRS SPINK, POLICEMAN, CAT, CHILD 1, CHILD 2, CHILDREN’S VOICES TOGETHER, OTHER COM
- Teaser before the introduction: Yes
- Spoken words (computed): 1442
- Already set (do not supply): none

### Source block (context only)

```text
Author: Neil Gaiman
ISBN: 978-0380977789
Publisher: HarperCollins
Date (Month/Year): July 2002
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Not since Narnia has the simple act of opening a door unlocked such a fantastic journey.

ACTOR 2: And not since Alice tumbled down the rabbit hole has that journey been so splendidly strange and frightening.

ACTOR 1: Caroline will have to fight with all her wits and courage if she is to save herself and return to her ordinary life.

TOGETHER: Coraline by Neil Gaiman
```

### Performance text (classify this)

```text
Suggested Roles: ACTOR 1: Coraline, Child 2

ACTOR 2: Narrator, Mrs. Spink, COM (Crazy Old Man), Mother, Father, Other Mother, Policeman, Cat, Child 1, Other COM

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

NARRATOR: (Pg 1-2) It was a very old house and Coraline’s family didn’t own all of [it] - it was too big for that. Instead they owned part of it. Miss Spink lived in the flat below . . .

MRS. SPINK: You see, Caroline . . .

CORALINE: It’s Coraline, Not Caroline. Coraline

MRS. SPINK: (waving the interruption away with her hand) [I was] a famous actress in my time. I trod the boards, luvvy!

NARRATOR: . . . and in the flat above was a crazy old man with a big mustache.

COM: One day, little Caroline . . .

CORALINE: It’s Coraline, Not Caroline. Coraline

COM: . . . (waving the interruption away with his hand) When they are all ready, everyone in the whole world will see the wonders of my mouse circus! The mice are not yet ready. They refuse the play the songs I have written for them. They go oompah oompah; but the white mice will only play toodle oodle, like that! I am thinking of trying them on different types of cheese . . . (Listens intently to a mouse held in his hand, then whispers in an ominous voice) (Pg 14) The mice have a message for you: “Don’t go through the door . . .”

NARRATOR: (Pg 2,4,1) The day after they moved in, Coraline went exploring. She explored the garden and the grounds. She explored every day until the day it rained, when Coraline had to stay inside.

CORALINE: (Pg 4-6) What should I do?

MOTHER: (busily typing on her keyboard) Read a book. Watch a video. Play with your toys. Go and pester Miss Spink or the crazy mold man upstairs.

CORALINE: I don’t want to do those things. I want to explore!

NARRATOR: It was time to talk to her father.

CORALINE: It’s raining. Can I go outside?

FATHER: (busily typing on his keyboard) What does your mother say?

CORALINE: (mimicking her mother’s voice) You’re not going out in weather like that, Coraline Jones. But I want to carry on exploring.

FATHER: (frustrated and impatient) Then explore the flat. Count all the doors and windows. List everything blue. And leave me alone to work.

CORALINE: (keeping track of everything on a sheet of paper) Everything blue – 153; Windows – 21; Doors . . .

NARRATOR: (Pg 1) [It was then that] Coraline discovered THE door. (Pg 6-7) The big, carved, wooden door at the far corner of the drawing room. It was locked.

CORALINE: (to Mother) Where does that door go?

MOTHER: Nowhere, dear. (angry at the interruption, grumpily takes a string of keys, selects the oldest key and unlocks the door. Coraline watches excitedly and then is disappointed)

NARRATOR: Her mother was right. The door didn’t go anywhere. It opened onto a brick wall.

COM.: (Pg 14) (whispering) Don’t go through the door!

CORALINE: (Pg 16) (confused at the ominous whisper from nowhere, releases a heavy disappointed sigh and goes to find her father again) . . . (to her father) I’m bored. Why don’t you play with me?

FATHER: Busy . . . Working . . .Why don’t you go and bother Miss Spink? ******

MRS. SPINK: Oh, it’s you, Caroline

CORALINE: (Pg 2) It’s Coraline, Not Caroline. Coraline

MRS. SPINK: (Pg 16-19) Come in dear. Would you like a cup of tea? (pours a cup and hands it to Coraline. Coraline takes a sip and Mrs. Spink grabs the teacup) I’ll read the leaves. I’ll read your future. (peers into the cup, then says ominously) You are in terrible danger.

CORALINE: What am I in danger from? What should I do?

MRS. SPINK: Be very, very careful!

NARRATOR: She reaches into her pocket and takes out a stone with a hole in it.

MRS. SPINK: [This] might help. (hands it to Coraline, who holds it up to the light and peers through the hole) They’re good for bad things . . . sometimes. ******

CORALINE: (bored again, wanders back into her part of the house and over to THE door. She turned the doorknob, and instead of a brick wall behind the door, there is a dark hallway.

OTHER MOTHER: (Pg 26-28) Coraline? Is that you? Lunchtime . . .

CORALINE: Who are you?

OTHER MOTHER: I’m your other mother.

CORALINE: (confused) I didn’t know I had another mother.

OTHER MOTHER: Of course, you do. Everyone does. It wasn’t the same here without you; but [I] knew you’d arrive one day, and then we could be a proper family. (Pg 43-45) You can stay here for ever and always. If you want to. (puts her hand on Coraline’s shoulder)

MRS SPINK: (Pg 18) You are in terrible danger.

CORALINE: (Pg 43-45) (pulling away, scared and nervous) I’m going now. (reaches into her pocket and pulls out the stone with a hole in it)

OTHER MOTHER: (her hand scuttles off Coraline’s shoulder like a frightened spider) If that’s what you want. Come back soon . . . then we’ll be together . . . for ever and always!

CORALINE: (backing away, hurries through the door back into her own house and searches for her Mother and Father) Mom?? Dad?? (they are nowhere to be found) (Pg 51) Where are they? (Pg 52-53) I suppose there is only one thing left to do. (picks up the phone, searches phone book for the number and dials)

POLICEMAN: Police

CORALINE: Hello. My name is Coraline Jones. I am ringing to report a crime. Kidnapping. Grown-up-napping really. My parents have been stolen away.

POLICEMAN: (humoring her) And do you know who stole them?

CORALINE: I think my other mother has them in her clutches. She may want to keep them in order to lure me back. I’m not sure.

POLICEMAN: (chuckling) Ah, the nefarious clutches, is it? Mmm. Ask your mother to make you a mug of hot chocolate and give you a great big old hug. (hangs up)

CORALINE: (Pg 57) (realizing she’s on her own . . . returns to THE door, places her hand on the knob, hesitates, gives herself a pep talk) When you’re scared, but you still do it anyway, that’s brave.

COM: (Pg 14) (whispering) Don’t go through the door!

MRS. SPINK: (Pg 18) You are in terrible danger.

CORALINE: (Pg 57) (arguing with the voices) They are my parents. If they noticed I was gone, I’m sure they would do the same for me. (opens the door and enters the other world)

OTHER MOTHER: (Pg 58-62) Coraline? Darling? (embraces Caroline in a desperate hug) Why did you ever run away from me.

CORALINE: (breaking free) Where are my parents?!

OTHER MOTHER: I’m here. I’m ready to love you and play with you and feed you and make your life interesting. (a creepy smile)

CORALINE: You don’t frighten me (pulls the stone from her pocket and uses it to ward off her other mother) I want my parents back!

OTHER MOTHER: (recoiling from the stone) Whatever would I have done with your old parents? If they have left you, Coraline, it must be because they became bored with you.

CORALINE: You’re lying. You stole them.

OTHER MOTHER: Please, don’t be difficult. I am going back to bed, Coraline . . . I would strongly suggest that you do the same. (exits)

CORALINE: (tries the door, but it won’t open. A cat enters, and she speaks to it, not expecting an answer) Why does she want me? Why does she want me to stay here with her?

CAT: (Pg 63) She wants something to love, I think (reacts with shock and awe, but then accepts this strange occurrence) Something that isn’t her. She might want something to eat as well. It’s hard to tell with creatures like that.

CORALINE: Do you have any advice?

CAT: Challenge her. There’s no guarantee she’ll play fair, but her kind of thing loves games and challenges . . . (Pg 36) By the by. It was sensible of you to bring protection. I’d hang on to it, if I were you. (exits)

CORALINE: Protection . . . (Coraline pulls the stone from her pocket, rubs it for luck and returns it to her pocket)

OTHER MOTHER: (Pg 75-77) (enters) Coraline, my darling. I thought we could play some games together. Hopscotch? Happy Families? Monopoly? What game should we play.

CORALINE: I don’t want to play with you. I want to go home and be with my real parents. I want you to let them go. To let us all go!

OTHER MOTHER: (tilts her head, purses her lips angrily) Manners! (grabs Coraline’s arm and pulls her to the end of the hall, opens a small door and pushes her inside) You may come out when you’ve learned some manners. And when you’re ready to be a loving daughter.

MRS. SPINK: (Pg 18) You are in terrible danger.

CORALINE: (Pg 79-84) (begins to cry but then notices 2 other children also locked inside)

CHILD 1: (in a whisper) Hush! And Shush! Say nothing, for the beldam might be listening!

CHILD 2: Art thou – alive?

CORALINE: (also in a hushed voice) What happened to you. How did you come here?

CHILDREN’S VOICES TOGETHER: She left us here. She stole our hearts, and she stole our souls, she took our lives away, and she forgot about us in the dark. Flee while you still have your mind and your soul.

CORALINE: I’m not running away. She has my parents. I came back to get them.

CHILD 1: If you could win your mamma and your papa back from the beldam, you could also free our souls.

CORALINE: Has she taken them?

CHILDREN’S VOICES TOGETHER: And hidden them. That is why we could not leave here when we died. She kept us, and she fed on us, until now we’ve nothing left of ourselves. Flee!

CORALINE: She won’t keep me in the dark forever. She brought me here to play games. Games and challenges, the cat said. (hears a rustling at the door)

OTHER MOTHER: (Pg 87-90) (opening the door) There, my sweet Coraline. You needed to be taught a lesson. Now, if you will be a good child who loves her mother. (gestures that Coraline may come out)

CHILDREN’S VOICES TOGETHER: Look through the stone (their voices echo)

CORALINE: (as she climbs out of the small room) You like games. That’s what I’ve been told.

OTHER MOTHER: (intrigued) Everybody likes games.

CORALINE: Yes. Wouldn’t you be happier if you won me, fair and square?

OTHER MOTHER: Possibly. What exactly are you offering?

CORALINE: Me. If I lose I’ll stay here with you forever and I’ll let you love me. I’ll be a most dutiful daughter. I’ll eat your food and play Happy Families.

OTHER MOTHER: That sounds very fine. And if you do not lose?

CORALINE: Then you let me go. You let everyone go – my real father and mother, the children [in that room] . . . everyone you’ve trapped here.

OTHER MOTHER: What kind of game shall it be? A riddle? A test of knowledge?

CORALINE: An exploring game. A finding-things game.

OTHER MOTHER: And what is it you should be finding, Coraline Jones?

CORALINE: My parents . . and the souls of the children.

OTHER MOTHER: Deal!

NARRATOR: (Pg 92) Caroline looked around the kitchen. She opened the oven, peered into the freezer and poked into the refrigerator.

CHILD 2: (Pg 85) Look through the stone

CORALINE: (Pg 93) (puts her hand in her pocket, pulls out the stone with a hole in it and peers though the hole. She wanders up the stairs, still peering through the stone) ******

(Pg 116-118) (Coraline has entered the other world rooms of the Crazy Old Man)

OTHER COM: Nothing’s changed, little girl. [If you win] You’ll go home. You’ll be bored. You’ll be ignored. They don’t even get your name right. Stay here with us. Your other mother will build whole worlds for you to explore. If you stay here, you can have whatever you want.

CORALINE: (sighing) You really don’t understand, do you? I don’t want whatever I want. Nobody does. What kind of fun would it be if I just got everything I ever wanted. You’re just a bad copy she made of the crazy old man upstairs.

CAT: (Pg 133) Come on! This is not a good place to be! Quickly!

CHILD 2: (Pg 85) Look through the stone

NARRATOR: (Pg 133-134) (Peering through her stone, Coraline acts out the following) Coraline began to run. Winds howled. She could hear the cat padding in the dark in front of her. She reached the door. It was open. She staggered through it and slammed it behind her with the loudest bang you can imagine. *******

(scene opens with Coraline sleeping on the floor just outside THE door. Her real mother gently shaking her to wake her up)

MOTHER: (in a non-nonsense tone) Coraline? What a funny place to fall asleep. We looked all over the house for you. Dinner in fifteen minutes. Don’t forget to wash your hands.

(Coraline gives her Mother a huge hug)
```

---

## IC-0501: Corrector

- Title: Corrector
- Author (byline): Maximillian Gill
- Work: The Best Ten-Minute Plays 2022, Pgs 77-84
- Publisher: Smith and Kraus
- Publication date as stated: Aug 2022
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: CORRECTOR, REFUGEE
- Teaser before the introduction: Yes
- Spoken words (computed): 1103
- Already set (do not supply): none

### Source block (context only)

```text
Author: Maximillan Gill
Book: The Best Ten-Minute Plays 2022, Pgs 77-84
ISBN: 978-1575259659
Publisher: Smith and Kraus
Date (Month/Year): Aug 2022
* Source for Introduction Statistic
UNHCR – The UN Refugee Agency
https://www.unhcr.org/refugee-statistics/
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Refugee -- by definition a person who has fled their home, crossed an international border and cannot return to their home country because they fear their life is in danger.

ACTOR 2: In the US, this concept is difficult to fathom. I mean, we’ve heard the word, but is it likely that John Smith from (Insert City, State) will ever experience life as a refugee?

ACTOR 1: What if I told you that world-wide as of October 2023 (update as needed), there are over 36.4 million refugees.*

ACTOR 2: And with new refugee crises in Ukraine and Gaza capturing headlines, the plight of others are at risk of being forgotten: Myanmar’s Rohingya, refugees of the Syrian Civil War, Afghans who fled the Taliban takeover. The list goes on . . .

ACTOR 1: Poet Warsan Shire perhaps said it best: “No one leaves home unless home is the mouth of a shark.”

ACTOR 2: What personal sacrifices are made by refugees in exchange for just the possibility of safety? What would you be willing to sacrifice?

TOGETHER: Corrector by Maximillian Gill
```

### Performance text (classify this)

```text
CHARACTERS • REFUGEE -- any age, any gender, any ethnicity, refugee from a war-torn nation. • CORRECTOR -- any age, any gender, any ethnicity, helps refugees for a price . SETTING -- A basement in a border town in an unnamed country. TIME -- An indeterminate point in the future. Although the play is inspired by the current refugee crisis, it is intended to represent dislocation and assimilation as universal human experiences; thus, nationalities are not specified. However, the characters should represent two ethnicities or should at least read as "different." The Refugee should ideally speak with some sort of accent and be a bit hesitant with language that is not their mother tongue. The neutral pronoun is used throughout for convenience.

(Pg 77-84) A basement. Midnight. CORRECTOR paces, checks their phone. Knock on door. They tap a button on the phone and put it in a pocket. They go to the door. REFUGEE enters, agitated

CORRECTOR: Anybody follow you?

REFUGEE: I don't like this place.

CORRECTOR: Then leave.

REFUGEE: You be careful with me.

CORRECTOR: I need to? (REFUGEE circles CORRECTOR menacingly)

REFUGEE: You know my country.

CORRECTOR: I know your nation is in the midst of a civil war of apocalyptic proportions.

REFUGEE: I was a soldier in that war.

CORRECTOR: Did you commit any atrocities I should know about?

REFUGEE: I won't talk about it.

CORRECTOR: Based on what we're told, your countrymen are a dangerous and violent menace who will likely destroy themselves.

REFUGEE: (They bristle at this a bit before answering) Yes, that's me.

CORRECTOR: Then I do need to be careful.

REFUGEE: It is true you don't want money?

CORRECTOR: Where did you hear that?

REFUGEE: At the camp.

CORRECTOR: And you believe it?

REFUGEE: It is true?

CORRECTOR: If it is, shouldn't there be a long line of refugees outside my door? (REFUGEE goes to the exit) Wait.

REFUGEE: (REFUGEE stops) Just to get here, I used all my money.

CORRECTOR: You need to know what I'm offering.

REFUGEE: You'll take me over the border.

CORRECTOR: Where do you think you want to go?

REFUGEE: The country on the other side.

CORRECTOR: You can pay quite a bit to get across. But once there you'll just end up in another camp.

REFUGEE: What else can I do?

CORRECTOR: You can stay here.

REFUGEE: I have no papers.

CORRECTOR: Papers can be arranged.

REFUGEE: People from my country cannot have papers.

CORRECTOR: You can be here, fully legal, with papers, with a job, in a safe part of the country.

REFUGEE: I am not allowed any of that here.

CORRECTOR: Why?

REFUGEE: They know where I am from.

CORRECTOR: What if nobody could tell?

REFUGEE: How?

CORRECTOR: What marks you?

REFUGEE: I don't understand. (CORRECTOR grabs REFUGEE arm)

CORRECTOR: This skin color? Is that it? (REFUGEE removes CORRECTOR'S hand violently) Is it your voice, your manner of walking? The way you move your head in such a way that I can't tell whether you're nodding or shaking it?

REFUGEE: It is everything.

CORRECTOR: I'm a corrector. I correct people.

REFUGEE: I am not wrong.

CORRECTOR: You are if you want to be here.

REFUGEE: Explain.

CORRECTOR: A form of gene therapy. Chemical injections. They'll correct you.

REFUGEE: And then what?

CORRECTOR: They'll change your skin color and subtly alter your facial features so you'll look more like us.

REFUGEE: All on the outside.

CORRECTOR: No, inside too. After genetic modification we proceed with a regimen to adjust your brain chemistry.

REFUGEE: What does it do?

CORRECTOR: Soften your accent. Give you a better command of our language. You'll even think like we do.

REFUGEE: Is it legal?

CORRECTOR: Not even close. But it's effective.

REFUGEE: I'll be like you.

CORRECTOR: It's not reversible. Who you are now, you won't be that ever again.

REFUGEE: To be here, I can't be who I am.

CORRECTOR: No, listen to me, you'll forget.

REFUGEE: What?

CORRECTOR: It's a side effect of the procedure. Slowly but methodically you will forget. Your mother tongue, the smells of your own country, the way the air feels on a summer morning.

REFUGEE: Forget those things?

CORRECTOR: The person you are now will be gone. But you will fit in very well.

REFUGEE: No.

CORRECTOR: It's the only way.

REFUGEE: I won't be who I am anymore.

CORRECTOR: Now you know why there's no line outside my door.

REFUGEE: I can't forget everything.

CORRECTOR: You've already left it behind.

REFUGEE: Because I had to.

CORRECTOR: Obviously you have another option.

REFUGEE: Which?

CORRECTOR: You can simply go back where you came from.

REFUGEE: The war will kill everybody.

CORRECTOR: You decide.

REFUGEE: When?

CORRECTOR: I administer the protocol in my workroom. It'll take all night. The recovery period will be long, but you will soon feel different.

REFUGEE: I can't lose who I am.

CORRECTOR: What's so great that you can't lose it?

REFUGEE: To me it's everything.

CORRECTOR: What exactly?

REFUGEE: I won't tell you.

CORRECTOR: Prove it.

REFUGEE: You will never have to hide who you are. You will never have to speak your own language only in a whisper or have some name that is not yours.

CORRECTOR: The way this world is going. Let's not be so sure.

REFUGEE: It is not the same for you.

CORRECTOR: What are you most afraid of losing?

REFUGEE: I don't want to lose anything.

CORRECTOR: But right now, choose something.

REFUGEE: It is all something to me.

CORRECTOR: At this moment, what is a painful thing for you to forget?

REFUGEE: A song.

CORRECTOR: What kind of song?

REFUGEE: A song kind of song. A song of my people. My mother sang to me when I was very little.

CORRECTOR: Sing it for me.

REFUGEE: People laugh at our music. It is ugly to them.

CORRECTOR: But it's important to you. Show me that it is.

REFUGEE: I can't remember the words.

CORRECTOR: Just sing.

(REFUGEE starts to sing a tune without words. They stop for a moment, embarrassed, and then continue. CORRECTOR listens, eyes closed. REFUGEE stops. CORRECTOR takes a phone out and presses a button.)

REFUGEE: What did you do?

CORRECTOR: I recorded you.

REFUGEE: What is this?

CORRECTOR: Just relax.

REFUGEE: You will turn me in.

CORRECTOR: No.

REFUGEE: Give me the phone.

CORRECTOR: (CORRECTOR puts it away and backs off) Let me explain.

(REFUGEE takes out a knife and attacks CORRECTOR. They scuffle. REFUGEE is not a good fighter. CORRECTOR disarms them and gets them on the ground. CORRECTOR holds up the knife.)

CORRECTOR: A soldier would be better with this. But you weren't a soldier, were you?

REFUGEE: (REFUGEE stands up) I made bread. In a bread shop.

CORRECTOR: I assume you've never killed anybody.

REFUGEE: You could be my first.

CORRECTOR: Clever tactic, using a violent stereotype as a defense mechanism. (CORRECTOR takes out the phone) Now listen. (REFUGEE grabs the phone from CORRECTOR’S hand. REFUGEE holds it as if ready to smash it against the wall.) No, don't.

REFUGEE: Tell me why or I break it.

CORRECTOR: I have a lot of voices in there. Some people give me recipes for delicately spiced dishes they used to cook in their home country. Others tell me stories they first learned from their grandmothers. A few videos demonstrate dances. One man told me five words in your language that have no equivalent in mine. My favorite is one that describes that specific pang of regret when one recognizes that something lost can never be recovered. From you, I have a song.

REFUGEE: I don't understand.

CORRECTOR: It's true, you will forget who you are. But you will not be forgotten. I'll keep you here.

REFUGEE: Why?

CORRECTOR: I'm a corrector. Because something in this world is very wrong. (REFUGEE hands the phone back to CORRECTOR.) This is all I wanted from you. You've paid. Do you want what you paid for?

REFUGEE: After I forget, can I come back here and listen to my song?

CORRECTOR: I hope you will. (REFUGEE makes an ambiguous motion of the head.)

CORRECTOR: I still can't tell if that's a "yes" or a "no."

REFUGEE: It has to be "yes."
```

---

## IC-0502: Darcy’s Cinematic Life

- Title: Darcy’s Cinematic Life
- Author (byline): Christa Crewdson
- Work: Random Acts of Comedy
- Publisher: Playscripts, Inc.
- Publication date as stated: Sept 2011
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: DARCY, MOM, BROTHER, LIZA, CHAD, TEACHER, BAILIFF, LAWYER, DAD, TOWNSPERSON 1, TOWNSPERSON 2, TOWNSPERSON 3, STUDENT 1, STUDENT 2
- Teaser before the introduction: Yes
- Spoken words (computed): 1648
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
ACTOR 2: Darcy’s Cinematic Life by Christa Crewdson
```

### Performance text (classify this)

```text
Suggested Roles: Actor 1: Darcy, Lawyer Actor 2: Mom, Brother, Liza, Chad, Teacher, Baliff, Runway Model, Dad, Townspersons 1-3, Bus Options (pantomime), Students 1 and 2

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

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

LIZA: (Breaking into Darcy’s daydreams, she speaks snarkily) Homeroom is over, Darcy!

**********

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

LAWYER: I rest my case. (Bell rings)

********

DARCY: (Pg 103-106) T-minus 22 hours and counting until the field trip. As I stand upon the precipice of the school curb, I await my next horror: the dreaded clothes shopping with mom!

MOM: How was your day? Anything new?

DARCY: The mall. The most horrific place on earth. I would rather travel 100 miles to Indiana to shop rather than come here where everyone shops. With my luck I always run into ...

MOM: Isn't that your friend Liza?

DARCY: Mom, she's not my friend.

MOM: Darcy, she's walking this way, it's rude not to say hello. Hello, Liza.

DARCY: Well, we really have to go. Right mom?

MOM: Bye. Nice to see you. (To Darcy) I don't know what your problem is with her. She seems like such a nice person. Oh! Look at this!

DARCY: Mom's idea of fashion is .. .is ... well...even my superior vocabulary can't find the right word, so I'll use my little brother's favorite word “dorky.” If she had her way, I'd be all buttoned up and in plaid or some other monstrosity. Cut to the first scene in the next movie - The Mom Fashion Show . . . . (Actor 2 walks the runway in very nerdy clothes with lots of attitude. A song plays throughout.) *****

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

LIZA: (Bumps in to Darcy on purpose; sarcastically) Sorry, I didn't see you. Oh, did you buy that cute little outfit at the mall yesterday?

DARCY: Well, at least I made an effort to look like I am going to a museum, not a Britney Spears concert.

LIZA: Well, excuse us. I guess we don't know what to wear to go stand in front of a painting and look at a bunch of dots! ******

DARCY: (Pg 109-110) T-minus 13 minutes until the trip. I can't do it. I have to think of some way out! I could cut off my leg with a pencil. No, that would take too much time. I could fake a demonic possession. No, too Hollywood. I have to face the music, I'm going to have to get on that bus. (Bus doors hisses open) Oh yellow nemesis of mine. I have been awaiting your cruel fate. Ok, this is it. I have exactly 8.5 seconds to survey the seating choices. (DARCY stands in the aisle surveying the seats and the kids Actor 2 characterizes her options in pantomime) Choice one-Lenny the loner. Choice two-Renee the mooch. Choice three-Mr. Donovan, a chaperone. (She sits down gingerly on the very edge of the bus seat and looks miserable.) Finally the museum! (Bus door hisses open) I've been here many times so I know exactly where all the exhibits are. I'll try to share some of my knowledge of art with my fellow classmates. (to Classmate while gazing in awe at a painting) Monet attempted to capture conditions of light and atmosphere with bright colors and lively, broken brush strokes.

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

DARCY: Right, the bus. Just as bad as a dragon. This is one beast I can't conquer. I know my fate. Doomed forever to sit alone or with . . . (Again surveys her options - Actor 2 characterizes her options in pantomime) Ugh.

CHAD: Hey! (He waves her over to sit next to him) (Darcy beams)

DARCY: (to audience) There will come a time when you believe everything is finished. That will be the beginning!
```

---

## IC-0503: The Dreaded Batter Pudding Hurler

- Title: The Dreaded Batter Pudding Hurler
- Author (byline): Spike Milligan
- Work: The Goon Show Scripts, Pgs 25-42
- Publisher: Sphere Books
- Publication date as stated: Jan 1973
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: SHARED, GREENSLADE, FX, HENRY CRUN, MINNIE BANNISTER, SEAGOON, GRYTPYPE, BLOODNOK, ECCLES, MORIARTY
- Teaser before the introduction: Yes
- Spoken words (computed): 1563
- Already set (do not supply): none

### Source block (context only)

```text
Author: Spike Milligan
Book: The Goon Show Scripts, Pgs 25-42
ISBN: 978-0722160794
Publisher: Sphere Books
Date (Month/Year): Jan 1973
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: You thought you were safe.

ACTOR 2: You thought you could hide.

ACTOR 1: You thought that you didn’t really need to use the restroom before the performance . . . but now you’re questioning that decision.

ACTOR 2: Now from the inner-most recesses of the BBC radio vaults and the creative minds of Spike Milligan, Peter Sellers

ACTOR 1: And a short, fat, little guy whose name is Harry Secomb, but who I prefer to lovingly call “Tubby” comes one of the famed Goon Show scripts.

ACTOR 2: The Dreaded Batter Pudding Hurler

ACTOR 1: Created by Spike Milligan, Peter Sellers and “Tubby”

ACTOR 2: Also known as Harry Secomb.
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles

Actor 1: Greenslade (narrator), Minnie Bannister, Seagoon

Actor 2: Henry Crun, Grytpype, Eccles, Moriarty

SHARED: FX (sound effects)

GREENSLADE: (Pg 25-42) The English Channel 1941. Across the silent strip of green-grey water – in England – coastal towns were deserted, except for people. Despite the threat of invasion and the stringent blackout rules, elderly gentlefolk of Bexhill-on-Sea still took their evening constitutionals.

FX: [Sea washing onto beach]

HENRY CRUN: Ohhh, dear, dear, dear, ohh, it's quite windy on these cliffs, Minnie.

MINNIE BANNISTER: Yes, yes, what a nice summer evening, typical English evening.

HENRY CRUN: Mnk yes, the rain is lovely and warm. Minnie, I think I'll take one of my sou'westers off . . . hold my elephant gun.

MINNIE BANNISTER: Oh dear, I don't know what you brought it for, you can't shoot elephants in England you know!

HENRY CRUN: Mnk? Why not?

MINNIE BANNISTER: They're out of season.

HENRY CRUN: Oh. Does this mean we shall have to have pelican for dinner again?

MINNIE BANNISTER: I fear so, I fear so!

HENRY CRUN: Then I'll risk it. I'll shoot an elephant out of season.

GREENSLADE: Listeners who are listening will, of course, realize that Minnie and Henry are talking rubbish; as erudite people will realize, there are no elephants in Sussex. They're only found in Kent. North of a line drawn between two points thus making it the shortest distance.

HENRY CRUN: . . . Well, if that's how it is, I can't shoot any.

MINNIE BANNISTER: Come Henry, we'd better be getting home.

FX: [Metal door slides open]

HENRY CRUN: Minnie, did you hear a gas oven door slam just then?

MINNIE BANNISTER: Don't be silly, Henry! Who'd be walking around these cliffs with a gas oven?

HENRY CRUN: Lady Docker?

MINNIE BANNISTER: Yes, but apart from the obvious ones, who'd want to . . .

FX: [Whoosh! Splat!] (Minnie is hit from behind and crumples in a heap)

MINNIE BANNISTER: Help Henry! I've been struck down from behind, buddy. Heelp!

HENRY CRUN: Mnk - oh dear dear! Poor Minnie! Police! English Police! Law Guardians. . .

FX: [Police whistle]

SEAGOON: Can I help you, sir?

HENRY CRUN: Are you a policeman?

SEAGOON: No, I'm a constable.

HENRY CRUN: Oh, what is the difference?

SEAGOON: They're spelt differently. What's happened to this dear old silver bearded lady?

HENRY CRUN: She was struck down from behind.

SEAGOON: And not a moment too soon. Congratulations, sir.

HENRY CRUN: I didn't do it.

SEAGOON: Coward. . . Now tell me, who did this felonious deed. What's happened to her?

HENRY CRUN: It's much too dark to see, strike a light.

SEAGOON: Not allowed in blackout. We daren't. Why, only twenty-eight miles across the Channel the Germans are watching this coast. [to audience] We tried using a candle, but it wasn't very bright and we daren't light it, so we waited for dawn, and there, in the light of the morning sun, we saw what had struck Miss Bannister. It was . . . A batter pudding!

FX: [Dramatic chord]

SEAGOON: Well, get her off this cliff, it's dangerous. Meantime, I must report this to the Inspector. I'll call on you later, goodbye. [to audience] That night I lay awake in my air-conditioned dustbin thinking; now who on earth would want to strike another with a batter pudding? Obviously it wouldn't happen again, so I fell asleep. Nothing much happened that night, except that I was struck with a batter pudding.

GREENSLADE: In the months to come, thirty-eight batter puddings were hurled at Miss Bannister. A madman was at large, Scotland Yard was called in.

GRYTPYPE: Inspector Seagoon, my name is Hercules Grytpype-Thynne, Special Investigation. This Batter Pudding Hurler... He's made a fool of the police.

SEAGOON: I disagree, we were fools long before he came along.

GRYTPYPE: You silly twisted boy. Nevertheless, he's got to be stopped, now Seagoon . . . these batter puddings, they were obviously thrown by hand.

SEAGOON: Not necessarily. Some people are pretty clever with their feet.

GRYTPYPE: [with a strange look at Seagoon] Now, Seagoon, these batter puddings, were they all identical.

SEAGOON: All except the last one. Inside it, we found this . . .

GRYTPYPE: What? An army boot!? So the dreaded hurler is a military man. Any troops in the town?

SEAGOON: The fifty-sixth Heavy Underwater Artillery.

GRYTPYPE: Get there at once, arrest the first soldier you see wearing one boot. Off you go!

FX: [Transition music – Should be somewhat recognizable military music]

SEAGOON: Major Bloodnok, [salute] I must ask you to parade your men. I'm looking for a criminal.

BLOODNOK: You find your own, it took me years to get this lot! [pause to contemplate the situation] Very well then, Bugler Max Geldray? Sound fall in the hard way.

FX: [Musical interlude: 'They Were Doing The Mambo'] (* see http://www.youtube.com/watch?v=kwDL-Bp8yP8 for music as troops assemble)

BLOODNOK: Silence, silence lads, silence! I'm sorry I had to get you out of bed in the middle of the day, but I'll see you get extra pay for this, I promise you. Now, Seagoon, which is the man?

SEAGOON: I walked among the ranks looking for the soldier with one boot, but my luck was out, the entire regiment were barefooted.

ECCLES: We want our beddy byes.

SEAGOON: Who are you?

ECCLES: Lance Private Eccles, sir.

SEAGOON: [to audience] I inspected the man closely, he was the nearest thing I'd seen to a human being, without actually being one. At last, by the light of a passing glue factory, I saw that Eccles was only wearing, one boot!

ECCLES: Well, I only got one boot.

SEAGOON: I know, but why are you wearing it on your head?

ECCLES: Why? Why? It fits, dat's why! What a silly question to ask . . .

SEAGOON: Let me see that boot! [to audience] Mmmmm, size nineteen . . . [to Eccles] What size head have you got?

ECCLES: Size nineteen.

SEAGOON: Curses, the man's defense was perfect. Major Blooknok? Where's this man's other boot?

BLOODNOK: Stolen.

SEAGOON: By whom?

BLOODNOK: A thief.

SEAGOON: You sure it wasn't a pickpocket?

BLOODNOK: Positive, Eccles never keeps his boots in his pocket.

SEAGOON: [to audience] Damn! They all had a watertight alibi. Months went by; I couldn't stop them. Still no sign of the Dreaded Hurler. Finally I walked the streets of Bexhill at night disguised as a human man. Then suddenly...

FX: [A sinister and dramatic fanfare]

SEAGOON: . . . Nothing happened. But it happened suddenly mark you.

MORIARTY: Pardon me, my friend.

SEAGOON: [to audience] I turned to see the speaker. He was a tall man wearing sensible feet, and a head to match. He was dressed in the full white outfit of a Savoy chef. Around his waist were tied several thousand cooking instruments. And behind him he pulled a portable gas stove from which issued forth the smell of batter pudding.

MORIARTY: Could I borrow a match? You see my gas has gone out and my batter pudding was just about to start browning.

SEAGOON: Certainly, here . . . No, no, no . . . Keep the whole box, I have another match at home.

MORIARTY: So rich! Well, thank you m'sieur, you have saved my batter pudding from getting cold. As you'll agree there's nothing quite so bad as being struck down with a cold batter pudding. Well, good night.

SEAGOON: I watched the strange man as he pulled his gas stove away into the darkness. But I couldn't waste time watching him, my job was to find the Dreaded Batter Pudding Hurler!

GREENSLADE: Those who think that Seagoon is not cut out to be a detective, please write to him care of Rowton House.

SEAGOON: [to audience] On December 25th the Hurler changed his tactics. That day Miss Bannister was struck with a Christmas Pudding.

GRYTPYPE: [reading a letter] A Miss Bannister has just received this letter. It was postmarked 'Africa', and inside was a portion of batter pudding.

SEAGOON: So he's in Africa, now we've got him cornered. I must leave at once.

GREENSLADE: Seagoon travelled by sea. To avoid detection by enemy U-boats he spoke German throughout the voyage and was heavily disguised as a Spaniard.

SEAGOON: [to audience] The ship was disguised as a train, to make the train sea-worthy it was done up to look like a boat and painted to appear like a tram. Also on board were Major Bloodnok and his regiment. When we were ten miles from Algiers, we heard a dreaded cry.

ECCLES: Mine ahead woohoowoo! Dirty big mine ahead!

FX: [Explosion]

SEAGOON: Bloodnok and I floundered in the cruel sea.

FX: [Lapping waves]

BLOODNOK: Fortunately, we found a passing lifeboat and dragged ourselves aboard.

SEAGOON: We had no oars, but luckily we found two outboard motors and we rowed with them. For thirty days we drifted to and fro, then hunger came upon us.

BLOODNOK: Aeioughhhhh, if I don't eat soon I'll die of hunger, and if I die I won't eat soon. Wait a moment, [sniffs] ohohohh, can I smell cooking or do my ears deceive me?

SEAGOON: He was right, something was cooking. There, in the other end of the lifeboat was. . . a gas stove! Could this be the end of our search?

BLOODNOK: I'll knock on the oven door.

FX: [Knocking on metal]

MORIARTY: [Faintly] Just a minute please, I'm in ze bath...

FX: [Door scrapes open]

SEAGOON: Don't move, I arrest you as the Dreaded Batter Pudding Hurler.

MORIARTY: Sacre Bleu!

SEAGOON: Hands up, you devil, don't move! This finger is loaded.

MORIARTY: If you kill me, I promise you, you'll never take me alive.

BLOODNOK: Wait, how can we prove he's the hurler?

SEAGOON: That batter pudding in the corner of the stove is all the evidence we need. We've got him!

FX: [Dramatic fanfare]

GREENSLADE: But it wasn't so easy. Forty days they drifted in an open boat.

FX: [Lapping waves]

BLOODNOK: Oooaeioughhhh, I tell you Seagoon, let's eat the batter pudding or we'll starve!

SEAGOON: No, yer hear me, No! That's the only evidence we've got.

BLOODNOK: We must eat it or die.

SEAGOON: Never!

GREENSLADE: And that, we fear, is the end of our story, except of course, for the end. Should Seagoon eat the batter pudding and live, or leave it and in the cause of justice, die? Send your suggestions on a piece of batter pudding.
```

---

## IC-0504: Elephant’s Graveyard

- Title: Elephant’s Graveyard
- Author (byline): George Brant
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: April 2010
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 1, ACTOR 2, HUNGRY TOWNSPERSON, ENGINEER, RINGMASTER, YOUNG TOWNSPERSON, TOGETHER, MUDDY TOWNSPERSON, STRONGMAN, CLOWN, TRAINER, YOUNG TOUNSPERSON, TOUR MANAGER, MARSHAL, STEAM SHOVEL OPERATOR, PREACHER, MUDDY TONSPERSON
- Teaser before the introduction: Yes
- Spoken words (computed): 1647
- Already set (do not supply): none

### Source block (context only)

```text
Author: George Brant
ISBN: 978-0573698156
Publisher: Samuel French, Inc.
Date (Month/Year): April 2010
NIETOC
MN State Qualifier
Historical Reference material:
https://rarehistoricalphotos.com/murderous-mary-1916/
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Her nickname, “Big Mary,” came well-earned.

ACTOR 2: Touted as “The Largest Living Land Animal On Earth,” the five-ton elephant stood taller than the popular Barnum & Bailey’s star, Jumbo, hovering over him by a supposed three inches.

ACTOR 1: Playing musical instruments, standing on her head, and even catching baseballs, this gentle giant awed crowds all over the country.

ACTOR 2: Mary’s future would find an expiration date, however, when the circus made its way to Tennessee.

TOGETHER: Based on true events . . . Elephant’s Graveyard by George Brant
```

### Performance text (classify this)

```text
Suggested Roles

ACTOR 1: Hungry Townsperson, Ringmaster, Clown, Tour Manager, Marshal, Steam Shovel Operator

ACTOR 2: Engineer, Young Townsperson, Muddy Townsperson, Strongman, Trainer, Preacher

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

HUNGRY TOWNSPERSON: (Pg 10) It was September and there was a Town . . . Erwin, Tennessee

ENGINEER: It was September and there was a Town and a Circus

RINGMASTER: Sparks World Famous Shows Proudly Presents . . .

YOUNG TOWNSPERSON: an Elephant . . . Mary . . . (Pg 15) We dreamed her before we saw her.

TOGETHER: (Pg 16) Mary! Mary! Mary!

MUDDY TOWNSPERSON: (Pg 15) She was plastered on every telephone pole.

RINGMASTER: (Pg 16) Ladies and Gentlemen, Children of All Ages!

STRONGMAN: Proudly present a tremendous exhibition of wealth and splendor

CLOWN: All new for 1916.

TRAINER: Starring Mary: the largest living land animal on Earth.

YOUNG TOUNSPERSON: (Pg 15) The Circus was coming!

TOGETHER: (Pg 16) Mary! Mary! Mary! (beat)

TOUR MANAGER: (Pg 10) And there was as Man with Red Hair. (A train whistle)

RINGMASTER: (Pg 17) An elephant is an investment. You’ve got the trained seals, the trapeze, the Strongman. Fine, but they aren’t the bread and butter. No rubberneck comes to a circus doesn’t have a big elephant.

TRAINER: They love a parade. All elephants do in the wild anyway. Wild elephant herd follows the leader and the leader is the biggest female. So they all march behind Mary, one behind the other. Let me tell ya, only thing better than watchin’ an elephant parade is being in the elephant parade. Sittin’ on top of the world – on top of Mary, legs wrapped around her back, head in the clouds.

TOUR MANAGER: (Pg 18) They’re not just for show. Hardest workers I got. Once that train stops in a town – they’re mine. Get ‘em to load and unload the boxcars, push up the tent poles. . . (beat) Tennessee started off with a bang. Circus can tell how it goes over by how many locals want to run away with it afterwards. Fifteen —That was a record.

CLOWN: (Pg 19) There was a Man with Red Hair

TOUR MANAGER: (Pg 20) Shocka red hair. Tells me he’s good with animals. He says, I want to work with the elephants, I have to work with the elephants.

TRAINER: (Pg 21) Lou knocks on my car, tells me I got a new roommate. Goofy-lookin’ red-haired guy. I show Red his corner. He gripes about the smell and I tell him get used to it. Townies think elephants smell bad in the ring, try sleepin’ with one in a boxcar. He shuts up when he sees Mary, looks at her like she’s the answer to his prayers.

TOUR MANAGER: We left Kingsport for Erwin. (A train whistle)

TRAINER: (Pg 24) I’d shown Red how to feed her, groom her, that’s it. That’s all he knew. One day. One day! What the hell can you learn in one day? In India, guy stays with an elephant his whole life, like a marriage. Here. . . Lou waltzed in—says . . .

TOUR MANAGER: (Pg 25) Shorty, he wants to ride Mary in the march. Back off and give the new guy a chance.

TRAINER: I shoulda said something. I shoulda told him she was mine. I didn’t. Just stepped aside. Maybe made a face. That was my big protest, a face. (beat) It’s trust. Trust you build up over years, not one day. Every peanut, every bath, every pat on the trunk. It’s love. But Red didn’t have time for any of that. (beat) TRUNKS UP! (Circus music as the parade begins)

YOUNG TOWNSPERSON: (Pg 26) That big elephant was leadin’ the whole thing. That goofy guy – red hair? He was up on her back.

TOGETHER: Mary, Mary, Mary!

HUNGRY TOWNSPERSON: (Pg 27-28) A band was playin, people rushin’ out, circus plowin’ through the middle of town . . . Erwin Garbage Department on strike until further notice. Clean up your own junk, people of Erwin. We on strike. And thus, the Holy Grail of Garbage left in the mud: a juicy chunk of watermelon. That’s when the dominoes start to fallin’ Elephant see melon . . . walks toward [it].

Elephant rider encourages elephant to abandon melon – is most insistent. Elephant hook across [its] head. Breaks elephant hook across [its] tusk.

Elephant decides she’s had enough – picks the rider off [its] back and throws [him] into a soda pop stand.

[Just when] the rider thinks it’s over, the elephant walks over and puts [its] foot on [his] head. (scream) [And his] head explodes.

MUDDY TOWNSPERSON: (Pg 29) She stepped on his skull. Crushed it. (beat) Coulda been any of us.

MARSHAL: (Pg 30) It coulda ended there, but that wouldn’ta been right, that wouldn’ta been justice. It wasn’t walking away from this. Erwin don’t look kindly upon murderers.

TOUR MANAGER: (Pg 31) Tried to get in touch with Red’s family, friends. Didn’t have none.

TRAINER: Like he didn’t exist except for us, like he was born to do nothin’ but cause us trouble.

RINGMASTER: Still have a show to do that night. Must go on. DOORS!

TOUR MANAGER: I told Charlie, maybe we should keep Mary out, maybe the people’d forget. But he told me what I already knew:

RINGMASTER: They won’t forget. Aren’t coming to see the circus. Coming to see the killer. (Pg 32) Ladies and Gentlemen, Children of All Ages . . . Sparks World Famous Shows Proudly Presents . . .

TOUR MANAGER: Normal night we play up the danger, talk up the toothless tier. Not this time. Brought Mary out like she was the most innocent a’ God’s creatures. (Drum roll / cymbal crash. A gasp)

TOGETHER: (Pg 33) Kill it. Kill it. Kill it!

YOUNG TOWNSPERSON: It got louder . . .

TOGETHER: Kill it. Kill it. Kill it!

YOUNG TOWNSPERSON: The marshal and people were wavin’ guns around. Everybody shoutin’. All ‘cept the colored section.

CLOWN: No, no, no! Red was one of us. Part of the circus. He knew the risks. You townies go no claim here. Military has its own court – so does the circus.

TRAINER: She was favoring her left tusk! They have nerves in there, big ones, run down half the tooth. You all saw him hittin’ her tusk with the hook, whackin’ the spit outta it, tryin’ to get her to behave, to stay in line. What’s she s’posed to do? She stopped him. That’s all. She stopped him!

TOGETHER: Kill it. Kill it. Kill it!

YOUNG TOWNSPERSON: (Pg 34) Fin’ly the Ringmaster raised his hand.

RINGMASTER: (Pg 35) (hand raised) Ladies and Gentlemen, Children of All Ages – the Circus Understands Your Wishes. Theis Mary Matter Will Be Settled to Your Liking Tomorrow . . . and We are Open to Suggestions.

ENGINEER: (Pg 36) They talked about electrocuting it, frying it like some of them had seen in the moving picture Thomas Edison made. But that was copycat stuff. (beat) The railyard. There’s a crane there can lift 100 tons. Now, something like that could do something special, something never been done before. Something like that could hang her. Hang her like any other murderer.

MUDDY TOWNSPERSON: Eye for an eye. Erwin’ll fin’ly be clean.

TRAINER: (Pg 37) (sadly) So now Lou and Sparks need my help. (to the men) I wasn’t good enough to handle her while she was alive, but I’m good enough to help you kill her? (beat) I will never forgive you; (to audience) [but] I stay ‘cause if I don’t, they’ll mess it up.

MUDDY TOWNSPERSON: (Pg 41-42) Mornin’ fin’ly came. Got to the railroad tracks, saw men in the only suits they owned. Women in their Sunday best, prancin’ ‘round with parasols like it was Easter. People standin’ top of boxcars, picknic baskets, punch. Laughin’, dancin’. You could feel it – we were ready.

TRAINER: TRUNKS UP! (marching drums)

STEAM SHOVEL OPERATOR: The killer was in front. Them elephants marched out holdin’ each other’s tails with their trunks – like a parade.

TRAINER: (Pg 37) Tuskers aren’t stupid, they know when somethin’s up. You have to make her think it’s a normal march. She can’t go out there alone. Mary has to lead the parade, like it’s any other parade.

STEAM SHOVEL OPERATOR: (Pg 42) They walked through the railyard up to the crane, and this guy chained the killer’s foot to a train track.

TRAINER: (calming Mary down) It’s okay, it’s okay, it’s okay. Ready? Showtime, sweetie.

STEAM SHOVEL OPERATOR: The guy hooked the chain ‘round her neck, patted her back and stood up. (applause)

YOUNG TOWNSPERSON: She looked scary.

PREACHER: (Pg 44) Helpless.

STEAM SHOVEL OPERATOR: Confused.

MUDDY TOWNSPERSON: Guilty.

MARSHAL: Like a killer.

ENGINEER: The crane groaned, gears grindin and --- (gasp)

MUDDY TONSPERSON: It rose up steady till it was standin’ on it’s hind ligs, tiptoe. Toenails scrapin’ the railroad track . . . like it was doin’ a trick.

MARSHAL: (Pg 45) But then we started wonderin’ why that thing wasn’t goin’ any higher up.

HUNGRY TOWNSPERSON: Nobody remembered to unhook her. Her foot was still chained to the track.

STEAM SHOVEL OPERATOR: They were rippin’ her in half, pullin’ her leg at this weird angle.

MUDDY TOWNSPERSON: Her leg broke – a bone ‘bout as big as my whole body – breakin’, I could feel it in my spine, my spine buckled, ached in sympathy, rang like a tuning fork.

STEAM SHOVEL OPERATOR: Shoulda left then, I s’ose. But I stayed to see ‘em unhook her foot, lift her up again –

PREACHER: (Pg 46) Think she was nearly gone, then. Or woulda been, soon. That is . . . if the chain hadn’t broke.

YOUNG TOWNSPERSON: The chain popped and she came crashin’ down onto the railroad track with this sound like an oak tree crackin’ in half. That guy who climbed her before started screamin’ like he was the one fell down. And they handed him a thicker link chain. And I couldn’t believe it, but he hooked her up again.

MARSHAL: (Pg 47) Crane lifted it off its feet again – higher . . .

YOUNG TOWNSPERSON: Higher . . She made some noises, some . . . air just kinda puffed outta her trunk and then that . . . that was it. (quiet)

MUDDY TOWNSPERSON: (with shock and sadness) I let my breath out. I breathed in, lungs searchin’ for that sanctified air. Waiting to be made clean. But the air . . . it tasted no different. It was flat and stale and rank.

MARSHAL: (Pg 48) (proudly) Look. Look at that thing swing. We hung an elephant today. An elephant. We made the impossible possible. This is America. And we can do anything we dream of. Anything at all!

HUNGRY TOWNSPERSON: (Pg 50) (disgusted) People go short mem’ries. But not me. (beat) All them colored boys led out to the yard must blur together somethin’ fierce, ‘ause nobody ever talk about how they hung colored boys in Erwin. They just talk about how they hung an elephant. Damndest thing. (train whistle)

RINGMASTER: (Pg 52) It was September and there was a Town and there was. Circus and there was a Man with Red Hair and there was an Elephant. (beat) You wait . . . After midnight, after the townsfolk have gone home and the prying eyes of Erwin are closed; sleeping with the certainty that their boogie monster is dead; You wake up the clowns and tell them to digger he up. Saw off her tusks and being them to you. You have to see what you can salvage, what you can get for the ivory. An elephant is an investment.
```

---

## IC-0505: Fantastic Mr. Fox

- Title: Fantastic Mr. Fox
- Author (byline): Roald Dahl
- Work: Not specified
- Publisher: Puffin
- Publication date as stated: June 1998
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 2, NARRATOR 2, NARRATOR 1, MR. FOX, BOGGIS, BUNCE, BEAN, MRS. FOX, BADGER, RAT, TOGETHER, MR.FOX
- Teaser before the introduction: Yes
- Spoken words (computed): 1537
- Already set (do not supply): none

### Source block (context only)

```text
Author: Roald Dahl
ISBN: 978-0141301136
Publisher: Puffin
Date (Month/Year): June 1998
```

### Introduction (context only: never use it for content warnings)

```text
Someone's been stealing from the three meanest farmers around, and they know the identity of the thief—it's Fantastic Mr. Fox! Working alone they could never catch him; but now fat Boggis, squat Bunce, and skinny Bean have joined forces, and they have Mr. Fox and his family surrounded. What they don't know is that they're not dealing with just any fox—Mr. Fox would rather die than surrender. Only the most fantastic plan can save him now.

Nobody outfoxes the . . . Fantastic Mr. Fox by Roald Dahl
```

### Performance text (classify this)

```text
Suggested Roles: ACTOR 1: Narrator 1, Mr. Fox, Boggis, Bean, Rat

ACTOR 2: Narrator 2, Bunce, Mrs. Fox, Badger

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

NARRATOR 2: (Pgs 1-4) Down in the valley there were three farms. The owners were rich, nasty men: Farmer Boggis, Farmer Bunce and Farmer Bean.

NARRATOR 1: Boggis was an enormously fat chicken farmer. (Actor 1 mimes Boggis) He ate three boiled chickens smothered with dumplings every day for breakfast, lunch and supper.

NARRATOR 2: Bunce was a duck-and-goose farmer. (Actor 2 mimes Bunce) He was a pot-bellied dwarf. His food was doughnuts and goose livers. He mashed the livers into a disgusting paste and then stuffed the paste into the doughnuts.

NARRATOR 1: Bean was a turkey-and-apple farmer. (Actor 1 mimes Bean) He never ate any food at all. Instead, he drank gallons of strong cider which he made from the apples in his orchard. He was as thin as a pencil and the cleverest of them all.

NARRATOR 2: (Pgs 7-9) On a hill above the valley lived Mr. and Mrs. Fox and their four small foxes. Every evening as soon as it got dark Mr. Fox would say . . .

MR. FOX: Well, what shall it be this time? A plump chicken from Boggis? A duck or a goose from Bunce? Or a nice turkey from Bean?

NARRATOR 2: And Mr. Fox would creep down into the valley in the darkness of the night and help himself.

BOGGIS: Dang and blast that lousy beast!

BUNCE: I'd like to rip his guts out!

BOGGIS: How on earth can we catch the blighter?

BEAN: (picking his nose delicately) I have a plan. Tomorrow night we will all hide just outside the hole where the fox lives. . . wait there until he comes out. Then. . . (mimes a shotgun) Bang! Bang-bang-bang!

MR. FOX: (Pg 10-14) What shall it be tonight?

MRS. FOX: Bring us two fat ducks, if you please. One for you and me, and one for the children. Just don't get careless. You know they'll be waiting for you, all three of them.

MR. FOX: Don't you worry about me. I’ll see you later.

NARRATOR 2: But Mr. Fox would not have been quite so cocky had he known the three farmers were waiting just outside the entrance to the hole, each one crouching behind a tree with his gun loaded.

MR. FOX: (creeping to the mouth of his hole, he pokes his face out and sniffs)

BEAN: (mimes a shotgun) Bang-bang! Bangbang! Bang-bang! (to the others) Did we get him?

(he finds the remains of a fox’s tail and picks it up, disappointed) We got the tail but we missed the fox.

BUNCE: He won't be poking out again in a hurry.

BEAN: It'll take three days at least before he gets hungry enough to come out again. I'm not sitting around here waiting for that. Let's dig him out!

MR. FOX: (Pg 15-19) (Glumly while Mrs. Fox tends to his tail) It will never grow again. I shall be tail-less for the rest of my life. I suppose I'm lucky to be alive at all. And now they've found our hole, we're going to have to move out as soon as possible. We'll never get any peace if we. . . What was that? (turns his head sharply and listens)

NARRATOR 2: Suddenly there was an especially loud crunch above their heads and the sharp end of a shovel came right through the ceiling.

MR. FOX: Come on! There's not a moment to lose! (beginning to dig) Nobody in the world can dig as quick as a fox! Go downwards! We've got to go deep! (frantic digging)

MRS. FOX: (panting for breath; to their children) I should like you to know that if it wasn't for your father we should all be dead by now. Your father is a fantastic fox.

BOGGIS: (Pg 20-22) (exhausted from digging) Dang and blast! Whose rotten idea was this?

BEAN: (angrily) Listen. I'm going to get that fox! I'm not giving in till I've strung him up over my front porch, dead as a dumpling! What we need is machines . . . mechanical shovels!

NARRATOR 2: Soon, two enormous caterpillar tractors came clanking into the wood. They were murderous, brutal-looking monsters. Now there began a desperate race, the machines against the foxes.

BUNCE: (Pg 27) Hey there, Mr. Fox! We're coming to get you now!

MR. FOX: (Pg 23) Tractors! And mechanical shovels! Dig for your lives! Dig, dig, dig!

BOGGIS: (Pg 27) You've had your last chicken! You'll never come prowling around my farm again!

NARRATOR 2: (Pg 29) At six o’clock in the evening. Bean switched off his tractor and climbed down from the driver's seat. Bunce did the same. Both men had had enough. (Pg 28) The hole was like the crater of a volcano.

BOGGIS: (Pg 29-30) Dang and blast that filthy stinking fox! What the heck do we do now?

BEAN: There's only one thing to do. We starve him out. We camp here day and night watching the hole. He'll come out in the end. He'll have to.

NARRATOR 2: (Pg 34-36) For three days and three nights this waiting-game went on. Down in the tunnel the foxes were slowly but surely starving to death.

MR. FOX: (deep in the new tunnel) I’ve just had an idea. It means more digging.

NARRATOR 2: (Pg 38-39) For a long, long time Mr. Fox and the children kept on digging. Slowly, wearily, the foxes began to slope the tunnel up towards the surface.

MR. FOX: (Pg 40) (cautiously poking his head up through the gap; he shrieks in excitement) I've done it! I've done it (pulls himself up though the gap and starts dancing with joy) Come up and see where you are! Hallelujah! Hooray! Hooray! Boggis's Chicken House Number One! Isn't that fantastic!

NARRATOR 2: Mr. Fox chose three of the plumpest hens, and with a clever flick of his jaws he killed them instantly.

BADGER: (Pg 46-47) (a deep voice from the shadows) Who goes there?

MR. FOX: Badger!

BADGER: Foxy! Haven't you heard what's happening up on the hill? It's chaos! Half the wood has disappeared and there are men with guns! What on earth are we going to do, Foxy? None of us can get out, even at night! I think we're finished!

MR. FOX: Who is we?

BADGER: All us diggers. Me and Mole and Rabbit and all our wives and children. Even Weasel, who can usually sneak out of the tightest spots, is right now hiding down my hole with Mrs. Weasel and six kids.

MR. FOX: (Pg 42) handing the hens to one of the children) Run back with these to your mother. Tell her to prepare a feast. [We’ll] be along in a jiffy, as soon as we have made a few other little arrangements. (Pg 49) (to Badger) You have come just at the right moment, my dear Badger. You can help us dig.

BADGER: (Pg 58-59) (while they are digging) Doesn't this worry you just a tiny bit, Foxy? All this. . . this stealing.

MR. FOX: (looks at Badger as if he is crazy) My dear old furry frump. do you know anyone in the whole world who wouldn't swipe a few chickens if his children were starving to death? (Pg 60-61) We shall simply take a little food here and there to keep us and our families alive. Right?

NARRATOR 2: Five minutes later, Badger's front paws hit against something flat and hard. It was a wall. But it was built of bricks, not stones. Mr. Fox saw that the cement between the bricks was old and crumbly (Mr. Fox and Badger begin loosening bricks)

RAT: Go away! You can’t come in here! It’s private!

BADGER: Good Lord! It’s Rat! (Pg 74) All rats have bad manners. I've never met a polite rat yet.

MR. FOX: (Pg 62) (smiling widely and speaking softly) My dear Rat, I am a hungry fellow and if you don't hop it quickly I shall eat-you-up-in-one-gulp!(Mr. Fox and Badger break down the wall and climb through) (Pg 64-66) Bean's Secret Cider Cellar. It will make the feast into a banquet!

BADGER: Cider is especially good for Badgers. We take it as medicine -- one large glass three times a day. (drinks deeply) Oh, Foxy, it's like drinking sunbeams and rainbows!

RAT: You're poaching! Put that down at once! There'll be none left for me! If you great clumsy brutes come messing about in here, we'll all be caught!

NARRATOR 1: (Pg 71) Mr. Fox and Badger ran across the cellar clutching a gallon jar each.

RAT: Thieves! Robbers! Bandits! Burglars!

NARRATOR 2: (Pg 72-73) Along the tunnel they flew. . . past Boggis's Chicken House Number One and then up the long home stretch towards the place where they knew Mrs. Fox would be waiting.

NARRATOR 1: (Pg 74-75) They rounded the final corner and burst in upon the most wonderful sight they had ever seen. The feast was just beginning. A large dining-room had been hollowed out of the earth, and in the middle of it, seated around a huge table, were no less than twenty-nine animals.

NARRATOR 1: Foxes and badgers

NARRATOR 2: Moles and rabbits

TOGETHER: Weasels!

NARRATOR 1: (Pg 76-77) You must remember no one had eaten a thing for several days. They were ravenous. So for a while there there was only the sound of crunching and chewing as the animals attacked the succulent food. (chewing, burping, assorted other noises) At last, Badger stood up.

BADGER: (raising his glass of cider) A toast! To our dear friend who has saved our lives this day -- Mr. Fox.

TOGETHER: (shouting) To Mr. Fox! Long may he live!

MRS. FOX: (shyly) I don't want to make a speech. I just want to say one thing: MY HUSBAND IS A FANTASTIC FOX.

TOGETHER: (cheering and clapping)

MR. FOX: (Pg 78-81) (grinning hugely) Thank you. But now, my friends, let us be serious. Let us think of tomorrow and the days after that. If we go out, we will be killed. Right?

TOGETHER: (shouting) Right!

MR.FOX: But who wants to go out, anyway? We are all diggers. We hate the outside. We only go out because we have to, to get food for our families. But now, my friends, we have a safe tunnel leading to the finest stores in the world! It means that none of us need ever go out into the open again! I invite you all to stay here with me forever.

TOGETHER: Forever!

MR. FOX: We will make an underground village, with streets and separate houses for Badgers and Moles and Rabbits and Weasels and Foxes. And every day we will eat like kings.

TOGETHER: (cheering and clapping)

NARRATOR 1: Outside the Fox’s hole, Boggis and Bunce and Bean sat with their guns on their laps. It was beginning to rain. Water was trickling down the necks of the three men and into their shoes.

BOGGIS: (miserably) He won't stay down there much longer now.

NARRATOR 1: [And] they sat there by the hole, waiting for the fox to come out.

NARRATOR 2: So far as [we] know, they are still waiting.

BEAN: (sneezes loudly)
```

---

## IC-0506: Get Up, Stand Up - Station 19 (Season 4, Episode 12)

- Title: Get Up, Stand Up - Station 19 (Season 4, Episode 12)
- Author (byline): Krista Vernoff
- Work: Not specified
- Publisher: TVShowTranscripts.ourboard.org
- Publication date as stated: Aired April 22, 2021
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 2, MAYA, DR. LEWIS, TRAVIS, ANDY, JACK
- Teaser before the introduction: Yes
- Spoken words (computed): 2454
- Already set (do not supply): none

### Source block (context only)

```text
Author: Krista Vernoff with contributions from Station 19’s writing/support staff and cast
ISBN: N/A
Publisher: TVShowTranscripts.ourboard.org
Date (Month/Year): Aired April 22, 2021
Full Transcript can be found at
https://tvshowtranscripts.ourboard.org/viewtopic.php?f=847&t=43548
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Eight minutes and 46 seconds.

ACTOR 2: That's how long a white Minneapolis police officer knelt on George Floyd's neck, while he was handcuffed and face down on the pavement, screaming out that he couldn't breathe.

ACTOR 1: Floyd's murder on May 25, 2020, sparked a renewed effort against police brutality and systemic racism.

ACTOR 2: In April 2021, ABC’s Station 19 aired an episode hailed as one of the most powerful reflections of George Floyd’s murder on television.

ACTOR 1: In this selection we find 4 of Station 19’s non-black first responders struggling to understand, empathize and cope with their own visceral responses as they work through their emotions with Counselor Dr. Diane Lewis.

TOGETHER: Get Up, Stand Up by Krista Vernoff
```

### Performance text (classify this)

```text
To be performed by white/black duo team – Dr. Lewis is black and could be played by an actor of any gender, all other characters are white.

NOTE: White actor should be prepared to play both masculine and feminine roles.

Characters:

Diane Lewis: Black grief counselor. In the wake of national outcry after the murder of George Floyd, Captain Maya Bishop brings in Dr. Lewis to grief counsel the team.

Maya Bishop: Current Fire Chief at Station 19 – a white woman who has worked her way up in the ranks. Ambitious but dealing with the aftereffects of childhood emotional and verbal abuse.

Travis Montgomery: Mixed race (Chinese/White); openly gay

Andy Herrera: Latina, her father was the former Fire Chief at Station 19. She is recently married to black firefighter Robert Sullivan.

Jack Gibson: White male who grew up in the foster care system. He struggles with the concept of white privilege.

ACTOR 2: with contributions from Station 19’s writing/support staff and cast.

MAYA: (Enters breezily) Any takers?

DR. LEWIS: Just one, so far. And you. What? Sit.

MAYA: No, I'm not . . .

DR. LEWIS: You're what? You're. . . You're. . . You're not grieving? You had a happy little firehouse where everyone was best friends and racial disparity was not a hot topic. And now? Everything has changed. Everything and nothing.

MAYA: I know fire. I mean, I'm the person that studies them for fun. But this fire. . . This fire is beneath our feet. It's built into every foundation. . . Our history, language, n-news coverage. It's everywhere. I mean, we vent fires to let out the hot smoke and gasses so that we can contain the fire, but I don't see how we can contain this, let alone put it out. And growing up, we were taught about Black history and the Civil Rights movement. We were taught to believe that they had beat it. And I think, on some level, that belief was still inside of me and I am so embarrassed saying that to you.

DR. LEWIS: Well, you were taught that in school. . . and probably also at home. And that teaching, it's the coal that keeps the fire hot. When I was a child and I learned about the Native American genocide, I pictured one small village. . . One small village of men with feathers in their hair who gave the white people turkey and then got mad that they wouldn't leave. Now, I pictured it because those were the literal pictures in my history books. And even though I knew that my people had been stolen from their homes and brought here chained up on ships, somehow, I believed that textbook. I was 35 years old when I learned that in 1492, Columbus sailed the ocean blue, and in the wake of that, millions upon millions of people who had been living here for 15,000 years were extinguished. And the ones who survived were fighting every day against a culture that still wants to pretend they don't exist. We learn when we learn. And the shame we feel at having taken so long to learn, well, that can be useful as long as we use it well. Once we know better, we have to do better.

MAYA: When I was 13, I ran cross country and track, and during the off-season, my dad would train a group of us girls who ran both. And he would push us too hard, and when I didn't hit a drill the way he wanted me to. . . he'd make me do it over and over and over until I would collapse on the ground. And my dad would leave me there, and one by one, my team members would lie down next to me. Face to the concrete, eyes on me, silent. Giving me space, but. . . also making sure I wasn't alone. And my instinct is that that is what I have to do for the Black members of my team... To quietly show up and let them know that I support them. But I think that instinct is wrong, because when my friends and I were 13, we didn't have the capacity to stand up against an abusive power. And now I do. I. . . I have the power to stand up and say when something is wrong. I mean, I have the power to call out injustices when I see them. I have. . . the power to make sure that everyone can breathe. I want to tell everyone that I support them attending the protests. I want to go. I don't want to silently support anymore. I want to scream in the streets. (beat) But The Department won't like it. (Sighs) I'm on a track, and if I support this publicly. . . Which everything in me wants to do. . . It'll take me off that track. Firefighters work with the police, okay? They're our brothers, too, and there are some bad apples, bu. . . after we all saw the horrific video, why aren't all the brothers. . . Why aren't all the friends. . . Why isn't every member of the police force in the streets demanding systemic change? Why? Because it'll take them off of the track. ****** Scene*******

DR. LEWIS: (Travis enters, stands awkwardly. He is visibly upset, then attempts to leave) You know, the Department pays me no matter what, but, uh, there's only so many crossword puzzles I can do, so. . . (Laughs) You want to talk?

TRAVIS: Oh, no. I mean, I. . . I want to let the Black firefighters go first.

DR. LEWIS: Do you see a line outside this door? I-I know the past couple months can't have been easy for you, either. Hate crimes are hate crimes, no matter the race.

TRAVIS: My mom got, uh. . . Well, she was spit on at the grocery store. . . Mm . . . the same day that George Floyd. . . My, uh. . . My mom was leaving, and a crazy maskless woman was like. . . "If this Kung Flu is real, it's because of people like her. The woman both didn't believe COVID was real and was blaming my mom for it. (Whimpers) When my mom told me, it actually felt like my organs were melting. I was so hot with rage, you know, remembering the times when I was a kid, and, you know, people would say stuff to us. And then, we would just go home. Never to be discussed again. And I. . . And I didn't say anything to anyone here about it because, you know, it didn't feel appropriate. This giant, massive thing was happening. . . A hate crime. (Whimpering; sobbing) An atrocity so much more brutal and egregious. You know, other people were hurting so much more. I'm sorry. I don't know why I'm talking to you about this. I don't know why I'm doing that.

DR. LEWIS: Because I'm a Black woman, and my racist stuff is "bigger"? That doesn't work. (beat) I know that since COVID, hate crimes against Asian Americans have spiked like crazy.

TRAVIS: And yet, no one is talking about it. . . No one but us. Not the media. Not the. . . (Scoffs) I mean, grandmas and grandpas. . . Halmoni and haraboji. People being shoved into walls and off subway platforms. You have Filipina nurses who say goodbye to their families and their own country to come here to work the front lines of a pandemic being attacked in the streets. A 2-year-old and a 6-year-old stabbed at a big-box store. I mean, who stabs a 2- year-old? And why is that not news? Why are we so. . . invisible?

DR. LEWIS: I don't know. I. . . (Sighs) I don't know.

TRAVIS: I don't know either! But how can we even make a fuss when this is all it is relative to how horrifically this country treats Black people? I mean, I watched that whole video, and in addition to the absolute horror that I felt. . . And feel. . . I also thought. . . "What do we have to even complain about?"

DR. LEWIS: Travis, it's all bad. I know you're trying to be generous, but it is all bad. There are no winners in the Oppression Olympics. Okay? And it's gaslighting if anyone tells you or if you tell yourself to be okay with the brutalities being inflicted on your community because worse things are happening to another. (Sighs) *****Scene*****

ANDY: (Enters with a heavy sighs, she gathers her thoughts then burst out angrily) You know, it's always bothered me when men would suddenly see the world differently after they had a daughter. Like, I always wondered why it took them having a daughter in order to open their eyes. But I guess that's how it feels for me now. I'm that guy. (Exhales sharply) The world changed for me because I fell in love with a Black man, and now I see what he sees. You know, I . . . I worry for him every day. I-I've taken on the fear that he doesn't allow himself to feel. I. . . You know, I've always seen it and felt it growing up. I saw my dad go through it. People would call him awful names, and he would. . . He would just walk by, hold his head up high. A-As a kid, people would look at my last name, and they would ask me, "Where are you really from?" (Scoffs) I even had teachers who would look really surprised once they realized that I was smart. But, you know, mostly. . . (Clicks tongue)

(Scoffs)

DR. LEWIS: It's okay to say it.

ANDY: Mostly, I got treated okay because my skin is light. I pass for white.

DR. LEWIS: And you feel guilty about that?

ANDY: (Clicks tongue) I. . . You know. . . (Clears throat) I swear to God, I don't even know how I feel. I feel. . . (Stammers) I feel betrayed. I mean, j. . . I know it's always been this way, but I needed to love a Black man. . . I needed to be married to a Black man. . . in order to see the whole picture? Why? Why? Where was my call for justice? Like, why didn't I see this before? W. . . Why am I just waking up now?

DR. LEWIS: A lot of people are waking up now, and they're asking themselves the same questions. And you. . . You're the daughter of a fire captain. Police have been a part of your life since you were a little girl. Cops and firefighters were your family.

ANDY: They would call me Pruitita. It means Little Pruitt. And there was this sort of mental gymnastics going on where, a-as I got older, I thought I knew that police brutality was rampant. But at the same time, I didn't count the cops that I knew personally into that issue. You know, it was double-think. Like, I never stopped and questioned why the good cops weren't calling out the bad ones. You know, not a single one of my dad's old police friends have stepped forward to denounce the actions of the officers that murdered George Floyd? Not a single one.

DR. LEWIS: It is my instinct as a therapist to comfort you, but your comfort. . . and everyone else's comfort. . . has been such a big part of this problem for so long. (Sighs) *****Scene*****

JACK: (Enters sheepishly) I'm sorry. I'm sure I'm not the one you're here to talk to.

DR. LEWIS: I'm here to talk to anyone who needs it.

JACK: I'm afraid to talk to anyone right now. Not just you. . . T-to anyone. I'm afraid I'm gonna get every word wrong, or even one word. Yeah, I know I'm not a racist. Ohh. I-I know that.

DR. LEWIS: You do realize that "I'm not racist" is kind of the. . . the club slogan of racists? And that's because we live in a culture built on white supremacy, so the racism is baked in. And we can't begin to undo it until we name it and own it.

JACK: (frustrated) Okay, see, this is exactly my point. You know, I'm damned if I do, and I'm damned if I don't. Cops take a knee, join the protests, they're called hypocrites. But it can't be that across the board.

DR. LEWIS: Jack, you came in here today looking for some clarity. So, here it is. I know what you mean when you say you aren't racist, and I believe that you do not have hatred in your heart. But you also aren't damned. Not even in the least bit. You're blessed as hell. I know you grew up on the streets in the system, and I'm not diminishing your hardship, but you are . . .

JACK: Yeah, I'm privileged because I'm white. I get it. When I was a kid. . . After that last foster home, there were a few of us who would hunker down to make a place for ourselves. . . squatting. You know, to stay out of the system. Eventually, the cops would find us, and we'd run. And it was scary. But when I was being chased, not once did I think that, "If he catches me, he might kill me." I never feared for my life. But I know some of my friends did. I know I'm privileged, Diane. I watched that video, and I want to blow up the world. And? And... we're firefighters. We need the cops, and they need us. And we can't all of a sudden overnight decide that the whole institution is evil. Some good guys stayed silent, and that makes them bad. Except, they're not actually all bad. They're individuals. And I feel like I'm not allowed to say that. I'm afraid to say anything. Mm. (Inhales deeply)

DR. LEWIS: I was a firefighter, too. I have cop buddies, too. Our cop buddies are not the point. Do you know what the 13th Amendment did? Abolished slavery. Except as a punishment for a crime.

JACK: Yeah, but that was like. . .

DR. LEWIS: That's still the law. It is still legal to enslave Americans as a punishment for a crime. And do you know the statistics of incarcerated Black folks in America? 34%. We are 34% of the prison population, but we only make up 13% of this country's population. That seem right to you? And you're thinking, "Well, that's because more Black people are poor, so they have to resort to crime. So they get arrested more. Sucks for them, but, hey, you do the crime, you do the time." But how many crimes did you commit, Jack, when you were out there on the streets? Did you, uh, steal to eat? Did you run from police? Did you get drunk sometimes and make a mess with your friends?

JACK: Yeah, all of that.

DR. LEWIS: But you never went to prison. Never went to jail. Never had a gun pointed at you. Never have a knee put on your neck. When you make mistakes, you get to learn from them. When people who look like me make any kind of mistake, we go to prison. . . or worse. And way too often, no mistake is needed. We can laugh too loud and they'll arrest us. We can put our hands in the air, and they'll shoot us. It's not in the past. It's now. It's still. And I know you don't have hatred in your heart, Jack. But that's not enough anymore. You have to dig deeper. When you're too uncomfortable to talk and you don't know what to say? That's okay. Listen instead.
```

---

## IC-0507: God’s Favorite

- Title: God’s Favorite
- Author (byline): Neil Simon
- Work: The Collected Plays of Neil Simon, Volume II; Pgs 475 - 548
- Publisher: Penguin Publishing Group
- Publication date as stated: Nov 1986
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: JOE, LIPTON’S VOICE, LIPTON
- Teaser before the introduction: Yes
- Spoken words (computed): 1834
- Already set (do not supply): none

### Source block (context only)

```text
Author: Neil Simon
Book: The Collected Plays of Neil Simon, Volume II; Pgs 475 - 548
ISBN: 978-0452263581
Publisher: Penguin Publishing Group
Date (Month/Year): Nov 1986
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Imagine if God sent a messenger to your house, but instead of a glowing angel with wings,

ACTOR 2: You got Sidney Lipton: a twitchy, cinematic-obsessed person in a "G" sweatshirt who acts like a pizza delivery driver bringing a box full of disasters

ACTOR 1: A cosmic intern who’s just trying to hit his plague-delivery quota so he doesn't get fired.

ACTOR 2: Will Joe renounce the Almighty or will he remain . . .

TOGETHER: God’s Favorite by Neil Simon
```

### Performance text (classify this)

```text
NOTE: Sidney Lipton could be played by either gender. Joe is forlorn and defeated. He sighs mournfully. The room is in darkness except for the moonlight shining through the French door. He looks up and speaks softly and reverently)

JOE: (Pg 494-495) Am I wrong? ... Is all of this too much for one family? If it is, then why did You give it to me? It's enough already, dear Lord. Don't give me any more. . . Just David. Give me back my David . . . If it be Your Will, dear God, that's all I ask. Amen!

LIPTON’S VOICE: (A voice from somewhere in the room itself, is heard) Amen!

JOE: (stops in his tracks, then wheels around, shocked) What? Who's there? Who said that?

LIPTON’S VOICE: Don't worry. It's not who you're thinking.

JOE: Who is it? I can't see you.

LIPTON’S VOICE: I can't see you either. I lost my glasses. Are the lights on or off? I can't see a damn thing.

JOE: Stay where you are! Don't move. I could have the police here in two minutes.

LIPTON’S VOICE: You're lucky. In my neighborhood you could wait for them all night! Would you please turn the lights on? I get very nervous in the dark.

JOE: (Pg 495-509) (turns on lights) All right, now who do you -- (But there is no one there) Where are you? ... WHERE ARE YOU? (He turns around quickly ... Silence. From behind the huge sofa, SIDNEY LIPTON appears, crawling and feeling the rug with his hands)

LIPTON: Don't get excited, I'm just looking for my glasses. (Continues to search. Not a very impressive-looking person, wearing khaki slacks, a thin raincoat, white sweat socks, Hush Puppies, a tweed cap -- a potpourri of cheap clothes) I still can't see. Where am I, on the floor?

JOE: What do you mean by breaking into my house? Who are you?

LIPTON: (Still feeling around on the floor) Oh, gorgeous rug. This is all handwoven. Must have cost a fortune. What is it, Persian?

JOE: Never mind the rug, I asked you a question. Who are you?

LIPTON: (Still on his knees) The name is Lipton. Sidney Lipton... Where am I, still on the floor?

JOE: (Takes the glasses out of his pocket) Here. Here's your glasses.

LIPTON: You found them? (Puts out his hand) Oh, good. Could you put them in my hand, please? (Joe puts the glasses into Lipton’s hand)

LIPTON: (Puts the glasses on, still on their knees) Ohh. Ohh, yes, there we are ... (looks up) Ohhh! This -- this is gorgeous! This is what I call a gorgeous room.

JOE: Is that why you broke in here?

LIPTON: Certainly not. I'm here on business. Very important business.

JOE: If you have business with me, you make an appointment like everyone else.

LIPTON: (Looking around) I'm not like everyone else. (Points to an ornate armchair) I love the chair. I don't fall in love easily, but I am in love with this chair.

JOE: Is that what you are? An antique dealer?

LIPTON: Antiques? No. Antiquity, perhaps.

JOE: What does that mean?

LIPTON: What does anything mean? What is the meaning of "meant"? What is real or unreal? What the hell are we talking about? I'm still dizzy from that fall I took.

JOE: I can't make you out. You're not a burglar, that I can tell.

LIPTON: A burglar? No. An antique dealer? No. But who am I? What am I? Why am I here? That's the mystery, isn't it? God, I love a good mystery.

JOE: If you don't tell me who you are . . .

LIPTON: Ah, ah, you're losing patience, aren't you? Mustn't lose patience, Joe. All in good time. I have cramps in the head. Did you ever get cramps in the head?

JOE: A lunatic! A lunatic wandered into my house from the snow. Why do I bother talking to you?

LIPTON: Curiosity! There is something curious about me, you've got to admit ... All right, enough chitchat. Let's get down to brass tacks, Joe Benjamin. Why, at this hour, on this night, in this year, in this house, on this rug, in these shoes, do I, Sidney Lipton stand before you? WHAT BUSINESS DO WE, STRANGERS TILL NOT FIVE MINUTES AGO, HAVE UNTO EACH OTHER?

JOE: Are you selling something? If you're a salesman, I'll kill you with my bare hands!

LIPTON: Do I look like a salesman? I am a man of flair, of fancy, a bizarre and unique guide to the world beyond our world.

JOE: A travel agent? Is that what you are, a travel agent?

LIPTON: (Yells, angrily) You have no imagination! What do I have to do to tell you who I am? Think, Joe, think!

JOE: I think you're a nut, that's what I think, and I want you out! (He grabs Lipton by the arm) Out, do you hear me? OUT!

LIPTON: Easy, easy. No rough stuff, I'm not a physical person.

JOE: Ten seconds and I throw you out that window head-first. One, two--

LIPTON: Don't force my hand. I deal a heavy hand

JOE: Three, four-

LIPTON: (Stops; points a finger) STAY! I STAY YOU! Yea, you would banish He who brings thee the gift of life and the eternal bliss? ... Forget that! Forget I said that. That was a slip. A boo-boo. Slipsies!

JOE: There's something funny going on here. You're not who you pretend to be at all, are you?

LIPTON: Aha! Aha, getting somewhere. Getting warm ...

JOE: This is all an act. A game. . . Somebody sent you, didn't they?

LIPTON: Hot! Getting hot!

JOE: Somebody sent you to get something from me!

LIPTON: Hotter! Hotter! Boiling hotter!

JOE: Somebody important who knows me sent you to get something that I have that has enormous value. Something I have that no other man on earth has.

LIPTON: Scalding! Steaming lava! Two weeks in a sauna bath!

JOE: My Bible! My Gutenberg Bible!

LIPTON: Cold. Freezing cold. Winter. A room for two in Toronto.

JOE: Damn you, what is it?

LIPTON: Hey! Hey hey hey! Calm, please. Take it easy. Let's not break our blood vessels. The last thing I want is for you to get sick. I mean, you are in good health, aren't you?

JOE: (Knocks wood) Thank God!

LIPTON: Hot! Boiling hot! Getting hot again!

JOE: (Screams) What are you saying? You're driving me crazy with these stupid games.

LIPTON: Temper, temper. And I was told you were such a patient, wonderful man.

JOE: Who told you? Who told you I was a wonderful man?

LIPTON: (Softly; side of their mouth) You know. . . He did.

JOE: Who's he?

LIPTON: He! Him! Capital "H," small "i" small "m" ... Do I have to spell it out for you? Went on and on about you. I'll tell you the truth, you're His favorite. Yes, you, Joe Benjamin, are considered to be His -- that's capital "H" again -- His absolute favorite. And that is the honest to God's truth. (makes a cross on his chest, then a circle, a square, all sorts of signs)

JOE: I can't understand what you're saying.

LIPTON: Can't understand or afraid to understand?

JOE: I'm not afraid of anything on the face of this earth except God himself.

LIPTON: BINGO! BULL'S-EYE! Ding-a-ling-a-ling-aling! Fire, fire, fire! Home run, home run! (jumps around in an excited jig)

JOE: STOP IT! I beg of you to stop it and tell me who you are, in plain, simple language. Who are you, please?

LIPTON: (stands erect, clasps his fingers together; solemnly) Very well. Forgive me, my son. I have taken this bizarre form, so that I might present myself to you in some acceptable dimension, for had I told you the truth straight on of my identity, even I could not have given you the power to accept or comprehend. Yes, Joe -- I am -- who you think I am!

JOE: Are you trying to tell me that you're -- that you're -- are you trying to tell me --

LIPTON: Say it, Joe. You will only believe if you say the words yourself.

JOE: God? Are you trying to tell me that you're God?

LIPTON: Who? . . . God? GOD? Is that what you thought? Nothing personal, but that's really crazy. Do I look like God? Would God wear glasses? I mean, if anyone's going to have good eyes, it's going to be God. No, Joe, I'm sorry to disappoint you, but I am not God.

JOE: Then who are you?

LIPTON: I'm a friend of God's. Not a close friend. We met a few times.

JOE: You met God?

LIPTON: Twice on business, once on a boat ride.

JOE: What business? What business do you have with God?

LIPTON: I deliver messages!

JOE: You're a messenger from God?

LIPTON: Important documents only; no packages.

JOE: All right, if you're who you say you are

LIPTON: I am.

JOE: Let me finish!

LIPTON: When you finish, I am!

JOE: If you're a messenger of God -- then where do you come from?

LIPTON: Oh, you mean like heaven? The Eternal Paradise? A place like that?

JOE: Yes.

LIPTON: Jackson Heights. It's in Queens, just over the Triborough Bridge.

JOE: But you said you met God.

LIPTON: Not face-to-face. There's always a big light over Him -- the glare is murder.

JOE: GOD! GOD! HAVE YOU SEEN GOD?

LIPTON: I didn't actually see Him. I heard Him. He blessed me.

JOE: God blessed you?

LIPTON: I sneezed and God blessed me -- what do you want from me? (Loudly) I cannot deliver God's message until you accept that I am God's messenger! What do I need to prove it to you, wings?

JOE: Tell me why? Then maybe I'll believe you. Why would God send a message to me, Joe Benjamin, a plain, simple, ordinary man?

LIPTON: To test your faith, that’s why! ... Strike that! You didn't hear it! Erase! I'm not supposed to tell you that.

JOE: Test my faith? My faith? Are you saying that God doesn't believe my faith in Him?

LIPTON: Oh, no. Not-Him. He believes! God's crazy about you ... It's the other one. (Softly, slyly) You know the other one. From downstairs ... Mr. Nasty … Bad, Bad Leroy Brown ... Oh, for God's sakes, you have to spell out everything for you ... Satan! Lucifer! The Devil, all right?

JOE: (Moving toward the phone) I've wasted enough time with you, I'm calling the police!

LIPTON: (Points a finger again) Stay! I stay you! I render you powerless! All right, I can't do it. I'll tell you everything . . . God and Satan were sitting around having one of those boring philosophical debates -- this was a week ago Tuesday. And Satan was sitting there in this pink suit -- gorgeous tan, little mole on his cheek ... And Satan says there is not one man on the face of the earth, who would not renounce God once the Devil put enough heat on. To which God said -- this is a quote, “one man would never renounce. And that man is ... (Makes a bugle sound) Tatum ta tum ta tum ta tum ta taaa ... JOE BENJAMIN!” Thrills, right? ... So they make a bet and the bet is, the Devil will make your life so miserable, you'll renounce God!

JOE: You think I would renounce God? You think so little of man that he would re-nounce God in the face of adversity?

LIPTON: I've seen people with a burning engine on a 747 who would sell out God in a second for a little good news from the pilot (Takes out a folded, dirty scrap of paper) You ready?

JOE: Let me see that.

LIPTON: (Pulls it away) I have to read it. It's not official unless I read it ... "To Joseph Melvin Benjamin, devoted husband and father ... if pain, calamity and disaster do not in any manner whatsoever appeal to you, then renounce your God!" That's it! Message delivered. No tip necessary, Good night, good luck, God bless you ... but I doubt it! (puts the message back in their pocket)

JOE: I will never renounce God, do you hear me? I fear Him and love Him but come hell or high water, I will never renounce Him!

LIPTON: Can I be honest? You can count on the hell and high water. Good luck, Joe. And no matter what terrible things happen to you, remember that God loves you! (a fire engine clanging in the distance)

JOE: What's that? What's going on out there?

LIPTON: (Looks out the window) Looks like a fire. Near the water ... Where's your factory?

JOE: Near the water.

LIPTON: Ohh ... Look at that burn. Like a cardboard box ... What do you make?

JOE: Cardboard boxes.

LIPTON: Ohh ... Well, I wouldn't worry unless I got a phone call. (Phone rings. They both look at it)

JOE: It's not my plant. My plant is a hundred percent fireproof. (picks up the phone) Hello? Eddie? ... What is it? ... What? ... What?

LIPTON: One more "what" and you're in trouble.

JOE: (Into the phone) WHAT?

LIPTON: What is it, a disaster or a calamity?

JOE: (Into the phone) The whole plant?

LIPTON: Oh, a catastrophe, wonderful!

JOE: Thank you, Eddie ... I know it wasn't your fault. (He hangs up)

LIPTON: How much did the insurance cover?

JOE: (Dazed) I didn't have insurance. I didn't believe in insurance ... GOD was my insurance.
```

---

## IC-0508: Greater Tuna

- Title: Greater Tuna
- Author (byline): Jaston Williams, Joe Sears and Ed Howard
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: Dec 1983
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 1, ACTOR 2, THURSTON, ARLES, THURSTON 2, ARLES 2, DIDI, CHAD, BERTHA, LEONARD, ELMER, VERA, COACH, ARLES & THURSTON
- Teaser before the introduction: Yes
- Spoken words (computed): 1540
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jaston Williams, Joe Sears and Ed Howard
ISBN: 978-0573619021
Publisher: Samuel French, Inc.
Date (Month/Year): Dec 1983
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Welcome to Tuna, the third-smallest town in Texas, “where the Lions Club is too liberal, and Patsy Cline never died.”

ACTOR 2: The play originated nearly 40 years ago as a Texas party skit based on a political cartoon; but frighteningly enough, it still rings true today!

ACTOR 1: So with no further ado . . . Here are our radio hosts, Arles Struvie and Thurston Wheelis!

TOGETHER: Greater Tuna by Jaston Williams, Joe Sears and Ed Howard
```

### Performance text (classify this)

```text
NOTE: This play was designed for 2 actors to play all the characters. This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles:

ACTOR 1: Thurston, Arles 2, Bertha, Vera, Leonard

ACTOR 2: Arles, Thurston 2, Didi, Chad, Elmer, Coach

THURSTON: (Pg 9-10) (Opening music) Good morning, Tuna, this is Thurston Wheelis.

ARLES: And this is Arles Struvie,

THURSTON: And this is the Wheelis

ARLES: Struvie-

THURSTON: Report.

ARLES: And here we go with the news. Take it away, Thurston.

THURSTON: Well, folks, in the news today, we've got the winner of the Tuna Junior High American Heritage Essay Contest for this year. And this year's winner is Connie Carp. She's the daughter of W.H. and Vera Carp here in Tuna, and the name of her essay was titled "Human Rights, Why Bother?"

THURSTON 2: Second place went to Jimbo Beaumont for "Living with Radiation", and third place went to Levita Posey for her essay titled, "The Other Side of Bigotry."

THURSTON: I'll tell you, Aries, with subjects like that, I don't know how they ever picked a winner.

ARLES: I don't either. I tell you, it should make the citizens of Tuna proud to know that we're still producing well-educated students who know what America is all about.

ARLES: (Pg 10-12) Now, on the Art scene, the on-again, off-again auditions for the Tuna Little Theatre production of "My Fair Lady" are on again. Now, they'd been called off due to a lack of budget. But Joe Bob Lipsey, who is the director of the show this year, said that he found a way to go ahead with the production by using sets and costumes from last year's show of "South Pacific."

ARLES 2: According to Joe Bob, this is gonna be the first production ever of "My Fair Lady" set in Polynesia. So get on your Hawaiian shirts, and your grass skirts, and your coconuts, and get out there to that Coweta Baptist Church at eight-thirty, Thursday night, and audition for "My Fair Lady."

ARLES: Joe Bob says he wants to integrate the cast this year. So if you know of any Negro or Mexican-American actors or actresses, have 'em come on out and try out for the chorus.

THURSTON: Well, folks, it's time for a word from our sponsor, Didi Snavely of Didi's Used Weapons. And here's Didi now to tell us all about it. Didi. (Musical transition)

DIDI: Does the high cost of security have you blue? If so, come by the store and browse through our complete selection of used guns and knives, or find what you need in our mace and tear gas department. Now we understand that many people are hesitant to buy used weapons, but all of Didi's weapons are absolutely guaranteed to kill. Now if you find a weapon here that won't kill, you bring it back and we'll give you something that will. It's on our guarantee: "If Didi's can't kill it, it's immortal." *****

ARLES: (Pg 13) And from our World News Desk: Peace talks fail, attack is imminent. Well, that’s all the news we got for ya, but stay tuned . . .

CHAD: (Pg 20-22) My name is Chad Hartford [Reporter for Intellect Magazine. Let’s get right to our interview] Now, Mrs. Bumiller, you are chairing the Censorship of the Textbooks Committee, am I correct?

BERTHA: Oh, no no no no. The Reverend Spikes heads that committee . . . although I am a member, I head the subcommittee that wants to snatch the books off the shelves of the high school library. Some of those books are absolutely disgusting. Our children have no business reading them, and somebody has got to protect the minds of the children.

CHAD: Now, exactly what are the books that you think should be removed from the shelves?

BERTHA: Well, now there's four of 'em that we're gonna try and have removed nationwide. And then we're gonna go from there. Roots. Now, we don't deny that Roots has been a very popular TV series, but we feel it only shows one side of the slavery issue. Bury My Heart at Wounded Knee. Well, it's the most disgusting title to begin with; it just makes me want to erp. It vilifies a great American, General Custer. And it encourages the reader to believe that the United States Government can't be trusted in makin' any treaties. Huckleberry Finn, by Mark Twain. Now, that book shows a pre-teenage boy avoidin' his chores, runnin' away from home, cohortin' with a Negro convict, and puttin' on women's clothes. [And] Romeo and Juliet. It shows sex among teenagers, and we're certainly not going to encourage it. Besides, it shows a rampant disrespect for parental authority.

CHAD: You are aware that William Shakespeare wrote that play?

BERTHA: Oh, yes, we are. And we're lookin' into the rest of his stuff too. He wrote Barefoot in the Park, didn't he?

CHAD: Thank you Mrs. Bumiller. I think we got one hell of a story here. ******

ARLES: (Pg 27-28) And now folks, sit back and listen to the number one show in Dewey County. On the Line with Leonard. Where your business is everybody’s business. Here’s station manager Leonard Childers. (Musical transition)

LEONARD: Hello everybody. This is Leonard Childers with “This Week in Tuna.” I got a message here from the Reverend Spikes over at the Coweta Baptist Church; he says he's gonna sponsor another record-burning. Bring all your rock-and-roll, and this time be sure and get your Chuck Berry and your Brenda Lee and your Little Richard. He says, leave that Buddy Holly and Elvis at home; they're good Southern boys and they'll be forgiven. Anyway, that'll be this comin' Sunday night at eight o'clock down at the Coweta Baptist Church. So bring your rock-and-roll, come on out and burn it . . . ******

THURSTON: (Pg 41) (Musical intro) Good afternoon, Tuna. This is Thurston Wheelis, and this is the Wheelis-Struvie Midday Report. First off in the news, there's gonna be a meeting of the Smut Snatchers of the New Order this afternoon at the Coweta Baptist Church, startin' about five o'clock. Now, Radio Station OKKK is gonna carry that meetin' live. So you tune in.

THURSTON 2: Now, the Smut Snatchers' latest project is cleaning up those dictionaries down at Tuna High School. And they say, if you know of a word that you feel has questionable value, or a word that you feel just should not be in the dictionary- now if you don't want your child around the word, bring that word with you to the meeting.

THURSTON: Bring it to the meeting. The Reverend Spikes says he'll consider each word on a word-by-word basis.

ARLES: (Pg 44) And from our National News Desk: Nuclear accident imperils millions in seven states-Texas not included. Well, that’s all the news we got for ya, but don’t touch that dial-

THURSTON: Don’t touch that dial . . . Get away from it!

ARLES: Get away from it! ‘Cause Tuna Speaks is next! (Musical transition)

ELMER: (Pg 45) This is Elmer Watkins on Tuna Speaks. As a citizen of Tuna, I feel it’s my obligation to speak up about this Agent Orange Stuff and its effects on servicemen. I just wanna say that in the last year I’ve hired fourteen veterans, Viet Nam veterans, to work for me on my road crew, and out of those fourteen, only four of ‘em have died, but there wasn’t a one of ‘em turned orange. I swear to God, not one of ‘em turned anyways near orange. I think it’s just more of this propaganda by this liberal press and these hippie-oriented groups!

VERA: (Pg 46) Vera Carp, Vice-President of the Smut Snatchers of the new Order . . . We need to send out our book-snatchin' squad to the Tuna High School Library to check those dictionaries. Now, we have a new list of words that have been declared possibly offensive or misunderstandable to pre-college students. Now the words are: hot, hooker, coke, clap, deflower, ball, knocker and nuts. After much prayer and soul-searching with the Lord, the Committee has decided not to include the word “snatch” on this year's list. We know some of you have very strong feelings about “snatch,” but we just can't afford to change our letterhead at this time.

LEONARD: (Pg 53) This is Leonard Childers with the Tuna Bulletin Board. Now, if you have any younguns between the ages of eight and fourteen, you need to know that Thursday is your last day to register your kids for Colonel Sprayberry's Character Camp and Survival Institute. Now this year, they're offering classes in Old Testament appreciation, segregation in the Scriptures, Christian biology, character development, and the proper use of firearms. So register your kids today; it will do them some good.

THURSTON: (Pg 49-50) (Musical transition) This is Thurston Wheelis with a sports flash. This just in. The Tuna High School Jaguars lost their season opener against the Kuhlburg Comanches. It was a hard-fought contest, but in the end, the Cats were on the short end of a 48 to nothin’ score. Coach Raymond Chassie evaluated the loss this way.

COACH: Well, we lost mainly because we couldn’t score. But the fact that they made seven touchdowns was a major factor in the loss also. I don’t know which was a bigger factor, but you take away them two things, and it would have been a tie. So, I’m real proud of our boys anyway.

ARLES: (Pg 58) I give up, Coach, take me out. So we're gonna say good night to ya . . . (Musical transition)

THURSTON: Good night!

ARLES: . . . And we'll see you tomorrow.

THURSTON: See you tomorrow.

ARLES: 'Til then, remember our motto here at Radio OKKK: If you can find someplace you like better than Tuna . . .

ARLES & THURSTON: MOVE!
```

---

## IC-0509: Heroes in a Half Shell

- Title: Heroes in a Half Shell
- Author (byline): T. J. Kenda
- Work: Heroes in a Half Shell
- Publisher: SpeechGeek
- Publication date as stated: 2013
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1197
- Already set (do not supply): none

### Source block (context only)

```text
Heroes in a Half Shell by T. J. Kenda
ISBN: 978-1-61387-042-6
Copyright 2013 by SpeechGeek.
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
SCENE ONE

(The television turns on with a news report in progress.)

APRIL. …much more than just a series of small, isolated incidents. It's

apparent an organized criminal element is at work. Citizens

of New York are waiting for someone to save them. This has

been April O'Neil reporting for Channel Three Eyewitness

News.

(Television turns off.)

LEONARDO. Master Splinter, we’ve been ignoring these attacks

long enough. The time has surely come for us to go to the

surface and fight. SPLINTER. Fifteen years ago I was a pet of my master Yoshi. I was

mimicking his movements from my cage and learning the

secret art of ninja. When we were forced to come to New

York, I found myself wandering the sewers. That’s when I

came upon a shattered glass jar and four baby turtles.
MIKEY. That was, like, totally us. Cowabunga!
RAPHAEL. Shut up, Mikey.
SPLINTER. The little ones were crawling in a strange, glowing ooze.
DONATELLO. Actually, it was molecular irradiated mutonium.
RAPHAEL. Shut up, Donatello.
SPLINTER. Then, one of them spoke.
BABY. Pizza! Pizza!
SPLINTER. Soon, I began their training and teaching them all that I

had learned from my master. I gave them all names.
LEONARDO. (brandishes his swords) Leonardo!
MIKEY. (brandishes his nunchucks) Cowabunga!
LEONARDO. Michelangelo!
MIKEY. Right!
DONATELLO. (brandishes his bow) I’m Donatello!
RAPHAEL. (brandishes his tsai) Shut up!
SPLINTER. And you became the Teenage Mutant Ninja Turtles, heroes

in a half shell. LEONARDO. Ok, but seriously, Splinter, can we get the shell out of the

sewers yet?

SCENE TWO
SPLINTER. My dear sons, the time is not yet right to surface.
LEONARDO. Don’t you think we’re ready?
SPLINTER. No, my sons. Your ninja skills have not yet reached their

peak. Just as I did, fifteen years ago, living in Japan as a

pet to my master Yoshi. I was mimicking his movements

from my cage and learning…(walks away still telling the

story)
LEONARDO. Master? Why does he always do that?
DONATELLO. I guess he’s meditating.
MIKEY. I say we, like, go up and, like, surf this crime wave.
RAPHAEL. Shut up.
DONATELLO. Raphael is right. We can’t do that.
LEONARDO. Yes, we can.
DONATELLO. No, we can’t.
MIKEY. Okay, while you two, like, argue, I’m going to do some

meditating of my own.

SCENE THREE

(The television turns on with a news report in progress.)

APRIL. ...mysterious gang of ninjas known as The Foot. I know, it

sounds like a funky club for podiatrists. But our recent

crime wave is reminiscent of a secret band of ninja thieves

who once operated in Japan. If only we knew who their

leader was. This is April O’Neil reporting for Channel

Three Eyewitness News.

(The television turns off.)

NINJA. Master Shredder? What should we do about the lady

reporter? She must not reveal our existence to the world.

Surely the Foot must stop her. Or stomp her. SHREDDER. Indeed. Find her. Silence her. NINJA. Yes, master. (draws sword and disappears)

SCENE FOUR
APRIL. (enters, humming to herself) Hmm, hmm, hmm.
NINJA. We've been waiting for you.
APRIL. For me? April O’Neil, Channel Three Eyewitness News?
NINJA. I deliver a message.
APRIL. (opens a fortune cookie and reads the fortune) Your mouth

may yet bring you much trouble, Miss O'Neil. Your lucky

numbers are 5, 4, 3, 2… NINJA. 1! Attack! (NINJA draws his sword to attack. The turtles

intervene.)
LEONARDO. Not so fast, Foot.
DONATELLO. Are you all right, Miss O’Neil?
APRIL. I think so. Who are you?
DONATELLO. I am (hesitates) a shadow! Ninja vanish. (The smoke bomb

goes off but DONATELLO doesn’t disappear.)

APRIL. Was that supposed to make you disappear? MIKEY. Whoa. APRIL. It’s kind of hard to disappear as a six foot turtle in a trench

coat. RAPHAEL. Shut up. (RAPHAEL knocks her out.) Ninja vanish.

SCENE FIVE SHREDDER. Is O’Neil dead? NINJA. Master, we failed. There were creatures. They were

mutant teenagers.
SHREDDER. Aren’t they all?
NINJA. No, they were ninjas.
SHREDDER. So are you.
NINJA. They were turtles!
SHREDDER. Heroes in a half shell?
NINJA. Yes. We were defeated. We were (beat) de-footed.
SHREDDER. Hmm, so there is a new enemy: freaks of nature who

interfere with our business. Find out more. You are my

eyes and ears… NINJA. …and Foot. SHREDDER Find them. Together, we will punish these creatures!

These...turtles!

SCENE SIX LEONARDO. Master! SPLINTER. Many years ago, when I lived in Japan, I was a pet of my

master Yoshi. I was mimicking his movements from my

cage...
LEONARDO. Sensei, there is no time. We just met ninjas of the Foot.
SPLINTER. The Foot?
DONATELLO. Yes, master.
SPLINTER. I heard of the Foot fifteen years ago when I lived in Japan, I

was a pet of my master Yoshi…(trails off)
MIKEY. Like, what do we do?
LEONARDO. Let us meditate.
RAPHAEL. Shut up.
DONATELLO. That's the plan from our great leader?
LEONARDO. I never said I was a great leader.
RAPHAEL. Shut up.
LEONARDO. That attitude of yours isn't helping anything, Raph.
RAPHAEL. Maybe I'll just take my attitude and leave! (shoves his head

down into his shell) LEONARDO. Oh, very mature, Raph. (knocks on the shell) Raph? Raph.

Forget it.

(The television turns on.)

APRIL. This just in: I’ve been kidnapped by the Foot clan. April

O'Neil, Channel Three Eyewitness News. MIKEY. Like, didn’t we just save her? DONATELLO. They must have come back after we left her unconscious

in the street. LEONARDO. Criminal mastermind fiends! Master, how much longer

must we wait? SPLINTER. (looks at watch) The time has come. Let’s go.

SCENE SEVEN

(A huge fight scene commences with random exclamations from the turtles.)

APRIL. Yo, turtle, would you mind saving April O'Neil, Channel

Three Eyewitness News?
RAPHAEL. Shut up!
LEONARDO. Man, this was easy.
DONATELLO. (thinks about it) Yeah…too easy.
SHREDDER. (enters) You fight well in the old style, but you've caused

me enough trouble. Now you face The Shredder.

(SHREDDER takes a piece of paper and shreds it.) MIKEY. Does anybody, like, have any idea about who or what this

is? APRIL. I don't know, but I'll bet it never has to look for a can

opener. April O'Neil reporting for Channel Three

Eyewitness News.
DONATELLO. Raph, get him.
RAPHAEL. (RAPHAEL gets beaten up.) Shut up.
MIKEY. Hey Leo, why don't you go next?

(The turtles fight and get beaten.)

APRIL. It seems we’ll be eating turtle soup tonight. April O'Neil,

Channel Three Eyewitness News.
RAPHAEL. Shut up!
SPLINTER. It is ok, my sons. I got him. I know you well, Shredder.
SHREDDER. As I know you, Splinter. I will finish what I started fifteen

years ago when you lived in Japan as a pet of your master

Yoshi. MIKEY. What is it with these guys and that story? SPLINTER. Death comes for us all, Shredder, but something much

worse comes for you. For when you die, it will be without

honor. LEONARDO. Ooooh, snap!

(SPLINTER and SHREDDER fight. SPLINTER wins.)

LEONARDO. Master Splinter, are you ok? SPLINTER. Better than I have been in fifteen years, when I lived in

Japan as a pet of my master Yoshi.
LEONARDO. Miss O’Neil, you are safe now.
APRIL. Thank you. How can I ever repay you?
RAPHAEL. Shut up. (knocks her out)
SPLINTER. Ninja vanish.

SCENE EIGHT

(The television turns on to a news broadcast that is already in progress.)

NEWS. Amazing! Then what happened, Ms. O’Neil? APRIL. Then guys in the black pajamas jumped me. NEWS. Miss O’Neil, you still haven't told us how you got away

from your attackers. APRIL. Some citizens of New York actually came to my rescue.

Who says everyone in the Big Apple looks the other way?

This is April O’Neil reporting for Channel Three

Eyewitness News. NEWS. Um, this is my interview.

(The television turns off.)

LEONARDO. Listen, Raph, about what I said before, about not needing

you and all... RAPHAEL. Shut up. SPLINTER. I am proud of you, my sons. Tonight you have learned the

final and greatest truth of the ninja: that ultimate mastery

comes not of the body but of the mind. DONATELLO. …and of the Foot. MIKEY. Let’s celebrate! Pizza?
```

---

## IC-0510: H.I. Train Wreck

- Title: H.I. Train Wreck
- Author (byline): Marie Pawelec
- Work: H.I. Train Wreck
- Publisher: SpeechGeek
- Publication date as stated: 2013
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1110
- Already set (do not supply): none

### Source block (context only)

```text
H.I. Train Wreck
by Marie Pawelec
ISBN: 978-1-61387-041-9
Copyright 2013 by SpeechGeek.
Free performance of this play for high school and college level
competitive forensics is permitted. All other rights reserved.
This PDF version of this selection, e-published in 2013, is identical to the
printed published version of this same publication dated 2013. This
statement along with the entire printed PDF of this publication must be
presented at any National Forensic League District or National event for the
script to comply with NFL rules per the request of the Executive Director.
This and other selections of quality performance literature for competitive
oral interpretation are published by SpeechGeek.
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
SCENE ONE H.I. COMPETITOR. (doing vocal warm-ups) Don't look at me.

(continues warming up, then turns to start piece) I just want to start this thing off by saying I don't want to be here. I'm sure all of you can sympathize…(at judge) …especially you. I mean, you've probably got it worse than all of us. You are literally wasting your Saturday. You don’t even get the benefit of a nice little extracurricular activity to go on a college résumé, or get to relive the fun, nerdy delights of high school, or even enjoy a consolatory Wendy's frosty on the way home. Nope, you get to wake up just as early as everyone else and sit in a chair forever. Plus, you're playing the lottery on how miserable you'll be while you're here. Will you get the joy of judging extemp? Oratory? Ooooh, maybe declamation! Luckily for you, dear judge, you landed DP! Enjoy the jealous looks of everyone else in the tab room who drew the short straw; I’m sure it’s the only rewarding part of judging. And now, for your viewing pleasure, let’s do a rundown of what you're going to see tonight over and over, and over. But first, I need to do my introduction. As if we ever really need those.

SCENE TWO H.I. COMPETITOR. Ok, now that we got that scripted piece of garbage out of the way, we can get to the meaty chunk of regurgitated mess that you will have to suffer through for the next 8 or so minutes. You have 3 options. A: You can try to remain mildly interested in the remote hope that it will actually be funny. Two: Zone out and think how dumb acne-riddled high school teens look in formal business attire. Or C: Give up and take a nap. I don't mind. If you chose options “A” or “Two”, I'm going to make this easier on you and give you a break down on all the characters I'm about to preform so you don't have to write on my ballot

JUDGE. (writing) Not enough...differentiation....between characters.

H.I. COMPETITOR. That's you, by the way. You're my first character.

STORYTELLER. (laughs maniacally) Hey friends! You best prepare your knees for slapping and your guts for wrenching because my piece is hi-lar-i-ous! No really! I'm funny! My mommy told me! This is "The Three Little Pigs!” (laughs) By that one guy!! (laughs) It's funny!

H.I. COMPETITOR. I'm also an attention seeker.

DECLAMATION SPKR. Hello. I'm about to stand up here for ten whole minutes and recite a poorly cut piece by an author whose name you'll have to ask for twice because when I speak, the monotony of my voice will make your head implode. If you’re lucky I will go over-time. You will also be incredibly distracted by my pit stains.

D.I. COMPETITOR. Darkness. Depression. Edgar Allen Poe, the saddest man that ever lived once said, "Ouch, broken hearts suck.” Ever since then, white girls like me have taken inspiration from legitimate tragedies to completely over-act in disturbing D.I.s that will cause you to go home and to look at pictures of cute puppies and silently sob at your computer. "Acid Face" by Susanne Buttkans.

NERVOUS COMPETITOR. Uhmm. Ok. Sorry??? Uhmm. Ok. Can I start over?

H.I. COMPETITOR. I know there's usually 6 people in a round, but I've already wasted 3 of your minutes and ain't nobody got time for that.

JUDGE. (writing) Three minutes have elapsed, (writing slowly) still not funny.

SCENE THREE JUDGE. Whenever you're ready.

STORYTELLER. (in gruff voice) Once upon a time there was a big bad wolf! (howls) AWOOOOOOO! He was bad guy, so I'm going to talk like this.

JUDGE. I'm going to give you a three, because I feel bad for your parents.

STORYTELLER. There are also three sweet little pigs! Oink oink! There’s a little onomatopoeia because that's the sound that pigs make!

JUDGE. Nobody loves you.

STORYTELLER. I know you know this story, but wait—plot twist—something really CRAAAAAZZZYYY HAPPENS!

JUDGE. I'm sorry, did you want time signals?

SCENE FOUR D.I. COMPETITOR. (intense) I KNOW WHY YOU'RE HERE. IT'S BECAUSE IM A MONSTER! But I’m a person too. You’ll see.

JUDGE. Wow, your eyebrows really make this piece.

D.I. COMPETITOR. NOW LISTEN TO THE DRAMATIC FLASH BACK OF MY PROGRESSION INTO MADNESS!

JUDGE. I wonder if this is about dead babies, murder, rape, or cancer.

D.I. COMPETITOR. My name is Suzy Lee. I look innocent, right? No one would ever guess that I'm a murderer!

JUDGE. Whoop, there it is!

D.I. COMPETITOR. I was a nice girl until my father did horrible things to me. Then my mother was diagnosed with cancer, my dog died, I broke every bone in my body, I got mugged in an alley by a one-hit wonder boy band, and I got stuck in traffic on the way to a BeeGee's concert!

JUDGE. I didn't even know that was possible to cram all of that into one plot line.

D.I. COMPETITOR. My emotions took control. I COULDN'T TAKE IT ANYMORE! THAT'S WHY I DID IT! That’s why I killed Mufasa!

JUDGE. There is nothing I want more than to give you a swirly in the toilet but I'm going to have to give you a one, aren’t I?

D.I. COMPETITOR. And thus, I die!

JUDGE. Ok, thank you.

SCENE FIVE

(D.I. COMPETITOR 2 stands awkwardly.)

JUDGE. Uhm, yes?

D.I. COMPETITOR 2. May I be excused?

JUDGE. Are you double entered?

D.I. COMPETITOR 2. No, I just want to practice my crying face in the bathroom.

JUDGE. Yes, please leave.

SCENE SIX ORATORY COMPETITOR. (nervous and stumbling over lines ) Hi, um, oh, sorry. I mean, hello, today we will be discussing how cultures, um today, um have pushed, uh, the superficial idea of beauty on today's youth. Today, and uh, my three points I will discuss are uh, all personal anecdotes uh, being, because I have lots of experience uh with this.

AUDIENCE MEMBER 1. (fake cough) Wrong room (cough)

AUDIENCE MEMBER 2. She doesn't even go here!

SCENE SEVEN NERVOUS COMPETITOR. (stands for a moment looking terrified) Can I go throw up?

JUDGE. Yeah, go ahead.

SCENE EIGHT D.I. COMPETITOR 3. Why would a woman want to be a detective? I don't know. I don't know a lot of things. What makes criminals tick? How could you kill someone in cold blood? Why does your car break down right after the warranty ends?

JUDGE. Please stop before I kill myself D.I. COMPETITOR 3. (immediately stops performing) Ok.

JUDGE. (surprised) Really?

D.I. COMPETITOR 3. (matter of fact) Yeah JUDGE. Oh, cool. (referencing rank for the round) Two?

SCENE NINE

(Later, on the bus.)

H.I. COMPETITOR. Wow, these ballots are ridiculous! (reads comments) “Nice diction, perfect characterization, very funny, nice job with intro, no stumbles. Overall perfect.”

(smiles before reading the rank with shock) SIXTH?!
```

---

## IC-0511: History (and a Dash of Hollywood)

- Title: History (and a Dash of Hollywood)
- Author (byline): Seth Kramer
- Work: After the Beep: Seven Short Plays
- Publisher: Dramatic Publishing
- Publication date as stated: 1999
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: CHARACTERS, ACTOR 2, ACTOR 1, TOGETHER, CAESAR, HARRISON
- Teaser before the introduction: Yes
- Spoken words (computed): 995
- Already set (do not supply): none

### Source block (context only)

```text
Author: Seth Kramer
Book: After the Beep: Seven Short Plays
ISBN: 978-0871299031
Publisher: Dramatic Publishing
Date (Month/Year): 1999
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: You think Americans don't care about history?

ACTOR 2: Think again. – From Ben Hur to Shindler’s List – Awards were granted and the American public scrambled to see history unfold on the big screen.

ACTOR 1: Popular films increase interest in history and contain much accurate information,

ACTOR 2: But producers of these films often take liberties with facts to tell a more entertaining story.

ACTOR 1: In fact, movies based on actual history tend to be a mixed bag.

ACTOR 2: Transforming complicated events and people into entertaining films is never easy

ACTOR 1: But when is it justified to sacrifice historical facts for entertainment value?

ACTOR 2: You see . . . The road to Hell is paved with good intentions . . .

ACTOR 1: Especially when money is involved.
```

### Performance text (classify this)

```text
CHARACTERS: 2 men or 2 women

(Lights up. CAESAR walks around a large desk, HARRISON sits across from him. There are numerous pads of paper and pens.)

ACTOR 2: History

ACTOR 1: (and a Dash of Hollywood)

TOGETHER: by Seth Kramer

CAESAR: So it's a script idea?

HARRISON: Sure.

CAESAR: Some new project?

HARRISON: That's right.

CAESAR: Talk to me.

HARRISON: OK. Benjamin Franklin. He's an inventor. He's a brilliant mind. A founding father.

CAESAR: OK.

HARRISON: We follow his life. His accomplishments.

CAESAR: He's our good guy?

HARRISON: Good guy?

CAESAR: Yeah, our hero. He does something. He fights in the revolutionary war. He saves the colony somehow? Rides a horse through towns: "The British are coming, the British are coming!" Something, right?

HARRISON: Well . . .

CAESAR: Talk to me.

HARRISON: That's not exactly right.

CAESAR: No?

HARRISON: Paul Revere made that ride.

CAESAR: Oh, well, he . . . something, what? The battle of Bunker Hill, the Boston Tea Party? What?

HARRISON: Benjamin Franklin was an inventor.

CAESAR: An inventor?

HARRISON: Yes, an inventor . . . one of the times· most respected thinkers.

CAESAR: I see. And you want to . . . what? Make a movie about this? About him and his ... thinking?

HARRISON: He had a very high IQ.

CAESAR: What's the movie'? What's the story?

HARRISON: Well, I told you, Benjamin Franklin was an inventor. He was one of our founding fathers. It could be a very educational film. Put people in touch with their roots.

CAESAR: No.

HARRISON: No?

CAESAR: No. There is no such thing as an “Educational Film." Not in this day and age. Not with fifteen million dollar budgets on the small projects. Do you want to make money? Huh? You do remember money, don't you? You want to educate, get a job at PBS. Go work for Sesame Street. Become a teacher!

HARRISON: I . . .

CAESAR: If you want to educate.

HARRISON: Are you saying that film can't educate?

CAESAR: Look... LOOK. This is movies, all right? You and me, we make movies. If someone looks at one of my flicks in twenty or thirty years and says it's ART or that they found it educational then they can give me a fuckin' plaque. That's of course assuming I'm still alive. But right now-TODAY- I want to kick something out. I want something I can walk into a studio with, sit down across from some cock-sucking vulture, and SELL. S-E-L-L.

HARRISON: You don't think historical movies can sell?

CAESAR: Let's just say I'm skeptical.

HARRISON: What about westerns? What about war movies? Don't they sell?

CAESAR: (long pause) Tell me THE STORY.

HARRISON: The story?

CAESAR: Let's work with it. Let's see what we can piece together.

HARRISON: I don't see how you can piece together histo-

CAESAR: Trust me.

HARRISON: (pause) OK.

CAESAR: Shoot.

HARRISON: Benjamin Franklin, he's one of the times' most prominent . . .

CAESAR: Inventor, founding father, thinker, Jesus, are you repetitive. Got it, we've done this before. Start the story. Start with . . . What?

HARRISON: Oh, I see . . . OK, Franklin is . . .

CAESAR: BEN. Call him Ben.

HARRISON: OK, Ben. Ben is a young man, he grows up in a prominent colonial family. He spends a great deal of his time reading and studying.

CAESAR: He's a loner.

HARRISON: I suppose.

CAESAR: He's angry all the time. He broods. A handsome, misunderstood loner.

HARRISON: Actually . . .

CAESAR: A young Brando-type.

HARRISON: No, actually . . .

CAESAR: James Dean?

HARRISON: Actually, he had a weight problem his whole life. He also had a mild form of asthma.

CAESAR: Oh, well that's gripping. We may have to take a few liberties. Change a bit here, change a bit there. BEN is our hero. We have to make him seem like a HERO, kapeesh?

HARRISON: I just think historical accuracy . . .

CAESAR: You want historical accuracy, write a book! We have two hours to tell a story, reality needs to be condensed. Let's move on.

HARRISON: Um . . .

CAESAR: Ben is young. He has a problem with authority. Where do we go from here?

HARRISON: Well, he's an inventor.

CAESAR: And?

HARRISON: And he . . .

CAESAR: What?

HARRISON: He invents the first . . .

CAESAR: Remember THINK FILM.

HARRISON: The first (pause.) Time machine?

CAESAR: Time machine?

HARRISON: Time machine. Hey, you said think film.

CAESAR: No. No. That's good. I like that. Time machine. Boy, once you get moving you don't screw around.

HARRISON: Anyway, he invents it.

CAESAR: Wait.

HARRISON: What?

CAESAR: God just spoke to me! He FINDS it!

HARRISON: FINDS it? He's an inventor! What's the point of having him be an inventor unless he can . . .

CAESAR: No. Wait. Wait. It finds him. The time machine comes to him. That's the story. That's what we need. A hook. Let's say, in the future, this guy, this scientist . . .

HARRISON: Scientist?

CAESAR: Indiana Jones type.

HARRISON: OK.

CAESAR: This Indiana Jones type, he discovers a plot that your basic, everyday, evil genius has hatched . . .

HARRISON: Wait?

CAESAR: What?

HARRISON: Saddam Hussein. Let's make the evil genius a Saddam Hussein type.

CAESAR: Now you're thinking! Saddam is very vogue as far as villains go this year. OK, what's the plot?

HARRISON: Well, OK. Let's say . . . Saddam is going to back in time to ... TO ASSASSINATE Franklin.

CAESAR: Ben.

HARRISON: Right, Ben. Saddam wants to stop America from ever happening by killing off BEN. Now our hero, our Indiana Jones type, has to go back in time and prevent this.

CAESAR: It's a buddy-buddy film.

HARRISON: Those sell, right?

CAESAR: Like blue jeans in Russia. Ben and Indiana fight off a horde of Middle- Eastern-type assassins dressed up like redcoats.

HARRISON: Along the way maybe this Indiana guy can fall in love?

CAESAR: Sure, it's a romance across time.

HARRISON: Very Romeo and Juliet.

CAESAR: Only nobody dies. I love it, LOVE IT! Go on.

HARRISON: Our Indiana Jones hero has to deal with other stuff too. No plumbing, no TV, no microwaves. Stuff like that.

CAESAR: A comment on modem society. Very interesting. What else?

HARRISON: He brings his Walkman with him.

CAESAR: What?

HARRISON: It gets stolen.

CAESAR: Where you goin' with this?

HARRISON: (lost in his own world) Some little kid takes it. Some kid that in the future is going to be very important. A young Thomas Jefferson! So now our hero, Indiana, has to retrieve it without affecting the kid's life too much, or he could seriously screw up the Space-time continuum.

CAESAR: Space-time con-what-uum?

HARRISON: It's a Star Trek term. People that are into time travel will eat that up.

CAESAR: Well, that's all right then.

HARRISON: So what do you think?

CAESAR: Honestly? It's *crap*-BUT-conservatively here, I'm thinking, a million bucks.

HARRISON: A cool million.

CAESAR: Hey. It's a movie, man.

HARRISON: History.

CAESAR: Ya got to love it, you know what I mean?
```

---

## IC-0512: Hooray for Diffendoofer Day!

- Title: Hooray for Diffendoofer Day!
- Author (byline): Theo Geisel (aka Dr. Seuss) and Jack Prelutsky
- Work: Not specified
- Publisher: Knopf Books for Young Readers
- Publication date as stated: April 1998
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 1, ACTOR 2, TOGETHER
- Teaser before the introduction: No
- Spoken words (computed): 1078
- Already set (do not supply): none

### Source block (context only)

```text
Author: Theo Geisel (aka Dr. Seuss) and Jack Prelutsky
ISBN: 978-0679890089
Publisher: Knopf Books for Young Readers
Date (Month/Year): April 1998
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Envision for a moment if you will the perfect learning environment.

ACTOR 2: Does it involve high-stakes testing for students and teachers?

ACTOR 1: Does it guarantee that all schools will be “failing” schools by 2014?

ACTOR 2: Or is it something different . . . something better . . . . something inspiring?

ACTOR 1: This is a story about creative teaching and thinking. It is a tale that celebrates originality, difference, and uniqueness a

ACTOR: 1: A school in which truly No Child is Left Behind.

TOGETHER: Hooray for Diffendoofer Day! By Theo Geisel (aka Dr. Seuss) and Jack Prelutsky
```

### Performance text (classify this)

```text
ACTOR 1: I've always lived in Dinkerville,
My friends all live there too.
We go to Diffendoofer School-
We're happy that we do.

ACTOR 2: Our school is at the corner of Dinkzoober and Dinkzott. It looks like any other school, but we suspect it's not.

ACTOR 1: I think we're learning lots of things not taught at other schools. Our teachers are remarkable, they make up their own rules.

ACTOR 2: Miss Bobble teaches listening,

ACTOR 1: Miss Wobble teaches smelling,

ACTOR 2: Miss Fribble teaches laughing,

ACTOR 1: And Miss Quibble teaches yelling.

ACTOR 2: Miss Twining teaches tying knots in neckerchiefs and noodles, And how to tell chrysanthemums from miniature poodles.

ACTOR 1: Miss Vining teaches all the ways a pigeon may be peppered, And how to put a saddle on a lizard or a leopard.

ACTOR 2: My teacher is Miss Bonkers,
She's as bouncy as a flea.
I'm not certain what she teaches,
But I'm glad she teaches me.

ACTOR 1: "Look! Look!"

ACTOR 2: she chirps.

ACTOR 1: "I'll show you how to tell a cactus from a cow, And then I shall instruct you why a hippo cannot hope to fly."

ACTOR 2: She even teaches frogs to dance, And pigs to put on underpants.

ACTOR 1: One day she taught a duck to sing- Miss Bonkers teaches EVERYTHING!

ACTOR 1: Of all the teachers in our school, I like Miss Bonkers best.

ACTOR 2: Our teachers are all different, But she's different-er than the rest.

ACTOR 1: We also have a principal, his name is Mr. Lowe.

He is the very saddest man that any of us know. He mumbles,

ACTOR 1: "Are they learning this and that and such and such?”

ACTOR 1: His face is wrinkled as a prune from worrying so much.

ACTOR 2: He breaks a lot of pencil points from pushing down too hard,
and many dogs start barking as he mopes around the yard.
We think he wears false eyebrows. In fact, we're sure it's so.
We've heard he takes them off at night...I guess we'll never know.

ACTOR 1: But we know he like Miss Bonkers, he treats her like a queen. He's always there to watch her when she's on her trampoline.

ACTOR 2: There are many other people who make Diffendoofer run. They are utterly amazing-I love every single one.

ACTOR 1: Our nurse, Miss Clotte, knows what to do when we'ver got sniffles or the flu. One day I had a splinter, so she bandaged me from head to toe.

ACTOR 2: Mr. Plunger, our custodian, has fashioned a machine-a super-zooper-flooper-do-it keeps the whole school clean.

ACTOR 1: Our music teacher, Mrs.Fox, makes bagpipes out of straws and socks.

ACTOR 2: Our art instructor, Mr. Beeze, paints pictures hanging by his knees.

ACTOR 1: In science class with Mr. Katz, we learn to build robotic rats. In gym we watch as Mr. Bear hoists elephants into the air.

ACTOR 1: Miss Loon is our librarian, she hides behind the shelves, and often cries out,

ACTOR 1: "LOUDER!"

ACTOR 1: when we're reading to ourselves.

ACTOR 2: We have three cooks, all named McMunch who merrily prepare our lunch. They make us hot dogs, beans and fries, plus things we do not recognized. And as they cook, they sing their song, not too short and not too long.

ACTOR 1: "Roast and toast and slice and dice, cooking lunch is oh so nice."

ACTOR 2: We were eating their concoctions, telling jokes and making noise, when Mr. Lowe appeared and howled,

ACTOR 1: "Attention, girls and boys!"

ACTOR 2: He began to fuss and fidget, scratch and mutter, sneeze and cough. He shook his head so hard, we thought his eyebrows would come off. He wrung his hangs, he cleared his throat, he shed a single tear: then sobbed,

ACTOR 1: "I've something to announce, and that is why I'm here."

ACTOR 1: "All schools for miles and miles around must take a special test,
To see who's learning such and such-to see which school's the best.
If our small school does not do well, then it will be torn down,
And you will have to go to school in dreary Flobbertown."

ACTOR 1: "Not Flobbertown!" we shouted, and we shuddered at the name, for everyone in Flobbertown does everything the same.

ACTOR 2: They’re miserable in Flobbertown, they dress in just one style. They sing one song, they never dance, they march in single file.

ACTOR 1: They do not have a playground. And they do not have a park. Their lunches have no taste at all, their dogs are scared to bark.

ACTOR 2: We sat in shock and disbelief.

ACTOR 1: "Oh no!"

ACTOR 2: we moaned.

ACTOR 1: "Oh no!"

ACTOR 2: We were even more unhappy than unhappy Mr. Lowe.

ACTOR 1: But then the test was handed out.

ACTOR 2: "Yahoo!"

ACTOR 1: we yelled.

ACTOR 2: "Yahoo!"

ACTOR 1: For it was filled with all the things that we all knew we knew.

ACTOR 2: There were questions about noodles, and poodles and frogs and yelling, about listening and laughing, and chrysanthemums and smelling.

ACTOR 1: There were questions about other things we'd never seen or heard, and yet we somehow answered them, enjoying every word.

ACTOR 2: One week later, after recess, Mr. Lower meandered in. We'd never seen him smile before, but now he wore a grin.

ACTOR 1: He soon began to giggle, then his giggle grew by half, and then it really happened- Mr. Lowe began to laugh.

ACTOR 2: "You've saved our school! You've saved our school!" He jubilantly roared. "we got the very highest score!" He wrote it on the board.

ACTOR 1: Miss Bonkers did some cartwheels till her face turned cherry red. She bounded up to Mr. Lowe and kissed him on the head.

ACTOR 2: "Hooray! Hooray!"

ACTOR 1: she shouted.

ACTOR 2: "I'm so proud I cannot speak."

ACTOR 1: So she did another cartwheel, and she peck him on the cheek.

ACTOR 2: "Ahem! Ahem!"

ACTOR 1: coughed Mr. Lowe.

ACTOR 2: "You all deserve a bow. I thus declare a holiday-it starts exactly now.
Because you've done so splendidly in every sort of way,
This day forever shall be known as Diffendoofer Day.
And furthermore, I promise I won't ever wear a frown.
For now I know we'll never go to dreary Flobbertown."

ACTOR 1: Then we held a celebration, there was pizza, milk and cake. Like everyone, I ate too much and got a bellyache.

ACTOR 2: We laughed and whooped and hollered the entire school day long, then we all sang, triumphantly, "The Diffendoofer Song."

TOGETHER: We love you, Diffendoofer School, We definitely do.
There surely is no other school that's anything like you.
You're gribbulous, you're grobbulous, each day we love you more.
You are the school we treasure and unceasingly adore.

Oh, finest school in Dinkerville-the only one as well-
We love you, Diffendoofer School, much more than we can tell.
You are so diffendooferouse It gives us joy to say,
Three cheers for Diffendoofer School- Hooray, Hooray, Hooray!!!
```

---

## IC-0513: Horton Hears a Who

- Title: Horton Hears a Who
- Author (byline): Theo Geisel (aka Dr. Seuss)
- Work: Not specified
- Publisher: Random House
- Publication date as stated: Feb 1997
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 1, ACTOR 2
- Teaser before the introduction: Yes
- Spoken words (computed): 1422
- Already set (do not supply): none

### Source block (context only)

```text
Author: Theo Geisel (aka Dr. Seuss)
ISBN: 978-0679883883
Publisher: Random House
Date (Month/Year): Feb 1997
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Theodore Seuss Geisel was born in Springfield Massachusetts in 1904.

ACTOR 2: His mother would often help him go to sleep by chanting rhymes.

ACTOR 1: This combined with an enchanted walk through Springfield’s Forest Park, inspired this young author to write a creative tale about an elephant who courageously protects and defends a speck of dust that is inhabited by a very small society of “people.”

ACTOR 2: Please enjoy this rendition of “Horton Hears a Who”

ACTOR 1: by Theodore Geisel (aka Dr. Seuss)
```

### Performance text (classify this)

```text
ACTOR 1: On the fifteenth of May in the jungle of Nool

ACTOR 2: In the heat of the day, in the cool of the pool

ACTOR 1: He was splashing… enjoying the jungle’s great joys

ACTOR 2: When Horton the elephant heard a small noise.

ACTOR 2: So Horton stopped splashing. He looked toward the sound.

ACTOR 1: “That’s funny,”

ACTOR 2: thought Horton.

ACTOR 1: “There’s no one around.”

ACTOR 2: Then he heard it again! Just a very faint yelp.

ACTOR 1: (make a sound)

ACTOR 2: As if some tiny person were calling for help.

ACTOR 1: “I’ll help you,”

ACTOR 2: said Horton.

ACTOR 1: “But who are you? Where?”

ACTOR 2: He looked and he looked. He could see nothing there But a small speck of dust blowing past through the air.

ACTOR 1: “I say!”

ACTOR 2: murmured Horton.

ACTOR 1: “I’ve never heard tell
Of a small speck of dust that is able to yell.
So you know what I think?... Why, I think that there must
Be someone on top of that small speck of dust?
Some poor little person who’s shaking with fear
That he’ll blow in the pool! He has no way to steer!
I’ll just have to save him. Because after all,
A person’s a person, no matter how small.

ACTOR 2: So gently, and using the greatest of care,
The elephant stretched his great trunk through the air,
And lifted the dust speck and carried it over
And placed it down, safe, on a very soft clover.
“Humpf”

ACTOR 1: humpfed a voice. Twas a sour Kangaroo. And the young kangaroo in her pouch said “Humpf!” too

ACTOR 2: “Why, that speck is as small as the head of a pin. A person on That? Why there never has been”

ACTOR 1: “Believe Me,”

ACTOR 2: said Horton,

ACTOR 2: “I tell you sincerely.
My ears are quite keen and I heard you quite clearly.
I know there’s a person down there. And what’s more.
Quite likely there’s two, Event three, Even Four.

ACTOR 2: “I think you’re a fool”

ACTOR 1: laughed the sour Kangaroo And the young kangaroo in her pouch said,

ACTOR 2: “Me too!” And the Kangaroo plunged in the cool of the pool.

ACTOR 1: “What terrible splashing!”

ACTOR 2: the elephant frowned.

ACTOR 1: “I can’t let my very small persons get drowned. I’ve got to protect them. I’m bigger than they.”

ACTOR 2: So he plucked up the clover and hustled away. Through the high jungle tree tops, the news quickly spread: “He talks to a dust speck! He’s out of his head!”

ACTOR 1:“Should I put this speck down?

ACTOR 2: Horton thought with alarm.

ACTOR 1: “If I do, these small persons may come to great harm. I can’t put it down, And I won’t! After all A person’s a person. No matter how small.

ACTOR 2: Then Horton stopped walking. The speck-voice was talking The voice was so faint he could just barely hear it.

ACTOR 1: “Speak up, please,”

ACTOR 2: said Horton.

ACTOR 1: He put his ear near it.

ACTOR 2: “I know,”

ACTOR 1: called the voice,

ACTOR 2: “I’m too small to be seen
But I’m Mayor of a town that is friendly and clean.
My town is called Who-ville, for I am a who
And we Who’s are all thankful and grateful to you”
And Horton called back to the Mayor of the town,

ACTOR 1: “You’re safe now. Don’t worry. I won’t let you down.”

ACTOR 2: But just as he spoke to the Mayor of the speck Three big jungle monkeys climbed up Horton’s neck. The Wickersham Brothers came shouting,

ACTOR 1: “What Rot”
This elephants talking to Who’s who are not
There aren’t any Whos, And they don’t have a Mayor
And we’re going to stop all this nonsense! So there!”

ACTOR 2: They snatched Horton’s clover! They carried it off
To a black- bottomed eagle named Vlad Vlad-i-Koff,
And, before the poor elephant could even speak,
That eagle flew off with the flower in his beak.
While Horton chased after, with groans, over stones
That tattered his toenails and battered his bones,
And begged,

ACTOR 1: “Please don’t harm all my little folks, who Have as much right to live as us bigger folk do!”

ACTOR 2: But far, far beyond him, that eagle kept flapping
And over his shoulder called back “Quit your yapping.
I’ll fly the night through. I’m a bird. I don’t mind it.
And I’ll hide this, tomorrow, where you’ll never find it!”

ACTOR 1: And at 6:56 the next morning he did it.
It sure was a terrible place that he hid it.
He let that small clover drop somewhere inside
Of a great patch of clovers a hundred miles wide!

ACTOR 2: “Find That!”

ACTOR 1: sneered the bird.

ACTOR 2: “But I think you will fail.” And he left, with a flip, of his black bottomed tail.

ACTOR 1: “I’ll find it!”

ACTOR 2: cried Horton.

ACTOR 1: “I’ll find it or bust!” I shall find my friends on my small speck of dust!”

ACTOR 2: And clover, by clover, by clover with care. He picked up and searched them, and called,

ACTOR 1: “Are you there?”

ACTOR 2: And by noon poor old Horton, more dead than alive,
Had picked, searched, and piled up, nine thousand and five.
Then, on through the afternoon, hour after hour.
Till he found them at last! On the three millionth flower!

ACTOR 1: “My friends!”

ACTOR 2: cried the elephant.

ACTOR 1: “Tell me! Do Tell! Are you safe? Are you sound? Are you whole? Are you well?

ACTOR 2: From down the speck came the voice of the Mayor:
“We’ve really had trouble! Much more than our share.
When that black-bottom birdie let go and we dropped,
Our tea pots are broken, our clocks have all stopped.
So, Horton, Please”

ACTOR 1: pleaded the voice of the Mayor

ACTOR 2: “Will you stick by us Whos while we’re making repairs?

ACTOR 1: “Of course”

ACTOR 2: Horton answered.

ACTOR 1: “Of course I will stick I’ll stick by you small folks through thin and through thick!”

ACTOR 2: “Humpf!”

ACTOR 1: Humpfed a voice!

ACTOR 2: “For almost two days you’ve run wild and insisted On chatting with persons who’ve never existed. And I’m here to state”

ACTOR 1: snapped the big kangaroo,

ACTOR 2: “That your silly nonsensical game is all through!”

ACTOR 1: And the young kangaroo in her pouch said, “Me too!”

ACTOR 2: “With the Wickersham Brother whose help I’ve engaged
You’re going to be roped! And you’re going to be caged!
And, as for your dust speck… hah! That we shall boil
In a hot steaming kettle of Beezle-nut oil!”

ACTOR 1: “Boil it?”

ACTOR 2: gasped Horton!”

ACTOR 1: “Oh, that you can’t do!” It’s all full of persons! They’ll prove it to you!”

ACTOR 2: And down on the dust speck, the scared little Mayor Quick called a big meeting in Who-ville Town Square.

And his people cried loudly. They cried out in fear: “We are here! We are here! We are here! We are here! The elephant smiled:

ACTOR 1: “That was clear as a bell. You kangaroos surely heard that very well.”

ACTOR 2: “I heard no small voice and you didn’t either” And the young kangaroo in her pouch said, “Me, neither” “Grab him!”

ACTOR 1: They shouted,

ACTOR 2: “and cage the big dope!”
Lasso his stomach with ten miles of rope!
Horton fought back with great vigor and vim
But the Wickersham gang was too many for him.
They beat him! They mauled him! They started to haul
Him into his cage, but he managed to call
To the Mayor,

ACTOR 1: I can hear you just fine
But the kangaroo’s ears aren’t as strong quite as mine.
They don’t hear a thing! Are you sure all your boys
Are doing their best? Are they all making noise?

ACTOR 2: Through the town rushed the Mayor, From the east to the west. But everyone seemed to be doing his best,

ACTOR 1: But it wasn’t enough, all this ruckus and roar!
He had to find someone to help him make more.
He raced through each building! He searched floor to floor
And just as he felt he was getting nowhere,
And almost about to give up in despair,
He suddenly burst through a door and that Mayor
Discovered one very small shirker named Jo-Jo
Was standing, just standing, and bouncing a yo-yo!

ACTOR 2: Not making a sound! Not a yipp! Not a chirp!
And the Mayor rushed inside and grabbed the young twerp!
And he climbed with the lad up the Eiffelberg Tower
“This”

ACTOR 1: cried the Mayor

ACTOR 2: “Is your town’s darkest hour!” “We’ve Got to make noises in greater amounts So, open your mouth lad! For every voice counts!”

ACTOR 1: Thus he spoke as he climbed. When he got to the top, The lad cleared his throat and he shouted out

ACTOR 2: “Yopp!”

ACTOR 1: And that “Yopp” That one small, extra Yopp, put it over!

ACTOR 2: Finally, at last! From that speck on that clover Their voices were heard! They rang out clear and clean. And the elephant smiled.

ACTOR 1: “Do you see what I mean?” They’ve proved they are persons, no matter how small. And their whole world was saved by the smallest of all!”
```

---

## IC-0514: How to Be a Villain

- Title: How to Be a Villain
- Author (byline): Neil Zawacki
- Work: Not specified
- Publisher: Chronicle Books
- Publication date as stated: April 2003
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 1, ACTOR 2, TOGETHER, STAGE 2, STAGE 3
- Teaser before the introduction: No
- Spoken words (computed): 1139
- Already set (do not supply): none

### Source block (context only)

```text
Author: Neil Zawacki
ISBN: 978-0811846660
Publisher: Chronicle Books
Date (Month/Year): April 2003
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Dracula. Hannibal. Frankenstein,

ACTOR 2: The doctor or the monster, either applies –

ACTOR 1: Fictional villains are so famous all you need to hear are their names, and you know exactly who they are.

ACTOR 2: Villains are some of the most memorable characters in fiction. But just how do these super villains get launched into infamy?

ACTOR 1: It’s How to Be a Villain, a step-by-step guide by Neil Zawacki, that answers all the most urgent questions . . .

ACTOR 2: From choosing an evil name, to marketing your brand;

ACTOR 1: Finding the perfect evil hideout, to developing an evil masterplan.

ACTOR 2: It’s cheaper than attending the annual bad guy conference

ACTOR 1: And way more fun than being good.

ACTOR 2: How to Be a Villain is guaranteed to elicit deep-throated evil laughs across the land!

TOGETHER: (evil laughter)
```

### Performance text (classify this)

```text
ACTOR 1: Step 1: Choosing an Evil Name (Pg 14-16)

ACTOR 2: To get your career launched with flair you’ll want a good evil name for yourself. One that is memorable, pithy and short. Choose carefully because this is what the world will know you as throughout time!

ACTOR 1: The Normal Name: Believe it or not, you don’t always need a big flash name. Trust in your evil deeds, and, should you become terrible enough, that alone can be enough to inspire fear in all humanity. . . [Updated from Bill Gates and Pat Robertson, you may insert your own real-life villains] Rudy Giuliani, (Actor 2 reacts) OJ Simpson, (Actor 2 reacts) Elon Musk. (Actor 2 reacts)

ACTOR 2: [Or] The Descriptive Name: What makes you so bad? If you like to crush things, for example you might decide to call yourself The Pulverizer. Evil geniuses with multiple limbs might opt for The Octopus.

ACTOR 1: [Or perhaps a more] Sinister Name: Lord FireHammer; Duke IronSkull; Doctor WormBlight -- Let your creativity blossom!

ACTOR 2: Step 2: Evil Branding (Pg 17) Make your new designation echo in the minds of the timid for eons with some sophisticated evil branding. You won’t need to consult Madison Avenue; chances are, you can come up with great ideas on your own. [You’ll need a]

ACTOR 1: SLOGAN – Three to five words that sum up your evil ways in an intimidating fashion. Remember, you’re talking directly to your victims, so make your message something they can relate to, such as, “Mercy is Not an Option!” [add additional examples such as “You Can’t Handle the Truth!” “You underestimate the power of the Dark Side!]

ACTOR 2: [And don’t forget a] TRADEMARK GESTURE -- Whether you leave behind a token of your villainy or howl from a mountaintop each fortnight, consistent delivery of a gesture or symbolic act, in other words a trademark, will help reinforce your name and identity, making it that much more likely that your evil ways will survive in perpetuity. [Insert a variety of gestures, body stances, entrances/exits here; be creative]

ACTOR 1: [Next] THE EVIL LAUGH – A Must-Have (Pg 23) There are a number of excellent ways to enhance your evil persona, from (in a heavy accent) feigning a foreign accent to (assume a physical tick) exaggerating a physical defect or tick. However, the most essential skill by far is an evil laugh.

ACTOR 2: The evil laugh is a defining characteristic of any supervillain, and you will find yourself calling on it quite regularly as you exult in your own wickedness.

ACTOR 1: Ha Ha Ha

ACTOR 2: Hehe-he-he-he

ACTOR 1: Muahahahaha

ACTOR 2: Bwah-ha-ha-ha-ha!!!

TOGETHER: HAHAHAHAHAHAHAHAHAHAHAHAHA

ACTOR 1: Once you have decided upon a laugh, practice it every day. (laugh)

ACTOR 2: Take a deep breath, relax, and feel yourself laugh like a crazed hyena. (laugh)

ACTOR 2: Learn all its different chortles and inflections, exploring the many ways it can inspire fear.

TOGETHER: (laugh)

ACTOR 1: [And finally] FASHION FOR THE EVIL-DOER (Pg 122) The most agonizing decision of your evil career. What to wear? It may seem wrong, but many people will form ideas about how evil you are based on how you dress and carry yourself. 1. ACTOR 2: It’s hard to go wrong with classic black. Sinister, foreboding, fashionable yet fearsome, black creates an air of mystery. (trademark gesture) Classic black remains THE fashion statement for villains everywhere. 2. ACTOR 1: (Pg 125) [But] If you spent your childhood hiding in the backyard reading comic books, you probably won’t be happy with anything less than the supervillain costume with gimmicks.

ACTOR 2: Be it a green jumpsuit with question marks or an outlandish clown suit that shoots confetti, the gimmicky costume will automatically provide a motif from which you can adopt a personal theme.

ACTOR 1: As you design your costume, take your body type into consideration. Colorful leotards may be high on visual impact, but remember, spandex is a privilege, not a right! 3. ACTOR 2: (Pg 131) Evil masterminds who posses a magical inclination may want to invest their money in wizard’s robes.

ACTOR 1: These sleek garments are ideal for sorcerers providing fashion sensibility and open-air comfort.

ACTOR 2: And they look great with sandals or basic black supervillain boot-socks.

ACTOR 1: You can find them in a wide range of colors, including black and red – avoid white [though] both because of the association with good and because you will look like you’re wearing a toga.

ACTOR 2: Step 3: [Don’t forget a] Location for Your Lair (Pg 88) Every evil mastermind needs a base of operations. Choose your lair carefully. If you have enemies, they will probably show up on your doorstep eventually, so you’ll want it to be an impressive edifice to your grandeur. Consider . . . 1. ACTOR 1: (Pg 90) An Underground Secret Headquarters of Doom. (trademark gesture) To the untrained eye the secret entrance looks like nothing more than an isolated shack in the middle of nowhere.

ACTOR 2: But should you take the secret elevator hidden within, all is horribly revealed. An underground headquarters is a diabolical lair of which you can be proud.

ACTOR 1: Popular for their low energy bills, privacy and “only a madman could live here” ambience, (laugh) a subterranean lair is an excellent choice indeed. 2. ACTOR 2: (Pg 92) The Fake Mountain with a hollow interior is another appealing site. On the outside it looks like any other mountain, but with the flip of a switch you can transform it into a deadly fortress of doom! (laugh)

ACTOR 1: The only caveat with the fake mountain is that you should not place it in the middle of a city. For some reason, they are too often noticed there. 3. ACTOR 2: (Pg 93) Although considered gimmicky for years, the amusement park lair has seen a resurgence in popularity in recent times.

ACTOR 1: The reason is simple: The décor can easily be transformed into a carnival of horrors, the fun houses laced with booby traps and the hall of mirrors at the end for confronting the heroes.

ACTOR 2: The tunnel of love offers endless possibilities for becoming the tunnel of screams (scream turning into laughter)

TOGETHER: Fun for the whole family!

ACTOR 1: Step 4: [And Last but Not Least . . . You must have an Evil Plan]

ACTOR 2: (Pg 140) Have you ever wanted to make a great evil plan, but didn’t have the time?

ACTOR 1: You’re not alone. In fact, many evil men and women struggle with this culminating act. The secret to success is planning ahead.

ACTOR 2: The Evil Plan Generator will help you! By identifying your goals, means and target for destruction, the EPG lets you concoct a truly nefarious scheme in a matter of minutes. Simply fill in the blanks! (See fill-in-the-blank options at the end of the selection – ACTOR 1 reads the Plan, asking for the Fill-in-the-blank prompt—ACTOR 2 provides the blank option with gusto) (Pg 156) STAGE 1: To begin, you must first (ACTION) (TARGET). This will cause the world to (REACTION), (DESCRIPTIVE VERB) by your arrival. Who is this (NAME)? Where did they come from? And why do they look so good in (FASHION)?

STAGE 2: Next, you must (ACTION) (MONUMENT). This will all be done from your (BASE), a mysterious place of unrivaled dark glory. Upon seeing this, the world will (REACTION), as countless hordes of (HENCHMEN) hasten to do your every bidding.

STAGE 3: Finally, you must (ACTION) your (WEAPON), bringing about (DESTINY). Your name shall become synonymous with (RANDOM), and no man will ever again dare (TRAGIC PAST). Everyone will bow before your (POWER), and the world will have no choice but to (END RESULT).

TOGETHER: And that’s How to be a Villain! (Evil laughter)
```

---

## IC-0515: How to Survive a Horror Movie

- Title: How to Survive a Horror Movie
- Author (byline): Seth Grahame-Smith
- Work: Not specified
- Publisher: Quirk Productions
- Publication date as stated: May 2007
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 1, ACTOR 2, TOGETHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1366
- Already set (do not supply): none

### Source block (context only)

```text
Author: Seth Grahame-Smith
ISBN: 978-1594741791
Publisher: Quirk Productions
Date (Month/Year): May 2007
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Let’s face it, characters in horror films are pretty stupid.

ACTOR 2: They make bad choices - leaving you to wonder if they have any brains at all. For example . . .

ACTOR 1: They never turn on the lights . . . roaming around in the dark with a serial killer on the loose is a MUCH better option, right?

ACTOR 2: They always go into the basement or wander alone in the woods.

ACTOR 1: They taunt and encourage the killer to come after them in amazing displays of false bravado.

ACTOR 2: “You want some of this – Come and get me, you freak!”

ACTOR 2: They hear a sound and HAVE to go investigate.

ACTOR 1: They utter the phrase:

ACTOR 2: “Let’s split up!”

ACTOR 1: Of all the dumb things people in horror movies do – this is the dumbest!

ACTOR 2: But . . . if you do find yourself trapped in a horror movie, worry not;

ACTOR 1: Today we’ll be presenting you with a comprehensive guide to keep you alive until the credits start rolling.

TOGETHER: How to Survive a Horror Movie by Seth Grahame-Smith
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

(From Chapter 1)

ACTOR 1: Those of us who’ve become trapped in a horror movie have a choice:

ACTOR 2: We can either line up with the other cattle and march into the slaughterhouse

TOGETHER: (Moo!)

ACTOR 1: Or we can fight back.

ACTOR 2: Yes, it’s a long way to the final credits.

ACTOR 1: No, the odds aren’t in our favor.

ACTOR 2: But that’s no excuse to lie down and let the filmmakers have their way with us.

ACTOR 1: (But you have to be smart!)

ACTOR 2: Horror movie characters aren’t killed by machete-wielding monsters or reincarnated psychopaths—

ACTOR 1: They’re killed by ignorance. Ignorance of the mortal danger they’re in.

ACTOR 2: Ignorance of the fact that they’re in a horror movie.

ACTOR 1: (So . . . ) How do you know if you’ve been sucked into the Terrorverse?

ACTOR 2: Sometimes the signs are unmistakable. For instance, if you’re a teenaged babysitter

ACTOR 1: caring for a mute toddler in a remote cabin during a blizzard

ACTOR 2: while an escaped killer roams the woods,

TOGETHER: you’re probably in a horror movie.

ACTOR 1: TAKE A LOOK AROUND. The environment should offer some clues.

ACTOR 2: If you’re on a crowded city street in broad daylight, you’re probably safe

ACTOR 1: (for now).

ACTOR 2: But if you’re anywhere remote—

ACTOR 1: the woods, an old house, an abandoned mental institution in the middle of a blackout—

ACTOR 2: then yes, your chances of being in a horror movie are much higher.

ACTOR 1: Do you hear strange sounds?

ACTOR 2: chi-chi-chi … ah-ah-ah

ACTOR 1: out of nowhere? Are you speaking Japanese?

ACTOR 2: (utter phrases or words in Japanese – Typhoon, Karaoke, Anime, Emoji, Pokemon!)

ACTOR 1: According to the laws of early twenty-first century cinema, anyone speaking Japanese is in a horror movie.

ACTOR 2: If the answer to any of these questions is

TOGETHER: Affirmative

ACTOR 1: then we have to consider the possibility that you’ve become trapped in a horror movie.

ACTOR 2: As much as you may feel like crying or making skid marks in your tighty-whiteys,

ACTOR 1: you’d better pull yourself together—and soon. Because if you don’t, the boogeyman’s really going to give you something to cry about.

ACTOR 1: Your situation requires immediate action, and the C.R.A.V.E. method (COVER, RECON, ARSENAL, VEHICLE, ESCAPE) was developed for just such an emergency.

ACTOR 2: It’s a kind of “stop, drop, and roll” for horror movie victims—

ACTOR 1: a way to stay alive long enough to summon your courage and get out of immediate danger

TOGETHER: C: COVER.

ACTOR 2: What you need right now is a temporary headquarters—a place to wipe the sweat from your brow, take a pull off the old asthma inhaler, and formulate your plan.

ACTOR 1: Some of the best places to do that: Good ol’ everyday houses.

ACTOR 2: Though not ideal fortresses, the average two-story house is almost always the closest option.

ACTOR 2: Water towers. If your movie takes place in a small Midwestern town, this might very well be the tallest structure around.

ACTOR 1: If you can get to the top, you’ll have a highly defensible (there’s only that one long ladder to worry about) perch with a 360-degree bird’s-eye view

TOGETHER: R: RECON.

ACTOR 2: Now that you’ve had a moment to catch your breath, it’s time to get an idea of where the enemy is and what he’s up to.

ACTOR 1: If you don’t have the height of a water tower working for you, peek through the highest window in your hideout and take a look.

ACTOR 2: If you see nothing, they’re probably right behind you. (Actor 1 begins to turn with a stricken look then pantomimes the actions described by Actor 2) No, wait! Don’t turn around; Nice and cool … that’s it. Now, on the count of three, cover your face with your arms and jump over the rail or through the window. (Actor 1 shows a fear of heights/jumping) Either you jump or you die. Ready? One … two … just kidding,

TOGETHER: you’re totally screwed . . . . A: ARSENAL.

ACTOR 1: You see a path to freedom—you’ll need some kind of weapon. If you’re barricaded in a house, look for a baseball bat, kitchen knife, or anything that kids aren’t allowed to play with indoors.

ACTOR 2: If you’re holed up in a church, grab a heavy-duty candlestick.

ACTOR 1: And if you’re up on that water tower, get your hands on the nearest, um … actually, there aren’t too many options with a water tower. You really should’ve thought of that before you climbed up there!

TOGETHER: V: VEHICLE.

ACTOR 2: You’ve summoned some courage, grabbed a weapon, and hopefully spotted a nearby unoccupied vehicle—now it’s time to kick a little ass.

ACTOR 1: In a burst of adrenaline-fueled speed. Your goal—your only goal—is to reach the nearest car or truck, get inside, and blow town as fast as inhumanly possible.

ACTOR 2: Don’t bother smashing the window—they left the car unlocked

ACTOR 1: (Actor 2 provides sound effects and pantomimes) Lock the doors, and pull down the driver’s-side sun visor. The keys will simply drop into your lap. When you try to start the engine, it’ll turn over again and again, but don’t worry—it’ll kick in as soon as the attacker reaches the car and pounds on the windows.

TOGETHER: E: Escape.

ACTOR 2: This is the easy part. Put the car in “D,”

ACTOR 1: point the compass to “N,”

TOGETHER: and get the “F” out of there.

ACTOR 2: [We’ve now come to that portion of our guide entitled] THE SEVEN DEADLY HORROR MOVIE SINS

ACTOR 1: 1ST DEADLY SIN: DOUBT. There are two types of horror movie characters: those who believe your story and those who don’t.

ACTOR 2: (as a parent) It was just a dream, honey.

ACTOR 1: No it wasn’t. Come on, people. Your son or daughter is having recurring dreams about getting brutally murdered night after night, and you’re brushing it aside as what— indigestion?

ACTOR 2: (as a skeptical teenager) Those are just ghost stories our parents told us.

ACTOR 1: Yes, and they just happen to be true.

ACTOR 2: If all the moms and dads have spent the last 17 years telling you not to go into the abandoned mannequin factory, here’s an idea:

TOGETHER: Don’t go into the abandoned mannequin factory.

ACTOR 1: 2ND DEADLY SIN: MACHISMO.

ACTOR 2: [You’ll recognize] The jock who thinks his football skills are enough to defeat the reincarnated serial killer.

ACTOR 1: Remember, [if you are a] male—in horror movies, testosterone might as well be cyanide.

ACTOR 2: (as a jock) You want some of this?

ACTOR 1: You know the guy. The one who just can’t take it anymore.

ACTOR 2: (as a jock) What’s your plan, huh? Sit and wait for that … that thing to pick us off one by one? No way, man! Not me.

ACTOR 1: He runs out into the open, yelling something like

ACTOR 2: (as a jock) C’mon, show your face!

ACTOR 1: And . . . well, you know how that ends.

ACTOR 2: 3RD DEADLY SIN: INDEPENDENCE.

ACTOR 1: (In a Steve Erwin accent) Have you ever seen that documentary about wildebeests? The one where it’s nothing but slow-motion footage of them getting torn apart by lions and crocodiles? Great, isn’t it?

ACTOR 2: (In a Steve Erwin accent) Funny how the predators always seem to kill the animals that are on the outer edges of the herd. The ones who are either too slow or too stupid to draw strength from their numbers. This is not a coincidence.

ACTOR 1: 4TH DEADLY SIN: UGLINESS.

ACTOR 2: Nobody said horror movies were fair.

ACTOR 1: 5TH DEADLY SIN: CURIOSITY.

ACTOR 2: - one of the basic horror movie equations: Investigation = mutilation.

ACTOR 1: (as a young girl) “Is that you, Patches?”

ACTOR 2: If “Patches” is your nickname for the man hiding in your closet with razorblades on his fingertips, then yes, it is.

ACTOR 1: (as a clueless teen) Do you think it’s dead?

ACTOR 2: No. Go ahead and poke it with a stick. We want to watch it grab your arm and bite half your face off.

ACTOR 1: 6TH DEADLY SIN: IRRESPONSIBILITY.

ACTOR 2: In a horror movie, if you accept a task and fail to carry it out, either you or someone close to you is going to die.

ACTOR 1: (as a clueless teen) Aw, what’s a little nap gonna hurt?

ACTOR 2: A lot.

ACTOR 1: (as a clueless babysitter) Trust me, the kids are sound asleep.

ACTOR 2: No, the kids are dead.

ACTOR 1: (as a disgruntled teen) How come I always get the crappy jobs?

ACTOR 2: Because you’re an idiot, and you’re about to prove that fact by failing miserably at the simple task you were assigned.

ACTOR 1: 7TH DEADLY SIN: VEHICULAR SEX.

TOGETHER: Do it and die.

(From the Epilogue)

ACTOR 2: [So . . . ] When is it safe? When we see credits rolling in front of our eyes? Hear applause? When the killer suddenly takes off the mask, shakes our hand, and says, “Nice working with you”?

ACTOR 1: No, it’s never safe. Once you’re in the Terrorverse, you’re in for good—even after the movie that brought you there has wrapped.

ACTOR 2: You succeeded in vanquishing the enemy? Great. Chances are you made it to the final credits, and you’ll lead a long, peaceful life (especially if your movie bombs at the box office).

ACTOR 1: But there will always be the possibility, however slight, that you’ll be called back for sequels.

ACTOR 2: (Ask Jamie Lee Curtis!)

ACTOR 1: Screenwriters will keep dreaming up new villains and killing methods.

ACTOR 2: Directors will get sleeker and bloodier.

ACTOR 1: And the enemy will keep its fangs and machetes razor sharp.

ACTOR 2: You’d better keep your skills the same way.
```

---

## IC-0516: Humpty Dumpty Egg-splodes

- Title: Humpty Dumpty Egg-splodes
- Author (byline): Kevin O’Malley
- Work: Not specified
- Publisher: Scholastic Books
- Publication date as stated: Jan 2001
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 1, ACTOR 2, MR. HATCHERY, MRS. BOARDERING, STUDENT, STUDENT 2, MARY, HUMPTY, JACK, KING COLE, PETER, DUKE, TOWNSPERSON, MOTHER GOOSE, STUDENTS
- Teaser before the introduction: Yes
- Spoken words (computed): 976
- Already set (do not supply): none

### Source block (context only)

```text
Author: Kevin O’Malley
ISBN: 978-0439357388
Publisher: Scholastic Books
Date (Month/Year): Jan 2001
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: Humpty Dumpty has wigged out.

ACTOR 2: Furious about being teased and taunted for his round and bald body and his bad habit of falling off walls, Humpty is wreaking havoc throughout Mother Goose Land.

ACTOR 1: And with Mother Goose out of town, it’s up to Old King Cole to put things right.

ACTOR 2: But as the king points out, he’s a merry old soul, not a smart one.

ACTOR 1: Luckily, he has Jack Be Nimble to help him pick up the pieces.

TOGETHER: Humpty Dumpty Egg-splodes by Kevin O’Malley
```

### Performance text (classify this)

```text
Suggested Roles

ACTOR 1: Mr. Hatchery, Student 2, Mary, Jack,

ACTOR 2: Mrs. Boardering, Student, King Cole, Humpty, Mother Goose and all other bit roles.

(Both actors will create the pantomimes and become the cheering students at the end)

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

MR. HATCHERY: Hi kids, I’m Mr. Hatchery. Your teacher, Mrs. Boardering, asked me to take part in “Read Across America Day.” Today I’m going to read the wonderful book The Nursery Rhymes of Mother Goose: Favorite Rhymes for Young and Old . . . (clears his throat and begins reading in a very flat voice) Mary had a little lamb. Her fleece was white as snow.

MRS. BOARDERING: Mr. Hatchery? I’m going to step down to the teachers’ lounge for a minute.

MR. HATCHERY: (silently acknowledging Mrs. B) And everywhere that Mary went, the lamb was sure to go.

STUDENT: Boring! What does your dad do anyway?

STUDENT 2: Aw . . . jeez, Dad. He works in an office.

MR. HATCHERY: It followed her to school one day, which was against the rules. (closing the book and addressing the class) Does anybody know what happens next? Anybody? No? (and suddenly his demeanor changes) Well, she found a giant egg crushing the school. It wasn’t just any egg, oh no! It was an . . . Egg-Ceedingly large Humpty Dumpty!!

MARY: Humpty Dumpty, what happened to you? You’re huge! (think Godzilla size)

HUMPTY: That’s right. I’m huge and I’m not gonna take it anymore! (mimicking the townsfolk who taunt him) “Oh, look, the tubby bald eggman is falling off the wall, Haa, haa, haa.” (sarcastically) Did anybody ever think how painful it would be to have a horse try to put you back together? No! So I’m back, baby! Say good-bye to Mother Goose Land!

MR. HATCHERY: Mary ran back to Jack’s house as fast as her dress would let her.

MARY: Jack be nimble, Jack be quick, Jack jump over the candlestick, and get over to Old King Cole’s place fast!

JACK: (jumping over a candlestick) Hey, Mary, can’t you see I’m working here? Do you think this is easy? (knocks the candlestick over and has to reset it and try again – he’s not very nimble)

MARY: Humpty Dumpty’s back and he’s gonna stomp the town. Hurry!

MR. HATCHERY: Old King Cole was a merry old soud until Jack came running in.

KING COLE: What? Humpty Dumpty’s gonna wreck the town? What am I supposed to do? I’m not a smart king, just a merry one. The real brains of the town is Mother Goose and she’s away on vacation getting her feathers fluffed!

JACK: Well, you’d better think of something quick. Humpty Dumpty’s headed this way.

KING COLE: (thinking, which is very hard for him) I’ve got it. Get me Peter Piper. . . (Jacks exits and returns with Peter) Peter Piper, pick me a peck of pickled peppers then throw them at Humpty Dumpty. He hates pickled peppers.

PETER: Yes sir, Sire! (races to rapid-fire as many peppers as he can at HD)

HUMPTY: (catching some in his mouth; others in his hands which he stuffs in his mouth) I’ve learned to love pickled peppers!

PETER: (returns to the King) Your Highness, it didn’t work. Humpty just ate the peppers.

(dejected, Peter exits)

KING COLE: (to Jack) How many pecks of pickled peppers did Peter Piper pick?

JACK: He pitched pickled peppers until he was positively popped. Should I try calling Mother Hubbard?

KING COLE: Naw, what’s she got to throw at Humpty? Her cupboard is always bare. Besides, she’s never at home and you’d end up talking to that smart aleck dog. Let’s call the Grand Old Duke of York.

JACK: Good idea! He’s got ten thousand men. (picking up the phone)

(pantomime a great battle with Humpty, with Humpty roaring and winning and the men losing and screaming)

DUKE: Retreat!!!

JACK: (lowering his spy glass and shaking his head) No good, Sire. He marched them all straight up the hill and he marched them down again.

KING COLE: I should have known.

JACK: I could try the Old Woman that Lives in the Shoe.

KING COLE: Naw, she’s got so many children she won’t know what to do.

JACK: (looking out the window) Sire?! Come quick! Humpty’s crashing through the town!

(Humpty rampages)

MR. HATCHERY: Humpty Dumpty was on a rampage. He found Jack Horner sitting in the corner. He stole his plum, Christmas pie and all. He sat on Little Miss Muffet’s tuffet and ate all her curds and whey. He shook the whole town. Things were looking bad.

HUMPTY: (singing as he destroys the bridge) London Bridge is falling down!

TOWNSPERSON: Falling down, falling down. London Bridge is falling down. My fair lady???

KING COLE: (to Jack) I’ve got it. You know Peter . . . Peter Pumpkin Eater?

JACK: Oh, sure. I heard his wife got out of the pumpkin shell. I believe she’s doing very well.

KING COLE: Yes, yes, yes. Go and tell Peter to roll that pumpkin downtown. I want him to stuff Humpty in it. (pantomime of Peter rolling the pumpkin at Humpty)

HUMPTY: Look . . . It’s a squash! (stomping the pumpkin to bits) Roses are red, violets are blue. Pumpkins are orange, and the town is too!

KING COLE: (to Jack, running out of ideas) I’ve got it! Do you know the Muffin Man?

JACK: (unsure) The Muffin Man?

KING COLE: The Muffin Man! Do you know the Muffin Man?

JACK: Oh sure, he lives on Drurey Lane.

KING COLE: Well, go to him and tell him to lay a path of muffins down Main Street. Tell him to make a left onto Wall Street. We’ll drive Humpty Dumpty right up the wall! (pantomime the Muffin Man laying a trail of muffins)

MR. HATCHERY: (very animated) Wrecking a town is hard work. Humpty was really hungry. He followed the muffin trail just as Old King Cole had hoped. (bending, snapping and popping muffins; he follows the trail right up the wall and sits there eating)

KING COLE: Now we have to find a way to push him off. That’ll knock some sense into him.

JACK: (running back into the throne room) Sire, Sire! Dr. Foster, on his way to Gloucester, reports that Mother Goose is on her way back home.

KING COLE: (with a huge sigh of relief) Thank goodness. Now I can get back to being merry.

MOTHER GOOSE: (flying in the window, she collides with King Cole and they struggle to untangle themselves) The town’s a mess. What’s going on here? I can’t even go away for the weekend without this place going to pieces.

MR. HATCHERY: Old King Cole filled Mother Goose in about Humpty Dumpty’s rampage.

MOTHER GOOSE: (honking, hissing and yelling) Get me all the king’s horses and all the king’s men! Send them all to the wall!

JACK: (saluting) Yes, Ma’am! (he races off)

MR. HATCHERY: Meanwhile, Humpty was almost finished with his muffins. He was extremely full. He was getting very sleepy. (HD begins to drift off and as he does so, he slips off the wall) (in a sing-song voice) Humpty Dumpty sat on the wall. Humpty Dumpty had a great fall. All the king’s horses and all the king’s men . . . (building suspense) held out a giant sheet and caught him!

JACK: (to Mother Goose) What are you going to do with him now?

MOTHER GOOSE: Get me Gregory Griggs.

JACK: Gregory Griggs? Had twenty-seven different wigs? He wore them up, he wore them down to please the people of the town? [that] Gregory Griggs?

MOTHER GOOSE: (impatient) Yes, yes, yes! Tell him to bring all his wigs.

MR. HATCHERY: Mother Goose stitched all the wigs together. (flapping her wings she lowers the giant wig onto HD’s bald head) When Humpty woke up, he had a fine head of hair.

(Humpty wakes up, feels his head, perhaps tosses his new mane of hair and assumes a new persona – think “hip” Elvis Presley)

HUMPTY: (*singing and performing in the style of Elvis Presley; adds in a death drop/half split)

MR. HATCHERY: With his egg-citing new look and attitude, Humpty Dumpty became a big star. He does two shows a day and when he falls . . .

HUMPTY: (*continues the performance; adds in a death drop/half split)

MR. HATCHERY: . . . the crowd goes wild!

STUDENTS: (screaming Humpty’s name as if at a rock concert)

MRS. BOARDERING: (entering from the hallway, she’s shocked at what she sees; the students go silent) Sorry I took so long, Mr. Hatchery. Is everything OK?

MR. HATCHERY: Oh, yes, Mrs. Boardering . . . everything worked out, “Happily ever after!”

STUDENTS: (chanting Humpty’s name)
```

---

## IC-0517: Inside Out

- Title: Inside Out
- Author (byline): Suzanne Francis
- Work: Not specified
- Publisher: Random House Books for Young Readers
- Publication date as stated: 978-0736433129
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 1, ACTOR 2, NARRATOR 1, NARRATOR 2, SADNESS, FEAR, DISGUST, ANGER, JOY, TEACHER, RILEY, TOGETHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1342
- Already set (do not supply): none

### Source block (context only)

```text
Author: Suzanne Francis, Adapted from the screenplay by Peter Docter, Meg Lafauve and
Josh Cooley
ISBN: May 2015
Publisher: Random House Books for Young Readers
Date (Month/Year): 978-0736433129
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: According to Psych Central, our society expects us to “appear happy.”

ACTOR 2: Messages to be “strong” and have “good vibes” rule on social media, but the encouragement to steer clear of sadness often starts in childhood.

ACTOR 1: Grownups angrily tell kids to stop crying, even when they have a “good reason.” And we learn early that being sad makes us, and others, uncomfortable.

ACTOR 2: Inside Out reminds us to embrace the wholeness of ourselves, and gives us permission to not be “okay.”

ACTOR 1: After all, you can’t be happy ALL the time.

ACTOR 2: Inside Out adapted by Suzanne Francis
```

### Performance text (classify this)

```text
Adapted from the screenplay by Peter Doctor, Meg Lafauve and Josh Cooley

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles

ACTOR 1: Narrator 1, Joy, Anger, Teacher

ACTOR 2: Narrator 2, Sadness, Fear, Disgust, Riley

NARRATOR 1: (Pg 1-6) On the day Riley was born, Joy found herself inside a strange and beautiful place.

NARRATOR 2: Riley’s mind. [You see] Joy was a glowing collection of yellow energy particles and was one of Riley’s Emotions.

NARRATOR 1: Joy thought it would just be her and Riley forever . . . but 33 seconds later (Riley begins to wail)

SADNESS: I’m Sadness

NARRATOR 1: As time went on, more Emotions showed up inside Headquarters. And with each new Emotion, memories started rolling through in different colored spheres. Purple

FEAR: Look out!

NARRATOR 1: Disgust was green

DISGUST: Ewwwwwwww!

ANGER: (scowling, screaming, growling)

NARRATOR 2: That’s Anger . . . short, red and . . . . (makes a face) angry.

NARRATOR 1: Joy could see why all of them were important . . . except for Sadness. She tried her best to keep Sadness as far from the controls as possible.

NARRATOR 2: Most of Riley’s memories were golden, just like Joy. And the most important ones glowed brighter

NARRATOR 1: Core memories! They power the Islands of Personality:

NARRATOR 2: Hockey Island! Goofball Island, Family Island – And there’s Honesty and Friendship Island – Like mini theme parks!

NARRATOR 1: Riley had a very happy childhood, but when she was 11 years old, her parents made a major decision that changed everything.

NARRATOR 2: Riley’s dad started a new business and the family moved from Minnesota to San Francisco.

FEAR: Look out!

DISGUST: Ewwwwwwww!

ANGER: (scowling, screaming, growling)

ACTOR 1: From the screenplay by Peter Docter, Meg Lafauve and Josh Cooley

NARRATOR 2: (Pg 7-8) The car ride was long and when Dad finally drove down their new block

(Riley looks excited for a moment as she stares at the new house, but her emotions can’t be kept in check)

JOY: (hopefully) Maybe it’s nice on the inside

ANGER: We’re supposed to live here?

FEAR: Can you die from moving?

DISGUST: I’m gonna be sick.

SADNESS: Oh, Riley can’t live here . . .

NARRATOR 1: (Pg 17-19) The first night in the new house was uncomfortable and creepy. Riley had to sleep in a sleeping bag on the floor. And inside Headquarters . .

FEAR: (reacting to a noise) Was it a bear? It’s a bear! I’m so jumpy. My nerves are shot.

JOY: Look, I get it. You have concerns, but we’ve been through worse!

DISGUST: (Sarcastically) Yeah, Joy. We could be lying on a dirty floor . . . in a sleeping bag.

JOY: But think of all the good things . . .

ANGER: No! There’s absolutely no reason for Riley to be happy right now.

FEAR: I say we skip school tomorrow and lock ourselves in the bedroom.

SADNESS: Yeah, we could cry until we can’t breathe. (Pg 15) Something’s wrong with me. It’s like I’m having a breakdown. I’m awful . . . and annoying.

NARRATOR 1: Sadness constantly focused on the negative.

NARRATOR 2: While Joy saw the rain as a fun opportunity for Riley to jump in puddles and carry a cool umbrella, Sadness liked when the rain made Riley feel soggy and droopy.

JOY: (Pg 19) Now hold on. (Pg 21) We are not going to end the day like this. (She shifts through the memory spheres and selects a golden one)

NARRATOR 2: And then she recalled a memory of Riley showcasing all her ice-skating moves on the lake with her parents. (Riley drifts off to sleep with a smile on her face) *****

JOY: (Pg 22-24) (Waking up with tons of energy) Okay! First day of school. Very exciting! Disgust. Make sure Riley stands out today . . . but also blends in.

DISGUST: When I’m through, Riley will look so good the other kids will look at their own outfits and bar.

JOY: (to Sadness) I have a super important job just for you. (She takes a piece of chalk and draws a circle around Sadness) This is the circle of Sadness. Your job is to make sure that ALL the Sadness stays inside it. (Beat – Sadness tries to put a foot outside the circle, but Joy blocks her) Isn’t it fun?

SADNESS: (exceedingly glum) No . . . .

JOY: All right, everyone. We are going to have a good day, which will turn into a good week, a good year and a good LIFE!

NARRATOR 2: (Pg 26-27) Riley waled to her new school. There were tons of students and the school as so big.

FEAR: Are you sure we want to do this?

DISGUST: Okay. We’ve got a group of cool girls at two o-clock. (Disgust turning to excitement) Double ears pierced, infinity scarves . . . We want to be friends with them.

FEAR: Worst case scenario is either quicksand, spontaneous combustion, or getting called on by the teacher. So long as none of those happen . . .

TEACHER: Okay, everybody. We have a new student in class today.

FEAR: Are you kidding me? Out of the gate? Nooooooo! Pretend we can’t speak English!

JOY: (Pg 28-30) Don’t worry. I got this!

RILEY: (Smiling) My name is Riley Anderson. I’m from Minnesota . . . (continues to speak silently)

NARRATOR 1: She told them about being on an ice hockey team, the Prairie Dogs, and how it was a family tradition. But then something very strange happened.

JOY: Sadness! You touched a memory! Get back in your circle!

DISGUST: Cool kids whispering at three o’clock!

FEAR: Did you see that look? They’re judging us!

RILEY: (Riley’s smile fades; she begins to cry) But everything’s different now . . . Since we moved . . . .

FEAR: Oh no! We’re CRYING AT SCHOOL! (PING)

NARRATOR 2: A new memory had been created and it was bright blue. Joy leaned over and pressed the end-of-day Memory Dump button, causing the vacuum tube to come down from the ceiling. (Suction sounds and Joy and Sadness are sucked into the vacuum tube) (Pg 42) Fear, Anger and Disgust were stunned.

DISGUST: We have a major problem. *****

(Joy and Sadness land in a strange remote area the memory spheres fall all around them)

JOY: (Pg 93-94) (as she is gathering the memories – she holds one up) Oh, it’s that time the hockey team showed up and Mom and Dad were there cheering – Look at her having fun and laughing. It’s my favorite.

SADNESS: I love that one too . . . (remembering) It was the day the Prairie Dogs lost the big playoff game. Riley missed the winning shot. She felt awful. She wanted to quit.

NARRATOR 2: (Pg 103) Joy watched as the hockey team surrounded Riley, and suddenly she realized . . .

JOY: Mom and Dad . . . the team . . . they had come to help because of Sadness.

SADNESS: Sorry. I went sad again, didn’t I? (a stricken look appears on her face)

JOY: (Pg 34) What is it?

SADNESS: You! YOU’RE not in Headquarters. Without you, Riley can’t be happy.

JOY: (Pg 68) This way! Riley . . . here we come! (Joy exits pulling Sadness with her) ******

NARRATOR 2: (Pg 91– 92) Meanwhile back at Headquarters . . .

FEAR: We were at school, and we were naked and there was a dog . . . .

ANGER: It was a DREAM! This is ridiculous, we can’t even get a good night’s sleep anymore. Time to take action! (Pg 75) All the good core memories were made in Minnesota. We go back to Minnesota and make more! (Anger picks up a lightbulb-shaped idea)

FEAR: Wait. You’re saying we run away? You can’t be serious . . . it’s just so . . . drastic.

ANGER: Need I remind you how great things were there? Our room? Our backyard? Our friends? (Pg 91) Who’s with me?

DISGUST: (Pg 75) Riley was happier in Minnesota . . . Yeah, let’s do it.

ANGER: (Pg 92) (Anger plugs the idea into the console) She took it! There’s no turning back!

DISGUST: So, how’re we gonna get to Minnesota from here?

ANGER: We’re taking the bus!

DISGUST: How do we get money?

ANGER: Mom’s purse. Mom and Dad got us into this mess. They can pay to get us out. ***BOOOM! scene shift to Joy and Sadness****

JOY: (Pg 94-95) Honesty Island! We lost another island . . . . what is happening? (as realization dawns) Riley is running away.

NARRATOR 2: (Pg 97-99) Suddenly Sadness pointed to a memory recall tube. Normally the tubs were buried deep beneath the shelving of Long-Term Memory, but one of them had become exposed. If they got to it in time . . . .

SADNESS: We can get recalled! (Joy and Sadness push against one another trying to get into the tube) –

JOY: (Pg 103) We have to get back up there!! ******

NARRATOR 1: (Pg 106) Riley’s cell phone rang as she walked through the streets of San Francisco.

FEAR: It’s Mom. She’s on to us.

ANGER: (Pg 109-110) This is madness! She shouldn’t run away.

DISGUST: Let’s get this idea out of her head. (Frantically pulling at the idea bulb in the console)

ANGER: It’s stuck.

DISGUST: Make her feel scared! That’ll make her change her mind. (Fear frantically pushes buttons and pulls levers, but nothing works.)

FEAR: (in frightened shock) Guys, we can’t make Riley feel anything!

ANGER: (Pg 114-115) AAAAAAAHHHHHHH! (suddenly Joy and Sadness race into headquarters out of breath)

DISGUST: Joy, you’ve got to fix this!

JOY: (shakes her head, then speaks to Sadness) Sadness, it’s up to you . . . Riley needs you.

(Sadness takes a deep breath and places both hands on the console. She gently removes the idea bulb)

RILEY: (Standing up from her seat on the bus) Wait! Stop! I want to get off!

NARRATOR 1: She got off the bus and ran toward home. And inside Headquarters Sadness was confidently driving. Joy pulled the yellow core memories out of her bag and handed them over to her. The memories all turned blue.

NARRATOR 2: (Pg 116-117) In the dining room, Riley cried as Sadness placed each memory, one at a time, into the recall unit.

RILEY: I know you don’t want me to, but . . . I miss home. I miss Minnesota. You need me to be happy, but I want my old friends, and my hockey team.

NARRATOR 1: Her parents talked about all the things they missed about Minnesota and the three of them hugged as Riley continued to cry. Sadness took Joy’s hand and placed it on the console alongside her own.

NARRATOR 2: And Riley smiled through her tears. (DING)

FEAR: (Pg 121) They love us!

ANGER: Yeah, Mom and Dad are pretty cool.

DISGUST: Guys, of course they are. But we can’t show it!

NARRATOR 1: (Pg 117) A new core memory was made. This one was gold and blue swirled together . . . a first. A new Family Island rose, bigger and better than the last.

JOY: (Pg 123) Things might have gotten turned inside out

SADNESS: And even upside down

TOGETHER: But everything is going to be just fine.
```

---

## IC-0518: James and the Giant Peach

- Title: James and the Giant Peach
- Author (byline): Roald Dahl
- Work: Not specified
- Publisher: Puffin
- Publication date as stated: April 2000
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 1, ACTOR 2, NARRATOR 1, NARRATOR 2, AUNT SPONGE, AUNT SPIKER, OLD MAN, JAMES, SPIDER, GRASSHOPPER, CENTIPEDE, EARTHWORM, LADYBIRD, NARRATOR, CHIEF OF POLICE, HEAD OF THE FIRE DEPT, NARARTOR 1
- Teaser before the introduction: Yes
- Spoken words (computed): 1342
- Already set (do not supply): none

### Source block (context only)

```text
Author: Roald Dahl
ISBN: 978-0140374247
Publisher: Puffin
Date (Month/Year): April 2000
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 2: James Henry Trotter, a lonely orphan living with two unkind and malicious guardians, longs for friends.

ACTOR 1: When a magical peach grows in his backyard, he unexpectedly finds companionship with a rag-tag bunch of characters.

ACTOR 2: Their journey together is exceptional as they overcome obstacles beyond imagination.

ACTOR 1: And James is transformed by the power of friendship, trust and the shared challenges they face.

ACTOR 2: He comes to realize the truth in this quote by Edna Buchanan: “Friends are the family we choose for ourselves.”

TOGETHER: James and the Giant Peach by Roald Dahl.
```

### Performance text (classify this)

```text
NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

Suggested Roles:

ACTOR 1: Narrator 1, Aunt Spiker, Old Man, Grasshopper, Centipede, Earthworm, Chief of Police,

ACTOR 2: Narrator 2, Aunt Sponge, James, Spider, Ladybird, Head of Fire Department

NOTE: The comedy in this selection comes from the creativity of the actors to create both speaking and non-speaking characters through body stances and sounds (singularly and together). Think of ways to “show” Mother, Father, the rhino, the tree, the hole in the peach. the seagulls, citizens of NYC and the Empire State Building.

NARRATOR 1: (Chpt 1) Until he was four years old, James Henry Trotter (James play happily) had a happy life. (Speaking over James’ playing) He lived peacefully with his mother and father in a beautiful house beside the sea. It was the perfect life . . . . (James resumes playing) Then one day a terrible thing happened. (James freezes) James’s mother and father went to the zoo.

NARRATOR 2: Both of them suddenly got eaten up by an enormous angry rhinoceros which had escaped.

NARRATOR 1: Poor James was sent away to live with his Aunt Sponge and Aunt Spiker.

AUNT SPONGE and AUNT SPIKER: (together) You filthy nuisance!

NARRATOR 2: I am sorry to say they were both really horrible people.

AUNT SPONGE: You disgusting little beast!

AUNT SPIKER: You miserable creature! (James begins to cry) (Chpt 2) What’s the matter with you?

AUNT SPONGE: Beat him!

AUNT SPIKER: I certainly will! (She glares at James who is very frightened)

NARRATOR 2: (Chpt 3) [One day a] rather peculiar thing happened to [James].

OLD MAN: (emerging from behind James) Come, little boy! (beckoning) Come and I will show you something wonderful! (he puts his hand into the pocket of his jacket and takes out a small bag and waves it in front of James’s face; James is enthralled) Take a look! Listen to them move! (James listens [insert sound effect]) (softly) There’s more power and magic in there than in all the rest of the world put together!

JAMES: But – but – what are they?

OLD MAN: Crocodile tongues! Boiled for twenty days with the eyeballs of a lizard! (he pushes the bag into James’s hands) Here! Take it! It’s yours! (Chpt 4) And don’t let those green things escape. Because if they do . . . Whoever they meet first, be it bug, insect, or tree, will get the full power of their magic! Marvelous things will start happening to you – and you will never be miserable again. Off you go! Hurry! (James exits at a run)

NARRATOR 1: (Chpt 5) James was running back towards the house as fast as he could. Then suddenly, just as he was passing the old peach tree, his foot slipped and he fell flat on his face. (James trips and loses all the green things in the bag, he is frantically searching for them when Aunt Spiker enters)

AUNT SPIKER: Get up at once, you lazy little beast! Get over there and finish chopping those logs! ****** Scene break*****

AUNT SPIKER: (Chpt 6) (staring in awe at the top of the peach tree) Sponge! Sponge! Come here and look at this! It’s a peach!

JAMES: (looking up at the tree) Something peculiar is about to happen . . . .

AUNT SPONGE: (preoccupied doing something else) A what? That miserable tree never has any peaches on it. (She sees the enormous peach) There really is a peach up there!

AUNT SPIKER: A nice big one too!

AUNT SPONGE: Why don’t we eat it! (licking her lips)

AUNT SPIKER: (in terror) It’s getting bigger! Great heavens alive!

NARRATOR 2: (Chpt 7) Bigger and bigger grew the peach. It grew as tall and wide as a small house. The bottom part of it gently touched the ground and there it rested.

JAMES: Oh, isn’t it beautiful. It’s the most beautiful thing I’ve ever seen.

AUNT SPIKER: Shut up, you little twerp! It’s none of your business. (walking around the peach) There’s a pile of money to be made out of this if we handle it right! (Chpt 8) (strutting around) Roll up! Only one shilling to see the giant peach! ****** Scene break*****

NARRATOR 1: Later, when the people had all gone home . . .

JAMES: (opening the door) Could I please have something to eat?

AUNT SPIKER: (slamming the door shut) No! We are counting our money! (She cackles and James exits, dejected)

NARRATOR 1: (Chpt 9) James, as though drawn by some powerful magnet, started walking towards the giant peach. (James enacts the narrator’s words, he rubs his cheek against the peach)

JAMES: (in awe) Something stranger than ever this time is about to happen to me again!

NARRATOR 1: Suddenly he happened to notice there was a hole in the side of the peach. (James crawls inside)

JAMES: (Chpt 10) This isn’t a hole . . . It’s a tunnel! (he continues to follow the tunnel and then suddenly – bang – the top of his head bumps into something hard) Good Heavens! I’ve come to the stone in the middle! (He pries open a door in the peach stone and steps through and reacts with large, frightened eyes)

SPIDER: (Chpt 11) I’m hungry!

GRASSHOPPER: I’m famished!

CENTIPEDE: (wriggling) Everyone’s famished! We need food!

GRASSHOPPER: (to James, who does look quite ill, shivering with fright) You look positively ill!

CENTIPEDE: Cheer up, my boy! (Chpt 12) (bragging and wagging his feet to introduce himself) Centipede. I have a lot of legs. One hundred, to be exact.

EARTHWORM: There he goes again! Telling lies about his legs! He’s only got forth two! There’s nothing marvelous about having a lot of legs. The really marvelous thing is to have no legs at all and to be ablet to walk just the same.

CENTIPEDE: You call that walking! You’re a slitherer. You just slither along!

EARTHWORM: (primly) I glide.

CENTIPEDE: You are a slimy beast.

EARTHWORM: I am not a slimy beast!

CENTIPEDE: (growing tired of harassing Earthworm) James? Have you ever in your life seen such a marvelous colossal Centipede as me?

JAMES: I certainly haven’t. How on earth did you get to be like that?

CENTIPEDE: Very peculiar, indeed. I was under the old peach tree and suddenly a funny little green thing came wriggling past my nose.

EARTHWORM: (proudly) I actually swallowed one!

JAMES: Oh! I know what that was!

SPIDER: There were little green things everywhere!

GRASSHOPPER: It’s too late to tell stories now. It’s time to go to sleep! (Chpt 14) (suddenly the peach shook as if in an earthquake)

JAMES: What’s happening? What’s going on? ****** Scene break*****

(Centipede chews through the peach stem with a purpose)

LADYBIRD (off stage): At this moment, Centipede is nibbling away at the stem. We are about to depart forever from the top of this ghastly hill and those two repulsive aunts of yours.

CENTIPEDE: I’ve done it! The journey begins!

NARRATOR 2: Slowly . . .

NARRATOR 1: Insidiously . . .

NARRATOR 2: Oh, most gently. . . The great peach started to lean forward and steal into motion.

GRASSHOPPER and JAMES: (crashing into furniture, walls and each other) ****** Scene break*****

AUNT SPONGE: (Chpt 15) I wonder what became of that horrid little boy last night.

AUNT SPIKER: He probably fell down in the dark and broke his leg.

AUNT SPONGE: Or his neck! (She cackles)

AUNT SPIKER: (sound effect inserted here) Good gracious me! What’s that awful noise? (Both turn around and react in terror. They try to scramble out of the path of the peach, but . . . . screams)

NARRATOR 1: And then there was silence. Aunt Sponge and Aunt Spiker lay lifeless. The peach?

NARRATOR 2: (Chpt 16) A round object will keep rolling as long as it is on a downhill slope.

NARRATOR 1: In this case the land sloped downhill all the way to . . . . ****** Scene break*****

(Atop the peach)

JAMES: (Chpt 18) (bobbing gently) We’re in the middle of the sea!

GRASSHOPPER: (also bobbing but trying to keep the fear out of his voice) I am afraid we find ourselves in a rather awkward situation.

EARTHWORM: Awkward! We are finished!

JAMES: (reassuringly) We are floating beautifully. Sooner or later a ship is bound to come along.

EARTHWORM: If we are not going to be drowned, then we are going to starve to death instead!

CENTIPEDE: Earthworm is right!

JAMES: We have enough food here for weeks!

SPIDER: Where?

JAMES: The peach of course! (he breaks off a piece and takes a bite) Our whole ship is made of food!

GRASSHOPPER: (taking a bite too) Jumping Jehoshophat!

SPIDER: (lassoing a piece of peach with her web) Isn’t it glorious! The finest dinner in the world!

CENTIPEDE: (Chpt 19) (looks over the side of the peach and pointing with many of his legs) Look! Look at that funny black thing gliding through the water!

EARTHWORM: Sharks!!!!

GRASSHOPPER: (looking on the bright side) Perhaps they have come to say hello? (James looks over the side nervously)

SPIDER: We are finished now! They will eat the peach and there’ll be nothing left to stand on.

(Grasshopper shakes his head and moans – James tries to comfort him)

EARTHWORM: I don’t want to be eaten!

CENTIPEDE: (panicked) Come on, James. There must be something we can do.

JAMES: (Chpt 20) I . . . I . . . I . . .

SPIDER: (Chpt 19) Think, James, think!

JAMES: (Chpt 20) There is something We’d need string to make this work!

SPIDER: I can spin (she demonstrates) As much as you want. But why?

JAMES: (firmly) I’m going to lift this peach clear out of the water!

GRASSHOPPER: The boy’s crazy.

LADYBIRD: How are you going to do it?

JAMES: Seagulls! I’m going to take a long silk string and loop one end round a seagull’s neck

(Spider begins spinning and hands the product to James) and tie the other end to the stem of the peach. (James pantomimes and seagull squawks) (with authority) (Chpt 21) Action stations! There’s not a moment to lose! (James smiles as the peach begins to rise)

NARRATOR 1: (Chpt 22) Suddenly. Slowly . . . Majestically

NARRATOR 2: The giant peach rose out of the water like some fabulous golden balloon.

EARTHWORM: (Chpt 23) Good-bye, sharks!

CENTIPEDE: Oh, boy, this is the way to travel! ****** Scene break*****

NARRATOR: (Chpt 31) Faster and faster flew the seagulls [until] (Chpt 33) far below them, in the City of New York, pandemonium was breaking out. (cries from townspeople as they spy the giant peach) A ball as big as a house had been sighted in the sky. It was an enormous bomb sent to blow the city to smithereens! Air-raid sirens began wailing (insert sound effect here) (Chpt 36) James could see the skyscrapers rushing up to meet them. The very tallest of them all had a top that tapered off into a long sharp point.

JAMES: Good-bye, Centipede. Good-bye everybody! (the peach lands on the top of spike of the Empire State Building insert sound effect here)

NARRATOR 2: Suddenly – there was the giant peach, caught on upon the very pinnacle of the Empire State Building

CHIEF OF POLICE: (Chpt 37) It’s a Snozzwanger!

HEAD OF THE FIRE DEPT: It’s a Whangdoodle!

JAMES: (realizing he’s alive, he peesr over the side of the peach and waves) Hello, everybody! Hello! Don’t be frightened. We are so glad to be here!

CHIEF OF POLICE: What about the others? Are any of them dangerous?

JAMES: Of course not! [This is] Spider with a mile of thread inside her. Grasshopper is a boon in millions of ways. This is Centipede. He is so sweet and gentle. And Earthworm? Absolutely grand! (townspeople cheer)

NARRATOR 1: (Chpt 39) And thus the journey ended. But the travelers lived on. Centipede became Vice President of a high-class boot manufacturer.

NARRATOR 2: Earthworm made commercials on television for women’s face creams.

NARARTOR 1: Miss Spider set up a factory and made ropes for tightrope walkers.

NARRATOR 2: Old-Green-Grasshopper became a member of the New York Symphony Orchestra

NARRATOR 1: And the enormous peach stone was set up in a place of honor in Central Park. It became a famous house. And inside the famous house lived a famous person. (James opens the door and steps outside) James Henry Trotter . . . once the saddest and loneliest boy that you could find . . . now had all the friends in the world.
```

---

## IC-0519: Law and Order – Fairy Tale Unit

- Title: Law and Order – Fairy Tale Unit
- Author (byline): Jonathan Rand
- Work: Random Acts of Comedy (Pg 39-72)
- Publisher: Playscripts, Inc.
- Publication date as stated: Aug 2011
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 1, ACTOR 2, INTENSE VOICEOVER, CHUH-CHUNK, CINDY, ZELLE, HD, UGLY D, GOLD, PINOCCHIO, CAPTAIN, MERM, PIG 1, PIG 2, PIG 3, STILTSKIN, PEEP, WOLF, JUDGE, BAILIFF, PIGS, PIG 1 / PIG 2
- Teaser before the introduction: Yes
- Spoken words (computed): 1797
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jonathan Rand
Book: Random Acts of Comedy (Pg 39-72)
ISBN: 978-0981909974
Publisher: Playscripts, Inc.
Date (Month/Year): Aug 2011
```

### Introduction (context only: never use it for content warnings)

```text
TOGETHER: Law and Order: Fairy Tale Unit by Jonathan Rand
```

### Performance text (classify this)

```text
Suggested Roles:

ACTOR 1: Intense Voiceover; Location; Cindy; HD; Gold; Captain; Pig 1; Pig 3; Peep; Wolf; Judge, Bailiff

ACTOR 2: Chuh-Chunk; Time; Zelle; Ugly D; Pinocchio; Merm; Pig 2; Stiltskin

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

INTENSE VOICEOVER: (Pg 43) In the fairy tale criminal justice system, the characters from fairy tales and nursery rhymes are represented by two separate yet equally ridiculous groups: the fairy tale police who investigate fairy tale crime, and the fairy tale district attorneys who prosecute the fairy tale offenders. These are their stories.

CHUH-CHUNK: (Pg 43-45) Chuh-chunk. LOCATION: Chestnut and Hill. TIME: 7:26 A.M.

(A pile of rubble, entirely made of straw. CINDY and H.D. arrive on the scene, each with a cheap cup of coffee. CINDY wears only one shoe; H.D. has his arm in a sling, a bandage wrapped around his head, maybe some other bandages and some bruises.)

CINDY: . . . So what’re we lookin’ at . . . Accident?

ZELLE: Not a chance. Perp struck the property from the rear, letting loose some form of wind power. Hey, what's with the missing shoe?

CINDY: Eh, lost it last night at a Prince concert. (Sings a line from a Prince Song while gyrating in some strange dance move. Realizes she’s being unprofessional and stops, embarrassed. Resumes her professional persona) Long story . . . . Any leads so far on our perp?

ZELLE: No dice. And the boys downtown got nothin' on the tenant either. But come take a look at this. (She holds up some straw) See this yellow-tinted, fibrous material here? We're stumped on what it might be.

HD: Let's have a look. (He does) The texture and appearance is almost straw-like in nature.

ZELLE: Whatever it is, the whole building was made out of it.

HD: What a mess . . .

CINDY: My gut's tellin' me someone's got a problem with the tenant, and for some reason, destroyed the place in retaliation.

HD: And whatever the reason- (Beat) it was the last straw . . .

CINDY: (Pg 50) (CINDY's phone rings. She takes it. Listens then hangs up. She turns to H.D.) Strike two. Downed building out in the boonies. We gotta fly. (They exit) ******** (Pg 50-53) CHUH-CHUNK: Chuh-chunk. LOCATION: The Sticks. TIME: 9:37 A.M.

(H.D. and CINDY enter.)

UGLY D: Took you fellas long enough.

HD: What you got.

UGLY D: Well, I heard on the wire about the pile over on Chestnut. Based on that report and on the workmanship here, it looks like the same perp. Identical approach on the building from the backside; identical wind velocity. This time, though? Different substance. (UGLY D shows a bundle of sticks.)

CINDY: What are those?

HD: They're almost stick-like in nature.

UGLY D: They're sticks. (Beat)

HD: Huh. (Moving on. . . gesturing yonder) Looks like Gold's got a witness.

UGLY D: Next door neighbor. Was on his way home and was first on the scene.

(They head over to GOLD, who has been questioning PINOCCHIO. PINOCCHIO is a normal-looking guy, except for his outrageously long nose.)

CINDY: Hey there, Goldie.

GOLD: I'm guessing you wanna meet our new friend. Tell them exactly what you told me.

HD: Whatsyername, Dumbo.

PINOCCHIO: Uhh, I'm ... Marcus. (Suddenly PINOCCHIO experiences noticeable nose pain. He puts his hand to it.) Ow . . . Okay. I was walking home from a ... doctor's appointment . . . and I suddenly heard this noise. Like someone dropped a box of toothpicks. I look up and I see that mess over there. And that's it.

CINDY: Did you see anything besides the pile of sticks?

PINOCCHIO: No, no, that's all. (Nose pain again.) Ow.

CINDY: Is everything all right, sir?

PINOCCHIO: Yeah, everything's fine. I feel great. (Nose pain.) Ow.

HD: (The detectives are suspicious. H.D. has an idea.) Marcus, let me ask you . . . What's the square root of sixty-four?

PINOCCHIO: Eight.

HD: What do you call a group of geese?

PINOCCHIO: A gaggle.

HD: How often do you work out at the gym?

PINOCCHIO: Twice a day. (Nose pain.) Ow.

CINDY: Mind telling us what's going on, "Marcus"?

HD: Howsabout telling us who you really are, Namey McFake.

PINOCCHIO: Okay, fine. FINE. (Beat.) My name isn't Marcus. (Beat.) It's Pinocchio. (Pause.) I'm what you'd call a test tube kid. There's this rebel scientist my "dad" who created me, and for some reason decided it would be a brilliant idea to endow me with an unbelievably enormous honker. So he merged the DNA of a human and an anteater, and tadahhhh! Oh, and as if that wasn't enough, Doctor Frankenstupid thought it might be, I don't know . . . fun? A challenge? . . . if my nose were connected to nerve endings in my brain. When I lie about anything, my trunk here grows three inches.

GOLD: I don't understand. When you lied before, it didn't look like your nose grew; it looked like you were in pain.

PINOCCHIO: Yeah, well, I can explain that. I wasn't at the doctor for a routine checkup, if ya get my meaning. Right after getting my nose "taken care of," the doctor warned me that my nerve endings would still be sensitive to lies.

GOLD: (Pg 56) If you got a nose job, why is it still long?

PINOCCHIO: It actually used to be ten feet longer-because of my career.

GOLD: What do you do?

PINOCCHIO: I'm running for President. (Double-take to audience) ********

CAPTAIN: (Pg 55-56) (CAPTAIN storms in. She has a hook for a hand. She's livid. She speaks extremely quickly and to the point.) You two better have some news. We've got two downed buildings and zero arrests. I got the commissioner, the mayor, and Governor Grimm, all breathin' down my neck - You two had better track down whoever nixed the straw and the sticks and you better book 'em. You hear me? You book 'em. Now look here-the 911 call just came in from the vics; we're bringin' 'em down to HQ for questioning.

CINDY: Who are they?

CAPTAIN: Pigs. They're pigs.

HD: Cops?

CAPTAIN: Real pigs, you nitwit. Swine, hogs, ham. It's a quarter till. By eleven, I want answers, I want arrests, I want something! Or I will put you both on unpaid suspension faster than you can say "unpaid suspension." (CAPTAIN storms out; Cindy and HD drop their questioning of Pinocchio and exit also) ********* (Pg 59-62 ) CHUH-CHUNK: Chuh-chunk. LOCATION: High Rise East construction site. TIME: 10:42 A.M.

MERM: So, let's review your story. Pig One, you were alone in your straw house; Wolf approaches the house; knocks it down.

PIG 1: Yeah. Kept sayin' he'd blow my house in, which, sounded a little weird. I told him to hold on, that I was shavin'-y'know, the really tough part right here (Indicates his chin area.) and then before I know it, bam, my house is kaput. I was freakin' out, right? So I curly-tail it to my bro's.

PIG 2: He showed up all discombob-uh-lated. Pork almighty . . . Same thing, I'm shavin', and the hairy guy shows up with that fan-a-his, and before ya know it, my bachelor pad's yardwaste.

PIG 3: They arrived at my doorstep, utterly frazzled . . .

STILTSKIN: At which point, the perpetrator arrived, attempted identical fan-powered destruction, but failed.

MERM: What about this Wolf character? You know him?

PIG 3: We did. He was the highest bidder on the contract for all three of our houses. But all of us withdrew at the last minute . . .

PIG 2: We saw him and that poor girl in the red hoodie on Judge Judy. So we certainly didn't want any association with a convicted felon.

STILTSKIN: One thing I'm not clear on: Why the disparity in the composition of your respective residences?

PIG 2: It's a simple story, really. See, Maw and Paw passed away about 10 years back.

PIG 1: Luau . . . (The PIGS pause for a somber moment of reflection.)

PIG 3: And they left behind a sizable trust fund for each of us.

PIG 2: Problem is, me and Pig One, we got our vices. Me, I invested mosta my inheritance as the executive producer of Kim Kardashian's debut album.

PIG 1: This little piggy went to Vegas.

PIG 2: He lost everything on the roulette wheel.

PIG 3: I invested my inheritance in a new condominium-replete with fortified Ukrainian stainless steel, state-of-the-art alarm system, and most importantly: wind-proof foundation. I, too, no longer have money.

PIG 2: But at least we have each other! *******

(Pg 62-64) (STILTSKIN and MERM across from WOLF and Defense Attorney PEEP.)

CHUH-CHUNK: Chuh-chunk. LOCATION: Plea-bargain session. TIME: 1:13 P.M.

STILTSKIN: We're coming in full-steam on this one: Two counts each of malicious destruction of property and reckless endangerment. Nothing less.

PEEP: My client pleads not guilty to all counts.

STILTSKIN: Oh, come off it, Peep. No jury out there would swallow that even if it was corn-battered and served on a stick. We've got eyewitness testimony of your client fleeing the scene with a fan, his personal effects in the rubble, we've got motive, opportunity, and let's not forget the guy's got a rap sheet.

MERM: Picnic-basket theft, nursing home B&E, impersonation of the aged -- and I'm just getting warmed up.

PEEP: For each of those crimes, my client was falsely accused.

MERM: Exactly. That's why his first and middle names are Big and Bad.

WOLF: That's not my name. (PEEP whispers in WOLF's ear.) No, it's okay. I wanna talk. . . My name is B.B. Wolf, yes, but that stands for Bernard Bartholomew Wolf. After the Riding Hood incident, the tabloids invented "Big Bad." I'm not bad, and I'm certainly not big. I'm just a wolf who always seems to end up at the wrong place at the wrong time. . .

STILTSKIN: If you're insistent you're not guilty, why were you at the scene of each crime with a fan?

PEEP: Again, my client has already explained to the police that he received three invitations to BYOF parties on Facebook.

STILTSKIN: And again, we found no such invitation.

WOLF: How many times do I have to get arrested for crimes I don't commit? First the Little Red misunderstanding, then the whole mix-up with that Peter kid, and now this! I can't take it anymore! ****** (Pg 67) CHUH-CHUNK: Chuh-chunk. LOCATION: Courtroom. TIME: 4:30 P.M.

JUDGE: (Pg 69-70) Order!! I will have order!! Prosecution, present your next witness.

STILTSKIN: We call Pigs 1 through 3. (The PIGS all take the stand together.)

BAILIFF: Do you swear to tell the truth the whole truth and nothing but the truth, so help you Goose?

PIGS: We do.

STILTSKIN: Now ... the members of the jury have already heard a detailed, point-by-point analysis of today's horrifying events. But does such an analysis convey the pure emotional turmoil that you three had to endure? . . . (The pigs don’t understand) I'll rephrase. Are you afraid of the Big Bad Wolf?

PIG 1: The Big Bad Wolf?

PIG 3: The Big Bad Wolf?

PEEP: Objection!

STILTSKIN: Are you afraid of Bernard Bartholomew Wolf?

PIG 1: Tra la la la la. (Use a similar rhythm as the song*)

PIG 3: You'll have to excuse my brother. He is speaking in an archaic version of Pig Latin. "Tra la la la la" roughly translates into English as . . . "Yes."

STILTSKIN: And would you describe that fear?

PIG 2: It was terrifyin'. I was just shavin' like any other day, and then outta nowhere this ferocious beast walked right up to my front door and blew my house in.

(An ominous sound effect. The lights suddenly narrow to STILTSKIN. Echoes of the characters)

PIG 2: Walked right up to my front door, front door, front door

ZELLE: Perp struck the property from the rear, rear, rear

UGLY D: . . . approach on the building from the backside, backside, backside.

PIG 3: I, too, no longer have money, money, money.

STILTSKIN: (Suddenly) Objection!

JUDGE: Mr. Stiltskin, did you just object to your own line of questioning?

STILTSKIN: Indeed, I did, Your Honor. Indeed, I did.

JUDGE: I'll allow it.

STILTSKIN: Pigs Number 1 and 2 ... In your testimony just now, you revealed to this court that the defendant approached your front door in order to topple your comically flimsy houses with an industrial fan.

PIG 1 / PIG 2: Yeah. / Yes sir.

STILTSKIN: But the crime scene investigators have confirmed that the point of attack took place from the rear of each house ... (The PIGS are frozen, unflinching.) Therefore, it is my supposition that you three pigs staged the destruction of your homes, knowing you could easily frame a convicted wolf en criminal, and in the end, walk away free pigs having collected on the windfall of insurance money you so desperately desire. (STILTSKIN gets in the PIGS' faces.) That is my supposition!! That is what really happened!! How do you plead?!

PIGS: Okay okay! All right! We did it! Guilty . . . Guilty . . .

PIG 1: We were broke! We needed the money so badly. I haven't bet on [anything] in almost 48 hours.

PIG 2: And KimKard lied to me! She promised that her music would bridge the generation gap and end world hunger with its hypnotic funky rhythms! And that was false! Neither of those things happened!

JUDGE: Bailiffs, take them away.

PIG 3: (As he exits in handcuffs) Well-played, Stiltskin. Well-played . . .
```

---

## IC-0520: The Lorax

- Title: The Lorax
- Author (byline): Theo Geisel (aka Dr. Seuss)
- Work: Not specified
- Publisher: Random House Books
- Publication date as stated: Aug 1971
- Event as filed: Duo Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTOR 2, NARRATOR 1, NARRATOR 2, ONCE-LER A, ONCE-LER B, LORAX, TOGETHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1409
- Already set (do not supply): none

### Source block (context only)

```text
Author: Geisel, Theo (aka Dr. Seuss)
ISBN: 978-0394823379
Publisher: Random House Books
Date (Month/Year): Aug 1971
```

### Introduction (context only: never use it for content warnings)

```text
ACTOR 1: When Dr. Seuss gets serious, you know it must be important. Published in 1971, and perhaps inspired by the "save our planet" mindset of the 1960s, The Lorax is an ecological warning that still rings true today amidst the dangers of clear-cutting, pollution, and disregard for the earth's environment.

ACTOR 2: In The Lorax, we find what we've come to expect from the illustrious doctor: brilliantly whimsical rhymes that are delightfully original. But there is also something more--a powerful message that Seuss implores both adults and children to heed.

TOGETHER: The Lorax by Theo Geisel (aka Dr. Seuss)
```

### Performance text (classify this)

```text
Suggested Roles -- ACTOR 1: Narrator I, Once-ler A

ACTOR 2: Narrator 2, Once-ler B, Lorax

NOTE: This cutting asks each student to portray multiple characters, which is permissible for Nationals and SOME states. It may not meet the rules requirement for DUO in your state! Be sure to check your STATE rules before performing at local tournaments.

NARRATOR 1: At the far end of town where the Grickle-grass grows
and the wind smells slow-and-sour when it blows
and no birds ever sing excepting old crows. . .
is the Street of the Lifted Lorax.

NARRATOR 2: And deep in the Grickle-grass, some people say,
if you look deep enough you can still see, today,
where the Lorax once stood just as long as it could
before somebody lifted the Lorax away.

NARRATOR 1: What was the Lorax? And why was it there? And why was it lifted and taken somewhere from the far end of town where the Grickle-grass grows?

NARRATOR 2: The old Once-ler still lives here. Ask him. He knows.

ONCE-LER A: Now I'll tell you, how the Lorax got lifted and taken away. . .
It all started way back. . . such a long, long time back. . .
Way back in the days when the grass was still green
and the pond was still wet and the clouds were still clean,

ONCE-LER B: and the song of the Swomee-Swans rang out in space. . . one morning, I came to this glorious place. And I first saw the trees!

ONCE-LER A: The Truffula Trees!

ONCE-LER B: The bright-colored tufts of the Truffula Trees! Mile after mile in the fresh morning breeze.

ONCE-LER A: And under the trees, I saw Brown Bar-ba-loots frisking about in their Bar-ba-loot suits as they played in the shade and ate Truffula Fruits.

ONCE-LER B: From the rippulous pond came the comfortable sound of the Humming-Fish humming while splashing around.

ONCE-LER A: But those trees! Those trees! Those Truffula Trees!
All my life I'd been searching for trees such as these.
The touch of their tufts was much softer than silk.
And they had the sweet smell of fresh butterfly milk.

ONCE-LER B: I felt a great leaping of joy in my heart.
I knew just what I'd do! I unloaded my cart.
In no time at all, I had built a small shop.
Then I chopped down a Truffula Tree with one chop.
And with great skillful skill and with great speedy speed,
I took the soft tuft. And I knitted a Thneed!

ONCE-LER A: The instant I'd finished, I heard a ga-Zump! I looked. I saw something pop out of the stump of the tree I'd chopped down. It was sort of a man.

ONCE-LER B: Describe him?. . . That's hard. I don't know if I can. He was shortish. And oldish.

ONCE-LER A: And brownish. And mossy. And he spoke with a voice that was sharpish and bossy.

LORAX: (with a sneeze) Mister! I am the Lorax. I speak for the trees.
I speak for the trees, for the trees have no tongues.
And I'm asking you, sir, at the top of my lungs"-
What's that THING you've made out of my Truffula tuft?

ONCE-LER A: Look Lorax, There's no cause for alarm. I chopped just one tree. I am doing no harm. I'm being quite useful. This thing is a Thneed.

ONCE-LER B: A Theend's a Fine-Something-That-All-People-Need! It's a shirt. It's a sock. It's a glove. It's a hat.

ONCE-LER A: But it has other uses. Yes, far beyond that. You can use it for carpets. For pillows! For sheets! Or curtains! Or covers for bicycle seats!"

LORAX: Sir! You are crazy with greed. There is no one on Earth who would buy that fool Thneed.

ONCE-LER A: But the very next minute I proved he was wrong.
For, just at that minute, a chap came along,
and he thought that the Thneed I had knitted was great.
He happily bought it for three ninety-eight.
(laughing at the Lorax) You poor stupid guy!
You never can tell what some people will buy.

LORAX: I repeat, I speak for the trees!

ONCE-LER A: I'm busy. Shut up, if you please.

ONCE-LER B: I rushed 'cross the room, and in no time at all, built a radio-phone. I put in a quick call.

I called all my brothers and uncles and aunts and I said

ONCE-LER A: Listen here! Here’s a wonderful chance for the whole Once-ler Family to get mighty rich!

ONCE-LER B: [They] were all knitting Theends just as busy as bees, to the sound of the chopping of Truffula Trees. Then . . . Oh! Baby! Oh! How the business did grow!

ONCE-LER A: Now, chopping one tree at a time was too slow
So I quickly invented my Super-Axe-Hacker
which whacked off four Truffula Trees at one smacker.
We were making Thneeds four times as fast as before!
And that Lorax? . . . He knocked on my new office door.

LORAX: I'm the Lorax who speaks for the trees
which you seem to be chopping as fast as you please.
But I'm also in charge of the Brown Bar-ba-loots
who played in the shade in their Bar-ba-loot suits
and happily lived, eating Truffula Fruits.
NOW. . . thanks to your hacking my trees to the ground,
there's not enough Truffula Fruit to go 'round.
And my poor Bar-ba-loots are all getting the crummies
because they have gas, and no food, in their tummies!
They loved living here. But I can't let them stay.
They'll have to find food. And I hope that they may.

ONCE-LER A: I, the Once-ler, felt sad as I watched them all go.
BUT . . . business is business! And business must grow
I meant no harm. I most truly did not.
But I had to grow bigger. So bigger I got.
Then again he came back! I was fixing some pipes
when that old-nuisance Lorax came back with more gripes.

LORAX: (coughing) I am the Lorax (sneezing, snuffling)
Once-ler! You're making such smogulous smoke!
My poor Swomee-Swans. . . why, they can't sing a note!
No one can sing who has smog in his throat.
And so - please pardon my cough –
they cannot live here. So I'm sending them off.
What's more, let me say a few words about Gluppity-Glupp.
Your machinery chugs on, day and night without stop
making Gluppity-Glupp. Also Schloppity-Schlopp.
And what do you do with this leftover goo?. . .
I'll show you. You dirty old Once-ler man, you!
You're glumping the pond where the Humming-Fish hummed!
No more can they hum, for their gills are all gummed.
So I'm sending them off. Oh, their future is dreary.
They'll walk on their fins and get woefully weary
in search of some water that isn't so smeary.

ONCE-LER A: And then I got mad. I got terribly mad.
(yelling) Now listen here, Dad!
All you do is yap-yap and day, 'Bad! Bad! Bad! Bad!'
Well, I have my rights, sir, and I'm telling you
I intend to go on doing just what I do!

ONCE-LER B: And at that very moment, we heard a loud whack!
From outside in the fields came a sickening smack
of an axe on a tree. Then we heard the tree fall.
The very last Truffula Tree of them all!
No more trees. No more Thneeds. No more work to be done.

ONCE-LER A: So, in no time, my uncles and aunts, everyone,
all waved me good-bye. They jumped into my cars
and drove away under the smoke-smuggered stars.
Now all that was left 'neath the bad-smelling sky
was my big empty factory. . . the Lorax. . . and I.

ONCE-LER B: The Lorax said nothing. Just gave a glance. . . just gave a very sad, sad backward glance. . . as he lifted himself by the seat of his pants.

ONCE-LER A: And I'll never forget the grim look on his face
when he heisted himself and took leave of this place,
through a hole in the smog, without leaving a trace.
And all that the Lorax left here in this mess
was a small pile of rocks, with the one word. . .

TOGETHER: UNLESS. (long pause)

ONCE-LER B: Whatever that meant, well, I just couldn't guess.
That was long, long ago.
But each day since that day I've sat here and worried and worried away.
Through the years, while my buildings have fallen apart,
I've worried about it with all of my heart.

ONCE-LER A: But now. . . Now that you're here, the word of the Lorax seems perfectly clear. UNLESS someone like you cares a whole awful lot, nothing is going to get better . . . It's not. SO. . . Catch! (he tosses something down)

ONCE-LER B: It's a Truffula Seed. It's the last one of all!
You're in charge of the last of the Truffula Seeds.
And Truffula Trees are what everyone needs.
Plant a new Truffula. Treat it with care.
Give it clean water. And feed it fresh air.
Grow a forest. Protect it from axes that hack.
Then the Lorax and all of his friends may come back.
```
