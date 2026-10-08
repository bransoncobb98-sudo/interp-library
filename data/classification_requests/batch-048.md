# Classification request: batch 48 of 63 (40 records, IC-1881 to IC-1920)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-048-reply.json`.

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

## IC-1881: The Congo: A Study of the Negro Race

- Title: The Congo: A Study of the Negro Race
- Author (byline): Vachel Lindsay
- Work: Not specified
- Publisher: Dover Publications
- Publication date as stated: Sept 1992
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1260
- Already set (do not supply): none

### Source block (context only)

```text
Author: Vachel Lindsay
ISBN: 978-0486272726
Publisher: Dover Publications
Date (Month/Year): Sept 1992
```

### Introduction (context only: never use it for content warnings)

```text
Vachel Lindsay is often ignored in analogies of twentieth-century poetry because he is judged to be exceptionally reactionary in his racism. However, when Lindsay justified his pacifism during World War I, he said he would rather have died "of his own will mounting a blazing pyre . . . by the side or in place of some black who had not trial by jury" than in the trenches.” He held a conviction that "the only way to end lynching would be to thrust yourself into the thick of such a mob and make the men slay you instead of the Negro. Was Lindsay too controversial for America nearly 100 years ago? Is he too controversial for America today . . . or does he perhaps provide and insight into the cultural history of African Americans which is too seldom recognized? The Congo by Vachel Lindsay.
```

### Performance text (classify this)

```text
I. Their Basic Savagery Fat black bucks in a wine-barrel room, Barrel-house kings, with feet unstable,

# A deep rolling bass. #
Sagged and reeled and pounded on the table,
Pounded on the table,
Beat an empty barrel with the handle of a broom,
Hard as they were able,
Boom, boom, BOOM,
With a silk umbrella and the handle of a broom,
Boomlay, boomlay, boomlay, BOOM.
THEN I had religion, THEN I had a vision.
I could not turn from their revel in derision.

# More deliberate. Solemnly chanted. #
THEN I SAW THE CONGO, CREEPING THROUGH THE
BLACK,
CUTTING THROUGH THE FOREST WITH A GOLDEN
TRACK.
Then along that riverbank
A thousand miles
Tattooed cannibals danced in files;
Then I heard the boom of the blood-lust song

# A rapidly piling climax of speed and racket. #
And a thigh-bone beating on a tin-pan gong.
And "BLOOD" screamed the whistles and the fifes of
the warriors,
"BLOOD" screamed the skull-faced, lean witch-doctors,
"Whirl ye the deadly voo-doo rattle,
Harry the uplands,
Steal all the cattle,
Rattle-rattle, rattle-rattle,
Bing.
Boomlay, boomlay, boomlay, BOOM,"

# With a philosophic pause. #
A roaring, epic, rag-time tune
From the mouth of the Congo
To the Mountains of the Moon.
Death is an Elephant,

# Shrilly and with a heavily accented metre. #
Torch-eyed and horrible,
Foam-flanked and terrible.
BOOM, steal the pygmies,
BOOM, kill the Arabs,
BOOM, kill the white men,
HOO, HOO, HOO.

# Like the wind in the chimney. #
Listen to the yell of Leopold's ghost
Burning in Hell for his hand-maimed host.
Hear how the demons chuckle and yell
Cutting his hands off, down in Hell.
Listen to the creepy proclamation,
Blown through the lairs of the forest-nation,
Blown past the white-ants' hill of clay,
Blown past the marsh where the butterflies play: --
"Be careful what you do,

# All the”o” sounds very golden. Heavy accents

very heavy. Light accents very light.

Last line whispered. #
Or Mumbo-Jumbo, God of the Congo,
And all of the other
Gods of the Congo,
Mumbo-Jumbo will hoo-doo you,
Mumbo-Jumbo will hoo-doo you,
Mumbo-Jumbo will hoo-doo you."

II. Their Irrepressible High Spirits

# Rather shrill and high. #
Wild crap-shooters with a whoop and a call
Danced the juba in their gambling-hall
And laughed fit to kill, and shook the town,
And guyed the policemen and laughed them down
With a boomlay, boomlay, boomlay, BOOM.

# Read exactly as in first section. # THEN I SAW THE CONGO, CREEPING THROUGH THE BLACK, CUTTING THROUGH THE FOREST WITH A GOLDEN TRACK.

# Lay emphasis on the delicate ideas. Keep as light-

footed as possible. #
A negro fairyland swung into view,
A minstrel river
Where dreams come true.
The ebony palace soared on high
Through the blossoming trees to the evening sky.
The inlaid porches and casements shone
With gold and ivory and elephant-bone.
And the black crowd laughed till their sides were sore
At the baboon butler in the agate door,
And the well-known tunes of the parrot band
That trilled on the bushes of that magic land.

# With pomposity. #
A troupe of skull-faced witch-men came
Through the agate doorway in suits of flame,
Yea, long-tailed coats with a gold-leaf crust
And hats that were covered with diamond-dust.
And the crowd in the court gave a whoop and a call
And danced the juba from wall to wall.

# With a great deliberation and ghostliness. # But the witch-men suddenly stilled the throng With a stern cold glare, and a stern old song: -- "Mumbo-Jumbo will hoo-doo you." . . .

# With overwhelming assurance, good cheer, and

pomp. #
Just then from the doorway, as fat as shotes,
Came the cake-walk princes in their long red coats,
Canes with a brilliant lacquer shine,
And tall silk hats that were red as wine.

# With growing speed and sharply marked dance-

rhythm. #
And they pranced with their butterfly partners there,
Coal-black maidens with pearls in their hair,
Knee-skirts trimmed with the jassamine sweet,
And bells on their ankles and little black feet.
And the couples railed at the chant and the frown
Of the witch-men lean, and laughed them down.
(O rare was the revel, and well worth while
That made those glowering witch-men smile.)
The cake-walk royalty then began
To walk for a cake that was tall as a man
To the tune of "Boomlay, boomlay, BOOM,"

# With a touch of negro dialect, and as rapidly as

possible toward the end. #
While the witch-men laughed, with a sinister air,
And sang with the scalawags prancing there: --
"Walk with care, walk with care,
Or Mumbo-Jumbo, God of the Congo,
And all of the other
Gods of the Congo,
Mumbo-Jumbo will hoo-doo you.
Beware, beware, walk with care,
Boomlay, boomlay, boomlay, boom.
Boomlay, boomlay, boomlay, boom,
Boomlay, boomlay, boomlay, boom,
Boomlay, boomlay, boomlay,
BOOM."

# Slow philosophic calm. # Oh rare was the revel, and well worth while That made those glowering witch-men smile.

III. The Hope of their Religion

# Heavy bass. With a literal imitation of camp-

meeting racket, and trance. #
A good old negro in the slums of the town
Preached at a sister for her velvet gown.
Howled at a brother for his low-down ways,
His prowling, guzzling, sneak-thief days.
Beat on the Bible till he wore it out
Starting the jubilee revival shout.
And some had visions, as they stood on chairs,
And sang of Jacob, and the golden stairs,
And they all repented, a thousand strong
From their stupor and savagery and sin and wrong
And slammed with their hymn books till they shook the
room
With "glory, glory, glory,"
And "Boom, boom, BOOM."

# Exactly as in the first section. Begin with terror

and power, end with joy. # THEN I SAW THE CONGO, CREEPING THROUGH THE BLACK CUTTING THROUGH THE JUNGLE WITH A GOLDEN TRACK. And the gray sky opened like a new-rent veil And showed the apostles with their coats of mail. In bright white steele they were seated round And their fire-eyes watched where the Congo wound. And the twelve Apostles, from their thrones on high Thrilled all the forest with their heavenly cry: --

# Sung to the tune of "Hark, ten thousand harps and

voices". #
"Mumbo-Jumbo will die in the jungle;
Never again will he hoo-doo you,
Never again will he hoo-doo you."

# With growing deliberation and joy. #
Then along that river, a thousand miles
The vine-snared trees fell down in files.
Pioneer angels cleared the way
For a Congo paradise, for babes at play,
For sacred capitals, for temples clean.
Gone were the skull-faced witch-men lean.

# In a rather high key -- as delicately as possible. # There, where the wild ghost-gods had wailed A million boats of the angels sailed With oars of silver, and prows of blue And silken pennants that the sun shone through. 'Twas a land transfigured, 'twas a new creation. Oh, a singing wind swept the negro nation And on through the backwoods clearing flew: --

# To the tune of "Hark, ten thousand harps and

voices". #
"Mumbo-Jumbo is dead in the jungle.
Never again will he hoo-doo you.
Never again will he hoo-doo you."

Redeemed were the forests, the beasts and the men,
And only the vulture dared again
By the far, lone mountains of the moon
To cry, in the silence, the Congo tune: --

# Dying down into a penetrating, terrified whisper. #
"Mumbo-Jumbo will hoo-doo you,
Mumbo-Jumbo will hoo-doo you.
Mumbo . . . Jumbo . . . will . . . hoo-doo . . . you."
```

---

## IC-1882: Counting the Children

- Title: Counting the Children
- Author (byline): Dana Gioia
- Work: 99 Poems: New & Selected, Pgs 117-123
- Publisher: Graywolf Press
- Publication date as stated: April 2017
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1299
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dana Gioia
Book: 99 Poems: New & Selected, Pgs 117-123
ISBN: 978-1555977719
Publisher: Graywolf Press
Date (Month/Year): April 2017
```

### Introduction (context only: never use it for content warnings)

```text
What Mr. Choi discovers in the room of the deceased is decidedly unexpected. What would compel an adult woman to collect so many “children?”

The experience gives our narrator nightmares about the future of his own family.

What is your greatest fear? Growing old, abandonment, the death of a loved one?

Counting the Children by Dana Gioia
```

### Performance text (classify this)

```text
I.

"This must have been her bedroom, Mr. Choi. It's hard to tell. The only other time I came back here was when I found her body."

Neither of us belonged there. She lived next door. I was the accountant sent out by the State To take an inventory of the house.

When someone wealthy dies without a will, The court sends me to audit the estate. They know that strangers trust a man who listens.

The neighbor led me down an unlit hall. We came up to a double door and stopped. She whispered as if someone else were near.

"She used to wander around town at night And rifle through the trash. We all knew that. But what we didn't know about was them."

She stepped inside and fumbled for a switch. It didn't work, but light leaked through the curtains. "Come in," she said. "I want to show you hell."

I walked into a room of wooden shelves Stretching from floor to ceiling, wall to wall, With smaller shelves arranged along the center.

A crowd of faces looked up silently. Shoulder to shoulder, standing all in rows, Hundreds of dolls were lining every wall.

Not a collection anyone would want -- Just ordinary dolls salvaged from the trash With dozens of each kind all set together.

Some battered, others missing arms and legs, Shelf after shelf of the same dusty stare As if despair could be assuaged by order.

They looked like sisters huddling in the dark, Forgotten brides abandoned at the altar, Their veils turned yellow, dresses stiff and soiled.

Rows of discarded little girls and babies -- Some naked, others dressed for play -- they wore Whatever lives their owners left them in.

Where were the children who promised them love? The small, caressing hands, the lips which whispered Secrets in the dark? Once they were woken,

Each by name. Now they have become each other -- Anonymous except for injury, The beautiful and headless side by side.

Was this where all lost childhoods go? These dim Abandoned rooms, these crude arrangements staged For settled dust and shadow, left to prove

That all affection is outgrown, or show The uniformity of our desire?

How dismal someone else's joy can be.

I stood between the speechless shelves and knew Dust has a million lives, the heart has one. I turned away and started my report.

II.

That night I dreamt of working on a ledger, A book so large it stretched across my desk, Thousands of numbers running down each page.

I knew I had to settle the account, Yet as I tried to calculate the total, The numbers started slipping down the page,

Suddenly breaking up like Scrabble letters Brushed into a box to end a game, Each strained-for word uncoupled back to nil.

But as I tried to add them back together And hold each number on the thin green line Where it belonged, I realized that now

Nothing I did would ever fit together. In my hands even 2 + 2 + 2 No longer equaled anything at all.

And then I saw my father there beside me. He asked me why I couldn't find the sum. He held my daughter crying in his arms.

My family stood behind him in a row, Uncles and aunts, cousins I'd never seen, My grandparents from China and their parents,

All of my family, living and dead, A line that stretched as far as I could see. Even the strangers called to me by name.

And now I saw I wasn't at my desk But working on the coffin of my daughter, And she would die unless I found the sum.

But I had lost too many of the numbers. They tumbled to the floor and blazed on fire. I saw the dolls then -- screaming in the flames.

III.

When I awoke, I sat up straight in bed. The sweaty sheet was twisted in my hands.

My heart was pounding. Had I really screamed?

But no, my wife was still asleep beside me. I got up quietly and found my robe, Knowing I couldn't fall asleep again.

Then groping down the unlit hall, I saw A soft-edged light beneath my daughter's door. It was the night-light plugged in by her bed.

And I remembered when she was a baby, How often I would get up in the night And creep into that room to watch her sleep.

I never told my wife how many times I came to check each night -- or that I was Always afraid of what I might discover.

I felt so helpless standing by her crib, Watching the quiet motions of her breath In the half-darkness of the faint night-light.

How delicate this vessel in our care, This gentle soul we summoned to the world, A life we treasured but could not protect.

This was the terror I could not confess -- Not even to my wife -- and it was the joy My daughter had no words to understand.

So standing at my pointless watch each night In the bare nursery we had improvised, I learned the loneliness that we call love.

IV.

But I gave up those vigils years ago. My daughter's seven now, and I don't worry At least no more than any father does.

But waking up last night after the dream, Trembling in the hall, looking at her door, I let myself be drawn into her room.

She was asleep -- the blankets softly rising And falling with each breath, the faint light tracing The sleek unfoldings of her long black hair.

Then suddenly I felt myself go numb. And though you won't believe that an accountant Can have a vision, I will tell you mine.

Each of us thinks our own child beautiful, But watching her and marveling at the sheer Smoothness of skin without a scar or blemish,

I saw beyond my daughter to all children, And, though elated, still I felt confused Because I wondered why I never sensed

That thrill of joy when looking at adults No matter how refined or beautiful, Why lust or envy always intervened.

There is no tabula rasa for the soul. Each spirit, be it infant, bird or flower, Comes to the world perfected and complete,

And only time proves its unraveling. But I'm digressing from my point, my vision. What I meant to say is merely this:

What if completion comes only in beginnings? The naked tree exploding into flower? And all our prim assumptions about time

Prove wrong? What if we cannot read the future Because our destiny moves back in time, And only memory speaks prophetically?

We long for immortality, a soul To rise up flaming from the body's dust. I know that it exists. I felt it there,

Perfect and eternal in the way That only numbers are, intangible but real, Infinitely divisible yet whole.

But we do not possess it in ourselves. We die, and it abides, and we are one With all our ancestors, while it divides

Over and over, common to us all, The ancient face returning in the child, The distant arms embracing us, the salt

Of our blind origins filling our veins. I stood confused beside my daughter's bed Surprised to find the room around me dim.

Then glancing at the bookshelf in the corner, I saw she'd lined her dolls up in a row. Three little girls were sitting in the dark.

Their sharp glass eyes surveyed me with contempt. They recognized me only as a rival, The one whose world would keep no place for them.

I felt like holding them tight in my arms, Promising I would never let them go, But they would trust no promises of mine.

I feared that if I touched one, it would scream.
```

---

## IC-1883: Creed of a Graffiti Writer

- Title: Creed of a Graffiti Writer
- Author (byline): Steven Bonafide Rojas
- Work: Bum Rush the Page
- Publisher: Three Rivers Press
- Publication date as stated: Oct 2001
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 707
- Already set (do not supply): none

### Source block (context only)

```text
Author: Steven Bonafide Rojas
Book: Bum Rush the Page
ISBN: 978-0609808405
Publisher: Three Rivers Press
Date(Month/Year): Oct 2001
```

### Introduction (context only: never use it for content warnings)

```text
In many people’s minds, ‘graffiti’ tends to instantly translate into ‘vandalism’ or ‘defamation’. In others’ minds, graffiti is intertwined with the Hip-Hop culture and can be viewed only as a misunderstood art form. Whether a crime, or a medium of self-expression, graffiti is always provocative. Creed of a Graffiti Writer by Steven Bonafide Rojas.
```

### Performance text (classify this)

```text
We strike at night
The streets of New York
Is our canvas
We hid in the shadows
When the pig patrol strolls by
The moon give us our
Only source of light
We are the Addicts of Aerosol
The Krylon Can Clan
The Rusto Patrol
We are the German tip spraying
Backpack wearing
Black book carrying
Magnum pilot tagging
The wack toy buffers
We are the Brigade of Bombers
Mounting on our midnight mission
Of colorized madness
The color blending
Spray paint and
Mind melding maniacs
We are the ghetto Picassos
The modern day Matisses
The artistic Shakespeares
That tear white walls in half
We are The Street Canvas Killers
With one quick splat of an ultra flat black
With silver outlines and
Yellow highlights perfected
During 3 a.m. night skylines
We are the crews that redecorate
Building walls with wildstyles
Burning people’s imagination
With motions of the can
The walls wailed words of life
Through sight of krylon colors
On the streets of New York
We bomb city blocks
Rocking throw-ups on top
Of window sills
While standing on top of
Garbage cans
We are the ones who set
Bronx-Brooklyn expeditions
In traditions of nomads
We go where no man’s can
Has sprayed on walls before
We are the underground tunnel turnstile
Hoppers that bomb
Posters with one light being our guide
Our names are found on
High rises and highways
Bridges and building roofs
We are the Bandits of Burners
Our plans are waterproof
Shockproof and foolproff
We are the Tye Dye Tone
Ting Maurauders that write
Graffiti Manifestos
On black wialls with
A silver Uni, SG-7 and
White Pentel markers
We mark the many lands
And train stations
Our tags rag black books and cardboard
Scratched on windows and train doors
Stickers slapped over any mother *****
You had beef with
Only in self-defense
We are the Graffiti Gurus
That spray silver spots on blackness
That become stars on the walls of galaxies
We gaze at our glossy words
And lose ourselves in arrows and 3-D shadows
We are the 12oz Prophets
That write prophecies with
Our hieroglyphics that help
Humans understand us
It is simply the love
Of seeing our name on the wall
It is the symbolic value
Of feeling important in a world
We are lost in
It is the outlet that introduces
Art into our way of thinking
We wear baggy jeans
Hat to the back
And army fatigues
When we venture on our
Trip of blending bombing wonderland
The street is our canvas
When art brushes and stencils
Don’t matter only liquitechs and spray paint
The toxic aroma that entered our bloodstream
On nights when we froze our fingertips
Writing upside down with the can
When finishing a powerhouse
Feel the wrath of Graff
When society calls us vandals and delinquents
That’s why your child wants
To be just like us
We bomb your door to tell
You aour name
It’s a shame you erased our
High rise artistic motion trains:
The Far Rockaway-Lefferta A
The outside D, B and Q in Brooklyn
The Coney Island F
The Canarsie-Broadway Junction L
The J, M and the Z
Over the Williamsburg Bridge
The N and the R in Astoria, Queens
The 1 and the 9 in Washington Heights
The 2 and the 5 in the Bronx
The New Lots 3
The Jerome 4
The Westchester 6
And the Flushing purple 7 train
Now we reign on your law
The Ink Scribe scribbles on your forehead
Then pronounces you hip hoply dead
The 4th Son of Hip Hop
Overshadowed by
Technic table microphones
And Puma gray suede complexion tone
There is no Hip Hop without
Graffiti only Rap
So we wrap our hands
Around cans become one
Our motions are studied
By plagiarist anthropologists
Making money off our art
The spirits on clean canvas can
Be hazardous to minds
When eyes can’t understand
The buck wildstyle alphabet
Sunrises call for travels
Homeward bound
We are the ones that make
The clikclakclikclakclikclakclikclak
Sound with the can on new land
When a tag could get our asses shot
We are the artistic poets
That perform magic with spray paint
And just cal ourselves writers
Graffiti Writers.
```

---

## IC-1884: Curriculum Vitae

- Title: Curriculum Vitae
- Author (byline): Ernest Cline
- Work: The Importance of Being Ernest
- Publisher: Write Bloody Publishing
- Publication date as stated: Sept 2013
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 630
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ernest Cline
Book: The Importance of Being Ernest
ISBN: 978-1938912306
Publisher: Write Bloody Publishing
Date (Month/Year): Sept 2013
```

### Introduction (context only: never use it for content warnings)

```text
This is my Curriculum Vitae by Ernest Cline
```

### Performance text (classify this)

```text
I’ve never been much good at selling myself,
Which is probably why I rank job interviews right up
there with,
oh, say, Chinese Water Torture on my list of fun things
to do.
I think I’d rather chew broken glass
at a Menudo Reunion Concert
being held in the third concentric circle of Dante’s
Inferno
than suffer the agony of auditioning myself
in some sanitized office
for some well-groomed stranger
who is intent on dissecting my identity
to match an eighty-word
computer-generated job description
while I sit there fidgeting and trying desperately to
remember
which parts of my resume
are actually TRUE

[But] I do my best to dodge the barrage of calculated, probing questions strategically designed to lay my soul bare for easy corporate analysis:

“What makes you think you’re qualified for this position?” “What skills do you posses that set you apart from the other applicants?” and the dreaded, inevitable: “Tell me why I should hire YOU!???”

Me? Well . . . because I’m a hard worker. I’m dedicated.

I enjoy a challenge.
I enjoy working with people.
I work well independently.
I work well as part of a group.
I can give orders, I can take orders.
I show up on time.
Hell, I usually show up early.
I have good personal hygiene.
I have a Can-Do attitude.
I’m a Self-Starter . . .

I’ve never been convicted of a felony.

I’m over 18, a U.S. Citizen,
and I’m authorized to work in this country.
I can take constructive criticism,
I keep my work space tidy,
I can probably pass your drug-test.

I follow through. I manage time efficiently.

And I’m proficient with the Internet,
Hypertext Markup Language,
File Transfer Protocols, Microsoft Word,
Windows 3.1, 9x, NT, and nine-millimeter Beretta
handguns.
I know how to make a thermonuclear device out of
everyday household items.
I know who really shot JFK.

If I wanted to, pal, I could reach into your chest, pull out your heart, show it to you while it’s still beating, AND THEN describe it’s physiological layout, including the location of the Aorta, and the Left and Right Ventricles.

You see, I’ve got what it takes.
I’ve got the world on a string.
I’m ambidextrous.
And I can use words like obsequious and ubiquitous
correctly in a sentence.

I can make weapons-grade Plutonium into a yummy
casserole.
I can make a difference.
I can locate Botswana on a map.
I can swing dance.
I’m a team player.
And I’ve been a puppet, a poet, a preacher, a pauper, a
pawn, and a king.

I am not now, nor have I ever been, a homosexual, but I am willing to learn. I can play Heart and Soul on the piano with my toes. I can bring home the bacon and fry it up in a pan. I can quote Shakespeare when I’m drunk. You see, I am the One the Legend spoke of.

I can pull the Sword from the Stone, hook up free cable, make Denver Omelets, and program my VCR.

I don’t take long lunch breaks, I don’t steal office supplies, And I rarely, if ever, call in sick.

And in case you’re about to ask me if I have any weaknesses…

**** NO, I don’t have any weaknesses, unless you count Kryptonite.

I have been known to fly into vengeful fits of homicidal rage when I get turned down for a job by some self-important, balding, baby-boomer ******** like you. But other than that, no . . .

No real weaknesses.

So why don’t you climb down off your high horse,
and just give me a yes or no answer, pal.
Because these are just a few of the reasons,
right off the top of my head,
why you should hire ME.
```

---

## IC-1885: The Dance of Life and Red is the Color of Blood

- Title: The Dance of Life and Red is the Color of Blood
- Author (byline): Conrad Aiken
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1054
- Already set (do not supply): none

### Source block (context only)

```text
Author: Conrad Aiken
Book: Turns and Movies and Other Tales in Verse.
ISBN: 978-0548470268
Publisher: Kessinger Publishing Company
Date (Month/Year): Sept 2007
Author: Conrad Aiken
Book: The Charnel Rose
ISBN: 978-0548411469
Publisher: Kessinger Publishing
Date (Month/Year): Aug 2007
```

### Introduction (context only: never use it for content warnings)

```text
Conrad Aiken grew up in a household with parents who constantly argued. His father was a physician with a struggling practice and his mother was a wanna-be socialite who loved to entertain. This marital discord ended when Aiken was only eleven years old. He found the bodies of his parents - his father, brilliant but unstable, had killed his mother and committed suicide. Aiken struggled with this tragedy, battling to keep his depression at bay; however he confessed in his later years that he "found himself possessed of them forever." The Dance of Life is his tribute to the memory of his parents, and quite possibly a form of self-therapy.
```

### Performance text (classify this)

```text
The Dance of Life

Gracious and lovable and sweet,
She made his jaded pulses beat,
And made the glare of streets grow dim
And life more soft and hushed for him....

Over her shoulder now she smiled
Trustfully to him, like a child,
The while her fingers gayly moved
Along these white keys dearly loved,
Making them laugh a jocund measure,
Making them show and sing her pleasure....
A smile that dwelt upon his eyes,
To see what mood might therein rise,--
What point of soft light seen afar
Which might dilate to moon or star....
A smile that for a second space
Brooded wistfully on her face,
Opening soft her spirit's door,
Disclosing depths undreamed before:
Passionate depths of half-seen flame,
Young loveliness despising shame,
Desire that trembled to meet desire,
And fire that yearned to fuse with fire....
And lightly then she turned away,
Ironic music rippled gay,--
Subtle sarcastic flippancies
Disguising speechless ecstasies...
"Play something else..." He rose to turn
The pages, while the deep nocturne
Struck slow rich chords of plangent pain,
Beautiful, into heart and brain;
A tortured, anguished, suffering thing
That seemed at once to cry and sing;
Despairing love that strove to find
The face beloved with fingers blind.
He saw her body's slender grace,
This drooping shoulder, shadowed face;
All of her body, hidden so
In saffron satin's flush and flow,--
Its white and simple loveliness,--
Came on his heart like giddiness,
Seductive as this music came;
Until her body seemed like flame,--
Intense white flame, so swiftly moving
That it gave scarcely time for loving;
But rapid as the sun she seemed,
A blinding light that flowed and streamed
And sang and shone through roaring space....
The sun itself! for now her face,
Wherein this music's whole soul dwelt,
Drew him like helpless star, he felt
A fierce compulsion, reckless, mad,
A sweet compulsion, troubled, glad,
His trembling hands went out to her,
Her cool flesh made his senses blur;
While, head thrown backward, sinking dim,
She opened wide her soul to him....
Past his life went whirls of lights,
Chaos of music, days and nights,
Her wild eyes yearned to lure him in
And close him up in dark of sin,
To lure him in and drink him down
And all his soul in love to drown....
Her nakedness he seemed to see.
And breast to breast, and knee to knee,
Tremulous, breathless, swaying, burning,
Body to beautiful body yearning,
In joy and terror, flesh to flesh,
They flamed in passion's fine red mesh,--
Living in one short breath again
The cosmic tide's whole bliss and pain,
Darkness and ether, nebulous fire,
Vast suns whirled forth by vast desire,
Huge moons flung out with monstrous mirth
And stars in glorious hells of birth,
All jubilating, blazing, reeling,
An orgiastic splendor wheeling,
Moon torn from earth and star from sun
In screaming pain, titanic fun,
And stars whirled back to sun again
To be consumed in flaming pain!...
In them at last all life was met:
They were God's self! This earth had set.
Mad fires of life sang through their veins,
Ruinous blisses, joyous pains,
Life the destroyer, life the breaker,
And death, the everlasting maker....

TRANSITION And while it is true that every life ends in death; Conrad Aiken demonstrates a fascination with the concept in a wide variety of his published works. Undoubtedly the trauma he witnessed as a child influenced his creativity throughout his life. In Red is the Color of Blood, Aiken seems to take on the persona of his own father in contemplating the thoughts that led up to his mother’s murder.

Red is the Color of Blood

Red is the color of blood, and I will seek it: I have sought it in the grass. It is the color of steep sun seen through eyelids.

It is hidden under the suave flesh of women--
Flows there, quietly flows.
It mounts from the heart to the temples, the singing
mouth--
As cold sap climbs to the rose.
I am confused in webs and knots of scarlet
Spun from the darkness;
Or shuttled from the mouths of thirsty spiders.

Madness for red! I devour the leaves of autumn. I tire of the green of the world. I am myself a mouth for blood ...

Here, in the golden haze of the late slant sun, Let us walk, with the light in our eyes, To a single bench from the outset predetermined. Look: there are seagulls in these city skies, Kindled against the blue. But I do not think of the seagulls, I think of you.

Your eyes, with the late sun in them, Are like blue pools dazzled with yellow petals. This pale green suits them well.

Here is your finger, with an emerald on it: The one I gave you. I say these things politely-- But what I think beneath them, who can tell?

For I think of you, crumpled against a whiteness;
Flayed and torn, with a dulled face.
I think of you, writing, a thing of scarlet,
And myself, rising red from that embrace.

November sun is sunlight poured through honey: Old things, in such a light, grow subtle and fine. Bare oaks are like still fire. Talk to me: now we drink the evening's wine. Look, how our shadows creep along the grave!-- And this way, how the gravel begins to shine!

This is the time of day for recollections,
For sentimental regrets, oblique allusions,
Rose-leaves, shriveled in a musty jar.
Scatter them to the wind! There are tempests coming.
It is dark, with a windy star.

If human mouths were really roses, my dear,-- (Why must we link things so?--) I would tear yours petal by petal with slow murder. I would pluck the stamens, the pistils, The gold and the green,-- Spreading the subtle sweetness that was your breath On a cold wave of death....

Now let us walk back, slowly, as we came.
We will light the room with candles; they may shine
Like rows of yellow eyes.
Your hair is like spun fire, by candle-flame.
You smile at me--say nothing. You are wise.

For I think of you, flung down brutal darkness; Crushed and red, with pale face. I think of you, with your hair disordered and dripping. And myself, rising red from that embrace.
```

