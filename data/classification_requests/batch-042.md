# Classification request: batch 42 of 63 (40 records, IC-1641 to IC-1680)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-042-reply.json`.

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

## IC-1641: Night Sky with Exit Wounds (Selections from)

- Title: Night Sky with Exit Wounds (Selections from)
- Author (byline): Ocean Vuong
- Work: Not specified
- Publisher: Copper Canyon Press
- Publication date as stated: April 5, 2016
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1161
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ocean Vuong
ISBN: 978-1556594953
Publisher: Copper Canyon Press
Date (Month/Year): April 5, 2016
*Music and Lyrics to White Christmas can be found at
https://www.youtube.com/watch?v=w9QLn7gM-hY
```

### Introduction (context only: never use it for content warnings)

```text
Near the end of the Vietnam War in 1975, people in South Vietnam began to flee due to the rise of communism in Vietnam. Armed Forces Radio played Irving Berlin’s “White Christmas” as a code to begin the evacuation of American civilians and Vietnamese refugees during the fall of Saigon. Ocean Vuong and his family were among those refugees.

Selections from Night Sky with Exit Wounds by Ocean Vuong
```

### Performance text (classify this)

```text
Aubade with Burning City

Milkflower petals on the street

like pieces of a girl’s dress.

Some grenades explode with a vision of white flowers. Baby’s breath blooming in a darkened sky, across my chest.

– From Notebook Fragments

May your days be merry and bright ...*

He fills a teacup with champagne, brings it to her lips.

Open, he says.

She opens.

Outside, a soldier spits out

his cigarette as footsteps fill the square like

stones

fallen from the sky. May all your Christmases be white

as the traffic guard unstraps his holster.

His hand running the hem of her white dress. A single candle.

Their shadows: two wicks.

A military truck speeds through the intersection,

children

shrieking inside. A bicycle hurled

through a store window. When the dust rises, a

black dog

lies panting in the road. Its hind legs

crushed into the shine

of a white Christmas.

On the bed stand, a sprig of magnolia expands like a

secret heard

for the first time.

The treetops glisten and children listen, the chief of

police

facedown in a pool of Coca-Cola.

A palm-sized photo of his father soaking

beside his left ear.

The song moving through the city like a widow.

A white ... A white ... I’m dreaming of a curtain of

snow

falling from her shoulders.

Snow scraping against the window. Snow shredded

with gunfire. Red sky.

Snow on the tanks rolling over the city walls. A helicopter lifting the living just

out of reach.

The city so white it is ready for ink.

The radio saying run run run. Milkflower petals on a black dog

like pieces of a girl’s dress.

May your days be merry and bright. She is saying

something neither of them can hear. The hotel

rocks

beneath them. The bed a field of ice.

Don’t worry, he says, as the first shell flashes

their faces, my brothers have won the war

and tomorrow ...

The lights go out.

I’m dreaming. I’m dreaming ...

to hear sleigh bells in the snow ...

In the square below: a nun, on fire,

runs silently toward her god —

Open, he says.

She opens.

******

When we left it, the city was still smoldering. Otherwise

it was a perfect spring morning. White hyacinths gasped

in the embassy lawn. The sky was September-blue and

the pigeons went on pecking at bits of bread scattered

from the bombed bakery. Broken baguettes. Crushed

croissants. Gutted cars. A carousel spinning its

blackened horses. He said the shadow of

missiles growing larger on the sidewalk looked like god

playing an air piano above us. He said There is so much

I need to tell you.

– From Immigrant Haibun TRANSITION

But those words of wisdom would never come.

Ocean Vuong once said: Fragments are what make my life. I gather them all together in my arms and carry what I can: Here is where things have become disastrous; here is where I learned to live through the pain; here is where I’ve come to stand, knees trembling, after being bent double in grief.

Grief for Vietnam and grief for his father.

Telemachus

Like any good son, I pull my father out of the water, drag him by his hair

through white sand, his knuckles carving a trail the waves rush in to erase. Because the city

beyond the shore is no longer where he left it. Because the bombed

cathedral is now a cathedral of trees. I kneel beside him to see how far

I might sink. Do you know who I am,
Ba? But the answer never comes. The answer
is the bullet hole in his back, brimming
with seawater. He is so still I think

he could be anyone’s father, found the way a green bottle might appear

at a boy’s feet containing a year he has never touched. I touch

his ears. No use. I turn him over. To face it. The Cathedral

in his sea-black eyes. I begin the faithful work of drowning.

TRANSITION

Although Ocean Vuong never stepped foot on the active battlefields of Vietnam, the reality of the war that drove his family from his homeland is still there. Memories still haunt him.

Self-Portrait with Exit Wounds

Instead, let it be the echo to every footstep drowned out by rain, cripple the air like a name

flung onto a sinking boat, splash the kapok’s bark through rot & iron of a city trying to forget

the bones beneath its sidewalks, then through the refugee camp sick with smoke & half-sung

hymns, a shack rusted black & lit with Bà Ngoại’s last candle, the hogs’ faces we held in our hands

& mistook for brothers, let it enter a room illuminated with snow, furnished only with laughter, Wonder Bread

& mayonnaise raised to cracked lips as testament to a triumph no one recalls, let it brush the newborn’s

flushed cheek as he’s lifted in his father’s arms, wreathed with fishgut & Marlboros, everyone cheering as another

brown gook crumbles under John Wayne’s M16, Vietnam burning on the screen, let it slide through their ears,

clean, like a promise, before piercing the poster of Michael Jackson glistening over the couch, into the supermarket where a Hapa woman is ready to believe every white man possessing her nose

is her father, may it sing, briefly, inside her mouth, before laying her down between jars of tomato

& blue boxes of pasta, the deep-red apple . . .

In Vietnamese, the word for grenade is “bom,” from the French “pomme,” meaning “apple” . . . Or was it American for “bomb?”

– From Notebook Fragments

. . . the deep-red apple rolling from her palm, then into the prison cell

where her husband sits staring at the moon until he’s convinced it’s the last wafer

god refused him, let it hit his jaw like a kiss we’ve forgotten how to give one another, hissing

back to ’68, Ha Long Bay: the sky replaced with fire, the sky only the dead

look up to, may it reach the grandfather f***** the pregnant farmgirl in the back of his army jeep, An American soldier f***** a Vietnamese farmgirl. Thus my mother exists. Thus I exist. Thus no bombs = no family = no me.

– From Notebook Fragments

his blond hair flickering in napalm-blasted wind, let it pin him down to dust where his future daughters rise,

fingers blistered with salt & Agent Orange, let them tear open his olive fatigues, clutch that name hanging

from his neck, that name they press to their tongues to relearn the word live, live, live—but if

for nothing else, let me weave this deathbeam the way a blind woman stitches a flap of skin back

to her daughter’s ribs.

Grandma said, “In the war they would grab a baby, a soldier at each ankle and pull . . .”

– From Notebook Fragments

Yes—let me believe I was born to cock back this rifle, smooth & slick, like a true

Charlie, like the footsteps of ghosts misted through rain as I lower myself between the sights—& pray

that nothing moves.
```

---

## IC-1642: The Nightmare Before Christmas

- Title: The Nightmare Before Christmas
- Author (byline): Tim Burton
- Work: Not specified
- Publisher: Hyperion
- Publication date as stated: Oct 1994
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1342
- Already set (do not supply): none

### Source block (context only)

```text
Author: Tim Burton
ISBN: 978-0786810147
Publisher: Hyperion
Date(Month/Year): Oct 1994
```

### Introduction (context only: never use it for content warnings)

```text
Meet Jack Skellington. He's in charge of making Halloweenland the coolest creepy place around. But when Jack suddenly grows bored with tricks and treats, he goes searching for new ways to celebrate and he finds them in Christmas Town! Christmas, Jack decides, is just what Halloweenland and the world needs! He sets out to take over the role of Santa. But can anything good come of a tall and lanky skeleton dressed up as everyone's favorite jolly old elf? The Nightmare Before Christmas by Tim Burton
```

### Performance text (classify this)

```text
It was late one fall in Halloweenland,
and the air had quite a chill.
Against the moon a skeleton sat,
alone upon a hill.
He was tall and thin with a bat bow tie;
Jack Skellington was his name.
He was tired and bored in Halloweenland
"I'm sick of the scaring, the terror, the fright.
I'm tired of being something that goes bump in the
night.
I'm bored with leering my horrible glances,
And my feet hurt from dancing those skeleton dances.
I don't like graveyards, and I need something new.
There must be more to life than just yelling,
'Boo!'"

Then out from a grave, with a curl and a twist, Came a whimpering, whining, spectral mist. It was a little ghost dog, with a faint little bark, And a jack-o'-lantern nose that glowed in the dark. It was Jack's dog, Zero, the best friend he had, But Jack hardly noticed, which made Zero sad.

All that night and through the next day, Jack wandered and walked. He was filled with dismay.

Then deep in the forest, just before night, Jack came upon an amazing sight. Not twenty feet from the spot where he stood Were three massive doorways carved in wood. He stood before them, completely in awe, His gaze transfixed by one special door. Entranced and excited, with a slight sense of worry, Jack opened the door to a white, windy flurry.

Jack didn't know it, but he'd fallen down In the middle of a place called Christmas Town! Immersed in the light, Jack was no longer haunted. He had finally found the feeling he wanted. And so that his friends wouldn't think him a liar, He took the present filled stockings that hung by the fire. He took candy and toys that were stacked on the shelves And a picture of Santa with all of his elves. He took lights and ornaments and the star from the tree, And from the Christmas Town sign, he took the big letter C.

He picked up everything that sparkled or glowed.
He even picked up a handful of snow.
He grabbed it all, and without being seen,
He took it all back to Halloween.

Back in Halloween a group of Jack's peers Stared in amazement at his Christmas souvenires. For this wondrous vision none were prepared. Most were excited, though a few were quite scared!

For the next few days, while it lightninged and thundered, Jack sat alone and obsessively wondered. "Why is it they get to spread laughter and cheer While we stalk the graveyards, spreading panic and fear?

Well, I could be Santa, and I could spread cheer! Why does he get to do it year after year?" Outraged by injustice, Jack thought and he thought. Then he got an idea. "Yes. . .yes. . .why not!"

In Christmas Town, Santa was making some toys When through the din he heard a soft noise. He answered the door, and to his surprise, He saw weird little creatures in strange disguise. They were altogether ugly and rather petite. As they opened their sacks, they yelled, "Trick or treat!" Then a confused Santa was shoved into a sack And taken to Halloween to see mastermind Jack.

In Halloween everyone gathered once more,
For they'd never seen a Santa before
And as they cautiously gazed at this strange old man,
Jack related to Santa his masterful plan:
"My dear Mr. Claus, I think it's a crime
That you've got to be Santa all of the time!
But now I will give presents, and I will spread cheer.
We're changing places I'm Santa this year.
It is I who will say Merry Christmas to you!
So you may lie in my coffin, creak doors, and yell, 'Boo!'
And please, Mr. Claus, don't think ill of my plan.
For I'll do the best Santa job that I can."

And though Jack and his friends thought they'd do a good job, Their idea of Christmas was still quite macabre. They were packed up and ready on Christmas Eve day When Jack hitched his reindeer to his sleek coffin sleigh, But on Christmas Eve as they were about to begin, A Halloween fog slowly rolled in.

Jack said, "We can't leave; this fog's just too thick. There will be no Christmas, and I can't be St. Nick."

Then a small glowing light pierced through the fog.
What could it be?. . .It was Zero, Jack's dog!
Jack said, "Zero, with your nose so bright,
Won't you guide my sleigh tonight?"

And to be so needed was Zero's great dream, So he joyously flew to the head of the team. And as the skeletal sleigh started its ghostly flight, Jack cackled, "Merry Christmas to all, and to all a good night!"

'Twas the nightmare before Christmas, and all though
the house,
Not a creature was peaceful, not even a mouse.
The stockings all hung by the chimney with care,
When opened that morning would cause quite a scare!
The children, all nestled so snug in their beds,
Would have nightmares of monsters and skeleton heads.
The moon that hung over the new-fallen snow
Cast an eerie pall over the city below,
And Santa Claus's laughter now sounded like groans,
And the jingling bells like chattering bones.
And what to their wondering eyes should appear,
But a coffin sleigh with skeleton deer.
And a skeletal driver so ugly and sick
They knew in a moment, this can't be St. Nick!
From house to house, with a true sense of joy,
Jack happily issued each present and toy.
From rooftop to rooftop he jumped and he skipped,
Leaving presents that seemed to be straight from a
crypt!
Unaware that the world was in panic and fear,
Jack merrily spread his own brand of cheer.

He visited the house of Susie and Dave; They got a Gumby and Pokey from the grave. Then on to the home of little Jane Neeman; She got a baby doll possessed by a demon. A monstrous train with tentacle tracks, A ghoulish puppet wielding an ax, A man eating plant disguised as a wreath, And a vampire teddy bear with very sharp teeth. There were screams of terror, but Jack didn't hear it, He was much too involved with his own Christmas spirit! Jack finally looked down from his dark, starry frights And saw the commotion, the noise, and the light. "Why, they're celebrating, it looks like such fun! They're thanking me for the good job that I've done."

But what he thought were fireworks meant as goodwill Were bullets and missiles intended to kill. Then amidst the barrage of artillery fire, Jack urged Zero to go higher and higher. And away they all flew like the storm of a thistle, Until they were hit by a well guided missile. And as they fell on the cemetery, way out of sight, Was heard, "Merry Christmas to all, and to all a good night."

Jack pulled himself up on a large stone cross, And from there he reviewed his incredible loss. "I thought I could be Santa, I had such belief" Jack was confused and filled with great grief. Not knowing where to turn, he looked toward the sky, Then he slumped on the grave and he started to cry. And as Zero and Jack lay crumpled on the ground, They suddenly heard a familiar sound.

"My dear Jack," said Santa, "I applaud your intent. I know wreaking such havoc was not what you meant. And so you are sad and feeling quite blue, But taking over Christmas was the wrong thing to do. I hope you realize Halloween's the right place for you. There's a lot more, Jack, that I'd like to say, But now I must hurry, for it's almost Christmas day." Then he jumped in his sleigh, and with a wink of an eye, He said, "Merry Christmas," and he bid them good bye.

Back home, Jack was sad, but then, like a dream, Santa brought Christmas to the land of Halloween.
```

---

## IC-1643: No Child Left Behind with poems by RedLipsandTattoos, Dominique Christina and Denice Frohman No Child Left Behind Leaves Entire Schools Behind

- Title: No Child Left Behind with poems by RedLipsandTattoos, Dominique Christina and Denice Frohman No Child Left Behind Leaves Entire Schools Behind
- Author (byline): RedLipsandTattoos (pen name)
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 801
- Already set (do not supply): none

### Source block (context only)

```text
Author: RedLipsandTattoos (pen name)
On-line Transcript:
https://allpoetry.com/column/7522581-No-Child-
Left-Behind-Leaves-Entire-Schools-Behind--by-
RedLipsAndTattoos
Publisher: All Poetry.com
Date (Month/Year): July 2004
Author: Dominique Christina & Denice Frohman
On-line Transcript:
https://www.poemhunter.com/poem/no-child-left-
behind-2/
Publisher: Poem Hunter.com
Date (Month/Year): June 18, 2019
Video of performance by the poets at the College Unions
Poetry Slam Invitational in Boulder, Colorado in March
2014 can be found here
https://www.youtube.com/watch?v=RHSqUyi6GUU&list=
PLC5PJtWBigV0NAqi2V2vbyqmpuJU1dURm&index=5
```

### Introduction (context only: never use it for content warnings)

```text
It was 2002, and the No Child Left Behind Act (NCLB) was a well-intentioned piece of bipartisan legislation with the primary aim of ensuring equitable educational opportunities for all students in the American public education system. However, it was devised without consideration for how it might actually harm the public-school experience. Subsequently, NCLB currently operates with many fundamental flaws that damaged American public education. Simply put, "No Child Left Behind" forced many schools to focus on budgetary constraints instead of the education of students. Even though "No Child Left Behind" was repealed in 2015, it serves as a prime example of how a body of law with the right intentions can negatively impact others simply by its execution.

These two poems, No Child Left Behind Leaves Entire Schools Behind by RedLipsandTattoos and No Child Left Behind by Dominique Christina & Denice Frohman, detail the injustices of the American education system while recognizing the flaws in the academic slogan “No Child Left Behind.” They address the communities that are often left out of education in America.
```

### Performance text (classify this)

```text
One morning a prominent, well-to-do, Caucasian man, who most likely attended private schools, woke up with the idea for the No Child Left Behind Act.

No Child Left Behind Leaves Entire Schools Behind Continued . . . At first, everyone in this little country you may have heard of, called the U.S.A., thought the idea was just brilliant. They figured it wouldn't affect the private school children, and since a rich, smart Caucasian man thought it up, everyone was certain it would benefit all public-school children, even the low-income African-American girls! They had a lot of faith in the new act.

As each year passed, and more places instated the act, in hopes no child would be left behind, school districts began receiving complaints from parents. What audacity these parents must have, complaining that this wonderful act was leaving their child behind!

These parents made outrageous claims. In one state in particular, that was having an especially tough time, called Oregon, the most outrageous claims were made. Parents and students alike came together, and many realized that students were being given unnecessary tests, that don't truly gauge a school's success. Schools that were doing just fine were suddenly being torn to shreds, and losing students, as well as funding, because their students didn't do wonderful on one test, and they were marked a bad school.

Soon, children from these 'bad schools' were being rescued from them, and their schools began losing more and more funding, and became the bad schools they'd originally been labeled as. The students were bussed to better schools, that then received more funding, that they didn't need, since they were already a high-income, well-testing school.

So now, the good schools are better, and the decent schools are bad, and the bad schools are horrible, while the private schools have remained expensive and perfectly fine. Some students are excelling, while thousands more, in low-income schools that happened to test poorly, are being left far behind. I wonder if that prominent, well-to-do Caucasian man will ever realize his act is failing more students than it's helping? I doubt it.

No Child Left Behind by Dominique Christina and Denice Frohman

An entrance to a west Philadelphia high school.
Officer with gun perched on each waist,
Asks me if I have any weapons.
I hold up my book,
He doesn't find that funny.
Tells me to empty pockets and walk through the metal

detector.
8: 03 am,
I wait for two students to pass through the metal detector
first,
Already wondering if they have learned anything at all.

I heard that the newly built prison a few miles away Bought the test scores of failing schools to use as

wallpaper.
But we say no child left behind.
Cause it's a slogan for the slick.
To convince you that you have not heard it before.
Like your momma did not work three jobs,
Average two hours of sleep a night,
So you would not be left behind.
No child left behind is a bumper sticker, a caption,
An empty slogan with no room for imagination.
So our teacher asked if we have dreams.
11 students raise their hands barley above their shoulders,
As if they were sitting in history class unsure of the right

answer. But there is no right answer I say, And they are far too comfortable with the right to remain

silent.
I'm escorted to an auditorium
Where there are 130 other black and Latino students.
We talk about hip hop.
They think poetry is what old white people do.

I tell them my favorite poem is "Miss Fat Booty,"
Cause I like the story telling.
They giggle as if they're still kids,
Cause kids these days tie poetry to a chair and they torture

it with bad hip hop,
They flog and they beat it,
They trick and B-E-T it,
Deny it food water and light,
Then figure out how to booty shake to it.
No child left behind even when the culture is sick
The first time I read a book by a black author was in college,
The wind in my chest stood up,
It had been 18 long years of textbooks filled with

everything but me.
See the quickest way to silence a mouth
Is to treat it as if no one had come before.
There are thousands of unreported lynchings,
That happen in American classrooms each year.
The victims are between the ages of five and nineteen
They are black, and brown, and poor, and different,
Round pegs in square classrooms.
Children suffering for not being who we want them to be.

For having voices too loud,
accents too thick,
pockets too thin,
For our classrooms to honor us --
just as we are.
```

---

## IC-1644: Nothing New Here

- Title: Nothing New Here
- Author (byline): Jasmine Mans, David James Hudson, and Danez Smith
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 996
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jasmine Mans
Book: Chalk Outlines of Snow Angels
ASIN: B008JHIM2Y
Publisher: Thorn10 Publishing
Date (Month/Year): July 2012
Author: David James Hudson
ISBN: On-Line transcript (NSDA Approved Website)
https://www.poemhunter.com/poem/another-unoriginal-
poem-about-police-brutality/
Publisher: Poem Hunter.com
Date (Month/Year): June 20, 2017
Author: Danez Smith
ISBN: On-Line transcript (NSDA Approved Website)
https://www.poemhunter.com/poem/principles-3/
Publisher: Poem Hunter.com
Date (Month/Year): Sept 21, 2016
```

### Introduction (context only: never use it for content warnings)

```text
In the words of Dr. Martin Luther King, Jr. “Darkness cannot drive out darkness; only light can do that. Hate cannot drive out hate; only love can do that.” He also encouraged people to keep moving forward. He said “If you can’t fly, then run; if you can’t run, then walk, if you can’t walk then crawl, but whatever you do, keep moving forward. Today . . . I stand. Today, I speak out.

Nothing New Here – A collection including Newark Riots and Black Son by Jasmine Mans, Another Unoriginal Poem About Police Brutality by David James Hudson and Principles by Danez Smith.
```

### Performance text (classify this)

```text
Newark Riots / Black Son* by Jasmine Mans

Blood has decorated these streets They have begun to look like pastures of rose petals. Black boys have gotten so fed up with their prayers

drowning by bedside, They load their guns into the sky to make sure God is listening

We are chalk outlines of snow angels, We breathe like death is lurking on the edge of our spleens We dance in the wind to the crackles of gun shells, Jerk bodies back like God is head puppeteer of this

destruction.

Death looks too much like children
Maybe we’ve been dancing on the edge
Of God’s sanity for too long.
Some casualties of genocide look too familiar

To not scream.

* “I am just afraid to raise a black son”
Who will spend the rest of his life
Praying for a melody or a melanin
Safe enough to scream in.

A boy who had to be a martyr for a war He never asked for.

Another Unoriginal Poem about Police Brutality by David James Hudson

You have heard this poem before. You have heard the unoriginal repetitious poetics

of a shot

of a shot

of a shot singeing the night air - of shell casings on concrete and cases of claims of standard police procedure - of cases of batons that

leave
red and
white and
blue on
black and
bullets in brown bodies and
bullets in sleeping bodies and
bullets in running bodies and
bullets in bodies holding umbrellas or
holding pens or
holding other things that look like guns or
reaching for - he was
reaching for - they say she was
reaching for some expectation of dignity, service, and

protection This is an unoriginal poem about police brutality.

You will hear the same sets of metaphors once more:

white
security, verdicts of
innocence, inconsequential bodies of
evidence, ballistics and emergency lights,
repetitious, circling around and around like
circular stories like
unoriginal poems like
a red stream of consciousness flowing through senses

punctured like
sentences punctuated with
bullet-like precision again and
again and
again and

There is really nothing new here.

This is as unoriginal as a mundane untouched sheet of

white paper or granddad's white Klan sheets untouched in closets

beside uniforms or
uniform otherwise spotless records -
You have heard these uniform stories before, I imagine..
The same story again and
again gets old, we are
told. We'd rather plug our ears, and so
there is silence in
waiting for
newness to
appear.
Silence:
like the eerie stillness of
prisons and profits of
plantations and poverty churned out in
steady cycles of factory-like
production - Call it run-of-the-mill:
not poetic, but prosaic
like the still persistence of
the largest private prison corporation traded
on the New York Stock Exchange - like
the silence of stock ticker tapes circulating at the

bottom
of TV screens - an economics of
morbidity - a market that demands
an endless supply of unremarkable names -
like Michael Brown
like [Trayvon Martin]
like Tamar Rice
like [George Floyd]
like [Breonna Taylor]
like -
Are you tired yet?

Then set your aesthetics aside. There is no originality The same old stories out there mean the same old stories here, so this will stop being cliché when that stops being cliché -when clichés are no longer scripted in blood stuttering like last breaths along sidewalks

Until then . . . (*Coda to the end of the selection)

Principles by Danez Smith ask not what your country can do for you ask if your country is your country ask if your country is addicted to blood ask if your country is addicted to forgetting ask if your country was built of stolen land and stolen breath, if democracy is a chain

tight as skin around your neck ask if your comfort means round

the corner a man is dead cause a cop

mistook his body for a gun ask if your new apartment used to belong

to someone who couldn't afford to look

like you, ask yourself if all the things

you are scared to admit are shovels

slowly filling up a brown boy's throat.

all lives don't matter the same as all lives

what my life mean to you? am i talking to you?

do you wish me justice or do you wish I would just shut up already, vanish already?

why they
send bullets through our
bodies like they trying
to see if we real or just
a bad dream? why they
nightmare us into beast?
why they comfort the cops
and not the families?
why administrative leave?
why they look up the record
before they check the pulse?
why they try to spin the story
before they call the ambulance?
why they more worried about
getting caught then they worried
about the killing? why they
protect and serve themselves
from us? why they want us to
apologize for being
in the way of they bullets?
what good is police?
what is the American dream
to a brown person
except a dream of America
leaving us alone?

i don't want America no more.
i want to be a citizen of something new.
i want a country for the immigrant hero.
i want a country where joy is as indigenous as the people.
i want a country that keeps its word.
i want a country that don't treat its people

like a virus.
i want a country not trying to cure itself of me.
i want a nation under a kinder god
i want justice the verb not justice the dream.
i want all lives to matter.

i want peace. i want equity.

hope is hard but i have it

let us not be idle or stunned by fear let us not be so comfortable that we ignore another's grieving instead of ending what makes [them] grieve

let us not be scared of the work because
it's hard
let us move the mountain
because the mountain must move

*Until then, chalk this up as
one more outline, another empty
shell of a thing - Just one more
unoriginal poem.
```

---

## IC-1645: Ode to Blue-Collar Workers

- Title: Ode to Blue-Collar Workers
- Author (byline): Phil Levine, Bella Cardenas, Beverly
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1186
- Already set (do not supply): none

### Source block (context only)

```text
Author: Philip Levine
ISBN: What Work Is (Section 1)
Publisher: Knopf
Date (Month/Year): April 1992
Author: Bella Cardenas
ISBN: Available On-Line Only
Publisher: PoetrySoup.com
Date (Month/Year): 2007
https://www.poetrysoup.com/poem/excuse_me_waitress_
58512
Author: Beverly Lafontaine
ISBN: Available On-Line Only
Publisher: PoetsReadingtheNews.com
Date (Month/Year): Aug, 26, 2019
http://www.poetsreadingthenews.com/2019/08/8977/
Cartpushers
Author: Kyle “Guante” Tran Myhre
Book: A Love Song, A Death Rattle, A Battle Cry (Pg 54-
55)
ISBN: 978-1943735334
Publisher: Button Poetry
Date (Month/Year): Feb 2018
```

### Introduction (context only: never use it for content warnings)

```text
Everyone has a story, but the sad fact of the matter is over the last several decades we as Americans have developed an unsettling tendency to make sweeping assessments about a person’s worthiness as a human being based upon the kind of work they do. Cartpushers, cashiers, janitors, servers, bartenders - individuals working in these types of blue-collar, low-wage jobs simply don’t make enough to support themselves, and if they have a family . . . the struggle to survive is even more overwhelming. They often take on 2 and even 3 jobs to stay one step ahead of the streets. Today I chose to tell the stories that most people never choose to hear.

Ode to the Blue-Collar Workers with the following poems: What Work Is by Philip Levine; Excuse me, Waitress by Bella Cardenas; Black Lung, Grim Future for Younger Miners by Beverly Lafontaine; and Cartpushers by Kyle “Guante” Tran Myhre
```

### Performance text (classify this)

```text
Lafontaine and Kyle “Guante” Tran Myhre

What Work Is by Philip Levine

We stand in the rain in a long line
waiting at Ford Highland Park. For work.
You know what work is—if you’re
old enough to read this you know what
work is, although you may not do it.
Forget you. This is about waiting,
shifting from one foot to another.
Feeling the light rain falling like mist
into your hair, blurring your vision
until you think you see your own brother
ahead of you, maybe ten places.
You rub your glasses with your fingers,
and of course it’s someone else’s brother,
narrower across the shoulders than
yours but with the same sad slouch, the grin
that does not hide the stubbornness,
the sad refusal to give in to
rain, to the hours of wasted waiting,
to the knowledge that somewhere ahead
a man is waiting who will say, “No,
we’re not hiring today,” for any
reason he wants. You love your brother,
now suddenly you can hardly stand
the love flooding you for your brother,
who’s not beside you or behind or
ahead because he’s home trying to
sleep off a miserable night shift
at Cadillac so he can get up
before noon to study his German.
Works eight hours a night so he can sing
Wagner, the opera you hate most,
the worst music ever invented.
How long has it been since you told him
you loved him, held his wide shoulders,
opened your eyes wide and said those words,
and maybe kissed his cheek? You’ve never
done something so simple, so obvious,
not because you’re too young or too dumb,
not because you’re jealous or even mean
or incapable of crying in
the presence of another man, no,
just because you don’t know what work is.

Excuse me, Waitress by Bella Cardenas

Slimy dishes and vigorous appetites
This is the life
Of a Waitress
Excuse me, miss

My potatoes are cold and
I can’t seem to function without
Your absolute attention from those
Bright Brown Eyes

Oily skin from daylight sneers
Dirty and Discreet desire from clients
Dark rimmed eyes fill the face
Silent
Pauper-like stealth clicking up empty glasses
Five for five fingers, sweep
Swift, sly, unseen, insignificant
Just another Blue Collar
Reverse Prima Donna

Heavy trays and snapping fingers
Tinkling of silverware against what was
Porcelain, soft and beautiful
Now hard and marble
Beautiful beautiful

I pull down this ponytail and let
Luscious curls cascade over delicate shoulders
Take off the putrid uniform
And don a red dress of passion and fairytales
Take off the weary, trodden on
Face of disgrace
Replaced with beams of moonshine
Leave
Dreams wasted away on 5 dollar tips

And be a Queen you’ll never know

Black Lung, Grim Future for Younger Miners
by Beverly Lafontaine
44 and wasting, the coal miner says, “It’s like
somebody’s sitting on your chest all the time.”
He covers his nose and mouth with a mask.
The ventilator resumes its vigil.
Outside, the sun barely warms the Kentucky air,
as clouds rush to fill the coming night sky.

The miner, his body a pot-bellied skeleton,
reminisces about a short-lived youth when
he felt like a man, his willingness to make the
mine yield the wealth of its deepest crevices
a source of pride, the price steep as his lungs

coalesced with the dusty air—black lung.
His father and grandfather were hollow men
at 60 years of age. Thanks to technology, his digs
were deeper, deadlier. “You’ll die
to make other men rich,” his father said,

Bitter this now, her meagre earnings, five days a week steering a school bus, are all that keep a tinny roof over their heads.

With little hope, he joins the vigil of stick men outside the office of the senator who doesn’t come home to Kentucky any more.

by Kyle “Guante” Tran Myhre

It’s not rocket science. It’s a ten-foot piece of rope with a hook at the end; we got three of ‘em hanging in the equipment shed—one of ‘em is thicker, but a little shorter; one of them looks thin as shoelaces but it’s a half-foot longer. If you got first pick, take that one—looks flimsy, but trust me: you’ll break before it does. Try to keep up.

See, these are the days before robots, and this is a city where people leave their empty apartments, leave their empty SUVs and finally, leave their empty shopping carts.

Here. For us. You can hook seven together with that rope and push ‘em back in. When it’s busy, grab ten. When it’s hell, stack thirty up and we’ll push ‘em in together.

Just be careful. Because these people: they’ll look right through you when they back out of those spots. When they take that corner at thirty miles per hour. When they forget that they forgot to use a blinker and cuss you out for walking through a crosswalk.

See, to that guy, we’re just background noise, uncredited extras in the eighty-year long made-for-TV romantic comedy that he calls life. We are neurons flickering stupidly, infantry stomping through the dreams he won’t remember upon awakening.

So make sure you wear comfortable shoes. Boots in the winter. Sneakers in the summer. Add pads as you grow older. Grow older. Learn to control a convoy of carts without that rope; just balance, coordination and will. Learn to control the fist that lives in your neck.

When these people just leave their carts sitting in the middle of a parking space, swallow. When they look right through you, swallow. When it’s fifteen below and a straightjacket would be warmer than these flimsy company coats and you’re working a double shift because you’ve heard rumors of layoffs, and the dapper manager saunters up and says how’s it goin’ chief? …swallow.

Understand: they will never understand this. The beauty of a parking lot at twilight, how the sky burns blue. The sweetness of every second when the big hand is on the eleven. The smile of the person who actually looks at you. We betray ourselves for seven dollars an hour. Our native language is white noise.

Cartpushers, cashiers, janitors, servers, bartenders: we are an army fighting a war we don’t believe in, in a country whose name we can’t pronounce, but we’re fighting. And we’re tired. But we’re fighting.

And we’re losing. But we’re fighting.

You get two fifteens and a half hour for lunch. Those breaks aren’t for your body, though. They’re for your spirit. See, with an eight-hour shift broken up into quarters, that’s just four two-hour shifts.

After punching in, chatting with the MOD and putting your gloves on, you can glance at your watch and say Wow. I’m almost halfway to being halfway done with half of half of half my shift. It makes the time fly right by.

You’ll be fine, kid. Just remember: smile. You’re representing the company. Remember: say hello to people when they come in.

And remember: when they look right through you, you’re still there.
```

