# Classification request: batch 41 of 63 (40 records, IC-1601 to IC-1640)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-041-reply.json`.

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

## IC-1601: In a Shared Land

- Title: In a Shared Land
- Author (byline): Julia Alvarez and Naomi Shihab Nye
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1202
- Already set (do not supply): none

### Source block (context only)

```text
Author: Julia Alvarez
Book: The Other Side / ElOotro Lado
ISBN: 978-0452273412
Publisher: Plume
Date (Month/Year): Dec 1996
Author: Naomi Shihab Nye
Book: Honeybee, Pg 162
ISBN: 978-0060853907
Publisher: Greenwillow Books
Date (Month/Year): Feb 2008
```

### Introduction (context only: never use it for content warnings)

```text
According to the UN, Not since World War II have so many people been on the move. Violent conflict has displaced 38 million within their own countries and forced another 22 million to flee across a border. But numbers that vast defy understanding . . . so today we make it personal with 2 poems that eloquently describe what it means to be adrift. . . In a Strange Land by Julia Alvarez and Naomi Shihab Nye.

Before his assassination on a dark highway on 30 May 1961, the Dominican dictator, Rafael Trujillo, ruled with an iron fist for almost 30 years. Those who dared to oppose him were imprisoned, tortured and murdered. In her poem “Exile,” Julia Alvarez shares her childhood memory of fleeing her homeland for America. You see, her grandfather had been charged with conspiracy to overthrow Trujillo, and the lives of his entire family were at risk.
```

### Performance text (classify this)

```text
Exile by Julia Alvarez
The night we fled the country, Papi,
you told me we were going to the beach,
hurried me to get dressed along with the others,
while posted at a window, you looked out
at a curfew-darkened Ciudad Trujillo,
speaking in worried whispers to your brothers,
which car to take, who’d be willing to drive it,
what explanation to give should we be discovered . . .

On the way to the beach, you added, eyeing me. The uncles fell in, chuckling phony chuckles, What a good time she’ll have learning to swim! Back in my sisters’ room Mami was packing

a hurried bag, allowing one toy apiece,
her red eyes belying her explanation:
a week at the beach so Papi can get some rest.
She dressed us in our best dresses, party shoes.

Something was off, I knew, but I was young
and didn’t think adult things could go wrong.
So as we quietly filed out of the house
we wouldn’t see again for another decade,

I let myself lie back in deep waters,
my arms out like Jesus’ on His cross,
and instead of sinking down like I’d always done,
magically, that night, I could stay up,
floating out, past the driveway, past the gates,
in the black Ford, Papi grim at the wheel,
winding through the back roads, stroke by difficult stroke,
out on the highway, heading toward the coast.

Past the checkpoint, we raced toward the airport,
my sisters crying when we turned before
the family beach house, Mami consoling,
there was a better surprise in store for us!

She couldn’t tell, though, until… until we were there.
But I had already swum ahead and guessed
some loss much larger than I understood,
More danger than the deep end of the pool.

At the dark, deserted airport we waited.
All night in a fitful sleep, I swam.
At dawn the plane arrived, and as we boarded,
Papi, you turned, your eyes scanned the horizon

as if you were trying to sight a distant swimmer,
your hand frantically waving her back in,
for you knew as we stepped inside the cabin
That a part of both of us had been set adrift.

Weeks later, wandering our new city, hand in hand, you tried to explain the wonders: escalators as moving belts; elevators: pulleys and rope; blonde hair and blue eyes: a genetic code.

We stopped before a summery display window at Macy’s, The World’s Largest Department Store, to admire a family outfitted for the beach: the handsome father, slim and sure of himself,

so unlike you, Papi, with your thick mustache, your three-piece suit, your fedora hat, your accent. And by his side a girl who looked like Heidi in my story book waded in colored plastic.

We stood awhile, marveling at America,
both of us trying hard to feel luckier
than we felt, both of us pointing out
the beach pails, the shovels, the sandcastles

no wave would ever topple, the red and blue boats. And when we backed away, we saw our reflections superimposed, big-eyed, dressed too formally with all due respect as visitors to this country.

Or like, Papi, two swimmers looking down at the quite surface of our island waters, seeing their faces right before plunging in, eager, afraid, not yet sure of the outcome.

TRANSITION

Today, the United States is experiencing its second great wave of immigration, a movement of people that has profound implications for a society that by tradition pays homage to its immigrant roots at the same time confronts complex and deeply ingrained ethnic and racial divisions. But I don’t want to live in a divided world. Fear and hatred of “the other” festering just below the slow boil of the American “melting pot.”

No . . . I want to live in a world where people connect across boundaries of race, ethnicity, geography and every other facet of identity. “This is the world I want to live in. The shared world.”

Wandering Around an Albuquerque Airport Terminal (aka Gate A-4) by Naomi Shihab Nye

After learning my flight was detained 4 hours,
I heard the announcement:
If anyone in the vicinity of gate 4-A understands any Arabic,
Please come to the gate immediately.
Well—one pauses these days. Gate 4-A was my own gate. I

went there. An older woman in full traditional Palestinian dress, Just like my grandma wore, was crumpled to the floor,

wailing loudly. Help, said the flight service person. Talk to her. What is her Problem? we told her the flight was going to be four hours

late and she
Did this.
I put my arm around her and spoke to her haltingly.
Shu dow-a, shu- biduck habibti, stani stani schway, min

fadlick, Sho bit se-wee? The minute she heard any words she knew—however

poorly used—
She stopped crying.
She thought our flight had been canceled entirely.
She needed to be in El Paso for some major medical

treatment the Following day. I said no, no, we’re fine, you’ll get there, just

late,
Who is picking you up? Let’s call him and tell him.
We called her son and I spoke with him in English.
I told him I would stay with his mother till we got on the

plane and Would ride next to her—Southwest. She talked to him. Then we called her other sons just for

the fun of it. Then we called my dad and he and she spoke for a while in

Arabic and Found out of course they had ten shared friends. Then I thought just for the heck of it why not call some

Palestinian Poets I know and let them chat with her. This all took up

about 2 hours. She was laughing a lot by then. Telling about her life.

Answering Questions. She had pulled a sack of homemade mamool cookies—little

powdered Sugar crumbly mounds stuffed with dates and nuts—out of

her bag— And was offering them to all the women at the gate. To my amazement, not a single woman declined one. It was

like a Sacrament. The traveler from Argentina, the traveler from

California, The lovely woman from Laredo—we were all covered with

the same Powdered sugar. And smiling. There are no better cookies. And then the airline broke out the free beverages from

huge coolers— Non-alcoholic—and the two little girls for our flight, one

African American, one Mexican American—ran around serving us

all apple juice And lemonade and they were covered with powdered sugar

too.

And I noticed my new best friend—by now we were holding

hands— Had a potted plant poking out of her bag, some medicinal

thing, With green furry leaves. Such an old country traveling

tradition. Always Carry a plant. Always stay rooted to somewhere. And I looked around that gate of late and weary ones and

thought, This is the world I want to live in. The shared world. Not a single person in this gate—once the crying of

confusion stopped —has seemed apprehensive about any other person. They took the cookies. I wanted to hug all those other

women too. This can still happen anywhere. Not everything is lost.
```

---

## IC-1602: In Relig Odhrain

- Title: In Relig Odhrain
- Author (byline): Neil Gaiman
- Work: Trigger Warning: Short Fictions and Disturbances (pg 261)
- Publisher: William Morrow Paperbacks
- Publication date as stated: Oct 2015
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 585
- Already set (do not supply): none

### Source block (context only)

```text
Author: Neil Gaiman
Book: Trigger Warning: Short Fictions and Disturbances
(pg 261)
ISBN: 978-0062330321
Publisher: William Morrow Paperbacks
Date (Month/Year): Oct 2015
```

### Introduction (context only: never use it for content warnings)

```text
Scottish history tells the tale of Saint Columa and Saint Oran . . . Fifteen centuries ago, a hot-tempered noble Irishman left his home. He had quarreled, and that quarrel had led to a battle. Many men were killed, and in penance, he left his native land, travelling to a remote island off the coast of Scotland with some companions. His name was Saint Columba – Among his twelve companions in exile was Saint Oran. They landed in Iona, which was to become their base for spreading the Gospel. First, though, a chapel was needed, for these were men of God, and must have a place to pray. So it was written.

But amongst official histories lie stranger tales – orally passed on with many variations through the years. As time passes, it becomes harder to know whether these tales are true, but they may tell us something about the people who passed them on, and about us, who hear them.

In Relig Odhrain by Neil Gaiman.
```

### Performance text (classify this)

```text
When Saint Columba landed on the island of Iona
His friend Oran landed with him
Though some say Saint Oran waited
in the shadows of the island, waiting for the saint to

land there, I believe they came together, came from Ireland, were

like brothers Were the blond and brave Columba and the dark man

they called Oran.

He was odran, like the otter, was the other. There were

others And they landed on Iona and they said, We’ll build a

chapel. It’s what saints did when they landed. (Oran: priest of

sun or fire Or from odhra, meaning dark-haired) But their chapel

kept on crumbling. And Columba took the answer from a dream or

revelation, That his building needed Oran, needed death in the

foundations.

Others claim it was doctrinal, and Saints Oran and

Columba Were debating, as the Irish love debating, about

Heaven, Since the truth is long-forgotten we are left with just

their actions (By their actions shall ye know them): Saint Columba

buried Oran Still alive, with earth about him, buried deep, with earth

upon him.

Three days later they returned there, stocky monks

with spades and mattocks And they dug down to Saint Oran, so Columba could

embrace him Touch his face and say his farewells. Three days dead.

They brushed the mud off When Saint Oran’s eyes blinked open. Oran grinned at

Saint Columba. He had died but now was risen, and he said the words

the dead know, In a voice like wind and water.

He said, Heaven is not waiting for the good and pure and

gentle There’s no punishment eternal, there’s no Hell for the

ungodly Nor is God as you imagine –

Saint Columba shouted “Quiet!” And to save the monks from error shoveled mud onto

Saint Oran. So they buried him forever. And they called the place

Saint Oran’s. In its churchyard kings of Scotland, kings of Norway, all

were buried On the island of Iona.

Some folk claim it was a druid priest of sunlight that

was buried In the earth of good Iona just to hold the church

foundations, But for me that’s much too simple, and it libels Saint

Columba (who cried “Earth! Throw earth on Oran, stop his mouth

with mud this moment Lest he bring us to perdition!”). They imagine it a

murder as one saint entombed another underneath that holy

chapel.

While Saint Oran’s name continues, Martyred heretic, his bones still hold the chapel stones

together, And we join them, kings and princes, in his graveyard, in

his chapel, For it’s Oran’s name they carry. He’s embraced in his

damnation by the simple words he uttered. There’s no Hell to spite

the sinners. There’s no Heaven for the blessed. God is not what you

imagine.

And perhaps he kept on preaching, for he’d died and he

had risen, Until silenced, crushed or muffled by the soil of Iona. Saint Columba, he was buried on the island of Iona Decades later. But they disinterred his body and they

took it to Downpatrick, where it’s buried with Saint Patrick and

Saint Brigid. So the only saint is Oran on the island of Iona. Don’t go digging in that graveyard for the kings of old,

the might, Or archbishops and their riches. They are guarded by

Saint Oran Who will rise up from the gravedirt like the darkness,

like an otter, For he sees the sun no longer. He will touch you, He will taste you, he will leave his words inside you. (God is not what you imagine. Nor is Hell and nor is

Heaven.)

Then you’ll leave him and his graveyard, and forget the

shadow’s terror, as you rub your neck, remember only this: He died to

save us. And that Saint Columba killed him on the island of Iona.
```

---

## IC-1603: In Remembrance - A Holocaust Collection

- Title: In Remembrance - A Holocaust Collection
- Author (byline): Elie Wiesel, William Heyen and Tawnysha Lynch
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1207
- Already set (do not supply): none

### Source block (context only)

```text
Author: Eli Wiesel
Book: Night, Pg 34
ISBN: 978-0374500016
Publisher: Hill and Wang
Date (Month/Year): Jan 2006
Author: William Heyen
Book: Erika: Poems of the Holocaust, Pgs 86-89; 39
ISBN: 978-1877770210
Publisher: Time Being Books
Date (Month/Year): June 1991
Author: Tawnysha Lynch
Book: Remembrance
ISBN: 978-1891231575
Publisher: Word Association Publishers
Date (Month/Year): 2001
Also On-line at
http://rihsenglish.pbworks.com/w/page/6787302/Poems
```

### Introduction (context only: never use it for content warnings)

```text
Through their poetry Never Shall I Forget by Elie Wiesel,
```

### Performance text (classify this)

```text
Never Shall I Forget by Eli Wiesel (Pg 34) Never shall I forget that night, the first night in camp, that

turned my life into one long night seven times sealed. Never shall I forget that smoke. Never shall I forget the small faces of the children whose

bodies I saw transformed into smoke under a silent sky. Never shall I forget those flames that consumed my faith

forever. Never shall I forget the nocturnal silence that deprived me

for all eternity of the desire to live. Never shall I forget those moments that murdered my God

and my soul and turned my dreams to ashes. Never shall I forget those things, even were I condemned to

live as long as God Himself. Never.

A Visit to Belzec and To the Onlookers by William Heyen and As the Orchestra Played by Tawnysha Lynch, shallow graves are unearthed and the tortured souls of six million who perished during the Holocaust are honored. In Remembrance – A Holocaust Collection

A Visit to Belzec by William Heyen (Pg 86-89)
I
This is Belzec,
in the East of Poland,
in the Lublin region
where the fumes of Sobibor,
Maidenek, and Treblinka still
stain the air:
smell the bodies
in the factories' smoke,
smell the sweet gas
in the clover and grass.
This is Belzec
where the death compound's gate
proclaims in Hebrew,
«Welcome to the Jewish State.»
This is Belzec.
This is SS humor.
Curse them forever
in their black Valhalla.
II
At 7:20 a.m. a train arrived from Lemberg with 45 wagons
holding more than 6,000 people. Of these, 1,450 were
already dead on arrival. Behind the small, barbed-wire
windows, children, young ones, frightened to death, women
and men. As the train drew in, 200 Ukrainians detailed for
the task tore open the doors and, laying about them with
their leather whips, drove the Jews out of the cars.
Instructions boomed from a loudspeaker, ordering them to
remove all clothing, artificial limbs, and spectacles. . .
They asked what was going to happen to them. . . Most of
them knew the truth. The odor told them what their fate
was to be. They walked up a small flight of steps and into
the death chambers, most of them without a word, thrust
forward by those behind them.
III
Listener, you have walked
into the smoke-streaked mirror
of my dream, but I can't,
or won't remember.
Did my jackboots gleam?
Did I fill out quotas?
Was it before, or after?
Did I close those doors,
or did I die?
I can still feel
iron and cold water on my fingers,
I remember running
along the bank of a river,
under trees with full summer
stars in their branches,
the sky lit up with flares
and the slight murderous arcs of tracers,
the night air wet
with the sugary odors of leaves.

Dogs barked. Were they mine? Were they yours? Was I running from, or after? IV Inside the chambers SS men were crushing the people together. `Fill them up well -- 700 or 800 of them to every 270 square feet.' Now the doors were closed. . . The bodies were tossed out, blue, wet with sweat and urine, the legs soiled with feces and menstrual blood. A couple of dozen workers checked the mouths of the dead, which they tore open with iron hooks. Other workers inspected anus and genital organs in search of money, diamonds, gold; dentists moved around hammering out gold teeth, bridges and crowns. . . V Listener, all words are a dream, You have wandered into mine. Now, as workers rummage among the corpses, we will leave for our affairs.

This happened only once, but happened:
one Belzec morning, a boy in deathline
composed a poem, and spoke it.
The words seemed true, and saved him.
The guard's mouth fell open to wonder.
We have walked together
into the smoke-streaked
terror of Belzec,
and have walked away.

Now wind, and the dawn sun,

lift our meeting to where they lift the human haze

above that region's pines.

To The Onlookers by William Heyen (Pg 39)

When our backs are turned,
when someone stares at us,
we feel them.
You who watched the killing, and did nothing,
still feel the eyes of those dead
on your bodies.

How many see you
as you pick a violet?
How many oak branches twist
into hands begging for help?
How many memories congeal
in the sun's evening blood?
O the unsung cradlesongs
in the dove's nightcries--
so many would have loved
their own stars in the night skies,
but now only the old well
can do it for them.
You did not murder,
but looked on, you,
who could have been changed
into light.

As the Orchestra Played by Tawnysha Lynch Summoned to Auschwitz’s doors, I could hear the violin’s mournful voice Calling to me as I entered history’s largest grave As the orchestra played.

When life’s selections took place,
I could hear the drum’s rhythmic pace
Chronicling our short life’s goodbye
As the orchestra played.

When I became a prisoner,
I could hear the clarinet’s fluid notes
Mocking at what I have become
As the orchestra played.

When I sorted through the evidence of martyrdom,
I could hear the guitar’s music
Allowing my mind to escape
As the orchestra played.

When beaten without reason,
I could hear the trumpet’s shout
Announcing each crippling blow
As the orchestra played.

When I dug graves for my brethren,
I could hear the bass’ low hum
Predicting the horror to come
As the orchestra played.

When train loads of people perished in gas chambers,
I could hear the bagpipe’s chilling song
Forever haunting their frozen, blackened faces
As the orchestra played.

When I saw massacred skeletons wither away in ovens,
I could hear the cello’s sorrowful tune
Lamenting a bitter cry
As the orchestra played.

When I struggled to survive,
I could hear the flute sing
Telling of my affliction
As the orchestra played.

When I was chosen to die,
I could hear the accordion’s melody
Foretelling my fate
As the orchestra played.

When my essence exhaled its last,
I could hear the harmonica
Proclaiming my life’s departure
As the orchestra played.

When my ashes drifted from the grave, I could hear the instruments join as one Bidding me farewell As the orchestra played.

(Echo from Never Shall I Forget)

Never shall I forget those things, even were I condemned to

live as long as God Himself.

Never.

CLOSING

But we must do more than just remember. Elie Weisel tried to explain in his Nobel Peace Prize speech in 1986: “When human lives are endangered, when human dignity is in jeopardy, national borders and sensitivities become irrelevant. Wherever men or women are persecuted because of their race, religion, or political views, that place must – at that moment – become the center of the universe.”

Can we stop the world from falling apart? Gaza, Sudan, Ukraine, Myanmar, Ethiopia, Haiti. The list of global conflicts grows longer; while here in the US we face our own divisions of race, religion and politics.

We must do more than just remember. Think higher, feel deeper, do more. Donate to a food bank, help your neighbor, volunteer, vote in all the elections. Be a part of the solution, not part of the problem.
```

---

## IC-1604: In Response to Columbine

- Title: In Response to Columbine
- Author (byline): Janet O’Neill
- Work: Turning Points
- Publisher: Tichenor Publishing
- Publication date as stated: 2001
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 810
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
“In Response to Columbine” by Janet O’Neill
```

### Performance text (classify this)

```text
The scene sets-up like this:

Shooters – up the hill

on their knees

guns cocked and ready.

Students -

exit from

south door. Downhill.

Teachers -
leading the students out to battle.
Pack leaders.
Coordinators.

Then
1 - the first shot
2 - the reaction
3 - the instinct to run away
4 - the frenzy for survival
5 - the aftermath

OK, let's run it
live in 5
4
3
2
1.

Where’s he at?
He promised to help me
make my car
For the pinewood derby.
We're gonna win this year.
Where's dad?

OK.
It's an open-and-shut case.
Kid opens fire in the cafeteria.
Two second graders get glazed.
One third grader takes it in the vitals.

Kid fleas the scene.
Has no escape plan.
Gets caught before he makes it to the ball diamond.
Motive?
Hell
We've got a cafeteria
filled with 246 witnesses.
We don't need motive.

Mommy
it's the new version.
The games so real it's
like you're actually there.
Can I have it?
Please?
I promise I'll be good.
If you get me this,
I won't be bored all summer.

It's like I don't
recognize her anymore.
She used to wear anything
GAP.
Now she wears anything
BLACK.
She comes home.
Goes to her room.

Types on the computer.
I've noticed
cuts on her
arm.
First
they were small.
Now they're larger.
Gashes
in her
arm.
She's punishing
herself
She's punishing
me.
She's punishing
anything she can.
She breaks things.
Anything.
Supposedly she
keeps a journal.
I haven't read it
I won't.
But I want to know.
Where's my daughter?
Why won't she come back?

For every action
there is an
equal
yet opposite
R
E
A
C
T
I
O
N
When it says here
"parents"
does that mean
my real parents
or the people I live
with?
Weekends, too?
Why can't I just
put grandma?
What if I don't know
their last name?
Can I leave it blank?
He's not really my dad.
He's like the guy
who lives with us, you know?
Can I leave it blank?

No, I'm not buying you
a rifle for Christmas!
Well we can't have
everything Timmy has
can we?
Can we?
You answer your mother
when she's talking to you.
We can't have
everything Timmy has
can we?
Can we?

See I keep the money
underneath my sock.
Deep down.
Then before lunch
I go to the bathroom
and dig it out.
No one else can get it.
They're always taking my money.
They don't even need it.
They just want to get a
R R R
E E E
A A A
C C C
T T T
I I I
O O O
N N N
out of me.

Tonight on "World's Toughest Men" a man who took 4 bullets and lived to tell the tale.

Today's topic:
Mothers who didn't
even know her child
was pregnant until she
brought home the baby.

Today - we celebrate with a five-gun salute.

She's started to pull away.
Even more.
I found these brochures
for a private school
in Vermont.
She's telling her
friends that's where she's
going.
Away.
She tells them.
She's going away.
If I read the diary. Just once
Would I find my daughter?
Would it be worth it
If
I
found my daughter?

For every action there is an
equal
yet opposite
R
E
A
C
T
I
O
N
I say we try the little f***er
as an adult.
Hell, I know he's only 13.
Little f***er knew.
He knew.

And he knew you'd be too
Chicken**** to call him
on it.
Boys school 'til he's 18.
He knew.
Little f***er knew.

Daddy's playing cards tonight
Daddy just got home. He'll play later.
Daddy's out betting on horses
Out on vacation
Out of town
Out shooting baskets
out at the shooting range.
Daddy can I go?

Daddy can I go?

(Opens diary) Sometimes
I want to tell mom
about it.
But
she thinks Al's a good guy.
He's not like dad
she says
He's not like dad.
He scares me.

I do what he tells me.
He says I better not
act like I'm asleep
and I don't
but I stay real quiet.
Real quiet.
Real quiet.
So mommy won't hear.
So mommy won't hear.
So mommy won't hear.
For every action
there is an
equal
yet opposite
R R R
E E E
A A A
C C C
T T T
I I I
O O O
N N N

Reaction to the shooting were mixed, as the families of the victims mourned the death of their children and the families of the perpetrators mourn the death of their children's souls. Next hour on Newsextra, we'll talk to the town rocked by the events of today. What triggered the attack? Next, on Newsextra. And we're out in 5 4 3 2 1.
```

---

## IC-1605: Instructions and Locks

- Title: Instructions and Locks
- Author (byline): Neil Gaiman
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1098
- Already set (do not supply): none

### Source block (context only)

```text
Author: Neil Gaiman
Book: A Wolf at the Door
ISBN: 978-0689821394
Publisher: Aladdin Paperbacks
Date (Month/Year): December 2001
Author: Neil Gaiman
Book: Silver Birch, Blood Moon
ISBN: 978-0380786220
Publisher: Eos
Date (Month/Year): March 1999
```

### Introduction (context only: never use it for content warnings)

```text
As adults we tend to forget that to children, everything is strange and wondrous; every step away from the familiar is fraught with peril and filled with potential dangers. Who knows for sure what lurks beneath the roses or what caused the bush in the deepest darkest corner of the garden to tremble? If the garden itself is filled with so many mysteries, what great adventures await should you choose to leave its safety? In the garden shelter is only a short sprint away, but out there in the world there will be no kitchen to replenish supplies when they run low or door to lock behind you when the sun expires and the shadows come alive. Instructions by Neil Gaiman are ones we'd all be wise to follow and remember, no matter what our age or experience.
```

### Performance text (classify this)

```text
Instructions
Touch the wooden gate in the wall you never
saw before.
Say "please" before you open the latch,
go through,
walk down the path.
A red metal imp hangs from the green-painted
front door,
as a knocker,
do not touch it; it will bite your fingers.
Walk through the house. Take nothing. Eat
nothing.
However, if any creature tells you that it hungers,
feed it.
If it tells you that it is dirty,
clean it.
If it cries to you that it hurts,
if you can,
ease its pain.

From the back garden you will be able to see the
wild wood.
The deep well you walk past leads to Winter's
realm;
there is another land at the bottom of it.
If you turn around here,
you can walk back, safely;
you will lose no face. I will think no less of you.

Once through the garden you will be in the
wood.
The trees are old. Eyes peer from the under-
growth.
Beneath a twisted oak sits an old woman. She
may ask for something;
give it to her. She
will point the way to the castle.
Inside it are three princesses.
Do not trust the youngest. Walk on.
In the clearing beyond the castle the twelve
months sit about a fire,
warming their feet, exchanging tales.
They may do favors for you, if you are polite.
You may pick strawberries in December's frost.
Trust the wolves, but do not tell them where
you are going.
The river can be crossed by the ferry. The ferry-
man will take you.
(The answer to his question is this:
If he hands the oar to his passenger, he will be free to
leave the boat.
Only tell him this from a safe distance.)

If an eagle gives you a feather, keep it safe. Remember: that giants sleep too soundly; that witches are often betrayed by their appetites; dragons have one soft spot, somewhere, always; hearts can be well-hidden, and you betray them with your tongue.

Do not be jealous of your sister.
Know that diamonds and roses
are as uncomfortable when they tumble from
one's lips as toads and frogs:
colder, too, and sharper, and they cut.

Remember your name. Do not lose hope — what you seek will be found. Trust ghosts. Trust those that you have helped to help you in their turn. Trust dreams.

Trust your heart, and trust your story.
When you come back, return the way you came.
Favors will be returned, debts will be repaid.
Do not forget your manners.
Do not look back.
Ride the wise eagle (you shall not fall).
Ride the silver fish (you will not drown).
Ride the grey wolf (hold tightly to his fur).

There is a worm at the heart of the tower; that is why it will not stand.

When you reach the little house, the place your
journey started,
you will recognize it, although it will seem
much smaller than you remember.
Walk up the path, and through the garden gate
you never saw before but once.
And then go home. Or make a home.
And rest.

TRANSITION Now that you know the secrets of successfully navigating the fairy tale world, or perhaps the “real” world – Oft times the line between the two can become blurred. I offer another selection by Neil Gaiman: Locks. You remember the tale of Goldilocks and the Three Bears, don’t you? The tale actually originated with Robert Southey, but in his original version, the main character is not a young girl, but a nameless, homeless and ill-tempered old woman who intentionally breaks into the bears’ home looking for food and shelter. In Locks, we find the speaker sharing this version with his young daughter and ruminating over the need for Locks – Golden or otherwise.

We owe it to each other to tell stories, as people simply, not as father and daughter. I tell it to you for the hundredth time:

"There was a little girl, called Goldilocks, for her hair was long and golden, and she was walking in the Wood and she saw — "

"— cows." You say it with certainty, remembering the strayed heifers we saw in the woods behind the house, last month.

"Well, yes, perhaps she saw cows, but also she saw a house."

"— a great big house," you tell me.

"No, a little house, all painted, neat and tidy."

"A great big house." You have the conviction of all two-year-olds. I wish I had such certitude.

"Ah. Yes. A great big house. And she went in . . ."

I remember, as I tell it, that the locks
Of Southey's heroine had silvered with age.
The Old Woman and the Three Bears . . .
Perhaps they had been golden once, when she was a
child.

And now, we are already up to the porridge,
"And it was too— "
"— hot!"
"And it was too— "
— cold!"
And then it was, we chorus, "just right."

The porridge is eaten, the baby's chair is shattered, Goldilocks goes upstairs, examines beds, and sleeps, unwisely.

But then the bears return.
Remembering Southey still, I do the voices:
Father Bear's gruff boom scares you, and you delight in
it.

When I was a small child and heard the tale,
if I was anyone I was Baby Bear,
my porridge eaten, and my chair destroyed,
my bed inhabited by some strange girl.

You giggle when I do the baby's wail,
"Someone's been eating my prridge, and they've eaten it
—"
"All up," you say. A response it is,
Or an amen.

The bears go upstairs hesitantly, their house now feels desecrated. They realize what locks are for. They reach the bedroom.

"Someone's been sleeping in my bed." And here I hesitate, echoes of old jokes, soft-core cartoons, crude headlines, in my head.

One day your mouth will curl at that line. A loss of interest, later, innocence.

Innocence; as if it were a commodity.
"And if I could," my father wrote to me,
huge as a bear himself, when I was younger,
"I would dower you with experience, without
experience."
and I, in my turn, would pass that on to you.
But we make our own mistakes. We sleep
unwisely.
It is our right. It is our madness and our glory.
The repetition echoes down the years.
When your children grow; when your dark locks begin to
silver,
when you are an old woman, alone with your three bears,
what will you see? What stories will you tell?

"And then Goldilicks jumped out of the window and she ran — Together, now: "All the way home."

And then you say, "Again. Again. Again."

We owe it to each other to tell stories.

These days my sympathy's with Father Bear. Before I leave my house I lock the door, and check each bed and chair on my return.

Again. Again. Again..
```

---

## IC-1606: Iraqi War Poetry

- Title: Iraqi War Poetry
- Author (byline): Various Authors
- Work: Poets Against the War
- Publisher: Nation Books
- Publication date as stated: April 2003
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 3608
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sam Hamill and Sally Anderson (editors)
Book: Poets Against the War
ISBN: 978-1560255390
Publisher: Nation Books
Date(Month/Year): April 2003
```

### Introduction (context only: never use it for content warnings)

```text
In late January 2003, in response to an invitation to a symposium by Laura Bush to celebrate "Poetry and the American Voice," Sam Hamill declined; a longtime pacifist, he could not in good faith visit the White House following the recent news of George W. Bush's plan for a unilateral "Shock and Awe" attack on Iraq. Instead, he asked about 50 fellow poets to "reconstitute a Poets Against the War movement like the one organized to speak out against the war in Vietnam...to speak up for the conscience of our country and lend your names to our petition against this war” by submitting poems of protest that he would send to the White House. 1,500 poets responded within four days . . . These are their heartfelt responses to the War in Iraq.
```

### Performance text (classify this)

```text
NOTE: This is way to long for one poetry presentation; but each poem is so incredible, it has been left up to the performer to pick and choose the items they’d like to include.