---

## IC-1886: Date of Estimated Return from Overseas (DEROS) for My Soul

- Title: Date of Estimated Return from Overseas (DEROS) for My Soul
- Author (byline): Steve Mason
- Work: Johnny’s Song
- Publisher: Bantam Books
- Publication date as stated: April 1986
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 788
- Already set (do not supply): none

### Source block (context only)

```text
Author: Steve Mason
Book: Johnny’s Song
ISBN: 978-0553051605
Publisher: Bantam Books
Date(Month/Year): April 1986
```

### Introduction (context only: never use it for content warnings)

```text
Steve Mason, a soldier and poet who became the unofficial bard of the Vietnam War, died on May 25 in Ashland, Oregon of lung cancer linked to Agent Orange exposure. He was 65. His poems are as taut and graceful as they are soulful. They are about boys who traded the trumped up battles of their hometown football fields for the deadly ones of Vietnam’s mangrove swamps, about men who returned from war to find other men raising their children, about men who, like himself, for 20 years have been toting “the duffel bags of their guilt” along the long road home. Date of Estimated Return from Overseas for My Soul by Steve Mason
```

### Performance text (classify this)

```text
At times when I am calm
I remember
that even if you waited for it
nothing came as suddenly
as gunfire
and nothing (not even the Lieutenant)
seemed as stupid
as the silence which followed

At such times I know also
that each of us
who fought in Vietnam
was spiritually captured by it,
and that each remains
a prisoner
of his own war-

It is, therefore, not surprising
that for some (like for me)
the AfterNam emptiness
published no D.E.R.O.S.
for the soul....

Yet, in moments better known to me,
when reason drifts
and whole worlds are illuminated
with Platonic images
dancing images
dancing against the cave-walls
of my mind,
lit by a single candle
borrowed from a twilight wish,
I take the stairs two-at-a-time
and wait in the second floor window
of my days,
hoping that someday will come next morning
and that I'll recognize the soul of a much younger me
come diddy-boppin' down the street,
eating a sky-bar
and hefting a duffle bag
filled with new and more believable myths
that I might live by
(not to mention back pay)
while humming something about
going to San Francisco
and something about a flower in somebody's hair

Frankly, I don't know if I'd throw flowers
or run down stairs, meet him at the curb
and beat Hell out of him-
leaving me the way he did!

I mean, it's not like my damned soul,
dressed up like Jennifer Jones in drag,
and waved farewell with a lace hanky
from the base of a Bon-Sai plant
in a To do Street floral shop
while i woke the next morning and
couldn't cry anymore
or laugh like before
or give a shit period.

And my soul didn't go berserk
under the too bright light
of a Government Moon
and go roaring down Highway #1
doing a wheelie on a cycle
like James Dean in a steel pot
and flak jacket
laughing Red Baron kind of laugh
and quoting Kipling's Barrack-Room
Ballads--

No.
My soul just did
what most souls did.
Just disappeared one afternoon
when I was in a firefight
Just "walked away" in the scuffle
like a Dunhill lighter
off the deck of a red-neck bar.

Peculiar,
A man can lose his money,
his woman
(even his mind)
and still he can come back,
but if he loses his courage
or his pride
then-
it is over.

And what of a lost soul?
I ask myself
when madness invades
scattering today's headlines
like March Hares
leaving nothing at the table
of my reason
beyond one crumb of truth
and the enormous bloodstain
on the white cloth of my youth-shaped
(if you come around this side
of the table and cock your head
just so)
like a distorted lunar projection of Vietnam.

And careful, don't strike your knee
against that table leg
cause then it jumps alive
like somebody flunked
the ink blot test
and knocking over the candelabra
dives out of the window of my sanity
to run naked down the street
lined on both sides by
Vietnam vets
who couldn't sleep either
and just followed the blood trail
like mute somnambulists
in a black and white foreign film
because they heard that tonight
their shared nightmare
(with Vietnamese sub-titles)

had called a muster of lost souls
to be followed by Nam,
Bloody Nam,
leading a one man parade
and twirling a baton
that looked like nobody's penis
I ever saw
and probably belonged
to the guy in back of me
poor bastard.

Geez, it gets scary in here sometimes,
do it not, Burtha?
And oh, sister, do you have songs to
sing?
About war without glory
and love beyond reward.

Maybe someday God will mint a medal so beautiful
no words are printed on it
and all of our sisters
who were there with us
would get one
and everyone, everywhere who saw it
would know just what it was
and would find a "thoughtful place"
to go sit down in for a week

And then maybe God would let us have a picnic (bigger than the moon) and all the boys and girls of daddies whose lives they saved could hold hands to make a daisy chain for the sun.

And when it was all done
the big people
would make God a prayer-promise
never, never to do anything like Nam
again
And when the cheers died down
the sun would bow his head
ever so slightly
so the children might wish their necklace
`round his head
and when it was in place,
all of a sudden-
faster, even then gunfire,
everybody's lost soul would
just come floating down like a
bright balloon
on a string

and mine would wink at yours
and pretend not to see me
and when everyone got his,
All the children would sing
Happy Birthday! Happy Birthday!!
over and over again.....
```

---

## IC-1887: Dear White America and ‘Cuz He’s Black

- Title: Dear White America and ‘Cuz He’s Black
- Author (byline): Danez Smith and Javon Johnson
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1243
- Already set (do not supply): none

### Source block (context only)

```text
Author: Danez Smith
Book: The BreakBeat Poets: New American Poetry in the
Age of Hip-Hop (Page 258)
ISBN: 978-1608463954
Publisher: Haymarket Books
Date (Month/Year): April 2015
Author: Javon Johnson
Book: Viral
ISBN: 978-0989641517
Publisher: Button Poetry
Date (Month/Year): Dec 2013
```

### Introduction (context only: never use it for content warnings)

```text
This is what I want to say: Dear White America, Look deep, look into your souls with silence, quiet that voice that will speak to you of your white “innocence.” Take a deep breath. Make a space for my voice in the deepest part of your psyche. Try to listen, to practice being silent. There are times when you must quiet your own voice to hear from or about those who suffer in ways that you do not. Dear White America by Danez Smith.
```

### Performance text (classify this)

```text
DEAR WHITE AMERICA

I’ve left Earth in search of darker planets, a solar system that revolves too near a black hole. I’ve left a patch of dirt in my place and many of you won’t know the difference, giving my name, if it makes you feel better while you run your hands through its soiled scalp.

I’ve left in search of a new God. I do not trust the God you have given us. My grandmother’s hallelujah is only outdone by the fear she nurses each time the blood fat summer swallows another child who used to sing in the choir. Take your God back. Though his songs are beautiful, his miracles are inconsistent.

I want the fate of Lazarus for Renisha, I want Chucky, Bo, Mo, Trah, Shah, and Islah and Trayvon risen 3 days after their entombing, their ghosts re-gifted flesh and blood, their flesh and blood re-gifted their children.

I have left Earth. I am equal parts sick of your “go back to Africa’s as I am your “I just don’t see races.” Neither did the poplar tree.

We did not build your boats, though we did leave a trail of kin to guide us home. We did not build your prisons, though we did, and we filled them too. We did not ask to be part of your America, though are we not America, her bones brittle and dragging a ripped gown through Oakland?

I will not stand your ground. I am sick of calling this recklessness the law.

Each night I count my brothers and, in the morning, when some did not survive to be counted, I count the holes they leave your master. Magic trick, America. Now he’s breathing, now he don’t. Abracadaver, white bread voodoo. Your rope-burned hands, tired of the noose, and my cousin epistled to do your work.

I tried, white people. I tried to love you all, but you spent my brother’s funeral making plans for brunch, talking too loud next to his bones. You took one look at the river, plump with the body of boy after boy after sweet boy and asked, “Why does it always have to be about race?” Because you made it that way.

Put an asterisk next to my sister’s gorgeous face, called her pretty for a black girl, because black girls go missing without a whisper of where, because there are no Amber Alerts for the amber-skinned girls, because Jordan boomed, because Emmett whistled, because Huey P spoke it, because Martin preached it, because black boys have always been too loud to live, because it’s taken my father’s time, my mother’s time, my aunts’ and my uncles’ time, my sisters’ and my brothers’ time, how much time do you want for your progress?

I have left Earth and I won’t stop ’til I find a place where my kin can be safe, until black people ain’t but people the same color as the good wet earth, until that means something.

Until then, I bid you well, I bid you war, I bid you our lives to gamble with no more. I have left Earth, and I am touching everything you beg your telescopes to show you, giving the stars their right names in this new testament, this new story you cannot see or ruin this, if only this one is ours.

TRANSITION Ntozake Shange once wrote that “cuz he’s black and poor he’s disappeared – the name was lost” This is what I want to say: Dear White America: Again, take a deep breath. Don’t tell me about how many black friends you have. Don’t tell me that you voted for Obama. Don’t tell me that you don’t see color. Don’t tell me that I’m blaming whites for everything. To do so is to hide yet again. You are part of a system that allows you to NOT engage in “the talk” that black people must have with their children. The “talk” about what to do when they are confronted by white police officers.” ‘Cuz He’s Black by Javon Johnson ‘CUZ HE’S BLACK

So I'm driving down the street with
my 4-year-old nephew.
He, knocking back a juice
box, me, a Snapple, today y'all
we are doing manly shit. I love
watching the way his mind works.
He asks a million questions.
Uncle, why is the sky blue?
Uncle, how do cars go?
Uncle, why don't dogs talk?
Uncle, uncle, uncle, he asks,
uncle, uncle, uncle, he asks
uncle uncle uncle
as if his voice box is
a warped record. I try my best
to answer every question, I do.
I say it's because the way
the sun lights up the outer space.
It's because engines
make the wheels go.
It's because their minds aren't
quite like ours. I say Yes.
No. No. Yes. No. Yes. No. I don't know.
Who knows? Maybe. We laugh.
He smiles at me, looks out the window,
spots a cop car, drops his seat
and says,
"Oh man, Uncle, 5-0, we gotta hide."
I'll be honest. I'm not happy
with the way we raise our Black boys.
Don't like the fact that
he learned to hide
from the cops before
he knew how to read.
Angrier that his survival
depends more on
his ability to deal
with the "authorities"
than it does his own literacy.
"Get up," I yell at him. "In this car, in this family,
we are not afraid
of the law."
I wonder if he can hear
the uncertainty in my voice.
Is today the day he learns
that uncle is willing to lie to him,
that I am more human
than hero?
We both know the truth
is far more complex than
do not hide. We both know too many
Black boys who disappeared.
Names lost.
Know too many Trayvon Martins
Oscar Grants
and Abner Louimas, know too many
Sean Bells, and Amadou Diallos
Know too well that we are
the hard-boiled sons of Emmett Till.
Still, we both know
it's not about whether or not
the shooter is racist,
it's about how poor Black boys
are treated as problems
well before we are treated as people.
Black boys in this country
cannot afford
to play cops and robbers
if we're always considered the latter,
don't have the luxury
of playing war
when we're already in one.
Where I'm from,
seeing cop cars drive
down the street feels a lot
like low-flying planes in New York
City. Where I'm from, routine traffic
stops are more like mine
fields, any wrong move
could very well mean your life.
And how do I look my nephew in his apple face
and tell him to be strong when we both know
black boys are murdered every day, simply
for standing up for themselves? I take him
by the hand, I say
be strong. I say be smart. Be kind, and polite.
Know your laws. Be aware of
how quickly your hands move
to pocket for wallet or ID,
be more aware of how quickly
the officer's hand moves to holster, for gun.
Be Black. Be a boy and have fun,
because this world will force you to
become a man much quicker
than you need to.
"Uncle," he asks, "what happens
if the cop is really mean?"
And, it scares me to
know that he, like
so many Black boys,
is getting ready for a war
I can't prepare him for.
```

---

## IC-1888: The Detective

- Title: The Detective
- Author (byline): Ai
- Work: Vice: New and Selected Poems
- Publisher: WW Norton and Co
- Publication date as stated: March 1999
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 706
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ai
Book: Vice: New and Selected Poems
ISBN: 978-0393047059
Publisher: WW Norton and Co
Date (Month/Year): March 1999
```

### Introduction (context only: never use it for content warnings)

```text
Graphic dreams and memories of the past are awakened for the speaker of this poem. He spends his days investigating horrific crimes and his nights re-living his own past as a soldier in Vietnam and Cambodia. A troubled soul? Or simply The Detective by Ai
```

### Performance text (classify this)

```text
I lie on my daughter's body
to hold her in the earth,
but she won't stay;
she rises, lifting me with here,
as if she were air
and not some remnant
of failed reeducation
in a Cambodian mass grave.
We rise, till I wake.

I sit up, turn on the lamp,
and stare at the photo of the girl
who died yesterday,
at her Vietnamese mother
and her American father.
Jewel van duc Thompson,
murdered in Springfield, Ohio,
in her eighteenth year,
gone the day she was born
like in the cartoons,
when somebody rolls up the road
that stretches into the horizon
and the TV screen goes black...

Go home, Captain,
the cop said yesterday,
as he gripped my hand
and hauled himself
up from the ditch
where they'd found her
like Persephone
climbing from the underworld
one more time,
his eyes bright,
the hunger for life
and a good time
riding his back like a jockey.
Death is a vacation, I answered.
Then my hand was free
and I could see
how she was thrown
from the highway
down the embankment.
Where were Art and Rationality
when it counted? I thought -
always around the corner
from somebody else's street.
Even the ice cream man
never, ever made your block,
though you could hear the bells,
though you could feel the chill
like a shock
those hot days
when your company beat the bushes,
when you bit into death's chocolate-covered center
and froze...

I turn off the lamp
and lie still in the dark.
Somewhere in time, it is 1968.
I am bending over a wounded man
with my knife.
My company calls me the Angel of Mercy.
I don't remember yesterday
and there is no tomorrow.
There is only the moment
the knife descends
from the equatorial dark.
Only a step
across the Cambodian border
from Vietnam
to search and destroy the enemy,
but it is just a short time
till the enemy discovers me
and I would die,
but for the woman
who takes me to the border,
who crosses with me from the underworld
back to the underworld.

I open the curtain.
Outside the early morning
is spinning, gathering speed,
and moving down the street
like a whirlwind.
I pull the curtain shut again
and switch on my tape
of the murderer's confession,
hear the faint, raspy voice
playing and replaying itself.

It was Saturday night.
She stood alone at the bus stop.
When she took the first step
toward my car,
I dropped the key once, twice.

She smiled, she picked it up.

I lie back on the bed,
while the voice
wears itself out.
Yes, I think,
you live for a while.
You get tired.
You walk the road into the interior
and never come back.
You disappear
the way the woman
and your child disappear
into Cambodia
in the pink light of dawn,
early April 1975.
You say you'll go back,
but you never do.

Springfield, Phnom Penh.
So many thousand miles
between a lie and the truth.
No, just a step.

The murderer's voice rises,
becomes shrill.
Man, he says, is it wrong
to do what is necessary?
I switch off the tape.
Each time I sit down,
I think I won't get up again;
I sink through the bed, the floor,
and out the other side of the Earth.

There my daughter denounces me. She turns me back at the muddy border of forgiveness. I get up dress quickly, then open the curtain wide.

At the door,
I put my hand on the knob, hesitate,
then step out into sunlight,
I get into the car,
lift the key to the ignition,
drop it.
My hand is shaking.

I look into the back seat.
The Twentieth Century is there,
wearing a necklace of grenades
that glitters against its black skin.
I stare, see the pins
have all been pulled.
Drive, says the voice.
I turn to the wheel,
imagine the explosions,
house after house
disintegrating in flames,
but all is silent.

People go on with their lives
on this day that is one hundred years long,
on this sad red balloon of a planet,
the air escaping from it
like the hot, sour breath of a child
```

---

## IC-1889: The Dislocated Room

- Title: The Dislocated Room
- Author (byline): Richard Siken
- Work: The Best American Poetry 2000
- Publisher: Scribner
- Publication date as stated: 2000
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 884
- Already set (do not supply): none

### Source block (context only)

```text
Author: Richard Siken
Book: The Best American Poetry 2000
ISBN: 978-0684842813
Publisher: Scribner
Date(Month/Year): 2000
```

### Introduction (context only: never use it for content warnings)

```text
According to Richard Siken there are three ways to approach the concept of death: Romantically, realistically or fighting the concept – kicking and screaming, against your will. In his poem, The Dislocated Room, the speaker, Henry, has been shot – the how is left open to interpretation, but the resulting approach of death and the fight against the inevitable is breathtaking. The Dislocated Room by Richard Siken.
```

### Performance text (classify this)

```text
It was night for many miles and then the real stars in the purple sky,

like little boats rowed out too far, begin to disappear.

And there, in the distance, not the promised land,

but a Holiday Inn, with bougainvillea growing through the chain link by the pool.

The door swung wide: twin beds, twin lamps, twin plastic cups wrapped up in cellophane

and he says No Henry, let's not do this. Can you see the plot like dotted lines across the room?

Here is the sink to wash away the blood, here's the whiskey, the ripped-up shirt, the tile of the bathroom floor,

the disk of the drain

punched through with holes. Here's the boy like a sack of meat, here are the engines, the little room

that is not a room, the Henry that is not a Henry, the Henry with a needle and thread,

hovering over the hollow boy passed out

on the universal bedspread.

Here he is again, being sewn up. So now we have come to a great battlefield, the warmth of the fire,

the fire still burning,

the heat escaping like a broken promise.

This is the part where you wake up in your clothes again, this is the part where you're trying to stay inside the building.

Stay in the room for now, he says. Stay in the room

for now. This is the place, you say to yourself, this is the place where everything

starts to begin, the wounds reveal a thicker skin and suddenly there is no floor.

Meanwhile, there is something underneath the building that is trying very hard

to get your attention---

a man with almond eyes and a zipper that runs the length

of his spine. You can see the shadow that the man is throwing across

the linoleum, how it resembles a boat, how it crosses the tiles just so,

the masts of his arms rasping against the windows. He's pointing at you with a glass of milk

as if he's trying to tell you that there is some sort of shining star now buried deep inside you and he has to

dig it out with a knife.

The bell rings, the dog growls, and then the wind picking up, and the light falling, and his mouth

flickering, and the dog howling, and the window closing tight against the dirty rain. Here is the hallway and here are the doors and here is the fear of the

other thing, the relentless

thing, your body drowning in gravity. This is the in-between, the waiting that happens in the

space between one note and the next, the place where you confuse

his hands with the room, the dog

with the man, the blood

with the ripped-up sky. He puts his hands all over you to keep you in the room.

It's night. It's noon. He's driving. It's happening

all over again.

It's love or it isn't. It isn't over. You're in a car. You're in the weeds again. You're on a bumpy road

and there are criminals everywhere,

longing for danger.

Henry, he's saying. Who is it that's talking? I thought I heard the clink

of ice to teeth. I thought I heard the clink of teeth to glass. Open the door and the light falls in. Open your mouth and it falls

right out again. He's on top of you. He's next to you, right next to you in fact.

He has the softest skin wrapped entirely around him.

It isn't him. It isn't you. You're falling now. You're swimming. This is not

harmless. You are not

breathing. You're climbing out of the chlorinated pool again.

We have not been given all the words necessary.

We have not been given anything at all.

We've been driving all night.

We've been driving a long time.
We want to stop. We can't.
Is there an acceptable result? Do we mean something
when we talk?

Is it enough that we are shuddering

from the sound? Left hand raising the fork to the mouth, feeling the meat slide down

your throat, thinking

My throat. Mine. Everything in this cone of light is mine. The ashtray and the broken lamp, the filthy orange curtains and his

ruined shirt.

I've been in your body, baby, and it was paradise.

I've been in your body and it was a carnival ride. They want to stop but they can't stop. They don't know what

they're doing. This is not harmless, the how to touch it, we do not want the screen

completely lifted from our eyes, just lifted long enough to see the holes.

Tired and sore and rubbed the wrong way,

rubbed raw and throbbing in the light. They want to stop but they don't stop. They cannot get the bullet out.

Cut me open and the light streams out.

Stitch me up and the light keeps streaming out between

the stitches. He cannot get the bullet out, he thinks, he can't, and then he does.

A little piece of grit to build a pearl around. Midnight June. Midnight July. They've been going at it for days now.

Getting the bullet out. Digging out the bullet and holding it up to the light, the light.

Digging out the bullet and holding it up to the light.
```

---

## IC-1890: A Finger, Two Dots, Then Me

- Title: A Finger, Two Dots, Then Me
- Author (byline): Derrick Brown
- Work: Born in the Year of the Butterfly Knife
- Publisher: Write Bloody Publishing
- Publication date as stated: 2004
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 716
- Already set (do not supply): none

### Source block (context only)

```text
Author: Derrick Brown
Book: Born in the Year of the Butterfly Knife
ISBN: 978-0978998905
Publisher: Write Bloody Publishing
Date (Month/Year): 2004
```

### Introduction (context only: never use it for content warnings)

```text
From the smallest to the greatest, from the richest to the poorest, everyone eventually dies. But what happens after death? Can you know for sure? Many view the end of their lives with uneasiness. They ponder, “What’s next?”—“Will I live again?”—“Is this it?”—“Will I ever see my loved ones again?”—“Where am I going after this life?” For the atheist and agnostic, what happens after death is not important. According to their philosophy, life should be enjoyed in the “here and now.” But what if, like the teachings of traditional Christianity, they are wrong? What if God does exist and He offers an awesome future beyond the grave, not taught by the religions and philosophies of men? A Finger, Two Dots, Then Me by Derrick Brown.
```

### Performance text (classify this)

```text
Lying together in the park on Seventh,
our backs smoosh grass and I say
I will love you till I become a child again,
when feeding me and bathing me is no longer romantic,
but rather necessary.

I will love you till there is no till.
Till I die.
And when that electroencephalogram shuts down, baby
that’s when the real lovin’ kicks in.
Forgive me for sounding selfish
but I won’t be able to wait under the earth for you
(albeit a romantic thought for groundhogs,
gophers and the gooey worms).
I will not be able to wait for you…
but I will meet up with you
and here’s where you will find me:
get a pen–
Hold your finger up
(two fingers if your hands are frail by now)
and count two stars directly to the left
of the North American moon.
You will find me there.
You will find me darting behind amazing quasars
Behind flirtatious winks
of bright and blasting boom stars!

Sometimes charging so far into space
the darkness goes blue.
I will be there chasing sound waves
riding them like two-dollar pony ride horses
that have finally broken free and wild.
I will be facing backwards, lying sideways,
no hands, sidesaddle, sometimes standing
sometimes screaming zip zang zowie!
My God, it’s good to be back in space… Where is
everybody?
You will recognize my voice.
You will see the flash of a fire trail
burning off the back of me
burning like a gasoline comet kerosene sapphire.
This is my voice.
Don’t look for my body or a ghost.
I’ll resemble more a pilot light than a man now.
I’m sure some will see
this cobalt star white light from earth
and cast me a wish like a wonder bomb.
And I’ll think “Hmmph. people still do that?”

I’m sure I’ll take the light wonder bombs
to the point in the universe
where sound does end.
The back porch of God’s summer home.
It’s so quiet here, you float.
It feels the way cotton candy tastes.
I say to him… why do I call you God?
He says ‘Because Grand Poobah sounds ridiculous.’
(Who knew he was so witty?)
I ask him ‘Lord, so many poets have tried to nail it and
missed, what is holy?’
At that moment,
the planets begin to spin and awaken
and large movie screens appear on Mars, Saturn and
Venus
each bearing images I have witnessed
and over each and every clip flashes the word holy.
armadillos–holy
magic tricks–holy
cows’ tongues–holy
snowballs upside the head–holy
clumsy first kisses–holy
sneaking into movies–holy
your mother teaching you to slow dance
the fear returning
the fear overcome–holy
eating top ramen on upside-down frisbees
cause it was either plates or more beer–holy
drunk beach cruiser nights–holy
the $5.00 you made in vegas
and the $450.00 you lost–holy
the last time you were nervous holding hands–holy
feeling God at a pool hall but not church–holy
sleeping during your uncle’s memorized dinner prayer–
holy
losing your watch in the waves and all that signifies–holy
the day you got to really speak to your father cause the
television broke–holy
the day your grandmother told you something meaningful
cause she was dying–holy
the medicine
the hope
the blood
the fear
the trust
the crush
the work
the loss
the love
the test
the birth
the end
the finale
the design
in the stars
is the same
in our hearts
the design
in the stars
is the same
in our hearts
in the rebuilt machinery of our hearts
So love, you should know what to look for
and exactly where to go…
Take your time and don’t worry about getting lost.
You’ll find me.
Up there, a finger and two dots away.
If you’re wondering if I’ll still be able to hold you
…I honestly don’t know
But I do know that I could still fall for
a swish of light that comes barreling
and cascading towards me.
It will resemble your sweet definite hands.
The universe will bend.
The planets will bow.
And I will say “Oh, there you are. I been waitin’ for ya.
Now we can go.”
And the two pilot lights go zoooooooom
into the black construction paper night
as somewhere else
two other lovers lie down on their backs and say
“What the hell was that?”
```

---

## IC-1891: First Period and It’s a Teenage Thang

- Title: First Period and It’s a Teenage Thang
- Author (byline): Kevin M. Derrig & Regie Gibson
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1041
- Already set (do not supply): none

### Source block (context only)

```text
Author: Kevin M. Derrig
Book: The Spoken Word Revolution: Slam, Hip Hop &
the Poetry of a New Generation
ISBN: 978-1402202469
Publisher: Sourcebooks, Incorporated
Date (Month/Year): March 2005
Author: Regie Gibson
Book: The Spoken Word Revolution: Slam, Hip Hop &
the Poetry of a New Generation
ISBN: 978-1402202469
Publisher: Sourcebooks, Incorporated
Date (Month/Year): March 2005
```

### Introduction (context only: never use it for content warnings)

```text
School should be a positive experience of learning, growing and becoming the person you are meant to be. Unfortunately, not all teachers possess the qualities of a nurturing" charismatic adult. And when students come in contact with these dream-stifling, spirit-crushing teachers, the impact they have can affect the way students feel about themselves for the rest of their lives.

First Period by Kevin M. Derring
```

### Performance text (classify this)

