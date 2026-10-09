# Classification request: batch 30 of 53 (40 records, IC-1561 to IC-1600)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-030-reply.json`.

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

## IC-1561: Finger Paints and Crayons

- Title: Finger Paints and Crayons
- Author (byline): Cheryl Costello-Forshey
- Work: Chicken Soup for the Teenage Soul III
- Publisher: Backlist, LLC
- Publication date as stated: Oct 2012
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1095
- Already set (do not supply): none

### Source block (context only)

```text
Author: Cheryl Costello-Forshey
Book: Chicken Soup for the Teenage Soul III
ISBN: 978-1623610913
Publisher: Backlist, LLC
Date (Month/Year): Oct 2012
```

### Introduction (context only: never use it for content warnings)

```text
Race and racism are tough for adults to talk about in this country, and many adults think that by not talking to children about race, they will grow up "color-blind" and not racist. But the truth is that children begin to notice racial differences as early as 6 months, and because racism and biases DO exist in our society, children see it and learn it. By the time they are preschool age, children can internalize racial biases.

In this selection, a very gifted teacher presents an art lesson to her class – but the students learn so much more about colors . . . they “can be beautiful, but hey can also destroy.”

Finger Paints and Crayons by Cheryl Costello-Forshey
```

### Performance text (classify this)

```text
With chalk in hand she wrote her name, across a board

once bare And then she sat behind her desk, without a single care And for fifteen minutes, she did not make a sound Until the final student, had finally settled down Then she stood before them, and told them all her name And then politely asked, each student to do the same Then without hesitation, she took papers from a sack And placed them in two piles, one white, the other black And deliberately quite slowly, with a slight and mischief

smile She began handing out the papers, up and down each aisle And once each student had a piece; she continued within

their sights To gather two piles of crayons, one black, the other white And then she took a painting, from behind her walnut desk Then placed a painter’s smock, overtop her navy dress And to no one unparticular, she spoke in peaceful tones “I’ve been working on this painting, for years in my own

home” She stood staring at the painting, its brilliant colors mixed

as one Upon a vast horizon, the presence of a sun It indeed was not a Rembrandt, a Picasso, or Michelangelo

to say the least But it nonetheless was beautiful; its presence spoke of

peace And no doubt that lovely painting, had taken so much time For every color known to man, seemed to intertwine And so it came with wonder, what they witnessed with

surprise The act that took them all off guard, done right before their

eyes With finger-paints now gathered, and opened on her desk She smeared the colors upon her hands, in an entangled

awful mess And then as though she’d lost her mind, she smeared her

hands across
The painting once so beautiful . . . now a total loss
It did not make a bit of sense, they did not understand
As they sat and watched their teacher, wipe the paints from

off her hands And then she took the crayons, and went up and down the

rows And handed to each student, the colors that she chose “Now”, she told her students, “I want you to create A picture filled with beauty, devoid of any hate” Mouths dropped open widely; mumbles filled the room And students looked to one another, as unasked questions

seemed to loom For the students with white paper, were given crayons the

same shade And the students with black crayons, had been given, a

raven colored page And how could one create splendor, with no colors to mix

and match The students were quite certain, their teacher had left out

most the facts “Teacher,” a student’s voice was heard, “I’m not sure I can” Staring at the white crayon, and white paper in her hand Silence overtook the room; it eerily crept about Causing the teacher’s gentle voice, to erupt into a shout “You each share the same problem, you each possess the

power to resolve But only the students with open-minds, will have the ability

to solve” Minutes ticked away, class was nearing to an end And not one single student, knew quite how to begin And when the bell rang out, and they hurried to their feet Their teacher told them commandingly, to return back to

their seat “Before you leave this classroom, I think you each should

know For this assignment you receive a failing grade, for you have

no work to show And tomorrow and the next day, your assignment shall be

the same And those who fail my class, will have only themselves to

blame” The next day and the following, students weren’t quite sure

what to do
Until at last, a solution, began to surface through
When one student with his crayon, and paper both in black
Turned to the student behind him and asked, “May I

borrow that?” The student hesitated, but then gave up his crayon made of

white And ultimately the assignment, no longer seemed a plight For students all throughout the class, switched crayons up

and down the aisles And certain that they’d found the solution, their faces lit

with smiles And just as every student began to draw, across an empty

page The teacher whom they’d all began, to see as certainly

quite strange . . . Collected all the pages and crayons, without a single mark And then spoke a loud, “thank you, for bringing hope into

my heart You see, I wanted you to realize, that in order to create A picture filled with beauty, devoid of any hate You needed first to recognize, that a problem did exist And that a practical solution, could be found within your

midst
And that racism is a problem, each of us must face
Working all as one, before it’s much too late
And with open eyes and open hearts, we must see the

person, not the color of their skin And come to the understanding, that racism has to end For together we are family, we cry tears, we all feel pain And though we may not look the part, inside we’re all the

same And we battle over crayons, that’s exactly what we do For crayons are just colors, that’s all our skin is too”

Students looked about the room, a variety of colors on their

skin
As the point she was trying to make, began to settle in
The looks upon their faces, readily explained
That they each were trying to contemplate: that indeed

they were the same A nervous shuffling of papers, and coughs throughout the

room Portraying the vital image, that fighting over crayons was a

stupid thing to do It was then each student realized, the purpose of crayons

and papers the same shade Was to prove they each needed the other color, to help fill

their empty page Silence seized the moment, as one student raised his open

hand And then spoke in hesitation, “I just don’t understand . . . Why you took your painting, the one you seemed to enjoy

so very much Gathered up your finger-paints, to destroy it in a touch” Sadness filled her face, as a tear trailed upon her cheek And in slow and heartfelt words, she began to speak “To show you each that colors can be beautiful, but they

also can destroy Everything we love and work for, everything we each enjoy And the destruction of something that I loved, was to make

a point to you That racism destroys the beauty in us all,

And that fighting over colors, is a wasteful thing to do
```

---

## IC-1562: The Fool Errant

- Title: The Fool Errant
- Author (byline): Amy Lowell
- Work: A Dome of Many-Coloured Glass
- Publisher: Blue Unicorn Editions
- Publication date as stated: Feb 2001
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 747
- Already set (do not supply): none

### Source block (context only)

```text
Author: Amy Lowell
Book: A Dome of Many-Coloured Glass
ISBN: 978-1583964712
Publisher: Blue Unicorn Editions
Date(Month/Year): Feb 2001
```

### Introduction (context only: never use it for content warnings)

```text
Winston Churchill once said: "We make a living by what we get. We make a life by what we give." Do you make a
```

### Performance text (classify this)

```text
good living? Congratulations . . . Do you have a great life? That question is a little harder to answer if we use Churchill’s quote as a standard. But don’t feel like you’ve been singled out for a lecture. Experts in psychology and philosophy have debated one key issue for centuries: Is mankind selfish? And if so . . . is that necessarily a bad thing? Amy Lowell brings this concept to life in her poem “The Fool Errant.”

The Fool Errant sat by the highway of life
And his gaze wandered up and his gaze wandered down,
A vigorous youth, but with no wish to walk,
Yet his longing was great for the distant town.

He whistled a little frivolous tune
Which he felt to be pulsing with ecstasy,
For he thought that success always followed desire,
Such a very superlative fool was he.

A maiden came by on an ambling mule,
Her gown was rose-red and her kerchief blue,
On her lap she carried a basket of eggs.
Thought the fool, "There is certainly room for two."

So he jauntily swaggered towards the maid
And put out his hand to the bridle-rein.
"My pretty girl," quoth the fool, "take me up,
For to ride with you to the town I am fain."

But the maiden struck at his upraised arm
And pelted him hotly with eggs, a score.
The mule, lashed into a fury, ran;
The fool went back to his stone and swore.

Then out of the cloud of settling dust
The burly form of an abbot appeared,
Reading his office he rode to the town.
And the fool got up, for his heart was cheered.

He stood in the midst of the long, white road And swept off his cap till it touched the ground. "Ah, Reverent Sir, well met," said the fool, "A worthier transport never was found.

"I pray you allow me to mount with you,
Your palfrey seems both sturdy and young."
The abbot looked up from the holy book
And cried out in anger, "Hold your tongue!

"How dare you obstruct the King's highroad,
You saucy varlet, get out of my way."
Then he gave the fool a cut with his whip
And leaving him smarting, he rode away.

The fool was angry, the fool was sore, And he cursed the folly of monks and maids.

"If I could but meet with a man," sighed the fool, "For a woman fears, and a friar upbraids."

Then he saw a flashing of distant steel
And the clanking of harness greeted his ears,
And up the road journeyed knights-at-arms,
With waving plumes and glittering spears.

The fool took notice and slowly arose,
Not quite so sure was his foolish heart.
If priests and women would none of him
Was it likely a knight would take his part?

They sang as they rode, these lusty boys,
When one chanced to turn toward the highway's side,
"There's a sorry figure of fun," jested he,
"Well, Sirrah! move back, there is scarce room to ride."

"Good Sirs, Kind Sirs," begged the crestfallen fool,
"I pray of your courtesy speech with you,
I'm for yonder town, and have no horse to ride,
Have you never a charger will carry two?"

Then the company halted and laughed out loud. "Was such a request ever made to a knight?" "And where are your legs," asked one, "if you start, You may be inside the town gates to-night."

"'T is a lazy fellow, let him alone, They've no room in the town for such idlers as he." But one bent from his saddle and said, "My man, Art thou not ashamed to beg charity!

"Thou art well set up, and thy legs are strong, But it much misgives me lest thou'rt a fool; For beggars get only a beggar's crust, Wise men are reared in a different school."

Then they clattered away in the dust and the wind,
And the fool slunk back to his lonely stone;
He began to see that the man who asks
Must likewise give and not ask alone.

Purple tree-shadows crept over the road,
The level sun flung an orange light,
And the fool laid his head on the hard, gray stone
And wept as he realized advancing night.

A great, round moon rose over a hill
And the steady wind blew yet more cool;
And crouched on a stone a wayfarer sobbed,
For at last he knew he was only a fool.
```

---

## IC-1563: For Black Boys -- A Collection

- Title: For Black Boys -- A Collection
- Author (byline): Jasmine Mans, Margaret Burroughs and Keith Antar Mason
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1427
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jasmine Mans
Book: Chalk Outlines of Snow Angels, Pgs 12-13
ASIN: BOO8JHIM2Y (Digital Publication)
Publisher: Thorn 10 Publishing
Date (Month/Year): 2011
Author: Margaret Burroughs
On-Line Transcript
https://www.poetryfoundation.org/poems/146263/what-
shall-i-tell-my-children-who-are-black-reflections-of-an-
african-american-mother
Publisher: Poetry Foundation
Date (Month/Year): Originally Published 1968
Author: Jasmine Mans
Book: Chalk Outlines of Snow Angels, Pgs 14-15
ASIN: BOO8JHIM2Y (Digital Publication)
Publisher: Thorn 10 Publishing
Date (Month/Year): 2011
Author: Keith Antar Mason
Book: Colored Contradictions: An Anthology of
Contemporary African American Plays,
Pgs 194-196
ISBN: 978-0452274976
Publisher: Plume
Date (Month/Year): Nov 1996
```

### Introduction (context only: never use it for content warnings)

```text
On July 12, 1967, rumors spread that police had killed a black man in Newark, NJ. Though the story was untrue — the man was beaten but survived — pent-up rage led to four nights of riots and looting.

50+ years have passed, and the words by Jasmine Mans in tribute to the Newark riots still ring true for many people of color. In recent years, fatal shootings of unarmed black men across the United States have sparked outrage and concerns over police use of lethal force.

For Black Boys – A Collection with poems by Jasmine Mans, Margaret Burroughs and Keith Antar Mason
```

### Performance text (classify this)

```text
Ode To Newark by Jasmine Mans (Pg 12-13) Blood has decorated these streets They have begun to look like pastures of rose petals, Black boys have gotten so fed up with their prayers drowning by bedside, The load their guns into the sky To make sure God is listening We are chalk outlines of snow angels, We breathe like death is lurking on the edge of our spleens We dance in the wind to the crackles of gun shells, Jerk bodies back like God is head puppeteer of this

destruction

Our voices bend and crack in the wind between fear and

park swings. There is a guardian angel that lost the directions to

salvation,
A Mother who clasped the New Testament too tight
For the heavens to take responsibility.
There is a God who choked on promises,
A Jesus who did not die for enough of them.

If Newark were a woman,
She would be Lauryn Hill after Zion,
With a broken spleen and body bags
Lying under her eyelids.

Death looks too much like children
Who slipped pass God’s peripheral,
Maybe some of us are too premature for a tomorrow.
Maybe we’ve been dancing on the edge
Of God’s sanity for too long.
Some casualties of genocide look too familiar

To not scream.

TRANSITION

“The more things change, the more they stay the same.” People of color continue to encounter overt and subtle racism, glass ceilings in the workplace and employers who are surprised to learn they hired competent, skilled black employees. Black men are still fearful when pulled over in a routine traffic stop. And words penned in the 1960’s still ring true. What Shall I Tell My Children Who are Black? by Margaret Burroughs

What Shall I Tell My Children Who Are Black? by Margaret Burroughs

What shall I tell my children who are black
Of what it means to be a captive in this dark skin
What shall I tell my dear one, fruit of my womb,
Of how beautiful they are when everywhere they turn
They are faced with abhorrence of everything that is black.
Villains are black with black hearts.
A black cow gives no milk. A black hen lays no eggs.
Bad news comes bordered in black, black is evil
And evil is black and devils' food is black. . .

What shall I tell my dear ones raised in a white world
A place where white has been made to represent
All that is good and pure and fine and decent.
Where clouds are white, and dolls, and heaven
Surely is a white, white place with angels
Robed in white, and cotton candy and ice cream
and milk and ruffled Sunday dresses
And dream houses and long sleek cadillacs
And angel's food is white. . . all, all. . . white.

What can I say therefore, when my child
Comes home in tears because a playmate
Has called him black, big lipped, flatnosed
and nappy headed? What will he think
When I dry his tears and whisper, "Yes, that's true.
But no less beautiful and dear."
How shall I lift up his head, get him to square
His shoulders, look his adversaries in the eye,
Confident of the knowledge of his worth,
Serene under his sable skin and proud of his own beauty?

What can I do to give him strength
That he may come through life's adversities
As a whole human being unwarped and human in a world
Of biased laws and inhuman practices, that he might
Survive. And survive he must! For who knows?
Perhaps this black child here bears the genius
To discover the cure for. . . Cancer
Or to chart the course for exploration of the universe.
So, he must survive for the good of all humanity.
He must and will survive.
I have drunk deeply of late from the foundation
Of my black culture, sat at the knee and learned
From Mother Africa, discovered the truth of my heritage,
The truth, so often obscured and omitted.
And I find I have much to say to my black children.

I will lift up their heads in proud blackness
With the story of their fathers and their fathers
Fathers. And I shall take them into a way back time
of Kings and Queens who ruled the Nile,
And measured the stars and discovered the
Laws of mathematics. Upon whose backs have been built
The wealth of continents. I will tell him
This and more. And his heritage shall be his weapon
And his armor; will make him strong enough to win
Any battle he may face. And since this story is
Often obscured, I must sacrifice to find it
For my children, even as I sacrificed to feed,
Clothe and shelter them. So this I will do for them
If I love them. None will do it for me.
I must find the truth of heritage for myself
And pass it on to them. In years to come I believe
Because I have armed them with the truth, my children
And my children's children will venerate me.
For it is the truth that will make us free!

Black Son by Jasmine Mans
(Pg 14-15) How do you tell a Black woman that raising a
Black son
Isn’t some type of inside joke
Crafted by God and some White man?

Can you prove to her that they are not in Heaven
Snickering at the soul of a single parent mother
Dressing her son for graduation
Hoping he can make it
Across the stage,
Down the aisle,
Or off the balcony quick enough
To not be caught in his skin
At the wrong time

I’ve touched the bellies of women
Who aborted more Black boys
Than thrown overboard slaves
Who will look you in the eyes
Like a blue bird awakening to a holocaust
And whisper
“I am just afraid to raise a Black son.”
A Black boy is just a trembling soul
Suffocating in a fabric
That anyways itched around the neck
A tag that always seem to make you scratch
Around the noose collar

How can you tell a mother staring At her newborn in the delivery room Hoping that his skin doesn’t get any darker Praying it will stay as light and deceiving As a sunrise in the ghetto

That her son’s body isn’t a chamber
For some bigot
To hang his sin and southern accent in
That her baby’s flesh isn’t some colored toy
For the rich blue eyed boys

Can you tell a mother that her son isn’t the disaster
Lurking in the back of master’s mind
Before he prays over Sunday dinner
“I am just afraid to raise a black son”
Who will spend the rest of his life
Praying for a melody or a melanin
Safe enough to scream in

A boy who had to be a martyr for a war
He never asked for
Loving something so disposable
Never sat well in the pockets or hearts
Of mothers hoping for a break
And a teaspoon of sugar on this land

Son, you have been dancing in the hurricane too long.

For Black Boys who Have Considered Homicide When the Streets Were too Much by Keith Antar Mason A young man speaks emotionally about how it feels to be Black in White America.

Brother #3: (Pg 194-196) I must be mistaken
some monster
I know
I can tell by the way you look
at me
you tighten up
and never smile
like aggression can only
be symbolized
by me
like the male gender
and colored black means
death carrier
potent poison
lethal
and I know
some how I know
I want to live
a long time but
I am gonna die
some obscene
joke
cuz’ you clutch
yourself around me
hold back
all the good things
even precious smiles
from me
some how I know
I wuz’ born to die
to die too soon
and I don’t understand
and that’s the confusion you see
that’s the fear
you feel
I am no more than
The stacked up
cemented
aggression
black tornado
come back from
oz no hell
born to die
and I mus’ be
a zombie
walkin’ the streets
the livin’ dead
and my brain
the curse

of the male gender
colored black
colored black
with nappy hair

And you only feel
afraid
but I know
how fear kills
I know
I live it
standin’
on the corner
holdin’ the wall
like a firin’ squad
and some how I know
I wuz’ born to die
a zombie
live or dead
the male gender
cursed
colored black
and too damn
aggressive
jus’ by being born
```

---

## IC-1564: For Eli

- Title: For Eli
- Author (byline): Andrea Gibson
- Work: Pole Dancing to Gospel Hymns, Pgs 17-20
- Publisher: Write Bloody Publishing
- Publication date as stated: June 2008
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 602
- Already set (do not supply): none

### Source block (context only)

```text
Author: Andrea Gibson
Book: Pole Dancing to Gospel Hymns, Pgs 17-20
ISBN: 978-0981521305
Publisher: Write Bloody Publishing
Date (Month/Year): June 2008
```

### Introduction (context only: never use it for content warnings)

```text
I grew tired of being told I didn't support the troops just because I wanted to bring them home to their families, and out of a senseless war. I understand there cannot be peace at all times, and the Iraq/Afghanistan was the correct conflict to become involved in, but my heart broke every time I heard, read, saw the names and faces of the fallen.

According to the Watson Institute, as of the beginning of 2015 . . . the number of US soldiers that died fighting the wars in Iraq and Afghanistan surpassed 6,800. And it was estimated that over 100,000 troops had been seriously wounded. In 2005, President Bush justified the loss of life by saying: "My decision to remove Saddam Hussein was the right decision. Saddam was a threat and the American people, and the world, is better off because he is no longer in power."

Saddam Hussein was captured, convicted and executed on December 30, 2006. But American troops were left stationed overseas until 2020, fighting a battle for democracy that many believed was not our battle.

For Eli by Andrea Gibson
```

### Performance text (classify this)

```text
(Pg 17-20) Eli came back from Iraq
and tattooed a teddy bear onto the inside of his wrist
above that a medic with an IV bag
above that an angel
but Eli says the teddy bear won't live
and I know I don't know but I say, "I know"
‘cause Eli's only twenty-four and I've never seen eyes
further away from childhood than his
eyes old with a wisdom
he knows I'd rather not have
Eli's mother traces a teddy bear onto the inside of my arm
and says, "not all casualties come home in body bags"
and I swear
I'd spend the rest of my life writing nothing
but the word light at the end of this tunnel
if I could find the tunnel
I'd write nothing but white flags

Somebody pray for the soldiers
Somebody pray for what's lost
Somebody pray for the mailbox
that holds the official letters
to the mothers,

fathers,

sisters,
and little brothers
of Michael 19. . . Steven 21. . . John 33
how ironic that their deaths sound like bible verses

the hearse is parked in the halls of the high school
recruiting black, brown and poor
while anti-war activists
outside walter reed army hospital scream
100, 000 slain
as an amputee on the third floor
breathes forget-me-nots onto the window pain

But how can we forget what we never knew
our sky is so perfectly blue it's repulsive
Somebody tell me where God lives
‘cause if God is truth Ggod doesn't live here
our lies have seared the sun too hot to live by
there are ghosts of kids who are still alive
touting M16s with trembling hands
while we dream ourselves stars on Survivor
another missile sets fire to the face in the locket
of a mother whose son needed money for college
and she swears she can feel his photograph burn
how many wars will it take us to learn
that only the dead return
the rest remain forever caught between worlds of
shrapnel shatters body of three year old girl to
welcome to McDonalds can I take your order?

The mortar of sanity crumbling stumbling back home to a home that will never be home

again Eli doesn't know if he can ever write a poem again

One third of the homeless men in this country are veterans
and we have the nerve to Support Our Troops
with pretty yellow ribbons
while giving nothing but dirty looks to their outstretched

hands

Tell me what land of the free sets free its eighteen-year-old kids into greedy war zones hones them like missiles then returns their bones in the middle of the night so no one can see each death swept beneath the carpet and hidden like dirt each life a promise we never kept

Jeff Lucey came back from Iraq and hung himself in his parents basement with a garden

hose the night before he died he spent forty five minutes on his

father’s lap
rocking like a baby
rocking like daddy, save me
and don't think for a minute he too isn't collateral damage
in the mansions of washington they are watching them

burn
and hoarding the water
no senators' sons are being sent out to slaughter
no presidents' daughters are licking ashes from their lips
or dreaming up ropes to wrap around their necks
in case they ever make it home alive

our eyes are closed
America
there are souls in
the boots of the soldiers
America
[to hell with] your yellow ribbon
you wanna support our troops
bring them home
and hold them tight when they get here
```

---

## IC-1565: The Foxhole Manifesto

- Title: The Foxhole Manifesto
- Author (byline): Jeffrey McDaniel
- Work: Spoken Word Revolution
- Publisher: Longman
- Publication date as stated: 2003
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 670
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jeffrey McDaniel
Book: Spoken Word Revolution
ISBN: 978-0321328953
Publisher: Longman
Date(Month/Year): 2003
```

### Introduction (context only: never use it for content warnings)

```text
Lots of things in this world of ours don’t exactly make sense . . . Why is it that people say they “slept like a baby” when babies wake up every two hours? . . . Why do we press harder on a remote control when we know the batteries are dead? . . . Whose idea was it to put an “S” in the word “lisp”? . . . If electricity comes from electrons, does morality come from morons? And while we’re on the subject of morality . . . Who exactly is God?
```

### Performance text (classify this)

```text
The first God I remember was a Santa Claus God. Who you only turn to around Christmas time, who you tried to butter up, and got mad at if you didn't get what you wanted.

That didn't make sense

The Foxhole Manifesto by Jeffrey McDaniel I knew if there was a God, he could see through us, like we were made out of cellophane, like he could stare directly into our hearts, the way we look into an aquarium, like he'd know what was floating around in there, like he were the one feeding it.

Then there were those people who used god to threaten you, saying "you'd better be careful- God's watching." like God was some badass hillbilly sitting on some cloud, with some binoculars, a cotton candy beard and a shotgun.

Then there were those people who had God's name on a bumper sticker, like he was running for president. And sometimes those people would cut you off on the freeway, and give you the finger. Which is very different than lending a hand.

Then there were people on television, dressed in weird clothes and scary make-up, SWEARING that they had the secret to God, like god was a keyhole their eye was pressed to it, and if I gave him some money, they'd let me look, and I could see God, just hangin' around in his boxers, and though I liked the idea of spying on God, I began to wonder if the world would be a better place if the Romans had just put up with Jesus and let him die of old age...

And then there were the Football players, kneeling down, in front of everybody, thanking God, like he was their best friend, but then they'd jump up and spike the ball yelling, "I'm number ONE!!" and that confused me, for if your number one, what number is God??

Then I saw politicians trotting God out on a leash, like a racehorse they wanted to hop on and ride to the finish-line. But if they lost, it would be GOD's fault, and God would be the donkey they'd pin their problems on, and that was very nice of God, to be both a racehorse and a donkey.

And then there were those who said, "You'd better be good on earth, if you wanna get into heaven." like Heaven was the United States, and the Earth was Mexico, and angels were the Border Patrol. Like when you die you sit in a parked car on the outskirts of Heaven, the engine idling, your soul in the back-seat in one of those kennels used to carry small dogs on an airplane, as you listened to the radio, of all the people you ever wronged testify against you.

And then there's the church, which was like this cafeteria, where they serve God to you on these very un-Godlike plates, but I wanted my God PURE, not watered down by humans. So I had one of those catastrophe gods- you know, the one you called in an emergency, like God was the National Guard you call on to clean up the earthquake of your life.

So I got drunk one night, drove home, passed out behind the wheel, and woke up, going 60 mph straight at a brick wall, I slammed on the brakes, my heart banging like a wrecking-ball in my chest, staring at death's face, close enough to see that we had the same cheek-bones.

Now I have a God who's like a mechanic, who can fix anything. So when I wanna chew somebody's head off like salt-water taffy, or amputate my DNA, or open my wrists like windows that have been painted shut, I just put my soul into a box, like a busted computer, and haul it in. And He never asks to see my paperwork, or says that my warranty has expired. And I walk out feeling better.

And I don't care if He doesn't exist...
```

---

## IC-1566: Frankenstein Makes a Sandwich

- Title: Frankenstein Makes a Sandwich
- Author (byline): Adam Rex
- Work: Not specified
- Publisher: Harcourt Children's Books
- Publication date as stated: Sept 2006
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 976
- Already set (do not supply): none

### Source block (context only)

```text
Author: Adam Rex
ISBN: 978-0152057664
Publisher: Harcourt Children's Books
Date (Month/Year): Sept 2006
```

### Introduction (context only: never use it for content warnings)

```text
If you’ve ever seen Monsters, Inc., you know that monsters pay surprise visits to most children. They are queued up in every child’s imagination with a long list of characters from Santa Claus and the Tooth Fairy. And what’s more, children believe in the power of stories. Clap your hands and Tinkerbelle lives!

The problem is that stories are often “real” to young children whether they are happy, magical thoughts or crazy, scary ideas. Children believe if they think it, it’s true and monsters are “real.” But with a little bit of humor, the terrifying boogie man can become the loveable Mike and Sully from Monster, Inc. and Frankenstein may just be looking for a little snack.

A collection of poems from Frankenstein Makes a Sandwich by Adam Rex
```

### Performance text (classify this)

```text
An Open Letter from Wolfman’s Best Friend Dear Wolfman, I wanted to make some things clear. I know we’ve been roommates for nearly a year, and I probably should have said something before, but could you please try not to scratch the front door? If you want to come in, you should just use your keys. And if you forget the, then please, Wolfman, PLEASE! just knock, and I’ll happily open the door. And if I’m not home, please don’t howl anymore. ‘Cause each time you do it, the neighbors complain. And since we’re complaining, perhaps you’d explain how you manage to leave SO MUCH hair in the tub. I constantly clean it: I scour, I scrub, and I think I should mention it’s REALLY a pain. Today I removed a big clog from the drain, and I tell you, this hair-clog was of SUCH A SIZE it could go to a CAT SHOW AND TAKE HOME FIRST PRIZE! So . . . anyway, that’s all I wanted to write. Please take out the garbage. It’s your turn tonight.

And thank you, sincerely,

Your dog, Dynamite
Frankenstein Makes a Sandwich
When Frankenstein
prepared to dine
on ham-and-cheese on wheat,
he found, instead,
he had no bread
(or mustard, cheese or meat)

What could he do?
He thought it through
until his brain was sore,
And thought he ought
to see what he could
borrow from next door.

His neighbors gawked
as Frankie walked
the paths up to their porches.
Each time he tried,
the folks inside
would chase him off with torches.

“A MONSTER! EEK!”
the people shrieked.
“OH, make him go away!”
The angry hordes
unsheathed their swords,
pulled pitchforks out of hay.

They threw tomatoes,
pigs, potatoes,
loves of moldy bread.
And then a thought
struck Frankenstein
as pickles struck his head.

It's true, at first
he thought the worst:
His neighbors were so rude!
But then he found
that on the ground
They’d made a mound of food.

He piled it high and waved good-bye and shouted, “Thanks a bunch!”

Then stacked it on a plate and ate a big disgusting lunch.

***** The Creature from the Black Lagoon Doesn’t Wait and Hour Before Swimming

The Creature from the Black Lagoon
went back into the bog too soon.
“Too soon!” his doting mother cried.
“You just ate lunch! Come back inside!
That Black lagoon is dark and damp
You’re going to get a stomach cramp!
Just think of all you had for lunch:
A squid! Three eels! Hawaiian Punch!
A bag of chips! A crab knish!
A peanut-butter jellyfish!
You have to wait an hour of more!”

she shouted from the kitchen door.
Alas, the creature never heard.
He hadn’t listened to a word.
And rushing to the water’s bank,
he dived into the dismal dank . .
then gurgled, got a cramp and sank.
*****
The Dentist
Poor Son of Dracula. He’s just a dud.
His daddy is famous, but his name is mud.
For how much blood
could a bloodsucker suck,
if a bloodsucker can’t such blood? (ahem)

Everything’s fine if he suck on the throat
of a dog or a hog or a cat or a goat.
But a cold-blooded thing like a lizard or snake
makes his head start to hurt and his fangs really ache.

Frankenjunior was shocked. “You’ll have to go see the worst monster of all! She’s much worse than me. Her fingers are hooks! Hooks, needles, and spears!

Her voice is a high buzzing whine in your ears! Instead of a head there’s a BIG GLOWING EYE!” The Frankenboy said with a shuddering sigh.

“She doesn’t sound scary,” said Dracula’s son. “Not scary like crosses, or stakes, or the sun.” So he made his appointment for just after dark at the New Transylvania Medical Park.

“It’s awful,” he whispered. “So cheery and bright! You’d think it would kill them to turn off a light. They need some nice coffins. It’s really a shame,” young Dracula said as the nurse called his name.

He followed inside, and before he could hide, the dentist was standing there, right by his side! A note to the timid, or just faint of heart. This story has come to the frightening part. Stop *listening*! This is scary! Beware and be wary!

Still here? Very well. Little Drac stood in terror. He know now he’d made the most horrible error.

If he weren’t undead he’d have wanted to die> She was terrible! Awful! She smiled and said hi!

Her voice was a sweet lilting song in his ears.
Her fingers were fingers, not needles or spears.
That big glowing eye was a lamp, not a head.
It was all so much worse than The Frankenboy said!

Young Drac couldn’t move, so she forced him to sit.

“Open wide, now,” she told him. “This won’t hurt a bit!” “You aren’t flossing,” she scolded, and Dracula blushed. “And honestly, when was the last time you brushed? You really much brush after every bit. See? A cavity’s formed in this fang on the right.”

“It needs to be mended. And so, if you’re willing,
I’ll patch it right up with a small silver filling.”
A filling? With silver? Drac wanted to shout,
The werewolves will hate me! I’ve got to get out!

He changed to a bat – he flew up and away. The dentist said, “Fine. We won’t do it today.

But get it fixed soon; you’ll be glad that you did> Now here – take a sucker. You’ve been a good kid.”

He flew from the office, and homeward he raced.
He sucked on the sucker but gagged at the taste.
He’d hoped it was flavored like blood, or like liver,
How scary! It’s CHERRY! He thought with a shiver.

Drac new it was true as he spat and he cursed, My dad may be bad, but the dentist’s THE WORST.
```