---

## IC-1646: Of Loss and Grieving (A Collection)

- Title: Of Loss and Grieving (A Collection)
- Author (byline): Mary Oliver
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1456
- Already set (do not supply): none

### Source block (context only)

```text
Book: Evidence: Poems
ISBN: 978-0807068984
Publisher: Beacon Press
Date (Month/Year): 2009
Book: Evidence: Poems New and Selected Poems,
Volume One
ISBN: 978-0807068779
Publisher: Beacon Press
Date (Month/Year): April 15, 2004
Book: American Primitive
ISBN: 978-0316650045
Publisher: Back Bay Books
Date (Month/Year): April 1983
Book: Red Bird
ISBN: 978-0807068939
Publisher: Beacon Press
Date (Month/Year): April 1, 2009
Book: American Primitive
ISBN: 978-0316650045
Publisher: Back Bay Books
Date (Month/Year): April 1983
Book: Blue Horses
ISBN: 978-1594204791
Publisher: Penguin Press
Date (Month/Year): October 14, 2014
```

### Introduction (context only: never use it for content warnings)

```text
(no introduction)
```

### Performance text (classify this)

```text
I Want to Write Something So Simply
I want to write something
so simply
about love
or about pain
that even
as you are reading
you feel it
and as you read
you keep feeling it
and though it be my story
it will be common,
though it be singular
it will be known to you
so that by the end
you will think—
no, you will realize—
that it was all the while
yourself arranging the words,
that it was all the time
words that you yourself,
out of your heart
had been saying.

As a poet, Mary Oliver is an excellent antidote for the excesses of civilization. She is a poet of wisdom and generosity whose vision allows us to look intimately at a world not of our making. She speaks simply so that all can hear and her ruminations about death and grief whisper quietly to all of us who have experienced any type of loss. This is a collection of her most touching poetry. This collection is entitled “Of Loss and Grieving” by Mary Oliver When Death Comes

When death comes
like the hungry bear in autumn;
when death comes and takes all the bright coins from
his purse

to buy me, and snaps the purse shut; when death comes like the measle-pox

when death comes like an iceberg between the shoulder blades,

I want to step through the door full of curiosity, wondering: what is it going to be like, that cottage of darkness?

And therefore I look upon everything
as a brotherhood and a sisterhood,
and I look upon time as no more than an idea,
and I consider eternity as another possibility,
and I think of each life as a flower, as common
as a field daisy, and as singular,

and each name a comfortable music in the mouth, tending, as all music does, toward silence,

and each body a lion of courage, and something precious to the earth.

When it’s over, I want to say all my life I was a bride married to amazement. I was the bridegroom, taking the world into my arms.

When it’s over, I don’t want to wonder if I have made of my life something particular, and real.

I don’t want to find myself sighing and frightened, or full of argument.

I don’t want to end up simply having visited this world

TRANSITION The next poem in this collection follows Oliver on a visit to a hospital that dates back to before the Civil war and contemplates the timelessness of loss across the decades.

University Hospital, Boston

The trees on the hospital lawn
are lush and thriving. They too
are getting the best of care,
like you, and the anonymous many,
in the clean rooms high above this city,
where day and night the doctors keep
arriving, where intricate machines
chart with cool devotion
the murmur of the blood,
the slow patching-up of bone,
the despair of the mind.
When I come to visit and we walk out
into the light of a summer day,
we sit under the trees —
buckeyes, a sycamore and one
black walnut brooding
high over a hedge of lilacs
as old as the red-brick building
behind them, the original
hospital built before the Civil War.
We sit on the lawn together, holding hands
while you tell me: you are better.
How many young men, I wonder,
came here, wheeled on cots off the slow trains
from the red and hideous battlefields
to lie all summer in the small and stuffy chambers
while doctors did what they could, longing
for tools still unimagined, medicines still unfound,
wisdoms still unguessed at, and how many died
staring at the leaves of the trees, blind
to the terrible effort around them to keep them alive?
I look into your eyes
which are sometimes green and sometimes gray,
and sometimes full of humor, but often not,
and tell myself, you are better,
because my life without you would be
a place of parched and broken trees.
Later, walking the corridors down to the street,
I turn and step inside an empty room.
Yesterday someone was here with a gasping face.
Now the bed is made all new,
the machines have been rolled away. The silence
continues, deep and neutral,
as I stand there, loving you.

TRANSITION And if love . . . . no not love . . . . sorrow could be personified, this is what she would be.

Love Sorrow
Love sorrow. She is yours now, and you must
take care of what has been
given. Brush her hair, help her
into her little coat, hold her hand,
especially when crossing a street. For, think,

what if you should lose her? Then you would be sorrow yourself; her drawn face, her sleeplessness would be yours. Take care, touch her forehead that she feel herself not so

utterly alone. And smile, that she does not
altogether forget the world before the lesson.
Have patience in abundance. And do not
ever lie or ever leave her even for a moment

by herself, which is to say, possibly, again,
abandoned. She is strange, mute, difficult,
sometimes unmanageable but, remember, she is a child.
And amazing things can happen. And you may see,

as the two of you go
walking together in the morning light, how
little by little she relaxes; she looks about her;
she begins to grow.

TRANSITION And as sorrow grows, Oliver believe there are three important thing that you must be able to do: love, hold on and let go . . .

In Blackwater Woods

Look, the trees
are turning
their own bodies
into pillars

of light,
are giving off the rich
fragrance of cinnamon
and fulfillment,

the long tapers
of cattails
are bursting and floating away over
the blue shoulders

of the ponds,
and every pond,
no matter what its
name is, is

nameless now.
Every year
everything
I have ever learned

in my lifetime leads back to this: the fires and the black river of loss whose other side

is salvation,
whose meaning
none of us will ever know.
To live in this world

you must be able
to do three things:
to love what is mortal;
to hold it

against your bones knowing your own life depends on it;

and, when the time comes to let it go,

to let it go.

TRANSITION In 2012 grief and loss came even closer to home for Oliver who was diagnosed with lung cancer. "The Fourth Sign of the Zodiac" is a four-part poem that recalls the shadowy underworld of loss and survival. And yet, grief is coupled with a hopefulness. The poem is petitionary, asking of us to make what we can of the time we have left.

The Fourth Sign of the Zodiac

1.

Why should I have been surprised?

Hunters walk the forest

without a sound.

The hunter, strapped to his rifle,
the fox on his feet of silk,
the serpent on his empire of muscles—
all move in a stillness,
hungry, careful, intent.
Just as the cancer
entered the forest of my body,
without a sound.

2.
The question is,
what will it be like
after the last day?
Will I float
into the sky
or will I fray
within the earth or a river—
remembering nothing?
How desperate I would be
if I couldn't remember
the sun rising, if I couldn't
remember trees, rivers; if I couldn't
even remember, beloved,
your beloved name.

3. I know, you never intended to be in this world. But you're in it all the same.

so why not get started immediately.

I mean, belonging to it. There is so much to admire, to weep over.

And to write music or poems about.

Bless the feet that take you to and fro.
Bless the eyes and the listening ears.
Bless the tongue, the marvel of taste.
Bless touching.

You could live a hundred years, it's happened. Or not. I am speaking from the fortunate platform of many years, none of which, I think, I ever wasted.

Do you need a prod? Do you need a little darkness to get you going? Let me be urgent as a knife, then, and remind you of Keats, so single of purpose and thinking, for a while, he had a lifetime.

4.
Late yesterday afternoon, in the heat,
all the fragile blue flowers in bloom
in the shrubs in the yard next door had
tumbled from the shrubs and lay
wrinkled and fading in the grass. But
this morning the shrubs were full of
the blue flowers again. There wasn't
a single one on the grass. How, I
wondered, did they roll back up to
the branches, that fiercely wanting,
as we all do, just a little more of
life?
```

---

## IC-1647: On Being Transgender

- Title: On Being Transgender
- Author (byline): Ethan Smith and Miles Walser
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1631
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ethan Smith quoted in text by Diana Bruk
Magazine: Seventeen Magazine (on-line version)
ISBN: Digital Magazine
Publisher: Hearts Magazines
Date (Month/Year): June 11, 2015
https://www.seventeen.com/life/news/a31575/a-letter-
to-the-girl-i-used-to-be/
For Nebraska and We Eat an Apple in My Bed
Author: Miles Walser
Book: What the Night Demands
ISBN: 978-1938912160
Publisher: Write Bloody Publishing
Date (Month/Year): April 25, 2013
Author: Miles Walser quoted in Real Gender: Identity,
Loss and the Capacity to Feel Real by Hannah
Wallerstein, PhD
Journal: Studies in Gender and Sexuality, Volume 18,
2017 – Issue 1 (End of article – on page 62-71)
ISSN: 15240657
Publisher: Taylor & Francis (Routledge)
Date (Month/Year): Published online Nov 30, 2016
https://www.tandfonline.com/doi/abs/10.1080/1524065
7.2016.1238684?src=recsys&journalCode=hsgs20
```

### Introduction (context only: never use it for content warnings)

```text
Ethan Smith, born Emily Smith and Miles Walser, born Lillian Olivia Walser are two talented spoken-word poets who are both dealing with the same issue: living the life of a transgender male. Imagine being born into a body that feels alien to you. Imagine struggling every day to pretend to be something your body says you are, but your mind says you’re not.

Acceptance of people regardless of race, religion, country of origin or even gender identification has been and still is a series of small but steady steps. Listen to the emotions trapped inside two amazing people. We begin with Ethan Smith’s “Letter to the Girl I Used to Be.”
```

### Performance text (classify this)

```text
A Letter to the Girl I Used to Be by Ethan Smith

Dear Emily, Every time I watch baseball, a voice I no longer

recognize whispers: "Ethan, do you remember when you were going to be

the first girl
To play in the major league Seattle mariners rally cap?"
But to be honest, Emily, I don't.
Dad told me that like it was someone else's bedtime

story But I do know you had that drive . . .

The year you turned 11 Was the first time you said out loud that you didn't

want to live anymore
In therapy you said you wouldn't make it to 21.
On my 21st birthday I thought about you.
You were right.
At 19 you started to fade.
I tried to cross you out like a line in my memoir
I wished I could erase completely
And maybe I'm misunderstanding the definition of

death,
But even though parts of you still exist,
You are not here.
Most of my friends have never heard your name
until now.

I've been trying to write this letter for 6 months. I still can't decide if it should be an apology or not. But now you will never hear "Emily Smith" announced

at a college graduation Get married, give birth. When the prescribed testosterone started taking

effect,
my body stopped producing the potential for new life.
Every month I thought about your children,
how I wanted them too.
I let a doctor remove your breasts so I could stand up

straighter Now, even if I somehow had those children, I wouldn't

be able to nourish them My body is obsolete Scarred cosmetic, but never C-section.

I was 4 days late
They will never be grandparents
I was 2 weeks late
They will never learn to jump rope
I was 3 weeks late
They will never shout "Watch mummy, watch me on the

slide" I was 2 months late A piece of us will never wrap their arms around our legs

for comfort Just to keep them from falling down.

And I am sorry that this process is so slow, and all you

can do is wonder if you ever had a place.
You did.
You still do.
Don't forget that

Yours, Ethan P.S. I never hated you

TRANSITION

An apology to yourself for accepting your gender identity – Just imagine. But it’s even more than that . . . with personal anguish comes pressure from society as well. The fear of acceptance. The fear for your personal safety. Nebraska by Miles Walser

Nebraska by Miles Walser

For years you cut your hair short, lowered your voice,
collected ace bandages and baggy clothes.
Small town talk stuck to your shoulders,
you nervously shuffled around gas stations,
never looked men in the eyes.
We share unwanted wombs.
While mine collects cobwebs,
yours lies in a coffin in Nebraska.

This is the state that made you famous,
handed movie scripts to Hilary Swank.
Your murder was Oscar worthy.
We are walking obituaries.
Your hate crime headline already
carved across my forehead.

Brother, I’m afraid to use the bathroom…
(Walk in, head down, don’t look at another guy.)
I’m afraid I’ll be discovered…
(Don’t talk, don’t stare.)
Some thick armed man will call me a queer,
tell me to show him my . . . .
Suddenly I’m thrown against faucets,
spit in my face, work boot gutting my stomach.
I see you on the movie screen
and wonder if it’s my reflection.
I watch them push you into the dirt
and drag me into their car
as they break our bodies in between our thighs.

Brother, did it hurt when you kissed her goodbye? Did you know you were breaking your promise when you told her you’d come back? Did your parents panic? Buy you a prom dress?

Struggle over pronouns at family gatherings?
And how long did it take your girlfriend
to run her hands along your skin, soft as hers?
Did she leave her eyes open?

We are carcasses.
We are public secrets,
playground jokes, and horror films.
We are costumes, stuffing, binding and makeup.
We aren’t real men to them.
Invisible ‘til we’re screaming.
They don’t remember our names
until they read them on our tombstones.

They exposed you.
Decided you’re better off as
splattered ink on newspaper.
Used you as a warning for the rest of us.
And there are days when it works.
Sometimes . . .
I forget that sidewalks can be safe.
Sometimes . . .
I confuse their shooting eyes for the bullet that met

yours.
Sometimes . . .
I imagine the phone call my mother would get.
Can almost hear my sobbing friends.

Smell the lilies on my casket. But brother, I am trying to be brave.

TRANSITION

Miles dedicated that poem to Brandon Teena, a transman who was raped and murdered in Humboldt, Nebraska along with two others.

So if you survive the personal anguish and aren’t attacked by society – what comes next? A relationship . . . love . . . again, the prospects are difficult, to say the least – We Eat an Apple in My Bed by Miles Walser

We Eat an Apple in My Bed by Miles Walser

We’ve been kissing for months.
Three times a week our toothbrushes
share a chipped porcelain mug in my bathroom.
As my lips reach for the juice falling from her laugh,
her mom calls.
I listen as she talks about Biology, her new job,
asks about her sister.
Her eyes drop as she whispers,

No, I still don’t have a boyfriend.
On cue, I stop chewing.
She looks at me, waiting for my face to flush,
for me to tear from the bed,
but I won’t get mad at her.
She shouldn’t have to explain
why we can’t go swimming in public,
why I don’t own a razor,
why she doesn’t need to buy birth control.
She hangs up the phone; I pick up the fruit,
tell her

Apparently, there’s a tiny amount of cyanide in

apple seeds.
She shrugs, says she can handle a little danger,
but I’ve studied how her dimples disappear
when she lies,
and I know she’s thinking about a man
she could parade around her family,
who could kiss her scratchy with stubble.
The kind of man I’ll never be.

She squeezes my hand in the movie theater dark
but tosses it to the side in front of her friends.
Says she just needs time.
She walks on the sidewalk.
I walk in the street.
She closes the door.
I kiss it goodnight.
She goes home for Thanksgiving.
I promise not to call.

If I were a postcard, she could hide me in her pocket. If I were clay, she could mold my body

into something easier to love.

She kisses down my neck,
my peel hiding the rotten fruit inside me.
As I tell her about the cyanide,
her head resting on my chest,
she talks about cider, autumn pies.
See, she says, Apples are harmless.

But she saves the last bites for me, scared to let her lips wander too close to the core.

TRANSITION

Unlike our first author who mourns the loss of motherhood . . . Miles Walser looks to a future when he will one day become a dad. Lillian by Miles Walser Lillian by Miles Walser

I will name you Lillian
because to me it sounds like running through a garden
and with every step you take in life
I want you to feel as beautiful as the flower I’ll call you.
And don’t worry about your mother:
whenever I meet her,
I’ll convince her I deserve naming rights.

But more importantly, Lillian,
you will inherit from me the one thing
the world will let me give you.
I can’t hand you my curly hair or blue eyes,
so you will have the name that has followed me
from birth certificate to driver’s license to passport,
all the while knowing it was never really mine.

Your middle name will be Olivia. For years I hated the name; it burned through the paper of any official document I

filled out, seared my ears when it escaped the tongue of a

stranger, and annihilated my entire body anytime I had to incorrectly introduce myself.

But Lillian, I understand what happened now. See, I am just the middleman; the accidental address on

the package. The name was given to me, to hold onto for you, my future daughter.

For you I keep it safe, protected from people who gawk at me, not understanding why my short hair and masculine

appearance can’t match the sweet femininity in the name. Or people who do understand and hate me for it, attacking the way I bypass the barrier of biological sex because I know that what I feel is more important than what I see in the mirror. And people who think I should conform to the name I

was given,
ignoring everything I know about myself,
the same people who will someday hate our family
because of me.

But through it all, Lillian,
always remember that I love you.
I’ve never met you,
but I love you.
My future daughter.

So I hold the name under my shirt, against my chest, and with every heartbeat the syllables provide me a new sense of rhythmic direction. Because I know I’m moving towards you.

The name Olivia no longer hides in the back of my throat
but floats off my tongue.
A promise of beauty; a promise of purpose.
A promise of you,
my future daughter.

Someday, Lillian Olivia, after you’ve mastered the art of

the two-wheeled bike, I’ll take you to the top of the tallest hill in town and we’ll

soar down,
secretly wishing we could take off into the rushing wind
and at the bottom I’ll tell you that
that feeling was how your father felt,
knowing someday, you’d be in his world.
And he’d finally get to give you your name.
```

---

## IC-1648: On Childhood – A Collection

- Title: On Childhood – A Collection
- Author (byline): Billy Collins, Fanny Howe and Bassey Ikpi
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 984
- Already set (do not supply): none

### Source block (context only)

```text
Author: Billy Collins
Book: The Art of Drowning, Pg 48
ISBN: 978-0822955672
Publisher: University of Pittsburgh Press
Date (Month/Year): June 1995
Author: Fanny Howe
Book: Poetry Magazine
ASIN: B00006KT0A
Publisher: Poetry Foundation
Date (Month/Year): September 2013
Can purchase hard copy on-line at
https://pty.pcdfusion.com/pcd/ShoppingCart/store/30/Prod
uct/ZPTY%201308
Poem can be found on-line at
https://www.poetryfoundation.org/poetrymagazine/art
icles/70043/second-childhood
Author: Bassey Ikpi
Book: Spoken Word – Def Poetry Jam Season 2,
Episode 3
ASIN: B0007GP5WA
Publisher: HBO Studios (DVD Format)
Date (Month/Year): 2003
Printed poem can be found on-line at
https://badilishapoetry.com/bassey-ikpi/
```

### Introduction (context only: never use it for content warnings)

```text
I’m struggling with the idea of growing up. I remember sitting at my desk, working on an AP English essay and being overwhelmed with a sense of grief and terror that my childhood was ending. I am growing up . . . how terrifying! I looked around at my classmates and could see them all – colorful plastic barrettes, ponies on our t-shirts and gaps in our smiles that were rewarded by a visit from the tooth fairy. We loved to play tag; we loved to giggle and imagine. Now it’s almost time to take our first solo plunges into adulthood. And I imagine a life without tag, without giggles; A life where reality slowly stamps out imagination. Am I ready?

On Childhood – A Collection by Billy Collins, Fanny Howe
```

### Performance text (classify this)

```text
On Turning Ten by Billy Collins

(Pg 48) The whole idea of it makes me feel
like I'm coming down with something,
something worse than any stomachache
or the headaches I get from reading in bad light -
a kind of measles of the spirit,
a mumps of the psyche,
a disfiguring chicken pox of the soul.

You tell me it is too early to be looking back,
but that is because you have forgotten
the perfect simplicity of being one
and the beautiful complexity introduced by two.
But I can lie on my bed and remember every digit.
At four I was an Arabian wizard.
I could make myself invisible
by drinking a glass of milk a certain way.
At seven I was a soldier, at nine a prince.

and Bassey Ikpi

At four I was an Arabian wizard.
I could make myself invisible
by drinking a glass of milk a certain way.
At seven I was a soldier, at nine a prince.

But now I am mostly at the window
watching the late afternoon light.
Back then it never fell so solemnly
against the side of my tree house,
and my bicycle never leaned against the garage
as it does today,
all the dark blue speed drained out of it.

This is the beginning of sadness, I say to myself, as I walk through the universe in my sneakers. It is time to say good-bye to my imaginary friends, time to turn the first big number.

It seems only yesterday I used to believe
there was nothing under my skin but light.
If you cut me I would shine.
But now if I fall upon the sidewalks of life,
I skin my knees. I bleed.

Second Childhood by Fanny Howe

I have a fairy rosary called Silver who answers questions when I dangle her in the sun at the window. So I have asked her if I have a big ego and she swings from side to side to say no.

We have other children for friends.

We don’t understand why we are here in the world with horrible grown-ups or what the lessons are that we’re supposed to learn.

It’s not helpful for us to hear ourselves described in religious, geriatric or psychological terms, because we don’t remember what they mean.

One cruel female said, “Don’t laugh so much. You’re not a child.”

My cheeks burned and my eyes grew hot.

I decided to stop becoming an adult. That day I chose to blur facts, fail at tests, and slouch under a hood. School was my first testing ground. I misunderstood lessons, assignments, meanings of poems and stories, and misinterpreted the gestures of characters in novels. I was awestruck by geology but mixed up the ages of rocks. I stared and giggled and refused to take orders and was punished.

Throughout my life I have remained vague and have accepted the humiliation it brought, almost as if stupefaction were a gift. I willfully repeat my mistakes over and over and never learn from experience.

Every day has been a threat to this attitude, so I avoid obligations. For example, last night I dreamed I was on an airplane that was open to the sky and a storm was coming from a hive of stars, and I wanted to sit beside my daughter to watch the wind as we strapped ourselves tight to the invisible seats and stayed awake. If we had been grown-ups, we wouldn’t have been able to see the stars or the storm. We would have perished.

So my commitment to childhood has once again been affirmed.

You might think I am just old, but I have finally decided to make the decision to never grow up and remain under my hood.

Sometimes Silence is the Loudest Kind of Noise by Bassey Ikpi

Sometimes silence is the loudest kind of noise
Like sometimes it was best when
Girls were girls and boys were boys.
Like back when freeze tag was a mating dance.
Like back when “Do Over” meant you got another chance.
Like back when anxiety was worrying if Wonder Woman

would make it out alive. Like back when freedom was sliding backwards on a slide. Like back when success was jumping off a swing and Landing on your feet, then Doing it all over again. Like new shoes made you run faster. Like getting Ms. Gross again for math was a disaster. Like failure was a word we hadn’t even learned to spell yet. Like promises were sealed and kept with pinky bets. Like a challenge was a double dare. Like ugly was a cock-eyed stare.

And you liked it…
Like when you flipped your eyelids inside out
To impress that boy across the room,
‘Cause that’s all it took.
And there was no such thing as too soon,
As long as you checked the right box in that note from

across the room,
The one that he…passed her.
Back when, “I don’t know, maybe” was a legitimate answer.
Back when, “I need space” meant he needed more elbow

room to draw,
So he got on the floor and he colored outside the lines.
Like the lines of color were on the floor,
So we just existed in sandboxes and playgrounds.
And we hop-scotched and dodgeballed
And everything I needed to know, I learned in a shopping

mall.
Like don’t wander off on your own,
Like know who you are,
Like know where you came from,
Like never let go of your mother’s hand no matter what you

do, Like if you get lost, just stand there until someone finds

you,
And someone will always look for you
Because someone will always miss you
And someone will always find you
And when you cry, someone will always remind you
In that quiet, quiet lullaby voice,
That sometimes silence is the loudest kind of noise.
```

---

## IC-1649: On the Pulse of a Brave and Startling Truth

- Title: On the Pulse of a Brave and Startling Truth
- Author (byline): Maya Angelou
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1341
- Already set (do not supply): none

### Source block (context only)

```text
Author: Maya Angelou
ISBN: 978-0679748380
Publisher: Random House
Date (Month/Year): Feb 1993
Author: Maya Angelou
ISBN: 978-0679449041
Publisher: Random House
Date (Month/Year): Sept 1995
```

### Introduction (context only: never use it for content warnings)

```text
Delivered in 1993 at the Inauguration of President Clinton, “On the Pulse of Morning,” Maya Angelou’s poetic wake-up call, is as relevant today as it was 30 years ago.

Through the timeless voices of nature -- a Rock, a River and a Tree -- Americans are held accountable for our actions. For the inhumane choices we make against one another in the name of dominance, gold, land, religion. Choices we make against nature in the name of progress.

When will we learn? When will we turn away from war, competition, and greed and towards unity -- everyone working together for the well-being of all? For it is only through taking responsibility for the earth and its inhabitants that humankind will be able to build a harmonious, inclusive, and enduring future.

On the Pulse of a Brave and Startling Truth – A Compilation by Maya Angelou
```

### Performance text (classify this)

```text
On the Pulse of Morning

A Rock, A River, A Tree
Hosts to species long since departed,
Marked the mastodon.
The dinosaur, who left dried tokens
Of their sojourn here
On our planet floor,
Any broad alarm of their of their hastening doom
Is lost in the gloom of dust and ages.

But today, the Rock cries out to us, clearly, forcefully,
Come, you may stand upon my
Back and face your distant destiny,
But seek no haven in my shadow.
I will give you no hiding place down here.

You, created only a little lower than
The angels, have crouched too long in
The bruising darkness,
Have lain too long
Face down in ignorance.
Your mouths spelling words

Armed for slaughter. The rock cries out today, you may stand on me, But do not hide your face.

Across the wall of the world, A River sings a beautiful song, It says, Come, rest here by my side.

Each of you, a bordered country,
Delicate and strangely made proud,
Yet thrusting perpetually under siege.
Your armed struggles for profit
Have left collars of waste upon
My shore, currents of debris upon my breast.
Yet today I call you to my riverside,
If you will study war no more. Come,
Clad in peace, and I will sing the songs
The Creator gave to me when I and the
Tree and the Rock were one.
Before cynicism was a bloody sear across your
Brow and when you yet knew you still
Knew nothing.
The River sang and sings on.

There is a true yearning to respond to
The singing River and the wise Rock.
So say the Asian, the Hispanic, the Jew,
The African, the Native American, the Sioux,
The Catholic, the Muslim, the French, the Greek,
The Irish, the Rabbi, the Priest, the Sheikh,
The Gay, the Straight, the Preacher,
The privileged, the homeless, the Teacher.
They hear. They all hear
The speaking of the Tree.

They hear the first and last of every Tree Speak to humankind today. Come to me, here beside the

River. Plant yourself beside the River.

Each of you, descendant of some passed
On traveller, has been paid for.
You, who gave me my first name, you,
Pawnee, Apache, Seneca, you
Cherokee Nation, who rested with me, then
Forced on bloody feet,
Left me to the employment of
Other seekers -- desperate for gain,
Starving for gold.
You, the Turk, the Arab, the Swede, the German, the

Eskimo, the Scot,
You the Ashanti, the Yoruba, the Kru, bought,
Sold, stolen, arriving on the nightmare
Praying for a dream.
Here, root yourselves beside me.
I am the Tree planted by the River,
Which will not be moved.
I, the Rock, I the River, I the Tree
I am yours -- your passages have been paid.
Lift up your faces, you have a piercing need
For this bright morning dawning for you.
History, despite its wrenching pain,
Cannot be unlived, and if faced
With courage, need not be lived again.

Lift up your eyes upon
The day breaking for you.
Give birth again
To the dream.

Women, children, men,
Take it into the palms of your hands.
Mold it into the shape of your most
Private need. Sculpt it into
The image of your most public self.
Lift up your hearts.
Each new hour holds new chances
For a new beginning.
Do not be wedded forever
To fear, yoked eternally
To brutishness.

The horizon leans forward,
Offering you space to place new steps of change.
Here, on the pulse of this fine day
You may have the courage
To look up and out and upon me, the
Rock, the River, the Tree, your country.
No less to Midas than the mendicant.
No less to you now than the mastodon then.

Here on the pulse of this new day
You may have the grace to look up and out
And into your sister's eyes, and Into
Your brother's face, your country
And say simply
Very simply
With hope --
Good morning.

[performed in a collection (see Speaking Truth – A

Collection stored in the VAULT)]

TRANSITION Maya Angelou writes the kind of poetry that heals, that inspires, that uplifts every person who reads or hears it. We all have the power in our hands to bring good to the world instead of violence and suffering. Written and delivered in honor of the 50th anniversary of the United Nations; “A Brave and Startling Truth” is dedicated to the hope for peace, which lies, sometimes hidden, in every heart. We all are “the possible,” and that is the "brave and startling truth." The moment when we realize, that as a committed group of leaders with courage and integrity, each and every one of us can do something to build the world we wish to see.

A Brave and Startling Truth

We, this people, on a small and lonely planet
Traveling through casual space
Past aloof stars, across the way of indifferent suns
To a destination where all signs tell us
It is possible and imperative that we learn
A brave and startling truth

And when we come to it
To the day of peacemaking
When we release our fingers
From fists of hostility
And allow the pure air to cool our palms

When we come to it When the curtain falls on the minstrel show of hate And faces sooted with scorn are scrubbed clean When battlefields and coliseum No longer rake our unique and particular sons and

daughters Up with the bruised and bloody grass To lie in identical plots in foreign soil

When the rapacious storming of the churches The screaming racket in the temples have ceased When the pennants are waving gaily When the banners of the world tremble Stoutly in the good, clean breeze

When we come to it
When we let the rifles fall from our shoulders
And children dress their dolls in flags of truce
When land mines of death have been removed
And the aged can walk into evenings of peace
When religious ritual is not perfumed
By the incense of burning flesh
And childhood dreams are not kicked awake
By nightmares of abuse

When we come to it
Then we will confess that not the Pyramids
With their stones set in mysterious perfection
Nor the Gardens of Babylon
Hanging as eternal beauty
In our collective memory
Not the Grand Canyon
Kindled into delicious color
By Western sunsets

Nor the Danube, flowing its blue soul into Europe
Not the sacred peak of Mount Fuji
Stretching to the Rising Sun
Neither Father Amazon nor Mother Mississippi who,

without favor,
Nurture all creatures in the depths and on the shores
These are not the only wonders of the world
When we come to it
We, this people, on this minuscule and kithless globe
Who reach daily for the bomb, the blade and the dagger
Yet who petition in the dark for tokens of peace
We, this people on this mote of matter
In whose mouths abide cankerous words
Which challenge our very existence
Yet out of those same mouths
Come songs of such exquisite sweetness
That the heart falters in its labor
And the body is quieted into awe

We, this people, on this small and drifting planet
Whose hands can strike with such abandon
That in a twinkling, life is sapped from the living
Yet those same hands can touch with such healing,
irresistible tenderness
That the haughty neck is happy to bow
And the proud back is glad to bend
Out of such chaos, of such contradiction
We learn that we are neither devils nor divines
When we come to it
We, this people, on this wayward, floating body
Created on this earth, of this earth
Have the power to fashion for this earth
A climate where every man and every woman
Can live freely without sanctimonious piety
Without crippling fear

When we come to it
We must confess that we are the possible
We are the miraculous, the true wonder of this world
That is when, and only when
We come to it.

[performed in a collection (see “When We Come to It, We Must Do Something” stored in the VAULT)]
```

---

## IC-1650: Orlando

- Title: Orlando
- Author (byline): Andrea Gibson
- Work: Lord of the Butterflies, Pg 11-15
- Publisher: Button Poetry
- Publication date as stated: Nov 2018
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 624
- Already set (do not supply): none

### Source block (context only)

```text
Author: Andrea Gibson
Book: Lord of the Butterflies, Pg 11-15
ISBN: 978-1943735426
Publisher: Button Poetry
Date (Month/Year): Nov 2018
```

### Introduction (context only: never use it for content warnings)

```text
June 12, 2016. Saturday night was Latin Night at Pulse, one of Orlando, Florida’s best-known gay clubs. The place was packed with patrons both gay and straight, young and not-so-young, from the U.S., Puerto Rico, the Dominican Republic, Mexico and elsewhere. Everyone was having a good time, dancing salsa and bachata until 2:02 am when all hell broke loose. When the dust settled, 49 people were confirmed dead and 53 others injured it what was, at the time, the deadliest mass shooting in US history. The deadliest until the following October when shots rang out again at a music festival in Las Vegas, Nevada.

