# Classification request: batch 49 of 53 (40 records, IC-2321 to IC-2360)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-049-reply.json`.

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

## IC-2321: Seriously, Cinderella is So Annoying!

- Title: Seriously, Cinderella is So Annoying!
- Author (byline): Trisha Shaskan
- Work: Not specified
- Publisher: Capstone Press
- Publication date as stated: August 2011
- Event as filed: Prose
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
2021 National Qualifier – MS
2022 National Qualifier – MS
NIETOC
```

### Introduction (context only: never use it for content warnings)

```text
Every story has two sides. It just so happens that we usually hear from the victim’s or protagonist’s point of view. In the classic retelling of the Cinderella story, the Stepmother has her own opinion of miss goody-two-shoes in. . .

Seriously, Cinderella is So Annoying!: The Story of Cinderella as Told by The Wicked Stepmother by Trisha Shaskan.
```

### Performance text (classify this)

```text
STEPMOTHER: You must have heard of me. The wicked stepmother? That’s not true. It’s just another one of Cinderella’s wild stories. Not as wild as the one about the pumpkin, or the one about the fairy godmother. The real story, the true story, began with some chatter-and some dust.

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

The prince and the girl danced and pranced while my darlings were left prince-less

A few days later, the prince made an announcement: a glass slipper was left at the castle. The prince would marry the girl whose foot it fitted. Our big chance! After visiting every other mansion in the city, the prince’s footman arrived at the door.

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

## IC-2322: Sex and the Single Mom

- Title: Sex and the Single Mom
- Author (byline): Emily Listfield
- Work: Not specified
- Publisher: Redbook Magazine
- Publication date as stated: October 2006
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 997
- Already set (do not supply): none

### Source block (context only)

```text
Author: Emily Listfield
ISBN: B00005N7SG
Publisher: Redbook Magazine
Date(Month/Year): October 2006
```

### Introduction (context only: never use it for content warnings)

```text
After 10 years of marriage and a year of mourning her husband’s death, Emily ventures out for her first date in years – and her first blind date EVER. Sex and the Single Mom by Emily Listfield.
```

### Performance text (classify this)

```text
I am about to head out on the first blind date of my life and I’m feeling crazily optimistic (“Crazy” being the operative word). Anyone with a shred more dating experience than me (and that includes most women over the age of, say, 14) can tell you that the proper attitude toward a blind date is one of extreme caution, with perhaps just a soupcon of hope. Bu the last time I went on any kind of date it was a different century, literally. There might have been shoulder pads involved. So I’m approaching blind dating with rose-colored blinders on.

This was all my boss Sally’s idea. It was time, she decided, for me to “get out there.” She began to give my phone number to every eligible (read: single and under 80) man she ran across. (Yes, I agreed to this plan. I was a widow with a full-time job and a 6-year-old daughter – I wasn’t exactly hanging out in bars meeting people.) Sally met Mark at a cocktail party, and after a 10-minute chat, during which she confirmed that he had no arrest record, she promptly gave him my number.

Mark’s specs seemed great – early 40s, divorced, steady job, handsome (according to Sally, whose word I will never take on anything again. Ever). When he called the next day, I agreed to go out to dinner and the theater. This was a major rookie error. RULE #1: Never meet a blind date for more than coffee or drinks and, for added insurance, have a friend call 20 minutes into it so you can claim a babysitting emergency if necessary. (“Her fever is how high? I’ll be right home.”)

Five minutes before I have to leave for my big date, I stand in the living room for a last-minute outfit check by my daughter, Sasha, and babysitter, Joyce.

We are all a little giddy. This is an adventure for them, too, after all. I have bought a new dress for the first time in months, and do a little twirl for their approval. RULE #2: Do not- I repeat, do not – go in for major shopping before a blind date. If the evening goes well, you’ll be sorry you didn’t save your clothing allowance for the all-important second date. If it doesn’t, you’ll be exceedingly cranky when your American Express bill arrives.

I am about to leave when Sasha races to her room and comes back with a drawing of a brilliant-hued rainbow. “If you like him, give it to him,” she instructs gravely. “If not, bring it home.” (Clearly, we are both very new at this. This kind of raw hopefulness will not surface again.) I carefully fold it and put it in my bag. I envision this act of generosity becoming part of “our” story, the one Mark and I will tel in years to come of the night we met. I kiss Sasha and head out.

Mark is waiting for me in front of the theater. From a distance, he looks exactly as Sally described him: six feet tall, dark suit, full head of hair, handsome. I don’t know what all my single friends are complaining about – I’m loving this dating thing. As I get closer, though, the image begins to go seriously awry. Mark is wearing a three-inch-wide neon Winnie the Pooh tie. With Tigger. An enormous, shocking pink Tigger that takes up half his chest. He does not seem particularly glad to see me either. In fact, he looks downright bored before we’ve even gotten through the hellos. Nevertheless, I decide to overlook his sartorial misjudgment (ties can always be “lost by the dry cleaner”) and his surliness. I smile gamely and we head to dinner – at an Arby’s across the street. Listen, I don’t need the Four Seasons, but I was envisioning something with cloth napkins.

Conversation does not exactly flow. Mark sits sullenly and doesn’t ask me a single question about my life; I try to pick up the slack. I have been known to get information out of a 6-year-old, I think to myself; I should be able to do this. Two minutes into it, though, Mark starts twitching and head-bobbing maniacally. I’m not talking a little tick, I’m talking Tourette’s. Le me go on record as saying I have nothing against neurological disorders – though it might have been nice if Sally had warned me. But this does bring up some etiquette issues. Am I supposed to pretend it isn’t happening? Tell him, “That’s okay, I bight my nails.”? (Before you start feeling sorry for him, let me add that the only piece of information I really get out of him the entire evening is that he’s involved in some quasi-religious cult.)

While Mark mumbles something about a rebirthing class that changed his life, all I can thin about is what will happen if he starts to bark in the theater. I have one moment of hope on the walk over, when the twitching stops. I quickly figure out that he doesn’t twitch standing up, only sitting down. (This, by the way, is Sally’s defense. She only say him standing.) Unfortunately, it’s hard to avoid sitting down at the theater. I fantasize about going to the bathroom and not coming back, but even under extreme circumstances, that seems just a little too, well, extreme.

Somehow, I make it through what feels like the longest play in the history of the western world – sans barking (though I am a little motion sick from sitting next to his shaking chair). Out on the street, Mark clearly has as little interest in continuing the evening as I do. He barely offers to walk me to a cab. We say goodnight without looking each other in the eye.

The next morning I take the drawing from my bag, smooth it out, and give it back to Sasha. She looks crest-fallen. “This dating thing might be a little more complicated than I thought,” I tell her gently. “Why?” she asks. “Well, I have to find someone I love who loves me. And you.” She considers this. “How long do you think that will take?” she demands?

Six years later, I’m still at it. (No, I can’t believe it, either.) I have gone on many more blind dates (though not through Sally, thank you very much). I’ve met one man I wanted to commit to, and others I’ve wanted to have committed. Twitch, as we have come to call my first blind date, has become part of our story – Sasha’s and mine. RULE #3: Don’t tell your child about every date (blind or otherwise) you go on. She will a) risk developing an unhealthy pessimism about romance when she sees how many don’t pan out, and b) will never look at Winne the Pooh in quite the same way again. Worst of all, she will tease you mercilessly about every date for years to come.
```

---

## IC-2323: The Shawl

- Title: The Shawl
- Author (byline): Cynthia Ozick
- Work: The Shawl
- Publisher: Vintage
- Publication date as stated: August 1990
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2018
- Already set (do not supply): none

### Source block (context only)

```text
Author: Cynthia Ozick
Book: The Shawl
ISBN: 978-0679729266
Publisher: Vintage
Date (Month/Year): August 1990
```

### Introduction (context only: never use it for content warnings)

```text
In a Nazi death camp, survival becomes one’s main concern. For Jews, a scrap of food, a bit of warmth, a minute or two of rest is worth more than gold. Prolonging life – even just one day – is a monumental accomplishment. This goal is purely selfish…unless you’re a mother. A Jewish mother puts the life of her baby above all else in “The Shawl” by Cynthia Ozick
```

### Performance text (classify this)

```text
“It was a magic shawl, it could nourish an infant for three days and three nights.”

Stella, cold, cold, the coldness of hell. How they walked on the roads together, Rosa with Magda curled up between her sore breasts, Magda wound up in the shawl. Sometimes Stella carried Magda. But she was jealous of Magda. A thin girl of fourteen, too small, with thin breasts of her own, Stella wanted to be wrapped in a shawl, hidden away, asleep, rocked by the march, a baby, a round infant in arms. Magda took Rosa’s nipple, and Rosa never stopped walking, a walking cradle. There was not enough milk; sometimes Magda sucked air; then she screamed. Stella was ravenous. Her knees were tumors on sticks, her elbows chicken bones.

Rosa did not feel hunger; she felt light, not like someone walking but like someone in a faint, in trance, arrested in a fit, someone who is already a floating angel, alert and seeing everything, but in the air, not there, not touching the road. As if teetering on the tips of her fingernails. She looked into Magda’s face through a gap in the shawl: a squirrel in a nest, safe, no one could reach her inside the little house of the shawl’s windings. The face, very round, a pocket mirror of a face: but it was not Rosa’s bleak complexion, dark like cholera, it was another kind of face altogether, eyes blue as air, smooth feathers of hair nearly as yellow as the Star sewn into Rosa’s coat. You could think she was one of their babies.

Rosa, floating, dreamed of giving Magda away in one of the villages. She could leave the line for a minute and push Magda into the hands of any woman on the side of the road. But if she moved out of line they might shoot. And even if she fled the line for half a second and pushed the shawl-bundle at a stranger, would the woman take it? She might be surprised, or afraid; she might drop the shawl, and Magda would fall out and strike her head and die. The little round head. Such a good child, she gave up screaming, and sucked now only for the taste of the drying nipple itself. The neat grip of the tiny gums. One mite of a tooth tip sticking up in the bottom gum, how shining, an elfin tombstone of white marble gleaming there. Without complaining, Magda relinquished Rosa’s teats, first the left, then the right; both were cracked, not a sniff of milk. The duct-crevice extinct, a dead volcano, blind eye, chill hole, so Magda took the corner of the shawl and milked it instead. She sucked and sucked, flooding the threads with wetness. The shawl’s good flavor, milk of linen.

It was a magic shawl, it could nourish an infant for three days and three nights. Magda did not die, she stayed alive, although very quiet. A peculiar smell, of cinnamon and almonds, lifted out of her mouth. She held her eyes open every moment, forgetting how to blink or nap, and Rosa and sometimes Stella studied their blueness. On the road they raised on burden of a leg after another and studied Magda’s face. “Aryan,” Stella said, in a voice grown as thin as a string; and Rosa thought how Stella gazed at Magda like a young cannibal. And the time Stella said “Aryan,” it sounded to Rosa as if Stella had really said “Let us devour her.”

But Magda lived to walk. She lived that long, but she did not walk very well, partly because she was only fifteen months old, and partly because the spindles of her legs could not hold up her fat belly. It was fat with air, full and round. Rosa gave almost all her food to Magda, Stella gave nothing; Stella was ravenous, a growing child herself, but not growing much. Stella did not menstruate. Rosa did not menstruate. Rosa was ravenous, but also not; she learned from Magda how to drink the taste of a finger in one’s mouth. They were in a place without pity, all pity was annihilated in Rosa, she looked at Stella’s bones without pity. She was sure that Stella was waiting for Magda to die so she could put her teeth into the little thighs.

Rosa knew Magda was going to die very soon; she should have been dead already, but she had been buried away deep inside the magic shawl, mistaken there for the shivering mound of Rosa’s breasts; Rosa clung to the shawl as if it covered only herself. No one took it away from her. Magda was mute. She never cried. Rosa hid her in the barracks, under the shawl, but she knew that one day someone would inform; or one day someone, not even Stella, would steal Magda to eat her. When Magda began to walk Rosa knew that Magda was going to die very soon, something would happen. She was afraid to fall asleep; she slept with the weight of her thigh on Magda’s body; she was afraid she would smother Magda under her thigh. The weight of Rosa was becoming less and less; Rosa and Stella were slowly turning into air.

Magda was quiet, but her eyes were horribly alive, like blue tigers. She watched. Sometimes she laughed—it seemed a laugh, but how could it be? Magda had never seen anyone laugh. Still, Magda laughed at her shawl when the wind blew its corners, the bad wind with pieces of black in it, that made Stella’s and Rosa’s eyes tear. Magda’s eyes were always clear and tearless. She watched like a tiger. She guarded her shawl. No one could touch it; only Rosa could touch it. Stella was not allowed. The shawl was Magda’s own baby, her pet, her little sister. She tangled herself up in it and sucked on one of the corners when she wanted to be very still.

Then Stella took the shawl away and made Magda die.

Afterward Stella said: “I was cold.”

And afterward she was always cold, always. The cold went into her heart: Rosa saw that Stella’s heart was cold. Magda flopped onward with her little pencil legs scribbling this way and that, in search of the shawl; the pencils faltered at the barracks opening, where the light began. Rosa saw and pursued. But already Magda was in the square outside the barracks, in the jolly light. It was the roll-call arena. Every morning Rosa had to conceal Magda under the shawl against a wall of the barracks and go out and stand in the arena with Stella and hundreds of others, sometimes for hours, and Magda, deserted, was quiet under the shawl, sucking on her corner. Every day Magda was silent, and so she did not die. Rosa saw that today Magda was going to die, and at the same time a fearful joy ran in Rosa’s two palms, her fingers were on fire, she was astonished, febrile: Magda, in the sunlight, swaying on her pencil legs, was howling. Ever since the drying up of Rosa’s nipples, ever since Magda’s last scream on the road, Magda had been devoid of any syllable; Magda was a mute. Rosa believed that something had gone wrong with her vocal cords, with her windpipe, with the cave of her larynx; Magda was defective, without a voice; perhaps she was deaf; there might be something amiss with her intelligence; Magda was dumb. Even the laugh that came when the ash-stippled wind made a clown out of Magda’s shawl was only the air-blown showing of her teeth. Even when the lice, head lice and body lice, crazed her so that she became as wild as one of the big rats that plundered the barracks at daybreak looking for carrion, she rubbed and scratched and kicked and bit and rolled without a whimper. But now Magda’s mouth was spilling a long viscous rope of clamor.

“Maaaa—“

It was the first noise Magda had ever sent out from her throat since the drying up of Rosa’s nipples.

“Maaaa…aaa!”

Again! Magda was wavering in the perilous sunlight of the arena, scribbling on such pitiful little bent shins. Rosa saw. She saw that Magda was grieving for the loss of her shawl, she saw that Magda was going to die. A tide of commands hammered in Rosa’s nipples: Fetch, get, bring! But she did not know which to go after first, Magda or the shawl. If she jumped out into the arena to snatch Magda up, the howling would not stop, because Magda would still not have the shawl; but if she ran back into the barracks to find the shawl, and if she found it, and if she came after Magda holding it and shaking it, then she would get Magda back, Magda would put the shawl in her mouth and turn dumb again.

Rosa entered the dark. It was easy to discover the shawl. Stella was heaped under it, asleep in her thin bones. Rosa tore the shawl free and flew—she could fly, she was only air—into the arena. The sunheat murmured of another life, of butterflies in the summer. The light was placid, mellow. On the other side of the steel fence, far away, there were green meadows speckled with dandelions and deep-colored violets; beyond them, even father, innocent tiger lilies, tall, lifting their orange bonnets. In the barracks they spoke of “flowers,” of “rain”: excrement, thick turd-braids, and the slow stinking maroon waterfall that slunk down from the upper bunks, the stink mixed with a bitter fatty floating smoke that greased Rosa’s skin. She stood for an instant at the margin of the arena. Sometimes the electricity inside the fence would seem to hum; even Stella said it was only an imagining, but Rosa heard real sounds in the wire: grainy, sad voices. The farther she was from the fence, the more clearly the voices crowded at her. The lamenting voices strummed so convincingly, so passionately, it was impossible to suspect them of being phantoms. The voices told her to hold up the shawl, high; the voices told her to shake it, to whip it, to unfurl it like a flag. Rosa lifted, shook, whipped, unfurled. Far off, very far, Magda leaned across her air-fed belly, reaching out with the rods of her arms. She was high up, elevated, riding someone’s shoulder. But the shoulder that carried Magda was not coming toward Rosa and the shawl, it was drifting away, the speck of Magda was moving more and more into the smoky distance. Above the shoulder a helmet glinted. The light tapped the helmet and sparkled it into a goblet. Below the helmet a black body like a domino and a pair of black boots hurled themselves in the direction of the electrified fence. The electric voices began to chatter wildly. “Maamaa, maaamaaa,” they all hummed together. How far Magda was form Rosa now, across the whole square, past a dozen barracks, all the way on the other side! She was no bigger than a moth.

All at once Magda was swimming through the air. The whole of Magda traveled through loftiness. She looked like a butterfly touching a silver vine. And the moment Magda’s feathered round head and her pencil legs and the balloonish belly and zigzag arms splashed against the fence, the steel voices went mad in their growling, urging Rosa to run and run to the spot where Magda had fallen from her flight against the electrified fence; but of course Rosa did not obey them. She only stood, because if she ran they would shoot, and if she tried to pick up the sticks of Magda’s body they would shoot; so she took Magda’s shawl and filled her own mouth with it, stuffed it in and stuffed it in, until she was swallowing up the wolf’s screen and tasting the cinnamon and almond depth of Magda’s saliva; and Rosa drank Magda’s shawl until it dried.
```

---

## IC-2324: Sickened

- Title: Sickened
- Author (byline): Julie Gregory
- Work: Not specified
- Publisher: Bantam Books, Inc.
- Publication date as stated: Sept 2004
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: JULIE, MOM, DOCTOR, NURSE
- Teaser before the introduction: Yes
- Spoken words (computed): 2111
- Already set (do not supply): none

### Source block (context only)

```text
Author: Julie Gregory
ISBN: 978-0553381979
Publisher: Bantam Books, Inc.
Date (Month/Year): Sept 2004
```

### Introduction (context only: never use it for content warnings)

```text
A young girl is perched on the cold chrome of yet another doctor’s examining table, missing yet another day of school. It’s four o’clock and she hasn’t been allowed to eat anything all day. Her mother, on the other hand, seems curiously excited. She checks her teeth once more for lipstick, and as the doctor enters, shoots the little girl a warning glance. This child will not ruin her plans . . . Munchausen by Proxy is a type of child abuse in which a parent exaggerates, fabricates, or induces symptoms of a medical condition in a child that leads to unnecessary and potentially harmful medical care. Julie Gregory was a victim . . . and this is her story:

Sickened by Julie Gregory.
```

### Performance text (classify this)

```text
JULIE: (Pg 3) For starters, I was a sick kid. Bean-pole skinny, I bruised easy and wilted in a snap. Kids in school used to walk straight up to me and ask point-blank if I was anorexic. But I wasn’t; just sick. And Mom bent over backwards trying to find out what was wrong with me. It wasn’t just that I had a heart problem. It was everything rolled into one, bleeding together with so many indistinguishable layers that to get to the root of it was impossible, like peeling off every layer of an onion, and when I got old enough to peel the onion myself, every layer made me cry.

MOM: (Pg 4) Look, dammit, this kid is sick, all right? Just look at her. And so help me God, if she dies on me because you can’t find anything wrong with her, I’ll sue you for every sent you got.

JULIE: Her voice trailed after any doctor who said no more tests could be done, stalked him down the corridor, sliced through the silence of the hallway. (to Mom)

Don’t worry, Mom. It’s okay. We’ll go find another one.

MOM: Look, I’m sacrificing my life to find out what the hell is wrong with you. So stop *screwing* it up when we get in here by acting all normal. Show them how sick you are, okay?

JULIE: (Pg 23) Today, I’m back at [the doctor] getting seen for my headaches. Mom and I sit in the examining room, waiting.

MOM: How do you act when you’re sick, Julie? Show me.

JULIE: (slouches, limbs dangling, tongue out and bottom lip away from her teeth, a glazed expression on her face)

MOM: That’s right. Now what do you think the doctor is going to say if he comes in here and you’re sitting up and all smiling? Do you think he’s going to believe me that you’re sick? You got to show him how sick you are.

(Doctor enters)

DOCTOR: So you say Julie’s been running a fever along with some sore throats? (taking notes in Julie’s chart)

MOM: (Pg 26-27) Well, I’ve caught it up at a hundred and one, but it seems to be low grade all the time and she has these, oh, I don’t know what you’d call them, headaches, I guess, don’t you Julie?

JULIE: I look between both of them. What is a headache exactly? Is it when my eyes hurt? Is it when I’m dizzy on the bus? I’m trying to guess, hoping it’s the right answer. (to Mom and Doctor) I’m not really sure.

MOM: Jesus, Julie, we’ve been seeing you sick and you’ve been telling me you’ve had headaches in the car all this week. Remember when you’ve been carsick? (to Doctor) There’s got to be something wrong with a kid that doesn’t even remember how sick she was just yesterday. (to Julie) Julie, stop wasting the man’s time and tell him what’s going on with you. (threateningly) I mean it!

JULIE: (Pg 28-29) Another week has gone by and nothing has changed. Mom and I sit in [the doctor’s] office waiting for Dr. Phillips.

MOM: Now, we’re going to tell Dr. Phillips about the dull pains in your head, right about (pushes fingers into Julie’s skull, hard) here. I don’t want any kind of fiasco like we had the last time, okay? I’m the mom: I know what’s going on here. So if he asks you questions, you just let me answer.

JULIE: Dr. Phillips breezes in and apologizes for our wait. Mom gives him an update on my allergy diet and pulls out her list of new symptoms. I sit in my sick pose. As she runs down the symptoms, I know some of them aren’t true. (Pg 30) No, I don’t have a sore throat every day, just yesterday. No, my fever last night wasn’t way up to 102. No, I don’t go to the school nurse every single day . . . [In fact] (Pg 32) it was usually after Mom slipped the little white pill under my tongue that my migraines got worse.

MOM: I can tell you’ve got a headache coming on. Here, open up. Lift your tongue. Goooood.

JULIE: Sometimes I about threw up. Most times I just needed to climb back into bed . . . (Pg 50-51) [Three years pass and] when fifth grade begins, Dr. Phillips prescribes us more migraine medicine and gives us the names of specialists who can see me for the rest of my symptoms. He tells us we should [find] somebody who can handle a case that’s as complicated as mine’s getting. And then he leaves. He just walks right out before Mom is even done running down the list she brought.

MOM: I can’t believe that. Did you see him, Julie? He just walked out on us! Well, if he’s going to treat me like that, Jesus!

JULIE: (resigned) Don’t worry, Mom, we’ll just go find another one. (Pg 52) (to audience) That night Mom curls up on the sofa, with her grocery store reading glasses hanging on to the tip of her nose, cornering through the pages of the thick Medical Journal for Home Use Manual. (to Mom) Whatcha doing, Mommy?

MOM: Well, you’re sick again, hon, and this book is helping Mommy figure out what’s wrong with you. You got a lot of the symptoms in here, but there’s all kinds of tests that’ll help us rule out some of the more serious diseases.

JULIE: [Later that night] (Pg 84-86) the doorknob on my bedroom door slowly squeaks open. Mom tiptoes to the edge of my bed. That’s when I notice the gun in her mouth. (Julie enters flashback ad responds immediately with a look of horror) She looks at me with her tear-streaked, puffy face, her eyes terrified like an animal in a chute, and raises her hand to cock the trigger. “Mommy, Mommy, Mommy!” (to audience) I shoot from under the covers and start crying on cue. Mimic and match. If I mirror her with an appropriate response, she’ll be distracted from the gun.

MOM: (she slides the gun out of her mouth) You want me to kill myself, don’t you? You hate me. I’m such a bitch, such a nag as your father says, and you hate me, that’s what he says.

JULIE: She drops the gun to her lap. I cling around her like a baby monkey. (To Mom) Mom, if you don’t live then I can’t live. Okay? Okay? Who would take care of me when I’m sick; who would take me to the doctor? (to audience) I hang on to her, slipping the gun so lightly from her lap she doesn’t notice, sliding it under my blankets. (To Mom) It’s okay, it’s okay, Mom. (to audience) And the harder I cry, the less my beautiful mother, who I could never live a second without, does. And then she stops altogether, straightens up, gives my knee a little squeeze and says

MOM: (in an upbeat mood; cheerful) Hey, thanks for listening, Sis. You better get to sleep now, honey.

JULIE: And she leaves me on the edge of my mattress with a loaded gun under my covers. [*Spoken Transition -- A few weeks later]

DOCTOR: (Pg 97-101) There’s a substantial difference in Julie’s heart rate when she stands up from when she’s at rest, Ms. Gregory.

MOM: (to Julie) Tell her how out of breath you are, Julie. (to doctor) She’s always out of breath around the farm, Dr. Kate. Jesus! (slaps her knee) This explains everything. (to Julie) You look like you’re about ready to pass out, hon. Don’t you feel like you could pass out?

DOCTOR: I think we might have something for the hospital here, something that could be detected with simple EKG or a heart exam. They might even want to attach something called a Holter monitor on her overnight to see the longer rhythms of her heart. I’ll call over to the cardiac unit and get you set up.

MOM: Yess – Yeeeessss! (gleefully) Finally, we’re getting somewhere. (to Julie) I knew there was something major going on with you!

JULIE: We’re going to the hospital! At last, I’ll just take one medication that will fix everything. I’ll have friends, be in sports, go to movies. And I’ll be a real kid and not miss school anymore. I’ll do good in school like before I got sick. I’m [only] failing because there’s always something wrong with me. [*Spoken Transition -- After the cardiac tests]

DOCTOR: (Pg 101) Well, Ms. Gregory, we’ve got good news. The Holter monitor shows no significant findings that lead us to believe Julie has a heart condition requiring further tests.

MOM: What? What do you mean, you can’t find anything. This kid had a racing heart and was out of breath all the time. Are you trying to tell me that this kid is normal? That I’m making this up? Well, let me tell you. I’m going to find a doctor competent enough to find out what’s wrong with her, you understand me?

JULIE: (Pg 104-105) The older I got, the worse I got. My possible conditions expanded to include genetic disorders and heart valve malfunctions. And the medications to treat them piled up in the kitchen cabinets. Sometimes I don’t take any, sometimes I get a double dose. I just feel sick all the time. Queasy, nauseated, clammy, stupid. . . By the time I was in Junior High, Mom decided I was allergic to a lot of things.

MOM: Julie, what the heck are you doing with those [eggs]? You know you’re allergic.

JULIE: I slide the eggs back and reach for the bacon.

MOM: At-at-at, we just got done telling Dr. Kate how meat makes you sick. Why don’t you just have a bowl of Sugar Pops? But use the powdered milk, just enough to get them wet, you could be lactose intolerant.

JULIE: (Pg 111) How long can you starve without side effects? If everyone around you tells you you’re sick, if they keep testing you for what’s making you sick, do you think, when you’re thirteen, that you aren’t? You feel sick, right? You can’t keep up; you’re tired. Is it the wrong mediation that makes you sick? Or the three different kinds you take all at once? . . . . (Pg 113-114) We’re on our way to a new cardiologist. This will be the third and if he can’t find anything, Dr. Kate says it’s probably not my heart.

MOM: I’ll show those goddam no-good sons a bitches at the hospital that I’m not crazy. You are sick, goddammit, you’ve got a heart problem. (glaring at Julie) C’mon now, let’s get in there, and I mean now, goddammit. You are going to tell him what’s wrong with you. Sharp chest pain. Shortness of breath. You got it? [*Spoken Transition -- So more tests are run and when the results come back . . . ]

DOCTOR: (Pg 115-116) Well, it looks like what we’ve got here is a possible case of periodic rapid heart action.

MOM: Does that mean we’ll have to go in for open-heart? I mean seriously, I’m not opposed to it if we can really find out what’s going on here. I’ve been reading up on a new pediatric valve syndrome, and . . .

DOCTOR: Oh, no, I don’t think we’re going to need that. What we really should do is some more tests under the close eye of hospital staff. Could we get Julie into Ohio State for a week and run a comprehensive assessment? [*Spoken Transition -- After 4 days in the hospital]

NURSE: (Pg 121-124) We’re going to have to shave you now, honey. Down here. (pats for Julie’s pubic bone)

JULIE: What? I’m done, I’m going home. I don’t have anything down there! (covering her private parts) I’m here for my heart!

NURSE: Tomorrow they’re going to make a little incision in the vein of your arm and the artery of your thigh and run some electrical connectors into the values of your heart so they can see it on TV.

JULIE: (to audience) This has got to be a mistake. How did this happen? They’re going to cut me. (breath quickens, as Julie’s eyes widen in horror – To nurse) You, you can’t do this to me. You can’t do it . . . My mother is making it up! (long horrified pause then to audience) I can’t believe I blurted that out. My mother loves me. There’s something wrong with me. If I wasn’t sick the doctors wouldn’t keep trying to fix me . . . Maybe I was acting sicker because [mom] slammed my head against the inside of the window on the way home if I didn’t show them how sick I was.

NURSE: (puzzled) Be back in a sec. Let me see what’s going on.

JULIE: Mom’ll be furious! . . . I don’t care. I can run away. Find a new family. . . . [No,] Mom knows what she’s doing. She’s the one who sees my symptoms.

(Pg 131) Heart surgery, iodine injections, tubes shoved, slits sliced, blood drawn. These things change a kid. You forget what you were like before they cut you, before they shaved you. You only look to the future when they’ll find what’s wrong so it can all be over; the tests, the trying, the meds you swallow without knowing why.

[Today, as an adult] (Pg 221-222) I cry from the guilt of betraying my mother, for not keeping the shroud of her secrets. I have been writing about what it feels like to be cut open while your mother’s tight, thin smile mouths, “Doctor’s orders, honey.” And to believe you are genuinely ill because that is what everything in your world mirrors back to you. I still told myself that it was okay, it really wasn’t that bad . . . [after all,] if a doctor couldn’t decipher what she did, how could I?
```

---

## IC-2325: Silhouettes

- Title: Silhouettes
- Author (byline): Janet O’Neill
- Work: Turning Points
- Publisher: Tichenor Publishing
- Publication date as stated: 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: SARAH, MOM, JEFF
- Teaser before the introduction: Yes
- Spoken words (computed): 907
- Already set (do not supply): none

### Source block (context only)

```text
Author: Janet O’Neill
Book: Turning Points
Publisher: Tichenor Publishing
ISBN: 978-0742117013
Date: 2001
```

### Introduction (context only: never use it for content warnings)

```text
Recent statistics have shown that one in three teenagers has experienced abuse in a dating relationship. Further statistics show that in the majority of these cases, the victim did nothing to try to stop or prevent the abuse. However, the statistics mean nothing compared to the psychological agony a victim suffers. This agony is brought to light in Silhouettes by Janet O’Neill.
```

### Performance text (classify this)

```text
SARAH: In my senior English class, I once learned a passage from Alfred Lord Tennyson that started with, "Dreams are true while they last, and do we not live in dreams?" And I always asked myself: Is the same true for nightmares?

SARAH: Jeff was my third boyfriend. First two were nice enough - one moved away; one found someone with a bigger chest. Jeff was different. He brought flowers. He sent cards. He even went and watched romantic movies with me. I'll even admit the first two months were great. Jeff was the kind of person you'd want to bring home to your parents. At first. I'll never forget my mom saying, out loud, in Jeff's presence, Now, Sarah, I think you've found a keeper this time! Don't screw it up! My friends adored him: What's he like? Does he talk? He seems so quiet. Everyone thought I should stay with him. Everyone but me.

It always started with a slow rage. Boiling inside, his voice a dead calm. He'd see me talk to someone in the cafeteria and say I was a slut. He'd call me a whore. He'd always say I don't ask for much, just you. It would start with a slap. Then he'd knock me down. Corner me somewhere. He'd transform into this monster. This being that was there to punish me. He'd kick me 'til I was down. And I would always remember thinking: Please hit me in the stomach. Don't hit any bones. It hurts so much more in the bones. He'd go at a faster pace and I could apologize, but it wouldn't stop him. Please hit me in the stomach. I'll throw up. I want to throw up.

Now, as they say on the talk shows, there comes a point where the female victim hides the bruises because she's ashamed. I did that for five months. Then one day, I had a big bruise on my shoulder and showed it to my mom:

MOM: Oh, what'd you do to yourself now?

SARAH: Mom ... Jeff did this.

MOM: Honey, really. Now wash up for dinner.

SARAH: No mom, please-

MOM: Sarah, you forget that I know how clumsy you are.

SARAH: And he was beating me again. While he hit me in the head, back and forth, he kept saying I just love you so much.

One day, I was looking at myself in the mirror. Who is Sarah Murray? A victim or a survivor?

So, I ran away. Far away. Springfield, Oregon. 1,873 miles away. No postcards. No phone calls. Sarah Murray had been reborn. From time to time, I'd wake in sweats, but I could never recall the dream. I started taking classes part time and worked full-time at a pet shop and the sweats became less frequent. I was outgoing. Independent. No one could touch me. I wanted to join something. Socialize. I became active in PETA. That's right, nothing to do with abuse. The new Sarah Murray had never been abused.

I met a man at the pet shop. His name was Keith. He loved animals as much as I did and seemed to have developed a crush on me. We'd had dinner a couple times, but never a date. Keith knew I wasn't a hugger, a toucher, a close person. Strangely, he liked that about me. I had built a new life. On my own with only $900 to start with. Even had a house. Rental, but a house. Just me. That's all I needed. Then, one night, the phone rang. The phone never rings.

JEFF: Hi, Sarah, it's Jeff Honey, it's Jeff. Are you there?

SARAH: Yes

JEFF: Sarah, I've come for you. I'm in Springfield. I'm getting a job here.

SARAH: How did you find me?

JEFF: Took a while. I knew you needed to be away from your family. It's OK, we're together again.

SARAH: Jeff –

JEFF: I'll stop by tomorrow night. We'll celebrate.

SARAH: And I dropped the phone and started pacing. My hands started to shake and I kept telling myself not to shake. The new Sarah doesn't shake. It wasn't just that he had found me. It was that he would always find me.

He would find me and the old Sarah would return. Victim Sarah. Please hit me in the stomach Sarah. I kept praying to God: God, I don't want this. God, I don't want this. God, I don't want this. Let me out. Please just let me out of this nightmare.

I went to the garage. Got in the car. Made sure the door was closed and turned the ignition. In an hour, it would be over. Old Sarah would die. New Sarah would live. A final act of defiance. A way of saying Jeff, you can't get me. Fifteen minutes passed. I didn't feel anything. I was calmer, but that was because I was at peace with myself. I would win.

28 minutes. I listen to the radio. Just one more old Beatles song. Play one more. 37 minutes. This is the point I should turn back. This is the point I should come to the realization that it's not so bad. 45 minutes. The music sounds further away. Is a band playing? 51 minutes.

I open my eyes and see a woman next to me. She's a nurse. You gave us quite a scare, she says. Your boyfriend would like to see you. Jeff enters and holds my hand. New Sarah is dead. Sarah the victim is resurrected.
```

---

## IC-2326: Silver Water

- Title: Silver Water
- Author (byline): Amy Bloom
- Work: Come to Me: Stories
- Publisher: Perennial Press
- Publication date as stated: April 1994
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: MOTHER, THERAPIST, VIOLET, ROSE, FATHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1746
- Already set (do not supply): none

### Source block (context only)

```text
Author: Amy Bloom
Book: Come to Me: Stories
ISBN: 978-0060995140
Publisher: Perennial Press
Date (Month/Year): April 1994
```

### Introduction (context only: never use it for content warnings)

```text
Silver Water by Amy Bloom
```

### Performance text (classify this)

```text
(Pg 87 – 100) My sister’s voice was like mountain water in a silver pitcher. After we went to [the opera], when she was fourteen and I was twelve, she elbowed me in the parking lot and said, “Check this out” And she opened her mouth wide and her voice came out, so crystalline and bright that all the departing opera-goers stood frozen by their cars, unable to take out their keys until she had finished.

That’s what I like to remember . . . That before her constant tinkling of commercials and fast-food jingles there had been Puccini and Mozart and hymns so sweet you expected Jesus to come down off his cross and clap. That before there was a mountain of Thorazined fat, swaying down the halls in sweatpants, there had been the prettiest girl i Landmark Junior High. To me, Rose, my beautiful blond defender, was perfect.

She had her first psychotic break when she was fifteen. She had been coming home moody and tearful, then quietly beaming, then she stopped coming home. She would go out into the woods behind our house and not come in until my mother went after her and stepped into the briars and saplings and pulled her out, blank-faced, her sweater covered with crumbled leaves, her jeans smeared with dirt. After three weeks of this, my mother said to my father:

MOTHER: David, she’s going crazy. She needs a hospital.

Rose was in hospitals, great and small, for the next ten years. She had lots of terrible therapists and a few good ones.

The worst family therapist we ever had sat in a pale green room with us, read Rose’s file in front of us and then watched in alarm as Rose began crooning, beautifully, and slowly massaging her breasts. My mother and I laughed, and even my father started to smile. This was Rose’s usual opening salvo for new therapists.

THERAPIST: I wonder why it is that everyone is so entertained by Rose behaving inappropriately.

Rose burped, and we all laughed. This was the seventh family therapist we had seen, and none of them had lasted very long.

THERAPIST: What do you think of Rose’s behavior, Violet?

VIOLET: I don’t know. Maybe she’s trying to get you to stop talking about her in the third person.

ROSE: That was not a successful intervention, Ferret Face.

He did look like a blond ferret, and we all laughed again. The day we met our best family therapist started out almost as badly. We scared off a resident and then scared off her supervisor, who sent us Dr. Thorne. Dr. Thorne was good for us, Rose moved into a halfway house, took her meds, lost about fifty pounds, and began singing at the A.M.E. Zion Church, down the street from the halfway house.

At first they didn’t know what do to with this big blond lady, dressed funny and hovering wistfully in the doorway during their rehearsals, but she gave them a few bars of “Precious Lord” and the choir director felt God’s hand.

Rose and the choir’s contralto, Addie Robicheaux, laid out their gold and silver voices and wove them together in strands as fine as silk, as strong as steel. And we wept as Rose and Addie, in their billowing garnet robes, swayed together clasping hands until the last perfect note floated up to God.

Rose would still go off from time to time and the voices would tell her to do bad things, but Dr. Thorne or Addie or my mother could usually bring her back . . . [And then] after five good years, Dr. Thorne had an aneurysm and died.

Rose stopped taking her meds, and the halfway house wouldn’t keep her after she pitched a patient down the stairs. My father called the insurance company and found out that Rose’s new psychiatric coverage wouldn’t begin for forty-five days. I put all of her stuff in a garbage bag, and we walked out of the halfway house.

My father convened a family meeting:

FATHER: This is going to be difficult--not all bad, but difficult--for the whole family, and I thought we should discuss everybody’s expectations. I know I have some concerns.

ROSE: (with lowered eyes, as she frantically pulled at her clothing) No meds!

My father looked in despair at my mother.

MOTHER: Rosie, do you want to drive the new car?

ROSE: (face lighting up, she speaks manically) I’d love to drive that car, I’d drive to California, I’d go see the bears at the San Diego Zoo, would take you, Violet, but you always hated the zoo. Remember how she cried at the Bronx Zoo when she found out that the animals didn’t get to go home at closing?

MOTHER: If you take your medication, after a while you’ll be able to drive the car. That’s the deal. Meds, car.

ROSE: You got yourself a deal, darlin’.

I was living about an hour away then, teaching English. I went home every few days for dinner. I called every night:

FATHER: (On the phone, quietly) It’s very hard. We’re doing all right, I think, Rose has been walking in the mornings with your mother and she watches a lot of TV. She won’t go to the day hospital, and she won’t go back to the choir. I’m sorry, sweetheart, don’t mean to depress you.

I stayed away all week, afraid to pick up my phone. On Sunday, I came in the early afternoon, to help my father garden. We weeded and staked tomatoes while my mother and Rose were down at the Lake. I didn’t even go into the house until four, when I needed a glass of water. Someone had broken the piano bench into five neatly stacked pieces and placed them where the piano bench usually was.

FATHER: We were having such a nice time, I couldn’t bear to bring it up.

VIOLET: What did Mommy say?

FATHER: She said, ‘Better the bench than the piano.’ And your sister lay down on the floor and just wept. Then your mother took her down to the lake. This can’t go on, Vi. We have twenty-seven days left, your mother gets no sleep because Rose doesn’t sleep, and if I could just pay twenty-seven thousand dollars to keep her in the hospital until the insurance takes over, I’d do it.

VIOLET: All right. Do it. Pay the money and take her back.

FATHER: I would if I could. The policy states that she must be symptom-free for at least forty-five days before her coverage begins. Symptom-free means no hospitalization.

VIOLET: Jesus, Daddy . . . She hasn’t been symptom-free for forty-five minutes.

FATHER: It’s the only one I could get for long-term psychiatric. (near tears, he places his hand over his mouth, to block whatever he was about to say, and goes back out to the garden).

He stayed outside and I stayed inside. Rose and my mother came home from the lake. My mother kissed me lightly and told Rose to go up to her room and change out of her wet pants.

ROSE: (eyes growing very wide) Never. I will never. . .!

(Begins rocking violently)

She knelt down and began banging her head on the kitchen floor with rhythmic intensity, throwing all her weight behind each attack. My mother put her arms around Rose’s waist and tried to hold her back. Rose shook her off, not even looking around to see what was slowing her down.

MOTHER: Violet, please . . .

I threw myself onto the kitchen floor, becoming the spot that Rose was smacking her head against. She stopped a fraction of an inch short of my stomach.

ROSE: (stopping her violent rocking) Oh Vi, Mommy, I’m sorry. I’m sorry don’t hate me! (she rushes from the room wailing)

Dinner was filled with all of our starts and stops and Rose’s desperate efforts to control herself. She could barely eat and hummed the McDonald’s theme song over and over again, pausing only to spill her juice down the front of her smock and begin weeping.

ROSE: (Rocking and chanting) I want to go to bed, I want to go to bed and be in my head. I want to go to bed and be in my bed and in my head and and and and . . . .

FATHER: Okay, okay, Rose. It’s okay. I’ll go upstairs with you and you can get ready for bed. Then Mommy will come up and say good night too. It’s okay, Rose.

My father reached out his hand and Rose grasped it, and they walked out of the dining room together, his arm around her middle. [A short time later] my father came into the kitchen and signaled to my mother. They went upstairs and came back down together and we went to sit on the porch and listen to the crickets. I don’t remember the rest of the evening, but I remember it as quietly sad, and I remember the rare sight of my parents holding hands, sitting on the picnic table, watching the sunset.

I woke up at three o’clock in the morning. I went down the hall and looked into Rose’s room, for no reason. She wasn’t there. I could feel her absence. I went outside and saw her wide, draggy footprints darkening the wet grass into the woods.

VIOLET: (in a loud whisper) Rosie. Rosie, it’s me. Are you here? Are you all right?”

I almost fell over her. Huge and white in the moonlight, her flowered smock bleached in the light and shadow, her sweatpants now completely wet. Her head was flung back, her white, white neck exposed like a lost Greek column. Her breathing was very slow, and her lips were not as pink as they usually were. Her eyelids fluttered.

ROSE: (whispering) Closing time . . .

I believe that’s what she said. (Long beat) I sat with her, uncovering the bottle of Seconal by her hand, and watched the stars fade. When [they] were invisible and the sun was warming the air, I went back to the house. My mother was standing on the porch, wrapped in a blanket, watching me.

MOTHER: Warrior queens . . . I raised warrior queens.

She kissed me fiercely and went into the woods by herself. Later in the morning she woke my father, who could not go into the woods, and still later she called the police and the funeral parlor. She hung up the phone, lay down, and didn’t get back out of bed until the day of the funeral. (Long beat)

My mother played the piano and Addie sang her pure gold notes and I closed my eyes and saw my sister, fourteen years old, lion’s mane thrown back and eyes tightly closed against the glare of the parking lot lights.

(Quietly sing first stanza of “Precious Lord, Take My Hand” hymn; Lyrics and Music by Thomas A. Dorsey)

Precious Lord, take my hand
Lead me on, let me stand
I'm tired, I’m weak, I’m lone
Through the storm, through the night
Lead me on to the light
Take my hand precious Lord, lead me home.

https://www.youtube.com/watch?v=fRGTR_wUje8
```

---

## IC-2327: The Smoking Room

- Title: The Smoking Room
- Author (byline): Shirley Jackson
- Work: Just an Ordinary Day
- Publisher: Bantam Books, Inc.
- Publication date as stated: Dec 1996
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1876
- Already set (do not supply): none

### Source block (context only)

```text
Author: Shirley Jackson
Book: Just an Ordinary Day
ISBN: 978-0553103038
Publisher: Bantam Books, Inc.
Date (Month/Year): Dec 1996
```

### Introduction (context only: never use it for content warnings)

```text
What would you do if the devil, himself, appeared to you and asked for your soul? In The Smoking Room by Shirley Jackson, the reaction of this particular college student isn’t quite typical. No fear, no quaking . . . but then again college is supposed to train you react logically to any situation, right? The Smoking Room by Shirley Jackson
```

### Performance text (classify this)

```text
He was taller than I had imagined him. And noisier. Here I was, all by myself, downstairs in the dormitory smoking room with my typewriter, and all of a sudden there was this terrific crash and sort of sizzle, and I turned around and there he was.

“Can’t you be a little quieter?” I said. “I’m trying to work.”

He just stood there, with smoke rolling off his head. “This is as quietly as I can do it,” he said apologetically. “IT takes a lot of explosive power, you know.”

“Well, explode somewhere else,” I said. “Men aren’t allowed in here.”

“I know,” he said.

I turned around to get a good look at him. He was still smoking a little, but otherwise he seemed quite a charming young man. The horns were barely noticeable, and he was wearing pointed patent leather shoes that covered his cloven hoofs. He seemed to be waiting for me to make conversation.

“You must be the devil,” I said politely, and added: “I presume.”

“Yes,” he said, pleased. “I am the devil.”

“Where’s your tail?” I demanded. He blushed and made a vague gesture with his hand.

“Circumstances . . . “ he murmured. He came over to the table where I was working. “What’re you doing?” he asked.

“I’m writing a paper,” I said.

“Let’s see.” He reached over to the typewriter and I shoved his hand away, getting quite a nasty burn from it, too.

“Mind your own business,” I told him

He sat down meekly. “Look,” he said, “do you have an extra cigarette?”

I threw the pack over to him and watched him light one with the tip of his finger. My hand was all inflamed where I had touched him, and it hurt.

I held out my hand to him. “You oughtn’t to treat people like that,” I said. “It makes enemies.”

He looked at my hand sympathetically, then murmured over it, and the burn vanished. “That’s better,” I said.

We sat back and smoked for a minute, looking at each other. He was a good-looking guy.

“By the way,” I said finally, “do you mind telling me what you’re here for?”

“This is a college, isn’t it?”

I looked at him for a minute, but he didn’t seem to mean anything nasty, so I said: “You are at present in the smoking room of the largest girls’ dormitory on the campus of State University, and the housemother will raise hell if she finds you here.

He began to laugh, and I realized that my choice of words had been a little silly, to say the least.

“I’d like to meet this housemother,” he said.

I tried to imagine what that would be like, and gave up. “She’s the closest thing to you you’ll find on earth,” I said earnestly.

He raised his eyebrows, and then suddenly seemed to think of something, because he reached into a pocket and pulled out a piece of paper.

“I wonder if you’d mind signing this?” he asked casually.

I picked up the paper. “May I read it first?”

He shrugged. “It isn’t important, but go ahead.”

I read: “This gives the devil my soul” and a space was left blank for my name. “This isn’t awfully legal,” I said.

He looked anxiously over my shoulder. “Isn’t it?” he said. “What’s wrong with it?”

“Well, obviously!” I threw the paper down on the table and pointed at it scornfully. “Who’s ever going to think that holds in a court of law? No witnesses, a thousand loopholes for a smart lawyer . . . “

He picked up the paper and was frowning over it miserably. “It’s always been perfectly all right before,” he said.

“Well, I’m just surprised at your methods of doing business, that’s all. No court would even look at it.”

“Look,” he said. “We’ll make out another contract . . . one you think it all right. I don’t want to do this thing wrong, after all.”

I thought. “All right,” I said. “I’ll make one up. Mind you, I’m not awfully sure of the legal terminology, but I think I can manage.”

“Go ahead,” he said. “If it suits you, it suits me.”

I pulled the paper out of the typewriter and found a carbon and two new sheets.

He looked at the carbon suspiciously.

“What’s that?”

“I’m making two copies,” I told him. “I’ve got to keep one myself. That makes it binding.”

He continued to regard me suspiciously while I worked over the contract.

“How long is this contract good for?” I asked at once.

“Oh, eternity,” he said easily.

I finally finished and took the sheets out of the typewriter. Due to the fact that my knowledge of legal documents is restricted to the notices the dean sends out about poor grades, the contract was just a little confused. It read: I (here a space was left blank for a name), hereinafter to be known as the party of the first part, do herby sell and consign my soul, hereinafter to be known as the party of the second part, to the custody and careful watchfulness of (here another space was left blank), hereinafter to be known as the party of the third part, who does hereby swear and promise the sum of one dollar in return, also other unnamed considerations, admitting and conceding that it is a far and just bargain, and no complaints afterward; this agreement to be binding, by mutual consent of the parties concerned, in any court of law, wherever conducted, (signed) (witnessed)

The devil read it twice. “I don’t understand it,” he said.

“It says the same thing as yours did,” I told him, “except that it’s more binding.” I pointed over his shoulder. “You see all those things about the parties of the first and second parts? And about the court of law? That all makes it legal.”

“Well, sign it, then,” he said.

I thought. “We need a witness,” I said. “I’ll go upstairs and get my roommate.”

I left before he could say anything. My roommate was asleep.

“Look, Bobbie,” I said. I shook here. She turned over and said, “Go away.”

“Bobbie,” I said, “you’ve got to come and witness a contract.”

“What the hell,” Bobbie said.

“I’ve got the devil waiting downstairs”

“Let him wait,” Bobbie said. She had both eyes open but she wouldn’t move. I rolled her out of bed and stood her up. “Come on,” I said. “He’ll get impatient”

“Signing contracts with the devil,” Bobbie said in disgust. “At three in the morning How’s a person ever going to get any sleep.”

“Come on!” I said.

Bobbie sat down on the edge of her bed. “IF he’s been waiting all these thousands of years,” she said, “he can wait until I get some lipstick on.”

By the time I got her downstairs, the devil had smoked four more of my cigarettes. He got up when we entered and bowed very low to Bobbie.

“Charmed,” he said.

Bobbie smiled at him invitingly. “Hello,” she said.

“Come on, you tow,” I told them, I’ve got to get this over with and get back to work>”

“What do I have to do? Bobbie said, looking at the devil out of the corner of her eye.

“Just sign,” the devil said, taking her arm to lead her over to the table.

Bobbie let out a yell that ought to have waked the housemother and the whole dormitory. The devil backed away and began to apologize, but Bobbie stood there rubbing her arm and glaring.

“Look,” she said belligerently, “I’m not fooling around with any guy sets fire to you when he touches you.” The devil looked at Bobbie’s arm and made the burn go away, but after that Bobbie kept the table between them. I took up the contract.

“I’ll sign first,” I said. I wrote my name quickly in the second blank and handed the paper to the devil.

“You have to sign, too,” I said.

“Where?” He looked blankly at the paper. I showed him the first place and handed him my pen. He blushed, and looked from me to Bobbie. “I’m afraid . . . “ he began, “do you mind if . . . “ he shrugged and made an X in the space. “I never learned . . . “ he said apologetically. Bobbie’s jaw dropped and she just stood there until I kicked her in the ankle.

“Sign here,” I said, and she signed in the witness space.

Then the devil and I signed again at the bottom, and signed the duplicate the same way, and I handed him one sheet and kept the other.

“Now,” I said as casually as I could, “I guess I owe you a dollar”

“What for?” he said.

“Bobbie,” I said rapidly, “run upstairs and borrow a buck from someone.”

“What the hell,” Bobbie said. But she turned around and started up the stairs.

“Well,” said the devil, rubbing his hands, “what can I do for you now?”

I began to polish my nails on my hand. “Lt’s see,” I said. “I’ll start out with an A in Chemistry 186, the power to be invisible when I come in after hours, a date with the captain of the football team for the senior ball – “

“Throw in something for me,” said Bobbie, coming through the door.

“Let’s see,” I said, “give her – “

“A date with that blond guy,” said Bobbie, “you know.” She handed me a dollar.

“I guess that’s about all,“ I said to the devil.

“Except, of course,” Bobbie put in, “except for a couple of hundred thousand dollars”

“You shall have all those things,” the devil promised eagerly.

“Oh, yes,” I said. “And you get this out of it.” I handed him the dollar.

“What’s this for?” he asked.

I looked at the contract. “That’s for your soul,” I said.

The devil looked at his contract. “Your soul,” he said.

“No.” I showed him the contract. “Where you signed, it says you give me your soul for the sum of one dollar, also other unnamed considerations. Those would be the cigarettes of mine you smoked.”

“And getting me out of bed,” Bobbie added.

The devil read the contract again. Then he began to stamp his feet, and flames came out of his mouth. Bobbie and I looked at each other.

“Golly,” she said. “What a date this guy would be!”

Just then the devil seemed to get a little pale, and he backed up against the wall, staring in back of us. Bobbie and I turned around, and there was the housemother. She stood in the doorway, in a bathrobe, with curlpapers on her hair, and she was an awe-inspiring sight.

She looked at the devil. “Young man,” she said, “what are you doing here?

“Ma’am . . . “ the devil began.

“You’re a fire hazard,” she snapped.

“Yes’m,” the devil said.

“Leave at once,” she said ominously, ‘before I report you to the dean of women,”

The devil ast one dreaful look at Bobbie and me, and then tried to vanish in a puff of smoke. All he succeeded in, however, was a weak sizzle, and then he was gone.

“All right,” said the housemother. Then she turned to Bobbie and me.

“Well?” she said.

“Look,” Bobbie began.

“You see, it was like this – “ I said.

“Humph,” said the housemother. “Devils, indeed!” and she went back to bed.
```

---

## IC-2328: A Snicker of Magic

- Title: A Snicker of Magic
- Author (byline): Natalie Lloyd
- Work: Not specified
- Publisher: Scholastic, Inc.
- Publication date as stated: April 2015
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: JONAH, FELICITY
- Teaser before the introduction: Yes
- Spoken words (computed): 1487
- Already set (do not supply): none

### Source block (context only)

```text
Author: Natalie Lloyd
ISBN: 978-0545552738
Publisher: Scholastic, Inc.
Date (Month/Year): April 2015
Cutting compliments of
Heather Whitney, Norfolk Public Schools, NE
*With minor adjustments by the 4N6 Fanatics staff to
ensure correlation with the original text.
```

### Introduction (context only: never use it for content warnings)

```text
Midnight Gulch used to be a magical place, a town where people could sing up thunderstorms and dance up sunflowers. But that was long ago, before a curse of the Brothers Threadbare drove the magic away. Twelve-year-old Felicity knows all about things like that; her nomadic mother is cursed with a wandering heart. But when she arrives in Midnight Gulch, her luck may be about to change. A “word collector”, Felicity sees words everywhere -- shining above strangers, tucked into church eves, and tangled up in dog’s ears - and Midnight Gulch is the first place she’s ever seen the word “home”. Will any words convince Mama not to move again? Felicity wants to stay here forever, but first she will need to bring back the magic, breaking the spell that’s been cast over the town in the novel A Snicker of Magic by Natalie Lloyd.
```

### Performance text (classify this)

```text
(Pg 137-138) The 5 Most Interesting Facts about Myself • I am Felicity Pickle. My first name stands for “wondrous joy.” My [last] name is Pickle and it stands for all my people behind me and ahead of me. • I live in a town that used to be full of magic. I think there’s still magic here. It’s just been playing hide-and-seek for a very long time. I want to stay forever. (Pg 5) [It’s] a proper place to call home. • My best friend’s name is Jonah Pickett. (Pg 145) Best Friend, not just a friend, a best friend. • Because of Jonah Pickett, I signed up for the Duel. Even though I would still rather floss with barbed wire than participate. • [The morning I signed up for the Duel], (Pg 8) I saw my first word of the day: Believe. Something wonderful was about to happen to me. I didn’t know what, or why, or how. But I believed.

(Pg 7) Mama liked to say that us Pickles were nomads. Sweet gypsies. Adventure seekers. (Pg 67) She’s always looking for a reason to leave. No matter where we go. (Pg 30) It’d take a miracle to make a bunch of gypsy Pickles finally settle down. A big miracle . . . or a little bit of magic.

JONAH: (Pg 67) “Maybe that’s why you have to do the Duel. Maybe if your mama sees you competing in the talent show . . . If she sees how happy you are in Midnight Gulch, then she’ll want to stay for a while. (Pg 37) Felicity Pickle, I’m going to help you win the talent show . . . Miss Lawson’s Duel.

FELICITY: I appreciate it, but I have no talent. Except well . . . (Pg 13) I see words everywhere, all around me, all the time. (Pg 37-39) I collect them. Words come in all sorts of shapes: stars, spaceships, pretzel words. Some words glow and some words dance. I know how to catch words and keep them. (Pg 9) I’m not sure how it works. I can’t be the only word collector in the whole world, but I’ve never met anybody else who has the knack.

JONAH: (Pg 134) I think your word collecting is a snicker of magic . . .

FELICITY: Word collecting’s not magic. It’s just a quirk . . .

JONAH: The Brothers Threadbare, (Pg 18) the most famous duo ever to call Midnight Gulch their home, (Pg 134) probably thought that way. Until they saw what their music did to people., how it made them dance. Made them happy.

(Pg 135) The only magic I was interested in was the kind that would make Mama stay put. I’d give anything to find a snicker of magic like that. TRANSITION Jonah took Felicity around all parts of town, helping her collect stories and words from the townsfolk – Gathering information for the talent show, best known as The Duel. But it was Miss Lawson, their teacher who told them the story of The Brothers Threadbare and the magical place that was once Midnight Gulch.

(Pg 19-22) “Like most people, the Brothers Threadbare were simple, easygoing folk . . . who just so happened to have a little magic in their veins. Their names were Stone and Berry Weatherly, farm boys. The Weatherly magic was a particularly wonderful kind, because their magic had to do with music. Whenever Stone played his guitar or at the first strum of Berry’s banjo, the whole world seemed to dance. They always started their concerts with a few magic tricks. But soon, the brothers realized people were more interested in their magic tricks than in their singing. So they focused on the magic. But sadly, their fame and fortune became a dividing line between them. The brothers became so jealous of one another that they finally decided to have a duel. Whoever won, they decided, could keep all the money and fame and fortune they’d earned. But the loser would be cursed forever with a wandering heart. They dueled for three whole days – Finally Berry cast the winning spell. And poor Stone Weatherly. He let town. Soon after he left, Berry discovered that, without his brother, his magic didn’t work anyhow. Eventually he disappeared from town, too. Midnight Gulch used to be their favorite secret, their favorite place, but [it] didn’t feel like home anymore. People started leaving, breaking apart from their families and heading out in search of what they’d lost. (Pg 89) [Oliver, the owner of Dr. Zook’s Ice Cream Shop, told us]: ”Most people in this town only know the story of the Duel. They don’t know about the day Stone Weatherly came back to Midnight Gulch, [looking for his brother.] (Pg 91) [He] didn’t stay here long. He was cursed with a wandering heart and had to keep moving along. He was such a lonely man. (Pg 95) They both spent the rest of their time trying to find each other, trying to break the curse. “Cursed to wander through the night, till cords align, and all’s made right. Where sweet amends are made and spoken, shadows dance, the curse is broken.” (Pg 158-159) [It was finally in talking to Aunt Cleo that we found out that] Stone Weatherly was [actually] my “no-good-lowdown-deadbeat-drifter great-great-grandfather”. And that means it [isn’t] magic we had in our veins. All we’ve got is the curse. Stone Weatherly lost the duel. And because he lost, he had to leave town and live out that curse for the rest of his days. He couldn’t set roots in any place. He was cursed with a restless soul. Like Mama. (Pg 127) Mama was always thinking of going, and never staying put. (Pg 253) I was sick of always beginning. I just wanted to be. Stop settling in here, I told my heart.

Pickles always leave. Soon enough, there’d be a new town. A new first day of school. (Pg 221) You don’t have to leave to find a new beginning, Mama. You can begin again exactly where you are. But me telling her wouldn’t matter. Mama had to see that we were home for herself. (Pg 274) [The day of the Duel] I Watched my whole family lodge themselves in the middle row, where they could see me and cheer for me when I took the stage. [And I realized] I could do anything if they were with me. My fears were monster big. But their love for me was bigger. (Pg 280) And suddenly I knew [what the curse of the Theadbare Brothers meant] There is no magic in the world more powerful than love. If you’re brave enough to love, and forgive . . . there’s no curse in the world that has any power over you. (Pg 281-282) [And so I shared these words at the Duel:] “Once upon a time, here in this place where I’m talking, two magicians made a mess of things. People say that when they left town, they took all the magic with them. There’s still a snicker of magic left, but there’s more sorrow, now, than joy. People leave here, and never come back. They don’t want to stay here. They don’t want to end up here, because this doesn’t feel like home anymore. In the end, I don’t think [the Brothers Threadbare] even cared about the magic. Instead of being so hateful, instead of dooming each other to wander off along . . . they should have said the words that mattered most of all. Their words were more powerful than any magic trick they ever did. I think the Brothers Threadbare had forgotten all about who they really were. They were family. I think if they had to do it over, I think they would have said “Sorry for what I did to you.” And they would have said “I love you.” Maybe if you say those words, maybe if you believe them, no curse in the world has any power over you. I’ve collected whole constellations of words. But these words are my favorite: Mama, [Aunt] Cleo, [Uncle] Boone, [sister] Frannie, [Jonah], [my dog] Biscuit. I wouldn’t know anything about love if it weren’t for them.

No matter what happens, or what I do, or how far apart we are, I know they love me. And if you say, “I love you,” and you mean it, then love makes up for a whole lifetime of mistakes. That’s some kind of magic.” (Pg 283) “Chords align, and all’s made right.” (Pg 298) [And just like that, after that day, we stayed in Midnight Gulch.[ The curse [that kept Mama a wanderer[ was broken. (Pg 306-307) It’s so weird how life is full of moving around - people coming and going, people passing by each other all day long. You never know which person’s going to steal your heart. You never know which place is going to settle your soul. All you can do is look. And hope. And believe. (Pg 309) I’m convinced Midnight Gulch can’t be the only magical town in the world. I bet there’s a snicker of magic on every street, in every old building, every broken heart, every word of a story. Maybe it’s hidden away and you need to look harder for it. Or maybe the magic is right there, right in front of you, and all you have to do is . . . believe.
```

---

## IC-2329: Snow Glass Apples

- Title: Snow Glass Apples
- Author (byline): Neil Gaiman
- Work: Red Riding Hood and the Wolf in Bed
- Publisher: University of Toronto Press
- Publication date as stated: Nov 2006
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2510
- Already set (do not supply): none

### Source block (context only)

```text
Author: Neil Gaiman
Book: Red Riding Hood and the Wolf in Bed
ISBN: 978-0802090867
Publisher: University of Toronto Press
Date (Month/Year): Nov 2006
```

### Introduction (context only: never use it for content warnings)

```text
Once upon a time there lived a young princess with skin as white as snow, with hair as black as coal, with lips redder than blood. Most people think they know what happens to this young unfortunate girl. Most people are wrong. Snow Glass Apples by Neil Gaiman
```

### Performance text (classify this)

```text
I do not know what manner of thing she is. None of us do. She killed her mother in the birthing, but that's never enough to account for it.

They call me wise, but I am far from wise, for all that I foresaw fragments of it, frozen moments caught in pools of water or in the cold glass of my mirror. If I were wise I would not have tried to change what I saw. If I were wise I would have killed myself before ever I encountered her.

Wise, and a witch, or so they said. I'd seen his face in my dreams and in reflections for all my life: sixteen years of dreaming of him before he reined his horse by the bridge that morning, and asked my name. His beard was red-bronze in the morning light, and I knew him, not as a king, for I knew nothing of kings then, but as my love. His daughter was only a child: no more than five years of age when I came to the palace. One night, several months after I was brought to the palace, she came to my rooms. She was six.

"Princess?"

She said nothing. Her eyes were black as coal, black as her hair; her lips were redder than blood. She looked up at me and smiled. Her teeth seemed sharp, even then, in the lamplight.

"I'm hungry," she said, like any child.

It was winter, when fresh food is a dream of warmth and sunlight; but I had strings of whole apples, cored and dried, hanging from the beams of my chamber, and I pulled an apple down for her.

She took the dried apple from me and began to chew it with her sharp yellow teeth.

I had always been scared of the little princess, but at that moment I warmed to her and, with my fingers, gently, I stroked her cheek. She looked at me and smiled -- she smiled but rarely -- then she sank her teeth into the base of my thumb and she drew blood. I began to shriek, from pain and from surprise; but she looked at me and I fell silent.

The little Princess fastened her mouth to my hand and drank. When she was finished, she left my chamber. Beneath my gaze the cut that she had made began to close, to scab, and to heal. The next day it was an old scar: I might have cut my hand with a pocket-knife in my childhood.

I had been frozen by her, owned and dominated. That scared me, more than the blood she had fed on. After that night I locked my chamber door at dusk, barring it with an oaken pole, and I had the smith forge iron bars, which he placed across my windows.

My husband, my love, my king, sent for me less and less, and when I came to him he was dizzy, listless, confused. I ran my fingers across his skin as he slept. It was covered in a multitude of ancient scars.

Soon he was a shadow of the man I had met and loved by the bridge. I was with him at the last: his hands were cold as stone, his eyes milky-blue, his hair and beard faded and lustreless and limp. He died, his skin nipped and pocked from head to toe with tiny, old scars.

So I was queen.

If it were today, I would have her heart cut out, true. But then I would have her head and arms and legs cut off. I would have them disembowel her. And then I would watch, in the town square, as the hangman heated the fire to white-heat with bellows, watch unblinking as he consigned each part of her to the fire. And I would not close my eyes until the princess was ash, and a gentle wind could scatter her like snow.

I did not do this thing, and we pay for our mistakes.

They took her in the day, while she slept, and was at her weakest. They took her to the heart of the forest, and there they opened her blouse, and they cut out her heart, and they left her dead, in a gully, for the forest to swallow.

They brought me her heart. I know it was hers -- no sow's heart or doe's would have continued to beat and pulse after it had been cut out, as that one did.

Outside, the snow fell, covering the footprints of my huntsmen, covering her tiny body in the forest where it lay.

There were people in the forest. They would come out, some of them, for the Spring Fair: a greedy, feral, dangerous people; some were stunted -- dwarfs and midgets and hunchbacks; others had the huge teeth and vacant gazes of idiots. They would creep out of the forest each year for the Spring Fair, held when the snows had melted.

Spring Fair followed Spring Fair: five of them, each sadder, poorer, shoddier than the one before. Fewer of the forest folk came out of the forest to buy. Those who did seemed subdued and listless.

The Lord of the Fair, and his page, came to me when the fair was done. I had known him slightly, before I was queen.

"I do not come to you as my queen," he said. "I come to you because you are wise. You know secrets and you can seek out things hidden. My queen," he asked, "what is taking the forest folk? Next year there will be no Spring Fair. The travellers from other kingdoms have grown scarce and few, the folk of the forest are almost gone. Another year like the last, and we shall all starve."

I commanded my maidservant to bring me my looking-glass. It was a simple thing, a silver-backed glass disk, which I kept wrapped in a doe-skin, in a chest, in my chamber.

They brought it to me, then, and I gazed into it:

She was twelve and she was no longer a little child. Her skin was still pale, her eyes and hair coal-black, her lips as red as blood. She was standing in the forest, beside a tree.

As I watched, in the eye of my mind, I saw her edge and step and flitter and pad from tree to tree, like an animal: a bat or a wolf. She was following someone.

He was a monk.She watched him from behind the trees. Eventually he paused for the night, and began to make a fire. He sat there in the firelight, and she came out from her hiding place. She crouched down on the other side of the fire, and stared at him. He grinned, as if it were a long time since he had seen another human, and beckoned her over to him. She sank her teeth deep into his breast. His eyes opened, then they closed again, and she drank.

I covered the mirror in doe-skin. I would personally take it upon myself to make the forest safe once more. I had to, although she terrified me. I was the queen.

I spent time with old books, for I could read a little. I prepared myself, and obtained those things I would need, and when the first snows began to fall, then I was ready. I carried a silver basin, and a basket in which I had placed a silver knife, a silver pin, some tongs, a grey robe and three green apples. I took the silver knife, and slashed my left arm -- once, twice, three times. The blood dripped into the basin, scarlet seeming black in the moonlight.

I added the powder from the vial that hung around my neck. It was a brown dust, made of dried herbs and the skin of a particular toad, and from certain other things. It thickened the blood, while preventing it from clotting. I took the three apples, one by one, and pricked their skins gently with my silver pin.

When dawn began to brighten the sky I covered myself with the grey cloak, and took the red apples. I buried the bowl in the earth. Then I cast a glamour on the apples that they were, beyond any doubt, the most wonderful apples in the world; and the crimson blush of their skins was the warm colour of fresh blood.

I pulled the hood of my cloak low over my face, and I took ribbons and pretty hair ornaments with me, placed them above the apples in the reed basket, and I walked alone into the forest, until I came to her dwelling: a high, sandstone cliff, laced with deep caves going back a way into the rock wall.

After some hours a clutch of dwarfs crawled out of the cave-front -- ugly, misshapen, hairy little men, the old inhabitants of this country.They vanished into the wood. I went to the cave entrance and hallooed into it, in a cracked old voice.

She was thirteen years of age, my stepdaughter, and nothing marred the perfect whiteness of her skin save for the livid scar on her left breast, where her heart had been cut from her long since.

She peered at me, hidden, as I was, in my cloak. She looked at me hungrily. "Ribbons, goodwife," I croaked. "Pretty ribbons for your hair..."

She smiled and beckoned to me. I did what I had planned to do: I dropped my basket, and screeched like the bloodless old pedlar woman I was pretending to be, and I ran. I made my way back to the palace.

I did not see it. Let us imagine though, the girl returning, frustrated and hungry, to her cave, and finding my fallen basket on the ground. What did she do?

I like to think she played first with the ribbons, twined them into her raven hair, looped them around her pale neck or her tiny waist. And then, curious, she moved the cloth to see what else was in the basket; and she saw the red, red apples.

They smelled like fresh apples, of course; and they also smelled of blood. And she was hungry. I imagine her picking up an apple, pressing it against her cheek, feeling the cold smoothness of it against her skin. And she opened her mouth and bit deep into it...

By the time I reached my chambers, the heart that hung from the roof-beam, with the apples and hams and the dried sausages, had ceased to beat. It hung there, quietly, without motion or life, and I felt safe once more.

The Spring Fair was slightly improved that year. The forest folk were few, but they were there, and there were travellers from the lands beyond the forest.

I saw the little hairy men of the forest-cave buying and bargaining for pieces of glass. I thought, briefly, about having them killed, but I did not. As long as the heart hung, silent and immobile and cold, from the beam of my chamber, I was safe, and so were the folk of the forest, and, thus, eventually, the folk of the town.

My twenty-fifth year came, and my stepdaughter had eaten the poisoned fruit two winters' back, when the Prince came to my Palace. He rode with a small retinue: large enough to defend him, small enough that another monarch -- myself, for instance -- would not view him as a potential threat.

He left early the next morning, with all his men, and they rode off into the forest.

I imagine his pale lips pressed so tightly together. Then I imagine his little troupe riding through the forest, finally coming upon the glass-and-crystal cairn of my stepdaughter. So pale. So cold. Little more than a girl, and dead.

In my fancy, I can almost feel the prayers he muttered beneath his breath in thanks for his good fortune. I imagine him negotiating with the little hairy men - offering them gold and spices for the lovely corpse under the crystal mound.

Did they take his gold willingly? Or did they look up to see his men on their horses, with their sharp swords and their spears, and realize they had no alternative?

I can only imagine... Hands, pulling off the lumps of glass and quartz from her cold body. Hands, gently caressing her cold cheek, moving her cold arm, rejoicing to find the corpse still fresh and pliable.

Did he shake the apple from her throat? Or did her eyes slowly open; did her mouth open, those red lips part, those sharp yellow teeth close on his swarthy neck, as the blood, which is the life, trickled down her throat, washing down and away the lump of apple, my own, my poison?

I imagine; I do not know. This I do know: I was woken in the night by her heart pulsing and beating once more. Salt blood dripped onto my face from above.

There was a hammering on the door. I felt afraid, but I am a queen, and I would not show fear. I opened the door.

First his men walked in to my chamber, and stood around me, with their sharp swords, and their long spears. Then he came in; and he spat in my face. Finally, she walked into my chamber, as she had when I was first a queen, and she was a child of six. She had not changed. Not really.

Her prince put his arm around her nonetheless, and they stood, side by side. They told me they would marry, and the kingdoms would be joined. They have told the people bad things about me; a little truth to add savour to the dish, but mixed with many lies.

I was bound and kept in a tiny stone cell beneath the palace, and I remained there through the autumn. Today they fetched me out of the cell; they stripped the rags from me, and washed the filth from me.

The snow was falling as they carried me through the midwinter crowds; and brought me to this kiln.

My stepdaughter stood there with her prince. She watched me but she said nothing.

As they thrust me inside, jeering and laughing as they did so, I saw one snowflake land upon her white cheek, and remain there without melting. She was not laughing, or jeering, or talking. She did not sneer at me or turn away. She looked at me, though; and for a moment I saw myself reflected in her eyes.

I will not scream. I will not give them that satisfaction. They will have my body, but my soul and my story are my own, and will die with me. I shall make no sound at all. I shall think instead of the snowflake on her cheek. I shall think of her hair as black as coal, her lips as red as blood, her skin, snow-white.
```

---

## IC-2330: Sold

- Title: Sold
- Author (byline): Patricia McCormick
- Work: Not specified
- Publisher: Hyperion
- Publication date as stated: Sept 2006
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: LAKSHMI, AMA, FATHER, BAJAI, AUNTIE, UNCLE, MUMTAZ, OLD MAN, SHAHANNA, PUSHPA, ANITA
- Teaser before the introduction: Yes
- Spoken words (computed): 1676
- Already set (do not supply): none

### Source block (context only)

```text
Author: Patricia McCormick
ISBN: 978-0786851713
Publisher: Hyperion
Date (Month/Year): Sept 2006
```

### Introduction (context only: never use it for content warnings)

```text
Statistically Nepal is one of the poorest countries in the world. Desperate to survive, families feel forced to extreme measures to survive. Each year, nearly 12,000 Nepali girls are sold by their families into a life of sexual slavery in the brothels of India.

Meet Lakshmi. She is 13 years old and this is her story. Sold by Patricia McCormick
```

### Performance text (classify this)

```text
CAUTION - This is a Novel in Verse. Check tournament event requirements before entering this selection in PROSE.

*LAKSHMI: (Pg 8) My stepfather's arm is a withered and useless thing. Broken as a child when there was no money for a doctor, his poor mangled limb pains him during the rainy months and gives him great shame. No one, he says, will hire a one-armed man. *Ama says we are lucky we have a man at all. She says I am to honor and praise him, respect and thank him for taking us in after my father died.

LAKSHMI: (Pg 48-49) I put the baby in a basket on my back and go about my chores. [Ama’s] steps are slow and heavy, and she stops often in her work to shake her head and sigh. At noon, I warm the remains of yesterday's soup, feed it to the baby, then tighten my waistcloth so my own hungry stomach will think it is full. Then I go in search of Ama and find her weeping. (to mother) "What is it, Ama?" Ama wipes her cheek with the hem of her shawl.

AMA: Your stepfather has said you must go to the city and earn your keep as a maid.

LAKSHMI: (to mother) “This is good news, Ama," . . . (to audience) my voice full of a boldness I did not know I had. (to mother) “There will be one less mouth to feed here, and I will send my wages home." (Pg 52-55) (to audience) The next morning my stepfather brings me to Bajai Sita's store.

FATHER: (to Bajai) Lakshmi wants to go to work in the city.

BAJAI: (to Lakshmi) Are you willing to do whatever is asked of you?

LAKSHMI: I nod. She goes behind a curtain and returns with the stranger in the yellow dress. The woman looks me over head to toe, then addresses my stepfather.

AUNTIE: How much do you want for her?

LAKSHMI: My stepfather squints. He takes in the costly fabric of the woman's dress, the baubles on her ears, the silver bangles on her wrist. "One thousand rupees," he says. There are not that many rupees in the world!

AUNTIE: (circling and inspecting Lakshmi) She has no hips. And she's plain as porridge. I'll give you five hundred.

LAKSHMI: I do not understand. I can carry a load of firewood so heavy it would put a man to shame, and my legs are sturdy enough to climb the mountain a dozen times in one day. What does it matter that I have no hips yet? My stepfather says he knows the going rate for a young girl like me.

FATHER: (to Bajai) No less than eight hundred.

LAKSHMI: My stepfather counts the money, then counts it again.

BAJAI: (to Lakshmi) Your family will get nothing, not one rupee, if you do not obey your new auntie. Do you understand?

LAKSHMI: (to audience) I don't. I don't understand at all. A great deal of money has just been paid for work I have not yet done. But I nod. (Pg 72-73) Auntie takes me into one of the rooms.

AUNTIE: (disdainfully) Take off those filthy hill clothes.

LAKSHMI: She holds out a pink dress of cloud fabric and a pair of shoes. I cannot imagine how I will walk freely in such a long, flowing gown, or how I will be able to haul the firewood and scrub the floors in such a fine and flimsy dress. TRANSITION And so Auntie takes Lakshmi to a larger village where once again she is Sold.

LAKSHMI: (Pg 74-75) Auntie is speaking to a man in a tongue I do not understand. It seems as though they are talking about me now. The man points to me and asks Auntie a question. The answer, as best I can tell, is the number 12. "How old are you?" he says in my language. I tell him I am thirteen. He wheels around and slaps Auntie across the face, and she turns from a woman of queenly bearing to a frightened child. I fall to my knees and beg the man to forgive me.

Auntie names a price as high as a mountain. The man spits. Auntie goes high. The man goes low. I do not know what they have agreed to. But I do know this: he gives her nearly enough money to buy a water buffalo. TRANSITION Alone with yet another stranger, Lakshimi still believes she is being taken to her new job as a maid in the large Indian city of Kolkata.

LAKSHMI: (Pg 90-91) Finally, we tum down an alley and arrive in front of a metal gate held fast with a heavy chain. Uncle takes a key from his vest, opens the lock, and hurries me inside. This place is dark as a cave, and it smells of liquor and incense. As my eyes adjust, I see a dozen sleeping girls, some in the comers, some on rope cots. (to Uncle) “What kind of place is this?"

UNCLE: Happiness House. Auntie Mumtaz will explain it all to you.

LAKSHMI: In the weak morning light, I see that the girls are wearing dresses of every color. They have heavy silver bangles on their wrists and ankles, and earrings of gold and jewels. Their eyes are painted with black crayon, and their lips are drawn on like red chilis. (Pg 92-94) Inside a darkened chamber, a fat woman in a purple sari lounges on a cot. She has folds of flesh like roti dough at her waist, and a face as plump as an overripe mango.

She surveys me head to toe, then spits.

MUMTAZ: How much?

UNCLE: Fifteen thousand.

LAKSHMI: Uncle goes high, the woman goes low. Eventually Uncle shrugs and gives up. The woman takes a record book out from inside the folds of her dress. She writes down the number 10,000. (long beat) I don't know why I am in this strange house. It seems as though this Auntie Mumtaz is my new mistress. She is a strict one, to be sure, but I will prove myself to her. And then my mother will have a new dress, shoes for the cold season, even a new shawl made of the finest yarn. My little brother will have fruit and curds twice a day and a jacket of yak fur. (Pg 102-104) Mumtaz studies me.

MUMTAZ: Are you ready to go to work?

LAKSHMI: I nod and say yes, then nod again, although I do not understand how these city people do their chores in such fine clothes. I follow Mumtaz down a hallway lined with tiny rooms. We pass by girls sitting cross-legged on the floor. Girls drawing on tiger eyes. Girls spraying themselves with flower water. We go up some stairs, down another hallway, then into a room where an old man is lying on a bed. His skin is yellow and he has tufts of hair poking out from his ears. Mumtaz speaks kindly to him and I wonder if he is sick. Mumtaz points to me and says something to the old man. He licks his palm and smoothes down his hair. Something is not right here. I don't know what is going on, but it is not right, not right at all. Mumtaz pats the edge of the bed.

MUMTAZ: Don't be afraid. Come here, now.

LAKSHMI: I don't move. Her voice turns hard.

MUMTAZ: Get over here, you ignorant girl.

LAKSHMI: Then Mumtaz flies at me. She grabs me by the hair and drags me across the room. She flings me onto the bed next to the old man. And then he is on top of me, holding me down with the strength of ten men. He kisses me with lips that are slack and wet and taste of onions. His teeth dig into my lower lip. Underneath the weight of him, I cannot see or move or breathe. He fumbles with his pants, forces my legs apart, and I can feel him . . . I gasp for air and kick and squirm. He thrusts his tongue in my mouth. And I bite down with all my might.

OLD MAN: Aghh!

LAKSHMI: . . . and I am running. Running down the hall, past the other girls, losing my fancy city shoes along the way. TRANSITION

But this is only the beginning; starved, beaten and drugged, Lakshmi is eventually broken and moved from a locked room into the general population of girls. She learns from them everything she needs to know to survive.

LAKSHMI: (Pg 141-143) While Anita and Pushpa stand in front of the mirror, painting their faces, Shahanna explains everything to me.

SHAHANNA: Before, when you were in the locked room, Mumtaz sent the customers to you. Now, you must do what it takes to make them choose you. Tell the customers that you are 12 or Mumtaz will beat you senseless. Do whatever the customer asks of you. Otherwise, he will beat you senseless. Then he will do whatever he likes and leave without paying.

PUSHPA: Always wash yourself with a wet rag after the man is finished. This will keep you from getting a disease. Once a month a government woman comes to the back door with a basket of condoms. Take a handful and hide them under your mattress. If an old man is at the door, bat your eyelashes and act the part of a little girl. He will pay extra for this. Press your shawl to your nose with the back of your hand when you must bring a dirty man to your bed. He will leave nothing but his smell, the stink of sweat, and hair oil and liquor and man. But you can use your shawl to block the worst of it.

LAKSHMI: Anita turns away from the mirror, transformed from a crooked-faced country girl into a tiger-eyed city woman.

ANITA: There is another way to use a shawl.

LAKSHMI: I cannot tell from her always-frowning face if she is being kind or cruel.

ANITA: [The] new girl, the one in your old room . . . Yesterday morning Mumtaz found her hanging from the rafters. (long beat)

LAKSHMI: (Pg 192) A few days later I pass by a mirror. The face that looks back is that of a corpse. Her eyes are empty. She is old and tired. Old and angry. Old and sad. Old, old, a hundred years old. I speak to her. "My name is Lakshmi," I tell her. "I am from Nepal. I am 13 years old."
```

---

## IC-2331: Speak

- Title: Speak
- Author (byline): Laurie Halse Anderson
- Work: Not specified
- Publisher: Puffin
- Publication date as stated: 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: MELINDA
- Teaser before the introduction: Yes
- Spoken words (computed): 1191
- Already set (do not supply): none

### Source block (context only)

```text
Author: Laurie Halse Anderson
ISBN: 978-0374371524
Publisher: Puffin
Date (Month/Year): 2001
```

### Introduction (context only: never use it for content warnings)

```text
At the end of the summer before she enters high school, Melinda attends a party at which two bad things happen to her. She gets drunk, and she is raped. Shocked and scared, she calls the police, who break up the party and sends everyone home. She tells no one of her rape, and the other students, even her best friends, turn against her for ruining their good time. By the time school starts, she is completely alone, and utterly desolate. She withdraws more and more into herself, rarely talking, cutting classes, ignoring assignments, and becoming more estranged daily from the world around her. Few people penetrate her shell; one of them is Mr. Freeman, her art teacher, who works with her to help her express what she has so deeply repressed. When the unthinkable happens-- the same upperclassman who raped her at the party attacks her again--something within the new Melinda says no, and in repelling her attacker, she becomes whole again.

Speak by Laurie Halse Anderson
```

### Performance text (classify this)

```text
MELINDA: I am Outcast. I don’t do parties. No thanks. I trot out excuses: homework, strict parents, tuba practice, late-night dentist appointment, have to feed the warthogs. I don’t have a good track record with parties. I am not going to think about it. It was ugly, but it’s over, and I’m not going to think about it.

MELINDA: There is no point looking for my ex-friends. Our clan, the Plain Janes, has splintered and the pieces are being absorbed by rival factions.

Her eyes meet mine for a second. It’s Rachel. “I hate you,” she mouths silently. She turns her back to me and laughs with her friends. I bite my lip. My lip bleeds a little. It tastes like metal. I need to sit down.

The Homecoming pep rally, and Heather drags me into the freshman section of the bleachers. The girl behind me taps me on the shoulder with her long black nails. She had heard Heather introduce me. “Sordino?” She asks. “You’re Melinda Sordino?”

I turn around. She blows a black bubble and sucks it back into her mouth. I nod. Heather waves to a sophomore she knows across the gym. The girl pokes me harder. “Aren’t you the one who called the cops at Kyle Rodger’s party at the end of the summer?”

A block of ice freezes our section of the bleachers. Heads snap in my direction with the sound of a hundred paparazzi cameras. Another girl chimes in. “My brother got arrested at that party. He got fired because of the arrest. I can’t believe you did that. Asshole.”

I have worked so hard to forget every second of that stupid party, and here I am in the middle of a hostile crowd that hates me for what I had to do. I can’t tell what really happened. I can’t even look at that part myself.

IT is my nightmare and I can’t wake up. I’m hanging a poster outside the metal-shop room when IT creeps up. Little flecks of metal slice through my veins. IT whispers to me.

I can smell him over the noise of the metal shop and I drop my poster and the masking tape and I want to throw up and I can smell him and I run and he remembers and he knows. He whispers in my ear.

“Freshmeat.” That’s what IT whispers.

IT found me again. I thought I could ignore IT. There are four hundred other freshmen in here, two hundred female. Plus all the other grades. But he whispers to me. Andy Evans. He’s a creep. He’s a bastard. Stay away!!!!! He should be locked up. He thinks he’s all that. Call the cops

Rachel got us to the end-of-summer party, a cheerleader party, with beer and seniors and music. She blackmailed her brother, Jimmy to drive us. We were all sleeping over at Rachel’s house. Her mother thought Jimmy was taking us roller-skating.

Most people hung at the edge of the lights. They looked like models. I felt like such a little kid. Rachel found a way to fit in. I tasted a beer. It was worse than cough medicine. I gulped it down. Another beer and one more, then I worried I would throw up. I walked out of the crowd, toward the woods.

A step behind me. A senior. And then he was talking to me, flirting with me. This gorgeous cover-model guy. His hair was way better than mine, his every inch a tanned muscle, and he had straight white teeth.

Flirting with me! Where was Rachel - - she had to see this! He took my hand and pulled me close to him. I breathed in cologne and beer and something I couldn’t identify. I fit in against his body perfectly, my head level with his shoulder.

He wrapped one arm around my back. His other hand slid down to my butt. I thought that was a little rude, but my tongue was thick with beer and I couldn’t figure out how to tell him to slow down. This is what high school was supposed to feel like. Where was Rachel? She had to see this!

He tilted my face up to his. He kissed me, man kiss, hard sweet and deep. Nearly knocked me off my feet, that kiss. And I thought for a minute there that I had a boyfriend, I would start high school with a boyfriend, older and stronger and ready to watch out for me. He kissed me again. His teeth ground hard against my lips. It was hard to breathe.

“Do you want to?” He asked

What did he say? I didn’t answer. I didn’t know. I didn’t speak.

We were on the ground. When did that happen? “No”. No I did not like this. I was on the ground and he was on top of me. My lips mumble something about leaving, about a friend who needs me. I can hear myself - - I’m mumbling like a deranged drunk. He is so heavy. There is a boulder on me.

I open my mouth to breathe, to scream, and his hand covers it. In my head, my voice is as clear as a bell: “NO I DON”T WANT TO!” But I can’t spit it out.

I’m trying to remember how we got on the ground and where the moon went and wham! Shirt up, shorts down, and the ground smells wet and dark and NO! - I’m not really here, I’m definitely back at Rachel’s, crimping my hair and gluing on fake nails, and he smells like beer and mean and he hurts me hurts me hurts me and gets up....and zips his jeans....and smiles.

The next thing I saw was the telephone. I stood in the middle of a drunken crowd and I called 911 because I needed help. All those visits from Officer Friendly in second grade paid off. A lady answered the phone, “Police, state your emergency,” and I saw my face in the window over the kitchen sink and no words came out of my mouth. Who was that girl? I had never seen her before. Tears oozed down my face, over my bruised lips, pooling on the handset. “It’s OK,” said the nice lady on the phone. “We have your location. Officers are on the way. Are you hurt? Are you being threatened?” Someone grabbed the phone from my hands and listened. A scream - - the cops were coming! Blue and cherry lights flashing in the kitchen-sink window. Rachel’s face - - so angry - - in mine. Someone slapped me. I crawled out of the room through a forest of legs. Outside, the moon smiled goodbye and slipped away.

I walked home to an empty house. Without a word.

IT happened. There is no avoiding it, no forgetting. No running away, or flying, or burying, or hiding. Andy Evans raped me in August when I was drunk and too young to know what was happening. It wasn’t my fault. He hurt me. It wasn’t my fault. And I’m not going to let it kill me. I can grow.
```

---

## IC-2332: Sports Psychology

- Title: Sports Psychology
- Author (byline): Janet O’Neill
- Work: Turning Points
- Publisher: Tichenor Publishing
- Publication date as stated: 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1556
- Already set (do not supply): none

### Source block (context only)

```text
Author: Janet O’Neill
Book: Turning Points
Publisher: Tichenor Publishing
ISBN: 978-0742117013
Date: 2001
```

### Introduction (context only: never use it for content warnings)

```text
In the past, fathers could stare down at the boy in the bassinet and dream of fishing trips and games of catch. Dreams for little girls were very different . . . softer. Today, however, when it comes to raising, happy and confident young women, "parent" is an equal opportunity position. Fathers and daughters have much to talk about, worlds to share. Learning to hit a curve ball or make the smart career move--once largely the arena of fathers and sons--is now fully and joyfully open to fathers and daughters. Thank Title IX for giving girls the opportunity to not only compete in sports, but to aspire to compete at the highest level. Thank equal opportunity for giving young women the ability to enter the professions and climb up organizations in numbers equal to men. Daddy’s Little Girl has taken on new meaning . . . Sports Psychology by Janet O’Neill.
```

### Performance text (classify this)

```text
I never had many conversations with my father until I was 7, when he taught me the art of the curve. Most adults don't know how to throw a curve ball, but my father had me sinking that ball several inches in a matter of months. Yes, baseball, because dad said softball was the weaker sport and I’ m not weak! Soon, we were watching football on Sunday afternoons and I was caddying for him at local golf tournaments. And soon, I'd found a best friend.

Let's get one thing straight: it wasn't that dad was sports obsessed. It wasn't that I felt pushed into playing. We'd merely found a way to communicate. A way to cross the barriers between adult and child, man and girl. Sport was a culture. A language. My moments with my father can be told as a series of sports stories. A veritable highlight reel, as my dad would say. Ready for some sports stories? Kickoff occurs now.

July, 1981. My first day in softball. We'd given up the baseball dream at this point. See, I could make the ball sink, but I couldn't catch or hit-two vital skills to life as a ball player. So I'm playing softball, playing deep right/center field. See, we had 14 players and we were just kids, so the league said everyone gets to play the field. I'm behind the outfielders because, well, I my athleticism wasn't exactly working out. I'd spend my time stepping on ant hills and looking into the sun. The chances of a 9 year-old girl popping one out 250 feet to where I was wasn't too likely. Still, dad's on the bleachers yelling "Hit one out there to my Adrian!! She'll show you how it's done!!" Unless Mike Schmidt had joined girls youth softball, I wasn't going to show anyone how it was done. "Hit it to Adrian!" Yeah, dad, I thought as I stepped on an ant pile. Rebuild.

November, 1983. Dad takes me to a football game at his alma-mater. We pack a thermos full of hot chocolate and bear the cold of University of Minnesota football. Beforehand, he takes me to see where he lived, as well as the fireplace at the union where he first met mom, as well as the restaurant he first took her out to. I catch him sneaking a beer out of the trunk and I call him on it. Did you bring enough for everyone? After the game, Dad says just two words: "Good day." I turn the radio to the post-game show as we drive home.

March, 1985. Dad and I watch the Georgetown/Villanova basketball game. Georgetown was favored by a bazillion points. Villanova won. "That could be you," dad says, "That could be you."

May, 1986. My first soccer league game. I still ran, well, I ran not even like a girl, so they put me in as goalie. I love the way my abilities always dictated my position! But something weird happened that day. No one scored. That's right. No one. I didn't give up a goal. Neither did the other goalie, but still. A scoreless tie. Greatest moment of my life. Dad went home to make phone calls. A phenom was on his hands! But what if I had to play soccer again?

May, 1986-three days later. My next game. People are kicking the ball hard this game. At me! I blocked it with my hands, my chest, my butt, my head. I dove around. No one scored. Coming home from the game, we both looked at my muddied uniform and didn't say a word. The dirt said it all. Dad didn't make phone calls that night. People called him.

June, 1988. By this point, I'd grown another 5 inches. I was Amazon woman! And I wasn't quite as uncoordinated as I used to be. Not so many soccer ball imprints on my face. Colleges started calling. Dad started giving me advice:

1.) Never listen to anything a college says. If they say you’re good, it just is part of a script read over the phone. 2.) Never doubt yourself If a college says you aren't good, they just haven't watched you play enough. 3.) Sports equates to college. College equates to degrees. Degrees equate to jobs. Jobs equate to success. Thus, sports can equal success, but you've got to know your math. 4.) Never count on sports. Count on him. Dad. Sports will come and go. You may find yourself stepping on anthills a year from now, so count on people. And yourself

August, 1989. Dad and I embark on our tours of college campuses. Everywhere from Virginia to UCLA. Dad buys a video camera to capture the moments. The guy who sold it said "just press play." Unfortunately, it took a little more than" just press play." First time I'd ever heard my dad swear. The "S" word. A bonding moment.

On the way, we bought a regular camera. As we passed each state line, we stopped at the border, set the timer, and took pictures of the two of us next to the state welcome signs.

September, 1989. I’m playing against Westview, our rival, when all of a sudden I see players running up into the stands. I focus on the game. It's tied 1-1. Out of the corner of my eye, I see my coach bolt for the bleachers. As I look, I see they are headed for row 5, where dad always sits.

The next thing I know, I'm running for him. I'm still not a good runner, but today I am. I'm next to him and he's not saying anything. Not "help". Not "don't worry, Adrian". Not even, "give me a second". He's just lying there.

Fifteen minutes pass. Fifteen minutes I still can't recall. The next thing I remember, I'm at the hospital. They tell me I can't see him so I dash for the chapel. I get down on my knees and pray. Pray for answers, pray for my eyes to open and I'll be back in front of the goal and dad is saying, "Good block, kid!"

I pray for him to live. I get my wish. My father has suffered a massive stroke. He cannot speak. No one knows how bad it actually is. I visit him and he shows no recognition. No smile.

November, 1989. I realize that we never got the pictures developed from our college trip last summer. I take the pictures to a local department store and three days later I return for them. I look through the picture bin, but they're not there. Maybe they couldn't read the handwriting. Check under other letters. A through Z, they're not there.

I ask the clerk, "Excuse me, but are pictures running late today?" She informs me that everything is on time. "Then where are my pictures?" He says, Oh, you're Adrian Clark, aren't you? I'm sorry, but your pictures didn't come out. Overexposed. May have been our fault. The next set of developing is on us.

It takes me 10 seconds to register what was just said. The last pictures I will ever have of my father with his arm around me, of his smile, of his glow and support.. .are gone. Gone. But hey, I should be happy because I get a free set of developing next time.

And, see, I want that film. I've gotta have that film. I've been counting on it. It's all have left of the father I know. And I wasn't the one who messed it up - they did. So fix my damn pictures and give them back. No "please". No "excuse me, fix my pictures". Just get me my pictures. The clerk doesn't know what has hit her and calls for the manager. I say, "They screwed up my pictures. Give me back my pictures!" The manager calls my mom and she comes to get me. Now, I know what you're thinking. That last story doesn't have anything to do with Sports. Not all of these moments are sports-related. Don't you get it by now? Nothing has to do with sports. Sports represent a means to an end. Sports was communication for my dad and myself That's it. Nothing is ever what it seems.

Let's say you join a country club. To play golf. It's all about sports, but it's not. It's about meeting friends, escaping from home. Let's say you jog daily. It's about sports, but it's not. Really you love the nature or you love skipping your homework to run, or your father has a massive stroke when he's 49 years old and he should have run more.

See, sports are just a cover. Communicating messages only certain people comprehend. Masking life so we can take it all in without saying so.

October, 1993. My team is in the NCAA playoffs for the first time. I'm in goal for our first televised game. I left for the game after making mom leave it on for dad to watch. She says he showed no expression during the game. We won, 2-0. Trust me, he showed expression. It may not have been about the game, but it was there. See, it's all about sports, but it's not.
```

---

## IC-2333: Standing on the Roof Naked

- Title: Standing on the Roof Naked
- Author (byline): Francess Lantz
- Work: On the Fringe: Stories
- Publisher: Dial
- Publication date as stated: April 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2208
- Already set (do not supply): none

### Source block (context only)

```text
Author: Francess Lantz
Book: On the Fringe: Stories
ISBN: 978-0142500262
Publisher: Dial
Date (Month/Year): April 2001
AWARD HISORTY
IL State Finalist
```

### Introduction (context only: never use it for content warnings)

```text
Standing on the Roof Naked by Francess Lantz
```

### Performance text (classify this)

```text
I don't know why . . . I wanted to be a boy until I was thirteen years old. To this day, I still feel more comfortable in baggy boy clothes than dresses. My hair is short and tangled and in my eyes instead of long and silky like some Pantene com-mercial. I'm different. And in this world, let me tell you, different is not good.

It's Monday morning and I'm at school. Walking alone, as usual.

"Hey, Johnny," Rory Peterson calls as I walk past. Actually, my name is Jeannie, but the jocks who like to harass me think it's a hoot to call me John.

"Nothing wrong with her that a hot date wouldn't cure," Mike Forelli says.

"Yeah, right-a hot date with a hot dyke," Rory snickers.

At home Mom greets me at the door with a smile and a plate of peanut butter cookies. "The doctor came by today." I freeze. The cookie feels like it's coming up in my throat. "Daddy ate a little more today. Dr. Heidleman was pleased."

I let out a breath and will my shoulders to relax. My father hasn't been taken to the hospital. He isn't dead. He's got cancer. But Mom never uses the C word. "He's under the weather," she says. Or, "He's feeling poorly."

He's dying! I want to scream.

I'm mad all the time-at Rory Peterson and his brain-dead buddies, at my father for getting sick, at myself for being such a freak.

******************

At lunch on Fridays we're allowed to play CDs in the cafeteria. Different kids take turns acting as DJ. Today I come into the cafeteria and see a kid setting up a couple of turntables. I've seen him around before, but I don't know his name. He's over six feet tall and skinny, with pale skin and spiky black hair. He reminds me of a spider, but not a dangerous one. A daddy longlegs maybe.

He sets up a microphone and starts to spin a stack of record albums. It's all old soul music, really funky stuff. . He's really putting on a show. I notice a few jocks are whispering and snickering. They can't deal with anything new or different. Their motto is: If it's unusual, it must be ridiculed. Who is this dude? When the bell rings, I walk past the turntables. "Hey, Reilly," someone calls. He looks up. Now I know his name.

*******************

Last week I saw a book in Borders called Lesbian Couples. Some of the women in it looked like me-skinny and flat-chested, with short hair and no makeup.

Is that what I am? I wonder. A lesbian?

I try to imagine kissing a girl. Strange. I try to imagine kissing a boy. Also strange. What's wrong with me?

When I was six, I started drawing pictures of car wrecks and plane crashes. Lots of blood, lots of severed body parts. All I knew was that when I drew those pictures, I felt wild, I felt free. Like standing on the roof naked, screaming my lungs out.

Now it's music that does that for me. I wish I had the talent to get up in front of everybody. I wish I had the nerve.

******************

Mom has started sleeping in the La-Z-Boy recliner in the spare bedroom. That must mean my father is getting worse. I peeked in at him yesterday morning. His cheeks were covered with stubble and his hair was mussed. And his body under the covers, it looked so small, more like a child's than a man's. He didn't see me. He was staring at the wall, at nothing.

Each time my mother gets up out of the La- Z-Boy, I hold my breath. If I can hold it until she sits back down, my father won't die. I wrap my arms around my legs and go on waiting.

*********************

"Jeannie, do you know Reilly Briggs?" Mrs. Filbert asks. "He's the boy who was playing records in the cafeteria last week. He's in my third-period class. He told me he's looking for someone to write raps to his beats. I gave him your name," she says. "I hope that's all right."

**************

It's study hall and I get a pass to go to the restroom. Oh, shit. Rory Petersen and Mike Forelli are hanging out in the hall near the water fountain. I do an about-face, but it's too late. They see me. "Hey, Johnny, need to use the boys' room?" Rory calls, coming in close to leer at me.

Mike sidles up behind me, cutting off my path of escape. "Do you think she pees standing up?" he muses.

"Maybe she is actually a he," Rory announces. "I mean, what if old Johnny isn't a girl who wants to be a guy, but a guy who wants to be a girl?" Mike nods. "We could find out."

They look at each other. Then suddenly they grab me. "Hey!" I try to break free, but they've got my arms pinned to my sides and they're half-dragging, half-shoving me into the boys' room. I let out a shriek, but it's too late. I'm inside, watching the door thump closed.

"Please," I whimper. I'm a pathetic sight. Frightened, humiliated, my knees weak and shaking. "Let me go."

"Not till we see what you got down there," Rory says. He reaches for the snap on my jeans and pops it open. Suddenly, the door opens and, like a spider in shining armor, Reilly Briggs walks in.

"What the hell's going on?" Reilly asks, glancing nervously at me.

Mike grabs my jeans and pulls them down. I'm too mortified to speak, to move. I'm just hunched over and shivering.

"Let her go or I'm going straight to the principal," Reilly says.

"Oh, for Christ's sake," Rory groans. "What does it matter what's in John-John's pants? Male or female, I don't want to get near it." Mike laughs. They exchange a glance, then release me and walk out the door, roughly shoving Reilly against the wall as they go.

I pull up my pants and fumble with the zipper. "You're Jeannie Holtz, right?" He smiles. There's definitely a rap in all this.”

I don't write raps, don't have a clue where to start. Still, all day long, words, phrases, even some rhymes begin to percolate in my head. I don't know where they're coming from.

Am I a girl, a boy, a lesbo, a fag?

I don't want a label, I don't need your tag.

I say the lines over and over in my head.

************

[A few days later I go to Reilly’s. He] lives in an apartment house near the river. "Ms. Filbert says you're a poet," Reilly tells me, clearing aside some records to sit on the bed.

"I don't know how to rap," I say. "But I wrote down a couple of lines."

My hand is trembling as I pull the paper from my pocket. It drops on the floor and Reilly snatches it.. I stand there, cheeks burning, stomach churning. I want to run away and never look back. Finally, he turns around, looks me over. He taps the page and smiles. "I think I can do something with this."

Soon I'm spending almost every afternoon at Reilly's house. Mom doesn't ask where I am. She's too busy taking care of my father to even notice I'm gone.

Reilly puts beats behind my rhymes. He makes me read them into the microphone, over and over. He doesn't laugh at me, thank God, and he never mentions what he saw that day in the boys' room. All he says is:

"Don't just read the words, Jeannie, feel them. Get pissed."

I shake my head and stare at the pattern on his Indian bedspread. I can write mad, but I can't let myself be mad. It's too scary.

. "I'll lay down a beat," he says. "Just close your eyes and sing. Don't think, just do it. Whatever pops into your head."

But the only words that come are too painful to say. I'm a freak, I'm a freak, I'm a freak.

*************

[My] father passed away late last night. I can't take in the fact that my father is dead. It's like the Grand Canyon, too vast to comprehend.. I want to cry and scream and fall on my knees, but my feet are paralyzed and I'm unable to produce even one tear.

******* The winter dance is this weekend. Reilly is going to be there, spinning discs.

I let Mom take me to the store, buy me a dress I'd never pick for myself in a million years. It's black velvet with lacy snowflakes around the neck and sleeves. At home I try on the dress and shoes. Mom looks really pleased. I force myself to smile, to push my hair out of my eyes. It's the least I can do for her.

**************

It's the night of the dance and I'm standing outside the school in my new dress and shoes. Underneath, just to make me feel more comfortable, I'm wearing black bike shorts and a sleeveless black undershirt. I can hear the music pounding inside, hear the people talking and laughing.

I practically run into Mike Forelli.

"Whoa, look at Johnny," he tells his buddies. "Shake it, baby, shake it. Show us what you've got!" Everyone laughs. I snake my way through the crowd of writhing bodies on the dance floor, putting some distance between Mike and me. Nobody notices me. I close my eyes and let the music throb through me. I pretend I'm alone in my room. Finally the music ends and Reilly starts setting up his turntables, a tape deck, and a mike.

He told me at our second rehearsal that he wanted me to perform my rap tonight, but I said no. I knew I couldn't get up in front of the entire school and rap. Reilly pops in a new cassette and the tempo speeds up. And suddenly I realize he's laying down the beat for my rap. The one we created together.

Reilly leans into the microphone. "Listen up, everyone. Jeannie Holtz is going to rap for us. Jeannie, get on up here."

Oh, my God. Everyone is looking at me. I can hear snickering. I'm just sitting there, staring at my feet, trying to will myself to disappear. Someone starts to clap. "Jean-nie! Jean-nie!" Soon all the people in the gym are stamping their feet and chanting my name.

Someone grabs my hand and pulls me up. The crowd shoves me onto the stage. I want to die. Just curl up in a corner and die. Then I spot Rory and Mike at the front of the crowd.

"Shake it, Johnny, shake it!" Mike taunts. "Come on, dyke. Show us what you've got."

That's when it happens. It's like a bomb going off inside of me, ripping me apart. I open my mouth and words explode into the air.

"Am I a girl, a boy, a lesbo. a fag?" I shout. "I don't want a label, I don't need your tag."

I'm glaring at Mike now, spitting out the words. "I'm a person, a human. I need room and a little respect, To grow and connect, Inspect, reject. Find my place in this world, Look for love, try sex."

Everyone is staring at me, stunned-the kids, the teachers, the parent chaperones. But I barely notice. I'm thinking about my mother, my father, Reilly, Rory and Mike. All the confusion, the rejection, the mistakes, the longing, the pain.

I grab the front of my dress and pull as hard as I can. I feel the seams give way. I pull again and the material falls off me, revealing my bike shorts and undershirt. I take off my shoes and throw them into the crowd.

The music is changing now. This is the spot where Reilly wanted me to sing the chorus.

"I'm a freak," I sing in a low, soulful voice. It's a mournful lament. Then my voice rises. "I'm a freak, a freak, a freak!" It's a proclamation now, a joyful refrain. I jump up on the amplifier and spit out the next lines.

"You want to trash me, smash me, Dis me and bash me.

Still I lower my head and I let you catch me.

Is it something in me,

That makes me freeze?

A fear of talking back,

Of showing feelings, I'm reeling,

I want to shout it to the ceiling:

I won't bow down, you won't catch me kneeling."

"I'm a freak!" I moan, so alone, so sad. "I'm a freak!" I shriek, angry, violent. "I'm a freak, a freak, a freak!" I cry, so joyous, so complete.

And then it's over and there's silence, just silence until someone decides to clap. Soon everyone is applauding, cheering. And I'm standing there in my bike shorts and undershirt, barefoot, the shredded dress at my feet, suddenly just me again-only different. Because for the first time in years, in centuries, in eons, I didn't stuff my emotions down inside of me. I was standing on the roof naked, screaming my lungs out, and it felt good.
```

---

## IC-2334: Stolen Moments

- Title: Stolen Moments
- Author (byline): Janet O’Neill
- Work: Turning Points
- Publisher: Tichenor Publishing
- Publication date as stated: 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: WOMAN, SUSAN, RICKY, AUNT, FATHER, GINA
- Teaser before the introduction: Yes
- Spoken words (computed): 1120
- Already set (do not supply): none

### Source block (context only)

```text
Author: Janet O’Neill
Book: Turning Points
Publisher: Tichenor Publishing
ISBN: 978-0742117013
Date: 2001
```

### Introduction (context only: never use it for content warnings)

```text
In 1967 the Supreme Court ruled in Loving v. Virginia that marriage bans between whites and blacks was unconstitutional, but before that interracial marriages were illegal in 16 states.

By 1995 interracial marriages were more common and far more accepted than they had ever been. But that didn’t always make it easy.

1995: The year a jury found OJ Simpson “not guilty” for the murder of his ex-wife Nicole. Seinfeld was the most popular television show on 1 of the only 3 major networks.

And Men were from Mars and Women from Venus. Black and white relationships were no longer taboo . . . But Susan’s family and friends still had some issues.

Stolen Moments by Janet O’Neill
```

### Performance text (classify this)

```text
I've gotten used to the snickers. The whispering. The name calling. The seven-year-old girl who just points and says Mommy! Look! I know Ricky and I are a scandal. Still, it stuns me when a woman approaches me at a restaurant and says:

WOMAN: Didn't know you liked dark meat. What do you say? Well, actually I'm a vegetarian? It never works. So I smile. Shake my head. And return to my seat. Skin pigment. It can be hell.

Ricky and I met at the Wash-n-Save Laundromat. He had this aloof look, like nothing could touch him and yet a magnetic charm that made you want to try. Our first conversation was pretty ironic:

SUSAN: Hey, I don't think you want to do that

RICKY: Do what?

SUSAN: Well, you need to separate your clothes. You're mixing your white and your coloreds. After dating for a few months, the mixing of the colors and the whites had taken on a much deeper meaning. No one approved. A glare from the parking attendant. A reprimand from my aunt:

AUNT: That's fine if you want to mix for a while, but always meet in a public place. Nothing gets stolen that way, dear. And of course, there was the resonating response from my father:

FATHER: I don't have anything against Blacks. I think everyone ought to own one. I kept using the line: It's 1995. People aren't going to tolerate that racist talk. Never seemed to make a differ-ence. Ricky and I didn't date on the assumption that we'd act like we're colorblind. Race did matter. Everyone else thought so and that made it an issue. But, we were in love. Race became another thing that we could talk about. See, when you're in love, you don't ignore things about the other person. You admire each aspect of them. You cherish them. And it was love. I'd never been in love before, but if this wasn't it, I didn't even want to know how giddy I'd be when the real thing came along. We'd spend time in the park; watch old M*A *S*H* re-runs; talk all night and then call in sick so we could let the moments linger. Ricky loved me. No doubts. No questions asked. Which is why, when my best friend Gina approaches me with her patented, “We gotta talk,” I could hardly believe that the topic was my so-called "dysfunction."

GINA: What are you thinking? Do you have any idea what people are saying about you?

SUSAN: Let me guess. I'm betraying my race, slumming it, got jungle fever, and if I said the" N" word, I could list a string of adjectives created from it. Who cares?

GINA: Fine. Who cares what they're saying. Here's what I, you best friend, am telling you. Get out. Please. Susan, it's just not right. I'm no Klansman or anything, but I just don't think you know what you're doing . . .

SUSAN: God, Gina. I expected this from my parents. But you? It's 1995. No. You understand me. It's 1995. You know how Bryan Adams sings about the Summer of '69 being the best time of his life? The Summer of '95. It was the best time for me. Despite it all, Ricky and I had fallen deeply in love. So deeply, that when I discovered I was pregnant, I was honestly overjoyed. Really. I told Ricky about it. He agreed; it was a blessing.

RICKY: Guess I'm going to have to make you legit.

SUSAN: Are you asking what I think you are?

RICKY: Not yet. I gotta wait and do it up special. But don't make any plans at New Years.

There I was. A not-yet-wed pregnant woman in a relationship no one approves of, and yet all I could say was Sweetheart, that sounds wonderful. I was about to get married. Be a mom. Do it all. Wow. No turning back now. I thought of my father. No turning back now. I thought of Gina, my church, my coworkers. No turning back now. August was spent in a mad rush between doctor’s appointments, titanic shopping sprees, and stacks of catalogs to be perused in the late afternoons, and, oh yes, stealing moments with Ricky. I was eating for two. Shopping for a wedding. It was exhausting. I collapsed in bed - thoroughly spent; thoroughly satisfied. Then one morning in early September, Ricky went out early to get doughnuts. Chocolate long johns. A dozen. We were skipping work again. I loved it. He left at 7:30. 8:00: Ricky hadn't returned. 8:30: nothing. 9:00: nothing. I called his friends, my friends, his family - no one had seen him. At 9:43, the call came. I knew something awful had happened. I couldn't pick up the phone, so I just listened to the machine. Ricky was dead. Dead. Dead. It was a car crash. There was no brake fluid. He had slammed into a tree. It appeared that the car had been tampered with. And that was it. And you know I could have been thinking a million things like my poor Ricky, should I call his parents? Should I go see him? What do I do? But instead, all I could think was: he was driving my car. It was supposed to be me. It was meant for me. It should have been me. I mean, that's kind of tough to grapple with. Did Ricky die because of lack of brake fluid and the placement of a tree? Or did he die because he loved me? Because someone didn't approve. I mean, it couldn't have been that, right? I mean, it's 1995. Two events shaped my October: the crash was found not to be an accident, and I lost my baby in its first trimester. The revelation of the crash just confirmed what I knew all along; the revelation of the baby was a strange mix of feelings between this black hole of emotion and an unsettling sense of relief. I felt this incredible void because I'd lost the last part of Ricky I had left. I felt relief that our child would never have to experience the hatred people felt for his Black father, merely hoping for a few seconds of peace.

I became a loner. I didn't see family. I didn't see Gina. I quit my job. But, I spent my time thinking of these people, asking myself one question: Who did it? Who took it all away? In the end, all I had was the moments. Stolen moments of one summer with a man. A Black man, but a man just the same. Moments in the park. Moments holding hands. Moments forever remembered in black and white.
```

---

## IC-2335: The Story of My Life

- Title: The Story of My Life
- Author (byline): Helen Keller
- Work: Not specified
- Publisher: Bantam Books, Inc.
- Publication date as stated: May 1990
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1090
- Already set (do not supply): none

### Source block (context only)

```text
Author: Helen Keller
ISBN: 978-0553213874
Publisher: Bantam Books, Inc.
Date (Month/Year): May 1990
```

### Introduction (context only: never use it for content warnings)

```text
Helen Keller was less than two years old when she came down with a fever. It struck dramatically and left her unconscious. The fever went just as suddenly. But she was blinded and, very soon after, deaf. As she grew up, she managed to learn to do tiny errands, but she also realized that she was missing something. "Sometimes," she later wrote, "I stood between two persons who were conversing and touched their lips. I could not understand, and was vexed. I moved my lips and gesticulated frantically without result. This made me so angry at times that I kicked and screamed until I was exhausted." She was a wild child . . . wild that is until Annie Sullivan tamed her and gave her hope for a future. Helen Keller altered our perception of the disabled and remapped the boundaries of sight and sense. This is . . . The Story of My Life by Helen Keller
```

### Performance text (classify this)

```text
The most important day I remembered in all my life is the one on which my teacher, Anne Mansfield Sullivan, came to me. I am filled with wonder when I consider the immeasurable contrasts between the two lives which it connects. It was the third of March, 1887, three months before I was seven years old.

On the afternoon of that eventful day, I stood on the porch, dumb, expectant. I guessed vaguely from my mother’s signs and from the hurrying to and fro in the house that something unusual was about to happen, so I went to the door and waited on the steps. The afternoon sun penetrated the mass of honeysuckle that covered the porch, and fell on my upturned face. My fingers lingered almost unconsciously on the familiar leaves and blossoms which had just come forth to greet the sweet Southern spring. I did not know what the future held of marvel or surprise for me. Anger and bitterness had preyed upon me continually for weeks, and a deep languor had succeeded this passionate struggle.

Have you ever been at sea in a dense fog, when it seemed as if a tangible white darkness shut you in, and the great ship, tense and anxious, groped her way toward the shore with plummet and sounding-line, and you waited with beating heart for the something to happen? I was like that ship before my education began, only

I was without compass or sounding-line, and had no way of knowing how near the harbor was. “Light! Give me light!” was the wordless cry of my soul, and the light of love shone on me in that very hour.

I felt approaching footsteps. I stretched out my hand as I supposed to my mother. Someone took it, and I was caught up and held close in the arms of her who had come to reveal all things to me and, more than all things else, to love me.

The morning after my teacher came she led me into her room and gave me a doll. The little blind children at the Perkins Institution had sent it and Laura Bridgman had dressed it; but I did not know this until afterward. When I had played with it a little while, Miss Sullivan slowly spelled into my hand the word “d-o-l-l.” I was at once interested in this finger play and tried to imitate it. When I finally succeeded in making the letters correctly I was flushed with childish pleasure and pride. Running downstairs to my mother I held up my hand and made the letters for doll. I did not know that I was spelling a word or even that words existed; I was simply making my fingers go in a monkey-like imitation.

In the days that followed I learned to spell in this uncomprehending way a great many words, among them pin, hat, cup, and a few verbs like sit, stand, and walk. But my teacher had been with me several weeks before I understood that everything has a name. One day, while I was playing with my new doll, Miss Sullivan put my big rag doll into my lap also, spelled “d-o-l-l” and tried to make me understand that “d-o-l-l” applied to both. Earlier in the day we had had a tussle over the words “m-u-g” and “w-a-t-e-r.” Miss Sullivan had tried to impress it upon me that “m-u-g” is mug and that “w-a-t-e-r” is water, but I persisted in confounding the two.

In despair she had dropped the subject for the time, only to renew it at the first opportunity. I became impatient at her repeated attempts and, seizing the new doll, I dashed it upon the floor. I was keenly delighted when I felt the fragments of the broken doll at my feet.

Neither sorrow nor reflection followed my passionate outburst. I had not loved the doll. In the still, dark world in which I lived, there was no strong sentiment of tenderness. I felt my teacher sweep the fragments to one side of the hearth, and I had a sense of satisfaction that the cause of my discomfort was removed.

She brought me my hat, and I knew I was going out into the warm sunshine. This thought, if a wordless sensation may be called a thought, made me hop and skip with pleasure. We walked down the path to the well house, attracted by the fragrance of the honeysuckle with which it was covered. Someone was drawing water, and my teacher placed my hand under the spout.

As the cool stream gushed over one hand she spelled into the other the word water, first slowly, then rapidly. I stood still, my whole attention fixed upon the motions of her fingers. Suddenly I felt a misty consciousness as of something forgotten-a thrill of returning thought; and somehow the mystery of language was revealed to me. I knew then that “w-a-t-e-r” meant the wonderful cool something that was flowing over my hand. That living word awakened my soul, gave it light, hope, joy, set it free! There were barriers still, it is true, but barriers that could in time be swept away.

I left the well house eager to learn. Everything had a name, and each name gave birth to a new thought. As we returned to the house every object which I touched seemed to quiver with life. That was because I saw everything with the strange, new sight that had come to me. On entering the door I remembered the doll I had broken. I felt my way to the hearth and picked up the pieces. I tried vainly to put them together. Then my eyes filled with tears; for I realized what I had done, and for the first time I felt repentance and sorrow.

I learned a great many new words that day. I do not remember what they all were; but I do know that mother, father, sister, teacher were among them-words that were to make the world blossom for me, “like Aaron’s rod, with flowers.” It would have been difficult to find a happier child than I was as I lay in my crib at the close of that eventful day and lived over the joys it had brought me, and for the first time longed for a new day to come.
```

---

## IC-2336: A Telephone Call

- Title: A Telephone Call
- Author (byline): Dorothy Parker
- Work: Here We Are, A Telephone Call
- Publisher: Travelman Publishing
- Publication date as stated: Oct 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2382
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dorothy Parker
Book: Here We Are, A Telephone Call
ISBN: 978-1860920172
Publisher: Travelman Publishing
Date(Month/Year): Oct 2001
```

### Introduction (context only: never use it for content warnings)

```text
A watched pot will never boil and a watched phone will never ring. All she really wanted was A Telephone Call by Dorothy Parker . . . .
```

### Performance text (classify this)

```text
PLEASE, God, let him telephone me now. Dear God, let him call me now. I won't ask anything else of You, truly I won't. It isn't very much to ask. It would be so little to You, God, such a little, little thing. Only let him telephone now. Please, God. Please, please, please.

If I didn't think about it, maybe the telephone might ring. Sometimes it does that. If I could think of something else. If I could think of something else. Knobby if I counted five hundred by fives, it might ring by that time. I'll count slowly. I won't cheat. And if it rings when I get to three hundred, I won't stop; I won't answer it until I get to five hundred. Five, ten, fifteen, twenty, twenty-five, thirty, thirty-five, forty, forty-five, fifty.... Oh, please ring. Please.

This is the last time I'll look at the clock. I will not look at it again. It's ten minutes past seven. He said he would telephone at five o'clock. "I'll call you at five, darling." I think that's where he said "darling." I'm almost sure he said it there. I know he called me "darling" twice, and the other time was when he said good-by. "Good-by, darling." He was busy, and he can't say much in the office, but he called me "darling" twice. He couldn't have minded my calling him up. I know you shouldn't keep telephoning them--I know they don't like that. When you do that they know you are thinking about them and wanting them, and that makes them hate you. But I hadn't talked to him in three days-not in three days. And all I did was ask him how he was; it was just the way anybody might have called him up. He couldn't have minded that. He couldn't have thought I was bothering him. "No, of course you're not," he said. And he said he'd telephone me. He didn't have to say that. I didn't ask him to, truly I didn't. I'm sure I didn't. I don't think he would say he'd telephone me, and then just never do it. Please don't let him do that, God. Please don't.

"I'll call you at five, darling." "Good-by, darling.,' He was busy, and he was in a hurry, and there were people around him, but he called me "darling" twice. That's mine, that's mine. I have that, even if I never see him again. Oh, but that's so little. That isn't enough. Nothing's enough, if I never see him again. Please let me see him again, God. Please, I want him so much. I want him so much. I'll be good, God. I will try to be better, I will, If you will let me see him again. If You will let him telephone me. Oh, let him telephone me now.

Ah, don't let my prayer seem too little to You, God. You sit up there, so white and old, with all the angels about You and the stars slipping by. And I come to You with a prayer about a telephone call. Ah, don't laugh, God. You see, You don't know how it feels. You're so safe, there on Your throne, with the blue swirling under You. Nothing can touch You; no one can twist Your heart in his hands. This is suffering, God, this is bad, bad suffering. Won't You help me? For Your Son's sake, help me. You said You would do whatever was asked of You in His name. Oh, God, in the name of Thine only beloved Son, Jesus Christ, our Lord, let him telephone me now.

I must stop this. I mustn't be this way. Look. Suppose a young man says he'll call a girl up, and then something happens, and he doesn't. That isn't so terrible, is it? Why, it's gong on all over the world, right this minute. Oh, what do I care what's going on all over the world? Why can't that telephone ring? Why can't it, why can't it? Couldn't you ring? Ah, please, couldn't you? You damned, ugly, shiny thing. It would hurt you to ring, wouldn't it? Oh, that would hurt you. Damn you, I'll pull your filthy roots out of the wall, I'll smash your smug black face in little bits. Damn you to hell.

No, no, no. I must stop. I must think about something else. This is what I'll do. I'll put the clock in the other room. Then I can't look at it. If I do have to look at it, then I'll have to walk into the bedroom, and that will be something to do. Maybe, before I look at it again, he will call me. I'll be so sweet to him, if he calls me. If he says he can't see me tonight, I'll say, "Why, that's all right, dear. Why, of course it's all right." I'll be the way I was when I first met him. Then maybe he'll like me again. I was always sweet, at first. Oh, it's so easy to be sweet to people before you love them.

I think he must still like me a little. He couldn't have called me "darling" twice today, if he didn't still like me a little. It isn't all gone, if he still likes me a little; even if it's only a little, little bit. You see, God, if You would just let him telephone me, I wouldn't have to ask You anything more. I would be sweet to him, I would be gay, I would be just the way I used to be, and then he would love me again. And then I would never have to ask You for anything more. Don't You see, God? So won't You please let him telephone me? Won't You please, please, please?

Are You punishing me, God, because I've been bad? Are You angry with me because I did that? Oh, but, God, there are so many bad people --You could not be hard only to me. And it wasn't very bad; it couldn't have been bad. We didn't hurt anybody, God. Things are only bad when they hurt people. We didn't hurt one single soul; You know that. You know it wasn't bad, don't You, God? So won't You let him telephone me now?

If he doesn't telephone me, I'll know God is angry with me. I'll count five hundred by fives, and if he hasn't called me then, I will know God isn't going to help me, ever again. That will be the sign. Five, ten, fifteen, twenty, twenty-five, thirty, thirty-five, forty, forty-five, fifty, fifty-five. . . It was bad. I knew it was bad. All right, God, send me to hell. You think You're frightening me with Your hell, don't You? You think. Your hell is worse than mine.

I mustn't. I mustn't do this. Suppose he's a little late calling me up --that's nothing to get hysterical about. Maybe he isn't going to call--maybe he's coming straight up here without telephoning. He'll be cross if he sees I have been crying. They don't like you to cry. He doesn't cry. I wish to God I could make him cry. I wish I could make him cry and tread the floor and feel his heart heavy and big and festering in him. I wish I could hurt him like hell.

He doesn't wish that about me. I don't think he even knows how he makes me feel. I wish he could know, without my telling him. They don't like you to tell them they've made you cry. They don't like you to tell them you're unhappy because of them. If you do, they think you're possessive and exacting. And then they hate you. They hate you whenever you say anything you really think. You always have to keep playing little games. Oh, I thought we didn't have to; I thought this was so big I could say whatever I meant. I guess you can't, ever. I guess there isn't ever anything big enough for that. Oh, if he would just telephone, I wouldn't tell him I had been sad about him. They hate sad people. I would be so sweet and so gay, he couldn't help but like me. If he would only telephone. If he would only telephone.

Maybe that's what he is doing. Maybe he is coming on here without calling me up. Maybe he's on his way now. Something might have happened to him. No, nothing could ever happen to him. I can't picture anything happening to him. I never picture him run over. I never see him lying still and long and dead. I wish he were dead. That's a terrible wish. That's a lovely wish. If he were dead, he would be mine. If he were dead, I would never think of now and the last few weeks. I would remember only the lovely times. It would be all beautiful. I wish he were dead. I wish he were dead, dead, dead.

This is silly. It's silly to go wishing people were dead just because they don't call you up the very minute they said they would. Maybe the clock's fast; I don't know whether it's right. Maybe he's hardly late at all. Anything could have made him a little late. Maybe he had to stay at his office. Maybe he went home, to call me up from there, and somebody came in. He doesn't like to telephone me in front of people. Maybe he's worried, just alittle, little bit, about keeping me waiting. He might even hope that I would call him up. I could do that. I could telephone him.

I mustn't. I mustn't, I mustn't. Oh, God, please don't let me telephone him. Please keep me from doing that. I know, God, just as well as You do, that if he were worried about me, he'd telephone no matter where he was or how many people there were around him. Please make me know that, God. I don't ask YOU to make it easy for me--You can't do that, for all that You could make a world. Only let me know it, God. Don't let me go on hoping. Don't let me say comforting things to myself. Please don't let me hope, dear God. Please don't.

I won't telephone him. I'll never telephone him again as long as I live. He'll rot in hell, before I'll call him up. You don't have to give me strength, God; I have it myself. If he wanted me, he could get me. He knows where I ram. He knows I'm waiting here. He's so sure of me, so sure. I wonder why they hate you, as soon as they are sure of you. I should think it would be so sweet to be sure.

It would be so easy to telephone him. Then I'd know. Maybe it wouldn't be a foolish thing to do. Maybe he wouldn't mind. Maybe he'd like it. Maybe he has been trying to get me. Sometimes people try and try to get you on the telephone, and they say the number doesn't answer. I'm not just saying that to help myself; that really happens. You know that really happens, God. Oh, God, keep me away from that telephone. Keep me away. Let me still have just a little bit of pride. I think I'm going to need it, God. I think it will be all I'll have.

Oh, what does pride matter, when I can't stand it if I don't talk to him? Pride like that is such a silly, shabby little thing. The real pride, the big pride, is in having no pride. I'm not saying that just because I want to call him. I am not. That's true, I know that's true. I will be big. I will be beyond little prides.

Please, God, keep me from, telephoning him. Please, God.

I don't see what pride has to do with it. This is such a little thing, for me to be bringing in pride, for me to be making such a fuss about. I may have misunderstood him. Maybe he said for me to call him up, at five. "Call me at five, darling." He could have said that, perfectly well. It's so possible that I didn't hear him right. "Call me at five, darling." I'm almost sure that's what he said. God, don't let me talk this way to myself. Make me know, please make me know.

I'll think about something else. I'll just sit quietly. If I could sit still. If I could sit still. Maybe I could read. Oh, all the books are about people who love each other, truly and sweetly. What do they want to write about that for? Don't they know it isn't tree? Don't they know it's a lie, it's a God damned lie? What do they have to tell about that for, when they know how it hurts? Damn them, damn them, damn them.

I won't. I'll be quiet. This is nothing to get excited about. Look. Suppose he were someone I didn't know very well. Suppose he were another girl. Then I d just telephone and say, "Well, for goodness' sake, what happened to you?" That's what I'd do, and I'd never even think about it. Why can't I be casual and natural, just because I love him? I can be. Honestly, I can be. I'll call him up, and be so easy and pleasant. You see if I won't, God. Oh, don't let me call him. Don't, don't, don't.

God, aren't You really going to let him call me? Are You sure, God? Couldn't You please relent? Couldn't You? I don't even ask You to let him telephone me this minute, God; only let him do it in a little while. I'll count five hundred by fives. I'll do it so slowly and so fairly. If he hasn't telephoned then, I'll call him. I will. Oh, please, dear God, dear kind God, my blessed Father in Heaven, let him call before then. Please, God. Please.

Five, ten, fifteen, twenty, twenty-five, thirty, thirty-five.…
```

---

## IC-2337: This is a Public Service Announcement

- Title: This is a Public Service Announcement
- Author (byline): Laurie Notaro
- Work: The Idiot Girls’ Action-Adventure Club
- Publisher: Villard Books
- Publication date as stated: July 2002
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1066
- Already set (do not supply): none

### Source block (context only)

```text
Author: Laurie Notaro
Book: The Idiot Girls’ Action-Adventure Club
ISBN: 978-0375760914
Publisher: Villard Books
Date (Month/Year): July 2002
```

### Introduction (context only: never use it for content warnings)

```text
Snicker if you will, but the International Paruresis Association, or IPA, estimates that the fear using a public restroom affects an estimated 17 million Americans, or 7 percent of the population. Think about it: You can avoid spiders or heights or flying and many other sources of common fears. But hydrating the body and releasing toxins is essential to life. And the fear, in part, is due to all of you who AREN’T afraid of the public restroom . . . in fact it’s because some of you are just too dang comfortable in there! So . . . especially for all you women out there . . . This is a Public Service Announcement by Laurie Notaro.
```

### Performance text (classify this)

```text
I hate public bathrooms.

I love and respect the sanctity of my own home potty; it may be as dirty as a truck stop, but at least I know the filth is mine, and I am free to do as I please or need. The fear of having to use a public bathroom is so horrible that I will do just about anything to avoid it.

When I was in sixth grade, my mother made me sign up for Girl Scout camp, and when I got there, I knew I was in for a long haul. The only way the facilities remotely qualified for the term “rest room” was because there was a light switch and a swinging bare bulb; other than that luxury, it was an outhouse, a long stream of port-o-potties lined in a row that smelled like the 4-H exhibit at the state fair on a hot day. The acoustics were incredible, and nearly echoed. What choice did I have? I held it for nearly two weeks and probably should have been hospitalized when I got home, but the pain that shot through my body when my intestines finally seized was nothing compared to the shame of pushing out a plopper within earshot of fifty Girl Scouts.

Even as an adult, I’ve noticed that some people don’t play by the rules and terrorize other people in the potty. I have therefore documented several bathroom terrorists that have tormented me and countless other potty hostages, forcing us to hold it in for unnatural periods of time. If you see yourself in any of the descriptions [you are about to hear], seek help. Cease your awful behavior before I am forced to do it for you.

Because I will.

The Trespasser: This violator is no friendly neighbor. She seeks pleasure by invading audio and aroma space of an already occupied unit by ignoring the “One-Stall Cushion” rule. She blatantly chooses the one next to it, despite groups of other available units within the vicinity. This action will automatically cease the operations being conducted in the already occupied stall, causing health risks and alarm. From a personal perspective, I can tell you that I try to use my turn-on/shut-off valve as little as possible so I don’t wear it out and become incontinent by my next birthday, because they don’t have transplants for those, you know. Try this catchphrase to remind you: “Beware of Fart, Stay One Apart.”

The Hoverer: Perhaps to avoid using a time-consuming potty protector, perhaps to mark her territory, this offender won’t let her bottom touch the seat, although it’s perfectly OK if her by-products do.

Now, the target area of a bowl is rather generous, so the reasons for a misfire are rather mysterious to me, unless the participant is completely standing up and aiming from a corner. Hovering is never, NEVER acceptable behavior unless you just dug a hole in the forest. Remember this the next time you’re tempted to resist a complete landing: “Don’t Leave Your Mark, Just Sit Down and Park.”

The Talker: Easily identifiable as the office chatterbox, the powers of this malefactor increase in strength once you are trapped in the same room and you’re half naked. Starting off with something as innocuous as “How are you?” the Talker persists in conversation until your gastrointestinal system has recoiled and everyone else in the bathroom has discovered that your mom is a lesbian, your husband has left you, and there’s a wart on your left hand. Words of caution: SILENCIO! Once the door closes on that stall, I am a nameless entity. IF I am at work, I do not exist as Laurie your co-worker, Laurie in the car pool, or the Girl That Everyone Hates. I am simply the Anonymous Pee-er. Do not attempt to make conversation with me. Do not ask me questions, and especially do not say, “BOY! Indian food again, huh?” When considering opening your mouth, let this come to mind: “Hear Me Unzip, Button Your Lip!”

The Waiter: Pity the Waiter. Unlike the others on this list, the Waiter is no criminal, sadly just a victim. Typically the Waiter has urgent emergencies at hand, yet is too polite and thoughtful to shoot off a missile while others are present. The Waiter is often in pain, clutching her abdomen in order to keep her organs from exploding. She is minutes away from death. Unfortunately, many don’t recognize the symptoms of a Wiater and hang around the bathroom like it was a free-sample booth at Costco. If you suspect there is a Waiter in your presence, leave immediately. If you are a Waiter yourself and sense that you are engaged in something of a Mexican standoff with another Waiter, call a truce, count to three, courtesy flush for background noise, then release. Offer to exit first, but only with the promise that the rival Waiter will not emerge until you have cleared the premises, lest you see each other’s face. Don’t forget now: “Silence, No Doubt; Just Get the Hell Out.”

The Primper: If the Waiter has a mortal enemy, it is the Primper. I hate the Primper. HATE THE PRIMPER! If there’s a horrifying sound a Waiter never wants to hear, it’s the THUMP of a purse on the counter. Then the digging sound of the Primper’s claws trying to find makeup, hairbrushes, and perfume. You see, I feel that if you cannot complete your prep work by the time you leave your house in the morning, you have completely forfeited your right to do so at any other point in the day. Your opportunity is over and you have lost your chance. Once, I was stuck in a bathroom waiting for a Primper to leave while my intestines threatened to shoot out of my belly button for hours. By the time the ordeal was over, it was dark outside, and everyone in my office thought I had gone home. SO the next time you plop that feed bag next to the sink, recall: “Face of a Gnome? Do Your Makeup at Home!”

So all you Trespassers, Hoverers, Talkers, and Primpers, beware. I’m waiting for you, ready to pounce from inside my favorite stall. And just because I haven’t seen your face, it doesn’t mean a thing.

I know your shoes.
```

---

## IC-2338: This is My Audition Monologue

- Title: This is My Audition Monologue
- Author (byline): Sara Zarr
- Work: Geektastic: Stories from the Nerd Herd, Pg 319-328
- Publisher: Little, Brown Books
- Publication date as stated: June 2010
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: RACHEL
- Teaser before the introduction: Yes
- Spoken words (computed): 1533
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sara Zarr
Book: Geektastic: Stories from the Nerd Herd,
Pg 319-328
ISBN: 978-0316008105
Publisher: Little, Brown Books
Date (Month/Year): June 2010
```

### Introduction (context only: never use it for content warnings)

```text
This is My Audition Monologue by Sara Zarr
```

### Performance text (classify this)

```text
RACHEL: (Pg 319-328) I wrote it. (beat) I know we’re supposed to pick something from a (airquotes) quote-unquote known work by Shakespeare or Chekhov, or one of those monologues in the drama room, but I looked at them and honestly there’s nothing that shows my range or says anything about who I am that will be memorable. And that’s what I need: to be memorable. Because, and I’m not trying to embarrass you, but you’ve had trouble remembering my name since I started auditioning freshman year. So obviously I need to take a new approach.

Look at the audition form and look at my face: Rachel Banks. Not Rochelle, not Ruthie, not Melissa -- I really don’t understand where you got that last one, but you have called me Melissa at least three times. So, my goal here is to be memorable. [So] . . .

RACHEL: You can start timing me . . . now. (deep breath) Scotty King got electrocuted while running the light board. It sounds like a joke, I know, but I’m saying that he got electrocuted. While running the light board. I’m saying that he died, during the second act of Miracle Worker when Julie-Ann Leskowitz had gotten so good at playing blind, deaf, and dumb that she didn’t stop her scene, even though the lights flashed and everyone heard the sizzling noise from up in the booth and Annie Sullivan stopped and said, “Oh my God, Scotty,” because she knew about the leak in the auditorium roof and Scotty’s belief that bare feet were good luck and we were having one of those late spring storms and there were puddles and drips everywhere, and she put it all together faster than any of us. And we stopped the show and people filed out, a lot of them not realizing what had happened and asking if they’d get a refund. Seriously, who asks for a refund for a seven-dollar high school play? I’m sorry, I’m still making it sound like a joke. You don’t know this about me, since you’ve never taken the time to know anything about me, but I use humor that way. It relieves the tension. Unless someone is actually dead, like Scotty, in which case it just ends up sounding sick and insensitive.

You know all this, of course, you were there. What you may not realize is that it was supposed to be me. (beat) Now it doesn’t sound like a joke. Now it sounds like I’m trying to get attention or turn the focus away from Scotty’s tragedy on to me.

If it had been me, would anyone have noticed? One, I’m obviously not memorable. I’ve never gotten a part. I audition every single time, and this is the mistake I’ve made. On the part of the audition form where it says: In the event you are not cast in the play, would you be willing to work behind the scenes on this production? I always put a checkmark in the YES box. Every time I see that question I think to myself:

Rachel, don’t check yes. DO NOT CHECK IT!

What happens is the part of me that would rather mop up Julie-Ann’s sweat or de-crust the greenroom furniture than not have anything to do with the play panics and I check YES. Yes, use me. Yes, abuse me. Yes, make me post call times in my own blood, I will do it. I will do anything, anything to be in the general vicinity of this auditorium every single day, including weekends.

Hence the trying-something-new-and-memorable ploy of writing my own audition, hoping it will help me relax (and it kind of is, now that I think about it). When I do the lines in my room and no one is watching, I’m so, so good and that isn’t bragging. When I practice in my room, I’m Sarah Bernhardt, I’m Julie Harris, I’m Dame Judi Dench, for real. Then I get in front of you and anyone else who might be in the room, I am so bad. So truly bad. Even I know how bad I am.

When there are lines, I say the wrong ones at the wrong time, in a total monotone, and I don’t know what to do with my hands, and one time I drooled. I was staring at the page with my mouth sort of agape I guess, because I lost my place, and this string of drool, sparkling in the stage lights, oozed right out.

This is why I check the YES box [and] how I ended up running lights. When I hand-picked Scotty to be my lighting assistant, my intent was not to kill. Originally, he wasn’t supposed to be running the board at all. Originally, he would have been my errand boy, my cue keeper, my clipboard peon. [But] I didn’t want to do lights. What I wanted was to be onstage; but since that didn’t happen, I hoped that while Scotty took care of things, I could spend a little more time with the actors and soak up some of their actory personalities.

Ever since I checked my first YES box, I’ve been stuck in this limbo between techie and performer. Unlike the techies, I do not own seventeen different black T-shirts. I do not spend my weekends scouring yard sales for the perfect Agatha Christie ashtray or Oscar Wilde table lamp. At the same time, I know I’ll never be one of those sparkling, chosen, beautiful oddballs that have “The Second I Turn Eighteen I’m Moving to New York” written all over them. I think too hard before I talk. I haven’t considered how I look from all angles. I can’t break into songs from Spring Awakening at the drop of a wool stocking. I have never dared to wear an item of clothing that strays from my jeans-and-cardigan comfort zone.

Which is why I put Scotty on the board and tried to spend a little more time with the Chosen. I thought if I want to be an actor so bad maybe I could at least try to act like an actor acts. Fake it ’til you make it. Most people do not look at Rachel Banks and think: Drama Nerd. Most people do not look at Rachel Banks and remember that Rachel Banks is her name.

The funny thing is I thought drama would be a place where being not like the others was okay, but it turns out you have to be not like the others in a way that is exactly like the others who are not like the others.

This is why I’m not doing that stupid piece from Butterflies Are Free for my audition and instead am trying to tell you who I am because let me assure you, I will never be one of them. Not in the way you expect me to. For one thing I don’t have that thing, that instinct that tells me about vintage tube tops and asymmetrical hair. But I know that doesn’t matter, that someday some director, some boy, some anybody, will like me plain and in my cardigan and not be blind to me just because I’m not aggressively DIFFERENT.

If I do this, if I leave this school and go on to study theater or go on auditions out in the real world and start getting parts, it’s not going to be because I am oh so delightfully quirky and wear unmatched shoes and tiaras around town. It’s going to be because I love it, and because I have paid my dues and been willing to check that YES box every time if only so that I can watch and learn and get out of here and finally become the real Rachel who will then go out and claim the parts that are out there waiting for me. I have what the rest of these girls do not. Passion.

Some might say I shirked my responsibilities by putting Scotty on the board at the last minute. But I figured since you don’t remember my name you wouldn’t really care if it were me or Scotty or the Queen of Sheba actually running the board, while the other one of us stayed backstage on the headset.

I know it wasn’t my fault. I know I don’t have any real responsibility for Scotty’s death, that it was a freak accident. And I also can’t help but think Scotty’s death was a sign, someone up there telling me:

• Stop checking the YES box. • Stop being willing to stay behind the scenes when what you want is to be in the scenes.

I’ve only got one more year and I’ve proved my dedication. The fact that I’m even here auditioning after what happened proves that I know the basic truth of plays and life: The show must go on. Even when it’s hard to watch the show going on without you.

I’ll take any part, I will; and if it’s Onlooker #8, I will be the best Onlooker #8 this town has ever seen. But if you can’t find a part for me, I’m going to walk away. I’m not going to hang around in the shadows anymore. This time you’ll remember my name.
```

---

## IC-2339: This is Where it Ends

- Title: This is Where it Ends
- Author (byline): Marieke Nijkamp
- Work: Not specified
- Publisher: Sourcebooks Fire
- Publication date as stated: Jan 2016
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: PRINCIPAL TRENTON, AUTUMN, FATHER, TYLER
- Teaser before the introduction: Yes
- Spoken words (computed): 1373
- Already set (do not supply): none

### Source block (context only)

```text
Author: Marieke Nijkamp
ISBN: 978-1492622468
Publisher: Sourcebooks Fire
Date (Month/Year): Jan 2016
```

### Introduction (context only: never use it for content warnings)

```text
This is Where It Ends by Marieke Nijkamp.
```

### Performance text (classify this)

```text
PRINCIPAL TRENTON: (at a podium addressing the entire school body on the 1st day of 2nd Semester) (Pg 5) Here at Opportunity, we pride ourselves on shaping the doctors, lawyers, and politicians of tomorrow. And it’s the choices you make now that will determine your future.

AUTUMN: (Pg 5-6) My brother would tell me that Principal Trenton’s words are truer than I think; that it’s up to me to make my future the best it can be. For me, college is the only way out of this misery, and Dad sure as hell isn’t going to pay my ride. Not to study dance.

FATHER: Look what happened to your mother. . .

AUTUMN: As if I haven’t counted the days, hours, minutes since Mom’s accident.

FATHER: Dance took everything from her. No daughter of mine is going into that business. Not if I can stop it.

AUTUMN: So he tries to stop me—every day. And with Mom gone, there’s no one to stop him. Not from drinking. Not from hitting me. There’s no one to keep our family from falling apart.

PRINCIPAL TRENTON: (Pg 4) . . . it’s all a matter of the decisions you make, today and every day. Your behavior reflects not only on yourself but also on your parents, your family, and your school.

AUTUMN: (Pg 30) A set of doors to my left opens. blond locks under a black knit cap. That’s the first thing I notice—the unruly hair that frames a too-familiar face. [NOTE: Attributed to another student, Sylv, in the novel] (Pg 42) Tyler. My brother.

AUTUMN: (Pg 35) The stage is a mess of people congregating around Principal Trenton—Mr. Jameson, everyone’s favorite English teacher, tries to stem the blood flow, except she’s hit in the head, and it’s not blood but brains. [NOTE: Attributed to another student, Sylv, in the novel]

TYLER: (Pg 60) I have no issue with most of you, so I’d rather you don’t force me to waste my bullets.

AUTUMN: (Pg 34) The room is swept up in panic. Screams echo in my ears. Teachers standing near the doors try to approach Tyler, but he picks them off methodically, like everyone who gets too close. (Pg 37) I hear gasps and cries and screams. There’s death, there’s dying, and there’s blood everywhere. [NOTE: Attributed to another student, Sylv, in the novel]

TYLER: (he struts to the stage) (Pg 71-72) I liked it here once. Opportunity High. Opportunity. It sounds so hopeful. I wanted to fit in here. Instead, I lost everything. All of you with your perfect lives. Do you know what losing feels like? Do you care?

AUTUMN: (Pg 57-58) Fear and survival are two sides of the same coin. Dad taught me that. These last two years, he proved it again and again and again. Terror is our strongest force because we’re only afraid when we have something to lose. (Pg 73) I don’t know what Ty wants, but if they try to stop him, this’ll only get worse.

TYLER: If you cooperate, some of you might go home today. All you have to do is listen carefully. No screaming, no running, no phones. Today, you’ll all listen.

AUTUMN: (Pg 42) My brother, who cared for my bruises when Dad couldn’t contain his grief. Who helped me dance. Once, he caught Dad’s belt on his bare arm to stop it from coming down on me. Afterward, Tyler cracked a joke and tousled my hair. He is the only real family I have. It can’t be him.

TYLER: (Pg 87-88) (smiling and grandiose) Now then. Good. To survive, you must know who your friends are. You must know who you can trust. And you must know how to stop caring.

AUTUMN: His smile was just like Dad’s—cold. A couple nights ago, Ty stood by while Dad showed me that the love he once had for dance, for me, died along with Mom. Yesterday, Ty laughed through his tears. When he tended my bruises, he told me there was nothing that made him happier than to see me dance. It reminded him of when Mom was alive and we’d go see her performances. He said that even though he’d never felt the extremes of Dad’s anger, he’d already lost so much. We both had. I wanted to believe him. He’s my brother.

TYLER: (Pg 89) Lesson one: don’t get attached and you won’t get hurt. (He fires)

AUTUMN: Without a second glance, without so much as a blink, he pulls the trigger and shoots Mr. Jameson.

TYLER: (Pg 102) Do you know what it feels like to lose everything you hold dear? Your family? Your girlfriend? For your entire town to turn against you too? I’m reclaiming Opportunity. Your lives are mine. And you will pay attention. (tapping the barrel of the gun against his chin he speaks softly while pacing back and forth) (Pg 104) I thought my family at least cared about me. But you corrupted them. You left nothing for me (beat) Wouldn’t you agree, Autumn? (silence) (Pg 107) (in a singsong voice) Would it help if I gave you an incentive to make the right decision?

AUTUMN: He jumps off the stage and paces in front of the students like he’s deciding who to pick for his basketball team in PE. (Pg 109-110) He leans over and drags a girl by her baseball jersey over the row of seats. She’s young—a sophomore maybe. Too young to die. The auditorium may be big enough to hold a thousand students, but it’s too small to hide just one.

TYLER: (Pg 113-114) (he calls out) It’s easy, Autumn. Come out or I’ll pick off the entire school. (gunshots punctuate each word) Just. Like. This.

AUTUMN: (to audience) (Pg 124-125) Every time I blink, I see Nyah’s face being torn apart by a bullet. If anyone can get through to him, it’s me. I have to try . . . (to Tyler) Tyler. (clears her throat and speaks louder) Tyler. I’m here. (to audience) (Pg 136) I’m staring at a stranger. This is not the same person who showed me the abandoned shed where I could dance in secret. This isn’t the same person who bought me pointe shoes. He may look and sound like Tyler, but this is not the same person.

TYLER: (Pg 134) (sarcastically) Do you expect me to shout at you from across the room? Did your mother not raise you better than that?

AUTUMN: (Pg 136) When I reach the stage, the full horror hits me. The bodies of half a dozen teachers lie up there. (to Tyler) Why, Tyler?

TYLER: (Pg 137) (grabbing a fistful of Autumn’s hair and pulling her on stage – his gaze devoid of humanity) You think you are so special, don’t you? Do you even care about anyone anymore? Or do you only care about yourself? (He holds the gun to her face)

AUTUMN: Please don’t. (whispers) I love you. (Pg 146-147) You’re my brother. You’re my best friend. You’re everything to me. What happened to us, Ty? I lost as much as you did. But you made me believe fulfilling Mom’s dream—my dream—was still possible.

TYLER: (blinks) Believe in your dream?

AUTUMN: To get out of here.

TYLER: (begins to laugh, louder and louder) I wanted to be your excuse to stay home. But you pushed me away. (Pg 148) You told me there was nothing keeping you here. Not even me. (the laughing turns to sobbing) It’s your fault. (gestures grandly) All of this, is your fault. (he fires again into the crowd)

AUTUMN: (Pg 153) I know it’s my fault. (softly) Not a day goes by when I don’t miss Mom. I wish I could go back and redo that day. But I can’t. I can’t. I can only keep doing what she wanted me to do, and she wanted me to dance, Ty.

TYLER: (Pg 161) (seething) I hate you. You never cared about me. You never cared about any of us. You only ever cared about dance.

AUTUMN: (wincing) I want to contradict him, but I can’t. Dance is beauty. Dance is compassion, honesty. The only way I’ve ever known how to share my feelings is through dance.

TYLER: (points the gun again at Autumn) So dance. You wanted a stage? Take it!

AUTUMN: (assumes 5th position and begins to dance with trembling hands and tears pouring down her face) (to the audience) (Pg 175) They say your life flashes in front of your eyes right before you die. As I wait for Ty to pull the trigger, no memories overtake me. No last wishes or if-onlys. (she can’t dance anymore, and crumples) When Dad was at his worst, he’d call me every name he could think of and wouldn’t stop until he felt like he’d won. Ty is worse. His eyes are wild and unrecognizable.

TYLER: (shaking his head) I thought you understood the loneliness and the loss. I thought that was why you wanted to get out—to fight back. To win. (facing the auditorium, he punctuates each word with a gunshot) (Pg 182) I. Will. Not. Let. You. Go.

AUTUMN: (grabbing his arm, she steps between him and the students in the auditorium) (Pg 260) You won’t kill me. We’re family. That must count for something. (he brushes Autumn aside roughly, takes aim and fires at her) (Autumn drops to the ground -- long beat) (to audience) (Pg 270) When Ty pointed the gun at me, he broke me. I didn’t need to die for him to kill me. He simply lowered his gun and pulled the trigger. And his bullet tore my knee to shreds.

TYLER: (with a complete lack of emotion) (Pg 260) Our family was everything to me once. (he puts the gun to his own temple) I just don’t want to be alone anymore . . . (he fires) (long beat)

AUTUMN: (to audience – she composes herself and speaks slowly) (Pg 280) We are not better because we survived. We are not brighter or more deserving. We are not stronger. But we are here. We are here, and this day will never leave us. [NOTE: Attributed to another student, Fareed, in the novel]
```

---

## IC-2340: The Throne of Fire

- Title: The Throne of Fire
- Author (byline): Rick Riordan
- Work: Cutting is from (Chapter 8)
- Publisher: Disney Hyperion
- Publication date as stated: Aug 2012
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: BES, SADIE, LIZ, NEKHBET
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
* Cutting compliments of Heidi Trevithic of Denver,
Colorado
```

### Introduction (context only: never use it for content warnings)

```text
Of course Sadie had seen stranger things . . . that tends to happen when you are one of the most powerful descendants of the ancient Egyptian pharaohs to be born in centuries!

Sadie is on a mission to revive the sun god Ra who can stop the god of Chaos and his minions from rising and destroying the world. (Where was she when we needed her in the years leading up to the 2016 Presidential Election?)

In this selection, Sadie finds an ally in Bes, the dwarf god

(Think Tirian Lannister from Game of Thrones), who helps her defeat two of Chaos’ minions: Nekhbet, the Vulture Goddess, and Babi, a blood-thirsty god of the underworld.

Will Sadie and Bes prevail or will Chaos reign? Throne of Fire by Rick Riordan.
```

### Performance text (classify this)

```text
*NOTE: Sadie and Liz should have pronounced British accents Nekhbet appears as a woman that is a hundred years old. The skin around her face, neck, and earlobes sag and her body is hunched over and emaciated. She is almost bald, with just a few clumps of greasy black hair on her head. She wears a "lush" black dress made entirely of feathers

I’d never been in a limousine before. I hope most are nicer than the one we took. The backseat was littered with take-away curry containers, old fish-and-chip paper, crisps bags, and various dirty socks. Despite this, Liz and I crammed together in the back, because neither of us dared ride up front. You may think I was mad to get in a car with a strange man. You’re right, of course. But the gods had promised us help and a driver. The fact that our promised help was a little man with bad hygiene and a magical limousine did not particularly surprise me. I’d seen stranger things.

He was shorter than me by half, and uglier than anyone else on the planet. His facial features were positively Neanderthal. Under his thick furry mono-brow, one eye was bigger than the other. His beard looked as if it had been used to scrape greasy pots. His skin was poxy with red welts, and his hair looked like a bird’s nest that had been set on fire then stomped out.

When he saw me, he scowled, which did nothing to help his appearance.

BES: About time! (American accent, belching into his fist). Sadie Kane?

SADIE: Um . . . possibly. By the way, we have two gods trying to kill us.

BES: (Turning toward the curb and yelling,) BOO!

SADIE: (To Audience) A black Mercedes limousine appeared out of nowhere, as if it had been scared into existence.

BES: (Glancing at Sadie and arching his brow.) Well? Get in!

The chauffeur started whistling a tune that sounded like “Short People.” His head barely reached the headrest. All I could see of him was a grubby nest of hair and a set of furry hands on the wheel. Stuck in the sun visor was an identification card with his picture – sort of. It had been taken at point-blank range, showing only an out-of-focus nose and a hideous mouth, as if he’d been trying to eat the camera.

The card read: Your Driver is BES. (To Bes) You’re Bes, I guess?

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

He spun the car to a stop in the middle of the bridge. Looking behind us, I almost lost the contents of my stomach. A winged black shape was circling over the riverbank. At the end of the bridge, Babi was taking care of the barricade in his own fashion. He was throwing police cars into the River Thames while the officers scattered and fired their weapons, though the bullets seemed to have no effect on the baboon god’s steely fur. (to Liz) Liz, we’re getting out.

LIZ: (whimpering) Getting. . . out?

BES: (stifling a yawn.) Need my help?

SADIE: Um . . . (To audience) Babi was lumbering towards us. Nekhbet circled over him, shrieking orders. I didn’t see how a dwarf god could stand against those two, but, (To Bes) Yes, I need help.

BES: Right. (cracking his knuckles.) So get out.

SADIE: What?

BES: I can’t change clothes with you in the car, can I? I have to put on my ugly outfit.

SADIE: Ugly outfit?

BES: Go! I’ll be out in a minute.

It didn’t take much encouragement. Neither of us wanted to see any more of Bes than we had to. We got out, and Bes locked the doors behind us. The windows were heavily tinted, so I couldn’t see in. For all I knew Bes would be relaxing, listening to music while we got slaughtered. I certainly didn’t have much hope that a wardrobe change was going to defeat Nekhbet and Babi. (To Liz and Bes) We’ll make our last stand here.

LIZ: Oh, no, no. I really don’t like the term “last stand.”

SADIE: (To Audience) Nekhbet must’ve seen the desperation in my face. She was a vulture. She specialized in knowing when her prey was finished.

NEKHBET: A good last effort child, but you have nothing left. Babi, attack!

SADIE: (To Audience) The baboon god reared up on his back legs. I got ready to charge and deliver one final burst of energy – to tap into my own life source and hopefully vaporize the gods. Then the limo’s door opened behind me.

BES: No one is attacking anyone! Except me, of course.

SADIE: (To Audience) Nekhbet shrieked in alarm. I turned to see what was going on. Immediately, I wished I could burn my eyes out of my head.

LIZ: (making a gagging sound.) Lord, no! That’s wrong! Make him stop!

Bes had indeed put on his ugly outfit. He climbed onto the roof of the limo and stood there, legs planted, arms akimbo, like Superman – except with only the underwear. For those faint of heart, I won’t go into great detail, but Bes, all of a meter tall, was showing off his disgusting physique – his potbelly, hairy limbs, awful feet, gross flabby bits – and wearing only a blue Speedo. Imagine the worst looking person you’ve ever seen on a public beach – the person for whom swimwear should be illegal. Bes looked worse than that. (To Bes) Put on some clothes!

BES: (laughing loudly in a sort of guffaw that says “Ha-ha! I’m amazing!”) Not until they leave. Or I’ll be forced to scare them away.

NEKHBET: This is not your affair, dwarf god! (snarling and averting her eyes from his hideousness.) Go away!

BES: These children are under my protection.

SADIE: I don’t know you! I never met you before today.

BES: Nonsense. You expressly asked for my protection.

SADIE: I didn’t ask for the Speedo Patrol!

Bes leaped off the limo and landed in front of me, placing himself between Babi and me. The dwarf was even more horrible from behind. His back was so hairy it looked like a mink coat. And on the back of his Speedo was printed DWARF PRIDE. Bes and Babi circled each other like wrestlers. The baboon god swiped at Bes, but the dwarf was agile. He scrambled up Babi’s chest and head-butted him in the nose. Babi staggered backward as the dwarf continued pounding away, using his face as a deadly weapon. Babi slumped against the railing. He blinked, trying to regain his bearings, but Bes breathed on him, and the smell of curry must’ve been too much. The baboon’s knees buckled. His body shimmered and began to shrink. Then Bes turned toward the vulture goddess.

BES: Now it’s your turn, Nekhbet. Leave.

NEKHBET: I stole this body fair and square! (wailing) I like it in here!

BES: You asked for it.

Bes rubbed his hands, took a deep breath, and did something I will never be able to erase from my memory. If I simply said he made a face and yelled BOO, that would be technically correct, but it wouldn’t begin to convey the horror. His head swelled. His jaw unhinged until his mouth was four times too big. His eyes bulged like grapefruits. His hair stuck straight up. He shook his face and waggled his slimy green tongue and roared BOOOO! so loudly, the sound rolled across the Thames like a cannon shot. This blast of pure ugly blew the feathers off Nekhbet’s cloak and drained all the color from her face. It ripped away the essence of the goddess like tissue paper in a storm. The dwarf’s face went back to normal – well, normal ugly, at least – (To Bes) Thank you. Now, will you please put on some clothes? (To Audience) He gave me a toothy grin, which I could have lived without.

BES: You’re all right, Sadie Kane.
```

---

## IC-2341: Through a Window

- Title: Through a Window
- Author (byline): Angela Johnson
- Work: On the Fringe
- Publisher: Penguin Group
- Publication date as stated: March 2003
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1729
- Already set (do not supply): none

### Source block (context only)

```text
Author: Angela Johnson
Book: On the Fringe
ISBN: 978-0142500262
Publisher: Penguin Group
Date (Month/Year): March 2003
```

### Introduction (context only: never use it for content warnings)

```text
Sometimes we think we know someone because we see him or her almost every day. Then something happens to make us realize we didn’t know that person at all. The death of a best friend is different than the death of a parent or spouse; there are no sympathy cards that quite fit the bill. There's no term for this loss and folks expect an abbreviated mourning period and offer a different, lighter brand of sympathy. It’s almost like you are living your life as a spectator . . . just watching . . . Through a Window by Angela Johnson
```

### Performance text (classify this)

```text
I don’t believe in God. Not right now. Not at this minute. But . . . When they cut Nick Gorden down from the upper stairwell outside the chem lab, a storm had just come up over the lake. You know the kind: lightning, rain, and wind that rips the roofs off buildings.

They were gentle when they took Nick away. The paramedics put him on the stretcher like he was a baby. I didn’t see the rest, the cops and all. I only watched through a second-floor window as they took my best friend away from me and here and this place . . . forever . . .

I tell my therapist that there had to be a storm the day Nick died. Something cataclysmic and ugly had to happen. If the sun had been shining, afterward maybe I would have cried and thought about how Nick just missed a day at the park. But as it happened, nature stepped in again. Somebody had to cry for Nick. The sky and his mother did that day. My eyes stayed dry.

It’s all about Nick. All of it. The therapy, the dreams, the way I can’t cry . . . Nick’s favorite song was the old Sly & the Family Stone tune called "Everybody Is a Star." He sang it all the time. (sing lines from the song here – See links to song and lyrics at the end of this selection) Wrote and tagged buildings everywhere with it, but in the end he didn’t believe it, I guess. It was the song Nick’s uncle was singing right before he died in Vietnam. Nick’s mom got all her brother’s belongings - clothes, records, dog tags - from one of the guys in his platoon.

It used to drive me crazy listening to those old records with scratches and jumps in them, but Nick said the scratches were in his head - he knew every one of them and they were like old friends. I never told Nick those records bothered me. Now I wished I had, ‘cause at least it would have been one more conversation we had had.

I used to be envious of Nick, ‘cause he was the person that everybody said hello to in the halls. He always smiled and seemed to sail along halls that had nothing but fear in them (to me, at least). In class pictures he always smiled. In his family pictures he always smiled. I overheard his mom on the phone once call him sweet and good-natured.

But I found out something about Nick a week before he died that got me all turned around, and I’d known Nick since first grade. We had been each other’s one and only friend since he’d followed me under the monkey bars after I stolen Josh Neil’s lunch. Nick had crawled under and sat behind me while I munched. He stared at me until I gave him a Fruit Roll-Up to go away. He ate it, kept staring, and stayed.

The next day the same thing, only this time I’d taken pudding out of Heather Longchamp’s backpack ‘cause she’d sat on me in front of the whole first grade. Plus she always had butterscotch. We finally got caught a week later. My mom dragged me out of the office mumbling that I was already a criminal.

Nick told the principal he’d taken the lunches and I said I’d taken them. Okay, we were tight; so why didn’t I understand that even though Nick was somebody people smiled at and waved to, nobody knew anything about him? Sometimes they couldn’t even remember his name. Nick said it. He was the invisible man.

The week before they took him out on a stretcher with his face covered, Mr. Miles (in civics class) couldn’t remember his name or that he had even been in that class. I think Nick could have taken that if Heather (no longer eating pudding--- a definite anorexic) hadn’t started laughing that he’d been going to school for years and nobody ever knew his name.

I wanted to hit her. Break those skinny, skinny cheerleader arms and that big-toothed smile she only used to torture people. Everybody laughed but me and Mr. Miles, who just looked confused and a little sorry he’d opened his mouth. Nick was even laughing. I spent the rest of the day with a stomachache, not able to look Nick in the eye. Later that night he laughed that invisible people had to have a sense of humor. I didn’t think that was funny.

I wasn’t invisible myself. I was just visible enough to be let out of conversation purposely - just visible enough to be picked on for my bad skin, nonexistent fashion sense, and biggest crime of all: I was smarter than anyone in my class and I had the nerve to be female. (Long beat)

I went over to Nick’s house after the police and [everyone] had gone back to their lives. At first I was going to knock on the door, but then I couldn’t face Miss Gorden. Her eyes would be puffy, her face tired and sad, her body drooping. I climbed into the open hall window on the side of the house. It’s the way me and Nick came in most of the time anyway.

I could hear Miss Gorden crying two rooms down. She sounded like a little kid. I almost started crying too. That would have been a good thing. That would have helped. But instead, I just ducked into Nick’s room.

His baseball and Greenpeace posters jumped out at me and stabbed me in the heart. I used to listen to guys at school talking basketball as Nick’s eyes glowed. I’d think: This time he’s going to say something, talk about what happened in some game somewhere. But he never did, and none of the group ever asked. I curled up on the bed and in a minute was asleep. When I woke up a few hours later, the sun was going down and Miss Gorden must have come in and taken Nick’s favorite blanket off his chair and covered me in it. I put it over my head and inhaled Nick, then crawled out the way I came in and walked the street-lit sidewalks.

At breakfast yesterday my dad said, "Do you want to go to another school?" I bit down hard on my apple without looking at him, then slurped my orange juice so that I couldn’t hear him if he asked me again. He asked again. So I grabbed a piece of toast and hoped it was as loud as the apple had been. He shook his head and looked at my mom, who was looking again for signs that I was so depressed I’d go the way Nick had. Finally, though, they started picking up the breakfast dishes and left me alone. I’d have to get used to alone.

I stood beside Miss Gorden when they put her son in the ground. I fought the urge to scream when the casket was lowered. I should have screamed. There were eight people there: Miss Gorden, my parents and me, the school principal, and three people that I’ve never seen before. Again, I wanted to scream. Nobody from school came. Not one classmate. Not even to get out of those halls from hell. Everyone cried but me.

When the service ended, Miss Gorden turned on the [CD] she’d told me to bring. She sat next to Nick’s grave and smiled as "Everyone Is A Star" echoed through the cemetery. And all I could think as I got into my mom’s minivan was that Nick probably wouldn’t even be mad that the last time he heard his song it was on a CD.

For a week, the halls and classes got quite when I walked through them. It was like I was carrying a plague that would only infect others if they talked around you. They all just stayed away.

The second week, though, it started. The questions: Why? And why there? Did I expect it? Did he talk about it? I would swallow what I wanted to say and never answer. Did they want me to put in a paragraph or less (while looking appropriately sad) how someone I loved more than anyone on the planet had lived his life, then ended it? Especially to people who couldn’t give a damn whether he lived or died before. Had most of the pack creatures ever held a single conversation with Nick? Had any of the ones who ask me "How come?" been in a group who had screamed out "Do it!" as Nick was about to let go of the rafters and swing like a rag doll in front of them? I lasted three days in school.

Nick had been happy his whole life. He’d never had a bad day, I thought. He never seemed miserable or lonely, ‘cause he had me. I thought he never minded that he was invisible. I’d always believed he never wanted to be like them, having basketball conversations and talking about what they did the night before. I guess that I was wrong about it all.

Wrong that he never minded that they thought he was a sad case ‘cause his best friend was a girl with bad skin who couldn’t form a social sentence. Wrong that it didn’t make him sad the person he identified with most was a boy who’d died thirteen years before he was born, fighting a war that shouldn’t have been. At thirteen when Nick found out about reincarnation, he decided his uncle had come back to the world as him. He really believed it. Believed it in his soul. Believed it more than anything he’d ever thought in his whole life, even believed it more than the thing about him being invisible.

[Now] I watch the world through a window of [a] Psychiatric Clinic for Adolescents, and the world only comes in and bothers me when I want it to. I’ve decided that it’s not such a bad thing to be invisible. The thing that you have to be careful of, the thing that Nick never learned, is that you can’t want to be anything else. You can’t want to have more people who care. You have to be invisible on your own all by yourself. You can’t even have a friend like me who loves you and thinks you’re better than anything else.

(sing lines from “Everybody is a Star” here – See links to song and lyrics at the end of this selection)

Nick got it wrong. Everybody isn’t a star. . . maybe in a better world they could be. They could be. They really could be . . .
```

---

## IC-2342: The Truth About Dino Girl

- Title: The Truth About Dino Girl
- Author (byline): Barry Lyga
- Work: Geektastic: Stories from the Nerd Herd
- Publisher: Little, Brown Books for Young Readers
- Publication date as stated: June 2010
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: SOOZ, KATIE, BOY, ANDI, JAMIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1991
- Already set (do not supply): none

### Source block (context only)

```text
Author: Barry Lyga
Book: Geektastic: Stories from the Nerd Herd
ISBN: 978-0316008105
Publisher: Little, Brown Books for Young Readers
Date (Month/Year): June 2010
```

### Introduction (context only: never use it for content warnings)

```text
The Truth About Dino Girl by Barry Lyga
```

### Performance text (classify this)

```text
When I was a kid, I had a picture book about T. rex. There was an illustration of a bunch of them ganging up on a lizard.,They weren't biting it or slashing at it or even touching it. They just surrounded the poor thing. And the lizard had...It had this look on its face. This long-suffering look of Here we go again. I knew how that lizard felt. And I hated that. [It] made me think that maybe...Maybe I was a lizard. I didn't want to be a lizard. I wanted to be a dinosaur. Predator and prey. Prey and predator. Sigh.

There were certain things I knew for sure. I knew that the dinosaurs lived from 65 million to 230 million years ago. I knew that the theropods were the only dinosaurs to survive the entire Age of Dinosaurs-- first on the scene, last to die off. I knew that they shook the earth when they walked. I also knew that I was in love with Jamie Terravozza. He was a junior and on the baseball team, while I was a mere freshman, and a geek. I remember the moment when I fell in love. One day Mrs. Knight asked us why animals never evolve with three limbs instead of four or two or six or eight. I raised my hand. I was the only one. I said, "Bilateral symmetry." Zik Lorenz chuckled and said, "What's this about bisexual?" Everyone laughed but me. And then I noticed Jamie. He wasn't laughing. He just rolled his eyes, flashed me a grin, then scribbled something on his notebook and slid it to the edge of his desk so that I could see it: IGNORE HIM. HE'S AN IDIOT. I loved him for that [and the] tattoo of a flaming baseball on his left arm. My bio notebook was filled with pages of me drawing that tattoo over and over again. The problem, of course, was that he had a girlfriend: Andi Donnelly. A junior. Captain of the girls' soccer team. Drop-dead gorgeous in all the ways boys like.

SOOZ: Ugh, Don't you just hate her?

KATIE: No. I just want to be her. And it was true. If I could be Andi, I would be the world's greatest Andi. She was perfect. And, of course, she had Jamie. ********* In kindergarten, when they asked what we wanted to be when we grew up, I said paleontologist. [In] first grade, a boy accosted me on the playground while I was sitting off to one side, reading a dinosaur book.

BOY: You're not really a girl. Girls don't like dinosaurs.

KATIE: What do you mean? Of course I'm a girl. I'm wearing pink. I pointed to my headband, just in case he didn't get it. Eighth grade--just last year-- I didn't care that the other girls were getting into makeup and boys. I didn't care that boys didn't think I was a girl. I didn't care about any of it. I just wanted a dinosaur nicknamed Katie [after me]. That was all I wanted.

Until high school started. Until Jamie. Suddenly, I wanted something else. And I had no idea how to get it.

SOOZ: I don't get how you can like Andi. She's so mean. She once made so much fun of another girl that she went into the bathroom and cried for, like, an hour

KATIE: Jamie likes her, so there must be something to her, right? I just couldn't find it in me to hate Andi. I figured it had to be difficult to be her. There were all kinds of stresses that came with being Andi, things I couldn't understand because I was not her. She was beautiful and funny and athletic and popular and I was... (shrug) ******** [The next day] On the way to homeroom, I looked around me at the swarm of kids in the hallway. I felt so small in that moment. I was alone. And I felt like that lizard, the one being hounded by the young T. rexes. Just little lizard me, slithering along on my belly and along comes a bunch of big, bad dinosaurs and they're going to take their time to eat me. They're in no hurry. You know why? Because I'm just a little lizard. I'm nothing. Less than nothing. Why couldn't I figure out the qualities in Andi that attracted Jamie? Why couldn't I mimic them, improve on them? I was smart. This was one more science problem, a biology test set in real life. Maybe that's crazy. But I couldn't help myself. I was desperate. But it didn't matter. Because one day it all became impossible. That day was the worst day of my life. My own personal extinction-level event, right in the halls of high school. I was leaving gym, following close to Andi. I did that whenever I could. Watching her. Listening. Trying to learn. Doing my research, like a good scientist. But then, suddenly, Andi turned around, as if she'd forgotten something. Maybe she had. I don't know. All I know is this: The worst thing that could possibly happen, happened. She bumped into me. Hard.

I dropped everything I was holding. Including my bio notebook. Which landed spread open. The reproductions of Jamie's tattoo. That tattoo. Over and over and over again. I prayed that Andi wouldn't notice it. But her eyes dipped down. Before she could say anything, I started babbling. I just couldn't stop myself. I was terrified and embarrassed and strangely giddy all at once.

KATIE: Please don't say anything. Andi. Please. Please. It's nothing. It doesn't mean...I would never try to take him away from you, really. Her eyes got wide and then she laughed. She laughed.

ANDI: Are you serious? Do you think I'm afraid of that? He doesn't [care] about you. He needs you following him around like he needs a hole in his head.

KATIE: "Actually, um, that can be useful." Oh my God! What on earth? Where was that coming from?

KATIE: The theropods had holes in their skulls to make their heads more lightweight.

Shut up, Katie! I begged myself. Shut up! But I couldn't stop myself. I was on autopilot.

KATIE: It's something of an evolutionary advantage for a large predator to have at least one hole in its head, as a way of reducing drag when?--

ANDI: Hey! Her eyes scrunched and her brows came together and her mouth twisted into a scowl. Andi was suddenly the one thing I never thought she could be--ugly. It shocked me into silence.

ANDI: Shut your little prissy, geeky mouth and listen to me, okay? Look, Dino Girl. There's, like, a natural order to things, okay? Girls like you do not get to go with guys like Jamie, okay? Especially when the guy is already with a girl like me. Did that get through your little lizard head? Dinosaurs aren't lizards! I wanted to shout. But I said-- --nothing. I just stood there, pinned, frozen by her anger. I thought about that lizard in the picture book. Wouldn't it shock those T. rexes if it suddenly stood on up on its hind legs and roared and bit one of their heads off? Impossible, of course. A physiological impossibility. But I wasn't a lizard. I was a human being. I managed to scoop up my stuff and make it to the girls' bathroom before I burst into tears. Why did she have to be so mean? Why? All I wanted was for a boy to like me. She was mean. Yes. But the worst part was that she was honest. Like she said, [Jamie] wouldn't like me. I was just a geeky girl who knew too much about dinosaurs. She could have just walked away from me. That's the thing: She could have been kind. Why was she so mean? Just because she was a dinosaur? Just because she was a dinosaur and I was a lizard, predator and prey, and she could? She could. That's what it came down to: She could do whatever she wanted just because she was Andi Donnelly, and there was nothing I could do about it. And then... It hit me. Like a comet. It hit me: The dinosaurs were more powerful, but the lizards survived. Look around. They still exist. They used to be prey, but they lived. Some of them are even predators now. It's scientifically, biologically impossible for a lizard to evolve into a dinosaur. But prey can become a predator. It happens all the time. All the time. ************

SOOZ: Well, what are you going to do about her? Sooz asked when I finally told her everything. I couldn't believe it when I heard the words come out of my mouth:

KATIE: "I'm going to destroy her." Maybe it was insane to take on Andi. She was bigger than me. She was more popular, more important. But here's something every good paleontologist knows: Even the biggest die. Even the meanest get killed off by something that they can't see coming. Like a meteor. Or an insect. What it comes down to is this: In this world, you're either predator or you're prey.

I had to wait for soccer season. I had to wait for Andi to be in practice pretty much every day of the week. So I waited. And waited. On one of my gym days, I "accidentally" left my math book in the locker room after changing. I begged Mom to take me back to school for it. We got there just as practice was ending. No one noticed my new little credit card-size camera. That's because I hid it in an empty blush compact, with a hole drilled through for the lens. So I could hold it up and look like I was just looking in the mirror, but I was actually snapping pictures. Sooz took the best one and massaged it in Photoshop. I looked at the screen over her shoulder.

KATIE: It's perfect. It's beyond perfect.

SOOZ: (grinning) How many should we print out? To have it all come out the next day would be too suspicious. Someone would remember me in the locker room. So I waited. Again, lying in ambush. I've already pegged the prey--it just doesn't know it yet. After two weeks, I pounced. Brookdale awakened to a new poster on its telephone poles and newspaper boxes and bulletin boards. The image Sooz had mocked up. Andi, half-naked from the shower in the locker room, drying her hip and leg, her torso completely revealed. Wet and gorgeous and totally unaware.

Sooz gave it atmosphere and mood. She Photoshopped out the locker room and Photoshopped in a sleazy hotel room we'd found online. And at the top:: CALL ANDI! with her phone number and her address. The first time I saw Andi that day, she was in tears. She was alone, rushing to the bathroom. It was the talk of the school. I heard all sorts of rumors: It was an ex trying to get back at her. It wasn't really her. (Then why did it look like her? Why was her phone number on it?)

JAMIE: If it's not real, how did they get a naked picture of you? What could she say to that? With the locker room Photoshopped out, how could she know where that picture had come from? According to the grapevine, Andi had broken down into tears again at that. I wished, oh, I wished I had been there to see it! I watched at lunch instead. I watched as Andi sat down at her table. Jamie didn't sit with her. In fact, no one sat with Andi.

Sooz flashed me the biggest smile I've ever seen. I resisted the urge to high-five her. Too incriminating. But when I got up from the table, something amazing happened. The earth shook with my footsteps. It shook. From now on, the earth would tremble in my wake. And I knew. I knew what the dinosaurs sounded like.

They sounded like me....
```

---

## IC-2343: Two Days

- Title: Two Days
- Author (byline): Aimee Bender
- Work: Not specified
- Publisher: Random House
- Publication date as stated: Aug 2006
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1607
- Already set (do not supply): none

### Source block (context only)

```text
Author: Aimee Bender
BOOK: This is Not Chick Lit
ISBN: 978-0812975673
Publisher: Random House
Date (Month/Year): Aug 2006
```

### Introduction (context only: never use it for content warnings)

```text
As a kid, I used to believe that my opinions would never change. But as we grow older our perspectives change – perspectives about life, other people and even ourselves. Now that I’m older, I believe they’ll never stop changing. Fears are diminished to be replaced by new concerns, people enter and leave our circle of importance and how we feel about ourselves are continually morphing into new perceptions. I believe that’s what growing up is all about – it’s all just a matter of perspective that can change over the years or in as little as Two Days by Aimee Bender.
```

### Performance text (classify this)

```text
I met Adam at the bookstore. He was in the section marked Biography/History, and he was looking at a book about some historical event no one’s ever heard of. The only way I knew it was a historical event was because the cover was in black and white and had a photo on it of a tank.

I myself was aiming for art books, because my friend Terrie had just had a life-changing experience from looking at a photograph of a clown. She’d spent her childhood terrified of clowns, but when she saw this photo, she experienced a 180- degree shift – one of those rare moments when the other side become clear as anything and we can no longer understand why it was so hard to get before.

“Clowns are desperate,” she’d told me, with wonder in her voice. “That’s why they’re so scary.”

It hadn’t occurred to me either, and I wanted to see if she was right. I too had had the experience of a childhood clown doll that one day had transformed from delightful toy-friend into the diabolical engineer of my nightmares. Someone bought it for seventy-five cents – some kid too young to feel the fear yet – and I threw the cursed coins into the outdoor trash, observing as the other neighborhood kids spotted and retrieved them. Let them spend it, I thought, from the safety of my bedroom. It will only bring them grief.

They used the quarters to buy ice cream. Story of my life.

I found the art book Terrie had been talking about and flipped toward the photo of the clown. As I skipped through those shiny pages, pages that smelled like a hair salon, Adam turned and held up the war book. “Do you know this photo?” he asked me, tapping the cover.

“Oh.,” I said. “Is that World War I?”

He shook his head, and his hair was very light brown, almost colorless, and as it shifted, it caught no light.

“Korean War,” he said. He shelved the book. “They told me it was a good read, but I just read a page and it was so dull,” he said, and then he stepped closer. Aside from that colorless hair, he had a wide open face, sort of big-featured, with a big nose and big eyes and teeth. Likeable. The kind of face you could immediately trust, even against better judgment.

I was looking, at a washed-up movie star wearing sequins in some kind of aquarium tank emptied of water. I guess they were trying to work with the phrase “washed up,” but the star didn’t seem aware of that because she was grinning in the tank like it was all funny and fun. Maybe the whole book should’ve been titled Desperation.

“What are you looking at?” he asked, peering over my shoulder.

“Art photos,” I said. I turned the page to have something to do, and there was the clown, with its big nose and scary mouth makeup and scary eyes and red costume. And I could see what she meant, Terri. It was trying so hard. That was part of what was so menacing, was its enormous effort to amuse. You kind of wanted to hurt the clown, before it smothered you.

“Do you think it looks desperate?” I asked him.

He squinted and stared at the photo for at least a minute. “Why do they do the eyes like that?” he said at last. “I mean, the star-shaped thing? Is that clown protocol?”

We ended up at the Greek coffee place next door, and before we left the store, I flipped through the rest of the photo book to see if the others were desperate too, but they weren’t, not in the same way.

Adam got up to get the coffees while I looked out at the cars driving by on Sunset. It was raining a little, and watching the windshield wipers made me feel more settled. The air smelled like city, like damp city. I felt attractive, talking to him. Next to those big features of his, I could feel myself as delicate. When the conversation waned, I sipped from my bitter little Greek coffee and told him that my friend Terrie was having surgery the following day. That she was young, still, but they’d found problematic shapes in her bronchitis X-ray. “Lumpy shapes,” I said, “inside her lungs.”

He stirred his coffee and nodded with appropriate solemnity.

“You know,” I said, “I just lied. That’s not true.”

“About Debby?”

I reached out and touched his arm. “I didn’t know what to say, so I made up Terrie’s lumps. That’s awful of me.”

He leaned in then, and he didn’t kiss me but it was too close for regular. We spent a few minutes there, blinking together, breathing the coffee-scented air. Who knew what would happen? He had that trust-worthy face, a face I didn’t trust, simply because I’d trusted it so swiftly.

We agreed to meet the following afternoon at the beach in Santa Monica. Of course I was early because I’m always early, and I didn’t head over to the water just yet, instead wandering past the snack bar, reading the names of foods listed in black plastic stick-on letters: Chili dog, Onion rings, Popsicle. Words I love to see in black plastic stick-on, words that conveyed summer to me, on this cloudy November afternoon.

I had not been flirted with in many months, and this man had not rejected the reeking desperation of either the clown or the old star, and asking for sympathy about a dying friend was the first tool that appeared from my own personal flirting toolbox. Sometimes my capacity for smallness is surprising, even to myself.

Adam was already at the beach when I walked over, and he had a picnic basket in his hands. He’d set up a blowzy checkered blanket, whose corners picked up with the wind, and when I walked across the sand, bumpy and difficult to traverse, he smiled at me with those wide-open eyes. For a few minutes we chitchatted, and at one point he threw his hands into the air and exclaimed some things, about nothing, really, just showing a sense of spirit. I felt the love, spreading roots in my chest, making it so easy to smile. We settled onto the blanket and he opened a small bottle of champagne and we toasted, and the water waves crashed.. I reached out a hand and touched his colorless hair, and he turned his face to my palm.

He told me he used to be a chef, that he used to won his own restaurant. He told me the name of it, and how he’d gotten a great review last year in the LA Weekly, saying he had a knack for unusual combinations.

“Really?” I said, impressed, and then, after a pause, he said no.

“I mean I’ve always liked to cook. Ever got paid for it. Sorry.” We looked out at the water. It was the second lie, and it was clear, from the tone of his takeback, that he had surprised himself with it. For whatever reason, it seemed we couldn’t help but lie to each other.

He handed me a charred chicken leg, and a bunch of grapes, and refilled my champagne. The seagulls approached. I ate the chicken and grapes, peeling stripes of chicken from the leg, but everything tasted a little off. Not like poison, but just no fulfilling, and Adam was striking me now as very difficult to know.

For dessert, he brought out oatmeal macadamia cookies that he had baked himself, but I would hardly eat them, my mouth felt so dry, and without thinking, I threw a few sprinkles to the seagulls, who stepped closer on their webbed feet. Adam and I walked to the water and held hands and touched our bare toes to the foam. I felt like crying, then, with those seagulls invading our perfect picnic behind us, eating the cookies and the chicken, stepping all over the napkins, cackling, shoving each other out of the way.

I touched his arm again, and my eyes filled with tears.

“I know,” he said. “It isn’t right.”

When we finally kissed, it was clear that it was our last. His lips pressed gently against mine. I felt that kind of wrenching in my heart, and as I turned and walked the other way,

A flock of seagulls. As a child, I’d found them so wonderful, seabirds, with their curving yellow-orange beaks and funny strut. They lived at the ocean, and anything that lived at the ocean I felt I could love forever. But they turned, in my mind. Sometime around adolescence, after hitting the critical mass of beach picnics, after seeing them come over again and again, pushing each other out of the way, squawking so loud, eating chicken and turkey sandwiches without pause, I found them repulsive.

At the snack bar I ordered a basket of onion rings and sat on the green-painted ocean bench, watching the water. The clouds were thick, and the water took on a metallic gray sheen that settled my mind. I have always like onion rings. They were the thickly cut kind, each ring the width of a wide plastic bracelet, dipped in golden brown crumbs. I ate almost the whole basket, licking the bits off my fingers, and when I was done, I threw the remaining few to the trio of waiting seagulls, who after all, were only hungry. Opinions change.
```

---

## IC-2344: Voices from Chernobyl

- Title: Voices from Chernobyl
- Author (byline): Svetlana Alexievich
- Work: Not specified
- Publisher: Dalkey Archive Press
- Publication date as stated: April 2005
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: LYUDMILLA, DOCTOR, NADEZHDA, LARISA Z
- Teaser before the introduction: Yes
- Spoken words (computed): 1724
- Already set (do not supply): none

### Source block (context only)

```text
Author: Svetlana Alexievich
ISBN: 978-1564784018
Publisher: Dalkey Archive Press
Date (Month/Year): April 2005
```

### Introduction (context only: never use it for content warnings)

```text
April 26, 1986 -- fourteen days after the worst nuclear accident in history, Lyudmilla Ignatenka lost her husband. Reactor #4 at the Chernobyl Nuclear Power Plant in what is now northern Ukraine exploded and burned. Scientists estimate the zone around the former plant will not be habitable for up to 20,000 years.

According to the official, internationally recognized death toll, just 31 people died as an immediate result of Chernobyl, these were the first responders. But over 600,000 people suffered from radiation poisoning that continues to impact generation after generation. Imagine being a mother and knowing that your children or future children are at risk.

Voices from Cherynobyl collected from interviews by Svetlana Alexievich in 1996.

Nadezhda Petrovna Vygovskaya -- mother
```

### Performance text (classify this)

```text
Lyudmilla -- wife of fireman, Vasily Ignatenko

LYUDMILLA: (Pg 5-6) We lived in the dormitory of the fire station where he worked. One night I heard a noise. I looked out the window. Everything was radiant. The whole sky. “Close the window and go back to sleep,” he said. “There’s a fire at the reactor. I’ll be back soon.”

They went off just as they were, in their shirt sleeves. No one told them. They had been called for a fire, that was it. Four o’clock. Five. Six. Seven o’clock. I was told he was in the hospital. The police had already encircled it, shouting “The ambulances are radioactive, stay away!”

[When] I saw him. He was all swollen and puffed up. You could barely see his eyes. Many of the doctors and nurses in that hospital would get sick themselves and die. But we didn’t know that then. (Pg 7) The doctors kept telling us they’d been poisoned by gas. Not one said anything about radiation. No one talked bout the radiation.

DOCTOR: (Pg 9) All right, listen: his central nervous system is completely compromised. And if you start crying, I’ll kick you out. No hugging or kissing. Don’t even get near him.

LYUDMILLA: (Pg 12) It was a hospital for people with serious radiation poisoning. For fourteen days . . (Pg 11) Will they live? Live. (Pg 12) In fourteen days, a person dies. [She is silent] (Pg 11-12) He started to change – every day I met a brand-new person. The burns started to come to the surface. At first there were little lesions, and then they grew. I came off in layers – as white film . . . the color of his face . . . his body . . . blue . . . red . . . gray-brown. The only thing that saved me was it happened so fast; there wasn’t any time to think, there wasn’t any time to cry.

(Pg 17) They photographed him. Naked. One thin sheet on top of him. I changed that sheet every day, and every evening it was covered in blood. I pick him up, and there are pieces of his skin on my hand. They photographed him. For science, they said.

NADEZHDA: (Pg 155-157) It happened late Friday night. My husband says, "There's some sort of fire at the nuclear plant. They're saying we are not to turn off the radio." I forgot to say that we lived in Pripyat, near the reactor. I can still see the bright-crimson glow. [But] this wasn't any ordinary fire, it was shining. It was pretty.

That evening everyone spilled out onto their balconies. We were on the ninth floor, so we had a great view.

People brought their kids out, picked them up, said, "Look! Remember!" And the people who worked at the reactor. . . They stood in the black dust, talking, breathing, wondering at it.

People came from all around on their cars and their bikes to have a look. We didn't know that death could be so beautiful. My throat tickled, and tears came to my eyes.

In the morning I woke up and I remember feeling something isn't right, something has changed forever. At eight there were already military people on the streets in gas masks. When we saw them on the streets, we didn't grow frightened -- on the contrary, it calmed us down. Since the army has come to our aid, everything will be fine. We didn't understand then that the peaceful atom could kill, that man is helpless before the laws of physics.

All day on the radio they were telling people to prepare for an evacuation. We settled in Mogilev and our son started school, he came back the very first day in tears. They put him next to a girl who said she didn't want to sit with him, he was radioactive. Our son was in the fourth grade, and he was the only one from Chernobyl in the class. The other kids were afraid of him, they called him "Shiny." His childhood had ended so early.

Larisa Z -- mother

LARISA Z: (Pg 85-88) My little daughter-she's different. She's not like the others. When she was born, she wasn't a baby, she was a little sack, sewed up everywhere, not a single opening, just the eyes. The medical card says: "Girl, born with multiple complex pathologies: aplasia of the anus, aplasia of the vagina, aplasia of the left kidney." That's how it sounds in medical talk, but more simply: no pee-pee, no butt, one kidney.

On the second day I watched her get operated on, on the second day of her life. She opened her eyes and smiled, and I thought that she was about to start crying. But, God, she smiled! The ones like her don't live, they die right away. But she didn't die, because I loved her.

In four years she's had four operations. She's the only child in Belarus to have survived being born with such complex pathologies. I love her so much. [Stops] I won't be able to give birth again. I wouldn't dare. I came back from the maternity ward, my husband would start kissing me, [and] I would lie there and tremble: we can't, it's a sin, I'm scared. I heard the doctors talking: "That girl was born in a suit of armor. If we showed it on television not a single mother would give birth." That was about our daughter. How are we supposed to love each other after that?

I went to church and told the minister. He said I needed to pray for my sins. But no one in my family has ever killed anyone. What am I guilty of? First they wanted to evacuate our village, and then they crossed it off their lists -- the government didn't have enough money. And right around then I fell in love. I got married. I didn't know that we weren't allowed to love here. Many years ago, my grandmother read in the Bible that there will be a time when everything is thriving, everything blossoming and fruitful, and there will be many fish in the rivers and animals in the forest, but man won't be able to use any of it. And he won't be able to propagate himself in his likeness, to continue his line. I listened to the old prophecies like they were scary fairy tales. I didn't believe them.

My daughter . . . She's four years old and she can sing, dance, she knows poetry by heart. Her mental development is normal, she isn't any different from the other kids, only her games are different. She doesn't play "store," or "school" she plays "hospital." She gives her dolls shots, takes their temperature, puts them on [an] IV. If a doll dies, she covers it with a white sheet.

We've been living in the hospital with her for four years, we can't leave her there alone, and she doesn't even know that you're supposed to live at home. When we go home for a month or two, she asks me, "When are we going back to the hospital?" That's where her friends are, that's where they're growing up.

After the last operation her urinary functioning completely broke down, and they were unable to insert a catheter. They'll need more operations for that.

They've advised us to seek medical help abroad. Where are we going to get tens of thousands of dollars if my husband makes 120 dollars a month?

One professor told us quietly: "With her pathologies, your child is of great interest to science. You should write to hospitals in other countries. They should be interested." So I write. [Tries not to cry.] I write that every half hour we have to squeeze out her urine manually through artificial openings. Where else in the world is there a child who has to have her urine squeezed out of her every half hour? And how much longer can it go on? No one knows the effect of small doses of radiation on a child. Take my girl, even if it's to experiment. I don't want her to die. I'm all right with her becoming a lab rabbit, just as long as she lives. [Cries.] I've written dozens of letters. Oh, God!

She doesn't understand yet, but someday she'll ask us: why isn't she like everyone else? Why can't she love a man? Why can't she have babies? I wanted to get papers so that she'd know, when she grew up, it wasn't our fault, my husband and I. It wasn't our love that was at fault. [Tries again not to cry.]

I fought for four years with the doctors. I knocked on the doors of important people. It took me four years to finally get a paper from the doctors that confirmed the connection between ionized radiation and her terrible condition. They refused me for four years, they kept telling me: "Your child is a victim of a congenital handicap." What congenital handicap? She's a victim of Chernobyl!

I studied my family tree. Nothing like this has ever happened in our family. Everyone lived until they were eighty or ninety. My grandfather lived until he was 94. The doctors said: "We have instructions. We are supposed to call incidences of this type general sicknesses. In twenty or thirty years, when we have a database about Chernobyl, we'll begin connecting these to ionized radiation. But for the moment science doesn't know enough about it." But I can't wait twenty or thirty years. I wanted to sue them. Sue the government. They called me crazy, laughed at me. [Beat] There were children like these in ancient Greece, too. One bureaucrat yelled at me: "You want Chernobyl privileges! Chernobyl victim funds!" How I didn't lose consciousness in his office, I'll never know.

[Breaks down. Cries.] This girl is growing up -- she's still a girl -- even our neighbors don't know. I'll put a dress on her, and a handkerchief, and they say, "Your Katya is so pretty." Meanwhile I give pregnant women the strangest looks. I have all these mixed feelings: surprise and horror, jealousy and joy, even this feeling of vengeance.

(Pg 126) We’re often silent. We’re afraid to talk about it. We don’t know how. [On April 26, 1986] the world was split in two: there’s us the Cherynobylites, and then there’s you, the others. (Pg 133) They’ve written dozens of books. Fat volumes, with commentaries. But the event is still beyond any philosophical description. (Pg 187) It’s not just the land that’s contaminated, but our minds.
```

---

## IC-2345: Walking with RJ

- Title: Walking with RJ
- Author (byline): Stephanie Peirolo
- Work: The Moth Presents All These Wonders, Pgs 82-88
- Publisher: Crown
- Publication date as stated: Mar 2017
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: STEPHANIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1577
- Already set (do not supply): none

### Source block (context only)

```text
Author: Stephanie Peirolo
Book: The Moth Presents All These Wonders, Pgs 82-88
ISBN: 978-1101904404
Publisher: Crown
Date (Month/Year): Mar 2017
```

### Introduction (context only: never use it for content warnings)

```text
No mother should have to choose between saving her child’s life and navigating the maze of health insurance coverage. But that’s exactly what Stephanie Peirolo faced when her son RJ suffered a traumatic brain injury. She thought the hardest part would be watching RJ fight for his life not fighting a system that puts profits before people.

Health insurance “coverage” quickly vanished behind automated phone lines and unreadable policies. And when Stephanie is fired from her job for taking too much time off, what little insurance safety net was in place disappeared too. While her son struggled to hold up his head, and relearn basic things like swallowing and speaking, Stephanie Peirolo discovered that our healthcare system doesn’t break only the sick. It breaks the families who love them, too.

Walking with RJ by Stephanie Peirolo
```

### Performance text (classify this)

```text
STEPHANIE: (Pgs 82-88) I was 23 years old when I had my first child. I was in labor for three days before my son, RJ, was born. So when I first laid eyes on him, I felt nothing but exhaustion. I said, “This is it?” It wasn’t until about an hour later, when I woke up and he was in my arms, wrapped up, that I felt it -- that rush of maternal love, that primal adoration. And I thought, This is it. This is how the species survives.

I had another child, a daughter, Emma. And soon after Emma was born, their father and I divorced. He moved to Europe, and I raised the kids by myself.

Fast-forward. We’re living in Seattle. The kids are in high school and doing great. They get straight A’s. The only thing RJ gets in trouble for is wearing his hair long. He goes to Catholic school and you’re supposed to have your hair above your collar. But RJ plays the drums, he’s in theater, so he wears his hair long.

In the fall of his junior year, he’s cast as the lead in the school play. He’s going to be Atticus Finch in To Kill a Mockingbird, so he has to get his hair cut. And I remember him walking out of the barbershop. He had a crew cut, and he was six feet tall and impossibly handsome. He had this kind of shy smile, and I thought, This is the man he is becoming.

STEPHANIE: In January of his junior year, a cop showed up at our door, and he said, “Are you RJ’s mom?” I said yes. He said, “There’s been an accident.” I said, “Is he dead?” And he said, “Not yet, but we have to get to the hospital right away.” So the cop drove me to Harborview, which is not the closest hospital to our house, but it is the one with a trauma center. We went in the back way, where the ambulance bays are. Someone was hosing blood out of the back of an ambulance, all of this blood, and I remember thinking, That’s my son’s.

It took a couple of hours for me to find out what had happened. RJ had been driving to his best friend’s. He had his seat belt on. He didn’t have drugs or alcohol in his system, and he was hit from the side in a blind intersection. He sustained a traumatic brain injury (or TBI), and he had broken his pelvis. At the time I didn’t understand the gravity of a TBI.

I was the vice president of an advertising agency. They had just changed their insurance plan. Keep in mind, it’s the first week of January. So I didn’t have a list of

my benefits. What I have is an insurance card with a phone number on the back. So while RJ’s in the ICU, I call the phone number, and the voice on the other end of the phone told me, “ICU is covered, intensive brain-injury rehab is covered, skilled nursing facility . . .”

And they list off all these great benefits. And I remember thinking, Thank God I don’t have to worry about insurance.

When RJ was discharged from the ICU, he was transferred to the rehab facility, and shortly after, they called me and said, “Your insurance company called and said RJ’s benefits are up on Friday.” I said, “No, no, no, no, he’s got many more benefits,” but of course I just had a voice on the other end of the phone.

So I went over there, and said, “Where am I supposed to take him? He’s in a coma.” They said, “Well, there’s always foster care.” (shocked pause) So Emma and I took RJ home. We made a hospital room in his bedroom. He had PEG tube in his stomach, and that’s how we pumped in nutrition. They taught us how to do physical therapy. Emma was 15, and she said, “Mom, I will help you take care of RJ in any way I can, as long as it doesn’t involve the Speedo zone.” So when he needed to be changed, because of course he was in diapers, she would bring me a bucket of warm water and washcloths and I would clean him up.

Coming out of a coma is nothing like what you see in the movies. It’s a long, slow, painstaking process. It took RJ months to learn how to hold up his head. We put him in his wheelchair, and his friends would come by every day after school.

Months had passed, and I still couldn’t get the Summary Plan Description. I kept calling [the insurance company]. But I realized this not a bureaucratic mix-up, this is intentional and this is illegal. This is a violation of a law called ERISA - the Employee Retirement Income Security Act of 1974. So I called an ERISA lawyer and told him the situation, and he said, “I can help you, but you’re going to have to give me a retainer of $30,000.” I said, “Let me be clear. I’m a single parent. I have paid to set up a hospital room in my house. I pay a nurse to sit with my son, so that I stay employed so I can keep this insurance. I don’t have $30,000.” And he said, “I’m sorry; I can’t help you.”

At this point, I was completely exhausted and I was very concerned about getting fired because I’d taken so much time off. So, I applied for and was granted FMLA leave. The Family Medical Leave Act says you can take 12 weeks of unpaid leave to care for a sick family member and they have to keep your job for you. Shortly into my FMLA leave, I was fired. These things are illegal, but you can’t call the police on a corporation. And I couldn’t afford an attorney.

When RJ turned 18, he was able to go on Medicaid, and I made the decision to put him in a nursing home. I found a facility that specialized in patients with TBIs. All their patients were on Medicaid, so they didn’t have much money. But they took really good care of RJ, and he continued to make slow progress. He could do thumbs-up for yes, thumbs-down for no. We were visiting him, and Emma was teasing him, and he flipped her off. I got really excited ‘cause that’s like some manual dexterity happening there, right? And then he turned to me and he put his hand down because, brain injury notwithstanding, he was not about to flip off his mother.

Before RJ’s accident, I had to drag him to Mass on Sundays, but after the accident, he loved to go to church.I’d say, “Do you want to go to Mass today?” He’d put his thumbs up. He learned how to put money in the collection plate again. And when he learned how to swallow – because apparently swallowing is incredibly complex; that took like a year to come back -- he could take Communion, and you could see it provided him so much solace.

In August of 2005, RJ got very sick, and we thought it was the flu. He still had his PEG tube in his stomach, and it had fallen out. That happens, and when it falls out, you put it back in. You’re supposed to X-ray to make sure you have it in the right place. Well, this facility couldn’t afford an X-ray machine, so they guessed and they guessed wrong.

His food had been going into his abdominal cavity and he had sepsis. At the hospital, the surgeon took me aside and said, “I can operate on RJ, and I might save his life, but he’s going to go back into a deep coma, and he will never come out. Or you can let him go. You have to decide.”

So I went down the hall and called his father, who was still in Europe, and I said, “What should I do?” He said, “You’re caring for him; it’s your choice.”

So I went into RJ’s room. [He] was completely aware of what was happening, and he was afraid. His eyes were open really wide. And I said, “Honey, you’re very sick, and they can’t fix you. So you’re gonna go to God -- you’re gonna go to God, but my dad is there, and he’s gonna come and find you, and I will be there soon.” (long beat as she struggles to compose herself)

It took RJ three days to die. (another long silence)

[Today], RJ would be 27 years old. Why didn’t you keep him at home? If you had made more money, you could’ve put him in a private nursing home, then he never would’ve died.

The world is so diminished without him, like there’s been a total eclipse of the sun. Only I’m the only one who can see it. (beat) I wonder if RJ’s existence is part of a larger narrative arc. If maybe this slice in time was how RJ had to work out his destiny, and maybe my job was to walk with him. (beat) Between RJ’s accident and his death, he was only able to say a handful of words. And the word he said most was “Mom.” And there are times now where I feel RJ. I feel that he is. And in those moments, I know it’s his turn . . . for his love to carry me.
```

---

## IC-2346: The Waltz

- Title: The Waltz
- Author (byline): Dorothy Parker
- Work: Literature Alive
- Publisher: NTC Publishing Group
- Publication date as stated: June 1994
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2007
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dorothy Parker
Book: Literature Alive
ISBN: 978-0844250007
Publisher: NTC Publishing Group
Date (Month/Year): June 1994
```

### Introduction (context only: never use it for content warnings)

```text
The Waltz by Dorothy Parker
```

### Performance text (classify this)

```text
Why, thank you so much. I'd adore to.

I don't want to dance with him. I don't want to dance with anybody. And even if I did, it wouldn't be him. He'd be well down among the last ten. I've seen the way he dances; it looks like something you do on Saint Walpurgis Night. Just think, not a quarter of an hour ago, here I was sitting, feeling so sorry for the poor girl he was dancing with. And now I'm going to be the poor girl. Well, well. Isn't it a small world?

And a peach of a world, too. A true little corker. Its events are so fascinatingly unpredictable, are not they? Here I was, minding my own business, not doing a stitch of harm to any living soul. And then he comes into my life, all smiles and city manners, to sue me for the favor of one memorable mazurka. Why, he scarcely knows my name, let alone what it stands for. It stands for Despair, Bewilderment, Futility, Degradation, and Premeditated Murder, but little does he wot. I don't wot his name, either; I haven't any idea what it is. Jukes, would be my guess from the look in his eyes. How do you do, Mr. Jukes? And how is that dear little brother of yours, with the two heads?

Ah, now why did he have to come around me, with his low requests? Why can't he let me lead my own life? I ask so little -- just to be left alone in my quiet corner of the table, to do my evening brooding over all my sorrows. And he must come, with his bows and his scrapes and his may-l-have-this-ones. And I had to go and tell him that I'd adore to dance with him. I cannot understand why I wasn't struck right down dead. Yes, and being struck dead would look like a day in the country, compared to struggling out a dance with this boy. But what could I do? Everyone else at the table had got up to dance, except him and me. There was I, trapped. Trapped like a trap in a trap.

What can you say, when a man asks you to dance with him? I most certainly will not dance with you, I'll see you in hell first. Why, thank you, I'd like to awfully, but I'm having labor pains. Oh, yes, do let's dance together -- it's so nice to meet a man who isn't a scaredy-cat about catching my beri-beri. No. There was nothing for me to do, but say I'd adore to. Well, we might as well get it over with. All right, Cannonball, let's run out on the field. You won the toss; you can lead.

Why, I think it's more of a waltz, really. Isn't it? We might just listen to the music a second. Shall we? Oh, yes, it's a waltz. Mind? Why, I'm simply thrilled. I'd love to waltz with you.

I'd love to waltz with you. I'd love to waltz with you. I'd love to have my tonsils out, I'd love to be in a midnight fire at sea. Well, it's too late now. We're getting under way. Oh. Oh, dear. Oh, dear, dear, dear. Oh, this is even worse than I thought it would be. I suppose that's the one dependable law of life -- everything is always worse than you thought it was going to be. Oh, if I had any real grasp of what this dance would be like, I'd have held out for sitting it out. Well, it will probably amount to the same thing in the end. We'll be sitting it out on the floor in a minute, if he keeps this up.

I'm so glad I brought it to his attention that this is a waltz they're playing. Heaven knows what might have happened, if he had thought it was something fast; we'd have blown the sides right out of the building, Why does he always want to be somewhere that he isn't? Why an't we stay in one place just long enough to get acclimated? It's this constant rush, rush, rush, that's the curse of American life. That's the reason that we're all of us so - - Ow! For God's sake, don't kick, you idiot; this is only second down. Oh, my shin. My poor, poor shin, that I've had ever since I was a little girl!

Oh, no, no, no. Goodness, no. It didn't hurt the least little bit. And anyway it was my fault. Really it was. Truly. Well, you're just being sweet, to say that. It really was all my fault.

I wonder what I'd better do -- kill him this instant, with my naked hands, or wait and let him drop in his traces. Maybe it's best not to make a scene. I guess I'll just lie low, and watch the pace get him. He can't keep this up indefinitely -- he's only flesh and blood. Die he must, and die he shall, for what he did to me. I don't want to be of the over-sensitive type, but you can't tell me that kick was unpremeditated. Freud says there are no accidents. I've led no cloistered life, I've known dancing partners who have spoiled my slippers and torn my dress; but when it comes to kicking, I am Outraged Womanhood. When you kick me in the shin, smile.

Maybe he didn't do it maliciously. Maybe it's just his way of showing his high spirits. I suppose I ought to be glad that one of us is having such a good time. I suppose I ought to think myself lucky if he brings me back alive. Maybe it's captious to demand of a practically strange man that he leave your shins as he found them. After all, the poor boy's doing the best he can. Probably he grew up in the hill country, and never had no larnin'. I bet they had to throw him on his back to get shoes on him.

Yes, it's lovely, isn't it? It's simply lovely. It's the loveliest waltz. Isn't it? Oh, I think it's lovely, too.

Why, I'm getting positively drawn to the Triple Threat here. He's my hero. He has the heart of a lion, and the sinews of a buffalo. Look at him -- never a thought of the consequences, never afraid of his face, hurling himself into every scrimmage, eyes shining, cheeks ablaze. And shall it be said that I hung back? No, a thousand times no. What's it to me if I have to spend the next couple of years in a plaster cast? Come on, Butch, right through them! Who wants to live forever?

Oh. Oh, dear. Oh, he's all right, thank goodness. For a while I thought they'd have to carry him off the field. Ah, I couldn't bear to have anything happen to him. I love him. I love him better than anybody in the world. Look at the spirit he gets into a dreary, commonplace waltz; how effete the other dancers seem, beside him. He is youth and vigor and courage, he is strength and gaiety and -- Ow! Get off my instep, you hulking peasant! What do you think I am, anyway -- a gangplank? Ow!

No, of course it didn't hurt. Why, it didn't a bit. Honestly. And it was all my fault. You see, that little step of yours -- well, it's perfectly lovely, but it's just a tiny bit tricky to follow at first. Oh, did you work it up yourself? You really did? Well, aren't you amazing! Oh, now I think I've got it. Oh, I think it's lovely. I was watching you do it when you were dancing before. It's awfully effective when you look at it.

It's awfully effective when you look at it. I bet I'm awfully effective when you look at me. My hair is hanging along my cheeks, my skirt is swaddling about me, I can feel the cold damp of my brow. I must look like something out of the "Fall of the House of Usher." This sort of thing takes a fearful toll of a woman my age. And he worked up his little step himself, he with his degenerate cunning. And it was just a tiny bit tricky at first, but now I think I've got it. Two stumbles, slip, and a twenty-yard dash; yes. I've got it. I've got several other things, too, including a split shin and a bitter heart. I hate this creature I'm chained to. I hated him the moment I saw his leering, bestial face. And here I've been locked in his noxious embrace for the thirty-five years this waltz has lasted. Is that orchestra never going to stop playing?Or must this obscene travesty of a dance go on until hell burns out?

Oh, they're going to play another encore. Oh, goody. Oh, that's lovely. Tired? I should say I'm not tired. I'd like to go on like this forever.

I should say I'm not tired. I'm dead, that's all I am. Dead, and in what a cause! And the music is never going to stop playing, and we're going on like this, Double-Time Charlie and I, throughout eternity. I suppose I won't care anymore, after the first hundred thousand years. I suppose nothing will matter then, not heat nor pain nor broken heart nor cruel, aching weariness. Well. It can't come too soon for me.

I wonder why I didn't tell him I was tired. I wonder why I didn't suggest going back to the table. I could have said let's just listen to the music. Yes, and if he would, that would be the first bit of attention he has given it all evening. George Jean Nathan said that the lovely rhythms of the waltz should be listened to in stillness and not be accompanied by strange gyrations of the human body. I think that's what he said. I think it was George Jean Nathan. Anyhow, whatever he said and whoever he was and whatever he's doing now, he's better off than I am. That's safe. Anybody who isn't waltzing with this Mrs. O'Leary's cow I've got here is having a good time.

Still if we were back at the table, I'd probably have to talk to him. Look at him -- what could you say to a thing like that! Did you go to the circus this year, what's your favorite kind of ice cream, how do you spell cat? I guess I'm as well off here. As well off as if I were in a cement mixer in full action.

I'm past all feeling now. The only way I can tell when he steps on me is that I can hear the splintering of bones. And all the events of my life are passing before my eyes. There was the time I was in a hurricane in the West Indies, there was the day I got my head cut open in the taxi smash, there was the night the drunken lady threw a bronze ashtray at her own true love and got me instead, there was that summer that the sailboat kept capsizing. Ah, what an easy, peaceful time was mine, until I fell in with Swifty, here. I didn't know what trouble was, before I got drawn into this danse macabre. I think my mind is beginning to wander. It almost seems to me as if the orchestra were stopping. It couldn't be, of course; it could never, never be. And yet in my ears there is a silence like the sound of angel voices. . . .

Oh they've stopped, the mean things. They're not going to play anymore. Oh, darn. Oh, do you think they would? Do you really think so, if you gave them twenty dollars? Oh, that would be lovely. And look, do tell them to play this same thing. I'd simply adore to go on waltzing.
```

---

## IC-2347: Warning Signs

- Title: Warning Signs
- Author (byline): Allie Brosh
- Work: Hyperbole and a Half (Pg 1-18)
- Publisher: Touchstone Books
- Publication date as stated: Oct 2013
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: ALLIE, IMAGINED BY A 10-YEAR-OLD
- Teaser before the introduction: Yes
- Spoken words (computed): 1981
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
Looking back . . . it should have been one of those very clear WARNING SIGNS. Parents, get your child to a therapist NOW!

Warning Signs from Hyperbole and a Half by Allie Brosh
```

### Performance text (classify this)

```text
ALLIE: (Pg 1-18) When I was ten years old, I wrote a letter to my future self and buried it in my backyard. Seventeen years later, I remembered that I was supposed to remember to dig it up two years earlier. I looked forward to getting a nostalgic glimpse into my childhood— perhaps I would marvel at my own innocence or see the first glimmer of my current aspirations. As it turns out, it just made me feel real weird about myself.

ALLIE: The letter was scrawled in green crayon on the back of a utility bill. My ten-year-old self had obviously not spent much time planning out the presentation of it. Most likely, I had simply been walking through the kitchen and suddenly realized that it was entirely possible to write a letter to my future self.

The overwhelming excitement of this realization probably caused me to panic and short-circuit, making me unable to locate proper writing implements. There was no time for that kind of thing.

I did, however, manage to fight through the haze of chaos and impulse long enough to find a crayon stub and a paper surface to mash it against.

The letter begins thusly: Dear 25 year old [note: not “Dear 25-year-old me” or “Dear 25-year-old self,” just “Dear 25 year old”]

Do you still like dogs? What is your favarite dog? Do you have a job tranning dogs? Is Murphy still alive? What is youre favarite food?? Are mom and dad still alive?

I feel it’s important to note the order of those questions. Obviously, dog-related subjects were my chief concern (Murphy was my family’s dog), followed closely by the need to know my future favorite food (I feel that the double question marks speak to how important I thought that question was). Only then did I pause to wonder whether my parents had survived.

The letter continues with a section titled “About me”: My name is Allie and I am ten years old. I have blound hair and blue eyes. My favarite dog is a german shepard. My second favarite dog is a husky. My third favarite dog is a Dobberman Pincher.

This is troubling for a number of reasons, the first of which is that I apparently thought my future self wouldn’t be aware of my name or eye color. “Who. What if – in the future – I’m not even me any more. I won’t know what I am.”

The second thing is the fact that I just tacked on my favorite dog breeds at the end there, like it was every bit as important to my identity as the other things. As if my past self had imagined my future self standing in the yard above the upturned earth, clutching my letter and screaming, “BUT WHAT DOGS DID I LIKE??? HOW AM I SUPPOSED TO UNDERSTAND MY IDENTITY WITHOUT KNOWING WHAT DOGS I LIKED WHEN I WAS TEN???”

I took a break from writing at that point to draw several pictures of what appear to be German shepherds.

Below the German shepherds, I wrote the three most disturbing words in the entire letter—three words that revealed more about my tenuous grasp on reality than anything else I have uncovered about my childhood. There, at the bottom of the letter, I had taken my crayon stub and used it to craft the following sentence: Please write back.

Judging by the thick, purposeful lines in each letter, I was applying a truly impressive amount of pressure to the crayon. The sincerity of the request is unmistakable. When I asked my future self what my favorite dog is or whether my mom and dad were still alive, I actually expected to get answers. And, apparently, I still expected to be ten years old when I got those answers. Please write back. I imagine myself patiently standing in the yard, day after day, thinking, Any time now . . . It’s going to happen soon, I just know it . . . 1, 2, 3, now. 1, 2, 3, NOW! 1, 2, 3, NOW

Time travel is a complex subject that I don’t expect a ten-year-old to fully understand, but this is more than just a basic misunderstanding of time travel.

ROUGH APPROXIMATION OF TEMPORAL CONTINUITY, AS

IMAGINED BY A 10-YEAR-OLD: Person . . . . Undergoes mitotic event at age 10. One “me” Stays 10 . . . One “me” continues to the future *possibly no longer aware of self . . . 15 year later, writes letter and sends it to the past to inform self about favorite dog.

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

## IC-2348: White Oleander

- Title: White Oleander
- Author (byline): Janet Fitch
- Work: Not specified
- Publisher: Back Bay Books
- Publication date as stated: May 2000
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2283
- Already set (do not supply): none

### Source block (context only)

```text
Author: Janet Fitch
ISBN: 978-0316284950
Publisher: Back Bay Books
Date (Month/Year): May 2000
```

### Introduction (context only: never use it for content warnings)

```text
And so they went, against Astrid’s better judgment, to visit the woman who genetically had the right to claim Astrid as daughter. After all, Astrid couldn’t protect her foster mother, Claire, forever, could she? White Oleander by Janet Fitch
```

### Performance text (classify this)

```text
Dear Claire,

Yes, I think it would be marvelous if you’d visit. It’s been so long since I’ve seen Astrid, I don’t know if I’d recognize her – and I’m always delighted to meet my loyal readers. I will put you on my visitors list – you’ve never been convicted of a felony, have you? Just teasing.

Your Friend,

Ingrid

It was February, a gray morning so overcast we couldn’t see the Hollywood Hills from our yard. We were going to visit my mother. Claire had set it up. The idea of this meeting was almost too much to bear. I could only lose. My mother could hurt her. Or she could win her over. I didn’t know which was worse. Claire was mine, someone who loved me. Why did my mother have to get in the middle? But, that was my mother, she always had to be the center of attention, everything had to be about her.

I looked in the mirror, imagining what my mother would think of me now. The scars on my face were just the start. I’d been through a few things since then. I wouldn’t know how to be with her now, I was too big to hide in her silence. And now I had Claire to worry about.

I had second thoughts about my clothes too, a long skirt and Doc Martens, thick socks, a crocheted sweater with a lace collar from Fred Segal, where all trendy young Hollywood shopped. My mother was going to hate it. But I had nothing to change into, all my clothes were like that now.

We drove east for an hour. It had been more than two years since I’d last come this way, a very different girl in pink shoes. We drove back along the same blacktop road to the CIW, the steam stack and the water tower, the guard tower that marked the edge of the prison. We parked in the visitors lot.

Claire took a deep breath. “This doesn’t look so bad.” We sat at a picnic table under the blue overhang. I watched the gate where my mother would come in. Claire shivered. She was trying to be brave. “Why are they staring at us like that?

It was cold, but now I was sweating, waiting for my mother. Who knew, maybe they would become friends. Maybe my mother wasn’t playing a game, or not to ugly a one. I saw my mother, waiting while the CO opened the gate. Her hair was long again, forming a pale scarf across the front of her blue dress, she was as nervous as I was. So beautiful. She always surprised me with her beauty. Even when she had just been away for a night, I’d see her and catch my breath. She was thinner than the last time I’d seen her, all the excess flesh had been burned away. Her eyes had become even brighter, I could feel them from the gate. She was very upright, muscular, and tan. She strode up, smiling, but I felt uncertainty in her hands. We looked into each other’s eyes, and I was astonished to find that we were the same height. Her eyes were searching within me, trying to find something to recognize. They made me suddenly shy, embarrassed of my fancy clothes, even of Claire. I was ashamed of the idea that I could escape her, even of wanting to. “Welcome to Valhalla,” she said, shaking Claire’s hand. I tried to imagine how my mother must be feeling right then, meeting the woman I’d been living with, a woman I liked so much I hadn’t written anything about her. Now my mother could see how beautiful she was, how sensitive, the child’s mouth, the heart-shaped face, the delicacy of her neck, her freshly cut hair. Claire smiled with relief that my mother had made the first move. She didn’t understand the nature of poisons.

She looked older than the last time I saw her, lines etching into her tanned face, around the eyes and thin mouth. I winced at her old-fashioned, actressy diction. I could imagine my mother mocking her later to her cellblock sisters. But I couldn’t protect Claire now. It was too late. I saw that the perennial hint of irony in the corners of my mother’s lips had now been etched into a permanent line, the tattoo of a gesture.

“My daughter says you’re an actress.” She wore no sweater in the cold grayness of the morning. The fog suited her, I smelled the sea on her although we were hundred miles from any ocean.

Claire twisted her wedding ring, it was loose on her thin fingers. “To tell you the truth, my career’s a disaster. I blotched my last job so badly, I’ll probably never work again.” Why did she always had to tell the truth? I should have told her, certain people should always be lied to. My mother instinctively felt for the crack in Claire’s personal history, like a rock climber in fog sensing fingerholds in a cliff face. “Nervous?” she said kindly. Claire leaned closer to my mother, eager to share confidences. “It was a nightmare,” she said, and began to describe the awful day.

Overhead the clouds roiled and clotted, like dysentery, and I felt sick. Claire was afraid of so many things, she only went thigh-deep into the ocean because she was afraid of being swept under. So why couldn’t she feel the undertow? My mother’s smile, so kind-looking. They treat actors so badly,” my mother said. “I’ve had it.” “No more. Dragging myself to auditions, just to have them look at me for two seconds and decide I’m too ethnic for orange juice, too classic for TV moms.” “That’s why Astrid and I get along. Scorpio and Pisces understand one another.” My mother didn’t like that we understood each other, Claire and I, could tell by the way she was pulling my hair. “Astrid and I never understood each other. Aquarius and Scorpio. She’s so secretive, haven’t you found that? I never knew what she was thinking.” “We just adore her,” Claire said, and for a moment I saw her my mother saw her. Actressy, naïve, ridiculous. No, I wanted to say stop, don’t judge her based on this. “She’s doing wonderfully well, she’s on the honor roll this year. We’re trying to keep that old grade point average up.” I was mortified and I didn’t want to be. When would my mother have worked with me, hour after hour, to raise the old grade point average?

“Does he have to travel a good deal, your husband? What’s his name again? Ron?” “He’s always gone,” Claire admitted. “He wasn’t even home for Christmas.” “It must be lonely for you,” my mother said. Sadly. So sympathetic. I wished I could get up and run away, but I would never leave Claire here alone with her. “It used to be,” Claire said. “But now I have Astrid.” I was such a traitor. I had betrayed my master. She knew why I’d kept Claire in the background. Because I loved her, and she loved me. Because I had the family I should have had all this time, the family my mother never thought was important, could never give me. “Astrid, do you mind letting us talk for a moment alone? Some grown-up things.” I looked from her to my foster mother. Claire smiled. “Go ahead. Just for a minute.” Like I was a kid who had to be encouraged to get into the sandbox. She didn’t know how long a minute could be, what might happen in a minute.

I got up reluctantly and went over to the fence closest to the road, ran my fingertips over the bark of a tree. I watched them, leaning toward each other over the table. My mother was talking without stopping, low, reasonable, I’d seen her hypnotize a cat this way. Claire was upset. I didn’t care what my mother’s game was. Her time was up. We were leaving, she was staying. She couldn’t screw this up for me, no matter what she said. They both looked up as I rejoined them. My mother glared at me, then veiled it with a smile. “You just remember what I told you.” “I’ll meet you in the car,” she said.

My mother and I watched her go. “What did you tell her?” “ I hear she’s having trouble with her husband.” She smiled sensually, “It’s not you, is it? I know you have an attraction to older men.” “No, it’s not me.” She couldn’t play with me the way she played with Claire. “You stay out of it.” I could see it startled her to have me oppose her. It angered her that I felt I could, but she was controlled, I could see her switch gears. “I have to do what I can for my new friend.” “Just leave her alone.” “Oh, but it’s fun,” my mother said. “Don’t screw it up for me.” “What could I do? I’m a poor prisoner. A little bird with a broken wing.” “If you love me, you’ll help me.” “Help you, darling? I’d rather see you in the worst kind of foster hell than with a woman like that.” She grabbed my wrist, forcing me to look at her. Now she was dead serious. “What are you going to learn from a woman like that?” “How to pine artistically? She stood and kissed me on the cheek, embraced me lightly. “All I can say is, keep you bags packed.” “I think I did well with you mom, don’t you?” “You did,” I told her, gazing out the window so I wouldn’t have to lie to her face. “She really liked you.” A tear rolled down her cheek,” What did she said to you?” “She said that I was right about Ron. That he was having an affair. I knew it anyway, she just confirmed it.” “How would she know,” I said. “For God’s sake, Claire, she just met you.” “All the signs are there,” she sniffled. “I just didn’t want to see them.” Claire was supposed to go to an audition. She had told Ron she would, but she had me call in and say she was sick. Ron was supposed to be home on Friday, but something came up. His trips home were handholds for her, so she could swing from one square on the calendar to the next. When he said he was going to come home and didn’t, she swung forward and grasped thin air, fell. I intercepted a letter from prison from my mother to Claire. In it, my mother advised a love potion to put in his food, but everything in the formula she sent looked poisonous to me. I wanted to hold her close, but something was pushing her away. I didn’t think I could save her anymore. “Claire, you know he’ll be back. He loves you, don’t worry.” I didn’t care if he came back or not. I heard the squeak of the bedsprings as she turned over, the effort it took to get up, stumble the three steps to the door. She tumbled with the lock. I opened the door and she fell back into bed, still wearing that red bathrobe. “I’m so cold,” she mumbled. “Come in with me.” I got in, clothes and all. She put her cold feel on mine, her head on my shoulder. “Stay with me, promise. Don’t leave.” I held her cold hands, rested my head against hers as she fell asleep. Claire was still sleeping when I woke up. I got up, careful not to disturb her, and went out to the kitchen. After a while, I checked on Claire. She was still asleep. The room was dark gray, no morning light penetrated the French doors covered with blinds. She had one hand flung across the top of the pillow. Her mouth was open, but she wasn’t snoring now. “Claire?” I put my face right to hers. She smelled of sherry and something metallic. She didn’t move. I put my hand on her shoulder, shook her gently. “Claire?” She didn’t do anything. I couldn’t hear her breathing. I shook her again. “Claire, wake up.” I yelled at her, hoping she would open her eyes. It was impossible. “Claire.” I screamed into her sleeping face. Nothing. I searched the bedside table, the floor. On the far side, I found the pills on the floor, along with the empty sherry bottle. The pill bottle was open, the pills spilled out, small pink tablets. Butalan, the label said. For Insomnia. Do Not Take With Alcohol. The sounds I was making were no long screams. I knocked the bedside light off the nightstand. I pulled the magnet box from under the bed and threw it across the room. I took her silver-backed hairbrush and threw it overhead like a baseball into the round mirror. I took the phone off the receiver against the headboard until it came apart in my hands, leaving dents in the soft pine. I lay my head on her chest where there was no heartbeat. She was so pale. Cold. Maybe she hadn’t meant to. She would have written a note, explaining everything two or five ways. Maybe all she wanted was to sleep. The house was still. I heard the tick of the clock on the bedside table. A car drove past in the street. Fresh air came through the windows. She lay with her mouth open on the flowered pillow in her red bathrobe in the brightness of the morning.
```

---

## IC-2349: Why Don’t I Like My Own Child?

- Title: Why Don’t I Like My Own Child?
- Author (byline): Jennifer Rabiner
- Work: Not specified
- Publisher: Redbook Magazine
- Publication date as stated: November 10, 2016
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1960
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jennifer Rabiner (pseudonym)
Weblink: https://www.redbookmag.com/life/mom-
kids/a11805/i-dont-like-my-child/
ASIN: B01M6Y82UP
Publisher: Redbook Magazine
Date (Month/Year): November 10, 2016
```

### Introduction (context only: never use it for content warnings)

```text
Motherhood is supposed to come with an instant, unbreakable bond—a love so natural that no one ever questions it. But what if that bond never appears? What if the child you dreamed about and the child you raise feel like two entirely different people? In this brutally honest account, a mother confesses the unthinkable: she never liked her daughter.

Only years later, when a startling diagnosis finally explains Sophie’s struggles, does the mother realize what it truly means to love the child you have, not the one you imagined.

Why Don’t I Like My Own Child? by Jennifer Rabiner
```

### Performance text (classify this)

```text
(pseudonym)

A mom is never, ever supposed to admit this, but here goes: I've never liked my child.

Growing up, I had hoped to someday have a daughter, and I had a clear vision of what she would be like: vivacious, spunky, and whip-smart, socially savvy and self-assured. What I got was the polar opposite.

(pseudonym)

At birth, Sophie was skinny and weak. She nursed poorly, and she cried so hard that she vomited—daily. As a toddler, she was strange. She wouldn't make eye contact, and she'd scream bloody murder at the sound of ripping paper. Instead of scribbling with crayons, she'd line them up at the edge of the paper. She'd climb to the top of the slide and then cry to be rescued. She couldn't or wouldn't answer direct questions. She didn't make friends. Life seemed hard for her. It broke my heart a little every day.

As you can probably imagine, I felt guilty that I was basically repelled by my own child. Who wouldn't? But honestly, the guilt was overshadowed by a colossal sense of disappointment. This just wasn't the magic mother-daughter bond that every book I read, every movie I saw, and every family I'd ever met had led me to expect.

When Sophie was 18 months old, we visited my sister, now a psychologist, who said out of the blue, "You know, Sophie is an odd kid." I asked what she meant. "She's just kind of — off ," she said. Her comment upset me but only confirmed my suspicions that Sophie might be on the autism spectrum. I spoke to her day-care director and had her tested by the school district. Neither found anything wrong. I found a pediatric neurologist, but when they sent me forms to fill out, Sophie had none of the physical symptoms in the boxes under "Reason for Visit." I canceled the appointment. My husband accused me of searching for a diagnosis that didn't exist, but I needed to know why my daughter wasn't meeting her developmental milestones, let alone my expectations.

I felt guilty that I was basically repelled by my own child. Who wouldn't?

My husband, by contrast, has always loved and cherished Sophie for who she is. And he makes it look so easy! Instead of gritting his teeth through her most eccentric behaviors, he imitates them in an exaggerated way, which makes her howl with laughter. Then he starts laughing too, and they collapse in hugs. I envy his ease with her.

I might have thought I was lacking a maternal instinct, but when my second daughter was born, I was blown away by overwhelming Mommy Love. Lilah was exactly the baby I'd envisioned: strong and healthy, with a penetrating gaze. She nursed vigorously and smiled and laughed easily. She talked early and often and, even as a toddler, befriended everyone she met. When I hugged her, she squeezed back hard, and I felt my own heart beating in two bodies at once.

As Lilah grew healthy and robust, Sophie looked noticeably meek by comparison. It's true that I, like all my relatives, am petite, but Sophie was beyond small — weak, skinny, and pale. The contrasts between Lilah and Sophie went beyond the physical. There was Lilah, initiating a joyous game of peekaboo at 6 months, while her sister, then 3, sat on the floor babbling phrases from books and TV shows. We'd ask, "Sophie, wanna join the game?" And she'd say: "Look, a clue! Where? Over there!" I called it her Rain Man act.

It got to the point where I viewed Sophie's every move through a lens of failure. At a birthday party, when she walked away from the parachute game the other kids were playing, I said, "There she goes again, being antisocial." But another mom said, "Sophie's doing her own thing. She wants no part of that dumb parachute. Smart girl." I thought, Whoa! I would never have seen it that way. To me, she was trapped in her own strange world, driven by her own mysterious motivations, and hopelessly incapable of being normal. I knew I was being hard on her, but I couldn't seem to stop.

A moment of reckoning came when Sophie was 4, at a playdate with my best friend and her daughter. I was judging Sophie as usual, criticizing how she was painting with the stick part of the paintbrush instead of the bristles, when my friend turned to me and said point-blank: "You are Sophie's mother. You're supposed to be her rock — the person she can count on most in the world for unconditional love and support. It doesn't matter if you like her or not; you still have to support her." I started to cry, because I knew she was right. And deep down, I was ashamed of how easily I had betrayed my own daughter. If I looked at my behavior objectively, it was disgusting.

My friend consoled me but didn't let me off the hook. "What are you going to do about this?" she asked. I honestly didn't know. Then, a few days later, we got a yer from Sophie's preschool. It advertised a workshop by a clinical psychologist called "Loving and Honoring the Child You Have, Not the One You Wish You Had." Bingo! I called the psychologist to see if we could meet privately, which we did. At her prompting, I described Sophie's various limitations, which I had jotted on the back of a business card:

• Has uneven skills (as a toddler, she knew the whole

alphabet and could count to 60, but could barely string

three words together).

• Hurts herself, perhaps out of anxiety (used to tear out

clumps of hair, then began scratching herself).

• Doesn't express needs or even recognize them (will cry

when hungry even as her peers use full sentences).

• Freaks out at high-pitched noises (like the beeping of

an ATM).

• Prefers to play alone (when other kids try to play with

her, she ignores them, or tries to play but doesn't

seem to grasp how).

She nodded as I listed my grievances, and I got excited, expecting to hear a diagnosis that would finally make sense of Sophie's quirks and lead to an effective treatment. But no luck. She felt I wasn't attuned to Sophie's vulnerabilities — she's a sensitive soul; I'm a bull-in-a-china-shop type. But something is wrong with my child, I kept thinking. Why can't anyone else see it?

Instead, she made suggestions designed to help me bond with her. I took notes.

The first thing I had to do, said the psychologist, was identify my expectations of Sophie so I could understand whether they were realistic or un- achievable. As long as I wanted her to be someone she could never be, I was setting her up to fail, in my eyes, every single day. I explained that I wanted Sophie to make eye contact.

To me, she was hopelessly incapable of being normal.

"That's too hard for her," the psychologist said, recalling my own checklist. "She's acutely sensitive — you whisper, and for her it's like a megaphone." I realized that I wished Sophie were tougher (she's hypersensitive), more outgoing (she's shy), and "cool" (even now, as a 9-year-old, she favors kittens and angels). Scrap those things. Start over. I needed to stop seeing what Sophie was not and start seeing what she was. A few months later, when Sophie drew a unicorn on a piece of construction paper and said she wanted to use it for her birthday party invitation, I resisted the temptation to hide it in the garbage and order glossy invites instead. Color copies of Sophie's rainbow unicorn went out to 45 kids — and I got emails raving about it! Score one for Sophie.

Advertisement - Continue Reading Below

Still, denying my expectations day after day was hard. I wondered if my upbringing may have set the bar too high. As the daughter of a local politician, I was expected to be a role model — to dress appropriately, smile and make small talk, write thoughtful thank-you notes. And I was a natural. My mother used to say, "Nothing succeeds like success," and I stepped up. Why couldn't Sophie?

I tried to ignore my gut instinct that something still wasn't quite right. The psychologist recommended that I connect with Sophie over something she enjoys, and as much as Calico Critters weren't my thing, I vowed to try. A few days later, I found her poring over a Mini Boden catalog. Aha! We shared a love of shopping! It might not be the most wholesome or financially sustainable hobby, but we needed to start somewhere. I plopped down next to her and asked, "If you could get one thing on each page, what would it be?" My sister and I had played this game as kids, and Sophie caught on instantly. Too bad life isn't one big catalog game.

Instead, more often, it was Sophie crawling on all fours and meowing, shrieking, jabbering in made-up languages, and asking nonsensical questions (What if day were night, and night were day? What if it snowed in summer? What if our last name was Nebraska?). Even when I tried to help her — by going over the moves that tripped her up in dance class and urging her to stop transferring her boogers from nose to mouth — I only did so because I wanted her to be accepted and liked, which was my agenda, not hers. Sadly, my efforts only made her feel more self-conscious and anxious. And I continued to feel exasperated and annoyed. Why was my own daughter so difficult for me to parent? I gradually got used to the feeling, but I never made peace with it.

Then, when Sophie was 7, a stunning revelation rocked our family's world. At the prompting of our pediatrician, who was concerned about Sophie's sluggish growth, she was tested and diagnosed with a growth hormone deficiency that had slowed her development across the board since birth. Her speech, motor skills, and social maturation were three years behind schedule. Wow! It wasn't the diagnosis I expected, but it made sense.

Growth hormone regulates so many functions in the body; Sophie's lack of it explained everything from her blue moods and anxious behaviors to her difficulty communicating to her birdlike appetite and negligible muscle tone. My first reaction was relief — a diagnosis! Then hope — help is on the way! Then guilt. All this time, Sophie was struggling. She was 7 by the calendar but only 4 by her own body clock, a pre-K'er thrust into second grade. She was coping with enormous challenges every day without a mother who believed in her. Even worse, I had resented her for letting me down, when it was I who was letting her down. I instantly regretted scads of horrible things I'd said to her over the years and prayed that the damage wasn't irreparable. What a wake-up call.

As the diagnosis sank in, I found myself feeling more tender, more motherly toward Sophie. Instead of me pitted against her, it's now us, together, pitted against this diagnosis. My husband is cautiously optimistic about the treatment (nightly hormone shots) but concerned about possible side effects. After all, he has accepted her as is all along. The happy dance I'm doing over this diagnosis is mine alone.

Whether I've finally learned to be a good parent to Sophie — or in spite of the fact that I haven't — my now- 9-year-old is in a pretty good place. The hormone shots have delivered positive effects beyond inches and pounds. Sophie competes on the local gymnastics team, aces her spelling tests, goes on loads of play- dates, and loves to download songs for her iPod. She makes eye contact and answers direct questions. I'm pretty sure she's genuinely happy most of the time, though she's still fairly anxious and still occasionally meows and shrieks. I watch her sometimes, looking for clues of the emotional scarring I fear I've inflicted, but I see none. Instead, she takes running leaps into my arms, her strong legs squeezing my middle in her signature "cobra hug." Do we see eye to eye? Almost never. But do I try to prop her up every single day anyway? Yes, I do. After all, I'm her mom.
```

---

## IC-2350: Wintergirls

- Title: Wintergirls
- Author (byline): Laurie Halse Anderson
- Work: Not specified
- Publisher: Penguin Books
- Publication date as stated: Feb 2010
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1161
- Already set (do not supply): none

### Source block (context only)

```text
Author: Laurie Halse Anderson
ISBN: 978-0142415573
Publisher: Penguin Books
Date (Month/Year): Feb 2010
```

### Introduction (context only: never use it for content warnings)

```text
The danger of habit. When you train yourself to do something over and over again, how do you break the rigorous training you’ve set up for yourself? In the following selection, Lia has spiraled into not eating. Counting calories, competing with her best friend to be the thinnest, Lia is caught and monitored by family, but nothing is enough to stop her from returning to old habits. What does it take to make a change? To turn toward recovery.

Wintergirls by Laurie Halse Anderson.
```

### Performance text (classify this)

```text
(Pg 7) . . . When I was a real girl, with two parents and one house, breakfast was granola topped with fresh strawberries, always eaten while reading a book propped up on the fruit bowl.

(Pg 5) “Why don’t you have one of those muffins?” [My stepmom, Jennifer, asks.] “I bought oranges yesterday, or you could have toast or frozen waffles.”

Because I can’t let myself want them because I don’t need a muffin (410), I don’t want an orange (75) or toast (87), and waffles (180) make me gag.

(Pg 7) No. I can’t go there. I won’t think. I won’t look.

I won’t pollute my insides with Bluberridazzlepops or muffins or scritchscratchy shards of toast, either. Yesterday’s dirt and mistakes have moved through me. I am shiny and pink inside, clean. Empty is good. Empty is strong.

(Pg 27) The first time . . . (Pg 9) Mom and Dad rushed in, side by side for a change, happy that I was not dead. A nurse handed my chart to my mother. She read through it and explained the disaster to my father and then they fought, a mudslide of an argument that spewed across the antiseptic sheets and out into the hall. I was stressed/overscheduled/manic/no -- depressed/no -- in need of attention/no -- in need of discipline/in need of rest/in need/your fault/your fault/fault/fault. They branded their war on this tiny skin-bag of a girl.

Phone calls were made. My parents force-marched me into New Seasons . . . They locked me up and dripped sugar water into my empty veins . . . (Pg 27) The first time they admitted me, this body weighed 093.00 pounds.

(Pg 28) I was a good girl because I didn’t poke holes in my skin, or write depressing poetry, and I ate and ate. They stuffed me like a pink little piggy ready for market. I bit, chewed, swallowed day after day and lied, lied, lied. (Who wants to recover? It took me years to get that tiny. I wasn’t sick; I was strong.) But staying strong would keep me locked up. The only way out was to shove in food until I waddled.

Four weeks later, the gates opened. Mom drove me home and we pretended none of it ever happened, except for the meal plans and the rules and the appointments and the scales and the hurricane of my mother’s disappointment.

(Pg 46) The doctors told Dad to buy a Blubber- O-Meter 3000, a bathroom scale with a giant dial that was easy to read. Jennifer had to do the dirty work, weighing me in my tattered yellow robe to make sure I stayed fat. For the first couple of months, she measured my sins every morning and called in the results to my doctor once a week. The ugly numbers made me cry.

Everyday weighing became every-other-day weighing became every-Tuesday weighing because none of us wanted to do it in the first place . . .

(Pg 189) Adrenaline kicks in when you’re starving. That’s what nobody understands. Except for being hungry and cold, most of the time I feel like I can do anything. It gives me superhuman powers of smell and hearing. I can see what people are thinking, stay two steps ahead of them.

(Pg 145) I’m hungry I need to eat.

I hate eating.

I need to eat.

I hate eating.

I need to eat.

I love not-eating.

(Pg 161) Why? You want to know why?

Go to school to jump through hoops, sit up and beg, and roll over on command. Listen to the whispers that curl into your head at night, calling you ugly and fat and stupid and bitch and whore and worst of all “a disappointment.” Puke and starve and cut and drink because you don’t want to feel any of this. Puke and starve and cut and drink because you need an anesthetic and it works. For a while. But then the anesthetic turns into poison and by then it’s too late because you are mainlining it now, straight from your soul. It is rotting you and you can’t stop. Look in a mirror and find a ghost. Hear every heart-beat scream that everysinglething is wrong with you.

“Why?” is the wrong question.

Ask “Why not?”

(Pg 46-47) I change into the yellow robe in my bedroom and make sure the quarters I sewed into the pockets aren’t making them droop. When I get to the bathroom, Jennifer is fixing her eyeliner in the mirror. I step on the scales. 107.00 fake pounds.

(Pg 220) Alone . . . I strip, to weigh my faults and measure my sins . . . (Pg 52-53) as I step on the scale, I open my eyes. 099.00 pounds. I am officially standing on Goal Number One.

Goal Number Two is 095.00, the perfect point of balance. At 095.00, I am pure. Light enough to walk with my head up, meaty enough to fool everyone.

At 090.00, I soar. That’s Goal Number Three.

(Pg 220) 089.00.

I could say I’m excited, but that would be a lie. The number doesn’t matter. If I got down to 070.00, I’d want 065.00. If I weighed 010.00, I wouldn’t be happy until I got down to 005.00. The only number that would ever be enough is 0. Zero pounds, zero life, size zero, double-zero, zero point.

(Pg 8) I [drive], windows down, music cranked, flying to the SATs.

Did I eat breakfast? Of course not. Did I eat dinner the night before, or lunch, or anything?

The car in front of [me] brake[s] as the traffic light turn[s] yellow, then red. My edges blur. The car in front disappear[s]. The steering wheel, the dashboard, vanish.

(Pg 271) The light beyond my eyes flashflashflashes with a hundred futures for me. Doctor. Ship’s captain. Forest ranger. Librarian. Beloved of that man of that woman or those children or those people who voted for me or who painted my picture. Poet. Acrobat. Engineer. Friend. Guardian. Avenging whirlwind. A million futures - not all pretty, not all long, but all of them mine.

(Pg 8) When I w[a]ke up, the emt-person and a cop [are] frowning. My blood pressure that of a cold snake. My heart [is] tired. My lungs [need] a nap.

(Pg 266) Two days later, (Pg 274-276) my third visit to New Seasons is the longest one yet, a marathon, not a sprint to the exit. No games this time. No midnight exercise parties in the shower for me. No dumping my food in the plants or sticking it in my underwear or bribing an attendant to lie about my intake.

The concept of eating is scary. I put all of the bites in my mouth and try not to count. It’s hard. Food is life. I exhale, take another breath. Food is life. And that’s the problem. When you’re alive, people can hurt you. It’s easier to lock everybody out. But it’s a lie.

Food is life. I have no idea how much I weigh. This scares me to death, but I’m working on it. I am beginning to measure myself in strength, not pounds. Sometimes in smiles.

I am learning how to taste everything.
```

---

## IC-2351: The Woman Who Walked Into Doors

- Title: The Woman Who Walked Into Doors
- Author (byline): Roddy Doyle
- Work: Not specified
- Publisher: Penguin Books
- Publication date as stated: Jan 1997
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: CHARLO, LEANNE, PAULA, NICOLA
- Teaser before the introduction: Yes
- Spoken words (computed): 2331
- Already set (do not supply): none

### Source block (context only)

```text
Author: Roddy Doyle
ISBN: 978-0140255126
Publisher: Penguin Books
Date (Month/Year): Jan 1997
```

### Introduction (context only: never use it for content warnings)

```text
In Ireland, the euphemism "she walked into a door" is so loaded with grim implications of domestic abuse that it is usually whispered, not spoken. According to Women’s Aid of Ireland, one third of women never relate their experiences to anyone and simply try to survive – as well as to protect their children in many instances – as best they can on their own. – Many people ask . . . Why don’t they just leave? And in Paula Spencer’s story, perhaps we can understand exactly that. Why?? The Woman Who Walked into Doors by Roddy Doyle
```

### Performance text (classify this)

```text
*NOTE: Roddy Doyle is an Irish author and this would be the perfect piece to try out your Irish dialect.

My name is Paula Spencer. I am thirty-nine years old. I was married for eighteen years. My husband left me. I threw him out. His name was Charles Spencer; everybody called him Charlo.

THE FIRST TIME IT HAPPENED . . . . . He lost his temper. And he hit me. It was as simple as that. He sent me flying across the kitchen. I hit the sink and fell. I felt nothing, only shock. And a spinning in my head. I knew nothing for a while, where I was, who was with me, how come I was on the floor. Then I saw his feet, then his legs, making a triangle with the floor. He seemed way up over me. Miles up. I had to bend back to see him. Then he came down to meet me.

CHARLO: Y'alright? His eyes were going all over my face, every inch and corner. Looking, searching. Looking for marks, looking for blood. He was worried. His face was full of worry and love. He was scared.

CHARLO: You fell. I didn't - I wouldn't do what he wanted, he was in his moods, I was being smart, he hated me being pregnant, I wasn't his little Paula any more - and he drew his fist back and he hit me. He wanted to hurt me. And he did. OR . . . . I'd been too near him; he hadn't realised. He'd only been warning me. He didn't know his own strength. He had things on his mind. Anything. It wouldn't happen again. It had been a mistake. We'd laugh about it later. Remember the time. We did laugh about it later. That night. And the time after that. And the time after that. Many other nights. Until I couldn't laugh any more. I wouldn't let myself. Nothing came out when I opened my mouth. Only pain. Someone once told me that we never remember pain. Once it's gone it's gone. A nurse. She told me just before the doctor put my arm back in its socket. She was being nice. She'd seen me before. -I fell down the stairs again, I told her. No questions asked. What about the burn on my hand? The missing hair? The teeth? I waited to be asked. Ask me. Ask me. Ask me. I'd tell her. I'd tell them everything. Look at the burn. Ask me about it. Ask. . . . No. The doctor never looked at me. He studied parts of me but he never saw all of me. He never looked at my eyes. Drink, he said to himself. I could see his nose moving, taking in the smell, deciding. I am an alcoholic. I've never admitted it to anyone. I've never done anything about it; I've never tried to stop. I think I could if I really wanted to, if I was ready. I've always liked a drink. I don't remember when I stopped liking it and started needing it. It crept up on me, I suppose. Being hit by Charlo the first time knocked everything else out of me. One day I was Mrs Paula Spencer, a young wife and soon to be a mother, soon moving into a new house, in a new place, making my husband's dinner, timing it so it would be just ready for when he came in from work. Then I was on the floor and that was the end of my life. The future stopped rolling in front of me. Everything stopped. I keep blaming myself. After all the years and the broken bones and teeth and torture I still keep on blaming myself. I can't help it. What if? What if? He wouldn't have hit me if I hadn't . . . none of the other fists and belts would have followed if I hadn't. . . He hit me, he hit his children, he hit other people - and I keep blaming myself. For provoking him. For not loving him enough; for not showing it. Did you fall down the stairs, Paula? Did you walk into a door, Paula? What made him do that, Paula? What made you do that, Paula? Did you say something to him, Paula? No. No. No! I'm innocent. I'm innocent. I'm innocent. He. Hit. Me. Ask me. Ask me. Ask me. Here goes. Broken nose. Loose teeth. Cracked ribs. Broken finger. Black eyes. I don't know how many; I once had two at the same time, one fading, the other new. Shoulders, elbows, knees, wrists. Stitches in my mouth. Stitches on my chin. A ruptured eardrum. Burns. Cigarettes on my arms and legs. Thumped me, kicked me, pushed me, burned me. He butted me with his head. He held me still and butted me; I couldn't believe it. He dragged me around the house by my clothes and by my hair. He kicked me up and he kicked me down the stairs. Bruised me, scalded me, threatened me. For seventeen years. Hit me, thumped me, raped me. Seventeen years. He threw me into the garden. He threw me out of the attic. Fists, boots, knee, head. Bread knife, saucepan, brush. He tore out clumps of my hair. Cigarettes, lighter, ashtray. He set fire to my clothes. He locked me out and he locked me in. He hurt me and hurt me and hurt me. He killed parts of me. He killed most of me. He killed all of me. Bruised, burnt and broken. Bewitched, bothered and bewildered. Seventeen years of it. He never gave up. Months went by and nothing happened, but it was always there - the promise of it. For seventeen years. There wasn't one minute when I wasn't afraid, when I wasn't waiting. Waiting for him to go, waiting for him to come. Waiting for the fist, waiting for the smile. I was brainwashed and braindead, a zombie for hours, afraid to think, afraid to stop, completely alone. I sat at home and waited. I mopped up my own blood.

I lost all my friends, and most of my teeth. He gave me a choice, left or right; I chose left and he broke the little finger on my left hand. Because I scorched one of his shirts. Because his egg was too hard. Because the toilet seat was wet. Because because because. He demolished me. He destroyed me. And I never stopped loving him. I adored him when he stopped. I was grateful, so grateful, I'd have done anything for him. I loved him. And he loved me. He was everything and I was nothing. I provoked him. I was stupid. I forgot. I needed him. I was hopeless, useless, good for nothing. I lived through years of my life thinking that they were the most important things about me, the only real things. I couldn't cope, I couldn't earn, I needed him. I needed him to show me the way; I needed him to punish me.

(FLASHBACK TO MEMORY)

LEANNE: -Don't hit my mammy! Leanne's voice. She is twelve [now – she was younger then . . . 5 or 6?] She always cheers me up. She's intelligent and creative and good at math. Leanne's arms around my leg, clinging to me. As he went around me. And I turned to keep facing him. Trying to keep Leanne behind me. -It's alright, love. To Leanne. Patting her head. Her face pushed into me. Looking at her father. Looking at his fists. At his face. Not being able to see her. My hand on her head. -It's okay. Having to keep my eyes on Charlo. Pleading with him, holding him back. Feeling Leanne's shivering. Keeping him back. Making sure I faced him. Making sure I didn't let her become a shield. Her heart beating. Keeping my eyes on Charlo's eyes.

CHARLO: -Where'd you get that?

PAULA: -What?

CHARLO: -The eye. It was a test. I was thumping inside. He was playing with me. There was only one right answer. - I walked into the door.

CHARLO: -Is that right? Looks sore. -It's not too bad. He was messing with me, playing. Like a cat with an injured bird. Keeping me in my place. Pretending he didn't remember. I could never fight back. When he wasn't hitting me he was reminding me that he could. He was reminding me and getting me ready. Like the cat playing with the bird, letting it live a bit longer before he killed it. He put one of his fingers on the bruise. I made sure I stayed absolutely still.

CHARLO: -You must have walked right into it, did you?

PAULA: -Yeah; I wasn't looking.

CHARLO: -Which door?

PAULA: -Bedroom.

CHARLO: -Were you drinking?

PAULA: -No. Just careless.

CHARLO: -Yeah. Every day. I think about it every minute. Why did he do it? No real answers come back, no big Aha. He loved me. I know it. But if he loved me, why did he hit me? Why did he hit me so hard and so often? The questions are never answered. They always torment me. And his love becomes a cruel thing, like a smile on a Nazi's face. You don't hit the people you love. You might, once or twice - it's only human. But not the way he did it, again and again. You don't pull back their fingers till they snap. You don't wake them in the morning with a kick in the stomach. You don't hold their face over the chip pan and threaten to dump their head into the boiling fat. You don't beat them in front of their children. That's not love. You can't love someone one minute, then beat them, and then love them again once the blood has been washed off. I never gave up. I always got up off the floor. I got between them and him. I made ends meet. I never gave up. I'm here. I picked myself up. I washed the blood off my face. I put on the kettle. I came close. I wanted to die. I lay on the floor and felt death under it. It was warm and I wanted it. I never wanted to get up. I was broken; I wanted to melt. I didn't know who I was. All I knew was the pain. But I got up. I always got up. I had children. I had a husband. I limped around the rooms, tucking the children up in their beds. I hung out the washing with a broken finger. I drank gin. I made sandwiches for their lunches; thin slivers of ham around the edges to hide the nothing in the middle. I hid. I hid the pain, the bruises and the poverty. I could never get past the door. There were too many things. Things I didn't have. Money, somewhere to go. Too many things. The kids. The schools. People seeing me. All of them stopped me. It was all black out there. -Where would you be without me? he said. I couldn't go. He'd come after me and kill me. And the kids. He said he'd never let me take them. I wasn't fit to look after them; I was an alcoholic and too stupid. He wouldn't let it happen; they'd be better off dead. He looked at me. He meant it. He smashed me against the door before I could open it. He hit my face off it. I waited for the glass to smash into me.

CHARLO: -I'll kill you; I'll kill you! I could never go. I always stopped at the door. But when I saw him looking that way at Nicola, She is eighteen . . . when I saw his eyes. It wasn't the way men look at women - I could nearly have understood that. It was almost natural, something to be careful about. But it was sheer hate. It was clear in his face. He wanted to ruin her, to kill her. His own daughter. Because he could. There was evil in him. I wasn't going to pretend any more. Things were falling apart and it didn't matter. I looked at Nicola.. She looked at me. Yes, her face said; you're right, it's happening. She looked embarrassed and guilty. What did I do? her face said. I'm sorry. Help. He started humming. The noise disgusted me. I grabbed the frying pan. He was looking straight at Nicola; he was going to make her get out of his way, rub against her. I could always tell when Charlo was about to move; his shoulders told you. They went before his legs. I hit him on the side of the head with the pan. I knew I was angry now. I took aim this time. He tried to get up. I hit him on top of the head. I could have killed him; it didn't matter. He collapsed properly. I'd done something. - I saw him, I said. -Looking. Nicola nodded. She shut the fridge door.

NICOLA: -Is he dead?

PAULA: -I hope so, I said. His head moved; I had to start again.

NICOLA: -Kill him

PAULA: -No, I said. -There's no need. She couldn't believe me. She thought I was being completely thick.

NICOLA: -He'll kill you now.

PAULA: -No, he won't, I said.

NICOLA: -He will. I escorted him off the premises. Out the gate he went. He got away from me, down the path, away from us. Drenched and bloody and stooped over like a travelling rat. -Go away! He stood there. At the gate. The blood was still running out of his head, down into one of his eyes. The door behind me slammed. It was Nicola. -Go away, will yeh! Go away! And he did. I couldn't believe it. He did what I'd told him to. He walked away. His head still down. He said nothing at all. -Jesus- -He's gone.

NICOLA: -What now? -God knows, I said. -But one thing's for certain. He's not coming back in here again. Her face said it: she'd heard it before. -He's not, I said. It was a great feeling for a while. I'd done something good.
```

---

## IC-2352: Words (from the Cancer Monologue Project)

- Title: Words (from the Cancer Monologue Project)
- Author (byline): Christine Barber
- Work: The Cancer Monologue Project
- Publisher: MacAdam/Cage Publishing
- Publication date as stated: 2002
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1585
- Already set (do not supply): none

### Source block (context only)

```text
Author: Christine Barber
Book: The Cancer Monologue Project
ISBN: 978-1931561228
Publisher: MacAdam/Cage Publishing
Date (Month/Year): 2002
```

### Introduction (context only: never use it for content warnings)

```text
Biopsy-A procedure where a piece of tissue is taken from a person's body and examined to determine if a person has cancer and, if so, what type it is. Prognosis-A prediction of what might Radiation Therapy-X-ray treatment that damages or kills cells. Remission-The disappearance of cancer symptoms Words from the Cancer Monologue Project by Christine Barber
```

### Performance text (classify this)

```text
I’m not a crier, but I cried that day. Wracking, can’t-catch-your-breath sobs, as I sat in my car in the hospital parking lot. A woman glanced at me as she walked by, seeing my smeared mascara, blotchy lipstick and cheeks streaked with tears. She probably thought I was sad. The doctor had said the scan “looked good.” I waited until I was alone in my care to break down in relief. I called everyone on my cell phone, telling them my scan was clean. The thyroid cancer that had spread to my lungs was gone. I cried more. I started my care and headed for the Glorieta Baptist Center. I wanted to walk in the prayer garden, the only green place I could think of in December. I need to be outside, near God

As I drove, I thought of the past year, the surgery, the radiation I had ten months ago. That damn radiation, where I sat for three days in a lead-lined room, my only constant visitor a hospital tech who checked me every few hours with some type of Geiger counter. Most of the room was covered in plastic, like when you visit your paranoid grandmother who Saran-wraps the sofa in case you spill something. The hospital put plastic on the phone, the toilet, the bed to protect them – from me, from my radioactivity. I was a radioactive danger to society. A prisoner in a lead-lined room who must be kept away from all the healthy people. The very nice doctors and very nice nurses who came in stood behind lead-lined screens, staring at me.

I drank bottle after bottle of Gatorade to coax the radiation out of my body, the sweet taste sticking to the roof of my mouth. I didn’t think about the plastic, the Gatorade or the very nice nurses. I just made it all into an amusing story I told the people who called me on the plastic-covered phone. I described with a laugh the weird three-flush toilet ritual I had to perform and the visits from the Geiger-counter man. I didn’t tell the callers about what the radiation was doing to me, seeping and creeping into my every cell. I didn’t think about what it was doing to my ovaries, my eggs—my eggs that were no contaminated by radiation. I made jokes to my sister on the phone about how my unborn kids would be superheroes, the radiation giving them the ability to bend steel and talk to fish. I didn’t tell her about my fears that I would now be childless.

I left the hospital after my three days and tried very hard not to think about that lead-lined room. I thought about work, school, guys, guacamole, anything but cancer. Did I really have cancer? Five months after I left the hospital, I was in Target, the bright, fluorescent lights giving everything a weird, radioactive glow. How the meaning of that word has changed for me. I don’t even remember what I was shopping for, probably something innocuous like cotton balls, toothpaste or a lava lamp. Everyone at work had been telling me how “fabulous” I looked, but I always wondered if they were lying as they tried not to stare at the neon pink surgical scar across my neck. The other Target shoppers didn’t even glance at my scar. I convinced myself that meant it wasn’t noticeable, as I grabbed my cotton balls or lava lamp and headed to the checkout line. I plunked my purchases on the counter, not paying much attention to what I was doing, my mind, my eyes, my everything, on something else.

And then I heard, “Hey, it’s the Scar Lady.”

I looked up. I’d seen this cashier before. His face was pink with acne. He had piggy little eyes of a piggy little, nondescript color. He was tall and bony, not yet grown into his body.

For one tiny second that will stretch out for the rest of my life, I hated that stupid, idiotic sixteen-year-old boy. A boy who was only trying to be friendly in his awkward teenage way. I hated him because he made me remember that I’d had cancer. I hated him because he told the truth when no one else would. He saw my scar and, for once, unlike every single person before him, he didn’t say I looked “fabulous.” He saw my scar for what it was: horrible. He told it like it was. I mumbled “hello” to the boy and left as quickly as I could, not wanting him to see the anger in my eyes.

Five months later the doctor said my cancer was gone and that silly boy became nothing more than a funny story for me to tell at dinner parties.

That December day as I pulled into the prayer garden, I thought about making myself a bumper sticker that read “Make Way for the Scar Lady.” I laughed at my own joke as I got out of the car, beaming, my face still wet with tears. I prayed and thanked God as I walked. I even got down on my knees in the icy mud. Hallelujah and all that. I found a quiet bench next to an unbelievably tall ponderosa pine and sat down to write in my journal. I wrote, “Today I walk in the garden of God,” and thought “What a nice thing to put on a tombstone.” My tombstone. Someday, fifty years from now. In the faraway future when I died of old age or an accident involving a llama and a Go-Kart, not cancer. I was joyous. I had always heard that word used in church songs and never understood it. That was my most joyous day. Isn’t that pathetic? My most joyous day involved cancer. No my graduation from college, not getting the big job. But a deadly illness.

How funny that day seems now. Not “ha, ha” funny, but horrible funny.

Almost a year after that day, I went to the doctor’s office for a checkup. I sat on the examination table, my feet not reaching the ground, kicking my legs like some elementary school kid sent to the principal’s office. I was there for a checkup. A simple checkup. Nothing more. Just a checkup like I had several times since finding out my cancer was gone.

The office was cold, but it always was. The nurse was looking at my chart, not at me. Always at my chart with all those bright green Post-it notes on the front that I couldn’t read from a distance no matter how much I scrunched up my eyes. The nurse’s brow was furrowed. Her red hair was wispy at the ends where it was dried from too much hair dye. I was bored. As always when I’m bored, I made a joke. I don’t remember exactly what I said. Something about being in remission. I laughed, but she didn’t. She seemed so hesitant, so unsure. She said something about “traces.” She said the scan last year, the same scan the doctor said “looked good,” showed traces of cancer. I still had cancer. I was confused, too confused to ask questions. Too confused to wonder why the doctor hadn’t mentioned that I still had cancer during my last three office visits. Had it just never come up in conversation? The nurse said when the doctor told me the scan “looked good,” he meant the cancer hadn’t spread, not that it was gone.

I work in words. I know their power. The doctor had said it “looked good,” the same as saying “You’re cured,” right? In journalism we call it paraphrasing a quote. I paraphrased that quote for a full year to my family, my friends, myself, telling everyone I was cured. The doctor said so when he saw my scan, didn’t he? Or did I just hear what I wanted? Did I just want to forget so badly about lead-lined hospital rooms and awkward cashiers that I turned it around in my head?

I needed facts. I needed this nurse with her bad dye job to tell me facts. I hand on to facts like that pink security blanket I had as a kid, the one I clutched into pieces while warding off the monsters in my closet. But she told me nothing in her sidestepping medical-speak. She just talked about “traces.” I used to like that word. It sounds like it could be the name of an upscale apartment complex: “The Traces de Pinon – An exclusive apartment community in the beautiful Sangre de Cristo Mountains.”

The nurse was nice and polite, bad hair and all; too polite to comment on how I melted into nothingness in front of her. I still think about the scene in the doctor’s office like it was inside a snow globe, and I’m on the outside, shaking up the globe and peering inside at the falling snow. It’s apart from me, not touching me. In some wonderland far away.

What now? What do I say to you now? I don’t know the answer to that. I wish I had some nice, happy ending to give you, complete with a handsome prince and a Disney song. But the truth is I’m still furious and devastated. That about covers it. Not much more to say than that. Too furious and too devastated for words.
```

---

## IC-2353: World I Cannot Touch

- Title: World I Cannot Touch
- Author (byline): Janet O’Neill
- Work: Turning Points
- Publisher: Tichenor Publishing
- Publication date as stated: 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1172
- Already set (do not supply): none

### Source block (context only)

```text
Author: Janet O’Neill
Book: Turning Points
Publisher: Tichenor Publishing
ISBN: 978-0742117013
Date: 2001
```

### Introduction (context only: never use it for content warnings)

```text
In today's world, even as awareness and tolerance increase, homosexuality continues to be viewed negatively and through stereotypes. Unfortunately, many of us are treated unfairly throughout society - in church, at school and even in our own homes. At various times homosexuality has been considered a crime, a sickness, a sin or at the very least an abnormality. Given these negative social, religious and familial attitudes it is likely that most gay and lesbian people face difficult and challenging experiences on a regular basis. Ostracized by their peers and rejected by adults, gay and lesbian teens develop disturbing thoughts and feelings about their place in this . . . World I Cannot Touch by Janet O’Neill
```

### Performance text (classify this)

```text
I have to confess. I watch people. I scout out my favorite spots: the food court at the mall, amusement parks, ball games. I watch people and write the rest of their stories. I have regulars. There's Mr. Tight Pants. Is he going to get Sbarro pizza or Panda Wok today? Then it's salad and I make up the rest of the story that Mr. Tight Pants has a big date tonight with someone who he's wanted to date for a long time, but he's not sure if it is a date or just a casual meeting, so Mr. Tight Pants figures eating some salad increases his chances of becoming Mr. Not-SoTight Pants, which will simultaneously increase his chances of it being a date.

You know - stuff like that.

I meet this girl, Andy (short for Andrea), at the movie theater. I write the rest of her story. For the first time ever, I include myself in the story. OK - more admissions. I watch movies more than once. OK - sometimes double-digits. It was during my sixth screening of Bed of Roses, that Andy came into the theatre. I always like to get there early. That way I have more time to concoct stories about the others. I'd seen her before. She'd come alone just like I would and she always brought her own food. Economical. Mental note to guess she's not very wealthy. Add that to the story.

I love to spy on people in cars. People make the false assumption that they are alone. Don't look directly at them or they'll give you this bug-eye stare. Wear sunglasses. Use the rear-view mirror. Suddenly, a whole new world opens up. A business woman picks her nose. Manicured nails. Football players singing musical tunes. OK - that never happened. Another case of me making up the end of the story.

Bed of Roses closed quickly, and I find myself feigning interest in other films. After enduring Celtic Pride, I find Andy sitting in a crowded theater before The Truth About Cats and Dogs. OK, let's be honest, the theater wasn't that crowded, but I acted like it was and sat next to her. Hey, I remember you Bed of Roses, right?

Her first words. More details to add to the story.

Suddenly, I've got the whole story written. Oddly, it's got sexual tension. I'd only had two boyfriends, both of which agreed that it was alright to wait. I was fine with waiting for years. But now I'm writing Andy's story, and the narrative is telling me not to wait. To do anything but wait. To go with her and . . .

We spent time doing fun things, goofy things, educational things. Our chance encounter at the movie theater had taken us to the Farmer's Market, pottery class, feng shi class, fencing lessons. And, of course, more movies. I couldn't get enough of Andy. She worked at the local bank. Guess who opened a checking and savings account and constantly had a transaction to make?

We became an official couple after she got off work one Saturday afternoon. We stopped by the fair and it was really crowded, so we held hands to stay together. I couldn't look forward anymore. I just stared at our hands...together. The next thing I knew, we were back by the lake. It started with a kiss on the neck and the intensity grew. Suddenly, we were . . .

OK, I get it. You're grossed out. You want to hear a lesbian love story as much as my mother does. She didn't have words for lesbians because she refused to speak about them - ever. Two lesbians could be making out three feet in front of her, and she'd only allow us to talk about what we would order for dinner. So when I had weird feelings for my ballet teacher, I didn't say much. Just waited for a guy to come along and find me.

But I understand the gross thing. I do. I mean, after watching Ellen DeGeneres and Anne Heche turn it into a farce, who could blame you? They thought they were bringing lesbianism about in the open. And they did - but put it in the open in a way that no one wanted to see. So I understand how you don't want to hear about my story. But in case you were wondering, it can be beautiful.

Time passes, memories fade and new memories begin to take their place. I wasn't possessive, but I didn't want her to leave. Ever. I didn't want to share her and sleep without her next to me. Andy was the eye-opener. If someone had told me I'd fall in love with a guy named Andy, I'd say sure, fine. If you'd said that Andy was short for Andrea, I'd do one of those Elaine from Seinfeld pushes: "Get out!" I no longer completed people's stories anymore. I was too engrossed in mine. Yet, despite this self-actualized state, when we'd walk hand-in-hand amidst other couples, I'd arrive at the same conclusion: This is heaven . . .for now. Did one relationship count as being a lesbian? Could I live as a lesbian permanently? How long could I last? I didn't know any of the answers. I just knew it couldn't last forever. This was not a life I could live. Look, but don't touch.

But what if I did go for it? Say hell with it all and I am who I am. I've already got hypoglycemia and this scar from a dog bite when I was four. This would be something else to explain to everyone I meet. There would be the attempts for religious conversion. The guys wanting to "fix" me. Everyone visualizing the stereotype of the hairy, gross, lesbian who must have grown up abused. I could fight the stereotypes. Explain myself. But, I'm not a strong person. Look, but don't touch, I decided. Sure, don't touch. But then there's Andy. I'd rather explain lesbianism a million times over than explain to her that it just won't work. After all, it did work!

I was driving to the bookstore one day, blissful yet confused, which had now become my constant state. I was stopped at a stoplight and I thought - hey, for old times sake, let's write the end of a story. The man at the newspaper stand didn't seem interesting. Suddenly, I try the old mirror trick and I see this couple really going at it. I mean...they were...WOW! Now that's love! The light turns green, and they pull away from each other. It was Andy. Andy was with some guy. Some guy. A quy. You know how sometimes, you can catch a person's eye in your rearview mirror? Andy saw me. I tromped the accelerator, but she'd seen me in the mirror, watching my eyes fill with tears.

Look, but don't touch. You touch; you get burned. Touching is going too far. I look, don't touch, and complete the rest of the story.
```

---

## IC-2354: WWJD

- Title: WWJD
- Author (byline): Will Weaver
- Work: On the Fringe: Stories
- Publisher: Dial
- Publication date as stated: April 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2302
- Already set (do not supply): none

### Source block (context only)

```text
Author: Will Weaver
Book: On the Fringe: Stories
ISBN: 978-0142500262
Publisher: Dial
Date (Month/Year): April 2001
```

### Introduction (context only: never use it for content warnings)

```text
Being a transfer student is difficult enough, but Suzanne also carries other burdens into her new high school. When counseling and drug therapy don't help, Suzanne's religious beliefs give her strength. However, her major tormentor, Eddie Halvorsen, won't give up. WWJD by Will Weaver.
```

### Performance text (classify this)

```text
LIKE JESUS, I am surrounded by sin. Every morning on my way to school I walk past rough boys with shaved heads and girls with pierced faces. They stand inches off the high school property line and smoke cigarettes. When I appear, they whoop and swear and throw their trash at me. Every morning I am their amusement. Their victim.

I could easily avoid my tormentors by taking a different path from my aunt's house. But I try to live by one rule: WWJD. What would Jesus do? And the answer is clear. Jesus never took the easy way out. He never avoided the sinners, the lost, the lonely, the hurting. Rather, He went among them.

Today I carry a black plastic garbage bag. My antagonists do not see me immediately-two of them are wrestling in the snow. The rest are laughing and egging them on. I tighten my long orange scarf around my throat, and quietly I ease behind them. I begin to pick up their trash.

"Hey look, it's Weird Suzy!" Weird Suzy, Weird Suzy! they all begin to chant. Sticks and stones. Their name-calling does not bother me. After all, my real name is Suzanne. I am a sixteen-year-old sophomore at River Forks High School in central Wisconsin, and the year is 2001. But I don't feel like this is my school, Wisconsin my state, or these times my times.

This morning a can of Mountain Dew clatters at my feet. Yellow spray splashes my clothes, spatters my face.

"Good hit, Eddie!" someone calls. I look up to my main tormentor, Eddie Halvorsen.

"Hey, pick up my can, Weird Suzy," Eddie says. I bend down to get it. I place it carefully in my garbage bag. "This too, freak," Eddie says. From between his thumb and middle finger he flips his cigarette directly at me. I'm not quick enough to avoid it, but would not have anyway. The cigarette stings my cheek like a bee. Sparks fly as the butt falls at my feet. I touch my cheek; gray ash comes off on my finger tip. I draw my ashy finger slowly across my forehead, then bend to pick up the dead butt.

The parking lot monitor, an off-duty security guard, trots across the street. He comes first to me. "Are you all right, miss?" he says. "You could have put her eye out," the guard says, catching Eddie by the arm.

Eddie shrugs. "I was just getting rid of my butt. Can't help it if she got in the way."

"If this were on school property, you'd be gone-for good," the guard says.

"But it ain't. It's public property. I got my rights, now shove off and stop bothering me."

Then the first hour bell rings. My tormenters look at one another, then swear loudly. Burping and cursing, they throw down their trash, then trudge onto school property. I wait for them to leave. My cheek stings a little but I keep working with my garbage bag.

"Suzanne-come along now," a voice says. I look up. It's the assistant principal, Ms. Kaufman. She takes my garbage bag in one hand and my arm in the other. She reminds me of my real mother, who is in prison. I have not told anyone in River Forks about this. She has leaned in to stare at my cheek. “You'd better drop by the nurse's office and get your face looked at. There's a little blister on your cheek."

"Eddie," I say. I touch the burned spot.

"The parking lot monitor told me. Would you like to fill out a harassment report?"

WWJD? "No," I say.

"I really encourage you to do so. Eddie is out of control these days. You would be helping him."

"A change of heart must come from the inside," I murmur.

Ms. Jones, the nurse, puts ointment on my face. She tries to wipe clean the ash mark but I lean away. "I consider it a religious symbol," I say. "Like the mark Catholics wear on Ash Wednesday," I add.

"Suzanne, today is Monday." Her eyes flicker down the rest of me. At my hair. At my clothes, which I get from the Salvation Army. At my sandals, which I made myself in shop class from tire rubber, leather straps, and buckles. At my long orange scarf, which I wear everywhere. Her eyes return to my hair. 'Are you keeping up your hygiene, Suzanne?" she says. "Good personal hygiene is important-particularly for girls." She smiles and winks. "Let me give you some samples of shampoo and deodorant," she says.

Next I go to the counselor's office. "Who's next? Why, it's Suzanne!" Mr. Klephorn calls heartily. "Come on in!" A hearty greeting is requisite for all counselors. That and positive body language. He glances at a memo on his desk. "I understand that you had an encounter with Eddie Halvorsen this morning."

"Nothing serious. I have no complaint against Eddie. I think he's going through tough times right now. Jesus is trying to speak to him."

Mr. Klephorn purses his lips. "He burned your cheek. I can see the mark from here."

“And I've forgiven him." "Suzanne, we've talked about this ... forgiveness thing.I know you're a very religious person," he continues. "You read the Bible every day."

"Yes. Though mainly in the New Testament. I find the Old Testament too centered upon retribution, revenge. Jesus believed not in punishment but in forgiveness. In turning the other cheek."

"Yes, of course, Suzanne," he says quickly. "But my point, one we've talked about before, is that this is the twenty-first century. These are different times than when Jesus lived. And we must live in them. We must inhabit our own times, so to speak." He clears his throat. "While Jesus provided us wonderful lessons, it is, may I say, perhaps unrealistic to try and live His example every minute of our day."

There is silence as I think about that. Then I say, "But isn't that why we go to church? Why we read the Bible? To live more like Jesus? There are no limits to forgiveness," I say.

My day goes all right. What I'm looking forward to is my last class of the day, woodworking. I've always liked to make things, plus I don't mind being surrounded by boys (I'm the only girl). It is among boys that I can do the most good. At 2:00 P.M. I go to woodworking. Eddie Halvorsen is there, along with the other "woodies." as they call them-selves. He glares at me.

I begin work on my wooden swan. The neck of my black walnut swan curves up gracefully. I've been working on her all term, and she's really getting beautiful. Even Mr. Patterson complimented me on her. He let me do a project different from the boys, most of whom are making gun cabinets. But I love my swan. When I work on her, she reminds me that there is hope for Eddie. For all of us.

After school, on my way home, it is snowing. I walk with my head down and my scarf wrapped around my face. It never snowed in California. Suddenly someone blocks the sidewalk. "Weird Suzy!" Eddie says.

I stop. Blink. "Hello, Eddie," I say. For a moment he scares me. But I remember that Jesus must have been afraid many times. Suddenly Eddie whoops and snakes out his arm; he grabs my orange scarf and strips it from my neck. I blink against the falling snow and look at him. WWJD? I set down my book bag, take off my coat, hold it out to him. "Take my coat too," I say. He stops, stares. Then he grabs my coat, throws it in the snow.

"My hat too," I say. I take off my beret, hand it to him. He throws it in the snow. He laughs. I peel off my sweater-I have on only a T-shirt underneath and it is suddenly very chilly-and I hand it to him. After a moment's hesitation, he takes it. He swallows as he stares at me. I am shivering in the February air. Suddenly he flings my sweater in my face so hard I stumble back. "What in hell is the matter with you?" he says. His voice cracks. When I look up again, he is disappearing in the snow.

The next morning I walk to school the usual way. Eddie's gang spots me, as usual. But this morning Eddie will not look at me. He stands with his back to me, his hands jammed in his pockets. I can feel his anger. His hard heart. Light snow is falling again and has whitened his cap and shoulders. For a moment he looks like a pillar of salt.

In shop class Eddie's dark eyes follow me as I go to my locker, unlock it, carefully take out my swan lamp. I go to my station and begin work. Working on my swan makes me forget everything, even my mother.

"What the hell's that supposed to be, anyway?" Eddie says in my ear. I turn. He grabs at my swan. I jerk it away from him and cradle it in my arms. Eddie laughs. I feel my face flush. I shouldn't have jerked my swan away from Eddie. It's not something Jesus would have done. Slowly I hold it out so that he can see it-but not touch it.

"It's a swan," I say.

"Looks like a damned crow to me," Eddie says.

"It's not finished," I answer. "Like all of us." He stares at me. I see the hate in his eyes.

"You should have stayed in California, you freak." After he leaves I turn back to my swan but my hands are shaky. For one brief moment I understand what Jesus felt like when He knew that He was the One. The Chosen One. "Take this cup," I murmur to my swan. "Choose someone else to help Eddie." But she is silent.

I do not see Eddie after school, which today is all right by me. I take a walk down by the river. I often come down here to pray. Today I pray for my mother that she will not forget me-and especially for Eddie Halvorsen.

Near school the next morning Eddie calls out to me. "Hey, Suzy! How's it going?" I stare. His voice is almost cheerful. None of his friends throw anything at me. They are all smiling. I do not quite understand this, but not everything Jesus does is understandable. I smile a little, nod and pass by.

In shop class I go straight to my locker. I can't wait to get started. But my padlock, broken, falls into my hands. I stare at it, then at my little metal door. Its hinges are bent. Slowly I pull open the door. My swan falls out in pieces. She clatters to the floor like a spilled puzzle that cannot ever be put right. I can't help myself: I drop to my knees, clutch the pieces, and begin to wail. I hear myself calling for my mother.

I leave school late. I have been in the nurse's office. Finally she lets me go home. I head down by the river, when I am aware of footsteps.

"Hey, Weird Suzy." Eddie says. "What happened to your crow?"

I stop. "It was a swan," I blurt. "A black swan." I hunch under my scarf and keep walking.

"So where you going now, Weird Suzy?" he says.

"Down by the river," I say.

"Gonna drown yourself?" Eddie says. He laughs with an odd, high-pitched sound. “Maybe today's the day," he whispers, close behind me now. "If not now, when, Weird Suzy?" Eddie says.

To get away, I head down the bank, past a "Danger -Thin Ice!" sign. "That's right. Good girl!" Eddie calls. He follows me down the bank. I step onto the ice.

I walk out several yards, toward the middle of the river where there is a dark, steaming, open patch. I think of Jesus when He walked on water. It was all a matter of faith. I move a couple of steps closer to the black water. Then I turn and face Eddie, who remains on the white shore. "Are you coming?" I say. "Don't be afraid."

He laughs but there is something thin and reedy and strangled in his throat. "You can do it," I say. I beckon him forward. "Come out to where I am," I say. He stops. "It's all a matter of not being afraid," I say. He takes several more steps-and suddenly there is a sound under his feet like foil ripping. Eddie's arms flap, like a bird taking off, as his legs and trunk disappear through the ice. He screams. I wonder if my black swan screamed when its head was cut off. Suddenly, Eddie is hanging on to the ice by his elbows. Most of his body is underwater.

"Help! Help me!" A car stops on the parkway; the driver quickly lifts a cell phone to his face. "Save me," Eddie screams. "Someone! Suzy! Please! Save me!"

I watch him. I think of my swan. My butchered black swan. I think, What would Jesus do? Possibly I could save Eddie, though he seems to have a grip on the ice. I have my long orange scarf. It would be enough to throw to him. It would be something for him to hold on to until help arrives. But I understand that not even Jesus could save everyone. I sit down on the ice just out of Eddie's reach. I must think about what to do. After all, I am only human.
```

---

## IC-2355: Your Loudmouth Lesbian Friend

- Title: Your Loudmouth Lesbian Friend
- Author (byline): Marcia Wilkie
- Work: Afterbirth: Stories you Won't Read in a Parenting Magazine
- Publisher: St. Martin's Griffin
- Publication date as stated: April 2010
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1500
- Already set (do not supply): none

### Source block (context only)

```text
Author: Marcia Wilkie
Book: Afterbirth: Stories you Won't Read in a Parenting
Magazine
ISBN: 978-0312638351
Publisher: St. Martin's Griffin
Date (Month/Year): April 2010
```

### Introduction (context only: never use it for content warnings)

```text
Are the days of lesbians being viewed with fear and faint disgust by our heterosexual sisters finally at an end? Can lesbians really be a straight girl’s best friend?

We all know about the claim that gay men make great friends for straight women because they love shopping, choosing curtains, and can advise on clothes and makeup.

But perhaps this fascination and focus on sexual preference has gone too far. When will “Your Loudmouth Lesbian Friend” . . . simply become“Your friend?”

This selection by Marcia Wilkie looks at the relationship between straight and lesbian women and especially how that relationship can change when children are factored into the equation.

Your Loudmouth Lesbian Friend by Marcia Wikie.
```

### Performance text (classify this)

```text
Hey there. Hello. It’s me, your loudmouth lesbian friend.

In our transient society, with so many parents of young children living long distances from their in-laws or know-it-all aunts, it really has fallen on the shoulders of the lesbian community to step up and be the voice of reason for all our straight sisters who have been hormonally altered through childbirth.

Many have lost that most precious commodity: common sense.

Here I am, the voice of reason. You can count on me.

You called me yesterday, seeking a friendly voice, exhausted from being up all night with your feverish two-year-old.

So, I said: “You know, you’re destroying your son’s immune system giving him antibiotics.”

It’s what you need to hear, especially since you’ve walked the floor for forty-eight hours carrying twenty-four pounds of screaming kid, yanking his ear off his head.

“Listen to me,” I said, pleased to have the perfect answer. “Get a pencil and write this down.

Ready? Give your baby one teaspoon of crushed garlic mixed in a tablespoon of fish oil. That should resolve the infection.”

When you tell me that right now your child spits even cherry-flavored Tylenol back out, I think to myself, Here’s a parent who lacks persistence. But what I say out loud to you is “You’re the adult. Don’t allow that.”

Raising children is often just that simple. Isn’t it?

Yes. It’s me, your loudmouth lesbian friend. Though I have never even read a baby book and I spend less than forty-five minutes a month around anyone under eighteen years old, I know that I can tell you exactly how to parent your child. I can mouth off advice for any age, from babyhood to the bachelor’s degree.

For example: When your fifteen-year-old comes home from the school dance with a slight smell of beer on her breath, you can count on me to say something useful, like “Wow. That’s a big red flag for future problems.”

Certainly you needed that warning. Somehow, I imagine you saying to your co-parent (if there is one), “You know, our loudmouth lesbian friend might have a point. Perhaps the stocked liquor cabinet we had planned to give our daughter for her Sweet Sixteen isn’t such a great idea. And I’m going to return the fake ID we had made for her.”

Lucky for you, I’m the loudmouth lesbian friend who is there for you, right from the start.

I show up at the hospital, the day after your C-section, and say comforting things like “Do you think you’ll ever regain any muscle tone in your abdomen?” Then I ask to hold your little newbie, bobbling his tiny head around like a Slinky as only a childless lesbian can. Ten minutes later I offer up: “I’d love to stay, but did you know that the florescent lighting in hospitals sucks important nutrients out of the human body? Besides, I’m fighting off a killer sore throat.” Before leaving, I lean into the baby’s bassinet to give him a smooch.

It’s obvious you’re being dramatic when you tell me with a shaky voice that you’re weary and weepy, you love your son, but you’re afraid you’ll fail as a mom and that you’re sore from trying to breast-feed.

“You’ll be okay in a day or two,” I reassure.

“Really?” a look of hope breaks through your glazed-over expression.

With that, I’m out the door. I can’t be late for happy hour at the Closet.

I don’t mean to sound self-important, but clearly, I had the solution when you called me for advice. I could hear the desperation in your voice.

“The baby has been upset for weeks,” you tell me. “Ten hours a day, and it’s making me crazy. My pediatrician said its colic.”

I try to speak in calming tones as I tell you that the solution is within reach.

“Get a dab of gel, rub it between your palms, and gently pat it into your baby’s hair, until the cowlick lies down. There’s no reason to get hysterical over a month of bad hair days.”

What would you do without your loudmouth lesbian friend? I’m the one who shows up to your five-year-old’s birthday party with a bucket of gummi worms, a Super Soaker, and ten cans of Silly String.

The kids have been quietly putting a puzzle together on the floor while the parents chat over coffee and bagels.

I pull you aside. “See, this is why childhood obesity is rampant,” I say, pointing to the composed, contented kids.

Two minutes later I have every child running and screeching through your clean house as I make crazy monster noises and chase them with the giant water pistol. It is only after one kid has crashed head-first into a door jamb, corn syrup solids have been drooled across the sofa, and every child is panting and crazed and moments from meltdown that I announce my departure. It’s been fun, but I’ve got a 3:30 massage.

As a tried-and-true loudmouth lesbian, I’m great at pointing out your parenting shortcomings.

You looked so happy on the afternoon you got an hour away without kids to grab lunch with me, until I noticed a clean diaper in your backpack.

“He’s still not potty trained at three and a half?” I shriek, because you just don’t have enough shrieking in your life.

“Every child is different,” you shrug, going back to your chopped chicken salad.

I, more than many, know that “every child is different.” After all, my mother never expected to raise a lesbian daughter who wouldn’t give her grandkids. I just was. It was my nature, my spirit, my road to travel, and those things have very little to do with parenting.

But I can’t let it be that simple, or that complicated.

So instead, I think to myself, This mom lacks initiative, but what I say out loud is “Well, you better force the issue. Having a Diaper Genie in his dorm room is not going to get him dates in college,” With that I secure my loudmouth lesbian title.

How many hundreds of times will I slap my head in regret over voicing my unneeded and inexperienced opinion? I’m amazed that you still want a loudmouth lesbian friend around. You wanted your child to now gay people, but I’m sure by now you are wishing you had been more selective.

I know the truth. You don’t need a loudmouth lesbian friend telling you how to parent. . .I need you. I need you because I’m not going to be a parent. I need to be around you and your babies, so I can realistically mark the passage of time. Otherwise, I might fool myself into believing that my whole life is ahead of me, because the only change I see is in a mirror. You, however, have the good fortune of seeing through your off-spring that the moment is now. That tie, like a growing child, can never be recovered.

Please don’t let me become one of those homos that treat their pets like children. I don’t want to build a cat condo for Snowflake. I’d rather build a sandbox for your son. I don’t want to spend five bucks on a dog bakery treat for Buster, when he’s obviously just as happy gobbling up horse turds on a hiking trail It’d rather buy cookies from your little girl’s Scout troop.

Don’t let me frame photos of golden retrievers and tuxedo cats. I’d rather show off your child’s artwork.

It makes me happy if you need me, too. Because I will be the loudmouth lesbian in the bleachers, cheering on your little cheerleader. I’ll glow with pride when your son takes honors at the debate tournament. I’ll locate the perfect Halloween costume when their request are impossible. I’ll try to keep your toddler amused with stories and songs when we are stuck in traffic on the I-10 freeway.

Perhaps I’ll be the person you child confides in when she feels different, alone, outside of the group, because she will know that I truly understand what that feels like. Hopefully I’ll be the one your high school student calls as midnight when she is in the next city at a forbidden party that has turned dangerous and she is too scared to call you to come get her.

I will go to get her, no questions asked. I’ll drop her off a half block from your house so you don’t see my car. I won’t drive off until she’s safely through your front door. You will never, ever know about it.

See, I don’t always have to be your loudmouth lesbian friend. As your friend, I know that what matters to you most is that your child has another reliable adult in her life: one who would rescue her no matter what. You can count on me.
```

---

## IC-2356: Zlata’s Diary

- Title: Zlata’s Diary
- Author (byline): Zlata Filipovic
- Work: Not specified
- Publisher: Penguin Books
- Publication date as stated: Feb 1995
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1713
- Already set (do not supply): none

### Source block (context only)

```text
Author: Zlata Filipovic
ISBN: 978-0140242058
Publisher: Penguin Books
Date (Month/Year): Feb 1995
```

### Introduction (context only: never use it for content warnings)

```text
In April 6, 1992 the siege of Sarajevo began. It was the longest siege of a capital city in modern history and produced the worst atrocities in Europe since World War II. Over the course of 3 ½ years, 100,000 people were killed, and half of Bosnia's population of 4.4 million fled their homes. Zlata Filipovic’s family stayed.

Zlata Filipovic, now in her early 30s and living in Paris, was a pre-teen in Sarajevo during the Bosnian war. Her diary of life under siege touched the world. In a recent interview Ms Filipovic says her dreams of peace for Bosnia are still the same . . . and that even today, young people still want to escape Sarajevo. "I really worry that violence is going to erupt again," she said. "There is still so much ethnic hatred and resentment. The majority of my friends are leaving or have already left. There is no work, no hope, and no future there."

This is Zlata’s Diary by Zlata Filipovic
```

### Performance text (classify this)

```text
Thursday, March 5, 1992

Oh, God! Things are heating up in Sarajevo. On Sunday (March 1) a small group of armed civilians (as they say on TV) killed a Serbian wedding guest and wounded the priest. On March 2 (Monday) the whole city was full of barricades. At 6:00 people got fed up and went out into the streets. The procession set out from the cathedral. It went past the parliament building and made its way through the entire city. Several people were wounded at the Marshal Tito army barracks. People sang: (The following is added from Stanza 2 of The National Anthem of Bosnia from 1992 – 1998 – see the You Tube Link at the end of this selection for the melody) Bosnian English Translation Jedna si, jedina, You are the one and only moja domovina. The only homeland I have Jedna si jedina You are the one and only Bosna i Hercegovina. Bosnia and Herzegovina

and cried “Bosnia, Bosnia,” “Sarajevo, Sarajevo,” “We’ll live together” and “Come outside.” Zdravko Grebo said on the radio that history was in the making.

The next day everything was the same as before. Classes, music, school . . . But in the evening, the news came that 3,000 Chetniks [Serbian nationalists] were coming from Pale to attack Sarajevo.

On March 4 (Wednesday) the barricades were removed, the “kids” [a popular term for politicians] had come to some agreement. Great?! [But later] that day our art teacher told us to go home. Something was wrong again! There was a panic. The girls started screaming and the boys quietly blinked their eyes. Daddy came home from work early that day too. It’s all too much!

Tuesday, May 5, 1992

The shooting seems to be dying down. I guess they’ve caused enough misery, although I don’t know why. It has something to do with politics. I just hope the “kids” come to some agreement. Oh, if only they would, so we could live and breathe as humans again. The things that have happened here these past few days are terrible. I want it to stop forever. PEACE! PEACE!

We’ve rearranged things in the apartment. My room and Mommy and Daddy’s are too dangerous to be in.

They face the hills, which is where they’re shooting from. If only you knew how scared I am to go near the windows. So, we turned a safe corner of the sitting room into a “bedroom.” We sleep on mattresses on the floor. It’s strange and awful. But, it’s safer that way.

Thursday, May 7, 1992

I was almost positive the war would stop, but today . . . Today a shell fell on the park in front of my house, the park where I used to play and sit with my girlfriends. A lot of people were hurt. Dado, Jaca and her mother have come home from the hospital, Selma lost a kidney but she’s still in the hospital. AND NINA IS DEAD. A piece of shrapnel lodged in her brain and she died. She was such a sweet, nice little girl. We used to play together in the park. Is it possible I’ll never see Nina again? Nina, an innocent eleven-year-old little girl–the victim of a stupid war. I feel sad. I cry and wonder why? She didn’t do anything. A disgusting war has destroyed a young child’s life. Nina, I’ll always remember you as a wonderful little girl.

Wednesday, May 27, 1992

SLAUGHTER! MASSACRE! HORROR! CRIME! BLOOD! SCREAMS! TEARS! DESPAIR!

That’s what Vaso Miskin Street looks like today. Two shells exploded in the street and one in the market. Mommy was nearby at the time. She ran to Grandma and Granddad’s. Daddy and I were beside ourselves because she hadn’t come home. I saw some of it on TV but I still can’t believe what I actually saw. It’s unbelievable. I’ve got a lump in my throat and a knot in my tummy. HORRIBLE. They’re taking the wounded to the hospital. It’s a madhouse. We kept going to the window hoping to see Mommy. We didn’t know what had happed to her. Was she alive? At 4:00, Daddy decided to go and check the hospital. I looked out the window one more time and. . . I SAW MOMMY RUNNING ACROSS THE BRIDGE. As she came into the house she started shaking and crying. Through her tears she told us how she had seen dismembered bodies. All the neighbors came because they had been afraid for her. Thank God, Mommy is with us. Thank God. A HORRIBLE DAY. UNFORGETTABLE. HORRIBLE! HORRIBLE! I don’t know how often I’ve written that word. HORRIBLE. We’ve had too much horror. The days here are full of horror. Maybe we in Sarajevo could rename the day and call it horror, because that’s really what it’s like.

Monday, June 29, 1992

BOREDOM!!! SHOOTING!!! SHELLING!!! PEOPLE BEING KILLED!!! DESPAIR!!! HUNGER!!! MISERY!!! FEAR!!!

That’s my life! The life of an innocent eleven-year-old schoolgirl!! A schoolgirl without a school, without the fun and excitement of school. A child without games, without friends, without the sun, without birds, without nature, without fruit, without chocolate or sweets, with just a little powdered milk. In short, a child without a childhood. A wartime child. I now realize that I am really living through a war, I am witnessing an ugly, disgusting war. I and thousands of other children in this town that is being destroyed, that is crying, weeping, seeking help, but getting none. God, will this ever stop, will I ever be a schoolgirl again, will I ever enjoy my childhood again? I once heard that childhood is the most wonderful time of your life. And it is. I loved it, and now an ugly war is taking it all away from me. Why? I feel sad. I feel like crying. I am crying.

Thursday, November 19, 1992

Nothing new on the political front. They are adopting some resolutions, the “kids” are negotiating, and we are dying, freezing, starving, crying, parting with our friends, leaving our loved ones.

I keep wanting to explain these stupid politics to myself, because it seems to me that politics caused this war, making it our everyday reality. It looks to me as though these politics mean Serbs, Croats and Muslims. But they are all people. They are all the same. They all look like people, there’s no difference. They all have arms, legs and heads, they walk and talk, but now there’s “something” that wants to make them different.

Among my girlfriends, among our friends, in our family, there are Serbs and Croats and Muslims. It’s a mixed group and I never knew who was a Serb, a Croat or a Muslim. Now politics has started meddling around. It has put an “S” on Serbs, and “M” on Muslims and a “C” on Croats, it wants to separate them. And to do so it has chosen the worst, blackest pencil of all – the pencil of war which spells only misery and death.

Of course, I’m “young,” and politics are conducted by “grown-up.” But I think we “young” would do it better. We certainly wouldn’t have chosen war.

Friday, July 23, 1993

Ever since July 17, various people have been coming around – journalists, reporters, cameramen. From Spain, France, the US, England . . . and yesterday a crew came from ABC News. They filmed me for American TV as the “person of the week.” Hey, imagine, me a personality?

They filmed me in my room, by my piano, in my apartment with my parents. They talked to me. In English, of course. I have to boast and tell you that they told me my English is EXCELLENT.

And tonight the world will be looking at me. Meanwhile I’m looking at the candle, and all around me is darkness. I’m looking in the dark.

Can that outside world see the darkness I see? Just as I can’t see myself on TV tonight, so the rest of the world probably can’t see the darkness I’m looking at. We’re at two ends of the world. Our lives are so different. Theirs is a bright light. Ours is darkness.

Friday, September 17, 1993

The “kids” are negotiating something, signing something. Again giving us hope that this madness will end. There’s supposed to be a cease-fire tomorrow and on September 21 at Sarajevo airport everybody is supposed to sign FOR PEACE. Will the war stop on the day that marks the change from one season to another???

With all the disappointments I’ve had with previous truces and signatures, I can’t believe it.

I can’t believe it because another horrible shell fell today, ending the life of a three-year-old little boy, wounding his sister and mother.

All I know is that the result of their little games is 15,000 dead in Sarajevo, 3,000 of them children, 50,000 permanent invalids, whom I already see in the streets on crutches, in wheelchairs, armless and legless. And I know that there’s no room left in the cemeteries and parks to bury the latest victims.

Maybe that’s why this madness should stop.

Sunday, October 17, 1993

Yesterday our friends in the hills reminded us of their presence and that they are now in control and can kill, wound, destroy . . . yesterday was a truly horrible day.

Five hundred and ninety shells. From 4:30 in the morning on, throughout the day. Six dead and fifty-six wounded. That is yesterday’s toll.

AGAIN! Again and again they keep sinking all our boats, taking and burning all our hopes. People said that they wouldn’t do it anymore. That there would soon be an end to it, that everything would resolve itself. THAT THIS STUPID WAR WOULD END!

Oh God, why do they spoil everything? Sometimes I think it would be better if they kept shooting, so that we wouldn’t find it so hard when it starts up again. This way, just as you relax, it starts up AGAIN. I am convinced now that it will never end. Because some people don’t want it to, some evil people who hate children and ordinary folk.

I keep thinking that we’re alone in this hell, that nobody is thinking of us, nobody is offering us a helping hand. [No] . . . People worry about us, they think about us, but as sub-humans. They want to destroy us. Why? I keep asking myself why?

We haven’t done anything. We’re innocent. But helpless! . . . some evil people hate children and ordinary folk.
```

---

## IC-2357: 23 Minutes in Hell

- Title: 23 Minutes in Hell
- Author (byline): Bill Wiese
- Work: Not specified
- Publisher: Charisma House
- Publication date as stated: Jan 2006
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1679
- Already set (do not supply): none

### Source block (context only)

```text
Author: Bill Wiese
ISBN: 978-1591858829
Publisher: Charisma House
Date (Month/Year): Jan 2006
```

### Introduction (context only: never use it for content warnings)

```text
Hell is a place of desolation, agony, and never-ending suffering. It is everything God is not, because God is truly absent from that place. In this book, we hear a man’s account of what he truly saw and felt in this place of torment.

23 Minutes in Hell by Bill Wiese
```

### Performance text (classify this)

```text
On Sunday, November 22, 1998 my wife, Annette and I spent the evening at the home of one of our closest friends. There was nothing unusual about that night. Annette and I headed home around 11:00 PM, and we fell into bed shortly before midnight, unaware that my life was about to be changed forever by an event I still find hard to explain. Suddenly at 3:00 AM on the 23rd, without any notice, I found myself being hurled through the air and then was falling to the ground completely out of control.

I landed in what appeared to be a prison cell. The walls of the cell were made out of a roughhewn stone and had a door made what appeared to be thick metal bars. I was completely naked which added to the vulnerability of a captive. This was not a dream - I realized I was actually in the strange place fully awake and cognizant. I had no idea what happened, how I had traveled, or why I was there until it was shown to me and explained later during my journey.

As I lay there on the floor of that cell, I felt extremely weak. I noticed I had a body; one appeared just as it is now. Lifting my head, I began to look around, immediately I realized that I was not alone in the cell. I saw two enormous beasts unlike anything I’ve ever seen before. These creatures were approximately 10 to 13 feet tall. These towering beasts were far, far beyond intimidating. It is one thing to be threatened by someone much taller than you. But these creatures were not of this natural world. I recognize that they were entirely evil, and were gazing at me with pure, unrestrained hatred, which completely paralyzed me with fear. ‘Evil’ and ‘Terror’ stood before me. Those creatures were on intensely concentrated manifestation of those 2 forces. The creatures weren’t animals, but they weren’t human either. Each giant beast resembled a reptile in appearance but took on human form. Their arms and legs were unequal in length, out of proportion – without symmetry. The first one had bones and scales all over its grotesque body. It had a huge protruding jaw, gigantic teeth, and large sunken-in eyes. This creature was stout and powerful with big legs abnormally large feet. It was pacing violently around the cell like a caged bull, and its demeanor was extremely ferocious. The second beast was taller and thinner with very long arms and razor-sharp fins that covered its body. Protruding from its hands were claws that were nearly a foot long. Its personality seemed different from the first being. It was certainly no less evil but it remained a rather still.

One of the creatures picked me up. The strength of the beast was amazing. I was comparable to the weight of a water glass in its hand. Then the beast threw me against the wall. It felt as though every bone in my body had been broken. The second beast with its razor like claws and sharp protruding fins then grabbed me from behind. As it pressed me into its chest, its sharp fins pierced my back. I knew that I could not escape this torture via death for not even that was an option. Death penetrated me but eluded me. No mercy existed in that place. Mercy is from God in heaven.

I was extremely nauseous from that terrible foul stench coming from these creatures. It was absolutely disgusting, foul, and rotten. If you could take every rotten thing you can imagine such as an open sewer, sour milk, rotting flesh, and sulfur, and magnify it 1000 times you might come close. The odor was extremely toxic and that alone should have killed me.

Somehow, I managed to move a bit and dragged myself across the ground toward the barred door. I finally made it to the door and crawled out of the cell. Apparently, the creatures allowed me to crawl out without stopping me.

All I could think of was to get up onto my feet. However, every move to get up took great effort. I remember wondering “Why is this so difficult’? After tremendous exertion, I was finally able to stand. I was thoroughly exhausted, and, at the same time, very frustrated at how hard simple movement had become.

I was horrified as I heard the screams of an untold multitude of people crying out in torment. Through the panic and the deafening noise, I struggled to gather my thoughts. “I’m in hell! This is a real place, and I’m actually here!” I frantically tried to understand, but it was just so inconceivable. This place was so terrifying, so intense, and so hostile that it would be impossible for me to exaggerate the horror.

As I stood outside the cell, I actually felt the darkness. It was not like the darkness on earth. I was once in a coal mine in Arizona that was completely void of light. I couldn’t see anything, yet it was nothing like the darkness in hell. It was as though the darkness had its own power, a power that consumed me. The darkness was not simply the absence of light—it had a distinctive evil presence, a feeling of death, of penetrating evil.

I looked off to my right and could faintly see flames from afar off that dimly lit the skyline. I knew the flames were coming from a large pit, a gigantic raging inferno approximately one mile in diameter and about ten miles away. This was just one of the many things I simply knew. My senses were keener.

The only visible area was that which the flames exposed. The ground was all rock, barren and desolate. There was not one green thing, not one living thing, not one blade of grass, not one leaf on the ground—it was just a complete wasteland.

The air was filled with smoke, and a filthy, deathly, decaying odor hung in the oxygen-depleted atmosphere. It seemed as if all the oxygen had been sucked up by the high leaping flames in the distance. I could barely breathe. The lack of oxygen in the atmosphere left me gasping for every little bit of air I could inhale. There was no humidity or moisture in the air. It was exhausting even to try to get just one breath.

One of the worst sensations I experienced was an insatiable thirst and dryness. I was so extremely thirsty. My mouth was so dry it felt as if I had been running through the desert for days. There was no water, no humidity in the air, no water anywhere. I desperately longed for just one drop of water.

One of the demonic creatures grabbed me and carried me back into the cell. It threw me on the floor; when, all of a sudden, I was taken back out of the cell and placed next to that pit of fire I had viewed from a distance earlier.

Momentary relief hit my soul as I realized I had been snatched from the grip of those hideous creatures. However, now I found myself next to an enormous pit with raging flames of fire leaping high into an open cavern. As I looked up into that dark, eerie, tomb-like atmosphere, it seemed to be like a mouth that had swallowed her dead. The flames of her ravenous appetite were never satisfied with the pitiful screams of untold multitudes.

The heat was far beyond unbearable, and I desperately wanted to escape before I too would be thrown into that inferno. As I look back on this experience now, I am reminded of the devastation of the twin towers of the World Trade Center of September 11, 2001, when some people, rather than facing the 2000-degree heat, chose to plummet to their death by leaping out a window. A fall, especially from such great heights, must have been horrendous. It was reported that a person subjected to that temperature would be completely incinerated in about fifteen seconds. Those people chose to make that leap rather than face the intensity of those flames for even fifteen seconds. Some scientists have reported that the core temperature at the center of the earth is approximately twelve thousand degrees. To endure that for an eternity is unfathomable.

I also experienced the misery of total exhaustion in hell. The continual emotional, mental, and physical trauma feeds this vicious cycle of sleep deprivation. You desperately long for even a few minutes of rest, but you never, ever get that privilege. In hell, you never sleep, rest, or find a quiet moment. And form of rest is completely nonexistent. Even though I was only there for 23 minutes, the torment and trauma were so intense that it felt like I hadn’t slept for weeks.

Now, it’s true that there are areas in this vast, fiery pit where people are thrown together, but they are only ‘together’ in the sense that they are all experiencing the same torment. Each person is very isolated in extreme agony and screaming in fear as fire and brimstone rain down upon him. They are ‘together’ in the same way cattle are herded into a slaughterhouse. A soul in such extreme agony would have no opportunity for a conversation. Besides, I believe that everyone is just on the verge of insanity. However, I believe you never quite go insane, for that would provide a form of escape. And there is no escape, even mentally.

Suddenly, I began ascending. I didn’t know how I was able to ascend or why. You see, the demons cannot harm God directly, but they can hurt His children and His creation. It saddens God to see His creation suffer. The Lord loves us and wants us to live healthy, peaceful, long lives. He wants us to warn more people about hell and to share with them just what they need to do to avoid that terrible place.
```

---

## IC-2358: 32 Third Graders and One Class Bunny

- Title: 32 Third Graders and One Class Bunny
- Author (byline): Phillip Done
- Work: Not specified
- Publisher: Touchstone
- Publication date as stated: Sept 2009
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: PHILLIP
- Teaser before the introduction: Yes
- Spoken words (computed): 1048
- Already set (do not supply): none

### Source block (context only)

```text
Author: Phillip Done
ISBN: 978-0743272407
Publisher: Touchstone
Date (Month/Year): Sept 2009
```

### Introduction (context only: never use it for content warnings)

```text
You were guessing something else, right? Well, I’m here to tell you that more men should become teachers - especially in elementary schools.

Want to do something really tough and brave? Something to change the world? Something adventurous . . . something really different? Well, you could join the Marines, or you could join the ranks of the Few. The proud. The male elementary school teachers!

PS: 95% of the adults you work with will be WOMEN!!

(wink)

32 Third Graders and One Class Bunny by Phillip Done.
```

### Performance text (classify this)

```text
I read Charlotte’s Web and Charlie and the Chocolate Factory every year, and every year when Charlie finds the golden ticket and Charlotte dies, I cry. I know when a child has gum in his mouth even when he is not chewing. I have sung “Happy Birthday” 657 times. I fix staplers that won’t staple and zippers that won’t zip, and I poke pins in the orange caps of glue bottles that will not pour. I hand out papers and pencils and stickers and envelopes for newly pulled teeth . . . I am a teacher.

I plan lessons while shaving, showering, driving, eating, and sleeping. I plan lessons five minutes before the bell rings. I know what time it is when the big hand is on the twelve and the little hand is on the nine. I say the r in library. I do not say the w in sword. . . I am a teacher.

I put on Band-Aids and winter coats and school plays. I wear four-leaf clovers and dandelions in my shirt pocket that have just been picked with love at recess. I pray for snow days. I pray for Stephen to be absent.

I buy books about cats and dogs and sharks and volcanoes and horses and dinosaurs. I turn jump ropes and am base in tag. I am glad you can only get chicken pox once. . . I am a teacher.

I correct pencil grips and spelling mistakes and bad manners. I push in chairs all the way, push swings higher, and push sleeves up while children are painting. I can touch the paper cutter.

******* I am a teacher . . . and I used to laminate everything, absolutely everything – posters, prints, bookmarks, birthday certificates, awards, library passes, name tags, file folders, book jackets, real estate calendars. You name it, I laminated it. They called me the laminating king.

It got pretty bad. Once Cathy sent me a note with a question. Attached was a sticky note. It said, “Please just answer question. Do not laminate.” But now I won’t go near the machine. Not even close. You see, one night I was in the staff room laminating my kids’ art for Back-to-School Night. It was late.

Now, you know what a laminating machine looks like of course. It’s about three feet wide and sits on a table. It has two big rolls of plastic. You put whatever it is you want to laminate in on one side. The paper rolls through the two big rolls of laminating plastic. The plastic is hot and adheres to the paper. And your paper comes out on the other side all nicely laminated. It’s great.

So there I was, carefully guiding each piece of artwork into the laminator, humming along, when all of a sudden, (begin pantomime) I felt this tug! I looked down. My tie was caught in the machine!

Immediately, I pulled back, but the tie was stuck. I tugged again. Still nothing. I jerked a third time. No luck. Meanwhile, I was still rolling into the machine. Oh my God, I thought. I am going to die!

I could see the headlines:
TEACHER FLATTENED IN LAMINATING MACHINE
TECHER SUFFOCATES TO DEATH IN HOT PLASTIC
JC PENNEY RECALLS ONE MILLION TIES

I slammed off the switch. It kept rolling. (screaming) Crap! It was the heat button. I pushed another button. It started rolling faster. (yelling) Nooooo! I reached under the table and fumbled for the cord. I found it. Thank God! I yanked it as hard as I could. Suddenly everything stopped.

I sighed, closed my eyes, and rested my chin on the edge of the table. I didn’t move for about ten seconds. My head was about five inches away from the roller.

(thinking out loud) How the hell am I going to get out of this thing? I couldn’t undo my tie. The skinny part in the back had gone through too. Then I spotted some scissors on the counter. I tried to reach them, but they were too far away. Damn! What was I going to do?

(softly) Helloooooo . . . . Hellooooo. Nobody answered. Oh my God, I thought. If I don’t get out of here, the other teachers will find me here in the morning. I yelled louder.

(yelling louder) Heeelp! Heeeeelp!

Finally, after about ten minutes of screaming at the top of my lungs, Marion walked into the room.

PHILLIP: Don’t laugh! Get me out of this thing! Grab those scissors over there and cut the tie. Just get me out of here! And stop laughing! It’s not funny.

Marion cut the tie and I was saved. That night I made her swear to not tell a soul. But Marion is not good at keeping secrets. For weeks afterward, strangers would pass me in the supermarket, at the gas station – everywhere – point to my tie and start cracking up.

I called my dad and told him the whole story. He couldn’t stop laughing either. Until I told him it was his tie!

*******

(regaining his composure from the beginning of the selection) I am a teacher. . . I own one suit, two pairs of shoes, and eight boxes of graham crackers. I have every teacher mug that Hallmark ever made and every Save the Children tie too. I say, “Use two hands!” when they carry their lunch trays. I say, “Accidents happen,” after they did not use two hands.

I sign library passes and yearbooks and new casts. I attend soccer games and Little League championships and funerals for guinea pigs. I answer to both “Mom” and “Dad.” . . . I am a teacher.

I hope April Fool’s Day is on a Saturday. I have worn green marker, red paint, yellow chalk dust, glue stick, and glitter all on the same day. I hate glitter.

I can make a telescope out of a toilet paper roll and a totem pole out of oatmeal boxes. I can make snowflakes out of coffee filters and a space shuttle out of a Pringles can too. [But] I can only say my ABCs if I sing them. . . I am a teacher.

I call on children whose hands are not raised. I know when a child does not understand. I know when a child is not telling the truth. I know when a child was up too late last night. I know when a child needs help finding a friend.

I am a teacher . . .
```

---

## IC-2359: 8 Simple Rules for Dating My Teenage Daughter

- Title: 8 Simple Rules for Dating My Teenage Daughter
- Author (byline): W. Bruce Cameron
- Work: 8 Simple Rules for Dating My Teenage Daughter: And other tips from a beleaguered father [not that any of them work] Pg 229
- Publisher: Workman Publishing Company
- Publication date as stated: March 2002
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 699
- Already set (do not supply): none

### Source block (context only)

```text
Author: W. Bruce Cameron
Book: 8 Simple Rules for Dating My Teenage Daughter:
And other tips from a beleaguered father [not that
any of them work] Pg 229
ISBN: 978-0761126331
Publisher: Workman Publishing Company
Date (Month/Year): March 2002
```

### Introduction (context only: never use it for content warnings)

```text
It seems to happen overnight. One minute your daughter is wearing bunny slippers and demanding bedtime stories. The next, she’s wearing a midriff-baring tee shirt (WOLF WHISTLE), demanding the car keys and wanting to go out ALONE with guys like me. And while, as a teenager, I have difficulty understanding your discomfort; I have a feeling your innermost thoughts may run something like this:

8 Simple Rules for Dating my Daughter by W. Bruce Cameron.
```

### Performance text (classify this)

```text
(Pg 229+) Whenever boys come over to date my daughter, I do my best to give them the impression that if they were looking for fun, they should have picked some other girl. My motto: wilt 'em in the living room and they'll stay wilted all night. To assist their understanding, I have come up with some basic rules, which I have carved into two stone tablets on display in my living room.

Rule One: If you pull into my driveway and honk you'd better be delivering a package, because you're sure as heck not picking anything up.

Rule Two: You do not touch my daughter in front of me. You may glance at her, so long as you do not peer at anything below her neck. If you cannot keep your eyes or hands off of my daughter's body, I will remove them.

Rule Three: I am aware that it is considered fashionable for boys of your age to wear their trousers so loosely that they appear to be falling off their hips. Please don't take this as an insult, but you and all of your friends are complete idiots. Still, I want to be fair and open minded about this issue, so I propose this compromise: You may come to the door with your underwear showing and your pants ten sizes too big, and I will not object. However, In order to assure that your clothes do not, in fact, come off during the course of your date with my daughter, I will take my electric staple gun and fasten your trousers securely in place around your waist.

Rule Four: I'm sure you've been told that in today's world, sex without utilizing a "barrier method" of some kind can kill you. Let me elaborate: when it comes to sex, I am the barrier, and I WILL kill you.

Rule Five: You may believe that in order for us to get to know each other, we should talk about sports, politics, and other issues of the day. Please do not do this. The only information I require from you is an indication of when you expect to have my daughter safely back at my house, and the only word I need from you on this subject is "early."

Rule Six: I have no doubt you are a popular fellow, with many opportunities to date other girls. This is fine with me as long as it is okay with my daughter. Otherwise, once you have gone out with my little girl, you will continue to date no one but her until she is finished with you. If you make her cry, I will make YOU cry.

Rule Seven: As you stand in my front hallway, waiting for my daughter to appear, and more than an hour goes by, do not sigh and fidget. If you want to be on time for the movie, you should not be dating. My daughter is putting on her makeup, a process which can take longer than painting the Golden Gate Bridge. Instead of just standing there, why don't you do something useful, like changing the oil in my car?

Rule Eight: The following places are not appropriate for a date with my daughter: • Places where there are beds, sofas, or anything softer than a wooden stool. • Places where parents, policemen, or nuns are not within eyesight. • Places where there is darkness. • Places where there is dancing, holding hands, or happiness. • Places where the ambient temperature is warm enough to induce my daughter to wear shorts, tank tops, midriff T-shirts, or anything other than a goose down parka zipped up to her chin. • Movies with a strong romantic or sexual theme are to be avoided; movies which feature chain saws are okay.

My daughter claims it embarrasses her to come downstairs and find me attempting to get her date to recite these eight simple rules from memory. I'd be embarrassed too--there are only eight of them, for crying out loud!

My wife says I'm being too hard on the boys. "Don't you remember being that age?" she challenges. Of course, I remember. Why do you think I came up with the eight simple rules?
```

---

## IC-2360: Ace Lacewing: Bug Detective

- Title: Ace Lacewing: Bug Detective
- Author (byline): David Biedrzycki
- Work: Not specified
- Publisher: Charlesbridge
- Publication date as stated: July 2005
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: MAYOR, XERCES, SGT ZITO, MAGGOT, DRONE BEE, ACE, MANTIS, UNIDENTIFIED DRONE, PRINCESS POLLEN
- Teaser before the introduction: Yes
- Spoken words (computed): 1346
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
It was a night like any other night in the city. Hot and sticky. Great weather if you’re a bug. Everyone’s a bug in Motham City. Some good, some bad. Bad bugs are my business. I was in my office eating some aphid lo mein when the phone buzzed. I answered it. “Ace Lacewing, Bug Detective.”

It was Mayor Buzzbee. Behind him it sounded like a beehive of activity. Actually, it was a beehive. “What’s the buzz?”

MAYOR: Ace! I’m at the Hive Rise with Princess Pollen. Queenie Bee’s been kidnapped. Get over here now! Queenie Bee kidnapped? Who would do a thing like that? Everyone loved Queenie and her sister Princess Pollen. The Hive Rise Honey Company made the best honey in town. Maybe someone thought it was too good . . . I was just about to fly out the door when I saw her standing there, like a moth drawn to a flame. The lovely rare butterfly, Doctor Xerces Blue. Not the kind of doctor who takes your tonsils out. The kind of doctor who studies bugs – dead bugs.

XERCES: Oh, Acie. How about dinner at my place tonight? Just you and me. I’m making your favorite – aphids a la mode. “The aphids will have to stew, sweetheart. Queenie Bee’s in a honey of a jam!” . . . Downtown the traffic was crawling.

SGT ZITO: Hey, Ace! It was Sergeant Zito, a mosquito. And a cop. I’ve known him ever since we were pupae at the same school. “Whadda ya know, Zito?”

SGT ZITO: We have a couple of witnesses, Ace. But none of them are talking except this little maggot.

MAGGOT: I saw the whole thing! I was crawling around minding my own business when all of a sudden I heard all this screamin’. I looked up and I saw ‘em right outside the Hive Rise – a couple of hooded bugs running off with Queenie Bee! “Which way did they go?” . . . I should have known better than to ask directions from a bug with no arms or legs. I told Zito to start rounding up suspects. I looked around . . . and noticed a suspicious trail of honey leading away from the crime scene. I followed it. At the corner of Tomato and Vine, I stopped in my tracks. The honey trail led to the Beetle Zoo. Lacewings have lost their heads to beetles. But I was on a case. It was Hive Rise Honey, all right. Still warm. I heard a noise, stood up, and froze! Someone had let the tiger beetle out of his cage, and this guy didn’t want to play! He wanted to eat. I did the only thing a bug detective worth his wings would do. I screamed and ran . . . smack into a wall. Ahhh, it could have been worse. It could have been a windshield on the interstate. [When I came to] I was lying in a corner of the police station. A bunch of handcuffed roaches and other pests were waiting to be questioned. Everyone had an alibi. The roaches said of course they ran from the scene of the crime – it was their nature to scatter when the lights go on.

Before we could question the cicada, he molted and flew out the window. Twig couldn’t have run anywhere. He was a walking stick. We brought in Smooch, the assassin bug. No one wanted to get near his kisser. We decided to call it a night.

DRONE BEE: Psssssst! Hey, Lacewing. I know who’s got Queenie and why.

ACE: Who are you?

DRONE BEE: A drone who knows the truth. But there are too many eyes and too many antennae around here. Let’s go someplace we can talk in private . . . We never got the chance. It happened quick as a cricket – a drive-by gassing. “Hit the dirt!” But it was too late for the bee. I couldn’t make out the driver, but the other one was no doubt a bombardier beetle. I could tell by the smell. I wondered if he had a license to pass gas. I checked the bee. He wasn’t moving, but he was trying to say something. I lowered my ear to his mouth . . . . Al the Drone.

SGT ZITO: Al the Drone? Oh no, not Al the Drone! Please don’t let it be Al the Drone. Anybody but Al the Drone . . . Who’s Al the Drone?

Al the Drone owns Drone HoneyWorks. Some bugs say he has his sticky little mandibles in more than just honey. I think we should pay Mr. Drone a visit. Xerces worked on the bee as Zito and I took off across town. Outside Drone HoneyWorks, the smell of honey hung thicker in the air than ants on a popsicle stick. Savage mantises kept guard. The back gate of the Beetle Zoo was right across the street. And the trail of honey led from the zoo to the HoneyWorks! We needed a way in. But how? Two dung beetles were making their way up the street, rolling their dung ball and collecting trash. They rolled up next to us. The dung beetles were too busy to notice us.

ACE: (to Zito) “You thinkin’ what I’m thinkin’?”

SGT ZITO: Oh no, Ace, not the dung. “Hold your breath!” We leapt onto the dung ball and rolled right past a mantis into the HoneyWorks. I peered in a window. What I saw made my antennae quiver. In the shadows I saw someone tied up and blindfolded. It looked like Queenie. She sure wasn’t getting the royal treatment here.

SGT ZITO: Uh . . . . Ace? We got company . . .

One of the mantises had followed our dung prints. He didn’t look too happy. Neither were we when he tied us up and carried us inside. Inside, the aroma of honey and pollen was sickeningly sweet. I’ve been in hives before. You can tell a good hive by the buzz of the bees. The buzz in here was not good. The mantis looked as if he were in a trance as he toted us past rows and rows of honeycomb. Standing in the shadows was Al the Drone . . . [or was it?]

MANTIS: Hey, boss. Look what I found snoopin’ around outside.

UNIDENTIFIED DRONE: Well, well, if it ain’t the little lacewing and his blood-sucking friend.

ACE: I know you got Queenie here, Drone. You’ll never get away with it!

UNIDENTIFIED DRONE: Funny, that’s the same thing Queenie said to me, and look where she is now. I couldn’t believe my eyes. Queenie was stuffed into a honeycomb, alive but not for long. If Queenie was holding her breath in the honeycomb, then who was tied up in the next room? Who was the mystery bug in the shadows? And why did the Drone smell of pollen? . . . .

Pollen! That was it! The clues clicked together in my head.

UNIDENTIFIED DRONE: Any last words, Lacewing? “Yeah. Since when do drones gather pollen?” The whole place went quiet.

PRINCESS POLLEN: Ha, you’re clever, Lacewing. Clever, clever, clever.

SGT ZITO: P-p-princess P-pollen?!

PRINCESS POLLEN: In the exoskeleton! . . . I’m sick of just being princess!! I want to be QUEEN! It’s always Queenie Bee this and Queenie Bee that. I’ll never have my own hive with her around. So I’m making it look like sleazy Al the Drone got rid of her. You guessed it, Lacewing – that’s him tied up in the back room. With Queenie and Drone HoneyWorks gone, I’ll be queen of the town. You’re in a rather sticky situation, Lacewing, so see ya, wouldn’t wanna bee ya! Princess Pollen made her way to the door. She signaled the mantises to seal us in the honeycombs. I had to think fast. Something fluttered overhead, so I shouted the only thing that makes a mantis run for cover. “BAT!!!” The mantis threw us high in the air. We soared helplessly until whatever was flying above grabbed us . . .It wasn’t a bat. It was Xerces. She had rounded up every cop from here to Termite Heights and brought them to the HoneyWorks, saving my wings again. Dawn was emerging like a monarch from a chrysalis when Xerces and I sat down for a plate of aphids a la mode. “Here’s to blue wings and my favorite things.”

And the city of Motham fluttered awake behind her.
```