```text
half way through first period dust accumulated on the sweaty palm of my

raised hand must be a centimeter thick by now as the chicken-legged teacher goes around the

room
defacing students’ homework from last night
with red pen graffiti
that focuses more on missed commas than the

content of the sentences he finally decides to acknowledge me “Mr. Derrig, why do I have a feeling that this is

another one of your dumb comments. You constantly waste my time. Why

don’t you just drop out or something?”

why don’t I just drop out why don’t I just drop out!

and it was at that moment that all statistics

began to make sense to me
statistics of children whose mouths water more
for the many taste of
society corner slanged penicillins
than the cardboard textures of diplomas
with pipes more important to fill
than class requirements
statistics of classes cut
to avoid battlefields full of aggravated shrapnel
from teachers with exploding tempers
teachers with magnifying glasses at the end

pointers who feed off the brightness of surrounding

students to singe holes in the esteems of those who need

just a little more help
than
others
I wanted to turn my shot-down hand into a fist
I wanted to hit him ‘til he was incapable of

speaking anymore but I didn’t want to become another number in

overflowing manila folders of children arrested in school and we wonder why a gun seems to fit perfectly

in the hands of this generation’s adolescents ladies and gentlemen I’m writing this poem to highlight that which has

been stuck like gum
underneath wobbly desks
free from parental eyes
only to mess the hand of those who have to sit
there
I’m writing this poem to speak for all the rows of

children before me who remained voiceless in the cracks of school

and its soundproof textbooks I’m writing this poem for all the children who

have not yet been named the ones that will one day have to fill these rows

I’ve been struggling in only to enter classrooms where they’ll be shot

down for what they feel ladies and gentlemen the future of America is being crushed between

the molars of power-hungry tyrants who think class rooms

are boot camps and if we have any teachers in the audience I urge you to understand that the hand you grab

the chalk with
the hand you grab those red pens with
the voices you speak with
are oversized chisels
and you must proceed to teach with caution
for what you say and what you do is written in

stone and if you chisel too hard these minds can crack “So what don’t you understand now, Mr. Derrig?” I just wanted to know if I could go to the bathroom

TRANSITION

Let’s face it . . . It’s hard to be a teenager. You have the expectations of teachers at school and your parents at home – all looming over you – beating you down. What’s a teenager to do?

According to Regie Gibson . . . “My mother is a very devout Jehovah’s Witness, and has been for most of my life. My father, at one time, was a Chicago police officer. Neither one of them would allow me or my brother Ron to go out. So my brother and I would sneak out of the home when mama went to sleep and pops went to work.” This is a recollection of what it meant to be young, defiant and feeling your oats at sixteen and is for every teenager who has rebelled against their parents by sneekin out. It’s a Teenage Thang by Regie Gibson.

bass slides in on all fours rabid with feral look in eyes bodies twist

into

blasphemous

angle of

rebellion/defiance

something smellin like

jail time cuts across air

like hand fulls of zirconia scratchin shit

out of a plexiglass sky

over in corner

cue balls psychotic smack breaks up tribe of stripes and solids on field of green

black eight sinks

thru smoky haze of aw shits

damns as ten spots reluctantly

ruffle they ways

out pissed off pockets

d.j. priest
sittin reverently in the pulpit
jacks sounds in alternatin patterns
of thirty three and thirds

spinnin gospel of our faith as congregations hands

reach heavenward exposin our palm to angles

as we hope to catch a
hallowed high five
from a god whose
pissed cuz shes gotta work
the night shift

tonight

we be young virile sweatin passions ya gotta experience to understand

we don’t give a damn

bout tympanic

cartilaginous erosion

of inner ears

weakened by 1200 to many

hot grindin weekends

of buttbumpinwoofinandtweetin

we don’t give a damn
bout ass kickin
waitin on us when we get
home way past curfew

(ok a little)

but tonight we only care bout

ass kickin bass and drum

can give

ass kickin bass and drum

can heal

tonight we live for strobelights

kissin vision

bringin new sight
for floors moanin with
weight of young
flippant attitudes

glasses mumblin

speech of stolen

kisses

sky exploding with funk of flirtin smiles

we live for bodega crew
comin up from barrio
bringin supple
brown morenas con
hips like congas
gon-boppin
6/8 rhythm
from front door to dance floor

got you tryin to speak in language you ain’t ever tongued before uh mira maimi uh pasie agee poo on

momentato po fayva (or something like that)

big red manzana lips
partin ever so slightly
revealin thin sliver of pink tongue
rollin like scarlet smoke off roof of latina mouths

we live for sisters blue blacks honey browns

heavenly ebonies getting down

on legs shaped like mamas soulfood

with a whole lotta attitude

calves

carved

outta hams and hocks

with backsides big round sweet and tender as grandmamas homemade biscuits (have mercy)

they hair icked

slicked

tricked

or picked out

into asymmetricalisoscelesrhomboidparallelograms

and a few other forms defying geometric classification

tonight

we be young virile

sweaty with passion you gotta experience to understand

tonight

be our night to hold somebodies body to feel they eye lashes brush up against face on slow jam

feel thin wispy fingers

of they breath invade

sensitive conch shell ear

like well trained guerillas

to hold them close firm heavin nubile against the mask of teenage knowin and adolescent pretence.
```

---

## IC-1892: From Violence to Peace

- Title: From Violence to Peace
- Author (byline): Jimmy Santiago Baca
- Work: Black Mesa Poems
- Publisher: New Directions Publishing Corporation
- Publication date as stated: Nov 1989
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1003
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jimmy Santiago Baca
Book: Black Mesa Poems
ISBN: 978-0811211024
Publisher: New Directions Publishing Corporation
Date (Month/Year): Nov 1989
```

### Introduction (context only: never use it for content warnings)

```text
Let’s hear it for Jimmy Santiago Baca! He put the Chicano into American literature; he put the bare-foot street kid into the American Library; he put the ex-con into the Academy.

From Violence to Peace is Baca’s tribute to his cause to decrease youth violence. It is a poem based around a narrative. In his teens, he bought a young bull calf, raised it. Then had to have it butchered: Full of self-hate for his betrayal, he gets fighting drunk, harasses a neighbour, who shoots him in self defence. Convalescing, he nurses the feud before realising it’s peace he needs, to dismantle the bloody wheel of violence he had ridden since childhood.

From Violence to Peace by Jimmy Santiago Baca
```

### Performance text (classify this)

```text
Twenty-eight shotgun pellets
crater my thighs, belly and groin.
I gently thumb each burnt bead,
fingering scabbed stubs with ointment.

Could have neutered me, made extinct
the volatile, romantic man I am.
“He’s dead,”
doctor at emergency room
could’ve easily told my wife that night.
Instead, “Soak him in a bath twice a day. Apply
this ointment to the sores. Here’s a month’s supply
of pain killers.” I remember the deep guttural groan
I gave, when the doctor pressed my groin.
Assured
I could still make love, morphine drowsed me
and in a dull stupor I don’t remember
police visiting my bed, or laughing so hard,
they scowled for a serious answer.
I howled a U.F.O. shot me along the Río Grande,
and they cursed and left.

In the summer of ’88
I’d traded alfalfa for a bull calf.
Still smelling of milk udders,
I tied it to the truck rack and drove off.
Its hooves teethed
at pink roots
’til the whole lush field went bare dirt.
A magnificent bull.
Glowing wheel of heart
breathed brimming stream of white flame at dawn.
He wrangled his black brawn
like a battleshield to challenge the sun,
reared thick neck down and sideways,
lunged at me with dart and snort,
hoof-stamped and nostrilled dirt,
’til I growled him back
whipping air
with a limber willow branch,
poured grain in trough
and spread alfalfa.
I respected his horns
and he the whistling
menace of willow.

One afternoon my cousin Patricio
helped me band the bull’s scrotum,
usurp swollen sap
in his testicle sack. It withered
to a pink wattle and seeded
the garden to drive cornstalks
to bear hardy, golden horns.

Thereafter, he grazed the fence line,
with the tempered lust and peaceful grace
of a celibate priest.
His bearing now arranged itself
elegant as a wild flower
sprung over night.
______________

Perfecto shot it.
Rasping on a black rope of blood
round its neck, it staggered,
bouldering convulsions.
Blood exploding
in bright lash of earthquaked air,
it stumble-butted stock trailer fender—
second and third shots glowed
its death.

A quivering shadow of life-flame
darkened the air and it sputtered
a last drop of blood.
I drank long swigs
of whiskey and, thinking it was dead,
turned to walk away,
then
it gave a tremendous groan, tremendous groan,
a birth-letting groan . . . a moon groan . . .
blood spurted out, thick, thick, thick
alleys of dead star blood

and I turned and said aloud to myself, “That’s the moon’s voice! That’s the moon’s voice!”

And the white moon was in the sky, and I looked at the moon for a long time.

______________

I sat on the ground
and gulped whiskey, drank the steer’s death
still warm in my throat.
A beautiful animal! I allowed to be butchered.
When it trounced and galloped in the field,
its body was a dark, windy cliff edge,
and its eyes were doorways of a dream—
now it bled a charred scroll
of ancient chant in gravel, I would never know,
and its blackened logs of blood
smoldered dying vowels, I would never hear.
My heart’s creak-n-tremble rage
milled the steer’s death to red grist,
I grieved,
I wept drunkenly
that no one cared,
that humankind betrayed him,
that we were all cowards.
______________
Perfecto, Valasquez and the butcher
tried to stop me
from driving,
but now was the time to settle
a bad feud with another friend.
Redeem the bull’s blood with ours.
I drove to Felipe’s house,
anger knotted in me
tight as the rope tied
to the stock trailer
steer strained against.
I pulled, but could not free myself.
(I had a dream night before—
I crossed black-iron footbridge,
partially collapsed by sea storm.
Left-hand railing swept out to sea,
I gripped bolt-studded right-hand railing,
finger-clutched wire netting sides,
carefully descended waist-high water. Waded
through slowly and ascended other side—
but had lost my sunglasses and wallet,
went back, groped bottom, found them and ascended
again.)

Had to cross that bridge again.
Full of significance . . . tonight,
deepest part of flooded bridge was danger . . . drowning
. . .
represented years of my life collapsed
and destroyed, water the cleansing element,
my ascent from had healed, onto firm ground,
but I went back, to re-live
destruction…
“Felipe!” I yelled, porch light
flicked on, illuminating the yard.
“Came to fight,” I said, “take off
your glasses.”

Bug-eyes glazed bewildered, then gray slits of lips snarled, “You motherless dog!”

He withdrew in darkness a moment,
reappeared on porch, serrated saw of his voice
cut the chill dark,
“Hijo de su pinche madre!
Mátalo! Mátalo!!”

First shot framed darkness round me
with a spillway of bright light,
eruption of sound, and second shot roared
a spray of brilliance and the third
gave an expanded halo-flash.
My legs woozed, and then
I buckled to the ground.
(I thought, holy shit, what ever happened
to the old yard-style fight between estranged friends!)

I groaned with the steer,
and crawled my dead legs
to the truck, lunged on elbows into the cab,
hand lifting the dead stone beneath my waist
to clutch and brake.

Following morning calls came,
“Tell us who did it Gato!”
“Our rifles are loaded!”
I said, “Leave it alone. What would you do
if a drunk man came into your yard,
threatened to beat you?”
I wanted peace,
wanted to diffuse the immovable core
of vengeance in my heart,
I had carried since a child,
dismantle the bloody wheel of violence
I had ridden since a child.

During my week in bed,
pellets pollinated me
with a forgotten peace,
and between waking thoughts of anger and vengeance,
sleep was a small meadow of light,
a clearing I walked into and rested. Fragrance of peace
filled me as fragrance
of flowers and dirt permeate hands
that work in the garden all day.

Curandero came to visit, and said,
“The bull in ancient times was the symbol of females.
Did you know that? Killing the bull,
is killing the intuitive part of yourself,
the feminine part. Did you realize,
when Jesus was raising Lazarus,
he groaned in his spirit and that bull groaned,
and when you killed the bull, it was raising you.
The dying bull gave birth to you and now you are either
blessed or cursed. The flood of that bull’s blood,
is either going to drown you or liberate you,
but it will not be wasted.”
```

---

## IC-1893: A Game of Chess

- Title: A Game of Chess
- Author (byline): Garrison Keillor
- Work: Definitely Above Average (Audio Book)
- Publisher: HighBridge Audio
- Publication date as stated: Aug 2000
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: GK, TR, SS, TK, TR BRIT LADY, SS COCKNEY, TR BRIT, TR KID, TR BRIT DOLT, TR DOLT
- Teaser before the introduction: Yes
- Spoken words (computed): 1107
- Already set (do not supply): none

### Source block (context only)

```text
Author: Garrison Keillor
Book: Definitely Above Average (Audio Book)
ISBN: 978-1565114128
Publisher: HighBridge Audio
Date (Month/Year): Aug 2000
```

### Introduction (context only: never use it for content warnings)

```text
A Game of Chess by Garrison Keillor
```

### Performance text (classify this)

```text
NOTE: Listen to Garrison Keillor’s Prairie Companion performance of this poem at the following link

http://prairiehome.publicradio.org/programs/2011/10/0 8/videos/#video-1

Legend of Players who provide script and sound

effects for performance:

GK: Garrison Keillor

TR: Tim Russell

SS: Sue Scotland

TK: Tom Keith

GK: I've lost some of life's battles,
I've known defeat and distress,
But I've not met defeat quite so grim and complete
As when I lost to Freddie at chess.
I've been dissed, dismissed, and demoted
I've even been dumped, I confess,
But never disgraced, demeaned and debased,
Until I lost to Freddie at chess.

He is eleven, my grandson,
And he's played a year or less.
And I'll never forget the day that he said:
TR (KID): Grandpa-----You want to play chess?

GK: I'm sort of busy today, I said.
And then he asked me again.
And he set up the board on the living room floor
And we sat down and set up our men. (SFX)

He advanced up the middle and soon my bishop Was caught in a three-way trap. (TK BRIT: Dear me!) I sent out a knight to join in the fight And he got shot in the kneecap. (TR: CRY OF PAIN) My bishop stood in confusion.

TK: Oh dear, what a pickle.

GK: he said.

TK: O Lord lift thine arm and preserve me from harm

GK: And Freddie lopped off his head. (TK: SHUDDER, LOP, PLOP)

I castled my king to protect him And I cautiously put forth a pawn. (TK TIMOROUS PAWN) And in rode his knight (GALLOPING) in open daylight And my other bishop was gone. (TR BRIT CRY, SPEARING, TR FALLS)

(TK AND TR MOUTH TRUMPETS, BATTLE SFX, HORSES, BATTLE MUSIC)

We fought it out in the middle,
We fought it out on the side,
Men in the saddle rode into the battle,
One after the other they died.

The air was filled with anguish,
You could hear the bagpipes cry (BAGPIPES)
The battleground shook from the march of the rook
(TR: GUTTURAL YELL)
And his knights went galloping by. (SFX)

My queen sat calmly knitting Protected by two loyal pawns,

TR BRIT LADY: What's all that shooting and shouting
and hooting
Out on our royal lawns?
We do not choose to lower ourself
To engage in such crude pursuits----
I'll stay right here, and ignore them, oh dear,
Such uncouth uncivilized brutes.

TK: Excuse me, ma'am. It's me. Your left rook.

TR BRIT LADY: Yes? Pray tell, what is it? Don't pester me when it's time for my tea---

TK: It's another queen, ma'am, come to visit.

GK: The other queen rode across the board (MOTORCYCLE) She was not what you'd call polite. She wore a T-shirt that said, "Eat my dirt," Her pants were pink, sequinned, and tight.

A cigarette dangled from her lower lip,
And she carried a six-pack of beer.
An axe and two knives and two .45s
On a long leather bandolier.

She was short and fat and ugly, And she yelled with all her might:

SS COCKNEY: Come out of your tower, you big fat coward, Get your butt on the field and fight!

GK: She planted herself in my queen's face With only a pawn in between.

TR BRIT: Who is that slut on the horse, tut, tut, She certainly is no queen.

Her hair is a mess, and that fishmonger's voice! And her manners --- my, my --- she is rough. Go see to her, rook, and tell her I'll brook No insults from her, no insolent---- (TR STRANGULATION)

GK: And my queen fell flat on her back,
With the other queen's foot on her neck,
And she scratched and grinned and she broke wind
(SFX)
As Freddie whispered---

TR KID: Check.

GK: I looked at my king and he looked at me---

TR BRIT DOLT: Oh dear--- In check? --- oh my. Well, it doesn't look good but maybe I could Find a way to play to a tie.

TR DOLT:
Or maybe that pawn could run to the end
And then be promoted to queen.
I'm sure we've not lost, but at least, at all cost,
One must remain serene.

GK: And he stood there serene and regal and proud As the enemy queen stood and laughed (SS LAUGHTER) As proud as could be, and my monarchy Was feeling understaffed.

A lowly pawn (TK) and a miserable knight (TR) And a rook made up our crew. (TK)

TR DOLT: It looks rather gloomy, but come, rally to me, And we'll figure out what to do. (TR KING DITHERING)

GK: And he brought out his charts and studied his books And he muttered:

TR: Ahem. Let me see. The hypotenuse squared by the root of the hair Of the dog times X over 3.

And carry the two, and divide by Y----

GK: And the handsome royal face Was very concerned, as he carefully turned And moved himself back one space.

And the pawn said--- TK: Brilliant!

GK: the knight said:

TR: Superb!

GK: And the rook said...

TK: Beautiful, sir.

GK: And the king said...

TR: My boy, it's a little known ploy That is known as the Spanish spur.

It was used by grandmaster Peter O'Bleness In 1978, When it seemed he had lost----

GK: And then the King paused, And Freddie said.....

TR: Checkmate.

GK: And his queen moved four spaces back (SS: CHUCKLE)

GK: Killing the rook with one blow (KONK, TK DEATH), And the king looked around at the bloody ground And there simply was no place to go.

TR DOLT: Impossible! Why---- it cannot be. I'll escape ---- I'll find a route!

GK: And the queen said:

SS: Oh yeah? You think so? Ha! Give up, ya big galoot.

TR DOLT: If I only could think--- I must persevere--- Dear me----- a route of escape----

SS: Throw down your sword and kneel on the board And kiss my foot, ya big ape.

TR DOLT: I must not give up ---- my army is scattered - -- I simply have to regroup it.

SS: Hey, king! kiss my foot---- it's over, kaput, What's wrong with you? you stupid?

GK: My head felt strangely empty
It seemed like a terrible joke.
My king was alone on his tiny throne
Awaiting the final stroke. (TR DOLT)

GK: I said, "Look--- there's a polar bear out on the
lawn!"
But Freddie did not blink his eyes.
I guess he had learned you should never turn
Your back on somebody who lies.
My king was dazed----

TR DOLT: Oh well--- toodle-ooo I surrender.

GK: He said with a sigh. And the queen yelled,

SS: Whee---hoo! Boogers on you!

GK: And she looked up and spit in my eye. (SS: SPIT)

SS: Let's play again. What do you say?
You want to be black or white?
Let's play again soon ----this afternoon----
Or after supper tonight.

GK: And later my king said,

TR DOLT: I've thought of a move
I'm sure would have won the day----
Look here--- if this pawn had not stopped but gone on---
Things would have turned out okay.

GK: I've dreamed of that game over and over Of the child who says......

TR: Can we play?

GK: And the battle roar (TUMULT) and the blood and the gore (SWACK, EUUUU) As the bodies are carried away (SFX).......

A game of Parchesi is gentle and easy Or Uno or Sorry, my, yes.

And Monopoly is okay by me But I do not play Freddie at chess.
```

---

## IC-1894: The Geek Wants Out

- Title: The Geek Wants Out
- Author (byline): Ernest Cline
- Work: The Importance of Being Ernest, Pgs 11-2; 14-17
- Publisher: Write Bloody Publishing
- Publication date as stated: Sept 2013
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 629
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ernest Cline
Book: The Importance of Being Ernest, Pgs 11-2; 14-17
ISBN: 978-1938912306
Publisher: Write Bloody Publishing
Date (Month/Year): Sept 2013
```

### Introduction (context only: never use it for content warnings)

```text
There’s never been a better time in history if you’re a geek. Comic books are getting serious big-budget movie adaptations. Captain America Rocks! Video games are getting more realistic and more compelling all the time. Buh, bye, Mario Cart! And Pop culture conventions

(basically huge events where geeks can congregate) are popping up all over the country, giving geeks huge events where they can congregate. Comic-Con Rocks!

Now, I know I’m not likely to turn my love for Ghostbusters or Power Rangers into a lucrative career. But geeks are inheriting the Earth (whispers “Elon Musk”).

By golly, if Elon and Ernest Cline, a regular dude who used to work in IT and did slam poetry, found a way to do it, I can, too! I’m not hiding my true geek nature anymore!

The Geek Wants Out by Earnest Cline
```

### Performance text (classify this)

```text
(Pgs 14-17) At first glance
I probably appear to be a somewhat ordinary,
somewhat average-looking fellow.
Calm, harmless, at ease.

But this is by design. You see, it is through decades of research and rigorous training that I have crafted this façade of normalcy.

And now, through intense concentration,
I am able to function in a social setting.
I can speak at length with educated people about
pertinent matters of public importance,
such as literature,
or the current political climate in Europe.

I am capable of conversing with you
without ever revealing that just underneath the surface
of this manufactured veneer
there hides an altogether different person.

A monster, some might say. My alter-ego.

[My alter-ego] is the opposite of the image I project. He is the antithesis of Cool. He is the last person you want to get trapped in a conversation

with.

He is The Geek.
The obsessive science fiction movie watching,
comic book collecting,
Monty Python dialogue memorizing,
(“Your mother was a hamster and your father smelt of
elderberries!” – Monty Python and the Holy Grail)
Dungeons and Dragons playing GEEK
that I struggle daily to keep hidden from the world.

But The Geek Wants Out. He wants to talk to you. He wants to give you his doctoral dissertation on why The Adventures of Buckaroo Banzai Across the 8th Dimension is the greatest film of all time!

(“Hey, now. Don't be mean; we don't have to be mean, cause, remember, no matter where you go, there you are.”)

He wants to slap you because you’ve never seen Big Trouble in Little China. What? Have you been living in a cave?!

He wants to kick you’re a** in Star Wars Trivial Pursuit. And he will. Because he’s a Geek.

(Question: The young Jedi Knight, Anakin Skywalker, becomes who in Star Wars? Answer: Darth Vader! -- (in a Darth Vader voice: “Luke, I am your father”)

And he wants his toys.
He wants the complete set
in mint condition,
still in the box.

He wants every item on the planet that is even remotely related to Ultraman. Because Ultraman is Airwolf!

He could give a squirt
about sports or politics or rhetoric.
Such things are of no consequence to him.
What matters is the release date of the
next Lord of the Rings movie!

(“One ring to rule them all, one ring to find them, one ring to bring them all and in the darkness bind them.” — Gandalf)

(From When I was a Kid, Pg 11-12) [It wasn’t that long ago when] we didn’t have any fancy Sony

PlayStation video games
with high-resolution 3D graphics.
(scoffs) Atari 2600
with games like Space Invaders and Asteroids. (scoffs)
and the graphics sucked!
Your guy was just a square!

You had to use your imagination!
And there were no multiple levels or screens,.
It was just one screen, forever,
and you could never win.

The game just kept getting harder and faster until you died. Just like life! (deep breath after this diatribe)

You see, The Geek can’t wait.
The Geek has no patience.
He wants what he wants when he wants it.
And all he wants is stupid *stuff*!

He wants his own TARDIS.
He wants his own light saber.
He wants to buy a DeLorean
And he wants to drive it 88 miles per hour.

He wants movies.
He wants to see the Director’s Cut.
He wants the impossible-to-find Japanese bootleg with
6 minutes of never-before-seen footage.

He wants to watch Blade Runner. Again.
He wants to watch Brazil. Again.
He wants to watch A Clockwork Orange.
Again and Again!

But I deprive him of these things, as best I can, until I can no longer ignore his voice screaming in my head.

I am Jekyll. He is Hyde. I am Bruce Banner. He is the Hulk. Especially the Hulk from issues #272 to #378.

But no longer!
I am putting a stop to all this nerdy s*** right now!
I’m an adult, for Christ’s sake!
And this body isn’t big enough for the both of us.
One of us has to go, and it’s gonna be him.
I banishing the Geek forever to the Phantom Zone,
just like in Superman II !
Because, in the end –
there can be only one.
```

---

## IC-1895: Go To Bed

- Title: Go To Bed
- Author (byline): Andy Griffiths
- Work: Just Disgusting!, Pgs 35-52
- Publisher: Scholastic, Inc.
- Publication date as stated: Feb 2005
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1047
- Already set (do not supply): none

### Source block (context only)

```text
Author: Andy Griffiths
Book: Just Disgusting!, Pgs 35-52
ISBN: 978-0439549547
Publisher: Scholastic, Inc.
Date (Month/Year): Feb 2005
```

### Introduction (context only: never use it for content warnings)

```text
Bedtime is supposed to be calm and peaceful . . . but clearly no one told Andy. Join me on a rollicking adventure that begins as an innocent moment on the couch but explodes into a full-scale bedtime war. You’ll witness desperate negotiations, mysterious illnesses, ghost infestations, legal threats, and a highly dramatic countdown to doom. Now let the show begin!

Go to Bed by Andy Griffiths
```

### Performance text (classify this)

```text
NOTE: Items in ( ) should be presented as an aside to the audience . . .

(Pg 35-52) I’m lying on the couch
reading a book (It’s really cool. It’s about this kid who
won’t go to bed)
When Mom comes in
and gives me THAT look (You know the one)

“Andy?” she says, “Did you hear what I said? Put down that book and GO TO BED!”

But there’s no way
I’m going to bed. (I bet the X-Men don’t go to bed at
8:30)
It’s time to stall.
It’s time to beg.

“Can’t I say up for just half an hour more?” “No!” says Mom, and she points at the door. (She thinks that just because she points at the door, I’m going to go through it. Boy, is she in for a surprise)

“Twenty minutes? Ten minutes? Five minutes? One? (I’ve already gained at least a minute, anyway, so I’m already winning, no matter what she says.) Please can I stay up? Please can I, Mom?”

“Come on,” she says, “Mom knows best. If you weren’t so tired, you wouldn’t protest. (Mom’s argument makes no sense. Because if I argue, it proves, according to her, that I’m tired and I need to go to bed. But if I don’t argue, I end up having to go to bed, anyway. What does she think I am? An idiot?)

“You’ve had a good time.
You’ve had a big day.
Just be a good boy
and do what I say.”
I stomp my foot
and shake my head.
“I am NOT a good boy.
I will NOT go to bed!” (There’s no way I’m going to give
in. Especially since Dad’s not home)

But then the door opens
and in walks Dad. (Uh-oh)
He’s got a big frown.
He looks mad.

“Not in bed yet,
Andy?” say he.
“I’ll give you to
the count of three!” (Dad always counts to three. I
think that’s because it’s as high as he can count.)

“One,” he says. He stares at me . . . “Two,” he says. He pauses . . . “THREE!” (The thing is, when he says “three” he’s not kidding around anymore. Better do what he says)

I leave the room.
I count to ten . . . [Count to ten]
And then I go
back in again. (You didn’t really think I was going to
give up that easily, did you?)

“I’ve lost my pajamas!
I can’t find my teddy! (I’m just making this up, of course.
As if I still need a teddy bear – they’re just for babies)
I’m hungry! I’m thirsty!
I’m really not ready!”
But Mom and Dad
ignore what I said.
“ANDY,” they say,
“JUST GO TO BED!” (Okay, they asked for it . . .)

“But I’ve got a sore finger
and I’ve got a sore butt.
I’ve got pains in my legs
and my arm has a cut . . . (None of this is true – I’m
actually 100 percent healthy, but they don’t know that)

“Not to mention my lice
and my chronic back pain
My cloudy vision!
My aching brain!

“My teeth! My tongue!
My eyes! My nose!
My tonsils! My kidneys!
My stomach! My toes! (Actually, the more I think
about it, the worse I feel)

“I can’t go to sleep.

I’ll wake up dead!”
“You soon will be,” says Dad,
“if you DON’T go to bed!” (Did I hear right? Did my dad
just give me a death threat?)

I start to cry. (Not real crying. Just pretend)
I start to moan.
“How would YOU like it
up there all alone?

“How would you like it
in your lumpy old bed
with the lumps in your pillow
sticking into your head?

“How would you like it if your pajamas were too tight and you had to lie there with a wedgie all night?” (I’ve had these X-Men pajamas since I was four. I’ve asked Mom for new ones, but she says they don’t make them in my size – that they only make them for little kids. I think she’s just trying to save money)

Now Dad’s really mad.
He’s pretty near blowing.
“All right,” I say,
“I’m going! I’m going!”

I climb the stairs
toward my room.
I open the door (With difficulty. There’s a huge pile of
clothes on the floor)
and face my doom.

I’m all alone. I’m full of fear. It’s cold and dark and ghosts live here! (The ghosts live in my closet. That’s why my clothes are all over the floor. I’m too scared to open it and put them away.)

A thumping noise!
A spooky sound!
I turn around
and run back down. (I want my mommy!)

Mom looks at me.
Dad shakes his head. (My mom and dad shake their
heads a lot. Especially around bedtime)
“I thought we told you to
GO TO BED!”

“But I’m scared,” I cry,
“I heard a thump.
It came from the closet.
Something went bump!” (It wasn’t the Boogeyman
either. He lives under my bed)

“Don’t make me go back there!

Don’t make me stay!
It’s cruelty to kids!
I’ll tell the SPCA!” (Society for the Prevention of Cruelty
to Andys)

But Mom and Dad
Don’t seem too scared. (Probably because they’ve heard
this one before)
“WE DON’T CARE,” they shout,
“JUST GO TO BED!”

It’s not looking good.
They’re tough nuts to crack.
But I WILL win.
I’m NOT going back,

I’m going to give it
one last try.
It’s time to pull out
My ultimate lie . . .

“But I CAN’T go to bed,” I say to those two. “I can’t go now, I’ve got homework to do!” (Well, actually, it’s not a lie. I do have homework, but I have no intention of actually doing it.)

“It’s too late now,” says my dad.

“Yes,” says Mom, “it’s just too bad!” (They obviously need a little more persuasion. Well, here it comes . . . )

“But if I don’t do it
I’m doomed!” I wail.
“If it’s not in tomorrow
I’m going to fail!” (Mom and Dad hate it when I say the
F-word)

“I’ll be expelled!
I’ll be out on the street
Who knows what thugs
I’m likely to meet?”

“I’ll join a gang! I’ll commit a crime!” (Not just walking when the sign says DON’T WALK, either. I mean a really bad crime. Like running across the road without even looking. And going to bed without brushing my teeth. And writing rap songs with lots of swears in them.) I’ll end up behind bars doing time!

“But there isn’t a jail
that could ever hold me.
I’d have to break out!
I’d have to bust free!

“Every cop in the world
would be looking for me.
A fugitive
is what I’d be. (They’ll probably make a movie about me
and everything)

“Hunted like an animal.
Public Enemy Number One!
Is that what you want
for your favorite son?”

I pause and wait
for my words to sink in. (They look kind of stunned)
Have I convinced them?
Will I win?

“All right,” says Dad.
“Perhaps we were wrong.
Stay up if you have to.
Stay up all night long. (Hmmmm. This could be a trick)

“Just do your homework
Just get it all done.
We don’t want you living
a life on the run.” (No, I don’t think it’s a trick. They’ve
swallowed my story hook, line and sinker.)

I look at my dad.
I look at my mom.
I can’t believe
they’ve bought this one.

This is amazing!
This is great!
I got what I wanted!
I’m staying up late!

But then Mom and Dad
get up out of their chairs,
walk out of the room,
And start climbing the stairs. (Huh?)

“Hey, where are you going?”
I say, scratching my head.
“We’re tired,” says Mom.
“We’re going to bed.” (She does look tired, actually. So
does Dad. It must be awful being that ancient)

“But what about me,”
I say, “here all alone?
I’ll be all by myself!
I’ll be all on my own! (Parents can be SO selfish.)

“You CAN’T go to bed! Not at THIS time of night! You’re older than me! (It doesn’t make sense. The whole point of being a grown-up is that you don’t have to go to bed early.) It just isn’t right!”

But Dad just yawns
and says, “Good night.
Don’t forget to lock up
and switch off the light.” (This has never happened
before. Never!)

“Hey, wait!” I say,
but they’ve disappeared.
I don’t like this --
it feels kind of weird. (I mean, what’s their problem.
Don’t they LIKE spending time with me?)

I’m all alone.
I’m full of fear.
I sit on the couch.
I don’t like it here. (Not anymore)

What was that noise?
I heard something squeak. (No, it didn’t come from me.
Or my butt)
Something went bump!
Something went creak!

It could be a mouse . . .
but it might be a bat! (A vampire bat that came to suck
on my blood. Aagggghhhh!)
No, I’m just being silly,
it’s probably the cat.

But what am I thinking?
I let out a shout:
“WE DON’T HAVE A CAT!”
This is creeping me out!

I try to calm down.
I turn on the TV.
But the first thing I see
is a horror movie. (Normally, I love horror movies, but
it’s not what I need right now)

The living room
fills with horrible shrieks!
It’s a film about ax-wielding
blood-sucking freaks.

I get up from the couch
Like a rocket I zoom –
I shoot up the stairs
and into my room!

Before I know it I’m cozy and calm with my favorite old teddy snuggled under my arm. (All right, I admit it. I DO have a teddy bear. In fact, I have a few. And I like to cuddle them in bed. So what? I bet you would too if you had ghosts in your closet)

I pull the blanket up to my chin.
“I’m safe and I’m warm
And I’m all tucked in. (Sure, I know I didn’t want to go
to bed before, but I’ve changed my mind, okay?)

Yes . . . I know I’m in bed.
But just you wait . . .
Tomorrow I’ll stay up
REALLY late! (Good night)
```