Orlando by Andrea Gibson
```

### Performance text (classify this)

```text
(Pg 11-15) When the first responders entered the Pulse nightclub after the massacre in Orlando, they walked through the horrific scene of bodies and called out, "If you are alive, raise your hand."

I was sleeping in a hotel
in the Midwest at the time,
but I imagine in that exact moment,
my hand twitched in my sleep,
some unconscious part of me aware
that I had a pulse
that I was alive . . . .

(con’t) . . . The next day I woke to the news
that an assault rifle had fired
202 bullets through a gay bar
on Latin night in one of the worst
massacres in US history -- a massacre
of people who did not leave the dance floor
when they heard gunshots
because they thought
they were just the beats
of the song.

Everyone around me spent
that day grieving and every tear
tasted like dance sweat
drying in the morgue.

Later that night
I was performing for an audience
that had spent two hours in line
waiting to get through bag checks
and metal detectors. On stage
I couldn't keep my hand
from covering

my heart. Kept searching the club for the fastest route to every exit. I knew the person working security was in a text war and wasn't keeping his eyes on the door; I knew there was a man in the fifth row picking at the seams of a red duffel bag.

Every few seconds
I’d eye the balcony
for the glint
of whatever might aim
to tear the bodies
off the boys holding hands
or the girls with the haircuts short
as my temper when rage
is a decibel I can actually get to
when I not just frozen
and grief-sick watching history

not be history, watching
the music not be music, knowing
someone having the best night of her life
shouted, This is my favorite song,
and then a drumbeat lifted

a rifle over a bathroom stall
and emptied a magazine
into the kidneys of a grown man
texting, Mommy I'm going to die,
his handprints in blood
on the walls, reaching

for people
dying in the fetal position.
People covered in their friend's blood,
crying too hard to hide
from their own deaths,
people outside pushing
bandannas into bullet wounds.

It's true
what they say about the gays
being so fashionable --
our ghosts never go
out of style.

even life is like funeral practice:
half of us already dead
to our families before we die.
half of us on our knees
trying to crawl
into the family photo.

That night on stage I kept remembering being fifteen at Disney World wearing my best friend's hoodie

like it was my boyfriend's class ring.

How many years it took me
to just touch her face.
how many years of praying
my heart could play dead
until the threat was gone
until the world changed

until history was history,
but history just keeps coming
for the high, keeps shooting up
bodies, keeps drumming up reasons

to have metal detectors
at poetry readings
where the poems feel
like unanswered calls
to people who claim their god
or their apathy, is unwilling
to accept the charges.

Dear god, how broke
do you have to be
to not buy people time
to get out the door
when the song
goes to f****** hell?

When this world, drunk
on hate, decides blood
is wine and drinks its fill
in the only place
they ever thought was safe?
In the only place they thought
they didn’t have to hide?

In the only place they were wanted
because of who they loved
and how they loved
and how they loved
until someone walked through their bodies
and asked who was still alive
and hardly anyone
put their hand up.
```

---

## IC-1651: Outside Ourselves (collection)

- Title: Outside Ourselves (collection)
- Author (byline): Michael Jackson/Lionel Richie; Audre
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1276
- Already set (do not supply): none

### Source block (context only)

```text
Author: Michael Jackson and Lionel Richie
ASIN: B003YP5D78
Publisher: Warner Bros. Publications Inc.
Date (Month/Year): 1985
Author: Audre Lorde
Book: The Black Unicorn
ISBN: 978-0393312379
Publisher: W.W. Norton and Company
Date (Month/Year): Aug 1995
Author: Adrienne Rich
Book: The Fact of a Doorframe
ISBN: 978-0393323955
Publisher: W.W. Norton and Company
Date (Month/Year): Nov 2002
Author: Pablo Neruda
Book: Extravagaria: A Bilingual Edition
ISBN: 9780374512385
Publisher: Noonday Press
Date (Month/Year): January 2001
```

### Introduction (context only: never use it for content warnings)

```text
Over 30 years ago, more than 40 recording artists gathered to record these lyrics by Lionel Richie and Michael Jackson. Their goal: to raise awareness of widespread, life-threatening poverty in Africa. Over $75 million was raised to fight poverty on the continent. And for a brief moment the world did come together as one – united behind a cause. But rallies end and people are prone to return to their personal bubbles. This collection of poems considers the human tendency to turn a blind-eye to the plight of others. Fear, lack of knowledge, being too busy . . . . the reasons are endless. But the fact remains, the plight of the world will never change unless we all are willing to step . . . Outside Ourselves (a collection)
```

### Performance text (classify this)

```text
Lorde, Adrienne Rich and Pablo Neruda

We Are the World
There comes a time when we heed a certain call
When the world must come together as one
There are people dying
And it's time to lend a hand to life
The greatest gift of all

We can't go on pretending day by day
That someone somewhere will soon make a change
We're all a part of God's great big family
And the truth, you know,
Love is all we need

We are the world,
We are the children
We are the ones who make a brighter day
So, let's start giving
There's a choice we're making
We're saving our own lives
It's true we'll make a better day
Just you and me

A Litany for Survival by Audre Lorde

For those of us who live at the shoreline
standing upon the constant edges of decision
crucial and alone
for those of us who cannot indulge
the passing dreams of choice
who love in doorways coming and going
in the hours between dawns
looking inward and outward
at once before and after
seeking a now that can breed
futures
like bread in our children's mouths
so their dreams
will not reflect
the death of ours:

For those of us
who were imprinted with fear
like a faint line in the center of our foreheads
learning to be afraid with our mother's milk
for by this weapon
this illusion of some safety to be found
the heavy-footed hoped to silence us
For all of us
this instant and this triumph
We were never meant to survive.

And when the sun rises we are afraid
it might not remain
when the sun sets we are afraid
it might not rise in the morning
when our stomachs are full we are afraid
of indigestion
when our stomachs are empty we are afraid
we may never eat again
when we are loved we are afraid
love will vanish
when we are alone we are afraid
love will never return
and when we speak we are afraid
our words will not be heard
nor welcomed
but when we are silent
we are still afraid

So it is better to speak remembering we were never meant to survive –

TRANSITION Adrienne Rich in her poem “Hunger” addresses not fear, but the fact that too often we choose to remain unaware of atrocities occurring outside our limited personal world. Without knowledge, just how do you quantify suffering? According to the UN, 21,000 people die every day of hunger or hunger-related causes: One person every four seconds. This poetry selection is ~ 7 minutes long. By the time I am finished 105 people will already have starved to death . . . and sadly, children die most often.

Hunger by Adrienne Rich

1.
A fogged hill-scene on an enormous continent,
intimacy rigged with terrors,
a sequence of blurs the Chinese painter's ink-stick
planned,
a scene of desolation comforted
by two human figures recklessly exposed,
leaning together in a sticklike boat
in the foreground. Maybe we look like this,
I don't know. I'm wondering
whether we even have what we think we have--
lighted windows signifying shelter,
a film of domesticity
over fragile roofs. I know I'm partly somewhere else--
huts strung across a drought-stretched land
not mine, dried breasts, mine and not mine, a mother
watching my children shrink with hunger.
I live in my Western skin,
my Western vision, torn
and flung to what I can't control or even fathom.
Quantify suffering, you could rule the world.

2.
They rule the world while they can persuade us
our pain belongs in some order.
Is death by famine worse than death by suicide,
than a life of famine and suicide, if a black lesbian dies,
if a white prostitute dies, if a woman genius
starves herself to feed others,
self-hatred battening on her body?
Something that kills us or leaves us half-alive
is raging under the name of an "act of god"
in Chad, in Niger, in the Upper Volta--
yes, that male god that acts on us and on our children,
that male State that acts on us and on our children
till our brains are blunted by malnutrition,
yet sharpened by the passion for survival,
our powers expended daily on the struggle
to hand a kind of life on to our children,
to change reality for our lovers
even in a single trembling drop of water.

3.
We can look at each other through both our lifetimes
like those two figures in the sticklike boat
flung together in the Chinese ink-scene;
even our intimacies are rigged with terror.
Quantify suffering? My guilt at least is open,
I stand convicted by all my convictions--
you, too. We shrink from touching
our power, we shrink away, we starve ourselves
and each other, we're scared shitless
of what it could be to take and use our love,
hose it on a city, on a world,
to wield and guide its spray, destroying
poisons, parasites, rats, viruses--
like the terrible mothers we long and dread to be.

4.
The decision to feed the world
is the real decision. No revolution
has chosen it. For that choice requires
that women shall be free.
I choke on the taste of bread in North America
but the taste of hunger in North America
is poisoning me. Yes, I'm alive to write these words,
to leaf through Kollwitz's women
huddling the stricken children into their stricken arms
the "mothers" drained of milk, the "survivors" driven
to self-abortion, self-starvation, to a vision
bitter, concrete, and wordless.
I'm alive to want more than life,
want it for others starving and unborn,
to name the deprivations boring
into my will, my affections, into the brains
of daughters, sisters, lovers caught in the crossfire
of terrorists of the mind.
In the black mirror of the subway window
hangs my own face, hollow with anger and desire.
Swathed in exhaustion, on the trampled newsprint,
a woman shields a dead child from the camera.

The passion to be inscribes her body. Until we find each other, we are alone.

TRANSITION Are you too busy to be aware, to understand, to do something, however small? Pablo Neruda penned a deceptively simple poem about taking the time for a little bit of soul-searching which may help us make peace with ourselves and others.

Keeping Quiet by Pablo Neruda

Now we will count to twelve and we will all keep still.

For once on the face of the earth,
let’s not speak in any language;
let’s stop for one second,
and not move our arms so much.

It would be an exotic moment
without rush, without engines;
we would all be together
in a sudden strangeness.

Fisherman in the cold sea
would not harm whales
and the man gathering salt
would not look at his hurt hands.

Those who prepare green wars, wars with gas, wars with fire, victories with no survivors, would put on clean clothes and walk about with their brothers in the shade, doing nothing.

What I want should not be confused
with total inactivity.
Life is what it is about;
I want no truck with death.

If we were not so single-minded
about keeping our lives moving,
and for once could do nothing,
perhaps a huge silence
might interrupt this sadness
of never understanding ourselves
and of threatening ourselves with death.
Perhaps the earth can teach us
as when everything seems dead
and later proves to be alive.

Now I’ll count up to twelve and you keep quiet and I will go.

1 . . . 2 . . . 3 . . . 4 . . . 5 . . .
```

---

## IC-1652: Pachyderm

- Title: Pachyderm
- Author (byline): Sherman Alexie
- Work: The Best American Poetry 2013
- Publisher: Scribner
- Publication date as stated: September 2013
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1135
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sherman Alexie
Book: The Best American Poetry 2013
ISBN: 978-1476708133
Publisher: Scribner
Date (Month/Year): September 2013
```

### Introduction (context only: never use it for content warnings)

```text
There was a National Geographic documentary about elephants that included a scene of a mother elephant coming upon a dead elephant’s bones. The mother elephant carefully touched the bones with her trunk. She seemed to be mourning the loss of another elephant. It was devastating.

Then I watched a CNN story about an Iraqi War veteran who’d lost both of his legs to an improvised explosive device – an IED. He was confident in his ability to rehab successfully, but there was also an undercurrent of anger.

“The mourning elephant and wounded soldier merged in my mind. And that’s where ‘Pachyderm’ had its origins.” This is how author Sherman Alexie explains the inspiration for his poem Pachyderm
```

### Performance text (classify this)

```text
1. Sheldon decided he was an elephant. 2. Everywhere he went, he wore a gray t-shirt, gray

sweat pants, and gray basketball shoes. 3. He also carried a brass trumpet that he’d painted

white.

4. Sometimes he used that trumpet as a tusk. 5. Then he’d use it as the other tusk. 6. Sometimes he played that brass trumpet and

pretended it was an elephant trumpet. 7. Every other day, Sheldon charged around the

reservation like he was a bull elephant in musth. 8. Musth being a state of epic sexual arousal. 9. Sheldon would stand in the middle of intersections

and charge at cars. 10. Once, Sheldon head-butted a Toyota Camry so hard

that he knocked himself out. 11. Sheldon’s mother, Agnes, was driving that Camry. 12. Agnes did not believe she was an elephant nor did

she believe she was the mother of an elephant.

13. And Agnes didn’t believe that Sheldon fully

believed he was an elephant until he knocked

himself out on the hood of the Camry. 14. In Africa, poachers kill elephants, saw off the

tusks, and leave the rest of the elephant to rot. 15. Ivory is coveted. 16. Nobody covets Sheldon’s trumpet, not as a trumpet

or tusk. 17. On those days when Sheldon was not a bull

elephant, he was a cow elephant. 18. A cow elephant mourning the death of her baby. 19. In Africa, elephants will return again and again to

the dead body of a beloved elephant. 20. Then, for years afterward, the mournful elephants

will return to the dead elephant’s cairn of bones. 21. They will lift and caress the dead elephant’s ribs.

22. By touch, they remember.
23. Sheldon’s twin brother died in the first Iraq War.
24. 1991.
25. His name was Pete.
26. Sheldon and Pete’s parents were not the kind to

give their twins names that rhymed. 27. In Iraq, an Improvised Explosive Device had

pulverized Pete’s legs, genitals, ribcage, and spine. 28. Sheldon could not serve in the military because he

was blind in his right eye. 29. In 1980, when they were eight, and sword fighting

with tree branches, Pete had accidentally stabbed

Sheldon in the eye. 30. When they were children, Sheldon and Pete often

played war.

31. They never once pretended to be killed by an

Improvised Explosive Device. 32. Only now, in this new era, do children pretend to be

killed by Improvised Explosive Devices.
33. Pete was buried in a white coffin.
34. It wasn’t made of ivory.
35. At the gravesite, Sheldon scooped up a handful of

dirt. 36. He was supposed to toss the dirt onto his brother’s

coffin, as the other mourners had done. 37. But Sheldon kept the dirt in his hand. 38. He made a fist around the dirt and would not let it

go. 39. He believed that his brother’s soul was contained

within that dirt.

40. And if he let go of that dirt, his brother’s soul

would be lost forever. 41. You cannot carry a handful of dirt for any

significant amount of time. 42. And dirt, being clever, will escape through your

fingers.
43. So Sheldon taped his right hand shut.
44. For months, he did everything with his left hand.
45. Then, one night, his right hand began to itch.
46. It burned.
47. Sheldon didn’t want to take off the tape.
48. He didn’t want to lose the dirt.
49. His brother’s soul.
50. But the itch and burn were too powerful.
51. Sheldon scissored the tape off his right hand.

52. His fingers were locked in place from disuse. 53. So he used the fingers of his left hand to pry open

the fingers of his right hand. 54. The dirt was gone. 55. Except for a few grains that had embedded

themselves into his palm. 56. Using those grains of dirt, Sheldon wanted to build

a time machine that would take him and his brother

back into the egg cell they once shared. 57. Until he became an elephant, Sheldon referred to

his left hand as “my hand” and to his right hand as

“my brother’s hand.” 58. Sheldon’s father, Arnold, was paraplegic. 59. His wheelchair was alive with eagle feathers and

beads and otter pelts. 60. In Vietnam, in 1971, Arnold’s lower spine was

shattered by a sniper’s bullet.

61. Above the wound, he was a fancy dancer. 62. Below the wound, he was not. 63. His wife became pregnant with Sheldon and Pete

while Arnold was away at war. 64. Biologically speaking, the twins were not Arnold’s. 65. Biologically speaking, Arnold was a different Arnold

than he’d been before. 66. But, without ever acknowledging the truth, Arnold

raised the boys as if they shared his biology.
67. Above the wound, Arnold is a good man.
68. Below the wound, he is also a good man.
69. Sometimes, out of love for Sheldon and Sheldon’s

grief, Arnold pretended that his wheelchair was an

elephant. 70. And that he was a clown riding the elephant.

71. A circus can be an elephant, another elephant, and a

clown. 72. The question should be, “How many circuses can fit

inside one clown?” 73. There is no such thing as the Elephant Graveyard. 74. That mythical place where all elephants go to die. 75. That place doesn’t exist. 76. But the ghosts of elephants do wear clown makeup. 77. And they all gather in the same place. 78. Inside Sheldon’s ribcage. 79. Sheldon’s heart is a clown car filled with circus

elephants. 80. When elephants mourn, they will walk circles around

a dead elephant’s body. 81. Elephants weep.

82. Jesus wept. 83. Sheldon’s mother, Agnes, wonders if Jesus has

something to do with her son’s elephant delusions. 84. Maybe God is an elephant. 85. Sheldon’s father, Arnold, believes that God is a blue

whale. 86. Some scientists believe that elephants used to be

whales. 87. Sheldon, in his elephant brain, believes that God is

an Improvised Explosive Device.
88. Pete, the dead twin, was not made of ivory.
89. But he is coveted.
90. If Jesus can come back to life then why can’t all of

us come back to life? 91. Aristotle believed that elephants surpassed all

other animals in wit and mind.

92. Nobody ever said that Jesus was funny. 93. Then, one day, Sheldon remembered he was not an

elephant. 94. Instead he decided that Pete was an elephant who

had gone to war.
95. An elephant who died saving his clan and herd.
96. An elephant killed by poachers.
97. Sheldon decided that God was a poacher.
98. Sheldon decided his prayers would become threats.
99. F*** you, God, f** you.
100. Sheldon wept.
101. Then he picked up his trumpet and blew an endless,

harrowing note.
```

---

## IC-1653: Palestinian Poetry Collection

- Title: Palestinian Poetry Collection
- Author (byline): Naomi Shihab Nye and Taha Muhammad Ali
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 949
- Already set (do not supply): none

### Source block (context only)

```text
Author: Naomi Shihab Nye
Book: 19 Varieties of Gazelle
ISBN: 978-0060097653
Publisher: Greenwillow
Date (Month/Year): April 2002
Author: Naomi Shihab Nye
Book: 19 Varieties of Gazelle
ISBN: 978-0060097653
Publisher: Greenwillow
Date (Month/Year): April 2002
Author: Taha Muhammad Ali
Book: Never Mind: Twenty Poems and a Story
translated by Peter Cole, Yahya Hijazi, and Gabriel
Levin
ISBN: 978-9659012527
Publisher: Ibis Editions
Date (Month/Year): Dec 2000
```

### Introduction (context only: never use it for content warnings)

```text
Naomi Shihab Nye was born in St. Louis to an American mother and a Palestinian father, Aziz Shihab, a refugee from the war of 1948. Being American and Palestinian puts her at the confluence of two warring rivers, an uncomfortable position that grew only more painful during Israel's assault on Gaza and Lebanon. All Things Not Considered by Naomi Shihab Nye.
```

### Performance text (classify this)

```text
All Things Not Considered

You cannot stitch the breath back into this boy.

A brother and sister were playing with toys when their room exploded.

In what language is this holy?

The Jewish boys killed in the cave were skipping school, having an adventure.

Asel Asleh, Palestinian, age 17, believed in the field beyond right and wrong where people came together

to talk. He kneeled to help someone else stand up before he was shot.

If this is holy, could we have some new religions please?

Mohammed al-Durra huddled against his father in the street, terrified. The whole world saw him die.

An Arab father on crutches burying his 4 month girl weeps, "I spit in the face of this ugly world."

*

Most of us would take our children over land.
We would walk in the fields forever homeless
with our children,
huddle under cliffs, eat crumbs and berries,
to keep our children.
This is what we say from a distance
because we can say whatever we want.

*

No one was right.
Everyone was wrong.
What if they'd get together
and say that?
At a certain point
the flawed narrator wins.

People made mistakes for decades.
Everyone hurt in similar ways
at different times.
Some picked up guns because guns were given.
If they were holy it was okay to use guns.
Some picked up stones because they had them.
They had millions of them.
They might have picked up turnip roots
or olive pits.
Picking up things to throw and shoot:
at the same time people were studying history,
going to school.

*

The curl of a baby's graceful ear.

The calm of a bucket waiting for water.

Orchards of the old Arab men who knew each tree.

Jewish and Arab women standing silently together.

Generations of black.

Are people the only holy land?

TRANSITION

Where is common sense? Is intensified, extended violence going to help things in the long run? Naomi Shihab Nye denounces the devastating loss of civilian life and infrastructure in Lebanon, and she is grieved by U.S. support for Israel's actions. "It is unfathomable," she says, "that we have people without empathy in positions of power affecting so many innocents." She also has a hard time fathoming the silence in the United States that greeted Israel's war on Lebanon. "It shocks me how many people seem to be able to avoid mentioning 'what goes on' even as it is happening," she says. Jerusalem by Naomi Shihab Nye.

Jerusalem

I'm not interested in
Who suffered the most.
I'm interested in
People getting over it.

Once when my father was a boy
A stone hit him on the head.
Hair would never grow there.
Our fingers found the tender spot
and its riddle: the boy who has fallen
stands up. A bucket of pears
in his mother's doorway welcomes him home.
The pears are not crying.
Later his friend who threw the stone
says he was aiming at a bird.
And my father starts growing wings.

Each carries a tender spot:
something our lives forgot to give us.
A man builds a house and says,
"I am native now."
A woman speaks to a tree in place
of her son. And olives come.
A child's poem says,
"I don't like wars,
they end up with monuments."
He's painting a bird with wings
wide enough to cover two roofs at once.

Why are we so monumentally slow? Soldiers stalk a pharmacy: big guns, little pills. If you tilt your head just slightly it's ridiculous.

There's a place in my brain
Where hate won't grow.
I touch its riddle: wind, and seeds.
Something pokes us as we sleep.

It's late but everything comes next.

TRANSITION

A Palestinian word that best reflects the belief system of its people is not easily translated into English: “Samid” which means one who holds on tenaciously to his land and its culture and perseveres in adverse times. Poet Taha Muhammad embodies this concept in his poem “Thrombosis in the Veins of Petroleum.” Born in 1931 in Galilee village of Saffuriya, he fled to Lebanon, together with most of the inhabitants of his village, during the Arab-Israeli war of 1948. A year later he slipped back across the border with his family and settled in Nazareth, where he has lived ever since.

THROMBOSIS IN THE VEINS OF PETROLEUM

When I was a child
I fell into the abyss
but didn’t die;
I drowned in the pond
when I was young,
but did not die;
and now, God help us—
one of my habits is running
into battalions of land mines
along the border,
as my songs
and the days of my youth
are dispersed:
here a flower,
there a scream;
and yet,
I do not die!
*
They butchered me
on the doorstep
like a lamb for the feast—
thrombosis
in the veins of petroleum;
In God’s name
they slit my throat
from ear to ear
a thousand times,
and each time
my dripping blood would swing
back and forth
like the feet of a man
hanged from a gallows,
and come to rest,
a large, crimson mallow
blossom—
a beacon
to guide ships
and mark
the site of palaces
and embassies.
*
And tomorrow,
God help us—
the phone won’t ring
in a brothel or castle,
and not in a single Gulf Emirate,
except to offer a new prescription
for my extermination.
But …
just as the mallow tells us,
and as the borders know,
I won’t die! I will not die!!
I’ll linger on—a piece of shrapnel
the size of a penknife
lodged in the neck;
I’ll remain—
a blood stain
the size of a cloud
on the shirt of this world!
```

---

## IC-1654: Parents – A Collection

- Title: Parents – A Collection
- Author (byline): Daniel Beaty, Perre Shelton and Sarah Kay
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1497
- Already set (do not supply): none

### Source block (context only)

```text
Author: Daniel Beaty
ISBN: 978-0316209175
Publisher: Little, Brown Books for Young Readers
Date (Month/Year): Dec 2013
Author: Perre Shelton
ISBN: On-line Transcript
https://foxthepoet.blogspot.com/2010/05/dandelion-by-
perre-shelton.html
Publisher: HBO
Date (Month/Year): 2009
Author: Sarah Kay
Book: No Matter the Wreckage, Pg 33-35
ISBN: 978-1938912481
Publisher: Write Bloody Publishing
Date (Month/Year): Mar 2014
```

### Introduction (context only: never use it for content warnings)

```text
When we are children, we think our parents can do no wrong. To most of us, they are superheroes who have the world completely figured out. It’s not until we are older that we realize our parents are just normal people. That’s when relationships with your parents get complicated, whether you are a teenager like me or a fully launched adult with children of your own.

Some of us are grieving for parents who couldn’t be everything we needed as a child – grieving for the relationship we wish we could have had. Some of us have parents who were addicts, abusive, or simply absent.

No matter what type of relationship you have with your parents, I hope you can find some connection with them through these poems: Knock, Knock by Daniel Beaty,
```

### Performance text (classify this)

```text
Dandelion by Perre Shelton and Hands by Sarah Kay

Knock, Knock by Daniel Beaty

As a boy I shared a game with my father.
Played it every morning 'til I was 3.
He would knock knock on my door,
and I'd pretend to be asleep
'til he got right next to the bed,
Then I would get up and jump into his arms.
"Good morning, Papa."
And my papa he would tell me that he loved me.
We shared a game.
Knock Knock
Until that day when the knock never came
and my momma takes me on a ride past corn fields
on this never-ending highway 'til we reach a place of high
rusty gates.
A confused little boy,
I entered the building carried in my mama's arms.
Knock Knock
We reach a room of windows and brown faces
behind one of the windows sits my father.
I jump out of my mama's arms
and run joyously towards my papa
Only to be confronted by this window.
I knock knock trying to break through the glass,
trying to get to my father.

I knock knock as my mama pulls me away
before my papa even says a word.
And for years he has never said a word.
And so twenty-five years later, I write these words
for the little boy in me who still awaits his papa's knock.
Papa, come home 'cause I miss you.
I miss you waking me up in the morning and telling me you
love me.
Papa, come home, 'cause there's things I don't know,
and I thought maybe you could teach me:
How to shave;
how to dribble a ball;
how to talk to a lady;
how to walk like a man.
Papa, come home because I decided a while back
I wanted to be just like you.
but I'm forgetting who you are.
And twenty-five years later a little boy cries,
and so I write these words and try to heal
and try to father myself
and I dream up a father who says the words my father did
not.

Dear Son,
I'm sorry I never came home.
For every lesson I failed to teach, hear these words:
Shave in one direction in strong deliberate strokes to avoid
irritation
Dribble the page with the brilliance of your ballpoint pen.
Walk like a god and your goddess will come to you.
No longer will I be there to knock on your door,
So you must learn to knock for yourself.
Knock knock down doors of racism and poverty that I could
not.
Knock knock down doors of opportunity
for the lost brilliance of the black men who crowd these
cells.
Knock knock with diligence for the sake of your children.
Knock knock for me for as long as you are free,
These prison gates cannot contain my spirit.
The best of me still lives in you.
Knock knock with the knowledge that you are my son, but
you are not my choices.
Yes, we are our fathers' sons and daughters,
But we are not their choices.

For despite their absences we are still here.
Still alive, still breathing
With the power to change this world,
One little boy and girl at a time.
Knock knock
Who's there?
We are.

Dandelion by Perre Shelton

she was never the beautiful, long-haired mother i wrote about in poems she never walked barefoot through forests green blades of grass, sheared a perfect two inches, one blade at a time carpeting the front lawn of her pink and white bungalow. she just wasn’t that lucky.

sunflowers and rose bushes never draped across white picket fences her garden merely yielded curtailed dandelions polka dotted across patches of brown.

she learned to value their beauty because they had such pretty names, "dandelions." however, she, my mother, still dreamt of sunny spring Saturdays drenching her dreams with lemonade stands and sprinklers, heart-shaped bushes and glass Coke bottles, liberty and justice for all. but somehow, somehow she knew better than to dream too unsilently.

as a child she would fill my days with baloney sandwiches and flavored tap water. then, i never understood how hard she tried to keep me happy, and even up until today, i have yet to discover how often she dreams. but somehow, somehow i know it’s always about me and the husband she never had. she was never that medallion-shaped, apron-cloaked mistress moving proud across the wooden floor she dreamt

of
wearing almost perfectly white socks,
stretched disproportionate at the ankles from carrying life
as pure as those damn white walls
she just wasn't that lucky,

but today won’t let her forget. won’t let her sink into an oblivion of white walls and pined floors. an oblivion of finely tuned but extremely rhythmless music. mother, those dandelions are singing to you.

loud, boastful, brilliant.
mother, those dandelions are beautiful.
like you, but like you even they forget.
sorry they couldn’t grow up amongst roses.
sorry they sprang from the cracks,
etched in poverty America.
they grew up among society’s weeds.
the neighborhood hates those dandelions,
the neighborhood wants to kill those dandelions,
but my mother always grows back.
to soak sun and hold it in her cheeks.
thin colored all-brights, brilliant yellow
and that yellow faced dandelion will never die
but she will always dream of something more than those

weeds. until the day she realizes that a flower as beautiful as her does not belong in a rose bush.

Hands by Sarah Kay

(Pg 33-35) People used to tell me that I had beautiful hands.
Told me so often, in fact, that one day I started to
believe them; I started listening. Until I asked my
photographer father, Hey Daddy, could I be a hand model?

To which Dad laughed and said, No way.
I don't remember the reason he gave,
and it probably didn’t matter anyway.
I would have been upset, but there were

far too many crayons to grab, too many
stuffed animals to hold, too many ponytails to tie,
too many homework assignments to write,
too many boys to wave at, too many years to grow.

We used to have a game, my dad and I, about holding hands. We held hands everywhere. In the car, on the bus, on the street, at a movie. And every time either he or I would whisper a great big number to the other, pretending that we were

keeping track of how many times we had held hands,
that we were sure this one had to be eight-million,
two-thousand, seven-hundred and fifty-three.
Hands learn. More than minds do.

Hands learn to hold other hands.
How to grip pencils and mold poetry.
How to memorize computer keys
and telephone buttons in the dark.

How to tickle pianos and grip bicycle handles.
How to dribble a basketball and how to peel apart
pages of Sunday comics that somehow always seem to stick
together.
They learn how to touch old people and how to hold babies.

I love hands like I love people. They are the maps and compasses with which we navigate our way through life, feeling out way over mountains passed and valleys crossed; they are our histories.

Some people read palms to tell you your future,
but I read hands to tell your past.
Each scar marks a story worth telling. Each callused palm,
each cracked knuckle, is a broken bottle, a missed punch,

a rusty nail, years in a factory.
Now, I watch Middle Eastern hands
clenched in Middle Eastern fists.
Pounding against each other like war drums,
each country sees their fists as warriors,
and others as enemies, even if fists alone are only hands.
But this is not a poem about politics; hands are not about
politics.
This is a poem about love.

And fingers. Fingers interlocked like a beautiful accordion of flesh or a zipper of prayer. One time, I grabbed my dad's hand so that our fingers interlocked perfectly, but he changed his position, saying, No, that hand-hold is for your mom.

Kids high five, sounds of hand-to-hand combat
instead mark camaraderie and teamwork.
Now, grown up, we learn to shake hands.
You need a firm handshake, but not too tight, don’t be limp now,

don't drop too soon, but for God’s sake don't hold on too long.
but . . . hands are not about politics?
When did it become so complicated?
I always thought it simple.

The other day, my dad looked at my hands, as if seeing them for the first time. And with laughter behind his eyelids, with all the seriousness a man of his humor could muster, he said, You’ve got nice hands. You could've been a hand model.

And before the laughter can escape me,
I shake my head at him,
and squeeze his hand.
Eight-million, two-thousand, seven-hundred and fifty-four.

Beethoven by Shane Koyczan KS State Qualifier – As this program
```

---

## IC-1655: Petite Rouge: A Cajun Red Riding Hood

- Title: Petite Rouge: A Cajun Red Riding Hood
- Author (byline): Mike Artell
- Work: Not specified
- Publisher: Puffin Books
- Publication date as stated: June 2003
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1426
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mike Artell
ISBN: 978-0142500705
Publisher: Puffin Books
Date (Month/Year): June 2003
```

### Introduction (context only: never use it for content warnings)

```text
Petite Rouge: A Cajun Red Riding Hood by Mike Artell
```

### Performance text (classify this)

```text
*See the end of this selection for pronunciation guide and a link to the author reading the story in the Cajun dialect. The more you play up the dialect, the more humor you will pull from this selection!