Afterward, We May Want to Know What Happened
by Ralph Angel
Amazing. We're all still here,
and everybody's talking at once.
But each moment works against us—we can't
hear everything—and gets us through the hour
in buses and taxis, airplanes
carving the sky, the slow shade of a cloud
that creeps through an open market with promises of
nighttime striking a deal with the daylight.

No. We can't see everything,
but when did looking convince us?
Now we don't want these flowers,
and we curse the vendor for showing them.
It's all regret, the fish on the ice,
the baskets of potatoes and green beans, all
regret, until regret too

is demolished. From the dust and rabble
steel skeletons stand in the grandeur of distance
and glass skin. And today, again,
we've hurried to Century City, but we arrive
forever early, unable to live up to our destination—
neither shades nor galoshes, but
the myth of afternoon.

Perhaps that's enough. Perhaps it's all true. These designs of ourselves, and the wind, somewhere else. Among corporate towers and modular dunes, among vacant, dazzling plazas we're all just here, and each voice is a tiny fissure in the earth's veneer. And each voice calls to us, calls in the spirit of a beggar with something to give.

GOOD CLEAN FUN by Diane di Prima

It's terrorism, isn't it, when you're afraid to answer the door for lack of a Green Card afraid to look for work, walk into the hospital when yr child is sick,

and what else than terrorism cd you call those smallpox blankets we gave the Indians the trail of tears, the raids on Ghost Dancing tribes It's terrorism when you're forbidden to speak yr language paddled for it, made to run a hundred laps in the snow in your thin & holey sneakers. What do you call it when you're locked in yr high school classroom, armed policemen manning the halls? Isn't it terrorism to force a young woman to talk to her parents abt her clandestine love the child she will or will not carry? Is it terrorism to shoot striking onion workers (1934), pick off AIM members one by one?

What happened to the Hampton family in Chicago his bed; would you call that terrorism? Or the MOVE kids in Philadelphia bombed in their home. Or all the stories we don't know buried in throats stuffed w/socks, or pierced w/bullets. Wd you call it terrorism, what happened at Wounded Knee or the Drug Wars picking off the youth of our cities twenty years ago now; you know the names. What was COINTELPRO if not terrorism? What new initials are they calling it today?

Is Leonard Peltier a victim of terrorism? Is Mumia Abu-Jamal?

Is it terrorism if you are terrified
of the INS, the IRS, the landlord, yr boss, the man
who might do yr job for less?
if you're scared of yr health insurance
no health insurance
scared of yr street, yr hallway, scared every month
you might not get to the 1st and the next measly check?

Is it terrorism to take food from hungry school-kids? To threaten teenagers who still have hope enough have joy enough to bring babies into this mess?

How has terrorism touched you, shaped your life? Are you afraid to go out, to walk in yr city, yr suburb, yr countryside? To read, to speak yr own language, wear yr tribe's clothes? Afraid of the thin-shelled birds w/twisted necks poisoned by nitrates, by selenium? Afraid that the dawn will be silent, the forests grey?

Is it terrorism to fill the Dnieper w/radiation?
or heat the ionosphere w/magnetism "to see what will
happen"?
A wonderful weapon, they say, it will perturb
the weather pattern, disrupt communications
Who are the terrorists in the lumber wars?
(the water wars are coming)
And we haven't even talked about AIDS and cancer.

Is the assault on native intelligence & good will that we call the evening news anything other than an act of terror?

What was the Gulf War but terrorism wearing the death mask of order? < one big car bomb it was the guys who drove it dying now one by one Is acid rain a form of terrorism? (Think for yourself.) Is GATT or NAFTA anything but a pact among brigands and their back-up men? How long before they fight over the spoils? Who'll do their fighting for them?

Is Alan Greenspan perhaps the biggest known & named of our terrorist leaders, here, nurtured here, trained here

the dark design of whose hearts makes
Hutu & Tutsi
Croat & Muslim & Serb
mere diversionary tactics before the onslaught

BULLETIN
by Diane di Prima
It is happening even as you read this page. By the time
you finish reading this it will be over.

She will have left the hotel and disappeared. He will have eaten the pills. That one will slip and crack her skull on the floor. That one will go out in a driveby shooting.

halfway around the world the bombs are dropping

As you read these words it is already too late. 200,000 children will have starved. One of them held the Jewel in his brain, another could cure plagues with her breath.

As you read this line one thousand have died of AIDS. They die alone hidden in furnished rooms. They die on the ground all over Africa.

halfway around the world the bombs are falling

Do not think to correct this by refusing to read. It happens as you put down the paper, head for the door. The ozone reaches the point of no-return

the butterflies bellyflop, the last firefly, etc. Do not think to correct this by reading.

The bombs burst the small skull of an Arab infant the silky black hair is stuck to your hands with brains. W/bits of blood. There is less shrieking than you would expect a soft silence. The silence of the poor, those who could not afford to leave. Drop flowers on them from yr mind, why don't you? "I guess we'll have to stay and take our chances."

They die so silently even as we speak

Black eyes of children seek eyes of the dying mother bricks fall dirt spurts like fountains in the streets. In the time you fill a cup they die of thirst.

In the time it takes to turn off the radio. Not past, not future

The huts are blazing now. South of Market a woman ODs with an elegant sigh. No more no less than is needed.

halfway around the world the bombs are dropping To the Forty-third President of the United States of America by William O'Daly Mr. President, our history speaks to us, the history of Chile and China, El Salvador and Nicaragua, Somalia, Puerto Rico— today, our solemn duty is to defy your willful aggression, to parse provocative words and habits, your heroic battle to distract us. Perhaps you think God will protect us from the religious zealots who sanctify your rule, from your opportunism and the race renewal, the investiture you have assumed because, as always, it is not yours. Let me ask an obvious question.

If we are to establish peace
and security for our nation, must we not do
everything in our power to end
the beginnings of war, must we not allow
our imaginations to craft a lasting peace?

Are not the children you would choose
to incinerate our own? We try on masks
to trick our isolated, frightened selves,
to propagate our sacred uncertainties
among the children of this blue planet,
a world we create and ruin every day.

Mr. President,
where do we walk, where may we sit down,
where can we work or rest, weep or pray,
what field does a man sunder and seed
in a country living only in memory, dying
every day at the hands of those who profess
to love her most? They say God loves America,
and that this “old bitch gone in the teeth” is
heaven on earth; in preemptive violence,
in obstinacy, in entitlements for the rich,
this murdered land, this, the people's
earth, is our reward for being right
no matter how wrong we are.

What “urge and rage” thrives in the American heart, that so many cheer this obsessive, unilateral madness?

Even through precise layers of glass, the TV peddling a thrilling efficiency, we cannot see them, the ghosts that inhabit our malnourished statistics, inhospitable closets, cold kitchens where we eat meat and raise goblets of wine to celebrate our belief that they are not like us. I want to spend more time with my daughter, my five-year-old, I want to see her, to know she is alive. It is her “evening of the morning,” she is just fine, though she implores me to tell her the “acommitation of naked truth.”

I imagine Iraqis, weakened by sanctions, spending time with their children. What do they play together, what makes them laugh, what crude medicine do parents spoon down fevered throats, when they too are roused from nightmares of fragile necklaces of bone, slung around the necks of American fighters whose hearts we camouflage?

Who will witness the small charred bodies floating in the Tigris, children writhing in pain, in smoking rubble, in the ruins of Bab al-Wastani or the Mirjan Mosque, severed limbs and glazed eyes that last night followed their favorite story by candlelight?

Mr. President, what does it mean when you say Saddam Hussein, Butcher of Baghdad, official liar, terrorizes himself? If he brings terror upon himself, will our dark angels exterminate him or his already wounded people; and would you answer Mr. Korb: What if Kuwait grew carrots, what if Iraq's main exports were chick peas and cotton shawls destined for American women longing for the exotic?

To be honest,
I have forgotten from what we must abstain,
yet we know how to prevent conception. “C'est la vie,”
you say, saddled up, ready to ride with your posse
across oil fields just like those in Texas.
It appears the one thing we cherish
more than petroleum or our children
is the greased machinery of destruction.

* Notes

1. “old bitch gone in the teeth”: Ezra Pound, from “Hugh Selwyn Mauberley”

2. “urge and rage”: Anne Frank, from The Diary of a Young Girl (1947; tr. 1952), entry for 3 May 1944

3. “evening of the morning”: Kyra Gray O'Daly

4. “acommitation of naked truth”: Kyra Gray O'Daly

5. Bab al-Wastani: the last remaining of the renowned gates of Baghdad

6. Mirjan Mosque: ancient mosque, completed in 1358

7. “If Kuwait grew carrots we wouldn't give a damn.”

Lawrence Korb, former U.S. assistant secretary of defense, on the motives for “Operation Desert Storm”

8. “The war on terror involves Saddam Hussein because of the nature of Saddam Hussein, the history of Saddam Hussein, and his willingness to terrorize himself.” George W. Bush

9. “C'est la vie” : “Either they are with us or not. Either one is fine. C'est la vie.” An aide to George W. Bush, quoting him

10. “I know some in Europe see me as a Texas cowboy with six-shooters at my side. But the truth is I prefer to ride with a posse.” One senior Bush aide, recalling President Bush's comment to Czech President Vaclav Havel in Prague (Fall 2002)

If There Were No Days, Where Would We Live
by Primus St. John
The heart line begins
on the thumbless side of the palm
traveling horizontally under the fingers,
when it is clear & deeply etched
you have deep emotions...
so the war is over, my love,
and we have killed enough of them,
torched their homes
trampled their fields
mutilated their arms
burned their legs
harvested their ears
and wore them like dark pearls
drove them crazy
made night a sure sign
of death
their schools, lost canyons
with nothing blowing through them
and an exact count of
dead mothers
dead fathers
dead children
and all that was given
taken away.
What do you do now
with the hunger
and the poverty glaring in their faces?
St. Teresa
would have probably kissed it,
but we were not saints
we were soldiers
hiding in the enemy's world.
How many times
must I be dipped into the water
to be a child again?

Portrait of George W. Bush as a Cowboy, or: America's Foreign Policy of Peace By Terry Tempest Williams (Warning: This is a rant and may not be good for your mental health)

Old myths die hard as they say in the American West, and perhaps no lie is as captivating as the romance of the American Cowboy. Talk about a sacred cow that lives on in Texas. What I want to know is how George W. Blue-blood Bush has spun his identity to the point where we believe him when he says his preference is “home on the range” rather than commander-in-chief.” Karl Rove, his trusty genius-in-residence, actually said, “Given the choice of Wall Street over Main Street, the President would choose Main Street every time.” Yup, he's just a regular ‘ole guy in a Stetson and levis who just happens to live in The White House.

He is a man who wears a Stetson and levis with a relentless appetite for war.. Yee-haw! Ride e'm cowboy, all the way to Iraq. Forgive me, but that's what it feels like every day in the USA, where conservative talk show host Rush Limbaugh tells his viewers to “relax, we'll get our war” as he called the anti-war demonstrations anti-American demonstrations fueled by communists and environmental wackos. Never mind that freedom of speech is a tenet of American democracy or that dissent is what this country was founded on in the first place. Bush and his conservative army of listeners wants blood, not ours, but theirs. And theirs is no longer Osama Bin Laden and Al-Qaeda, but rather Saddam Hussein and Iraqi dissidents who are a more stable target, not prone to hiding in caves or shape shifting. We want to show what we've got by way of military prowess, in case the world has forgotten.

Just the other day, Dan Rather exposed the latest military scheme called “Shock and Awe,” a strategy developed with the hopes it would “have this simultaneous effect rather like the nuclear weapons at Hiroshima, not taking days or weeks but minutes” to destroy the enemy. 300 to 400 cruise missiles would be deployed at once, more than the number launched during the entire 40 days of the first Gulf War. “The sheer size of this has never been seen before, never been contemplated before,” a Pentagon official said. “There will be not be a safe place in Baghdad,” “The horror and destruction will be so vast and fast it will inspire nothing but shock and awe.” Within minutes, blood-soaked handkerchiefs will be waving from the rubble begging for mercy, and then presto, the war will be over. Nice and neat, clap the dust off our hands. In and out, mission accomplished.

One lariat thrown around the neck of Saddam Hussein, and it's the end of the rodeo. George W. Bush will wave his white hat to the crowd as he takes a bow from the saddle of his fast-riding horse in the middle of the arena.

“Shock and awe.” Read all about it. Barrel riders secure the Iraqi oil for themselves in record time.

It is time to expose the myth of the American Cowboy for what it is, a lie designed to perpetuate the rugged loner who takes the law into his own hands.. It doesn't matter if in truth, he's just a hired hand of the people who pay him. Or that his real home is not on the range, but simply moving through with no sense of responsibility to the folks who live there. What matters is that he can speak in simple verse and smoke his Marlboro cigarettes with style at the same time he rides off into the sunset with his silver pistols lashed to his thighs as he feels his trustworthy horse between his legs. Bodies left behind or broken fences never mended don't trouble him. He is the perfect image for American individualism. Take what's yours and move on.

Of course we can “go it alone,” says George W. to the increasing world-wide opposition to war in Iraq. That's the American way. “You're either with us or against us.” As the president so eloquently said, “I don't do nuance.”

The cowboy president doesn't talk details, he just points his pistol in the general direction of fear and starts shooting off his rhetoric like those three quick bullets, “Axis of Evil,” that were heard around the world. North Korea flashes news of nuclear weapons and then it's our turn to reply that our missiles are bigger than their missiles and now it's no longer rodeo time, but Super Bowl Sunday, with the United States Cowboy on the starting line with George as quarterback, his arm cocked and ready for a military touchdown.

George W. Bush loves a good game. The problem is -- war is not a game. And for those of us who do not view this man as our legitimate president, how do we get his attention?

I used to think democracy was a good place to start, but since September 11, and the creation of the new Department of Homeland Security, our civil liberties are being whittled and eroded away. Our voices raised in question are discredited and quelled. Fear has replaced reason. Confrontation has overruled contemplation. Entitlement has replaced respect as we watch environmental laws slashed and sensitive wildlands ravaged for their oil and ancient trees in the name of national security. The "war on terror" is first being waged here at home.

To those of you living in Europe, we thank you for your leadership of resistance. We thank you for gathering in the hundreds of thousands in London, Florence, Madrid, and Paris, showing us what is possible and inspiring our own demonstrations. And our numbers in the anti-war movement in America are growing. We thank you for crying foul on what we Americans have only dared to think to ourselves until now. And we thank you for your prayers and we pray with you believing there is a "conservative compassion" that can stay the violence of war. What we are learning from you is that those with a memory of war on their own soil are the first to call for patience and pause...

Perhaps, it will continue to be this kind of pressure from countries with a memory of fascism and a history of empires that have risen and fallen, that in the end will remind our cowboy culture in America that the poster with burnt edges, “Wanted Dead or Alive,” has never translated well in international law. America right now, under the Bush Regime, has a very destructive, call it foreign, policy for peace.

What I fear in America right now is this: War is the body bag flown home with a nice note from the president that reads, “She served our country well in the fight for freedom.” War is also amnesia, so that in the grief of that moment, Americans will choose to believe him and find ourselves imprisoned by our own arrogance.

THE HEARTH by C. K. Williams

1.

Alone after the news on a bitter
evening in the country, sleet slashing
the stubbled fields, the river ice;
I keep stirring up the recalcitrant fire,
but when I throw my plastic coffee cup
in with new kindling it perches intact
on a log for a strangely long time,
as though uncertain what to do,

until, in a somehow reluctant, almost
creaturely way, it dents, collapses,
and decomposes to a dark slime
untwining itself on the stone hearth.

I once knew someone who was caught in a fire and made it sound something like that. He'd been loading a bomber and a napalm shell had gone off; flung from the flames,

at first he felt nothing, and thought he'd been spared, but then came the pain, then the hideous dark--he'd been blinded, and so badly charred he spent years

in recovery: agonizing debridements, grafts, learning to speak through a mouth without lips, to read Braille with fingers lavaed with scar, to not want to die--

Though that never happened. He swore, even years later, with a family, that if he were back there, this time allowed to put himself out of his misery, he would.

2.

There was dying here tonight, after
dusk, by the road: an owl,
eyes fixed and flared, breast
so winter-white he seemed to shine

a searchlight on himself, helicoptered
near a wire fence, then suddenly
banked, plunged, and vanished
into the swallowing dark with his prey.

Such an uncomplicated departure;
no detonation, nothing to mourn;
if the creature being torn from its life
made a sound, I didn't hear it.

But in truth I wasn't listening, I was thinking, as I often do these days, of war; I was thinking of my children, and their children, of the more than fear I feel for them,

and then of radar, rockets, shrapnel,
cities razed, soil poisoned
for a thousand generations; of suffering so vast
it nullifies everything else.

I stood in the wind in the raw cold
wondering how those with power over us
can effect such things, and by what
cynical reasoning pardon themselves.

The fire's ablaze now, its glow
on the windows takes the night even darker,
but it barely keeps the room warm.
I stoke it again, and crouch closer.
```

---

## IC-1607: Israeli-Palestinian Conflict (A Collection)

- Title: Israeli-Palestinian Conflict (A Collection)
- Author (byline): Elana Bell, Yehuda Amichai, Nadine
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 879
- Already set (do not supply): none

### Source block (context only)

```text
Author: Elana Bell
Book: Eyes, Stones
ISBN: 978-0807144640
Publisher: LSU Press
Date (Month/Year): April 2012
Author: Yehuda Amichai
Book: The Selected Poetry of Yehuda Amichai
ISBN: 978-0520205383
Publisher: University of California Press
Date (Month/Year): Oct 1996
Author: Nadine Murtaja
ISBN: On-line Transcript
Publisher: Aljazeera.com
Date (Month/Year): June 8 2021
https://www.aljazeera.com/features/2021/6/8/as-the-
bombs-fall-i-write-the-poets-of-gaza
Author: Naomi Shihab Nye
Book: Words Under the Words: Selected Poems
ISBN: 978-0933377295
Publisher: The Eighth Mountain Press
Date (Month/Year): Oct 1994
Author: Rabbi Tamara Cohen
ISBN: On-line Transcript
Publisher: Ritualwell.org
https://www.ritualwell.org/ritual/no-pain-my-pain
```

### Introduction (context only: never use it for content warnings)

```text
Poetry, by its nature, is a form of dialogue; an attempt to communicate. In the throes of the Palestinian-Israeli conflict that has lasted more than 70 years – in societies politically torn apart -- the need to communicate across political and cultural boundaries is particularly intense.

Spoken word poet Mohammed Moussa describes the reality of Gaza today: “life here is poetry blown into pieces and scattered all over the place. In the weddings, there’s poetry, in times of war, in the eyes of an old man sitting in front of his small shop, mourning the death of his child, in the flames of bombs falling . . . poetry blown to pieces.

if you do not look because it is not your village

it is still your village

The Israeli-Palestinian Conflict, a collection by Elana Bell,
```

### Performance text (classify this)

```text
Murtaja, Naomi Shihab Nye and Rabbi Tamara Cohen

Your Village by Elana Bell

Once in a village that is burning

because a village is always somewhere burning

And if you do not look because it is not your village

it is still your village

In that village is a hollow child

You drown when he looks at you with his black,

black eyes

And if you do not cry because he is not your child

he is still your child

Yehuda Amichai, Nadine Murtaja, Naomi Shihab Nye and Rabbi Tamara Cohen

The Diameter of a Bomb by Yehuda Amichai

The diameter of the bomb was thirty centimeters
and the diameter of its effective range about seven meters,
with four dead and eleven wounded.
And around these, in a larger circle
of pain and time, two hospitals are scattered
and one graveyard. But the young woman
who was buried in the city she came from,
at a distance of more than a hundred kilometers,
enlarges the circle considerably,
and the solitary man mourning her death
at the distant shores of a country far across the sea
includes the entire world in the circle.
And I won’t even mention the crying of orphans
that reaches up to the throne of God and
beyond, making a circle with no end and no God.

Untitled by Nadine Murtaja

There, on the other side, time changes, hours pass, and it gets darker, the sky takes off its dim dress, then the morning arrives,

But here where I live, and breathe, life wears its black dress

constantly, To mourn the labor of my land Which took a long time.

Here, the hanging clock, in my room is broken,
not only this one, everyone’s clock is broken here,
my mother keeps saying:
everyone is waiting for the elixir,
we’ve had it with the grief and agony,

in this holy land we sleep and wake up to the sound of
bombing and shooting
so the first light of day rises in the evening,
lighting up the sky with the blood of martyrs,
here death sleeps not far from us,
we all walk towards freedom, towards hope,
we walk on the shattered glass of our broken windows,
we walk on stones that once were a house, carrying stories

and secrets, we walk with the screams of children, and the groans of

mothers pulsating over and over in our ears.

Kindness by Naomi Shihab Nye

Before you know what kindness really is you must lose things, feel the future dissolve in a moment like salt in a weakened broth. What you held in your hand, what you counted and carefully saved, all this must go so you know how desolate the landscape can be between the regions of kindness. How you ride and ride thinking the bus will never stop, the passengers eating maize and chicken will stare out the window forever.

Before you learn the tender gravity of kindness
you must travel where the Indian in a white poncho
lies dead by the side of the road.
You must see how this could be you,
how he too was someone
who journeyed through the night with plans
and the simple breath that kept him alive.
Before you know kindness as the deepest thing inside,
you must know sorrow as the other deepest thing.
You must wake up with sorrow.
You must speak to it till your voice
catches the thread of all sorrows
and you see the size of the cloth.
Then it is only kindness that makes sense anymore,
only kindness that ties your shoes
and sends you out into the day to gaze at bread,
only kindness that raises its head
from the crowd of the world to say
It is I you have been looking for,
and then goes with you everywhere
like a shadow or a friend.

No Pain Like My Pain by Rabbi Tamara Cohen

"Look carefully and see if there could possibly be pain like my pain, like the one bestowed by You upon me."

No pain like my pain,
no exile like my exile,
No land my land,
No desolate city like my desolate city.
No heart like my own aching heart.
No fear like the fear of my people.
No genocide like our genocide.
No humanity like our humanity.
No right like our right.
No wrong like their wrong.
No rage like my rage.

No pain like my pain,
immediate and raw and righteous,
ancient and true and etched in our genes by history's
injustices.

Dear God, help us look,
look closer so that we may see
our children in their children,
their children in our own.

Help us look so that we may see You – in the bleary eyes of each orphan, each grieving childless mother, each masked and camouflaged fighter for his people's dignity.

Dear God, Divine Exiled and Crying One,
Loosen our claim to our own uniqueness.
Soften this hold on our exclusive right – to pain, to
compassion, to justice.

May your children, all of us unique and in Your image,
come to know the quiet truths of shared pain,
shared hope,
shared land,
shared humanity,
shared risk,
shared courage,
shared peace.

In Sh'Allah. Ken yehi Ratzon. May it be Your will. And may it be ours.
```

---

## IC-1608: It’s Called Kings

- Title: It’s Called Kings
- Author (byline): Susana Cabanas
- Work: Bum Rush the Page
- Publisher: Three Rivers Press
- Publication date as stated: Oct 2001
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 716
- Already set (do not supply): none

### Source block (context only)

```text
Author: Susana Cabanas
Book: Bum Rush the Page
ISBN: 978-0609808405
Publisher: Three Rivers Press
Date(Month/Year): Oct 2001
```

### Introduction (context only: never use it for content warnings)

```text
The Divine Right of Kings is a theory which argued that certain kings ruled because they were chosen by God to do so and that these kings were accountable to no person except God. The king ruled by virtue of God's authority; therefore he should be obeyed in all things. Furthermore, no group, whether they be nobles, or a parliament, or the people in the street, had a right to participate in this rule; to question or oppose the monarch was to rebel against God's purpose.

And although we don’t have a King in the U.S. today, we do have a president and too often it seems that this theory is unilaterally applied to our leaders. It’s enough to make anyone angry . . . It’s Called Kings by Susana Cabana.
```

### Performance text (classify this)

```text
I’m angry because I hate to be angry and because I hate to be angry I’m angry angry makes me smoke too much and drink too much and eat too much or not enough binge this and binge that saturate yourself in something or the other to forget the fact that I’m angry I’m angry because I don’t like who I am who I become when I’m angry I’m mean and vengeful and vile and acid and ulcers and high blood pressure and headaches and backaches and aches and aches and aches and my head aches when I think how much I ached when I’m angry and how constipated I get when I realize how much I ache because I am so angry I’m so angry I don’t want to wake up much less go to bed that’s how angry rage rage rage fear pain anger I’m angry because why can’t we all be the same not some have too much while others not enough of nothing to eat not enough of a house over our heads not enough of the pain in our hearts that makes us to angry angry angry because don’t tell me that that guy sleeping on a stoop down the stoop from where you live doesn’t make you angry or the $40 real live trees that smell so good when you go by a whisper in our minds of a time gone by a time when the wind smelled of the sea or of trees a clean clear smell no more long time gone by your need to get out of the city and how many of us get a chance to get out of the city rolling up our pennies those of us who still have any left you know you are poor when you have to count your pennies in America to get high to forget how angry you can get in America in the land of milk and honey brother kills brother for a woman for a life for a piece of the land we shoot each other up day after day after day we shoot each other up because we’re so angry we’re so angry we break things we throw things we beat we beat each other up even those we love we yell and scream and scream and scream and hurt and cry and cry and rage and scream and cry and want to kill and want to die because we want to kill ourselves most of all because we’re so angry one must get very angry to put on a white robe white being the color of virtue of grace and add a white hood covering up the rage from our face and go burn a white cross on somebody’s lawn because of their color or creed or else to put on a white robe and stand on a white altar covered with the most exquisite white cotton and lace and hold up a gold chalice filled with red blood in which we submerge a white wafer and eat and drink of another’s flesh and blood in the name of the Lord in the name of the Lord this is my land says the conqueror and kills and kills with ease and grace in the name of the Lord whose Lord is my Lord your Lord is my God your God is your God my God do I believe in the Lord and Dukes and Earls and Princes and Pearls and Lords and Knights of the round table around the table of the Lord of the round table who rules above all and tells all the knights who sit around the round table what to do when to jump where to live divine right of kings have divine rights and dukes and earls and princes and pearls and lords the lord of the land and the supreme commander of the armed forces of all the nations and the people the masses of people who believe in the lord homeless wanderers wandering wandering wandering nomads migrating roaming moving constantly moving running from the landlord constantly moving constantly moving because the landlord owns all the land constantly moving in the name of the lord constantly moving constantly moving I’m angry I’m angry I’m angry I’m so angry.
```

---

## IC-1609: Jeremy

- Title: Jeremy
- Author (byline): Leonard Feeney
- Work: Fish on Friday
- Publisher: Loreto Publications
- Publication date as stated: Aug 1999
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 326
- Already set (do not supply): none

### Source block (context only)

```text
Author: Leonard Feeney
Book: Fish on Friday
ISBN: 978-1930278004
Publisher: Loreto Publications
Date (Month/Year): Aug 1999
```

### Introduction (context only: never use it for content warnings)

```text
Let’s face it: Women have some inherent portion of the second “X” chromosome that makes it easier for them to remember special occasions . . . . Like birthdays, Valentine’s day and Yes, even anniversaries. The smaller and disfigured “Y” chromosome simply wasn’t designed for these amazing feats of memory. It’s really not the man’s fault – It’s genetic. In fact there are some things that men are better at than women . . . . I just can’t remember what they are right now *grin* Jeremy by Leonard Feeney.
```

### Performance text (classify this)

```text
Lucy said to Jeremy, “Jeremy!” Jeremy said to Lucy, “What?” “Don’t you remember what day today is? Surely you’ve not forgot? Didn’t you notice the special pudding, And the little blue vase of flowers? Whose anniversary is it, Jeremy?” Jeremy said to Lucy, “Ours.”

Lucy said to Jeremy, “Jeremy!” Jeremy said to Lucy, “What?” “I’ve been waiting till I’ve been weary Keeping your supper hot. All day long I’ve been so excited! Didn’t you like your tea?

How many years are we married, Jeremy?” Jeremy said to Lucy, “Three.”

Lucy said to Jeremy, “Jeremy!” Jeremy said to Lucy, “What?” “You seem dreadfully unromantic; Maybe we fuss a lot, But aren’t we still the same old lovers, Summer and winter through?

Tell me who was your sweetheart, Jeremy?” Jeremy said to Lucy, “You.”

Lucy said to Jeremy, “Jeremy!” Jeremy said to Lucy, “What?”

“Remember the first year we were married, Out in the garden plot? The moon was lovely, and you said I had Something as blue as skies. What did I have so pretty, Jeremy?” Jeremy said to Lucy, “Eyes.”

Lucy said to Jeremy, “Jeremy!” Jeremy said to Lucy, “What?” “Remember the winter we went to dances? Remember the gown I bought? We danced one night at the Grand Pavilion, And you wore an evening suit; And how did you say your wife looked, Jeremy?” Jeremy said to Lucy, “Cute.”

Lucy said to Jeremy, “Jeremy!” Jeremy said to Lucy, “What?” “Remember the time when we had birthdays, And wasn’t it nice you thought To buy me bows for my satin slippers, Because I had tiny feet!

And what did you have to call them, Jeremy?” Jeremy said to Lucy, “Sweet.”

Lucy said to Jeremy, “Jeremy!” Jeremy said to Lucy, “What?” “Remember the poems we read together, The Maiden of Camelot And the Knight who lived in a wondrous castle, Holding her hand in his? Didn’t they used to thrill us, Jeremy?” Jeremy said to Lucy, “Zzzzzz!”
```

---

## IC-1610: Jesse

- Title: Jesse
- Author (byline): Scott Woods
- Work: High Desert Voices
- Publisher: The Wordsmith Press
- Publication date as stated: 2006
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 501
- Already set (do not supply): none

### Source block (context only)

```text
Author: Scott Woods
Book: High Desert Voices
ISBN: 978-1893972834
Publisher: The Wordsmith Press
Date(Month/Year): 2006
```

### Introduction (context only: never use it for content warnings)

```text
Who is Jesus to you? Great question! Do you have a great answer? Let's face it, we are asked many questions each day. "Where do you go to school?" "What is your favorite flavor of ice cream?" "Uh, would you like fries with that?" You see, most of the questions we are asked each day don't have much of a permanent impact on our life or on our future. They usually deal with stuff that's not all that important. Scott Woods in his poem “Jesse” describes his personal relationship with Jesus in a way that may seem strange to some, but is undeniably personal. Jesse by Scott Woods.
```

### Performance text (classify this)

```text
Jesus's name was not Jesus. It was JESSE. And YES, he was just another Black boy with a white boy's name.

