# Classification request: batch 47 of 63 (40 records, IC-1841 to IC-1880)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-047-reply.json`.

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

## IC-1841: Sisters’ Entrance (Selections From)

- Title: Sisters’ Entrance (Selections From)
- Author (byline): Emtithal “Emi” Mahmoud
- Work: Not specified
- Publisher: Andrews McMeel Publishing
- Publication date as stated: May 2018
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1508
- Already set (do not supply): none

### Source block (context only)

```text
Author: Emtithal (Emi) Mahmoud
ISBN: 978-1449492793
Publisher: Andrews McMeel Publishing
Date (Month/Year): May 2018
```

### Introduction (context only: never use it for content warnings)

```text
From Refugee to Ivy League College Student to World Champion Poet, and now Goodwill Ambassador— 24-year-old Emtithal (Emi) Mahmoud advocates for the cause of refugees through her poetry and incredible experience.

Despite death-threats and repeated attempts at silencing, Emi continues to shatter long-standing stereotypes both at home and abroad. Her debut collection of poetry, Sisters' Entrance, has lifted the voices of women and girls, reaching across languages and barriers. Selections from Sisters’ Entrance by Emi Mahmoud
```

### Performance text (classify this)

```text
Bullets (Pg 100)

My father’s voice yanked me awake
My brother had been shot.
I had never felt fear like that:
waiting for that first breath on the other side of the line at a
hospital half a world away.

The thing we had been fighting for the past 11 years had reached the capitol and burrowed itself into my next of kin.

I am 21 years old and I know more about death than about living

My life experiences revolved around massacres and funerals. I know how to start revolutions, but

I don’t know how to give in to this thing called youth because I know how it ends.

I called my brother an idiot and he said, live free or die. He said, freedom is a question of life;

If you do not reach for it, then you are not alive.

People Like Us (Pg 2)

Memories of my childhood live between the rings of sand around my ankles and the desert heat in my lungs.

I still believe that nothing washes worry from tired skin better than the Nile and my grandma’s hands.

Every day I go to school with the weight of dead neighbors on my shoulders.

The first time I saw bomb smoke, it didn’t wind and billow like the heat from our kitchen hearth.

It forced itself on the Darfur sky,

Smothering the sun with tears that it stole from our bodies.

The worst thing about genocide isn’t the murder, the politics, the hunger the government-paid soldiers

that chase you across borders and into camps

It’s the silence.

For three months, they closed the schools down because people like us are an eyesore.

The first month, we took it. The second, we waited.

The third month, we met underneath the date palm trees, drinking up every second our teachers gave us, turning fruit pits into fractions. On the last day, they came with a message Put them in their place.

We didn’t stand a chance. Flesh was never meant to dance with silver bullets.

So we prayed for the sun to come and melt daggers from our backs.

Lifted our voices up to God
until the clouds were spent for weeping
and the sand beneath our toes
echoed with the song of every soul
that ever walked before us.

I hid underneath the bed that day with four other people.

Twelve years later and I can’t help but wonder
where my cousins hid when the soldier
torched the houses,
threw the bodies
in the wells.

If the weapons didn’t get you, the poison would.

Sometimes they didn’t want to use bullets because it would cost them more than we did.

I’ve seen sixteen ways to stop a heart.

When you build nations on someone’s bones what sense does it make to break them?

In one day, my mother choked on rifle smoke,

my father washed the blood from his face,
my uncles carried half the bodies
to the hospital,
the rest to the grave.

We watched. For every funeral we planned there were sixty we couldn’t

Half the sand in the Sahara tastes a lot like powdered bone.

TRANSITION

In addition to the million refugees already in Uganda, over the past 12 months, an average of 1,800 South Sudanese have been arriving there every day. More than 85% are women and children who continue to speak of barbaric violence occurring in Sudan. Armed groups burn down houses with civilians inside, people are killed in front of family members, and women and girls are sexually assaulted.

Head Over Heels (Pg 54)

They hand me the microphone as my shoulder sinks under the weight of this dress; The woman says, The one millionth refugee just left South Sudan, can you comment?

I feel my feet rock back and
forth on the heels my mother
bought Begging the question,
do we stay, or is it safer to choose flight?

My mind echoes through the numbers:
One million gone, 400,000 dead in
Darfur,
two million displaced
and this lump takes over my throat as if each of those
bodies found a grave right here in
my esophagus.

Our once country—
all west, and south, and east, and
north— so restless, the Nile couldn’t hold us
together and you ask me to summarize?

They talk about the numbers as if this isn’t still happening, As if 500,000 didn’t just die in Syria, as if 3,000 aren’t still making their final stand at the bottom of the Mediterranean, as if there aren’t entire volumes full of factsheets about our genocide and now you want me to write one?

Fact: we never talked over breakfast because the warplanes would swallow our voices.

Fact: my grandfather didn’t want to leave home so he died in a warzone.

Fact: a burning bush without God is just a fire.

I measure the distance between what I know and what is safe to say on a microphone. Do I talk about sorrow, displacement? Do I mention the violence? How it’s never as simple as what we see on TV? How there are weeks’ worth of fear before the camera is on?

Do I talk about our bodies? How they are 60 percent water, but we still burn like driftwood? Do I tell her the men died first? Mothers forced to watch the slaughter? That they came for our children? Scattering them across the continent until our homes sank, that even castles sink at the bite of the bomb?

Do I mention the elderly? Our heroes—
too weak to run too expensive to shoot?
How they would march them hands raised, rifles at their
backs into the fire?
How their walking sticks kept the flames alive?

It sounds too harsh for a bundle of wires and an audience to swallow; too relentless, like the valley that filled with the putrid smoke of our deaths.

Is it better in verse? Can a stanza become a burial shroud?

Will it sting less if I say it softly?
Will the pain leave when the microphone does?
If you don’t see me cry will you listen better?
30 seconds for the sound bite and now 3 minutes for the
poem. Why does every word feel like
I’m saying my last?

My tongue goes dry, the same way we died—
becoming ash without ever having been coal.
I feel my left leg go numb and realize that I locked my
knees,
bracing for impact.

I never wear shoes I can’t run in.

Mama (Pg 108)

I was walking down the street when a man stopped me and

said,

Hey yo sistah, you from the motherland?

Because my skin is a shade too deep not to have come from

foreign soil

Because this garment on my head screams Africa

Because my body is a beacon calling everybody to come

flock to the motherland

I said, I’m Sudanese, why? He says, ‘cause you got a little bit of flavor in you, I’m just admiring what your mama gave you

Let me tell you something about my mama
She can reduce a man to tattered flesh without so much as
blinking
Her words fester beneath your skin and the whole time,
You won’t be able to stop cradling her eyes.
My mama is a woman, flawless and formidable in the same
step.
Woman walks into a warzone and has warriors cowering at
her feet
My mama carries all of us in her body,
on her face, in her blood and
Blood is no good once you let it loose
So she always holds us close.

When I was 7, she cradled bullets in the billows of her robes. That same night, she taught me how to get gunpowder out of cotton with a bar of soap. Years later when the soldiers held her at gunpoint and asked her who she was She said, I am a daughter of Adam, I am a woman, who the hell are you?

The last time we went home, we watched our village burn,
Soldiers pouring blood from civilian skulls
As if they too could turn water into wine.
They stole the ground beneath our feet.

The woman who raised me turned and said, don’t be scared I’m your mother, I’m here, I won’t let them through.

My mama gave me conviction.
Women like her
Inherit tired eyes,
Bruised wrists and titanium plated spines.
The daughters of widows wearing the wings of amputees
Carry countries between their shoulder blades.

[So. . . ] Don’t talk about the motherland unless you know
that being from Africa
means waking up an afterthought in this country.
Don’t talk about my flavor unless you know that
My flavor is insurrection, it is rebellion, resistance
my flavor is mutiny
It is burden, it is grit and it is compromise
And you don’t know compromise until you’ve rebuilt your
home for the third time
Without bricks, without mortar, without any other option

I turned to the man and said,
My mother and I can’t walk the streets alone back home
anymore.
Back home, there are no streets to walk.
```

---

## IC-1842: Sleeping Sickness and Andrew

- Title: Sleeping Sickness and Andrew
- Author (byline): Julia Serano and Andrea Gibson Sleeping Sickness
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1180
- Already set (do not supply): none

### Source block (context only)

```text
Author: Julia Serano
Book: Word Warriors
ISBN: 978-1580052214
Publisher: Seal Press
Date (Month/Year): Oct 2007
Author: Andrea Gibson
Book: The Madness Vase
ISBN: 978-1935904373
Publisher: Write Bloody Publishing
Date (Month/Year): 2012
```

### Introduction (context only: never use it for content warnings)

```text
“Are transgender people allowed to pray?” If one prays for strength, for knowledge, for forgiveness, for help in forgiving, for clarification, for peace; then not only are transgender people “allowed” to pray, they are blessed by praying. And so are we all.

When Julia Serano was 12, she attended a Catholic school and lived in daily fear of rejection by a vengeful God who she had been taught would cast sinners into the pit of hell. Julia’s sin? She had been born a boy, but in her heart knew that she was a girl. She prayed and begged for forgiveness.

Sleeping Sickness by Julia Serano
```

### Performance text (classify this)

```text
in the name of the father
the son
and the holy spirit
amen

that's how it begins
my nights are spent
composing insomniac open letters to you
two-hour-long monologues
that end in exhaustion
and sometimes in the middle of my day
i'll remember that i fell asleep
before ending my previous night's prayer
with a proper amen
and i'll wonder whether my channel to you is still open
my every word an invocation
the sounds of my atari games
little league practice
and eighth grade history class
becoming the annoying background noise of heaven

. . . maybe forgetting to say amen
makes my life one long continuous prayer
and if so, then you were there that afternoon
when i tucked my penis tightly behind my legs
just to see what i'd look like without it
when i wrapped bedroom curtains around my body
like a prom dress
turned tattered shoelaces
into necklaces and bracelets
and you were there later that same night
when i began another prayer within a prayer
to once again beg for your forgiveness

wanting to be a girl
never came up in CCD or sunday mass
and it's not covered in the ten commandments
but from everything the nuns and priests taught me
about you
i know that you do not approve
and when i turn to your holy words
to look for anything that might shed some light
onto whatever this is that i'm going through
i keep returning to the same story
the one about abraham
and how you commanded him to sacrifice his son to you
stopping the blade only seconds before
he actually went through with it
and forgive me father
for i can't help but think
that that was a ***** up thing to do

and maybe i'm like abraham
and this is just another one of your tests
maybe you put girl thoughts
into the heads of twelve-year-old boys
just to see how they'll react
maybe i'm an experiment
and you're up in heaven looking down on me
taking notes as i tear myself apart in self-hatred
tossing and turning in bed
as if acting out my inevitable burning in hell
and at first
my sins made me even more devout
i'd lie awake each night
clutching the glow-in-the-dark rosary beads
that my grandmother gave me
repeating the words that i once heard her say
“blessed are those who have not seen yet believe”
and i want to believe
but more and more it just feels
like you're torturing me
and i'm doing the best that i can
to plug up all the holes
in this disintegrating dam
as my brain bleeds rivers of bad thoughts
that pour out of my mouth and hands
like wounds that won't clot
and i can't understand
why you won't help
when i've asked you over and over again
to please either turn me into a girl
or else make these thoughts stop

the nuns say that you answer all prayers
it's just that sometimes the answer is no
well, i'm tired of praying to a god
who only offers me
thou shalt not's
i'm tired from lack of sleep
from keeping secrets
that burn so much that they hollow me out
i am tired of hurting so much
that sometimes i pray
that i don't wake up
so forgive me father for i have sinned
i have dared to share
all of myself with you
forcing you to watch
one long sacrilegious prayer
within a prayer
within a prayer
within a prayer
like a serpent swallowing its own soul
like a serpent swallowing itself whole
and maybe tonight
i'll finally be cured of this sleeping sickness
because the last few years
of living in absolute shame
and unbelievable pain
has made me fearless enough to finally say
amen.

TRANSITION Poet Andrea Gibson also struggled with gender identity as she was growing up. For her the issue isn’t male OR female . . . but perhaps some category in between. She concludes that the best thing a person can do for the world is be themselves, honestly, openly -- brave and beautiful. We are all different. Not one of us the same, but we all share a common bond: we want to be loved. The only place to start is with the self. Love yourself first, share the beauty. She shares her beauty with us in “Andrew” by Andrea Gibson.

Andrew Would tug at the crotch of my pants the way only pubescent boys do When I was a kid I would sometimes secretly call myself Andrew Ran around pounding on my bare chest like Tarzan It’s not that I thought I’d grow up to be a man I just never thought I’d grow up to be a woman either From what I could tell neither of those categories fit me But believe me I knew from a very young age never to say Hey Dad, this Adam or Eve thing isn’t really working for me I mean what about all the kinds of people in-between? In the third grade Lynette Lions asked me where all my Barbies were I lied and told her I got in trouble so my mom took ‘em away I didn’t dare say Barbie sucks, Lynette!

And for that matter, Timmy, so does G.I. Joe
I want to grow into something none of us has ever seen
before
And gender is just one of the ways we’re boxed and
labeled
Before we’re ever able to speak who we dream we are
Who believe we’ll become
Like drum beats forever changing their rhythm
I am living today as someone I had not yet become
yesterday
And tonight I will borrow only pieces of who I was today
To carry with me tomorrow
No, I’m not gay
No, I’m not straight
I’m sure as **** not bisexual, damn it!
I am whatever I am when I am it
Loving whoever you are when the stars shine
And whoever you’ll be when the sun rises
Yes, I like girls
Yes, I like boys
Yes, I like boys who like boys
I like girls . . .
Girls who don’t call themselves girls
Crew cuts or curls and that really bad hair phase in
between
Tell me we’ll be naming our children “Beautiful” and
nothing else
Tell Barbie she can go now
Tell GI Joe to put his gun down
And find a boyfriend or a girlfriend or a girl-boy-friend
GI Joe just needs a friend
I mean, he’s plastic and not even the kind of plastic that
bends
I want to bend in a thousand directions
Like the sun does, like love does, like time stopped
So the hands of the clock could hold each other
Like I held these words for too many years on the tip of
my tongue
I am my mother’s daughter
I am midnight sun
You can find me on the moon waxing and waning
My heart full of petals, every single one begging
“Love me, love me, love me
Whoever I am
Whoever I become
```

---

## IC-1843: Snow White and the Seven Dwarfs

- Title: Snow White and the Seven Dwarfs
- Author (byline): Anne Sexton
- Work: Transformations
- Publisher: Mariner Books
- Publication date as stated: Feb 2001
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 964
- Already set (do not supply): none

### Source block (context only)

```text
Author: Anne Sexton
Book: Transformations
ISBN: 978-0618083435
Publisher: Mariner Books
Date (Month/Year): Feb 2001
```

### Introduction (context only: never use it for content warnings)

```text
We’ve all been told the stories of women like Cinderella, Snow White, and Rapunzel, saved from their wretched lives by a gorgeous prince to live faultless lives filled with wealth and beauty. We all know them because stories like these seem to be a necessity in our society. So that when life gets really rough, as it often does, some part of us can hope for some form of a gorgeous prince to come and save us from our own misery. Having hope like that doesn’t seem so wrong, which is probably why our mothers and grandmothers told us these silly stories over and over again.

In the poetical modern adaptation of Snow White and The Seven Dwarfs by Anne Sexton, however, Snow White becomes as vain as her wicked stepmother. Why? Well, because there is the potential for evil in all of us, really. Nobody fits neatly into either the good or evil category – and sometimes the heroines of our own stories are vain or ignorant and are certainly always flawed.

Snow White and the Seven Dwarfs by Anne Sexton.
```

### Performance text (classify this)

```text
No matter what life you lead
the virgin is a lovely number:
cheeks as fragile as cigarette paper,
arms and legs made of Limoges,
lips like Vin Du Rhône,
rolling her china-blue doll eyes
open and shut.
Open to say,
Good Day Mama,
and shut for the thrust
of the unicorn.
She is unsoiled.
She is as white as a bonefish.

Once there was a lovely virgin
called Snow White.
Say she was thirteen.
Her stepmother,
a beauty in her own right,
though eaten, of course, by age,
would hear of no beauty surpassing her own.
Beauty is a simple passion,
but, oh my friends, in the end
you will dance the fire dance in iron shoes.
The stepmother had a mirror to which she referred--
something like the weather forecast--
a mirror that proclaimed
the one beauty of the land.
She would ask,
Looking glass upon the wall,
who is fairest of us all?
And the mirror would reply,
You are the fairest of us all.
Pride pumped in her like poison.

Suddenly one day the mirror replied,
Queen, you are full fair, ‘tis true,
but Snow White is fairer than you.
Until that moment Snow White
had been no more important
than a dust mouse under the bed.

But now the queen saw brown spots on her hand and four whiskers over her lip so she condemned Snow White to be hacked to death. Bring me her heart, she said to the hunter, and I will salt it and eat it. The hunter, however, let his prisoner go and brought a boar’s heart back to the castle. The queen chewed it up like a cube steak. Now I am fairest, she said, lapping her slim white fingers.

Snow White walked in the wildwood
for weeks and weeks.
At each turn there were twenty doorways
and at each stood a hungry wolf,
his tongue lolling out like a worm.
The birds called out lewdly,
talking like pink parrots,
and the snakes hung down in loops,
each a noose for her sweet white neck.

On the seventh week
she came to the seventh mountain
and there she found the dwarf house.
It was as droll as a honeymoon cottage
and completely equipped with
seven beds, seven chairs, seven forks
and seven chamber pots.
Snow White ate seven chicken livers
and lay down, at last, to sleep.

The dwarfs, those little hot dogs,
walked three times around Snow White,
the sleeping virgin. They were wise
and wattled like small czars.
Yes. It’s a good omen,
they said, and will bring us luck.
They stood on tiptoes to watch
Snow White wake up. She told them
about the mirror and the killer-queen
and they asked her to stay and keep house.
Beware of your stepmother,
they said.
Soon she will know you are here.
While we are away in the mines
during the day, you must not
open the door.

Looking glass upon the wall . . .
The mirror told
and so the queen dressed herself in rags
and went out like a peddler to trap Snow White.
She went across seven mountains.
She came to the dwarf house
and Snow White opened the door
and bought a bit of lacing.
The queen fastened it tightly
around her bodice,
as tight as an Ace bandage,
so tight that Snow White swooned.
She lay on the floor, a plucked daisy.
When the dwarfs came home they undid the lace
and she revived miraculously.

She was as full of life as soda pop.
Beware of your stepmother,
they said.
She will try once more.

Looking glass upon the wall. . .
Once more the mirror told
and once more the queen dressed in rags
and once more Snow White opened the door.
This time she bought a poison comb,
a curved eight-inch scorpion,
and put it in her hair and swooned again.
The dwarfs returned and took out the comb
and she revived miraculously.
She opened her eyes as wide as Orphan Annie.
Beware, beware, they said,
but the mirror told,
the queen came,
Snow White, the dumb bunny,
opened the door
and she bit into a poison apple
and fell down for the final time.
When the dwarfs returned
they undid her bodice,
they looked for a comb,
but it did no good.
Though they washed her with wine
and rubbed her with butter
it was to no avail.
She lay as still as a gold piece.

The seven dwarfs could not bring themselves
to bury her in the black ground
so they made a glass coffin
and set it upon the seventh mountain
so that all who passed by
could peek in upon her beauty.
A prince came one June day
and would not budge.
He stayed so long his hair turned green
and still he would not leave.
The dwarfs took pity upon him
and gave him the glass Snow White--
its doll’s eyes shut forever--
to keep in his far-off castle.
As the prince’s men carried the coffin
they stumbled and dropped it
and the chunk of apple flew out
of her throat and she woke up miraculously.

And thus Snow White became the prince’s bride.
The wicked queen was invited to the wedding feast
and when she arrived there were
red-hot iron shoes,
in the manner of red-hot roller skates,
clamped upon her feet.
First your toes will smoke
and then your heels will turn black
and you will fry upward like a frog,
she was told.
And so she danced until she was dead,
a subterranean figure,
her tongue flicking in and out
like a gas jet.
Meanwhile Snow White held court,
rolling her china-blue doll eyes open and shut
and sometimes referring to her mirror
as women do.
```

---

## IC-1844: The Spark Inside You – A Collection

- Title: The Spark Inside You – A Collection
- Author (byline): Susan Griffin and Clementine von Radics
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 935
- Already set (do not supply): none

### Source block (context only)

```text
Author: Susan Griffin
Book: No More Masks! An Anthology of Poems by
Women (eds Florence Howe)
ISBN: 978-0060965174
Publisher: Harper Perennial
Date (Month/Year): Aug 1993
Author: Clementine von Radics
ISBN: 978-1449479701
Publisher: Andrews McMeel Publishing
Date (Month/Year): April 2016
```

### Introduction (context only: never use it for content warnings)

```text
Throughout history, in every culture around the world, extraordinary women have pushed society to think bigger, move forward and create. Take a historical trip with me and I’ll introduce you to a few examples of their ceaseless curiosity, boundless courage and world-changing resourcefulness. Thanks to each of them, women and girls all over the world are able to live with bigger dreams than ever before.

The Spark Inside You – A Compilation by Susan Griffin and Clementine von Radics
```

### Performance text (classify this)

```text
I Like to Think of Harriet Tubman by Susan Griffin
I like to think of Harriet Tubman.
Harriet Tubman who carried a revolver,
who had a scar on her head from a rock thrown
by a slave-master (because she
talked back) , and who
had a ransom on her head
of thousands of dollars and who
was never caught, and who
had no use for the law
when the law was wrong,
who defied the law. I like
to think of her.
I like to think of her especially
when I think of the problem
of feeding children.

The legal answer to the problem of feeding children is ten free lunches every month, being equal, in the child’s real life, to eating lunch every other day. Monday but not Tuesday. I like to think of the President eating lunch on Monday, but not Tuesday. and when I think of the President and the law, and the problem of feeding children, I like to think of Harriet Tubman and her revolver.

And then sometimes
I think of the President
and other men,
men who practice the law,
who revere the law,
who make the law,
who enforce the law
who live behind
and operate through
and feed themselves
at the expense of
starving children
because of the law.

men who sit in paneled offices
and think about vacations
and tell women
whose care it is
to feed children
not to be hysterical
not to be hysterical as in the word
hysterikos, the greek for
womb suffering,
not to suffer in their
wombs,
not to care,
not to bother the men
because they want to think
of other things
and do not want
to take women seriously.
I want them to think about Harriet Tubman,
and remember,
remember she was beaten by a white man
and she lived
and she lived to redress her grievances,
and she lived in swamps
and wore the clothes of a man
bringing hundreds of fugitives from
slavery, and was never caught,
and led an army,
and won a battle,
and defied the laws
because the laws were wrong, I want men
to take us seriously.
I am tired wanting them to think
about right and wrong.
I want them to fear.
I want them to feel fear now I want them
to know
that there is always a time
there is always a time to make right
what is wrong,
there is always a time
for retribution
and that time
is beginning.

For Teenage Girls with Wild Ambitions and Trembling Hearts by Clementine von Radics

[Anne Frank . . .]
When you are 13 years old,
the heat will be turned up too high
and the stars will not be in your favor.
You will hide behind a bookcase
with your family and everything left behind.
You will pour an ocean into a diary.
When they find you, you will be nothing
but a spark above a burning bush,
still, tell them
Despite everything, I really believe people are good at heart.

[Joan of Arc . . .]
When you are 14,
a voice will call you to greatness.
When the doubters call you crazy, do not listen.
They don’t know the sound
of their own God’s whisper. Use your armor,
use your sword, use your two good hands.
Do not let their doubting
drown out the sound of your own heartbeat.
You are the Maid of Untamed Patriotism.
Born to lead armies into victory and unite a nation
like a broken heart.

[Malala . . .]
When you are 15, you will be punished
for learning too proudly. A man
will climb onto your school bus and insist
your sisters name you enemy.
When you do not hide,
he will point his gun at your temple
and fire three times. Three years later,
in an ocean of words, with no apologies,
you will stand before the leaders of the world
and tell them your country is burning.

[Mary Shelley . . .]
When you are 16 years old,
you will invent science fiction.
The story of a man named Frankenstein
and his creation. Soon after you will learn
that little girls with big ideas are more terrifying
than monsters, but don’t worry.
You will be remembered long after
they have put down their torches.

[Jackie Mitchell . . .]
When you are 17 years old,
you will strike out Babe Ruth and Lou Gehrig
one right after the other.
Men will be afraid of the lightening
in your fingertips. A few days later
you will be fired from the major leagues
because “Girls are too delicate to play baseball”

[Sacajawea . . . ]
You will turn 18 with a baby on your back
leading Lewis and Clark
across North America.

[Cleopatra . . .] You will turn 18 and become queen of the Nile.

[Nelly Bly . . .] You will turn 18 and bring justice to journalism.

[For Teenage Girls with Wild Ambitions and Trembling
Hearts . . .]
You are now 18, standing on the precipice,
trembling before your own greatness.

This is your call to leap.

There will always being those
who say you are too young and delicate
to make anything happen for yourself.
They don’t see the part of you that smolders.
Don’t let their doubting drown out the sound
of your own heartbeat.

You are the first drop of a hurricane.
Your bravery builds beyond you. You are needed
by all the little girls still living in secret,
writing oceans made of monsters and
throwing like lightening.

You don’t need to grow up to find greatness.
You are stronger than the world has ever believed you to
be.
The world laid out before you to set on fire.
All you have to do
is burn.
```

---

## IC-1845: Stop Pretending

- Title: Stop Pretending
- Author (byline): Sonya Sones
- Work: Not specified
- Publisher: HarperCollins Publishers, Inc
- Publication date as stated: Oct 1999
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 776
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sonya Sones
ISBN: 978-0060283872
Publisher: HarperCollins Publishers, Inc
Date (Month/Year): Oct 1999
```

### Introduction (context only: never use it for content warnings)

```text
It happens just like that, in the blink of an eye. An older sister has a mental breakdown and has to be hospitalized. A younger sister is left behind to cope with a family torn apart by grief and friends who turn their backs on her. But worst of all is the loss of her big sister, her confidante, her best friend, who has gone someplace no one can reach.

Selections from the auto-biographical verse novel: Stop Pretending by Sonya Sones
```

### Performance text (classify this)

```text
My Whole Family
(Pg 3) I can
remember what
things were like before she
got sick: my whole family climbed
into

the big
hammock on the
moondappled beach, wove
ourselves together, and swayed
as one.

My Sister’s Christmas Eve Breakdown

(Pgs 4-5) One day
she was my big
sister, so normal and
well-behaved, the next she was a
stranger

rushing
out the door to
Midnight Mass, a wild-eyed
Jewish girl wearing only a
nightgown.

One day
he was my dad,
so calm and quiet and
in control, the next he was a
stranger

dragging
my big sister
away from the door, up
the stairs, screaming so loud that my
ears stung.

One day
she was my mom,
so reliable and good in
a crisis, the next she was a
stranger

standing
stock still with her
hands clamped over her mouth
and her eyes squeezed shut, not even
breathing.

That day
I sank into
the wall, wondering what
these three people were doing in
my house

and I
shouted that they
had to stop, even though
I wasn't supposed to talk to
strangers.

Three A.M. That Same Night (Pgs 6-7) She hasn't gone to Mass, hasn't gone to sleep, hasn't stopped to catch her breath -- she can't stop talking.

She's showing me her stuff,
tons of stuff she bought,
stuff she bought this afternoon
when she went shopping.

Our bedroom's filled with bags,
way too many bags,
bags crammed full with too much stuff,
they're overflowing.

She's emptying them out:
fifty bars of soap,
feather dusters, Ping-Pong balls,
a ski mask, fishbowls,

twelve pairs of sexy shoes
(the kind she never wears),
stationery monogrammed
with wrong initials.

I'm huddled on my bed,
wrapped up in my quilt,
listening to Sister rave
on and on and

just outside the door
angry whispers rise.
Trying not to let us hear,
our parents fight.

I'm huddled on my bed,
rocking in my quilt,
wishing I could fall asleep
and end this nightmare.

[And then she was . . .]
Hospitalized
(Pg 9-10) Sister's in the psycho ward
and when I visit, I glance toward
the other patients' twisted faces,
quaking fingers,
frightened eyes,
wishing I could somehow break her out of here...

Then Sister starts to scream at Mother,
telling her how much she hates her,
begging her to stop the voices
chattering inside her skull.
I'm feeling sick,
the air's too thick...

Suddenly I'm running, stumbling,
Sister's demons chasing after,
leering, laughing,
right behind me
lurching at my heels
remind me:
I could have been the one.
Run, Sister, run!
TRANSITION
And as we all do when we run, we run to a place that
feels safe. Sometimes it’s not that we are running from
something, but rather we are running to something. To a
place of safety. For Sonya Somes, that safe place was a
place of family. . . a place before. She found safety in her
Midnight Swing.

Midnight Swing
(Pg 17-18) When I can't fall asleep
I sneak out to the yard
and climb onto the swing
that's attached to a branch
of the sweet scented pine.

As I glide through the night
and I hang back my head
I see stars and a moon
that's following me
through the evergreen trees.

And I fly on my swing through the midnight ice cold as the swirling white clouds of my own frozen breath brush my tingling cheeks.

And my nightgown wafts up and my hair billows out as I float through the air and there's only the sound of the dark whooshing past.

And my thoughts drift to you on a day long ago when my legs were too short so you helped me climb up and you taught me to pump.

TRANSITION But memories fade and reality tightens its grasp on our minds and souls very quickly. When you love someone who is suffering from a mental illness, it seems at times that you will never find them again; the real person -- a mother, a father, a sister who is drowning in a pool you cannot see. You talk, you love, you try, but you just can’t reach them. It’s like they don’t even know you; and it’s so easy to give up hope. But if you are patient and persevere . . . in many cases . . . finally

Finally
(Pg 174) I fly home
from the hospital
to share the news
with my parents:

"She knew me today.
She knew who I was
and I knew her, too.
She was there. Really there.
We talked about dreams.
She braided my hair.
We sat side by side
and played 'Heart and Soul.'
Today, I hated to leave."

I hug my parents
and they hug me back,
holding tight
like feathers to the wing of a bird.
```

---

## IC-1846: The Stream

- Title: The Stream
- Author (byline): Mona Van Duyn
- Work: Letting Myself Go
- Publisher: Cengage Learning
- Publication date as stated: 2005
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 771
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mona Van Duyn
Book: Letting Myself Go
ISBN: 978-1413004731
Publisher: Cengage Learning
Date (Month/Year): 2005
```

### Introduction (context only: never use it for content warnings)

```text
Every woman has stories to tell about her mother. The mother she has, the mother she wants, the mother she misses, the mother she didn't know. We carry our mothers with us. Sometimes we carry her in our hearts, in our heads-or on our backs. Sometimes we are connected to our mothers with the thick, strong cords of intertwined love and true acceptance; other times the bonds are stretched thin and taut, scratching against our consciousness, rubbing raw the sore spots in our souls. But we are always linked to our mothers: both to the dreams of the mothers we wish for and the realities of the mothers we have. Even if our mother has been gone for years-for decades-the relationship is still very much alive. The Stream by Mona Van Duyn
```

### Performance text (classify this)