---

## IC-1896: Good Job, Buddy

- Title: Good Job, Buddy
- Author (byline): Kathi Appelt
- Work: Poems from Homeroom: A Writer’s Place to Start
- Publisher: Henry Holt and Co
- Publication date as stated: Aug 2002
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1380
- Already set (do not supply): none

### Source block (context only)

```text
Author: Kathy Appelt
Book: Poems from Homeroom: A Writer’s Place to Start
ISBN: 978-0805069785
Publisher: Henry Holt and Co
Date (Month/Year): Aug 2002
```

### Introduction (context only: never use it for content warnings)

```text
Most people have crushes at some point in their lives. You know you have a crush on someone when you experience a powerful rush of feeling for the person, who you may not even know. You admire them, dream about them, feel happy when you see them or spend all your time counting the minutes until you will see them again. These powerful, and let’s face it, irrational, emotions usually go away after a time, but it is hard to handle this overwhelming attraction when you are in the midst of it. Especially when you’re in the midst of it at work. God job, Buddy by Kathi Appelt.
```

### Performance text (classify this)

```text
Food City, 2 A.M., he tucks in his Red and black uniform shirt as He passes the paperback books Where he knows she’ll arrive soon. All the masters of mystery are there:

Mary Higgins Clark,

Clive Cussler,

Richard North Patterson,

Dean Koontz most of all.
He hurries by, tonight’s the night, he knows it . . .
He loves to work this shift,
The fluorescent lights humming,
A steady thrum just behind his ears.

He and the other boys load cases of Ragu and
Hamburger Helper onto carts,
Roll them down the aisles,
There they slice the cardboard,
A jagged swish of utility knives.
He loves the danger of it, the pull of the blade toward
His thigh, knowing a slip could sever
His thumb or his first finger, could slice
Through his black denim pants, the
Ones he wears every night, required.
It’s a dance he does with the razor blade and boxes

a-one, a-two, a-three . . .

would Lacey dance if he asked?

He glances at paperbacks – Too early, Dean Koontz, he thinks.

He places the jars and bottles in quick Rows on the shelves, labels facing out like flags –

The Republic of Kraft, the United Emirates

Of Nabisco, the Duchy of Birds Eye,

The kingdom of discounts and coupons and

A greeting card for every occasion. Oh, would she dance if he asked? The young night manager, Roy, turns Off the subliminal music – Neil Sedaka, Marvin Gaye, Barry Manilow – Mandy or Mandy – And pipes in the local rock station, KRUD< Heavy metal washes down the aisles in waves of Drums and electricity, it races up his feet, through the Bones in his legs, pumps the blood right through his chest. “Yeehaw,” he wants to scream. “Yeehaw!” he screams. He loves heavy metal, its driving pulse.

Soon he finds his own subliminal rhythm, He’s got the beat . . . canned tomatoes fly Onto the metal shelves, Campbell’s Cream of Mushroom Settles neatly next to Split Pea, boxes of Jell-O – Raspberry, cranberry, lemon – line up like soldiers Waiting for inspection. He stands back and salutes. Who could have dreamed he’d get such satisfaction out of Rows of instant gelatin? Who could have dreamed He’d dream so much about her . . . Lacey.

Roy pats him on the shoulder. “Good job, buddy,” He shouts over the grinding music. Good job, he thinks As he glances at his watch – 3:30. She should be here soon. His steps are full of little hops he can’t stop himself from taking. Good job, he thinks as he sings along With Jack from produce up to his knees In cantaloupes fresh from the Valley, Sweet and round and juicy.

Ahh . . . cantaloups . . . ahh . . . Lacey!

Good job, he thinks, as he walks to cereal, Aisle 14, His favorite – and no wonder – all his childhood friends

Are there

Tony,

Snap, Crackle, and Pop,

Count Chocula,

Fred and Barney . . . But she, she should be here soon, He looks at Cap’n Crunch - - why didn’t you Warn me, he asks? Then lines up the Trix and Kix And Cocoa Puffs, Froot Loops, Cheerios, and Total . . . He’s almost to the end of the aisle, somewhere Between Post and General Mills, near the Check-out counter, he turns the corner,

Smack! She’s there! Lacey,
Parked in the paperback books
Just like he knew she would be
4 A.M., like clockwork, like an alarm
His heart skips at least three beats,
He finishes with the Raisin Bran.

Almost every night, after her shift at the Pancake
House,
Still wearing her blue apron and plastic Lacey name tag,
She floats into Food City, blond hair
Tied back, back, back Lacey.
He holds a box of Grape-Nuts against his chest and
watches . . .
Each night she reaches behind the stack of
mysteries, and pulls out the newest Dean Koontz
. . . no one asks her to pay for it. What is it about
Dean Koontz?
Once after she left, he hurried to paperbacks and
Pulled out the copy she had so recently held.
He brought it to his face and breathed
In the scent of her – pancakes, strawberries,
And something else . . . a mystery.
The music bounced along the linoleum
Filled the bags of miniature marshmallows
And frozen shrimp, filled his nostrils,
His eardrums, his fingers with resonance
So deep he couldn’t name it.
Would she dance with Dean Koontz?
He knew she would.
But what did Dean Koontz know about her
Quiet manner, her punctuality, her small frame,
The smell of syrup?
He sighed. Metallica rolled toward
Him from the loudspeaker. All at once he
Hated Metallica, its ear-splitting wall of noise.
There she was with her mysteries
All alone, and here he was alone with only Grape-Nuts
Tight against his chest. And what he wanted
Was his mother’s old Simon and Garfunkel albums,
Something soft, like Lacey.

Suddenly, he knew he had to
get her attention . . . had to make her see him
had to had to had to . . . that’s when
all reason, all intelligence, all hope of
ever being considered normal again
left his body, walked right out through his skin
stranded him in cereal, where he set the Grape-Nuts
down in the middle of Fruity Pebbles and

without a thought grabbed an empty shopping cart, a wide-nosed bundle of stainless steel, and began to run.

Up and down the rows he went.
Past the bins of onions and Irish potatoes,
The yellow squash and broccoli heads,
Past Orville Redenbacher and Sun-Maid Raisins,
Down the rows of canned vegetables,
Earlyspringpeas-artichokehearts-limabeans-navybeans
Greatnorthernbeans-creamedstylecorn-hominy
The colors flew by in a rainbow beside his vision
Faster he went, then faster and faster,
The basket hummed in front of him. He saw the rice
and pasta, the rows of spaghetti sauce –
Mama mia, holy Toledo, shazam!
He’s almost there, only frozen foods between
Them, Stouffer’s, Borden, Pepperidge Farm,
Faster, faster, he pushes, he pushes, then all at once
The cart is pulling, pulling, pulling . . .
He’s hanging on with all his might.

The cart has taken over. It pulls him past meat And cheese, past paper goods, past pet food, Past the young night manager Roy.

Finally, the magazines! And just past that – The paperbacks – romances, adventures, comics, How-tos, bestsellers, Lacey!

His stomach cramps, his legs drag. He can do this. He knows he can. He must do this. Then, just as he nears the turn, he leaps . . .

The air rushes beneath him, his body flies above The green and white linoleum, he pulls himself forward Both feet are on the bottom bar now, His palms sweat, he’s breathing hard, he takes a gulp, With a mighty heave he jerks the cart toward him

Did he do it? Could he do it? Is he flying? Yes!

Victory! He and the cart are one Balanced on its tow back wheels, a wheelie to end All wheelies! There’s never been another like it In the history of Food City. “Yeehaw,” he wants to scream. “Yeehaw!” he screams. He sails past her And let’s go with one hand, which he raises to her, Let’s go of his heart, which he throws her way, Let’s go of his senses, which he left back there in the cereal . . . Kaboom, splat, errrrrrrt . . . he crashes into Dr. Pepper.

Is there a doctor in the house?

What in the world possessed him? Keebler Elves? The Jolly Green Giant? Oscar Mayer, the great weiner himself?

He’s pretty sure he’ll never again hear Roy
Say, “Good job, buddy.” He’s certain
He’s bruised his ribs. He knows for sure
That he’s going to pay for all that Dr. Pepper.

But like a voice from heaven . . .
“Are you okay?”
He doesn’t think he is . . .
He’s sure he’s not . . .
Maybe he’ll walk again . . .
Oh, what difference does it make?
Al he can see is her blue apron,
Her plastic Lacey nametag,
She fills the aisle with the scent of maple
Looking down at him, so soft, and . . .

There he lay, faceup in a pool of carbonated soda, Soaking into his red and black shirt, bubbling into his hair, spewing Into the florescent air, the boy who took her Away from Dean Koontz, drew her away from all that intrigue, Won her full attention.

Oh tell me, ye of little faith – Who is the master of mystery now?
```

---

## IC-1897: Here, Bullet (Selections from)

- Title: Here, Bullet (Selections from)
- Author (byline): Brian Turner
- Work: Not specified
- Publisher: Alice James Books
- Publication date as stated: Nov 2005
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1116
- Already set (do not supply): none

### Source block (context only)

```text
Author: Brian Turner
ISBN: 978-1882295555
Publisher: Alice James Books
Date (Month/Year): Nov 2005
```

### Introduction (context only: never use it for content warnings)

```text
A harrowing, beautiful first-person account of the Iraq War by a solider-poet. Based upon Brian Turner’s year-long tour in Iraq as an infantry team leader, these poems offer gracefully-rendered, unflinching description but, remarkably, leave listeners to draw their own conclusions on the morality of war. This compilation is for anyone who cares about war, regardless of political affiliation.

Selections from Here, Bullet by Brian Turner
```

### Performance text (classify this)

```text
2000 lbs.

Ashur Square, Mosul

It begins simply with a fist, white-knuckled
and tight, glossy with sweat. With two eyes
in a rearview mirror watching for a convoy.
The radio a soundtrack that adrenaline has
pushed into silence, replacing it with a heartbeat,
his thumb trembling over the button.

A flight of gold, that's what Sefwan thinks
as he lights a Miami, draws in the smoke
and waits in his taxi at the traffic circle.
He thinks of summer 1974, lifting
pitchforks of grain high in the air,
the slow drift of it like the fall of Shatha's hair,
and although it was decades ago, he still loves her,
remembers her standing at the canebrake
where the buffalo cooled shoulder-deep in the water,
pleased with the orange cups of flowers he brought her,
and he regrets how so much can go wrong in a life,
how easily the years slip by, light as grain, bright
as the street's concussion of metal, shrapnel
traveling at the speed of sound to open him up
in blood and shock, a man whose last thoughts
are of love and wreckage, with no one there
to whisper him gone.

Sgt. Ledouix of the National Guard
speaks but cannot hear the words coming out, and it's
just as well his eardrums ruptured
because it lends the world a certain calm,
though the traffic circle is filled with people
running in panic, their legs a blur
like horses in a carousel, turning
and turning the way the tires spin
on the Humvee flipped to its side,
the gunner's hatch he was thrown from
a mystery to him now, a dark hole
in metal the color of sand, and if he could,
he would crawl back inside of it,
and though his fingertips scratch at the asphalt he
hasn't the strength to move:
shrapnel has torn into his ribcage
and he will bleed to death in minutes,
but he finds himself surrounded by a strange
beauty, the shine of light on the broken,
a woman's hand touching his face, tenderly
the way his wife might, amazed to find
a wedding ring on his crushed hand,
the bright gold sinking in flesh
going to bone.

Rasheed passes the bridal shop
on a bicycle, with Sefa beside him,
and just before the air ruckles and breaks
he glimpses the sidewalk reflections
in the storefront glass, men and women
walking and talking, or not, an instant
of clarity, just before each of them shatters
under the detonation's wave,
as if even the idea of them were being
destroyed, stripped of form,
the blast tearing into the manikins
who stood as though husband and wife
a moment before, who cannot touch
one another, who cannot kiss,
who now lie together in glass and debris,
holding one another in their half-armed embrace,
calling this love, if this is all there will ever be.

The civil affairs officer, Lt. Jackson, stares
at his missing hands, which make
no sense to him, no sense at all, to wave
these absurd stumps held in the air
where just a moment before he'd blown bubbles
out the Humvee window, his left hand holding the bottle,
his right hand dipping the plastic ring in soap,
filling the air behind them with floating spheres
like the oxygen trails of deep ocean divers,
something for the children, something beautiful,
translucent globes with their iridescent skins
drifting on vehicle exhaust and the breeze
that might lift one day over the Zagros mountains,
that kind of hope, small globes which may have
astonished someone on the sidewalk
seven minutes before Lt. Jackson blacks out
from blood loss and shock, with no one there to bandage
the wounds that would carry him home.

Nearby, an old woman cradles her grandson,
whispering, rocking him on her knees
as though singing him to sleep, her hands
wet with their blood, her black dress
soaked in it as her legs give out
and she buckles with him to the ground.
If you'd asked her forty years earlier
if she could see herself an old woman
begging by the roadside for money, here,
with a bomb exploding at the market
among all these people, she'd have said
To have your heart broken one last time
before dying, to kiss a child given sight
of a life he could never live? It's impossible,
this isn't the way we die.

And the man who triggered the button,
who may have invoked the Prophet's name,
or not -- he is obliterated at the epicenter,
he is everywhere, he is of all things,
his touch is the air taken in, the blast
and the wave, the electricity of shock,
his is the sound the heart makes quick
in the panic's rush, the surge of blood
searching for light and color, that sound
the martyr cries filled with the word
his soul is made of, Inshallah.

Still hanging in the air over Ashur Square, the telephone line snapped in two, crackling a strange incantation the dead hear as they wander confused amongst one another, learning each other's names, trying to comfort the living in their grief, to console those who cannot accept such random pain, speaking habib softly, one to another there in the rubble and debris, habib over and over, that it might not be forgotten.

The Hurt Locker
Nothing but hurt left here.
Nothing but bullets and pain
and the bled-out slumping
and all the f***s and god****s
and Jesus Christs of the wounded.
Nothing left here but the hurt.

Believe it when you see it.
Believe it when a twelve-year-old
rolls a grenade into the room.
Or when a sniper punches a hole
deep into someone's skull.
Believe it when four men
step from a taxicab in Mosul
to shower the street in brass
and fire. Open the hurt locker
and see what there is of knives
and teeth. Open the hurt locker and learn
how rough men come hunting for souls.

Here, Bullet

If a body is what you want, then here is bone and gristle and flesh. Here is the clavicle-snapped wish, the aorta’s opened valves, the leap thought makes at the synaptic gap. Here is the adrenaline rush you crave, that inexorable flight, that insane puncture into heat and blood. And I dare you to finish what you’ve started. Because here, Bullet, here is where I complete the word you bring hissing through the air, here is where I moan the barrel’s cold esophagus, triggering my tongue’s explosives for the rifling I have inside of me, each twist of the round spun deeper, because here, Bullet, here is where the world ends, every time.
```

---

## IC-1898: Home of the Brave

- Title: Home of the Brave
- Author (byline): Katherine Applegate
- Work: Not specified
- Publisher: Square Fish
- Publication date as stated: December 2008
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1252
- Already set (do not supply): none

### Source block (context only)

```text
Author: Katherine Applegate
ISBN: 978-0312535636
Publisher: Square Fish
Date (Month/Year): December 2008
```

### Introduction (context only: never use it for content warnings)

```text
South Sudan has been devastated by decades of war in which 2 million people have died and 4 million have been forced to flee Today, UNICEF estimates that 17 percent of South Sudan's entire child population is without one or both parents. They have lost fathers, mothers, siblings -- everything dear to them. Kek was one of the more fortunate . . . he escaped the civil war to live with relatives in the United States – the land of the free and the . . .

Home of the Brave by Katherine Applegate.
```

### Performance text (classify this)

```text
The night my cousin Ganwar lost his hand Was the night I lost my father and brother, The night of men in the sky with guns, The night the earth opened up like a black pit And swallowed my old life whole.

Are you glad that you’re here, Ganwar? I ask.

This is a good land, he says.
There’s great freedom here.
But even when you travel far,
The ghosts don’t stay behind.
They follow you.
You come here to make a new life,
But the old life is still haunting you.

We don’t say anything for a few minutes.
Finally Ganwar speaks.
They’re all gone, Kek.
They’re all dead.

I want to hate Ganwar for his words.
But I am too weary for anger.
Already there are so many people to hate,
Too many.

Not all, I finally whisper. Not mama.

****************

A woman sits behind a pile of papers Tall as a termite mound.

“We’ve been trying to get more information on your mom, Kek. Here’s what we’ve got.”

My hope flutters high
Like a bird I cannot catch.
I ready my heart for the words I need to hear:
Found her. Good news. Coming here.
Those are the words she must say.

“This is a very difficult process,”

she says. “Refugees in that area move frequently, And tracking someone down can be Almost impossible.”

“I don’t want to get your hopes up, Kek.
We’ll know more in a while.”
That night,
I try on the school clothes
In the box they have brought for me.
I pick a button shirt with flowers on it
And soft red pants,
But Ganwar rolls his eyes.
Those are pajamas, he says.
You wear them when you sleep.

I try again. Ganwar shakes his head. The kids will eat you alive, he says.

This is bad news, Since I didn’t know that America people Like to eat each other. Ganwar must see the fear in my eyes Because he explains: It means they’ll beat you up.

Ganwar finds a pair of hard blue pants And a shirt the color of sand. Jeans, he says, T-shirt.

In the bathing room
I look hard in the shiny glass.
I wonder if I look
Like an America boy.

I’m not sure if that would be A good thing or a not-good thing.

***********************

They take me to school.

When I see it, I use the words I learned from the TV machine: No way! It’s big enough to graze A herd of cattle in, Made of fine, red square stones And surrounded by many Tall not-dead trees.

This will be your desk.
Have a seat.
She points to a shiny chair
And a little table.

A chair of my own And a table, too?

I’m very sorry, but I can’t, I say softly. I don’t have the cattle For such a fine desk as this.

Oh, she says,
You don’t have to pay for this desk, Kek.
School’s free here.
You just bring your mind
And your smile
Every day, OK?

Carefully I sit. I like very much this new desk.

My mouth will not stop smiling.

********************

It isn’t hunger I feel today.
This pain is worse,
This pain is a question,
The one my heart will not stop asking:
Why am I here,
When so many others are not?
Why should I have a desk
And a pair of fine jeans
And a soft place for my head to rest?
Why should I have the freedom to hope
While my brother and father
Sleep in bloodied earth?

I should not take these gifts
I do not deserve.
Listen, buddy, they say.
I’m afraid we’ve got some more news.
They tracked down the people who made it
To the two refugee camps we told you about.

None of them was your mom, Kek.

***************

I’m in our tent at the camp,
And all around me children and women sleep.
We are too crowded to lie down.
We sleep on each other, legs and arms twined.

I’m not so hungry tonight. Grain came in bags from the helping people today. Mosquitoes buzz at the tent flaps, Louder and louder still, And then I know it is the drone of a flying boat. The gunfire is almost gentle at first – pop—pop—pop, And then it gets closer And the world goes crazy with fear.

Children scream, mothers sob, men threaten.
A fire is burning somewhere close.
My mother takes my hand, firm, sure.
Come, my child, she says, as if we were
going for a walk to look at the moon.
We run from the tent
Pretending a safe place lies just a few steps away.
My mother falls, her dress caught on a bush,
And then the gunfire comes harder,
Flying toward us like hot little stars.
Run, Kek, my mother screams, run now.
I kneel beside her. I can’t leave you, I say,
Or I think I say, for my voice is swallowed by the
roaring night.
My leg’s hurt, I can’t run. You hide in the trees.
You can get help for me when it’s safe.
Go. Now.

And I run
And the trees are waiting
And the men come
With their knives and their guns and their mysterious
hate.

I wait with other children.
I hold a little child and cover her mouth
When she tries to cry.
Dawn comes, silence comes,
Blood and death are everywhere.

And my mother is gone.

************
I awake to no blood, no bodies,
No Mama.
I’m on the sofa, and Ganwar sits on the floor
Next to me.

You were moaning, he says. It must have been a bad one.

I wipe my wet cheeks. Very bad. I was in the camp, And the men with guns came.

Ganwar nods. He clicks on a light And the shadows take form. I still have that one sometimes.

Not like this one. I shiver.

How can you be so sure, he asks. You can’t visit my head. Because mine has truth in it, I say.

Because in mine –
I drop my head in my hands –
Because in mine I leave Mama
And run.
In mine I’m a coward.
And it’s the truth.

*****************

I wait till Ganwar falls asleep. I don’t want to be here anymore. I don’t want to be in a place where My words taste wrong in my mouth. I don’t want to live in a place where Every year the trees must die.

I want to be in a place where the things
I love and know
Are there within my reach.
But where is that place?

Fifteen months later –

The airplanes float in
One by one
But each one is the wrong one
And we wait
And wait
And wait some more.

At last the time comes
And the door opens
And people pour out
But no one is the right one.

One more person comes out,
Slow and searching.
A voice comes,
A voice like laughing water
On my thirsty heart:
My son!
And Mama embraces me
I can’t find words.
There are no words, not in my old language,
Not in my new one.
We walk together
Like one person,
Her arm tight around my shoulders,
And the air is wild with talking and
Laughter and questions,
So many questions,
But I don’t speak.

I take a breath,
I take a step,
I hold out my hand.
She takes my hand
And at last
The right words come.

Mama, I say, Welcome home.
```

---

## IC-1899: Honest/Clean

- Title: Honest/Clean
- Author (byline): Carlos Andres Gomez
- Work: Man Up: Reimagining Modern Manhood
- Publisher: Gotham
- Publication date as stated: Nov 2013
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 575
- Already set (do not supply): none

### Source block (context only)

```text
Author: Carlos Andres Gomez
Book: Man Up: Reimagining Modern Manhood
ISBN: 978-1592408078
Publisher: Gotham
Date (Month/Year): Nov 2013
```

### Introduction (context only: never use it for content warnings)

```text
Joseph Hatcher, a soldier in the 1st Infantry Division of the U.S. Army who did a tour of duty in Iraq in 2004-2005, experienced the struggle of war, politics and ideals first hand. He said: “I love it. I love the fight. It’s just I don’t think we should be fighting in that country. I don’t think we should be fighting a war there for any reason whatsoever.

But when it actually happens, for those few brief seconds it’s – it’s honest, it’s clean. There’s no politics involved when it actually happens.” Honest? Clean? What values in our society can even link war and those two words in the same breath?

The poetry of Carolos Andres Gomez questions the concept of aggression both in war and in everyday life. Why does the world value the ability to fight more than the ability to love? And in the tradition of the peaceful protests of Gandhi and Dr. Martin Luther King: Cries out . . . “Let me be . . . .greater than the flawed society in which I live . . . let me be . . . .greater than the flaws within.”

Honest/Clean by Carlos Andres Gomez
```

### Performance text (classify this)

```text
(NOTE: This “teaser” intro is from the book by Gomez, (ending of Chapter 5), although is not part of the poem itself.

Dr. King and Gandhi were both men. They were both

human. They were both flawed. They were both, at

times, crippled and haunted by their uncompromising

visions of how this life should be lived. Two men with

extraordinary ideas about this world, and many of the

same flaws, struggles, and compulsions with which we all

wrestle. And it is okay to struggle – that is human – but

it doesn’t mean our ideas or actions have to be anything

less than extraordinary.

let me be a mold of soft foam inside reinforced silicone

let me be a soggy piece of plywood nailed across another

let me be a 50 cm scrap of folded cotton fabric

an inch and a half
of worn brown leather
a simple grip of two plates
of poplar wood or stainless steel
something made to hold
someone
or be held
or worshipped
and nothing else

encase me in iron
feed me fuel and gunpowder
make me machine sharp
fingerprint me cutting edge
a smart bomb
a docile land mine

not this vicious human need
don’t make me this clouded, raw heart
all conflict and contradiction
all horror and beauty

let me be a mold of soft foam inside reinforced silicone

but not the upper arm
attached to it
not the soldier saluting
above the flag-encased coffin
of his best friend
don’t call me prosthesis
as the ghost arm salutes
against his right temple

let me be a soggy piece of plywood nailed across another

not a cross
fitted with crude nails and screws
not a symbol of religion or belief
not lighter fluid ignited with a blow torch
not the man shouting to a gathered group
not the pale sheet hiding his cleft palate scar
the nightmares of his alcoholic father
the torment of poverty in Neshoba County, Mississippi
not the stutter he found hate to overcome

let me be a 50 cm scrap of folded cotton fabric

let my color be incidental
neither signifier nor signified
neither red nor blue
neither Athens Park blood
nor Eastside Crip
not the symbol of family
a fatherless son finds
not the tears he hides
the hands he once used
for break-dancing and poems

let me be an inch and a half of worn brown leather

not a belt lashing
a little girl’s face
not the father holding it
not those nightmares of his father
holding his little boy’s hand in scalding hot water
for forgetting his backpack in 4th grade
not the 41-year-old man
that still wets his bed
is still afraid of the dark

let me be
simple
a simple grip of two plates
of poplar wood or stainless steel
attached to a large blade
or a heavy clip of steel tipped rounds
but not the hand
hewing the sugarcane
hacking up a neighbor
the shaking finger about to fire
a woman dressed in a black hijab
in the scope
about to pull a white flag
from her shopping bag
as the 2nd bullet exits
her 4th vertebra

let me be absolute

that woman’s final breath
a heavy release from the heavens
flood rain like sobbing
a god
that never has to answer
for itself

I want to die an idea a desperate myth in the sky

as the whole world kneels
not sure
if this is their last day
on earth --
```

---

## IC-1900: How to Watch Your Brother Die

- Title: How to Watch Your Brother Die
- Author (byline): Michael Lassell
- Work: Poets for Life: Seventy-Six Poets Respond to AIDS
- Publisher: George Braziller
- Publication date as stated: March 1992
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 677
- Already set (do not supply): none

### Source block (context only)

```text
Author: Michael Lassell
Book: Poets for Life: Seventy-Six Poets Respond to AIDS
ISBN: 978-0892551705
Publisher: George Braziller
Date (Month/Year): March 1992
```

### Introduction (context only: never use it for content warnings)

```text
Every popular magazine today has them – Check lists. It seems so simple . . . just follow the steps and life will be easier & happier, relationships more fulfilling & exciting, your home will be organized, your children will raise themselves AND if you act now, you can save enough money by clipping coupons to take that vacation to Tahiti . . . It all sounds so easy. But let’s face it. There are no easy answers to life’s most difficult situations, no checklists to cover as you work through the traumas of life. You survive with God’s Grace and learn by trial and error “How to Watch Your Brother Die” by Michael Lasso.
```