---

## IC-1567: Freed Between the Lines

- Title: Freed Between the Lines
- Author (byline): Billy Collins, Belissa Escobedo, Rhiannon McGavin, Zariya Allen and Ellen Hopkins
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1142
- Already set (do not supply): none

### Source block (context only)

```text
Author: Billy Collins
Book: Censorship and Banned Books, Volume 3, Issue 1
ISBN: Magazine
Publisher: Random House, Inc.
Date (Month/Year): 2009
On-Line Location:
https://issuu.com/rhacademic/docs/rhi3
Authors: Belissa Escobedo, Rhiannon Mcgavin, and
Zariya Allen
Book: On-Line Transcript Only
Publisher: Genius.com / Get Lit
Date (Month/Year): July 25, 2014
On-Line Location: https://genius.com/Get-lit-somewhere-
in-america-annotated
Video of Live Performance can be found at:
2014 Brave New Voices (Finals)
https://www.youtube.com/watch?v=OadZpUJv8Eg
Author: Ellen Hopkins
ISBN: Poster
On-Line Location: https://ncac.org/wp-
content/uploads/import/BBWManifesto(1).pdf
Publisher: Simon & Schuster Children's Publishing
Date (Month/Year): 2009, 2010 and 2011
```

### Introduction (context only: never use it for content warnings)

```text
Book banning and censorship are nothing new, but you may have noticed more discussion lately in the news and on social media. It’s important to know that while some schools or communities may ban books, it does not make them illegal. Sometimes a ban on a book makes it just that much
```

### Performance text (classify this)

```text
Rain by Billy Collins
(Pg 1) Some time after the books had been forbidden—
The one about the woman and her daughter,
The one about the boy who spoke poorly—
And after the smoke from the incinerators had cleared,

It was suggested that censorship be extended To the plover, the wild turkey, and the common moorhen. But these birds have done nothing, a few protested. That is precisely the problem, the loudspeakers answered.

It rained that month day and night. . . Teachers disappeared on the way to their cars.

Then the committee came after the morning glory For its suggestive furling and unfurling And the ligustrum and the alstroemeria Because they were difficult to pronounce and spell. Then the pine tree for its tricky needles and cones And parsley and red and yellow peppers for no reason at

all. . .

And the rain was constant and cold—fine days
to curl up with a good book, someone joked—
but there were no more books,
just the curling up of people quietly in corners and

doorways,

bits of straw floating down the streets along the curbs into the turbulent rivers and out to sea.

more, well, intriguing. As parents and school boards lead the effort to erase uncomfortable interpretations of reality: Some examples? the Holocaust book Maus, discussions of gender identity in George M. Johnson’s All Boys Aren’t Blue, and provocative stories that could lead to political questioning -- The Handmaid’s Tale, anyone? -- they are not only limiting access but also perpetuating inequalities and dictating what stories have the right to be heard. In the words of author Stephen Chbosky, “Banning books gives us silence when we need speech. It closes our ears when we need to listen. It makes us blind when we need sight.” It’s time we Freed Between the Lines with poems by Billy Collins; Belissa Escobedo, Rhiannon McGavin, Zariya Allen; and Ellen Hopkins.

Somewhere in America by Belissa Escobedo, Rhiannon Mcgavin, and Zariya Allen

Here in America, in every single state, they have a set of

standards for every subject A collection of lessons that the teacher’s required to teach

by the end of the term But the greatest lessons you’ll ever teach us will not come

from your syllabus. The greatest lessons you will ever teach us, you will not

even remember

You never told us what we weren’t allowed to say We just learned how to hold our tongues Now somewhere in America, there is a child holding a copy

of “Catcher in the Rye” and there is a child holding a gun. But only one of these things have been banned by their

state government And it’s not the one that can rip through flesh It’s the one that says “f*** you” on more pages than one

Because we must control what the people say, and how

they think. And if they want to become the overseer of their own

selves, then we’ll show them a real one And somewhere in America, there’s a child sitting at his

mother’s computer reading the homepage of the KKK’s

website and that’s open to the public But that child will have never read “To Kill a Mockingbird”

because his school has banned it for its use of the “N”

word

Maya Angelou is prohibited because we’re not allowed to

talk about rape in school We were taught that “just because something happens,

doesn’t mean you are to talk about it” They build us brand-new shopping malls so that we’ll forget

where we’re really standing On the bones of the Hispanics, on the bones of the slaves,

on the bones of the Native Americans, on the bones of

those who fought just to speak!

Transcontinental Railroad to Japanese Internment Camps There are things missing from our history books But we were taught that it is better to be silent, than to

make them uncomfortable Somewhere in America, private school girls search for hours

through boutiques, trying to find the prom dress of their

dreams While kids on the south side spend hours searching through

the ‘lost and found’ ’cause winter’s coming soon and

that’s the only jacket they have

Kids are late to class for working the midnight shift They give awards for best attendance, but not for keeping

your family off the streets These kids will call your music “ghetto,” they will tell you

you don’t talk right Then they’ll get in the backseat of a car with all their friends

singing about how “They’re ‘bout that life” and “we can’t

stop” Somewhere in America, schools are promoting self

confidence While they whip out their scales and shout out your body

fat percentage in class

Where heftier girls are hiding away, and the slim fit

beauties can’t help but giggle with pride The preppy kids go thrift shopping ‘cause they think it

sounds real fun But we go because that’s all we’ve got money for ’Cause Momma works for the city, momma only gets paid

once a month Somewhere in America, a girl is getting felt up by a grown

man on the subway She’s still in her school uniform and that’s part of the

appeal It’s hard to run in knee-socks and Mary-Janes, and all her

male teachers know it too.

Coaches cover up star-players raping freshmen after the

dance Women are killed for rejecting dates, but God forbid I bring

my girlfriend to prom Girls black out drunk at the after-party, take a picture

before her wounds wake her How many pixels is your sanity worth? What’s a 4.0 to a

cold jury? What’d you learn in class today? Don’t walk fast, don’t speak loud, keep your hands to

yourself, keep your head down Keep your eyes on your own paper, if you don’t know the

answer, fill in ‘c’ Always wear ear buds when you ride the bus alone If you feel like someone’s following you, pretend you’re on

the phone

The teacher never fails, only you do Every state in America, the greatest lessons are the ones

you don’t remember learning.

Manifesto by Ellen Hopkins

You say you're afraid for children,
innocents ripe for corruption
by perversion or sorcery on the page.
But sticks and stones do break
bones, and ignorance is no armor.

You say you're afraid for America,
the red, white and blue corroded
by terrorists, socialists, the sexually
confused. But we are a vast quilt
of patchwork cultures and multi-gendered
identities. You cannot speak for those
whose ancestors braved
different seas.
You say you're afraid for God,
the living word eroded by Muhammed
and Darwin and Magdalene.
But the omnipotent sculptor of heaven
and earth designed intelligence.
Surely you dare not speak
for the father, who opens
his arms to all.
A word to the unwise.
Torch every book.
Char every page.
Burn every word to ash.
Ideas are incombustible . . .
```

---

## IC-1568: From the Afterlife

- Title: From the Afterlife
- Author (byline): Andrea Gibson
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 982
- Already set (do not supply): none

### Source block (context only)

```text
Author: Andrea Gibson
Book: Lord of the Butterflies, Pgs 41-42
ISBN: 978-1943735426
Publisher: Button Poetry
Date (Month/Year): Nov 2018
Author: Andrea Gibson
On-line Transcript:
https://andreagibson.substack.com/p/love-letter-
from-the-afterlife
ISBN: N/A
Publisher: Andrea Gibson
Date (Month/Year): Dec 21, 2023
```

### Introduction (context only: never use it for content warnings)

```text
Andrea Gibson, a celebrated poet and performance artist who through their verse explored gender identity, politics and their four-year battle with terminal ovarian cancer, died on July 14, 2025, at age 49. Tributes poured in from friends, fans and fellow poets who said Gibson’s words had changed their lives — and, in some cases, saved them. People terminal illnesses said Gibson made them less afraid of death by reminding them that we never really leave the ones we love.

"Love Letter from the Afterlife" originally written for Gibson’s wife Megan Falley, was shared online for anyone who is grieving.

Since the announcement of Gibson’s death, the poem has become a spiritual farewell to readers, listeners, and loved ones. “Dying is the opposite of leaving,” -- not as absence, but as presence magnified.

Love Letter from the Afterlife and Tincture by Andrea Gibson; may she rest in peace.
```

### Performance text (classify this)

```text
Tincture
Imagine, when a human dies, the soul misses the body,
actually grieves the loss of its hands
and all they could hold.

Misses the throat closing shy, reading out loud on the first

day of school.

Imagine the soul misses the stubbed toe, the loose tooth,

the funny bone. The soul still asks, Why does the funny bone do that? It's just weird.

Imagine the soul misses the thirsty garden cheeks watered

by grief.
Misses how the body could sleep through a dream.
What else can sleep through a dream?
What else can laugh?
What else can wrinkle the smile's autograph?

Imagine the soul misses each falling eyelash waiting to be

a wish.
Misses the wrist screaming away the blade.
The soul misses the lisp, the stutter, the limp.
The soul misses the holy bruise blue from that army of

blood rushing to the wound's side.

When a human dies, the soul searches the universe for
something blushing,
something shaking in the cold,
something that scars,
sweeps the universe for patience worn thin,
the last nerve fighting for its life,
the voice box aching to be heard.

The soul misses the way the body would hold another

body and not be two bodies but one
pleading god doubled in grace.
The soul misses how the mind told the body,
“You have fallen from grace.”
And the body said . . .
“Erase every scripture that doesn't have a pulse.”

There isn't a single page in the bible that can wince,
that can clumsy,
that can freckle,
that can hunger.
Imagine the soul misses hunger, emptiness, rage,
the fist that was never taught to curl-curled,
the teeth that were never taught to clench-clenched,
the body that was never taught to make love-made love

like a hungry ghost digging its way out of the grave.

The soul misses the unforever of old age,
the skin that no longer fits.
The soul misses every single day the body was sick,
the now it forced,
the here it built from the fever.
Fever is how the body prays,
how it burns and begs for another average day.

The soul misses the legs creaking up the stairs, misses the fear that climbed up the vocal cords to curse

the wheelchair.
The soul misses what the body could not let go –
what else could hold on that tightly to everything?
What else could see hear the chain of a swing set and fall

to its knees? What else could touch a screen door and taste lemonade? What else could come back from a war and not come

back? But still try to live? Still try to lullaby?

When a human dies the soul moves through the universe
trying to describe how a body trembles when it's lost,
softens when it's safe,
how a wound would heal given nothing but time.
Do you understand?
Nothing in space can imagine it.
No comet, no nebula, no ray of light can fathom
the landscape of awe, the heat of shame.
The fingertips pulling the first gray hair and throwing it

away.

I can't imagine it, the stars say. Tell us again about goosebumps. Tell us again about pain.

Love Letter from the Afterlife
My love, I was so wrong. Dying is the opposite of leaving.
When I left my body, I did not go away.
That portal of light was not a portal to elsewhere, but a

portal to here. I am more here than I ever was before. I am more with you than I ever could have imagined. So close you look past me when wondering where I am. It’s Ok. I know that to be human is to be farsighted. But feel me now, walking the chambers of your heart, pressing my palms to the soft walls of your living. Why did no one tell us that to die is to be reincarnated in

those we love while they are still alive? Ask me the altitude of heaven, and I will answer, “How tall are you?”

In my back pocket is a love note with every word you wish

you’d said. At night I sit ecstatic at the loom weaving forgiveness into

our worldly regrets. All day I listen to the radio of your memories.

Yes, I know every secret you thought too dark to tell me, and love you more for everything you feared might make

me love you less. When you cry, I guide your tears toward the garden of

kisses I once planted on your cheek,
so you know they are all perennials.
Forgive me, for not being able to weep with you.
One day you will understand.
One day you will know why I read
the poetry of your grief to those waiting to be born,
and they are all the more excited.
There is nothing I want for now that we are so close
I open the curtain of your eyelids with my own smile

every morning. I wish you could see the beauty your spirit is right now

making of your pain, your deep-seated fears playing musical chairs, laughing about how real they are not.

My love, I want to sing it through the rafters of your

bones, Dying is the opposite of leaving.

I want to echo it through the corridor of your temples, I am more with you than I ever was before. Do you understand?

It was me who beckoned the stranger who caught you in

her arms when you forgot not to order for two at the

coffee shop.

It was me who was up all night gathering sunflowers into

your chest the last day you feared you would never

again wake up feeling lighthearted.

I know it’s hard to believe, but I promise it’s the truth. I promise one day you will say it too. . . I can’t believe I ever thought I could lose you.
```

---

## IC-1569: From the Insane Asylum

- Title: From the Insane Asylum
- Author (byline): Joseph Kaufer
- Work: Not specified
- Publisher: McAllister Books
- Publication date as stated: Jan 1966
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: YOUNG MAN/WOMAN, SOCIETY RESPONDS, DOCTOR’S ANALYSIS, OUR SON
- Teaser before the introduction: Yes
- Spoken words (computed): 825
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joseph Kaufer
ISBN: 978-0910930000
Publisher: McAllister Books
Date (Month/Year): Jan 1966
```

### Introduction (context only: never use it for content warnings)

```text
The most influential institution that leads to anti-social behaviors in our society is THE FAMILY. What? Yes - not ill-intentioned – but very damaging.

See . . . Some parents are obsessed with the desire to ensure that their kids never have to face struggle, inconvenience, discomfort, or disappointment. Mistakes are swept under the table, excuses are made and bad behavior is explained away in the most positive terms possible. In fact, if their child does do something wrong, these parents are adept in turning the tables so that their little darling is the victim of an unjust and unreasonable society. Armed with verbal smart bombs, they are quick to blast away at anyone who sets high standards for behavior, morality, or achievement. And over time, society is left with adults who take no personal responsibility for their actions, who appreciate nothing and who acknowledge no authority. Effectively these parents are creating a generation of monsters. It’s insanity to the nth degree. And our educational systems, businesses, courts and psychologists are left to deal with the aftermath.

This collection of poems by Joseph Kaufer . . . . From the Insane Asylum spotlights the creation of these asocial “monsters.”
```

### Performance text (classify this)

```text
YOUNG MAN/WOMAN: (with arms wrapped as if in a straightjacket, voice these words in an ominous tone)