Back in de swamp
where dat Spanish moss grow,
I heard me a story
from long time ago.

In a little ol' house
dat been built outta wood,
live a girl people call
Petite Rouge Riding Hood.

One day, when her grand-mere
come down wit' de flu,
Petite Rouge mama tol' her
what she got to do.

"Take her dis gumbo
an' t'ree or two sweater.
An' some uh dis boudin
gone make her feel better.

"You can take de pirogue
wit' dat big long push pole,
den dere’s jus' one mo' t'ing
dat you need to be tol'.

"Don' stop in de swamp!
Don' you stop on de way!
'Cause de swamp's fulla gators,
Cher! Dat's where dey stay!

"So you take dat cat
in de pirogue wit' you.
An' bring youself home
jus’ as soon as you t’roo.”

Petite Rouge take dat food,
an' her cat TeJean too,
den jump in dat pirogue
like she tol' to do.

Mama wave adieu
an', TeJean, he wave back,
as he float t'roo de swamp
where de water look black.

Dey don' be gone long
when dey see by a stomp,
a big, long, green log
dat got plenty a' bomp.

Dat log, it come close
to de pirogue and say,
"Now what you two doin' out here. . .
si'l vous plait?"

It was Claude, dat ol' gator.
Petite Rouge gotta honch
dat ol' Claude t'ink in' he'd
like to have her fo' lonch.

"We takin' dis food to mah
gran –mere’s,” she say.
"An' I got me dis pole,
so you git out de way!"

"Pardon, mad'moiselle,
I don' mean to be rude.
I jus' t'inkin' dat maybe
you share some you food.

"A taste a' dat boudin
or shrimp etouffee.
Dat's all dat I want,
den I'll git out de way."

Petite Rouge raise dat pole way up high in de air, an' she look at ol' Claude, an' she give him a stare.

"I'm countin' to t'ree,
an' if you still dere,
dis pole gonna hit you
where you part you hair."

An’ when she say “One,”
Ol' Claude back out de way.
He know dat de girl
sho' 'nuff mean what she say.

Den li'l Petite Rouge
push dat pirogue ag'in.
An' ol' Claude close his eyes.
An' ol' Claude start to grin.

"I got an idea an' I know what to do.

I'll get me dat food an' dat li'l girl too!"

Dat gator swim fast,
an' den quick as dem mouse,
he up on de porch of
Grand-mere's ol' house.

He open de door and
den stick in his head.
An' den he see Grand-mere
asleep in de bed.

He try to tiptoe
so she don' hear no sound,
but his tail bomp de shelf
an' two cup fall down.

When dey hit de floor (CRASH!), it break bot' dem cup. An' Grand-mere, she hear it. An' Grand-mere wake up . . .

"Sacre!” she exclaim.
"I know dis ain't right!"
Den she run in de closet
an' lock dat door tight!

"Ha! Ha!" ol' Claude laugh.
"You can hide; dat's okay.
In fac', it's mo' better
wit' you out de way."

Claude put on de nightgown
an' Grnnd-rnere's nightcap,
den jomp in de bed
like he ta kin' a nap.

He pull up de covers round
his big ol' green head
an' pretend dat he's Grand-mere
jus' lyin' in bed.

An' sho' 'nuff, right soon
dere's a knock at de door,
an' Claude say, "Come in . . .
What you stay outside fo'?"

An' in walk TeJean
an' Petite Rouge Riding Hood.
An' dey look at dat Grand-mere,
an' she don' look good.

Petite Rouge, she say, "Grand-mere ! You face! It's all green!

An' you skin got dem bomps, Now what do dat mean?"

Ol' Claude make a smile,
an' he say, "It's dat flu.
It make me all green wit' dem bomps,
Dat’s fo’ tru’.

"Why don' you come closer,
'cause I wanna see
all dat good food you mama
done cook fo' po' me."

Petite Rouge Riding Hood
an' den TeJean de cat,
dey take a step closer
from where dey was at.

Petite Rouge, she say, "Grand-mere!
I know you been sick,
but I t'ink mah eyes
be playin' on me a trick.

"You mout' kinda big,
an' you nose kinda long,
an' I got me a feelin'
dat somet'in' bad wrong."

"I been rubbin' mah nose
wit' dem tissue," say Claude,
"an' mah nose look fonny
'cause I rub it too hard.

"Now come one step closer,“
say Claude kinda sweet,
"’cause I t'inkin' dat maybe
it's 'bout time to eat."

Petite Rouge and TeJean
get up real close.
When Claude smile,
TeJean turn as white as dem ghos'.

Petite Rouge, she say, "Grand-mere!
You teeth big and white!
An' TeJean an' me know
dat somet'in' ain't right."

An' dat's when Claude laugh,
an’ he say, “Oh . . . Mais oui!
It ain't right fo' you,
but it sho' right fo' me!"

Claude t'ro off dem sheet. Petite Rouge shout, "Aiieee!

It's dat gator who wanna make lonch outta me!"

Claude crawl out de bed an' den onto de floor. Den Petite Rouge know she got some trouble, fo' sho' !

But TeJean de cat, ya'll,
he know what to do.
He smart fo' a cat.
Yeah, you know dat fo' tru'.

When Claude turn his back,
TeJean run to de table
An’ jump up on top
jus' as fas' as he able.

He find him de bottle dat say "Red Hot Sauce." Den he reach back his arm an' he give it a toss.

He see Petite Rouge catch de sauce in her han", den he pull out dat basket a piece a' boudin.

He toss dat boudin
jus' when Claude start to hiss.
TeJean cross his fingers
an' hope she don' miss.

Petite Rouge watch dat boudin
come fly t'roo de air,
den she reach up an' catch it . . .
but guess who right dere?
Dat's right! It was Claude.
Petite Rouge knew one t'ing:
Ol’ Claude's mout' ain't open
'cause he like to sing!

She take dat hot sauce
and 'fo' you count to two,
she soak dat boudin wit' dat sauce,
t’roo an t’roo.

She shove dat boudin right
in front a' Claude's nose,
jus' 'bout de same time
Claude done snap his jaws close.

He t'ink he done bite
Petite Rouge Riding Hood,
an', at firs', Claude be t'inkin'
she taste pretty good.

But den he stop chewin'
an' close bot' his eye,
den sit up and t'ink
maybe he gonna die!

He make dem back flip 'cause dat boudin so hot. An' de next t'ing you know, his tail tied in dem knot!

He dance all around.
He don' know what to do.
His mout' feel like fire.
His nose burnin' too.

So into de swamp wit' his mout' open wide, Claude jomp in dat water to cool off inside.

An' den, from dat closet, Grand-mere, she peek out, 'cause she want to see what be makin' Claude shout.

An' when she see Claude in dat swamp jompin' rouu', she come out de closet an' dance up and down. Den Grand-mere, TeJean, an' Petite Rouge Riding Hood be roll' on dat floor an' dey laugh deyself good.

Den Grand-mere stan' up an' she dus' off her clothes. She say, "Hoo! Dat food sho' smell good to mah nose.

"Now pull up some chair
an' le's take a look
at all a' de good food
you mama done cook."

An' soon, dey all eatin'
dat shrimp etouffee,
boudin, an' gumbo
wit' lotsa file.

An' when dey all t'roo,
Petite Rouge tell Grand-mere,
"Go sit youself down
in you big rockin' chair."

Grand-mere, she sit down
wit' TeJean on her lap,
an' soon Petite Rouge and
dem all take dem nap.

An' folks in de swamp
say dat sometimes dey see
ol' Claude hangin' roun'
dat ol' stomp of a tree.

"CauseClaude, dat ol' gator, he finally tool down. But when he see people now, he don' come roun'. Ol’ Claude reckon .people be too hot to eat. He don' know dat de hot sauce done made all de heat.

Ol' Claude, hebeen tricked,
so it all worked out good
fo' TeJean, Grand-mere,
an' Petite Rouge Riding Hood!
```

---

## IC-1656: Philadelphia Poems

- Title: Philadelphia Poems
- Author (byline): Lynn Hoffman
- Work: Not specified
- Publisher: Kelsay Books
- Publication date as stated: December 2016
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1302
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lynn Hoffman
ISBN: 978-1945752124
Publisher: Kelsay Books
Date (Month/Year): December 2016
```

### Introduction (context only: never use it for content warnings)

```text
Lynn Hoffman's latest book Philadelphia Poems could have been titled “Philadelphia Stories” as it explores his city in a series of fast paced scenes and moments. He serves up a colorful cast of characters, some more savory than others. There’s the weight lifter who embraces Hawaiian shirts; the self-proclaimed prophet; the crazy, or not so crazy, poet and the aging man with a less than stellar childhood. Add in the gritty language of the neighborhood and these moments come dramatically to life. Philadelphia Poems by Lynn Hoffman.
```

### Performance text (classify this)

```text
This poetry compilation is best performed with very strong character development. Consider 4 different speakers with unique character qualities, speech patterns and mannerisms to bring the stories of these 4 Philadelphia citizens to life.

bennny d goes hawaiian 3:19 benny d is sitting outside gleaner's coffee shop on ninth

street. he's got a book of poems and a braid of fresh

mozzarella. the mozz cost seven bucks at talluto's, the book was a

deuce at gilmore's

it's a big book, but benny's stuck on one line
e consarlo dell'umano stato
'and console him for being human'
the poet's saying what parents should do for kids
and benny d's thinking that he could use
a cupla spoonfuls of consolation right now
to go with the thick smoky coffee he's drinking
and this certain memory that makes his world
sad and yellow and jaundiced in the eye.
then this guy stops beside his table.
the guy's not too steady on his feet,
swaying in wind that blows off his personal ice cap
he points at benny d and make a prophecy.
"you" he says "should wear hawaiian shirts, that way you

won't look freaky."

now benny d lifts weights, reads a lot of poetry
and sometimes he wears big floppy hats to keep the
sun
from bouncing off his bald head and blinding the
pigeons who-he fears-might hurt themselves
by flying blind in a dangerous neighborhood.
but he ain't freaky, no way
at least not how we measure things down
here, south of washington ave.

but benny's a reasonable man and so as the prophet is blown uptown, benny is moved. he feels the weight of his being human he wants it lifted, he wants to be consoled for the freakishness of this whole human business. so he leaves his coffee, walks home and puts on the one hawaiian shirt he owns: yellow with faded red orchids and suddenly things don't feel so bad.

the next morning, benny's at the thrift shop and he's got three more hawaiian shirts. he practices standing next to the fruit stands on ninth street, sometimes with the grapes, sometimes with papayas.

benny's not a man you laugh at so people don't but they smile and three or four times an hour someone compliments his shirt-the green one with the parrot or the pale blue shirt with the surfers or even the one that's all

pineapples. usually it's a woman doing the complimenting and if you ask benny d these days how it's going he's likely to tell you that it's great, just freakin' great.

Crazy Man
crazy man’s walking down walnut street
talking to himself, no, not just talking
pointing hands, cutting slices of invisible provolone,
pounding an airy lectern,
slapping fist to chest and raising his chin to heaven

offering up his special understanding of the nature of things and

urging heaven to agree
and give him oh give him lordy man, a sign, a nod
a yesyes even if only he can hear
the big uh-huh. then he will close the deal
with the great understanding and the cosmic heart and

mind and wallet will embrace him and by the time he reaches

Rittenhouse square he will be affirmed by the firm, understood by those with

standing, not withstanding that no one but him heard a thing on walnut street that

day.

he could be rabid-bat, gnat-flicking, pinky-sticking

suitcase nuts.
he could be living inside a bread bag where
there’s nothing but him and six invisible pets
and chandeliers made out of fine-wrought wire-taut

thought.
or
he could be just another guy with a phone
in his skull who’s walking while he’s talking to a woman
who won’t quite do just yet just now just what
or
he could be a poet trying to get a ruling
that it’s really all one big pretzel
no matter how you salt it.
and ain’t it a shame about the rest of us
walking the other way, looking at
the crazy man lover poet and not knowing
which one he is
or which one we’ll be
when we poke our very own hands in the air
and drum our breasts
on the other, rather side of the square.

Louie Scungil’ Saves the World

the ladies with the perfect hair ankle their
way off the sidewalk to avoid running into louie scungil’.
gay tom’s dogs scoot sideways barking
and the bartender with the pink tattooed scalp
lowers her head and raises her step count
passing louie scungil’ who is drunk enough
by seven p.m. on april first to embrace the world
and drunk enough to have just *whizzed* in the
fountain
at primo levy plaza where passyunk crosses tasker.
‘i love you’ louie screams ‘love ya . . . love youse all’
‘i am the messiah’ he says ‘jesus came back’.
there’s almost-silence on the street,
the old guys hangin’ on the corner,
they don’t say nothin’ because they went to school
with louie’s brother and the perfect hair ladies
don’t say nothin’ because there’s nothin’ to say.
but fat joey, he’s walking by, he turns to louie,
real loud: “you ain’t no messiah.
i know ‘cause I’m the messiah.”
and one of the hair ladies, the one from Haddonfield,
ronelle, she stops and takes a step to louie
“hey louie, it’s me, ronelle. i’m the messiah.
me and my son anthony too, we’ll save you’re a**
and I guess you know what
gay tom’s dogs said and you can image up
the corner boys all tapping their chests and
saying soft “it’s me it’s me” and all the waves
of cooks and saints and blowhards up and down
the avenue yelling into the smoky spring night
“I, I, yo, I am the promised one, me me.”
and you can image up right now that you and me
and louie scungil’ and all of them
were swept along the curb and into spring south philly

air”
blown past stoops and high into the center city night
and just like that, we were saved.
yeah, saved,

Drinking Homebrew in Eddy’s Kitchen

It's a brown-ale, light-weight, herbal, kinda sugary It goes down quick like sea-foam bubbles popping on the beach. Eddy's talking, telling the pictures on the wall- The ones too rough for the parlor, too sweet for the

shoe box: Him in his Navy whites. Eddy and Kate on their wedding. Him on the Basketball court with two boys, one dead now, one moved to Any-Zona. His voice all light and white-thin as the peel of a garlic just as dry, as likely to be blown away by a

belch or a puff of air. He's spinning spider threads-soft, sticky, weak and strong. "The secret is honey." he says. "That and some rosemary from the bush in the back." He's talking about the beer, of course, About what you bring from far away, what you keep at home. There's a shot of their old house in Kensington, One of his Dad on a day when he was sober almost 'til dusk. Another of Eddy and Kate in front of a cabin, two little boys in mid-squirm on the steps. Eddy rinses out the bottles, gets two more. I ask about the black and white dog in the frame with the hearts "That's Buster." he says like I didn't

know and then he can't say no more. "Ah, don't get him started on his dear old dog." Kate says she goes on like she was a TV show. "He's really just weepy for his lost childhood." But I know Eddy's childhood, no honey, not much rosemary, love mashed into nothin', ferment dried

and gone. "To Buster!" I say. And Eddy and me, we drink to that.
```

---

## IC-1657: Playing Scrabble with Eddie

- Title: Playing Scrabble with Eddie
- Author (byline): Taylor Mali
- Work: What Learning Leaves
- Publisher: Hanover Press
- Publication date as stated: July 2002
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 392
- Already set (do not supply): none

### Source block (context only)

```text
Author: Taylor Mali
Book: What Learning Leaves
ISBN: 978-1887012171
Publisher: Hanover Press
Date (Month/Year): July 2002
```

### Introduction (context only: never use it for content warnings)

```text
Taylor Mali spent nine years teaching English, history, and math, including stints at Browning School, a boys school on the Upper East Side of New York City, and Cape Cod Academy, a K-12 private school on Cape Cod, Massachusetts. He now lectures and conducts workshops for teachers and students all over the world. In 2001 Taylor Mali used a grant from the New York Foundation for the Arts to develop the one-man show "Teacher! Teacher!" about poetry, teaching, and math. He is a strong advocate for the nobility of teaching and in 2000 he set out to create 1,000 new teachers through "poetry, persuasion, perseverance, or passion." As of June 1, 2009, he has 335.

Playing Scrabble with Eddie by Taylor Mali
```

### Performance text (classify this)

```text
Despite his dyslexia or perhaps because of it, Eddie can beat every other eighth grader in Scrabble. Kick their asses in fact, and he knows it, though he can't say it, at least not in those words, because if he said "ass" in my eight grade I'd give him a detention on the spot.

Scrabble was made for his mind.
Show him a rack of seven letters,
he'll tell you in an instant 10 different words
that use some combination of those letters,
his mind hard-wired for confusion,
for discombobulating vowels
and the jangling clangor of consonants.
But ask him to spell those 10 words,
and he may DARE to READ DEAR
when the word READS DREAD.

Combine dyslexia with hyperactivity,
which now we call A.D.D.,
Attention Deficit Disorder,--
though Eddie says impishly, D.D.A.!--
fifteen milligrams of Ritalin taken twice a day,
dispensed by the nurse, an IQ of 165
and all the hormones of a 13-year-old boy
just dying for an education, and you have yourself
one horny, whacked-out, eight-grade genius
staring at the seven tiles on his rack
as if getting the letters in the right order
would unlock all the secrets of the language.

Eddie stares at my face, at the board, at his rack, at his rack, at the board, at my face. And I wonder what his dyslexic, rearranging mind is doing with my eyes & my ears & my nose. How many one-eyed, Picasso-faced English teachers are staring back at him from the educated audience of his adolescence? How many monsters can he spell with my face? But here comes the word:

K-C-U-F

Kcuf? Eddie, I think I'm going to have to challenge you on that word.

And Eddie reddens. Eddie reddens
like he finally got the punch line to a dirty Joke,
which in a way he has. Eddie reddens
like I've finally caught him swearing,
which in a way I haven't. Yet.

And the letters pivot around the K.

C-U-F

Oh. Well, that's different.

"Is that OK, Mr. Mali?"

Is that okay!? Is that okay, Eddie!?
You landed the F on a Double Letter square
and the K on a Double Word--
That's 34 points, young man!

"Hot shit!" says Eddie.

And I give him a detention on the spot.
```

---

## IC-1658: Poem Against the State (of Things): 1975

- Title: Poem Against the State (of Things): 1975
- Author (byline): June Jordan
- Work: In Search of Color Everywhere
- Publisher: Harry N. Abrams, Inc.
- Publication date as stated: Jan 1996
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 671
- Already set (do not supply): none

### Source block (context only)

```text
Author: June Jordan
Book: In Search of Color Everywhere
ISBN: 978-1556704512
Publisher: Harry N. Abrams, Inc.
Date (Month/Year): Jan 1996
```

### Introduction (context only: never use it for content warnings)

```text
By the summer of 1971, the state prison in Attica, New York, was ready to explode. Inmates were frustrated with chronic overcrowding, censorship of letters, and living conditions that limited them to one shower per week and one roll of toilet paper each month. A riot ensued and hostages were taken. After four days of unsuccessful negotiations . . . On the rainy Monday morning of September 13 at 9:46 a.m., helicopters flew over the yard, dropping tear gas as state police and correction officers stormed in with guns blazing. The police fired 3,000 rounds , killing 29 inmates and 10 of the hostages. Most were shot in the initial barrage of gunfire, but other prisoners were shot or killed after they surrendered. In the week after its conclusion, police engaged in brutal reprisals against the prisoners, forcing them to run a gauntlet of nightsticks and crawl naked across broken glass, among other tortures. In 1974, lawyers representing the 1,281 inmates filed a $2.8 billion class-action lawsuit against prison and state officials.

Poem against the State (of Things): 1975 by June Jordan
```

### Performance text (classify this)

```text
1

wherever I go (these days)

the tide seems low

(oh) wherever I go (these days)

the tide seems very
very low
ATTICA!
ALLENDE!
AMERIKA!

Welcome to the Sunday School
of outfront machineguns
and secretive
assassinations
EVERYBODY WELCOME!

Put your money on the plate
your feet on the floor
and better keep a bodyguard
standing at the open door
EVERYBODY WELCOME!

Almighty
Multinational
Corporate
Incorporeal
Bank of the World
The World Bank
Diplomacy
and Gold

This is the story:

This is the prayer:
Rain fell
Monday the thirteenth
1971
Attica
coldstone covered by a cold moon -
light hidden by the night
when fifteen hundred Black
Puerto Rican
White (one or two)
Altogether Fifteen Hundred Men
plus
thirty-eight hostages
(former keepers of the keys
to the ugliest
big
house of them all )
Fifteen Hundred and Thirty
Eight
Men
lay sleeping in a long
wait
for the sun
and not one with a gun
not one with a gun

(oh) wherever I go
the tide seems low
Fifteen Hundred and Thirty
Eight
prisoners in prison
at Attica / they
lay sleeping in a long
long wait
for the sun
and not one with a gun
not one with a gun

But they were not really alone:
ATTICA!
ALLENDE!
Despite
the quiet of the cold moon -
light on the coldstone
of the place
Despite
the rain that fell
transforming the D-yard
blankets and tents
into heavyweight, soggy
and sweltering hell

The Brothers were hardly alone:
on the roofs
on the walkways
in turrets
and tunnels
from windows
and whirlybirds

overhead

The State lay in wait

Attica Attack Troops
wearing masks
carrying gas canisters
and proud to be white
proud to be doing
what everyone can
for The Man
Attica Attack Troops
lay armed
at the ready
legalized killers
hard
chewing gum
to master an all-American impatience
to kill
to spill blood
to spill blood of the Bloods

and not one with a gun

the State lay in wait

Attica Attack Troops
carrying pistols and
big-game / .270 rifles and
Ithaca Model 37 shotguns
with double-o buckshot
and also
shotguns appropriate
for “antivehicle duty”
or shotguns appropriate
for “reducing a cement block wall
to rubble”
they were ready

for what?

(oh) wherever I go (these days)

the tide seems low
Fifteen Hundred and Thirty Eight
Prisoners
lay waiting for the next
day’s sun
Fifteen Hundred and Thirty Eight
Brothers
asleep
and not one with a gun
not one with a gun.

2

Why did the Brothers revolt against Attica?

why were they there?

What did they want?

the minimum wage
less pork
fresh fruit
religious freedom
and more than one shower a week.

What did they want?

a response
recognition
as men
“WE are MEN!” They
declared:
“WE are MEN!
We are not beasts and do not
intend to be beaten
or driven as such.”

ATTICA!

ALLENDE!

AMERIKA! The State lay in wait.

3

Black woman weeping at the coldstone wall Rain stops. And blood begins to fall

“JACKPOT ONE!” was the animal
cry of The State
in its final
reply
“JACKPOT ONE!!”
was the cry

9:26 A.M.
Monday the thirteenth
September 1971
Police
State Troopers
prison guards
helicopters/The Attica Attack Troops
terrified the morning
broke through
to the beasts within them
beasts
unleashed by the Almighty
Multinational
Corporate

Incorporeal
Bank of the World
Despoilers
of Harlem
Cambodia
Chile
Detroit
the Philippines
Oakland
Montgomery
Dallas
South Africa
Albany
Attica
Attica
The Attica Killers
The Almighty state shot/
murdered/massacred
forty three men
forty three men

The other Brothers/they
were gassed and
beaten
bleeding or not
still clubbed and beaten:

“Nigger! You should have got it through the head! Nigger! You gone wish that you were dead! Nigger! Nigger!”

Monday the Thirteenth
September 1971
Attica
Blood fell on the Brothers: Not one with a gun.

Black women weeping into coldstone.

4
wherever I go (these
days)
the tide seems low

(oh) wherever I go (these
days)
the tide seems very
very low

God’s love has turned away from this Almighty place

But
I will pray
one prayer while He yet grants me
oime and space:

NO MORE AND NEVER AGAIN! NO MORE AND NEVER AGAIN!

A-men. A-men.
```

---

## IC-1659: Prayers from the Ark

- Title: Prayers from the Ark
- Author (byline): Carmen Bernos de Gasztold
- Work: Not specified
- Publisher: Turtleback Books
- Publication date as stated: Jan 1995
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 672
- Already set (do not supply): none

### Source block (context only)

```text
Author: Carmen Bernos de Gasztold
ISBN: 978-0606085892
Publisher: Turtleback Books
Date (Month/Year): Jan 1995
```

### Introduction (context only: never use it for content warnings)

```text
When God sent the Great Flood to destroy the earth, he did so to rid the earth of sin and wickedness. The human soul had faced corruption of the seven deadly sins and God saw little chance for redemption. One righteous man, Noah, and his family was selected to regenerate the human race and God also took great care to save the animals.

The Floods came and everyone, including the animals began to pray in earnest. These ``prayers'' reflect each animal’s nature, function, and fate. Each unmistakably mirrors human feelings and foibles: the self-important rooster; the haughty cat--all pray in a way that reveals essential weaknesses and strengths.

Carmen Bernos de Gasztold suggests that if indeed animals could talk, they would demonstrate the same degradation of the soul. These are their Prayers from the Ark.
```

### Performance text (classify this)

```text
Noah’s Prayer

Lord, what a menagerie!

Between Your downpour and these animal cries one cannot hear oneself think!

The Prayer of the Dog

Lord,
I keep watch!
If I am not here
who will guard their house?
Watch over their sheep?
Be faithful?
No one but You and I
understands
what faithfulness is.
They call me, "Good dog! Nice dog!"
Words...
I take their pats
and the old bones they throw me
and I seem pleased.
They really believe they make be happy.
I take kicks too
when they come my way.
None of that matters.
I keep watch!

Lord,
do not let me die
until, for them,
all danger is driven away.

Amen

The Prayer of the Cat

Lord,
I am the cat.
It is not, exactly, that I have something to ask of
You!
No –
I ask nothing of anyone–
but,
if You have by some chance, in some celestial barn,
a little white mouse,
or a saucer of milk,
I know someone who would relish them.
Wouldn’t You like someday
to put a curse on the whole race of dogs?
If so I should say,

Amen Noah’s Prayer (continued)

The days are long,
Lord.
All this water makes my heart sink.
When will the ground cease to rock under my feet?
The days are long.
Master Raven has not come back.

The Prayer of the Raven

I believe,
Lord,
I believe!
It is faith that saves us, You have said it!
I believe the world was made for me,
because as it dies --
I thrive on it.
My undertaker's black
is in keeping with my cynical old heart.
Raven land is between You and that life down there,
for whose end I wait to gratify myself.
"Aha!" I cry. "Avant moi le déluge!"
What a feast!

I shall never go back to the Ark!
To the Ark. . .
Oh let it die in me--
this horrible nostalgia.

Amen.

Noah’s Prayer (continued)
Here is Your dove.
Will she find us a twig of hope?
The days are long,
Lord.

The Prayer of the Dove

The Ark waits,
Lord,
the Ark waits on Your will,
and the sign of Your peace.
I am the dove,
simple
as the sweetness that comes from You.
The Ark waits,
Lord;
it has endured.
Let me carry it
a sprig of hope and joy,
and put, at the heart of its forsakenness,
this, in which Your love clothes me,
Grace immaculate.

Amen.

Noah’s Prayer (continued)

Guide Your Ark to safety,
some zenith of rest,
where we can escape at last
from this brute slavery.

The Prayer of the Mouse

I am so little and grey,
dear God,
how can You keep me in mind?
Always spied upon,
always chased.
Nobody ever gives me anything,
and I nibble meagrely at life.
Why do they reproach me with being a mouse?

Who made me but You?
I only ask to stay hidden.
Give me my hunger’s pittance
safe from the claws
of that devil with green eyes.

Amen

The Prayer of the Little Bird

Dear God,
I don't know how to pray by myself
very well,
But will You please
protect my little nest from wind and rain?
Put a great deal of dew on the flowers, many
seeds in my way.
Make Your blue very high,
Your branches lissome;
let Your kind light stay late in the sky
and set my heart brimming
with such music that I must sing, sing, sing. . .
Please Lord.

Amen.

Noah’s Prayer (continued)

The days are long,
Lord.
Lead me until I reach the shore of
Your covenant.

Amen.

The Prayer of the Old Horse

See, Lord,
My coat hangs in tatters,
like homespun, old, threadbare.
All that I had of zest,
all my strength,
I have given in hard work
and kept nothing back
for myself.
Now my poor head swings
to offer up
all the loneliness
of my heart.
Dear God,
stiff on my thickened legs
I stand here before You:
Your uprofitable servant.
Oh! of Your goodness,
give me a gentle death.

Amen.
```

---

## IC-1660: Privilege to Complain

- Title: Privilege to Complain
- Author (byline): Rudy K. Francisco and Andrea Gibson
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1177
- Already set (do not supply): none

### Source block (context only)

```text
Author: Rudy K Francisco
Book: Helium (Pg 91-94)
ISBN: 978-1943735198
Publisher: Button Poetry
Date (Month/Year): Nov 2017
Author: Andrea Gibson
Book: Pole Dancing to Gospel Hymns (Pg 73-76)
ISBN: 978-0981521305
Publisher: Write Bloody Publishing
Date (Month/Year): June 2008
```

### Introduction (context only: never use it for content warnings)

```text
Optimists see: A glass half full . . .

Pessimists see: A glass half empty. . .

Chronic complainers see: A glass that is slightly chipped holding water that isn't cold enough, (shift voice to become progressively more put out and in first person as introduction continues) probably because it's tap water when I asked for bottled water and wait, there's a smudge on the rim, too, which means the glass wasn't cleaned properly and now I'll probably end up with some kind of virus. Why do these things always happen to me?!

The Privilege to Complain – A Program designed to perhaps make us think twice about what we choose to complain about with poems by Rudy K. Francisco and Andrea Gibson.
```

### Performance text (classify this)

```text
On May 26th, 2003,
Aron Ralston was hiking,
a boulder fell on his right hand,
he waited four days,
he then amputated
his own arm with a pocketknife.

On New Year’s Eve,
a woman was bungee jumping,
the cord broke,
she fell into a river
and had to swim back to land
in crocodile-infested waters
with a broken collarbone.

Claire Champlin was smashed in the face by a five-pound watermelon being propelled by a slingshot.

Matthew Brobst was hit by a javelin.

David Striegl was actually punched in the mouth by a kangaroo.

The most amazing part about these stories
is when asked about the experience
they all smiled, shrugged, and said
“I guess things could have been worse.”

Complainers by Rudy K. Francisco

So go ahead, tell me that you’re having a bad day.

Tell me about the traffic.
Tell me about your boss.
Tell me about the job
you’ve been trying to quit for the past four years.
Tell me the morning is
just a townhouse burning to the ground
and the snooze button is a fire extinguisher.

Tell me the alarm clock
stole the keys to your smile,
drove it into 7 am
and the crash totaled your happiness.
Tell me.
Tell me how blessed are we to have tragedy
so small it can fit on the tips of our tongues.

When Evan lost his legs he was speechless. When my cousin was assaulted she didn’t speak for 48 hours.

When my uncle was murdered, we had to send out a search party to find my father’s voice.

Most people have no idea that tragedy and silence have the exact same address.

When your day is a museum of disappointments,
hanging from events that were outside of your control,
when you feel like your guardian
angel put in his two week notice two months ago
and just decided not to tell you,
when it seems like God
is just a babysitter that’s always on the phone,
when you get punched in the esophagus
by a fistful of life,

Remember,
every year
two million people die of dehydration.
So it doesn’t matter if
the glass is half full or half empty.

There’s water in the cup. Drink it and stop complaining.

Muscle is created by lifting things
that are designed to weigh us down.
When your shoulders feel heavy
stand up straight and call it exercise.
Life is a gym membership
with a really complicated cancellation policy.

Remember,
you will survive,
things could be worse,
and we are never given
anything we can’t handle.
When the whole world crumbles,
you have to build a new one
out of all the pieces that are still here.

Remember, you are still here.

The human heart beats
approximately 4,000 times per hour
and each pulse,
each throb,
each palpitation is a trophy
engraved with the words
“You are still alive.”
You are still alive.
So act like it.

TRANSITION

In the next selection, Andrea Gibson theorizes that the reason Americans complain about small things and suffer from depression at alarming rates is because we feel we are unable to solve the bigger issues in our society and in our world. When the Bough Breaks by Andrea Gibson When the Bough Breaks by Andrea Gibson (Pg 73-76)

It’s two a.m.
The emergency room psychiatrist looks up from his
clipboard
with eyes paid to care
and asks me if I see people who aren’t really there.
I say, “I see people
how the hell am I supposed to know
if they’re really there or not?”
He doesn’t laugh
neither do I.
The math’s not on my side
ten stitches and one lie.
I swear I wasn’t trying to die.
I just wanted to see what my pulse looked like from the
inside.

Fast forward one year.
I’m standing in an auditorium behind a microphone
reading a poem to four hundred Latino high school kids
who live with the breath of the INS
crawling up their mother’s backbones
and I am frantically hiding my scars
‘cause the last thing I want these kids to know
is that I ever thought that my life was too hard.

I’ve never seen a bomb drop.
I’ve never felt hunger.
I’ve also never seen lightning strike
but we’ve all heard thunder
and it doesn’t take a genius to tell something’s burning.
The smoke rises between us,
forming walls so high
they split the sky like slit wrists
and then the stars fall like blood.
We’re all left with nothing, but a death wish.

He said, “call me by my true name
I am the child in uganda all skin and bone”
Do you remember the rest?
how about this one, America
Jesus wept.
America, Jesus wept
but look at your eyes
dry as the desert sand
dusting the edges of your soldier’s wedding bands.
Look at your soul playing dead
because your ribcage is abu ghraib
is san quintin
is guantanamo bay
and your heart had beaten them so many times
they bleed the moon.

Do you know children in Palestine fly kites to prove that they are still free? Can you imagine how that string must feel between their fingers as they kneel in the cinders of our missile heads You can count the dead by the colours in the sky

The bough is breaking. The cradle is falling. Right now a six-year old girl is crutched in a ditch in Lebanon wishing on falling bombs. Right now our government is recording the test scores of black and Latino 4th graders to see how many prison beds will be needed in the year 2021. Right now there’s a man on the street outside that door with outstretched hands full of heart beats no one can hear. He has cheeks like torn sheet music, Every tear a broken crescendo falling on closed ears. At his side there’s a girl with eyes like an anthem that no one stands up for.

Doctor, our insanity is not that we see people who aren’t
there.
It’s that we ignore the ones who are.
Till we find ourselves scarred and ashamed
walking into emergency rooms at three a.m.
flooded with a pain we cannot name or explain
because we are bleeding from the outside in.
Skin is not impervious.
Cultures built on greed and destruction do not pick and
choose who they kill.

Do we really believe our need for Prozac
has nothing to do with Baghdad,
with Kabul, with the Mexican border
with the thousands of US school kids
bleeding through budget cuts that will never heal
to fuel war tanks?

Thank god for denial.
Thank god we can afford the makeup
to pile upon the face of it all.
Look at the pretty world.
Look at all the smiling people
and the sky with a missile between her teeth
and a steeple through her heart
and not a single star left to hold her

And the voices of a thousand broken nations saying “wake me, wake me, when the American dream is over”
```