```text
Four days with you, my father three months dead. You can’t tell months from years, but you feel sad.

And you hate the nursing home. I’ve arranged a lunch for the two of us, and somehow you manage to pinch The pin from Madrid I bought you closed at the neck of your best red blouse, put on new slacks, and take

off your crocheted slippers to put on shiny shoes, all by yourself. “I don’t see how you could close

that pin. You look so nice!” “Well, I tried and tried, and worked till I got it. They didn’t come,” you said.

“Mother, I’m sorry, this is the wrong day, our lunch is tomorrow. Here’s a big kiss anyway

for dressing up for me. The nurse will come in “ tomorrow and help you put on your clothes and pin.”

“These last few days her mind has certainly cleared. Of course the memory’s gone,” your doctor said.

Next day they bathed you, fixed your hair and dressed you up again, got a wheelchair and wheeled you past the fat happy blabber of nonsense who rolled her chair all day in the hall, the silent stroller who wore

a farmer’s cap and bib overalls with rows of safety pins on the bib, rooms of old babies

in cribs, past the dining hall, on down to a sunny lounge in the other wing. “Where can I pee,

if I have to pee? I don’t like it here, I’m afraid. Where’s my room? I’m going to faint,” you said.

But they came with the lunch and card table and chairs and bustled and soothed you and you forgot the fears

and began to eat. The white tablecloth, the separate plate for salad, the silvery little coffee pot,

the covers for dishes must have made you feel
you were in a restaurant again after all
those shut-in years. (Dad would never spend the money,
but long ago you loved to eat out with me.)

You cleaned your soup bowl and dishes, one by one, and kept saying, “This is fun! This is fun!”

The cake fell from your trembly fork, so I fed it to you. “Do you want mine, too?” “Yes,” you said,

“and I’ll drink your milk if you don’t want it.” (You’d lost twelve pounds already by refusing your food.)

I arranged for your old companion, who came twice a day, to bring you milkshakes, and reached the end of my stay.

On the last night I helped you undress. Flat dugs like antimacassars lay on your chest, your legs

and arms beetle-thin swung from the swollen belly (the body no more misshapen, no stranger to see, after all, at the end than at the beloved beginning). You chose your flowered nightgown as most becoming.

You stood at the dresser, put your teeth away, washed your face, smoothed on Oil of Olay,

then Avon night cream, then put Vicks in your nose, then lay on the bed. I sat beside your knees

to say goodbye for a month. “You know I’ll call every Sunday and write a log. Try to eat well—“

Tears stopped my voice. With a girl’s grace you sat up and, as if you’d done it lifelong, reached out to cup

my face in both your hands, and, as easily as if you’d said it lifelong, you said, “Don’t cry,

don’t cry. You’ll never know how much I love you.” I kissed you and left, crying. It felt true.

I forgot to tell them that you always sneaked your meat, You’d bragged, to the man who ate beside you. One night

at home, my heart ringing with what you’d said, then morning, when the phone rang to say you were dead.

I see your loving look wherever I go. What is love? Truly I do not know.

Sometimes, perhaps, instead of a great sea, it is a narrow stream running urgently

far below ground, held down by rocky layers, the deeds of mother and father, helpless sooth-sayers

of how our life is to be, weighted by clay, the dense pressure of thwarted needs, the replay

of old misreading, by hundreds of feet of soil, The gifts and wounds of the genes, the short or tall

shape of our possibilities, seeking and seeking a way to the top, while above, running

and stumbling this way and that on the clueless ground, another seeker clutches a dowsing-wand

which bends, then lifts, dips, then straightens, everywhere, saying to the dowser, it is there, it is not there,

and the untaught dowser believes, does not believe, and finally simply stands on the ground above,

till a sliver of stream finds a crack and makes its way, slowly, too slowly, through rock and earth and clay.

Here at my feet I see, after sixty years, the welling water – to which I add these tears.
```

---

## IC-1847: The Subtle Art of Breathing

- Title: The Subtle Art of Breathing
- Author (byline): Asha Bandele
- Work: Not specified
- Publisher: Moore Black Press
- Publication date as stated: July 2005
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1135
- Already set (do not supply): none

### Source block (context only)

```text
Author: Asha Bandele
ISBN: 978-0965830881
Publisher: Moore Black Press
Date (Month/Year): July 2005
```

### Introduction (context only: never use it for content warnings)

```text
The Subtle Art of Breathing by Asha Bandele
```

### Performance text (classify this)

```text
in the middle of everything i’m not doing my doorbell rings it’s the landlady’s lost son i point him up the stairs mildly annoyed to have been interrupted from my intent viewing of a soap opera one life to live ironic now that i think about it.

nobody ever suspects women like me poets politically conscious watch soap operas but we do at least I do grateful to retreat into the fictitious chaos of somebody else’s life

but this is not a poem about soap operas It’s just that I cannot find another way to begin I mean how would you do it?

would you start with a father’s scream lancing the air with the little sister’s indelicate weep or the acidic gurgle of a stomach self-destruction maybe you would simply begin like a broadcast journalist scanning a teleprompter: in anchorage today a 30 year old black woman was found in her apartment dead of an overdose. The incident has been ruled a suicide . . .

but this is not a poem about how to begin a poem
or a poem about lost sons and landlady’s
this is not a poem about soap operas
in islam they say from Allah we come to Allah we return
leaving the curious among us hungry
for the story in between arrival and
departure the person in the center the thin arms
desperate
to stop the steady crush of closing walls her first
wall was daughter
her second was wife not much room there to just be a
woman
holy or unholy
but this is not a poem about religion

there are people who have accused me of creating the various & sundry crises in my life there are people who have accused me of refusing joy & of blanketing the sun but then there are people who know as I know that even as we laugh we cannot ignore the wincing in our eyes we are not crazy or invested in sadness sister was it that you knew there was no space to be second best or needy in a country swallowing up the earth from the inside out they incinerate their own children here i have seen the scraping their own 8 year olds into garbage bags or compactors whatever’s efficient &

it might be that this is a political poem

forgive me i feel guilty borrowing your family’s pain you were not my daughter not my sister i never even met you your name & troubles were a footnote at the end of a discussion on lovers and where to go for dinner that night i know this space of mourning is not mine to occupy but i cannot leave your life reads like the details of my life & i must know why you are dead I am not yet we both were 30 black female & fighting histories of drugs violence separation loss start stop start stop again We are a ritual of everyday blackwoman experience stories repeated on sally & Geraldo ricki lake & the news Nothing unusual been there done that &

maybe this is a poem about déjà vu or a poem about phyllis hyman or billie holiday maybe this is a poem about my grandmother or your best friend from back in the day maybe this is a poem about you but it is definitely not a poem about invented crises fictitious lives or retreating pretending lying turning away or even praying

this is not a poem about soap operas.

Once i was told that i was more than all of my hurting added up together if i had known you i would have told you that too girl there was more to you than your violent marriage more than the brown girl you became crouching beneath the dining room table more to you than the baby you lost or the last time you or any one of gave ourselves up Like unwilling virgins to cocaine vodka tonics cheap wine newports colombian gold & beer when the money got tight girl there was clear skin beneath your bruises muscle behind the split ribs a raving beauty beyond his broke up sight & screams & did you ever see here even once & if i did & if i told you we were the same woman sisters maybe twins would you have been able to hear me

was this the first time you felt powerful? did you feel finally some control did you say to yourself can’t be yanked out from under this table gotta hiding place that [he] won’t never find me in did you think at last a truth no one will ignore that the world will believe you now i just remember feeling very calm

as i slid into pieces of the splintered wood of my dormroom floor all those years ago you know what would have happened if you had survived been surprised by somebody coming back in after the 18th pill? you would have tried to fight them as they tried to make you walk they would have dragged you up & down the floors til the ambulance arrived someone would have slapped you to keep you awake whoever found you might have read your journals displayed your diaries said they just wanted to understand at the hospital if you arrived conscious they would have made you eat a black chalk substance to induce vomiting you would have vomited uncontrollably in front of you they would have stirred through it picking out the pills for analysis there is no other way to say this besides i told you

this is not a poem about soap operas but

this may be a poem that warns breathing is a difficult and subtle art it may be a poem to say simply i understand sister after 3 attempts years past the last one i understand girl i think this is a poem that wants to assert itself i’m proud even glad that i’m a survivor & sometimes when i am quiet & sometimes when i am alone & sometimes when i am reflective & sometimes when i am scared & sometimes sometimes when i am watching soap operas i say oneday i’m gonna be even more than a survivor i’ll be a celebrant inside myself party girl in my own soul i’ll take myself out to fancy restaurants bring me roses then make love to myself & in the heat of passion call out my own name (asha, asha . . . ) yes i’m gonna marry myself does that sound crazy?

martin luther king said we may not get there together but we as a people . . . & What if i do girl? Get there & find myself dancing wild in a bright silver dress & high heeled shoes will you come too ok not now but your next time around be your own sensual dance partner in high heeled shoes fine as hell girl & so so so fulla life
```

---

## IC-1848: Tell the Black Girls We Believe in Their Magic

- Title: Tell the Black Girls We Believe in Their Magic
- Author (byline): Lamont Lilly and Jasmine Mans
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1078
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lamont Lilly
ISBN: On-Line Transcript
Website:
https://www.newblackmaninexile.net/2016/05/tell-black-
girls-and-other-poems-by.html
Publisher: New Black Man In Exile.net
Date (Month/Year): May 6, 2016
*Website Notes poem was to be published in Honor in the
Ghetto (Fall 2016) – Cannot confirm publication
Author: Jasmine Mans
Book: Black Girl, Call Home, Pg 190-193
ISBN: 978-0593197141
Publisher: Berkley
Date (Month/Year): March 2021
Author: Jasmine Mans
Book: Black Girl, Call Home, Pg 194-197
ISBN: 978-0593197141
Publisher: Berkley
Date (Month/Year): March 2021
```

### Introduction (context only: never use it for content warnings)

```text
Today I pay tribute to 2 amazing black women through the poetic lens of Jasmine Mans: Serena Williams and Michelle Obama. Believe in their magic . . . for it is real.

Since her tennis debut in 1995, Serena Williams has won 23- time grand slam singles, four Olympic gold medals and is considered one of the greatest athletes of all time. Williams and her career have meant so much to me because she is and has always been unapologetically Black. In a world that often makes it seem as though Blackness and success are mutually exclusive; she is a shining example of what is possible. Of course, her success didn’t shield her from racism – in fact, she refused to play in one tournament after receiving a ton of racial abuse from the crowd in 2011. But the way she handled the prejudice levelled at her taught me an invaluable lesson. Racism can be a footnote in an epic story of achievement – not a main theme or chapter. Serena Williams is and will forever be one of the most influential Black women on the planet.
```

### Performance text (classify this)

```text
tell the black girls we believe in their magic.

tell the black girls
how they were born
from a long tradition
of black woman dream merchants
miracle makers
and super heroes.

tell the black girls
how special powers
are interwoven
in their braids and cornrows.
god gifted
in the tips
of their twists and locs.
tell the black girls
how the others
can only dream
and imagine their powers.

tell the black girls we believe in their magic and it’s real.

Serena by Jasmine Mans (Pg 190-193)

They will ask you to run, and when you become the fastest

they will fear your lightning, how it cracks ceilings and breaks ground. They will place rules on your body, say it’s a distraction from their game, as if they know better than you

how your bones should wear your own body, how you should dress up in your own skin.

They don’t know why your hair

needs extra bobby pins, or how you got the biggest booty in tennis,

something about Compton and collard greens. They will not be graceful with your body, but you will always have to be.

When they put you against your own sister,

she’ll sharpen you. Passersby will attack your

character, Serena smashes racket,

point penalty,
violation,
how will she ever come back from this one,
she is too aggressive,
she has gone too far with her

clothing, how can Serena possibly regroup from this, fight back, women do not yell, women do not take their shirts off, Serena loses the match and is fined $17,000,

we cannot allow her to get too out of control.
Women are not allowed real emotion
in tennis,
in the street,
in the office,
In their skin.
Serena, lean in

more power, use more power, backhand,

back! Backhand, Serena!

More! More follow through!!
Take the net, Serena,
be tuff,
be tuff.

Act like you want to win.
Forward!
Forward!
Back,
back,
back,

you got this Serena, net, net

net, Serena,
yes!
Power, Serena,
play to win!!
What does it feel like
to prepare your body for the
US Open,
Australian Open,
to be cut open.

And to still give them grace, even when they call you names,

even when they paint your face, you give them grace.

Without fear, doubt, or discomfort, what else is there to overcome?

You’re sport,
not spectacle,
woman before
competitor
When they walk
You fly

when they grunt, you roar.

You are a fire catching its breath.

You embrace failure, never run from it.

We’ve already
watched you defy
gravity
but today,

today, you will become it.

TRANSITION

Tell the Black girls . . . And perhaps no one spoke to our hearts more clearly than First Lady Michelle Obama when she talked about the universal challenges that black women face every day: “. . . there are voices that tell you that you’re not good enough. That you have to look a certain way, act a certain way. If you speak up, you’re too loud, if you step up to lead, you’re being bossy. But I decided I wasn’t bossy. I was strong. I wasn’t loud. I was a young woman with something important to say.” * What makes us diverse isn’t something to diminish, but to celebrate.

Dear First Lady (for Michelle Obama) (Pg 194-197)
Dear First Lady,
I watched as my 4-year old cousin,
as she sat in the mirror,
placed my grandmother’s pearls
around her neck and said,
“Do I look like Michelle Obama?”

This little girl
who does not know how to say
Rice Krispies or macaroni and cheese,
properly said your name
as if it existed in her long list of heroes
in between Snow White and Santa Claus.

My little cousin does not know Jim Crow.
How to interpret the Constitution
or fight for human rights,
she does not know your views
on health care reform,
your Princeton education,
nor can she point to Chicago on a map.

But she knows Black Barbie dolls and nap time,
how to identify your face in a land-field
of misrepresented women
who share our skin color
like a sequin revolution.

She knows your smile, Michelle,
she knows the day
her mother jumped up and down
crying,
November 4th’s
black and red dresses,
how to say how to say
“African American”
better than her own first name.

You proved that her identity belongs somewhere in this American dream. She knows that if she can find your face in the jumbled channels on television there’s a possibility she can stay up past her bedtime.

You are everything
her mother never got the chance to be,
Cover Girl’s Beauty of the Week,
a love story sprinkled
in an inaugural speech,
a woman
she can mistake for her mommy.

She traded in her Dora the Explorer costume for a brooch of the American flag, and a tee shirt with your husband’s face on it.

And for the first time
I could identify the revolution
that would actually change the world.
And it’s not in how many Barack and Martin
comparisons we can make,
but the idea of little boys
jumping off their bunk beds
actually believing that they can fly.

It’s in little girls with dreams
and their grandmother’s pearls.
My little cousin doesn’t know
about the war in Iraq,
she just wonders if Sasha and Malia
like to Hula-Hoop
and if you force them to eat
their Flintstones vitamins too.

Thank you for being a brown girl’s dream come true, something tangible to look up to.

I know that our skin color
exists on time lines
of women who had craters
engraved in their backs.

Stretch marks similar to maps
of underground railroads.
Grandmothers who couldn’t afford
all the ingredients to the American pie.

Women who laid down their lives,
strutted with chips and cracks
in their spines,
dying to inject more estrogen
in “man’s kind.”

Creating tradition under the idea
that if I can’t afford my daughter the world,
a college degree,
or at least, a decent meal tonight.

I’ll wrap my grandmother’s pearls around her neck like a gravity-stricken halo

and I’ll whisper in her ear

“Baby,
if I can’t,
you will . . .
. . . she did.”

*(From the 1st poem)
tell the black girls
we believe in their magic
and it’s real.

*Transition Quote Source Remarks by the First Lady at BET’s “Black Girls Rock!” Event, March 28, 2015, New Jersey Performing Arts Center, Newark, New Jersey https://obamawhitehouse.archives.gov/the-press-office/2015/03/28/remarks-first-lady-bets-black-girls-rock-event
```

---

## IC-1849: Thanks, Nurse

- Title: Thanks, Nurse
- Author (byline): Diane Carlson Evans
- Work: Visions of War, Dreams of Peace
- Publisher: Grand Central Publishing
- Publication date as stated: May 1991
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 747
- Already set (do not supply): none

### Source block (context only)

```text
Author: Diane Carlson Evans
Book: Visions of War, Dreams of Peace
ISBN: 978-0446392518
Publisher: Grand Central Publishing
Date(Month/Year): May 1991
```

### Introduction (context only: never use it for content warnings)

```text
When Diane Carlson Evans, a former army nurse in Vietnam, first saw the Vietnam Veterans Memorial, she felt something was missing. Her efforts to highlight the service of women in Vietnam were rewarded on November 11, 1993, when the Vietnam Women's Memorial was dedicated. The women's war was different from the men's -- instead of exploding in the jungle, it blew up in the mind. Surrounded by death, the nurses had to shut down emotionally. They could not show their feelings to the soldiers they were trying to heal. Thanks, Nurse by Diane Carlson Evans.
```

### Performance text (classify this)

```text
November 13th, 1982
I stand beside the Vietnam Veterans Memorial.
Pleiku, is written on my wrinkled jungle hat, and
71st Evacuation Hospital, Vietnam.
Wearing it today feels natural
Even with a skirt and among strangers.
Thirteen years ago it found its place
In a foot locker with worn out combat boots,
Fatigues, a malaria net and poncho liner.
Strange memorabilia for a young woman of 22 years.
A foot locker filled with memories
Of a lifetime of one year and
Locked away, forever - I had hoped,
Until today.

"Thanks, Nurse," that day in Washington. D.C.
You, with your boonie hat and
Faded camouflage
Threw your arms around me, and said
"Thanks, nurse, I never had a chance to say that"
The tears rolled down my face,
Don't make me cry,
I've passed thirteen years without a tear.
Please, don't remind me of sadness
With that look on your face.
My soul was overwhelmed with
Emotion I hadn't felt
Since leaving that faraway war
In 1969.
"You nurses saved our lives, you know, we
Love you,"
My tears are uncontrollable, and
I am as much with the
Dead as with the living.
Facing the sall, I encounter
Something I left behind me so many
Years ago.
I am at that moment lifted away
And reunited with those who suffered
And died and had left me
Alone.
Left me alone, with the memories of them.
And left me too numb to dry.
As I put my hands on the hard granite
And touched the names of those who
Died, 1968-'69, I no longer
Felt alone.

Those who had died, came back at that moment, Allowed me to grieve, embraced me And touched a part of my Soul I had thought was gone. That vague place in my Life, Vietnam, which could not bring forth Emotion or feelings Or tears. It was such a relief to cry now, to Feel again. It was so strange. I felt unbearable sadness, and yet Set free - free of an intangible Burden.

That beautiful black granite
Wall, now carries the burden
For me
And for us all.
It carries the names and souls,
The memories, of those who died
In Vietnam.
It shelters them with respect
And dignity.

"Nurse, I don't want to die here," they would say
"Will I make it home? Oh God, don't let me die here."
That look in their eyes - so young, so serious,
Please don't make me remember.
The longing for home among the
Wounded was so strong.
We worked so hard to "get them home."
And thousands we did,
But for those who died we were
Sorry they couldn't have their last wish.

It would not have been their
Last wish - to be on this wall
Their life had just begun -
"Nurse I want to get home."

Now they are home and
Are again with their fallen
Friends.
The memorial that honors the living
And the dead, by giving us
a Place
To join together.

To you in your faded camouflage And boonie hats and Green berets, I want to say Thank you" too, from someone who Cared for you in Vietnam, and Still cares today. "Thank you too" For you see, you, and this wall Set me free Free to cry and free to remember, What I had hoped to forget And found I could not.

If our country could have known
But one dying man, alone in Vietnam
With that look on his face
And hopelessness in his eyes
If this country could have seen
The courage he had and concern
For his friends
If this country could have
Wept in his tears
And told him he was good.
If only, this country would have
Listened - listened and learned of his
Experience and his sacrifice
And then told him they were
Proud. If only there would have been
"Thanks."

We sacrificed our youth
I'm not sure why
How does one explain, to those
Who didn't go
The fear, the suffering, the inhumanity,
It's not what we wanted
To have names on this wall,
Or to visit a Place such as this but
It was a real war
And we are real veterans.

Now this country has wept
In our tears from that era
By watching us stand proudly, honorably, beside
The Names, our comrades.
Sons and daughters at war do not know why
They are chosen ones to sacrifice.
But we stand proud and we will not
Let our nation forget our
Comrades.
```

---

## IC-1850: There was Once a Little Girl – A Collection

- Title: There was Once a Little Girl – A Collection
- Author (byline): Jessica Jocelyn
- Work: Stars at Last (SAL)
- Publisher: Jessica Jocelyn Poetry
- Publication date as stated: Sept 2024
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1062
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jessica Jocelyn
Book: Paper Flowers: Poetry on the Mother Wound (PF)
ISBN: 979-8990868625
Publisher: Jessica Jocelyn Poetry
Date (Month/Year): Aug 2025
Author: Jessica Jocelyn
Book: Stars at Last (SAL)
ISBN: 979-8987930588
Publisher: Jessica Jocelyn Poetry
Date (Month/Year): Sept 2024
```

### Introduction (context only: never use it for content warnings)

```text
From the trembling perspective of a daughter who wanted nothing more than to be loved -- these poems breathe in the quiet terror of growing up too carefully; of learning when to speak, when to disappear, and how to make yourself small enough to survive your mother’s pain.

There was Once a Little Girl – A Collection of poems from Paper Flowers and Stars at Last by Jessica Jocelyn
```

### Performance text (classify this)

```text
(PF, Pg 3) Welcome to childhood,
where the monsters under your bed
are the least of your problems.
Where the real ones sleep in the next room,
and you learn to breathe more quietly
when they’re angry.
Where your tears are unwelcome,
and ‘I love you’ comes with conditions.
Where you mistake fear for respect
and silence for safety.

Welcome to childhood, where you never meet the child you were supposed to be.

(PF, Pg 4) There was once a little girl made of paper raised by a mother with scissor hands.

Everyone was quick to misunderstand her.

They didn’t know love and hate
felt the same to her.
They didn’t know what it was like
to run to be held
only to be left in shreds.

So they labeled her as the bad seed. Her cries for help were mislabeled as being difficulty.

And so
She drifted through life like a ghost
in a body that remembered
every time she was torn
and told it was love.

(SAL, Pg 75) if you ask me about my mom, I will just shrug and say we don’t talk.

But if you look into my eyes,

They will tell you that I never outgrew the little girl who always wanted her mother. When my heart broke for the first time, when I had a positive pregnancy test . .

I always wanted her.

I wanted her hand to be there on my arm, to tell me she knew what it felt like and that I would make it to better days.

I could never outrun the little girl who cried out for her until my lungs collapsed, until my knees bled from being on the ground for so long.

They will tell you that inside, I will never stop being the little girl who reaches out for her.

(PF) I wasn’t just the eldest daughter.
I was the shield,
the mouthpiece,
the stand-in mother.

I wore those roles so well that
they forgot I was a child.
And eventually
so did I.

(PF) How to be good to your mother:

Mirror her pain but don’t outshine it
try to heal her
try to save her
carry her wounds like heirlooms
smile pretty for the pictures
let her take credit
never say what really happened
protect her reputation
shrink when she gets loud
thank her for the bare minimum
become the daughter she could love.

(PF, Pg 6) She loved me once.
When I was warm and brand new,
smooth on her chest.
Smelling of all her hopes and dreams.

She loved me sometimes.
When I started to grow,
I brought a new fear into her heart --
the one where I might leave someday.

She loved me when I wasn’t a mirror. When she could look at me and not see the girl she never got to be.

(PF) If I run far enough, will I still be someone’s daughter? Will my name be spoken in whispers, Or worse, not spoken at all?

If I stay away long enough, can I be erased by time?

Can I slip between the cracks so far that I void the blood that ties us?

I’m not sure what it feels like to be loved, but I don’t think it’s supposed to feel like this. I don’t think my feet should be scarred from walking on eggshells.

(PF) I can’t bleed in the name of
‘Honor your parents.’
I can’t disappear in the name of
‘That never happened.’
I can’t keep dying in the name of
‘You’re being dramatic.’

(PF) They say it’s in my blood,
that I was born this way.
I was wired wrong,
fused from my mother’s sadness
and my father’s violence.

But I remember the nights
she would scream at the walls
that never gave her peace.
the way I watched
instead of slept,
memorizing her storms
so I’d know how to survive mine.

They say it’s nature, But I know it was nurture too.

How can a child raised in fire not grow flames of their own?

(SAL) my mother’s rage bounced off the walls in our house and hid in all the dark corners.

It would fester in the walls and start to eat them like mold.

She was always angry but there was never a fire in her yes, only a dark, cold, emptiness

(PF) my mother was judge, jury and executioner.

Once you were sentenced, you were rotten flesh decaying under six feet of dirt.

No one could hear you, no one could smell you, no one could even say your name.

To acknowledge your existence would mean you were against her.

And if you went against her, she could make you disappear.

(PF) In other life and time,
I could save my mother.
I’d pull her from the fire
before it reached her heart,
teach her that softness isn’t weakness.
that love doesn’t have to hurt to be real.

I’d braid her hair and tell her she’s safe, hold her while she cries for the childhood she lost.

I’d rewrite the story before it wrote her, before she wrote me with the same ink.

Maybe then, we could have found each other whole.

(PF) Mom, Can I please be little again? Undo the years that taught me my voice never mattered.

Mom, just this once,
sing me to sleep with a lullaby
and maybe I’ll wake up in
a world where your love
is louder than your pain.

(SAL) my mother placed her pain in my palm and clasped her hands around mine.

‘this was given to me by my mother. it was a gift and now I’m giving it to you. to be a woman is to inherit pain.’

I carried that pain with me for many years. one day, I was rocking my brand-new baby daughter to sleep. her face on my chest, being soothed by the sound of my heartbeat.

I took the pain from my pocket and swallowed it whole. I could feel it burning my stomach.

I will gladly feel the pain for the rest of my life if it means I can’t ever give it to my daughter.

I will never know what it is like to have my mother protect me.

but my daughter will.

(SAL) yes, you are still my mother, and you always will be.

But, I’ve always been your daughter.

I can forgive that you didn’t know
how to love me.
but, I can’t forget that you didn’t even
want to learn how.
```

---

## IC-1851: There’s Been a Slight Mistake – Rehab 3 A.M.

- Title: There’s Been a Slight Mistake – Rehab 3 A.M.
- Author (byline): Ally Sheedy
- Work: Yesterday I Saw the Sun
- Publisher: Summit Books
- Publication date as stated: Feb 1991
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 845
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ally Sheedy
Book: Yesterday I Saw the Sun
ISBN: 978-0671731304
Publisher: Summit Books
Date (Month/Year): Feb 1991
```

### Introduction (context only: never use it for content warnings)

```text
Ally Sheedy, famous for her roles in The Breakfast Club and St. Elmo’s Fire back in the 1980’s, had a live that wasn’t always sunshine and roses. She suffered from recurrent bouts of bulimia. She had an abortion at 16. She was addicted to drugs and contemplated suicide. Finally, in 1989, a group of friends led by Demi Moore handed her an airplane ticket to the famous Hazelden Foundation rehab clinic in Minnesota. It was there that she learned to rely on her poetry as a way of understanding her turbulent emotions. But at first . . . at first . . . she was convinced There’s Been a Slight Mistake . . . Rehab at 3 AM by Ally Sheedy.
```

### Performance text (classify this)

```text
There’s been a slight mistake, Miss
I don’t know where I am
See, the last thing I remember
We were in some L.A. traffic jam –
(God, who the hell was that I was with?)
Anyway –
I think there was an airplane and a Xanax and some chips –
oh, God – and
YES
a Rolling Stone – (whew!)
and a Halcion and –
SEE! – of course, all over me, these
cherry ice cream drips.

I remember now. I was going on a trip! . . . going . . . . . . somewhere . . . with . . . someone – who? . . . I’m losing

it . . .
. . . and . . . THEN . . . .
ummmmm – there’s been a slight mistake, Miss . . .
Is this the office of Hazelden?

OH SHIT. OK – OK.
I’ll laugh. I get it.
Jokes are going down.
AHA! Oh, God, it’s funny now!
My L.A. friends are crazy clowns!
I mean, I don’t belong here. And, as you see, I’m fine.
Do you have some Tylenol 3? I’ve had a hell of a time.

Well – HA! Looks like we’ve both been had!
Can you call me a cab? RIGHT NOW!?!!
I have important meetings soon and
I-AM-GETTING-MAD
I’m not signing shit, Miss Nurse. Will you pick up the

goddamn phone? I’m telling you – there’s been a slight mistake and I am going home!

Excuse me. I just lost my temper.
Do you have some water or soda?
And, nurse, you still aren’t calling, nurse.
(You’re the kind of controlling bitch I keep meeting in

CODA)

Please just tell me where I am . . . where? . . .
. . . you must be loaded . . .
There is no way that I can be I fucking
Central City Minnesota!

I DON’T HAVE A DRUG PROBLEM.

It’s all a slight mistake, nurse-Bitch.
(God, I’m hot)
I never had any kind of a problem –
Demi, you little witch
Excuse me. I just got angry there.
God, it’s hot. My eyeballs itch.

Nurse, there’s been a slight mistake.
It’s all a little trick.
We both know those beds belong to addicts –
Who are – you know –
Really sick.

What? Me? Oh, no, not addiction, miss Nurse. Cause I never shot a needle in my vein. I could use, maybe, a hit of Valium, though To kill this FUCKING red pain.

NOW, RATCHETT, NOW.

Sorry. I don’t mean to sound crude.

I could use a little help here and,
you’re being very rude.
I’m not supposed to be here.
There’s been this slight mistake.
Someon’es out to do me in and
I have too much career at stake.
Listen, Nurse, you gotta hear –
Yes, hon, you’re being polite –
please, babe,
the Valium is just my way to lessen
my creative artist’s fright.

I was never meant to come here, really. --and I would never use drugs. But before I go, can you suck out my veins? They’re crawling with thousands of bugs! OK, fine, don’t help me, Nurse, I’m not staying in this hellhole place. You don’t get me at all, do you? I can see it in your nasty old face.

So can you just let me use that phone?
No?
Can you just give me some aspirins in a glass?
And will you get those fuckin rehab forms away from me –
I AM CLAM --
Before I shove them up your ass?

That was my beginning at Hazelden
and I’m glad I stayed that night
I’m sorry I broke that door down and ran
I feel like that nurse helped me save my own life.

Lately she’s even smiled at me when I’ve come into Med.
for my drugs
Still I pray every day to awaken released
from the itching of
crawling black bugs.

I guess I’ve decided that this isn’t jail –
It’s more like a “drug camp,” they’ve said –
I’m even starting to love the strange lumpy pillows
on my own
seldom slept-in bed.
And something happened suddenly.

Yesterday I saw the sun.
Something in my head had cleared
And I realized there was one.
I stopped in its Light
“I am here!” I screamed. “I’m alive!”
and fuck it
I let those tears run
I’m gonna get back and I’m gonna get through
“I’m gonna make this” I said to no one.
So I kept walking and thinking about what drugs ad my

sickness
From somewhere in the bushes I was hearing heaving sighs had done
And realizing they came from me
I took a breath
and closed my eyes.
I breathed in the River
Breathed the trees
Breathed all around the sky
and in the wind I breathed my God
Who had not let me die.
I’ve been very tired; it’s been a long time
Since I’ve really known where I’ve been
My heart started pounding and beating with love
Aliveness was just flowing in
and that certain faces
like Alec’s and Jane’s and Demi’s
were like God and my sun
And all my friends who spoke ad cared and broke my heart

to intervene And those who have been there: junkies and dealers and

drunks
who believe in me
I breathed them inside me
every one
and all that my own Higher Power has done.

Excuse me, Miss; excuse me nurse
There is no slight mistake been done
I opened up my rehab door and knew
that home was truly where I’d come.
```

---

## IC-1852: A Tribute to Emmett Till

- Title: A Tribute to Emmett Till
- Author (byline): Marilyn Nelson and Dominique Christina
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1282
- Already set (do not supply): none

### Source block (context only)

```text
Author: Marilyn Nelson
ISBN: 978-0618397525
Publisher: Houghton Mifflin
Date (Month/Year): April 2005
Author: Dominique Christina
Book: They Are All Me
ISBN: 978-0692460009
Publisher: Swimming with Elephants Publications
Date (Month/Year): July 2015
```

### Introduction (context only: never use it for content warnings)

```text
The brutal abduction and murder of 14-year-old Emmett Till on August 28, 1955, galvanized the emerging Civil Rights Movement. Till was visiting relatives in Mississippi when the fourteen-year-old was accused of whistling at Carolyn Bryant, a white woman who was a cashier at a grocery store.