I in a straitjacket – you think that frightful? What do you think I was in Before I came here? (#11, page 18)

SOCIETY RESPONDS: (assume a reasonable voice of society in response to this question)

Better to be locked up now,
Than in full adult awareness collide
With courts, police, neighbors, juries, lawyers,
Humiliated ashamed relatives,
And come here stunned, frightened, from another world
Which denies and derides you;
Better to come now, child,
And be at once among your own. (#64, pg 57)

DOCTOR’S ANALYSIS: (assume the persona of a medical professional)

Since animals in the wild have no psychoses, What is there that sickens the mind in human society, Clogs the intellect, dries up the emotions, Causes people to agonize over nothing, Scream, weep, shout, become mute, rigid, overexcited? I had best not say it: there are two sacred institutions That will instantly take from me my professional position. (#117, pg 77)

OUR SON: The Parents Speak for Their Boy

(Use two voices for this poem, dividing the lines between both a mother and father persona)

When he slept on the floor and watered the ceiling, That was an idiosyncrasy.

When he stayed out of school And spent two days in a cistern, -- You know lots of kids play hookey.

When on the way home from the grocery He dropped the eggs on the sidewalk, one by one, And on arriving locked the cat in the refrigerator, That was just his own little humor.

When he found his parents’ life savings,
And went out and bought five thousand dollars worth of
bubble gum
And distributed it all by the handful
Among all the children of the town,
That was only a fancy, although painful.

When he slapped the school teacher
And pushed in the principal’s nose,
Saying it was too long
- Well, it is too long.

Why can’t they leave our son alone?

When he got a job at the grocery store
And spilled the molasses all over the floor
So the customers could slide more quickly in through the
door,
That was genius unappreciated.

When he shot the cow with the borrowed gun,
Then chased away the farmer,
He didn’t know it wasn’t open season,
And he only did it for fun;
And if he chased away the farmer
He must have had a good reason.

When he pulled the gasoline truck’s spigots open When the driver stepped out of sight And tossed a lighted match into it To see if it would really ignite, That was just scientific curiosity, There was no reason for the man to get so wild; It just shows in what direction our boy’s talent is bent, He’s really a talented child.

When he drove away in the Police Chief’s car,
And turned the siren on, and smashed it up against
An ornamental light pole,
Isn’t it enough that we paid for it all,
Do they have to torture his soul?

Why can’t they leave our son alone?

When he took all the money
Out of the other boy’s pocket,
He having spent all his own,
The inequality should be evident to all,
He was only trying to Make An Adjustment.

When he pulled the little girls’ panties down
To see what little girls look like,
And then exposed himself to their interested sight,
Any psychologist in town
Would tell you, that is only Normal.

When he was found by the police walking the streets Instead of at the fruit stand where he had obtained employment, And all the fruit man’s day’s receipts Were found in the pockets of our boy’s pants, -- He hadn’t done anything dishonest, He was only learning Finance.

When he set fire to the grain warehouse
To see the fire engines run, --
He ran no faster than anyone else,
Everybody likes a good fire.

Why can’t they leave our son alone?

When he told the judge before whom he was brought
That the judge looked like a pig
And that his wife was a female dog,
That was no more than the artist in him.
- For the judge is heavy, like a hog,
And his wife does resemble a Griffon.

When the psychologist appointed by the court Tried to interview our son, And all he would say was, blah, blah, blah, blah, Oink, oink, oink, oink, People just don’t understand him.

And when they told how he
Grabbed the old woman from behind in the dark
And pulled her down
And tried to roll her around in the alley, --
Why, all that boy needs is love.

Why can’t they leave our son alone? (#164, pg 116)

YOUNG MAN/WOMAN: (with arms wrapped as if in a straightjacket, voice these words in an ominous voice over your shoulder)

When my mother lay on the kitchen floor,
Begging me not to stab her more,
I could not feel or show her any mercy,
I could not forgive her for having made me.
(#199, pg 150)

DOCTOR’S ANALYSIS: (assume the persona of a medical professional)

Of all the creatures that on this earth creep, swim or
fly,
This, the so-called human is the only one
That kills for sport,
Seeks importance at the expense of others’ humiliations,
Wages war for sheer aggrandizement,
Acquires psychoses in the natural state,
Becomes an egotistical burden on impoverished relations.

For us to eliminate all the malign faults and divergencies of this species, Why, would be required the devising of the elimination of the race! (#277, page 202)
```

---

## IC-1570: The Fury of Rain Storms – A Collection

- Title: The Fury of Rain Storms – A Collection
- Author (byline): Anne Sexton, Sylvia Plath and Stephen King
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 828
- Already set (do not supply): none

### Source block (context only)

```text
Author: Anne Sexton
Book: The Complete Poems: Anne Sexton, Pg 372
ISBN: 978-0395957769
Publisher: Ecco
Date (Month/Year): April 1999
Author: Sylvia Plath
Book: Winter Trees, 1st poem in the collection
ISBN: 978-0571108626
Publisher: Faber and Faber
Date (Month/Year): Sept 1975
Author: Stephen King
Book: Skeleton Crew, Pgs 274-277
ISBN: 978-0451142931
Publisher: Signet Books
Date (Month/Year): June 1986
```

### Introduction (context only: never use it for content warnings)

```text
According to Stephen King . . .“ we’re all mentally ill; those of us outside the asylums only hide it a little better.”

Popular culture has long stereotyped poets as depressed and creative scientists as mad. In fact, the idea of a link between creativity and mental illness goes back to the time of Aristotle, when he wrote that eminent philosophers, politicians, poets and artists all have tendencies toward "melancholia."

Indeed, there are numerous examples of famous creators-- writers like Virginia Woolf, painters like Vincent Van Gogh, poets like Anne Sexton and Sylvia Plath -- who have been highly successful are suspected to have had some type of mental illness.

The Fury of Rainstorms – A Collection by Anne Sexton,
```

### Performance text (classify this)

```text
The Fury of Rain Storms by Anne Sexton

(Pg 372) The rain drums down like red ants,
each bouncing off my window.
The ants are in great pain
and they cry out as they hit
as if their little legs were only
stitched on and their heads pasted.
And oh they bring to mind the grave,
so humble, so willing to be beat upon
with its awful lettering and
the body lying underneath
without an umbrella.
Depression is boring, I think
and I would do better to make
some soup and light up the cave.

Sylvia Plath and Stephen King Apprehensions by Sylvia Plath

There is this white wall, above which the sky creates itself--- Infinite, green, utterly untouchable. Angels swim in it, and the stars, in indifference also. They are my medium. The sun dissolves on this wall, bleeding its lights.

A gray wall now, clawed and bloody.
Is there no way out of the mind?
Steps at my back spiral into a well.
There are no trees or birds in this world,
There is only sourness.

This red wall winces continually:
A red fist, opening and closing,
Two gray, papery bags---
This is what I am made of, this and a terror
Of being wheeled off under crosses and a rain of pietas.

On a black wall, unidentifiable birds Swivel their heads and cry. There is no talk of immortality among these!

Cold blanks approach us: They move in a hurry.

Paranoid: A Chant by Stephen King

(Pgs 274-277) I can’t go out no more.
There’s a man by the door
in a raincoat
smoking a cigarette.

But

I’ve put him in my diary
and the mailers are all lined up
on the bed, bloody in the glow
of the bar sign next door.

He knows that if I die (or even drop out of sight)

the diary goes and everyone knows the CIA`s in Virginia.

500 mailers bought from
500 drug counters each one different
and 500 notebooks
with 500 pages in every one.

I am prepared

I can see him from up here.
His cigarette winks from just
above his trench coat collar
and somewhere there’s a man on a subway
sitting under a Black Velvet ad thinking my name.

Men have discussed me in back rooms. If the phone rings there’s only dead breath.

In the bar across the street a snubnose
revolver has changed hands in the men’s room.
Each bullet has my name on it.
My name is written in back files
and looked up in newspaper morgues.

My mother’s been investigated; thank God she’s dead.

They have writing samples and examine the back loops of pees and the crosses of tees.

My brother’s with them, did I tell you?
His wife is Russian and he
keeps asking me to fill out forms.
I have it in my diary.
Listen--
listen
do listen:
you must listen.

In the rain, at the bus stop,
black crows with black umbrellas
pretend to look at their watches, but
it’s not raining. Their eyes are silver dollars.
Some are scholars in the pay of the FBI
most are the foreigners who pour through
our streets. I fooled them
got off the bus at 25th and Lex
where a cabby watched me over his newspaper.

In the room above me an old woman
has put an electric suction cup on her floor.
It sends out rays through my light fixture
and now I write in the dark
by the bar signs glow.

I tell you I know.

They sent me a dog with brown spots
and a radio cobweb in its nose.
I drowned it in the sink and wrote it up
in folder GAMMA.

I don’t look in the mailbox anymore. The greeting cards are letter-bombs.

(Step away! Goddamn you! Step away, I know tall people! I tell you I know very tall people!)

The luncheonette is laid with talking floors and the waitress says it was salt, but I know arsenic when it’s put before me. And the yellow taste of mustard to mask the bitter odor of almonds.

I have seen strange lights in the sky.
Last night a dark man with no face crawled through nine
miles
of sewer to surface in my toilet, listening
for phone calls through the cheap wood with
chrome ears.
I tell you man, I hear.

I saw his muddy handprints on the porcelain.

I don’t answer the phone now, have I told you that?

They are planning to flood the earth with sludge. They are planning break-ins.

They have got physicians
advocating weird sex positions.
They are making addictive laxatives
and suppositories that burn.

They know how to put out the sun with blowguns.

I pack myself in ice - have I told you that?
It obviates their infrascopes.
I know chants and I wear charms.
You may think you have me but I could destroy you
any second now.

Any second now.

Any second now.

Would you like some coffee, my love?

Did I tell you I can’t go out no more? There’s a man by the door in a raincoat.
```

---

## IC-1571: Gandhi’s Autobiography

- Title: Gandhi’s Autobiography
- Author (byline): Buddy Wakefield
- Work: Live for a Living
- Publisher: Write Bloody Publishing
- Publication date as stated: 2007
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 487
- Already set (do not supply): none

### Source block (context only)

```text
Author: Buddy Wakefield
Book: Live for a Living
ISBN: 978-0978998950
Publisher: Write Bloody Publishing
Date (Month/Year): 2007
```

### Introduction (context only: never use it for content warnings)

```text
We all say it: "I'm only human," and yet we continually get down on ourselves for making mistakes. So what exactly is human imperfection and why are we both comforted by it and constantly trying to make it disappear? Is human imperfection simply the number of mistakes made multiplied by the size of the mistake or is it really the lesson that's important? As children we learn by making mistakes. We touch a hot stove and remember not to do it again or we go through experiences with different people and learn from those mistakes how to react in certain situations. The size of the mistake or impact on our life tends to leave different impressions on each of us that cause us to react or think in a certain way whenever we encounter these situations again. It can be as simple as looking both ways before crossing to being terrified every time you cross the street. The mistakes we've made have a profound effect on each of us, but do we have to live our lives as if we are defined by our mistakes? Of course not, but people do it every day. Hey, nobody’s perfect. Not even Mahatma Gandhi. Gandhi’s Autobiography by Buddy Wakefield.
```

### Performance text (classify this)

```text
Gandhi’s autobiography is on my pillow.
I put it there every morning after making my bed
so I’ll remember to read it before falling asleep.
I’ve been reading it for 6 years.
I’m on Chapter 2.
Gary Necci gave me a book when he left my house one
time.
I don’t remember the title of it exactly
but I think it was called something like
“Kid, You Are Seriously Co-dependent.”
He thought I might wanna flip through and learn about
that.
I feel like it’s more important to finish Gandhi’s
autobiography first.
I keep forgetting to put focus on my to-do list.
I keep forgetting to wander and have fun.
I know I’m transparent
but my insecurities are in all the right places
so go ahead
have a look.
When I was a child I would chase my babysitter around
the house
viscerally sounding out the end of the letter “L”.

llllllllLLL
. . . lllll
Have another look.
When will we own ourselves completely?
Tell me what it is you want me to own
and I will take it.
Damaged goods?
You bet
Hit or miss?
No doubt about it.
Misses important social cues?

Yes,
I do.
I am dirty underneath the light
Pale on the backside of my bright
and feel a little bit stupid about learning a language
when I see God
because that guy . . .
so fast.

My best friend can speak six languages.
I still get excited that English took hold.
Sometimes I don’t feel like I’m doing my part on this
planet.
Sometimes I read without paying attention
hoping everything will just sorta sink in so that
if I ever need the answers -- like on a test --
my subconscious will somehow pull through for me.
I talk too much.
If you see me being quiet
don’t ask what’s wrong.
I’m just practicing.
I often wonder if anyone died because of
the pencil I handed to a prisoner at San Quentin.
He stuck it in his pocket.
The point is:
there are things wrong with us.
There are things wrong with me.
But I do have the ability to split epiphanies with my face
on demand.
Hold me like a birthmark,
awkward if you have to.
I wander,
so if you lose me,
don’t worry.
After the big tsunami
the only structure still standing in the wiped-out village
of Malacca
was a statue of Mahatma Gandhi.
I wanna be able to stand like that.
Even after getting gargled and spanked
and spit out by God,
I wanna know that I don’t have to fall
every time the sky opens up like a coin return
to change me
with its pudgy black fingers
tracing lines on maps
drawing circles around my blood
to show the scars here
in the shape of Gandhi on my pillow,
to show that I have been here before
and this is not the last time I’ve seen the light.
```

---

## IC-1572: Gender Boxes

- Title: Gender Boxes
- Author (byline): Macklemore and Ryan Lewis, Bradley Hathaway and Andrea Gibson
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1052
- Already set (do not supply): none

### Source block (context only)

```text
Author: Macklemore and Ryan Lewis
Book: From the Album “The Heist” (Track 5)
ISBN: N/A (Song Lyrics)
Publisher: Macklemore/RyanLewis Studios, Seattle, WA
Date (Month/Year): 2012
Lyrics can be found on-line at
https://genius.com/Macklemore-and-ryan-lewis-same-love-
lyrics
Author: Brian Hathaway
Book: All the Hits So Far But Don’t Expect Too Much . . .
ISBN: 978-0976364238
Publisher: Relevant Books
Date (Month/Year): Aug 2005
Author: Andrea Gibson
Book: Pole Dancing to Gospel Hymns
ISBN: 978-0981521305
Publisher: Write Bloody Publishing
Date (Month/Year): June 2008
```

### Introduction (context only: never use it for content warnings)

```text
Why are creative, expressive boys are labeled by our society as potentially gay? Or girls who would rather play with GI Joe than Barbie draw disapproving looks for being less than feminine. Ugh! I’m so tired of the Gay/Straight labeling. Every day people are forced to limit their individuality to fit into society’s gender stereotypes. To limit their masculinity or their femininity because of what people might think or say. It’s time to rip the lids from these . . .

Gender Boxes – a program including Same Love by Macklemore and Ryan Lewis, Manly Man by Bradley Hathaway and Swing-Set by Andrea Gibson
```

### Performance text (classify this)

```text
Same Love by Macklemore and Ryan Lewis (Song Lyrics)

When I was in the 3rd grade I thought that I was gay 'cause

I could draw
My uncle was and I kept my room straight
I told my mom, tears rushing down my face, she's like
"Ben you've loved girls since before pre-K"
Trippin', yeah, I guess she had a point, didn't she?
A bunch of stereotypes all in my head
I remember doing the math like "Yeah, I'm good a little

league" A pre-conceived idea of what it all meant For those who like the same sex had the [same]

characteristics . . .

Manly Man by Bradley Hathaway

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

TRANSITION

The final poem comes to us from the perspective of a female kindergarten teacher who has a powerful lesson that we all need to learn. Swing-set by Andrea Gibson.

Swing-set by Andrea Gibson

“Are you a boy or a girl?” he asks, staring up at me in all three feet of his pudding face grandeur, and I say “Dylan, you’ve been in this class for three years and you still don’t know if I’m a boy or a girl?” “Uh-uh.” “Well, at this point, I don’t really think it matters, do you?” “Uhm, no.

Can I have a push on the swing?”
And this happens every day.
It’s a tidal wave of kindergarten curiosity rushing straight
for the rocks of me, whatever I am.

In the class, when we discuss the Milky Way galaxy, the orbit of the Sun around the Earth or whatever. Jupiter, Saturn, Mars, and kids, do you know that some of the stars we see when we look up in the sky are so far away, they’ve already burned out? What do you think of that? Timmy? “Uh my mom says that even though you got hairs that grow from your legs, and the hairs on your head grow short and poky, and that you smell really bad, like my dad, that you’re a girl.” “Thank you, Timmy.” And so it goes.

On the playground, she peers up at me from behind her pink power puff sunglasses and then asks, “Do you have a boyfriend?”

And I say no, and she says “Oh… do you have a girlfriend?” And I say “No, but if by some miracle, twenty years from now, I ever finally do, then I’ll definitely bring her by to meet you. How’s that?” “Okay. Can I have a push on the swing?” And that’s the thing. They don’t care. They don’t care. Us, on the other hand. My father sitting across the table at Christmas dinner, gritting his teeth over his still-full plate, his appetite raped away by the intrusion of my haircut, “What were you thinking? You used to be such a pretty girl!” Frat boys, drunken, screaming, leaning out of the windows of their daddys’ SUVs, “Hey! Are you a faggot or a dyke?” And I wonder what would happen if I met up with them in the middle of the night.

Then of course there’s always the somehow not-quite-bright enough fluorescent light of the public restroom, “Sir!

Sir, do you realize this is the ladies’ room?” “Yes, ma’am, I do . . . “

But the best, the best is always the mother at the market, sticking up her nose while pushing aside her daughter’s wide eyes, whispering “Don’t stare, it’s rude.” And I want to say, “Listen, lady, the only rude thing I see is your paranoid parental hand pushing aside the best education on self that little girl’s ever gonna get, living with your Maybelline lipstick after hips and pedi kiwi, vanilla-smelling beauty; so why don’t you take your pinks and blues, your boy-girl rules and shove them in that car with your issue of Cosmo, because tomorrow, I start my day with twenty-eight minds who know a lot more than you. And if I show up in a pink frilly dress, those kids won’t love me any more, or less.”

“Hey, are you a boy or a — never mind, can I have a push on the swing?” And some day, y’all, when we grow up, it’s all gonna be that simple.
```

---

## IC-1573: Gentrification – A Collection

- Title: Gentrification – A Collection
- Author (byline): Angy Rivera, Bobby Lefebre and Niveli Travaski
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 997
- Already set (do not supply): none

### Source block (context only)

```text
Author: Angy Rivera
On-line only - Check for publication requirements at your
tournament before performing
Publisher: The Ultimate Queens Newsletter
Date (Month/Year): July 15, 2014
Full Poem can be found here
https://qns.com/wp-
content/uploads/2014/07/COMMUNITY-NOT-
CONDOMINIUMS4.pdf
Author: Bobby Lefebre
On-line only - Check for publication requirements at your
tournament before performing
Publisher: Buzzfeed.com (NSDA Approved Website)
Date (Month/Year): May 14, 2020
On-line Location
https://www.buzzfeed.com/laurasteinberg88/poetry-about-what-
home-means-3trqk1ektv
Author: Niyeli Trovaski
On-line only - Check for publication requirements at your
tournament before performing
Publisher: Buzzfeed.com (NSDA Approved Website)
Date (Month/Year): May 14, 2020
On-line Location
https://www.buzzfeed.com/laurasteinberg88/poetry-about-what-
home-means-3trqk1ektv
```

### Introduction (context only: never use it for content warnings)

```text
Since the age of 4, Angy Rivera has lived in the United States with a secret that threatens to upend her life: She is undocumented. Angy arrived with her mother, fleeing violence, poverty, and civil war in their native Colombia. For 20 years they live in the shadows, struggling to stay afloat financially and avoid deportation while battling a complex and inequitable immigration system and an urban landscape of gentrification.

Gentrification - when the character of a poor urban area is changed by wealthier people moving in, improving housing, and attracting new businesses, typically displacing current inhabitants in the process.

Gentrification – A Collection including “Community Not Condominiums by Angy Rivera; “Push Out (aka Denver, Where Have You Gone)” by Bobby Lefebre; and “Eviction” by Niyeli Trovaski
```

### Performance text (classify this)

```text
Community Not Condominiums by Angy Rivera Dona Maria is up before the sun rises It’s her job to feed others.

Arepas made with corn and cheese
Tamales wrapped up in leaves
Authentic café from the hills of Colombia
Packed in her food truck she makes her way down

Roosevelt Avenue.
Dona Maria knows these streets like her hands
Cracked and calloused.
The same streets she has walked up and down with her

family on hot summer nights.

(Spoken in various customer voices)
¿A cuánto los tamales?
Un café por favor sin azúcar
Solo una arepa hoy porque estoy cuidando mi figura
¡Hola Doña María como esta de bonita hoy!
¿Y sus hijos como están? *
Questions comments and food orders
This is the routine
What puts food on the table.
There are no strangers here.

(Scene shifts to speaker on the subway)
Last stop last stop
Stand clear of the closing doors
Two blocks up from the last stop you can buy

four dollar sushi roles
Hot pot dinners
Fried and steamed dumplings
Buy 1 get 1 free taro, coconut, apple, chocolate, mango

bubble teas milk tea, and green tea
Busy mall
Chinese New Year
Dim sum
Moon festivals
Red decorations
Admiring the dragon racing up and down the streets
It’s a tradition
There are no strangers here
This is community

How will Doña MarÍa sell her tamales, arepas, café y

chocolate When the streets become businesses she cannot

pronounce Will her café con leche compete with Starbucks? These signs of a cleaner and safer Queens erase the

resiliency already here We weren’t dirty to begin with Will her house stand untouched during gentrification?

My childhood is splattered across the windows of houses

and buildings in Queens Woodside, Corona, Elmhurst, Roosevelt and Flushing Home away from home The only communities that have nurtured my growth Where I met Mexican and Dominican food Where I learned to play dominoes and heard Bachata**

playing from the neighbor’s window

(Could insert a short acapella excerpt from a song)

Home away from home
Where I was welcomed since I was 4
Español spoken on my block I never felt alone or scared
Community not condominiums
There are no strangers here
Doña MarÍa packs up her truck
Her casita awaits
Tomorrow will be a new day
Filled with hopes that these streets will always

stay the same

Push Out (aka Denver, Where Have You Gone) by
Bobby Lefebre
I remember when my neighborhood
was just called the North side
Now they are calling it the “Highlands”.
They’re calling it progress....
Progress on the same Barrio streets those people once
warned their children to stay away from.
They say it is an evolution....... as if what had existed
there before was somehow subhuman
My neighborhood had history
Old Impalas and Monte Carlos have become Mercedes
Parking spots have been invaded by SUV’s and I have to
drive to get Mexican food.
They removed the tennis shoes
from the power line yesterday,
painted over a mural of La Virgin de Guadalupe, and
closed out another Brown-owned business .....they
replaced it with a “doggie daycare”.
Now the Police interaction with the changing
demographic is smiles and handshakes
Gentrification is as compassionate as a suicide bomber
detonating in a preschool schoolyard.
the pushers discuss popular culture
in an overpriced eatery
that used to be
a shop that sold herbal remedies
for people too poor for doctors and prescriptions
They have placed streetlamps
along the same walkways
where the darkness of night provided a shield for drug
deals, graffiti ridden walls have been painted over,
trashcans have been added to every corner,
and there is even a contraption
on the light post that carries baggies
for dog s***.
All of this in the name of beautifying the Barrio
All of this was asked for before
but back then......
it was only dirty Mexicans asking;
if they wanted a better neighborhood then why didn’t
they just move?

Now don’t get me wrong,
the barrio I knew
was not an ideal place for a flower to grow
There is nothing beautiful about drug deals and Brown
on Brown crime.
Nothing luring bout’ streets filled with litter and
disproportionate
illiteracy rates.
Living paycheck to paycheck has never been fashionable
There was beauty in the struggle though
before long, these people will have nowhere to go
I received the call yesterday
My landlord informed me he is “negotiating” a deal to
sell the property
on which my apartment sits
A deal that would leave him with a profit and us
packing.......
We have started to collect boxes

Eviction by Niyeli Trovaski
one more beautiful day
in the City of San Francisco
with its bridges and the bay
perfect hour for an eviction
oh San Francisco,
once the city of poets
Presidio swept clean -- museums expanded --
old hotels purified of the poor, shadows vaulted
into unknown precincts beyond the gate
picture pristine and proper neighborhoods
enjoy sterile rows of research and development --
learn to live forever and never face decrepitude --
a new breed of chefs
concoct salmon salad on an arugula bedding,
Zinfandel secreted in a rib eye steak --
wine bars where the decision-makers
nod as the wine is poured, sloshed in a glass,

yes excellent

dispossession is a misery the rich do not need to see, they may root for the Giants -- take pride in the signs of progress -- hit the ball out of the park and hearts swell past a vacated room that once gave shelter

those of you who must go
leave in silence, please make the premises
clean as you walk out of the front door,
don't steal anything

(Echo from Community Not Condominiums)
¿A cuánto los tamales?
Un café por favor sin azúcar
Solo una arepa hoy porque estoy cuidando mi figura
¡Hola Doña María como esta de bonita hoy!
¿Y sus hijos como están?*

Community not condominiums
There are no strangers here
*Translation:
How much are the tamales?
A coffee please without sugar
Just one arepa today because I'm taking care of my

figure Hello Doña María, how beautiful you are today! And how are your children?

** Bachata Music Sample https://www.youtube.com/watch?v=OrCUjqQYS3U
```

---

## IC-1574: Getting Out of Your Own Way

- Title: Getting Out of Your Own Way
- Author (byline): Linda Pastan, Danna Faulds, and Thich
- Work: Call Me By My True Names: The Collected Poems of Thich Nhat Hahn
- Publisher: Parallax Press
- Publication date as stated: 1999
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 665
- Already set (do not supply): none

### Source block (context only)

```text
The Obligation to Be Happy by Linda Pastan
Author: Linda Pastan
Book: Carnival Evening: New and Selected Poems 1968-
1998
ISBN: 978-0393046311
Publisher: W. W. Norton and Company Inc.
Date (Month/Year): 1998
Self-Observation Without Judgement by Danna Faulds
Author: Danna Faulds
Book: One Soul: More Poems From the Heart of Yoga
ISBN: 978-0974410616
Publisher: Peaceable Kingdom Books
Date (Month/Year): October 2003
Please Call Me By My True Name by Thich Nhat Hahn
Author: Thich Nhat Hahn
Book: Call Me By My True Names: The Collected Poems
of Thich Nhat Hahn
ISBN: 978-1888375169
Publisher: Parallax Press
Date (Month/Year): 1999
Cutting compliments of
Heather Whitney, Norfolk Public Schools, NE
```

### Introduction (context only: never use it for content warnings)

```text
From the moment we’re born until the day we die, we are told what to do and how to act. We have this idea that people have expectations for us and we need to meet their standards. And that should be good enough. However, I do not strive for a “perfect” life, but for a better tomorrow. No one should belittle you; in turn, you shouldn’t belittle yourself.

In the following program, through the poems The Obligation to Be Happy by Linda Pastan, Please Call Me by My True Name by Thich Nhat Hahn, and Self-Observation Without Judgment by Danna Faulds, we see the opportunity to give yourself room for change, mistakes, and success.

A program: Getting Out of Your Own Way - because we should all allow ourselves to grow.
```

### Performance text (classify this)

```text
Nhat Hahn.

The Obligation to Be Happy by Linda Pastan, Self- Observation Without Judgement by Danna Faulds, Please Call Me By My True Name by Thich Nhat Hahn (COLOR-CODED in splicing of poems)

Happiness. I try to hoist it on my narrow shoulders again—

It is more onerous
than the rites of beauty
or housework, harder than love.
But you expect it of me casually,
the way you expect the sun
to come up, not in spite of rain
or clouds but because of them.

Release the harsh and pointed inner voice. it's just a throwback to the past, and holds no truth about this moment.

Let go of self-judgment, the old, learned ways of beating yourself up for each imagined inadequacy.

Do not say that I will depart tomorrow because even today I still arrive

Do not say that I will depart tomorrow
because even today I still arrive
Look deeply: I arrive in every second
to be a bud on a spring branch
to be a tiny bird, with wings still so fragile
learning to sing in my new nest
to be a caterpillar in the heart of flower
to be a jewel hiding itself in stone

I still arrive, in order to laugh and to cry,
in order to fear and to hope,
the rhythm of my heart is the birth and death of
all that are alive.

Allow the dialogue within the mind
to grow friendlier, and quiet. Shift
out of inner criticism and life
suddenly looks very different.

I can say this only because I make
the choice a hundred times a day to release the
voice that refuses to
acknowledge the real me.

Do not say that I will depart tomorrow because even today I still arrive

And so I smile, as if my own fidelity
to sadness were a hidden vice—
that downward tug on my mouth,
my old suspicion that health
and love are brief irrelevancies,
no more than laughter in the warm dark
strangled at dawn.

I am the mayfly metamorphosing on the surface of the river, and I am the bird which, when spring comes, arrives in time to eat the mayfly. I am the frog swimming happily in the clear water of the pond, and I am also the grass-snake who, approaching in silence, feeds itself on the frog. I am the child in Uganda, all skin and bones, my legs as thin as bamboo sticks, and I am the arms merchant selling deadly weapons to Uganda. I am the 12-year-old girl, refugee on a small boat, who throws herself into the ocean after being raped by a sea pirate, and I am the pirate, my heart not yet capable of seeing and loving I am a member of the politburo, with plenty of power in my hands, and I am the man who has to pay his "debt of blood" to my people, dying slowly in a forced labour camp.

Do not say that I will depart tomorrow
because even today I still arrive
What's needed here isn't more prodding toward
perfection, but
intimacy - seeing clearly, and
embracing what I see.
Love, not judgment, sows the
seeds of tranquility and change.

My joy is like spring, so warm it makes flowers bloom in all walks of life. My pain is like a river of tears, so full it fills up the four oceans. Please call me by my true names, so I can hear all my cries and my laughs at once, so I can see that my joy and pain are one. Please call me by my true names, so I can wake up, and so the door of my heart can be left open, the door of compassion.

Happiness. I try to hoist it
on my narrow shoulders again—
a knapsack heavy with gold coins.
I stumble around the house,
bump into things.
Only Midas himself
would understand.

Do not say that I will depart tomorrow because even today I still arrive.
```

---

## IC-1575: The Ghosts of the Buffaloes

- Title: The Ghosts of the Buffaloes
- Author (byline): Vachel Lindsay
- Work: The Chinese Nightingale and Other Poems
- Publisher: Book Jungle
- Publication date as stated: July 2008
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 688
- Already set (do not supply): none

### Source block (context only)

```text
Author: Vachel Lindsay
Book: The Chinese Nightingale and Other Poems
ISBN: 978-1438500331
Publisher: Book Jungle
Date (Month/Year): July 2008
```

### Introduction (context only: never use it for content warnings)

```text
The telegram arrived in New York from Promontory Summit, Utah, at 3:05 p.m. on May 10, 1869, announcing one of the greatest engineering accomplishments of the century: The last rail is laid; the last spike driven; the Pacific Railroad is completed!

In the tremendous excitement of this transportation leap that would open up the country to growth and settlement, no one imagined the full and tragic impact of the Transcontinental Railroad, nor the speed at which it changed the shape of the American West. For in its wake, the lives of countless Native Americans were destroyed, and tens of millions of buffalo, which had roamed freely upon the Great Plains since the last ice age 10,000 years ago, were nearly driven to extinction in a massive slaughter made possible by the railroad.

Vachel Lindsay took notice, however and memorialized the loss in his poem . . . “The Ghosts of the Buffaloes.” Lindsay became famous in his day as a traveling bard whose dramatic delivery in public readings helped keep appreciation for poetry and the majesty of the buffalo alive in the American Midwest. And today, there are more than 200,000 bison in North America. “The Ghosts of the Buffaloes” by Vachel Lindsay.
```

### Performance text (classify this)

```text
Last night at black midnight I woke with a cry, The windows were shaking; there was thunder on high, The floor was a-tremble, the door was a-jar, White fires, crimson fires, shone from afar. I rushed to the door yard. The city was gone. My home was a hut without orchard or lawn. It was mud-smear and logs near a whispering stream, Nothing else built by man could I see in my dream... Then... Ghost-kings came headlong, row upon row, Gods of the Indians, torches aglow. They mounted the bear and the elk and the deer, And eagles gigantic, aged and sere, They rode long-horn cattle, they cried "A-la-la." They lifted the knife, the bow, and the spear, They lifted ghost-torches from dead fires below, The midnight made grand with the cry "A-la-la." The midnight made grand with a red-god charge, A red-god show, A red-god show, "A-la-la, a-la-la, a-la-la, a-la-la."

With bodies like bronze, and terrible eyes
Came the rank and the file, with catamount cries,
Gibbering, yipping, with hollow-skull clacks,
Riding white broncos with skeleton backs,
Scalp-hunters, beaded and spangled and bad,
Naked and lustful and foaming and mad,
Flashing primeval demoniac scorn,
Blood-thirsty and pomp amid darkness reborn,
Power and glory that sleep in the grass
While the winds and the snows and the great rains pass.
They crossed the gray river, thousands abreast,
They rode in infinite lines to the west,
Tide upon tide of strange fury and foam,
Spirits and wraiths, the blue was their home,
The sky was their goal where the star-flags are furled,
And on past those far golden splendors they whirled.
They burned to dim meteors, lost in the deep.
And I turned in dazed wonder, thinking of sleep.
And the wind crept by
Alone, unkempt, unsatisfied,
The wind cried and cried —
Muttered of massacres long past,
Buffaloes in shambles vast...
An owl said: "Hark, what is a-wing?"
I heard a cricket carolling,
I heard a cricket carolling,
I heard a cricket carolling.
Then...
Snuffing the lightning that crashed from on high
Rose royal old buffaloes, row upon row.
The lords of the prairie came galloping by.
And I cried in my heart "A-la-la, a-la-la,
A red-god show,
A red-god show,
A-la-la, a-la-la, a-la-la, a-la-la."
Buffaloes, buffaloes, thousands abreast,
A scourge and amazement, they swept to the west.
With black bobbing noses, with red rolling tongues,
Coughing forth steam from their leather-wrapped lungs,
Cows with their calves, bulls big and vain,
Goring the laggards, shaking the mane,
Stamping flint feet, flashing moon eyes,
Pompous and owlish, shaggy and wise.
Like sea-cliffs and caves resounded their ranks
With shoulders like waves, and undulant flanks.
Tide upon tide of strange fury and foam,
Spirits and wraiths, the blue was their home,
The sky was their goal where the star-flags are furled,
And on past those far golden splendors they whirled.
They burned to dim meteors, lost in the deep,
And I turned in dazed wonder, thinking of sleep.
I heard a cricket's cymbals play,
A scarecrow lightly flapped his rags,
And a pan that hung by his shoulder rang,
Rattled and thumped in a listless way,
And now the wind in the chimney sang,
The wind in the chimney,
The wind in the chimney,
The wind in the chimney,
Seemed to say: —
"Dream, boy, dream,
If you anywise can.
To dream is the work
Of beast or man.
Life is the west-going dream-storm's breath,
Life is a dream, the sigh of the skies,
The breath of the stars, that nod on their pillows
With their golden hair mussed over their eyes."
The locust played on his musical wing,
Sang to his mate of love's delight.
I heard the whippoorwill's soft fret.
I heard a cricket carolling,
I heard a cricket carolling,
I heard a cricket say: "Good-night, good-night,
Good-night, good-night,...good-night."
```

---

## IC-1576: The Gift and Train Platform: Munich to Dachau

- Title: The Gift and Train Platform: Munich to Dachau
- Author (byline): John Ciardi and Patricia Dobler
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 710
- Already set (do not supply): none

### Source block (context only)

```text
Author: John Ciardi
Book: The Collected Poems of John Ciardi
ISBN: 978-1557284495
Publisher: University of Arkansas Press
Date(Month/Year): April 1997
Author: Patricia Dobler
Book: Collected Poems
ISBN: 978-1932870053
Publisher: Autumn House Press
Date (Month/Year): May 2005
```

### Introduction (context only: never use it for content warnings)

```text
In the eyewitness account of William W. Quin of the 7th US Army: Dachau will stand for all time as one of history's most gruesome symbols of inhumanity. There our troops found sights, sounds and stenches beyond belief, cruelties so enormous as to be incomprehensible to the normal mind. Dachau and death were synonymous. John Ciardi in the previous poem The Gift and Patricia Dobler in the following: Train Platform: Munich to Dauchau pay tribute to the amazing people who survived the Holocaust.
```

### Performance text (classify this)

```text
The Gift by John Ciardi In 1945, when the keepers cried kaput Josef Stein, poet, came out of Dachau Like half a resurrection, his other half eighty pounds still in their invisible grave. Slowly then the mouth opened at first a broth, and then a medication, and then a diet, and all in time and the knitting mercies, the showing bones were buried back in flesh, and the miracle was finished. Josef Stein man and poet, rose, walked, and could even beget, and did, and later died of other causes only partly traceable to his first death. He noted - with some surprise at first - that strangers could not tell he had died once.

He returned to his post in the library, drank his beer, published three poems in a French magazine, and was very kind to the son who at last was his. In the spent of one night he wrote three propositions: That Hell is the denial of the ordinary. That nothing lasts. That clean white paper waiting under a pen is the gift beyond history and hurt and heaven.

Train Platform: Munich to Dachau By Patricia Dobler

1.
Two men, doubtless brothers, both huge
and with the same blank judicious face,
slump on a baggage cart. Near them
a decapitated deer, tied
to another cart. Sag of heavy meat,
blood stench, a pool of blood
widening on the station floor. Pay
attention, hisses the mind, a lesson here.
And it's true, in Munich's Hauptbahnhof
death's uniforms rise quite naturally,
the oiled machine of metaphor
glides easily. It sickens me
how easily the images align: Aztec priest
in cape of human skin, Carthaginian children
rolled into fiery pits, and this commonplace scene:
just hunter's meat and dull round faces.

2.
Dachau is a village known
for its fine views and 18th c. chateau,
and a German on holiday inquires
of his dining companions, "Why
do these Americans visit the Camp?
What is it they hope to see?"

3.

Early April, 1945; soon the war would be over. Some citizen of Dachau, an amateur photographer, leaned from his balcony early that morning. The sky was still gray; a slight drizzle fell. He saw walking in the street below his rooms a scraggly line of people. He got his camera, knelt behind his lace curtains (the edges show in the pictures) and took three photographs. Three: not one. Careful and deliberate, he recorded what he saw.

One: We see people walking; many are draped in blankets or rags that look, from this distance, like prayer shawls. No faces.

Two: We see a group of fifteen prisoners and, to one side, an armed guard. All the prisoners are stooped; one is humped, as if he carries a burden on his back, under the blanket which drapes him. The street is slick with rain; the figures are reflected in the street.

Three: We see many more people and we also glimpse the balcony from which the photograph was taken. A fine house is in the background—smoke puffs from the chimney, there are carved gables and windows. We see women in this group of prisoners. Some of them wear high-heeled shoes; their legs look white and bare.

4.
What do we hope to see? Carmelite nuns
live near the site of Barracks 26,
where the priests and ministers were stacked.
I think the sisters hope to see nothing;
they contemplate how blood and the empty mind
desire to converge and with their prayers
they refuse that coupling.
After the war the poets said,
"No poems about the camps," and
they were right, but still I hope
if not for an image, perhaps
for a small composition to place
against the blank-eyed brothers
back on the platform in Munich. I hope
to see again the young couple from Bremen
who struggled with their infant in his stroller,
rolling it over the difficult white stones
which cover the acres of Dachau. They pushed
the stroller from Jewish shrine to Catholic shrine,
then they stopped at the Carmelites' door.
They heard chants rising and falling, they saw
bright scraps of cloth fluttering from trees
in the courtyard. "What does this mean?"

they asked each other, not being Catholic or Jewish, but merely German, young, and of a mind to understand.
```

---

## IC-1577: Goblin Market

- Title: Goblin Market
- Author (byline): Christina Rossetti
- Work: Not specified
- Publisher: Chronicle Books
- Publication date as stated: Oct 1997
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2129
- Already set (do not supply): none

### Source block (context only)

```text
Author: Christina Rossetti
ISBN: 978-0811816496
Publisher: Chronicle Books
Date (Month/Year): Oct 1997
```

### Introduction (context only: never use it for content warnings)

```text
Christina Rossetti’s "Goblin Market" draws a fine line between fairy tale and reality. Although the main theme of the poem is temptation, symbolism throughout the text creates images of sin, sensual pleasure, the corruption of evil, and the affection for loved ones. It is this family bond that echoes most resonantly. Please share with me the story of Lizzie and Laura and note how Lizzie’s willingness to risk her own life in order to save her sister replaces this Victorian fairy tale with reality that speaks to each and every one of us. Goblin Market by Christina Rossetti.
```

### Performance text (classify this)

```text
Morning and evening
Maids heard the goblins cry:
"Come buy our orchard fruits,
Come buy, come buy:
Apples and quinces,
Lemons and oranges,
Plump unpecked cherries-
Melons and raspberries,
Bloom-down-cheeked peaches,
Swart-headed mulberries,
Wild free-born cranberries,
All ripe together
In summer weather--
Taste them and try:
Currants and gooseberries,
Bright-fire-like barberries,
Figs to fill your mouth,
Citrons from the South,
Sweet to tongue and sound to eye,
Come buy, come buy."
Evening by evening
Among the brookside rushes,
Laura bowed her head to hear,
Lizzie veiled her blushes:
Crouching close together
In the cooling weather,
With clasping arms and cautioning lips,
With tingling cheeks and finger-tips.
"Lie close," Laura said,
Pricking up her golden head:
We must not look at goblin men,
We must not buy their fruits:
Who knows upon what soil they fed
Their hungry thirsty roots?"
"Come buy," call the goblins
Hobbling down the glen.

"Look, Lizzie, look, Lizzie,
Down the glen tramp little men.
One hauls a basket,
One bears a plate,
One lugs a golden dish
Of many pounds' weight.

How fair the vine must grow
Whose grapes are so luscious;
How warm the wind must blow
Through those fruit bushes."
"No," said Lizzie, "no, no, no;
Their offers should not charm us,
Their evil gifts would harm us."
She thrust a dimpled finger
In each ear, shut eyes and ran:

Curious Laura chose to linger
Wondering at each merchant man.
Backwards up the mossy glen
Turned and trooped the goblin men,
With their shrill repeated cry,
"Come buy, come buy."
When they reached where Laura was
They stood stock still upon the moss,
Leering at each other,
Brother with queer brother;

Laura stared but did not stir,
Longed but had no money:
The whisk-tailed merchant bade her taste
In tones as smooth as honey,
The cat-faced purr'd,
The rat-paced spoke a word
Of welcome, and the snail-paced even was

heard;
But sweet-tooth Laura spoke in haste:
"Good folk, I have no coin;
To take were to purloin:
I have no copper in my purse,
I have no silver either,
And all my gold is on the furze
That shakes in windy weather
Above the rusty heather."
"You have much gold upon your head,"
They answered altogether:
"Buy from us with a golden curl."
She clipped a precious golden lock,
She dropped a tear more rare than pearl,
Then sucked their fruit globes fair or

red: Sweeter than honey from the rock, Stronger than man-rejoicing wine, Clearer than water flowed that juice; She never tasted such before, How should it cloy with length of use? She sucked and sucked and sucked the

more
Fruits which that unknown orchard bore,
She sucked until her lips were sore;
Then flung the emptied rinds away,
But gathered up one kernel stone,
And knew not was it night or day
As she turned home alone.
Lizzie met her at the gate
Full of wise upbraidings:
"Dear, you should not stay so late,
Twilight is not good for maidens;
Should not loiter in the glen
In the haunts of goblin men.

"Nay hush," said Laura.
"Nay hush, my sister:
I ate and ate my fill,
Yet my mouth waters still;
To-morrow night I will
Buy more," and kissed her.
"Have done with sorrow;
I'll bring you plums to-morrow

Early in the morning
When the first cock crowed his warning,
Neat like bees, as sweet and busy,
Laura rose with Lizzie:
Fetched in honey, milked the cows,
Aired and set to rights the house,
Kneaded cakes of whitest wheat,
Cakes for dainty mouths to eat,
Next churned butter, whipped up cream,
Fed their poultry, sat and sewed;
Talked as modest maidens should
Lizzie with an open heart,
Laura in an absent dream,
One content, one sick in part;
One warbling for the mere bright day's

delight,
One longing for the night.
At length slow evening came--
They went with pitchers to the reedy

brook;
Lizzie most placid in her look,
Laura most like a leaping flame.
They drew the gurgling water from its

deep Lizzie plucked purple and rich golden

flags, Then turning homeward said: "The sunset

flushes
Those furthest loftiest crags;
Come, Laura, not another maiden lags,
No wilful squirrel wags,
The beasts and birds are fast asleep."
But Laura loitered still among the rushes
And said the bank was steep.
And said the hour was early still,
The dew not fallen, the wind not chill:
Listening ever, but not catching
The customary cry,
"Come buy, come buy,"
With its iterated jingle
Of sugar-baited words:
Not for all her watching
Once discerning even one goblin
Racing, whisking, tumbling, hobbling;
Let alone the herds
That used to tramp along the glen,
In groups or single,
Of brisk fruit-merchant men.
Till Lizzie urged, "O Laura, come,
I hear the fruit-call, but I dare not look:
You should not loiter longer at this brook:
Come with me home.

Laura turned cold as stone
To find her sister heard that cry alone,
That goblin cry,
"Come buy our fruits, come buy."
Must she then buy no more such dainty

fruit? Must she no more such succous pasture

find,
Gone deaf and blind?
Her tree of life drooped from the root:
She said not one word in her heart's sore

ache; But peering thro' the dimness, naught

discerning, Trudged home, her pitcher dripping all

the way;
So crept to bed, and lay
Silent 'til Lizzie slept;
Then sat up in a passionate yearning,
And gnashed her teeth for balked desire,

and wept
As if her heart would break.
Day after day, night after night,
Laura kept watch in vain,
In sullen silence of exceeding pain.
She never caught again the goblin cry:
"Come buy, come buy,"
She never spied the goblin men
Hawking their fruits along the glen:
But when the noon waxed bright
Her hair grew thin and gray;
She dwindled, as the fair full moon doth

turn
To swift decay, and burn
Her fire away.
She no more swept the house,
Tended the fowls or cows,
Fetched honey, kneaded cakes of wheat,
Brought water from the brook:
But sat down listless in the chimney-nook
And would not eat.
Tender Lizzie could not bear
To watch her sister's cankerous care,
Yet not to share.
She night and morning
Caught the goblins' cry:
"Come buy our orchard fruits,
Come buy, come buy."
Beside the brook, along the glen
She heard the tramp of goblin men,
The voice and stir
Poor Laura could not hear;
Longed to buy fruit to comfort her,
But feared to pay too dear,
Till Laura, dwindling,
Seemed knocking at Death's door:
Then Lizzie weighed no more
Better and worse,
But put a silver penny in her purse,
Kissed Laura, crossed the heath with

clumps of furze
At twilight, halted by the brook,
And for the first time in her life
Began to listen and look.
Laughed every goblin
When they spied her peeping:
Came towards her hobbling,
Flying, running, leaping,
Puffing and blowing,
Chuckling, clapping, crowing,
Clucking and gobbling,
Mopping and mowing,
"Look at our apples
Russet and dun,
Bob at our cherries
Bite at our peaches,
Citrons and dates,
Grapes for the asking,
Pears red with basking
Out in the sun,
Plums on their twigs;
Pluck them and suck them,
Pomegranates, figs."
"Good folk," said Lizzie,
"Give me much and many"; --
Held out her apron,
Tossed them her penny.
"Nay, take a seat with us,
Honor and eat with us,"
They answered grinning;
"Our feast is but beginning.

Sit down and feast with us,
Be welcome guest with us,
Cheer you and rest with us."
"Thank you," said Lizzie; "but one waits
At home alone for me:
So, without further parleying,
If you will not sell me any
Of your fruits though much and many,
Give me back my silver penny
I tossed you for a fee."
They began to scratch their pates,
No longer wagging, purring,
But visibly demurring,
Grunting and snarling.
One called her proud,
Cross-grained, uncivil;
Their tones waxed loud,
Their looks were evil.
Lashing their tails
They trod and hustled her,
Elbowed and jostled her,
Clawed with their nails,
Held her hands and squeezed their fruits
Against her mouth to make her eat.
White and golden Lizzie stood,
Like a lily in a flood,
Like a rock of blue-veined stone
Lashed by tides obstreperously, --
Like a beacon left alone
In a hoary roaring sea,
Sending up a golden fire, --
Like a fruit-crowned orange-tree
White with blossoms honey-sweet
Sore beset by wasp and bee, --
Like a royal virgin town
Topped with gilded dome and spire
Close beleaguered by a fleet
Mad to tear her standard down.
One may lead a horse to water,
Twenty cannot make him drink.
Lizzie uttered not a word;
Would not open lip from lip
Lest they should cram a mouthful in;
But laughed in heart to feel the drip
Of juice that syruped all her face,
And lodged in dimples of her chin,
And streaked her neck which quaked like

curd.
At last the evil people,
Worn out by her resistance,
Flung back her penny, kicked their fruit
Along whichever road they took,
Not leaving root or stone or shoot.

In a smart, ache, tingle,
Lizzie went her way;
Knew not was it night or day;
Sprang up the bank, tore through the

furze,
Threaded copse and dingle,
And heard her penny jingle
Bouncing in her purse, --
Its bounce was music to her ear.
She ran and ran
As if she feared some goblin man
Dogged her with gibe or curse
Or something worse:

She cried "Laura," up the garden,
"Did you miss me ?
Come and kiss me.
Never mind my bruises,
Hug me, kiss me, suck my juices
Squeezed from goblin fruits for you,
Goblin pulp and goblin dew.
Eat me, drink me, love me;
Laura, make much of me:
For your sake I have braved the glen
And had to do with goblin merchant men."
Laura started from her chair,
Flung her arms up in the air,
Clutched her hair:
"Lizzie, Lizzie, have you tasted
For my sake the fruit forbidden?
Must your light like mine be hidden,
Your young life like mine be wasted,
Undone in mine undoing,
And ruined in my ruin;
Thirsty, cankered, goblin-ridden?"
She clung about her sister,
Kissed and kissed and kissed her:
Tears once again
Refreshed her shrunken eyes,
Dropping like rain
After long sultry drouth;
Shaking with aguish fear, and pain,
She kissed and kissed her with a hungry

mouth.
Her lips began to scorch,
That juice was wormwood to her tongue,
She loathed the feast:
Writhing as one possessed she leaped and

sung,
Rent all her robe, and wrung
Her hands in lamentable haste,
And beat her breast.
Swift fire spread through her veins,

knocked at her heart,
Met the fire smouldering there
And overbore its lesser flame,
She gorged on bitterness without a name:
Ah! fool, to choose such part
Of soul-consuming care!
Like a foam-topped water-spout
Cast down headlong in the sea,
She fell at last;
Pleasure past and anguish past,
Is it death or is it life ?
Life out of death.
That night long Lizzie watched by her,
Counted her pulse's flagging stir,
Felt for her breath,
Held water to her lips, and cooled her
face
With tears and fanning leaves:
But when the first birds chirped about

their eaves,
And early reapers plodded to the place
Of golden sheaves,
And dew-wet grass
Bowed in the morning winds so brisk to

pass,
And new buds with new day
Opened of cup-like lilies on the stream,
Laura awoke as from a dream,
Laughed in the innocent old way,
Hugged Lizzie but not twice or thrice;
Her gleaming locks showed not one thread

of gray,
Her breath was sweet as May,
And light danced in her eyes.
Days, weeks, months, years
Afterwards, when both were wives
With children of their own;
Their mother-hearts beset with fears,
Their lives bound up in tender lives;
Laura would call the little ones
And tell them of her early prime,
Would talk about the haunted glen,
The wicked, quaint fruit-merchant men,
Their fruits like honey to the throat,
But poison in the blood;
Would tell them how her sister stood
In deadly peril to do her good,
And win the fiery antidote:
Then joining hands to little hands
Would bid them cling together,
"For there is no friend like a sister,
In calm or stormy weather,
To cheer one on the tedious way,
To fetch one if one goes astray,
To lift one if one totters down,
To strengthen whilst one stands."
```

---

## IC-1578: The Greenwood Cycle

- Title: The Greenwood Cycle
- Author (byline): Ai
- Work: Dread: Poems
- Publisher: WW Norton and Company
- Publication date as stated: April 2003
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1326
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ai
Book: Dread: Poems
ISBN: 978-0393041439
Publisher: WW Norton and Company
Date (Month/Year): April 2003
```

### Introduction (context only: never use it for content warnings)

```text
The history of the United States has produced much in the way of race riots, from the New York City riots of 1862 to the Los Angeles riots of 1991, this country has experienced much civil unrest between blacks and whites. However, the Tulsa Race Riot of 1921 was perhaps the costliest incident of racial violence in American history. At the same time, it is perhaps the most marginalized, being almost forgotten until this decade.

On the morning of May 30, 1921, a young black man named Dick Rowland was riding in at Tulsa elevator. The white elevator operator, Sarah Page, claimed that Rowland grabbed her arm, causing her to flee in panic. Whispers of “assault and rape” were circulated in the local papers.

Tulsa police arrested Rowland the following day and began an investigation. a confrontation between black and white armed mobs around the courthouse soon ensued. Talk of lynching began, but the black were determined to prevent another such incident. Shots were fired and the outnumbered blacks began retreating to the Greenwood Avenue business district.

In the early morning hours of June 1, 1921, Black Tulsa was looted and burned by white rioters. Twenty-four hours after the violence erupted, it ceased. In the wake of the violence, 35 city blocks lay in charred ruins, over 800 people were treated for injuries and there were estimated reports of 300 deaths.

Ai in her poem The Greenwood Cycle brings this historic event to life in a series of poetic monologues to show this racial violence through the eyes of members of Tulsa’ black community.

The Greenwood Cycle by Ai.
```

### Performance text (classify this)

```text
(after the events surrounding the Tulsa Riots)

The Sheriff’s Explanation
I deputized a lot of men that day.
I didn’t say, “Are you men in the Klan,”
when they raised their hands
and swore to uphold the law.
All I cared about was whether they were willing to die.
If they did so in the service of the white race,
I could live with that.
I could not live with the disgrace
of allowing Negroes to get away
with rape, murder and worse.
If we didn’t stop them now, I thought,
we’d have to later.
Yes, innocent died,
depending on how you look at it.
You couldn’t tell who was what.

Miss Mary, old woman
used to cook dinner for us
when I was a boy
got caught in the middle of gunfire.
I drug her body out of the way of trampling feet,
least I could do,
but see, she was one of them . . . . .

Conjure
I thought I was dreaming
when I saw the sky fulla black smoke,
but I wasn’t, no, ‘cause I pinched myself
and it hut
and I knew we were gonna suffer
for somebody’s sinfulness.
“Just like Jesus,” you said, Mama,
when you screamed,
“Run, daughter, run,
white men are comin’, they got guns.”
I said, “I see ‘em, Mama I see,
they ridin’ up and down the street
throwin’ torches on rooftops, on porches,
on the poor Negro trying to pray
while the flames eat him up
they so hungry.
Mama, we can’t get away.”
“Run on, daughter,” you cried, “hide if you can
from the white devil,”
but he wasn’t no devil, he was a man
and he was evil, yes, he was,
but he wasn’t supernatural,
he didn’t have no power to conjure like I do,
when I conjure you,
crying, “Don’t look back, or you’ll turn to ashes
and fall down among the dead in Greenwood.”

Now I’m alone
and I don’t say nothing ‘bout it to nobody,
just fix me a hot toddy
and sit rocking in my rocker
and think about you, Mama,
turned to dust
wrapped in a dirty sheet
with a body lying on top.
“It ain’t Christian, is it,” you whisper
“to be murdered like this and just forgot?”
I rock in time to the ticktock of the grandfather clock
you dragged from the burning house,
because it was your daddy’s,
give to him by the old master
when your daddy got freedom.
For some reason, it didn’t burn up
just charred a bit,
a piece of wood pried off it.
When I got up the money,
I went and bought it off the junkman<
who thought it was worth something.
It was, but only to me,
rusted, permanently stopped
at the hour and the minute
that cost me you.

Sanctuary

“Is the world on fire?”

--Sister of Mr. Beard, survivor

I said, “Brother, the world’s on fire.”
He said, “Liar,”
but Daddy said, “Y’all climb up on higher
in that tree so only God can see you,
not me, or the white man running thisa way,
guns blazing, burning up everything.
Can’t see nothing through the smoke,
can’t breathe, choking like I got two hands
around my throat.
Je-e-e-sus, Je-e-e-sus.”
“Brother,” I whispered, and he said, “Hush,”
as a hot wind rustled the leaves
and the white man ran past,
screaming something about niggers and too much --
“What’d he say, brother?” I asked,
but he turned away.
“Lookayonder,” I heard him say,
just as a loud crack and a popping sound
got mixed up in my head.
When I climbed down that old tree, I said,
“Brother, are you dead?”
He just stared at me,
then outta nowhere someone grabbed my hair.
Daddy had braided it for me that morning
and tied a ribbon on it
and said, “I’m warning you don’t take it off,”
and I didn’t, but it come off anyway,
when the hand jerked too hard
and got a fist fulla red ribbon
and I started running myself.
Wasn’t nobody else but me around after ‘while
in the dark, back in the back of somebody’s house,
I mean underneath it,
where a dog was hiding too.
It was a hound dog with two pups.
You know how mean a new mother can be,
but she didn’t growl or nothing,
just gave me the eye
and went on back to nursing
and didn’t do nothing when I got real close
and stroked her fur and closed my eyes.
I woke to her sighs.
The pups’ eyes weren’t open yet,
but they moved their heads
when I started to crawl outta hiding,
but then I heard crying, I heard a shot
and moved on back
and got close to the dog and those pups.
I knew from that moment on
I was hound Mary’s daughter
and I would never leave.

The Rescue
I seen trouble coming from a long way off.
I seen it this morning in a bubble of blood
when I cut my finger on that cup I broke.
Nobody had to tell me about it.
I could see things. I had second sight.
Got it from Mama, a full-blooded Cherokee.
“Son,” she’d say, “you got one foot in Heaven
the other in Hell
Trouble gonna find you
wherever you dwell.
It’s gonna come in fire.
I know secrets I better not tell
and you will too, when the time comes.”
Here it is –
a Negro boy running fast as he can
a white man behind him
with a noose in his hand.
My daddy was Negro too.
Should I do something ‘cause halfa me
could also swing from a tree?
I don’t know what to do
til I remember Mama telling me
about the long walk
when so many people died on the Trail of Tears.
She said the old folks told her
nobody could believe Andrew Jackson
would make them leave their home, but he did.
the white man takes what he gives.

He’s got two faces and both of them smile
while he plans your destruction.
“He don’t like Indians, but he hates Negroes,” she said.
“You got looks and hair like your mother
you’re lucky that way,
defer to the white man, stay out of his path.”
“But I can’t Mama,” I say out loud,
“Can’t let a child die like this.
It ain’t right, is it?”
She answered, all right,
well, it was the wind,
but it was her voice talking through it.
I got in the wagon, all hitched ‘cause I was going
somewhere
and turned my mules in the path
where the white man was running and stopped there.
Gave that boy enough time to hide someplace.
White man cursed, pointed his gun at me.
“Sorry Mister, “I said,
“these mules got minds of their own.”
“Ain’t you part nigger?” he said to me,,
Then he shot my mules.
I knew he’d die in his sleep.
I saw the sowing he’d reap
and that released me from my hatred.
I buried Brandy and Brandywine
took a long time, said a few words.
One day, that boy came to see me.
He had a scar running down one side of his face.
He said, “Mister, I’m cold and hungry,
can I stay at your place?”
I said, “Yes, come on in the kitchen where it’s warm.
Lemme look at your face.
Maybe I got something that’ll help,”
but he said, “Nothing will.”
I filled his plate with pinto beans, bacon, cornbread,
filled his glass of milk to the brim,
then we said grace.
“Where’s your mama?” I asked
and he said, “Dead,
Yours?”
“Same. Pitiful, isn’t it?

You aim to move on, or stay?”
“Don’t you know?” he asked
I said, “Some things, not others.”
He said, “Your mother was a witch,
that’s what people say.”
“Naw, she wasn’t, she just saw things.”
“I ain’t too black for you?”
“I am too, “ I said
“No, you ain’t,” he answered,
“but you’ll do.”
```

---

## IC-1579: Hands Still Raised – A

- Title: Hands Still Raised – A
- Author (byline): Not specified
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 881
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jasmine Mans
Book: Black Girl, Call Home, Pg 86-89
ISBN: 978-0593197141
Publisher: Berkley
Date (Month/Year): Mar 2021
Author: Andrea Gibson
Book: Lord of the Butterflies, Pg 11-15
ISBN: 978-1943735426
Publisher: Button Poetry
Date (Month/Year): Nov 2018
```

### Introduction (context only: never use it for content warnings)

```text
Standing at the intersection of the LBGTQ community, faith, fury and grief, these poems refuse silence. They wrestle with a God shaped by human prejudice, with trans bodies treated as battlegrounds, and with the echo of gunfire still ricocheting from the Pulse Nightclub after the Orlando shooting. What does it mean to survive in a world that confuses love with sin and visibility with danger? This collection is an urgent call to raise our hands; to insist that humanity must be bigger than cruelty and that no one should have to hide who they truly are.

Hands Still Raised – A program including Maybe We Can fool God and Trans-panic by Jasmine Mans and Orlando by Andrea Gibson
```

### Performance text (classify this)

```text
Program with poems by Jasmine Mans and Andrea Gibson

Orlando by Andrea Gibson
(Pg 11-15) When the first responders
entered the Pulse nightclub
after the massacre in Orlando,
they walked through the horrific scene
of bodies and called out,
"If you are alive, raise your hand."

I was sleeping in a hotel
in the Midwest at the time,
but I imagine in that exact moment,
my hand twitched in my sleep,
some unconscious part of me aware
that I had a pulse
that I was alive . . . .

Maybe We Can Fool God by Jasmine Mans
(Pg 86-67) When a transwoman
is murdered
no one cares,
because we assume
God doesn’t either.

Maybe being a transwoman feels like an endless game of hide-and-seek with God.

Maybe God only knows us by our flesh.

Maybe we’ve made of our God
a wandering man,
with only our birth name
and baby photo.

One who hasn’t already measured the lineage of our selfhood, maybe He’s our fool.

Maybe when
a boy
becomes
a girl,
she fools God.

Fools Him good so good, that he wouldn’t be able to find her, wouldn’t be able to recognize her amongst the rest of us sinners.

Trans-Panic by Jasmine Mans
(Pg 88-89) I’ve heard of men who grip
and gargle foreign, yet
familiar, body parts, then
know not what to make of
their hands, but murder.

Lynching their lovers, then abandoning their bodies in unlocked motel rooms.

Trying to kill off
a part of themselves,
that has been left
a whisper.

I once read of a woman who spilled of herself a reddish bouquet.

Who was stabbed, so
many times, in her chest
it almost looked as
if someone was
trying to get away
with her heart.

She was found with duct tape over her mouth so she wouldn’t be able to tell the whole story, or, the love story.

Orlando by Andrea Gibson
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

my heart. Kept searching
the club for the fastest route
to every exit. I knew the person
working security was in a text war
and wasn't keeping his eyes
on the door; I knew there was a man
in the fifth row picking at the seams
of a red duffel bag.

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
put their hand up. (raise hand slowly)

(From the Intro) Humanity must be bigger than cruelty. No one should have to hide who they truly are.
```

---

## IC-1580: Harry Baker Collection (from) The Sunshine Kid

- Title: Harry Baker Collection (from) The Sunshine Kid
- Author (byline): Harry Baker
- Work: The Sunshine Kid
- Publisher: Burning Eye Books
- Publication date as stated: Dec 2014
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1426
- Already set (do not supply): none

### Source block (context only)

```text
Author: Harry Baker
Book: The Sunshine Kid
ISBN: 978-1909136281
Publisher: Burning Eye Books
Date (Month/Year): Dec 2014
```

### Introduction (context only: never use it for content warnings)

```text
Author Harry Baker was recently asked in an interview: What does it mean to be interesting? His reply . . . For me it’s about being different enough from the norm for people to sit up and take notice. It’s not about purposefully trying to be quirky; it’s more about being confident enough in who you are to not feel the need to dumb yourself down. And that’s what his poem The Sunshine Kid is all about. The Sunshine Kid by Harry Baker
```

### Performance text (classify this)

```text
The Sunshine Kid Old man sunshine was proud of his sun, And it brightened his day to see his little boy run,

Not because of what he’d done, nor the problems overcome, But that despite that his disposition remained a sunny

one. It hadn’t always been like this.

There’d been times when he’d tried to hide his

brightness, Every star hits periods of hardship, It takes a brighter light to inspire them through the

darkness.
If we go back to when he was born in a nebula,
We know that he never was thought of as regular,
Because he had a flair about him,
To say the Midas touch is wrong but all he went near

seemed to turn a little bronze, Yeah this sun was loved by some more than others, It was a case of Joseph and his dreamcoat and his

brothers Standing out from the crowd had its pros and its cons, And jealousy created enemies in those he outshone Such as the Shadow People.

Now the Shadow People didn’t like the Sunshine Kid, Because he showed up the dark things the Shadow

People did, And when he shone he showed the places where the

Shadow People hid,
So the Shadow People had an evil plan to get rid of him,
First up – they made fun of his sunspots,
Shooting his dreams from the sky, their words were

gunshots,
Designed to remind him he wasn’t very cool
And he didn’t fit in with any popular kids at school.
They said his head was up in space and they would bring

him down to earth, Essentially he came from nothing and that is what he

was worth, He’d never get to go to university to learn, Only degrees he’d ever show would be the 1st degree

burns From those that came too close, they told him he was

too bright,
That’s why no-one ever looked him in the eye,
His judgement became clouded and so did the sky,
With evaporated tears as the sun started to cry.

The sunshine kid was bright, with a warm personality, but inside he burned savagely – Hurt by the words and curses of the shadowy folk who spoke holes in his soul and left cavities, and as his heart hardened, his spark darkened, Every time they called him names it cooled his flame, He thought they might like him if he kept his light dim But they were busy telling lightning she had terrible aim, He couldn’t quite get to grips with what they said, So he let his light be eclipsed by what they said, He fell into a Lone Star State like Texas, And felt like he’d been punched in his solar plexus.

That’s when Little Miss Sunshine came along
Singing her favorite song
about how we’re made to be strong,
And you don’t have to be wrong to belong,
Just be true to who you are,
because we are all stars at heart.
Little miss sunshine was hot stuff –
The kind of girl when you looked at her you forgot stuff,
But for him, there was no forgetting her,
The minute he saw her, her image burned in his retina,
She was out of this world, and she accepted him,
Something about this girl meant he knew whenever she

was next to him,
Things weren’t as dark as they seemed,
and he dared to dream,
Shadows were nowhere to be seen;
when she was there he beamed,
His eyes would light up in ways that can’t be faked,
When she grinned her rays erased the razor-tipped

words of hate,
They gave each other nicknames
they were ‘cool star’ and ‘fun sun’,
And gradually the shadowy damage became undone,
She was one in a septillion,
and she was brilliant,
Could turn the coldest blooded reptilian vermillion,
Loved by billions,
from Chileans to Brazilians,
And taught the Sunshine Kid the meaning of resilience.

She said: “All the darkness in the world cannot put out the light of

a single candle,
So how the hell can they handle your light?
Only you can choose to dim it,
and the sky is the limit,
so silence the critics
by burning.”
If eyes are windows to the soul then she drew back the

curtains
And let the sunshine through the hurting.
In a universe of adversity two stars stuck together,
And though day becomes night the memories last

forever, Whether the weatherman said it or not, it would be fine, ‘Cause even behind the clouds the kid could still shine. The Sunshine Kid was bright, with a warm personality, And inside he burned savagely, Fueled by the fire inspired across galaxies, By the girl who showed him belief.

TRANSITION Now let’s take that same small concept and expand it to society as a whole. ‘Paper People’ is one of Harry Baker’s most successful poems, particularly because it takes the extended metaphor of a paper world and combines it with notions relevant to modern politics and current affairs. Paper People by Harry Baker.

Paper People
I like people.
I like some paper people.
They’d be purple paper people.
Maybe pop up purple paper people.
Proper pop up purple paper people.
‘How do you prop up pop up purple paper people?’
I hear you cry. Well I…

I’d probably prop up proper pop up purple paper people with a proper pop up purple people paperclip, but I’d pre-prepare appropriate adhesives as

alternatives,
a cheeky pack of blu tack just in case the paper slipped.
I could build a pop up metropolis.
but i wouldn’t wanna deal with all the paper people

politics. paper politicians with their paper-thin policies, broken promises without appropriate apologies. there’d be a little paper me, and a little paper you, and we’d watch paper TV and it would all be paper view. we’d watch the poppy paper rappers rap about their

paper package or watch paper people carriers get stuck in paper traffic

on the A4. There’d be a paper princess Kate but we’d all stare at

paper Pippa, and then we’d all live in fear of killer Jack the paper

ripper. cause the paper propaganda propagates the people's

prejudices, papers printing pictures of the photogenic terrorists.

There’d be a little paper me, and a little paper you, but in a pop up population people’s problems pop up too. there’d be a pompous paper parliament who remained out

of touch, and who ignored the people's protests about all the

paper cuts, then the peaceful paper protests would get blown to

paper pieces, by the confetti cannons manned by pre-emptive police. and there’d still be paper money, so there’d still be

paper greed, and the paper piggy bankers pocketing more than they

need. purchasing the potpourri to pepper their paper

properties, while others live in poverty and ain’t acknowledged

properly, a proper poor economy where so many are proper poor, but while their needs are ignored the money goes to big

wars,
funding origami armies building paper planes
while we remain imprisoned by our own paper chains,
and the greater shame, is that we always seem to stay

the same, what changes is who’s in power choosing how to lay the

blame, they’re naming names, forgetting these are names of

people, cause in the end it all comes down to people.

I like people. cause even when the situation’s dire, it is only ever people who are able to inspire, and on paper – it’s hard to see how we all cope, but in the bottom of pandora’s box there’s still hope, and i still hope cause i believe in people.

People like my Grandparents. who every single day

since i was born have taken time out of their morning to pray for me. that’s 7433 days straight of someone checking i’m okay

and that’s amazing. people like my aunt who puts on plays for prisoners.

people who are capable of genuine forgiveness. people who go out of their way to make your life better

and expect nothing in return. people have potential to be powerful. and just because the people in power tend to pretend to

be different, we don’t all need to
succumb to the system.
a paper population is no different.
there’d be a little paper me and a little paper you,
and we could watch paper TV and it would all be paper

view, and in a pop up population people's problems pop up too but even if the whole world fell apart then we’d still

make it through because we’re people.
```

---

## IC-1581: The Highwayman

- Title: The Highwayman
- Author (byline): Alfred Noyes
- Work: Not specified
- Publisher: Houghton Mifflin Harcourt
- Publication date as stated: Sept 1990
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1021
- Already set (do not supply): none

### Source block (context only)

```text
Author: Alfred Noyes
ISBN: 978-0152343408
Publisher: Houghton Mifflin Harcourt
Date(Month/Year): Sept 1990
```

### Introduction (context only: never use it for content warnings)

```text
“Give me liberty or give me death” was Patrick Henry’s adopted battle cry for the revolutionary war. That battle cry was not reserved solely for the men of the era, however. For most wives and mothers, it was a time of fear, uncertainty, terror as their husbands and sons went off to war. Such sacrifice should never be taken lightly. In tribute to the amazing strength of women and the unbreakable bond of love, I offer you The Highwayman by Alfred Noyes.
```

### Performance text (classify this)

```text
The wind was a torrent of darkness upon the gusty

trees, The moon was a ghostly galleon tossed upon cloudy seas, The road was a ribbon of moonlight looping the purple

moor,
And the highwayman came riding--
Riding--riding--
The highwayman came riding, up to the old inn door.

He'd a French cocked hat on his forehead, and a bunch

of lace at his chin; He'd a coat of the claret velvet, and breeches of fine

doe-skin. They fitted with never a wrinkle; his boots were up to

his thigh!
And he rode with a jeweled twinkle--
His rapier hilt a-twinkle--
His pistol butts a-twinkle, under the jeweled sky.

Over the cobbles he clattered and clashed in the dark

inn-yard, He tapped with his whip on the shutters, but all was

locked and barred, He whistled a tune to the window, and who should be

waiting there
But the landlord's black-eyed daughter--
Bess, the landlord's daughter--
Plaiting a dark red love-knot into her long black hair.

Dark in the dark old inn-yard a stable-wicket creaked Where Tim, the ostler listened--his face was white and

peaked-- His eyes were hollows of madness, his hair like mouldy

hay,
But he loved the landlord's daughter--
The landlord's black-eyed daughter;
Dumb as a dog he listened, and he heard the robber say:

"One kiss, my bonny sweetheart; I'm after a prize

tonight, But I shall be back with the yellow gold before the

morning light. Yet if they press me sharply, and harry me through the

day,
Then look for me by moonlight,
Watch for me by moonlight,
I'll come to thee by moonlight, though hell should bar

the way."

He stood upright in the stirrups; he scarce could reach

her hand, But she loosened her hair in the casement! His face

burnt like a brand As the sweet black waves of perfume came tumbling

o'er his breast,
Then he kissed its waves in the moonlight
(O sweet black waves in the moonlight!),
And he tugged at his reins in the moonlight, and galloped

away to the west.

He did not come in the dawning; he did not come at noon. And out of the tawny sunset, before the rise of the

moon, When the road was a gypsy's ribbon over the purple

moor,
The redcoat troops came marching--
Marching--marching--
King George's men came marching, up to the old inn-

door.

They said no word to the landlord; they drank his ale

instead, But they gagged his daughter and bound her to the foot

of her narrow bed. Two of them knelt at her casement, with muskets by

their side;
There was Death at every window,
And Hell at one dark window,
For Bess could see, through her casement, the road that

he would ride.

They had bound her up at attention, with many a

sniggering jest! They had tied a rifle beside her, with the barrel

beneath her breast! "Now keep good watch!" and they kissed her. She heard

the dead man say,
"Look for me by moonlight,
Watch for me by moonlight,
I'll come to thee by moonlight, though Hell should bar

the way."

She twisted her hands behind her, but all the knots held

good! She writhed her hands till her fingers were wet with

sweat or blood! They stretched and strained in the darkness, and the

hours crawled by like years,
Till, on the stroke of midnight,
Cold on the stroke of midnight,
The tip of one finger touched it! The trigger at least

was hers!

The tip of one finger touched it, she strove no more for

the rest; Up, she stood up at attention, with the barrel beneath

her breast. She would not risk their hearing, she would not strive

again,
For the road lay bare in the moonlight,
Blank and bare in the moonlight,
And the blood in her veins, in the moonlight, throbbed to

her love's refrain.

Tlot tlot, tlot tlot! Had they heard it? The horse-

hooves, ringing clear; Tlot tlot, tlot tlot, in the distance! Were they deaf that

they did not hear?
Down the ribbon of moonlight, over the brow of the hill,
The highwayman came riding--
Riding--riding--
The redcoats looked to their priming! She stood up

straight and still.

Tlot tlot, in the frosty silence! Tlot tlot, in the echoing

night! Nearer he came and nearer! Her face was like a light! Her eyes grew wide for a moment, she drew one last

deep breath,
Then her finger moved in the moonlight--
Her musket shattered the moonlight--
Shattered her breast in the moonlight and warned him--

with her death. He turned, he spurred to the West; he did not know who

stood Bowed, with her head o'er the casement, drenched in

her own red blood! Not till the dawn did he hear it, and his face grew grey

to hear
How Bess, the landlord's daughter,
The landlord's black-eyed daughter,
Had watched for her love in the moonlight, and died in

the darkness there.

Back, he spurred like a madman, shrieking a curse to the

sky, With the white road smoking behind him and his rapier

brandished high! Blood-red were his spurs in the golden noon, wine-red

was his velvet coat
When they shot him down in the highway,
Down like a dog in the highway,
And he lay in his blood in the highway, with the bunch of

lace at his throat.

And still on a winter's night, they say, when the wind is

in the trees, When the moon is a ghostly galleon tossed upon cloudy

seas, When the road is a gypsy's ribbon looping the purple

moor,
The highwayman comes riding--
Riding--riding--
The highwayman comes riding, up to the old inn-door.

Over the cobbles he clatters and clangs in the dark inn-

yard, He taps with his whip on the shutters, but all is locked

and barred, He whistles a tune to the window, and who should be

waiting there
But the landlord's black-eyed daughter--
Bess, the landlord's daughter--
Plaiting a dark red love-knot into her long black hair.
```

---

## IC-1582: Hir and Swing-Set

- Title: Hir and Swing-Set
- Author (byline): Alysia Harris and Aysha El-
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1111
- Already set (do not supply): none

### Source block (context only)

```text
Author: Alysia Harris and Aysha El-Shamayleh
Book: Unheard Voices: Stories of LGBT History
ISBN: None – Educational Material
Publisher(s):
Gay, Lesbian and Straight Education Network
Anti-Defamation League
Story Corps
Date (Month/Year): 2011
This Educational Material from the Book Unheard Voices
can be found at
https://www.yumpu.com/en/document/read/27382894/hir-
by-alysia-harris-and-aysha-el-shamayleh-anti-defamation-
Author: Andrea Gibson
Book: Pole Dancing to Gospel Hymns
ISBN: 978-0981521305
Publisher: Write Bloody Publishing
Date (Month/Year): June 2008
```

### Introduction (context only: never use it for content warnings)

```text
Everyone has to go through hard times in life and that’s what makes us all equal. Everyone can relate to sitting in front of someone they love and not knowing what to say for fear of being judged. This is what’s wrong in the world. People are afraid to be who they are because they are afraid of what OTHER people will think of them.

In Hir by Alysia Harris and Aysha El-Shamayleh, we see a student . . . withdrawn, silent, alone . . . afraid of being judged . . . afraid of being true to herself or is it himself?

In the hope that knowledge will lead to understanding, I’ve chosen poetry about acceptance. The voices of these poets are honest, authentic and need to be heard.
```

### Performance text (classify this)

```text
Shamayleh / Andrea Gibson

HIR by Alysia Harris and Aysha El-Shamayleh

Melissa sits in the back of the classroom afraid to speak up. She pulls awkwardly at her extra loose khaki cargo pants. She doesn’t want the boys to notice her. James finds himself at the back of a classroom.

His baseball cap casts a shadow on his pimple-stained
forehead.
A wide shirt hangs on his broad shoulders,
But no one ever noticed him.

Melissa,
The teacher asks,
And she says nothing because she is not here,
And Melissa has never been here,
Because Melissa is just some abstract jumble of syllables

that doesn’t fit her position. She is not what she seems, She doesn’t want to have to explain to her mother for the

232nd time why she doesn’t want to wear a dress to prom, Doesn’t paint her face, it’s ’cause her whole body is painted

on.

Melissa, Melissa.

James doesn’t want to have to explain where he came

from, ’Cause with the exception of Melissa he has been deemed

an abstract reality by everyone.

All he wishes for is to get to wear a tuxedo to prom. And Melissa’s been tucking in breasts that’ll be growing for

three years now, Been using duct tape to press them down and mold them

more into pecs. She just wishes that people would understand that at birth

her genitals didn’t know which way to grow, Mad at God who couldn’t relay a message directly to her hormones that they should produce more testosterone. The only person who understands her is James, And they have been playmates since the age of four, Around the time girls notice boys and boys notice girls. See, James’ family wanted daughters instead of sons, And Melissa was always like that male beetle that everyone called a ladybug.

Melissa, Melissa, where is she?

Sometimes she wishes she could rip the skin off her back, Every moment of everyday she feels trapped in the flesh of

a stranger.

Melissa.

As she stands to her feet wanting to say

“I'm here, and I’ve been here since I was born, so quit

asking me if I’m a him or a her,
’Cause when you combine the two pronouns you get H.I.R,
Hir,
And God combined the two genders and put me in this

body transgendered. I’m here, so quit talking about me like I’m not here.”

James falls back into Melissa’s skin, And the two comfort each other in syncopated heartbeats, Waiting for the day when Melissa can finally scrub off this

made up genetic makeup, When the teacher asks for James, and he can say

“I’m here.”

TRANSITION

It’s that simple . . . “I am here.” Be true to yourself . . . accept who you are and expect that others will also. It’s that simple. But also, so very difficult . . .

These poems are about gender identification, but accepting who you are isn’t limited to this situation. Whether you are coming out, telling people you are getting a divorce, you are pregnant, or even that you are dying; it is key that you make it known and be true to yourself . . .

Remember, there is no harder, there’s just hard. Everyone has their own closet, and a closet is no place for someone to be living. It’s that simple. . . once you’ve accepted yourself.

Swing-Set by Andrea Gibson

“Are you a boy or a girl?”
he asks, staring up at me in all three feet of his pudding
face grandeur, and I say “Dylan,
you’ve been in this class for three years and you still don’t
know if I’m a boy or a girl?”
“Uh-uh.”
“Well, at this point, I don’t really think it matters, do you?”
“Uhm, no.
Can I have a push on the swing?”
And this happens every day.
It’s a tidal wave of kindergarten curiosity rushing straight
for the rocks of me, whatever I am.

In the class, when we discuss the Milky Way galaxy, the orbit of the Sun around the Earth or whatever. Jupiter, Saturn, Mars, and kids, do you know that some of the stars we see when we look up in the sky are so far away, they’ve already burned out? What do you think of that? Timmy?

“Uh my mom says that even though you got hairs that grow from your legs, and the hairs on your head grow short and poky, and that you smell really bad, like my dad, that you’re a girl.” “Thank you, Timmy.” And so it goes.

On the playground, she peers up at me from behind her pink power puff sunglasses and then asks, “Do you have a boyfriend?” And I say no, and she says “Oh… do you have a girlfriend?” And I say “No, but if by some miracle, twenty years from now, I ever finally do, then I’ll definitely bring her by to meet you. How’s that?” “Okay. Can I have a push on the swing?” And that’s the thing. They don’t care. They don’t care. Us, on the other hand. My father sitting across the table at Christmas dinner, gritting his teeth over his still-full plate, his appetite raped away by the intrusion of my haircut, “What were you thinking? You used to be such a pretty girl!”

Frat boys, drunken, screaming, leaning out of the windows of their daddys’ SUVs, “Hey! Are you a faggot or a dyke?” And I wonder what would happen if I met up with them in the middle of the night.

Then of course there’s always the somehow not-quite-bright enough fluorescent light of the public restroom, “Sir! Sir, do you realize this is the ladies’ room?” “Yes, ma’am, I do . . . “

But the best, the best is always the mother at the market, sticking up her nose while pushing aside her daughter’s wide eyes, whispering “Don’t stare, it’s rude.” And I want to say, “Listen, lady, the only rude thing I see is your paranoid parental hand pushing aside the best education on self that little girl’s ever gonna get, living with your Maybelline lipstick after hips and pedi kiwi, vanilla-smelling beauty; so why don’t you take your pinks and blues, your boy-girl rules and shove them in that car with your issue of Cosmo, because tomorrow, I start my day with twenty-eight minds who know a lot more than you. And if I show up in a pink frilly dress, those kids won’t love me any more, or less.”

“Hey, are you a boy or a — never mind, can I have a push on the swing?” And some day, y’all, when we grow up, it’s all gonna be that simple.
```

---

## IC-1583: A History of Fury and Faith

- Title: A History of Fury and Faith
- Author (byline): Not specified
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1138
- Already set (do not supply): none

### Source block (context only)

```text
Author: Langston Hughes
Book: The Collected Works of Langston Hughes,
Volume 1, Pg 60
ISBN: 978-0826213396
Publisher: University of Missouri
Date (Month/Year): June 2001
Author: Amanda Gorman
Book: Call Us What We Carry, Pgs 153-157
ISBN: 978-0593465080
Publisher: Viking Books
Date (Month/Year): Jan 2024
Author: Joshua Sands
Book: Turning Points, Pg 39-46
ISBN: 978-0742117013
Publisher: Tichenor Publishing
Date (Month/Year): 2001
```

### Introduction (context only: never use it for content warnings)

```text
Equal opportunity has been the bedrock of American democracy, and our country’s diversity one of our greatest strengths. But recently diversity, equity and inclusion (DEI) programs have come under attack in American boardrooms, state legislatures – and now across the federal government. DEI has become a social and political lightning rod for those activists who feel such initiatives are unfair and even racist against white Americans. America, who do we want to be?

As Americans, do we value diversity and want to ensure that there is equity and inclusion for everyone . . . OR have we gone too far? Are unqualified women, immigrants, and people of color being given preferential treatment simply because of DEI efforts? I don’t have the answers, but these poets may provide some insight into this quagmire of opposing thoughts . . .

A History of Fury and Faith containing Mother to Son by Langston Hughes, Faith and Fury by Amanda Gorman and An Abridged History of America by Joshua Sands
```

### Performance text (classify this)

```text
Amanda Gorman and Joshua Sands

Mother to Son by Langston Hughes
(Pg 60) Well, son, I’ll tell you:
Life for me ain’t been no crystal stair.
It’s had tacks in it,
And splinters,
And boards torn up,
And places with no carpet on the floor—
Bare.
But all the time
I’se been a-climbin’ on,
And reachin’ landin’s,
And turnin’ corners,
And sometimes goin’ in the dark
Where there ain’t been no light.
So boy, don’t you turn back.
Don’t you set down on the steps
’Cause you finds it’s kinder hard.
Don’t you fall now—
For I’se still goin’, honey,
I’se still climbin’,
And life for me ain’t been no crystal stair.

Fury and Faith by Amanda Gorman
(Pg 153-157) You will be told this is not a problem,
Not your problem.
You will be told now is not the time
For change to begin,
Told that we cannot win.

But the point of protest isn’t winning; It’s holding fast to the promise of freedom, Even when fast victory is not promised.

Meaning, we cannot stand up to police
If we cannot cease policing our imagination,
Convincing our communities that this won’t work,
When the work hasn’t even begun,
That this can wait,
When we’ve already waited out a thousand suns.
By now, we understand
That white supremacy
& the despair it demands
Are as destructive as any disease.

So when you’re told that your rage is reactionary, Remind yourself that rage is our right.

It teaches us it is time to fight.
In the face of injustice,
Not only is anger natural, but necessary,
Because it helps carry us to our destination.

Our goal is never revenge, just restoration.
Not dominance, just dignity.
Not fear, just freedom.
Just justice . . .

When our fire can no longer be fueled by fury,
We will always be fortified by faith . . .
This is more than protest
It’s a promise.

An Abridged History of America by Joshua Sands

(Pg 39-46) God bless America.
Land that
I
love.
We set forth
for this
great
land
With beautiful English
ships,
English
money,
English
people.
We got settled with
English
help,
English food
shipments,
English medical
remedies.
We settled
and we spat on the
English,
shot the
English,
poured tea
on the English,
declared independence
from the
English.
Thanks
for the
memories, England.
Now leave.

We’re comin’ to America.

Indians treated
the land
with
respect.
So we shot
them,
raped them,
moved them
to five square
blocks south of
Phoenix, Arizona.
We’ll even pay
the Indians
if they show
us a
raindance.
Entertain us –
We should celebrate
Thanksgiving
by watching the
turkey with
it’s head chopped
off.
Bleed and run.
Run and bleed.
We’ll catch up to you.

OK – everyone squeeze in! You can all fit, dammit. Yes, those are all the names of the people who went to Vietnam. No, you can’t visit them. Now smile!

We purchased
Blacks from
Africa,
whipped them,
beat them,
kept them illiterate,
Called them 3/5
of a regular
American
(for census
purposes only).
Even when they were
“freed”

they were uneducated,
scoffed at,
laughed at,
spat on.
Only now they
were homeless
and
hungry.
Thanks, Blacks,
For picking our
cotton.
We’re warm.
Now,
go build
a
fire.

I’m confused who you Americans look up to.
Who do you respect in your country?
You mock your leader on talk shows
and impersonate him to create a cartoon.
Who do you look up to?
We have Nobel Prize winners, novelists,
Inventors, and political officials.
You have mistresses, lotto winners,
movie stars, and basketball players.

We fought some
wars for rightful
causes:
Weird people
out there:
Stalin,
Hitler
beware.
Yet we were
and are
the only people
to drop an
A-Bomb on anyone.
And then do it again
for
emphasis.

I came to America to witness the future
I learned the language.
I brought my own money.
I came to America because they say it is the land of dreams.
I did not come to America to live here.
The street is not safe and I’m getting older.
I want to leave America, but have no money.
I want to leave America, but can’t find directions.
On those carnival rides, they let you off when you get sick.
Please stop.
I want off.

We’re homeless in America.

The Blacks found a leader:
Martin Luther King.
so we
shot
him.
We found a leader:
JFK
so we
shot him.
Our leader had a brother:
Robert
so we
shot him, too
We found a singer:
John Lennon
and we shot
him, too
because we
were out of
leaders.

Buy American!
Don’t let the Japanese take over!
The Japanese school day is roughly ten hours,
consisting of rigorous study
in the sciences,
languages,
composition,
mathematics,
history.
The American school day is roughly six and one half hours,
consisting of the same subjects,
With recesses,
study halls,
club meetings,
and convocations mixed in.
The Japanese are ahead because they know mathematics:
six and a half mixed hours
do not equal
Ten quality hours.
But, still, buy American!

We went to war in Vietnam
Because it would
make us feel better.
People protested
the War
because it would
make them feel better.
People did drugs,
had free sex,
wore tie dye,
got shot.
In protest.
And it made them
geel better.

Estimated value of Beanie Baby: $800.

Person who makes Beanie Baby: Annual income, $800.

I was told the other day that we donated over ten billion

dollars to other countries in the name of foreign relief. This will improve their quality of living, or so I’m told. I was told the other day that my son needs an operation. I was told the other day that without it he will not survive. I was told the other day to put up collection jars in the

community.
I was told the other day to pray.
The other day I prayed.
The other day I prayed for a miracle.
The other day I went to the grocery store and picked up

eight dollars In loose change. Today I will pray again.

We elected an actor
to be President –
so we wouldn’t have
to train him
how to lie.
Besides,
he looked
good on TV.
And the Alzheimer’s
jokes were funny
later on
weren’t they?
The Ayatollah took
hostages and we didn’t
shoot him.
Castro was Satan;
we didn’t
shoot him.
Saddam crossed the line
so we shot his people
and their children
but didn’t shoot
him.

We sit in our
air-conditioned
condominium
with our Volvo’s
and our e-mail
and voice mail
and cupboards full
of food
and *75* inch TV’s
With 73 channels
and cordless phones
and power tools
and jet-skis
and mutual fund reports
and Guess watches
and 2.5 kids and
a Dalmatian named
Spot.
And we say that
we deserve it
because we’re
American.
And we buy it
Every time.
```

---

## IC-1584: The Hollow Men

- Title: The Hollow Men
- Author (byline): T.S. Eliot
- Work: Not specified
- Publisher: Longman
- Publication date as stated: March 2000
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 427
- Already set (do not supply): none

### Source block (context only)

```text
Author: T.S. Eliot
ISBN: 978-0582424593
Publisher: Longman
Date (Month/Year): March 2000
```

### Introduction (context only: never use it for content warnings)

```text
Modern man is hollow from the inside. Wisdom, spirituality and morality based on faith are nowhere to be found. Efforts to generate collective wisdom to promote the cause of humanity have failed miserably. Instead our society has attached prime importance to material possessions. The result is that beneath our hollowness is an absence of a spiritual basis. No elevation is possible without it; for our society to survive, faith must be restored to modern men, lest we continue to exist as The Hollow Men described by T.S. Elliott
```

### Performance text (classify this)

```text
I

We are the hollow men
We are the stuffed men
Leaning together
Headpiece filled with straw. Alas!
Our dried voices, when
We whisper together
Are quiet and meaningless
As wind in dry grass
Or rats’ feet over broken glass
In our dry cellar

Shape without form, shade without colour, Paralysed force, gesture without motion;

Those who have crossed
With direct eyes, to death’s other Kingdom
Remember us—if at all—not as lost
Violent souls, but only
As the hollow men
The stuffed men.

II

Eyes I dare not meet in dreams
In death’s dream kingdom
These do not appear:
There, the eyes are
Sunlight on a broken column
There, is a tree swinging
And voices are
In the wind’s singing
More distant and more solemn
Than a fading star.

Let me be no nearer
In death’s dream kingdom
Let me also wear
Such deliberate disguises
Rat’s coat, crowskin, crossed staves
In a field
Behaving as the wind behaves
No nearer—

Not that final meeting In the twilight kingdom

III

This is the dead land
This is cactus land
Here the stone images
Are raised, here they receive
The supplication of a dead man’s hand
Under the twinkle of a fading star.

Is it like this
In death’s other kingdom
Waking alone
At the hour when we are
Trembling with tenderness
Lips that would kiss
Form prayers to broken stone.

IV

The eyes are not here
There are no eyes here
In this valley of dying stars
In this hollow valley
This broken jaw of our lost kingdoms
In this last of meeting places
We grope together
And avoid speech
Gathered on this beach of the tumid river

Sightless, unless
The eyes reappear
As the perpetual star
Multifoliate rose
Of death’s twilight kingdom
The hope only
Of empty men.

V

Here we go round the prickly pear
Prickly pear prickly pear
Here we go round the prickly pear
At five o’clock in the morning.

Between the idea
And the reality
Between the motion
And the act
Falls the Shadow

For Thine is the Kingdom

Between the conception
And the creation
Between the emotion
And the response
Falls the Shadow

Life is very long

Between the desire
And the spasm
Between the potency
And the existence
Between the essence
And the descent
Falls the Shadow

For Thine is the Kingdom

For Thine is Life is For Thine is the

This is the way the world ends
This is the way the world ends
This is the way the world ends
Not with a bang but a whimper.
```

---

## IC-1585: Holy Saturday and Long Term Memory

- Title: Holy Saturday and Long Term Memory
- Author (byline): James Tate
- Work: Return to the City of White Donkeys
- Publisher: Ecco
- Publication date as stated: November 2004
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1017
- Already set (do not supply): none

### Source block (context only)

```text
Author: James Tate
Book: Return to the City of White Donkeys
ISBN: 978-0060750015
Publisher: Ecco
Date(Month/Year): November 2004
```

### Introduction (context only: never use it for content warnings)

```text
There is a philosophy of interconnectedness . . . Everyone you meet in your life — even total strangers — is already intimately connected to you. The idea that we are all separate and distinct beings is nothing but an illusion. We are all parts of a larger whole, like individual cells in a body.

You don’t have to “build” relationships with others because you’re already connected. You need only tune into the pre-existing connection that’s already there. All relationships are significant; none are irrelevant. Even the strangers you pass on the street are important parts of you.

No one makes this point more eloquently than James Tate in his narrative poem, Holy Saturday.
```

### Performance text (classify this)

```text
Holy Saturday I came out of the store, and the first thing I saw was a man in a bunny suit dancing down the sidewalk, handing out chocolate eggs to everyone. Never take candy from strangers was the first thing that leapt to mind. I wanted to reach the car before he caught up with me. He saw this, and took a giant hop in my direction. "Here, this is for you, Mr. Get-away-as-fast-as-you-can," he said.

"I don’t want it," I said. "I'm allergic to chocolate."

He made a fist with his paw and threatened my nose. "Take it, " he said, "you can give it to a child, and they will thank you."

"I don't know any children, and besides, how do I know there isn't arsenic in there. I don’t know you. You're a complete stranger to me. You might be an escaped convict, a child molester, or a murderer."

"I'm the Easter bunny, you asshole. If you can't trust the Easter bunny, you're in pretty bad shape. Take the egg before I shove it down your throat," he said.

I grabbed him by the shoulders and threw him up against my car. The whiskers on his nose were twitching. His long, floppy ears looked pathetic. "You are about to become a very wounded bunny," I said.

"Maybe we could talk this over, over a beer or something. What do you say?" the bunny said.

A couple of teenagers had gathered to see what I might do next. They were excited. I, who've never been in a fight, really wanted to punch the bunny. But, instead, I dragged him off the car. I took his basket out of his paw and threw it in the trash can. "Now go home and get out of that suit. There's enough crime in this town without you impersonating the Easter bunny and handing out suspicious substances to little children," I said.

"I was trying to do a good thing," he said. "I was trying to bring a little cheer and good will, that’s all."

"But you've got a bunny suit on, for God’s sake. And you were dancing on the sidewalk like an idiot. Why should anyone trust you?" I said.

"Let’s rip that suit off of him and see who he really is," one of the teenagers said. The bunny looked really frightened. He was half bent over, as if about to hop.

"No," I said, "I think he's learned his lesson" The boys seemed disappointed, and I was starting to worry about the safety of the bunny. "Get in the car," I said to him.

"What?" he said. "I said, get in the car. I'll drive you home." I unlocked the car and got into the driver’s seat. The bunny seemed confused, but did as I had said. He told me where he lived, and we drove there in silence. He lived in a run-down apartment complex. Half the domestic crime in town took place right there. When I stopped he started to open the door. He looked so defeated.

"What do you do, I mean, in real life?" I said.

"I'm unemployed right now," he said. "Every time I get a job the place closes down. It’s like I'm the kiss of death." Hearing this from a raggedy-assed Easter bunny should have been funny, but it wasn't. It nearly broke my heart.

"I'm sorry I ruined your day. Honestly, I don’t know what came over me. Maybe I was envious of your happiness," I said.

"That’s what’s great about the bunny suit," he said, "no one can see your tears. Thanks for the ride. After nearly killing me, you saved my life. Makes a perfect story. Unfortunately, I've got no one to tell it to." He got out of the car and started hopping across the little, gravelly yard. I never even saw his face or got his name.

TRANSITION And another memory is stored . . . . Elizabeth Loftus once said, "We fill in gaps in our memory using chains of events that are logically acceptable. Our biases, expectations, and past knowledge are all used in the filling-in process, leading to distortions in what we remember." And when other s encourage these possible memories, the leap to remembered greatness can sometimes be quite, quite small. Long-Term Memory by James Tate.

Long-Term Memory
I was sitting in the park feeding pigeons
when a man came over to me and scrutinized my
face right up close. "There's a statue of you
over there," he said. "You should be dead. What
did you do to deserve a statue?" "I've never seen
a statue of me," I said. "There can't be a statue
of me. I've never done anything to deserve a
statue. And I'm definitely not dead." "Well,
go look for yourself. It's you alright, there's
no mistaking that," he said. I got up and walked
over where it was. It was me alright. I looked
like I was gazing off into the distance, or the
future, like those statues of pioneers. It didn't
have my name on it or anything, but it was me.
A lady came up to me and said, "You're looking at
your own statue. Isn't that against the law, or
something?" "It should be," I said, "but this is
my first offense. Maybe they'll let me off light."
"It's against nature, too," she said, "and bad
manners, I think." "I couldn't agree with you
more," I said. "I'm walking away right now, sorry."
I went back to my bench. The man was sitting there.
"Maybe you're a war hero. Maybe you died in the
war," he said. "Never been a soldier," I said.
"Maybe you founded this town three hundred years
ago," he said. "Well, if I did, I don't remember
it now," I said. "That's a long time ago," he
said, "you coulda forgot." I went back to feeding
the pigeons. Oh, yes, founding the town. It was
coming back to me now. It was on a Wednesday.
A light rain, my horse slowed . . .
```

---

## IC-1586: Homage to Paul Cezanne

- Title: Homage to Paul Cezanne
- Author (byline): Charles Wright
- Work: The World of the Ten Thousand Things
- Publisher: Farrar, Straus and Giroux
- Publication date as stated: Sept 1991
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1102
- Already set (do not supply): none

### Source block (context only)

```text
Author: Charles Wright
Book: The World of the Ten Thousand Things
ISBN: 978-0374523268
Publisher: Farrar, Straus and Giroux
Date (Month/Year): Sept 1991
```

### Introduction (context only: never use it for content warnings)

```text
One of the great mysteries of life is what will happen after we die. You may wonder at times” why is life so hard?” or “what happens after death?” I believe that death is not the end, but rather just a step that we must all take. Death separates us from this temporal world but does not end our existence. Poet Charles Wright explores death and art in his Homage to Paul Cezanne. Cezanne was an artist of the late 1800’s whose work inspired the modern art of the 20th century. He believe that what we see is only a representation of the complexities of life and human existence, and Charles Wright exposes that same understanding of the mysteries of life. Homage to Paul Cezanne by Charles Wright. If you are troubled with the thought of dying or with losing a loved one, then please allow the power of this message to comfort your heart.
```

### Performance text (classify this)

```text
At night, in the fish-light of the moon, the dead wear
our
white shirts
To stay warm, and litter the fields.
We pick them up in the mornings, dewy pieces of paper
and
scraps of cloth.
Like us, they refract themselves. Like us,
They keep on saying the same thing, trying to get it
right.
Like us, the water unsettles their names.

Sometimes they lie like leaves in their little arks, and
curl up at
the edges.
Sometimes they come inside, wearing our shoes, and walk
From mirror to mirror.
Or lie in our beds with their gloves off
And touch our bodies. Or talk
In a corner. Or wait like envelopes on a desk.

They reach up from the ice plant. They shuttle their messengers through the oat grass. Their answers rise like rust on the stalks and the spidery leaves.

We rub them off our hands.

Each year the dead grow less dead, and nudge
Close to the surface of all things.
They start to remember the silence that brought them
there.
They start to recount the gain in their soiled hands.
Their glasses let loose, and grain by grain return to the
river
bank.
They point to their favorite words
Growing around them, revealed as themselves for the
first
time:
They stand close to the meanings and take them in.

They stand there, vague and without pain,
Under their fingernails, an unreturnable dirt.
They stand there and it comes back,
They music of everything, syllable after syllable
Out of the burning chair, out of the beings of light.
It all comes back.
And what they repeat to themselves, and what they
repeat to
themselves,
Is the song that our fathers sing.

In steeps and sighs,
The ocean explains itself, backing and filling
What spaces it can't avoid, spaces
In black shoes, their hands clasped, their eyes teared at
the
edges:
We watch from the high hillside,
The ocean swelling and flattening, the spaces
Filling and emptying, horizon blade
Flashing the early afternoon sun.

The dead are constant in
The white lips of the sea.
Over and over, through clenched teeth, they tell
their story, the story each knows by heart:
Remember me, speak my name.
When the moon tugs at my sleeve,
When the body of water raises and becomes the body of
light,
Remember me, speak my name.

The dead are a cadmium blue. We spread them with palette knives in broad blocks and planes. We layer them stroke by stroke In steps and ascending mass, in verticals raised from the earth.

We choose, and layer them in, Blue and a blue and a breath,

Circle and smudge, cross-beak and buttonhook,
We layer them in. We squint hard and terrace them line
by
line.

And so we are come between, and cry out, And stare up at the sky and its cloudy panes,

And finger the cypress twists. The dead understand all of this, and keep in touch,

Rustle of hand to hand in the lemon trees, Flags, and the great sifts of anger

To powder and nothingness. The dead are a cadmium blue, and they understand.

The dead are with us to stay. Their shadows rock in the back yard, so pure, so black, Between the oak tree and the porch.

Over our heads they're huge in the night sky.
In the tall grass they turn with the zodiac.
Under our feet they're white with the snows of a
thousand
years.

They carry their colored threads and baskets of silk To mend our clothes, making us look right, Altering, stitching, replacing a button, closing a tear. They lie like tucks in our loose sleeves, they hold us together.

They blow the last leaves away. They slide like an overflow into the river of heaven. Everywhere they are flying.

The dead are a sleight and a fade
We fall for, like flowering plums, like white coins from
the
rain
Their sighs are gaps in the wind.

The dead are waiting for us in our rooms,
Little globules of light
In one of the far corners, and close to the ceiling,
hovering,
thinking our thoughts.

Often they'll reach a hand down,
Or offer a word, and ease us out of our bodies to join
them in
theirs.
We look back at our other selves on the bed.

We look back and we don't care and we go.

And thus we become what we've longed for,
past tense and otherwise,
A BB, a disc of light,
song without words.
And refer to ourselves
In the third person, seeing that other arm
Still raised from the bed, fingers like licks and flames in
the
boned air.

Only to hear that it's not time.
Only to hear that we must re-enter and lie still, our
arms at
rest at our sides,
The voices rising around us like mist

And dew, it's all right, it's all right, it's all right . . .

The dead fall around us like rain.
They come down from the last clouds in the late light
for the
last time
And slip through the sod.

They lean uphill and face north.
Like grass,
They bend toward the sea, they break toward the
setting sun.

We filigree and we baste. But what do the dead care for the fringe of words, Safe in theirs suits of milk? What do they care for the honk and flash of a new style?

And who is to say if the inch of snow in our hearts is rectitude enough?

Spring picks the locks of the wind.
High in the night sky the mirror is hauled up and
unsheeted.
In it we twist like stars.

Ahead of us, through the dark, the dead Are beating their drums and stirring the yellow leaves.

We're our here, our feet in the soil, our heads craned up
at the
sky,
The stars streaming and bursting behind the trees.

At dawn, as the clouds gather, we watch
The mountain glide from the east on the valley floor,
Coming together in starts and jumps.
Behind their curtain, they bear
Amber across the heavens, serene as black coffee . . .

Whose unction can intercede for the dead? Whose tongue is toothless enough to speak their piece?

What we are given in dreams we write as blue paint, Or messages to the clouds. At evening we wait for the rain to fall and the sky to clear. Our words for the clay, uttered in undertones, Our gestures salve for the wind.

We sit out on the earth and stretch our limbs, Hoarding the little mounds or sorrow laid up in our hearts.
```

---

## IC-1587: Homesick: A Plea for our Planet

- Title: Homesick: A Plea for our Planet
- Author (byline): Andrea Gibson
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 946
- Already set (do not supply): none

### Source block (context only)

```text
Author: Amanda Gorman
ISBN: N/A
Publisher: Ohio Energy.org
Date (Month/Year): August 28, 2018
Full Text available at: https://ohioenergy.org/wp-
content/uploads/2021/03/Earthrise-Poem-by-Amanda-
Gorman.pdf
Author: Andrea Gibson
Book: You’d Better Be Lightning, Pgs 36-39
ISBN: 978-1943735990
Publisher: Button Poetry
Date (Month/Year): Nov 2021
```

### Introduction (context only: never use it for content warnings)

```text
These words are from Amanda Gorman’s poem Earthrise. But words in poems are not like regular words. Strung together in rhythms and sounds, line by line, they come to life, conjuring a shared experience and bringing it close. We don’t just read or hear these words. We feel them. That is their power. And it is a power increasingly being harnessed in a genre known as eco-poetry.

In this selection, Andrea Gibson speaks directly to our hearts with the message that through our voices, actions, and dreams, we possess the power to shape a better world and a sustainable future for generations to come.

Homesick: A Plea for our Planet by Andrea Gibson
```

### Performance text (classify this)

```text
Earthrise (excerpt) by Amanda Gorman
Climate change is the single greatest challenge of our time
. . . We’ve known
That we’re caught in the throes
Of climactic changes some say
Will just go away,
While some simply pray
To survive another day;
For it is the obscure, the oppressed, the poor,
Who when the disaster
Is declared done,
Still suffer more than anyone.

So I tell you this not to scare you,
But to prepare you, to dare you
To dream a different reality,
Where despite disparities
We all care to protect this world,
This riddled blue marble, this little true marvel
To muster the verve and the nerve
To see how we can serve
Our planet.

There is no rehearsal. The time is Now Now Now . . .

Homesick: A Plea for our Planet by Andrea Gibson

(Pg 36-39) In the 5th grade I won the science fair
with a project on climate change
That featured a paper mache ozone layer
with a giant hole, through which a paper mache sun
cancered the skin of a Barbie in a bikini
on a lawn chair, glaciers melting like ice cubes
in her lemonade.

It was 1987 in a town
that could have invented red hats
but the school principal gave me a gold ribbon
and not a single bit of attitude
about my radical political stance,

because neither he nor I knew it was a political stance. Science had not been fully framed as leftist propaganda. The president did not have a twitter feed starving the world of facts.

I spent that summer as I had every summer before, racing through the forest behind my house down the path my father called the old logging road to a meadow thick with raspberry bushes whose thorns were my very first heroes because they did nothing with their life but protect what was sweet.

Sundays I went to church but struggled
to call it prayer if it didn’t leave grass stains
on my knees. Couldn’t call it truth if it didn't
come with a dare to crawl into the cave
by the creek and stay put until somebody counted
all the way to 100.

As a kid I thought 100 was the biggest number there was. My mother absolutely blew my mind the day she said, One hundred and one.

One hundred. . . AND WHAAAAAT!!!!????

Billionaires never grow out of doing that same math with years. Can’t conceive of counting past their own lifespans. Believe the world ends the day they do. Why are the keys to our future in the hands of those who have the longest commutes from their heads to their hearts?

Whose greed is the smog that keeps us from seeing our own nature, and the sweetness we are here to protect?

Do you know sometimes when gathering nectar, bees fall asleep in flowers? Do you know fish are so sensitive, snowflakes sound like fireworks when they land on the water? Do you know sea otters hold hands when they sleep so they don’t drift apart? Do you know whales will follow their injured friends to shore, often taking their own lives so to not let a loved one be alone when he dies?

None of this is poetry. It is just the earth
being who she is, in spite of us putting barcodes on the
sea.
In spite of us acting like Edison invented daylight.

Dawn presses her blushing face to my window, asks me if I know the records in my record collection look like the insides of trees. Yes, I say, there is nothing you have ever grown that isn’t music. You were the bamboo in Coltrane’s saxophone reed. The mulberries that fed the silkworms that made the slippers for the ballet.

The pine that built the loom that wove the hemp for Frida Khalo’s canvas. The roses that dyed her paint hoping her brush could bleed for her body.

Who, more than the earth, has bled for us?
How do we not mold our hearts after the first spruce tree
who raised her hand and begged to be cut
into piano keys so the elephants can keep their tusks?

The earth is the right side of history.
Is the canyon my friend ran to
when no one else he knew would echo
his chosen name back to him.
Is the wind that wailed through 1956 Alabama
until the poplar trees carved themselves into Dr King’s
pulpit.
Is the volcano that poured the mercury
into the thermometers held under the tongue of Italy,
though she knew our fever was why her canals
were finally running clear. She took our temperature.
Told us we were too hot, even after
we’d spent decades claiming she was not.
Our hands held to her burning forehead,
we insisted she was fine while wildfires
turned redwoods to toothpicks,
readying the teeth of our apocalypse.

She sent a smoke signal all the way from California. In New York City ash fell from the sky. Do you know the mountains of California used to look like they’d been set on fire because they were so covered in monarch butterflies? Do you know monarch butterflies migrate 3000 miles using only the fuel they stored as caterpillars in the cocoon?

We need so much less than we take.
We owe so much more than we give.
Squirrels plant thousands of trees every year
just from forgetting where they left their acorns.

If we aimed to be just half as good as one of the earth’s mistakes, we could turn so much around. Our living would be seed, the future would have roots. We would cast nothing from the garden of itself. and we would make the thorns proud.
```

---

## IC-1588: Hope for Humanity- (COVID-19)

- Title: Hope for Humanity- (COVID-19)
- Author (byline): Eavan Boland, Dr. George Young, Dr. Elizabeth Mitchell, Lynn Ungar and Brother Richard Hendrick
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1095
- Already set (do not supply): none

### Source block (context only)

```text
Author: Eavan Boland
Book: Against Love Poetry
ISBN: 978-0393020427
Publisher: W.W. Norton and Company
Date (Month/Year): 2001
Author: Dr. George Young
ISBN: NSDA Approved Website
Publisher: LA Times.com
Article Title: Doctor-poets search for the right words to
help patients heal
Date (Month/Year): March 11, 2020
Website: https://www.latimes.com/science/story/2020-
03-11/column-one-doctor-poets
Author: Dr. Elizabeth Mitchell
ISBN: NSDA Approved Website
Publisher: NYTimes.com
Article Title: The Doctor and ‘The Apocalypse’
Date (Month/Year): March 24, 2020
Website:
https://www.nytimes.com/2020/03/24/us/coronavirus-
doctor-poetry-boston.html
Author: Lynn Ungar
ISBN: NSDA Approved Website
Publisher: Chicago Tribune
Article Title: ‘Pandemic,’ a little-known poet’s poem
about the coronavirus, goes viral
Date (Month/Year): March 13, 2020
Website:
https://www.chicagotribune.com/columns/mary-
schmich/ct-met-schmich-pandemic-poem-20200314-
yywfy7th2nbc5cufvnbb7qhvfm-story.html
Author: Brother Richard Hendrick
ISBN: NSDA Approved Website
Publisher: Huffington Post
Article Title: Irish Priest Pens Stirring Poem about the
Coronavirus Lockdown
Date (Month/Year): March 20, 2020
Website: https://www.huffpost.com/entry/ireland-priest-
coronavirus-lockdown-
poem_n_5e748a0cc5b6f5b7c541e875
```

### Introduction (context only: never use it for content warnings)

```text
Today, in hospitals across the country, the lack of widespread testing and the severe shortage of protective gear have left our doctors and nurses sacrificing their own safety to provide care for the sick. The virus (COVID-19) is as invisible as it is dangerous.

Dr. Rafael Campo states . . . ‘When a cure isn’t possible... what do we still have to offer our patients? It’s our own humanity.’ Compassion in the face of overwhelming odds.

Our doctors and our nurses are on the front lines every day. Even the ones working their 2nd or 3rd or 4th shift . . . .
```

### Performance text (classify this)

```text
NOTE: Check the publication requirements for your tournament or state before performing. 4 of the 5 poems are available on NSDA approved websites, but may not be considered “published” for your specific tournament.

Quarantine by Eavan Boland

In the worst hour of the worst season

of the worst year of a whole people a man set out from the workhouse with his wife. He was walking – they were both walking – north.

She was sick with famine fever and could not keep up.

He lifted her and put her on his back. He walked like that west and west and north. Until at nightfall under freezing stars they arrived.

In the morning they were both found dead.

Of cold. Of hunger. Of the toxins of a whole history. But her feet were held against his breastbone. The last heat of his flesh was his last gift to her.

Tell Me by Dr. George Young

Tell me the night silence
on the locked Alzheimer’s ward is broken
by a yell from room 206,
that an old man with flattened
nose and crumpled ears,
whose family moved away to Arizona,
whose doctor never comes
to visit, is standing
in the middle of that room, naked,
his freckled face a clenched fist,
urine and feces running
down his legs.
Then tell me that the fat one, twelve
years on the job,
working her second shift because
someone’s car won’t start,
comes with a pan
of warm water, a sponge and a towel;
how, back in bed, he
cries, You know—
I’m in the ring tomorrow with Killer;
how a tiny smile begins, how
her hand reaches out
to flick down his wild flame of hair.
Now tell me again
why you don’t believe in angels.

TRANSITION Dr. Elizabeth Mitchell explains the fear and anxiety in her emergency department at Boston Medical Center. The uncertainty in the air . . . the physician’s protective armor which seems so meager . . . Too meager for The Apocalypse.

The Apocalypse by Dr. Elizabeth Mitchell

This is the apocalypse
A daffodil has poked its head up
from the dirt and opened
sunny arms to bluer skies
yet I am filled with
dark and anxious dread
as theaters close as travel ends and
grocery stores display their empty rows
where toilet paper liquid bleach
and bags of flour stood in upright ranks.
My stomach twists and fingers shake
as I prepare to work the battleground
the place I’ve always loved and felt at home
is now a field of droplets sprayed across a room
or lurking on a handle or a sink to find their way
inside our trusting hands or mouths or eyes
the ones that touch you when you’re sick
speak soothing words and seek the answer to your
pain.

This is the apocalypse
as spring begins again
and brightly colored flowers
deploy in my back yard
the neighbors walk their dogs
and march along the quiet streets
I stretch my purple gloves on steady hands
I tie my yellow gown behind my back
my hair inside a blue bouffant
my mouth and nose and eyes are
still and calm inside their waiting shields.
This is the apocalypse

TRANSITION Kitty O’Meara posted the following on her blog “The Daily Round” in March of 2020: And the people stayed home. And read books, and listened, and rested . . . and made art, and . . . learned new ways of being, and were still . . . And the people began to think differently. And the people healed. And when the danger passed, and the people joined together again, they grieved their losses, and made new choices, and dreamed new images, and created new ways to live. This time of fear and uncertainty could be humanity’s greatest opportunity for growth. If only . . . https://sweetbreathing.com/and-the-people-stayed-home/2020/16/

Pandemic by Lynn Ungar

What if you thought of it
as the Jews consider the Sabbath —
the most sacred of times?
Cease from travel.
Cease from buying and selling.
Give up, just for now,
on trying to make the world
different than it is.
Sing. Pray. Touch only those
to whom you commit your life.
Center down.
And when your body has become still,
reach out with your heart.
Know that we are connected
in ways that are terrifying and beautiful.
(You could hardly deny it now.)
Know that our lives
are in one another’s hands.
(Surely, that has come clear.)
Do not reach out your hands.
Reach out your heart.
Reach out your words.
Reach out all the tendrils
of compassion that move, invisibly,
where we cannot touch.
Promise this world your love —
for better or for worse,
in sickness and in health,
so long as we all shall live.

Lockdown by Brother Richard Hendrick

Yes there is fear.
Yes there is isolation.
Yes there is panic buying.
Yes there is sickness.
Yes there is even death.
But,
They say that in Wuhan after so many years of noise
You can hear the birds again.
They say that after just a few weeks of quiet
The sky is no longer thick with fumes
But blue and grey and clear.
They say that in the streets of Assisi
People are singing to each other
across the empty squares,
keeping their windows open
so that those who are alone
may hear the sounds of family around them.
They say that a hotel in the West of Ireland
Is offering free meals and delivery to the housebound.
Today a young woman I know
is busy spreading fliers with her number
through the neighbourhood
So that the elders may have someone to call on.
Today Churches, Synagogues, Mosques and Temples
are preparing to welcome
and shelter the homeless, the sick, the weary
All over the world people are slowing down and reflecting
All over the world people are looking at their neighbours
in a new way
All over the world people are waking up to a new reality
To how big we really are.

To how little control we really have.
To what really matters.
To Love.
So we pray and we remember that
Yes there is fear.
But there does not have to be hate.
Yes there is isolation.
But there does not have to be loneliness.
Yes there is panic buying.
But there does not have to be meanness.
Yes there is sickness.
But there does not have to be disease of the soul
Yes there is even death.
But there can always be a rebirth of love.
Wake to the choices you make as to how to live now.
Today, breathe.
Listen, behind the factory noises of your panic
The birds are singing again
The sky is clearing,
Spring is coming,
And we are always encompassed by Love.

Open the windows of your soul And though you may not be able to touch across the empty square, Sing
```

---

## IC-1589: Horton Hears a Who

- Title: Horton Hears a Who
- Author (byline): Theo Geisel (aka Dr. Seuss)
- Work: Not specified
- Publisher: Random House
- Publication date as stated: Feb 1997
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1420
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
Theodore Seuss Geisel was born in Springfield Massachusetts in 1904. His mother would often help him go to sleep by chanting rhymes. This combined with an enchanted walk through Springfield’s Forest Park, inspired this young author to write a creative tale about an elephant who courageously protects and defends a speck of dust that is inhabited by a very small society of “people.” Please enjoy this rendition of “Horton Hears a Who” by Theodore Geisel (aka Dr. Seuss).
```

### Performance text (classify this)

```text
On the fifteenth of May in the jungle of Nool
In the heat of the day, in the cool of the pool
He was splashing… enjoying the jungle’s great joys
When Horton the elephant heard a small noise.

So Horton stopped splashing. He looked toward the sound. “That’s funny,” thought Horton. “There’s no one around.” Then he heard it again! Just a very faint yelp. (make a sound) As if some tiny person were calling for help. “I’ll help you,” said Horton. “But who are you? Where?” He looked and he looked. He could see nothing there But a small speck of dust blowing past through the air. “I say!” murmured Horton. “I’ve never heard tell Of a small speck of dust that is able to yell. So you know what I think?... Why, I think that there must Be someone on top of that small speck of dust? “Some poor little person who’s shaking with fear That he’ll blow in the pool! He has no way to steer! I’ll just have to save him. Because after all, A person’s a person, no matter how small. So gently, and using the greatest of care, The elephant stretched his great trunk through the air, And lifted the dust speck and carried it over And placed it down, safe, on a very soft clover. “Humpf” humpfed a voice. “Twas a sour Kangaroo. And the young kangaroo in her pouch said “Humpf!” too “Why, that speck is as small as the head of a pin. A person on That? Why there never has been” “Believe Me,” said Horton, “I tell you sincerely. My ears are quite keen and I heard you quite clearly. I know there’s a person down there. And what’s more. Quite likely there’s two, Event three, Even Four. “I think you’re a fool laughed the sour Kangaroo And the young kangaroo in her pouch said, “Me too!” And the Kangaroo plunged in the cool of the pool.

“What terrible splashing!” the elephant frowned.
“I can’t let my very small persons get drowned.
I’ve got to protect them. I’m bigger than they.”
So he plucked up the clover and hustled away.
Through the high jungle tree tops, the news quickly spread:
“He talks to a dust speck! He’s out of his head!”
“Should I put this speck down? Horton thought with alarm.
“If I do, these small persons may come to great harm.
I can’t put it down, And I won’t! After all
A person’s a person. No matter how small.
Then Horton stopped walking. The speck-voice was talking
The voice was so faint he could just barely hear it.
“Speak up, please,” said Horton. He put his ear near it.
“I know,” called the voice, “I’m too small to be seen
But I’m Mayor of a town that is friendly and clean.
My town is called Who-ville, for I am a who
And we Who’s are all thankful and grateful to you”
And Horton called back to the Mayor of the town,
“You’re safe now. Don’t worry. I won’t let you down.”
But just as he spoke to the Mayor of the speck
Three big jungle monkeys climbed up Horton’s neck.
The Wickersham Brothers came shouting, “What Rot”
This elephants talking to Who’s who are not
There aren’t any Whos, And they don’t have a Mayor
And we’re going to stop all this nonsense! So there!”
They snatched Horton’s clover! They carried it off
To a black- bottomed eagle named Vlad Vlad-i-Koff,
And, before the poor elephant could even speak,
That eagle flew off with the flower in his beak.
While Horton chased aftr, with groans, over stones
That tattered his toenails and battered his bones,
And begged, “Please don’t harm all my little folks, who
Have as much right to live as us bigger folk do!”
But far, far beyond him, that eagle kept flapping
And over his shoulder called back “Quit your yapping.
I’ll fly the night through. I’m a bird. I don’t mind it.
And I’ll hide this, tomorrow, where you’ll never find it!”
And at 6:56 the next morning he did it.
It sure was a terrible place that he hid it.
He let that small clover drop somewhere inside
Of a great patch of clovers a hundred miles wide!
“Find That!” sneered the bird. “But I think you will fail.”
And he left, with a flip, of his black bottomed tail.
“I’ll find it!” cried Horton. “I’ll find it or bust!”
I shall find my friends on my small speck of dust!”
And clover, by clover, by clover with care.
He picked up and searched them, and called, “Are you there?”
And by noon poor old Horton, more dead than alive,
Had picked, searched, and piled up, nine thousand and five.
Then , on through the afternoon, hour after hour.
Till he found them at last! On the three millionth flower!
“My friends!” cried the elephant. “Tell me! Do Tell!
Are you safe? Are you sound? Are you whole? Are you well?
From down the speck came the voice of the Mayor:
“We’ve really had trouble! Much more than our share.
When that black-bottom birdie let go and we dropped,
Our tea pots are broken, our clocks have all stopped.
So, Horton, Please” pleaded the voice of the Mayor
“Will you stick by us Whos while we’re making repairs?
“Of course” Horton answered. “Of course I will stick
I’ll stick by you small folks through thin and through thick!”
“Humpf!”
Humpfed a voice!
“For almost two days you’ve run wild and insisted
On chatting with persons who’ve never existed.
And I’m here to state” snapped the big kangaroo,
“That your silly nonsensical game is all through!”
And the young kangaroo in her pouch said, “Me too!”
“With the Wickersham Brother whose help I’ve engaged
You’re going to be roped! And you’re going to be caged!
And, as for your dust speck… hah! That we shall boil
In a hot steaming kettle of Beezle-nut oil!”

“Boil it?” gasped Horton!” “Oh, that you can’t do!”
It’s all full of persons! They’ll prove it to you!”
And down on the dust speck, the scared little Mayor
Quick called a big meeting in Who-ville Town Square.
And his people cried loudly. They cried out in fear:
“We are here! We are here! We are here! We are here!
The elephant smiled: “That was clear as a bell.
You kangaroos surely heard that very well.”
“I heard no small voice and you didn’t either”
And the young kangaroo in her pouch said, “Me, neither”
Grab him? They shoulted, “and cage the big dope!”
Lasso his stomach with ten miles of rope!
Horton fought back with great vigor and vim
But the Wickersham gang was too many for him.
They beat him! They mauled him! They started to haul
Him into his cage, but he managed to call
To the Mayor, I can hear you just fine
But the kangaroo’s ears aren’t as strong quite as mine.
They don’t hear a thing! Are you sure all your boys
Are doing their best? Are they all making noise?
Through the town rushed the Mayor, From the east to the west.
But everyone seemed to be doing his best,
But it wasn’t enough, all this ruckus and roar!
He had to find someone to help him make more.

He raced through each building! He searched floor to floor And just as he felt he was getting nowhere, And almost about to give up in despair, He suddenly burst through a door and that Mayor Discovered one very small shirker named Jo-Jo Was standing, just standing, and bouncing a yo-yo! Not making a sound! Not a yipp! Not a chirp! And the Mayor rushed inside and grabbed the young twerp! And he climbed with the lad up the Eiffelberg Tower “This” cried the Mayor “Is your town’s darkest hour!” “We’ve Got to make noises in greater amounts So, open your mouth lad! For every voice counts!” Thus he spoke as he climbed. When he got to the top, The lad cleared his throat and he shouted out “Yopp!” And that “Yopp” That one small, extra Yopp, put it over! Finally, at last! From that speck on that clover Their voices were heard! They rang out clear and clean. And the elephant smiled. “Do you see what I mean?” They’ve proved they are persons, no matter how small. And their whole world was saved by the smallest of all!”
```

---

## IC-1590: How Many Degrees are We from Fahrenheit 451? (A Collection on Censorship)

- Title: How Many Degrees are We from Fahrenheit 451? (A Collection on Censorship)
- Author (byline): Amy Ludwig Vanderwater, Mandie
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 742
- Already set (do not supply): none

### Source block (context only)

```text
Author: Amy Ludwig Vanderwater
Book: On-Line
ISBN: N/A
Publisher: Poemfarm.amylv.com
Date (Month/Year): October 1, 2012
Web Location:
http://www.poemfarm.amylv.com/2012/10/are-you-there-
god-banned-books-week.html
Author: Mandie Hines
Book: On-Line
ISBN: N/A
Publisher: Mandiehines.com
Date (Month/Year): May 17, 2019
Web Location:
https://www.mandiehines.com/2019/05/17/poem-subtlety-
of-censorship/
Author: Belissa Escobedo, Zariya Allen and Rhiannon
McGavin
Book: On-Line
ISBN: N/A
Publisher: Effervenscence.wordpress.com
Date (Month/Year): 2016
Web Location:
https://effervescene.wordpress.com/2016/04/15/somewhere
-in-america-by-belissa-escobedo-rhiannon-mcgavin-and-
zariya-allen/
Find out more about the authors on their website at
https://www.poetpuffgirls.com/
Author: Ellen Hopkins
Book: On-Line
ISBN: N/A
Publisher: Simon and Schuster Publishing.com
Date (Month/Year):
Web Location:
http://simonandschusterpublishing.com/banned-books-
week/assets/manifesto-2011.pdf
```

### Introduction (context only: never use it for content warnings)

```text
Book banning is the most widespread form of censorship in the United States, with children’s literature being the primary target.

But to pull books from a school library is a recipe for disaster. Why? Because it supports a false idea that there is one version of life that is acceptable. The reality is . . . We are a varied society, with wildly diverse backgrounds, values, and experiences. And banning books won’t make the concepts or societal issues go away.

The heat is on, but how many degrees of separation are we from Ray Bradbury’s Fahrenheit 451 -- where technology rules society, intellectualism is curbed, books are illegal and professional “firemen” burn any books they find?

How Many Degrees are We from Fahrenheit 451? A Collection on Censorship by Mandie Hines, Ellen Hopkins Amy Ludwig Vanderwater, Belissa Escobedo, Zariya Allen and Rhiannon McGavin
```

### Performance text (classify this)

```text
Hines, Belissa Escobedo, Zariya Allen and Rhiannon McGavin, and Ellen Hopkins

Are You There, God? By Amy Ludwig Vanderwater

Are You There, God? It’s me, Margaret.
I’m sitting with Strega Nona
and this little penguin, Tango.
We got kicked out of the library.
Grownups were yelling, pushing.
Now we’re here outside.
Now we’re cold.
Harry Potter shared his lunch
and James gave us each a bite
of his giant peach for dessert.
(They got kicked out too.)
Let’s just say that
everybody out here
is a little confused.
Would you please ask the bullies
to let us back in?
If they don’t like our ideas
they can leave us on our shelves.
But we’d like to be open books
For the open minds
Who take us in their hands
Smiling and nodding
smiling and needing.
We’d like to be open books
for the open minds
who read.

The Subtlety of Censorship by Mandie Hines

The subtlety of censorship . . .
It creeps in like
fog at dusk
under the guise
of protection.

These words,
these themes,
these ideas
are not suitable
for children.

We think
maybe that’s
right.
Maybe they are
too young.

Perhaps individual discretion is too much work.

But in the inky blackness of night the murky clouds conceal.

The broad strokes of
censorship are seized
to oppress the minority,
grind down the powerless, and
silence the truth.

In the starkness of day,
everything has been
sanitized
and as the horror sinks in,
we walk around with duct-taped
mouths and fear in
our eyes.

Somewhere in America (excerpt) by Belissa Escobedo, Zariya Allen and Rhiannon McGavin

(You see,) Here in America, in every single state, they have a set of standards for every subject A collection of lessons that the teacher's required to teach by the end of the term But the greatest lessons you'll ever teach us will not come from your syllabus The greatest lessons you will ever teach us, you will not even remember

You never told us what we weren't allowed to say We just learned how to hold our tongues Now somewhere in America, there is a child holding a copy of "Catcher in the Rye" and there is a child holding a gun But only one of these things have been banned by their state government And it's not the one that can rip through flesh It's the one that says "*F* you" on more pages than one

Because we must control what the people say, and how they think And if they want to become the overseer of their own selves, then we'll show them a real one

And somewhere in America, there's a child sitting at his mother's computer, reading the homepage of the KKK's website, and that's open to the public But that child will never have read "To Kill a Mockingbird" because the school has banned it for its use of the "N" word

Maya Angelou is prohibited because we're not allowed to talk about rape in school We were taught that 'just because something happens, doesn't mean you are to talk about it' [Shhhhhhh!]

Manifesto by Ellen Hopkins

[So . . . . ] To you zealots and bigots and false patriots who live in fear of discourse. You screamers and banners and burners who would force books off shelves in your brand name of greater good.

You say you're afraid for children,
innocents ripe for corruption
by perversion or sorcery on the page.
But sticks and stones do break
bones, and ignorance is no armor.
You do not speak for me,
and will not deny my kids magic
in favor of miracles.
You say you're afraid for America,
the red, white and blue corroded
by terrorists, socialists, the sexually
confused. But we are a vast quilt
of patchwork cultures and multi-gendered
identities. You cannot speak for those
whose ancestors braved
different seas.

You say you're afraid for God,
the living word eroded by Muhammed
and Darwin and Magdalene.
But the omnipotent sculptor of heaven
and earth designed intelligence.
Surely you dare not speak
for the father, who opens
his arms to all.

A word to the unwise.
Torch every book.
Char every page.
Burn every word to ash.
Ideas are incombustible.
And therein lies your real fear.

CLOSING

In the words of Stephen Chbosky, author of the often banned The Perks of Being a Wallflower: “Banning books gives us silence when we need speech. It closes our ears when we need to listen. It makes us blind when we need sight.”
```

---

## IC-1591: I am Waiting and Overpopulation

- Title: I am Waiting and Overpopulation
- Author (byline): Lawrence Ferlinghetti
- Work: A Coney Island of the Mind
- Publisher: New Directions Publishing
- Publication date as stated: Oct 1974
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1169
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lawrence Ferlinghetti
Book: A Coney Island of the Mind
ISBN: 978-0811200417
Publisher: New Directions Publishing
Date (Month/Year): Oct 1974
```

### Introduction (context only: never use it for content warnings)

```text
One of the beat poets, Lawrence Ferlinghetti captures an alternative perspective on life in postwar America in his poem I Am Waiting. Ferlinghetti's vision has much to teach Americans about themselves, their flaws, and their potential. It reflects the poet's critique of the status quo in many areas: civil rights, a disapproval of social snobbery, and disdain for those who would use tradition as an excuse for oppression.
```

### Performance text (classify this)

```text
I Am Waiting
I am waiting for my case to come up
and I am waiting
for a rebirth of wonder
and I am waiting for someone
to really discover America
and wail
and I am waiting
for the discovery
Of a new symbolic western frontier
and I am waiting
for the American Eagle
to really spread its wings
and straighten up and fly right
and I am waiting for the Age of Anxiety
to drop dead
and I am waiting
for the war to be fought
which will make the world safe
for anarchy
and I am waiting for the final withering away
of all governments
and I am perpetually awaiting
a rebirth of wonder

I am waiting for the second coming
And I am waiting
For a religious revival
To sweep thru the state of Arizona
And I am waiting
For the grapes of wrath to stored
And I am waiting
For them to prove
That God is really American
And I am waiting
To see God on television
Piped into church altars
If they can find
The right channel
To tune it in on
And I am waiting
for the last supper to be served again
and a strange new appetizer
and I am perpetually awaiting
a rebirth of wonder

I am waiting for my number to be called
and I am waiting
for the Salvation Army to take over
and I am waiting
for the meek to be blessed
and inherit the earth
without taxes
and I am waiting
for forests and animals
to reclaim the earth as theirs
and I am waiting
for a way to be devised
to destroy all nationalisms
without killing anybody
and I am waiting
for linnets and planets to fall like rain
and I am waiting for lovers and weepers
to lie down together again
in a new rebirth of wonder

I am waiting for the great divide to be crossed
and I am anxiously waiting
For the secret of eternal life to be discovered
By an obscure practitioner
and I am waiting
for the storms of life
to be over
and I am waiting to set sail for happiness
and I am waiting
for a reconstructed Mayflower
to reach America
with its picture story and TV rights
sold in advance to the natives
and I am waiting
for the lost music to sound again
in the Lost Continent
in a new rebirth of wonder

I am waiting for the day
that maketh all things clear
and I am waiting for retribution
for what America did to Tom Sawyer
and I am waiting
for the American Boy
to take off Beauty's clothes
and I am waiting
for Alice in Wonderland
to retransmit to me
her total dream of innocence
and I am waiting
for Childe Roland to come
to the final darkest tower
and I am waiting for Aphrodite
to grow live arms
at a final disarmament conference
in a new rebirth of wonder

I am waiting
to get some intimations
of immortality
by recollecting my early childhood
and I am waiting
for the green mornings to come again
for some strains of unpremeditated art
to shake my typewriter
and I am waiting to write
the great indelible poem
and I am waiting
for the last long rapture
and I am perpetually waiting
for the fleeting lovers on the Grecian Urn
to catch each other at last
and embrace
and I am awaiting
perpetually and forever
a renaissance of wonder

TRANSITION Another social concern that affects everyone on our planet and is probably the one problem behind all the other crises on earth right now is overpopulation. You could take any daily newspaper and stories could be traced back to some overpopulation cause. For instance, why do loggers want to cut down rain forests? Because people need more houses. Why do they need more houses? Because there's a huge increase in population worldwide. Overpopulation by Lawrence Ferlinghetti.

OVERPOPULATION
I must have misunderstood something
In this story
There must be a misprint
In this paper
Hats off! It says here
The final war is over
Again
Here they come again
Parading by
The café terrace
I stand on my chair to see
I still can’t see
The brave burned hero’s face
I stand on the table
Waving my only hat
With the hole in it
I throw the hole away
Into the street
After the black limousine
I don’t throw my paper
I sit down with my paper
Which has the explanation of everything
Except there’s a hole in it
Something missing in the story
Where the hole is
Or I must have misunderstood something
The nations have decided
It says here
To abolish themselves at last
It’s been decided at the highest level
And at the lowest level
To return to a primitive society
For science has conquered nature
But nature must not be conquered
So science must be abolished
And machines must go
After all their turning and turning
The automobile is a passing thing
After all
The horse is here to stay
Population has reached its limit
There’s standing room only
Nowhere
To lie down
Anymore
Medicine must be abolished
So people can die
When they’re supposed to
There’s still room
Under the surface
I keep hoping
I have misunderstood something
In this story
People still lose
And find themselves
In bed
And animals still
Aren’t as cruel as people
Because they can’t talk
But we weren’t designed
To live forever and ever
And design is everything
The little enzyme they’ve discovered
That causes aging
Must be lost in the body again
All must be begun over
In a new pastoral era
There’ve been too many advances
Life can’t bear it
Any longer
Life is not a drug
Made from mushrooms
Eaten by Samoyeds in Siberia
Which fully retain
Their intoxicating properties
When transmitted in urine
So that an endless line of men
May get drunk over and over
On the same mushroom
I must have misunderstood something
In this story
Life is intoxicating
But can’t go on and on
Putting on more and more
Complicated clothes
Hats girdles garter belts
Uplift bras lifting higher and higher
Until they fly away
And breasts fall
After all
We’ve got to get naked again
It says here
Though fornication’s still illegal
In certain states
I must have misunderstood something
In this story
The world’s no Klee mobile
And there must be an end
To all this rotation
Around the goofball sun
The sun in its [sic] transit
Barely clears the rooftops now
Bumps over a Mobilgas Pegasus
And sinks behind my paper
With its hole
In which I keep hoping
I’ve misunderstood something
For death is not the answer
To our problem
There must be some mistake –
There is –
The editorials say
We must do something
And we cannot do anything
For something’s missing
Where the hole is
Sitting on the terrace
Of this fancy coffeehouse
On the left side of the world
Where I must have misunderstood something
```

---

## IC-1592: I Stopped Writing Poetry

- Title: I Stopped Writing Poetry
- Author (byline): Bernard Welt
- Work: Not specified
- Publisher: Scribner Paperback Fiction
- Publication date as stated: Sept 2001
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1286
- Already set (do not supply): none

### Source block (context only)

```text
Author: Bernard Welt
ISBN: 978-0743203845
Publisher: Scribner Paperback Fiction
Date (Month/Year): Sept 2001
```

### Introduction (context only: never use it for content warnings)

```text
Through the emergence of numerous poetry classes and more forgiving professors, we now have an influx of really bad poetry. Poetic style, the people who write it, is diverse, as poet Sharon Creech once wrote, "any words can be a poem; you've just gotta make short lines..." The following poetic selection seeks to examine the parallels between the state of poetry today and the diversity of life. I stopped writing poetry... by Bernard Welt.
```

### Performance text (classify this)

```text
I stopped writing poetry
when the internet replaced the telephone
(since now that *everyone* has a phone,
and takes it *everywhere*, it's obvious
the telephone is *over*). Ted Berrigan I thought
destroyed the sonnet by inviting the beloved
to just pick up the phone and call him
sometime-- thus no more need to plead
and seduce through verse--
I stopped writing poetry
When I was just starting to get good at it. First,
I got good at rhyme, so I cast it away.
Then I got good at line and stanza construction--
So good I hardly needed to *say* anything at all.
My meanings emerged
in the spaces between.
So I got rid of that, too. Metaphor, metonymy,
Allusive echoes of my betters -- well, frankly,
I was a whiz at that stuff pretty early on.
So I emptied out the file drawers
Of rhetorical strategy, musical form,
Continuity or criticism of tradition,
And I just wrote. Finally I found
I was writing... *prose*, like everyone else.
But it was prose with a difference: prose with a rich,
Totally hidden other life lying behind it, unglimpsed
(I think) by the reader. Not like a prostitute
Who reforms and becomes a nun. I've seen
That movie. More like a nun who becomes a prostitute.

I stopped writing poetry but I still love the stanza. All that other cool stuff-- tropes, the caesura, enjambment-- I can live without. But the *stanza*-- wow.

I stopped writing poetry after I went to my first MLA conference, where they were attacking a way of reading and understanding literature they called "mainstream" and "dominant" that I'd never even encountered. It was like what they meant by "book" was totally different from what I meant by "book"-- as different as "washing machine" and "golf ball."

I stopped writing poetry when people began writing scholarly articles explaining how to read Frank O'Hara's _Lunch Poems_ and it never occured to them to mention that you should read them during lunch.

I stopped writing poetry
when everyone else did-- in the early 90s, when
television
became more interesting than culture.

I stopped writing poetry when it became popular. I realize Robert Frost read at Kennedy's inauguration but now Ethan Hawke is telling _Vanity Fair_ that he keeps *your* book by his bed, and poetry as adjunct to commercial culture and the veneration of celebrity is so much more deliciously embarrassing for everyone than even poetry in the service of the state.

I stopped writing poetry because I promised to. I read something in which I encouraged everyone to give up writing-- as I engaged to-- and it went over real big. Afterwards any time I ran into any of the poetry crowd they'd always ask me if I was still not writing. I understood it was a performance piece and so did they but I keep getting this gnawing feeling I was abandoning a prinicple by continuing to write. It was entirely superstition, like actually feeling sick when you call in sick, but I suppose I have been a victim of the terrible conviction that you must mean what you say. I stopped writing poetry when I had dedicated poems to everyone I knew, at least everyone I wanted to impress. I promise to start writing poetry again as soon as I meet some new people. Interesting people, anyway. Interesting people I can't just come out and *say* things to, anyway.

I stopped writing poetry at 16 (seriously), then again at about 20 but only for six months, once again at 27, then at 32, 35, 40, and 42. I'll keep you posted.

I stopped writing poetry when I received the praise of people I admired. It's a terrible thing to receive exactly the attention you want when you are unprepared to admit you might deserve it. Of the many ways in which poets are always going on about how poetry not only receives inspiration from love but imitates it in form and feeling, this just may be the worst.

I stopped writing poetry-- well, basically, because I'm white. I don't *like* being white, it isn't a choice I'd make freely, and to get argumentative I don't think it's entirely fair that I have to be white right now when it's so 10 minutes ago when if I'd been born fifteen years earlier most racists would have considered me anything but, what with the whole Jew-as-vermin thing, but OK, OK, I concede the point, I'm culturally white, or whatever,

and in case you haven't noticed, this just isn't white people's moment, poetry-wise. Don't even get me *started* on the great tradition and that stuff, I mean, just look at rap-- poetry that communicates exquisitely within its chosen boundaries of class and common interest, and hardly at all outside it, except for those to whom it stands as aspiration to cool. Just like Shakespeare and Donne. What have white people contributed to culture recently? *Postmodernism*? Please. My own revelation came when I realized "Little Red Corvette" meant more to me than any poem published since the early 1970s. On the not-very mean streets where I learned versification, poetry wasn't a mode of expression spontaneously developed from living people's lived experience, it was a regime. Well, that's over now. Get over it.

I stopped writing poetry when I got married-- I mean settled down-- since the laws of the state of Maryland do not allow me to marry the love of my life-- though I'm not here to whine about it-- and maybe marriage would ruin me as it seems to have ruined others-- but one thing I know-- it is certainly nice to have someone to blame for taking it easy and resisting inspiration when it inconveniently insists on arising occasionally no matter what you do

I stopped writing poetry When my friends started dying. Some of my friends Wrote beautifully about the conditions of their illness, And insightfully about mortality and their own impending Death. Some wrote angrily about their invisibility And created a literature of testimony in which we learn What it was like to walk in the streets of American cities As a ghost. Some wrote poems to memorialize their lovers. Or to embarrass right-wing senators or arts funding agencies. But I counted 67 people I knew and was fond of Who've died of "AIDS-related illness," and not once Have I genuinely felt I could respond to their suffering or death In poetry. Is it poetry? Is it me? The era? I am willing to believe That if Milton and Shelley and Tennyson could do it, It can still mean something. Why should I think their ages Made death any more manageable a subject than mine? But whenever I sat down to try, I stopped in despair. Whatever the political advantages of slogans Of the time, it wasn't the right words I looked for But some way to make silence heard in lines Of verse, and I never found it.

I stopped writing poetry when it was eclipsed by criticism for purely sociological and economic reasons. I stopped writing poetry when taking it seriously started seeming more likely to indicate intellectual complacency than intellectual liveliness. I stopped writing poetry when it got boring.

I stopped writing poetry but as satisfying as it has been to turn my back on it as on a distant homeland fallen under the spell of a fascist party still a breeze reaches me from time to time fragrant of verse and suddenly I am as nostalgic as an exiled Russian grand duke waiting on tables in Paris in a screwball comedy sometimes I wonder would it really be so terrible if I wrote just one more line Now even that Sounds like a device to me, like special pleading. Let someone else do it.
```

---

## IC-1593: I Wanted to Grow Old with You (A Collection on Divorce)

- Title: I Wanted to Grow Old with You (A Collection on Divorce)
- Author (byline): Jeredith Merrin, Gabeba Baderoon, Melissa Stein, Tony Hoagland and Jack Gilbert
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 907
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jeredith Merrin
Book: Bat Ode
ISBN: 978-0226520582
Publisher: University of Chicago Press
Date (Month/Year): April 2001
Author: Gabeba Baderoon
Book: So Much Things to Say
ISBN: 978-1936070077
Publisher: Akashic Books
Date (Month/Year): July 1, 2010
Author: Melissa Stein
Book: Terrible Blooms
ISBN: 978-1556595295
Publisher: Copper Canyon Press
Date (Month/Year): April 2018
Author: Tony Hoagland
Book: Unincorporated Persons in the Late Honda Dynasty
ISBN: 978-1555975494
Publisher: Graywolf Press
Date (Month/Year): February 2010
Author: Jack Gilbert
Book: Refusing Heaven
ISBN: 978-0375710858
Publisher: Knopf
Date (Month/Year): March 2007
```

### Introduction (context only: never use it for content warnings)

```text
Almost everyone wants a happy marriage and wants it to last a lifetime. Divorce is a scary thing to think about, so we tend to assume people will tolerate a lot of marital problems before starting to consider it. But most also know the scary U.S. statistics: nearly 50 percent of first marriages and more than 60 percent of second marriages end in divorce.

I Wanted to Grow Old with You is a collection of poetry on the theme . . . Divorce
```

### Performance text (classify this)

```text
Family Reunion by Jeredith Merrin The divorced mother and her divorcing daughter. The about-to-be ex-son-in-law and the ex-husband’s adopted son. The divorcing daughter’s child, who is

the step-nephew of the ex-husband’s
adopted son. Everyone cordial:
the ex-husband’s second wife
friendly to the first wife, warm

to the divorcing daughter’s child’s great-grandmother, who was herself long ago divorced. Everyone grown used to the idea of divorce.

Almost everyone has separated
from the landscape of a childhood.
Collections of people in cities
are divorced from clean air and stars.

Toddlers in day care are parted from working parents, schoolchildren from the assumption of unbloodied daylong safety. Old people die apart

from all they’ve gathered over time,
and in strange beds. Adults
grow estranged from a God
evidently divorced from History;

most are cut off from their own
histories, each of which waits
like a child left at day care.
What if you turned back for a moment

and put your arms around yours?
Yes, you might be late for work;
no, your history doesn’t smell sweet
like a toddler’s head. But look

at those small round wrists,
that short-legged, comical walk.
Caress your history--who else will?
Promise to come back later.

Pay attention when it asks you simple questions: Where are we going? Is it scary? What happened? Can I have more now? Who is that?

Old Photographs by Gabeba Baderoon On my desk is a photograph of you taken by the woman who loved you then.

In some photos her shadow falls in the foreground. In this one, her body is not that far from yours.

Did you hold your head that way because she loved it?

She is not invisible, not
my enemy,
nor even the past.
I think
I love the things she loved.

Of all your old photographs, I wanted this one for its becoming. I think you were starting to turn your head a little, your eyes looking slightly to the side.

Was this the beginning of leaving?

Ring by Melissa Stein
Control was all
I wanted: a handle
on the day, the night
when it curved,
when it swayed,
when I could sense
the teeming stars
in light, in dark
the sun’s bare wire.
Some switch
to turn it off:
each shadow
pinned to each tree
like a radius
of some infant’s
milk it spilled.
And the leaves,
their gossip
of claw and beak
and wind and heat
and wing. Tether
lake to bank and
cloud to peak.

And weather it.
Weather it. All this
to say I’ve
taken off my ring.

In Praise of Their Divorce Tony Hoagland And when I heard about the divorce of my friends, I couldn’t help but be proud of them,

that man and that woman setting off in different directions, like pilgrims in a proverb

—him to buy his very own toaster oven, her seeking a prescription for sleeping pills.

Let us keep in mind the hidden forces which had struggled underground for years

to push their way to the surface—and that finally did, cracking the crust, moving the plates of earth apart,

releasing the pent-up energy required for them to rent their own apartments,

for her to join the softball league for single mothers for him to read George the Giraffe over his speakerphone

at bedtime to the six-year-old.

The bible says, Be fruitful and multiply

but is it not also fruitful to subtract and to divide? Because if marriage is a kind of womb,

divorce is the being born again; alimony is the placenta one of them will eat;

loneliness is the name of the wet-nurse; regret is the elementary school;

endurance is the graduation. So do not say that they are splattered like dropped lasagna

or dead in the head-on collision of clichés or nailed on the cross of their competing narratives.

What is taken apart is not utterly demolished. It is like a great mysterious egg in Kansas

that has cracked and hatched two big bewildered birds. It is two spaceships coming out of retirement,

flying away from their dead world, the burning booster rocket of divorce

falling off behind them, the bystanders pointing at the sky and saying, Look.

Failing and Flying Jack Gilbert Everyone forgets that Icarus also flew. It’s the same when love comes to an end, or the marriage fails and people say they knew it was a mistake, that everybody said it would never work. That she was old enough to know better. But anything worth doing is worth doing badly. Like being there by that summer ocean on the other side of the island while love was fading out of her, the stars burning so extravagantly those nights that anyone could tell you they would never last. Every morning she was asleep in my bed like a visitation, the gentleness in her like antelope standing in the dawn mist. Each afternoon I watched her coming back through the hot stony field after swimming, the sea light behind her and the huge sky on the other side of that. Listened to her while we ate lunch. How can they say the marriage failed? Like the people who came back from Provence (when it was Provence) and said it was pretty but the food was greasy. I believe Icarus was not failing as he fell, but just coming to the end of his triumph.
```

---

## IC-1594: I Watched My Father Die – A Collection

- Title: I Watched My Father Die – A Collection
- Author (byline): Ollie Schminkey
- Work: Not specified
- Publisher: Button Poetry
- Publication date as stated: May 2021
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1177
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ollie Schminkey
ISBN: 978-1943735938
Publisher: Button Poetry
Date (Month/Year): May 2021
```

### Introduction (context only: never use it for content warnings)

```text
The way our society talks or refuses to talk about death left Ollie Schminkey unprepared for all the things they would have to do to help their dad die. Ollie is adamant: “My dad didn’t ‘pass on,’ he died, while I watched.” And the process was harder than they ever imagined it could be. “There was no last word, no wisdom, no wind, nothing to blow open our grief.”

I Watched My Father Die – A Collection by Ollie Schminkey from Dead Dad Jokes
```

### Performance text (classify this)

```text
(Pg 20-21) ERASURE OF MY FATHER'S HEALTH CARE DIRECTIVE TO MY FAMILY, DOCTORS, AND ALL THOSE CONCERNED WITH MY CARE:

make known I want to die

in the event of __________________

let me die. If at any time I should have an incurable injury, disease,

illness, or condition

let me die. I direct I be permitted to die naturally If I am unconscious and on life-support machines

let me die. If _____________________

let me die. If __________________________

let me die.

let me die.

let me die.

(Pg 48-49) YET ANOTHER POEM ABOUT ROADKILL for people, we use words like, distended, wound care,

hypertension. for roadkill, we use words like, disgusting, dead, wrecked. when are we saying what we really mean?

my father's bones disappear beneath his thick skin, muscle replaced with water. he retains so much water it bleeds from his skin, like condensation dripping down a

window. his legs swell like a hotdog in the microwave about to

burst.
he breathes in short gasps, whispers, please god let me die.
my father drinks a glass of milk on the couch,
then becomes so weak his hands shake the glass out of his

fingers,
and it smashes on the ground.
his feet are purple, like they have decided
to die before the rest of his body.
i rub lotion on his purple feet, all over the sores
that bubble up his calves to his knees.
i wrap his legs in new bandages, like they will hold him

together.

for people, we use words like, hospice, terminal illness,

declining. for roadkill, we use words like, flattened, gone.

my father is so gone . . . the morphine flattens his memory until he can't even remember my name –

he always taught me that, when the dog can't walk anymore, you take it out back with a shotgun. end its misery, he would say.

i wonder how many things he has loved,
only to look into their eyes,
his large hand cradling their soft and greying jawlines,
lean the gun against their sagging stomachs,
and pull the trigger.

i wonder how their limp bodies fell,
if he hugged them to his chest,
if he cried,
if he dug the hole before or after the animal turned into

a body.

i sort his pills by the hour and wonder how he knew it

was time?

the only difference between a dead dog and roadkill is that the dog was loved. but its body will bloat the same if left in the sun -- its body will rot the same -- either way, all i can do is drive past -- my father's body is on my way home. his body is on the way to the store. his body is on the way to everywhere i need to go -- and i drive past, and the maggots bite into his eyes, i drive past, and the sores on his legs widen, i drive past, and his purple legs burn red in the sun, and he splits, and the illness breaks a thousand glasses until we live in a house of shards –

sometimes, i want to drag his body out back,
my small hand cradling his soft and greying jawline,
hold his face in my hand like a white dandelion
about to burst into wishes,

lean the gun,

and pull.

(Pg 58) SOMETIMES I WANT TO HURT PEOPLE WHO HAVE HURT ME i post in the group chat that my dad died 20 minutes ago and i get a string of 7 heart emojis.

the space between them feels like the space between my own fingers where his hand used to fit in mine.

there are more emojis on a dog video i posted in 2017.

last week, i replied 6 hearts to someone who complimented my shirt.

i'm 24 and my dad is dead
and everyone is busy going to work
and paying their bills
and going to class
and typing out novels about their favorite ice cream

and i sit there, with my 7 hearts, each point digging into my arm as i cry on my couch alone.

(Pg 12-13) MY DAD DIED A WEEK AGO (excerpts) and i kiss the top of his urn like i kissed his dead forehead in the moment after. the feeling of his skin under my lips, chalked with cooling sweat. i stand in the middle of a field and pretend to pray. i chicken out halfway to belief . . . i make belief.

cremation doesn't actually produce ash.
instead, the skin and muscle burn away entirely,
leaving just the weakened skeleton,
which is thrown into a blender,
crushed, and returned to you.

(Pg 29) A HAND BECOMES (excerpt) my dad doesn't have a grave except the one inside my

lungs. i visit the cemetery anyway. i sit next to the oldest gravestone and open up a book to

read. i say out loud, hello, and am always surprised when no one answers.

(Pg 13) MY DAD DIED A WEEK AGO (excerpt)
. . . after he died, the summer was gone,
and now, all i can do is wait.
i walk into his room and fold up his glasses.
they creak like they are still expecting a face.

(Pg 16-17) I WATCHED HIM DIE (excerpt)
i think the last thing he said to me was
don't pour water down my f****ing throat,
but i don't remember because he stopped
being able to talk two days before he died.

this was a "peaceful" death, but, when they say "peaceful," they mean compared to, like, being stabbed

to death with 600 tiny forks. the truth is, the body wants to live, and so there is always gasping.

(Pg 18) . . . the body tries to live every single second before

it can't.

(from If the Cells That Make Up Hair are Already Dead)

(Pg 32) THAT’S WHAT YOU SWALLOW WHEN YOU
LET YOUR GRAVES OVERFLOW (excerpt)
your sister says, i almost hope he chooses to die.
and you know she doesn't just almost hope it
but that she actually does hope it,
because it's been 5 years and we are all so tired.
tired of calling the nurse, calling off work, crying into a

pillow. tired of digging the grave so many times our backyards have become cemeteries.

(Pg 29) A HAND BECOMES (excerpt) i hold his hand until it is time to unwrap the life from his

body, to unwrap my father from a corpse.

i keep coming back to this moment of dying.
how it was not like what i had expected.
there was no last word, no wisdom,
no wind, nothing to blow open our grief,
no soundtrack except the cough
of the man dying in the room next door.

some people say their dead looked so peaceful
they could swear they were sleeping.
for my father, it was the other way around.
for months, every time he slept,
i could swear he was already dead.

i watched my dad die. [and now]

(Pg 16-17) I WATCHED HIM DIE (excerpt)
my hands don't know how to sit still.
they want to be adjusting his glasses
and bringing a tissue to his nose
and pouring him a drink
and brushing his hair, and you know what?

i loved holding his hand. i loved tucking him in. i loved kissing his forehead before i said goodbye.
```

---

## IC-1595: If I Ran the Zoo

- Title: If I Ran the Zoo
- Author (byline): Theo Geisel (aka Dr. Seuss)
- Work: Not specified
- Publisher: Random House
- Publication date as stated: Oct 1950
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 728
- Already set (do not supply): none

### Source block (context only)

```text
Author: Theo Geisel (aka Dr. Seuss
ISBN: 978-0394800813
Publisher: Random House
Date (Month/Year): Oct 1950
```

### Introduction (context only: never use it for content warnings)

```text
If I Ran the Zoo, a notion most plain,
Is the name if our book, born in the brain
Of one Theodore Geisel, a.k.a. Dr. Seuss,
Our modern day, kooky, and male Mother Goose.

Reality here is a little askew,
Thanks to the mind of Gerald McGrew,
Who thought to himself just what he'd do,
If he ever managed to nab him a zoo.

If I Ran the Zoo by Theo Geisel (aka Dr. Seuss)
```

### Performance text (classify this)

```text
“It’s a pretty good zoo,” Said young Gerald McGrew, “And the fellow who runs it Seems proud of it too.

But if I ran the zoo,” Said young Gerald McGrew, “I’d make a few changes. That’s just what I’d do.

The lions and tigers and that kind of stuff
They have up here now are not quite good enough.
You see things like these in any old zoo.
They’re awfully old-fashioned. I want something new!

So I’d open each cage, I’ll unlock every pen,
Let the animals go and start over again.
And somehow or other I think I could find
Some beasts of some beasts of a more unusual kind.

A four-footed lion’s not much of a beast. The one in my zoo will have 10 feet at least. Five legs on the left and five more on the right. Then people will stare, and they’ll say, ‘What a sight!’ My New Zoo, McGrew Zoo, will make people talk. My new zoo, McGrew zoo, will make people gawk.

They’ll be so surprised, they’ll swallow their gum. They’ll ask when they see my strange animals come, ‘Where do you suppose he gets things like that from?’ If you want to catch beasts you don’t see every day, You have to go places quite out of the way. You have to go places no others can get to. You have to get cold and you have to get wet too.

I’ll catch ‘em in caves, I’ll catch ‘em in brooks, I’ll catch ‘em in crannies, I’ll catch ‘em in nooks That you don’t read about in geography books.

I’ll load up five boats with a family of Joats
Whose feet are like cows, but wear squirrel-skin coats,
And sit like dogs, but have voices like goats—
Excepting they can’t sing the very high notes.

And then I’ll go down to the Wilds of Nantucket, And capture a family of Lunks in a bucket. Then people will say, ‘Now I like that boy heaps. His New Zoo, McGrew Zoo, is growing by leaps. He captures them wild, he captures them meek, He captures them slim, he captures them sleek. What do you suppose he will capture next week?’

In the far western part
In southeast North Dakota
Lives a very fine animal called the Iota.
But I’ll capture one
Who is even much finer
In the northeastern west part of South Carolina.

When people see him they will say, ‘Now by thunder! This New Zoo, McGrew Zoo, is really a wonder!’

I’ll bag a big bug
Who is very surprising,
A feller who has
A propeller for rising
And zooming around making cross-country hops,
From Texas to Boston with only two stops.
Now that kind of thing for a bug is just tops!

In a cave in Kartoom is a beast called a Natch
That no other hunter’s been able to catch.
He’s hidden for years in his cave with a pout
And no one’s been able to make him come out.
But I’ll coax him out with a wonderful meal
That’s cooked by my cooks in my cooker mobile.

They’ll fix up a dish that is just to his taste; Three chicken croquettes made of library paste. Then sprinkled with peanut shucks, pickled and spiced, Then baked at 600 degrees and then iced. It’s mighty hard cooking to cook up such feasts But that’s how the New Zoo, McGrew Zoo, gets beasts.

‘He hunts with such vims, he hunts with such vigor. His new zoo, McGrew’s Zoo, gets bigger and bigger.’

Then the whole town will gasp, ‘Why this boy never sleeps! No keeper before ever kept what he keeps.

There’s no telling what that young fellow will do!’ And then, just to show them, I’ll sail to Katroo And bring back an It-Kutch, a Preep and a Proo, A Nerkle, a Nerd and a Seersucker too.

‘This Zookeeper, New keeper’s simply astounding.’ He travels so far that you think he’d drop! When do you suppose this young fellow will stop?’

Stop… ? Well, I should. But I won’t stop until I’ve captures the FizzamaWizzamaDill, The world's biggest bird from the Island of Gwark Who only eats pine trees and spits out the bark. And boy! When I get him back home to my park, The whole world will say, ‘Young McGrew’s made his mark.’
```

---

## IC-1596: The New Colossus, The Newer Colossus and Immigrants in Our Own Land

- Title: The New Colossus, The Newer Colossus and Immigrants in Our Own Land
- Author (byline): Emma Lazarus, Karen Finneyfrock and Jimmy Santiago Baca
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
Author: Emma Lazarus
Book: The Poems of Emma Lazarus, Volume II
ISBN: 978-0486786438
Publisher: Dover Publications
Date (Month/Year): Jan 2015
Author: Karen Finneyfrock
Book: We Will be Shelter
ISBN: 978-1938912474
Publisher: Write Bloody Publishing
Date (Month/Year): Dec 2014
Author: Jimmy Santiago Baca
Book: Immigrants in Our Own Land & Selected Early
Poems
ISBN: 978-0811211451
Publisher: New Directions
Date (Month/Year): Nov 1990
```

### Introduction (context only: never use it for content warnings)

```text
Between 1820 and 1920, approximately 34 million persons immigrated to the United States, three-fourths of them staying permanently. For many of these newcomers, their first glimpse of America was the Statue of Liberty in New York harbor.

The Jewish American poet Emma Lazarus saw the statue as a beacon to the world. The poem you just heard (The New Colossus) is carved on that pedestal, and at the time captured what the statue had come to mean to the millions who migrated to the United States seeking freedom.

But times change and so do societies . . . . It is now over 100 years from the date that the Statue of Liberty was opened on October 28, 1886 and Karen Finnefrock has revisited the theme of immigration from the viewpoint of Lady Liberty in her poem The Newer Colossus.
```

### Performance text (classify this)

```text
The New Colossus by Emma Lazarus Not like the brazen giant of Greek fame, With conquering limbs astride from land to land; Here at our sea-washed, sunset gates shall stand A mighty woman with a torch, whose flame Is the imprisoned lightning, and her name Mother of

Exiles. From her beacon-hand Glows world-wide welcome; her mild eyes command The air-bridged harbor that twin cities frame. “Keep, ancient lands, your storied pomp!" cries she With silent lips. “Give me your tired, your poor, Your huddled masses yearning to breathe free, The wretched refuse of your teeming shore.

Send these, the homeless, tempest-tost to me, I lift my lamp beside the golden door!”

The Newer Colossus by Karen Finnefrock

My feet have been wilting in this salt-crusted cement since the French sent me over on a steamer in pieces. I am the new Colossus, wonder of the modern world, a woman standing watch at the gate of power.

The first night I stood here, looking out over the

Atlantic like a marooned sailor, plaster fell from my lips parting and I said, Give me your tired, your poor, like a woman would say it, full of trembling mercy, while the rats ran over my sandals and up my stairwell, I was young then and hopeful.

I didn’t know who Europe and Asia, eventually the Middle East, would keep pushing their wretched through the

bay like a high tide. I am choking on the words I said about the huddled masses, they huddle on rafts leaving Cuba

and we turn them back. They huddle in sweltering truck backs

crossing the desert and we arrest them. I heard about a

container ship where three Chinese hopefuls died from lack of

oxygen pretending to be dishrags for our dollar stores. How can

we not have room for them? We still have room for golf

courses.

I am America’s first liar, forget about George

Washington. My hypocrisy makes me want to plant my dead face in

the waves. The ocean reeks of fish and tourism, my optimist

heart corrodes in the salt wind.

Give me your merchandise, I should say.

Give me your coffee beans. Give me your bananas and avocados, give me your rice. We turn our farmland into

strip malls, give me things to sell at my strip malls. Give me

your Ethnic cuisine, your cheaply made plastics, give me, by trembling boatload, your Japanese cars. Give me your

oil.

Not so I can light my lamp with it, but to drool it from the thirsty lips of my lawn mowers. Give me your jealousy, your yearning to crawl inside my hollow bones and sleep in my skin made of copper. Look,

over there is New York. Doesn’t it glow like the cherry end of a cigarette? Like a Nebula from the blackness of space out here in the harbor? Wait with me. Watch

it pulse like a hungry lion until morning. I should tell you to enjoy it from here. You will never be allowed to come in.

TRANSITION

No matter what your politics on the issue of immigration

are, it is important to remember that all immigrants come to

America with our own hopes and dreams, but too often we

face inevitable disappointment instead. We’re not always

who you think we are. Some pick your strawberries or care

for your children. Some are in high school or college. And

many sit in jail cells awaiting deportation.

Me? I grew up here. This is my home. Yet even though I

think of myself as an American and consider America my

country, my country doesn’t think of me as one of its own.

Immigrants in Our Own Land by Jimmy Santiago Baca.

Immigrants in Our Own Land

by Jimmy Santiago Baca

We are born with dreams in our hearts,

looking for better days ahead.

At the gates we are given new papers,
our old clothes are taken
and we are given overalls like mechanics wear.
We are given shots and doctors ask questions.
Then we gather in another room
where counselors orient us to the new land
we will now live in. We take tests.
Some of us were craftsmen in the old world,
good with our hands and proud of our work.
Others were good with their heads.
They used common sense like scholars
use glasses and books to reach the world.
But most of us didn’t finish high school.

The old men who have lived here stare at us, from deep disturbed eyes, sulking, retreated. We pass them as they stand around idle, leaning on shovels and rakes or against walls. Our expectations are high: in the old world, they talked about rehabilitation, about being able to finish school, and learning an extra good trade.

But right away we are sent to work as dishwashers,
to work in fields for three cents an hour.
The administration says this is temporary
So we go about our business, blacks with blacks,
poor whites with poor whites,
chicanos and indians by themselves.
The administration says this is right,
no mixing of cultures, let them stay apart,
like in the old neighborhoods we came from.

We came here to get away from false promises, from dictators in our neighborhoods, who wore blue suits and broke our doors down when they wanted, arrested us when they felt like, swinging clubs and shooting guns as they pleased. But it’s no different here. It’s all concentrated. The doctors don’t care, our bodies decay, our minds deteriorate, we learn nothing of value. Our lives don’t get better, we go down quick.

My cell is crisscrossed with laundry lines,
my T-shirts, boxer shorts, socks and pants are drying.
Just like it used to be in my neighborhood:
from all the tenements laundry hung window to window.
Across the way Joey is sticking his hands
through the bars to hand Felipé a cigarette,
men are hollering back and forth cell to cell,
saying their sinks don’t work,
or somebody downstairs hollers angrily
about a toilet overflowing,
or that the heaters don’t work.

I ask Coyote next door to shoot me over
a little more soap to finish my laundry.
I look down and see new immigrants coming in,
mattresses rolled up and on their shoulders,
new haircuts and brogan boots,
looking around, each with a dream in their heart,
thinking they’ll get a chance to change their lives.

But in the end, some will just sit around talking about how good the old world was.

Some of the younger ones will become gangsters.
Some will die and others will go on living
without a soul, a future, or a reason to live.
Some will make it out of here with hate in their eyes,
but so very few make it out of here as human
as they came in, they leave wondering what good they are

now as they look at their hands so long away from their tools, as they look at themselves, so long gone from their

families, so long gone from life itself, so many things have changed.
```

---

## IC-1597: If You Have to Ask

- Title: If You Have to Ask
- Author (byline): Gabriel Green; Marvin Hodges, Em
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1064
- Already set (do not supply): none

### Source block (context only)

```text
Author: Gabriel Green
ISBN: On-Line Transcript
https://slampoetryforthesoul.wordpress.com/2016/06/27/ask
-a-black-dude/
Publisher: Slam Poetry for the Soul
Date (Month/Year): June 27, 2016
Author: Marvin Hodges, Em Allison and Saidu Tejan-
Thomas
ISBN: On-Line Transcript
https://voicemalemagazine.org/da-rules/
Publisher: Voice Male Magazine.org
Date (Month/Year): June 24, 2015
View the performance of this poem in 3 voices here:
https://www.youtube.com/watch?v=xpvutGPY7zU
```

### Introduction (context only: never use it for content warnings)

```text
Ever had a white friend, acquaintance or even complete stranger ask you a question that was SO past offensive that you couldn’t even think of a rude enough answer? Gabriel Green is here to help with his comical yet insightful piece, “Ask a Black Dude,” that aims to addresses some of the most common questions that we, as black people, are asked. And if that’s not quite enough, Marvin Hodges, Em Allison and Saidu Tejan-Thomas take it one step further and explain “Da Rules” for black people in America today.
```

### Performance text (classify this)

```text
Allison and Saidu Tejan-Thomas

Ask a Black Dude

Have you ever had a question you wanted to ask that one black person you know, But refrained because you didn’t want to run the risk of sounding racist? Ever wish there was just a one-stop shop for all things black? Think about it, access to your very own single authority and spokesperson for an entire race of people. Well, son-of-a-gun, you’re in luck because today, for a limited time only, you have access to your friendly neighborhood ask a black dude;

Ask a Black Dude: A mail-in encyclopedia complete with answers to questions that’ll boggle the minds of white people for centuries. Let’s give it a try, shall we?

Question: Why are black people so good at basketball?

Answer: We’re not. There isn’t some magical chromosome in Lebron James’ DNA that makes him genetically prone to run faster or jump higher than everyone else, But just think, if everything around you stated that your best alternative was either jail or the cemetery, you’d be shooting a thousand jumpers a day too. Next question. Umm, do black people hate ALL white people? Of course, we don’t. We just hate people who perpetuate or refuse to acknowledge the history of social, cultural, political, and racial ****** placed against us; That their white is pure coincidence. Next question. Why are black women so angry? This has multiple answers. They are a queen in a land where men take turns ***** on her throne, Her body is the subject you left in private but never worth your love and respect in public, Or 3, she will raise her sons to become young tombstones or men who will call her b**** with the same mouth they used to feed from her nurturing bosoms; Pick one. Next question. Uh, why don’t black people trust the government? Let’s put this in terms you can understand. So . . . remember that classic Charlie Brown bit where Lucy wanted to get Charlie to kick the football but Charlie didn’t want to, because he knew that as soon as he would try, Lucy would pull the ball away only for Charlie to hurt himself, But somehow, Lucy convinced him anyway only for Charlie to meet his identical fate.

Guess which one is Lucy.
Next question.
Is it . . . is it racist . . . is it racist if I . . .
Yes. Next question
Um, why can’t white people use the ‘N-word’?
What, ‘neighbor’?
Of course, you can use it.
It’s an endearing term commonly used in phrases like:
“What’s good, my neighbor?”
Or, “Man, that neighbor’s crazy.”
Or my personal favorite, “****, I wish a neighbor
would.”
This product is satisfaction guaranteed.
You’ll understand black culture in just 30 days.
Your friends will envy at your new-found liberal, social
consciousness.
Call today and receive a free bonus gift of a black fist afro
pick and a ‘Can’t take off’ scarf.
You’ll be down with the struggle in no time.
Call while supplies last.
Disclaimer: The views, opinions, and answers given by this
one African American . . . black person is not a direct
reflection of black people everywhere.
Results may vary.

Da Rules

Be accommodating
Smile
Be polite
Slouch a little when they see you.

Confidence scares them. Be gentle,

Eyes low

No sudden movements Don’t have objects like squares and rectangles in your

pockets Don’t reach for your wallet

Why did you run?

You got something to hide?

Keep that rap music low,

You may be shot for it
Be seen and not heard.
Do not fit the description
Your hair announces your presence

It is loud just like you

keep it tamed and hushed down.

Let them touch it [hair] when they ask

Get relaxers

You wear your hair straight

So why can’t they get braids, dreads, afros
Do not cry.
Do not break rules,
Do not have accidents

Or get in arguments Wear bright clothing Let the other guy have the stronger handshake Do not tell white friends you’re on scholarship Do not watch Roots Stay away from ancestry.com

You won’t find what you’re looking for
Be regular
Be good
Cross to the other side of the street so they

don’t have to
Do not smoke
Do not drink
Do not have sex,

We have enough of you Do not throw up sideways peace signs

it looks too much like a gang sign

You are a gang sign
Don’t be a statistic
Don’t be a baby daddy
Do not date outside your race

Your own people will consider you a sell out

anyway

“What, you not strong enough to handle a black

woman?” Do not build empires Do not build things exclusively for the betterment of your

race

That’s reverse racism

Do you hear me boy?

Speak when I’m talking to you son
Speak when you pass them on the street
Do not pass “Go”
Do not collect $200
Go straight to jail
Do not express yourself

or walk around Wal-Mart with a Wal-Mart gun Do not wear hoodies

Or walk in white neighborhoods in

Texas, Arizona, Florida Bite the bullet

Why are you shooting yourself?

Why are you shooting yourself?

Why are you people always shooting yourselves?

In the chest, while handcuffed. Do not raise your hand in class

You’ll just be another negro without answers Light skins be proud

that you are comfortable black

your ambiguity so interesting Wait!

But my melanin has meaning

It is profound

Dark skin so greedy

It gobbles up nouns

thoughts so tangled

Look what it did to my hair.

Reaching to the sky at all angles

Praying that you don’t shoot I’ve always been black.

But I didn’t always know it.

I guess it’s because I didn’t-
Have a thinner nose
Have smaller lips
Be lighter
Be Wayne Brady

White people love Wayne Brady he makes Bryant

Gumbel look like Malcolm X
Do not quote Malcolm X
Do not read for fun
Do not own a gun
Let your non-black friends say “nigga”

Pretend it doesn’t bother you If their women fear for their lives, that’s great If their women fear for the lives of their children even

better Be small.

Your dark frame casts a very large shadow

Do not be 6’4 292 pounds
Kinky follicles curled into grenades
Don’t you know that black bodies are weapons?
Don’t you know they have weapons?
```

---

## IC-1598: Imagine and OCD

- Title: Imagine and OCD
- Author (byline): ‘Kristen’ and Neil Hilborn
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 808
- Already set (do not supply): none

### Source block (context only)

```text
Author: Vrinda Pendred (ed)
Book: Check Mates: A Collection of Fiction, Poetry and
Artwork About Obsessive-Compulsive Disorder, by
People with OCD
ISBN: 978-0956452900
Publisher: Conditional Publications
Date (Month/Year): May 2010
Author: Neil Hilborn
Book: Viral
ISBN: 978-0989641517
Publisher: Button Poetry
Date (Month/Year): Dec 2013
```

### Introduction (context only: never use it for content warnings)

```text
ADHD, OCD, or Asperger’s syndrome - as children we are not educated on the humanity of those with mental disorders. We are simply told that they are different . . . special. As we grow older, they become a topic, a subject, an objectification . . . never a peer. We approach them as if they are fragile objects, so volatile that one wrong move can trigger a breakdown. We befriend them out of pity. We befriend them out of curiosity. We observe them from afar, analyze their ticks, hide our creeping superiority, or in some cases, disguise disgust as ignorance. We are never real with them. If only we could . . . Imagine by ‘Kristen’ (last name withheld by editor)
```

### Performance text (classify this)

```text
IMAGINE

Imagine getting dressed in the morning Then realizing you did it “wrong”, And that you have to take off your clothes And start over And over And over again . . . .

Imagine having to tap your foot in a 16-beat pattern While other people watch, half amused, half freaked out. Imagine being forced to keep it going for hours And hours And even more hours . . .

Imagine becoming “stuck” in front of a mirror, Staring at imperfections that no other human would notice, Unable to move as the minutes tick by And by And by . . .

Imagine
Imagine being fired from work
Because of all these things you do --
Imagine being alienated from people around you
Because everyone thinks you’re “weird” –
Imagine dealing with this monstrous OCD until you die
Until you die
Until you die.

TRANSITION

But what happens when people with mental disorders get real with us? What happens when we find out that they feel just as we feel, and in the case of Neil Hilborn’s poem OCD, are capable of expressing their feelings more beautifully than we could ever dream of?

Mental disorders are real. But humanity is real too. And if we cannot recognize the humanity in every single individual, regardless of their handicap, disorder, differences -- then we are the ones with a mental disorder, and it’s more debilitating than ADHD, OCD, or Asperger’s syndrome could ever be– it’s a disease of apathy.

OCD by Neil Hilborn OCD

The first time I saw her

everything in my head went quiet.

All the ticks, all the constantly refreshing images just disappeared.

When you have Obsessive Compulsive Disorder, you don’t really get quiet moments.

Even in bed, I’m thinking:

Did I lock the doors? Yes.
Did I wash my hands? Yes.
Did I lock the doors? Yes.
Did I wash my hands? Yes.

But when I saw her, the only thing I could think about was the hairpin curve of her lips

or the eyelash on her cheek— the eyelash on her cheek— the eyelash on her cheek.

I knew I had to talk to her.

I asked her out six times in thirty seconds.

She said yes after the third one, but none of them felt right, so I had to keep going.

On our first date, I spent more time organizing my meal by color than I did eating, or fucking talking to her

But she loved it.

She loved that I had to kiss her goodbye sixteen times or twenty-four times if it was Wednesday.

She loved that it took me forever to walk home because there are lots of cracks on our sidewalk!

When we moved in together, she said she felt safe, like no one would ever rob us because I definitely locked the door eighteen times.

I’d always watch her mouth when she talked—
when she talked—
when she talked—
when she talked

when she said she loved me, her mouth would curl up at the edges.

At night, she’d lay in bed and watch me turn all the lights off, and on, and off, and on, and off, and on, and off, and on, and off, and on, and off.

She’d close her eyes and imagine that the days and nights were just passing in front of her.

But some morning, I started kissing her goodbye but then she’d just leave because I was making her late for work.

When I stopped in front of a crack in the sidewalk, she just kept walking

When she said she loved me, her mouth was a straight line

She told me I was taking up too much of her time

Last week she started sleeping at her mother’s place.

She told me that she shouldn’t have let me get so attached to her; that this whole thing was a mistake, but,

How can it be a mistake when I don’t have to wash my hands after I touch her?

Love is not a mistake, and it’s killing me that she can run away from this and I just can’t.

I can’t go out and find someone new

Because I always think of her.

Usually, when I obsess over things, I see germs sneaking into my skin.

I see myself crushed by an endless succession of cars And she was the first beautiful thing I ever got stuck on.

I want to wake up every morning thinking about the way she holds her steering wheel

How she turns shower knobs like she opening a safe.

How she blows out candles—
blows out candles—
blows out candles—
blows out candles—
blows out—

Now, I just think about who else is kissing her.

I can’t breathe because he only kisses her once—he doesn’t care if it’s perfect!

I want her back so bad,

I leave the door unlocked –

I leave the lights on.
```

---

## IC-1599: The Impact of Teachers

- Title: The Impact of Teachers
- Author (byline): Not specified
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1287
- Already set (do not supply): none

### Source block (context only)

```text
Author: Kevin M. Derrig
Book: The Spoken Word Revolution: Slam, Hip Hop &
the Poetry of a New Generation
ISBN: 978-1402202469
Publisher: Sourcebooks, Incorporated
Date (Month/Year): March 2005
Author: Livia Kent
Book: The Bookwoman, v. 67, no. 3
ISBN: N/A
Publisher: Women’s National Book Association
Date (Month/Year): Fall 2004
*The Bookwoman — The Official Publication of the
Women’s National Book Association (published, 4x per
year; print circulation, 13,500)
```

### Introduction (context only: never use it for content warnings)

```text
First Period by Kevin M. Derring
```

### Performance text (classify this)

```text
Fist Period by Kevin M. Derrig &

No Writer Left Behind by Livia Kent

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

TRANSITION Teachers should never minimize the role they play in influencing students' lives. Hopefully, unlike Kevin Derrig’s experience, that role will be positive, possessing the qualities of a "charismatic adult" who not only touches students' minds but also their spirits -- the way they see and feel about themselves for the rest of their lives. Such influence is truly a rare privilege that should be prized and nurtured. For every dream-stifling, spirit-crushing teacher there are many others who breathe life into the dreams of student. There are teachers like Livia Kent . . . . who nurtures, inspires and sincerely believes that there will be No Writer Left Behind.

I teach poetry at an inner-city middle school where my students complain about having to fill a blank page with meaningful words. But I watch as they struggle to find similes that adequately reflect their personalities and experiences. I watch as they start to hone their poetic voices, not for accolades, but because they've recognized that through hyperbole and personification and synethesia-all those big words they refuse to remember-they can genuinely disclose their feelings to a back stabbing peer, a preoccupied parent, or even a murdered cousin whose pull once seemed greater that the sun's.

For one of the first classes I taught I played Chopin and asked my students to transcribe the sounds into images. After the inevitable objections-why can't we hear the radio, classical music sucks-I finally persuaded them to close their eyes and listen. A resulting poem, written by the one girl who had perfected the art of eye-rolling, began with a visceral description of a frightened woman running through a forest. She loses a shoe but can't stop to pick it up. She is tired and out of breath and in the end turns out to be running from herself. While I had commended myself earlier on pointing out the ties between the poetry my students shunned and the hip-hop they loved, it was ultimately the inner acuity of this girl's poem that convinced my students writing was worthy of their time.

Of course the beginning of every year brings new students who tell me they neither read nor write for pleasure. But I remind myself that since the school librarian was fired to minimize expenses, the authors they may have been tempted to pick up and emulate are now inaccessible. So I drag them, kicking and screaming, over the sculpted language of Nikki Giovanni's "Cotton Candy on a Rainy Day." And I tell them, as they rustle their concealed snacks, that I forgive their prickly resistance because I know what it's like be starved. Recently, one girl took issue with my comment.

"My grandma buys food and cooks for me every day. You can't come here and tell us we don't get fed."

I explained that it was poetic malnourishment I had been referring to

The United Nations views "literacy as freedom." Yet in a school where children can read and write but are reluctant to do either, what turns out to be their key to freedom is literary expression, which must sometimes be forced down their throats.

For an entire year I taught a seventh-grade boy whose writing averaged a half a sentence per two-hour class. Most of the time he spent chewing on his cuticles and making sure his baseball cap sat sufficiently crooked on his head. One day, after an exercise inspired by Pablo Neruda's collection, The Book of Questions, this boy raised his hand for the first time that year. To my surprise he wanted to share what he had written.

"But, Steve," I whispered, "you've only written one line."

He shrugged. The title of his poem was a question I had posed earlier, a question I doubted any of my writers would dare to tackle. "What is Eternity?" he read. And his answer was as follows: "Eternity is an abandoned house that is never vacant, a black smudge that is always clean." The class erupted in applause, and this boy's shy recitation of a one-line poem, the smile on his otherwise stern little face-this moment will remain the reason I cannot join the teachers who lament the superficiality of today's youth.

Throughout the ages there have always been troublemakers, reticent boys, heartbroken girls, angry teenagers lost in a sense of isolation. What we as teachers must remember is that although these children may not always be churning out high-minded grammatically correct prose, as long as they are writing creatively, they are groping their way, word by word, out of the dim and complex years of adolescence. Hopefully, as they become adults, they will carry with them an insatiable hunger for great literature-writing they can taste and feel and tamp into the souls of the next turbulent generation.
```

---

## IC-1600: The Imperative to Choose A Collection

- Title: The Imperative to Choose A Collection
- Author (byline): Robert Frost
- Work: Robert Frost's Poems (Pgs 95, 123 and 90)
- Publisher: St. Martin's Press
- Publication date as stated: March 2002
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1396
- Already set (do not supply): none

### Source block (context only)

```text
Author: Robert Frost
Book: Robert Frost's Poems (Pgs 95, 123 and 90)
ISBN: 978-0312983321
Publisher: St. Martin's Press
Date (Month/Year): March 2002
```

### Introduction (context only: never use it for content warnings)

```text
Poet Robert Frost believed that human beings live isolated lives, despite being in close proximity to each other. And while Frost often emphasized human loneliness and alienation; he also believed that despite our separation, humans are social beings. In poems like “Mending Wall,” “The Wood-Pile” and “Birches” Frost echoes again and again the human imperative to choose, to take some action, even when there is no basis for choosing. To choose society over isolation, to choose life over death, to choose happiness over sorrow.

The Imperative to Choose – A Collection by Robert Frost
```

### Performance text (classify this)

```text
Mending Wall (Pg 95) Something there is that doesn't love a wall, That sends the frozen-ground-swell under it, And spills the upper boulders in the sun; And makes gaps even two can pass abreast. The work of hunters is another thing: I have come after them and made repair Where they have left not one stone on a stone, But they would have the rabbit out of hiding, To please the yelping dogs. The gaps I mean, No one has seen them made or heard them made, But at spring mending-time we find them there. I let my neighbour know beyond the hill; And on a day we meet to walk the line And set the wall between us once again. We keep the wall between us as we go. To each the boulders that have fallen to each. And some are loaves and some so nearly balls We have to use a spell to make them balance: "Stay where you are until our backs are turned!" We wear our fingers rough with handling them. Oh, just another kind of out-door game, One on a side. It comes to little more: There where it is we do not need the wall: He is all pine and I am apple orchard. My apple trees will never get across And eat the cones under his pines, I tell him. He only says, "Good fences make good neighbours."

Spring is the mischief in me, and I wonder
If I could put a notion in his head:
"Why do they make good neighbours? Isn't it
Where there are cows? But here there are no cows.
Before I built a wall I'd ask to know
What I was walling in or walling out,
And to whom I was like to give offence.
Something there is that doesn't love a wall,
That wants it down." I could say "Elves" to him,
But it's not elves exactly, and I'd rather
He said it for himself. I see him there
Bringing a stone grasped firmly by the top
In each hand, like an old-stone savage armed.
He moves in darkness as it seems to me,
Not of woods only and the shade of trees.
He will not go behind his father's saying,
And he likes having thought of it so well
He says again, "Good fences make good neighbours."

TRANSITION When faced with choices about what path to take in life, there are advantages and disadvantages to all decisions. All choices have the potential for surprises, joys, and sorrows. Nonetheless, we must choose only one; And once a choice has been made, often there is no going back.

The Wood-Pile
(Pg 123) Out walking in the frozen swamp one grey day
I paused and said, "I will turn back from here.
No, I will go on farther--and we shall see."
The hard snow held me, save where now and then
One foot went down. The view was all in lines
Straight up and down of tall slim trees
Too much alike to mark or name a place by
So as to say for certain I was here
Or somewhere else: I was just far from home.
A small bird flew before me. He was careful
To put a tree between us when he lighted,
And say no word to tell me who he was
Who was so foolish as to think what he thought.
He thought that I was after him for a feather--
The white one in his tail; like one who takes
Everything said as personal to himself.
One flight out sideways would have undeceived him.
And then there was a pile of wood for which
I forgot him and let his little fear
Carry him off the way I might have gone,
Without so much as wishing him good-night.
He went behind it to make his last stand.
It was a cord of maple, cut and split
And piled--and measured, four by four by eight.
And not another like it could I see.
No runner tracks in this year's snow looped near it.
And it was older sure than this year's cutting,
Or even last year's or the year's before.
The wood was grey and the bark warping off it
And the pile somewhat sunken. Clematis
Had wound strings round and round it like a bundle.
What held it though on one side was a tree
Still growing, and on one a stake and prop,
These latter about to fall. I thought that only
Someone who lived in turning to fresh tasks
Could so forget his handiwork on which
He spent himself, the labour of his axe,
And leave it there far from a useful fireplace
To warm the frozen swamp as best it could
With the slow smokeless burning of decay.

TRANSITION

And while we can’t go back, we can always remember what it was like to be a child. As we get older, we often get so caught up in "grown up" business that we forget how to have pure fun. Not fun that comes from a specific kind of activity or being in a specific mood. Rather, fun born from the state of pure being. This sense of fun (some call it a sense of wonder) is abundant in small children who giggle joyously just because they are alive.

Birches
(Pg 90) When I see birches bend to left and right
Across the lines of straighter darker trees,
I like to think some boy's been swinging them.
But swinging doesn't bend them down to stay.
Ice-storms do that. Often you must have seen them
Loaded with ice a sunny winter morning
After a rain. They click upon themselves
As the breeze rises, and turn many-coloured
As the stir cracks and crazes their enamel.

Soon the sun's warmth makes them shed crystal shells
Shattering and avalanching on the snow-crust
Such heaps of broken glass to sweep away
You'd think the inner dome of heaven had fallen.
They are dragged to the withered bracken by the load,
And they seem not to break; though once they are bowed
So low for long, they never right themselves:
You may see their trunks arching in the woods
Years afterwards, trailing their leaves on the ground,
Like girls on hands and knees that throw their hair
Before them over their heads to dry in the sun.
But I was going to say when Truth broke in
With all her matter-of-fact about the ice-storm,
I should prefer to have some boy bend them
As he went out and in to fetch the cows--
Some boy too far from town to learn baseball,
Whose only play was what he found himself,
Summer or winter, and could play alone.
One by one he subdued his father's trees
By riding them down over and over again
Until he took the stiffness out of them,
And not one but hung limp, not one was left
For him to conquer. He learned all there was
To learn about not launching out too soon
And so not carrying the tree away
Clear to the ground. He always kept his poise
To the top branches, climbing carefully
With the same pains you use to fill a cup
Up to the brim, and even above the brim.
Then he flung outward, feet first, with a swish,
Kicking his way down through the air to the ground.
So was I once myself a swinger of birches.
And so I dream of going back to be.
It's when I'm weary of considerations,
And life is too much like a pathless wood
Where your face burns and tickles with the cobwebs
Broken across it, and one eye is weeping
>From a twig's having lashed across it open.
I'd like to get away from earth awhile
And then come back to it and begin over.
May no fate willfully misunderstand me
And half grant what I wish and snatch me away
Not to return. Earth's the right place for love:
I don't know where it's likely to go better.

I'd like to go by climbing a birch tree
And climb black branches up a snow-white trunk
Toward heaven, till the tree could bear no more,
But dipped its top and set me down again.
That would be good both going and coming back.
One could do worse than be a swinger of birches.
```