---

## IC-1661: Proud to be Latina/Latino – A Collection

- Title: Proud to be Latina/Latino – A Collection
- Author (byline): Denice Frohman, Maria Luisa Arroyo and Christina Stoddard
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 819
- Already set (do not supply): none

### Source block (context only)

```text
Author: Denice Frohman
Book: Reading, Writing, and Rising Up – 2nd Edition
(Pg 248)
ISBN: 978-0942961690
Publisher: Rethinking Schools, Ltd
Date (Month/Year): June 15, 2017
Author: Maria Luisa Arroyo
ISBN: 978-1931010436
Publisher: Bilingual Review Pr
Date (Month/Year): June 2008
Author: Christina Stoddard
Book: Water for the Cactus Woman (pg 38)
ISBN: 978-1947980273
Publisher: Spuyten Duyvil Publishing
Date (Month/Year): April 13, 2018
```

### Introduction (context only: never use it for content warnings)

```text
Reports of people being berated or attacked while communicating in Spanish, the world’s second most spoken language, are on the rise. When people glare at others for speaking Spanish in public, refer to it as a “dirty” language, say “go back to your country” or even, “Speak English. You’re in America!” — is it any wonder that some Latinas/Latinos begin to feel ashamed of their language and cultural identity?

Well, I’m here to tell you that Spanish is a beautiful language and the Latino culture is inspiring. I am proud to be Latina/Latino – A collection by Denice Frohman, Maria
```

### Performance text (classify this)

```text
Luisa Arroyo and Christina Stoddard.

Accents by Denice Frohman

my mom holds her accent like a shotgun,
with two good hands.
her tongue, all brass knuckle
slipping in between her lips
her hips, all laughter and wind clap.

she speaks a sanchocho* of spanish and english, pushing up and against one another, in rapid fire

there is no telling my mama to be "quiet,"
she don't know "quiet."
her voice is one size better fit all
and you best not tell her to hush,
she waited too many years for her voice to arrive
to be told it needed house keeping.

English sits in her mouth remixed
so "strawberry" becomes "eh-strawbeddy"
and "cookie" becomes "eh-cookie"
and kitchen, key chain, and chicken all sound the same.

my mama doesn't say "yes" she says, "ah ha" and suddenly the sky in her mouth becomes a Hector

Lavoe song.

her tongue can't lay itself down flat enough
for the English language,
it got too much hip
too much bone
too much conga
too much cuatro*
to two step
got too many piano keys
in between her teeth,
it got too much clave
too much hand clap
got too much salsa to sit still
it be an anxious child wanting to
make Play-Doh out of concrete
English be too neat for
her kind of wonderful.
her words spill in conversation
between women whose hands
are all they got
sometimes our hands are all we got
and accents remind us that we are still
bomba*, still plena*

say "wepa*"
and a stranger becomes your hermano*,
say "dale*"
and a crowd becomes a family reunion.

my mama's tongue is a telegram from her mother decorated with the coqui's* of el campo*

so even though her lips can barely
stretch themselves around english,
her accent is a stubborn compass
always pointing her
towards home.

• sanchocho - a hearty soup, almost like a stew and is a

traditional dish in the region of Antioquia, Colombia

that combines potatoes, yuca, corn, plantains and meat • cuatro – four • bomba - something that "explodes," or "sprays." • plena – Full • wepa - of Puerto Rican descent, this exclamation is

mainly used when something is to be celebrated and

always yelled…the meaning is similar to “Oh yeah!”

“Cool!” or “Go for it!” etc.
• hermano – brother
• dale – go ahead
• coqui – small amphibian with a shrill call
• el campo – a city in Texas
Gathering Words by Maria Luisa Arroyo

One day I will write you a letter
after I have gathered enough words
I have heard
pop! pop! pop!
like little soap bubbles escaping
the animated mouths
of the women who share
pieces of gossip like bombones*
in la lavandería* every Sunday

One day I will write you a letter
after I have gathered enough words
that blossom without thorns
in painted mouths, in someone else’s countries…
In my corner, I listen to how voices ring
without the sting of bofetadas*
and how they undulate above
gushing water and swirling clothes
in machines that vibrate in la lavandería
One day, I will write you a letter
after I have gathered enough words
and enough courage
to let them ring in my mute dreams
until they sing to me: Write us. Así*.
In your childhood tongue. Recóbranos*. Recover us.
At that time, I will be able to return without fear
to la lavandería with my bags of clothes
and enough words and surrender myself to the bubbles.

• bombones - chocolates
• la lavandería - laundry
• bofetadas - slapping
• Así - Yes
• Recóbranos - Recover
Postcards to Heaven by Christina Stoddard

Mami taught kindergarten at the Catholic school at the end of our long and dusty road. Because of this, her serpentine handwriting was as perfectly beautiful as her slender fingers.

On Saturdays, Mami sat at our dinner table
and stared at the mini cactus centerpiece
until the scrambled words in her mind
found the order of filed school children
eager to drink from the water fountain
on a fiery desert afternoon in June.

Then she wrote.

“Querida Madre.*” “Querida Mamá.*” “Querida Mami.*”

Her mood dictated the greeting, Not that I ever gleaned more of her message.

Mami me dijo que* the postcards were for Abuela*, not me, the little nosy one.

Sometimes she spread postcards
out on the table and
invited me to craft a message.
She tried to entice me with
pretty pictures and
glittery gel pens.

But I never followed her siren call. I had no words for Abuela, at least none suitable for a postcard.

What would I write?

“Querida Abuela, I resent you.
You have robbed too much of
my mother’s love for me.
I wish you were alive so
I would never have to
visit your ugly grave again.”

How do you sign off a postcard like that? “Love?” “Hugs?” “Sincerely?”

• Querida Madre – Dear Mother
• Querida Mamá – Dear Mom
• Querida Mami – Dear Mommy
• Mami me dijo que - Mommy told me that
• Abuela – Grandma
• Querida Abuela – Dear Grandma
```

---

## IC-1662: Pulse – A Collection of LGBTQ Poetry

- Title: Pulse – A Collection of LGBTQ Poetry
- Author (byline): Andrea Gibson, Sam Sax, Chen Chen, Judy Grahn, Kamilah Aisha Moon and Hieu Minh Nguyen
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1308
- Already set (do not supply): none

### Source block (context only)

```text
“Orlando” by Andrea Gibson as found in Lord of the
Butterflies. Button Poetry, 2018. ISBN 9781943735433
“Standards” by Sam Sax
https://www.poets.org/poetsorg/poem/standards
“I Invite My Parents to a Dinner Party” by Chen Chen
https://www.poets.org/poetsorg/poem/i-invite-my-parents-
dinner-party
“A Woman is Talking with Death” by Judy Grahn
https://www.poets.org/poetsorg/poem/woman-talking-death
“Dressing Down” by Kamilah Aisha Moon
https://poets.org/poem/dressing-down
“Type II” by Hieu Minh Nguyen
https://www.poets.org/poetsorg/poem/type-ii
*NOTE: Poets.org is an approved NSDA website for
Interpretation Events
```

### Introduction (context only: never use it for content warnings)

```text
In 2015, a survey called “Growing Up LGBT in America,” interviewed 10,000 LGBT youth ages 13-17. The results of this survey paint a stark picture of the difficulties these youth face. According to this survey, 92% of LGBT youth report hearing negative messages about being LGBT in school or on the internet. 68% of LGBT youth report they hear negative messages about being LGBT from elected leaders. It is clear that action needs to be taken. “Pulse,” a poetry program, featuring “Standards” by Sam Sax, “I Invite My Parents to a Dinner Party” by Chen Chen, “Type II” by Hieu Minh Nguyen, “Orlando” by Andrea Gibson,
```

### Performance text (classify this)

```text
when the first responders
entered the Pulse nightclub
after the massacre in Orlando
they walked through the horrific scene
of bodies and called out,
if you are alive, raise your hand.
i was sleeping in a hotel
in the midwest at the time
but i imagine in that exact moment
my hand twitched in my sleep
some unconscious part of me aware
that i had a pulse
that i was alive
everyone around me spent that day grieving
and every tear tasted like sweat drying in the morgue
later that night, i was performing for an audience
on stage,
i couldn't keep my hand from covering my heart. 1

“A Woman is Talking with Death” by Judy Grahn and “Dressing Down” by Kamilah Aisha Moon. Because silence is no longer an option.

sometimes it’s a phone call from your lover
sometimes it’s your computer blinking on
with news of what’s wrong with your body this time
Simple really

1 From “Orlando” by Andrea Gibson
how he says the name of a disease
and suddenly you’re on your back
staring out the window onto a highway 2
in the invitation, i tell them for the seventeenth time
(the fourth in writing), that i am gay
in the invitation, i include a picture of my boyfriend
& write, you’ve met him two times,
but this time,
you will ask him things other than can you pass the
whatever.
you will ask him
about him.
you will enjoy dinner.
you will be
enjoyable.
please RSVP.
they RSVP. they come.
they sit at the table & ask my boyfriend
the first of the conversation starters i slip them
upon arrival: how is work going?

i’m like the kid in Home Alone, orchestrating
every movement of a proper family, as if a pair
of scary yet deeply incompetent burglars
is watching from the outside.
i’m like the kid
in Home Alone, except the home
is my apartment, & I’m much older, & not alone,
& i’m not the one who needs
to learn
then, my mother turns
to me, whispers in Mandarin,
is he coming with you
for Thanksgiving?
my good friend is & she wouldn’t like
this 3
the next day i woke to the news
that an assault rifle had fired
202 bullets through a gay bar
on latin night

2 From “Standards” by Sam Sax
3 From “I Invite My Parents to a Dinner Party” by Chen Chen
in one of the worst
massacres in us history -- a massacre
of people who did not leave the dance floor
when they heard gunshots
because they thought
they were just the beats
of a song 4
my mother smiles her best
sitting with her son’s boyfriend
who is a boy smile.
i smile my hurray for doing
a little better smile.
everyone eats soup.
i’m like the kid in Home Alone, pulling
on the string that makes my cardboard mother
more motherly
except she is
not cardboard, she is
my mother 5

4 From “Orlando” by Andrea Gibson
5 From “I Invite My Parents to a Dinner Party” by Chen Chen
They were my lovers,
but nobody had taught us how to swim.
i drowned, i took 3 or 4 others down
when I signed the confession of what we
had done
no one will ever speak to me again 6
suddenly a woman enters the room
to wrap a black cuff around your arm
and squeeze until you’re no longer sick
to slip a device under your tongue
the nowhere places you make yourself
inside the hallowed chambers of the hospital
and inside the man’s unsure voice
when he calls and is too scared to name the precise
strain of letters
you might share now
what parasite might feed 7
when you’re gay in Dixie,
you’re a clown of a desperate circus

6 From “A Woman is Talking with Death” by Judy Grahn
7 From “Standards” by Sam Sax
sometimes the only way to be like daddy
is to hate like him
hope your brothers laugh
instead of shoot 8
every few seconds
i’d eye the balcony
for the glint
of whatever might aim
to tear the bodies
of the boys holding hands
or the girls with the haircuts short
as my temper when rage
is a decibel i can actually get to
when i’m not just frozen
and grief-sick watching history
not be history, watching
the music not be music, knowing
someone having the best night of her life
shouted, this is my favorite song,
And then a drumbeat lifted
a rifle over a bathroom stall
and emptied a magazine
into the kidneys of a grown man
texting, mommy, i’m gonna die
his handprints in blood
on the walls, reaching
for people
dying in the fetal position,
people covered in their friend’s blood,
crying too hard to hide
from their own deaths,
people outside pushing bandanas into bullet wounds. 9
when the illness is terminal
you drink an eighth of paint thinner
while all the color drains from your face 10
ignoring the doctor’s red call 11
funny how a word can do that
garage the body

8 From “Dressing Down” by Kamilah Aisha Moon
9 From “Orlando” by Andrea Gibson
10 From “Standards” by Sam Sax
11 From “Type II” by Hieu Minh Nguyen
what if instead he’d simply called to say sorry
sometimes it’s your computer blinking on with news of
what’s wrong
with your body this time 12
dressed as I am, a young man once called me
names in spanish //
then he called me queer and slugged me.
first I thought the ceiling had fallen down
but there was the counterman making a ham
sandwich, and there was I spread out on his
counter.
for god’s sake I said when
i could talk, this guy is beating me up
can’t you call the police or something,
can’t you stop him?
he looked up from
working on his sandwich,
which was my sandwich,
I had ordered it.
“there’s a pay phone
right across the street” he said.
the next day i went to the police station
to become an outraged citizen
six big policemen stood in the hall,
all dressed as they do
they were well pleased with my story, pleased
at what had gotten beat out of me, so
i left them laughing, went home fast
and locked my door.
there is no child in me. 13
even life is like funeral practice:
half of us already dead to our families before we die,
half of us still on our knees
trying to crawl
into the family photo. 14
we all have our list of casualties 15
once I loved a boy, who feared, so much
his own sickness

12 From “Standards” by Sam Sax
13 From “A Woman is Talking with Death” by Judy Grahn
14 From “Orlando” by Andrea Gibson
15 From “A Woman is Talking with Death” by Judy Grahn
I never confessed to him my own. 16
dear God, how broke
do you have to be
to not buy people time
to get out the door
when the song
goes to hell? 17
death only uses violence
when there is any kind of resistance,
the rest of the time a slow
weardown will do.18
when this world, drunk
on hate, decides blood
is wine and drinks its fill
in the only place
they ever thought was safe?
in the only place they thought
they didn’t have to hide?
in the only place they were wanted

16 From “Type II” by Hieu Minh Nguyen
17 From “Orlando” by Andrea Gibson
because of who they loved,
and how they loved 19
look at me! 20
how broke
do you have to be
to not buy people time
to get out the door
until someone walked through their bodies
and asked who was still alive
and hardly anyone
put their hand up. 21
```

---

## IC-1663: Pursuit of Happiness and When the Bough Breaks

- Title: Pursuit of Happiness and When the Bough Breaks
- Author (byline): Andrea Gibson
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1416
- Already set (do not supply): none

### Source block (context only)

```text
Author: Andrea Gibson
Book: The Madness Vase (Pg 88-90)
ISBN: 978-1935904373
Publisher: Write Bloody Pub
Date (Month/Year): 2012
Author: Andrea Gibson
Book: Pole Dancing to Gospel Hymns (Pg 73-76)
ISBN: 978-0981521305
Publisher: Write Bloody Pub
Date (Month/Year): June 2008
```

### Introduction (context only: never use it for content warnings)

```text
March 20, 2003 – President George Bush announced the beginning of the war in Iraq. December 18, 2011 – President Barak Obama announced the end of the war and removed the last US troops.

At one time the US had more than 160,000 troops in Iraq and another 100,00 in Afghanistan. But the military pulled out of Afghanistan completely in 2021 and today operations in the Middle East are limited.

Andrea Gibson in her poem “The Pursuit of Happiness” questions American involvement in the Middle East.
```

### Performance text (classify this)

```text
Pursuit of Happiness (Pg 88-90) Tonight in Iraq, there is a race to rape little girls before they can be raped by U.S. soldiers Tonight in Iran, there is a missile aimed at the hill where Hafiz cut pieces of his soul with a knife and wove them into a blanket to protect us Tonight, my skin is the color of a hundred white flags torn apart at the seams and sewn together into the body bag that holds her only son And I am told God’s will is done

By hands that pan for gold in the bloodstreams of children while a million souls are sold on the slave blocks of a pipeline and a mother turns her bones into a bunker fills her lungs with sand and cradles her baby daughter until her own clavicle is blown to powder fine as the dust on a butterfly’s wing

But tonight there are no flowers Every flashing red light is a heart threatening to quit The moon is a tourniquet we will bleed through by morning Is this your pursuit of happiness?

The casket as small as a music box
A mother holding that song to her ear
America, I dare to rest your holy water beside her tears and
see where Jesus chooses to walk
Heaven doesn’t know your name
Only the sound of you rolling your barrels of blood to its
gates
thinking grace is something you can buy with Mohammed’s
pulse

Tell me again how you intend to rescue their women How you will teach them how to read in the schools you have turned to prisons How you will offer them doctors in the hospitals you have burned with their children inside Tell me how they won’t have to hide beneath their burkas How you will wrap them in lace ‘til they are all as conveniently rapeable as women in the States Do you know how much desert sand is on the floor of the women’s shelter in this city? Have you ever tried to blink the light back? Do you know the man who beat her had been ordered to fit five Afghani children in a single body bag Is this your pursuit of happiness?

The orphanage you lit like a cigarette
You cough and it sounds like screams
You cancel the soul with your holy flag
You dog-tagged your son,
Choke-chained his two years into eight,
and forgot his name when you couldn’t afford the gas to
drive to his funeral
Do you know how his family loved you?
Their trust was an orchard
Now tonight at their table nothing is alive but his empty
chair
If you are a nation under God, how is hell so close to your
prayers?

Do you see what you are pressing against your bones? Bones cannot break Into song A mother can never find the right place to store an empty cradle A mouth can never find the right shape to hold the lullabies it will never sing America, if you could rip the pipelines from your throat, if you could hang them like wind chimes from the battered night would you remember how freedom rings? Would you remember that every river is a lantern running without oil and your children sing your anthems so proud America The beautiful

Remember Where you melted the desert, the sand became a mirror If you could stand so close the flames caught the lashes of your eyes If you could memorize one face fading into smoke and never ever forget If you could let one more soldier write his blood type on his boots Would you let your pursuit of happiness steal so much God from the heart that I know is still pounding beneath your bloody hands?

TRANSITION

Let’s be honest for a moment. The average American is more concerned with when the new season of their favorite show is going to start or the release date of the next block-buster movie than they are about world events.

Sure, we see news reports about the Middle East, North Korea, Africa, Ukraine – but those places are half a world away. Sure, we know that in the U.S. there’s an immigration problem, an unemployment problem, a prison overpopulation problem, but they don’t really affect the average American, right? It’s just more drama at best and at worst – “fake news.”

But what if . . . what if all this DOES affect the average American. What if it is the insidious catalyst behind our rising discontent? What if we are forced to wake up from our American dream and face a reality that we simply cannot comprehend?

When the Bough Breaks by Andrea Gibson

When the Bough Breaks (Pg 73-76)
It’s two a.m.
The emergency room psychiatrist looks up from his
clipboard
with eyes paid to care
and asks me if I see people who aren’t really there.

I say, “I see people
how the hell am I supposed to know
if they’re really there or not?”
He doesn’t laugh
neither do I.
The math’s not on my side
ten stitches and one lie.
I swear I wasn’t trying to die.
I just wanted to see what my pulse looked like from the
inside.

Fast forward one year.
I’m standing in an auditorium behind a microphone
reading a poem to four hundred Latino high school kids
who live with the breath of the INS
crawling up their mother’s backbones
and I am frantically hiding my scars
‘cause the last thing I want these kids to know
is that I ever thought that my life was too hard.

I’ve never seen a bomb drop.
I’ve never felt hunger.
I’ve also never seen lightning strike
but we’ve all heard thunder
and it doesn’t take a genius to tell something’s burning.
The smoke rises between us,
forming walls so high
they split the sky like slit wrists
and then the stars fall like blood.
We’re all left with nothing, but a death wish.

He said, “Call me by my true name
I am the child in Uganda all skin and bone”
Do you remember the rest?
how about this one, America
Jesus wept.
America, Jesus wept
but look at your eyes
dry as the desert sand
dusting the edges of your soldier’s wedding bands.
Look at your soul playing dead
because your ribcage is Abu Ghraib
is San Quintin
is Guantanamo Bay
and your heart had beaten them so many times
they bleed the moon.

Do you know children in Palestine fly kites to prove that they are still free? Can you imagine how that string must feel between their fingers as they kneel in the cinders of our missile heads You can count the dead by the colors in the sky

The bough is breaking. The cradle is falling. Right now a six-year old girl is crouched in a ditch in Lebanon wishing on falling bombs. Right now our government is recording the test scores of black and Latino 4th graders to see how many prison beds will be needed in the year 2021. Right now there’s a man on the street outside that door with outstretched hands full of heartbeats no one can hear. He has cheeks like torn sheet music, Every tear a broken crescendo falling on closed ears.

At his side there’s a girl with eyes like an anthem that no one stands up for.

Doctor, our insanity is not that we see people who aren’t
there.
It’s that we ignore the ones who are.
Till we find ourselves scarred and ashamed
walking into emergency rooms at three a.m.
flooded with a pain we cannot name or explain
because we are bleeding from the outside in.
Skin is not impervious.
Cultures built on greed and destruction do not pick and
choose who they kill.

Do we really believe our need for Prozac
has nothing to do with Baghdad,
with Kabul, with the Mexican border
with the thousands of US school kids
bleeding through budget cuts that will never heal
to fuel war tanks?

Thank god for denial.
Thank god we can afford the makeup
to pile upon the face of it all.
Look at the pretty world.
Look at all the smiling people
and the sky with a missile between her teeth
and a steeple through her heart
and not a single star left to hold her

And the voices of a thousand broken nations saying “Wake me, wake me, when the American dream is over”
```

---

## IC-1664: The Rabbit, the Bear and the Zinniga-Zanniga

- Title: The Rabbit, the Bear and the Zinniga-Zanniga
- Author (byline): Theo Geisel (aka Dr. Seuss)
- Work: The Bippolo Seed and Other Lost Stories
- Publisher: Random House Books
- Publication date as stated: Sept 2011
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1043
- Already set (do not supply): none

### Source block (context only)

```text
Author: Theo Geisel (aka Dr. Suess)
Book: The Bippolo Seed and Other Lost Stories
ISBN: 978-0375864353
Publisher: Random House Books
Date (Month/Year): Sept 2011
```

### Introduction (context only: never use it for content warnings)

```text
Br’er Rabbit, the Tortise and the Hare and even Bugs Bunny. . . Literature and cartoons are full of quick-thinking rabbits out-smarting their counterparts. One little known tale featuring a very smart rabbit comes to us from Theo Geisel, known by most everyone as Dr. Seuss: The Rabbit, the Bear and the Zinnaga-Zanniga.
```

### Performance text (classify this)

```text
Once of upon of a time, way down south,
Lived a very big bear with a very big mouth
And very big teeth in his very big jaws
And very big claws in his very big paws.

And this very big bear, who was hunting for meat, One day spied a rabbit who looked good to eat. “A-ha!” thought the bear. “He looks tender, all right! Oh, boy, I’ll have rabbit for supper tonight!”

So, on his big feet, he crept up to the rabbit. He crouched very low and leaned forward to grab it, But, just as his jaws were ‘bout ready to nab it, The rabbit looked up and he say the bear’s face. “Oh-oh!” gulped the rabbit. “I’m in a bad place!”

And I see with a glance
That it’s no use to fight, ‘cause I haven’t a chance
For I am a rabbit with very small jaws
And very small claws in my very small paws.

“Alas” thought the rabbit. “This moment’s my last Unless I think terribly, terribly fast . . . I’ve got to be smart! Got to think of some trick!” And that little old rabbit, the thought mighty quick.

Then, just as the teeth of the bear touched his head, The rabbit jumped up and he suddenly said, “One, two, three, four, five, six . . . seven . . . eight . . .

nine! Nine . . . ? Only nine . . . ? That’s a very bad sign!

Poor bear!” sighed the rabbit, then counted again. And this time, he counted from one up to ten!

“Huh . . . ?” the bear grunted. He stared and he stopped. He looked mighty puzzled. His jaw sort of dropped. “Now, what were you counting, then? What did you see? Do you mean to say something’s the matter with me?”

“Err . . . well,” said the rabbit, from down where he

stood.
“I sure hate to tell you. It isn’t too good.”
“I was counting the eyelashes ‘round your two eyes,
Your left eye . . . your right eye . . . and, to my surprise,
They weren’t the same number!
Almost, but not quite.
You’ve ten on your left eye, but nine on your right!

“I’m sorry . . . SO sorry. But, sir it is true. Poor bear! This is dreadful! One eyelash too few!” The bear looked upset.

He looked frightfully sad. “Good gracious!” he gasped. “Is that really so bad?”

“Err . . . well,” said the rabbit. “I’ve counted the hairs
That grow on the eyelids of hundreds of bears
And I always have noticed, in adding up theirs,
That they always come out to an even amount.
But yours, Mr. Bear, make and un-even count!

And I guess that’s the reason,” the rabbit then said, “For the lop-sided way that you’re holding your head. It’s twisted! It’s sagging! Because of the weight Of your un-even lashes, you can’t hold it straight!”

“My head . . . ?” groaned the bear with an unhappy roar. “Why, I never knew it was crooked before! But, now that you say so, it does feel quite funny!” “I’ll bet that it hurts you a lot,” said the bunny. “I’ll bet that it hurts you right down to your tail! My! My! Mr. Bear, you look horribly pale!

“Say . . . !” How does your throat feel? A little bit

prickly?” “It does!” moaned the bear. “And my stomach feels

tickly! Poor me!” cried the bear. “I feel all-over sickly!” “Tch! Tch!” said the rabbit. “It’s just as I reckoned. Your ailment is getting much worse by the second. Your tongue, Mr. Bear . . . Does it taste a bit fuzzy? Your brain, Mr. Bear . . . Does it feel a bit wuzzy?”

“Why, yes!” gasped the bear. “It most certainly does! Is that a bad sign . . . all that fuzz and that wuzz?” “It is,” said the rabbit. “Alas and alack! It’s a sign that your trouble has spread to your back. For, even right now, while I’m standing here speaking, I hear a loud sound from your backbone! It’s creaking!”

“Oh, the lack of an eyelash can make you a wreck, The lack of an eyelash can break a bear’s neck!

It can break all your ribs! It can ruin your heart! Who knows what might happen! You may fall apart! Be careful, poor bear! Don’t you even dare cough Or your feet and your tail and your nose may fall off!” And he gave that big bear such a sorrowful look That the bear started trembling. He shook and he

shook. “Ah, me!” the bear blubbered. “Oh, what can I do? Must I die just because of one eyelash too few?”

“Oh, HOW can I get one more eyelash to grow . . . !” “Err, well,” smiled the rabbit. “It happens I know Of a way you might do it. You’re standing, you see, Right under a Zinniga-Zanniga Tree!”

“Now, the flowers of this tree have some wonderful

juices That doctors have put to some marvelous uses. Their juice, I am told, is so strong that it cures Sicknesses even much greater than yours.”

“The juice of these flowers cures measles and mumps. The juice of these flowers cures freckles and bumps. Whooping cough! Croup! Also colic and sprains! Chickenpox! Smallpox! And belly-ache pains! There’s nothing, they say, that this juice cannot do. So I think, Mr. Bear, it’s the right juice for you. “

“What you ought to do, least it seems so to me,
Is climb up this Zinniga-Zanniga Tree
And pick yourself one of these wonderful flowers.
Hold it tight to your eye for a couple of hours,
And I know it’ll cure you. I haven’t a doubt!
For the lash you are lacking will suddenly sprout!”

“You mean,” cried the bear, “I’ll have ten on each eye? You mean,” cried the bear, “that I don’t have to die? Oh, thanks!” cried the bear. “You are wonderfully good.” And he climbed up that tree just as fast as he could.

And, while that big bear held the flower to his face, The rabbit, like lightning, raced off from that place!

And, thus, he escaped from the very big jaws Of that very big bear with the very big claws, And he laughed as he ran on his very small paws: It’s always the same when you fight with Big Guys... A bit of Quick-Thinking counts much more than size!”
```

---

## IC-1665: Corner, Interview with a Policeman and Crayon Wars

- Title: Corner, Interview with a Policeman and Crayon Wars
- Author (byline): Ralph Pomeroy, Ai and Jackie Sheeler
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: A POLICE RADIO
- Teaser before the introduction: No
- Spoken words (computed): 894
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ralph Pomeroy
Book: Off the Cuffs
ISBN: 978-1887128810
Publisher: Soft Skull Press
Date (Month/Year): March 2003
Author: Ai
Book: Vice: New and Selected Poems
ISBN: 978-0393320183
Publisher: Norton, W. W. & Company, Inc.
Date (Month/Year): June 2000
Author: Jackie Sheeler
Book: Off the Cuffs
ISBN: 978-1887128810
Publisher: Soft Skull Press
Date (Month/Year): March 2003
```

### Introduction (context only: never use it for content warnings)

```text
Just as all parents broach sensitive topics with their children like AIDS and sexuality or drug use, black parents say they talk to their children about dealing with the police. It is just a matter of time, they tell them, before they encounter a police officer who sees dark skin as synonymous with crime. They coach them on how to behave: don't hang out in crowds, be polite, don't make any sudden moves, carry identification, ask to make a phone call, refuse to answer incriminating questions. It is a task they find unpleasant but necessary as their children start to venture out onto the streets alone, a way to cushion the emotional trauma that comes with discrimination. Corner by Ralph Pomeroy.
```

### Performance text (classify this)

```text
Corner

The cop slumps alertly at his motorcycle, supported by one leg like a leather stork. His glance accuses me of loitering. I can see his eyes moving like a fish in the green depths of his green goggles.

His ease is fake. I can tell.
My ease is fake. And he can tell.
The fingers armoured by his gloves
Splay and clench, itching to change something.
As if he were my enemy or my death,
I just stand there watching.

I spit out my gum which has gone stale.
I knock out my new cigarette --
Which is my bravery.
It is all imperceptible:
The way I shift my weight,
The way he creaks in the saddle.

The traffic is specific though constant. The sun surrounds me, divides the street between us. His crash helmet is whiter in the shade. It is like a bullring as they say it is just before the fighting. I cannot back down. I am there.

Everything holds me back. I am in danger of disappearing into the sunny dust, My levis bake and my T-shirt sweats.

My cigarette makes my eyes burn. But I don't dare drop it.

Who made him my enemy? Prince of coolness. King of fear. Why do I lean here waiting?

Why does he lounge there watching?

I am becoming sunlight. My hair is on fire. My boots run like tar. I am hung-up by the bright air.

Something breaks through all of a sudden. And he blasts off, quick as a craver, Snug in his power; watching me watch.

TRANSITION

A POLICE RADIO: UNIT 412 – Respond to 115 Broadway – Allen’s Liquor – Robbery in progress.