Four days later, Bryant's husband and his half-brother kidnapped Till, beat the teenager brutally, dragged him to the bank of the Tallahatchie River, shot him in the head, tied him with barbed wire to a large metal fan and shoved his mutilated body into the water. The men were tried for murder, but an all-white, male jury acquitted them.

A Wreath for Emmett Till by Marilyn Nelson and Strange Fruit by Dominique Christina
```

### Performance text (classify this)

```text
A Wreath for Emmett Till by Marilyn Nelson III

Pierced by the screams of a shortened childhood, my heartwood has been scarred for fifty years by what I heard, with hundreds of green ears. That jackal laughter. Two hundred years I stood listening to small struggles to find food, to the songs of creature life, which disappears and comes again, to the music of the spheres. Two hundred years of deaths I understood. Then slaughter axed one quiet summer night, shivering the deep silence of the stars. A running boy, five men in close pursuit. One dark, five pale faces in the moonlight. Noise, silence, back-slaps. One match, five cigars. Emmett Till’s name still catches in the throat.

IV Emmett Till’s name still catches in my throat, like syllables waylaid in a stutterer’s mouth. A fourteen-year-old stutterer, in the South to visit relatives and to be taught the family’s ways. His mother had finally bought that White Sox cap; she’d made him swear an oath to be careful around white folks. She’s told him the truth of many a Mississippi anecdote: Some white folks have blind souls. In his suitcase she’d packed dungarees, T-shirts, underwear, and comic books. She’d given him a note for the conductor, waved to his chubby face, wondered if he’d remember to brush his hair. Her only child. A body left to bloat.

V
Your only child, a body thrown to bloat,
mother of sorrows, of justice denied.
Surely you must have thought of suicide,
seeing his gray flesh, chains around his throat.
Surely you didn’t know you would devote
the rest of your changed life to dignified
public remembrance of how Emmett died,
innocence slaughtered by the hands of hate.
If sudden loving light proclaimed you blest
would you bow your head in humility,
your healed heart overflow with gratitude?
Would you say yes, like the mother of Christ?

Or would you say no to your destiny, mother of a boy martyr, if you could?

*NOTE: The complete text of A Wreath for Emmett Till consists of 15 sonnets – this compilation uses only an excerpt of 3 of the 15.

TRANSITION In an interview, Dominique Christina explained . . . “Poetry is storytelling. Stories are medicine. They’ve always been. Stories are so critical. I tell you the story of Emmett Till as a way for you to locate your own humanness, find yourself inside it somewhere. We know each other and stories facilitate that better than anything else.” Strange Fruit by Dominique Christina Strange Fruit (For Emmett Till) by Dominique Christina

"Southern trees bear a strange fruit. Blood on the leaves and blood at the root."

In this photo he's laughing and
there's no cotton gin tied 'round his waist.
He's not stretched into swollen limbs.
His eyes are still hazel and
recognizable, two neat white rows of perfect teeth
sit totem-like in his mouth and
the world didn't know him because
he'd not been murdered yet.

He's still slipping into the kitchen to
get another piece of cornbread
while his mama ain't lookin'.
He'll mash it with his fingers,
drink some buttermilk and laugh
with his eyes and they're still hazel
and bright like stars in uppercase and
ain't nobody gouged 'em out
or shut 'em closed and when he goes
to school he'll do a silly dance with his
arms and legs cocked out in odd angles and
his classmates will laugh and there'll
be no cotton gin tied 'round his waist.

"Pastoral scenes of the gallant south, the bulging eyes and the twisted mouths..."

In this photo he's proud of the hat on his head.
You can see that by how straight his neck is
and his mama's in the picture and they got the same
face and his head's high and perfect and
ain't no bullet in it and it'll be months before there is
one
and in those months he's his mother's child,
the smug and overfed man-child all southern
women love to cook for and dote on cuz he
licks the plate clean even if it's leftovers.
He just eats and yes ma'ams and makes you giggle
so much you got to shoo him out the kitchen
just so you can get the pots clean and
he's breathing and whole and
ain't no men dressed like midnight with
yellow teeth and sunless un-laughing eyes
snatching him out the door
changing everything when neither of 'em
asked to be anything other than
laughing in the kitchen with
the greens still simmering in the pot.

"Here is a fruit for the crows to pluck..."

This last photo's a holocaust.
The one history concretized into
the nighttime musings of black children
who hopscotched above and below the bible belt,
who saw a tattered other worldly version of
the 14 year-old Emmett,
his head poised strangely above a sharp black suit on
the cover of Jet magazine.
There were no eyes, smiling
mischievous man-child wonderful,
cornbread and buttermilk slicking,
fast talking, looking like his mama,
bubblegum pop saunter and sizzle
straight necked full of tomorrow's boy
staring back into the camera.

What was there, wasn't there at all.
What was there, swallowed the world.
My mama was eight years old when
they painted Emmett Till's fractured image
on the cover of a negro magazine.
Eight years old.
Pigtails, knee socks, pinafores, pleats, and
a heap of pretty girl possibilities.

But I know my grandmother set that book down
with intention on the coffee table
knowing her baby girl would see it and know
what shouldn't be known but what must be known.

This is what the south did when an adolescent mistake when a fast-talking, finger-snapping negro from up north whistles and boasts about big city white girl honeys with rosy lips and no Jim Crow.

It's an imagine I shoved
at my 13 year old son,
frenetic in my attempt to tell him
that this is black history.
I need him to known that if he isn't
careful, not brave, not the sum total of all
our unlit courage, if he relegates
these stories to cliff-notes,
he'll bleed out and die in the epilogue.

I need you to know, Salih,
that my arms will never be wide enough
to cover sins like these,
that your head held so high
is still a cautionary tale
but to go on and do it anyway and
laugh and dance with your
arms and legs cocked out in odd angles and
slip by me and get the extra cornbread
whenever you can and
be grateful that when you and your boys
say something slick
about the pretty blonde girl
in the front row of algebra...

You're permitted that levity
after 400 years of
midnights. Necks decorated in nooses.
Plantations that decorated terrorism in
white pillars and mint juleps.
I tell my son to remember Emmett Till,
to remember when his eyes
were still hazel, still smiling
and how high he held his head
to celebrate that brand new hat,
to remember that his mother loved him
and almost couldn't recognize him
after that last whistle left his throat.

I tell him I'll be his mother
and celebrate his brown boy buoyancy
all the days of my life, and that while I don't
know what tomorrow holds,
I know that he'll never be strange fruit,
will never be broken open, will never be strung up,
will never be hog tied,
will never have his face so like my own
crushed or mangled or hatcheted.

I tell my son:

I'm growing these limbs to get
'round him and surround him and
we'll be strong and
unapologetically black for as long

as we can be.
```

---

## IC-1853: The Truth About Being a Girl – A Collection

- Title: The Truth About Being a Girl – A Collection
- Author (byline): Lina Banzaca and Aija Mayrock
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1121
- Already set (do not supply): none

### Source block (context only)

```text
Author: Aija Mayrock
Book: Dear Girl, pg 3,7
ISBN: 978-1524856175
Publisher: Andrews McMeel Publishing
Date (Month/Year): Aug 2020
Author: Lina Banzaca
ISBN: On-Line Transcript
https://hellopoetry.com/poem/2031728/dress-code/
Publisher: Hello Poetry.com
Date (Month/Year): July 2017
Author: Aija Mayrock
Book: Dear Girl, pg 34-39
ISBN: 978-1524856175
Publisher: Andrews McMeel Publishing
Date (Month/Year): Aug 2020
```

### Introduction (context only: never use it for content warnings)

```text
The Truth About Being a Girl – A Collection by Lina Banzaca and Aija Mayrock
```

### Performance text (classify this)

```text
Dear, Girl by Aija Mayrock
(Pg 3) Dear Girl,
You ask me what I wish for you.
I simply say --
never allow any soul to clip your wings
you were not born an ember,
you were born the flame.
(Pg 7) Dear Everyone,
Grab ahold of your voice.
It is time to make a choice
to believe survivors
to pay us all the same
to give women of color equal access and opportunity
to protect the safety of trans girls every day.
Make the choice to change the climate,
make the choice to not stay silent.

This is not the era of girls. This is the future of girls.

Dress Code by Lina Banzaca It's before first-period . . . My teachers see me walking down the hallway and rudely

gawk at my body as if it's some sort of disgrace. Flash forward . . . My teacher calls the assistant principal down to 'approve'

my clothes. I'm sent to the office to find out my mother was on her

way. The same mother who has to work every day to make a

living, and to pay for my clothes.

The same mother who's making eighty-one cents to my

principal's dollar. The same mother who taught me to love my body and how

to look appropriate. The same mother who approved and complimented me,

only an hour before, earlier that morning.

The bell for the second period rings. I'm still sitting in the office. Because wasting my time over what I'm wearing is more

important than my education. Right? I can hear the whispers of my degrading school's staff. A few higher established adults to an 'outfit check'. Quickly after, the assistant called my name. I gulped down my fear and anxiety, as I stood up. Then I'm sent into a room. The dullest, dark, and grayest room I have ever entered. "Hello Lina, we're gathered here to talk about your outfit

today."
A tee shirt dress with shorts underneath.
It reminded me of when I was in the fifth grade.
Girls were told that we needed to cover ourselves up
because boys thought about our bodies in a sexual manner,

and if we dressed a certain way and something

happened, it was our fault.

It's getting close to the third period when my mother

arrives.
After the constant duel to what seemed, death, with words,
I got to go.
I didn't have to change this time.
I was lucky.
Lucky that a teacher came to my defense along with my

mother, and told them my outfit was fine, and I couldn't

help that I was a curvier girl. Instead of focusing on what girls are wearing, maybe we

should tell boys to keep their hands to themselves and

grow up. Because that's what the girls have to learn from an early

age. Our bodies shouldn't be over sexualized for what's covering

them. Girls are body shamed and dress coded everywhere

because of what we wear.

What if we focused on teaching students to be mature young adults, rather than disgusting pigs who apparently

can't handle a girl who shows her shoulders?
Let's all obsess over real world problems.
Not what someone wears, or if it's distracting to boys.
Just when someone starts having confidence
(which is a victory in itself),
we're torn down based off of the clothes we put on our

bodies. Girls are taught that it's our fault.

Boys can just open and claim your body,
like some kind of book.
Even when the only word printed is NO.
We struggle in our bodies from such a young age.
Instead of worrying about a girl's apparel, let's worry about
the men who need to learn to control themselves.

The Truth About Being a Girl by Aija Mayrock (Pg 34-39)

People always say that the girls of this generation are so

vain: “Why can't they put their brains towards books instead of

good looks?” I used to blame girls too: “Be more than a perfect body and

a pretty hairdo.” But then I stepped into the world and opened my eyes to the truth about being a girl.

Don’t blame me, but when I thought about boys,
I thought about dinner dates and soul mates,
not boys that look at you like shark bait.
It breaks my heart for every girl growing up in this world.

I am not an object.
I have a voice and something to say.
For anyone who thinks that this generation is so vain,
it's because we girls are held under a microscope day after

day.

It's like “beautiful” doesn't even exist
unless you can cross everything off the checklist
big butt
big boobs
skinny waist
Includes:
small nose
plump lips

In all fairness,
I want to be seen as beautiful too.
I mean,
I don't want to be demeaned.
I am stuck in between
being a girl and a woman.
Growing up in a world
that has taught me to look sexy,
get a degree,
maybe a little rhinoplasty,
but never,
never
disagree with misogyny.

A world that has taught me
that being a woman
means living in fear
that your basic health care
will disappear,
or
that your paycheck
might somehow be smaller
than a man
who does the same job,
or
that your boss will tell you to stop giving him
eyes
“If you want a raise, you gotta compromise.
Boy, please.
The moment you misidentified everything,
you forgot
that a hundred years ago
I could not vote.
Look at what happens
when you try to demote
the very bodies
that give birth to you.
Please.
We are used to it all
and we are appalled
but, you see,
we don't know what it's like to be free.
***
Equality
is not just about
calling someone out.
Equality is accountability.
It is my brother knowing
that I am equal to him.
So equality
is education
from classrooms
and courtrooms,
to conference rooms
and computer screens.
Equality is truth,
is strong voices.

It is breaking through the silence that exists,
because silence
can't exist
if it's not tolerated.
Equality is you
changing the future,
clearing the path
for every woman
and
every man.
It is raising the next generation to know
that not only
does their voice matter
but
it will be heard.

We have the power in our hands.
As we will not sit back
and nod
and smile
while certain people
reconcile
the rules
of being fertile.

Sorry, but it's my body, baby.

I may be a young lady
but my father always taught me
to speak out
and fight
against injustice of every kind.

We will not stop
until we hold our rights
for women of every color
size
shape
sexual identity
and place
in this world.

And that is the truth about being a girl.
```

---

## IC-1854: Until We Dance, for Joseph

- Title: Until We Dance, for Joseph
- Author (byline): Jessica Care Moore
- Work: The Alphabet Verses the Ghetto
- Publisher: Moore Black Press
- Publication date as stated: June 2003
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 604
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jessica Care Moore
Book: The Alphabet Verses the Ghetto
ISBN: 978-0965830874
Publisher: Moore Black Press
Date (Month/Year): June 2003
```

### Introduction (context only: never use it for content warnings)

```text
Behind every AIDS death is a story. Behind each statistic is a person who is loved, who was someone's brother, mother, father, sister, aunt, uncle, friend, grandparent or lover. The ones who died early on created the most heart-wrenching times -- they were subjected to the worst kinds of fear and isolation, even by those who were supposed to be family. In Until We Dance, for Joseph, Jessica Care Moore explain her 14-year-old understanding of AIDS through the loss of her most beloved family member . . . and she offers her hope for the future of those who are living with HIV and AIDS.

Until We Dance, for Joseph by Jessica Care Moore
```

### Performance text (classify this)

```text
I was taught about AIDS
Inside the whispers and beneath the foundation of my
white aluminum Detroit house.
The wind smelled of wild flowers and car exhaust
As I sat on my porch waiting for you to arrive.
Full of smiles joy and candy
You pull up in your car and spin me around with promises
at 14,
that one day we would be as famous as fred astaire and
josephine baker.
I am still dizzy with anticipation.
Spinning like all little girls do when in love.
Waiting for you to show up for our encore performance.
That afternoon my innocence stretched
and pulled into the shape of a
woman’s heart.
I was never allowed to see you again.
You didn’t want me to.
You didn’t know I had old wise eyes
no hospital bed, no four letter word,
no sickness could ever define or contain you.
The phone calls shook our house daily.
The sound of the ring made the butterflies shuffling
inside my stomach begin to return their cocoons.
I was losing you and couldn’t tell anybody.
Suddenly, Joseph was an angel. An urban legend. A myth.
A man inside my dreams I’d made up inside my head.
Not the tall brown curly haired man with arms as wide as
oceans.

I begged my family to let me see you.
Why has Joseph become a secret?
Why can’t I visit him just because he is sick?
The day Joseph died.
I lost my breath.
I ran outside to my porch to ask God where the air had
gone.
I danced alone for hours pretending he was holding me in
the air flying me through the living room with ease.
Then the truth.

****************************

Finally, I was told of Joseph’s condition.
There were rumors of trips to LA and wild parties,
Because, of course, in the 80’s no one in the Midwest
could contract HIV.
There were no walks, or candlelight vigils or multi-
colored quilts to warm me When Joseph died.
There wasn’t even an open funeral.
Our family was ashamed of their son
didn’t want anyone to come. Including me.
They forgot that Joseph’s life
made the world better.
His full, beautiful child-like smile lit up rooms & hearts &
Sunrays battled for his light.
After that week I never wanted to be an adult.
I wondered how many died in silence and how many still
do.
I write so their lives are not in vain.
This poem is for New York, Detroit, Chicago, Atlanta,
San Francisco, For survivors around the US.
For Zimbabwe, Botswana, and South Africa.
For the more than 28 million people living with AIDS in
Africa.
For the 10,000 that died this morning.
For the survivors, the truth-tellers, educators,
organizers, and activists.
Who aren’t ashamed
of a hug or sharing a meal
or providing medical care to someone with AIDS.

For the children born with AIDS who must fight for
every breath.
Today we walk with Joseph’s wind in our heels with the
names of millions in our stride.
I hope we walk loud so no one else dies in silence
Walk hard enough to shake the earth like Shango
Walk outside the boundaries of neighborhood,
of country, of gender, of sexual orientation, of race, of
generation, of reflection,
Walk past the idea of not my son, not my daughter.
Walk an inch closer to being better humans.
Walk so no one else learns about AIDS
The way I did.
Without protection. Inside a whisper.
Because every grave needs a flower.
Every survivor has a story worth celebrating.
And this one is for you.
Encore Joseph, Encore.
```

---

## IC-1855: Virtuoso Literature for Two and Four Hands

- Title: Virtuoso Literature for Two and Four Hands
- Author (byline): Diane Wakoski
- Work: Not specified
- Publisher: Doubleday
- Publication date as stated: March 1975
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1393
- Already set (do not supply): none

### Source block (context only)

```text
Author: Diane Wakoski
ISBN: 978-0385004633
Publisher: Doubleday
Date (Month/Year): March 1975
```

### Introduction (context only: never use it for content warnings)

```text
Nothing is simple or innocent any more except poetry and music. Love is definitely not a simple or innocent concept. Love can be complicated, messy, misunderstood, and tragic, even. Love, like gravity, is a force not to be reckoned with. We try to bridle it, we try to contain it, we try to create it and destroy it and it plays by its own rules. Love can be beautiful and it can be painful, but it’s always real. Virtuoso Literature for Two and Four Hands by Diane Wakoski.
```

### Performance text (classify this)

```text
Memory relies on emotion. No other part of the mind does.

A night near New Year's Eve, in New York City. I do not remember if it was raining, but it was either cold or damp, weather that affects you like someone tracking mud onto your freshly scrubbed kitchen floor,

and my life was falling apart,
that is
the man I loved was running away from me as if I were a
leaking ceiling or a broken step, and he,
a homeowner, fatigued,
eschewing one more repair.

A party in a prosperous uptown apartment was something
to do,
voices, faces, fragrant and effulgent,
like gardenias on a hothouse tree,
forced in a December greenhouse,

the story of that night is a story of waiting,
a story of waiting for a hand which was not there to
touch me on the shoulder and say, "Let's
go home," a story of waiting
for a carpenter in a land where there are no trees, a
story of waiting,
waiting,

except for one moment which I remember,
like an afterimage from bright light:
a man,
an old friend,
a writer and teacher,
sat down at the piano/ he was drunk and nostalgic,
and bending over the keys like the limbs of a willow,
he played "Stella By Starlight,"
here in this company of intellectuals and poets,
he forgot where he was.
He forgot the rain and the evening of talk,
and played as if he were in some 1940s piano bar,
a song none of us knew the words to,
here in this company of intellectuals and poets
he played "Stella By Starlight"
this man who read Blake and Reich and Vallejo,
who listened to Bruchner in his spare time,
who did not believe in popular art,
even Bob Dylan or the Rolling Stones whom we all
listened to. He sat there
and with reverence
played "Stella By Starlight"
And I remember that part of the evening better than
anything else.

Though I later went to a jazz club and heard exciting
Pharaoh Sanders,
though I later sat desperately with a man who asked me
why,
why I was faithful to that man I loved,
the one who wanted nothing to do with me,
and I could not answer.
I could not answer.

I could not answer,
because the simple answer,
the true answer,
was one I could not believe.
Nothing is simple or innocent any

more, except poetry and music.
A night near Thanksgiving,
in Wisconsin, snow crystals blowing through the air,
an owl in the nearby woods
reminding me that I am alone,
"a woman alone"
(my mother always referred to herself as "a woman
alone" /
I learned it was a desperate and terrible condition).
I visit friends.
- They too have a piano in their living room,
gleaming in the dark, like brandied cherries
in a flat french bottle.

Whenever my life falls apart, I am reminded
that I still have not fallen apart.
The owl speaking alone in the woods, the one
we never see; we know he is waiting for a small soft
creature like a mouse, to snap the backbone in half,
and that this
is not cruel but simply his means of sustaining life.

The piano glows in Mary and Walter's living room, the luster of the wood is like well polished boots promising the hands and feet someplace to go. I feel the energy of the piano and remember my old friend, writer and teacher, who sat down and played, so lovingly, "Stella By Starlight"

sun
moon
stars
minerals and fire which liberate us from earth & water
and I tell them my meager story,
wondering why we are not satisfied with our minds
unless our hands can do their share.

As if in a story, myself,
I tell them of my promise when I was twenty-one
not to touch the piano again,
to take the motion of my hands
and transform it
into the energy of my life,
and then I confess that I feel the piano vibrating in the
next room, like a nova, an exploding star, one whose heat
and light I cannot resist,

and I go in to the piano with my hands on fire
and sit down and play old Chopin preludes/ my fingers
have not touched the keyboard for fifteen years,
they do not respond automatically,
but they remember patterns, they remember rhythms,
they remember chords and keys,
and they do not wait,
they do not wait,
they touch the keyboard, I sway, bending my body like a
willow tree, one which will weep for me.
I do not know "Stella By Starlight" but I know Chopin,
and I let my friends hear me,
how badly I play now
I remember the pleasure of touching
sun
moon
stars
that owl lonely in the woods obsidian and ivory
the hard rocks of life

they did not ask me
why
I do not play, why I am faithful to my promise though
touching the keys means so much
to me,
They knew I could not answer,
or rather,
that I could
but that my answer
would not be an
answer.

Nothing is simple or innocent any more, including poetry and music? My friend, the astronomer, cannot recognize the constellations in the sky. They are not math or science. He honors truth, not poetry.

A night in spring, Colorado mountain air, like razors near the cheek, my husband and I entering a mountain resort bar, a place where they serve beer in half-yards, steak and kidney pie is on the menu, the entertainment is an old lady named "Juneau Hattie" who plays ragtime piano. We sit among business men and college boys, someone from Sigma Chi having a birthday, middle-aged tourists drunk and revealing marital fears, "My mother was afraid I would marry the first man in uniform who came along. . . and I did"

drinking Irish coffee,

thin and steamy against the cold night

outside. We are together and happy. My hands move along with the piano player's hands. She is thumping out "My Wild Irish Rose," "Take Me Out To The Ball Game," the exposed hammers above her keyboard moving the way they must move every night for her.

She is over fifty, wears a green silk dress, Hong Kong style, slit up the sides; and a little green hat she may have made herself. Thin legs, like sticks, under a chunky body that hammers out tunes we members of the bourgeoisie can sing together. I think of her playing every night, every night having to be gay, a party, wondering how she can do it, knowing that we all always are on stage, that we all do it, though each day gets harder.

How can she bear to play those same songs every night,
put the same emotion into them?
My friend and I,
the man who played "Stella By Starlight," and I, who
was moved to confess to the keys my longing for them
last winter,
could we be moved
more than once?
He,
had he played "Stella By Starlight" any time in the past
ten years?
Will he again,
in ten more?
I, ,
holding my hands away from the pianos I have passed,
like a hiker in the hot dry mountains refusing to open his
canteen of water until he is absolutely sure he could not
continue without it,
taking a sip,
and saving the rest for another
desperate time,
I yielding that one night to Chopin in winter

and knowing that I would not be so tempted again for at least fifteen more years. . .

Drinking Irish coffee, listening to this music-hall
performer who probably makes little more money than
will pay her rent, buy her Irish whiskey;
sitting with a man I love,
one who cares for me,
wondering how
we renew
our emotions each day,
wondering what it means to have a simple desire
with a simple response.
Nothing is simple or innocent any more, except poetry
and music.

When I speak,
I hear many other voices,
like a tv store with the sets all tuned to different
channels,
When I listen,
I no longer can identify voices,
often
do not know the words of songs, cannot remember
the names of
pieces.
When I type the word "piano"
my fingers often slip.
They spell "pain" Oh,
how do we do it?
Get from day to day, when nothing is simple or innocent,
not even poetry or music?
```

---

## IC-1856: The Warrior

- Title: The Warrior
- Author (byline): Francis Richey
- Work: Not specified
- Publisher: Viking Adult
- Publication date as stated: April 2008
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1153
- Already set (do not supply): none

### Source block (context only)

```text
Author: Frances Richey
ISBN: 978-0670019618
Publisher: Viking Adult
Date (Month/Year): April 2008
```

### Introduction (context only: never use it for content warnings)

```text
When Frances Richey's son, Ben, a graduate of the United States Military Academy at West Point and a Green Beret, went on the first of his two deployments to Iraq, Richey began to write. The Warrior is her urgent and intensely personal exploration of what a mother is feeling as her only son goes off to war, as she says good-bye to him, misses him, prays for him, and waits for him to come home.

Poems from The Warrior by Francis Richey
```

### Performance text (classify this)

```text
Her son was going to do what he was going to do. He was headstrong and beautiful

and couldn't imagine he would ever die. From where she slept in the depths

of the sea, she heard his cry and did what sons despise:

she intervened,

commissioned divine armor, lobbied Zeus .... It's the same

when you see your son fall in with a bad crowd: he's thirteen and won't listen,

so you stop by the school
on your way home from work,
tell the principal, and quietly,
he takes an interest in the boy.

Isn't that your job?
To whisper in the ear of
any god who'll listen: Please,
protect him.

That was the summer he rappelled down mountains on rope

that from a distance looked thin as the dragline of a spider,

barely visible, the tension he descended

into the made-up state of Pineland

with soldiers from his class. They started with a rabbit,

and since my son was the only one who'd never hunted,

he went first. He described it: moonlight, the softness

of fur, another pulse against his chest.

The trainer showed him how to rock the rabbit

like a baby in his arms, faster and faster,

until every sinew surrendered and he smashed its head into a tree.

They make a little squeaking sound, he said. They cry.

He drove as he told me: You said you wanted to know.

I didn't ask how he felt. Maybe I should have,

but I was biting off the skin from my lips,

looking out beyond the glittering line

of traffic flying past us in the dark.

*****

I don't remember what he'd done. He was two. He'd done something, and I’d read that instead of spanking, you could put your child in a chair and tell him to sit there and think about what he'd done. A mother mothered by a woman who could not control her rages, I was determined not to hit him. Sit here, I said, and put him in the little wooden chair in the corner of his room beside the window. Maybe he was three. All arms and legs, he fought me. Think, I said, as I ran for the door, closed it, and held it closed, while he pulled with all his strength on the other side, Think about what you've done.

******

My son is always leaving.
Sometimes he looks back
and waves good-bye.
Sometimes he just disappears.
Where is he now?
In the air, returning from Poland?
On the ground, training at Fort Bragg?
The day he graduated from West Point,
the sun was so bright I couldn't see
the secretary of defense, a dark speck
under the white awning
on a makeshift stage, saying something
about the world, about danger,
a different kind of war.
No one else seemed to notice
the barn swallows swoop in
like a swarm of enormous black butterflies,
their throats bloodied,
marring the brilliance of the sky.
They arrived out of nowhere,
the way my son was suddenly a man.
As each new lieutenant shook
the secretary's hand, the swallows dipped
and keened over the field, the barracks,
those gray castles of learning,
the dead generals bronzed on pedestals.
What had drawn them to this moment,
the red sash and the saber?
What had drawn my son to this life?
Where had it come from,
his certainty of purpose?

When I was my son's age, I had no faith.
Now I believe in the prescience of wings,
each bird, its presentation of colors,
bearing the messages we pray will never come.
Looking down through borrowed binoculars
into the perfect rows,
I searched for his face.

**********

Listen, dearie, there is no world without war. An unfamiliar voice in my head -- My son is in Iraq.

I see him in the faces of soldiers on the news, in the Times --

The voice
in my mind, like the tune of a song
I hate but can’t forget,
doesn’t care about the dark circles around their eyes.
There is no world without war.

Before he was a warrior, he was a boy; before he drank blood, he drank milk . . . .

So what? says the voice. We’re all going to die.

********
Before he left for combat,
he took care of everything:
someone to plow the driveway,
cut the grass.
And the letter he wrote me,
just in case, sealed,
somewhere, in a drawer;
can't be opened,
must be opened
if he doesn't return.
I feel for my keys,
hear his voice:
Less is better. Late
for work, still,
I linger
at the window of the Century
Florist, a bowl of peonies,
my face among the tulips.

Last Mother's Day, when
he was incommunicado,
nothing came.
Three days later, a message
in my box; a package,
the mail room closed.
I went out into the lobby,
banged my fist against
the desk. When they
gave it to me, I clutched it
to my chest, sobbing
like an animal.
I spoke to no one,
did not apologize.
I didn't care about the gift.
It was the note I wanted,
the salt from his hand,
the words.

**********

[his letter . . . . ]

THE WORST THING
... too many windows and doors.
You have to check each one: look through it,
around it, beyond it ...
• • •
You have to use the light
on your gun. That shadow
in the corner, a bad guy
can move around inside it.
• • •
When you're attacked,
you've got three to five seconds
to make the right move.
Guys get killed in the open,
when they should jump
behind a wheel well.
That's why they shoot us
again and again
with plastic bullets for mistakes
the body makes, until it learns
to override the monkey –
adrenaline. When it's pumped,
you'll do things you'd never do at home.
• • •
36o-degree security. Crucial.
If you're not sure, you have to call out
to the rear: 'Are you there?"
The whole James Bond thing looks glamorous
in film, but let me tell you, the worst thing,
the worst, is to be out there alone.

*****

I believed if I was present
for his football games,
he wouldn't get hurt;
that if I made the two-hour drive
from Stamford to Ramsey
in half the time
that day he ran into a tree,
I could keep him
whole in his body.

Midafternoon, September, after Beast, that first training plebe year, I fixed him in my mind, and he called later that evening: Mom, were you at West Point today? And I said no.

But I thought
I saw you on the Plain.
I said no, but what time
did you see me?
And he named the moment
I'd prayed for him.

I thought it had something
to do with our
heartbeats, like clocks
placed in the same
room. Once
I believed I could
close my eyes and know,
even when my son was
on the other side of the world,
if he was alive.
```

---

## IC-1857: We Speak Your Names - A Celebration

- Title: We Speak Your Names - A Celebration
- Author (byline): Pearl Cleage
- Work: Not specified
- Publisher: Ballantine Books
- Publication date as stated: May 2006
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1132
- Already set (do not supply): none

### Source block (context only)

```text
Author: Pearl Cleage
ISBN: 978-0345490278
Publisher: Ballantine Books
Date (Month/Year): May 2006
```

### Introduction (context only: never use it for content warnings)

```text
For centuries, African American women have been remaking the world, giving testament to the power of hope, courage, and resilience. But it took the inspiration of Oprah Winfrey to honor fully the many gifts of sisterhood. For three amazing days–from May 13 to 15, 2005–a distinguished group of women was invited to celebrate the enduring achievements of their mentors and role models– and in the process pay tribute to the long, glorious tradition of African American accomplishment. The brilliant centerpiece of the weekend was the reading aloud of Pearl Cleage’s poem “We Speak Your Names.” With heartfelt eloquence, Pearl Cleage celebrates the priceless example of black women’s lives.

We Speak Your Names by Pearl Cleage
```

### Performance text (classify this)