Every time we went to market, somebody would inevitably shout out "Jesse!" and Jesus and 12 white Roman kids would turn around. I ought to know: His house was up the street from mine, and we spent most of our respective childhoods this way: Jesse and me used to play Muslims and Indians when we were kids.

I'd wrap a rag around my head and he'd starve himself for a month. We'd spend hours trying to knock down the old sandals hanging from the

crosses in our neighborhood. He would heal the crips and convert the Blood. He always smelled like Jerusalem goat's meat pizza to me, but to Aaron he smelled like Dead Sea Salt Water Taffy and to Martha he smelled like something she couldn't place at the time,

but when we went out on our third anniversary,

two years after Jesse'd moved on,

I walked with her through the Garden of Gethsemane

and she stopped at a flower and said "Jesse used to smell like this"

and the "this" in question was white
oleander.
See, he smelled differently to everyone.
Whatever you liked, even if you didn't know it,
that's how he smelled.
You expect a little bit of occasional magic when
your best friend is
the Son of God.
He was the best man at my wedding,
gave a four word toast at the reception: "I love
you guys."
And he danced with my bride,

and we arm-wrestled into the night,

and he kept the party goin',

gracious one-touch bartender that he was. And I loved him – and love him – like a brother,

back when being a man's brother meant something,

And that book? That book you can kill nations over? That book you stood black men on to lynch? That book you swing at the heads of gays on parade?

That book doesn't give you HALF the magic tricks he used to do. But to you,

he's the rock star of the universe, he's God Bon Jovi

he's a gold necklace depicting his death, not his life. To me, he's larger than two lives stacked on top of one another, even

Ghandi's and Mother Theresa's

and I'm not here to debate with you about

whether or not he was a great man – you

wouldn't know greatness in this day and age

if the real Madonna came down out of

heaven and kissed Brittney Spears dead in

her mouth of COURSE he was a great man,

but you didn't know him. No matter how strongly you believe

you will always, at best, just know the way,

putting words in his quiet mouth,

never resting your hat upon a friendly hook at the

destination that is the truth. The truth is he smelled like Dead Sea Salt Water Taffy. The truth is he smelled like goat's meat pizza. The truth is Jesse smelled

like love.
```

---

## IC-1611: A Jubilee of People Dreaming

- Title: A Jubilee of People Dreaming
- Author (byline): Not specified
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 873
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mahogany L. Browne
Book: This is the Honey: An Anthology of Contemporary
Black Poets, Pg 47
ISBN: 978-0316417525
Publisher: Little, Brown and Company
Date (Month/Year): Jan 2024
Author: Margarita Engle
ISBN: 978-0544102293
Publisher: Clarion Books
Date (Month/Year): March 2015
Author: Carrie Newcomer
Book: Until Now: New Poems
ISBN: 978-1737533504
Publisher: Available Light Publishing
Date (Month/Year): August 2021
```

### Introduction (context only: never use it for content warnings)

```text
That’s the world I want to live in – “A jubilee of people dreaming wildly” – A world when someone says you can’t do it. You do it twice and take pictures!

This collection is dedicated to those who never accepted the word “can’t.” Did you know that Stphen King’s 1st novel was rejected by publishers 30 times? Oprah Winfrey was fired from her 1st TV job and Walt Disney was told he’d never make it because he lacked imagination and had no good ideas.

A Jubilee of People Dreaming Wildly with This is the Honey by Mahagony L. Browne, Drum Dream Girl by Margarita Engle and Liminality by Carrie Newcomer
```

### Performance text (classify this)

```text
Wildly with poems by Mahogany L. Browne, Margarita Engle and Carrie Newcomer

This is the Honey by Mahogany L. Browne

(Pg 47) There is no room on this planet for anything less

than a miracle We gather here today to revel in the rebellion of a silent

tongue Every day, we lean forward into the light of our brightest

designs

& cherish the sun Praise our hands & throats

each incantation, a jubilee of people dreaming wildly
Despite the dirt
beneath our feet
or the wind
pushing against
our greatest efforts

Soil creates things Art births change This is the honey

& doesn’t it taste like a promise? Where your heart is an accordion

& our laughter is a soundtrack

Friend, dance to this good song— look how it holds our names!

Each bone of our flesh-homes sings welcome

O look at the Gods dancing

as the rain reigns against a steely skyline

Where grandparents sit on the porch & nod at the

spectacle in awe of the perfection of their grandchildren’s faces Each small discovery unearthed in its own outpour Tomorrow our daughters will travel the world with each

poem

& our sons will design cities against the backdrops of

living museums

Yes! Our children will spin chalk until each equation

bursts a familial tree

Rooted in miraculous possibilities & alive

Drum Dream Girl

On an island of music
in a city of drumbeats
the drum dream girl
dreamed

of pounding tall conga drums tapping small bongó drums and boom boom booming with long, loud sticks on big, round, silvery moon-bright timbales.

But everyone
on the island of music
in the city of drumbeats
believed that only boys
should play drums

so the drum dream girl
had to keep dreaming
quiet
secret
drumbeat
dreams.

At outdoor cafés that looked like gardens
she heard drums played by men
but when she closed her eyes
she could also hear
her own imaginary
music.

When she walked under
wind-wavy palm trees
in a flower-bright park
she heard the whir of parrot wings
the clack of woodpecker beaks
the dancing tap
of her own footsteps
and the comforting pat
of her own
heartbeat.

At carnivals, she listened
to the rattling beat
of towering
dancers
on stilts

and the dragon clang of costumed drummers wearing huge masks.

At home, her fingertips
rolled out their own
dreamy drum rhythm
on tables and chairs…

and even though everyone kept reminding her that girls on the island of music have never played drums

the brave drum dream girl
dared to play
tall conga drums
small bongó drums
and big, round, silvery
moon-bright timbales.

Her hands seemed to fly
as they rippled
rapped
and pounded
all the rhythms
of her drum dreams.

Her big sisters were so excited that they invited her to join their new all-girl dance band

but their father said only boys should play drums.

So the drum dream girl
had to keep dreaming
and drumming
alone

until finally
her father offered
to find a music teacher
who could decide if her drums
deserved
to be heard.

The drum dream girl’s
teacher was amazed.
The girl knew so much
but he taught her more
and more
and more
and she practiced
and she practiced
and she practiced

until the teacher agreed
that she was ready
to play her small bongó drums
outdoors at a starlit café
that looked like a garden

where everyone who heard
her dream-bright music
sang
and danced
and decided
that girls should always
be allowed to play
drums

and both girls and boys should feel free to dream.

Liminality by Carrie Newcomer

So much of what we know
Lives just below the surface.
Half of a tree
Spreads out beneath our feet.
Living simultaneously in two worlds,
Each half informing and nurturing
The whole.
A tree is either and neither
But mostly both.

I am drawn to liminal spaces,
The half-tamed and unruly patch
Where the forest gives way
And my little garden begins.
Where water, air and light overlap
Becoming mist on the morning pond.

I like to sit on my porch steps, barn jacket and boots
In the last long exhale of the day,
When bats and birds loop in and then out,
One rising to work,
One readying for sleep.

And although the full moon calls the currents,
And the dark moon reminds me that my best
language
Has always emerged out of the silence,
It is in the waxing and waning
Where I most often live,
Neither here nor there,
But simply On the way.

There are endings and beginnings
One emerging out of the other.
But most days I travel in an ever present
And curious now.
A betwixt and between,
That is almost,
But not quite,
The beautiful,
But not yet.

I’ve been learning to live with what is,
More patient with the process,
To love what is becoming,
And the questions that keep returning.

I am learning to trust
The horizon I walk toward
Is an orientation
Not a destination
And that I will keep catching glimpses
Of something great and luminous
From the corner of my eye.

(softly – from Drum Dream Girl) feel free to keep dreaming quiet secret drumbeat dreams

(louder – from This is the Honey) Nod at the spectacle

(with unbridled joy - This is the Honey) Be a jubilee of people dreaming wildly
```

---

## IC-1612: Kidnap Poem and Poem for Aretha

- Title: Kidnap Poem and Poem for Aretha
- Author (byline): Nikki Giovanni
- Work: The Black Poets
- Publisher: Bantam Books
- Publication date as stated: April 1985
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 770
- Already set (do not supply): none

### Source block (context only)

```text
Author: Nikki Giovanni
Book: The Black Poets
ISBN: 978-0553275636
Publisher: Bantam Books
Date (Month/Year): April 1985
```

### Introduction (context only: never use it for content warnings)

```text
African-American women have contributed to music significantly over the last several decades. It is also significant to note that many African-American musicians succeeded at a time when blacks were still the recipients of discrimination in the United States.

An American songwriter, singer and pianist, Aretha Franklin (aka the Queen of Soul) is regarded at least by Rolling Stone magazine to be the greatest singer who ever lived. She became famous in the late 1960s with the hit song “Respect.” In Poem for Aretha, Nikki Giovanni pays her tribute and “respect” to this amazing woman and the other black musicians who forged new ground in the music industry. After all . . . it was Johann Paul Richter who said . . . “Music is the poetry of the air”
```

### Performance text (classify this)

```text
Kidnap Poem

ever been kidnapped
by a poet
if i were a poet
i’d kidnap you

put you in my phrases
and meter you to jones beach
or maybe coney island
or maybe just to my house

lyric you in lilacs
dash you in the rain
alliterate the beach
to complement my see
play the lyre for you
ode you with my love song
anything to win you
wrap you in the red Black green
show you off to mama

yeah if i were
a poet i’d kid
nap you
Poem for Aretha
Cause nobody deals with Aretha—a mother with four

children— having to hit the road
they always say "after she comes
home" but nobody ever says what it's like
to get on a plane for a three week tour
the elation of the first couple of audiences the good
feeling of exchange the running on the high
you get from singing good
and loud and long telling the world
what's on your mind.

then comes the eighth show on the sixth day the

beginning to smell like the plane or bus the if-you-forget-your-

toothbrush in-one-spot-you-can't-brush-until-the-second-show

the strangers pulling at you cause they love you but you having no love

to give back the singing the same songs night after night day after

day and if you read the gossip columns the rumors that your

husband is only after your fame the wondering if your children will be glad to see you and

maybe the not caring if they are scheming to get out of just one show and go just one place where some doe-

doe-dupaduke won't say "just sing one song, please"

mobody mentions how it feels to become a freak
because you have talent and how
no one gives a damn how you feel
but only cares that Aretha Franklin is here like maybe

that'll stop:

chickens from frying

eggs from being laid

crackers from hating

and if you say you're lonely or tired how they always just say "oh come off it" or "did you see how they loved you did you see huh did you?" which most likely has nothing to do with you anyway and i'm not saying Aretha shouldn't have talent and i'm

certainly
not saying she should quit
singing but as much as i love her i'd vote "yes" to her
doing four concerts a year and staying home or doing

whatever
she wants and making records cause it's a shame
the way we're killing her.
we eat up artists like there's going to be a famine at the

end of those three minutes when there are in fact an

abundance of talents just waiting let's put some of the giants away for a while and deal with them like

they have a life to lead

Aretha doesn't have to relive billie holiday's life doesn't

have to relive dinah washington's death but who will stop the pattern?

she's more important than her music—if they must be

separated— and they should be separated when she has to pass out

before
anyone recognizes she needs
a rest and i say i need
aretha's music
she is undoubtedly the one who put everyone on

notice. She revived johnny ace and remembered lil green

Aretha sings
"i say a little prayer" and dionne doesn't
want to hear it anymore
aretha sings "money won't change you"
but james can't sing "respect" the advent
of aretha pulled ray charles from marlboro country
and back into
the blues made nancy wilson
try one more time forced
dionne to make a choice (she opted for the movies)
and diana ross had to get an afro wig pushed every
Black singer into his Blackness and negro entertainers
into negroness you couldn't jive
when she said "you make me/feel" the blazers
had to reply "gotta let a man be/a man"
aretha said "when my soul was in the lost and found/you

came along to claim it" and joplin said "maybe" there has been no musician whom her very presence

hasn't affected when humphrey wanted her to campaign she

said
"woeman's only hueman"
and he pressured james brown
they removed otis cause the combination was too strong
the impressions had to say "lord have mercy/we're

moving on up" the Black songs started coming from the singers on

stage and the dancers
in the streets
aretha was the riot was the leader if she had said "come
let's do it" it would have been done
temptations say why don't we think about it

think about it

think about it
```

---

## IC-1613: Knock, Knock

- Title: Knock, Knock
- Author (byline): Daniel Beaty
- Work: Not specified
- Publisher: Little, Brown Books for Young Readers
- Publication date as stated: Dec 2013
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 538
- Already set (do not supply): none

### Source block (context only)

```text
Author: Daniel Beaty
ISBN: 978-0316209175
Publisher: Little, Brown Books for Young Readers
Date (Month/Year): Dec 2013
```

### Introduction (context only: never use it for content warnings)

```text
One in 28 children in the United States has a parent behind bars -- Among black children, one in nine. And while the media focuses on crime and the prison population, the children who must learn to cope without a parent often drop through the cracks of our society. They struggle to understand – they struggle to succeed. Daniel Beaty lost contact with his father at the age of three but even 20 years later, the pain of the loss, the love for his father and his unrelenting hope for the future shines through in his poem

Knock, Knock by Daniel Beaty
```

### Performance text (classify this)

```text
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
on this never ending highway 'til we reach a place of high
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
```

---

## IC-1614: Kong

- Title: Kong
- Author (byline): Pamela Sneed
- Work: The Best American Short Plays 2005-2006
- Publisher: Applause Books
- Publication date as stated: Dec 2008
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1278
- Already set (do not supply): none

### Source block (context only)

```text
Author: Pamela Sneed
Book: The Best American Short Plays 2005-2006
ISBN: 978-1557837141
Publisher: Applause Books
Date (Month/Year): Dec 2008
```

### Introduction (context only: never use it for content warnings)

```text
Kong by Pamela Sneed tackles the current political landscape of war in Iraq, the crisis in New Orleans, the lack of American healthcare, gay and lesbian issues, and finally the need for new kinds of activism. Sneed’s poem never loses sight of her aim: to offer a work that is transformative, intellectual, emotional, and spiritual. At its heart, Kong is a resilient protest work, and a luminescent and universal call for freedom. Kong by Pamela Sneed.
```

### Performance text (classify this)

```text
I want to talk about that last Star Wars movie which
they promised was a final installment
But we'll see
all I can say is it really sucked except for the part near
the end
where you see the transformation of Luke Skywalker
into the evil Darth Vader
His innocence destroyed
crawling through some molten lava-limbless
He looked like a soldier
or something out of a war movie one of those battered
survivors
who has left his child self behind him
But, I earnestly believed
And now all I can do is carry myself/battle scarred to
some semblance of safety
All I can do is hold on like a survivor of the tsunami tidal
wave
Hold on to a tree, a pipe, anything, my papers from an
old life
verifying who I am
wait for the storm to pass
a shoulder to lean on/anything
But I earnestly believed.
You know when I left my parents house the small town
for a big city
and experienced all accoutrements of a counter culture
I earnestly believed
queer boys
queer nations
nose rings
dread locks
muscle shirts on girls
punk rockers
were all some semblance of an alternative
I believed poet Glen James
who called us the sissified warriors
I believed when Marlon Riggs premiered the ground
breaking film for Black Gay Men, Tongues Untied.
I believed Audre Lorde when she said in synopsis if we
don't do our work
One day women's blood will congeal upon a dead planet.
I believed poet Assoto Saint in all 6ft 4 of his cross
dressing self
I believed when he stood up at the funeral of Donald
Woods
and said in essence we must tell the truth about who we
really are.
I believed Black lesbian writer Pat Parker when she
declared
straights are OK, but why must they be so blatant
I earnestly believed when my child eyes almost twenty
years ago
first saw bisexual poet June Jordan
and the first thing she said was this country needs a
revolution.
I believed in Nelson and Winnie premiering even at the
height of apartheid with their fists
and heads held high
I believed even after they found Angel my student at
Hetrick Martin murdered
a handsome boy chopped into pieces
Yeah when they were still pulling queers out of the river
there downtown
Dead from queer bashings and suicide
I kept on believing change was possible.
I read the literature
had hope
I lived in America after all.
I earnestly believed.
You know this is an aside but
I'm tired of the previews for that latest King Kong
movie
Tired of all the actors looking to the sky with that same
perplexed look,
That over the top awesome
because King Kong is computer generated they can't see
him
so they're really acting
and you know King is a thin veil for a Black man
America assuaging it's racial fears.
Still, I'll pay ten, or twelve or twenty with popcorn to
see it.
There was a time too when I earnestly believed in
theatre
in performance
Believed I'd be a great big overnight success
that courage, innovation, tenacity would be recognized. I
earnestly believed
And I know there are those who will say I'm bitter
mislabel me
say I spew hatred
am raining down on their parade
That I lack optimism
when I try to say there is another America
when I try to say things are not equal
when I try telling them there are crimes being carried
out with doctors
many of them are modern criminals
who don't deserve white coats
There's another final solution that's occurring right
under our noses
and it's gonna get tougher and tougher
and tougher and tougher to hide the bodies
I earnestly believed
Saddam Hussein has been tried and convicted
but maybe it’s just my secret silly wish
I keep wanting them to try George Bush
I keep wanting those feared 30,000 Iraqi soldiers dead
I want their bodies to rise up
walk to the White House
speak against this senseless war
For them to matter
to someone besides their mothers
I want to see something like the truth and
reconciliation
hearings after apartheid
where this country must admit to committing atrocities
I want those millions of Americans living without health
care after working an entire lifetime ...
I want seniors who can't afford their prescriptions
I want my parents to go
I want America's poor
ones who know about when hospitals and doctors pull the
plug on those who can't pay
I want the family of that little Black girl in New Orleans
whose body was found floating facedown
still wearing pink short shorts and a pink squeegee in
hear hair.
Again, in New Orleans, I want the son whose mother
died during the floods
waiting for governmental help,
I want everyone to see the eyes of my student,
a black girl whose family is from the Ninth Ward in New
Orleans and how she looked the day in class when she
said
they won't give us back our houses
want everyone to hear my friend when she said Bush
got up in the middle of the night to sign papers to help
Terry Schivo but did nothing to help the people of New
Orleans
I want every year for those gays and lesbians in New
York during Gay Pride
to stop dancing on the piers and form a political
movement I want all those voiceless people we're turning
our
backs on
right now in the Darfur region of Africa to speak
And thank you Oprah, Thank you Bono, Thank you Jon
Bon Jovi for your generous donations
but the system has to change
Yes, there was a time when I earnestly believed
People get so defensive when I try telling them what's
happening systemically
when I say under this regime censorship has increased.
Artists no longer have spaces to work
nor money
and it's not just all about personal will pulling oneself up
by a bootstrap
There is marginalization and silencing
occurring across the board more than in other eras
perhaps this is a return to.
I honestly believed once that there were people more
enlightened
that competition and jealousy couldn't destroy our
world.
I believed helping a neighbor was more important than
money
I earnestly believed
Yes, by now I'm probably like someone in a horror film
who gets killed off easy
wasn't careful enough
Kept running toward instead of away
from the monster
The one who stayed in haunted house
you know who goes into an attic or a basement to
investigate what's going on
when they should have been long gone, the one who stays
in an abusive cycle
believes the partner will change
The one who hasn't read all the signals walks into a
thieves den
like on the old 42nd St.
with money hanging out of their pockets.
I earnestly believed like Anne Frank in human good.
I believed the slogans I read in kindergarten
that policemen help you across the street
will return lost children to their parents.
Maybe I'm as naive as MLK
when he said he had a dream of what America could
become
Maybe he isn't here to witness
just how tough things have become
Integration is now only a small step or small slice of
what we need.
Yesterday I sat down in the sun
and let it beam across my face
I prayed like Martin Luther King I could live one day in
freedom
One day not racked by pain or injustice.
I felt like Harriet who lived in slavery
Just one day wanting to feel freedom's kiss
And caress.
```

---

## IC-1615: Last Days

- Title: Last Days
- Author (byline): Donald Hall
- Work: Inventions of Farewell (ed Sandra Gilbert)
- Publisher: WW Norton & Co
- Publication date as stated: April 2001
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 725
- Already set (do not supply): none

### Source block (context only)

```text
Author: Donald Hall
Book: Inventions of Farewell (ed Sandra Gilbert)
ISBN: 978-0393049725
Publisher: WW Norton & Co
Date (Month/Year): April 2001
```

### Introduction (context only: never use it for content warnings)

```text
In 1994, Jane Kenyon was diagnosed with leukemia. She and her husband opted for a harrowing bone marrow transplant rather than other less aggressive treatments. It was not successful, and 12 weeks later, Jane was dead. The following describes the moment of her dying in a way that makes one believe that the ultimate experience of intimacy is to watch your loved one die . . . to be the one to close her eyes. Last Days by Jane’s husband, Donald Hall.
```

### Performance text (classify this)

```text
“It was reasonable
to expect.” So he wrote. The next day,
in a consultation room,
Jane's hematologist Letha Mills sat down,
stiff, her assistant
standing with her back to the door.
"I have terrible news,"
Letha told them. “The leukemia is back.
There's nothing to do.”
The four of them wept. He asked how long,
why did it happen now?
Jane asked only: “Can I die at home?”
Home that afternoon,
they threw her medicines into the trash.
Jane vomited. He wailed
while she remained dry-eyed – silent,
trying to let go. At night
he picked up the telephone to make
calls that brought
a child or a friend into the horror.
The next morning,
they worked choosing among her poems
for Otherwise, picked
hymns for her funeral, and supplied each
other words as they wrote
and revised her obituary. The day after,
with more work to do
on her book, he saw how weak she felt,
and said maybe not now; maybe
later. Jane shook her head: “Now,” she said.
“We have to finish it now.”

Later, as she slid exhausted into sleep,
she said, “Wasn't that fun?
To work together? Wasn't that fun?”
He asked her, “What clothes
should we dress you in, when we bury you?”
“I hadn't thought,” she said.
“I wondered about the white salwar
kameez,” he said –
her favorite Indian silk they bought
in Pondicherry a year
and a half before, which she wore for best
or prettiest afterward.
She smiled. “Yes. Excellent,” she said.
He didn't tell her
that a year earlier, dreaming awake,
he had seen her
in the coffin in her white salwar kameez.
Still, he couldn't stop
planning. That night he broke out with,
“When Gus dies I'll
have him cremated and scatter his ashes
on your grave!” She laughed
and her big eyes quickened and she nodded:
“It will be good
for the daffodils.” She lay pallid back
on the flowered pillow:
“Perkins, how do you think of these things?”
They talked about their
adventures – driving through England
when they first married,
and excursions to China and India.
Also they remembered
ordinary days – pond summers, working
on poems together,
walking the dog, reading Chekhov
aloud. When he praised
thousands of afternoon assignations
that carried them into
bliss and repose on this painted bed,
Jane burst into tears
and cried, “No more ***. No more ****!”

Incontinent three nights
before she died, Jane needed lifting
onto the commode.
He wiped her and helped her back into bed.
At five he fed the dog
and returned to find her across the room,
sitting in a straight chair.
When she couldn't stand, how could she walk?
He feared she would fall
and called for an ambulance to the hospital,
but when he told Jane,
her mouth twisted down and tears started.
“Do we have to?” He canceled.
Jane said, “Perkins, be with me when I die.”
“Dying is simple,” she said.
“What's worst is… the separation.”
When she no longer spoke,
they lay along together, touching,
and she fixed on him
her beautiful enormous round brown eyes,
shining, unblinking,
and passionate with love and dread.
One by one they came,
the oldest and dearest, to say goodbye
to this friend of the heart.
At first she said their names, wept, and touched;
then she smiled; then
turned one mouth-corner up. On the last day
she stared silent goodbyes
with her hands curled and her eye stuck open.
Leaving his place beside her,
where her eyes stared, he told her,
“I'll put these letters
in the box.” She had not spoken
for three hours, and now Jane said
her last words: “O.K.”
At eight that night,
her eyes open as they stayed
until she died, brain-stem breathing
started, he bent to kiss
her pale cool lips again, and felt them
one last time gather
and purse and peck to kiss him back.
In the last hours, she kept
her forearms raised with pale fingers clenched
at cheek level, like
the goddess figurine over the bathroom sink.
Sometimes her right fist flicked
or spasmed toward her face. For twelve hours
until she died, he kept
scratching Jane Kenyon's big bony nose.
A sharp, almost sweet
smell began to rise from her open mouth.
He watched her chest go still.
With his thumb he closed her round brown eyes.
```

---

## IC-1616: Let My People Go

- Title: Let My People Go
- Author (byline): James Weldon Johnson
- Work: God’s Trombones
- Publisher: Penguin Books
- Publication date as stated: Feb 1990
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1271
- Already set (do not supply): none

### Source block (context only)

```text
Author: James Weldon Johnson
Book: God’s Trombones
ISBN: 978-0140184037
Publisher: Penguin Books
Date(Month/Year): Feb 1990
```

### Introduction (context only: never use it for content warnings)

```text
Estimates suggest that almost 900 million people have died in religious conflicts throughout history, with many more suffering a vast array of abuses in the name of God.

In the Book of Exodus, God tells Moses to go to Pharaoh, to demand: “Let my people go.” The plea is insufficient. Pharaoh is an evil man, wielding murderous power. In the end, however, neither his wickedness nor his troops are any match for the rower of God. Pharaoh is defeated, at a terrible human price, and peace comes to the Children of Israel.

Today, our Armed Forces battle in Iraq, because words failed to stop Saddam Hussein from his own mad murderousness. Let us pray that, when all is done, we will view the invasion of Iraq as an act of peace not war. Let My People Go by James Weldon Johnson.
```

### Performance text (classify this)

```text
And God called Moses from the burning bush,
He called in a still, small voice,
And he said: Moses - Moses
And Moses listened,
And he answered and said:
Lord, here am I.
And the voice in the bush said: Moses,
Draw not nigh, take off your shoes,
For you're standing on holy ground.
And Moses stopped where he stood,
And Moses took off his shoes,
And Moses looked at the burning bush,
And he heard the voice,
But he saw no man.

Then God again spoke to Moses,
And he spoke in a voice of thunder:
I am the Lord God Almighty,
I am the God of thy fathers,
I am the God of Abraham,
Of Isaac and of Jacob.
And Moses hid his face.
And God said to Moses:
I've seen the awful suffering
Of my people down in Egypt.

I've watched their hard oppressors,
Their overseers and drivers;
The groans of my people have filled my ears
And I can't stand it no longer;
So I'm come down to deliver them
Out of the land of Egypt,
And I will bring them out of that land
Into the land of Canaan;
Therefore, Moses, go down,
Go down into Egypt,
And tell Old Pharaoh
To let my people go.
And Moses said: Lord, who am I
To make a speech before Pharaoh?
For, Lord, you know I'm slow of tongue.
But God said: I will be thy mouth and
I will be thy tongue;
Therefore, Moses, go down,
Go down yonder into Egypt land,

And tell Old Pharaoh
To let my people go.
And Moses with his rod in hand
Went down and said to Pharaoh:
Thus saith the Lord God of Israel,
Let my people go.
And Pharaoh looked at Moses,
He stopped still and looked at Moses
And he said to Moses: Who is this Lord?
I know all the gods of Egypt,
But I know no God of Israel
So go back, Moses, and tell your God,
I will not let this people go.
Poor Old Pharaoh,
He knows all the knowledge of Egypt,
Yet never knew
He never knew
The one and the living God.
Poor Old Pharaoh,
He's got all the power of Egypt,
And he's going to try
To test his strength
With the might of the great Jehovah,
With the might of the Lord God of Hosts,
The Lord mighty in battle.
And God, sitting high up in his heaven,
Laughed at poor Old Pharaoh.
And Pharaoh called the overseers,
And Pharaoh called the drivers,
And he said: Put heavier burdens still
On the backs of the Hebrew Children.
Then the people chode with Moses,
And they cried out: Look here, Moses,
You've been to Pharaoh, but look and see
What Pharaoh's done to us now.
And Moses was troubled in mind.
But God said: Go again, Moses,
You and your brother, Aaron,
And say once more to Pharaoh,
Thus saith the Lord God of the Hebrews,
Let my people go.
And Moses and Aaron with their rods in hand
Worked many signs and wonders.

But Pharaoh called for his magic men, And they worked wonders, too. So Pharaohs' heart was hardened, And he would not, No, he would not Let God's people go. And God rained down plagues on Egypt, Plagues of frogs and lice and locusts, Plagues of blood and boils and darkness, And other plagues besides. But ev'ry time God moved the plague Old Pharaoh's heart was hardened, And he would not,

No, he would not Let God's people go. And Moses was troubled in mind. Then the Lord said: Listen, Moses, The God of Israel will not be mocked, Just one more witness of my power I'll give hard-hearted Pharaoh.

This very night about midnight,
I'll pass over Egypt land,
In my righteous wrath will I pass over,
And smite their first-born dead.
And God that night passed over.
And a cry went up out of Egypt.
And Pharaoh rose in the middle of the night
And he sent in a hurry for Moses;
And he said: Go forth from among my people,
You and all the Hebrew Children;
Take your goods and take your flocks,
And get away from the land of Egypt.
And, right then, Moses led them out,
With all their goods and all their flocks;
And God went on before,
A guiding pillar of cloud by day,
And a pillar of fire by night.
And they journeyed on in the wilderness,
And came down to the Red Sea.

In the morning,
Oh, in the morning,
They missed the Hebrew Children.
Four hundred years,
Four hundred years
They'd held them down in Egypt land.
Held them under the driver's lash,
Working without money and without price.
And it might have been Pharaoh's wife that said:
Pharaoh -look what you've done.
You let those Hebrew Children go,
And who's going to serve us now?
Who's going to make our bricks and mortar?
Who's going to plant and plow our corn?
Who's going to get up in the chill of the morning?
And who's going to work in the blazing sun?
Pharaoh, tell me that!
And Pharaoh called his generals,
And the generals called the captains,
And the captains called the soldiers.
And they hitched up all the chariots,
Six hundred chosen chariots of war,
And twenty-four hundred horses.
And the chariots all were full of men,
With swords and shields
And shiny spears
And battle bows and arrows.
And Pharaoh and his army
Pursued the Hebrew Children
To the edge of the Red Sea.

Now, the Children of Israel, looking back,
Saw Pharaoh's army coming.
And the rumble of the chariots was like a thunder
storm,
And the whirring of the wheels was like a rushing wind,
And the dust from the horses made a cloud that darked
the day,
And the glittering of the spears was like lightnings in
the night.
And the Children of Israel all lost faith,
The children of Israel all lost hope;
Deep Red Sea in front of them
And Pharaoh's host behind.
And they mumbled and grumbled among themselves:
Were there no graves in Egypt?
And they wailed aloud to Moses and said:
Slavery in Egypt was better than to come
To die here in this wilderness.
But Moses said:
Stand still! Stand still I
And see the Lord's salvation.
For the Lord God of Israel
Will not forsake his people.
The Lord will break the chariots,
The Lord will break the horsemen,
He'll break great Egypt's sword and shield,
The battle bows and arrows;
This day he'll make proud Pharaoh know
Who is the God of Israel.

And Moses lifted up his rod
Over the Red Sea
And God with a blast of his nostrils
Blew the waters apart,
And the waves rolled back and stood up in a pile,
And left a path through the middle of the sea
Dry as the sands of the desert.
And the Children of Israel all crossed over
On to the other side.
When Pharaoh saw them crossing dry,
He dashed on in behind them
Old Pharaoh got about half way cross,
And God unlashed the waters,
And the waves rushed back together,
And Pharaoh and all his army got lost,
And all his host got drownded.
And Moses sang and Miriam danced,
And the people shouted for joy,
And God led the Hebrew Children on
Till they reached the promised land.
Listen 1- Listen 1
All you sons of Pharaoh.
Who do you think can hold God's people
When the Lord God himself has said,
Let my people go?
```