### Performance text (classify this)

```text
When the call comes, be calm. Say to your wife, "My brother is dying. I have to fly to California." Try not to be shocked that he already looks like a cadaver. Say to the young man sitting by your brother's side, "I'm his brother." Try not to be shocked when the young man says, "I'm his lover. Thanks for coming."

Listen to the doctor with a steel face on. Sign the necessary forms. Tell the doctor you will take care of everything. Wonder why doctors are so remote.

Watch the lover's eyes as they stare into
your brother's eyes as they stare into
space
Wonder what they see there.

Remember the time he was jealous and
opened your eyebrow with a sharp stick.
Forgive him out loud
even if he can't
understand you.
Realize the scar will be
all that's left of him.

Over coffee in the hospital cafeteria say to the lover, "You're an extremely good-looking young man." Hear him say, "I never thought I was good enough looking to deserve your brother."

Watch the tears well up in his eyes. Say,
"I'm sorry. I don't know what it means to be
the lover of another man."
Hear him say,
"It's just like a wife, only the commitment is
deeper because the odds against you are so much
greater."
Say nothing, but
take his hand like a brother's.

Drive to Mexico for unproven drugs that might help him live longer. Explain what they are to the border guard.

Fill with rage when he informs you,
"You can't bring those across."
Begin to grow loud.
Feel the lover's hand on your arm
restraining you. See in the guard's eye
how much a man can hate another man.
Say to the lover, "How can you stand it?"
Hear him say, "You get used to it."
Think of one of your children getting used to
another man's hatred.

Call your wife on the telephone. Tell her, "He hasn't much time. I'll be home soon." Before you hang up say, "How could anyone's commitment be deeper than a husband and wife?" Hear her say, "Please. I don't want to know all the details."

When he slips into an irrevocable coma,
hold his lover in your arms while he sobs,
no longer strong. Wonder how much longer
you will be able to be strong.
Feel how it feels to hold a man in your arms
whose arms are used to holding men.
Offer God anything to bring your brother back.
Know you have nothing God could possibly want.
Curse God, but do not
abandon Him.

Stare at the face of the funeral director
when he tells you he will not
embalm the body for fear of
contamination. Let him see in your eyes
how much a man can hate another man.

Stand beside a casket covered in flowers,
white flowers. Say,
"Thank you for coming," to each of several hundred
men
who file past in tears, some of them
holding hands. Know your brother's life
was not what you imagined. Overhear two
mourners say, "I wonder who'll be next?" and
"I don't care anymore,
as long as it isn't you."

Arrange to take an early flight home.
His lover will drive you to the airport.
When your flight is announced say,
awkwardly, "If I can do anything, please
let me know." Do not flinch when he says,
"Forgive yourself for not wanting to know him
after he told you. He did."
Stop and let it soak in. Say,
"He forgave me, or he knew himself?"
"Both," the lover will say, not knowing what else
to do. Hold him like a brother while he
kisses you on the cheek. Think that
you haven't been kissed by a man since
your father died. Think,
"This is no moment not to be strong."

Fly first class and drink Scotch. Stroke your split eyebrow with a finger and think of your brother alive. Smile at the memory and think how your children will feel in your arms, warm and friendly and without challenge.
```

---

## IC-1901: Identity Papers

- Title: Identity Papers
- Author (byline): Jeffrey Ethan Lee
- Work: Not specified
- Publisher: Ghost Road Press
- Publication date as stated: Nov 2006
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1709
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jeffrey Ethan Lee
ISBN: 978-0978945619
Publisher: Ghost Road Press
Date (Month/Year): Nov 2006
```

### Introduction (context only: never use it for content warnings)

```text
Identify Papers by Jeffery Ethan Lee
```

### Performance text (classify this)

```text
You're so far away when the smogged moon crests the
ochre haze a jaundiced leaf
I'm supine on the sidewalk thinking of you as more idiot
questioners lean over me
“Do you have I.D?”
“Name?”
“What day is it?”
“Did he hit you in the head?”

streetlight vapors climb the brick walls escaping these narrows for the high abyss where tranquil darkness flows...

I’m at the bottom of an ocean of black air where atomized trash rivers over me smudging my body like newsprint...

—out of nowhere a woman’s head hangs over me— she’s frantic and sorry:

“I-saw-the-whole-thing-I-saw-the-whole-thing-I’m-praying-for-you-I’m praying for you...

Do you believe in Jesus?”

—just to ease her anguish I rasp “yes” but this witness leaves with no trace.

—just a few days ago by coincidence I bought

a 4 oz. hammer to fix a

broken bed slat but only for me— it was no tree like the bed at the

end of The Odyssey with branches to cradle our bodies together like leaves between heaven and earth...

An officer booms his questions again but as I answer again, voices say:

“D’jou see anything?”

“Yeah... Guy had a hammer— hit the guy who’s down...”

“Were they really fighting?”

“Yeah, for a while.”

“Was it any good?”

“Nah, it was mostly wrestling...”

“Who won?”

“Uh— the guy on the ground...”

But my ear a siren stinging inside
is my evidence
a 16 oz. hammer struck:
each bruise is a fossil in the flesh,
each blood gout sharpens the blurred image of

the acts —it was a fistful of night exploding in my brain but there was no pain

—it was black lightning blinding as it flashed but with no sudden last image the second time

—it was like a gun going off by my ear but without sound it blew my spirit dark the third time—

still no pain —but it wasn’t painless the last—was it lost—time-erased?

Even here I dimly sense
this must not be mere trauma—
it must tell me something.
An eyeless head demands: “WHAT

HAPPENED?” I say what I can again, again (hating them): “We were the last two off the train; he had a hammer in his right, a plastic-wrapped rose in his left...”

Do they—don’t they—believe me? “—a young guy’s pumped up drug-crazed

eyes— then behind me I heard the crash of

shattering glass, a window on the departing train was a

cobweb— my god, I thought of those passengers—

shocked— and he glared straight at me, struck again, eyes hardening—he missed the last

window...”

I see each thing again, saying the history as whole as I can... inside the moment again, again—

and an invisible violence cleaves to every moment, an ax always in our souls not just now, not just here— the rage is futile, empty as a public school’s bars and chain fences singing in cold rain—

and sometimes in our racing blood the hate for any people who have anything is

random— He wasn’t after money—he just wanted to

get even. Suddenly I must see him, “Where is he?”

—a blind head barks, “WHAT HAPPENED?” I see it in flashes fragment-flows

in which only his face is always clear —our eyes’ contact so sharp it aches: “I let him pass and exit up the left stairs

first, not wanting him near me in the dark...” I see the token-sellers in their booth—

cold aquarium light washes their faces blue,
I wait some seconds,
scan the empty left stairway
and whisper, “Hey d’jou see that?”
“We didn’t see nuthin”

(he buzzes like a drowning radio, amplified but muffled) “That guy just broke a window on the R train.” “Can’t do nuthin. Didn’t see nuthin...” “...so, then, I took the right stairs but he’d circled back for me and hid at the turning of the stairs... ‘Where you goin’?’ he grunted ‘You ain’t goin’—You ain’t goin—’ But I pushed past—he shoved from

behind,
I took my heavy book-bag off,
reached the sidewalk first and turned.
He whipped his hammer past me like a

claw,
then smashed my arms backing away
all the way past
the other stairs—
then he saw a couple he knew down

there...”

“WAIT. What couple? Where? Down the stairs?” “Yeah, he went halfway down to them— they tried to—help—” “WHO?”

—he’s screaming at me,
spurting Spanish,
rising so enraged he wants to kill—
though the guy tries to cool him
and I could kick him down these stairs but
— he’s still hu—
“AND?”

“...and, and he came back up swinging, I swung the bag at his head but missed and left it by that woman there... and then we fought...”

—blindness lurches over: “WAIT. What woman? From that couple?” “Don’t know. Wait—maybe...”

I try so hard to see:

that woman (the witness?)

whose eyes well up in fear (for who?)
I fight stunned more than in rage
but he strikes my head—fierce,
his face a frigid happy sneer
—but what if I have to kill
or die? — he’s trying to
while I’m missing punching air...

—only one kick shoves his shoulder slightly back—

He jeers with glee: “Ho—karate, huh?”

—and I know just how he is, how thrilled— how stupid.

I’m backed against the corrugated steel
of another abandoned store,
I swerve toward the street and roar:
“BACK OFF!”

He pauses— his eyes flicker just like he’s scared but when they ice over he lunges...

—and his eyes flash in my endlessly waking

nightmare-daymare scenes
cut all out of order for days, yet each segment yearns
for its sequels
until I have to go back just to walk it through
till it finally flows like a film:
he lunged...
The pounding cut just over my ear—

It was a pitchless siren— all volume without shape or
color,
pure sound without traits like a haze of rage—
my glasses flew to the ground
but I didn’t go down—
he hammered my ribs in back so hard
my knees buckled—I stumbled—
he tackled— then for a long time
we wrestled— his right still
clutching the hammer
while concrete cut us
and asphalt scraped us
struggling close to cars—
he swung again
but his right thigh was so thin
I lifted him
off balance— he flailed
hammering my arm inside, outside,
at my head—
then tore my shirt all down—
I ripped his neck too
infuriating him—we both rose—
he gasped “AW!” swung wild,
his rage a funnel cloud uncoiling
its last blow—

and I never see the memory of my violence; I won’t even realize till days later

when I must have counterpunched
because my ring and middle knuckles were broken open
and one of his short curly hairs
was lodged deep in my gashed skin for
days
—I only see my left darkly in re-enacting rages

three months later, striking his head
to finally kill
that youth with hammer arm recoiling,
floating on extended wings into darkness, an

armed crucifix ...I remember only a sudden

daze—
he was grappling my arms
his hands defending
—he was feebler— I didn’t know why
or when the hammer fell—
but I kicked it away
still grappling him,
scuffling the ground— kicked it further,
dimly knew I wanted that hammer
and could get it—
spotted him retreating and

thought:
now it will be different.
In a flash as long as a falling star
the hammer flowered in my hand,
its head as light as a thorn
to kill, disfigure,
cripple, maim—
I wanted murder so much
I became a bleeding machine.
But just at the instant
he slid into a blur,
the police pulled up
glaring obscene light,
commanding like god out of a machine:
“DROP THAT

HAMMER!”
—they’d saved him!
and they closed around me
while I heard—then saw—him smash
each lens in my glasses.
Having known this before, long ago
saves me from the deepest disillusion—

he’s one blade-edge in the wilding streets
where glasphalt glisters like random junkie jewels
and every concrete slab is stained
by the killed, wretched, despairing, and the
maimed
crumpled in rancid steaming clothes—

it’s not personal—

this world is weapons just waiting to wound,
fists to smash, broken bottles to slash,
boots to crush, bats to fracture,
belts to whip, pins to stick,
and sticks and bricks and names can injure,
and every thing that loves can rape,
every thing that’s cool can kill—
Potato-head blooms: “Do you have I.D? What’s your

name?”

My fingers burrow in my pocket

—pain pours up my arm and overflows my torso— a silhouette takes my wallet, then stands back in

halogen light.

Then that guy says I was to blame,
crouches right over me— in fist-range—
and prods hard: “Eh— you alright? You!”
worried for my attacker if I die: “Eh, you! You

gonna be alright?”

“Get away from me!”

His paper voice skitters away: “I didn’ do nuthin! Hey it wasn’t me— he’s

crazy!”

paper doll shallow: “I didn’ do nuthin! nuthin! He’s crazy—“ streetlight vapor blues into steel-gray—

Blind-eyed dogman broods, “Name... Do you have I.D?”

Potato nudges Gotham: “I already took it from him,” and softer: “What happened?”

Gotham broadcasts: “What happened?”

I say it all slowly over

then carefully beg, “Where is he?”

eyes pleading— Where is he?

Potato eyes darken,

disappear.

They can’t tell who the victim is.

Deeper and deeper fears dawn— you’re so far

away
but this knowledge will hurt you more than me
under the weltering sky where my pain is born at last
—a storm has crushed my clown body to the

concrete— it rains crude oil in my head spills a negative

rainbow in my skull
far away you must be worried now I feel it I’m afraid
the damage is spreading
god it hurts— I’m scared this could be it and what

rage will you feel how will you stand it when I tell you this?

...the sidewalk feels soft as death clean as ether strangely warm I’m numb my hands my arms the wide field of fire roaring before me like a blacktop meadow

the ambulance opens like a time-lapse-photo

flower
```

---

## IC-1902: Incanto – Some Lamb

- Title: Incanto – Some Lamb
- Author (byline): Stuart Rice
- Work: Singing Yet: New and Selected Poems
- Publisher: Knopf
- Publication date as stated: June 1992
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 882
- Already set (do not supply): none

### Source block (context only)

```text
Author: Stuart Rice
Book: Singing Yet: New and Selected Poems
ISBN: 978-0679411451
Publisher: Knopf
Date (Month/Year): June 1992
```

### Introduction (context only: never use it for content warnings)

```text
In a grief-ridden haze after her daughter Michele died of leukemia at age 6, Anne Rice wrote her first novel Interview With the Vampire in only five weeks. As a tribute to Michelle, Rice created the character Claudia, a six-year old vampire child parented by Lestat and Louis, who is granted immortality.

"Writers write about what obsesses them. You draw those cards. I lost my mother when I was 14. My daughter died at the age of 6... When I'm writing, the darkness is always there. I go where the pain is." she explained.

After Michelle’s death, Anne’s husband also used writing as an outlet for his grief. . . His release came through poetry and dealt directly with the overwhelming emotions of watching your child face certain death. Incanto – Some Lamb by Stuart Rice.
```

### Performance text (classify this)

```text
1.
I sit waiting for one of the two kinds of miracle:
the thing as it is, or the thing transformed –
which Tyger?–
There are no lambs here, my juicy head –Time
hath made off with the last lamb left – That’s dead –
Anne sits reading the Chronicle in her nightmare clothes
– Daisy
glossy on couch – I hear a broom & a hose on concrete –
my neighbor,
sweeping his reflection away, no doubt – The
photographs are in the album
each face under its plastic, waiting, for the Real, the
cheek
crushed to cheek
that the brain might arc the gulf between brains –
Orgasm? –
A huge hand comes out of the clouds and squeezes the
brain
and lets it go
and it soaks back up what it let – self drenched again –
astonished,
a mirror in grass –
Is the miracle clarity? – precise definitions instead of
this song? –
Which tyger shall eat the reflection? – If I’m to go on
the terms of the slaughter must be known –
Huge headed child lying on couch beating her lace collar
under which is the pain in her lungs –
The precise names of the medicines
did not help:
6-mercaptopurine prednisone cytoxin methotrexate
dilantin
thioguanine vincristine asparaginase cytocine-
arabanacide
NO HELP –
At 4 a.m. I wake up on hospital linoleum beside her bed
TV
hissing the screen a miracle of chaos not a single word
worth saving they’re all too small throw them back no
limit
to errors the faces are under the plastic in the album
two
months have passed she’s dead that’s it the scissors lie
in
the moonlight on the bedstand clarity is cannibalism –
Sunday – 8 October – 72
Michele now nothing but an emptying dress in the grave.

2.
White day – glare – light on the liars –
Outside the Rainbow Carwash & Lounge
the blacks in ankle-length leather – shoes of shame
vanished –
lightning in leather – All the names of the colors
in the 48 count box of crayolas,
listed – Clarity & Vividness joined – screamy with silky –
The books articulate, intact – poodles barking at
windows – a girl
at a curtain, reading – a white dress drying in a tree –
ruthless clockshop window & enameled scarlet chinese
porcelain egg
on crunchless velvet –
And not one human in the landscape who is not a
metaphor –
Everything metaphor except the metaphors – Gesture is
sculpture –
The swinger stands fixed in nitrogen
and the brain that talked just an hour ago shines in a jar
–
To write this right is to cope with the corpse –
I kissed her in the coffin, the big cool rubber doll in the
coffin,
she smelled like crayolas, her face
a Thought –
Hold on – even in heaven, frozen in gold – in the
boneyard
where the clock coughs, hold on – in the marble, safe
against seepage,
hold – in the dirt, in the neutral, hold on
that you might be able,
should the miracle come,
LET GO.

3. I let her go, I told her, me, squeezing the oxygen bag, Electrocardiagram ink line straight to horizon, no blip, Precision useless again, Chief Doctor In rumpled suit no tie unshaven 5 a.m. & fumbling Intern, This probably his first death, mine too, Anne in her blue robe astonished, after two years, still, at the last moment, ASTONISHED, Fingers to lips, The oxygen tent ripped back, the cooler roaring for nothing, me Squeezing the rubber bag trying to find the rhythm of a breather sleeping That her heart might recognize, begin again, all the time Saying to myself “Don’t come back Mouse don’t come back,” her head Heavy on rubbery neck the veins I’m ASTONISHED Rising to the surface of the skin like crazed lacquer, One Two Three Shots of adrenalin straight into the vein, No response, Me squeezing now the tears dropping bright on the black rubber bag No Response, The head nurse massaging the chest a deep gurgle like a clogged trap NO RESPONSE, Anne “Can’t we do anything, isn’t there anything else we can do?” The Doctor Stands up, “You can stop now, we might as well stop kidding ourselves, she’s Gone,” and my head cocks sideways like the RCA Victor dog & I bend over & her lips part easily & wetly & I give her the long kept sexual kiss of father to daughter, too late Hello.

4. Enough is never enough – That voice comes back – Suave shells of gesture in doors – The photographs just holes full of crayolas, a glare in a book – Never enough – Anne drinks, pregnant with novel, writes & screams – Ten twelve fifteen beers, never enough – Once more small voiced prophetess bald and swollen in final months in red wheelchair spoke the truth & knew no other thing to say & Death ate her & Death wasn’t even hungry – Well, “when the sun goes to sleep it makes a hole in its bed” – There was no key to lock the door no emergency shriek no police the rapist came in under the door a crack too small even for light to get he got – Backwards, that – Forward, Michele as a model – Meanwhile, the poem, for a moment, voice in the gulf, the nightmare articulated, the clock naked, its back off, blood on the toilet paper, the experience sung, done, Incanto, the brain squeezed then released to drink back up what it bled – Clarity & Vividness, both miracles, wed – At last – For a moment – No more death.
```

---

## IC-1903: Journal for My Daughter

- Title: Journal for My Daughter
- Author (byline): Stanley J. Kunitz
- Work: The Collected Poems of Stanley Kunitz
- Publisher: WW Norton & Co, Inc.
- Publication date as stated: Oct 2000
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 453
- Already set (do not supply): none

### Source block (context only)

```text
Author: Stanley J. Kunitz
Book: The Collected Poems of Stanley Kunitz
ISBN: 978-0393050301
Publisher: WW Norton & Co, Inc.
Date (Month/Year): Oct 2000
```

### Introduction (context only: never use it for content warnings)

```text
We all know the stereotype. He’s the clued-out dad who doesn’t know an iPod from IHOP; the guy with the wallet whose relationship with his kids, especially if they’re daughters, is decidedly background.

As the primary male role model in a girl's life, however, fathers influence their daughters in profound ways, from how they see themselves to what they come to expect from men and the world at large.

Men often don't realize the importance of their interactions or may shy away from too close involvement because of their inexperience, or conditioning. Some may even resort to a relationship via the written word rather than face-to-face interaction. Such is the case in Stanley J. Kunitz’ Journal for My Daughter.
```

### Performance text (classify this)

```text
1 Your turn. Grass of confusion. You say you had a father once: his name was absence. He left, but did not let you go.

Part of him, more than a shadow,
beckoned down corridors,
secret, elusive, saturnine,
melting at your touch.
In the crack
of a divided house
grew the resentment-weed.
It has white inconspicuous flowers
Family of anthologists!
Collectors of injuries!

2 I wake to a glittering world, to the annunciation of the frost. A popeyed chipmunk scurries past. the pockets of his cheeks bulging. As the field mice store seeds, as the needle-nosed shrew threading under the woodpile deposits little heaps of land-snails for milestones on its runways, I propose that we gather our affections Lambkin, I care.

3
I was happy you were born,
your banks of digits
equipped for decimals,
and all your clever parts
neatly in place.
Your nation gives me joy,
as it has always given.
If I could have my choice
on the way to exile
I think I'd rather sleep forever
Than wake up cold
In a country without women.

4 You cried. You cried. You wasted and you cried.

Night after night
I walked the floor with you,
croaking the same old
tranquilizing song,
the only tune
I ever learned to carry.
In the rosy tissue
of your brain
where memory begins,
that theme is surely scored,
waiting till you need
to play it back.
There were three crows
Sat on a tree
Sing Billy Magee Magaw.
You do not need to sing to me.
I like the sound of your voice
even when you phone from school
Asking for money.

5
There was a big blond uncle-bear,
wounded, smoke-eyed, wild,
who shambled from the west
with his big bags full of havoc.
He spoke the bear's grunt-language,
waving his paws
and rocking on his legs.
both of us were drunk,
slapping each other on the back,
sweaty with genius.
He spouted his nonsense-rhymes,
roaring like a behemoth.
You crawled under the sofa.

6
Goodies are shaken
From the papa-tree:
Be what you are. Give
what is yours to give.
Have style. Dare.

Such a storm of fortune cookies!
Outside your room
stands the white-headed prowler
in his multiple disguises
who reminds you of your likeness.
Wherever you turn,
down the street,
in the fugues of appetite,
in the groin of nightmare,
he waits for you,
haggard with his thousand years.
His agents are everywhere,
His heart is at home
in your own generation;
the folded message in his hands
is stiff with dirt and wine-stains,
older than the Dead Sea Scrolls.
Daughter, read:
What do I want of my life?
More! More!
```

---

## IC-1904: The Last Deaths

- Title: The Last Deaths
- Author (byline): CK Williams
- Work: Collected Poems
- Publisher: Farrar, Straus and Giroux
- Publication date as stated: Oct 2006
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 787
- Already set (do not supply): none

### Source block (context only)

```text
Author: CK Williams
Book: Collected Poems
ISBN: 978-0374126520
Publisher: Farrar, Straus and Giroux
Date (Month/Year): Oct 2006
```

### Introduction (context only: never use it for content warnings)

```text
Turn on the international news any evening and you will see reports of bloodshed – families being slaughtered, children left crying in the rubble of what used to be their home, wondering where mamma and papa have gone. I don’t need to name a country – the violence and uprisings are becoming more and more widespread. The Last Deaths by CK Williams examines the situation from the perspective of an American parent. How do we explain our world to our children? The Last Deaths by CK Williams.
```

### Performance text (classify this)

```text
1. A few nights ago I was half-watching the news on

television and half-reading to my daughter. The book was about a boy who makes a zoo out of junk

he finds in a lot – I forget exactly; a horse-bottle, a bedspring that’s a

snake, things like that – And on the news they were showing a film about the

most recent bombings. There was a woman crying, tearing at her hair and

breasts, shrieking incomprehensibly’ Because her husband and all her children had been killed

the night before And just when she’d flung herself against the legs of one

of the soldiers watching her, Jessie looked up and said, “What’s the matter with her?

Why’s she crying?”

2. I haven’t lived with my daughter for a year now and

sometimes it still hurts not to be with her more. Not to have her laughter when I want it or to be able to

comfort her when she cries out in her sleep. I don’t see her often enough to be able to know what I

can say to her, What I can solve for her without introducing more

confusions than there were in the first place.

That’s what happened with death. She was going to step

on a bug and when I told her she’d kill it, It turned out that no one had ever told her about death

and now she had to know. “It’s when you don’t do anything anymore,” I told her.

“It’s like being asleep.” I didn’t say for how long but she’s still been obsessed

with it since then, Wanting to know if she’s going to die and when and if I

am and her mother and grandma and do robbers

do it? Maybe I should have just given her the truth, but I

didn’t: now what was I going to say about that

woman? “Her house fell down,” I said. “Who knocked down her

house?” “It just fell.” Then I found something for us to do, but last night,

again, first thing, “Tell me about that girl.” “What girl?” “You know,” Of

course I know.

What could have gone on in my child’s dreams last night

so that woman was a girl now? How many times must they have traded places back and

forth in that innocent crib? “You mean the lady whose house fell down?” “Yeah, who

knocked her house down?”

3. These times. The endless wars. The hatreds. The

vengefulness. Everyone I know getting out of their marriage. Old

friends distrustful. The politicians using us until you can’t think about it

anymore because you can’t tell anymore Which reality affects which and how do you escape from

it without everything battering you back again? How many times will I lie to Jessie about things that

have no meaning for either of us?

How many forgivenesses will I need from her when all I

wanted was to keep her from suffering the same

ridiculous illusions I have? There’ll be peace soon. They’ll fling it down like sick meat we’re supposed to lick

up and be thankful for and then what? 4. Jessie, it’s as though the whole race is sunk in an

atmosphere of blood and it’s been clotting for so many centuries we can

hardly move now. Someday, you and I will face each other and turn away

and the absence, The dread, will flame between us like an enormous,

palpable word that wasn’t spoken. Do we only love because we’re weak and murderous? Are we commended to each other to alleviate our terror

of solitude and annihilation and that’s all?

5.

I wish I could change dreams with you, baby. I’ve had

the bad ones, what comes now is calm and

abstract. Last night, while you and that poor woman were trading

deaths like horrible toys, I was dreaming about the universe. The whole universe

was happening in one day, like a blossom, And during that day people’s voices kept going out to it,

crying, “Stop! Stop!” The universe didn’t mid, though. It knew we were only

cursing love again Because we didn’t know how to love, not even for a day, But our little love days were just seeds it blew out on

parachutes into the summer wind. Then you and I were there. We shouted “Stop!” too.

We kept wanting the universe to explode, We kept wishing it would go back into its root, but the

universe understood. We were its children. It let us cry into its petals, it let

its stems bend against us, Then it fed and covered us and we looked up sleepily – it

was time to sleep – And whatever our lives were, our love, this once, was

enough.
```

---

## IC-1905: The Last Patrol

- Title: The Last Patrol
- Author (byline): Steve Mason
- Work: Johnny's Song
- Publisher: Bantam Books
- Publication date as stated: April 1986
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1675
- Already set (do not supply): none

### Source block (context only)

```text
Author: Steve Mason
Book: Johnny's Song
ISBN: 978-0553051605
Publisher: Bantam Books
Date (Month/Year): April 1986
```

### Introduction (context only: never use it for content warnings)

```text
Some survive by blocking the past. Others by working through it. For the combat veteran of Vietnam, reliving a critical moment in his war can become all too real. Even the smells come back. . . . The Last Patrol by Steve Mason
```

### Performance text (classify this)

```text
In my neighborhood (when I was a kid)
we didn’t know how to cure it,
but we knew how you got it,
“Walk around all day
in your wet bathing suit
and you’ll get Polio!”
That’s it--
We were ahead of the scientists
by about eight years!
Jeez, we were smart.
We also knew how to avoid
the second most dreaded injury
in the whole world,
“Don`t pick that up by yourself!
You`ll get a HERNIA!!!
or worse--the unspeakable
DOUBLE (cross yourself) HERNIA!!!
AARGH”
Forget about that no one
ever knew anybody who had one
(or both)
it was enough that grandmothers
shrieked against them--
and if They shrieked
We listened.
Funny thing about that neighborhood,
we always asked about the kids
you know, years later
like, “Whatever happened to that
Irish kid, Tommy? Ya’ know the one
I mean could hitta ball
to ----in’ Mars
an’ run like a deer--Phizzz,
he was fast . . .”
--He got killed in Korea.
“An ya’ rememba’ da’ Feinstein kid?
Da’ one wit da’ tradin’ cards?
Always flippin’ always tradin’
‘Super Flipper’ he usta call himself . . .
Brudda’ was a big wheel on da’ Exchange?”
--Lieutenant Feinstein MIA in Vietnam.
Funny . . . thing about my neighborhood,
we knew so much about so many things
and mainly about how to love life
(the secret was in sharing yours).
But we didn’t know jack-shit
about keeping our kids safe from war--
forget about that we didn’t even know
anybody who ever found anything good
in one . . .
Maybe that’s why our grandmothers
shrieked so much when we left.
And maybe we shoulda listened.
Like you,
I was raised
in the centerfield of summer,
in a time
when everybody’s grandmother
was still alive
and kids and weeds grew
only to keep baseballs from bouncing
into another world--
It was pure and good
and unfortunately not real,
but it was sweet enough
to last a lifetime
as every boyhood should . . .
For us, it began
with fourth-grade dreams
of long home runs
and loud applause
and ended (for some of us)
when they moved
Jackie Robinson
off second base
never to return
from left field--
I knew right away
something very big
was very wrong
with my little world.
Later, that summer
there was a death
in the family,
but I had already been prepared.
For most of us, though
the “game” ended
behind a locked bathroom door
just down the road from boyhood
about a hundred yards
from the end of the earth
where parallel lines meet
and the concepts of toys and sex
collide
in increasingly frequent,
fantastic visits
(lasting longer than a double-header)
and eventually causing
the dissolution of more secret pacts
among the many alliances of youth
than the surrender
of Nazi Germany--Girls, Yuk!
There, on that very spot
(about a block and half
from the Plains of Runnymede)
Hermes sewed the Levi Tag
into the butt seam of the world
as a monument to the end
of baggy boyhood
and the incessant
between-the-teeth whistlings
of ”the very young at heart.”
And Johnny’s Song Begins . . .