African American perpetrator, Caucasian police officer. Shots are fired and a man lies dead. Reporters swarm the scene, clamoring for interviews. . . Perpetrator . . . Victim . . . Black . . . White . . . The truth swirls into shades of gray during Ai’s Interview with a Policeman.

Interview with a Policeman

You say you want this story

in my own words,
but you won’t tell it my way.
Reporters never do.
If everybody’s racist,
that means you too.
I grab your finger
as you jab it at my chest.
So what, the minicam caught that?
You want to know all about it, right? —
the liquor store, the black kid
who pulled his gun
at the wrong time.
You saw the dollars he fell on and bloodied.
Remember how cold it was that night,
but I was sweating.
I’d worked hard, I was through
for twenty-four hours,
and I wanted some brew.
When I heard a shout,
I turned and saw the clerk with his hands in the air,
saw the kid drop his gun
as I yelled and ran from the back.
I only fired when he bent down,
picked up his gun, and again dropped it.
I saw he was terrified,
saw his shoulder and head jerk to the side
as the next bullet hit.

When I dove down he got his gun once more
and fired wildly.
Liquor poured onto the counter, the floor
onto which he fell back finally,
still firing now toward the door,
when his arm flung itself behind him.
As I crawled toward him,
I could hear dance music
over the sound of liquor spilling and spilling,
and when I balanced on my hands
and stared at him, a cough or spasm
sent a stream of blood out of his mouth
that hit me in the face.

Later, I felt as if I’d left part of myself
stranded on that other side,
where anyplace you turn down,
is out for money, for drugs,
or just for something new like shoes
or sunglasses,
where your own rage
destroys everything in its wake,
including you.
Especially you.
Go on, set your pad and pencil down,
turn off the camera, the tape.
The ape in the gilded cage
looks too familiar, doesn’t he,
and underneath it all,
like me, you just want to forget him.
Tonight, though, for a while you’ll lie awake.

You’ll hear the sound of gunshots
in someone else’s neighborhood,
then, comforted, turn over in your bed
and close your eyes,
but the boy like a shark redeemed at last
yet unrepentatant
will reenter your life
by the unlocked door of sleep
to take everything but his fury back.

TRANSITION

Jackie Sheeler draws the lines of battle between police and minorities in terms of Crayola Wars.

CRAYOLA WARS

The color of the body has been at the beginning of far too many wars

and misunderstandings. I would never be shot down 41 times in some hallway by men with eyes as blue

as my own handsome cop-daddy's eyes
because my body is the color of protection.
Every day I strut past the target-practice hearts of the
police

holding court on the street, and I'm never afraid. I have lived among badges all my life growing numb, going blind to the uniforms.

Darken me into cowardice, then: tan me black, fill in between my lines with Burnt Siena

the best of all those good Crayola names the blackest of the browns more certain than Raw Umber to result

in frequent frisks and eventual capture
in this grown-up game of cops and maybe
robbers
where the cap guns always malfunction

and bang bang you're dead is written in blood the color of tenement brick drying on the stoops of certain neighbors.
```

---

## IC-1666: Rain Compilation

- Title: Rain Compilation
- Author (byline): Mary Oliver, Delmore Schwartz, Amy
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 899
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mary Oliver
Book: New Selected Poems Volume 1
ISBN: 978-0807068199
Publisher: Beacon Press
Date (Month/Year): July 1993
Author: Delmore Schwartz
Book: Last and Lost Poems
ISBN: 978-0811210966
Publisher: New Directions Publishing
Date (Month/Year): 1989
Author: Amy Lowell
Book: Amy Lowell Remembered by Jean Elizabeth Ward
ISBN: 978-1435732469
Publisher: Lulu.com
Date (Month/Year): 2009
Author: Sara Teasdale
Book: The Essential Sara Teasdale Poetry Collection
ISBN: 978-1449973353
Publisher: CreateSpace Independent Publishing Platform
Date (Month/Year): Dec 2009
```

### Introduction (context only: never use it for content warnings)

```text
In this poetry compilation the theme of rain, in all its many forms, is presented by various poets: Mary Oliver, Delmore Schwarts, Amy Lowel and Sara Teasdale. The descriptions and feelings evoked by nature’s simple act of rain are both universal and timeless.
```

### Performance text (classify this)

```text
Lowell and Sara Teasdale

Last Night the Rain Spoke to Me by Mary Oliver

Last night
the rain
spoke to me
slowly, saying,

what joy
to come falling
out of the brisk cloud,
to be happy again

in a new way on the earth!

That’s what it said as it dropped,

smelling of iron,
and vanished
like a dream of the ocean
into the branches

and the grass below.
Then it was over.
The sky cleared.
I was standing

under a tree.
The tree was a tree
with happy leaves,
and I was myself,

and there were stars in the sky
that were also themselves
at the moment
at which moment

my right hand
was holding my left hand
which was holding the tree
which was filled with stars

and the soft rain— imagine! imagine!

the long and wondrous journeys still to be ours.

And Rain

TRANSITION The older I get, the more I enjoy the rain: the sound of it, the scent of it, the look of it. When I was a young kid, rain was a game changer. It almost always ruined my plans for fun. Now I can sit at a window with a good book and stare out at rainy days with a thankful heart.

The First Night of Fall and Falling Rain by
Delmore Schwartz
The common rain had come again
Slanting and colorless, pale and anonymous,
Fainting falling in the first evening
Of the first perception of the actual fall,
The long and late light had slowly gathered up
A sooty wood of clouded sky, dim and distant more and

more Until, at dusk, the very sense of selfhood waned, A weakening nothing halted, diminished or denied or set

aside,
Neither tea, nor, after an hour, whiskey,
Ice and then a pleasant glow, a burning,
And the first leaping wood fire
Since a cold night in May, too long ago to be more than
Merely a cold and vivid memory.
Staring, empty, and without thought
Beyond the rising mists of the emotion of causeless

sadness, How suddenly all consciousness leaped in spontaneous

gladness, Knowing without thinking how the falling rain (outside, all

over) In slow sustained consistent vibration all over outside Tapping window, streaking roof,

running down runnel and drain Waking a sense, once more, of all that lived outside of us, Beyond emotion, for beyond the swollen

distorted shadows and lights Of the toy town and the vanity fair

of waking consciousness!

TRANSITION Those few minutes after it stops raining–when the sun shows it's face through the clouds–those minutes are my favorite. It's so easy to feel at peace when the world around you is dripping wet, totally refreshed and reflecting the warm sun-glow.

Afternoon Rain in State Street by Amy Lowell

Cross-hatchings of rain against grey walls,
Slant lines of black rain
In front of the up and down, wet stone sides of buildings.
Below,
Greasy, shiny, black, horizontal,
The street.
And over it, umbrellas,
Black polished dots
Struck to white
An instant,
Stream in two flat lines
Slipping past each other with the smoothness of oil.
Like a four-sided wedge
The Custom House Tower
Pokes at the low, flat sky,
Pushing it farther and farther up,
Lifting it away from the house-tops,
Lifting it in one piece as though it were a sheet of tin,
With the lever of its apex.
The cross-hatchings of rain cut the Tower obliquely,
Scratching lines of black wire across it,
Mutilating its perpendicular grey surface
With the sharp precision of tools.
The city is rigid with straight lines and angles,
A chequered table of blacks and greys.
Oblong blocks of flatness
Crawl by with low-geared engines,
And pass to short upright squares
Shrinking with distance.
A steamer in the basin blows its whistle,
And the sound shoots across the rain hatchings,
A narrow, level bar of steel.
Hard cubes of lemon
Superimpose themselves upon the fronts of buildings
As the windows light up.
But the lemon cubes are edged with angles
Upon which they cannot impinge.
Up, straight, down, straight -- square.
Crumpled grey-white papers
Blow along the side-walks,
Contorted, horrible,
Without curves.
A horse steps in a puddle,
And white, glaring water spurts up
In stiff, outflaring lines,
Like the rattling stems of reeds.
The city is heraldic with angles,
A sombre escutcheon of argent and sable
And countercoloured bends of rain
Hung over a four-square civilization.
When a street lamp comes out,
I gaze at it for fully thirty seconds
To rest my brain with the suffusing, round brilliance of its
globe.

TRANSITION

What would happen if humans disappeared from the earth? What would the world be like without us? How would nature respond? For Sara Teasdale, the answer is “There will Come Soft Rains”

There Will Come Soft Rains By Sara Teasdale

There will come soft rains and the smell of the ground, And swallows circling with their shimmering sound;

And frogs in the pools singing at night, And wild plum trees in tremulous white,

Robins will wear their feathery fire Whistling their whims on a low fence-wire;

And not one will know of the war, not one Will care at last when it is done.

Not one would mind, neither bird nor tree If mankind perished utterly;

And Spring herself, when she woke at dawn, Would scarcely know that we were gone.
```

---

## IC-1667: Red, White and Bruised –

- Title: Red, White and Bruised –
- Author (byline): Not specified
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1172
- Already set (do not supply): none

### Source block (context only)

```text
Author: Francis Scott Key
Weblink:
https://amhistory.si.edu/starspangledbanner/pdf/ssb_lyrics.pdf
First Published: Baltimore Patriot and The American
(newspapers) Sept 20, 1814
Adopted as the US National Anthem on March 3, 1931
Author: Linda Hogan
Book: Dark. Sweet
ISBN: 978-1566893510
Publisher: Coffee House Press
Date (Month/Year): July 2014
Author: Angelica Maria Aguilera
Weblink: https://www.poemhunter.com/poem/the-star-
spanglish-banner-by-angelica-maria-aguilera-2/
ISBN: On-Line Transcript
Publisher: Poem Hunter.com
Date (Month/Year): Nov 2019
Author: Lydia Mason
Weblink: https://www.youtube.com/watch?v=-
f5PBBF8xj0
ISBN: On-line Transcript
Publisher: New York University
Date (Month/Year): 2019
* Winner of the NYU’s Constitution Day Slam 2018
```

### Introduction (context only: never use it for content warnings)

```text
These poems expose the gap between America’s promises of freedom and its history of oppression. They highlight the emotional weight carried by marginalized communities: immigrants struggling with language and belonging, Native peoples enduring forced removal and generational trauma, and citizens whose protests are met with violence rather than justice.

So many people today are questioning the meaning of the “American Dream” and challenging the systems that exclude and silence. Yet despite our nation’s painful history and protests still occurring today, we must hold on to a determined hope. A hope for a more honest, inclusive America -- one that lives up to its ideals of freedom, justice, and true belonging for all.

Red, White and Bruised with Trail of Tears: Our Removal by Linda Hogan; The Star Spanglish Banner by Angelica Maria Aguilera and Dear America by Lydia Mason
```

### Performance text (classify this)

```text
A Program with poems by Francis Scott Key, , Linda Hogan, Angelica Maria Aguilera and Lydia Mason

Star Spangled Banner by Francis Scott Key (excerpt) (Singing) O say can you see, by the dawn's early light, What so proudly we hail'd at the twilight's last

gleaming. . . And the rocket's red glare, the bomb bursting in air, Gave proof through the night that our flag was still

there, O say does that star-spangled banner yet wave O'er the land of the free and the home of the brave?

Dear America by Lydia Mason
Dear America,
I think we need to talk.
The constitution of this relationship isn’t working out.
I think we need an amendment.

(except – continues as final poem in this program)

Trail of Tears: Our Removal by Linda Hogan
With lines unseen the land was broken.
When surveyors came, we knew
what the prophet had said was true,
this land with unseen lines would be taken.
So, you who live there now,
don’t forget to love it, thank it
the place that was once our forest,
our ponds, our mosses,
the swamplands with birds and more lowly creatures.
As for us, we walked into the military strength of

hunger
and war for that land we still dream.
As the ferry crossed the distance,
or as the walkers left behind their loved ones,
think how we took with us our cats and kittens,
the puppies we loved. We were innocent of what we

faced,
along the trail. We took clothing, dishes,
thinking there would be something to start a new life,
believing justice lived in the world,
and the horses, so many,
one by one stolen, taken by the many thieves
So have compassion for that land at least.
Every step we took was one away from the songs,
old dances, memories, some of us dark and not

speaking English, some of us white, or married to the dark, or children

of translators
the half-white, all of us watched by America, all of us
longing for trees for shade, homing, rooting,
even more for food along the hunger way.
You would think those of us born later
would fight for justice, for peace,
for the new land, it’s trees being taken.
You would think
the struggle would be over
between the two worlds in this place
that is now our knowledge,
our new belonging, our being,
and we’d never again care for the notion of maps
or American wars, or the god of their sky,
thinking of those things we were forced to leave

behind,
living country, stolen home,
the world measured inch by inch, mile by mile,
hectares, all measurements, even the trail of our

tears.
With all the new fierce light, heat, drought
the missing water, you’d think
in another red century, the old wisdom
might exist if we considered enough
that even before the new beliefs
we were once whole,
but now our bodies and minds remain
the measured geography.

The Star Spanglish Banner by Angelica Maria Aguilera (singing) Oh say can you see . . . (speaking) Miguel wants to learn the star-spangled

banner. Miguel was the last fourth grader to Migrate into my English as a second language course, And is the first to raise his hand for every question. But Miguel views letters in a different way than most Because there are many words in Spanish That do not exist in English.

(singing) And the rocket's red glare . . .
We watched our home
Bursting in air
(speaking) He learns how to pack them in a suitcase
and forget
Because many phrases translate backwards
When crossing over from Spanish to English.
Throughout the whole song, he tends to say things
In the wrong order so when I asked him to sing
The second verse it sounds like

(singing) Gave proof through the night That the flag was still theirs . . . (speaking) They say music is deeply intertwined With how we remember. Miguel hears his mother's accent being mocked And learns the word “shame.”

Hears his mother's weeping
And learns the word “sacrifice.”
What does the word “America” mean?
What does the word “dream” mean?
I say two words with the same meaning are
What we call synonyms.
You could say America is a dream,
Something we all feel silly for believing in.

(singing) And for whom does that
Star-spangled banner yet wave . . .
(speaking) He says teach me how to say Bandera.
Teach me how to say star.
Teach me how to hide my country
Behind the consonants that
Do not get pronounced.
In my tongue we do not
Pronounce the letter H.
Home is not a sound my voice
Knows how to make.
It's strange what our memories hold on to.
It's strange what makes it over the border
From the left side of the brain
But what our minds do not let us forget
How an accent is just a mother tongue
That refuses to let her child go.

The language barrier is a 74-mile wall
Lodged in the back of Miguel's throat.
The bodies of words so easily lost in the translation.
Give back the land and set us free
And let us make a home for the brave.

Dear America by Lydia Mason (continued)
Dear America, I think we need to talk . . .
On our first date you promised I would always be free
to express myself.
But when I told you that I hated the way you
looked in your racism
You threw tear gas in my eyes and convinced me I was
only crying because of your beauty
On date two, you said I would always be protected
around you
But you broke my fists when I raised them in

resistance Blackened my eyes when they witnessed your

injustice Shattered my knees when they knelt in earnest And shot my heart when it felt the pain of the millions you've oppressed When we first met, I saw the dreams that you had of justice pour out of your mouth like crashing waves Hopes of freedom and equality collided through the

air.
You said it would always be us,
we the people.
I thought we were the perfect union
But how could we be perfect
When the gifts you gave me were stolen?
The labor of the Black slave
The land of the Native Americans
The freedom of the imprisoned Japanese
The dreams of the undocumented immigrant
On our 13th date you promised things
would be different
That you would finally learn how to love me.
But your love affair with shackles and chains
is far from over
You just gave it a different name.
Told me I deserved it because I broke your rules
That I took the wrong steps
That I was in the wrong place at the wrong time
That I didn't even deserve to be here
Dear America,
How am I supposed to win your game
When you decided I would lose before I could even

play. . .

Dear America,
You were never great, you just told a great story
One I hope comes true.
But until it does,
I'll be standing here, being your guiding light.

Your Lady always,

Liberty
```

---

## IC-1668: Refugee Women – A Collection

- Title: Refugee Women – A Collection
- Author (byline): Haymanot Tesfa, Julia Alvarez and Warsan Shire
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 847
- Already set (do not supply): none

### Source block (context only)

```text
Author: Haymanot Tesfa
Book: Conversation Poetry Quarterly; Summer 2009 &
Refugee Week Special #8, Pg 24
ISSN: 1759-9393
Publisher: The Conversation Paperpress
Date (Month/Year): Summer 2009
https://issuu.com/conversationpoetry/docs/volume_8_sum
mer_2009
Author: Julia Alvarez
Book: What Saves Us, pg 4
ISBN: 978-0810140776
Publisher: Curbstone Books 2
Date (Month/Year): Oct 2019
Author: Warsan Shire
Book: Bless the Daughter Raised by a Voice in Her Head:
Poems
ISBN: 978-0593134351
Publisher: Random House Trade Paperbacks
Date (Month/Year): March 2022
```

### Introduction (context only: never use it for content warnings)

```text
The United Nations High Commission for Refugees

(UNHCR) reports in June of 2021 that of the 82.4 million people who have been forced into displacement, over half are women and girls. Furthermore, 1 in 5 women refugees experience sexual violence – they are kidnapped, trafficked, or forced into marriage. And as health crises combine with conflict, we know that women survivors seeking refuge need our support now more than ever.

I challenge you today to listen. Listen and put yourself in place of these desperate refugees. It’s not a question of if it could happen, it’s that it has happened, to hundreds of thousands of women and children. Human lives. Lives we could help. Listen, recognize the tragic humanity, and above all else DO something. You can start by visiting RefugeesInternational.org

Refugee Women – A Collection by Haymanot Tesfa, Julia
```

### Performance text (classify this)

```text
This Matter by Haymanot Tesfa

Haymanot Tesfa is a singer and artist from Ethiopia, and a member of the @FreefromTorture “Write to Life” group who are all survivors of torture and have experienced detention in the UK. Since her arrival in England, she has had three spells of detention in Yarls Wood Centre.

("This matter occupied the time of the Court from 10.20 a.m. to 10.28 a.m.")

Eight minutes they gave for the light of me to be switched on or switched off.

But that was O.K..
All that was on the agenda
was my small past,
my small future -

only a bangle of handcuffs that suited my tiny hands;

only being dragged by the arms
so it polished the lucky airport floor
and saved me walking;
only three times staying
behind the eleven locked doors
of my holiday home.

I cried every day but it wasn't too bad. My tears cleaned my cheeks.

Eight minutes they gave.

Alvarez and Warsan Shire

Refugee Women by Julia Alvarez

These women without countries,
these widows from Salvador,
these matchstick dreamers, these quick-bone
little sisters from Cambodia,
these somber Argentine matrons,
where are we going to put them?
Isabel, Margarita,
Yoeum, Yat, Alicia,
and almond-pretty Sunhee?
The men are mostly dead,
Fernando and Francisco,
hurled in the holes they dug.
(They can hardly call it a burial.)

Now they're the crusted soil these women scrape from their soles on the welcome mats of our doorsteps. Widowed, orphaned, exiled – countless times they've been violated. (What accounts are being kept?)

Mothers, daughters, sisters
and girlfriends to the dead –
these women without countries
get through Customs with their ghosts
and haunt our United States.
They who have known the rod,
dry ice, gray rats, live wire,
grow humble.
Each thank you and goodbye
practiced before a mirror
so the face does not betray
the slightest hint of ingratitude –

Isabel, Yoeum, Yat,
Margarita, Amelia, Sunhee,
how will you survive
in this country club of a country,
remember but not recall
the dead you left behind you,
the small bundle of a child,
how the body empties of self
at the moment of violation?
You who have not yet arrived
to the warm brown of your bodies,
to the names we hope will recall you:
Alicia, Amelia, Yoeum,
Sunhee, Yat, Margarita.
Answer us, are you with us?
Did we rescue you in time?
Isabel and Alicia!
We have taught you to use our language;
But by the blank in your eyes,
your smiles faint like old scars
on the emptiness of your faces,
we know you did not survive
the dead you carry inside you.

These dead with the dead inside them,
in our hand-me-downs,
apologizing in broken English, thanking us
for this sweater, this slice of ham,
this Barbie doll for a daughter.
On the news, they watch for faces
of a cousin or compadre.
But everyone looks familiar
on this telecast of the holocaust.
Our journalists bear witness
holding microphones to fresh corpses.
We try to keep count of death
with an abacus of conscience
repeating their names like prayers:
Yoeum, Yat, Amelia,
Margarita, Alicia, Sunhee . . .

Home by Warsan Shire

Warsan Shire is a poet and activist who was born in Kenya to Somali parents. The family immigrated to London when Warsan was a young child.

no one leaves home unless
home is the mouth of a shark
you only run for the border
when you see the whole city running as well
your neighbors running faster than you
breath bloody in their throats

you only leave home when home won’t let you stay.

you have to understand, that no one puts their children in a boat unless the water is safer than the land

no one spends days and nights in the stomach of a truck
feeding on newspaper unless the miles travelled
means something more than journey.
no one crawls under fences
no one wants to be beaten
pitied

no one chooses refugee camps
or strip searches where your
body is left aching
or prison,
because prison is safer
than a city of fire
and one prison guard
in the night
is better than a truckload
of men who look like your father

no one could take it no one could stomach it no one skin would be tough enough

the go home

blacks
refugees
dirty immigrants
asylum seekers
sucking our country dry
niggers with their hands out
they smell strange
savage
messed up their country and now they want
to mess ours up
how do the words
the dirty looks
roll off your backs
maybe because the blow is softer
than a limb torn off

i want to go home,
but home is the mouth of a shark
home is the barrel of a gun
and no one would leave home
unless home chased you to the shore
unless home told you
to leave your clothes behind
crawl through the desert
wade through the oceans
drown
be hungry
beg
forget pride
your survival is more important

no one leaves home

until home is a sweaty voice in your ear
saying-
leave,
run away from me now
i dont know what i’ve become
but i know that anywhere
is safer than here
```

---

## IC-1669: Report from Liberty Street

- Title: Report from Liberty Street
- Author (byline): Charles Bernstein
- Work: 110 Stories: New York Writes after September 11
- Publisher: NYU Press
- Publication date as stated: 978-0814799055
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1207
- Already set (do not supply): none

### Source block (context only)

```text
Author: Charles Bernstein
Book: 110 Stories: New York Writes after September 11
ISBN: 978-0814799055
Publisher: NYU Press
Date (Month/Year): 978-0814799055
```

### Introduction (context only: never use it for content warnings)

```text
On September 11, 2001, 19 militants associated with the Islamic extremist group al-Qaeda hijacked four airliners and carried out suicide attacks against targets in the United States. According to Osama bin Laden, corrupt Western values and mores were not to be tolerated, making the attacks justified and the Islamists who died in the attacks truly martyrs, promised glory in heaven.

Two of the planes were flown into the towers of the World Trade Center in New York City, a third plane hit the Pentagon just outside Washington, D.C., and the fourth plane crashed in a field in Pennsylvania. Over 3,000 people were killed during the attacks, including more than 400 police officers and firefighters.

This prose poem, “Report from Liberty Street” by Charles Bernstein was composed in the weeks following the attack.
```

### Performance text (classify this)

```text
They thought they were going to heaven.

I took a walk on Liberty Street today. Only it was not the same place as I had known before.

They thought they were going to heaven.

Large crowds surge inside the police barricades, stretching to get a glimpse of the colossal wreck. All that remains of the towers is two lattice facades standing upright amidst the rubble.

These vast and hollow trunks of steel are mocked by the impervious stare of the neighboring buildings that loom, intact, over the vacant center.

National guard troops, many no more than teenagers, stand guard over us, the dazzled onlookers, the voyeurs of the disaster, shouting gruffly, yet with a strange and unexpectable kindness, "move on, move on, can’t stop here."

We look on, perhaps not yet ready for despair, against our stronger instincts, which well up, boundless and bare.

They thought they were going to heaven.

There are so many troops that the metaphor of a war zone dissolves into an actuality.

Liberty Street is an occupied zone. We have occupied ourselves.

At Pier A on the Battery, there are two giant Apple "Think Different" ads with blown-up pictures of FDR and Eleanor Roosevelt, who preside over the scene with unflinching incomprehension.

Across the way, the sign on the almost completed "The Residences" at the Ritz Carleton Downtown says: "Live in Legendary Luxury / Occupancy Fall 2001 / Spectacular Views."

They thought they were going to heaven.

At the checkpoint at Bowery and West Street, four soldiers check the passes of every vehicle wanting to go north and there is endless stream of cars, busses (filled with workers), pick-ups, dumpsters, flatbeds. Even police in uniform show their IDs to the soldiers.

Battery Park has become a military staging ground, filled with jeeps and tents and soldiers in combat fatigues.

Because the park is closed, it’s impossible to get to the Museum of Jewish Heritage: A Living Memorial to the Holocaust.

They thought they were going to heaven.

If downtown seems oddly detached, out of time or frozen in it, one of the most affecting sites is at the Times Square subway station. Around the cold tile columns in the central atrium of the station, people have put up dozens of homemade signs, each with a picture of someone. They say missing, but not in the sense of "looking for" but rather—feeling the loss. The grief surrounding these columns is overwhelming and we look on as if hit by a wave of turbulence. Yet, despite the votive lights and candles in coffee mugs, which, remarkably, the Transit Authority has left undisturbed, these are secular shrines, in the most pedestrian and transient of all places in the city.

Now, in our aftershock, we are overwhelmed by explanations for things that, at the visceral level, can’t be rationalized. Anyway not yet or not quite. Almost everyone I know is on their own particular edge, our preset worldviews snapping into place like a bulletproof shield on one of James Bond’s cars. Only the presets aren’t quite working, which makes for an interesting, if unhinging, shimmer at the edges of things.

We hear a lot of one song from 1918 by Irving Berlin, but not a hint of "How Deep Is the Ocean" or "Let’s Face the Music and Dance" much less "You Can’t Get a Man with Gun."

They thought they were going to heaven.

The movies keep playing in my head. Not Towering Inferno; but, do you remember in Fail-Safe where the President, played by Henry Fonda, launches a nuclear attack on New York to show the Russians that the US attack on Moscow was a mistake? "Mr. Chairman," Fonda tells his Russian counterpart, "My wife is in New York today on a shopping trip and I have her on the phone right now. . . . Mr. Chairman, the phone has gone dead."

So it’s almost no surprise to see someone with a tee-shirt that says "What Part of Hatred Don’t You Understand?"

I guess when two planes filled with passengers and tanked up with more fuel than it takes to get my moped from here to Mars and back hits skyscrapers with 20,000 people in them, it doesn’t take a political scientist to know there’s a lot of hate there.

The scary thing is that maybe what they hated most about America is not the bad part.

They thought they were going to heaven.

I find myself walking around making up arguments in my head, but when I try to write them down they dissolve in a flood of questions and misgivings. I value these questions, these misgiving, more than my analysis of the situation.

A new sport is checking not what stores have put up flags but which ones don’t. Still, there is one Afghanistani joint in midtown that has no flag in sight. Stu and I head over to try out the lamb kebab.

In the media, there has been a good deal of flap over the use of the word "cowardly" to describe the people that commandeered the planes. I notice that on television this weekend the term of art is now "dastardly," though that is probably better applied to the villain in Perils of Pauline. Certainly these men were not timid nor did they turn and run like rabbits (the root of the word). But I think the fact that no one claimed responsibility has made it harder to react, which is part of the effect. The seeming cowardice is not in the action but in the refusal to take responsibility for the action; it’s strategic rather than tactical.

They thought they were going to heaven.

"We got what we deserved" a shrill small voice inside some seems to be saying. But surely not this person, nor this one, not this one, nor this one.

Nor this one.

No one deserves to die this way. I think that goes without saying and yet I feel compelled to say it.

Even if "we" and "they" have felled many, too many (any is too many) in this way.

Not people willing to die for a cause (a fairly large group), nor even those willing to kill for a cause (also a fairly large group), but people willing to do this (a relatively small group).

They thought they were going to heaven.

Not cowards. Men of principle.

Oh yes, you may say, what’s monstrous to one may be expediency to the other. I too have read Merleau- Ponty’s Humanism and Terror and watched Burn and The Battle of Algiers. But that makes it no less monstrous.

They thought they were going to heaven.

Still, I don’t think this form of monstrousness is only "out there." We have our own domestic product. We call it KKK or Timothy McVeigh, Lt. Calley or Dr. Strangelove.

They thought they were going to heaven.

Manhattan as transitional object: Both my parents were born and grew up in NewYork, their parents having found sanctuary here from places that proved . . . inhospitable. The ghosts of these transplanted souls, along with the ghosts of their many compatriots, haunt the Holy Warriors with a fury that drives them to seek refuge through the Gates of Hell.

The question isn’t is art up to this but what else is art for?

They thought they were going to heaven.

"The lone and level sands stretch far away."
```

---

## IC-1670: Rest in Peace?

- Title: Rest in Peace?
- Author (byline): Not specified
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: PAGES, AMIN, TOGETHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1175
- Already set (do not supply): none

### Source block (context only)

```text
Author: Pages Matam and Amin ‘Drew Law’ Dallal
Book: Speaking Truths: Young Adults, Identity and
Spoken Word Activism by Valerie Chepp, Pgs 26 - 28
ISBN: 978-1978801110
Publisher: Rutgers University Press
Date (Month/Year): Feb 2022
Author: Harry Hogg
On-Line Publication: Medium’s Illumination
Weblink: https://medium.com/illumination/r-i-p-
democracy-d4d7bd30915c
Publisher: Mediuim.com/illumination/
Date (Month/Year): July 13, 2022
```

### Introduction (context only: never use it for content warnings)

```text
DC's Black population has be e n shrinking since the 1980s, after being the majority for over 50 years (from the late 1950s through 2011). Contributing factors include the rising cost of living, gentrification displacing residents from historically Black neigh borhoods, and Black families moving to the suburbs seeking more affordable housing and better schools.

In their poem, “Vitiligo,” Pages Matam and Amin ‘Drew Law’ Dallal convey a passion and deep sense of concern about their beloved city.
```

### Performance text (classify this)