---

## IC-1617: The Life of Lincoln West

- Title: The Life of Lincoln West
- Author (byline): Gwendolyn Brooks
- Work: The Forerunners: Black Poets in America
- Publisher: Howard University Press
- Publication date as stated: Sept 1981
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 800
- Already set (do not supply): none

### Source block (context only)

```text
Author: Gwendolyn Brooks
Book: The Forerunners: Black Poets in America
ISBN: 978-0882580937
Date (Month/Year): Sept 1981
Publisher: Howard University Press
```

### Introduction (context only: never use it for content warnings)

```text
“I have a dream that my four little children will one day live in a nation where they will not be judged by the color of their skin but by the content of their character,” Martin Luther King told the masses in Washington D.C. in 1963.

Many today celebrate that Barack Obama is the first black — or should we say African-American — president of the United States. Some others say he isn’t really the first black president, but instead the first “president of color,” because he is, in fact, bi-racial, borne of a white mother and black father. Others argue that if it were 1955, there’s little question as to which water fountain he would be allowed to drink from, or where he would be allowed to sit on a Montgomery city bus.

Gwendolyn Brooks, a powerful voice of black consciousness and social protest in mid-century America, is among the most distinguished African-American poets of the twentieth century. Out of the loving security of her home, Brooks experienced racial prejudice in grade school, where other black students ridiculed her for her dark skin and lack of social or athletic abilities. She addressed this pervasive judgment of others in The Life of Lincoln West; and through her words we realize that King’s dream in many ways is still, in the words of Langston Hughes . . . “a dream deferred.”
```

### Performance text (classify this)

```text
Ugliest little boy that everyone ever saw. That is what everyone said.

Even to his mother it was apparent—
when the blue-aproned nurse came into the
northeast end of the maternity ward
bearing his squeals and plump bottom
looped up in a scant receiving blanket,
bending, to pass the bundle carefully
into the waiting mother-hands—that this
was no cute little ugliness, no sly baby waywardness
that was going to inch away
as would baby fat, baby curl, and
baby spot-rash. The pendulous lip, the
branching ears, the eyes so wide and wild,
the vague unvibrant brown of the skin,
and, most disturbing, the great head.
These components of That Look bespoke
the sure fibre. The deep grain.

His father could not bear the sight of him. His mother high-piled her pretty dyed hair and put him among her hairpins and sweethearts, dance slippers, torn paper roses. He was not less than these, he was not more.

As the little Lincoln grew,
uglily upward and out, he began
to understand that something was
wrong. His little ways of trying
to please his father, the bringing
of matches, the jumping aside at
warning sound of oh-so-large and
rushing stride, the smile that gave
and gave and gave—Unsuccessful!

Even Christmases and Easters were spoiled.
He would be sitting at the
family feasting table, really
delighting in the displays of mashed potatoes
and the rich golden
fat-crust of the ham or the festive
fowl, when he would look up and find
somebody feeling indignant about him.

What a pity what a pity. No love
for one so loving. The little Lincoln
loved Everybody. Ants. The changing
caterpillar. His much-missing mother.
His kindergarten teacher.

His kindergarten teacher—whose concern for him was composed of one part sympathy and two parts repulsion. The others ran up with their little drawings. He ran up with his. She tried to be as pleasant with him as with others, but it was difficult. For she was all pretty! all daintiness, all tiny vanilla, with blue eyes and fluffy sun-hair. One afternoon she saw him in the hall looking bleak against the wall. It was strange because the bell had long since rung and no other child was in sight. Pity flooded her. She buttoned her gloves and suggested cheerfully that she walk him home. She started out bravely, holding him by the hand. But she had not walked far before she regretted it. The little monkey. Must everyone look? And clutching her hand like that. . . . Literally pinching it. . . .

At seven, the little Lincoln loved
the brother and sister who
moved next door. Handsome. Well-
dressed. Charitable, often, to him. They
enjoyed him because he was
resourceful, made up
games, told stories. But when
their More Acceptable friends came they turned
their handsome backs on him. He
hated himself for his feeling
of well-being when with them despite—
Everything.

He spent much time looking at himself
in mirrors. What could be done?
But there was no
shrinking his head. There was no
binding his ears.

“Don’t touch me!” cried the little fairy-like being in the playground.

Her name was Nerissa. The many
children were playing tag, but when
he caught her, she recoiled, jerked free
and ran. It was like all the
rainbow that ever was, going off
forever, all, all the sparklings in
the sunset west.

One day, while he was yet seven,
a thing happened. In the down-town movies
with his mother a white
man in the seat beside him whispered
loudly to a companion, and pointed at
the little Linc.
“THERE! That’s the kind I’ve been wanting
to show you! One of the best
examples of the specie. Not like
those diluted Negroes you see so much of on
the streets these days, but the
real thing.

Black, ugly, and odd. You
can see the savagery. The blunt
blankness. That is the real
thing.”

His mother—her hair had never looked so
red around the dark brown
velvet of her face—jumped up,
shrieked “Go to—” She did not finish.
She yanked to his feet the little
Lincoln, who was sitting there
staring in fascination at his assessor. At the author of
his
new idea.

All the way home he was happy. Of course,
he had not liked the word
“ugly.”
But, after all, should he not
be used to that by now? What had
struck him, among words and meanings
he could little understand, was the phrase
“the real thing.”
He didn’t know quite why,
but he liked that.
He liked that very much.

When he was hurt, too much
stared at—
too much
left alone—he
thought about that. He told himself
“After all, I’m
the real thing.”

It comforted him.
```

---

## IC-1618: Lift Off and Miracle Workers

- Title: Lift Off and Miracle Workers
- Author (byline): Donovan Livingston and Taylor Mali
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 914
- Already set (do not supply): none

### Source block (context only)

```text
Author: Donald Livingston
ISBN: 978-0399591372
Publisher: Random House Publishing
Date (Month/Year): April 2017
NOTE: Presented at the Harvard Graduate School of
Education’s 2016 Convocation -- May 25, 2016
Author: Taylor Mali
Book: The Last Time as We Are, Pgs 53-55
ISBN: 978-0982148839
Publisher: Write Bloody Publishing
Date (Month/Year): Aug 2009
```

### Introduction (context only: never use it for content warnings)

```text
In 2016, Donovan Livingston delivered a convocation speech to the Harvard Graduate School of Education that went viral, reaching over 5 million people, and receiving national acclaim.

Livingston's message that day -- the boundless potential that lies within each child, the continuing fight for equity, and the transformative promise of education -- retains its power to challenge and elevate. And at a time when the existence of the American Department of Education balances on the knife’s edge of existence, his words encourage and inspire students, educators, and communities to realize they have the power to change the shape of education, and to . . .

Lift Off by Donovan Livingston and Miracle Workers by Taylor Mali
```

### Performance text (classify this)

```text
At the core, none of us were meant to be common.
We were born to be comets,
Darting across space and time —
Leaving our mark as we crash into everything.

Education then, beyond all other devices of human origin, Is a great equalizer of the conditions of men.”

— Horace Mann, 1848.
At the time of his remarks I couldn’t read, I couldn’t write.
Any attempt to do so, punishable by death.
For generations we have known of knowledge’s infinite

power. Yet somehow, we’ve never questioned the keeper of the

keys —
The guardians of information.
Unfortunately, I’ve seen more dividing and conquering
In this order of operations — a heinous miscalculation of

reality. For some, the only difference between a classroom and a

plantation is time.
How many times must we be made to feel like quotas —
Like tokens in coined phrases? —
“Diversity. Inclusion”
There are days I feel like one, like only —
A lonely blossom in a briar patch of broken promises.
But hey, I’ve always been a thorn in the side of injustice.
Disruptive. Talkative. A distraction.
With a passion that transcends the confines of my

consciousness —
Beyond your curriculum, beyond your standards.
I stand here, a manifestation of love and pain,
With veins pumping revolution.
I am the strange fruit that grew too ripe for the poplar tree.
I am a DREAM Act, Dream Deferred incarnate.
I am a movement — an amalgam of memories America

would care to forget
My past, alone, won’t allow me to sit still.
So my body, like the mind
Cannot be contained.
As educators, rather than raising your voices
Over the rustling of our chains,
Take them off. Un-cuff us.
Unencumbered by the lumbering weight
Of poverty and privilege,
Policy and ignorance.
I was in the 7th grade, when Ms. Parker told me,
“Donovan, we can put your excess energy to good use!”
And she introduced me to the sound of my own voice.
She gave me a stage. A platform.
She told me that our stories are ladders
That makes it easier for us to touch the stars.

So climb and grab them. Keep climbing. Grab them. Spill your emotions in the big dipper and pour out your

soul.
Light up the world with your luminous allure.
To educate requires Galileo-like patience.
Today, when I look my students in the eyes, all I see are

constellations.
If you take the time to connect the dots,
You can plot the true shape of their genius —
Shining in their darkest hour.
I look each of my students in the eyes,
And see the same light that aligned Orion’s Belt
And the pyramids of Giza.
I see the same twinkle
That guided Harriet to freedom.
I see them. Beneath their masks and mischief,
Exists an authentic frustration;
An enslavement to your standardized assessments.
At the core, none of us were meant to be common.
We were born to be comets,
Darting across space and time —
Leaving our mark as we crash into everything.
A crater is a reminder that something amazing happened

here — An indelible impact that shook up the world. Are we not astronomers – searching for the next shooting

star?
I teach in hopes of turning content, into rocket ships —
Tribulations into telescopes,
So a child can see their potential from right where they

stand.
An injustice is telling them they are stars
Without acknowledging night that surrounds them.
Injustice is telling them education is the key
While you continue to change the locks.
Education is no equalizer —
Rather, it is the sleep that precedes the American Dream.
So wake up, wake up! Lift your voices
Until you’ve patched every hole in a child’s broken sky.
Wake up every child so they know of their celestial

potential. I’ve been a Black hole in the classroom for far too long; Absorbing everything, without allowing my light escape.

But those days are done. I belong among the stars. And so do you. And so do they. Together – together we can inspire galaxies of greatness For generations to come. No, no, sky is not the limit. It is only the beginning. Lift off.

Miracle Workers (excerpt) by Taylor Mali (Pg 53-55) I like to lecture on love and speak on

responsibility. I hold forth on humility, compassion, eloquence, and

honesty. And when my students ask, "Are we going to be responsible for this?"

I say, If not you, then who?
You think my generation will be responsible?
We're the ones who got you into this mess,
now you are our only hope.
And when they say, "What we meant to say
was, 'Will we be tested on this?’"
I say, Every single day of your lives!

Once, I put a pencil on the desk of a student
who was digging in her backpack for a pencil.
But she didn't see me do it, so when I walked
to the other side of the room and she raised her hand
and asked if she could borrow a pencil,
I intoned, “In the name of Socrates and Jesus,
and all the gods of teaching,
I declare you already possess everything you will ever

need!”
Shazzam!
"You are the weirdest teacher I have ever -- "
Then she saw the pencil on her desk and screamed.
"You're a miracle worker! How did you do that?"

I just gave you what I knew you needed
before you had to ask for it.
Education is the miracle, I'm just the worker.
But I'm a teacher.
And that's what we do
```

---

## IC-1619: Lion and Blue

- Title: Lion and Blue
- Author (byline): Robert Vavra
- Work: Not specified
- Publisher: William Morrow and Company
- Publication date as stated: Oct 1974
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 590
- Already set (do not supply): none

### Source block (context only)

```text
Author: Robert Vavra
ISBN: 978-0688611644
Publisher: William Morrow and Company
Date (Month/Year): Oct 1974
```

### Introduction (context only: never use it for content warnings)

```text
There’s only one kind of love that can fill us up, make us whole, and give us the happiness we all want: unconditional love or Real Love. This is the story of a lonely lion and a blue butterfly. You see, love comes in all shapes, sizes and colors. It is not bound by gender or age. True love conquers all. Lion and Blue by Robert Vavra
```

### Performance text (classify this)

```text
My lonely roars
echoed far
in a jungle
that was old
to me,
a lion
in the winter
of his years,
whose heart
had never known
spring.

Until that afternoon
when in the darkness
of silent thoughts
my yellow eyes
were dazzled
blue.

Suddenly blossoms
lit this dull stare
when you,
brilliant,
beautiful,
Brazilian
butterfly
drifted into
my life.

Blue became . . .
Blue was
my
love,
my
life,
my all around.

Happiness was
a spring and summer
that seemed could never
turn to
fall.
though you told me,
‘Someday,
Lion,
the time will come
when I will have to
leave you,
in search of

the

flower

of

the

sun.’

Those thoughts made me
want to shut my ears
or roar away
a destiny
which threatened
our happy voyage
across
the sea of
love.

The other butterflies
clustered round my
head,
and off somewhere
I heard a lioness
call,
but in my world,
my sky,
there was only
you
my bella
Blue.

One night you left
me, Blue,
in search of
your golden
destiny.

Then there was
no world for me.
Endless years
I awaited your
return.

But our boat
drifted past
as empty as
my
heart.
And so my quest
began,
I sailed to places
far away.

In search of
you
I wandered
far,
and all the while
I thought,
‘Why could we
not have met
when the time
was right,
when youth had lit
my stars.’

‘But yesterday is over,’ whispered the far-seeing giraffe, ‘as tomorrow is yet to come.’

‘The only time
that is ever
right,’
rumbled the
wise elephant,
‘is
n o w,
so make haste,
this journey of yours
is a one way trip
eternally.’

As I climbed the
grass
towards the clouds,
a yellow blossom
appeared.
Could it be your
destiny
Would you be there,
oh Blue?

‘This flower is the leopard’s.’
came the cheetah’s voice,
‘it sprang from the garden
of his soul.
You won’t find the love
of which you speak
until your roots have grown strong,
grown deep.’

In the dark of
night
or in the flame of
morning sky
often hope would
awaken in my
heart
with the flashing
of blue wings.
But feathers covered
them
and not your brilliance.

Then one day
on the plain’s edge,
where the wind blows
fast and clean,
a wart hog came
trotting by,
a daisy in his
mouth,
and as he passed
I heard these words,

White and straight
stood a daisy
proudly at the
field’s edge.
‘Come among us,’
beckoned the simple
flower.
And so I strode
through that meadow
of
honey and snow.
Then,
not the tawny lioness’s
purrrrr
or the tides
of oceans
could take me from
my course.

But no blossom of
the sun was
there.
‘The brilliant flower
you seek,’
lulled the daisies
‘is springing now
from your lion’s
heart.’
And as rich pollen
covered me,
golden petals crowned

my

head.

Centuries,
years,
days . . .
how many passed,
I don’t know.
But born again
was I
when in the
evening sky
a dot of blue
appeared against
the moon.

And as the sky
oranged
with break of day,
I saw you

Blue.
But to me
why come
when your search had been
for that

golden

blossom

who by now

your heart

had surely

won?

‘Lion, Lion!’
Dreams do
come true.
You dared,
you hoped,
you believed,
and for doing so
look what you’ve become

My
Golden
Maned
Flower
Hero
Of
The
Sun!’

And n o w . . .
Blue!
Blue!
brilliant,
bella,
Brazilian
butterfly,
again my life,
my all around

is

you.
```

---

## IC-1620: Listen Lord, The Creation and Prodigal Son

- Title: Listen Lord, The Creation and Prodigal Son
- Author (byline): James Weldon Johnson
- Work: God’s Trombones
- Publisher: Penguin Books
- Publication date as stated: Feb 1990
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1771
- Already set (do not supply): none

### Source block (context only)

```text
Author: James Weldon Johnson
Book: God’s Trombones
ISBN: 978-0140184037
Publisher: Penguin Books
Date(Month/Year): Feb 1990
```

### Introduction (context only: never use it for content warnings)

```text
The poet and civil rights activist, James Weldon Johnson was influenced by his impressions of the rural South. His interest in the African-American folk tradition was ignited and resulted in a collection of “sermons” entitled God’s Trombones. It is said that Johnson considered the voice of the black preacher to be a musical instrument “not a piano . . . or trumpet but a trombone. From the printed page, peals the roar of the black preacher delivering a rousing sermon. The ability of Johnson to capture the sense of deliverance from the trials and tribulations of everyday life is indeed a talent. Listen Lord, The Creation and Prodigal Son by James Weldon Johnson from the anthology God’s Trombones.
```

### Performance text (classify this)

```text
LISTEN LORD

O Lord, we come this morning Knee-bowed and body-bent Before thy throne of grace.

O Lord - this morning
Bow our hearts beneath our knees,
And our knees in some lonesome valley.
We come this morning
Like empty pitchers to a full fountain,
With no merits of our own.
O Lord - open up a window of heaven,
And lean out far over the battlements of glory,
And listen this morning.
Lord, have mercy on proud and dying sinners
Sinners hanging over the mouth of hell,
Who seem to love their distance well.
Lord - ride by this morning
Mount your milk-white horse,
And ride-a this morning
And in your ride, ride by old hell,
Ride by the dingy gates of hell,
And stop poor sinners in their headlong plunge.
And now, O Lord, this man of God,
Who breaks the bread of life this morning
Shadow him in the hollow of thy hand,
And keep him out of the gunshot of the devil.
Take him, Lord - this morning
Wash him with hyssop inside and out,
Hang him up and drain him dry of sin.
Pin his ear to the wisdom-post,
And make his words sledge hammers of truth
Beating on the iron heart of sin.
Lord God, this morning
Put his eye to the telescope of eternity,
And let him look upon the paper walls of time.
Lord, turpentine his imagination,
Put perpetual motion in his arms,
Fill him full of the dynamite of thy power,
Anoint him all over with the oil of thy salvation,
And set his tongue on fire.
And now, O Lord
When I've done drunk my last cup of sorrow
When I've been called everything but a child of God
When I'm done travelling up the rough side of the
mountain
O Mary's Baby
When I start down the steep and slippery steps of
death
When this old world begins to rock beneath my feet -
Lower me to my dusty grave in peace
To wait for that great gittin' up morning - Amen.

THE CREATION

And God stepped out on space,
And he looked around and said:
I'm lonely -
I'll make me a world.
And far as the eye of God could see
Darkness covered everything,
Blacker than a hundred midnights
Down in a cypress swamp.
Then God smiled,
And the light broke,
And the darkness rolled up on one side,
And the light stood shining on the other,
And God said: That's good!
Then God reached out and took the light in his hands,
And God rolled the light around in his hands
Until he made the sun;
And he set that sun a-blazing in the heavens.
And the light that was left from making the sun
God gathered it up in a shining ball
And flung it against the darkness,
Spangling the night with the moon and stars.
Then down between
The darkness and the light
He hurled the world;
And God said: That's good!
Then God himself stepped down -
And the sun was on his right hand,
And the moon was on his left;
The stars were clustered about his head,
And the earth was under his feet.
And God walked, and where he trod
His footsteps hollowed the valleys out
And bulged the mountains up.
Then he stopped and looked and saw
That the earth was hot and barren.
So God stepped over to the edge of the world
And he spat out the seven seas -
He batted his eyes, and the lightnings flashed -
He clapped his hands, and the thunders rolled -
And the waters above the earth came down,
The cooling waters came down.
Then the green grass sprouted,
And the little red flowers blossomed,
The pine tree pointed his finger to the sky,
And the oak spread out his arms,
The lakes cuddled down in the hollows of the ground,
And the rivers ran down to the sea;
And God smiled again,
And the rainbow appeared,
And curled itself around his shoulder.
The God raised his arm and he waved his hand
Over the sea and over the land,
And he said: Bring forth! Bring forth!
And quicker than God could drop his hand,
Fishes and fowls
And beasts and birds
Swam the rivers and the seas,
Roamed the forests and the woods,
And split the air with their wings.
And God said: That's good!
Then God walked around,
And God looked around
On all that he had made.
He looked at his sun,
And he looked at his moon,
And he looked at his little stars;
He looked on his world
With all its living things,
And God said: I'm lonely still.
Then God sat down -
On the side of a hill where he could think;
By a deep, wide river he sat down;
With his head in his hands,
God thought and thought,
Till he thought: I'll make me a man!
Up from the bed of the river
God scooped the clay;
And by the bank of the river
He kneeled him down;
And there the great God Almighty
Who lit the sun and fixed it in the sky,
Who flung the stars to the most far corner of the night,
Who rounded the earth in the middle of his hand;
This Great God,
Like a mammy bending over her baby,
Kneeled down in the dust
Toiling over a lump of clay
Till he shaped it in his own image;
Then into it he blew the breath of life,
And man became a living soul.
Amen. Amen.

THE PRODIGAL SON
Young man Young man
Your arm's too short to box with God. B
ut Jesus spake in a parable, and he said:
A certain man had two sons.
Jesus didn't give this man a name,
But his name is God Almighty.
And Jesus didn't call these sons by name,
But ev'ry young man,
Ev'rywhere,
Is one of these two sons.
And the younger son said to his father,
He said: Father, divide up the property,
And give me my portion now.

And the father with tears in his eyes said: Son,
Don't leave your father's house.
But the boy was stubborn in his head,
And haughty in his heart,
And he took his share of his father's goods,
And went into a far-off country.
There comes a time,
There comes a time
When ev'ry young man looks out from his father's
house,
Longing for that far-off country.
And the young man journeyed on his way,
And he said to himself as he travelled along:
This sure is an easy road,
Nothing like the rough furrows behind my father's plow.
Young man
Young man
Smooth and easy is the road
That leads to hell and destruction.
Down grade all the way,
The further you travel, the faster you go.
No need to trudge and sweat and toil,
Just slip and slide and slip and slide
Till you bang up against hell's iron gate.
And the younger son kept travelling along,
Till at night-time he came to a city.

And the city was bright in the night-time like day, The
streets all crowded with people,
Brass bands and string bands a-playing,
And ev'rywhere the young man turned
There was singing and laughing and dancing.
And he stopped a passer-by and he said:
Tell me what city is this?
And the passer-by laughed and said: Don't you know?
This is Babylon, Babylon,
That great city of Babylon.
Come on, my friend, and go along with me.
And the young man joined the crowd.
Young man
Young man
You're never lonesome in Babylon.
You can always join a crowd in Babylon.
Young man
Young man
You can never be alone in Babylon,
Alone with your Jesus in Babylon.

You can never find a place, a lonesome place,
A lonesome place to go down on your knees,
And talk with your God, in Babylon.
You're always in a crowd in Babylon.
And the young man went with his new-found friend, And
bought himself some brand new clothes,
And he spent his days in the drinking dens, Swallowing
the fires of hell.
And he spent his nights in the gambling dens,

Throwing dice with the devil for his soul.
And he met up with the women of Babylon.
Oh, the women of Babylon!
Dressed in yellow and purple and scarlet, Loaded with
rings and earrings and bracelets, Their lips like a
honeycomb dripping with honey, Perfumed and sweet-
smelling like a jasmine flower; And the jasmine smell of
the Babylon women Got in his nostrils and went to his
head,
And he wasted his substance in riotous living,
In the evening, in the black and dark of night, With the
sweet-sinning women of Babylon.
And they stripped him of his money,
And they stripped him of his clothes,
And they left him broke and ragged
In the streets of Babylon.
Then the young man joined another crowd The beggars
and lepers of Babylon.
And he went to feeding swine,
And he was hungrier than the hogs;
He got down on his belly in the mire and mud And ate
the husks with the hogs.
And not a hog was too low to turn up his nose At the man
in the mire of Babylon.
Then the young man came to himself
He came to himself and said:
In my father's house are many mansions,
Ev'ry servant in his house has bread to eat, Ev'ry
servant in his house has a place to sleep; I will arise and
go to my father.

And his father saw him afar off,
And he ran up the road to meet him.
He put clean clothes upon his back,
And a golden chain around his neck,
He made a feast and killed the fatted calf,
And invited the neighbors in.
Oh-o-oh, sinner,
When you're mingling with the crowd in BabylonDrinking
the wine of Babylon
Running with the women of Babylon
You forget about God, and you laugh at Death. Today
you've got the strength of a bull in your neck And the
strength of a bear in your arms,
But some 0' these days, some 0' these days,
You'll have a hand-to-hand struggle with bony Death,
And Death is bound to win.
Young man, come away from Babylon,
That hell-border city of Babylon.
Leave the dancing and gambling of Babylon,
The wine and whiskey of Babylon,
The hot-mouthed women of Babylon;
Fall down on your knees,
And say in your heart:
I will arise and go to my Father.
```

---

## IC-1621: Loch Ness Monsters and Something Like Fire

- Title: Loch Ness Monsters and Something Like Fire
- Author (byline): Lenelle Moise (pronounced "moy-eez")
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1116
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lenelle Moise
Book: Word Warriors: 35 Women Leaders in the Spoken
Word Revolution
ISBN: 978-1580052214
Publisher: Seal Press
Date (Month/Year): Oct 2007
Author: Tana Hardy
Book: We Will Be Shelter: Poems for Survival
ISBN: 978-1938912474
Publisher: Write Bloody Publishing
Date (Month/Year): December 2014
```

### Introduction (context only: never use it for content warnings)

```text
Martin Niemöller, a prominent Protestant pastor who opposed the Nazi regime, who spent the last seven years of Nazi rule in a concentration camp, spoke these words of wisdom 80 years ago: .First they came for the Socialists, and I did not speak out— Because I was not a Socialist. Then they came for the Trade Unionists, and I did not speak out— Because I was not a Trade Unionist. Then they came for the Jews, and I did not speak out— Because I was not a Jew. Then they came for me—and there was no one left to speak for me. How can we turn a blind eye to man’s inhumanity to man even on a small, individual scale. Lenelle Moise asks this question in her poem Loch Ness Monsters.
```

### Performance text (classify this)

```text
Loch Ness Monsters by Lenelle Moise

after patricia’s face
was dragged across
the parking lot of pete’s
grocery store and gasoline
stop on buffalo street
in ithaca, ny, one late afternoon
during rush hour traffic in july
2002’s brutal, blatant sun

after a white man held her down and two white women kicked her jaw because they claimed – although they sat innocently in their parked pickup truck -- this stranger/black woman -- patricia – just had to go and look at them funny so they had to get out and try to put her in her place

after their fists and their spit after their tired word nigger

after ithacan would-be witnesses filled their giant grape slurpee cups – filled their unleaded tanks – filled their ears with the predictable weather forecast – their ears with an international report on terrorism -- their air-conditioned ears turned off to screams, turned on to britney spears’ overplayed number one hit hit me baby one more time.

after bystanders sat
in their jammed cars, unmoved, someone
inside the grocery store
called the cops and,
late, the cops
handcuffed the assaulted
twenty-year-old black woman
first because –

though her stunned skull thumped
with bitter bewilderment and her broad
nose bled from the burden of meeting
her tears on three dog shit shoes --
since patricia was shrilling cracker and flailing
her bruised arms uncontrollably, the ithacan
cops thought she seemed
menacing, not molested

after the ithaca times
reported the incident four days
late, the local liberal whites simply
could not believe
it happened here. here?
in Ithaca? My god,
they said, that’s just
incredible. are you serious? here?

and i wonder how some people can keep their minds
open to the possibility of a loch ness monster
open to extraterrestrials, open
to the crazed fantasy of a so-called king of rock
and roll resurrected, somehow
sighted alive; how people will
nod of course to a headline that guesses
angelina stole brad from jennifer;
tarot cards, ouija boards
tea leaves for spiritual guidance
people will bribe invisible grim reapers
with age-defying dreams and potions
people will encourage their children
to write letters to santa claus, share
secrets with jesus and keep appointments
with philanthropic tooth fairies

but the sun we can all confirm and agree upon
will shine down on one black woman –
patricia - getting her ass kicked
by three epithet-wielding whites –
her spirit and features evidently crushed
by their hate – the rage in her
gut, the insistence of her fists
obviously outnumbered

and some people just cannot
see it.
and some people just don’t
believe it.

TRANSITION And yet in a sea of those who turn a blind eye, those who are wronged . . . abused . . . brutalized . . . somehow survive. Tana Hardy questions how those survivors come to view the world. Do they take up the mantle of “defender of the innocent” – “voice of the down-trodden” or do they revel in the word. Survivor. Because I survived, I am better than THOSE victims. Because I survived, they should be able to as well. What does the word survivor mean to you? Something Like Fire by Tana Hardy.

Something Like Fire by Tana Hardy

Survivor: “…but I did it because of the trauma.”

Survivor- what a pointed word.
What a something to sharpen and jab
at someone. Survivor- what a blockade
to stand behind. What a shield. What a
corner around which to peek
a gun. Explosive to roll into
a party. “Everything I’ve said and done
is because I am a Survivor!”
When is the day we become responsible

for ourselves? For the ways our damage spills over,
onto others? I want to join a parade of: This is What
I’ve Done and This is Where I Did it and This is to
Whom. I want a spotlight
on their scars, not mine. I want to carry
my fault on a platter, like a cake
down a street. With the names
of the people I made into a whom
on top. Until everyone comes out
of their houses into the square
and starts confessing, as if
our future depends on it.
(Because it does.)

I want to meet the ones who made me
a whom on the other edge of town
at the end of their cake parade. I want them to put
down their sharp sticks,
empty their cheeks of explosives, and
step out from behind the barricade. I
want them to pull their whole bodies from around the
corner and say,
“Me. I did it.”
Without blinking or minimizing.
And then I want them to give me
some cake. The slice with my name
on top. But when I take a second look,
I want it to be their name. I want our names to be the
same.
(Because they are.)