Johnny`s Song (I call it)
the song of each man`s soul
who has come from a boyhood
such as ours
and gone to a war
such as we have known
and as yet has no DEROS.
I would gladly put it to words
and play it for you
(if only I could) on a flute,
but what the hell,
you know it by heart anyway . . .
I heard it once
somewhere between the finite
mathematics of harmony
and the infinitely inescapable
possibilities of loneliness.
Heard it, in the sad music
of solitary whales
in the North Atlantic
and recognized the voice
of my own soul
swimming also
in the dark
in the cold
under the implacable pull of the moon.
When a man is lost
he returns to the last known thing--
It is possible the same is true
for souls.
I have rummaged, therefore,
through childhood
for the essence of my manhood
and the substance of my humanity.
I have found only where the boy
was born--and where he learned
to trust and to love,
but since I am no longer he,
it becomes a vague exercise
like viewing the cosmos
through a kaleidoscope
(delightful, but without value).
A lot of good men died in Vietnam.
But like some of you, I was born there.
So sometimes (like you)
I just get tired of waiting for me
to feel like me again
and on days like that--
late nights actually
(the days after Nam
have always come and gone
like meaningless ricochets)
I just pull back the final perimeter
of my fat and bivouacked-by-the-fire
middle age
to the very edge of the TV,
hunker down into the chair
and get black-faced in my mind
(and blank in my heart)
ready to slip under the wire
for one last patrol.
And with the last strains
of the “Star Spangled Banner”
in my ears
the tube turns the night into snow
and I am gone--
Quietly,
quickly,
past the concertina
on the downward slope
of my nightly fears
into the no man’s land
from which my instinct draws
the knowledge to explain
(in dream symbols) all I failed to see
when first I lived it.
Tonight I am moving smoothly
(even in my pain)
and I am missing nothing--
I am a one man
search and recollect mission.
Back. Way Back, the way I came in.
And this time maybe I’ll find it.
Whatever “it” was that went wrong.
Christ, it could be something
obvious that was there all along--
like being party to the least
experienced group of combat soldiers
ever sent into combat.
Some killers we showed up to be!
Of the nearly three million guys
“in country”
probably eighteen of us killed chickens
for lunch down on the farm--
one hundred and twelve
caught fish in a stocked pond
(big enough to keep)
and the rest of us manicured killers
let the likes of Burger Chef
do our bludgeoning for us.

Really, did you ever kill a chicken?
I never killed a chicken. Shit.
Where I come from kill a chicken
spend the rest of your life
in reform school. It was like a jingle.
I never killed anything.
First thing I ever killed
was no kind of thing at all--
it was an enemy soldier
which is a hell of a lot easier
to say than
the first thing I ever killed
was a man.
See that? Back to childhood again.
How unprepared for real life
we were.
I’ve got a sister forty years old
I don’t think to this day
my father has the heart to tell her
pork chops come from l’l piggies.
Damm! I go off to war and what do I get
in my bag of tricks from childhood?
What is it I tap into in crisis?
Thirteen Ralph Kiners
Triples in the entire starting lineup
of the 1952 Brooklyn Dodgers
and the top half of the
game winning Spalding Hi-Bouncer
that warped off the end of my stick
into a dreaded “egg-ball”
that was so vicious
that when poor Dumb-Eddie
clamped his mitts on it--it split
(and the run scored).
Pretty tame stuff
compared to Madam Tich’s
little boy, Nguyen, anyway
who came to kill me one afternoon
in the Plain of Reeds
(not near Runnymede)
and brought his own duck with him
as an appetizer
(strung upside down from his belt).
And oh, oh there it is!
Careful, just like it was real life
step over those same trip wires
like the first time.
Can I screw up? Can I blow myself up
in a late-night reverie
(a little on the frantic side)?

Can I change the past
and be dead all along? Oh, shit:
And there’s the pagoda
where I drop my Zippo
and bend to pick it up
as the rounds hit the wall above me
like freight trains
and I become the first guy in history
who can say cigarette smoking
saved his life . . .
I am moving even better now
and my guts tell me
that in these next moments
I will be reunited with myself
in that irrevocable moment of truth
when last my mind and body, heart and soul
were as one . . .
There it is, the church in the rain
(on this side of the canal from Cambodia).
On both sides
the flood rises
the war worsens
and the monsoons are no more interested
than typhus or the plague,
Through the storm the church looks
like a shadow
and in my mind it has ever remained so.
That night, when we were ambushed,
I was certain it was the only building
left standing between Kien Phong Province
and Augusta, Georgia.
When he woke up next morning,
Nguyen must have weighed 90 lbs.
(I could have killed him
with my bad breath)
instead somebody shot him 5 times
(the duck they missed completely).
When he crawled out of the water
to die on the thick mud outside
the church door.
(the flood left little room)
I had just left the church
preferring the rain and the danger
to the roistering inside
where cooking fires had been started
and men rode each other`s shoulders
to drape the wet clothing
over the support beams,
pitifully decorated with faded
pink crepe paper
scalloped and twisted by some long gone
custodian of the faith.
After several sharp words from me
they reluctantly gave up the torture
of two hapless captives
and as I turned to leave I noticed
that the dais was covered
with flat sheets of uncut
French grape soda cans
and on the podium an erect
decapitated statuette of Christ stood
(the head placed gently at the base).
Outside I sensed Nguyen’s presence
before I saw him
almost directly
at my feet;
Even in the rain
and the faint light of the church
his wounds were atrocious.
I sat with him in the mud
and put a soggy cigarette in his lips
to allay his fears of me
and stroked his hair,
“Toi com biet,” (I don`t understand)
he whimpered.

I was silent.
He was in unbearable pain.
He moved his head with great effort
(and even greater meaning)
to the pistol at my side.
Back inside the church
the muffled “puff”
which blew Nguyen’s lights out
was barely discernible
above the rain
(but for me it still echoes).
I stopped by this dais
and spoke directly
to the Christ head,
“Toi com biet.”
Arms at my side
I turned into the laughter
of the smoke-filled room
into the gold, gap-toothed smile
of a little man with a big knife
holding Nguyen’s duck over his head
like a trophy--
raising my head to the rafters
I howled like a mad dog,
“ANYBODY FOR A LITTLE STICKBALL!?”
```

---

## IC-1906: Love Poem Medley

- Title: Love Poem Medley
- Author (byline): Rudy Francisco
- Work: Helium
- Publisher: Button Poetry
- Publication date as stated: Nov 2017
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 999
- Already set (do not supply): none

### Source block (context only)

```text
Author: Rudy Francisco
Book: Helium
ISBN: 978-1943735198
Publisher: Button Poetry
Date (Month/Year): Nov 2017
```

### Introduction (context only: never use it for content warnings)

```text
Ah, love. The elusive and ephemeral chemical experience that all humans want and crave. It's so powerful that it can be hard to describe. Let's face it: you don't want to trip over your words when you're trying to convey to someone just how much affection you have for them. Love is taking a risk; but the risk is always, always worth it. In fact, a Chinese proverb describes love in this way: “Being deeply loved by someone give you strength, while loving someone deeply gives you courage.” So here’s a bit of courage . . .

Love Poem Medley by Rudy Francisco
```

### Performance text (classify this)

```text
To the Girl Who Works at Starbucks, Down the Street from My House on Del Mar Heights Road, I Swear to God I’m Not a Stalker (Pg 21)

When I asked you for a chai latte,
what I meant to say was:
”I was walking past. I saw you in the window.
I only came in here because I had to know
what your voice sounded like.”
But instead of saying that, I got really nervous
and just ordered the first thing on the menu.
I don’t even know what “chai” is.

Or a latte, for that matter.

I imagine, when God made you, he cussed for the first time. He turned to an angel, gave him a high five and said: “Goddamn, I’m good!” You are that beautiful. I spent the last five days trying to figure out how I’m going introduce myself to you properly, and I think I’ve finally figured it out. It’s going be something like… “Hi.”

That’s all I got so far, but I think it’s a good start.

Correctly (Pg 17)

. . . I want you to come to me like an afternoon, come to me slowly as if you were a broken sunset with a lazy sky on your shoulders. If you let me be your sunlight, I promise that I will penetrate your darkness until you speak in angel wings. Pull me close to you, tell me that you love me, and then scratch your future into my back so I can be everything that you live for. I promise that I will love you as if it’s the only thing that I’ve ever done correctly.

If I Was a Love Poet (Pg 23-24)

I’ll be honest, I’m usually not really a love poet. In fact, every time I try to write about love, my hands

cramp just to show me how painful love can be and sometimes, pencils break just to prove that every now and then, love takes a little more work than planned. I’m not much of a love poet. But if I was to wake up tomorrow morning and decide that I really wanted to write about love, my first poem would be about you.

About how I loved you the same way that I learned how to ride a bike. Scared, but reckless. With no training wheels or elbow pads so my scars can tell the story of how I fell for you.

I’m not much of a love poet, but if I was, I’d write about

how I see your face in every cloud and your reflection in every

window. I’ve written a million poems, hoping that somehow, you’ll jump

out of the page and be closer to me. Because if you were here

right now, I
would massage your back until your skin sings songs
that your lips don’t even know the words to.
Until your heartbeat sounds like my last name.
And you smile like the Pacific Ocean.
I want to drink the sunlight in your skin.

If I was a love poet, I’d write about how
you have the audacity to be beautiful
even on days when everything around you is ugly.
I’d write about your eyelashes, and how they are like
violin strings that play symphonies every time you blink.

If I was a love poet, I’d write about how I melt in front of

you like an ice sculpture every time I hear the vibration in your

voice. and whenever I see your name on the caller ID, my heart

plays hopscotch inside of my chest. It climbs onto my ribs like monkey bars, and I feel like a child all over again.

I know that this is going to sound weird, but sometimes, I pray that God somehow turns you back into one of my ribs just so that I would never have to spend an entire day

without you. I swear, I’m usually not a love poet, but if I were to wake up tomorrow morning and decide that I really wanted to write

about love, my first poem would be about you.

Again (Pg 25)

Last night, I had a dream. And in this particular dream, I died in my dreams, woke not knowing I was still sleeping, decided to walk. That night, I walked in my sleep, I slept in my walk, I walked backwards until I saw you for the first time, and I could barely muster the courage to introduce myself all over again. You see, I’ve been trying to find the right words. I’ve been trying to take the right steps for what seems to me like thousands of years, but something always seems to go wrong between us. We lived in Egypt, I was the Pharaoh’s slave, you were his daughter. Loving you led to my death, they claimed that I seduced you, and after they stole my life, I was resurrected as a mason. I made the foundation for your house. We met eyes for two seconds, you left, and I didn’t see you again until I died. I came back as a caterpillar. I turned into a butterfly, I landed in the palm of your hands, you brushed me away, and the rejection killed me. When I awoke, I was a kick drum, you were a snare, we were both owned by this drummer named Cozy Cole, and when he died, so did we. But I came back just to look for you. I left notes in random places, hoping that you would stumble across them. I carved our names in trees, and then prayed that it would jog your memory. I whispered your name in the wind, hoping somehow, maybe some way, my voice would reach you, but it didn’t, and I died. I died early. I died young with breadcrumbs in my hand, so they buried me and when they buried me, they put these coins over my eyes, and I used them as bus fare to get back to Earth, just so I can look for you.
```

---

## IC-1907: Manly Man

- Title: Manly Man
- Author (byline): Brian Hathaway
- Work: All the Hits So Far But Don’t Expect Too Much . . .
- Publisher: Relevant Books
- Publication date as stated: Aug 2005
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 930
- Already set (do not supply): none

### Source block (context only)

```text
For Both Poems
Author: Brian Hathaway
Book: All the Hits So Far But Don’t Expect Too Much . . .
ISBN: 978-0976364238
Publisher: Relevant Books
Date (Month/Year): Aug 2005
```

### Introduction (context only: never use it for content warnings)

```text
A Manly Man carries himself with pride and self-assurance. He is not a follower and may not be a leader but, is unswayed by external forces. He goes where he wants, wears what he wants and says what he wants with no fear of condemnation. Brian Hathaway is the quintessential Manly Man – unafraid to speak his thoughts and to explain himself in a world that is often unexplainable. In No Worries . . . I’m Going To, Hathaway outlines a typical day in the life of a manly man . . . with commentary!
```

### Performance text (classify this)

```text
No Worries . . . I’m Going To
Wait Wait Wait Wait a minute
Hold up
STOP
. . . .The press

I woke up today without that 5 million pound boulder of stress on my chest and now I feel blessed and can rest.

Oh! to rest these weary extremities that have been inflicted with infirmities unseen or experienced by them before So tell me, what does the future have in store? I don't know

I'm just going to let today be today, I'm going to wake up this morning with a smile on my face, look in the mirror brush my teeth and not wrack my brain wondering whether she’s going to call me or not because when a girl says, "let’s just be friends," what she really means is "I'm never going to talk to you again."

Accept it Move on I just did

And after that I'm going to put on my play clothes, go in the front yard and climb that pecan tree like I did last week, but this time I'm not going to get halfway up it and start debating whether morality is . . . A social adaptation A product of Evolution Or put there, by God I'm just going to climb the thing and have fun like I did when I was a kid

And after that I'm going to go to vertebrate zoology class and listen to my boring, lifeless instructor talk about how there are 50 different species of minnow in Arkansas alone.

But I'll smile
Nod
SHOW INTEREST
Act interested

(because that really is interesting if you think about it . . . Think about it)

And then after that I'll go home and have lunch. The same ol' boring lunch again! Two more fricken' frozen Monterey jack bean and cheese burritos with a glass of distilled water and an orange. But I'll give thanks that I do have food to eat because so many people don't

