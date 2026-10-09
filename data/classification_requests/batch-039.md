# Classification request: batch 39 of 53 (40 records, IC-1921 to IC-1960)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-039-reply.json`.

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

## IC-1921: The Seven Stage a Comeback

- Title: The Seven Stage a Comeback
- Author (byline): Gregory Maguire
- Work: Not specified
- Publisher: Aladdin
- Publication date as stated: Nov 2001
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1497
- Already set (do not supply): none

### Source block (context only)

```text
Author: Gregory Maguire
Found in: A Wolf at the Door
ISBN: 978-0689821394
Publisher: Aladdin
Date (Month/Year): Nov 2001
```

### Introduction (context only: never use it for content warnings)

```text
(SING) Hi Ho! Hi Ho! It’s off to work we go . . . . . SNOW WHITE: Reminds me of a dream I must have had. As if I had lived somewhere else, once upon a time. I never did, of course. I was always here, awake, and in my life. Smiling as if the happily ever after of stories begins right now, at the very start of life.

For you see, Snow White went on to have her happily ever after. But what about her saviors: Dopey, Doc, Happy, Sleepy, Sneezy, Bashful and Grumpy? How did they feel when Snow White left them high and dry . . . after all they’d done for her. . . I think it’s time for The Seven to Stage a Comeback by Gregory Maguire.
```

### Performance text (classify this)

```text
1: The man with the crazed expression
Clawed open her coffin,
Kissed her awake,
And carried her off.
There goes our lovely daughter.
All we have left of her
Is the apple that tumbled from her lips
And the glass box we nested her in.

2: We’re better off without her.
Wasn’t she always on us about something?
“Hasn’t anyone ever heard of a thing called soap?”
“I don’t trust little men with beards.”
And then with the signs.
The expressive eyes.
Followed by floods of agitated song.
Frankly, when she ate that poisoned apple –
Oh, yes, I was sad, I cried –
But you want to know what else?
I thought: At last. A little peace and quiet
around here.

3: So why are your eyes all rimmed with red? You loved her as we all did. Or did you just like having someone to complain about?

4: And all that’s left is the apple and the coffin. What could we do? Put the bit of the apple in the glass coffin And close it up again? The coffin keeps things pretty fresh. And for a good, long time, too, it seems. You never know when we’ll need a bit of poison apple again.

5: Let’s take the coffin on our backs And wander o’er the mountain tracks. Sing ho! For the life of a dwarf.

6: This isn’t the time for singing.
But it’s not a bad idea.
Let’s get this baby home.
All together now, on a count of three –
One, two – alley-oop and upsy-daisy.
You, carry the iron-head hammer.
And stop with that racket.

7: Ohhhhhhh, ohhhhhhhh, ohhhhhhh, ohhhhhhhh, ohhhhhhhhh, ohhhhhhhhh

************************************

1: We find an orphan girl, we take her in. Locate some moldy blankets to keep her warm. Porridge in the morning, porridge in the evening. A little dwarf folk music to cheer her up. It was a humble life, but it was ours, And freely we gave it to her. No wonder we’re still upset. No wonder we can’t focus. We have to shape up. We’re falling to pieces here

2: Easy come, easy go. We’re better off without her.

3: You are the one who speaks with the sharpest tongue, But you’re the one who moans her name in your sleep. Face it. We all miss her. When’s the last time any one of us laughed out loud? We don’t manage to do what we should. We never go out with our iron-head hammer To bash the jewels out of secret caves. But what can we do?

4: We could go find her where she is.
We could beg her to come back.
We could bring the glass coffin.
We could lay her where she was.

5: Let’s take the coffin on our backs Sing ho! For the life of a dwarf.

6: Please, would you stop your singing, please? Though I’m not one for kidnapping old friends, She did leave us high and dry.

She married that traveling prince. They could be nine kingdoms away by now. But I’m a one for marching impressively off a cliff. Better than sitting around with tears in our beards! Let me hunt for a map, a compass. We need cloaks, and staffs, and gumption. Somebody grab the iron-head hammer, Somebody bring the silver guitar. You, are you weeping again, you fool?

7: Ohhhhh, ohhhh, ohhhhh, ohhhhh, ohhhhh, ohhhhh

*********************

1: Good-bye to the house in the autumn woods There’s no life left for us at home. This little house, this moldy tomb – the grave and marker Of what we lost when she went away.

Now hoist the coffin on your backs, And off we go.

2: We’re better off without her. We’re better off without her.

3: So you say.
But you walk faster than the rest of us.
It never was to come to this
We took her in when she was lost,
But then we lost her in our turn.
And are we losing ourselves as well?

4: We’ll find our beauty where she rests, And coax her home. What’s wrong with that? The least she owes us is a little loyalty. She never should have eaten the apple, one, Nor, two, attracted the first available prince. Ours is not to harm or hurt her. Just to keep her safely with us.

5: We have the coffin on our backs Sing ho! For the life of a dwarf.

6: You, are you weeping again, you fool?

7: Ohhh, ohhhh, ohhhhh, ohhhhhh

*******************************

1: We’ll cross this rushing icy mountain stream. Don’t drop the coffin into the flood, For there it would sink, and clear as light, We’d search in vain and never see it. Steady your feet, and steady your hearts.

2: We’re better off without her.
But should we come across her . . .
I’ll be the one to ask her.
How she could ever leave use.
I’ll laugh at any answer.

We’re better off without her.

3: We arent’ her abductors.
Just friends who com a-calling.
We’ll ask her to rejoin us.
The coffin waits.

4: The coffin waits.

5: Sing ho! For the life of a dwarf

6: I fear what we’re about.
I cannot stop.
We are bewitched; no more, no less.
Her beauty calls us, and we can’t escape.

7: Ohhhh, ohhhhh, ohhhhh

************************

1: Here in the inn-yard, huddled about a fire, Today we learn that the girl we seek Lives just beyond the ridge, in a noble home. No dragons to guard the moat, no spells to break. No soldiers lurking upon the singled roofs. Nothing to stop us from going the final steps. Here we’ll commit what crime we may, And live to rue, or praise the day.

7: Ohhhh, ohhhhh, ohhhhh

2: We’re better off without her.
Let’s give her the poisoned sleep
And lock her within her windows.
What’s dead cannot live to leave us again.
We love her too much to allow her to live.

7: Oh, oh, oh, oh 3: We’re smaller than human men, with smaller hearts. We aren’t built to know what’s right or wrong. We’re hardly more than pagan animals. We met her when she was young, we took her in, As much to serve us at our filthy home As out of any wish to do charity. Let’s finish the job we started, and shed no tears For being smaller creatures than we’d like. Up to the mansion, then, to take her back. There to cherish her incorruptible corpse.

7: Oh, oh, oh

4: The apple awaits to do it lethal job. The glassy walls of the coffin are polished clear, Its hinges oiled silent by dwarfish spit.

5: Let’s lift the coffin from our backs And see what sleeper it attracts.

Sing ho! For the life of a dwarf.

*********************************

1: There she sits, in an orchard of apple trees. Who could have thought she would be more beautiful Than memory could picture?

2: We’re better off without – we’re better off – we’re better

3: Hush, lest she hears us before we make our approach. See how her smile blossoms; she looks aside, Shyly, at mending collected inside the basket That rests in the fragrant grass near her pretty feet.

4: She always loved the household task. She sang when she worked.

Who can forget her voice?

5: Sing ho, sing ho, sing ho, Off with the girl and away we go.

6: She smiles upon the laundry with radiant look, She stirs the cloth as if something lies gently within, A bruisable apple, a blossom, a porcelain toy. Now is the time. There is nobody else around. At the count of three, we leap from these thickets, see, Surround her – confound her – accuse her – reclaim her – One – two –

7: Three Is the number we never expected to see. Yes, you will listen, all of you! Hear me out. It is not just the prince and the princess we disturb.

That basket of washing is laughing at its mother. There is a child within. Are you wholly blind? I’ll swing this iron-head hammer at your skulls. I’ll smash the coffin seven directions to heaven. Dwarfish mischief we make, and dwarfish music, But mischief and music never come closer together Than in the laugh of an infant adoring its mother.

3: We come to see what loneliness is worth; It bring new life upon the ancient earth.

4: We smash the coffin of your former days Seeing the happiness that spills in your gaze.

5: No coffin is left to life upon our backs And carry home along the mountain tracks. Sing ho! For the life of a dwarf.

6: No standing in splintered glass, in scented grass, We sing you all our love, before we pass.

7: All of us loved her as much as we could grieve. As hard as we could do, each in our way. Now hand me the silver guitar, and I will play Hi Hooooooo, Hi Hooooooooo.
```

---

## IC-1922: Song and Dance

- Title: Song and Dance
- Author (byline): Alan Shapiro
- Work: Not specified
- Publisher: Houghton Mifflin
- Publication date as stated: Feb 2002
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1164
- Already set (do not supply): none

### Source block (context only)

```text
Author: Alan Shapiro
ISBN: 978-0618152858
Publisher: Houghton Mifflin
Date (Month/Year): Feb 2002
```

### Introduction (context only: never use it for content warnings)

```text
Ranging through memories old and recent, factual and imagined, Alan Shapiro celebrates his brother, David, a song-and-dance man diagnosed with inoperable brain cancer. All poems are from Shapiro’s collection Song and Dance . . . The opening poem portrays the brothers as children, lip-synching and step-kicking to an Ethel Merman record for their parents. Everything the Traffic will allow by Alan Shapiro. In the next selection “Sleet” both his father and mother are remembered.
```

### Performance text (classify this)

```text
Everything the Traffic Will Allow

The two boys don’t suspect

they don’t exist. And Ethel Merman is

the shade of a shade – what Plato says

all poetry is –

a record spinning beneath

a needle

as the boys lip-sync into

imaginary mikes her glottal swagger,

brassy, large,

streetwise and from their mouths

so touchingly naïve for being so . . .

There’s no

people

like show

people . . . . Their parents clap

and whistle

from the bed, propped up

on pillows . . .

Everything about it is appealing . . .

They are shouting “Encore! Bravo!”

when the boys,

like chorus girls, arms on each other’s shoulders,

step-kid their way across the room

and out of it,

then back . . . stealing that extra bow . . . .

Shades of a shade. What poetry is.

Because there’s nowhere else for them to be

except

inside the room in which it isn’t

when it is,

in which there is no room

uUnless I think of it – the boys

their arms flung wide

on one knee mouthing the last words

before the needle slides off into silence,

the parents propped up

on pillows, half laughing, half

shouting “Bravo!

Encore!”

All now just the shade

of a shade –

like no

people

I know . . .

Sleet

What was it like before the doctor got there?

Till then, we were in the back seat of the warm dark bubble of the old Buick. We were where we’d never not been, no matter where we were.

And when the doctor got there?

Everything outside was in a rage of wind and sleet, we were children, brothers, safe in the back seat, for once not fighting, just listening, watching the storm.

Weren’t you afraid that something bad might happen?

Our father held the wheel with just two fingers even though the car skidded and fishtailed and the chains clanged raggedly over ice and asphalt.

Weren’t you afraid at all?

Dad sang for someone to fly him to the moon, to let him play among the stars, while Mom held up the lighter to another Marlboro.

But when the doctor started speaking. . .

The tip of the Marlboro was a bright red star. Her lips pursed and she released a ring of Saturn, which dissolved as we caught at it, as my dad sang Mars.

When you realized what the doctor was saying. . .

They were closer to the storm in the front seat. The high beams, weak as steam against the walled swirling, only illuminated what we couldn’t see.

When he described it, the tumor in the brain and what it meant. . .

See, we were children. Then we weren’t. Or my brother wasn’t He was driving now, he gripped the steering wheel with both hands and stared hard at the panicked wipers.

What did you feel?

Just sleet, the slick road, the car going way too fast, no brother beside me in the back seat, no singing father, no mother, no ring of Saturn to catch at as it floats.

TRANSITION

The accident that doesn’t happen in the childhood memory of “Sleet” happens in “The Accident” which juxtaposes the intense physicality of a hummingbird and the consolations of song with the accident of the poem’s title—a nurse dropping a physically fading David in the bathroom.

The Accident

While it was happening,

the absolute not me of it, the all

of a sudden see-through whir of wings beside me

that the late sun just as I looked up

turned to a hovering flash, a watery gray—

green iridescence as the beak dipped into

a funnel of blossom, dipped and was gone, and not even

the blossom's white tip bent in its going,

or shivered—

While this, which could have happened

without me, here or elsewhere, happened the way

it did, and would continue happening

for others, for no one, for nothing but the blind urge

of its happening, this ever-transient

accidental crossing of momentums

that was, in this case, beautiful but could

have not been and so seemed all the more consoling

for the thought—

even the thought of death,

just then, consoling, shaping itself inside me

as the now there now not there hovering

of bird, flower, late sun iridescences—

beloved singers, you who in the aftermath

surged from the shadows to sing in your different voices

the same song, Route of evanescence, Mother

of beauty, It avails not, time nor place,

distance avails not,

if you had known, just then,

three hundred miles away, in another state,

that one of the nurses getting my brother up

from the commode and back to bed, the one

who held him on his left side, the dead side,

all of a sudden lost hold of him and, as

he fell hard, grabbed for the loose papery gown

and ripped it off, so that he lay there naked,

utterly exposed—

beloved singers, tricksters

of solace, if you had known this, seen

this, as I did not, you would have offered him

no sumptuous destitution, no fire-

fangled feathers, or blab about death as being

luckier than one supposes. You would have bowed

your heads, you would have silently slipped back

into the shadows out of which you surged forth,

singing to me.

TRANSITION

Song and Dance is much more than a collection about a brother’s death; it is a story of family and memory, a song for a sibling’s life. The final selection shares the collection’s title Song and Dance by Alan Shapiro

Song and Dance

Did you ever have a family?

Dark dining room,

bright kitchen,

white steam
from the big pot my mother’s stirring
reaching in wavy tendrils to her face,
around her face, all the way around
to me at the table, then beyond me
into the darkness where my brother is.

Were you ever a child?

I’m hungry but I know we’ll

eat soon,

so even the hunger’s sweet.

Did you ever really have a brother?

He’s singing there in the dark

corner

beside the stereo,
the volume turned down so low
all we hear is him, his voice, and
his eyes are closed so that there’s
nothing around him anywhere
that might reveal he isn’t
who the song insists he is.

And that is?

Irresistible, unforgettable,

someone

to whom
as in imaginary gardens
where “the nectarine and curious
peach into my hands themselves
do reach,” love comes as soon
as called, comes just as dreamed.

Did any of this ever happen?

The hunger’s sweet,

it’s as if

the song weaves
through the fragrance of the braiding
steam from him to me to her
to me to him because her eyes
are closed now too; her
slippered feet tap, caper
a soft shoe while the ladle
sways in her hand as she stirs.

Were you ever a child?

I know I’ll eat soon.

Did you ever really have a brother? You should have

heard him,

his voice was
unforgettable, irresistible, his voice
was an imaginary garden woven through with
fragrance.

Did you ever have a family?

Their eyes are closed. That’s how I know
```

---

## IC-1923: Spade from John Brown’s Body

- Title: Spade from John Brown’s Body
- Author (byline): Stephen Vincent Benet
- Work: John Brown’s Body
- Publisher: Buccaneer Books
- Publication date as stated: Aug 1986
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 558
- Already set (do not supply): none

### Source block (context only)

```text
Author: Stephen Vincent Benet
Book: John Brown’s Body
ISBN: 978-0899664057
Publisher: Buccaneer Books
Date (Month/Year): Aug 1986
```

### Introduction (context only: never use it for content warnings)

```text
Spade is a slave who escapes to freedom and characterizes traits of the common people that Benet so admires, people who suffered, fought, and died to bring about a new birth of American freedom. Benet treats them all with honor and respects the choices they made. Spade from John Brown’s Body by Stephen Vincent Benet
```

### Performance text (classify this)

```text
The slave got away from Zachary's place that night. He was a big fellow named Spade with one cropped ear. He had splay feet and sometimes walked with a limp. His back was scarred. He was black as a pine at night. He'd tried to run away a couple of times --That was how he got some of the marks you could tell him by-- But he'd been pretty quiet now for a year or so And they thought he had settled down.

When he got away He meant to kill Zachary first but the signs weren't right. He talked to the knife but the knife didn't sweat or heat, So he just got away instead.

When he reached the woods And was all alone, he was pretty scared for a while, But he kept on going all night by the big soft stars, Loping as fast as he could on his long splay feet And when morning broke, he knew he was safe for a time.

He came out on a cleared place, then. He saw the red Sun spill over the trees.

He threw his pack
Down on the ground and started to laugh and laugh,
"Spade, boy, Spade, you's lucky to git dis far.
You never managed to git dis far before,
De Lawd's sho'ly with you, Spade."

He ate and drank. He drew a circle for Zachary's face in the ground And spat in the circle. Then he thought of his woman. "She's sho'ly a grievin' woman dis mawnin', Spade." The thought made him sad at first, but he soon cheered up. "She'll do all right as soon as she's thu with grievin'. Grievin' yaller gals always does all right. Next time I'se gwine to git me a coal-black gal. I'se tired of persimmon-skins.

I'se gwine to break loose. De signs is right dis time. I'se gwine to be free, Free in de Norf."

He saw himself in the North. He had a stovepipe hat and a coal-black gal.

He had a white-folks' house and a regular mule. He worked for money and nobody ever owned him. He got religion and dollars and lucky dice And everybody he passed in the white folks' street Said "Good mawnin', Mr. Spade--Mr. Spade, good mawnin'." He chuckled aloud. "Good mawnin', Mistuh Spade, Gwine to be free, Mistuh Spade--yes, suh, Mistuh Spade!" For a lazy moment, he was already there-- Then he stiffened, nostrils flaring, at a slight sound. It couldn't be dogs already.

"Jesus," he whispered,
"Sweet, lovin' Jesus, don't let 'em git me again,
Burn me up, but don't let 'em git me again,
Dey's gwine to cut me apart."

The rabbit ran past. He stared at it for a moment with wild, round eyes, Started a yell of laughter--and choked it off. "Dat ain't no nachul rabbit dere, Spade, boy. Dat's a sign. Yes, suh. You better start makin' tracks. Take your foot in your hand, Mistuh Spade."

He swung the bundle Up on his shoulders and slid along through the trees. The bundle was light. He was going to be hungry soon And the big splay feet would soon be bleeding and sore, But, as he went, he shook with uncanny chuckles. "Good mawnin', Mr. Spade--glad to see you dis mawnin'! How's Mrs. Spade, Mr. Spade?"
```

---

## IC-1924: Storm

- Title: Storm
- Author (byline): Tim Minchin
- Work: Not specified
- Publisher: Laughing Stock Productions
- Publication date as stated: 2009
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1446
- Already set (do not supply): none

### Source block (context only)

```text
Author: Tim Minchin
Book/CD: Ready for This?
ISBN: B002X2ZMHO
Publisher: Laughing Stock Productions
Date (Month/Year): 2009
NOTE: Only published in CD Audio Format. Check
requirements in your state for “publication” rules before
performing.
```

### Introduction (context only: never use it for content warnings)

```text
Being a hippie is not a matter of dress, behavior, economic or social status. It is a philosophical approach to life that emphasizes freedom, peace, love and a respect for others and the earth. The way of the hippie never died. There have always been hippies from the first time society laid down rules, to Jesus, to Henry David Thoreau, to John Lennon, to you and me. I believe there’s a little hippy in all of us. It’s just been repressed by our socialization process. We need to find it and cultivate our hippie within. Only then can we reach our true potential. Here is your first lesson: Memorize these quotes from great men, and use them as mantras for your life. "Give peace a chance"~ John Lennon "We must learn to live as brothers, or parish as fools"~ Martin Luther King Jr. "What shall it profit a man if he gains the whole world, but loses his soul?"~Jesus Christ

But in the meantime, let me introduce you to Storm by Tim Minchin
```

### Performance text (classify this)

```text
Inner North London, top floor flat
All white walls, white carpet, white cat,
Rice Paper partitions
Modern art and ambition
The host’s a physician,
Lovely bloke, has his own practice
His girlfriend’s an actress
An old mate from home
And they’re always great fun.
So to dinner we’ve come.

The fifth guest is an unknown,
The hosts have just thrown
Us together for a favor
because this girl’s just arrived from Australia
And has moved to North London
And she’s the sister of someone
Or has some connection.
As we make introductions
I’m struck by her beauty
She’s irrefutably fair
With dark eyes and dark hair
But as she sits
I admit I’m a little bit wary
because I notice the tip of the wing of a fairy
Tattooed on that popular area
Just above the derrière
And when she says “I’m Sagittarian”
I confess a pigeonhole starts to form
And is immediately filled with pigeon
When she says her name is Storm.
Chatter is initially bright and light-hearted
But it’s not long before Storm gets started:
“You can’t know anything,
Knowledge is merely opinion”
She opines, over her Cabernet Sauvignon
Vis-à-vis,
Some un-hippily
Empirical comment by me
“Not a good start” I think
We’re only on pre-dinner drinks
And across the room, my wife
Widens her eyes
Silently begs me, Be Nice
A matrimonial warning
Not worth ignoring
So I resist the urge to ask Storm
Whether knowledge is so loose-weave
Of a morning
When deciding whether to leave
Her apartment by the front door
Or a window on the second floor.
The food is delicious and Storm,
Whilst avoiding all meat
Happily sits and eats
While the good doctor,
Holds court on some anachronistic aspect of medical
history
When Storm suddenly she insists
“But the human body is a mystery!
Science just falls in a hole
When it tries to explain the nature of the soul.”
My hostess throws me a glance
She, like my wife, knows there’s a chance
That I’ll be off on one of my rants
But my lips are sealed.
I just want to enjoy my meal
And although Storm is starting to get my goat
I have no intention of rocking the boat,
Although it’s becoming a bit of a wrestle
Because -- like her meteorological namesake -
Storm has no such concerns for our vessel:
“Pharmaceutical companies are the enemy
They promote drug dependency
At the cost of the natural remedies
That are all our bodies need
They are immoral and driven by greed.
Why take drugs
When herbs can solve it?
Why use chemicals
When homeopathic solvents
Can resolve it?
It’s time we all return-to-live
With natural medical alternatives.”
And try as hard as I like,
A small crack appears
In my diplomacy-dike.
“By definition”, I begin
“Alternative Medicine”, I continue
“Has either not been proved to work,
Or been proved not to work.
You know what they call “alternative medicine”
That’s been proved to work?
Medicine.”
“So you don’t believe
In ANY Natural remedies?”
“On the contrary actually:
Before we came to tea,
I took a natural remedy
Derived from the bark of a willow tree
A painkiller that’s virtually side-effect free
It’s got a weird name,
Darling, what was it again?
Masprin?
Basprin?
Asprin!
Which I paid about a buck for
Down at my local drugstore.
The debate briefly abates
As our hosts collects plates
but as they return with desserts
Storm pertly asserts,
“Shakespeare said it first:
There are more things in heaven and earth
Than exist in your philosophy…
Science is just how we’re trained to look at reality,
It can’t explain love or spirituality.
How does science explain psychics?
Auras; the afterlife; the power of prayer?”
I’m becoming aware
That I’m staring,
I’m like a rabbit suddenly trapped
In the blinding headlights of vacuous crap.
Maybe it’s the Hamlet she just mis-quothed
Or the eighth glass of wine I just quaffed
But my diplomacy dike groans
And the arsehole held back by its stones
Can be held back no more:
“Look , Storm, I don’t mean to bore you
But there’s no such thing as an aura!
Reading Auras is like reading minds
Or star-signs or tea-leaves or meridian lines
These people aren’t plying a skill,
They are either lying or mentally ill.
Same goes for those who claim to hear God’s demands
And Spiritual healers who think they have magic hands.
By the way,
Why is it OK
For people to pretend they can talk to the dead?
Is it not totally fucked in the head
Lying to some crying woman whose child has died
And telling her you’re in touch with the other side?
That’s just fundamentally sick
Do we need to clarify that there’s no such thing as a
psychic?
What, are we fucking 2?
Do we actually think that Horton Heard a Who?
Do we still think that Santa brings us gifts?
That Michael Jackson hasn’t had facelifts?
Are we still so stunned by circus tricks
That we think that the dead would
Wanna talk to pricks
Like John Edward?
Storm to her credit despite my derision
Keeps firing off clichés with startling precision
Like a sniper using bollocks for ammunition
“You’re so sure of your position
But you’re just closed-minded
I think you’ll find
Your faith in Science and Tests
Is just as blind
As the faith of any fundamentalist”
“Hm that’s a good point, let me think for a bit
Oh wait, my mistake.
Science adjusts its beliefs based on what’s observed
Faith is the denial of observation so that Belief can be
preserved.
If you show me
That, say, homeopathy works,
Then I will change my mind
I’ll spin on a dime
I’ll be embarrassed as hell,
But I will run through the streets yelling
It’s a miracle! Take physics and bin it!
Water has memory!
And while it’s memory of a long lost drop of onion juice is
Infinite
It somehow forgets all the poo it’s had in it!
You show me that it works and how it works
And when I’ve recovered from the shock
I will take a compass and carve Fancy That on the side
of my cock.”
Everyone’s just staring at me now,
But I’m pretty pissed and I’ve dug this far down,
So I figure, in for penny, in for a pound:
“Life is full of mysteries, yeah,
But there are answers out there
And they won’t be found
By people sitting around
Looking serious
And saying isn’t life mysterious?
Let’s sit here and hope
Let’s call up the Pope
Let’s go watch Oprah
Interview Deepak Chopra
If you’re going to watch tele, you should watch Scooby
Doo.
That show was so cool
because every time there’s a church with a ghoul
Or a ghost in a school
They looked beneath the mask and what was inside?
The janitor or the dude who runs the water-slide.
Throughout history
Every mystery
EVER solved has turned out to be
Not Magic.
Does the idea that there might be truth
Frighten you?
Does the idea that one afternoon
On Wikipedia might enlighten you
Frighten you?
Does the notion that there may not be a supernatural
So blow your hippy noodle
That you would rather just stand in the fog
Of your inability to Google?
Isn’t this enough?
Just this world?
Just this beautiful, complex
Wonderfully unfathomable world?
How does it so fail to hold our attention
That we have to diminish it with the invention
Of cheap, man-made Myths and Monsters?
If you’re so into Shakespeare
Lend me your ear:
“To gild refined gold, to paint the lily,
To throw perfume on the violet… is just silly”
Or something like that.
Or what about Satchmo?!
I see trees of Green,
Red roses too,
And fine, if you wish to
Glorify Krishna and Vishnu
In a post-colonial, condescending
Bottled-up and labeled kind of way
That’s ok.
I am a tiny, insignificant, ignorant lump of carbon.
I have one life, and it is short
And unimportant…
But thanks to recent scientific advances
I get to live twice as long as my great great great great
uncles and auntses.
Twice as long to live this life of mine
Twice as long to love this wife of mine
Twice as many years of friends and wine
Of sharing curries and getting shitty
With good-looking hippies
With fairies on their spines
And if perchance I have offended
Think but this and all is mended:
We’d as well be 10 minutes back in time,
For all the chance you’ll change your mind.
```

---

## IC-1925: Superman in the Nursing Home/Dear Superman

- Title: Superman in the Nursing Home/Dear Superman
- Author (byline): Rusty Russell and Ron Koertge
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 720
- Already set (do not supply): none

### Source block (context only)

```text
Author: Rusty Russell
Book: Poetry Slam: The Competitive Art of Performance
Poetry (ed Gary Mex Glazner)
ISBN: 978-0916397661
Publisher: Manic D Press
Date: Sept 2000
Author: Ron Koertge
Book: Geography of the Forehead
ISBN: 978-1557286116
Publisher: The University of Arkansas Press
Date: Nov 2000
```

### Introduction (context only: never use it for content warnings)

```text
Superhuman strength. Invulnerability. Motivation to defend the world from evildoers. A secret identity. AND the ability to look good in long underwear. These are the traits that define the true superhero: Batman, Captain America, Captain Marvel, Spider-Man (gradually look up into the sky during this phrase, then point and get really excited . . . . ) Faster than a speeding bullet! More powerful than a locomotive! Able to leap tall buildings in a single bound! LOOK! Up In The Sky! It's a bird! It's a plane! It's SUPERMAN!

How serious a subject matter is Superman? Serious enough for poetry to be based on him. Today I want you to meet the man inside the super hero: Clark Kent or Superman in the Nursing Home by Rusty Russell
```

### Performance text (classify this)

```text
Superman in the Nursing Home
It started with the flying.
I just had to get away.
I thought I was going crazy, hearing things –
voices, sirens, water running behind walls,
and the crying, someone always crying behind closed
doors.
It was that super hearing. I had it then.
So some nights I'd fly out of the city
until I couldn't hear them anymore,
way out over the ocean where I could see the earth
turning
and the sun rising over the edge of the next day.
Miraculous, made me feel like the only man on earth,
but I wasn't a man. I was a freak.
Then came all those years
of changing clothes in dirty phone booths;
chewing gum on the floor getting stuck in my pants,
cigarette butts, and the smell of winos and urine.
Sometimes the phone would ring while I was in there
and it always gave me the creeps.
Think about it – an anonymous telephone
in the middle of the night on a deserted street
and it's ringing for someone. Anyone.
I never picked it up. I didn't want to hear it –
lives pulled thin over a phone wire,
stories of pockets with holes,
bad breath whistling through bad teeth.
What could I do?
Someone sobbing and sloppy drunk in a bar somewhere
picks up a phone, dials a number at random
and gets Superman
with his pants down in a phone booth.

Believe it or not, this Superman thing started out
modestly:
no cape, no tights.
Just lifting automobiles off trapped motorists,
or catching falling babies before they hit the sidewalk.
But it felt so good, the applause,
the way the Earth girls looked at me,
and it all got out of hand.
I should have stopped after the first bank robbery.
There would never be any cash reward in this
for an indestructible guy like me.
Just "Thanks, Superman,"
and the bankers smiling as I flew away.

All the time they were thinking,
"What a ***** tool," and they were right.
Hell, it was all insured.
If I'd quit then and done something with myself –
forgotten this superhero thing and gotten a realtor's
license
or just a full time job with benefits,
maybe I wouldn't be waiting for the TV hour
here in the dayroom of the County Home.
I never saved anyone from this. No one could.

But in a way, it's true, what they say,
that every moment lasts forever,
because I still dream about those first nights
when I was young, before it all started,
flying out of Metropolis in my pajamas
with the moon overhead and the silver ocean below,
and the billboards left behind
like a cry for help I can finally ignore.

TRANSITION And as if this pitiful reverie wasn’t enough . . . Superman has problems with women to . . . . In fact, and he’ll hate me for sharing this . . . he just got this letter from his wife Lois yesterday. Dear Superman by Lois Lane (aka Ron Koertge)

Dear Superman

Dear Superman,
I know you think that things
will always be the same: I'll rinse
out your tights, kiss you good-bye
at the window, and every few weeks
get kidnapped by some stellar goons.

But I'm not getting any younger, and you're not getting any older. Pretty soon I'll be too frail to take aloft, and with all those nick-of-time rescues, you're bound to pick up somebody more tender and just as ga-ga as I used to be. I'd hate her for being 17 and you for being… what, 700? I can see your sweet face as you read this, and I know you'd like to siphon off some strength for me, even if it meant you could only leap small buildings at a single bound. But you can't, and, anyway, would I want to just stand there while everything else rushed past? Take care of yourself and of the world which is your own true love. One day soon, as you patrol the curved earth, that'll be me down there tucked in for good, being what you'll never be but still Your friend,

Lois Lane

CLOSING

SAID WISTFULLY, SADLY: Faster than a speeding bullet? More powerful than a locomotive?! Able to leap tall buildings in a single bound! LOOK! Up In The Sky! It's a bird! It's a plane! It's SUPERMAN!
```

---

## IC-1926: Sweet Ruin and Safeway

- Title: Sweet Ruin and Safeway
- Author (byline): Tony Hoagland
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 940
- Already set (do not supply): none

### Source block (context only)

```text
Author: Tony Hoagland
Book: Sweet Ruin
ISBN: 978-0299135843
Publisher: University of Wisconsin Press
Date (Month/Year): Jan 1993
Author: Tony Hoagland
Book: Sweet Ruin
ISBN: 978-0299135843
Publisher: University of Wisconsin Press
Date (Month/Year): Jan 1993
```

### Introduction (context only: never use it for content warnings)

```text
You probably already know more about parents than you’d like to. When they were kids, they walked through three-foot snow drifts to school and home again, uphill both ways. They never had an allowance, or asked for one. They always did their homework and chores, and they never missed a church meeting.

And now they work their fingers to the bone so you can enjoy all the luxuries they had to do without. And are you grateful? Do you understand them?

Maybe.

Sometimes.

You try, anyway. . . . Sweet Ruin by Tony Hoagland
```

### Performance text (classify this)

```text
Sweet Ruin

Maybe that is what he was after, my father, when he arranged, ten years ago, to be discovered in a mobile home with a woman named Roxanne, an attractive, recently divorced masseuse.

He sat there, he said later, in the middle
of a red, imitation-leather sofa,
with his shoes off and a whiskey in his hand,
filling up with a joyful kind of dread--
like a swamp, filling up with night,

--while my mother hammered on the trailer door
with a muddy, pried-up stone,
then smashed the headlights of his car,
drove home,
and locked herself inside.

He paid the piper, was how he put it,
because he wanted to live,
and at the time knew no other way
than to behave like some blind and willful beast,
--to make a huge mistake, like a giant leap

into space, as if following
a music that required dissonance
and a plunge into the dark.
That is what he tried to tell me,
the afternoon we talked,
as he reclined in his black chair,
divorced from the people in his story
by ten years and a heavy cloud of smoke.
Trying to explain how a man could come
to a place where he has nothing else to gain

unless he loses everything. So he louses up his work, his love, his own heart. He hails disaster like a cab. And years later, when the storm has descended and rubbed his face in the mud of himself,

he stands again and looks around,
strangely thankful just to be alive,
oddly jubilant--as if he had been granted
the answer to his riddle,
or as if the question
had been taken back. Perhaps
a wind is freshening the grass,
and he can see now, as for the first time,
the softness of the air between the blades. The

pleasure built into a single bending leaf.

Maybe then he calls it, in a low voice
and only to himself, Sweet Ruin.
And maybe only because I am his son,
I can hear just what he means. How
even at this moment, even when the world

seems so perfectly arranged, I feel
a force prepared to take it back.
Like a smudge on the horizon. Like a black spot
on the heart. How one day soon,
I might take this nervous paradise,

bone and muscle of this extraordinary life,
and with one deliberate gesture,
like a man stepping on a stick,
break it into halves. But less gracefully

than that. I think there must be something wrong with me, or wrong with strength, that I would break my happiness apart simply for the pleasure of the sound. The sound the pieces make. What is wrong

with peace? I couldn't say.
But, sweet ruin, I can hear you.
There is always the desire.
Always the cloud, suddenly present
and willing to oblige.

TRANSITION I wish I could never see it, I wish I could never see my parents for anything other than the all-knowing beings who brought me into this world but ignoring their flaws gets harder and harder as I age. It doesn’t make me love them any less. It just makes me think. Finding out that your parents are people too with their own unique set of failures and shortcomings is sort of like finding out Santa Claus isn’t real. I never wanted to know. I wish they could’ve just kept feeding me the lies so I’d feel safe and didn’t have to cope with their loss . . . . Safeway by Tony Hoagland

Safeway

Even after an hour in her room
with eye shadow and rouge,
moisture whip, lip gloss, and perfume
my mother still looked like she was dying

unexotically,
still looked like a person
trying to impersonate a person
going somewhere other than the grave,

though she was only going to the store,
after weeks of living
horizontally
while her blood was scoured by detergents
bleached by blasts of subatomic light.

Riding on her bony little head,
the glossy auburn wig
looked like something stolen,
the lame hip pulled her to one side
like the stuck wheel of the shopping cart we pushed

past pyramids of fruit,
down mile long corridors of breakfast food
where cartoon animals shot sugar stars
over an infinity of bowls,

--a landscape which seemed,
in the brightness and abundance of its goods,
like somebody’s idea
of paradise--

and the bright, continual ringing of the registers was like the sound of happiness for sale.

I was angry, dutiful, and seventeen, afraid she was going to read her obituary in the faces of the shoppers;

frightened they would stop and stare
at the black cloud hovering above our heads
as we moved slow as history
up and down the aisles.

Maybe months of sickness had burned away my mother’s

shame
and left in her dry mouth
a taste for irony, maybe she wanted
to show the populace

what death looked like in person or maybe it was simply her last chance to make small talk with the neighbors who stopped to say hello--

Mrs. Johnson, Mrs. Green, whose kindness I imagined, then despised, caught awkwardly among them as I was, between the living and the dead.

But looking back across the years,
the scene looks different to me now. I see
a little group of people, halted
in the midst of life,
their carts jammed up
against the lettuce and the tangerines.

There is no gallows standing there, no spectral executioner fingering his blade.

And I seem sweet at seventeen, innocent
even in my rage--
trying to protect
what didn’t need protecting
from what couldn’t be saved.
```

---

## IC-1927: Toxic Masculinity and the Psyche of Men

- Title: Toxic Masculinity and the Psyche of Men
- Author (byline): Mwende “FreeQuency” Katwiwa, Rudy Francisco, and Kyle “Guante” Tran Myhre
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1244
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mwende "Freequency" Katwiwa
Website: https://freequency.medium.com/yo-masculinity-
so-fragile-7fbe0b238c59
ISBN: On-line Transcript
Publisher: Freequency.Medium.com
Date (Month/Year): Feb 28, 2018
Author: Rudy Francisco
Book: Helium (Pg 70-73)
ISBN: 978-1943735198
Publisher: Button Poetry
Date (Month/Year): Nov 2017
Author: Kyle “Guante” Tran Myhre
Website: https://guante.info/2022/05/31/manup/
ISBN: On-line Transcript
Publisher: Guante.info
Date (Month/Year): May 31, 2011 (Ten Year Anniversary)
Author: Rudy Francisco
Book: Helium (Pg 46)
ISBN: 978-1943735198
Publisher: Button Poetry
Date (Month/Year): November 2017
```

### Introduction (context only: never use it for content warnings)

```text
According to Psychologist Ellen Hendricksen, toxic masculinity can best be described as a narrow, rigid box that men, especially men of color, must contort themselves to fit inside. To do so, he must live by a societal set of beliefs and behaviors:

1. Suffer pain in silence.

2. Have no needs.

3. Never lose.

4. Show no emotions other than bravado or rage.

5. Show no weakness.

If you don’t fit in the man box, you pay the price.

This needs to stop. We need to be role models for the new generation. We need to teach boys not to be men, but to be human. This is NOT a gender issue. It is a human issue and once we recognize it as such, toxic masculinity will fade.

Toxic Masculinity and the Psyche of Men with poems by Mwende “FreeQuency” Katwiwa, Rudy Francisco, and
```

### Performance text (classify this)

```text
Yo Masculinity So Fragile by Mwende "Freequency" Katwiwa

Yo masculinity so fragile it would starve in a house made of kitchens

Yo masculinity so fragile,

it thinks saying you do something like a girl is an insult,

thinks getting a compliment from a man makes him or you gay,

Yo masculinity so fragile,

that when a woman tells you
‘no’
you hear
‘try harder’,
but when she tells you she has a man,
you learn to recognize restraint,
so fragile,
it thinks gift wrapping catcalls with compliments
means women should receive them like gifts,
so fragile,
it become a grinch or a gun if they don’t.

Yo masculinity so fragile,
it would shatter under the weight of the truth. . .
that it’s not helping anyone,
especially yourself,

so fragile, that if it shatters, it’ll still expect a woman to clean it up off the floor.

Yo masculinity so fragile, that it can’t possibly be all your fault,

so fragile
we must deal with the fact
that this world,
it makes men hard
because it is less complicated
than allowing them to be human.

Yo masculinity is so fragile that if it shatters

(and if you are lucky it will eventually shatter)

it will die a heavy thing, having consumed so much of your being.

. . . but on that day, I look forward to finally meeting you.

Kyle “Guante” Tran Myhre.

Rifle II (aka The Heart and the Fist) by Rudy Francisco (Pg 70-73)

On average
the Mexican government
confiscates approximately
38,000 illegal firearms per year.

In 2012,
Pedro Reyes,
an artist from Mexico City,
convinced his government
to donate the guns to him
so he could turn them into
musical instruments.

So somewhere
there is a tambourine,
a drum set, a guitar,
all made out of things
that were used to take people’s lives,
but now they create a sound
that puts life back into people’s bodies,
I wonder how long it took to convince
the first rifle that it could hold a note
instead of a bullet, but still fire into a crowd
and make everyone move.

When I was six, I was taught how to throw a punch, In the 80s, that was the anti-bullying movement.

The first time one of my classmates
took a yo mama joke a little too far,
I remembered all of my training,
I hit the boy in the face,
I turned his nose into a fountain.

I remember staring at my hands
the same way you stare at a midterm
when all your answers are correct.
I had no idea what class this was
but I did know I was passing
and isn’t that what masculinity has become?

A bunch of dudes afraid of their own feelings,
terrified of any emotion other than anger,
yelling at shadows on the wall,
but still haven’t realized
that we’re the ones standing in front of the light.

We learn how to dodge a jab,
we learn how to step in before we swing,
we learn that the heart is the same size as the fist,
but we keep forgetting they don’t have the same functions.
We keep telling each other to man up
when we don’t even know what that means.

We turn our boys into bayonets,
point them in the wrong direction,
pull their triggers and fail to acknowledge
all the damage they are doing in the distance.

The word “repurpose” means to take an object and give it amnesia.

It means to make something forget what it’s been trained to do so you can use it for a better reason.

I am learning that this body is not a shotgun.
I am learning that this body is not a pistol.
I am learning that a man is not defined
by what he can destroy.

I am learning that a person
who only knows how to fight
can only communicate in violence
and that shouldn’t be anyone’s first language.

I am learning that the difference between a garden and a graveyard is only what you choose to put in the ground.

One day,
I came across a picture of a strange-looking violin.
The caption said it was made out of a rifle
and I was like,
“someday
that can be me.”

Ten Responses to the Phrase Man Up by Kyle “Guante” Tran Myhre (Clean Version)

1. I know what you’re trying to say. Man up means to do the difficult thing in the face of hardship, to take responsibility. As if women, and nonbinary people, never faced hardship. As if the people in my life who taught me responsibility were ever men.

2. You want to question my masculinity, like a schoolyard circle of curses, fine. Just remember: not every problem can be solved by “growing a pair.” You can’t arm-wrestle your way out of depression. The CEO of the company that just laid you off does not care how much you bench. And I promise, there is no lite beer in the universe full-bodied enough to make you love yourself.

3. Man up? Oh that’s that new superhero, right? Mild-mannered supplement salesman Mark Manstrong says the magic words “MAN UP,” and then transforms into THE FIVE O’CLOCK SHADOW, the massively-muscled, deep-voiced, leather-duster-wearing super-man who defends the world from, I don’t know, feelings.

4. Of course. Why fight to remove our chains, when we can simply compare their lengths? Why step outside the box, when the box has these awesome flame decals on it? We men are cigarettes: dangerous, poisonous, mass-produced.

5. You ever notice how nobody ever says “woman up?” They might imply it, but it’s not like a thing people say. Maybe because women and the women’s movement figured out a long time ago that being directly ordered around by commercials, magazines, and music is dehumanizing. When will men figure that out?

6. The phrase “Man Up” suggests that competence and perseverance, both generally good things, are also uniquely masculine. That women and nonbinary people—not to mention any man who doesn’t eat steak, drive a big pickup truck, and have lots of sex with women—are nothing more than background characters, comic relief, props. More than anything, though, it suggests that to be yourself—whether you, wear skinny jeans, rock a little eyeliner, drink some other brand of light beer, or write poetry—will cost you.

7. And how many boys have to kill themselves before this country acknowledges the problem? How many women have to be assaulted? How many trans people have to be murdered? We teach boys how to wear the skin of a man, but we also teach them how to raise that skin like a flag and draw blood for it.

8. Boy babies get blue socks. Girl babies get pink socks. What about green? What about purple? What about orange, yellow, chartreuse, cerulean, black, tie-dyed, buffalo plaid, rainbow…

9. I want to be free, to express myself. Man up. I want to have meaningful, emotional relationships with my brothers. Man up. I want to be weak sometimes. Man up. I want to be strong in a way that isn’t about physical power or dominance. Man up. I want to talk to my son about something other than sports. Man up. I want to be who I am. Man up.

10. No.

Chameleon by Rudy Francisco (Pg 46) As men, it is important that we start asking ourselves, What will the boys learn from us?

*NOTE: Authors are all men of color, perspectives may best be performed by students of color
```

---

## IC-1928: Mexican Poetry Collection

- Title: Mexican Poetry Collection
- Author (byline): Jimmy Santiago Baca, Bill Dahl and Rafael Guillen
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 978
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jimmy Santiago Baca
Book: Immigrants in our Own Land
ISBN: 978-0811211451
Publisher: New Directions Publishing
Date (Month/Year): Nov 1990
Author: Bill Dahl
Book: Immigration Law Weekly
ISBN: Magazine
Publisher: Immigration Law Weekly
Date (Month/Year): January 8, 2007
Author: Rafael Guillen
Book: I’m Speaking: Selected Poems
ISBN: 978-0810118515
Publisher: Northwestern University Press
Date (Month/Year): July 2000
```

### Introduction (context only: never use it for content warnings)

```text
According to USA Today: "Most of the estimated 6.3 million Mexicans who are in the USA illegally came because of family connections and better job opportunities here, not because they were unemployed or destitute in their homeland.”. And therein lies part of the issue: the vast majority of American citizens believe that illegal immigrants from Mexico are taking away our jobs. The statistics tend to prove this perception; however, as with every issue, there are two sides that should be heard. Jimmy Santiago Baca presents a view from south of the border in “So Mexicans are Taking Jobs from Americans” .
```

### Performance text (classify this)

```text
So Mexicans are Taking Jobs from Americans

O Yes? Do they come on horses with rifles, and say,

Ese gringo, gimmee your job?

And do you, gringo, take off your ring, drop your wallet into a blanket spread over the ground, and walk away?

I hear Mexicans are taking your jobs away. Do they sneak into town at night, and as you’re walking home with a whore, do they mug you, a knife at your throat, saying, I want your job?

Even on TV, an asthmatic leader crawls turtle heavy, leaning on an assistant, and from a nest of wrinkles on his face, a tongue paddles through flashing waves of lightbulbs, of cameramen, rasping “They’re taking our jobs away.”

Well, I’ve gone about trying to find them,
asking just where the hell are these fighters.
The rifles I hear sound in the night
are white farmers shooting blacks and browns
whose ribs I see jutting out
and starving children,
I see the poor marching for a little work,
I see small white farmers selling out
to clean-suited farmers living in New York,
who’ve never been on a farm,
don’t know the look of a hoof or the smell
of a woman’s body bending all day long in fields.

I see this, and I hear only a few people got all the money in this world, the rest count their pennies to buy bread and butter.

Below that cool green sea of money,
millions and millions of people fight to live,
search for pearls in the darkest depths
of their dreams, hold their breath for years
trying to cross poverty to just having something.

The children are dead already. We are killing them, that is what America should be saying; on TV, in the streets, in offices, should be saying, “We aren’t giving the children a chance to live.”

Mexicans are taking our jobs, they say instead. What they really say is, let them die, and the children too.

TRANSITION

Immigration is now and always has been a tricky affair. The delicate balance of need and want, verses can and should. We can certainly understand someone living in desperate conditions wanting to improving their lot in life. What better place to do it than the greatest nation on earth. America is the envy of the world. We are a magnet, and a beacon. After all . . "Give us your poor, your tired, your huddled masses longing to be free..."is engraved at the base of the Statue of Liberty. Before you make your final decision on the issue of immigration (legal or otherwise), ask yourself a simple question. What would you do if you were in their place, but first, take a long look around your home, in you fridge and in your pantry.. and just for an added effect, and take an extra moment thinking of your children. Perhaps, you'll come away with a slightly different outlook. Immigrace-un by Bill Dahl

Immigrace-un

Unconvinced, we can’t let them in.
Uncertain what to do with sin.
Unsettled because they are here.
Undue stress of misdirected fear.

Unbelievable, the insensitivity of man. Unwilling to do all we can.

Unconscious of the opportunity to rise above, Unjust policies that can be slain with love.

Unswerving loyalty to a partisan creed.
Unabated cries of those in need.
Undisturbed, is how we prefer to live.
Unconscionable, man’s inability to forgive.

Unbalanced adoration of power and might. Uncomfortable adjustments required to do what’s right. Uncertain about the legitimacy of a border fence and gate. Unbearable guilt over ungodly hate.

Unearth in us, the will to stand tall.
Unspeakable injustice harms us all.
Unfortunate inequities cast a vast pall.
Unfounded self-righteousness blinds us all.

Under the lies, truth has a face. Uncommon courage, it’s name is Grace.

Underscore the urgency in this nation. Undo the injustice of Immigrace-un.

TRANSITION

Illegal immigrants are in some ways the lowest of the low in the modern world. Not only do they start over, usually with limited resources; they have a difficult, sometimes expensive and dangerous task getting to their destination; and then have to find employment. They have to deal with ethnic prejudice, xenophobia, and prejudice against their illegal status: "come over here and take our jobs", "can't speak the language", "sponge off welfare", etc. They may live in fear of arrest and deportation or incarceration. Why would anyone become an illegal immigrant? Because it's better than the alternatives. Not Fear by Rafael Guillen Not Fear Not fear. Maybe, out there somewhere, the possibility of fear; the wall that might tumble down, because it's for sure that behind it is the sea. Not fear. Fear has a countenance; It's external, concrete, like a rifle, a shot bolt, a suffering child, like the darkness that's hidden in every human mouth. Not fear. Maybe only the brand of the offspring of fear.

It's a narrow, interminable street
with all the windows darkened,
a thread spun out from a sticky hand,
friendly, yes, not a friend.
It's a nightmare
of polite ritual wearing a frightwig.
Not fear. Fear is a door slammed in your face.

I'm speaking here of a labyrinth
of doors already closed, with assumed
reasons for being, or not being,
for categorizing bad luck
or good, bread, or an expression
— tenderness and panic and frigidity - for the children
growing up. And the silence.
And the cities, sparkling, empty.
and the mediocrity, like a hot
lava, spewed out over
the grain, and the voice, and the idea.

It's not fear. The real fear hasn't come yet.
But it will. It's the doublethink
that believes peace is only another movement.
And I say it with suspicion, at the top of my lungs.
And it's not fear, no. It's the certainty
that I'm betting, on a single card,
the whole haystack I've piled up,
straw by straw, for my fellow man.
```

---

## IC-1929: Two Brothers: A Fiction

- Title: Two Brothers: A Fiction
- Author (byline): Ai
- Work: Vice: New and Selected Poems
- Publisher: WW Norton and Co
- Publication date as stated: March 1999
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 656
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ai
Book: Vice: New and Selected Poems
ISBN: 978-0393047059
Publisher: WW Norton and Co
Date (Month/Year): March 1999
NOTE: An analysis of this poem to aid in the student’s
understanding and interpretation can be found at
http://oldrpo.library.utoronto.ca/poem/3359.html
```

### Introduction (context only: never use it for content warnings)

```text
Why did Robert Kennedy court his brother's fate by seeking the Presidency after incurring the enmity of the same criminal and political underworlds that, most people now believe, precipitated his older brother's murder? It is documented fact that Robert Kennedy ordered that autopsy materials remaining from investigations into his brother's death be handed over to his staff. This included a stainless steel container that held President Kennedy's brain, which subsequently vanished.

"Two Brothers" by Ai is a dramatic poem spoken by Jack Kennedy, five years after his death, in the Los Angeles Ambassador Hotel room of his brother, just as Bobby comes out of a dreaming sleep before making his victory speech in the pivotal California Democratic Presidential Primary on the night of June 4, 1968. After midnight that same night, as Bobby Kennedy walked off-stage through the hotel kitchen area, he would, too, be assassinated as he paused to shake hands with well-wishing kitchen staff. Now, however, Bobby prepares to assume his dead brother's destiny.

Two Brothers by Ai
```

### Performance text (classify this)

```text
1
Night tightens its noose.
You swim toward me out of sleep
like an eel,
as I put the glass canister
beside you on the bed.
Death, Bobby, hit me
like the flat of a hand.
Imagine you are made of crystal
and someone ice picks you
and you shatter,
all your cells coming
almost to despair
it is so good. Dallas. Dallas.
I turn toward the window,
then turn back to you.
Remember that Crayola drawing
of John-John’s? --
the black smoke coming out the roof
of the White House
like curly black hair.

How Jackie spanked his hand
and drew him another
with angels lifting up?
Our own childhoods? --
days of ease and grace.
The good life sucking us deeper
and deeper in
toward its hot, liquid center,
where seasoned with the right diction,
schools, and politics
we would fry crisp and greaseless.
King for a day,
that’s who I was.
I drove power,
the solid-gold Cadillac.
Go ahead, frown.
Tell me about the sin of pride
and I’ll tell you
about the lie of forgiveness.
It wasn’t Oswald killed me,
it was envy.

2
“I have this dream, Jack,” you say.
“I’m at Arlington. It’s twilight.
Thousands of funeral markers
rise from the ground
like dirty alabaster arms.
It’s here, pilgrim,
they seem to say.
And then I’m in a room.
A man is counting green bills
Sharp enough to cut,
while I pry the lid off a barrel
and peer down into it,
As if inside, there are dark green pickles
or steel-blue fish,
as if I were a boy
on a crowded street in Russia
with my hand around a coin
and the other in my brother’s hand>
And while I scuff my shoe
and try to decide,
from far away I hear bugles, hoofbeats,
I see my brother’s head
suddenly rise from his body
like a tiny pink ball
on a spout of dark red water,
clear past the rooftops
into the serene evening sky.
I am that boy, Jack,
dipping his hands
in the one standing barrel,
Into water warm as blood,
with nothing to say to anybody,
except, ‘My brother is the moon.’”

3
Riddles, I say,
lifting the lid off the canister.
I pull out a wet, gray mass,
stare at it, then put it back.
Some African tribes
eat the brains of their dead.

It brings them closer;
it kills them too.
But whatever it takes, Bobby, right?
I look out the window
at the deep rose welts of dawn,
streaking the sky’s broad back,
Then hand you the canister.
You lift out my brain.
When you bit down, I burn.
The air smells like creosote
and I stand before you,
my skin plum and pink,
my wounds healed.
I put my arms around you
and you disappear into me . . .

I stare at myself in the mirror:
Jack Kennedy,
thinner now, almost ascetic,
wearing the exhaust fumes of L.A.
like a sharkskin suit,
while the quarter moon
hangs from heaven,
a swing on a gold chain. My throne.
I step back and knot my tie.
Bobby, it’s all a matter of showmanship.
You have to have the ability to entertain,
to stand like P.T. Barnum
in the enchanted center
of the public eye,
to drop your pants now and then
and have the crowd
cry for more,
to give it to them,
to take those encores,
till like the clown in Piaf’s song
the show is all there is,
and the bravos, the bravos.
You give the people what they want, Bobby,
Someone they can’t help loving
like a father or an uncle,
someone who through his own magical fall
lifts them above the slime
of their daily lives.
Not God made man,
but man made God.
I step back to the mirror.
Break a leg, kid, I say to myself.
Give ‘em a miracle,
Give ‘em Hollywood.
Give ‘em Saint Jack.
```

---

## IC-1930: The Victory Explosions

- Title: The Victory Explosions
- Author (byline): Derrick Brown
- Work: I Love You Is Back
- Publisher: Write Bloody Publishers
- Publication date as stated: Jan 2006
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 720
- Already set (do not supply): none

### Source block (context only)

```text
Author: Derrick C. Brown
Book: I Love You Is Back
ISBN: 978-0978998912
Publisher: Write Bloody Publishers
Date (Month/Year): Jan 2006
```

### Introduction (context only: never use it for content warnings)

```text
When have you failed? You have. It’s a given. It’s inevitable. But . . . I’ll admit . . . it’s not a popular conversation to have – the one where we admit we’ve failed. Winston Churchill once said: “Success is not final, failure is not fatal: it is the courage to continue that counts.” In this poetry selection, Derrick Brown reflects on his first memory of failure in what he (in hind-site) calls . . . The Victory Explosions.

The Victory Explosions by Derrick Brown.
```

### Performance text (classify this)

```text
I was in the fifth grade and I got my a** kicked by a
fourth grader.
Good times.
I try to remember my youth.
It evaporated into 76 memories.
One memory when you were young
was that you believed the earth was made perfect by
god
and that humans fouled it up.

That sin was something we gave birth to a as god shook his head at our idiocy and said “how could they choose terror and loss?” You didn’t think god ever really wanted perfection if he designed the things he made with an instinct to screw up. Fighting it sometimes failing is beautiful and hard screwing up is part of the program. Call it sin, call it human maybe there are codes built inside of darkness needing light and vice versa. It did not shake your belief in an existence of a god, but it shook your belief in the bland necessity for perfection. It birthed the belief that the human who could figure out the balance of a hunger for winning and a deep respect for losing would win the life trophy. You go back to the first year you learned to daydream in a clothing rack.

The first year butterflies bloomed adrenalized in your
wet guts.
In the fifth grade you tempted everything
bicycle wheelie spinning
the smell of girls
pencils at war
dismantled radios
launching off the swing set into the air.
Your first sensation of flight.
An innocent season for getting you’re a** royally kicked
by a boy who thought it would be a nice sign of his love.
Adam White heard I liked his girl and kissed her
underwater
at a Dutch pool party French style
which is weird for a fifth grader.
These were skill sets in the fifth grade my tongue was
not prepared for.
I didn’t know who started the rumor
but I was about to pay for it with the cash of my face.
The same field we chased girls together in
the strong freckled Adam challenged me to my first fist
fight.
I felt like a coward in a costume of a coward.
I was skinnier than a dead model.
No matter how much I denied the rumor
freckles popping from his face like brail.
“Your a** is grass Derrick Brown!”
I know, I know.
The crowd gathered
I stared at them like a sparrow trapped in an airport
terminal
wanting the sky but stuck against the glass.
I stood there like a cricket in a junkyard of fiddles.
Unable to stop my legs from shaking music from my
knees.
He swore he loved her and that I would pay.
Forehead blistering, wrinkling like a crumbled valentine.
And where were the teachers?
That’s what they’re paid for.

What I wanted was mercy, but in the fifth grade
mercy was just a word in the dictionary
and even I didn’t know what it meant.
And he cocked.
His fists came out and crushed at my jaw
my eyes went black and all that I saw
was a shower of lightning bugs
children flashing into sunshine
teeth penetrating my cheek
children falling backwards
blood fertilizing the softball field.
But instead of freezing for some dumb reason
I stood up again and he struck me down once more.
Eyes ricocheting against the back of my skull.
The earth meeting my failure.
Legs buckling, skin wreaking with contact.
And for some dumb reason,
for some dumb stupid reason
I stood up again and he socked me with all his might.
Matchsticks lighting in my cheeks.
And I stood up again and he hit me so hard my mother’s
eyes bled.

And I fell again and I stood up again
and again
and again
and again
until he grew tired of socking me in the face and he just
left.
And everybody left until I stood there alone
baptized in my own warm blood.
I now knew the cost of the saddened sponge
and slop of a girl’s ridiculous lips because guess what?
We did kiss underwater at her Dutch pool party.
Like aqua spies.
And it was worth it.
There’s nothing for me to learn from winning.
It is losing that has yielded the unforgettable lessons.
Losing is pregnant with chance.
Victory escorts loss to every dance.
That is harmony

harmony

harmony.
```

---

## IC-1931: Walking on Glass

- Title: Walking on Glass
- Author (byline): Alma Fullerton
- Work: Not specified
- Publisher: HarperTeen
- Publication date as stated: Jan 2007
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: TRIGGER WARNING
- Teaser before the introduction: Yes
- Spoken words (computed): 1633
- Already set (do not supply): none

### Source block (context only)

```text
Author: Alma Fullerton
ISBN: 978-0060778514
Publisher: HarperTeen
Date (Month/Year): Jan 2007
```

### Introduction (context only: never use it for content warnings)

```text
Your mother’s suicide attempt has left her in a coma from which she’s never waking up. You know that she wouldn’t want to live like this, but could you really help her die? The hardest decision of your life, and there’s no one to help you . . . It’s all up to you.

Walking on Glass by Alma Fullerton.
```

### Performance text (classify this)

```text
TRIGGER WARNING: MOTHER’S SUICIDE AND DEATH

[CAUTION - This is a Novel in Verse. Check with your tournament before entering this selection in the POETRY category]

(Pg 4) Writing a journal
for some shrink
won’t make me
feel better.
It won’t change
what happened.
it’ll just make me think,
and I don’t want to think.
Mom thought too much.
Look where it got her.

(Pg 10) I slouch in a chair
across from Dr. Mac.
He takes my journal
and flips through it
without reading,
like he promised.
“I’m glad you’re writing.”
He hands it back.
“How’s your mother?”
I spin my chair, lean back,
and put my feet up on his desk.
“Same.”
He nods, waiting for me to say more.
I don’t, making him ask,
“How are you?”
I shrug. “Same.”

****

(Pg 12) I took the photograph
From the mirror in my mother’s room.
Her at the age of eight,
perched high in a tree,
arms stretched out like
an untamed eagle,
prepared to take on
The world.
I keep the picture
in my pocket
so I’ll always
remember
the way she was
before she was caged
by a baby
she never wanted.

****

(Pg 13) Dad says,
“Come and see Mom.”
So I do.
Mom,
tucked tight in the bed,
empty minded.
No longer herself,
or anyone else.
Wires force life into a body
left hanging
like a marionette
With no one to pull
the strings.
Dad leans close to her
and whispers,
“You’ll come home soon, dear.
Everything will be better.”
I know he really
wants that
to be true,
but the thought of her
coming back
into our lives
makes my insides
flip.

(Pg 16) I don’t want her to die.
I just want
it all to
stop.
Does that make me
so terrible?

****

(Pg 35-36) The beeping
from her machines
shrieks.
A reminder
her soul is tethered to the ground,
a captive falcon,
circling in confusion,
longing for someone
to set it
free.
. . . and I think maybe sometimes
nonexistence
is better than being
caged.

I stand watching her.
I want to smack her
for putting us through this.
I want to scream,
“Why didn’t you want to live
You’re supposed to want to stay here
with us!”
If she’s going to die,
she should get it over with
and just
do
it.

(Pg 45) I stand over Mom,
shaking inside,
and wonder why she did it.
Why she didn’t think about anyone
but herself.
Why she didn’t think
about us.
Why she didn’t think
about me.

****
(Pg 48-49) Nurses lurk
around Mom’s bed
like vultures.
But Dad guards her --
a lion
ready to pounce on
the vultures as they swoop
to take away his mate.
He doesn’t seem to know
what the vultures
already know.

She’s gone.

If Mom came home,
things wouldn’t change.
Her mood would always flip
from bad to worse
in a matter of seconds,
and for the rest of our lives
Dad and I would
be walking on
shards of glass
from a broken
chandelier.

****
(Pg 56) My teacher asks everyone,
“If you could change
anything in history,
what would it be?”

Kids say things like,
I’d prevent wars
or Bin Laden and Hitler
wouldn’t have been born.
Other kids not their heads to agree.
When the teacher asks me,
I say,
“Four months ago,
I would have come home
five minutes earlier.”
Everyone looks away from me
like my face is on
sideways.

****
(Pg 58) It’s too quiet
at home,
and it smells different.

There’s no longer
the scent of fresh flowers
Mom always kept
in the living room.
Instead I smell
dust, rot, and
even after cleaning the floor,
blood.
Why can I still smell
the blood?

****
(Pg 64) As I sit on the couch
staring at a cushion,
in silence,
I keep seeing Mom
curled up and gripping
this cushion on this couch,
alone,
crying
in the dark.
Instead of going to her,
I walked by.
Saying nothing,
like she was invisible.
I hug the cushion
and smell it,
hoping to get a hint
of her perfume,
but it’s gone.
. . . I go to my room,
and turn up the music
loud
so I can forget what
I remember.

****
(Pg 70) My father
cries out to Mom
in his sleep.
I slide from the warmth
of my bed
to sleep on the bumpy couch
in the living room,
where I’ll no longer
hear his calls.

****
(Pg 73) What’s left of the
old chandelier
is heaped next to the window.
And once in a while
the sun shines in
and rainbows dance
against the walls.
It’s as if the crystals
stole Mom’s spirit.
I hang the crystals
by the window
in Mom’s room.
I hope they
give her
spirit
back.

****
(Pg 82-83) Today
the doctors tell Dad
there’s still no hope.
Mom’s not getting better.
They ask if he would
consent
to have the machines
shut down
and donate

Mom’s organs.
Dad gets mad.
He refuses to believe
she’s gone.
But I’m feeling
more relieved
than mad.

God, Forgive Me . . . The thought of my own mother dying shouldn’t leave the taste of freedom in my mouth.

****
(Pg 87) Nurses flock
to Mom’s room
like she’s having a sale
on white sneakers.
In between their visits
I’m alone with her
and her machines.
I reach for the machine
to do what I need to do.

My hands shake,
and sweat drips
down the back of my legs,
stinging the open blisters
on my heels.
I jerk my hand away,
without even touching
the switch.
I race out of there,
gasping for air,
and throw up on
the shoes I still can’t
fill.

****
(Pg 93) Dad putters around the house
avoiding me.
I want to get right up
in his face
and scream for him
to be the man he should be
so I won’t have to,
but I
can’t.

(Pg 95) “I know you think
I’m wrong,”
Dad says.
He looks at me
over the piles of
takeout containers
on the coffee table.
“I can’t let go yet.”
I scarf down my
chow-mein noodles
to avoid looking
directly at him.
“It’s not my fault. . . ,”
he says.
I glance up.
His eyes water
I focus my attention
on my noodles.
“And I didn’t know she was that
unhappy,” he says.
I put my plate
across the table.
It tips.
I get up
and walk away,
leaving my dad’s heart
and the noodles
spilled all over the floor.

****
(Pg 102) As I left the house
that June morning,
Mom said,
“I love you.”
I just closed the door
and left her
alone.
I should have told her
I loved her.
Maybe then
she wouldn’t be
in the hospital
today.

****
(Pg 103) I bring Mom
roses.
I watch her carefully,
looking for any clue
she knows I’m with her.
She lies there
lifeless.
I try to swallow the lump
building in my throat,
but it just expands.
The aroma from the roses
filters through the air.
They smell like she used to
when I was small.
Sweet and fresh.

Their scent
will fade
now that they’re
no longer attached
to the roots
which gave them life.
I stare outside
and wonder
if I’ll ever have the courage
to cut Mom off
from her roots.

(Pg 106-107) I don’t doubt for a second
that most people think
what I want to do
is wrong.
But I don’t want to
murder
my mother.
I want to set her
free.
Murder
The unlawful killing of a human
being
with malice
aforethought.
I’m thinking about it.
Does that make it
murder?

(Pg 119) Mom doesn’t have
a future.
Mom doesn’t have
a life.
Mom has been dead
for six months.
You can’t call
it murder.

****

(Pg 112-113) Dad sits beside
Mom’s bed.
He strokes her hair
and whispers to her.
He closes his eyes.
Clenching his jaw,
he lets out a sigh.
When he opens his eyes,
a tear drips from each corner.
He shakes his head
and walks out of the room.
I wait for him to come back.
He doesn’t.
I wonder
if Dad is torn up inside
for the same reason
I’m torn.

*****
(Pg 116) Today
Dr. Mac explains how
sick Mom was.
How she needed medicine
to make her feel better,
but she refused to take it
He explains how,
if she did,
she’d still be here.
Today Dr. Mac
explains how
sick Mom was
and how nothing she did
was my
fault.

***** (Pg 122) What happened ???

That day,
I came home and found
a new pair of shoes
by the door.
When I went into the dining room
to tell Mom they were
too big,
mom stepped off of the table.
A noose slung around her neck.

I caught her
and held her up.
Mom struggled.
She kicked me away.
But I wouldn’t
let go.

(Pg 109) Sometimes I wish
I hadn’t held Mom up.
Then it would have
all been over
that rainy June day.

(Pg 122) [But] I wanted to tell her
I loved her.
I wanted to tell her
I needed her.
I wanted to tell her
to stay with us.
The wires holding
the chandelier snapped
and it crashed on top of her head,
and my arm broke
and I dropped her.
Her blood splattered
all over my new shoes.

****
(Pg 125) I remember
her soft voice
floating through the air
like the smell of fresh roses,
as she sings me a lullaby
to take away
the monsters in the night.
I remember
her dimpled smile,
her blue eyes,
her gentle touch.
I remember
my mother,
the way she was.

**** (Pg 130) [It’s] Mom’s birthday

The doctors take
Dad into another room,
leaving me alone
with the shell
of my mother.
I brush the hair from her face
and rest my hand
on her forehead.
I sit,
listening to the machines
as their parts move,
and I’m no longer afraid.

I bend
and kiss my mother’s cheek.
“I will always love you, Mom.”
I reach over
and shut
off
the machine.
When I open the door
to leave,
I notice,
I finally fit
into the shoes
my mother gave me.
```

---

## IC-1932: What it Means to Be a Man – Collection 2

- Title: What it Means to Be a Man – Collection 2
- Author (byline): Harold Norse; Guante (aka Kyle
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1159
- Already set (do not supply): none

### Source block (context only)

```text
Author: Harold Norse
Book: The Outlaw Bible of American Poetry, Pg 133
ISBN: 978-1560252276
Publisher: Thunder's Mouth Press
Date (Month/Year): Nov 1999
Author: Kyle “Guante” Tran Myhre
Book: A Love Song, A Death Rattle, A Battle Cry,
Pg 18-19)
ISBN: 978-1943735334
Publisher: Button Poetry
Date (Month/Year): February 2018
Author: Mark Gonzales
Book: Critical Muslim (Book 8)
ISBN: 978-1849043175
Publisher: Hurst Publishers
Date (Month/Year): September 2014
Author: Kyle “Guante” Tran Myhre
Book: A Love Song, A Death Rattle, A Battle Cry,
Pg 20-21
ISBN: 978-1943735334
Publisher: Button Poetry
Date (Month/Year): February 2018
```

### Introduction (context only: never use it for content warnings)

```text
Over the last three decades a lot of attention has been devoted to the question: “What does it mean to be a man?” These days, the media provides a range of contrasting images in answer to this question. For instance, there is the new domesticated and sensitive man, and his counterpart, the undomesticated, inarticulate and emotionally detached man. Or you may conclude as does Harold Norse . . . I am Not a Man.
```

### Performance text (classify this)

```text
Tran Myhre) and Mark Gonzales

I am Not a Man by Harold Norse (Pg 133) I am not a man, I can't earn a living, buy things for my family. I have acne and a small peter. [edited to "small biceps"] I am not a man, I don't like football, boxing and cars. I like to express my feelings, and I even like to put an arm around my friends shoulders. I am not a man, I won't play the role assigned to me.

The role created by Madison Avenue, Playboy, Hollywood, and Oliver Cromwell. Television does not dictate my behavior. I am not a man, once when I shot a squirrel I swore I would never kill again. I gave up meat, the sight of blood makes me sick. I like flowers. I am not a man I went to prison for resisting the draft. I do not fight back when real men beat me up or call me queer. I dislike violence. I am not a man, I have never raped a woman, I don't hate blacks. I don't get emotional when a flag is waved. I do not think I should love America or leave it, I think I should laugh at it. I am not a man. I have never had the clap. [edited: removed] I am not a man. Playboy is not my favorite magazine. I am not a man. I cry when I am unhappy. I am not a man. I do not feel superior to women. I am not a man. I don't wear a jockstrap.

I am not a man. I write poetry. I am not a man. I meditate on peace and love. I am not a man. I do not want to destroy you.

(Combined with Logic In the House of Sawed-Off

Telescopes by Jeffrey McDaniel (Pg 253) and I’m an Emotional Idiot by Maggie Estep (Pg 256) -- The Outlaw Bible of American Poetry)

TRANSITION

In our society today, I can almost guarantee that you have heard one of the following phrases – “Be a Man” – “Boys don’t cry” or the all-encompassing . . . “Man Up.” And maybe, just maybe boys and men have wanted to respond with something other than straightening their spines and biting their lips. Responses to the Phrase “Man up” by Kyle “Guante” Tran Myhre Responses to the Phrase ‘Man Up’ (Pg 18-19)

by Guante (aka Kyle Tran Myhre)

1. If you want to question my masculinity, save your breath. Because contrary to what you may believe, not every problem can be solved by “growing a pair.” You can’t arm-wrestle your way out of chemical depression. The CEO of the company that just laid you off does not care how much you [can] bench.

2. The phrase “Man Up” suggests that competence and perseverance are uniquely masculine traits. More than anything, though, it suggests that to be yourself— whether you wear skinny jeans, listen to Lady Gaga, rock a little eyeliner, or write poetry—will cost you.

3. How many boys have to kill themselves before this country acknowledges the problem? How many women have to be assaulted? How many trans people have to be murdered? We teach boys how to wear the skin of a man, but we also teach them how to raise that skin like a flag and draw blood for it.

4. Boy babies get blue socks. Girl babies get pink socks. What about purple? What about orange, yellow, chartreuse, black, tie-dyed, rainbow . . .

5. I want to be free to express myself. Man up. I want to have meaningful, emotional relationships with my brothers. Man up. I want to be weak sometimes. Man up. I want to be strong in a way that isn’t about physical power or dominance. Man up. I want to be who I am.

TRANSITION

Consider the “idea” of what it has meant to be a man in our society. Many are quick to assume that to be a man means being aggressive, loud, violent, and dominant. But today I want to celebrate men who are trying to redefine what it means to be one. As with Most Men by Mark Gonzales As with Most Men by Mark Gonzales (Book 8)

As with most men, it is easier for me to give hugs than to accept them.

At the age of five
men are taught to colonize one another
through games like cops and robbers
cowboys and Indians.

At the age of eight
we’re given helmets
then told to hit each other in the head with [them].
Bleed but do not blink
cut but do not cry.

Be a man, join the military
die for your country
and if death comes for you
look it in the eye, say
‘bring it on, I fear nothing but
intimacy.’
When it comes to intimacy
men quiver like fault
lines, crumble like cities

Men take note: this is how you give love this is how you receive hugs pressed breast to breast till egos deflate like oxygen.

TRANSITION

And still hugs between men are often full of bravado, back slapping and crushing power which expels every bit of air from one’s lungs. Why? Why must a sign of affection be turned into a show of power. “Guante” explores this concept in Handshakes.

Handshakes by Guante (aka Kyle Tran Myhre) (Pg 20-21)

As a young man, I was taught that one’s masculinity is tied directly to one’s handshake. Your grip must be firm. Some men, however, treat every handshake like a gladiator’s death-match, a test of strength, a test of will. And when I meet these men, as I often do, their handshakes never fail to illuminate my inadequacies. I am reminded that cars confuse and frighten me and that I don't really care about sports. These men attempt to squeeze the testosterone from my body.

Maybe I’m just insecure. But maybe that would make two of us. As he wrings the color from my fingers I find myself wanting to ask him:

Do you ever get tired of the voice in your head telling you to constantly reaffirm that you’re a “real man” by catcalling women, eating enormous hamburgers, and squeezing everything really, really hard?

Is there a teddy bear, somewhere in your history, being ripped away from a pair of hands that just aren’t strong enough?

Do you remember the first time your father wouldn’t let you hold his hand when crossing the street? Do you remember the way he looked at you?

Do you remember being handed your first-born son and not knowing how to hold him? Do you remember squeezing his shoulders like this the first time he disappointed you?

Do you remember what you were trying to hold on to?

And I know: there is so much space between us, as men, that sometimes we feel compelled to cram as much contact as we physically can into every touch. I know.

We’ve become so comfortable with crushing, so hypnotized by our own strength, we forget: how incredible it can feel to let go.

NOTE: Poem by Norse was not included in KS State Qualifier
```

---

## IC-1933: What it Means to Be a Man – Collection 1

- Title: What it Means to Be a Man – Collection 1
- Author (byline): Rudyard Kipling, Charles
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1101
- Already set (do not supply): none

### Source block (context only)

```text
Author: Rudyard Kipling
Book: If: A Father's Advice to His Son
ISBN: 978-0689877995
Publisher: Simon and Schuster
Date (Month/Year): 2007
Author: Charles Bukowski
Book: Septuagenarian Stew: Stories and Poems,
(Pg 283-284)
ISBN: 978-0876857946
Publisher: Black Sparrow Press
Date (Month/Year): May 2002
Author: John Struloeff
ISBN: 978-0931507212
Publisher: Loom Press
Date (Month/Year): March 2008
Author: Harold Norse
Book: The Outlaw Bible of American Poetry, Pg 133
ISBN: 978-1560252276
Publisher: Thunder's Mouth Press
Date (Month/Year): Nov 1999
```

### Introduction (context only: never use it for content warnings)

```text
Fathers can be many things: involved, absent, loving, abusive, supportive or controlling. In some cases, they can be all of the above. But one thing is certain, their influence impacts their sons positively or negatively in profound ways. Fathers can determine the type of man their sons ultimately become – be it through words of advice, the daily examples they set, or even through their absence. Yes, some sons are left to figure things out for themselves. But whatever your experience with your father has been like – positive, negative, or a mix of both – there’s always a choice moving forward. What kind of lessons will you teach the next generation of sons about What it Means to Be a Man?

What it Means to Be a Man – A Collection with poems by Rudyard Kipling, Charles Bukowski, John Struloeff and Harold Norse
```

### Performance text (classify this)

```text
Bukowski, John Struloeff and Harold Norse If by Rudyard Kipling

If you can keep your head when all about you
Are losing theirs and blaming it on you;
If you can trust yourself when all men doubt you,
But make allowance for their doubting too;
If you can wait and not be tired by waiting,
Or, being lied about, don't deal in lies,
Or, being hated, don't give way to hating,
And yet don't look too good, nor talk too wise;

If you can dream - and not make dreams your master; If you can think - and not make thoughts your aim; If you can meet with triumph and disaster And treat those two imposters just the same; If you can bear to hear the truth you've spoken Twisted by knaves to make a trap for fools, Or watch the things you gave your life to broken, And stoop and build 'em up with worn out tools;

If you can make one heap of all your winnings And risk it on one turn of pitch-and-toss, And lose, and start again at your beginnings And never breath a word about your loss; If you can force your heart and nerve and sinew To serve your turn long after they are gone, And so hold on when there is nothing in you Except the Will which says to them: "Hold on"; If you can talk with crowds and keep your virtue, Or walk with kings - nor lose the common touch; If neither foes nor loving friends can hurt you; If all men count with you, but none too much; If you can fill the unforgiving minute With sixty seconds' worth of distance run - Yours is the Earth and everything that's in it, And - which is more - you'll be a Man my son!

My Father by Charles Bukowski (Pg 283-284)

(My father) was a truly amazing man
he pretended to be
rich
even though we lived on beans and mush and weenies
when we sat down to eat, he said,
"not everybody can eat like this."

and because he wanted to be rich or because he actually thought he was rich he always voted Republican and he voted for Hoover against Roosevelt and he lost and then he voted for Alf Landon against Roosevelt and he lost again saying, "I don't know what this world is coming to, now we've got that god damned Red in there again and the Russians will be in our backyard next!"

I think it was my father who made me decide to
become a bum.
I decided that if a man like that wants to be rich
then I want to be poor.

and I became a bum.
I lived on nickels and dimes and in cheap rooms and
on park benches.
I thought maybe the bums knew something.

but I found out that most of the bums wanted to be rich too. they had just failed at that.

so caught between my father and the bums
I had no place to go
and I went there fast and slow.
never voted Republican
never voted.

buried him
like an oddity of the earth
like a hundred thousand oddities
like millions of other oddities,
wasted.

The Man I Was Supposed to Be by John Struloeff (Part II)

The man I was supposed to be works
in a small cedar mill in Oregon.
The heel of his left boot is worn smooth
by the way the engage lever makes him stand,
the shift he has to make, grinding his heel,
a slow turn as the log carriage feeds the wood
that will shriek against the rolling blade.
He watches the blade eight hours a day,
and when he goes home to sleep,
he sees the blade rolling in the dark.

The man I was supposed to be has two sons, and when his youngest is loud he twists his ear, watching for the boy’s eyes to well with tears.

Knock off the racket, he says. The TV’s on. If the boy does it again, he grabs him by his hair, drags him to his room, then watches TV in silence, the way it is supposed to be.

The man I was supposed to be buys beer in a case and drives around at night, looking for a friend to drink it with. He drinks until his face is numb and awakens on the cement floor of his garage, lying flat on his back, his arms spread. Both of his hands are bleeding.

The man I was supposed to be tracks deer on the leaf-covered trails behind his house. There is a doe ahead of him somewhere, and he kneels to place his fingertips on its tracks. That night he will smell the rawness of warm bone and blood. It will hang in his garage seven days until he begins to separate the loosened joints and carefully strip the flesh. He will do it alone, at night, his forearms and hands coated in blood.

Like the stink of beer-sweat and fresh cedar dust, this odor will stay in his skin for days.

I am Not a Man by Harold Norse (Pg 133)

I am not a man, I can't earn a living, buy things for my family. I am not a man, I don't like football, boxing and cars. I like to express my feelings, and I even like to put an arm around my friends shoulders. I am not a man, I won't play the role assigned to me. The role created by Madison Avenue, Playboy, Hollywood, and Oliver Cromwell. Television does not dictate my behavior. I am not a man, once when I shot a squirrel, I swore I would never kill again. I gave up meat, the sight of blood makes me sick. I like flowers.

I do not fight back when real men beat me up or call me
queer.
I dislike violence.
I don't get emotional when a flag is waved.
I do not think I should love America or leave it, I think I
should laugh at it.
I am not a man. Playboy is not my favorite magazine.
I am not a man. I cry when I am unhappy.
I am not a man. I do not feel superior to women.
I am not a man. I write poetry.
I am not a man. I meditate on peace and love.
I am not a man. I do not want to destroy you.

(Combined with Logic In the House of Sawed-Off Telescopes by Jeffrey McDaniel (Pg 253) and I’m an Emotional Idiot by Maggie Estep (Pg 256) -- The Outlaw Bible of American Poetry)
```

---

## IC-1934: The White Guy

- Title: The White Guy
- Author (byline): Stephen Hunt
- Work: The Best American Short Plays 1997-1998
- Publisher: Applause Books
- Publication date as stated: February 2000
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1922
- Already set (do not supply): none

### Source block (context only)

```text
Author: Stephen Hunt
Book: The Best American Short Plays 1997-1998
ISBN: 978-1557834263
Publisher: Applause Books
Date(Month/Year): February 2000
```

### Introduction (context only: never use it for content warnings)

```text
Mark Twain once said “There are many humorous things in the world, among them the white man's notion that he is less savage than the other savages.” This might be true, a white man may be no different than any other man. However, history shows that though the white man is down, he most certainly is not out. “White Guy” by Stephen Hunt
```

### Performance text (classify this)

```text
I long to go to Detroit, not Flint.
It is 1968 and I live in Manitoba, Canada.
And as I am seven, my world is divided in two: places
that are on television, and places that aren't. Detroit is
on television.
Flint isn't.
Flint has shopping, but Detroit has the Tigers.
I see the Tigers on TV all the time.
Ty Cobb played for the Tigers, in the twenties.
I read a book about Ty Cobb once.
Ty Cobb had a .367 lifetime average.

Do you know how high that is?
Dad, we could go to a game! It would be fun!
It's an American city!
Dad says, No.
[Beat.]
Why not, Pop? We go through Flint every summer. Flint
sucks.
Why can't we go to Detroit?
Dad goes, We take one wrong turn at Detroit,
the blacks will turn over the trailer and set fire to it.
[Beat.]
That was a surprise answer.
I don't know what to say.
I don't know any blacks.
There are no blacks where I come from.
The only thing I know about blacks are what I've read
in sports biographies - From Ghetto to Glory, The Bob
Gibson Story.
Wilt Chamberlain, the only player to score 100 points in
a game. Willie Mays, the most exciting ballplayer of his
era.

Willie Mays sounds so cool, he's my favorite player, even though his era was never my era. It's best not to argue with Dad, though. Travelling is all business with him. We go through Michigan on our way to Ontario because gas is cheaper than in Canada. We write down the mileage in a book, so we can figure out miles-per-gallon. We keep track of what we spend. We rise at dawn, to maximize daylight driving. We always tell Customs the truth. For me though, travelling isn't business at all. It's total bonus points. I'm thinking, if the blacks realize we're from Canada, they won't turn our trailer over and set fire to it! Just point to the license plate, Pop! We never did anything! It's 1968, and they're burning down inner cities across America, and just because Willie Mays is your favorite ballplayer don't mean nothin’. To nobody.

We skip Detroit.
I'm the Boss, Dad says, And you do what the Boss says.
When you're the Boss, you can go to Detroit.
Detroit's not going anywhere.
We pull up outside a shopping mall in Flint.
Who wants ice cream? Pop asks.
I'm buying - as if he doesn't buy everything.
My Dad gets out, then sticks his head back inside.
You coming in, or you just gonna sit there and sulk?
I don't speak. I'm never speaking again.
Have it your way, he says. We'll be inside if you change
your mind.
They all go into the mall. I watch them, thinking, why is
the right answer
always 'no' with him?
Sometimes, I think the guy got his degree from the
University of 'No.'
That's when I make a promise to myself.
Someday, I'm getting out of there.
I'm gonna get to a place where people say 'yes.'
I'm goin' to Detroit.

[beat] Mabuti comes from Lesotho, a township by South Africa. I can't picture this Lesotho place in my mind. They don't have any teams from Lesotho. They never get on television. Lesotho is like, the Flint of South Africa. Down there by South Africa, somewhere. Country full of protestors, from the sounds of it. Protesting what? Well - South Africa. Apartheid. White Guys! Who sound like the very worst white guys ever invented. White guys even a white guy could hate. Mabuti is a small man. He has a beard. He seems wise, someone who puts the big picture before himself. He has a bullet scar on his forehead. That's where he got grazed. That's what they call it when the bullet doesn't stick, it just skims past you, leaving a permanent scar. Mabuti has friends who weren't so lucky. Mabuti came to Winnipeg. He goes to my university. He is the first black man I know.

I meet him one day at a party at the university President's house. Our university is sponsoring him. Every year, we sponsor one person from someplace awful. Generally ends up being a black guy, from Africa, as a rule. We have Yohannes Selassi, from Ethiopia. Yohannes isn't what you think when you hear 'Ethiopia.' He's not starving at all. Yohannes claims he's related to the Emperor Halle Selassie, and since none of us knows nothin’ about Ethiopia, and hey they have the same last name we accept this as fact. We got Grace Edward Galabuzzi, from Uganda. Grace is a soccer player with astonishing posture. Like Prince Charles. And to tell you the truth, Grace seems more British than African. But Mabuti is different. He seems truly African. Mabuti is a wise jester, a prankster.

If Grace Edward Galabuzzi is an Empire man, Mabuti is
his Irish counterpart.
Mabuti will always join ya for a drink.
And sometimes,
Mabuti hints at the horrors he has witnessed in life,
but he never goes into very much detail.
Of course, I do the right thing.
I'm always horrified by his stories - as if I could be
anything but. Mabuti makes me feel like he understands
me.
In fact - and this is what's so great about the guy - he
makes me feel
as if he understands how hard it is to be me,
listening to all those bad things that happened to him.
In summer, I lose track of the Africans.
They vanish from my life.
Whoosh! Africans, away.
I rediscover my old life, my high school buddies.
We have barbecues in our backyards,
go to the cottage,
play golf, watch baseball on TV;
none of us has any real plans.
We have our own indigenous way of life.
We are at home here.
Hey - we're white guys!
Nothin is a biggie...
As for the Africans - well, I don't know what happens to
the Africans in summer.
You see, I don't want to know what happens to the
Africans.
In principle, I am anti-apartheid, but in practice - well,
it would be weird,
awkward, it's summer - the thing is, my high school pals,
they don't want to meet new people. They want things to
be familiar. Until
Late one night, around midnight, the phone rings,
- and it's Mabuti. Of all people.
Hey man, how are you? He asks.
Mabuti, how you doin'?
Thinking, why are you calling me in the summer?
I'm no good man.
Why not? What's wrong?

Thinking, please don't give me more information than I
need? I'm just not doing very good man, he says. I'm
alone here.
He asks. You wanna do something? Mabuti. I'm real
tired.
Man, he says. Come on.
I need company.
[Beat.]
No, can't do it. I gotta get up early.
You take care, Mabuti. You'll be OK. 'Night!
I'm going to sleep now.
I can't go out with everyone.
I gotta go to work in the morning.
I think these really normal thoughts everyone thinks all
the time. But I have another feeling, underneath those
feelings. Something like, that one was a test, a cosmic
challenge.
And I failed.
In my own way, I said,
This is my house.
You can't come in.

OK, I'm a white guy. I know it. It's obvious, right? You
probably think I'm this
domestic beer drinking,
red meat eating, USA Today reading, ESPN watching,
normal, perfect home-owning
kind a guy!
And you'd be surprised,
how long I went
before noticing that I'm actually this Bass Ale drinking,
sushi eating,
khaki-shorts wearing, Bravo-Channel watching,
New Yorker reading emotionally-arrested
kind of renter!
[Beat.]
But then again,
To everybody else, lookin' back at me, it's so obvious,
I'm just one thing:
a white guy!
I'm part of a tribe!
Know what that means, don't you?

Construction workers sittin' on their high beams when I
walk by don't shout 'nice ***’.
Women seeing me come towards them on the street
don't, clutch their purses tighter.
[Beat.]
Cops don't shoot me by accident.
Never.
Does not happen.
To live the life of a white guy,
in a white guy's world, well, it's, it's
It's nice.
It's tremendous.
But frankly, it's not the greatest time to be me.
For one thing, my media role models suck.
The only thing you ever read about white guys these
days
is either how mean we are or how mad we are.
Witness the collected films of Michael Douglas.
And one reason why so many of us are mad
is this certain intellectual perspective
held by universities and certain political parties and non-
profit theater across America - those season tickets
theaters,
you know the ones I'm talking about, theaters
dedicated to serving audiences smarter than usual.
It's not something they say out loud - because a lot of
us are season ticket holders - but it's there, in the
subtext,
of almost everything.
You just gotta listen for it.
It goes a little like this:
who invented patriarchy?
A white guy, livin' in a cave, tired of chasing down
takeout. Who invented Apartheid?
A white guy, who showed up one day in darkest Africa
and said, to hell with Holland, I'm stayin!
And I gotta be in charge!
Who ruined the Ozone Layer?
Well, let's just say - a white guy, with perfect hair,
driving his Ford Explorer 10 MILES AN HOUR down the
Santa Monica Freeway!

Who stole rock and roll?
A fat, spangled jumpsuit wearin', 14-year-old marryin',
pill devourin',
B-movie makin', Live-in-Hawaii,
Hunka-hunka burnin’ white guy!
Dead, on a stamp!
Look we're the problem with everything!
But
To tell you the truth, when I was in college,
I hated white guys too!
In fact, I hated white guys so much
I forgot I was one.
As much as I could.
I mean, let's face it - it's tough, when you recognize the
enemy - and it's you.
I had a limited set of choices to work with.
I couldn't become a non-white guy.
I was still attracted to women.
I was ashamed of my lifelong passion for competitive
sports. [Beat ]
[Then, sadly:]

I turned inward.
Started writing. Poetry. Bad, sad, poetry.
Until I was completely disgusted with myself.
Then, I wrote a TV script - spec script - about a group
of tough, yet sensitive lesbians.
Single moms by day, Canadian documentary filmmakers
by night. Called it... Goddesses.
I even sold it, to Canadian television.
You never know, with those wacky Canadians.
To those of you out there who aren't white guys and I
can feel you out there
- and you're welcome here
you might think our little 5000 year winning streak came
at your expense.
You have a point there.
To you, I say, sorry about that.
And to those of you like me,
white guys who feel a little down,
a little browbeaten, a little frustrated, remember:
there are still things we can be proud of:
Who was first on the moon?

A white guy, with a five iron!
Who's almost all of the coaches?
White guys, even though they're almost none of the
players. Who's on the money?
White guys, white guys, and more white guys-and
pyramids.
Who wrote Death of a Salesman?
A red white guy, a well-liked white guy.
Who were the Beatles?
Tell me a white guy is the problem with everything, and I
say, OK, we did steal rock and roll.
Guilty.
And we do make easy targets.
Don't shoot!
```

---

## IC-1935: Who Are We?

- Title: Who Are We?
- Author (byline): Alan Kaufman
- Work: Jew Boy
- Publisher: Foxrock Books
- Publication date as stated: Oct 2001
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 439
- Already set (do not supply): none

### Source block (context only)

```text
Author: Alan Kaufman
Book: Jew Boy
ISBN: 978-0964374096
Publisher: Foxrock Books
Date (Month/Year): Oct 2001
```

### Introduction (context only: never use it for content warnings)

```text
Growing up in the Bronx with a deeply depressed mother who was a Holocaust survivor, Alan Kaufman came to grips with his Jewish heritage in disquieting ways: he found himself facinated by photos of German death camps, formed a clique in high school that jokingly called for "death to the Jews" and created "The Purple Jew," a comic book that featured a Jewish superhero even as Kaufman understood that "more than anything in the world, I wanted not to be Jewish." Who Are We? By Alan Kaufman
```

### Performance text (classify this)

```text
Into the past
I go like a stranger
to discover why at night
I lay alone as a child
waiting for the front door
to slam, my father gone
to night-shift work,
and my mother, Marie, to enter, unable to sleep, and tell
me
tales of childhood
war, pursued by those
who, as she spoke,
seemed to enter the room, Gestapo men in leather coats
who ordered me to pack
and descend to a waiting truck,

for I am still going to Auschwitz though a grown man in 1999 I am still boarding the freight, crushed against numbed, frightened Jews and Gypsies and Russian soldiers and homosexuals crossing frontiers to be gassed

I am her, in my heart,
though I am six feet two
and two hundred and ten pounds and have played college
football and served as a soldier
and have scars from fights
with knives and jagged
bottles smashed on bars
I am still her, little girl, hiding in chicken coops
and forests, asleep on dynamite among partisans
I am still her, brushing teeth with ashes
from the ruins of nations gutted in war
I am still her brown eyes and black hair of persecution
foraging scraps of thistle soup, a star-shaped patch
sewn to my shirt

I am still my mother every day in the streets of New York or San Francisco, the chimney skies glow and swirl with soot like night above a crematorium, or the Bronx incinerator chute where I threw out trash in a brick darkness shooting sparks

I am still her in the streets of Berkeley, walking among

sparechangers, dyed-hair punkers, gays in stud leather,
Blacks, Mexicans and Asians
I am still her rounded up among poets and thieves
and politically incorrect
social deviants
on sun-drenched sidewalks
in the Mission and the Haight, Greenwich Village, the
Lower East Side, or anywhere the weird
congregate in tolerance

And every day in this age
of intolerance,
in a mental ghetto
affirmed by the homeless,
I pass the dying
with the loud ring of my boots, ashamed to think that
perhaps my heels are the last thing
they heard
Every day I am a
survivor of AIDS and poverty

Every day I sit in cafes watching tattoos turn to
numbers and I grow angry
I want America back
I want America to be
the home I never had

And you, who are you if you hear my voice? Who are you, stranger if you read these words?

Who are we
who stand threatened
in these times of darkness? Who are we, condemned to
die, who do not know ourselves
at all?
```

---

## IC-1936: Winter Run

- Title: Winter Run
- Author (byline): Brian O’Neill
- Work: Hopewell Review, Volume 5
- Publisher: Arts Indiana Press
- Publication date as stated: 1993
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1297
- Already set (do not supply): none

### Source block (context only)

```text
Author: Brian O’Neill
Book: Hopewell Review, Volume 5
ISSN: 1069-6636
Publisher: Arts Indiana Press
Date (Month/Year): 1993
```

### Introduction (context only: never use it for content warnings)

```text
Fishing trips with my dad would begin with a lesson on knot tying, or when to set the hook, but if I waited long enough dad would begin to tell stories. Each fishing story told of relationships with brothers, or uncles, or friends. If you unfolded the story you could see love between family members -- they revealed something new about the man I cherished the most.

My dad is no longer with us – a victim of a massive heart attack. But he is still here (put hand on heart) in the stories I will pass on to my kids. I suspect my children will be touched in the same way I was as a child...by the stories.

Brian O’Neill in his poem Winter Run brings the family tradition of steelhead fishing in Indiana to life with memories and stories of his own. You can almost feel the water, smell the outdoors and envy the memories he has of his father. Winter Run by Brian O’Neill
```

### Performance text (classify this)

```text
In Northern Indiana Ioam returns to sand. Gulls scream over breakers. The French knelt believing it was the end of America.

Imagine La Salle’s surprise,
or Pierre Navarre flat
on his back: fresh water
roaring in like the sea;
cactus, wild roses, and pine
rooted in the same dune, sturgeon
running rivers, and jumbo perch.
On a bridge south of Gary
millfire blots out the stars
I’ve tasted its metallic sourdough.
Winter makes it clean somehow:
a good wind off the lake, snow
thick as goose down, and he stacks
were never there, only the silence
a blizzard makes, rivers sliding
under glass, the open pools steaming
Another kind of waking dream,
steelhead run where snaggers
take the channel. Planted from
Pacific stock, they surge and flash
in unfamiliar water because the sadness
of rivers is real: it ruined the sleep
of Michigan lumber barons
who logged whole water sheds
and sunk holes for ore, their tailings
left to leach a thousand years,
who felt the river rise in sleep
and a final exhalation disappear
in a dark that gave no reply;
towns as bankrupt as the runs
they were named for:
Iron River and Grayling
and the milltown where scarfers swear
a cougar cleared the fence
at Inland Steel: a hundred
desperate sightings followed,
in dune grass and scrub, between stacked
oil drums and silos filled with methane,
all along the lake shore ringed in fie.
I saw the foreman grin and the three
fingers on his right hand dance.
“These sons of bitching fingers,”

he told us, “the three who made it
up the river can’t stand the quiet water.
Sometimes I swear the other two
were never lost. I’ll look down
and for a second the hand is whole.
It even feels whole, then it’s gone.
It’s come to that with cougars.
It’s why the steelhead run the Calumet,”
Johansen said, “it’s why
the man’s a foreman” and David said,
“the old man’s full of shit.”
Underneatht the stab and parry,
steelhead make a winter run,
wherever we imagine a line can be thrown,
up the discharge of NIPSCO generators,
up dredged rivers steaming like soup:
Trail Creek the best of the lot,
tea colored as if stained by cedar,
clear enough to see a gravel bottom die
in the backwater behind the jams.
It’s where we drove one New Year’s Eve
to try out luck – again to test the ice
and wade a waist-deep current.
You gave me the good hole to work,
as my father might have done,
or a brother, then struggled upstream
through the drifts. Eight months
since my father died. Not a soul left
on this earth to mourn my lack of sense
or tell me to be in before dark.
Now semis are gearing down
on the iced bridge and the dark
setting in, I open his tackle box
and tie on the Little Cleo
I gave him one Christmas for a joke.
Stainless steel pressed into a spoon.
On the convex side: a funny lime body
under eight or nine yellow eyes,
some bigger than others. On the concave:
Little Cleo herself, bare-breasted,
hands locked behind her head,
a treble hook beneath. A form of life
meant to imitate another form of life.
I cast her out as a last recourse.
The dead-drift to deep water. The surprise
of a good strike. Like the day my father
swam me to the drop off, where weeds
die out for lack of light,
and pike hand in the predatory silence.
There was that great empty space
beneath us. Reasoning failed
to assure me of a bottom.
It was not so much sinking, then,
but fear of what might rise
that enlarged my arms and stiffened
the flutter in my legs.
I did not turn back but imagined
the necessity of continuing
because there was nowhere else to go.
I had left the earth. I had made
the water hum with hard
and certain strokes. Then my father
called me back. Now I pull
the fear upward, and the steelhead
rises to a surface more alien
than the sad river he was brought to,
sleek as a zeppelin, the color of sky,
the beautiful, barbed, pale tongue
exposed along a pearl jaw. You slide
the bank like an otter, enter
without a splash, the long-handled net
held exactly where it must b,
repeating what we know.
Ease him out with roots whole
and unbroken. Lay him in the snow
the gills already stunned,
the eye fixed. We should smoke
the flesh in hickory, invent
a wilderness to surround our fear,
but the world burns all along
the floodlit highway –
the lamp posts hum and shudder.
Wind has driven clouds
right to the ground Roads
are drifting over. The window
that fogged with my father’s breath
is clear. His old friend in Grayling
wears his grief without despair
or bitterness. Even so, he talks
some nights as if talking all morning
weren’t enough, clips a surgeon’s knot
and quits because his hands
are stiff, and the fly belongs
to dreams of kelp and tidal flats
where steelhead taste freshwater
in the wide estuaries. He wants
the grayling back for rivers
that never reach the sea.
His wife smiles at peacock hurl
and deer hair, the Black
Demon Streamer clamped in its vise,
the half-turned hackle,
the steelhead streaming in the snow
at Gary, the extinct replaced
by the dispossessed. For Mishawaka,
Elkhart, Wakarusa, Potawatomi
For Osceola, Oswego, Maxinkuckee.
For my grandfather laying track
from Chicago to South Bend.
For Italians and Germans and Irish
buried under rails. For Blacks marooned
in snow as north as they could walk,
who found no work or love but their own,
who held one another and did not freeze
in the shacks outside Cassopolis,
Vandalia, White Pigeon, where they dug in
and lived by what they scratched
from the dirt, and the mothers
who never threw one scrap away,
husked dried beans, canned
over coal fires. For my mother
and the women who put off pleasure
attending the needs, always the needs
of others. For my father couting
automotive parts let go without notice
and the men he worked with who carried
the week without question, the ones
who broke under fluorescent tedium.
For families driving north for perch,
who lay their sleeping children down,
drank whisky in the musty cabins and talk.
There are nights when I give myself
completely up to the emptiness of sleep,
when language slides unto its sheath
and nothing remains but the spine
attending the tidal pull of the heart,
and the spirit gathers itself
in a stillness out of which
the past is perpetually created
like a pulse, because the past is nothing
until it is imagined, and because
whatever we are begins there
and is real: a wide, slow river,
in which everything we have forgotten
or felt without knowing – a word
whispered in our ear before we knew
what the word was – rises,
and a ripple breaks the flat surface
the way grayling break a pool so gently
you’d think it was a stonefly hatching
the rings concentrically gliding outward,
one within the other. The dream
you never remember arrives like that,
and sometimes it’s a gift, a cleansing,
though we hardly know it, leaving only
the barest trace of a feeling
we cannot name, so that I shake myself
and find nothing buy my two hands
and a stiff right knee. An August moon
cutting the night haze. The light
around my wife’s red hair.
My two sons lost in sleep.
All I can offer is the image
they’ve made of me, the one
they’ll lean into like a hard current –
below them, steelhead moving in
for another winter run.
```

---

## IC-1937: Xenophobia – A Collection

- Title: Xenophobia – A Collection
- Author (byline): Daryl Ngee Chinn
- Work: Letters to America: Contemporary American Poetry on Race
- Publisher: Wayne State University Press
- Publication date as stated: Dec 1995
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1165
- Already set (do not supply): none

### Source block (context only)

```text
Author: Daryl Ngee Chinn
Book: Letters to America: Contemporary American
Poetry on Race
ISBN: 978-0814325421
Publisher: Wayne State University Press
Date (Month/Year): Dec 1995
```

### Introduction (context only: never use it for content warnings)

```text
Chinese are more than a stereotype. Chinese have been and are . . . an integral part of American society . . .

And then 2020 arrived with the first reported case of COVID-19 in Wuhan, China. Since the beginning of the pandemic, President Trump and other officials have kindled flames of anti-Asian sentiment by referring to COVID-19 as the “China Virus” and even the “kung flu.” Doing so has helped normalize anti-Asian xenophobia.

But unfortunately, this is nothing new. The racist belief that Asians carry disease goes back centuries. In the 1800s, out of fear that Chinese workers were taking jobs that could be held by white workers, white labor unions argued for an immigration ban by claiming that “Chinese” disease strains were more harmful than those carried by white people.

Skin Color from the Sun and Not Translation, Not Poetry by Daryl Ngee Chinn
```

### Performance text (classify this)

```text
Skin Color From the Sun

Chinese are

--mathematical

--docile, unassertive, quiet

-- skinny, short martial artists

--good ping pong players

--poor English speakers

--studious

--nearsighted

--good cooks and laundry workers

--engineers, doctors, or optometrists

--a model minority

--not poets . . . .

Not Translation, Not Poetry

Ask the old men in Chinatown,
the ones who washed and ironed in laundries
cooked in restaurants, fished in San Francisco Bay,
laid rocks and track from California to Utah
and then down to Los Angeles.
These old men remember
that the rocks and snow in the Sierras
are softer and warmer than memories
of interrogators and officials on Angel Island
who said, “It is my duty to question your past,
to find out if you know where the stove was
back in your home in China. And it is my judgment
that this man who calls himself your brother
and these women who claim to be your wife and mother
are liars and will be sent back to China.”

These men never had a wife to rub their tired shoulders
or to warm their bed. They never had children
climbing their laps or searching their pockets
for quarters or candy.
They never heard their mothers complaining
or saw them washing vegetables.
Even if they had owned all the tea in China,
they never drank tea with their brothers again.

That short chapter
in the middle of a book
about Chinese-American dreams fulfilled
has no darkness for your dreaming,
no scenery, demons, romance, epic<
only a spotlight on
laws, numbers, facts, dates,
history you and I
should have learned in the eleventh grade.

Go back and ask your teachers about the California Congressman who used eloquence and power in 1882 to argue and lobby for the exclusion, from the pursuit of happiness in America, of all Chinese laborers

--would-be laundrymen, houseboys,

fishermen, farmers, cigarmakers, gravediggers –
and about the Congressman who wrote the law
that kept all Chinese women
from entering the United States
from 1902 to 1946. Wasn’t that when
your grandparents came to America?

Ask the white women who never asked their husbands
why they killed Chinese
in Utah, after they finished the railroad in 1865,
in Los Angeles in 1871,
in Rock Springs, Wyoming, in 1885.
Ask the kids who ran to the docks in 1886
to watch their fathers put pigtailed men
on steamboats in Humboldt Bay.

Ask Judge Kaufman of Detroit
who said in 1982
that Robert Ebens and Michael Nitz,
who killed Vincent Chin with a Louisville Slugger,
could have probation and a suspended fin
because Vincent Chin looked Japanese.

Pretend you are Caucasian and pregnant
like Christina Tien of Grand Ledge, Michigan>
It is New Year’s Day, 1985.
Imagine how much warmth and softness
you feel when four men with knives
Slash your car tires outside in the snow,
break your living room windows with crowbars
and say, “We want to speak with your husband
and any other Chinks in the house.”

You don’t understand my anger TRANSITION

But we should try. Our poet, Daryl Ngee Chinn, has personally faced systemic racism throughout his career. But so too have Blacks, Latinos, and Jews. Is America truly a ‘melting pot’ or is America a simmering stew of unrest? Is multi-culturalism a reality or merely a pipe dream?

Skin Color From the Sun

I used to be an admissions counselor at Humboldt State University.

One day Penny, our secretary, told me to
pick up Line One.
I talked to this man from Palo Alto
about life in the dorms,

the low cost of movies and rent,

whether his daughter would need a car,

the friendly people,

the small classes of ten or fifteen.

When we were done, he thanked me
and asked my name. Daryl Chinn, I said.
Oh, he said, you speak very good English.
Where are you from?

I grew up in Richmond and El Cerrito, California, just
across the bay and north of where you’re
calling from, I said.
Well, he said, where were you born?
Salt Lake City, I said.
Well then, where were your parents from?

My mothers’ from Austin, Texas, but her brothers and sisters were born in Washington, D.C., and Utah and –

--no, he interrupted, where
were your ancestors from?
Using the California English I had learned
from my mother and father,
from my teachers at Pullman Elementary,
Granada Junior High, and Harry Ells High,
I said, My father is from Southern China,
my voice flat and dead.
I wanted to ask him,
Where did you learn to speak English so well?
Where are you from, really
from?

*****

My wife and I spent a year in Florida teaching
at the University of Central Florida in Orlando.
One day, we were waiting at a stop light
near our kids’ grade school. A busload
of junior high students pulled alongside.
Someone yelled out the window,
Go home Vietnamese.

******

Sticks and stones will break my bones but names can never hurt me.

Bullshit.

*****

I, a Chink, married this Yid broad. Our kids are half-breeds, mulattos. We drive Frog and Nazi cars, play a Jap stereo with good speakers and flatlander turntable.

*****
In the high school locker room
one day just after we showered,
Lon, next to me,
said white boys smelled funny.
When I looked at him, he held his nose
and pointed silently at Jay
behind us. Later, at lunch time,
Jay said that without nigger boys
Coach wouldn’t have a basketball team.

That year, just before I went to college,
Aunt Annie said, “Just remember,
since you’re Chinese, they
can’t tell what you are. Black people
won’t think you’re white. White people
won’t know if you’re colored.
Both might trust you. You can be
on either side. Use your race
to be whatever you want to be.”

*****
For a very long time in Europe,
Jews were forced into ghettos,
where their lives were circumscribed --
where they could live, what they could be,
who their friends could be,
where they could travel.
Some Jews found their ways out of the ghetto.
They intermarried, changed their names,
converted to Christianity,
became doctors, lawyers, royal advisors<
university scholars, and moved into
non-Jewish neighborhoods.

During the Holocaust, Adolf Hitler
convinced blond, blue-eyed women
to have babies fathered by
blond, blue-eyed men.
During the Holocaust,
if a man or woman or child
had even one grandparent who was Jewish
that person went to the ovens.

Even the children of those
blond, blue-eyed parents,
if their skin or hair or eyes
turned dark,
went to the ovens.

*****

My children come home with questions, complaints, reports. My son asks, Are we half-Jewish, half-Chinese?

My daughter complains, Someone called me a China doll.

How can we tell what part of you is Jewish or Chinese? I ask them. Your right eye? Your left shoulder? Your bones? The skin below your belly button? Tell them your ancestors came from China, that your mother is Jewish. Tell them you are all, both.
```

---

## IC-1938: Got a problem? Just pick up the phone. It solved them all—and all the same

- Title: Got a problem? Just pick up the phone. It solved them all—and all the same
- Author (byline): Not specified
- Work: Classic Prose Collection
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2599
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
way!

B

R

B

by KURT VONNEGUT, JR.

Everything was perfectly swell. There were no prisons, no slums, no insane asylums, no cripples, no poverty, no wars. All diseases were conquered. So was old age. Death, barring accidents, was an adventure for volunteers. The population of the United States was stabilized at forty-million souls. One bright morning in the Chicago Lying-in Hospital, a man named Edward K. Wehling, Jr., waited for his wife to give birth. He was the only man waiting. Not many people were born a day any more. Wehling was fifty-six, a mere stripling in a population whose average age was one hundred and twenty-nine. X-rays had revealed that his wife was going to have triplets. The children would be his first. Young Wehling was hunched in his chair, his head in his hand. He was so rumpled, so still and colorless as to be virtually invisible. His camouflage was perfect, since the waiting room had a disorderly and demoralized air, too. Chairs and ashtrays had been moved away from the walls. The floor was paved with spattered dropcloths.

Mushroom Cloud Press | Classic Prose Collection

The room was being redecorated. It was being redecorated as a memorial to a man who had volunteered to die. A sardonic old man, about two hundred years old, sat on a stepladder, painting a mural he did not like. Back in the days when people aged visibly, his age would have been guessed at thirty-five or so. Aging had touched him that much before the cure for aging was found. The mural he was working on depicted a very neat garden. Men and women in white, doctors and nurses, turned the soil, planted seedlings, sprayed bugs, spread fertilizer. Men and women in purple uniforms pulled up weeds, cut down plants that were old and sickly, raked leaves, carried refuse to trash-burners. Never, never, never—not even in medieval Holland nor old Japan—had a garden been more formal, been better tended. Every plant had all the loam, light, water, air and nourishment it could use. A hospital orderly came down the corridor, singing under his breath a popular song: If you don't like my kisses, honey, Here's what I will do: I'll go see a girl in purple, Kiss this sad world toodle-oo. If you don't want my lovin', Why should I take up all this space? I'll get off this old planet, Let some sweet baby have my place. The orderly looked in at the mural and the muralist. "Looks so real," he said, "I can practically imagine I'm standing in the middle of it." "What makes you think you're not in it?" said the painter. He gave a satiric smile. "It's called 'The Happy Garden of Life,' you know." "That's good of Dr. Hitz," said the orderly.

He was referring to one of the male figures in white, whose head was a portrait of Dr. Benjamin Hitz, the hospital's Chief Obstetrician. Hitz was a blindingly handsome man. "Lot of faces still to fill in," said the orderly. He meant that the faces of many of the figures in the mural were still blank. All blanks were to be filled with portraits of Mushroom Cloud Press | Classic Prose Collection

important people on either the hospital staff or from the Chicago Office of the Federal Bureau of Termination. "Must be nice to be able to make pictures that look like something," said the orderly. The painter's face curdled with scorn. "You think I'm proud of this daub?" he said. "You think this is my idea of what life really looks like?" "What's your idea of what life looks like?" said the orderly. The painter gestured at a foul dropcloth. "There's a good picture of it," he said. "Frame that, and you'll have a picture a damn sight more honest than this one." "You're a gloomy old duck, aren't you?" said the orderly. "Is that a crime?" said the painter. The orderly shrugged. "If you don't like it here, Grandpa—" he said, and he finished the thought with the trick telephone number that people who didn't want to live any more were supposed to call. The zero in the telephone number he pronounced "naught." The number was: "2 B R 0 2 B." It was the telephone number of an institution whose fanciful sobriquets included: "Automat," "Birdland," "Cannery," "Catbox," "De-louser," "Easy-go," "Good-by, Mother," "Happy Hooligan," "Kiss-me-quick," "Lucky Pierre," "Sheepdip," "Waring Blendor," "Weep-no-more" and "Why Worry?" "To be or not to be" was the telephone number of the municipal gas chambers of the Federal Bureau of Termination.

The painter thumbed his nose at the orderly. "When I decide it's time to go," he said, "it won't be at the Sheepdip." "A do-it-yourselfer, eh?" said the orderly. "Messy business, Grandpa. Why don't you have a little consideration for the people who have to clean up after you?" The painter expressed with an obscenity his lack of concern for the tribulations of his survivors. "The world could do with a good deal more mess, if you ask me," he said. The orderly laughed and moved on. Wehling, the waiting father, mumbled something without raising his head. And then he fell silent again.

Mushroom Cloud Press | Classic Prose Collection

A coarse, formidable woman strode into the waiting room on spike heels. Her shoes, stockings, trench coat, bag and overseas cap were all purple, the purple the painter called "the color of grapes on Judgment Day." The medallion on her purple musette bag was the seal of the Service Division of the Federal Bureau of Termination, an eagle perched on a turnstile. The woman had a lot of facial hair—an unmistakable mustache, in fact. A curious thing about gas-chamber hostesses was that, no matter how lovely and feminine they were when recruited, they all sprouted mustaches within five years or so. "Is this where I'm supposed to come?" she said to the painter. "A lot would depend on what your business was," he said. "You aren't about to have a baby, are you?" "They told me I was supposed to pose for some picture," she said. "My name's Leora Duncan." She waited. "And you dunk people," he said. "What?" she said. "Skip it," he said. "That sure is a beautiful picture," she said. "Looks just like heaven or something." "Or something," said the painter. He took a list of names from his smock pocket. "Duncan, Duncan, Duncan," he said, scanning the list. "Yes—here you are. You're entitled to be immortalized. See any faceless body here you'd like me to stick your head on? We've got a few choice ones left." She studied the mural bleakly. "Gee," she said, "they're all the same to me. I don't know anything about art." "A body's a body, eh?" he said. "All righty. As a master of fine art, I recommend this body here." He indicated a faceless figure of a woman who was carrying dried stalks to a trash-burner. "Well," said Leora Duncan, "that's more the disposal people, isn't it? I mean, I'm in service. I don't do any disposing." The painter clapped his hands in mock delight. "You say you don't know anything about art, and then you prove in the next breath that you know more about it than I do! Of course the sheave-carrier is wrong for a hostess! A snipper, a pruner—that's more your line." He pointed to a figure in purple who was sawing a dead branch from an apple tree. "How about her?" he said. "You like her at all?"

Mushroom Cloud Press | Classic Prose Collection

"Gosh—" she said, and she blushed and became humble—"that—that puts me right next to Dr. Hitz." "That upsets you?" he said. "Good gravy, no!" she said. "It's—it's just such an honor." "Ah, You... you admire him, eh?" he said. "Who doesn't admire him?" she said, worshiping the portrait of Hitz. It was the portrait of a tanned, white-haired, omnipotent Zeus, two hundred and forty years old. "Who doesn't admire him?" she said again. "He was responsible for setting up the very first gas chamber in Chicago." "Nothing would please me more," said the painter, "than to put you next to him for all time. Sawing off a limb—that strikes you as appropriate?" "That is kind of like what I do," she said. She was demure about what she did. What she did was make people comfortable while she killed them.

And, while Leora Duncan was posing for her portrait, into the waitingroom bounded Dr. Hitz himself. He was seven feet tall, and he boomed with importance, accomplishments, and the joy of living. "Well, Miss Duncan! Miss Duncan!" he said, and he made a joke. "What are you doing here?" he said. "This isn't where the people leave. This is where they come in!" "We're going to be in the same picture together," she said shyly. "Good!" said Dr. Hitz heartily. "And, say, isn't that some picture?" "I sure am honored to be in it with you," she said. "Let me tell you," he said, "I'm honored to be in it with you. Without women like you, this wonderful world we've got wouldn't be possible." He saluted her and moved toward the door that led to the delivery rooms. "Guess what was just born," he said. "I can't," she said. "Triplets!" he said. "Triplets!" she said. She was exclaiming over the legal implications of triplets.

Mushroom Cloud Press | Classic Prose Collection

The law said that no newborn child could survive unless the parents of the child could find someone who would volunteer to die. Triplets, if they were all to live, called for three volunteers. "Do the parents have three volunteers?" said Leora Duncan. "Last I heard," said Dr. Hitz, "they had one, and were trying to scrape another two up." "I don't think they made it," she said. "Nobody made three appointments with us. Nothing but singles going through today, unless somebody called in after I left. What's the name?" "Wehling," said the waiting father, sitting up, red-eyed and frowzy. "Edward K. Wehling, Jr., is the name of the happy father-to-be." He raised his right hand, looked at a spot on the wall, gave a hoarsely wretched chuckle. "Present," he said. "Oh, Mr. Wehling," said Dr. Hitz, "I didn't see you." "The invisible man," said Wehling. "They just phoned me that your triplets have been born," said Dr. Hitz. "They're all fine, and so is the mother. I'm on my way in to see them now." "Hooray," said Wehling emptily. "You don't sound very happy," said Dr. Hitz. "What man in my shoes wouldn't be happy?" said Wehling. He gestured with his hands to symbolize care-free simplicity. "All I have to do is pick out which one of the triplets is going to live, then deliver my maternal grandfather to the Happy Hooligan, and come back here with a receipt."

Dr. Hitz became rather severe with Wehling, towered over him. "You don't believe in population control, Mr. Wehling?" he said. "I think it's perfectly keen," said Wehling tautly. "Would you like to go back to the good old days, when the population of the Earth was twenty billion—about to become forty billion, then eighty billion, then one hundred and sixty billion? Do you know what a drupelet is, Mr. Wehling?" said Hitz. "Nope," said Wehling sulkily.

Mushroom Cloud Press | Classic Prose Collection

"A drupelet, Mr. Wehling, is one of the little knobs, one of the little pulpy grains of a blackberry," said Dr. Hitz. "Without population control, human beings would now be packed on this surface of this old planet like drupelets on a blackberry! Think of it!" Wehling continued to stare at the same spot on the wall. "In the year 2000," said Dr. Hitz, "before scientists stepped in and laid down the law, there wasn't even enough drinking water to go around, and nothing to eat but sea-weed—and still people insisted on their right to reproduce like jackrabbits. And their right, if possible, to live forever." "I want those kids," said Wehling quietly. "I want all three of them." "Of course you do," said Dr. Hitz. "That's only human." "I don't want my grandfather to die, either," said Wehling. "Nobody's really happy about taking a close relative to the Catbox," said Dr. Hitz gently, sympathetically. "I wish people wouldn't call it that," said Leora Duncan. "What?" said Dr. Hitz. "I wish people wouldn't call it 'the Catbox,' and things like that," she said. "It gives people the wrong impression." "You're absolutely right," said Dr. Hitz. "Forgive me." He corrected himself, gave the municipal gas chambers their official title, a title no one ever used in conversation. "I should have said, 'Ethical Suicide Studios,'" he said. "That sounds so much better," said Leora Duncan. "This child of yours—whichever one you decide to keep, Mr. Wehling," said Dr. Hitz. "He or she is going to live on a happy, roomy, clean, rich planet, thanks to population control. In a garden like that mural there." He shook his head. "Two centuries ago, when I was a young man, it was a hell that nobody thought could last another twenty years. Now centuries of peace and plenty stretch before us as far as the imagination cares to travel." He smiled luminously. The smile faded as he saw that Wehling had just drawn a revolver. Wehling shot Dr. Hitz dead. "There's room for one—a great big one," he said. And then he shot Leora Duncan. "It's only death," he said to her as she fell. "There! Room for two."

Mushroom Cloud Press | Classic Prose Collection

And then he shot himself, making room for all three of his children.
Nobody came running. Nobody, seemingly, heard the shots.
The painter sat on the top of his stepladder, looking down reflectively on the sorry
scene.

The painter pondered the mournful puzzle of life demanding to be born and, once born, demanding to be fruitful ... to multiply and to live as long as possible—to do all that on a very small planet that would have to last forever. All the answers that the painter could think of were grim. Even grimmer, surely, than a Catbox, a Happy Hooligan, an Easy Go. He thought of war. He thought of plague. He thought of starvation. He knew that he would never paint again. He let his paintbrush fall to the drop-cloths below. And then he decided he had had about enough of life in the Happy Garden of Life, too, and he came slowly down from the ladder. He took Wehling's pistol, really intending to shoot himself. But he didn't have the nerve. And then he saw the telephone booth in the corner of the room. He went to it, dialed the well-remembered number: "2 B R 0 2 B." "Federal Bureau of Termination," said the very warm voice of a hostess. "How soon could I get an appointment?" he asked, speaking very carefully. "We could probably fit you in late this afternoon, sir," she said. "It might even be earlier, if we get a cancellation." "All right," said the painter, "fit me in, if you please." And he gave her his name, spelling it out. "Thank you, sir," said the hostess. "Your city thanks you; your country thanks you; your planet thanks you. But the deepest thanks of all is from future generations."

THE END
```

---

## IC-1939: A Haunted House

- Title: A Haunted House
- Author (byline): Virginia Woolf
- Work: Classic Prose Collection
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 686
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
Whatever hour you woke there was a door shutting. From room to room they went, hand in hand, lifting here, opening there, making sure—a ghostly couple.

"Here we left it," she said. And he added, "Oh, but here too!" "It's upstairs," she murmured. "And in the garden," he whispered. "Quietly," they said, "or we shall wake them."

But it wasn't that you woke us. Oh, no. "They're looking for it; they're drawing the curtain," one might say, and so read on a page or two. "Now they've found it," one would be certain, stopping the pencil on the margin. And then, tired of reading, one might rise and see for oneself, the house all empty, the doors standing open, only the wood pigeons bubbling with content and the hum of the threshing machine sounding from the farm. "What did I come in here for? What did I want to find?" My hands were empty. "Perhaps it's upstairs then?" The apples were in the loft. And so down again, the garden still as ever, only the book had slipped into the grass.

But they had found it in the drawing room. Not that one could ever see them. The window panes reflected apples, reflected roses; all the leaves were green in the glass. If they moved in the drawing room, the apple only turned its yellow side. Yet, the moment after, if the door was opened, spread about the floor, hung upon the walls, pendant from the ceiling—what? My hands were empty. The shadow of a thrush crossed the carpet; from the deepest wells of silence the wood pigeon drew its bubble of sound. "Safe, safe, safe," the pulse of the house beat softly. "The treasure buried; the room ..." the pulse stopped short. Oh, was that the buried treasure?

A moment later the light had faded. Out in the garden then? But the trees spun darkness for a wandering beam of sun. So fine, so rare, coolly sunk beneath the surface the beam I sought always burnt behind the glass. Death was the glass; death was between us; coming to the woman first, hundreds of years ago, leaving the house, sealing all the windows; the rooms were darkened. He left it, left her, went North, went East, saw the stars turned in the Southern sky; sought the house, found it dropped beneath the Downs. "Safe, safe, safe," the pulse of the house beat gladly. "The Treasure yours."

The wind roars up the avenue. Trees stoop and bend this way and that. Moonbeams splash and spill wildly in the rain. But the beam of the lamp falls straight from the window. The candle burns stiff and still. Wandering through the house, opening the windows, whispering not to wake us, the ghostly couple seek their joy.

"Here we slept," she says. And he adds, "Kisses without number." "Waking in the morning—" "Silver between the trees—" "Upstairs—" "In the garden—" "When Mushroom Cloud Press | Classic Prose Collection

summer came—" "In winter snowtime—" The doors go shutting far in the distance, gently knocking like the pulse of a heart.

Nearer they come; cease at the doorway. The wind falls, the rain slides silver down the glass. Our eyes darken; we hear no steps beside us; we see no lady spread her ghostly cloak. His hands shield the lantern. "Look," he breathes. "Sound asleep. Love upon their lips."

Stooping, holding their silver lamp above us, long they look and deeply. Long they pause. The wind drives straightly; the flame stoops slightly. Wild beams of moonlight cross both floor and wall, and, meeting, stain the faces bent; the faces pondering; the faces that search the sleepers and seek their hidden joy.

"Safe, safe, safe," the heart of the house beats proudly. "Long years—" he sighs. "Again you found me." "Here," she murmurs, "sleeping; in the garden reading; laughing, rolling apples in the loft. Here we left our treasure—" Stooping, their light lifts the lids upon my eyes. "Safe! safe! safe!" the pulse of the house beats wildly. Waking, I cry "Oh, is this your buried treasure? The light in the heart."
```

---

## IC-1940: Gabriel-Ernest

- Title: Gabriel-Ernest
- Author (byline): Saki (H.H. Munro)
- Work: Classic Prose Collection
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2505
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
"There is a wild beast in your woods," said the artist Cunningham, as he was being driven to the station. It was the only remark he had made during the drive, but as Van Cheele had talked incessantly his companion's silence had not been noticeable.

"A stray fox or two and some resident weasels. Nothing more formidable," said Van Cheele. The artist said nothing.

"What did you mean about a wild beast?" said Van Cheele later, when they were on the platform.

"Nothing. My imagination. Here is the train," said Cunningham.

That afternoon Van Cheele went for one of his frequent rambles through his woodland property. He had a stuffed bittern in his study, and knew the names of quite a number of wild flowers, so his aunt had possibly some justification in describing him as a great naturalist. At any rate, he was a great walker. It was his custom to take mental notes of everything he saw during his walks, not so much for the purpose of assisting contemporary science as to provide topics for conversation afterwards. When the bluebells began to show themselves in flower he made a point of informing every one of the fact; the season of the year might have warned his hearers of the likelihood of such an occurrence, but at least they felt that he was being absolutely frank with them.

Mushroom Cloud Press | Classic Prose Collection

What Van Cheele saw on this particular afternoon was, however, something far removed from his ordinary range of experience. On a shelf of smooth stone overhanging a deep pool in the hollow of an oak coppice a boy of about sixteen lay asprawl, drying his wet brown limbs luxuriously in the sun. His wet hair, parted by a recent dive, lay close to his head, and his light-brown eyes, so light that there was an almost tigerish gleam in them, were turned towards Van Cheele with a certain lazy watchfulness. It was an unexpected apparition, and Van Cheele found himself engaged in the novel process of thinking before he spoke. Where on earth could this wild-looking boy hail from? The miller's wife had lost a child some two months ago, supposed to have been swept away by the mill-race, but that had been a mere baby, not a half-grown lad.

"What are you doing there?" he demanded.

"Obviously, sunning myself," replied the boy.

"Where do you live?"

"Here, in these woods."

"You can't live in the woods," said Van Cheele.

"They are very nice woods," said the boy, with a touch of patronage in his voice.

"But where do you sleep at night?"

"I don't sleep at night; that's my busiest time."

Van Cheele began to have an irritated feeling that he was grappling with a problem that was eluding him.

"What do you feed on?" he asked.

Mushroom Cloud Press | Classic Prose Collection

"Flesh," said the boy, and he pronounced the word with slow relish, as though he were tasting it.

"Flesh! What Flesh?"

"Since it interests you, rabbits, wild-fowl, hares, poultry, lambs in their season, children when I can get any; they're usually too well locked in at night, when I do most of my hunting. It's quite two months since I tasted child-flesh."

Ignoring the chaffing nature of the last remark Van Cheele tried to draw the boy on the subject of possible poaching operations.

"You're talking rather through your hat when you speak of feeding on hares." (Considering the nature of the boy's toilet the simile was hardly an apt one.) "Our hillside hares aren't easily caught."

"At night I hunt on four feet," was the somewhat cryptic response.

"I suppose you mean that you hunt with a dog?" hazarded Van Cheele.

The boy rolled slowly over on to his back, and laughed a weird low laugh, that was pleasantly like a chuckle and disagreeably like a snarl.

"I don't fancy any dog would be very anxious for my company, especially at night."

Van Cheele began to feel that there was something positively uncanny about the strange-eyed, strange-tongued youngster.

"I can't have you staying in these woods," he declared authoritatively.

"I fancy you'd rather have me here than in your house," said the boy.

Mushroom Cloud Press | Classic Prose Collection

The prospect of this wild, nude animal in Van Cheele's primly ordered house was certainly an alarming one.

"If you don't go. I shall have to make you," said Van Cheele.

The boy turned like a flash, plunged into the pool, and in a moment had flung his wet and glistening body half-way up the bank where Van Cheele was standing. In an otter the movement would not have been remarkable; in a boy Van Cheele found it sufficiently startling. His foot slipped as he made an involuntarily backward movement, and he found himself almost prostrate on the slippery weed-grown bank, with those tigerish yellow eyes not very far from his own. Almost instinctively he half raised his hand to his throat. The boy laughed again, a laugh in which the snarl had nearly driven out the chuckle, and then, with another of his astonishing lightning movements, plunged out of view into a yielding tangle of weed and fern.

"What an extraordinary wild animal!" said Van Cheele as he picked himself up. And then he recalled Cunningham's remark "There is a wild beast in your woods."

Walking slowly homeward, Van Cheele began to turn over in his mind various local occurrences which might be traceable to the existence of this astonishing young savage.

Something had been thinning the game in the woods lately, poultry had been missing from the farms, hares were growing unaccountably scarcer, and complaints had reached him of lambs being carried off bodily from the hills. Was it possible that this wild boy was really hunting the countryside in company with some clever poacher dogs? He had spoken of hunting "four-footed" by night, but then, again, he had hinted strangely at no dog caring to come near him, "especially at night." It was certainly puzzling. And then, as Van Cheele ran his mind over the various depredations that had been committed during the last month or two, he Mushroom Cloud Press | Classic Prose Collection

came suddenly to a dead stop, alike in his walk and his speculations. The child missing from the mill two months ago--the accepted theory was that it had tumbled into the mill-race and been swept away; but the mother had always declared she had heard a shriek on the hill side of the house, in the opposite direction from the water. It was unthinkable, of course, but he wished that the boy had not made that uncanny remark about child-flesh eaten two months ago. Such dreadful things should not be said even in fun.

Van Cheele, contrary to his usual wont, did not feel disposed to be communicative about his discovery in the wood. His position as a parish councillor and justice of the peace seemed somehow compromised by the fact that he was harbouring a personality of such doubtful repute on his property; there was even a possibility that a heavy bill of damages for raided lambs and poultry might be laid at his door. At dinner that night he was quite unusually silent.

"Where's your voice gone to?" said his aunt. "One would think you had seen a wolf."

Van Cheele, who was not familiar with the old saying, thought the remark rather foolish; if he HAD seen a wolf on his property his tongue would have been extraordinarily busy with the subject.

At breakfast next morning Van Cheele was conscious that his feeling of uneasiness regarding yesterday's episode had not wholly disappeared, and he resolved to go by train to the neighbouring cathedral town, hunt up Cunningham, and learn from him what he had really seen that had prompted the remark about a wild beast in the woods. With this resolution taken, his usual cheerfulness partially returned, and he hummed a bright little melody as he sauntered to the morning-room for his customary cigarette. As he entered the room the melody made way abruptly for a pious invocation. Gracefully asprawl on the ottoman, in an attitude of almost Mushroom Cloud Press | Classic Prose Collection

exaggerated repose, was the boy of the woods. He was drier than when Van Cheele had last seen him, but no other alteration was noticeable in his toilet.

"How dare you come here?" asked Van Cheele furiously.

"You told me I was not to stay in the woods," said the boy calmly.

"But not to come here. Supposing my aunt should see you!"

And with a view to minimising that catastrophe, Van Cheele hastily obscured as much of his unwelcome guest as possible under the folds of a Morning Post. At that moment his aunt entered the room.

"This is a poor boy who has lost his way--and lost his memory. He doesn't know who he is or where he comes from," explained Van Cheele desperately, glancing apprehensively at the waif's face to see whether he was going to add inconvenient candour to his other savage propensities.

Miss Van Cheele was enormously interested.

"Perhaps his underlinen is marked," she suggested.

"He seems to have lost most of that, too," said Van Cheele, making frantic little grabs at the Morning Post to keep it in its place.

A naked homeless child appealed to Miss Van Cheele as warmly as a stray kitten or derelict puppy would have done.

"We must do all we can for him," she decided, and in a very short time a messenger, dispatched to the rectory, where a page-boy was kept, had returned with a suit of pantry clothes, and the necessary accessories of shirt, shoes, collar, etc. Clothed, clean, and groomed, the boy lost none of his uncanniness in Van Cheele's eyes, but his aunt found him sweet.

Mushroom Cloud Press | Classic Prose Collection

"We must call him something till we know who he really is," she said. "Gabriel- Ernest, I think; those are nice suitable names."

Van Cheele agreed, but he privately doubted whether they were being grafted on to a nice suitable child. His misgivings were not diminished by the fact that his staid and elderly spaniel had bolted out of the house at the first incoming of the boy, and now obstinately remained shivering and yapping at the farther end of the orchard, while the canary, usually as vocally industrious as Van Cheele himself, had put itself on an allowance of frightened cheeps. More than ever he was resolved to consult Cunningham without loss of time.

As he drove off to the station his aunt was arranging that Gabriel- Ernest should help her to entertain the infant members of her Sunday-school class at tea that afternoon.

Cunningham was not at first disposed to be communicative.

"My mother died of some brain trouble," he explained, "so you will understand why I am averse to dwelling on anything of an impossibly fantastic nature that I may see or think that I have seen."

"But what DID you see?" persisted Van Cheele.

"What I thought I saw was something so extraordinary that no really sane man could dignify it with the credit of having actually happened. I was standing, the last evening I was with you, half-hidden in the hedgegrowth by the orchard gate, watching the dying glow of the sunset. Suddenly I became aware of a naked boy, a bather from some neighbouring pool, I took him to be, who was standing out on the bare hillside also watching the sunset. His pose was so suggestive of some wild faun of Pagan myth that I instantly wanted to engage him as a model, and in another moment I think I should have hailed him. But just then the sun dipped out Mushroom Cloud Press | Classic Prose Collection

of view, and all the orange and pink slid out of the landscape, leaving it cold and grey. And at the same moment an astounding thing happened--the boy vanished too!"

"What! vanished away into nothing?" asked Van Cheele excitedly.

"No; that is the dreadful part of it," answered the artist; "on the open hillside where the boy had been standing a second ago, stood a large wolf, blackish in colour, with gleaming fangs and cruel, yellow eyes. You may think--"

But Van Cheele did not stop for anything as futile as thought. Already he was tearing at top speed towards the station. He dismissed the idea of a telegram. "Gabriel-Ernest is a werewolf" was a hopelessly inadequate effort at conveying the situation, and his aunt would think it was a code message to which he had omitted to give her the key. His one hope was that he might reach home before sundown. The cab which he chartered at the other end of the railway journey bore him with what seemed exasperating slowness along the country roads, which were pink and mauve with the flush of the sinking sun. His aunt was putting away some unfinished jams and cake when he arrived.

"Where is Gabriel-Ernest?" he almost screamed.

"He is taking the little Toop child home," said his aunt. "It was getting so late, I thought it wasn't safe to let it go back alone. What a lovely sunset, isn't it?"

But Van Cheele, although not oblivious of the glow in the western sky, did not stay to discuss its beauties. At a speed for which he was scarcely geared he raced along the narrow lane that led to the home of the Toops. On one side ran the swift current of the mill-stream, on the other rose the stretch of bare hillside. A dwindling rim of red sun showed still on the skyline, and the next turning must bring him in view of the ill-assorted couple he was pursuing. Then the colour went suddenly out of Mushroom Cloud Press | Classic Prose Collection

things, and a grey light settled itself with a quick shiver over the landscape. Van Cheele heard a shrill wail of fear, and stopped running.

Nothing was ever seen again of the Toop child or Gabriel-Ernest, but the latter's discarded garments were found lying in the road so it was assumed that the child had fallen into the water, and that the boy had stripped and jumped in, in a vain endeavour to save it. Van Cheele and some workmen who were near by at the time testified to having heard a child scream loudly just near the spot where the clothes were found. Mrs. Toop, who had eleven other children, was decently resigned to her bereavement, but Miss Van Cheele sincerely mourned her lost foundling. It was on her initiative that a memorial brass was put up in the parish church to "Gabriel-Ernest, an unknown boy, who bravely sacrificed his life for another."

Van Cheele gave way to his aunt in most things, but he flatly refused to subscribe to the Gabriel-Ernest memorial.
```

---

## IC-1941: KING LEAR

- Title: KING LEAR
- Author (byline): E. Nesbit
- Work: Classic Prose Collection
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1053
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
King Lear was old and tired. He was aweary of the business of his kingdom, and wished only to end his days quietly near his three daughters. Two of his daughters were married to the Dukes of Albany and Cornwall; and the Duke of Burgundy and the King of France were both suitors for the hand of Cordelia, his youngest daughter.

Lear called his three daughters together, and told them that he proposed to divide his kingdom between them. “But first,” said he, “I should like to know much you love me.”

Goneril, who was really a very wicked woman, and did not love her father at all, said she loved him more than words could say; she loved him dearer than eyesight, space or liberty, more than life, grace, health, beauty, and honor.

“I love you as much as my sister and more,” professed Regan, “since I care for nothing but my father's love.”

Lear was very much pleased with Regan's professions, and turned to his youngest daughter, Cordelia. “Now, our joy, though last not least,” he said, “the best part of my kingdom have I kept for you. What can you say?”

“Nothing, my lord,” answered Cordelia.

“Nothing can come of nothing. Speak again,” said the King.

And Cordelia answered, “I love your Majesty according to my duty--no more, no less.”

And this she said, because she was disgusted with the way in which her sisters professed love, when really they had not even a right sense of duty to their old father.

“I am your daughter,” she went on, “and you have brought me up and loved me, and I return you those duties back as are right and fit, obey you, love you, and most honor you.”

Lear, who loved Cordelia best, had wished her to make more extravagant professions of love than her sisters. “Go,” he said, “be for ever a stranger to my heart and me.”

The Earl of Kent, one of Lear's favorite courtiers and captains, tried to say a word for Cordelia's sake, but Lear would not listen. He divided the kingdom between Goneril and Regan, and told them that he should only keep a hundred knights at arms, and would live with his daughters by turns.

When the Duke of Burgundy knew that Cordelia would have no share of the kingdom, he gave up his courtship of her. But the King of France was wiser, and said, “Thy dowerless daughter, King, is Queen of us--of ours, and our fair France.”

Mushroom Cloud Press | Classic Prose Collection

“Take her, take her,” said the King; “for I will never see that face of hers again.”

So Cordelia became Queen of France, and the Earl of Kent, for having ventured to take her part, was banished from the kingdom. The King now went to stay with his daughter Goneril, who had got everything from her father that he had to give, and now began to grudge even the hundred knights that he had reserved for himself. She was harsh and undutiful to him, and her servants either refused to obey his orders or pretended that they did not hear them.

Now the Earl of Kent, when he was banished, made as though he would go into another country, but instead he came back in the disguise of a servingman and took service with the King. The King had now two friends--the Earl of Kent, whom he only knew as his servant, and his Fool, who was faithful to him. Goneril told her father plainly that his knights only served to fill her Court with riot and feasting; and so she begged him only to keep a few old men about him such as himself.

“My train are men who know all parts of duty,” said Lear. “Goneril, I will not trouble you further--yet I have left another daughter.”

And his horses being saddled, he set out with his followers for the castle of Regan. But she, who had formerly outdone her sister in professions of attachment to the King, now seemed to outdo her in undutiful conduct, saying that fifty knights were too many to wait on him, and Goneril (who had hurried thither to prevent Regan showing any kindness to the old King) said five were too many, since her servants could wait on him.

Then when Lear saw that what they really wanted was to drive him away, he left them. It was a wild and stormy night, and he wandered about the heath half mad with misery, and with no companion but the poor Fool. But presently his servant, the good Earl of Kent, met him, and at last persuaded him to lie down in a wretched little hovel. At daybreak the Earl of Kent removed his royal master to Dover, and hurried to the Court of France to tell Cordelia what had happened.

Cordelia's husband gave her an army and with it she landed at Dover. Here she found poor King Lear, wandering about the fields, wearing a crown of nettles and weeds. They brought him back and fed and clothed him, and Cordelia came to him and kissed him.

“You must bear with me,” said Lear; “forget and forgive. I am old and foolish.”

And now he knew at last which of his children it was that had loved him best, and who was worthy of his love.

Goneril and Regan joined their armies to fight Cordelia's army, and were successful; and Cordelia and her father were thrown into prison. Then Goneril's husband, the Duke of Albany, who was a good man, and had not known how Mushroom Cloud Press | Classic Prose Collection

wicked his wife was, heard the truth of the whole story; and when Goneril found that her husband knew her for the wicked woman she was, she killed herself, having a little time before given a deadly poison to her sister, Regan, out of a spirit of jealousy.

But they had arranged that Cordelia should be hanged in prison, and though the Duke of Albany sent messengers at once, it was too late. The old King came staggering into the tent of the Duke of Albany, carrying the body of his dear daughter Cordelia, in his arms.

And soon after, with words of love for her upon his lips, he fell with her still in his arms, and died.
```

---

## IC-1942: My Brother Henry

- Title: My Brother Henry
- Author (byline): J.M. Barrie
- Work: Classic Prose Collection
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1556
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
At first sight it may not, perhaps, seem quite the thing that I should be hilarious because I have at last had the courage to kill my brother Henry. For some time, however, Henry had been annoying me.

Strictly speaking, I never had a brother Henry. It is just fifteen months since I began to acknowledge that there was such a person. It came about in this way:—I have a friend of the name of Fenton, who, like myself, lives in London. His house is so conveniently situated that I can go there and back in one day. About a year and a half ago I was at Fenton’s, and he remarked that he had met a man the day before who knew my brother Henry. Not having a brother Henry, I felt that there must be a mistake somewhere; so I suggested that Fenton’s friend had gone wrong in the name. My only brother, I pointed out with the suavity of manner that makes me a general favourite, was called Alexander.

“Yes,” said Fenton, “but he spoke of Alexander also.”

Even this did not convince me that I had a brother Henry, and I asked Fenton the name of his friend. Scudamour was the name, and the gentleman had met my brothers Alexander and Henry some six years previously in Paris. When I heard this I probably frowned; for then I knew who my brother Henry was. Strange though it may seem, I was my own brother Henry.

I distinctly remembered meeting this man Scudamour at Paris during the time that Alexander and I were there for a week’s pleasure, and quarrelled every day. I explained this to Fenton; and there, for the time being, the matter rested. I had, however, by no means heard the last of Henry. Several times afterwards I heard from various persons that Scudamour wanted to meet me because he knew my brother Henry.

At last we did meet, at a Bohemian supper-party in Furnival’s Inn; and, almost as soon as he saw me, Scudamour asked where Henry was now. This was precisely what I feared. I am a man who always looks like a boy. There are few persons of my age in London who retain their boyish appearance as long as I have done; indeed, this is the curse of my life. Though I am approaching the age of thirty, I pass for twenty; and I have observed old gentlemen frown at my precocity when I said a good thing or helped myself to a second glass of wine. There was, therefore, Mushroom Cloud Press | Classic Prose Collection

nothing surprising in Scudamour’s remark that, when he had the pleasure of meeting Henry, Henry must have been about the age that I had now reached.

All would have been well had I explained the real state of affairs to this annoying man; but, unfortunately for myself, I loathe entering upon explanations to anybody about anything. When I ring for my boots and my servant thinks I want a glass of water, I drink the water and remain indoors. Much, then, did I dread a discussion with Scudamour, his surprise when he heard that I was Henry (my Christian name is Thomas), and his comments on my youthful appearance. Besides, I was at that moment carving a tough fowl; and, as I learned to carve from a handbook, I can make no progress unless I keep muttering to myself, “Cut from A to B, taking care to pass along the line C D, and sever the wing K from the body at the point F.”

There was no likelihood of my meeting Scudamour again, so the easiest way to get rid of him seemed to be to humour him. I therefore told him that Henry was in India, married, and doing well.

“Remember me to Henry when you write to him,” was Scudamour’s last remark to me that evening.

A few weeks later someone tapped me on the shoulder in Oxford Street. It was Scudamour.

“Heard from Henry?” he asked. I said I had heard by the last mail.

“Anything particular in the letter?” I felt it would not do to say there was nothing particular in a letter which had come all the way from India, so I hinted that Henry had had trouble with his wife. By this I meant that her health was bad; but he took it up in another way, and I did not set him right.

“Ah, ah!” he said, shaking his head sagaciously, “I’m sorry to hear that. Poor Henry!”

“Poor old boy!” was all I could think of replying.

“How about the children?” Scudamour asked.

“Oh, the children,” I said, with what I thought presence of mind, “are coming to England.”

Mushroom Cloud Press | Classic Prose Collection

“To stay with Alexander?” he asked; for Alexander is a married man. My answer was that Alexander was expecting them by the middle of next month; and eventually Scudamour went away muttering “Poor Henry!”

In a month or so we met again. “No word of Henry’s getting leave of absence?” asked Scudamour. I replied shortly that Henry had gone to live in Bombay, and would not be home for years. He saw that I was brusque, so what does he do but draw me aside for a quiet explanation.

“I suppose,” he said, “you are annoyed because I told Fenton that Henry’s wife had run away from him. The fact is I did it for your good. You see I happened to make a remark to Fenton about your brother Henry, and he said that there was no such person. Of course, I laughed at that, and pointed out not only that I had the pleasure of Henry’s acquaintance, but that you and I had a talk about the old fellow every time we met.

“ ‘Well,’ Fenton said, ‘this is a most remarkable thing; for Tom,’ meaning you, ‘said to me in this very room, sitting in that very chair, that Alexander was his only brother.’

“I saw that Fenton resented your concealing the existence of your brother Henry from him, so I thought the most friendly thing I could do was to tell him that your reticence was doubtless due to the fact that Henry’s private affairs were troubling you. Naturally, in the circumstances, you did not want to talk about Henry.”

I shook Scudamour by the hand, telling him that he had acted judiciously; but if I could have stabbed him quietly at that moment I dare say I should have done it. I did not see Scudamour again for a long time, for I took care to keep out of his way; but I heard first from him and then of him. One day he wrote to me saying that his nephew was going to Bombay, and would I be so good as to give the youth an introduction to my brother Henry? He also asked me to dine with him and his nephew. I declined the dinner, but I sent the nephew the required note of introduction to Henry.

The next I heard of Scudamour was from Fenton.

“By the way,” said Fenton, “Scudamour is in Edinburgh at present.” I trembled, for Edinburgh is where Alexander lives.

Mushroom Cloud Press | Classic Prose Collection

“What has taken him there?” I asked, with assumed carelessness. Fenton believed it was business; “but,” he added, “Scudamour asked me to tell you that he meant to call on Alexander, as he was anxious to see Henry’s children.”

A few days afterwards I had a telegram from Alexander, who generally uses this means of communication when he corresponds with me. “Do you know a man Scudamour? reply,” was what Alexander said. I thought of answering that we had met a man of that name when we were in Paris; but, on the whole, replied boldly: “Know no one of the name of Scudamour.”

About two months ago I passed Scudamour in Regent Street, and he did not recognise me. This I could have borne if there had been no more of Henry; but I knew that Scudamour was now telling everybody about Henry’s wife. By-and-by I got a letter from an old friend of Alexander’s, asking me if there was any truth in a report that Alexander was going to Bombay. Soon afterwards Alexander wrote to me to say that he had been told by several persons that I was going to Bombay. In short, I saw that the time had come for killing Henry.

So I told Fenton that Henry had died of fever, deeply regretted; and asked him to be sure to tell Scudamour, who had always been interested in the deceased’s welfare. The other day Fenton told me that he had communicated the sad intelligence to Scudamour.

“How did he take it?” I asked.

“Well,” Fenton said, reluctantly, “he told me that when he was up in Edinburgh he did not get on well with Alexander; but he expressed great curiosity as to Henry’s children.”

“Ah,” I said, “the children were both drowned in the Forth; a sad affair—we can’t bear to talk of it.” I am not likely to see much of Scudamour again, nor is Alexander. Scudamour now goes about saying that Henry was the only one of us he really liked.
```

---

## IC-1943: Several Trojan Skirmishes and One Wooden Animal

- Title: Several Trojan Skirmishes and One Wooden Animal
- Author (byline): Not specified
- Work: Classic Prose Collection
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2588
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
The Story of the Greatest War on Earth

By Clyde Hendrickson

A long, long time ago, in a land far, far away, the great gods of Olympus were attending the wedding of King Lysol and the sea nymph Tide. Unfortunately, the deities had forgotten to invite the goddess of discord, Eris. She was enraged - the gods saw her as unimportant and troublesome, and she knew she would be missing a delightful salad bar at the feast. So, she decided to cause discord, because, after all, that was her job.

In the middle of the proceedings, Eris heaved a golden apple through the window marked "To The Most Stupid.” Of course, none of the gods wanted this title, and they all fought amongst themselves to decide which would not get the apple. Zeus, who was lazy and had other fish to fry, decided that simple-minded Paris would do the honors of judging the immortal gods.

Each god, to try to win his favor, decided to bribe Paris. The competition came down to two women, Hera and Aphrodite. Hera, knowing that she was not too bright, approached Paris first.

She said, "Paris, if you give the apple to Aphrodite, I will let you conquer all of Europe, Asia, and maybe even New Jersey."

To this, simple-minded Paris said, " Uhh... Duhh.... Ummm... What?"

Aphrodite was next. She was just a tad smarter than Hera, and knew what Paris really wanted.

"If you give the apple to Hera, I will give you the most beautiful woman in the world," The goddess of love told him.

Paris replied, "Um, all right. I don't like New Jersey, anyway."

The judgment had been made. Hera was the stupidest of the Olympians and received the golden apple. She vowed to make Paris pay, but he paid little attention as he was led away by Aphrodite. Little did the simpleton know that Hades has no fury like a goddess's scorn.

The most beautiful woman in the world was no doubt Helen. Unfortunately, she had been dead for 400 years, and her mummified body was a tourist attraction at the house of Manyscars in Sparta. Aphrodite gave Paris the power to raise her from the dead, and she returned with him to his home state of Troy.

Manyscars, furious that his prized cashcow had been stolen from him by an Asia Minor hillbilly, united all of Greece against Troy. With Hera and Athena at his side, he was ready to lay siege to the wondrous city across the sea. However, two men were missing from his party. They were King Ondajon of the island of Ithaca, and the invulnerable, very vain warrior, Tendinitis.

The king of Sparta first sent his messenger to the land of King Ondajon. When the messenger arrived, the ruler was nowhere to be found, so he called out in the castle hall,

"King Ondajon! I'm looking for the great King Ondajon!"

A servant quickly responded, "Sir, I am afraid you are mistaking. There is no king using our restroom facilities, or 'on the john' as you put it."

"No, no, I'm looking for the king named Ondajon."

"Oh. He's out back, having a martini."

Mushroom Cloud Press | Classic Prose Collection

The messenger quickly made his way to the rear porch of the castle. There, he saw the king sipping his cocktail and mumbling about something.

"Sir, I am from glorious King Manyscars's battle fleet. We would like your help in defeating the pesky Trojans," the messenger announced.

"Guinea Pigs," the King said.

"Excuse me?"

"Guinea pigs."

"Yes, yes, guinea pigs. Good King Ondajon, will you accompany me to the fleet?"

"Are there guinea pigs there?"

"Uhh... " the messenger had to think quickly, "...yes. Thousands of guinea pigs. As far as the eye can see."

"Who's eye? Because, if it's a blind man's eye, he can't see any guinea pigs."

"No, no, sir, a young man's keen eye."

"Excellent. I will summon my troops there tomorrow."

Meanwhile, the skilled warrior Acracked was dispatched to find Tendinitis, the very vain warrior. He found him in full dress at a quilting bee.

"Good day, Tendinitis. I am your fellow Greek warrior, Acracked. I am here to bring you with me on a quest."

Tendinitis responded in high, squeaky voice.

"I am on a quest - a quest for the perfect shoes to match this outfit."

"Well sir, we are going to Troy, and I hear they have lovely shoes there."

"Ah, yes! Well, I will have to join you!"

"Excellent! May I ask what you are weaving on your quilt?"

"A decapitation scene. Oh, I do love violence."

"Then you'll fit right in with our group. Let's go." And they went.

***Meanwhile in Olympus***

In the great palace atop Mount Olympus, two great gods, Poseidon and Hermes, were watching the earth. Specifically, they were watching a man whose hat Poseidon kept blowing off his head. Both deities were getting quite a kick out of this when Zeus stormed in, bellowing,

"Enough with that! It's time for some real fun!"

"Oo! oo! what do we get to do, huh, huh?" they squealed in unison.

"We're gonna go watch the humans kill each other!"

"Goody goody gumdrops!" yelled Poseidon.

*** *** ***

So, the Greeks headed out. For the next nine years, both sides slaughtered countless men, the ground was soaked with blood, but nothing very exciting actually happened. Then, early in the tenth year of the war, Tendinitis got into a fight with another of the great chieftains, Aggravation. It seems they were fighting over which was leader in killing statistics. Tendinitis was the first to speak out at a meeting of the Greek council.

"My dear comrades, I am afraid you have made a grave mistake. The kill board says that I am second in people slaughtered with 6091, to Aggravation's 6092. Surely, there has been some error."

Mushroom Cloud Press | Classic Prose Collection

Aggravation quickly replied, "Nonsense! I have killed more men than you, and don't call me Shirley."

"You have beefed up your statistics, my friend. I know for a fact that the last two men you defeated you backed over with your chariot."

"Uhh... yes, that is true, but I'm sure I wouldn't have hit them if the gods had not willed them dead by my hand. Ask the good chieftain Ondajon, he will agree with me."

"What? Why would I ask the person who was on the toilet?"

"No, no, no. The chieftain named Ondajon."

"You should make yourself more clear, Aggravation. Ondajon, have you any say in this matter?"

Now the great ruler of Ithaca rose from his seat, and cleared his throat for what appeared to be a rousing speech. He glanced around the room, and then spoke these words:

"Yes. However, I had quite a traumatic experience today involving a terribly impolite dog named Cerebus and three of my guinea pigs, so I'm not in the mood to talk. Please, carry on."

This threw the meeting into disorder, not because the words had a profound impact, but because no one had any idea what they meant. Aggravation went out back to have a smoke while Tendinitis went to his tent, vowing to stay there in his woman's clothes until he regained his honor.

*** Meanwhile in Olympus ***

"Hey hey hey out there in classic literature land, I'm Zeus, and boy, you look like a great crowd. Any of you out there form Jersey? Really, what exit? Ha Ha! Budda-bing, Budda-boom, eh folks? Let's get on with the show. You know, I had the oddest thing happen to me today - I had to shoot a hydra in my underpants. What he was doing in my underpants, I'll never know. Then this girl comes up to me, and asks, 'how do you gods sleep, with all the bad stuff going on in the world?' You know what I said?"

"What?"

"I said, 'we sleep with our eyes closed!' Get it? With our eyes closed! Budoomboom. Well, kids, that's all for today. See you next time, ladies and germs. Goodnight!"

*** *** ***

A few days after the big fight, Greece was in deep dog doodoo. Troy, led by their great fighter Heckuva, was kicking booty in every battle, even beating the Greeks back to their ships. However, one of the Trojan warriors made a grave mistake. While on a mad killing rampage, he murdered Ondajon's prized guinea pig, brutally beat Tendinitis's best friend, and even short sheeted Aggravation's bed. Now, these three were united again, and together they would bring down Troy.

When dawn approached, sour and smelly fingered, the entire Greek force of over 400,000 men launched an all out assault on Troy. Up on the city walls, Paris watched in dismay as thousands of his friends were slaughtered. He quickly ran to warn his father, King Priam.

"Great King Priam! The great man Ondajon approaches with Tendinitis on his rear and Aggravation by his side. Oh, Heckuva the warrior could not even fell these Mushroom Cloud Press | Classic Prose Collection

determined men," Paris screamed as he entered King Priam's chamber. The king gave Paris an annoyed look and said,

"Paris, what do I care of the man who is on the jon? I certainly do no want to know that he has tendinitis in his rear, and if his side is so aggravated, tell him to take an Aspirin. And why in the world would we need a heck of a warrior to defeat him? Go away."

Paris, looking gloomy, returned to the lookout post, knowing their fate was sealed.

Meanwhile, Tendinitis had met Heckuva outside the walls of Troy. The gods of Olympus were wagering money on the fight, and were trying to help their man. Athena came to the assistance of Tendinitis. Heckuva, unfortunately, had the help of Silenus, who was a drunk, fat, and unimportant god. He knew he was about to get his butt whipped, so Heckuva ran around the city three times, clicked his heels and yelled something about there being no place like home, but this was unsuccessful.

Tendinitis struck first. His spear, however, hit a women who was standing in the middle of the battlefield. She was later identified, and had a very strange name: Edith Hamilton. Anyway, Heckuva took advantage of the situation and attacked with his sword. He could not penetrate Tendinitis's armor, because it was made of Kevlar, a substance made by the blacksmith of Olympus, Dupontus. Tendinitis killed Heckuva, and did a little touchdown dance to celebrate. He even spiked Heckuva's head in the endzone.

The gods were enraged by the great and pretty warrior's boastfulness. They then had their revenge. They filled Paris with courage, who ran out onto the battleground and gave Tendinitis a dead leg. Tendinitis was in so much pain that he limped around until he hopped right off a cliff and fell 500 feet to a watery grave. Simple-minded Paris, having lost his godlike boldness, was chopped into itty-bitty pieces and also heaved off the cliff.

So, the Greeks and Trojans were pretty much even again. The war looked like it was going to last another ten years until one night, while staring at a oak-colored guinea pig, the mentally unstable King Ondajon had a brilliant idea. He shared it with the others at the Assembly:

"My comrades," he began, "Last night, I had what was quite frankly a brilliant idea. It will lead to the fall of Troy and to our glorious victory." At this, the crowd cheered. The king continued,

"Here is my plan. We will construct a giant wooden guinea pig, hollow so that many of the real animals can fit inside. We will then surrender to the Trojans, and offer them the enormous monument as a sacrifice. They will wheel it into the city, and on that night, the guinea pigs will leap out and destroy the entire population with their fiery breath and razor sharp teeth."

The group of men were so joyful when they heard this wonderful contrivance that they ran wildly around the room, screaming and smashing things. One of them yelled "mosh pit!" loudly, and the entire company started slamming into each other to the rocking tunes of the Rolling Stones, who were just getting started then.

Within five days, the contraption was quickly prepared. The day after the Greeks surrendered, everything was ready when dawn appeared, sour and smelly fingered. However, just as the men were wheeling the great wooden guinea pig up to Troy, they realized they had done something wrong. They had forgotten to give the guinea pigs a way of getting out of their vehicle.

Mushroom Cloud Press | Classic Prose Collection

So, the unlucky soldier Gonnadi was elected to ride the enormous mount into the city. When he asked what his excuse should be, the chieftains just said to make up any old story.

It took three days for Gonnadi to convince the Trojans to take in the guinea pig, and he changed his story fifteen times. Finally, he fooled them into thinking he was Zeus by performing several cheesy card tricks which the Trojans had never seen before. That night, when Gonnadi was alone with the giant fabricated creature, he released the guinea pigs. Perhaps the mayhem which ensued is best described by Hickus Maximus, a Trojan warrior:

"Duhhh... Well, them guinea things, they come a runnin' over the hills, burning everything they got their little feet on. They even killed my wife, which made me real sad, cause she was my lil sister too."

When dawn came, sour and smelly fingered, Troy was flattened. The Greeks had won a great victory. To thank the guinea pigs for winning a war which ten years of human toiling could not, they sacrificed them and some wine to the great god Zeus. However, the Greeks made a horrendous mistake. They made the sacrifice with a number 240 white zinfandel, when everyone knows that the god of thunder prefers a number 241 white zinfandel. For this sacrilege, most of the Greeks were killed on their return voyages.

*** Meanwhile in Olympus ***

"Brother Poseidon, what do you have to say in the matter?" Zeus asked

"Lord Zeus, I believe the metric system is far more convenient than the standard one."

Another voice piped up. "I, Hermes, will not rest until the metric system is shown as the offensive garbage it is."

"But Hermes, as king of the gods, I can see that you are better at numbers than we are. After all, you are the god of commerce, aren't you? You're just trying to keep us out of your little ring."

"No, Zeus, I would never do that. Besides, how could I be better at numbers? Were all immortal gods with incredible powers."

"Oh yeah, I always forget that. You know, I think I forgot to mark that down on the last census."

*** *** ***

And so, the greatest war on earth was over. Troy was in ruins, with its citizens sold into slavery, and the Greeks had been killed by the gods. In fact, just about everyone was dead or dying, and Ondajon had retired to Bermuda with about two million guinea pigs. Well, there is one happy thing about this ending - Since everyone is dead, it leaves no room for a Trojan War II.

The End Mushroom Cloud Press | Classic Prose Collection

Make sure to see the movie version of this story, starring Mark Wahlberg as Tendinitis, Travis Scott as Ondajon, and Cardi B as Helen.
```

---

## IC-1944: The Eyes Have It

- Title: The Eyes Have It
- Author (byline): PHILIP K. DICK
- Work: Classic Prose Collection
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1081
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
IT WAS quite by accident I discovered this incredible invasion of Earth by lifeforms from another planet. As yet, I haven’t done anything about it; I can’t think of anything to do. I wrote to the Government, and they sent back a pamphlet on the repair and maintenance of frame houses. Anyhow, the whole thing is known; I’m not the first to discover it. Maybe it’s even under control.

I was sitting in my easy-chair, idly turning the pages of a paperbacked book someone had left on the bus, when I came across the reference that first put me on the trail. For a moment I didn’t respond. It took some time for the full import to sink in. After I’d comprehended, it seemed odd I hadn’t noticed it right away.

The reference was clearly to a nonhuman species of incredible properties, not indigenous to Earth. A species, I hasten to point out, customarily masquerading as ordinary human beings. Their disguise, however, became transparent in the face of the following observations by the author. It was at once obvious the author knew everything. Knew everything — and was taking it in his stride. The line (and I tremble remembering it even now) read: … his eyes slowly roved about the room.

Vague chills assailed me. I tried to picture the eyes. Did they roll like dimes? The passage indicated not; they seemed to move through the air, not over the surface. Rather rapidly, apparently. No one in the story was surprised. That’s what tipped me off. No sign of amazement at such an outrageous thing. Later the matter was amplified. … his eyes moved from person to person.

There it was in a nutshell. The eyes had clearly come apart from the rest of him and were on their own. My heart pounded and my breath choked in my windpipe. I had stumbled on an accidental mention of a totally unfamiliar race. Obviously non-Terrestrial. Yet, to the characters in the book, it was perfectly natural — which suggested they belonged to the same species.

And the author? A slow suspicion burned in my mind. The author was taking it rather too easily in his stride. Evidently, he felt this was quite a usual thing. He made absolutely no attempt to conceal this knowledge. The story continued: … presently his eyes fastened on Julia.

Mushroom Cloud Press | Classic Prose Collection

Julia, being a lady, had at least the breeding to feel indignant. She is described as blushing and knitting her brows angrily. At this, I sighed with relief. They weren’t all non-Terrestrials. The narrative continues: … slowly, calmly, his eyes examined every inch of her.

Great Scott! But here the girl turned and stomped off and the matter ended. I lay back in my chair gasping with horror. My wife and family regarded me in wonder.

“What’s wrong, dear?” my wife asked.

I couldn’t tell her. Knowledge like this was too much for the ordinary run-of-the-mill person. I had to keep it to myself. “Nothing,” I gasped. I leaped up, snatched the book, and hurried out of the room.

IN THE garage, I continued reading. There was more. Trembling, I read the next revealing passage: … he put his arm around Julia. Presently she asked him if he would remove his arm. He immediately did so, with a smile.

It’s not said what was done with the arm after the fellow had removed it. Maybe it was left standing upright in the corner. Maybe it was thrown away. I don’t care. In any case, the full meaning was there, staring me right in the face.

Here was a race of creatures capable of removing portions of their anatomy at will. Eyes, arms — and maybe more. Without batting an eyelash. My knowledge of biology came in handy, at this point. Obviously they were simple beings, uni-cellular, some sort of primitive single-celled things. Beings no more developed than starfish. Starfish can do the same thing, you know.

I read on. And came to this incredible revelation, tossed off coolly by the author without the faintest tremor: … outside the movie theater we split up. Part of us went inside, part over to the cafe for dinner.

Binary fission, obviously. Splitting in half and forming two entities. Probably each lower half went to the cafe, it being farther, and the upper halves to the movies. I read on, hands shaking. I had really stumbled onto something here. My mind reeled as I made out this passage: … I’m afraid there’s no doubt about it. Poor Bibney has lost his head again.

Which was followed by: … and Bob says he has utterly no guts.

Mushroom Cloud Press | Classic Prose Collection

Yet Bibney got around as well as the next person. The next person, however, was just as strange. He was soon described as: … totally lacking in brains.

THERE was no doubt of the thing in the next passage. Julia, whom I had thought to be the one normal person, reveals herself as also being an alien life form, similar to the rest: … quite deliberately, Julia had given her heart to the young man.

It didn’t relate what the final disposition of the organ was, but I didn’t really care. It was evident Julia had gone right on living in her usual manner, like all the others in the book. Without heart, arms, eyes, brains, viscera, dividing up in two when the occasion demanded. Without a qualm. … thereupon she gave him her hand.

I sickened. The rascal now had her hand, as well as her heart. I shudder to think what he’s done with them, by this time. … he took her arm.

Not content to wait, he had to start dismantling her on his own. Flushing crimson, I slammed the book shut and leaped to my feet. But not in time to escape one last reference to those carefree bits of anatomy whose travels had originally thrown me on the track: … her eyes followed him all the way down the road and across the meadow.

I rushed from the garage and back inside the warm house, as if the accursed things were following me. My wife and children were playing Monopoly in the kitchen. I joined them and played with frantic fervor, brow feverish, teeth chattering.

I had had enough of the thing. I want to hear no more about it. Let them come on. Let them invade Earth. I don’t want to get mixed up in it.

I have absolutely no stomach for it.
```

---

## IC-1945: The Girl at the Gate

- Title: The Girl at the Gate
- Author (byline): Lucy Maud Montgomery
- Work: Classic Prose Collection
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1527
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
Something very strange happened the night old Mr. Lawrence died. I have never been able to explain it and I have never spoken of it except to one person and she said that I dreamed it. I did not dream it ... I saw and heard, waking.

We had not expected Mr. Lawrence to die then. He did not seem very ill ... not nearly so ill as he had been during his previous attack. When we heard of his illness I went over to Woodlands to see him, for I had always been a great favourite with him. The big house was quiet, the servants going about their work as usual, without any appearance of excitement. I was told that I could not see Mr. Lawrence for a little while, as the doctor was with him. Mrs. Yeats, the housekeeper, said the attack was not serious and asked me to wait in the blue parlour, but I preferred to sit down on the steps of the big, arched front door. It was an evening in June. Woodlands was very lovely; to my right was the garden, and before me was a little valley abrim with the sunset. In places under the big trees it was quite dark even then.

There was something unusually still in the evening ... a stillness as of waiting. It set me thinking of the last time Mr. Lawrence had been ill ... nearly a year ago in August. One night during his convalescence I had watched by him to relieve the nurse. He had been sleepless and talkative, telling me many things about his life. Finally he told me of Margaret.

I knew a little about her ... that she had been his sweetheart and had died very young. Mr. Lawrence had remained true to her memory ever since, but I had never heard him speak of her before.

"She was very beautiful," he said dreamily, "and she was only eighteen when she died, Jeanette. She had wonderful pale-golden hair and dark-brown eyes. I have a little ivory miniature of her. When I die it is to be given to you, Jeanette. I have waited a long while for her. You know she promised she would come."

I did not understand his meaning and kept silence, thinking that he might be wandering a little in his mind.

Mushroom Cloud Press | Classic Prose Collection

"She promised she would come and she will keep her word," he went on. "I was with her when she died. I held her in my arms. She said to me, 'Herbert, I promise that I will be true to you forever, through as many years of lonely heaven as I must know before you come. And when your time is at hand I will come to make your deathbed easy as you have made mine. I will come, Herbert.' She solemnly promised, Jeanette. We made a death-tryst of it. And I know she will come."

He had fallen asleep then and after his recovery he had not alluded to the matter again. I had forgotten it, but I recalled it now as I sat on the steps among the geraniums that June evening. I liked to think of Margaret ... the lovely girl who had died so long ago, taking her lover's heart with her to the grave. She had been a sister of my grandfather, and people told me that I resembled her slightly. Perhaps that was why old Mr. Lawrence had always made such a pet of me.

Presently the doctor came out and nodded to me cheerily. I asked him how Mr. Lawrence was.

"Better ... better," he said briskly. "He will be all right tomorrow. The attack was very slight. Yes, of course you may go in. Don't stay longer than half an hour."

Mrs. Stewart, Mr. Lawrence's sister, was in the sickroom when I went in. She took advantage of my presence to lie down on the sofa a little while, for she had been up all the preceding night. Mr. Lawrence turned his fine old silver head on the pillow and smiled a greeting. He was a very handsome old man; neither age nor illness had marred his finely modelled face or impaired the flash of his keen, steel-blue eyes. He seemed quite well and talked naturally and easily of many commonplace things.

At the end of the doctor's half-hour I rose to go. Mrs. Stewart had fallen asleep and he would not let me wake her, saying he needed nothing and felt like sleeping himself. I promised to come up again on the morrow and went out.

It was dark in the hall, where no lamp had been lighted, but outside on the lawn the moonlight was bright as day. It was the clearest, whitest night I ever saw. I turned aside into the garden, meaning to cross it, and take the short way over the west meadow home. There was a long walk of rose bushes leading across the garden to a little gate on the further side ... the way Mr. Lawrence had been wont to take long ago when he went over the fields to woo Margaret. I went along it, enjoying the night. The bushes were white with roses, and the ground under my feet was all snowed over with their petals. The air was still and breezeless; again I felt that Mushroom Cloud Press | Classic Prose Collection

sensation of waiting ... of expectancy. As I came up to the little gate I saw a young girl standing on the other side of it. She stood in the full moonlight and I saw her distinctly.

She was tall and slight and her head was bare. I saw that her hair was a pale gold, shining somewhat strangely about her head as if catching the moonbeams. Her face was very lovely and her eyes large and dark. She was dressed in something white and softly shimmering, and in her hand she held a white rose ... a very large and perfect one. Even at the time I found myself wondering where she could have picked it. It was not a Woodlands rose. All the Woodlands roses were smaller and less double.

She was a stranger to me, yet I felt that I had seen her or someone very like her before. Possibly she was one of Mr. Lawrence's many nieces who might have come up to Woodlands upon hearing of his illness.

As I opened the gate I felt an odd chill of positive fear. Then she smiled as if I had spoken my thought.

"Do not be frightened," she said. "There is no reason you should be frightened. I have only come to keep a tryst."

The words reminded me of something, but I could not recall what it was. The strange fear that was on me deepened. I could not speak.

She came through the gateway and stood for a moment at my side.

"It is strange that you should have seen me," she said, "but now behold how strong and beautiful a thing is faithful love—strong enough to conquer death. We who have loved truly love always—and this makes our heaven."

She walked on after she had spoken, down the long rose path. I watched her until she reached the house and went up the steps. In truth I thought the girl was someone not quite in her right mind. When I reached home I did not speak of the matter to anyone, not even to inquire who the girl might possibly be. There seemed to be something in that strange meeting that demanded my silence.

The next morning word came that old Mr. Lawrence was dead. When I hurried down to Woodlands I found all in confusion, but Mrs. Yeats took me into the blue parlour and told me what little there was to tell.

Mushroom Cloud Press | Classic Prose Collection

"He must have died soon after you left him, Miss Jeanette," she sobbed, "for Mrs. Stewart wakened at ten o'clock and he was gone. He lay there, smiling, with such a strange look on his face as if he had just seen something that made him wonderfully happy. I never saw such a look on a dead face before."

"Who is here besides Mrs. Stewart?" I asked.

"Nobody," said Mrs. Yeats. "We have sent word to all his friends but they have not had time to arrive here yet."

"I met a young girl in the garden last night," I said slowly. "She came into the house. I did not know her but I thought she must be a relative of Mr. Lawrence's."

Mrs. Yeats shook her head.

"No. It must have been somebody from the village, although I didn't know of anyone calling after you went away."

I said nothing more to her about it.

After the funeral Mrs. Stewart gave me Margaret's miniature. I had never seen it or any picture of Margaret before. The face was very lovely—also strangely like my own, although I am not beautiful. It was the face of the young girl I had met at the gate!
```

---

## IC-1946: The Inconsiderate Waiter

- Title: The Inconsiderate Waiter
- Author (byline): J.M. Barrie
- Work: Classic Prose Collection
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 7088
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
Frequently I have to ask myself in the street for the name of the man I bowed to just now, and then, before I can answer, the wind of the first corner blows him from my memory. I have a theory, however, that those puzzling faces, which pass before I can see who cut the coat, all belong to club waiters.

Until William forced his affairs upon me that was all I did know of the private life of waiters, though I have been in the club for twenty years. I was even unaware whether they slept downstairs or had their own homes; nor had I the interest to inquire of other members, nor they the knowledge to inform me. I hold that this sort of people should be fed and clothed and given airing and wives and children, and I subscribe yearly, I believe for these purposes; but to come into closer relation with waiters is bad form; they are club fittings, and William should have kept his distress to himself, or taken it away and patched it up like a rent in one of the chairs. His inconsiderateness has been a pair of spectacles to me for months.

It is not correct taste to know the name of a club waiter, so I must apologise for knowing William's, and still more for not forgetting it. If, again, to speak of a waiter is bad form, to speak bitterly is the comic degree of it. But William has disappointed me sorely. There were years when I would defer dining several minutes that he might wait on me. His pains to reserve the window-seat for me were perfectly satisfactory. I allowed him privileges, as to suggest dishes, and would give him information, as that some one had startled me in the reading-room by slamming a door. I have shown him how I cut my finger with a piece of string. Obviously he was gratified by these attentions, usually recommending a liqueur; and I fancy he must have understood my sufferings, for he often looked ill himself. Probably he was rheumatic, but I cannot say for certain, as I never thought of asking, and he had the sense to see that the knowledge would be offensive to me.

In the smoking-room we have a waiter so independent that once, when he brought me a yellow chartreuse, and I said I had ordered green, he replied, "No, sir; you said yellow." William could never have been guilty of such effrontery. In appearance, of course, he is mean, but I can no more describe him than a milkmaid could draw cows. I suppose we distinguish one waiter from another much as we pick our hat from the rack. We could have plotted a murder safely before William. He never presumed to have any opinions of his own. When such was my mood he Mushroom Cloud Press | Classic Prose Collection

remained silent, and if I announced that something diverting had happened to me he laughed before I told him what it was. He turned the twinkle in his eye off or on at my bidding as readily as if it was the gas. To my "Sure to be wet to-morrow," he would reply, "Yes, sir;" and to Trelawney's "It doesn't look like rain," two minutes afterward, he would reply, "No, sir." It was one member who said Lightning Rod would win the Derby and another who said Lightning Rod had no chance, but it was William who agreed with both. He was like a cheroot, which may be smoked from either end. So used was I to him that, had he died or got another situation (or whatever it is such persons do when they disappear from the club), I should probably have told the head waiter to bring him back, as I disliked changes.

It would not become me to know precisely when I began to think William an ingrate, but I date his lapse from the evening when he brought me oysters. I detest oysters, and no one knew it better than William. He has agreed with me that he could not understand any gentleman's liking them. Between me and a certain member who smacks his lips twelve times to a dozen of them William knew I liked a screen to be placed until we had reached the soup, and yet he gave me the oysters and the other man my sardine. Both the other member and I quickly called for brandy and the head waiter. To do William justice, he shook, but never can I forget his audacious explanation: "Beg pardon, sir, but I was thinking of something else."

In these words William had flung off the mask, and now I knew him for what he was.

I must not be accused of bad form for looking at William on the following evening. What prompted me to do so was not personal interest in him, but a desire to see whether I dare let him wait on me again. So, recalling that a caster was off a chair yesterday, one is entitled to make sure that it is on to-day before sitting down. If the expression is not too strong, I may say that I was taken aback by William's manner. Even when crossing the room to take my orders he let his one hand play nervously with the other. I had to repeat "Sardine on toast" twice, and instead of answering "Yes, sir," as if my selection of sardine on toast was a personal gratification to him, which is the manner one expects of a waiter, he glanced at the clock, then out at the window, and, starting, asked, "Did you say sardine on toast, sir?"

It was the height of summer, when London smells like a chemist's shop, and he who has the dinner-table at the window needs no candles to show him his knife and fork. I lay back at intervals, now watching a starved-looking woman sleep on a door-step, and again complaining of the club bananas. By-and-by I saw a girl of the commonest kind, ill-clad and dirty, as all these Arabs are. Their parents should be compelled to feed and clothe them comfortably, or at least to keep them indoors, where they cannot offend our eyes. Such children are for pushing aside with one's umbrella; but this girl I noticed because she was gazing at the club Mushroom Cloud Press | Classic Prose Collection

windows. She had stood thus for perhaps ten minutes when I became aware that some one was leaning over me to look out at the window. I turned round. Conceive my indignation on seeing that the rude person was William.

"How dare you, William?" I said, sternly. He seemed not to hear me. Let me tell, in the measured words of one describing a past incident, what then took place. To get nearer the window he pressed heavily on my shoulder.

"William, you forget yourself!" I said, meaning—as I see now—that he had forgotten me.

I heard him gulp, but not to my reprimand. He was scanning the street. His hands chattered on my shoulder, and, pushing him from me, I saw that his mouth was agape.

"What are you looking for?" I asked.

He stared at me, and then, like one who had at last heard the echo of my question, seemed to be brought back to the club. He turned his face from me for an instant, and answered shakily:

"I beg your pardon, sir! I—I shouldn't have done it. Are the bananas too ripe, sir?"

He recommended the nuts, and awaited my verdict so anxiously while I ate one that I was about to speak graciously, when I again saw his eyes drag him to the window.

"William," I said, my patience giving way at last, "I dislike being waited on by a melancholy waiter."

"Yes, sir," he replied, trying to smile, and then broke out passionately, "For God's sake, sir, tell me, have you seen a little girl looking in at the club windows?"

He had been a good waiter once, and his distracted visage was spoiling my dinner.

"There," I said, pointing to the girl, and no doubt would have added that he must bring me coffee immediately, had he continued to listen. But already he was beckoning to the child. I have not the least interest in her (indeed, it had never struck me that waiters had private affairs, and I still think it a pity that they should have); but as I happened to be looking out at the window I could not avoid seeing what occurred. As soon as the girl saw William she ran into the street, regardless of vehicles, and nodded three times to him. Then she disappeared.

I have said that she was quite a common child, without attraction of any sort, and yet it was amazing the difference she made in William. He gasped relief, like one who had broken through the anxiety that checks breathing, and into his face there came a silly laugh of happiness. I had dined well, on the whole, so I said:

"I am glad to see you cheerful again, William."

I meant that I approved his cheerfulness because it helped my digestion, but he must needs think I was sympathising with him.

Mushroom Cloud Press | Classic Prose Collection

"Thank you, sir," he answered. "Oh, sir! when she nodded and I saw it was all right I could have gone down on my knees to God."

I was as much horrified as if he had dropped a plate on my toes. Even William, disgracefully emotional as he was at the moment, flung out his arms to recall the shameful words.

"Coffee, William!" I said, sharply.

I sipped my coffee indignantly, for it was plain to me that William had something on his mind.

"You are not vexed with me, sir?" he had the hardihood to whisper.

"It was a liberty," I said.

"I know, sir; but I was beside myself."

"That was a liberty also."

He hesitated, and then blurted out:

"It is my wife, sir. She—"

I stopped him with my hand. William, whom I had favoured in so many ways, was a married man! I might have guessed as much years before had I ever reflected about waiters, for I knew vaguely that his class did this sort of thing. His confession was distasteful to me, and I said warningly:

"Remember where you are, William."

"Yes, sir; but you see, she is so delicate—"

"Delicate! I forbid your speaking to me on unpleasant topics."

"Yes, sir; begging your pardon."

It was characteristic of William to beg my pardon and withdraw his wife, like some unsuccessful dish, as if its taste would not remain in the mouth. I shall be chided for questioning him further about his wife, but, though doubtless an unusual step, it was only bad form superficially, for my motive was irreproachable. I inquired for his wife, not because I was interested in her welfare, but in the hope of allaying my irritation. So I am entitled to invite the wayfarer who has bespattered me with mud to scrape it off.

I desired to be told by William that the girl's signals meant his wife's recovery to health. He should have seen that such was my wish and answered accordingly. But, with the brutal inconsiderateness of his class, he said:

"She has had a good day; but the doctor, he—the doctor is afeard she is dying."

Already I repented my questions. William and his wife seemed in league against me, when they might so easily have chosen some other member.

"Pooh! the doctor," I said.

"Yes, sir," he answered.

"Have you been married long, William?"

"Eight years, sir. Eight years ago she was—I—I mind her when . . . and now the doctor says—"

Mushroom Cloud Press | Classic Prose Collection

The fellow gaped at me. "More coffee, sir?" he asked.

"What is her ailment?"

"She was always one of the delicate kind, but full of spirit, and—and you see, she has had a baby lately—"

"William!"

"And she—I—the doctor is afeard she's not picking up."

"I feel sure she will pick up."

"Yes, sir?"

It must have been the wine I had drunk that made me tell him:

"I was once married, William. My wife—it was just such a case as yours."

"She did not get better sir?"

"No."

After a pause he said, "Thank you, sir," meaning for the sympathy that made me tell him that. But it must have been the wine.

"That little girl comes here with a message from your wife?"

"Yes; if she nods three times it means my wife is a little better."

"She nodded thrice to-day."

"But she is told to do that to relieve me, and maybe those nods don't tell the truth."

"Is she your girl?"

"No; we have none but the baby. She is a neighbour's; she comes twice a day."

"It is heartless of her parents not to send her every hour."

"But she is six years old," he said, "and has a house and two sisters to look after in the daytime, and a dinner to cook. Gentlefolk don't understand."

"I suppose you live in some low part, William."

"Off Drury Lane," he answered, flushing; "but—but it isn't low. You see, we were never used to anything better, and I mind when I let her see the house before we were married, she—she a sort of cried because she was so proud of it. That was eight years ago, and now—she's afeard she'll die when I'm away at my work."

"Did she tell you that?"

"Never; she always says she is feeling a little stronger."

"Then how can you know she is afraid of that?"

"I don't know how I know, sir; but when I am leaving the house in the morning I look at her from the door, and she looks at me, and then I—I know."

"A green chartreuse, William!"

I tried to forget William's vulgar story in billiards, but he had spoiled my game. My opponent, to whom I can give twenty, ran out when I was sixty-seven, and I put aside my cue pettishly. That in itself was bad form, but what would they have thought had they known that a waiter's impertinence caused it! I grew angrier with Mushroom Cloud Press | Classic Prose Collection

William as the night wore on, and next day I punished him by giving my orders through another waiter.

As I had my window-seat, I could not but see that the girl was late again. Somehow I dawdled over my coffee. I had an evening paper before me, but there was so little in it that my eyes found more of interest in the street. It did not matter to me whether William's wife died, but when that girl had promised to come, why did she not come? These lower classes only give their word to break it. The coffee was undrinkable.

At last I saw her. William was at another window, pretending to do something with the curtains. I stood up, pressing closer to the window. The coffee had been so bad that I felt shaky. She nodded three times, and smiled.

"She is a little better," William whispered to me, almost gaily.

"Whom are you speaking of?" I asked, coldly, and immediately retired to the billiard-room, where I played a capital game. The coffee was much better there than in the dining-room.

Several days passed, and I took care to show William that I had forgotten his maunderings. I chanced to see the little girl (though I never looked for her) every evening, and she always nodded three times, save once, when she shook her head, and then William's face grew white as a napkin. I remember this incident because that night I could not get into a pocket. So badly did I play that the thought of it kept me awake in bed, and that, again, made me wonder how William's wife was. Next day I went to the club early (which was not my custom) to see the new books. Being in the club at any rate, I looked into the dining-room to ask William if I had left my gloves there, and the sight of him reminded me of his wife; so I asked for her. He shook his head mournfully, and I went off in a rage.

So accustomed am I to the club that when I dine elsewhere I feel uncomfortable next morning, as if I had missed a dinner. William knew this; yet here he was, hounding me out of the club! That evening I dined (as the saying is) at a restaurant, where no sauce was served with the asparagus. Furthermore, as if that were not triumph enough for William, his doleful face came between me and every dish, and I seemed to see his wife dying to annoy me.

I dined next day at the club for self-preservation, taking, however, a table in the middle of the room, and engaging a waiter who had once nearly poisoned me by not interfering when I put two lumps of sugar into my coffee instead of one, which is my allowance. But no William came to me to acknowledge his humiliation, and by-and-by I became aware that he was not in the room. Suddenly the thought struck me that his wife must be dead, and I—It was the worst cooked and the worst served dinner I ever had in the club.

I tried the smoking-room. Usually the talk there is entertaining, but on that occasion it was so frivolous that I did not remain five minutes. In the card-room a Mushroom Cloud Press | Classic Prose Collection

member told me excitedly that a policeman had spoken rudely to him; and my strange comment was:

"After all, it is a small matter."

In the library, where I had not been for years, I found two members asleep, and, to my surprise, William on a ladder dusting books.

"You have not heard, sir?" he said, in answer to my raised eyebrows. Descending the ladder, he whispered tragically: "It was last evening, sir. I—I lost my head, and I—swore at a member."

I stepped back from William, and glanced apprehensively at the two members. They still slept.

"I hardly knew," William went on, "what I was doing all day yesterday, for I had left my wife so weakly that—"

I stamped my foot.

"I beg your pardon for speaking of her," he had the grace to say, "but I couldn't help slipping up to the window often yesterday to look for Jenny, and when she did come, and I saw she was crying, it—it sort of confused me, and I didn't know right, sir, what I was doing. I hit against a member, Mr. Myddleton Finch, and he—he jumped and swore at me. Well, sir, I had just touched him after all, and I was so miserable, it a kind of stung me to be treated like—like that, and me a man as well as him; and I lost my senses, and—and I swore back."

William's shamed head sank on his chest, but I even let pass his insolence in likening himself to a member of the club, so afraid was I of the sleepers waking and detecting me in talk with a waiter.

"For the love of God," William cried, with coarse emotion, "don't let them dismiss me!"

"Speak lower!" I said. "Who sent you here?"

"I was turned out of the dining-room at once, and told to attend to the library until they had decided what to do with me. Oh, sir, I'll lose my place!"

He was blubbering, as if a change of waiters, was a matter of importance.

"This is very bad, William," I said. "I fear I can do nothing for you."

"Have mercy on a distracted man!" he entreated. "I'll go on my knees to Mr. Myddleton Finch."

How could I but despise a fellow who would be thus abject for a pound a week?

"I dare not tell her," he continued, "that I have lost my place. She would just fall back and die."

"I forbade your speaking of your wife," I said, sharply, "unless you can speak pleasantly of her."

"But she may be worse now, sir, and I cannot even see Jenny from here. The library windows look to the back."

Mushroom Cloud Press | Classic Prose Collection

"If she dies," I said, "it will be a warning to you to marry a stronger woman next time."

Now every one knows that there is little real affection among the lower orders. As soon as they have lost one mate they take another. Yet William, forgetting our relative positions, drew himself up and raised his fist, and if I had not stepped back I swear he would have struck me.

The highly improper words William used I will omit, out of consideration for him. Even while he was apologising for them I retired to the smoking-room, where I found the cigarettes so badly rolled that they would not keep alight. After a little I remembered that I wanted to see Myddleton Finch about an improved saddle of which a friend of his has the patent. He was in the newsroom, and, having questioned him about the saddle, I said:

"By the way, what is this story about your swearing at one of the waiters?"

"You mean about his swearing at me," Myddleton Finch replied, reddening.

"I am glad that was it," I said; "for I could not believe you guilty of such bad form."

"If I did swear—" he was beginning, but I went on:

"The version which has reached me was that you swore at him, and he repeated the word. I heard he was to be dismissed and you reprimanded."

"Who told you that?" asked Myddleton Finch, who is a timid man.

"I forget; it is club talk," I replied, lightly. "But of course the committee will take your word. The waiter, whichever one he is, richly deserves his dismissal for insulting you without provocation."

Then our talk returned to the saddle, but Myddleton Finch was abstracted, and presently he said:

"Do you know, I fancy I was wrong in thinking that the waiter swore at me, and I'll withdraw my charge to-morrow."

Myddleton Finch then left me, and, sitting alone, I realised that I had been doing William a service. To some slight extent I may have intentionally helped him to retain his place in the club, and I now see the reason, which was that he alone knows precisely to what extent I like my claret heated.

For a mere second I remembered William's remark that he should not be able to see the girl Jenny from the library windows. Then this recollection drove from my head that I had only dined in the sense that my dinner-bill was paid. Returning to the dining-room, I happened to take my chair at the window, and while I was eating a deviled kidney I saw in the street the girl whose nods had such an absurd effect on William.

The children of the poor are as thoughtless as their parents, and this Jenny did not sign to the windows in the hope that William might see her, though she could not see him. Her face, which was disgracefully dirty, bore doubt and dismay on it, Mushroom Cloud Press | Classic Prose Collection

but whether she brought good news it would not tell. Somehow I had expected her to signal when she saw me, and, though her message could not interest me, I was in the mood in which one is irritated at that not taking place which he is awaiting. Ultimately she seemed to be making up her mind to go away.

A boy was passing with the evening papers, and I hurried out to get one, rather thoughtlessly, for we have all the papers in the club. Unfortunately, I misunderstood the direction the boy had taken; but round the first corner (out of sight of the club windows) I saw the girl Jenny, and so asked her how William's wife was.

"Did he send you to me?" she replied, impertinently taking me for a waiter. "My!" she added, after a second scrutiny, "I b'lieve you're one of them. His missis is a bit better, and I was to tell him as she took all the tapiocar."

"How could you tell him?" I asked.

"I was to do like this," she replied, and went through the supping of something out of a plate in dumb-show.

"That would not show she ate all the tapioca," I said.

"But I was to end like this," she answered, licking an imaginary plate with her tongue.

I gave her a shilling (to get rid of her), and returned to the club disgusted.

Later in the evening I had to go to the club library for a book, and while William was looking in vain for it (I had forgotten the title) I said to him:

"By the way, William, Mr. Myddleton Finch is to tell the committee that he was mistaken in the charge he brought against you, so you will doubtless be restored to the dining-room to-morrow."

The two members were still in their chairs, probably sleeping lightly; yet he had the effrontery to thank me.

"Don't thank me," I said, blushing at the imputation. "Remember your place, William!"

"But Mr. Myddleton Finch knew I swore," he insisted.

"A gentleman," I replied, stiffly, "cannot remember for twenty-four hours what a waiter has said to him."

"No, sir; but—"

To stop him I had to say: "And, ah, William, your wife is a little better. She has eaten the tapioca—all of it."

"How can your know, sir?"

"By an accident."

"Jenny signed to the window?"

"No."

"Then you saw her, and went out, and—"

"Nonsense!"

Mushroom Cloud Press | Classic Prose Collection

"Oh, sir, to do that for me! May God bl—"

"William!"

"Forgive me, sir; but—when I tell my missis, she will say it was thought of your own wife as made you do it."

He wrung my hand. I dared not withdraw it, lest we should waken the sleepers.

William returned to the dining-room, and I had to show him that if he did not cease looking gratefully at me I must change my waiter. I also ordered him to stop telling me nightly how his wife was, but I continued to know, as I could not help seeing the girl Jenny from the window. Twice in a week I learned from this objectionable child that the ailing woman had again eaten all the tapioca. Then I became suspicious of William. I will tell why.

It began with a remark of Captain Upjohn's. We had been speaking of the inconvenience of not being able to get a hot dish served after 1 A.M., and he said:

"It is because these lazy waiters would strike. If the beggars had a love of their work they would not rush away from the club the moment one o'clock strikes. That glum fellow who often waits on you takes to his heels the moment he is clear of the club steps. He ran into me the other night at the top of the street, and was off without apologising."

"You mean the foot of the street, Upjohn," I said; for such is the way to Drury Lane.

"No; I mean the top. The man was running west."

"East."

"West."

I smiled, which so annoyed him that he bet me two to one in sovereigns. The bet could have been decided most quickly by asking William a question, but I thought, foolishly doubtless, that it might hurt his feelings, so I watched him leave the club. The possibility of Upjohn's winning the bet had seemed remote to me. Conceive my surprise, therefore when William went westward.

Amazed, I pursued him along two streets without realising that I was doing so. Then curiosity put me into a hansom. We followed William, and it proved to be a three-shilling fare, for, running when he was in breath and walking when he was out of it, he took me to West Kensington.

I discharged my cab, and from across the street watched William's incomprehensible behaviour. He had stopped at a dingy row of workmen's houses, and knocked at the darkened window of one of them. Presently a light showed. So far as I could see, some one pulled up the blind and for ten minutes talked to William. I was uncertain whether they talked, for the window was not opened, and I felt that, had William spoken through the glass loud enough to be heard inside, I must have heard him too. Yet he nodded and beckoned. I was still bewildered Mushroom Cloud Press | Classic Prose Collection

when, by setting off the way he had come, he gave me the opportunity of going home.

Knowing from the talk of the club what the lower orders are, could I doubt that this was some discreditable love-affair of William's? His solicitude for his wife had been mere pretence; so far as it was genuine, it meant that he feared she might recover. He probably told her that he was detained nightly in the club till three.

I was miserable next day, and blamed the deviled kidneys for it. Whether William was unfaithful to his wife was nothing to me, but I had two plain reasons for insisting on his going straight home from his club: the one that, as he had made me lose a bet, I must punish him; the other that he could wait upon me better if he went to bed betimes.

Yet I did not question him. There was something in his face that—Well, I seemed to see his dying wife in it.

I was so out of sorts that I could eat no dinner. I left the club. Happening to stand for some time at the foot of the street, I chanced to see the girl Jenny coming, and—No; let me tell the truth, though the whole club reads: I was waiting for her.

"How is William's wife to-day?" I asked.

"She told me to nod three times," the little slattern replied; "but she looked like nothink but a dead one till she got the brandy.”

"Hush, child!" I said, shocked. "You don't know how the dead look."

"Bless yer," she answered, "don't I just! Why, I've helped to lay 'em out. I'm going on seven."

"Is William good to his wife?"

"Course he is. Ain't she his missis?"

"Why should that make him good to her?" I asked, cynically, out of my knowledge of the poor. But the girl, precocious in many ways, had never had any opportunities of studying the lower classes in the newspapers, fiction, and club talk. She shut one eye, and, looking up wonderingly, said:

"Ain't you green—just!"

"When does William reach home at night?"

"'Tain't night; it's morning. When I wakes up at half dark and half light, and hears a door shutting, I know as it's either father going off to his work or Mr. Hicking come home from his."

"Who is Mr. Hicking?"

"Him as we've been speaking on—William. We calls him mister, 'cause he's a toff. Father's just doing jobs in Covent Gardens, but Mr. Hicking, he's a waiter, and a clean shirt every day. The old woman would like father to be a waiter, but he hain't got the 'ristocratic look."

"What old woman?"

Mushroom Cloud Press | Classic Prose Collection

"Go 'long! that's my mother. Is it true there's a waiter in the club just for to open the door?"

"Yes; but—"

"And another just for to lick the stamps? My!"

"William leaves the club at one o'clock?" I said, interrogatively.

She nodded. "My mother," she said, "is one to talk, and she says Mr. Hicking as he should get away at twelve, 'cause his missis needs him more'n the gentlemen need him. The old woman do talk."

"And what does William answer to that?"

"He says as the gentlemen can't be kept waiting for their cheese."

"But William does not go straight home when he leaves the club?"

"That's the kid."

"Kid!" I echoed, scarcely understanding, for, knowing how little the poor love their children, I had asked William no questions about the baby.

"Didn't you know his missis had a kid?"

"Yes; but that is no excuse for William's staying away from his sick wife," I answered, sharply. A baby in such a home as William's, I reflected, must be trying; but still—Besides, his class can sleep through any din.

"The kid ain't in our court," the girl explained. "He's in W., he is, and I've never been out of W.C.; leastwise, not as I knows on."

"This is W. I suppose you mean that the child is at West Kensington? Well, no doubt it was better for William's wife to get rid of the child—"

"Better!" interposed the girl. "'Tain't better for her not to have the kid. Ain't her not having him what she's always thinking on when she looks like a dead one?"

"How could you know that?"

"Cause," answered the girl, illustrating her words with a gesture, "I watches her, and I sees her arms going this way, just like as she wanted to hug her kid."

"Possibly you are right," I said, frowning; "but William had put the child out to nurse because it disturbed his night's rest. A man who has his work to do—"

"You are green!"

"Then why have the mother and child been separated?"

"Along of that there measles. Near all the young 'uns in our court has 'em bad."

"Have you had them?"

"I said the young 'uns."

"And William sent the baby to West Kensington to escape infection?"

"Took him, he did."

"Against his wife's wishes?"

"Na-o!"

"You said she was dying for want of the child?"

"Wouldn't she rayther die than have the kid die?"

Mushroom Cloud Press | Classic Prose Collection

"Don't speak so heartlessly, child. Why does William not go straight home from the club? Does he go to West Kensington to see it?"

"'Tain't a hit, it's an 'e. Course he do."

"Then he should not. His wife has the first claim on him."

"Ain't you green! It's his missis as wants him to go. Do you think she could sleep till she knowed how the kid was?"

"But he does not go into the house at West Kensington?"

"Is he soft? Course he don't go in, fear of taking the infection to the kid. They just holds the kid up at the window to him, so as he can have a good look. Then he comes home and tells his missis. He sits foot of the bed and tells."

"And that takes place every night? He can't have much to tell."

"He has just."

"He can only say whether the child is well or ill."

"My! He tells what a difference there is in the kid since he seed him last."

"There can be no difference!"

"Go 'long! Ain't a kid always growing? Haven't Mr. Hicking to tell how the hair is getting darker, and heaps of things beside?"

"Such as what?"

"Like whether he larfed, and if he has her nose, and how as he knowed him. He tells her them things more 'n once."

"And all this time he is sitting at the foot of the bed?"

"'Cept when he holds her hand."

"But when does he get to bed himself?"

"He don't get much. He tells her as he has a sleep at the club."

"He cannot say that."

"Hain't I heard him? But he do go to his bed a bit, and then they both lies quiet, her pretending she is sleeping so as he can sleep, and him 'feard to sleep case he shouldn't wake up to give her the bottle stuff."

"What does the doctor say about her?"

"He's a good one, the doctor. Sometimes he says she would get better if she could see the kid through the window."

"Nonsense!"

"And if she was took to the country."

"Then why does not William take her?"

"My! you are green! And if she drank port wines."

"Doesn't she?"

"No; but William, he tells her about the gentlemen drinking them."

On the tenth day after my conversation with this unattractive child I was in my brougham, with the windows up, and I sat back, a paper before my face lest any one should look in. Naturally, I was afraid of being seen in company of William's Mushroom Cloud Press | Classic Prose Collection

wife and Jenny, for men about town are uncharitable, and, despite the explanation I had ready, might have charged me with pitying William. As a matter of fact, William was sending his wife into Surrey to stay with an old nurse of mine, and I was driving her down because my horses needed an outing. Besides, I was going that way at any rate.

I had arranged that the girl Jenny, who was wearing an outrageous bonnet, should accompany us, because, knowing the greed of her class, I feared she might blackmail me at the club.

William joined us in the suburbs, bringing the baby with him, as I had foreseen they would all be occupied with it, and to save me the trouble of conversing with them. Mrs. Hicking I found too pale and fragile for a workingman's wife, and I formed a mean opinion of her intelligence from her pride in the baby, which was a very ordinary one. She created quite a vulgar scene when it was brought to her, though she had given me her word not to do so, what irritated me even more than her tears being her ill-bred apology that she "had been 'feared baby wouldn't know her again." I would have told her they didn't know any one for years had I not been afraid of the girl Jenny, who dandled the infant on her knees and talked to it as if it understood. She kept me on tenter-hooks by asking it offensive questions, such as, "'Oo know who give me that bonnet?" and answering them herself, "It was the pretty gentleman there;" and several times I had to affect sleep because she announced, "Kiddy wants to kiss the pretty gentleman."

Irksome as all this necessarily was to a man of taste, I suffered even more when we reached our destination. As we drove through the village the girl Jenny uttered shrieks of delight at the sight of flowers growing up the cottage walls, and declared they were "just like a music-'all without the drink license." As my horses required a rest, I was forced to abandon my intention of dropping these persons at their lodgings and returning to town at once, and I could not go to the inn lest I should meet inquisitive acquaintances. Disagreeable circumstances, therefore, compelled me to take tea with a waiter's family—close to a window too, through which I could see the girl Jenny talking excitedly to the villagers, and telling them, I felt certain, that I had been good to William. I had a desire to go out and put myself right with those people.

William's long connection with the club should have given him some manners, but apparently his class cannot take them on, for, though he knew I regarded his thanks as an insult, he looked them when he was not speaking them, and hardly had he sat down, by my orders, than he remembered that I was a member of the club, and jumped up. Nothing is in worse form than whispering, yet again and again, when he thought I was not listening, he whispered to Mrs. Hicking, "You don't feel faint?" or "How are you now?" He was also in extravagant glee because she ate two cakes (it takes so little to put these people in good spirits), and when Mushroom Cloud Press | Classic Prose Collection

she said she felt like another being already the fellow's face charged me with the change. I could not but conclude, from the way Mrs. Hicking let the baby pound her, that she was stronger than she had pretended.

I remained longer than was necessary, because I had something to say to William which I knew he would misunderstand, and so I put off saying it. But when he announced that it was time for him to return to London,—at which his wife suddenly paled, so that he had to sign to her not to break down,—I delivered the message.

"William," I said, "the head waiter asked me to say that you could take a fortnight's holiday just now. Your wages will be paid as usual."

Confound them! William had me by the hand, and his wife was in tears before I could reach the door.

"Is it your doing again, sir?" William cried.

"William!" I said, fiercely.

"We owe everything to you," he insisted. "The port wine—"

"Because I had no room for it in my cellar."

"The money for the nurse in London—"

"Because I objected to being waited on by a man who got no sleep."

"These lodgings—"

"Because I wanted to do something for my old nurse."

"And now, sir, a fortnight's holiday!"

"Good-bye, William!" I said, in a fury.

But before I could get away Mrs. Hicking signed to William to leave the room, and then she kissed my hand. She said something to me. It was about my wife. Somehow I—What business had William to tell her about my wife?

They are all back in Drury Lane now, and William tells me that his wife sings at her work just as she did eight years ago. I have no interest in this, and try to check his talk of it; but such people have no sense of propriety, and he even speaks of the girl Jenny, who sent me lately a gaudy pair of worsted gloves worked by her own hand. The meanest advantage they took of my weakness, however, was in calling their baby after me. I have an uncomfortable suspicion, too, that William has given the other waiters his version of the affair; but I feel safe so long as it does not reach the committee.
```

---

## IC-1947: The Magic Shop

- Title: The Magic Shop
- Author (byline): H.G. Wells
- Work: Classic Prose Collection
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 4078
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
I had seen the Magic Shop from afar several times; I had passed it once or twice, a shop window of alluring little objects, magic balls, magic hens, wonderful cones, ventriloquist dolls, the material of the basket trick, packs of cards that looked all right, and all that sort of thing, but never had I thought of going in until one day, almost without warning, Gip hauled me by my finger right up to the window, and so conducted himself that there was nothing for it but to take him in. I had not thought the place was there, to tell the truth--a modest-sized frontage in Regent Street, between the picture shop and the place where the chicks run about just out of patent incubators, but there it was sure enough. I had fancied it was down nearer the Circus, or round the corner in Oxford Street, or even in Holborn; always over the way and a little inaccessible it had been, with something of the mirage in its position; but here it was now quite indisputably, and the fat end of Gip's pointing finger made a noise upon the glass.

"If I was rich," said Gip, dabbing a finger at the Disappearing Egg, "I'd buy myself that. And that"--which was The Crying Baby, Very Human --and that," which was a mystery, and called, so a neat card asserted, "Buy One and Astonish Your Friends."

"Anything," said Gip, "will disappear under one of those cones. I have read about it in a book.

"And there, dadda, is the Vanishing Halfpenny--, only they've put it this way up so's we can't see how it's done."

Gip, dear boy, inherits his mother's breeding, and he did not propose to enter the shop or worry in any way; only, you know, quite unconsciously he lugged my finger doorward, and he made his interest clear.

"That," he said, and pointed to the Magic Bottle.

"If you had that?" I said; at which promising inquiry he looked up with a sudden radiance.

"I could show it to Jessie," he said, thoughtful as ever of others.

Mushroom Cloud Press | Classic Prose Collection

"It's less than a hundred days to your birthday, Gibbles," I said, and laid my hand on the door-handle.

Gip made no answer, but his grip tightened on my finger, and so we came into the shop.

It was no common shop this; it was a magic shop, and all the prancing precedence Gip would have taken in the matter of mere toys was wanting. He left the burthen of the conversation to me.

It was a little, narrow shop, not very well lit, and the door-bell pinged again with a plaintive note as we closed it behind us. For a moment or so we were alone and could glance about us. There was a tiger in papier-mache on the glass case that covered the low counter--a grave, kind-eyed tiger that waggled his head in a methodical manner; there were several crystal spheres, a china hand holding magic cards, a stock of magic fish-bowls in various sizes, and an immodest magic hat that shamelessly displayed its springs. On the floor were magic mirrors; one to draw you out long and thin, one to swell your head and vanish your legs, and one to make you short and fat like a draught; and while we were laughing at these the shopman, as I suppose, came in.

At any rate, there he was behind the counter--a curious, sallow, dark man, with one ear larger than the other and a chin like the toe-cap of a boot.

"What can we have the pleasure?" he said, spreading his long, magic fingers on the glass case; and so with a start we were aware of him.

"I want," I said, "to buy my little boy a few simple tricks."

"Legerdemain?" he asked. "Mechanical? Domestic?"

"Anything amusing?" said I.

"Um!" said the shopman, and scratched his head for a moment as if thinking. Then, quite distinctly, he drew from his head a glass ball. "Something in this way?" he said, and held it out.

The action was unexpected. I had seen the trick done at entertainments endless times before--it's part of the common stock of conjurers-- but I had not expected it here.

Mushroom Cloud Press | Classic Prose Collection

"That's good," I said, with a laugh.

"Isn't it?" said the shopman.

Gip stretched out his disengaged hand to take this object and found merely a blank palm.

"It's in your pocket," said the shopman, and there it was!

"How much will that be?" I asked.

"We make no charge for glass balls," said the shopman politely. "We get them,"-- he picked one out of his elbow as he spoke--"free." He produced another from the back of his neck, and laid it beside its predecessor on the counter. Gip regarded his glass ball sagely, then directed a look of inquiry at the two on the counter, and finally brought his round-eyed scrutiny to the shopman, who smiled.

"You may have those too," said the shopman, "and, if you don't mind, one from my mouth. So!"

Gip counselled me mutely for a moment, and then in a profound silence put away the four balls, resumed my reassuring finger, and nerved himself for the next event.

"We get all our smaller tricks in that way," the shopman remarked.

I laughed in the manner of one who subscribes to a jest. "Instead of going to the wholesale shop," I said. "Of course, it's cheaper."

"In a way," the shopman said. "Though we pay in the end. But not so heavily--as people suppose. . . . Our larger tricks, and our daily provisions and all the other things we want, we get out of that hat. . . And you know, sir, if you'll excuse my saying it, there isn't a wholesale shop, not for Genuine Magic goods, sir. I don't know if you noticed our inscription--the Genuine Magic shop." He drew a business-card from his cheek and handed it to me. "Genuine," he said, with his finger on the word, and added, "There is absolutely no deception, sir."

He seemed to be carrying out the joke pretty thoroughly, I thought.

Mushroom Cloud Press | Classic Prose Collection

He turned to Gip with a smile of remarkable affability. "You, you know, are the Right Sort of Boy."

I was surprised at his knowing that, because, in the interests of discipline, we keep it rather a secret even at home; but Gip received it in unflinching silence, keeping a steadfast eye on him.

"It's only the Right Sort of Boy gets through that doorway."

And, as if by way of illustration, there came a rattling at the door, and a squeaking little voice could be faintly heard. "Nyar! I warn 'a go in there, dadda, I warn 'a go in there. Ny-a-a-ah!" and then the accents of a down-trodden parent, urging consolations and propitiations. "It's locked, Edward," he said.

"But it isn't," said I.

"It is, sir," said the shopman, "always--for that sort of child," and as he spoke we had a glimpse of the other youngster, a little, white face, pallid from sweet-eating and over-sapid food, and distorted by evil passions, a ruthless little egotist, pawing at the enchanted pane. "It's no good, sir," said the shopman, as I moved, with my natural helpfulness, doorward, and presently the spoilt child was carried off howling.

"How do you manage that?" I said, breathing a little more freely.

"Magic!" said the shopman, with a careless wave of the hand, and behold! sparks of coloured fire flew out of his fingers and vanished into the shadows of the shop.

"You were saying," he said, addressing himself to Gip, "before you came in, that you would like one of our 'Buy One and Astonish your Friends' boxes?"

Gip, after a gallant effort, said "Yes."

"It's in your pocket."

And leaning over the counter--he really had an extraordinarily long body--this amazing person produced the article in the customary conjurer's manner. "Paper," he said, and took a sheet out of the empty hat with the springs; "string," and behold his mouth was a string-box, from which he drew an unending thread, which when he had tied his parcel he bit off--and, it seemed to me, swallowed the ball of string.

Mushroom Cloud Press | Classic Prose Collection

And then he lit a candle at the nose of one of the ventriloquist's dummies, stuck one of his fingers (which had become sealing-wax red) into the flame, and so sealed the parcel. "Then there was the Disappearing Egg," he remarked, and produced one from within my coat-breast and packed it, and also The Crying Baby, Very Human. I handed each parcel to Gip as it was ready, and he clasped them to his chest.

He said very little, but his eyes were eloquent; the clutch of his arms was eloquent. He was the playground of unspeakable emotions. These, you know, were real Magics. Then, with a start, I discovered something moving about in my hat-- something soft and jumpy. I whipped it off, and a ruffled pigeon--no doubt a confederate--dropped out and ran on the counter, and went, I fancy, into a cardboard box behind the papier-mache tiger.

"Tut, tut!" said the shopman, dexterously relieving me of my headdress; "careless bird, and--as I live--nesting!"

He shook my hat, and shook out into his extended hand two or three eggs, a large marble, a watch, about half-a-dozen of the inevitable glass balls, and then crumpled, crinkled paper, more and more and more, talking all the time of the way in which people neglect to brush their hats inside as well as out, politely, of course, but with a certain personal application. "All sorts of things accumulate, sir. . . . Not you, of course, in particular. . . . Nearly every customer. . . . Astonishing what they carry about with them. . . ." The crumpled paper rose and billowed on the counter more and more and more, until he was nearly hidden from us, until he was altogether hidden, and still his voice went on and on. "We none of us know what the fair semblance of a human being may conceal, sir. Are we all then no better than brushed exteriors, whited sepulchres--"

His voice stopped--exactly like when you hit a neighbour's gramophone with a well-aimed brick, the same instant silence, and the rustle of the paper stopped, and everything was still. . . .

"Have you done with my hat?" I said, after an interval.

There was no answer.

I stared at Gip, and Gip stared at me, and there were our distortions in the magic mirrors, looking very rum, and grave, and quiet. . . .

Mushroom Cloud Press | Classic Prose Collection

"I think we'll go now," I said. "Will you tell me how much all this comes to? . . . .

"I say," I said, on a rather louder note, "I want the bill; and my hat, please."

It might have been a sniff from behind the paper pile. . . .

"Let's look behind the counter, Gip," I said. "He's making fun of us."

I led Gip round the head-wagging tiger, and what do you think there was behind the counter? No one at all! Only my hat on the floor, and a common conjurer's lop-eared white rabbit lost in meditation, and looking as stupid and crumpled as only a conjurer's rabbit can do. I resumed my hat, and the rabbit lolloped a lollop or so out of my way.

"Dadda!" said Gip, in a guilty whisper.

"What is it, Gip?" said I.

"I do like this shop, dadda."

"So should I," I said to myself, "if the counter wouldn't suddenly extend itself to shut one off from the door." But I didn't call Gip's attention to that. "Pussy!" he said, with a hand out to the rabbit as it came lolloping past us; "Pussy, do Gip a magic!" and his eyes followed it as it squeezed through a door I had certainly not remarked a moment before. Then this door opened wider, and the man with one ear larger than the other appeared again. He was smiling still, but his eye met mine with something between amusement and defiance. "You'd like to see our show-room, sir," he said, with an innocent suavity. Gip tugged my finger forward. I glanced at the counter and met the shopman's eye again. I was beginning to think the magic just a little too genuine. "We haven't VERY much time," I said. But somehow we were inside the show-room before I could finish that.

"All goods of the same quality," said the shopman, rubbing his flexible hands together, "and that is the Best. Nothing in the place that isn't genuine Magic, and warranted thoroughly rum. Excuse me, sir!"

I felt him pull at something that clung to my coat-sleeve, and then I saw he held a little, wriggling red demon by the tail--the little creature bit and fought and tried to get at his hand--and in a moment he tossed it carelessly behind a counter. No doubt the thing was only an image of twisted indiarubber, but for the moment--! And his Mushroom Cloud Press | Classic Prose Collection

gesture was exactly that of a man who handles some petty biting bit of vermin. I glanced at Gip, but Gip was looking at a magic rocking- horse. I was glad he hadn't seen the thing. "I say," I said, in an undertone, and indicating Gip and the red demon with my eyes, "you haven't many things like that about, have you?"

"None of ours! Probably brought it with you," said the shopman-- also in an undertone, and with a more dazzling smile than ever. "Astonishing what people will carry about with them unawares!" And then to Gip, "Do you see anything you fancy here?"

There were many things that Gip fancied there.

He turned to this astonishing tradesman with mingled confidence and respect. "Is that a Magic Sword?" he said.

"A Magic Toy Sword. It neither bends, breaks, nor cuts the fingers. It renders the bearer invincible in battle against any one under eighteen. Half-a-crown to seven and sixpence, according to size. These panoplies on cards are for juvenile knights-errant and very useful-- shield of safety, sandals of swiftness, helmet of invisibility."

"Oh, daddy!" gasped Gip.

I tried to find out what they cost, but the shopman did not heed me. He had got Gip now; he had got him away from my finger; he had embarked upon the exposition of all his confounded stock, and nothing was going to stop him. Presently I saw with a qualm of distrust and something very like jealousy that Gip had hold of this person's finger as usually he has hold of mine. No doubt the fellow was interesting, I thought, and had an interestingly faked lot of stuff, really good faked stuff, still--

I wandered after them, saying very little, but keeping an eye on this prestidigital fellow. After all, Gip was enjoying it. And no doubt when the time came to go we should be able to go quite easily.

It was a long, rambling place, that show-room, a gallery broken up by stands and stalls and pillars, with archways leading off to other departments, in which the queerest-looking assistants loafed and stared at one, and with perplexing mirrors and curtains. So perplexing, indeed, were these that I was presently unable to make out the door by which we had come.

Mushroom Cloud Press | Classic Prose Collection

The shopman showed Gip magic trains that ran without steam or clockwork, just as you set the signals, and then some very, very valuable boxes of soldiers that all came alive directly you took off the lid and said--. I myself haven't a very quick ear and it was a tongue- twisting sound, but Gip--he has his mother's ear--got it in no time. "Bravo!" said the shopman, putting the men back into the box unceremoniously and handing it to Gip. "Now," said the shopman, and in a moment Gip had made them all alive again.

"You'll take that box?" asked the shopman.

"We'll take that box," said I, "unless you charge its full value. In which case it would need a Trust Magnate--"

"Dear heart! No!" and the shopman swept the little men back again, shut the lid, waved the box in the air, and there it was, in brown paper, tied up and--with Gip's full name and address on the paper!

The shopman laughed at my amazement.

"This is the genuine magic," he said. "The real thing."

"It's a little too genuine for my taste," I said again.

After that he fell to showing Gip tricks, odd tricks, and still odder the way they were done. He explained them, he turned them inside out, and there was the dear little chap nodding his busy bit of a head in the sagest manner.

I did not attend as well as I might. "Hey, presto!" said the Magic Shopman, and then would come the clear, small "Hey, presto!" of the boy. But I was distracted by other things. It was being borne in upon me just how tremendously rum this place was; it was, so to speak, inundated by a sense of rumness. There was something a little rum about the fixtures even, about the ceiling, about the floor, about the casually distributed chairs. I had a queer feeling that whenever I wasn't looking at them straight they went askew, and moved about, and played a noiseless puss-in-the-corner behind my back. And the cornice had a serpentine design with masks-- masks altogether too expressive for proper plaster.

Then abruptly my attention was caught by one of the odd-looking assistants. He was some way off and evidently unaware of my presence-- I saw a sort of three-quarter length of him over a pile of toys and through an arch--and, you know, he Mushroom Cloud Press | Classic Prose Collection

was leaning against a pillar in an idle sort of way doing the most horrid things with his features! The particular horrid thing he did was with his nose. He did it just as though he was idle and wanted to amuse himself. First of all it was a short, blobby nose, and then suddenly he shot it out like a telescope, and then out it flew and became thinner and thinner until it was like a long, red, flexible whip. Like a thing in a nightmare it was! He flourished it about and flung it forth as a fly-fisher flings his line.

My instant thought was that Gip mustn't see him. I turned about, and there was Gip quite preoccupied with the shopman, and thinking no evil. They were whispering together and looking at me. Gip was standing on a little stool, and the shopman was holding a sort of big drum in his hand.

"Hide and seek, dadda!" cried Gip. "You're He!"

And before I could do anything to prevent it, the shopman had clapped the big drum over him. I saw what was up directly. "Take that off," I cried, "this instant! You'll frighten the boy. Take it off!"

The shopman with the unequal ears did so without a word, and held the big cylinder towards me to show its emptiness. And the little stool was vacant! In that instant my boy had utterly disappeared? . . .

You know, perhaps, that sinister something that comes like a hand out of the unseen and grips your heart about. You know it takes your common self away and leaves you tense and deliberate, neither slow nor hasty, neither angry nor afraid. So it was with me.

I came up to this grinning shopman and kicked his stool aside.

"Stop this folly!" I said. "Where is my boy?"

"You see," he said, still displaying the drum's interior, "there is no deception---"

I put out my hand to grip him, and he eluded me by a dexterous movement. I snatched again, and he turned from me and pushed open a door to escape. "Stop!" I said, and he laughed, receding. I leapt after him--into utter darkness.

THUD!

Mushroom Cloud Press | Classic Prose Collection

"Lor' bless my 'eart! I didn't see you coming, sir!"

I was in Regent Street, and I had collided with a decent-looking working man; and a yard away, perhaps, and looking a little perplexed with himself, was Gip. There was some sort of apology, and then Gip had turned and come to me with a bright little smile, as though for a moment he had missed me.

And he was carrying four parcels in his arm!

He secured immediate possession of my finger.

For the second I was rather at a loss. I stared round to see the door of the magic shop, and, behold, it was not there! There was no door, no shop, nothing, only the common pilaster between the shop where they sell pictures and the window with the chicks! . . .

I did the only thing possible in that mental tumult; I walked straight to the kerbstone and held up my umbrella for a cab.

"'Ansoms," said Gip, in a note of culminating exultation.

I helped him in, recalled my address with an effort, and got in also. Something unusual proclaimed itself in my tail-coat pocket, and I felt and discovered a glass ball. With a petulant expression I flung it into the street.

Gip said nothing.

For a space neither of us spoke.

"Dada!" said Gip, at last, "that was a proper shop!"

I came round with that to the problem of just how the whole thing had seemed to him. He looked completely undamaged--so far, good; he was neither scared nor unhinged, he was simply tremendously satisfied with the afternoon's entertainment, and there in his arms were the four parcels.

Confound it! what could be in them?

"Um!" I said. "Little boys can't go to shops like that every day."

Mushroom Cloud Press | Classic Prose Collection

He received this with his usual stoicism, and for a moment I was sorry I was his father and not his mother, and so couldn't suddenly there, coram publico, in our hansom, kiss him. After all, I thought, the thing wasn't so very bad.

But it was only when we opened the parcels that I really began to be reassured. Three of them contained boxes of soldiers, quite ordinary lead soldiers, but of so good a quality as to make Gip altogether forget that originally these parcels had been Magic Tricks of the only genuine sort, and the fourth contained a kitten, a little living white kitten, in excellent health and appetite and temper.

I saw this unpacking with a sort of provisional relief. I hung about in the nursery for quite an unconscionable time. . . .

That happened six months ago. And now I am beginning to believe it is all right. The kitten had only the magic natural to all kittens, and the soldiers seem as steady a company as any colonel could desire. And Gip--?

The intelligent parent will understand that I have to go cautiously with Gip.

But I went so far as this one day. I said, "How would you like your soldiers to come alive, Gip, and march about by themselves?"

"Mine do," said Gip. "I just have to say a word I know before I open the lid."

"Then they march about alone?"

"Oh, quite, dadda. I shouldn't like them if they didn't do that."

I displayed no unbecoming surprise, and since then I have taken occasion to drop in upon him once or twice, unannounced, when the soldiers were about, but so far I have never discovered them performing in anything like a magical manner.

It's so difficult to tell.

There's also a question of finance. I have an incurable habit of paying bills. I have been up and down Regent Street several times, looking for that shop. I am inclined to think, indeed, that in that matter honour is satisfied, and that, since Gip's name and address are known to them, I may very well leave it to these people, whoever they may be, to send in their bill in their own time.
```

---

## IC-1948: The Outcasts of Poker Flat

- Title: The Outcasts of Poker Flat
- Author (byline): Bret Harte
- Work: Classic Prose Collection
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 4047
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
As Mr. John Oakhurst, gambler, stepped into the main street of Poker Flat on the morning of the twenty-third of November, 1850, he was conscious of a change in its moral atmosphere since the preceding night. Two or three men, conversing earnestly together, ceased as he approached, and exchanged significant glances. There was a Sabbath lull in the air which, in a settlement unused to Sabbath influences, looked ominous.

Mr. Oakhurst's calm, handsome face betrayed small concern in these indications. Whether he was conscious of any predisposing cause was another question. "I reckon they're after somebody," he reflected; "likely it's me." He returned to his pocket the handkerchief with which he had been whipping away the red dust of Poker Flat from his neat boots, and quietly discharged his mind of any further conjecture.

In point of fact, Poker Flat was "after somebody." It had lately suffered the loss of several thousand dollars, two valuable horses, and a prominent citizen. It was experiencing a spasm of virtuous reaction, quite as lawless and ungovernable as any of the acts that had provoked it. A secret committee had determined to rid the town of all improper persons. This was done permanently in regard of two men who were then hanging from the boughs of a sycamore in the gulch, and temporarily in the banishment of certain other objectionable characters. I regret to say that some of these were ladies. It is but due to the sex, however, to state that their impropriety was professional, and it was only in such easily established standards of evil that Poker Flat ventured to sit in judgment.

Mr. Oakhurst was right in supposing that he was included in this category. A few of the committee had urged hanging him as a possible example, and a sure method of reimbursing themselves from his pockets of the sums he had won from them. "It's agin justice," said Jim Wheeler, "to let this yer young man from Roaring Camp--an entire stranger--carry away our money." But a crude sentiment of equity residing in the breasts of those who had been fortunate enough to win from Mr. Oakhurst overruled this narrower local prejudice.

Mr. Oakhurst received his sentence with philosophic calmness, none the less coolly that he was aware of the hesitation of his judges. He was too much of a gambler not to accept Fate. With him life was at best an uncertain game, and he recognized the usual percentage in favor of the dealer.

A body of armed men accompanied the deported wickedness of Poker Flat to the outskirts of the settlement. Besides Mr. Oakhurst, who was known to be a coolly desperate man, and for whose intimidation the armed escort was intended, the expatriated party consisted of a young woman familiarly known as the "Duchess"; another, who had won the title of "Mother Shipton"; and "Uncle Billy," a suspected sluice-robber and confirmed drunkard. The cavalcade provoked no comments from the spectators, nor was any word uttered by the escort. Only, when the gulch which marked the uttermost limit of Poker Flat was reached, the leader spoke briefly and to the point. The exiles were forbidden to return at the peril of their lives.

As the escort disappeared, their pent-up feelings found vent in a few hysterical tears from the Duchess, some bad language from Mother Shipton, and a Parthian volley of expletives from Uncle Billy. The philosophic Oakhurst alone remained silent. He listened calmly to Mother Shipton's desire to cut somebody's heart out, to the repeated statements of the Duchess that she would die in the road, and to the alarming oaths that seemed to be bumped out of Uncle Billy as he rode forward. With the easy good humor characteristic of his class, he insisted upon exchanging his own riding horse, "Five Spot," for the sorry mule which the Duchess rode. But even this act did not draw the party into any closer sympathy. The young woman readjusted her somewhat draggled plumes with a feeble, faded coquetry; Mother Shipton eyed the possessor of "Five Spot" with malevolence, and Uncle Billy included the whole party in one sweeping anathema.

The road to Sandy Bar--a camp that, not having as yet experienced the regenerating influences of Poker Flat, consequently seemed to offer some invitation to the emigrants--lay over a steep mountain range. It was distant a day's severe travel. In that advanced season, the party soon passed out of the moist, temperate regions of the foothills into the dry, cold, bracing air of the Sierras. The trail was narrow and difficult. At noon the Duchess, rolling out of her saddle upon the ground, declared her intention of going no farther, and the party halted.

The spot was singularly wild and impressive. A wooded amphitheater, surrounded on three sides by precipitous cliffs of naked granite, sloped gently toward the crest of another precipice that overlooked the valley. It was, undoubtedly, the most suitable spot for a camp, had camping been advisable. But Mr. Oakhurst knew that scarcely half the journey to Sandy Bar was accomplished, and the party were not equipped or provisioned for delay. This fact he pointed out to his companions curtly, with a philosophic commentary on the folly of "throwing up their hand before the game was played out." But they were furnished with liquor, which in this emergency stood them in place of food, fuel, rest, and prescience. In spite of his remonstrances, it was not long before they were more or less under its influence. Uncle Billy passed rapidly from a bellicose state into one of stupor, the Duchess became maudlin, and Mother Shipton snored. Mr. Oakhurst alone remained erect, leaning against a rock, calmly surveying them.

Mr. Oakhurst did not drink. It interfered with a profession which required coolness, impassiveness, and presence of mind, and, in his own language, he "couldn't afford it." As he gazed at his recumbent fellow exiles, the loneliness begotten of his pariah trade, his habits of life, his very vices, for the first time seriously oppressed him. He bestirred himself in dusting his black clothes, washing his hands and face, and other acts characteristic of his studiously neat habits, and for a moment forgot his annoyance. The thought of deserting his weaker and more pitiable companions never perhaps occurred to him. Yet he could not help feeling the want of that excitement which, singularly enough, was most conducive to that calm equanimity for which he was notorious. He looked at the gloomy walls that rose a thousand feet sheer above the circling pines around him; at the sky, ominously clouded; at the valley below, already deepening into shadow. And, doing so, suddenly he heard his own name called.

A horseman slowly ascended the trail. In the fresh, open face of the newcomer Mr. Oakhurst recognized Tom Simson, otherwise known as the "Innocent" of Sandy Bar. He had met him some months before over a "little game," and had, with perfect equanimity, won the entire fortune--amounting to some forty dollars--of that guileless youth. After the game was finished, Mr. Oakhurst drew the youthful speculator behind the door and thus addressed him: "Tommy, you're a good little man, but you can't gamble worth a cent. Don't try it over again." He then handed him his money back, pushed him gently from the room, and so made a devoted slave of Tom Simson.

There was a remembrance of this in his boyish and enthusiastic greeting of Mr. Oakhurst. He had started, he said, to go to Poker Flat to seek his fortune. "Alone?" No, not exactly alone; in fact (a giggle), he had run away with Piney Woods. Didn't Mr. Oakhurst remember Piney? She that used to wait on the table at the Temperance House? They had been engaged a long time, but old Jake Woods had objected, and so they had run away, and were going to Poker Flat to be married, and here they were. And they were tired out, and how lucky it was they had found a place to camp and company. All this the Innocent delivered rapidly, while Piney, a stout, comely damsel of fifteen, emerged from behind the pine tree, where she had been blushing unseen, and rode to the side of her lover.

Mr. Oakhurst seldom troubled himself with sentiment, still less with propriety; but he had a vague idea that the situation was not fortunate. He retained, however, his presence of mind sufficiently to kick Uncle Billy, who was about to say something, and Uncle Billy was sober enough to recognize in Mr. Oakhurst's kick a superior power that would not bear trifling. He then endeavored to dissuade Tom Simson from delaying further, but in vain. He even pointed out the fact that there was no provision, nor means of making a camp. But, unluckily, the Innocent met this objection by assuring the party that he was provided with an extra mule loaded with provisions and by the discovery of a rude attempt at a log house near the trail. "Piney can stay with Mrs. Oakhurst," said the Innocent, pointing to the Duchess, "and I can shift for myself."

Nothing but Mr. Oakhurst's admonishing foot saved Uncle Billy from bursting into a roar of laughter. As it was, he felt compelled to retire up the canyon until he could recover his gravity. There he confided the joke to the tall pine trees, with many slaps of his leg, contortions of his face, and the usual profanity. But when he returned to the party, he found them seated by a fire--for the air had grown strangely chill and the sky overcast--in apparently amicable conversation. Piney was actually talking in an impulsive, girlish fashion to the Duchess, who was listening with an interest and animation she had not shown for many days. The Innocent was holding forth, apparently with equal effect, to Mr. Oakhurst and Mother Shipton, who was actually relaxing into amiability. "Is this yer a damned picnic?" said Uncle Billy with inward scorn as he surveyed the sylvan group, the glancing firelight, and the tethered animals in the foreground. Suddenly an idea mingled with the alcoholic fumes that disturbed his brain. It was apparently of a jocular nature, for he felt impelled to slap his leg again and cram his fist into his mouth.

As the shadows crept slowly up the mountain, a slight breeze rocked the tops of the pine trees, and moaned through their long and gloomy aisles. The ruined cabin, patched and covered with pine boughs, was set apart for the ladies. As the lovers parted, they unaffectedly exchanged a kiss, so honest and sincere that it might have been heard above the swaying pines. The frail Duchess and the malevolent Mother Shipton were probably too stunned to remark upon this last evidence of simplicity, and so turned without a word to the hut. The fire was replenished, the men lay down before the door, and in a few minutes were asleep.

Mr. Oakhurst was a light sleeper. Toward morning he awoke benumbed and cold. As he stirred the dying fire, the wind, which was now blowing strongly, brought to his cheek that which caused the blood to leave it--snow!

He started to his feet with the intention of awakening the sleepers, for there was no time to lose. But turning to where Uncle Billy had been lying, he found him gone. A suspicion leaped to his brain and a curse to his lips. He ran to the spot where the mules had been tethered; they were no longer there. The tracks were already rapidly disappearing in the snow.

The momentary excitement brought Mr. Oakhurst back to the fire with his usual calm. He did not waken the sleepers. The Innocent slumbered peacefully, with a smile on his good-humored, freckled face; the virgin Piney slept beside her frailer sisters as sweetly as though attended by celestial guardians; and Mr. Oakhurst, drawing his blanket over his shoulders, stroked his mustaches and waited for the dawn. It came slowly in a whirling mist of snowflakes that dazzled and confused the eye. What could be seen of the landscape appeared magically changed. He looked over the valley, and summed up the present and future in two words--"snowed in!"

A careful inventory of the provisions, which, fortunately for the party, had been stored within the hut and so escaped the felonious fingers of Uncle Billy, disclosed the fact that with care and prudence they might last ten days longer. "That is," said Mr. Oakhurst, sotto voce to the Innocent, "if you're willing to board us. If you ain't--and perhaps you'd better not--you can wait till Uncle Billy gets back with provisions." For some occult reason, Mr. Oakhurst could not bring himself to disclose Uncle Billy's rascality, and so offered the hypothesis that he had wandered from the camp and had accidentally stampeded the animals. He dropped a warning to the Duchess and Mother Shipton, who of course knew the facts of their associate's defection. "They'll find out the truth about us all when they find out anything," he added, significantly, "and there's no good frightening them now."

Tom Simson not only put all his worldly store at the disposal of Mr. Oakhurst, but seemed to enjoy the prospect of their enforced seclusion. "We'll have a good camp for a week, and then the snow'll melt, and we'll all go back together." The cheerful gaiety of the young man, and Mr. Oakhurst's calm, infected the others. The Innocent with the aid of pine boughs extemporized a thatch for the roofless cabin, and the Duchess directed Piney in the rearrangement of the interior with a taste and tact that opened the blue eyes of that provincial maiden to their fullest extent. "I reckon now you're used to fine things at Poker Flat," said Piney. The Duchess turned away sharply to conceal something that reddened her cheeks through its professional tint, and Mother Shipton requested Piney not to "chatter." But when Mr. Oakhurst returned from a weary search for the trail, he heard the sound of happy laughter echoed from the rocks. He stopped in some alarm, and his thoughts first naturally reverted to the whisky, which he had prudently cached. "And yet it don't somehow sound like whisky," said the gambler. It was not until he caught sight of the blazing fire through the still-blinding storm and the group around it that he settled to the conviction that it was "square fun."

Whether Mr. Oakhurst had cached his cards with the whisky as something debarred the free access of the community, I cannot say. It was certain that, in Mother Shipton's words, he "didn't say cards once" during that evening. Haply the time was beguiled by an accordion, produced somewhat ostentatiously by Tom Simson from his pack. Notwithstanding some difficulties attending the manipulation of this instrument, Piney Woods managed to pluck several reluctant melodies from its keys, to an accompaniment by the Innocent on a pair of bone castanets. But the crowning festivity of the evening was reached in a rude camp-meeting hymn, which the lovers, joining hands, sang with great earnestness and vociferation. I fear that a certain defiant tone and Covenanter's swing to its chorus, rather than any devotional quality, caused it speedily to infect the others, who at last joined in the refrain:

"I'm proud to live in the service of the Lord, And I'm bound to die in

His army."

The pines rocked, the storm eddied and whirled above the miserable group, and the flames of their altar leaped heavenward as if in token of the vow.

At midnight the storm abated, the rolling clouds parted, and the stars glittered keenly above the sleeping camp. Mr. Oakhurst, whose professional habits had enabled him to live on the smallest possible amount of sleep, in dividing the watch with Tom Simson somehow managed to take upon himself the greater part of that duty. He excused himself to the Innocent by saying that he had "often been a week without sleep." "Doing what?" asked Tom. "Poker!" replied Oakhurst, sententiously; "when a man gets a streak of luck,--dumb luck--he don't get tired. The luck gives in first. Luck," continued the gambler, reflectively, "is a mighty queer thing. All you know about it for certain is that it's bound to change. And it's finding out when it's going to change that makes you. We've had a streak of bad luck since we left Poker Flat--you come along, and slap you get into it, too. If you can hold your cards right along you're all right. For," added the gambler, with cheerful irrelevance, "'I'm proud to live in the service of the Lord, And I'm bound to die in His army.'"

The third day came, and the sun, looking through the white- curtained valley, saw the outcasts divide their slowly decreasing store of provisions for the morning meal. It was one of the peculiarities of that mountain climate that its rays diffused a kindly warmth over the wintry landscape, as if in regretful commiseration of the past. But it revealed drift on drift of snow piled high around the hut--a hopeless, uncharted, trackless sea of white lying below the rocky shores to which the castaways still clung. Through the marvelously clear air the smoke of the pastoral village of Poker Flat rose miles away. Mother Shipton saw it, and from a remote pinnacle of her rocky fastness hurled in that direction a final malediction. It was her last vituperative attempt, and perhaps for that reason was invested with a certain degree of sublimity. It did her good, she privately informed the Duchess. "Just you go out there and cuss, and see." She then set herself to the task of amusing "the child," as she and the Duchess were pleased to call Piney. Piney was no chicken, but it was a soothing and original theory of the pair thus to account for the fact that she didn't swear and wasn't improper.

When night crept up again through the gorges, the reedy notes of the accordion rose and fell in fitful spasms and long-drawn gasps by the flickering campfire. But music failed to fill entirely the aching void left by insufficient food, and a new diversion was proposed by Piney--storytelling. Neither Mr. Oakhurst nor his female companions caring to relate their personal experiences, this plan would have failed too but for the Innocent. Some months before he had chanced upon a stray copy of Mr. Pope's ingenious translation of the ILIAD. He now proposed to narrate the principal incidents of that poem--having thoroughly mastered the argument and fairly forgotten the words--in the current vernacular of Sandy Bar. And so for the rest of that night the Homeric demigods again walked the earth. Trojan bully and wily Greek wrestled in the winds, and the great pines in the canyon seemed to bow to the wrath of the son of Peleus. Mr. Oakhurst listened with quiet satisfaction. Most especially was he interested in the fate of "Ash-heels," as the Innocent persisted in denominating the "swift-footed Achilles."

So with small food and much of Homer and the accordion, a week passed over the heads of the outcasts. The sun again forsook them, and again from leaden skies the snowflakes were sifted over the land. Day by day closer around them drew the snowy circle, until at last they looked from their prison over drifted walls of dazzling white that towered twenty feet above their heads. It became more and more difficult to replenish their fires, even from the fallen trees beside them, now half-hidden in the drifts. And yet no one complained. The lovers turned from the dreary prospect and looked into each other's eyes, and were happy. Mr. Oakhurst settled himself coolly to the losing game before him. The Duchess, more cheerful than she had been, assumed the care of Piney. Only Mother Shipton--once the strongest of the party--seemed to sicken and fade. At midnight on the tenth day she called Oakhurst to her side. "I'm going," she said, in a voice of querulous weakness, "but don't say anything about it. Don't waken the kids.

Take the bundle from under my head and open it." Mr. Oakhurst did so. It contained Mother Shipton's rations for the last week, untouched. "Give 'em to the child," she said, pointing to the sleeping Piney.

"You've starved yourself," said the gambler.

"That's what they call it," said the woman, querulously, as she lay down again and, turning her face to the wall, passed quietly away.

The accordion and the bones were put aside that day, and Homer was forgotten. When the body of Mother Shipton had been committed to the snow, Mr. Oakhurst took the Innocent aside, and showed him a pair of snowshoes, which he had fashioned from the old pack saddle. "There's one chance in a hundred to save her yet," he said, pointing to Piney; "but it's there," he added, pointing toward Poker Flat. "If you can reach there in two days she's safe." "And you?" asked Tom Simson. "I'll stay here," was the curt reply. The lovers parted with a long embrace. "You are not going, too?" said the Duchess as she saw Mr. Oakhurst apparently waiting to accompany him. "As far as the canyon," he replied. He turned suddenly, and kissed the Duchess, leaving her pallid face aflame and her trembling limbs rigid with amazement.

Night came, but not Mr. Oakhurst. It brought the storm again and the whirling snow. Then the Duchess, feeding the fire, found that someone had quietly piled beside the hut enough fuel to last a few days longer. The tears rose to her eyes, but she hid them from Piney.

The women slept but little. In the morning, looking into each other's faces, they read their fate. Neither spoke; but Piney, accepting the position of the stronger, drew near and placed her arm around the Duchess's waist. They kept this attitude for the rest of the day. That night the storm reached its greatest fury, and, rending asunder the protecting pines, invaded the very hut.

Toward morning they found themselves unable to feed the fire, which gradually died away. As the embers slowly blackened, the Duchess crept closer to Piney, and broke the silence of many hours: "Piney, can you pray?" "No, dear," said Piney, simply. The Duchess, without knowing exactly why, felt relieved, and, putting her head upon Piney's shoulder, spoke no more. And so reclining, the younger and purer pillowing the head of her soiled sister upon her virgin breast, they fell asleep.

The wind lulled as if it feared to waken them. Feathery drifts of snow, shaken from the long pine boughs, flew like white-winged birds, and settled about them as they slept. The moon through the rifted clouds looked down upon what had been the camp. But all human stain, all trace of earthly travail, was hidden beneath the spotless mantle mercifully flung from above.

They slept all that day and the next, nor did they waken when voices and footsteps broke the silence of the camp. And when pitying fingers brushed the snow from their wan faces, you could scarcely have told from the equal peace that dwelt upon them which was she that had sinned. Even the law of Poker Flat recognized this, and turned away, leaving them still locked in each other's arms.

But at the head of the gulch, on one of the largest pine trees, they found the deuce of clubs pinned to the bark with a bowie knife. It bore the following, written in pencil, in a firm hand:

BENEATH THIS TREE

LIES THE BODY

OF

JOHN OAKHURST,

WHO STRUCK A STREAK OF BAD LUCK

ON THE 23D OF NOVEMBER, 1850,

AND

HANDED IN HIS CHECKS

ON THE 7TH DECEMBER, 1850.

And pulseless and cold, with a Derringer by his side and a bullet in his heart, though still calm as in life, beneath the snow lay he who was at once the strongest and yet the weakest of the outcasts of Poker Flat.
```

---

## IC-1949: The Queen of Spades

- Title: The Queen of Spades
- Author (byline): Alexander Pushkin
- Work: Classic Prose Collection
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 3609
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
At the house of Naroumov, a cavalry officer, the long winter night had been passed in gambling. At five in the morning breakfast was served to the weary players. The winners ate with relish; the losers, on the contrary, pushed back their plates and sat brooding gloomily. Under the influence of the good wine, however, the conversation then became general.

"Well, Sourine?" said the host inquiringly.

"Oh, I lost as usual. My luck is abominable. No matter how cool I keep, I never win."

"How is it, Herman, that you never touch a card?" remarked one of the men, addressing a young officer of the Engineering Corps. "Here you are with the rest of us at five o'clock in the morning, and you have neither played nor bet all night."

"Play interests me greatly," replied the person addressed, "but I hardly care to sacrifice the necessaries of life for uncertain superfluities."

"Herman is a German, therefore economical; that explains it," said Tomsky. "But the person I can't quite understand is my grandmother, the Countess Anna Fedorovna."

"Why?" inquired a chorus of voices.

"I can't understand why my grandmother never gambles."

"I don't see anything very striking in the fact that a woman of eighty refuses to gamble," objected Naroumov.

"Have you never heard her story?"

"No--"

"Well, then, listen to it. To begin with, sixty years ago my grandmother went to Paris, where she was all the fashion. People crowded each other in the streets to get a chance to see the 'Muscovite Venus,' as she was called. All the great ladies played faro, then. On one occasion, while playing with the Duke of Orleans, she lost an enormous sum. She told her husband of the debt, but he refused outright to pay it. Nothing could induce him to change his mind on the subject, and grandmother was at her wits' ends. Finally, she remembered a friend of hers, Count Saint-Germain. You must have heard of him, as many wonderful stories have been told about him. He is said to have discovered the elixir of life, the philosopher's stone, and many other equally marvelous things. He had money at his disposal, and my grandmother knew it. She sent him a note asking him to come to see her. He obeyed her summons and found her in great distress. She painted the cruelty of her Mushroom Cloud Press | Classic Prose Collection

husband in the darkest colors, and ended by telling the Count that she depended upon his friendship and generosity.

"'I could lend you the money,' replied the Count, after a moment of thoughtfulness, 'but I know that you would not enjoy a moment's rest until you had returned it; it would only add to your embarrassment. There is another way of freeing yourself.'

"'But I have no money at all,' insisted my grandmother.

"'There is no need of money. Listen to me.'

"The Count then told her a secret which any of us would give a good deal to know."

The young gamesters were all attention. Tomsky lit his pipe, took a few whiffs, then continued:

"The next evening, grandmother appeared at Versailles at the Queen's gaming-table. The Duke of Orleans was the dealer. Grandmother made some excuse for not having brought any money, and began to punt. She chose three cards in succession, again and again, winning every time, and was soon out of debt."

"A fable," remarked Herman; "perhaps the cards were marked."

"I hardly think so," replied Tomsky, with an air of importance.

"So you have a grandmother who knows three winning cards, and you haven't found out the magic secret."

"I must say I have not. She had four sons, one of them being my father, all of whom are devoted to play; she never told the secret to one of them. But my uncle told me this much, on his word of honor. Tchaplitzky, who died in poverty after having squandered millions, lost at one time, at play, nearly three hundred thousand rubles. He was desperate and grandmother took pity on him. She told him the three cards, making him swear never to use them again. He returned to the game, staked fifty thousand rubles on each card, and came out ahead, after paying his debts."

As day was dawning the party now broke up, each one draining his glass and taking his leave.

The Countess Anna Fedorovna was seated before her mirror in her dressing-room. Three women were assisting at her toilet. The old Countess no longer made the slightest pretensions to beauty, but she still clung to all the habits of her youth, and spent as much time at her toilet as she had done sixty years before. At the window a young girl, her ward, sat at her needlework.

"Good afternoon, grandmother," cried a young officer, who had just entered the room. "I have come to ask a favor of you."

"What, Pavel?"

"I want to be allowed to present one of my friends to you, and to take you to the ball on Tuesday night."

Mushroom Cloud Press | Classic Prose Collection

"Take me to the ball and present him to me there."

After a few more remarks the officer walked up to the window where Lisaveta Ivanovna sat.

"Whom do you wish to present?" asked the girl.

"Naroumov; do you know him?"

"No; is he a soldier?"

"Yes."

"An engineer?"

"No; why do you ask?"

The girl smiled and made no reply.

Pavel Tomsky took his leave, and, left to herself, Lisaveta glanced out of the window. Soon, a young officer appeared at the corner of the street; the girl blushed and bent her head low over her canvas.

This appearance of the officer had become a daily occurrence. The man was totally unknown to her, and as she was not accustomed to coquetting with the soldiers she saw on the street, she hardly knew how to explain his presence. His persistence finally roused an interest entirely strange to her. One day, she even ventured to smile upon her admirer, for such he seemed to be.

The reader need hardly be told that the officer was no other than Herman, the would-be gambler, whose imagination had been strongly excited by the story told by Tomsky of the three magic cards.

"Ah," he thought, "if the old Countess would only reveal the secret to me. Why not try to win her good-will and appeal to her sympathy?"

With this idea in mind, he took up his daily station before the house, watching the pretty face at the window, and trusting to fate to bring about the desired acquaintance.

One day, as Lisaveta was standing on the pavement about to enter the carriage after the Countess, she felt herself jostled and a note was thrust into her hand. Turning, she saw the young officer at her elbow. As quick as thought, she put the note in her glove and entered the carriage. On her return from the drive, she hastened to her chamber to read the missive, in a state of excitement mingled with fear. It was a tender and respectful declaration of affection, copied word for word from a German novel. Of this fact, Lisa was, of course, ignorant.

The young girl was much impressed by the missive, but she felt that the writer must not be encouraged. She therefore wrote a few lines of explanation and, at the first opportunity, dropped it, with the letter, out of the window. The officer hastily crossed the street, picked up the papers and entered a shop to read them.

In no wise daunted by this rebuff, he found the opportunity to send her another note in a few days. He received no reply, but, evidently understanding the female Mushroom Cloud Press | Classic Prose Collection

heart, he presevered, begging for an interview. He was rewarded at last by the following:

"To-night we go to the ambassador's ball. We shall remain until two o'clock. I can arrange for a meeting in this way. After our departure, the servants will probably all go out, or go to sleep. At half-past eleven enter the vestibule boldly, and if you see any one, inquire for the Countess; if not, ascend the stairs, turn to the left and go on until you come to a door, which opens into her bedchamber. Enter this room and behind a screen you will find another door leading to a corridor; from this a spiral staircase leads to my sitting-room. I shall expect to find you there on my return."

Herman trembled like a leaf as the appointed hour drew near. He obeyed instructions fully, and, as he met no one, he reached the old lady's bedchamber without difficulty. Instead of going out of the small door behind the screen, however, he concealed himself in a closet to await the return of the old Countess.

The hours dragged slowly by; at last he heard the sound of wheels. Immediately lamps were lighted and servants began moving about. Finally the old woman tottered into the room, completely exhausted. Her women removed her wraps and proceeded to get her in readiness for the night. Herman watched the proceedings with a curiosity not unmingled with superstitious fear. When at last she was attired in cap and gown, the old woman looked less uncanny than when she wore her ball-dress of blue brocade.

She sat down in an easy chair beside a table, as she was in the habit of doing before retiring, and her women withdrew. As the old lady sat swaying to and fro, seemingly oblivious to her surroundings, Herman crept out of his hiding-place.

At the slight noise the old woman opened her eyes, and gazed at the intruder with a half-dazed expression.

"Have no fear, I beg of you," said Herman, in a calm voice. "I have not come to harm you, but to ask a favor of you instead."

The Countess looked at him in silence, seemingly without comprehending him. Herman thought she might be deaf, so he put his lips close to her ear and repeated his remark. The listener remained perfectly mute.

"You could make my fortune without its costing you anything," pleaded the young man; "only tell me the three cards which are sure to win, and--"

Herman paused as the old woman opened her lips as if about to speak.

"It was only a jest; I swear to you, it was only a jest," came from the withered lips.

"There was no jesting about it. Remember Tchaplitzky, who, thanks to you, was able to pay his debts."

An expression of interior agitation passed over the face of the old woman; then she relapsed into her former apathy.

Mushroom Cloud Press | Classic Prose Collection

"Will you tell me the names of the magic cards, or not?" asked Herman after a pause.

There was no reply.

The young man then drew a pistol from his pocket, exclaiming: "You old witch, I'll force you to tell me!"

At the sight of the weapon the Countess gave a second sign of life. She threw back her head and put out her hands as if to protect herself; then they dropped and she sat motionless.

Herman grasped her arm roughly, and was about to renew his threats, when he saw that she was dead!

Seated in her room, still in her ball-dress, Lisaveta gave herself up to her reflections. She had expected to find the young officer there, but she felt relieved to see that he was not.

Strangely enough, that very night at the ball, Tomsky had rallied her about her preference for the young officer, assuring her that he knew more than she supposed he did.

"Of whom are you speaking?" she had asked in alarm, fearing her adventure had been discovered.

"Of the remarkable man," was the reply. "His name is Herman."

Lisa made no reply.

"This Herman," continued Tomsky, "is a romantic character; he has the profile of a Napoleon and the heart of a Mephistopheles. It is said he has at least three crimes on his conscience. But how pale you are."

"It is only a slight headache. But why do you talk to me of this Herman?"

"Because I believe he has serious intentions concerning you."

"Where has he seen me?"

"At church, perhaps, or on the street."

The conversation was interrupted at this point, to the great regret of the young girl. The words of Tomsky made a deep impression upon her, and she realized how imprudently she had acted. She was thinking of all this and a great deal more when the door of her apartment suddenly opened, and Herman stood before her. She drew back at sight of him, trembling violently.

"Where have you been?" she asked in a frightened whisper.

"In the bedchamber of the Countess. She is dead," was the calm reply.

"My God! What are you saying?" cried the girl.

"Furthermore, I believe that I was the cause of her death."

The words of Tomsky flashed through Lisa's mind.

Mushroom Cloud Press | Classic Prose Collection

Herman sat down and told her all. She listened with a feeling of terror and disgust. So those passionate letters, that audacious pursuit were not the result of tenderness and love. It was money that he desired. The poor girl felt that she had in a sense been an accomplice in the death of her benefactress. She began to weep bitterly. Herman regarded her in silence.

"You are a monster!" exclaimed Lisa, drying her eyes.

"I didn't intend to kill her; the pistol was not even loaded.”

"How are you going to get out of the house?" inquired Lisa. "It is nearly daylight. I intended to show you the way to a secret staircase, while the Countess was asleep, as we would have to cross her chamber. Now I am afraid to do so."

"Direct me, and I will find the way alone," replied Herman.

She gave him minute instructions and a key with which to open the street door. The young man pressed the cold, inert hand, then went out.

The death of the Countess had surprised no one, as it had long been expected. Her funeral was attended by every one of note in the vicinity. Herman mingled with the throng without attracting any especial attention. After all the friends had taken their last look at the dead face, the young man approached the bier. He prostrated himself on the cold floor, and remained motionless for a long time. He rose at last with a face almost as pale as that of the corpse itself, and went up the steps to look into the casket. As he looked down it seemed to him that the rigid face returned his glance mockingly, closing one eye. He turned abruptly away, made a false step, and fell to the floor. He was picked up, and, at the same moment, Lisaveta was carried out in a faint.

Herman did not recover his usual composure during the entire day. He dined alone at an out-of-the-way restaurant, and drank a great deal, in the hope of stifling his emotion. The wine only served to stimulate his imagination. He returned home and threw himself down on his bed without undressing.

During the night he awoke with a start; the moon shone into his chamber, making everything plainly visible. Some one looked in at the window, then quickly disappeared. He paid no attention to this, but soon he heard the vestibule door open. He thought it was his orderly, returning late, drunk as usual. The step was an unfamiliar one, and he heard the shuffling sound of loose slippers.

The door of his room opened, and a woman in white entered. She came close to the bed, and the terrified man recognized the Countess.

"I have come to you against my will," she said abruptly; "but I was commanded to grant your request. The tray, seven, and ace in succession are the magic cards. Twenty-four hours must elapse between the use of each card, and after the three have been used you must never play again."

The fantom then turned and walked away. Herman heard the outside door close, and again saw the form pass the window.

Mushroom Cloud Press | Classic Prose Collection

He rose and went out into the hall, where his orderly lay asleep on the floor. The door was closed. Finding no trace of a visitor, he returned to his room, lit his candle, and wrote down what he had just heard.

Two fixed ideas cannot exist in the brain at the same time any more than two bodies can occupy the same point in space. The tray, seven, and ace soon chased away the thoughts of the dead woman, and all other thoughts from the brain of the young officer. All his ideas merged into a single one: how to turn to advantage the secret paid for so dearly. He even thought of resigning his commission and going to Paris to force a fortune from conquered fate. Chance rescued him from his embarrassment.

Tchekalinsky, a man who had passed his whole life at cards, opened a club at St. Petersburg. His long experience secured for him the confidence of his companions, and his hospitality and genial humor conciliated society.

The gilded youth flocked around him, neglecting society, preferring the charms of faro to those of their sweethearts. Naroumov invited Herman to accompany him to the club, and the young man accepted the invitation only too willingly.

The two officers found the apartments full. Generals and statesmen played whist; young men lounged on sofas, eating ices or smoking. In the principal salon stood a long table, at which about twenty men sat playing faro, the host of the establishment being the banker.

He was a man of about sixty, gray-haired and respectable. His ruddy face shone with genial humor; his eyes sparkled and a constant smile hovered around his lips.

Naroumov presented Herman. The host gave him a cordial handshake, begged him not to stand upon ceremony, and returned, to his dealing. More than thirty cards were already on the table. Tchekalinsky paused after each coup, to allow the punters time to recognize their gains or losses, politely answering all questions and constantly smiling.

After the deal was over, the cards were shuffled and the game began again.

"Permit me to choose a card," said Herman, stretching out his hand over the head of a portly gentleman, to reach a livret. The banker bowed without replying.

Herman chose a card, and wrote the amount of his stake upon it with a piece of chalk.

"How much is that?" asked the banker; "excuse me, sir, but I do not see well."

"Forty thousand rubles," said Herman coolly.

All eyes were instantly turned upon the speaker.

"He has lost his wits," thought Naroumov.

"Allow me to observe," said Tchekalinsky, with his eternal smile, "that your stake is excessive."

Mushroom Cloud Press | Classic Prose Collection

"What of it?" replied Herman, nettled. "Do you accept it or not?"

The banker nodded in assent. "I have only to remind you that the cash will be necessary; of course your word is good, but in order to keep the confidence of my patrons, I prefer the ready money."

Herman took a bank-check from his pocket and handed it to his host. The latter examined it attentively, then laid it on the card chosen.

He began dealing: to the right, a nine; to the left, a tray.

"The tray wins," said Herman, showing the card he held--a tray.

A murmur ran through the crowd. Tchekalinsky frowned for a second only, then his smile returned. He took a roll of bank-bills from his pocket and counted out the required sum. Herman received it and at once left the table.

The next evening saw him at the place again. Every one eyed him curiously, and Tchekalinsky greeted him cordially.

He selected his card and placed upon it his fresh stake. The banker began dealing: to the right, a nine; to the left, a seven.

Herman then showed his card--a seven spot. The onlookers exclaimed, and the host was visibly disturbed. He counted out ninety-four-thousand rubles and passed them to Herman, who accepted them without showing the least surprise, and at once withdrew.

The following evening he went again. His appearance was the signal for the cessation of all occupation, every one being eager to watch the developments of events. He selected his card--an ace.

The dealing began: to the right, a queen; to the left, an ace.

"The ace wins," remarked Herman, turning up his card without glancing at it.

"Your queen is killed," remarked Tchekalinsky quietly.

Herman trembled; looking down, he saw, not the ace he had selected, but the queen of spades. He could scarcely believe his eyes. It seemed impossible that he could have made such a mistake. As he stared at the card it seemed to him that the queen winked one eye at him mockingly.

"The old woman!" he exclaimed involuntarily.

The croupier raked in the money while he looked on in stupid terror. When he left the table, all made way for him to pass; the cards were shuffled, and the gambling went on.

Herman became a lunatic. He was confined at the hospital at Oboukov, where he spoke to no one, but kept constantly murmuring in a monotonous tone: "The tray, seven, ace! The tray, seven, queen!"
```

---

## IC-1950: Two Friends

- Title: Two Friends
- Author (byline): Guy de Maupassant
- Work: Classic Prose Collection
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2263
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
Besieged Paris was in the throes of famine. Even the sparrows on the roofs and the rats in the sewers were growing scarce. People were eating anything they could get. As Monsieur Morissot, watchmaker by profession and idler for the nonce, was strolling along the boulevard one bright January morning, his hands in his trousers pockets and stomach empty, he suddenly came face to face with an acquaintance-- Monsieur Sauvage, a fishing chum. Before the war broke out Morissot had been in the habit, every Sunday morning, of setting forth with a bamboo rod in his hand and a tin box on his back. He took the Argenteuil train, got out at Colombes, and walked thence to the Ile Marante. The moment he arrived at this place of his dreams he began fishing, and fished till nightfall. Every Sunday he met in this very spot Monsieur Sauvage, a stout, jolly, little man, a draper in the Rue Notre Dame de Lorette, and also an ardent fisherman. They often spent half the day side by side, rod in hand and feet dangling over the water, and a warm friendship had sprung up between the two. Some days they did not speak; at other times they chatted; but they understood each other perfectly without the aid of words, having similar tastes and feelings. In the spring, about ten o'clock in the morning, when the early sun caused a light mist to float on the water and gently warmed the backs of the two enthusiastic anglers, Morissot would occasionally remark to his neighbor: Mushroom Cloud Press | Classic Prose Collection

"My, but it's pleasant here."
To which the other would reply:
"I can't imagine anything better!"
And these few words sufficed to make them understand and appreciate each other.
In the autumn, toward the close of day, when the setting sun shed a blood-red glow
over the western sky, and the reflection of the crimson clouds tinged the whole
river with red, brought a glow to the faces of the two friends, and gilded the trees,
whose leaves were already turning at the first chill touch of winter, Monsieur
Sauvage would sometimes smile at Morissot, and say:
"What a glorious spectacle!"
And Morissot would answer, without taking his eyes from his float:
"This is much better than the boulevard, isn't it?"
As soon as they recognized each other they shook hands cordially, affected at the
thought of meeting under such changed circumstances.
Monsieur Sauvage, with a sigh, murmured:
"These are sad times!"
Morissot shook his head mournfully.
"And such weather! This is the first fine day of the year."
The sky was, in fact, of a bright, cloudless blue.
They walked along, side by side, reflective and sad.
"And to think of the fishing!" said Morissot. "What good times we used to have!"

Mushroom Cloud Press | Classic Prose Collection

"When shall we be able to fish again?" asked Monsieur Sauvage.
They entered a small cafe and took an absinthe together, then resumed their walk
along the pavement.
Morissot stopped suddenly.
"Shall we have another absinthe?" he said.
"If you like," agreed Monsieur Sauvage.
And they entered another wine shop.
They were quite unsteady when they came out, owing to the effect of the alcohol
on their empty stomachs. It was a fine, mild day, and a gentle breeze fanned their
faces.
The fresh air completed the effect of the alcohol on Monsieur Sauvage. He stopped
suddenly, saying:
"Suppose we go there?"
"Where?"
"Fishing."
"But where?"
"Why, to the old place. The French outposts are close to Colombes. I know
Colonel Dumoulin, and we shall easily get leave to pass."
Morissot trembled with desire.
"Very well. I agree."
And they separated, to fetch their rods and lines.

Mushroom Cloud Press | Classic Prose Collection

An hour later they were walking side by side on the-highroad. Presently they reached the villa occupied by the colonel. He smiled at their request, and granted it. They resumed their walk, furnished with a password. Soon they left the outposts behind them, made their way through deserted Colombes, and found themselves on the outskirts of the small vineyards which border the Seine. It was about eleven o'clock. Before them lay the village of Argenteuil, apparently lifeless. The heights of Orgement and Sannois dominated the landscape. The great plain, extending as far as Nanterre, was empty, quite empty-a waste of dun-colored soil and bare cherry trees. Monsieur Sauvage, pointing to the heights, murmured: "The Prussians are up yonder!" And the sight of the deserted country filled the two friends with vague misgivings. The Prussians! They had never seen them as yet, but they had felt their presence in the neighborhood of Paris for months past--ruining France, pillaging, massacring, starving them. And a kind of superstitious terror mingled with the hatred they already felt toward this unknown, victorious nation. "Suppose we were to meet any of them?" said Morissot. "We'd offer them some fish," replied Monsieur Sauvage, with that Parisian light-heartedness which nothing can wholly quench. Still, they hesitated to show themselves in the open country, overawed by the utter silence which reigned around them. At last Monsieur Sauvage said boldly: Mushroom Cloud Press | Classic Prose Collection

"Come, we'll make a start; only let us be careful!" And they made their way through one of the vineyards, bent double, creeping along beneath the cover afforded by the vines, with eye and ear alert. A strip of bare ground remained to be crossed before they could gain the river bank. They ran across this, and, as soon as they were at the water's edge, concealed themselves among the dry reeds. Morissot placed his ear to the ground, to ascertain, if possible, whether footsteps were coming their way. He heard nothing. They seemed to be utterly alone. Their confidence was restored, and they began to fish. Before them the deserted Ile Marante hid them from the farther shore. The little restaurant was closed, and looked as if it had been deserted for years. Monsieur Sauvage caught the first gudgeon, Monsieur Morissot the second, and almost every moment one or other raised his line with a little, glittering, silvery fish wriggling at the end; they were having excellent sport. They slipped their catch gently into a close-meshed bag lying at their feet; they were filled with joy--the joy of once more indulging in a pastime of which they had long been deprived. The sun poured its rays on their backs; they no longer heard anything or thought of anything. They ignored the rest of the world; they were fishing. But suddenly a rumbling sound, which seemed to come from the bowels of the earth, shook the ground beneath them: the cannon were resuming their thunder.

Mushroom Cloud Press | Classic Prose Collection

Morissot turned his head and could see toward the left, beyond the banks of the river, the formidable outline of Mont-Valerien, from whose summit arose a white puff of smoke. The next instant a second puff followed the first, and in a few moments a fresh detonation made the earth tremble. Others followed, and minute by minute the mountain gave forth its deadly breath and a white puff of smoke, which rose slowly into the peaceful heaven and floated above the summit of the cliff. Monsieur Sauvage shrugged his shoulders. "They are at it again!" he said. Morissot, who was anxiously watching his float bobbing up and down, was suddenly seized with the angry impatience of a peaceful man toward the madmen who were firing thus, and remarked indignantly: "What fools they are to kill one another like that!" "They're worse than animals," replied Monsieur Sauvage. And Morissot, who had just caught a bleak, declared: "And to think that it will be just the same so long as there are governments!" "The Republic would not have declared war," interposed Monsieur Sauvage. Morissot interrupted him: "Under a king we have foreign wars; under a republic we have civil war." And the two began placidly discussing political problems with the sound common sense of peaceful, matter-of-fact citizens--agreeing on one point: that they would Mushroom Cloud Press | Classic Prose Collection

never be free. And Mont-Valerien thundered ceaselessly, demolishing the houses of the French with its cannon balls, grinding lives of men to powder, destroying many a dream, many a cherished hope, many a prospective happiness; ruthlessly causing endless woe and suffering in the hearts of wives, of daughters, of mothers, in other lands. "Such is life!" declared Monsieur Sauvage. "Say, rather, such is death!" replied Morissot, laughing. But they suddenly trembled with alarm at the sound of footsteps behind them, and, turning round, they perceived close at hand four tall, bearded men, dressed after the manner of livery servants and wearing flat caps on their heads. They were covering the two anglers with their rifles. The rods slipped from their owners' grasp and floated away down the river. In the space of a few seconds they were seized, bound, thrown into a boat, and taken across to the Ile Marante. And behind the house they had thought deserted were about a score of German soldiers. A shaggy-looking giant, who was bestriding a chair and smoking a long clay pipe, addressed them in excellent French with the words: "Well, gentlemen, have you had good luck with your fishing?" Then a soldier deposited at the officer's feet the bag full of fish, which he had taken care to bring away. The Prussian smiled. "Not bad, I see. But we have something else to talk about. Listen to me, and don't be alarmed: Mushroom Cloud Press | Classic Prose Collection

"You must know that, in my eyes, you are two spies sent to reconnoitre me and my movements. Naturally, I capture you and I shoot you. You pretended to be fishing, the better to disguise your real errand. You have fallen into my hands, and must take the consequences. Such is war. "But as you came here through the outposts you must have a password for your return. Tell me that password and I will let you go." The two friends, pale as death, stood silently side by side, a slight fluttering of the hands alone betraying their emotion. "No one will ever know," continued the officer. "You will return peacefully to your homes, and the secret will disappear with you. If you refuse, it means death-instant death. Choose!" They stood motionless, and did not open their lips. The Prussian, perfectly calm, went on, with hand outstretched toward the river: "Just think that in five minutes you will be at the bottom of that water. In five minutes! You have relations, I presume?" Mont-Valerien still thundered. The two fishermen remained silent. The German turned and gave an order in his own language. Then he moved his chair a little way off, that he might not be so near the prisoners, and a dozen men stepped forward, rifle in hand, and took up a position, twenty paces off. "I give you one minute," said the officer; "not a second longer." Then he rose quickly, went over to the two Frenchmen, took Morissot by the arm, led him a short distance off, and said in a low voice: Mushroom Cloud Press | Classic Prose Collection

"Quick! the password! Your friend will know nothing. I will pretend to relent."
Morissot answered not a word.
Then the Prussian took Monsieur Sauvage aside in like manner, and made him the
same proposal.
Monsieur Sauvage made no reply.
Again they stood side by side.
The officer issued his orders; the soldiers raised their rifles.
Then by chance Morissot's eyes fell on the bag full of gudgeon lying in the grass a
few feet from him.
A ray of sunlight made the still quivering fish glisten like silver. And Morissot's
heart sank. Despite his efforts at self-control his eyes filled with tears.
"Good-by, Monsieur Sauvage," he faltered.
"Good-by, Monsieur Morissot," replied Sauvage.
They shook hands, trembling from head to foot with a dread beyond their mastery.
The officer cried:
"Fire!"
The twelve shots were as one.
Monsieur Sauvage fell forward instantaneously. Morissot, being the taller, swayed
slightly and fell across his friend with face turned skyward and blood oozing from
a rent in the breast of his coat.
The German issued fresh orders.

Mushroom Cloud Press | Classic Prose Collection

His men dispersed, and presently returned with ropes and large stones, which they attached to the feet of the two friends; then they carried them to the river bank. Mont-Valerien, its summit now enshrouded in smoke, still continued to thunder. Two soldiers took Morissot by the head and the feet; two others did the same with Sauvage. The bodies, swung lustily by strong hands, were cast to a distance, and, describing a curve, fell feet foremost into the stream. The water splashed high, foamed, eddied, then grew calm; tiny waves lapped the shore. A few streaks of blood flecked the surface of the river. The officer, calm throughout, remarked, with grim humor: "It's the fishes' turn now!" Then he retraced his way to the house. Suddenly he caught sight of the net full of gudgeons, lying forgotten in the grass. He picked it up, examined it, smiled, and called: "Wilhelm!" A white-aproned soldier responded to the summons, and the Prussian, tossing him the catch of the two murdered men, said: "Have these fish fried for me at once, while they are still alive; they'll make a tasty dish." Then he resumed his pipe.
```

---

## IC-1951: Why the Sea is Salt

- Title: Why the Sea is Salt
- Author (byline): George Webbe Dasent
- Work: Classic Prose Collection
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1850
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
Once on a time, but it was a long, long time ago, there were two brothers, one rich and one poor. Now, one Christmas eve, the poor one hadn't so much as a crumb in the house, either of meat or bread, so he went to his brother to ask him for something to keep Christmas with, in God's name. It was not the first time his brother had been forced to help him, and you may fancy he wasn't very glad to see his face, but he said:

"If you will do what I ask you to do, I'll give you a whole flitch of bacon."

So the poor brother said he would do anything and was full of thanks.

"Well, here is the flitch," said the rich brother, "and now go straight to Hell."

"What I have given my word to do, I must stick to," said the other; so he took the flitch and set off. He walked the whole day, and at dusk he came to a place where he saw a very bright light.

"Maybe this is the place," said the man to himself. So he turned aside, and the first thing he saw was an old, old man, with a long white beard, who stood in an outhouse, hewing wood for the Christmas fire.

"Good even," said the man with the flitch.

"The same to you; whither are you going so late?" said the man.

"Oh! I'm going to Hell, if I only knew the right way," answered the poor man.

"Well, you're not far wrong, for this is Hell," said the old man; "when you get inside they will be all for buying your flitch, for meat is scarce in Hell; but, mind you don't sell it unless you get the hand-mill which stands behind the door for it. When you come out, I'll teach you how to handle the mill, for it's good to grind almost anything."

So the man with the flitch thanked the other for his good advice, and gave a great knock at the Devil's door.

When he got in, everything was just as the old man had said. All the devils, great and small, came swarming up to him like ants round an anthill, and each tried to outbid the other for the flitch.

"Well!" said the man, "by rights, my old dame and I ought to have this flitch for our Christmas dinner; but since you have all set your hearts on it, I suppose I must give it up to you; but if I sell it at all, I'll have for it the mill behind the door yonder."

At first the Devil wouldn't hear of such a bargain, and chaffed and haggled with the man; but he stuck to what he said, and at last the Devil had to part with his mill. When the man got out into the yard, he asked the old woodcutter how he was to handle the mill; and after he had learned how to Mushroom Cloud Press | Classic Prose Collection

use it, he thanked the old man and went off home as fast as he could, but still the clock had struck twelve on Christmas eve before he reached his own door.

"Wherever in the world have you been?" said his old dame; "here have I sat hour after hour waiting and watching, without so much as two sticks to lay together under the Christmas brose."

"Oh!" said the man, "I couldn't get back before, for I had to go a long way first for one thing, and then for another; but now you shall see what you shall see."

So he put the mill on the table, and bade it first of all grind lights, then a table-cloth, then meat, then ale, and so on till they had got everything that was nice for Christmas fare. He had only to speak the word, and the mill ground out what he wanted. The old dame stood by blessing her stars, and kept on asking where he had got this wonderful mill, but he wouldn't tell her.

"It's all one where I got it from; you see the mill is a good one, and the mill-stream never freezes, that's enough."

So he ground meat and drink and dainties enough to last out till Twelfth Day, and on the third day he asked all his friends and kin to his house, and gave a great feast. Now, when his rich brother saw all that was on the table, and all that was behind in the larder, he grew quite spiteful and wild, for he couldn't bear that his brother should have anything.

"Twas only on Christmas eve," he said to the rest, "he was in such straits that he came and asked for a morsel of food in God's name, and now he gives a feast as if he were count or king;" and he turned to his brother and said:

"But whence, in Hell's name, have you got all this wealth?"

"From behind the door," answered the owner of the mill, for he didn't care to let the cat out of the bag. But later on in the evening, when he had got a drop too much, he could keep his secret no longer, and brought out the mill and said:

"There, you see what has gotten me all this wealth;" and so he made the mill grind all kind of things. When his brother saw it, he set his heart on having the mill, and, after a deal of coaxing, he got it; but he had to pay three hundred dollars for it, and his brother bargained to keep it till hay-harvest, for he thought, if I keep it till then, I can make it grind meat and drink that will last for years. So you may fancy the mill didn't grow rusty for want of work, and when hay-harvest came, the rich brother got it, but the other took care not to teach him how to handle it.

It was evening when the rich brother got the mill home, and the next morning he told his wife to go out into the hay-field and toss, while the mowers cut the grass, and he would stay at home and get the dinner ready. So, when dinner-time drew near, he put the mill on the kitchen table and said:

"Grind herrings and broth, and grind them good and fast."

Mushroom Cloud Press | Classic Prose Collection

So the mill began to grind herrings and broth; first of all, all the dishes full, then all the tubs full, and so on till the kitchen floor was quite covered. Then the man twisted and twirled at the mill to get it to stop, but for all his twisting and fingering the mill went on grinding, and in a little while the broth rose so high that the man was like to drown. So he threw open the kitchen door and ran into the parlour, but it wasn't long before the mill had ground the parlour full too, and it was only at the risk of his life that the man could get hold of the latch of the house door through the stream of broth. When he got the door open, he ran out and set off down the road, with the stream of herrings and broth at his heels, roaring like a waterfall over the whole farm.

Now, his old dame, who was in the field tossing hay, thought it a long time to dinner, and at last she said:

"Well! though the master doesn't call us home, we may as well go. Maybe he finds it hard work to boil the broth, and will be glad of my help."

The men were willing enough, so they sauntered homeward; but just as they had got a little way up the hill, what should they meet but herrings, and broth, and bread, all running and dashing, and splashing together in a stream, and the master himself running before them for his life, and as he passed them he bawled out: "Would to heaven each of you had a hundred throats! but take care you're not drowned in the broth."

Away he went, as though the Evil One were at his heels, to his brother's house, and begged him for God's sake to take back the mill that instant; for, said he:

"If it grinds only one hour more, the whole parish will be swallowed up by herrings and broth."

But his brother wouldn't hear of taking it back till the other paid him down three hundred dollars more.

So the poor brother got both the money and the mill, and it wasn't long before he set up a farmhouse far finer than the one in which his brother lived, and with the mill he ground so much gold that he covered it with plates of gold; and as the farm lay by the sea-side, the golden house gleamed and glistened far away over the sea. All who sailed by, put ashore to see the rich man in the golden house, and to see the wonderful mill, the fame of which spread far and wide, till there was nobody who hadn't heard tell of it.

So one day there came a skipper who wanted to see the mill; and the first thing he asked was if it could grind salt.

"Grind salt!" said the owner; "I should just think it could. It can grind anything."

When the skipper heard that, he said he must have the mill, cost what it would; for if he only had it, he thought he should be rid of his long voyages across stormy seas for a lading of salt. Well, at first the man wouldn't hear of parting with the mill; but the skipper begged and prayed so hard that at last he let him have it, but he had to pay many, many thousand dollars for it. Now, when the skipper had got the mill on his back, he soon made off with it, for he was afraid lest the man should Mushroom Cloud Press | Classic Prose Collection

change his mind; so he had no time to ask how to handle the mill, but got on board his ship as fast as he could, and set sail. When he had sailed a good way off, he brought the mill on deck and said:

"Grind salt, and grind both good and fast."

Well, the mill began to grind salt so that it poured out like water; and when the skipper had got the ship full, he wished to stop the mill, but whichever way he turned it, and however much he tried, it was no good; the mill kept grinding on, and the heap of salt grew higher and higher, and at last down sunk the ship.

There lies the mill at the bottom of the sea, and grinds away at this very day, and that's why the sea is salt.
```

---

## IC-1952: 1 Dead in Attic

- Title: 1 Dead in Attic
- Author (byline): Chris Rose
- Work: Not specified
- Publisher: CR Books
- Publication date as stated: Feb 2006
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1350
- Already set (do not supply): none

### Source block (context only)

```text
Author: Chris Rose
ISBN: 978-0977771509
Publisher: CR Books
Date (Month/Year): Feb 2006
```

### Introduction (context only: never use it for content warnings)

```text
The impact of Hurricane Katrina on New Orleans in 2005 was shattering and long-lasting. Winds were in the Category 3 range with frequent intense gusts and tidal surges. New Orleans was devastated -- By August 31, 2005, eighty percent of New Orleans lay under 15 feet of water. The good news? 90% of the residents of southeast Louisiana were evacuated to safety in the most successful evacuation of a major urban area in the nation's history.

Despite this, many remained (mainly the elderly and poor). According to the Louisiana Department of Health, the official death toll, was 1,464. But body collection couldn’t begin until September 9. Prior to that date, the locations of corpses were recorded, but most were not retrieved. Like ghosts populating an abandoned city, haunting messages and mystical artifacts adorned the homes of neighborhoods struggling to come back from the dead.

1 Dead in Attic by Chris Rose
```

### Performance text (classify this)

```text
I live on The Island, where much has the appearance of Life Goes On. Gas stations, bars, pizza joints, joggers, strollers, dogs, churches, shoppers, neighbors, even garage sales.

Sometimes trash and mail service, sometimes not.

It sets to mind a modicum of complacency that maybe everything is all right. But I have this terrible habit of getting into my car every two or three days and driving into the Valley Down Below, that vast wasteland below sea level that was my city, and it's mind-blowing A) how vast it is and B) how wasted it is.

My wife questions the wisdom of my frequent forays into the massive expanse of blown-apart lives and property that local street maps used to call Gentilly, Lakeview, the East, and the Lower 9th. She fears that it contributes to my unhappiness and general instability, and I suspect she is right.

Perhaps I should just stay on the stretch of safe, dry land Uptown where we live and try to move on, focus on pleasant things, quit making myself miserable, quit reliving all those terrible things we saw on TV that first week.

That's advice I wish I could follow, but I can't. I am compelled for reasons that are not entirely clear to me. And so, I drive.

I drive around and try to figure out those Byzantine markings and symbols that the cops and the National Guard spray-painted on all the houses around here, cryptic communications that tell the story of who or what was or wasn't inside the house when the floodwater rose to the ceiling.

In some cases, there's no interpretation needed. There's one I pass on St. Roch Avenue in the 8th Ward at least once a week. It says: "1 dead in attic."

That certainly sums up the situation. No mystery there.

It's spray-painted there on the front of the house, and it probably will remain spray-painted there for weeks, months, maybe years, a perpetual reminder of the untimely passing of a citizen, a resident, a New Orleanian.

One of us.

You'd think some numerical coding could have conveyed this information on this house, so that I -- we all - - wouldn't have to drive by places like this every day and be reminded: "1 dead in attic."

I have seen plenty of houses in worse shape than the one where 1 Dead in Attic used to live, houses in Gentilly and the Lower 9th that yield the most chilling visual displays in town: low-rider shotgun rooftops with holes that were hacked away from the inside with an ax, leaving small, splintered openings through which people sought escape.

Imagine if your life came to that point, and remained there, on display, all over town for us to see, day after day.

Amazingly, those rooftops are the stories with happy endings. I mean, they got out, right?

But where are they now? Do you think they have trouble sleeping at night?

The occasional rooftops still have painted messages: "HELP US." I guess they had paint cans in their attic. And an ax, like Margaret Orr and Aaron Broussard always told us we should have if we weren't going to evacuate.

Some people thought Orr and Broussard were crazy. Alarmists. Extremists. Well, maybe they are crazy. But they were right.

Perhaps 1 Dead in Attic should have heeded this advice. But judging from the ages on the state's official victims list, he or she was probably up in years. And stubborn. And unafraid. And now a statistic. I wonder who eventually came and took 1 Dead in Attic away. Who knows? Hell, with the way things run around here -- I wonder if anyone has come to take 1 Dead in Attic away.

And who claimed him or her? Who grieved over 1 Dead in Attic and who buried 1 Dead in Attic?

Was there anyone with him or her at the end and what was the last thing they said to each other? How did 1 Dead in Attic spend the last weekend in August of the year 2005?

What were their plans? Maybe dinner at Mandich on St. Claude? Maybe a Labor Day family reunion in City Park -- one of those raucous picnics where everybody wears matching T-shirts to mark the occasion and they rent a DJ and a SpaceWalk and a couple of guys actually get there the night before to secure a good, shady spot?

I wonder if I ever met 1 Dead in Attic. Maybe in the course of my job or maybe at a Saints game or maybe we once stood next to each other at a Mardi Gras parade or maybe we once flipped each other off in a traffic jam.

1 Dead in Attic could have been my mail carrier, a waitress at my favorite restaurant or the guy who burglarized my house a couple years ago. Who knows?

My wife, she's right. I've got to quit just randomly driving around. This can't be helping anything.

But I can't stop. I return to the Valley Down Below over and over, looking for signs of progress in all that muck, some sign that things are getting better, that things are improving, that we don't all have to live in a state of abeyance forever but -- you know what?

I just don't see them there.

I mean, in the 8th Ward, tucked down there behind St. Roch Cemetery, life looks pretty much like it did when the floodwater first receded 10 weeks ago, with lots of cars pointing this way and that, kids' yard toys caked in mire, portraits of despair, desolation and loss. And hatchet holes in rooftops.

But there's something I've discovered about the 8th Ward in this strange exercise of mine: Apparently, a lot of Mardi Gras Indians are from there. Or were from there; I'm not sure what the proper terminology is.

On several desolate streets that I drive down, I see where some folks have returned to a few of the homes and they haven't bothered to put their furniture and appliances out on the curb -- what's the point, really? -- but they have retrieved their tattered and muddy Indian suits and sequins and feathers, and they have nailed them to the fronts of their houses.

The colors of these displays are startling because everything else in the 8th is gray. The streets, the walls, the cars, even the trees. Just gray.

So the oranges and blues and greens of the Indian costumes are something beautiful to behold, like the first flowers to bloom after the fallout. I don't know what the significance of these displays is, but they hold a mystical fascination for me.

They haunt me, almost as much as the spray paint on the front of a house that says 1 Dead in Attic. They look like ghosts hanging there. They are reminders of something. Something very New Orleans.

Do these memorials mean these guys -- the Indians - - are coming back? I mean, they have to, don't they? Where else could they do what they do?

And -- maybe this is a strange time to ask -- but who are these guys, anyway? Why do they do what they do with all those feathers and beads that take so much time and money to make? What's with all the Big Chief and Spy Boy role-playing?

As many times as I have reveled in their rhythmic, poetic and sometimes borderline absurd revelry in the streets of our city, I now realize that if you asked me to explain the origins and meaning of the Mardi Gras Indians -- I couldn't do it. I have no clue. And that makes me wish I'd been paying more attention for the past 20 years. I could have learned something.

I could have learned something about a people whose history is now but a sepia mist over back-of-town streets and neighborhoods that nobody's ever heard of and where nobody lives and nothing ever happens anymore; a freeze frame still life in the air, a story of what we once were.
```

---

## IC-1953: 2BR02B Pronounced To Be or Naught To Be

- Title: 2BR02B Pronounced To Be or Naught To Be
- Author (byline): Kurt Vonnegut
- Work: Bagombo Snuff Box
- Publisher: Berkley Publishing Group
- Publication date as stated: August 2000
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, ORDERLY, PAINTER, LEORA, DR. HITZ, WEHLING, HOSTESS ON THE PHONE, HOSTESS
- Teaser before the introduction: Yes
- Spoken words (computed): 1668
- Already set (do not supply): none

### Source block (context only)

```text
Author: Kurt Vonnegut
Book: Bagombo Snuff Box
ISBN: 978-0425174463
Publisher: Berkley Publishing Group
Date (Month/Year): August 2000
```

### Introduction (context only: never use it for content warnings)

```text
The future Kurt Vonnegut describes sounds amazing, doesn’t it. But unfortunately, it hinges on a concept that most people rarely consider: Population control. In 1979 the Chinese government implemented a policy to control its population: 1 child per family. Families meeting this expectation received numerous economic incentives. It worked so well that the birth rate declined rapidly, and the restrictions were relaxed in May of 2021 to allow women to bear up to three children.

Kurt Vonnegut in his story 2BR02B imagines a future for the United States that institutes a different version of population control.
```

### Performance text (classify this)

```text
NARRATOR: Everything was perfectly swell. There were no prisons, no slums, no insane asylums, no [disabilities], no wars. All diseases were conquered. So was old age. Death, barring accidents, was an adventure for volunteers. The population of the United States was stabilized at forty million souls.

NARRATOR: One bright morning at the Chicago Lying-In Hospital, a man named Edward K. Wehling, Jr., waited for his wife to give birth. He was the only man waiting. Not many people were born each day anymore. Wehling was fifty-six, a mere stripling in a population whose average age was one hundred twenty-nine. X rays had revealed that his wife was going to have triplets. The children would be his first.

Young Wehling was hunched in his chair, his head in his hand. He was so rumpled, so still and colorless as to be virtually invisible. His camouflage was perfect, since the waiting room had a disorderly and demoralized air, too. Chairs and ashtrays had been moved away from the walls. The floor was paved with spattered drop cloths. The room was being redecorated. It was being redecorated as a memorial to a man who had volunteered to die.

A sardonic old man, about two hundred years old, sat on a stepladder, painting a mural he did not like. Back in the days when people aged visibly, his age would have been guessed at thirty-five or so. Aging had touched him that much before the cure for aging was found. The mural he was working on depicted a very neat garden. Men and women in white, doctors and nurses, turned the soil, planted seedlings, sprayed bugs. Men and women in purple uniforms pulled up weeds, cut down plants that were old and sickly and carried refuse to trash burners. A hospital orderly came down the corridor . . .

ORDERLY: (singing under his breath a popular song. He stops to look at the mural) Looks so real. I can practically imagine I'm standing in the middle of it.

PAINTER: What makes you think you're not in it? (smiling) It's called The Happy Garden of Life, you know.

ORDERLY: That’s good of Dr. Hitz. . .

NARRATOR: Dr. Benjaminm Hitz, the hospital’s Chief Obstetrician.

ORDERLY: Lots of faces still to fill in.

NARRATOR: He meant that the faces of many of the figures in the mural were blank. All blanks were to be filled with the portraits of important people either on the hospital staff or from the Chicago office of the Federal Bureau of Termination.

ORDERLY: Must be nice to be able to make pictures that look like something.

PAINTER: (with a scornful look) You think I'm proud of this? You think this is my idea of what life really looks like?

ORDERLY: You're a gloomy old duck, aren't you?

PAINTER: Is that a crime?

ORDERLY: If you don't like it here, Grandpa . . . 2BR02B

NARRATOR: 2BR02B -- The trick telephone number that people who didn't want to live anymore were supposed to call. "To Be or Not to Be" was the telephone number of the municipal gas chambers of the Federal Bureau of Termination. [Also called]: The Automat; The Happy Hooligan; and Why Worry?

PAINTER: (with derision) When I decide it's time to go, it won't be at the Automat.

ORDERLY: A do-it-yourselfer, eh? Messy business, Grandpa. Why don't you have a little consideration for the people who have to clean up after you?

PAINTER: The world could do with a good deal more mess, if you ask me.

NARRATOR: A coarse, formidable woman strode into the waiting room on spike heels. Her shoes, stockings, trench coat, bag, and overseas cap were all purple, a purple the painter called "the color of grapes on Judgement Day." The medallion on her purple bag was the seal of the Service Division of the Federal Bureau of Termination, an eagle perched on a turnstile. The woman had a lot of facial hair--an unmistakable mustache, in fact. A curious thing about gas chamber hostesses was that no matter how lovely and feminine they were when recruited, they all sprouted mustaches within five years or so.

LEORA: They told me I was supposed to pose for some picture. My name's Leora Duncan. (pause as she admires the painting) That sure is a beautiful picture. Looks just like heaven or something.

PAINTER: Or something. (taking a list of names from his pocket) Duncan, Duncan, Duncan. (scanning the list) Yes--here you are. You're entitled to be immortalized. See any faceless body here you'd like me to stick your head on? We've got a few choice ones left. As a master of the fine arts I recommend this body here.

(pointing to a figure)

LEORA: Well, that's more the disposal people, isn't it? I mean, I'm in service. I don't do any disposing.

PAINTER: (in mock delight) You say you don't know anything about art, and then you prove in the next breath that you do know more about it than I do!

(pointing to another faceless figure) How about her?

LEORA: Gosh—(blushing and humble) That--that puts me right next to Dr. Hitz. It's--it's just such an honor. He was responsible for setting up the very first gas chamber in Chicago.

PAINTER: Nothing would please me more than to put you next to him for all time. Sawing off a limb – that strikes you as appropriate?

LEORA: That is kind of like what I do.

NARRATOR: She was demure about what she did. What she did was make people comfortable while she killed them. And while Leora Duncan was posing for her portrait, into the waiting room bounded Dr. Hitz himself. He was seven feet tall, and he boomed with importance, accomplishments, and the joy of living.

DR. HITZ: Well, Miss Duncan! Miss Duncan! (joking) What are you doing here? This isn't where the people leave. This is where they come in!

LEORA: (Shyly) We're going to be in the same picture together.

DR. HITZ: I'm honored to be in it with you. Without women like you, this wonderful world we've got wouldn't be possible. (Salutes and moves off) Guess what was just born? Triplets!

LEORA: (aghast) Triplets!

NARRATOR: She was exclaiming over the legal implications of triplets. The law said that no newborn child could survive unless the parents of the child could find someone who would volunteer to die. Triplets, if they were all to live, called for three volunteers.

LEORA: Do the parents have three volunteers?

DR. HITZ: Last I heard, they had one, and were trying to scrape another two up.

LEORA: I don't think they made it. Nobody made three appointments with us. Nothing but singles going through today, unless somebody called in after I left. What's the name?

WEHLING: (perking up, red-eyed and frowzy, he raises his hand) Wehling -- Edward. K. Wehling, Jr., is the name of the happy father-to-be.

DR. HITZ: Oh, Mr. Wehling, I didn't see you. They just phoned me that your triplets have been born. They're all fine and so is the mother. I'm on my way in to see them now.

WEHLING: (emptily) Hooray.

DR. HITZ: You don't sound very happy.

WEHLING: What man in my shoes wouldn't be happy? All I have to do is pick out which one of the triplets is going to live, then deliver my maternal grandfather to the Happy Hooligan, and come back here with a receipt.

DR. HITZ: (severely) You don't believe in population control, Mr. Wehling? Would you like to back to the good old days, when the population of the earth was twenty billion--about to become forty billion, then eighty billion, then one hundred and sixty billion? (pause) Do you know what a drupelet is, Mr. Wehling? A drupelet, Mr. Wehling, is one of the little knobs, one of the little pulpy grains, of a blackberry. Without population control, human beings would now be packed on the surface of this old planet like drupelets on a blackberry! Think of it! In the year 2000, before scientists stepped in and laid down the law, there wasn't even enough drinking water to go around, and nothing to eat but seaweed -- and yet still people insisted on their right to reproduce like jackrabbits. And their right, if possible, to live forever.

WEHLING: I want those kids. I want all three of them. I don't want my grandfather to die, either.

DR. HITZ: (sympathetically) Nobody's really happy about taking a close relative to the Automat.

LEORA: I wish people wouldn't call it that. It gives people the wrong impression.

DR. HITZ: You're absolutely right. Forgive me. I should have said `Ethical Suicide Studios. (to Wehling) This child of yours--whichever one you decide to keep, Mr. Wehling. He or she is going to live on a happy, roomy, clean, rich planet, thanks to population control. In a garden like that mural there. (shaking his head) Two centuries ago, when I was a young man, it was a hell that nobody thought could last another twenty years.

Now centuries of peace and plenty stretch before us as far as the imagination cares to travel.

WEHLING: (Drawing a revolver – he shoots Dr. Hitz) There's room for one--a great big one. (He shoots Leora) It's only death. There! Room for two. (He puts the gun to his own head and fires)

NARRATOR: And then he shot himself, making room for all three of his children. Nobody came running. Nobody, it seemed, had heard the shots. The painter sat on the top of his stepladder, looking down reflectively on the sorry scene. [He] pondered the mournful puzzle of life demanding to be born and, once born, demanding to be fruitful ... to multiply and to live as long as possible--to do all that on a very small planet that would have to last forever.

All the answers that the painter could think of were grim. He thought of war. He thought of plague. He thought of starvation. He knew that he would never paint again. He let his paint brush fall to the drop cloths below. And then he decided he had had about enough of the Happy Garden of Life, too, and he came slowly down from the ladder. He took Wehling’s pistol, really intending to shoot himself. But he didn’t have the nerve. And then he saw the telephone booth in the corner of the room. He went to it, dialed the well-remembered number: 2BR02B.

HOSTESS ON THE PHONE: (warmly) Federal Bureau of Termination.

PAINTER: How soon could I get an appointment?

HOSTESS: We could probably fit you in late this afternoon, sir. It might be even earlier, if we get a cancellation.

PAINTER: All right. Fit me in, if you please.

NARRATOR: And he gave her his name, spelling it out.

HOSTESS: Thank you, sir. Your city thanks you, your country thanks you, your planet thanks you. But the greatest thanks of all is from future generations.
```

---

## IC-1954: 7 Variations on Margarita Weinberg

- Title: 7 Variations on Margarita Weinberg
- Author (byline): Moises Kaufman
- Work: A Memory, A Monologue, A Rant and A Prayer
- Publisher: Random House
- Publication date as stated: May 2007
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, WOMAN, COSSACK LEADER, GRANDMOTHER, BORIS, MARGARITA, SIMON
- Teaser before the introduction: Yes
- Spoken words (computed): 1677
- Already set (do not supply): none

### Source block (context only)

```text
Author: Moises Kaufman
Book: A Memory, A Monologue, A Rant and A Prayer
ISBN: 978-0345497918
Publisher: Random House
Date (Month/Year): May 2007
```

### Introduction (context only: never use it for content warnings)

```text
Moises Kaufman, acclaimed playwright known for his play The Laramie Project based on extensive interviews with people who were involved with the aftermath of the murder of gay student Matthew Shepard, turns the author’s magnifying glass on his own family.

He addresses his grandmother’s concept of heroic suicide -- “the road not taken. . . the life not lived” and the alternative -- compromises people make to survive. In 2005 he described himself in an interview by saying, “I am Venezuelan, I am Jewish, I am gay. I am the sum of all my cultures. I couldn’t write anything that didn’t incorporate all that I am.”

7 Variations on Margarita Weinberg by Moises Kaufman
```

### Performance text (classify this)

```text
NARRATOR: My grandmother was born in the Ukraine but immigrated to Venezuela before the Second World War. She told me this story: A young Jewish woman was kidnapped by a group of Cossacks during a pogrom. They brought her into a room and held her down, deciding who would have her first.

WOMAN: If you touch me, I will put a curse on you. I am a witch.

NARRATOR: The Cossacks laughed.

WOMAN: (shouting) I can prove it! I can prove to you that I’m a witch.

COSSACK LEADER: (smiling) Very well. Prove it, then.

WOMAN: I am immortal, and you cannot kill me. Not even if you shoot me. Try it. (pointing to her chest) Here. Shoot me in the heart. You will see I won’t die. And then you’ll have your proof that I’m a witch.

NARRATOR: The leader thought for a moment, then quickly took out his pistol and shot her in the heart. The young woman fell to the floor bleeding, looked at the man who had shot her, and said,

WOMAN: Thank you, you imbecile.

NARRATOR: My grandmother liked stories of heroic suicides.

NARRATOR: My grandmother was the storyteller in the family. In some arrangement made long before I was born, she had inherited the responsibility of keeping our narratives and our history alive for us.

GRANDMOTHER: My brother was a Communist who left our village in the Ukraine and went to Paris to join the Resistance fighters against the Nazis. He became one of their best spies. A street in Paris is named after him.

NARRATOR: Two years after he joined the Resistance, he was surprised on a mission inside a German arsenal in a suburb of Paris.

GRANDMOTHER: When the Nazis surrounded the arsenal, he used all the weapons in it to defend himself. He killed many Nazis that day . . . He saved the last bullet for himself.

NARRATOR: Heroic suicides . . . I grew up with these narratives. (pause) My grandmother wanted to be a doctor when she was young. But in the Ukraine in 1935, there were only a few seats at the university allotted to Jews, and all of them went to men. So she became a nurse.

When she told her family in 1937 that she wanted to go to Venezuela, everyone was against it. They hardly knew where Venezuela was on the map. But her fiancé, Boris (my grandfather), had moved here two years earlier to make his fortune, and he wanted her to come join him; business was going well for him and he was worried about rumors of a war in Europe.

I don’t know if it was the imminent war or the invitation of a lover in the tropics, or both, but she came here. She was twenty-two years old. The story goes that when she arrived in Caracas, she was a woman of such delicate beauty, every immigrant wanted to marry her. (I’ve seen pictures, and she was stunning.) And my grandfather said

BORIS: Although I brought you here, you have no obligation to marry me. We’ve been apart for two years, and your feelings might have changed. You can have your pick of any man in our community.

NARRATOR: My grandmother cried, moved by his words, and told him that her decision was to marry him.

When their first child was born, my grandmother named her Margarita, which is the name of Venezuela’s national flower. Margarita Weinberg.

My mother’s childhood in Venezuela was idyllic. The country was blessed with warm weather and kind inhabitants who were welcoming to the immigrants. The war was an ocean away, and my mother heard about it only when my grandparents would talk in hushed tones about relatives who had stayed behind and were now either in concentration camps or dead.

(pause) At nineteen my mother, Margarita, met a young man named Simon, who’d arrived in Venezuela after the war, from Romania. He’d survived the war by sewing and selling the yellow Stars of David that the Jews were made to wear. He spent most of the war alternately hiding in a small room and selling Stars of David. He was eleven.

[Simon and my mother] went out on a few dates, and then he asked her to marry him. She liked him, but her intuition told her she shouldn’t marry him—he came from such a different life. She had never known hunger or war, except in the heroic and suicidal stories of her mother. But my grandfather Boris said,

BORIS: Do you think there’s a line of men waiting for you? We are a small Jewish community here. He’s a good man. You should marry him.

NARRATOR: My grandmother heard this but said nothing. And my mother married him. Her strongest memory of her wedding day is standing under the canopy in the synagogue thinking

MARGARITA: What am I doing here? This feels like suicide.

NARRATOR: Their marriage was a disaster. My mother’s intuition about Simon, my father, was absolutely correct. They were from two different worlds.

My father’s Eastern European upbringing, already stern and strict, had then been further hardened by the war. He was despotic and had little patience for things other than survival. His main interests were making a living, having children, and attending synagogue. My mother loved American movies and Venezuelan ballads and porcelain dolls. He was punctual and Germanic in his daily habits. She had the punctuality of people in the tropics and their laid-back attitude. He perceived her as spoiled and lazy. And his inability to understand her quickly turned to fury.

For her part, she often thought herself superior to him. The war had left deep scars: His manners were lacking or nonexistent; he laughed too loudly, spoke broken Spanish, and ate voraciously. (He told me he had been hungry for so long that he thought one could never have enough food to be satiated.)

Every Friday night there would be a Sabbath dinner at our house. My clearest memory of those dinners was my father’s bright red face and the swollen veins in his neck as he yelled accusations.

SIMON: The Sabbath candles were not lit at the right time! You don’t care about the Sabbath! What kind of a mother are you? This food is terrible! You don’t know how to cook! The children are too loud, what have you taught them?

NARRATOR: Each attack was louder than the last: the shouting, the insults. And yet every time my mother tried to answer him, my grandfather would say,

BORIS: Margarita, let it be. Shoin.

NARRATOR: (“Enough” in Yiddish.) And he wouldn’t let her respond. If my mother tried again, he would again say “Shoin,” and silence her. Perhaps he thought this the best way to diffuse the argument, perhaps he himself was afraid of my father, perhaps he felt pity for him. Whatever the reason, my mother was always the one encouraged to silence.

BORIS: Let him have his way. Who cares?

NARRATOR: But the most striking thing to me, even as a young boy, was that my grandmother would watch and listen and never say a word. Margarita was being savagely attacked by my father and silenced by my grandfather and my grandmother said nothing—not a word.

I thought my grandmother was heroic. She had to be, to cross the Atlantic, to settle in a small Latin American village without knowing the language, to raise three children in this new land, and to bear the responsibility of keeping our narratives alive. But what good are narratives if they lead to suicide?

How could she stand by and watch her daughter be assaulted and do nothing? Did she think the harassment would end? Did she not realize that my mother needed her mother to defend her?

My mother thought of suicide many times. But she had three children. That’s the trouble with heroic stories . . .

My grandmother passed away seven years ago, and since then another tacit agreement has made me the writer in the family, the keeper of our stories. Members of my family come to me to ask about the past. And so in writing this story I call my mother to make sure I’ve gotten it right. And I take the opportunity to ask her about these events.

“Did you ever ask your mother why she didn’t defend you?”

MARGARITA: I was an adult. I had three children. It was not for her to defend me. And I think you have part of the story wrong.

NARRATOR: She tells me a different version of my grandmother’s arrival in Venezuela, one she heard from her aunt.

In this version, after my grandfather left the Ukraine to come to Venezuela, my grandmother fell madly in love with a revolutionary Communist. Her father forbade the affair, and the Communist lover, brokenhearted, went to Spain to fight in the civil war. There he was killed in battle. Her father, keenly aware of the imminent war in Europe, forced my grandmother to go to Venezuela and marry my grandfather.

If this version is true, my grandmother’s heroic tales served a deeper purpose than I had originally imagined. They weren’t a code of conduct, or a commitment to revolt; they were simply the longings of an adolescent Ukrainian girl living in the tropics.

Heroic actions that she could fantasize about but never act upon.

The real lesson she had learned from her father was: Compromise to survive.

The heroine in my grandmother’s pogrom story might have survived had she compromised. Her brother would have been captured and maybe even lived a few more years had he not used the bullet on himself. But they decided against it. These stories were the road not taken. The life not lived. And hence she could dream them, but she could not really teach her daughter how to act on them.

Suicide was good in fiction. Not good in reality. In reality, silence and obedience seemed to secure survival. And heroism was a virtue to admire in a novel or a trans-Atlantic journey. But not a recipe for life . . .

My mother eventually divorced my father, then married him again and divorced him again. That was ten years ago.

MARGARITA: I’m glad you’re writing this down. It certainly doesn’t have the flair of your grandmother stories. (smiling) It took me a long time and many rewrites, but I finally left your father. And I’m satisfied with that outcome (long pause) and that it didn’t end in suicide.
```

---

## IC-1955: Adolf Hitler: The Larry King Interview

- Title: Adolf Hitler: The Larry King Interview
- Author (byline): Jon Stewart
- Work: Naked Pictures of Famous People (Pg 139-150)
- Publisher: Harper Collins
- Publication date as stated: Oct 1999
- Event as filed: Prose
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

HITLER: Not much. I fully expect that by this time next year, I'll have been convicted and possibly put to death. I'm going to represent myself, though. From now on the blame goes here (pointing to chest). The only one to blame for Hitler . . . is Hitler. Besides, who wants to get involved with a bunch of phony-baloney defense lawyers. . . I mean, talk about evil. (Both laugh.)

KING: Well, Adolf, thanks for coming by.

HITLER: Thank you. CLOSING

KING: Stay tuned next week when we get up close and personal with another “man-about-town” -- Former President Donald Trump! (Larry King Live Music*)
```

---

## IC-1956: After I Was Thrown in the River and Before I Drowned

- Title: After I Was Thrown in the River and Before I Drowned
- Author (byline): Dave Eggers
- Work: Speaking with the Angel
- Publisher: Riverhead Books
- Publication date as stated: Feb 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: SQUIRREL 1, SQUIRREL 2
- Teaser before the introduction: Yes
- Spoken words (computed): 2014
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dave Eggers
Book: Speaking with the Angel
ISBN: 978-1573228589
Publisher: Riverhead Books
Date (Month/Year): Feb 2001
```

### Introduction (context only: never use it for content warnings)

```text
Pit Bulls are probably the most abused dogs on the planet. The breed suffers horribly at the hand of humans. In the face of potential and outright banning of this breed, the dogs-- very real victims--are often completely overlooked.

Case #5125 . . . Severely dehydrated, starved and beaten with a metal pipe. This pit bull was barely clinging to life after losing a fight and being bagged and thrown in the river to die by its former owner. But fate intervened and this pup was found in the nick of time. This is where our story begins

After I was Thrown in the River and Before I Drowned by Dave Eggers.
```

### Performance text (classify this)

```text
OH, I'M A FAST DOG. I'm fast- fast. It's true and I love being fast I admit It I love it. You know fast dogs. Dogs that just run by and you say, That's a fast dog! Well that's me. A fast dog. I'm a fast- fast dog. Hoooooooo! Hooooooo!

I love it I love it. I run to feel the cool air cool through my fur. I run to feel the cold water come from my eyes. I run to feel my jaw slacken and my tongue come loose and flap from the side of my mouth and I go and go and go my name is Steven. I was once in a river. I was thrown in a river when I was small. You just cannot know. I was swimming, trying to know why I had been thrown in the river. I was six months old, and my eyes were burning, the water was bad. I paddled and it was like begging. The land on either side was a black stripe, indifferent. I saw the gray water and then the darker water below and then my legs wouldn't work, were stuck in some kind of seaweed or spider web and then I was in the air. I opened my burning eyes and saw him in yellow. The fisherman. I was lifted from the water, the water was below me. Then shivering on their white plastic boat bottom and they looked at me with their mustaches. I dried in the sun. They brought me to the place with the cages and I yelled for days. Others were yelling too. Everyone was crazy. Then people and a car and I was new at home. Ate and slept and it was dry, walls of wood.

Two people and two girls, thin twins who sleep in the next room, with a dollhouse between them. Every night I walk from the neighborhood and head to the woods and meet the others. It's shadowy out, the clouds low. I see the blues jumping inside the windows. I want all these people gone from the buildings and moved to the desert so we can fill the buildings with water. It's an idea I have. The buildings would be good if filled with water, or under water. These people. The only ones I like are the kids. I come to the kids and lick the kids. I run to them and push my nose into their stomachs. I run around them and around again as they run forward. They're slow but they are perfect things, almost perfect. I just cannot tell you how much I love all this, these woods, the dirt, and the smell of dogs nearby waiting to run. Tonight is cool, almost cold. There are no stars or clouds. We're all-impotent but there is running. I jog down the trail and see the others. Six of them tonight-Edward, Franklin, Susan, Mary, Robert, and Victoria.

Tonight I race Edward. Edward is a bull terrier and he is fast and strong but his eyes want to win too much; he scares us. The course is a simple one. We run from the entrance through the black-dark interior and out to the meadow and across the meadow and into the next woods, along the creek, then over the gap over the drainpipe and then along the creek until the highway. The jump over the drainpipe is the hard part. On the banks of the creek, near the drainpipe, on the dirt and in the weeds and on the branches of the rough gray trees are the squirrels. The squirrels have things to say; they talk before and after we jump. Sometimes while we're jumping they talk.

SQUIRREL 1: He is running funny.

SQUIRREL 2: She will not make it across. When we do not make it across the gap, and instead fall into the sandy bank, the squirrels say other things, their eyes full of glee.

SQUIRREL 1: It makes me laugh that she did not make it across the gap.

SQUIRREL 2: I am very happy that he fell and seems to be in pain. Sometimes one of the dogs, annoyed past tolerance, catches a squirrel in his mouth and crushes him. But then the next night they are back, all the squirrels, more of them. Always more. Edward is nudging me as I run. He bites me and bumps me and yells things at me. When we come to the bend he tries to bump me into the tree. I skid and then find my footing and keep running. I catch up to him quickly and because I am faster I gain all the speed and then I see the gap. Two more strides and I jump. I clear the gap by two feet and turn to see Edward jumping, and Edward's face looking across the gap, looking at my side of the gap, and his eyes still on the grass, exploding for it, and then he is falling, and only his front paws, claws, land above the bank. He yells something as he grabs, his eyes trying to pull the rest of him up, but he slides down the bank. He is fine but in the past others have been hurt. One dog, Wolfgang, died here, years ago. The other dogs and I jump down to help Edward up.

The squirrels say things.

SQUIRREL 1: That was a terrible jump.

SQUIRREL 2: Bad landing - Awful landing. I run the rest of the race alone. After we all run we go home. The next night I walk alone to the woods, my claws clicking on the sandpaper cement. Tonight I race Susan. Susan is a retriever, a small one, fast and pretty with black eyes. We take off, through the entrance through the black-dark interior and out to the meadow. Then the straightaway before the gap. Now we have to think about our own legs and muscles and timing before the jump. Susan looks at me and smiles but looks tired. Two more strides and I jump and then the hard ground rushes toward me and I land and hear her scream. I turn to see her face failing down the gap and run back to the gap. Robert and Victoria are down with her already. Her leg is broken and bleeding from the joint. She screams then wails, knowing everything already. The squirrels are above and talking.

SQUIRREL 1: Well, looks like she got what she deserved.

SQUIRREL 2: That's what you get when you jump. Some of them laugh. Franklin is angry. He walks slowly to where they're sitting; they do not move. He grabs one in his jaws and crushes all its bones. Their voices are always talking but we forget they are so small, their head and bones so tiny. The rest run away. He tosses the squirrel's broken form into the slow water. We go home. I jog to the buildings with Susan on my back. . I take her home and scratch at her door until she is let in. I go home and see the thin twins with their dollhouse and I go to the room with the bed and fall asleep before they come. The next night I don't want to go to the woods. I can't see someone fall, and can't hear the squirrels, and don't want Franklin to crush them in his jaws. I stay at home and I play with the twins in their pajamas. They put me on a pillowcase and pull me through the halls. I like the speed and they giggle. I stay with them tonight and then stay home for days.

When I come to the woods again, after ten days away, Susan has lost her leg. Susan has three legs, a bandage around her front shoulder. Her smile is a new and more fragile thing. It's colder out and the wind is mean and searching. Mary says that the rain has made the creek swell and the current too fast. The gap over the drainpipe is wider now so we decide that we will not jump. I race Franklin. Franklin is still angry about Susan's leg; neither of us can believe that things like that happen, that she has lost a leg and now when she smiles she looks like she's asking to die. When we get to the straightaway I feel so strong that I know I will go. I'm not sure I can make it but I know I can go far, farther than I've jumped before. I want this so much, the floating. I run and see the squirrels and their mouths are already forming the words they will say if I don't make it across. On the straightaway Franklin stops and yells to me that I should stop but it's just a few more strides and I've never felt so strong so I jump yes jump.

When I hit my head it was obvious. I hit my head and had a moment when I could still see - I saw Susan's face, her eyes open huge, and then the current took me out and then I fell under the surface. After I fell and was out of view the squirrels spoke.

SQUIRREL 1: He was a fool.

SQUIRREL 2: Everything he ever did was worthless. Franklin was angry and took five or six of them in his mouth, crushing them, tossing them one after the other. After I died, so many things happened that I did not expect. The first was that I was there, inside my body, for a long time. I was at the bottom of the river, stuck in a thicket of sticks and logs, for six days. I was dead, but was still there, and I could see out of my eyes. I could move around inside my body like it was a warm loose bag. I had been thrown into the river, a different river, when I was young by a man because I would not fight. I was supposed to fight and he kicked me and slapped my head and tried to make me mean. I didn't know why he was kicking me, slapping. I wanted him to be happy. I wanted the squirrels to jump and be happy as we dogs were. But they were different than we were, and the man who threw me to the river was also different. I thought we were all the same but as I was inside my dead body and looking into the murky river bottom I knew that some are wanting to run and some are afraid to run and maybe they are broken and are angry for it. After the sixth day I woke up and it was bright. I knew I was back. I stood and was in a wide field of buttercups. I could smell their smell and walked through them, my eyes at the level of the yellow, a wide blur of a line of yellow. I should say that it's very much the same here as there. There are more hills, and more waterfalls, and things are cleaner. I like it. Each day I walk for a long time, and I don't have to walk back. I can walk and walk, and when I am tired I can sleep. When I wake up, I can keep walking and I never miss where I started and have no home. I haven't seen anyone yet. I don't miss the cement like sandpaper on my feet, or the buildings with the sleeping men reaching. I sometimes miss the other dogs and the running. The one big surprise is that as it turns out. God is the sun. It makes sense, if you think about it. Why we didn’t see it sooner I cannot say. Every day the sun was right there burning, our and other planets hovering around it, always apologizing, and we didn't think it was God. Why would there be a God and also a sun? Of course, God is the sun. Everyone in the life before was cranky, I think, because they just wanted to know.
```

---

## IC-1957: After the Death of Anna Gonzales

- Title: After the Death of Anna Gonzales
- Author (byline): Terri Fields
- Work: Not specified
- Publisher: Henry Holt and Co
- Publication date as stated: Nov 2002
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1083
- Already set (do not supply): none

### Source block (context only)

```text
Author: Terri Fields
ISBN: 978-0805071276
Publisher: Henry Holt and Co
Date (Month/Year): Nov 2002
```

### Introduction (context only: never use it for content warnings)

```text
Picture this: It's the beginning of an ordinary school day. The bell has just rung. The halls are almost empty except for a few students trying to make it into homeroom before they're marked tardy. The day officially gets under way as usual with morning announcements being read over the PA: "Today is Thursday, October 3rd. Volleyball practice has been moved to 5:00pm. The chess club will meet today in Mr. Malkin's room. Congratulations to the JV football team on last night's 14-0 win against the Raiders. Go JV! Student Council will be selling spirit T-shirts during both lunch periods all week in honor of their victory. And now we have a special announcement from the principal."
```

### Performance text (classify this)

```text
CAUTION - This is a Novel in Verse. We recommend checking with your regional, state or national tournament before entering this selection in PROSE. Some states may require it be entered as POETRY.

Anna Gonzales

(Pg 99-100) "I will slip away,
Making little fuss.
And being less remembered,
which is pretty much the way I have always been.

Never pretty or popular enough to matter. Never outrageous or outstanding enough

to get attention. Sometimes, I have to pinch myself to make certain

that I am even real.
Conversations swirl around me.
Invitations to others surround me.
Even Alexis, who has tried to be my best friend,
Is dragged down by my invisibility.

No, I am not pregnant
Not on drugs
Not alcohol
Not influenced by rock or heavy metal or rap
I am just not.
And I am so tired of trying to be.

So I say good-night to this world Feeling since it has never embraced me It will not mind if I have abandoned it."

Principal Barron

(Pg 6 -7) Thirty years in education.
I’ve broken up fights.
Fired a teacher.
Failed a student.

But not this. This is too much to ask.

Thirty years in education
I’ve learned school law.
Listened to angry parents.
Located lost school buses.
But not this.
This is too much to ask.

To make a difference.
To better kids’ lives.
That was why I went into education.
So how does this happen?
How do I . . .

“Mr. Barron, announcements are almost over.

Do you still have a special?”

I trudge toward the camera. Words caught in unwilling voice.

“I am sorry to tell you of the death of one of our

students.”

Must continue. Rumors always worse than truth.

“Anna Gonzales took her life last night.

Our sympathies to her family and friends.

Grief counselors will be available all day.”

TRANSITION

And so, life goes on, but how does it go on? How does one life really affect another? If I am here today and not tomorrow, would that make an impact on your life in any way? Anna Gonzales is dead. She committed suicide. If you could take a notebook and somehow chronicle what went through the minds of students and faculty immediately after that announcement was made, you would know what happened on the day . . .

After the Death of Anna Gonzales by Terri Fields

Damon Reingold

(Pg 9) The game doesn’t always go your way.
I know.
You can go to every practice
Even when your shoulder aches

Your ankle throbs

Your homework waits. You can do 100 hand-offs

1,000 free throws

10,000 reps And still sit on the bench

While You watch Darrith Evans

Slack off

Skip practice

Showboat for Debbie And still be part of the

Starting five. The game doesn’t always go your way.

Forget fair.

Feel forgotten. But damn it, Anna,

You don’t stop playing.

Lauren Reynolds

(Pg 21) Since September,
I sat one seat behind Anna in algebra.
Passed papers to her every day.
Studied for tons of tests together.

Though it often seemed impossible, Eventually, We always found the unknown for X.

But not this time.
This equation
Bounces against my brain.
And sneers at all attempted answers.

I know I'll re-examine the variables,
And reanalyze the unknowns, maybe forever.
But
It won't matter.

Because, Anna- I know I'll never figure out Y.

Y you didn't want to live- And Y I never noticed.

TRANSITION

According to the Center for Disease Control, suicide is responsible for almost 4,400 deaths of young people each year. The same study speculates that students aged 10 to 14 are more likely to commit suicide than other age group. Even more concerning is that the suicide of a peer is often a traumatic experience for adolescents (many of whom are left bewildered by the lack of warning signs), often influencing other teens who are already feeling suicidal. The following two poems are by students who have already felt the closeness of death – Anna’s suicide had a dramatic impact on these vulnerable teens as well.

Kathleen Hays

(Pg 13) My brother was seven
When they told us the bad news:
It was a tumor
That had bloomed in his body
Like a weed.

Seven surgeries, and still he smiled.
We had his eighth birthday party in the hospital.
He said he could feel that he was almost well.
And we celebrated.

At nine, they said new cells had sprouted. The chemo was strong. The cancer was stronger.

But . . . in spite of the pills and the pain, In spite of the surgeries and suffering, He chose life.

And you, Anna, who had health, Chose death. How could you?

Karen Covington

(Pg 69) Mixed up memories
Of the daddy
Who introduced me to Winnie-the-Pooh.
Who sang every verse of kids' silly songs.
Who whispered the lullabies that lured me to sleep.
Mixed-up Memories
Of the dad
Who cheered my summer softball
Even if I never got a hit.
Who promised I would always be
His most perfect princess.
Mixed-up Memories
Of the father
Who guaranteed he'd be the proudest of all the parents
At my college graduation.
Who vowed he'd walk me down the aisle
even if I married at forty. Who predicted no one would be
a better Grandpa.
Of a morning last summer
When I learned
My hero had taken his own life.
When that was the truth,
Everything I understood of love and safety
Was a lie.
So, Anna, did you know
That when you kill yourself
Those you say you love,
They die too?

TRANSITION

Suicide is a permanent solution to temporary problems. And the suicide of a student affects not only other students, but the teachers and staff at a school as well. You’ve heard Principal Barron’s thoughts already and in the following poem, Ms. Mason, Anna’s English teacher explains her feelings.

Ms. Mason, English Teacher

(Pg 61) "Death be not proud."

"Do not go gentle into that good night'"

Fragments of poems I've taught.

Can't finish them--can't think how they go.

Brain too numb to truly believe.

That empty seat in the third row. Anna will be back. She must be.

Quiet, sweet'

A face framed by long lush brown hair. Almond eyes always seemed luminous. Giving no hint that this unnatural sleep would be her fate.

I've tried to teach through literature

The wonder of life.

Yet the quiet rebuke of that empty chair

Speaks louder than the most vocal of student skeptics.

I cannot take my eyes from the spot.

"There in the sudden blackness, the black pall

Of nothing, nothing, nothing--nothing at all."
```

---

## IC-1958: After Twenty Years

- Title: After Twenty Years
- Author (byline): William Sydney Porter
- Work: The Complete Works of O. Henry
- Publisher: Doubleday
- Publication date as stated: Nov 1960
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, BOB, POLICEMAN, MAN
- Teaser before the introduction: No
- Spoken words (computed): 1179
- Already set (do not supply): none

### Source block (context only)

```text
Author: William Sydney Porter
Book: The Complete Works of O. Henry
ISBN: 978-0385009614
Publisher: Doubleday
Date (Month/Year): Nov 1960
```

### Introduction (context only: never use it for content warnings)

```text
O. Henry is the pen name of William Sydney Porter, famous today for his short stories with surprise endings. However, not many people know that he left school when he was 15 years old and moved to Texas. He edited a humor magazine called The Rolling Stone and worked for a few years in a bank in Austin. He was a careless record keeper, and two years after he left the bank, he was accused of embezzling its money. He was probably innocent, but he panicked and ran off to Honduras. A year or so later, he returned to Austin to be with his dying wife and was arrested. He was convicted and spent 3 years in an Ohio federal prison.

Porter actually found many of his story plots in jail. He may also have found his "pen" name there...a prison guard was named Orrin Henry.

After Twenty Years by William Sydney Porter. . . aka O. Henry
```

### Performance text (classify this)

```text
NARRATOR: The policeman on the beat moved up the avenue impressively. The impressiveness was habitual and not for show, for spectators were few. The time was barely 10 o'clock at night, but chilly gusts of wind with a taste of rain in them had well-nigh de-peopled the streets.

Trying doors as he went, twirling his club with many intricate and artful movements, turning now and then to cast his watchful eye adown the pacific thoroughfare, the officer, with his stalwart form and slight swagger, made a fine picture of a guardian of the peace. The vicinity was one that kept early hours. Now and then you might see the lights of a cigar store or of an all-night lunch counter; but the majority of the doors belonged to business places that had long since been closed.

When about midway of a certain block, the policeman suddenly slowed his walk. In the doorway of a darkened hardware store a man leaned, with an unlighted cigar in his mouth. As the policeman walked up to him the man spoke up quickly.

BOB: It's all right, officer. I'm just waiting for a friend. It's an appointment made twenty years ago. Sounds a little funny to you, doesn't it? Well, I'll explain if you'd like to make certain it's all straight. About that long ago there used to be a restaurant where this store stands--'Big Joe' Brady's restaurant.

POLICEMAN: Until five years ago. It was torn down then.

NARRATOR: The man in the doorway struck a match and lit his cigar. The light showed a pale, square-jawed face with keen eyes, and a little white scar near his right eyebrow. His scarfpin was a large diamond, oddly set.

BOB: Twenty years ago to-night, I dined here at 'Big Joe' Brady's with Jimmy Wells, my best chum, and the finest chap in the world. He and I were raised here in New York, just like two brothers, together. I was eighteen and Jimmy was twenty. The next morning, I was to start for the West to make my fortune. You couldn't have dragged Jimmy out of New York; he thought it was the only place on earth. Well, we agreed that night that we would meet here again exactly twenty years from that date and time, no matter what our conditions might be or from what distance we might have to come. We figured that in twenty years each of us ought to have our destiny worked out and our fortunes made, whatever they were going to be.

POLICEMAN: "It sounds pretty interesting. Rather a long time between meets, though, it seems to me. Haven't you heard from your friend since you left?

BOB: Well, yes, for a time we corresponded. But after a year or two we lost track of each other. You see, the West is a pretty big proposition, and I kept hustling around over it pretty lively. But I know Jimmy will meet me here if he's alive, for he always was the truest, staunchest old chap in the world. He'll never forget. I came a thousand miles to stand in this door to-night, and it's worth it if my old partner turns up.

(pulls out a pocket watch to check the time) Three minutes to ten. It was exactly ten o'clock when we parted here at the restaurant door.

POLICEMAN: Did pretty well out West, didn't you?

BOB: You bet! I hope Jimmy has done half as well. He was a kind of plodder, though, good fellow as he was. I've had to compete with some of the sharpest wits going to get my pile. A man gets in a groove in New York. It takes the West to put a razor-edge on him."

POLICEMAN: (twirling his club, he begins to leave) I'll be on my way. Hope your friend comes around all right. Going to call time on him sharp?

BOB: I should say not! I'll give him half an hour at least. If Jimmy is alive on earth he'll be here by that time. So long, officer.

POLICEMAN: Good-night, sir. (he continues on his beat)

NARRATOR: There was now a fine, cold drizzle falling, and the wind had risen from its uncertain puffs into a steady blow. The few foot passengers astir in that quarter hurried dismally and silently along with coat collars turned high and pocketed hands. And in the door of the hardware store the man who had come a thousand miles to fill an appointment, uncertain almost to absurdity, with the friend of his youth, smoked his cigar and waited.

About twenty minutes he waited, and then a tall man in a long overcoat, with collar turned up to his ears, hurried across from the opposite side of the street. He went directly to the waiting man.

MAN: (doubtfully) Is that you, Bob?

BOB: Is that you, Jimmy Wells?

MAN: Bless my heart! (grasping Bob’s hands with his own) It's Bob, sure as fate. I was certain I'd find you here if you were still in existence. Well, well, well! --twenty years is a long time. The old gone, Bob; (gestures to the old diner) I wish it had lasted, so we could have had another dinner there. How has the West treated you, old man?

BOB: Bully; it has given me everything I asked it for. You've changed lots, Jimmy. I never thought you were so tall by two or three inches.

MAN: Oh, I grew a bit after I was twenty.

BOB: Doing well in New York, Jimmy?

MAN: Moderately. I have a position in one of the city departments. Come on, Bob; we'll go around to a place I know of and have a good long talk about old times."

NARRATOR: The two men started up the street, arm in arm. The man from the West, his egotism enlarged by success, was beginning to outline the history of his career. The other, submerged in his overcoat, listened with interest.

At the corner stood a drug store, brilliant with electric lights. When they came into this glare each of them turned simultaneously to gaze upon the other's face. The man from the West stopped suddenly and released his arm.

BOB: (snapping) You're not Jimmy Wells. Twenty years is a long time, but not long enough to change a man's nose from a Roman to a pug.

MAN: It sometimes changes a good man into a bad one. You've been under arrest for ten minutes, 'Silky' Bob. Chicago thinks you may have dropped over our way and wires us she wants to have a chat with you. Going quietly, are you? That's sensible. Now, before we go on to the station here's a note I was asked to hand you. You may read it here at the window. It's from Patrolman Wells.

The man from the West unfolded the little piece of paper handed him. His hand was steady when he began to read, but it trembled a little by the time he had finished. The note was rather short.

"Bob: I was at the appointed place on time. When you struck the match to light your cigar, I saw it was the face of the man wanted in Chicago. Somehow I couldn't do it myself, so I went around and got a plain clothes man to do the job. Jimmy"
```

---

## IC-1959: Alexander and the Terrible, Horrible, No Good, Very Bad Day

- Title: Alexander and the Terrible, Horrible, No Good, Very Bad Day
- Author (byline): Judith Viorst
- Work: Not specified
- Publisher: Atheneum Books
- Publication date as stated: June 1972
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 744
- Already set (do not supply): none

### Source block (context only)

```text
Author: Judith Viorst
ISBN: 978-0689300721
Publisher: Atheneum Books
Date (Month/Year): June 1972
```

### Introduction (context only: never use it for content warnings)

```text
Ever had one of those days or a day when lots of “THOSE DAYS” gang up on your all at once? Alexander is only 8, but today, he’s faced a barrage of bummers worthy of a country- western song: getting smushed in the middle seat of the car, a dessert-less lunch sack, a cavity at the dentist's office, stripe-less sneakers, witnessing kissing on television, and being forced to sleep in railroad-train pajamas. When it comes right down to it . . . it’s all in your perspective.

Alexander and the Terrible, Horrible, No Good, Very Bad Day by Judith Viorst
```

### Performance text (classify this)

```text
I went to sleep with gum in my mouth and now there’s gum in my hair and when I got out of bed this morning I tripped on the skateboard and by mistake I dropped my sweater in the sink while the water was running and I could tell it was going to be a terrible, horrible, no good, very bad day.

At breakfast Anthony found a Corvette Sting Ray car kit in his breakfast cereal box and Nick found a Junior Undercover Agent code ring in his breakfast cereal box but in my breakfast cereal box all I found was breakfast cereal. I think I’ll move to Australia.

In the carpool, Mrs. Gibson let Becky have a seat by the window. Audrey and Elliott got seats by the window too. I said I was being scrunched. I said I was being smushed. I said, if I don’t get a seat by the window, I am going to be car sick. No one even answered. I could tell it was going to be a terrible, horrible, no good, very bad day.

At school Mrs. Dickens liked Paul’s picture of the sailboat better than my picture of the invisible castle. At singing time, she said I sang too loud. At counting time, she said I left out sixteen. Who needs sixteen? I could tell it was going to be a terrible, horrible, no good, very bad day.

I could tell because Paul said I wasn’t his best friend anymore. He said that Phillip Parker was his best friend, and that Albert Moyo was his next best friend and that I was only his third best friend. I hope you sit on a tack, I said to Paul. I hope the next time you get a double-decker strawberry ice cream cone the ice cream part falls off the cone part and lands in Australia.

There were two cupcakes in Phillip Parker’s lunch bag and Albert got a Hershey bar with almonds and Paul’s mother gave him a piece of jelly roll that had little coconut sprinkles on the top. Guess whose mother forgot to put in dessert? It was a terrible, horrible, no good, very bad day.

That’s what it was, because after school, my mom took us all to the dentist and Dr. Fields found a cavity just in me. “Come back next week and I’ll fix it,” said Dr. Fields. “Next week,” I said, “I’m going to Australia.”

On the way downstairs the elevator door closed on my foot and while we were waiting for my mom to go get the car, Anthony made me fall where it was muddy and then when I started crying because of the mud, Nick said I was a crybaby and while I was punching Nick for saying “crybaby,”

my mom came back with the car and scolded me for being muddy and fighting. I am having a terrible, horrible, no good, very bad day.

I told everybody. No one even answered. So then we went to the shoe store to buy some sneakers. Anthony chose white ones with blue stripes. Nick chose red ones with white stripes. I chose blue ones with red stripes, but the man said, “We’re all sold out.” They made me buy plain old white ones, but they can’t make me wear them.

When we picked up my dad at his office, he said I couldn’t play with his copying machine, but I forgot. He also said to watch out for his books on his desk and I was careful as could be except for my elbow. He also said don’t fool around with his phone, but I think I called Australia. My dad said please don’t pick him up anymore. It was a terrible, horrible, no good, very bad day.

There were lima beans for dinner, and I hate limas. There was kissing on TV and I hate kissing. My bath was too hot, I got soap in my eyes, my marble went down the drain, and I had to wear my railroad-train pajamas. I hate my railroad-train pajamas. When I went to bed, Nick took back the pillow he said I could keep, and the Mickey Mouse night-light burned out and I bit my tongue. The cat wants to sleep with Anthony, not with me. It has been a terrible, horrible, no good, very bad day.

My mom says some days are like that even in Australia.
```

---

## IC-1960: All I Really Need to Know I Learned in Kindergarten

- Title: All I Really Need to Know I Learned in Kindergarten
- Author (byline): Robert Fulghum
- Work: Not specified
- Publisher: Ballentine Books
- Publication date as stated: 1993
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1283
- Already set (do not supply): none

### Source block (context only)

```text
Author: Robert Fulghum
ISBN: 978-0804105262
Publisher: Ballentine Books
Date (Month/Year): 1993
```

### Introduction (context only: never use it for content warnings)

```text
All I Really Need to Know I Learned in Kindergarten By Robert Fulghum
```

### Performance text (classify this)

```text
Each spring, for many years, I have set myself the task of writing a personal statement of belief: a Credo. When I was younger, the statement ran for many pages, trying to cover every base, with no loose ends. It sounded like a Supreme Court brief, as if words could resolve all conflicts about the meaning of existence.

Finally I realized that I already know most of what’s necessary to live a meaningful life—that it isn’t all that complicated. I know it. And have known it for a long, long time. Living it—well, that’s another matter, yes? Here’s my Credo:

ALL I REALLY NEED TO KNOW about how to live and
what to do and how to be I learned in kindergarten.
Wisdom was not at the top of the graduate-school
mountain, but there in the sandpile at Sunday School.
These are the things I learned:
• Share everything.
• Play fair.
• Don’t hit people.
• Put things back where you found them.
• Clean up your own mess.
• Don’t take things that aren’t yours.
• Say you’re sorry when you hurt somebody.
• Wash your hands before you eat.
• Flush.
• Warm cookies and cold milk are good for you.
• Live a balanced life—learn some and think some and

draw and paint and sing and dance and play and work

every day some. • Take a nap every afternoon.

• When you go out into the world, watch out for traffic,

hold hands, and stick together. • Wonder. Remember the little seed in the Styrofoam

cup: The roots go down and the plant goes up and

nobody really knows how or why, but we are all like

that. • Goldfish and hamsters and white mice and even the

little seed in the Styrofoam cup—they all die. So do we. • And then remember the Dick-and-Jane books and the

first word you learned—the biggest word of all—LOOK.

Everything you need to know is in there somewhere. The Golden Rule and love and basic sanitation. Ecology and politics and equality and sane living.

Take any one of those items and extrapolate it into sophisticated adult terms and apply it to your family life or your work or your government or your world and it holds true and clear and firm. Think what a better world it would be if we all—the whole world—had cookies and milk about three o’clock every afternoon and then lay down with our blankies for a nap. Or if all governments had as a basic policy to always put things back where they found them and to clean up their own mess. And it is still true, no matter how old you are—when you go out into the world, it is best to hold hands and stick together.

The Kindergarten Credo is not kid stuff. It is not simple. It is elemental.

[It] answers the questions asked sooner or later by every one of us who once stared out a classroom window wondering: Why am I here? Why do I have to go to school?

We are sent to school to be civilized—to be introduced to the essential machinery of human society. Early on in our lives we are sent out of the home into the world. To school. We have no choice in this. Society judges it so important that we be educated that we must go. It is the law. And when we get to school we are taught the fundamentals on which civilization rests. These are first explained in language a small child understands.

For example, it would do no good to tell a six-year-old that “Studies have shown that human society cannot function without an equitable distribution of the resources of the earth.” While this statement is profoundly and painfully true, a child cannot comprehend this vocabulary. So a child is told that there are twenty children and five balls to play with; likewise four easels, three sets of blocks, two guinea pigs, and one bathroom. To be fair, we must share.

Likewise a six-year-old will not understand that “By and large it has been demonstrated that violence is counterproductive to the constructive interaction of persons and societies.” True. But a child can better understand that the rule out in the world and in the school is the same: Don’t hit people. Bad things happen. The child must understand this rule is connected to the first rule: People won’t share or play fair if you hit them.

It’s hard to explain the cost and consequences of environmental pollution and destruction to a six-year-old. But we are paying a desperate price even now because adults did not heed the instructions of kindergarten: Clean up your own mess; put things back where you found them; don’t take what’s not yours.

“The history of society is more defined by its understanding of disease than its formulation of philosophy and political theory.” True. Basic sanitation. Keeping excrement off our hands as well as out of our minds is important. But it’s enough to teach a child to use the toilet, flush, and wash his hands regularly.

And so on. From the first day we are told in words we can handle what has come to be prized as the foundation of community and culture. Though the teacher may call these first lessons “simple rules,” they are in fact the distillation of all the hard-won, field-tested working standards of the human enterprise.

Once we are told about these things, we soon discover we are taking a lab course. We are going to be asked to try and practice these precepts every day. Knowledge is meaningful only if it is reflected in action. The human race has found out the hard way that we are what we do, not just what we think. This is true for kids and adults—for schoolrooms and nations.

I am sometimes amazed at what we did not fully grasp in kindergarten. In the years I was a parish minister I was always taken aback when someone came to me and said, “I’ve just come from the doctor, and he told me I have a only a limited time to live.”

I was tempted to shout, “What? You didn’t know? You had to pay a doctor to tell you—at your age? Where were you the week in kindergarten when you got the little cup with the cotton and water and seed? Life happened— remember? A plant grew up and the roots grew down. A miracle. And then a few days later the plant was dead. DEAD. Life is short. Were you asleep that week or home sick or what?”

I never said all that. But I thought it. And it’s true. The idea was for us to have the whole picture right from the beginning. Life-and-death. Lifedeath. One event. One short event. Don’t forget.

There’s another thing not everyone figures out right away: It’s almost impossible to go through life all alone. We need to find our support group—family, friends, companion, therapy gatherings, team, church or whatever. The kindergarten admonition applies as long as we live: “When you go out into the world, hold hands and stick together.” It’s dangerous out there—lonely, too. Everyone needs someone. Some assembly is always required. What we learn in kindergarten comes up again and again in our lives as long as we live. In far more complex, polysyllabic forms, to be sure. In lectures, encyclopedias, bibles, company rules, courts of law, sermons, and handbooks. Life will examine us continually to see if we have understood and have practiced what we were taught that first year of school.
```