```text
NOTE: The names Kamala Harris and Simone Biles have been added to this cutting, following Cleage’s instructions to “adapt it” – Performers should feel free to add the names of black women who have shaped their world.

“My sisters, here, there, and everywhere, this poem is for you. Use it, adapt it, pass it on . . .”

Because we are free women,
born of free women,
who are born of free women,
back as far as time begins,
we celebrate your freedom.

Because we are wise women,
born of wise women,
who are born of wise women,
we celebrate your wisdom.

Because we are strong women,
born of strong women,
who are born of strong women,
we celebrate your strength.

Because we are magical women,
born of magical women,
who are born of magical women,
we celebrate your magic

My sisters, we are gathered here to speak your names. We are here because we are your daughters as surely as if

you had conceived us, nurtured us, carried us in your

wombs, and then sent us out into the world to make

our mark.

and see what we see, and be what we be, but better truer,

deeper because of the shining example of your own

incandescent lives.

We know that we are walking in footprints made deep by

the confident strides Of women who parted the air before them like the forces of

nature that you are.

We are here to speak your names because you taught us

that the search is always for the truth And that when people show who us who they are, we

should believe them.

We are here because you taught us that sisterspeak can

continue to be our native tongue, No matter how many languages we learn as we move about

as citizens of the world And of the ever-evolving universe. We are here to speak your names because of the way you

made for us. Because of the prayers you prayed for us. We are the ones

you conjured up, hoping we would have strength

enough, And discipline enough, and talent enough, and nerve

enough. To step into the light when it turned in our direction.

We are the ones you hoped would make you proud Because all of our hard work makes all of yours part of

something better, truer, deeper. Something that lights the way ahead like a lamp unto our

feet, As steady as the unforgettable beat of our collective heart.

We speak your names.

We speak your names.

Dr. Maya Angelou
Roberta Flack
Aretha Franklin
Nikki Giovanni
Lena Horne
Coretta Scott King

We speak your names.

We speak your names.

You could not have known how closely we watched your

every move. How we hung on your every word. How eagerly we ran to sit cross-legged in front of the

television Whenever you were on Ed Sullivan or Soul Train or 60

Minutes.

How patiently we saved our money to buy that record, or

that theatre ticket, Or that museum membership, or that magazine

subscription That would allow us to see you doing what nobody else had

ever done before, In just that way, on every front, all at the same time.

We were so proud of you, it made us walk taller, smile

wider, dream bigger.

You could not have been in each of our little black girl

bedrooms, Watching us hold that make-pretend microphone as we lip-

synched your latest hit when dinner was ready

downstairs, Or curled up under the covers with your new book when

we had math homework to do, Or prayed for your safety when our parents told us you

were somewhere Fighting for our freedom, and it was dangerous work. It is always dangerous work, but the trade-off is

unacceptable. From you we learned that freedom is non-negotiable.

You could not have known that your collective example of the limitless possibilities that were open to us is what

allowed us to look our mothers in the eye and say: Mama, I want to be a singer Mama, I want to be an actress.

Mama, I want to be a dancer, or a sculptor, or a lawyer, or

a leader, Or a world-changing force for good, loose in the world, and

whirling. . .

And even when she rolled her eyes and shook her head And pronounced us more our father’s child than we had

ever been hers, She knew you had planted those ideas in our heads, and he

thanked you for letting us see That we could be a part of something better, truer, deeper.

We speak your names.

We speak your names.

We speak your names.

We speak your names.

Gladys Knight
Patti LaBelle
Dr. Toni Morrison
Rosa Parks
Diana Ross

We speak your names.

We speak your names.

You change the world around you with such fierce

determination, Effortless style, and unshakeable grace that we never

suspected how hard it was to be out there in the real

world, Where sisterhood sometimes seems and abstract idea and

not the living, breathing thing we know and need and

want it to be.

We have sometimes shivered at the edges of a very cold

place,
Where people do not always see our beauty
Or understand the rhythm of our song.
At those moments, we whisper your names as a talisman

and a touchstone, So we will not forget who and what and why we are here.

And then, sometimes, in recognition of our superior skill, or

our undeniable talent,
Or our absolute refusal to bend in the face of injustice,
Sometimes, we win the prize. The big one.
The one they will mention forever after when they call our

names, Or write our reviews or compose our obituaries.

Sometimes, at that crucial, first one ever moment, we are

invited to come to center court at Wimbledon, Or up to the Oscar podium, or the Oval Office, or the Nobel

ceremony, Or the Broadway stage, and express our feelings and the

feeling of every other African American woman

watching At a moment when all we really want to do is call your

names. All we really want to do is thank all of you for being with all

of us, Whenever and wherever we find ourselves, standing alone

in the light. At those moments, we remember those lessons you shared By living your very public lives with such integrity and honor That they became something better, truer, deeper.

We speak your names.

We speak your names.

Tina Turner
Alice Walker
Dionne Warwick
Oprah Winfrey
[Kamala Harris]
[Simone Biles]

We speak your names.

We speak your names.

We celebrate your courage. We celebrate your spirit. We celebrate your genius.

And we stand before you now, your living legacy, the flesh

and blood of our collective dreaming, and we realize

with a knowing deeper than the flow of human blood

in human veins That we are part of something better, truer, deeper.

We speak your names.

We speak your names.
```

---

## IC-1858: What am I? – A Collection

- Title: What am I? – A Collection
- Author (byline): Leah Anderson, Timothy D. Prott and Laura Hymson
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1471
- Already set (do not supply): none

### Source block (context only)

```text
Author: Leah Anderson
On-Line Transcript: https://goodmenproject.com/featured-
content/leah-anderson-you-ask-me-what-i-am-so-you-
may-know-how-to-fear-me/
Publisher: The Good Men Project
Date (Month/Year): Aug 2019
Author: Timothy D. Prott
On-Line Transcript:
http://www.interracialvoice.com/poetry.html
Publisher: Interracial Voice.com
Date (Month/Year): N/A
NOTE: Interracial Voice served as an independent,
information-oriented, networking news journal, serving
the mixed-race/interracial community in cyberspace.
Editor and publisher Charles Michael Byrd
Author: Laura Hymson
On-Line Transcript:
http://www.interracialvoice.com/poetry.html
Publisher: Interracial Voice.com
Date (Month/Year): N/A
NOTE: Interracial Voice served as an independent,
information-oriented, networking news journal, serving
the mixed-race/interracial community in cyberspace.
Editor and publisher Charles Michael Byrd
```

### Introduction (context only: never use it for content warnings)

```text
What are you?! It’s a question that people of mixed ethnicity endure with far too much frequency, one that is asked, quite often, with no regard for culture or background, simply as a way to classify a person. We might not realize the pain it causes to be asked this, but our ignorance does not excuse our callousness.

We must always be interested in a person’s story, not as a means of filing them into a box, but as a way to celebrate their uniqueness and individualism. If we want to to know “who” a person is, we have to learn how to listen and how to ask questions that honor their answers.

What am I?- A Collection including “You Ask Me What I am So you May Know How to Fear Me” by Leah Anderson;
```

### Performance text (classify this)

```text
You Ask Me What I am So you May Know How to Fear Me by Leah Anderson

I see you from across the room with your question mark

brows,
arms crossed in expectation,
head on tilt.
Watch you come slinking towards me,
and before we’ve even met, before you’ve even asked my

name, before you’ve even said, “Hello, what a fine day we’re

having,”
you stare at my face like a map you cannot read,
like a puzzle with centerpiece missing,
like a game you will play and will win.
“Your eyes,” you say - and here comes the grocery store

list.

“Almonds,” you say, “with a spoonful of mint jelly.” “Honey,” you say, “with the zest of a lime. The inside of a Tootsie Pop mixed with green apple Pop

Rocks.

What are you?”

“Fitting In” by Timothy D. Prott; and “What am I?” by Laura Hymson What are you?”

Words so familiar yet sharp, like the pain in the side after running a mile on a full

stomach,
like an old pocket knife, handle worn smooth in your hand
but still dried in blood after all these years.
“Well . . . ” I say, but already you are gone,
turned on your heels, retreating to safe spaces.
This is not what you wanted.
You want a one-word answer. But friend, this is not a

one-word story. There is a child whose ancestors came from across a

salty blue sea.
She is one half of the world’s population.
She is multiplying by the second.
She is unstoppable, yet on this soil she is taught to be

silent, to never raise her hand, never make too much trouble, never make herself known. They fear her for the magic she holds between her ears, for the magic of momentum that will not be still.

There is a child whose ancestors have always lived here. They crossed borders that were created only out of some colorless man’s imagination, yet within these lines, she is told she does not belong, to go back where she came from, as if where she came from is not where she is, as if her limbs were not birthed on this land, as if her toes have not always known the feel of this earth. They fear her for the magic she holds in soft places, for the magic of her seeds spreading like wildflowers in

the spring.

There is a child whose ancestors came on ships.
They were kings in a land we all came from,
before we even knew what white was,
before we set it on an altar, apart and above.
Yet here she is told that her scars are too loud,
that she must hide all evidence of building a country on

her back,
that she must be content
that things now are better than they have been,
though every breath and bullet would tell her

differently. They fear her for the magic she holds in the bones of

her memory, for the magic of her song that will not lay down quietly. You ask me what I am and hear my words as mutiny, igniting fires you are not ready for in your comfortable

home,
surrounded by your books and your friends,
not even noticing when you look around the room
that your skin is all the milky same,
that you have learned how to keep out anything
that may dirty the walls of your castles,
that may challenge the sovereignty of your thrones.

And where does this fear come from? We all run when we’re scared, or turn with fists up and

fight, or drop to the ground to find solace in the earth, or find some sense in the smell of the grass.

I can tell you my history in terms of trauma, or laughter, or scars on my knees, or books on my

shelves, or the number of times my heart has been broken. I can tell you my history by the things my eyes have

seen, but you learn nothing by the shape of them.

You ask me what I am and search for safety in the

answer. There is no safety here. There is a child whose ancestors came from opposite

ends of the earth. They met in the middle in a land where the air is sticky

and sweet. She loves Malay and eating ice cream in bed, and the way her body feels when covered in mud and in

sweat and small living things she can hold in the palm of her

hand.
She is too young for stillness.
She is too old for silence.
And her eyes . . .
her eyes change color with the wind.

Fitting In by Timothy D. Prott

Why won't I fit in?

Is it the way I dress?
I dress the only way I know how.
I dress to feel comfortable, not to impress.
It is no more justified to judge a person on their style
Than it is to judge them on their lack thereof.

It is like judging how a walnut will taste
By examining the bumps and ridges on its shell.
The two entities, though one unit, are not directly
related to one
another.
I dress the only way I know how.

Perhaps it is how I talk
I speak the way my parents taught me.
My speech is for clarification, not for impression.
Why is it that one group denotes my speech as "too

proper,"
Whereas another group sees it as "not proper enough?"
If I wanna be down, I have to speak a certain way.
If I wanna rise up, I have to speak a certain way.
Or so they say . . .
You know what I say?
I say my voice is my character.
To know my speech is to know me.
I don't think anyone sees it my way.

I wonder if it is the way I carry myself.
My personality is not one that stands out.
Except to those who are in my soul.
Low-key, you might say, is the word for me.
At least that is what you see
Unless I let you in.
But for some this is my drawback
They use my personality as a means to discredit me.
Telling me I'm this or that
Placing me in a category because of my choice.

Can't they see!
If you strip away all the matter we are all the same.
But they will never see me as such.
So they use my personality as a crutch.
To justify their false beliefs in facts they themselves

cannot prove. Is that what we have come to?

Or is it the one defining factor that our society

choosed [sic] to use To separate us?

Is it my race that keeps me from the fit?
For me the answer is two sided, you see
Yet joined in one, in its simplicity
I'll admit, "race" has been a benefit and a burden.
But what is so important about this four-letter word?

For some it is the ladder upon which they climb. For others it is the heavy chain that chokes the very life from them For the vast majority, it is very significant. It is the reason the square does not fit with the round And the triangular does not fit with the trapezoidal It separates us like oil separates from water.

What does race mean to me? One who straddles the boundaries between night and

day?
Race is just a word.
Simply a word.
Not a barrier to be crossed
Not an obstacle to be overcome
Not a crutch upon which I support my very existence.
A word.

And once they see as I see
With the pureness of their hearts
Not with their eyes
Then and then will I truly fit in.

What am I? by Laura Hymson

What am I? You want a one-word answer. But friend, this is not a

one-word story. (from Poem #1)

I was born out of love
Fostered in confusion
Came to stumble on pride and inner strength
Found power within myself
I never knew what I was but I knew what I was not
I knew then I did not fit into one of your small boxes of

identity
I know now I am too big, too strong to curl up into one of
your conventional
convenient categories of existence
I knew then I was different, special, unique
I know now just how special I am
I am the small minded man’s fear
The fear of the unknown
The nameless
The outsider

What am I?

Each one of our answers lies out there somewhere

before us Our identities waiting to be claimed Claimed, not by a checked off box nor society nor

anyone else other than you, the individual, the perfect combination, the union of two

beautiful cultures, backgrounds, and colors
```

---

## IC-1859: When Your Family Falls Apart

- Title: When Your Family Falls Apart
- Author (byline): Nova Venerable
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: UPDATE
- Teaser before the introduction: No
- Spoken words (computed): 1298
- Already set (do not supply): none

### Source block (context only)

```text
Author: Nova Venerable
DVD: Louder Than a Bomb
DVD available at Amazon.com
ASIN: B006UTDG42
Publisher: Virgil Films
Date (Month/Year): March 20, 2012
On-line Video at
https://www.youtube.com/watch?v=FZMpePbF454
Author: Nova Venerable
Book: Learn Then Burn (Pg 57)
ISBN: 978-0984251575
Publisher: Write Bloody Publishing
Date (Month/Year): May 2010
Author: Nova Venerable
DVD: Louder Than a Bomb
DVD available at Amazon.com
ASIN: B006UTDG42
Publisher: Virgil Films
Date (Month/Year): March 20, 2012
On-line Video at
https://www.youtube.com/watch?v=3kpt1rCtPEQ
```

### Introduction (context only: never use it for content warnings)

```text
By all accounts Nova Venerable was a troubled child. Once a student at Oak Park/River Forest High School, Illinois, she described her high-school self in this way, "I was really angry all the time, I used to try to fight people every day, I used to yell at people, choke people, stab at people with pencils."

But poetry (and speech competitions) gave her a constructive outlet -- a way to express herself and feel rewarded for it. Her poems about her addicted father and her younger brother Cody are raw, honest and heart-breaking.

When Your Family Falls Apart by Nova Venerable
```

### Performance text (classify this)

```text
Apartment on Austin
There are always sirens outside your place.
Your condo always seemed to lean to the left,
the cement windows rusted like overused water pipes.
We lived on the first floor.
The mango skinned buzzer never worked.
A window in the door was cracked.
Broken into on Austin, stole everything but your big
screen TV and your furniture
Because everyone with a grudge knew that
You worked nights at Joliet and days at Chicago Public
Schools
Never enough time to sleep.
Our condo door was tainted white,
like a three year old sock washed every week,
the walls were the 49ers,
the carpet was rough,
like tangled hair,
everything you had no room for
piled on to shelves like children.
It smelled like alcohol, bad food and body odor mixed
like margaritas.
You would always ask me to make your drinks,
Measure liquid with the width of my nine year old
fingers:
Four fingers sangria,
two gin,
two tonic,
and one lemon juice.
Sometimes I remembered I would wake up,
And you would be standing in the doorway,
Smiling at us while we slept.
I would wrap my arms around your sunken stomach
Like tissue paper you would kiss my forehead, lay me
back down,
Tie me in bows around my blankets
Because momma moved out and wasn’t around to do it no
more.
By the time I was 10,
I was your wife,
your mother,
your best friend,
your sister,
and you were bitter.
I would feed you chicken soup when you were sick,
kiss your forehead to see how bad your fever was.

Phone Wires
Prison guards maced my father when I was 12.
He fell asleep on his back that night,
gas braiding down his throat
like rain on power lines
I wonder if he remembers
he woke up screaming for me
that I walked him to the bathroom,
cleaned his eyes with cold water
and put him back to bed.

My mother used to tell me
that my father was disgusting
that I didn’t have to see him if I
didn’t want to.
“Tell the cops he’s physically, emotionally
and psychologically abusive”
like I knew what that meant
when I was 11.

I would wake my father up every night
at 9:00 and braid his hair.
Over, Under, Over, Under
The grease seeped
from his scalp and kept
his dandruff suffocating
under my fingernails.
“Nova girl, you’re gonna come see me more right?
You’re gonna tell the judge that you wanna see me just
as much as your mother?”
His eyes sagged,
a job,
pent up under each one.

“Nova, just tell him you don’t wanna see him anymore.”
My mother dialed his number
and stayed on the line,
made sure that I left my father
hung up on other end of chords,
ending my father and I like phone calls.
She taught me to break my father’s heart
with wires,
My Baba and I haven’t spoken since I was 12.

My father’s left eye sagged more than his right,
night time prison guard stretched
out his face.
He risked his life every day for his children
every time he drove to Joliet.
kept teaching at Chicago Public Schools
His right eye was darker,
cramped in the wrinkles of his skin,
promised he would teach
Them like he did his children.
Over, Under, Over, Under

After I hung up the phone
mom asked me
if it was really
all that hard
to break my father’s heart
and at 17 I can finally answer her question.

I can tell her
I know why our relationship is choking
I left father for mother
and I wake up cold,
dreaming about my Baba
waiting to tell him that I have his eyes.
Want to know if he wonders which college his baby girl
is going to.
I can tell her that I hate talking on the phone now
I wish I could erase calls from five years ago
so I wouldn’t have liked when I told my father
“Yes, Daddy, I’m gonna come see you more.

Cody

My youngest brother was born
with my grandfather's nose
round like spools of thread,
my father's eyes and
my mother's genes.

He is 12 years old now and
I watch him play
Hungry Hungry Hippos,
see his body jitters
like a wind up toy
and he screams like a happy crow
when he asks me to play with him.

He tries to learn the words
to the Scooby-doo song,
repeats the phrases my mother
and I say, and when I see him,
I wonder how could God know that
Diabetes peels 27 years of life
like dead skin.
Yet he still allows my brother
to have his fingers pricked
every day.

Why is it when I look
at him, I can see every needle
we've ever had to stick
his arms, legs, or stomach with
to keep him alive.
Sometimes five shots a day
isn't enough to fight juvenile diabetes.

I think

How could God bless him
with seizures and autism.
Why every time we rush him to the hospital
it could be my last day watching
him rewind on-demand
until his lips can curve
to form words
that aren't even his because my mother
gave him a broken X chromosome.

Today,
I will smile
As he learns to brush his teeth for the first time
or obsesses over his red pants and shirts,
I will laugh as he tries to learn sign language
to make up for tongue lost in Fragile-X
Syndrome
and I will accept his fake kisses
like disorders.

But I can't help but wonder
Can his brain still hold the times
I meshed his food up when he was 8
or changed his diapers at 7.

Will he miss me
when I am not there to run my fingers
through his hair like Pink Oil
Over, Under, Over, Under
when he wakes up from
ear tube surgeries or seizures.

Will he remember
how he slept in my bed every night
after mama left,
and I held him like an extra pillow.
Or when my arms were his restraints
when daddy said put him in middle
without seatbelt so he would be the
first to die in car accident.
Can he know how he found
a mother in big sister?

For now,
I will pray for him every night
that his kidneys will stop trying to fail on us,
that his blood sugar won't send him into
a coma.
I hope
that he won’t grow accustomed
to not pronouncing my name
when I go away to college,
and I pray I pray that his seizures
won't kill him before his diabetes does.
Over, Under, Over, Under

From Apartment on Austin

[Baba] . . . I’m 17 now,
and we don’t even talk.
And sometimes I wish I could tell you
how much I miss you.
How I want to wrap my arms around
your sunken stomach like tissue paper.
That I love you,
and I wish you were here to be my Papa G again.
So you would know that I have a boyfriend
that loves me more than you ever use to.
But I guess you’re too busy rusting,
like cement windows,
to notice that your baby girl is a woman.
Over, Under, Over, Under
UPDATE: In 2020, the NSDA Board of Directors voted to
pilot new rules regarding what sources for material may be
used in Interpretation events, including removal of the
requirement that digital sources must be found on the
Approved Websites List. Students are no longer required to
use only digital sources found on this list.

This change may or may not impact specific regional or state tournaments. Please check requirements for publication for your tournament before performing this poetry selection.
```

---

## IC-1860: The White Rose: Sophie Scholl 1921-1943

- Title: The White Rose: Sophie Scholl 1921-1943
- Author (byline): Erika Mumford
- Work: Willow Water
- Publisher: Every Other Thursday Press
- Publication date as stated: May 1988
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1507
- Already set (do not supply): none

### Source block (context only)

```text
Author: Erika Mumford
Book: Willow Water
ISBN: 978-0961996017
Publisher: Every Other Thursday Press
Date (Month/Year): May 1988
```

### Introduction (context only: never use it for content warnings)

```text
Hans and Sophie Scholl were German teenagers in the 1930s. Like other young Germans, they enthusiastically joined the Hitler Youth. Initially they like thousands of others believed that Adolf Hitler was leading the German people back to greatness. Their parents were not so enthusiastic. Gradually, Hans and Sophie came to realize that their parents were right: Hitler and the Nazis were enslaving and destroying the German people. The government had become an evil regime, sending hundreds of thousands of its citizens to their deaths.

This is the story Sophie Scholl’s resistance. This is the story of The White Rose. It is a lesson in dissent. It is a tale of courage, of principle, of honor. The White Rose: Sophie Scholl 1921-1943 by Erika Mumford.
```

### Performance text (classify this)

```text
It is the deep, green and dark forest
where the wild animals spring past
Snow White. Pine cones dot the moss,
and mushrooms, small one-legged people,
stand straight and silent in their scarlet hoods.

Why is Father sad?

"There was once a splendid castle
filled with treasure: carpets
from Isfahan, ruby and cobalt goblets,
rock crystal windows, floors of ebony,
and fountains everywhere. You would have thought
the people who lived there
the luckiest in the world.

But in the cellar of that castle
a frightful slaughter went on day and night
until blood bubbled up from the ground
and dyed the fountains red."

"But Papa," says Hans "are you sure, are you sure the Fuehrer knows about the camps?"

Some people believe this is the end of the world.

"Drink your cocoa, Sophie, you've hardly touched your breakfast."

"Too much to do - the rally this afternoon - is my blouse ready?"

"And your piano lesson?"

Piano lesson!

"But Mama, the Fuehrer himself is speaking - you know our troop has to be there. Don't you want to come?"

She slams the iron down.

"Here - take it - go!" And then her arms are around me. "The Pied Piper - remember?"

"Oh Mama - that dumb story - "

************

They're calling it Kristallnacht - lovely word that makes you think of jewelled chandeliers' blaze in a midnight-blue and silver ballroom where waltzing couples whirl, and violins set all the drops of moonlight trembling.

Night
of smashed and trampled lives,
the image in the mirror crazed and blinded
beyond repair. Oh delicate splinters, stars
sparkling like tears on the soiled face of earth,
oh piercing, bloody fragments: Crystal.

Night

*****************

- the sound we wait for. Wail
rising and falling in my sleep shocked
torn awake stumble
into clothes
I grab Inge's hand quick hurry
Father at the cellar door
"It's all right - don't rush
Werner, here's the thermos. Hans
your coat" rising, falling
"Where's Mother" - "here, Sophie
take this blanket". CRASH and
CRASH not this house not us
walls tremble, tinkle of glass CRASH fainter
this time thank God further silence
the All Clear.

******************

"Beloved, let us pray
also for Yakov Androvenko,
forced-laborer in this parish
who was beaten to death - "

in the night, Herr Pastor Harms is arrested - but our whole country is a prison.

A friend of Hans's returned from the front
to find his wife - an epileptic,
pregnant with their first child -
gassed.

Today in a shuffling, close-packed column
of old men, women, young girls and boys
all wearing yellow stars
all carrying suitcases,
I saw a baby playing peek-a-boo
over his mother's shoulder. His laughter
spurted into the smoky air
like jets of blood.

**************

Munich seems vast to me coming from little Ulm. And everywhere the grisly bombed buildings, gaping like smashed dollhouses - you can see where stairs went up, tatters of flowered wallpaper, a picture hanging crazily above charred heaps that once were chairs.

Strange, how in the midst of this we can still laugh together, still celebrate.

my first day at the University - Hans and his friends gave a party for me.

Later we talked. And Hans: "It sickens me -
the irony of medical school, healing people
for Hitler to feed into this roaring furnace
of war - and into those - into those other ovens . . .
I can't remember who first spoke the word
resistance. Then Christoph -
"How can we hold our heads up ever again,
a nation of cowards ruled by criminals?"
What if we win this war? Already
they are warning us
that rather than hang around the universities
we should be "making a child for Hitler".
My flesh creeps - I want to plunge into my studies
as into a cleansing stream.

******************* In large, clear letters on the blackboard Professor Huber's text from Lao Tzu:

Do you think you can take over the universe and improve it? If you try to hold it you will lose it.

If you rejoice in victory you delight in killing. Force is followed by loss of strength.

That which goes against the Tao comes to an early end.

The mild words are an open dare. If just one student should denounce him? Watching him balance on that knife-edge I draw deep breaths of icy mountain air.

*******************

Leaflets on floors and windowsills
- with pounding heart I read
Nothing is so unworthy of a civilized nation
as that it should permit itself to be governed
by an irresponsible ruling caste
that has surrendered
to its darkest instincts . . .
resist . . . a people deserves that government
it tolerates . . . resist . . .

We're not alone, then -
there are others like us!
In the main lecture hall
women with pails and brushes
are scrubbing slogans off the walls:
DOWN WITH HITLER!
FREEDOM!

Goosebumps along my arms - it's in the air, spark of resistance - flame - fire –

In classes, whispering excitement.
Impossible to keep my mind
on philosophy today.
I rush to Hans's room
- he'll have spent the morning at the lab
and won't have seen the flyers.

A book lies open on his desk,
a sentence, lightly underlined
leaps out: A people deserves
that government it tolerates.

O merciful God.

****************

Why must it be me?

Why not you? But there are others, political people -

The work is not political. people who understand this kind of thing -

What don't you understand? organizations -

We are born and die alone. I don't want to die.

The work is urgent. Oh please, please don't

The decision is yours. I'm so afraid.

Yes.

*********

Breathless, in the streetcar. Beside me
an S.S. officer fidgets, glances restlessly
about. Once, horribly,
I catch his eye. My briefcase
burns into my side, I can't stop
seeing the clasp give way, papers
spilling, whirling into people's laps -
does it look odd? Too full?
Should I have looked away so quickly?

The ticket collector -
breathe deeply - don't run - I fumble
with change - the briefcase
slips, crashes down, the officer
grabs it his face swims before my eyes
- hands it back, smiling -
hot trickle of terror down my leg

There are times at night
when I am fear, icy, my bones
liquid, blood humming in darkness
listening. I pray to sleep, I pray
to wake and find myself and Hans,
Christoph and Alex and the others
just students again.
The deadly pressure lifted.

*********

It is morning, the University
about to open. In the stillness
before voices, the slam and clatter
of doors, our footsteps
sound like shots. Hans and I
lean over the topmost bannister, empty
our bags. A snowfall of paper
settles on landings, stairs.

Relief,
familiar, welling nausea.
I grasp the railing
to keep my legs from giving way.
Hans hugs me, our eyes meet. His
are glowing. "Let's get out of here."

We take the stairs two at a time,
reach the door, which
and time slows
stops won't open impossible
won't

open

I'm still trying
to grasp why is the janitor sirens
"Hans! The police"
uniformed men surround us

so quickly done

**********************
Stripped naked, my chain with the gold cross
broken, clothes
turned inside out, seams slit, flesh
shrinking from hard fingers
when very quietly,
"if you have anything forbidden on you
destroy it now. I'm a prisoner too."
The clothes she gives me hang on me
as though already
my body takes up less space.

*******************

An entire day and night of questioning

The officers who question me
seem puzzled.
I was even offered coffee.
"If you had realized, Fraulein Scholl,
how you have undermined the war effort,
surely you would have acted differently?"

Christoph, Herr Huber, Willi, Alex - my mind shuts around you - not one crack of light - silence

the room

tilts

*****************

The indictment - so thick the list of all my crimes?

In spite of myself my hands

shake
I can hardly hold it
much less read
the type that

blurs

and chatters on the page. I force myself

to look to look

until the words stand
clear
black and implacable:
High Treason.

will it hurt to die *******************

Judge Freisler himself
was flown here for our trial.
Blood-red robes, cold heavy-lidded eyes
- so everything has been decided.

Hans. After these dark days and nights - your smile,

warm
sunshine. Christoph's blue, blue eyes.
Out there, a blur - so many people?
Mother and Father, I am willing you
to come dear God to come in time

"Traitors, sniveling trash - " Freisler actually foams at the mouth, rage shakes him like a terrier a rat

it has nothing to do with me.

Silence - a question - I shake my head, no. Hans is saying something

Freisler's mouth
a black hole dribbling . . . treason
To be beheaded. Beheaded.
Beheaded.

**************

A still and luminous room.
Mother and Father - it is only air
that parts us, not this silly barrier.
I hardly feel the floor beneath my feet.

- We've brought - they let us bring - this chocolate - Hans didn't want any –

- Will they arrest you, too?

- We're in God's hands
as you are, Sophie –
I've never seen you
so beautiful - but you're trembling –

- I'm not afraid.

Mama? I promise

I'm not afraid.

*************** Some people believe this is the end of the world.
```

---

## IC-1861: Wild Embers: Poems of Rebellion, Fire and Beauty

- Title: Wild Embers: Poems of Rebellion, Fire and Beauty
- Author (byline): Nikita Gill
- Work: Not specified
- Publisher: Hachette Books
- Publication date as stated: Nov 2017
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1274
- Already set (do not supply): none

### Source block (context only)

```text
Author: Nikita Gill
ISBN: 978-1549113314
Publisher: Hachette Books
Date (Month/Year): Nov 2017
```

### Introduction (context only: never use it for content warnings)

```text
If words are magic, then poetry is the ultimate magic. Nikita Gill said: “The greatest wish I have ever had is to create with words what wizards cannot and what magic never has. The most elegant bond I can ever pray for is aiding in the recovery of someone who is made of wreckage and facilitating their becoming their own hero in their story.”*

In these poems from her book Wild Embers, Nikita Gill re-imagines heroines of well-known fairy tales as powerful heroes of their own stories. And in doing so, she inspires us to rewrite our own narratives and encourage the next generation of women to do the same.

Poems from Wild Embers by Nikita Gill
```

### Performance text (classify this)