And then I want to hug
about it. I want Survivor to be a name
we stop taking in vain, stop using
as excuse. Here, I’ll start: I have raged
and thrown and manipulated and coerced and lied and
lied and lied
and lied
and lied. Every single time I have held up the card
“survivor” as if it is a get out of jail free ticket. But
there are real live names in my wake. In the sea foam
behind my boat. Can’t you see their eyes?
The way they spin in the waves- the whites and the blues
and the browns and the hazels of them?
Those are the people I made
into a whom, people to whom I gave
a card, while showing them exactly how to stand

behind it. Survivor- what a pointed word.
What a shield, an explosive. I want the day when
Survivor means a temporary
state, a place to pass through
but not set up a permanent, fenced-in
residence. I want survivor to mean something
like a fire of renewal after which grows a forest with as
many trees as human complexities.
I don’t always want to stomp my feet
on home plate saying,
“That person. Did this. To me.”
But neither do I want to stand
on the pitchers mound- hurling forward
what someone else pitched

at me. I’ve been getting this backwards, thinking
Survivor meant I had to toughen
up instead of melt and maybe offer myself as something
to quench.
Something to ease, to nourish and embolden. Don’t get
me wrong,
I am as mad as a Volkswagen full of hornets about what’s
been done to me, but that doesn’t mean
I want to let my stingers out. Not
only because the world needs all of us
to step into the light. But also because what a day, what
a triumph when Survivor means
-I am-
so much more
than what was done to me.
(Because it does.)
```

---

## IC-1622: The Lorax

- Title: The Lorax
- Author (byline): Theo Geisel (aka Dr. Seuss)
- Work: Not specified
- Publisher: Random House Books
- Publication date as stated: Aug 1971
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: NARRATOR, ONCE-LER, LORAX
- Teaser before the introduction: Yes
- Spoken words (computed): 1395
- Already set (do not supply): none

### Source block (context only)

```text
Author: Theo Geisel (aka Dr. Seuss)
ISBN: 978-0394823379
Publisher: Random House Books
Date (Month/Year): Aug 1971
```

### Introduction (context only: never use it for content warnings)

```text
When Dr. Seuss gets serious, you know it must be important. Published in 1971, and perhaps inspired by the "save our planet" mindset of the 1960s, The Lorax is an ecological warning that still rings true today amidst the dangers of clear-cutting, pollution, and disregard for the earth's environment. In The Lorax, we find what we've come to expect from the illustrious doctor: brilliantly whimsical rhymes and delightfully original. But there is also something more--a powerful message that Seuss implores both adults and children to heed.

The Lorax by Theo Geisel (aka Dr. Seuss)
```

### Performance text (classify this)

```text
NARRATOR: At the far end of town where the Grickle-grass grows and the wind smells slow-and-sour when it blows and no birds ever sing excepting old crows. . . is the Street of the Lifted Lorax. And deep in the Grickle-grass, some people say, if you look deep enough you can still see, today, where the Lorax once stood just as long as it could before somebody lifted the Lorax away.

NARRATOR: What was the Lorax? And why was it there? And why was it lifted and taken somewhere from the far end of town where the Grickle-grass grows? The old Once-ler still lives here. Ask him. He knows.

ONCE-LER: Now I'll tell you, how the Lorax got lifted and taken away. . . It all started way back. . . such a long, long time back. . . Way back in the days when the grass was still green and the pond was still wet and the clouds were still clean, and the song of the Swomee-Swans rang out in space. . one morning, I came to this glorious place. And I first saw the trees! The Truffula Trees! The bright-colored tufts of the Truffula Trees! Mile after mile in the fresh morning breeze. And under the trees, I saw Brown Bar-ba-loots frisking about in their Bar-ba-loot suits as they played in the shade and ate Truffula Fruits. From the rippulous pond came the comfortable sound of the Humming-Fish humming while splashing around. But those trees! Those trees! Those Truffula Trees!

All my life I'd been searching for trees such as these. The touch of their tufts was much softer than silk. And they had the sweet smell of fresh butterfly milk. I felt a great leaping of joy in my heart. I knew just what I'd do! I unloaded my cart. In no time at all, I had built a small shop. Then I chopped down a Truffula Tree with one chop. And with great skillful skill and with great speedy speed, I took the soft tuft. And I knitted a Thneed! The instant I'd finished, I heard a ga-Zump! I looked. I saw something pop out of the stump of the tree I'd chopped down. It was sort of a man. Describe him?. . . That's hard. I don't know if I can. He was shortish. And oldish. And brownish. And mossy. And he spoke with a voice that was sharpish and bossy.

LORAX:(with a sneeze) Mister! I am the Lorax. I speak for the trees. I speak for the trees, for the trees have no tongues. And I'm asking you, sir, at the top of my lungs"- What's that THING you've made out of my Truffula tuft?

ONCE-LER: Look Lorax, There's no cause for alarm.

I chopped just one tree. I am doing no harm.
I'm being quite useful. This thing is a Thneed.
A Theend's a Fine-Something-That-All-People-Need!
It's a shirt. It's a sock. It's a glove. It's a hat.
But it has other uses. Yes, far beyond that.
You can use it for carpets. For pillows! For sheets!
Or curtains! Or covers for bicycle seats!"

LORAX: Sir! You are crazy with greed. There is no one on Earth who would buy that fool Thneed.

ONCE-LER: But the very next minute I proved he was
wrong.
For, just at that minute, a chap came along,
and he thought that the Thneed I had knitted was great.
He happily bought it for three ninety-eight.
(laughing at the Lorax) You poor stupid guy!
You never can tell what some people will buy.

LORAX: I repeat, I speak for the trees!

ONCE-LER: I'm busy. Shut up, if you please. I rushed 'cross the room, and in no time at all, built a radio-phone. I put in a quick call. I called all my brothers and uncles and aunts and I said Listen here! Here’s a wonderful chance for the whole Once-ler Family to get mighty rich! [They] were all knitting Theends just as busy as bees, to the sound of the chopping of Truffula Trees. Then . . . Oh! Baby! Oh! How the business did grow! Now, chopping one tree at a time was too slow So I quickly invented my Super-Axe-Hacker which whacked off four Truffula Trees at one smacker. We were making Thneeds four times as fast as before! And that Lorax? . . . He knocked on my new office door.

LORAX: I'm the Lorax who speaks for the trees which you seem to be chopping as fast as you please. But I'm also in charge of the Brown Bar-ba-loots who played in the shade in their Bar-ba-loot suits and happily lived, eating Truffula Fruits. NOW. . . thanks to your hacking my trees to the ground, there's not enough Truffula Fruit to go 'round. And my poor Bar-ba-loots are all getting the crummies because they have gas, and no food, in their tummies! They loved living here. But I can't let them stay. They'll have to find food. And I hope that they may.

ONCE-LER: I, the Once-ler, felt sad as I watched them all go. BUT . . . business is business! And business must grow I meant no harm. I most truly did not. But I had to grow bigger. So bigger I got. Then again he came back! I was fixing some pipes when that old-nuisance Lorax came back with more gripes.

LORAX: (coughing) I am the Lorax (sneezing, snuffling) Once-ler! You're making such smogulous smoke! My poor Swomee-Swans. . . why, they can't sing a note! No one can sing who has smog in his throat. And so - please pardon my cough – they cannot live here. So I'm sending them off. What's more, let me say a few words about Gluppity- Glupp. Your machinery chugs on, day and night without stop making Gluppity-Glupp. Also Schloppity-Schlopp. And what do you do with this leftover goo?. . . I'll show you. You dirty old Once-ler man, you! You're glumping the pond where the Humming-Fish hummed!

No more can they hum, for their gills are all gummed. So I'm sending them off. Oh, their future is dreary. They'll walk on their fins and get woefully weary in search of some water that isn't so smeary.

ONCE-LER: And then I got mad. I got terribly mad. (yelling) Now listen here, Dad! All you do is yap-yap and day, 'Bad! Bad! Bad! Bad!' Well, I have my rights, sir, and I'm telling you I intend to go on doing just what I do! And at that very moment, we heard a loud whack! From outside in the fields came a sickening smack of an axe on a tree. Then we heard the tree fall. The very last Truffula Tree of them all! No more trees. No more Thneeds. No more work to be done. So, in no time, my uncles and aunts, everyone, all waved me good-bye. They jumped into my cars and drove away under the smoke-smuggered stars. Now all that was left 'neath the bad-smelling sky was my big empty factory. . . the Lorax. . . and I. The Lorax said nothing. Just gave a glance. . . just gave a very sad, sad backward glance. . .

as he lifted himself by the seat of his pants.
And I'll never forget the grim look on his face
when he heisted himself and took leave of this place,
through a hole in the smog, without leaving a trace.
And all that the Lorax left here in this mess
was a small pile of rocks, with the one word. . .
UNLESS. (long pause)
Whatever that meant, well, I just couldn't guess.
That was long, long ago.
But each day since that day I've sat here and worried
and worried away.
Through the years, while my buildings have fallen apart,
I've worried about it with all of my heart.
But now. . . Now that you're here, the word of the Lorax
seems perfectly clear.
UNLESS someone like you cares a whole awful lot,
nothing is going to get better . . . It's not.
SO. . . Catch! (he tosses something down)
It's a Truffula Seed. It's the last one of all!
You're in charge of the last of the Truffula Seeds.
And Truffula Trees are what everyone needs.
Plant a new Truffula. Treat it with care.

Give it clean water. And feed it fresh air. Grow a forest. Protect it from axes that hack. Then the Lorax and all of his friends may come back.
```

---

## IC-1623: Lost in Translation

- Title: Lost in Translation
- Author (byline): James Merrill
- Work: Collected Poems
- Publisher: Knopf
- Publication date as stated: Nov 2002
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1423
- Already set (do not supply): none

### Source block (context only)

```text
Author: James Merrill
Book: Collected Poems
ISBN: 978-0375709418
Publisher: Knopf
Date (Month/Year): Nov 2002
```

### Introduction (context only: never use it for content warnings)

```text
Build your life just as you would a puzzle. Piece by piece. Section by section. You may get bored at times, or frustrated, or feel as though you'd rather give up. What you must do, however, is know that the pieces are all there, and the more ways you try to place them where they belong, the more connections you discover.

What does your puzzle look like? Is it falling into place, or are you forcing the pieces to fit where they don't belong. Lost in Translation by James Merrill uses the metaphor of a “puzzle” to describe one young boy’s attempt to understand the world around him though a series of memories – stories – puzzle pieces. .
```

### Performance text (classify this)

```text
Diese Tage, die leer dir scheinen und wertlos für das All, haben Wurzeln zwischen den Steinen und trinken dort überall.

(TRANSLATION from GERMAN)
"These days, which seem empty
and entirely fruitless to you,
have roots between the stones
and drink from everywhere."

A card table in the library stands ready To receive the puzzle which keeps never coming. Daylight shines in or lamplight down Upon the tense oasis of green felt. Full of unfulfillment, life goes on, Mirage arisen from time's trickling sands Or fallen piecemeal into place: German lesson, picnic, see-saw, walk With the collie who "did everything but talk"— Sour windfalls of the orchard back of us. A summer without parents is the puzzle, Or should be. But the boy, day after day, Writes in his Line-a-Day No puzzle.

He's in love, at least. His French Mademoiselle, In real life a widow since Verdun, Is stout, plain, carrot-haired, devout. She prays for him, as does a curé in Alsace, Sews costumes for his marionettes, Helps him to keep behind the scene Whose sidelit goosegirl, speaking with his voice, Plays Guinevere as well as Gunmoll Jean. Or else at bedtime in his tight embrace Tells him her own French hopes, her German fears, Her—but what more is there to tell? Having known grief and hardship, Mademoiselle Knows little more. Her languages. Her place. Noon coffee. Mail. The watch that also waited Pinned to her heart, poor gold, throws up its hands— No puzzle! Steaming bitterness Her sugars draw pops back into his mouth, translated: "Patience, chéri. Geduld, mein Schatz." (Translation: “Patience, love. Patience, my dear”) (Thus, reading Valéry the other evening And seeming to recall a Rilke version of "Palme," That sunlit paradigm whereby the tree Taps a sweet wellspring of authority, The hour came back. Patience dans l'azur. Geduld im. . . Himmelblau? Mademoiselle. Translation: “Patience in the sky. Patience in . . . sky blue? Ma’am)

Out of the blue, as promised, of a New York
Puzzle-rental shop the puzzle comes—
A superior one, containing a thousand hand-sawn,
Sandal-scented pieces. Many take
Shapes known already—the craftsman's repertoire
Nice in its limitation—from other puzzles:
Witch on broomstick, ostrich, hourglass,
Even (surely not just in retrospect)
An inchling, innocently branching palm.
These can be put aside, made stories of
While Mademoiselle spreads out the rest face-up,
Herself excited as a child; or questioned
Like incoherent faces in a crowd,
Each with its scrap of highly colored
Evidence the Law must piece together.
Sky-blue ostrich? Likely story.
Mauve of the witch's cloak white, severed fingers
Pluck? Detain her. The plot thickens
As all at once two pieces interlock.

Mademoiselle does borders— (Not so fast.

A London dusk, December last.
Chatter silenced in the library
This grown man reenters, wearing grey.
A medium. All except him have seen
Panel slid back, recess explored,
An object at once unique and common
Displayed, planted in a plain tole
Casket the subject now considers
Through shut eyes, saying in effect:
"Even as voices reach me vaguely
A dry saw-shriek drowns them out,
Some loud machinery— a lumber mill?
Far uphill in the fir forest
Trees tower, tense with shock,
Groaning and cracking as they crash groundward.
But hidden here is a freak fragment
Of a pattern complex in appearance only.
What it seems to show is superficial
Next to that long-term lamination
Of hazard and craft, the karma that has
Made it matter in the first place.

Plywood. Piece of a puzzle." Applause
Acknowledged by an opening of lids
Upon the thing itself. A sudden dread—
But to go back. All this lay years ahead.)

Mademoiselle does borders. Straight-edge pieces
Align themselves with earth or sky
In twos and threes, naive cosmogonists
Whose views clash. Nomad inlanders meanwhile
Begin to cluster where the totem
Of a certain vibrant egg-yolk yellow
Or pelt of what emerging animal
Acts on the straggler like a trumpet call
To form a more soph"isticated unit.
By suppertime two ragged wooden clouds
Have formed. In one, a Sheik with beard
And flashing sword hilt (he is all but finished)
Steps forward on a tiger skin. A piece
Snaps shut, and fangs gnash out at us!
In the second cloud—they gaze from cloud to cloud
With marked if undecipherable feeling—
Most of a dark-eyed woman veiled in mauve
Is being helped down from her camel (kneeling)
By a small backward-looking slave or page-boy
(Her son, thinks Mademoiselle mistakenly)
Whose feet have not been found. But lucky finds
In the last minutes before bed
Anchor both factions to the scene's limits
And, by so doing, orient
Them eye to eye across the green abyss.
The yellow promises, oh bliss,
To be in time a sumptuous tent.

Puzzle begun I write in the day's space,
Then, while she bathes, peek at Mademoiselle's
Page to the curé: ". . . cette innocente mère,
Ce pauvre enfant, que deviendront-ils?" (Translation: . . .
This mother innocent, this poor child, what will become?)
Her azure script is curlicued like pieces
Of the puzzle she will be telling him about.
(Fearful incuriosity of childhood!
"Tu as l'accent allemande" (Translation: You have the
German accent) said Dominique.
Indeed. Mademoiselle was only French by marriage.
Child of an English mother, a remote
Descendant of the great explorer Speke,
And Prussian father. No one knew. I heard it
Long afterwards from her nephew, a UN
Interpreter. His matter-of-fact account
Touched old strings. My poor Mademoiselle,
With 1939 about to shake
This world where "each was the enemy, each the friend"
To its foundations, kept, though signed in blood,
Her peace a shameful secret to the end.)
"Schlaf wohl, chéri." (Translation: “Sleep well, darling”)
Her kiss. Her thumb
Crossing my brow against the dreams to come.

This World that shifts like sand, its unforeseen
Consolidations and elate routine,
Whose Potentate had lacked a retinue?
Lo! it assembles on the shrinking Green.

Gunmetal-skinned or pale, all plumes and scars,
Of Vassalage the noblest avatars—
The very coffee-bearer in his vair
Vest is a swart Highness, next to ours.

Kef easing Boredom, and iced syrups, thirst, In guessed-at glooms old wives who know the worst Outsweat that virile fiction of the New: "Insh'Allah, he will tire—" "—or kill her first!"

(Hardly a proper subject for the Home, Work of—dear Richard, I shall let you comb Archives and learned journals for his name— A minor lion attending on Gérôme.)

While, thick as Thebes whose presently complete Gates close behind them, Houri and Afreet Both claim the Page. He wonders whom to serve, And what his duties are, and where his feet,

And if we'll find, as some before us did,
That piece of Distance deep in which lies hid
Your tiny apex sugary with sun,
Eternal Triangle, Great Pyramid!

Then Sky alone is left, a hundred blue
Fragments in revolution, with no clue
To where a Niche will open. Quite a task,
Putting together Heaven, yet we do.

It's done. Here under the table all along Were those missing feet. It's done.

The dog's tail thumping. Mademoiselle sketching
Costumes for a coming harem drama
To star the goosegirl. All too soon the swift
Dismantling. Lifted by two corners,
The puzzle hung together—and did not.
Irresistibly a populace
Unstitched of its attachments, rattled down.
Power went to pieces as the witch
Slithered easily from Virtue's gown.

The blue held out for time, but crumbled, too.
The city had long fallen, and the tent,
A separating sauce mousseline,
Been swept away. Remained the green
On which the grown-ups gambled. A green dusk.
First lightning bugs. Last glow of west
Green in the false eyes of (coincidence)
Our mangy tiger safe on his bared hearth.

Before the puzzle was boxed and readdressed To the puzzle shop in the mid-Sixties, Something tells me that one piece contrived To stay in the boy's pocket. How do I know? I know because so many later puzzles Had missing pieces—Maggie Teyte's high notes Gone at the war's end, end of the vogue for collies, A house torn down; and hadn't Mademoiselle Kept back her pitiful bit of truth as well? I've spent the last days, furthermore, Ransacking Athens for that translation of "Palme." Neither the Goethehaus nor the National Library Seems able to unearth it. Yet I can't Just be imagining. I've seen it. Know How much of the sun-ripe original Felicity Rilke made himself forego (Who loved French words—verger, mûr, parfumer) In order to render its underlying sense. Know already in that tongue of his What Pains, what monolithic Truths Shadow stanza to stanza's symmetrical Rhyme-rutted pavement. Know that ground plan left Sublime and barren, where the warm Romance Stone by stone faded, cooled; the fluted nouns Made taller, lonelier than life By leaf-carved capitals in the afterglow. The owlet umlaut peeps and hoots Above the open vowel. And after rain A deep reverberation fills with stars.

Lost, is it, buried? One more missing piece?

But nothing's lost. Or else: all is translation
And every bit of us is lost in it
(Or found—I wander through the ruin of S
Now and then, wondering at the peacefulness)
And in that loss a self-effacing tree,
Color of context, imperceptibly
Rustling with its angel, turns the waste
To shade and fiber, milk and memory.
```

---

## IC-1624: The Maiden without Hands

- Title: The Maiden without Hands
- Author (byline): Anne Sexton
- Work: Transformations
- Publisher: Mariner Books
- Publication date as stated: Feb 2001
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 741
- Already set (do not supply): none

### Source block (context only)

```text
Author: Anne Sextion
Book: Transformations
ISBN: 978-0618083435
Publisher: Mariner Books
Date (Month/Year): Feb 2001
```

### Introduction (context only: never use it for content warnings)

```text
We all need fairy tales. We read them or watched them as children and they serve as little idealistic beacons of hope once we reach adulthood. Then there are those who worry that all this exposure to happily ever after can warp our brains and leave us unprepared for the harsh reality that life has to offer. But regardless of the happily every eafter endings, there is no denying that many of the events that occur in our fairy tales are dark, scary, and intimidating events. Perhaps none as dark as the one that I have prepared for you today - A strange retelling of the Grimms’ fairy tale in which a wizard tricks a miller into giving him his daughter and then forces the miller to cut off her hands. The girl runs away, has good fortune, but is once again plagued by the malicious wizard. This adaptation is called The Maiden without Hands and is prepared in poetry format by Anne Sexton.
```

### Performance text (classify this)

```text
Is it possible he marries a cripple out of admiration? A desire to own the maiming so that not one of us butchers will come to him with crowbars or slim precise tweezers? Lady, bring me your wooden leg so I may stand on my own two pink pit feet. If someone burns out your eye I will take your socket and use it for an ashtray. If they have cut out your uterus I will give you a laurel wreath to put in its place. If you have cut off your ear I will give you a crow who will hear just as well. My apple has no worm in it! My apple is whole!

Once
there was a cruel father
who cut off his daughter’s hands
to escape from the wizard.

The maiden held up her stumps
as helpless as dog’s paws
and that made the wizard
want her. He wanted to lap
her up like strawberry preserve.
She cried on her stumps
as sweet as lotus water,
as strong as petroleum,
as sure-fire as castor oil.
Her tears lay around her like a moat.
Her tears so purified her
that the wizard could not approach.

She left her father’s house
to wander in forbidden woods,
the good, kind king’s woods.
She stretched her neck like an elastic,
up, up, to take a bite of a pear.
handing from the king’s tree.
Picture her there for a moment,
a perfect still life.

After all,
she could not feed herself
or pull her pants down
or brush her teeth.

She was, I’d say,
without resources.
The king spied upon her at
that moment of stretching up, up
and he thought,
Eeny, Meeny, Miny, Mo –
There but for the grace of --
I will take her for my wife.

And thus they were married
and lived together on a sugar cub.
The king had silver hands made for her.
they were polished daily and kept in place,
little tin mittens.
The court bowed at the sight of them from a distance.
The leisurely passerby stopped and crossed himself.

What a fellow he is, they said of the king,
and kept their lips pursed as for a kiss.
But that was not the last word
for the king was called to war.
Naturally the queen was pregnant
so the king left her in care of his mother.
Buy her a perambulator, he said,
and send me a message when my son is born.
Let me hear no catcalls
or see a burned mattress.
He wad superstitious.
You can see his point of view.

When the son wads born
the mother sent a message
but the wizard intercepted it,
saying, instead, a changeling was born.
The king didn’t mind.
He was used to this sort of thing by now.
He said: Take care,
but the wizard intercepted it,
saying: Kill both;
then cut out her eyes and send them,
Also cut out his tongue and send it;
I will want my proof.

The mother,
now the grandmother --
a strange vocation to be a mother at all --
told them to run off in the woods.
The queen named her son
Painbringer
and fled to a safe cottage in the woods.
She and Painbringer were so good in the woods
that her hands grew back.
The ten fingers budding like asparagus,
the palms as whole as pancakes,
as soft and pink as face powder.

The king returned to the castle
and heard the news from his mother
and then he set out for seven years in the woods
never once eating a thing,
or so he said,
doing far better than Mahatma Ghandi.

He was good and kind as I have already said
So he found his beloved.
She brought forth the silver hands.
She brought froth Painbringer
and he realized they were his,
though both now unfortunately whole.
Now the butchers will come to me,
he thought, for I have lost my luck.
It put an insidious fear in him
like a tongue depressor held fast
at the back of your throat.
But he was good and kind
so he made the best of it
like a switch hitter.

They returned to the castle and had a second wedding feast.

He put a ring on her finger this time
and they danced like dandies.
All their lives they kept the silver hands,
polished daily,
a kind of purple heart,
a talisman,
A yellow star.
```

---

## IC-1625: Making Sarah Cry

- Title: Making Sarah Cry
- Author (byline): Cheryl L. Costello-Forshey
- Work: Chicken Soup for the Teen’s Soul II
- Publisher: Health Communications, Inc
- Publication date as stated: Oct 1998
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 766
- Already set (do not supply): none

### Source block (context only)

```text
Author: Cheryl L. Costello-Forshey
Book: Chicken Soup for the Teen’s Soul II
ISBN: 1558746161
Publisher: Health Communications, Inc
Date (Month/Year): Oct 1998
```

### Introduction (context only: never use it for content warnings)

```text
”Never criticize a man until you walk a mile in his moccasins” began as a Native American adage, but its truth stood the test of time. “Do unto others as you would have them do unto you” Even Aretha Franklin’s R-E-S-P-E-C-T demands that the moral message be heard. This message crosses religious barriers, cultural barriers and even bridges the gap between generations. It’s simple really . . . so simple even a child can understand why it’s wrong to enjoy Making Sarah Cry by Cheryl L. Costello-Forshey.
```

### Performance text (classify this)

```text
He stood among his friends from school, He joined their childhood games Laughing as they played kickball And when they called poor Sarah names.

Sarah was unlike the rest; She was slow and not as smart, And it would seem to all his friends She was born without a heart

And so he gladly joined their fun Of making Sarah cry.

But somewhere deep within his heart, He never knew just why

For he could hear his mother's voice, Her lessons of right and wrong Playing over and over inside his head Just like a favorite song.

"Treat others with respect, son, The way you'd want them treating you. And remember, when you hurt others, Someday, someone might hurt you."

He knew his mother wouldn't understand The purpose of their game Of teasing Sarah, who made them laugh As her own tears fell like rain. The funny faces that she made And the way she'd stomp her feet

Whenever they mocked the way she walked Or the stutter when she'd speak.

To him she must deserve it Because she never tried to hide. And if she truly wanted to be left alone, Then she should stay inside.

But every day she'd do the same:
She'd come outside to play,
And stand there, tears upon her face,
Too upset to run away.

The game would soon be over.
As tears dropped from her eyes,
For the purpose of their fun
Was making Sarah cry.

It was nearly two whole months
He hadn't seen his friends.
He was certain they all must wonder
What happened and where he'd been

So he felt a little nervous
As he limped his way to class.
He hoped no one would notice,
He prayed no one would ask

About that awful day: The day his bike met with a car, Leaving him with a dreadful limp And a jagged-looking scar.

So he held his breath a little
As he hobbled into the room,
Where inside he saw a "Welcome Back" banner
And lots of red balloons.

He felt a smile cross his face As his friends all smiled, too And he couldn't wait to play outside- His favorite thing to do.

So the second that he stepped outdoors And saw his friends all waiting there, He expected a few pats on the back- Instead, they all stood back and stared.

He felt his face grow hotter As he limped to join their side To play a game of kickball And of making Sarah cry.

An awkward smile crossed his face When he heard somebody laugh And heard the words, "Hey freak, Where'd you get that ugly mask?"

He turned expecting Sarah, But Sarah could not be seen. It was the scar upon his own face That caused such words so mean.

He joined in their growing laughter,
Trying hard to not give in
To the awful urge inside to cry
Or the quivering of his chin.

They are only teasing
He made himself believe.
They are still my friends;
They'd never think of hurting me.

But the cruel remarks continued
About the scar and then his limp.
And he knew if he shed a single tear
They'd label him a wimp.

And so the hurtful words went on, And in his heart he wondered why. But he knows without a doubt

The game would never end, until they made him cry.

And just when a tear had formed,
He heard a voice speak out from behind.
"Leave him alone you bullies,
Because he's a friend of mine".

He turned to see poor Sarah,
Determination on her face,
Sticking up for one of her own tormentors
And willing to take his place.

And when his friends did just that,
Trying their best to make poor Sarah cry,
This time he didn't join in,
And at last understood exactly why.

"Treat others with respect, son, The way you'd want them treating you. And remember, when you hurt others, Someday, someone might hurt you."

It took a lot of courage
But he knew he must be strong,
For at last he saw the difference
Between what's right and wrong.

And Sarah didn't seem so weird.
Through his understanding eyes.
Now he knew he'd never play again
The game of making Sarah cry.

It took several days of teasing
And razzing from his friends,
But when they saw his strength,
They chose to be like him.

And now out on the playground, A group of kids meets every day For a game of kickball and laughter

And teaching their new friend, Sarah, how to play.
```

---

## IC-1626: The Man with the Broken Fingers

- Title: The Man with the Broken Fingers
- Author (byline): Carl Sandburg
- Work: Selected Poems
- Publisher: Harvest Books
- Publication date as stated: Aug 1996
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 621
- Already set (do not supply): none

### Source block (context only)

```text
Author: Carl Sandburg
Book: Selected Poems
ISBN: 978-0156003964
Publisher: Harvest Books
Date (Month/Year): Aug 1996
```

### Introduction (context only: never use it for content warnings)

```text
"We are going to pick potatoes." That's what the family housekeeper told four-year-old Irene when she was whisked away to flee German-occupied Norway in 1942. Berman was one of 1,200 Norwegian Jews who escaped to Sweden, while the nearly 800 Jews who remained were deported and perished. What happened to the Jews of Norway is a largely unknown chapter in World War II history. However, Carl Sandburg’s poem “The Man with the Broken Fingers” published in The Chicago Times Syndicate newspapers August 23,1942brought to light a story of one incident in which a Norwegian nationalist defied the Gestapo. The Man with the Broken Fingers by Carl Sandburg.
```

### Performance text (classify this)

```text
The Man with the Broken Fingers throws a shadow. Down from the spruce and evergreen mountain timbers of Norway- And across Europe and the Mediterranean to the oasis palms of Libya- He lives and speaks a sign language of lost fingers. From a son of Norway who slipped the Gestapo nets, the Nazi patrols, The story comes as told among those now in Norway. Shrines in their hearts they have for this nameless man Who refused to remember names names names the Gestapo wanted. "Tell us these names. Who are they? Talk! We want those names!" And the man faced them, looked them in the eye, and hours passed and no names came-hours on hours and no names for the Gestapo. They told him they would break him as they had broken others. The rubber hose slammed around face and neck, The truncheon handing pain with no telltale marks, Or the distinction of the firing squad and death in a split second The Gestapo considered these and decided for him something else again. "Tell us those names. Who were they? Talk! Names now-or else!" And no names came-over and over and no names.