And after that I’ll go to work and paint But I'm not going to paint that boring eggshell white on that old lady’s wall like she requested . . . no, I'm not going to do it. I'm going to pretend I'm a juvenile Leonardo daVinci and paint a stick figure masterpiece of a young couple frolicking in a field of flowers with little butterflies and gophers popping up here and there. (I'm sure the old lady will appreciate it later in life)

And after that, I'm going to have dinner with my Paw Paw and when he cries to me about how his arthritis is bad -- his own daughter rejects him -- he's sad, I'll put my arm around him and listen -- watch his old weary eyes glisten as he experiences my love for him.

And after that I'll go home, sit on the floor and start singing songs to the one that gave me this joy that I'm feeling, but it's more than just some fleeting feeling, it's eternal truth in which I am reeling.

And then at night I lay my head to rest without the slightest bit of fright or fret knowing I made the day the best I could

And that God truly is good TRANSITION

So you see . . . A Manly Man has nothing to do with how much you can bench press, or what kind of truck you drive or how many women you have added to your “repertoire” - - Nope being a Manly Man has nothing to do with your military wardrobe or 1/8 “ crew cut or the anchor tattoo on your bicep. Brian Hathaway further defines a “Manly Man” in his poem by the same name.

Manly Man

I don't want my long hair
pretty green eyes with
no I do not have on mascara
Eyelashes
Skinny figure
Undersized T-shirt

Hips
Shake
Too
Much
when I walk
Confuse anybody . . .

I am a Manly Man!

Within this sissy frame
obviously rib laden chest
lies a heart
that beats
to the drum of a
Native American ritual dancing
wildness

It pumps an ever-cascading supply of untamedness that a herd of wild mustangs have yet to grasp.

If danger lurks about, I will seek it out. If adventure abounds, there I will be found. If a damsel be in distress

I will show her who is best.

I am a Manly Man!

Because I don't flush
and I leave the lid up.
Girls don't break up with me
I break up with them first!

I don't shave the hair on my face (because I still can't grow facial hair yet, but when I can I

won't.) Because beards are tough.

I fart
burp
spit
when I want

Not caring who's nearby

Disrespect my momma and I will punch you in the eye!

I am a Manly Man!

Or am I?

I tell my guy friends that I love them. And sometimes, sometimes, I even hug them. No because I'm not gay. But because I love em'.

And when people talk
I try to listen
a spirit of compassion
That's my vision.
Surely I am a Manly Man
I want to be loved
and have love
and give Love.

Although I am looking for that beauty
Not helpless
But wants to be rescued.
The Damsel in distress
Man
Woman
Myth
True.

I will fight for her.
Climb the highest tower for her
Love her.
Share with her.
Delight in her.
Be her warrior.
Her protector.
She will be my crown
and I will be hers.

My Masculinity will be passed down and affirmed to my sons.

Each of my daughters will know they are lovely and deserving of authentic romance.

Society tells me all day long

That I have defined manhood completely wrong.

But you ask any honest man and he will agree You ask any honest woman and she too will see

That I am a Manly Man!
```

---

## IC-1908: Me and My Big Fat Mouth (The Bus Story)

- Title: Me and My Big Fat Mouth (The Bus Story)
- Author (byline): Mike McGee
- Work: Not specified
- Publisher: The Wordsmith Press
- Publication date as stated: 2003
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 911
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mike McGee
Book/CD: World’s Greatest Poetry Slam 2003
ISBN: B000F1PO3W
Publisher: The Wordsmith Press
Date (Month/Year): 2003
NOTE: Only published in CD Audio Format. Check
requirements in your state for “publication” rules before
performing.
```

### Introduction (context only: never use it for content warnings)

```text
Infatuation... we're in love with it! Millions of people live in anxious hope of experiencing IT as soon as possible... and over and over again... if necessary. Come to think of it, infatuation has become a popular model for love itself, and at this very moment, infatuation fever is directing the most critical intimate choices of an enormous sub-culture of teens. Infatuation crosses all race, gender, weight ranges, social classes and yes, even cultural cliques . . . there is no rhyme or reason, no rescue from it’s clutches . . . . IT can make you do and say things you never thought possible. . . . Trust Me and My Big Fat Mouth by Mike McGee.
```

### Performance text (classify this)

```text
In the summer of 1991
I was 15 years old and 200 pounds
I had spent the weekend in Reno with my
family and we were heading back home
to San Jose on a Greyhound Bus which was, always dull.

I rested, bored on the harsh cloth and vinyl seats second to the last in the back of the bus while listening to Cool Mo D on cheap headphones and praying for a stranger to consume as much of my time as possible.

We got to Sacramento and the coolest chick
of all cool chicks got on the bus alone
Her perfume preceded her entrance.
I looked up to see a flash of black.
Black everything.
Pants, boots, makeup, shirt, hair, and book bag.
She was Goth, I guess, but I didn’t know what that
meant back then.
But she was.
She was gorgeous.

She was a mystery sitting right behind me
in the last seat on the bus
I stalled and stalled
She was drowning out the world with
her own headphones—I had to talk to her
So I hopped up and spun around and
kneeled on my seat like those annoying children
resting my chin on the top of the backrest.
She looked up at me.
Reclined and slouched into the book she was reading.
She smirked, like my presence was unusual,
but my spontaneity was somewhat punk rock and
welcome.

I can’t remember what exactly started the conversation,
but within fifteen minutes, she had put her
headphones and book away
She told me she only listened to college radio;
now, I had to listen to college radio
She was my age, but she was exotic and cultural
She was dark and lonely and found very little humor in
the world,
but I could make her laugh—Boy, could I make her laugh.

Up until then, humor had always been my wall
To joke and tease was to defend and protect myself
To deflect any words that could hurt me when I was a
boy
I used my humor to get to them before
they could to me, and I got inside this girl
But the more she opened up, the more I didn’t
In an hour we were friends. In another hour
we would be comfortably flirting and joking
around like two people who would eventually
become dorm room lovers.
She thought I was funny.
She thought I was special.
She told me she thought my chubby face was cute
and really wanted to get to know me.
This was the easiest thing I had ever done
We were 15 minutes away from home,
she gave me her address, and in seconds
I realized it would only take me half an hour
and two buses to get from my house to hers.
I promised I would visit her as often as possible.
I even considered transferring to her high school to be
near her.
She was beautiful.
And I wasn’t, and we fit like the last two pieces of
this glorious puzzle completing the most complex
work of abstract art anyone has ever seen.
And we could feel it. There isn’t a genius in
the world that could explain to us what was
happening, but we didn’t care about details.
We were the world’s youngest scientists
committing ourselves to cosmic chemistry on a
Greyhound bus.

I wanted to kiss her so badly and I knew she’d
let me if I could just walk her home.
But I didn’t care if I ever got off that bus,
as long as she was
there with me.
We laughed and talked like old friends.
And when we had nothing to say
we just smiled comfortably,
because we both knew the energy between us was magic.

Nothing could stop us, nothing could hurt us. She was the first person I was willing to grow up for. Days could’ve gone by and we wouldn’t have noticed. We had gone galaxies in a relationship that still had universes to build on. She had grown so pleased with my presence that she had slowly slithered down into her seat, slouching ever more. This position of her body forced her to lay on her side. She looked comfortable but was unaware that her entire pelvic area was pointed right up at me. I pretended not to notice, until I joked:

So, do you spread your legs for every guy you meet?

Evil dreads swarmed her face.
At warp speed she ripped her cold book and headphones
out of her bag.
She opened to her dog-eared chapter and
blasted the Smiths into her brain.
I apologized like a cheating husband.

So close to tears, she wouldn’t look at me.
Her guard was down and I attacked.
It only took her 7 seconds to become a stranger all over
again.
What was I thinking?
She wasn’t ready for that. She didn’t deserve that.
We were different. We were gonna get married.

The humor that I had always used to
make friends had backfired for the first time,
but to this day I know I lost more.
I lost the opportunity to walk a cool chick home.
I lost my very first kiss from some awesome
faint black lips.
Faint, because she covered her mouth every
time I made her laugh, wiping away
the gothic façade that first attracted me to her.

It’s been so long. I could’ve fallen in love with her. And boy, did I.
```

---

## IC-1909: Meatloaf

- Title: Meatloaf
- Author (byline): Derrick Brown
- Work: Scandalabra: A Collection of Poetry and Prose
- Publisher: Write Bloody Publishing
- Publication date as stated: 2009
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 509
- Already set (do not supply): none

### Source block (context only)

```text
Author: Derrick Brown
Book: Scandalabra: A Collection of Poetry and Prose
ISBN: 978-0978998967
Publisher: Write Bloody Publishing
Date (Month/Year): 2009
```

### Introduction (context only: never use it for content warnings)

```text
Nearly one out of every two marriages ends in divorce these days. And though the divorce rate has leveled off recently, one million new children a year are living through the breakups of their families. When a father abandons his family, the break up is especially difficulty for the mothers and sons who are left to cope alone. Derrick Brown recalls in his poem “Meatloaf” a discussion he had with his mother regarding the meaning of love and commitment. Meatloaf by Derrick Brown.
```

### Performance text (classify this)

```text
My mother is washing the dishes and singing a song about someone dancing on the moon.

She stops to pat the globe of her stomach. “So full.”

I help her with the dirty meatlof dishes and pass them

from the table The gunk slides through the soap and the green goo slips across her strong hands.

There is a flash of light every time she turns
her palm through the soap.
My mother has a small diamond
that she received on her wedding day.

It was given to her by my father, as a symbol.

It was very affordable.

I always asked her why a diamond meant that you loved someone?

Why not a brick, snail, wombat, or cat brain?

Why not give someone a pair of handcuffs to show the world that this person will be with you

forever?

Why not a steamroller and you can tell your love that your world is flat without

them?

Why not give them a trophy of a zombie to prove that you will kiss their brains out?

There is diswashing liquid in a brigade of bulging bubbles and the “tink spink” of moving plates, and my mother is singing again.

To her, the diamond ring was a cheap, special reminder:
--my dad’s bright trying eyes,
--a relationship of exhausting sacrifices,
-- a beauty once hidden in the earth, but revealed to the

hand of the searcher.

The garbage disposal does its horrible growl.

My mother says she loves the way the diamond catches the light and shoots it into your eye like sitting across from

someone who just bit into fresh grapefruit.

The filthy forks sifted through her hands as the

disposal burled: “Gnrlwygnlrygnlrywy.”

She stopped singing and turned off the disposal. Her face turned the color of the kitchen sink walls.

Water off. She tosses through the plates. She pulls out a rubber doo-dad to check the garbage

disposal, continues this for about ten minutes.

I wait for her to say it. I can feel my face, ready to burst like a cloud.

“It’s gone. I can’t believe we were just talking about it

and it’s gone.” She patted my head and handed me a paper towel.

“It’s okay, Mom. It’s just a thing.”

“Not really.” She starts to weep a little. “Excuse me.”

She goes to the bathroom to blow her nose, returning, kissing my head and going back to washing the

dishes with me, scanning every bubble’s gleam for the rock.

I roll my damp paper towel into a ring and give it to her. “If we weren’t blood, I’d marry you. And I’d stick

around.” She replies, “That is sweet, Illegal, a little weird, but so

sweet, Derrick.” She grabs some tape so it would stay wrapped up.

I sneak outside to the neighbors’ place and steal her a brick from their garden.

When I come back in, she smiles and begins to sing that song of someone somewhere dancing on the moon, a song about a boy spinning in the dark with a beam of light.
```

---

## IC-1910: My Darling Sara

- Title: My Darling Sara
- Author (byline): Shane Koyczan
- Work: Visiting Hours
- Publisher: House of Parlance Media
- Publication date as stated: Sept 2005
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 967
- Already set (do not supply): none

### Source block (context only)

```text
Author: Shane Koyczan
Book: Visiting Hours
ISBN: 978-0973813104
Publisher: House of Parlance Media
Date (Month/Year): Sept 2005
```

### Introduction (context only: never use it for content warnings)

```text
Men grieve differently than women. Our cultural roles make it difficult for men to look for support, and harder again to accept it. Men are so often silent, solitary mourners who immerse themselves in activity and private, symbolic rituals. They feel profoundly, but often can't express the depth of their loss. Coping with the death of a loved one is never easy, regardless of how old you are when that loss occurs. However, turning a tragedy into a tribute is one of the ways that the survivors can keep going and keep living after a traumatic loss . . . A tribute to My Darling Sara by Shane Koyczan.
```

### Performance text (classify this)

```text
The failing use of my right hand
isn't actually the failing use of my right hand
It's just another way to tell the time
and I'm ticking
so I've been picking myself up at bars
with a bottle in each hand
but I never give myself any play
I only make plans with myself for the day after next
but by the time the sun swings back around into position
I forget the context of why I asked myself out
in the first place

did I think I was going to score?

I let a stranger pour me one more she says my name is sara

doesn't take much more than that to start a relationship

my darling sara
cleans rooms for a living
giving her youth and beauty
the dirt and dust
understands more than most
that family must be a foot you put forward first
you must weather the worst together
but having never met her family
she places love above all else

then protests that I use the word love too freely in poems and I should really just say what I mean

and I suppose what I mean most is that I'm trying

she's been buying me time on a maxed out credit card arms scarred from selling her own blood to pay down the debt tells me she doesn't mind going broke just so long as I can give her a little sweat she says try

so I do my best impression
of a pen
and when every problem looks like a page
I commit ink to paper
the worth of the words that come out
determines my wage
I've been making enough
to pay her the compliment
of not quitting
of not sitting
when standing is required
she only asks that I put the effort in
and in return she's willing
to pin a paper heart to her chest
then do her best impression
of a target

Sara tells me that effort
is the Siamese twin of success
so when everyone else looks like a wrong answer
she says she'll settle for being my best guess

so we lie in bed like a mess
that someone's been meaning to clean
for the large part
of a long while
we lie there like a pile of dirty laundry
and how we'll ever come clean
is beyond me
so we don't

she says
it's supposed to be dirty
if by the end you haven't hurt me
then you didn't try

so I do my best impression
of a surgeon
cutting purple hearts out of my own
use my veins like thread
then have hurt sewn to our skin like medals
because when the bleeding stops
and the dust settles
all we have are our wounds
to wear like decorations
upon our chest

Sara does her best impression of a war tells me not to count my pride among the casualties because maybe faith means never keeping score she says there's more to effort than just switching gears and in terms of what one should give in this life sweat holds more value than tears

you have to try
and even though
the failing use of my right hand
means I'll never land a knockout punch
in the first round
life is composed of sound and fury
whatever noise is left in me
will be twice as loud when I try
so I plug myself into the idea of going the distance
and I amplify
Sara has a throat like a vase
she sings her words into bloom
has a voice like perfume
It's been sticking to my clothes
so everyone knows where I've been sleeping

She's been keeping me so close
you could use my body for evidence
pull her fingerprints as proof
that she's been on top so often
she's beginning to look like my roof

but a real sexy roof and she doesn't leak

unless you count the crying

she does that sometimes
worries that she's just a back up plan
but I've lived long enough to learn
too many options can kill a man
I will make no exodus
I'll be around long enough
to watch uncertainty bid us farewell
then echo our names into the crater
caused by the impact
of when our lack of conviction fell

Sara,
you've never had to sell me on the idea
of absolute certainty in the trustworthiness of another
the first and only time you met my mother
mom said
"I like the way she looks at you"
and I echoed back to her
that I liked it too

eyes like recycle bin blue
she looks at broken things
as if she can make them new
more than a few times I've caught her staring
caught her wearing
a smile reserved for those busy making plans

Sara believes that distance is a fundamental that can be side-stepped by a piece of string and two tin cans

and I remember when my tin can rang
they said
there's no family to speak of
so love is next in line
and there's not a lot of time
she's asking for her boyfriend

in the cab to the hospital I feel my heart bend
as if bracing for impact
so I do my best impression of a man
and face the fact

it's supposed to hurt

a doctor does his best impression of the truth and spares me his attempts to skirt around the issue

they can't stop the bleeding

and the failing use of Sara's heart
isn't actually
the failing use of Sara's heart
It's just another way to tell the time
and she's ticking

my darling Sara
I was holding your hand when you died
and even though the failing use of my right hand
prevented me from feeling you leave

I tried.
```

---

## IC-1911: Neil Hilborn Collection

- Title: Neil Hilborn Collection
- Author (byline): Neil Hilborn
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 920
- Already set (do not supply): none

### Source block (context only)

```text
Author: Neil Hilborn
Book: Our Numbered Days
ISBN: 978-0989641562
Publisher: Button Poetry
Date (Month/Year): April 2015
Author: Neil Hilborn
Book: The Future
ISBN: 978-1943735310
Publisher: Button Poetry
Date (Month/Year): April 2018
Author: Neil Hilborn
Book: Our Numbered Days
ISBN: 978-0989641562
Publisher: Button Poetry
Date (Month/Year): April 2015
```

### Introduction (context only: never use it for content warnings)

```text
Neil Hilborn was diagnosed with Obsessive Compulsive Disorder (OCD) at the age of 11 and with Bipolar Disorder in college. Anxiety and depression have been a part of his life for years. Now he’s one of the most-watched spoken word poets in the world – and an accomplished author. And though his work, we find insight into the reality of what it’s like to live with mental illness. OCD, The Future and Joey by Neil Hilborn.
```

### Performance text (classify this)

```text
OCD

The first time I saw her...
Everything in my head went quiet.
All the tics just disappeared.
When you have Obsessive Compulsive Disorder, you don’t
really get quiet moments.
Did I lock the doors? Yes.
Did I wash my hands? Yes.
Did I lock the doors? Yes.
Did I wash my hands? Yes.

But when I saw her,
I knew I had to talk to her.
I asked her out six times in thirty seconds.
On our first date, I spent more time organizing my meal
by color than I did eating it...
But she loved it.
She loved that I had to kiss her goodbye sixteen times
or twenty-four times if it was Wednesday.
She loved that it took me forever to walk home because
there are lots of cracks on our sidewalk.
When we moved in together, she said she felt safe, like
no one would ever rob us because I definitely locked the
door eighteen times.
I’d always watch her mouth when she talked—
when she talked—
when she talked—
when she talked
when she talked;
when she said she loved me, her mouth would curl up at
the edges.
[THEN . . . ]

Some mornings I’d start kissing her goodbye but she’d just leave cause I was just making her late for work... When I stopped in front of a crack in the sidewalk, she just kept walking... When she said she loved me her mouth was a straight line. She told me that I was taking up too much of her time. Last week she started sleeping at her mother’s place. She told me that she shouldn’t have let me get so attached to her; that this whole thing was a mistake, but... How can it be a mistake that I don’t have to wash my hands after I touch her? Love is not a mistake, and it’s killing me that she can run away from this and I just can’t. I can’t – I can’t – I can’t –

The Future

The worst thing about being naked—and then
being hit by a car—is that road rash
is a problem for skin. Why was I naked
in the middle of the road at noon? I am glad
you asked, imaginary other half of this
conversation! I have no idea! Some characteristics
of bipolar disorder include dissociation, hallucinations,
and fugue states, so sometimes I wake up in places
I didn't go to sleep!
So. There I am. Nude. Splayed out on a car, and I'm
screaming about the government
conspiracy to take away my feet.
"This is not how I imagined my life would turn out."
When I was young, I broke
both my ankles jumping off a roof because
I was sure a cape would enable me to fly. My parents
attributed this to my strong imagination. Last year,
my therapist called it a delusion. I fail
to see the difference. Also, I really can fly and see the
future – 43% of the time.
They keep telling me seeing things that aren't
technically there
is called "disturbed cognitive functioning." I call it
"having a superpower."
Once, I pulled over on the 110 freeway
and jumped out of my old Jeep because I saw it burst
into flames twenty seconds before it actually burst
into flames. I know tomorrow is going to come
because I've seen it. Sunrise is going to come,
all you have to do is wake up. The future
looks like a child in a cape. The future looks just like
gravity: everyone is slowly drifting toward everyone
else.
I saw the future, I did,
and in it I was alive.

Joey
Joey always told me, laughing, as though it were actually
a joke
That he wanted to kill himself but it was never the right
time,
There were always groceries to be bought
And little brothers to be tucked in at night.
Don’t worry, Joey isn’t gonna kill himself 20 more
seconds into this poem,
It’s not that kind of story I’m telling here.

I once caught Joey in my dad’s office, Staring at the safe where he knew we kept the guns Once Joey molded his car into the shape of a tree trunk and refused to give a reason why I once caught Joey in biology class Staring at a scalpel like he wanted to be the frog Splayed out, wide open So honest

There is one difference between me and Joey:
When we got arrested, bail money was waiting for me at
the station
When I was hungry, I ate
When I wanted to open myself up and see if there really
were bees rattling around in there,
My parents got me a therapist.
I can pinpoint the session that brought me back to the
world,
That session cost seventy-five dollars.
Seventy-five dollars is two weeks of groceries
It’s a month of bus fare
It took weeks of seventy-five dollars to get to the one
that saved my life.
We both had parents that believed us when we said that
we weren’t okay
But mine could afford to do something about it
I wonder how many kids like Joey wanted to die,
And were unlucky enough to actually pull it off,
How many kids had people who cared about them but
also had to pay rent?
I’m so lucky that right now I’m not describing Joey’s
funeral
I’m so lucky we all lived through who we were
To become who we are
I’m so lucky-
I’m so
Lucky
```

---

## IC-1912: Neil Hilborn Collection 2

- Title: Neil Hilborn Collection 2
- Author (byline): Neil Hilborn
- Work: Our Numbered Days
- Publisher: Button Poetry
- Publication date as stated: April 2015
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1381
- Already set (do not supply): none

### Source block (context only)

```text
Author: Neil Hilborn
Book: Our Numbered Days
ISBN: 978-0989641562
Publisher: Button Poetry
Date (Month/Year): April 2015
```

### Introduction (context only: never use it for content warnings)

```text
Neil Hilborn – One of the greatest Slam poets of all time. But what makes Hilborn special is his ability to talk about his experiences and how the pain of dealing with mental illness – OCD and Bi-Polar Disorder -- have dramatically impacted his life. As someone without a mental illness, I can only try to understand what living with a mental illness is like. Hopefully these poems will help you to understand too.
```

### Performance text (classify this)

```text
Not Dead (Pg 14)

When I say I’m on my way I probably mean it, I probably want to die less than I say I do,

but who knows, the statistics are sporadic at best. I’ll say I love you when I actually love you.

We are in your mother’s house
and I guess I want to be here. There’s no
reason not to, I guess. I guess
I’d rather be tattooing a bunch of triangles
on myself or ordering a steak
at an Indian restaurant or setting

all my s*** on fire, but none of those
are currently reasonable options. If anyone
is gonna kill me, it should be me.
The nearest place you can buy a gun
is only twenty minutes away. I’m not going

to tell you how to live your life, but maybe you should listen to your feet when they tell you to run away. Maybe you should get out of here,

then get out some more. I feel like I’ve spent my whole life waiting for this moment and now this moment

is terrible. This moment doesn’t even have any fireworks. This moment falls asleep with its keys in its hand. It’s not your fault,

probably because you didn’t make me this way, stupid, no, I mean I’m stupid.

OCD (Pg 38)

The first time I saw her, everything in my head went quiet. All the tics, all the constantly refreshing images, just disappeared. When you have

Obsessive Compulsive Disorder, you don’t really get quiet moments. Even in bed I’m thinking

did I lock the door yes
did I wash my hands yes
did I lock the door yes.
did I wash my hands yes.

But when I saw her, the only thing I could think about was the hairpin curve of her lips or the eyelash on her chee

the eyelash on her cheek the eyelash on her cheek

I knew I had to talk to her.
I asked her out six times.
In thirty seconds. She said yes
after the third one, but none of them
felt right, so I had to keep going.

On our first date, I spent more time organizing my meal by color than I did eating or talking to her

but she loved it. She loved
that I had to kiss her goodbye
sixteen times or twenty-four times
if it was Wednesday. She loved that
it took me forever to walk home
because there are lots of cracks
in our sidewalk.

When we moved in together,
she said she felt safe, like no one would ever rob us
because I definitely lock the door
18 times. I’d always watch her mouth

when she talked when she talked when
she talked when she talked. When she said
she loved me, her mouth would curl up
at the edges. At night, she’d lay in bed
and watch me turn all the lights off and on

and off and on and off and on and off
and on and off. She’d close her eyes
and imagine that the days and nights
were passing in front of her.

Some mornings, I’d start kissing her goodbye but she’s just leave because I was making her late for work.

When I stopped in front of a crack in the sidewalk, she just kept walking. When she said she loved me, her mouth was a straight line. She told me I was taking up too much of her time. Last week she started sleeping at her mother’s place.

She told me that she shouldn’t
have let me get so attached to her;
that this whole thing was a mistake,
but how can it be a mistake

that I don’t have to wash my hands
after I touch her? Love is not a mistake.
It’s killing me that she can run away
from this and I just can’t. I can’t

go out and find someone new because I always think of her.

Usually, when I obsess over things, I see germs sneaking into my skin. I see myself crushed by an endless succession of cars. She was the first

beautiful thing I ever got stuck on. I want to wake up every morning thinking about the way she

holds her steering wheel. How she turns shower knobs like she opening a safe. How she blows out candles blows out

candles blows out candles--
blows out candles blows out
candles blows out candles
blows out --

now I just think about who else is kissing her. I can’t breathe because he only kisses her once. He doesn’t care if it’s perfect. I want her back so bad,

I leave the door unlocked. I leave the lights on.

TRANSITION Hilborn himself has explained in interviews that even though people have viewed the previous poem as a “love conquers all” poem. In reality he felt he saw her as a talisman to fix his mental illness. The relationship ended and he’s back to feeling exactly how he did before. In his own words: “Somebody else isn’t going to fix your mental health. The only, the only person that is going to fix whatever is going on in your head, is you.” This next poem, Here and Away is Hilborn’s attempt to understand himself.

Here and Away (Pg 53)

I’ve been hearing that the world is ending.
I’ve heard it so much these days
that I can either completely ignore it
or never leave my house again.
That is, if I actually left my house
for things that don’t directly enable
me to keep my house. See, I’ve been thinking
about driving nowhere. I’ve been thinking
about becoming a box inside a locked room
inside a dark house at the dark end of the street.
I wanna go away until I’m gone. It takes so much
less energy to not exist than it does to exist
and get burned. I’ve been burned so much
I’m not me anymore. I’m a stupid puppet version
of me. I’ve got strings that lead to nowhere.
Nothing is pulling on me. I wish someone
would drag my hand out of hiding
and sign my name on the dotted line.
There are days when I cannot find the sun
even though it’s right outside my goddamn
window, when getting out of bed feels like the key
in the doomsday machine, so on those days,
this is what I tell myself: whatever
you are feeling right now, there is
a mathematical certainty that someone
is feeling the exact thing. This is not
to say you aren’t special. This is to say
thank god you aren’t special. I too
have kissed no one good night.
I have launched myself off tall places
and hoped no one would catch me.
I have ended relationships because suddenly
I was exposed. But isolation is not safety,
it is death. If no one knows you’re alive
you aren’t. If a tree falls in the forest
and no one’s around to hear it, it does
make a sound, but then that sound is gone.
I’m not saying you will find the meaning of life
in other people. Am saying that other people
are the life to which you provide the meaning.
See, we are wrong when we say I think,
therefore I am. The more we say it,
the more it sounds like, “I think,
therefore I wall be.” You cannot think yourself
into a full table. You cannot think and make
walls and a roof appear around you.
I have thought and thought myself into corners
made words, nightmares, and what
has it gotten me but more thoughts,
a currency that only buys more currency.
So please, if you want to continue existing,
do something. . Learn to make clouds with only
your breath. Build a house, even if every wall
leans to the left. Love it anyway, just like a season.

just like a child. Love how you hate yourself sometimes,
because goddamn, at least there’s still something
to hate. It’s so easy to think and keep thinking
until you are the last person left on earth.
until the entire world is no larger than the space
between your bed and the light switch,
but I hear the world is ending soon.
when we go, and we’re all going to go,
I will be part of it.
```

---

## IC-1913: New Heaven and Earth

- Title: New Heaven and Earth
- Author (byline): D.H. Lawrence
- Work: Look! We Have Come Through
- Publisher: BiblioBazaar
- Publication date as stated: 2009
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1286
- Already set (do not supply): none

### Source block (context only)

```text
Author: D.H. Lawrence
Book: Look! We Have Come Through
ISBN: 978-1110503445
Publisher: BiblioBazaar
Date (Month/Year): 2009
```

### Introduction (context only: never use it for content warnings)

```text
D.H. Lawrence, novelist, short-story writer, poet and essayist, was born in Eastwood, Nottinghamshire, England, in 1885. Though better known as a novelist, Lawrence's first-published works were poems. He believed in writing poetry that was stark, immediate and true to the mysterious inner force which motivated it. Many of his best-loved poems are bitterly satiric and express his outrage at the Puritanism and hypocrisy of conventional Anglo-Saxon society. Lawrence was a rebellious writer with radical views, who regarded sex, the primitive subconscious, and nature as cures to what he considered the evils of modern industrialized society. In this poem New Heaven and Earth we are introduced to D.H. Lawrence’s vision of Utopia.
```

### Performance text (classify this)

```text
I AND so I cross into another world shyly and in homage linger for an invitation from this unknown that I would trespass on. I am very glad, and all alone in the world, all alone, and very glad, in a new world where I am disembarked at last.

I could cry with joy, because I am in the new world, just ventured in. I could cry with joy, and quite freely, there is nobody to know. And whosoever the unknown people of this unknown world may be they will never understand my weeping for joy to be adventuring among them because it will still be a gesture of the old world I am making which they will not understand, because it is quite, quite foreign to them.

II
I WAS so weary of the world
I was so sick of it
everything was tainted with myself,
skies, trees, flowers, birds, water,
people, houses, streets, vehicles, machines,
nations, armies, war, peace-talking,
work, recreation, governing, anarchy,
it was all tainted with myself, I knew it all to start with
because it was all myself.
When I gathered flowers, I knew it was myself plucking
my own flowering.
When I went in a train, I knew it was myself travelling
by my own invention.
When I heard the cannon of the war, I listened with my
own ears to my own destruction.
When I saw the torn dead, I knew it was my own torn
dead body.
It was all me, I had done it all in my own flesh.

III
I SHALL never forget the maniacal horror of it all in
the end
when everything was me, I knew it all already, I
anticipated it all in my soul
because I was the author and the result
I was the God and the creation at once;
creator, I looked at my creation;
created, I looked at myself, the creator:
it was a maniacal horror in the end.
I was a lover, I kissed the woman I loved,
and God of horror, I was kissing also myself.
I was a father and a begetter of children,
and oh, oh horror, I was begetting and conceiving in my
own body.

IV AT last came death, sufficiency of death, and that at last relieved me, I died. I buried my beloved; it was good, I buried myself and was gone. War came, and every hand raised to murder; very good, very good, every hand raised to murder! Very good, very good, I am a murderer! It is good, I can murder and murder, and see them fall the mutilated, horror-struck youths, a multitude one on another, and then in clusters together smashed, all oozing with blood, and burned in heaps going up in a foetid smoke to get rid of them the murdered bodies of youths and men in heaps and heaps and heaps and horrible reeking heaps till it is almost enough, till I am reduced perhaps; thousands and thousands of gaping, hideous foul dead that are youths and men and me being burned with oil, and consumed in corrupt thick smoke, that rolls and taints and blackens the sky, till at last it is dark, dark as night, or death, or hell and I am dead, and trodden to nought in the smoke-sodden tomb; dead and trodden to nought in the sour black earth of the tomb; dead and trodden to nought, trodden to nought.

V
GOD, but it is good to have died and been trodden out
trodden to nought in sour, dead earth
quite to nought
absolutely to nothing
nothing
nothing
nothing.
For when it is quite, quite nothing, then it is everything.
When I am trodden quite out, quite, quite out
every vestige gone, then I am here
risen, and setting my foot on another world
risen, accomplishing a resurrection
risen, not born again, but risen, body the same as
before,
new beyond knowledge of newness, alive beyond life
proud beyond inkling or furthest conception of pride
living where life was never yet dreamed of, nor hinted at
here, in the other world, still terrestrial
myself, the same as before, yet unaccountably new.

VI
I, IN the sour black tomb, trodden to absolute death
I put out my hand in the night, one night, and my hand
touched that which was verily not me
verily it was not me.
Where I had been was a sudden blaze
a sudden flaring blaze!
So I put my hand out further, a little further
and I felt that which was not I,
it verily was not I
it was the unknown.
Ha, I was a blaze leaping up!
I was a tiger bursting into sunlight.
I was greedy, I was mad for the unknown.
I, new-risen, resurrected, starved from the tomb
starved from a life of devouring always myself
now here was I, new-awakened, with my hand stretching
out
and touching the unknown, the real unknown, the
unknown unknown.
My God, but I can only say
I touch, I feel the unknown!
I am the first comer!
Cortes, Pisarro, Columbus, Cabot, they are nothing,
nothing!
I am the first comer!

I am the discoverer!
I have found the other world!
The unknown, the unknown!
I am thrown upon the shore.
I am covering myself with the sand.
I am filling my mouth with the earth.
I am burrowing my body into the soil.
The unknown, the new world!

VII IT was the flank of my wife I touched with my hand, I clutched with my hand rising, new-awakened from the tomb! It was the flank of my wife whom I married years ago at whose side I have lain for over a thousand nights and all that previous while, she was I, she was I; I touched her, it was I who touched and I who was touched. Yet rising from the tomb, from the black oblivion stretching out my hand, my hand flung like a drowned man's hand on a rock, I touched her flank and knew I was carried by the current in death over to the new world, and was climbing out on the shore, risen, not to the old world, the old, changeless I, the old life, wakened not to the old knowledge but to a new earth, a new I, a new knowledge, a new world of time. Ah no, I cannot tell you what it is, the new world I cannot tell you the mad, astounded rapture of its discovery. I shall be mad with delight before I have done, and whosoever comes after will find me in the new world a madman in rapture.

VIII
GREEN streams that flow from the innermost continent
of the new world,
what are they?

Green and illumined and travelling for ever
dissolved with the mystery of the innermost heart of
the continent
mystery beyond knowledge or endurance, so sumptuous
out of the well-heads of the new world.--
The other, she too has strange green eyes!
White sands and fruits unknown and perfumes that
never
can blow across the dark seas to our usual world!
And land that beats with a pulse!
And valleys that draw close in love!
And strange ways where I fall into oblivion of uttermost
living!--
Also she who is the other has strange-mounded
breasts and strange sheer slopes, and white levels.
Sightless and strong oblivion in utter life takes
possession of me!
The unknown, strong current of life supreme
drowns me and sweeps me away and holds me down
to the sources of mystery, in the depths,
extinguishes there my risen resurrected life
and kindles it further at the core of utter mystery.
```

---

## IC-1914: The No Hug Rule

- Title: The No Hug Rule
- Author (byline): Cheryl Costello-Forshey
- Work: Chicken Soup for the College Soul
- Publisher: Health Communications
- Publication date as stated: Sept 1999
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 833
- Already set (do not supply): none

### Source block (context only)

```text
Author: Costello-Forshey, Cheryl
Book: Chicken Soup for the College Soul
ISBN: 978-1558747029
Publisher: Health Communications
Date(Month/Year): Sept 1999
```

### Introduction (context only: never use it for content warnings)

```text
Women everywhere seem to say the same thing about their male partners and it goes like this: ‘He just shuts off to emotion! He never tells me how he is feeling!' Or ‘He’ll leave the room and refuse to talk about it!' There is an unspoken rule that we boys learn very early . . . . Don’t cry, don’t hug . . . . be a man! It’s been said however (and this applies to men and women) that you need four hugs a day for survival, eight for maintenance, and twelve for growth. This poem by Cheryl Costello-Forshey traces the development of “The No Hug Rule,” and the ability of one young man to overcome society’s implied expectations.
```

### Performance text (classify this)

```text
The first day of kindergarten
He hurried to the door
Shrugging off his mother's hugs
He didn't need them anymore
For he was all grown up now
Too big for all that stuff
Instead he waved a quick good-bye
Hoping that would be enough
When he came home from school that day
She asked what he had done
He handed her a paper
With a big round yellow sun
A picture quite imperfect
For he'd messed up here and there
But she didn't seem to notice
Or she didn't seem to care

The first day of junior high
He hurried to the door
Running from his mother's hugs
He didn't want them anymore
He ignored her calling out to him
As he hurried down the street
Near the intersection
Where his friends had planned to meet
He hoped that she would understand
Why he had to walk to school
Riding with his mother
Just wouldn't have been cool

And when he came home from school She asked what he had done He handed her some papers With Xs marked on more than one The teacher clearly pointing out The wrong answers here and there But his mother didn't seem to notice Or she didn't seem to care

The first day of senior high
He hurried out the door
Jumped into the driver's seat
Of his jacked-up shiny Ford
He left without his breakfast
He left without a word
But he turned and looked back
Before pulling from the curb
He saw her waving frantically
As he drove away
He tapped his horn just once
To brighten up her day
He saw a smile cross her face
And then he drove from sight
Onward to a different world
A new exciting life

And at his graduation
As tears shone in her eyes
He knew the time had come
To bid his mom good-bye
For he was off to college
Off to better days
No more rules to abide
Alone to find his way

Suitcases filled the trunk
Of his dirty beat-up Ford
He couldn't wait to get to school
To check out his room and dorm
She opened up his car door
Closed it when he got in
Then smiled proudly at her son
As tears dropped from her chin
She reached through the open window
Wished him luck in school
And then she pulled him close to her
And broke the "no hug" rule
He felt the freedom greet him
As he pulled out on the interstate
At last his life was his alone
He anticipated fate

College life was more challenging
Than he ever could have hoped
There was no time to respond to letters
His mother often wrote
He was a grown adult now
Too old for all that stuff
His visits during holidays
Would have to be enough
Besides, midterms were quickly coming
The pressure was immense
He studied late into the night
His need to pass intense
He wondered how he'd manage
How he'd ever cope
What if he failed his tests?
Would there be no hope?

As if he had a calling
He headed down the interstate
Driving at full speed
The hour getting late
He pulled up the curb
Where once he used to roam
And went through the open door
Of his mother's home
She was sitting at the table
With a drawing in a frame
Memories from the past
That brought both joy and pain
She didn't need to ask
Why he was home from school
Because she knew the answer
When he broke the "no hug" rule
HIs arms around her tightly
Peering at the drawing he had done
Lots of trees, imperfect branches
And a big round yellow sun
She smiled a knowing smile
And then she spoke aloud
"Son you always did
And you always will make me very proud
For look how far you've traveled
From that little boy so brave
Heading off to kindergarten
Your hand up in a wave
And through the years you've made mistakes
But son I've made them, too
Being perfect is not an option in life
Simply do the best you can do
And don't expect more than that
For life is supposed to be fun
You've only got one to live
Do what is best for you son"

Sitting in his dorm room
When the pressure seems too much
And all that he is striving for
Seems completely out of touch
He peers at the drawing
Of a big round yellow sun
And then he is reminded
Of just how far he's come
From childhood to manhood
Fighting back many a fear
Through trials and tribulations
Holding back many a tear
Knowing that being successful
Isn't passing every test
And the only way to falter in life
Is by failing to do his best
And the biggest lesson he's learned
One he did not learn in school...

That it's okay, for even a man To break the "no hug" rule
```

---

## IC-1915: Open Letter to Neil Armstrong

- Title: Open Letter to Neil Armstrong
- Author (byline): Mike McGee
- Work: Spoken Word Revolution Redux
- Publisher: Sourcebooks, Inc.
- Publication date as stated: April 2007
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 762
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mike McGee
Book: Spoken Word Revolution Redux
ISBN: 978-1402208690
Publisher: Sourcebooks, Inc.
Date (Month/Year): April 2007
```

### Introduction (context only: never use it for content warnings)

```text
As the ruler of the tides, it is fitting that the Moon should be the ruler of our emotions. Yes, our emotions have long been portrayed in terms of the sea: fluid, momentous, churning from within. How we feel about things and how our feelings affect others are all influenced by the Moon. Whereas the Sun gives us our spirit, it's the Moon that gives us our soul. In this selection, “Open Letter to Neil Armstrong,” Mike McGee explores the concept of love through a letter to the first man to walk on the Moon and concludes that there is no experience more fulfilling (not even traveling to the moon) than to experience the emotion of love. Open Letter to Neil Armstrong by Mike McGee
```

### Performance text (classify this)

```text
Dear Neil Armstrong,
I write this to you as she sleeps down the hall
I need answers that I think only you might have
When you were a boy
When space was simple -- science fiction and
flying was merely a daydream between periods of
history and physics
When gifts of moon dust to the one you loved
Could only be bought and wrapped in your imagination
Before the world knew your name
What was the moon like from your back porch?
Before it was a destination
Your arm; strong, warm and wrapped under her hair
across her shoulders
Both of you gazing up from the back porch
Summers before your distant journey
I don’t want to hear about the mission
I want to know if you wrote her name in the dirt,
if you surrounded both of your initials with a heart
for alien life to study a million years from now
Does she know how much you missed her while you were
gone?
Could you feel how much she missed you
while you were away, farther than any man had ever
been?
What is it like to love something so distant?
What was it like to fall from the sky?

What words did you use to bring the moon back to her?
And what did you whisper in the moon’s ear about the
girl back home?
Did you promise to bring her back next time?
When the Earth rose over the Sea of Tranquility, did
you look for her?
What was it like to look at our planet and know that
everything you could be,
All you could ever love and long for was still there, just
floating before you?
Every July I think of you
I imagine the summer of 1969
And the feelings you must’ve had, doing what you did
How lonely she must’ve felt while you were gone
You never went back to the moon and I believe that’s
because it doesn’t take rockets to get you where you
belong
The flight home always means more
I see that in this woman down the hall
And sometimes she seems so much further than across
the room
But I’m ready for whatever walk I must make to get to
her
I’ve been to many places in my life
The moon looks the same no matter what sky I am under
I thank you for being so adventurous, but
That rock you landed on has got nothing
on the rock she’s landed on [point to chest]
You walked around, took samples and left
She’s built a fire, cleaned up the place and I hope she
decides to stay
Mr. Armstrong, I don’t have much
Many times have I been upside-downtrodden
But with these empty hands
Comes a heart that is full more often than the moon
She’s becoming my world
sending me spinning out of orbit and
I now know that I may never find life outside of hers
So maybe I should just stay
I ask you all of this not because I doubt your feet/feat
And certainly not out of any disrespect
I just want to know what it’s like to go somewhere no
man had ever been
Just to find that she wasn’t there
To realize your moonwalk could never compare to the
steps that lead to her
I wanna give her everything I don’t have yet
It would be nice to wrap her neck with a priceless
moonstone set in gold chain
But I can’t imagine such gift would mean anymore than
her knowing
I will never long to be so far away from her
That I could collect that unearthly jewel
In conclusion, yes, I would go to the moon and back
But not without her
we’d claim the moon for each other with flags made
from sheets down the hall
And I’d risk it all to kiss her under the light of Earth
The brightness of home
but I can do all of that and more
Right here, wherever she is, and when I have my arm
around her,
gazing up, on the back porch
I will not promise her gifts of moon dust or flights of
fancy
Instead, I will gladly give her all the Earth she wants
In return for the sound of her heartbeat and laughter
And the time it takes to fall from the sky down the hall
and
right into love
I’d do it every day
If I could land next to her
She is one small step for a man
one giant leap for my kind
```

---

## IC-1916: Poem for Jen

- Title: Poem for Jen
- Author (byline): Big Poppa E (Eirik Ott)
- Work: Big Poppa E’s Greatest Hits
- Publisher: Lulu.com
- Publication date as stated: Oct 2000
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 710
- Already set (do not supply): none

### Source block (context only)

```text
Author: Big Poppa E. (Eirik Ott)
Book: Big Poppa E’s Greatest Hits
ISBN: 978-0615149486
Publisher: Lulu.com
Date (Month/Year): Oct 2000
```

### Introduction (context only: never use it for content warnings)

```text
The loss of a loved one is life’s most stressful event and can cause a major emotional crisis. After the death of someone you love, you experience bereavement, which literally means “to be deprived by death.” Often, death is a subject that is avoided, ignored or denied. At first it may seem helpful to separate yourself from the pain, but you cannot avoid grieving forever. Someday those feelings will need to be resolved or they may cause physical or emotional illness. Eirik Ott approached the one year anniversary of Jen O’Hare’s death trying desperately to cope with her death. In an attempt to resolve his pain, he wrote and now performs nationwide this Poem for Jen by Big Poppa E. aka Eirik Ott.
```

### Performance text (classify this)

```text
There’s a hole in my heart
in the shape of her smile
that will never be filled
I will never forget
the last sentence
of the article in the newspaper
the next day:
“The terrible crash pancaked the tiny Honda Civic.”
It rattled our minds
as we ran our fingers
across the gouges
in the pavement,
our eyes squinting
through a thousand glaring pinpricks
from windshield fragments,
searching
for lucky pennies
scattered
(hundreds of them)
from her broken penny jar.

“The terrible crash pancaked the tiny Honda Civic.”
That sentence robbed us of closure.
We weren’t allowed to marvel
at the mortician’s handiwork
(she looks like she’s asleep).
We couldn’t cup
her lifeless hand —
powdered
and colored
with an artist’s touch —
and confirm
that it was true
that it actually really
had happened.
No, the terrible crash pancaked the tiny Honda Civic,
and they wouldn’t even run photos because it’s a family
newspaper and you can’t run photos like that in a family
newspaper.
We had to just agree
nod our heads in unison
and agree that she was gone
and would never be back
this precious flower
plucked in mid-blossom.
And we held each other
and remembered her
as we had last seen her
pink and alive and smiling
that big thumbs up smile
And we were warmed by the knowledge
that if anyone could’ve changed the world
she could’ve.
She would’ve
had she only been given the chance.
But now...
We’ll always feel like she’s out there somewhere
always at the corner of our eyes
in the summer sea of spaghetti straps and backpacks
tan lines and smiles
she’ll be there at the corner of our eyes
and we’ll catch our breath
turn and see nothing.
I think about that last sentence every time I drive, it
echoes in my brain as I near the spot on the four-lane
highway where she crossed the median and died.
I picture the time of day: around 11 a.m.
The sun was out. The sky was blue. There was no rain.
She was driving alone. She was probably smoking.
She was listening to James Taylor’s Greatest Hits;
we know this because the tow crew
pried that CD from what was left of her stereo.
And I grip my wheel white-knuckled
as I near the spot.
And I can’t help counting down
the time she had left.
(and she didn’t even know it was coming.)
It was a bright sunny day and she was singing...
“I’ve seen fire and I’ve seen rain” 20 seconds
“I’ve seen sunny days that I thought would have no end”
10 seconds
“I’ve seen lonely times when I could not find a friend” 5
seconds
“But I always thought I’d see you baby one more time
again...”

And JUST LIKE THAT we are past it and the scars in the pavement are left behind. And JUST LIKE THAT we are past it and the white cross we left in the grass on the embankment is left behind.

And JUST LIKE THAT we are past it and the lucky pennies and the photos and the little good luck tokens and the letters and the constellations of shattered windshield are left behind. just like that she was left behind. The headline should not have read “Chico State Student Killed in Car Crash.” No, the headline should’ve shouted in capitol letters across the front page:

JENNIFER LYNN OʼHARE KICKED SO MUCH ASS!

She was a poetess, a priestess, a goddess, a feminist, a fighter, a lover, a laugher, a teller of truths, a spinner of midnight balcony tales shrouded in Heinekin and Camels... (she could break down Brian Johnson’s male chauvinist arguments with the precision of a surgeon, hurling words like “patriarchal” and “misogyny” and “hegemony” in a rapid fire distillation of everything she had learned in Women’s Studies classes, we almost felt sorry for Brian as she leaned towards him on the edge of her stool pointing with the glowing cherry of a lit cigarette...) She was a God-awful drummer but a very enthusiastic drummer, a deep and passionate kisser, a liver of life, a lover of all things, not the best of students but the best of teachers, a mentor, a sister, a daughter, a confidant, a friend. These words should have been displayed on the pages of every newspaper in the world. But they weren’t. Most people in this world probably didn’t even realize their loss. And I feel sorriest of all for those people -- you -- those of you who never had the chance to meet her. She was that cool. The last sentence in this poem is how I will remember Jennifer Lynn O’Hare: This world is a better place
```

---

## IC-1917: Poems from Guantanamo Bay

- Title: Poems from Guantanamo Bay
- Author (byline): Not specified
- Work: Poems from Guantanamo: the Detainees Speak
- Publisher: University of Iowa Press
- Publication date as stated: 2007
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1088
- Already set (do not supply): none

### Source block (context only)

```text
Author: Edited by Mark Falkoff
Book: Poems from Guantanamo: the Detainees Speak
ISBN: 978-1587296062
Publisher: University of Iowa Press
Date (Month/Year): 2007
```

### Introduction (context only: never use it for content warnings)

```text
One of the most laudable tenets of American law is the assurance that anyone accused of a crime is “innocent until proven guilty.” However, this fundamental legal right seems to have taken a reverse path in the post 9/11 world, especially when it comes to Muslims. These racially targeted individuals are more often “guilty until proven innocent,” and this is a rather disturbing vein in the realm of American democracy and international human rights. Since 2002, at least 775 men have been held in the U.S. detention center at Guantanamo Bay, Cuba. According to Department of Defense data, fewer than half of them are accused of committing any hostile act against the United States or its allies. In hundreds of cases, even the circumstances of their initial detainment are questionable. Despite President Obama’s promise two years ago to shut down the Guantánamo Bay detention center, as of August 2011 it remains open. This collection gives voice to the men held at Guantanamo. If, in the words of Audre Lorde, poetry “forms the quality of light within which we predicate our hopes and dreams toward survival and change,” these verses—some originally written in toothpaste, others scratched onto foam drinking cups with pebbles and furtively handed to attorneys—are the most basic form of the art.

Today I offer you art in the form of Poems from Guantanamo Bay: The Detainees Speak. The collection includes They Fight for Peace by Shaker Abdurraheem Aamer, a British citizen; Humiliated In The Shackles by Sami al Hajj, a Sudanese journalist; Terrorist 2003 by Martin Mubanga, an athletic kick-boxer and First Poem of My Life by Mohammed El-Gharani, a 14-year old detainee.

Poems are interspersed and are color-coded to assist in the dramatic portrayal of each “character”
```

### Performance text (classify this)

```text
Edited By Mark Falkoff

Peace they say.
Peace of mind?
Peace of earth?
Peace of what kind?
I see them talking arguing, fighting –
What kind of peace are they looking for?
Why do they kill? What are they planning?
Is it just talk? Why do they argue?
Is it so simple to kill? Is this their plan?
Yes, of course!
They talk, they argue, they kill –
They fight for peace.

• They Fight for Peace by Shaker Abdurraheem

Aamer

• Humiliated In The Shackles by Sami al Hajj

• Terrorist 2003 by Martin Mubanga

• First Poem of My Life by Mohammed El-

Gharani

Hustle cautiously in the land of those who speak no
Arabic!
Even if they gave you oaths bound by oaths.
Their aim is to worship petty cash
And for it they break all vows.
I came to their land to pursue an education,
And saw such malice among them.
They surrounded the mosque, weapons drawn,
As if they were in a field of`war.
They said to us, "Come out peacefully,
And don't utter a single word."
Into a transport truck they lifted us,
And in shackles of injustice they bound us.

For sixteen hours we walked; For the entire time we remained in shackles.

Humiliated in the Shackels . . .
When I heard pigeons cooing in the trees,
Hot tears covered my face.
When the lark chirped, my thoughts composed
A message for my son.
Mohammad, I am afflicted.
In my despair, I have no one but Allah for comfort.
The oppressors are playing with me,
As they move freely around the world.
They ask me to spy on my countrymen,
Claiming it would be a good deed.
They offer me money and land,
And freedom to go where I please.
Their temptations seize
My attention like lightning in the sky.
But their gift is an empty snake,
Carrying hypocrisy in its mouth like venom,
America sucks, America chills,
While d’ blood of d’ Musllims is forever getting spilled,
In d’ streets of Nablus, in d’ streets of Jenin,
Yeahhhhhh! You know what I mean.

American Gangstas, American lies In downtown LA, they was burning rubber tyres. After Rodney King they woz burning ‘nough fires. Yeahhhhhh! Them mother sumthing liars.

American justice, American pigs,
American soldiers, American wigs.
Yes I’m feeling angry, yes I’m feeling pissed,
An’ it’s about time that the JIF got dissed.

JIF – Joint Interrogation Facility at Guantanamo

Now them ask me, what will ya do if ya leave the prison?
Will ya be able to slip back into d’ system?
What ya gonna do with ya new-found fame?
An’ will ya ever, ever go jihad again?

All of us wanted to move our bowels But they insisted on denying us.

The soldier struck with his boot; He said we were all equally subjects.

In the prison's darkness they spread us out In the cold's bitterness we sat......

When the red-faced infidels came to spend their money,

Never had I seen such tribulation.

In a warplane they brought us up,

And after a half hour, brought us down.

We saw such insults from them;

Not even the book of God was protected.

Along with their malice, they were foolish.

Tribulations, then hitting and imbecility.

For they are a people without reasonable minds,

Due to their supply of alcoholic drinks.

They have monuments to liberty
And freedom of opinion, which is well and good.
But I explained to them that
Architecture is not justice.
America, you ride on the backs of orphans,
And terrorize them daily.
Bush, beware.
The world recognizes an arrogant liar.
To Allah I direct my grievance and my tears.
I am homesick and oppressed.

An’ them er says to me, if ya’s walking down d’ street, Sees a fine girl will ya sweep her off her feet? Or leave her standing thinking that she sweet, For the next mans to come and reap?

An’ them er says to me, no you’s back from d’ core, You’re a terrorist, a big-time hardcore. But my friends them know the score, Cause back in d’ day me use to g’waan juss like a whore. Now me a Muslim, so me whan . . . . . shut that door.

But the government’s them, them a feeling sore! Cause like a page in a book you know me done a tore A hole in them heart, them exposing hypocrisy, For all the world them to clearly come ‘n see.

Now them ask me, will ya come work for us?
Had to hold my breath so they would not hear me cuss,
Dumb mother sumthings, I’d rather suck pus,
Than work for the mans that Allah did a cuss.

Mohammad, do not forget me.
Support the cause of your father, a God-fearing man.
I was humiliated in the shackles.
How can I now compose verses? How can I now write?

After the shackles and the nights and the suffering and
the tears,
How can I write poetry?
My soul is like a roiling sea, stirred by anguish,
Violent with passion.
I am a captive, but the crimes are my captors’.
I am overwhelmed with apprehension.
Lord, unite me with my son Mohammad.
Lord, grant success to the righteous.

The “Red Cross” arrived, in our state of need

On the condition that we raise the card with a cross.

“If you want dignity and protection,

Then raise the cross for protection.”

All of us threw the card away,

Intent that our spirits be redeemed.

They carried us, afterwards, to Cuba,

Because it is an afflicted isle.

Out of spite, they showed such impudence.

Their war is against Islam and justice.

An’ them a says to me, we can make your life sweet,
Give you all the things you ever wanted to eat.
All you got to do is practice deceit,
An’ everything a go be really neat.

“Sauf ofaker fi haza. Let me think about about it.” Qurrratu Qur’an. There was no need to doubt it, Did you think for a second I really did doubt it? There wasn’t even need for me to go shout it.

They’re scum, they’re criminals, on their way to hell, And not for all of the dunya would I join them as well!

Now me’s coming with these lyrics from Guantanamo B,
In my prison cell down by the sea,
For hard-core detainees like you an’ me.
Terrorist 2003,
So called. Yeah, that’s me!

Qurrratu Qur’an – Arabic for I read the Qur’an

dunya – Arabic for wordly, material things as

opposed to spiritual matters
```

---

## IC-1918: Puddin’ and Soul Food: A Duel with Death at Lunchtime

- Title: Puddin’ and Soul Food: A Duel with Death at Lunchtime
- Author (byline): Mike McGee
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1242
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mike McGee
Book: In Search of Midnight: The Mike McGee
Handbook of Awesome
ISBN: 978-0982148822
Publisher: Write Bloody Publishing
Date (Month/Year): June 2009
Author: Mike McGee
Book: Solomon Sparrows Electric Whale Revival
ISBN: 978-0978998998
Publisher: Write Bloody Publishing
Date (Month/Year): Sept 2007
```

### Introduction (context only: never use it for content warnings)

```text
This is a love poem, but not to any specific person. Oh, no . . . this is a love poem to specific substance. One that we’re all familiar with. Ladies and Gentleman, that substance is Pudding. I’m concerned for your safety. For those of you who are already experiencing pangs of hunger, I urge you to leave the room. For those of you who wish to stay, please . . . . Picture a buffet unlike any other where beautiful people of your dreams have gathered to feed you the silky delicacy known as Puddin’ by Mike McGee
```

### Performance text (classify this)

```text
Puddin’
Imagine that they
are also enveloped by ecstasy,
so into the feast they keep referring to the substance
as
Puddin’.
So drawn to it
they forget the letter “G”

I would like to take moment to speak directly to that in which this poem was written.

Hello, Pudding.
Oh how I miss you, baby.
How I long to be near your bowl
with a very tiny spoon,
so that I can take my time
and enjoy you.
To caress your shapeless existence.
To watch you do that gelatinous jiggle you do so well just
before I consume you with all the passion I learned from
Bill Cosby himself.
Goddamn you, Pudding.
How dare you disguise yourself.
Who will you be tonight, my sweet?
Hmm?
Maybe a bowl of tapioca,
a taste of butterscotch,
or will you be more complex,
donning a vanilla chocolate ripple,
hiding away in my freezer,
hugging a stick
and only succumbing to the name pudding pop.

Ohhhhh, Pudding.
Temptation is for the weak,
so please call me Weakly Weakerson when I am near you.
Me and my band the Week Tones
will play you songs of desire and merriment
and if that doesn’t work for you, my dear, sweet Pudding.
I can always put on my Marlo Brando costume.
The one that seems to turn you on the most.
The one that gets you all thick and creamy.
Ohhhh, Pudding.
The Horror, The Horror.

I could just drink you from a straw out in my front yard,
naked
in an inflatable kiddie pool
full of you.

The envy and confusion of all those walking by would make it well worth the effort.

We now interrupt this poem to bring you viable content in an attempt to make this poem more accessible to a broader audience.

Peace in the Middle East
Allah at a play
Word for a Nerd
My Father Never Loved Me
I Wanna Make a Difference
I suck
You Suck
Bush Sucks

Now back to the poem already in progress . . .

I could cover myself with you and go as you to a
masquerade ball.
People will want to lick you off of me,
but I’ll say
Noooooooo
I will lick me.
For a I have a tongue
and a book on Yoga.
Nooks and crannies.

However, our love is limited, for I’ve discovered that my colon cannot possibly tolerate our passion much longer. You are composed with the blood of milk and I shall rather die than make you with water.

So let us call for one last night of nasty.
Let me sing your praises.
For now I shall summon the spirit of Bill Cosby and say
to you this:
Zippa Zang
Chaz a Piece of damn
saz a faz,
Wednesday’s hump day,
Kodak Moment,
Ha!

TRANSITION Let’s face it, food can inspire intense emotions. Some people eat when they are happy, or sad, or anxious. In fact, we have such an emotional connection to food that obesity is an overwhelming concern for a growing (ha ha) number of Americans today. And everyone has a favorite food. You know, the one that you hide from the rest of your family so that you don’t have to share. Or the one that, hands-down, you know you could win with if challenged to an eating contest. 87 cups of puddin’ in less than 3 mintues! Whoo Whoo. So how many do you think you could eat if the prize wasn’t a new car or a life-time supply of Rice-a-Roni? What if the prize was your ETERNAL SOUL? Soul Food: A Duel with Death at Lunchtime by Mike McGee.

Soul Food: A Duel with Death at Lunchtime

So last week the Angel of Death comes knocking at my door Totally interrupting Perfect Strangers And I’m like, “Dude, you are so early! There is so much more I wanted to do with my life!”

“You’ve had plenty of time for that!” “You know, you sound a bit like Sean Connery.” “No, he sounds a bit like me.” "Whatever, dude. There’s gotta be some sort of loop-hole. What if we competed for my soul? Like some sort of contest." “I love a good challenge. If we can both agree on one, then the winner may keep your soul.”

At this point I remembered I had a pot a ramen noodles waiting for me on the stove. The Angel of Death was lured into my kitchen by the sweet aromatic joy of powdered shrimp flavoring. I could see that Death was hungry, so I made a second pack of Ramen. We sat and ate in silence, but my hunger just wouldn’t subside. So while I raided the fridge, I noticed Death scoping my Rice Krispy Treats.

“Still hungry, dude?” “We’ll take one for the road.” he said. And we both put a Rice Krispy treat in our pockets. “Actually, I could probably eat half of all your food.” “So could I, dude, so could I.”

And it hit us both at the same time. We pulled out every bit of food in my house and divided it all into equal halves. We had one rule: First person to finish eating their half of food keeps my soul.

We sat down on the kitchen floor surrounded by an odd buffet. The world’s greatest food challenge began. But this was no ordinary match.

I took an early lead as Death fumbled opening a can of refried beans. I plowed through a dozen eggs and half a gallon of milk. I strategically swallowed spoonful after spoonful of leftover lasagna, without chewing. Death caught up to me with a tub of butter and half a soggy pumpkin pie. I hustled my way through cans of corn, green beans, kidney beans, chili, chicken soup, fruit cocktail, and a few cans of peas, but I was stopped dead in my tracks by a mystery can. It’s label missing and nowhere to be found. Damn, dog food! No time to think, I had to eat it.

Death was now ahead of me by two-cans of beer, a frozen steak and what we think may have been tamales. I burped to make room and continued on in the feast for my soul. I ate broccoli, cauliflower, cucumbers, oranges, bananas, a container of baking powder, two cups of salt & pepper, a jug of Pepto-Bismol and a can of whipped cream. We reached our last item of food. One. Raw. Potato. Each. We slowly gnawed our way through the raw potatoes, swallowing our last bites at the exact same time. It appeared as though we had a draw. Then Death looked to me with a sly grin and handed me a Tupperware bowl with my half of uneaten Jello. I grabbed a straw and sucked it down, saying:

“There’s always room for Jello!”

But Death just smiled and said, “I believe I finished my half before you. Your soul is mine.”

But I just outsmiled him and said, “What’s that in your pocket?”

His face sunk as he reached into his pocket and pulled out the last Rice Krispy Treat. He looked to me with fear as I handed him my wrapper, and swallowed a mouthful of crispy, marshmallow goodness. “I believe I win..” With that, the Angel of Death bowed and vanished.

I sat down to an episode of Full House and ordered a pizza... cuz there’s never anything to eat at my house.
```

---

## IC-1919: Repetition and Beginning, Middle, End

- Title: Repetition and Beginning, Middle, End
- Author (byline): Phil Kaye
- Work: Date & Time
- Publisher: Button Poetry
- Publication date as stated: Sept 2018
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 402
- Already set (do not supply): none

### Source block (context only)

```text
Author: Phil Kaye
Book: Date & Time
ISBN: 978-1943735365
Publisher: Button Poetry
Date (Month/Year): Sept 2018
```

### Introduction (context only: never use it for content warnings)

```text
Words shape our thinking, trigger emotions and affect our behavior. Words are power. No one knows this better than poet Phil Kaye who, at a very young age, struggled to use his words during his parents' divorce. He developed a stutter that has challenged him to this day. But the power of words has set him free.

Repetition; Beginning, Middle, End by Phil Kaye
```

### Performance text (classify this)

```text
Repetition My mother taught me this trick If you repeat something over and over again it loses its

meaning For example: Homework, homework, homework, homework,

homework, homework, homework, homework, See, nothing

Our existence, she said, is the same way. You watch the sun set too often, it just becomes 6 PM You make the same mistake over and over; you’ll stop

calling it a mistake
If you just
wake up, wake up, wake up, wake up, wake up.
one day you’ll forget why
Nothing is forever, she said.

My parents left each other when I was 7 years old Before their last argument they sent me off to the

neighbor’s house,
like some astronaut jettisoned from the shuttle.
When I came back there was no gravity in our home, beds
floating
I imagined it as an accident, that when I left
They whispered to each other “I love you” so many times

they forgot what it meant Family, family, family, family, family, family

My mother taught me this trick If you repeat something over and over again it loses its

meaning
This became my favorite game
It made the sting of words evaporate.
Separation, separation, separation;
see, nothing
Apart, apart, apart;
see, nothing

I am an injured handyman now I work with words all day Shut up, I know the irony!

When I was young, I was taught that the trick to dominating
language
was breaking it down
Convincing it that it was worthless
I love you, I love you, I love you, I love you;
See, nothing

Soon after my parents’ divorce, I developed a stutter
Fate is a cruel and efficient tutor
There is no escape in stutter
You feel the meaning of every word drag itself up your

throat
S-s-s-separation
Stutter is a cage made of mirrors
Every “Are you ok?”
Every “What’d you say?”
Every “Come on kid, spit it out”
Is a glaring reflection you cannot escape
Every terrible moment skips upon its own announcement
Over and over until it just hangs there,
floating in the middle of the room

Mom, Dad, I am not wasteful with my words anymore. Even now after hundreds of hours of practicing away my

stutter, I still feel the claw of meaning in the bottom of my

throat.
I have heard that even in space;
You can hear the scratching of a
I-I-I-I love you.
```

---

## IC-1920: Revenge of the Outcast – A Collection

- Title: Revenge of the Outcast – A Collection
- Author (byline): Solomon Walker, Eric Robert Nolan and Lamar Jorden
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1124
- Already set (do not supply): none

### Source block (context only)

```text
Author: Solomon Walke
On-line Transcript:
https://medium.com/@creativehubs2/revenge-of-the-
outcast-a-poem-80ee1b52d50e
Publisher: Medium.com
Date (Month/Year): July 26, 2023
Author: Eric Robert Nolan
Book: Peeking Cat Anthology 2018, Pgs 59-61
ISBN: 978-0244422905
Publisher: Lulu.com
Date (Month/Year): Oct 2018
Author: Lamar Jorden
Documentary: Louder than a Bomb, Film Curriculum,
Pg 37
https://www.louderthanabombfilm.com/docs/LTAB-Film-
Curriculum.pdf
ISBN: Documentary DVD
Publisher: Siskel/Jacobs Productions
Date (Month/Year): Mar 2012
*Material used in the introduction can be found here:
https://www.npr.org/sections/health-
shots/2019/02/10/690372199/school-shooters-whats-their-
path-to-violence
```

### Introduction (context only: never use it for content warnings)

```text
* It's hard to empathize with someone who carries out a school shooting. The brutality is unspeakable, traumatizing to students and communities. But what is it like to be one of these school shooters?

Studies have shown that most school shooters lead particularly stressful lives: They live with physical or emotional abuse and unstable families. Most have experienced significant losses. Couple these personal traumas with social rejection at school, and you have students with anxiety, depression, aggression and antisocial behavior.

When someone has been struggling alone and failing, their despair can turn into anger. There's loss. There's humiliation. There's anger. There's blame. They may wish someone would kill them. They may wish they could kill themselves. Or they may start fantasizing about revenge.

Revenge of the Outcast – A Collection with poems by Solomon Walker, school shooter by Eric Robert Nolan and Shooter by Lamar Jorden
```

### Performance text (classify this)

```text
Revenge of the Outcast In a world where darkness reigns supreme, Where outcasts dwell, unseen, unheard, A tale of revenge, a daring dream, Unfolds in verses, untamed, uncurled.

Once an outcast, shunned by the crowd,
A soul forgotten, left to decay,
But within his heart, a fire avowed,
To rise above, to make them pay.

With every step, he embraced the night,
A cloak of shadows, his armour true,
His eyes ablaze, burning with spite,
He vowed to seek vengeance, to pursue.

Through treacherous forests, he did tread, Where whispers of danger echoed loud, His heart pounding, filled with dread, Yet fuelled by a purpose, strong and proud.

He ventured into the dragon’s lair,
Where flames danced, fierce and wild,
With sword in hand, he faced despair,
Defying fate, like an innocent child.

The dragon roared, its fury unleashed, But the outcast fought with all his might, His blade clashed against scales, unceased, A battle of darkness, a clash of light.

With a final strike, the dragon fell,
Its reign of terror, forever ceased,
The outcast stood tall, triumphant, compelled,
His victory, a testament to the beast.

But revenge was not yet fully claimed,
For the outcast had a score to settle,
He journeyed on, his heart untamed,
To face the ones who caused his mettle.

Through stormy seas, he sailed with might, To the kingdom where his tormentors dwelled, His eyes gleamed with a vengeful light, As the waves crashed, his fury swelled.

He stormed the castle, walls crumbling down, His presence, a tempest, fierce and grand, His enemies trembled, their faces a frown, As he took their fate into his own hand.

With each strike, he reclaimed his pride,
His tormentors fell, one by one,
Their cries for mercy, swiftly denied,
As the outcast’s revenge was finally done.

In the aftermath, he stood alone, A victor, yet still an outcast, true, But in his heart, a newfound tone, A sense of purpose, a life anew. For revenge had shaped him, made him strong, And though he remained an outcast, scorned, He had proven them all, proved them wrong, That even the forgotten can be reborn.

So let this tale be a testament,
To the power of vengeance, fierce and bold,
That even the outcasts, long lamented,
Can rise above, their stories untold.

For in the depths of darkness, they find, A strength untamed, a spirit unbound, And in their hearts, a fire designed, To conquer the world, to astound.

school shooter (excerpt)
Grendel’s mother wanted murder; but we all knew that,
you knew that just by looking at her:
the green and odorous skin like dark olive parchment over
her cheeks’ low bones,
the blackening teeth where the stale blood caked
and dried in her receding gumlines
like burgundy ink on her molars and incisors,
and a blackening-scarlet
stain on her canines.

Remember her mocking our own mothers? Her derisive voice was like the crack of splitting emeralds, asking, “Am I so strange to young eyes?”

Remember the boiling fat on her tongue and
her victims’ burning skin there?
The scalps she held in her upturned palms
were like watery garments.
Her talons were as black
as snapping-turtle shells.
We all knew at once that we were quarry.

Remember her
sorrel-colored cataracts?
Her eyes were as green seas
boiling under Ragnarok.
Remember their ruptured capillaries
like collapsing red galaxies?
Remember her very irises bleeding?

But what if evil appeared
not as the face of Grendel’s mother,
but, rather, the ordinary boy in her maw —
as unexotic and as common
as we are?

If we were boys and girls again
and bored in English class —
maybe at Beowulf’s strangeness —
and he were next to us,
with neither green skin
nor blood along his molars,
if he wanted murder, could we tell?

His face was as a clock’s face — prosaic and round.
Neither silt nor sinew lined his frame.
His gaze did not depict a grisly cosmos;
no galaxies had hemorrhaged in his eyes.
Would the difference be perceptible there
between wanting to kill time
and wanting to kill ten?
Would we know that we were quarry?

Shooter (excerpt)
2:36 pm
Bullets bask in barrel before booming.
Students zooming towards exit run rampant
like thoughts in my head.
Any student not thought to be dead
gets shot again
Students think "not again" . . .
Students scream aloud as rounds rip through the crowd.
The scene is wild
but for once,
I get to be center stage.
Behind my blank look I'm in a rage,
a renegade,
tamed, but in a cage I stand
stance stiff as a statue starin' at you.
Shots and shotgun shells fly like pterodactyls.

The scene is so thick,
which fits cuz I'm an outcast.
But this is no "Player's Ball."
This is a scene of prayers, calls and screams.
Anybody from teens to professors to football players crawl,
and I spray ‘em all.
Lay ‘em all down in a timely fashion.
As they're dashin' to safety, I'm safely solid as a mannequin
Brandishin' three handguns and a shotgun
The world is goin’ crazy,
The world is goin’ crazy, I'm just a daily reminder.
Scrutinize my autopsy, you still won't find a spine to justify
my acts.
You run from my bullets but can't escape the fact that this
goes back.
This goes back to the 19th century in elementaries around
the globe.
1891
St. Mary's Parochial School.
Fools before me used shotguns to empty a class.
Fast forward 36 years.
1927
2nd to 6th graders were the targets,
45 were martyred,
58 more wounded at the hands of school board member
Andrew Kehoe.
Y'all upset at me though.
This coward killed kids because his farm was being
foreclosed.

I swear the world is goin' crazy. The world is insane.

Gunsmoke and sudden death make the atmosphere putrid.
Today's Valentine's Day homie, I wanna be Cupid.
Slugs replace arrows,
Icebox replaces heart that I can't seem to find.
No one seems to mind that students show more school
spirit when
someone is dead.

Shots to the head seemingly make you more popular - that has to be why most the shooters kill themselves My blood boils at the realization that you can get killed for nothin’ in college just as easily as you can in a war or in jail, but we're still more concerned with weed sales . . .

The world is beyond crazy. Why are we overseas when the real war is in front of us? The real war is in the institutions that are supposed to build a better tomorrow. The sorrow is in the hearts of those who fall victim to those dimming bright futures. Because guns don't kill people, we kill ourselves

I'm sorry. I'm sorry. . . I’m sorry. . .
```