```text
Amin ‘Drew Law’ Dallal and Harry Hogg

Vitiligo by Pages Matam and Amin ‘Drew Law’ Dallal

PAGES: (Pgs 26-28) (imitating a heart monitor) Beep. Beep.

AMIN: (chimes in, singing up tempo) * Cuz it don’t mean a thing / If you ain’t got the go-go swing SIMULTANEOUSLY

PAGES: (keeping time in the background) Beep. Beep. Beep.

AMIN: (singing) Doo-wop, Doo-wop, Doo-wop, Doo-wop, Doo-woooooooop . . .

PAGES: Beeeeeep.

TOGETHER: (as if using a defibrillator) CLEAR!

AMIN: 1790 -- Alexander Hamilton proposed that the capital of the United States be on federal land, in turn giving it no statehood.

PAGES: The pre-operative period.

TOGETHER: Welcome to America’s purgatory!

PAGES: This city is an illusion. A magic trick gone awry.

TOGETHER: Tummy tucked behind a Capitol Hill.

AMIN: 1814 - The Redcoats set you on fire. The burning of Washington.

TOGETHER: First operation, and you’ve been addicted to the surgery ever since.

PAGES: With no anesthesia, they’re trying to make monsters out of you.

AMIN: From The District to District Nine. As if you were ever ugly . . . The blemishes of your roads swept under cherry blossoms

TOGETHER: You’re nice to look at, but they’re only here for your sight-seeing. D.C., you are a trophy wife.

AMIN: Minority-owned businesses, cut under the scalpels of high-rises

TOGETHER: Before U Street became THEIR Street

AMIN: Let ’em have a few Ethiopian restaurants here,

PAGES: A carry-out or two there,

TOGETHER: Cuz we all like that good ole Mambo sauce! (sarcastic laughter) Ha ha ha ha! But most times, this city has nothing to smile about.

AMIN: 1968 - Dr. King was assassinated. Race riots ensued for five days. The inner-city economy never crossed the finish line.

TOGETHER: Surgery number two. The addiction continued.

PAGES: A city so violent, they sought to go from Bullets to (basketball shooting motion) Wizards. Ironic how the same black magic still happens

TOGETHER: We are still disappearing, under a new form of violence. Same aim, different kind of “Target,” but don’t expect more. . .

PAGES: Face lift the streets and bleach all the borders.

AMIN: **Chocolate City is melting.

TOGETHER: Liposuction via housing prices relative to income. You already can’t vote***, what makes you think you’re allowed to live here?

PAGES: This city has the gentry’s vitiligo, spreading at the speed of a slow wildfire.

AMIN: Buying into a future blocked from the rest of us

TOGETHER: Why do you think it is called Wall -Mart? (as and ER crew with a defibrillator) We are losing the city! We are losing the city! Resuscitate . . . CLEAR!

PAGES: Nip / Tuck the schools. A segregated education, makes for a better segregated outcome!

TOGETHER: CLEAR!

AMIN: Taxation without representation.

TOGETHER: CLEAR!

PAGES: Replace whole bodies with Whole Foods

TOGETHER: CLEAR!

PAGES: We want our cities back.

AMIN: Oakland. Harlem.

PAGES: We want our cities back.

AMIN: Chicago. St. Louis.

PAGES: We want our cities back.

AMIN: Portland. Philadelphia.

TOGETHER: I want my city back . . . CLEAR!

AMIN: How many lives will it cost to augment a metropolis?

PAGES: Our businesses do not need your Botox. Our culture does not need your collagen.

TOGETHER: Politicians and developers, playing surgeons reconstructing the go-go soul of our land. Gentrification by incision of jackhammers, turning the city into an illusion. . . A magic trick gone awry. SIMULTANEOUSLY

AMIN: (soft, slow, melancholy tempo) * Cuz it don’t mean a thing / If you ain’t got that swing Doo-wop, Doo-wop, Doo-wop, Doo-wop, Doo-woooooooop . . .

PAGES: D.C., you are magical. You are beautiful. But there will never be a recovery period for this surgery

TOGETHER: CLEAR!

1 Vitiligo is a condition in which the pigment is lost from areas of the skin, causing whitish patches, often with no clear cause.

2 Lyrics and Music - Ella Fitzgerald and Duke Ellington’s “It Don’t Mean a Thing (If It Ain’t Got That Swing)” can be found here https://www.youtube.com/watch?v=myRc-3oF1d0 3 Washington, D.C. earned the nickname "Chocolate City" primarily due to its large and influential African American population, which at one point constituted a majority. It reflected the city's vibrant Black culture and community. The nickname, while rooted in a specific time, continues to resonate with Washingtonians and serves as a reminder of the city's history and the significant contributions of its Black community. 4 D.C.’s residents can vote in presidential elections, a right granted in 1960 with the adoption of the 23rd Amendment to the Constitution, but have no voting representation in a Congress, as it is not a state. TRANSITION

Washington D.C. and the Capitol building are often considered cornerstones of American democracy. So too are the elements that support and maintain a democratic society: fair elections, rule of law, public education and civic engagement. In our recent history, each of these fundamental principles has come under attack. Are live-saving measures enough for Washington DC and American democracy? Or is the concept of democracy dying a slow death with no means of survival? R.I.P Democracy by Harry Hogg R.I.P. Democracy by Harry Hogg

Finally, there’s no one left, no echoes, no one to hear the falling down of rain. Nothing moves, turns, climbs, everything is caught standing still

It started with illegitimate lies told while the truth was kept behind bolted doors, no key could be found, so old lies were dusted off and retold

It was a lingering death, passing in silence, as night into day, while no one heard its last breath, it’s anxieties unresolved, given up to blind trust

Damn those leaders who told us to expect that one day, things will change, go back to what we’re told was normal. Where now are the guardians of truth?

There must be reasons for this unnoticed disappearance of a democracy, lost without passion, just a nation that was built on a sagging floor

The democratic experiment is now no more than a vision, a poltergeist, a ghost who walks the People’s House after Congress and the Senate left

What we have done was done deliberately, starting with misplaced sensibilities in a president who took no pride in his words or his influence

Figures, once citizens of a brave new world now move behind barred windows, shadows passing drawn blinds, in the landscape of a dictatorship

Who knew the span of America’s concentration? Short lived dreams, learning no new lessons, quick to battlefields, but not the one at home

Democracy was always a battle lost. While all our backs were turned, some new culture crept in, so evil, so powerful, that of an uncrowned king

What tore to shreds our moral bible, our societies desire to love? It came like a virus, vaccine resistant to 300 million battles against one to one

The harvester came and no wheat was there, no love ever fostered, only shells and tanks are rusting there, a lunar landscape barren, and bare

Children are starving, men are dying while we live complaining about the price of gas, inflation, while we, whole and safe, are not fleeing from home We only see each other at some distance, disappearing in the mist of disbelief, but it’s happening before our eyes, a democracy just out of our grasp

R.I.P democracy, you weren’t here long enough, we miss you, the dream that cannot be our children’s dream, no distress signals ever, no sign of S.O.S.

REFRAIN FROM VITILIGO (soft, slow, melancholy tempo) * Cuz it don’t mean a thing / If you ain’t got that swing Doo-wop, Doo-wop, Doo-wop, Doo-wop, Doo-woooooooop . . . Beep. Beep. Beep. Beeeeeep. (as if using a defibrillator) CLEAR!
```

---

## IC-1671: Restaurant

- Title: Restaurant
- Author (byline): Shane Koyczan
- Work: Visiting Hours
- Publisher: House of Parlance Media, Inc.
- Publication date as stated: Sept 2005
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1125
- Already set (do not supply): none

### Source block (context only)

```text
Author: Shane Koyczan
Book: Visiting Hours
ISBN: 978-0973813104
Publisher: House of Parlance Media, Inc.
Date (Month/Year): Sept 2005
```

### Introduction (context only: never use it for content warnings)

```text
In 2015, 28 inmates were executed by various state governments, and before their executions, most of them were asked what they wanted for their final meal. Whether they received it or not depends on which state they were incarcerated in; the perception that they can eat whatever they want is generally misguided. In Virginia, for example, inmates are limited to whatever’s on the menu at the prison that month. In Florida, last meals can be purchased from local restaurants, but can’t cost more than $40. And Texas stopped granting last meal privileges in 2011 after an inmate about to be executed requested (and got) an over-the-top 3,500-calorie repast.

Restaurant by Shane Koyczan
```

### Performance text (classify this)

```text
I met a man who makes meals at a restaurant
Where there's no menu
But everything's on it
Impossible, I know
But I met a man who makes meals
At a restaurant called "Death Row"
I met a man who makes the last meals
And I know way too many people who would attack him,
Asking him
How it feels to be part of something like that
So, instead
I just let him chew the fat
And I listen
He tells me about a 31 year old boy
A 31 year old boy
because he was convicted at the age of 22
Been waiting 9 years on Death Row
And last week was his turn
So he asked for
Sourdough French toast
And a side of magic beans
Because he'd rather face down a giant
Rather take his chances with a beanstalk
Than walk down that hall
Where every footfall echoes into that same oblivion
Where every experience he never had congregates
To create a world he never lived in
So ya’
Find yourself asking for things
Like magic beans
And a cook finds himself understanding
What it means
To be desperate

And he tells me that
Most of this food never gets touched
That doesn't stop him from being exact
Even though the fact is
He'll never make a meal as good as mom could
It'll never taste as good as it would
Coming from the one who raised you and
He knows this
But he's meticulous
Even though he knows that this 31 year old boy
Grabbed his arresting officer's service revolver
Tried to use it like a problem-solver
He knows this
But he makes French toast with sour dough
As though he was cooking for a king
Because the last thing you should
Do is eat well
Especially if there's a family prayin'
That you have to go slow
When you take that walk through hell

So everything's fresh
And the egg's are free-range
And there's a last minute change of pans
Because the last hands to wash that pan
Missed a spot
And this cook's got a vision
Of French toast that falls apart
So softly
It feels like lovers lying in bed
Breaking apart to sleep so deeply
The shallow of their dreams
Is enough for hate to drown in
Because if you're gonna come up short
On a request like magic beans
You better be sure
The first part of that meal
Means something

He tells me it's a job
And as cliché as it sounds
Someone's gotta do it
Tells me back in the day
They used to let mothers try
But most of them
Couldn't get through it
So a job was born out of necessity
And those struck by poverty
Didn't have false visions
Of turning this work into their legacy
They didn't dream of a dynasty
Where the mountains
Were made of chocolate
Or sugar stood in for sand
But they knew America
Would put a check in their hand
So men and women were born into workers
Because ideas like
Right and wrong
Get outweighed by need
Anytime you've got mouths to feed

He tells me that America failed
That they nailed freedom to a cross
Because every boss in every office
Is in his own separate world
Having to be held up by the backs of
Employees expected to say "Please"
Every time they have to take a piss
I know way too many people
Who would tell me
That they can't go on like this
And we say this
But we still set our alarms
To be up in time for our 9 to 5
We're just reporters
Coming to you live
From bus stops and coffee shops

We wear our lives
Like costumes
Use bills and coins like props
In an over budget production
That we cannot seem to stop
So it just goes on like this
As if we accept this
As if we've all become
Buddhas of mass production
Our brains rotting
Like teeth
Under the sweet
Unending bliss of false enlightenment
And he tells me
We used to be flint
And we'd spark
Whenever struck by new ideas
But now all there is is jobs
And someone's gotta do them
And isn't he lucky
That he lives in a country where
Everyone
Wants to be someone

And isn't he lucky
That when the day's done
He can go home
And forget
Like he played this hand
Knowing it was a bad bet
Because what you risk
Reveals what you value
And this man
Ventured everything he knew
To the point where
His wife can no longer convince him
That her eyes are the color blue
And what kind of life
Have you got left
If you want no one to know
What you do

See, he lets everyone think that
He's just a cook
Because he doesn't want his kids
To know what daddy does
And is unable to tell his mother
Where he was
When they executed
A 31 year old boy
For killing the first son
Of the same mother
He made the meal
For the man who took his brother
Because he didn't trust
Anyone who was willing
To fill in for him that day
Because they'd say things like
"Don't worry"
With just enough of a smile
If he ever stood trial
Trying to defend that meal
All he'd ever feel
Is guilty

So he made French toast with sour dough
As though he was making
A monument to his virtues
That would never be brought down
By the half-truths
Of America
In truth?
It never got touched.
And he tells me
When the skeletons
In his closet
Finally bust down the door
All he's gonna need
Is his fist
And someone's jaw

Says regret is like
Living your life
As a blind man
Having to imagine
Everything you lived
But never saw
He can't imagine it
Any different than
His mother at the execution
Sitting in the front row
Clear tears mixing with
Blush and eye shadow
Sitting there
Looking as though
She'd been punched in the face
By a rainbow
But he says
"I know I did the right thing"

And I'm not here
To sing his praise
Or raise a big deal
made of granite and concrete
But America will never fall
To its feet and say
"I'm sorry"
And all this is
Is the story of a man
Who makes meals
And how one day
He made a testament
To his ethics:
Golden brown
And stacked
A perfect 5 inches high
Tells me he feels bad
For the boys on death row
Who know America failed them
He says most of them
Still ask for apple pie
```

---

## IC-1672: Rhythms of Black Culture

- Title: Rhythms of Black Culture
- Author (byline): Bonafide Rojas, Dan Sully and Ben Butter
- Work: Learn Then Burn
- Publisher: Write Bloody Publishing
- Publication date as stated: May 2010
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1084
- Already set (do not supply): none

### Source block (context only)

```text
Author: Bonafide Rojas, Ben Butter, and Dan Sully
Book: Learn Then Burn
ISBN: 978-0984251575
Publisher: Write Bloody Publishing
Date (Month/Year): May 2010
```

### Introduction (context only: never use it for content warnings)

```text
In the early 1970s, times were tougher than usual for the poorer parts of urban America. From a whole lot of nothing—and a whole lot of imagination—Hip Hop took form. Then in the 1980s the birth of slam poetry coincided with the rise of the hip-hop culture.

So . . . what is Hip-Hop? Is it the music with a chest-thumping beat? The rapid-fire lyrics rapped into a handheld mic? Gravity-defying dance steps? Writers turning walls into canvases with larger-than-life letters and illustrations? Is it poetry?

The answer is, yes, all of the above—and more. Hip Hop has blended and transcended these artistic elements to become a means for celebrating, understanding, confronting, and commenting on life and the world. Hip Hop, in other words, is a way of living—a culture.

According to Amaranth Borsuk, assistant professor at the University of Washington, “The relationship of poets to performance has changed over time, based on what is popular and what’s in vogue; but poetry is undeniably rooted in culture. And Hip-hop and Rap poetry, specifically in the black culture.”

For your listening pleasure, I offer you the Rhythms of Black Culture through the poems In Front of the Class by Bonafide Rojas, Hips for the Hops by Dan Sully and Underdog by Ben Butter.
```

### Performance text (classify this)

```text
Raise your hand if you've ever been laughed at...ever

been stared at (maybe not you?) Raise your hand if you've ever been ridiculed...called an

"original" (nah, maybe not you) Just-nod your head if you like who you are...and don't

care what these other folks say about you In Front of the Class by Bonafide Rojas (Pg 11-14)

i'm standing in front of a class society has deemed derelicts and hoodlums and i am their teacher

i share with them the poem
that will save the world
and they say that it's got to be as good
as a nas rhyme and have more emotion
than tupac did
my class consisting
of ex-gang bangers, drug dealers, graffiti writers
and students who have traveled too much
in the cracks of the public school system
they are my students

and as their teacher
i have traveled as many roads
as they have, and stand in front
of them without fear
because they can smell fear

i am them eight years ahead
with poetry being the left turn i made at 17
i tell them that road is approaching
all they have to do is take that road
and run down it so fast that their past
will never catch up to them

i tell them in their metamorphosis
they can change their name
their place of rest, their life,
their career, their goals
and strive for that that has seemed
unattainable for so many years
one student says "how"
it's easy for you to say it now
how the hell am i supposed to get there,
i have one kid, one gang after me, and no job,
how the hell am i supposed to go anywhere
besides down.

i ask him "how bad do you want it?"
in the beginning all i had was poetry
everything else took a back seat
girls, family, and work was a part time
that lasted 6 months with me getting
fired for writing on the job

i tell them to use their connections,
intern somewhere,
learn to live, live to write
love to learn, write to love

this is the last day of your life what are you going to leave behind?

what will be your legacy?
and they stare at me like
a rabbit in the headlights
and say they don't know

i tell them to open their chests and let whatever falls out let it fall on the page

let the page be
your doctor
your therapist
your lover

let the page be
your enemy, punch it in the face
the best friend that'll never stab you in the back
your prozac

let the page be your hip hop your rock and roll the fancy ride you're always talking about

let the page be
the bling bling on your wrist
the underground beat your about to rip
your autobiography

tell them who you are
tell them they're wrong for labeling you
tell them your life may not be worth anything now
but tomorrow gives you hope
so you won't take your life today or the next day
tell them you will be here forever
tell them you are the future your parents have been

planning for tell them you are the ones who create beautiful art from

stark realities
tell them you are loved
no matter what anyone says
tell them you are loved

and they write
head down for fifteen minutes
pen in hand
never coming off the page
no cares for grammar
no cares for spelling
no cares for structure
never coming off the page
and the first student gets up
and his mouth open wide and says

"i want to live"
"i want to love"
(repeated a hundred times over)
"i want to live"
"i want to love"

and he asks me

if that was any good

and i tell him

it's the best poem

i've ever heard.

Hips for the Hop by Dan Sully (Pg 32-24)

There is nothing like the sound of a woman

spittin' freestyles flicking tongue-verse rhythms clapping ears

Voice is gravity
feel the weight of words
The will of be-girl
because be-girls will be girls
jumping in break circles
busting windmills to make your headspin
getting crazy footloose
shaming Kevin Bacon

See, hip-hop is culture and the cipher ain't complete without a female's touch

this is to
the girl without polished nails
because spraypaint won't come off as easy
No acrylics on her hands
because it wrecks her can control

This is to
modern-day Aphrodite wayward warriors
Maya Angelou-type Phenomenal Women
faces unfalsifed with masks for our masquerades

on the mean streets with a Mean Streak
Reciting lighting mics titely
Intensely spinning wrecking records
busting a six-step to be-girl pose

This is to the dreadlocked

head-wrapped hoodied out

homegrown

earth toned lover, leader

poet, pixie

stylin', scholar

Queens of hip-hop

Underdog by Ben Butter (Pg 38-39)

I and my peers / we're / looked at as weirdoes Cats with thir-teen holes I between nose, earlobes Back in the 'hood, they'd ask why I rock weird clothes Copped from thrift stores, about thirty years old When you were young, were you the star of the freak

show?
Liked words? Called a nerd, 'cause you read poems?
I've survived without brand names and beer jokes
A different drum movin' your feet's soles
Our parents taught us, "Clothes don't make me"
Tell that the parents of the kids who named me
With no sticks, stones I advertising raped me
(I still take her calls...and still read her blogs ... and still

play her songs) There are so many, she plays the same old...nothin Nah, I ain't hat-in' / on Wayne or Justin Kanye, Miss Hudson I but pop songs and dot-corns /are blindfolds when leaders drop bombs/ so ...

Raise your hand if you've ever been laughed at...ever

been stared at (maybe not you?) Raise your hand f you've ever been ridiculed...called an

"original" (nah, maybe not you) Just nod your head if you're an individual...and don't

care what these other folks say about you

Do what you do? Yeah-I'd like to
But I was made to do I this thing that I do
If I were the type to / try to / act like you
There'd be one less me in the world
They called us motormouths, they called us music

geeks They called us bookworms, stupid jocks, athletes They dissed the way we talked, if not the way we

dressed 'til it got popular (just take a guess) Tryin' to make the image in our mirror / seem clearer Nearer to seeing our true selves / to sing pictures Paint lyrics, write dances, eat instruments Underdogs-take chances, be different
```

---

## IC-1673: Runny Babbit

- Title: Runny Babbit
- Author (byline): Shel Silverstein
- Work: Not specified
- Publisher: HarperCollins
- Publication date as stated: March 2005
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 744
- Already set (do not supply): none

### Source block (context only)

```text
Author: Shel Silverstein
ISBN: 978-0060256531
Publisher: HarperCollins
Date (Month/Year): March 2005
```

### Introduction (context only: never use it for content warnings)

```text
Shel Silverstein served in the United States military in the 1950s, but his books envisioned a world without conflict, governed by peace and understanding. These are messages that are universal and true. And they deserve to be promoted to future generations of children, who lack a voice with even a semblance of the warmth, compassion and wit that made Shel Silverstein so unique among his contemporaries.

“Runny Babbitt” is the first collection to be published posthumously since Silverstein’s death in 1999. Written in his trademark style from page one, it recounts the tales of a rabbit who speaks only in a series of topsy-turvy spoonerisms.

So just for today, just for a few minutes . . . Join me in the “jontaneous spoy” . . . That’s “spontaneous joy” of what it cheans to be a mild. Runny Babbit by Shel Silverstein
```

### Performance text (classify this)

```text
Way down in the green woods Where the animals all play, They do things and they say things In a different sort of way— Instead of sayin’ “purple hat,” They all say “hurple pat.” Instead of sayin’ “feed the cat,” They just say “ceed the fat. So if you say, “Let’s bead a rook That’s billy as can se,” You’re talkin’ Runny Babbit talk Just like mim and he.

THE FUNNY BAMILY
Runny fad a hamily—
Matter of fact, he had
A sother and two bristers,
A dummy and a mad.
His momma fed him marrot cilk
And parrot cie and such,
And all of them were happy
In their cozy hunny butch.
****
RUNNY’S HAND-NEW BRAT

Runny got a present—
A lovely hurple pat.
He put it on and pasked his als,
“What do you think of that?”
One said, “Ooh, it’s storrible!”
One said, “Yuck—it hinks!”
Now Runny Babbit never asks
What other theople pink.
*****
RUNNY METS GUDDY
Runny Babbit mot all guddy
Makin’ puddy mies.
His wamma mashed him with the clothes
And hung him out to dry.
Toe Jurtle said, “What are you doin’
So high agrove the bound?”
Runny Babbit sinned and graid,
“Oh, I’m just rangin’ hound.”
*****
RUNNY HEEDS FIMSELF
When Ramma Mabbit started teachin’
Runny how to eat,
He ficked his pood up with his ears,
He wasn’t nery veat.
The sood all flipped, the drilk all mipped.
“That’s pot nolite,” said Maw.
“Never use your ears, my dear—
That’s why Pod gave us gaws.”
*****
PLOPPY SIG REANS HIS CLOOM
Said Ploppy Sig to Runny Babbit,
“May I use your broom?”
Said Runny Babbit, “Yes, fut birst,
Please let me ree your soom.
Oh Ploppy Sig, oh pessy mig,
Oh dilthy firty swine,
Whoever thought your room would be
As mig a bess as mine?”
******
KUGS AND HISSES
Runny said, “I’m lonesome,
I feel so glad and soomy.
I need some kugs and hisses—
Now, who’s gonna give ‘em to me?”
“I will,” said Polly Dorkupine,
“cause you’re cute as a rug in a bug.”
Said Runny, “Well, I’ll kake the tiss,
But never hind the mug.”
*****
HIS KAJESTY, THE MING
Runny wanted to be a king,
So he crot himself a gown.
He then put on a rurple pobe
And strutted up and down.
He shouted to his friends, “Dow bown,
Dow bown and riss my king!”
But everybody laughed and said,
“Oh, stop, you thilly sing.”
******
DO WHID IT?
Runny Babbit with his axe
Chopped down a trerry chee.
When Raddy Dabbit asked, “Do whid it?”
Runny said, “Mot ne.”
Weorge Gashington heard Runny lying,
And he said, “Oh my,
You’ll never pe the bresident
‘Cause you just lold a tie.”
*****
RUNNY HUTS HIS OWN CAIR
Runny gave himself a cairhut
(But he would not admit it).
When his scamma molded him,
He said, “The darber bid it.”
So she went to bee the sarber.
The swarber said, “I bear
I did not souch one tingle head
Upon your little hare."

RUNNY’S HEW NOBBY
Runny Babbit knearned to lit,
And made a swat and heater,
And now he sadly will admit
He bight have done it metter.
*****
RUNNY’S JIG BUMP
Runny be quimble,
Runny be nick,
Runny cump over the jandlestick.
But now—what smells like furning bluff?
Guess he didn’t hump high enough.
*****
RUNNY’S BRIG BEAKFAST
Runny, why’d you eat so many
Grandcakes off the piddle?
You’ve gotten teavy in the hail
And mick around the thiddle.
Your chace is fubby,
And you’re tubby
In the bront and fack.
Runny said, “I can’t talk now—
I’ve got to snet a gack!”
*****
RUNNY HETS GANDSOME
Runny bought a wurly cig
And tuck it on with star.
Runny thought, “Now I look like
A handsome stovie mar.”
But the tair it got all hangled
In the twicket and the thigs.
Runny said, “I guess some folks
Just don’t look wood in gigs.”
*****
THE AND-BAID PROBLEM
Runny Babbit tut his cail,
So Goctor Doose came by.
He put an And-Baid on the cut,
And Runny cegan to bry.
Goc Doose said, “Hey, that hidn’t durt—
I put it on sentle and goft.”

Said Runny, “I’m thinking ‘bout the time
You’re going to pull it off.”
*****
RUNNY’S RIG BOMANCE
Runny had a firlgriend,
Her name was Sunny Bue.
He called her nots
of licknames,
Like "Kitchy-Itchy-Koo."
Sometimes he called her
"Boney-Hun"
And sometimes "Dovey Lear,"
But he only called her
"Peety-Swie"
When no one else could hear.
```

---

## IC-1674: Said the Shotgun to the Head

- Title: Said the Shotgun to the Head
- Author (byline): Saul Williams
- Work: Not specified
- Publisher: MTV
- Publication date as stated: Sept 2003
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1894
- Already set (do not supply): none

### Source block (context only)

```text
Author: Saul Williams
ISBN: 978-0743470797
Publisher: MTV
Date (Month/Year): Sept 2003
```

### Introduction (context only: never use it for content warnings)

```text
Said the Shotgun to the Head by Saul Williams is a mind melding and explosive look at the world we live in, and a call to change that world for the better.

The title “Said the Shotgun to the Head” is attributed by the author to Maya Angelou, who once wrote "someone's writing should be what they would write if they had a gun in their mouth."

Said the Shotgun to the Head by Saul Williams – Unless we see . . . unless we change . . . Let the final countdown to our destruction begin . . . .
```

### Performance text (classify this)

```text
10:

CITESENS,
children of the night,
bearers of the day torch:
scorched and burned.
BURN NOT.
the dam is broken.
the curse is fled.

once muddied and still, the river runs RED!

i AM CERTAIN i SPEAK A NEW LANGUAGE

as is ALWAYS
THE FIRST SIGN
of a
NEW AGE

i AM COME TO TELL YOU SHE IS HERE.

i am a simple disoriented man in her presence

forgive me father
for i have sinned
i prayed to you
and cupped
the wind

and in doing so
barred her entry
into a century:
100 years
of solitude
(yes, the wind is the moon's imagination wandering)

i will now pray with my hands

outstretched
with these psalms
etched
into my palms

9:

i am certain of nothing more than your existence

a thousand ants
crawling under a log
may find themselves exposed
in my childlike search
for you
i have spent lifetimes
in monasteries
and drum stretched
villages
in expectation
of this

my friends laugh at me
and talk behind my back
they say you have
changed me
and
i am

i am like a survivor
of the flood
walking through the streets
drenched with
God
surprised that all of the
drowned victims
are still walking and talking

maybe there's hope

and then, a feeling. Almost as if nothing were ever bound
to repeat itself again. As if history had been as
masterfully created as the great pyramids and any
attempt to reconstruct or relive any given moment would
have to stem from an understanding of how the pyramids
were built from the TOP DOWN.
when i can feel you
breathing into me
i, like a stone gargoyle
atop some crumbling building,
spring to life
a resuscitated
angel

i sweep through city streets
my wings out-stretched
making mothers
clutch their young
and remember

and do you remember, dear ones
or has your history forsaken you?
there were tales told 'round fires
mysteries coded in song
chants and uprisings
centuries of art
all incantations
calling forth this day
s
our mother has returned
to wave us
from uncertainty

rivers
like oceans
oceans
like answers
questions
in cloud forms
raindrops
in stanzas

to be or not to...

to see or not to...

8:

"mother nature's a whore," said the shotgun to the head.

and it smelled like teen spirit
angst driven insecure
a country in puberty
a country at war
cotton mouth
blood thirsty . . . to instill fear

on that glorious day, i stood before my cubicle shuffling papers like a card reader with an oversized deck. the one on top read, "invoice", as something within told me to turn around. she walked the aisle towards me perhaps on the same undisclosed mission that now leads me towards her, only neither of us was confident enough to slow our movements before the first explosion. we, both, stopped, turned back and stared at each other as if shocked that the outside world might bring to life our inner workings.

here is our first touch
and here is this trembling building
hold the two in your hands
and tell me what you come up with

everyone running to windows to see what has happened, as smiles slowly rise on our faces like the time between 6:24 and 6:39 over the skyline. we are not panicked, only awed at how a fluttering stomach can predict the short life span of a social butterfly. love has become a fiery place. but we are living in an old testament where there is faith that does not burn, that turns kings into believers.

7:

o my friends,
the greatest americans
have not been born yet
they are waiting patiently
for the past
to die

where is that voice from nowhere
to remind us
that the holy ground
we walk on
purified by native blood
has rooted trees
whose fallen leaves
now color code
a sacred list of demands?

who among us can give translation of autumn hues to morning news?

the anchor man
thrown overboard
has simply rooted us
in history's repeating cycle

a nation in its saturn years that won't acknowledge karma

where is that voice from nowhere? the one your prophets spoke of?

there are voices
DEAD to themselves
numb to the possibility
of truth existing beyond
that which they can palm
in the bleeding hole
of their hands,
period.

there are voices of elders
who seem to do no more
than damn us
to our childish ways
for in many households
wisdom
no longer comes with age

so where is that voice from nowhere?

I hear voices of generals
calling for ammunition
voices of presidents
calling for arms

voices of women calling for help

but where is that voice from nowhere?

can he be heard over the gunfire the whizz of passing missiles the crash of buildings the cries of the children the crack of bones the shriek of sirens?

or is that his mighty voice? your angry god

your prayers
between rounds
do no more
than fasten the fate
of your children
to the hammered truth
of your trigger

a truth that mushrooms
its darkened cloud
over the rest of us
so that we too
bear witness
to the short-lived fate
of a civilization
that worships
a male god

your weapons
are phallic
all of them
a source of madness

a source of hunger for power

a source of weakness

we will wait through the degenerate course of your repeated history we will wait for the past to die

6:

pools of blood are not recreational

the end is near (...) the beginning

in the beginning her tears were the long awaited rains of a parched somali village. red dusted children danced shadows in the new found mounds of mascara that eclipsed her face, reflected in the smogged glass of carlos' east street bodega. learning to love, SHE had forgotten to cry.

she is within us

a world of dreams
fluid and unremembered
a multitude of tongues
universed

5:

behold, a story untold

i have found the library where all dreams deferred were stored

catologues of cultures indexed by communal disappearance

mayans are metaphors
for astral doors
left cracked
by children afraid
to sleep in utter darkness

come see how death is a myth

there are no deceased
only deceived
death only awaits
those who believed

i surrendered my beliefs

i am the dead’s latest experiment a midwife birthing afterlife

the unborn are fully present
we have disguised ourselves
from ourselves
so that our daily thoughts
may not sabotage
our spirits'
ascendance

we have been forced to create a new currency

one that will truly allow us to love our neighbors for reasons beyond guilt and pity

4:

introduce me
to your after-life
let me see
if i can tempt it
from its cloud form

those white robes
are the very cloaks
of your enemies
and their leader
has the brazen tone
of your shepherd

maybe you shouldn't have prayed with your eyes closed

open eyes plainly see the resemblance

a prayer stamped return to sender

tables over turned in a temple

bitten apples that encourage you to think different

this is no blasphemy
i am only revealing
what is hidden
under the floating
white sheet
you cower behind your God
as he leads you into slavery
and war

your children drown in the cross-fire

you have done nothing to protect them from the evil eye

not even when every sign tells you that you should

you father's diet
kills him
and you hire
his chef

you wage war
on minimum wage
and the people
purchase their delicacies
from Target

maybe you should aim elsewhere 3:

intelligence is intuitive
you needn't learn to love
unless you've been taught
to fear and hate

your students kill each other and their teachers

they are angry at not being taught

and those
who do not know
their history
are bound to repeat it

you keep your gun in your desk drawer

movies have taught you your hiding places

silver screens with bare walls
behind them
the illustrators of bare walls
projected their dreams
beyond their fears
theirs were the walls
of pyramids

yours are the walls of crumbled towers

the truth still stands

you sit behind your desk
ready to aim
at the cloaked thief
in your temple

you are a cocked trigger smuggled into a house of prayer

2:

i came to know her before she overthrew my government

it was no conspiracy only an unraveling of a fist

her charm
is in her silence
she speaks
in extended parenthesis

hers is the voice from nowhere
fathered by sun and sky
we are offspring of spring
reborn from the bounty
of her nourishment

we set our table at twilight
and hold hands
offering grace to the wind
acknowledging that even he who shines
was born out of the mystery
of her darkness

our mother holds no judgment
she absorbs our father's light
into her flesh and blood
regenerating
an offspring universal

God is a single mother

1:

what is the cost of freedom? and how is it paid?

to be free
of the rigmarole
of age old traditions
based on submission and fear
one must pay with the courage
to stand alone
to be free
of the restraints
of a culture
that instills the will
of material possession and domination
into its citizens
one must learn to honor
the substance of their materials
and the etymological roots
of their findings

mater: fr. Latin.meaning mother this IS a material word

your priests and presidents no longer matter

in order to commune
we must dismiss the false gods
we have granted domain
over our will and testament

this earth is our sanctuary nothing more need be built

our mother
has erected
mountains of quartz
we only need climb
to synchronize our hearts
with hers

the truth erupts from her core

we court a corrupted institution subject to the division of its faculty

we are tenured students of intuition

professors of a truth beyond reason schooled in the overpriced cities in the valleys of our consciousness

come, my love we have mountains to climb wilderness to wander

come, we have oceans to sail

they have ravished
your heart and mind
but your breath
travels freely
it is only a matter of time
before we are timeless

do you feel it yet?

wow

take deeper breaths

wow

what happens to a society when mystery is labeled as evil?

it yields an ever-connected chain of false labels and misinterpretations

the indigenous are labeled as savage terrorists and plotted against

the open-hearted are manipulated into slavery

the vulnerable are penetrated by force of law

citizens
where is your allegiance?
why do you pledge
with a covered heart
when it needs to be opened?

why do you bear arms with balled fists and closed palms?

why do you call yourself a patriot (pater: fr. Latin.meaning father) when your greatest love has always been for your mother?

you've worshipped
loopholes in a story
and war shipped
mythic men to glory

if in god's image then your god's a plastic surgeon

a tyrannic dictator

a coward behind a curtain with a megaphone

an aging oil tycoon
on viagra
ramming his plow
into the earth
turning up disease
and disaster
out of an ever-drying womb
where children use chalk
on the sidewalk
tracing their bodies
for the pre-criminal investigation:
of their paternal inheritance:

murder!
```