```text
(Pg 59) Fairytales exist.
They always have.
We just have to rewrite them
over and over again
till they fit.

Heros (Pg 70)
We feed ourselves
so many stories
of princes and saviours
coming to protect us
from our monster,
from our demons,
that we forget there
is nothing more beautiful,
more fulfilling,
than becoming our own heroes,
than saving ourselves.

Sleeping Beauty (Pg 60)

The version of Sleeping Beauty I tell my daughter will be a fairytale about consent before it is a fairytale about true love. In it, I will pause and ask her, ‘Do you think it was right for the Prince to kiss a girl who was unconscious, just because he thinks she is pretty?’ And I expect her to say, ‘No. No, it is not!’ In my story, Aurora will not marry the Prince. In my story, Aurora will stand tall, say 'no' to a marriage with a man she barely knows and rule her father's kingdom all on her own.

I will use this story to help her understand, no boy has the right to touch her without her consent just because he thinks she is pretty.

I will teach her to say the word ‘No,’ before she learns ‘Yes.’ I will teach her that others may think she is being difficult, but no one’s opinion matters as much as her own.

And most important of all, I will teach her never to feel guilty or wear her body as though it is a gift to anyone except herself.

Belle (Pg 61)

Belle is fierce in the way lionesses are when they hunt. She fears nothing and takes on monsters with ease when it comes to protecting the people she loves. She looks at someone and sees their inner beauty before she allows herself to fall in anything close to love. She sacrifices her freedom, her most treasured possession, for her father. She stands out from the crowd and reads in a time when education for women was unheard of. Her kindness and willingness to give to others is where her true beauty lies.

And yet, in the fairytales we tell our children, we first introduce her as beautiful rather than fierce, kind, independent, intelligent, giving, full of light and powerful. Even her name is a testament to outward beauty.

Her name should never have been Belle. Her name should have been Feroce. Her name should have been Liberte.

Snow White (Pg 64-65)

The thing with Snow White is that she isn’t so Snow White when the hunter tries to kill her. She grew up in a home with a stepmother who was cruel, which led her to believe that she needed to learn self defense before she sang to the birds or baked apple pie. Because little girls who grow up with the constant threat of a parent who does not love them in their lives learn to listen for footsteps, watch body language and understand it is they who are responsible for their own little lives.

Imagine, young Snow White in the soldier’s training area, wielding a sword, being taught by her father’s knights how to overcome any enemy. By the time she is grown, the girl knows her way around a bow and arrow better than she knows around a kitchen and the hunter had no idea what hit him when the princess he thought an easy mark had him on his back, his own sword turned on him in a second.

The seven dwarves didn’t give her refuge so she could cook and clean and do their laundry, they gave her refuge because they knew she was the rightful and just hear to the throne, also, they were just decent human beings. And Snow White never bit that apple, because she knew better than to be pressured by strange old ladies she had only just met.

She spent her years in the forest making up an army to reclaim her throne.

Don’t ever let them tell you that girls are made for glass boxes and princes and apples pies when girls are made for swords and shields and anything else they damn well want to be.

Cinderella (Pg 66)

There is only so much a good person can be verbally insulted and abused before they unleash their inner, sleeping dragon. And this is why Cinderella, locked in her attic, doomed to a life of cleaning, decided enough was enough and decided to take some action.

Cinderella’s fairy Godmother wasn’t a fairy Godmother at all. She was the best damned lawyer in town, and she took Cinderella’s stepsisters and stepmother to the cleaners before they were unceremoniously thrown out of a house that wasn’t theirs. At the end of the day, that house was her father’s last possession and as its mistress, Cinderella could return it to its former glory and bring back its sunny disposition. She didn’t need to worry about balls and glass slippers because she took over her father’s business of trading beautifully woven fabric from lands far and wide.

When the Prince did come to her door, he hand delivered her invitation, and Cinderella, who had to leave for a business trip that very evening, told him she had no inclination. She needed no husband at the tender age of nineteen. And she didn’t want to become a princess and abandon what she had built, as a royal she would have no time. Because girls who were building empires for themselves did not need kingdoms to shine.

Girls of the Wild (Pg 72)

They won’t tell you fairytales
of how girls can be dangerous and still win.
They will only tell you stories
where girls are sweet and kind
and reject all sin.
I guess to them it’s a terrifying thought,
a Red Riding Hood
who knew exactly
what she was doing
when she invited the wild in.

Little Red Riding Hood (Pg 67)

Girls who survive trauma wear a certain vulnerability around them, and some men are wolves, they look for those girls, their eyes hungry for prey, their tongues filled with lies to pull girls like this back into the void they have just escaped from.

Little Red Riding Hood was a survivor too, and once, when a man had taken a step too far, she had told the story of what she did to the last thing that tried to devour her.

‘I let the wild seep in,’ she said, her voice perilously low, ‘I let him think he was going to win, but little did he know, I bare teeth too, sharper than his and a heart that has survived terrible pain young. When he tried to devour me, I took the axe from the basket and hacked until he was done.’

If you want to know the secret, if you want to know the truth, there is nothing more dangerous than a girl who is aware of the flames inside her, and all the damage she can do.

Yes. Girls who survive trauma do wear a certain
vulnerability around them, but this kind of
vulnerability is from where their greatest
strength stems.

Bedtime Stories (Pg 147)

When your daughter asks you to tell her bedtime stories, the kind that you grew up with, I hope you tell her better versions.

I hope you tell her bedtime stories where the princess isn’t a princess but a knight and she’s going to war with dragons all by herself. I hope you tell her stories where the princess rescues her father’s kingdom from impending doom. I hope you tell her stores where girls save themselves from anything. And no towers and monsters and dragons and kings can ever stop them from doing what they want to do.
```

---

## IC-1862: Wild Grapes

- Title: Wild Grapes
- Author (byline): Robert Frost
- Work: The Poetry of Robert Frost: The Collected Poems, Complete and Unabridged
- Publisher: Henry Holt and Company, Inc.
- Publication date as stated: Nov 1969
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 881
- Already set (do not supply): none

### Source block (context only)

```text
Author: Robert Frost
Book: The Poetry of Robert Frost: The Collected Poems,
Complete and Unabridged
ISBN: 978-0805005028
Publisher: Henry Holt and Company, Inc.
Date (Month/Year): Nov 1969
```

### Introduction (context only: never use it for content warnings)

```text
Letting go is a journey that never ends. Never. It only begins -- over and over again -- each time you can glimpse something higher than your own painful certainty over who you think you are. There is always something higher; a life beyond the limits of your present sight. In Robert Frost’s poem Wild Grapes, I urge you to consider whether Frost is praising or criticizing man's unyielding nature? Is “letting go” a virtue or a flaw . . . Wild Grapes by Robert Frost.
```

### Performance text (classify this)

```text
What tree may not the fig be gathered from?
The grape may not be gathered from the birch?
It's all you know the grape, or know the birch.
As a girl gathered from the birch myself
Equally with my weight in grapes, one autumn,
I ought to know what tree the grape is fruit of.
I was born, I suppose, like anyone,
And grew to be a little boyish girl
My brother could not always leave at home.
But that beginning was wiped out in fear
The day I swung suspended with the grapes,
And was come after like Eurydice
And brought down safely from the upper regions;
And the life I live now's an extra life
I can waste as I please on whom I please.
So if you see me celebrate two birthdays,
And give myself out of two different ages,
One of them five years younger than I look--
One day my brother led me to a glade
Where a white birch he knew of stood alone,
Wearing a thin head-dress of pointed leaves,
And heavy on her heavy hair behind,
Against her neck, an ornament of grapes.
Grapes, I knew grapes from having seen them last year.
One bunch of them, and there began to be
Bunches all round me growing in white birches,
The way they grew round Leif the Lucky's German;
Mostly as much beyond my lifted hands, though,
As the moon used to seem when I was younger,
And only freely to be had for climbing.
My brother did the climbing; and at first
Threw me down grapes to miss and scatter
And have to hunt for in sweet fern and hardhack;
Which gave him some time to himself to eat,
But not so much, perhaps, as a boy needed.
So then, to make me wholly self-supporting,
He climbed still higher and bent the tree to earth
And put it in my hands to pick my own grapes.
"Here, take a tree-top, I'll get down another.
Hold on with all your might when I let go."
I said I had the tree. It wasn't true.
The opposite was true. The tree had me.
The minute it was left with me alone
It caught me up as if I were the fish
And it the fishpole. So I was translated
To loud cries from my brother of "Let go!
Don't you know anything, you girl? Let go!"
But I, with something of the baby grip
Acquired ancestrally in just such trees
When wilder mothers than our wildest now
Hung babies out on branches by the hands
To dry or wash or tan, I don't know which,
(You'll have to ask an evolutionist)--
I held on uncomplainingly for life.
My brother tried to make me laugh to help me.
"What are you doing up there in those grapes?
Don't be afraid. A few of them won't hurt you.
I mean, they won't pick you if you don't them."
Much danger of my picking anything!
By that time I was pretty well reduced
To a philosophy of hang-and-let-hang.
"Now you know how it feels," my brother said,
"To be a bunch of fox-grapes, as they call them,
That when it thinks it has escaped the fox
By growing where it shouldn't--on a birch,
Where a fox wouldn't think to look for it--
And if he looked and found it, couldn't reach it--
Just then come you and I to gather it.
Only you have the advantage of the grapes
In one way: you have one more stem to cling by,
And promise more resistance to the picker."
One by one I lost off my hat and shoes,
And still I clung. I let my head fall back,
And shut my eyes against the sun, my ears
Against my brother's nonsense; "Drop," he said,
"I'll catch you in my arms. It isn't far."
(Stated in lengths of him it might not be.)
"Drop or I'll shake the tree and shake you down."
Grim silence on my part as I sank lower,
My small wrists stretching till they showed the banjo

strings.
"Why, if she isn't serious about it!
Hold tight awhile till I think what to do.
I'll bend the tree down and let you down by it."
I don't know much about the letting down;
But once I felt ground with my stocking feet
And the world came revolving back to me,
I know I looked long at my curled-up fingers,
Before I straightened them and brushed the bark off.
My brother said: "Don't you weigh anything?
Try to weigh something next time, so you won't
Be run off with by birch trees into space."
It wasn't my not weighing anything
So much as my not knowing anything--
My brother had been nearer right before.
I had not taken the first step in knowledge;
I had not learned to let go with the hands,
As still I have not learned to with the heart,
And have no wish to with the heart--nor need,
That I can see. The mind--is not the heart.
I may yet live, as I know others live,
To wish in vain to let go with the mind--
Of cares, at night, to sleep; but nothing tells me
That I need learn to let go with the heart.
```

---

## IC-1863: With No Immediate Cause and Woman, Do You Know

- Title: With No Immediate Cause and Woman, Do You Know
- Author (byline): Ntozake Shange and Lisa Dietz
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 741
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ntozake Shange
Book: Nappy Edges
ISBN: 978-0312064242
Publisher: St. Martin's Griffin
Date(Month/Year): July 1991
Author: Lisa Dietz
Book: "Murphy Square: Unbound"
ISBN: N/A
Publisher: Augsburg College, Minneapolis, MN
Date (Month/Year): 1990
```

### Introduction (context only: never use it for content warnings)

```text
Domestic violence should not happen to anybody. Ever. Period. But it does - and when it does, there is help. Maybe you have lived with abuse, maybe it happened just once; maybe you work or live next to someone who is being abused right now. For all the women who have ever endured domestic abuse . . . the poetry of Ntozake Shange and Lisa Dietz speaks softly but strongly. With No Immediate Cause by Ntozake Shange
```

### Performance text (classify this)

```text
With No Immediate Cause

every 3 minutes a woman is beaten
every five minutes a
woman is raped/every ten minutes
a lil girl is molested
yet i rode the subway today
i sat next to an old man who
may have beaten his old wife
3 minutes ago or 3 days/30 years ago
he might have sodomized his
daughter but i sat there
cuz the young men on the train
might beat some young women
later in the day or tomorrow
i might not shut my door fast
every 3 minutes it happens
some woman's innocence
rushes to her cheeks/pours from her mouth
like the betsy wetsy dolls have been torn
apart/their mouths
menses red & split/every
three minutes a shoulder
is jammed through plaster and the oven door/
chairs push thru the rib cage/hot water or
boiling sperm decorate her body
i rode the subway today
& bought a paper from a
man who might
have held his old lady onto
a hot pressing iron/i don't know
maybe he catches lil girls in the
park & rips open their behinds
with steel rods/i can't decide
what he might have done i only
know every 3 minutes
every 5 minutes every 10 minutes/so
i bought the paper
looking for the announcement
the discovery/of the dismembered
woman's body/the
victims have not all been
identified/today they are
naked and dead/refuse to
testify/one girl out of 10's not
coherent/i took the coffee
& spit it up/i found an
announcement/not the woman's
bloated body in the river/floating
not the child bleeding in the
59th street corridor/not the baby
broken on the floor/
there is some concern
that alleged battered women
might start to murder their
husbands & lovers with no
immediate cause"

i spit up i vomit i am screaming
we all have immediate cause
every 3 minutes
every 5 minutes
every 10 minutes
every day
women's bodies are found
in alleys & bedrooms/at the top of the stairs
before i ride the subway/buy a paper/drink
coffee/i must know/
have you hurt a woman today
did you beat a woman today
throw a child across a room
are the lil girl's panties
in yr pocket

did you hurt a woman today
i have to ask these obscene questions
the authorities require me to
establish
immediate cause
every three minutes
every five minutes
every ten minutes
every day.

TRANSITION Women may be afraid of strangers, but it's a husband, a lover, a boyfriend, or someone they know who is most likely to hurt them. According to a U.S. Justice Department study, two-thirds of violent attacks against women are committed by someone the woman knows. In the United States, one of the most dangerous places for a woman is her own home. According to the FBI, approximately 1,500 women are killed each year by husbands or boyfriends. Lisa Dietz provides graphic insight into this brutal existence. Woman, Do You Know? By Lisa Dietz

Woman, Do You Know?

Woman
Do you know your name?
The one you had
Before the scars
Thick make-up covering
Sun-glassed face
Over red, blue, oily stains
Cropped hair in a fit of passion
Unpaid hospital bills
The broken nose, bruised ribs
Finger, elbow, knee, vagina
Nothing left untouched.
Woman
Do you know where you live?
In a suburban house
Redwood fence
Haunting memory-dream reality
Locking doors, banging walls
Wipe away the blood
Scramble for the phone
The line is dead
As the door breaks down.
Woman
Do you remember who you were?
Little girl
Whistling carefully into blades of grass
Stomping out beetles
Climbing crop-branched trees
Your fairy palace fortress
Escape the noise
A dream of being married
Raising children
A strong man
"He'll protect me
It'll be different then."
Woman
Do you see your children now?
Crouched like fetuses
Climbing beneath the covers
Stomping pillows on their ears
A wish for dreams
Praying, the way you taught them
"Please make daddy stop
Please let mommy
End the screaming."
Woman
Do you know what you really deserve?
When the time comes for apologies
Grasping the tenderness you live for
His lips wet on yours
Fingers tracing pain-lines on your face
"I'll never do it again, I promise."
DON'T BELIEVE IT.

In the dawn of reprieval
Gather what's left
Before you're dead
Choke back fear
And find your escape.
```

---

## IC-1864: Women and

- Title: Women and
- Author (byline): Not specified
- Work: Women and
- Publisher: SpeechGeek
- Publication date as stated: 2017
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 698
- Already set (do not supply): none

### Source block (context only)

```text
Women and Scars by Deb Royce
ISBN: 978-1-61387-114-0
Copyright 2017 by SpeechGeek.
Free performance of this play for high school and college level competitive forensics is
permitted. All other rights reserved.
This PDF version of this selection, e-published in 2015, is identical to the printed published
version of this same publication dated 2015. This statement along with the entire printed PDF of
this publication must be presented at any National Speech and Debate Association District or
National event for the script to comply with NFL rules per the request of the Executive Director.
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
At first glance
You might not see
Behind the curtain of her hair and headscarf
But some women are aware of our wounded
Like a sick sixth sense
We can spot survivors
Like a sonar ping from a lost submarine.

I am reading her.

The right side of her face Is young and beautiful The color of cardamom the smoothness of silk

The left side of her face
Like a melted candle
The skin drips down
And meanders into an ancient riverbed
Cracked and barren
Eroded away
By streams of tears?
It's hard to say

And her one eye is white, like it's covered in liquid paper Like the mistake was her seeing

Grotesque

She is a gargoyle carved by a hateful hand
If she wasn’t always stone, she surely is now
Because that’s what happens
When your soft places go stale
When your happiness hollows out
When your body is used as a weapon against you

I've heard that in some countries
Acid rains down from the hands of men
To cut women down to size
To burn out the sin of beauty
To avoid the temptation of other men
For who could want such spoiled goods?

They call it honor
We call it horror
They call her property
I call it prophecy
Because women were always the keepers of blame
He was the wick, she was the flame
How could he be responsible for his actions?
Hers was the face that launched a thousand ships
She was the one who held an apple to his lips and sighed
“Just a bite”

So?

He denuded her mind of education - calling her the muse, merely inspiration
He industrialized her hands for exploitation - she was good enough to work, but not enough to
earn
He strip-mined her womb for labor - she had a right to procreate, if that’s what he wanted
He hunted her body for meat
He hunted her body for sport
He hunted her body for no reason at all
Just to watch it wither and die.
Don’t you feel powerful?

And this woman
(The one with the scars)
She is no different
She is the story we all tell our daughters
Like a watercolor Picasso
A jungle of skin
A jumble of feminine burden
A topographic map of everything that is wrong with where she comes from
With where she is
With where we all live

But as bad as it is to see her bear the yoke
To see her shopping for groceries
Choosing what foods she can consume
with only half a working face

This is the sick part:

My mouth hungers
while throat parched
My eyes ache
While hands tremble

What started as a glance is now a full trance Of envy

She wears her history on her face
like the wrinkles of hateful wisdom
And she cannot escape
But who can?
Who can escape the marks history and fate leaves on us?

No woman can. Not her. Not me.

That same death mask Lives inside of me It is the inner structure of my smiling skull

Those same dripping scars
Line cage of my chest
The insides of my legs
That whiteout eye is mine
Looking out at the world through damaged lenses

We are the sisterhood of burden
A society of souls
That you can’t call survivors
Because parts of us didn’t survive
We only look that way in this lighting
With thick makeup
And contortionist skills that make
Our grim mouths grin

We are monuments to what love can do When it is loaded into the barrel of a cannon And fired through a nursery of hope

All the while I recognize her as my own reflection
Still, echos of my worst self cry out
At least when the world sees her
They cannot unknown her
They cannot ignore what life has done to her

They may choose to judge
Or handle with silk gloves
But they know there is damage
They know there is pain
That the monster she is now was never the life she had planned

Some of us aren't so lucky
Some of us wear our terrors on the inside
We survive our horrors in silence
The world never knows
```

---

## IC-1865: A Working Girl Can’t Win

- Title: A Working Girl Can’t Win
- Author (byline): Deborah Garrison
- Work: A Working Girl Can’t Win
- Publisher: Random House, Inc.
- Publication date as stated: Feb 2000
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 856
- Already set (do not supply): none

### Source block (context only)

```text
Author: Deborah Garrison
Book: A Working Girl Can’t Win
ISBN: 978-0679451457
Publisher: Random House, Inc.
Date(Month/Year): Feb 2000
```

### Introduction (context only: never use it for content warnings)

```text
These are the twentysomethings, who live in the post-hippie '80s and '90s and feel that the movements of the '60s did not change the world. The legacy to the twentysomethings is a bleak future in which they can never hope to be as successful as their parents. Disenchanted with treading the career path and pursuing "pointless jobs done grudgingly to little applause,” life is a series of vignettes, of incidents wherein one tries desperately to derive some deeper meaning. Selections from A Working Girl Can’t Win by Deborah Garrison.
```

### Performance text (classify this)

```text
Worked Late on a Tuesday Night
Again.
Midtown is blasted out and silent,
drained of the crowd and its doggy day.
I trample the scraps of deli lunches
some ate outdoors as they stared dumbly
or hooted at us career girls-the haggard
beauties, the vivid can-dos, open raincoats aflap
in the March wind as we crossed to and fro
in front of the Public Library
Never thought you'd be one of them,
did you, little lady?
Little Miss Phi Beta Kappa,
with your closetful of pleated
skirts, twenty-nine till death do us
part! Don't you see?
The good schoolgirl turns thirty,
forty, singing the song of time management
all day long, lugging the briefcase
home. So at 10:00 PM
you're standing here
with your hand in the air,
cold but too stubborn to reach
into your pocket for a glove, cursing
the freezing rain as though it were
your difficulty. It's pathetic,
and nobody's fault but
your own. Now
the tears,
down into the collar.
Cabs, cabs, but none for hire.
I haven't had dinner; I'm not half
of what I meant to be.
Among other things, the mother
of three. Too tired, tonight,
to seduce the father.

TRANSITION Young adults feel that they have to do fantastic things by their mid-20s, like they see in the media. Twentysomethings are depressed because they believe they've been "sold" on a lifestyle — the 20s aren't as easy as their idle thoughts.

