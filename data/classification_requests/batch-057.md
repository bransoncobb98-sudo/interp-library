# Classification request: batch 57 of 63 (40 records, IC-2241 to IC-2280)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-057-reply.json`.

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

## IC-2241: From the Flow

- Title: From the Flow
- Author (byline): Janet O’Neill
- Work: Turning Points, Pgs 63-65
- Publisher: Tichenor Publishing
- Publication date as stated: 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: TEACHER, MOTHER
- Teaser before the introduction: No
- Spoken words (computed): 964
- Already set (do not supply): none

### Source block (context only)

```text
Author: Janet O’Neill
Book: Turning Points, Pgs 63-65
Publisher: Tichenor Publishing
ISBN: 978-0742117013
Date: 2001
```

### Introduction (context only: never use it for content warnings)

```text
What I should have said: Suicide is not chosen; it happens when pain exceeds resources for coping with pain. That’s all it’s about. You are not a bad person, or crazy, or weak, or flawed because you feel suicidal. It doesn’t even mean that you really want to die – it only means that you have more pain than you can cope with right now. There are people out there (I’m one of them) who can be with you in this horrible time, and will not judge you, or argue with you, or send you to a hospital, or try to talk you out of how badly you feel. They will . . . I will simply care for you. I’m here . . . let me help.

What I did say: Keep the pen flowing. Never drop the pen. . . Just flow.

From the Flow by Janet O’Neill
```

### Performance text (classify this)

```text
TEACHER: (Pg 63-65) Welcome to my home away from home. Room 316. Parkside High. For thirteen years I have taught English composition to teens. Show them their voice. Help find their voice in print. I read a lot of Peter Elbow, who postulates that if you help someone find their voice, as a teacher, you are an educational success. So that's what I do; I develop voices. They write daily journals and that gives me the chance to delve into what makes teenagers tick. One writes of an impending pom squad tryout, another about their love of Nascar. One day, one writes, “Sometimes I wish the world would leave me alone. Or that I could leave it alone.” My inquisitive mind reels. Am I reading too much into it?

Journals develop voices. That's a fact. When I was sixteen, my English teacher made us write ten minutes a day. No subject. No "daily topic." And confidential -- no telling the parents anything! The only objective was to keep the pen flowing. Never drop the pen, he announced. Just flow.

His name is Dean Aiken and his journal has become my Friday obsession. Once a week, the students stack their notebooks under the chalkboard and I quickly race to Dean's writings first as soon as the bell rings. While others are talking about how the cafeteria food needs improvement, Dean writes in the abstract. He's a junior but hasn't made varsity baseball yet. He doesn't like that. He doesn't like having to take the bus to school.

His parents used to take him. His writings were the same, yet constantly differing. Altering from the glass being half full to half empty. Why can't they just leave me alone? he’d write. "They" could be anyone. "They" were anyone.

Just flow. So I wrote. I told my teacher about how students told me I was a lesbian because of the way I dressed. Told him about how Tim Robertson always calls me a slut if I don't let him copy off my paper. Told him about how I felt sitting alone in the cafeteria for lunch until a teacher sat with me. It helped. And he helped, too. One day, we got a seating chart. Tim was seated in the opposite corner from me. It was only a seating chart, but it was a signal. He was helping me.

Dean's writing became erratic. Days would be skipped completely. Lines would be erased. I felt like some sort of voyeur trying to uncover the mystery of what he'd erased. Then he wrote: My granddad had it tough. He worked at a coal mine 6 to 6. But God helped him. He's resting at the cemetery next to a beautiful tree. He can sleep when he wants. Get up when he wants. He must like that. I know I will. Not "would," but "will." My God, I thought. Does this child really want to die? I slipped a card for a local youth center into his journal. Maybe he'll go, I thought. He has to go.

People think I'm weird, he'd write, but they just don't know what's going down. The messages became blatant cries. I have nowhere to go. I kept him after class to discuss things. What things? He’d say. We'd stare at each other and fifteen minutes later, he'd leave with a pass. Sorry to waste your time. My teacher solved it with a seating chart. I can do this. I can.

My mind raced. What should I do?? I can't tell his parents -- that's the whole point of the journals. It's a secret. But they should know. Could I tell the principal? That'd be worse. He's not even family. Besides, he hasn't actually said he's suicidal, right?

The classes are called to the auditorium over the intercom. The principal steps to the microphone. He announces that a student at our school, Dean Aiken, has died from a fatal gunshot wound to the head. I pinch myself. Wake up! I said. Wake up! But there I was. In an auditorium filled with now-mourning people, apparently the only one who saw it coming. And the only one that did nothing about it. Newspapers ran stories that night, denouncing his father for keeping a gun in the house. Part of me wanted to blame him. I needed someone to share the blame.

Class was canceled for the funeral. Dean has a lot of friends. I could have helped. I could have told. How bad could it have been? I could have done something. Instead, l’d told him to flow.

When his mother asked for a meeting, I was not shocked. She had gathered his belongings from his locker and scoured over them undoubtedly. I would have done it, too. (the conversation echoes in her memory)

MOTHER: Do you read these journals??

TEACHER: Yes. Yes I do. Every Friday.

MOTHER: Then explain to me why you passed Dean's over.

TEACHER: I didn't. I read it.

MOTHER: Well, if you read it you would have known! We all would have known!

TEACHER: I knew . . . I knew.

MOTHER: Then why. Why!!

TEACHER: I don't know. See, the journals are confidential –

MOTHER: Damn you! He came to you. I don't know why he came to you, but he did. You chose to sit there.

TEACHER: No -- I kept him after class –

MOTHER: You call yourself a teacher. You murdered him.

TEACHER: I know, I know. Please forgive me. (to audience) Only I knew I wasn't just asking forgiveness from her. I was asking God as well.

TEACHER: I open my journal and write the events of the day. Usually, I write of achievements. Accomplishments at the job. At home. With my family. Today, I write of being accused of murder. Today I write without having a response. I write to escape. I write to release. I write out of habit.

Just flow, I think. Just flow.
```

---

## IC-2242: Funny Weird or Funny Ha Ha?

- Title: Funny Weird or Funny Ha Ha?
- Author (byline): Neil Smith
- Work: Bang Crunch Stories, Pgs 125-150
- Publisher: Vintage
- Publication date as stated: Jan 2008
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: PEG, LUCY, OPERATOR, CARL’S VOICE, MAN, CARL, TONY
- Teaser before the introduction: Yes
- Spoken words (computed): 1849
- Already set (do not supply): none

### Source block (context only)

```text
Author: Neil Smith
Book: Bang Crunch Stories, Pgs 125-150
ISBN: 978-0307386106
Publisher: Vintage
Date (Month/Year): Jan 2008
```

### Introduction (context only: never use it for content warnings)

```text
Funny Weird or Funny Ha Ha? by Neil Smith
```

### Performance text (classify this)

```text
PEG: (Pg 125-150) I loved Lucy, that loopy redhead with the Silly Putty face. When I was a girl, I'd watch the reruns of her show and howl. I'd practice my Lucy faces. Her bug-eyed surprise. Her clownish smile. Also her blubbering Wahhhhhh! when she was scolded by long-suffering Ricky Ricardo. In my favorite episode, Lucy auditioned for a TV commercial plugging a vitamin tonic.

LUCY: (imitation) Are you rundown and listless? Are you unpopular? The answer to all your problems, friends, is in this little bottle: Vitameatavegamin.

PEG: She poured a spoonful of the tonic and swallowed, her face twisting from its terrible taste. Vitameatavegamin contained 23 percent alcohol, and so, after several run-throughs of the commercial, Lucy was sloshed. She tripped over the product's name, flubbed her lines. Too tipsy to pour the tonic onto her spoon, she downed it straight from the bottle like a Bowery bum. The studio audience and I howled.

Later I put on that sketch for my parents and little sister, Elaine. I stood behind a card table, holding an old bottle of cough syrup filled with apple juice. Behind me was a poster with the slogan: DRINK YOUR WAY TO HEALTH! I had the red hair. I had the rubber face. My middle name was even Lucille. I was sure I'd grow up to be a comedienne.

PEG: (fondly remembering) My late husband, Carl shared my weird sense of humor. For instance, when our son, Max (Max-a-Million, 19 years old now. He starts university in the fall). When Max was born, Carl hung an Edward Gorey poster beside Max's crib -- comical pen drawings of twenty-six little kids representing the letters of the alphabet. Each kid was killed in a bizarre way. "K is for Kate who was struck with an axe. L is for Leo who swallowed some tacks." (beat) Carl died in an unusual way: he was lining up a shot during a curling championship when a blood vessel burst. After his death, "C is for Carl who died on the curling rink" kept running through my head. In the end, I had his ashes placed in a hollowed-out curling stone. (holding up the curling stone by its curved handle, to Carl) Welcome home, Carl.

I talk to Carl all the time, both out loud and in my head. Some people may think chatting with your dead husband is maudlin or the premise of a hokey Hollywood movie. But I'll do what I want. (to Carl) I miss you. (to audience) I feel a familiar, clinging loneliness. I close my eyes and . . . *****Flashback******

PEG: (to audience) 20 of us at AA gathered in the basement of the Atwater Library. I stand at the front like a stand-up comic. The story I tell happened years ago. At the time, my sister owned a townhouse in the red-light district near the bus terminal. Elaine was away for the summer, and after work I'd go water the flowers in her backyard. I'd buy a bottle of wine and gulp most of it down. I'd lie sozzled in her backyard till the fog began dissipating. Then I'd ride the metro home. One night I passed out in the backyard and my husband, sick with worry, found me there around midnight. By this time, I'd sobered up, although my brain felt like a bongo drum. "You're overreacting," I told him, even though Carl wasn't reacting at all. He was dead silent.

As we left my sister's house, we saw a woman teetering on high heels on the front sidewalk. Other than her heels and a tiny purse slung over one shoulder, she was naked - - high on something, a dopey grin on her face. I went inside to call 911. Soon a cop car pulled up, and we watched awkwardly as the two officers wrestled the naked lady into the back seat. By this time, she was laughing.

On our drive home, I tried telling my husband what the 911 operator had asked when I phoned.

OPERATOR: Could you describe the individual, ma' am?

PEG: Describe her? She's the only naked broad on the street. But if you have trouble picking her out, she's the one with the red purse.

(to audience) The people at AA laugh. I tell them that Carl wouldn't even look at me. He glared straight ahead. Finally, he muttered, "A cautionary tale, Peg. A cautionary tale." But it wasn't. Not for me. That naked lady wasn't a warning; she confirmed what I thought an addict was. Someone lurching out of control, demeaning herself in public. I wasn't that. I was a respected MD. I never missed a day of work even during my worst hangovers. ******

PEG: (to audience) A week after my move, my bare feet rest on the curling stone as I read a book: an inside look at the I Love Lucy show. In real life, Ricky was a womanizer and a cheat and Fred a mean-spirited drunk. Ethel struggled with soul-crushing despair and suicidal thoughts. Even Lucy said she could play funny but she was not naturally funny. I've accomplished little. Maybe I have too much crap around me to find my core. I get an idea. I drag myself up, find a roll of paper towels and rip off three sheets. I write IN, OUT and MAX on the sheets before taping them to the walls. For the next few days, I sort through my boxes, Carl egging me on.

CARL’S VOICE: With your red hair, that green sweater makes you look like a leprechaun.

PEG: Out goes the sweater. Out go my old watercolor set, three wristwatches, a desk fan, and on and on. Once my out pile has grown large enough, I load the junk into moving boxes, which I heave into the Dumpster behind my building. Max's stuff goes into boxes that I drag to the storage locker in the basement. Within days, I've discarded two-thirds of my belongings. What the hell am I doing?

CARL’S VOICE: You 're reinventing yourself again. Wife, mother, doctor, drunk, twelve-stepper, widow. Who will Peg be next? What do we get rid of now?

PEG: I eye the curling stone. I stroke its surface. The granite is called Blue Hone, quarried in Scotland. When Carl died, Max was upset that I'd stopped up his father's ashes in a curling stone. Why not sprinkle them in a forest or a river the way normal people do? But I insisted on the curling stone. I wanted Carl around . . . for the camaraderie.

CARL’S VOICE: But that's not all, is it? There's more to it than that.

PEG: (wiping away tears, softly) The memory of love.

CARL’S VOICE: You've stayed dry this long because of one thing. Me. My constant watch. I'm your rock.

PEG: My hand grabs the stone's handle. I grip till my knuckles turn white. I sit awhile and then finally open the bottle of Chardonnay. I slide the cork out. It makes a sound like a kiss. I pour, twisting the bottle slightly so no wine spills. (takes a drink) Warm pear. Golden apple.

Vanilla. (to Carl) I proved you wrong, buster! (to audience) I drink two big glasses.

CARL’S VOICE: The comedy festival is still on. Why don't we go? For old times sake.

PEG: (to audience) So I grab a cab to the Just for Laughs festival. Saint-Denis Street is closed off. On a platform, a woman dressed as the Tin Man, with a funnel on her head and her face painted silver, stands motionless as if rusted solid. Also on hand are acrobats, jugglers of china cups and the dreaded mime. The marquee advertises Andrea Martin's one-woman show, The Lint Inside My Belly Button. *****Flashback*****

PEG: (to audience) One of the last drinks I had was at my sister's fortieth. Everyone got more liquored up than usual. Especially me. Whenever the Chardonnay dipped below three-quarters empty, I motioned to the waiter. At the end of the brunch, I hugged Elaine too hard, and Carl and I left the restaurant. It was a sunny fall afternoon, and I insisted on a stroll, although by this time I was staggering. At the top of a steep cobblestone street, we came upon a blond man pushing an old lady in a wheelchair, a plaid blanket over her legs. The woman, who wore sunglasses and a rain bonnet, was so stooped, I figured she was snoozing.

MAN: Could you folks direct us to Chinatown?

PEG: (slurring) Oh, I love Chinatown! (to audience) Carl gave directions while I stood there pretending to be sober. As the young man pointed toward Chinatown, his hand let go of the wheelchair, which slid forward and began zipping down the street.

I ran after the lady. Halfway down the street, my heart hammering, I grabbed the back of the wheelchair, but then my ankle twisted and I fell to the ground. The wheelchair overturned and the sleeping lady pitched out and tumbled lifeless over the cobblestones. Carl came running toward me. "The lady, the lady," I shouted. "Help the lady!" She was lying still. Carl turned her over. Somehow her sunglasses and rain bonnet had stayed attached to her head. "What the hell?" Carl said. He picked the old lady up by the shoulders of her cardigan and shook her. Her head lolled. Her orthopedic shoes swung. "She's a dummy!" he yelled.

Out of nowhere came the fellow with a handheld camera. He explained we were the victims of a setup for the comedy festival, a candid-camera show called Funny Weird or Funny Ha Ha? He had a waiver for us to sign. I sat on the cobblestones, one knee scraped and bloody, my ankle throbbing, my husband kneeling beside me. I was about to laugh till I turned to Carl. A vein in his neck looked as swollen as a garden hose. He stood, wrested the camera from the guy and heaved it down the street.

CARL: (yelling) You hurt my wife!

MAN: Maybe she fell because she's had too much to drink.

PEG: (to audience) Carl flew at him. I watched my sweet, docile husband, his fist full of blond hair, smash a man's face against cobblestones. (beat) The blond man, eventually let the charges drop. *****

PEG: (to audience) It's the last day of my vacation, and I'm dressing up. I curled my hair and piled it atop my head. I'm wearing red lipstick and contact lenses that turn my eyes baby blue. I'm Lucille Ball.

CARL’S VOICE: You zany redhead.

PEG: (to audience) I'm heading off to AA. In the basement of the Atwater Library, I'm standing in the women's washroom with Ricky Ricardo. His hair is greased back into a pompadour. He has on a jacket with a handkerchief peeking out of his pocket.

TONY: (in a fake Latino accent) I'm nervous, Lucy. I don't have no acting 'sperience."

PEG: (to Tony) We alcoholics all have years of acting experience. (to audience) The story we're sharing tonight is that of Ricky and Lucy, sketches I've written and persuaded Tony to co-star in. Lucy hiding her Vitameatavegamin bottles in the clothes hamper. Ricky blowing a gasket. Lucy making her own wine by stomping barefoot in a vat of grapes. Ricky yelling in rapid-fire Spanish and calling Lucy a wino. Lucy wailing Wahhhhhh!

(rolling her eyes, in her best Lucy imitation) Drink your way to health!

(to audience) Whenever these people stand up and share their stories, a hush falls over the room, a stillness that feels sacred. I love that stillness. It keeps me coming back here. But tonight it's not what I want. Tonight I want this room ringing with laughter.
```

---

## IC-2243: Fur is Back

- Title: Fur is Back
- Author (byline): Eve Ensler
- Work: A Memory, a Monologue, a Rant and a Prayer
- Publisher: Villard
- Publication date as stated: May 2007
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1137
- Already set (do not supply): none

### Source block (context only)

```text
Author: Eve Ensler
Book: A Memory, a Monologue, a Rant and a Prayer
ISBN: 978-0345497918
Publisher: Villard
Date (Month/Year): May 2007
```

### Introduction (context only: never use it for content warnings)

```text
I will admit it. Watching the world news makes me angry. So much violence, corruption and so many crimes against humanity that I feel trapped into an anger that has no outlet. Rage that there’s nothing I can do to stop or fix any of it.

And I, like many people, turn off the TV, and try to find my way to happiness by ignoring the problems of the world. But I know that this is not the answer. We can’t expect to live in our frivolous, self-created bubbles while the world goes to hell. But it seems that more and more, that is the only option left.

Eve Ensler in Fur is Back takes a personal look at how this social “head-in-the-sand” epidemic is played out at a party. When the simple question, “What’s up” is answered honestly in light of our world situation, rather than responded to with “Not much, how about you?”

Fur is Back by Eve Ensler.
```

### Performance text (classify this)

```text
I wanted to be funny. I wanted to be a funny, laughing, invited-to-the-party person. I wanted to be a little flirty, maybe, a little naughty, a little fab, mysterious, chic. I wanted to be fun—telling wild, crazy stories, jumping in the pool naked at midnight, wearing that sexy push-up bra. Driving the convertible fast down the highway in a rainstorm. I wanted to be delicious and adorable and not too available, not too talkative.

I would have settled for a little dry, even, or sarcastic. Dry people get invited to the party. Dry nihilists, who are permanently unhappy, permanently in despair, bleak. They are there in their very expensive torn, shredded black clothing, surrounded by groups of beautiful people with fabulous torn, shredded haircuts that look like they just survived something awful—you know, that private jet ride where they ran out of merlot.

But I am not dry. I am not adorable. I am not funny. I am angry. ***** angry. I am raging.

I do not get invited to parties. Well, not anymore. I did at the beginning. I had a certain charm, a certain flair. People mistook it for funny until they discovered that I was the person who ruins the party. Interrupts the pleasure, brings in the rest of the world like a brutal Chicago winter wind. I am the person who, for some reason, has to see it, say it, and make everyone aware. I am the one who responds to the casual “what’s up” with “Well, I just got back from Afghanistan, downtown Qandah-ar, where the Taliban is back. Where the Taliban actually never went away, but they are now blatantly back because the U.S. supported the wicked jihadis and put them in office. The jihadis who raped and pillaged and murdered and, instead of being brought to justice, were brought to power by the U.S., and now there is so much corruption and so much violence that the Taliban looks good.

I am that person who doesn’t stop there, who has to go on because being at the party makes me even angrier. I somehow forgot until that moment that the rest of the world went on, went to the party, they were laughing, drinking, flirting, enjoying. They weren’t undone or depressed by the whacked things going on. No the person asking me what’s up didn’t really expect an answer, didn’t even particularly want an answer. Was just asking the question, a stupid party question ’cause that’s what people do at parties. They don’t listen, they don’t give a shit, no, that’s why they are at the party. That’s why their whole life is a ***** party. Their whole life is directed toward getting invited to the party. Dressing for the party. Getting drunk or into the party mood, and there I am ruining everything. What’s up?

What’s ***** up? Don’t you read the news? The Amish girls shot down in the school ’cause they were there, ’cause they were girls. Or the girls in the refugee camps in Darfur going to get grass for their donkeys or wood for the fire who get grabbed, who get raped and raped and can’t find their way back. But let’s protect the rapists, okay, let’s defend them like the cleric in Australia said. They are being given too hard a time, a terrible sentence, when it’s really the woman’s fault, she brought it on herself, they brought it on themselves by not wearing a head scarf. They were open meat. If she had just stayed in her home, in her hijab, there wouldn’t have been a problem. The cleric saying this—in 2006. If they had just stayed at home.

If I had just stayed at home, hadn’t gone out, hadn’t opened my mouth. I wasn’t even invited to this party, a friend was invited and took me ’cause she couldn’t find anyone else. It wasn’t a direct invitation, a primary invitation from the source to me, and I am ruining the party, embarrassing my friend. I shouldn’t have gone out of the house. There were too many bad things happening. Maybe it was hearing the woman at the party with the big stuffed thing around her neck say, “Isn’t it fabulous—fur is back.”

Fur is back. Isn’t it fabulous? Mutilation is back. Murder is back. Mink is back. Mink always makes me think about women. Not just that women wear minks, but that there is something about how women are raised to serve. Raised for slaughter. Something about being so beautiful, so soft and warm, that people have to wear you, have to wrap you around their neck or rape you or shoot you in the head or mangle or beat or starve you.

Fur is back. Fur is back. Isn’t it fabulous, fur is back? So, it turns out, is rape. Rape is back. The Taliban is back. O.J. is back. Fur is back. Back back back.

But when did any of this go away? It never went away. It just gets ignored and buried and accepted by the people at parties, by the people who cannot stop partying, who think that life is one big party, which it is for them because they have everything, because they are wealthy and privileged and perfect and partying partying.

Stop it. Stop it. Please please stop. Women are dying. Women have their labias ripped off in the Congo, their faces melted off in Pakistan, they are bought as children in Atlanta. Stop, please, doesn’t it matter to you? Don’t their lives matter? I am screaming. I am on the floor, on the wall-to-wall plush carpet near the buffet table with its goat cheese quesadillas and grilled shrimp and chocolate martinis. I am on the floor screaming, Stop it, stop it.

Stop. Can’t you just stop? For one moment, stop your lives, stop your quest for pleasure, stop your partying. A crowd is now looking at me, a crowd of fabulous partygoers who won’t look directly at me ’cause they are scared they might catch what I have, fabulous partygoers going on as I am being handcuffed, dragged, and removed from the party.

I don’t move, I can’t move. I lie there on the street against the building and I open my eyes. I am looking up, straight up. I don’t remember seeing stars before in the city. There are so many of them and they are particularly sparkly. I don’t know if they are even real. They are so far away and they are right next to me. I am lying there and my eyes are open. I am not funny and my friend’s silk shirt is torn, but I can see what is in front of me. I can see the stars.
```

---

## IC-2244: Getting Sex Out of the Schools and Back into the Gutter Where It Belongs

- Title: Getting Sex Out of the Schools and Back into the Gutter Where It Belongs
- Author (byline): Erma Bombeck
- Work: The Grass is Always Greener over the Septic Tank
- Publisher: Fawcett
- Publication date as stated: Feb 1985
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1141
- Already set (do not supply): none

### Source block (context only)

```text
Author: Erma Bombeck
Book: The Grass is Always Greener over the Septic Tank
ISBN: 978-0449207598
Publisher: Fawcett
Date(Month/Year): Feb 1985
```

### Introduction (context only: never use it for content warnings)

```text
The fact that the morality of this nation has greatly deteriorated cannot be successfully denied. An article in McCall's magazine stated that each year about one million teenagers between the ages of 15 and 19 become pregnant. One survey revealed a 30% increase among teenagers in sexual activity within the last five years. Many other statistics could be quoted to show that we are fast becoming a nation of people who support and practice sexual activity outside of marriage. What can be done to reverse the head-long plunge into complete moral decadence? Those who run our schools believe the answer lies in teaching our children about the sexual functions of their body from kindergarten through twelfth grade. However, Erma Bombeck offers an alternative option . . . Getting Sex Out of the Schools and Back in the Gutter Where It Belongs. Sometimes the best way to approach a serious topic is with a little bit of humor!
```

### Performance text (classify this)

```text
My son was five years old when his teacher sent home a not informing me he was sexually immature.

I confronted her the next day after school and said, “What is this supposed to mean, Mrs. Kravitz?”

It means we had a little quiz the other day on reproductive organs and he defined every one of them as an Askyourfather. You are sending a child into the world, Mrs. Bombeck, who thinks Masters and Johnson, is a golf tournament and fertilization is something you do in the fall to make the lawns green.”

“That’s true.” I nodded.

“Have you ever discussed sex in your home?” she asked.

“No, but once he caught Barbie and Ken together in a cardboard car in their underwear.”

“Have you ever discussed with him the parts of his body?”

“Only those that showed dirt.”

“You have to do better than that. This is a new day, Mrs., Bombeck. We don’t hide our heads in the sand anymore. Suburban schools are taking the lead in informing our young people about sex at an early age. For example, I am expecting a baby and I told the class about it.”

“You told them you had something in the oven?” I asked incredulously.

“I told them I was pregnant! She said.

I bit my finger “Good Lord, Mrs. Kravitz. I didn’t know why my husband gasped every time Lassie cleared the fence until I was twenty-six.”

“Then you had better get used to it., your son is about to be informed.”

The suburbs didn’t invent sex—it only gave it a wider distribution. No one could have known the ramifications sex education could have had in the community. Little boys wrote dirty sayings on the sidewalks with chalk as they always did, but adults didn’t protect. They didn’t understand what they meant.

Parents who tried to deal directly with their children by saying, “Look, Brucie, there seems to be some confusion between sexual and asexual reproduction, “only to be interrupted with, “Look, Dad, you should have come to me sooner. What do you need to know?”

Eavesdropping (among young people) dropped off 75 percent but increased 86 percent among adults. And one second grader confronted his parents one night with, “You little devils, you. And you told me I was conceived without sin.”

Things had clearly gotten out of hand and we knew it. So a meeting was called at the school to discuss the future of sex education.

“Frankly,” said the librarian, “I’m worried. Do you realize the new National Geographic has been in for three weeks and has not been checked out once by a third grader?”

We gasped. “The youngsters don’t wasn’t to play Doctor and Nursie anymore,” said a distraught father. “My son wants to open up his own office.”

“I’m afraid,” said Ken Kinsey, “that the impact of sex education goes even deeper. We now have before us the problem of dress code. It seems with the laxity of certain rules and the casualness with which we are regarding the human body, some youngsters are coming to school in various attire. Tonight, we have been asked to consider the outcome of displaying—(he swallowed hard)—the navel.”

The librarian sucked in her breath. The co-chairman cleared his throat and I grabbed for my son’s sex manual to see if it had a double meaning.

“It seems,” continued Ken, “that many of our little girls have been wearing jeans that fit around the hips and shirts that hang just below the rib cage and there is a bare area in between that needs some clarification. Anyone have any ideas?”

“Well, I have always felt if the Good Lord had meant for people to go nude He would never have invented the wicker chair,” said one mother.

“That is a good point,” said Ken. “Anyone else?”

“Have we established what a navel is?” asked a teacher.

“I think it is safe to assume that most of us are familiar with the navel . . .”

“Wait a minute,” said a mother, “there are navels and there are navels. I mean some are `outies` and some are `innies`. I personally find the outies disgusting.”

“That’s strange,” said her husband, “I find them sexy.”

“You don’t know how strange,” said his wife. “I have an `innie` and demand to know where you’ve seen an ‘outie’”.

“Please people. Let’s get back to the issue here. Should we permit the navel to be displayed in a classroom atmosphere?”

“Today the nave, tomorrow the buttock,” grumbled the math teacher.

“It seems to me,” said a parent, “that if lax dress codes are allowed to continue, we may be in for something that only the National Guard can handle.”

“I worry,” said a mother who had been sitting quietly, “that it will blow the lid off a whole can of emotions. I mean, how do you expect a six-year-old to stay in the lines when he colors if he is distracted by a bared navel witting at the desk next to his.”

“That’s a good point, Ethel,” said Ken.

“I see nothing wrong with navels,” said a militant in the rear. “Why are all of you so hung up over something as normal as a navel?”

“Navels are not on trial here,” interrupted Ken. “It’s simply we must draw the line somewhere with the relaxing of morals among our young people.

“So, if you’re ashamed of your navel,” persisted the militant, “I’ll put a Band-Aid over it.”

“What does the U.S. government say about navels?”Asked a businessman.

“To my knowledge, there is no department at the moment that is conducting any sort of findings on the subject," said Ken. “If we could just get back to the subject . . .”

“If you ask me,” said a concerned mother, “I think by our condoning navels in a public-school building, we are lowering the age of puberty. Next thing you know, we will permit them to have acne before they are tem and lower their voices at nine. I say they are growing up too fast. Let’s save the navels for later when they can handle them and enjoy them like adults.”

There was a round of applause and a few in the back stood up and said, “Here, here.”

“Should we put it to a vote?” asked Ken. “Okay, all of you in favor of issuing a dress code in which navels must be covered, signify by saying , ‘Aye” (a roar). Opposed? (One, “you bet your sweet umbilical cord!’)

“Now, the next thing on the agenda,” said Ken nervously, “is Miss Barker who teaches third-graders human sexuality, would like to have a lab . . .”

I slipped out the back door. I wanted time to consider the ramifications, the objectives, the impact of bringing such a program within my child’s learning processes. Also, to have my six-year-old explain to me what human sexuality is.
```

---

## IC-2245: Girl in Pieces (Charlie and Riley)

- Title: Girl in Pieces (Charlie and Riley)
- Author (byline): Kathleen Glasgow
- Work: Not specified
- Publisher: Delacorte Press
- Publication date as stated: August 2016
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: CHARLIE, RILEY
- Teaser before the introduction: Yes
- Spoken words (computed): 1373
- Already set (do not supply): none

### Source block (context only)

```text
Author: Kathleen Glasgow
ISBN: 978-1101934715
Publisher: Delacorte Press
Date (Month/Year): August 2016
```

### Introduction (context only: never use it for content warnings)

```text
17-year-old Charlie Davis thinks she has little reason to live: her father drowned himself; her abusive mother kicked her out; and her best friend is nearly brain dead after cutting too deeply.

After spending time in treatment with other young women like herself -- those who find comfort in self-harm -- Charlie is released and takes a bus to Arizona where she finds an apartment, a job and begins to think she might be a “real girl.” Pulled in by desire and the feeling of being wanted, she gradually falls for Riley West. But Riley is like her – broken -- and together they fall apart.

Girl in Pieces by Kathleen Glasgow
```

### Performance text (classify this)

```text
CHARLIE: (Pg 81-82) A girl is born.
Her father loves her. Her mother loves her father.
Her father is sad.
Her father drinks and smokes, rocks and cries.
Into the river, he goes.
The mother becomes a fist.
The girl is alone.
No one likes the girl.
She tries.
But her mouth is mush.
Stupid girl. Angry girl.
Girl finds knife. Girl makes herself small, small, smaller.
World gone.

(Intro by 4N6 Fanatics Staff)

CHARLIE: (Pg 232-233) It’s a bad day in the kitchen: Riley has asked me something, and that something is floating in the air between us, becoming heavier and heavier by the second. Riley is staring at me, waiting for me to answer his question.

RILEY: (hoarsely) Please. Your shift’s almost over. I’ll pay you.

CHARLIE: A familiar numbness comes over me as I take off my apron. I don’t say anything to Riley. I hold out my hand for the money and close my fingers around it. I slid[e] the money into my pocket. My fingers fish about for a minute, then give up. Riley [doesn’t] notice the knife in my pocket . . .

(Pg 233-236) The man who answers the door looks me up and down and then past me, to the street, like he wants to make sure I’m alone. He’s chewing on the cap of a pen.

He asks me what I’ve got. [I hand him the money.] The man counts the money, reaches back and drops a brown bag [into my hands.] I just turn and leave. I don’t stop or look back until I’m pushing through the screen door of True Grit.

Riley pulls me into the grill station, holds out his hands. He tucks the bag under his shirt. He whispers for me to cover the grill for him.

On his way to the bathroom, he motions to the refrigerator. When I open it, I see my thank you: another bulky bag of food. I take it like a robot, no feeling, no expression.

I don’t know what to think of what I did or why. I’ve blanked myself out, erased myself.

[At home], I put the bag of food on the table. I slide the knife from my pocket. And then, just like that, all the numbness I had drops away. Doing that for Riley, it felt good. But I’m getting really far down the ladder of rules, and all of a sudden I’m flooded with despair. I try breathing exercises, but I just gasp, I can’t slow down.

My tender kit is still wedged far back under the claw-foot tub, hidden inside [a] suitcase. I don’t want that, I don’t. I run the blade of the knife lightly across my forearm, testing. My skin prickles and longing fills me up; my eyes grow wet. I’m so close to feeling better, feeling release, right here, with the stubby little blade. But I turn my arms over, force myself to look at the rough red lines ridging my soft skin. Anything but that. I let the knife clatter to the sink . . .

(Pg 270-275) I forgot to lock the door. When [Riley] knocks, I don’t answer, and he pushes in anyway. He’s clutching a paper bag and he holds it up to his lips, drinks from it.

I’m between the tub and the wall, where I’ve been burrowed for the past several hours, waiting. Groaning, he settles on the floor next to me, stretching his legs out on the scarred linoleum. He lolls his head to the side. Something catches his eye and he leans forward.

RILEY: Why do you have a suitcase wedged under the tub, Strange Girl?

CHARLIE: Before I can stop him, he slides over and pulls it out. He fixes his glisteny eyes on me, the side of his mouth rising in a smile. He lowers his voice in a spooky way.

RILEY: Is this it? Does the magic suitcase hold the secret of my little stranger?

CHARLIE: He flips the clasps and paws through the shirts until he finds the metal kit. Only he thinks it’s just something neat, because he says, “Cool.” But then he unlatches it. His eyes dart over the objects inside, the creams, the tape, the bandages, everything I bought the first day I got here. My heart’s in my throat, watching him.

It’s a little mean, a little payback for today, for never asking me about myself. Because it’s going to make him scared, and a little sick, being faced with the puzzle pieces of me for a change. Riley picks up the roll of linen hesitantly and lets it unfurl; pieces of broken glass tumble onto the floor, making their family chimelike sound.

RILEY: What the f*** is this?

CHARLIE: Before I can stop myself, I blurt, “It’s me. It’s what I do. What I did, I mean. I’m trying not to do that anymore.” (holds her breath, waiting)

RILEY: (angry, holding out the box) What is this?

CHARLIE: He holds up the pieces of glass one by one, the small plastic container of hydrogen peroxide, the tube of ointment, the roll of gauze. (to Riley) It’s what I use. To cut myself. Those are my things.

(to audience) Riley drops them all back in the box as though they’ve burned his fingers. He kicks the kit violently across the floor and stands up, yanking the hood of his jacket over his head tightly. I close my eyes. The front door slams.

I crawl across the floor and take my kit in my hands, holding it close to my body. I carefully reassemble everything in its place, because it’s all precious to me. In my fingers, the glass tinkles, pricks, tiny promises that I have to steel myself to ignore.

The door to my apartment bangs open.

RILEY: Tell me. Like, what is that all about? Why do you have that box? What does it mean?

CHARLIE: (to Riley) Where did you think my scars came from? Do you think they just . . . appeared by themselves?

RILEY: (mumbling) I don’t know . . . I just . . . I kind of kept it abstract. I figured you were all done with that. It didn’t occur to me that you kept, like, a box of s*** to cut yourself if you [freaking] felt like it.

CHARLIE: (to Riley, breath coming in gasps) Are you the only one in the world who gets to be a [screwup]? Am I spoiled for you now that you’ve seen my stuff? Did it make me real? (to audience) My body is revving up in a dangerous way.

RILEY: (warning tone) Don’t. Don’t even go there.

CHARLIE: (to Riley) I’m the only one here who’s trying not to do the bad thing, who’s trying to get better, and you’re treating me like s*** for it.

(to audience) I ferried his drugs. I let him see all of me, every bit, and now I’m sitting here on the grungy floor, a dog at his feet. Like a dog, I wait for him at night. Like a dog, now stupidly, I only want him to pet me, love me, not leave, and that makes me suddenly, blazingly angry and sad all at once, which feels like fire inside me.

I pound and claw at his legs. He jumps in surprise. He catches my arms, swearing when I struggle, a flicker of something dark crosses his face, his lip curls. His fingers tighten like metal on my skin. He’s shouting now, like my mother . . .

RILEY: What’s wrong with you?!? (raises his hand to strike)

CHARLIE: And then one of his hands is in the air, fingers together, palm flat. (she cowers) My mother and her raised fist flashes in front of my eyes. I shrink away from Riley, shutting myself off, bracing myself.

There is the person people see on the outside and then there is the person on the inside and then, even farther down, is that other buried person, a naked silent creature, not used to light. I have it and now, here, I see it: Riley’s hidden person.

RILEY: Jesus, this is [crap]. You’re still such a kid. I’m twenty-seven years old. What am I doing?

CHARLIE: His face is papery with exhaustion as he walks to the door. I turn off all the lights and curl up in the bathtub in a very tight ball. I imagine myself in an egg, a metal egg, impenetrable, locked on the outside, anything to keep me from crawling to my kit . . .

(Pg 252) I know this is all wrong. But maybe, me being me, this is as good as it’s going to get. It’s too late anyway . . . I’ve already fallen in.
```

---

## IC-2246: Girl in Pieces

- Title: Girl in Pieces
- Author (byline): Kathleen Glasgow
- Work: Not specified
- Publisher: Delacorte Press
- Publication date as stated: Aug 2016
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: CHARLIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1319
- Already set (do not supply): none

### Source block (context only)

```text
Author: Kathleen Glasgow
ISBN: 978-1101934715
Publisher: Delacorte Press
Date (Month/Year): Aug 2016
```

### Introduction (context only: never use it for content warnings)

```text
Studies show that 75% of girls with low self-esteem reported engaging in negative activities like cutting, smoking, drinking and drugs. Charlie Davis is one of those girls. Nearly broken by a suicide attempt and a rush of personal losses, she finds solace in the broken shards of a mason jar.

First came the death of her father, followed by her mother’s abuse and abandonment. Charlie turns to her only friend, Ellis, her Beautiful Girl. But Ellis is battling her own demons and is left stuck in limbo -- cutting deeply enough to cause significant blood loss but not enough to die.

Bandaged and silent, Charlie ends up in a psych unit for self-harmers, trying desperately to put herself back together. Girl in Pieces, by Kathleen Glasgow.
```

### Performance text (classify this)

```text
CHARLIE: (Pg 81-83) A girl is born.
Her father loves her. Her mother loves her father.
Her father is sad.
Her father drinks and smokes, rocks and cries.
Into the river, he goes.
The mother becomes a fist.
The girl is alone.
No one likes the girl.
She tries.
But her mouth is mush
Stupid girl. Angry girl.
Girl finds knife. Girl makes herself small, small, smaller.
World gone.

Girl meets girl. Beautiful Girl! They watch planets move on the ceiling. Beautiful Girl meets Wolf Boy. He fills her up, but makes her small. Girl stays with Beautiful Girl, but wolf boy leaves drugs.

Beautiful Parents are angry. Beautiful Girl lies and blames Girl for drugs. Girl on street. Girl goes home.

Beautiful Girl texts and texts. Something wrong Hurts Girl slips headphones on. Girl slides phone under pillow. Beautiful Girl bleeds too much. Girl gets messed up too, too messed up, broken heart, guilt. World gone.

(Intro by 4N6 Fanatics Staff)

CHARLIE: (Pg 3) Like a baby harp seal, I’m all white. My forearms are thickly bandaged, heavy as clubs. My thighs are wrapped tightly, too; white gauze peeks out from the shorts Nurse Ava pulled from the lost and found box behind the nurses’ station. Like an orphan, I came here with no clothes. Like an orphan, I was wrapped in a bedsheet and left on the lawn of Regions Hospital in the freezing sleet and snow, blood seeping through the flowered sheet. The security guard who found me was bathed in menthol cigarettes and the flat stink of machine coffee. He said, “Holy Mother of God, girl, what’s been done to you?” My mother didn’t come to claim me. But I remember the stars that night. They were like salt against the sky, like someone spilled the shaker against very dark cloth. That mattered to me, their accidental beauty. The last thing I thought I might see before I died on the cold, wet grass. (beat)

(Pg 4) The girls here, they try to get me to talk. I hear their stories every day in Group, at lunch, in Crafts, at breakfast, at dinner. . .These words that spill from them, black memories, they can’t stop. Their stories are eating them alive, turning them inside out. They cannot stop talking. I cut all my words out. My heart was too full of them.

(Pg 5) I room with Louisa. Louisa is older and her hair is like a red and gold noisy ocean down her back. There’s so much of it, she can’t even keep it in with braid or buns or scrunchies. Her hair smells like strawberries; she smells better than any girl I’ve ever known. My first night here, when she lifted her blouse to change for bed, I saw them, all of them, and I sucked my breath in hard. She said, “Don’t be scared, little one.” I wasn’t scared. I just never seen a girl with skin like mine. (beat)

(Pg 9) Sometimes I can’t breathe in this Goddamn place; my chest feels like sand. I don’t understand what’s happening. I was too cold and too long outside. I start to panic, shake, choke, and Louisa, she comes up very close to me in our room. She cups my cheek and even that makes me flinch. She says, “Little one, you’re with your people.” (long Pause as Charlie is lost in thought)

(Pg 15) We’re never in darkness. Every room has lights on in the walls that ping on at 4 p.m. and ping off at six a.m.

How long have I been here? I’m waking from something. From somewhere. A dark place.

(Pg 20) It isn’t true that I want to be like the turtle and be alone. What’s true is that I want Ellis back, but she can never come back, ever, ever. Not the way she was, anyway. When I think about Ellis, I feel sadness, and while I say sadness, what I really mean is a black hole inside me filled with nails and rocks and broken glass and the words I don’t have anymore. (beat)

(Pg 42) The first time I ever cut myself, the best part was after: swabbing the wound with a cotton ball, carefully drying it, inspecting it, this way and that, cradling my arm protectively against my stomach. There, there.

I cut because I can’t deal. It’s as simple as that. The world becomes an ocean, the ocean washes over me, the sound of the waves is deafening, the water drowns my heart, my panic becomes as large as planets. I need release, I need to hurt myself more than the world can hurt me, and then I can comfort myself. There, there.

(Pg 44) It hurts to make a river. The pain is sharp and bleary all at once; curtains part and shut over your eyes; bull breath from your nostrils. It f**** hurts, hurts, hurts. But when the blood comes, everything is warmer and calmer.

(Pg 90) I wondered why [Ellis] picked me to be her friend: me with my haphazardly cut red-and-black hair, my holey cardigans and ripped jeans.

(Pg 69) I know who I am. I mean, I don’t know know, because I’m only 17, but I know who I am when I’m with people, or when they're looking at me. [I’m] that one, the kid who never gets anything right, and sits alone in the cafeteria, and draws all the time, and sometimes she gets mad and punches, because what else is there? So when [someone] says, “Who keeps your secrets?” I think, “Nobody.” Nobody until Ellis.

(Pg 74) [Sometimes] I say Ellis killed herself, but she did not die, die. She isn’t in the ground. There were drugs, wolf boy, and she slid very far from me. And when the wolf was done, he left her gaunt, my Ellis, my plump and glowing friend. And then I guess she tried to be like me. She tried to drain herself, make herself smaller, only cutting wasn’t her thing. I imagine her room soaked in blood, rivers of it, her parents fighting upstream to get to her. But there was too much, do you understand? A person can only lose so much blood, you can only starve the brain of oxygen for so long, or you suffer an anoxic brain injury after hemorrhagic shock, which emptied out my friend and left only her body.

(Pg 342) The text messages flicker in front of my eyes. Smthing hrts. U never sd hurt like this. 2 much.

(Pg 40 – 41) The hands on the wall clock tell me it’s time to get my bandages off. It’s one of the day nurses, Vinnie, who does it, his big hands chapped and methodical. He pauses before he begins unpeeling the pads on my arms. “You want someone here?” I shake my head, No. “Yeah, that’s right. You a tough girl, Davis.”

(Pg 41-42) Carefully he unwinds the gauze from each arm. They make a wet soft, thwack as he tosses them in the metal trash bin. I stare at the ceiling lights so hard dark clouds form over my eyes. There’s the sound of trickling water. Vinnie is washing his hands. I lift my arms up. They’re pale and puckered from being wrapped up for so long. Turning them over, I look at the red ropy scars rivering from my wrists to my elbows. I touch them gingerly; there, there. Underneath these new scars, I can see the old ones. My scars are like a dam or something.

(Pg 45-46) My eyes are fierce with water, and I want Ellis, the Ellis who would dab my cuts and steal wine from her dad so we could cry together. Because when you’re hurt, and someone loves you, they’re supposed to help you, right? When you’re hurt and someone loves you, they kiss you tenderly, and they hold the bottle to your mouth, they stroke your hair with their fingers, right? I’m in a place filled with girls who are filled with longing and I want none of them. I want the one I can’t have, the one who is never coming back.
```

---

## IC-2247: A Girl Named Zippy

- Title: A Girl Named Zippy
- Author (byline): Haven Kimmel
- Work: Not specified
- Publisher: Doubleday
- Publication date as stated: March 2001
- Event as filed: Prose
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

Zippy: (speaking to the audience) Oh. This explained so many things. I couldn’t think of any right off-hand, but I knew my life was about to become tragically clearer to me. (runs inside)

Mom! Mom! How could you not tell me I was adopted?! Don’t you think I have a right to know? And who were my real parents anyway?

(trying to be mature, but spit flies)

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

The drugstore was owned by a man named, no
kidding, Doc Holiday. Many people found Doc
Holiday’s personality objectionable, but I
appreciated how one always knew where one
stood with him, which was too close and making
too much noise. He never even looked at people
as he shouted at them. Asking Doc for advice
was a mistake. I was once in the drugstore when
a woman asked if Bag Balm was good for diaper
rash.

Doc: I don’t know! What are you asking me for?!

(bellowing, looking north)

Zippy: Doc was not in the business in meddling in other people’s affairs. He didn’t step into fights or defend small children from bullies. The bottom line for me was that I wasn’t safe in his establishment, particularly not from Edythe. At the Marathon station, all the mechanics were on full alert when I was there, and would tell me exactly where Edythe was if they saw her approaching, and Big Dave had even figured out a way for me to climb into a little filthy tool closet if it looked like she was actually coming into the station.

But Doc Holiday was a man of no sympathy. Once when Edythe was chasing me I had blindly run behind the counter, and he instantly picked me up by the back of my shirt and plopped me right back in harm’s way.

To be perfectly candid, Doc and I had a history.

My third-grade teacher had been, in my opinion, the meanest woman in the history of the Mooreland Elementary School, and a bad teacher besides. One day in the spring a tornado came, and our classroom was on the second floor, and when we could actually see the tornado in the distance we turned to our teacher to find out what to do and she was completely gone. I had to drag Julie under a desk, using my unexpected emergency strength, which I now know came from the gypsies.

So one afternoon in the summer after my third-
grade year I was standing at the drugstore
counter waiting Doc Holiday make my lemon
phosphate, when in came my wretched, former
teacher. I leaned across the counter and said,
“Speaking of the Wicked Witch of the West,
huh? There’s no place like home, is there?”

(Spoken directly to the audience) For the first and only time in my life, Doc looked me in the eye.

Doc: She’s my wife.

Zippy: (Spoken directly to the audience) He was very quiet, and so, in fact, was the whole planet. (To Doc) She is? (whispering)

Doc: What’s her name? (drilling holes into her head with his glance)

Zippy: Mrs. Holiday. (muttering, swallowing, can’t look at him.) (spoken directly to the audience) I wished for blindness.

Doc: (Handing her the drink.) That’s 26 cents.

Zippy: (Spoken directly to the audience.) I knew that in an emergency I could never count on Doc, and so I tried to keep my guard up at all times, but sometimes I got sorely distracted, notably when the new Josie and the Pussycats comic came out, which it had on this particular afternoon.

I was standing in the corner behind the magazine rack, trying to read a comic I had no intention of purchasing. When my instincts kicked in and I finally looked up, Edythe was heading straight for me. She was staring right at me and grinning. (stands frozen) I began to pray to the baby Jesus that it would just be over quickly, that she would completely hypnotize me and drag me down to her terrible house and finish me off in whatever way she had planned, and that I would not feel any of it, like a gazelle being eaten alive by a hyena on Wild Kingdom.

Edythe leaned closer to my face. She got closer
and closer, and when she was only about three
inches from my nose she quickly and sharply
clacked her false teeth together like a castanet,
which in turn waggled her dreadful and
fascinating whiskers and caused her seven chins
to undulate in dray waves.

As my vision dimmed and my knees began to melt, I heard Doc Holiday say quite loudly to the ice cream freezer:

Doc: That’s enough, Edythe.

Zippy: (Spoken directly to the audience) Still looking right at me, she straightened up and laughed out loud, clapping her hands in front of her like a child at a carnival. She marched out of the drugstore whistling “What a Friend We Have in Jesus.”

I slid limply into a booth at the back of the store and put my head down, trying to catch my breath. Before I knew it, Doc Holiday was standing over me, offering me a lemon phosphate.

Doc: Talk about the Wicked Witch, huh? (spoken grimly)

Zippy: That woman is going to be the death of me.

(staring at her shoes)

Doc: Well, what are you telling me about it for? (bellowing) That’s 26 cents.

Zippy: I slipped the change out of my pocket and placed it gently in his dry, old hand.
```

---

## IC-2248: A Girl’s Guide to Bragging and Lying

- Title: A Girl’s Guide to Bragging and Lying
- Author (byline): Susan Jane Gilman
- Work: Hypocrite in a Pouffy White Dress, Pgs 24-40
- Publisher: Grand Central Publishing
- Publication date as stated: Jan 2005
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: SUSIE, TEACHER, CARMEN, SARA, ROBIN, BATMAN, MOTHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1429
- Already set (do not supply): none

### Source block (context only)

```text
Author: Susan Jane Gilman
Book: Hypocrite in a Pouffy White Dress, Pgs 24-40
ISBN: 978-0446679497
Publisher: Grand Central Publishing
Date (Month/Year): Jan 2005
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

What strikes me now, of course, was how stereotypical our choices were. Not a single girl longed to be a mathematician or a pulmonary cardiologist. (Pg 27) What it really boiled down to [for me], was the “-ess” in the word “stewardess.” It was the culmination of all things feminine and highly desirable. Princess, goddess, actress . . . stewardess. “-Ess” made any profession sound glamorous. If someone had only been enterprising enough to call female MDs “Doctresses” and female scientists “nuclear biolgesses,” I would have been equally enthusiastic about becoming those too.

No matter. After my classmates and I recited our career litanies about a zillion times each, they began to lose their luster. So, we began transforming ourselves. (Pg 28-29) We soon began staking out starring roles for ourselves in an even more fantastic world: Television.

“I call, I’m Ginger!” we’d yell, lunging at the television, trying to be the first one to press her palm over the seductive smile of Tina Louise before the picture flashed to the infinitely duller Professor and Mary Anne. The rule was: Whoever touched a character first got to “be” her for the duration of the show. “I call, I’m Marcia!” we’d shriek, leaving the losers to fight over Cindy and Jan. Cartoons were equally fair game. We “called” Daphne, Veronica, Wonder Woman, and Judy on the Jetsons.

For me one character was the apotheosis of all I admired and hoped to be. By day, Barbara Gordon was the brainy daughter of Gotham’s police commissioner; yet, with one flick of the switch, her vanity table rotated around and she was transformed into Batgirl! -- a crime fighter with stiletto heels, a peak-a-boo black mask and sparkling body suit that made it look like she had been dipped in liquid rubber.

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

SUSIE: (nodding with her hand in the air) Last night my mother was hit by a truck!

This time, Mrs. Mutnick didn’t wait for the end of the day. She telephoned my mother, and during Juice and Cookie Time, they sat down with me again. Out came “The Boy who Cried Wolf” again, and again we had the discussion roughly titled “Why It Is Bad to Lie.” (Pg 39) When we got home from school, [mother] said:

MOTHER: Why don’t we try to come up with the most interesting true thing for you to share? That way, you can show everybody at school how smart you are.

SUSIE: The next day, I trooped into kindergarten armed with my maracas. (in front of the class) Today (shakes maracas) I’m going to tell you about something

(shakes maracas) true. (shakes maracas) Today I’m going to tell you about the Cuban Revolution. What’s a revolution? Sometimes, my mommy said, it’s when people in a country don’t like the way the country is. Sometimes lots of people are poor, and only a few people are rich. . .

(Pg 40) Mrs Mutnick was beaming. I had everyone’s attention. Everybody was focused on me. Not because of my costumes, or who I was pretending to be, but because of what I had to say. It was my moment. Finally, I was a stewardess, I was a prima ballerina. I was BatGirl! And I couldn’t help myself . . .

SUSIE: The Cuban Revolution was led by a man named Fidel Astro. He was named after the dog on the Jetsons!
```

---

## IC-2249: The Girls Who Went Away

- Title: The Girls Who Went Away
- Author (byline): Ann Fessler
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Prose
- Record type: Program
- Speaker labels in the text: ANNIE, MOTHER, DOCTOR, MOM, FESSLER, NANCY, DIANE, CLAUDIA, GLORY, MARGARET, PRINCIPAL, YVONNE, DAD, MARY, POLLIE, LYNNE, DEBORAH, KAREN, CASEWORKER
- Teaser before the introduction: Yes
- Spoken words (computed): 2044
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ann Fessler
ISBN: 978-1594200946
Publisher: Penguin Books
Date (Month/Year): May 2006
Author:
Book:
ISBN:
Publisher:
Date (Month/Year):
```

### Introduction (context only: never use it for content warnings)

```text
Margaret Atwood wrote in The Handmaid’s Tale: “But who can remember pain, once it’s over? All that remains of it is a shadow, not in the mind even, in the flesh. Pain marks you, but too deep to see. Out of sight, out of mind.”

The Girls Who Went Away by Ann Fessler
```

### Performance text (classify this)

```text
ANNIE: (Pg 36-37) Mother, we didn’t go to the circus last night. We went to a doctor.

MOTHER: Oh my God, don’t tell me you’re pregnant!

ANNIE: Within a few days, she took me to her doctor . . .

DOCTOR: There’s a place where they send girls like her in Kansas City. It’s pretty expensive. If you have any money put aside for her, use it for this. She doesn’t deserve to have it anyway.

MOM: (to Annie) . . . and you’re going to stay there until you have the baby. Then you’re going to give your baby up for adoption and you’re going to come home and forget that this ever happened. Someday you’ll thank me.

ANNIE: That was when the shame began. At sixteen, I had to do everything that my mother said. That was it. There were no options. It was all decided for me.

FESSLER: (Pg 20-21) Just about everyone who lived through [the 1950s-1960s] has a memory of a girl from their high school, college, or neighborhood who disappeared. The girls who went away were told by family members, social-service agencies, and clergy that relinquishing their child for adoption was the only acceptable option. It would preserve their reputation and save both mother and child from a lifetime of shame. They must surrender their child, keep their secret, move on, and forget. (beat) Between the end of World War II in 1945 and the passage of Roe v. Wade in 1973, one and a half million babies were relinquished for nonfamily adoptions.

FESSLER: (Pg 19) Despite the increase in the number of young people having sex in the 1950s and 1960s, access to birth control and sex education lagged far behind. Fearing that sex education would promote or encourage sexual relations, parents and schools thought it best to leave young people uninformed.

NANCY: (Pg 55) . . . (to mother) How do they get rid of the mark when they take the baby out?” She stood there, three feet from me, with a look of horror on her face and said.

MOM: My God, Nancy, that baby comes out the same way it went in.

NANCY: I was sixteen and pregnant and I did not know how babies were born. It’s pathetic, but it’s true. I mean, it’s borderline child abuse not to share this kind of information. How can anyone think that we will just absorb it naturally, or that it’s our responsibility as children to figure it out?

FESSLER: (Pg 39) By 1973 the percentage of unmarried girls who had gone “all the way” before they were 20 years old had risen to 68%. (Pg 20) The result was an explosion in premarital pregnancy and in the numbers of babies surrendered for adoption.

DIANE: (Pg 43) Girls are only two types, a Madonna or a whore, and not the singer Madonna, the virgin Madonna. You were good or bad. You were very bad if you had sex. So, you couldn’t really plan to have sex; it had to just happen.

CLAUDIA: (Pg 64) I don’t remember any dialogue around having choices. (mimicking those in charge) You are gonna do the only thing that is right. You’re gonna give that baby to good people, decent people, people who can take care of it because you are so bad and so flawed for just having this happen. (pause as a memory surfaces) (Pg 67) I named my baby Raina Elizabeth [and] I did get to hold her for three days. She had a little tiny heart-shaped mouth, big dark eyes, beautiful skin, and tons and tons of black hair. (pause) And then on the third day my parents came. It was the beginning of it being invisible. It was never, ever, brought up again. It was never talked about—not once, not ever.

GLORY: (Pg 72) I called my folks from college to tell them I was pregnant and my dad said . . . “Don’t come home.” At the time, my dad was a sheriff. He would be up for reelection and he did not want a daughter like me around. It was fine while I was class valedictorian and the shining star, but not while I was pregnant, no.

FESSLER: (Pg 75) In one of the strictest forms of banishment, high schools and most colleges required a pregnant girl to withdraw immediately. It was not until Title IX of the Education Amendments Act of 1972 that federally funded high schools and colleges, by law, could not expel a pregnant girl or a teenage mother.

MARGARET: I got called down to the office and the principal said . . .

PRINCIPAL: There’s a lot of gossip about you being pregnant. We figure that you’re about three to four months and you may not return to school until you have a doctor’s note saying that you’re not pregnant.

MARGARET: The gym teacher helped me clean out my locker and drove me home, and the school called my mother. I had been this girl who didn’t smoke, didn’t drink, didn’t do anything wrong. Everybody’s parents wanted their daughters to be with me. Now, when I walked down the street, parents made their daughters cross the street.

FESSLER: (Pg 77) Meanwhile, the young men who had fathered these children largely escaped social condemnation. Their role in the pregnancy wasn’t publicly visible, so they were not expelled from school, and were generally not treated with scorn, and not considered a disgrace to their families. Most parents supported the double standard by holding their daughters, but not their sons, accountable. (Pg 78) The standards of the day dictated that a young woman was responsible for stopping the advances of a young man. She was ultimately responsible both for his behavior and it was “her own fault” if she got pregnant.

YVONNE: (Pg 89) My dad said . . .

DAD: I’m not going to spend one damn cent on that little bastard.

YVONNE: (Pg 92) What’s worse -- for a child to grow up being adopted or being labeled illegitimate?

What’s going to be harder for him to live with? (Pg 98) From everything I see, I think the general public believes that mothers who give their babies away are glad to be rid of them, they’re glad to be rid of the problem. They think, “She didn’t care about that kid. She just wanted him out of the way so that she could go on having a good time.” I’ve heard people say that. It’s like if you have a child and you’re not married, you don’t have those same maternal feelings that other mothers have? I have never, ever met a mother who felt that way. Never.

MARY: (Pg 102) I told my mother and she started screaming at me. It was horrific. I was told to leave the house and not return. I was not allowed to make a phone call -- not allowed to take any clothes, pack a suitcase, nothing. I don’t remember where I went to use a phone, but I called the doctor I had babysat for and I went to their house. He pleaded with my mother and father to let me come home. But they refused to take me back.

POLLIE: (Pg 103) My mother was horrified. She called me a slut, a whore. And it seemed like just a day or so after that, my mother came in and had me go to the bathroom, disrobe, and get into the bathtub, which was very humiliating in itself. She administered a douche, which was very painful. I didn’t know anything about a douche. I found out later that what she had used was Lysol from the brown bottle. . .

LYNNE: (Pg 132) We drove to the maternity home on back roads. I walked in and there were all of these strange pregnant people and these nuns. And some of the nuns were harsh. Harsh. I had committed a sin. It’s not like today when you go through therapy, for God’s sakes. No. There was no therapy.

DEBORAH: (Pg 133) I found the letters I wrote [to my parents] while I was away. They are hard to read because I was still so naïve. I was trying to protect them, trying to give them this picture of a normal life with my continual, Shirley Temple kind of “I’m having a great day, the baby is kicking, everything is wonderful,” like it was a normal thing. I mean, I was living in an institution, for Christ’s sake. They locked us in at night. It wasn’t normal life.

LYNNE: (Pg 143) I remember the nun at St. Andre’s telling me that it was God’s will. We were fulfilling the needs of women who couldn’t have children. God chose us to bear these children for these women who couldn’t have any. I was so susceptible to this thinking: I must accept God’s will. I could have more children, you see, so what’s one child to be given away? I would see this child in heaven.

KAREN: (Pg 149) Then they would say things about the baby. It’s always “the baby,” never “your baby.”

CASEWORKER: This experience will end. You will forget that you went through this. You will get over it. You know what you did was wrong? You know that you are really not worthy of keeping your own child? That child needs a mother and a father, and the things that they can give that child. You can’t provide anything that child needs.

KAREN: (Pg 152-153) We were not told any of our rights. We were not told we had the right to keep our own baby. The social workers should have been required to tell us what was available to us, so we could make an informed decision. We were never told anything except adoption—it was the only option offered to us. We weren’t told that we could get child support from the fathers. We weren’t told that we could apply for welfare or Aid to Families with Dependent Children, which was available then. There was a lack of informed consent. All of our rights were abused. Ignored and abused. The rights that people take for granted today, we were denied. We didn’t know because we were young, and we trusted our parents, and we trusted authority. They would tell us what was best. So, we figured if that’s what was best, then that was what we needed to do. They’ve injured and damaged millions of people. You’re just so beaten down by being in that place and being told, “You can’t, you can’t, you can’t.” And “You aren’t a mother, you don’t deserve to be a mother.” It was just overwhelming . . .

The whole point was to keep us scared and feeling guilt all the time. And compliant, you know? “You do this and you can go home.” It makes me very, very angry today to think about that manipulation. To me, it was evil. Nobody ever said, “What do you want, Karen? Do you want to keep your baby?”

(pause to regain composure, then with anger)

CASEWORKER: No, no, no. Don’t even think of that because it’s not your child. It’s these people’s child over here. It’s been promised to them. You should be happy you’re giving your child to someone so wonderful who has so much to offer that child. You should be grateful we’re solving your problem. You made this mistake. You caused this problem for everyone.

KAREN: (Pg 154) There was such emotional and mental damage done. We were not criminals. We were mothers. The difference was I was not an authenticated mother. I was an illegal mother. I was a denied mother. And I had to come home and live my life as if I was an unwilling accomplice to the kidnapping of my own child. You have to live with the trauma of losing your child and then you have to live with the trauma of knowing you didn’t stop it. How do you do that?

CONCLUSION We’ve come a long way from 1950 -- from the lack of education; the stigma of being an unwed mother; and a woman’s right to choose. But the pendulum of values began shifting again in 2022. *Since the Supreme Court overturned Roe v. Wade and the federal right to abortion in 2022, there has been a nationwide expansion of maternity homes – many of them faith-based. As abortion restrictions increase, anti-abortion advocates want to open more of these transitional housing facilities, which often have long waitlists. As of 2024, there are more than 450 maternity homes in the U.S. You see . . . ““Nothing changes instantaneously: in a gradually heating bathtub you'd be boiled to death before you knew it.” -- Margaret Atwood, the Handmaid’s Tale

*Conclusion – Source information from “After the End of Roe, a New Beginning for Maternity Homes” at https://www.cnn.com/2024/08/02/health/maternity-homes
```

---

## IC-2250: The God of Cake

- Title: The God of Cake
- Author (byline): Allie Brosh
- Work: Hyperbole and a Half, Pg 54-75
- Publisher: Touchstone Books
- Publication date as stated: Oct 2013
- Event as filed: Prose
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
Will little Allie get her sugar fix and ride the marshmallow giraffe of awesome or will the grown-ups keep her from her ultimate goal of becoming . . .

The God of Cake by Allie Brosh
```

### Performance text (classify this)

```text
ALLIE: (Pg 54-75) My mom baked the most fantastic cake for my grandfather’s birthday. [It] was slathered in thick frosting and topped with creatures my mom crafted out of mini-marshmallows and toothpicks. To a four-year-old, it was a thing of wonder—half toy, half cake, and all glorious possibility. (mimics Mom) “This is for Grandpa, not for you!”

Mom knew that it was extremely important to keep the cake away from me because if I was allowed even a tiny amount of sugar, not only would I become intensely hyperactive, but the entire scope of my existence would funnel down to the singular goal of ingesting more sugar. Cake. Caaake. Cake. Cake. Cake. Cake.

I managed to climb onto the counter and grab a handful while my mom’s back was turned, [and] an irreversible chain reaction was set into motion. Cake. Cake. Cake. Cake. Cake. I had tasted cake and there was no going back. My tiny body morphed into a writhing mass of tenacity encased in desperation. Cake is the only thing that matters!

ALLIE: Mom had prepared the cake early in the day to get the task out of the way. She thought she was being efficient, but really she had only ensured that she would be forced to spend the whole day protecting the cake from my all-encompassing need to eat it. I followed her around doggedly, hoping that she would set the cake down—just for a moment.

Mom quickly tired of having to hold the cake out of my reach. She tried putting [it] on top of the refrigerator, (climbing like a mountain goat) but my freakish climbing abilities soon proved [that] to be an unsatisfactory solution. (Mom sweeps in to grab Allie down from a precarious perch and Allie throws a fit)

Her next attempt at cake security involved putting the cake in the refrigerator and placing a very heavy box in front of the door. The box was far too heavy for me to move. When I discovered that I couldn’t move the box, I decided that the next-best strategy would be to dramatically throw my body against it. (demonstrates) Surprisingly, this tactic did not garner much sympathy.

(mimics Mom, unimpressed, arms crossed) “Get up. Go play with your toys.”

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

## IC-2251: The Good Guy

- Title: The Good Guy
- Author (byline): Laurie Notaro
- Work: Autobiography of a Fat Bride
- Publisher: c Books
- Publication date as stated: July 2003
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2133
- Already set (do not supply): none

### Source block (context only)

```text
Author: Laurie Notaro
Book: Autobiography of a Fat Bride
ISBN: 978-0375760921
Publisher: c Books
Date (Month/Year): July 2003
```

### Introduction (context only: never use it for content warnings)

```text
The illusive . . . the rare . . . I’m talking Loch Ness Monster and Sasquatch rare . . . Every women, everywhere is on the search for The Good Guy by Laurie Notaro.
```

### Performance text (classify this)

```text
You know I've heard there was one out there, one left, running and living among them. I always took it as a tall tale, and urban legend, an archetype of mythical proportions, but maybe he is out there. I believe there were several strands of hair discovered on a bush one time, as well as a questionable poop. Apparently, he's been spotted, according to several notable anthropologists, but never identified. Based on what I've heard, from his appearance, he's indistinguishable from the rest.

I had wanted a good boyfriend all of my life, and when I finally got one, I had no idea what to do with him.

He called when he said he would.

He held my hand when other people were watching.

He had his own car, which, coincidentally actually ran.

His ex-girlfriend lived in another state and although she was currently pregnant, it was BY ANOTHER MAN, and a demonstrated pie chart/timeline proved that my boyfriend's chromosomes could not have, in any way, been detected in a DNA paternity test.

One night, after an evening of drinking, he told me he loved me in a Denny's parking lot at 2 am, and then he bought me a Grand Slam breakfast. When he sobered up the next day, he didn't even take what he said back or ask me to pay half of the check.

What do you do with a guy like that?

I had no idea. I have to admit I was completely perplexed.

All I could do was keep waiting for the Real Boyfriend in him to come out, because I knew the craven creature had to be in there somewhere, lurking. I mean, it's inborn. This one, I figured, was the most patient and affectionate sociopath I had ever dated. On night as he slept, I hovered over the breathing patterns of my boyfriend and whispered. "I command thy demon to show himself!" but all that happened was that the poor little fellow started to drool.

I tried to ask my friends for advice, but they all looked at me as if I was crazy.

"What do you mean 'he's never made you cry?'" my friend Nikki said. "How else are you supposed to know he likes you!"

"Are you serious that he's never stood you up?" my friend Sara said. "That sounds a little... clingy if you ask me."

"I can't believe he hasn't asked you for a loan yet," my friend Kate said. "He must have another girlfriend with a better job."

"I agree, it's highly unusual," my best friend Jamie mentioned, scratching her chin. "But could it be— Nah. No. Nope. No way. I mean, I don't think so, what are the chances? Are you really, completely sure that he's not working undercover, perhaps as a religious missionary attempting to save your damned soul or a guy who's trying to sell you life insurance or a mutual fund?"

"I'm pretty sure," I disclosed.

“I don't want to freak you out, but I think you've found him."

"Found who?" I asked.

She smiled. "The Good Guy," she said with a wink.

I freaked out. I mean, this was pressure. If he really was a Good Guy, the weight on my shoulders was insurmountable. Because that meant I had to keep him, if I spooked him or chased him away or introduced him to any of my attractive friends, I would never find another of his kind. Therefore I was facing incredible challenges.

He was an endangered species; the only thing that could make him more valuable is if he was albino. If I had any chance of keeping the Good Guy, I was going to start wearing clean clothes. Stop eating sugar and let my face clear up. I was probably going to have to cook. I was definitely going to have to shave. It looked like I might have to compromise on occasion.

Honestly, there was no chance that a girl like me, with all of her scratches and her dents, was going to be able to hang onto a guy like that, not even if I grew hawk-like talons which might take my nails up to a week to reach their full puncture-level maturity. I was not a shiny, gleaming firm Red Delicious or a fuzzy, blushing Georgia peach. My fruit was bruised and came with its own colony of Med flies.

I embarked on the only option open to me considering the limitations of my talents and skills. Plan A involved taking him to the bar and plying him with alcohol, keeping the man as inebriated and befuddled for as long as humanly possible. By the time he sobered up, it was time to send him off to work where he would be too consumed with dehydration and alcohol poisoning to realize there was a gap between my two front teeth. Or that they were slightly bucked, despite four years of relentless lying on my behalf when documenting the usage on my headgear chart. Or that they were the color of butter. Or that I had a mole under my lip, which by the time I reached middle age would be mistaken for an M&M and by the time I had gone gray and my ass was slapping the back of my knees when I walked, would effloresce into the size of a giant gumdrop, undoubtedly knocking down my nose in the to second place in the pecking order for the largest feature of my face.

Oh yeah. I had problems, all right, and they were about to get worse.

He mentioned that he wanted me to meet his family over the Christmas holiday, and that was when I felt the possibility of the love balloon deflate. What was I going to do then? How could I possibly intoxicate all of his kin, including the children? Nyquil would probably work for any of them in the featherweight category, but for the full-size adults, I'd have to inject commercial quality heroin into the Butterball. My cover would be blown, and I would be revealed for the day-old fruit that I was. Besides, I didn't want to meet his family so soon—we had only been dating for a couple of months, and frankly, that's not even enough time for a primate to bond with its mother, let alone try to get the Catch of the Century attached to me. I had visions of myself walking through the door and meeting his mother for the first time, as she looked at me as if she just saw me slide down a brass pole wearing nothing but a string of fake pearls.

So I was forced to stop getting my boyfriend drunk, which was probably a good thing, I figured, since sobriety may have given him the opportunity to learn my last name. I started trying to prepare myself for the family introduction, telling myself "How bad could it be? There's bound to be an introduction in the history of the world that had more horrific consequences, President Clinton and Monica Lewinsky, Angelo Buono and Kenneth Bianchi, Elton John and Bernie Taupin? Rush Limbaugh and a microphone?" I had miles to go before I reached that level of disaster, and time had come to call in my reinforcement talents now that I could no longer turn my boyfriend into a blithering alcoholic. Aside from getting a bartender's attention quickly and ordering drinks at the bar, I only had one talent left: frying cutlets.

Certainly, in some areas of the world, frying cutlets is a menial task, but in the land of the Italian-American- Catholic hierarchy, cutlet frying could easily take the place of beauty and could even forgive a sin as ugly as infertility, especially in a marriage-aged woman with an above average number of moles. Now, in this specific culture, frying a perfect cutlet, comparatively speaking, is equal to the ability of a woman of Germanic stock to plow a field by herself without even assistance from livestock, an English woman for keeping most of her teeth a variation of the color "pale", or the duty of a Mormon woman to pop out a baby every birthing season for a decade straight without missing even one year.

And it just so happens, I can fry a mean cutlet.

I'm sure it was no mistake, either. I'm nearly positive that when I was five and the baby freckle under my lip began to assert itself as a growth, my mother gasped, "Jesus, Mary and Joseph, when the time comes to marry her off, that thing will be the size of a brown Volkswagen. Egg, breadcrumbs, frying pan, Laurie! Egg, breadcrumbs, frying pan, pay attention!" If there had been a fry-off, I would have won it hands down before I even realized this was my only chance at love, but due to the fact that my parents had uprooted my sisters and me from our native Brooklyn to the desolate shit hole known as Phoenix, Arizona, my title as the Cutlet Queen tragically went uncrowned. There was no way my gift could be appreciated, let alone recognized in a land that called a dinner roll a "bagel." In hindsight, our neighbors were nice to us simply because they were afraid my Italian New Yorker father would, at any minute, start shaking down the block for protection money or insist on selling them fur coats in 118 degree weather that he said fell off a truck (though in Arizona, you'd say, "fell offer this here waggin"). After all, they believed we must have been related to the Gambino crime family because our last names ended with the very same letter.

Arizona was new territory to New York Italians, evidenced when, on our first day in our new desert home, the unafraid and impeccably tanned leader of the Welcome Wagon ladies brought over a pan of lasagna made of cottage cheese, Ragu and Velveeta. My mother promptly responded by running out to the front yard, waving her arms and screaming, trying frantically to flag down the disappearing Mayflower moving truck as it turned the corner and was gone forever.

But it was now apparent to me that my cutlet prowess had not been in vain; now was my time to shine in order to keep my boyfriend hooked. I pounded, I floured, I dipped. I fried. And I fried. And I fried. Veal cutlets. Beef cutlets. Chicken cutlets. If I could hit it with a hammer and it stayed still long enough for me to submerge it in an egg wash then bathe it in breadcrumbs, it became a cutlet. Soon, I didn't own a single piece of clothing that didn't bear the scars of an exploding oil bubble, my skin was covered with tiny red oil burns that looked disturbingly like the pox, and everything I owned became laminated with a thin, grimy sheen.

And my poor boyfriend, who had been raised on a steady diet of pressed meats and Dinty Moore stew, didn't have the first inclination of how to handle it.

"Wow, I never knew you could do this," he said the first time that I placed a pan of chicken parmesan in front of him, as he looked at me with a smile that said he thought I was a goddess. "I didn't know you could cook! You can cook! You never told me you could cook! I haven't had a home-cooked meal since the last time my mom made....toast....for our chopped ham sandwiches! This is incredible! Wow! You can cook!"

And then he gobbled the whole pan of chicken parmesan down like he was a hominid who didn't know if he would survive long enough for a next meal. It was simply beautiful. I had laid the cutlet trap, and the Good Guy had fallen head first into it.

When I felt that I had securely gotten him hooked on cutlets, that he was now a junkie with a hunger that no other woman could fix or satisfy, I stood above him as he ravaged a casserole dish of Veal Piccata.

"Look at this!" I yelled, pointing to my lip. "Look at this mole! Some day, especially if I'm exposed to enough radiation, this thing will be mammoth enough in size to require its own pillow at night! Do you understand that?"

"That's a mole?" he said, barely looking up. "I thought that was just a permanent smudge because you eat so much chocolate. I'm glad to know it's not a food particle, that's a relief!"

Then he wolfed down another piece of veal as a caper rolled from his chin.

I had dared the demon to show itself, and it had.

It just turned out that it was me.
```

---

## IC-2252: Got Spirit

- Title: Got Spirit
- Author (byline): Judy Budnitz
- Work: Flying Leap
- Publisher: Picador USA
- Publication date as stated: November 1998
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2090
- Already set (do not supply): none

### Source block (context only)

```text
Author: Judy Budnitz
Book: Flying Leap
ISBN: 978-0312198848
Publisher: Picador USA
Date (Month/Year): November 1998
```

### Introduction (context only: never use it for content warnings)

```text
Can you remember what your school years were like? In grade school it was all about reading time, coloring sheets, and recess. It was also about tests, report cards, and PTA meetings. As I got older school still involved tests, and report cards but it also involved school spirit and relationships. In the end, that is what makes going to school so exciting. It is friendships, and the bonds that develop over the years. It is having teachers that pour their hearts out into students, day after day. But some people have a different take on school spirit. For all you cheerleaders out there, pardon the stereotypes, but seriously sometimes the mentality gives you guys a bad rap, and who am I to stop the insanity?? Dedicated to the girls everyone loves to hate . . . I’ve got spirit, Yes I do, I’ve got spirit how about . . . . Got Spirit by Judy Budnitz
```

### Performance text (classify this)

```text
Cheerleading, for the true believer, is no extracurricular activity. It is a vocation, a calling. I myself received the call when I was a mere novice, a member of the junior varsity drill team. It was the first football game of the season, third quarter. The score was tied and the tension mounting. Our boys were looking haggard. The spectators murmured softly in their seats. Someone in the stands tossed a cigarette onto the field and it sparked the dry grass on the sidelines. I watched the blaze, and that was when the vision came to me. I stared into those flames, and I heard a voice. It sounded like the voice of the announcer who called the plays over the loudspeakers, but I swear to you it was not. It was the voice of the Spirit. School Spirit. It called my name. It told me to take up the pompoms and megaphone and bring my message to the people. I was filled with ecstasy. The manager's assistant doused the fire with Gatorade and the game continued. But I knew what I had to do.

I immediately turned in my drill team uniform and tried out for the varsity cheerleading squad. My ascension was swift. I acquired the short skirts, the tight sweaters. I visited a tanning salon three days a week, I had my teeth bleached. I began at the bottom of the ranks but progressed quickly. Soon I was elevated to the second, and then the third tier of the pyramid formations. I learned the jumps, the cheers, the ritual of the pep rally.

During that first season, I came to know the thrill of leading the masses. We regularly incited a stadium full of fans to madness and hysteria. "Let's go, Westside, let's go!" we would chant, and they would repeat the mantra in one voice. I experienced the euphoria of victory, felt my heart catch at the sight of the blazing scoreboard; and I knew, too, the despair of defeat

I gracefully accepted my new social responsibilities. I confined myself to dating varsity players with scholarship prospects. I bonded with my sisters. We had our own table in the school cafeteria. We held bathroom conferences, skipped class to watch soap operas, waxed one another's legs,

We spent our summers at cheerleading camp, practicing back handsprings, whip-backs, and slingshots (in both tucked and pike position). During our quieter moments we composed new cheers, heartfelt little haikus full of tender sentiments, which we would later screech at the tops of our lungs to the enthusiastic masses.

Those were the heady, early days of my cheerleading career. I felt invincible. My life had purpose and meaning. My skin was clear.

We practiced two hours a day, followed by an hour of step aerobics or the Buns of Steel video. Our stunts were flawless. Our united voices could set off car alarms. I could feel the great Spirit walking among us.

Then came the fall.

Things started to unravel in September. Right at the start of the new football season we lost three cheerleaders in a stunt gone bad. None of us knew what really went wrong. No one on the squad is a genius at physics. Suffice it to say that at the first game of the season, we were doing a three-level "Eiffel Tower" human pyramid and there was a weakness somewhere in the structure. No one pointed fingers, but we all had our suspicions. I myself thought Staci looked a bit wiggy that day. School spirit was no match for the forces of gravity. The pyramid fell, bodies tumbled and rolled; several uniforms were irreparably damaged. We lost Bibi and Gwennie and Cat that night.

It was a tragedy, certainly, but we couldn't afford to linger over it; we had to think about the future. We did not want to lose our momentum. We needed replacements immediately. We were forced to hold emergency tryouts. Plenty of eager hopefuls showed up, but our standards were very exacting, and we feared none of the girls would measure up.

Sadly, we were right.

One of the girls who tried out was a member the U.S. national gymnastics team. Corrie could do a great tumbling routine, of course, but her problem was that she just wasn't happy enough. She was a solemn girl with big circles under her eyes. When she performed the classic cheer "I've got spirit, yes I do, I've got spirit, how 'bout you?' none of us felt for a second that she really had spirit.

We'd all seen Corrie on television during the Olympics, sobbing because she won the silver medal instead of the gold. This was a double liability. First of all, we didn't want anyone on the squad who would cry on national TV; didn't she have any dignity? we asked one another. Second of all, there was the matter of that silver medal. Why not the gold? She'd really let down her team. Let down the whole country. We didn't want a loser like that on our squad. For God's sake.

Corrie looked terrified all during the tryouts, and she recited the cheers in a squeaky, strangled voice, as if her gymnastics coaches had snipped her vocal cords to make her neck a little more flexible. And her body was wrong. She was definitely thin enough, but she had no chest at all. You need something there, it's what people like to see. A little jiggle. You can't hold their attention otherwise.

When Bunny and I tried to explain these shortcomings to her, Corrie started to cry more of those big Olympic-sized tears and said that she couldn't help it. We told her she should have considered implants; lots of girls do it before tryouts. There's no shame in it. As long as you don't tell anyone. If word does get out, your social life is finished. We told her we were sorry.

We had high hopes for another prospect. Her name was Mei-Ii and she almost passed muster. Nice legs, great smile, good straight teeth. Excellent posture. She seemed to have the spirit in her. We were preparing to take her when it came to our attention that she was not a natural blonde. When confronted, Mei-li tried to defend herself by saying she was Korean. That's no excuse, we told her. There are rules.

It was unfortunate; we would have accepted her if we hadn't noticed the telltale dark roots. Even then, some of us were willing to let it slide, but Bunny declared Mel-li unacceptable. No bottle-blondes, that was the rule. Bunny was a real stickler; it could cause difficulties at times, but we all had to admire her fervor.

We were very excited about a third applicant, LaShonda. LaShonda had style. She had the moves. She had grace and panache. She looked fantastic in the uniform. She was unexpectedly strong; we were eager to use her as the base of our human pyramids. She said she was dating a twenty-six-year-old, which pleased us; it meant we wouldn't have to worry about her stealing our boyfriends. You can imagine our disappointment, then, when we discovered that LaShonda was really Sean, and had until recently been the star kicker on the football team. We questioned LaShonda, who burst into tears and swore she was on a waiting list for an operation. We hugged her, some of us cried, too, but we had to tell her no.

"Oh my God, my life is over," LaShonda told us, sobbing into her hands. But Bunny was firm. We had standards to uphold, after all. If we started making compromises, exceptions, then everything would fall apart. Without rules, society would quickly disintegrate and soon we'd all be living in the wilderness, eating rats and beetles, peeing on the ground and wearing stripes with plaids. At least this was Bunny's reasoning, and it seemed sound to the rest of us.

So when we learned of LaShonda's suicide a short time later, none of us felt particularly responsible. Some of us rationalized it as a sacrifice of the one for the sake of many. I admit I felt a bit sad at the time, and considered dedicating a cheer to her at the next game, but I had so much on my mind that I forgot all about it.

We eventually accepted three girls who managed to meet all our qualifications. Nikki, Sherri, and Tonya were thrilled. big game.

We thought our troubles were over. We hoped the Spirit would return, now that our squad was complete.

During this time, too, Bunny began her campaign to change the school's mascot. She had chosen the phoenix as our new symbol and filled the school hallways with banners and posters depicting the mythic bird. Her reasons were vague; everyone assumed she was simply caught up in the thrill of the winning season.

The local television stations began broadcasting our games; Bunny smiled fiercely for the cameras, light glaring off her teeth.

I sensed I was being excluded from something; my sisters whispered behind my back. I tried to attribute my uneasiness to the season: It was late autumn, cool and crisp, the dusk began at four o'clock and seemed to last for hours, a mysterious time with the trees like black silhouettes in the dying light; then a purple sky, a prickle of stars, and the voluptuous sighing of mourning doves.

Homecoming approached. The evening before the Homecoming game we held the annual bonfire on the playing field behind the school. The football team set up a huge pyre of old railroad ties and newspapers, then lit it.

It was twilight, that electric, dusky time. Darkness crept around the edges of the field as the flames shot upward. Nearly all of the students and teachers were there. They stood with dazed looks on their faces, hushed and awed by the blaze. The band blared out the school anthem, repeating the chorus over and over. My sisters and I turned cartwheels, and I was filled with hope and serenity. All those people, united in a common purpose. And they were watching me. I felt the old thrill. I had veered away from the others. I turned another cartwheel, then another cartwheel, and another, and then I stopped and faced the fire. I heard a piercing noise and spun around to look. It was the squad.

The cheerleaders. My sister cheerleaders. They were cheering. Without me. They were dousing themselves in gasoline, marching into the fire in their flammable polyester uniforms. They were screaming for the Westside Phoenixes, ghastly smiles on their faces as their hairspray ignited; they lifted their arms in final salutes, windmills, Russians, whip-kicks. "We got spirit!" I heard, and "Victory tonight!" and "Let's go, Westside!" And then they were gone.

Afterward everyone asked me why I didn't join them. The truth is that I hadn't heard the call. Maybe I wasn't ready yet. But most people wouldn't understand that, so I just told them I'd pulled a tendon doing that last cartwheel, and I couldn't make it to the fire in time.

The team won the Homecoming game and went on to win the state championship. At first I tried to lead cheers at the games, alone, but somehow it just didn't feel right.

Westside never did officially change its mascot as Bunny had wanted. We kept the same mascot we've always had. The lemming.

I got back together with my boyfriend. "I hope you're not going to get fat now that you're not doing the cheerleading," he said. But he seems happy enough to have me. After all, I'm the only pretty girl left in the school.

Also I've been spending a lot of time talking to my dad. He's been encouraging me to apply to colleges.

I think this is mainly because he wants to get me out of the house as soon as possible. I seem to make him nervous, for some reason.

"There are plenty of colleges out there for a girl like you," he told me. "Take your pick."

I said, "I'm glad the other girls are gone; now I won't have to compete with them for the best collegiate cheerleading programs."

My dad patted my knee. He laughed, and then he shook his head and said, "Sweetie, you are living proof that ruthlessness and stupidity are not mutually exclusive."

I'm not sure what he meant by that. But I have ways of making him tell me.
```

---

## IC-2253: Handle With Care

- Title: Handle With Care
- Author (byline): Jodi Picoult
- Work: Not specified
- Publisher: Washington Square Press
- Publication date as stated: September 2009
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1859
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jodi Picoult
ISBN: 978-0743296427
Publisher: Washington Square Press
Date (Month/Year): September 2009
```

### Introduction (context only: never use it for content warnings)

```text
How far would you go to care for the ones you love? In the following selection, Willow O’Keefe is a little girl who has Type III osteogenesis imperfecta, also known as brittle bone syndrome. Her parents, Sean and Charlotte, have spent most of her life with sleepless nights, hospital bills, and stares from other parents who are luckier than they are. After going to Disney World, where Willow suffers a serious bone break, Sean and Charlotte decide to file a lawsuit against the park and the hospital, but it suddenly turns into a wrongful birth lawsuit against the OB/GYN who treated Charlotte during her pregnancy. The parents must testify that if they knew before birth that Willow had this disease, they would have aborted her. Told through the eyes of Charlotte, Willow’s mother; and Amelia, Willow’s sister, the trial takes a toll on their entire family. Handle With Care by Jodi Picoult.
```

### Performance text (classify this)

```text
Charlotte (Mom): (Pg 403) The movie that had been filmed to show a day in your life was the last bit of evidence that Marin would offer to the jury. It was the emotional counterpart to the cold, hard facts the actuary had given, about what it costs in this country to have a disabled child. It began with an image of your face, reflected in the windowpane you were peering through. You weren’t speaking, but you didn’t have to. There was a lifetime of longing in your eyes. The view panned out the window, then, to watch your sister skating on the pond.

Amelia (Sister): (Pg 17) I [can] imagine our parents saying, There Amelia goes, being difficult again. (Pg 18-19) Pick ten strangers and stick them in a room, and ask them which one of us they feel sorrier for – you or me – and we all know who they’ll choose. It’s kind of hard to look past your casts; and the fact that you’re the size of a two-year-old, even though you’re five. I’m not saying that you’ve had it easy. It’s just that I have it worse, because every time I think my life sucks, I look at you and hate myself even more for thinking my life sucks in the first place. Here’s a snapshot of what it’s like to be me: Amelia, don’t jump on the bed, you’ll hurt Willow. Amelia, how many times have I told you not to leave your socks on the floor, because Willow could trip over them? Amelia, turn off the TV (although I’ve only watched a half hour, and you’ve been staring at it like a zombie for five hours straight). I know how selfish this makes me sound, but then again, knowing something’s true doesn’t keep you from feeling it. Charlotte (Mom): [The lawyer continued talking to Sean and me.]

Marin (Attorney): (Pg 64) I know how horrible this sounds. But the term wrongful birth is just a legal one. We don’t wish your child wasn’t born. We just think that, when a doctor doesn’t meet the standard of care a patient deserves, someone ought to be held responsible. Think of all the time and money that’s gone into taking care of Willow – and will go into taking care of her in the future. Why should you pay for someone else’s mistake? Charlotte (Mom): (Pg 60) What if it was someone’s fault? For five years now I had loved you, hovered over you, held you when you had a break. So how could I admit to anyone – much less myself- that you were not only the most wonderful thing that had ever happened to me . . . but also the most exhausting, the most overwhelming?

Marin (Attorney): (Pg 91) If you file this lawsuit, you have to be able to swear – under oath – that if you’d known about your daughter’s illness earlier, if you’d been given the choice, you would have terminated the pregnancy. Is that going to be a problem?

Charlotte (Mom): Can you miss a person you’ve never known? Amelia (Sister): (Pg 121) The last time my parents had been fighting – which was, like, yesterday – you and I were in our bedroom, and we could hear them loud and clear. Words slipped under the door, even though it was closed: wrongful birth… testimony… deposition. At one point I heard the mention of television: Don’t you think reporters would get wind of this? Is that what you really want? and for a moment I thought how cool it would be to be on the news, until I remembered that being a poster child for dysfunctional family life wasn’t really how I wanted to spend my fifteen minutes of fame. They’re mad at me, you said. No. They’re mad at each other.

Then we both heard Dad say, Do you really think Willow wouldn’t figure this out? You looked at me. Figure what out?

Charlotte (Mom): (Pg 71) Sean was the risk taker when it came to you. Then again, he wasn’t the one who was home most often when you had a break. Maybe I could convince him that two silly words like wrongful birth meant nothing when compared to the future they might secure for you. (Pg 104) It’s because we want her, because we love her, that I’d ever think about this in the first place. I’m not stupid, Sean. I know people are going to talk, and say I’m after a big settlement. They’re going to think I’m the worst mother in the world, the most selfish. But I don’t care what they say about me – I care about Willow. I want to know that she’ll be able to go to college and live on her own and do everything she dreams of. Does it really matter what everyone else says if I know why I’m doing it?”

Willow: (Pg 193) (whispering) You know how Mom always says that I can be anything when I grow up? That’s a lie.

Amelia: Why?

Willow: I couldn’t be a boy. And I couldn’t be Miss America.

Amelia: How come?

Willow: You can’t wear leg braces in a pageant. Amelia: (to audience) I thought about those pageants, girls too beautiful to be real, tall and thin and plastic-perfect. And then I thought of you, short and stubby and twisted, like a root growing wrong from the trunk of a tree, with a banner draped across your chest. MISS UNDERSTOOD. MISS INFORMED. MISS TAKE.

That made my stomach hurt.

Charlotte (Mom): [This is what I tell the jury.] (Pg 359-360) I know what I look like to all of you. I know you think I’m in this for a big payday, that this is why I started this lawsuit. It is about cost. But not the financial kind. I don’t sleep at night. (blinking back tears) I don’t sleep at night. I feel guilty when I laugh at a joke on TV. I watch little girls the same age as Willow at the playground, and I hate them sometimes – that’s how bitterly jealous I can get when I see how easy it is for them. I made a promise to my daughter – I said, If you fight, I will, too. If you live, I will make sure your life is the best it can possibly be. That’s what a good mother does, right? (Shakes her head) The way it usually works, the parent takes care of the child, until years later, when the roles are reversed. But with Willow and me, I’ll always be the one taking care of her. That’s why I’m here today. That’s what I want you to tell me. How am I supposed to take care of my daughter after I’m gone?

Willow: (Pg 320-321) (wiping tears from her eyes) Mom wants to get rid of me because [I keep breaking]. I’m not the kind of kid anyone wants.

Amelia: What are you talking about? It’s not like you’re a serial killer. You don’t torture chipmunks or do anything revolting, except try to burp ‘God Bless America’ at the dinner table-

Willow: I only did that once. But think about it, Amelia. Nobody keeps things that get broken. Sooner or later, they get thrown away.

Amelia: Willow, you are not being sent off, believe me. And if you are, I’ll run away with you first.

Charlotte (Mom): (Pg 442) [Amelia] asked me not too long ago what the world would be like without Willow in it. So here’s what I think: if Willow had never been born, I’d still look for her in the aisles of the grocery store, or at the bank, or in the bowling alley. I’d stare at every individual face in a crowd, trying to find hers. There’s this weird part about having kids – you know when your family is finished, and when it’s not. If Willow hadn’t been born, that’s how the world would be for me – unfinished.

Amelia (Sister): (Pg 455) We all protected you, in our own ways. Dad blustered around, angry at anything that made life harder for you. Mom, well, she was apparently stupid enough to gamble everything in order to get more for you in the long run. And me, I guess I just lacquered a shell around myself, so that when you got hurt, it was easier to pretend I didn’t feel it, too.

Charlotte (Mother): [The day the jury reached its verdict, I told] (Pg 465) you that this was finally over. I [told] you that you’d have everything you needed, for the rest of your life – and after mine ended. I [told] you that I had won, and that the verdict award[ed] damages in the amount of eight million dollars.

Willow: (Pg 469) Eight million is the number of dollars written on the big blue check that has been on our refrigerator for almost six months now. (Pg 471) My parents had never cashed the check. A lot of zeros didn’t mean anything really, except security – my parents could splurge a little, because if their funds ran out, there was a backup.

Charlotte (Mom): Tell you wat. Go get Amelia and we’ll figure out a plan of action. A movie, maybe. Be . . .

Willow: . . . careful. Yeah, I know. It was March, but still cold enough the ground still crunched under the soles of my boots. Amelia was probably in the woods . . . I hesitated as I came to the edge of the pond. (Pg 472) Right now, for the first time in months, I had no healing fractures, and I planned to keep it that way. I’d never been allowed on the ice, and like most things that you aren’t allowed to do, it was all I thought about. I got down carefully on my hands and knees, and inched forward. I couldn’t get hurt this way. [Then] there was a moan rippled across the surface of the pond. Suddenly, all around me, the ice became a spiderweb and I was the bug stuck at its center. As the water filled my nose and mouth, I closed my eyes and curled my fists around the things I knew for sure: That I was loved and that this time, it was not me who broke.

Charlotte (Mom): (Pg 475) For a long time, I could only see you sinking. I pictured you, with your skin pale blue and your hair streaming out behind you like a mermaid’s. I would wake up screaming, beating the mattress with my hands, as if I could reach through the ice and drag you to safety. . . I do not have the money anymore. It was yours, after all. I slipped the check into the silk lining of the coffin when I kissed you good-bye for the last time. But that wasn’t you, no more than the skeleton you’d been given was you. You were more than that, lighter. You were the steam that fogged the mirror in the morning when Sean dragged me out of bed and forced me to take a shower. You were the crystals painting my car windshield after a night’s frost. You were the heat rising off the pavement like a ghost in the middle of the summer. You never left me. Here are the things I know for sure: • When you think you’re right, you are most likely wrong. • Things that break – be they bones, hearts, or promises – can be put back together but will never really be whole. • And, in spite of what I said, you can miss a person you’ve never known. • I learn this over and over again, every day I spend without you.
```

---

## IC-2254: Hannah’s Gift

- Title: Hannah’s Gift
- Author (byline): Maria Housden
- Work: Not specified
- Publisher: Bantam Books
- Publication date as stated: July 2003
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: MARIA, HANNAH, DOCTOR, CINDERELLA, SOCIAL WORKER, CHILD
- Teaser before the introduction: Yes
- Spoken words (computed): 1263
- Already set (do not supply): none

### Source block (context only)

```text
Author: Maria Housden
ISBN: 978-0553381221
Publisher: Bantam Books
Date (Month/Year): July 2003
```

### Introduction (context only: never use it for content warnings)

```text
According to St. Baldrick’s Foundation, one in 285 children in the United States will be diagnosed with cancer before age 20. These children are true gifts. They have no interest in being victims. They change the lives of everyone they touch with their bravery, strength, compassion, optimism, and willpower. This is . . .

Hannah’s Gift by Maria Housden
```

### Performance text (classify this)

```text
MARIA: (Prologue) Looking back, I realize that my whole life pivots around a single moment: The Red Shoes. I was standing in a Stride-Rite children’s shoe store. Black or blue leather would coordinate with every outfit in Hannah’s preschool wardrobe. [But] Hannah had already decided . . . [she was] holding up a pair of red patent leather Mary Janes.

HANNAH: These are my shoes! (slipping her feet into the shoes)

MARIA: (smiling patiently) Those are lovely, but we need to buy something practical that will match the dresses in your closet.

HANNAH: But Mommy, red shoes go with everything. Besides . . . they fit me just perfect!!! (whispering) Just like Cinderella!

MARIA: Closing her eyes and extending her arms, Hannah began to dance, oblivious to everything but the shoes on her feet. (Beat) (Beyond Fear) The two of us were crossing the parking lot. Her red shoes tapped on the pavement as she walked beside me.

HANNAH: Mommy, do children ever die?

MARIA: I paused before answering. I wished I could tell her that children didn’t die. But I knew that wasn’t the truth, and I knew Hannah knew it too. (to Hannah) Yes, Hannah, sometimes children die.

MARIA: (Light in the Shadow) [It began] during our vacation in Michigan. We had taken Hannah to an emergency room. She had been complaining that it hurt to lie down. The doctor told us she had the flu and sent us away with Children’s Tylenol. Two days later, we took her to another hospital. The pediatrician tried to examine her abdomen but she screamed and refused to lie down and the doctor gave up, obviously exasperated.

DOCTOR: There’s nothing wrong with her; she’s just manipulating you. She has too much energy to be really sick. As far as I can see, she’s fine.

MARIA: Every bone in my body was telling me something was wrong, and yet, perhaps the doctor was right. Maybe I was just the inadequate mother of an overindulged child. (Beat) Now, [a third] doctor . . . He came into the room, flipped the switch on the light board, and slid the film under the clip. [There was] a large, dark shadow beneath the white outline of Hannah’s ribs. I felt like a profound failure.

DOCTOR: (A Deeper Silence) It’s called a Rhabdoid tumor of the kidney. It’s malignant, aggressive and rare.

MARIA: (Truth: A Special Medicine) The weight of the moment crushed against my chest. (to Hannah) Hannah, the doctors have figured out why you are feeling so sick. There is a lump in your tummy called a tumor. The doctors are going to take it out, and then give you medicines to try to make sure the bad cells don’t come back. (Beat) (Magic) A week after Hannah’s second surgery, and as a Make-A-Wish kid, Hannah qualified for an all-expenses-paid trip to Walt Disney World. Hannah performed two somersaults in the middle of the floor to celebrate. Cinderella’s castle was our first stop.

CINDERELLA: Hello, I’m Cinderella. What’s your name?

HANNAH: (in awe) My name’s Hannah. (quietly) I just had surgery. Do you want to see my scar? (She raises her dress)

CINDERELLA: (looking at Hanna’s scar, she then opens her arms wide to hug the little girl) Thank you for sharing that with me, Hannah.

MARIA: As she held Hannah, she looked at me, her eyes full of tears. It didn’t matter that Cinderella was a girl from Iowa. The joy we experienced in the meeting was real, and that was magic enough for me. (Beat) (Anticipation) Since the day Dr. Kamalaker told us Hannah had cancer, I had begun living the paradox of wanting to do anything to find a cure and needing to preserve the quality of time Hannah had left. I agreed to try the chemotherapy protocol once a week at the outpatient clinic.

SOCIAL WORKER: You realize that chemotherapy will severely compromise Hannah’s immune system. Preschool is definitely out of the question.

MARIA: I knew it was true. But to me, Hannah was a three-year-old first, and a caner patient second. (to the Social Worker) You don’t understand. After everything Hannah’s been through, I won’t take preschool away from her. She wants to ride on a bus and go on field trips with her friends. I’m willing to do anything to make that happen. (to audience) Hannah started preschool the week after her third birthday. (Nurse Katie and the Tea Party) Her friends exclaimed over her dress [and red shoes] and hardly seemed to notice the paper hospital mask or her lack of hair. (Beat) (Hannah’s Birthday) Soon it was Hanna’s birthday. When I asked how she wanted to celebrate the day she said:

HANNAH: I want a party with a Little Mermaid cake, not too much people and not too much gifts!

MARIA: The children had greeted Hannah shyly, tentatively. It was clear they had been reminded just before coming that Hannah had had surgery [again] and might still feel sick. Hannah had been the one to step into the moment and set us all straight.

HANNAH: Hey, you guys, do you want to see my scar? It’s just surgery! (she lifts the hem of her dress and, exclaims enthusiastically) My doctors gave me medicine and pizza!

CHILD: Ooooo . . . Ahhh . . . Wow! I want to have surgery! (pause) Can you still play?

HANNAH: Of course, you silly. This is a party, isn’t it?

MARIA: One of the mothers turned to me and whispered, “Is this okay with you?” And I smiled and shrugged. If it’s okay with her, it’s okay with me. (long beat) (Say Yes) [But] Less than a week after Easter, Dr. Kamalaker slid a piece of film under the clip of a lightboard and pointed to the spot where the cancer had metastasized. In a different place this time. Very close to Hannah’s spinal cord and wrapped around some very important veins. The doctors can’t take this one out. (On the Threshold) As Hannah’s tumor grew, so did the amount of morphine she required.

HANNAH: Mommy, I want you to carry me to my room

MARIA: It was the first time in days she had asked to go anywhere other than the bathroom.

HANNAH: Don’t put me down and don’t go it. I just want to look.

MARIA: The two of us stood on the threshold, watching dust dance in the late afternoon sun. The magic wand she had made at her birthday party almost a year ago lay in the middle of the floor. I wanted to wave it through the hush and bring everything back to life. (beat) I knew Hannah was saying good-bye, but I wasn’t ready. This room with its Barbie dolls and red patent leather shoes was Hannah. If I were to say good-bye to this, what part of her would be left? (long beat) (Everywhere I Am, There You’ll Be) Hannah hadn’t eaten more than a bite or two of solid food for almost a week. I was sitting at the foot of the bed, early in the day, when Hanna stirred and sat up slowly.

HANNAH: (wincing then smiling) Mommy, do you know that even if I go to Heaven, I’m going to come back?

(deep moan of pain)

MARIA: Yes, Hannah, I know.

HANNAH: (deep moan of pain)

MARIA: (Silence) I jumped up, checking the morphine pump to make sure nothing had malfunctioned. Something had drastically changed. I decided to pick her up, not knowing what else to do. Hannah’s body continued to fight for twenty minutes, but some part of her already felt free. One moment she was alive and breathing; the next, she wasn’t. (beat) (Prologue) The truest measure of a life is not its length, but the fullness in which it is lived. (Everywhere I Am, There You’ll Be) In that instant I knew that, no matter what happened, there was a part of Hannah that would always be with me, something of her that would never die. It wasn’t a belief. It wasn’t a hope. It was a knowing beyond the workings of my mind. (beat) I closed my eyes for a moment. And there, behind my eyelids, I saw something I could hardly believe: It was Hannah . . . radiant . . . laughing (Prologue) in red patent leather shoes. Closing her eyes and extending her arms, Hannah began to dance. May her story offer solace to those who suffer and inspiration to those who want the courage to live their own truth.
```

---

## IC-2255: The Hiding Place

- Title: The Hiding Place
- Author (byline): Corrie ten Boom
- Work: Not specified
- Publisher: Chosen Books
- Publication date as stated: Jan 2006
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: CORRIE, FATHER, WOMAN, PASTOR, MR. SMIT, JEWS, SOLDIER, MEDICAL MAN, PRISON MATRON, PRISONER, PRISONERS, GUARD
- Teaser before the introduction: Yes
- Spoken words (computed): 2036
- Already set (do not supply): none

### Source block (context only)

```text
Author: Corrie ten Boom
ISBN: 978-0800794057
Publisher: Chosen Books
Date (Month/Year): Jan 2006
```

### Introduction (context only: never use it for content warnings)

```text
They didn’t have to wait long. . . In this true story, 50-year-old Corrie Ten Boom and her 80-year-old father open their home to Jews who are hiding from Hitler’s Gestapo. The Ten Booms were not Jews themselves, but Christians – Christians committed to caring for the needs of others, no matter what the cost.

The Hiding Place by Corrie ten Boom
```

### Performance text (classify this)

```text
CORRIE: (Pg 82-83) The true horror of Nazi occupation came over us only slowly. During the first year of German rule there were only minor attacks on Jews in Holland. A rock through the window of a Jewish-owned store. An ugly word scrawled on the wall of a synagogue.

[But over time], Father and I saw the symptoms spread. A sign in a shop window: JEWS WILL NOT BE SERVED. At the entrance to a public park: NO JEWS. On the door of the library. In front of restaurants, theaters, even the concert hall.

Worst were the disappearances. We never knew whether our Jewish friends had been spirited away by the Gestapo or gone into hiding. Public arrests, with no attempt to conceal what was happening, were becoming more frequent. One day as Father and I were returning from our walk, we found a truck parked in front of the fish mart; into the back were climbing men, women and children, all wearing the yellow star. “Father! Those poor people!”

FATHER: Those poor people. I pity the poor Germans, Corrie. They have touched the Jews: the apple of God’s eye.

CORRIE: We talked often, Father, [my sister] Betsie and I, about what we could do if a chance should come to help some of our Jewish friends.

WOMAN: (Pg 91) (Knock on door) Can I come in? (voice is high-pitched in fear)

CORRIE: Of course. (steps back)

WOMAN: (Looks over her shoulder) My name is Kleermaker. I’m a Jew.

CORRIE: (Pg 92) Just two nights later the same scene was repeated. Again there was a furtive knock at the side door. This time an elderly couple was standing outside. It was the same story: the same tight-clutched possessions, the same fearful glance. The story of neighbors arrested, the fear that tomorrow their turn would come. (Pg 96) Still the hunted people kept coming, and the needs were often more complicated. If a Jewish woman became pregnant, where could she go to have her baby? If a Jew in hiding dies, how could he be buried?

(Pg 97) We were friends with half of Haarlem! We knew nurses and clerks in the Records office. We knew someone in every business and service in the city.

CORRIE: (Pg 112-113) Good morning, Pastor. Would you be willing to take a Jewish mother and her baby into your home? They will almost certainly be arrested otherwise.

PASTOR: (Takes a step back. Color drains from his face) Miss Ten Boom! I do hope you’re not involved with any of this illegal concealment and undercover business. It’s just not safe! Think of your father! And your sister!

CORRIE: On impulse I told the pastor to wait and ran upstairs. I asked the mother’s permission to borrow the infant. Back in the dining room, I pulled the coverlet from the baby’s face.

PASTOR: (Long silence. He bends forward, his hand reaching for the tiny fist. Compassion and fear struggle on his face. Then he straightens) No. Definitely not. We could lose our lives for that Jewish child!

CORRIE: Unseen by either of us, Father had appeared in the doorway.

FATHER: Give the child to me, Corrie. (Holds the baby close, brushing his beard against the child’s check. Looks at the pastor) You say we could lose our lives for this child. I would consider that the greatest honor that could come to my family.

CORRIE: (Pg 99-102) [In time] one of the most famous architects in Europe; I knew him only as Mr. Smit, paid us a visit.

MR. SMIT: Your building lacks a secret room. This is a danger for all, those you are helping as well as yourselves.

CORRIE: He started up the narrow corkscrew stairs. At last, at the very top of the stairs, he entered my room.

MR. SMIT: You want your hiding place as high as possible. Gives you the best chance to reach it while the search is on below. This is it!

CORRIE: Over the next few days the false wall was up; 30 inches from the back wall. Even I who had lived half a century in this room could scarcely believe was not the original. And in the far lefthand corner, a sliding panel, two feet high and two wide, opened into the secret room.

MR. SMIT: The Gestapo could search for a year. They’ll never find this one! (Pg 118) A raid may come any day. Your secret room is no good to you if people can’t get to it in time. Put a buzzer in every room with a door or a window on the street. Then hold practice drills until your people can disappear in that room without a trace in less than a minute.

CORRIE: [We] installed a buzzer near the top of the stairs – loud enough to be heard all over the house but not outside. Buttons were placed to sound the buzzer at every vantage point where trouble might first be spotted. A Mr. Smit arrived one morning to teach me how to conduct the drills.

MR. SMIT: (Pg 119) Mealtimes. hat’s the favorite hour for a raid. Also the middle of the night. (Walks from room to room, pointing to evidence) Watch for evidence that more than three people live in the house. Wastebaskets and ashtrays. If the raid comes at night, they must not only take their sheets and blankets, but get the mattress turned. That’s the S.D.’s (Security Police’s) favorite trick – feeling for a warm spot on a bed.

CORRIE: (Buzzer) Mr. Smit pushed the button. People sprang to their feet, snatching up glasses and plates, scrambling for the stairs.

JEWS: Faster! Not so loud! You’re spilling it!

CORRIE: (Pg 120) The whole process had taken four minutes. A little later we were all gathered again around the dining room table. Mr. Smit set before him the incriminating evidence he had found: two spoons and a piece of carrot on the stairs, pipe ashes in an “unoccupied” bedroom.

The next night I sounded the alarm again and this time we shaved a minute thirty-three seconds off our run. By our fifth trial, we were down to two minutes.

(Pg 139) It was the morning of February 28, 1944. For two days I had been in bed with influenza. (Pg 141) In my fevered dream a buzzer kept ringing. On and on it went. Why wouldn’t it stop? Feet were running, voices whispering: “Hurry! Hurry!”

I sat bolt upright. People were running past my bed. I turned just in time to see [someone’s] heels disappear through the secret panel.

But . . . I hadn’t planned a drill for today! Who in the world – unless – unless it wasn’t a drill. (Pg 142) I dropped the panel down and pushed by prison bag up against it. I had just reached the bed when the door flew open.

SOLDIER: What’s your name?

CORRIE: What? (Corrie sits up slowly and sleepily)

SOLDIER: Your name!

CORRIE: Cornelia Ten Boom

SOLDIER: (Turns and shouts down the stairs) We’ve got one more up here. (Turns back to Corrie) Get up! Get dressed! (Takes a slip of paper from his pocket and consults it. Looks at Corrie with new interest) So you’re the ring leader. Tell me now, where are you hiding the Jews?

CORRIE: I don’t know what you’re talking about.

SOLDIER: (Pg 144) (striking her across the face) Where is your secret room?

CORRIE: Lord Jesus, protect me!

SOLDIER: (raises his hand to strike again, but then stopes) If you say that name again I’ll kill you.

CORRIE: (Pg 143) It was the hardest thing I had ever done to turn and walk out of that room. The man behind me gave me a push and I hurried down the stairs to the dining room. Father and Betsie were sitting on chairs against the wall. (Pg 147) I would not let myself think about the secret room and the six people [the hiding place] upstairs.

(Pg 149-150) In the Smedestraat a wall of people pressed against police barricades set across the street. As Betsie and I stepped out with Father between us, a murmur of horror greeted the sight of “Haarlem’s Grand Old Man” being led to prison. In front of the door stood a green city bus with soldiers occupying the rear seats. Father, Betsie, and I squeezed into a double seat near the front.

(Pg 153) The truck had no springs and bounced roughly over the bomb-pitted streets. I slipped my arm behind Father’s back to keep him from striking the edge. The truck jerked to a halt. Behind us massive gates clanged shut.

SOLDIER: (Pg 154) Women prisoners follow me!

CORRIE: Father! God be with you!

FATHER: And with you, my daughters.

CORRIE: I turned and followed the others. Behind me the door slammed closed. Oh Father, when will I see you next?

(Pg 161) We were heading deep into the maze of prison passageways. Without a word, the prison matron halted in front of a door and opened it with a key. I stepped inside. The door clanged behind me. The bolt slammed shut. Alone. Alone behind these walls . . . I must not let my thoughts run wildly; I must be very mature and very practical. Six steps. Sit down on the cot. It reeked; the straw seemed to be fermenting. I reached for the blanket: someone had been sick on it. I thrust it away, but it was too late. (Turn back to audience. Dry heaves)

What had I done to be separated from people this way? Maybe my sentence was solitary confinement for years and years . . .

(Pg 162) The door opened once a day to let in a man from Medical Supply with some stinging yellow liquid from a very dirty bottle. Please! (raspy voice; clutching at his sleeve) Have you seen an 84-year old man – white hair, a long beard? Casper Ten Boom! You must have taken medicine to him!

MEDICAL MAN: (Tugging loose) I don’t know! I don’t know anything!

CORRIE: The cell door slammed back against the wall.

PRISON MATRON: Solitary prisoners are not permitted to talk!

CORRIE: (Pg 164) It seemed to me strangely important not to lose track of time. I scratched a calendar on the wall behind the cot. As each long featureless day crawled to a close, I checked off another square. I also started a record of special dates beneath the calendar: February 28, 1944 Arrest February 29, 1944 Transport to Scheveningen March 16, 1944 Beginning of Solitary

(Pg 166) One evening as I was crossing another long, long day from the calendar scratched on my wall, I heard shouts far down the corridor. They were answered closer by. Now noisy voices came from every direction. Names were being passed from cell to cell. People were singing, others pounding on their doors. The guards must all be away!

CORRIE: What’s happening? Where are the guards?

(Crying out through the open slot)

PRISONER: At a party. It’s Hitler’s birthday.

CORRIE: Then – these must be their own names people were shouting down the corridor. This was our chance to tell where we were, to get information. I’m Corrie Ten Boom! My whole family is here somewhere! Oh, has anyone seen Casper Ten Boom! Betsie Ten Boom! I shouted names until I was hoarse and heard them repeated from mouth to mouth down the long corridor. After a while, answers began to filter back. Some of the messages I could hardly bear to relay: “To my husband Joost: our baby died last week . . .” Along with personal messages were rumors about the world outside: “The Allies have invaded Europe!” (beat) (Pg 167) At last some of the names I had shouted began to return.

PRISONERS: Betsie Ten Boom is in cell 312. She says to tell you that God is good!

CORRIE: As far as I could discover, every single one taken in the raid – with the exception of Betsie and me – had been freed. Only about Father could I discover no news at all although I called his name over and over into the murmuring hall. No one seemed to have seen him. No one seemed to know . . .

(Pg 169) It was the third of May. I was sitting on my cot when the food shelf in the door banged open and shut with a single motion. And there on the floor of the cell lay a letter -- Nollie’s writing. Why should my hand tremble as I picked it up? The letter had been opened by the censors – held by them too: the postmark was over a week old. But it was a letter from home – the very first one! Why this sudden fear? (Unfolds the paper) “Corrie, can you be very brave?” . . .

CORRIE: No! No, I couldn’t be brave! (reading) I have news that is very hard. Father survived his arrest by only ten days. He is now with the Lord . . .” No details, not how or where he died, not even where he was buried. (reacts to a sound in the corridor) Footsteps were passing . . . “Please! I’ve had bad news – oh please, don’t go away”

(Pg 170) A jangle of keys - the cell door opened. “This letter just came. It says that my father – it says that my father has died.”

GUARD: Your father . . . (then coldly) Whatever happens, you brought it on yourself by breaking the laws!

CORRIE: (long beat, then she begins to pray) “Dear Jesus! How foolish of me to have called for human help when you are here. To think that father sees you now, face to face! To think that he and Mama are together again, walking those bright streets . . . “

I pulled the cot from the wall and below the calendar scratched another date: March 9, 1944 Father. Released.
```

---

## IC-2256: The House of Mourning

- Title: The House of Mourning
- Author (byline): Kate Braestrup
- Work: The Moth Presents All These Wonders, Pg 27-32
- Publisher: Crown
- Publication date as stated: Mar 2017
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: KATE, NINA’S MOM, FUNERAL DIRECTOR, TOM, KATE’S MOM, NINA’S DAD, NINA
- Teaser before the introduction: Yes
- Spoken words (computed): 1294
- Already set (do not supply): none

### Source block (context only)

```text
Author: Kate Braestrup
Book: The Moth Presents All These Wonders, Pg 27-32
ISBN: 978-1101904404
Publisher: Crown
Date (Month/Year): Mar 2017
```

### Introduction (context only: never use it for content warnings)

```text
It has been said that if you are old enough to love, you are old enough to grieve. Children as young as five are aware of the concept of death. They hear about it in fairy tales, see it in shows and movies – some children may have already experienced the death of a pet.

But what advice do you give to a parent in this situation? Is a child of five ready to enter . . .

The House of Mourning by Kate Braestrup
```

### Performance text (classify this)

```text
KATE: (Pg 27-32) Nina's mother came up to me, and she said . . . .

NINA’S MOM: Chaplain, I think I have a problem. It's Nina. She says she wants to go and see Andy, her cousin.

KATE: Well, I looked over at Nina, who was hanging by her knees from the swing set in her backyard, little pigtails brushing the ground. (to Nina’s Mom) How old is Nina, again?

NINA’S MOM: Five.

KATE: Wow. (to audience) I should probably mention that cousin Andy was dead.

KATE: I've been chaplain to the Maine Warden Service for about thirteen years now. And in Maine game wardens enforce fish and wildlife law. But they also respond to a whole variety of outdoor calamities: snowmobile accidents, freshwater drownings, all-terrain-vehicle accidents. And when they think the outcome is likely to be fatal, they ask their chaplain to go along. And I also teach game wardens in the academy how to support bereaved people. The example I usually use is personal. My first husband, a state trooper, was killed in the line of duty. He died instantly when his cruiser was T-boned by a truck. As soon as I was told that fact, I knew I wanted to see him and take care of him. So I told the funeral director, and [he] responded using a special voice that I think funeral directors learn in school.

FUNERAL DIRECTOR: Yes. I understand.

KATE: And then he went back to the funeral parlor, and he called the Maine State Police.

FUNERAL DIRECTOR: I think you should know that your trooper's widow wants to see and dress and take care of the body herself.

KATE: And the state police freaked out. All night long, phone calls were ricocheting back and forth between the state police, the funeral parlor and Tom, the trooper who had been specifically assigned to manage me. In the morning Tom arrived, and he said,

TOM: Kate, we're gonna let you do this thing. But you have to take me with you. And we're going to bring Sergeant Drake and Sergeant Cunningham along as well. If we don't like what we see, we're going to take you out.

KATE: And I pictured three troopers all drawing their sidearms and taking aim in the funeral parlor. I said, "I think it's gonna be okay." Mom was reassuring.

KATE’S MOM: (To Tom) You know, she grew up on a farm. She's used to dead things. (Pause)

KATE: I had to fake absolute confidence in this because I'd never done this before. But I faked it. I took my mother by the hand, and she and I, surrounded by troopers, did a weird sort of perp walk up the street to the funeral parlor. They were all watching me as I walked into this cool room where Drew's body lay. (Long pause) And it was okay. I was okay. I had about twenty minutes alone with my husband's body. Then they all came back, and we got him dressed in his dress uniform. And it was hard. (I mean, if you've ever tried to get someone into a Class-A uniform when they're not cooperating, you know what I mean.) But it was fine. Actually, it was better than fine. It was actually kind of great. It was beautiful and sad and funny, and it was okay. (Pause) But there are [those] who need a less personal, more biblical example. So, I remind them that Mary Magdalene went to see and touch and anoint the body of Jesus, and she didn't have to overcome the protective skepticism of the disciples to do that. When she got to the tomb and found it empty, she didn't have to justify her distress at finding the body gone. Nowadays we're persuaded that it's the presence of the body, not its absence, that is most distressing. But in my experience -- and I have a lot of experience by now -- people are far more likely to regret not having seen the body than they are to wish they hadn't. So, we're actually training our wardens to make space for the family to be with the body. Give them a moment where all the strangers and officials get out of the way and let them take care of their own. And let me tell you, the mourners are (pause) brave and (pause) tender. A mother will smooth the hair back from her drowned son's forehead, and the dad will hold his hand. A spouse will bring a flower and put it on his breast and murmur endearments. They're beautiful. (Pause) But okay. Nina was five. She was five. And her cousin, her best friend Andy. . . was four. Nina -- she didn't grow up on a farm. Maybe there's a dead goldfish in her background somewhere. But if you're five, there's not a lot of background to work with. Suffer the little children to come unto me. That was this biblical phrase that kept going around in my head. Although, the one good thing you could say about Andy's death was that he didn't suffer. He was killed instantly when an all-terrain vehicle driven by a neighbor rolled over on him. When we had cleared the scene that day, they had taken his body to a funeral parlor, and that was where Nina wanted to go, to visit him. Her dad said . . .

NINA’S DAD: We want to protect her.

NINA’S MOM: I know, but she's so sure.

KATE: And finally, I said (to Nina’s parents) You know, you're her parents. You know her. You know what's right for her much better than I do. But I do believe it would be okay. I believe it would not hurt her more to see him. (to audience) So, three days later, I went back up to this little town, because Andy's family had asked me to preside over the service. I got to the church a little early, and Nina's mom was there, and she was arranging stuff on the altar table -- photographs and Tonka trucks and teddy bears, flowers. (To Nina’s Mom) So, did Nina go see Andy?

NINA’S MOM: Let me tell you . . . Got in the car, drove her to the funeral parlor. Soon as we pull in, Nina's out of the car, striding across the parking lot. We had to scramble to keep up with her. She goes in through the front door, past the funeral-parlor guy. And we stopped her at the door of the cool room. (to Nina) Nina, we just want to make sure that you understand that Andy's not gonna be able to talk to you.

NINA: Yup.

NINA’S MOM: Well, and you understand, he's not gonna move or get up.

NINA: Yeah, yeah.

KATE: (takes over the story telling) And she opened the door, and in she went, and she walked right up to the dais where Andy's body lay, covered by a quilt that his mom had made for him when he was a baby. She walked right up to him, putting her hands on him to make sure he was all there. Then she put her head down on his chest and talked to him. After about ten minutes of this, her parents were awash in tears, and they'd kind of had enough, so they said, "Nina, you ready to go?"

NINA: No. I'll tell you when I am.

KATE: So, she sang him a song, and she put his Fisher- Price plastic telescope in his hand, so that he could see anyone he wanted to see from heaven. And then she was okay, and she was done.

NINA: But he's not gonna be getting up again, so I have to tuck him in.

KATE: So, she walked all the way around the dais, tucking in the quilt. And then she put her hand on him and said,

NINA: I love you, Andy Dandy. Good-bye. (Long pause)

KATE: You can trust a human being with grief. (Pause) Walk fearlessly into the house of mourning, for grief is just love squaring up to its oldest enemy. And after all these mortal human years, love is up to the challenge. (Pause) I don't have to fake confidence in this anymore, because I have Nina. And now, with the gracious permission of Nina's family, so do you.
```

---

## IC-2257: How to Explain Sex to a Child

- Title: How to Explain Sex to a Child
- Author (byline): Ellen Degeneres
- Work: My Point . . . And I Do Have One
- Publisher: Bantam Books
- Publication date as stated: Sept 2007
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1062
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ellen Degeneres
Book: My Point . . . And I Do Have One
ISBN: 978-0553384222
Publisher: Bantam Books
Date (Month/Year): Sept 2007
```

### Introduction (context only: never use it for content warnings)

```text
How to Explain Sex to a Child by Ellen Degeneres
```

### Performance text (classify this)

```text
Hey, Debbie, this is Ellen. Thanks for saying that you’d watch my house while I’m gone next week. I know you said you would water the plants, bring in the mail, and turn some lights on so that it looks like somebody is home. But if it’s not too much of an imposition, could you also make sure that the mobile over the crib isn’t tangled? Otherwise, the baby is just going to get bored. I never knew having a kid was so much responsibility! Bye bye.

I’m just joking. I don’t have a baby. I want to have a child. I really do. I think about it every day – and every day I change my mind. I think that part of my dilemma is that even though I want to have a baby, I don’t want to HAVE the baby. I can’t imagine HAVING the baby. Giving birth is just so much pain. I know it’s a beautiful child you end up with. I’m aware of that. But if I want a new washer and dryer, I wouldn’t necessarily want to HAVE a new washer and dryer, if you know what I mean (and if you don’t, I really don’t care to explain it in any more detail).

I don’t need a baby growing inside of me for nine months either. I know that a woman glows when she’s pregnant, and that sounds neat. But, I can get a pretty good glow by enjoying a steam bath followed by some assorted skin creams. The thing that I don’t understand most is when a pregnant woman joyfully talks about feeling her baby kick. To me, getting kicked isn’t as big a thrill as others make it out to be. I’ve never liked getting kicked from the outside, why would I feel any different about an inside kick?

But I would like to have a child. So, one day I’d like to adopt a baby who needs a loving home and be a mother who will adore him or her and teach it important things. I think I’d make a great mother. I’m great with kids. I know this because I’m the godmother to a precious little two- or five-year-old boy or girls (I’m not sure of the specifics). She (if it’s a girl) or he (if it’s not a girl) would always have to wear a helmet (even if it’s just to each cereal; those spoons can be mighty dangerous!); would be on one of those protective leashes until, at least, senior year of high school; and would, in general, be raised like people raise veal – confined to a crate by itself somewhere.

I think my best quality as a mother would be the ability to communicate complex ideas simply. I think all parents dread the old “How are babies made” question. I know my parents had a problem explaining this to me.

“Mommy, Daddy – how are babies made?”

“Well Ellen honey, there’s an egg.”

“Like a chicken egg?”

“No, smaller.”

“Like a robin’s egg?”

“No, much smaller – it’s very small. And Daddy gives Mommy . . . Well, there’s a Pappa Bear and a Mama Bear and the Mamma Bear has the baby in her tummy – “

“So I grew in a bear’s stomach?”

“No, but if you were a bear you would’ve.”

“But I’m not a bear?”

“No, you’re a little girl.”

“So, where did I grow?”

“In Mommy’s tummy.”

“How did I get there?”

“Daddy gave her special sauce.”

“Like McDonald’s?”

“Who knows? Maybe.”

“How did he give it to her? In a hamburger?”

“Okay. Yes.”

“I like hamburgers. God night.”

“Good night, sleep tight.”

I know that I could do a much better job answering that question than my parents. Other people sense this too. In fact, hardly a day goes by when somebody doesn’t ask me, “Ellen, how can I explain sex to my children?” And the more children there are, the more explaining about sex there is to be done.

By sex I mean, of course . . . sex. You know what I’m saying. There are many different types of sex, but for the purpose of this explanation I’m just talking about . . . you know, sex. In other words, you might have two consenting adults, a coconut, a pound of confetti, and a very thirsty yak. What they do may be very beautiful and spiritual and fulfilling, but it’s not necessarily something you’d care to explain to a child. Okay, I think we’ve defined our terms, so let’s get on with the explanation.

What you’ve got to do is just explain sex simply and to the point. You just say, “When you get older you’re going to meet somebody that you really, really, really like. Well, if you’re lucky you’re going to like that person. Maybe you don’t even like ‘em a lot, but at least they don’t bug you too much.

Maybe it’s better to be a bit more allegorical. Tell a little story. You could say that there’s a Papa Bear and a Mama Bear. And the Mama Bear says, “Where is that Papa Bear? He hasn’t been home in a long time. He says he’s working late at the pretzel factory, but I don’t believe that lying grizzly.” So she hires another bear to follow the Pap Bear – a Detective Bear (or, if you prefer, a detective goat – don’t be afraid to add your own spin to the story).

Well, the Detective Bear shadows the Papa Bear for a week. Then he tells the Mama Bear that every night, after work, Papa Bear goes to the same hotel room in the Poconos. Well, Mama Bear decides that she’s going to give Papa Bear a big surprise. So she goes to the hotel, kicks down the door, and there in the hear-shaped tub, sipping champagne, as naked as the day they were born are . . . . No, this isn’t a good way either.

There’s is a big fat queen bee, and she likes her honey. So she’s in her have and all these male bees are just buzzing around saying, “Oooo baby, I feel lucky tonight.”

Or you take a big tub of butter, some milk, tow or thee eggs, a dash of vanilla . . . No, I’m sorry, that’s not sex, that’s my recipe for French toast. At least I hope that’s not sex.

You know, I think the best idea is just to let the child watch cable TV.

So in conclusion, that’s how I would talk to a child about sex. I sincerely hope that I’ve been of help. Excuse me, but I’ve got to go out for a short walk. All of a sudden it has gotten very hot in here, and I’ve developed a craving for French toast!
```

---

## IC-2258: How to Help Your Husband Die

- Title: How to Help Your Husband Die
- Author (byline): David James Poissant
- Work: Heaven of Animals, Pgs 145-156
- Publisher: Simon and Schuster
- Publication date as stated: Mar 2014
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1762
- Already set (do not supply): none

### Source block (context only)

```text
Author: David James Poissant
Book: Heaven of Animals, Pgs 145-156
ISBN: 978-1476729961
Publisher: Simon and Schuster
Date (Month/Year): Mar 2014
```

### Introduction (context only: never use it for content warnings)

```text
Someone is taking their last breath in a hospital bed today, and you’re frustrated sitting in traffic. Someone is spending their first night alone after years of love, and you’re upset that your partner left dishes in the sink. Someone is burying their mother, and you’re annoyed your mom called you twice today. Perspective is everything. Appreciate the little things because, one day, they’ll be the big things.

How to Help Your Husband Die by David James Poissant
```

### Performance text (classify this)

```text
. . . in which a terrible loss punctuates the unfathomable depths of grief.

The morning your husband, the chef, stays in bed, bleary-eyed, sweating, and says for the past six months he’s been coughing up blood, turn hysterical. Demand he drive you both to the emergency room at once.

Ask why he didn’t see a doctor six months ago. Ask why he’s such a man when it comes to his health. Ask what he thought would happen if he kept smoking. If you scold and scold, when the bad news comes, it won’t be your fault. When the bad news comes, you can say, I told you so.

When the bad news comes, cry . . . He will not cry. He will not say anything at all. You will ride home in silence.

Tell him not to worry, that it could be a thousand things, that the hospital only said possibly, that no good doctor diagnoses something like that on a first visit. At home, when you think of the way you spoke to him that morning, run to the toilet and throw up. When he asks what made you sick, blame the week-old pizza you reheated for lunch. Blame anything but him.

Get second opinions, thirds, however many it takes to find a doctor who will say, This is not what it looks like.

Learn tricks to keep yourself from crying. When a doctor talks, cross your arms. When the doctor leaves the room, press your thumbs to your eyes and suck in air. Before your husband can ask, say, I’m okay . . .

Wait. By the time this is all over, you will know patience in a whole new way. Wait for the nurses. Wait for the doctors. Keep track of time. On average, find you spend five to six hours a week sitting in rooms waiting for people to see you. Wait. Learn new ways to wait. Bring books. Bring bills. Bring board games. In waiting rooms and offices, play cards. Hearts, Spades, Crazy Eights. Quit Slapjack after you miss the pile and leave a bruise on his hand that lingers for weeks . . .

After a month of meetings, tell yourself that you are tired of doctors, that tomorrow’s X-rays will be the last. Smile when you imagine the wait is almost over. The doctor will tell your husband that he has several options, but only one, really, if he wants to live. Listen and smile -- smile the way you do at a person you wish would just, for God’s sake, please stop talking.

What the doctor won’t tell you is that the disease will tear your husband apart. That he will be sicker than he has ever been. That, in the end, it will be the cure that kills him. But you will, somehow, in the flicker of an instant, see what lies ahead. Your husband won’t see another summer.

He will begin treatments in a week. Beg him to quit his job. He will say he’s not giving up that easy. Yes, he knows your health insurance could cover him. Yes, he knows he needs rest, that the kitchen of a four-star restaurant is no place for a chemo patient. No, he won’t quit his job. Quit your job. You never liked it anyway. Who grows up saying, I want to be a dental hygienist? Kids want to be artists, veterinarians, firefighters.

When you find you have too much time on your hands, decide to learn everything there is to know about cancer. Decide you want to know exactly how your husband is going to die. The moment you do, believe that you can save him.

Study the disease. Go to the university library. Read every book they own on cancer. Search for the card catalog. Learn the Dewey decimal system. If you learn enough about the cancer, you can conquer it. If you search long enough— comb every essay, read every study, explore each article— you will find a treatment.

Make this your day job, five days a week. To battle fatigue, work harder. Don’t stop. Stay at the library all day, every day. Don’t leave until your fingertips are gray with ink, until your tailbone aches from the curve of the library’s stylishly modern chairs. When you can’t take any more, are ready to give up, you will know guilt . . .

By winter, you will know more than the doctors. Recommend treatments. Question their methods. Grow irritated when a doctor hasn’t heard of a specific drug or experiment in Southeast Asia.

When your husband comes home from the restaurant one night and falls to the floor, understand it’s time for him to stay home. Forget the library. Concentrate on chemotherapy. Concentrate on radiation. Concentrate on making it through each day.

Notice the hair in the bathroom. Strands in the sink and shower, tangles in drains. When you find clumps in the bed, collect the hair. Save it in a Ziploc bag like a child’s first haircut keepsake. When he finds the bag and yells at you, throw it out. Once he’s lost the last of his hair, tell him that he is beautiful. Wait until he’s asleep to sob.

Try church. When the priest places the wafer on your tongue and says, “This is His body, broken for you,” think, This is his body. Spend the rest of the day whispering it to yourself: This is his body. This is his body. . .

There are certain things you should know.

There will be things you can’t make better. Don’t try to hold his hand when he coughs. Don’t try to trade Seinfeld reruns for hours of meaningful this-is-your-life conversation. (He’ll want nothing to do with such talk.)

Know that no matter how many laps you walk to raise money for research, no matter how many free T-shirts you earn, your husband is still going to die . . .

The night he has the first seizure, call 911. Ride in the ambulance. Bury your face in your husband’s shirt and cry. Sit beside him on the thin hospital mattress. Watch him sleep. Stay awake, all night, running your hand down his arm. Realize you spent so much time studying the disease that you forgot to prepare for what comes next.

From this point forward, spend your days in the hospital room, for this is where he is meant to spend the rest of his life. Learn to tell when he wants to talk about this and when he doesn’t, regardless of the words that come out of his mouth. Buy a potted plant. Place the plant on a table by the window, where it will get plenty of light. Water it every day. Tell yourself that as long as the plant lives, he will live. On his worst days, imagine the plant as his lifeline. The plant is alive. He cannot die.

Get used to seeing blood drawn from his body. Eventually, he won’t notice the needles. At night, trace the veins of his arms. Rub the purple circles left by needles jabbed too hard. Hold your breath and kiss each bruise.

Be brave.

While he’s still lucid, write the will, then put it away in the safety deposit box with the marriage license and birth certificates. Marvel at how these three—birth, death, and the union that came between—fit into an inch-deep metal drawer.

At the hospital, read books to him, as many as you can. Don’t talk doctors or painkillers or funeral arrangements. Don’t make him leaf through brochures to pick out a casket, flowers, the perfect burial plot. There is no last lesson, no big picture, no final words. So, read to him and let his mind wander. Read even when you know he’s not listening . . .

When the very end is in sight, tell him you’re leaving and you’re taking him with you. Clean him and dress him and pull out his IV. Let the fluid flow from the tube to the floor. Unplug the heart monitor, and pull the black pads from his chest. He’ll worry about expenses, about insurance coverage. He’ll worry about being a burden. Tell him he never could be.

When you lift him, his lightness will make you dizzy. He will feel like a child in your arms. Help him into a wheelchair, then make a break for it. Wheel him out a side door, and, when you hear a woman’s voice, don’t look back. Drive home and put him in his real bed.

Understand that things will move quickly now, without fluids and pills, monitors and morphine, electrodes and tubes. Bring him more covers when he grows cold.

While he sleeps, listen to him breathe. Lie awake counting breaths. As the breaths grow farther apart, wonder, in the silence of daybreak, whether each breath you just heard was the last. Do this, and you will know despair. You will know helplessness. Fall asleep with the sunrise, weak, feeling alone . . .

Wake to his smile beside you, and see he’s been watching you sleep. He’ll be too tired to talk. Don’t try to fill up the silence with words. Help him out of bed with quick, simple commands. Lift your head. Help me with your feet. Hold my shoulder. Otherwise, keep quiet. Nothing you say can make this sacred. Everything you want to tell him before he dies is only for you, so pray it to yourself tonight when he’s gone.

Take him to the beach. Take him because it is beautiful. Take him because you can. Sit on the shore and trace your initials together in the sand. Play tic-tac-toe and let him win. Hold him as he coughs and coughs and coughs. He will rattle like a skeleton in your arms.

When your husband tells you every terrible thing he’s done, every way he’s wronged you, no matter how it hurts, don’t make him beg your forgiveness. Tell him you love him, that nothing else matters. Do this because you’ve reached the end together, because why make it harder. Love him.

The whole round world will funnel into nothingness, and you will see the truth in his eyes: that life, that living, is more than what’s come before. That all you have is this moment. Don’t look away or he’ll disappear. The world is here only as long as you keep your eyes open. Keep your eyes on him and he’ll never leave you, if you can just keep from blinking. And your eyes will ache, they’ll burn from holding them open for so long, and when you blink, like that, he’ll be gone.
```

---

## IC-2259: Hump Day

- Title: Hump Day
- Author (byline): Lynda van Devanter
- Work: Home Before Morning: The Story of an Army Nurse in Vietnam
- Publisher: University of Massachusetts Press
- Publication date as stated: April 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: LYNDA
- Teaser before the introduction: No
- Spoken words (computed): 1769
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lynda Van Devanter
Book: Home Before Morning: The Story of an Army
Nurse in Vietnam
ISBN: 978-1558492981
Publisher: University of Massachusetts Press
Date (Month/Year): April 2001
```

### Introduction (context only: never use it for content warnings)

```text
Lynda van Devanter was an army nurse who served in Vietnam in 1969 and ’70 at the 71st evacuation hospital in Pleiku. She began and led the Vietnam Veterans of America’s Women’s Writing Project and counseled many other veterans. She died on November 15th, 2002 from a cancer as a result of exposure to Agent Orange. Her story lives on. “Hump Day” by Lynda van Devanter
```

### Performance text (classify this)

```text
LYNDA: The largest number of people I grew up with grew up with a sense that we had a mission. We had a purpose to our lives, and that we had a responsibility to give something back to this world, and I was part of a generation of Americans who were chosen to change the world. We were sure of that. It was only a matter of waiting until we all grew up. We were the kid next door, both men and women. What I saw in Vietnam was not men. What I saw in Viet Nam was boys. They were kids. They were

generally 17, 18, and 19 years old. And for those of us who were women in Viet Nam, we were barely out of nursing school. We were basically these naïve, idealistic kids of the 50’s and 60’s who thought of Kennedy in the same breath with, “Ask not what your country can do for you, ask what you can do for your country.” We thought of Kennedy in the same breath with, “This generation will pay any price, bear any burden, to save this world for democracy.” I was a citizen of the greatest country in the world, and I was about to give part of my self to keep America great. We were carried along by the noble sentiments of John Fitzgerald Kennedy, and honest to God, I mean, it beat in my heart. It beat in all of our hearts. It really did. And so, nursing was the way that I was going to make my contribution to society. As we began our odyssey into Viet Nam, as we began our odyssey into the new people that we were eventually to become, it was a process that I think we had hoped we would be able to ease our way into, and it didn’t quite turn out that way. The day that I arrived in Viet Nam, I arrived in --- --- at the 90th replacement battalion, I learned that 2nd lieutenant Sharon Lane, who was a nurse on a ward at the 312th evacuation hospital at Cu Chi, had been killed that morning when a rocket had landed on her ward. I suddenly became very aware that women could in fact be in danger, and that this was no game anymore. Although the instructors back in basic had warned us what to expect, no amount of warning could ever have prepared me for the sheer numbers of mutilated young bodies that the helicopter kept bringing to the 71st. Dead bodies in glad bags were still being lined up outside the ER door, to be moved to the morgue as there was time. The moans and screams of so many wounded were mixed up with the shouted orders of doctors and nurses. So much for easing my way in.

What I came to realize was we developed a living, breathing relationship with Death as a human entity. Death became somebody who we had a relationship with, and Death became somebody to fight sometimes and welcome sometimes. And when we fought with Death, we fought tooth and nail. And we used every tool at hand, and a lot of times the only tool we had was cursing it out because we were so enraged at it. As each day passed, I found myself growing a harder and harder shell to protect my emotions. I started listening to the local discontents, who railed against Nixon, Congress, the Joint Chiefs of Staff, and the whole U.S. government. Every time another person died on my table, I came one step closer to agreeing with them. As each day passed, I found myself growing a harder and harder shell to protect my emotions. I started listening to the local discontents, who railed against Nixon, Congress, the Joint Chiefs of Staff, and the whole U.S. government. Every time another person died on my table, I came one step closer to agreeing with them. And one day I saw some dead American soldiers lying outside the morgue. They had been ambushed by an NVA unit. The butchers had cut off our soldiers penises and stuffed them into the GI’s mouths. I was outraged by the scene, but not as outraged as I became when I later saw a similar scene, only this time with dead Viet Cong.

During those months, I lost my direction and found myself becoming a person I would never have been before Viet Nam. Maybe, you would have said I was merely getting tough. Like thousands of Americans, I began calling the Vietnamese, both friendly and enemy, gooks. I would have thought I was above that sort of racism. After all, hadn’t I marched in the United States for civil rights like a good Catholic girl who believed all oppression was wrong? For each one of us, there was someone who seemed to personify what the war was, its futility, its desperation, and the worst of it, the parts of it that remained with us for the rest of our lives after returning, at least for every one of us, who I know of who was a woman who served in Viet Nam. Mine was a guy named Gene. It was a few days before my hump day, the exact middle of my tour when I would be over the hump. I was lost in a heavy sleep under my bed when the phone started ringing. Still half asleep, I listened to the worlds. More casualties, Van. We need you in surgery. There’s a bad one in the neuro room, she said. I need you to pump blood in there. Leading to the operating table was the largest trail of blood I had ever seen. I tried to walk quickly through it but slipped. When I regained my balance, my eyes were drawn to the gurney, where several people were transferring the wounded soldier from the green litter to the table. The lower portion of his jaw, teeth exposed, dangled from what was left of his face. It dragged across the canvas litter and then swung in the air as he moved from the gurney to the table. His tongue hung hideously to the side with the rest of the bloody meat and exposed bone. When he was on the table, Mac Schafner, the facial surgeon, dropped the lower jaw back into place. I held my breath to keep from getting sick. For a moment, I was glued to the spot. I thought I had gotten used to it all, but they kept getting worse. I wasn’t sure I could handle this one. But the shout of the anesthesiologist, Jim Castellano, snapped me out of my trance.

‘The son of a bitch is drowning in blood!’ he screamed. ‘Someone help me get a f---ing airway into him.’ A gurgling came from the soldier’s throat. Jim’s hands were quick. ‘Don’t you dare die, you motherf---er.’ There was an ugly, metallic coughing sound as the soldier bucked for breath.

‘Breathe, damn you!’

A barely audible sound escaped. ‘That’s it, soldier. Come on.’

In the middle of the confusion, the neurosurgeon came into the room. He looked at the soldier on the table and shook his head. His face was red. ‘Who the f--k woke me up for this GORK?’

‘The brain doesn’t look too damaged,’ Mac said. ‘You’re wasting your time.’

‘We can fix him,’ Mac insisted, ‘just give me a chance.’ ‘Bulls--t,’ the neuro guy said, ‘that sucker’s going to die and there’s not a f---ing thing you can do.’ He stormed out of the room. It was all just another simple job where I could turn off my mind and try to forget that we were working on a person, but this one was different. The young soldier was not about to let me forget. During one of my circuits around the table, I accidentally kicked his clothes to the side. A snapshot fell from the torn pocket of his fatigue shirt. The picture was of a young couple, him and his girlfriend, I guessed, standing on the lawn in front of a two story house, perhaps belonging to her parents. On the back of the picture was writing, the ink partially blurred from sweat: ‘Gene and Katie, May 1968.’ I had to fight the tears as I looked from the picture to the helpless boy on the table. Now a mass of blood vessels and skin, so lacerated that nothing could hold them together. I had always held the notion that given enough time, anything could be stopped from bleeding I pumped 120 units of blood into that young man, yet as fast I pumped it in, he pumped it out. After hours of work, Mac realized it was futile. The boy had received so much banked blood that it would no longer clot. Now he was oozing from everywhere. Slowly, Mac wrapped the boy’s head in layers of pressure dressings and sent him to post-op ICU to die. Gene and Katie, May 1968. While I cleaned up the room, I kept telling myself a miracle could happen. He could stop bleeding. Nothing was impossible. Please, God, help him. This wasn’t merely another casualty, another piece of meat to throw on the table and try to sew back together again. He had been real, Gene. When I finished making the room ready for the next head injury, the next young boy, I walked to post-op to see Gene. I held his hand and asked him if he was in pain. In answer, he squeezed my hand weakly. I asked him if he wanted some pain medication, and he squeezed my hand again. All the ICU patients had morphine ordered for pain, and I asked one of the nurses to give Gene his morphine intravenously, knowing that while it would relieve his pain, it would also make him die faster. I didn’t care at that point. I just wanted him to slip away painlessly, quickly, easily. I ran my finger over the edge of the picture before putting it into an envelope with his other possessions, then I walked outside, sat on the grassy hill next to post-op and put my head in my hands. I wouldn’t cry, I told myself. I had to be tough. But I knew a profound change had already come over me. With the death of Gene and with the deaths of so many others, I had lost an important part of myself. The Lynda I had known before the war was gone forever.
```

---

## IC-2260: I Can Hear My Soul Cracking

- Title: I Can Hear My Soul Cracking
- Author (byline): Slavenka Drakulic
- Work: A Memory, a Monologue, a Rant, and a Prayer, Pg 51+
- Publisher: Villard
- Publication date as stated: May 2007
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: MOTHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1448
- Already set (do not supply): none

### Source block (context only)

```text
Author: Slavenka Drakulic
Book: A Memory, a Monologue, a Rant, and a Prayer,
Pg 51+
ISBN: 978-0345497918
Publisher: Villard
Date (Month/Year): May 2007
```

### Introduction (context only: never use it for content warnings)

```text
In 1995, a paramilitary Serbian unit known as the Scorpions executed six unidentified civilian men. Four of them were underage; the other two, under 30. The soldiers filmed the executions to be used for educational purposes. A “how to” instructional video for executions, if you will.

Before the film footage was destroyed, a US film company created a documentary covering the Bosnian War. And the events of Srebrenica. More than 8,000 men and boys in and around the town of Srebrenica were killed – a massacre – a genocide.

Fast forward to 2005. Imagine flipping through the channels on your television only to come across film footage of your son’s execution. A son who had disappeared a decade earlier when he was only 16.

I Can Hear My Soul Cracking by Slavenka Drakulic
```

### Performance text (classify this)

```text
MOTHER: (Pg 51+) You ask me about my son? How I felt when I saw Azmir being killed? My child, how can I answer that kind of question? How can I tell you that? What words can I use to describe my pain? You say “killed,” and it seems to me that you feel nothing— how could you? He is only a name to you. But my whole body trembles when I hear it, just that one word. Azmir, my son, he was the soul of my soul. . .

But perhaps I should try to tell you that, for the sake of others who show remorse and have respect for my tragedy. And for the sake of other mothers like me, I know that they are many.

MOTHER: That day it was only the beginning of June but already very hot. Just like that July day in Srebrenica ten years ago, I thought as I put a dzezva with water for a coffee on a stove. My second coffee of the day. It was late afternoon, and soon my neighbor Amra will come home from work with her young daughter, Selma. Often I envied her for having a daughter; it is such a blessing to have a female child in a time of war. But I am wrong, of course. A woman’s curse is different, that’s all. I was grateful that Amra was helping me. I expected that the three of us would have a supper together and watch television, as we did every evening. Ten years passed. If Azmir had not disappeared, he would have been twenty-six now—a grown-up man, maybe even married. I still remember that he liked that dark-haired girl from his school class, though nowadays it would be difficult for them to marry.

She was a Serb. I like to imagine what would happen if he were here with me. I daydream about his job—he was so good with his hands—and a new house that he would surely be able to build. I like to daydream, imagining Azmir had the power to warm me and wake me up from a cold that I felt inside. That warmth used to keep me alive. But then immediately, I feel shame, the same feeling that I have experienced so many times, shame that I am alive and he. . . . Why? Why me? If someone had asked me to trade my life for that of my son, Azmir, I gladly would have done it. Not very tall and rather thin, he looked younger than his age— no more than a boy, really! This was the reason that I believed Azmir could be spared by soldiers. How wrong I was, I thought, embittered, sitting in the kitchen that afternoon. I slowly sipped my thick, strong coffee. See, I was convinced that I was reconciled with Azmir’s death long ago. Only I didn’t mention that ugly word, not even to myself. What else would keep him from coming back to me, calling me, for ten years? No way Azmir would not contact me somehow, through relatives, perhaps, he would find a way. My whole body told me that Azmir was no longer in this world, the same as his uncle, who was killed by Arkan’s soldiers when he visited Bijeljina at the very beginning of the war. At least I knew about him, I was certain, I was even able to get his body (for money, of course) and bury him properly. It is important to give people a burial; one should not be buried without a name, together with others in a mass grave. Why do we all have a name? We have it in life, and we should have it in death, that’s what I think. And I wanted to bury Azmir properly, if he was . . . Well. Although I felt Azmir’s end in my every muscle and bone, the truth is that I did not know for certain what had happened to him. And when. And where. It was not officially confirmed, or so I was told. In the last few years there were bones dug out, bones of thousands of men who were executed around Srebrenica.

Like other women, I went to identify remnants of my son. But a watch and a few photos and a piece of shirt I was shown, together with some darkened bones, were not his—odd how thin and fragile human bones look, as if eaten by earth, I thought. I remember letting out a big sigh, not knowing if I was relieved that these remains were not Azmir’s, or unhappy that I could not finally get over with the torture of living with uncertainty year after year. Thinking that his bones are shattered in the woods, that he is not buried, that some other mother—just like me—looks at someone’s things with fear and then relief. I was afraid that Azmir was not only dead but also lost for me, lost forever. So, that evening I was in the kitchen washing dishes after dinner with Amra and Selma, as usual. Just then I heard a voice from the TV in the living room saying something about Srebrenica. Ah, yet another program, I thought. I had seen a few in the years that passed, always with a knot in my throat while looking for the familiar face of Azmir and hoping that I wouldn’t see it. I was tired of this, not sure that I could force myself to watch anything that had to do with Srebrenica again. Ten years is a long time when you wait. Why look at that program, what could it tell me that I already didn’t know?

Yet I could not resist and went back to the living room and sat down. Amra was still there; Selma had gone back to their apartment. It was not a real film but some kind of a documentary, they said, and the picture was shaking, jumping. But I could see the Serbian soldiers in fatigue uniforms and red caps, their faces in front of the camera.

They were not even hiding, so sure they were of themselves, so arrogant. . . . And then I saw a group of four prisoners, young men with their hands tied in the back. The soldiers killed them just like that. It all happened so abruptly, so quickly, that I had no time to react, to switch off the TV set or something. But when another two prisoners appeared on the screen, I averted my eyes. I was not quick enough, though . . . because from the corner of my eye, I saw a familiar figure.

Instantly, I recognized my son, Azmir, his light brown hair, his hands, his shirt. He stood there for a short while with his hands tied back, bent slightly forward. Suddenly, I felt pressure in my chest, as if I were sinking into water—like when I was small and fell into a river. I gasped for air, but there was not enough. I could hear no sound, not even my heartbeat, nor could I utter a single sound. I was trapped in that water. In that room, in that picture on the screen, and there was no way out. I knew what was coming. When Azmir turned toward the camera with a frown on his forehead so familiar to me—because he used to frown like that when he was small and frightened, just before he would start crying—I tried to close my eyes. I had seen enough. But my own eyes betrayed me, and I stared while Azmir took a bullet and fell gently on his back. Now it all happened very, very slowly, or it only seemed so to me, I didn’t know any longer, nor did I care. I was still under the water with my lungs about to explode. Then I felt Amra shaking me gently, and I took a breath. I saw what I had seen so many times in my nightmares—but now, for the first time, I saw it to the very end. In my nightmare, there was never an end, and I would wake up wishing to know . . . the end. That evening I saw it. I know it now.

When I finally managed to close my eyes, I heard a strange sound coming from somewhere inside me. The sound of cracking, like cracking of ice in the springtime. “I can hear my soul cracking,” I said to Amra. She held me tightly in her arms for a while. That night, alone in my bed, I saw the same picture again and again. Not of Azmir’s death, but of his face, looking for help that did not come.
```

---

## IC-2261: I Know Why the Caged Bird Sings

- Title: I Know Why the Caged Bird Sings
- Author (byline): Maya Angelou
- Work: Not specified
- Publisher: Bantam Books
- Publication date as stated: May 1983
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: MINISTER, SISTER MONROE, DEACON JACKSON, BAILEY, REVEREND THOMAS, MOMMA, UNCLE WILLIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1556
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
Note: Items in brackets or parentheses are to be acted out, not spoken. In the Christian Methodist Episcopal Church the children’s section was on the right, cater-cornered from the pew that held those women called the Mothers of the Church. On Sundays, it was ordained by Momma that Bailey and I occupy the first row, called the mourners’ bench. I thought we were placed in front because Momma was proud of us, but Bailey assured me that she just wanted to keep her grandchildren under her thumb and eye.

People spoke of Momma as a good-looking woman and some said she used to be right pretty. I saw only her power and strength. She was tall, and her hands were so large they could span my head from ear to ear. Each Sunday the minister would announce,

MINISTER: We will now be led in a hymn by Sister Henderson.

And each Sunday she looked up with amazement at the preacher and asked,

SISTER HENDERSON (MOMMA): Me? [After a second of assuring herself that she indeed was being called upon, she laid down her handbag and slowly folded her handkerchief. This was placed neatly on top of the purse, then she leaned on the bench in front and pushed herself to a standing position, and then she opened her mouth and the song jumped out as if it had only been waiting for the right time to make an appearance.] [Insert hymn phrase of your choice here] That Sunday Reverend Thomas took his text from Deuteronomy. Deuteronomy was my favorite book in the Bible. The laws were so clear, that I knew if a person truly wanted to avoid being roasted forever in the devil’s fire, all she had to do was memorize Deuteronomy. I also liked the way the word rolled off the tongue. Deuteronomy.

Bailey and I sat alone on the front bench, the wooden slats pressing hard on our behinds. I would have wriggled just a bit, but each time I looked over at Momma, she seemed to threaten, “Move and I’ll tear you up,” so, I sat still. The church ladies were warming up behind me with a few “hallelujahs” and “Praise the Lords” and “Amens“, and the preacher hadn’t really moved into the meat. It was going to be a hot service.

I saw Sister Monroe, her gold crown glinting when she opened her mouth. She couldn’t get to church every Sunday, so she made up by shouting so hard when she did make it that she shook the whole church. It took three women and sometimes a man or two to hold her.

Once when she hadn’t been to church for a few months she got the spirit and started shouting, throwing her arms around and jerking her body, so that the ushers went over to hold her down, but she tore herself away from them and ran up to the pulpit.

SISTER MONROE: [She stood in front of the altar, shaking like a fresh caught trout. She screamed at Reverend Taylor.] “Preach it. I say, preach it.”

Naturally he kept on preaching.

SISTER MONROE: [Then she screamed an extremely fierce] “I said, preach it”

. . . and stepped up on the altar. The Reverend kept on. Sister Monroe made a quick break and caught the minister by the sleeve of his jacket and his coattail, then she rocked him from side to side.

I have to say this for our minister, he never stopped giving us the lesson. The usher board fairly ran to the minister’s aid. Two of the deacons, in their shiny Sunday suits, joined the ladies in white on the pulpit, and each time they pried Sister Monroe loose from the preacher he took another deep breath and kept on preaching, and Sister Monroe grabbed him in another place, and more firmly. Reverend Taylor was helping his rescuers as much as possible by jumping around when he got a chance. His voice at one point got so low it sounded like a roll of thunder, then

SISTER MONROE: Preach it!

Then the pandemonium spread. The spirit infused Deacon Jackson and Sister Willson, the chairman of the usher board, at the same time. Deacon Jackson gave a scream

DEACON JACKSON: [like a falling tree,] Aaaaahhhh!

. . . and punched Reverend Taylor on the arm. It must have hurt. Reverend Taylor jerked around sur-prised, and punched Deacon Jackson. Then Sister Willson caught his tie, looped it over her fist, and pressed down on him. Next thing all three of them were down on the floor behind the altar. Their legs spiked out like kindling wood. Sister Monroe got up and walked off.

SISTER MONROE: (singing) I came to Jesus, as I was, worried, wound, and sad, I found in Him a resting place and He has made me glad.

The minister took advantage of already being on the floor and asked in a choky little voice if the church would kneel with him to offer a prayer of thanksgiving. He said we had been visited with a mighty spirit, and let the whole church say “Amen.”

On the next Sunday, Sister Monroe’s fuse was already lit, and she sizzled somewhere to the right behind me. I saw the ushers from the left side of the church near the big windows begin to move discreetly, like pallbearers, toward Sister Monroe’s bench. Bailey jogged my knee. When the incident with Sister Monroe, which we always called “the incident,” had taken place, we had been too astounded to laugh. But for weeks after, all we needed to send us into violent outbursts of laughter was a whispered “Preach it” Anyway, he pushed my knee, covered his mouth and whispered,

BAILEY: I say, preach it.

I looked toward Momma over the collection table, hoping that a look from her would root me safely to my sanity. But Momma was staring at Sister Monroe with a severe look. But Sister Monroe’s voice had already reached the danger point.

SISTER MONROE: Preach it!

Bailey nudged me again.

BAILEY: [in a whisper] I say, preach it

SISTER MONROE: (echoing him loudly) I say, preach it!

Two deacons wedged themselves around Brother Jackson as a preventive measure and two large de-termined-looking men walked down the aisle toward Sister Monroe. Elder Thomas made the regrettable mistake of increasing his volume. Then suddenly, Sister Monroe broke through the people trying to hem her in, and [ran] up to the pulpit.

SISTER MONROE: I say, preach it!

BAILEY: Hot dog . . . Damn . . . She’s going to beat his butt.

But Reverend Thomas didn’t intend to wait for that, so as Sister Monroe approached the pulpit from the right, he started descending from the left, preaching and moving. He finally stopped right in front of the collection table, which put him almost in our laps, and Sister Monroe rounded the altar on his heels, followed by the deacons, ushers, some unofficial members and a few of the bigger children. Just as the elder said . . .

REVEREND THOMAS: Great God of Mount Nebo . . .

Sister Monroe hit him on the back of his head with her purse. Twice. Before he could bring his lips together, his teeth jumped out of his mouth and landed right by my foot. Bailey pinched me and said without moving his lips,

BAILEY: I’d like to see him eat dinner now.

Now, I dreaded laughing in church. If I lost control, two things were certain to happen. I would surely pee, and just as surely get a whipping. And this time I would probably die because everything was funny — Sister Monroe, and Momma trying to keep her quiet with those threatening looks, and Bailey whispering

BAILEY: Preach it

. . . and Elder Thomas with his lips flapping loose like tired elastic.

REVEREND THOMAS: (gummed without his teeth) Naked I came into the world, and naked I shall go out.

Bailey’s laugh had worked its way up through his body and was escaping through his nose.

BAILEY: (Snort. Snort. Snort)

I didn’t try any longer to hold back the laugh, I just opened my mouth and released sound. [Laughs] Momma said,

MOMMA: Sister!

. . . but the bench was greasy and I slid off onto the floor. There was more laughter in me trying to get out. I didn’t know there was that much in the whole world. It pressed at all my body openings, forcing everything in its path. I cried and hollered, passed gas and peed.

I didn’t see Bailey descend to the floor, but I rolled over once and he was kicking and screaming too. Each time we looked at each other we howled louder than before, and though he tried to say something, he was only able to get out

BAILEY: I say, preach.

. . . And then I rolled over onto Uncle Willie’s rubber-tipped cane.

UNCLE WILLIE: [The one side of his mouth pulled down as it usually did when he cried (it also pulled down when he laughed). He stuttered,] I’m gonna whip you this time myself.

I have no memory of how we got out of church and into the parsonage, but in that parlor, Bailey and I received the whipping of our lives. Uncle Willie ordered us between licks to stop crying. I tried to, but Bailey yelled so loud and disturbed what was left of the service, the minister’s wife came out and asked Uncle Willie to quiet us down.

For weeks after that I stood on laughter’s cliff and any funny thing could hurl me off far below.

Each time Bailey said “Preach it” to me, I hit him as hard as I could and cried.
```

---

## IC-2262: I Love Everybody

- Title: I Love Everybody
- Author (byline): Lori Notaro
- Work: I love Everybody (and other Atrocious Lies); Pgs 113-132
- Publisher: Villard
- Publication date as stated: June 2004
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: LORI, SAMPLE LADY, BIG HAIR LADY, BAKERY LADY
- Teaser before the introduction: Yes
- Spoken words (computed): 1895
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lori Notaro
Book: I love Everybody (and other Atrocious Lies);
Pgs 113-132
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

I am not indiscriminately mean; I must be provoked first. I would classify myself as a Pointer-Outer of Extraordinary Acts of Incredible Foolishness. Some people would call these experiences meltdowns, but I would rather consider them Opportunities to Enlighten. For example: • If you are sitting behind me in a movie and you feel the need to converse as freely as if you are in your living room, I will "Shhhh!" you and then I will ask you for ten dollars. I cannot grasp the need to talk in a movie theater. • If you cut me off in traffic like you've got someone in the passenger seat whose severed limb is floating in an Igloo cooler on his lap, then suddenly and inexplicably slam on your brakes for no apparent reason, I will scream, maniacally, and point my finger at you. This

• If you try to sneak two weeks' worth of groceries through the express line and think that no one will notice, I will look at your cart, look at you, and then shake my head in utter and obvious disgust. I'm done tolerating your type. I mean it. I have the ability to count to fifteen and I will USE IT ON YOU. • If I happen to be looking out the window and see you allow your dog to take a *poop* in my yard, I will run outside with a pen and a piece of paper and query, "Hey, can I have your address? Because my dog will probably have to crap in the next hour or two, and I'm bringing her to your house to do it."

So I guess I am mean, I can admit that much . . . [And then in that millisecond of reflection] I hatched a brilliant, brilliant, magnificent plan: I would immediately embark on a life as a Nice People Person Person.

Really, I said to myself, how much energy could it take to be nice? A whole lot less than being angry, hostile, and frustrated nearly every time you encountered one of the Foolish, which could realisti-cally be sixty times in one single minute if you were at the movies, the grocery store . . . . driving someplace. All you had to do to be nice was smile and nod your head. Smile and nod. And sometimes toss in a "My, what a pretty dress!" or an "Aren't you delightful?"

So I practiced smiling and nodding, and what a piece of cake! To think I could have been doing this all along! After a couple of hours, I felt I was ready to start a new phase in my life, appropriately titled "I Love Everybody," and it was going to be a good day to test out my new niceness, especially as I was headed to Costco to pick up my nephew's birthday cake before his party.

I Love Everybody

LORI: Two miles from Costco, all is going well until a Chevy two-ton crosses two empty lanes of traffic to squeal in front of me and then reduces its speed to that of a Fred Flintstone car. As I passed the truck, I smiled and I nodded. "Aren't you delightful?" I said, to which he stuck his big, filthy tongue into his cheek and vigorously moved it around as he raised his eyebrows repeatedly. I laughed and said through my smiling, clenched teeth, “Nice.” I Love Most Everybody

LORI: "Hi, how are you?" I said to people passing by who smiled at me, had some sort of visible ailment or challenge, or were in my way, which I figured would earn me more karma nice points, as I had a lot of catching up to do.

It was almost noon, and in Costco, that translates into a free hors d'oeuvres lunch. So I got in line, waiting for my free whatever it was. It was almost my turn, there were only two girls, who looked to be in their very early twenties, ahead of me.

At that precise moment, a sharp, high-pitched noise erupted in front of me that used my ear as a portal to repeatedly stab at my brain: Brrrring! Brrrring! 1st GIRL: That’s you! Brrrring! Brrrring! Stab! Stab! 2nd GIRL: It is so totally not me! Brrrring! Brrrring! Stab! Stab!

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

I tightly clutched the handle of my own cart, chanting with a clenched jaw over and over again like a mantra, "I Love Everybody, I Love Everybody, I Love Everybody, I Love Everybody," until I saw a break in cart traffic ahead and geared myself, getting ready to make a break for it.

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

## IC-2263: I Love You, Dad (An Unsent Letter)

- Title: I Love You, Dad (An Unsent Letter)
- Author (byline): Grace Song
- Work: Yell-OH! Girls
- Publisher: Harper Collins
- Publication date as stated: July 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1454
- Already set (do not supply): none

### Source block (context only)

```text
Author: Grace Song
Book: Yell-OH! Girls
ISBN: 978-0060959449
Publisher: Harper Collins
Date (Month/Year): July 2001
```

### Introduction (context only: never use it for content warnings)

```text
Asian girls who have emigrated to the West with their families often feel torn between a reluctance to take on traditional roles and guilt over rejecting them . . . between the sense of independence Western society offers and the sense of obligation they feel not only to their parents, but to their parents' cultural values. And even as they strive for independence, they confront a society that often type-casts Asian women as meek and submissive. In I Love You, Dad by Grace Song . . . a young Asian woman tries desperately to put her conflicted feelings down on paper for her dying father.
```

### Performance text (classify this)

```text
Dear Dad,

I don't know why I'm writing this letter to you. It's probably because writing is easier than making you sit down with me for a serious father-daughter talk, since it's difficult for me to freely display my emotions around you. We discuss politics, religion, and education, but I can't remember ever saying "I love you" and giving you a warm embrace. I guess I thought that getting good grades in school was the best way of expressing my affection. Then, three months ago, you were diagnosed with liver cancer and I didn't know what to say. I've watched you sitting on the couch with a blank stare out the window, trying to conceal your worries and fears.

Although we're close, we never had the kind of relationship where I could tell you about a new guy I met, or ask you for advice about problems I was having with close friends. Our relationship revolved around what was going on at school for instance, how many scholarships I could obtain in university. You encouraged me to strive for excellence in all aspects of my life and you always tried your best to give me everything I ever needed or wanted. We've shared good times, aside from the roughest period of my life when our relationship nearly ended.

Looking back I regret the grief I caused you but I hope you realize that the tension between us was largely due to generational differences. I know that my naiveté was a huge factor, but it was the pressure of learning to assimilate into two worlds bringing the mutually exclusive cultures (the East and the West) together- that was so overwhelming.

I didn't think you could understand what I was going through. Listening to your stories, it seemed like you were used to living according to a set of rules that everyone accepted. For instance, in Korea, students woke up bright and early to study and, not surprisingly, their typical day ended the way it began. They just studied more. Unlike our rela-tionship, parents and their children shared the same mindset and methods of discipline, and the kids generally did as they were told. Immigrating to Canada wasn't easy. You set foot on foreign soil and immediately confronted new ideas. As traditional Korean parents you tried to keep your customs (the entire spirit) alive by teaching me the values your parents once taught you. Miscommunication led to confusion, and our relationship turned into a never-ending tug-of-war.

You put so much pressure on me to perform well in school. If my grades slipped the tiniest bit, it was time for you to pull out the "what-is-going-on-in-your-head?" lecture. You never failed to ask if I'd surpassed a smart Jewish boy who went to my school. ("Who got better grades this year, you or him?") And then we talked about my future. I thought that by becoming some big-shot lawyer, I'd be living your dream. You said that law was "in my blood" and went on about my "grandfather who was a great litigation attorney." I was glad that you thought I had the potential to become a successful lawyer, but you exerted so much pressure on me. I retaliated from time to time, yelling, "What if I don't become a lawyer! Will that make me less of a daughter?" But as usual, you ignored my emotional outburst. I usually surrendered, totally exhausted, with a pounding headache. I didn't see the point of arguing when it felt like everything I was saying was going in one ear and out the other.

The curfew you enforced also caused friction between us. My friends would constantly ask, "Why are your parents so strict?" My first reaction was to defend you and Mom.

"They're not that bad, they let me stay out later on some nights."

Of course that was totally untrue.

I was always the first one to go home from a house party or a slumber party. I knew it was natural for parents to worry about their children, but you and Mom were so extreme, and l envied my friends, whose parents gave them more freedom.

Things started to change when I turned fifteen. Determined to break your rules, I was sneaking out of the house and meeting friends at karaoke bars and clubs. I experimented with beer and cigarettes, and started to hang out in predominantly Asian crowds. You forbade me to date because you thought it would distract me from my schoolwork, so I began to date people behind your back.

The guys I usually dated were either school dropouts or guys who were on the verge of failing out. My closest girlfriends were shallow, materialistic, and unmotivated to go to school. For some reason, though, I longed for their company. It was comforting to be in the presence of other young, second-generation Asian kids. They seemed to understand me in ways that you couldn't. When I came home, I wore a mask that concealed my true identity. Upon entering the house, the adventurous and humorous girl would disappear, instantly transforming into a quiet and submissive daughter.

I could see it in your eyes when I turned sixteen. You were worried. I was no longer the daughter you once knew. I had become somebody you barely recognized. To take control of the situation, you would deliver long-winded speeches at dinner table every night (if I were home). You eventually disconnected all the phones in the house, tore up all of my friends' pictures, and made me a prisoner in my own house. I kicked and screamed and spat evil words in your face; still, you didn't flinch. At the time I thought you wanted to make me mis-erable, when, really, you were saving me from failure.

In my self-absorbed state, I never considered the hardships you endured together so I was happy. You didn't make me pay for groceries, you paid my rent, and I never had to cook my own meals. While you and Mom were busy providing for me, I made you suffer.

I remember the night you told me to get out of the house. Mom cried silently, but refused to interfere, aware that it would probably cause more damage. In the heat of anger, I left home with one backpack slung over my shoulder, and you didn't stop me. Instead, you slipped away into your room, defeated.

Eventually, Mom found out where I was staying and, in a tired voice, she asked me to come back home. When I did, she burst into tears and told me that 1 was killing you. Every day, she said, you came home and walked straight toward the cupboard where the alcohol was kept. The condition of your liver worsened, but you didn't care. Drinking cased your mind and washed your sorrows away. You didn't say much to me when I came back, but Mom told me that you cried for the first time in a long time while I was gone.

Looking in the mirror, l saw an unhappy girl, fraught with anger, confusion, and guilt. l was headed in the wrong direction, and deep down inside, I knew that you were right. I needed to take control of my future. I needed new friends. I needed to start living for myself and not for others. At twenty-one, I haven't finished growing up, but I'm changing for the better. Aware that all of my actions have consequences, I now know that if I'm not careful, life can easily turn into a reckless roller-coaster ride.

During the last couple of years, since you've been fighting your illness, we've switched roles. Now that you are weaker and more vulnerable, I've taken on some of your responsibilities. I seldom have time to hang out with friends because I'm so busy helping you and Mom buy this or pick up that, but I don't mind. It's my turn to take care of you. Sometimes I feel like the cancer is my fault, and that your drinking was intensified by my wrongdoings, but I've gradually learned to change my perspective. Dwelling on the past is pointless, and right now, I just want to make sure that you're healthy today and tomorrow.

Thank you for your unconditional love, and for saving me from following the wrong path in life. You never wanted to give up on me, and you have done everything in your power to see me grow up to become a responsible and caring adult.

ln the past our struggles drove us apart, but now, our experiences have brought us closer than ever. l will never lose hope in you, Dad, just as you never lost hope in me. I love you.

Grace
```

---

## IC-2264: The Idiot Girl and the Flaming Tantrum of Death

- Title: The Idiot Girl and the Flaming Tantrum of Death
- Author (byline): Laurie Notaro
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Prose
- Record type: Program
- Speaker labels in the text: LAURIE, HUSBAND
- Teaser before the introduction: Yes
- Spoken words (computed): 1205
- Already set (do not supply): none

### Source block (context only)

```text
Author: Howard Kern
On-Line Transcript:
(excerpts from 25 Things My Mother Taught Me)
https://www.poemhunter.com/poem/25-things-my-mother-
taught-me/
Publisher: Poem Hunter.com
Date (Month/Year): Aug 8, 2009
Author: Laurie Notaro
Book: The Idiot Girl and the Flaming Tantrum of Death
(Pg 228-241)
ISBN: 978-1400065035
Publisher: Villard
Date (Month/Year): June 2008
```

### Introduction (context only: never use it for content warnings)

```text
Is it possible to see your mother [or grandmother] as a person – an entirely separate entity apart from her relationship to you? A person who sees the world through a totally unique and possibly quirky lens. A person full of humor, personality and an outrageousness all her own. Will you grow up to be like her? Laurie Notaro paints a vivid picture of herself as an older woman, navigating life in a college town that will make every young person stop and wonder, “What Flaming Tantrums of Death” is my own mother [or grandmother hiding? After all, she does drive a Prius . . .

Idiot Girl and the Flaming Tantrum of Death by Laurie Notaro
```

### Performance text (classify this)

```text
My mother taught me TO APPRECIATE A JOB WELL DONE: “If you’re going to kill each other, do it outside. I just finished cleaning.”

My mother taught me LOGIC: “If you fall out of that swing and break your neck, you’re not going to the store with me.”

My mother taught me MEDICAL SCIENCE: “if you don’t stop crossing your eyes, they are going to get stuck that way.”

But most of all, my mother taught me WISDOM: “When you get to be my age, you’ll understand.”

LAURIE: (Pg 228-241) My advice to you is that unless you really want to know just how old you are, a college campus is the last place you’d ever want to be. I was entirely unprepared for what I saw the first time I went to pick my husband up at the university. (in shock, jaw dropping) Those children are naked!

HUSBAND: It was cold this morning. You should have seen what happens on a hot day. It looks like lunchtime at a Roman bathhouse.

LAURIE: Why doesn’t someone do something?

HUSBAND: (laughing) Like what?

LAURIE: I don’t know. Institute a ‘clothing mandatory’ rule? Napkins are not apparel! I would never wear that! She could at least have two bandanas, one for each chichi!

HUSBAND: The returning adult students don’t dress like that. They dress like you.

LAURIE: (to audience) (sound effect) And just like that, with a long squeak and several pops, I felt the air dribble out of my coolness balloon, stopping every now and then to catch its breath.

HUSBAND: When was the last time you were on a college campus?

LAURIE: I don’t know . . . Probably . . .

HUSBAND: Things have changed. You have insurance now AND you drive a Prius!

LAURIE: (defensively) So?!

HUSBAND: Can’t be bad a** in a Prius.

LAURIE: Whatever . . . (to audience) But I had already realized that was true – in a Prius, no matter how you cut it, you have the ferocity of Lovey Howell in a floppy straw hat holding a mai tai. And besides, Eugene [Oregon] is a quiet little town full of old hippies, college professors, and solar-energy enthusiasts, naming their children insidiously damaging names [like] Ptolemy, Star and Alchemy. Eugene was ideal, until that day when I saw what youth really looked like instead of the way I remembered it.

I didn’t feel any different than I did when I was 20. Okay, okay, maybe not 20. Thirty. I don’t feel any different from when I was thirty. But then again, I bought a HUD house in a bad neighborhood across the street from a lady with a shelter’s worth of diseased cats. 35. YES. Thirty-five. I don’t feel any different from when I was 35. (to husband) I am still cool.

I loved my age now. I loved where I was and I loved driving a Prius. Several days later I was driving that same Prius back from the market. I was going about thirty miles per hour; so I braked a couple of times because Priuses are rather quiet cars and are no friend to the blind, people using iPods, people on cell phones and, sadly, squirrels. My concern, however, was not good news to the shiny, black Volkswagen Jetta behind me, which, to be frank, was acting a little like a bull, I’m a cow, and there’s been an inappropriate amount of drinking going on.

I descended the hill and approached the street where I needed to make a right, put on my blinker, slowed down, and started to make the turn when the Jetta passed me, honking loudly, and the passenger – a college-aged hippie, screamed out the passenger window, “What the F___?” and threw her hands up. At me!

She was young, I was not, and I was driving a Prius. To her, insulting me was the safest thing in the world. However . . .

The old lady in the spinless car who was hitting her brakes every ten seconds to keep the children and squirrels safe was the same girl who lived for nearly a decade in a craptastic neighborhood where she chased packs of wild dogs off her porch, hired local drug addicts as handymen and was entirely unafraid of two privileged brats in a brand-new German car.

The brazen hippie chick in a black shiny Jetta had just activated the FLAMING TANTRUM OF DEATH.

Backstory: The Flaming Tantrum of Death was born one afternoon after witnessing one of the most spectacular hissy fits in world history. After a former acquaintance of mine decided that writing impolite bulletins about people and posting them on the Internet would be a productive use of spare time, there was no response from anyone targeted in the tirades. So, the author e-mailed the bulletins to those being insulted, including me, to ensure that they were seen – “Just in case you didn’t notice my Flaming Tantrum of Death, here it is!”

Now, you can either become offended or see it as the high-caliber, Las Vegas -style entertainment that it is. The Flaming Tantrum of Death was spellbinding and spectacular in its absurdity. It raised anger and revenge to a new plateau, and with proper usage, it is something to aspire to, mixing 7th grade rage with the resilience of Tempur-Pedic technology. In awe of its inspiring power, I decided to take possession of it, deliver it from evil and use it only for good.

If you’re wondering what a Flaming Tantrum of Death looks like in its physical form, it very much resembles me abandoning that right-hand turn and furiously flipping my car around to follow a shiny black Jetta and the hippies inside it, who were laughing . . . laughing . . . . LAUGHING at Lady Prius until they saw her directly behind them in their rearview mirror (evil laugh) They were stuck at a red light and never once thought that Lady Prius had the ability to terrorize anyone.

The Flaming Tantrum of Death progressed to its second stage. I laid on my horn. (sound effect) (cackling) Don’t you love honking? You’re so good at it, you little honkers! How ‘bout I honk this horn until I get out of this fussy Prius, come over there and rip the hippie dreadlocks off your head?! (to audience) We all know I probably wasn’t going to do that, but it sounded so good and dramatic, I had to say it.

Initially, both simply sat there dumbfounded as the horn blared until they decided upon their method of retaliation: the weapon of mass destruction known as “interpretive dance.” (demonstrate) They began moving their arms and torsos from side to side and all around. They were dancing!

(yelling) Is that all you’ve got? You’re going to DANCE at me? Big horn honkers, “What the F___?” screamers, brazen tailgaters can only DANCE at me? Well dance to this! (horn blaring) And I laid on the horn again until the light turned green. They ran the next red trying to get away from me. I guess they were tired of dancing.

Now, I was fully aware that the next day’s front-page headline was most likely to read: PRIUS OWNER NEEDS ANGER MANAGEMENT THERAPY AND A HUG, but I could not care less.

And just for the record, I am still looking for that car. It’s a mall enough town. I’ll find it. I happen to have some fire tantrum left in me – just enough to make some hippies dance.
```

---

## IC-2265: If Life is a Bowl of Cherries, What am I Doing in the Pits?

- Title: If Life is a Bowl of Cherries, What am I Doing in the Pits?
- Author (byline): Erma Bombeck
- Work: Not specified
- Publisher: Fawcett
- Publication date as stated: Mar 1985
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1839
- Already set (do not supply): none

### Source block (context only)

```text
Author: Erma Bombeck
ISBN: 978-0449208397
Publisher: Fawcett
Date (Month/Year): Mar 1985
```

### Introduction (context only: never use it for content warnings)

```text
Dear Cathie and children everywhere . . .

Mothers are just normal people, really. We don’t pretend to be perfect or to have all the answers to childrearing. Why, throughout the years, there are a lot of aspects of children for which I profess complete ignorance. For example . . .

If Life is a Bowl of Cherries, What am I Doing in the Pits? By Erma Bombeck
```

### Performance text (classify this)

```text
Dear Mrs. Bombeck,

I do not understand Mothers.

How come my Mom can hit anyone anywhere in the house at any distance with a shoe?

How can she tell without turning her head in the car that I am making faces at my brother in the back seat?

How can she be watching television in the living room and know that I am sneaking cookies in the kitchen?

We think it is spooky the way the phone rings and before we even pick it up she says, “Five mintues!”

Since you write about kids all the time, we thought you could explain Moms to us.

Sincerely, Cathie Haven’t I always loved Whatshisname the best?

A women starts thinking of a name for her baby from the minute she knows she is carrying one. She will write it out, say it aloud, try it out on her friends and embroider it on little shirts. When the baby is born she will whisper the name softly in its ear, write it on dozens of announcements and file in in the courthouse records.

A few years and a few kids later, she can’t remember who you are.

I’ve heard mothers go through ten or twelve names before they get lucky and hit the right one. (Once I wore my P.J.s wrong side out and my mom, thinking it was a name tag, called me Dr. Denton for a week.)

Children seem to think there is something Freudian in the entire exercise. The old if-my-mother-really-loved-me-she’d-remember-my-name trauma. This is hogwash. I love Marc . . . Mary . . . Mike . . . Mil . . . Massa . . whatshisname with the same affection as I love Bet . . . Bronc . . Evely . . . Mar . . . Tri . . . you know who you are.

Our neighborhood psychiatrist bears me out. He said there is nothing you can generalize from mothers who can’t put a name to their children right off the bat.

It used to be a good day for me when I could remember what I called them for, let alone remember who they are.

In talking with a young married [man] the other day, it was revealed that he was one of seven children and not once when he was growing up was he ever called by his real name. “I guess it was because there were so many of us,” he said, “that it confused my mother.”

I hated to shoot his theory down, but for a long while I was an only child and still got Sara . . Bet . . Mild . . Vir . . Edna. Finally, in desperation, my mother would shout, “How long do I have to call you before you answer?”

I’d yell back, “Until you get it right.”

“Was I close?” she’d shout.

“Edna was somewhere in the neighborhood.”

“I always like Edna,” she mused. “I should have named you that.”

“Then why did you name me Erma?”

“Because it was easy to remember.”

At what age is a child capable of dressing himself?

Some say when a child can reach the clothes hamper without falling in, he is ready to assume responsibility for what he wears.

A child develops individuality long before he develops taste. I have seen my kid straggle into the kitchen in the morning with outfits that need only one accessory: an empty gin bottle.

There is always one child in the family who thrives on insecurities and must have her emotional temperature taken every five minutes. I call it the “Parade of the Closet.” Beginning at 7 a.m. she will appear at breakfast fully clothed and ready for school. Before the cereal has stopped exploding in the bowl, she has disappeared to her room and is in another complete outfit. Four words from her mother (“You look nice today”) and she is off again to her bedroom in tears for still another complete change.

She plays the same musical clothes until she runs out of clothes/the bus leaves/her mother is instutionalized . . . whichever ever comes first.

There is always the kid who has an aversion to clean clothes. He is allergic to creases in trousers, socks that have soft toes, underwear that is folded, and sweaters you can sniff without passing out. He’s the child who always applauds the Ring Around the Collar commercials.

The opposite is the youngster who neither desires what is in his closet nor what is in the dirty clothes hamper. He wants what has to be ironed. I have always said, “If I had nothing in my ironing bag but a diaper, that kid would wear a top hat and go to school dressed as the New Year.”

Last year, we allowed our children to pack their own suitcases for our vacation. One wore a baseball cap and a pair of brown corduroys for an entire week. (We told everyone he had brain surgery.)

Another brought one coat . . . and old army jacket belonging to his father. (He looked like a deserter from the other side.) The other one packed one pair of shoes . . a red-white-and-blue pair of sneakers with stars. The only time he didn’t look out of place was under a basket in a coliseum.

Last week, all three of my children looked worse than usual as they headed for the door. “Why do all of you look so rotten today?” I asked. “Are you in a school play or something?”

“No, we’re having our class pictures taken.”

It figures.

Who killed apple pie?

It’s a frightening feeling to wake up one morning and discover that while you were asleep you went out of style.

That’s what happened to millions of housewives, who one day looked into their mirrors and said “I do not feel fulfilled putting toilet seats down all day.”

Women were sick of pushing buttons, besides, the buttons were pushing back. There was a housewife in Michigan who was vacuuming her carpet one morning and leaned over to pick an object off the floor. Her hair was pulled into the machine by the underside brush roller, causing her to fall on top of the vacuum and sustain electrical shock to the left side of her head.

They no longer brought the theory, advanced by a British Medical Association, that doing housework was the secret to female longevity and that all that exercise would prolong life.

As I was on my knees one afternoon, hoisting the bunk beds on my back and trying to put the slats back into the grooves, my husband asked, “What are you doing down there?”

“Prolonging my life,” I said dryly.

What I always wanted to do was run away from home. You all know the feeling. You diet for two weeks and gain three pounds. You break your bottom to get to a White Sale only to discover that all they have left are double top sheets, single contour bottom and King pillowcases.

Your best friend (whom you have always trusted) calls and tells you she just found out how to bake bread.

Some wise guy just wrote “HELP” in the dust on the draperies.

You pick up a movie magazine in the supermarket with headline reading JACKIE ONASSIS’ SPENDING HABITS SUGGEST MENTAL DISORDER and realize you’ve had the same disorder for years.

The supermarket just discontinued your silverware pattern and you spend forty minutes ironing a linen dress and it doesn’t fit you anymore.

Then one day in a leading magazine, I saw a story called, “Today’s Women on the Go.”

At the top of the article was a picture of a well-stacked blonde at construction site with a group of men around her while she reads blueprints to them. I noted her shoes were coordinated with her Gucci yellow hard hat.

The second picture showed her in a pair of flowing pajamas standing over the stove while her husband tossed the salad and her children lovingly set the table.

It made me want to spit up.

I wanted to be “on the go.” (I was half-gone already.) Imagine! Every morning going off to carpetland . . . to fresh bread for lunch . . . to a phone that wasn’t sticky with grape jelly . . . to perfume behind each knee that spelled madness to stock boys.

And I said to myself, “There, but for the grace of a babysitter go I.”

Once I made up my mind, I interviewed sitters for six months. It’s depressing when you realize no one wants to be paid for what you’ve been doing for years for nothing.

Other women, I was to discover, had the same problem. A friend of mine who is a registered nurse said she had a shattering experience. She found a “gem” who was willing to sit with her children if she left explicit instructions. The first day she left the following note:

Greg gets 1 tsp of pink medicine in refrigerator at 8 A.M. and before lunch. He has impetigo, so wash your hands good with soap and water and don’t let him use anyone else’s glass.

Paula has to be taken to the potty every two to three house. There’s a potty seat upstairs and a small chair in Rec. Room.

Don’t let dog in the chewing gum. He craves it but has to be taken to the vet to remove. He gets pills once a day (no birth control) for slight infection. Get Frank (who is in an out all day long) to hold him so he will not bite.

Take messages. Don’t use toilet in utility room. It bubbles. If you have questions, call me.

When she arrived home, the door was marked with lamb’s blood and there was a large quarantine sign tacked on it. The sitter had fled.

Who is I. Dunno?

Ever since I can remember, our home has harbored a fourth child-I. Dunno. Everyone sees him but me. All I know is, he’s rotten.

“Who left the front door open?”

“I. Dunno.”

“Who let the soap melt down the drain?”

“I. Dunno.”

“Who ate the banana I was saving for the cake?”

“I.Dunno.”

Frankly, I. Dunno is driving me nuts.

He’s lost two umbrellas, four pairs of boots and a

bicycle. He has thirteen books overdue from the library, hasn’t brought home a paper from school in three years and once left a thermos of milk in the car for three weeks.

The other day the phone rang. I ran from the mailbox, cut my leg, tore off a fingernail in the door and got to the phone in time to see my son hanging up. “Who was it?” I asked breathlessly. “I. Dunno. He hung up.”

When I told my neighbor about it she said, “Cheer up. I’ve had an invisible child for years.”

“What’s his name?”

“Nobody.”

“Is he rotten?”

“He makes Dennis the Menace look like a statue. He cracked the top of an heirloom candy dish, tears up the paper before anyone gets to read it, and once when I was driving the car pool, he nearly knocked me senseless with a ball bat.”

“Ha!” I said bitterly, “you should have seen I. Dunno. He left thirteen light burning the other night when he went out. I don’t know how much longer I can stand it.” This morning at breakfast, I said to my husband,

“Who wants liver for dinner this evening?” He looked up and said “I dontcare.” That can only mean one thing. I. Dunno has a brother.
```

---

## IC-2266: I’m Listening as Hard as I Can

- Title: I’m Listening as Hard as I Can
- Author (byline): Terry Galloway
- Work: With Wings: An Anthology of Literature By and About Women With Disabilities
- Publisher: Feminist Press
- Publication date as stated: 1987
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2159
- Already set (do not supply): none

### Source block (context only)

```text
Author: Terry Galloway
Book: With Wings: An Anthology of Literature By and
About Women With Disabilities
ISBN: 978-0935312621
Publisher: Feminist Press
Date (Month/Year): 1987
```

### Introduction (context only: never use it for content warnings)

```text
There are over 500,000 deaf people in the United States, but the only time we hear about deaf culture is when someone is making up sign language at presidential funerals, rioting, or teaching kids on Sesame Street. As a result, the average person has no idea what being deaf involves, and therefore life can get downright weird for anyone who can't hear like the rest of society. Now imagine how less accepting society was of differences in the 1960s . . . that’s when Terry Galloway turned ten and the voices of everyone she loved began to disappear. I’m Listening as Hard as I Can by Terry Galloway
```

### Performance text (classify this)

```text
At the age of twelve I won the swimming award at the Lions Camp for Crippled Children. When my name echoed over the PA system the girl in the wheelchair next to me grabbed my hearing aid and shouted, “You won!” My ear quaking, I took the cue. I stood up straight – the only physically unencumbered child in a sea of braces and canes – affixed a pained but brave grin to my face, then limped all the way to the stage.

Later, after the spotlight had dimmed, I was overcome with remorse, but not because I’d played the crippled heroine. The truth was that I was ashamed of my handicap. I wanted to have something more visibly wrong with me. I wanted to be in the same league as the girl who’d lost her right leg in a car accident; her artificial leg attracted a bevy of awestruck campers. I, on the other hand, wore an unwieldy box hearing aid buckled to my body like a dog halter. It attracted no one. Deafness wasn’t, in my eyes, a blue-ribbon handicap. Mixed in with my envy, though, was an overwhelming sense of guilt; at camp I was free to splash in the swimming pool, while most of the other children were stranded at the shallow end, where lifeguards floated them in lazy circles. But seventeen years of living in the “normal” world has diminished my guild considerable, and I’ve learned that every handicap has its own particular hell.

I’m something of an anomaly in the deaf world. Unlike most deaf people, who were either born deaf or went deaf in infancy, I lost my hearing in chunks over a period of twelve years. Fortunately I learned to speak before my loss grew too profound, and that ability freed me from the most severe problem facing the deaf – the terrible difficulty of making themselves understood. My opinion of deafness was just as biased as that of a person who can hear. I had never met a deaf child in my life, and I didn’t know how to sign. I imagined deaf people to be like creatures from beyond: animal-like because their language was so physical, threatening because they were unable to express themselves with sophistication – that is, through speech. I could make myself understood, and because I had a talent for lip-reading it was easy for me to pass in the wider world. And for most of my life that is exactly what I did – like a black woman playing white, I passed for something other than what I was. But in doing so I was avoiding some very painful facts. And for many years I was inhibited not only by my deafness but my own idea of what it meant to be deaf.

My problems all started when my mother, seven months pregnant with me, developed a serious kidney infection. Her doctors pumped her full of antibiotics.

Two months later I was born, with nothing to suggest that I was anything more or less than a normal child. For years nobody knew that the antibiotics had played havoc with my fetal nervous system. I grew up bright, happy, and energetic.

But by the time I was ten I knew, if nobody else did, that something somewhere had gone wrong. The people around me had gradually developed fuzzy profiles, and their speech had taken on a blurred and foreign character. But I was such a secure and happy child that it didn’t enter my mind to question my new perspective or mention the changes to anyone else. Finally, my behavior became noticeably erratic – I would make nonsensical replies to ordinary questions or simply fail to reply at all. My teachers, deciding that I was neither a particularly creative child nor an especially troublesome one, looked for a physical cause. They found two: I wasn’t quite as blind as a bat, but I was almost as deaf as a doornail.

My parents took me to San Antonio, where I was examined from ear to ear. Finally a verdict was delivered: “Congenital interference has resulted in a neural disorder for which there is no know medical or surgical treatment.” My hearing loss was severe and would grow progressively worse.

I was fitted with my first hearing aid and sent back home to resume my childhood. I never did. I just had turned twelve, and my body was undergoing enormous changes. I had baby fat, hairy legs, and thick pink cat-eye glasses. My hearing aid was about the size of a small transistor radio and rode in a white linen pouch that hit exactly at breast level. It was not a welcome addition to my pubescent woe.

As a vain child trapped in a monster’s body, I was frantic for a way to survive the next few years. Glimpsing my reflection in mirrors became such agony that I acquired a habit of brushing my teeth and hair with my eyes closed. Everything I did was geared to making my body more inhabitable, but I only succeeded in making it less so. I kept my glasses in my pocket and developed an unbecoming squint; I devised a smile that hid two broken front teeth, but it looked disturbingly like the grin of a piranha. But the hearing aid was a different story. There was no way to disguise it. I could tuck it under my blouse, but then all I could hear was the static of cotton. So I resigned myself: a monster I was, a monster I would be.

I became more withdrawn, more suspicious of other people’s intentions. I imagined that I was being deliberately excluded from schoolyard talk because the other children didn’t make much of an effort to involve me – they simply didn’t have the time or patience to repeat snatches of gossip ten time and slowly. Conversation always reached the point of ridiculousness before I could understand something as simple as “The movie starts at five.” (The groovy shark’s alive? The moving stars that thrive?) I didn’t make it to many movies.

For the first few years my parents were as bewildered as I was. Nothing had prepared them for a handicapped child on the brink of adolescence. They sensed a whole other world of problems, but in those early stages I still seemed so normal that they just couldn’t see me in a school for the deaf. They felt that although such schools were there to help, they also served to isolate. I have always been grateful for their decision. Because of it, I had to contend with public schools, and in doing so I developed two methods of survival: I learned to read not just lips but the whole person, and I learned the habit of clear speech by taking every speech and drama course I could.

That is not to say my adolescent years were easy going – they were misery. The lack of sound cast a pall on everything. Life seemed less fun than it had been before. I didn’t associate that lack of fun with the lack of sound. I didn’t begin to make the connection between the failing of my body and the failings of the world until I was well out of college. I simply did not admit to myself that deafness caused certain problems – or even that I was deaf.

From the time I was twelve until I was twenty-four, the loss of my hearing was erratic. I would lose a decibel or tow of sound and then my hearing would stabilize. A week or a year later there would be another slip and then I’d have to adjust all over again. I never knew when I would hit bottom. I remember going to bed one night still being able to make out the reassuring purr of the refrigerator and the late-night conversation of my parents, then waking the next morning to nothing – even my own voice was gone.

My professors were frequently alarmed by my almost maniacal intensity in class. I was petrified that I’d have to ask for special privileges just to achieve marginal understanding. My pride was in flames. I became increasingly bitter and isolated. I was terrified of being marked a deaf woman, a label that made me sound dumb and cowlike, enveloped in a protective silence that denied me my complexity. I did everything I could to hide my handicap. I wore my hair long and never wore earrings, thus keeping attention away from my ears and their riders. I monopolized conversations so that I wouldn’t slip up and reveal what I was or wasn’t hearing; I took on a disdainful air at large parties, hoping that no one would ask me something I couldn’t instantly reply to. I lied about the extent of my deafness so I could avoid the stigma of being through “different” in a pathetic way.

It was not surprising that in my senior year I suffered a nervous collapse and spent three days in the hospital crying like a baby. When I stopped crying I knew it was time to face a few things – I had to start asking for help when I needed it because I couldn’t handle my deafness alone, and I had to quit being ashamed of my handicap so I could begin to live with its consequences and discover what (if any) were its rewards.

When I began telling people that I was really deaf I did so with grim determination. Some were afraid to talk to me at any length, fearing perhaps that they were talking into a void; others assumed that I was somehow an unsullied innocent and always inquired in carefully enunciated sentences; “Dooooooo youuuuuu driinnk liquor?” But most people were surprisingly sympathetic – they wanted to know the best way to be understood, they took great pains to talk directly to my face, and they didn’t insult me by using only words of one syllable.

It was, in part that gentle acceptance that made me more curious about my own deafness. Always before it had been an affliction to wrestle with as one would with angels, but when I finally accepted it is an inevitable part of my life, I relaxed enough to do some exploring. I would take my hearing aid off and go through a day, a night, an hour or two – as long as I could take it – in absolute silence. I felt as if I were indulging in a secret vice because I was perceiving the world in a new way – stripped of sound.

Of course I had always known that sound is vibration, but I didn’t know, until I stopped straining to hear, how truly sound is a refinement of feeling. Conversations at parties might elude me, but I seldom fail to pick up on moods. I enjoy watching people talk. When I am too far away to read lips I try reading postures and imagining conversations. Sometimes to everyone’s horror, I respond to thing better left unsaid when I’m trying to find out what’s going on around me. I wasn’t to see, touch, taste, and smell everything with reach; I especially have to curb a tendency to judge things by their smell – not just potato salad but people as well – a habit that seems to some people entirely too barbaric for comfort. I am not claiming that my other senses stepped up their work to compensate for the loss, but the absence of one does allow me to concentrate on the others. Deafness has left me acutely aware of both the duplicity that language is capable of and the many expressions the body cannot hide.

Silence is not empty; it is simply more sobering than sound. At times I prefer the sobriety. I can still “hear” with a hearing aid – that is, I can discern noise, but I can’t tell you where it’s coming from or if it is laughter or a faulty drain. When there are many people talking together I hear a strange music, a distant rumbling in my consciousness. But when I take off my hearing aid at night and lie in bed surrounded by my fate, I wonder, “What is this – a foul subtraction or a blessing in disguise?” For despite my fears there is a kind of peace in the silence – albeit an uneasy one.

There is, after all, less to distract me from my thoughts.

But I know what I’ve lost. The process of becoming deaf has at times been frightening, akin perhaps to dying, and early in life it took away my happy confidence in the image of a world where things always work right. When I first came back from the Lions Camp that summer I cursed heaven and earth for doing such terrible wrong to me and to my friends. My grandmother tried to comfort me by promising, “Honey, God’s got something special planned for you.

But I thought, “Yes. He plans to make me deaf.”
```

---

## IC-2267: The Impossible Knife of Memory

- Title: The Impossible Knife of Memory
- Author (byline): Laurie Halse Anderson
- Work: Not specified
- Publisher: Viking Books for Young Readers
- Publication date as stated: Jan 2014
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: HALEY, DAD, RANDY
- Teaser before the introduction: No
- Spoken words (computed): 1853
- Already set (do not supply): none

### Source block (context only)

```text
Author: Laurie Halse Anderson
ISBN: 978-0670012091
Publisher: Viking Books for Young Readers
Date (Month/Year): Jan 2014
KS State Qualifier
```

### Introduction (context only: never use it for content warnings)

```text
Two million American fought in Iraq and Afghanistan. Most who came back describe themselves as physically and mentally healthy. They move on; the war recedes. But studies suggest that between 20-30% of returning veterans suffer from PTSD, a mental-health condition triggered by some type of terror; or a traumatic brain injury, when the brain is jolted so violently it collides with the inside of the skull, causing psychological damage.

Every war has its after-war: depression, anxiety, nightmares, suicidal thoughts. The wars in Iraq and Afghanistan created roughly 500,000 mentally wounded American veterans.* Haley’s father is one of them.

The Impossible Knife of Memory by Laurie Halse Anderson
```

### Performance text (classify this)

```text
HALEY: (Pg 8) At the end of the last street, past a forgotten cornfield and the ruin of a barn, sat the house that I was supposed to call “home.” My father wanted me to remember. . . (Pg 9) we were back and living in Gramma’s old house.

DAD: (Pg 8) Are you sure you don’t remember it, Hayley Rose?

HALEY: I shook my head but kept my mouth shut. It made him sad when I talked about how hard I tried not to remember. (Pg 9) A few days after we moved in, Daddy got unstuck from time again. The past took over. All he heard were exploding IEDs and incoming mortar rounds; all he saw were body fragments, like an unattached leg still wearing its boot, and shards of shiny bones, sharp as spears. All he tasted was blood.

These attacks had been getting worse for months. They were the only reason I went along with his ridiculous plan to quit trucking and settle down into a so-called “normal life.” I let him think that he was right, that spending my senior year in a high school instead of riding shotgun in his big rig was a practical and exciting idea. Truth? I was terrified.

(Pg 6) I swallowed the fear. It’s always there - fear - and if you don’t stay on top of it, you’ll drown.

DAD: (Pg 301) (to audience/self) The good soldier swears to kill. Fire the cannon, mount the barricade, lock and load. Smell your brother’s blood on your shirt. Wipe your sister’s brains off your face. Die, if you have to, so they’ll live. Kill to keep your people alive, live to kill some more. Odysseus had twenty years to shed his battle skin. My grandfather left the battlefield in France and rode home in a ship that crawled across the ocean slowly so he could catch his breath. I get on a plane in hell and get off, hours later, at home. I try to ignore Death, but she’s got her arm around my waist, waiting to poison everything I touch.

HALEY: (Pg 248) [Here’s the] short clean version [of my dad]: two tours in Iraq, two tours in Afghanistan. Earned the Purple Heart. The IED that blew up his truck and his brain and his career. Months in the hospital, then the big welcome home, dog tags turned in, army days over.

(Pg 249-250) He homeschooled me. Unschooled me. It was kind of awesome for a while: him driving, me reading out loud, the two of us talking about everything, fractions and evolution, Abraham Lincoln’s cabinet and which Hemingway book is the best.

He got arrested in Arkansas last year. Public drunkenness. He was only in the jail overnight, but he came out completely set on moving back here. Said I needed to go to a regular school to get ready for college. I thought the move would be good for him, that he’d hook up with old friends and get a decent job. Instead it’s like a bomb had started ticking in his head.

[Dad’s] worst yesterdays played on a constant loop in his head and he couldn’t (or he wouldn’t) stop paying attention to them. At least on the road, there had been times when we’d outrun memories. Now they had us surrounded and were closing in.

(Pg 11) (calling out) Dad? [I’m home]! I walked toward his door and gently knocked. I waited. This was where he should ask me how my day went or if I had homework or what I wanted for dinner. Or he could tell me what he felt like eating, because I could cook. Or he could just open the door and talk. (through the door) Dad? Did you stay home again?

DAD: It’s been a bad day, I’ll try harder tomorrow, princess.

HALEY: (Pg 58) The dining room table was covered with newspapers, cleaning rods, a double-ended breech-brush, used patches, and rags stained with barrel oil, solvents, and gunpowder. What makes him want to clean all of [his guns]. Does he think he’s going to need them? (Pg 60) How many of the girls in my gym class had to clean up gunpowder and barrel oil after school?

(Pg 87) Dad hated talking about the war and never did it sober. Half the time he didn’t even want people to know he was a vet. Strangers often said things like, “Thank you for your service,” because they meant it and they thought that was the right thing to do, but the problem was it set off a series of detonations inside my father that sometimes ended with him punching a wall or the face of a jerk in a bar. The worst was when he accidentally found himself in conversation with the family member of a soldier who had been killed. The sadness in their eyes would blow another hole in his brain and then he’d go dead quiet for days. [Transition: Randy, one of Dad’s army friends, called me to ask how things were going.]

RANDY: (Pg 105-107) Is Andy seeing a counselor or a shrink?

HALEY: He won’t go. [Did you know he’s] afraid of bridge overpasses? [He’s afraid of] snipers. [And] he’ll take huge detours around dumpsters or trash cans ‘cause they could be hiding an IED. He knows that’s stupid, but knowing doesn’t stop the panic attacks. Why is he getting worse? He’s been back for years.

RANDY: The blood is still flowing. His soul is still bleeding. That’s a lot harder to fix than a busted-up leg or traumatic brain injury.

HALEY: (to audience) (Pg 308-309) [There were days] Dad wouldn’t cooperate. We argued about everything: my attitude, the weather, the smell of the garbage. There were the days when he’d disappear in his head without saying a word. He couldn’t sleep more than an hour or two at a time without waking up or shouting or screaming. He always apologized for that, once he calmed down.

[A month went by. I came home after classes to find] (Pg 328) the door was locked. Dad hadn’t locked it in weeks.

(to herself) Get a grip and stop catastrophizing. (Pg 329) That’s when I smelled something burning. Saw smoke rising from the fire pit. I walked over to it, thinking maybe he’d started a fire to cook hotdogs or something. He’d been burning his uniform. The half-melted boots smoldered in the middle.

I ran to the living room window, cupped my hands to cut down on the glare. The living room had been trashed [and] my father was curled into a ball on the floor. Blood on his face. Blood staining the carpet under his head.

NONONODADDYDADDYNO!!!! (Pg 330) [Then] The body moved. Uncurled. It sat up, wiped its face on the front of its T-shirt.

DAD: (crying) He’d dead . . . Roy.

HALEY: (Pg 331) The war. Another dead friend. Is there anything worse than watching your father cry? When I was a kid, I watched him scaling walls, running miles in the heat wearing full gear. My dad was a superhero who made the world safe. He went overseas with his troops and chased the bad guys out of the mountains so that little kids over there could go to school. (Pg 332) I patted his back, waiting for the storm to pass.

(Pg 335) When the sun went down, he opened a bottle [of whiskey], sat me on the couch, and made me listen to stuff I’d heard a million times before: ambushed foot patrols, IEDs ripping open vehicles and bodies, suicide bombers living in ghost villages. The private who was shot in the neck. The guy who removed his helmet to wipe the sweat off his head, and the sniper who blew that head into a red mist that hung in the air for a moment before it dropped to the dirt and soaked the ground.

(Pg 336) Around quarter after four, he puked all over the carpet and finally passed out. I laid him on his side, put a bucket by his head, and threw a towel over the mess so the dog wouldn’t eat it. I took a long shower to wash off the tears and the stench of whiskey puke. (Pg 339) I [called] the cops.

(Pg 343) In the end, they called an ambulance because Dad was so dehydrated. (Pg 344) He was alive. I’d been afraid of a day like this forever, but he was alive. At a hospital, getting help. This was a good thing, right? It was all that mattered . . . except . . . What now?

(Pg 360) In [the coming] weeks, Daddy was down to one bottle of Jack every three days. He didn’t explode or cry. He spent his nights writing letters at the dining room table. (Pg 361) A Christmas tree turned up in our living room the morning of Christmas Eve. [There was] (Pg 371) a big, red box [with] dozens of crisp, sealed, sharp-edged envelopes. Every envelope had my name on it. In the top-right corner was a date. Half of the envelopes were dated my birthday. The other half were dated December 25, and the years that followed those dates stretched for decades into the future. (Pg 368) I shivered . . . [and] my shivering turned into shaking. I pulled out a faded blue bandanna that held two gold rings, one man-sized, the other a little smaller, and one Purple Heart.

(Pg 370) He wasn’t in the kitchen or the living room or the dining room . . . so where? (pause) (Pg 377) I know where he is . . . I know how he’s going to do it. (pause) [But] I didn’t know I was right until I turned off Route 15 onto Quarry Road and saw boot prints that cut through the snow all the way up the hill. (Pg 378) From the top I saw him, my father, a dark lump sitting in a hollow of snow a foot away from where the earth ended.

(Pg 379) (softly) Daddy, please. (Pg 381) I know you have nightmares and you saw horrible things, but . . . (choking up) but I don’t care. I want my dad back. I want you to be brave again, the way you used to be! (she moves closer to the edge with her dad)

DAD: (Pg 382) Go back, Hayley Rose, you’re too close to the edge.

HALEY: (to her dad) You [don’t] understand. I’ve been standing on the edge with you for years. (Pg 383) That feeling you have, Daddy, that you want me to be safe, you want me to stay alive? I feel that way about you all the time. If you kill yourself, then every minute of your life has been wasted. When I got stuck or confused, you used to say, “We’ll figure it out.” I love you, Daddy. I know we’ll figure it out! (Pg 391) You can’t do this, you can’t quit!

(to audience) (Pg 385) If this were a fairy tale, I’d stick in the “Happily Ever After” right here. But this was my life, so it was a little more complicated than that.

(Pg 386) The fairly solid rim of snow [that] I’d been standing on collapsed. Dad broke three ribs when he grabbed me. . . I blew out my knee and got a grade two concussion. (pause) [But] out there on the edge, the spinning of the Earth had slowed to give us the time we needed to start finding each other again.

(Pg 387) Dad called his version of Happily Ever After “Good Enough for Today.” (pause) Some days were better than others. (Pg 386-387) Dad was transferred to a VA rehab place after the hospital. By the time he came home, he’d lost twenty pounds, and looked ten years older, but the shadows had left his face. And he, [finally], remembered how to smile.
```

---

## IC-2268: Incendiary

- Title: Incendiary
- Author (byline): Chris Cleave
- Work: Not specified
- Publisher: Anchor
- Publication date as stated: Sept 2006
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: WIFE, HUSBAND, RADIO ANNOUNCER, BOY, MENA, NURSE
- Teaser before the introduction: Yes
- Spoken words (computed): 2004
- Already set (do not supply): none

### Source block (context only)

```text
Author: Chris Cleave
ISBN: 978-1400096688
Publisher: Anchor
Date (Month/Year): Sept 2006
```

### Introduction (context only: never use it for content warnings)

```text
On July 7, 2005, during the morning rush hour, four bombs were detonated in the center of London killing 52 and injuring over 770 others. Three IED’s exploded in underground stations and the fourth on a bus. The attacks were inspired by al-Qaeda and its ideology.

On that same day, Chris Cleave's debut novel was published: the fictional story of what happens after a bomb kills more than 1,000 people in a London soccer stadium as told through the eyes of a young mother. It is hard to imagine an uglier “literature echoes reality” coincidence.

Incendiary by Chris Cleave
```

### Performance text (classify this)

```text
WIFE: (Pg 29-30) (to husband) I wish you wouldn’t take the boy to the game. He’s too little. The violence makes me nervous.

HUSBAND: (laughing) Crowd violence at a football game. That’s a laugh considering I defuse bombs for a living. Listen love, football crowds aren’t how they used to be. It’s a family game now and anyway I’m a copper. I’m a big bloke I can handle myself.

WIFE: It’s not you I’m worried about. It’s the boy. He is 4 years old [and] still sleeps with Mr. Rabbit. (holds and interacts with Mr. Rabbit throughout the selection) (Pg 11) (to audience) I sewed Mr. Rabbit myself he was purple with green ears.

HUSBAND: (Pg 30) Oh for Christ’s sake, said my husband. You think I don’t look after him? You think I’d let anyone touch a hair on his head? I’d kill them first.

WIFE: Alright. But it still makes me nervous.

HUSBAND: Everything makes you nervous.

WIFE: (to audience) And he was right. Oh, god, he was absolutely right. I could feel death rushing towards us. (Pg 39-40) It was May 1st and the sky was blue and it was nice and warm just like you want it to be on May Day. My husband was carrying the boy on his shoulders and both of them were grinning like idiots. They were wearing their Arsenal shirts because it was Saturday -- the big day. They climbed in our old Astra and drove off. I never saw my husband or my boy again.

RADIO ANNOUNCER: (Pg 73) THE NUMBER OF CONFIRMED DEAD FROM THE MAY DAY ATTACK HAS RISEN TO 966 WITH DOZENS MORE STILL MISSING OR IN CRITICAL CONDITION.

WIFE: (Pg 76-77) They reckon 200 people died straight away -- blown to bits by the fragmentation bombs. I hope my husband and my boy were part of that 200. That’s a funny thing to say isn’t it? But that is what I hope. Because the 200 people who died straight away didn’t have to suffer.

After the first blast anyone who could still run did run. There was an inferno. Phosphorus raining down all around. It set fire to the seats. To the stands. To the clothes and skin of the fallen bodies. They reckon 500 people were crushed and burned to death while fire rained down. They would swing open the ambulance doors and blood would be an inch deep on the floor. They said some of the (pause) things (pause) that arrived on the ambulance stretchers didn’t really look like anything.

Dear Osama . . . (Pg 73) They kept calling it The Catastrophe. The BBC never did work out what to call the thing you’d blown up. After days of calling it the Emirates Stadium or Gunners Park, they gave up and started calling the whole thing May Day. Everyone did. Like you hadn’t just blown up a football ground you’d blown a hole straight through our calendar. I felt like I’d fallen through the hole.

BOY: (Pg 228) Mummy . . . Mummy, why don’t you help me?

WIFE: (Pg 4) You can see what a boy really is from the shape of the hole he leaves behind. I want you to feel that hole in your heart, Osama. Stroke it with your hands and cut your fingers on its sharp edges.

(Pg 163) Everything happened in the spring and it never stopped for one second. It was dirty and sad and anyone who wasn’t blown up and burned -- It was like we all became animals again. You could look at people on the bus and you’d almost see the fur bristling under their nice clean clothes. After May Day everyone was nervous. It wasn’t just me anymore.

(Pg 27) They say you are a FIEND, Osama, but like I say I don’t believe a word of it. I’ve seen you in your videos. You give me the shivers and you look like a gentleman. They say you believe in paradise. They say you believe that if your people kill anyone innocent then you’re doing them a favour because they will go to be with Allah. I wouldn’t know about that. My husband didn’t believe in Allah he believed in his kid and Arsenal football club.

(Pg 27-29) I always liked the football but my husband and my boy were mad for it. The fun used to start the night before. Before we put the boy to bed my husband would run around the flat with the boy on his shoulders. They would sing *1 NIL TO THE ARSENAL till the upstairs neighbours banged on the ceiling. After the singing the boy would be laughing and giggling like a lunatic. We couldn’t get him to sleep. (flashback to a memory)

BOY: Mum! Mum, mum, mum, come quick there’s something in my room.

WIFE: What is it? I’d say.

BOY: Nothing (giggling) I fooled you!

WIFE: (to audience) He was 4 years and 3 months old. You couldn’t be cross with him. That boy had such a beautiful smile. He was just pleased to be alive. (to boy) Go to sleep, little monster or you’ll be tired for the big game.

BOY: But I’m not sleepy mum,

WIFE: Go to sleep or I’ll have to fetch your father.

BOY: I’m not scared of him! My dad is the best dad in the world! He’s better than. Than. Than.

WIFE: Than what? Eh, little monster? What’s your dad better than?

BOY: (erupting in giggles again) Monkeys! My dad is better than monkeys!

WIFE: (Pg 11) (beat, then to audience) In the night my boy’s room smelled of boy. Boy is a good smell it is a cross between angels and tigers. My boy slept on his side sucking Mr. Rabbit’s paws. He went everywhere my boy went. (Pg 37) I’ve gone through a lot of changes since then Osama but if you looked very carefully and the light was right, I expect you could still see the memory of that happy time in me. Hidden but not quite invisible (beat) (Pg 11) Mr. Rabbit survived.

still have him. His green ears are black with blood and one of his paws is missing. (beat) (Pg 101) A lot of things survived because they were trapped under bodies. (gasp)

(Pg 29) It sounds silly, Osama, but sometimes I’m pleased your people blew them both up together. (Pg 117) All they found was their teeth and Mr. Rabbit.

(Pg 311) The only thing going through my head? My boy screaming with Mr. Rabbit in his pocket and his Arsenal shirt in flames.

BOY: (Pg 262) Mummy, save me!

WIFE: (Pg 295) (puts hands to her mouth to stifle a silent scream) His lovely ginger hair burned. Thick black tar dripping down his face. His skin raw with burns and one of his eyes boiled white as an egg.

(Pg 209) Mr. Rabbit stained black with my boy’s blood -- scars where his skin had burned through and his stuffing roasted brown and hard as crackling. (Pg 137-138) [They say] the Arabs are different from us. In the Iran/Iraq war they sent children to walk across the minefields. To clear a path so the grown ups could go and gas each other. They gave each kid a little metal key to paradise. The kids hung those keys around their necks. The grown-up Arabs told the little Arab children that there weren’t enough landmines to send all the kids to paradise. So the little children actually ran. Kids will believe anything you tell them . . . (long beat) (Pg 71-73) Well Osama I sometimes think we deserve whatever you do to us. Maybe you are right maybe we are infidels. Even when you blow us into chunks we don’t stop fighting each other. I suppose you were sitting out on the rocks before dawn listening to the goat bells when one of your men came over to you. Did he say, “Hey boss turn on the radio! We did it! We blew up Arsenal’s shiny new stadium1” ? Did you smile? Did you turn on the radio and listen to the death toll rise? (beat)

I fell unconscious and I stayed that way for 3 days. When I woke up in hospital. The sheets were very stiff and white. The radio was on in the ward. 912 dead it said. At first they said 700 dead but it went up and up. The survivors wouldn’t stop dying you see. They had so many bits blown off them they couldn’t really help themselves. There was a BRAVE 82 YR OLD GRAN in the bed across from me. She’d lost both eyes at the stadium and she was singing 1 NIL TO THE ARSENAL again and again and again. (covers ear, cradles Mr. Rabbit and wimpers, then gathers herself to continue the story)

(Pg 86-88) Mena was my favourite nurse. She was a nice girl. She was from the East. Kazakhstan or Uzbekistan or one of those Stans anyway. She’d sit on the end of my bed and we’d watch the sun rising. Mena used to hold my hand while we looked out over the city.

MENA: So many people down there. So many people under this sunrise. And all those people want is to get through today.

WIFE: Mena was like that. Philosophical. (contemplative beat) I’d definitely of killed myself if it hadn’t of been for her. (beat) Each morning [we] watched what they were doing to London. First, they stopped boats using the river. They just stopped them so you couldn’t blow up the Houses of Parliament, Osama. They drained the life out of the river till it was just an empty vein with police boats drifting up and down it like white blood cells. (Pg 102) For a whole week after May Day the airports stayed closed.

(Pg 88) What really changed the view though was the barrage balloons shining silver in the rising sun. It gave me the shivers. Mena gripped my hand and I could see the goose bumps on her arm.

MENA: This is grotesque. The world has gone crazy.

WIFE: It makes sense to me. I reckon it’s to stop them flying planes into the tall buildings.

MENA: (Pg 89-90) We turn London into a fortress? As if that could possibly stop the terror.

WIFE: (to audience) I could feel Mena’s hand trembling. I watched a tear run down the side of her nose. It stopped on her upper lip. (to Mena) If you had kids, you’d be all for anything they can do against the terrorists. It doesn’t matter if it’s logical when it’s your own kids.

MENA: It matters if you’re Asian. Look, my family is Muslim right. Do you have any idea what it’s been like for us? I don’t think you can imagine how it feels for me just to walk to work since May Day. To see the hate in people’s eyes when they look at me. I have become the enemy. There’s this one cafe I walk past on my way here. This morning this old man, he must have been 80, was reading the paper and the headline on the paper was THE CRUELTY OF ISLAM. He looked up when I walked past and he sneered at me. He actually curled his lips. That is the nature of this madness. It fills the sky with barrage balloons and people’s eyes with hate.

WIFE: (Pg 91-92) Mena gave me this lovely smile and touched her right hand to her heart.

MENA: I must go . . .

WIFE: I’ll see you tomorrow. (to audience) But I didn’t. In fact, I never did see Mena again. The next morning the sun turned up just like normal, but Mena didn’t. A new nurse came instead. (to nurse) What happened to Mena?

NURSE: They stopped her working. Muslim wasn’t she? Security risk. They suspended all of them from working as of midnight. This country’s finally starting to get it. Don’t get me wrong. I’m sure 99 percent of the Muslims are fine but if you can’t trust some of them you can’t trust any of them can you?

WIFE: But they can’t just stop all the Muslims from working.

NURSE: Oh, they haven’t. Only the ones who fly planes and work in hospitals or have access to information.

WIFE: (with great sorrow) The new nurse didn’t hold my hand. She didn’t watch the sunrise with me. (Pg 136) You really think it was Islam that killed my husband and my boy? [Mena] was the gentlest woman I ever met. Her god wasn’t a bombing god.

BOY: (Pg 271) Mummy, why are you crying?

WIFE: (to Mr. Rabbit) Mummy’s not crying darling. Mummy’s fine. She’s just got something in her eye. (Pg 235-236) Before you bombed my boy, Osama, I always thought an explosion was such a quick thing but now I know better. The flash is over very fast but the fire catches hold inside you and the noise never stops. . . I live in an inferno where you shiver with cold. This life is a deafening roar . . . but listen. You could hear a pin drop.
```

---

## IC-2269: Infinity

- Title: Infinity
- Author (byline): Sarah Dessen
- Work: Sixteen: Stories about that Sweet and Bitter Birthday
- Publisher: Three Rivers Press
- Publication date as stated: May 2004
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2105
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sarah Dessen
Book: Sixteen: Stories about that Sweet and Bitter
Birthday
ISBN: 978-1400052707
Publisher: Three Rivers Press
Date (Month/Year): May 2004
```

### Introduction (context only: never use it for content warnings)

```text
Are you good at making decisions? Are you able to make them in a timely fashion? And are the outcomes you get what they should be? What is the process you use to make a decision? Is a decision based on your gut feeling? Or perhaps what your heart tells you? Or in those few rare cases – even what the head tells you?

We all make many decisions every day. Some are quite trivial, while others can change the direction of our lives. But the bottom line is . . . as long as the decision is your own, it doesn't matter how long it takes you to make it. In Infinity by Sarah Dessen, a young girl ponders her ability to make her own choices. Infinity by Sarah Dessen.
```

### Performance text (classify this)

```text
Lately I don't dream about Anthony. I dream about the rotary.

Most people don't even know what rotaries are. That's because most towns have those most modern of inventions, stoplights, to deal with traffic. Not here. Instead, some genius decided however many years ago to put in this big circle, with all the main roads feeding into it, then sat back to watch people crash to their deaths as they attempted to negotiate it.

My first experience with the rotary was when I was about seven. "Oh my God," my mother said, poking her glasses up the bridge of her nose, which she always does when she's really nervous. "What is this?" The answer came in the form of a loud, impatient beep from behind us.

"I'm merging!" she shrieked. And we were merging, pretty well, slowly easing into traffic. In fact, we were almost relaxed when we had to try to get back out; no easy trick, as there were many cars merging in. We got stuck on the inside track for two more turns, watching our exit go by, before my mother panicked and just sort of jerked the wheel, sending us in its general direction. And that was when the station wagon hit us.

The entire episode ended with a ticket, our insurance rates rising, and my mother swearing to never do the rotary ever again, which seemed somewhat overdramatic, until we realized that she meant it.

My boyfriend, Anthony, is a year older than me. He's good at the rotary, but he understands my hesitation. In fact, since I got my [learner’s] permit, we've spent a lot of time going in circles together, practicing. We started late at night, when it was pretty much deserted . . .

"Okay, now the first thing you're gonna do is stop and look to the left here Okay now," Anthony said. "Just ease out."

I did. Just as my mother had, all those years earlier. But this time there was no one coming; it was dark. No problem. But still my heart was beating hard, thumping against my chest, even as I picked up speed.

"See?" Anthony said. "Piece of cake, right?"

"Right," I said. We passed all the exits once, then started through again. Of course this was okay, I thought. Like a merry-go-round, only faster. But it was a trial run. And trial runs are always easier.

Finally Anthony pointed toward the beach route exit. I slowed down, pulling up into a space right behind the lifeguard stand. Then I cut the engine. "You did good tonight," Anthony said. And then he leaned over and kissed me. I knew he would. I knew because we'd been practicing this, too, all this time, trial run after trial run. As with the rotary, what came next was obvious. And scary. And, it seemed, inevitable.

I'd been with Anthony for more than six months. He wanted to sleep with me. He hadn't come out and said it, but he didn't really have to. Us having sex would be a natural progression: Like moving from learner's permit to license, there's only one thing left. And so I have this choice. To either merge in or take the long way home. ******

"I'm so proud of you!" That was my mother when I came out of the DMV office, holding my new license. "You know, you don't have to do the rotary right away."

"I know," I said. We'd already discussed this during the weeks I'd had my permit, when she'd officially taught me all of her extended shortcuts. "But I think I should just go ahead and get it over with."

My mother had gotten accustomed to taking the long way everywhere: It wasn't even a burden for her anymore. That's the thing about habits. And fears. At first they might seem like trouble, but eventually they just fold in, becoming part of the fabric. I longed for the simple, solid logic of traffic lights, no decisions necessary: Green means go, red means stop, yellow means slow down or run the light-make up your mind, though, because time's a-wasting.

I could do this. It wasn't any different from all those nights I'd merged and circled the rotary with Anthony: The traffic was just a little heavier. I told myself I wasn't just doing this for me, but for my mother as well. The traffic was picking up now, the last intersection coming up in front of us. The engine seemed to grind as I downshifted, the other drivers pressing in around me.

There was a honk a few cars back-not at us, but loud nonetheless-and I have to admit it threw me, sending a quick hot flush up the back of my neck. It didn't help, of course, that my mother gasped in a breath loud enough for me to hear over the wind whistling through my not-quite-shut window. And just like that, I lost my confidence, my hand reaching up to hit the right tum signal as if it had made the choice all by itself.

"It's okay," she said as we breezed past a few neighborhoods, with only two left turns, one access road, and a shopping center parking lot to traverse before arriving home. "You'll do it when you're ready." But I was angry with myself for ducking out. It seemed a bad way to begin things, with a false start, a last-minute abort so close to takeoff. As if I'd come this far, right to the brink, and in pulling back set a precedent that would echo, like the sound of my mother's gasp, next time.

I avoided the rotary for a week and a half. There were several almosts, most of them with Anthony in the car, pep-talking me like a motivational coach. "Be the road!" he urged me as we coasted up to the ROTARY AHEAD signs. But always, I took that last possible right turn, while Anthony would just shake his head, easing an elbow out the window, and say nothing.

His urging was gentler, but no less insistent, when the car was off and we were alone together at the beach. "I love you, I love you," he'd whisper, and I'd feel that same hot flush, traveling up from my feet, the adrenaline rush that was a mix of fear and longing. We'd gotten very close, but again, I pulled back. Scared. It seemed ludicrous that I was unable to follow through with anything, as if from sixteen on I was doomed to be ruled by indecision.

"I just don't understand why you don't want to," he asked me one night as we sat looking at the water. There was no gray here, no compromise. We'd come up so quickly on all or nothing that it blind-sided me, a mere glint out of the comer of my eye before full impact.

"I want it to be right," I told him.

"How can this not be right?" He sat up straighter, jutting a finger up at the windshield. "Moonlight? Check. Crashing waves? Check. I love you? Check. You love me? ... "

It took me a second, just a second, to realize it was my tum to say something. "Check," I said quickly, but he glared at me and let his finger drop, as if this explained everything.

As the days passed, and I found myself consistently taking the long way everywhere, I got frustrated with all these decisions. A part of me wanted to barrel into the rotary blindfolded, pushing the gas pedal hard, and let whatever was going to happen just happen, anything for it to be over. The same part sometimes was so close to giving into Anthony's pleadings, wanting to finally just relax against the seat and let him do what he wanted, just give it all up and finally ease myself of these burdens.

Scenario number one, of course, was stupid: I'd cause a multicar pileup and kill myself. As far as number two, well, it was harder to say. What would change? Maybe there wouldn't be visible damage, dented bumpers or crumpled hoods. But something in me would be different, even if no one else could tell. Like a car that's been wrecked and fixed, but the frame stays bent. Just because you don't see it doesn't mean something isn't there. Or gone.

The fall carnival appeared in one afternoon, with rides and a midway and the huge Ferris wheel. I used my money to buy a funnel cake and tickets for [for Anthony and me].

Behind us was a guy with his daughter, who looked to be about eight. She had a big stuffed lion under her arm and was gripping her dad's hand, staring up at the Ferris wheel as it moved lazily above us.

"Now, honey," the man said, squatting down beside her, "you don't have to go on it if you don't want to. Because it might be scary."

"I want to," she said. I watched her face, the careful way she studied the ride as it came to a stop, I envied her for knowing exactly what she wanted. But it was easy when you're little, I figured. Not so many choices.

[Then] we were at the very top. Anthony was pressing against me, hardly caring that this was not the place, not the time. All those nights at the beach, when I'd pushed him away, I hadn't known exactly why, just that it hadn't felt right. But as my view from high up narrowed, I realized that my relationship with Anthony had done the same, going from a wide endless horizon of possibilities to one pinpoint of a destination. I wanted to have choices, to know that I could, at any moment, still take the long way home. Sure, there was a quick way to anywhere. But sometimes, when you took the shortcut, you missed the view.

"I love you," he whispered in my ear. "I want you." But it wasn't enough. As I pushed him away, I knew that [the “right”] time would never come. Anthony was tired of losing at this game. If he couldn't have me, he'd find an easier prize. The ride hadn't even come to a full stop when he pushed the safety bar away from us. Then he stomped down the stairs, pushing past all the people lined up for the next ride while I climbed out slowly, taking my time, telling myself to pay attention to how the earth felt beneath me and not take it for granted anymore.

I'd driven, and Anthony was gone, lost in the crowd. Even though I'd only been driving for a couple of weeks, it already felt more natural. Maybe all it took, in the end, was the time to let the new soak in. To stand in the face of change and size it up, acquaint yourself, before jumping in. It was all the pressure that was so hard, those little nudges forward, poke poke poke. If you just backed off and let it come to you, it would.

When I finally made it to the light, I hit my blinker, signaling the left tum that would lead me around the shopping mall and through two neighborhoods before depositing me onto my own road. It was the way I'd always gone, up until now, but this time I didn't feel that burning burst of shame in it, knowing I was taking the easy way out. I just remembered the view from up high, the way all the roads led to one another eventually. It didn't matter which route you took, as long as you got home.

There was that burst of freedom in realizing that my choice was okay. But even so, at the last minute, I turned my wheel to the right, surprising even myself, and shifted into second as the rotary came up into my sight. This was normally the moment I was dumb scared, hands shaking, but this time I only moved closer, pressing my shoulders back against the seat as if taking the scariest and most exhilarating of rides. I glanced in my rearview [mirror] and saw the Ferris wheel. Another circle, representing a kind of infinity that I was only beginning to understand. I turned the wheel, leaning into the first curve, feeling that rush of accomplishment and speed. It was happening so fast, but I was there, right there, alive, wanting this moment to be like brass rings and Ferris wheels and all the circulars of this life and others, never ending.
```

---

## IC-2270: Inside the Tower

- Title: Inside the Tower
- Author (byline): Stephanie Burgis
- Work: Jabberwocky
- Publisher: Wildside Press/Prime Books
- Publication date as stated: Sep 2005
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1208
- Already set (do not supply): none

### Source block (context only)

```text
Author: Stephanie Burgis
Book: Jabberwocky
ISBN: 978-0809550623
Publisher: Wildside Press/Prime Books
Date(Month/Year): Sep 2005
```

### Introduction (context only: never use it for content warnings)

```text
The story of Rapunzel is a familiar one . . . Beautiful girl, imprisoned in a tower by her mother to keep her safe from the evils of the world . . . rescued by a handsome prince and of course . . . . they lived happily ever after. But the real relationship between Rapunzel and her mother is a much more intriguing, Some people call this the “Back story.” Stephanie Burgis calls it Inside the Tower.
```

### Performance text (classify this)

```text
Rapunzel grew into the most beautiful child beneath the sun. When she was twelve years old, the enchantress shut her into a tower, which lay in a forest, and had neither stairs nor door, but quite at the top was a little window. When the enchantress wanted to go in, she placed herself beneath this and cried,

"Rapunzel, Rapunzel,

Let down thy hair to me."

Rapunzel had magnificent long hair, fine as spun gold, and when she heard the voice of the enchantress she unfastened her braided tresses, wound them round one of the hooks of the window above, and then the hair fell twenty ells down, and the enchantress climbed up by it.

Light streams into the single tower room, onto the bed. Too much light, too bright, too harsh. I don't want to see my mother's emaciated face so clearly; I can't bear to see the hollows that formed in her cheeks while I was gone, or her dark eyes, staring at me with such fierce longing.

I've hated my mother for half my life, but watching her die is killing me. I stand up and hurry to the window, nearly running to grab the heavy curtains. Outside, warm sunlight streams down onto the forest below us. This was my only view for years, my only outlook onto the world. Beyond the trees, the bright pennants atop the castle flap, blown by a summer breeze. The depth of my bitterness takes me by surprise when I see them.

My life is good, now. I have to remind myself of that, my hands white-knuckled around the curtains. I can't see my cottage from here; it feels like a dream from which I've too-suddenly awoken, not the reality to which I'll soon return. Back home, my husband and our children are waiting. They're eating vegetables fresh from our garden, and the youngest children are playing with the dogs all day long, then snuggling up with them on the hearth as if they're puppies themselves.

Whenever I see them like that, so tender and helpless, I feel as if my heart might break from wonder, fear, and envy. I've never experienced that freedom, that trust.

"Leave the windows open," Mother says. Her voice is cracked and weak, nothing like the harsh commanding tone I used to hear. "I need to feel the fresh air."

"Yes, Mother." I step back obediently, clenching my fists, and look away from the blue sky.

Life is carrying on outside, but here I am, back in my tower again, with the person who kept me imprisoned until I was nineteen years old.

At least she's coherent, now. When I first arrived, she was babbling, lost in the middle of one of her old hate-filled rants. I almost turned and ran.

"I remember," my mother says dreamily. "When you were a little girl, I used to braid your hair for hours. It was so soft. Like golden silk in my fingers."

I have to hold myself back from reaching up to feel my short, cropped hair. I never let it grow long anymore. "Can I make you anything to drink?" I ask. "One of your potions? If you tell me which herbs to mix—"

"No," she says. "No, I'm fine, now that you're back. Come, sit down."

She pats the mattress beside her with a blue-veined hand. Her knuckles have swollen into rocks.

Fighting all my instincts, I sit.

"We did everything together," she says. "The only person you ever wanted was me."

My mother is dying. I tell myself that. I use it to hold back the rage that wants to spill. The words of poison that want to pour out of my mouth and beat at her ravaged face the way she beat me with her fists, the first time I ever tried to find love away from her.

My prince is long-married to a suitably highborn bride. If I had known anything of the world, I would never have believed his promises.

But how could I possibly have known?

"You never even let me see anybody else," I whisper.

She blinks and pats my hand. "I kept you safe," she says. "You didn't understand. I wouldn't let anybody get close enough to hurt you."

You would never let me breathe.

I bite my lip so hard that I taste blood. "Maybe you should get some sleep," I say. "I'll work in the garden for a bit, cook us some dinner—"

"Everything outside is so dangerous," she says. Her eyes have gone unfocused; they move back and forth, searching—for what? "People everywhere. Waiting. Waiting to rob you. Hurt you. Take you away."

"Mother." I swallow. "I think you're getting too excited. Why don't you just close your eyes?"

But she doesn't seem to even hear me. "He said he would do it."

She's shivering, even though the air is warm. I reach over and pull the covers up around her. She tries to grab my hand. I pull it back.

"Who said?"

"My prince—"

"My prince!" Suddenly I'm breathing hard. I'm seventeen again, suffering the lash of her voice, her blows. "That was me, remember? My life, not yours!"

"They burned the house down," she says. "My mother, screaming. The prince and his men. They laughed. And then he looked at me."

Tears stand in her pale blue eyes, trickle down her cheeks. Nausea twists my stomach.

"You're upset," I say. "We'll talk about this later, when you're feeling better. I'll—"

"It hurt," she says, and it turns into a moan. "It hurt so much!"

"Mother—"

"And he said, if I whelped—"

"Mother, please—"

"I ran," she whispers. "I ran and ran. To a different kingdom, where he would never find me. And I built the tallest tower, to keep my baby safe. So no one could ever take her away. No one will ever hurt her. Ever."

Tears burn behind my eyes. She's gasping for breath as she talks.

"Shh," I whisper. "Please, Mother."

"But she's gone," Mother says. Her voice rises. It spirals into panic. "He took her! He hurt her! Where's she gone?" Her head jerks back; she twists it around on the pillow, eyes wild. "Where is she? Where's my daughter? Tell me! Where's my daughter? I need my daughter!"

"I'm here," I whisper. My chest is so tightly constricted, it feels like it's about to break apart.

"Stop lying to me!" she screams. "Where's my daughter?"

"It's all right." I force out the words through a throat clenched tight and burning. I reach out, through the memories. I reach through the beatings, through the suffocation and the mania. I make myself reach toward the girl who was hurt so badly, the girl who let fear warp the shape of her life.

I reach out and take her shaking hands, and I fold them between both of mine. "It's all right now, Mother," I whisper, and I watch her face tremble with longing. I look at the old woman I've been afraid of for so long. "See?" I whisper. In the distance, in the future, my husband and children are waiting for me. I'm not imprisoned. Not anymore. "I'm right here. With you."
```

---

## IC-2271: Invisible Monsters

- Title: Invisible Monsters
- Author (byline): Chuck Palahniuk
- Work: Not specified
- Publisher: W. W. Norton & Company
- Publication date as stated: Sept 1999
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1781
- Already set (do not supply): none

### Source block (context only)

```text
Author: Chuck Palahniuk
ISBN: 978-0393319293
Publisher: W. W. Norton & Company
Date (Month/Year): Sept 1999
```

### Introduction (context only: never use it for content warnings)

```text
Welcome to Lifestyles of the Rich and Famous . . . . Today we walk with one of the world’s leading fashion-models. She has or should I say had just about everything: a boyfriend, a career, a loyal best friend. But one day, driving along the freeway, a sudden "accident" leaves her with half her face, no ability to speak, and next to no self-esteem. Once the beautiful center of attention, she becomes an invisible monster, so hideous that no one will acknowledge she exists. Today’s story is one of revenge, of downfalls, of the ugliness of human nature, and of invisibility. Invisible Monsters by Chuck Palahniuk.
```

### Performance text (classify this)

```text
Where you're supposed to be is some big West Hills wedding reception in a big manor house with flower arrangements and stuffed mushrooms all over the house. This is called scene setting: where everybody is, who's alive, who's dead. This is Evie Cottrell's big wedding reception moment. Evie is standing halfway down the big staircase in the manor house foyer, inside what's left of her wedding dress, still holding her rifle. Me, I'm standing at the bottom of the stairs but only in a physical way. My mind is, I don't know where.

Nobody's all-the-way dead yet, but let's just say the clock is ticking. Not that anybody in this big drama is a real alive person, either. You can trace everything about Evie Cottrell's look back to some television commercial for an organic shampoo, except right now Evie's wedding dress is burned down to just the hoopskirt wires orbiting her hips and just the little wire skeletons of all the silk flowers that were in her hair. And Evie's blonde hair, her big, teased-up, back-combed rainbow in every shade of blonde blown up with hairspray, well, Evie's hair is burned off, too.

The only other character here is Brandy Alexander, who's laid out, shotgunned, at the bottom of the staircase, bleeding to death. What I tell myself is the gush of red pumping out of Brandy's bullet hole is less like blood than it's some sociopolitical tool. The thing about being cloned from all those shampoo commercials, well, that goes for me and Brandy Alexander, too. Shotgunning anybody in this room would be the moral equivalent of killing a car, a vacuum cleaner, a Barbie doll. Erasing a computer disk. Burning a book. Probably that goes for killing anybody in the world. We're all such products.

Brandy Alexander, the long-stemmed latte queen supreme of the top-drawer party girls, Brandy is gushing her insides out through a bullet hole in her amazing suit jacket. The suit, it's this white Bob Mackie knock-off Brandy bought in Seattle with a tight hobble skirt that squeezes her hips into the perfect big heart shape. You would not believe how much this suit cost. The mark-up is about a zillion percent. The suit jacket has a little peplum skirt and wide lapels and shoulders. The single-breasted cut is symmetrical except for the hole pumping out blood.

Then Evie starts to sob, standing there halfway up the staircase. Evie, that deadly virus of the moment. This is our cue to all look at poor Evie, poor, sad Evie, hairless and wearing nothing but ashes and circled by the wire cage of her burned-up hoop skirt. Then Evie drops the rifle. With her dirty face in her dirty hands, Evie sits down and starts to boo-hoo, as if crying will solve anything. The rifle, this is a loaded thirty-aught rifle, it clatters down the stairs and skids out into the middle of the foyer floor, spinning on its side, pointing at me, pointing at Brandy, pointing at Evie, crying.

It's not that I'm some detached lab animal just conditioned to ignore violence, but my first instinct is maybe it's not too late to dab club soda on the bloodstain. Most of my adult life so far has been me standing on seamless paper for a raft of bucks per hour, wearing clothes and shoes, my hair done and some famous fashion photographer telling me how to feel. Him yelling, Give me lust, baby. Flash. Give me malice. Flash. Give me detached existentialist ennui. Flash. Give me rampant intellectualism as a coping mechanism. Flash.

Probably it's the shock of seeing my one worst enemy shoot my other worst enemy is what it is. Boom, and it's a win-win situation. This and being around Brandy, I've developed a pretty big penchant for drama. It only looks like I'm crying when I put a handkerchief up under my veil to breathe through. To filter the air since you can about not breathe for all the smoke since Evie's big manor house is burning down around us. Me, kneeling down beside Brandy, I could put my hands anywhere in my gown and find Darvons and Demerols and Darvocet 100s.

This is everybody's cue to look at me. My gown is a knock-off print of the Shroud of Turin, most of it brown and white, draped and cut so the shiny red buttons will button through the stigmata. Then I'm wearing yards and yards of black organza veil wrapped around my face and studded with little hand-cut Austrian crystal stars. You can't tell how I look, face-wise, but that's the whole idea. The look is elegant and sacrilegious and makes me feel sacred and immoral. Haute couture and getting hauter. Fire inches down the foyer wallpaper.

Me, for added set dressing I started the fire. Special effects can go a long way to heighten a mood, and it's not as if this is a real house. What's burning down is a re-creation of a period revival house patterned after a copy of a copy of a copy of a mock-Tudor big manor house. It's a hundred generations removed from anything original, but the truth is aren't we all? Just before Evie comes screaming down the stairs and shoots Brandy Alexander, what I did was pour out about a gallon of Chanel Number Five and put a burning wedding invitation to it, and boom, I'm recycling.

It's funny, but when you think about even the biggest tragic fire it's just a sustained chemical reaction. The oxidation of Joan of Arc.

Still spinning on the floor, the rifle points at me, points at Brandy.

Another thing is no matter how much you think you love somebody, you'll step back when the pool of their blood edges up too close.

Except for all this high drama, it's a really nice day. This is a warm, sunny day and the front door is open to the porch and the lawn outside. The fire upstairs draws the warm smell of the fresh-cut lawn into the foyer, and you can hear all the wedding guests outside.

Brandy, she says, "There's no way the Bon March will take this suit back." Evie lifts her face, her face a finger-painting mess of soot and snot and tears from her hands and screams, "I hate my life being so boring!" Evie screams down at Brandy Alexander, "Save me a window table in hell!" Tears rinse clean lines down Evie's cheeks, and she screams, "Girlfriend! You need to be yelling some back at me!" As if this isn't already drama, drama, drama, Brandy looks up at me kneeling beside her. Brandy's aubergine eyes dilated out to full flower, she says, "Brandy Alex-ander is going to die now?" Evie, Brandy and me, all this is just a power struggle for the spotlight. Just each of us being me, me, me first.

The murderer, the victim, the witness, each of us thinks our role is the lead. Probably that goes for anybody in the world. It's all mirror, mirror on the wall because beauty is power the same way money is power the same way a gun is power. Anymore, when I see the picture of a twenty-something in the newspaper who was abducted and sodomized and robbed and then killed and here's a front-page picture of her young and smiling, instead of me dwelling on this being a big, sad crime, my gut reaction is, wow, she'd be really hot if she didn't have such a big honker of a nose.

My second reaction is I'd better have some good head and shoulders shots handy in case I get, you know, abducted and sodomized to death.

My third reaction is, well, at least that cuts down on the competition.

If that's not enough, my moisturizer I use is a suspension of inert fetal solids in hydrogenated mineral oil. My point is that, if I'm honest, my life is all about me. My point is, unless the meter is running and some photographer is yelling: Give me empathy. Then the flash of the strobe. Give me sympathy. Flash. Give me brutal honesty. Flash.

"Don't let me die here on this floor," Brandy says, and her big hands clutch at me. "My hair," she says, "My hair will be flat in the back." My point is I know Brandy is maybe probably going to die, but I just can't get into it. Evie sobs even louder. On top of this, the fire sirens from way outside are crowning me queen of Migraine Town.

The rifle is still spinning on the floor, but slower and slower.

Brandy says, "This is not how Brandy Alexander wanted her life to go. She's supposed to be famous, first. You know, she's supposed to be on television during Super Bowl halftime, drinking a diet cola in slow motion before she died." The rifle stops spinning and points at nobody. At Evie sobbing, Brandy screams, "Shut up!" "You shut up," Evie screams back. Behind her, the fire is eating its way down the stairway carpet. The sirens, you can hear them wandering and screaming all over the West Hills. People will just knock each other down to dial 911 and be the big hero. Nobody looks ready for the big television crew that's due to arrive any minute.

"This is your last chance, honey," Brandy says, and her blood is getting all over the place. She says, "Do you love me?" It's when folks ask questions like this that you lose the spotlight. This is how folks trap you into a best-supporting role. Even bigger than the house being on fire is this huge expectation that I have to say the three most worn-out words you'll find in any script.

Just the words make me feel nauseas. They're just words is all. Powerless. Vocabulary. Dialogue. "Tell me," Brandy says. "Do you? Do you really love me?"

It's than that the fire eats its way down the stairway carpet to where Evie is sitting. Evie screams to her feet and pounds down the stairs in her burnt up white high heels. Naked and hairless wearing wire and ashes Evie Cottrelruns out the front door.

This is the world we live in conditions change, we mutate. So of course this will be all about Brandy, Hosted by me with guest appearances by Evelyn Cottrel. I'll be here eating smoke just to document this Brandy Alexander Moment. Give me Attention *flash* Give me Adoration *flash* Give me a Break.
```

---

## IC-2272: The Isabel Fish

- Title: The Isabel Fish
- Author (byline): Julie Orringer
- Work: How to Breathe Underwater
- Publisher: Knopf
- Publication date as stated: September 2003
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2481
- Already set (do not supply): none

### Source block (context only)

```text
Author: Julie Orringer
Book: How to Breathe Underwater
ISBN: 978-1400034369
Publisher: Knopf
Date (Month/Year): September 2003
```

### Introduction (context only: never use it for content warnings)

```text
Isabel is dead . . . in fact she dies twice in this story. Once with Maddy and once at the hands of Maddy’s brother Sage. But it is Maddy, a normal 14-year-old little sister, who tells her story of just how hard it is to deal with the death of a friend – especially when your brother holds you responsible for that death.

And the story unfolds slowly -- as if underwater -- in The Isabel Fish by Julie Orringer
```

### Performance text (classify this)

```text
Crime and punishment. That is the pattern between my brother Sage and me. A quiet private criminal justice system, with Sage as judge, jury, jailer and executioner. Our system allows multiple punishments for the same crime. If, in a real court, I’d been proven guilty of killing Isabel, I would have gotten my punishment and been left to live with it. In the world of Sage and me, however, I must pay and pay.

I am the canker of my brother Sage’s life. He has told me so in no uncertain terms. Tonight on the way to our first scuba class, he can’t stop talking about the horrible fates that might befall me underwater. This, even though he knows how scared I am after what happened last November.

“You could blow out your eardrums,” he says. “Or your lungs might implode from the pressure. Did you know that one in twelve scuba divers gets attacked by sharks?”

Sage is sixteen, plays drums, smokes unfiltered cigarettes, and drives his beat-up black Pinto to school every morning. He sees me as a problem, a younger and more stupid version of himself, and a girl, not popular, sort of plain. He used to be cruel to me in the normal sibling sense, but now it’s worse. He is far from forgetting Isabel, and who can blame him? She’d been his girlfriend for six months before the accident, and it’s only been four months since. Four months is a short time in the grand scheme of things, shorter than it’s taken me to grow twenty-six fighting fish from eggs for my science experiment.

I got the eggs one month before the accident. When I showed them to Isabel, red and clumped together in a small tank, she laughed and said she could hardly believe that bunch of caviar would become real animals. Well, guess what? They are now. Every day I feed them and give them liquid vitamins and alter their blood pressure with drugs, and still get my homework done and make it to school just as if I were fully recovered. Which I’m not, in many ways.

My parents are aware of this. As a kind of remedy, they came up with the idea of a spring-break trip to St. Maarten in the Dutch Virgin Islands. They’ve been talking about the problem between Sage and me for months, our mom trying to give us counseling, our dad distracting us with jokes. Now scuba lessons, in preparation for the trip.

What our parents don’t understand is that their son has become cruel and unusual, and he shows no sign of changing. “Anyone could f*** with your tank underwater,” he says. “One turn of a knob, that’s all it would take.”

I remember being in Isabel’s car with the water coming in, filling my mouth with its cold fishy taste, and me groping in the dark for my seat belt, my lungs already hot and tight, and Isabel in the seat beside me bleeding into the darkness. Sage must know what I’m thinking about, but he won’t look at me or say anything more.

At the YMCA I follow Sage into the lobby, where the chlorine smell of the pool stops me cold. Sage doesn’t notice. He doesn’t even look back. He just disappears down the hall toward the men’s locker room, leaving me standing there alone. Tonight, for the first time, I’ll begin to know what my fish have known all their lives: how to breathe underwater. When I get calm enough I go to the women’s locker room and find an empty locker. When I go to St. Maarten I will have my own fins, according to my father; we have already looked at examples and I have admired a translucent blue pair with a matching mask. They seem like they’d be almost invisible underwater.

Looking at those fins made it easy to imagine swimming, but now that I’m here at the Y it seems crazy. Sure, in St. Maarten there are a lot of fish you can see living their lives around coral reefs if you happen to know how to scuba. That kind of thing is attractive to an ichthyophile like me. But I am also a person who almost drowned. When my dad told me about St. Maarten, with its great diving, I wanted to ask if he and my mother were crazy. Did they really think I would voluntarily walk into the ocean and let it close over my head? “Scuba?”

“We think it’ll be good for you,” my mother said. “We think it’ll help you form positive associations with water.”

As I get into my tank suit I cannot help noticing the mistakes of my body.. My chest is too flat, my legs too skinny, and there is a scar running the length of my left thigh. Under the water, car metal sliced me in a neat line. I didn’t even feel it. Only at the edge of the pond afterward did I look down and see the blood.

I realize there are probably only ten or fifteen minutes between me and the experience of getting underwater again. For a moment I wish my mother or father were here. Then I remember I am fourteen and lucky to be alive.

But nothing has prepared me for the experience of actually seeing the pool. Sage is nowhere to be seen. I sit down on a bench and put my head between my knees to feel better. The instructor tells us we’ll have fifteen minutes of laps. But I look at my feet waving in the water and wonder if I’m going to brick. It’s one of the main reasons I didn’t want to take the class, the possibility of me freaking out and Sage having to take me home. Sage probably expects me to freak out too. . . I will not drown here with all these people watching, and me a good swimmer. I will not drown here . . . .

Finally it’s my turn. I stand at the edge of the pool and pretend there is no water behind me at all, but instead my bed with the quilt I wrap myself in when I get depressed, and there will be no moment when the water cover me, and I will not remember the plunge in the car as we hit the surface and started going down.

“Go!” cries the instructor, and I push off the edge. I plunge backward into the cold shock of water and sink almost immediately. My arms and legs go numb with panic, and my mouth fills with the bleach taste of pool water. I feels like I’m going down to that place where I was before, the cold dark pond on that November night, and if I go down father still I will reach Isabel, her hair floating mermaidlike around her.

All I could think about was how mad Sage would be on our way home. Once again I’d given him evidence of what a non-hero I am. Both of us can plainly see how I might have failed at a crucial moment, missed my chance to pull Isabel out of the car. The thing the police told him, the thing the autopsy confirmed, was that she was already unconscious and wedged into the crushed driver’s side, the steering wheel pinning her ribs. It might have been possible for me to pull her out, but if I’d tried, I might have drowned too. And she might not have survived anyway. Everyone says I did the right thing by swimming up and climbing out to run for help. Still I know Sage blames me, and in my heart I agree.

In my room, my science-experiment fish seem to be sleeping in their plastic containers. I’ve tried to learn everything they can teach me about the chemistry of anger, what makes it ebb and flow, how it can be controlled. TO be professional I tried not to name my science experiment fish, but then I realized the coincidence of there being 26 of them, one for each letter of the alphabet, and now they all have names. The Isabel fish is in the experimental group, fed a calming drug a couple times a day. The Sage fish is a control, mean and small with high blood pressure. I pity these fish, them not knowing what’s going on and being in isolation except during the aggression trials. I keep telling myself [Sage] cannot be angry at me forever, though maybe I am wrong.

I go into my bathroom, close the door, and though I don’t have time to cry, I cry anyway. [and remember . . . ]

(FLASHBACK)

I would never have gone along if I hadn’t been standing around in the garage with Sage and Isabel when Ty drove up. There was talk about going to check out a new hot tub. Ty worked weekends as a hot tub installer and knew where all the tubs were – places where people were building houses – sometimes he got the tubs hooked up weeks before the owners moved in.

Everyone was excited except me. I’d been having a great time there in the garage, and now everyone was going to leave. I turned to go inside, and that was when Isabel said, “Hey, Maddy, you can come if you want.” So I ran inside to get a suit and towel, and then we were off, all piled in Isabel’s Toyota. Isabel singing along with the radio. I felt lucky and cool and older. I took a breath and looked up at the stars. It was November.

I headed for the Jacuzzi as if this were the kind of think I did all the time. The water steamed and rolled and burbled around us. [But] then, as if he couldn’t stand that people were talking to me and acting like I belonged there, Sage had to start telling the story about my 5th birthday – the pool story. . . . I look in the pool and there’s Maddy with this peaceful expression on her face. Our mom got everyone out of the pool to go in and have cake. Everyone was like, ‘Why can’t we swim anymore/” Meanwhile, Maddy tried to act like she hadn’t don it. She still won’t admit it, will you Maddy?’ I called her the Mad Pisser that whole summer.” He wouldn’t let it rest. He kept poking me in the shoulder and saying, “Think you can hold it?” . . . until Isabel climbed out of the tub.

“Why do you have to be such an asshole?” she said.

“It was funny . . . Wasn’t it funny?”

“It wasn’t funny,” Isabel said. The next minute floodlights were flashing and a shrill alarm was screaming. The house security system had gone off. Suddenly everyone was screaming and running around. I was so scared, Isabel had to grab my hand and run us to the front of the house where her car was parked. “What about Sage?” I said.

“He can find another ride.” Then she hit the gas and we were off. We turned in at Gettyswood Townhomes. Isabel laid on the gas, and as we came around the curve near the pond I felt the jolt of the curb and a sudden hollow rush in my chest and we were airborne.

The car hit the pond nose-first. The windshield crunched and everything was dark and water poured in through the open windows, so cold it erased every part of me it touched, and suddenly it was in my mouth with its pond-scum taste and I couldn’t breathe. In the darkness I felt for Isabel, and my hands brushed something warm and soft, but I couldn’t make my fingers hold on to anything. My lungs began to burn. I shrugged out of the seatbelt and felt for the edge of the open window, pushing through, trying to kick up to where the moon wavered. I struggled through what seemed like think black hones, broke the surface, breathed, swam to the edge. Kneeling on the wet grass, I coughed out water, waiting to see Isabel come up. I screamed to her. I got up onto the numb block of my feet and ran toward the townhouse, toward a phone, shouting for help.

(END FLASHBACK)

God only know how he killed them, but when I get home from school I find eleven of my fighting fish dead, the Sage fish and Isabel fish among them. And though I don’t want to let myself cry, I do, because they’re dead beyond the reach of hope or science, and Sage is the one who did it. After dinner, I take [them] and walk the mile to the pond. It’s the first time I’ve been to the pond since the accident. Though I know the car was dragged out months ago, I imagine it there beneath the surface of the water, Isabel still trapped inside. It’s impossible to believe how gone she is, how untouchable.

On the way to scuba that night I watch Sage as he drives . . . “You can’t just not mention the fish, Sage. You can’t pretend nothing happened.”

“Maddy, I’m an asshole. I admit it.”

“You make me wish I died instead of her.”

Finally he speaks again, so quiet I have to lean close to hear him. “I can’t believe I turned out to be such a shitty person,” he says. “I wasn’t even nice to her. I was a terrible boyfriend. I got mad at her for no reason. I didn’t listen to her enough. I forgot her birthday. I made fun of her car.

“You weren’t a terrible boyfriend, I say. “Isabel loved you. I could see it.”

“We’re going to be late,” Sage says.

The instructor says we’re going to do a five-minute dive and tells everyone to get into wetsuits. We learn how to attached the regulator to the tank, how to turn on the air and how to test the regulator by pushing the purge button. The air from the tank is metallic and very dry.

Finally it is time again for all of us to get into the water. Sage moves close to me as we line up to splash in . . . me trying not to look over the edge into the mouth of the water. “Quit thinking about last time,” he says. “It’s going to be different. Practice measuring your breaths, like she told us.”

Together we fall back and splash down. When I think of Isabel this time it’s not as a mermaid but as the living girlfriend of my brother. She would have like to see us diving, Sage and me. We treat water, watching each other through our masks. I cannot see his eyes, but I can see reflected small and blue, a girl wearing swim fins and a metal tank, self-contained and breathing underwater.
```

---

## IC-2273: Juliette’s Journal

- Title: Juliette’s Journal
- Author (byline): Tahereh Mafi
- Work: Unite Me (Shatter Me)
- Publisher: Random House Books
- Publication date as stated: August 2002
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1659
- Already set (do not supply): none

### Source block (context only)

```text
Author: Tahereh Mafi
Book: Unite Me (Shatter Me)
ISBN: 978-0062327963
Publisher: Random House Books
Date (Month/Year): August 2002
```

### Introduction (context only: never use it for content warnings)

```text
In a crumbling world under the dictatorship of the Reestablishment, 17-year-old Juliette Ferrars is locked away in a cell. She is not an ordinary teenager. In fact, she is a lethal one. A touch from her can kill.

When she was fourteen, she accidentally killed a little boy. He had tripped and fallen, and Juliette was just trying to help, but people believed that she choked the little boy to death. Juliette has been locked away ever since. For the Reestablishment, she is as much a threat as she is potentially the ultimate weapon.

Juliette’s Journal by Tahereh Mafi
```

### Performance text (classify this)

```text
(Pg 177+) We had homes. Before. We bought lawn ornaments and twinkle lights and learned to ride bikes without training wheels. I remember televisions and fireplaces and porcelain sinks. I remember movie tickets and parking lots and SUVs. I remember hair salons and holidays and toothpaste commercials; ladies in high heels and old men in business suits. I remember mailmen and libraries and boy bands and balloons and Christmas trees. We ate the things we shouldn’t, spent money when we couldn’t, lost sight of the Earth we had to inhabit, and wasted . . . wasted . . . wasted everything. Food. Water. Resources.

I remember being 10 years old when we couldn’t ignore the food shortages anymore and things got so expensive no one could afford to live.

Soon the skies were gray with chemical pollution and the plants and animals were sick from genetic modification, and diseases rooted themselves in our air, our meals, our blood and bones. The food disappeared. People were dying. Our empire fell to pieces.

The Reestablishment said they would help us. Save us. Rebuild our society. Instead they tore us all apart.

I keep thinking I need to stay calm, that it’s all in my head, that everything is going to be fine and someone is going to open the door, someone is going to let me out of here. Things like this don’t just happen. People aren’t forgotten like this. Not abandoned like this. This doesn’t just happen. (SCREAMS, SCREAMS, SCREAMS, but there is no response)

(Breathless) There are a million screams caught inside of my chest but what’s the point of screaming if you’ll never be heard and no one will ever hear me in here. No one will ever hear me ever again.

It’s a strange thing, to never know peace. To know that no matter where you go, there is no sanctuary. That the threat of pain is always a whisper away. I’m not safe locked into these 4 walls, I was never safe leaving my house, and I couldn’t even feel safe in the 14 years I lived at home. ********

The asylum kills people every day, the world has already been taught to fear me, and my home is the same place where my father locked me in my room every night and my mother screamed at me for being the abomination she was forced to raise.

She always said it was my face. There was something about my face, she said, that she couldn’t stand. Something about my eyes, the way I looked at her, the fact that I even existed. She’d always tell me to stop looking at her. She’d always scream it. Like I might attack her. Stop looking at me, she’d scream. You just stop looking at me, she’d scream.

********

I don’t know when it started. I don’t know why it started. I don’t know anything about anything except for the screaming.

My mother screaming when she realized she could no longer touch me. My father screaming when he realized what I’d done to my mother. My parents screaming when they’d lock me in my room and tell me I should be grateful. For their food. For their humane treatment of this thing that could not possibly be their child. For the yardstick they used to measure the distance I needed to keep away.

I ruined their lives, is what they said to me. I stole their happiness. Destroyed my mother’s hope for ever having children again.

Couldn’t I see what I’d done? is what they’d ask me. Couldn’t I see that I’d ruined everything? I tried so hard to fix what I’d ruined. I tried every single day to be what they wanted. I tried all the time to be better but I never really knew how. ********

She put my hand in the fire once. Just to see it would burn, she said. Just to check if it was a regular hand, she said. I was 6 years old then. I remember because it was my birthday. ********

I wonder what they’re thinking. My parents. I wonder where they are. I wonder if they’re okay now, if they’re happy now, if they finally got what they wanted. I wonder if my mother will ever have another child. I wonder if someone will ever be kind enough to kill me and I wonder if hell is better than here. I wonder if I’ll ever breathe fresh air again. I wonder about so many things. (Listens intently)

I wonder who else is locked in this asylum. I wonder where the other screams are coming from. . . (Puts her hand to her lips and then to her throat) I wonder if they’re coming from me.

There’s something simmering inside of me. Something I’ve never dared to tap into, something I’m afraid to acknowledge. There’s a part of me clawing to break free from the cage I’ve trapped it in, banging on the doors of my heart begging to be free.Begging to let go.

Every day I feel like I’m reliving the same nightmare. I open my mouth to shout, to fight, to swing my fists but my vocal chords are cut, my arms are heavy and weighted down as if trapped in wet cement and I’m screaming but no one can hear me, no one can reach me and I’m caught. And it’s killing me.

I’ve always had to make myself submissive, subservient, twisted into a pleading, passive mop just to make everyone else feel safe and comfortable. My existence has become a fight to prove I’m harmless, that I’m not a threat, that I’m capable of living among other human beings without hurting them. ********

I don’t know what’s happening to me.

Sometimes I think the shadows are moving.

Sometimes I think someone might be watching.

Sometimes this idea scares me and sometimes the idea makes me so absurdly happy I can’t stop crying. And then sometimes I think I have no idea when I started losing my mind in here. Nothing seems real anymore and I can’t tell if I’m screaming out loud or only in my head.

There’s no one here to hear me.

To tell me I’m not dead. ********

Hate.

It’s poison, an unrelenting punch to the gut, an injustice injected directly into your bloodstream that slowly paralyzes your organs until you can’t breathe

you can’t

breathe

because loneliness has stuffed itself into your clothes and you’re rotting to death in a dark corner of the world and you’re already forgotten.

You never even were. ********

Loneliness is a strange sort of thing.

It creeps up on you, quiet and still, sits by your side in the dark, strokes your hair as you sleep. It wraps itself around your bones, squeezing so tight you almost can’t breathe, almost can’t hear the pulse racing in your blood as it rushes up your skin and touches its lips to the soft hairs at the back of your neck. It leaves lies in your heart, lies next to you at night, leeches the light out from every corner. It’s a constant companion, clasping your hand only to yank you down when you’re struggling to stand up, catching your tears only to force them down your throat. It scares you simply by standing by your side.

You wake up in the morning and wonder who you are. You fail to fall asleep at night and tremble in your skin. Loneliness is an old friend standing beside you in the mirror, looking you in the eye, challenging you to live your life without it. You can’t find the words to fight yourself, to fight the words screaming that you’re not enough never enough never ever enough.

Loneliness is a bitter, wretched companion. Sometimes it just won’t let go. ********

I close my eyes and try to remember a world beyond these walls. I wonder what it would be like to know that I’m not dreaming, that this isolated existence is not caged within my own mind.

And I do. I do I wonder, I think about it all the time.

What it would be like to kill myself.

Because I never really know, I still can’t tell the difference, I’m never quite certain whether or not I’m actually alive.

So I sit here.

I sit here every day. ********

Run, I said to myself.

Run until your lungs collapse, until the wind whips and snaps at your tattered clothes, until you’re a blur that blends into the background.

Run, Juliette, run faster, run until your bones break and your shins split and your muscles atrophy and your heart dies because it was always too big for your chest and it beat too fast for too long and run.

Run run run until you can’t hear their feet behind you. Run until they drop their fists and their shouts dissolve in the air. Run with your eyes open and your mouth shut and darn the river rushing up behind your eyes. Run, Juliette.

Run until you drop dead.

Make sure your heart stops before they ever reach you. Before they ever touch you.

Run, I said. ********

Why don’t you just kill yourself? someone at school asked me once.

I think it was the kind of question intended to be cruel, but it was the first time I ever contemplated the possibility. I didn’t know what to say. Maybe I was crazy to consider it, but I always hoped that if I were a good enough girl—if I did everything right, if I said the right things or said nothing at all—I thought my parents would change their minds. I thought they would finally listen when I tried to talk. I thought they would give me a chance. I thought they might finally love me.

I always had hope. ********

I remember televisions and fireplaces and porcelain sinks . . .

I remember movie tickets and parking lots and SUVs . . .

I remember hair salons and holidays and toothpaste commercials;

ladies in high heels and old men in business suits . . .

I remember mailmen and libraries and boy bands and balloons and Christmas trees . . .

[I remember hope]
```

---

## IC-2274: Kissing Doorknobs

- Title: Kissing Doorknobs
- Author (byline): Terry Spencer Hesser
- Work: Not specified
- Publisher: Laurel Leaf
- Publication date as stated: November 1999
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1862
- Already set (do not supply): none

### Source block (context only)

```text
Author: Terry Spencer Hesser
ISBN: 978-0440413141
Publisher: Laurel Leaf
Date (Month/Year): November 1999
```

### Introduction (context only: never use it for content warnings)

```text
In adolescence, there are many things that seem out of my control - juggling school obligations, teacher and parent expectations, and finding time to just be a kid.

In the novel Kissing Doorknobs, based on real-life experiences, Tara has the same issues. Up until the time Tara was eleven years old, she thought her life was pretty much ordinary. Tall, blond, good grades, sister and parents, and enough anxieties to keep her company. But Tara’s anxieties turned into rounds of habits that plagued her life and family, a result of OCD that wasn’t diagnosed until after years of questioning her sanity.

Having no control in finding our solutions can be exhausting as seen in Kissing Doorknobs by Terry Spencer Hesser.
```

### Performance text (classify this)

```text
(Pg 12-13) Step on a crack, break your mother’s back! The first time I heard that stupid rhyme was when I was eleven years old and still in possession of my own thoughts. At first I thought the rhyme was stupid.

But [then] I couldn’t stop hearing it in my head over and over again. Eating dinner - Step on a crack, break your mother’s back! Doing homework - Step on a crack, break your mother’s back! Having a conversation - Step on a crack, break your mother’s back! Falling asleep - Step on a crack, break your mother’s back!

Nine syllables. Uneven. I hate that.

Not long after I heard that moronic rhyme for the first time, I suddenly couldn’t take my eyes off the sidewalk. Anyone who saw me quietly counting cracks would know that something was seriously wrong with me.

To and from school. Counting. Sweating. And, of course, worrying. About my mother’s spine. About my sanity. About being seen. And about being interrupted.

(Pg 18) [When I was little], I always woke up screaming from nightmare[s]. Usually, by the time I opened my eyes, my mother was already by my side, stoking my hair.

“I hate dream monsters too. But that’s all they are. Dream monsters.”

Letting kindness get that near to pain is like giving a fire some oxygen. Each time it happened, I cried harder and harder as my eczema secretly spread to my torso. Eczema is a red, scaly rash that can crop up anywhere, anytime, and itch so badly that you want to scratch if off with a chain saw. My eczema, like my worries, seemed to come and go regardless of nightmares or the terrible kindness.

(Pg 20) Kindergarten was hell. After a few months, I got over my separation anxiety. But other things started to bother me. I lived in dread of fire drills and emergency evacuations.

(Pg 30) I worried so much that I worried about worrying.

(Pg 21) There were parent-teacher and counselor meetings about my fears, but no one seemed to feel confident about what to do. And so, unable to rely on adults in my life to save me, I turned my attention to God.

(Pg 35-36) Then, one freezing day in winter, while waiting for the bell to ring, I heard someone say, “Step on a crack, break your mother’s back!” and my entire life changed.

No matter how hard I tried, I couldn’t not think the monotonous, scary refrain… and once I began to count cracks, I couldn’t stop.

(Pg 44-45) [But] I decided to save as many souls as I could in my own small way. From that moment on, anytime anyone swore or took the Lord’s name in vain, I said a prayer for their soul and punctuated my plea with the sign of the cross.

My family found my new quirk very irritating. My father tolerated it as another in my series of what he referred to as stages. My mother wasn’t so philosophical. After a few months of it, she was pretty hostile.

Like the time she kicked the car door shut because she had groceries in both arms and got her skirt stuck in the door. “Son of a b--- already!” I instantly came to her aid.

“Our Father who art in heaven, hallowed be thy name…”

“Cut it out! Damn!”

This time [I] was silent. But she saw me make the sign of the cross.

“I’m warning you…”

Unpacking the groceries, my mother caught me murmuring a Hail Mary.

“Cut it out, Tara. PLEASE.”

But I couldn’t. “...and blessed is the fruit of thy womb…”

“Cut it out, I said! If I see you doing that one more time, I’m going to punish you… severely… Dammit!”

I was halfway through the sign of the cross and muttering an “Our Father…”

(Pg 48) A few days later, my parents sent me to see a shrink. I’d been counting cracks for almost a year, but it was the praying that couldn’t be tolerated. (Pg 69) I missed the way we all used to be, so badly that I felt sick.

(Pg 72) To take our minds off our problems, [my family] decided to go to a carnival together. [Earlier that day, my mother had told me,] (Pg 71) “I’ve been patient, but from now on, every time I see you make the sign of the cross, I’m going to slap you silly.”

(Pg 72) Mounting the stairs to the Octopus ride, I reflexively performed a quick sign of the cross. I didn’t even really know that I did it. But my mother did.

She grabbed my arm so violently I almost fell off the platform. “Do that on the ride and I’m going to kill you.”

(Pg 73) As the carnival worker strapped Greta and me in, my mother and I locked eyes. I crossed myself. Not just once but again and again for the duration of the ride.

“Why, Tara? Why?” was all my sister said, but I didn’t answer her. I just kept praying and watching my mother even when we were upside down.

When the ride stopped, I knew I was a dead girl walking.

My mother picked me up by my arms, grabbed both my shoulders and shook me and shook me and shook me, crying harder than I did the entire time.

(Pg 88) For the most part, [by] eighth grade, I was normal. I rarely counted cracks or prayed anymore.

[For Christmas, my grandparents came over for dinner.] (Pg 94) The house smelled great, and everyone was standing around the table admiringly.

(Pg 95-96) My dad said, “Okay, everybody can sit down where they’re standing.”

As everyone began to sit down, I went ballistic. “What’s going on? Everybody is in the wrong places! You don’t sit there! You sit there! Like always. Mom sits there like always! And Gramma and Grampa sit there, please! Please! Come on, Greta, you sit there like always… and [I] sit here… just like always! What’s wrong with you guys? Huh? What are you trying to do to me! Come on, Daddy! Pleeeeeze sit there. Mom! Please! Please! Just like always! Just like always. It’s got to be just like always!”

My grandparents looked more scared than I did. My mom’s tears of pride had turned to fountains of pain. It was my father who spoke first. “Jesus, Mary and Joseph!”

“Our Father who art in Heaven -”...

“That’s it!” My dad knocked a chair on its side and stormed out.

(Pg 100) One day in late January, I stopped in front of the doorknob in our living room and… froze.

Before I knew what was happening, I had placed all ten of my fingers on the doorknob in a little circle with the exact same pressure… [and then] brought those fingers to my lips.

I spread my lips out as wide as I could and touched all ten of my fingers to my lips with the exact same pressure. It was the birth of a ritual that would be repeated many, many times. From that day on, I was compelled to perform that ritual almost any time I came in contact with my front door. If I slipped and applied more pressure with one finger than another, or if a finger fell off my lip, I’d have to do it all over again. (Pg 134) A new ritual.

(Pg 100) “Why? Why!? WHY?” my mother asked over and over, as if she was stuck on Replay.

(Pg 110-111) It was a warm spring night and my dad was watching television. I was trying to get out the door so [I] could hang out at the park. Of course, in order to get out the front door, I had to touch the doorknob and my lips. Usually I had to do it thirty-three times. Thirty-three perfect times, and at least a half hour later than I’d planned on leaving, I could finally slip out. Usually. . . I felt [my father] staring at me.

“Was it something your mother and I did? Tara . . . please. I love you, Tara, We all do. Please stop. Please.” The doorbell rang. My father and I were both startled. I didn’t stop my ritual, although I did try to speed it up. Eighteen. Nineteen.

“Answer the door! Answer the damn door. Can’t you just stop it for once? Stop it. Just stop it!”

I couldn’t stop. I was so nervous I lost count just as he picked me up, moved me to the side and opened the door. It was Allan Jacobson, my father’s old friend from college who was also the local high-school science teacher. As I looked at my dad’s frightened face, I burst into tears. Giant tears. And my daddy took me in his arms and rocked me. Then he did something I’d never seen before. He began to cry too. We cried. And rocked. And cried.

After my dad and I calmed down, Mr. Jacobson started asking me questions that nobody had ever asked me before.

(Pg 112) “What does it feel like when you do that thing with the doorknob, honey? Do you do it a certain number of times? I have a boy in my class, a little older than you, who I think has a similar problem.”

[My new therapist explained.] (Pg 123-124) “I’m sure she acts pretty crazy. Imagine how you’d act if you were trapped in an endless loop of repetitive obsessive thoughts accompanied by an anxiety so powerful you’d do anything . . . perform any compulsive act . . . just to make it go away. We don’t know what causes it. Maybe genetics. Maybe stress, trauma, or other injury. Although the behavior has been around as long as man, the research is new. The longer a person has been a slave to OCD, the harder it is to make him or herself risk freedom. Why don’t we move ahead with behavior therapy. If that proves inadequate on its own, then we’ll consider medication.”

(Pg 132-134) No matter how passionate I was, or how strong I decided to be, behavior therapy was very, very hard. I lost a lot of battles. It had been months and I was still involved in a terrible thirty-three-step dance involving my lips, fingers, and a doorknob. I also still counted cracks and prayed. Not all the time. But enough of the time to doubt that I’d ever win the war for my freedom.

And on the good days, when I felt as if I was making progress - I was scared then, too.

[Walking home with my friends one day], I stepped on every crack I could find. I felt nervous, dizzy, sick, but I did it.

When we passed the hardware store, I ran inside. Standing in front of a wall of doorknobs, as a test, I ran my hand across a few of the doorknobs. I felt nothing.

(Pg 18) [When I was little], I always woke up screaming from nightmare[s].

(Pg 142) I think I figured out my dream. As I look at it now, it’s kind of obvious. That monster was my OCD. It came out of nowhere, blocked out my world and threatened to crush me. I was paralyzed.

(Pg 148) But [I] didn’t fold or drop out. [I] summoned the courage to play the cards life had dealt [me]. Reluctant, insecure warrior but warrior all the same. And [I’m not] alone.
```

---

## IC-2275: Know My Name

- Title: Know My Name
- Author (byline): Chanel Miller
- Work: Not specified
- Publisher: Viking
- Publication date as stated: Sept 2019
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2164
- Already set (do not supply): none

### Source block (context only)

```text
Author: Chanel Miller
ISBN: 978-0735223707
Publisher: Viking
Date (Month/Year): Sept 2019
```

### Introduction (context only: never use it for content warnings)

```text
One night in January 2015, two Stanford University graduate students biking across campus spotted a freshman thrusting his body on top of an unconscious, half-naked woman behind a dumpster. A California jury found 20-year-old Brock Allen Turner, guilty of three counts of sexual assault. Facing a maximum of 14 years in state prison, Turner was sentenced to only 6 months in county jail and probation. The judge said he feared a longer sentence would have a “severe impact” on Turner, a champion swimmer who once aspired to compete in the Olympics.

At that time, Chanel Miller, the victim, was known to the world as Emily Doe. Her impact statement was viewed by 11 million people within 4 days; it was translated globally and read on the floor of Congress; it inspired changes in California law and the recall of the judge in the case. Thousands wrote to say that she had given them the courage to share their own experiences of assault for the first time. Now she reclaims her identity to tell her story of trauma, transcendence, and the power of words.

Know My Name by Chanel Miller
```

### Performance text (classify this)

```text
(Pg 7) (to audience) In this story, I will use Brock Turner’s name, but the truth is he could be Brad or Brody or Benson, and it doesn’t matter. This is an attempt to transform the hurt inside myself, to confront a past, and find a way to live with and incorporate these memories. I want to leave them behind so I can move forward. My name is Chanel. I am a victim, I have no qualms with this word, only with the idea that it is all that I am. However, I am not Brock Turner’s victim. I am not his anything. I don’t belong to him.

(Pg 284-285) (to audience) On January 17th, 2015, it was a quiet Saturday night at home. My dad made some dinner and I sat at the table with my younger sister who was visiting for the weekend. I was working full time and it was approaching my bed time. I planned to stay at home by myself, watch some TV and read, while she went to a party with her friends. Then, I decided it was my only night with her, I had nothing better to do, so why not, there’s a dumb party ten minutes from my house, I would go, dance like a fool, and embarrass my younger sister.

I made silly faces, let my guard down, and drank liquor too fast not factoring in that my tolerance had significantly lowered since college. The next thing I remember I was in a gurney in a hallway. I had dried blood and bandages on the backs of my hands and elbow. A deputy explained I had been assaulted. I was asked to sign papers that said “Rape Victim. ” On that morning, all that I was told was that I had been found behind a dumpster, potentially penetrated by a stranger, and that I should get retested for HIV because results don’t always show up immediately. But for now, I should go home and get back to my normal life.

(Pg 52) In rape cases it’s strange to me when people say, Well why didn’t you fight him? If you woke up to a robber in your home, saw him taking your stuff, people wouldn’t ask, Well why didn’t you fight him? Why didn’t you tell him no? He’s already violating an unspoken rule, why would he suddenly decide to adhere to reason? What would give you reason to think he’d stop if you told him to? And in this case, with my being unconscious, why were there still so many questions?

(Pg 287) One day, I was at work, scrolling through the news on my phone, and came across an article. In it, I read and learned for the first time about how I was found unconscious, with my hair disheveled, long necklace wrapped around my neck, bra pulled out of my dress, dress pulled off over my shoulders and pulled up above my waist, that I was butt naked all the way down to my boots, legs spread apart, and had been penetrated by a foreign object by someone I did not recognize. This was how I learned what happened to me, sitting at my desk reading the news at work. I learned what happened to me the same time everyone else in the world learned what happened to me -- This can’t be me, this can’t be me -- I kept reading. In the next paragraph, I read something that I will never forgive; I read that according to him, I liked it. I liked it.

And then, at the bottom of the article, after I learned about the graphic details of my own sexual assault, the article listed his swimming times. She was found breathing, unresponsive with her underwear six inches away from her bare stomach curled in fetal position. By the way, he’s really good at swimming. Throw in my mile time if that’s what we’re doing. I’m good at cooking, put that in there, I think the end is where you list your extracurriculars to cancel out all the sickening things that’ve happened.

(Pg 288) I thought there’s no way this is going to trial; there were witnesses, there was dirt in my body, he ran but was caught. He’s going to settle, formally apologize, and we will both move on. Instead, I was told he hired a powerful attorney, expert witnesses, private investigators who were going to try and find details about my personal life to use against me, find loopholes in my story to invalidate me in order to show that this sexual assault was in fact a misunderstanding. (Pg 289) I had no power, I had no voice, I was defenseless. My memory loss would be used against me. His attorney constantly reminded the jury, the only one we can believe is Brock, because she doesn’t remember. That helplessness was traumatizing.

(Pg 290) After a physical assault, I was assaulted with questions designed to attack me, to say see, her facts don’t line up, she’s out of her mind, she’s practically an alcoholic, she probably wanted to hook up, he’s like an athlete right, they were both drunk, whatever, the hospital stuff she remembers is after the fact, why take it into account, Brock has a lot at stake so he’s having a really hard time right now.

(Pg 80) When a woman is assaulted, one of the first questions people ask is, Did you say no? This question assumes that the answer was always yes, and that it is her job to revoke the agreement. To defuse the bomb she was given. But why are they allowed to touch us until we physically fight them off? Why is the door open until we have to slam it shut?

(Pg 291) (to defendant) [For] future reference, if you are confused about whether a girl can consent, see if she can speak an entire sentence. You couldn’t even do that. Just one coherent string of words. If she can’t do that, then no. Not maybe, just no. Where was the confusion? This is common sense, human decency.

(Pg 293-297) (to audience) In the end, his unsupported statements and his attorney’s twisted logic fooled no one. The truth won, the truth spoke for itself. You are guilty. Twelve jurors convicted you guilty of three felony counts beyond reasonable doubt, that’s twelve votes per count, thirty-six yeses confirming guilt, that’s one hundred percent, unanimous guilt. This is not a story of another drunk college hookup with poor decision making. Assault is not an accident. (to defendant) Somehow, you still don’t get it. Somehow, you still sound confused.

You said, “Being drunk I just couldn’t make the best decisions and neither could she.” Alcohol is not an excuse. Is it a factor? Yes. But alcohol was not the one who [raped me]. Having too much to drink was an amateur mistake that I admit to, but it is not criminal. Everyone in this room has had a night where they have regretted drinking too much. Regretting drinking is not the same as regretting sexual assault.

You said, you are in the process of establishing a program for high school and college students in which you speak about your experience to “speak out against the college campus drinking culture and the sexual promiscuity that goes along with that.” Campus drinking culture. That’s what we’re speaking out against? You think that’s what I’ve spent the past year fighting for? Not awareness about campus sexual assault, or rape, or learning to recognize consent. Campus drinking culture. Down with Jack Daniels. Down with Skyy Vodka. If you want to talk to people about drinking go to an AA meeting. You realize, having a drinking problem is different than drinking and then forcefully trying to have sex with someone? Show men how to respect women, not how to drink less. Drinking culture and the sexual promiscuity that goes along with that. Goes along with that, like a side effect, like fries on the side of your order. Where does promiscuity even come into play? I don’t see headlines that read, Brock Turner, Guilty of drinking too much and the sexual promiscuity that goes along with that. Campus Sexual Assault. There’s your first PowerPoint slide. Rest assured, if you fail to fix the topic of your talk, I will follow you to every school you go to and give a follow up presentation.

Lastly you said, “I want to show people that one night of drinking can ruin a life.” A life, one life, yours, you forgot about mine. Let me rephrase for you, I want to show people that one night of drinking can ruin two lives. You and me. You are the cause, I am the effect. If you think I was spared, came out unscathed, that today I ride off into sunset, while you suffer the greatest blow, you are mistaken. Nobody wins. We have all been devastated, we have all been trying to find some meaning in all of this suffering. Your damage was concrete; stripped of titles, degrees, enrollment. My damage was internal, unseen, I carry it with me. You took away my worth, my privacy, my energy, my time, my safety, my intimacy, my confidence, my own voice, until today . . . You made me a victim. In newspapers my name was “unconscious intoxicated woman,” ten syllables, and nothing more than that. For a while, I believed that that was all I was. I had to force myself to relearn my real name, my identity. To relearn that this is not all that I am. That I am not just a drunk victim at a frat party found behind a dumpster, while you are the All-American swimmer at a top university, innocent until proven guilty, with so much at stake.

While you worry about your shattered reputation, I refrigerated spoons every night so when I woke up, and my eyes were puffy from crying, I would hold the spoons to my eyes to lessen the swelling so that I could see. I can’t sleep alone at night without having a light on, like a five-year-old, because I have nightmares of being touched. I used to pride myself on my independence, now I am afraid to go on walks in the evening, to attend social events with drinking among friends where I should be comfortable being. It is embarrassing how feeble I feel, how timidly I move through life, always guarded, ready to defend myself, ready to be angry.

(Pg 298-299) You do not get to shrug your shoulders and be confused anymore. You do not get to pretend that there were no red flags. You have been convicted of violating me, intentionally, forcibly, sexually, with malicious intent, and all you can admit to is consuming alcohol. Do not talk about the sad way your life was upturned because alcohol made you do bad things. Face the consequences of putting my pain into question, of making us wait so long for justice. Someone who cannot take full accountability for his actions does not deserve a mitigating sentence.

(Pg 300) (to audience) He has been found guilty of three serious felonies and it is time for him to accept the consequences of his actions. He will not be quietly excused. He is a lifetime sex registrant. That doesn’t expire. Just like what he did to me doesn’t expire, doesn’t just go away after a set number of years. It stays with me, it’s part of my identity, it has forever changed the way I carry myself, the way I live the rest of my life.

(Pg 301) To girls everywhere, I am with you. On nights when you feel alone, I am with you. When people doubt you or dismiss you, I am with you. I fought every day for you. So never stop fighting, I believe you. As the author Anne Lamott once wrote, “Lighthouses don’t go running all over an island looking for boats to save; they just stand there shining.” Although I can’t save every boat, I hope that by speaking today, you absorbed a small amount of light, a small knowing that you can’t be silenced, a small satisfaction that justice was served, a small assurance that we are getting somewhere, and a big, big knowing that you are important, unquestionably, you are untouchable, you are beautiful, you are to be valued, respected, undeniably, every minute of every day, you are powerful and nobody can take that away from you.

(Pg 280) Hold up your head when the tears come, when you are mocked, insulted, questioned, threatened, when they tell you you are nothing, when your body is reduced to openings. The journey will be longer than you imagined, trauma will find you again and again. Do not become the ones who hurt you. Stay tender with your power. Never fight to injure, fight to uplift. Fight because you know that in this life, you deserve safety, joy, and freedom. Fight because it is your life. Not anyone else’s.

Emily Doe’s Victim Impact Statement was originally published by Katie J.M. Baker in Buzzfeed News on June 3, 2016.
```

---

## IC-2276: The Knowers

- Title: The Knowers
- Author (byline): Helen Phillips
- Work: Some Possible Solutions (Pg 1-14)
- Publisher: Picador
- Publication date as stated: June 2017
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: ELLIE, TEM
- Teaser before the introduction: Yes
- Spoken words (computed): 1648
- Already set (do not supply): none

### Source block (context only)

```text
Author: Helen Phillips
Book: Some Possible Solutions (Pg 1-14)
ISBN: 978-1250132185
Publisher: Picador
Date (Month/Year): June 2017
```

### Introduction (context only: never use it for content warnings)

```text
We all know our time here on earth is limited. But we don’t know by how much. Are we better off not knowing when we’ll die? Or would a countdown help us all to lead happier and more fulfilling lives? If you knew exactly when you were going to die, what would you change about the way you live?

The Knowers by Helen Phillips
```

### Performance text (classify this)

```text
ELLIE: April 17, 2043. The knowledge heightened my life. The knowledge burdened my life. I regretted knowing. I was grateful to know.

ELLIE: (Pg 1-14) There are those who wish to know, and there are those who don’t wish to know. At first Tem made fun of me when I claimed to be among the former; when he realized I meant it, he grew anxious, and when he realized I really did mean it, his anxiety morphed into terror.

TEM: (tearfully) Why? Why why why? This isn’t only about you, you know. It affects me too. I don’t want to sit around for a bunch of decades awaiting the worst day of my life.

ELLIE: If only I could have known it was possible to know and still have been fine with ignorance. But now that the technology had been mastered, the knowledge was available to every citizen for a nominal fee.

No way was I going to tell him about the bureaucratic office with its pale-yellow walls. It never ceases to amaze me that, even as our country forges into the future with ever more bedazzling devices and technologies, the archaic infrastructure rots away beneath our feet, the pavement and the rails, the schools and the DMV. In any case: Tem would not know, today or ever, about the place I’d gone, about the humming machine that looked like a low-budget ATM (could they really do no better?), about the chilly metal buttons of the keypad into which I punched my social security number after waiting in line behind other soon-to-be Knowers. There was a silent, grim camaraderie among us as I glanced down at the paper the slot spat out at me, as I folded it up and stepped away from the machine.

TEM: (holding out his hand, palm quivering but in a jovial voice) Okay, lay it on me.

ELLIE: The words were light, almost jovial, but I could tell they were the five hardest words he’d ever uttered. I swore to never again accuse Tem of being less than courageous. And I applauded myself for going straight from the bureaucratic office to the canal, for standing there above the sickly greenish water, for glancing once more at the piece of paper, for tearing it into as many scraps as possible, for dropping it into the factory-scented breeze. I’d thought it was the right thing to do, and now I knew it was. Tem should not have to live under the same roof with that piece of paper. (to Tem, brightly) I don’t have it.

TEM: (gasping) You don’t? You mean you changed your —

ELLIE: I got it. I got it, and then I got rid of it, after memorizing it, of course. I know.

TEM: You know! You know! (softly, with trepidation) Tell me.

ELLIE: Are you sure? (to audience) Suddenly it seemed quite likely that I’d made a catastrophic error. The kind of error that could ruin the rest of my life. I became wildly scared; I who’d so boldly sought knowledge now did not even dare give voice to a date. (to Tem) April 17 —

TEM: (covering his ears) Stop! Never mind! I don’t want to know! Don’t! Don’t don’t don’t!

ELLIE: OKAY. (to audience) It was lonely to hold this knowledge. April 17, 2043: a tattoo inside my brain. But it was as it should be. It was the choice I had made. Tem wished to be spared, and spare him I would.

It was an okay lifespan. Not enough — is it ever enough? — but enough to have a life; to work a job, to raise children, perhaps to meet a grandchild or two. Short, yes; but not tragically short. And so in many ways I could live a life like any other. I could go blithely along, indulging my petty concerns, lacking perspective, frequently forgetting I wasn’t immortal. Yet it would be a lie if I said a single day passed without me thinking about April 17, 2043.

I began to mark April 17. I would buy myself a gift: a bar of dark chocolate -- a new dress. I always felt extravagant on April 17; I’d leave a tip of twenty-five percent, hand out a five-dollar bill to any vagrant who happened to cross my path. You can’t take it with you and all that. I’d make a reservation for us at a fancy restaurant; I’d schedule a weekend getaway. Luxuries we spent the whole rest of the year carefully avoiding.

My life would seem normal — bland, really — to an outside observer, but I tell you that for me it has been rich, layered and rich. There have been so many moments, almost an infinity of moments — soaping up the kids’ hair when they were tiny, walking from the parking lot to the office on a bird-studded Friday morning. What can I say. I don’t mean to be sentimental, but these are not small things. The deeper that sorrow carves into your being, the more joy you can contain. This is no time to go into the ups and downs, the stillbirths and the car accident and the estrangement, but I believe the above statement to be true. April 17, 2043. The knowledge heightened my life. The knowledge burdened my life. I regretted knowing. I was grateful to know.

I’ve never been the type to bungee jump or skydive, yet in many small ways I lived more courageously. I knew when to fear death, yes, but that also meant I knew when not to fear it. I’d gone to the grocery store during times of quarantine. I’d volunteered at the hospital, driven in blizzards, ridden roller coasters so rickety Tem wouldn’t let the kids on them. But I have to admit that December 31, 2042, was a fearful day for me.

We’d hosted everyone for a last supper of the year, both children and their spouses, and our first grandchild, bright as a brand-new penny. At the dinner table, our radiant daughter and her husband announced that they were expecting in August. Amid the raucous cheers and exclamations, no one noticed that I wasn’t cheering. The child I’d miss by four months. The ache was vast. I couldn’t speak.

I stood in the bathroom, clinging to the sink, staring at my face in the mirror until it no longer felt like my face. This would develop into a distasteful but addictive habit over the course of the next three and a half months. I got pretty good at hiding my dread. From Tem, and even at times from myself. We planted bulbs; we bought a cooler for summer picnics. I pretended and pretended; it felt nice to pretend.

Yet when Tem asked, on April 10, what I’d planned for this year’s getaway, the veil fell away. Given the circumstance, I had — of course — neglected to make any plans for the 17th. The dread rushed outward from my gut until my entire body was hot and cold. Panicking, I looked across the table at Tem, who was gazing at me hopefully, the way he’d looked at me for almost four decades. Tem and I — we’ve been so lucky in love. (to Tem; choked up) Tem . . . (to audience) And then he realized.

TEM: Damn it, Ellie! Why’d you have to — !

ELLIE: I quietly quit my job and Tem took the week off. We spent every minute together and invited the blissfully ignorant kids out for brunch. Everything I saw — a gas station, a tree, a flagpole — I thought how it would go on existing, just the same.

On the morning of April 17, 2043, I was half-amazed to open my eyes to the light. Six hours and four minutes into the day, and I was alive. Petrified, scared to move even a muscle, I wondered how death would come for me. Would it be a heart attack, a stroke, a tumble down the basement stairs? I had the inclination to stay in bed, but by 10 a.m. I was still alive and feeling antsy, bold. Why lie here whimpering when it was coming for me no matter what? (To Tem) Let’s go out. It’s not like I’m sick or anything.

(to audience) The outside seemed more dangerous — there it could be a falling branch, a malfunctioning crane, a truck raring up onto the sidewalk. But it could just as easily catch me at home — misplaced rat poison, a chunk of meat lodged in my throat, a slick bathtub.

We walked, looking this way and that as we went, hyperaware of everything. Vigilant. I felt like a newborn person, passing so alertly through the world. We sat in a park, each additional moment a small shock. Come 11:45 pm, we were inside, brushing our teeth, shaking. Would I simply collapse onto the floor, or would it be a burglar with a weapon?

What if there had been an error? Remembering back to that humble machine, that thin scrap of paper, the cold buttons of the keypad, I indulged in the fantasy I’d avoided over the years. It suddenly seemed possible that I’d punched my social in wrong, one digit off. Or that there had been some kind of bureaucratic mistake, some malfunction deep within the machine. Or perhaps I’d mixed up the digits — April 13, 2047. If I lived beyond April 17, 2043, where would the new boundaries of my life lie?

We stood there staring at each other in the bathroom mirror. This time I didn’t fall into my own reflection — I was looking at Tem. Why had it never occurred to me that it might be something that would kill Tem too? In all of these years, truly, I had never once entertained that possibility. But it could be a meteorite, a bomb, an earthquake, a fire. I unlocked my eyes from Tem’s reflection and clung to him like I was clinging to a cliff, and he clung right back. I counted ten tense seconds. The pulse in his neck.

11:54 pm on April 17, 2043. We are both alive and well. Yet I mustn’t get ahead of myself. There are still six minutes remaining. [Six . . . Five . . . Four . . . ]
```

---

## IC-2277: Last Wish

- Title: Last Wish
- Author (byline): Christi Galloway
- Work: Chicken Soup for the Teenage Soul
- Publisher: HCI Teens
- Publication date as stated: May 1997
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1256
- Already set (do not supply): none

### Source block (context only)

```text
Author: Christi Galloway
Book: Chicken Soup for the Teenage Soul
ISBN: 978-1558744639
Publisher: HCI Teens
Date (Month/Year): May 1997
```

### Introduction (context only: never use it for content warnings)

```text
"It's the anticipation and anxiety of climbing the highest hill on the scariest roller-coaster, only it never comes down. And you're stuck up there - waiting - expecting - not knowing when it will fall - if you fall." Seventeen-
```

### Performance text (classify this)

```text
year-old Melissa describes her feelings after being diagnosed with cancer. For every teen-ager the concept of a terminal illness is frightening; and the coping skills vary dramatically. Today, I’d like to tell you Chris’ story; a story of a life waiting; expecting; not knowing and how he and his friends found faith in his Last Wish by Christi Galloway.

Chris Hart was not your average 16-year-old. He was six-feet-eight-inches tall and weighed 260 pounds. In his freshman year of high school he played on the varsity football team; he could bench-press 250 pounds and squat 450. Then he was diagnosed with osteogennic sarcoma, a form of cancer. For a while it was in remission, then during his junior year it returned. A couple of months before Christmas in 1993, he was told by doctors that he probably did not have long to live.

That same year a local radio station sponsored a contest granting requests to people who wrote in with the best Christmas wishes. A member of our church wrote a letter in to the radio station on Chris's behalf. Little did I know that when this letter was chosen, my world would change, too.

Chris's first wish was to have a stereo system for his truck. A local electronics firm obliged. His second wish was to see a Dallas Cowboys football game. That was his favorite team and he was their greatest fan. To his surprise, he not only got to see the Cowboys play, he actually met some of them in the locker room. Chris's third wish was more difficult to coordinate because of its sensitive nature. He wanted a date with a redhead.

At this point I should explain that I am a redhead.

My dad came home from church one night and told me about Chris and his three wishes, especially his third wish.

"Dad, I don't even know the guy," I said.

How could I go on a date with him? I didn't go to his school. I had never met him. My dad, who is a minister, had visited Chris several times and all he could say about him was the he was very nice, very tall, and "big-boned." With some hesitation I said yes.

The date was scheduled for the week before Christmas. Before then Chris and I had only talked on the phone. He seemed sweet, but I was nervous about going out on a date, so I asked one of my best friends to join us. When Chris came to pick me up I was a little shocked by how he looked. He was huge, and bald from his chemotherapy treatments. He wore a hat, but took it off inside to be polite, exposing his hairless head. When we went to a local pizza restaurant, he had to duck to get through the door, and everybody stared at us.

After that he started to come to my house after school and we talked about our problems or watched movies. He told me how much he missed playing football, and sometimes we listened to music.

On Valentine's Day, a friend and I cooked a special dinner for Chris and his girlfriend, and we exchanged presents. Chris seemed pleased with the teddy bear and the new CD. He even asked me to go to his junior-senior prom.

Then I did something I'm still ashamed of. It started when the town newspaper did an article about Chris's three wishes. It was accompanied by a picture of the two of us in front of his truck. The caption said we dated. When kids from school saw the article and pictures, they made comments. I tried to ignore them, but one day, one of the popular seniors said to me, "Hey, I guess that guy couldn't find anybody better to date."

It really hurt. I was only a sophomore and still felt new to the town. I wanted people to like me. I didn't want them to think I was weird.

When Chris called, I said I was busy and couldn't talk. I made excuses, so he stopped coming over and we stopped going out. At night I cried myself to sleep because I knew I was being cruel, but I couldn't help it. Chris's prom was coming up and I knew I had to talk to him. Mom's friend had made a special dress for me and I had promised to go. So I called Chris and we made plans to go out to dinner with friends before the prom.

That night when he came to pick me up, we didn't talk much at first. He looked good in his tuxedo and sneakers (he couldn't find any black shoes big enough to fit). He had also lost a lot of weight. His class ring was so loose it kept falling off.

We joined our friends for dinner and started to laugh and joke like old times. On the way to the dance, Chris began to feel bad. We waited in the parking lot until he regained his strength.

The auditorium was beautifully decorated with an Egyptian theme. Everyone else was dancing and having a great time, but Chris still felt weak, so he could only sit and watch. While we were talking, the DJ interrupted the music and one of the football players took the microphone. He talked about Chris and how special he was. They dedicated the prom to Chris and gave him a plaque. It was one of his proudest moments.

After the prom I didn't care what people at my school thought. They could say whatever they wanted.

Chris was my friend. I just hoped he could forgive me for the way I had treated him. That spring he became much worse and the doctors gave him two weeks to live. Every day for those two weeks I visited him. He had a huge bed set up in his bedroom with a lot of pillows, and together we watched TV and talked.

He wasn't afraid to talk about dying. I found it painful, but my dad said that just by listening to Chris, I was helping him.

Each day it got harder for Chris to concentrate. By the last few days he could barely recognize anybody. Saturday afternoon was the last time I got to visit Chris. As I was leaving, he called me back and asked for a hug. As I hugged him, he whispered, "I love you."

It was the first time he had said those words to me. He really had forgiven me.

Sunday morning I went straight home after church. My parents suggested I join them at the restaurant for lunch, but I felt there was some reason I shouldn't. Only moments after I got home a phone call came from Chris's dad; Chris was dying. I called the restaurant where my parents were eating and they rushed home and took me to Chris's.

Family and friends were gathered around Chris's bed. He was breathing with great gasps, very slowly. I stood there but could say nothing. Words wouldn't come.

"Christi's here," my dad said softly. "We're all here and we love you." How could I say good-bye?

"Dear God," my dad prayed, "please be with Chris and all of those present and his family. Give us a sense of peace as you receive Chris into your loving arms."

I looked up to see Chris take his last breath. He was gone.

That was two years ago, and I still miss him.
```

---

## IC-2278: Learning How to Walk

- Title: Learning How to Walk
- Author (byline): Jason Sheets
- Work: Turning Points: 30 Pieces for Oral Interpretation, Pgs 141-145
- Publisher: Tichenor Publishing
- Publication date as stated: Jan 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: WHITNEY
- Teaser before the introduction: Yes
- Spoken words (computed): 1424
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jason Sheets
Book: Turning Points: 30 Pieces for Oral Interpretation,
Pgs 141-145
ISBN: 978-0742117013
Publisher: Tichenor Publishing
Date (Month/Year): Jan 2001
```

### Introduction (context only: never use it for content warnings)

```text
When life takes an unexpected turn and someone you love becomes disabled, the challenges faced by both people in the relationship can be overwhelming. In this selection, a young couple are involved in a horrible car accident and are now faced with a future that looks dramatically different from the one they had envisioned. Can Tony learn how to walk again, or will Whitney learn how to walk away?

Learning How to Walk by Jason Sheets
```

### Performance text (classify this)

```text
WHITNEY: (Pg 141-145) All I remember from the incident are five still-frames, mentally stored as black and white images.

Frame # 1: Tony is driving down the road. He spills part of his Taco Bell burrito on his new shirt. I reprimand him. We laugh.

Frame #2: A loud crash. Darkness beyond anything I've ever seen before. It's like I'm miles back into a cave, only darker.

Frame #3: My mother tells me she's glad to see me wake up. She is arranging flowers in the room. She tells me to rest.

Frame #4: My mother tells me I'll be OK, but begins to cry when she states that Tony is not as fortunate. A feel-ing of death enters my heart.

Frame #5: My friend Tricia tells me that Tony did not die, but can no longer walk. He'll need your strength, she says. I say I will do whatever I can to help.

That is all I can remember from the incident that changed my life forever. I wish I knew more. I wish the images were at least in color.

WHITNEY: Tony and I met when I was 18 and he was 21. Ironically, because of my AP credit and his momentary lapses of reason, we were both sophomores. I'd never dated much. People asked me -- that wasn't the problem. The problem was me: I noticed things. My mother had divorced when I was eight, and she told me to watch out for men. Never settle, she told me. And you could bet I listened to my mother.

But Tony was different. lt took him three months, four sly winks, and a blatantly written note from Tricia to make him finally ask me out. I suppose people marveled at his lack of focus, his carefree nature. I saw it as indelible charm.

Everything interested him. l absolutely detest the "I am a sponge" analogy that so many others overuse, but Tony really was. He soaked up the nuances of movies, of relationships, of me. By the time my 19th birthday rolled around, it was clear: I planned on falling in love once in a lifetime, and Tony would be that one time.

I would like to say that the day of the accident somehow had special connotations to me. Perhaps I'd had an eerie feeling. Perhaps we'd just said we'd always go everywhere together. Perhaps we'd had some moment that defined the day. But there was no real irony to the events. We were riding in the car on the way to my hometown, a truck veered past the median, and then the darkness. It took me 3 days before I could finally see Tony. He was wrapped in countless bandages, but that scene-stealing smile was still there. I'm glad you 're OK, he said. You too, I replied before I realized what I was saying. Tony just looked at me with adoration: At least I have you, he responded.

Unbeknownst to most of the population, I believe doctors have to take a class in medical school that teaches them how to properly double-speak. It took me three more days before I could finally get the man to say that, yes, his brain is fine, but no, he'd never do the two-step with me again. It was only after I cleared the double-speak that the reality of what was happening really kick[ed] in. My life became a series of daily rituals. At nine o' clock I would start my journey to the hospital. If there was one thing I was leery of, it was hospitals. I used to find excuses to keep me from going. The truth was I couldn't stand the smell. The attitude. The feeling of unsettled completion of life that occurred every day. Now, my fear of hospitals and my love for Tony has been unbearably linked. When I think of Tony, l imagine the smell of hospitals. l imagine death. I wanted to vomit. Sometimes, I did.

But of course, the doctor is wrong. Tony will walk. He'll walk. Of course he will. It happens all the time in the movies. Doctor says: "I'm sorry, there's just no hope." Patient: "But I can if I try hard enough." Three months later he walks. He does. It happens in the movies. And what are movies? A reflection of real life. Right?

So now I find myself in Tony's house. I've dropped out of school, I have all my calls and mail forwarded. People refer to me as "Nurse Whitney." It was cute for a while. Now I find the title impeccably accurate. The only real difference is that after l wash his face, or feed him or bathe him, he tells me he loves me and I return the feelings. When most nurses get off work, they would go home. We stay up and watch television together and discuss our future. He wants to marry me. He tells me: We can still have the fairy tale. I say, Of course we can sweetheart I always said I'd only fall in love one time and you are the one I love. He follows this by saying I've been the best and that he' lucky to have someone who's willing to make the sacrifice. After he says that I feel strangely worse.

I tell Tony everything. Everything, but my dreams. For the first few months, I dreamt that he'd walk again. Now, I dream of leaving. I dream of running away from all my family and friends who would tell me I was being selfish, and I would spend the rest of my life on some lonely beach reading.

I dream he will say: Whitney, I don't love you anymore. Please go. I dream it. And I never tell anyone. Ever.

l figure the equation and try to re-figure it for a different answer. I never get one. I've [even] started making a list of the ways I could leave. Just in case one could actually be plausible.

1.) I could say I can't afford to stay. 2.) I could say I found someone else. 3.) I could say it's not right of me to dominate his time. 4.) I could say there was a doctor in India who's supposed to have a cure. I'II go find out. 5.) I could kill myself for thinking these things about the man I love. 6.) I could say I'm not worthy of him because of my evil thoughts -- That one could be plausible.

When I tell him I'm leaving, he does not look shocked, or stunned, or even surprised. He merely says OK, and then I feel ten times worse. For months, I'd pictured this traumatic scene where I announce my intentions and he begs and pleads with me to stay. He offers me the world and I walk away. Instead, he says OK.

OK, so now I have to explain myself. See, my mother always told me to never settle and always wait for the fairy tale. And you were the fairy tale, Tony! You were my prince that was set to sweep me off my feet and never look back. You were everything. The looks. The smile. The wit. The "sponge" of life that soaked up everything that it has to offer. You were it. You were it. But, see Tony, princes walk. They pick me up and carry me over the threshold on our wedding day. They play football with our children. They go for late night jogs with me when the rest of the world is driving me nuts. They do it all, Tony. That's the fairy tale. That's my fairy tale.

Tony now has a tear running down his cheek and I say to myself are you happy now? Is this the way it's supposed to play out? Is this the way the movie ends?

He says: I wish you all the best. If you need me, you know where I'll be.

I don't know if he's trying to be funny or vindictive, so I leave. I cry.

Life is a series of trades. You give something to get something. Fifty cents: a Pepsi. A compliment: a promotion. I made the biggest trade of all. I traded love for freedom. And now I'm left to ask: Did I make the right choice? And I like to think I can find the answer, but I can't. All I can think is that in the fairy tales, you get both. In the fairy tale, you get everything.
```

---

## IC-2279: Lessons from God

- Title: Lessons from God
- Author (byline): Jennifer Rhea Cross
- Work: Chicken Soup for the Kid’s Soul
- Publisher: HCI
- Publication date as stated: July 1998
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1148
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jennifer Rhea Cross
Book: Chicken Soup for the Kid’s Soul
ISBN: 978-1558746091
Publisher: HCI
Date (Month/Year): July 1998
```

### Introduction (context only: never use it for content warnings)

```text
According to Bernie S. Siegel, M.D. . . . . One cannot get through life without pain . . . What we can do is choose how to use the pain life presents us. In Lessons from God by Jennifer Rhea Cross A girl explains the difficulty of watching her older brother die of AIDS.
```

### Performance text (classify this)

```text
There was a time in my childhood when I believed that God was punishing my family by making us watch my only brother die.

My brother Brad was a hemophiliac. If a person has hemophilia, his blood doesn’t clot in a normal way; so, if he gets a cut, it is very difficult to stop the bleeding. When too much blood is lost, he has to have his blood replenished to keep him going.

Even through Brad couldn’t be as active as other kids because of the hemophilia, we had many common interests and spent a lot of time together. Brad and I rode bikes with the neighborhood kids, and we spent most of our summers swimming in our pool. When we played football or baseball, Brad would throw the ball, and the rest of us would do all the rough playing. Brad picked out a puppy for me when I was seven, and I named her PeeWee. My brother, Brad, was my protector and my best friend.

When Brad was ten, he received blood from someone who didn’t realize, or was too selfish to admit, that he or she was carrying the AIDS virus. ` I had just entered the sixth grade when my brother began to have serious symptoms, and was diagnosed with AIDS. He was a freshman in high school and had just turned fifteen. At that time, many people were not educated about how you “catch” AIDS and were very afraid of being around people who had it. My family worried about how people would act when they found out.

Our lives changed when Brad’s symptoms became obvious. I couldn’t have friends over to spend the night. Whenever I had a basketball game, only one, never both of my parents, could come to watch because someone had to stay with Brad. Often, my parents would need to be with Brad during the times he was hospitalized. Sometimes they were gone for a week at a time while I stayed at a neighbor’s or an aunt’s house. I never knew where I’d be from one day to the next,

Through all the sadness and confusion, I grew resentful about not being able to lead a normal life. My parents weren’t able to help me with my homework because they had to tend to Brad’s needs. I began having problems in school. The emotional part of slowly losing Brad, my best friend, made things even worse. I became very angry and needed to blame someone, so I turned my blame toward God.

It was a burden to keep his condition a secret, yet I knew how cruel kids could be. I didn’t want anyone to see my brother not looking at all like his former self, and lying in diapers. I wasn’t going to have him be the subject of their jokes at school. It wasn’t my brother’s fault that his twelve-year-old sister had to change his diapers or feed him through a tube.

The AIDS virus caused damage to Brad’s brain and destroyed the person that he had grown to be. Eventually, he became like a very young child again. Instead of listening to current music or talking about things that kids in junior high or high school would be interested in, he wanted us to read childhood books to him. He wanted me to help him color. I felt like I had lost my brother while he was still alive.

I remember the day that Brad died, just like it was yesterday. The old musty room was filled with recognizable faces. There was my brother’s worn-out body in the bed. The body was now empty, and the pain could no longer be felt. That was the end of my only brother’s life – two weeks before his eighteenth birthday.

Between 1980 and 1987, over 10,000 hemophiliacs like Brad received blood that was infected with the AIDS virus. Ninety percent of these severe hemophiliacs who were infected are either living with AIDS or have died from it. If the blood that they received had been tested before they gave it to them, their early deaths could have been avoided. As I see it, my brother was basically murdered.

The experimental drugs used to battle AIDS only made him worse. Even some of the doctors seemed to have a what’s-the-use attitude. Some of these things made losing him even more painful.

Since his passing, I’ve searched for some reason for his life and death. Although there may not be a complete answer to my question, I believe that there was a purpose. Brad taught us many things. He is still teaching people, even now, with the story of his life. I told his story to someone just the other day, and that person learned something.

Brad was a person who always fought for what he believed in. He taught his friends and family members not to give up. He never gave up, and he never gave in to his hemophilia. Although Brad was special because of it, he never wanted to be treated special. He would play basketball with the heart of Larry Bird, but the body of a hemophiliac. Those who watched him play for his elementary school team would see him limping up and down the court, trying his hardest.

Out of respect for his memory, we have not given up. My family and I have taken an active part in helping to make a difference in the way that people with hemophilia and AIDS are treated. We have been interviewed on the television program, 60 Minutes. We have gone to Washington D.C. twice, fighting for the Ricky Ray Bill to be passed by Congress. This bill would help families who have been through similar or worse situations. The bill was named for a boy who was taken out of school because he had AIDS. People who were afraid of AIDS and thought they could get it from him burned down his family’s home. The people didn’t understand that people can get AIDS from tainted blood donations.

My brother gave so much love and happiness to so many people while he was alive, that his death left us feeling empty and sad. Before he was infected with AIDS, my big brother, Brad, was my protector and the person I would tell all my secrets to. Brad can no longer protect me, or even talk to me, and I miss him every day.

Since Brad’s death I’ve come to realize that God was not punishing my family for anything. He simply had given us a gift of love – my brother, Brad – that had to be taken back. With these lessons from God, I can continue with my journey – this journey called life – with the hope that everyone with whom I share Brad’s story will learn exactly how precious life is.
```

---

## IC-2280: Let’s Pretend This Never Happened

- Title: Let’s Pretend This Never Happened
- Author (byline): Jenny Lawson
- Work: Not specified
- Publisher: Berkley Trade
- Publication date as stated: March 2013
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1419
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jenny Lawson|
ISBN: 978-0425261019
Publisher: Berkley Trade
Date (Month/Year): March 2013
```

### Introduction (context only: never use it for content warnings)

```text
Author Jenny Lawson had an over-eccentric, anxiety-causing father who would never-endingly bring into her life a circus of animals, people, and Avis (Latin for Birds). She recounts a story from third grade that put her on the road to self-confidence. Her advice to all of us? You never know who or what might teach you a valuable lesson.

Let’s Pretend This Never Happened by Jenny Lawson.
```

### Performance text (classify this)

```text
(From the Chapter Jenkins, You Mother F****, Pg 43-53)

When I was little, my mother used to say that I <was> “nervous.”

Most children didn’t hyperventilate when asked to leave the house. My teachers whispered “neurotic.” But deep down I knew there was a better word for what I was. Doomed.

Doomed because I couldn’t give a speech in class without breaking into uncontrollable hysterical laughter. Doomed because I knew, without a shadow of a doubt, that something horrible and nameless was going to happen and that I was helpless to stop it.

When I was in third grade, my father rushed inside one night to tell us all to come out and look at what he had in the back of his pickup. I was young, but still well trained enough to know that nothing good could come of this.

My mother peered guardedly to see whether anything large was moving in my father’s truck. It was. She gave us a look that my father always seemed to interpret as “How lucky you girls are to have such an adventurous father,” but which I always read as “One of you will probably not survive your father’s enthusiasm.”

Usually when my father wanted us to come outside to see what was in the bed of his truck, it was only because whatever was in there was either too bloody and/or vicious for him to carry inside, so we all stayed in the relative safety of our house and asked a series of questions designed to indicate the level of danger of whatever Daddy would be exposing us to.

My Father was perpetually disappointed by our lack of trust.

My mother braced herself with a deep breath and leaned forward to uneasily to stare into the eyes of a dozen grim live birds. A few squawked indignantly, but most huddled numbly in the corner, no doubt shell-shocked from the windblown journey, coupled with being forced to share the pickup bed with several animal carcasses my father had probably picked up for taxidermy work. To the birds I assume it must’ve been very much like accepting a ride from a stranger, only to get in the back of the van to find several murdered hikers who were being made into lamp shades.

My father explained that the birds were well-behaved Wisconsin jumbo quail, and my mother countered that the birds were, in fact, rowdy turkeys.

Those birds loved my father with a white-hot passion.

As the months wore on, the turkeys grew bigger and louder and more obnoxious, and would roost on low tree branches, screaming at my mother every time she left the house. My father insisted that the quails were just eccentric, and that we were misinterpreting the loud, angry gobbling, which he maintained was simply the birds singing with joy.

My father insisted on naming the turkeys and treating them like pets. Pets who would angrily run at you in full-out attack, nipping at your tiny ankles as you ran in circles around the yard, screaming for someone to open the door to the house and let you in.

We lived on a rural route, so our mailman was fairly used to being besieged by stray dogs, but he’d been utterly unprepared for an angry turkey attack.

My father lifted the large bird off the hood <of his mail truck>, and tucked him under his arm, saying “Sir, this bird is a quail. And his name is Jenkins.”

I was not surprised when we found a note in our mailbox, informing us that all further packages would be left by the mailbox rather than being delivered to the door. This was upsetting to my mother, because the mailman’s idea of leaving packages at the mailbox was him flinging our mail in the general direction of the house. The turkeys adapted to this by quickly gathering up the mail in the yard, which would have been helpful if they’d brought it to the house like a dog, but instead they’d carry the letters around proudly, as if they were important turkey documents that my mother was attempting to steal from them.

My sister and I began putting together a defensive strategy to protect us from bird assault.

Lisa and I attempted to fashion ankle armor out of empty soup cans that we’d opened on both sides, but my feet were too big to fit into them, and Lisa’s feet were so little that when she ran, the tin cans would clink loudly together and simply attract the attention of the vicious herd. She was basically like a tiny, pigtailed dinner bell. I considered telling her that the ankle armor wasn’t helping, but that was tantamount to telling a fellow zebra that he’s covered in steak sauce right before you both have to cross a parking lot full of loins. Self-preservation is a narcissistic bedfellow.

Occasionally the turkeys would follow us, menacingly, on our quarter-mile walk to school, lurking behind us like improbable gang members. Even at age nine I was painfully self-conscious, and was aware that dysfunctional pet turkeys would not be viewed as “cool,” so I would always duck inside the school-house as quickly as possible and feign ignorance, conspicuously asking my classmates why there were always jumbo quail on the playground.

This worked perfectly until the morning when I ducked inside the school lobby a little to sluggishly, and Jenkins blithely followed me in, gobbling to himself and looking both clueless and vaguely threatening. Two other turkeys followed behind Jenkins. I quickly ran into my classroom as the turkeys wandered aimlessly into the library. I sighed in relief that no one had noticed the turkey expedition, until an hour later, and we discovered that the principal and librarian had found the turkeys. They had managed to shit <Poop> everywhere. It was actually a little bit impressive, and also horribly revolting. The principal had seen the turkeys follow us to school before, so he called my father and demanded that he come to the school to clean up the mess. My father explained to the principal that he must be mistaken, because he was raising jumbo quail, but the principal wasn’t buying it.

A half-hour later, when my class lined up to go to PE, I found my father on his knees, cleaning up poop. He was unsuccessfully attempting to shoo the turkeys away, forcefully yelling, “GO HOME, JENKINS.”

I froze, but it was too late. Jenkins recognized me immediately and ran up to me, gobbling with excited recognition like, “OH MY GOD, ISN’T THIS AWESOME? WHO ARE YOUR FRIENDS?”

And for the first time I didn’t run screaming from him. Instead I sighed and waved weakly, mumbling dejectedly, “Hey, Jenkins,” as my classmates stared at me in amazement. But not the good kind of amazement, it was more of the bad kind of amazement. Like when you realize that not having the right kind of leg warmers is really small potatoes compared to being assaulted by an overexcited turkey named Jenkins. I think this was the point when I realized that I was kind of *doomed* when it came to ever becoming the most popular kid in the class, and so I just nodded to Jenkins and my father, and I held my head up high as I walked down the hall and tried not to slip in the feces.

All the rest of that day I waited for the taunting to come, but it never did. It was pretty obvious there was no way to turn me into a “normal” third-grader.

And actually? <I was> a little relieved too. Because it was the first time in my life that I gave myself permission to be me. I was still shy and self-conscious and terrified of people, but Jenkins had essentially freed me of the bonds of having to try to fit in.

Soon afterward, Jenkins and the other turkeys disappeared from our lives, but the lessons I learned from them sill remain: Turkeys make terrible pets, you should never trust your father to identify poultry, and you should accept who you are, flaws and all, because if you try to be someone you aren’t, then eventually some turkey is going to *poop* all over your well-crafted façade, so you might as well save yourself the effort. And so I guess, in a way, I owe Jenkins a debt of gratitude, because (even if it was entirely unintentional) he was a brilliant teacher.

And also? Totally delicious.

NOTE: <> Bracketed words are added as transition words

by editor
```