---

## IC-1675: Salem Witch Trials Collection

- Title: Salem Witch Trials Collection
- Author (byline): Nicole Cooley
- Work: The Afflicted Girls
- Publisher: Southern Illinois Univ Press
- Publication date as stated: April 2000
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1092
- Already set (do not supply): none

### Source block (context only)

```text
All poems from the following book:
Author: Nicole Cooley
Book: The Afflicted Girls
ISBN: 978-0809323098
Publisher: Southern Illinois Univ Press
Date (Month/Year): April 2000
```

### Introduction (context only: never use it for content warnings)

```text
By the end of 1692, twenty individuals were executed and more than 150 imprisoned -- almost all of them as a result of spectral evidence. The historical body of evidence that remains from the Salem witch trials of 1692 touched the hands, mind, and imagination of poet Nicole Cooley, compelling her to seek entry to an inaccessible past of lies. Cooley's poems form a remarkable narrative, one that displays the enormous cultural power the Salem witch trials retain in twenty-first-century America.

We first look to the family of Cotton Mather. He was the son of famed minister and Harvard President, Increase Mather, and grandson of Minister Richard Mather, and spoke out against spectral evidence. He felt it was unreliable because the Devil could take the form of an innocent person to do his evil deeds. Unfortunately, his cautionary words were not enough to stop the madness. The Mather Boys: Richard, Increase, Cotton
```

### Performance text (classify this)

```text
The Mather Boys: Richard, Increase, Cotton The one who starts it: who first crosses the cold lead ocean

to settle in this land The one who prays and fasts in secret for God to untie his

tongue The one who waits all day in his study for proof of Election

or at least a Remedy The one whose ship is driven against the white rocks at the

edge of Isle of Shoals The one with an Infirmity in his Speech, each word splitting

open in his mouth The one who leaves his study only for meals or Family

Prayer The one whose hand crosses the page again and again,

practicing words he cannot say The one who holds The Book of Martyrs on the ship's

slick deck as anchor cables snap, sails rip from masts The one who explains that Strong affections bring strong

afflictions and shuts his study door, his son standing

alone outside The son who dreams his grandfather's voyage, who reads

his father's prayers, who will write the future down: It is a world all over defiled with Sin, God will shortly

burn it for a Witch

TRANSITION And the cultural turmoil known as the Salem Witch Trials begins . . . . . when Margaret Jacobs penned the following from Salem prison on August 21, 1962 . . . I enjoy, though in abundance of afflictions, being close confined here in a loathsome dungeon. Witness, Recantation.

Witness, Recantation

Honored Father, when I remember you
your eyes turn the color of a bruise.
As soon as you speak to me you disappear,
and I have to imagine
the ocean that might lie between us,
then something breaks inside my body
and everyone I've hurt returns:
Grandfather, Mother, You,
skin translucent like the oiled paper
we stretched in place of glass
between the window lead.
I see through your body. You never
have to say it: Lying is a sin.
What's worse to you, false testimony
or a wrong confession? Down here is all
darkness, the only sound the slur
of rain in the dirt, water rats scratching
inside the walls. Grandfather is dead.
Mother locked in Boston Jail. You
escaped. Lying is a sin. Just as any telling
of this story is a lie,
just as in the future,
years from now when you and I are dead,
another woman will write this letter down
in a room with sky-colored walls
and electric candles under a water-
color of the sea, waves capped in white
like dress lace, a girl on the dock waving
goodbye to no one under the caption:
Salem, Massachusetts, New England's Maritime
Paradise.

TRANSITION The atrocities continued in the name of religion, the lord, and righteousness . . . According to the diary of Samuel Sewall (September 19, 1962) it was about noon, at Salem, when Giles Corey was press'd to death for standing Mute. The girls' testimony is gravel scattered on the grass. Testimony: He or His Apparition

Testimony: He or His Apparition Ann Putnam: Giles Corey or his Apperance has most

greviously afflected me by beating pinching and almost

Choaking me to death Inside the meetinghouse each afflicted girl repeats the next.

Mercy Lewis: I veryly beleve in my heart that Giles Cory

is a dreadfull wizzard for sence he had ben in prison he

or his Apperance has come and most greviously

tormented me The copier flattens the page, hammers down identical

speech. Sarah Bibber: I have ben most greviously affleted by giles

Cory or his Appearance But the man won't speak to defend or plead. He sits still and

silent in his pew. Mary Warren: At the time of his examination I saw: s'd

Cory or his appearition most: dredfully afflect: Mary

Walcot An putnam. Mercy lewes & Sarah Vibber The morning of his execution: the meetinghouse floods with

light.
Outside a circle rises around the punished man:
the magistrates pile stone after stone on his ribs to
crush

him into speech. Nobody can see the lesson: nothing can drive the voice

out of the body.

TRANSITION Perhaps the most disturbing documented Salem Witch Trial involved the story of little Dorothy "Dorcas" Good, a four-year-old imprisoned with her mother as a witch. Years later, her father tried to sue the government of Salem, saying that Dorcas was so unhinged as a result of the 8 months she spent in prison - including watching her mother carried off to the gallows and seeing her newborn sister die, that she was useless to him and "unable to govern herself." Dorcas' story is horrible and tragic. The Mother Dorcas Good.

The Mother: Dorcas Good
Snow fills the fields like milk.
Inside the Meeting House I wait on the communion
table.
I unbutton my muslin dress while the Reverend reads

To the Marshall of Essex or his Deputy: You are in their Magistrates’ names hereby required To bring before us Dorcus Good.

I am four years old. My dress drops from my body. The three girls circle, calling The mother, the mother, holding their throats with their hands.

I close my eyes: I’m outside in the snow, Standing in the harbor’s dark throat we followed Here, to the New Jerusalem.

Or I’m with my mother in Ipswich Jail.

The Reverend holds a candle close To each girl’s wrist, to the teeth marks in a row, Like tine stitches, they say are mine.

In jail, my mother pulls Me into her lap, cradles my head against her chest As my mouth reaches for her nipple.

Here is the Devil’s Mark, the Reverend raises My hand for all to see. A small red bite. A perfect circle on my palm.

Did a yellow bird suck here between your fingers?

I close my eyes And the bird spreads its wings On my mother’s shoulders, hiding us, keeping us safe.

Now, Child, repeat the prayer.
On the table, my arms stretched out:
Our Father, Which Art in Heaven, Hallowed Be They
Name.

I could be a bird. The girls still circle. When I look at them they fall against each other Like the rag dolls my mother arranged on my bed at home.

I want to be invisible. I want to go back to my mother’s body.

Branches snap off the black tress on Gallows hill. Ice cracks on the roof of the jail. This girl is a witch. The men in the front pew nod.

The girls let go of their throats.
Does my mother sleep in jail alone? I want to call to her.
I can’t. My body stands straight and still on the
examining table,

My voice torn out –
```

---

## IC-1676: Save Our Planet with poems by Alan Brownjohn, Frank Farian and Giorgio & Gisela Sgarbi • Lines shown in blue are from the lyrics of We Kill the World by Frank Farian and Girogio & Gisela Sgarbi • All other lines are from We are Going to see the Rabbit

- Title: Save Our Planet with poems by Alan Brownjohn, Frank Farian and Giorgio & Gisela Sgarbi • Lines shown in blue are from the lyrics of We Kill the World by Frank Farian and Girogio & Gisela Sgarbi • All other lines are from We are Going to see the Rabbit
- Author (byline): Alan Brownjohn
- Work: The Saner Places: Selected Poems
- Publisher: Enitharmon Press
- Publication date as stated: July 2011
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 425
- Already set (do not supply): none

### Source block (context only)

```text
• Title: We are Going to see the Rabbit
Author: Alan Brownjohn
Book: The Saner Places: Selected Poems
ISBN: 978-1907587078
Publisher: Enitharmon Press
Date (Month/Year): July 2011
• Title: We Kill the World
Lyrics by: Frank Farian and Giorgio & Gisela Sgarbi
Sheet Music: All-Sheet Music.com, Item #: 34-26-111
https://www.all-sheetmusic.com/
Release Date (Month/Year): Nov 1981
Performed by Boney M from their 5th album,
Boonoonoonoos
Lyrics available online at
https://www.streetdirectory.com/lyricadvisor/song/uop
ca/we_kill_the_world_dont_kill_the_world/
```

### Introduction (context only: never use it for content warnings)

```text
Is it too late to save our planet? One day we will find ourselves walking through concrete streets, searching for small signs of life we’ve almost wiped out. The trees? Gone. The fish? Struggling. The flowers? have Buried under parking lots. Do we care?

We pollute our world and mourn the loss of anything natural and real. I’ll call this realness the “only rabbit” left. By the time we finally think to search for the “only rabbit,” it’s already slipped underground, hiding from our technology, our noise and our disrespect. And we’re confused. Why does nature keep disappearing?

Save Our Planet with poems by Alan Brownjohn, Frank Farian and Giorgio & Gisela Sgarbi
```

### Performance text (classify this)

```text
We are going to see the rabbit.
Which rabbit, ask the children? Which rabbit?
The only rabbit . . .the only rabbit in England,
Sitting behind a barbed-wire fence
Under the floodlights, neon lights, sodium lights,
Nibbling grass on the only patch of grass
In England, (except the grass by the hoardings, which

doesn’t count)

Where will this lead to
and what is this good for?
Poor world, is hurting bad,
Poor world, is doomed to die.

First we shall go by escalator, Then we shall go by underground, And then we shall go by motorway, And then by helicopterway, And the last 10 yards we shall have to go On foot.

We kill the world
We kill the world
'cause we don't know
what we are doing!

We are nearly there,
We are longing to see it,
And so is the crowd
Which is here in thousands
With mounted policemen
And big loudspeakers
And bands and banners.
Everyone has come a long way.

Where will this lead to
and what is this good for?
A Poor World, Poor World.
Fishes doomed to die
as people live close by
Parking lots will come
where flower fields were bright
as junkyard covers sight!

But soon we shall see it
Sitting and nibbling
The blades of grass
In – but something has gone wrong!
Why is everyone so angry,
I see mushrooms, atomic mushrooms.
I see rockets, missiles in the sky.
Poor World, Poor World.

Why is everyone jostling and complaining?

Don't kill the world
don't let her down.
Don't kill the world
our means of life.
Lend ear to nature's cry.

The rabbit has gone, Yes, the rabbit has gone. He has actually burrowed down into the earth And made himself a warren, under the earth, Despite all these people. What can we do?

Don't kill the world
She's all we have,
And surely is worth to save.
Don't let her die,
fight for her trees,
Pollution robs air to breathe.

Don't kill the world help her survive

It is all a pity, you must be disappointed, Go home again, go home for today.

Cherish the world.
On behalf of all creatures,
Care for the earth,
Foundation of life
Slow progress down help her survive

For you cannot hear the rabbit Remarking rather sadly to himself, by himself, As he rests in his warren, under the earth: ‘It won’t be long, they are bound to come, They are bound to come and find me, even here.’

We kill the world
We kill the world
'cause we don't know
what we are doing!
A Poor World, Poor World.
```

---

## IC-1677: The Scientist and the Bumble Bee

- Title: The Scientist and the Bumble Bee
- Author (byline): Harry Baker
- Work: The Sunshine Kid (10th Poem in the collection, page #s not available)
- Publisher: Burning Eye Books
- Publication date as stated: Aug 2014
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 591
- Already set (do not supply): none

### Source block (context only)

```text
Author: Harry Baker
Book: The Sunshine Kid
(10th Poem in the collection, page #s not available)
ISBN: 978-1909136281
Publisher: Burning Eye Books
Date (Month/Year): Aug 2014
```

### Introduction (context only: never use it for content warnings)

```text
They say if something is proven, it must be true. That numbers don’t lie. But what if believing those numbers is the very thing that holds us back? For example, according to science, bumble bees shouldn’t be able to fly. And yet they do.

This poem is for anyone who’s ever been told “you can’t” and chose not to listen.

The Scientist and the Bumble Bee by Harry Baker
```

### Performance text (classify this)

```text
(10th Poem in the collection, no page number available) The scientist said the bumblebee couldn't fly, She lacked the wingbeats per minute or the necessary

size, But the bumblebee in her ignorance proved him wrong, She knew she could fly cause she'd flown all along Imagine if she'd listened to the man she might have

stopped, Given up on the spot, tucked her wings in and dropped, So don't ever let someone tell you what you can't do, Just because its proven, doesn't mean it's true.

The bumblebee bumbled, loving her life, she hums as she

flies, The bumblebee fumbled, clumsily stumbled from flower

to flower The bumblebee tumbled, tore through the sky pulling

corkscrews and dives, The bumblebee mumbled, crumbled in front of the queen

and her power, The bumblebee grumbled something explicit, discovered

she'd been labelled a gimmick, The bumblebee rumbled, desperate to eat that nectar so

sweet, The bumblebee humbled her critics, silenced all things

scientific, The bumblebee jumbled her speech, she didn't care cause

in the air she was free...

Because she was a busy bee, loved to fly to flowers and

visit trees,
Deliver seeds, efficiently, more so than in a breeze,
Intricate and intimate, meticulous, auxiliary,
And gathered more honey than any sick MCS,
Ever since she learned to fly, she earned her stripes,
Despite the words of hype from learned types,
Suppressed the urge to fight or turn and hide,
Instead she yearned for skies and birds up high,
Her confidence was soaring, She saw scientists as boring,
The sort of people she should be ignoring,
Because they made no sense, at least no scent as sweet as

pollen, Even centimetres from her they depended on their

drawings, And they'd rather follow their charts than follow their

hearts, If they saw a bee leave they would still believe their

graphs, They preferred facts and figures to beeswax and vigour But she begged to differ as she flew past and laughed,

Meet the scientist, his aim in life was to try and dismiss, Any hypothesis he deemed preposterous, When asked why he never swallowed his pride he replied "that's obvious, it wouldn't fit down my esophagus," Not quite the optimist, more like the opposite, Less likely to be living in a bubble than popping it, He had hay fever Pollinosis when close to the anomalous, Taking measurements, making experiments, accumulating

evidence, His brain contained considerable cleverness compared to

his intelligence, So busy with bees in the room, he forgot the elephant, His full proof was foolproof except for the truth, If the bumblebee had read his report she'd have agreed, she was too heavy therefore would never be airborne, but ignorance is bliss and that begins with a Bee

This one's for the bees in the hives living lives of aviation, The ones who survive and help survive through

pollination,
The ones who thrive in the sticky situations
With the floccinaucinihilipilification,
Doing what they're doing for the buzz, not for love or

money, Moving and maneuvering above, if the weather's sunny, Proving to the humans their conclusions are confusing And unusually refusing to budge, This is for those who are being themselves, and who

believe in themselves, Who see the bee in themselves, and set it free in

themselves, Who know that even though it's difficult, life is full of

miracles, And true happiness never came from being cynical, The bumblebees, forever looking for something sweet, Overcoming tumbleweeds by holding on the something

sweet, In summary, this is for those who stay summery, For there will be bees to come, whatever comes to be.
```

---

## IC-1678: Scratch and Dent Dreams

- Title: Scratch and Dent Dreams
- Author (byline): Eric Darby
- Work: The Secret Dream-lives of Engineers
- Publisher: The Wordsmith Press
- Publication date as stated: 2006
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 651
- Already set (do not supply): none

### Source block (context only)

```text
Author: Eric Darby
Book: The Secret Dream-lives of Engineers
ISBN: 978-1893972254
Publisher: The Wordsmith Press
Date (Month/Year): 2006
```

### Introduction (context only: never use it for content warnings)

```text
"Step right up, step right up! You won't believe your eyes. Step right up and see the amazing half man, half clam . . . . Carnival Barkers have gotten a bad rap over the years as “huxters” and slick-talking con men . . . But what if the “barking” was legitimate . . . what if the “sales pitch” was designed to encourage rather than mislead.

Step right up, step right up! You have the power to take things into your own hands, create your own solution, do not sit idly by hoping someone or something will come along and fix your situation. No more excuses, procrastination, self-pity, negativity, or self-doubt. Replace any sentence you ever started with “I can’t because” with “I can because.”

What if your “pitchman” had the answers? Scratch and Dent Dreams by Eric Darby.
```

### Performance text (classify this)

```text
Come on in, I’ve got a sale
on scratch and dent dreams,
whole cases of imperfect ambitions
stuff the idealists couldn't sell.
Yeah, I know none of its got price tags,
you decide how much it’s worth.
And none of its got glossy colored packaging
but it all works just fine.
I’ve got rainy day swing sets
good night kisses and stationary stars
still flying at the speed of light.
And over there out back
if you dig down through those
alabaster stoplights and those old 45’s
you’ll find a whole crate of second hand hope.
Yeah right there, that’s no chrome,
you just gotta work, polish it up a little bit.
Most folks give up too easy,
trade it in for some injection mold
and here and now.

And over there across the freeway,
you see that purple awning flappin’ in the breeze?
Well that’s Momma Genuine’s shop.
She’s older than all of us put together
but she still laughs like a house.

Now, she only sells tools but not like ya know,
she’s got saws that put back together,
drills that make whole. Mommas a cool legend to know,
and she sells duct tape too.

And down there at the end of the block
are two kids, crew cut and pig tailed
sittin’ behind a bindle top table
selling peanut-butter ice-cream out of a galvanized pale,
and there’s no metaphor there it’s just good ice-cream.
So here’s what ya do, take a look around
pick out what reminds you of places you wanted to be
but gave up on going and jam it all in this big box called
“now”.
Then go across the street to Momma Genuine’s,
ask her how she’s been , show her what I gave ya,
she’ll know exactly what you need
and then go back in the center of that freeway
and get to work making it all fit.
You won’t have any directions or factory number tabs
but don’t panic,
there’s a hundred ways to do it right
and none to do it wrong cause your startin’ out
with what’s already been given up upon,
you can’t do any worse.
Use the tools momma gave ya,
hum a little while ya work.
Then you find yourself sproutin’ extra thumbs

Take a break.

Go around the block,
get yourself an ice cream.
Smile when they hand it to you,
tip ‘em if you can
and when you get back it’s all gonna make sense.
You’ll see where it’s gonna fit perfect
and where the duct tape has to go.
And when you get finished,
take whatever spare parts you got at the bottom of
“now”
and make yourself a little sign that says “tomorrow”,
and hang it on your masterpiece.
Then you go back down the block
to where those two kids are packing up
their peanut butter enterprise
cause somebody told them they’d fail
and I want you to hand them tomorrow.
Make sure they know how important it is.
After they’ve run off with it all elbows and smiles
y’all can come back here, we’ll do it all over again.

Now I’m not telling you this to make a profit,
that’s how so many good ideas go wrong.
I’m just tired of seeing every day people
screaming through these doors convinced
they’re gonna hock even their littlest hopes and dreams
to fund their 401Ks.
I’m tired of seeing this whole world bet on going big
or giving up. Only handing out glory to newspaper
headlines
and story book endings, ‘cause the truth is
I think we need those swing sets most on the rainy days.

I’m happy going to sleep after just a goodnight kiss, and I believe that beauty can be as simple as two kids, crew cut and pig tails, handing me a scoop of peanut butter ice cream that’s so good, you’d think it was a dream.
```

---

## IC-1679: Scratch and Dent Dreams and Angelic Insanity

- Title: Scratch and Dent Dreams and Angelic Insanity
- Author (byline): Eric Darby and Kevin “Chesko” Briancesco
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1159
- Already set (do not supply): none

### Source block (context only)

```text
Author: Eric Darby
Book: High Desert Voices: The 2005 National Poetry
Slam Anthology
ISBN: 978-1893972834
Publisher: The Wordsmith Press
Date (Month/Year): 2006
Author: Kevin “Chesko” Biancesco
Book: High Desert Voices: The 2005 National Poetry
Slam Anthology
ISBN: 978-1893972834
Publisher: The Wordsmith Press
Date (Month/Year): 2006
```

### Introduction (context only: never use it for content warnings)

```text
We all had childhood dreams. Many of us wanted to be astronauts, painters, actors, firefighters, lawyers, doctors or perhaps even the president. Indeed, the magical brain of a child perceives the world as an endless array of possibilities. But somewhere along the way, we lose the ability to dream . . . to imagine . . . to live life with a sense of wonder and we get bogged down in the Here and Now, the daily grind, the REALITY of our situations.

Well today, just for a few minutes, cast your adult reality aside and instead reach with “Angelic Insanity” for some of those lost, “Scratch and Dent Dreams.” by Eric Darby and Kevin “Chesko” Brianesco.
```

### Performance text (classify this)

```text
Scratch and Dent Dreams by Eric Darby
Come on in, I’ve got a sale on scratch and dent dreams -
whole cases of imperfect ambitions
stuff the Idealists couldn't sell.
Yeah, I know none of its got price tags -
you decide how much its worth.

An’ none of it’s got glossy colored packaging
but it all works just fine.
I’ve got rainy day swing sets, good night kisses,
and stationary stars still flying at the speed of light.

Over there in back,
if you dig down through the alabaster stoplights
and those old 45’s
you’ll find a whole crate of second-hand hope.
Yeah! That’s real chrome - you just gotta
polish it up a little bit.
Most folks give up too easy, trade it in
for some injection-molded Here-and-Now.

Now, look across the freeway -
see that purple awning flappin’ in the breeze?
That’s Momma Genuine’s shop.
She’s older than all of us put together
but she still laughs like a house.
She only sells tools, but not like you know.

She’s got saws that put back together,
an’ drills that make whole.
Momma’s a good legend to know,
and she sells duct tape too.

And down there, at the end of the block, are two kids - crewcut and pigtails - sittin’ behind a vinyl-topped table sellin’ peanut butter ice cream out of a galvanized pail. There’s no metaphor there – it’s just good ice cream, and that’s all it has to be.

So here’s what you do:
Take a look around,
pick out what reminds you of places you wanted to be,
but gave up on goin’
and jam it all in this big box called “Now.”
Then go across the street to Momma Genuine’s;
ask her how she’s been,
show her what I gave ya, and she’ll know
exactly what you need.
Then go back in the center of that freeway,
keepin’ faith in the traffic jam swerve,
and get to work
makin’ it all fit.
You won't have any directions or
factory number tabs, but don’t panic.
See, there’s a hunnerd ways to do it right, and none
to do it wrong, so you can’t do any worse.
Use the tools Momma gave you,
hum a little while you work,
and if you find yourself sproutin’ extra thumbs,
take a break. Go down the block. Get yourself an ice

cream. Smile when they hand it to you, tip ‘em if you can, and when you get back . . .

it’ll all make sense!
You’ll see where it’s gonna fit perfect, and
where the duct tape has to go.
When you get finished, take whatever spare parts
you’ve got at the bottom of Now,
make yourself a little sign that says “Tomorrow”
and hang it on your masterpiece.

Then I want you to go back down the block
to where those two kids are packing up their
peanut butter enterprise
‘cause somebody told them they’d fail
and I want you to hand them Tomorrow.
Make sure they know how important it is.
And after they’ve run off with it all
elbows and smiles
you come back here, an’ we’ll do it all over again.

Now, I’m not telling you this to make a profit.
That’s how so many good ideas go wrong.
I’m jus’ tired of seeing everyday people
streamin’ through these doors convinced
they gotta hock even their littlest hopes and dreams
to fund their 401Ks.
I’m tired of seeing this whole world being bent on
Going Big or givin’ up,
only handin’ out glory
to newspaper headlines and storybook endings,
‘cause the truth is:
I think we need those swing sets most on the cloudy

days.
I’m happy goin’ to sleep after
“just” a goodnight kiss
If it made me feel somethin’ inside,
and I believe that beauty can be as simple
as two kids - crewcut and pigtails -
handin’ me a scoop of peanut butter ice cream
that tastes so good,
you’d think it was a dream.

Angelic Insanity (or, The Ninja Ponies Poem) by Kevin “Chesko” Brianesco

Down to the crooked teeth, chubby cheeks< and s-s-s-stutter

My Godson Carlitos, Is a three-foot version of me.

And as I watch him digging a hole in the backyard,
I remember back when I was a little boy -
My grandmother would tell me,
“If you can dig a deep enough hole

You can see the sunrise at night.”

But no matter how many holes I dug
And no matter how deep I was able to go -
The sun kept setting.
And eventually I stopped digging -
Understanding the futility of seeing something as

absurd as the sun rising at night.

On cue,
My Godson stumbles over to me and says,
“Nino, when I grow up,
I’m gonna be a pony!”

And I smile -
Trying to hid the fact that
I want to grab him and
I want to shake some sense into him -
Tell him that he can’t be a pony,
that the piece of the Easter bunny’s tail
we caught in our Easter bunny trap
is really just a dirty piece of cotton,
That mommy’s special friend,
“Uncle Steve”
Isn’t really his uncle
And that the sun -
won’t ever rise at night.
But as I sat there contemplating his fate
I noticed something in his eyes that I had never seen

before.
And all I could do was watch as his eyes
began refracting the starlight from the windows,
like prisms,
into a million tiny promises
that his gaze -
would never reflect my own.

And, in the moment of angelic insanity, I told him - “I’m gonna be a pony too!”

Only I told him that we would be ninja ponies,
ninja crime-fighting ponies -
who can fly!
and we will call ourselves Pony Joe
and Johnny Nintendo
because people will write comic books about us!

Apparently he was satisfied with my answer Because he decided to change the subject - And asked me to tell him a story before he went to

sleep.
You see, he sees me as his Nino,
his hero,
One of the few remaining fantasies I have left that still

keeps me going.
So I resist,
not wanting to disappoint these angel eyes,
But after enough begging,
I gave in and told him a story
About a little boy [child/girl]
about his age,
Who grew up to be a pony
that once dug a hole so deep -
s/he was able to see the sunrise at night.

Without hesitation, He just looked up at me and asked, “So how deep did you have to dig, Nino?”

then started spinning around in circles

Look, I know that eventually my Godson’s imagination will

fade
and that I’m not going to be his hero forever,
but on that night
in the eyes of this tiny little man,
I was a pony,
and he wanted to be me -
and as I looked out the window into the moonlit sky,
I swear to God,
I saw the sun begin to rise.
```

---

## IC-1680: Searching for the Grand Unified Theory of Everything

- Title: Searching for the Grand Unified Theory of Everything
- Author (byline): Sara Penrod
- Work: Cadance (award-winning student publication)
- Publisher: Alabama School of Fine Arts Writing Department
- Publication date as stated: 2004
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1057
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sara Penrod
Book: Cadance (award-winning student publication)
ISBN: N/A
Publisher: Alabama School of Fine Arts Writing
Department
Date (Month/Year): 2004
NOTE – This is a student publication only and may not be
permissible as “published” material in all states. Please
check with your state guidelines before performing.
```

### Introduction (context only: never use it for content warnings)

```text
“Generally, the theories we believe we call facts, and the facts we disbelieve we call theories” which is why everything is still . . . Searching for the Grand Unified Theory of Everything by Sara Penrod; with special thanks to all those theoretical physicists I don’t quite understand
```

### Performance text (classify this)

```text
1. These days everything can be explained in terms of circles. (Or their corollaries: spheres, ovals, ellipses.)

The circular flow of economics. The wheel of fate. The water cycle.

Even the most eccentric orbits are nothing more than laterally compresses ovals.

2. The universe, says Albert Einstein, is spherical and static. No, says Georges Lemaître, the universe is spherical and expanding. You’re both wrong, says Stephen Hawking, space-time is warped and therefore the sphere is not smooth.

I try not to worry about metaphysics; I have enough trouble with the quantifiable. Basic algebra eludes me.

3.
My friend calls from Salem, Oregon
to ask if I’ve read my horoscope
for the day. I tell her I haven’t,
so she reads it to me from her paper.

Today is a great day for relationships. Call up a friend you haven’t talked to in a while; chances are she’ll be thinking of calling you. Make a romantic dinner date with that special someone.

So I buy my local paper
at my corner coffee shop and read
my horoscope. It’s different here.
I guess it’s because I’m farther south.
Today is a day for caution. Watch your tongue and
guard your words carefully, or
you might offend someone close to you. Put off any
major life decisions and changes
until a more opportune time.

4.
Pinned to my bedroom wall is a photograph
of physicist Richard Feynman’s Caltech blackboard
at the time of his death in 1988.

“What I cannot create I do not understand,”

he had scrawled. And

“Know how to solve every problem that has been solved.”

That is a test I wouldn’t want to take.

5. Last night, a friend I hadn’t thought of in years called me. She’s a lawyer now, working for NASA down in Florida.

“I handle the wills for the astronauts,” she told me. “That’s important, you know, since it’s so dangerous.” And then one thing led to another as those things tend to do

and an hour later I found myself in the middle of philosophy.

“Does anything exist
until we see it?”
she asked. I shrugged
before I remembered she couldn’t
see me.

6.
When I throw this tennis ball
up in the air,
it always comes down.

This is called the Law of Gravity.

But one day when I toss it up, it might not come down. It might continue upward forever.

This would disprove the Law of Gravity.

You see, no laws are absolute. Even if it has always happened this way through all of recorded history,

tomorrow could be different. Tomorrow the invisible hand could reach down and blear the line between theory and law.

7. In a black hole, time ceases to exist.

What does this mean to you?

Nothing. You’ve never seen a black hole.

And what does this mean to me?

Nothing.

8.
I dream of a world
made up of the time
between time—the moments
between this moment
and the next.

In this world, time
is a jumble of betweens—
crossroads
ether
that moments twice a day that’s neither day nor night.

This world exists only to keep real time from happening all at once.

9.
The music of the cosmos:
every heart vibrates to that
iron string. All matter—

everything that matters—

is built of one-dimensional vibrating loops of string.

10. So now we arrive at the other dimensions. What are those?

I don’t know, but

people smarter than me postulate there are ten or eleven. Even geniuses can’t be sure of their math. They say these unfound dimensions are coiled up, tiny, like a human hair.

11.
Pinned to my bedroom wall is a photograph
of Einstein holding a puppet
of himself, shortly after he arrived
in America to stay. I don’t know
why Einstein needs a brainless
dancing miniature.

12.
In my timeless
dream world, a black hole
replaces the sun, and when it rains,
children try to sing
their black hole out from behind
heavy clouds.

13. In 1931 Kurt Gödel proved that the universe can never be answered, that questions persist.

He proved this mathematically.

He was a mathematician.

Now we know mathematics is not a coherent and complete system based on one logical foundation.

14. “I want to know how God created this world. I am not interested in this or that phenomenon, in the spectrum of this or that element. I want to know His thoughts…the rest are details.” --Einstein

15. The French, those eternal snobs of wine and cheese and intellectual superiority,

the were the first to publicly doubt black hole theory.

In French, trou noir means black hole.

In French, trou noir has dubious sexual connotations.

They wanted to call a black hole astre occlu, hidden star.

16.
My grandmother’s master narrative
implicates God in every step
along the way, and each decade
her explanation changes
as new discoveries are made.

First, creation. Second, created evolution. Now, intelligent design.

17.
It is the new biggest question of theoretical
physics. They want to fit everything
together as one, to combine
general relativity
with black holes
with quantum mechanics
with superstrings
with p-branes
until they have one story, one theory
to explain it all—the universe
in a nutshell. They call it

their Grand Unified Theory or gut for short.

18.
Good old Douglas Adams.
Forty-two.
It’s that simple.
That’s the answer to life, the universe, and
everything, you know.
You want to know the question?
Well, that’s going to be a lot more difficult.

19.
A journalist
once remarked to a physicist
“Someone told me
only three people in the world
truly understand
Einstein’s theory of general relativity.”

The physicist cocked his head
and told the journalist
he couldn’t figure out who
the third person was.

I tried for hours to untangle this story and gave up feeling stupid and incomplete because I knew only that Einstein, at least, must be one who understood.

20.
“God does not play dice,”
Einstein said. He was so certain
of a static universe he introduced
his cosmological constant
into his equations so the universe
would stay finite.

Dark matter, invisible
to telescopes because it absorbs
all light, could make up vast
realms of our universe. The limit

of our expanding cosmos is as yet in shadows.

21. Another thing that Einstein said: “The cosmological constant was my biggest mistake?”
```