So they broke the little finger of the left hand. Three fingers came next and the left thumb bent till it broke. Still no names and there was a day and night for rest and thinking it over. Then again the demand for names and he gave them the same silence. And the little finger of the right hand felt itself twisted, Back and back twisted till it hung loose from a bleeding socket. Then three more fingers crashed and splintered one by one And the right thumb back and back into shattered bone. Did he think about violins or accordions he would never touch again? Did he think of baby or woman hair he would never again play with? Or of hammers or pencils no good to him any more? Or of gloves and mittens that would always be misfits? He may have laughed half a moment over a Gestapo job So now for a while he would handle neither knife nor fork Nor lift to his lips any drinking-cup handle Nor sign his name with a pen between thumb and fingers. And all this was halfway-there was more to come. The Gestapo wit and craft had an aim. They wanted it known in Norway the Gestapo can be terrible. They wanted a wide whispering of fear of how the Nazis handle those who won't talk or tell names. "We give you one more chance to co-operate." Yet he had no names for them. His locked tongue, his Norwegian will pitted against Nazi will, His pride and faith in a free man's way, His welcoming death rather than do what they wanted They brought against this their last act of fury, Breaking the left arm at the elbow, Breaking it again at the shoulder socket- And when he came to in a flicker of opening eyes They broke the right arm first at the elbow, then the shoulder. By now of course he had lost all memory of names, even his own. And there are those like you and me and many many others Who can never forget the Man with the Broken Fingers. His will, his pride as a free man, shall go on. His shadow moves and his sacred fingers speak. He tells men there are a thousand writhing shattering deaths Better to die one by one than to say yes yes yes When the answer is no no no and death is welcome and death comes soon And death is a quiet step into a sweet clean midnight.
```

---

## IC-1627: March 25, 1911 (From Fragments from the Fire)

- Title: March 25, 1911 (From Fragments from the Fire)
- Author (byline): Chris Llewellyn
- Work: Fragments from the Fire, Pg 4-9
- Publisher: Puffin
- Publication date as stated: March 1987
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 951
- Already set (do not supply): none

### Source block (context only)

```text
Author: Chris Llewellyn
Book: Fragments from the Fire, Pg 4-9
ISBN: 978-0140585865
Publisher: Puffin
Date (Month/Year): March 1987
```

### Introduction (context only: never use it for content warnings)

```text
The Triangle Shirtwaist Factory Fire -- the deadliest workplace accident in New York City's history. An event that highlighted the disgusting nature of the “sweatshop” in America –sweatshops where children as young as 13 were paid a mere $15 a week and who were forced to work 12 hours a day, every day.

On March 25th, 1911, the blaze ripped through the congested 8th, 9th and 10th floors of the building as petrified workers -- mostly teen-age immigrant girls who spoke little English -- desperately tried to make their way downstairs. By the time the fire burned itself out, 146 people were dead. Forty-nine workers had burned to death or been suffocated by smoke, 36 were dead in the elevator shaft and 58 died from jumping to the sidewalks.

This poem takes us back to that fateful day. It was spring, it was Saturday, it was payday and it was close to closing time on March 25, 1911 . . . . by Chris Llewellyn
```

### Performance text (classify this)

```text
(Pg 4-9) It was Spring. It was Saturday. Payday. For some it was Sabbath. Soon it will be Easter. It was approaching April, nearing Passover. It was close to closing time.

The heads of trees budding
in Washington Square Park.
The sun a hot flywheel spinning
the earth’s axle. The days long
enough for leaving in light.

It was Spring.

America’s sweethearts – the ladies -- stroll in shirtwaists of lawn and lace, Mimic Charles Dana Gibson’s Girls. They pose in finery cut from bolts of flimsy and stitched by garment girls on Gibbs, Wilcox, and Singer machines.

It was Saturday.

Up in the Ash Building in the Triangle Shirtwaist Company Rosie Glantz is singing “Every Little Movement Has a Meaning of Its Own.” * Fixing hair, arranging puffs and trendils, the other girls in the cloakroom join in: (Sing) “Let me call you Sweetheart, I’m in love with you.” **

It was Payday.

Attar-of-roses, lily of the valley,
still they smell of machine oil
that soaks the motors and floors.
The barrel in each stairwell
could fill a thousand lamps.

For some it was Sabbath.

Here at Triangle, Sophie Salemi
and Della Costello sew on Singers.
Neighbors from Cherry Street,
they piecework facing each other,
the oil pan hitting their knees.
Tomorrow sisters will nail flowers
on tenement doors.

Soon it will be Easter.

The machine heads connected by belts
to the flywheel to rotating axle
sing the Tarantella. Faster,
Faster vibrate the needles, humming
faster the fashionable dance.

It was approaching April.

Della and Sophie up on Ninth
piece sleeves, race the needle’s pace
no knowing on Eighth, paper patterns
burn from the wire, fall on machines,
Spark moths and pinwheels round the room.
Rockets push up cutting-tables.

It was nearing Passover.

On Eighth, cutters throw pails of water
on the lawn of lame, and Louis,
Holding the canvas hose, hollers:
“No pressure! Nothing coming!”

It was close to closing time.

Down on Green Street, Old Dominick
Pushes his wheelbarrow, describes
“a big puff” when windows popped,
glittering showers of glass.

It was Spring.

Flaming swords, Pluto piles to Ninth.
Sophie and Della and dozens of others
jump on machine tables; the aisles jammed
with wicker workbaskets and chairs.

It was Saturday.

Mrs. Yaller testified: “Some froze at
machines. Others were packed in the cloakroom
filled with smoke. I heard them yelling
in Yiddish or Italian, crying out
the names of their children.”

It was Payday.

Reporter Bill Shepherd is writing:
“I remember the great strike of last year,
these same girls demanding decent
working conditions.”

For some it was Sabbath.

Rosie runs to the stairway. The door, Locked! The telephone, Dead! Piling red Ribbons, fire backs girls into windows. They stand on sills, see the room a smashed altar lamp, hear the Screaming novenas of flame.

Soon it will be Easter.

Pleats of purple and gold wave, incandescent filaments of lace snow in shrapnel of needles and screws. The blaze from molten bolts stains glass, walls and lawns – on Cherry Street sisters nail flowers on tenement doors.

It was approaching April.

“I could see them falling,” Said Lena Goldman. “I was sweeping out front of my café. At first we thought it was bolts of cloth – till they opened with legs! I still see the day it rained children. Yes.

It was nearly Passover”

Sophie and Della stand on windowsill,
look out on the crazy quilt of town:
We will leave for our
block on Cherry Street,
Leave these skeletons
leaning on machines,
the faces fixed on black
crucifix of cloakroom window.

It was close to closing time.

The Times quotes Mr. Porter: “The Triangle never had a fire drill – only three factories in the city have. One man I pleaded with replied, ‘Let em burn. They’re A lot of cattle anyhow.’”

It was Spring.

Sophie and Della stand on sill:
We will leave, our arms
around each other, our only
sweethearts. Piling red roses
two white hearses pull up
Cherry Street and the Children
of Mary Society march
in banners of Prayers.

It was Saturday.

Captain Henry was the first policeman to arrive: “I saw dozens of girls hanging from sills. Others, dresses on fire, leapt from the ledges.”

It was Payday.

Sophie and Della look on crazy quilt of town:
Fifty of our schoolmates
sing in procession:
O Trinity of Blessed Light
Our Lady of Perpetual Help
Ave Maria, Ave Maria
Now and at the Hour
of the Tarantella.

For some it was Sabbath.

Ordering the nets and ladders, Battalion Chief Worth explains, “I didn’t know they would come down three and even four together. Why these little ones went through life-nets, pavement and all.”

Soon it will be Easter.

Sophie and Della stand on windowsill:
Look, the flywheel sun sinks
in the west. In the Winter
Garden, Mr. Jolson springs
and bows in blackface.

It was approaching April.

At the Metropolitan Opera
George M. Cohan struts “The Rose
of Tralee” to the rich trailing
in diamond-sackcloth, rending
green ashes of dollar bills.

It was nearing Passover. ‘

Sophie and Della stand on sill,
look down crazy quilt of town:
Intertwined comets we will stream
the nightmares of Triangle Bosses
Joseph Asch
Max Blanck
Isaac Harris.

It was close to closing time.

Our Bosses of the Locked
Doors of Sweetheart Contracts
who in puffs and tendrils
of silent telephones,
Disconnected hoses, barred
shutters, fire escapes
dangling in perpetual no
help on earth in heaven.

It was Spring.

The Lord is my shepherd
green pastures still
waters anointest heads
With oil overflowing
prepares a table – now
our arms around each other
we thread the needles
where no rich man can go spinning
the earth’s axle we are
leaving in light.
```

---

## IC-1628: The Medical Profession – A Collection

- Title: The Medical Profession – A Collection
- Author (byline): Anne Sexton, David Schiedermayer and John Stone
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 912
- Already set (do not supply): none

### Source block (context only)

```text
Author: Anne Sexton
Book: Poetry in Medicine: An Anthology of Poems
About Doctors, Patients, Illness and Healing
ISBN: 978-0892554492
Publisher: Persea
Date (Month/Year): March 16, 2015
Author: John Stone
Book: Music from Apartment 8: New and Selected
Poems
ISBN: 978-0807129548
Publisher: LSU Press
Date (Month/Year): 2004
Author: David Schiedermayer
Book: House Calls, Rounds, and Healings: A Poetry
Casebook
ISBN: 978-1883620172
Publisher: Galen Press Ltd
Date (Month/Year): October 1, 1996
```

### Introduction (context only: never use it for content warnings)

```text
When you were a child, what did you want to be when you grew up? An astronaut. A professional athlete . . . a doctor? Many children change their answer as they grow older. But for some, medicine will always be their calling. There’s a sense of pride in helping others – providing care in the direst of times. The poem, Gaudeamus Igitur by John Stone was presented to the graduates of Emory University School of Medicine in 1982.
```

### Performance text (classify this)

```text
From “Doctors”

They work with herbs
and penicillin
They work with gentleness
and the scalpel.
They dig out the cancer,
close an incision
and say a prayer
to the poverty of the skin.
They are not Gods
though they would like to be;
they are only a human
trying to fix up a human.

From “Gaudeamus Igitur” *

* Therefore, let us rejoice For this is the day of joy

For this is the day you know too little

against the day when you will know too much For you will be invincible

and vulnerable in the same breath

which is the breath of your patients For their breath is our breathing and our reason For the patient will know the answer

and you will ask him

ask her For the family may know the answer For there may be no answer

and you will know too little again

or there will be an answer and you will know too much

forever For you will look smart and feel ignorant

and the patient will not know which day it is for you

and you will pretend to be smart out of ignorance For you must fear ignorance more than cyanosis For you will cry and there will be no one to talk to

or no one but yourself
For you will be lonely
For you will be alone
For there is a difference
For the days will run together in gallops and the years

go by as fast as the speed of thought

which is faster than the speed of light

or Superman

or Superwoman
For you will not be Superman
For you will not be Superwoman
For this is the end of examinations
For this is the beginning of testing
For Death will give the final examination

and everyone will pass For the best hospital is a house of joy

even with rooms of pain and loss

exits of misunderstanding
For there is the mortar of faith
For it helps to believe
For disease will peer up over the hedge

of health, with only its eyes showing For you can be trained to listen only for the oboe

out of the whole orchestra For you may need to strain to hear the voice of the patient

in the thin reed of his crying For you will learn to see most acutely out of

the corner of your eye

to hear best with your inner ear For there are late signs and early signs For the patient's story will come to you

like hunger, like thirst For you will know the answer

like second nature, like first For the patient will live

and you will try to understand For you will be amazed

or the patient will not live

and you will try to understand
For you will be baffled
For you will try to explain both, either, to the family
For love is what death would always intend if it had the
choice
For there will be days of joy
For there will be elevators of elation

and you will walk triumphantly

in purest joy

along the halls of the hospital

and say Yes to all the dark corners

where no one is listening For the heart will lead For the head will explain

but the final common pathway is the heart

whatever kingdom may come
For what matters finally is how the human spirit is
spent
For this is the day of joy
For this is the morning to rejoice
For this is the beginning

Therefore, let us rejoice

Gaudeamus igitur.

TRANSITION But let’s bring the practice of medicine to a more personal level. One doctor, one patient – a fight for a life. Fighting Bare-Handed by David Schiedermayer

Fighting Bare-Handed

Last night, Saturday night
I fought death bare-handed
in and over the body
of a 61 year-old man
with liver and kidney failure
which started and worsened
after his back surgery.
I had a bad feeling at about 6 pm,
looking at his 4 pm labs,
so I went to his room and found him
barely breathing. Breathing once
or maybe twice a minute.
So I sat by his bed
and I begged him to breathe
I pinched his toes when he stopped.

Once, when he had stopped for a minute,
and I am not proud of this,
but it is just true,
I rubbed my bare knuckles right across
the staples on his abdomen
(they had operated his back from both
the back and the front to fix the bones)
and he woke up with a start
and a grimace
and said, "what do you want me to do?"
And knowing how death was possessing him,
I said "Breathe!" to him, not to death,
and he took a big breath before he
fell back to sleep.
And so I kept him alive until we could
move him down to the ICU, waited with him
for an hour in that quiet room at the very end
of the orthopedics unit, just me and him and death,
me pinching him every minute
death quietly creeping in and through
I pinched him and shook him
and used Narcan to fight the morphine
so he would have a chance to breathe
And when I went home
I laughed a little as I walked across the driveway
I skipped up the steps
because
in the ICU they were giving him all kinds of medicine
and putting in all kinds of lines
but me
I guess I really do
like a good bare-knuckled fight on a Saturday night.
```

---

## IC-1629: The Melancholy Death of Oyster Boy & Other Stories

- Title: The Melancholy Death of Oyster Boy & Other Stories
- Author (byline): Tim Burton
- Work: Not specified
- Publisher: Harper Collins
- Publication date as stated: Oct 1997
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1125
- Already set (do not supply): none

### Source block (context only)

```text
Author: Tim Burton
ISBN: 978-0688156817
Publisher: Harper Collins
Date (Month/Year): Oct 1997
```

### Introduction (context only: never use it for content warnings)

```text
In this collection, Tim Burton – the creative genius behind Edward Scissorhands, Sleepy Hollow and Nightmare Before Christmas, gives birth to a cast of gruesomely sympathetic children: misunderstood outcasts who struggle to find love and belonging in their cruel, cruel worlds. What Burton's sad kids all have in common are their bizarre differences.

But the characters in these poems who are truly terrifying are humans, determined to destroy anything that is different. In many ways, the Oyster Boy universe reflects our own world: a place where innocence disappears too easily. As you listen to the seemingly childish verses, think about one thing: Who are the real monsters here?

The Melancholy Death of Oyster Boy and Other Stories by Tim Burton
```

### Performance text (classify this)

```text
The Robot Boy

Mr. and Mrs. Smith had a wonderful life. They were a normal, happy husband and wife. One day they got news that made Mr. Smith glad. Mrs. Smith would be a mom which would make him the dad!

But something was wrong with their bundle of joy. It wasn't human at all, it was a robot boy!

He wasn't warm and cuddly
and he didn't have skin.
Instead there was a cold, thin layer of tin.
There were wires and tubes sticking out of his head.
He just lay there and stared,
not living or dead.

The Melancholy Death of Oyster Boy

He proposed in the dunes,
they were wed by the sea,
Their nine-day-long honeymoon
was on the isle of Capri.

For their supper they had one spectacular dish-
a simmering stew of mollusks and fish.
And while he savored the broth,
her bride's heart made a wish.

That wish came true-she gave birth to a baby. But was this little one human Well, maybe.

Ten fingers, ten toes,
he had plumbing and sight.
He could hear, he could feel,
but normal?
Not quite.

This unnatural birth, this canker, this blight, was the start and the end and the sum of their plight.

She railed at the doctor: "He cannot be mine. He smells of the ocean, of seaweed and brine."

"You should count yourself lucky, for only last week,
I treated a girl with three ears and a beak.
That your son is half oyster
you cannot blame me.
. . . have you ever considered, by chance,
a small home by the sea?"

Not knowing what to name him,
they just called him Sam,
or sometimes,
"that thing that looks like a clam"

Everyone wondered, but no one could tell, When would young Oyster Boy come out of his shell?

When the Thompson quadruplets espied him one day, they called him a bivalve and ran quickly away.

One spring afternoon,
Sam was left in the rain.
At the southwestern corner of Seaview and Main,
he watched the rainwater as it swirled
down the drain.

His mom on the freeway
in the breakdown lane
was pounding the dashboard-
she couldn't contain
the ever-rising grief,
frustration,
and pain.

"Really, sweetheart," she said
"I don't mean to make fun,
but something smells fishy
and I think it's our son.
I don't like to say this, but it must be said,
you're blaming our son for your problems in bed."

He tried salves, he tried ointments
that turned everything red.
He tried potions and lotions
and tincture of lead.
He ached, and he itched and he twitched and he bled.

The doctor diagnosed, "I can't quite be sure, but the cause of the problem may also be the cure. They say oysters improve your sexual powers. Perhaps eating your son would help you for hours!"

He came on tiptoe,
he came on the sly,
sweat on his forehead,
and on his lips-a lie.

"Son, are you happy? I don't mean to pry, but do you dream of Heaven? Have you ever wanted to die?

Sam blinked his eye twice. but made no reply. Dad fingered his knife and loosened his tie.

As he picked up his son,
Sam dripped on his coat.
With the shell to his lips,
Sam slipped down his throat.

They buried him quickly in the sand by the sea -sighed a prayer, wept a tear-and they were back home by three.

A cross of gray driftwood marked Oyster Boy's grave. Words writ in the sand promised Jesus would save.

But his memory was lost with one high-tide wave.

*****

Mummy Boy

He wasn't soft and pink
with a fat little tummy;
he was hard and hollow,
a little boy mummy.

"Tell us, please, Doctor,
the reason or cause,
why our bundle of joy
is just a bundle of gauze."

"My diagnosis," he said
"for better or worse,
is that your son is the result
of an old pharaoh’s curse."

That night they talked
of their son's odd condition-
they called him "a reject
from an archaeological expedition."

They thought of some complex
scientific explanation,
but assumed it was simple
supernatural reincarnation.

With the other young tots
he only played twice,
an ancient game of virgin sacrifice.
(But the kids ran away, saying, "You aren't very nice.")

alone and rejected, Mummy Boy wept, then went to the cabinet where the snack food was kept.

He wiped his wet sockets with his mummified sleeves, and sat down to a bowl of sugar-frosted tanna leaves.

One dark, gloomy day, from out of the fog, appeared a little white mummy dog.

For his newfound wrapped pet,
he did many things,
like building a doghouse
à la Pyramid of kings.

It was late in the day-
just before dark.
Mummy Boy took his dog
for a walk in the park.

The park was empty except for a squirrel, and a birthday party for a Mexican girl.

The boys and girls had all started to play, but noticed that thing that looked like a papier mâché.

"Look it’s a píñata,"
said one of the boys,
"Let's crack it wide open
and get the candy and toys."

They took a baseball bat
and whacked open his head.
Mummy Boy fell to the ground;
he finally was dead.

Inside of his head
were no candy or prizes,
just a few stray beetles
of various sizes.

*****

Anchor Baby

There was a beautiful girl
who came from the sea.
And there was just one place
that she wanted to be.

With a man named Walker
who played in a band.
She would leave the ocean
and come onto the land.

He was the one that she wanted the most. And she tried everything to capture this ghost.

But throughout all their lives
they never connected.
She wandered the earth
alone and rejected

She tried looking happy
she tried looking tragic,
she tried astral projecting,
and [you know] black magic.

Nothing could join them,
except maybe one thing,
just maybe . . .
something to anchor their spirits . . .
They had a baby.

But to give birth to a baby
they needed a crane.
the umbilical cord
was in the form of a chain.

It was ugly and gloomy,
and as hard as a kettle.
It had no pink skin,
just heavy gray metal.

The baby that was meant to bring them together, just shrouded them both in a cloud of foul weather.

So Walker took off
to play with the band.
And from that day on,
he stayed mainly on land.

And she was alone
with her gray baby anchor,
who got so oppressive
that eventually sank her.

As she went to the bottom,
not fulfilling her wish,
it was her, and her baby . . .
and a few scattered fish.
```

---

## IC-1630: Middle Passage

- Title: Middle Passage
- Author (byline): Robert Hayden
- Work: American Negro Poetry: An Anthology
- Publisher: Hill & Wang
- Publication date as stated: December 1995
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1207
- Already set (do not supply): none

### Source block (context only)

```text
Author: Robert Hayden
Book: American Negro Poetry: An Anthology
ISBN: 0809015641
Publisher: Hill & Wang
Date (Month/Year): December 1995
```

### Introduction (context only: never use it for content warnings)

```text
The poem Middle Passage by Robert Hayden, tells the story of the slave trade in three parts. Part 1 takes us on board a slave ship, and shows us the chilling inhumanity of a world with no borders or laws but itself. Part 2, in the terrifying voice of an unrepentant slave trader, presents a brotherhood of greed (which is no brotherhood at all) between the slavers and the African tribal kings with whom they traded in human flesh. Finally Part 3 describes the slave revolt on the Amistad, led by Cinquez, who became a symbol both of freedom and of the awful violence that must sometimes be its path. Middle Passage by Robert Hayden.
```

### Performance text (classify this)

```text
Jesús, Estrella, Esperanza, Mercy:

Sails flashing to the wind like weapons, sharks following the moans the fever and the dying; horror the corposant and compass rose.

Middle Passage: voyage through death to life upon these shores.

"10 April 1800-- Blacks rebellious. Crew uneasy. Our linguist says their moaning is a prayer for death, our and their own. Some try to starve themselves. Lost three this morning leaped with crazy laughter to the waiting sharks, sang as they went under."

Desire, Adventure, Tartar, Ann:

Standing to America, bringing home black gold, black ivory, black seed.

Deep in the festering hold thy father lies, of his bones New England pews are made, those are altar lights that were his eyes.

Jesus Saviour Pilot Me Over Life's Tempestuous Sea

We pray that Thou wilt grant, O Lord, safe passage to our vessels bringing heathen souls unto Thy chastening.

Jesus Saviour

"8 bells. I cannot sleep, for I am sick
with fear, but writing eases fear a little
since still my eyes can see these words take shape
upon the page & so I write, as one
would turn to exorcism. 4 days scudding,
but now the sea is calm again. Misfortune
follows in our wake like sharks (our grinning
tutelary gods). Which one of us
has killed an albatross? A plague among
our blacks--Ophthalmia: blindness--& we
have jettisoned the blind to no avail.
It spreads, the terrifying sickness spreads.
Its claws have scratched sight from the Capt.'s eyes
& there is blindness in the fo'c'sle
& we must sail 3 weeks before we come
to port."

What port awaits us, Davy Jones' or home? I've heard of slavers drifting, drifting, playthings of wind and storm and chance, their crews gone blind, the jungle hatred crawling up on deck.

Thou Who Walked On Galilee

"Deponent further sayeth The Bella J
left the Guinea Coast
with cargo of five hundred blacks and odd
for the barracoons of Florida:

"That there was hardly room 'tween-decks for half the sweltering cattle stowed spoon-fashion there; that some went mad of thirst and tore their flesh and sucked the blood:

"That Crew and Captain lusted with the comeliest of the savage girls kept naked in the cabins; that there was one they called The Guinea Rose and they cast lots and fought to lie with her:

"That when the Bo's'n piped all hands, the flames spreading from starboard already were beyond control, the negroes howling and their chains entangled with the flames:

"That the burning blacks could not be reached,
that the Crew abandoned ship,
leaving their shrieking negresses behind,
that the Captain perished drunken with the wenches:

"Further Deponent sayeth not."

Pilot Oh Pilot Me

II

Aye, lad, and I have seen those factories,
Gambia, Rio Pongo, Calabar;
have watched the artful mongos baiting traps
of war wherein the victor and the vanquished

Were caught as prizes for our barracoons.
Have seen the nigger kings whose vanity
and greed turned wild black hides of Fellatah,
Mandingo, Ibo, Kru to gold for us.

And there was one--King Anthracite we named him--
fetish face beneath French parasols
of brass and orange velvet, impudent mouth
whose cups were carven skulls of enemies:

He'd honor us with drum and feast and conjo
and palm-oil-glistening wenches deft in love,
and for tin crowns that shone with paste,
red calico and German-silver trinkets

Would have the drums talk war and send
his warriors to burn the sleeping villages
and kill the sick and old and lead the young
in coffles to our factories.

Twenty years a trader, twenty years, for there was wealth aplenty to be harvested from those black fields, and I'd be trading still but for the fevers melting down my bones.

III

Shuttles in the rocking loom of history, the dark ships move, the dark ships move, their bright ironical names like jests of kindness on a murderer's mouth; plough through thrashing glister toward fata morgana's lucent melting shore, weave toward New World littorals that are mirage and myth and actual shore.

Voyage through death, voyage whose chartings are unlove.

A charnel stench, effluvium of living death
spreads outward from the hold,
where the living and the dead, the horribly dying,
lie interlocked, lie foul with blood and excrement.

Deep in the festering hold thy father lies, the corpse of mercy rots with him, rats eat love's rotten gelid eyes. But, oh, the living look at you with human eyes whose suffering accuses you, whose hatred reaches through the swill of dark to strike you like a leper's claw. You cannot stare that hatred down or chain the fear that stalks the watches and breathes on you its fetid scorching breath; cannot kill the deep immortal human wish, the timeless will.

"But for the storm that flung up barriers
of wind and wave, The Amistad, señores,
would have reached the port of Príncipe in two,
three days at most; but for the storm we should
have been prepared for what befell.
Swift as a puma's leap it came. There was
that interval of moonless calm filled only
with the water's and the rigging's usual sounds,
then sudden movement, blows and snarling cries
and they had fallen on us with machete
and marlinspike. It was as though the very
air, the night itself were striking us.
Exhausted by the rigors of the storm,
we were no match for them. Our men went down
before the murderous Africans. Our loyal
Celestino ran from below with gun
and lantern and I saw, before the cane-
knife's wounding flash, Cinquez,
that surly brute who calls himself a prince,
directing, urging on the ghastly work.
He hacked the poor mulatto down, and then
he turned on me. The decks were slippery
when daylight finally came. It sickens me
to think of what I saw, of how these apes
threw overboard the butchered bodies of
our men, true Christians all, like so much jetsam.
Enough, enough. The rest is quickly told:
Cinquez was forced to spare the two of us
you see to steer the ship to Africa,
and we like phantoms doomed to rove the sea
voyaged east by day and west by night,
deceiving them, hoping for rescue,
prisoners on our own vessel, till
at length we drifted to the shores of this
your land, America, where we were freed
from our unspeakable misery. Now we
demand, good sirs, the extradition of
Cinquez and his accomplices to La
Havana. And it distresses us to know
there are so many here who seem inclined
to justify the mutiny of these blacks.
We find it paradoxical indeed
that you whose wealth, whose tree of liberty
are rooted in the labor of your slaves
should suffer the august John Quincey Adams
to speak with so much passion of the right
of chattel slaves to kill their lawful masters
and with his Roman rhetoric weave a hero's
garland for Cinquez. I tell you that
we are determined to return to Cuba
with our slaves and there see justice done.
Cinquez--
or let us say 'the Prince'--Cinquez shall die."

The deep immortal human wish, the timeless will:

Cinquez its deathless primaveral image, life that transfigures many lives.

Voyage through death to life upon these shores.
```

---

## IC-1631: Miss Spider’s Wedding

- Title: Miss Spider’s Wedding
- Author (byline): David Kirk
- Work: Not specified
- Publisher: Scholastic Press
- Publication date as stated: 1995
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1225
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Kirk
ISBN: 978-0590568661
Publisher: Scholastic Press
Date (Month/Year): 1995
```

### Introduction (context only: never use it for content warnings)

```text
Miss Spider is spinning with joy! She has met a wonderful spider man who is wise and kind and ever so sincere. Perhaps he's just the one to be Miss Spider's Mr. Right. But when her well-meaning friends set out to find her a more dashing mate, the suave arachnid strongman they choose threatens to destroy even the best-spun spider plans

Miss Spider’s Wedding by David Kirk.
```

### Performance text (classify this)