An Idle Thought
I'm never going to sleep
with Martin Amis
or anyone famous.
At twenty-one I scotched
my chance to be
one of the seductresses
of the century,
a vamp on the rise through the ranks
of literary Gods and military men,
who wouldn't stop at the President:
she'd take the Pentagon by storm
in halter dress and rhinestone extras,
letting fly the breasts that shatter
crystal--then dump him, too,
and break his power-broker heart.
Such women are a breed apart.
I'm the type
who likes to cook--no,
really likes it; does the bills;
buys towels and ties;
closes her eyes during kisses:
a true first wife.
The seductress when she's fifty
nobody misses, but a first wife
always knows she's first,
and the second (if he leaves me
when he's forty-five) won't forget me
either. The mention of my name,
the sight of our son--his and mine--
will make her tense; despite
perfected bod, highlighted hair
and hip career, she'll always fear
that way back there
he loved me more
and better simply
for being first.
But ho:
the fantasy's unfair to him,
who picked me young and never tried
another. The only woman he's ever left
was his mother.

TRANSITION For many American women, rushing from work to home to school—then getting up and doing it all over again—has become the norm. Juggling a spouse, children, boss and friends all adds up to a hectic lifestyle that can put your physical and mental health in the dumps. It’s easy to conclude that A Working Girl Can’t Win.

A Working Girl Can't Win
Is this the birth of a pundit
or a slut? Is she the woman
they courted for her youthful edge
or a kiss-and-tell bimbo,
a careerist coquette?
The loyal daughter to spin doctors
losing their hair or soul sister
to feminist essayists everywhere?
Is her meteoric rise the source
of her potential demise?
Is her worldview equal parts
yuppie whine and new-age rumor?
Can we get a biopsy on her latest
breast tumor? Is she a failed
anorexic, or a diet-pill faddist
who'll let it all go and get fat
in her fifties? Are her roots
rural, right-leaning? Is she Jewish,
self-hating? Past her sell-by date,
or still ovulating?
Will her husband talk?
Does he mind her success?
Does anyone know -- does he see
her undressed? Has she been
photographed? Will she play
truth or dare? And more to the point,
does anyone care?
Come next year, will the masses
be reading her story? Will she be
on the cover, or well past her glory?
Either way, we'll move on, and she'll tire
before long: only her children will grieve
at the way she was wronged.

TRANSITION But maybe failing isn’t so bad. In fact, it may be the only rescue these twentysomething superwomen can hope for. It’s not like you can just walk into your bosses office and say “Please, fire me.”

Please Fire Me
Here comes another alpha male,
and all the other alphas
are snorting and pawing,
kicking up puffs of acrid dust

while the silly little hens
clatter back and forth
on quivering claws and raise
a titter about the fuss.

Here comes another alpha male--
a man's man, a dealmaker,
holds tanks of liquor,
charms them pantsless at lunch:

I've never been sicker. Do I have to stare into his eyes and sympathize? If I want my job I do. Well I think I'm through with the working world, through with warming eggs and being Zenlike in my detachment from all things Ego.

I'd like to go
somewhere else entirely,
and I don't mean
Europe.
```

---

## IC-1866: Yell-Oh! Girls Poetry Collection

- Title: Yell-Oh! Girls Poetry Collection
- Author (byline): Vickie Nam (ed.)
- Work: Not specified
- Publisher: Harper
- Publication date as stated: Aug 2001
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1124
- Already set (do not supply): none

### Source block (context only)

```text
Author: Vickie Nam (editor)
ISBN: 978-0060959449
Publisher: Harper
Date (Month/Year): Aug 2001
```

### Introduction (context only: never use it for content warnings)

```text
As young children, we don’t understand race or skin color. We assume everyone is the same. In fact, as a child I remember telling my mother that I was vanilla and my best friend was chocolate – as if the race issue was as simple as flavors of ice cream. If only this were so. Unfortunately, once society imposes itself on our view of the world, there comes an almost earth-shattering moment when we realize race is much more complex and divisive than flavored ice cream. Poems from Yell-Oh! Girls edited by Vickie Nam
```

### Performance text (classify this)

```text
Innocence by Debra Yoo (pg 153)

The first day of kindergarten. The classroom, filled with happy children A sea of blond and brown heads

And yes, one head of black.

Me. I didn’t care. I didn’t notice.

But everyone else did.

I walk in the classroom. Whispers follow, buzzing with gossip. Secrets float from child to child.

I tensed, everyone was looking

At me. They stared. I stared back.

Why was everyone watching me?
I see a boy about my age.
Pulling his eyes at the corners.
Making them sharp and pointed.

I realized, he was making fun

Of me. But why? Because of my eyes?

I couldn’t understand.

That first day was horrible. Girls giggling, boys pointing. No one who would be my friend.

I noticed, they were staying away

From me. I almost cried. Tears sprang to my eyes.

But I kept my pride.

I boarded the bus for my ride home. I felt safe, finally, at last. Two boys sat in front of me.

They turned. “Chink,” they said.

Me? Chink? The word brought sadness to my soul.

Dejection crossed my face.

That first day hurt me. Hurt my core, my only being. But I finally realized.

People were prejudiced

Against me. It came like a tidal wave. Smashed my spirit.

My eyes opened to the harsh world around me.

TRANSITION You see, racism isn’t just black and white. – it’s also Asian, Hispanic, and people of the Middle East. Today our focus is on Asian-Americans who struggle not only with the issue of race, but also culture. The blending of cultures is unique, significant and often cherished; but the beauty of a blended culture also can come with a burden . . . a burden of feeling as if you don’t truly belong to either culture. Two by June Kim explores this cultural dichotomy.

Two by June Kim (pg 8)
Raised in two separate cultures
Growing up in a world with customs
Familiar at home and foreign in society

Reaching, roaring, Rocking between things that surround And lessons of a homeland farther away

Seeing crowds of endless faces different from your own Hearing English words mixed with native tongues Tasting foods loaded with thick flavor and warm spices

Scarlet passion
Craving, calling
To accept a blend of opposites
To create an experience unique to you
A struggle to convey thoughts to those who cannot
understand
Despite the
Searching
Studying what cannot be taught or red in lines

The experience that only comes from
Living, loving
Leaving one behind
The choice to abandon one completely for the other
Causing betrayal and ignorant hatred
Compulsions that wrench you violently from both sides
Fighting, fearing
Fitting into two places
Two cultures
Or maybe none.

Untitled by Olivia Chung (pg 266)

At first glance, they looked at my face and prepared
themselves in advance
For what kind of person I am, an Asian.
I watched them uncomfortably guess my “original”
nation.
Chinese? Japanese? Malaysian?
This is the overplayed scenario like the replayed songs
on the radio,
Over and over like there ain’t no end to it yo.

Since the first day of school I heard it.
Ching chong chinaman, chinky winky twinky
DO YOU SPEAK ENGLISHEE?
From the first moment, I felt it.
Can you really see through those eyes?
Oh how cute, two oriental girls. Are you twins?

I listened to their ignorant remakes as their sharp words pierced my heart.

I allowed them to form my identity and tell me who I was. Bruce Lee, Michelle Kwan, Yan Can Cook and so can you! Because pigeonholed, it was all I was told. Aren’t you gonna be a doctor? All Asians are good at science right?

So now you’re thinking, “What? Things like that don’t happen to me. I hear no evil, I see no evil.hear no evil, see no

evil . . no evil.”

You tell me you don’t know what it means to be Asian, born and raised in a white nation, you’re third generation, “I’ve never seen discrimination.” I’ve read about Hitler and his evils of intended entire elimination of Jews. I’ve heard about Rosa Parks with the blacks-at-the-back-of-the-bus laws — to obey, she

refused.

But me . . . I’ve never seen discrimination, never felt racial humiliation,

never experienced segregation.

So you know you’re Asian if you leave your shoes at the front door. That’s your definition of tradition. You consider yourself Asian on this one condition!

I am who I am, I be who I be,
I am who I am, I be who I be
People will see me for me and award me for ability,
Praise me for attending ivy league,
Hire me for working so hard, so hopefully,
Holding onto a vision of my future reality . . .

But . . .

What if they fire me?
Look at Dr. Wen Ho Lee —
Maybe innocent, maybe guilty
Targeted unfairly ‘cause of his ethnicity.
“You know dem chinese. They’re either restaurant
owners or spies.”

I despise the lies seen in society’s eyes.
See, even though
I am who I am and I be who I be
People can’t see me for me.
That’s the reality.

Can you hear the evil? Can you see the evil? The sugarcane harvesters, sweatshop workers, picture brides, interned Japanese Americans . . . all the immigrants who came with high hopes seeking liberty stretching from sea to shining sea, singing my country ‘tis of thee, sowing seed of strife in hopes of a better life . . . sacrifices and sweat, sacrifices and sweat, sacrifices and sweat, and sweat

These people faced persecution in the form of piercing painful prejudices pointing at them at every place . . . political pariahs, unable to speak their piece, unable to speak peace.

That is why I get offended when you ask me where I’m
really from.
That is why I fight for justice while obstacles continue
to come.
That is why I call myself Asian American.
I am who I am, I be who I be
See me for me,
Then you’ll get the reality.

Who is Singing This Song by Janice Mirikitani (pg xxxiii) Who is singing this song?

I am.

pulled by hands of history to not sit in these times, complacently, walkmans plugged to our ears, computers, soap operas lulling our passions to sleep. We are required by legacies of grandparents, parents, our enslaved and servant ancestors, our heroes and sheroes, our fighters for freedom, to be now the storm of hands that wave in protest against apartheid, racism, classism, sexism

war, hate crime violence and indifference to the poor.

Who is singing this song?

I am.
We survive by hearing.
We speak to each other,
offering choices,
to love, to dream,

I DARE YOU, dare you to love, to dream . . .

Who is singing this song?

I am.

You are.

Our music is beautiful.
```

---

## IC-1867: Yesterday I Saw the Sun

- Title: Yesterday I Saw the Sun
- Author (byline): Ally Sheedy
- Work: Not specified
- Publisher: Summit Books
- Publication date as stated: Feb 1991
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1428
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ally Sheedy
ISBN: 978-0671731304
Publisher: Summit Books
Date (Month/Year): Feb 1991
```

### Introduction (context only: never use it for content warnings)

```text
The publisher claims that Ally Sheedy’s book of poetry, Yesterday I Saw the Sun, is "a work of fiction". If only that were the case. Then the contents in it wouldn't break your heart. Ally Sheedy, famous in the 80s as part of the “Brat Pack” – Remember her angst ridden role in Breakfast Club – was and is more than just a celebrity. She is a survivor who gives new definition to the word. From drug addiction and domestic abuse to questioning her own sanity and a desire to end her own life . . . Ally Sheedy has survived. Today she lives with her daughter, Rebecca, in NYC and is still working in the film industry.

Selections from Yesterday I Saw the Sun by Ally Sheedy
```

### Performance text (classify this)

```text
Xmas Break

So why’d you hit me, huh? Did you have to go and do that? And I’ve been working so hard on myself, too.

I had a moment of clarity One night It was during Christmas.

I was outside barefoot in the East Coast snow.

Dead of winter, dead of night.
He was looking for a rooftop murderer.
Running around the house with
a baseball bat.
“Shut up and get inside!”
he screamed.

I looked up.
The sky was filled with bright blue stars
twinkling like
Christmas lights.
Smoke was curling out the chimney of his cozy hearth..
It was cold.

Crouching down by a bush in the rocks
I listened for the frantic sounds
of escaping rooftop killers.
He tears past me with the bat.
Slams into the house.
“Get inside!” he screams again.
So I follow.

I sit on the sofa by the Christmas tree
looking up again.
This time at the ceiling.
Sounds of bangs and frantic thumps
rain down on my head.

I hug my knees into my chest and count in silence

backward slowly with each breath from 99.

So sad.

When I reach 36, he is back.
With his bat.
“Who left the window open?” he demands.
Scary. Low.
I look all around me for the answer.
But we are alone.

“I did,” I sigh. “I guess.”

He comes up in my face.
His teeth are stained dark.
The eyes are crazy.
The bat’s an inch from the bridge
of my freckled nose.
“There’s no one else here,” he breathes.
“I guess you did.”

Have you ever known an angry crazy drinking man? Have you ever been thrown in with that rage? Alcoholic sweat -- Do you know that smell?

I do.
I did.
I left the window open.
He breathes.
I keep his bat
in view.

I try to find my mind.

In the East now for a week prisoner insane

(Beat – speaker shifts from speaking to the audience to speaking to her abuser – focus should change as well as demeanor)

You grab me by the chin and
and stare into my eyes.
“You left an open window. In there. Don’t lie.
Tell me who you are seeing.”

It comes to me
a flash of
what will come.
There is no mistaking or escaping this.
You want to kill me.
I mean I saw it was beyond
returning sane.
“NO ONE I swear. I’m so sorry. Forgive me, baby,

please.”

(Beat – speaker shifts from speaking to her abuser to speaking with the audience again)

Without a backward glance I let go the rope
slipped away
drowned myself
in chemical reprieves.
And I knew where the door was. All along.

Coke’s on the table a girl on the floor bottles all around

(Beat – speaker shifts from speaking to the audience to speaking to her abuser – focus should change as well as demeanor)

You fall unconscious and I try
to rub away the dread
of what I know.
I long to sleep and dull
that clear moment when I’m hit.
To render weightless what I bear in what I’ve seen.
I can forget. I can forget.

And yet I stay awake
trying to retrieve
the moment
where you say
I asked for it.

TRANSISTION

And finally, at the age of 27, Ally Sheedy realized that she needed help – She checked herself into Minnesota's Hazelden Foundation. She begged for help with a drug addiction, but in reality the drug use was a symptom of a much larger problem . . .

MY DISEASE

I don’t understand this sickness.

it is the observer
watching me through a telephoto lens
reporting on me in its private tabloids
waiting patiently in the bush

like the fan with a gun
in a fascinated all-encompassing horrifying trance
it waits
distorting my every detail
magnifying y every transgression
hypnotic

some days are nightmares
coming off the drugs
I look at my skull in the mirror and wonder
how so much rage can be contained within
such a narrow circumference
of bone
there is a rec room at the Center
with a saggy well-worn couch
while the others watch CNN and smoke
I crouch in the corner and hold my head together
with my hands
to keep it from breaking in a cracked web.

I can see the sickening thoughts and violent images
come crawling out
like so many little black spiders
swarming over my face m y neck my eyelids
When there is a break in the action
I stand up and go to the vending machine
to get a Diet Mountain Dew.

I used to sit at a kitchen table in the sun
and hem myself in safely with stacks of morning papers.
I drank coffee watching the clock tick
watching the orange-papered kitchen shelves
and the little black cat on the garden wall.
I was afraid to move.

Now I am split beyond my shell
and roam as far as the grounds can go
I shoot basket after basket
I swim lap after lap
and there are nurses who, like creases in a sheet,
smooth me into flattened sleep

but mostly the sickness with the gun is absent
unsuccessful yet in tracking me down
I have been safe here for three weeks
within walls that are, finally, not of my making.

For the first time in my life
I gladly welcome my restraints.
There is no prison like the one
where I used to live.

TRANSISTION

Three-months drug free, Ally was released from the treatment center . . . cured of her drug addiction, but still fragile . . . so fragile inside. In this last poem, she creates an extended metaphor, comparing her daily struggle to that of a crippled baby bird . . . “Please let me live”

HEROICS

I found a baby bird yesterday.
I was climbing up a hill.
the bird was by the side of my path
fluttering in the undergrowth.
It had a crippled left leg and looked up at me
with the sweetest darkest little bird face
Don’t kill me, I thought I heard it say.
Please let me live.
I cupped it in my hands and held it to my heart.
I love you, I said.
I will save you from the coyotes by carrying you to a

safer place.

Really, you are very fortunate that I happened by.
But this bird did not seem to agree
and struggled desperately in my grasp.
Its wings beat and beat against my chest --
fighting me.
I did try to calm it
but it was drowning.
Little bird, I said telepathically. Why struggle so?
I have always longed to swim and float on the waves of

someone else’s
deep desire to save me.
Can’t you relax and enjoy it?
But it only fought me harder
Angrily dissolving into a tiny puddle of tears
and wet feathers
within my grasping palm.
This was an ungrateful creature.
I opened my hand to the sun
to see what was left of it.

I was halfway up the hill now
the trail becoming steep and narrow
with jagged rocks falling away on either side.
I looked to the top of the hill
and wondered why I was still trying.
Such an effort to conquer another canyon trail.
For what?
To feel I was in some small way
correcting my misshapen parts?
To achieve a victory over an obstacle?

These were the philosophical ramblings
banging pointlessly inside my head.
This was my state of mind.
You are an idiot, I said.
Alone on this hill.
Trapped, exhausted, covered with dust and
crying suddenly at the ludicrousness of it all.

That was when the bird stirred in the sun and
lifted its small black head.
Did it think of freedom?
It seemed conflicted for a second
then seized its chance
and zoomed straight up into the air
toward the sun
it leapt
broken leg and all
before I could grab it again.

I saw it suspended for a moment
in a frozen shining silhouette
of absolute abandonment and wild joy
and then I could swear to you I heard that little bird

laugh
crying out in victory
before it feel onto the rocks
disappearing below.
It was to me an act of heroism that made me envious.

A bird had the courage to throw itself off a mountain
to escape
the sweat and constraint
of a human hand.
Where is my leap?

And, you know, I did keep climbing that hill
I didn’t turn back halfway
because I needed that moment
When I reached the top and faced
for a split second
the desire to throw myself over the side
to fall
completely free
unsaved
unstopped
unchained
recklessly abandoning myself to gravity and to
everything
escape
I want it so much
Don’t I?

I remain. It’s my struggle to stay alive and be braver

than
a little bird
who has suffered from a crippled leg
but never – once – a crippled soul.
```

---

## IC-1868: You Tell Me How to be a Girl in 2010

- Title: You Tell Me How to be a Girl in 2010
- Author (byline): Eve Ensler
- Work: I am an Emotional Creature
- Publisher: Random House
- Publication date as stated: 2010
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 900
- Already set (do not supply): none

### Source block (context only)

```text
Author: Even Ensler
Book: I am an Emotional Creature
ISBN: 978-1400061044
Publisher: Random House
Date (Month/Year): 2010
```

### Introduction (context only: never use it for content warnings)

```text
Women are subjected to many stereotypes in today’s society. Movies and television shows suggest that all women are air-heads. Magazine and other advertisements push photographs of very slender and “sexy” women into the minds of children. Men’s magazines write articles on how to “dupe” a girl into sleeping with them. Haven’t we, as a society moved past the sexist ideals of the past? Judging from the way the media portrays women, it seems as if things are only getting worse. Television and movies shows tend to stereotype women (One of the most common ways television depicts teenage girls, especially, is as a dumb, ditzy girl with a credit card. The girl’s interests are usually limited to make-up, boys, clothing and shopping. Movies such as Clueless, Legally Blonde, and other such movies encourage the idea that teenage girls and women are ditzy, stupid, and superficial. I deny all of these stereotypes, but You Tell me How to be a Girl in 2010 by Eve Ensler.
```

### Performance text (classify this)

```text
Questions, doubt, ambiguity, and dissent have somehow become very un-masculine. Authoritarian maniacs are premiers, czars, and presidents.

Each one is more righteous than the next.
Each town they bomb
each human they kill
is done for "humanitarian" purposes.
People don't own the water in their own village
and they certainly don't own the diamonds and gold.
Millions are forced to make dinner out of garbage and
dust
while Russian businessmen and movie stars
are buying 500-million-euro villas on C’te Sud.
Bees have stopped making honey.
People are drilling in all the wrong places.
The U.S., Russia, Canada, Denmark, and Norway all claim
the Arctic
but none of them seem to care that the polar bears are
drowning.
They are fingerprinting, photographing our licenses and
teeth.
Big Brother is now in our phones, our pods, our PCs.
Not one of us feels even a little safer.
New Age mental health providers turn
out to be former war torturers with beards.
And the pope in a dress showing off his
ermine trim and cuffs
is telling everyone that
people kissing people they love is the greatest evil.
A woman running for U.S. vice president
believes in creationism
but not global warming.
Why is everyone so much more afraid of sex
than SCUD missiles?
And who decided God wasn't into pleasure?
And if the hetero nuclear family is so great
how come everyone is fleeing it
or paying their life savings just
to sit in a room with a stranger and cry about it?
The Iraq war cost nearly $3 trillion.
I can't even count that high
but I know
that money could have
would have
ended poverty in general
which would have canceled terrorism.
How come we have money to kill
but no money to feed or heal?
How come we have money to destroy
but no money for art and schools?
The fundamentalists now have
billion-dollar private armies.
The Taliban is back
but never went away.
Women are burned, raped, bludgeoned, sold,
starved, and buried alive
and still don't know they are the majority.
Water is clearly nearly running out
but even in the desert where there's serious drought
the golf courses are green and lush
and the swimming pools are full of water
for the twelve rich people who might decide to come.
Special people adopt hand-picked babies in faraway
lands.
Their flights there cost more
than the babies' parents made
this year.
Why don't they just give it to them?
Slavery is back
but never went away.
Just ask anyone who's been whipped
how deep the legacy.
Six million dead in the Congo
and they never made the news,
and don't tell me it doesn't have
to do with color
and minerals.
Poor folks are dying first
From hurricanes
Shame
Tsunamis
Radiation
Pollution
Floods
And neglect.
Rich folks
just put up fancier super-electrified gates
on their private perfect cities.
Everyone's having "benefits"
and throwing fancy parties
with lots of swag
so the rich people feel good about giving
away the tiny little bit of the whole lot they have.
But no one really wants to change anything.
If you really want it
you have to give something up
like everything
and then those that have, wouldn't,
and then who would they be?
And that's too complicated
so they write checks
and keep doing the same old things.
Selling change.
Making revolution profitable.
Corporations own everything anyway
even our hippie jeans, memory cells, and rain.
Why do so many women leaders look like Margaret
Thatcher
and act even meaner?
Why doesn't anyone remember anything?
And how come rich bad people
get paid lots of money to give speeches
and poor bad people are tortured
and in prisons?
Is there anyone in charge?
Or is this whole thing spinning out until it explodes
or dissolves?
And if there is something we can do
why aren't we doing it?
What happened to fury?
What happened to accuracy
or accountability?
What happened to not showing off your wealth?
What happened to kindness?
What happened to teenagers rebelling
instead of buying and selling?
What happened to teenagers kissing
instead of blogging and dissing?
What happened to teenagers marching
and refusing
instead of exploiting and using?
I want to touch you in real time
not find you on YouTube,
I want to walk next to you in the mountains
not friend you on Facebook.
Give me one thing I can believe in
that isn't a brand name.
I'm lonely.
I'm scared.
Girls younger than me are giving blowjobs
in homeroom
and they don't even know it's sex.
They just want to be popular
and get some respect.
Most girls my age are taking pills
or not getting out of bed
or eating or starving
or getting nose jobs or implants
or getting cut
or twittering away
or covering themselves
or desperate for a way
to be awake without faking
to be alive without freaking
to be serious
to be true
to even think of loving someone
when we're already doomed.
You tell me how to be a girl in 2010
I say let's go for it
if it's all coming down.
I say let's speak it
let's fight it
let's right it
there's nothing to hold on to
if it's already gone.
They left it to us.
It sucks but it's true.
It's you and me baby.
```

---

## IC-1869: Across the Mississippi

- Title: Across the Mississippi
- Author (byline): Alan Kaufman
- Work: The Outlaw Bible of American Poetry
- Publisher: Thunder’s Mouth Press
- Publication date as stated: Nov 1999
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1102
- Already set (do not supply): none

### Source block (context only)

```text
Author: Alan Kaufman
Book: The Outlaw Bible of American Poetry
ISBN: 978-1560252276
Publisher: Thunder’s Mouth Press
Date (Month/Year): Nov 1999
```

### Introduction (context only: never use it for content warnings)

```text
On December 1, 1955, Ms. Rosa Parks walked into history when she refused to give up her seat for a white man on a Montgomery Alabama bus. She was arrested for her defiance, and challenged segregational riding policies in court. Although her local court challenge failed, it brought light to the situation and sparked the Montgomery bus boycott. "For a little more than a year, we stayed off those busses. We did not return to using public transportation until the Supreme Court said there shouldn't be racial segregation," Ms. Parks said. . . . Today I have another story to tell, not one of segregation, but one of how community is forged on a bus-ride Across the Mississippi by Alan Kaufman.
```

### Performance text (classify this)

```text
We crossed the Mississippi's muddy brown expanse in a blinding thunderstorm, creeping over a big suspension bridge whose name nobody knew, in a bus with sheets of rain battering windows feeble as eyelids trembling in fear, and we could hardly see but for glimpses of suspension cable over the sullen river, on the banks houses like garbage cans with pedal lids, and over it all a sky the color and consistency of clay, with an occasional lightening bolt seaming it like a cheek wrinkled in angry laughter. And we didn't even know that we were crossing the Mississippi until that bottle of Fleishman's whiskey fell from the overhead luggage rack and the lanky driver with hair in his eyes, and rolled sleeves, and a pack of filterless Pall Malls cast a glaring boozy eye our way in the rear view mirror, pulled over the bus right there on the bridge and announced for the twentieth time since leaving New York City that Federal regulations prohibit booze consumption aboard, which hadn't made a difference to anyone for over a thousand miles so far, and didn't make a difference now.

The drunkards still snuck drinks and the sober people didn't. And he put the bus into high gear and gunned it. And this was as we crossed the Mississippi, though we didn't even know it. Assumed it was just some trash river, as some birds are trash birds-say, the robin. A trash river, some of us thinking, a love canal, an above-ground industrial sewer of radioactive Republican by-products by which to contaminate and kill the poor on the merry road to profit. So we didn't even know that we were crossing that famous river, had no way to know. Most of us had never seen it. I had come from a transient hotel room east of the Hudson to find my gain in California. I didn't have much money. When the bus pulled into a rest stop, I stayed on board-didn't stumble off like the others blear-eyed drunk on lack of sleep to gorge myself on fast food.

I was making it across the continent on three loaves of wonder bread and two jars of peanut butter and one of jam, and so far so good. And that bottle of Fleishman's that dropped out missed a passenger's big pink ear by a hair's breadth, bounced without shattering, and rolled to a stop against the bolted leg of a chair, and the passenger, his name as I recall was Chopper, reached down, retrieved the bottle, held it up with a big grin and while everybody in the back of the bus roared with approval, he waved it at the driver, who stopped the bus and made the speech. And then, after a moment's sullen pause, suddenly the driver's voice came on again, but kinder, and he said with a gentle pride that surprised most of us I think: "You are crossing the Mississippi River, on the Sasquahana Bridge, and are about to enter the town of Shilo Springs."

And the effect on us of this announcement was like what maybe the Hebrews felt when Moses told them after all their wanderings and afflictions: You are crossing the Jordan River. You are entering the Promised Land. Because everyone became very serene suddenly, and reposed quiet in their seats, some with heads cocked, and just slow-watching the passage occur. The ex-con wearing the shower cap, the hungry computer jock, the professional piercer with earrings in his eyes and ears, the old woman with a garbage bag containing all her possessions riding on her lap, the Nam vet with a baseball cap gray beard blue eyes the color of anti-freeze, that girl who looked like every girl I'd ever seen, the silent man who refused our repeated offers of whiskey with a tight, unresentful smile, and even the loud, hard-muscled mustached guy with a face like a skinned and butchered leg of steer and who claimed to be a lumberjack (but whom many of us figured for a killer of some kind, in flight from his latest barroom manslaughter), everybody, and that includes that stiff and uncommunicative respectably-dressed middle-aged lady with silver hair who shuddered when asked by the ex-con for a match, everyone without exception seemed to give up their tension and their fear like the dying surrender of a soul on its way to final rest and we sat back and just let the transition occur. And on the other side of the Mississippi River it was like an older, more innocent time in America. There was a kind of canal branching from the main body of water, and less turbulence to the rain and we could see clearly through the windows as an old time boat paddled its way to the interior past banks lined with weeping willows, and the houses were bigger than they'd seemed from the bridge, they were stately gray with age and big columns announced their facades and dark mandala-shaped stained glass attic windows, the kind you see in pictures in magazines, suggested, at least to my mind, the sanctuary and safety of a family cemetery vault, of time and place and the dignity of knowing where you come from and where you'll probably end up too. And this calmed me, calmed everyone I think, and then the bus met, to our delight, a roadblock and we had to detour through little old time streets and it was peaceful for a few brief minutes, and then the bus drew up to the edge of a puddle as wide and deep as a stream and the brakes hissed and the driver's voice announced: "We are going to ford this puddle," and we cheered.

And just then a man dressed in a green flannel shirt and denim coveralls stepped from the door of one of the houses and stood there stock still on the porch to watch. The rain had lessened and as the bus descended, almost kissing the rim of the tires, we watched the man's face watching us with a kind of compassionate interest, as if encouraging our success, and when the bus climbed out on the other side dripping like a baptized bather the driver braked again. "We'll sit here a minute," he said "to let the brakes dry." And that man on the porch, I guess he saw our faces dim in the tinted rain swept-windows, and lifted his hand in a wave. A few of us waved back, and he beamed a smile. Then he turned and entered the house.

We heard the porch door slam, crisp and clean in the pattering rainfall.
```

---

## IC-1870: Albuquerque

- Title: Albuquerque
- Author (byline): “Weird Al” Yankovic
- Work: Weird Al: The Book by Nathan Rabin with Al Yankovic, Pgs 166-167
- Publisher: Scholastic
- Publication date as stated: Jan 2016
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1248
- Already set (do not supply): none

### Source block (context only)

```text
Author: “Weird Al” Yankovic
Book: Weird Al: The Book by Nathan Rabin with
Al Yankovic, Pgs 166-167
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
(Pg 166-167) Way back when I was just a little bitty boy

living in a box

under the stairs in the corner of the basement of the

house half a block down the street from Jerry's Bait shop You know the place well anyway, back then life was going swell and everything

was just peachy

Except, of course, for the undeniable fact that every single

morning My mother would make me a big bowl of sauerkraut for

breakfast

A big bowl of sauerkraut Every single morning It was driving me crazy

I said to my mom . . . "Hey, mom, what's with all the

sauerkraut?"
And my dear, sweet mother
She just looked at my like a cow looks at an oncoming train
And she leaned right down next to me
And she said "IT'S GOOD FOR YOU"

That's when I swore that someday Someday I would get outta that basement and travel to a

magical, faraway place Where the sun is always shining and the air smells like

warm root beer And the towels are oh so fluffy Where the Shriners and the lepers play their ukuleles all

day long

Well, let me tell you, people, it wasn't long at all before my

dream came true Because the very next day, a local radio station had this

contest
To see who could correctly guess the number of molecules
in Leonard Nimoy's butt
I was off by three, but I still won the grand prize
That's right, a first-class one-way ticket to . . .

You know, I'd never been on a real airplane before And I gotta tell ya, it was really great Except that the little kid in back of me kept throwin' up the

whole time The flight attendants ran out of Dr. Pepper and salted

peanuts And, oh yeah, three of the airplane engines burned out And we went into a tailspin and crashed into a hillside And the plane exploded in a giant fireball and everybody

died Except for me You know why?

'Cause I had my tray table up
And my seat back in the full upright position
Had my tray table up
And my seat back in the full upright position

So I crawled from the twisted, burnin' wreckage I crawled on my hands and knees for three full days Draggin' along my big leather suitcase and my garment bag And my tenor saxophone and my twelve-pound bowling

ball And my lucky, lucky autographed glow-in-the-dark snorkel But finally I arrived at the world famous Albuquerque

Holiday Inn Where the towels are oh so fluffy

Well, I checked into my room and I turned down the A/C And I'm just about to eat that little chocolate mint on my

pillow That I love so very, very much when suddenly, there's a

knock on the door

Well now, who could that be?

I say "Who is it?"
No answer
"Who is it?"
They're not sayin' anything

So, finally I go over and I open the door and just as I

suspected It's some big fat *guy* with a Flock-Of-Seagulls haircut and

only one nostril So anyway, he bursts into my room and he grabs my lucky

snorkel
And I'm like "Hey, you can't have that"
"That snorkel's been just like a snorkel to me"
And he's like "Tough"
And I'm like "Give it"
And he's like "Make me"
And I'm like "'Kay"
So I grabbed his leg and he grabbed my esophagus
And I bit off his ear and he chewed off my eyebrows
Yes indeed, you better believe it
And somehow in the middle of it all, the phone got knocked

off the hook
And twenty seconds later, I heard a familiar voice
And you know what it said?
I'll tell you what it said

It said . . . "If you'd like to make a call, please hang up and

try again"

"If you need help, hang up and then dial your operator"

Well, to cut a long story short, he got away with my snorkel But I made a solemn vow right then and there that I would

not rest I would not sleep for an instant until the one-nostrilled man

was brought to justice But first, I decided to buy some donuts

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
He says "All I got right now is this box of one dozen
starving, crazed weasels"
I said "OK, I'll take that"

So he hands me the box and I open up the lid and the

weasels jump out And they immediately latch onto my face and start bitin'

me all over (rabid gnawing sounds)

Oh man, they were just going nuts
They were tearin' me apart
Oh, oh God, oh God
Oh, get 'em off me
(more screaming)

I ran out into the street with these flesh-eating weasels all

over my face Wavin' my arms all around and just runnin', runnin', runnin' And as luck would have it, that's exactly when I ran into the

girl of my dreams Her name was Zelda She was a calligraphy enthusiast with a slight overbite and

hair the color of strained peaches I'll never forget the first thing she said to me She said "Hey, you've got weasels on your face"

That's when I knew it was true love
We were inseparable after that
We ate together, we bathed together
We even shared the same piece of mint-flavored dental

floss
The world was our burrito
So we got married and we bought us a house
And had two beautiful children - Nathaniel and Superfly
Oh, we were so very very very happy

But then one fateful night, Zelda said to me She said "Sweetie pumpkin? Do you wanna join the

Columbia Record Club?"
I said "Woah, hold on now, baby"
"I'm just not ready for that kinda commitment"
So we broke up and I never saw her again
But that's just the way things go . . . In Albuquerque

Anyway, things really started lookin' up for me Because about a week later, I finally achieved my lifelong

dream That's right, I got me a part-time job at The Sizzler I even made employee of the month after I put that grease

fire out with my face Aw yeah, everybody was pretty jealous of me after that I was gettin' a lot of attitude

Anyway I, I know it's kinda been a roundabout way of

saying it But I guess the whole point I'm tryin' to make here is . . .

I! HATE! SAUERKRAUT!
That's all I'm really tryin' to say
And, by the way, if one day you happen to wake up
And find yourself in an existential quandary
Full of loathing and self-doubt
And wracked with the pain and isolation of your pitiful

meaningless existence At least you can take a small bit of comfort in knowing that Somewhere out there in this crazy ol' mixed-up universe of

ours There's still a little place called . . . Albuquerque

I said "A" - "L" -"B" - "U" - "querque" Albuquerque
```

---

## IC-1871: Alice’s Restaurant

- Title: Alice’s Restaurant
- Author (byline): Arlo Guthrie
- Work: Not specified
- Publisher: Random House Trade Paperbacks
- Publication date as stated: January 1968
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2433
- Already set (do not supply): none

### Source block (context only)

```text
Author: Arlo Guthrie
ISBN: 978-0394176642
Publisher: Random House Trade Paperbacks
Date(Month/Year): January 1968
```

### Introduction (context only: never use it for content warnings)

```text
The politics of "Alice's Restaurant" criticize America's draft, which truly was a "selective service system" -- from which clever young men could escape with no harm to their future careers. But Arlo Guthrie throws no bombs, gets busted for littering, trusts his fate to "the system" and does fine in court because justice is literally blind. His crime makes him ineligible for the draft that turned young American males into soldiers for the Asian war he opposes. Let me share the story with you from Arlo Guthrie’s point of view . . . Alice’s Restaurant by Arlo Guthrie
```

### Performance text (classify this)

```text
You can get anything you want at Alice's Restaurant You can get anything you want at Alice's Restaurant Walk right in it's around the back Just a half a mile from the railroad track You can get anything you want at Alice's Restaurant

Now it all started two Thanksgivings ago, was on - two years ago on Thanksgiving, when my friend and I went up to visit Alice at the restaurant, but Alice doesn't live in the restaurant, she lives in the church nearby the restaurant, in the bell-tower, with her husband Ray and Fasha the dog. And livin' in the bell tower like that, they got a lot of room downstairs where the pews used to be in. Havin' all that room, seein' as how they took out all the pews, they decided that they didn't have to take out their garbage for a long time.

We got up there, we found all the garbage in there, and we decided it'd be a friendly gesture for us to take the garbage down to the city dump. So we took the half a ton of garbage, put it in the back of a red VW microbus, took shovels and rakes and implements of destruction and headed on toward the city dump.

Well we got there and there was a big sign and a chain across across the dump saying, "Closed on Thanksgiving." And we had never heard of a dump closed on Thanksgiving before, and with tears in our eyes we drove off into the sunset looking for another place to put the garbage.

We didn't find one. Until we came to a side road, and off the side of the side road there was another fifteen foot cliff and at the bottom of the cliff there was another pile of garbage. And we decided that one big pile is better than two little piles, and rather than bring that one up we decided to throw our's down.

That's what we did, and drove back to the church, had a thanksgiving dinner that couldn't be beat, went to sleep and didn't get up until the next morning, when we got a phone call from officer Obie. He said, "Kid, we found your name on an envelope at the bottom of a half a ton of garbage, and just wanted to know if you had any information about it." And I said, "Yes, sir, Officer Obie, I cannot tell a lie, I put that envelope under that garbage."

After speaking to Obie for about fourty-five minutes on the telephone we finally arrived at the truth of the matter and said that we had to go down and pick up the garbage, and also had to go down and speak to him at the police officer's station. So we got in the red VW microbus with the shovels and rakes and implements of destruction and headed on toward the police officer's station.

Now friends, there was only one or two things that Obie coulda done at the police station, and the first was he could have given us a medal for being so brave and honest on the telephone, which wasn't very likely, and we didn't expect it, and the other thing was he could have bawled us out and told us never to be see driving garbage around the vicinity again, which is what we expected, but when we got to the police officer's station there was a third possibility that we hadn't even counted upon, and we was both immediately arrested. Handcuffed. And I said "Obie, I don't think I can pick up the garbage with these handcuffs on." He said, "Shut up, kid. Get in the back of the patrol car."

And that's what we did, sat in the back of the patrol car and drove to the quote Scene of the Crime unquote. I want tell you about the town of Stockbridge, Massachusets, where this happened here, they got three stop signs, two police officers, and one police car, but when we got to the Scene of the Crime there was five police officers and three police cars, being the biggest crime of the last fifty years, and everybody wanted to get in the newspaper story about it. And they was using up all kinds of cop equipment that they had hanging around the police officer's station. They was taking plaster tire tracks, foot prints, dog smelling prints, and they took twenty seven eight-by-ten colour glossy photographs with circles and arrows and a paragraph on the back of each one explaining what each one was to be used as evidence against us. Took pictures of the approach, the getaway, the northwest corner the southwest corner and that's not to mention the aerial photography.

After the ordeal, we went back to the jail. Obie said he was going to put us in the cell. Said, "Kid, I'm going to put you in the cell, I want your wallet and your belt." And I said, "Obie, I can understand you wanting my wallet so I don't have any money to spend in the cell, but what do you want my belt for?" And he said, "Kid, we don't want any hangings." I said, "Obie, did you think I was going to hang myself for littering?" Obie said he was making sure, and friends Obie was, cause he took out the toilet seat so I couldn't hit myself over the head and drown, and he took out the toilet paper so I couldn't bend the bars roll out the - roll the toilet paper out the window, slide down the roll and have an escape. Obie was making sure, and it was about four or five hours later that Alice (remember Alice? It's a song about Alice), Alice came by and with a few nasty words to Obie on the side, bailed us out of jail, and we went back to the church, had a another thanksgiving dinner that couldn't be beat, and didn't get up until the next morning, when we all had to go to court.

We walked in, sat down, Obie came in with the twenty seven eight-by-ten colour glossy pictures with circles and arrows and a paragraph on the back of each one, sat down. Man came in said, "All rise." We all stood up, and Obie stood up with the twenty seven eight-by-ten colour glossy pictures, and the judge walked in sat down with a seeing eye dog, and he sat down, we sat down. Obie looked at the seeing eye dog, and then at the twenty seven eight-by-ten colour glossy pictures with circles and arrows and a paragraph on the back of each one, and looked at the seeing eye dog. And then at twenty seven eight-by-ten colour glossy pictures with circles and arrows and a paragraph on the back of each one and began to cry, 'cause Obie came to the realization that it was a typical case of American blind justice, and there wasn't nothing he could do about it, and the judge wasn't going to look at the twenty seven eight-by-ten colour glossy pictures with the circles and arrows and a paragraph on the back of each one explaining what each one was to be used as evidence against us. And we was fined $50 and had to pick up the garbage in the snow, but thats not what I came to tell you about. Came to talk about the draft.

They got a building down New York City, it's called Whitehall Street, where you walk in, you get injected, inspected, detected, infected, neglected and selected. I went down to get my physical examination one day, and I walked in, I sat down, got good and drunk the night before, so I looked and felt my best when I went in that morning. `Cause I wanted to look like the all-American kid from New York City, man I wanted, I wanted to feel like the all-, I wanted to be the all American kid from New York, and I walked in, sat down, I was hung down, brung down, hung up, and all kinds o' mean nasty ugly things. And I waked in and sat down and they gave me a piece of paper, said, "Kid, see the phsychiatrist, room 604."

And I went up there, I said, "Shrink, I want to kill. I mean, I wanna, I wanna kill. Kill. I wanna, I wanna see, I wanna see blood and gore and guts and veins in my teeth. Eat dead burnt bodies. I mean kill, Kill, KILL, KILL." And I started jumpin up and down yelling, "KILL, KILL," and he started jumpin up and down with me and we was both jumping up and down yelling, "KILL, KILL." And the sargent came over, pinned a medal on me, sent me down the hall, said, "You're our boy."

Didn't feel too good about it.

Proceeded on down the hall gettin more injections, inspections, detections, neglections and all kinds of stuff that they was doin' to me at the thing there, and I was there for two hours, three hours, four hours, I was there for a long time going through all kinds of mean nasty ugly things and I was just having a tough time there, and they was inspecting, injecting every single part of me, and they was leaving no part untouched. Proceeded through, and when I finally came to the see the last man, I walked in, walked in sat down after a whole big thing there, and I walked up and said, "What do you want?" He said, "Kid, we only got one question. Have you ever been arrested?"

And I proceeded to tell him the story of the Alice's Restaurant Massacre, with full orchestration and five part harmony and stuff like that and all the phenome... - and he stopped me right there and said, "Kid, did you ever go to court?"

And I proceeded to tell him the story of the twenty seven eight-by-ten colour glossy pictures with the circles and arrows and the paragraph on the back of each one, and he stopped me right there and said, "Kid, I want you to go and sit down on that bench that says Group W .... NOW kid!!"

And I, I walked over to the, to the bench there, and there is, Group W's where they put you if you may not be moral enough to join the army after committing your special crime, and there was all kinds of mean nasty ugly looking people on the bench there. Mother rapers. Father stabbers. Father rapers! Father rapers sitting right there on the bench next to me! And they was mean and nasty and ugly and horrible crime-type guys sitting on the bench next to me. And the meanest, ugliest, nastiest one, the meanest father raper of them all, was coming over to me and he was mean 'n' ugly 'n' nasty 'n' horrible and all kind of things and he sat down next to me and said, "Kid, whad'ya get?" I said, "I didn't get nothing, I had to pay $50 and pick up the garbage." He said, "What were you arrested for, kid?" And I said, "Littering." And they all moved away from me on the bench there, and the hairy eyeball and all kinds of mean nasty things, till I said, "And creating a nuisance." And they all came back, shook my hand, and we had a great time on the bench, talkin about crime, mother stabbing, father raping, all kinds of groovy things that we was talking about on the bench. And everything was fine, we was smoking cigarettes and all kinds of things, until the Sargeant came over, had some paper in his hand, held it up and said.

"Kids, this-piece-of-paper's-got-47-words-37- sentences-58-words-we-wanna-know-details-of-the-crime-time-of-the-crime-and-any-other-kind-of-thing-you-gotta-say-pertaining-to-and-about-the-crime-I-want-to-know-arresting-officer's-name-and-any-other-kind-of-thing-you-gotta-say", and talked for forty-five minutes and nobody understood a word that he said, but we had fun filling out the forms and playing with the pencils on the bench there, and I filled out the massacre with the four part harmony, and wrote it down there, just like it was, and everything was fine and I put down the pencil, and I turned over the piece of paper, and there, there on the other side, in the middle of the other side, away from everything else on the other side, in parentheses, capital letters, quotated, read the following words: ("KID, HAVE YOU REHABILITATED YOURSELF?")

I went over to the sargent, said, "Sargeant, you got a lot a damn gall to ask me if I've rehabilitated myself, I mean, I mean, I mean that just, I'm sittin' here on the bench, I mean I'm sittin here on the Group W bench 'cause you want to know if I'm moral enough join the army, burn women, kids, houses and villages after bein' a litterbug." He looked at me and said, "Kid, we don't like your kind, and we're gonna send you fingerprints off to Washington."

And friends, somewhere in Washington enshrined in some little folder, is a study in black and white of my fingerprints. And the only reason I'm singing you this song now is cause you may know somebody in a similar situation, or you may be in a similar situation, and if your in a situation like that there's only one thing you can do and that's walk into the shrink wherever you are ,just walk in say "Shrink, You can get anything you want, at Alice's restaurant.". And walk out. You know, if one person, just one person does it they may think he's really sick and they won't take him. And if two people, two people do it, in harmony, they may think they're both faggots and they won't take either of them. And three people do it, three, can you imagine, three people walking in singin a bar of Alice's Restaurant and walking out. They may think it's an organization. And can you, can you imagine fifty people a day,I said fifty people a day walking in singin a bar of Alice's Restaurant and walking out. And friends they may thinks it's a movement.

And that's what it is, the Alice's Restaurant Anti- Massacre Movement
```

---

## IC-1872: All in the Timing

- Title: All in the Timing
- Author (byline): Jason Sheets
- Work: Turning Points
- Publisher: Tichenor Publishing
- Publication date as stated: 2001
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 839
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jason Sheets
Book: Turning Points
Publisher: Tichenor Publishing
ISBN: 978-0742117013
Date: 2001
```

### Introduction (context only: never use it for content warnings)

```text
An average day in the typical American father’s life is unmemorable. We average man lives his life on autopilot. We put off until tomorrow what should be done today. We forget promises we’ve made. We cut corners. We procrastinate. We go through the motions, ignoring the clock that is ticking our lives away. Maybe one day, one man will be fortunate enough to realize that it’s “All in the Timing” by Jason Sheets
```

### Performance text (classify this)

```text
6:55 AM Snooze alarm

7 :00 AM Wake up
7:02 AM Shave
7:05 AM Shower
7:15 AM Comb hair
7:16 AM Dress
7:30 AM Breakfast
7 :40 AM Brush teeth
7:50 AM Leave for work
7:59 AM Arrive at work
There.
Got it.
Wait-
What if I have to go to the bathroom? Damn!
6:50 AM Snooze alarm
6:55 AM Wake up ...
Tick, tick, tick
Tick, tick, tick, tick ...
What?? Pick up what? No.
No.
I don't have the time. Yeah, love you, too. Later.
No.
Later.
9:00 Check e-mail
9:06 Open e-mail
9: 15 Check voice- mail
9:18 Check faxes
9:20 Answer beeper
9:25 Return calls
9:35 Check e-mail again
9:38 Check faxes again
9:45 Start workday
Now let me get this straight. I sign on with your
company, I spend the next 45 years of my life
making money for you,
working on your schedule,
your pay rates, your promotion standards,
with your hand-picked people who are supposed to
become my respected colleagues.
Every 50 weeks
you'll grant me 2
weeks off where I can
go to Tahiti and spend the little money I've saved
on coconut flavored milkshakes for the
whole family.
And, after my 45
years, you'll throw
a party for me that
lasts 2 hours and
that half the people
will make up reasons
not to go and half

of the half

that do show up
will get my name wrong. Then, you'll give me an
engraved watch
that isn't even a Timex. Is that right?
fine.
Sign me up.
This is a much better deal than I expected.
11:30 Remember that you forgot lunch at home
11:31 Use profanity
11:35 Agree to go to lunch with boring, useless,
drips of society
12:00 During lunch, mentally use profanity.
No, I haven't read the new Grisham novel. No, I
didn't see the game last night.
No, I haven't seen Calvin Klein's new fall fashions.
No, I haven't volunteered to teach Church Bible
School. But, I do know that gas is selling at the
Marathon station for just a dollar-five.
See -
I haven't missed out on everything.
You're doing what?
Save that for home.
You're on the clock.
Tick, tick, tick,
Tick, tick, tick, tick.
Not today.
I haven't got the time
When I'm a parent,
I'm going to do everything differently.
I'm going to play catch with my son every evening
that it's not raining.
I'm going to sit my daughter on my knee
and let her bounce up and down. I'm going to bring
my wife roses every Friday.
I'm going to fix up the house. Learn to cook.
Fix my wife breakfast in bed. Build my kids a tree-
house. Do my own oil changes.
Help my son get more Cub Scout badges than
anyone else.
Get in shape.
Get a life.
Get a hobby.
When will I find the time to do all this?
I'm not worried.
I'll make time.
Tick, tick, tick
5:00 Return home
5:01 See list of jobs that you posted on the
refrigerator
5:03 Get beer
5:05 Start jobs
No, mom.
Can't make it home this year. You know how it is.
Next year.
I promise.
Right now I just don't have the time.
Can't you see? Daddy's busy.
Go play with one of the kids over there.
One of them must like you. Go play.
Can't you see? Daddy's busy.
Daddy's tired.
He works very hard. This is his vacation. Go play.
Go see mommy.
Yes, we'll go see the ponies. Tomorrow.
Not right now.
Can't you see
Daddy's busy.
Tick, tick, tick, tick, tick Dear dad,
I'm sorry I never made it back
in time to see you.

Mom didn't tell me that it was serious this time.
If I had known that this would
be it,
I would have made the time. I would have found the
time. I would have, dad.
I would have.
Quiet!
The game's on! Go ask your mom.
Honey - the kids want to practice for some spelling
bee or something.
Can you help them out? The game's on!
Tick, tick, tick,
Tick, tick, tick, tick.
So when are you two going to have kids? She's 33.

Don't forget about that biological clock.

Tick, tick, tick, Tick, tick, tick, tick.

They're done. Eight down with a minute to play. Comeback?

Nah
They haven't got the time.
10:28 Collapse in bed
10:30 Wearily watch "Nightline"
10:32 Fall asleep
2:00 am. Realize you forgot to tell your wife you lo-
2:02 Mental note to tell her in the morning
So where did all the time go?
It flits away and you don't even know when it
happens.
Time rapes you.
From your family.
From your friends.
From your own existence. We let it happen.
We know it's happening. We'd realize it's happening
... if
we'd taken the time.
```

---

## IC-1873: And to Think That I Saw It On Mulberry Street

- Title: And to Think That I Saw It On Mulberry Street
- Author (byline): Theo Geisel (aka Dr. Seuss)
- Work: Not specified
- Publisher: Creative Co (Sd)
- Publication date as stated: Aug 1995
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 523
- Already set (do not supply): none

### Source block (context only)

```text
Author: Gabriel Garcia Marquez
ISBN: 978-0394844947
Publisher: Creative Co (Sd)
Date (Month/Year): Aug 1995
```

### Introduction (context only: never use it for content warnings)

```text
One day Marco sees a horse pulling a man on a broken-down wagon on Mulberry Street. But he soon imagines something much grander. If you change a horse for a zebra, that's better. Or you could change that zebra for a large reindeer. Or better yet, how about an elephant with a Rajah wearing rubies on a throne on top? And on it goes.

Pulitzer-prize winning Dr. Seuss needs no introduction. His ode to the imagination of a child is as fresh and exquisitely outlandish today as it was when first published in 1937. This is a classic that will never fade with age. And to Think That I Saw it On Mulberry Street by Theo Geisel.
```

### Performance text (classify this)

```text
When I leave home to walk to school,
Dad always says to me,
“Marco, keep your eyelids up
And see what you can see.”
But when I tell him where I’ve been
And what I think I’ve seen,
He looks at me and sternly says,
“Your eyesight’s much too keen.
Stop telling such outlandish tales,
Stop turning minnows into whales.”
• • • • • • •
Now, what can I say
When I get home today?
All the long way to school
And all the way back,
I’ve looked and I’ve looked
And I’ve kept careful track,
But all that I’ve noticed,
Except my own feet,
Was a horse and a wagon
On Mulberry Street.
That’s nothing to tell of,
That won’t do of course …
Just a broken-down wagon
That’s drawn by a horse.
That can’t be my story. That’s only a start.
I’ll say that a ZEBRA was pulling the cart!

And that is a story that no one can beat,
When I say that I saw it on Mulberry Street.
-Yes, the zebra is fine, but I think it’s a shame,
Such a marvelous beast with a cart that’s so tame,
The story would really be better to hear
If the driver I saw were a charioteer.
A gold and blue chariot’s something to meet,
Rumbling like thunder down Mulberry Street!
No, it won’t do at all … Azebra’s too small,
A reindeer is better; he’s fast and he’s fleet,
And he’d look mighty smart on old Mulberry Street.
Hold on a minute! There’s something wrong!
A reindeer hates the way it feels
To pull a thing that runs on wheels,
He’d be much happier, instead, if he could pull a fancy
sled.

Hmmmmm … A reindeer and sleigh …
… Say … anyone could think of that, Jack or Fred, or
Joe or Nator … say, even Jane could think of that.
But it isn’t too late to make one little change,
A sleigh and an elephant! There’s something strange!
—I’ll pick one with plenty of power and size,
A blue one with plenty of fun in his eyes.
And then, just to give him a little more tone,
Have a Rajah, with rubies, perched high on a throne.
Say! That makes a story that no one can beat,
When I say that I saw it on Mulberry Street.
But it still could be better. Suppose that I add …
(look at watch)
… Notime for more,
I’m almost home
• • • • • • •
I swung around the corner
And dashed through the gate,
I ran up the steps
And I felt simply GREAT!
FOR I HAD A STORY THAT NO ONE COULD BEAT!
AND TO THINK THAT I SAW IT ON MULBERRY
STREET!
But Dad said quite calmly,
“Just draw up your stool
And tell me the sights
On the way home from school.”
THERE WAS SO MUCH TO TELL, I JUST COULDN’T
BEGIN!
Dad looked at me sharply and pulled at his chin,
He frowned at me sternly from there in his seat,
“Was there nothing to look at …Nopeople to greet?
Did nothing excite you or make your heart beat?”
“Nothing,” I said, growing red as a beet,
“But a plain horse and wagon on Mulberry Street.”
```

---

## IC-1874: The Antihero

- Title: The Antihero
- Author (byline): Ai
- Work: Vice: New and Selected Poems
- Publisher: W.W. Norton and Company
- Publication date as stated: June 2000
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 837
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ai
Book: Vice: New and Selected Poems
ISBN: 978-0393320183
Publisher: W.W. Norton and Company
Date (Month/Year): June 2000
and when I raise my revolver to my head and fire,
a wave of desire washes over me
and I understand that what I always wanted
was release from my own pain,
but there’s only the terrible surrender to it,
```

### Introduction (context only: never use it for content warnings)

```text
When we hear the word 'hero,' certain images come to mind: Superman swooping in to save Lois Lane; Harry Potter sacrificing himself to rescue his friends; Simba from The Lion King and William Wallace from Braveheart. But what if Superman had acne and had a hard time getting the girl or Harry Potter suffered from OCD? What if Simba was too afraid to take on the villain Scar and instead was filled with self-doubt? Enter the anti-hero -- a notable figure who is conspicuously lacking in heroic qualities. In other words, he is flawed. It is this flaw or weakness that leads to his downfall, destruction, and usually death.

Meet our Antihero . . . On April 19, 1995, he ran back and forth into the concrete mess of bricks and mortar that was once the Murrah Building in Oklahoma City. He scraped and crawled and dug until his fingers bled and then kept digging some more. But just over a year later, 30-year-old Terry Yeakey was gone – a victim of what was officially deemed as “Suicide” only four days before he was to receive a medal of honor for rescuing people after the Oklahoma City bombing.

The Antihero by Ai
```

### Performance text (classify this)

```text
I park my old maroon Ford in the field outside El Reno,
where wildflowers used to grow, when I was a kid,
but now only thorny memories push their heads
through the dirt like misplaced cacti.
At first, I just sit in the dark,
my heart racing,
then I take my Swiss Army Knife
and slit my wrists.
As blood runs down my hands, I feel exhilarated,
until I remember who I am --
a man with rat’s eyes,
pink rimmed and sensitive to light.
When I was born,
the doctor pronounced me “albino.”
I’m told my mother said,
“They run in the family,
but he’s all right, he’s my baby.”
Six months later, I was adopted by another,
who loved me even though I wasn’t an albino after all.
Much like a Siamese, who are born white,
parts of my body began to darken
until I looked like any other boy.
When I was nine, Widow Dobbs, who lived next door,
brought home a Siamese.
She named him Buster Kitty.
He was a big, round-headed cat,
who hunted birds and tormented dogs,
when he wasn’t sitting outside my window,
looking in at me,
as if I were a long-lost relative.
We respected each other,
but avoided too much contact.
When I went outside to play, he’d stroll away,
his tail lifted in the air, as if to say, “Take that.”
One afternoon, he got run over by a moving van.
Widow Dobbs wasn’t home and neither was my mother,
so I carried him to our backyard
and buried him in a hole I dug with a garden trowel.
I didn’t tell anyone I’d done it.
After a week, the widow put up signs
offering a reward.
A few months later,
A stray dog dug up Buster’s skeleton.
“I suppose you know nothing about it,” said Mother.
“A truck hit him, he was dead, so I buried him,” I

confessed,
but Mother only said “I found your water pistol.”
Now Buster sits on my shoulder,
whispering that I’ll get what I deserve.
I tell him I always do.
I used to see him two, or three times a day,
when I was a military policeman,
during the Persian Gulf War.
That’s when I helped bury civilians in mass graves.
The corpses gave off the smell of chemicals and oil
and when I washed my hands,
a black film came off on my Handi Wipes.
There, as the smoke from the burning oil wells
blackened the light of each day.,
I picked up the carcasses of birds
overcome by fumes,
having dropped from the air
after dying in midflight.

I buried them too,
as Buster scolded me about how I placed the bodies.
“No,” he’d say, “don’t drop them in like stones
down the well of death,”
And I didn’t. I laid them down gently
like a mother, who has found her lost children.
After a while, he simply faded
into the scenery of that endless night
and when I went home to Oklahoma City,
he kept his distance.
It was enough to convince me that I was free of him,
until the day the Murrah building was bombed.
I was a policeman then too,
because I’d persuaded myself
it was the best way to help people.
That morning, I pulled three men and two women
from the rubble,
before I fell through a hole two floors
and lay helpless in the debris.
As body fluids dripped on me, Buster appeared,
but he didn’t say anything,
only hovered in the air, until I passed out.
After I came home from the hospital,
my back hurt constantly
and I had nightmares about dead children.
I was afraid of what I might do,
without knowing what it was.
Waves of nausea often sent me to the bathroom,
Where I kneeled in front of the toilet,
until a vile liquid bubbled up
from the pit of my stomach.
It tasted like green chilies
and burned the back of my throat.
I pissed blood and cursed Buster,
who truly knew me for what I was,
because I was to blame for his death
and hid my shame by covering it with dirt.
The day he died, I shot him with my water pistol.
That’s when he darted in the path
of a Bekins truck.
That night, I made a promise to myself
that I would be of help to anyone who needed it.

Now as I listen to the drip, drip of my blood, hitting the rubber floor mat and my shoes, I realize I can’t rescue the dead, or erase the zero of my life and make it count, when all it amounts to is a few pints of blood turning to red mud, as I stagger from the car to a gully nearby. I kneel down and lay my Bible and copy of In Their Names on the ground, As Buster reappears to tell me it’s all right, I won’t feel a thing, but we both know he’s lying
```

---

## IC-1875: Becoming – A Collection

- Title: Becoming – A Collection
- Author (byline): Jonathan Green, Roger Bonair-
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1028
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jonathan Green
Website: https://medium.com/isolation/becoming-and-
unbecoming-c6dae66b3940
ISBN: N/A
Publisher: Medium.com
Date (Month/Year): Published on-line Dec 15, 2020
Author: Roger Bonair-Agard
Book: The Spoken Word Revolution (Pg 196-197)
ISBN: 978-0321328953
Publisher: Longman
Date (Month/Year): 2003
Author: John Roedel
Book: 2023 Poetry Wall Calendar
ISBN: N/A
Publisher: John Roedel
Date (Month/Year): 2022
Can be Purchased at https://johnroedel.square.site
```

### Introduction (context only: never use it for content warnings)

```text
So many of us go through life with our stories hidden, feeling ashamed that we haven’t lived up to some self- or society- imposed ideal . . . But becoming doesn’t have an end game. Becoming is a life-long process.

The Skin Horse explains in the Velveteen Rabbit by Margery Williams: “You become. It takes a long time. That’s why it doesn’t happen often to people who break easily, or have sharp edges, or who have to be carefully kept. . . You become.”

Becoming – A Collection containing Becoming and Unbecoming by Jonathan Green, Naming and Other Christian Things by Roger Bonair-Agard and Hey God. Hey John by John Roedel.
```

### Performance text (classify this)

```text
Agard and John Roedel

Becoming and Unbecoming by Jonathan Green
Each day I want to be the best version of myself
and then I fail, and fall flat on my face,
chipping two teeth and busting my lip and nose
only to realize that I can try again tomorrow

I am constantly becoming and unbecoming my best self and it gets pretty tiring trying to figure out which is which so I drink some tea and look deep into the mirror so I can decide which version of myself I am today

And the second I realize who is staring back at me I start to become a new version of that person a constant realization that I am both enough and not

enough all at the same time, with this same face, this same brain How can I become someone while unbecoming someone

else when I don’t even know which one was objectively better or more so, which one I even liked being from inside of

these eyes looking at a moving target of myself and who I want to be?

Naming and Other Christian Things by Roger Bonair-Agard

(Pg 196-197) At 31 I finally learn that Lena is short for Magdalene

one of those enigmas of biblical lore whore found religion I have often questioned her motives -- this love of Jesus

Christ this holy supplication to the Son of Man And I think about Lena my grandmother

great big woman, skin of ashy obsidian hair whitened with the burden of conviction and I wonder about this business of weeping and

foot washing;

but I can only remember her iron hand and

rigid schedules her admonition on catching me daydreaming on

the outhouse roof
• Get down off that thing boy
• You have your book to study
• What kind of man do you expect to become?!
I recall her jacking up of my equally stern

grandfather reminding him of the folly of any repeated attempts to hit her

Never does Mary Magdalene come to mind

not in the helpless “weeping for the crucified” way

not in the convenient Catholic depictions of feminine frailty of morals and spirit

I know of a Magdalene with fight more Joan of Arc than Maid Marion more Sojourner Truth than damsel in distress

and I want to tell the withering two-

dimensional ghost couched and crumpled at the foot of the cross

• Get up and fight woman!

• Wake up and live if you love him!

• Jack up the Pontius Pilate and refuse

surrender At 4 I was beaten for disrespect of my

grandfather at 8 because I was satisfied with only a 75 in

Math -- because she knew having fought battles based

purely on conviction that she was preparing a man for the holiest of

crucifixions

there would be no washing of feet here

no flimsy eruption of tears only the austerity of a warrior and a Puritan insistence on perfection and effort

the creases through her aged jowls softening only when she thought I need to eat to get

strong

• Son yuh lookin thin; come and get

some food

a name orients one to his universe the Lakotas

believed so a change in a name meant a chance for

improvement for the child who was not doing well

so having learned the root of my

grandmother's name I cannot summon the sympathy for Mary Magdalene

cannot help her weep tears of distress only wish I could retroactivate a name change for her show her my grandmother carrying 30lb sacks of coffee

dragging her swollen leg behind her rising from her deathbed to fight her daughter's battles

One day if I am worthy of her expectations
I will become a man worth crucifying
and all her beatings
her lessons
her Puritanism and super-human strength
will have taught me
that surrender is not an option

On that day I expect to see
standing at the foot of whatever urban cross they fashion
all five-foot-ten of Lena
pointing one huge gnarled finger at me

the shining authority of her eyes
coming from the black forest of her flesh
the white electricity of her hair
lips trembling in rage

• Get down off that thing boy and fight!

• What kind of man do you intend to become?!

Hey God, Hey John by John Roedel

Me: Hey God.

God: Hello . . .

Me: I'm falling apart. Can you put me back together?

God: I would rather not.

Me: Why?

God: Because you aren't a puzzle.

Me: What about all of the pieces of my life that are falling down onto the ground?

God: Let them stay there for a while. They fell off for a reason. Take some time and decide if you need any of those pieces back.

Me: You don't understand! I'm breaking down!

God: No - you don't understand. You are breaking through. What you are feeling are just growing pains. You are shedding the things and the people in your life that are holding you back. You aren't falling apart. You are falling into place. Relax. Take some deep breaths and allow those things you don't need anymore to fall off of you. Quit holding onto the pieces that don't fit you anymore. Let them fall off. Let them go.

Me: Once I start doing that, what will be left of me?

God: Only the very best pieces of you.

Me: I'm scared of changing.

God: I keep telling you - YOU AREN'T CHANGING!! YOU ARE BECOMING!

Me: Becoming who?

God: Becoming who I created you to be! A person of light and love and charity and hope and courage and joy and mercy and grace and compassion. I made you for more than the shallow pieces you have decided to adorn yourself with that you cling to with such greed and fear. Let those things fall off of you. I love you! Don't change! ... Become! Become! Become who I made you to be. I'm going to keep telling you this until you remember it.

Me: There goes another piece.

God: Yep. Let it be.

Me: So . . . I'm not broken?

God: Of course Not! - but you are breaking like the dawn. It's a new day. Become!!!
```

---

## IC-1876: Being Latino – A Program

- Title: Being Latino – A Program
- Author (byline): Carlos Andres Gomez and Jonathan Mendoza
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1055
- Already set (do not supply): none

### Source block (context only)

```text
Author: Carlos Andres Gomez
Book: Fight Evil with Poetry – Anthology Volume 1,
Pg 81-82
ISBN: 978-0997129762
Publisher: Sideshow Media Group
Date (Month/Year): October 2018
Author: Jonathan Mendoza
Book: On-Line Transcript
https://www.splitthisrock.org/poetry-
database/poem/onomastico
Publisher: Split This Rock.org
Date (Month/Year): October 1, 2019
Author: Carlos Andres Gomez
Magazine: Rattle
ISSN# 1097-2900 (print)
2153-8115 (online)
Website: https://www.rattle.com/whats-genocide-by-
carlos-andres-gomez/
Publisher: Rattle.com – Issue #27; Summer 2007
Print Issue can be purchased at
https://www.rattle.com/product/i27/
On-line Publishing Date (Month/Year): April 7, 2009
Also Found in
Book: Man Up: Reimagining Modern Manhood, Chpt 8
ISBN: 978-1592408078
Publisher: Gotham
Date (Month/Year): Nov 2013
```

### Introduction (context only: never use it for content warnings)

```text
What does it mean to be Latino? To be Hispanic? What does it mean to be American? Identity, or how we understand and express ourselves, is very complex. The US Latino community is incredibly diverse, and many of us have layered identities.

As activist Jonathan Jayes Green has said “I am not willing to compartmentalize my identities. I am all that I am all the time.” * Latino/Hispanic identities are unique and shaped by factors such as geography – over 20 countries -- heritage, race, and more. This program explores the struggle to be both Latino and American.

Where are You Really From? by Carlos Andres Gomez and Onomastico by Jonathan Mendoza and What’s Genocide? by Carlos Andres Gomez
```

### Performance text (classify this)

```text
CHANGE OF CHARACTER VOICE AND STANCE RECOMMENDED FOR EACH POEM

Where are You Really From? by Carlos Andres Gomez

(Pg 81-82) The man’s words to me are not offered but flung:

“So, what are you? I mean, where are you from?”

I say, “New York.”

“But your name is Carlos -- where are you really from?”

I say, “New York.”

“Bueno, yo soy Latino - mi padre es Colombiano,

mi madre es Estadounidense, nací in New York

City, [“Well, I'm Latino. My father is Colombian.

My mother is American. I was born in New York

City.”] I lived in 4 countries, moved 12 times, and

went to 12 schools before I graduated high school

– is not what I would ever say in 12,341 years

because I don’t owe a damn thing to anyone.

What am I?

What am I? Dude discovers his first Latino with green eyes and suddenly appoints himself the authority on Latinidad.

“But you totally don’t look Mexican . . .

Oh, Colombian. But like what percentage are you . . .?

“Do you speak it, though? Fluently?

Dance salsa? Well? Oh, but not both parents.”

I know: everyone you hang out with looks like you. Has a name you are able to pronounce and/or sounds pulled directly from an episode of Leave it to Beaver.

Here’s the deal: Latin America is not just Mexico (actually pronounced Méjico, pero whatever). Central America is not part of South America. And Mexican is still not a language.

The question, “Where are you from?” -- in our current America -- is a slur disguised with a question mark, a passive-aggressive microaggression saying:

“You are ‘other’.” Saying: “You are not, nor will ever be, one of us.” Saying: “Go back to where you came from!”

But I am from a place beyond place. A place beyond your linear and limited concept of time.

I am from bloodlines unkillable as water.

I am a boy without a word of English in his mouth
in a Catholic school classroom in south Florida, his son
on a stage on the Lower East Side tonight
reading this poem for him.

I am what hard-earned joy looks like carved from the wreckage of a lifetime’s worth of grief.

You are not ready for the answers to the questions you ask, not ready for the worlds these words might shake free. You could never understand what I am, or where I am from.

Onomastico* by Jonathan Mendoza

You ask me for my name, and I say, “It’s pronounced Mendoza,”

I’m sorry. I did not mean to confuse you.

I, too, would like to proudly bestow a heritage,
except I do not know what home
I’d tell my children to go to.
I speak English, and my Abuelo’s cane shakes.
I speak Spanish, and an Aztec priest
cradles smallpox with his lungs,
I say “Nahuatl,” and a Wixarika mother
asks for her daughter back. When I say “home,”
to whose mother am I referring?

Which war am I praying to flee?

Ask me of my name, and I will tell you
of the first men who brought it here,
how they’d unleash dogs onto the children
and clothe entire villages in flames.
Ask me of my name, I’ll tell you I only have it
because a Spaniard stamped it
into a Caxcane woman with his teeth.

I’m sorry, I did not mean to bring
my blood into the room.
I, too, would like to state my presence
and not hawk up a genocide.

I would have known my indigenous parts first, but I searched for my kin in a schoolbook, and learned only of them as the European’s casualty, in that I asked for a history and was handed a cup of blood. I’m sorry,

I reached back across the border
to find anything that has not already been buried,
but most times, I find America imperialized
an already colonized nation.
Most times, I find colony
stacked atop another colony, repeatedly,
a layered cake of mass graves,

I mean the Spanish
literally built the Mexican capitol
over the Aztec city and broadened it
to swallow the entire lake;
each year the city sinks whole feet
into a cavity of its own making.

Ask me of my name, and I’ll say
I do not know how to honor my existence
and the holocaust that caused it
in the same mouth.
Ask me of my name,
“It’s pronounced Mendoza,”
but a Wixarika elder
sings and cries
You’ve survived.
Now dig deeper.
Find me.”

*Translation: The feast of the saint you are named after What’s Genocide? by Carlos Andres Gomez

I asked my students,
“Raise your hand if you’ve heard of the Holocaust.”
in unison, their arms rose up like poisonous gas
then straightened out like an SS infantry
Now raise your hand if you’ve heard of the Rwandan
genocide.”
blank stares mixed with curious ignorance
a quivering hand out of the crowd
half-way raised, like a lone survivor
struggling to stand up in Kigali
“Luz, are you sure about that?”
“No.”
“That’s what I thought.”

“Carlos, what’s genocide?”

your books leave out Emmett Till and Medgar Evers call themselves “World History” and don’t mention King Leopold or diamond mines call themselves “Politics in the Modern World” and don’t mention Apartheid “Carlos, what’s genocide?”

my students thought Che Guevara was a rapper
from East Harlem
still think my Mumia t-shirt is of Bob Marley
how can literacy not include Phillis Wheatley?

“Carlos, what’s genocide?”

“Roselyn, how old was she? Cuántos años tuvo tu madre cuando se murió?” [How old was your mother when she died?]

“My mother had 32 years when she died. Ella era bellísima.” [She was so beautiful]

. . . what’s genocide?

they’ve moved from sterilizing “Boriqua” women
injecting indigenous sisters with Hepatitis B,
now they just kill mothers with silent poison
stain their loyalty and love into veins and suffocate them

. . . what’s genocide?

Ridwan’s father hung himself in the box because he thought his son was ashamed of him

. . . what’s genocide?

Maureen’s mother gave her skin lightening cream the day before she started the 6th grade

. . . what’s genocide?

she carves straight lines into her beautiful brown thighs so she can remember what it feels like to heal

. . . what’s genocide? . . . what’s genocide?

“Carlos, what’s genocide?”

“Luz, this. . . this right here. . . is genocide.”

* Source for the quote in the introduction https://latino.si.edu/exhibitions/presente/latino-identity
```

---

## IC-1877: Blood and Brains

- Title: Blood and Brains
- Author (byline): Roger Guenveur Smith
- Work: Extreme Exposure
- Publisher: Theatre Communications Group
- Publication date as stated: March 2000
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1762
- Already set (do not supply): none

### Source block (context only)

```text
Author: Roger Guenveur Smith
Book: Extreme Exposure
ISBN: 978-1559361552
Publisher: Theatre Communications Group
Date(Month/Year): March 2000
```

### Introduction (context only: never use it for content warnings)

```text
Slavery has been a part of nearly every civilization and has existed in one form or another since the beginning of time, yet today many people seem to believe slavery is just an ugly part of the past. Not so. Slavery persists today in a less obvious, more pervasive way. Inflation, energy costs, housing and health care are putting a strain on everyone in the lower echelons of America’s class structure – the vast majority of these citizens are African American.. As life in the 21st century progresses, a harsh reality has become obvious for anyone willing to see. We remain slaves - Slaves manipulated by the capitalist, consumer economy, which uses poverty as a tool of suppression and punishment. The American dream of freedom and prosperity has been replaced by service and consumerism. The country wants nothing less than our Blood and Brains by Roger Guenveur Smith.
```

### Performance text (classify this)

```text
I am a fugitive slave
I live underneath the Hollywood Freeway
Or the Brooklyn Bridge
Somewhere
Under the Rainbow
My coalition kept warm
by blazing barrels of trash
scraps from the cane fields
and the fast food establishments
I'm on the run
Up and down a basketball court
and into the bush
You can't touch me
I am a maroon
Chilling high above
the smog line
and the tourist enclaves
The North Star
visible every night
My guide into a Philly groove
The Delfonics
Soundtracks to my most intimate moments
Ain't no stopping me now
I'm on the move
Up the Chesapeake
and into the Mississippi
inventing jazz and blood plasma along the way
I'm wearing a hat
a brim
a new attitude
and I'm ready for a new century
so bring it on
serve it up with mush
crumbs
from the table of discontents
I'm going to the Great House Farm
O Yea
and I can't decide if I want dreads
or an Afro
or a skinhead
or a conk
so I'm shopping for wigs
Do you have the Henry Box Brown look?
He was shipped North in a box
and wound up with a flat top
Henry Box Brown
I'm on the run
In a white Bronco disguised as an ex-football player
Through the streets of Virginia Beach
and into a boxing ring
battering my brother to death
grinning at the press conference
proclaiming victory
and misquoting some dead leader
I'm a movie star
gun at the ready
plastered on plantation walls
next to the malt liquor ads
Drunk
on my own infected blood
Strong
stronger than the jackass and the circus elephant that
get more respect than I do
No I'm not registered to vote
but still I'm running for office
For the Canadian border
For some hovel in South London
where I can make a living
a better living than I'm making now
cutting cane
with this rusty machete:
My master is my father
My father my master
Note my resemblance to this wooden nickel
Isn't my grimace the same as his?
I whipped my overseer
Didn't you see it on Cops?
I whipped Rosa Parks
She forgave me
I know how to do
the Black Panther Stomp
and the Charleston
and don't forget the Texas Hop
Disguised myself as a tap dancer
Entertained on the White House lawn
All the while tapping the phone
and getting out the message
to the barbershops
and the Lodges
The Howard University School of Law
Never go outside
without wearing my root
tucked into my right Nike boot
I'm a fugitive slave
running in Hitler's Olympics
gold chains and medals dangling
on the cover of a box of Wheaties
constructing ships for my imminent departure moored in
the Harlem River
or Lake Michigan
When it's frozen over
My kind of town
Quiet
No slave catchers in sight
Just a soft neon glow
from the taquerias
Someone wants to sell me a green card
I'm in the Grand Canyon
listening to Bob Marley tapes
Smoking the peace pipe
with Osceola and the Wild Tchoupitoulas
Jumping up at Mardi Gras
and carnival
and on the first and fifteenth of every month
I'm sitting on the dock of the bay
watching the luxury liners go by
and it's New Year's Eve
and they're playing the blues
and Public Enemy
and I'm trying desperately not to believe the hype
All I need is my Thorazine
I'm not a violent person
Just terribly misguided
I went into space and blew up
I went into hiding up your family tree:
Don't look now
I'm an American slave
and I've got my own sitcom
Millions of laughs per century
with no commercial interruption
I wear three-piece suits
and penny loafers
I've read the classics
I've been to Yale
and I've been to jail
Trumped up charges
They gagged me
Then they made me a news anchor
on the Titanic
Reporting live from a disaster in progress S
wam to shore with Cuban refugees only to be shipped to
Panama
where we swam the Canal
after we dug it
The Rio Grande
The Nile with Langston Hughes
Caught the mock slave auction
in Williamsburg
Took a couple of licks
just for old times' sake
Gave a couple
to show my versatility
Personally escorted Nelson Mandela throughout the
fifty states
Showed him where the Civil War started and never
ended
The Underground Railroad
upgraded for the 1990s
Let's just say it runs from here to there and it's not a
straight path
I'm moving
to the beat
of bare feet
Shackled and perfumed
Pedicured
for the front row patrons
who love public executions
Yeah I ran with Fred
Knew him from the projects
Even back in the day
He had his own talk show
Guests like Nat Turner
and Denmark Vesey
Theme song went:
Learning will spoil the best nigger in the world
So let's get spoiled y'all
That's how I learned my ABC
Wrote my first book
Gave my first lecture
Recorded my first platinum CD
Conferred with Dr. King
at the Lorraine Motel
Told him to duck
Now I'm at large
My portrait on the post office wall
and the cover of Time magazine
A tremendous reward for my capture
Because I'm the most valuable player
One of the world's great men of color
Taught Hendrix how to play "Foxy Lady" Yet invisible
in my Eleganza ensemble
My tuxedo
My butt-nakedness at Attica
My tears frozen
in some rerun sequence
on somebody's telethon
I'm eating my pass to freedom
Once carefully forged
and now digested
My only meal for days
WILL WORK FOR FOOD
my latest poem
scrawled on Henry Brown's discarded box
A liquor company told me
I'm descended from great Kings and Queens: forty
ounces of black history anybody?
You can't catch me
I know all the black roads and alleys
The best restaurants
How to live high
on the hog
I invented chitlins and crack cocaine
A secret lab
behind where Thurgood Marshall plotted civil rights and
political casualties come to be consoled
Where the dismembered get stitched
And everything is everything
Doorman
to the best club in the world
where the passwords are
Freedom
Now
Changed my name
From Bailey to Stanley to Johnson to Douglass to Ida B.
Wells
Plotted with John Brown
Narrowly escaped the noose myself
Still running
All those European tours
Applauded and lauded
till they mistook me for an Arab
Got hooked on heroin and bebop
Started my own import export concern
Got busted for trafficking in literacy
Still doing time on that charge
Never should have preached about
David or Goliath
or how we need to boycott Denny's
This is written by myself
in blood if necessary
No Westside abolitionist
furiously working the laptop
on my behalf
scripting my punch lines
and designing my wardrobe
This is written in my mother's milk
Stronger than any formula
or synthetic decongestant
My voice is my own
No Richard and Willie act here
I write my own music too
The only tune I've ever covered
was the "Star Spangled Banner"
1983 NBA All Star Game
Remember?
I've gone from Jamestown
to Trenchtown
to Jonestown
Never did like Kool-Aid
Fought in every war invented and then some
Right now I'm fighting for the right
to peddle this knowledge
on this particular corner
at this particular time
Dime bags of truth, anybody?
Fugitive
In the jungles of Surinam
and the hills above South Central
awaiting an earthquake
or an insurrection:
whichever comes first
Meanwhile making myself heard
on the far end of the dial
in between
the shouts and screams
the grunts and sighs
the sirens and helicopters
Dogs
lapping at my scent
Chasing me since 1838
Up and down Malcolm X Boulevard
Somebody tell me
It's just a Spike Lee movie
Somebody tell me
why I just fired two rounds
into my own reflection
like some Narcissus gone mad
I've read the classics
Remember?
Spray painting my name
any name
on any wall that will have me
Outlaw
Gangsta rappa
Ph.D.
My dissertation lies unread
Trampled underneath the crowd
as they file out of Madison Square Garden
or the unemployment office
or the 4th of July celebration
where they just hanged two niggers for sport
Still I rise
From this nightmare called history
Cold sweats
in my cardboard box
my concrete crib
my room without a view
Dreamless nights
and endless days
Punching this heavy bag
like Louis
or Ali
like James Brown at the Apollo:
Out of confusion
Out of bondage
Up from slavery
Up from Maryland
Up from Mississippi
Up from the gutter
in which I'm lying right now
choking on my own filth
and the automotive exhaust
See me in your rearview mirror?
Now look into your future
Snap
into that virtual reality
Am I still preaching the gospel
on late night TV?
Pushing pancake batter?
Reading old slave narratives
as bedtime stories?
Putting America to sleep?
Fugitive
I've gone underground
Way underground
Burrowed underneath Mount Rushmore and Stone
Mountain Georgia
Got an inventory of all Confederate flags and colored
jockey statues
Closely monitoring the activities
of the brother
who took my mom's car keys on Crenshaw
and the brother
who put a knife to my lady's neck on Wilshire
and the brother
who pulled a gun on me
claiming to be an off-duty cop
in search of a stolen bicycle
and the brothers
who stomped my friend to death
in front of the Hollywood Palladium
and laughed
Something about a black leather jacket
Are my references too obscure?
Can you follow my drift?
In the Atlantic?
In the Caribbean?
In the creek
in chapter four
of Frederick Douglass's Native?
In an instant
poor Denby
was no more
His mangled body sank
out of sight
and blood
and brains
marked the water
where he had stood
The deed was done by a religious overseer named Gore
Hell of a baptism
But still I have risen
To fight the negro breaker
Jim Crow
Naysayers
and doomsayers
Enemies within
Supremacists of every stripe
My own self doubt
and suicidal tendencies:
You have seen
how a man was made a slave;
You shall see
how a slave was made a man
Armed with two fists
one mind
and a semi-colon
Dangerous
Devious
Made it to Tribeca in one day feeling as if I'd escaped a
den of lions
One of the lucky ones I suppose
So many more to follow
So many more to lead the way: Now take me to the
bridge
I'm ready.
```

---

## IC-1878: A Bone Close to My Brain

- Title: A Bone Close to My Brain
- Author (byline): Dan Dietz
- Work: Humana Festival 2004 Complete Plays, Pgs 16-23
- Publisher: Smith & Kraus
- Publication date as stated: April 2005
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: MAN
- Teaser before the introduction: Yes
- Spoken words (computed): 960
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dan Dietz
Book: Humana Festival 2004 Complete Plays, Pgs 16-23
ISBN: 978-1575253855
Publisher: Smith & Kraus
Date (Month/Year): April 2005
```

### Introduction (context only: never use it for content warnings)

```text
What are the limits of brotherly love? And what do they have to do with the 32 bones huddling tight inside your mouth? Through sparse dialogue and childlike illustrations, a man describes his relationship with his younger brother -- who is both brilliant and mentally ill -- and the heartbreaking decision he has to make.

A Bone Close to My Brain by Dan Dietz
```

### Performance text (classify this)

```text
NOTE: This is a play written in verse format Check event requirements for your tournament before entering in Poetry A MAN stands beside an easel; he uncaps a marker and draws a big tooth on the paper.

MAN: (Pg 16-23) today my brother is a dentist
he knows all about these little bones
huddling tight inside your mouth
incisors, bicuspids, wisdoms way in the back
he knows them all
their shapes and contours
their uses and misuses
the damage they can reasonably take
from impact or decay
my brother is a dentist today

i don't mean he just got certified
i don't mean he opened a practice
i mean that today my brother is a dentist
just like yesterday he was a radiologist
and last month he was a reporter for the new york
times
only two things about him stay the same
day in, day out
his address, this tidy little house in new jersey
which we've shared for the nine years
since our parents passed away
and the fact that i am his big brother
no matter what else he erases and remakes
inside his mind
these two facts sit solid and bonehard
within his head

MAN: he can't feed himself
he doesn't grasp the need to fuel his body
he can't bathe himself
left on his own, he'll either starve or stink himself
to death
he doesn't live in his skin, his stomach, his
fingernails
he lives here
in the bulbous gray organ
just above and behind
the roof of his mouth
that's his house

(MAN draws a roof and windows on the tooth, maybe even a chimney with smoke)

the rest of him
skin, stomach, fingernails
is like a yard (draws a yard by the house)
a yard that needs a full-time, round the dock
landscaper
to keep from going to hell
that's me
i tend him
he trusts me
anyone else comes near the yard
(skin, stomach, fingernails)
he screams, hits, bites
gets arrested, gets bailed out, forgets, etc.
but not me
he would never hurt me

except for today
today he will hurt me
in about ten minutes
he will walk in here
lay me down on this chair
and tear out of my head
a single, white, completely healthy
tooth (flips to a new sheet, draws a new tooth)
and i will let him

i can't get used to the way teeth look
strange
spiny
like they belong on the outside
of some prehistoric fish
not sprouting from my face
maybe i should smile more
but i was always that way
even as a kid
i can't find one picture of me
smiling showing my teeth
always just a twist of the lips
to indicate a grin
gerald always smiled with teeth
he's smiling right now
in the kitchen, sterilizing his instruments
which consist of a penlight
and a pair of pliers

he's brilliant
he learns this stuff in just hours
pores over textbooks
random ones i pick up
from the public library
to keep his house (draws a roof on the tooth, draws
a yard)
occupied (draws a happy stick figure waving from
the house)

he dives into the volumes
(the only medication he'll accept)
and the next time i see him
he's completely reborn
he's memorized it all
he's a dentist
(radiologist, reporter)
and he can't remember a day
when he wasn't a dentist
(radiologist, reporter)

he was reading tolstoy at age eight studying fractals at eleven those huge numbers blooming out infinite all over the place numbers that want to be pictures he called them

what does a number do if it wants to be a picture

he grew into adolescence
his head devouring everything
like his eyes were mouths
awards, acclaim
the "g" word tossed about
(and i don't mean "gerald")
by people important enough to believe
he was slated to graduate high school
before his sixteenth birthday

then mom and dad died
when our house
got broken into (draws a hole on the house and an
arrow pointing into the hole)
attempted robbery
became
attempted rape
became

i was away at college
i didn't have to come downstairs
didn't have to try to stop it
try to save
but gerald
he was fifteen
the same age as the boy
they caught and convicted
after finding his skin cells
beneath my mother's

i moved back home
took a break from school
gerald however refused to take a break
so close to graduation
less than a year
but the things he started saying
and doing

it was like his mind had twisted
to indicate a person (points to the person waving
from the house)
a person
that wants to be a picture
and he'll erase and try again
until he gets the picture
right
he's beautiful at night
he sits in his room
soft light
pages blurring by

he was expelled
for tearing open a substitute's blouse
he insisted she was in danger
her beat was irregular
he could hear it across the room
he had to press his stethoscope
to her bare chest to be sure

silly tragic moments are always so f***ing silly

like this one today

(flips to a new sheet, draws a new tooth) today my little brother will remove my tooth which he is convinced upon examination with his penlight is rife with decay

(draws holes on the tooth) little holes in a bone close to my brain

he will administer anesthetic
a rag steeped in ether
(which he got from god knows where)
and pluck out my tooth
("pluck" is probably not
the right word)
and smile
believing
he has saved me from danger
i will give him this belief
today
and tomorrow
i will take him to a place
where they will administer
a more sophisticated anesthetic
one which will
maybe
combined with other treatments
over the course of years
help

tomorrow i will turn him over to people who will break into his house

(draws a roof on the tooth, a yard, arrows pointing
into the holes in the tooth)
and do their best
as he flails and screams
to clean the damn thing up

i will leave him there i will erase him and

because i can't i

you wake up one day and the decay

i can't find myself in this picture

i will leave him there
and return here (turns to a fresh blank page)
to my house
and gerald
i know
will hold onto my tooth
forever
a bone close to my brain
perhaps it will reside
beneath his pillow
as he sleeps
giving him dreams
of his big brother
crying "don't hate me"

don't hate me

and perhaps
somewhere in the back of my mouth
i will feel the head
of my little brother shift
in the night
every night
after
tonight.
```

---

## IC-1879: Brutal Imagination

- Title: Brutal Imagination
- Author (byline): Cornelius Eady
- Work: Not specified
- Publisher: G.P. Putnam's Sons
- Publication date as stated: Feb 2001
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: IMAGINED BLACK MAN, SUSAN SMITH, LITTLE BOY
- Teaser before the introduction: Yes
- Spoken words (computed): 1560
- Already set (do not supply): none

### Source block (context only)

```text
Author: Cornelius Eady
ISBN: 978-0399147203
Publisher: G.P. Putnam's Sons
Date (Month/Year): Feb 2001
```

### Introduction (context only: never use it for content warnings)

```text
On October 25, 1994, 23-year-old Susan Smith, accused a man of kidnapping her two small boys. She said that a black gunman had jumped into her Mazda while she waited at a stoplight, forced her out of the car and drove away with her sons. Nine days later, she shocked the entire nation by confessing that she herself had driven her car, with the two children strapped in the back seat, into a lake.

Over a quarter of a century later, the investigation that took place and the headlines Susan’s lies created, have faded. But not for everyone . . . This selection poses the question: what if, at least during the nine days between the boys' disappearance and Ms. Smith's confession, the black man in her imagination actually existed? What would he have to say?

Brutal Imagination by Cornelius Eady
```

### Performance text (classify this)

```text
IMAGINED BLACK MAN: (Pg 5) Though it's common belief
That Susan Smith willed me alive
At the moment
Her babies sank into the lake

When called, I come.
A mother needs me clothed
In hand-me-downs
And a knit cap ???? Whatever.

SUSAN SMITH: (Pg 53-57) --When I left my home on Tuesday, October 25, I was very emotionally distraught

IMAGINED BLACK MAN: I have yet
To breathe.
I am in the back of her mind,
Not even a notion.
A scrap of cloth, the way
A man lopes down a street.

Later, a black woman will say:
"We knew exactly who she was describing."
At this point, I have no language,
No tongue, no mouth.
I am not me, yet.
I am just an understanding.

SUSAN SMITH: --I felt I couldn't be a good mom anymore, but I didn't want my children to grow up without a mom.

IMAGINED BLACK MAN: I am not me, yet.
At the bridge,
One of Susan's kids cries,
So she drives to the lake,
To the boat dock. . .
I am not yet opportunity.

SUSAN SMITH: --I wanted to end my life so bad
And was in my car ready to
Go down that ramp into
The water

IMAGINED BLACK MAN: My hand isn't her hand Panicked on the Emergency brake.

SUSAN SMITH: --And I did go part way, But I stopped. I then got out of the car.

IMAGINED BLACK MAN: Susan stares at the sinking.
My muscles aren't her muscles,
Burned from pushing.
The lake has no appetite,
But it takes the car slowly,
Swallow by swallow, like a snake.

Susan stares at the taillights
As they slide from here
To hidden.
******

IMAGINED BLACK MAN: (Pg 6) Susan Smith has invented me
because
Nobody else in town will do what
She needs me to do.
I mean: jump in an idling car
And drive off with two sad and
Frightened kids in the back.

She has given me a poisoned heart.
It pounds both our ribs, black, angry, nothing but
business.
Since her fear is my blood
And her need part mythical,
Everything she says about me is true.
******
(Pg 36-37) Susan fills our hands with plain objects,
Key, door handle, steering wheel,
But my hands are nothing:
A song you can't remember
The words to,
The button that pops
Off a vest, a comb that
Falls out of a pocket
Or purse.
Susan fills my lungs with air,
But what do I breathe out?
Parchment, ink, low growls, the
Blank gap between words.
Nothing fits upon my back,
Nothing actually catches my eye,
I am hidden and found,
I am North, South, East, West,
My dark skin porous, in-between.
Susan claims my name is muscle,
Bone, calls me tissue
And sinew, fills in my blank
With the absence of her boys,
But I am water, pebble,
Silt and gravity,
Evidence under her nail.
*******

LITTLE BOY: (Pg 7) --Who are you, mister?

IMAGINED BLACK MAN: One of the boys asks
From the eternal backseat
And here is the one good thing:
If I am alive then so, briefly, are they.
Two boys returned, three and one,
Quiet and scared, bunched together
Breathing like small beasts.
They can't place me, yet there's
Something familiar.
Though my skin and sex are different, maybe
It's the way I drive
Or occasionally glance back
With concern,
Maybe it's the mixed blessing
Someone, perhaps circumstance,
Has given us,
The secret thrill of hiding,
Childish, in plain sight,
Seen, but not seen,
As if suddenly given the power
To move through walls,
To know every secret without permission.
We roll sleepless through the dark streets, but inside
The cab is lit with brutal imagination.
******
(Pg 8-9) A few nights ago
A man swears he saw me pump gas
With the children
At a convenience store
Like a punchline you get the next day,
Or a kiss in a dream that returns while
You're in the middle of doing
Something else.
I left money in his hand.
Mr. who lives in ___
South Carolina,
Of average height
And a certain weight
Who may or may not
Believe in any of the
Basic recognized religions,
Saw me move like an angel
In my dusky skin
And knit hat.
Perhaps I looked him in the eye.

Ms. __ saw a glint of us
On which highway?
On the street that's close
To what landmark?
She now recalls
The two children in the back
Appeared to be behaving.
Mr. __ now knows he heard
The tires of the car
Everyone is looking for
Crunch the gravel
As I pulled up,
In the wee, wee hours
At the motel where
He works the night desk.
I signed or didn't sign the register.
I took or didn't take the key from his hand.

He looked or forgot to look
As I pulled off to park in front
Of one of the rooms at the back.
Did I say I was traveling with kids?
Who slept that night
In the untouched beds?
********
(Pg 18-19) How far do you think we'd have gotten
If I'd jumped in her car, a car I wanted
For who knows what,
A woman,
And not noticed the paraphernalia?
The rattles, the child's seat?
Had smelled the spills, the dried pee,
The cloudy musk of old formula?
Even if I had pushed her out, head wild
With all I guessed I'd taken,
How many minutes,
After my foot brushed a ball,
After my eyes cooled down and focused on
The rubble of play,
How many lights do you think I'd run
Before all the stuff they'd dropped
Over the years
Into the small cracks; the straws, the cold
Fries, the pacifier,
How long do you think the cops would listen
Had Susan not sworn
I was black, I was a bad dream,
The children didn't mean a thing
To that woman.
*******
(Pg 21) I am not the hero of this piece.
I am only a stray thought, a solution.
But now my face is stuck to lampposts, glued
To plate glass, my forehead gets stapled
To my hat.
I am here, and here I am not.
I am a door that opens, and out walks
No-one-can-help-you.
Now I gaze, straight into your eye,
From bulletin boards, tree trunks.
I am papered everywhere,
A blizzard called
You see what happens?

I turn up when least expected.
If you decide to buy some milk,
If you decide to wash your car,
If you decide to mail a letter,
I might tumbleweed onto a pant leg.
You can stare, and stare, but I can't be found.
Susan has loosed me on the neighbors,
A cold representative,
The scariest face you could think of.
*******
(Pg 39-40) The black man in town
They thought looked like me,
Without the dreamed-up cap
And wardrobe,
The police have him now.
He sits in a small room.
They turn him this way
And that.
He'll cool there for hours.
How do you think he feels?
I whisper we're innocent
Into his ears.

He looks so much like me,
We could be brothers.
Already, folks
May have their doubts:
He's poor enough.

Where has he been? He has his needs. What do they know? Susan has lent me His cheekbones, His gait. For a while, He is as close as They'll ever get. ******** (Pg 41) The sheriff reads off a list of things I have not done: I have not called on the phone. I did not discard the Childrens' clothing they found by the highway, I wasn't the man who robbed a convenience store In a car the same color as Susan's. I didn't drop Off the child they found, in Seattle, in a child's Seat like hers; the baby someone thought they Heard crying in the woods; not there, none of My doing.

Bloodhounds cannot catch a whiff of me. Divers
Rake the bottom of John D. Long Lake. I give
Them a snootful of silt. Who am I? Nothing
Says the sheriff, can be ruled out. A teenaged girl
Sees a man, covered in mud, walk out of the woods.
The heat sensors of the helicopter they send fail
To light my soggy footprints. Nothing can be
Dismissed. A psychic tumbles through a dream.
He nods as the children point everywhere but
In my direction. I am zip, my
Face and reasons an educated guess.
*********
(Pg 38) WHAT THE SHERIFF SUSPECTS . . .
Each time the town tells the sheriff
To look harder, my nose straightens and
My hair uncurls. I rustle like wind upon
The surface of a lake. I wink just
Below Susan's cheeks.
The sheriff has shuffled my deck all week.
So many miles, so many deeds.
I do not tire. I can't stop driving. I can
Wrangle kids in broad daylight and never
Be seen or heard. I'm not doing this for ransom.
When I'm about, things simply don't add up,
A short distance becomes too large, clocks run amok,
Stop signs change into traffic lights. Now he wonders
Why he's never noticed the way Susan's body can't sit
still,
My accent rising from her alibi.

CONCLUSION Unfounded criminal accusations across racial lines have a long history in the United States. The overwhelming majority of these cases have involved white accusers implicating black people, and the consequences have often been grievous. These hoaxes have one thing in common: The accusers are counting on stereotypes to distract the police and the public from what actually took place. In the end, these hoaxes are a clarion call, reminding us of the work we as a society still have to do to achieve racial justice.
```

---

## IC-1880: The Confession of St. Jim- Ralph

- Title: The Confession of St. Jim- Ralph
- Author (byline): Denis Johnson
- Work: The Throne of the Third Heaven of the National Millennium General Assembly: Poems Collected and New
- Publisher: Harper Collins
- Publication date as stated: 1995
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1735
- Already set (do not supply): none

### Source block (context only)

```text
Author: Denis Johnson
Book: The Throne of the Third Heaven of the National
Millennium General Assembly: Poems Collected
and New
ISBN: 978-0060926960
Publisher: Harper Collins
Date (Month/Year): 1995
```

### Introduction (context only: never use it for content warnings)

```text
Thus begins a poetic life story of a half-crazed eccentric who seems to have been throughout his life: a soldier, an rock star and religious zealot.. The Confession of St. Jim- Ralph by Denis Johnson
```

### Performance text (classify this)

```text
I used to sneak into the movies without paying. I watched the stories but I failed to see the dark. I went to college and drank everything they gave me, and I never paid for any of that water on which I drifted as if by grace until after the drownings, when in the diamond light of seven-something A.M., as the spring was tearing me up in Cartajena, only praying on my knees before the magnifying ark of the Seventh St. Hotel could possibly save me, until falling on my face before the daughter of money while the world poured from the till brought the moment’s length against the moment’s height, and paying was what I was earning and eating and wearing. This to the best of my recollection my uncle said in 1956, moving against my father like a bear on fire as the evening of his visit killed the rum. He’d come from Alaska or some place like that, the Antarctic, maybe, and he left in a hot rage, screaming by the door that nothing would save me from my awful father, just as he, my uncle, had been saved by nothing. Thirteen weeks from then, he died.

“This family’s full of the dead,” my father told me. I was eight. I used to make excuses to join him in the washroom as he bathed in the mornings, soaping himself carefully so as not to splash the automatic pistol wrapped in plastic he rested near to hand. At a certain point, the sun came through the blinds and shafted the toilet bowl, filling it with light as he spoke of killing everyone, often taking the pistol from its wrap and holding its mouth against his breast, explaining that no safety lay anywhere, unless he should shoot the fear that stood up on its hind legs in his heart. Such things were always on TV—I thought that one world merged in the next, and I resolved to win the great Congressional Medal of Honor, to make a name on the stage, and die a priest.

In the war the bullets yanked the fronds
from palms and the earth ate them up like acid
before our eyes. When dead men hit the ground
they came alive, they spoke in tongues, holding
babies that came from nowhere in their arms.
We were all afraid of the earth. My father’s fear
turned it like a plow, delivering
dogs and bugs, bright music, and a feminine
whispering of our names. My comrades fled,
but I was healed by everything that happened,
the midnight Rapid Transit stations
of hand grenades made moonlight as I moved
from life to life, getting off and shouting
whatever the signs said, getting on again,
received like lightning, changing everything.
My body disappeared. The enemy
knew me as a ghost who dropped a shadow
the size of night and turned the air to edges.
I am your grand companion of surprise,
big-time harbinger canceling everyone’s
business in a constant dream of all
the starring roles and franchises the great
Congressional Medal of Honor winners win.
Wounded twice, then decorated more
than any other in my regiment,
I stood at home plate, vomit on my blouse
and whiskey in my blood, and heard the dirt
of my home town falling grain by grain
out of the afternoon, while everyone’s
rahrahrahs affected me like silence.
The mayor handed me a four-by-four-
inch cardboard box a colonel handed him;
I threw it at the vast face of the crowd,
screaming I wanted only the Medal of Honor …
I lose the thread of my existence here.
I see me strange and drugged against my will,
telling my life story to a room,
traveling the aisles of an asylum
out there in Maine, among the aborigines.
They must have set me loose, or I escaped:
I see myself in a forest-bordered field,
unchanged and wearing my uniform—
free; yet somehow jailed by old desires
and saying what a soldier says: For home,
nothing. Comrades, for you, these hoarded rations.

With four monstrosities in uniforms
like mine, I pulverized guitars and wept
for the merriment of many. Brothers,
when shadows lengthen, and they lower down
the American flag and close our government,
another country rises like a mist
by garbagey coliseums on the warehouse
side of town to listen to that rock
and roll: God speaking with the Devil’s voice,
unbreathable air of manacles, a storm
to bless your multicolored lips.
We sundered them until they brought their bones
forth from the flesh and laid them at our feet,
screaming their lungs shut tight as fists,
shedding their homes forever, leaving name
and tongue and mind and sending us their heads
through the mails in the night. We ran it past the edge,
we gave them something everyone could dance to—
whatever is most terrible is most real—
the Bible fights, the fetuses burning in light-bulbs.

Three times I died on stage,
and the show went on while doctors snatched
me back from Chinatown with their machines.
We struck it rich. Without a repertoire,
without a name or theme, we toured the land
and eighty thousand perished. We were real,
but not one company recorded us:
everywhere we went they passed a law.
We toured the land—sweet, burning Texacos,
the adrenaline darkness palpitates frantically,
the highway eats itself all night, the radio’s
wheedling bebop fails in the galactic
soup near dawn; the Winnebago shimmers.
One night I heard our music end
abruptly in the middle of a number
and looked around me at a gigantic silence.
I felt the pounding, saw the screams, but all
was like the long erasure of a wind
calming and disturbing everything
on its route through stunned fields of hay.
My bodyguards tried with huge gentleness to lead
me off, but I threw myself outside, rolling
through a part of town I’d never seen—
the flat gray streets looked Hebrew, and the windows
held out the paraphernalia of old age,
porcelain Jesuses gesturing from the shadows
of porcelain vases, surrounded by medicines.
A rain began. I strained myself to hear
the trashcans say their miserable names,
but nothing. At the brink
of stardom high over the United States,
untouchable as God but better known,
I stumbled over streets that might’ve been rubber,
deaf as a cockroach, finished as a singer.

Brothers, I spilled myself along the roads.
Mold grew on me as I dampened in alleys.
I began in ignorance. How could I know
that whoever is grinding up his soul is making
himself afresh? That the ones who run away
get nearer all the time? Look here or there,
it’s always the horizon, the dull edge
of earth dicing your plan like a potato.
Does water break the light, or light the water?
Which do you choose: what is or what is?
I lied. I cheated like a shark. I robbed the dead.
Nothing healed me, just as nothing healed
my uncle of himself—but he was healed,
while I grew phosphorescent with a kind
of cancer that I carried like a domino,
a tiny badge discovering me …
Oh please my love I want to rock and roll with you
Feel it feel it
feel it all night like a shoe …
Ten years I wasted all I had, and then
ten years I lived correctly—held a job
in a factory that made explosions,
where deafness was an asset. I did well,
I never missed a day, I polished late,
honed my skills, received promotions—in the end
I built explosions for atomic bombs,
forty-three I built myself, which one of these
days will deafen you, as I am deafened.

I wrenched the fraternal orders with my tale
of sorrowful delinquency—the Elks,
the Lions, Moose; those animals, they loved
the crippled rock’n’roller with the heart
wrung out as empty as his former mind,
and variously and often they cited me.
I walked the malls with an expanded chest,
yearning for the strength of soul it takes
to suck a bullet from an actual
pistol, hating my own drained face
as I intimidated mirrors, or stood
in a jail of lies before the Eagle Scouts,
an alarm clock going off inside an alarm clock
in a lump of iron inside a lump of iron:
hating myself for having become my father.
At night I prayed aloud to God and Jesus
to place me on a spaceship to the moon—
Heaven, I told Them constantly, my mind
is tired of me, and I would like to die.
There I fell on my face, and let light carry
me into the world—just as my uncle told it
nine million years ago when I was eight—
a little boy
in a baseball cap and pajamas, doing things
to the locks of the heart … This was my vision.
Here I saw the truth of the horizon,
the way of coming and going in this life.
I never drifted up from my beginning:
I rose as inexorably as heat.

Brothers, I reached you, and you took me in.
You saw me when I was invisible,
you spoke to me when I was deaf,
you thanked me when I was a secret,
and how will I make of myself something
at this hour when I am already made?
Never a famous hero, a star, a priest—
my mind decides a little faster than
the world can talk, and what I dreamed was only
the darker sketch of what I would become.
It’s 1996. I’m forty-eight.
I am a monk who never prays. I am
a prayer. The pilgrim comes to hear me;
the banker comes, the bald janitors arrive,
the mothers lift their wicked children up—
they wait for me as if I were a bus,
with or without hope, what’s the difference?
One guy manipulates a little calculator,
speaking to it as to a friend. Sweat
is delivered from its mascara,
sad women read about houses …
and now the deaf approach, trailing the dark smoke
of their infirmity behind them as they leave it
and move toward the prayer that everything
is praying: the summer evening a held bubble,
every gesture riveting the love,
the swaying of waitresses, the eleven television
sets in a storefront broadcasting a murderer’s face—
these things speak the clear promise of Heaven.
```