```text
“Good morning, Miss! A lovely day.” Miss Spider spun around To see Ike hanging by his knees Three inches from the ground.

“My good friend Holley,” Ike went on, “Is someone you should know. But he’s too timid to come down Or even say hello.”

They heard a snap and then a crash And gasped as Holley tumbled. He flopped down at Miss Spider’s feet, Embarrassed, stunned and rumpled.

Miss Spider knelt to help him up. He blushed, to shy to speak. She bid demurely, “Won’t you come To tea one day this week?”

The color drained from Holley’s face. He looked as though he’d swoon. His acorn hat slipped from his head. He gulped, “This afternoon?”

And when she heard his little voice, It seemed to her somehow That she had known him always Though they’d never met ‘til now…

“Please pay attention when I speak. Stop daydreaming!” barked May. Miss Spider’s thoughts were still upon The man she met that day.

May nagged, “You should get on with life. I thought by now you’d be a wife!” “But I _” Miss Spider tried to say. “You mustn’t interrupt!” sniffed May.

May jabbered on and on and on…. Miss Spider, with her patience gone,

Surveyed the clock and tapped the floor, But when a face peeked ‘round the door,

She whispered, “I apologize,
But, May I just now realize,
A gentleman who asked to call
Is waiting for me in the hall.”

“A man?” squealed May, “Well, Finally!” She dashed right out so she could see, The screamed, “Get lost you puny pest. She’s waiting for her special guest!”

Miss Spider scurried toward the din. She took his hand, then led him in. May cried, “How can I stop her folly?

She’s desperate if she’s dating Holley!”

They talked of all her dreams and hopes, Of art and nature, love and fate. They peered though toy kaleidoscopes And murmured thoughts I shan’t relate.

Then Holley held Miss Spider’s hand…. I’ll say no more, you understand. For private moments between spiders Should not be witnessed by outsiders.

Back home, May snipped at Ike, her mate, “Miss Spider’s come undone! That milksop Holley is her date. Go fetch a better one!”

“Be certain he’s intelligent, Strong, handsome, brave and elegant. Just find an eight-legged Mr. Right And bring him back here by tonight.”

Ike said, “But I think Holley
Is particularly nice.
It’s not just me who thinks so.
You can go and ask the mice.

“They say he’s helpful, wise and kind And always so polite. Perhaps he’s just the one to be Miss Spider’s Mr. Right.”

May gasped, “You’ve lost your senses too! That pantywaist will never do. What a difference if he’s kind and wise? He isn’t half Miss Spider’s size.

“I see I’ll have to go with you. For clearly, Ike, You simply do not have a clue To what we women like.”

May called, “Oh, spider sir, yoo-hoo! I’ve got the perfect girl for you.”

She whispered, “Now I’ll put things right.”

“I hope,” squeaked Ike, “he doesn’t bite.”

“Please tell me of this lonely miss,” The spider strongman cooed. “Is she a beauty? Is she rich? And is she in the mood…

“To be adroitly charmed and wooed By dashing, handsome me? But, how could it be otherwise!” He laughed triumphantly.

Miss Spider later welcomed in This strange arachnid gentleman. His air was fine, his manner grand. He bowed and kissed her dainty hand,

“I’ve journeyed her, dear lady, From the Land of Falling Leaves. Please let me introduce myself, I’m called Spiderus Reeves.”

He peered around the drawing room
At all the finery.
He coveted the furnishings,
The carpets and settee.

All this, he thought, would soon be mine If she and I were wed. He mused, her house will suit me well. But here is what he said:

“My darling, I can plainly see That you are everything to me. I long to know the soul within Your lovely exoskeleton.”

“Is it mere chance? No, it is fate, That soon we shall co-webitate/ ‘Twas set down by a will divine That I am yours and you are mine.”

“My angel let us not delay,”
The sly Spiderus pled.
“Tomorrow is the perfect day
For you and I to wed.”

“Kind sir, you move to fast for me,” Miss Spider cried protestingly. “My love already has been spun And promised to another one.”

“You cannot mean,” Spiderus howled, “That you’re rejecting me! Tell me this loathsome rival’s name; I’ll squash him like a flea!”

His hot breath sprayed Miss Spider’s face- With all the force he had, He screamed, “You will reveal his name!” She said, “I won’t you cad!”

He turned his back and brayed, “I must Go find and grind him into dust! So foolish woman, be forewarned. Spiderus Reeves shall not be scorned.”

At that same moment in the hall, Poor Holley, staring at the wall,

Could dwell on one and just one thought, Does she love me? Does she not?

Just then there was a little sound That didn’t seem quite right.

He cocked his head and heard two voices Whimpering in fright.

“And so it’s you,” Spiderus snarled, “Who dares to interfere.

There’s been just one mistake, my friend, But I shall fix it here.”

Holley’s life flashed before his eyes Peering up that toothy jaw. As everything was growing dim, Fading out, he thought he saw

An angel swoop down in a gown Of yellow flecked with black,

Who shrieked, “Let go of him, you brute!” And smacked the scoundrel’s back.

Drifting back to consciousness, Holley sensed someone he knew…. Yes, yes, Miss Spider’s lovely face Came swimming into view.

“Darling, are you back with me?” His spider nurse begged hopefully. “I’ve tried a hundred different ways

To wake you up for three whole days!”

He gazed upon here reverently, Then wobbling to her side,

Looked up into her eyes and whispered, “Will you be my bride?”

A blush of scarlet tinged her cheek. Her lips, aquiver, could not speak. He stroked her gently with his feet.

She murmured softly, “Yes, my sweet.”

They sat together in the sun,
And when the day is through,
They’d made a list of all the most
Important things to do.

The crickets would be asked to play The music on their wedding day. The field mice, woolly bears and bees Would cater and affair to please!

“I’ll bake the cake,” Miss Spider said, “And weave my silken veils.” The Holley peeped. “I’ll spin a suit With silk to hat and tails!”

“We’ll send an incitation out
To every bug alive,
With notices in every bush
And treetop, hill and hive.”

“Oh, see how handsome Holley looks!” Miss spider sings with glee. “Of all the spiders in the world, he chose to be with me.”

“We’ve found the place where love abides, and share the warmth that it provides For all those who have found the way To savor life’s most sweet bouquet.”

The bride and groom, at last withdrawn From all the chaos on the lawn, Poise low upon a willow tree And hold each other tenderly.

We see their forms in silhouette, Their shapes are clear to us, and yet, How can we fully recognize The beauty seen through true loves eyes.
```

---

## IC-1632: The Missing Piece

- Title: The Missing Piece
- Author (byline): Shel Silverstein
- Work: Not specified
- Publisher: HarperCollins Publishers, Inc
- Publication date as stated: May 1976
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 558
- Already set (do not supply): none

### Source block (context only)

```text
Author: Shel Silverstein
ISBN: 978-0060256715
Publisher: HarperCollins Publishers, Inc
Date (Month/Year): May 1976
```

### Introduction (context only: never use it for content warnings)

```text
A truly unique and multi-faceted artist, Shel Silverstein was a renowned poet, playwright, illustrator, screenwriter, and songwriter. Best known for his immensely popular children’s books including The Giving Tree, Falling Up, and The Missing Piece, Silverstein has delighted millions of readers around the world, becoming one of the most popular and best-loved children's authors of all time.

In The Missing Piece, Silverstein concocts a marvelous tale with a powerful message: “Nno one should try to find all the answers, no one should hope to fill all the hopes in themselves, because a person without a search, loose ends, internal conflicts and external goals becomes too smooth to enjoy life." Never stop searching for The Missing Piece by Shel Silverstein.
```

### Performance text (classify this)

```text
It was missing a piece.
And it was not happy.
So it set off in search of its missing piece.
And as it rolled it sang this song-

"Oh I'm lookin' for my missin' piece

I'm lookin' for my missin' piece

Hi-dee-ho, here I go,

Lookin' for my missin' piece."
Sometimes it baked in the sun
but then the cool rain would come down.
And sometimes it was frozen by the snow
but then the sun would come and warm it again.
And because it was missing a piece it could not very
fast so it would stop to talk to a worm
or smell a flower
and sometimes it would pass a beetle
and sometimes the beetle would pass it
and this was the best time of all.
And on it went, over oceans

"On I'm lookin' for my missin' piece

Over land and over seas

So grease my knees and fleece my bees

I'm lookin' for my missin' piece."
through swamps and jungles
up mountains
and down mountains
Until one day, lo and behold!

"I've found my missin' piece," it sang,

"I've found my missin' piece

So grease my knees and fleece my bees

I've found my..."
"Wait a minute," said the piece.
"Before you go greasing your knees
and fleecing your bees..."
I am not your missing piece. I am nobody's piece.
I am my own piece.
And even if I was somebody's missing piece
I don't think I'd be yours!"
"Oh," it said sadly,
"I'm sorry to have bothered you."
And rolled on.
It found another piece
but this one was too small.
And this one was too big
this one too sharp
and this one too square.
One time it seemed to have found the perfect piece

but it didn't hold it tightly enough

and lost it.

Another time it held too tightly

and broke.

So on and on it rolled,

having adventures

falling into holes

and bumping into stone walls.

And one day it came upon another piece that seemed to be just right.

"Hi," it said.

"Hi," said the piece.

"Are you anybody else's missing piece?"

"Not that I know of."

"Well, maybe you want to be your own piece?"

"I can be someone's and still be mine."

"Well, maybe you don't want to be mine."

"Maybe I do."

"Maybe we won't fit...."

"Well..."

"Hummm?"

"Ummmm!"
It fit!
It fit perfectly!
At last! At last!
And away it rolled
and because it was now complete,
it rolled faster and faster.
Faster than it had ever rolled before!
So fast that it could not stop to talk to a worm
or smell a flower
too fast for a butterfly to land.
But it could sing its happy song,
at last it could sing "I've found my missing piece."
And it began to sing-

"I've frown my nizzin' geez

Uf vroun my mitzin' brees

So krease ny meas

An bleez ny drees

Uf frown..." Oh my, now that it was complete it could not sing at all. "Aha," it thought.

"So that's how it is!"

So it stopped rolling...

and it set the piece down gently,

and slowly rolled away

and as it rolled it softly sang-

"Oh I'm lookin' for my missin' piece

I'm lookin' for my missin' piece

Hi-dee-ho, here I go,

Lookin' for my missin' piece."
```

---

## IC-1633: Mission Statement

- Title: Mission Statement
- Author (byline): Big Poppa E (Eirik Ott)
- Work: Big Poppa E's Greatest Hits: Poems To Read Out Loud
- Publisher: Lulu.com
- Publication date as stated: 2007
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 642
- Already set (do not supply): none

### Source block (context only)

```text
Author: Big Poppa E (Eirik Ott)
Book: Big Poppa E's Greatest Hits: Poems To Read Out
Loud
ISBN: 978-0615149486
Publisher: Lulu.com
Date(Month/Year): 2007
```

### Introduction (context only: never use it for content warnings)

```text
You have a purpose in life. You know in your heart what's most important to you. In fact, your mission and values are expressed every day, by how you live–you just may not realize it. A personal mission statement provides clarity and gives you a sense of purpose. It defines who you are and how you will live. Eirik Ott also known as Big Poppa E has crafted one of the most amazing Mission Statements that I’d like to share with you today. It’s not the Mission Statement for an organization or even for an individual, it is the Mission Statement for a group of people I hold in the hightest esteem . . . Poets. Mission Statement by Big Poppa E.
```

### Performance text (classify this)

```text
“We are poets. And that lifestyle choice may have destroyed our credit, yes. It may have destroyed relationships, yes. It may have destroyed our backs from sleeping on couches between times when we could afford a place of our own, yes. But, oh, the beauty. The soul. The whole wide world. We live for that connection between a poet and someone moved to touch their hand to their chest and whisper, “Oh.” Between two people sitting cross-legged on dusty wooden floors bathed in Joni Mitchell and candlelight at 3am. Heads bowed. Hands held. Knees touching. Between the wind and a person alone at a bus stop whispering his truth over invisible turntable break-beats from the shady confines of his hoodie. It’s all poetry. All of it. Every single breath is scented with poetry. We will die penniless, but oh the stories. The love. The whole wide world held limp in the palms of our hands. The smiles on our faces as we bid you all goodbye with a twinkle in our eyes and so many sweet, sad songs in our hearts. So many people never get the chance to fly, because they never have the courage to leap blindingly, stupidly, floppingly out of the nest and bash themselves against the branches all the way down then get up and do it again and again so many times they feel like they’ll die if they try again, but that’s the only way to learn how to fly. Every poet who has ever spread their wings and left the bonds of this earth has a body covered in scars and bruises you feel in every word they speak. We don’t just write poetry.

We live poetry.
Warm noses on cold windowpanes leave haiku in
frost.
Blank pages across foreheads yield truth.
We can cut our wrists on your lips and drip songs on
your tongues.
We can’t help it.
We are poets.
People chain themselves to desks
and cage themselves in cubicles
and trade their precious hours on this planet
for scraps of paper and a gold watch and some
fleeting notion of security.
And we’re the crazy ones?
Wasting time with moonbeams and seashores.
We’re the irresponsible ones?
Chasing butterflies and making love on rooftops.
To hell with that!

Poetry may be the rose colored glasses through
which we see the world,
but we get to see everything.
We are not allowed to close our eyes.
We do not have the right to remain silent.
We are hopelessly, painfully, ravishingly,
wonderfully, terribly, horribly
in love with love. And life itself.
Even when it hurts.
Even when we cry and beg for it all to end.
Even then it’s all so very beautiful and real and
perfect.
And we carry sunshine in our chests.
Our rib cages cast shadows on the blind side of our
skin.
You can see ghosts dancing in our flesh if you
squint.
And we can guide ships to rocky shores
just by toeing the lips of the ocean and spreading
our arms wide.
Our goal in life is simple.
To be.
Wide eyed and breathless at the wonders of the
world around us
and dance naked in the warm summer rain
and laugh and laugh
even when everything sucks.
Because we may not always be happy
and we may not always be right
and we may not always be beautiful.
But right here and right now we are all so young.
Young enough to be alive.
And all the stoplights are so green
they sprout tendrils that tickle the tops of passing
buses.
And the whole wide world is still so full of magic
and possibility.
It would be an insult not to drink deeply of it.
That’s what we do.
We drink deeply of life in full-throated gulps.
That’s who we are.
We are poets.”
```

---

## IC-1634: Move Pen Move

- Title: Move Pen Move
- Author (byline): Shane Koyczan
- Work: Visiting Hours
- Publisher: House of Parlance Media, Inc.
- Publication date as stated: Sept 2005
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 542
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
When your mother dies, lessons learned when you were four become much more meaningful. Sometimes the air thins and you gasp for breath just sitting in a chair. You lose something vast and precious that you didn't even know you had. Your chance to repay an enormous debt is lost. The one person who would take on anyone, or anything (any army for that matter) in your defense is no longer there for you. You very much want to give a big hug to every little old lady you meet. . . and you would love for them to hug you back.

Move Pen Move by Shane Koyczan
```

### Performance text (classify this)

```text
Stay
That’s what mothers say when their sons and daughters go away
They say stay
My mother said go
So I wasn’t there the night she fell out of her wheelchair
So frustrated that she amputated her legs . . . rather tried to with
a steak knife
Her life lay on the white floor like
Roses in the snow
Our relationship was an anthem composed of words like

“gotta go”
So we went
And sent our regards on post cards from the places we’ve been
Stories about all the things we’ve seen
That’s how it was with you and I
Why say good bye when we could still write
And then I took your hands
We should have practiced our good-byes
Because then I took your eyes
And I was somewhere in the middle of nowhere
Watching the sun rise
Over a stop sign placed down the center line of a high way full of
sudden turns for the worse
Running back home cause I gotta play nurse
Gotta figure out which pill alleviates which pain
Which part of your brain is being used for a boxing bag
As your body became a never ending game of freeze tag
Taking place in an empty playground
That was left looking for your limbs in the lost and found and I
couldn’t set you free
So we just sat there
Our heads bent towards each other like flowers in the small
hours of the morning
While light wondering in like a warning that
Time is passing
And you right along with it
Bit by bit everyday
And all I can say is if I could I would write you some way

out of this
But my gift is useless
And you said no
Write me a poem to make me happy
So I wrote move pen move
Write me a bedroom where curse make love to our cancers
But my mother just motions to a bottle full of answers and says
Help me go
And I know something of how pianos feel when it looks at the
fireplace to see sheet music
Being used for kindling
Smoke signaling the end of some song that it thought would take
too long to learn
Now I just sit here and watch you burn away
All those notes never had a chance to play to hear the music of
what you had to say
But I count out the pills just to see if I can do it
I can’t even get half way through it before I turn back into your
son and say
Stay
I could hook up my heart to your ears and let my tears be your
morphine drip
Because maybe it’s easier to let you slip away than it is to say
goodbye
So I hold my breath
Because in the countdown to death the question of why melts
into when
How much time do we have left
Because if I knew what I know now then
I would say move pen move
Write me a mountain
Because head stones are not big enough
And my mother says
Stop it
Write me a poem to make me happy
So I write this
Stay
She smiles and says
Gotta go
I know
Good bye. . .
```

---

## IC-1635: Mrs. Riberio and What Teachers Make

- Title: Mrs. Riberio and What Teachers Make
- Author (byline): Sarah Kay and Taylor Mali Mrs. Riberio
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1320
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sarah Kay
Book: No Matter the Wreckage
ISBN: 978-1938912481
Publisher: Write Bloody Publishing
Date (Month/Year): March 2014
Author: Taylor Mali
Book: What Learning Leaves
ISBN: 978-1887012171
Publisher: Hanover Press
Date (Month/Year): July 2002
```

### Introduction (context only: never use it for content warnings)

```text
One of my favorite quotes about teaching goes something like this: One hundred years from now it will not matter what kind of car I drove, what kind of house I lived in, how much money I had in the bank, nor what my clothes looked like. But the world may be a little better, because... I was important in the life of a child. Teachers, I believe, are the most important people in our society – they shape the future.

In her poem Mrs. Riberio, author Sarah Kay pays tribute to a teacher who most definitely shaped her future and the future of a multitude of students. Mrs. Riberio by Sarah Kay.
```

### Performance text (classify this)

```text
I was in Northern India, at a school run entirely by women volunteers, when I heard it for the first time in ages. It was barely audible above the shouting of children -- the squeals and laughter bubbling from the schoolyard into the classroom windows. But it was there: the swish of silk saris and the jingle jangle of bangles on thin wrists like wind chimes.

This is what learning sounds like. I remember.

I remember when I was five years old, the principal of my Junior School was Mrs. Ribeiro. She was an Indian woman the size of a nightlight, and she glided like a sailboat through the hallways of our school.

Once, when I got close enough to grab a fistful of her draping silk sari, I lifted it to try and see whether she had any feet at all. I thought she floated.

We begged to be sent to her office: the hanging plants like a jungle above our heads, her quiet laughter. Adults needed appointments, but we did not. And even when she was in a grown-up meeting, all it took was a gentle knock on the door, a peek around the corner, and she was off calling, "Sorry dear. We’ll have to reschedule. I have to see someone else about a very important matter. It’s about a gold star. It’s about a new diorama. It’s about a finished reading book one level higher than last time."

She visited every classroom, knew every student by name. She spoke to us like we were scholars. Artists. Scientists. Athletes. Musicians. And we were My world was the size of a crayon box, and it took every color to draw her.

Once, on a New York City sidewalk, a group of women in a brightly colored saris walked by and someone shouted, "Look, Mom. Look at all those principals!" My world was the size of a classroom. It was a tall as I could stretch my fingers, calling, Please! Let me be the one to read to Mrs. Ribeiro. Let me be the one to show her what I know. Clothes. Shirt. Pants. Socks. Shoes. Animals. Cat. Dog. Bird. Fish. Look how much I know.

She brought us guests and artists and a petting zoo. They set up the cages in the parking lot while we were still tucked up in our classroom, unaware. Rabbits and guinea pigs poked out their noses, but Mrs. Ribeiro came to rest in front of the llama cage.

She and the llama considered each other for a long time. She asked if he was tame enough to go inside. The trainers laughed and told her he was plenty tame, but he didn’t know how to go up stairs. So she led him to the elevator. And when the doors slid open on the second floor, there stood Mrs. Ribeiro in her bright pink sari, with gold bangles and a llama on a leash.

She floated from class to class, and we stared, cheered, laughed, and shouted. We tugged at her sari calling, "Miss, what is that? Where did it come from?" She made us wonder. She made us question. She made us proud of what we had learned. Clothes. Shirt. Pants. Shoes. Socks. Saris. Animals. Cat. Dog. Bird. Fish. Llama. Look how much I’ve learned.

She taught us to share. She taught us to listen when someone else is speaking. And then she let us go. We were dandelion seeds released to the wind, she asked for no return. We are saplings now with gentle hands.

The girl with bright cheeks and messy hairpins now works at an orphanage in Cameroon. The boy with the color-ordered markers is now a graphic designer in Chicago. The one with the best diorama is now an animal activist in Argentina. The girl who loved to read out loud is now a poet in India. She let us fly. So I find myself at the front of a classroom. My students tug at my sleeves and ask me, "Miss, do all poets wear big black boots?" I pray for patience. For wisdom. To find a way to tame all the peculiar animals of this world, to coax them enough to brave the elevator, to see the doors slide open to my student’s gaping mouths.

All the wile they wonder.
They worry about everything.
They worry about what to write.
They worry about their grades.
They talk over one another until I cannot hear them.

I tell them, "Listen. Listen to one another like you know you are scholars. Artists. Scientists. Athletes. Musicians. Like you know you will be the ones to shape this world. Show me how many colors you know how to draw with. Show me how proud you are of what you have learned. And I promise I will do the same."

TRANSITION So . . . . Sarah Kay leaves us with a teacher’s promise . . . but in this next poem, Taylor Mali leaves us with just as much passion when he speaks the truth about teaching. After all, he does have a policy about honest and ass-kicking. What Teachers Make by Taylor Mali What Teachers Make

He says the problem with teachers is
What’s a kid going to learn
from someone who decided his best option in life
was to become a teacher?
He reminds the other dinner guests that it’s true
what they say about teachers:
Those who can, do; those who can’t, teach.
I decide to bite my tongue instead of his
and resist the temptation to remind the dinner guests
that it’s also true what they say about lawyers.
Because we’re eating, after all, and this is polite
conversation.
I mean, you’re a teacher, Taylor.
Be honest. What do you make?
And I wish he hadn’t done that— asked me to be
honest—
because, you see, I have this policy about honesty and
ass-‐kicking:
if you ask for it, then I have to let you have it.

You want to know what I make? I make kids work harder than they ever thought they could. I can make a C+ feel like a Congressional Medal of Honor and an A-‐ feel like a slap in the face. How dare you waste my time with anything less than your very best. I make kids sit through 40 minutes of study hall in absolute silence. No, you may not work in groups. No, you may not ask a question. Why won’t I let you go to the bathroom? Because you’re bored. And you don’t really have to go to the bathroom, do you? I make parents tremble in fear when I call home: Hi. This is Mr. Mali. I hope I haven’t called at a bad time, I just wanted to talk to you about something your son said today. To the biggest bully in the grade, he said, “Leave the kid alone. I still cry sometimes, don’t you? It’s no big deal.”

And that was noblest act of courage I have ever seen.
I make parents see their children for who they are
and what they can be.
You want to know what I make? I make kids wonder,
I make them question.
I make them criticize.
I make them apologize and mean it.
I make them write.
I make them read, read, read.
I make them spell definitely beautiful, definitely
beautiful, definitely beautiful
over and over and over again until they will never
misspell
either one of those words again.
I make them show all their work in math
and hide it on their final drafts in English.
I make them understand that if you’ve got this,
then you follow this,
and if someone ever tries to judge you
by what you make, you give them this.

Here, let me break it down for you, so you know what I say is true: Teachers make a goddamn difference! Now what about you?
```

---

## IC-1636: Mulatto Poetry Program

- Title: Mulatto Poetry Program
- Author (byline): Langston Hughes and Zora Howard
- Work: Clutch
- Publisher: Penmanship Books
- Publication date as stated: Jan 2011
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 856
- Already set (do not supply): none

### Source block (context only)

```text
Cross by Langston Hughes and
Mulatto by Langston Hughes
Book: The Collected Poems of Langston Hughes
ISBN: 978-1439571736
Publisher: Vintage Classics
Date (Month/Year): Nov 2008
Biracial Hair by Zora Howard
Book: Clutch
ISBN: 978-0983121909
Publisher: Penmanship Books
Date (Month/Year): Jan 2011
```

### Introduction (context only: never use it for content warnings)

```text
That first poem was Cross by Langston Hughes . . . and it makes me think about the difficulty of growing up as a part of two different cultures.

I often hear people say things like, “It doesn’t matter what you look like on the outside; it’s what’s inside that counts,” or “Nobody’s really different; we are all the same,” Really?

Let’s keep it real, we are not all the same, and you can sugar-coat it if you’d like to, but at the end of the day, each one of us has a unique story to tell and personal struggle that is all our own. Mulatto by Langston Hughes tells of his personal struggle to fit in.
```

### Performance text (classify this)

```text
Cross by Langston Hughes My old man’s a white old man And my old mother’s black. If ever I cursed my white old man I take my curses back. If ever I cursed my black old mother And wished she were in hell, I’m sorry for that evil wish And now I wish her well My old man died in a fine big house. My ma died in a shack I wonder where I’m going to die, Being neither white nor black.

Mulatto by Langston Hughes
I am your son, white man!
Georgia dusk
And the turpentine woods.
One of the pillars of the temple fell.
You are my son!
Like Hell!
The moon over the turpentine woods.
The Southern night
Full of stars,
Great big yellow stars.
What’s a body but a toy?
Juicy bodies
Of nigger wenches
Blue black
Against black fences.
O, you little bastard boy,
What’s a body but a toy?
The scent of pine wood stings the soft night air.
What’s the body of your mother?
Silver moonlight everywhere.
What’s the body of your mother?
Sharp pine scent in the evening air.
A nigger night,
A nigger joy,
A little yellow
Bastard boy. Naw, you ain’t my brother.
Niggers ain’t my brother.
Not ever.
Niggers ain’t my brother.

The Southern night is full of stars,
Great big yellow stars.
O, sweet as earth,
Dusk dark bodies
Give sweet birth
To little yellow bastard boys.
Git on back there in the night,
You ain’t white
The bright stars scatter everywhere.
Pine wood scent in the evening air.
A nigger night,
A nigger joy. I am your son, white man!
A little yellow
Bastard boy.

TRANSITION Take two or more cultural identities and mix them together, then slap a few labels and stereotypes onto them, dice ‘em up and then, just for fun, put them all back together again into whatever one box you see fit that day based on, say . . . hair texture, skin tone, eye or nose shape, and lip fullness, et voila! You’ve got a mixed-race person. And for 13 year old Zora Howard, Bi-racial Hair is the worst!

Biracial Hair by Zora Howard
I have bi-racial hair
Pantene Pro-V waves on the top
Easy to style, comb, rock-
Until-I encounter my naps,
I’m not talking about those-cute detangle with the spray
naps.
I’m talking about those, slave naps, like,
No comb, brush, or man can handle the kind of naps I
got- like,
No way you are touching my hair-naps like
Back 10 feet up, or we can dance naps
Those naps like-
D***!
I have bi-racial hair,
Those smooth and silk rafts hanging all through my
mane,
Until you get to the back, and encounter the jungle, in
which you can find Tarzan and Jane.
In the front you forget and relax in the pleasure,
Until you get to the back and remember pain
Baby hair slicked back with that good 4 dollar pomade,
That goes with roots and tangles,
Soaked with that same olive oil; mixed with that
spaghetti sauce mom made.
I have bi-racial hair,
Combs run freely through my fine breezy, just to the
part, the most you can make,
Until it gets to the back and
Breaks.
I have bi-racial hair
Like-
The only thing my mother could put it in was 2 big
braids,
And sometimes that was to much,
So she left half undone.
I was in the mirror, I was in the mirror,
Convincing myself I looked just like a dark-skinned Alicia
Keys
I have bi-racial hair,
because I have bi-racial blood.
I’m not talking about that-cute they met then fell in
love, blood
I’m talking about that- slaved raped six times by the
master,
Birthing 6 mixed babies, later hung blood
I’m talking about that cross burning in the mud, blood
And you call me a mud blood,
Slit my wrist,
my blood does not excrete in black and white.
I dream in verse and in red
Like what drained from Emmett Tills’ lips when he was
killed for breaking down color lines
Bi-racial who succumbs to the abuse from her peers in
her middle school,
Those whose who constantly called me an Oreo
Well she’s not white, it’s more like Reese’s cookie, mixed
breed or a mulatto
That’s what it is a reverse mulatto
I AM NOT A F****** COOKIE OR A B****!
My roots are deep too
my bi-racial roots are not blind
or more than cotton soft
cause my blood were in the sun, picking cotton too
a thousand times desecrated for my race
a thousand time desecrated from my history y'all never
get
let textbooks be your truth
and sprinkle the ashes of your history into streams
I dream for a time and place where
maybe y'all all accept me
maybe we need to wake up again and remember a
morning of you
like something new
baby I'll be green cause my people drove there
you people drove me there
with my tender heart
tender head
and my bi-racial hair
```

---

## IC-1637: Multi-Cultural Collection

- Title: Multi-Cultural Collection
- Author (byline): Regie Cabico, Margaret Burroughs and Willie Perdomo
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1530
- Already set (do not supply): none

### Source block (context only)

```text
Author: Regie Cabico
Book: Returning a Borrowed Tongue
ISBN: 978-1566890434
Publisher: Coffee House
Date (Month/Year): 1995
Author: Margaret Burroughs
Book: Writing African American Women
ISBN: 978-0313331961
Publisher: Greenwood
Date (Month/Year): April 2006
2003 National Qualifier
Author: Willie Perdomo
Book: Where a Nickel Costs a Dime
ISBN: 9780393313833
Publisher: W.W. Norton and Company
Date (Month/Year): March 1996
Watch Willie Perdomo preform this poem at
https://www.youtube.com/watch?v=Mvo0g3dHAHw
```

### Introduction (context only: never use it for content warnings)

```text
Who can say what race a person belongs to strictly by his or her appearance? Labeling leads people to distinguish themselves from others based on a racial category. Why must we label people at all? Each person is different and possesses unique qualities. Check one race? How about The Human Race. This is a Collection on the concept of Race.
```

### Performance text (classify this)

```text
Check One by Regie Cabico

The Government asks me to "check one" if I
want money.
I just laugh in their face and say,
"How can you ask me to be one race?"

I stand proudly before you a fierce Filipino who knows how to belt hard-gospel songs played to African drums at a Catholic mass-and loving the music to suffering beats, and lashes from men's eyes on the capitol streets-

South-East D.C..., with its sleepy crime, my mother nursed patients from seven to nine, patients gray from the railroad riding past civil rights

I walked their tracks when I entertained them at the chapel and made their canes pillars of percussion to my heavy gospel-my comedy out-loud, laughing about, our shared, stolen experiences of the South.

Would it surprise you if I told you my blood was delivered from North off Portuguese vessels who gave me spiritual stones and the turn in my eyes-my father's name when they conquered the Pacific Isles. My hair is black and thick as "negrito," growing abundant as "sampaguita"-flowers defying civilization like pilipino pygmies that dance in the mountain.

I could give you an epic about my ways of life or my look and you want me to fill it in "one square box." From what integer or shape do you count existing identities, grant loans for the mind, or crayola white census sheets- There's no "one kind" to fill for anyone.

You tell me who I am, what gets the most money and I'll sing that song like a one-man caravan. I know arias from Naples, Tunis, and Accra-lullabyes from welfare, food-stamps, and nature

and you want me to sing one song? I have danced jigs with Jim Crow and shuffled my hips to a sonic guitar of Clapton and Hendrix, waltzed with dead lovers, skipped to bamboo sticks, belleted kabuki and mimed cathacali arrivedercied-a-rhumba and tapped Tin Pan Alley-and you want me to dance the Bhagavad Gita on a box to small for a thumbelina-thin diva?

I'll check "other"

TRANSITION In 1970, 1 in 100 babies born was multiracial; these days, that number has climbed to 1 in 10. By 2050, 1 in 5 Americans is expected to be multiracial. Why is this important? Because in America, multiracial individuals are always labeled as “non-white” – and in America today, it’s still a white man’s world. What Shall I Tell My Children who are Black by Margaret Burroughs.

What Shall I Tell My Children Who Are Black by Margaret Burroughs

What shall I tell my children who are black Of what it means to be a captive in this dark skin? What shall I tell my dear one, fruit of my womb, of how beautiful they are when everywhere they turn

they are faced with abhorrence of everything that is black. The night is black and so is the boogyman. Villains are black with black hearts.

A black cow gives no milk. A black hen lays no eggs. Storm clouds, black, black is evil and evil is black and devil’s food is black…

What shall I tell my dear ones raised in a white world A place where white has been made to represent all that is good and pure and fine and decent, where clouds are white and dolls, and heaven surely is a white, white place with angels robed in white, and cotton candy and ice cream and milk and ruffled Sunday dresses

and dream houses and long sleek Cadillacs and Angel’s food is white… all, all… white.

What can I say therefore, when my child Comes home in tears because a playmate

Has called him black, big lipped, flatnosed and nappy headed?

What will he think when I dry his tears and whisper, “Yes, that’s true. But no less beautiful and dear.” How shall I lift up his head, get him to square his shoulders, look his adversaries in the eye, confident in the knowledge of his worth. Serene under his sable skin and proud of his own beauty?

What can I do to give him strength That he may come through life’s adversities

As a whole human being unwarped and human in a world Of biased laws and inhuman practices, that he might Survive. And survive he must! For who knows? Perhaps this black child here bears the genius To discover the cure for… cancer

Or to chart the course for exploration of the universe. So, he must survive for the the good of all humanity.

He must and will survive. I have drunk deeply of late from the fountain of my black culture, sat at the knee of and learned from mother Africa, discovered the truth of my heritage. The truth, so often obscured and omitted. And I find I have much to say to my black children. I will lift up their heads in proud blackness with the story of their fathers and their father’s fathers. And I shall take them into a way back time of kings and queens who ruled the Nile, and measured the stars and discovered the laws of mathematics.

I will tell them of a black people upon whose backs have been built the wealth of three continents. I will tell him this and more. And knowledge of his heritage shall be his weapon and his armor;

It will make him strong enough to win any battle he may face. And since this story is so often obscured, I must sacrifice to find it for my children, even as I sacrifice to feed, clothe and shelter them.

So this I will do for them if I love them. None will do it for me.

I must find the truth of heritage for myself and pass it on to them.

In years to come, I believe because I have armed them with the truth, my children and their children’s children will venerate me. For it is the truth that will make us free!

TRANSITION In a climate currently riddled with anti-immigrant and anti- Latino rhetoric, people of mixed-race (black and Latino) face significant challenges as well. Afro-Latinos are often deemed too black for the Latino culture and not black enough for African Americans. Willie Perdomo explains in Nigger-Reecan Blues. I say again: Why must we label people at all? Check one race? How about The Human Race.

Nigger-Reecan Blues by Willie Perdomo *NOTE: a link to the video of Willie Perdomo performing this selection is included at the end of this file. Multiple characters are portrayed.

Hey, Willie. What are you, man? Boricua (a Puerto Rican, especially one living in the United States.) ? Moreno? (A Spanish term to refer to individual of dark skin tones) Que?

I am.

No, silly. You know what I mean: What are you?

I am you. You are me. We the same. Can’t you feel our veins drinking the same blood?

—But who said you was a Porta Reecan?
—Tú no eres Puerto Riqueño, brother.
—Maybe Indian like Gandhi Indian.
—I thought you was a Black man.
—Is one of your parents white?
—You sure you ain’t a mix of something like
—Portuguese and Chinese?
—Naaaahhhh…You ain’t no Porta Reecan.
—I keep telling you: The boy is a Black man with an
accent.

If you look closely you will see that your spirits are standing right next to our songs. Yo soy Boricua! You soy Africano! I ain’t lyin’. Pero mi pelo es kinky y kurly y mi skin no es negra pero it can pass…

—Hey, yo. I don’t care what you say—you Black.

I ain’t Black! Everytime I go downtown la madam blankeeta de madeeson avenue sees that I’m standing right next to her and she holds her purse just a bit tighter. I can’t even catch a taxi late at night and the newspapers say that if I’m not in front of a gun, chances are that I’ll be behind one. I won-der why…

—Cuz you Black, nigger.

I ain’t Black, man. I had a conversation with my professor. Went like this:

—Where are you from, Willie?

—I’m from Harlem.

—Ohh! Are you Black?

—No, but—

—Do you play much basketball?

Te lo estoy diciendo, brother. Ese hombre es un moreno! Míralo! Mira yo no soy moreno! I just come out of Jerry’s Den and the coconut spray off my new shape-up sails around the corner, up to the Harlem River and off to New Jersey. I’m lookin’ slim and I’m lookin’ trim and when my homeboy Davi saw me, he said: “Coño, Papo. Te parece como un moreno, brother. Word up, bro. You look like a stone black kid.”

—I told you—you was Black.

Damn! I ain’t even Black and here I am sufferin’ from the young Black man’s plight/the old white man’s burden/and I ain’t even Black, man/a Black man/I am not/Boricua I am/ain’t never really was/Black/like me…

—Leave that boy alone. He got the Nigger- Reecan Blues

I’m a Spic!
I’m a Nigger!
Spic! Spic! No different than a Nigger!
Neglected, rejected, oppressed, and depressed

From banana boats to tenements Street gangs to regiments… Spic! Spic! I ain’t nooooo different than a Nigger.
```

---

## IC-1638: The Museum of Broken Relationships

- Title: The Museum of Broken Relationships
- Author (byline): Andrea Gibson
- Work: You Better Be Lightning, Pg 10-15; 45; 104-105
- Publisher: Button Poetry
- Publication date as stated: Nov 2021
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 959
- Already set (do not supply): none

### Source block (context only)

```text
Author: Andrea Gibson
Book: You Better Be Lightning, Pg 10-15; 45; 104-105
ISBN: 978-1943735990
Publisher: Button Poetry
Date (Month/Year): Nov 2021
Visit the virtual museum at https://brokenships.com/
```

### Introduction (context only: never use it for content warnings)

```text
In 2006, Olinka Vistica & Drazen Grubisic created a communal space, a kind of refuge for – and cathartic celebration of – the everyday objects that had outlasted love. These items, along with the anonymous, intimate stories each piece represented, quickly captured hearts and imaginations across the globe. As word spread, the tiny museum became a worldwide sensation.

Today, you are invited to explore our ultimate need for love and connection despite the difficulties that go with it.

The Museum of Broken Relationships by Andrea Gibson
```

### Performance text (classify this)

```text
Museum of Broken Relationships

(Pg 10-15) In Croatia, in 2006, Olinka and Drazen broke up.
Having no idea what to do with the relics
from the four years of their love, they created
the Museum of Broken Relationships.

For years now they've been collecting items from the broken-hearted all over the world.

Each day, treasures arrive at the museum's door: a small bottle of a lover's tears.

The last checkbook with both partners' names.
A shiny watch with the pin pulled out
the second he said I love you for the first time.
In the Museum of Broken Relationships

there is a toaster. Beside it, a note:
When I moved across the country
I took the toaster. That will show you.
How are you going to toast anything now?

In another display there is a cell phone.
Written beside it, the words: He gave me
his own cell phone so I couldn't
call him anymore.

There is a letter T from a keyboard
from a couple whose online passion died
after their first real-life encounter.
The keyboard taken apart in a commitment

to never again trust a computer key
to open one's heart. In the Museum
of Broken Relationships, you can find a letter
from a thirteen-year-old boy to his first love in Sarajevo
written before leaving to escape the war.

You can find an air sickness bag from a couple whose relationship did not survive the turbulence of long distance.

You can find an ax used to chop the furniture of a partner who had an affair, giving new traumatic meaning to the phrase splitting up.

There is a jar of Love Incense with a note that says, It simply doesn't work.

And in the Museum of Broken Relationships in Croatia, there are three juggling balls sewn by hand,

by my hands, from material cut from my socks, you say, though I am certain

it was my underwear. Either way, the juggling balls were made from what I wore

underneath what everyone could see
and sewn with precision
the way my grandma taught me
before dying of a broken heart
and leaving me a collection of thimbles
so I couId be someone

strong enough to keep things from falling apart. The first time I saw you

I fell apart. I had no idea who you were. You walked into a studio l was in

and walked out. Minutes later I was a puddle in the parking lot,

my friend's hand on my back asking what was wrong. I couldn't explain it.

It was 2003. I had no woo-woo in me back then. I didn't believe

in reincarnation.
I just knew I'd loved you once
and would again. Months later,
still not knowing who you were,
I saw you on TV reporting the invasion
of Iraq, then the occupation of Palestine,

a blood fire in the sky above you and you not flinching, or I thought you weren't flinching

until we started sharing a bed and I could see the war behind your eyelids,

how you tore the covers off every morning like a kid unwrapping a gift.

Like the dawn of a simple day was everything you'd ever put on your Christmas list.

I'd still be sleeping when you'd leave for circus practice. Circus practice, where you'd walk the tightrope, twirl

on trapeze bars, then come home
and pull me into the front yard to teach me
how to toss juggling balls
into a still-blushing sky.
When I think about why we broke up,
why you flew all the way to Croatia

to let go of the juggling balls I made you, I know it's because I was a terrible juggler. I couldn't figure out how to hold something

and set it free at the same time. So I dropped the ball. Convinced myself I was up in the air about you

when really I was up in the air about me. It's what we do turn our bodies into museums of what was broken. Blame

the checkbook, the affair, the bottled up tears. Blame the toast going stale the day after the wedding.

We rip the letter off the keyboard instead of control, command, escape, delete. Say it was the turbulence

of long distance instead of the baggage unclaimed. But at the carousel of clarity (otherwise known as fifteen years of therapy).

I see I wasn't running from the war back then. I was running from the peace. The love I did not believe I was worth.

And because that lie held so much grief, I don't know that I ever got over you as much as I got under

the engine of myself to fix the machine of my love, which now runs okay

but still runs way too much, if you know what I mean, and I know you know what I mean,

because this was not the first lifetime we said goodbye without wanting to say goodbye,

was it?

Spelling Bee Without Stinger

(Pg 45) I love myself
is often spelled
g-o-o-d-b-y-e
See This Through

(Pg 104-105) My therapist has a theory about love. She says often we are believing a lie when we believe time is what helps us see each other more clearly. Says to consider the opposite might be true. Consider the beginning might actually be when our hearts have perfect vision.

What if what you saw then was the truth? Your holiest self seeing someone else’s holiest self? What if what came after was the lie? What if the disco ball never stopped sparkling, something just closed your eyes? Your past, maybe? The terror you carry inside? The not enough or too much that raised you to do everything you could to ensure you’d be hurt more than you’d be loved.
```

---

## IC-1639: Neferti-iti

- Title: Neferti-iti
- Author (byline): Ethyl Eichelberger
- Work: Extreme Exposure: An Anthology of Solo Performance Texts from the 20th Century
- Publisher: Theatre Communications Group
- Publication date as stated: February 1999
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2350
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ethyl Eichelberger
Book: Extreme Exposure: An Anthology of Solo
Performance Texts from the 20th Century
ISBN: 978-1559361552
Publisher: Theatre Communications Group
Date (Month/Year): February 1999
```

### Introduction (context only: never use it for content warnings)

```text
Nefertiti was the wife of the Egyptian Pharaoh Amenhotep IV (later Akhenaten), and mother-in-law of the Pharaoh Tutankhamun. Her name roughly translates to "the beautiful one is come". Famed throughout the ancient world for her outstanding beauty, Nefertiti remains the one of the most well known Queen of Egypt. Though Akhenaten had several wives, Queen Nefertiti was his chief wife. Nefertiti joined her husband in worship of a new religion that celebrated the power of the sun-disk Aten - a god of light. In this religion, she was a priest. Supposedly, It was only through the combined royal pair, that the full blessing of god Aten could be bestowed.

May I introduce you to the woman who was . . . . . Neferti-iti by Etyhl Eichelberger.

Ancient Egypt, Eighteenth Dynasty, inside the royal sunshade of Nefert-iti. The Egyptian queen has barricaded herself inside the tomb built for her by her husband Akhenaten. Her sisters and her lover, Bek, the artist who created the queen's famed bust, pay visits, yet remains locked outside the tomb.
```

### Performance text (classify this)

```text
Thank Aten I'm a beautiful woman!

Without that I'd have nothing, no one, nor my self-
respect!
(" Impassioned hormones" with a need to be expressed,
a professional woman,
a serious live-er of life!)
Quel joie to be alone each day here in this lovely
sunshade Akhenaten built me!
Today is different, though
All Egypt will regret!

(Laughter like the tinkling of bells is heard from offstage.) It's lovely here with no one telling me what to do! No one turning my priceless uniqueness into worthless guilt! Sometimes in this sunshade I have the distinct feeling I'm being watched, but I am alone here, you can see that!

(Knocking is heard on tomb door.) There is a knocking at my temple door-who could it be? I'll ignore the eager knock!

Go away, there's no one here! (Listens at door.) I won't go back to Memphis-I won't! You can't make me! Scarcity is valued, so value me-- I've made myself scarce! I'll keep right on praying to Aten, thank you. I'm too old to change! Time is running out! There just aren't enough hours in the day to worship all those other gods again! Besides, I've sworn my Ka to Aten, the one and only God, the god whose golden rays come streaming down to give me life!

(Knocking is again heard on tomb door.) Go 'way! No not Osiris; I won't let my beautiful body be shriveled into a dried-up image of Osiris Give me life, give me the globe, Aten; I have no need to be preserved forever, when I'm dead and gone they'll not forget me! "She passed like a meteor, leaving the world astonished and amazed!" (Knocking on door continues.) Stop that pounding and send for Bek- Have him make a bust of me, then carve my thoughts beneath it. And for Aten's sake make sure he carves my cartouche right this time; there is only one uraeus, not two! My dear, if Bek paid as much attention to his work as he did to his diet, something would get done around here! Tell me, what good are lazy people? Everybody has to work! I don't mind ... I love to work; the busier the better! Fill my life with work! But my father is a military genius, I've always been moderately wealthy and relatively unhappy -- could have spoiled me rotten, but he didn't- He cracked the whip at home and made us girls work! "People who don't work are bums," he taught us! "Bums!" What does he know? Who does he think he is anyway? The father of God! Casta diva ... Oh, Aten, make father Ay butt out of my life! He doesn't give me credit for anything!

I've had to claw my way to the sanctity of this
sunshade!
Isis knows it hasn't been easy!
It's a lot of hard work being a queen!
And there are factions out there who don't like what I
represent!
Tough noogies!
I have a right to be here!
Don't do that here!
"Don't be a queen," they say!
The kinder ones tell me that I transcend queenery-
They let me know they'll overlook my queenly failings
and benignly be so gracious as to accept me as one of
them.
It's true most people would rather queens should stay
under wraps, so to speak!
Hide!
Deny your feminine soul!
Being a queen frightens them!
But I am a queen, a beautiful one, at that!
I know who I am!

Ms. Marcia and I share the same madnessI have seen it in a dream! If my soul were to present itself to me within a miraculous vision, I would have that soul emblazoned on my back for all the world to see! (Knocking on tomb door starts again.) Quit pounding on that door! You're giving me a headache. I don't care if the Hittites are coming I won't come out! Oh, go on, I'm not afraid! They wouldn't dare come in here! I am safe here! This is a magic place! Aten will protect me ...

(More knocking on tomb door is heard.) What light, lovely knocking now! Mut-Nodjme, Honey, is that you, my sweet little sister? No, Dear-heart, I shan't come out again I've decided to refuge myself in here forever. Oooeee, what is that awful stench? Mut, Honey, have you got those stinking dwarves with you again?

I don't care if the Mitannia emperor did give them to
you, do you have to take them everywhere you go?
I will not shut up! I don't care if I hurt their little
feelings!
Let them hang around your sunshade!
Mut-Nodjme, don't go away mad!
Mut-Nodjme!
Gone!
Have a pleasant voyage back to Memphis!
I'll miss you, light of my life!
She's such a sweet girl -ambitious-
But she's nice, my little Nodjme!
Whoever followed me about and aped my ways!
Will I never ever see happy Mut-Nodjme?
She'll remember me kindly all her days!
I'm hot!
The Aten's globe has risen to its zenith! Now is the time
to pray! (Starts to play dulcimer and sing-stops.)
Merytaten should be here to shake her little sistrum
while I play-ah, children!!!
What can you do with them?

All she cares for is that foolish Smenkhare and his
vegetarian ways!
She'll be sorry!
Where is Meketaten now?
I miss her so! ... (pause.)
Oh, I won't let myself get started on that; not now!
This is a joyous day! I must think positive!
If Ankhesenpaten were here, she'd tell me a joke and
tickle her little Neferneferura!
Ah, three lovely children have I now,
even though three lovely more have died -three
daughters live while three have passed overthree out of
six-not bad,
could have been worse!
Praise be to Aten ... (plays dulcimer and sings.)
And here I sit alone-" I'm never bored!"
This must be what life is like to barren people,
disciples of Seth with never hope of having children-
actually, it's not so bad, I rather like having no one's
company but my own! (Picks up hand mirror and looks into
it.)

I know who I am-
you know who I am-
and then there is the real me who grins and hides from
sight!
Thank goodness I've brought clay tablets and senet
games!
I'll summon Thoth and write 'til day is done!
Thoth- Thoth(No response.) and here I sit alone!
Dear Aunt Tiye once told me:
"Being alone is not the worst thing in the world!" -But, it
is!!! Yes it is-
it's horrible=deplorable->
especially when the Aten begins his nightly journey
beneath the Nile!
Where are my lover's arms to hold me!
Oh for pity's sake!
I hereby choose to be alone-
I renounce my children; I have no children,
I renounce my husband; I have no husband
my belief in the Aten will sustain me-
l have my beliefs in one God to guide me! (Knocking on
tomb door starts again.)
Cease knocking-
I won't go back to Memphis, I won't; you can't make me!
There just aren't enough hours in the day to worship all
those other godsI am a student of the late Amenophis-
son-of-Hapu who has given me the strength to fight for
my
belief in Tiye, no, not "Inti," but "Aten!" (Listens at
tomb door.)
Who sighs beside my door and stirs the desert's
silence?
Is it you at last?
The sound of your voice awakens flowers in my heart!
Go away!
Do not tempt me!
Let me feel nothing once again!
Yes, I long to see you, hold you, give myself up to my
caged desires like I did when you first looked into my
eyes-
Do I make no sense?

I never asked you to understand me
Joy was mine when you but listened!
No, it is too late-our lives got in the way!
No, no! Of course I love you!
You are the divine father, my lover, the sacred
possessor of Min's phallic treasures!
Call me by my rightful name again and sing to me of
happiness, make hunger fly my aching heart!
I do not choose to hear them, Bek!
For me they do not exist!
While you stand close, all I can hear are fleet gazelle
and leopards screaming when the hounds have dragged
them down!
Oh bless you, simplicity becomes you,
it is I who am pretentious-
But you will always remain in my mind
if I may use your own words: "Pretentiously
unpretentious!"
All right, for Aten's sake, labels, labels, labels!
Forgive me, I've offended you again! ...
But we don't change, do we?

... Good-bye! ...
Yes, I'm telling you to go! Would you rob me of
my few remaining shreds of dignity!
Leave me, let me be! I was happy before I needed you!
No, I'm neither happy nor unhappy!
I try not to think about it anymore! I exist! ...
Of course I have survived!
There was nothing left inside me to destroy after you
had had your way ...
Oh, please don't leave just yet! ...
Yes, I do remember well! It was early morning!
I was gazing out upon the azure Nile when suddenly I
knew
this homely, snoring stranger lying next to me with beer
upon his breath was surely the greatest love of my life
and I would live forever needing him alone!
It made me violently depressed!
Somehow I felt short-changed, tricked, cheated.
Were you what I had lived for, hoped for, longed for all
my days?
Yee-gods! "What next," I thought! ...

Am I repeating myself again? Yes, yes, of course I would do anything! I won't go back to Memphis, I won't; you can't make me! No, I can't come out, I give myself to God. I no longer belong to your race! I have given myself up to the great Aten from whom I spring each morning when the sacred lotus blooms anew! Sometimes I truly wish with all my might that I were a human being instead of whatever it is I am! I can feel, I want to be like the rest! I have a right to some sort of life like other people. Bek, Dear-heart, it's just not that easy! Let myself fall in love again? With whom if not with you? Oh, a lovely thought-the maiden returning from the tryst with a functioning looney on her arm! And what could I offer him, sagging flesh and swollen eyes? Bek, Bek, you're most kind! Yes, they'll say I was a lost woman; only my bust was found!

That splendid bust!
Do you really still have it where it was?
Bek, what must your wife think?
If only life could imitate art!
If only it were true that truth is beauty!
I can speak true!
But if truth were beauty, more girls would get their hair
done at the library!
Yes, no, of course I've brought my mirror, what queen
would be without one?
All right, I'll look into it once again! Yes! Is that what
you have seen?
No! Must I say?
Bek, what I see couldn't turn a trick in Boy's Town!
No, I'm not being negative!
Go then, back to your wife and leave me be!
What do you need me for?
You can create alone! You are an artist!
Bek, I didn't mean it! Bek There is no key to let you in!
Please don't accuse me of being negative again!
I couldn't stand it! I am trying! I am trying!

I will be positive!
Oh, God, don't leave me again, Bek. I couldn't stand it to
be alone, abandoned!
Bek, talk to me! Say something!
Bek, Almighty Aten, bring him back! Bek!
Don't leave me here to die alone!
All right, I'm through.
You have won.
I don't believe in you-
Is that what you want me to say?
I curse you, I curse the name of the Aten.
I believe in nothing.
Strike me dead if you will! I don't believe in you!
There is no chance of everlasting life!
When I am dead, my detractors will erase my face and
name from every building, every tablet, every wall!
Bek will leave my image here to crumble into dust when
he goes back to Memphis!
The name of Nefert-iti will be gone forever! No one will
remember who I am!
I know what will be said:
"Who is Achenchae, Nefertiti who?" "I've never heard
of Akhenastae!
Who was she?"
Aten has tricked me! I believed in a calf of gold!
Hear me, Aten, I believe in you no more!
You are hateful!
You lied when in a blast of fire you told me you were
coming back to get me!
You have abandoned me! I hate you! I hate you!
Oh, why have you forsaken me?
What have I said? What does it matter?
Talk is cheap in the end Where is the Kohl to stain my
eyes?
Where is camel hair ground to bruise my lips?
There is no one left to help me! I must carry on alone?!
I have driven all away!
Once I had many friends and lovers, they are all gone
now; life goes on

(Drinks poison. Plays dulcimer and sings "The Song of Abandon.") Give me a sign, kind Aten! Send gentle spirits down to join my dance!

Is there no justice in the world? Must I accept what
comes my way?
No! I am fighting back!
There must be some sort of justice, even in Egypt!
I demand it!
I won't be thrown out the door like yesterday's dinner
to be eaten by crocodiles or hippopotami!
I must be worth more than that, I can still learn!
Hapu's son taught me to be forever a student!
To be learned is to be trained for a world already gone,
he said.
Change, change and more change!
It's happening fast-too fast!
Busy, busy, busy, but I'm never too busy to count my
assets!
That's rule #1 in business and I have assets, Aten, hear
me! I can work hard and long!
I can listen!
For a while, at least, I can be trusted!
I am a true friend to a few and kind to many
I can love,
I've been burned once too often! You are looking at
damaged goods!
I have been abandoned! I can't find my way! Aten, do
something! Help me! I beseech you!
I will not be ignored any longer!
Look at me!
Acknowledge me!
React or something
Give me a sign!
Aten! Aten! Aten!
I've had it! Hapu's son was wrong! Believe in the one
true God, he said and you will have everlasting life!

(Nefert-iti dies.)
```

---

## IC-1640: Next Life Soundtrack – A Program

- Title: Next Life Soundtrack – A Program
- Author (byline): Billy Joel, Buddy Wakefield and Terence Kawaja
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1215
- Already set (do not supply): none

### Source block (context only)

```text
Author: Billy Joel
Book: Storm Front, Pg 15-25
ISBN: 978-0793502615
Publisher: Hal Leonard Corporation
Date (Month/Year): April 1990
Author: Buddy Wakefield
Book: Learn then Burn 2: This Time It’s Personal
(Pg 69-73)
ISBN: 978-1938912504
Publisher: Write Bloody Publishing
Date (Month/Year): Jan 2015
Author: Terence Kawaja
ISBN: On-Line Transcript
Publisher: Youtube.com
Date (Month/Year): Nov 15, 2022
https://www.youtube.com/watch?v=Tnao981OyVw
* We Didn’t Start the Fire by Billy Joel
Music and Lyrics
https://www.youtube.com/watch?v=eFTLKWw542g
```

### Introduction (context only: never use it for content warnings)

```text
Artist Billy Joel said that the ultimate purpose of the song We Didn’t Start the Fire was to neither provide a complete account nor pass blame; what he really wanted to do was help young people realize that there are lessons in the past that might help us work through the present and plan for the future.

Buddy Wakefield takes that concept one step further and in reverse when he wrote: “Years from now, the enlightened civilization ahead of us will stare bewildered at our lethal masculinity and say, But each one, when he was running, tied bows to the top of his feet.” (From a Choir of Honest Killers)

Where do you live your life? In the past . . . the present . . . or with an eye on the future?

Next Life Soundtrack – A Program by Billy Joel, Buddy
```

### Performance text (classify this)

```text
We Didn’t Start the Fire by Billy Joel Birth control, Ho Chi Minh, Richard Nixon back again Moonshot, Woodstock, Watergate, punk rock Begin, Reagan, Palestine, terror on the airline Ayatollah's in Iran, Russians in Afghanistan

We didn't start the fire
It was always burning, since the world's been turning
We didn't start the fire
No, we didn't light it, but we tried to fight it . . .

Wakefield and Terence Kawaja

Next Life Soundtrack by Buddy Wakefield Having pumped panic buttons and pedal metal down the throats of freeways and crashed like heavy glass ashtrays into our own homes broadside with department store force and a gas can, distended stomachs and God's holes. . .

Having shown off our momentum for yawning
as a clever way to denigrate deeds of kindness. . .
Having created enough minimum wage faith
to distract orphans from the exit rows
then thrown holding pattern parties in their honor
only to present each other with our own names on gold
plaques bolted
to a fountain of toll booths used to dressed up up in our go
go
go and gone uninterrupted
by the signs that serve to encourage calming down,
it is good to know I have at least been loosening my grip on
the expectation
that our thumbs will necessarily oppose each other
in the next life.

There is a next life
and it is my understanding we will not necessarily
be binge-drinking bros
wearing Greek lamp shades paying for friendships
based on how our breath smells.
I will not necessarily find myself rationalizing with computer
gamers
and overly polite customer service robots
about how much life is lost on alternative realities
or how much violence peaceful consumers cause.
The results of our language cannot be programmed.
There is no proper way to hide the rampage with whom we
have been banking.
There are no words thick enough to conceal the
transparencies
in these stories we have crafted

out of loopholes and nothin' but net.

The next life is being offered to us daily
via live streaming satellite by entitled white rabbits and
tragedy addicts
dragging their
fingernail
file
cabinets
across records of the damage my nerves have done.
You inglorious preachers of a sensational game.

Sensations and games are at the root of why we are walking so inefficiently, warped 45's with credit card swagger charging up a sad sad path like Ray Charles singing Seven Spanish Angels to the bottom of the barrel in broad daylight. Stop congregating in the valley just because an echo sounds good when it agrees with itself A trajectory of misery -- at this point -- seems intentional. We have all the information we need to see clearly. We are no longer unaware toddlers on the landscape of consciousness. It is no longer cute to crap ourselves.

Get the sticky off your buns and roll with me.
Brush the hair from your eyes and comb over.
Stop paying the dentist for a night guard if it's still allowing
your jaw to
pulverize the truth.
The truth is: You feel fine, right now.

We are a point of complete, not a soundtrack to the next
life.
The future
gets no say in who we are.
Settle your debt and logout.
Thank you
for laughing at the joke several lines ago about sticky buns.
That was sweet. This is nuts.
Listen. . .

Having listened
to the parentheses of passive aggression
and made far too much bracket in response,
incriminating ourselves as sucker punches and suckerfish,
soaker hoses
and preying on the dead weight
of fashion-forward food for overpopulation,
having inflicted the most amount of pleasure with the least
harm done
then called it progress,
I am still, without fail, eligible to remind us that there is a
reason
the future gets so agitated by our advances.
We are not built to barge ahead of ourselves in false fast-
forward on a
flat fifth wheel made out of spokespeople for progress
who fly off the handle whenever anyone taps the breaks.
Throw it in park.

Gauge the pressure.
Renunciation is not a frigid concept.
It is okay to abandon the tackle practice
of having and crashing and having and crashing
through this circuit board of carrier pigeons carrying torch
carriers
over an orchestra of strung-out sixteenth notes
composed with a matchstick that struck out and broke off
but did not
burn up.
If the next life keeps finding us in these uncomfortable
positions
they might mistake us for honest.
How honest is it that we drink until we are dehydrated?
If my throat turns into carbonated leather
and you hang me like a lucky foot from the rearview mirror
while barreling down the freeway, toll booth after toll
booth, in a heavyglass ash tray, wondering how the hell
freeways got so expensive, remember this:

The White Rabbit is said to be a symbol of human beings who are pompous and belittling toward anything they deem less valuable than themselves, yet they grovel to accommodate anyone from whom they stand to gain. To what end are you gaining? I'm not speaking to our governments, I'm speaking to the way we govern ourselves. Make your stopwatch live up to its name. We are not late for an important date, we have simply shown up too early for the next life and forgot to knock, forgot that the future doesn't want us to arrive. It knows that if we do, it dies. As if people on stilts really need you to offer them more gravity.

TRANSITION

Baby Boomers considered “We Didn’t Start the Fire” a soundtrack documenting their lives. But what about Gen Xers, Millennials and Zoomers? Where's our soundtrack? Events are spiraling rapidly – Let’s take just a quick look at the year 2022.

We Didn't Start the Fire: 2022 EDITION by Terence Kawaja

Jeff Epstein, Uyghur mess, Fentanyl, COVID stress Royal hush, Metaverse, election lies keep getting worse Crypto scams, tech stock crash, Canadian truckers make a splash Lockdown driving us insane, trouble in Ukraine

Work from home, supply chain, Oscar slap, sanction pain Gender roles, Ukraine aid, say goodbye to Roe v. Wade Russian war, KBJ, Fed rate hikes, don’t say gay Putin bash, Uvalde, tourists on a travel spree

Saudi golf, streaming ads, Latins voting for comrades Pipeline bomb, Chairman Xi, Tim Cook says it’s privacy Chip wars, antitrust, Greg Norman, Elon Musk $5 buck gas, going green?, Britain loses its loved Queen

Interest rates, crypto pain, web3 mania insane Recession fears, SPACs don’t work, Boris such a Tory jerk World War 3?, Taiwan threats, Rocketman, hijab protests Lettuce wins, Elon’s sink, democracy at the brink

Kanye hate, election lies, tech layoffs on the rise
Russians lose, Bannon jail, Elon’s Twitter product fail
Crypto crash, FTX, US young men get no sex
Lula wins, trade dispute, MAGA Trumpists get the boot

Billy Joel’s 80s song covered issues decades long This parody so true only cites 2022 More change is on the way, consternation’s here to stay Election 2024, I swear I can’t take any more Billy Joel Reprieve (Singing) We didn't start the fire It was always burning, since the world's been turning We didn't start the fire But when we are gone It will still burn on, and on, and on, and on, and on, and on, and on, and on
```
